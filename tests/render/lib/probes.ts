import type { Page } from '@playwright/test';

/**
 * Scroll the full page in viewport-sized steps so lazy-loaded images fetch,
 * wait for every image to settle, then return to the top.
 * Required before any IMG check — below-fold images are otherwise unloaded.
 */
export async function settlePage(page: Page): Promise<{ pending: number }> {
  // Force every lazy image to fetch BEFORE scrolling.
  //
  // Scrolling alone does not do it: measured on /congo-african-grey-for-sale/,
  // a full-page scroll left 45 of 52 images with complete === false, zero HTTP
  // 4xx, and they stayed unloaded after a further 15 seconds. All 45 were
  // ordinary loading="lazy" images — visible, real widths, not inside <details>.
  // Chromium never commits a lazy load when the viewport passes that fast, and
  // returning to the top drops the pending ones. The consequence was that
  // img-srcset-within-2x examined 7 of 52 images and called the page clean.
  //
  // We measure the assets a page SHIPS, not the order a browser happens to
  // fetch them in, so eager is the honest setting here — and it is
  // deterministic, where the scroll race was not.
  await page.evaluate(() => {
    for (const img of Array.from(document.images)) {
      if (img.getAttribute('loading') === 'lazy') img.setAttribute('loading', 'eager');
    }
  });

  await page.evaluate(async () => {
    const step = window.innerHeight;
    // Re-read scrollHeight each iteration: the document GROWS while settling
    // (measured +611px on the corpus page), so a height cached up front stops
    // the loop short of the real bottom. Iteration cap guards a page that grows
    // faster than we scroll.
    for (let y = 0, i = 0; y < document.body.scrollHeight && i < 400; y += step, i++) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 30));
    }
    window.scrollTo(0, 0);
  });

  // BOUNDED. An image that never loads and never errors fires neither onload nor
  // onerror, so an unbounded Promise.all here hangs until the test timeout —
  // measured on /congo-african-grey-for-sale/, where it stalled both IMG checks
  // past 45s and killed the page's results entirely. A page whose results never
  // get written scores as absent rather than as failed, which is the worst
  // failure mode this harness has. Never let this wait be unbounded.
  const pending = await page.evaluate(async () => {
    const incomplete = Array.from(document.images).filter((i) => !i.complete);
    await Promise.race([
      Promise.all(
        incomplete.map(
          (i) =>
            new Promise((res) => {
              i.onload = i.onerror = () => res(null);
            }),
        ),
      ),
      new Promise((res) => setTimeout(res, 3000)),
    ]);
    return Array.from(document.images).filter((i) => !i.complete).length;
  });

  await page.waitForTimeout(150);
  // Callers may surface this; the IMG checks already report any image that
  // failed to decode, so a stuck image becomes a defect rather than a hang.
  return { pending };
}

export interface TopChrome {
  /** Height in px of the band of pinned chrome at the top of the viewport. */
  height: number;
  /** What was counted, for reports — a bare number hides why it is wrong. */
  parts: { tag: string; cls: string; height: number }[];
  /** True when chrome exceeds 40% of the viewport; the caller should treat this as a defect, not a measurement. */
  implausible: boolean;
}

/**
 * Height of the sticky/fixed chrome band pinned to the top of the viewport
 * (header + any jump rail). Measured, never assumed — one page had five
 * `var(--hdr, 72px)` fallbacks against a header that measures 96px.
 *
 * Two things this gets right that the obvious implementation does not, both
 * found by measuring the congo-pair page rather than by reading its CSS:
 *
 * 1. MUST SCROLL FIRST. A rail with `top: var(--hdr)` is not pinned at
 *    scrollY 0 — measured at rest it sits at top:1030, far down the document.
 *    Measuring without scrolling returns 96 (header only) and misses a 55px
 *    rail, so anchor targets landing *behind the rail* score as correct.
 * 2. MUST ACCUMULATE. Chrome stacks: the header pins at 0, the rail pins at
 *    the header's bottom. A `box.top <= 2` filter sees only the header. The
 *    band is grown iteratively — absorb anything whose top touches the band
 *    so far, and repeat until nothing more is absorbed.
 */
export async function measureTopChrome(page: Page): Promise<TopChrome> {
  // Pin whatever pins. 1.5 viewports is past every sticky trigger on this site.
  await page.evaluate(() => window.scrollBy(0, Math.round(window.innerHeight * 1.5)));
  await page.waitForTimeout(250);

  const result = await page.evaluate(() => {
    const candidates: { tag: string; cls: string; top: number; bottom: number }[] = [];
    for (const el of Array.from(document.body.querySelectorAll<HTMLElement>('*'))) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      if (cs.visibility === 'hidden' || cs.display === 'none') continue;
      if (parseFloat(cs.opacity) === 0) continue;
      const box = el.getBoundingClientRect();
      if (box.height === 0 || box.width === 0) continue;
      // must actually span the viewport horizontally — excludes off-canvas drawers
      if (box.right <= 0 || box.left >= window.innerWidth) continue;
      candidates.push({
        tag: el.tagName.toLowerCase(),
        cls: (el.className || '').toString().trim().split(/\s+/).slice(0, 2).join(' '),
        top: box.top,
        bottom: box.bottom,
      });
    }

    // Grow the band: start at the viewport top, absorb anything touching it, repeat.
    let band = 0;
    const parts: { tag: string; cls: string; height: number }[] = [];
    const used = new Set<number>();
    let grew = true;
    while (grew) {
      grew = false;
      candidates.forEach((c, i) => {
        if (used.has(i)) return;
        if (c.top <= band + 2 && c.bottom > band) {
          parts.push({ tag: c.tag, cls: c.cls, height: Math.round(c.bottom - c.top) });
          band = c.bottom;
          used.add(i);
          grew = true;
        }
      });
    }

    return {
      height: Math.round(band),
      parts,
      implausible: band > window.innerHeight * 0.4,
    };
  });

  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(120);
  return result;
}

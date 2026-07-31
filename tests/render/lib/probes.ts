import type { Page } from '@playwright/test';

/**
 * Scroll the full page in viewport-sized steps so lazy-loaded images fetch,
 * wait for every image to settle, then return to the top.
 * Required before any IMG check — below-fold images are otherwise unloaded.
 */
export async function settlePage(page: Page): Promise<void> {
  await page.evaluate(async () => {
    const step = window.innerHeight;
    const total = document.body.scrollHeight;
    for (let y = 0; y < total; y += step) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 30));
    }
    window.scrollTo(0, 0);
  });
  await page.evaluate(
    () =>
      Promise.all(
        Array.from(document.images)
          .filter((i) => !i.complete)
          .map(
            (i) =>
              new Promise((res) => {
                i.onload = i.onerror = () => res(null);
              }),
          ),
      ),
  );
  await page.waitForTimeout(200);
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

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

  // Instant, not `scrollTo(0, 0)`. That plain form is smooth-ANIMATED under the site's
  // global `html{scroll-behavior:smooth}` — the exact shape of the bug removed from
  // nav.ts. It happened to be harmless here only because this animation's destination is
  // also 0, so it was safe by coincidence rather than by design. Left as-is it is the
  // nearest wrong pattern for the next reader to copy, one function above its own fix.
  await resetScrollInstant(page);
  return result;
}

/**
 * Return to the top with NO animation, whatever `scroll-behavior` the page declares.
 *
 * `window.scrollTo(0, 0)` is itself smooth-animated under `html{scroll-behavior:smooth}`,
 * which every page on this site sets. The previous NAV check reset that way and clicked
 * 80ms later — starting a fragment navigation while a full-document smooth scroll was
 * still in flight. `behavior:'instant'` overrides the computed style; `'auto'` does not
 * (in ScrollOptions, 'auto' means "use the computed style", which is the trap).
 */
export async function resetScrollInstant(page: Page): Promise<void> {
  // An instant scroll sets scrollY to 0 SYNCHRONOUSLY but does not CANCEL an animation
  // already in flight. Measured: a smooth scroll toward 20000 interrupted at y=1213 read
  // 0 immediately, then resurrected to 485 one frame later and stayed there. So the wait
  // below is not decoration — it is the window in which a surviving animation reveals
  // itself, and re-asserting afterwards is what stops one slow target from contaminating
  // the next one's landing measurement.
  for (let attempt = 0; attempt < 3; attempt++) {
    await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' as ScrollBehavior }));
    await page.waitForTimeout(50);
    if ((await page.evaluate(() => window.scrollY)) === 0) return;
  }
}

export interface ScrollSettle {
  y: number;
  /** False means it was still moving when the budget ran out — that is a finding, not a landing. */
  settled: boolean;
  ms: number;
  /**
   * Pixels moved over the final tick. Only meaningful when `settled` is false, where it
   * separates "the page never started scrolling" (0, at y=0 — a real page defect) from
   * "the page is still travelling and our budget was too short" (non-zero — OUR defect).
   * Without it both look identical in the scorecard, which is the confusion this whole
   * check was rewritten to remove.
   */
  lastDeltaPx: number;
}

/**
 * Poll until `scrollY` stops changing, or give up and say so.
 *
 * Replaces a fixed 1200ms wait, which is simultaneously too long for an instant jump and
 * too short for a smooth scroll across 26,000px — so it reported false failures on slow
 * pages and wasted 20 minutes per run on fast ones.
 *
 * Polls with setTimeout, not requestAnimationFrame: rAF is throttled to a stop in a page
 * that is not painting, and a probe that silently never ticks reports `settled:false` on a
 * page that is perfectly fine. See MEMORY reference_intersectionobserver_needs_painting_page.
 */
export async function waitForScrollSettle(
  page: Page,
  opts: { maxMs?: number; stableTicks?: number; tickMs?: number } = {},
): Promise<ScrollSettle> {
  // 3000ms, not 5000. Chromium caps programmatic smooth-scroll DURATION rather than
  // scaling it with distance — measured on this harness's own fixture, 23,284px took
  // 1494ms and 11,984px took 1496ms. 3000 is ~2x the observed worst case, and the ceiling
  // matters because pages.spec runs every check for one page+viewport inside a single
  // 120s test: at 5000ms, 18 targets could spend 90s in NAV alone, blow the test timeout,
  // and write no partial — and a page with no partial scores ABSENT rather than failed,
  // which probes.ts already calls the worst failure mode this harness has.
  const { maxMs = 3000, stableTicks = 5, tickMs = 32 } = opts;
  return page.evaluate(
    ({ maxMs, stableTicks, tickMs }) =>
      new Promise<{ y: number; settled: boolean; ms: number; lastDeltaPx: number }>((resolve) => {
        const t0 = Date.now();
        let last = window.scrollY;
        let stable = 0;
        let lastDeltaPx = 0;
        const tick = () => {
          const y = window.scrollY;
          if (y === last) stable++;
          else {
            stable = 0;
            lastDeltaPx = Math.abs(y - last);
            last = y;
          }
          const ms = Date.now() - t0;
          if (stable >= stableTicks) return resolve({ y, settled: true, ms, lastDeltaPx });
          if (ms >= maxMs) return resolve({ y, settled: false, ms, lastDeltaPx });
          setTimeout(tick, tickMs);
        };
        setTimeout(tick, tickMs);
      }),
    { maxMs, stableTicks, tickMs },
  );
}

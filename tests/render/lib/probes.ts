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

/**
 * Height in px of sticky/fixed chrome pinned to the top of the viewport
 * (header + any jump rail). Measured, never assumed — one page had five
 * `var(--hdr, 72px)` fallbacks against a header that measures 96px.
 */
export async function measureTopChrome(page: Page): Promise<number> {
  return page.evaluate(() => {
    let bottom = 0;
    for (const el of Array.from(document.body.querySelectorAll<HTMLElement>('*'))) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const box = el.getBoundingClientRect();
      if (box.height === 0 || box.width === 0) continue;
      // pinned at the top, and not a full-screen overlay
      if (box.top <= 2 && box.bottom > bottom && box.bottom < window.innerHeight / 2) {
        bottom = box.bottom;
      }
    }
    return Math.round(bottom);
  });
}

import { register, type CheckResult } from '../lib/registry.js';
import type { Page } from '@playwright/test';

register({
  id: 'layout-no-horizontal-overflow',
  family: 'LAYOUT',
  severity: 'advisory',
  describe: 'the document must not scroll sideways at any viewport',
  // This check judges exactly ONE unit: the document's own overflow measurement.
  // The per-element walk below runs only to NAME offenders, never to decide.
  // That keeps it free of false positives from intentionally-translated
  // decorative elements — but it also means the fixture pair is this check's
  // only real protection, so never weaken the fixtures.
  minExamined: 1,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const de = document.documentElement;
      const limit = de.clientWidth;
      const overflow = de.scrollWidth - limit;
      const offenders: string[] = [];
      if (overflow > 1) {
        for (const el of Array.from(document.body.querySelectorAll<HTMLElement>('*'))) {
          if (getComputedStyle(el).position === 'fixed') continue;
          const box = el.getBoundingClientRect();
          if (box.width === 0 || box.height === 0) continue;
          if (box.right > limit + 1) {
            const cls =
              typeof el.className === 'string' && el.className.trim()
                ? '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.')
                : '';
            offenders.push(`${el.tagName.toLowerCase()}${cls}@${Math.round(box.right)}px`);
          }
        }
      }
      return { overflow, offenders: offenders.slice(0, 8) };
    });

    return {
      examined: 1,
      defects:
        r.overflow > 1
          ? [
              {
                checkId: 'layout-no-horizontal-overflow',
                family: 'LAYOUT' as const,
                viewport,
                count: 1,
                message: `document overflows by ${r.overflow}px — offenders: ${
                  r.offenders.join(' | ') || 'none isolated'
                }`,
              },
            ]
          : [],
    };
  },
});

register({
  id: 'layout-min-font-size',
  family: 'LAYOUT',
  severity: 'advisory',
  describe: 'no visible text may render below 12.5px',
  // 12.5 was questioned on 2026-08-01: 88 declarations of `.78rem` compute to 12.48px
  // and fail by 0.02px, which reads like a rounding artifact, and the backlog advised
  // exempting them. It is not an artifact — `.78rem` is the single most-used small size
  // in this codebase (88 declarations across 17 files), so moving the threshold to 12.4
  // would retire the check's LARGEST cohort permanently and leave it unable to speak
  // about that band again. The threshold stayed; the codebase moved to `--fs-micro`
  // (0.79rem = 12.64px). Do not lower this number to make a sweep smaller.
  minExamined: 3,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      let examined = 0;
      const bad: string[] = [];
      let node: Node | null;
      while ((node = walker.nextNode())) {
        const text = (node.textContent || '').trim();
        if (!text) continue;
        const el = node.parentElement;
        if (!el) continue;
        // getClientRects() is empty when ANY ancestor is display:none
        if (el.getClientRects().length === 0) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden') continue;
        examined++;
        const size = parseFloat(cs.fontSize);
        if (size < 12.5) {
          bad.push(`${el.tagName.toLowerCase()} ${size}px "${text.slice(0, 30)}"`);
        }
      }
      return { examined, bad: bad.slice(0, 10), count: bad.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'layout-min-font-size',
              family: 'LAYOUT' as const,
              viewport,
              count: r.count,
              message: `${r.count} text node(s) below 12.5px: ${r.bad.join(' | ')}`,
            },
          ]
        : [],
    };
  },
});

register({
  id: 'layout-tap-target-size',
  family: 'LAYOUT',
  severity: 'advisory',
  describe: 'every visible interactive control is at least 24x24px',
  minExamined: 2,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const sel = 'a[href], button, input:not([type=hidden]), select, textarea, [role=button]';
      const nodes = Array.from(document.querySelectorAll<HTMLElement>(sel));
      let examined = 0;
      const bad: string[] = [];
      for (const el of nodes) {
        if (el.getClientRects().length === 0) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden') continue;
        const box = el.getBoundingClientRect();
        if (box.width === 0 || box.height === 0) continue;
        examined++;
        if (box.width < 24 || box.height < 24) {
          const label = (el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 24);
          bad.push(
            `${el.tagName.toLowerCase()} ${Math.round(box.width)}x${Math.round(box.height)} "${label}"`,
          );
        }
      }
      return { examined, bad: bad.slice(0, 10), count: bad.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'layout-tap-target-size',
              family: 'LAYOUT' as const,
              viewport,
              count: r.count,
              message: `${r.count} control(s) under 24x24: ${r.bad.join(' | ')}`,
            },
          ]
        : [],
    };
  },
});

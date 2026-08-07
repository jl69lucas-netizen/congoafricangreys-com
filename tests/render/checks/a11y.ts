import { register, type CheckResult } from '../lib/registry.js';
import type { Page } from '@playwright/test';

/**
 * A11Y family. Contrast is computed from RENDERED colours, never from source.
 *
 * The bug class this exists for is "component re-themed, child not": `.bpair` flipped the
 * dial to a white bed and `.ti` kept its dark-theme sage `#7ba98d` — 2.66:1, ten Lighthouse
 * failures on 2026-08-07. A source grep cannot see that, because neither declaration is
 * wrong on its own; only the composed result is. See reference_markup_css_drift.
 *
 * What it deliberately does NOT judge, because it cannot do so honestly:
 *  - text over a background-image or gradient (no single backdrop colour exists)
 *  - text over a semi-transparent layer (the composite depends on paint order)
 *  - zero-area, hidden, or fully-transparent elements
 * Skipping is not the same as passing: skipped elements are excluded from `examined`, so
 * the count reports what the predicate actually ran against.
 */
register({
  id: 'a11y-text-contrast-aa',
  family: 'A11Y',
  severity: 'blocking',
  describe: 'rendered text must meet WCAG AA contrast against its own backdrop',
  // The known_broken fixture carries 4 judgeable spans (2 failing, 2 passing); the floor is
  // set to that so the check cannot pass the meta gate by judging one element and skipping
  // the rest. reference_promote_check_needs_examined_count.
  minExamined: 4,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const rgb = (s: string): number[] | null => {
        const m = (s.match(/[\d.]+/g) || []).map(Number);
        if (m.length < 3) return null;
        if (m.length >= 4 && m[3] === 0) return null; // fully transparent
        return m.slice(0, 3);
      };
      const lum = (c: number[]) => {
        const [r, g, b] = c.map((v) => {
          const x = v / 255;
          return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4);
        });
        return 0.2126 * r + 0.7152 * g + 0.0722 * b;
      };

      /** The nearest OPAQUE backdrop, or null when no honest answer exists. */
      const backdrop = (el: Element): number[] | null => {
        let n: Element | null = el;
        while (n && n !== document.documentElement) {
          const cs = getComputedStyle(n);
          if (cs.backgroundImage && cs.backgroundImage !== 'none') return null;
          const parts = (cs.backgroundColor.match(/[\d.]+/g) || []).map(Number);
          if (parts.length >= 3) {
            const alpha = parts.length >= 4 ? parts[3] : 1;
            if (alpha === 1) return parts.slice(0, 3);
            if (alpha > 0) return null; // translucent layer — composite is paint-order dependent
          }
          n = n.parentElement;
        }
        const root = (getComputedStyle(document.documentElement).backgroundColor.match(/[\d.]+/g) || []).map(Number);
        return root.length >= 3 && (root.length < 4 || root[3] === 1) ? root.slice(0, 3) : [255, 255, 255];
      };

      const fails: { sel: string; text: string; ratio: number; need: number }[] = [];
      let examined = 0;

      for (const el of Array.from(document.body.querySelectorAll('*'))) {
        // Only elements with their OWN text. Judging containers would count the same
        // string once per ancestor and inflate the count with units never evaluated.
        const own = Array.from(el.childNodes)
          .filter((n) => n.nodeType === 3 && (n.textContent ?? '').trim().length > 0)
          .map((n) => (n.textContent ?? '').trim())
          .join(' ');
        if (!own) continue;

        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden' || cs.display === 'none' || Number(cs.opacity) === 0) continue;
        const box = (el as HTMLElement).getBoundingClientRect();
        if (box.width === 0 || box.height === 0) continue;

        const fg = rgb(cs.color);
        if (!fg) continue;
        const bg = backdrop(el);
        if (!bg) continue; // image/gradient/translucent backdrop — not judgeable

        const size = parseFloat(cs.fontSize);
        const weight = Number(cs.fontWeight) || 400;
        const large = size >= 24 || (size >= 18.66 && weight >= 700);
        const need = large ? 3 : 4.5;

        const lf = lum(fg);
        const lb = lum(bg);
        const ratio = (Math.max(lf, lb) + 0.05) / (Math.min(lf, lb) + 0.05);
        examined++;

        if (ratio < need - 0.005) {
          const cls =
            typeof el.className === 'string' && el.className.trim()
              ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.')
              : el.tagName.toLowerCase();
          fails.push({ sel: cls, text: own.slice(0, 24), ratio: Math.round(ratio * 100) / 100, need });
        }
      }
      return { examined, fails: fails.slice(0, 6), total: fails.length };
    });

    return {
      examined: r.examined,
      defects: r.total
        ? [
            {
              checkId: 'a11y-text-contrast-aa',
              family: 'A11Y' as const,
              viewport,
              count: r.total,
              message: `${r.total} text node(s) below AA: ${r.fails
                .map((f) => `${f.sel} "${f.text}" ${f.ratio}:1 (needs ${f.need})`)
                .join(' | ')}`,
            },
          ]
        : [],
    };
  },
});

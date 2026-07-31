import { register, type CheckResult } from '../lib/registry.js';
import { settlePage } from '../lib/probes.js';
import type { Page } from '@playwright/test';

register({
  id: 'img-srcset-within-2x',
  family: 'IMG',
  severity: 'blocking',
  describe: 'no image may decode at more than 2x the width it paints at',
  minExamined: 1,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    await settlePage(page);
    const r = await page.evaluate(() => {
      const dpr = window.devicePixelRatio || 1;
      let examined = 0;
      const bad: string[] = [];
      const skipped: string[] = [];
      for (const img of Array.from(document.images)) {
        const box = img.getBoundingClientRect();
        if (box.width < 1) continue;
        if (!img.complete || img.naturalWidth === 0) {
          // A 404'd image has complete === true and naturalWidth === 0.
          // Silently dropping it is how a broken page scores clean, so surface it.
          skipped.push((img.currentSrc || img.src || '(no src)').split('/').pop() as string);
          continue;
        }
        examined++;
        const ratio = img.naturalWidth / (box.width * dpr);
        if (ratio > 2.0) {
          const file = (img.currentSrc || img.src).split('/').pop();
          bad.push(
            `${file} natural=${img.naturalWidth} painted=${Math.round(box.width)} ${ratio.toFixed(2)}x`,
          );
        }
      }
      return { examined, bad: bad.slice(0, 10), count: bad.length, skipped: skipped.slice(0, 10) };
    });

    const defects = [];
    if (r.count) {
      defects.push({
        checkId: 'img-srcset-within-2x',
        family: 'IMG' as const,
        viewport,
        message: `${r.count} oversized image(s): ${r.bad.join(' | ')}`,
      });
    }
    if (r.skipped.length) {
      defects.push({
        checkId: 'img-srcset-within-2x',
        family: 'IMG' as const,
        viewport,
        message: `${r.skipped.length} image(s) failed to decode and could not be measured: ${r.skipped.join(', ')}`,
      });
    }
    return { examined: r.examined, defects };
  },
});

register({
  id: 'img-alt-present-and-unique',
  family: 'IMG',
  severity: 'advisory',
  describe: 'every rendered image declares alt; non-decorative alts are unique on the page',
  minExamined: 3,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    await settlePage(page);
    const r = await page.evaluate(() => {
      let examined = 0;
      const missing: string[] = [];
      const seen = new Map<string, number>();
      for (const img of Array.from(document.images)) {
        if (img.getBoundingClientRect().width < 1) continue;
        examined++;
        if (!img.hasAttribute('alt')) {
          missing.push(((img.getAttribute('src') || '(no src)').split('/').pop()) as string);
          continue;
        }
        const alt = (img.getAttribute('alt') || '').trim();
        if (alt === '') continue; // declared decorative — allowed
        seen.set(alt, (seen.get(alt) || 0) + 1);
      }
      const dupes: string[] = [];
      seen.forEach((n, alt) => {
        if (n > 1) dupes.push(`"${alt.slice(0, 48)}" x${n}`);
      });
      return { examined, missing: missing.slice(0, 6), dupes: dupes.slice(0, 6) };
    });

    const defects = [];
    if (r.missing.length) {
      defects.push({
        checkId: 'img-alt-present-and-unique',
        family: 'IMG' as const,
        viewport,
        message: `image(s) with no alt attribute: ${r.missing.join(', ')}`,
      });
    }
    if (r.dupes.length) {
      defects.push({
        checkId: 'img-alt-present-and-unique',
        family: 'IMG' as const,
        viewport,
        message: `duplicate alt text (Rule 50b): ${r.dupes.join(' | ')}`,
      });
    }
    return { examined: r.examined, defects };
  },
});

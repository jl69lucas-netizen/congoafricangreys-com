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
      // skippedTotal is derived BEFORE the slice, for the same reason `count` is:
      // a row's count must be the true magnitude, never the length of a list that
      // was truncated for readability. Phase 2 swept two checks for exactly this
      // and the comment below claimed both were the only stragglers — `skipped`
      // was a third, and reported 10 whenever 10 or more images failed to decode.
      return {
        examined,
        bad: bad.slice(0, 10),
        count: bad.length,
        skipped: skipped.slice(0, 10),
        skippedTotal: skipped.length,
      };
    });

    const defects = [];
    if (r.count) {
      defects.push({
        checkId: 'img-srcset-within-2x',
        family: 'IMG' as const,
        viewport,
        count: r.count,
        message: `${r.count} oversized image(s): ${r.bad.join(' | ')}`,
      });
    }
    if (r.skippedTotal) {
      defects.push({
        checkId: 'img-srcset-within-2x',
        family: 'IMG' as const,
        viewport,
        count: r.skippedTotal,
        message: `${r.skippedTotal} image(s) failed to decode and could not be measured: ${r.skipped.join(', ')}${
          r.skippedTotal > r.skipped.length ? ` (+${r.skippedTotal - r.skipped.length} more)` : ''
        }`,
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
      // Return the true totals ALONGSIDE the truncated display lists. `count` is the
      // magnitude the ledger ranks families by, so deriving it from a list already
      // sliced for readability would silently cap this check's contribution at 6 —
      // undercounting exactly the field that was just made load-bearing, and doing it
      // invisibly, since a capped number looks like a small problem rather than a
      // truncated one. img-srcset-within-2x already returns a separate `count` for
      // this reason; these two were the stragglers.
      //
      // CORRECTION (2026-08-01): "these two were the stragglers" was false when
      // written. img-srcset-within-2x returned a separate `count` for its OVERSIZED
      // row but derived its decode-failure row's count from `skipped.slice(0, 10)`,
      // so it reported 10 whenever 10 or more images failed. A comment asserting a
      // safety property the code lacks is worse than no comment — it is why that
      // third case survived a dedicated sweep for exactly this defect.
      return {
        examined,
        missing: missing.slice(0, 6),
        missingTotal: missing.length,
        dupes: dupes.slice(0, 6),
        dupesTotal: dupes.length,
      };
    });

    const defects = [];
    if (r.missing.length) {
      defects.push({
        checkId: 'img-alt-present-and-unique',
        family: 'IMG' as const,
        viewport,
        count: r.missingTotal,
        message: `image(s) with no alt attribute: ${r.missing.join(', ')}`,
      });
    }
    if (r.dupes.length) {
      defects.push({
        checkId: 'img-alt-present-and-unique',
        family: 'IMG' as const,
        viewport,
        count: r.dupesTotal,
        message: `duplicate alt text (Rule 50b): ${r.dupes.join(' | ')}`,
      });
    }
    return { examined: r.examined, defects };
  },
});

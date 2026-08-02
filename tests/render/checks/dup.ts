import { register, type CheckContext, type CheckResult } from '../lib/registry.js';
import { loadWhitelist, normalise } from '../lib/dupCorpus.js';
import type { Page } from '@playwright/test';

/** The Python auditor's window. Changing it here without changing it there splits the gate. */
const MIN_WORDS = 12;

/**
 * DUP: no page may share a run of copy with a sibling.
 *
 * Chosen over reimplementing the whole auditor in TypeScript: the SHINGLING is fifteen
 * lines and reimplementing it costs nothing, but the WHITELIST is the tuned artefact —
 * it encodes exactly which lines CLAUDE.md mandates as identical across siblings, and a
 * second copy of it would drift the first time either was tuned. So the comparison is
 * local (fast, and its failure messages are the harness's own) while the whitelist is
 * read out of `scripts/dup_content_audit.py` at run time. One list, two readers.
 *
 * Rejected: shelling out to the Python auditor per page. It is inherently cross-page, so
 * every one of the 45 page-viewport runs would re-run the whole pairwise comparison, and
 * the meta gate would have nothing to fire against — a fixture page is not in `dist/`.
 */
register({
  id: 'dup-no-sibling-crossover',
  family: 'DUP',
  severity: 'advisory',
  describe: 'no run of 12+ words is shared with a sibling page outside the mandated whitelist',
  minExamined: 1,
  async run(page: Page, viewport: number, ctx: CheckContext): Promise<CheckResult> {
    const siblings = await ctx.siblings();
    // examined counts SIBLING PAGES COMPARED AGAINST, which is the unit actually judged.
    // Counting shingles instead would report thousands while possibly comparing against
    // nothing — a page with no siblings must read as "0 examined", not as a pass.
    if (siblings.length === 0) return { examined: 0, defects: [] };

    const own = normalise(
      await page.evaluate(() => (document.querySelector('main') || document.body).innerText || ''),
    );
    const whitelist = loadWhitelist();

    const ownShingles = new Map<string, number>();
    for (let i = 0; i + MIN_WORDS <= own.length; i++) {
      const key = own.slice(i, i + MIN_WORDS).join(' ');
      if (!ownShingles.has(key)) ownShingles.set(key, i);
    }

    const findings: { sibling: string; words: number; run: string }[] = [];
    for (const sib of siblings) {
      const sw = normalise(sib.text);
      const sibShingles = new Set<string>();
      for (let i = 0; i + MIN_WORDS <= sw.length; i++) {
        sibShingles.add(sw.slice(i, i + MIN_WORDS).join(' '));
      }
      const reported: string[] = [];
      for (const [key, i] of [...ownShingles.entries()].sort((a, b) => a[1] - b[1])) {
        if (!sibShingles.has(key)) continue;
        if (reported.some((r) => r.includes(key))) continue;
        // Grow the match to its maximal run, so one long shared passage is ONE finding
        // rather than one per sliding window. Without this a 60-word crossover reports
        // 49 times and DUP outvotes every other family by counting style alone.
        let j = i + MIN_WORDS;
        while (j < own.length && sibShingles.has(own.slice(j - MIN_WORDS + 1, j + 1).join(' '))) j++;
        const run = own.slice(i, j).join(' ');
        reported.push(run);
        if (whitelist.some((w) => run.includes(w))) continue;
        findings.push({ sibling: sib.slug, words: j - i, run });
      }
    }

    if (!findings.length) return { examined: siblings.length, defects: [] };
    findings.sort((a, b) => b.words - a.words);
    return {
      examined: siblings.length,
      defects: [
        {
          checkId: 'dup-no-sibling-crossover',
          family: 'DUP' as const,
          viewport,
          count: findings.length,
          message:
            `${findings.length} passage(s) shared with a sibling: ` +
            findings
              .slice(0, 3)
              .map((f) => `${f.words}w vs /${f.sibling}/ "${f.run.slice(0, 90)}"`)
              .join(' | '),
        },
      ],
    };
  },
});

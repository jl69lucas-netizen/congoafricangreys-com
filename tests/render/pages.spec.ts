import { test, expect } from '@playwright/test';
import { readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { registry } from './lib/registry.js';
import './checks/index.js';
import { writePartial, writeManifest } from './lib/scorecard.js';
import { checkDistFreshness } from './lib/freshness.js';
import type { Defect } from './lib/registry.js';

const here = dirname(fileURLToPath(import.meta.url));
const targets = JSON.parse(readFileSync(resolve(here, 'targets.json'), 'utf8')) as {
  families_by_page_type: Record<string, string[]>;
  pages: { slug: string; page_type: string; corpus: boolean }[];
};

/**
 * RENDER_OVERRIDE="check-id:reason; other-check:reason"
 *
 * An override suppresses a blocking failure and is written into the scorecard,
 * so overrides are counted rather than hidden. A bare id with no reason is rejected.
 *
 * Entries are separated by SEMICOLONS, not commas, because a real reason
 * contains commas — "card srcset regen queued, see backlog" was split into two
 * entries by a comma separator and rejected for the fragment having no colon.
 * A reason nobody can write is an override nobody will use, and an override
 * nobody will use gets replaced by someone quietly flipping the check back to
 * advisory, which is the outcome this whole mechanism exists to prevent.
 */
const overrides: { checkId: string; reason: string }[] = (process.env.RENDER_OVERRIDE ?? '')
  .split(';')
  .map((s) => s.trim())
  .filter(Boolean)
  .map((entry) => {
    const idx = entry.indexOf(':');
    if (idx < 1 || !entry.slice(idx + 1).trim()) {
      throw new Error(`RENDER_OVERRIDE entry "${entry}" needs the form check-id:reason`);
    }
    return { checkId: entry.slice(0, idx).trim(), reason: entry.slice(idx + 1).trim() };
  });
const overridden = new Set(overrides.map((o) => o.checkId));

writeManifest(
  registry.map((c) => c.id),
  targets.pages.length * 3,
);

/**
 * A throwing beforeAll fails every test in this file, so no partial is written, so
 * build_scorecard.mjs Guard 1 (partials !== manifest) also fails. That cascade is
 * deliberate: a stale measurement must be loud at both ends, never a green run.
 *
 * meta.spec.ts is intentionally NOT gated — it tests the checkers against fixtures,
 * where dist/ is irrelevant, and it must stay runnable while a build is broken.
 */
test.beforeAll(() => {
  const f = checkDistFreshness();
  if (!f.fresh) throw new Error(`RENDER HARNESS REFUSES TO MEASURE: ${f.reason}`);
  console.log(`[freshness] ${f.reason}`);
});

for (const target of targets.pages) {
  const families = targets.families_by_page_type[target.page_type];
  if (!families || families.length === 0) {
    throw new Error(
      `targets.json: page_type "${target.page_type}" (slug ${target.slug}) maps to no families. ` +
        `A page examined by nothing would score a perfect zero.`,
    );
  }
  const checks = registry.filter((c) => families.includes(c.family));
  if (checks.length === 0) {
    throw new Error(
      `no registered check matches families ${families.join(',')} for page_type "${target.page_type}"`,
    );
  }

  test(`${target.slug}`, async ({ page }, testInfo) => {
    const viewport = testInfo.project.use.viewport!.width;
    const res = await page.goto(`/${target.slug}/`);
    expect(res?.status(), `${target.slug} must be built`).toBe(200);

    const defects: Defect[] = [];
    const examined: Record<string, number> = {};

    for (const check of checks) {
      // Reset shared page state between checks — NAV clicks leave scroll,
      // :target styling and focus mutated for whatever runs next.
      await page.evaluate(() => {
        window.scrollTo(0, 0);
        (document.activeElement as HTMLElement | null)?.blur?.();
      });
      const result = await check.run(page, viewport);
      examined[check.id] = result.examined;
      defects.push(...result.defects);
    }

    writePartial({
      slug: target.slug,
      page_type: target.page_type,
      viewport,
      examined,
      defects,
      overrides,
    });

    const blocking = defects.filter(
      (d) =>
        registry.find((c) => c.id === d.checkId)?.severity === 'blocking' &&
        !overridden.has(d.checkId),
    );
    expect(
      blocking.map((d) => `[${d.family}] ${d.message}`),
      `${target.slug} @ ${viewport}px`,
    ).toEqual([]);
  });
}

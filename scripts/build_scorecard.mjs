#!/usr/bin/env node
// Merges data/quality/raw/*.json (one per page+viewport) into one scorecard per page.
// Usage: node scripts/build_scorecard.mjs [--run first|recheck]
import { readdirSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const RAW = resolve('data/quality/raw');
const OUT = resolve('data/quality/scorecards');
const runLabel = process.argv.includes('--run')
  ? process.argv[process.argv.indexOf('--run') + 1]
  : 'first';
const date = new Date().toISOString().slice(0, 10);

mkdirSync(OUT, { recursive: true });

const files = readdirSync(RAW).filter((f) => f.endsWith('.json') && f !== '_manifest.json');
let manifest = { checkIds: [], expectedPartials: 0 };
try {
  manifest = JSON.parse(readFileSync(resolve(RAW, '_manifest.json'), 'utf8'));
} catch {
  console.error('FAIL: no _manifest.json — cannot tell which checks were supposed to run.');
  process.exit(1);
}

const bySlug = new Map();
const examinedAnywhere = new Map(manifest.checkIds.map((id) => [id, 0]));
for (const file of files) {
  const p = JSON.parse(readFileSync(resolve(RAW, file), 'utf8'));
  if (!bySlug.has(p.slug)) bySlug.set(p.slug, []);
  bySlug.get(p.slug).push(p);
  for (const [checkId, n] of Object.entries(p.examined)) {
    examinedAnywhere.set(checkId, (examinedAnywhere.get(checkId) ?? 0) + n);
  }
}

// Guard 1: a page that crashed the harness writes no partial and would otherwise
// score as absent rather than as failed. "PASS in 0 pages" wearing a new costume.
if (files.length !== manifest.expectedPartials) {
  console.error(
    `FAIL: expected ${manifest.expectedPartials} partials, found ${files.length}. ` +
      `Missing results are not passes.`,
  );
  process.exit(1);
}

// Guard 2: seeded from the MANIFEST, not from the partials — a check that ran
// nowhere contributes no key to any partial and would be invisible otherwise.
const dead = [...examinedAnywhere.entries()].filter(([, n]) => n === 0).map(([id]) => id);
if (dead.length) {
  console.error(`FAIL: check(s) examined zero nodes across every page: ${dead.join(', ')}`);
  process.exit(1);
}

if (bySlug.size === 0) {
  console.error('FAIL: zero pages examined. A run over no pages is never a pass.');
  process.exit(1);
}

let grandTotal = 0;
for (const [slug, parts] of bySlug) {
  const defectsByFamily = {};
  const examined = { pages: 1, checks: 0 };
  const details = [];
  for (const part of parts) {
    examined.checks = Math.max(examined.checks, Object.keys(part.examined).length);
    for (const d of part.defects) {
      defectsByFamily[d.family] = (defectsByFamily[d.family] || 0) + 1;
      details.push({ viewport: part.viewport, checkId: d.checkId, message: d.message });
    }
  }
  const total = Object.values(defectsByFamily).reduce((a, b) => a + b, 0);
  grandTotal += total;
  const card = {
    slug,
    date,
    page_type: parts[0].page_type,
    run: runLabel,
    harness_version: '1.0.0',
    viewports: parts.map((p) => p.viewport).sort((a, b) => a - b),
    examined,
    defects: defectsByFamily,
    total,
    overrides: parts.flatMap((p) => p.overrides ?? []),
    details,
  };
  writeFileSync(resolve(OUT, `${slug}-${date}.json`), JSON.stringify(card, null, 2));
  console.log(`${String(total).padStart(3)}  ${slug}`);
}

const allOverrides = [...bySlug.values()].flat().flatMap((p) => p.overrides ?? []);
console.log(`---\n${grandTotal} defects across ${bySlug.size} pages (run=${runLabel})`);
if (allOverrides.length) {
  console.log(`${allOverrides.length} OVERRIDE(S) IN EFFECT — these are suppressed defects:`);
  for (const o of allOverrides) console.log(`  ${o.checkId}: ${o.reason}`);
}

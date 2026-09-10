/**
 * Unit checks for src/lib/srcset.ts — srcsetAttrs() and the actual-width guard.
 *
 * No vitest/jest/node:test runner exists in this repo (only Playwright, wired for
 * rendered-page checks under tests/render/). This file is written as a plain script,
 * not a suite a `test` script discovers — run it directly:
 *
 *   npx tsx tests/srcset.spec.ts
 *
 * If a real TS test runner is ever added to package.json, convert the three checks
 * below into it verbatim; do not add a runner just for this file.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');

let failures = 0;
function check(name: string, cond: boolean) {
  if (cond) {
    console.log(`PASS: ${name}`);
  } else {
    failures++;
    console.error(`FAIL: ${name}`);
  }
}

async function main() {
  const { srcsetAttrs, srcsetFor } = await import(
    path.join(repoRoot, 'src/lib/srcset.ts')
  );

  // (a) unknown image -> {} (no srcset, no sizes: both attrs must be absent together)
  const nope = srcsetAttrs('/nope.webp', [300], '300px');
  check('unknown src yields {} from srcsetAttrs', Object.keys(nope).length === 0);

  // (b) a real manifest entry (the homepage hero) -> both keys present, sizes preserved
  const hero = srcsetAttrs(
    '/african-grey-parrot-breeder-midland-tx-hero.webp',
    [300],
    '300px'
  );
  check(
    'known src yields both srcset and sizes',
    'srcset' in hero && 'sizes' in hero && (hero as any).sizes === '300px'
  );
  check(
    'srcset for hero matches direct srcsetFor call',
    (hero as any).srcset ===
      srcsetFor('/african-grey-parrot-breeder-midland-tx-hero.webp', [300])
  );

  // (c) actual-width guard: a variant file misnamed to claim a width below the master,
  // but whose real (manifest) width is >= the master, must be dropped.
  // image-widths.json is a static import inside srcset.ts, so we temporarily patch the
  // manifest file on disk, import a cache-busted copy of the module, then restore it.
  const manifestPath = path.join(repoRoot, 'src/data/image-widths.json');
  const backup = fs.readFileSync(manifestPath, 'utf8');
  try {
    const fake = JSON.parse(backup);
    fake['/__test-guard.webp'] = 700; // "master"
    fake['/__test-guard-760.webp'] = 800; // misnamed variant, actually wider than the master
    fs.writeFileSync(manifestPath, JSON.stringify(fake));

    const { srcsetFor: srcsetForFresh } = await import(
      path.join(repoRoot, 'src/lib/srcset.ts') + `?bust=${Date.now()}`
    );
    const result = srcsetForFresh('/__test-guard.webp', [760]);
    check(
      'actual-width guard drops a variant whose real width >= master',
      result === undefined
    );
  } finally {
    fs.writeFileSync(manifestPath, backup);
  }

  if (failures > 0) {
    console.error(`\n${failures} check(s) failed.`);
    process.exit(1);
  }
  console.log('\nAll srcset checks passed.');
}

main();

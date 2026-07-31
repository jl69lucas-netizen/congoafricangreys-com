import { test, expect } from '@playwright/test';
import { mkdtempSync, mkdirSync, writeFileSync, utimesSync, symlinkSync, rmSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { registry } from './lib/registry.js';
import { fixtureUrl } from './lib/servers.js';
import { checkDistFreshness } from './lib/freshness.js';
import { resetRaw } from './lib/scorecard.js';
import './checks/index.js';


test('the registry is not empty', () => {
  expect(
    registry.length,
    'a harness that examines zero checks is not a passing harness',
  ).toBeGreaterThan(0);
});

for (const check of registry) {
  test.describe(`${check.id} [${check.family}]`, () => {
    test('fires on the known_broken fixture', async ({ page }, testInfo) => {
      const viewport = testInfo.project.use.viewport!.width;
      const res = await page.goto(fixtureUrl('known_broken', check.id));
      expect(res?.status(), 'known_broken fixture must exist').toBe(200);
      const result = await check.run(page, viewport);
      expect(
        result.examined,
        `examined must reach the declared floor (${check.minExamined}) — a check cannot pass by inflating its own count`,
      ).toBeGreaterThanOrEqual(check.minExamined);
      expect(
        result.defects.length,
        `${check.id} did not fire on a page built to contain its defect`,
      ).toBeGreaterThan(0);
    });

    test('is silent on the known_good fixture', async ({ page }, testInfo) => {
      const viewport = testInfo.project.use.viewport!.width;
      const res = await page.goto(fixtureUrl('known_good', check.id));
      expect(res?.status(), 'known_good fixture must exist').toBe(200);
      const result = await check.run(page, viewport);
      expect(
        result.examined,
        `examined must reach the declared floor (${check.minExamined})`,
      ).toBeGreaterThanOrEqual(check.minExamined);
      expect(
        result.defects.map((d) => d.message),
        `${check.id} cried wolf on a clean page`,
      ).toEqual([]);
    });
  });
}

test.describe('dist/ freshness gate', () => {
  // mkdtemp leaks a real directory per call unless something removes it. Tracked here
  // and swept in afterAll — 5 tests x 3 viewport projects otherwise left 15 orphaned
  // dirs under the OS tmpdir on every meta run.
  const tempRoots: string[] = [];
  const newRoot = () => {
    const root = mkdtempSync(join(tmpdir(), 'fresh-'));
    tempRoots.push(root);
    return root;
  };
  const mk = () => {
    const root = newRoot();
    mkdirSync(join(root, 'dist'), { recursive: true });
    mkdirSync(join(root, 'src'), { recursive: true });
    return root;
  };

  test.afterAll(() => {
    for (const root of tempRoots) rmSync(root, { recursive: true, force: true });
  });

  test('a dist/ newer than src/ is fresh', () => {
    const root = mk();
    writeFileSync(join(root, 'src', 'a.astro'), 'x');
    writeFileSync(join(root, 'dist', 'index.html'), 'x');
    utimesSync(join(root, 'src', 'a.astro'), new Date(1000), new Date(1000));
    utimesSync(join(root, 'dist', 'index.html'), new Date(2000), new Date(2000));
    expect(checkDistFreshness(root).fresh).toBe(true);
  });

  test('a src/ file newer than every dist/ file is STALE', () => {
    const root = mk();
    writeFileSync(join(root, 'dist', 'index.html'), 'x');
    writeFileSync(join(root, 'src', 'a.astro'), 'x');
    utimesSync(join(root, 'dist', 'index.html'), new Date(1000), new Date(1000));
    utimesSync(join(root, 'src', 'a.astro'), new Date(2000), new Date(2000));
    const r = checkDistFreshness(root);
    expect(r.fresh, r.reason).toBe(false);
    expect(r.reason).toContain('npm run build');
    expect(r.reason).toContain('a.astro');
  });

  test('a newer package.json (the non-directory branch of newest()) forces refusal', () => {
    // 'src' and 'public' hit the directory-walk branch of newest(); 'package.json' and
    // 'astro.config.mjs' are plain files in SOURCES and take the other branch (newest()'s
    // `else best = { path, ms: st.mtimeMs }`, never exercised by any test above). Pin it
    // directly rather than trusting the directory-walk tests to stand in for it.
    const root = mk();
    writeFileSync(join(root, 'dist', 'index.html'), 'x');
    utimesSync(join(root, 'dist', 'index.html'), new Date(1000), new Date(1000));
    writeFileSync(join(root, 'package.json'), '{}');
    utimesSync(join(root, 'package.json'), new Date(2000), new Date(2000));
    const r = checkDistFreshness(root);
    expect(r.fresh, r.reason).toBe(false);
    expect(r.reason).toContain('package.json');
  });

  test('a missing dist/ is STALE, never fresh-by-default', () => {
    const root = newRoot();
    const r = checkDistFreshness(root);
    expect(r.fresh).toBe(false);
    // Pin the actual message, not just the boolean. Deleting the dedicated
    // `!existsSync(dist)` guard would fall through to the ms===0 branch below and
    // still report fresh:false — silently trading a clear message for a confusing one
    // ("a.astro is 29759023 min newer than the newest file in dist/ (dist)"). For a
    // refusal gate the message IS the deliverable; a boolean-only assertion can't catch that.
    expect(r.reason).toContain('dist/ does not exist');
  });

  test('an empty dist/ is STALE', () => {
    const root = mk();
    writeFileSync(join(root, 'src', 'a.astro'), 'x');
    const r = checkDistFreshness(root);
    expect(r.fresh).toBe(false);
    expect(r.reason).toContain('dist/ contains no files');
  });

  // src/pages/node_modules/.vite/deps/ genuinely exists in this repo. Walking it
  // reads thousands of vendored files whose mtimes have nothing to do with our
  // build, and any one of them being newer than dist/ would refuse every run.
  test('vendored trees under src/ are not treated as source', () => {
    const root = mk();
    mkdirSync(join(root, 'src', 'pages', 'node_modules', '.vite'), { recursive: true });
    writeFileSync(join(root, 'dist', 'index.html'), 'x');
    writeFileSync(join(root, 'src', 'pages', 'node_modules', '.vite', 'dep.js'), 'x');
    utimesSync(join(root, 'dist', 'index.html'), new Date(1000), new Date(1000));
    utimesSync(join(root, 'src', 'pages', 'node_modules', '.vite', 'dep.js'), new Date(9000), new Date(9000));
    expect(checkDistFreshness(root).fresh).toBe(true);
  });

  // A directory that legitimately contains nothing but SKIP-listed vendor content also
  // computes ms:0 (proven by the test above) — so ms===0 alone can't distinguish "found
  // nothing" from "couldn't read it". A read failure needs its own signal. Simulated with
  // a broken symlink (points at a path that doesn't exist) rather than chmod, because a
  // permission-denied test is unreliable under a root-running CI user, while a dangling
  // symlink throws ENOENT from statSync regardless of who's running the test.
  test('an unreadable path under src/ refuses rather than silently passing as fresh', () => {
    const root = mk();
    writeFileSync(join(root, 'dist', 'index.html'), 'x');
    utimesSync(join(root, 'dist', 'index.html'), new Date(1000), new Date(1000));
    symlinkSync(join(root, 'this-target-does-not-exist'), join(root, 'src', 'broken-link'));
    const r = checkDistFreshness(root);
    expect(r.fresh, r.reason).toBe(false);
    expect(r.reason).toContain('could not be fully read');
  });
});

test.describe('resetRaw', () => {
  test('empties a populated raw dir, so a refused run cannot merge into a prior clean scorecard', () => {
    const dir = mkdtempSync(join(tmpdir(), 'raw-'));
    writeFileSync(join(dir, 'some-page-vp375.json'), '{}');
    writeFileSync(join(dir, '_manifest.json'), '{}');
    resetRaw(dir);
    expect(existsSync(dir)).toBe(false);
  });
});

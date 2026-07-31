import { test, expect } from '@playwright/test';
import { mkdtempSync, mkdirSync, writeFileSync, utimesSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { registry } from './lib/registry.js';
import { fixtureUrl } from './lib/servers.js';
import { checkDistFreshness } from './lib/freshness.js';
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
  const mk = () => {
    const root = mkdtempSync(join(tmpdir(), 'fresh-'));
    mkdirSync(join(root, 'dist'), { recursive: true });
    mkdirSync(join(root, 'src'), { recursive: true });
    return root;
  };

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

  test('a missing dist/ is STALE, never fresh-by-default', () => {
    const root = mkdtempSync(join(tmpdir(), 'fresh-'));
    expect(checkDistFreshness(root).fresh).toBe(false);
  });

  test('an empty dist/ is STALE', () => {
    const root = mk();
    writeFileSync(join(root, 'src', 'a.astro'), 'x');
    expect(checkDistFreshness(root).fresh).toBe(false);
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
});

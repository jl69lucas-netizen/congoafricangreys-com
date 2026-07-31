import { test, expect } from '@playwright/test';
import { registry } from './lib/registry.js';
import { fixtureUrl } from './lib/servers.js';
import './checks/index.js';

const VIEWPORT = 1280;

test('the registry is not empty', () => {
  expect(
    registry.length,
    'a harness that examines zero checks is not a passing harness',
  ).toBeGreaterThan(0);
});

for (const check of registry) {
  test.describe(`${check.id} [${check.family}]`, () => {
    test('fires on the known_broken fixture', async ({ page }) => {
      const res = await page.goto(fixtureUrl('known_broken', check.id));
      expect(res?.status(), 'known_broken fixture must exist').toBe(200);
      const result = await check.run(page, VIEWPORT);
      expect(result.examined, 'examined must be > 0').toBeGreaterThan(0);
      expect(
        result.defects.length,
        `${check.id} did not fire on a page built to contain its defect`,
      ).toBeGreaterThan(0);
    });

    test('is silent on the known_good fixture', async ({ page }) => {
      const res = await page.goto(fixtureUrl('known_good', check.id));
      expect(res?.status(), 'known_good fixture must exist').toBe(200);
      const result = await check.run(page, VIEWPORT);
      expect(result.examined, 'examined must be > 0').toBeGreaterThan(0);
      expect(
        result.defects.map((d) => d.message),
        `${check.id} cried wolf on a clean page`,
      ).toEqual([]);
    });
  });
}

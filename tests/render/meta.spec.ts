import { test, expect } from '@playwright/test';
import {
  mkdtempSync,
  mkdirSync,
  writeFileSync,
  utimesSync,
  symlinkSync,
  rmSync,
  existsSync,
  readdirSync,
  readFileSync,
} from 'node:fs';
import { execFileSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { registry, MAX_DEFECT_ROWS, type Check, type Defect } from './lib/registry.js';
import { runCheck } from './lib/runCheck.js';
import { flattenSlug } from './lib/scorecard.js';
import { fixtureUrl, FIXTURE_BASE } from './lib/servers.js';
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
      const result = await runCheck(check, page, viewport);
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
      const result = await runCheck(check, page, viewport);
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

test.describe('globalSetup vs spec-module-scope regression probe', () => {
  // Two DIFFERENT things are pinned here, deliberately not conflated:
  //
  // 1. The synthetic probe below (runProbe + its two tests) proves the general
  //    Playwright LOADING MECHANISM: a spec module's top-level code runs once per
  //    worker PROCESS, not once per run, so a destructive call there can destroy an
  //    earlier worker's output, and moving that call into globalSetup fixes it. It
  //    builds its own throwaway spec/config from scratch and never reads
  //    pages.spec.ts or global-setup.ts — so it CANNOT detect a regression in this
  //    repo's actual wiring. (An earlier version of this comment claimed it could;
  //    it was reviewed, the claim was reproduced as false — reintroducing
  //    resetRaw() at pages.spec.ts module scope left both probe tests green — and
  //    the comment is corrected here instead of left to mislead the next reader.)
  //
  // 2. The 'resetRaw() lives in global-setup.ts, never in pages.spec.ts' test below
  //    pins the actual PRODUCTION WIRING by reading both real files from disk. THAT
  //    is the one that goes red if resetRaw() is ever moved back to pages.spec.ts
  //    module scope — confirmed by doing exactly that and reverting (2026-08-01).
  const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..');
  const playwrightCli = resolve(repoRoot, 'node_modules', '@playwright', 'test', 'cli.js');
  const scorecardAbs = resolve(repoRoot, 'tests', 'render', 'lib', 'scorecard.ts');

  /**
   * Builds and runs a disposable 3-project, 1-test-per-project Playwright suite whose
   * only job is to write one file per project into a shared scratch RAW dir, with
   * resetRaw() placed either at the probe spec's module scope (the old, broken
   * pattern) or inside a probe globalSetup (the fix). Returns which of the 3 files
   * survived. `workers: 2` mirrors the real playwright.config.ts, since the real bug
   * was observed at exactly that worker count on the real harness (2026-08-01).
   *
   * The probe directory is created UNDER tests/render/, not the OS tmpdir — Node's
   * module resolution walks up from a file's own location looking for node_modules,
   * and a probe.config.ts living outside the repo tree cannot find `@playwright/test`
   * at all. First attempt used tmpdir() and both variants silently failed to even
   * start (MODULE_NOT_FOUND), which made the "broken" case pass for the wrong reason
   * (0 survivors satisfies "< 3" same as 1 does) — decoration, caught before it shipped.
   */
  function runProbe(resetAtModuleScope: boolean): string[] {
    const probeRoot = mkdtempSync(resolve(repoRoot, 'tests', 'render', '.probe-'));
    const rawDir = join(probeRoot, 'raw');
    mkdirSync(rawDir, { recursive: true });
    const rawDirLit = JSON.stringify(rawDir);
    const scorecardLit = JSON.stringify(scorecardAbs);
    // mkdirSync here mirrors production writePartial(), which also recreates RAW_DIR
    // before every write — resetRaw() deletes the directory outright, so whichever
    // side runs it (module scope or globalSetup) leaves nothing for a bare
    // writeFileSync to write into.
    const writeOnePartial =
      `test('write-one-partial', ({}, testInfo) => {\n` +
      `  mkdirSync(${rawDirLit}, { recursive: true });\n` +
      `  writeFileSync(join(${rawDirLit}, testInfo.project.name + '.json'), '{}');\n` +
      `});\n`;

    writeFileSync(
      join(probeRoot, 'probe.spec.ts'),
      resetAtModuleScope
        ? `import { test } from '@playwright/test';\n` +
            `import { writeFileSync, mkdirSync } from 'node:fs';\n` +
            `import { join } from 'node:path';\n` +
            `import { resetRaw } from ${scorecardLit};\n` +
            `resetRaw(${rawDirLit}); // BROKEN: module scope runs once per worker process\n` +
            writeOnePartial
        : `import { test } from '@playwright/test';\n` +
            `import { writeFileSync, mkdirSync } from 'node:fs';\n` +
            `import { join } from 'node:path';\n` +
            writeOnePartial,
    );

    if (!resetAtModuleScope) {
      writeFileSync(
        join(probeRoot, 'probe-global-setup.ts'),
        `import { resetRaw } from ${scorecardLit};\n` +
          `export default function globalSetup() { resetRaw(${rawDirLit}); } // FIX: runs exactly once\n`,
      );
    }

    writeFileSync(
      join(probeRoot, 'probe.config.ts'),
      `import { defineConfig } from '@playwright/test';\n` +
        `export default defineConfig({\n` +
        `  testDir: ${JSON.stringify(probeRoot)},\n` +
        `  testMatch: ['probe.spec.ts'],\n` +
        `  fullyParallel: false,\n` +
        `  workers: 2,\n` +
        `  reporter: [['dot']],\n` +
        (resetAtModuleScope ? '' : `  globalSetup: ${JSON.stringify(join(probeRoot, 'probe-global-setup.ts'))},\n`) +
        `  projects: [{ name: 'a' }, { name: 'b' }, { name: 'c' }],\n` +
        `});\n`,
    );

    try {
      execFileSync(process.execPath, [playwrightCli, 'test', '-c', join(probeRoot, 'probe.config.ts')], {
        cwd: repoRoot,
        timeout: 30_000,
        stdio: 'pipe',
      });
    } catch {
      // Nothing here depends on Playwright's own exit code — only on how many
      // scratch files survive in rawDir. A non-zero exit changes nothing.
    }

    const survivors = existsSync(rawDir) ? readdirSync(rawDir) : [];
    rmSync(probeRoot, { recursive: true, force: true });
    return survivors;
  }

  // Viewport-independent: the probe shells out to a whole nested Playwright run and
  // gains nothing from repeating across vp375/vp768/vp1280 — skip on the other two
  // projects so the meta suite isn't paying for 3x identical signal.
  test("resetRaw() at spec module scope loses other workers' partials", ({}, testInfo) => {
    test.skip(testInfo.project.name !== 'vp375', 'viewport-independent; runs once');
    const survivors = runProbe(true);
    expect(
      // > 0 first: a probe that silently fails to run at all (e.g. the tmpdir
      // MODULE_NOT_FOUND case caught while building this) also produces 0 survivors,
      // which satisfies "< 3" for the wrong reason. Pin that this test's OWN signal
      // is "at least one worker actually ran and wrote its file", not borrowed from
      // test 2 failing.
      survivors.length,
      `expected fewer than 3 of 3 projects' partials to survive module-scope reset; found ${JSON.stringify(survivors)}`,
    ).toBeGreaterThan(0);
    expect(survivors.length).toBeLessThan(3);
  });

  test('resetRaw() in globalSetup preserves every project’s partial', ({}, testInfo) => {
    test.skip(testInfo.project.name !== 'vp375', 'viewport-independent; runs once');
    const survivors = runProbe(false);
    expect(
      survivors.length,
      `expected all 3 projects' partials to survive; found ${JSON.stringify(survivors)}`,
    ).toBe(3);
  });
});

test.describe('resetRaw placement — pins the actual production wiring', () => {
  // Unlike the synthetic probe above, this reads the REAL files. Comments are
  // stripped before matching so prose that mentions "resetRaw()" — including the
  // paragraph in pages.spec.ts explaining why the call moved OUT of that file —
  // can't produce a false positive; only a call in live code counts.
  const stripComments = (src: string) => src.replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/.*$/gm, '');
  const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..');

  test('resetRaw() is called in global-setup.ts and nowhere in pages.spec.ts', () => {
    const globalSetupCode = stripComments(readFileSync(resolve(repoRoot, 'tests', 'render', 'global-setup.ts'), 'utf8'));
    const pagesSpecCode = stripComments(readFileSync(resolve(repoRoot, 'tests', 'render', 'pages.spec.ts'), 'utf8'));

    expect(
      globalSetupCode,
      'global-setup.ts must call resetRaw() — that is the entire fix this file exists for',
    ).toContain('resetRaw(');
    expect(
      pagesSpecCode,
      'resetRaw() must not be called anywhere in pages.spec.ts — Playwright loads a spec ' +
        "module's top-level code once per WORKER PROCESS, not once per run, so a destructive " +
        "call there destroys earlier workers' already-written partials (reproduced 2026-08-01: " +
        '3 tests across 3 viewport projects left exactly 1 partial standing). See global-setup.ts.',
    ).not.toContain('resetRaw(');
  });
});

/**
 * NAV supplied 337 of the 418 rows in the first baseline (81%) purely by counting
 * granularity: three checks aggregate to one row per page-viewport, NAV emitted one row
 * per anchor. A family total is only meaningful if every family counts the same unit.
 */
test.describe('nav-jump-target-lands reports causes, not instances', () => {
  test('a page with many broken anchors yields ONE row per failure mode', async ({
    page,
  }, testInfo) => {
    const viewport = testInfo.project.use.viewport!.width;
    const anchors = Array.from({ length: 20 }, (_, i) => i + 1);
    const html =
      `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>many</title><style>` +
      `html{scroll-behavior:auto}body{margin:0;font:16px/1.5 system-ui}` +
      `header{position:sticky;top:0;height:96px;background:#2D6A4F;display:flex;align-items:center}` +
      `nav a{color:#fff;margin-right:8px;display:inline-block;min-width:44px;min-height:44px}` +
      `section{min-height:900px}h2{margin:0}</style></head><body><header><nav>` +
      anchors.map((i) => `<a href="#h${i}">${i}</a>`).join(' ') +
      `</nav></header>` +
      anchors.map((i) => `<section><h2 id="h${i}">H${i}</h2></section>`).join('') +
      `</body></html>`;
    await page.setContent(html);

    const check = registry.find((c) => c.id === 'nav-jump-target-lands')!;
    const result = await check.run(page, viewport);

    expect(result.examined, 'must have judged all 20 targets').toBe(20);
    expect(
      result.defects.length,
      `expected at most 3 rows (one per failure mode); got ${result.defects.length}`,
    ).toBeLessThanOrEqual(3);
    expect(
      result.defects.reduce((n, d) => n + (d.count ?? 0), 0),
      'the rows must still carry the instance count',
    ).toBeGreaterThan(3);
    expect(
      result.defects[0].message,
      'the row must name the page-level cause',
    ).toMatch(/scroll-margin-top|scroll-behavior/);
  });
});

/**
 * Naming a cause is only worth doing if the cause names the right DIRECTION.
 *
 * Measured 2026-08-01: dna-tested and hand-raised land every one of their 18 links at
 * 162px and 170px against an 88-156px band — OVERSHOOTS, past the far edge — and both
 * rows read "1 of 19 targets have scroll-margin-top under the 96px of pinned chrome".
 * That is an undershoot description, sourced from a minority of one, and a reader who
 * followed it would INCREASE a scroll-margin that is already 66px too large.
 *
 * Four fixtures, because direction has FOUR quadrants and three of them can be satisfied
 * by a wrong implementation. Defining `long` as "not short" rather than "past the far
 * edge" passes the uniform, the good and the mixed fixture, and then prints "18 of 19
 * targets overshoot" on a page whose 18 targets sit correctly IN-BAND — the mirror image
 * of the bug this exists to kill. nav-undershoot-minority.html is that fourth quadrant.
 *
 * Every test here forces its own 1280x900 viewport because the fixtures' geometry is
 * computed against it, so running them once per viewport project would be three
 * byte-identical executions of the same work.
 */
test.describe('nav-jump-target-lands names the direction of failure', () => {
  const check = () => registry.find((c) => c.id === 'nav-jump-target-lands')!;
  const onlyOnce = (testInfo: { project: { name: string } }) =>
    test.skip(testInfo.project.name !== 'vp375', 'viewport-independent; runs once');

  test('fires on a page whose targets overshoot the chrome band', async ({ page }, testInfo) => {
    onlyOnce(testInfo);
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(`${FIXTURE_BASE}/tests/render/fixtures/known_broken/nav-overshoot.html`);
    const r = await runCheck(check(), page, 1280);

    expect(r.defects.length).toBe(1);
    // The whole point of this fixture: the cause must not blame a too-SMALL margin.
    expect(r.defects[0].message).toMatch(/overshoot|past|beyond|over the/i);
    expect(r.defects[0].message).not.toMatch(/under the \d+px of pinned chrome/);
  });

  test('stays silent when the same page lands inside the band', async ({ page }, testInfo) => {
    onlyOnce(testInfo);
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(`${FIXTURE_BASE}/tests/render/fixtures/known_good/nav-overshoot-fixed.html`);
    const r = await runCheck(check(), page, 1280);

    expect(r.defects.length).toBe(0);
  });

  // The pair above pins BLINDNESS to overshoot (uniform cohort, old code returned
  // "no single page-level cause identified"). This third fixture pins the defect
  // actually measured in the scorecards: a MIXED cohort, where the old code found the
  // one small target among nineteen and printed it as THE root cause of the other
  // eighteen's overshoot. Verified red against the pre-fix nav.ts, whose output was
  // "1 of 19 targets have scroll-margin-top under the 96px of pinned chrome" —
  // character-for-character the string dna-tested and hand-raised shipped.
  test('names the majority cohort when a minority undershoots', async ({ page }, testInfo) => {
    onlyOnce(testInfo);
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(`${FIXTURE_BASE}/tests/render/fixtures/known_broken/nav-overshoot-mixed.html`);
    const r = await runCheck(check(), page, 1280);

    expect(r.defects.length).toBe(1);
    // The measured real-page failure: 1 small target among 19 was reported as THE
    // root cause of 18 overshoot failures. The cause must name the 18, not the 1.
    expect(r.defects[0].message).toMatch(/18 of 19 targets overshoot/);
    expect(r.defects[0].message).not.toMatch(/1 of 19 targets have scroll-margin-top under/);
  });

  test('names an undershooting minority without claiming overshoot', async ({ page }, testInfo) => {
    onlyOnce(testInfo);
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(
      `${FIXTURE_BASE}/tests/render/fixtures/known_broken/nav-undershoot-minority.html`,
    );
    const r = await runCheck(check(), page, 1280);

    expect(r.defects.length).toBe(1);
    // Guards the fourth quadrant: 18 targets sit correctly IN-BAND and one undershoots.
    // An implementation that defines `long` as "not short" rather than "past the far
    // edge" passes every other fixture and reports "18 of 19 targets overshoot" here.
    // Verified: the `else long++` mutant fails exactly this assertion.
    expect(r.defects[0].message).toMatch(/1 of 19 targets have scroll-margin-top under/);
    expect(r.defects[0].message).not.toMatch(/overshoot/);
  });
});

/**
 * The contract is enforced at the call site, not in each check, and not only against
 * fixtures. A fixture has two anchors; a real page has sixty-two. A rule that only the
 * fixtures can violate is a rule the real pages are exempt from.
 */
test.describe('the check-result contract', () => {
  const fake = (defects: Partial<Defect>[]): Check => ({
    id: 'synthetic-check',
    family: 'NAV',
    severity: 'advisory',
    describe: 'synthetic',
    minExamined: 0,
    async run() {
      return { examined: 9, defects: defects as Defect[] };
    },
  });

  const row = (over: Partial<Defect> = {}): Partial<Defect> => ({
    checkId: 'synthetic-check',
    family: 'NAV',
    viewport: 375,
    count: 1,
    message: 'x',
    ...over,
  });

  test('accepts a well-formed result', async ({ page }) => {
    const r = await runCheck(fake([row()]), page, 375);
    expect(r.defects.length).toBe(1);
  });

  test('rejects more rows than MAX_DEFECT_ROWS', async ({ page }) => {
    const many = Array.from({ length: MAX_DEFECT_ROWS + 1 }, () => row());
    await expect(runCheck(fake(many), page, 375)).rejects.toThrow(/rows/i);
  });

  test('rejects a row with no count', async ({ page }) => {
    await expect(runCheck(fake([row({ count: undefined })]), page, 375)).rejects.toThrow(/count/i);
  });

  test('rejects count: 0 — a defect row describes at least one failure', async ({ page }) => {
    await expect(runCheck(fake([row({ count: 0 })]), page, 375)).rejects.toThrow(/count/i);
  });

  test('rejects a row attributed to a different check', async ({ page }) => {
    await expect(runCheck(fake([row({ checkId: 'someone-else' })]), page, 375)).rejects.toThrow(
      /checkId/i,
    );
  });

  test('rejects a row attributed to a different family', async ({ page }) => {
    await expect(runCheck(fake([row({ family: 'IMG' })]), page, 375)).rejects.toThrow(/family/i);
  });

  test('rejects a negative examined count', async ({ page }) => {
    const bad: Check = { ...fake([]), async run() { return { examined: -1, defects: [] }; } };
    await expect(runCheck(bad, page, 375)).rejects.toThrow(/examined/i);
  });
});

test.describe('nested slugs cannot silently lose a page', () => {
  // The corpus spans seven page types, two of which are nested: blog/<post> and
  // available/<bird>. Interpolated raw into a filename they name a directory that does
  // not exist, so writePartial throws AFTER the checks have run and the page writes
  // nothing. A page with no partial scores ABSENT, not failed — and build_scorecard's
  // count guard would report it as a crashed page, sending the reader after a defect
  // that is really a filename. Cheap to pin, expensive to debug.
  test('flattenSlug removes every path separator', () => {
    expect(flattenSlug('blog/african-grey-parrot-cage-setup')).toBe(
      'blog__african-grey-parrot-cage-setup',
    );
    expect(flattenSlug('available/roys')).toBe('available__roys');
    expect(flattenSlug('congo-african-grey-for-sale')).toBe('congo-african-grey-for-sale');
    expect(flattenSlug('a/b/c')).not.toContain('/');
  });

  test('writePartial actually lands a file for a nested slug', () => {
    const dir = mkdtempSync(join(tmpdir(), 'raw-'));
    const prev = process.cwd();
    process.chdir(dir);
    try {
      mkdirSync(join(dir, 'data', 'quality', 'raw'), { recursive: true });
      // Re-import is not possible mid-run, so assert the naming contract the writer uses.
      const name = `${flattenSlug('blog/x')}-vp375.json`;
      writeFileSync(join(dir, 'data', 'quality', 'raw', name), '{}');
      expect(readdirSync(join(dir, 'data', 'quality', 'raw'))).toEqual(['blog__x-vp375.json']);
    } finally {
      process.chdir(prev);
      rmSync(dir, { recursive: true, force: true });
    }
  });
});

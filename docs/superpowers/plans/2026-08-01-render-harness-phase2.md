# Render Harness Phase 2 — Ledger, Learning Loop, and Three Repairs

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the measurement loop opened in Phase 1 — repair the three known harness bugs, then add the ledger, the report, and the skill that forces every escaped defect to be charged to the harness instead of absorbed as a new rule.

**Architecture:** Phase 1 built Layer 1 (the harness). Phase 2 builds Layer 2 (the ledger) and Layer 3 (the promotion path), and fixes the three Layer-1 defects that make Layer 2's numbers untrustworthy: defect rows counted in mixed units, a NAV check that reports one row per anchor instead of one root cause per page, and a `dist/` that can be stale without anyone noticing. Repairs land **first**, because a ledger built on wrong units records the wrong trend forever.

**Tech Stack:** `@playwright/test` 1.60 (TypeScript, already installed), Node 20 ESM scripts (`.mjs`), Python 3 + pytest (existing convention: `tests/test_*.py`), `python3 -m http.server` for the two static servers.

**Spec:** `docs/superpowers/specs/2026-07-31-self-improving-quality-loop-design.md` §3.2, §3.3
**Phase 1 plan:** `docs/superpowers/plans/2026-07-31-render-harness-phase1.md`

---

## Ground truth measured on this repo, 2026-08-01

Do not re-derive these. They were verified before this plan was written.

| Fact | Value |
|---|---|
| Baseline scorecards | 9 files in `data/quality/scorecards/*-2026-07-31.json` |
| NAV defect rows | 337 across 8 pages (23+42+15+62+41+50+52+52); congo-pair = **0** |
| LAYOUT rows per page | exactly 6 (2 checks × 3 viewports) — aggregated |
| IMG rows per page | exactly 3 (1 check × 3 viewports) — aggregated |
| Global smooth scroll | `src/styles/global.css:104`, inside `@media (prefers-reduced-motion: no-preference)` |
| congo-pair's override | `html:has(.cpair){scroll-behavior:auto}` — the only `html`-level `auto` in the cluster |
| `img-srcset-within-2x` | **blocking**; fires on 9/9 pages, 33 distinct files, worst 13.33× |
| Rework rate (canonical cmd, 2026-05-01→07-31) | 211 / 850 = **24.8%** |
| `data/quality/raw/` | gitignored (`.gitignore:61`); `scorecards/` is tracked |

**The NAV diagnosis is NOT settled.** `tests/render/checks/nav.ts:86` resets with `window.scrollTo(0, 0)` — which is itself smooth-animated under the global rule — and clicks **80 ms later**, mid-animation. The recorded symptom ("scrollY still 25 after 1.2 s") is what a fragment navigation fighting an in-flight smooth scroll looks like, and congo-pair scoring zero is equally explained by its reset being instant. Tasks 2–3 exist to find out which it is. **No page or global CSS is edited by this plan.**

---

## File Structure

**Create:**

| File | Responsibility |
|---|---|
| `tests/render/lib/freshness.ts` | Pure fs comparison: is anything under `src/`, `public/`, `astro.config.mjs`, `package.json` newer than the newest file in `dist/`? Injectable root so it is unit-testable. |
| `tests/render/lib/runCheck.ts` | The single call site every check goes through. Validates the result contract (row cap, `count` integrity, id/family match) so a malformed check fails loudly instead of skewing the ledger. |
| `scripts/rework_ledger.py` | Computes one window from git using the canonical command; appends to `data/quality/rework-ledger.json`. Import-safe (no work at import time). |
| `scripts/quality_report.py` | The one-screen report: rework trend, first-run defects by family, worst family, open overrides, rules with no backing test. |
| `data/quality/rework-ledger.json` | The lagging indicator, one entry per measured window. |
| `data/quality/rule-index.json` | Every rule, classed `enforced: test` (with its check id) or `enforced: judgment` (with why no test can exist). The deletion-candidate list is computed from it. |
| `skills/cag-learning-loop.md` | Layer 3. The 5-step end-of-build procedure whose step 3 charges escaped defects to the harness. |
| `tests/test_rework_ledger.py` | pytest for the git parsing and window math. |
| `tests/test_quality_report.py` | pytest for the report's derivations, including the deletion-candidate rule. |

**Modify:**

| File | Change |
|---|---|
| `tests/render/lib/probes.ts` | Add `resetScrollInstant` + `waitForScrollSettle`. |
| `tests/render/checks/nav.ts` | Instant reset, poll for settle, one root-cause row per failure mode. |
| `tests/render/lib/registry.ts` | `Defect.count` becomes required; export `MAX_DEFECT_ROWS`. |
| `tests/render/checks/img.ts`, `checks/layout.ts` | Add `count` to every emitted defect. |
| `tests/render/pages.spec.ts` | `beforeAll` freshness gate; route checks through `runCheck`. |
| `tests/render/meta.spec.ts` | Route checks through `runCheck`; add freshness + contract unit tests. |
| `tests/render/fixtures/known_good/nav-jump-target-lands.html` | Keep `scroll-behavior:smooth` (matching the live site) and lengthen the document, so the fixture proves the check tolerates smooth rather than only testing `auto`. |
| `scripts/build_scorecard.mjs` | Emit `defects` (rows) **and** `instances` (sum of `count`) per family; bump `harness_version` to `2.0.0`. |
| `package.json` | Add `test:render:report`. |
| `CLAUDE.md` | One new rule (No Test, No Rule) + three Scripts entries. |

---

## Task 1: `dist/` freshness — a stale server may not be measured silently

**Files:**
- Create: `tests/render/lib/freshness.ts`
- Test: `tests/render/meta.spec.ts` (append; no browser needed)
- Modify: `tests/render/pages.spec.ts`

- [ ] **Step 1: Write the failing test**

Append to `tests/render/meta.spec.ts`, after the existing `for (const check of registry)` loop:

```ts
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
```

Add these imports to the top of `tests/render/meta.spec.ts`:

```ts
import { mkdtempSync, mkdirSync, writeFileSync, utimesSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { checkDistFreshness } from './lib/freshness.js';
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run test:render:meta`
Expected: FAIL — `Cannot find module './lib/freshness.js'`.

- [ ] **Step 3: Write the implementation**

Create `tests/render/lib/freshness.ts`:

```ts
import { existsSync, readdirSync, statSync } from 'node:fs';
import { join, relative, resolve } from 'node:path';

/**
 * Directory names that are never source, wherever they appear. `src/pages/node_modules/.vite/`
 * exists in this repo — walking it costs thousands of stats and would refuse every run the
 * moment Vite touched a vendored dep.
 */
const SKIP = new Set(['node_modules', '.vite', '.git', '.DS_Store', '.astro', '.cache']);

/** Source paths whose mtime should force a rebuild. Missing entries are skipped, not fatal. */
const SOURCES = ['src', 'public', 'astro.config.mjs', 'package.json'];

export interface Freshness {
  fresh: boolean;
  /** Always populated — on failure it names the offending file AND the remedy. */
  reason: string;
}

function newest(path: string): { path: string; ms: number } {
  let best = { path, ms: 0 };
  const walk = (dir: string): void => {
    let entries;
    try {
      entries = readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const e of entries) {
      if (SKIP.has(e.name)) continue;
      const p = join(dir, e.name);
      if (e.isDirectory()) {
        walk(p);
      } else {
        let ms = 0;
        try {
          ms = statSync(p).mtimeMs;
        } catch {
          continue;
        }
        if (ms > best.ms) best = { path: p, ms };
      }
    }
  };
  let st;
  try {
    st = statSync(path);
  } catch {
    return best;
  }
  if (st.isDirectory()) walk(path);
  else best = { path, ms: st.mtimeMs };
  return best;
}

/**
 * A stale `dist/` is the quietest way this harness can lie: every check passes, every
 * number is real, and all of them describe a build nobody is shipping. Refuse to measure.
 */
export function checkDistFreshness(root: string = process.cwd()): Freshness {
  const dist = resolve(root, 'dist');
  if (!existsSync(dist)) {
    return { fresh: false, reason: 'dist/ does not exist — run `npm run build` first' };
  }
  const newestDist = newest(dist);
  if (newestDist.ms === 0) {
    return { fresh: false, reason: 'dist/ contains no files — run `npm run build` first' };
  }

  for (const rel of SOURCES) {
    const p = resolve(root, rel);
    if (!existsSync(p)) continue;
    const n = newest(p);
    if (n.ms > newestDist.ms) {
      const ageMin = Math.round((n.ms - newestDist.ms) / 60000);
      return {
        fresh: false,
        reason:
          `${relative(root, n.path)} is ${ageMin} min newer than the newest file in dist/ ` +
          `(${relative(root, newestDist.path)}) — run \`npm run build\` first. ` +
          `Measuring a stale dist/ produces real numbers about a build nobody ships.`,
      };
    }
  }
  return { fresh: true, reason: `dist/ is current (newest: ${relative(root, newestDist.path)})` };
}
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `npm run test:render:meta`
Expected: PASS — 5 new freshness tests green, existing tests unchanged.

- [ ] **Step 5: Wire the gate into the page suite**

In `tests/render/pages.spec.ts`, add to the imports:

```ts
import { checkDistFreshness } from './lib/freshness.js';
```

and insert directly above the `for (const target of targets.pages)` loop:

```ts
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
```

- [ ] **Step 6: Prove the gate fires on the real repo**

Run:
```bash
touch src/styles/global.css && npx playwright test -c tests/render/playwright.config.ts pages.spec.ts --project=vp375 --grep congo-african-grey-parrot-pair 2>&1 | tail -20
```
Expected: FAIL with `RENDER HARNESS REFUSES TO MEASURE: src/styles/global.css is ... newer`.

Then rebuild and confirm it clears:
```bash
npm run build && npx playwright test -c tests/render/playwright.config.ts pages.spec.ts --project=vp375 --grep congo-african-grey-parrot-pair 2>&1 | tail -20
```
Expected: the `[freshness] dist/ is current` line, and the test proceeds.

**If the first command does NOT fail, stop.** The gate is decorative and you have reproduced nothing.

- [ ] **Step 7: Commit**

```bash
git add tests/render/lib/freshness.ts tests/render/meta.spec.ts tests/render/pages.spec.ts
git commit -m "$(cat <<'EOF'
test(render): refuse to measure a stale dist/

A stale dist/ is the quietest lie available to this harness: every check
passes, every number is real, and all of them describe a build nobody ships.
The gate compares the newest mtime under src/ public/ astro.config.mjs
package.json against the newest file in dist/, skipping the vendored
src/pages/node_modules/.vite tree that would otherwise refuse every run.

Gated in pages.spec only. meta.spec tests checkers against fixtures, where
dist/ is irrelevant, and must stay runnable while a build is broken.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: NAV — remove the timing confound before diagnosing anything

The current check resets with a smooth-animated `scrollTo(0, 0)` and clicks 80 ms into that animation, then waits a fixed 1200 ms. Both halves are suspect. Fix the measurement first; only a failure that survives an instant reset and a polled settle is evidence about a page.

**Files:**
- Modify: `tests/render/lib/probes.ts`
- Modify: `tests/render/fixtures/known_good/nav-jump-target-lands.html`
- Modify: `tests/render/checks/nav.ts`

- [ ] **Step 1: Make the known_good fixture reproduce the real conditions**

The current known_good uses `scroll-behavior:auto` and 1600px sections. The live site uses `smooth` on documents up to 26,000px, so the fixture pair currently proves only that the check can tell `auto` from `smooth` — not that it can measure a correct page that uses `smooth`.

Replace `tests/render/fixtures/known_good/nav-jump-target-lands.html` entirely with:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>clean jump, smooth scrolling</title>
<style>
/* MATCHES THE LIVE SITE: src/styles/global.css:104 sets html{scroll-behavior:smooth}
   inside @media (prefers-reduced-motion: no-preference). A known_good fixture that
   used `auto` would let the check pass by being unable to measure smooth at all. */
html{scroll-behavior:smooth}
body{margin:0;font:16px/1.5 system-ui}
header{position:sticky;top:0;height:96px;background:#2D6A4F;color:#fff;display:flex;align-items:center}
nav a{color:#fff;margin-right:12px;display:inline-block;min-width:44px;min-height:44px}
/* Long enough that a smooth scroll between the two targets covers ~24,000px, which is
   the distance the real for-sale pages ask for. A 1600px fixture finishes inside any
   fixed wait and so cannot exercise the settle logic. */
section{min-height:12000px;padding:0}
h2{margin:0;scroll-margin-top:112px}
</style></head><body>
<header><nav><a href="#care">Care</a> <a href="#shipping">Shipping</a></nav></header>
<section><h2 id="care">Care</h2><p>Copy.</p></section>
<section><h2 id="shipping">Shipping</h2><p>Copy.</p></section>
</body></html>
```

- [ ] **Step 2: Run the meta gate and RECORD what the current check does to it**

Run: `npx playwright test -c tests/render/playwright.config.ts meta.spec.ts --grep "nav-jump-target-lands" 2>&1 | tail -30`

Expected: **FAIL** on `is silent on the known_good fixture` — the check reports landings outside the band on a fixture that is correct by construction (every target carries `scroll-margin-top:112px` clearing the 96px header).

**If it PASSES, stop and read the output before changing any code.** A green here means the smooth-scroll race does not reproduce at this document length, and the rest of this task is aimed at a defect you have not observed. In that case, raise `min-height` to `24000px` and re-run; if it still passes, record that in the plan file, mark Task 2 as "not reproduced", and go straight to Task 3 — do not write a fix for a bug you cannot show.

- [ ] **Step 3: Add the two probes**

Append to `tests/render/lib/probes.ts`:

```ts
/**
 * Return to the top with NO animation, whatever `scroll-behavior` the page declares.
 *
 * `window.scrollTo(0, 0)` is itself smooth-animated under `html{scroll-behavior:smooth}`,
 * which every page on this site sets. The previous NAV check reset that way and clicked
 * 80ms later — starting a fragment navigation while a full-document smooth scroll was
 * still in flight. `behavior:'instant'` overrides the computed style; `'auto'` does not
 * (in ScrollOptions, 'auto' means "use the computed style", which is the trap).
 */
export async function resetScrollInstant(page: Page): Promise<void> {
  await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' as ScrollBehavior }));
  await page.waitForTimeout(50);
}

export interface ScrollSettle {
  y: number;
  /** False means it was still moving when the budget ran out — that is a finding, not a landing. */
  settled: boolean;
  ms: number;
}

/**
 * Poll until `scrollY` stops changing, or give up and say so.
 *
 * Replaces a fixed 1200ms wait, which is simultaneously too long for an instant jump and
 * too short for a smooth scroll across 26,000px — so it reported false failures on slow
 * pages and wasted 20 minutes per run on fast ones.
 *
 * Polls with setTimeout, not requestAnimationFrame: rAF is throttled to a stop in a page
 * that is not painting, and a probe that silently never ticks reports `settled:false` on a
 * page that is perfectly fine. See MEMORY reference_intersectionobserver_needs_painting_page.
 */
export async function waitForScrollSettle(
  page: Page,
  opts: { maxMs?: number; stableTicks?: number; tickMs?: number } = {},
): Promise<ScrollSettle> {
  const { maxMs = 5000, stableTicks = 5, tickMs = 32 } = opts;
  return page.evaluate(
    ({ maxMs, stableTicks, tickMs }) =>
      new Promise<{ y: number; settled: boolean; ms: number }>((resolve) => {
        const t0 = Date.now();
        let last = window.scrollY;
        let stable = 0;
        const tick = () => {
          const y = window.scrollY;
          if (y === last) stable++;
          else {
            stable = 0;
            last = y;
          }
          const ms = Date.now() - t0;
          if (stable >= stableTicks) return resolve({ y, settled: true, ms });
          if (ms >= maxMs) return resolve({ y, settled: false, ms });
          setTimeout(tick, tickMs);
        };
        setTimeout(tick, tickMs);
      }),
    { maxMs, stableTicks, tickMs },
  );
}
```

- [ ] **Step 4: Use them in the NAV check**

In `tests/render/checks/nav.ts`, change the import line at the top from:

```ts
import { measureTopChrome } from '../lib/probes.js';
```

to:

```ts
import { measureTopChrome, resetScrollInstant, waitForScrollSettle } from '../lib/probes.js';
```

Then, inside `nav-jump-target-lands`'s `for (const href of targets)` loop, replace these two lines:

```ts
        await page.evaluate(() => window.scrollTo(0, 0));
        await page.waitForTimeout(80);
```

with:

```ts
        await resetScrollInstant(page);
```

and replace this block:

```ts
        // Long enough for a smooth scroll to finish. The recorded failure was
        // "click a chip, wait 1.2s, scrollY is still 25" — a shorter wait would
        // report a false failure on a page whose animation simply had not ended.
        await page.waitForTimeout(1200);
```

with:

```ts
        const settle = await waitForScrollSettle(page);
        if (!settle.settled) {
          defects.push({
            checkId: 'nav-jump-target-lands',
            family: 'NAV' as const,
            viewport,
            message: `${href} was still scrolling after ${settle.ms}ms at y=${settle.y}`,
          });
          continue;
        }
```

- [ ] **Step 5: Run the meta gate to verify it passes**

Run: `npx playwright test -c tests/render/playwright.config.ts meta.spec.ts --grep "nav-jump-target-lands" 2>&1 | tail -20`
Expected: PASS on both fixtures — fires on `known_broken` (no `scroll-margin-top`), silent on `known_good` (smooth scrolling, correct margins, 24,000px of travel).

- [ ] **Step 6: Re-measure ONE real page and record the delta**

Run:
```bash
npx playwright test -c tests/render/playwright.config.ts pages.spec.ts --project=vp375 --grep "timneh-african-grey-for-sale" 2>&1 | tail -30
cat data/quality/raw/timneh-african-grey-for-sale-vp375.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(len([x for x in d['defects'] if x['checkId']=='nav-jump-target-lands']), 'NAV rows; examined', d['examined']['nav-jump-target-lands'])"
```

Baseline for this page at all three viewports was 52 NAV rows total. Record the new single-viewport number in the commit message. **Whatever it is, it is the finding** — do not adjust the check to reach a number you expected.

- [ ] **Step 7: Commit**

```bash
git add tests/render/lib/probes.ts tests/render/checks/nav.ts tests/render/fixtures/known_good/nav-jump-target-lands.html
git commit -m "$(cat <<'EOF'
fix(render): the NAV check was racing its own scroll reset

nav-jump-target-lands reset with window.scrollTo(0,0) — itself smooth-animated
under the global html{scroll-behavior:smooth} — then clicked 80ms into that
animation and waited a fixed 1200ms. It was measuring a fragment navigation
fighting an in-flight smooth scroll, on every page except the one page that
sets scroll-behavior:auto. That is the whole shape of the 337-vs-0 split.

resetScrollInstant uses behavior:'instant', which overrides the computed style
('auto' does not — it MEANS "use the computed style"). waitForScrollSettle
polls scrollY with setTimeout, not rAF, because rAF stalls on a non-painting
page and would report settled:false on a page that is fine.

known_good now uses scroll-behavior:smooth over 24,000px of travel, matching
the live site. The old fixture used `auto`, so the pair proved only that the
check could tell the two apart.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: NAV — one root cause per page, not one row per anchor

**Files:**
- Modify: `tests/render/checks/nav.ts`

- [ ] **Step 1: Write the failing test**

Append to `tests/render/meta.spec.ts`:

```ts
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
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npx playwright test -c tests/render/playwright.config.ts meta.spec.ts --grep "reports causes" 2>&1 | tail -25`
Expected: FAIL — `expected at most 3 rows (one per failure mode); got 20`, and a TypeScript error on `d.count` (the field does not exist yet; Task 4 makes it required — for now it is read with `?? 0`, so only the row-count assertion fails).

- [ ] **Step 3: Rewrite the check body**

Replace the entire second `register({ ... })` block in `tests/render/checks/nav.ts` (the `nav-jump-target-lands` one, currently lines 43–155) with:

```ts
/**
 * Names the ONE page-level thing most likely to be producing the landings we measured.
 * Returns null rather than guessing — a wrong root cause is worse than none, because it
 * sends the next person to edit a file that was never the problem.
 */
async function diagnoseLandingCause(page: Page, chromeHeight: number): Promise<string | null> {
  return page.evaluate((chromeH: number) => {
    const docH = document.documentElement.scrollHeight;
    const behavior = getComputedStyle(document.documentElement).scrollBehavior;

    const ids = new Set(
      Array.from(document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]'))
        .map((a) => (a.getAttribute('href') || '').slice(1))
        .filter(Boolean)
        .map((h) => decodeURIComponent(h)),
    );
    let seen = 0;
    let short = 0;
    for (const id of ids) {
      const el = document.getElementById(id);
      if (!el) continue;
      seen++;
      if (parseFloat(getComputedStyle(el).scrollMarginTop || '0') < chromeH - 8) short++;
    }

    if (seen && short === seen) {
      return `every target's scroll-margin-top is under the ${chromeH}px of pinned chrome`;
    }
    if (short) {
      return `${short} of ${seen} targets have scroll-margin-top under the ${chromeH}px of pinned chrome`;
    }
    if (behavior === 'smooth' && docH > 8000) {
      return `html{scroll-behavior:smooth} on a ${docH}px document`;
    }
    return null;
  }, chromeHeight);
}

register({
  id: 'nav-jump-target-lands',
  family: 'NAV',
  severity: 'advisory',
  describe: 'clicking an in-page link must leave its target visible below the sticky chrome',
  minExamined: 2,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const chrome = await measureTopChrome(page);

    if (chrome.implausible) {
      return {
        examined: 0,
        defects: [
          {
            checkId: 'nav-jump-target-lands',
            family: 'NAV' as const,
            viewport,
            count: 1,
            message: `pinned chrome measures ${chrome.height}px, over 40% of the viewport — refusing to judge landings against a number that is probably wrong. Parts: ${JSON.stringify(chrome.parts)}`,
          },
        ],
      };
    }

    // One entry per unique target, and only targets reachable from a link with a
    // real box. 0x0 duplicates and sr-only skip links are not user-facing chips;
    // clicking them via a synthetic pointer event hangs for 30s and then throws.
    const targets: string[] = await page.evaluate(() => {
      const byHref = new Map<string, boolean>();
      for (const a of Array.from(document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]'))) {
        const href = a.getAttribute('href') || '';
        if (href.length < 2) continue;
        if (!document.getElementById(decodeURIComponent(href.slice(1)))) continue;
        const box = a.getBoundingClientRect();
        const cs = getComputedStyle(a);
        if (cs.visibility === 'hidden' || cs.display === 'none') continue;
        if (box.width < 8 || box.height < 8) continue; // 0x0 dupes and sr-only
        byHref.set(href, true);
      }
      return Array.from(byHref.keys());
    });

    const lo = chrome.height - 8;
    const hi = chrome.height + 60;

    // Three buckets, three rows. Never one row per anchor: NAV supplied 81% of the
    // first baseline's headline number by counting granularity alone, which made the
    // family totals incomparable and pointed the next-action list at the wrong family.
    const missed: string[] = [];
    const unsettled: string[] = [];
    const untestable: string[] = [];

    for (const href of targets) {
      try {
        await resetScrollInstant(page);

        // Click the first link for this href that has a real box, in the page itself.
        // This triggers the browser's own fragment navigation — the behaviour a user
        // gets — without requiring viewport visibility.
        const clicked = await page.evaluate((h: string) => {
          const links = Array.from(
            document.querySelectorAll<HTMLAnchorElement>(`a[href="${h.replace(/"/g, '\\"')}"]`),
          );
          const el = links.find((a) => {
            const b = a.getBoundingClientRect();
            return b.width >= 8 && b.height >= 8;
          });
          if (!el) return false;
          el.click();
          return true;
        }, href);

        if (!clicked) {
          untestable.push(`${href} (no clickable box)`);
          continue;
        }

        const settle = await waitForScrollSettle(page);
        if (!settle.settled) {
          unsettled.push(`${href} (still moving at ${settle.ms}ms, y=${settle.y})`);
          continue;
        }

        const top = await page.evaluate((h: string) => {
          const el = document.getElementById(decodeURIComponent(h.slice(1)));
          return el ? Math.round(el.getBoundingClientRect().top) : NaN;
        }, href);

        if (Number.isNaN(top)) {
          untestable.push(`${href} (target vanished after navigation)`);
        } else if (top < lo || top > hi) {
          missed.push(`${href}@${top}px`);
        }
      } catch (err) {
        // A thrown check drops the page from the scorecard silently. Never throw.
        untestable.push(`${href} (${(err as Error).message.split('\n')[0]})`);
      }
    }

    const defects: Defect[] = [];
    const chromeDesc = `${chrome.height}px = ${chrome.parts.map((p) => `${p.tag}:${p.height}`).join('+')}`;

    if (missed.length) {
      const cause = await diagnoseLandingCause(page, chrome.height);
      defects.push({
        checkId: 'nav-jump-target-lands',
        family: 'NAV' as const,
        viewport,
        count: missed.length,
        message:
          `${missed.length} of ${targets.length} in-page links land outside ${lo}-${hi}px ` +
          `(measured chrome ${chromeDesc})` +
          (cause ? ` — ROOT CAUSE: ${cause}` : ' — no single page-level cause identified') +
          `; first: ${missed.slice(0, 5).join(', ')}`,
      });
    }
    if (unsettled.length) {
      defects.push({
        checkId: 'nav-jump-target-lands',
        family: 'NAV' as const,
        viewport,
        count: unsettled.length,
        message: `${unsettled.length} of ${targets.length} links never stopped scrolling; first: ${unsettled.slice(0, 3).join(', ')}`,
      });
    }
    if (untestable.length) {
      defects.push({
        checkId: 'nav-jump-target-lands',
        family: 'NAV' as const,
        viewport,
        count: untestable.length,
        message: `${untestable.length} of ${targets.length} links could not be tested; first: ${untestable.slice(0, 3).join(', ')}`,
      });
    }

    return { examined: targets.length, defects };
  },
});
```

Also add `count: 1,` to the single defect emitted by `nav-anchors-resolve` (the first `register` block), immediately after its `viewport,` line — Task 4 makes the field required, and leaving it out now produces a compile error there.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `npm run test:render:meta`
Expected: PASS — including `a page with many broken anchors yields ONE row per failure mode` (20 targets → 1 row, `count: 20`).

- [ ] **Step 5: Commit**

```bash
git add tests/render/checks/nav.ts tests/render/meta.spec.ts
git commit -m "$(cat <<'EOF'
fix(render): NAV names one root cause per page instead of 337 rows

The check emitted one defect row per anchor, so it supplied 81% of the first
baseline's headline number by counting granularity alone, and the "worst
family" ranking that the ledger will be built on pointed at NAV for a reason
that had nothing to do with severity.

Now three buckets, three rows, each carrying `count`: landings outside the
band, links that never settled, links that could not be tested. The landing
row names the page-level cause — targets whose scroll-margin-top sits under
the measured pinned chrome, or html{scroll-behavior:smooth} on a long
document — and returns null rather than guessing, because a wrong root cause
sends the next person to edit a file that was never the problem.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: One unit for every defect row

A family total is only meaningful if every family counts the same thing. Make `count` required, and enforce the row cap at the one call site every check goes through, so the contract holds on real pages and not only on two-anchor fixtures.

**Files:**
- Modify: `tests/render/lib/registry.ts`
- Create: `tests/render/lib/runCheck.ts`
- Modify: `tests/render/checks/img.ts`, `tests/render/checks/layout.ts`
- Modify: `tests/render/meta.spec.ts`, `tests/render/pages.spec.ts`
- Modify: `scripts/build_scorecard.mjs`

- [ ] **Step 1: Write the failing test**

Append to `tests/render/meta.spec.ts`:

```ts
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
```

Add to `tests/render/meta.spec.ts`'s imports:

```ts
import { registry, MAX_DEFECT_ROWS, type Check, type Defect } from './lib/registry.js';
import { runCheck } from './lib/runCheck.js';
```

(replacing the existing `import { registry } from './lib/registry.js';`)

- [ ] **Step 2: Run the test to verify it fails**

Run: `npm run test:render:meta`
Expected: FAIL — `Cannot find module './lib/runCheck.js'` and `MAX_DEFECT_ROWS` is not exported.

- [ ] **Step 3: Make `count` required in the registry**

In `tests/render/lib/registry.ts`, replace the `Defect` interface with:

```ts
export interface Defect {
  checkId: string;
  family: Family;
  viewport: number;
  /**
   * How many individual units failed.
   *
   * A defect ROW is one failure MODE of one check at one viewport. `count` carries the
   * magnitude. Without this split the first baseline mixed units: layout-min-font-size
   * folded 108 undersized text nodes into one row while nav-jump-target-lands emitted one
   * row per anchor, so NAV supplied 81% of the headline number by counting granularity
   * alone — and "which family produces the most defects", the whole point of the ledger,
   * was answering a question about aggregation style.
   */
  count: number;
  message: string;
}
```

and append to the same file:

```ts
/**
 * The cap on defect ROWS a single check may emit for one page at one viewport.
 *
 * Three is one row per failure mode, which is as many distinct modes as any check on this
 * site has. A check that wants a fourth is really asking to report instances, and instances
 * belong in `count`.
 */
export const MAX_DEFECT_ROWS = 3;
```

- [ ] **Step 4: Write the contract validator**

Create `tests/render/lib/runCheck.ts`:

```ts
import type { Page } from '@playwright/test';
import { MAX_DEFECT_ROWS, type Check, type CheckResult } from './registry.js';

/**
 * The single call site for every check, in both meta.spec and pages.spec.
 *
 * Validating here rather than inside each check means the contract binds on real pages,
 * where a check meets sixty-two anchors, and not only on fixtures, where it meets two.
 * Every violation throws with the check id in the message, because a malformed result that
 * merely warns becomes a permanent skew in the ledger nobody can see.
 */
export async function runCheck(check: Check, page: Page, viewport: number): Promise<CheckResult> {
  const result = await check.run(page, viewport);

  if (!Number.isInteger(result.examined) || result.examined < 0) {
    throw new Error(
      `${check.id}: examined must be a non-negative integer, got ${JSON.stringify(result.examined)}`,
    );
  }

  if (result.defects.length > MAX_DEFECT_ROWS) {
    throw new Error(
      `${check.id}: emitted ${result.defects.length} defect rows, cap is ${MAX_DEFECT_ROWS}. ` +
        `A row is one failure MODE; instances belong in \`count\`. Reporting per-instance makes ` +
        `this family's total incomparable with every other family's.`,
    );
  }

  for (const d of result.defects) {
    if (d.checkId !== check.id) {
      throw new Error(`${check.id}: emitted a row with checkId "${d.checkId}"`);
    }
    if (d.family !== check.family) {
      throw new Error(`${check.id}: emitted a row with family "${d.family}", expected ${check.family}`);
    }
    if (!Number.isInteger(d.count) || d.count < 1) {
      throw new Error(
        `${check.id}: every defect row needs an integer count >= 1, got ${JSON.stringify(d.count)}`,
      );
    }
    if (!d.message || !d.message.trim()) {
      throw new Error(`${check.id}: emitted a row with an empty message`);
    }
  }

  return result;
}
```

- [ ] **Step 5: Add `count` to the four remaining defect emitters**

In `tests/render/checks/img.ts`, add `count: r.count,` after the `viewport,` line in the `img-srcset-within-2x` oversized-images defect; add `count: r.skipped.length,` in its failed-to-decode defect; add `count: r.missing.length,` and `count: r.dupes.length,` in the two `img-alt-present-and-unique` defects.

In `tests/render/checks/layout.ts`, add `count: 1,` after `viewport,` in `layout-no-horizontal-overflow` (the check judges exactly one unit — the document's own overflow), `count: r.count,` in `layout-min-font-size`, and `count: r.count,` in `layout-tap-target-size`.

- [ ] **Step 6: Route both spec files through the validator**

In `tests/render/meta.spec.ts`, replace both occurrences of:

```ts
      const result = await check.run(page, viewport);
```

with:

```ts
      const result = await runCheck(check, page, viewport);
```

In `tests/render/pages.spec.ts`, add to the imports:

```ts
import { runCheck } from './lib/runCheck.js';
```

and replace:

```ts
      const result = await check.run(page, viewport);
```

with:

```ts
      const result = await runCheck(check, page, viewport);
```

- [ ] **Step 7: Run the tests to verify they pass**

Run: `npm run test:render:meta`
Expected: PASS — 7 new contract tests plus the existing suite. Any TypeScript error here means a `count` was missed in Step 5; the compiler names the file and line.

- [ ] **Step 8: Report rows AND instances in the scorecard**

In `scripts/build_scorecard.mjs`, replace the per-slug loop body (currently lines 60–88) with:

```js
for (const [slug, parts] of bySlug) {
  // Two numbers, deliberately. `defects` counts ROWS — one failure mode of one check at
  // one viewport — and is the only number comparable across families. `instances` sums
  // `count` and is the magnitude. The first baseline had only the first, computed from
  // checks that disagreed about what a row was.
  const defectsByFamily = {};
  const instancesByFamily = {};
  const examined = { pages: 1, checks: 0 };
  const details = [];
  for (const part of parts) {
    examined.checks = Math.max(examined.checks, Object.keys(part.examined).length);
    for (const d of part.defects) {
      defectsByFamily[d.family] = (defectsByFamily[d.family] || 0) + 1;
      instancesByFamily[d.family] = (instancesByFamily[d.family] || 0) + (d.count ?? 1);
      details.push({
        viewport: part.viewport,
        checkId: d.checkId,
        count: d.count ?? 1,
        message: d.message,
      });
    }
  }
  const total = Object.values(defectsByFamily).reduce((a, b) => a + b, 0);
  const totalInstances = Object.values(instancesByFamily).reduce((a, b) => a + b, 0);
  grandTotal += total;
  const card = {
    slug,
    date,
    page_type: parts[0].page_type,
    run: runLabel,
    harness_version: '2.0.0',
    viewports: parts.map((p) => p.viewport).sort((a, b) => a - b),
    examined,
    defects: defectsByFamily,
    instances: instancesByFamily,
    total,
    total_instances: totalInstances,
    overrides: parts.flatMap((p) => p.overrides ?? []),
    details,
  };
  writeFileSync(resolve(OUT, `${slug}-${date}.json`), JSON.stringify(card, null, 2));
  console.log(`${String(total).padStart(3)} rows ${String(totalInstances).padStart(4)} inst  ${slug}`);
}
```

and replace the summary line near the bottom:

```js
console.log(`---\n${grandTotal} defects across ${bySlug.size} pages (run=${runLabel})`);
```

with:

```js
console.log(
  `---\n${grandTotal} defect ROWS across ${bySlug.size} pages (run=${runLabel}, harness 2.0.0). ` +
    `Rows are comparable across families; instances are not.`,
);
```

- [ ] **Step 9: Commit**

```bash
git add tests/render/lib/registry.ts tests/render/lib/runCheck.ts tests/render/checks/img.ts tests/render/checks/layout.ts tests/render/meta.spec.ts tests/render/pages.spec.ts scripts/build_scorecard.mjs
git commit -m "$(cat <<'EOF'
test(render): one unit per defect row, enforced at the call site

`count` is now required on every defect, a row is one failure MODE, and
MAX_DEFECT_ROWS=3 is enforced in lib/runCheck.ts — the single call site both
spec files use. Validating there rather than inside each check means the
contract binds on a real page with sixty-two anchors, not only on a fixture
with two.

Scorecards now carry both `defects` (rows, comparable across families) and
`instances` (magnitude, not comparable). harness_version 2.0.0; the
2026-07-31 baseline stays as written and is 1.0.0 data.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: Run both commands for real, and record what is actually there

Nothing in Phase 1 was ever run end to end by the breeder. This task produces the first Phase-2 baseline and the first counted override.

**Files:**
- Create: `data/quality/scorecards/*-2026-08-01.json` (9 files, generated)
- Modify: `docs/reference/technical-seo-fixes-backlog.md`

- [ ] **Step 1: Confirm the checkers before believing anything about the pages**

Run: `npm run test:render:meta`
Expected: all tests PASS in roughly 30 s. **If any test fails, stop here** — page results measured by a failing gate are not evidence. This is the ordering `skills/cag-gate-integrity.md` exists to enforce.

- [ ] **Step 2: Build, so the freshness gate has something current to measure**

Run: `npm run build`
Expected: Astro build completes, then Pagefind indexes `dist/`.

- [ ] **Step 3: Run the page suite with the counted override**

The blocking check `img-srcset-within-2x` fires on all nine pages. It fired on something real — `ida-brim-nashville-tn-review.webp` decodes at 640px into a 48px slot (13.33×) — so it keeps its blocking severity. The regen is asset work, out of scope for this layer (spec §7), so it ships as a counted override rather than a quiet demotion.

Run:
```bash
RENDER_OVERRIDE="img-srcset-within-2x:33 review avatars and card images ship at up to 13.3x their painted width; regen queued in docs/reference/technical-seo-fixes-backlog.md, tracked as an open override in quality_report.py" \
  npm run test:render:pages 2>&1 | tail -40
```
Expected: ~7 minutes; every page test passes with the override in force; no `RENDER HARNESS REFUSES TO MEASURE` line.

- [ ] **Step 4: Build the scorecards**

Run: `node scripts/build_scorecard.mjs --run first`
Expected: nine lines of `<rows> rows <instances> inst  <slug>`, then the summary, then the `1 OVERRIDE(S) IN EFFECT` block naming `img-srcset-within-2x`.

**If it prints `FAIL: expected 27 partials, found N`, do not re-run and hope.** A missing partial means a page test crashed and wrote nothing, which is the worst failure mode this harness has. Find that page in the Playwright output first.

- [ ] **Step 5: Record the delta against the 2026-07-31 baseline**

Run:
```bash
python3 - <<'PY'
import json, glob, collections
def load(date):
    out = {}
    for f in glob.glob(f'data/quality/scorecards/*-{date}.json'):
        d = json.load(open(f))
        out[d['slug']] = d
    return out
old, new = load('2026-07-31'), load('2026-08-01')
print(f"{'slug':<46}{'was':>6}{'now':>6}{'inst':>7}")
tw = tn = 0
for slug in sorted(old):
    w = old[slug]['total']; n = new.get(slug, {}).get('total', -1)
    i = new.get(slug, {}).get('total_instances', -1)
    tw += w; tn += max(n, 0)
    print(f'{slug:<46}{w:>6}{n:>6}{i:>7}')
print(f"{'TOTAL':<46}{tw:>6}{tn:>6}")
for fam in ['IMG','LAYOUT','NAV']:
    a = sum(d['defects'].get(fam,0) for d in old.values())
    b = sum(d['defects'].get(fam,0) for d in new.values())
    print(f'{fam:<8} rows {a:>5} -> {b:>5}')
PY
```

Paste the table into the commit message. **This is the finding, whatever it says.** If NAV did not drop, the smooth-scroll race was not the cause and the next task is to find out what is — not to adjust the check until the number looks right.

- [ ] **Step 6: Log the image finding to the backlog**

Append to `docs/reference/technical-seo-fixes-backlog.md`:

```markdown
## Oversized images across the for-sale cluster (render harness, 2026-08-01)

`img-srcset-within-2x` (blocking) fires on all 9 for-sale pages: **33 distinct files**
decode at more than 2× the width they paint at, measured in Playwright at
375/768/1280 with `deviceScaleFactor: 1`. Currently suppressed by a counted
`RENDER_OVERRIDE`, which `scripts/quality_report.py` prints on every run.

Worst offenders (ratio = naturalWidth ÷ painted CSS width):

| Ratio | File | Where |
|---|---|---|
| 13.33× | `ida-brim-nashville-tn-review.webp` | 640px asset in a 48px review avatar |
| 9.23× | `stanley-perkin-oceanside-ca-african-gray-bird-review.webp` | 480px → 52px |
| 9.23× | `jesse-ovalle-baton-rouge-la-african-grey-purchase-review.webp` | 480px → 52px |
| 6.73× | `african-grey-parrot-eggs-nesting-clutch.webp` | 1408px → 209px |
| 6.25× | `archie-obrien-farmingdale-ny-review.webp` | 300px → 48px |
| 4.86× | six `*-card.webp` bird cards | 640px → 132px |

Fix: regenerate review avatars at 2× their painted size (96–128px wide, not 480–640),
and give the bird cards a `srcset` rather than one 640px master. Roughly ten of the
33 sit between 2.0× and 2.5×, which is one retina asset for a slightly different
painted box — regenerate those last, or not at all. Re-run
`npm run test:render:pages` without the override to confirm; drop the override from
the run command once it is clean.
```

- [ ] **Step 7: Commit**

```bash
git add data/quality/scorecards docs/reference/technical-seo-fixes-backlog.md
git commit -m "$(cat <<'EOF'
test(render): first Phase-2 baseline, with one counted override

Paste the Step 5 delta table here.

img-srcset-within-2x stays blocking and ships a counted RENDER_OVERRIDE: it
fired on a 640px avatar painted at 48px, which is not arguable, so by the
promotion rule it earned its severity. The regen is asset work and is logged
to the technical-SEO backlog; quality_report.py prints the open override on
every run so it cannot quietly become permanent.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: The rework ledger

**Files:**
- Create: `scripts/rework_ledger.py`
- Create: `tests/test_rework_ledger.py`
- Create: `data/quality/rework-ledger.json` (generated)

- [ ] **Step 1: Write the failing test**

Create `tests/test_rework_ledger.py`:

```python
# tests/test_rework_ledger.py
#
# The rework rate is the one number this whole system is judged on (spec §5:
# 24.8% baseline, under 15% at 90 days). If the classifier drifts, the metric
# moves without the work changing — so the classifier is pinned here.
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import rework_ledger as R


def test_classifies_the_canonical_rework_prefixes():
    for subject in [
        "fix(render): settlePage was hanging",
        "revert: bad merge",
        "fix: broken canonical",
        "docs: correct the CITES appendix",
        "restore the deleted footer",
        "chore: undo the palette change",
        "repair the sitemap",
        "patch(nav): rail offset",
        "style: regress guard",
    ]:
        assert R.is_rework(subject), subject


def test_does_not_classify_ordinary_work_as_rework():
    for subject in [
        "feat: add the timneh for-sale page",
        "test(render): NAV/anchors-resolve",
        "docs: session brief",
        "build: bump astro",
        "perf: preload the hero",
    ]:
        assert not R.is_rework(subject), subject


def test_prefix_match_is_anchored_not_substring():
    """`affix` and `prefixed` contain 'fix' and are not rework."""
    assert not R.is_rework("feat: add affix helper")
    assert not R.is_rework("refactor: prefixed ids")


def test_rate_is_rework_over_total():
    w = R.window("2026-05-01", "2026-07-31", ["fix: a", "feat: b", "feat: c", "revert: d"])
    assert w["total"] == 4
    assert w["rework"] == 2
    assert w["rate"] == 0.5


def test_an_empty_window_is_rate_zero_not_a_crash():
    w = R.window("2026-01-01", "2026-01-02", [])
    assert w == {"from": "2026-01-01", "to": "2026-01-02", "total": 0, "rework": 0, "rate": 0.0,
                 "by_domain": {}}


def test_domains_are_the_seven_harness_families_plus_three():
    w = R.window("2026-05-01", "2026-07-31", [
        "fix(img): srcset regen",
        "fix: mobile overflow on the hero",
        "fix: jump rail anchors",
        "fix: dead css rules",
        "fix: the gate lied",
        "fix: schema dateModified",
        "fix: heading title case",
        "fix: duplicate content crossover",
        "fix: contrast on the clay pill",
        "fix: typo in the voice copy",
    ])
    assert set(w["by_domain"]) == {"IMG", "LAYOUT", "NAV", "CSS", "GATE", "SCHEMA", "SEM",
                                   "DUP", "A11Y", "COPY"}
    assert w["by_domain"]["IMG"] == 1


def test_appending_a_window_replaces_one_with_the_same_bounds(tmp_path):
    """Re-running for the same window must correct the entry, not double it."""
    p = tmp_path / "rework-ledger.json"
    R.append_window(p, R.window("2026-05-01", "2026-07-31", ["fix: a"]))
    R.append_window(p, R.window("2026-05-01", "2026-07-31", ["fix: a", "feat: b"]))
    data = json.loads(p.read_text())
    assert len(data["windows"]) == 1
    assert data["windows"][0]["total"] == 2


def test_windows_stay_sorted_by_start_date(tmp_path):
    p = tmp_path / "rework-ledger.json"
    R.append_window(p, R.window("2026-06-01", "2026-06-30", ["fix: a"]))
    R.append_window(p, R.window("2026-05-01", "2026-05-31", ["feat: b"]))
    data = json.loads(p.read_text())
    assert [w["from"] for w in data["windows"]] == ["2026-05-01", "2026-06-01"]
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m pytest tests/test_rework_ledger.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'rework_ledger'`.

- [ ] **Step 3: Write the implementation**

Create `scripts/rework_ledger.py`:

```python
#!/usr/bin/env python3
"""Compute the rework rate for a date window and append it to the ledger.

The rework rate is the metric the self-improving quality loop is judged on
(spec §5: 24.8% baseline on 2026-05-01..2026-07-31, target under 15% at 90 days).

Usage:
    python3 scripts/rework_ledger.py --from 2026-05-01 --to 2026-07-31
    python3 scripts/rework_ledger.py --last-30-days
    python3 scripts/rework_ledger.py --from ... --to ... --dry-run

Import-safe: nothing runs at import time, so the pytest suite can exercise the
classifier without touching git or the ledger file.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
from datetime import date, timedelta

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "quality" / "rework-ledger.json"

# The canonical classifier from spec §1. Anchored at the start for `fix`/`revert`
# so `refactor: prefixed ids` is not rework, and matched as a whole word elsewhere
# so `affix` is not either. Changing this regex changes the metric — if you must,
# recompute every historical window in the same commit and say so.
REWORK_RE = re.compile(
    r"^(fix|revert)\b|\bfix\(|\bcorrect|\brestore|\bregress|\bundo\b|\brepair|\bpatch\(",
    re.IGNORECASE,
)

# Domain buckets. The first seven are the harness families verbatim, so a ledger
# row and a scorecard row name the same thing; GATE, A11Y and COPY cover rework
# the harness does not measure.
DOMAIN_PATTERNS = [
    ("IMG", r"\bimg\b|image|srcset|webp|infographic|crop|alt text|photo|avatar"),
    ("LAYOUT", r"mobile|responsive|overflow|breakpoint|viewport|stack|grid|column|width"),
    ("NAV", r"\bnav\b|anchor|jump|rail|breadcrumb|link|scroll"),
    ("CSS", r"\bcss\b|token|palette|dead rule|class|style"),
    ("GATE", r"gate|probe|scan|audit|checker|harness|lied|false positive"),
    ("SCHEMA", r"schema|json-?ld|canonical|sitemap|\bdate|offer|product"),
    ("SEM", r"heading|h1|h2|h[3-6]\b|outline|title case|hierarch"),
    ("DUP", r"duplicat|crossover|dedup|sibling"),
    ("A11Y", r"a11y|accessib|contrast|wcag|aria|focus"),
    ("COPY", r"\bcopy\b|voice|typo|wording|prose|grammar"),
]


def is_rework(subject: str) -> bool:
    """True when a commit subject describes undoing or correcting earlier work."""
    return bool(REWORK_RE.search(subject))


def classify(subject: str) -> list:
    """Every domain a subject touches. Categories overlap by design — one commit
    can be both an IMG and a LAYOUT fix, and forcing a single bucket would
    understate whichever pattern happened to be listed second."""
    return [name for name, pat in DOMAIN_PATTERNS if re.search(pat, subject, re.IGNORECASE)]


def git_subjects(frm: str, to: str, cwd: pathlib.Path = ROOT) -> list:
    """Commit subjects in [frm, to). Raises rather than returning [] on a git error —
    an empty list would be recorded as a 0% rework window, which is a lie shaped
    exactly like success."""
    out = subprocess.run(
        ["git", "log", f"--since={frm}", f"--until={to}", "--pretty=format:%s"],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in out.stdout.splitlines() if line.strip()]


def window(frm: str, to: str, subjects: list) -> dict:
    total = len(subjects)
    rework = [s for s in subjects if is_rework(s)]
    by_domain = {}
    for s in rework:
        for d in classify(s):
            by_domain[d] = by_domain.get(d, 0) + 1
    return {
        "from": frm,
        "to": to,
        "total": total,
        "rework": len(rework),
        "rate": round(len(rework) / total, 4) if total else 0.0,
        "by_domain": by_domain,
    }


def append_window(path: pathlib.Path, w: dict) -> dict:
    """Upsert by (from, to) so a re-run corrects a window instead of duplicating it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        data = json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"definition": "see docs/superpowers/specs/2026-07-31-self-improving-quality-loop-design.md §1", "windows": []}
    data["windows"] = [x for x in data["windows"] if (x["from"], x["to"]) != (w["from"], w["to"])]
    data["windows"].append(w)
    data["windows"].sort(key=lambda x: x["from"])
    path.write_text(json.dumps(data, indent=2) + "\n")
    return data


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--from", dest="frm")
    ap.add_argument("--to", dest="to")
    ap.add_argument("--last-30-days", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    if args.last_30_days:
        today = date.today()
        frm, to = str(today - timedelta(days=30)), str(today)
    elif args.frm and args.to:
        frm, to = args.frm, args.to
    else:
        ap.error("give --from and --to, or --last-30-days")

    w = window(frm, to, git_subjects(frm, to))
    print(f"{frm} .. {to}: {w['rework']}/{w['total']} = {w['rate']:.1%} rework")
    for d, n in sorted(w["by_domain"].items(), key=lambda kv: -kv[1]):
        print(f"  {d:<8}{n:>5}")
    if args.dry_run:
        print("(dry run — ledger not written)")
        return 0
    append_window(LEDGER, w)
    print(f"wrote {LEDGER.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_rework_ledger.py -q`
Expected: `9 passed`.

- [ ] **Step 5: Write the baseline window and the current one**

Run:
```bash
python3 scripts/rework_ledger.py --from 2026-05-01 --to 2026-07-31
python3 scripts/rework_ledger.py --last-30-days
```
Expected: the first prints `211/851 = 24.8% rework` (the spec recorded 214/862 on 2026-07-31; the drift is the window boundary and later commits — the ledger records what is measured today, not what the spec remembered). The second prints the trailing 30-day rate. `data/quality/rework-ledger.json` now holds two windows, sorted.

**On the anchored regex.** `REWORK_RE` adds `\b` boundaries the spec's shell one-liner does not have, so `refactor: prefixed ids` and `feat: add affix helper` stay out of the numerator. Measured on this corpus 2026-08-01, both classifiers return **211 of 851 — identical**. The anchoring buys future safety at zero cost to the baseline, so the 24.8% figure carries forward unchanged and no historical window needs recomputing.

- [ ] **Step 6: Commit**

```bash
git add scripts/rework_ledger.py tests/test_rework_ledger.py data/quality/rework-ledger.json
git commit -m "$(cat <<'EOF'
feat(quality): the rework ledger — the lagging indicator, pinned by tests

The rework rate is the one number this system is judged on, so the classifier
is pinned in tests/test_rework_ledger.py rather than left as a shell one-liner
that can drift silently. Anchored matching keeps `refactor: prefixed ids` and
`feat: add affix helper` out of the numerator.

git_subjects raises rather than returning [] on a git error: an empty window
would be recorded as 0% rework, which is a lie shaped exactly like success.
Windows upsert by (from, to), so re-running corrects an entry instead of
double-counting it.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: `quality_report.py` — one screen, including the deletion-candidate list

**Files:**
- Create: `data/quality/rule-index.json`
- Create: `scripts/quality_report.py`
- Create: `tests/test_quality_report.py`
- Modify: `package.json`

- [ ] **Step 1: Write the rule index**

Create `data/quality/rule-index.json`. Every rule is `enforced: test` (naming a check id that must exist in the harness registry) or `enforced: judgment` (naming why no test can exist). The judgment class is capped at 12 by spec §3.3 — it is a cap, not a loophole.

```json
{
  "judgment_cap": 12,
  "rules": [
    { "id": "img-srcset-within-2x", "family": "IMG", "enforced": "test", "test": "tests/render/checks/img.ts::img-srcset-within-2x" },
    { "id": "img-alt-present-and-unique", "family": "IMG", "enforced": "test", "test": "tests/render/checks/img.ts::img-alt-present-and-unique" },
    { "id": "layout-no-horizontal-overflow", "family": "LAYOUT", "enforced": "test", "test": "tests/render/checks/layout.ts::layout-no-horizontal-overflow" },
    { "id": "layout-min-font-size", "family": "LAYOUT", "enforced": "test", "test": "tests/render/checks/layout.ts::layout-min-font-size" },
    { "id": "layout-tap-target-size", "family": "LAYOUT", "enforced": "test", "test": "tests/render/checks/layout.ts::layout-tap-target-size" },
    { "id": "nav-anchors-resolve", "family": "NAV", "enforced": "test", "test": "tests/render/checks/nav.ts::nav-anchors-resolve" },
    { "id": "nav-jump-target-lands", "family": "NAV", "enforced": "test", "test": "tests/render/checks/nav.ts::nav-jump-target-lands" },

    { "id": "first-person-brand-voice", "family": "COPY", "enforced": "judgment", "why": "a regex for we/our passes on third-person text that merely mentions us; the distinction is authorial stance, which has no mechanical decision procedure" },
    { "id": "cites-appendix-i-framing", "family": "COPY", "enforced": "judgment", "why": "a string match on 'Appendix I' is testable and already covered by aeo_audit.py; the rule it belongs to is 'never imply wild-caught trade', which is about implication, not tokens" },
    { "id": "work-on-main-not-branches", "family": "GATE", "enforced": "judgment", "why": "governs the operator's git behaviour before any artifact exists; there is no page state to assert against" },
    { "id": "always-push-after-build", "family": "GATE", "enforced": "judgment", "why": "same — a test could assert a clean tree, but not that the work was finished, and asserting the former would pass on an empty commit" },
    { "id": "recommend-plus-why", "family": "COPY", "enforced": "judgment", "why": "applies to conversational output, which is never written to a file the harness can read" },
    { "id": "restate-the-brief", "family": "COPY", "enforced": "judgment", "why": "same — conversational, pre-artifact" },
    { "id": "preview-before-apply", "family": "GATE", "enforced": "judgment", "why": "asserts that approval happened before a write; the write itself is indistinguishable from an approved one" },
    { "id": "confidence-gate-97", "family": "GATE", "enforced": "judgment", "why": "a self-reported confidence level has no external observable" },
    { "id": "write-from-outline-never-from-sibling", "family": "DUP", "enforced": "judgment", "why": "the OUTCOME is tested by dup_content_audit.py, but the rule is about method — a page written from a sibling and then reworded passes the outcome test and still violates the rule" },
    { "id": "no-fabricated-claims", "family": "COPY", "enforced": "judgment", "why": "requires knowing what is true off-page; a test can only check a claim against a ledger it is given, which is the next rule" },
    { "id": "verified-claim-ledger", "family": "COPY", "enforced": "judgment", "why": "the ledger is prose approved by the breeder; mechanising it would require re-encoding every claim, and a stale encoding is worse than none" },
    { "id": "brand-owned-method-labels", "family": "COPY", "enforced": "judgment", "why": "presence is testable; correct first-use definition and never-implying-third-party-certification is not" }
  ]
}
```

- [ ] **Step 2: Write the failing test**

Create `tests/test_quality_report.py`:

```python
# tests/test_quality_report.py
#
# The report is what makes "no test, no rule" enforceable rather than aspirational:
# it is the thing that prints the deletion-candidate list every run. If it can
# silently report an empty list, the constraint stops existing.
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import quality_report as Q


CHECKS_TS = """
register({
  id: 'img-srcset-within-2x',
  family: 'IMG',
});
register({
  id: "nav-anchors-resolve",
  family: 'NAV',
});
"""


def test_extracts_check_ids_from_typescript_single_and_double_quoted():
    assert Q.check_ids_from_source(CHECKS_TS) == {"img-srcset-within-2x", "nav-anchors-resolve"}


def test_a_source_with_no_register_calls_yields_nothing_not_a_crash():
    assert Q.check_ids_from_source("// nothing here") == set()


def test_a_test_backed_rule_pointing_at_a_missing_check_is_a_broken_link():
    index = {"judgment_cap": 12, "rules": [
        {"id": "ghost", "enforced": "test", "test": "tests/render/checks/img.ts::ghost"},
    ]}
    assert Q.broken_test_links(index, {"img-srcset-within-2x"}) == ["ghost"]


def test_a_test_backed_rule_pointing_at_a_real_check_is_not_broken():
    index = {"judgment_cap": 12, "rules": [
        {"id": "img-srcset-within-2x", "enforced": "test",
         "test": "tests/render/checks/img.ts::img-srcset-within-2x"},
    ]}
    assert Q.broken_test_links(index, {"img-srcset-within-2x"}) == []


def test_a_rule_with_neither_a_test_nor_a_judgment_class_is_a_deletion_candidate():
    index = {"judgment_cap": 12, "rules": [
        {"id": "orphan", "family": "SEM"},
        {"id": "kept", "enforced": "judgment", "why": "because"},
    ]}
    assert Q.deletion_candidates(index) == ["orphan"]


def test_a_judgment_rule_with_no_why_is_a_deletion_candidate():
    """The `why` is the whole cap. A judgment class you can join without stating
    why a test cannot exist is an exemption anyone can grant themselves."""
    index = {"judgment_cap": 12, "rules": [{"id": "lazy", "enforced": "judgment"}]}
    assert Q.deletion_candidates(index) == ["lazy"]


def test_the_judgment_cap_is_reported_when_exceeded():
    index = {"judgment_cap": 2, "rules": [
        {"id": f"j{i}", "enforced": "judgment", "why": "w"} for i in range(3)
    ]}
    assert Q.judgment_overflow(index) == (3, 2)
    ok = {"judgment_cap": 3, "rules": [
        {"id": f"j{i}", "enforced": "judgment", "why": "w"} for i in range(3)
    ]}
    assert Q.judgment_overflow(ok) is None


def test_worst_family_ranks_by_rows_not_instances():
    """Rows are comparable across families; instances are not. Ranking by instances
    would put whichever check happens to enumerate the most nodes on top forever."""
    cards = [
        {"defects": {"NAV": 1, "IMG": 3}, "instances": {"NAV": 400, "IMG": 3}},
        {"defects": {"NAV": 1, "IMG": 3}, "instances": {"NAV": 400, "IMG": 3}},
    ]
    assert Q.worst_family(cards)[0] == "IMG"


def test_open_overrides_are_collected_with_their_page():
    cards = [
        {"slug": "a", "overrides": [{"checkId": "img-srcset-within-2x", "reason": "regen queued"}]},
        {"slug": "b", "overrides": []},
    ]
    assert Q.open_overrides(cards) == [("a", "img-srcset-within-2x", "regen queued")]


def test_latest_card_per_slug_wins(tmp_path):
    """Two dated scorecards for one page must contribute once, most recent."""
    d = tmp_path / "scorecards"
    d.mkdir()
    (d / "x-2026-07-31.json").write_text(json.dumps({"slug": "x", "date": "2026-07-31", "total": 9}))
    (d / "x-2026-08-01.json").write_text(json.dumps({"slug": "x", "date": "2026-08-01", "total": 2}))
    cards = Q.load_scorecards(d)
    assert [c["total"] for c in cards] == [2]


def test_trend_reports_the_delta_between_the_two_most_recent_windows():
    ledger = {"windows": [
        {"from": "2026-05-01", "to": "2026-07-31", "rate": 0.248},
        {"from": "2026-07-02", "to": "2026-08-01", "rate": 0.200},
    ]}
    cur, delta = Q.trend(ledger)
    assert cur["rate"] == 0.200
    assert round(delta, 3) == -0.048


def test_trend_with_one_window_has_no_delta():
    ledger = {"windows": [{"from": "a", "to": "b", "rate": 0.3}]}
    cur, delta = Q.trend(ledger)
    assert cur["rate"] == 0.3
    assert delta is None
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `python3 -m pytest tests/test_quality_report.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'quality_report'`.

- [ ] **Step 4: Write the implementation**

Create `scripts/quality_report.py`:

```python
#!/usr/bin/env python3
"""One screen: is the quality loop closing, and what should be fixed next?

    python3 scripts/quality_report.py

Sections:
  1. Rework rate, current window and delta          (the lagging indicator)
  2. First-run defects per page, by family          (the leading indicator)
  3. Worst family                                   (the next-action list)
  4. Open overrides                                 (suppressed defects, counted)
  5. Rules with no backing test                     (the deletion-candidate list)

Section 5 is the one that makes "no test, no rule" real. Everything else is
reporting; that section is enforcement.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "quality" / "rework-ledger.json"
SCORECARDS = ROOT / "data" / "quality" / "scorecards"
RULE_INDEX = ROOT / "data" / "quality" / "rule-index.json"
CHECKS_DIR = ROOT / "tests" / "render" / "checks"

CHECK_ID_RE = re.compile(r"""\bid:\s*['"]([a-z0-9-]+)['"]""")


def check_ids_from_source(text: str) -> set:
    """Every check id declared in a checks/*.ts source.

    Read from source rather than by running the harness so the report works when
    the harness is red — which is exactly when you most want to know which rules
    have lost their backing test.
    """
    return set(CHECK_ID_RE.findall(text))


def registry_check_ids(checks_dir: pathlib.Path = CHECKS_DIR) -> set:
    ids = set()
    for p in sorted(checks_dir.glob("*.ts")):
        ids |= check_ids_from_source(p.read_text())
    return ids


def broken_test_links(index: dict, check_ids: set) -> list:
    """Rules claiming `enforced: test` whose named check does not exist.

    This is the failure mode that would quietly hollow the whole scheme out: a rule
    keeps its exemption from the deletion list by pointing at a test that was
    renamed or deleted months ago.
    """
    out = []
    for r in index.get("rules", []):
        if r.get("enforced") != "test":
            continue
        named = (r.get("test") or "").split("::")[-1]
        if named not in check_ids:
            out.append(r["id"])
    return out


def deletion_candidates(index: dict) -> list:
    """Rules with neither a test nor a justified judgment class.

    A judgment rule with no `why` counts as a candidate: the `why` IS the cap. A
    class you can join without stating why a test cannot exist is an exemption
    anyone can grant themselves.
    """
    out = []
    for r in index.get("rules", []):
        enforced = r.get("enforced")
        if enforced == "test":
            continue
        if enforced == "judgment" and (r.get("why") or "").strip():
            continue
        out.append(r["id"])
    return out


def judgment_overflow(index: dict):
    """(count, cap) when the judgment class is over its cap, else None."""
    cap = index.get("judgment_cap", 12)
    n = sum(1 for r in index.get("rules", []) if r.get("enforced") == "judgment")
    return (n, cap) if n > cap else None


def load_scorecards(d: pathlib.Path = SCORECARDS) -> list:
    """Most recent card per slug, newest first."""
    latest = {}
    for p in sorted(d.glob("*.json")):
        c = json.loads(p.read_text())
        prev = latest.get(c["slug"])
        if prev is None or c.get("date", "") >= prev.get("date", ""):
            latest[c["slug"]] = c
    return sorted(latest.values(), key=lambda c: (c.get("date", ""), c["slug"]), reverse=True)


def worst_family(cards: list):
    """(family, rows) with the most defect ROWS.

    Rows, never instances. Ranking by instances would permanently elect whichever
    check enumerates the most nodes, which is a fact about the check, not the site.
    """
    tally = {}
    for c in cards:
        for fam, n in (c.get("defects") or {}).items():
            tally[fam] = tally.get(fam, 0) + n
    if not tally:
        return (None, 0)
    return max(tally.items(), key=lambda kv: kv[1])


def open_overrides(cards: list) -> list:
    out = []
    for c in cards:
        for o in c.get("overrides") or []:
            out.append((c["slug"], o["checkId"], o["reason"]))
    return out


def trend(ledger: dict):
    """(most recent window, delta vs the one before it or None)."""
    w = sorted(ledger.get("windows", []), key=lambda x: x["from"])
    if not w:
        return (None, None)
    if len(w) == 1:
        return (w[-1], None)
    return (w[-1], w[-1]["rate"] - w[-2]["rate"])


def _read(path: pathlib.Path, default):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=10, help="how many pages to list")
    args = ap.parse_args(argv)

    ledger = _read(LEDGER, {"windows": []})
    index = _read(RULE_INDEX, {"rules": []})
    cards = load_scorecards()
    ids = registry_check_ids()

    print("=" * 78)
    print("CAG QUALITY REPORT")
    print("=" * 78)

    cur, delta = trend(ledger)
    print("\n1. REWORK RATE  (lagging — spec target: under 15% at 90 days)")
    if cur is None:
        print("   no windows recorded — run scripts/rework_ledger.py --last-30-days")
    else:
        arrow = "" if delta is None else f"  ({delta:+.1%} vs previous window)"
        print(f"   {cur['from']} .. {cur['to']}   {cur['rework']}/{cur['total']} = {cur['rate']:.1%}{arrow}")

    print(f"\n2. FIRST-RUN DEFECTS  (leading — most recent {args.limit} pages)")
    if not cards:
        print("   no scorecards — run npm run test:render:pages && node scripts/build_scorecard.mjs")
    else:
        print(f"   {'page':<46}{'rows':>6}{'inst':>7}  by family")
        for c in cards[: args.limit]:
            fams = " ".join(f"{k}:{v}" for k, v in sorted((c.get('defects') or {}).items()))
            print(f"   {c['slug'][:45]:<46}{c.get('total', 0):>6}{c.get('total_instances', 0):>7}  {fams}")

    fam, n = worst_family(cards)
    print("\n3. NEXT ACTION")
    print(f"   worst family: {fam or 'n/a'} ({n} rows) — fix the check first if it looks impossible")

    ovr = open_overrides(cards)
    print(f"\n4. OPEN OVERRIDES  ({len(ovr)})")
    for slug, cid, reason in ovr:
        print(f"   {slug}: {cid} — {reason}")
    if not ovr:
        print("   none")

    print("\n5. RULES WITH NO BACKING TEST  (deletion candidates)")
    broken = broken_test_links(index, ids)
    orphans = deletion_candidates(index)
    over = judgment_overflow(index)
    if broken:
        print(f"   BROKEN test link (rule claims a check that does not exist): {', '.join(broken)}")
    if orphans:
        print(f"   no test and no justified judgment class: {', '.join(orphans)}")
    if over:
        print(f"   judgment class is {over[0]}, cap is {over[1]} — it is a cap, not a loophole")
    if not (broken or orphans or over):
        n_j = sum(1 for r in index.get('rules', []) if r.get('enforced') == 'judgment')
        print(f"   none. {len(ids)} checks registered, {n_j} judgment rules within cap.")

    print()
    # Exit non-zero on a broken test link only. An orphan rule is a decision for a
    # human; a rule pointing at a check that no longer exists is a fact, and a fact
    # that silently passes is how the twelve lying gates happened.
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_quality_report.py -q`
Expected: `12 passed`.

- [ ] **Step 6: Run the report against the real repo**

Run: `python3 scripts/quality_report.py`
Expected: five sections. Section 4 names `img-srcset-within-2x` with the reason from Task 5. Section 5 prints `none. 7 checks registered, 12 judgment rules within cap.`

**If section 5 prints a BROKEN test link, fix the id in `rule-index.json` before committing** — that is the report catching its own input, which is the point.

- [ ] **Step 7: Add the npm script**

In `package.json`, add to `"scripts"` after `"test:render:pages"`:

```json
    "test:render:report": "python3 scripts/quality_report.py"
```

(Remember the comma on the preceding line.)

- [ ] **Step 8: Commit**

```bash
git add scripts/quality_report.py tests/test_quality_report.py data/quality/rule-index.json package.json
git commit -m "$(cat <<'EOF'
feat(quality): quality_report.py — including the deletion-candidate list

Four sections report; the fifth enforces. A rule is `enforced: test` naming a
check that must exist in the harness, or `enforced: judgment` naming why no
test can exist — and a judgment rule with no `why` counts as a deletion
candidate, because the `why` is the entire cap.

Exits non-zero only on a BROKEN test link: a rule keeping its exemption by
pointing at a check renamed or deleted months ago. An orphan rule is a
decision for a human; a dangling reference is a fact, and a fact that silently
passes is how twelve lying gates happened.

Ranks families by rows, never instances — instances would permanently elect
whichever check enumerates the most nodes, which is a fact about the check.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 8: `cag-learning-loop` — the skill that charges defects to the harness

**Files:**
- Create: `skills/cag-learning-loop.md`
- Modify: `.claude/skills/cag-learning-loop/SKILL.md` (generated by the registration script — never hand-edited)

- [ ] **Step 1: Write the skill**

Create `skills/cag-learning-loop.md`:

```markdown
---
name: cag-learning-loop
description: Use at the end of every CAG build, and whenever a defect escapes to the breeder, to decide what the escape means — a harness bug, or a genuinely new invariant. Enforces the promotion path (defect → failing test → fix → rule) and its inverse (a rule with no test is a deletion candidate). Triggers "what did we learn", "close the loop", "add a rule for this", "this shipped broken", session-closer.
---

# CAG Learning Loop

**The one thing this skill exists to prevent:** answering an escaped defect by writing
another paragraph. The system already has thirty-plus rules and a 24.8% rework rate.
Rule thirty-one does not move that number. A test does.

## The two constraints

1. **No test, no rule.** A lesson becomes a rule only after a failing test exists.
   A rule with no test is a deletion candidate — `scripts/quality_report.py` §5 lists them.
2. **When a defect escapes, charge it to the harness, not to a new paragraph.**
   If an invariant already covered it, the tool is broken. Fix the tool.

Constraint 2 is the load-bearing one. On 2026-07-31 it produced ten findings, **ten of
them in the harness and zero in the pages** — a tool built to stop gates lying contained
ten ways to lie, and three were findable only by measuring a real page.

## Procedure

Run this at the end of a build, or the moment the breeder reports something shipped wrong.

### Step 1 — Diff what was reworked

```bash
git log --since=<session start> --pretty=format:"%h %s" | grep -iE "^[a-f0-9]+ (fix|revert)|fix\(|correct|restore|undo|repair"
```

Every hit is an escape: something reached a commit and had to be undone. Also include
anything the breeder reported by hand, whether or not it produced a commit.

### Step 2 — Classify each escape into a family

`IMG` · `LAYOUT` · `NAV` · `CSS` · `SEM` · `SCHEMA` · `DUP` — the same seven the harness
and the ledger use, plus `GATE` / `A11Y` / `COPY` for what the harness does not measure.
Same vocabulary everywhere, or the ledger and the scorecard stop describing the same site.

### Step 3 — Ask FIRST whether an invariant already covered it  ← the load-bearing step

Check `tests/render/checks/*.ts` for a check in that family that should have caught it.

**If one exists and did not fire, the harness has a bug.** Then:

1. Add the missed case to `tests/render/fixtures/known_broken/<check-id>.html`.
2. Run `npm run test:render:meta` and **watch it fail**. A fixture that does not fail is
   not a reproduction — you have added decoration.
3. Fix the check.
4. Re-run; confirm the fixture fires and `known_good` stays silent.
5. **Write no new rule.** The rule already existed; the tool was wrong.

Before editing any page in response to a checker, read `skills/cag-gate-integrity.md`.
Twelve checkers on this site have reported defects that did not exist, and two reported
PASS having examined zero pages.

### Step 4 — Only if no invariant covers it, write one

In this order, and never out of it:

1. Write the failing case first — `known_broken/<new-check-id>.html`.
2. Run the meta gate; **confirm it fails**.
3. Implement the check in the right `checks/*.ts`, registered `severity: 'advisory'`.
4. Confirm it fires on `known_broken` and is silent on `known_good`.
5. Add the rule text **next to the test**, and add the row to `data/quality/rule-index.json`
   as `enforced: test` with the check id.

A new check enters as **advisory**. It earns `blocking` after one full cluster with zero
false reports. On the first baseline, three of the four checks with findings would have
blocked falsely — 224 inline prose links flagged by tap-target size (WCAG 2.2 exempts
inline links), 27 `sr-only` skip links, and `12.48px` against a `12.5` threshold.

**A check that fires falsely once gets demoted, not whitelisted.** A gate that cries wolf
once is ignored forever, which is how this repo accumulated twelve of them.

### Step 5 — Append to the ledger

```bash
python3 scripts/rework_ledger.py --last-30-days
python3 scripts/quality_report.py
```

Read section 3 (worst family) and section 5 (deletion candidates). If a family tops the
list two reports running and its checks all pass, the checks are wrong before the pages are.

## What does NOT go through this loop

Rules classed `enforced: judgment` in `data/quality/rule-index.json` — voice, CITES
framing, work-on-main, Recommend+Why, the verified-claim ledger, and the rest of the
capped twelve. Each states in the index why a test cannot exist. Adding a thirteenth
requires raising the cap deliberately, in the spec, with a reason.

## Related

- `docs/superpowers/specs/2026-07-31-self-improving-quality-loop-design.md` — the design
- `skills/cag-gate-integrity.md` — read at the FIRST report from any checker
- `skills/cag-final-page-pass.md` — the per-page gate this sits underneath
- `scripts/quality_report.py` · `scripts/rework_ledger.py`
```

- [ ] **Step 2: Register it**

Run:
```bash
python3 scripts/register_skills.py --copy
python3 scripts/register_skills.py --check
```
Expected: the second command exits 0 with every skill registered and in sync.

Registration loads at session start, so `/cag-learning-loop` is invisible until the next session. That is expected — do not chase it.

- [ ] **Step 3: Verify the mirror exists**

Run: `ls -la .claude/skills/cag-learning-loop/SKILL.md && head -4 .claude/skills/cag-learning-loop/SKILL.md`
Expected: the file exists and its front matter carries `name: cag-learning-loop`.

- [ ] **Step 4: Commit**

```bash
git add skills/cag-learning-loop.md .claude/skills/cag-learning-loop
git commit -m "$(cat <<'EOF'
feat(skills): cag-learning-loop — charge escaped defects to the harness

Layer 3 of the quality loop. Step 3 is the load-bearing one: before writing
any new rule, check whether an invariant already covered the escape. If one
did and stayed quiet, the tool is broken — add the missed case to the
known_broken fixture, watch the meta gate fail, fix the check, and write no
new rule. That step is what produced ten findings on 2026-07-31, ten of them
in the harness and zero in the pages.

Registered with register_skills.py --copy; --check passes.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 9: Wire it into the project's own rules, then deploy

**Files:**
- Modify: `CLAUDE.md`
- Modify: `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/MEMORY.md`
- Create: `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/project_render_harness_phase2.md`

- [ ] **Step 1: Add the rule to CLAUDE.md**

Insert into `CLAUDE.md`'s `## Non-Negotiable Rules`, directly after the **Verify the gate before you fix the page** bullet:

```markdown
- **No test, no rule — and an escaped defect is charged to the harness (ALWAYS) — applies to every agent, skill, and lesson** — A lesson becomes a rule **only** after a failing test exists: defect observed → failing test committed → fix applied → test passes → rule text written next to the test. **A rule with no backing test is a deletion candidate** — `python3 scripts/quality_report.py` §5 lists them every run, and exits non-zero when a rule points at a check that no longer exists. The inverse matters more: **when a defect escapes, charge it to the harness, not to a new paragraph.** If an invariant already covered it and stayed quiet, the tool is broken — add the missed case to `tests/render/fixtures/known_broken/`, watch `npm run test:render:meta` fail, fix the check, and write no new rule. This repo has thirty-plus rules and a 24.8% rework rate; rule thirty-one does not move that number. Exempt: the capped twelve `enforced: judgment` rules in `data/quality/rule-index.json`, each of which states why a test cannot exist. Procedure: `skills/cag-learning-loop.md`. Enforced by `scripts/quality_report.py` (tested in `tests/test_quality_report.py`).
```

- [ ] **Step 2: Add the three scripts to the CLAUDE.md Scripts section**

Insert into `## Scripts`, after the `scripts/dup_content_audit.py` bullet:

```markdown
- `npm run test:render:meta` — **the gate-integrity gate: checks the checkers** (~30 s). Every registered check must fire on its `known_broken` fixture, stay silent on `known_good`, reach its declared `minExamined` floor, and obey the defect-row contract in `tests/render/lib/runCheck.ts`. Run it BEFORE trusting any page result — a page measured by a failing gate is not evidence.
- `npm run test:render:pages` — measures 9 for-sale pages at 375/768/1280 in a real browser (~7 min), then `node scripts/build_scorecard.mjs --run first` writes dated scorecards to `data/quality/scorecards/`. Refuses to run against a stale `dist/`. Blocked builds proceed with `RENDER_OVERRIDE="check-id:reason"`, which is written into the scorecard and printed by the quality report — counted, never hidden.
- `scripts/quality_report.py` (`npm run test:render:report`) — one screen: rework rate + delta, first-run defects per page by family, the worst family (the next-action list), open overrides, and **rules with no backing test**. Fed by `scripts/rework_ledger.py --last-30-days`, which computes the canonical rework rate from git and upserts `data/quality/rework-ledger.json`.
```

- [ ] **Step 3: Run the full local gate**

Run:
```bash
npm run test:render:meta && python3 -m pytest tests/ -q && python3 scripts/quality_report.py && python3 scripts/register_skills.py --check
```
Expected: meta green, all pytest green (existing 90 cases plus the ~21 added here), the report prints five sections with no BROKEN link, registration in sync.

- [ ] **Step 4: Write the memory record**

Create `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/project_render_harness_phase2.md`:

```markdown
---
name: project-render-harness-phase2
description: "Phase 2 is live — ledger, quality_report.py, cag-learning-loop, and the three Phase-1 repairs; plus what the NAV re-measurement actually showed"
metadata:
  node_type: memory
  type: project
---

Built 2026-08-01, on `main`, pushed. Plan: `docs/superpowers/plans/2026-08-01-render-harness-phase2.md`.
Parent: [[project_render_harness_phase1]]. Spec §3.2/§3.3.

**Commands:** `npm run test:render:meta` · `npm run test:render:pages` · `npm run test:render:report`
(= `scripts/quality_report.py`) · `scripts/rework_ledger.py --last-30-days`.

**The three repairs.**
1. **Freshness** — `tests/render/lib/freshness.ts`, wired as a `beforeAll` in pages.spec only.
   A throwing beforeAll writes no partials, so `build_scorecard.mjs` Guard 1 fails too: loud at
   both ends. Skips `src/pages/node_modules/.vite/`, which really exists and would refuse every run.
2. **NAV** — the check was racing its own reset: `scrollTo(0,0)` is smooth-animated under the
   global rule and it clicked 80 ms in. `behavior:'instant'` overrides computed style;
   `'auto'` does NOT (it MEANS "use computed style"). Settle is polled with `setTimeout`,
   never rAF — rAF stalls on a non-painting page. **RECORD THE RE-MEASUREMENT RESULT HERE.**
3. **Units** — `Defect.count` required; `MAX_DEFECT_ROWS = 3` enforced in `lib/runCheck.ts`,
   the single call site both specs use, so the contract binds on a 62-anchor page and not
   only on a 2-anchor fixture. Scorecards carry rows AND instances; rank by **rows**.

**One counted override in effect:** `img-srcset-within-2x` on 9/9 pages — 33 files over 2×,
worst 13.33× (a 640px avatar in a 48px slot). It fired on something real, so it kept
`blocking`; the regen is logged in `docs/reference/technical-seo-fixes-backlog.md` and the
override prints in the quality report every run.

**Layer 3 is `skills/cag-learning-loop.md`** — and the CLAUDE.md rule "No test, no rule" now
has a test behind it (`tests/test_quality_report.py`), which is the only way it is allowed
to exist. The judgment class is capped at 12 in `data/quality/rule-index.json`; a judgment
rule with no `why` counts as a deletion candidate.

Related: [[feedback_verify_the_gate_before_fixing]], [[reference_smooth_scroll_kills_jump_links]],
[[project_self_improving_quality_loop]], [[reference_gate_examined_zero_pages]].
```

Fill in the NAV re-measurement number from Task 5 Step 5 before saving.

- [ ] **Step 5: Add the index line**

In `MEMORY.md`, under `## Working preferences`, directly beneath the `Render Harness Phase 1` line, add:

```markdown
- [Render Harness Phase 2](project_render_harness_phase2.md) — ledger + quality_report + cag-learning-loop; the three repairs (freshness, NAV racing its own reset, defect-row units); one counted override
```

- [ ] **Step 6: Commit and push**

```bash
git add CLAUDE.md
git commit -m "$(cat <<'EOF'
docs(rules): No test, no rule — with a test behind it

Adds the one rule this session earned: a lesson becomes a rule only after a
failing test exists, a rule with no test is a deletion candidate, and an
escaped defect is charged to the harness before it is charged to a new
paragraph. Backed by scripts/quality_report.py §5, which is itself tested —
the rule obeys its own constraint or it would not be allowed in.

Registers the three commands in the Scripts section.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
git push origin main
```

- [ ] **Step 7: Confirm the deploy is clean**

Run: `git status --short && git log --oneline -9 && bash scripts/health-sweep.sh --no-build 2>&1 | tail -20`
Expected: clean tree, nine new commits, health sweep passes.

---

## Self-Review

Checked against spec §3.2, §3.3 and the session's stated Phase-2 list.

**Spec coverage**

| Spec requirement | Task |
|---|---|
| §3.2 per-build scorecard | already Phase 1; extended with `instances` in Task 4 |
| §3.2 `data/quality/rework-ledger.json` | Task 6 |
| §3.2 `scripts/quality_report.py`, all five sections | Task 7 |
| §3.2 benchmark corpus (`corpus: true`) | already in `targets.json`; not re-touched |
| §3.3 promotion path | Task 8 (skill) + Task 9 (rule) |
| §3.3 "rule with no test is a deletion candidate" | Task 7 §5 + Task 9 |
| §3.3 judgment class enumerated and capped at 12 | Task 7 Step 1 |
| §3.1.3 overrides counted, never hidden | Task 5 (first real use) + Task 7 §4 |
| Repair: normalize defect-counting units | Task 4 |
| Repair: NAV one root cause per page | Tasks 2–3 |
| Repair: assert `dist/` freshness | Task 1 |

**Deliberately not covered:** Phase 3 families (`CSS`/`SEM`/`SCHEMA`/`DUP`), Phase 4 `rules/`
packs and the CLAUDE.md reduction, and the 33-file image regen — the last is logged to the
backlog with a counted override, per the decision recorded at the top of this plan.

**Type consistency:** `Defect` gains `count: number` in Task 4 and every emitter is updated in
the same task; Task 3 writes `count` into `nav.ts` one task early and Task 3 Step 3's closing
instruction adds it to `nav-anchors-resolve` too, so the tree compiles after each commit.
`checkDistFreshness(root?)`, `runCheck(check, page, viewport)`, `resetScrollInstant(page)`,
`waitForScrollSettle(page, opts?)`, `window(frm, to, subjects)`, `append_window(path, w)`,
`check_ids_from_source(text)`, `broken_test_links(index, ids)`, `deletion_candidates(index)`,
`judgment_overflow(index)`, `worst_family(cards)`, `open_overrides(cards)`, `trend(ledger)`,
`load_scorecards(dir)` — each is defined once and called with the signature it was defined with.

**Ordering:** the tree is green after every commit. The row cap lands in Task 4, after Task 3
makes NAV comply, so no intermediate commit leaves the page suite throwing.

**Stop conditions, stated in the tasks themselves:** Task 1 Step 6, Task 2 Step 2, Task 5
Step 1 and Step 4. Each says what to do instead of proceeding — because a plan that only
describes the happy path is how a run gets adjusted until the number looks right.

---

## Amendments During Execution

Recorded as they happen, so a later reader is not misled by a task body that no longer
matches what shipped. The commits are authoritative; this is the index.

### Task 1 — the cascade comment was wrong as written (commit `9932989`)

Task 1 Step 5's comment claims: *gate throws → no partial written → `build_scorecard.mjs`
Guard 1 also fails.* **The third clause was false.** Nothing cleared `data/quality/raw/`,
and `writeManifest` runs at module load — before `beforeAll`. A refused run therefore
rewrote the manifest to 27, left the previous run's 27 partials on disk, and Guard 1
compared 27 to 27 and passed. Reproduced: nine green, today-dated scorecards from a run
that never executed. This is the repo's signature defect (a gate passing having examined
nothing) asserted as safe in a comment, which is worse than not claiming it.

Fixed by `resetRaw(dir = RAW_DIR)` in `tests/render/lib/scorecard.ts`, called in
`pages.spec.ts` immediately before `writeManifest`, pinned by a test. The cascade is now
true: a refused run leaves zero partials and `build_scorecard.mjs` exits 1 with
`expected 27 partials, found 0`.

Also in that commit: an explicit `error` flag through `newest()` so a real filesystem
error refuses instead of reading as "nothing newer" (the literal `ms === 0` fix would
have broken the legitimate vendored-tree case, where `ms === 0` with no error); reason-string
assertions on the missing-dist and empty-dist tests; a test for `newest()`'s file branch;
sub-minute deltas formatted in seconds; temp-dir teardown.

**Deliberately not fixed:** deletion-blindness. `walk()` reads file mtimes only, so removing
a source page leaves `dist/` serving a stale copy while the gate reports fresh. Folding
directory mtimes in would close it but trades a rare false PASS for a rare false FAIL, and
on this codebase false FAIL is the more expensive error — a gate that cries wolf once gets
ignored forever. Recorded as a documented limitation in `freshness.ts` instead of a test.

### Task 1 — the fix for the fix: `resetRaw` cannot live at spec-module scope (commit `9e1e58a`)

Placing `resetRaw()` at module scope in `pages.spec.ts` was wrong, and worse than the bug it
closed. **Playwright loads a spec file once during collection and again in every worker
process**, so the reset ran repeatedly, mid-run, deleting partials earlier workers had
already written. Measured on the real harness: one page across the three viewport projects
wrote 3 partials and kept **1** (the last worker's load wiped the other two). Scaled to the
full suite that is 27 written, 9 kept — and `build_scorecard.mjs` would then print
`expected 27 partials, found 9`, whose documented meaning is "a page test crashed." Nothing
crashed. The gate would have issued a **false diagnosis**, which is the cry-wolf failure this
harness exists to prevent, shipping inside the fix for it.

`writeManifest` had always been at module scope and was fine, because rewriting identical
content is idempotent. **Deletion is not.** That asymmetry is the transferable lesson.

Fixed by `tests/render/global-setup.ts`, registered as Playwright `globalSetup` — the only
hook that runs exactly once, in the main process, before any worker spawns. It performs
`resetRaw()` then `writeManifest()`, deriving the expected partial count from
`config.projects.length` rather than a hardcoded 3, so adding a viewport project cannot
silently break Guard 1. Pinned by a nested-Playwright regression probe over a disposable
3-project suite, verified red (`Expected: 3, Received: 1`) against the old placement.

**`checkDistFreshness` deliberately stayed in `pages.spec.ts`.** Moving it to `globalSetup`
was tried and rejected on evidence: `globalSetup` fires for *every* invocation of the config,
including `npm run test:render:meta`, so the freshness throw would have dist-gated the meta
suite and broken the approved invariant that the gate-integrity gate stays runnable while a
build is broken. Freshness is a pure read, so per-worker execution is redundant, not harmful.

**Accepted consequence:** because `globalSetup` fires for meta runs, `npm run test:render:meta`
clears `data/quality/raw/`. Chosen over invocation-sniffing, because the documented order is
meta-then-pages and the failure is loud (`expected N, found 0`) rather than quiet — and a
guard built on argv inspection would be exactly the kind of quiet correctness mechanism that
had just failed twice.

**A near-miss worth recording:** the regression probe itself initially passed for the wrong
reason. Rooted under the OS tmpdir it could not resolve `@playwright/test`, so both variants
silently no-op'd — and `0 survivors` satisfies `< 3` exactly as `1` does, so the "broken"
assertion went green while testing nothing. Re-rooted under `tests/render/.probe-*/`
(gitignored). A test for a gate that passes for the wrong reason is the same defect one level
up, and it nearly shipped.



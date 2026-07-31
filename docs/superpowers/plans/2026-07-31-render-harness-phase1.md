# Render Harness (Phase 1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Playwright acceptance harness that measures CAG pages as they actually paint at 375/768/1280, where every check must prove it fires on a broken fixture and stays silent on a good one before it is allowed to block a build.

**Architecture:** A check registry (`lib/registry.ts`) holds self-describing check objects. `meta.spec.ts` is the gate-integrity gate: it iterates the registry and asserts each check fires on `fixtures/known_broken/<id>.html` and is silent on `fixtures/known_good/<id>.html`, and that it examined more than zero nodes. `pages.spec.ts` runs the registry over real built pages listed in `targets.json`, writing one partial JSON result per (page, viewport); `scripts/build_scorecard.mjs` merges partials into a per-page scorecard. Checks ship as `advisory` and are promoted to `blocking` only after a clean baseline run.

**Tech Stack:** `@playwright/test` 1.60.0 (matches installed `playwright-core@1.60.0`; Chromium 1223 already cached — no browser download), TypeScript via Playwright's built-in transform, Node 24, `python3 -m http.server` as the static server. No other new dependencies.

**Spec:** `docs/superpowers/specs/2026-07-31-self-improving-quality-loop-design.md` §3.1 (Phase 1 only).

---

## Scope

**In scope (spec Phase 1):** harness bootstrap, registry, gate-integrity meta gate, the `IMG` / `LAYOUT` / `NAV` families, targets manifest, page runner, scorecard merge, baseline run over the 9 for-sale cluster pages.

**Out of scope (later plans):** `CSS` / `SEM` / `SCHEMA` / `DUP` families (Phase 3), the rework ledger and `quality_report.py` (Phase 2), `skills/cag-learning-loop.md` (Phase 2), `CLAUDE.md` reduction and `rules/` packs (Phase 4).

**Deliberately deferred inside Phase 1, with reason:** tap-target *spacing*. The spec lists it under `LAYOUT`, but commit `fix(gate): tap-target-spacing was reporting 7 false ERRORs` is a recorded false-report incident for exactly this check. Phase 1 implements tap-target **size** only. Spacing returns in Phase 3 with fixtures that encode the seven false cases.

**One refinement to spec §3.1.2, adopted here.** The spec says a run with `examined == 0` is a FAIL. Applied per-page that would fail any page that legitimately has no jump links. The correct semantics, implemented in this plan: `examined == 0` is a hard FAIL **on a fixture** (Task 3), and at suite level a check that examined zero nodes across *every* target page is a FAIL (Task 11) — which is precisely the `seam_parity` "PASS in 0 pages" bug class — while `examined == 0` on a single page means *not applicable*.

---

## File Structure

| Path | Responsibility |
|---|---|
| `tests/render/playwright.config.ts` | Three viewport projects, static server, reporters |
| `tests/render/lib/registry.ts` | Check contract types + the registry array. No logic. |
| `tests/render/lib/probes.ts` | Shared measurement helpers: `settlePage`, `measureTopChrome` |
| `tests/render/lib/scorecard.ts` | Writes one partial result file per (page, viewport) |
| `tests/render/checks/layout.ts` | `LAYOUT` family checks |
| `tests/render/checks/img.ts` | `IMG` family checks |
| `tests/render/checks/nav.ts` | `NAV` family checks |
| `tests/render/checks/index.ts` | Imports every check module so registration happens |
| `tests/render/fixtures/known_good/<id>.html` | Minimal clean page per check |
| `tests/render/fixtures/known_broken/<id>.html` | Minimal page containing exactly that defect |
| `tests/render/meta.spec.ts` | The gate-integrity gate over the whole registry |
| `tests/render/pages.spec.ts` | Runs the registry over real pages from `targets.json` |
| `tests/render/targets.json` | Which slugs, which page type, which families apply |
| `scripts/build_scorecard.mjs` | Merges partials into `data/quality/scorecards/` |

Checks live in `checks/*.ts` (not `*.spec.ts`) so Playwright does not collect them as test files; only `meta.spec.ts` and `pages.spec.ts` are tests.

---

## Task 1: Bootstrap the harness

**Files:**
- Modify: `package.json`
- Create: `tests/render/playwright.config.ts`
- Create: `tests/render/smoke.spec.ts` (deleted in Step 6)
- Create: `.gitignore` entries

- [ ] **Step 1: Install the test runner**

Chromium 1223 is already in `~/Library/Caches/ms-playwright/`, and `playwright-core@1.60.0` is already a dependency. Pin the runner to the same version so no browser download is triggered.

```bash
cd /Users/apple/Downloads/CAG
npm install -D @playwright/test@1.60.0
```

Expected: installs without downloading a browser. Verify:

```bash
node -e "import('@playwright/test').then(()=>console.log('OK')).catch(e=>console.log('MISSING',e.code))"
```
Expected output: `OK`

- [ ] **Step 2: Write the config**

Create `tests/render/playwright.config.ts`:

```ts
import { defineConfig } from '@playwright/test';

const PORT = 4321;

export default defineConfig({
  testDir: '.',
  testMatch: ['meta.spec.ts', 'pages.spec.ts', 'smoke.spec.ts'],
  fullyParallel: false,
  workers: 2,
  timeout: 120_000,
  reporter: [['list']],
  use: {
    baseURL: `http://127.0.0.1:${PORT}`,
    deviceScaleFactor: 1,
  },
  projects: [
    { name: 'vp375', use: { viewport: { width: 375, height: 812 } } },
    { name: 'vp768', use: { viewport: { width: 768, height: 1024 } } },
    { name: 'vp1280', use: { viewport: { width: 1280, height: 800 } } },
  ],
  webServer: {
    command: `python3 -m http.server ${PORT} --bind 127.0.0.1`,
    cwd: '../../',
    port: PORT,
    reuseExistingServer: true,
    timeout: 60_000,
  },
});
```

`cwd: '../../'` resolves relative to this config file, so the server serves the repo root. That makes both `/dist/<slug>/` and `/tests/render/fixtures/...` reachable from one server.

`fullyParallel: false` with `workers: 2` is deliberate: the NAV click-and-measure check drives real scrolling, and parallel workers on one page object produce flaky landings.

- [ ] **Step 3: Add npm scripts**

In `package.json`, replace the `"scripts"` block with:

```json
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build && npx pagefind --site dist",
    "preview": "astro preview",
    "test:render": "playwright test -c tests/render/playwright.config.ts",
    "test:render:meta": "playwright test -c tests/render/playwright.config.ts meta.spec.ts",
    "test:render:pages": "playwright test -c tests/render/playwright.config.ts pages.spec.ts"
  },
```

- [ ] **Step 4: Write a smoke test that proves the server serves `dist/`**

Create `tests/render/smoke.spec.ts`:

```ts
import { test, expect } from '@playwright/test';

test('static server serves a built page', async ({ page }) => {
  const res = await page.goto('/dist/congo-african-grey-parrot-pair-for-sale/');
  expect(res?.status()).toBe(200);
  await expect(page.locator('h1').first()).toBeVisible();
});
```

- [ ] **Step 5: Run the smoke test**

```bash
npm run test:render -- smoke.spec.ts
```
Expected: `3 passed` (one per viewport project).

If it fails with `ECONNREFUSED`, another process holds port 4321 — `lsof -ti:4321 | xargs kill` and rerun.

- [ ] **Step 6: Delete the smoke test and ignore harness output**

```bash
rm tests/render/smoke.spec.ts
```

Append to `.gitignore`:

```
# render harness
test-results/
playwright-report/
data/quality/raw/
```

Remove `smoke.spec.ts` from `testMatch` in `tests/render/playwright.config.ts` so the array reads:

```ts
  testMatch: ['meta.spec.ts', 'pages.spec.ts'],
```

- [ ] **Step 7: Commit**

```bash
git add package.json package-lock.json tests/render/playwright.config.ts .gitignore
git commit -m "test(render): bootstrap the Playwright acceptance harness at 375/768/1280"
```

---

## Task 2: The check contract and shared probes

**Files:**
- Create: `tests/render/lib/registry.ts`
- Create: `tests/render/lib/probes.ts`

- [ ] **Step 1: Write the registry contract**

Create `tests/render/lib/registry.ts`:

```ts
import type { Page } from '@playwright/test';

export type Family = 'IMG' | 'LAYOUT' | 'NAV' | 'CSS' | 'SEM' | 'SCHEMA' | 'DUP';
export type Severity = 'blocking' | 'advisory';

export interface Defect {
  checkId: string;
  family: Family;
  viewport: number;
  message: string;
}

export interface CheckResult {
  /** How many nodes/items this check actually inspected. Zero on a fixture is a FAIL. */
  examined: number;
  defects: Defect[];
}

export interface Check {
  id: string;
  family: Family;
  severity: Severity;
  /** One-line statement of what a defect means, printed in reports. */
  describe: string;
  run(page: Page, viewport: number): Promise<CheckResult>;
}

export const registry: Check[] = [];

export function register(check: Check): void {
  if (registry.some((c) => c.id === check.id)) {
    throw new Error(`duplicate check id: ${check.id}`);
  }
  registry.push(check);
}
```

- [ ] **Step 2: Write the shared probes**

Create `tests/render/lib/probes.ts`:

```ts
import type { Page } from '@playwright/test';

/**
 * Scroll the full page in viewport-sized steps so lazy-loaded images fetch,
 * wait for every image to settle, then return to the top.
 * Required before any IMG check — below-fold images are otherwise unloaded.
 */
export async function settlePage(page: Page): Promise<void> {
  await page.evaluate(async () => {
    const step = window.innerHeight;
    const total = document.body.scrollHeight;
    for (let y = 0; y < total; y += step) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 30));
    }
    window.scrollTo(0, 0);
  });
  await page.evaluate(
    () =>
      Promise.all(
        Array.from(document.images)
          .filter((i) => !i.complete)
          .map(
            (i) =>
              new Promise((res) => {
                i.onload = i.onerror = () => res(null);
              }),
          ),
      ),
  );
  await page.waitForTimeout(200);
}

/**
 * Height in px of sticky/fixed chrome pinned to the top of the viewport
 * (header + any jump rail). Measured, never assumed — the congo-pair page
 * had five `var(--hdr, 72px)` fallbacks against a header that measures 96px.
 */
export async function measureTopChrome(page: Page): Promise<number> {
  return page.evaluate(() => {
    let bottom = 0;
    for (const el of Array.from(document.body.querySelectorAll<HTMLElement>('*'))) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const box = el.getBoundingClientRect();
      if (box.height === 0 || box.width === 0) continue;
      // pinned at the top, and not a full-screen overlay
      if (box.top <= 2 && box.bottom > bottom && box.bottom < window.innerHeight / 2) {
        bottom = box.bottom;
      }
    }
    return Math.round(bottom);
  });
}
```

- [ ] **Step 3: Verify both files typecheck**

```bash
npx tsc --noEmit --module esnext --target es2022 --moduleResolution bundler --lib es2022,dom tests/render/lib/registry.ts tests/render/lib/probes.ts
```
Expected: no output (success).

- [ ] **Step 4: Commit**

```bash
git add tests/render/lib/registry.ts tests/render/lib/probes.ts
git commit -m "test(render): check contract + settlePage/measureTopChrome probes"
```

---

## Task 3: The gate-integrity gate (fails first, by design)

This is the mechanical replacement for `skills/cag-gate-integrity.md`'s request to be careful. It runs before any page test, and it fails right now because the registry is empty — which is the same zero-examined rule the harness enforces on everything else, applied to itself.

**Files:**
- Create: `tests/render/checks/index.ts`
- Create: `tests/render/meta.spec.ts`

- [ ] **Step 1: Write the empty check barrel**

Create `tests/render/checks/index.ts`:

```ts
// Importing a check module runs its register() call. Add every check file here.
export {};
```

- [ ] **Step 2: Write the failing meta gate**

Create `tests/render/meta.spec.ts`:

```ts
import { test, expect } from '@playwright/test';
import { registry } from './lib/registry.js';
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
      const res = await page.goto(`/tests/render/fixtures/known_broken/${check.id}.html`);
      expect(res?.status(), 'known_broken fixture must exist').toBe(200);
      const result = await check.run(page, VIEWPORT);
      expect(result.examined, 'examined must be > 0').toBeGreaterThan(0);
      expect(
        result.defects.length,
        `${check.id} did not fire on a page built to contain its defect`,
      ).toBeGreaterThan(0);
    });

    test('is silent on the known_good fixture', async ({ page }) => {
      const res = await page.goto(`/tests/render/fixtures/known_good/${check.id}.html`);
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
```

- [ ] **Step 3: Run it and confirm it fails for the right reason**

```bash
npm run test:render:meta
```
Expected: FAIL — `the registry is not empty` × 3 projects, with the message `a harness that examines zero checks is not a passing harness`.

This is the intended red state. Do not proceed until you see that exact failure.

- [ ] **Step 4: Commit the red gate**

```bash
git add tests/render/meta.spec.ts tests/render/checks/index.ts
git commit -m "test(render): gate-integrity meta gate — every check must fire on broken, stay silent on good"
```

---

## Task 4: LAYOUT — no horizontal overflow

Born from `fix(footer): two horizontal-overflow bugs on every page of the site`.

**Files:**
- Create: `tests/render/checks/layout.ts`
- Create: `tests/render/fixtures/known_good/layout-no-horizontal-overflow.html`
- Create: `tests/render/fixtures/known_broken/layout-no-horizontal-overflow.html`
- Modify: `tests/render/checks/index.ts`

- [ ] **Step 1: Write the broken fixture**

Create `tests/render/fixtures/known_broken/layout-no-horizontal-overflow.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>broken overflow</title>
<style>body{margin:0;font:16px/1.5 system-ui}.wide{width:120vw;height:80px;background:#e8604c}</style>
</head><body>
<h1>Overflowing page</h1>
<div class="wide">this box is 120vw wide</div>
<p>Body copy that sits inside the viewport.</p>
</body></html>
```

- [ ] **Step 2: Write the good fixture**

Create `tests/render/fixtures/known_good/layout-no-horizontal-overflow.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>clean overflow</title>
<style>body{margin:0;font:16px/1.5 system-ui}.wide{width:100%;height:80px;background:#2D6A4F}</style>
</head><body>
<h1>Contained page</h1>
<div class="wide">this box fits</div>
<p>Body copy that sits inside the viewport.</p>
</body></html>
```

- [ ] **Step 3: Write the check**

Create `tests/render/checks/layout.ts`:

```ts
import { register, type CheckResult } from '../lib/registry.js';
import type { Page } from '@playwright/test';

register({
  id: 'layout-no-horizontal-overflow',
  family: 'LAYOUT',
  severity: 'advisory',
  describe: 'the document must not scroll sideways at any viewport',
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const de = document.documentElement;
      const limit = de.clientWidth;
      const all = Array.from(document.body.querySelectorAll<HTMLElement>('*'));
      const overflow = de.scrollWidth - limit;
      const offenders: string[] = [];
      if (overflow > 1) {
        for (const el of all) {
          if (getComputedStyle(el).position === 'fixed') continue;
          const box = el.getBoundingClientRect();
          if (box.width === 0 || box.height === 0) continue;
          if (box.right > limit + 1) {
            const cls =
              typeof el.className === 'string' && el.className.trim()
                ? '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.')
                : '';
            offenders.push(`${el.tagName.toLowerCase()}${cls}@${Math.round(box.right)}px`);
          }
        }
      }
      return { overflow, offenders: offenders.slice(0, 8), examined: all.length };
    });

    return {
      examined: r.examined,
      defects:
        r.overflow > 1
          ? [
              {
                checkId: 'layout-no-horizontal-overflow',
                family: 'LAYOUT' as const,
                viewport,
                message: `document overflows by ${r.overflow}px — offenders: ${
                  r.offenders.join(' | ') || 'none isolated'
                }`,
              },
            ]
          : [],
    };
  },
});
```

The document-level measurement is the only thing that raises a defect; the per-element walk runs solely to name offenders. That ordering is deliberate — it is what stops the check reporting intentionally-translated decorative elements as defects on a page that does not actually overflow.

- [ ] **Step 4: Register it**

Replace the contents of `tests/render/checks/index.ts` with:

```ts
// Importing a check module runs its register() call. Add every check file here.
import './layout.js';
export {};
```

- [ ] **Step 5: Run the meta gate**

```bash
npm run test:render:meta
```
Expected: PASS — 9 tests (registry-not-empty + fires-on-broken + silent-on-good, × 3 projects).

- [ ] **Step 6: Commit**

```bash
git add tests/render/checks/layout.ts tests/render/checks/index.ts tests/render/fixtures
git commit -m "test(render): LAYOUT/no-horizontal-overflow with both fixtures"
```

---

## Task 5: LAYOUT — minimum rendered font size

Born from the congo-pair measurement of **108 text nodes rendering below 12.5px**.

**Files:**
- Modify: `tests/render/checks/layout.ts`
- Create: `tests/render/fixtures/known_good/layout-min-font-size.html`
- Create: `tests/render/fixtures/known_broken/layout-min-font-size.html`

- [ ] **Step 1: Write the broken fixture**

Create `tests/render/fixtures/known_broken/layout-min-font-size.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>broken font size</title>
<style>body{margin:0;font:16px/1.5 system-ui}.tiny{font-size:10px}.hiddenbox{display:none;font-size:8px}</style>
</head><body>
<h1>Type scale</h1>
<p>Readable body copy at sixteen pixels.</p>
<p class="tiny">This caption renders at ten pixels.</p>
<div class="hiddenbox"><span>hidden eight pixel text must be ignored</span></div>
</body></html>
```

The hidden node is in the fixture on purpose: a recorded false-positive cause on this site was `display:none` not being tested on ancestors.

- [ ] **Step 2: Write the good fixture**

Create `tests/render/fixtures/known_good/layout-min-font-size.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>clean font size</title>
<style>body{margin:0;font:16px/1.5 system-ui}.caption{font-size:13px}.hiddenbox{display:none;font-size:8px}</style>
</head><body>
<h1>Type scale</h1>
<p>Readable body copy at sixteen pixels.</p>
<p class="caption">This caption renders at thirteen pixels.</p>
<div class="hiddenbox"><span>hidden eight pixel text must be ignored</span></div>
</body></html>
```

- [ ] **Step 3: Append the check**

Append to `tests/render/checks/layout.ts`:

```ts
register({
  id: 'layout-min-font-size',
  family: 'LAYOUT',
  severity: 'advisory',
  describe: 'no visible text may render below 12.5px',
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      let examined = 0;
      const bad: string[] = [];
      let node: Node | null;
      while ((node = walker.nextNode())) {
        const text = (node.textContent || '').trim();
        if (!text) continue;
        const el = node.parentElement;
        if (!el) continue;
        // getClientRects() is empty when ANY ancestor is display:none
        if (el.getClientRects().length === 0) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden') continue;
        examined++;
        const size = parseFloat(cs.fontSize);
        if (size < 12.5) {
          bad.push(`${el.tagName.toLowerCase()} ${size}px "${text.slice(0, 30)}"`);
        }
      }
      return { examined, bad: bad.slice(0, 10), count: bad.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'layout-min-font-size',
              family: 'LAYOUT' as const,
              viewport,
              message: `${r.count} text node(s) below 12.5px: ${r.bad.join(' | ')}`,
            },
          ]
        : [],
    };
  },
});
```

- [ ] **Step 4: Run the meta gate**

```bash
npm run test:render:meta
```
Expected: PASS — 15 tests. If `is silent on the known_good fixture` fails for `layout-min-font-size`, the hidden-node guard is wrong; fix the guard, not the fixture.

- [ ] **Step 5: Commit**

```bash
git add tests/render/checks/layout.ts tests/render/fixtures
git commit -m "test(render): LAYOUT/min-font-size, with a display:none ancestor in both fixtures"
```

---

## Task 6: LAYOUT — tap target size

**Files:**
- Modify: `tests/render/checks/layout.ts`
- Create: `tests/render/fixtures/known_good/layout-tap-target-size.html`
- Create: `tests/render/fixtures/known_broken/layout-tap-target-size.html`

- [ ] **Step 1: Write the broken fixture**

Create `tests/render/fixtures/known_broken/layout-tap-target-size.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>broken tap targets</title>
<style>body{margin:0;font:16px/1.5 system-ui}
a,button{display:inline-block}
.small{width:18px;height:18px;padding:0;font-size:10px}
.ok{min-width:44px;min-height:44px}
</style></head><body>
<h1>Controls</h1>
<a href="#x" class="ok">Reserve this bird</a>
<button class="small">x</button>
<p id="x">target</p>
</body></html>
```

- [ ] **Step 2: Write the good fixture**

Create `tests/render/fixtures/known_good/layout-tap-target-size.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>clean tap targets</title>
<style>body{margin:0;font:16px/1.5 system-ui}
a,button{display:inline-block}
.ok{min-width:44px;min-height:44px}
</style></head><body>
<h1>Controls</h1>
<a href="#x" class="ok">Reserve this bird</a>
<button class="ok">Close</button>
<p id="x">target</p>
</body></html>
```

- [ ] **Step 3: Append the check**

Append to `tests/render/checks/layout.ts`:

```ts
register({
  id: 'layout-tap-target-size',
  family: 'LAYOUT',
  severity: 'advisory',
  describe: 'every visible interactive control is at least 24x24px',
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const sel = 'a[href], button, input:not([type=hidden]), select, textarea, [role=button]';
      const nodes = Array.from(document.querySelectorAll<HTMLElement>(sel));
      let examined = 0;
      const bad: string[] = [];
      for (const el of nodes) {
        if (el.getClientRects().length === 0) continue;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden') continue;
        const box = el.getBoundingClientRect();
        if (box.width === 0 || box.height === 0) continue;
        examined++;
        if (box.width < 24 || box.height < 24) {
          const label = (el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 24);
          bad.push(
            `${el.tagName.toLowerCase()} ${Math.round(box.width)}x${Math.round(box.height)} "${label}"`,
          );
        }
      }
      return { examined, bad: bad.slice(0, 10), count: bad.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'layout-tap-target-size',
              family: 'LAYOUT' as const,
              viewport,
              message: `${r.count} control(s) under 24x24: ${r.bad.join(' | ')}`,
            },
          ]
        : [],
    };
  },
});
```

- [ ] **Step 4: Run the meta gate**

```bash
npm run test:render:meta
```
Expected: PASS — 21 tests.

- [ ] **Step 5: Commit**

```bash
git add tests/render/checks/layout.ts tests/render/fixtures
git commit -m "test(render): LAYOUT/tap-target-size (size only; spacing deferred to Phase 3)"
```

---

## Task 7: IMG — srcset within 2x of rendered width

Born from `harden(congo-pair): correct the hero sizes lie` and the measured 2.13× hero waste.

**Files:**
- Create: `tests/render/checks/img.ts`
- Create: `tests/render/fixtures/known_good/img-srcset-within-2x.html`
- Create: `tests/render/fixtures/known_broken/img-srcset-within-2x.html`
- Create: `tests/render/fixtures/assets/wide-1600.png`, `tests/render/fixtures/assets/narrow-400.png`
- Modify: `tests/render/checks/index.ts`

- [ ] **Step 1: Generate the two fixture images**

PIL is installed; Pillow is the project's image tool (never `sips`).

```bash
mkdir -p tests/render/fixtures/assets
python3 -c "
from PIL import Image
Image.new('RGB',(1600,900),(45,106,79)).save('tests/render/fixtures/assets/wide-1600.png')
Image.new('RGB',(400,225),(232,96,76)).save('tests/render/fixtures/assets/narrow-400.png')
print('ok')
"
```
Expected output: `ok`

- [ ] **Step 2: Write the broken fixture**

A 1600px-wide source painted into a 300px box is 5.33× — well past the 2× ceiling.

Create `tests/render/fixtures/known_broken/img-srcset-within-2x.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>broken srcset</title>
<style>body{margin:0;font:16px/1.5 system-ui}img{display:block;width:300px;height:auto}</style>
</head><body>
<h1>Image weight</h1>
<img src="../assets/wide-1600.png" alt="Congo African Grey perched on a play stand">
</body></html>
```

- [ ] **Step 3: Write the good fixture**

Create `tests/render/fixtures/known_good/img-srcset-within-2x.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>clean srcset</title>
<style>body{margin:0;font:16px/1.5 system-ui}img{display:block;width:300px;height:auto}</style>
</head><body>
<h1>Image weight</h1>
<img src="../assets/narrow-400.png" alt="Congo African Grey perched on a play stand">
</body></html>
```

- [ ] **Step 4: Write the check**

Create `tests/render/checks/img.ts`:

```ts
import { register, type CheckResult } from '../lib/registry.js';
import { settlePage } from '../lib/probes.js';
import type { Page } from '@playwright/test';

register({
  id: 'img-srcset-within-2x',
  family: 'IMG',
  severity: 'advisory',
  describe: 'no image may decode at more than 2x the width it paints at',
  async run(page: Page, viewport: number): Promise<CheckResult> {
    await settlePage(page);
    const r = await page.evaluate(() => {
      const dpr = window.devicePixelRatio || 1;
      let examined = 0;
      const bad: string[] = [];
      for (const img of Array.from(document.images)) {
        const box = img.getBoundingClientRect();
        if (box.width < 1 || !img.complete || img.naturalWidth === 0) continue;
        examined++;
        const ratio = img.naturalWidth / (box.width * dpr);
        if (ratio > 2.0) {
          const file = (img.currentSrc || img.src).split('/').pop();
          bad.push(
            `${file} natural=${img.naturalWidth} painted=${Math.round(box.width)} ${ratio.toFixed(2)}x`,
          );
        }
      }
      return { examined, bad: bad.slice(0, 10), count: bad.length };
    });

    return {
      examined: r.examined,
      defects: r.count
        ? [
            {
              checkId: 'img-srcset-within-2x',
              family: 'IMG' as const,
              viewport,
              message: `${r.count} oversized image(s): ${r.bad.join(' | ')}`,
            },
          ]
        : [],
    };
  },
});
```

- [ ] **Step 5: Register it**

Replace the contents of `tests/render/checks/index.ts` with:

```ts
// Importing a check module runs its register() call. Add every check file here.
import './layout.js';
import './img.js';
export {};
```

- [ ] **Step 6: Run the meta gate**

```bash
npm run test:render:meta
```
Expected: PASS — 27 tests.

- [ ] **Step 7: Commit**

```bash
git add tests/render/checks/img.ts tests/render/checks/index.ts tests/render/fixtures
git commit -m "test(render): IMG/srcset-within-2x — the check that would have caught the hero sizes lie"
```

---

## Task 8: IMG — alt present and unique

Enforces CLAUDE.md Rule 50b: no two images on a page share an alt.

**Files:**
- Modify: `tests/render/checks/img.ts`
- Create: `tests/render/fixtures/known_good/img-alt-present-and-unique.html`
- Create: `tests/render/fixtures/known_broken/img-alt-present-and-unique.html`

- [ ] **Step 1: Write the broken fixture**

Create `tests/render/fixtures/known_broken/img-alt-present-and-unique.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>broken alts</title>
<style>body{margin:0;font:16px/1.5 system-ui}img{display:block;width:120px;height:auto}</style>
</head><body>
<h1>Gallery</h1>
<img src="../assets/narrow-400.png" alt="Congo African Grey for sale">
<img src="../assets/narrow-400.png" alt="Congo African Grey for sale">
<img src="../assets/narrow-400.png">
<img src="../assets/narrow-400.png" alt="">
</body></html>
```

Two defects on purpose (a duplicate pair and a missing attribute), plus a legitimate decorative `alt=""` that must **not** be reported.

- [ ] **Step 2: Write the good fixture**

Create `tests/render/fixtures/known_good/img-alt-present-and-unique.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>clean alts</title>
<style>body{margin:0;font:16px/1.5 system-ui}img{display:block;width:120px;height:auto}</style>
</head><body>
<h1>Gallery</h1>
<img src="../assets/narrow-400.png" alt="Congo African Grey for sale in Midland Texas">
<img src="../assets/narrow-400.png" alt="Hand-raised Congo chick at twelve weeks">
<img src="../assets/narrow-400.png" alt="">
</body></html>
```

- [ ] **Step 3: Append the check**

Append to `tests/render/checks/img.ts`:

```ts
register({
  id: 'img-alt-present-and-unique',
  family: 'IMG',
  severity: 'advisory',
  describe: 'every rendered image declares alt; non-decorative alts are unique on the page',
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
          missing.push((img.getAttribute('src') || '(no src)').split('/').pop() as string);
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
      return { examined, missing: missing.slice(0, 6), dupes: dupes.slice(0, 6) };
    });

    const defects = [];
    if (r.missing.length) {
      defects.push({
        checkId: 'img-alt-present-and-unique',
        family: 'IMG' as const,
        viewport,
        message: `image(s) with no alt attribute: ${r.missing.join(', ')}`,
      });
    }
    if (r.dupes.length) {
      defects.push({
        checkId: 'img-alt-present-and-unique',
        family: 'IMG' as const,
        viewport,
        message: `duplicate alt text (Rule 50b): ${r.dupes.join(' | ')}`,
      });
    }
    return { examined: r.examined, defects };
  },
});
```

- [ ] **Step 4: Run the meta gate**

```bash
npm run test:render:meta
```
Expected: PASS — 33 tests.

- [ ] **Step 5: Commit**

```bash
git add tests/render/checks/img.ts tests/render/fixtures
git commit -m "test(render): IMG/alt-present-and-unique — Rule 50b, with a decorative alt in both fixtures"
```

---

## Task 9: NAV — in-page anchors resolve

**Files:**
- Create: `tests/render/checks/nav.ts`
- Create: `tests/render/fixtures/known_good/nav-anchors-resolve.html`
- Create: `tests/render/fixtures/known_broken/nav-anchors-resolve.html`
- Modify: `tests/render/checks/index.ts`

- [ ] **Step 1: Write the broken fixture**

Create `tests/render/fixtures/known_broken/nav-anchors-resolve.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>broken anchors</title>
<style>body{margin:0;font:16px/1.5 system-ui}</style></head><body>
<nav><a href="#care">Care</a> <a href="#missing-section">Shipping</a></nav>
<h2 id="care">Care</h2><p>Copy.</p>
</body></html>
```

- [ ] **Step 2: Write the good fixture**

Create `tests/render/fixtures/known_good/nav-anchors-resolve.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>clean anchors</title>
<style>body{margin:0;font:16px/1.5 system-ui}</style></head><body>
<nav><a href="#care">Care</a> <a href="#shipping">Shipping</a></nav>
<h2 id="care">Care</h2><p>Copy.</p>
<h2 id="shipping">Shipping</h2><p>Copy.</p>
</body></html>
```

- [ ] **Step 3: Write the check**

Create `tests/render/checks/nav.ts`:

```ts
import { register, type CheckResult } from '../lib/registry.js';
import { measureTopChrome } from '../lib/probes.js';
import type { Page } from '@playwright/test';

register({
  id: 'nav-anchors-resolve',
  family: 'NAV',
  severity: 'advisory',
  describe: 'every in-page #anchor points at an element that exists',
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const links = Array.from(document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]')).filter(
        (a) => (a.getAttribute('href') || '').length > 1,
      );
      const dead: string[] = [];
      for (const a of links) {
        const raw = a.getAttribute('href') as string;
        const id = decodeURIComponent(raw.slice(1));
        const byId = document.getElementById(id);
        const byName = document.querySelector(`[name="${CSS.escape(id)}"]`);
        if (!byId && !byName) dead.push(raw);
      }
      return { examined: links.length, dead: Array.from(new Set(dead)).slice(0, 10) };
    });

    return {
      examined: r.examined,
      defects: r.dead.length
        ? [
            {
              checkId: 'nav-anchors-resolve',
              family: 'NAV' as const,
              viewport,
              message: `dead in-page anchor(s): ${r.dead.join(', ')}`,
            },
          ]
        : [],
    };
  },
});
```

- [ ] **Step 4: Register it**

Replace the contents of `tests/render/checks/index.ts` with:

```ts
// Importing a check module runs its register() call. Add every check file here.
import './layout.js';
import './img.js';
import './nav.js';
export {};
```

- [ ] **Step 5: Run the meta gate**

```bash
npm run test:render:meta
```
Expected: PASS — 39 tests.

- [ ] **Step 6: Commit**

```bash
git add tests/render/checks/nav.ts tests/render/checks/index.ts tests/render/fixtures
git commit -m "test(render): NAV/anchors-resolve"
```

---

## Task 10: NAV — jump targets actually land

The check that would have caught the congo-pair rail. It clicks every chip and measures where the target settles, rather than reading the CSS.

**Files:**
- Modify: `tests/render/checks/nav.ts`
- Create: `tests/render/fixtures/known_good/nav-jump-target-lands.html`
- Create: `tests/render/fixtures/known_broken/nav-jump-target-lands.html`

- [ ] **Step 1: Write the broken fixture**

`scroll-behavior:smooth` plus a sticky header and no `scroll-margin-top` — the exact congo-pair failure, where the heading lands under the header.

Create `tests/render/fixtures/known_broken/nav-jump-target-lands.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>broken jump</title>
<style>
html{scroll-behavior:smooth}
body{margin:0;font:16px/1.5 system-ui}
header{position:sticky;top:0;height:96px;background:#2D6A4F;color:#fff;display:flex;align-items:center}
nav a{color:#fff;margin-right:12px}
section{min-height:1600px;padding:0}
h2{margin:0}
</style></head><body>
<header><nav><a href="#care">Care</a> <a href="#shipping">Shipping</a></nav></header>
<section><h2 id="care">Care</h2><p>Copy.</p></section>
<section><h2 id="shipping">Shipping</h2><p>Copy.</p></section>
</body></html>
```

- [ ] **Step 2: Write the good fixture**

Create `tests/render/fixtures/known_good/nav-jump-target-lands.html`:

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>clean jump</title>
<style>
html{scroll-behavior:auto}
body{margin:0;font:16px/1.5 system-ui}
header{position:sticky;top:0;height:96px;background:#2D6A4F;color:#fff;display:flex;align-items:center}
nav a{color:#fff;margin-right:12px}
section{min-height:1600px;padding:0}
h2{margin:0;scroll-margin-top:112px}
</style></head><body>
<header><nav><a href="#care">Care</a> <a href="#shipping">Shipping</a></nav></header>
<section><h2 id="care">Care</h2><p>Copy.</p></section>
<section><h2 id="shipping">Shipping</h2><p>Copy.</p></section>
</body></html>
```

- [ ] **Step 3: Append the check**

Append to `tests/render/checks/nav.ts`:

```ts
register({
  id: 'nav-jump-target-lands',
  family: 'NAV',
  severity: 'advisory',
  describe: 'clicking an in-page link must leave its target visible below the sticky chrome',
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const chrome = await measureTopChrome(page);
    const hrefs: string[] = await page.evaluate(() =>
      Array.from(
        new Set(
          Array.from(document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]'))
            .map((a) => a.getAttribute('href') as string)
            .filter((h) => h.length > 1)
            .filter((h) => !!document.getElementById(decodeURIComponent(h.slice(1)))),
        ),
      ),
    );

    const defects = [];
    for (const href of hrefs) {
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(80);
      await page.locator(`a[href="${href}"]`).first().click();
      await page.waitForTimeout(1200); // long enough for a smooth scroll to finish if one is running
      const top = await page.evaluate((h: string) => {
        const el = document.getElementById(decodeURIComponent(h.slice(1)));
        return el ? Math.round(el.getBoundingClientRect().top) : NaN;
      }, href);

      const lo = chrome - 8;
      const hi = chrome + 60;
      if (!(top >= lo && top <= hi)) {
        defects.push({
          checkId: 'nav-jump-target-lands',
          family: 'NAV' as const,
          viewport,
          message: `${href} landed at ${top}px; expected ${lo}–${hi}px (measured chrome = ${chrome}px)`,
        });
      }
    }

    return { examined: hrefs.length, defects };
  },
});
```

The 1200ms wait is not padding: the congo-pair measurement was *"click a chip, wait 1.2s, `scrollY` is still 25"*. A check that waited less would report a false failure on a page whose smooth scroll simply had not finished.

- [ ] **Step 4: Run the meta gate**

```bash
npm run test:render:meta
```
Expected: PASS — 45 tests.

If `fires on the known_broken fixture` fails at vp375, the sticky header may wrap to a different height; confirm by reading the reported `measured chrome` value in the message rather than assuming 96px.

- [ ] **Step 5: Commit**

```bash
git add tests/render/checks/nav.ts tests/render/fixtures
git commit -m "test(render): NAV/jump-target-lands — click every chip, measure where it settles"
```

---

## Task 11: The page runner

**Files:**
- Create: `tests/render/targets.json`
- Create: `tests/render/lib/scorecard.ts`
- Create: `tests/render/pages.spec.ts`

- [ ] **Step 1: Write the targets manifest**

All nine slugs verified present in `dist/` on 2026-07-31. Exactly one page carries `"corpus": true` — spec §3.2's frozen sample is one page *per page type*, and `for-sale` is the only type Phase 1 has families for. The other six corpus members (bird, comparison, interior, location, blog, hub) are added in Phase 3 as their families land.

Create `tests/render/targets.json`:

```json
{
  "families_by_page_type": {
    "for-sale": ["IMG", "LAYOUT", "NAV"]
  },
  "pages": [
    { "slug": "congo-african-grey-parrot-pair-for-sale", "page_type": "for-sale", "corpus": true },
    { "slug": "congo-african-grey-for-sale", "page_type": "for-sale", "corpus": false },
    { "slug": "timneh-african-grey-for-sale", "page_type": "for-sale", "corpus": false },
    { "slug": "dna-tested-african-grey-for-sale", "page_type": "for-sale", "corpus": false },
    { "slug": "hand-raised-african-grey-parrot-for-sale", "page_type": "for-sale", "corpus": false },
    { "slug": "african-grey-parrot-bird-eggs-for-sale-usa", "page_type": "for-sale", "corpus": false },
    { "slug": "african-grey-parrot-health-guarantee", "page_type": "for-sale", "corpus": false },
    { "slug": "baby-african-grey-parrot-for-sale", "page_type": "for-sale", "corpus": false },
    { "slug": "african-grey-parrot-adoption-cost", "page_type": "for-sale", "corpus": false }
  ]
}
```

- [ ] **Step 2: Write the partial-result writer**

Each (page, viewport) writes its own file so parallel workers never race on shared state.

Create `tests/render/lib/scorecard.ts`:

```ts
import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import type { Defect } from './registry.js';

/** Named PagePartial, not Partial — `Partial<T>` is a TypeScript built-in and shadowing it here would be a trap for the next reader. */
export interface PagePartial {
  slug: string;
  page_type: string;
  viewport: number;
  examined: Record<string, number>;
  defects: Defect[];
}

const RAW_DIR = resolve(process.cwd(), 'data/quality/raw');

export function writePartial(p: PagePartial): void {
  mkdirSync(RAW_DIR, { recursive: true });
  writeFileSync(resolve(RAW_DIR, `${p.slug}-vp${p.viewport}.json`), JSON.stringify(p, null, 2));
}
```

- [ ] **Step 3: Write the page runner**

Create `tests/render/pages.spec.ts`:

```ts
import { test, expect } from '@playwright/test';
import { readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { registry } from './lib/registry.js';
import './checks/index.js';
import { writePartial } from './lib/scorecard.js';
import type { Defect } from './lib/registry.js';

const here = dirname(fileURLToPath(import.meta.url));
const targets = JSON.parse(readFileSync(resolve(here, 'targets.json'), 'utf8')) as {
  families_by_page_type: Record<string, string[]>;
  pages: { slug: string; page_type: string; corpus: boolean }[];
};

for (const target of targets.pages) {
  const families = targets.families_by_page_type[target.page_type] ?? [];
  const checks = registry.filter((c) => families.includes(c.family));

  test(`${target.slug}`, async ({ page }, testInfo) => {
    const viewport = testInfo.project.use.viewport!.width;
    const res = await page.goto(`/dist/${target.slug}/`);
    expect(res?.status(), `${target.slug} must be built`).toBe(200);

    const defects: Defect[] = [];
    const examined: Record<string, number> = {};

    for (const check of checks) {
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
    });

    const blocking = defects.filter(
      (d) => registry.find((c) => c.id === d.checkId)?.severity === 'blocking',
    );
    expect(
      blocking.map((d) => `[${d.family}] ${d.message}`),
      `${target.slug} @ ${viewport}px`,
    ).toEqual([]);
  });
}
```

**Why the zero-examined-anywhere guard is not in this file.** The obvious place for it is a
`test.afterAll` accumulating examined counts across pages — and that would be a bug. Playwright
runs this suite across two workers, each holding its own module state, so a check that examined
nodes on worker A's pages and nothing on worker B's would look dead to worker B and fail falsely.
The guard belongs where all the data is visible at once: `scripts/build_scorecard.mjs` (Task 12),
which reads every partial from disk after the run.

- [ ] **Step 4: Run the page suite**

```bash
npm run test:render:pages
```
Expected: it runs 9 pages × 3 viewports = 27 tests. **All 27 should pass**, because every check currently ships `severity: 'advisory'` — nothing blocks yet. The purpose of this run is to populate `data/quality/raw/`.

Verify the partials landed:

```bash
ls data/quality/raw/ | wc -l
```
Expected: `27`

- [ ] **Step 5: Commit**

```bash
git add tests/render/targets.json tests/render/lib/scorecard.ts tests/render/pages.spec.ts
git commit -m "test(render): page runner over the 9 for-sale slugs"
```

---

## Task 12: Baseline scorecards, then promote to blocking

**Files:**
- Create: `scripts/build_scorecard.mjs`
- Create: `data/quality/scorecards/*.json` (generated)
- Modify: `tests/render/checks/layout.ts`, `tests/render/checks/img.ts`, `tests/render/checks/nav.ts`

- [ ] **Step 1: Write the merge script**

Create `scripts/build_scorecard.mjs`:

```js
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

const bySlug = new Map();
const examinedAnywhere = new Map();
for (const file of readdirSync(RAW).filter((f) => f.endsWith('.json'))) {
  const p = JSON.parse(readFileSync(resolve(RAW, file), 'utf8'));
  if (!bySlug.has(p.slug)) bySlug.set(p.slug, []);
  bySlug.get(p.slug).push(p);
  for (const [checkId, n] of Object.entries(p.examined)) {
    examinedAnywhere.set(checkId, (examinedAnywhere.get(checkId) ?? 0) + n);
  }
}

// The seam_parity bug class: a check whose selector matches nothing, anywhere,
// reports a clean run forever. Zero across EVERY page is a harness failure, not a pass.
// Checked here rather than in the suite because only this script sees all workers' output.
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
    overrides: [],
    details,
  };
  writeFileSync(resolve(OUT, `${slug}-${date}.json`), JSON.stringify(card, null, 2));
  console.log(`${String(total).padStart(3)}  ${slug}`);
}
console.log(`---\n${grandTotal} defects across ${bySlug.size} pages (run=${runLabel})`);
```

- [ ] **Step 2: Produce the baseline**

```bash
rm -rf data/quality/raw && npm run test:render:pages && node scripts/build_scorecard.mjs --run first
```
Expected: one line per slug with its defect count, then a grand total. **Record that grand total — it is the Phase 1 baseline** the spec's "first-run defects per page: 13 → under 4" target is measured against.

- [ ] **Step 3: Read every finding before promoting anything**

```bash
node -e "
const {readdirSync,readFileSync}=require('fs');
for(const f of readdirSync('data/quality/scorecards')){
  const c=JSON.parse(readFileSync('data/quality/scorecards/'+f));
  if(!c.details.length) continue;
  console.log('\n=== '+c.slug+' ('+c.total+') ===');
  for(const d of c.details) console.log('  vp'+d.viewport+' '+d.checkId+': '+d.message.slice(0,160));
}"
```

**This step is a human read, not a script.** For each finding, open the page and confirm the defect is real before promoting its check. This repository has twelve recorded incidents of a gate reporting a defect that did not exist; a check that produced a false report here must be fixed and given a new `known_good` fixture encoding that false case — it does not get promoted.

- [ ] **Step 4: Promote the checks that survived**

For each check confirmed to have produced zero false reports across all nine pages, change its `severity` from `'advisory'` to `'blocking'` in `tests/render/checks/layout.ts`, `img.ts`, or `nav.ts`. Leave any check that cried wolf as `'advisory'` and open a follow-up.

- [ ] **Step 5: Confirm the gate now bites**

```bash
npm run test:render:pages
```
Expected: pages carrying real defects now **FAIL**, listing them. This is the intended state — the harness is blocking.

Confirm the meta gate still passes:

```bash
npm run test:render:meta
```
Expected: PASS — 45 tests.

- [ ] **Step 6: Commit the baseline and the promotion**

```bash
git add scripts/build_scorecard.mjs data/quality/scorecards tests/render/checks
git commit -m "test(render): baseline scorecards for the 9 for-sale pages, promote clean checks to blocking"
git push origin main
```

---

## Task 13: The counted override hatch (spec §3.1.3)

Once Task 12 promotes checks to `blocking`, a harness bug can stop a legitimate build. The spec's answer is an override that is **recorded, not hidden** — it lands in the scorecard and shows up in every report.

**Files:**
- Modify: `tests/render/pages.spec.ts`
- Modify: `scripts/build_scorecard.mjs`
- Modify: `tests/render/lib/scorecard.ts`

- [ ] **Step 1: Add overrides to the partial shape**

In `tests/render/lib/scorecard.ts`, add one field to `PagePartial`, after `defects`:

```ts
  overrides: { checkId: string; reason: string }[];
```

- [ ] **Step 2: Parse and apply overrides in the runner**

In `tests/render/pages.spec.ts`, insert this immediately after the `targets` constant:

```ts
/**
 * RENDER_OVERRIDE="check-id:reason,other-check:reason"
 * An override suppresses a blocking failure and is written into the scorecard,
 * so overrides are counted rather than hidden. A bare id with no reason is rejected.
 */
const overrides: { checkId: string; reason: string }[] = (process.env.RENDER_OVERRIDE ?? '')
  .split(',')
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
```

Then change the `writePartial` call to pass them through, and the blocking filter to respect them. Replace the block from `writePartial({` to the end of the `expect(` statement with:

```ts
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
```

- [ ] **Step 3: Surface overrides in the scorecard**

In `scripts/build_scorecard.mjs`, replace the line `    overrides: [],` with:

```js
    overrides: parts.flatMap((p) => p.overrides ?? []),
```

And replace the final summary line with:

```js
const allOverrides = [...bySlug.values()].flat().flatMap((p) => p.overrides ?? []);
console.log(`---\n${grandTotal} defects across ${bySlug.size} pages (run=${runLabel})`);
if (allOverrides.length) {
  console.log(`${allOverrides.length} OVERRIDE(S) IN EFFECT — these are suppressed defects:`);
  for (const o of allOverrides) console.log(`  ${o.checkId}: ${o.reason}`);
}
```

- [ ] **Step 4: Prove a bare override is rejected**

```bash
RENDER_OVERRIDE="layout-min-font-size" npm run test:render:pages
```
Expected: FAIL with `RENDER_OVERRIDE entry "layout-min-font-size" needs the form check-id:reason`.

- [ ] **Step 5: Prove a reasoned override suppresses and is recorded**

```bash
RENDER_OVERRIDE="layout-min-font-size:harness bug, tracked in backlog" npm run test:render:pages
node scripts/build_scorecard.mjs --run recheck
```
Expected: the run passes despite any `layout-min-font-size` findings, and the summary prints `1 OVERRIDE(S) IN EFFECT` naming the reason.

- [ ] **Step 6: Commit**

```bash
git add tests/render/pages.spec.ts tests/render/lib/scorecard.ts scripts/build_scorecard.mjs
git commit -m "test(render): counted override hatch — suppressed defects are recorded, never hidden"
git push origin main
```

---

## Definition of done for Phase 1

- [ ] `npm run test:render:meta` passes: every registered check fires on its broken fixture, is silent on its good one, and examined more than zero nodes.
- [ ] `npm run test:render:pages` runs 9 slugs × 3 viewports and fails on real defects.
- [ ] `data/quality/scorecards/` holds a dated first-run scorecard per page, committed.
- [ ] The baseline defect total is recorded in the commit message.
- [ ] Every check is either `blocking` (zero false reports across nine pages) or `advisory` with a written reason.
- [ ] `RENDER_OVERRIDE` rejects a reasonless override and records a reasoned one in the scorecard.
- [ ] `node scripts/build_scorecard.mjs` exits non-zero if any check examined zero nodes across every page, or if zero pages were examined.
- [ ] `git push origin main` done — the harness is on `main`, which is the only branch that deploys.

## What Phase 2 picks up

`data/quality/rework-ledger.json`, `scripts/quality_report.py`, and `skills/cag-learning-loop.md` — the layer that turns these scorecards into a trend, a sorted next-action list, and the promotion path where a lesson may only become a rule after a failing test exists. Phase 1 deliberately produces the data that Phase 2 reads.

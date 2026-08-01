# Layout Legibility and Jump-Target Landings — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Act on the render harness's two ranked findings — `layout-min-font-size` (the worst family on every page type) and `nav-jump-target-lands` (in-page links landing behind or past the pinned chrome) — after first proving which of the flagged rows are page defects and which are harness defects.

**Architecture:** Harness before pages, in three phases. Phase A repairs two confirmed reporting bugs in `nav-jump-target-lands` and settles one open measurement question with a Playwright probe, because four of the eight NAV rows currently carry a root-cause sentence that contradicts its own numbers. Phase B fixes the legibility floor from the top of the cascade down — the global token scale first (three lines, site-wide reach), then the 17 shared components, then the 46 page files — so the largest cohorts are cleared before anyone opens a page file. Phase C re-scores the 15-page corpus and rewrites the baseline. Every fix is proved by the same `npm run test:render:pages` run, and no CSS change is committed without the check count that justifies it.

**Tech Stack:** Playwright (`tests/render/`), TypeScript checks under `tests/render/checks/`, Python reporting (`scripts/quality_report.py`), Astro pages and `src/styles/global.css`, Vitest-style meta gate via `npm run test:render:meta`.

---

## Ground truth measured on this repo, 2026-08-01

Everything below was measured before the plan was written, and several items contradict the summary carried in `docs/reference/technical-seo-fixes-backlog.md`. Where they differ, this section is right and the backlog is stale; Task 12 rewrites the backlog.

### The NAV finding is 5 pages and 8 rows, not 3 pages

Read out of `data/quality/scorecards/*-2026-08-01.json`:

| Page | Viewports | Links | Lands at | Chrome measured | Direction |
|---|---|---:|---|---|---|
| `available/roys` | 375, 768, 1280 | 9 / 21 / 21 | **0px** | 96px (header) | undershoot |
| `baby-african-grey-parrot-for-sale` | 768 | 22 | 114px | 158px (header 96 + nav 62) | undershoot |
| `congo-vs-timneh-african-grey` | 375, 768 | 20 / 20 | 114px | 139px (header 96 + nav 43) | undershoot |
| `dna-tested-african-grey-for-sale` | 375 | 18 | **162px** | 96px (header) | **overshoot** |
| `hand-raised-african-grey-parrot-for-sale` | 375 | 18 | **170px** | 96px (header) | **overshoot** |

Two facts follow that the plan is built around.

**`available/roys` is the largest NAV defect and was not in the brief at all.** Every in-page link on the corpus bird page lands at `0px` — the targets have no `scroll-margin-top` whatsoever, so every heading lands flush under a 96px header. `grep -n "scroll-margin" src/pages/available/roys/index.astro` returns nothing. It is the only page failing at all three viewports.

**`dna-tested` and `hand-raised` fail in the opposite direction from what their message says.** They land at 162px and 170px against a stated band of 88–156px — that is 6px and 14px *past* the far edge, an overshoot. Their root-cause sentence reads `1 of 19 targets have scroll-margin-top under the 96px of pinned chrome`, which describes an undershoot, and describes a minority of one target as the cause of 18 failures.

### Two confirmed bugs in `nav-jump-target-lands`

**Bug 1 — `causeFor` only tests one direction.** `tests/render/checks/nav.ts:64` computes `short` as targets whose `scrollMarginTop < chromeH - 8`. Nothing tests the reverse. On an overshooting page the loop finds whatever small minority exists (here 1 of 19) and lines 72–74 report it as the cause of every failure. The narrative is not merely incomplete, it points the reader at the wrong CSS.

**Bug 2 — the band's far edge is unexplained.** The message names a band (`88-156px`) but the cause text only ever discusses its near edge. A reader who fixes "scroll-margin-top is too small" on `dna-tested` will increase 162px and make it worse.

### One open question that source reading cannot settle

At 375px, `measureTopChrome` reports **96px** on `dna-tested` and `hand-raised` (header only), but reports **158px** on `baby` at 768px (header + rail). All three rails are declared inside `@media (max-width:980px)` and are **not** hidden by the nested `@media (max-width:640px)` block — verified by reading lines 1164+, 1026+ and 1557+ respectively. So at 375px the rail markup is displayed on all three.

Either the rail is genuinely not *pinned* at 375px (a `position:sticky` element only sticks within its parent's box, and `measureTopChrome` scrolls 1.5 viewports before measuring — at 375px that is ~1,220px, possibly past the rail's parent), or the probe misses it. **These have opposite fixes**, and the repo's history is that guessing here produces a site-wide change curing a defect that does not exist. Task 2 measures it.

### The legibility surface is 684 declarations across 64 files

A first grep undercounted this by 5× because the codebase writes `.78rem`, not `0.78rem`, and the pattern required a leading zero. The correct count:

| Declarations | Size | Computed |
|---:|---|---|
| 88 | `.78rem` | 12.48px |
| 84 | `.72rem` | 11.52px |
| 79 | `.68rem` | 10.88px |
| 74 | `.7rem` | 11.2px |
| 47 | `.74rem` | 11.84px |
| 44 | `11px` | 11px |
| 38 | `12px` | 12px |
| 37 | `.76rem` | 12.16px |
| 32 | `.75rem` | 12px |
| 30 | `.66rem` | 10.56px |
| 18 | `10px` | 10px |
| 15 + 15 | `.62rem`, `.64rem` | 9.92px, 10.24px |
| 9 | **`7px`** | 7px |
| 9 + 9 + 6 | `.56rem`, `.6rem`, `.58rem` | 8.96–9.6px |
| … | remainder | under 12.5px |
| **684** | **total** | **across 64 files: 46 pages, 17 components, 1 stylesheet** |

Regenerate this table any time with:

```bash
grep -rhoE 'font-size: *\.?[0-9]+(\.[0-9]+)?(rem|em|px)' src/ --exclude-dir=node_modules | sed 's/font-size: *//' | sort | uniq -c | sort -rn
```

### The `12.48px` band is not a rounding artifact

The backlog says ~11% of hits are `12.48px` = `0.78rem`, calls it "a rounding artifact, not a legibility defect", and advises fixing the 10–12px text and leaving it alone. **`.78rem` is the single most common small size in the codebase at 88 declarations.** Dismissing it exempts the largest cohort permanently and moves the threshold to accommodate a value chosen by hand, not by measurement. Task 6 decides this explicitly, with a recommendation, rather than inheriting the backlog's advice.

### The global token scale itself emits sub-12.5px text

`src/styles/global.css:51–57`:

```css
--fs-eyebrow: clamp(0.625rem, 1.2vw, 0.75rem);    /* 10 → 12px */
--fs-h5:      clamp(0.6875rem, 1.1vw, 0.875rem);  /* 11 → 14px */
--fs-caption: clamp(0.75rem, 1vw, 0.875rem);      /* 12 → 14px */
```

At 375px, `1.1vw` = 4.1px and `1.2vw` = 4.5px, so all three clamp to their minimum: **11px, 10px, 12px**. Line 70 is `h5, h6 { font-size: var(--fs-h5); }`, and CLAUDE.md's Heading Hierarchy Outline Gate mandates **at least 5 H5 and 5 H6 on every page**. So every page on the site renders at least ten headings at 11px on mobile, by design, from three lines of global CSS. This is the highest-leverage fix in the plan and it lands in Task 7.

### Nine declarations at 7px

`.tdial-ring span`, `.cdial-ring span`, `.handraised .ring-of` and siblings set `font-size:7px` inside the circular counter dials on five for-sale pages. These are not a threshold argument — 7px is illegible at any reasonable distance. They are also physically constrained: the text sits inside a ~64px ring. Task 10 handles them as their own category, with a counted exemption if the geometry genuinely cannot carry legible text, following the precedent set by the `img-srcset-within-2x` override.

### What is deliberately NOT in this plan

- **The 33-file image regen.** Separate work: asset pipeline, not CSS, and needs its own re-score. The counted override stays and `quality_report.py` keeps printing it.
- **Freshness deletion-blindness.** Deferred on a reasoned trade-off recorded in the Phase-2 plan: closing it trades a rare false PASS for a rare false FAIL, and on this codebase a gate that cries wolf once is ignored forever.
- **Phase 3 families** (`CSS`/`SEM`/`SCHEMA`/`DUP`) and **Phase 4 rules packs**.
- **The skipped whole-implementation review of Phases 1–2.** Still open; Task 12 records it rather than silently dropping it.

---

## File Structure

| File | Responsibility | Action |
|---|---|---|
| `tests/render/checks/nav.ts` | `causeFor` gains direction-awareness; the defect message names overshoot vs undershoot | Modify |
| `tests/render/fixtures/known_broken/nav-overshoot.html` | A page whose targets overshoot the chrome band — the fixture that makes Bug 1 fail | Create |
| `tests/render/fixtures/known_good/nav-overshoot-fixed.html` | Same page with a correct `scroll-margin-top` — proves the check goes quiet | Create |
| `tests/render/meta.spec.ts` | Register the new fixture pair; assert the cause string names the direction | Modify |
| `scripts/probe_chrome_375.mjs` | One-off diagnostic: is the rail pinned at 375px on `dna-tested`? Prints evidence, judges nothing | Create |
| `src/styles/global.css` | Raise `--fs-eyebrow` / `--fs-h5` / `--fs-caption` minimums above the floor; add `--fs-micro` | Modify |
| `src/components/**` (17 files) | Sweep sub-floor `font-size` in the shared kit | Modify |
| `src/pages/**` (46 files) | Sweep sub-floor `font-size` in page-local CSS | Modify |
| `src/pages/available/roys/index.astro` | Add the missing `scroll-margin-top` | Modify |
| `src/pages/baby-african-grey-parrot-for-sale/index.astro` | Add the rail-aware `scroll-margin-top` override | Modify |
| `src/pages/congo-vs-timneh-african-grey/index.astro` | Same | Modify |
| `docs/reference/technical-seo-fixes-backlog.md` | Rewrite items 1–3 against measured reality | Modify |

The sweep is split component-first because the 17 components are imported by many of the 46 pages; clearing them first shrinks the page-file work and prevents two people fixing the same rendered text in two places.

---

## Task 1: Make `nav-jump-target-lands` name the direction it failed in

The check currently reports an undershoot cause for an overshoot failure. Fix the harness before any page — this is the `cag-learning-loop` rule: an escaped defect is charged to the harness first.

**Files:**
- Create: `tests/render/fixtures/known_broken/nav-overshoot.html`
- Create: `tests/render/fixtures/known_good/nav-overshoot-fixed.html`
- Modify: `tests/render/checks/nav.ts:60-78`
- Modify: `tests/render/meta.spec.ts` *(see Step 4 for the exact registration block)*

- [ ] **Step 1: Write the failing fixture — a page that overshoots**

Create `tests/render/fixtures/known_broken/nav-overshoot.html`. The header is 96px of pinned chrome; every target sets a 200px `scroll-margin-top`, so every link lands ~104px past the band's far edge.

```html
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>nav overshoot fixture</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: system-ui, sans-serif; font-size: 16px; }
  header { position: sticky; top: 0; height: 96px; background: #2D6A4F; color: #fff;
           display: flex; align-items: center; padding: 0 16px; z-index: 50; }
  nav a { color: #fff; margin-right: 12px; display: inline-block; padding: 8px; }
  /* THE DEFECT: 200px clears the 96px header more than twice over. */
  section { scroll-margin-top: 200px; min-height: 1400px; padding: 24px 16px; }
</style>
</head>
<body>
  <header>
    <nav>
      <a href="#alpha">Alpha</a>
      <a href="#bravo">Bravo</a>
      <a href="#charlie">Charlie</a>
    </nav>
  </header>
  <section id="alpha"><h2>Alpha</h2><p>Alpha body.</p></section>
  <section id="bravo"><h2>Bravo</h2><p>Bravo body.</p></section>
  <section id="charlie"><h2>Charlie</h2><p>Charlie body.</p></section>
</body>
</html>
```

- [ ] **Step 2: Write the matching good fixture**

Create `tests/render/fixtures/known_good/nav-overshoot-fixed.html` as a byte-for-byte copy of the broken one with a single changed declaration, so the fixture pair isolates exactly one variable:

```html
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>nav overshoot fixture — fixed</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: system-ui, sans-serif; font-size: 16px; }
  header { position: sticky; top: 0; height: 96px; background: #2D6A4F; color: #fff;
           display: flex; align-items: center; padding: 0 16px; z-index: 50; }
  nav a { color: #fff; margin-right: 12px; display: inline-block; padding: 8px; }
  /* FIXED: clears the 96px header by 12px and lands inside the band. */
  section { scroll-margin-top: 108px; min-height: 1400px; padding: 24px 16px; }
</style>
</head>
<body>
  <header>
    <nav>
      <a href="#alpha">Alpha</a>
      <a href="#bravo">Bravo</a>
      <a href="#charlie">Charlie</a>
    </nav>
  </header>
  <section id="alpha"><h2>Alpha</h2><p>Alpha body.</p></section>
  <section id="bravo"><h2>Bravo</h2><p>Bravo body.</p></section>
  <section id="charlie"><h2>Charlie</h2><p>Charlie body.</p></section>
</body>
</html>
```

- [ ] **Step 3: Run the meta gate to confirm the fixtures are not yet wired**

```bash
npm run test:render:meta
```

Expected: PASS, 98 tests, with **no** test naming `nav-overshoot`. The fixtures exist on disk but nothing loads them yet. If the suite is red before you start, stop and fix that first — a plan step cannot be verified against an already-failing gate.

- [ ] **Step 4: Register the fixture pair and assert the cause names the direction**

Open `tests/render/meta.spec.ts` and find the existing `known_broken` registration block for NAV checks (search for `nav-jump-target-lands` — it sits alongside the other fixture-pair describes). Add this block immediately after it:

```ts
test.describe('nav-jump-target-lands names the direction of failure', () => {
  test('fires on a page whose targets overshoot the chrome band', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(`${FIXTURE_BASE}/tests/render/fixtures/known_broken/nav-overshoot.html`);
    const check = getCheck('nav-jump-target-lands');
    const r = await runCheck(check, page, 1280);

    expect(r.defects.length).toBe(1);
    // The whole point of this fixture: the cause must not blame a too-SMALL margin.
    expect(r.defects[0].message).toMatch(/overshoot|past|beyond|over the/i);
    expect(r.defects[0].message).not.toMatch(/under the \d+px of pinned chrome/);
  });

  test('stays silent when the same page lands inside the band', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(`${FIXTURE_BASE}/tests/render/fixtures/known_good/nav-overshoot-fixed.html`);
    const check = getCheck('nav-jump-target-lands');
    const r = await runCheck(check, page, 1280);

    expect(r.defects.length).toBe(0);
  });
});
```

If `FIXTURE_BASE` or `getCheck` are named differently in the file, use the local names — read the neighbouring describe block and match it rather than introducing a second convention.

- [ ] **Step 5: Run the new tests and watch the first one fail for the stated reason**

```bash
npm run test:render:meta
```

Expected: FAIL, exactly one test — `fires on a page whose targets overshoot the chrome band`. The failure must be the `not.toMatch` assertion, reporting a received message containing `under the 96px of pinned chrome`. That is Bug 1 reproduced.

If instead the first assertion fails (`r.defects.length` is 0), the check is not flagging the overshoot at all, which is a larger bug than the message wording. Record it in the plan's Amendments section and widen this task to cover it before proceeding.

- [ ] **Step 6: Teach `causeFor` both directions**

In `tests/render/checks/nav.ts`, replace the body of the `causeFor` page-evaluate callback — the section running from `let seen = 0;` through the final `return null;` (currently lines 60–78) — with:

```ts
    let seen = 0;
    let short = 0;
    let long = 0;
    for (const id of ids) {
      const el = document.getElementById(id);
      if (!el) continue;
      seen++;
      const smt = parseFloat(getComputedStyle(el).scrollMarginTop || '0');
      // The band nav.ts judges against is [chromeH - 8, chromeH + 60]. A target is
      // "short" when it lands under the chrome and "long" when it lands past the far
      // edge. Testing only `short` reported an undershoot cause for every overshooting
      // page, pointing the reader at the opposite CSS change from the one needed.
      if (smt < chromeH - 8) short++;
      else if (smt > chromeH + 60) long++;
    }

    if (seen && long === seen) {
      return `every target overshoots — scroll-margin-top sits over the ${chromeH}px of pinned chrome plus the 60px tolerance`;
    }
    if (seen && short === seen) {
      return `every target's scroll-margin-top is under the ${chromeH}px of pinned chrome`;
    }
    // Mixed or minority cases: name the larger cohort, and never present a minority
    // as "the" root cause without saying how small it is.
    if (long > short) {
      return `${long} of ${seen} targets overshoot the ${chromeH}px of pinned chrome by more than 60px`;
    }
    if (short) {
      return `${short} of ${seen} targets have scroll-margin-top under the ${chromeH}px of pinned chrome`;
    }
    if (behavior === 'smooth' && docH > 8000) {
      return `html{scroll-behavior:smooth} on a ${docH}px document`;
    }
    return null;
```

Confirm the `+ 60` tolerance matches the band actually used to decide failures further down the file (the `lo`/`hi` pair used in the message at line 202). If it does not, change **this** constant to match the decision band — never the other way round, because the decision band is what the scorecards were built from.

- [ ] **Step 7: Run the meta gate to verify both new tests pass**

```bash
npm run test:render:meta
```

Expected: PASS, 100 tests. The two new tests are green and the 98 pre-existing tests are unchanged. If any previously-green NAV test now fails, the tolerance constant in Step 6 does not match the decision band — go back and reconcile them.

- [ ] **Step 8: Commit**

```bash
git add tests/render/checks/nav.ts tests/render/meta.spec.ts tests/render/fixtures/known_broken/nav-overshoot.html tests/render/fixtures/known_good/nav-overshoot-fixed.html
git commit -m "fix(render): NAV reported an undershoot cause for every overshooting page

causeFor tested only scrollMarginTop < chromeH - 8, so on dna-tested and
hand-raised — which land at 162px and 170px against an 88-156px band — it
found the one small target out of 19 and named it the root cause of all 18
failures. The message told the reader to increase a margin that was already
too large. Fixture pair added; the broken one is red against the old code.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 2: Settle whether the rail is pinned at 375px — measure, do not reason

`measureTopChrome` returns 96px at 375px on `dna-tested` and `hand-raised`, but 158px at 768px on `baby`. All three rails are `display:block` at ≤980px and are not hidden at ≤640px. Either the rails genuinely unstick at 375px, or the probe misses them. The two possibilities have opposite fixes.

**Files:**
- Create: `scripts/probe_chrome_375.mjs`

- [ ] **Step 1: Confirm `dist/` is current before measuring anything**

```bash
npx astro build && ls -la dist/dna-tested-african-grey-for-sale/index.html
```

Expected: a successful build and a file dated today. A probe run against a stale `dist/` measures last week's CSS — this is the failure `checkDistFreshness` exists to prevent, and the probe below does not call it.

- [ ] **Step 2: Write the probe — it prints evidence and judges nothing**

Create `scripts/probe_chrome_375.mjs`:

```js
#!/usr/bin/env node
// One-off diagnostic for the 375px chrome-measurement question (plan Task 2).
//
// It does NOT decide anything. It prints, for each page and scroll position, every
// sticky/fixed element with its computed top/bottom, so a human can see whether the
// jump rail is pinned at the moment measureTopChrome takes its reading.
//
// Run:  node scripts/probe_chrome_375.mjs
// Needs: a server on 4321 rooted at dist/  (npx http-server dist -p 4321 --silent)

import { chromium } from 'playwright';

const PAGES = [
  'dna-tested-african-grey-for-sale',
  'hand-raised-african-grey-parrot-for-sale',
  'baby-african-grey-parrot-for-sale',
];
const VIEWPORTS = [375, 768];

const browser = await chromium.launch();

for (const slug of PAGES) {
  for (const width of VIEWPORTS) {
    const page = await browser.newPage({
      viewport: { width, height: 800 },
      deviceScaleFactor: 1,
    });
    await page.goto(`http://localhost:4321/${slug}/`, { waitUntil: 'load' });

    // Exactly what measureTopChrome does: 1.5 viewports down, settle, then look.
    await page.evaluate(() => window.scrollBy(0, Math.round(window.innerHeight * 1.5)));
    await page.waitForTimeout(250);

    const seen = await page.evaluate(() => {
      const out = [];
      for (const el of Array.from(document.body.querySelectorAll('*'))) {
        const cs = getComputedStyle(el);
        if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
        if (cs.visibility === 'hidden' || cs.display === 'none') continue;
        const b = el.getBoundingClientRect();
        if (b.height === 0 || b.width === 0) continue;
        out.push({
          tag: el.tagName.toLowerCase(),
          cls: (el.className || '').toString().trim().split(/\s+/).slice(0, 2).join(' '),
          position: cs.position,
          cssTop: cs.top,
          top: Math.round(b.top),
          bottom: Math.round(b.bottom),
          // Why a sticky element may have stopped sticking: its parent scrolled past.
          parentBottom: el.parentElement
            ? Math.round(el.parentElement.getBoundingClientRect().bottom)
            : null,
        });
      }
      return { scrollY: Math.round(window.scrollY), els: out };
    });

    console.log(`\n=== ${slug} @ ${width}px  (scrollY=${seen.scrollY}) ===`);
    if (!seen.els.length) console.log('  no sticky/fixed elements visible');
    for (const e of seen.els) {
      const pinned = e.top <= 2 ? 'PINNED-AT-TOP' : `top=${e.top}`;
      console.log(
        `  ${e.position.padEnd(6)} ${e.tag}.${e.cls.padEnd(22)} css-top=${String(e.cssTop).padEnd(7)} ${pinned} bottom=${e.bottom} parentBottom=${e.parentBottom}`,
      );
    }
    await page.close();
  }
}

await browser.close();
```

- [ ] **Step 3: Serve `dist/` and run the probe**

In one shell:

```bash
npx http-server dist -p 4321 --silent
```

In another:

```bash
node scripts/probe_chrome_375.mjs
```

Expected: three page × two viewport blocks, each listing the sticky elements with their measured positions.

- [ ] **Step 4: Read the result against explicit criteria**

Decide from the printed output, not from the CSS:

- **If, at 375px on `dna-tested`, the rail (`.railA`) appears with `top` at or near 96 and a `bottom` around 158** — the rail *is* pinned and `measureTopChrome` missed it. This is a harness bug of the same family as the Phase-1 `measureTopChrome` defect. **Go to Task 3.**
- **If the rail does not appear at all, or appears with `top` far below the viewport top, or its `parentBottom` is above its own `top`** — the rail genuinely unsticks at 375px because its sticky container has scrolled past. The chrome really is 96px, and the pages' `+66px` / `+74px` overrides are wrong at that viewport. This is a page bug. **Skip Task 3 and go to Task 4.**
- **If the output is ambiguous** — for example the rail is present at 375px but its bottom does not match the 62px height seen on `baby` — do not pick the more convenient branch. Record what was printed in the Amendments section, then re-run with `height: 800` changed to the real device height for that width and re-read.

Write the verdict, quoting the probe's own output lines, into the Amendments section at the bottom of this plan before continuing.

- [ ] **Step 5: Commit the probe**

```bash
git add scripts/probe_chrome_375.mjs
git commit -m "test(render): probe for the 375px chrome-measurement question

measureTopChrome returns 96px at 375 on dna-tested and hand-raised but 158px
at 768 on baby, and all three rails are display:block at <=980px. Prints every
sticky element with its box and its parent's bottom at the exact scroll
position the real probe measures from, so the branch is chosen on evidence.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 3: If Task 2 proved the probe missed the rail — fix `measureTopChrome`

**Run this task only if Task 2 Step 4 landed on the first branch.** If it landed on the second, skip to Task 4 and record the skip.

**Files:**
- Modify: `tests/render/lib/probes.ts`
- Modify: `tests/render/meta.spec.ts`

- [ ] **Step 1: Write the failing test**

The band-growing loop in `measureTopChrome` absorbs a candidate when `c.top <= band + 2 && c.bottom > band`. A rail sitting at exactly `top: 96` under a 96px header satisfies that. If the probe still missed it, the element was excluded earlier — by the zero-size guard, the horizontal-span guard, or the opacity guard. The probe output from Task 2 says which. Add a fixture reproducing that specific exclusion.

Create `tests/render/fixtures/known_broken/chrome-two-tier.html`:

```html
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>two-tier chrome fixture</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: system-ui, sans-serif; }
  header { position: sticky; top: 0; height: 96px; background: #2D6A4F; z-index: 50; }
  /* Second tier, pinned directly under the header — the shape measureTopChrome
     must absorb into one 158px band. */
  .rail { position: sticky; top: 96px; height: 62px; background: #faf7f4;
          border-bottom: 1px solid #e7ddd3; z-index: 40; overflow-x: auto;
          white-space: nowrap; }
  .rail a { display: inline-block; padding: 20px 14px; }
  main { min-height: 6000px; padding: 20px; }
</style>
</head>
<body>
  <header></header>
  <div class="rail"><a href="#a">One</a><a href="#b">Two</a><a href="#c">Three</a></div>
  <main><section id="a">A</section><section id="b">B</section><section id="c">C</section></main>
</body>
</html>
```

Add to `tests/render/meta.spec.ts`:

```ts
test.describe('measureTopChrome absorbs a second pinned tier', () => {
  test('reports 158px, not 96px, for header + rail at 375', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 800 });
    await page.goto(`${FIXTURE_BASE}/tests/render/fixtures/known_broken/chrome-two-tier.html`);
    const chrome = await measureTopChrome(page);
    expect(chrome.height).toBe(158);
    expect(chrome.parts.length).toBe(2);
  });
});
```

Add `measureTopChrome` to the file's imports from `./lib/probes.js` if it is not already there.

- [ ] **Step 2: Run it and confirm it fails**

```bash
npm run test:render:meta
```

Expected: FAIL — `Expected: 158, Received: 96`. If it PASSES, the fixture does not reproduce the real exclusion; go back to the Task 2 probe output and build the fixture around the guard it actually named.

- [ ] **Step 3: Fix the guard the fixture exposed**

Apply the minimal change to `tests/render/lib/probes.ts` that makes the fixture pass, and write a comment naming the real page that motivated it. For example, if the horizontal-span guard rejected a rail whose scroll container reported `box.right <= 0`:

```ts
      // must actually span the viewport horizontally — excludes off-canvas drawers.
      // Measured against the element's own box, NOT a scrolled child's: dna-tested's
      // .railA is a horizontal scroller whose inner ul reports a negative right edge
      // once scrolled, which read as off-canvas and dropped 62px of real chrome.
      if (box.right <= 0 || box.left >= window.innerWidth) continue;
```

Do not widen more than one guard per commit. Each guard that stops excluding things is a guard that can start admitting false chrome, and the whole value of this probe is that its number is trusted.

- [ ] **Step 4: Run it and confirm it passes**

```bash
npm run test:render:meta
```

Expected: PASS — 101 tests, including the new one, and every pre-existing chrome test unchanged. If a previously-green test flipped, the widened guard now admits something it should not; narrow it.

- [ ] **Step 5: Commit**

```bash
git add tests/render/lib/probes.ts tests/render/meta.spec.ts tests/render/fixtures/known_broken/chrome-two-tier.html
git commit -m "fix(render): measureTopChrome dropped the second pinned tier at 375

Returned 96px on dna-tested and hand-raised at 375 while returning 158px on
baby at 768, for the same header+rail shape. Every NAV landing on those pages
was therefore judged against a band 62px too high, which is why an overshoot
of 6px read as a failure. Fixture reproduces it red.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 4: Fix the three confirmed undershoots

`available/roys` (0px), `baby` (114px vs 158px) and `congo-vs-timneh` (114px vs 139px) are real page defects in the direction their message says. Fix them regardless of which branch Task 2 took.

**Files:**
- Modify: `src/pages/available/roys/index.astro`
- Modify: `src/pages/baby-african-grey-parrot-for-sale/index.astro:1408`
- Modify: `src/pages/congo-vs-timneh-african-grey/index.astro:753`

- [ ] **Step 1: `available/roys` — add the missing `scroll-margin-top`**

The page has no `scroll-margin-top` anywhere, so all 51 links across three viewports land at 0px. Its mobile jump bar is `.jump-mobile { position: sticky; top: 94px; }` at line 185.

In `src/pages/available/roys/index.astro`, inside the page's existing `<style>` block, immediately after the `.jump-mobile` rule at line 185, add:

```css
    /* Anchored landings. Every in-page link previously landed at 0px — flush under
       the 96px global header — so each jump looked like it had not fired. 108px
       clears the header with 12px of breathing room; the mobile jump bar pins at
       94px and is 44px tall, so the ≤980px override clears both. */
    [id] { scroll-margin-top: 108px; }
    @media (max-width: 980px) {
      [id] { scroll-margin-top: 152px; }
    }
```

Confirm the mobile bar's real height before trusting `152px` — measure it rather than assuming 44px:

```bash
node -e "
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:375,height:800}});
  await p.goto('http://localhost:4321/available/roys/');
  await p.evaluate(() => window.scrollBy(0, window.innerHeight * 1.5));
  await p.waitForTimeout(250);
  console.log(await p.evaluate(() => {
    const el = document.querySelector('.jump-mobile');
    if (!el) return 'no .jump-mobile';
    const b = el.getBoundingClientRect();
    return { top: Math.round(b.top), height: Math.round(b.height), bottom: Math.round(b.bottom) };
  }));
  await b.close();
})();
"
```

Set the `≤980px` value to the printed `bottom` plus 12. If `.jump-mobile` reports `no .jump-mobile` or an unpinned `top`, use `108px` at every viewport and note it.

- [ ] **Step 2: `baby` — add the rail-aware override its siblings already have**

`baby` sets `scroll-margin-top: calc(var(--hdr) + 18px)` = 114px at line 1408 and never raises it, while `.chero-rail` becomes `display:block` at ≤980px (line 1545) adding 62px of chrome. Its siblings all carry the override: `timneh` line 1120 (`+51px`), `egg` line 1167 (`+51px`), `congo` line 1032 (`+51px`).

In `src/pages/baby-african-grey-parrot-for-sale/index.astro`, inside the existing `@media(max-width:980px)` block that opens at line 1542, immediately after `.chero-rail{display:block}` on line 1545, add:

```css
  /* The rail appears here and adds 62px of pinned chrome above the 96px header.
     Without this, all 22 in-page links land at 114px behind 158px of chrome —
     every heading arrives hidden. Measured, not assumed: scorecard 2026-08-01. */
  .baby-main section{scroll-margin-top:calc(var(--hdr) + 74px)}
```

`96 + 74 = 170px`, which sits inside the `150–218px` band the check measured for this page.

- [ ] **Step 3: `congo-vs-timneh` — same fix, different rail height**

`congo-vs-timneh` sets 114px at line 753 against a measured chrome of **139px** (header 96 + nav 43). Its rail is shorter than `baby`'s, so the value differs — do not copy `baby`'s number.

In `src/pages/congo-vs-timneh-african-grey/index.astro`, find the media query that reveals the page's jump rail (the sibling comparison pages use `@media(max-width:900px)` — `african-grey-comparison/index.astro:1323` is the reference) and add inside it:

```css
.cvt .cvt-main section{scroll-margin-top:calc(var(--hdr) + 55px)}
```

`96 + 55 = 151px`, inside the measured `131–199px` band. If the page has no such media query, add one matching the breakpoint at which its rail becomes visible — find it with:

```bash
grep -n "@media\|rail" src/pages/congo-vs-timneh-african-grey/index.astro | grep -B2 -i rail | head -20
```

- [ ] **Step 4: Rebuild and verify all three against the check**

```bash
npx astro build && npm run test:render:pages
```

Expected: the run takes ~12 minutes and completes. Then read the NAV rows:

```bash
python3 - <<'PY'
import json, glob, datetime
today = datetime.date.today().isoformat()
for f in sorted(glob.glob(f'data/quality/scorecards/*-{today}.json')):
    d = json.load(open(f))
    nav = [x for x in d.get('details', []) if x['checkId'].startswith('nav-')]
    print(f"{d['slug']:48s} NAV rows={len(nav)}")
    for x in nav:
        print(f"    vp{x['viewport']} count={x['count']}  {x['message'][:150]}")
PY
```

Expected: zero NAV rows on `available/roys`, `baby-african-grey-parrot-for-sale` and `congo-vs-timneh-african-grey`.

**Stop condition:** if any of the three still reports NAV rows, do not adjust the number until it passes. Read the new message — it now names the direction, thanks to Task 1 — and fix the cause it names. Tuning a constant until a gate goes quiet is how a gate stops meaning anything.

- [ ] **Step 5: Commit**

```bash
git add src/pages/available/roys/index.astro src/pages/baby-african-grey-parrot-for-sale/index.astro src/pages/congo-vs-timneh-african-grey/index.astro
git commit -m "fix(nav): three pages' jump links landed behind the pinned chrome

roys had no scroll-margin-top at all — all 51 links across three viewports
landed at 0px, flush under the 96px header. baby and congo-vs-timneh reveal a
jump rail at their mobile breakpoint without raising the 114px margin to match,
so every heading arrived behind 158px and 139px of chrome respectively.
Verified by nav-jump-target-lands going to zero rows on all three.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 5: Fix whichever of `dna-tested` / `hand-raised` Task 2 assigned to the pages

**Run this task only if Task 2 Step 4 landed on the second branch** (the rails genuinely unstick at 375px). If Task 3 ran instead, these two pages were already cleared by the harness fix — verify that in Step 3 below and skip the edits.

**Files:**
- Modify: `src/pages/dna-tested-african-grey-for-sale/index.astro:1162`
- Modify: `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro:1024`

- [ ] **Step 1: Narrow each override to the breakpoint where its rail is actually pinned**

Both pages set their rail-clearing margin across the whole `≤980px` range, but the rail is only pinned above 640px. In `src/pages/dna-tested-african-grey-for-sale/index.astro`, change line 1162 from:

```css
  .dnat .sec{scroll-margin-top:calc(var(--hdr) + 66px);}
```

to:

```css
  /* The rail is pinned only above 640px; below that it scrolls away with its
     container, so the header alone is the chrome and +66px overshoots by 66px.
     Measured 2026-08-01: 18 of 18 links landed at 162px against a 88-156px band. */
  .dnat .sec{scroll-margin-top:calc(var(--hdr) + 16px);}
  @media (min-width:641px){
    .dnat .sec{scroll-margin-top:calc(var(--hdr) + 66px);}
  }
```

- [ ] **Step 2: The same change on `hand-raised`, with its own value**

In `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro`, change line 1024 from:

```css
  .handraised .sec{scroll-margin-top:calc(var(--hdr) + 74px);}
```

to:

```css
  /* See dna-tested: rail pinned only above 640px. 18 of 18 links landed at 170px
     against a 88-156px band at 375. */
  .handraised .sec{scroll-margin-top:calc(var(--hdr) + 16px);}
  @media (min-width:641px){
    .handraised .sec{scroll-margin-top:calc(var(--hdr) + 74px);}
  }
```

- [ ] **Step 3: Rebuild and verify both pages report zero NAV rows**

```bash
npx astro build && npm run test:render:pages
```

Then re-run the NAV reader from Task 4 Step 4. Expected: zero NAV rows on `dna-tested-african-grey-for-sale` and `hand-raised-african-grey-parrot-for-sale` at every viewport.

If Task 3 ran instead of this task, run this same verification without making any edits — the harness fix should have cleared both pages. If it did not, the two causes are both present and this task's edits are still needed.

- [ ] **Step 4: Commit**

```bash
git add src/pages/dna-tested-african-grey-for-sale/index.astro src/pages/hand-raised-african-grey-parrot-for-sale/index.astro
git commit -m "fix(nav): rail-clearing margin applied below the breakpoint that shows the rail

Both pages set scroll-margin-top for header+rail across the whole <=980px
range, but their rails unstick below 640px — so at 375 the links overshot the
chrome by 66px and 74px. Scoped the larger value to min-width:641px.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 6: Decide the 12.5px threshold explicitly, and record the decision next to the check

684 declarations sit under 12.5px and the largest single cohort — 88 declarations of `.78rem` — computes to 12.48px, failing by 0.02px. The backlog calls that a rounding artifact and advises exempting it. Decide deliberately instead, because 88 declarations is not a rounding band, it is a house style.

**Recommendation: keep the threshold at 12.5 and fix `.78rem` to `.79rem`.** Grounded: `.78rem` is the most-used small size in the codebase, so lowering the threshold to 12.4 would permanently exempt the largest cohort and leave the check unable to ever speak about it again; the visual difference between 12.48px and 12.64px is 0.16px, which no reader will see; and a threshold moved to accommodate the code it measures stops being a measurement. **The trade-off, stated plainly:** this makes the sweep larger — 88 extra declarations across the 64 files — and `.79rem` is an unusual-looking value that a future contributor may "tidy" back to `.78rem`, which is why Step 3 puts a comment on the token rather than relying on the number to defend itself.

**Files:**
- Modify: `tests/render/checks/layout.ts`
- Modify: `src/styles/global.css`

- [ ] **Step 1: Confirm the cohort size before deciding**

```bash
grep -rhoE 'font-size: *\.?0?\.78rem' src/ --exclude-dir=node_modules | wc -l
grep -rlE 'font-size: *\.?0?\.78rem' src/ --exclude-dir=node_modules | wc -l
```

Expected: 88 declarations across some number of files. If the count has moved materially from 88, re-read the recommendation above against the new number before proceeding — the argument depends on the cohort being large.

- [ ] **Step 2: Record the decision in the check itself**

In `tests/render/checks/layout.ts`, replace the `describe` line of the `layout-min-font-size` registration:

```ts
  describe: 'no visible text may render below 12.5px',
```

with:

```ts
  describe: 'no visible text may render below 12.5px',
  // 12.5 was questioned on 2026-08-01: 88 declarations of `.78rem` compute to
  // 12.48px and fail by 0.02px, which reads like a rounding artifact. It is not —
  // `.78rem` is the most-used small size in this codebase, so moving the threshold
  // to 12.4 would exempt the largest cohort permanently and leave the check unable
  // to speak about it again. The threshold stayed; the codebase moved to `.79rem`
  // (12.64px) via `--fs-micro`. Do not lower this number to make a sweep smaller.
```

- [ ] **Step 3: Add the floor token**

In `src/styles/global.css`, immediately after the `--fs-caption` line (line 58), add:

```css
    /* The legibility floor. 12.64px — the smallest size that clears the
       layout-min-font-size check's 12.5px threshold with room for sub-pixel
       rounding. Use this instead of hand-picked .78rem / .72rem / .68rem values.
       Do not "tidy" it to .78rem: that computes to 12.48px and fails. */
    --fs-micro:   0.79rem;                              /* 12.64px */
```

- [ ] **Step 4: Verify the token is live and the check is unchanged**

```bash
npx astro build && grep -c "fs-micro" dist/index.html && npm run test:render:meta
```

Expected: a non-zero grep count and a PASS on the meta gate with the same test count as after Task 1 or Task 3. This step changes no rendered size yet — it only publishes the token and pins the decision.

- [ ] **Step 5: Commit**

```bash
git add tests/render/checks/layout.ts src/styles/global.css
git commit -m "docs(quality): keep the 12.5px floor, add --fs-micro instead of exempting .78rem

The backlog called the 12.48px band a rounding artifact and advised leaving it.
It is 88 declarations — the most-used small size in the codebase — so exempting
it would have retired the check's largest cohort. Threshold stays; the reasoning
now lives next to the threshold so the next reader does not relitigate it.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 7: Raise the global token scale above the floor

Three lines of `global.css` put at least ten headings per page at 11px on mobile, across every page on the site. This is the single highest-leverage change in the plan.

**Files:**
- Modify: `src/styles/global.css:51-58`

- [ ] **Step 1: Capture the before-count on one corpus page**

```bash
npx astro build
npx http-server dist -p 4321 --silent &
sleep 3
node -e "
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:375,height:800}});
  await p.goto('http://localhost:4321/african-grey-parrot-care-guide/');
  const n = await p.evaluate(() => {
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let bad = 0, node;
    while ((node = w.nextNode())) {
      const t = (node.textContent||'').trim(); if (!t) continue;
      const el = node.parentElement; if (!el || !el.getClientRects().length) continue;
      if (getComputedStyle(el).visibility === 'hidden') continue;
      if (parseFloat(getComputedStyle(el).fontSize) < 12.5) bad++;
    }
    return bad;
  });
  console.log('sub-12.5px text nodes at 375px:', n);
  await b.close();
})();
"
```

Record the number. The care-guide page reported 663 instances in the 2026-08-01 corpus run — the highest of the seven page types — so it is the most sensitive place to measure the token change.

- [ ] **Step 2: Raise the three clamp minimums**

In `src/styles/global.css`, replace lines 51–58:

```css
    --fs-eyebrow: clamp(0.625rem, 1.2vw, 0.75rem);    /* 10 → 12px */
    --fs-h1:      clamp(1.75rem, 5vw, 3rem);            /* 28 → 48px */
    --fs-h2:      clamp(1.25rem, 3.5vw, 2rem);          /* 20 → 32px */
    --fs-h3:      clamp(1.0625rem, 2.2vw, 1.5rem);      /* 17 → 24px */
    --fs-h4:      clamp(0.9375rem, 1.8vw, 1.25rem);     /* 15 → 20px */
    --fs-h5:      clamp(0.6875rem, 1.1vw, 0.875rem);    /* 11 → 14px */
    --fs-body:    clamp(0.9375rem, 1.5vw, 1.0625rem);   /* 15 → 17px */
    --fs-caption: clamp(0.75rem, 1vw, 0.875rem);        /* 12 → 14px */
```

with:

```css
    /* Every clamp MINIMUM must clear --fs-micro (12.64px). At 375px a `1.1vw`
       term is 4.1px, so these clamps always resolve to their minimum on mobile —
       which meant --fs-h5 rendered every H5 and H6 at 11px, on every page, while
       CLAUDE.md's Heading Hierarchy Gate mandates at least five of each. The
       maximums are unchanged; only the mobile end moves. */
    --fs-eyebrow: clamp(0.79rem, 1.2vw, 0.8125rem);   /* 12.64 → 13px */
    --fs-h1:      clamp(1.75rem, 5vw, 3rem);            /* 28 → 48px */
    --fs-h2:      clamp(1.25rem, 3.5vw, 2rem);          /* 20 → 32px */
    --fs-h3:      clamp(1.0625rem, 2.2vw, 1.5rem);      /* 17 → 24px */
    --fs-h4:      clamp(0.9375rem, 1.8vw, 1.25rem);     /* 15 → 20px */
    --fs-h5:      clamp(0.8125rem, 1.1vw, 0.875rem);    /* 13 → 14px */
    --fs-body:    clamp(0.9375rem, 1.5vw, 1.0625rem);   /* 15 → 17px */
    --fs-caption: clamp(0.8125rem, 1vw, 0.875rem);      /* 13 → 14px */
```

- [ ] **Step 3: Re-measure the same page and confirm the count dropped**

```bash
npx astro build
```

Then re-run the exact command from Step 1. Expected: a materially lower number than the Step 1 reading. The remainder is page-local and component-local CSS, which Tasks 8 and 9 clear.

**Stop condition:** if the number did not move at all, the token is being overridden downstream — check whether `direction-d.css` re-declares `--fs-h5` or sets `h5, h6 { font-size }` directly, and fix the override rather than raising the token further.

- [ ] **Step 4: Screenshot the change at all three viewports before believing it**

The check measures legibility, not layout balance. Raising a heading from 11px to 13px can wrap a heading that previously fit on one line.

```bash
node -e "
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const w of [375, 768, 1280]) {
    const p = await b.newPage({viewport:{width:w,height:1200}, deviceScaleFactor:1});
    await p.goto('http://localhost:4321/african-grey-parrot-care-guide/');
    await p.waitForTimeout(400);
    await p.screenshot({path:\`/tmp/care-guide-\${w}.png\`, fullPage:false});
    await p.close();
  }
  await b.close();
})();
"
```

Open all three. Look specifically for: eyebrow labels that now wrap, counter-strip numbers that no longer fit their box, and nav pills that have grown past their row. Any of those is a layout regression to fix now, not later.

- [ ] **Step 5: Commit**

```bash
git add src/styles/global.css
git commit -m "fix(a11y): the global token scale itself rendered H5/H6 at 11px on mobile

--fs-h5's clamp minimum was 0.6875rem and its vw term is 4.1px at 375, so it
always resolved to 11px there — on every page, for at least ten headings, since
the Heading Hierarchy Gate mandates five H5 and five H6. --fs-eyebrow resolved
to 10px the same way. Minimums raised above the 12.64px floor; maximums
unchanged. Screenshotted at 375/768/1280 for wrap regressions.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 8: Sweep the 17 shared components

Components are imported by many of the 46 page files, so clearing them first shrinks Task 9 and stops the same rendered text being fixed twice.

**Files:**
- Modify: the 17 files under `src/components/` listed by the command in Step 1

- [ ] **Step 1: List the component files and their offending declarations**

```bash
grep -rnE 'font-size: *(\.[0-7][0-9]*|0\.[0-7][0-9]*)(rem|em)|font-size: *(1[0-2](\.[0-9]+)?|[1-9])px' src/components/ | tee /tmp/component_smallfont.txt | wc -l
cut -d: -f1 /tmp/component_smallfont.txt | sort -u
```

Expected: a line count and 17 unique files, including `cag-library/JumpRail.astro`, `cag-library/JumpLinks.astro`, `cag-library/StickyCtaBar.astro`, `cag-library/MobileNav.astro`, `Breadcrumb.astro`, `cag-inquiry-form.astro`, `cag-inquiry-compact.astro`, `cag-faq-static.astro`, `cag-blog-post.astro`, `cag-hero-3split.astro`, `infographics/ComparisonInfographic.astro`, `infographics/FeatureGridInfographic.astro`.

- [ ] **Step 2: Classify every declaration before changing any of it**

Go through `/tmp/component_smallfont.txt` line by line and put each into one of three buckets. Do this in a scratch file — the classification is the work; the edit is mechanical.

- **Bucket A — real text a reader must read.** Nav labels, breadcrumb links, form labels and hints, list items, captions, badge text, table headers. **Action: raise to `var(--fs-micro)`.**
- **Bucket B — text inside a fixed-geometry ornament.** The circular counter dials, ring labels, anything where 12.64px physically will not fit. **Action: leave for Task 10.**
- **Bucket C — text that is already ≥12.5px** because a parent scales it, or is `display:none` at every viewport. **Action: none.** Verify with the browser rather than by reading — a `.7rem` inside a `1.2rem` parent is `em`-relative only if the unit is `em`, not `rem`.

- [ ] **Step 3: Apply Bucket A across the components**

For each Bucket A declaration, replace the hand-picked size with the token. For example, in `src/components/Breadcrumb.astro`:

```css
  .crumb a { font-size: var(--fs-micro); }
```

and in `src/components/cag-library/JumpRail.astro`:

```css
  .rail a { font-size: var(--fs-micro); font-weight: 600; }
```

Keep every other property on the rule unchanged. Do **not** run a blanket `sed` across the directory — Bucket B lives in the same files and a global replace will inflate ring labels into their own borders.

- [ ] **Step 4: Rebuild, re-measure, and screenshot the component-heavy pages**

```bash
npx astro build
```

Re-run the Step-1 measurement command from Task 7 against three pages that lean on these components:

```bash
for slug in african-grey-parrot-care-guide african-grey-parrots-for-sale blog/african-grey-parrot-cage-setup; do
  echo "== $slug =="
  node -e "
  const { chromium } = require('playwright');
  (async () => {
    const b = await chromium.launch(); const p = await b.newPage({viewport:{width:375,height:800}});
    await p.goto('http://localhost:4321/$slug/');
    console.log(await p.evaluate(() => {
      const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      let bad = 0, node;
      while ((node = w.nextNode())) {
        const t=(node.textContent||'').trim(); if(!t) continue;
        const el=node.parentElement; if(!el||!el.getClientRects().length) continue;
        if (getComputedStyle(el).visibility==='hidden') continue;
        if (parseFloat(getComputedStyle(el).fontSize) < 12.5) bad++;
      }
      return bad;
    }));
    await b.close();
  })();
  "
done
```

Expected: each number lower than after Task 7. Screenshot all three at 375px and check the breadcrumb, jump rail and form labels for wrapping.

- [ ] **Step 5: Commit**

```bash
git add src/components/
git commit -m "fix(a11y): shared components rendered nav, breadcrumb and form text under 12.5px

Swept the 17 component files in src/components/ to var(--fs-micro), skipping
the fixed-geometry dial ornaments which are handled separately. Components
first because they are imported across the 46 page files — clearing them here
prevents the same rendered text being fixed twice.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 9: Sweep the 46 page files, in four batches

46 files is too large for one reviewable commit. Batch by cluster so each commit is a coherent unit and a regression is bisectable to a cluster.

**Files:**
- Modify: the 46 files under `src/pages/` listed by the command in Step 1

- [ ] **Step 1: List the page files and split them into batches**

```bash
grep -rlE 'font-size: *(\.[0-7][0-9]*|0\.[0-7][0-9]*)(rem|em)|font-size: *(1[0-2](\.[0-9]+)?|[1-9])px' src/pages/ --exclude-dir=node_modules | sort | tee /tmp/page_smallfont_files.txt
wc -l < /tmp/page_smallfont_files.txt
```

Expected: 46 files. Split them:

- **Batch 1 — for-sale cluster:** every slug containing `for-sale`, `buy-`, or `adoption-cost`
- **Batch 2 — comparison cluster:** `*-vs-*`, `african-grey-comparison`, `african-grey-pros-and-cons`, `*-breeders-comparison`
- **Batch 3 — interior + care:** `african-grey-parrot-care-guide`, `african-grey-care`, `african-grey-parrot-diet`, `best-african-grey-parrot-food`, `african-grey-parrot-lifespan`, `african-grey-parrot-faq`, `african-grey-parrot-guide`, `how-to-*`, `cites-*`, `captive-bred-*`, `african-grey-reviews`, `african-grey-adoption`, `african-grey-parrot-price`
- **Batch 4 — everything else:** the homepage, hub, location and `available/` pages

- [ ] **Step 2: Apply Task 8's three-bucket classification to Batch 1, then edit**

Same rule as Task 8 Step 2: Bucket A → `var(--fs-micro)`; Bucket B (dial rings, `7px` labels) → leave for Task 10; Bucket C → nothing.

The for-sale cluster is where the `7px` dial labels live, so expect Bucket B to be non-empty here and nowhere else. Do not touch `.tdial-ring span`, `.cdial-ring span`, `.dial-ring span`, or `.handraised .ring-of` in this task.

- [ ] **Step 3: Rebuild and verify Batch 1 with the check itself**

```bash
npx astro build && npm run test:render:pages
```

Then read `layout-min-font-size` counts for the for-sale pages:

```bash
python3 - <<'PY'
import json, glob, datetime
today = datetime.date.today().isoformat()
for f in sorted(glob.glob(f'data/quality/scorecards/*-{today}.json')):
    d = json.load(open(f))
    rows = [x for x in d.get('details', []) if x['checkId'] == 'layout-min-font-size']
    tot = sum(x['count'] for x in rows)
    print(f"{d['slug']:48s} min-font instances={tot:5d} rows={len(rows)}")
PY
```

Expected: the for-sale slugs' instance counts substantially lower than the 2026-08-01 baseline (`baby` 480, `timneh` 477, `hand-raised` 485, `dna-tested` 552, `congo` 418, `congo-pair` 324). A residue remains — the Bucket B dial labels.

- [ ] **Step 4: Commit Batch 1**

```bash
git add src/pages/
git commit -m "fix(a11y): for-sale cluster page CSS raised to the 12.64px floor

Batch 1 of 4. Bucket-A text only; the 7px dial-ring labels are geometry-bound
and are handled separately in the ornament task.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

- [ ] **Step 5: Repeat Steps 2–4 for Batch 2 (comparison cluster)**

Same classification, same verification command, then:

```bash
git add src/pages/
git commit -m "fix(a11y): comparison cluster page CSS raised to the 12.64px floor

Batch 2 of 4.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

- [ ] **Step 6: Repeat Steps 2–4 for Batch 3 (interior + care)**

```bash
git add src/pages/
git commit -m "fix(a11y): interior and care page CSS raised to the 12.64px floor

Batch 3 of 4.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

- [ ] **Step 7: Repeat Steps 2–4 for Batch 4 (homepage, hub, location, available)**

```bash
git add src/pages/
git commit -m "fix(a11y): homepage, hub, location and available page CSS raised to the floor

Batch 4 of 4.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 10: The 7px dial ornaments — fix the geometry or count the exemption

Nine declarations set `font-size:7px` inside circular counter dials on five for-sale pages. 7px is illegible; the question is whether the ring can carry legible text at all.

**Files:**
- Modify: `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro:801`
- Modify: `src/pages/congo-african-grey-for-sale/index.astro:818`
- Modify: `src/pages/baby-african-grey-parrot-for-sale/index.astro:1398`
- Modify: `src/pages/timneh-african-grey-for-sale/index.astro:873`
- Modify: `src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro:917`

- [ ] **Step 1: Measure the ring, do not assume it is too small**

```bash
node -e "
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:375,height:800}});
  await p.goto('http://localhost:4321/baby-african-grey-parrot-for-sale/');
  console.log(await p.evaluate(() => {
    const el = document.querySelector('.tdial-ring');
    if (!el) return 'no .tdial-ring';
    const r = el.getBoundingClientRect();
    const span = el.querySelector('span');
    return {
      ring: { w: Math.round(r.width), h: Math.round(r.height) },
      spanText: span ? span.textContent.trim() : null,
      spanBox: span ? { w: Math.round(span.getBoundingClientRect().width), h: Math.round(span.getBoundingClientRect().height) } : null,
    };
  }));
  await b.close();
})();
"
```

Record the ring's real diameter and the label's text. A ring of ~64px carrying the word `of` can hold 12.64px text; a ring carrying `WEEKS BEFORE A BABY FLIES` at `letter-spacing:.06em` cannot.

- [ ] **Step 2: Take the branch the measurement supports**

**If the label is short (≤4 characters) and the ring is ≥56px:** raise it and keep the ornament.

```css
.tdial-ring span{font-size:var(--fs-micro);color:#6b625a;letter-spacing:.02em}
```

Then rebuild, screenshot the dial at 375px, and confirm the text still sits inside the ring without touching the stroke.

**If the label is long, or the ring is small enough that 12.64px text overflows it:** the honest options are to shorten the label, move it outside the ring, or exempt it. Prefer shortening — a ring reading `of 5` instead of `WEEKS BEFORE A BABY FLIES` says the same thing with the surrounding copy carrying the rest.

**Only if none of those work:** add a counted exemption, following the `img-srcset-within-2x` precedent. Never a silent one.

- [ ] **Step 3: If exempting, register it as a counted override**

Run the page suite with the override so it is recorded in the scorecard and printed by the report every run:

```bash
RENDER_OVERRIDE=$'layout-min-font-size:9 dial-ring ornament labels render at 7px inside ~64px counter rings on five for-sale pages. Legible text does not fit the geometry; shortening the labels is queued in docs/reference/technical-seo-fixes-backlog.md. Every other sub-12.5px instance on these pages is fixed.' npm run test:render:pages
```

Then confirm it appears in section 4 of the report:

```bash
python3 scripts/quality_report.py
```

Expected: `4. OPEN OVERRIDES` lists two distinct overrides — the pre-existing `img-srcset-within-2x` and this one.

- [ ] **Step 4: Commit**

```bash
git add src/pages/
git commit -m "fix(a11y): 7px dial-ring labels resolved

The circular counter dials on five for-sale pages set font-size:7px, which is
illegible at any distance. Measured the ring geometry first rather than
assuming it could not carry real text.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 11: Full corpus re-score and the new baseline

**Files:**
- Modify: `data/quality/scorecards/` (generated)

- [ ] **Step 1: Verify the meta gate before trusting any page result**

```bash
npm run test:render:meta
```

Expected: PASS. A page measured by a failing gate is not evidence — this is the repo's own rule and the reason the meta gate exists. Do not proceed on a red or skipped run.

- [ ] **Step 2: Build clean and run the full 15-page corpus**

```bash
npx astro build && npm run test:render:pages
```

Expected: ~12 minutes, 45 partials, a completed run. If `build_scorecard.mjs` reports `expected N partials, found M` with M < N, a page test crashed — find it and fix it before reading any number. Missing results are not passes.

- [ ] **Step 3: Read the report and compare against the 2026-08-01 baseline**

```bash
python3 scripts/quality_report.py
```

Compare against the recorded baseline: **140 rows across 15 pages — LAYOUT 90, IMG 42, NAV 8; instances LAYOUT 6,498, IMG 333, NAV 149.**

Expected: NAV rows at or near **0**; LAYOUT rows and instances substantially reduced; IMG unchanged at 42 rows (the image regen is out of scope and its override still stands).

**Stop condition:** if LAYOUT instances did not fall by a large margin, do not adjust the threshold and do not re-run hoping for a different number. Read which pages still carry the count and which selectors the messages name, and fix those. If the messages name selectors already swept, the token is being overridden downstream — that is a real finding and belongs in the Amendments section.

- [ ] **Step 4: Commit the new baseline**

```bash
git add data/quality/scorecards/ data/quality/rework-ledger.json
git commit -m "test(render): post-sweep corpus baseline

15 pages, 7 page types. NAV cleared; LAYOUT reduced from the 2026-08-01
baseline of 90 rows / 6,498 instances. IMG unchanged — the 33-file regen
remains out of scope with its counted override standing.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 12: Rewrite the backlog against measured reality, then deploy

The backlog's items 1–3 are now stale in ways that would mislead the next reader: it says three pages where there are five, calls an overshoot an undershoot, undercounts the sweep surface by 5×, and advises exempting the largest cohort.

**Files:**
- Modify: `docs/reference/technical-seo-fixes-backlog.md`

- [ ] **Step 1: Replace backlog item 1 (`layout-min-font-size`)**

Replace the section beginning `### 1. \`layout-min-font-size\` — 3,916 instances` with:

```markdown
### 1. `layout-min-font-size` — swept 2026-08-01

**Resolved for real text.** The surface was 684 declarations across 64 files, not the
129 a first grep suggested — the codebase writes `.78rem`, not `0.78rem`, so a pattern
requiring the leading zero undercounted it by 5×.

Three root causes, fixed top-down:

1. **The global token scale itself.** `--fs-h5`'s clamp minimum was `0.6875rem` and its
   `vw` term is 4.1px at 375px, so it always resolved to **11px** on mobile — applying to
   `h5, h6` site-wide, on pages that carry at least five of each by rule. `--fs-eyebrow`
   resolved to 10px the same way. Minimums now clear the floor.
2. **17 shared components**, swept to `var(--fs-micro)`.
3. **46 page files**, swept in four cluster batches.

**The 12.48px band was NOT a rounding artifact.** The earlier note here advised leaving
`.78rem` alone. It is 88 declarations — the most-used small size in the codebase — so
exempting it would have retired the check's largest cohort permanently. The threshold
stayed at 12.5 and the codebase moved to `--fs-micro: 0.79rem` (12.64px). The reasoning
lives in a comment next to the threshold in `tests/render/checks/layout.ts`.
```

- [ ] **Step 2: Replace backlog item 3 (`nav-jump-target-lands`)**

Replace the section beginning `### 3. \`nav-jump-target-lands\` — the 337 was mostly the harness` with a version that keeps the 337 correction — it is still true and still load-bearing — and replaces the "three pages" paragraph with:

```markdown
**What survived was five pages and eight rows, in two opposite directions.** The
2026-08-01 scorecards, read properly:

| Page | Viewports | Links | Lands at | Chrome | Direction |
|---|---|---:|---|---|---|
| `available/roys` | 375/768/1280 | 51 | 0px | 96px | undershoot — **no `scroll-margin-top` at all** |
| `baby-african-grey-parrot-for-sale` | 768 | 22 | 114px | 158px | undershoot |
| `congo-vs-timneh-african-grey` | 375/768 | 40 | 114px | 139px | undershoot |
| `dna-tested-african-grey-for-sale` | 375 | 18 | 162px | 96px | **overshoot** |
| `hand-raised-african-grey-parrot-for-sale` | 375 | 18 | 170px | 96px | **overshoot** |

And a harness bug underneath them: `causeFor` tested only
`scrollMarginTop < chromeH - 8`, so on the two overshooting pages it found the single
small target out of 19 and reported it as the root cause of all 18 failures — telling
the reader to increase a margin that was already 66px too large. Fixed with a fixture
pair; the check now names the direction it failed in.
```

- [ ] **Step 3: Record the two items that remain open**

Append to the backlog:

```markdown
### 5. Still open after the 2026-08-01 layout pass

- **The 33-file image regen.** Unchanged. `img-srcset-within-2x` still fires on the
  corpus and its counted override still stands, printed by `quality_report.py` every run.
- **Freshness deletion-blindness.** `walk()` reads file mtimes only, so deleting a source
  page leaves `dist/` serving a stale copy while the gate reports fresh. Deliberately not
  fixed: closing it trades a rare false PASS for a rare false FAIL, and on this codebase a
  gate that cries wolf once is ignored forever. Documented in `freshness.ts`.
- **The whole-implementation review of render-harness Phases 1 and 2** was skipped for
  budget and has not been run. Given this repo's record — ten findings in one session, ten
  in the harness and zero in the pages — it is the highest-value unrun check on the system.
```

- [ ] **Step 4: Regenerate page dates and sitemaps**

```bash
python3 scripts/generate_page_dates.py && python3 scripts/generate_sitemaps.py
```

Expected: both succeed. No pages were added or removed, so the sitemap URL count should be unchanged — if it moves, something else changed and needs explaining before deploy.

- [ ] **Step 5: Run the health sweep**

```bash
bash scripts/health-sweep.sh
```

Expected: PASS. Fix anything it reports before pushing — push is deploy.

- [ ] **Step 6: Commit and deploy**

```bash
git add docs/reference/technical-seo-fixes-backlog.md data/page-dates.json public/sitemap*.xml
git commit -m "docs(quality): backlog rewritten against what was measured, not summarized

Items 1 and 3 were stale in ways that would misdirect the next reader: three
pages where there are five, an overshoot described as an undershoot, a sweep
surface undercounted 5x by a grep pattern that required a leading zero, and
advice to exempt the largest cohort as a rounding artifact. Open items now
name the unrun Phase-1/2 implementation review explicitly.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
git push origin main
```

- [ ] **Step 7: Verify the deploy**

```bash
sleep 90
for slug in available/roys baby-african-grey-parrot-for-sale congo-vs-timneh-african-grey dna-tested-african-grey-for-sale; do
  printf '%-45s ' "$slug"
  curl -s -o /dev/null -w '%{http_code}\n' "https://congoafricangreys.com/$slug/"
done
```

Expected: `200` on all four.

---

## Self-Review

Checked against the brief (LAYOUT sweep + the scroll-margins) and against what was measured on the repo.

**Scope coverage**

| Brief item | Task |
|---|---|
| `layout-min-font-size` — the ranked next action | Tasks 6–10 |
| The scroll-margin pages behind the sticky rail | Tasks 1–5 |
| Harness-first discipline (`cag-learning-loop`) | Tasks 1–3 precede every page edit |
| Re-score and new baseline | Task 11 |
| Backlog + deploy | Task 12 |
| 33-image regen | Explicitly out; override left standing, Task 12 Step 3 |
| Freshness deletion-blindness | Explicitly out; recorded, Task 12 Step 3 |
| Skipped Phase-1/2 review | Explicitly out; recorded as open, Task 12 Step 3 |

**Placeholder scan.** No `TBD`, no "similar to Task N", no "add appropriate error handling". Every CSS change shows the replacement text; every verification step shows the command and the expected output. Two places deliberately branch on a measurement rather than prescribe a value — Task 2 Step 4 and Task 10 Step 2 — and both state the decision criteria and what to do in the ambiguous case, which is the opposite of a placeholder.

**Type and name consistency.** `--fs-micro` is defined once (Task 6 Step 3) and consumed in Tasks 7–10. `measureTopChrome`, `runCheck`, `getCheck`, `FIXTURE_BASE` are used with the signatures they already have in `tests/render/`; Task 1 Step 4 says to match the file's local names rather than introduce a second convention. `causeFor`'s `+ 60` tolerance is explicitly reconciled against the decision band in Task 1 Step 6 instead of being assumed.

**Ordering.** The harness is green after every commit: Task 1 lands the fixture and the fix together; Task 3 is conditional and self-contained; the page sweeps come after the token change so the largest cohorts are gone before anyone opens a page file. Task 6 publishes `--fs-micro` before Tasks 7–10 consume it.

**Stop conditions are stated in the tasks, not implied:** Task 2 Step 4 (three branches, including the ambiguous one), Task 4 Step 4 ("do not adjust the number until it passes"), Task 7 Step 3 (token overridden downstream), Task 11 Step 1 (never read pages through a red gate) and Step 3 (do not re-run hoping for a different number). This matters more than usual here: the finding being acted on is a 3,916-instance count, and the cheapest way to make a large count go away is to move the threshold that produced it.

**Known weakness.** The `layout-min-font-size` check measures legibility, not layout balance — raising a size can wrap a heading or overflow a box, and nothing in the harness catches that. Tasks 7, 8 and 10 each require screenshots at 375/768/1280 for exactly this reason. That is a human check inside an otherwise mechanical plan, and it is the step most likely to be skipped under time pressure.

---

## Amendments During Execution

Record deviations here as they happen, so a later reader is not misled by a task body that no longer matches what shipped. The commits are authoritative; this is the index.

### Task 1 — one fixture pair became four, and the fix was never the problem

Commits `91a6013`, `446770b`, `43a9873`, plus the consolidation commit that follows them.

**Every count in Task 1's body was stale.** The meta gate was at **104**, not 98, before any of this landed; it is at **108 passed / 12 skipped** after. Task 1 Step 3's "PASS, 98 tests" and Step 7's "PASS, 100 tests" were both wrong when written.

**The RED step went red on a different assertion than predicted.** Step 5 said the failure would be `not.toMatch(/under the \d+px of pinned chrome/)`. It was actually the *positive* assertion: with a uniform 200px cohort there is no minority for the old code to misblame, so `causeFor` returned `null` — "no single page-level cause identified" — rather than the wrong cause. The fixture reproduced overshoot-*blindness*, not the overshoot-*misattribution* actually measured on `dna-tested` and `hand-raised`. The `not.toMatch` assertion passed even in the RED state; it had no teeth.

**Four fixtures were needed, not one pair, and each addition came from attacking the previous round rather than from a new requirement:**

1. `nav-overshoot.html` + `nav-overshoot-fixed.html` — pins all-overshoot vs all-in-band.
2. `nav-overshoot-mixed.html` (18 at 200px, 1 at 40px) — pins the shape actually measured on the real pages. Verified by reproducing the verbatim scorecard string `1 of 19 targets have scroll-margin-top under the 96px of pinned chrome` against the pre-fix code. Without it, the branch that changes what those two pages print was shipping untested.
3. `nav-undershoot-minority.html` (18 in-band at 108px, 1 at 40px) — closes a **constructible bypass**: defining `long` as "not short" rather than "past the far edge" passed all three earlier fixtures while reporting `18 of 19 targets overshoot` on a page where 18 targets are correct. Mutation-tested: three green, one red.

**The consolidation round then rewrote `diagnoseLandingCause` itself**, closing four review findings at once — it now takes `targets`, `lo` and `hi` **from the caller** instead of re-deriving them. That fixed two latent defects the fixtures could not have caught: the diagnostic had been rebuilding its own id set with **no box or visibility filter** while the headline counted the filtered set (why real scorecards read `18 of 18 in-page links … 1 of 19 targets` — two counts over two different populations), and it recomputed `chromeH ± 8/60` inline, so its idea of the band could drift from the band that actually decides a failure. It now reports **both** cohorts when both exist, because naming only the majority silently drops the targets needing the opposite fix.

**The decision-band expression at `nav.ts:151-152` was never modified**, in any commit. That was the hard constraint — every scorecard in `data/quality/scorecards/` was computed from it.

**`onlyOnce` used to fail open.** It skipped on the string literal `'vp375'`; renaming that project made all four direction tests skip in *every* project with the suite still reporting green. It now derives from `testInfo.config.projects[0].name`. Proven by renaming the project and confirming the four tests still execute.

**The transferable lesson, and the correction to this plan's own method:** Task 1 specified what the fixtures should *contain* but not what they must *prove*. Three successive rounds each shipped a test that would pass on a wrong implementation. **Mutation-kill, not green, is the acceptance criterion for a gate-integrity fixture** — if you cannot state which wrong implementation the fixture rejects, it pins nothing. Task 3, if the Task 2 probe leads there, is written under that standard.

### Task 2 — neither branch was right: the chrome measurement is ORDER-DEPENDENT

The probe was written to choose between "the rail is genuinely not pinned at 375px" (page bug → Task 5) and "the probe misses a pinned rail" (harness bug → Task 3). **The answer is a third thing that invalidates both, and it invalidates two of this plan's own NAV conclusions.**

Measured with the REAL `measureTopChrome` — a hand-rolled copy in `scripts/probe_chrome_375.mjs` did NOT reproduce the harness's own readings, and using it would have produced a confident wrong answer:

| Page | Viewport | Fresh load | Pre-scrolled deep |
|---|---|---:|---:|
| dna-tested | 375 | **96** | **147** (header 96 + railA 51) |
| dna-tested | 768 | **96** | **147** |
| hand-raised | 375 | **96** | **158** (header 96 + railB 62) |
| hand-raised | 768 | **96** | **158** |
| baby | 768 | **158** | 158 |
| baby | 375 | **96** | **158** |
| all three | 1280 | 96 | 96 (rails are ≤980px only — correct) |

**`measureTopChrome`'s 1.5-viewport scroll is not far enough to pin these rails.** It returns 96px on a freshly-loaded page and 147–158px on the same page pre-scrolled. Since `pages.spec.ts` shares one page object across every check, NAV measures whatever state the previous check left behind — so the band `[chrome-8, chrome+60]` that judges every landing is **non-deterministic across runs and dependent on check order.** This is the same defect class as Phase-1 lesson #2, which moved the measurement from scrollY 0 to 1.5 viewports; 1.5 viewports is still short.

`baby @768` is the tell. It is the ONE row in the 2026-08-01 scorecards that recorded 158px while dna-tested and hand-raised recorded 96px — because at 768×1024 a 1.5-viewport scroll is 1,536px, which happens to clear baby's rail. Nothing about baby was different; the scroll distance was.

**Consequence 1 — `dna-tested` and `hand-raised` are FALSE POSITIVES. Task 5 must not run.** Their true chrome is 147px and 158px, so their true bands are `[139, 207]` and `[150, 218]`. They land at **162px** and **170px** — comfortably inside. Their `+66px` and `+74px` overrides are **correct as written**. Task 5 would have narrowed two working pages to a `min-width:641px` scope and broken the mobile landings it was trying to fix. This is the "verify the gate before you fix the page" rule catching a page edit that would have introduced the defect it was meant to remove.

**Consequence 2 — Task 3 is required, but not for the reason it was written.** Its premise (a guard wrongly excluding a visible rail) is wrong: all three guards pass. The real fix is to make the measurement **deterministic and independent of prior page state**. Recommended approach — sample the band at several scroll depths and take the maximum, because neither a fixed offset nor "scroll to the bottom" is safe: at the document end a sticky element whose parent has ended has already *un*stuck. Chrome is "the most that can be pinned at once", not "what is pinned at one arbitrary offset".

**Consequence 3 — every NAV row in every existing scorecard was judged against a possibly-wrong band**, so the NAV portion of the 2026-08-01 baseline cannot be trusted until Task 3 lands and Task 11 re-scores. The LAYOUT and IMG portions are unaffected — they never consult chrome height.

**Consequence 4 — `available/roys`, `baby` and `congo-vs-timneh` remain real defects** (Task 4 stands), but their corrective *values* must be derived after Task 3, not from the current scorecards' band figures.

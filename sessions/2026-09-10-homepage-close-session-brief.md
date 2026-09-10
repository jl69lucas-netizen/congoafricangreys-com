# 2026-09-10 — Homepage close-out + component variations

## Brief (restated)
Goal: close open flags 1/2/4/6 from the 2026-09-09 evidence pass on `/` only; fix IMG-oversized, IMG-dup-alt, NAV-scroll-margin; fix the oklab contrast harness bug; run every gate on `/`; deliver 3×3 component variations on a design canvas + a component library artifact + a skill.
Scope: `src/pages/index.astro`, `data/reviews.json`, `HeroV3.astro`, `tests/render/checks/a11y.ts` + 2 fixtures, `scripts/evidence_audit.py` (per-page title cap), `.claude/agents/cag-homepage-builder.md`. Nothing else on the site.
Gates: `npm run test:render:meta` → `npm run test:render:pages` → hardening scan → final_page_audit --type home → aeo → evidence → seam → dup → quality_report → pytest.
Done: gates green or overridden visibly; built, committed, pushed, IndexNow `/` submitted; artifacts published; canvas published; skill registered.
Out of scope: blog titles, Rule 21 text, budget calibration, sitewide srcset, any other page.

## Open Flags

- evidence_audit term-budget WARNs on `/` for USDA/CITES/DNA/vet/PBFD/hatch are breeder-accepted (2026-09-10: "these are entities Google needs to see"). Not a defect. Revisit when Sprint 0 calibrates budgets.
- B2 touched one shared component: `OwnerCard.astro` `scroll-mt-20` → `scroll-mt-28` (both consumers sit under the same 96px header; 80px was wrong on both). Rendered output of `/trusted-african-grey-parrot-breeders/` changed → submit it to IndexNow with `/` at ship (Task C2).
- B3 follow-up not done: two SplitFeature images on `/` have variants the ladder cannot reach (`timneh-african-grey-variant.webp` has 310/390/579 but the tag asks [600,1000]; `african-grey-head-scratch-cags-breeder.webp` variants are named `-card-NNN`). Both masters sit inside 2×, so no defect — a missed byte saving. Re-plan with `image_srcset_plan.mjs` (slug "" for the homepage) when the BirdCard ladders are redone.
- srcset toolchain traps found 2026-09-10 (harness, not pages): `plan.mjs`/`verify.mjs` build `/${slug}/`, so `index` 404s — pass `""` for the homepage; `map.mjs` must run AFTER `instrument.mjs --off` (offsets are recorded unstamped); `verify.mjs` reuses one page across viewports so Chrome keeps a cached larger candidate — measure with a fresh context per viewport. Fix the scripts before the next cluster run.

## Gate Pass 2026-09-10

Every gate run against `dist/` after `npx astro build` (105 pages, 27.0s). The full page
gate was run **twice**. Nothing was fixed in this pass — findings are recorded only.

### 1. Gate → verdict → examined → rows

| Gate | Verdict | Examined (its own count) | Rows on `/` |
|---|---|---|---|
| `npx astro build` | OK | 105 pages built in 27.0s | — |
| `npm run test:render:meta` | **PASS** | 255 passed · 24 skipped | — |
| `npm run test:render:pages` (run 1) | **PASS** (57 tests, 15.1m) | 19 pages · 294 rows sitewide | **24 rows / 216 inst** |
| `npm run test:render:pages` (run 2) | **PASS** (57 tests, 14.7m) | 19 pages · 294 rows sitewide | **24 rows / 216 inst** |
| `page_hardening_scan.py index` | **NO VERDICT** — did not terminate (>30 CPU-min, 0 bytes out) | see harness defect H1 | — |
| `seam_parity.py index` | FAIL `index.astro` sections=20 seams=6 missing=13 | 52 pages using the idiom (53 N/A) · 29 FAIL | out-of-profile, see F3 |
| `final_page_audit.py index --type home` | **PASS-WITH-WARNINGS** | 1 of 1 | WARN `min_h6_5`, `house_method` |
| `aeo_audit.py index` | **0 pages matched — not a pass** (harness defect H2) | 0 | — |
| `aeo_audit.py --all` (homepage row `── /`) | 0 ERROR / 3 WARN | 105 pages examined | 3 WARN |
| `evidence_audit.py index` | **0 ERROR / 8 WARN**, exit 0 | 1 page | 8 WARN (6 proof `NOT FETCHED` + 2 statement-label PROXY) |
| `dup_content_audit.py --headers` | FAIL — 160 crossover headers sitewide | 105 pages | homepage in **24** crossover rows (keyed `'dist'`, harness defect H3) |
| `python3 -m pytest tests/ -q` | **PASS** | 186 passed in 2.07s | — |
| `quality_report.py` | reported | §1 PAGE 38/278 = 13.7% · harness self-repair 36 = 13.0% | §3 worst family **CSS (111 rows)** · §4 0 overrides · §5 **15** untested rules |

`quality_report.py` §5 untested-rule list (15): entity-4-move-loop,
meaningful-words-no-stop-words, header-style-declared, image-keyword-distribution,
uniform-inbody-image-sizing, link-first-anchors, src-pages-is-deployed,
skills-are-registered, design-context-read-first, visual-first-workflow,
same-content-on-redesign, verify-the-gate-first, for-sale-extended-meta,
shipping-cost-on-every-card, design-system-nine.

### 2. Homepage scorecard — every check's examined count

`data/quality/scorecards/index-2026-09-10.json` (run=first, harness 2.0.0),
**identical in both runs**.

| Check | Examined | Rows (×3 viewports) |
|---|---|---|
| `layout-no-horizontal-overflow` | 3 | 0 |
| `layout-min-font-size` | 3557 | 0 |
| `layout-tap-target-size` | 555 | 0 |
| `layout-hero-counter-separation` | **0** | 0 — structural, see below |
| `layout-h3-image-first` | **0** | 0 — structural, see below |
| `img-srcset-within-2x` | 117 | **0** (was 3) |
| `img-alt-present-and-unique` | 117 | **0** (was 3) |
| `nav-anchors-resolve` | 258 | 0 |
| `nav-jump-target-lands` | 58 | **0** (was 3) |
| `sem-heading-order` | 300 | 0 |
| `sem-all-six-levels` | 300 | 3 (count 2 — H6=3) |
| `sem-title-case-headings` | 300 | 3 (count 29) |
| `sem-section-opening-paragraph` | 300 | 3 (count 5) |
| `sem-statement-label-visible` | 96 | 0 |
| `schema-single-product-offer` | 24 | 3 (count 2) |
| `schema-sold-not-instock` | **0** | 0 — no sold birds on `/` |
| `schema-date-modified-present` | 24 | 0 |
| `schema-no-visible-date` | 3 | 0 |
| `css-class-resolves` | 24135 | 3 (count 20) |
| `css-no-dead-component-rule` | 309 | 3 (count 6) |
| `css-component-color-not-overridden` | 60 | 3 (count 1) |
| `a11y-text-contrast-aa` | 2742 | 3 (count **7**, was 44/39/39) |

**The two zeros are structurally correct, not broken checks** — confirmed on
`dist/index.html`, no edit made:
- `layout-hero-counter-separation` selects `.counter-wrap, .counter-strip, [data-counters]`
  and returns `examined: 0` when none exists. `grep -c 'counter-wrap\|counter-strip\|data-counters' dist/index.html` → **0**.
- `layout-h3-image-first` counts only H3 blocks that OWN an `img.sec-img`.
  `grep -c 'sec-img' dist/index.html` → **0** (the page has 61 H3s, none with a `.sec-img`).
- `schema-sold-not-instock` → 0 because `/` lists no sold bird.
- `targets.json` `families_by_page_type.home` = IMG, LAYOUT, NAV, SEM, SCHEMA, CSS, A11Y
  (**no DUP** — that is why no DUP row appears; correct for the home profile).

### 3. Baseline 2026-09-09 → today

| Family | 2026-09-09 | 2026-09-10 | Δ |
|---|---|---|---|
| IMG | 6 rows | **0** | −6 (B3 measured srcset + dup-alt fix) |
| NAV | 3 rows | **0** | −3 (B2 `scroll-mt-28`) |
| A11Y | 3 rows / 44+39+39 inst | 3 rows / **7+7+7** inst | −108 instances (B1 oklab readback) |
| SEM | 9 | 9 | 0 |
| SCHEMA | 3 | 3 | 0 |
| CSS | 9 | 9 | 0 |
| **total** | 30 rows / 304 inst | **24 rows / 216 inst** | −6 rows / −88 inst |

### 4. Run 1 vs run 2

Run 1 15.1m · run 2 14.7m · both 57 passed · both 294 defect rows across 19 pages.
Diffed the homepage scorecard field-by-field:

- `defects` — identical: `{SEM: 9, SCHEMA: 3, CSS: 9, A11Y: 3}`, total 24 rows / 216 inst.
- `examined_by_check` — **identical for all 22 checks**, including the large ones
  (`css-class-resolves` 24135, `a11y-text-contrast-aa` 2742, `layout-min-font-size` 3557).
- `details` — **no row differs**: same viewport, checkId, count and message text.

**Zero divergence between runs.** The homepage result is reproducible; nothing here is a
bimodal metric masquerading as a finding.

### 5. Runtime probes — Playwright, `file://dist/index.html`, fresh context per viewport

(The Browser pane reports a zero viewport, so every number below is Playwright.)

| Probe | 375 | 768 | 1280 |
|---|---|---|---|
| `scrollWidth` vs `innerWidth` | 375 / 375 ✓ | 768 / 768 ✓ | 1280 / 1280 ✓ |
| elements with `rect.right > innerWidth+1` | 5 | 5 | **0** |
| …all inside a scroll/clip ancestor? | yes — `div.overflow-x-auto [auto]` (the comparison table) | yes — `div.grid.overflow-hidden [hidden]` (the card rail) | — |
| `.hero-v3-b` height | 951px | 842px | **649px** |
| hero `div.grid` height | 951px | 842px | 649px (`.hero-v3-b` padding = `0px`, so grid == hero) |
| `h1` computed font-size | 28.95px | 38.4px | 38.4px |
| `#available-birds article` heights | 682/682/702/722/702/682 | 682/660/702/722/679/682 | 633/633/633/**652**/633/633 |
| uniform ±2? | **no** (Δ40) | **no** (Δ62) | **no** (Δ19) |
| `#cag-jump-rail` | hidden | hidden | **visible** ✓ |
| `.cag-jump-mobile` | **visible** ✓ | visible | hidden ✓ |
| `main p` > 75ch (real `ch`, 100 zeros in the element's own font) | **0** | **0** | **0** |

No horizontal overflow at any viewport — the five "offenders" at 375 and 768 are
confirmed children of an `overflow-x` container, which is the sanctioned pattern and not
a defect (gate-integrity trap #5-shape). Line length is clean everywhere with a measured
`ch`; the `0.5em` approximation that over-reports ~20% was not used.

Open: **the hero is 649px at 1280, over the 350–400px band** (Part D's job), and the bird
cards are not height-uniform at any viewport — one card runs 19–62px taller.

### 6. Learning loop — this session's fix/repair commits

`git log --since="2026-09-10 00:00" | grep -iE "fix|revert|correct|restore|repair"` → 8 hits.

| SHA | Subject | Family | Page or harness |
|---|---|---|---|
| `0b909af8` | a11y-text-contrast-aa normalises `oklab()`/`color()` by canvas readback | **GATE** | **harness** — the check mis-parsed modern colour syntax and invented 44/39/39 instances; page untouched |
| `40e61081` | a11y contrast — true fixture counts, colour-string cache | **GATE** | **harness** — follow-up to the same defect |
| `3ae91b0d` | in-page anchors clear the 96px header (`scroll-mt-28`) | **NAV** | **page** — real; `nav-jump-target-lands` was right |
| `cce25371` | `OwnerCard` `#about` anchor `scroll-mt-28` on both consumers | **NAV** | **page** — same defect in a shared component |
| `3643b254` | hero credential pills wrap instead of overflowing | **LAYOUT** | **page** — caused by A4's longer credential labels; self-inflicted, caught same session |
| `31091bb3` | evidence: warn on a per-slug override term the page type never caps | **GATE** | **harness** — silent no-op override |
| `63473b93` | restore the five-part title and meta description | **COPY** | **page** — breeder ruling, not a defect escape |
| `33056dc9` | docs(plan) fold the 2026-09-10 rulings | — | docs only |

`rework_ledger.py --last-30-days` → 2026-08-11..2026-09-10: **PAGE 5/45 = 11.1%** ·
harness self-repair 7 = 15.6% · NAV 3, LAYOUT 1, COPY 1.

Reading: 4 of 8 were harness, 3 page, 1 docs. Harness self-repair (15.6%) is now running
*ahead* of page rework (11.1%) — the invariants are absorbing the errors, which is the
intended direction. The one page defect that escaped a gate (hero pill overflow) was
caused by a same-session content change, not by a missing rule; per CLAUDE.md it is
charged to the change, not to a new rule.

### 7. New harness defects found this pass (recorded, NOT fixed)

- **H1 — `page_hardening_scan.py <slug>` cannot be scoped, and does not terminate on the
  homepage.** `main()` filters with `pages = [p for p in pages if any(s in p for s in args)]`.
  Every built page's path ends `/index.html`, so the slug `index` matches **all 105 pages**
  (proved: `len([p for p in glob('dist/**/index.html') if 'index' in p]) == 105`). The run
  burned >30 CPU-minutes with 100% of `sample(1)` frames inside the regex engine (three
  frames below `main`, consistent with `_subtrees_with_class` / `check_class_drift`
  backtracking) and produced no output. **The homepage has no hardening-scan verdict this
  pass.** Fix belongs in `tests/render/fixtures/known_broken/` first, per CLAUDE.md.
- **H2 — `aeo_audit.py index` matches nothing.** The filter is `f"/{s}/" in p`; the
  homepage is `dist/index.html`, which has no `/index/` segment, so the homepage is
  **unreachable by slug** and only appears under `--all` (as `── /`). The script correctly
  refuses to call it a pass, so this is a coverage gap, not a false green.
- **H3 — `dup_content_audit.py` keys the homepage `'dist'`.** `pages = {p.parent.name or "home": p ...}`
  — `dist/index.html`'s parent directory is named `dist`, so the `or "home"` branch is dead
  and the homepage is labelled `dist` in every crossover row. Cosmetic, but it makes the
  homepage invisible to anyone grepping the report for `index` or `home`.

### 8. Findings on the page (recorded, NOT fixed)

- **F1 — a11y: 7 real rows at every viewport.** clay/green glyphs at 3.22–3.38:1 against
  their ground: `div "5"` 3.38:1, `.text-green-600.font-bold "✓"` 3.22:1 (×several),
  `"!"`. Needs 4.5:1. Left for triage.
- **F2 — hero 649px at 1280**, over the 350–400px band. Part D.
- **F3 — seam parity FAIL on `index.astro`** (20 sections / 6 seams / 13 missing). The
  gate's own docstring calls one-seam-per-section "a for-sale / comparison-cluster
  convention, not a sitewide law"; the homepage is neither, and `families_by_page_type.home`
  does not carry DUP for the same reason. Confirmed on `dist/index.html`: 6 `cag-seam`,
  26 `<section`. Treat as out-of-profile until the breeder rules otherwise.
- **F4 — `sem-title-case-headings` count 29** — all FAQ questions rendered as H3/H5/H6
  ("Is a Congo African Grey good for a beginner?"). Pre-existing outlier, `skills/cag-page-hardening.md` §1e-ter.
- **F5 — `sem-all-six-levels` H6=3** against a 5-per-level floor. Advisory on `/` by the
  breeder's 2026-09-09 exception; `final_page_audit` repeats it as `min_h6_5`.
- **F6 — `sem-section-opening-paragraph` count 5** — 4 FAQ wrappers and one H3→H4 hop with
  no lead paragraph.
- **F7 — `schema-single-product-offer` count 2** — Congo and Timneh Products carry Offers
  outside an ItemList.
- **F8 — `css-class-resolves` count 20** — classes on rendered elements matching no rule:
  `font-display` ×28, `text-ink` ×25, `cag-glow` ×11, `bg-warm` ×8, `bird-item` ×6,
  `doc-check` ×6, `cag-warm-shadow` ×5, `cag-warm-shadow-lg` ×4, `mobile-section` ×3, …
  This is the dead-token family (`reference_dead_design_system_tokens`), and CSS is
  `quality_report` §3's worst family at 111 rows sitewide.
- **F9 — `css-no-dead-component-rule` count 6** — `.scam-compare`, `.pricing-track`,
  `.pricing-track >`, `.cag-fab.visible`, `.cag-sheet-scrim.open`, `.cag-sheet.open`.
  The last three are state classes JS adds at runtime; triage before deleting.
- **F10 — `css-component-color-not-overridden` count 1** — `.inq-subtext` wants
  `rgb(90,82,72)`; `body.theme-d h2 + p:not(…)` wins with `rgb(32,…)`.
- **F11 — `final_page_audit` WARN `house_method`** and **`aeo_audit` WARN "no brand-owned
  method name"** are the same finding, and it is **confirmed**:
  `grep -c "Benjamin Home-Raising Protocol\|Midland Socialization Method" dist/index.html` → **0**.
  Neither brand-owned method label appears on the homepage (CLAUDE.md rule 12).
- **F12 — bird cards are not height-uniform** at 375/768/1280 (Δ40 / Δ62 / Δ19px).
- **F13 — homepage in 24 dup-header crossover rows** — all shared-component headers
  ("adopt an african grey — inquiry form", "on this page", "airport pickup", "home
  delivery", "current pricing", "why apply with us?") and PAA-style FAQ questions
  ("do african grey parrots really talk?", "how much does an african grey parrot cost?").
  Component boilerplate + FAQ questions; the homepage is not in the DUP family for the
  home profile.
- **F14 — evidence_audit 8 WARN / 0 ERROR** — 6 `proof object NOT FETCHED`
  (usda-awa ×5, cites-docs ×4, dna-sexing ×16, avian-vet-cert ×17, pbfd-apv-pcr ×22,
  hatch-band ×14) + 2 statement-label PROXY (`#available-birds`, `#blog`). Breeder-accepted;
  proof docs pending.
- **F15 — `/blog/` carries the site's only AEO ERROR** ("no dateModified in JSON-LD").
  Not the homepage; noted so it is not lost.

### What remains before `/` is closed

1. a11y — 7 real rows (clay/green `✓`/`!`/`5` glyphs at 3.22–3.38:1). Triage.
2. Hero measures 649px at 1280, over the 350–400 band — Part D.
3. `sem-title-case-headings` 29 — FAQ questions as headings; pre-existing outlier.
4. `sem-all-six-levels` H6=3 — advisory by the breeder's 2026-09-09 exception.
5. Two SplitFeature srcset ladders the plan cannot reach (no defect, missed bytes).
6. srcset toolchain traps (`plan.mjs`/`verify.mjs`/`map.mjs`) — logged, not fixed.
7. **New:** H1/H2/H3 harness defects above — `page_hardening_scan` cannot be scoped to
   the homepage and does not terminate; `aeo_audit` cannot reach `/` by slug;
   `dup_content_audit` labels `/` as `dist`.
8. **New:** neither brand-owned method label appears on `/` (F11).
9. **New:** bird cards are not height-uniform (F12).

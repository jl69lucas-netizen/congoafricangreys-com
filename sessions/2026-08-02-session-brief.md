# Session brief — 2026-08-02 — Quality Loop Phase 3 + Phase 4

Executed `docs/superpowers/plans/2026-08-02-quality-loop-phase-3-4-plan.md` cold, as
written. The plan's own status table now sits at the top of that file; this brief is the
working record.

## The measured result

`npm run test:render:pages`, 15 pages x 3 viewports, harness 2.0.0: **45 passed (12.7m)**
— every page clears all six blocking checks.

| Check | rows | instances |
|---|---:|---:|
| css-class-resolves | 45 | 186 |
| css-no-dead-component-rule | 33 | 147 |
| img-srcset-within-2x *(overridden)* | 28 | 146 |
| dup-no-sibling-crossover | 24 | 216 |
| sem-section-opening-paragraph | 21 | 54 |
| sem-title-case-headings | 18 | 393 |
| css-component-color-not-overridden | 12 | 21 |
| sem-all-six-levels | 6 | 18 |
| schema-single-product-offer | 3 | 18 |
| **TOTAL** | **190** | **1,199** |

**LAYOUT and NAV report ZERO rows on all 15 pages.** That is what made promoting them to
blocking safe, and it is the whole point of Task 0b: before today the harness had one
blocking check, overridden everywhere.

Every row above belongs to a family that entered TODAY and is `advisory`. They are a
backlog, not a regression — and each one has already been interrogated once (see below).
Three findings worth naming:

- **`schema-single-product-offer` on `/african-grey-parrot-adoption-cost/`** — six offered
  Products outside an `ItemList`. Either they belong in one or the page is advertising six
  separate offers. This is the SCHEMA family earning its place on its first run.
- **`sem-title-case-headings`, 393 instances** — the known ~1,099-heading backlog, now
  measured rather than asserted.
- **`css-class-resolves`** now names 1-5 genuine orphans per page (`mobile-section`,
  `text-clay-text` x47 on roys, `counter-snippet`, `key-takeaway-v2`, `cmpe`) — the same
  defect class as the adoption-cost page putting FAQ text in `.faqC-x`, a 16x16 icon box.

## What shipped

**Phase 3 — four new invariant families.** `tests/render/` went from 7 checks in 3
families to **19 in 7**. Every one carries a `known_good` and a `known_broken` fixture,
a `minExamined` floor, and a row in `data/quality/rule-index.json`.

| Family | Checks |
|---|---|
| SEM | heading-order · all-six-levels · title-case-headings · section-opening-paragraph |
| SCHEMA | single-product-offer · sold-not-instock · date-modified-present · no-visible-date |
| CSS | class-resolves · no-dead-component-rule · component-color-not-overridden |
| DUP | no-sibling-crossover |

Meta gate: **124 → 196 tests**, green.

**Task 0b — the harness now actually blocks.** The six Phase-1/2 advisory checks are
`blocking`. Before this the harness had exactly one blocking check and an override
silencing it on all 15 pages, so Layer 1 blocked nothing at all.

**`CheckContext`** was added to the check signature — `pageType`, `slug`, `siblings()`.
SCHEMA genuinely needs page type (a bird page must carry exactly one `Product`/`Offer`; a
hub legitimately carries an `ItemList` of many) and DUP needs the sibling set. Fixtures
are judged under the **strictest** page type so a check cannot pass its fixtures through
a branch it never takes on a real page.

**DUP does not fork the whitelist.** It reads `WHITELIST_SNIPPETS` out of
`scripts/dup_content_audit.py` at run time and asserts a floor on how many entries it
parsed, because a silently-empty whitelist would report every mandated line as a defect
on every page at once. Shingling is local, so the meta gate has a real corpus
(`tests/render/fixtures/dup_corpus/`) to fire against rather than a mock.

**Phase 4 — `CLAUDE.md` 87,952 → 8,604 chars** (441 → 146 lines). Rules moved
**verbatim** into nine `rules/*.md` packs with `enforced: test | judgment | untested`
front-matter; the agent/skill/script registries into
`docs/reference/system-registry.md`; quick-start into `docs/reference/quick-start.md`;
history and known issues into `docs/reference/session-log.md`. Verified: all 28 rules
survived the move, none lost.

Registering the 15 previously-unregistered rules as `untested` made
`scripts/quality_report.py` §5 honest — it had been printing "none" only because those
rules were never in the index. It now names all 15. **That list is the Phase-5 backlog:
each one earns a test or gets deleted.**

**Task 5 — memory re-keyed** to the seven families in `MEMORY.md`, as an additional axis
alongside the existing topic groups.

## Six harness defects found, zero pages edited for them

The ratio the learning loop predicts. Each was interrogated before being believed.

1. **`layout-tap-target-size` flagged 12 label-wrapped controls per page.** 13×13
   checkboxes and radios inside `<label>`s between 86×47 and 341×62. The label *is* the
   target. "Enlarge the checkbox" would have been a design change bought for zero
   accessibility gain.
2. **…and 6 isolated card-title links per page**, which SC 2.5.8's **spacing exception**
   covers explicitly. Both exemptions are now implemented and each is pinned
   independently — an earlier fixture passed with the label rule *deleted*, because
   spacing was silently covering that case too.
3. **Two CSS checks reported a clean pass having examined ZERO rules.**
   `rule.cssRules` is truthy on every `CSSStyleRule` in current Chromium (nested CSS gave
   plain rules an empty `CSSRuleList`), so `if (rule.cssRules) { recurse; continue; }`
   skipped every rule in the document. Caught by `minExamined`, which is what that floor
   is for.
4. **`css-class-resolves` refused on every page of the site.** Its cross-origin branch
   fired on `fonts.googleapis.com` — a sheet of `@font-face` with no class selectors —
   so the check never judged anything anywhere. A blanket refusal that always fires is
   indistinguishable from a check that does not exist.
5. **`css-no-dead-component-rule` reported JS-toggled state variants as dead**
   (`.cag-fab.visible`, `.nav-dropdown-btn[aria-expanded="true"] + .nav-dropdown`), and
   **`css-component-color-not-overridden` flagged Tailwind utilities** that Direction D
   deliberately restyles.
6. **`css-class-resolves` was blind to CSS-ESCAPED class tokens.** Tailwind writes
   `.hover\:text-clay:hover`, `.text-white\/80`, `.gap-0\.5`, so a tokeniser that stops
   at the backslash captures `gap-0` and reports every element carrying `gap-0.5` as
   unstyled — 45 of the CSS family's 90 rows, all 15 pages, every named orphan a class
   that IS styled. Eggs page: 58 orphans -> 1.

**Five of the six fired on EVERY page of the site.** That uniformity is the reliable tell,
and it is now the first thing to check when a new family arrives with a large number.

Plus one that would have been worse than a false report: **`sem-section-opening-paragraph`
hung the page run.** It tested visibility inside its forward scan, so every heading
re-tested every following element with a `getClientRects()` layout flush each time —
O(n²) forced reflows on a 96-heading page. It blocked the renderer past the 120s
per-test timeout and the run sat on one page for 20+ minutes. **Playwright's per-test
timeout does not save you from a synchronous `page.evaluate` that blocks the renderer.**
Precomputing in one pass: hung → **82 ms**.

## Two real page defects, both surfaced by the harness

- `/african-grey-parrot-for-sale-florida/` had **two broken images** — `<img>` tags still
  pointing at `https://congoafricangreys.com/wp-content/uploads/…`, a path that now 301s
  to the homepage and serves HTML. Replaced with local WebP at measured sizes.
- `/blog/african-grey-parrot-cage-setup/` — all 11 in-page links landed at 96px behind
  159px of pinned chrome. Same defect class as `f401cae`, one page further on.

## Task 0a — partial, and the scope was wrong in the plan

The plan assumed the remaining srcset work was regenerating oversized masters. It is not.
`scripts/image_srcset_plan.mjs` (new) measures every `<img>` **per occurrence** across a
sweep that straddles every Tailwind breakpoint, classifies each band FIXED or FLUID, and
verifies its own plan before a file is cut.

**290 occurrences over 2.0×. Three are constant-painted. 287 are FLUID** and need
per-role `srcset` + measured `sizes`. Generating variants is scriptable; patching `sizes`
per occurrence is not, because several of these images render from data arrays inside
shared components. The override is therefore **narrowed and re-stated from a
measurement**, not cleared. Full plan, derived `sizes` per role, and the traps banked
from the reverted blanket-`sizes` attempt: `docs/reference/technical-seo-fixes-backlog.md`.

## Task 3 — deliberately not started

Its own precondition is "only after the replacements are **blocking**". SEM/SCHEMA/CSS/DUP
entered `advisory` per the promotion rule. Retiring static checks on a fixture-level
argument alone would be the shortcut this repo's rules exist to prevent.

## Open Flags

- **Next session, in order:** (1) re-run `npm run test:render:pages` on the current
  harness and promote SEM/SCHEMA/CSS/DUP if the cluster is clean; (2) Task 3 retirements
  with the re-inject → FAIL → remove → PASS proof per check; (3) the 287 fluid image
  occurrences.
- **DUP's whitelist has a real gap.** Its first findings are dominated by text CLAUDE.md
  already names as mandated-identical — inquiry-form labels and real reviews — which the
  Python whitelist's stems do not match in their *rendered* phrasing. Widening it
  requires the gate-integrity proof procedure; do not widen it casually.
- **`sem-title-case-headings` confirms the known backlog** of ~1,099 sentence-case
  headings. It is now measured rather than asserted.

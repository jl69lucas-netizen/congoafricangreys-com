# Self-Improving Quality Loop — Phase 3 + Phase 4 Execution Plan

> ## STATUS AFTER THE SECOND 2026-08-02 SESSION — read this first
>
> | Task | State |
> |---|---|
> | promote SEM/SCHEMA/CSS/DUP | **4 of 12 promoted.** `sem-heading-order`, `schema-date-modified-present`, `schema-no-visible-date`, `schema-sold-not-instock` are `blocking`. The other 8 stay advisory with `severity` + `why_advisory` now recorded per rule. |
> | 3  retire the superseded static checks | **NOT DONE — and 6 of 8 are still blocked by the plan's own precondition.** The other 2 hit a coverage problem this plan does not model. See below. |
> | 0a  the 287 fluid srcset occurrences | **UNCHANGED.** Still the largest single piece of open work. |
>
> **The session's real finding was a flaky BLOCKING check.** `nav-jump-target-lands`
> returned different verdicts across three runs of the SAME commit against the SAME
> `dist/` — adoption-cost@375, then timneh@375 + hand-raised@768. Two distinct bugs: a
> settle probe that could not tell an UNSTARTED scroll from a FINISHED one (it reported a
> target at its raw 26,059px document offset, i.e. the page never moved), and then a gate
> failing on a verdict whose own message says *"PROBABLY A BUDGET DEFECT, NOT A PAGE
> DEFECT"*. Both fixed in the harness; **zero pages were edited.** Full write-up, and the
> new `known_broken/scroll-late-start.html` fixture proved to fail without the fix, in
> `docs/reference/technical-seo-fixes-backlog.md`.
>
> **The tell was not a high count.** Every individual number looked plausible; what
> exposed it was the same input producing different verdicts. Add that to §3's trap list:
> a gate whose result changes between runs is broken even when its numbers look sane.
>
> **Task 3's table needs a third column — page coverage.** `page_hardening_scan.py`
> defaults to all **108** built pages; the render harness runs **15**. Retiring a static
> check trades 108-page enforcement for 15-page enforcement, leaving 93 pages uncovered
> for that invariant. Sampled to confirm: three non-target comparison pages return 29
> ERROR · 30 WARN. Recommendation: retire nothing until the harness covers those pages or
> the retirement is scoped to the 15; the trade-off of waiting is the running triage cost
> of the static checks' known false positives.
>
> **`npm run test:render:pages` cannot pass as written** — `RENDER_OVERRIDE` is a shell
> env var the npm script never sets, so the documented gate command fails 28
> page-viewports and the recorded baseline is not reproducible from the repo alone. The
> reproducing command is in the backlog.
>
> ---
>
> ## STATUS AFTER THE FIRST 2026-08-02 SESSION
>
> | Task | State |
> |---|---|
> | 0a  clear the srcset override | **PARTIAL.** Override narrowed and re-stated from a measurement, not cleared. |
> | 0b  promote the 6 advisory checks | **DONE.** All six are `blocking`. |
> | 1   SEM + SCHEMA families | **DONE.** 8 checks, both fixtures each. |
> | 2   CSS + DUP families | **DONE.** 4 checks, both fixtures each. DUP wraps the tuned whitelist rather than forking it. |
> | 3   retire the superseded static checks | **NOT STARTED** — deliberately. See below. |
> | 4   `rules/` packs + the CLAUDE.md cut | **DONE.** 87,952 -> 8,604 chars. |
> | 5   memory re-key to the seven families | **DONE.** |
>
> **Task 0a — what actually happened.** The plan assumed the remaining work was
> regenerating oversized masters. It is not. `scripts/image_srcset_plan.mjs` (new)
> measured every `<img>` on all 15 target pages **per occurrence** across a sweep that
> straddles every Tailwind breakpoint: **290 occurrences over 2.0x, of which 3 are
> constant-painted and 287 are FLUID** and need per-role `srcset` + measured `sizes`.
> Generating variants is scriptable; patching `sizes` per occurrence is not, because
> several of these images render from data arrays inside shared components. That is the
> next session's work and it is the whole of it — the measured plan, the derived `sizes`
> per role, and the traps are in `docs/reference/technical-seo-fixes-backlog.md`.
> Two genuinely BROKEN images were found and fixed on the Florida page in the process.
>
> **Task 3 — why it was not started.** The plan's own precondition is "only after the
> replacements are **blocking**". SEM/SCHEMA/CSS/DUP entered as `advisory`, per the
> promotion rule (fixtures passed AND zero false reports across one full cluster). The
> cluster run that would earn their promotion is the first thing to do next session; the
> retirements follow it, each with the re-inject -> confirm FAIL -> remove -> confirm PASS
> proof. Retiring on a fixture-level argument alone would be the shortcut this repo's
> rules exist to prevent.
>
> **Corrections to this plan's own assumptions**, recorded so they are not re-derived:
> - §4c says `scripts/quality_report.py` "flags any rule present in both" CLAUDE.md and
>   the agents. **It does not** — no such check exists. The two-copy problem is instead
>   recorded in `rules/README.md` with the injector -> pack table.
> - §0's "33+ assets" was a filename count and implied the wrong fix. See above.
> - Task 0b listed `layout-tap-target-size` as "still emits 15 rows/page". It was
>   emitting them for two reasons WCAG itself exempts (label-wrapped controls, isolated
>   small targets). Both are now implemented and the check was promoted.
>
> **Five harness defects were found and fixed this session, and zero pages were edited
> for any of them** — the ratio the learning loop predicts. They are listed in the commit
> messages of ffc2c2b, 5839b51 and 8c3db65.

**Written:** 2026-08-01 (end of session), for the NEXT session to start from cold.
**Spec:** `docs/superpowers/specs/2026-07-31-self-improving-quality-loop-design.md`
**Status of the spec as of 2026-08-01:** Phases 1 and 2 **DONE and green**. Phases 3 and 4 **NOT STARTED**.

> **Start here. No planning, no re-audit, no brainstorming.** The audit is already done and
> recorded in §0 below. Open Task 0 and begin. Every task carries its own acceptance
> command; a task is done when that command prints what the task says it prints.

---

## 0. Verified state at hand-off (measured 2026-08-01, do not re-derive)

| Thing | State |
|---|---|
| `npm run test:render:meta` | **124 passed / 20 skipped / 45.6s** — green |
| Checks registered | **7** — IMG×2, LAYOUT×3, NAV×2 |
| Blocking checks | **1** (`img-srcset-within-2x`); the other 6 are still `advisory` |
| Open overrides | **1** — `img-srcset-within-2x`, silencing all 15 page-runs |
| Scorecards | 25 files in `data/quality/scorecards/` (2026-07-31 baselines + 2026-08-01 re-score) |
| Rework rate | 22.8% (30-day, 2026-07-02→08-01), down 2.0 pts from the 24.8% baseline |
| First-run defects/page | 3–7 rows (target <4) |
| `rules/` directory | **does not exist** |
| `CLAUDE.md` | **87,952 chars / 441 lines** — grew ~3k from the 84,913 baseline. Target <12,000 |
| Memory | 152 files, `MEMORY.md` topic-grouped, **no seven-family index** |
| `data/quality/rule-index.json` | 19 rules — 7 `test`, 12 `judgment` (exactly the spec's capped 12) |

**The gating fact:** the harness's only blocking check is overridden on every page, so
Layer 1 currently blocks nothing. Task 0 fixes that, and the spec forbids Phase 4 until
Phase 1 is genuinely blocking.

---

## 1. Task order (sequential — each unblocks the next)

```
Task 0  Make the harness actually block      → prerequisite for Phase 4
Task 1  Phase 3 families: SEM, SCHEMA        → cheap, static-adjacent, high rule coverage
Task 2  Phase 3 families: CSS, DUP           → harder, needs cross-page state
Task 3  Retire the superseded static checks  → only after 1+2 are blocking
Task 4  Phase 4: rules/ packs + CLAUDE.md cut
Task 5  Phase 4: memory re-key to the seven families
```

---

## Task 0 — Make the harness actually block

Two sub-items. Both must land before Phase 4 starts.

### 0a. Clear the srcset override

The override reason names the cause: 33+ assets decode above 2× their painted width,
worst 13.3×. Regen queue lives in `docs/reference/technical-seo-fixes-backlog.md`.

**Read the backlog's image section FIRST** — it records a REVERTED srcset attempt and the
four reasons it failed. The trap: one blanket `sizes` value conflated gallery cells (~45vw)
with full-width feature images (~92vw), so the browser loaded a 168px file into a 343px box.
**Shipping blur to satisfy a byte metric is a bad trade — per-context `sizes`, not one value.**

Done when:
```bash
npm run test:render:pages && python3 scripts/quality_report.py
```
prints `4. OPEN OVERRIDES (0 distinct...)` — or the remaining override names a *different*,
newly-discovered cause with its own backlog entry.

### 0b. Promote the 6 advisory checks to blocking

Spec §3.1.1: a check is promoted once it has passed its fixtures **and produced zero false
reports across one full cluster.** That evidence now exists — the 2026-08-01 sweep re-scored
15 pages and every finding was charged to the harness, none to the pages.

Promote in `tests/render/checks/*.ts` by flipping `severity: 'advisory'` → `'blocking'`:

| Check | File | Note before flipping |
|---|---|---|
| `img-alt-present-and-unique` | `checks/img.ts` | safe |
| `layout-no-horizontal-overflow` | `checks/layout.ts` | safe |
| `layout-min-font-size` | `checks/layout.ts` | corpus is at ZERO rows — safe |
| `layout-tap-target-size` | `checks/layout.ts` | **still emits 15 rows/page.** Either fix the pages or keep advisory with a written reason in `rule-index.json` |
| `nav-anchors-resolve` | `checks/nav.ts` | safe |
| `nav-jump-target-lands` | `checks/nav.ts` | safe |

Done when: `npm run test:render:meta` is green, `npm run test:render:pages` passes without a
new override, and `rule-index.json` records any check deliberately left advisory **with the
reason written in the rule row**.

---

## Task 1 — Phase 3, part A: `SEM` and `SCHEMA` families

New files: `tests/render/checks/sem.ts`, `tests/render/checks/schema.ts`.
Register both in `tests/render/checks/index.ts`.
Add `"SEM"`, `"SCHEMA"` to every page type in `tests/render/targets.json` →
`families_by_page_type`.

### SEM checks (spec §3.1.1, all four already exist as CLAUDE.md rules with no test)

| id | asserts | minExamined |
|---|---|---|
| `sem-heading-order` | H1–H6 descend with no skipped level (H3→H6 and H2→H4 are FAIL; stepping back up is fine) | 6 |
| `sem-all-six-levels` | all six levels present, **≥5 H5 AND ≥5 H6** | 6 |
| `sem-title-case-headings` | every H1–H6 in AP Title Case. **`<summary>` FAQ questions are NOT headings — exempt.** Port the caser from `scripts/page_hardening_scan.py` (`header-not-title-case`) rather than rewriting it | 5 |
| `sem-section-opening-paragraph` | every section carries an opening paragraph before its first sub-element | 3 |

### SCHEMA checks

| id | asserts | minExamined |
|---|---|---|
| `schema-single-product-offer` | exactly one `Product`/`Offer` where the page type requires it (bird pages); pair pages use `AggregateOffer` | 1 |
| `schema-sold-not-instock` | no listing with `sold` status carries `InStock` | 1 |
| `schema-date-modified-present` | `dateModified` present in JSON-LD | 1 |
| `schema-no-visible-date` | **no visible date anywhere in rendered text** — the reason this belongs in the render harness and not a source grep | 1 |

**Trap already banked:** nested/list `@type` and inline JSON-LD strings produce false
positives — `skills/manual-auditor-check.md` records all four. Strip inline JSON-LD from the
*text* pass before asserting `schema-no-visible-date`, or it will flag its own schema.

### Acceptance for Task 1
Every new check needs `fixtures/known_good/<id>.html` **and** `fixtures/known_broken/<id>.html`
before `meta.spec.ts` will accept it. Then:
```bash
npm run test:render:meta      # every new check fires on broken, silent on good, hits minExamined
npm run test:render:pages     # 15 pages re-scored
python3 scripts/quality_report.py
```
Add each new check to `data/quality/rule-index.json` as `enforced: test` with its `test:` path.
New checks enter as `advisory`; promote per Task 0b's rule.

---

## Task 2 — Phase 3, part B: `CSS` and `DUP` families

Harder than Task 1: both need state beyond a single painted page.

### CSS checks (`tests/render/checks/css.ts`)

| id | asserts |
|---|---|
| `css-class-resolves` | every class in markup resolves to ≥1 rule or is explicitly inert |
| `css-no-dead-component-rule` | every declared component class has markup behind it |
| `css-component-color-not-overridden` | a component's colour is not overridden by a descendant rule |

`scripts/page_hardening_scan.py` already implements the static half as
`markup-css-drift`, `markup-css-orphan`, `component-color-loses-to-descendant`.
**Port the logic, do not re-invent it** — the render version wins because it reads computed
style instead of guessing from the stylesheet.

### DUP check (`tests/render/checks/dup.ts`)

`dup-no-sibling-crossover` — zero non-whitelist crossover against every sibling in the cluster.
This is **not per-page**; it needs the sibling set. Two options, pick one and say why:
- **(Recommended)** wrap `scripts/dup_content_audit.py` and assert on its exit — reuses the
  12-word shingle logic, the `--headers` mode, and the whitelist that already exists.
  *Trade-off:* the check shells out, so it is slower and its failure messages come from Python.
- Reimplement shingling in TS — self-contained, but forks a whitelist that has already been
  tuned once and will drift.

### Acceptance for Task 2
Same as Task 1. `MAX_DEFECT_ROWS = 3` — a check wanting a fourth row is asking to report
*instances*, and instances go in `count`. This is enforced at the call site in
`tests/render/lib/runCheck.ts`; violating it fails the meta gate.

---

## Task 3 — Retire the superseded static checks

Only after the replacements are **blocking**. Candidates in `scripts/page_hardening_scan.py`:

| Static check | Superseded by |
|---|---|
| `img-no-srcset`, `hero-preload-srcset-drift` | `img-srcset-within-2x` (measures the chosen candidate, not its presence) |
| `tap-target-spacing` | `layout-tap-target-size` |
| `smooth-scroll-breaks-anchors` | `nav-jump-target-lands` |
| `header-not-title-case` | `sem-title-case-headings` |
| `markup-css-drift`, `markup-css-orphan`, `component-color-loses-to-descendant` | the CSS family |

**Do NOT retire:** `clay-small-text-contrast`, `opacity-dims-text-contrast`,
`links-colour-only`, `escaped-svg`, `svg-in-css-content`, `css-math-spacing`,
`user-select-none`, `form-control-ios-zoom`, `analytics-double-load`,
`font-family-loaded-unused`, `absolute-hero-not-unwound`, `infographic-cropped-mobile`,
`bottom-bar-under-tabbar`, `deflist-label-not-differentiated`, `icon-text-baseline-drift` —
no harness family covers them.

**Per-check retirement proof (from `skills/cag-gate-integrity.md`, non-negotiable):**
re-inject the real defect → confirm the *new* check FAILs → remove it → confirm PASS →
confirm the diff is empty. Then delete the static check and its row in
`tests/test_page_hardening_new_checks.py`.

---

## Task 4 — Phase 4: `rules/` packs and the CLAUDE.md cut

**Migration rule (binding): a rule may leave `CLAUDE.md` only once its test exists.**
After Tasks 1–3 that is ~18 rules instead of today's 7.

### 4a. Create the packs
```
rules/for-sale.md   rules/bird.md      rules/comparison.md
rules/interior.md   rules/location.md  rules/blog.md
rules/images.md     rules/headings.md  rules/schema.md
```
Every rule carries front-matter:
```yaml
id: img-srcset-within-2x
enforced: test
test: tests/render/checks/img.ts::img-srcset-within-2x
family: IMG
```

### 4b. Cut CLAUDE.md to ~150 lines / <12,000 chars
Keep only: identity, paths, deploy model; the **12 `enforced: judgment` rules** already
enumerated in `data/quality/rule-index.json`; a page-type → rule-pack router; and the
explicit pointer *"the pixel rules are enforced by `tests/render/`, not by this file."*

**The 12 judgment rules that STAY** (verbatim from `rule-index.json`, do not re-litigate):
first-person-brand-voice · cites-appendix-i-framing · work-on-main-not-branches ·
always-push-after-build · recommend-plus-why · restate-the-brief · preview-before-apply ·
confidence-gate-97 · write-from-outline-never-from-sibling · no-fabricated-claims ·
verified-claim-ledger · brand-owned-method-labels.

### 4c. The injector problem — do not skip
The five `scripts/add_*_rule.py` injectors write rule text into all 68 agent Golden Rules.
Moving a rule out of `CLAUDE.md` does **not** remove it from the agents. Decide per rule:
re-point the injector at the pack, or leave the agent text and delete only the core copy.
`scripts/quality_report.py` flags any rule present in both — check it after every move.

### Acceptance for Task 4
```bash
wc -c CLAUDE.md                      # < 12,000
python3 scripts/quality_report.py    # §5 prints "none" — no rule without a test or judgment class
bash scripts/health-sweep.sh
```

---

## Task 5 — Phase 4: re-key memory to the seven families

152 files in `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/`.
Add a **family index** to `MEMORY.md` — IMG / LAYOUT / NAV / CSS / SEM / SCHEMA / DUP —
so recall vocabulary matches the harness vocabulary. Existing topic groups stay; the family
index is an additional axis, not a replacement. Merge duplicates while passing through.

Done when `MEMORY.md` carries all seven family headings and every render-defect memory
appears under one.

---

## 2. Success criteria — where the numbers must land

| Measure | Baseline | Target | 2026-08-01 |
|---|---|---|---|
| Rework rate, 30-day | 24.8% | **<15% at 90 days** | 22.8% |
| First-run defects per page | 13 | **<4** | 3–7 rows |
| Blocking checks with both fixtures | 0 of 0 | **100%** | 1 of 1 (only 1 blocking) |
| Gate false reports per cluster | 12 historical | **0** | 0 escaped |
| `CLAUDE.md` size | 84,913 | **<12,000** | 87,952 |
| Rules with no test and no judgment class | ~20 | **0** | 0 |

---

## 3. Traps already paid for — read before writing any check

1. **Verify the gate before you fix the page.** Twelve checkers have cried wolf here. A gate's
   output is a hypothesis. `skills/cag-gate-integrity.md`.
2. **A suspiciously high finding count means a broken check, not a broken page.** 418 rows
   collapsed to 85 with zero page edits.
3. **Rows vs instances.** One row = one failure *mode* at one viewport; magnitude goes in
   `count`. Mixing them let NAV supply 81% of a headline number by aggregation style alone.
4. **Read a gate's own examined count before believing a PASS.** `PASS … in 0 pages` is not a
   pass. `minExamined` exists for exactly this.
5. **Measure in Playwright, never from a formula.** The Browser pane reports `vw:0`;
   `0.5em` over-reports a `ch` by ~20%.
6. **Charge escaped defects to the harness, not to a new rule.** `skills/cag-learning-loop.md`
   step 3 is the load-bearing one.
7. **`behavior:'instant'` ≠ `'auto'`** when resetting scroll, and Playwright loads a spec once
   per WORKER — module-level state is shared across tests in that worker.

---

## 4. First three commands of the next session

```bash
cd /Users/apple/Downloads/CAG && git checkout main && git pull
```
```bash
npm run test:render:meta && python3 scripts/quality_report.py
```
```bash
sed -n '/^## Render-harness baseline, 2026-08-01/,$p' docs/reference/technical-seo-fixes-backlog.md
```
(that last section carries the three named findings — `layout-min-font-size`, the 33
oversized images behind the override, and the `nav-jump-target-lands` remainder — plus the
reverted-srcset post-mortem.)

Then start Task 0a.

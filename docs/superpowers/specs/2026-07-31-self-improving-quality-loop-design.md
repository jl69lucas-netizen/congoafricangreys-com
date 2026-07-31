# Self-Improving Quality Loop — Design

**Date:** 2026-07-31
**Status:** Approved (breeder, 2026-07-31)
**Supersedes:** nothing. Sits underneath every existing builder skill and gate.
**Related:** `skills/cag-gate-integrity.md`, `skills/cag-final-page-pass.md`,
`skills/cag-page-hardening.md`, `docs/superpowers/sessions/2026-07-31-congo-pair-harden-lessons.md`

---

## 1. Problem

The CAG system is **open-loop**. Rules are written, injected into 68 agents by five
`add_*_rule.py` scripts, and then never scored. Nothing measures whether adding a rule
improved anything, and nothing fails when the system regresses.

Measured on this repository, 2026-07-31:

| Signal | Value |
|---|---|
| Commits, all time | 863 |
| Commits, 2026-05-01 → 2026-07-31 | 862 |
| **Rework commits in that window** | **214 (24.8%)** |
| Rework commits, looser all-time match | 275 of 863 (31.9%) |
| `CLAUDE.md` | 84,913 chars / 437 lines ≈ 21,000 tokens loaded per session |
| Memory files | 149 |
| Skills / agents | 63 / 68 |
| Lessons docs | 7 files, 1,068 lines |
| Tests | 5 files, 90 cases — **all testing scripts, none testing page output** |
| Recorded incidents of a gate reporting a defect that did not exist | 12 |
| Rework commits mentioning a broken gate/probe/scan | 18 |

**Canonical rework-rate definition** (reproducible, used for every future measurement):

```bash
git log --since=<FROM> --until=<TO> --pretty=format:"%s" \
  | grep -icE "^(fix|revert)|fix\(|correct|restore|regress|undo|repair|patch\("
```
divided by total commits in the same window.

### Where rework concentrates

Over the 214 rework commits (categories overlap — one commit can match several):

| Domain | Commits | Share |
|---|---:|---:|
| Images (srcset, crop, alt, infographic, weight) | 55 | 26% |
| Mobile / responsive (overflow, stacking, breakpoints) | 41 | 19% |
| Links / rails / nav (jump rails, anchors, breadcrumbs) | 35 | 16% |
| CSS + token drift (dead rules, classes with no markup) | 19 | 9% |
| Gates that lied | 18 | 8% |
| Schema / canonical / dates | 18 | 8% |
| Headings / outline / title case | 17 | 8% |
| Duplicate content | 15 | 7% |
| Contrast / a11y | 14 | 7% |
| Copy / voice / typos | 8 | 4% |

Images + mobile + links + CSS drift = **150 of 214 (70%)**. Every one of those is a
**rendered-state** defect: it exists in the painted page, not in the source. The current
gates (`page_hardening_scan.py`, `final_page_audit.py`, `seam_parity.py`, `aeo_audit.py`,
`dup_content_audit.py`) read HTML as text.

The congo-pair build is the proof: `page_hardening_scan.py` returned `0 ERROR · 0 WARN`
and `seam_parity.py` returned `PASS 24/23` on a page carrying **13 real defects**, every
one of which was found only by a runtime probe.

### Root cause

**The rules are checked against source. The defects live in pixels.** Rule #31 cannot
move a number produced by that mismatch. A rendered-state acceptance harness can.

The secondary cause is that a "rule" in this system is prose with no executable
counterpart, so it can be forgotten, mis-scoped, or silently contradicted — and a gate
built to check it can be wrong in either direction without anyone noticing (12 recorded
false reports, 2 gates that reported PASS having examined zero pages).

---

## 2. Decisions

Three forks were resolved by the breeder on 2026-07-31:

1. **Metric:** rework rate. Baseline 24.8%, target under 15% at 90 days.
2. **Enforcement:** blocking, **and** test-first rules — a page is not "done" until the
   render suite passes at 375/768/1280, and **no new rule may be added without a failing
   test committed first.**
3. **Context:** thin core `CLAUDE.md` + task-scoped rule packs, migration gated on the
   rule's test existing.

---

## 3. Architecture

Four layers. Each closes a loop the current system leaves open.

```
Layer 1  Harness         measures the painted page, blocks "done"
Layer 2  Ledger          turns measurements into a trend + a next-action list
Layer 3  Promotion Path  the only legal way a lesson becomes a rule
Layer 4  Context         thin core + packs, safe because Layer 1 backstops it
```

### 3.1 Layer 1 — The Harness

**Runner:** `@playwright/test` (Playwright 1.60.0 is already installed; no new
dependency). The existing pytest suite (`tests/*.py`, 90 cases) stays as-is for
script-level unit tests. Playwright is chosen over python-playwright because
python-playwright and bs4 are not installed, and because `@playwright/test` gives
viewport projects, parallelism, and a JSON reporter that feeds Layer 2 directly.

**Layout:**

```
tests/render/
  playwright.config.ts      # projects vp375 / vp768 / vp1280; webServer serves dist/
  targets.json              # slug -> page_type -> which families apply
  lib/
    registry.ts             # every check declares: id, family, fixtures, severity
    probes.ts               # shared measurement helpers
  checks/
    img.spec.ts
    layout.spec.ts
    nav.spec.ts
    css.spec.ts
    sem.spec.ts
    schema.spec.ts
    dup.spec.ts
  fixtures/
    known_good/<check-id>.html
    known_broken/<check-id>.html
  meta.spec.ts              # the gate-integrity gate (see 3.1.2)
```

The static server is `python3 -m http.server` pointed at `dist/`, declared in
`playwright.config.ts` under `webServer` — no new tooling.

#### 3.1.1 Invariant families

Each family is derived from real rework events in the log, not from theory.

| Family | Asserts | Evidence |
|---|---|---|
| `IMG` | every in-body image's chosen srcset candidate is within 1×–2× of its rendered CSS width; no image renders above 2× intrinsic; alt text non-empty and unique within the page; decorative images carry `alt=""` | 55 commits; "the hero sizes lie"; 2.13× hero waste |
| `LAYOUT` | `documentElement.scrollWidth ≤ clientWidth + 1` at each viewport; no element exceeds its container's box; card/geo grids do not collapse to one column unintentionally; zero text nodes rendering below 12.5px; tap targets ≥24px with ≥8px spacing | 41 commits; "two horizontal-overflow bugs on every page"; "108 sub-12.5px nodes" |
| `NAV` | every jump-rail chip is **clicked**, and its target heading must settle between `header + rail` and `+60px`; every in-page `#anchor` resolves to an element; no dead internal links | 35 commits; measured failure "click a chip, wait 1.2s, `scrollY` is still 25" |
| `CSS` | every class present in markup resolves to at least one rule or is explicitly inert; every declared component class has markup behind it (dead-rule detection); a component's colour is not overridden by a descendant rule | 19 commits; "50 dead rules"; "form rewired to the classes it was styled for" |
| `SEM` | heading levels descend sequentially with no skips; ≥5 H5 and ≥5 H6; all H1–H6 in AP Title Case; every section carries an opening paragraph | 17 commits |
| `SCHEMA` | single `Product`/`Offer` where the page type requires it; sold listings are never `InStock`; `dateModified` present in JSON-LD; **no visible date anywhere in rendered text** | 18 commits |
| `DUP` | zero non-whitelist crossover against every sibling page in the cluster | 15 commits |

Severity is per check: `blocking` or `advisory`. Only `blocking` checks stop a build.
A check enters the codebase as `advisory` and is promoted to `blocking` once it has
passed its fixtures and produced zero false reports across one full cluster.

#### 3.1.2 `meta.spec.ts` — the gate-integrity gate

This is the mechanical answer to the 12 false reports and the 2 zero-page passes.

Every check registered in `lib/registry.ts` must declare two fixture paths. `meta.spec.ts`
asserts, for every registered check:

1. it **passes** on `fixtures/known_good/<check-id>.html`
2. it **fails** on `fixtures/known_broken/<check-id>.html`
3. it reports its own **examined count**, and a run with `examined == 0` is a **FAIL**,
   never a pass

A check that cannot demonstrate all three is refused `blocking` severity. This converts
`skills/cag-gate-integrity.md` from a paragraph asking for care into a control that runs.

`meta.spec.ts` runs first in the suite. If it fails, no page results are trusted.

#### 3.1.3 Escape hatch

A blocked build may proceed with `--override=<check-id>:<reason>`. The override is
**written into that page's scorecard**, so overrides are counted, not hidden, and appear
in the quality report as their own line. An override with no reason string is rejected.

### 3.2 Layer 2 — The Ledger

**Per-build scorecard** — written on the **first** harness run, before any fixing. This
is the leading indicator.

`data/quality/scorecards/<slug>-<YYYY-MM-DD>.json`
```json
{
  "slug": "congo-african-grey-parrot-pair-for-sale",
  "date": "2026-07-31",
  "page_type": "for-sale",
  "run": "first",
  "harness_version": "1.0.0",
  "viewports": [375, 768, 1280],
  "examined": { "pages": 1, "checks": 24 },
  "defects": { "IMG": 3, "LAYOUT": 7, "NAV": 2, "CSS": 1,
               "SEM": 0, "SCHEMA": 0, "DUP": 0 },
  "total": 13,
  "overrides": []
}
```

**Rework ledger** — computed from git, the lagging indicator.

`data/quality/rework-ledger.json`
```json
{
  "definition": "see spec §1 canonical command",
  "windows": [
    { "from": "2026-05-01", "to": "2026-07-31",
      "total": 862, "rework": 214, "rate": 0.248,
      "by_domain": { "IMG": 55, "LAYOUT": 41, "NAV": 35, "CSS": 19,
                     "GATE": 18, "SCHEMA": 18, "SEM": 17, "DUP": 15,
                     "A11Y": 14, "COPY": 8 } }
  ]
}
```

**`scripts/quality_report.py`** prints, in one screen:
- current rework rate + delta since the previous window
- first-run defects per page, by family, most recent 10 builds
- **which family produces the most first-run defects** — the sorted next-action list
- open overrides
- **rules in core with no backing test** (the deletion-candidate list, see §3.3)

**Benchmark corpus:** per-build scorecards on new work, **plus a frozen 7-page sample**
— one per page type (bird, for-sale, comparison, interior, location, blog, hub) — stored
in `tests/render/targets.json` under `corpus: true` and re-scored on demand, so the trend
line does not depend on which pages happened to be built that month.

### 3.3 Layer 3 — The Promotion Path

The rule that makes the system self-improving rather than merely instrumented:

> **A lesson becomes a rule only by this path: defect observed → failing test committed →
> fix applied → test passes → rule text written next to the test. No test, no rule.**

And its inverse, which does the work of keeping the system small:

> **A rule with no backing test is a deletion candidate.** Every quality report lists
> them. Either someone writes the test, or the rule is removed.

**Exemption class.** Some rules are genuinely untestable and must not be deleted. Each
rule is classed `enforced: test` or `enforced: judgment`. The `judgment` class is
enumerated and capped — currently ~12 (first-person voice, CITES framing, work-on-main,
push-after-build, Recommend+Why, restate-the-brief, preview-before-apply, confidence gate,
write-from-outline, no-fabricated-claims, verified-claim ledger, breeder-approved method
labels). Adding to the `judgment` class requires naming, in the rule itself, why a test
cannot exist. It is a cap, not a loophole.

**`skills/cag-learning-loop.md`** — new skill, runs at the end of every build (invoked by
`session-closer`, and standalone). Procedure:

1. Diff what was reworked during this session.
2. Classify each rework event into a family.
3. **If an existing invariant already covers it → the harness has a bug.** Fix the
   harness and add the missed case to `known_broken`. Do **not** write a new rule, and do
   **not** treat the page as the only problem.
4. If no invariant covers it → write the failing case first, confirm it fails, fix, confirm
   it passes, then write the rule text beside the test.
5. Append the event to the ledger.

Step 3 is the load-bearing one: it is the step that would have caught all 12 false reports
and the 13-defect clean scan, because it forces every escaped defect to be charged to the
harness rather than absorbed as a new paragraph.

### 3.4 Layer 4 — Context re-architecture

**`CLAUDE.md` → ~150 lines**, containing only:
- identity, paths, deploy model
- the ~12 `enforced: judgment` rules from §3.3
- a page-type → rule-pack router
- an explicit pointer: *the pixel rules are enforced by `tests/render/`, not by this file*

**`rules/` packs**, loaded on demand by page type:
`rules/for-sale.md`, `rules/bird.md`, `rules/comparison.md`, `rules/interior.md`,
`rules/location.md`, `rules/blog.md`, plus cross-cutting `rules/images.md`,
`rules/headings.md`, `rules/schema.md`.

Each rule carries front-matter:
```yaml
id: img-srcset-within-2x
enforced: test
test: tests/render/checks/img.spec.ts::srcset-within-2x
family: IMG
```

**Migration rule: a rule may leave `CLAUDE.md` only once its test exists.** This makes
the migration incremental and safe — a pack that fails to load cannot silently un-enforce
anything, because the blocking harness still catches it.

**Memory** (149 files) is re-keyed to the same seven-family taxonomy so recall matches the
harness vocabulary, and `MEMORY.md` gains a family index.

---

## 4. Phasing

| Phase | Deliverable | Covers |
|---|---|---|
| **1** | `playwright.config.ts`, `lib/registry.ts`, `meta.spec.ts` + fixtures, and the `IMG` / `LAYOUT` / `NAV` families. Baseline scorecards on the 8 for-sale cluster pages. | **70% of rework** |
| **2** | `data/quality/` ledger, `scripts/quality_report.py`, `skills/cag-learning-loop.md` (registered via `register_skills.py --copy`) | makes the loop self-improving |
| **3** | `CSS` / `SEM` / `SCHEMA` / `DUP` families; retire the overlapping static checks in `page_hardening_scan.py` that the harness now covers better | remaining 30% |
| **4** | `rules/` packs; `CLAUDE.md` reduction, rule by rule as tests land; memory re-key | the 21k-token per-session tax |

Phases are sequential. Phase 4 must not begin before Phase 1 is blocking, because the
harness is what makes moving rules out of core safe.

---

## 5. Success criteria

| Measure | Baseline | Target |
|---|---|---|
| Rework rate (canonical command, 30-day rolling) | **24.8%** (214/862, 2026-05-01→07-31) | **< 15% at 90 days** |
| First-run defects per page | **13** (congo-pair, 2026-07-31) | **< 4** |
| Blocking checks carrying both fixtures | 0 of 0 | **100%, no exceptions** |
| Gate false reports per cluster | 12 recorded historically | **0** |
| `CLAUDE.md` size | 84,913 chars | **< 12,000 chars** |
| Rules in core with no test and no `judgment` class | ~20 | **0** |

---

## 6. Risks and trade-offs

- **Builds get slower.** A full render pass at three viewports on a 31,000px page is
  minutes, not seconds. Mitigation: `targets.json` scopes families per page type; the full
  sweep runs at final pass, not on every edit.
- **The harness will block on its own bugs.** The fixtures make diagnosis fast; they do
  not make the problem zero. The override hatch (§3.1.3) exists for this and is counted.
- **"No test, no rule" can be gamed** by over-using the `judgment` class. Mitigation: the
  class is enumerated in this spec, capped, and each member must state why a test cannot
  exist. The quality report prints its size every run.
- **Migration window.** During Phase 4, some rules live in core and some in packs. The
  `test:` front-matter field is the single source of truth for which is which; the report
  flags any rule present in both.

---

## 7. Out of scope

- Building or rebuilding any page.
- Changing the 68 agents' model/effort tiers.
- Replacing the existing Sprint model, `grill-me`, or any builder skill's method — this
  layer sits underneath them and changes only what "done" means.
- Visual/aesthetic judgment. The harness measures against locked tokens and measurable
  invariants; it never scores taste.

# Lessons — `/african-grey-breeding-pair-for-sale/` Finish Sprint

**Date:** 2026-08-07 (closed out 2026-08-08)
**Plan:** `docs/superpowers/plans/2026-08-07-breeding-pair-finish.md`
**Scope:** Tasks 1–14 — OG re-bakes, bird cards, the review, the singles row, two missed
design rules, two mobile defects, ten contrast failures, a perf gate that did not exist,
and the Sprint 5 LLM visibility baseline.

---

## 1. One missing word in a selector list, two separate screenshotted defects

`caption` was absent from the mobile `display:block` list on `.bpair .tH`. Every other
table child — `thead`, `tbody`, `th`, `td`, `tr` — was there.

Left at its default `display:table-caption` inside a table whose other children had all
become blocks, the browser shrink-to-fits the caption into a narrow column with dead space
beside it. Compounding it, the caption kept a desktop label style — uppercase with `.1em`
tracking — which at 375px forces roughly one word per line.

The breeder screenshotted these as two problems. They were one omission.

**The transferable part:** when a rule converts a table to blocks at a breakpoint, the
child list must be exhaustive, and `caption` is the element everyone forgets because it is
the only table child that is not a row, cell or row-group. This would have hit every future
`.tH` on the site, not just this page.

Banked as `reference_table_caption_mobile_stacking.md`.

## 2. `.ti` — markup↔CSS drift, again

`.bpair` re-themed the dial onto a white bed, but `.ti` kept its dark-theme sage `#7ba98d`.
On white that is **2.66:1** — the ten Lighthouse contrast failures the breeder hit.

The re-theme touched the container and every element that looked like it needed touching.
`.ti` did not look like it needed touching, because on the old dark bed it was fine. Nothing
in the change was wrong on its own; the defect lives in the gap between a re-themed parent
and a child that inherited an assumption about its background.

Fixed with `#5d7d6a` — **4.56:1** on `#fff`, computed rather than eyeballed. Worth noting
the plan predicted 4.62:1 and the shipped comment records 4.56:1; the shipped number is the
recomputed one. Both clear AA, but the lesson is that the ratio gets written down from a
calculation, not from the draft that proposed it.

This is the same failure class as `reference_markup_css_drift.md`: a clean hardening scan is
not a clean page. When a scoped re-theme changes a background, every descendant that sets its
own colour has to be re-checked against the new bed — the scan cannot infer which ones matter.

## 3. Both new rules shipped WITH checks and a known-broken fixture

Task 8 surfaced two design rules the site had been following by habit and never encoded:
hero/counter separation, and image-first H3s.

Neither shipped as a paragraph in a rules pack. Both shipped as:

- a check in `tests/render/checks/layout.ts` — `layout-hero-counter-separation` and
  `layout-h3-image-first`
- a fixture in `tests/render/fixtures/known_broken/` that the check must catch
- an entry in `data/quality/rule-index.json` pointing at the test

Confirmed at close-out: `quality_report.py` §5 lists neither as `untested`, so neither is a
deletion candidate.

**Why this matters more than the two rules do.** CLAUDE.md's own history is the evidence —
that file once carried ~37 rules in 88,000 characters and the measured result was that rules
were re-asserted rather than enforced. A rule with a failing check is worth more than a
paragraph that asks nicely. When a defect escapes, the charge goes to the harness, not to a
new rule.

## 4. There was no perf gate — so the fix was a gate, not a skill

The ten contrast failures reached the breeder because **nothing measured contrast**. The
honest diagnosis was not "we should be more careful"; it was that the invariant had no
enforcement.

What shipped (Task 12):

- `a11y-text-contrast-aa` — a **blocking** harness check, so a regression fails the build
- `scripts/perf_audit.py`
- `skills/cag-perf-gate.md`

A bare skill would have been the cheaper answer and the wrong one: a skill is guidance an
agent may or may not read, and this defect class had already proven it survives guidance.
The blocking check is what actually closes it.

`/70de/` source maps stay **known-ignored** — Cloudflare Rocket Loader, dashboard-only, no
code task exists. Recorded so a future run does not re-diagnose it.

## 5. The gate we shipped to stop contrast regressions was running on ZERO pages

Found at close-out, 2026-08-08, and it is the most important thing in this document.

`a11y-text-contrast-aa` shipped 2026-08-07 as a **blocking** check with a known-broken
fixture and an entry in `rule-index.json`. It passed its fixtures. It appeared in the
manifest. `quality_report.py` did not list it as untested. Every signal said "shipped
gate."

It examined **zero nodes on every page of the site**, for a full day.

**The mechanism.** `pages.spec.ts:88` filters the registry by
`targets.json > families_by_page_type`. The A11Y family was registered in code and added
to no page type. Registering a check does not wire it in, and nothing asserted the two
agreed.

**What caught it, and how late.** `build_scorecard.mjs` Guard 2 — seeded from the manifest
rather than from the partials, precisely so a check that ran nowhere cannot be invisible.
It works, and it is the reason this was found at all. But it only speaks *after* a full
13-minute page run, and its verdict is one line at the very end of thousands of lines of
web-server noise. The run before it reported `48 passed` immediately above the failure.

**Why this is the same bug as three already in the memory bank.**
`reference_gate_examined_zero_pages`, `reference_cssrules_truthy_on_every_rule` and
`reference_promote_check_needs_examined_count` are all one failure: *a check that judged
nothing reporting as a check that judged everything*. This is the fourth instance and the
first where the check itself was flawless — only its wiring was missing. `minExamined: 4`
did not save it either, because that floor is enforced against the fixture, not against
the site.

**The fix is a harness invariant, not a rule and not a fixture.** Added to `meta.spec.ts`:

- a family registered in code but wired to no page type fails the meta gate
- a family declared in `targets.json` that no check registers also fails (the mirror
  typo case)
- both asserted against the real repo, in milliseconds, *before* a 13-minute run

Verified the honest way: the predicate was run against `git show HEAD:tests/render/targets.json`
and reports `['A11Y']` on yesterday's state, `[]` after the fix. The test fails on the
real defect, which is the only evidence that a regression test is worth anything.

**The transferable rule:** *a check is not shipped when it is registered; it is shipped
when it has examined a non-zero count on a real page.* Promotion should be gated on the
examined count from a live run, never on fixtures passing.

### What wiring it in actually found — and why it is now advisory

| | |
|---|---|
| Page-viewports measured | 45 |
| Text nodes examined | 19,685 |
| Reported below AA | 1,783 |
| Clean page-viewports | **0** |

**Zero clean pages is a fact about the check, not about the site.** Two false-positive
classes were confirmed against the built CSS before anything was "fixed":

1. **Out-of-flow labels over photos** — `.rbadge` is `position:absolute; background:none;
   color:#ffffffe0` with `text-shadow:0 1px 4px rgba(20,14,10,.7)`. It is white text over a
   *photo*, legible because of the shadow. `backdrop()` walks DOM ancestors, and an
   absolutely positioned element's ancestors are not the thing it visually covers — so the
   walk sails past the image to a white section and reports white-on-white, exactly 1:1.
   The check's own docstring already says it will not judge text over a background-image;
   it simply cannot detect that case out of flow.
2. **Translucent foregrounds** — Tailwind `text-cream/80` renders `rgb(… / 0.8)`. The
   check's `rgb()` helper returns the three colour channels and discards alpha unless it is
   exactly 0, so a composited foreground is judged as if it were opaque. The translucent
   *backdrop* already gets a "not judgeable" skip; the foreground needs the same.

A third family looks real: clay/gold on light at **3.17–3.38:1** against a 4.5 requirement,
consistent with the clay-contrast issue already banked in
`reference_forsale_dial_rail_contrast` and `reference_aa_contrast_and_perf_fixes`.

**Decision (breeder, 2026-08-08): demote to `advisory`, close out, triage as its own
sprint.** The justification is the project's own promotion rule, quoted in `targets.json`:
*a check is promoted once it has passed its fixtures AND produced zero false reports across
one full cluster.* A11Y has not met that bar. Its two same-day siblings —
`layout-hero-counter-separation` and `layout-h3-image-first` — both entered advisory
correctly; only the contrast check skipped the step, and skipping it is what let a
zero-examined gate look shipped.

Advisory is strictly better than what shipped yesterday: the check was already stopping
nothing, and now it counts 1,783 leads instead of reporting silence.

## 6. Sprint 5 — verify an agent's report against source before acting on it

The `cag-llm-keyword-intel` run produced a well-formed 30-cell brief. Two of its
load-bearing claims were re-checked against our own files before any of it was trusted, and
that check changed two findings:

- **Report Action 2 overstated its gap.** It described the DNA answer as "one FAQ item near
  the bottom." There are two placements — an H5 at `:670`, mid-page inside the paperwork H2,
  and FAQ 05 at `:854`. The real weakness is structural (no H2/H3 of its own), not absence.
  Acting on the report as written would have added content that already existed.

- **A suspected same-page contradiction was not one.** Verification found five `DNA-sexed`
  trust labels on the singles cross-sell row against two prose statements saying the pairs
  carry no DNA certificate. This looked like a factual defect. The breeder's ruling: *all the
  single birds are DNA sexed; only the three breeding pairs have no DNA.* **Both statements
  are true of different birds.** There was no defect and no edit to make.

**The transferable part, and it cuts twice.** A gate's output is a hypothesis about the page;
so is an agent's report. But the second bullet is the sharper lesson — *my own* verification
finding was also only a hypothesis, and it took the breeder's domain knowledge to falsify it.
Confirming that text X and text Y coexist on a page does not establish that they contradict;
that requires knowing which birds each refers to. This is the same trap as the 72-hour /
3-day guarantee, which once sent agents across 53 live pages to "fix" copy that was already
correct. The flag is now recorded in the plan's `## Open Flags` as **resolved, do not
re-raise**.

The baseline itself is honest: **24 of 30 cells fetched**, Claude's 6 written `NOT FETCHED`
with the barrier named (hard login wall, no API key). Nothing was inferred to fill them, so
future runs compare against 24, not 30.

---

## What a future session should carry forward

1. Exhaustive child lists when a table becomes blocks — `caption` included.
2. After any scoped re-theme, re-check every descendant that sets its own colour against the
   new background. The scan will not find it for you.
3. New rule ⇒ check + known-broken fixture + `rule-index.json` entry, in the same commit.
4. When a defect class reaches the breeder, ask what *measured* it. If the answer is nothing,
   build the gate.
5. Verify an agent's findings against source before acting — and hold your own verification
   to the same bar, because "these two statements coexist" is not "these two statements
   conflict."

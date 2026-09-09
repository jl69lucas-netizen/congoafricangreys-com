# Evidence Pass Gate Report

Plan `docs/superpowers/plans/2026-09-09-evidence-pass.md`, executed 2026-09-09 on `main`, commits `3492c4c5` → `de03d165`. Strategy A: sections stay, repetition goes, proof replaces assertion.

## 1. Homepage: before and after

Measured on the built page (`dist/index.html`, `<main>` text only) by `python3 scripts/evidence_audit.py index`.

| Term | Before | After | Ceiling |
|---|---|---|---|
| C.A.Gs | 66 | 16 | 20 |
| CITES | 44 | 6 | 6 |
| DNA | 40 | 6 | 6 |
| Appendix I | 28 | 2 | 2 |
| captive-bred | 32 | 6 | 6 |
| USDA | 19 | 3 | 4 |
| Midland | 23 | 5 | 5 |
| scam | 10 | 2 | 2 |
| legit | 7 | 0 | 0 |
| Title (chars) | 197 | 54 | 70 |
| Statement labels | 0 | 32 | — |
| Sections | 20 | 20 | never fewer |

Verdict: **0 ERROR / 7 WARN**. Every WARN is a claim whose proof object is still NOT FETCHED (see §5) plus one PROXY note on the blog cards.

Eight of the sixteen remaining C.A.Gs mentions sit inside verbatim review quotes and were not edited.

## 2. What shipped, task by task

| Task | What it is | Commit |
|---|---|---|
| 1 | RED baseline: a subagent under the old rules doubled two sections and raised every trust term | `3492c4c5` |
| 2 | `evidence-budgets.json` (per-page-type ceilings, proposals until Sprint 0 calibrates) + `evidence-ledger.json` (six claims → proof, all NOT FETCHED) | `bf94786e` |
| 3 | `scripts/evidence_audit.py`: seven checks, 19 tests, fires on the two known review defects before it was trusted | `106f6687` `1d0d7775` `72f2daba` |
| 4 | Four rule rows in `rule-index.json`; `quality_report.py` reads ids from `*_audit.py` | `200aede0` |
| 5 | `StatementLabel.astro` (Fact / Observed here / Our recommendation) + `sem-statement-label-visible` render check with fixture pair | `205a6153` |
| 6 | `skills/cag-evidence-pass.md`, written against the baseline's fourteen verbatim excuses; GREEN on first run | `79512400` |
| 7 | Six injector rules retired across 16 files: no keyword floor, Rule 57 = 95–105 distinct entities, Rule 56 = competitor count +5–10, H5/H6 advisory on home + location, alt ≤125, title ≤70 | `2aba161b` |
| 8 | `data/reviews.json` single source + sweep; the breeder's names applied on 8 pages | `e9674f2a` |
| 9 | Homepage pass: one-clause title and H1, `#proof` trust section, 32 labels, brand and credential budgets met, homepage added to the render harness | `288b0df0` `de03d165` |
| Follow-up | Final review found an AI-invented USDA licence number (`#74-B-0247`) live on two near-me pages plus a Timneh price below the floor; removed, home profile skips breadcrumb, copy pack and rule index now describe all seven checks | `d5fedfbb` |

## 3. Review attribution: final

| Quote | Buyer | Photo |
|---|---|---|
| "I searched for African Grey parrots for sale near me…" | Clifford Hutter, Secaucus, NJ | none on file |
| "At first I was hesitant about buying a bird online…" | Richard Woodard, Winter Haven, FL | on file |
| "I ordered a Congo African Grey from C.A.Gs and the experience was flawless…" | Catherine Kempf, Schaumburg, IL | on file |
| "Finding a healthy and well-socialized female Congo African Grey…" | Archie O'Brien, Farmingdale, NY | on file |

Albert Schroder was the wrong name on two pages and is gone. Archie's photo never sits next to another buyer's words. The stray word "parrot" after the final period in the supplied O'Brien text was treated as a typo. Eight pages changed and were submitted to IndexNow once live. The homepage and the two near-me pages were submitted after their own deploys.

## 4. Gates run on the shipped homepage

| Gate | Result |
|---|---|
| evidence_audit (×2) | 0 ERROR / 7 WARN, 1 page examined |
| pytest tests/ | 170 passed |
| test:render:meta (×2) | 255 passed, 24 skipped |
| test:render:pages | 54 passed; homepage blocked by three pre-existing rows (§6) |
| final_page_audit --type home | has_breadcrumb = FALSE POSITIVE (root page), img_alt_unique = Kempf ×2 (pre-existing), min_h6_5 advisory |
| dup_content_audit (key `dist`) | PASS body and headers, 1 page |
| review attribution pytest | 3 passed |
| Other pages' rendered markup | byte-identical to a HEAD worktree build; only the shared Tailwind bundle gained five homepage-only utilities |

## 5. Open flags for the breeder

1. **Proof objects.** All six ledger rows are NOT FETCHED: a redacted USDA AWA record, an example CITES certificate, an example DNA certificate, an example avian-vet certificate, a PBFD/APV PCR result, a hatch certificate or band photo. Each row's link currently reads "How we document it". Supply one image or PDF per row and the audit's six WARNs close.
2. **Catherine Kempf twice.** Four real quotes fill five review slots, so her quote shows in reviews-mid and in the grid. A fifth verified review removes the duplicate and the duplicate-alt row.
3. **Blog title lock.** Task 7 changed the 2026-07-02 pipe-stacked blog title pattern to the one-clause form ("retrofit on next touch"). Confirm blogs should follow the newer ruling.
4. **Rule 21.** seo-rules Rule 21's five-part title formula still sits above the new ≤70 cap; a follow-up pass should reconcile it.
5. **Budgets are proposals.** `calibrated: null` until Sprint 0 checks them against the pages answer engines actually cite.
6. **BirdCard badges on the homepage** now read "Documented → #proof · Fully Weaned" instead of the five credential badges; other pages keep the five. Say if you want the homepage cards to match.

## 6. Pre-existing homepage defects the harness now sees

The homepage was never a render-harness target. Adding it exposed three blocking rows that predate this pass and are live today:

- **IMG oversized**: 7–12 images served at 2.7×–12.5× their displayed size (hero, candled eggs, breeding pair, habitat, a review avatar). srcset work.
- **IMG duplicate alt**: "Catherine Kempf" ×2 (flag 2 above).
- **NAV scroll-margin**: 19–20 in-page links land outside the target band because sections use an 80px scroll margin under a 96px header.

One harness bug surfaced too: the contrast checker parses Tailwind v4 `oklab(… / 0.85)` as near-black and reports false 3.28:1 rows on white text. Needs a `known_broken` fixture; charged to the harness, not to a rule.

## 7. What the next build session does first

```bash
npx astro build && python3 scripts/evidence_audit.py <slug>
```

The skill `cag-evidence-pass` runs after `anti-ai-writing` and before `cag-final-page-pass` in Sprint 4. Then: Sprint 0 budget calibration; the 14-day LLM-visibility re-probe on the homepage's six queries (Sprint 6); the three render rows in §6; the `/african-grey-reviews/` page carries the same shared-component repetition the budgets will now flag.

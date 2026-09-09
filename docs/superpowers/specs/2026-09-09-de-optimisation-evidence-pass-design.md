# C.A.Gs De-Optimisation & Evidence Pass

Brief date 2026-09-09 · Author: Claude (Fable 5.1) working from the repo, `dist/`, and the data files · Status: DESIGN FOR APPROVAL. Nothing on the site has been edited.

## 1. Verdict in One Paragraph

The ChatGPT report is directionally right and evidentially weak. Its central claim, that the site repeats trust concepts far more often than it proves them, is confirmed by measurement: the built homepage says **CITES 44 times, C.A.Gs 66 times, DNA 40 times, "Appendix I" 28 times and captive-bred 32 times** inside `<main>` alone, across 8,830 words and 25 H2s. Its most alarming claims are not supported by anything we hold: there is **no before/after AI Overview data** in our GSC exports, the location pages are **thin, not duplicated** (median 8-gram overlap between any two state pages is 0.044), and one of its "proof" examples (a USDA licence number) is invented. The one evidence defect that matters most, it missed entirely: the homepage attributes the **same review text to two different named buyers** in two places. The fix is not to cut sections. It is to replace repetition with proof, one section at a time, and to retire the four house rules that manufactured the repetition in the first place.

## 2. What I Measured (Not What I Believe)

All figures are from `dist/` after the current build, main content only unless stated. Nothing here is inferred.

### Homepage, `<main>` only

| Signal | Count | Read |
|---|---|---|
| Words | 8,830 | 25 H2 · 60 H3 · 10 H4 · 5 H5 · 3 H6 |
| C.A.Gs | 66 | brand self-reference every 134 words |
| CITES | 44 | "Appendix I" alone appears 28× |
| DNA | 40 | |
| captive-bred | 32 | |
| hand-raised / hand-fed / hand-reared | 25 | |
| Midland | 23 | |
| avian (vet) | 23 | |
| USDA | 19 | |
| health certificate | 15 | |
| guarantee | 13 | |
| scam | 10 | on the homepage, not the scam page |
| legit | 7 | |
| `<title>` length | 233 chars | four pipe-separated clauses; the house rule allows ≤205 |

Rhetoric ChatGPT quoted that is really on the page: "nothing to hide" (1), "waitlist" (5), "World's Best Talking" (1), "America's Trusted" (3), "dream of" (1). Rhetoric it quoted that is **not** on the page: "no bait listings" (0), "the opposite of how scams work" (0). It paraphrased from memory in places.

### Site-wide (105 built pages)

| Signal | Value |
|---|---|
| Pages whose body mentions "scam" | 39 of 105 |
| Pages whose body mentions "legit" | 32 of 105 |
| Titles containing a `\|` or `—` separator | 105 of 105 |
| Title length, deciles | 30 · 59 · 61 · 65 · 80 · 95 · 136 · 153 · 177 · 197 · 233 |
| Titles containing "for Sale" | 64 |
| Longest pages (main words) | scam guide 10,343 · vs-amazon 9,800 · vs-macaw 9,360 · homepage 8,830 |
| Scam guide: "scam" ×154, "USDA" ×71, "CITES" ×84 | the page that should own the topic also over-repeats it |

### Location pages (40 state/city pages)

| Signal | Value |
|---|---|
| Median pairwise 8-gram Jaccard | 0.044 (very low; these are not find-replace copies) |
| Worst pairs | 0.55 (Tennessee ~ Virginia ~ Wisconsin ~ North Carolina; Colorado ~ Oregon) |
| Main word count range | 172 to 595 |

The doorway diagnosis is wrong on the evidence. The real exposure is the opposite one: **most state pages are under 600 words of body copy**, and a cluster of five late-batch states share over half their 8-grams. Thin plus templated is the risk, not mass duplication.

### AI visibility, the only measured baseline we have

`sessions/2026-08-07-breeding-pair-sprint5-llm-visibility.md`, 6 queries × 4 reachable engines, live browser:

| Engine | Cited | Note |
|---|---|---|
| Google AI Overview | 0 of 6 | cited zero breeder-owned pages for any query; directories and marketplaces only |
| Perplexity | 4 of 6 | leaned on **our own vocabulary** (PBFD/APV PCR, band, hatch certificate); twice attached facts from the wrong page to the wrong pair |
| ChatGPT | 1 of 6 | "C.A.Gs, Midland, Texas" was the only breeder named |
| Gemini | 0 of 6 | named two competitor breeders by brand |

The GSC "Search appearance" export on disk contains two rows only: Product snippets and Merchant listings. **There is no AI Overview row in our data.** Any statement that we "lost" AI Overview citations is NOT FETCHED. Bing (2026-08-26 export) shows the homepage at average position 6.5 with 528 impressions and 23 clicks, so organic visibility on the homepage is intact on at least one engine.

## 3. Honest Review of the ChatGPT Report

### Where it is right, and now measured

- **Concept repetition, not keyword density** (its §3). Confirmed above. This is the primary defect.
- **The homepage does too many jobs** (§2, §21). 25 H2s and 8,830 words is a site, not a page. The breeder's constraint that sections stay is compatible with this finding: the problem is what each section repeats, not that the section exists.
- **Scam and "legit" propagation** (§13, §14). 39 and 32 pages respectively. One page should own each, everything else links once.
- **Titles read as engineered** (§24). Every one of 105 titles carries a separator; the median is 95 characters and the longest is 233. Our own meta rule (Title ≤205, never short) is the cause.
- **Claims outrun proof** (§35, §36). Every credential is asserted; none is shown. `credentials.md` records the USDA licence as "Active, verifiable at aphis.usda.gov" but holds no number, no redacted certificate, no example DNA or vet certificate is published anywhere.
- **Fact, observation and recommendation are blended** (§10). True in the species, comparison and care sections.
- **Do not answer this with more pages** (§31). Agreed, and it is the reason Strategy C below is not recommended first.

### Where it is wrong, or unverifiable, and must not be acted on

- **"AI Overview loss" is the report's premise and we cannot see it.** No AI Overview data exists in our exports. The only baseline we hold shows Google AIO citing no breeder-owned pages at all, which argues the loss is category-level, not a penalty on us. Sprint 0 forensics must run before any consolidation is justified by "loss".
- **Doorway abuse on location pages.** Measured overlap says no. The pages are thin. Consolidating them would remove the one place the state-level real buyer stories it recommends in §34 could live.
- **"USDA License #74-B-0247".** Invented as an example. It is not in `credentials.md` and must never appear on the site. Rule 10 applies: the real number comes from the breeder or it is written NOT FETCHED.
- **"4.9 / 5 across 52 verified buyers".** It took this at face value. On the homepage source, the quote beginning "I searched for African Grey parrots for sale near me for months" is credited to **Clifford Hutter, Secaucus NJ** in the feature block and to **Archie Obrien, Farmingdale NY** in the bottom grid; the quote beginning "I ordered a Congo African Grey from C.A.Gs and the experience was flawless" is credited to **Albert Schroder, Santa Clara CA** and to **Catherine Kempf, Schaumburg IL**. Identical text, two attributions, same page. This is the single most damaging evidence defect on the site and it is invisible to every gate we run. Memory records fabricated testimonials being removed once already. Only the breeder can say which attribution is real.
- **The 55,000-query arXiv study, the "1,000+ lines" figure, and every /10 rating** are unsourced or taste. NOT FETCHED. They change nothing in the plan.
- **§23 and §37 (neutral reference pages, knowledge base) contradict its own §31.** Both are "publish more". They belong after the evidence pass, not before it.
- **"Reduce the homepage 30 to 50 percent"** is a target, not a diagnosis. Word count should fall as a by-product of removing repetition. Cutting to a number invites cutting proof.

### What it missed that our own system caused

Four house rules actively manufacture the pattern ChatGPT is describing. They are in `docs/reference/WORKFLOW.md` Sprint 4 and the keyword-verifier agent:

| Rule | Text | Effect |
|---|---|---|
| keyword-verifier band | flags **UNDER-OPTIMIZED** below 85 keyword mentions | a floor on repetition |
| Rule 57 | "150+ entity mentions verified" | rewards entity stuffing |
| Rule 56 | "150–200 keyword variants" documented | pushes 25-H2 pages |
| Heading gate | ≥5 H5 **and** ≥5 H6 on every page, no skips | forces depth that has to be filled with words |
| IMAGE-01 / IMAGE-02 | alt text ≥250 chars; 300-word image description block per hero | keyword-carrying text nobody reads |
| Meta format | title ≤205, "never short" | the 233-char title |

These are the injectors. A de-optimisation skill that does not retire or invert them will be overruled by them in the same sprint.

## 4. Three Strategies

### Strategy A — Evidence Substitution, section by section (Recommended)

Keep every section on every built page. Inside each section, do three things: (1) say each trust concept **once** where it is load-bearing and replace the other mentions with a link to the proof; (2) attach one **proof object** per credential (redacted USDA record, example DNA certificate, example vet certificate, example CITES paperwork, buyer + date + bird + photo) and show it once per page; (3) label every claim as **Fact (sourced)**, **Observed here (n birds, since year)** or **Our recommendation**, using one visible component. Set per-page term budgets and let word count fall out of them.

**Why (data).** The measured defect is repetition and unproven assertion, not coverage. Perplexity, the one engine that cites us, already lifts our own evidence vocabulary; giving it proof objects feeds the engine that is listening. The approach is mechanical enough to gate (term budgets, proof-object presence, label presence, review-attribution integrity), which is the only kind of rule this project has found to hold.

**Trade-off.** It is blocked on the breeder for proof objects and for the review-attribution answer, the same asset dependency that stopped the for-sale cluster close. Copy can be de-repeated now; the proof layer waits for assets.

### Strategy B — Consolidate and re-route

Prune the location matrix, move all scam and "legit" content to the two pages that own it, collapse titles to ≤70 characters, noindex the thinnest pages.

**Why not first.** The location pages are thin, not duplicated, and we have no per-page AI or GSC evidence that any of them is hurting. Cutting before Sprint 0 forensics is the exact "act on a gate's output without confirming the defect" failure this project has recorded twelve times. The title and scam-routing parts of B are correct and are folded into A as budgets.

### Strategy C — Authority layer

Build the neutral species, legal, health and behaviour reference pages and the breeder knowledge base, then link commerce from them.

**Why not first.** It is more pages, which is what the report itself says not to do first, and every one of those pages would today be written under the same injector rules that produced the homepage. Run it after A has changed the rules, and seed it from the proof objects A collects.

## 5. Homepage Section-by-Section Plan (Sections Stay)

Each row keeps the section. "Cut" means repeated concept mentions, never the section. Budgets are starting points to calibrate in Sprint 0 against the pages Perplexity actually cited; they are not fetched from a competitor.

| Section (`id`) | Keep | De-optimise | Add proof |
|---|---|---|---|
| Hero + H1 | hero, CTA, bird count | H1 "Breeder You Can Trust" → what we are and where; title 233 → ≤70 chars, one clause | one credential row with links to proof objects, shown here only |
| On This Page (jump rail) | rail | drop "18 sections · everything about C.A.Gs" self-description | none |
| `reviews-top` | one featured review | **resolve the duplicate attribution first** | buyer + date + bird + shipping method |
| `available-birds` | cards, prices, shipping line | remove repeated CITES/DNA badges per card; one badge row above the grid | link each card to its `/available/` record |
| `eggs-pairs` | both offers | verify no DNA-sexing claim attaches to the pairs (singles are DNA-sexed, pairs are not; both statements are true) | none |
| `congo` | species facts | mark species facts as **Fact (source)**; remove "world's best talking" | first vocalisation age observed here, if the breeder has it |
| `timneh` | species facts | same treatment; keep Levi × Rily lineage | same |
| `compare-species` | table | strip superlatives ("wins", "best"); keep measured differences | none |
| `why-us` | the two brand methods | one definition each; remove third-party-sounding certification language | Benjamin Home-Raising Protocol: weaning-age range observed |
| `trust` | credential row | say each credential once here; delete the re-statements elsewhere on the page | the proof objects live here |
| `reviews-mid` | one review | different buyer from top | date + bird |
| `history` | since-2014 story | cut "America's Trusted" ×3 | none |
| `health` | screening list | PBFD/APV/DNA said once; ledger-bound | example vet certificate (redacted) |
| `pricing` | ladder | keep; one CITES mention | none |
| `tools` | calculators | keep | none |
| `shipping` | two-tier cost | keep; "all 50 states" once | one real shipment: airport, date, outcome |
| `reviews` (grid) | grid | dedupe against `reviews-top` | photos already exist; add dates |
| `blog` | cards | keep | none |
| `video` | embed | keep | VideoObject schema already required |
| `faq` | 4 accordions | keep questions buyers ask; drop keyword-only questions | answers link to proof |
| `pros-cons` | list | keep; this is the most honest section on the page | none |
| `how-to-buy` + form | steps, form | "no waitlist tricks" → the actual reservation rule | none |
| Scam paragraphs (anywhere) | one sentence + link to the scam guide | remove the other nine mentions | none |

Starting term budgets for the homepage `<main>`: C.A.Gs ≤20 · CITES ≤6 · Appendix I ≤2 · DNA ≤6 · captive-bred ≤6 · USDA ≤4 · Midland ≤5 · scam ≤2 · legit 0 · superlatives (best, smartest, most, wins) 0 unless sourced.

## 6. The Skill: `cag-evidence-pass`

### Do we need it?

Yes, and only as a gate that owns things no existing skill owns. What already exists and must not be duplicated:

| Existing | Owns | Gap it leaves |
|---|---|---|
| `cag-aeo-pass` | BLUF, atomic sections, brand method names, citability | pushes toward more declaratives; no ceiling on repetition |
| `anti-ai-writing` | AI-tell phrases and rhythm | no notion of proof vs claim |
| `framework-eeat` | E-E-A-T signal checklist | asserts signals; does not check that each is backed by an object |
| `cag-duplicate-content-gate` | sibling crossover | nothing about within-page repetition |
| `cag-keyword-verifier` | keyword count band | the floor is the defect |
| `cag-non-commodity-content-agent` | original breeder-voice content | generator, not a gate |
| `cag-gate-integrity` | trusting checkers | applies to this one too |

The new skill owns four checks nothing else does: **term budgets per page type**, **claim-to-proof binding** (every ledger claim on a page points at a proof object or is written once and linked), **statement labels** (Fact / Observed here / Our recommendation present where species, health or comparison claims are made), and **evidence integrity** (no review text under two names, no invented identifiers, no NOT FETCHED left in prose).

### Shape

```
skills/cag-evidence-pass/
  SKILL.md                    # gate + rationalisation table + red flags
  budgets.json                # per-page-type term ceilings, calibrated in Sprint 0
scripts/evidence_audit.py     # mechanical: budgets · proof binding · labels · review integrity · title length
data/quality/evidence-ledger.json   # per claim: proof object path or NOT FETCHED, breeder-confirmed date
tests/render/fixtures/known_broken/evidence-*.html  # the meta gate must catch a planted duplicate review + a budget breach
```

Rule-index entries added with `enforced: test`: `term-budget-per-page`, `claim-bound-to-proof`, `statement-labels-present`, `review-attribution-unique`. `python3 scripts/quality_report.py` picks them up automatically.

### Built by the writing-skills method

Per the Iron Law: baseline first. A subagent is given one homepage section and today's rules and asked to "improve" it; its output and rationalisations ("the keyword band says under-optimised", "≥5 H6 needs more headings", "the AEO pass wants a declarative per H2") are recorded verbatim, then the skill is written against those exact excuses, re-run, and tightened. Then `known_broken` fixtures make `npm run test:render:meta` fail before the check is trusted on a page.

## 7. Where It Sits in the 7 Sprints

| Sprint | Change | Owner |
|---|---|---|
| 0 Intel | Add **AI-visibility forensics**: `cag-llm-keyword-intel` baseline on the target page's 6 queries; term-density of the pages each engine actually cited → `budgets.json`; note that GSC holds no AI Overview row (NOT FETCHED, not "lost") | cag-gsc-analytics + llm-keyword-intel |
| 0.5 Orient | grill-me gains one question per credential: "what proof object exists for this, and can we show it?" → `evidence-ledger.json` | grill-me |
| 1 Blueprint | The H1–H6 outline carries a **Claim → Proof** column per section and the page's term budget; header dup-gate also flags superlative headers | cag-content-architect |
| ASSET GATE | Proof objects (redacted certificates, dated buyer records) are assets like infographics: no proof, the section ships as **link-to-proof**, never as re-assertion | breeder |
| 2 Build | EEBP's Evidence slot must resolve to a ledger row; the statement-label component is part of the kit | page-type builder skills |
| 3 Harden | Unchanged; adds a render check that the label component and proof links are visible at 375 | page_hardening_scan |
| 4 Final | **Insert `cag-evidence-pass` after `anti-ai-writing`, before `cag-final-page-pass`.** Keyword-verifier band inverted to a ceiling only; Rule 57 relaxed to "entities present where load-bearing" | final gate |
| 5 Ship | Unchanged; IndexNow every slug whose rendered output changed | deploy |
| 6 Bank | quality_report adds an evidence rework rate; re-probe LLM visibility 14 days post-deploy and record it; back-propagate any new rationalisation into the skill | session-closer |

### Rules to retire or invert (proposed, needs breeder approval)

| Rule | Proposal |
|---|---|
| keyword-verifier UNDER-OPTIMIZED < 85 | delete the floor; keep the ceiling at the Sprint 0 calibrated budget |
| Rule 57 "150+ entity mentions" | replace with "every ledger entity present once where load-bearing" |
| Rule 56 "150–200 keyword variants documented" | keep as research, remove as page requirement |
| ≥5 H5 and ≥5 H6 on every page | keep "no skipped levels"; drop the minimum counts on homepage and location pages |
| IMAGE-01 alt ≥250 chars · IMAGE-02 300-word image block | alt describes the image, ≤125 chars; drop the image block |
| Meta title ≤205, "never short" | ≤70 characters, one clause, brand suffix optional |

## 8. Open Flags and the One Question

- **Review attribution.** Two quotes, four names. I cannot know which are real. This blocks `reviews-top` and `reviews` and it is the first thing to fix on the homepage regardless of strategy.
- **Proof objects.** None exist in the repo. Each is NOT FETCHED until the breeder supplies it.
- **AI Overview before/after.** Not measurable from what we hold. If the GSC property has the 2026 generative-AI report, an export of it is the single most useful file for Sprint 0.
- **Budgets** are proposals until calibrated against cited pages.
- Nothing has been edited on the site or in the rules. The skill is not written; per the writing-skills method it cannot be until its baseline test has been run, and per the brainstorming gate it waits for this design's approval.

**The one question:** approve Strategy A with the six rule changes in §7, so the next session runs the baseline test, writes `cag-evidence-pass`, and applies it to the homepage first?

## 9. What Happens on Approval

1. Breeder answers the review-attribution question and supplies whichever proof objects exist.
2. RED: baseline subagent run on two homepage sections; rationalisations logged.
3. GREEN: `cag-evidence-pass` skill + `evidence_audit.py` + ledger + rule-index rows + known_broken fixtures; `npm run test:render:meta` must fail on the fixtures first.
4. Rule changes applied to WORKFLOW.md Sprint 4 and the keyword-verifier agent; `register_skills.py --copy`.
5. Homepage: sections in §5 order, dup-gated, hardened, evidence-passed, final-passed, built, pushed, IndexNow.
6. Location cluster next, using the thin-not-duplicate finding: one real dated shipment per state where one exists, NOT FETCHED where none does.

# Closing the For-Sale Cluster — Shipping · Near-Me · Hub — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. **Breeder mandate for this program: work inline, NO subagents** (carried over from `2026-07-19-for-sale-pages-program.md`). Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the for-sale cluster. Rebuild the **three** remaining pages — buy-with-shipping, the near-me geo router, and the hub — execute the three near-me retirements verdicted on 2026-08-09 but never applied, and retire the singular `/african-grey-parrot-for-sale/` into the hub. Scope expanded from two pages to three builds + one retirement on 2026-08-10 at breeder request; the analysis behind the role split is §0f–§0g.

**Architecture:** Both pages are pre-standard WordPress-era stubs (15,411 B and 5,583 B against a cluster median of ~114,000 B). They are rebuilt in place at their existing slugs using `skills/cag-for-sale-page-builder` under the TRANSACTIONAL profile — Sprint 0 research → Sprint 0.5 strategy → H1–H6 outline gate → component tuple → visual companion → build → Phase-4 QA. Page A is **retargeted** (shipping is demoted from search target to trust section; the page aims at the unowned buy/buy-online cluster). Page B is built as a **routing hub** that catches near-me query variance and hands buyers to the 22 location pages, then absorbs three retired siblings. Order is load-bearing: **B ships before the three 301s point at it.**

**Tech Stack:** Astro (`src/pages/<slug>/index.astro`) · Direction D theme · the for-sale component kit (`assets/1WORKING-ON/FOR-SALE-PAGES/`) · `data/clutch-inventory.json` + `data/price-matrix.json` as the only price/inventory sources · Firecrawl MCP for SERP/competitor fetch · `scripts/final_page_audit.py`, `scripts/dup_content_audit.py`, `scripts/page_hardening_scan.py`, `scripts/generate_sitemaps.py`, `scripts/indexnow_submit.py` · `npm run test:render:meta` / `test:render:pages`.

---

## 0 · Where we actually are — verified 2026-08-10

This section is the answer to "have we done the full deep competitor analysis, and what gate are we at."
Every line below was checked against the repo or the live site today, not recalled.

### 0a · Deep competitor analysis: **partially done. Per-page Sprint 0 is NOT done for either page.**

The Gate-1 document says so in its own words, in §5 "What I Have Not Done":

> *"Not re-run: full §6 research depth — section and visual inventory per competitor, PAA to three levels, autosuggest, Reddit mining. That belongs to Sprint 0 of whichever page is approved for build."*
> — `docs/artifacts/gate1-buy-prefixed-pages.html`, committed `27e78d20` (2026-08-09)

**What exists and does not need re-running:**

| Asset | Where | Covers |
|---|---|---|
| Google GSC keyword mining, 16 months to 2026-07-16 | `docs/research/for-sale-keywords-2026-07.md` §143 | Per-page buckets: near-me **23 queries / 310 imp**; shipping **0 queries / 0 imp** |
| Gate-1 build-or-consolidate verdict | `docs/artifacts/gate1-buy-prefixed-pages.html` | Both Google windows, Bing Aug-26 export, Firecrawl SERP 2 queries × 10, the 40-query buy cluster, the 55-query near-me cluster, the survivor decision + trade-off |
| Registry-wide competitor sweeps 1–5 | `docs/research/competitor-sweep-page{1..5}-2026-08-09.md` (~322 KB) | 27 competitors re-verified; shipping-page evidence (22 mentions in sweep 1, 12 in sweep 2); live price ladder; state coverage vs the canonical 22; AI-Overview citation ledger; **Reddit thread ledger — marked "do not re-mine"** (sweep 3 §C4) |
| Competitor registry, repaired | `data/competitors.json` + `docs/artifacts/cags-competitor-registry-2026-08-09.html` | 60 entries, pytest-gated, 2 never-link domains |

**What is missing for these two pages specifically — this is the Sprint 0 work Tasks 2 and 3 do:**

- SERP top-10 **section-by-section inventory** for `buy african grey parrot online` and `african grey parrot for sale near me` (which sections the ranking pages ship, in what order, with what visual assets).
- **PAA to three levels** + **autosuggest** fan-out for both query sets. Neither is in any sweep — the string "People Also Ask" appears 2–4 times per sweep, all in method notes, never as a harvested set.
- Per-page **entity map** and **visual asset blueprint**.
- **Local-pack composition** for the near-me SERP (Gate 1 established the SERP is classifieds + local businesses; it did not enumerate what the pack shows or how the 22 location pages compare).

**Bing query-level data stays `NOT FETCHED`** — every Bing export is page-level or a date series. Do not infer it.

### 0b · Gate status: **Gate 1 is verdicted, not approved, not executed.**

| Gate | State | Evidence |
|---|---|---|
| **Gate 1 — build-or-consolidate** | Verdict written, **awaiting breeder approval** | Artifact ends `▣ APPROVAL GATE 1 — breeder approves, rejects, or splits per page` |
| **The 3 retirements** | **NOT executed** | `data/page-map.json` still records all three as `"status": "live"` with `"redirects_to": null`; no lines for them in `public/_redirects`; all three return **200** live |
| Prior Gate-1 batch (2026-08-08) | Executed | `grey-african-parrots-for-sale` + `male-african-gray-for-sale` carry `"status": "consolidated"` + do-NOT-rebuild notes — that is what an executed gate looks like |
| **Sprint 0 / 0.5 / outline / visual / build** | Not started for either page | No `sessions/for-sale-research/<slug>/` exists for either; the only folder there is `african-grey-parrot-adoption-cost` |

### 0c · The gate that cannot fire — a harness defect, found today

`scripts/final_page_audit.py:359` defines `FORSALE`. **Neither target slug is in it. Neither is the hub.**
The list still contains the three slugs consolidated on 2026-08-08, which is why a clean run prints:

```
✗ affordable-african-grey-birds-for-sale: dist/ MISSING — run `npx astro build`
✗ grey-african-parrots-for-sale: dist/ MISSING — run `npx astro build`
✗ male-african-gray-for-sale: dist/ MISSING — run `npx astro build`
```

`tests/render/targets.json` has the same hole — both target slugs are absent from `pages`.

This is the **Registered ≠ Wired** failure again: a blocking gate that examines zero of the pages it is
supposed to guard. Per CLAUDE.md — *"When a defect escapes, charge it to the harness, not to a new rule"* —
Task 1 fixes the harness **before** any page work, so that the build is measured rather than asserted.

### 0d · Defects confirmed on the two pages (read from source today, to be fixed by the rebuild)

**`/buy-african-grey-parrots-with-shipping/`** — 15,411 B · 4 H2 · H4–H6 absent · 14 inbound internal links:

1. **Internal factual contradiction.** FAQ schema line 21 says birds travel *"in the climate-controlled cargo hold"*; the Delivery Options card line 161 says the bird *"flies in a climate-controlled **cabin**, supervised by experienced pet nannies."* Both are in the rendered page. One is wrong.
2. **Home Delivery card ships no price** — the `$350 home` tier is missing while `$185 airport` appears five times. Violates the shipping-line rule.
3. **4 stale-gold occurrences** — `text-gold` (lines 99, 197), `border-gold/30` (158, 168). Gate 1 estimated 2; the real count is 4.
4. **"Where We Ship" is WordPress residue** — Wausau WI, Oak Ridge TN, Princeton NJ, Asheville NC, Harrison AR. Six unlinked strings, none matching the canonical 22 location pages.
5. **Zero bird cards, zero prices, zero Product/Offer schema, no contact form, no seams, no dial/rail, no in-body images.**

**`/african-grey-parrots-for-sale-near-me/`** — 5,583 B · **1 H2** · no H3–H6 · 2 inbound links:

6. **Timneh price is wrong.** The page says `$1,200–$2,500`. `data/price-matrix.json` says **$1,500–$1,600**, and live inventory is Evie $1,500 / Elad $1,600. The $1,200 floor is not sourced from anything.
7. **Stale gold hex** `#f0c674` inline at line 55.
8. The page is otherwise a hero + trust chips + 4 FAQs. It is the destination of a **54-click** 301 and cannot hold it.

### 0e · One price-vocabulary drift to settle, not a blocker

`data/price-matrix.json` sets Congo at **$1,700–$3,500**; CLAUDE.md states the Congo range is **$1,500–$3,500**;
sweep 3 §C4 asserts *"$1,500 — exactly CAG's Congo floor."* Live inventory reconciles them: **$1,500 is the
site-wide floor (Evie, Timneh); $1,700 is the Congo floor (Bery).** Both live pages are internally consistent
under that reading — `congo-african-grey-for-sale` ships `$1,700–$3,500`, `baby-african-grey-parrot-for-sale`
ships `$1,500–$3,500` for the whole range. **The sweep-3 sentence is the one wrong artefact** and is corrected
in Task 12. Write "from $1,500" only when the sentence is about the whole aviary; write "Congo from $1,700"
whenever the sentence is about Congos.

### 0f · The singular/plural pair — scope EXPANDED 2026-08-10 at breeder request

The breeder asked for `/african-grey-parrot-for-sale/` (singular) and `/african-grey-parrots-for-sale/`
(plural) to be folded into this sprint as the hub work. Analysis below; the decision is §0g.

**Correction to an earlier reading of this plan.** An earlier draft cited the singular page as *"123 queries /
5,346 impressions — the largest query bucket in the cluster."* **That is a regex-assigned target cluster, not
earned traffic.** `docs/research/for-sale-keywords-2026-07.md:3` states it plainly: *"Bucket assignment is
regex-based, first-match; treat as draft until per-page Sprint 0 refines it."* The real page-level rows:

| Page | Google window 1 (123 rows) | Google window 2 (76 rows) | On disk | Inbound links |
|---|---|---|---|---|
| `/african-grey-parrot-for-sale/` | 0 clk · **9** imp · pos 7.11 | **absent entirely** | 8,930 B · 3 H2 | 106 |
| `/african-grey-parrots-for-sale/` | 0 clk · **13** imp · pos 6.23 | **absent entirely** | 16,387 B · 7 H2 | 105 |

Both windows agree. **Neither page is a traffic asset to protect.** Any argument for keeping both must be made
on structure, not on rankings.

**Finding 1 — the site links them in lockstep.** 105 pages link to **both** slugs. Exactly **one** page links
to the singular but not the plural, and it is `404.html`. **Zero** pages link to the plural alone. This is the
cannibalisation engine: every real page on the site points at both slugs together.

**Finding 2 — 105 anchors point the wrong way.** The singular's dominant inbound anchor is **`Baby African
Grey for Sale` ×105**, emitted by `src/components/Footer.astro:46` on every page. It describes
`/baby-african-grey-parrot-for-sale/` — a separate, fully built 111,895 B page. The plural's anchors are
coherent by comparison (`Browse by State` ×210, `African Greys for Sale` ×115).

**Finding 3 — the plural page is ALREADY the near-me router, which collides with Task 9.** Its live headings:

> H1 African Grey Parrots for Sale Near You · H2 How Do You Find an African Grey Parrot for Sale Near You? ·
> H2 Find an African Grey Parrot for Sale in Your State · H2 African Grey Parrots for Sale by City

That is the exact job Task 9 assigns to `/african-grey-parrots-for-sale-near-me/`. Building near-me as
originally written would have created a fresh cannibalisation pair with the page intended to become the hub.
Task 9 Step 2 is amended accordingly: **the geo grid is enumerated in exactly one place.**

### 0g · The role split — decided 2026-08-10

| Slug | Role | Change |
|---|---|---|
| `/african-grey-parrots-for-sale/` (plural) | **The cluster HUB** — national inventory, `AggregateOffer`, links to every spoke | Rebuilt; **sheds** its state/city grid |
| `/african-grey-parrots-for-sale-near-me/` | **The geo ROUTER** — sole owner of the 22-state and city grid; keeps the 54-click 301 | Rebuilt (Task 9) |
| `/african-grey-parrot-for-sale/` (singular) | **RETIRED → 301 into the hub** | Its 3 H2s are a strict subset of the hub's job |
| `/buy-african-grey-parrots-with-shipping/` | Buy / buy-online cluster | Unchanged (Task 8) |

**WHY:** the singular has no traffic to lose in either window; its entire job (national inventory + "Current
Pricing" + "Inquire About Available African Greys") is what the hub must ship regardless; and its 106 inbound
links are worth more consolidated than split — especially the 105 footer links that currently mis-describe
their own destination. Splitting hub from geo-router also gives each page a head term matching its content:
the plural's term is national-commercial, the near-me's term is geographic by definition. Today the plural
page ranks a national term while serving geographic content.

**TRADE-OFF, named:** the plural holds position 6.23 and the singular 7.11 — both nominally page one.
Rebuilding one and 301'ing the other puts both through a re-crawl. Accepted because those positions produce
**0 clicks on 13 and 9 impressions**; it is the same reasoning that retired `/where-to-buy-african-greys-near-me/`
at position 8.74.

**REJECTED — keep both, singular as a standalone national money page.** 105 of its 106 linking pages link to
the plural too, and its regex bucket is full of plural-form queries (`african grey parrots sale`, `parrots
african grey for sale`), meaning Google does not separate them either. Two pages for one intent is exactly
what Gate 1 retired four near-me pages for.

**Sprint scope is therefore 3 builds + 1 retirement**, in this order:
**Task 8** buy-with-shipping → **Task 9** near-me (geo router) → **Task 13** the hub (+ singular retired into it).

---

## File Structure

| File | Responsibility |
|---|---|
| `scripts/final_page_audit.py` | **Modify** — `FORSALE` list: add the 2 targets + hub, drop the 3 consolidated |
| `tests/render/targets.json` | **Modify** — register both slugs as `for-sale` page type |
| `sessions/for-sale-research/buy-african-grey-parrots-with-shipping/2026-08-10-sprint0.md` | **Create** — Page A Sprint 0 |
| `sessions/for-sale-research/african-grey-parrots-for-sale-near-me/2026-08-10-sprint0.md` | **Create** — Page B Sprint 0 |
| `sessions/2026-08-10-two-pages-sprint05-strategy.md` | **Create** — 2 strategies + 1 blended per page, one (Recommended) |
| `sessions/2026-08-10-two-pages-outline-gate.md` | **Create** — H1–H6 outlines, both pages |
| `sessions/2026-08-10-two-pages-image-prompt-pack.md` | **Create** — infographic + OG prompt pack |
| `sessions/2026-07-19-for-sale-component-map.md` | **Modify** — append 2 tuple-ledger rows |
| `src/pages/buy-african-grey-parrots-with-shipping/index.astro` | **Rewrite** — Page A |
| `src/pages/african-grey-parrots-for-sale-near-me/index.astro` | **Rewrite** — Page B, the geo router |
| `src/pages/african-grey-parrots-for-sale/index.astro` | **Rewrite** — Page C, the cluster hub |
| `src/pages/african-grey-parrot-for-sale/` | **Delete** — 301 into the hub |
| `src/components/Footer.astro:46` | **Modify** — the `Baby African Grey for Sale` anchor points at the wrong page on all 105 pages |
| `sessions/for-sale-research/african-grey-parrots-for-sale/2026-08-10-sprint0.md` | **Create** — Page C Sprint 0 |
| `site/content/_redirects` + `public/_redirects` | **Modify** — 3 retirements + 1 chain flatten |
| `data/page-map.json` | **Modify** — 3 × `consolidated`, 2 × rebuild notes |
| `docs/research/competitor-sweep-page3-2026-08-09.md` | **Modify** — correct the "$1,500 Congo floor" sentence |
| `docs/superpowers/sessions/2026-08-10-two-pages-lessons.md` | **Create** — lessons doc |

---

## Task 1: Wire both pages into the gates before building anything

**Why first:** a gate that never examines a page cannot fail on it. Building first and measuring second is how
`african-grey-parrot-adoption-cost` shipped with zero in-body figures and five components whose CSS had no
markup behind it.

**Files:**
- Modify: `scripts/final_page_audit.py:359-372`
- Modify: `tests/render/targets.json`

- [ ] **Step 1: Prove the gate is blind — record the "before" number**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/final_page_audit.py --for-sale 2>&1 | tail -6
```

Expected: a summary line counting **13 targets**, three of them printing `dist/ MISSING`, and **no row for
`buy-african-grey-parrots-with-shipping` or `african-grey-parrots-for-sale-near-me`**. Copy that output into
the lessons doc as the before-state.

- [ ] **Step 2: Fix the `FORSALE` list**

In `scripts/final_page_audit.py`, replace the `FORSALE` assignment with:

```python
FORSALE = ["african-grey-parrot-bird-eggs-for-sale-usa",
           "congo-african-grey-for-sale",
           "timneh-african-grey-for-sale",
           "hand-raised-african-grey-parrot-for-sale",
           "dna-tested-african-grey-for-sale",
           "african-greys-for-sale-with-health-guarantee",
           # group of 7 — added 2026-07-27
           "baby-african-grey-parrot-for-sale",
           "african-grey-parrot-adoption-cost",
           "congo-african-grey-parrot-pair-for-sale",
           "african-grey-breeding-pair-for-sale",
           # 2026-08-10: the last two spokes + the hub they feed.
           # affordable- / grey-african-parrots- / male-african-gray- were REMOVED:
           # consolidated 2026-08-08, they 301 and have no dist/ output. They were
           # printing "dist/ MISSING" as if the build were broken.
           "buy-african-grey-parrots-with-shipping",
           "african-grey-parrots-for-sale-near-me",
           "african-grey-parrots-for-sale"]
```

- [ ] **Step 3: Run the gate again and confirm it now fails on the two stubs**

```bash
cd /Users/apple/Downloads/CAG && npx astro build >/dev/null 2>&1 && python3 scripts/final_page_audit.py --for-sale 2>&1 | grep -E "buy-african-grey-parrots-with-shipping|african-grey-parrots-for-sale-near-me"
```

Expected: three `[FAIL]` rows, and the summary moving from `0 PASS · 10 PASS-WITH-WARNINGS · 0 FAIL (of 13)`
to `0 PASS · 10 PASS-WITH-WARNINGS · 3 FAIL (of 13)`. **The before-state is the finding: the gate claimed 13
targets while examining 10, and reported zero failures because the two broken pages were not in its list.**
**If any row reports PASS, stop and read `skills/cag-gate-integrity.md` — a stub cannot pass this gate, so a
PASS means the check is broken, not the page.** Also confirm the three `dist/ MISSING` lines are gone.

**Actual result, 2026-08-10 — record these, they extend §0d:**

```
[FAIL] buy-african-grey-parrots-with-shipping   H1:1 H2:5 H3:10 H4:0 H5:0 H6:0
    FAIL → all_h1_h4, all_six_levels, min_h5_5, min_h6_5, shipping_line, real_hero_image, brand_in_title
[FAIL] african-grey-parrots-for-sale-near-me    H1:1 H2:2 H3:4  H4:0 H5:0 H6:0
    FAIL → all_h1_h4, all_six_levels, min_h5_5, min_h6_5, has_org, shipping_line, real_hero_image, brand_in_title
[FAIL] african-grey-parrots-for-sale            H1:1 H2:6 H3:8  H4:0 H5:0 H6:0
    FAIL → all_h1_h4, all_six_levels, min_h5_5, min_h6_5, has_org, shipping_line, real_hero_image
```

Four failures were **not** in the §0d catalogue and are now build requirements: **`shipping_line` fails on all
three** (the `$185 airport · $350 home` rule), **`real_hero_image` fails on all three**, **`has_org`** is
missing on the near-me page and the hub, and **`brand_in_title`** on the two spokes. Counts are read from
`dist/`, so they differ slightly from source greps — dist is the truth.

- [ ] **Step 4: Register both pages in the render harness**

In `tests/render/targets.json`, add to `pages`:

```json
    { "slug": "buy-african-grey-parrots-with-shipping", "page_type": "for-sale" },
    { "slug": "african-grey-parrots-for-sale-near-me",  "page_type": "for-sale" }
```

Entries take three keys — `slug`, `page_type`, `corpus` — and both of these get `"corpus": false`. `corpus:
true` marks the frozen benchmark sample, one page per page type; these are targets, not benchmarks.
`families_by_page_type["for-sale"]` already resolves to `IMG, LAYOUT, NAV, SEM, SCHEMA, CSS, DUP, A11Y`, so
no second switch needs touching.

**Do NOT add `african-grey-parrots-for-sale` here.** *(Recorded 2026-08-10 after doing exactly that.)* The hub
is **already registered**, as `{"slug": "african-grey-parrots-for-sale", "page_type": "hub", "corpus": true}`
— it is the frozen benchmark page for the `hub` page type, and `hub` maps to all eight families. Adding a
second `for-sale` row for it creates a duplicate slug and would shadow the benchmark. Verify after editing:

```bash
cd /Users/apple/Downloads/CAG && python3 -c "
import json,collections
d=json.load(open('tests/render/targets.json'))
c=collections.Counter(p['slug'] for p in d['pages'])
print('duplicates:',{k:v for k,v in c.items() if v>1} or 'none')"
```

Expected: `duplicates: none`. Task 13 inherits this — the hub needs **no** targets.json edit.

- [ ] **Step 5: Run the meta gate — the gate that checks the checkers**

```bash
cd /Users/apple/Downloads/CAG && npm run test:render:meta
```

Expected: PASS. If it fails, the fixture set caught the edit — fix the check, not the page.

- [ ] **Step 6: Commit**

```bash
git add scripts/final_page_audit.py tests/render/targets.json && git commit -m "fix(gates): the two unbuilt for-sale pages were invisible to both harnesses

final_page_audit FORSALE never listed buy-with-shipping, parrots-for-sale-near-me
or the hub, and still listed three slugs consolidated on 2026-08-08 — which is
what the three 'dist/ MISSING' lines were. tests/render/targets.json had the same
hole. Both stubs now FAIL as they should.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" && git push origin main
```

---

## Task 2: Sprint 0 deep research — Page A, `/buy-african-grey-parrots-with-shipping/`

**Files:**
- Create: `sessions/for-sale-research/buy-african-grey-parrots-with-shipping/2026-08-10-sprint0.md`
- Read (do not re-derive): `docs/research/for-sale-keywords-2026-07.md:338`, the Gate-1 artifact §2, `docs/research/competitor-sweep-page1-2026-08-09.md`, `competitor-sweep-page2-2026-08-09.md`

**The target the research must serve:** the page keeps its URL and its shipping content, but the **search
target moves** to the buy / buy-online cluster — 40 queries, 443 impressions, 1 click, positions 34–80, owned
by nobody on this site. Shipping intent is 0 queries / 0 clicks / 0 impressions across all 792 Google query
rows and stays as trust content only.

- [ ] **Step 1: SERP snapshot, top 10, both queries**

Use Firecrawl Search (US locale) for `buy african grey parrot online` and `buy african grey parrot`. Record
per result: URL, title, meta description, H1, and the **ordered list of its H2s**. Write a table. Any result
that will not fetch is written `NOT FETCHED` with the barrier named — never inferred.

- [ ] **Step 2: Section + visual inventory of the top 5**

For each of the top 5, list every section in document order with: section purpose, whether it carries an
image, image type (product photo / infographic / stock), and whether it carries a price. This is the artefact
Gate 1 explicitly deferred; it is what makes the distribution matrix in Task 4 evidence-based rather than
taste-based.

- [ ] **Step 3: PAA to three levels + autosuggest**

Expand the People-Also-Ask box for both queries three levels deep; record every question with its parent.
Capture Google autosuggest for `buy african grey `, `buy african gray `, `african grey parrot buy `. Target
≥25 distinct questions. These become the H4 layer and the FAQ set.

- [ ] **Step 4: Reuse the competitor evidence already banked — do NOT re-fetch**

Pull from the existing sweeps into this doc, each with its source line:
- `exoticglobalparrotsfarm.com/shipping/` (#4) and `williamsafricangreys.com/shipping/` (#8, *"free shipping on all parrot purchases"*) — shipping-as-trust-page precedent.
- theavianexchange's **"Ships to You"** listing badge — shipping as a *badge*, not a page.
- The live price ladder from sweep 1 §"Price ladder measured this pass".
- The health-guarantee window comparison from sweep 1.
- Reddit verbatims from sweep 3 §C4 — the ledger says **do not re-mine**; quote from it. The load-bearing ones for this page: *"Almost all bird shippers are scams and those prices are way too low"* [249] and the non-refundable-deposit-as-scam-signal thread [74].

- [ ] **Step 5: Entity map (85–112 distinct entities) + gap table**

Group as: birds by name (Bery, Amie, Roys, Jins & Jeni, Elad, Evie) · geo (Midland TX + the 4–5 states this
page owns) · credentials (CITES Appendix I, USDA AWA #74-B-0247, DNA sexing, PBFD/Polyomavirus PCR) · carriers
(Delta, United, American, Alaska, IATA LAR) · money ($185 airport, $350 home, $1,500 site floor, $1,700 Congo
floor). Every health/credential entity must be traceable to the Verified-Claim Ledger; anything not in it is
not assertable.

- [ ] **Step 6: Write the doc and commit**

```bash
mkdir -p sessions/for-sale-research/buy-african-grey-parrots-with-shipping
```

Then write the file and:

```bash
git add sessions/for-sale-research/buy-african-grey-parrots-with-shipping/ && git commit -m "research(sprint0): buy-with-shipping — the page ranks on borrowed relevance

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" && git push origin main
```

---

## Task 3: Sprint 0 deep research — Page B, `/african-grey-parrots-for-sale-near-me/`

**Files:**
- Create: `sessions/for-sale-research/african-grey-parrots-for-sale-near-me/2026-08-10-sprint0.md`
- Read: `docs/research/for-sale-keywords-2026-07.md:402`, Gate-1 artifact §3, `docs/research/competitor-sweep-page3-2026-08-09.md` §C2 (state coverage)

**The target the research must serve:** a **routing hub**, not a fourth attempt at ranking a generic national
page. It catches the grey/gray and singular/plural variance across the 55-query / 575-impression cluster and
hands the buyer to one of the 22 location pages. It also becomes the landing page for a **54-click** 301.

- [ ] **Step 1: SERP snapshot + local-pack composition**

Firecrawl Search for `african grey parrot for sale near me` and `african grey breeders near me`. Beyond the
ten organic results, record **what the local pack shows** — how many entries, whether they are stores,
rescues, or breeders, and whether any is a national seller. Gate 1 established the SERP is classifieds and
local businesses; this step establishes whether a national routing page can appear at all, and where.

- [ ] **Step 2: Section inventory of the regional pages that DO rank**

Birds By Joe (NJ), Midnight Parrot Place (IL), NW Parrot Rescue (WA), Denise's Parrot Place (WA). For each:
ordered H2 list, whether they show inventory with prices, whether they name a service radius, and how they
express locality. A regional page that outranks us is showing us what "near me" content looks like when it
works.

- [ ] **Step 3: PAA three levels + autosuggest across the variance axis**

Run PAA and autosuggest for all four spellings: `african grey`/`african gray` × `parrot`/`parrots` + near me.
The whole point of the page is that these are one intent; the research has to prove the question sets overlap
rather than assume it.

- [ ] **Step 4: Audit our own 22 location pages as routing destinations**

```bash
cd /Users/apple/Downloads/CAG && ls -d src/pages/african-grey-parrot-for-sale-* | sed 's|.*for-sale-||' | tr '\n' ' '
```

Expected: 22 slugs. For each, record the state or metro and confirm the slug resolves in `dist/`. Cross-check
against sweep 3 §C2 "State coverage against the canonical 22" so the routing grid claims only coverage we
actually have. A routing hub that links to a 404 is worse than no routing hub.

- [ ] **Step 5: Redirect-equity map**

Document the four inbound sources this page will hold after Task 11: the legacy `/product/…` 301 (54 clicks /
722 impressions, confirmed in both Google windows at 54/722 and 53/713), plus the three retiring siblings
(1 + 3 + 5 = 9 inbound internal links, taking the page from 2 to 11). Name every one of the 9 links by source
page so Task 11 can repoint them without a second search.

- [ ] **Step 6: Entity map + geo split that does not collide with Page A**

Page A and Page B must not own the same states. Record the split explicitly. Page B, as the routing hub, cites
many states shallowly; Page A owns 4–5 deeply. Check both against the geo sets already spent by the built
siblings (health-guarantee: TX/OH/CO/NC/GA/MI/PA/VA · baby: CA/TX/WA/FL/NY/IL/GA/AZ · adoption-cost:
NJ/MA/MN/MO/OR/IN).

- [ ] **Step 7: Write and commit**

```bash
mkdir -p sessions/for-sale-research/african-grey-parrots-for-sale-near-me
```

```bash
git add sessions/for-sale-research/african-grey-parrots-for-sale-near-me/ && git commit -m "research(sprint0): parrots-for-sale-near-me — 54 clicks arriving at a 1-H2 stub

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" && git push origin main
```

---

## Task 4: Sprint 0.5 — two strategies plus a blend per page, one (Recommended)

**Files:**
- Create: `sessions/2026-08-10-two-pages-sprint05-strategy.md`

- [ ] **Step 1: Write three strategies per page**

For each page: Strategy 1, Strategy 2, Blended. Each carries an angle, a structure, a primary framework stack,
and a named voice lever. Mark exactly **one (Recommended)** per page, justify it from the Sprint 0 data by
citing the specific table or query row, and **name the trade-off of the recommended pick** — CLAUDE.md rule 5.

Anchors the research already supports, to be argued for or against rather than assumed:
- **Page A** — the *"the ranking exists on borrowed relevance"* angle: it holds 789 impressions at position 15.28 for queries it does not target. The blend is buy-intent structure with the shipping content retained as the proof layer.
- **Page B** — the *"near me is 22 pages, not one page"* angle: route rather than rank. The trade-off to name is that a routing page has a lower ceiling on its own head term than a content page would.

- [ ] **Step 2: Distribution matrix per page**

Every section tagged **MANDATORY** / **COMPETITOR-BASED** / **SUGGESTED-RECOMMENDED**, each with a grounded
why that cites Sprint 0. COMPETITOR-BASED rows must name the competitor and the sweep line.

- [ ] **Step 3: Keyword distribution table per page**

Fill the §2a targets (primary 30–35 · LSI 20–25 · long-tail 15–20 · branded 10–15 · conversational ~23 ·
comparison 5–8 · solution 5–10 · transactional ~15) from the real query buckets — Page A from the 40-query
buy cluster, Page B from the 55-query near-me cluster. **Never invent a keyword.**

- [ ] **Step 4: Present to the breeder and record the decision**

Present as an Artifact per CLAUDE.md rule 13, sections carrying copy buttons, plus the `.md`. Record the
breeder's pick in the doc, then commit.

---

## Task 5: H1–H6 outline gate + header dup-gate — both pages

**Files:**
- Create: `sessions/2026-08-10-two-pages-outline-gate.md`

- [ ] **Step 1: Draft the full outline for each page**

Complete H1→H6, no skipped levels, **≥5 H5 and ≥5 H6** each. Semantic map: H1 topic · H2 search intents ·
H3 subtopics · H4 PAA/micro-intents · H5 supporting facts and warnings · H6 breeder notes and citations.
Every header Title Case (AP style) except FAQ `<summary>`, which stays conversational. Two-Keyword Headers
rule applies. Draft **5 A/B variants** for the H1 and each major H2; the breeder picks.

Page B needs an H6 prefix family that no sibling has spent — health-guarantee used *In Writing: / From the
Vet: / On File:*, baby used *At Week N: / From the Nursery: / Weaning Log:*, adoption-cost used *Line Item: /
From the Ledger: / Receipt Note:*. Pick fresh ones and record them.

- [ ] **Step 2: Dup-gate the headers BEFORE approval, not after**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/dup_content_audit.py --headers 2>&1 | grep -iE "near-me|with-shipping" | head -40
```

Expected: **zero** non-whitelist header crossover against all sibling for-sale pages, the comparison cluster,
and the variant pages. Whitelist is furniture only — shipping line, doc-badge lists, counter strip, CITES
notice, CTA labels, real page-name link labels.

- [ ] **Step 3: Verify the outline satisfies the gate arithmetic before any code**

Count H5s and H6s in the outline document itself. If either is below 5, fix it here — adding depth at the
outline stage costs minutes; adding it to a built page costs a rebuild.

- [ ] **Step 4: Breeder approval gate — HARD STOP**

No page code is written until the breeder approves both outlines. Ship as an Artifact + `.md`.

---

## Task 6: Lock the component tuple for each page

**Files:**
- Modify: `sessions/2026-07-19-for-sale-component-map.md` (append two ledger rows)

**The ledger's standing assignments for these two pages** (`sessions/2026-07-19-for-sale-component-map.md:10-12,
17-18, 76`):

- Buy-prefixed 5 → **Split-Hero A · image left + trust ribbon**. Already spent once by health-guarantee, so Page A ships a **refresh delta**, not the raw shell.
- Hub + near-me → **Hero-C · Mosaic Metrics**. Spent once by dna-tested → Page B ships a refresh delta.
- **Rail B green ticker** rotates onto hub/near-me pages — Page B's default.
- **T3 Boarding-Pass** was reserved for shipping-heavy pages only (*"buy-with-shipping, near-me"*) but was **spent first** by the breeding-pair page. Page A therefore refreshes T3 rather than claiming a first use. **Verify this against the built breeding-pair page before relying on it** — the ledger has been wrong before, which is why the dna-tested row carries its own correction note.

- [ ] **Step 1: Verify T3's true status against the built page, not the ledger**

```bash
cd /Users/apple/Downloads/CAG && grep -l "boarding\|bpass" dist/*/index.html 2>/dev/null | head
```

Record what you find. If T3 is genuinely unused in `dist/`, Page A may claim first use.

- [ ] **Step 2: Pick and record both tuples**

Each tuple is `{hero variant, dial + rail, TOC, takeaway, table style, FAQ style}` and **no two sibling pages
may ship an identical combo**. Append one row per page to the ledger table with the same column shape as the
existing rows, including the differentiation rationale.

- [ ] **Step 3: Commit the ledger rows**

---

## Task 7: Visual companion, image prompt pack, and the image HARD STOP

**Files:**
- Create: `sessions/2026-08-10-two-pages-image-prompt-pack.md`
- Create: `sessions/visual-companion-buy-with-shipping.html`, `sessions/visual-companion-near-me.html`

- [ ] **Step 1: Build skeleton-screen visual companions for both pages**

Browser-mockup companions are the default workflow here. Skeletons only — layout and component placement, no
final copy.

- [ ] **Step 2: Write the image prompt pack**

Every H2, H3, and key H4 needs an image (OG photo or infographic). Reuse the two banked shipping prompts from
the skill verbatim for Page A's airport and home-delivery slots. Page B needs a routing/map-flavoured
infographic set that does not repeat the adoption-cost price-ladder motif or the baby-page weaning timeline.
Rule 50b: **no two images on a page share an alt**.

- [ ] **Step 3: HARD STOP**

Do not begin Task 8 until the breeder has dropped the images and said explicitly to start. This stop is in the
skill's Phase 2 and is not optional.

---

## Task 8: Build Page A — `/buy-african-grey-parrots-with-shipping/`

**Files:**
- Rewrite: `src/pages/buy-african-grey-parrots-with-shipping/index.astro`

- [ ] **Step 1: Write the prose fresh from the approved outline**

Do not open a sibling for-sale page to copy paragraphs. Open siblings only for component and CSS structure.
Every H2/H3/H4 opens with an **EFBP** sentence pair in first-person breeder voice. Reuse the `.xsell`,
`.availB`, `.otA`, `.fs-nl`, `.read-cards`, `.seam` component classes from the kit.

- [ ] **Step 2: Fix the six confirmed defects from §0d as you build**

1. Resolve the cargo-hold vs cabin contradiction — pick the true one, and make the FAQ schema and the Delivery Options card say the same thing.
2. Add `$350` to the Home Delivery card; every card carries `Ships nationwide · $185 airport · $350 home`.
3. Replace all four `text-gold` / `border-gold/30` with DESIGN.md tokens (clay, with `--clay-ink` fills and `#b04228` for small clay on light).
4. Replace the six WordPress town strings with real linked `/african-grey-parrot-for-sale-<state>/` destinations from the geo set Task 3 Step 6 assigned to this page.
5. Add bird cards from `data/clutch-inventory.json` with prices from `data/price-matrix.json` — never hardcoded.
6. Add the two-column contact form listing every reservable bird with its price, plus the delivery select including `Pickup in Midland, TX — if you live within 2–3 hours of us`.

- [ ] **Step 3: Schema**

One `Product` + `Offer` per real available bird. `AggregateOffer` only if the page presents the flock as a
group. Sold birds are never `InStock`. Extend the existing JSON-LD; never emit a second block of the same type.

- [ ] **Step 4: CTA cadence and seam parity**

A reserve/inquire CTA every 500–700 words, `hideGlobalCta` set since the page ships its own band. Then:

```bash
cd /Users/apple/Downloads/CAG && f=src/pages/buy-african-grey-parrots-with-shipping/index.astro && echo "seams=$(grep -c 'class="seam"' $f) sections=$(grep -c '<section class="sec"' $f)"
```

Expected: the two numbers match. A page with 7 seams across 17 sections reads as unfinished — that is the
health-guarantee lesson.

- [ ] **Step 5: Build and verify in `dist/`, never in source**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5 && python3 scripts/final_page_audit.py --for-sale 2>&1 | grep -A2 "buy-african-grey-parrots-with-shipping"
```

Expected: `[PASS]` or `[PASS-WITH-WARNINGS]`. `min_h5_5` and `min_h6_5` must no longer appear in the fail list.

- [ ] **Step 6: Commit and push — push is deploy**

```bash
git add src/pages/buy-african-grey-parrots-with-shipping/index.astro && git commit -m "build(for-sale): buy-with-shipping retargeted at the buy cluster, shipping demoted to proof

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" && git push origin main
```

---

## Task 9: Build Page B — `/african-grey-parrots-for-sale-near-me/`

**Files:**
- Rewrite: `src/pages/african-grey-parrots-for-sale-near-me/index.astro`

- [ ] **Step 1: Write the prose fresh from the approved outline**

Same discipline as Task 8 Step 1. This page's own angle is **routing**, not inventory-first — its distinctive
content is the state grid, the service-radius honesty (Midland pickup within 2–3 hours; everywhere else
flies), and the variance capture.

- [ ] **Step 2: Build the routing grid — and make this the ONLY place it is enumerated**

Every one of the 22 location pages verified in Task 3 Step 4 gets a real link. No link may 404. This is the
component the page exists for.

**Amended 2026-08-10 (§0f Finding 3):** `/african-grey-parrots-for-sale/` currently ships this exact grid
under `H2 Find an African Grey Parrot for Sale in Your State` and `H2 African Grey Parrots for Sale by City`.
It **sheds** that grid in Task 13. The two pages must not both enumerate states — the hub links to *this*
page for geography and to the location hub, and enumerates nothing itself. Verify after Task 13 ships:

```bash
cd /Users/apple/Downloads/CAG && for p in african-grey-parrots-for-sale-near-me african-grey-parrots-for-sale; do echo "$p: $(grep -o 'african-grey-parrot-for-sale-[a-z-]*/' dist/$p/index.html | sort -u | wc -l) state links"; done
```

Expected: the near-me page reports **22**; the hub reports a small single-digit number (its own cross-links),
never 22.

- [ ] **Step 3: Fix the two confirmed defects from §0d**

6. Timneh price becomes `$1,500–$1,600` from `data/price-matrix.json`. Congo stays `$1,700–$3,500`. Delete the unsourced `$1,200`.
7. Replace `#f0c674` with the DESIGN.md token.

- [ ] **Step 4: Bird cards, schema, form, CTA cadence, seam parity**

Identical requirements to Task 8 Steps 2.5, 2.6, 3 and 4. Run the same seam-parity check against this file.

- [ ] **Step 5: Build and verify**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5 && python3 scripts/final_page_audit.py --for-sale 2>&1 | grep -A2 "african-grey-parrots-for-sale-near-me"
```

Expected: `[PASS]` or `[PASS-WITH-WARNINGS]`, `H2` well above 1, `H5`/`H6` both ≥5.

- [ ] **Step 6: Commit and push**

```bash
git add src/pages/african-grey-parrots-for-sale-near-me/index.astro && git commit -m "build(for-sale): parrots-for-sale-near-me rebuilt as the routing hub the 54-click 301 lands on

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" && git push origin main
```

---

## Task 10: Phase-4 QA on both pages

- [ ] **Step 1: Dup-gate, body and headers, both pages**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/dup_content_audit.py 2>&1 | grep -iE "near-me|with-shipping" | head -40
```

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/dup_content_audit.py --headers 2>&1 | grep -iE "near-me|with-shipping" | head -40
```

Expected: only whitelist furniture matches. **Verify every hit against the flagged rule before editing** — the
dup gate produced 23 legitimate-furniture false alarms on 2026-07-26.

- [ ] **Step 2: Hardening scan, both pages**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/page_hardening_scan.py buy-african-grey-parrots-with-shipping && python3 scripts/page_hardening_scan.py african-grey-parrots-for-sale-near-me
```

Confirm each reported defect on the built page before fixing it. Four checkers cried wolf on 2026-07-26.

- [ ] **Step 3: Render harness at three widths, run TWICE**

```bash
cd /Users/apple/Downloads/CAG && npm run test:render:meta && npm run test:render:pages
```

Then run `test:render:pages` a second time. **One clean run proves nothing** — same input, different verdict
is a documented failure mode on this harness.

- [ ] **Step 4: Manual gate list**

400px-class heroes · unique newsletter image and one-liner per page, shared with nothing · opening paragraph
under every header · uniform `.sec-img.inf-img` 760px 16:9 boxes · separate blog and contact H2s · mobile
table stacking (`caption` in the `display:block` list) · jump-rail `scroll-margin` with `scroll-behavior:auto`
· further-reading cards whose thumbnails are **the target page's own hero** · AA contrast.

- [ ] **Step 5: Voice and originality sweep**

First-person brand voice throughout (`we / us / our / here at C.A.Gs`), neutral register only for species
facts and cited research. Run the anti-ai-writing filter and the non-commodity check. Confirm CITES reads
**Appendix I** everywhere on both pages. Leave both "72-hour" and "3-day" guarantee phrasings alone — they are
the same guarantee said two ways and neither is a defect.

- [ ] **Step 6: Perf, median of warm runs**

Lighthouse warm median-of-3 minimum; if any CLS conclusion is going to be drawn, take **5 runs** — CLS on this
site is bimodal and a single run has already produced one confidently wrong attribution.

---

## Task 11: Execute the three retirements — only after Page B is live

**Order is the whole point:** the 54 redirected clicks and the consolidated equity must arrive at a finished
page, not at the stub. Do not start this task until `/african-grey-parrots-for-sale-near-me/` returns 200 with
the rebuilt content.

**Files:**
- Modify: `site/content/_redirects`, `public/_redirects`
- Modify: `data/page-map.json`
- Delete: `src/pages/where-to-buy-african-greys-near-me/`, `src/pages/buy-african-grey-parrot-near-me/`, `src/pages/african-grey-parrot-for-sale-near-me/`

- [ ] **Step 1: Confirm Page B is live and rebuilt**

```bash
curl -s https://congoafricangreys.com/african-grey-parrots-for-sale-near-me/ | wc -c
```

Expected: an order of magnitude above the 5,583-byte stub. If it still reads small, the deploy has not landed
— wait, do not proceed.

- [ ] **Step 2: Flatten the existing chain first**

`public/_redirects` and `site/content/_redirects` lines 102–103 currently send
`/african-gray-parrots-for-sale-near-me/` (12 impressions) to `/african-grey-parrot-for-sale-near-me/`, which
is being retired. Repoint both lines directly at `/african-grey-parrots-for-sale-near-me/` **before** adding
the new rules, or the result is an A→B→C chain.

- [ ] **Step 3: Add the three 301s to both redirect files**

```
/where-to-buy-african-greys-near-me    /african-grey-parrots-for-sale-near-me/ 301
/where-to-buy-african-greys-near-me/   /african-grey-parrots-for-sale-near-me/ 301
/buy-african-grey-parrot-near-me       /african-grey-parrots-for-sale-near-me/ 301
/buy-african-grey-parrot-near-me/      /african-grey-parrots-for-sale-near-me/ 301
/african-grey-parrot-for-sale-near-me  /african-grey-parrots-for-sale-near-me/ 301
/african-grey-parrot-for-sale-near-me/ /african-grey-parrots-for-sale-near-me/ 301
```

Both files must stay identical — `site/content/_redirects` is the source, `public/_redirects` is the synced
copy. Preserve the www→non-www rule.

- [ ] **Step 4: Repoint the 9 inbound internal links**

Use the by-source list built in Task 3 Step 5. Rewrite the anchor text wherever the old sentence no longer
describes the destination — a link labelled "where to buy near me" pointing at a routing hub is fine; one
labelled with a retired page's title is not. Draw new anchors from the Anchor Diversity Ledger so no anchor
repeats site-wide.

- [ ] **Step 5: Remove the three pages and update the data files**

```bash
cd /Users/apple/Downloads/CAG && rm -rf src/pages/where-to-buy-african-greys-near-me src/pages/buy-african-grey-parrot-near-me src/pages/african-grey-parrot-for-sale-near-me
```

Then, in `data/page-map.json`, set each of the three to `"status": "consolidated"`, `"redirects_to":
"/african-grey-parrots-for-sale-near-me/"`, and a `notes` string carrying the measured reason and an explicit
do-NOT-rebuild — matching the shape of the `grey-african-parrots-for-sale` entry written on 2026-08-08. Drop
the three from `TIER_09`, and clear their entries from `data/page-dates.json`.

- [ ] **Step 6: Regenerate sitemaps and build**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/generate_sitemaps.py && npx astro build 2>&1 | tail -5
```

- [ ] **Step 7: Verify in `dist/` before pushing**

```bash
cd /Users/apple/Downloads/CAG && ls dist/where-to-buy-african-greys-near-me dist/buy-african-grey-parrot-near-me dist/african-grey-parrot-for-sale-near-me 2>&1 | head
```

Expected: all three "No such file or directory". Confirm no remaining internal link points at them:

```bash
cd /Users/apple/Downloads/CAG && grep -rl "where-to-buy-african-greys-near-me/\"\|buy-african-grey-parrot-near-me/\"\|african-grey-parrot-for-sale-near-me/\"" dist/ | head
```

Expected: no output. (`african-grey-parrots-for-sale-near-me` — plural — will not match these patterns.)

- [ ] **Step 8: Commit, push, and verify live cache-busted**

```bash
git add -A src/pages data/page-map.json data/page-dates.json site/content/_redirects public/_redirects public/sitemap* && git commit -m "consolidate(gate-1): retire three near-me stubs into the rebuilt routing hub

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" && git push origin main
```

After the deploy lands, verify **without** `-L` so a 301 reads as a 301:

```bash
for u in where-to-buy-african-greys-near-me buy-african-grey-parrot-near-me african-grey-parrot-for-sale-near-me; do curl -s -o /dev/null -w "%{http_code} %{redirect_url}\n" "https://congoafricangreys.com/$u/?cb=$RANDOM"; done
```

Expected: `301 https://congoafricangreys.com/african-grey-parrots-for-sale-near-me/` three times.

---

## Task 12: IndexNow, data hygiene, and the corrections this plan owes other files

- [ ] **Step 1: IndexNow — every slug whose RENDERED output changed**

Only after the deploy is live and each URL returns its final status:

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/indexnow_submit.py buy-african-grey-parrots-with-shipping african-grey-parrots-for-sale-near-me where-to-buy-african-greys-near-me buy-african-grey-parrot-near-me african-grey-parrot-for-sale-near-me
```

Then submit every page carrying a repointed internal link from Task 11 Step 4. The script's live check follows
redirects and will print `200` for a `301` — that is known and is not a bug to fix. Confirm the retired slugs
separately with the no-`-L` curl above.

- [ ] **Step 2: Correct the sweep-3 price sentence**

In `docs/research/competitor-sweep-page3-2026-08-09.md` §C4, the line asserting *"$1,500 — exactly CAG's Congo
floor"* is wrong: `data/price-matrix.json` puts the Congo floor at $1,700. Rewrite it to say the community's
named minimum matches **C.A.Gs' site-wide floor** ($1,500, Evie, Timneh), and that the Congo floor is $1,700.
The argument survives the correction; the number does not.

- [ ] **Step 3: Update the page-map entries for the two rebuilt pages**

Record for each: rebuild date, the new primary keyword (Page A moves from `buy african grey parrot with
shipping` to the buy/buy-online cluster head term), and the component tuple.

- [ ] **Step 4: Write the lessons doc**

Create `docs/superpowers/sessions/2026-08-10-two-pages-lessons.md`. It must carry, at minimum: the
harness-blindness finding from Task 1 with the before/after gate output, whichever gate findings turned out to
be false alarms, and the component-refresh deltas chosen in Task 6 so the hub build does not re-spend them.

- [ ] **Step 5: Save memory**

Write a `project` memory for the two builds (tuple + angle + geo split + reusable patterns) and a `reference`
memory for the harness-blindness pattern if it is not already covered by `reference_registered_is_not_wired`.
Update `MEMORY.md` with a one-line pointer for each. Check for an existing file that already covers it before
creating a new one.

- [ ] **Step 6: Commit**

---

## Task 13: Build Page C — the cluster hub `/african-grey-parrots-for-sale/` — and retire the singular into it

**Runs last, by design.** The hub links every spoke, so it is built once the spokes are final. Do not start
until Tasks 8–12 are done and both rebuilt spokes return 200 live.

**Files:**
- Create: `sessions/for-sale-research/african-grey-parrots-for-sale/2026-08-10-sprint0.md`
- Rewrite: `src/pages/african-grey-parrots-for-sale/index.astro`
- Delete: `src/pages/african-grey-parrot-for-sale/`
- Modify: `src/components/Footer.astro:46` · `site/content/_redirects` + `public/_redirects` · `data/page-map.json`

- [ ] **Step 1: Sprint 0 for the hub**

Same protocol as Tasks 2–3, aimed at `african grey parrots for sale` and `african greys for sale`. Additional
hub-specific work: inventory how the ranking competitors structure a *category* page versus a *listing* page,
and record which of our own 21 spokes each competitor has an equivalent of. Reuse the banked sweeps; do not
re-mine Reddit. The keyword bucket for this slug is at `docs/research/for-sale-keywords-2026-07.md:460` —
**29 queries / 1,370 impressions, regex-assigned, draft.** Treat it as a target list, not as earned traffic;
§0f explains why that distinction cost this plan a correction already.

- [ ] **Step 2: Outline, tuple, visual companion, images**

The hub goes through the same gates as the spokes: H1–H6 outline (≥5 H5, ≥5 H6) + header dup-gate before
approval, a tuple recorded in the ledger that no sibling has spent, visual companion, then the image HARD
STOP. The ledger assigns **Hero-C Mosaic Metrics** to the hub group; dna-tested spent it once, so the hub
ships a refresh delta.

- [ ] **Step 3: Build the hub — inventory and spokes, NOT geography**

Required: every available bird from `data/clutch-inventory.json` with prices from `data/price-matrix.json`;
**`AggregateOffer`** (hub pages take AggregateOffer, never per-bird `Offer` — that is the spoke pattern); a
link to every one of the 21 spokes with anchors drawn from the Anchor Diversity Ledger; the contact form; the
CTA cadence; seam parity.

**Removed from the current page:** the `Find an African Grey Parrot for Sale in Your State` and `African Grey
Parrots for Sale by City` grids. Geography now lives on `/african-grey-parrots-for-sale-near-me/` (Task 9
Step 2). The hub carries one link to that page for geographic intent and enumerates no states itself.

**Absorbed from the singular page:** its "Current Pricing" and "Inquire About Available African Greys" jobs.
Write the prose fresh from the hub's own outline — do not paste the singular page's copy across, or the
dup-gate will catch it and the Write-From-Outline rule will have been broken either way.

- [ ] **Step 4: Fix the 105 mis-described footer anchors**

In `src/components/Footer.astro:46`, the link labelled `Baby African Grey for Sale` points at
`/african-grey-parrot-for-sale/`. Repoint it at the page it names:

```html
        <li><a href="/baby-african-grey-parrot-for-sale/" class="text-white/80 hover:text-clay transition-colors">Baby African Grey for Sale</a></li>
```

Check `src/components/Header.astro` for the same defect before moving on — it also references these slugs.
This single edit changes the rendered output of every page on the site, which matters for Step 8's IndexNow
submission.

- [ ] **Step 5: Build, verify, push the hub BEFORE the redirect**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5 && python3 scripts/final_page_audit.py --for-sale 2>&1 | grep -A2 "^\[.*\] african-grey-parrots-for-sale "
```

Expected: `[PASS]` or `[PASS-WITH-WARNINGS]`. Then commit and push, and confirm the live page is the rebuilt
one before Step 6 — same discipline as Task 11 Step 1. Equity must arrive at a finished page.

- [ ] **Step 6: Retire the singular into the hub**

Add to both `site/content/_redirects` and `public/_redirects`:

```
/african-grey-parrot-for-sale    /african-grey-parrots-for-sale/ 301
/african-grey-parrot-for-sale/   /african-grey-parrots-for-sale/ 301
```

**Check for chains before adding** — any existing rule whose target is `/african-grey-parrot-for-sale/` must
be repointed at the hub directly:

```bash
cd /Users/apple/Downloads/CAG && grep -n "african-grey-parrot-for-sale/ *$\|african-grey-parrot-for-sale/ 301" site/content/_redirects
```

Then repoint the 106 inbound internal links. 105 of them are the Footer link already fixed in Step 4; the
remaining one is `404.html`. Verify nothing is left:

```bash
cd /Users/apple/Downloads/CAG && npx astro build >/dev/null 2>&1 && grep -rl 'href="/african-grey-parrot-for-sale/"' dist/ | head
```

Expected: no output.

- [ ] **Step 7: Remove the page and update the data files**

```bash
cd /Users/apple/Downloads/CAG && rm -rf src/pages/african-grey-parrot-for-sale
```

In `data/page-map.json`, set `/african-grey-parrot-for-sale/` to `"status": "consolidated"`, `"redirects_to":
"/african-grey-parrots-for-sale/"`, and a `notes` string recording the measured reason — **0 clicks on 9
impressions in window 1, absent from window 2 entirely; 105 of its 106 inbound links also pointed at the hub;
its dominant anchor described a different page** — plus an explicit do-NOT-rebuild. Drop it from `TIER_09` and
clear `data/page-dates.json`.

**Do not touch `FORSALE` in `scripts/final_page_audit.py` here.** `/african-grey-parrot-for-sale/` was never
in that list — Task 1 added the *plural* hub, not the singular — so there is nothing to remove and the list
stays at 13. Adding it and then deleting the page is precisely how the three `dist/ MISSING` lines got there
in the first place.

- [ ] **Step 8: Sitemaps, deploy, verify, IndexNow**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/generate_sitemaps.py && npx astro build 2>&1 | tail -3
```

Push, then verify the 301 without `-L` so a redirect reads as a redirect:

```bash
curl -s -o /dev/null -w "%{http_code} %{redirect_url}\n" "https://congoafricangreys.com/african-grey-parrot-for-sale/?cb=$RANDOM"
```

Expected: `301 https://congoafricangreys.com/african-grey-parrots-for-sale/`.

Because Step 4 changed the global footer, **every page's rendered output changed** — submit the whole site,
not just the hub:

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/indexnow_submit.py --all
```

---

## Task 14: Cluster close-out

- [ ] **Step 1: Re-run the full for-sale gate and record the final state**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/final_page_audit.py --for-sale 2>&1 | tail -20
```

Expected: **13** targets — the count is unchanged from Task 1, because the singular was never in the list —
zero `dist/ MISSING`, and all three rebuilt pages passing.

- [ ] **Step 2: Confirm the cannibalisation is actually gone**

```bash
cd /Users/apple/Downloads/CAG && for p in african-grey-parrots-for-sale african-grey-parrots-for-sale-near-me buy-african-grey-parrots-with-shipping; do echo "$p → $(grep -o 'african-grey-parrot-for-sale-[a-z-]*/' dist/$p/index.html | sort -u | wc -l) state links"; done
```

Expected: near-me **22**, hub and shipping page small single digits. If two pages both report 22, the geo grid
was duplicated and Task 9 Step 2's amendment was not applied.

- [ ] **Step 3: Update the lessons doc with the singular/plural finding**

Add to `docs/superpowers/sessions/2026-08-10-two-pages-lessons.md`: the regex-bucket-vs-earned-traffic
correction (a draft keyword bucket was read as page traffic and nearly justified building a fourth page), the
105/105 lockstep-linking test as a reusable cannibalisation probe, and the footer-anchor defect class — a
global component anchor that names one page and links to another, multiplied across the whole site.

- [ ] **Step 4: Save memory**

A `reference` memory for the lockstep-linking probe and for "regex-assigned keyword buckets are a target list,
not earned traffic — always cross-check the page-level GSC row in both windows." A `project` memory for the
final cluster shape. Update `MEMORY.md`. Check for an existing file covering each before creating a new one.

- [ ] **Step 5: Commit**

---

## Open Flags

1. ~~**Gate-1 approval is the one blocking answer needed before Task 2.**~~ **RESOLVED 2026-08-10 — breeder approved as written: build both, retire three into Page B.** Do not re-raise. Original text kept for the record: the verdict had been written since 2026-08-09 but never approved, and nothing had been executed. Tasks 2–13 all assume approval. **(Recommended: approve as written.)** WHY: the near-me survivor is already the settled 301 target of the 54-click legacy URL, and §4a of the build brief warns against reversing a settled 301 — doing so costs a re-crawl cycle and strands the equity mid-move. **Trade-off, named:** `/where-to-buy-african-greys-near-me/` has the better Google position (8.74 vs 64.90) and the family's only Bing click, and retiring it gives that up. It is still the right call, because that position converts at **0% on 109 impressions**.
2. ~~**Page A's search target moves.**~~ **RESOLVED 2026-08-10 — breeder approved the retarget.** The rebuild aims the page at the buy/buy-online cluster (40 queries · 443 impressions · positions 34–80) and keeps shipping as a trust section. This is the single largest strategic change in the plan and it is reversible only at the cost of another rebuild. Do not re-raise; do not restore shipping as the search target.
3. ~~**`/african-grey-parrot-for-sale/` is unresolved.**~~ **RESOLVED 2026-08-10 — scope expanded at breeder request.** The singular is retired into the hub (Task 13 Steps 6–7); the plural becomes the hub; geography moves to the near-me router. Full analysis, the rejected alternative, and the named trade-off are in §0f–§0g. Sprint scope is **3 builds + 1 retirement**, not 4 builds. Do not re-raise, and do not rebuild the singular.
5. **Task 13 Step 4 changes every page on the site.** Repointing the Footer anchor re-renders all 105 pages, which is why Step 8 submits `--all` to IndexNow rather than a slug list. Anyone re-scoping that step should keep the sitewide submission with it.
4. **Bing query-level data remains `NOT FETCHED`.** Every Bing export the project holds is page-level or a date series. All query claims in this plan are Google-only, and any Sprint 0 table must say so rather than filling the gap.

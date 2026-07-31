---
name: cag-visual-intelligence
description: Use when a page must be judged as a communication system rather than as markup — "does this page actually communicate", "score the visual quality", "what job is this page doing", "why does this page feel flat / generic / same as the other one", visual scorecard, functional audit, predicate audit, image-usefulness review, or when a page passes every mechanical gate and still underperforms. Also use before a cluster-wide design decision, when deciding whether a section needs a visual at all, and when a rendered page must be described in words for accessibility or AI citation.
---

# SKILL: CAG Visual Intelligence & Functional Semantics

Every other CAG gate asks **does the page render correctly**. This one asks **what is the
page saying, to whom, how well, and what work is it doing** — for a human eye, a search
crawler, and an answer engine.

**Position in the pipeline:** after `cag-page-hardening` (defects fixed) and before or
alongside `cag-aeo-pass`. Hardening makes the page *correct*; this makes it *effective*.
It never edits pages — it produces a scored report and routes every finding to the
specialist that owns the fix.

**Read `skills/cag-gate-integrity.md` first.** This skill emits ~20 numbers. Numbers are
the easiest thing in the world to invent, and on this site twelve checkers have already
reported defects that did not exist.

---

## 0. The Iron Rules

**0a. Measure in a painting viewport, or print `NOT MEASURED`.**
The Browser pane reports `vw: 0` — every `getBoundingClientRect()` returns zero, so every
visual probe false-passes. Use Playwright: `browser_resize` → `browser_navigate` →
`browser_evaluate`. Breakpoints **375 / 768 / 1280**, and **768 is the one that fails** —
on the adoption-cost pass, mobile and desktop were clean and every line-length defect was
at tablet.

**`NOT MEASURED` is a legal, expected value in every table in this skill.** A missing
number costs the breeder nothing. An invented number costs a cluster-wide reflow — that
nearly happened once, when `0.5em` was used to approximate a `ch` and over-reported by
~20%.

**0b. A score is a hypothesis about the page, not a fact about it.**
Before reporting any score below 6/10, quote the specific element and confirm the weakness
on the rendered page. **A suspiciously low score means a broken probe far more often than
a broken page.** Baseline evidence: a heading probe reported `h1: 0 … h6: 0` on a page with
1/15/21/13/11/6 headings, and an alt probe read `52 alts / 38 unique` as "14 duplicates,
Rule 50b violated" when the truth was 15 decorative `alt=""` plus **37 unique non-empty
alts and zero violations**.

**0c. Your own probes are gates too, and they lie.** Two shipped wrong on 2026-07-28: a
contrast sweep tested `display:none` on the element but not its ancestors (8 of 13
"failures" evaporated), and a hero measured 432px only because the probe included padding
instead of measuring `.hero-grid`, the element the spec names. Skip nodes where
`!el.offsetParent` or the rect is zero-sized. Print the probe's own examined count and
refuse to call a 0-element run a pass.

**0d. Every finding names an owner.** A report with no routing column is not done.

**0e. Terminate deterministically.** The source spec says "continue until exhaustion."
Exhaustion is not a stopping rule — it makes runs undiffable. This skill uses **closed
inventories** (§4 function taxonomy, §5 predicate taxonomy). Anything genuinely new goes
in an `UNCLASSIFIED` bucket with a proposed taxonomy addition, and the taxonomy is
extended by edit, not by improvisation.

---

## 1. Run the machine half first

Never hand-score what a script already counts.

```bash
npx astro build
python3 scripts/page_hardening_scan.py <slug>      # static defect classes
python3 scripts/final_page_audit.py <slug>         # page-type profile gates
python3 scripts/aeo_audit.py <slug>                # BLUF, entities, tables, dates
python3 scripts/seam_parity.py <slug>              # one seam per section
python3 scripts/dup_content_audit.py --headers     # sibling crossover
```

Structural counts — headings, images, alts, schema, links, tables — come from a parser,
never from shell globs (baseline failure B2). Minimum viable extractor:

```python
import re, collections
body = open(f'dist/{slug}/index.html', encoding='utf-8').read().split('<body',1)[1]
heads = {f'h{n}': len(re.findall(rf'<h{n}[\s>]', body, re.I)) for n in range(1,7)}
alts  = re.findall(r'alt="([^"]*)"', body)
decorative = [a for a in alts if not a.strip()]          # legitimate — NOT a defect
named      = [a for a in alts if a.strip()]
dupes = {k:v for k,v in collections.Counter(named).items() if v > 1}   # Rule 50b
```

**Decorative `alt=""` is correct markup, not a missing alt and not a duplicate.** Any
image-alt finding that counts empty alts is wrong before it is written.

---

## 2. Visual Intelligence — scored against locked tokens, never taste

The brand is decided. `PRODUCT.md`, `DESIGN.md` and `IMAGE-DESIGNS.md` are the rubric, so
colour and type score as **pass/fail against tokens**, not as opinion.

### 2a. Visual Hierarchy — /10

| Dimension | How it is measured | Fail condition |
|---|---|---|
| Hero effectiveness | Element screenshot at 375/768/1280 | Primary claim + price + CTA not all visible without scrolling at 1280 |
| Dominant element | Largest painted area above the fold | Two elements compete; no single focus |
| Reading order | DOM order vs visual order | They disagree — a screen reader gets a different page |
| Section rhythm | Painted section heights + `seam_parity.py` | A section > 2.5× the median with no internal break |
| Grid + alignment | `getBoundingClientRect().left` clustering of section children | More than 3 distinct left edges in one section |
| Spacing | Computed gaps vs the 4/8px scale | Off-scale values, or a `clamp()`/`calc()` silently dropped by the CSS-math spacing bug |

### 2b. Typography — /10
Newsreader (headings) + IBM Plex Sans (body) via `body.theme-d`, applied globally — a page
that hard-codes `font-family` to fight the theme is a defect. Check: heading clamp band
does not invert at any breakpoint (the `vw` term decides ordering — resolve `var()` before
judging), body line-height 1.6–1.7, `<p>` capped at 70ch, **measured as a real `ch`, never
as `0.5em`**, AP Title Case on every H1–H6 (FAQ `<summary>` stays conversational).

### 2c. Colour — /10
Pass/fail, not preference: Forest `#2D6A4F`, Clay `#e8604c`, Cream `#faf7f4`; solid clay
button fills render `--clay-ink #c8472f`; clay as small text on light is `#b04228`; on
dark `#f08070`; `--gold` must equal `--clay`. CTA emphasis = exactly one clay pill
(`border-radius:50px`) owning the page's primary action. Run a full-page contrast sweep at
AA and **skip invisible nodes** (§0c). Never dim text with `opacity`.

### 2d. Image Intelligence — /10 per image
Score each image on: **uniqueness** (is this photo used on a sibling page?),
**authenticity** (real bird photo vs AI infographic — the `.jpg` = photo / `.webp` =
infographic taxonomy), **usefulness** (does it carry information the prose does not?),
**trust contribution**, **conversion support**, and **AI understanding** (§3).

Hard CAG gates, all pass/fail:
- Uniform in-body box: `.sec-img.inf-img` = `max-width:760px`, `aspect-ratio:1408/768`,
  `object-fit:cover` — identical on all breakpoints, focal point tuned per image via
  `object-position`, never by changing the box.
- `<100 KB` WebP + a `-760.webp` sibling with `srcset`/`sizes`.
- `sizes` must not under-declare the rendered box — probe `wasteRatio` (§2e), flag `>1.5`.
- Rule 50b: primary keyword in the **primary image alt only**; every other alt rotates a
  different keyword type; **no two non-empty alts on a page may match**.
- Never 🦜 — Congo/Timneh use `/emoji/cag-*.png`.

### 2e. Runtime probes

```js
// srcset/sizes waste, per <img>, at 375/768/1280
const r = img.getBoundingClientRect();
({ declared: img.sizes, renderedCss: Math.round(r.width),
   intrinsic: img.naturalWidth,
   wasteRatio: +(img.naturalWidth / (r.width * devicePixelRatio)).toFixed(2) })
```
Also probe: horizontal overflow at 375, line length in real `ch` at 768, tap targets ≥24px,
and every jump-rail anchor actually scrolling (`scroll-behavior:smooth` cancels `#anchor`
navigation on long pages — use `auto`).

---

## 3. Visual Verbalization — can a machine read your pictures?

An image an answer engine cannot verbalize is decoration, however beautiful. For each
**non-decorative** image produce one row:

| Field | Requirement |
|---|---|
| Visual description | One sentence a blind reader could act on |
| Primary entity | The one named thing the image is about |
| Supporting entities | 2–4, from the §5 taxonomy |
| Relationships shown | Predicates the image asserts visually |
| Educational value /5 | Does it teach something the prose does not? |
| Search value /5 | Could it rank in Images for a real query? |
| AI citation value /5 | Is the claim it makes checkable and attributable to us? |
| Accessibility value /5 | Does the alt carry the information, or just the caption? |

**The verbalization is the alt-text spec.** If a row's description is better than the
shipped alt, that is a finding routed to `@cag-image-pipeline` — and it must respect
Rule 50b rotation, so the fix is a *different* keyword type, not the primary one again.

**Infographics carry a second duty:** every claim inside the image must also exist as
selectable page text. An answer engine cannot read a number that exists only as pixels.

---

## 4. Functional Intelligence — what work is this page doing?

Inventory the page's functions from the **closed taxonomy**: Inform · Teach · Compare ·
Recommend · Sell · Convert · Build Trust · Answer Questions · Handle Objections ·
Cross-link · Route Users · Qualify Buyers · Present Products · Explain Pricing ·
Present Reviews · Present Documentation · Display Certifications · Provide CTA ·
Generate Leads · Build Authority · Reduce Uncertainty · Support Snippets · Support AI
Overviews · Support Voice Search · Support Semantic Retrieval · Support Internal
Navigation · Support Decision Making · `UNCLASSIFIED`.

For each: **present / partial / absent**, the evidence (section + line), and its owner.

### 4a. Required-function matrix — this is what makes "Missing Functions" real

A generic "you could add trust signals" is worthless. Each CAG page type has a *required*
set; anything absent is a defect, not a suggestion.

| Page type | Required functions (absence = FAIL) |
|---|---|
| **For-sale / buy** | Present Products · Explain Pricing · Provide CTA every 500–700 words · shipping cost line on **every** card (`Ships nationwide · $185 airport · $350 home`) · Product/Offer schema with sold ≠ `InStock` · Qualify Buyers (form lists real birds + prices + Midland pickup) · Reduce Uncertainty (documentation) |
| **Bird `/available/`** | Single `Product`+`Offer` (never `AggregateOffer`) · real photos · Present Documentation · sell-and-retire lifecycle · 700–1,000 words |
| **Comparison** | Compare · Recommend · Decision Support · Route Users to both spokes · table + interactive module |
| **Location** | Route Users · Support Voice Search · local entity coverage · shipping tiers |
| **Interior / care** | Teach · Answer Questions · Build Authority · Cross-link to money pages |
| **Blog** | Teach · Cross-link · 6–7 diverse outbound links · Build Authority |
| **Every page** | Build Trust · Support Internal Navigation · Provide CTA (one per page) · **no visible date anywhere** — freshness is schema-only |

### 4b. Function metrics

- **Function Density** = functions present ÷ 1,000 words. Below ~1.5 the page is narrating,
  not working; above ~6 it is doing too many jobs and should be split.
- **Function Diversity** = distinct functions ÷ taxonomy size.
- **Function Coverage** = required set satisfied ÷ required set.  **This is the headline
  number.** Coverage < 100% blocks a pass.
- **Functional Redundancy** = the same function served ≥3× with no added information —
  the usual cause of a bloated for-sale page.

### 4c. Visual Differentiation — the breeder's recurring complaint, made numeric

Sibling pages that read as one template are a defect (`Write-From-Outline, NEVER-From-
Sibling`). Measure pairwise against **every** sibling in the cluster:

- Section-type sequence similarity (component order)
- Component-variant overlap (which hero, dial, rail, table, FAQ variant)
- Image reuse
- `dup_content_audit.py` body + `--headers` crossover

Target: **zero non-whitelist prose/header crossover** and at least three deliberate
component-variant deltas per sibling pair. Route to `cag-component-refresh` — layout,
accent and motif deltas only, **never a palette change**.

---

## 5. Predicate Intelligence — bounded, and CITES-safe

Extract the semantic predicates the page asserts, from the closed taxonomy:
`IS_A · HAS · CAN · USES · REQUIRES · PROVIDES · SUPPORTS · IMPROVES · REDUCES ·
LOCATED_IN · SHIPS_TO · SOLD_BY · RAISED_BY · SCREENED_FOR · CERTIFIED_BY · PRICED_AT ·
GUARANTEED_FOR · BETTER_THAN · COMPARES_WITH · INCLUDES · PART_OF · RELATED_TO · CAUSES ·
PREVENTS · RECOMMENDS · OWNS · PURCHASES · LEARNS · TRAINS · EXPLAINS · QUALIFIES ·
MEASURES · UNCLASSIFIED`.

**5a. Every predicate is authorized or it is not asserted.** Check each against the
Verified-Claim Ledger (`cag-entity-incorporation-agent` + `sessions/2026-06-03-homepage-
entity-map.md`). Ledger-backed → `ASSERTED`. Not backed → `PROPOSED`, and it is a finding,
not a fact. PBFD/Polyomavirus PCR screening **is** assertable (confirmed 2026-06-20);
board-certification and un-ledgered health claims are not.

**5b. Blacklist — a page carrying any of these is a hard FAIL, not a score:**
`WILD_CAUGHT · IMPORTED_FROM · SMUGGLED · UNDOCUMENTED_SALE` — or any phrasing implying
them. African Greys are **CITES Appendix I** (uplisted CoP17, effective Jan 2017), IUCN
Endangered (Congo) / Vulnerable (Timneh), and every bird is captive-bred in the USA.

**5c. Three fact predicates are checked on sight** (all three have regressed before):
`PRICED_AT` Congo = **$1,500–$3,500** (never a flat $3,000; the bonded pair sets the
ceiling) · `CERTIFIED_BY` = **Appendix I**, never II · `GUARANTEED_FOR` = **72-hour**
(plus the 24-hour window), never "3-day".

**5d. Brand-owned predicates.** `The Benjamin Home-Raising Protocol` and `The Midland
Socialization Method` are the only two approved method labels — never invent a third,
never imply third-party certification. A page teaching our method without naming it is
donating the expertise to answer engines.

**Metrics:** Predicate Inventory · Frequency · Diversity (distinct ÷ taxonomy) · Density
(per 1,000 words) · Complexity (share of multi-hop chains, e.g. `Roys —IS_A→ Congo
—SCREENED_FOR→ PBFD —CERTIFIED_BY→ Avian Biotech`) · Authorization ratio (ASSERTED ÷ all).

---

## 6. Scorecard

Report every number with its **source**: `measured` (Playwright/script), `derived`
(computed from measured), or `NOT MEASURED`. A score with no source is invalid output.

| # | Score | Basis |
|---|---|---|
| 1 | Visual Hierarchy | §2a |
| 2 | Visual Consistency | §2b–2c token pass rate |
| 3 | Visual Trust | credential/documentation/review visibility above 50% scroll |
| 4 | Visual Information Gain | § of images carrying non-redundant information |
| 5 | Visual Communication | §3 educational + search value means |
| 6 | Visual Storytelling | section progression: problem → evidence → decision |
| 7 | Visual Conversion | CTA visibility, one-CTA rule, shipping line, form friction |
| 8 | Visual Accessibility | AA contrast, tap targets, heading order, alt correctness |
| 9 | Visual Readability | line length in real `ch`, line-height, clamp band |
| 10 | Visual AI Readiness | schema present + infographic claims duplicated as text |
| 11 | Visual Verbalization | §3 row completeness |
| 12 | Visual Differentiation | §4c pairwise vs siblings |
| 13 | Function Density | §4b |
| 14 | Function Diversity | §4b |
| 15 | **Function Coverage** | §4a — **gate, not a score** |
| 16 | Predicate Diversity | §5 |
| 17 | Predicate Density | §5 |
| 18 | Predicate Authorization | §5a — **gate: any blacklist hit = FAIL** |

**Verdict:** `PASS` (Coverage 100%, Authorization clean, no score < 6) ·
`PASS-WITH-WARNINGS` · `FAIL` (any gate breached).

---

## 7. Output contract

Save to `sessions/YYYY-MM-DD-visual-intel-<slug>.md`:
Executive summary (≤150 words, verdict first) · Scorecard with source column · Visual
Intelligence report · Verbalization table · Function inventory + required-set gaps ·
Predicate inventory with authorization state · Strengths · Weaknesses · **Prioritized
recommendations with owners**.

| Finding class | Route to |
|---|---|
| Contrast, overflow, srcset, drift, title case | `cag-page-hardening` |
| Sibling sameness, template feel | `cag-component-refresh` |
| Alt text, image box, compression | `@cag-image-pipeline` / `IMAGE-DESIGNS.md` |
| Missing/weak infographic | `cag-infographic` |
| CTA, form friction, trust placement | `@cag-conversion-tracker` |
| Missing entity/predicate coverage | `@cag-entity-incorporation-agent`, `cag-entity-graph` |
| Snippet/citation shape | `cag-aeo-pass` |
| Duplicate prose or headers | `cag-duplicate-content-gate` |

---

## Common mistakes

| Mistake | Reality |
|---|---|
| Scoring layout from HTML source | The layout does not exist until it paints. Playwright or `NOT MEASURED`. |
| Counting `alt=""` as a defect | Decorative alt is correct markup. 15 empty + 37 unique named = zero violations. |
| Trusting a shell heading count | It returned `0` for every level on a 66-heading page. Use a parser. |
| Reporting a low score you did not verify | Quote the element and confirm on the rendered page, or downgrade to a question. |
| "Continue until exhaustion" | Use the closed taxonomies. Undiffable output is not measurement. |
| Recommending a visual for every section | §11 of the audit system is explicit: honest, **not** everywhere. |
| Suggesting a visible "Updated …" freshness cue | Banned site-wide. Freshness is schema-only, always. |
| Changing the palette to fix a differentiation score | Layout/accent/motif deltas only. The palette is locked. |

## Red flags — stop, the probe is wrong

- A count of `0` for something you can see on the page
- A defect count far higher than the page's element count
- Every sibling page scoring identically
- A contrast failure on text you cannot find on screen (check ancestors for `display:none`)
- A single Lighthouse run used to judge CLS — **CLS is bimodal here; ≥5 runs or no claim**

---

## Portable core

§§2–6 are domain-agnostic: taxonomies, probes, metric formulas and the source-labelled
scorecard work on any site. The CAG binding is exactly four things — the locked-token
rubric (§2b–2d), the required-function matrix (§4a), the ledger and CITES blacklist (§5),
and the routing table (§7). Swap those four to port the skill.

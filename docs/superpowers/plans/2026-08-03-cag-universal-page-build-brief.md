# C.A.Gs — Universal Page Build Brief (Portable Edition v1.0)

> **What this is.** A single self-contained, copy-paste build brief for **any** CongoAfricanGreys.com
> page type. Paste it into claude.ai (web), attach it as `.md`, or hand it to Claude Code. It carries
> every binding value inline, so it works with **no repo access**.
>
> **How to use it.** Fill in `§0 Target Block` only. Everything else is standing law and does not
> change per page. Sections run in dependency order — do not reorder, do not skip a gate.
>
> **Rule of the document.** Nothing is written, coded, or deployed until every `▣ APPROVAL GATE`
> is signed off by the breeder. A gate is passed by an explicit reply, never by silence.

---

## Contents

| § | Sprint | Section |
|---|---|---|
| 0 | — | [Target Block · fill this in](#0--target-block) |
| 1 | — | [Non-Negotiable Facts and Brand Constants](#1--non-negotiable-facts-and-brand-constants) |
| 2 | — | [Skill and Agent Routing by Sprint](#2--skill-and-agent-routing-by-sprint) |
| 3 | — | [The Seven-Sprint Pipeline](#3--the-seven-sprint-pipeline) |
| 4 | 0 | [URL, Canonical and Redirect Decision Gate](#4--url-canonical-and-redirect-decision-gate) |
| 5 | 0 | [Deep Competitor Research and Query Fan-Out](#5--deep-competitor-research-and-query-fan-out) |
| 6 | 0 | [Keyword Deliverables and Metrics](#6--keyword-deliverables-and-metrics) |
| 7 | 0 | [Entity Relationships and Co-Occurrence](#7--entity-relationships-and-co-occurrence) |
| 8 | 0 | [Competitor Gaps, Angles and Voice Tones](#8--competitor-gaps-angles-and-voice-tones) |
| 9 | 0.5 | [Strategy — Two Plus One Blended](#9--strategy--two-plus-one-blended) |
| 10 | 1 | [Section Distribution Matrix](#10--section-distribution-matrix) |
| 11 | 1 | [Heading Outline Gate — H1 to H6](#11--heading-outline-gate--h1-to-h6) |
| 12 | 1 | [Component Selection and Hero Refresh](#12--component-selection-and-hero-refresh) |
| 13 | 1 | [Tool / Special Element Decision](#13--tool--special-element-decision) |
| 14 | Asset | [OG Images, Infographics and the Asset Gate](#14--og-images-infographics-and-the-asset-gate) |
| 15 | 2 | [Build Rules — Write From Outline](#15--build-rules--write-from-outline) |
| 16 | 2 | [Responsive Typography, Spacing and Scroll](#16--responsive-typography-spacing-and-scroll) |
| 17 | 3 | [Harden Pass](#17--harden-pass) |
| 18 | 4 | [Gates and Pass Checks](#18--gates-and-pass-checks) |
| 19 | 5 | [LLM Visibility Measurement](#19--llm-visibility-measurement) |
| 20 | 6 | [Deploy and Session Close](#20--deploy-and-session-close) |
| 21 | — | [Master Deliverables and Metrics Index](#21--master-deliverables-and-metrics-index) |
| 22 | — | [Reference Library](#22--reference-library) |

**Legend** — `▣ APPROVAL GATE` breeder must reply · `[ ___ ]` awaiting breeder · `[AI RECOMMENDS: ___ ]`
Claude fills with exactly one **(Recommended)** pick + data-grounded why + named trade-off · ☐/☑ task.

---

## 0 · Target Block

*Fill in only this section. Everything below is standing law.*

```
TARGET URL      : [ ___ ]
PAGE TYPE       : [ for-sale | bird-listing | comparison | interior/care | location | blog | hub ]
POSITION        : Page [ ___ ] of [ ___ ] in the [ ___ ] cluster
MODE            : [ CREATE (no file on disk) | REBUILD (stub exists) | POLISH (full page exists) ]
ON DISK         : [ path ] — [ size ] — last modified [ date ]
LIVE STATUS     : [ HTTP 200 | 404 | redirects to ___ ]
INBOUND LINKS   : [ N internal pages link here — must not break ]
PRIMARY KEYWORD : [ ___ ]
BASELINE (GSC)  : [ clicks ] / [ impressions ] / [ CTR ] / [ avg position ]
BASELINE (Bing) : [ clicks ] / [ impressions ] / [ CTR ] / [ avg position ]
ASSET FOLDER    : [ path — must be listed and each file opened before assignment ]
SIBLINGS        : [ every page the dup-gate must run against ]
```

**Mode is determined by looking, not by assuming.** `ls -la` the path and read the file before
declaring the mode. A page that shipped last week is not a stub because the brief says so.

`▣ APPROVAL GATE 0` — breeder confirms the Target Block is accurate before Sprint 0 opens.

---

## 1 · Non-Negotiable Facts and Brand Constants

These bind every page, every sprint, every agent. Correct any contradiction **on sight**.

### 1a · The three facts that are wrong in circulation

| Wrong in the wild | Correct, always |
|---|---|
| CITES **Appendix II** | **Appendix I** — uplisted at CoP17, effective January 2017 |
| — | **72-hour** and **"3-day"** are BOTH correct; never rewrite one into the other |
| A single flat Congo price | **Congo range $1,500–$3,500** — the bonded pair sets the ceiling |

Also standing: **IUCN Endangered** (Congo) / **Vulnerable** (Timneh). All our birds are **captive-bred
in the USA with full documentation**. Never imply wild-caught or illegal trade.

### 1b · Voice

**First-person breeder voice** — *we / us / our / here at C.A.Gs*. Our birds and credentials are
framed as ours, never described from the outside. Neutral encyclopedic register is correct **only**
for species/taxonomy facts and cited research.

### 1c · The Verified-Claim Ledger

Every health and credential claim is bounded by the Ledger. In it: **PBFD / Polyomavirus PCR
screening · DNA sexing · psittacosis · UV-B/D3**. Anything not in it is **not assertable**.

### 1d · Brand-owned method labels — exactly two, never a third

- **The Benjamin Home-Raising Protocol** — hand-feeding, weaning, the 12–16-week gate.
- **The Midland Socialization Method** — family handling, out-of-cage routine.

Each is defined once at first use. Neither is ever implied to be third-party certification.

### 1e · No fabricated anything

Never invent credentials, prices, reviews, ratings, review counts, test results, competitor metrics,
or buyer stories. Un-fetched data is written **`NOT FETCHED`**, never inferred. Real review figures
only (4.9 / 52) and only where already sanctioned. No fabricated scarcity or urgency.

### 1f · Palette and identity

Forest green `#2D6A4F` · clay/terracotta `#e8604c` (accent, sparing) · warm cream `#faf7f4` ·
soft beige and warm wood · dark charcoal `#3a2f2a` text. Small clay on light backgrounds uses
`#b04228` for AA; clay on dark uses `#f08070`. Any incoming kit or draft is **reconciled to this
palette on intake** — stale gold/other palettes are a known drift vector.

Species markers use `/emoji/cag-congo.png` and `/emoji/cag-timneh.png` images — **never 🦜**.

### 1g · Working rules

- **Work on `main`.** Only `main` auto-deploys. Finished work on a branch is a live 404 that looks done.
- **Commit *and push* after every build.** Push *is* deploy.
- `src/pages/<slug>/index.astro` is what ships. Every gate measures **`dist/`**, never source.
- **Confidence gate, 97%.** Below it, do not dead-stop: write the finished work to disk, log the open
  question under `## Open Flags` in the session brief, ask exactly **one** narrow question, and keep
  building everything that is not blocked.
- **Restate the brief before building** — goal · scope · gates · definition of done · out of scope.
- **Preview before apply.** Any redesign is previewed and approved before it touches site files. A
  redesign never adds or removes content — visual layer only.
- **Recommend + Why.** Every set of options gets exactly one **(Recommended)**, justified from real
  data (GSC, Bing, competitors, the codebase — never taste), with the trade-off named.
- **No test, no rule.** A rule nothing enforces is a deletion candidate. When a defect escapes, charge
  it to the harness — add the case to the known-broken fixtures, watch the meta gate fail, fix the
  check, and write **no new rule**.

---

## 2 · Skill and Agent Routing by Sprint

Invoke, do not paraphrase. If a skill exists for the step, it is not optional.

| Sprint | Invoke |
|---|---|
| **Session open** | `grill-me` · page-type builder skill (see below) |
| **0 Research** | `keyword-cluster` · `cag-branded-hybrid-keywords` · `cag-branded-search-skill` · `cag-entity-agent` · `cag-entity-graph` · `research-recency` · `reddit-strategy` · agents: `cag-competitor-intel`, `cag-competitive-keyword-gap-agent`, `cag-framework-agent`, `cag-paa-agent` |
| **0.5 Strategy** | agent: `cag-strategy-synthesizer` · `cag-cta-strategy` |
| **1 Plan** | `framework-heading-hierarchy` · `framework-eebp` · `cag-component-refresh` · `cag-seo-master-checklist` · `cag-visual-intelligence` |
| **Asset Gate** | `cag-image-generation` · `cag-infographic` · `image-prompt-generator` · `image-metadata` · `cag-asset-proofing` |
| **2 Build** | page-type builder skill · `anti-ai-writing` · `cag-duplicate-content-gate` · `internal-link-agent` · agent: `cag-non-commodity-content-agent`, `cag-entity-incorporation-agent` |
| **3 Harden** | `cag-page-hardening` (v2.0) · `impeccable` · `frontend-design` |
| **4 Gates** | `cag-gate-integrity` · `cag-final-page-pass` · `cags-comprehensive-page-audit-system` · `cag-aeo-pass` · `section-auditor` · `manual-auditor-check` |
| **5 Visibility** | agent: `cag-llm-keyword-intel` · `framework-aio-geo` |
| **6 Close** | `sitemap-agent` · `cag-indexing` · `session-closer` · `cag-learning-loop` |

**Page type → builder skill:** for-sale/buy → `cag-for-sale-page-builder` · bird `/available/<slug>/`
→ `cag-bird-listing-page` (+ `cag-bird-page-excellence`) · comparison → `cag-comparison-page-builder`
· interior/care/trust → the manual interior checklist · location → `cag-location-page-builder` ·
blog → `cag-blog-post` · Reddit modifier → `reddit-strategy`.

**Planning discipline:** `superpowers:writing-plans` before a multi-step build;
`superpowers:verification-before-completion` before any "done" claim.

---

## 3 · The Seven-Sprint Pipeline

```
☐ Sprint 0    Research      → research doc, keyword universe, entity map, gap matrix, PAA set
☐ Sprint 0.5  Strategy      → two strategies + one blended, ONE recommended, breeder picks
☐ Sprint 1    Plan          → distribution matrix, H1–H6 outline, component tuple, meta sets
☐ Asset Gate  HARD STOP     → breeder drops OG photos + infographics and says "start"
☐ Sprint 2    Build         → section-by-section, on main, verified in dist/
☐ Sprint 3    Harden        → hardening scan + impeccable/frontend polish, mobile-first
☐ Sprint 4    Gates         → dup · final audit · seam parity · a11y · perf · gate-integrity
☐ Sprint 5    Visibility    → LLM visibility measurement + AEO/GEO pass
☐ Sprint 6    Deploy/Close  → sitemaps, IndexNow, push, lessons doc, memory
```

Each sprint ends at an `▣ APPROVAL GATE`. **Nothing from a later sprint starts early** — in
particular, no HTML is written before the Asset Gate clears, and no images are baked before the
outline is approved.

**Build-first, images-last** within Sprint 2: structure and prose land first, the OG bake runs at the
open of Sprint 2 against the approved outline, not before it.

---

## 4 · URL, Canonical and Redirect Decision Gate

*New step — previously handled ad-hoc, which is how a 22-click URL got redirected by accident.*

Before any research, resolve the URL family. Deliverable: **one table, one recommendation.**

☐ Enumerate **every** URL in the family — legacy `/product/` paths, `-nearby` / `-near-me` variants,
  singular/plural, `buy-` prefixes. Search the GSC Pages export and the Bing page-traffic CSV for the
  keyword stem, not just the exact slug.

☐ For each URL, pull the full row: **clicks · impressions · CTR · average position**, from **both**
  Google and Bing. A URL absent from an engine is recorded `NOT PRESENT`, never assumed zero.

☐ Pull the **query-level** rows for the family stem. This is the decisive evidence — page-level
  clicks tell you where equity landed, query-level tells you what people actually search.

☐ Read the live `_redirects` file. Map the current chains. Flag any chain of length ≥ 2 (A→B→C must
  be flattened to A→C) and any redirect whose target does not exist on disk.

☐ Count **inbound internal links** to each candidate. A slug with 28 internal links is not freely
  swappable.

### 4a · The decision rule

Consolidate **toward the clean, cluster-native slug** — the one that matches the cluster's naming
convention and that internal links already point at. Legacy `/product/` paths are WooCommerce
artifacts and are never a consolidation target.

**Low clicks on a redirect target is not evidence the URL is weak.** If the destination is a thin
stub, the equity arrived at an empty room. Diagnose the page before blaming the slug. Reversing a
settled 301 costs a re-crawl cycle and strands existing internal links — reverse only when the
target slug is genuinely off-intent, never to chase a click count.

**Distinct intents get distinct pages.** Two URLs in the same family are only a cannibalization
problem when they target the same query set. Verify against the query rows before merging anything.

`▣ APPROVAL GATE 1` — breeder approves the canonical URL, the redirect map, and any changes.

---

## 5 · Deep Competitor Research and Query Fan-Out

**No research may be skipped.** Un-fetchable source = `NOT FETCHED`.

☐ **SERP snapshot** — Google *and* Bing top 10 for the primary keyword plus the top 5 variations.
  Record: URL, title, meta, word count, H2 count, image count, video presence, schema types, page type.

☐ **Query fan-out** — every query the primary keyword expands into. Mine from: GSC Queries export
  (all rows containing the stem), Bing query data, Google PAA (expand three levels), autosuggest
  A–Z, "Related searches", Reddit/Quora/Facebook group thread titles, YouTube titles, and competitor
  H2/H3 text. **Every 6+-word conversational query is captured** — these are the AEO/voice targets.

☐ **Section inventory per competitor** — every H2/H3 they ship, in order, with word counts.

☐ **Visual inventory per competitor** — image count, image types (photo / infographic / chart /
  table), video count and length, interactive tools, comparison tables.

☐ **Recency sweep** — last-30-days signal via `research-recency`. When a source 403s: retry with a
  UA header, then Firecrawl, then Playwright. A 403 from curl is **not** a dead link.

☐ **Reddit / forum thread mining** — real buyer language, objections, and the phrasing they use.
  Log each thread in the Thread Ledger so it is not re-mined.

### 5a · The competitor-registry sweep — MANDATORY, never skipped

**This step is not optional and no judgement call may substitute for it.** It was skipped once, on
2026-08-03, on the reasoning that it "would not change the angle." Run it, then decide.

☐ Load the full competitor registry and sweep the **target keyword** against **every** domain in it.
  The efficient method is one search restricted to the registry's domains, not one search per domain.
☐ Produce the **compete / does-not-compete table** — one row per registry domain, with the evidence
  for each verdict. "No breeding-pair page" is a finding, not an omission.
☐ **Add every new direct competitor** the SERP surfaced that is not already registered, with tier,
  discovery date, the keyword set, and a grounded note. Only direct competitors for *this* keyword.
☐ Record the sweep date and keyword on the registry itself, so the next page can see when it last ran.
☐ Harvest the sweep's **pricing and positioning intel** — in-state and in-category comparables are
  worth more than out-of-state ones and are usually only found this way.

### 5a · Sprint 0 output artifacts

One dated research doc containing, in order: SERP snapshot table · query fan-out list ·
section inventory · visual inventory · gap matrix · keyword universe · entity map · PAA set ·
recency notes · `NOT FETCHED` list.

`▣ APPROVAL GATE 2` — breeder reviews the research doc before strategy opens.

---

## 6 · Keyword Deliverables and Metrics

*This is the section that determines whether the page ranks. Every metric below is a deliverable,
reported as a number, for **our planned page** and for **each top-5 competitor**.*

### 6a · Required metric table — ours vs each competitor

| Metric | Definition | Our target |
|---|---|---|
| **Unique keyword count** | Distinct keywords/phrases present at least once | 85–105 total mentions across 40+ distinct terms |
| **Variation count** | Distinct surface variations of the primary keyword | ≥ 12 |
| **Variation density, top 30 KB** | Variation mentions ÷ words, measured over the **first 30 KB of HTML** | 1–2% primary; never stuffed |
| **Exact matches in HTML tags** | Count of exact-match primary in `<title>`, `<h1>`–`<h6>`, `<a>`, `<img alt>`, `<meta>` | Title 1 · H1 1 · H2s 2–4 · alt 1 (primary image only) |
| **Clean keyword density in HTML tags** | Tag-only density, stopwords stripped, boilerplate excluded | Report the number; flag > 3% as stuffing |
| **First-100-words placement** | Primary keyword appears in the first 100 rendered words | Required |
| **Header keyword spread** | % of H2/H3 carrying a distinct keyword type | ≥ 80%, no two headers on the same type |

### 6b · Keyword type distribution (~85–105 total mentions)

| Type | Count | Placement note |
|---|---|---|
| Primary keyword | 30–35 | front-loaded in title, H1, first 100 words |
| LSI | 20–25 | spread across variations |
| Long-tail, 6+ words, conversational | 15–20 | headers + opening paragraphs |
| Branded (C.A.Gs, Mark & Teri Benjamin, C.A.Gs reviews/pricing) | 10–15 | branded + hybrid search targets |
| Conversational / voice | ~23 | headers + PAA answers |
| Comparison (Congo vs Timneh, male vs female) | 5–8 | link to the comparison cluster |
| Solution (scam-free, with health guarantee) | 5–10 | |
| Transactional (reserve, deposit, available now) | ~15 | honest only |

### 6c · Competitor keyword deliverables

☐ The keywords each top-5 competitor **has** that we do not — as a list, with their placement
  (title / H1 / H2 / body / alt).
☐ The keywords **nobody** in the top 10 covers — the open gap, ranked by impression potential.
☐ Their header text verbatim, so ours can be provably different.
☐ Their image alt text and filenames — the image-keyword layer is usually their weakest.
☐ Their video presence and what it covers.

### 6d · Meta

Two long formats, three sets per page (Educational / Benefit-Solution / Transactional-Urgency), one
marked **(Recommended)** with why and trade-off.
- **Title** ≤ 205 chars: `Primary Keyword | Related Conversational Query | Number + Positive Word | Brand — LSI/NLP terms`
- **Description** F1 ≤ 185 or F2 ≤ 300: `Primary Benefit | Secondary Benefit | Trust Signal + CTA`
- Front-load the primary keyword. Include a real price floor and real credentials. Never short-form.

### 6e · Counter snippets

8 per page, **< 4 words**, number-led, Ledger-verified only. Example shape: `12+ Yrs Aviary` ·
`100% CITES Papered` · `$1,500 Floor Price` · `24h Reply` · `0 Wild-Caught`. Never a fabricated count.

---

## 7 · Entity Relationships and Co-Occurrence

☐ **85–112 distinct entities** per page, each mentioned a natural number of times. The anti-pattern
  this exists to prevent: the business name in every sentence — unreadable and unrankable.

☐ Entity classes to cover: birds by name · Midland/TX geo · CITES Appendix I · USDA AWA · DNA-sexing
  labs · PBFD / Polyomavirus PCR · Delta / United / American cargo · IATA LAR · pellet brands ·
  avian-vet terminology · the two brand-owned method labels.

☐ **Frequency targets:** brand 5–10× · full location 1–2× plus city/state 5–8× · each bird named in
  its card plus 1–2 body mentions.

☐ **Co-occurrence map** — which entities the top-ranking pages mention *together*, as pairs. This is
  what topical-authority scoring reads. Deliver as a pair-frequency table.

☐ **Predicate extraction** — the subject→predicate→object triples each competitor asserts. Ours must
  assert more, and every one must trace to the Ledger or a data file.

☐ **Schema drift check** — the schema types the top 10 ship vs ours. Ours extends existing JSON-LD,
  never duplicates it, and is verified in `dist/`.

☐ **EEBP under every header** — Entity → Evidence → Benefit → Purpose, first-person, 1–2 sentences.
  (Distinct from `framework-ebp`; do not substitute.)

☐ Every health and credential entity is **bounded by the Verified-Claim Ledger** (§1c).

---

## 8 · Competitor Gaps, Angles and Voice Tones

For each top-5 competitor, deliver:

| Field | What to record |
|---|---|
| **Why they rank** | The specific mechanism — domain authority, exact-match slug, depth, freshness, schema, backlinks. Name it; don't hand-wave. |
| **Content gaps** | Sections and questions they do not answer at all |
| **Depth gaps** | Sections they answer thinly (word count) that we can own |
| **Trust gaps** | Missing credentials, documentation, real photos, named people |
| **Voice / tone** | Their register — corporate, hobbyist, aggregator-neutral, hard-sell. Ours must be distinguishable at one paragraph. |
| **Angle** | The single frame their page is built on |
| **Visual gaps** | Missing infographics, tables, video, tools |
| **Weaknesses to exploit** | Stale dates, broken elements, thin schema, no author, no location |

Then, one synthesis paragraph: **how we beat them** — the specific, defensible mechanism, not
"we'll write better content."

---

## 9 · Strategy — Two Plus One Blended

☐ Produce **two complete transactional strategies** plus **one blended**, each with: the angle, the
  target query set, the section architecture at H2 level, the conversion path, the risk.

☐ Mark exactly **one (Recommended)**, justify it from real data — GSC/Bing numbers, competitor
  positions, codebase reality — **never taste** — and name the trade-off you are accepting.

☐ Include the CTA strategy: cadence, anchor text, destination, and the one-global-CTA rule.

`▣ APPROVAL GATE 3` — breeder picks the strategy.

---

## 10 · Section Distribution Matrix

**Mandatory deliverable before any outline.** One row per planned section:

| # | Section | Group | Angle | Framework | Entities assigned | Keyword types | Image type | Word target | Why (grounded) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | MANDATORY | | EEBP | | | OG | | |
| 2 | | COMPETITOR-BASED | | QAB | | | Infographic | | |
| 3 | | SUGGESTED-RECOMMENDED | | BAB | | | Table | | |

**Groups are required labels:**
- **MANDATORY** — the page type demands it (house standard).
- **COMPETITOR-BASED** — the top 10 have it and we would be visibly thinner without it. Cite which competitor.
- **SUGGESTED-RECOMMENDED** — our differentiator. Justify why it earns its space.

Every row's *Why* is grounded in the Sprint 0 research, with the source named. Target 22+ sections
for a full transactional or comparison page.

`▣ APPROVAL GATE 4` — breeder approves the matrix.

---

## 11 · Heading Outline Gate — H1 to H6

**The full H1→H6 outline is approved before a single line of page code is written.** This gate has
teeth: an outline approved after the fact is not an outline.

☐ **All six levels present.** No skipped levels — an H4 never follows an H2 directly.
☐ **≥ 5 H5 and ≥ 5 H6.**
☐ **Title Case on every H1–H6** (AP style). FAQ `<summary>` stays conversational and is exempt.
☐ **Conversational Q&A headers** — What / How / Is / Can / Where / Why.
☐ **Two-Keyword Headers rule** — each major header carries two distinct keyword types.
☐ **Semantic map:** H1 topic · H2 search intents · H3 subtopics · H4 PAA/micro-intents ·
  H5 supporting facts and warnings · H6 breeder notes and citations.
☐ **Inline H6 must follow an H5** — a breeder-note H6 cannot be the first heading after an H4.
☐ **Header dup-gate runs BEFORE approval** — zero exact or template crossover with any sibling.
☐ **5 A/B variants** drafted for the H1 and each major H2; breeder picks.
☐ **Conversational opening paragraph under every header** — no header is ever followed immediately
  by a list, table, or image.
☐ **Header style** — declare which of the three registered header styles this page uses, per the
  header-style routing table. H2s carry the clay rule/orange line treatment used on the shipped
  reference pages.

☐ **Heading hierarchy band** — H3 renders at 40–50px equivalent; fix H4–H6 gaps by adding depth, not
  by shrinking. Watch the clamp-inversion trap: the `vw` term decides ordering, so verify the
  computed sizes at 375 / 768 / 1280, not the declarations.

`▣ APPROVAL GATE 5` — breeder approves the full outline. **This is the hard gate before any code.**

---

## 12 · Component Selection and Hero Refresh

☐ **Every page ships a distinct component tuple.** Record it in the component-map ledger: hero ·
  dial style · rail · stepper · key-takeaway · TOC · table · FAQ style · newsletter placement.

☐ **When the hero pool is exhausted**, do not invent a sixth and do not silently reuse. Run
  `cag-component-refresh` and ship a **delta spec** against the chosen reuse:
  - **Allowed deltas:** layout arrangement, accent placement, motif, image grid shape, eyebrow
    treatment, ribbon vs chips, stat-strip presence, crop ratio, entrance motion.
  - **Never a delta:** the palette. Refresh changes arrangement, not brand color.
  - Deliver the reuse recommendation **with** the delta spec at Sprint 1, as one **(Recommended)**
    pick with the trade-off named. Do not present it as a free choice when it is not.

☐ **Component fidelity** — the cluster's own kit only. Never import another cluster's hero, counter
  strip, newsletter, or seam. Read the kit's component-names doc and inspect the design PNGs first.

☐ **Dial TOC must actually work** — the conic ring's `--p` is driven by an IntersectionObserver
  scroll-spy that also highlights the active item and updates the `x of N` counter. A static ring
  reads as broken. Two known traps: the last-intersecting entry wins, and a rAF-gated handler
  latches on a non-painting page. Verify in Playwright, not in an occluded browser pane.

☐ **Dial compact spec** — 196px sidebar in `grid 196px minmax(0,1fr); gap:28px`; plain `#fff` card,
  `radius 16px`, `padding 12px 10px`, shadow `0 3px 12px rgba(60,30,10,.05)`, sticky at
  `calc(var(--hdr) + 16px)`, `max-height:calc(100vh - var(--hdr) - 32px)`, thin scrollbar. Ring
  **64px** (inner 50, number 15px serif, "of N" 7px). Links `.74rem/1.25`, padding `5px 7px`,
  radius 8px. **18-stop cap** on the dial — beyond that it must be grouped.

☐ **Seam dividers** — 4–8 per page, one before every section (seam parity is a gate). Decorative
  `alt=""` + lazy + explicit CLS dimensions.

☐ **`scroll-behavior: auto`** on any page with jump links — `smooth` cancels `#anchor` navigation.
  Set `--hdr` and a matching `scroll-margin-top` on every target.

☐ **No page-level sidebar.** Sticky filters are section-level components only; a sticky mobile CTA
  bar covers persistent-CTA needs.

---

## 13 · Tool / Special Element Decision

**A tool or special element is required unless the page type genuinely does not support one.** The
decision is made from data, not preference.

☐ Decide from: what the SERP shows (do the top 10 ship calculators, quizzes, checklists, tables?),
  the query intent (does the fan-out contain "how much", "which", "checklist", "compare"?), and the
  PAA set.

☐ Candidate elements: cost calculator · fit quiz · documentation checklist · shipping-timeline
  estimator · verification guide · interactive comparison table · decision tree.

☐ Constraints: pure HTML/CSS with minimal vanilla JS. **No frameworks, no dependencies, no external
  CDNs.** Live data reads from the real data files, never hardcoded.

☐ Deliver the decision as: chosen element + the SERP/query evidence + one **(Recommended)** with the
  trade-off. If the answer is "no tool", say so and name the evidence.

☐ **GEO fact tables** are near-always warranted — Markdown-style fact tables signal answerability to
  engines and are cheap to ship.

---

## 14 · OG Images, Infographics and the Asset Gate

### 14a · Sizing — the rule that keeps getting reworked

**Every in-body image — OG photo AND infographic alike — renders in the same box:**

```
.sec-img.inf-img {
  max-width: 760px;
  aspect-ratio: 1408 / 768;   /* 16:9 */
  object-fit: cover;
  height: auto;
}
```

Identical at mobile, tablet, and desktop. Do **not** give OG photos smaller or variable boxes.
Tune **`object-position` per photo** so the bird is not cropped out — the box never changes, only
the focal point.

**Bake pipeline (exact):** `PIL.ImageOps.fit(src, (1408,768), LANCZOS, centering=per-image)` → WebP
`method=6`, quality-walk from 82 downward **until under 95 KB** → emit the `-760.webp` sibling →
ship `srcset` + measured `sizes`. Ceiling is **< 100 KB**, target **< 95 KB**. A low-res master is
upscaled to the box on purpose — uniform sizing beats pixel-peeping.

**Portrait OG framing (locked default):** bake single-bird and pair portraits with
`--style blurfill --mobcrop 4:5` from the **original master**. Never focal-point cover-crop a
portrait — it cuts heads. Tag `class="sec-img og-photo og-tall"` and ship the mobile full-bleed rule:

```
.sec-img.og-tall { width:100vw; margin-left:calc(50% - 50vw); aspect-ratio:4/5; border-radius:0 }
```

Desktop keeps the uniform 16:9 box; mobile gets the taller full-bleed frame; the subject is dual-safe
at both widths. Wide/scene/infographic images stay 16:9 desktop / 5:4 mobile. Page root needs
`overflow-x: clip` so full-bleed never causes horizontal scroll.

**`sizes` is measured, not guessed** — `sizes`-first ordering is what cut 205 KiB on the last pass.
`naturalWidth` is density-corrected; do not read it as the served width.

### 14b · Coverage and alt text

☐ **Every H2, every H3, and every key H4 gets an image** — OG photo, infographic, or AI-generated.
☐ **Rule 50b alt rotation** — the primary keyword goes in the **primary image's alt only** (hero or
  first content image). Every other image rotates a **different** keyword type. **No two images on a
  page share an alt.**
☐ **Image SEO 5-element, none optional** — filename · alt · title · caption · description.
☐ Lazy-load everything below the fold; the LCP image gets `fetchpriority="high"` + preload, never
  `loading="lazy"`. Conditional renders still need the lazy attribute.
☐ Infographics need a **reserved box** (explicit dimensions) or they cause CLS.

### 14c · The Asset Gate — a hard stop

☐ **List the asset folder and open every file** before assigning anything. Check
  `assets/brand/` before declaring an image missing.
☐ **Analyze each OG image**, then assign it to a section — **after** the competitor research and the
  approved outline exist, never before.
☐ Produce the **infographic prompt pack**: one prompt per section that needs an infographic, with
  the type (Comparison / Feature Grid / Process Flow) and the 300–350px height target.
☐ **HARD STOP.** No page HTML is written until the breeder has dropped every generated infographic
  **and explicitly said "start."**

`▣ APPROVAL GATE 6` — breeder drops assets and says start.

---

## 15 · Build Rules — Write From Outline

### 15a · The non-negotiable

**Write from the outline, never from a sibling.** Reuse components, CSS classes, and structural
patterns freely — that *is* the kit. But every page's **prose** is written fresh from its own
approved outline and distribution matrix. **Never open a sibling's file to copy paragraphs.**

A page that is copied and then reworded **passes the automated dup check and still breaks the rule.**
The rule is about method, not about the score.

### 15b · Dedup is a pre-write discipline

Run the dup gate on **your own draft, before it is done** — body **and** `--headers` — pairwise
against **every** sibling in the cluster, the comparison cluster, and the variant pages. Target zero
non-whitelist crossover.

**Whitelist (may match verbatim):** the shipping line, documentation badge lists, the counter strip,
the CITES notice, CTA labels, real reviews, and real page-name link labels. Nothing else.

### 15c · Prose standards

☐ First-person breeder voice throughout (§1b).
☐ `anti-ai-writing` pass — strip AI-tell phrases, robotic rhythm, generic structure.
☐ Non-commodity check — would a generic model have written this? If yes, it fails.
☐ **Humor: Style-2 dry, ≤ 1 beat per section, never on legal or health content.**
☐ **Link-First anchors** — external and internal anchors go at the **start** of a sentence, never
  mid-sentence, never at the end. Branded CTA action anchors are exempt.
☐ Internal links same-tab; external new-tab with ↗. Pull anchors from the Anchor Diversity Ledger —
  no repeated anchor text site-wide.
☐ External links: 6–7 diverse authorities, citing the **specific resource page**, not the homepage.
  A curl 403 is not a dead link — retry with a UA header.
☐ Every claim traces to the Ledger or a data file. `NOT FETCHED` where it does not.

### 15d · Transactional layer (for-sale and buy pages)

☐ Real bird cards near the fold, from live inventory and the price matrix. **Every card carries the
  shipping line:** `Ships nationwide · $185 airport · $350 home`. Never a card without it.
☐ One `Product` + `Offer` per real bird. `AggregateOffer` **only** on group and hub pages. A sold
  bird is **never** `InStock`. Extend existing JSON-LD; verify in `dist/`.
☐ Reserve/inquire CTA every 500–700 words, clay pill, branded action anchor, anchored to `#reserve`.
  Respect the one-CTA-per-page rule via `hideGlobalCta` when the page ships its own band.
☐ Honest scarcity only — real counts, real waitlist.
☐ Contact form lists **every actual available bird with its real price** as select options, plus the
  delivery options including `Pickup in Midland, TX — if you live within 2–3 hours of us`.
☐ Negative-keyword counter-positioning — wild-caught, scam, and "cheap" handled head-on with
  green-flag framing, linking to the scam cluster.

---

## 16 · Responsive Typography, Spacing and Scroll

Verified at **375 / 768 / 1280** in a real browser, on the built page.

☐ **Fluid clamp scale** for all headings. No `text-3xl`-class utilities on H2/H3. Verify computed
  sizes, because the `vw` term decides ordering and can invert the hierarchy at one breakpoint.
☐ **No oversized headers.** H2 clamps down on mobile; nothing overflows its container.
☐ **Even paragraph rhythm** — consistent measure, consistent leading, no orphan lines from
  `text-wrap: balance` on short strings.
☐ **Measure a real `ch`** when checking line length. `0.5em` over-reports by ~20% and has triggered
  a needless cluster-wide reflow.
☐ **Tables stack on mobile** — one card per row at ≤ 640px, `data-label` on every `td`. Never a
  `::before` on `<tr>`; it shifts columns.
☐ **Cards go horizontal below 640px** where the playbook specifies; one fact per line.
☐ **Seam gutters −40%** on mobile versus desktop.
☐ **Tap targets ≥ 24px** with real spacing between them.
☐ **`flex: 1 0 100%` will not break a line past a `max-width`** — use grid.
☐ **A scoped `* { margin: 0 }` reset zeroes Tailwind's `px-`/`py-`** — never ship one page-scoped.
☐ **`clamp()` and `calc()` need spaces around `+` and `-`** or the declaration is silently dropped.
☐ Nothing is cut off at the screen edge; no horizontal scroll at any width.

---

## 17 · Harden Pass

Sprint 3 is its own sprint. It is not folded into build or into gates.

☐ Run the hardening scan for the slug. Then **verify each finding on the built page** before editing.
☐ **Markup ↔ CSS drift check** — a clean hardening scan is not a clean page. Class-diff every ported
  section against the source component.
☐ **Color specificity check** — the 1.19:1 contrast mechanism comes from a losing specificity
  battle, not from a wrong token.
☐ **Contrast floors:** stone-600 body floor · small clay on light `#b04228` · clay on dark `#f08070`
  · footer text on green `white/80` minimum · no opacity-based dimming for text.
☐ **Impeccable + frontend-design pass** — visual hierarchy, information architecture, cognitive load,
  spacing, alignment, motion, micro-interactions, error and empty states, UX copy. Nothing may feel
  roughed. Every component reads as intentional at all three widths.
☐ **Verify in a painting page.** IntersectionObserver reads static in an occluded browser pane;
  scroll-spy and animation checks run in Playwright.

---

## 18 · Gates and Pass Checks

### 18a · Run these

```bash
npm run test:render:meta
```
```bash
npm run test:render:pages
```
```bash
python3 scripts/quality_report.py
```

Plus, per page: the duplicate-content audit (body **and** `--headers`), the final page audit for the
correct page-type profile, the seam-parity check, the page hardening scan, and the AEO audit.

### 18b · Gate integrity — read this before believing any gate

**A gate's output is a hypothesis about the page, not a fact about it.** Twelve checkers have cried
wolf on this site, and two reported PASS having examined **zero pages**.

☐ **Run the meta gate first** — it is the gate that checks the checkers.
☐ **Before editing in response to a finding, confirm the defect on the built page.**
☐ **Before believing a PASS, read the gate's own examined count.** A PASS over zero items is not a PASS.
☐ **Run every gate twice.** One clean run proves nothing — the same input has produced different
  verdicts.
☐ **Perf conclusions need ≥ 5 runs.** CLS here is bimodal; a single Lighthouse run produced a
  confident wrong attribution. Report the warm median of at least 3, look at the distribution.
☐ **When a defect escapes a gate that should have caught it, fix the harness, not the page — and
  write no new rule.** Add the case to the known-broken fixtures, watch the meta gate fail, fix the
  check.

### 18c · Manual pass list

☐ 400px-class hero · staggered hero image sizing
☐ Unique newsletter image and one-line title per page — never shared across siblings
☐ Opening paragraph under **every** header
☐ Uniform OG boxes throughout
☐ Separate blog and contact H2s
☐ Mobile table stacking verified
☐ Jump-rail `scroll-margin` verified; jump links actually jump
☐ Further-reading cards with **real** thumbnails
☐ Seam count matches section count
☐ Schema verified in `dist/` — types, no duplicates, no false `InStock`
☐ No visible dates in body copy (schema-only freshness)
☐ All six heading levels, ≥ 5 H5, ≥ 5 H6
☐ Lighthouse warm median-of-3 recorded
☐ Verified in **`dist/`**, never by grepping source

---

## 19 · LLM Visibility Measurement

**Mandatory for every page.** This is a required deliverable, not an optional extra.

☐ Query **ChatGPT, Claude, Gemini, Perplexity, and Google AIO** for the page's primary keyword and
  its top 5 variations.
☐ Record for each engine: are we cited · which URL · what position in the answer · which competitors
  are cited instead · what phrasing the answer uses.
☐ Extract the **answer structure** each engine returns — that structure is the AEO target.
☐ Extract the **keywords the engines themselves use** that our page does not contain.
☐ Produce an **LLM Visibility score** and record it against the page.
☐ Route the gaps: missing keywords → the keyword verifier; missing questions → the FAQ builder;
  missing structure → the AIO/GEO framework.
☐ Re-measure after deploy to establish the delta.

---

## 20 · Deploy and Session Close

☐ Build, then verify the **built** page — content, schema, images, links.
☐ Regenerate sitemaps after any page is added or removed.
☐ **Commit and push.** Push is deploy. On `main` only.
☐ Confirm live HTTP 200 at the canonical URL, and that every redirect in the family resolves in one hop.
☐ Submit to IndexNow.
☐ Write the **lessons doc** — what broke, what the root cause was, what the reusable fix is.
☐ Run the learning loop: if a defect escaped a gate, the harness gets the fix.
☐ Update the session brief's *What's Next*; save durable, non-obvious findings to memory.

---

## 21 · Master Deliverables and Metrics Index

Every artifact this brief produces, in order. **Each one is a deliverable, reported as a document or
a table — not as a claim that it was considered.**

### Sprint 0 — Research
1. URL family table — clicks / impressions / CTR / position, per URL, Google **and** Bing
2. Query-level table for the family stem, both engines
3. Redirect map with chain lengths and orphan targets
4. Inbound internal link count per candidate URL
5. SERP snapshot — top 10 Google + top 10 Bing, 9 fields each
6. Query fan-out list — every variation, PAA (3 levels), autosuggest A–Z, related searches
7. Section inventory per competitor — H2/H3 in order with word counts
8. Visual inventory per competitor — images, infographics, video, tools, tables
9. Gap matrix — content, depth, trust, visual gaps ranked by opportunity
10. Keyword universe — every term, classified by the 8 types
11. Entity map — 85–112 entities with class and target frequency
12. Entity co-occurrence pair table
13. Predicate extraction table
14. PAA question set
15. Reddit/forum thread ledger entries
16. `NOT FETCHED` list

### Sprint 0.5 — Strategy
17. Two full strategies + one blended, one **(Recommended)** + why + trade-off
18. CTA strategy — cadence, anchors, destinations

### Sprint 1 — Plan
19. Section distribution matrix — 10 columns, grouped MANDATORY / COMPETITOR-BASED / SUGGESTED
20. Full H1–H6 outline with all six levels, ≥5 H5, ≥5 H6
21. 5 A/B variants for H1 and each major H2
22. Header dup-gate result (pre-approval)
23. Component tuple + hero refresh delta spec
24. Tool / special-element decision + evidence
25. 3 meta sets (Title ≤205, Desc ≤185 or ≤300), one **(Recommended)**
26. 8 counter snippets, Ledger-verified
27. Visual companion / skeleton screens

### Asset Gate
28. Asset folder inventory — every file listed and opened
29. Per-image analysis + section assignment table
30. Infographic prompt pack — type + height per section
31. Image metadata set — filename / alt / title / caption / description, no duplicate alts

### Sprint 2 — Build
32. The built page, verified in `dist/`
33. Pre-write dup-gate result — body and headers, zero non-whitelist crossover
34. Keyword metric table — ours vs each top-5 competitor (all 7 metrics from §6a)
35. Entity count and frequency verification
36. Schema block, verified in `dist/`

### Sprint 3 — Harden
37. Hardening scan result + per-finding verification note
38. Markup↔CSS drift class-diff
39. Contrast audit at all three widths
40. Impeccable / frontend-design polish notes

### Sprint 4 — Gates
41. Meta gate result (run first)
42. Render pages result at 375 / 768 / 1280
43. Quality report — rework rate, worst family, open overrides, untested-rule list
44. Final page audit — PASS / PASS-WITH-WARNINGS / FAIL + fix list
45. Seam parity count
46. Manual pass list, all 14 items checked
47. Lighthouse warm median-of-3 (≥5 runs where CLS matters)
48. Gate-integrity note — examined counts, second-run confirmation

### Sprint 5 — Visibility
49. LLM visibility table — 5 engines × 6 queries, citation status
50. Answer-structure extraction
51. Engine-keyword gap list + routing
52. LLM Visibility score

### Sprint 6 — Close
53. Sitemap regeneration confirmation
54. Live 200 confirmation + one-hop redirect confirmation
55. IndexNow submission
56. Lessons doc
57. Memory entries for durable findings

---

## 22 · Reference Library

**Read before the relevant sprint. Not optional when named.**

| When | Document |
|---|---|
| Before any UI/UX polish on a live for-sale page | the for-sale UI/UX polish playbook — 18-stop dial cap, the two scroll-spy failure modes, one-fact-per-line card stack, −40% seam gutters, `sizes`-first image sequence |
| Before starting a new for-sale group | the for-sale cluster impeccable lessons — cross-sell component spec, Anchor Diversity Ledger with anchors already spent, corrected measurement probes, copy-paste command sequence |
| Before any image work | the image-designs art-direction source of truth (§1a uniform sizing, §7 OG framing styles) |
| Before any design or content work | the strategic product doc (register, users, personality, anti-references, a11y bar) and the visual design doc (locked palette, typography, components, motion) |
| Before trusting any gate | the gate-integrity skill |
| Component assignment | the for-sale component map with the per-page tuple ledger |
| Standard of done | the most recently shipped page in the same cluster |

**Known systemic traps, banked:**
`smooth-scroll` kills jump links · `CSSStyleRule.cssRules` is truthy on every rule (a recursion guard
that examined zero) · `behavior:'instant'` ≠ `'auto'` · Playwright loads a spec once per **worker** ·
lazy images do not load by scrolling · a hung check makes a page score ABSENT · zsh will not
word-split `$VAR` (a gate examined zero pages) · a static scan covers 108 pages where the harness
covers 15 · the design-system CSS file is **not** globally imported — tokens live in the global and
theme sheets.

---

*Portable Edition v1.0 — 2026-08-03. Self-contained; no repo access required. When used inside the
repo, the repo's own rule packs and skills are authoritative where they are more specific.*

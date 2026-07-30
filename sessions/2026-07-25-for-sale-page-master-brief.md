# 🦜 C.A.Gs — For-Sale Page Master Build Brief

> **Target page (current):** `https://congoafricangreys.com/congo-african-grey-parrot-pair-for-sale/` — **Page 9 of 22**, first page of Cluster 3.
> **On disk:** `src/pages/congo-african-grey-parrot-pair-for-sale/index.astro` — an **8 KB inline-styled stub** (1 H1, 2 H2, 4 FAQs, no kit components, no images, no dial, no bird cards). Live HTTP 200. **Mode: full rebuild from stub**, exactly like Congo on 2026-07-21.
> **Pipeline:** ☐ Sprint 0 · ☐ Sprint 0.5 · ☐ Sprint 1 · ☐ Asset Gate · ☐ Sprint 2 · ☐ Sprint 3 · ☐ Sprint 4 · ☐ Sprint 5 · ☐ Sprint 6
> **Nothing is written or coded until every ▣ Approval Gate below is signed off by the breeder.**
>
> **Target history.** This brief is the standing template for every remaining for-sale page. It was written for `/african-greys-for-sale-with-health-guarantee/` (Page 5, shipped 2026-07-25), retargeted to `/congo-african-grey-parrot-pair-for-sale/` on 2026-07-30. Part II is cumulative and is never retargeted — it grows one dossier per shipped page.

> **Editorial note.** This is the copy-edited edition. Spelling, grammar, and phrasing have been corrected, and the shouted capitals converted to sentence case with bold emphasis. Every instruction, value, path, and requirement is unchanged. The word-for-word original is preserved in the `.docx` twin and in git at commit `5d29c73`.

---

## 📑 Contents

| # | Section |
|---|---|
| 0 | [Placeholder Legend](#0--placeholder-legend) |
| 1 | [Brand Color](#1--brand-color) |
| 2 | [Invoke — Skills to Run First](#2--invoke--skills-to-run-first) · *2a session-opening · 2b full roster by sprint* |
| 3 | [Headers, Copy, and Voice Standard](#3--headers-copy-and-voice-standard) · *3a header style · **3b Keyword Variation Standard*** |
| 4 | [Deliverables and Approval Requirements](#4--deliverables-and-approval-requirements) · *4a required reading · 4b binding fact corrections* |
| 5 | [Internal and External Link Standard](#5--internal-and-external-link-standard) |
| 6 | [CTAs and Buttons](#6--ctas-and-buttons) |
| 7 | [Footer Divider Style](#7--footer-divider-style) |
| 8 | [OG Images and Hero Image Selection](#8--og-images-and-hero-image-selection) · *8a asset proof · **8b pair framing vs Jins & Jeni*** |
| 9 | [Infographics and the Asset Gate](#9--infographics-and-the-asset-gate) |
| 10 | [Components — Desktop and Mobile Versions](#10--components--desktop-and-mobile-versions) |
| 11 | [The Five Heroes](#11--the-five-heroes) |
| 12 | [Desktop and Mobile Image Styles](#12--desktop-and-mobile-image-styles) |
| 13 | [Section Architecture — 22+ Sections](#13--section-architecture--22-sections) |
| 14 | [Deep Competitor Analysis — Mandatory](#14--deep-competitor-analysis--mandatory) |
| 15 | [Blended Strategies and Frameworks (EEBP)](#15--blended-strategies-and-frameworks-eebp) |
| 16 | [Two New Verified Reviews](#16--two-new-verified-reviews) |
| 17 | [Workflow — The Seven-Sprint Pipeline](#17--workflow--the-seven-sprint-pipeline) · ***17c full skill routing, top to bottom*** · ***17d component quality bar*** |
| 18 | [Verified Results the Page Must Pass](#18--verified-results-the-page-must-pass) |
| 19 | [Root Causes Found — Saved Reference](#19--root-causes-found--saved-reference) |
| 20 | [Desktop Dial TOC — Locked Spec](#20--desktop-dial-toc--locked-spec) |
| 21 | [Hero Image Order and Height](#21--hero-image-order-and-height) |
| 22 | [Bird Card Label Placement](#22--bird-card-label-placement) |
| 23 | [Example of Done — Reference Build](#23--example-of-done--reference-build) |
| II | [Part II — Cluster Build Record](#-part-ii--cluster-build-record) |

---

## 0 · Placeholder Legend

| Marker | Meaning |
|---|---|
| `▣ APPROVAL GATE` | The breeder must reply before work continues |
| `[ ___ ]` | Awaiting the breeder's answer |
| `[AI RECOMMENDS: ___ ]` | Claude fills this with one **(Recommended)** pick, the reasoning behind it, and the trade-off |
| ☐ / ☑ | Task checkbox |

---

## 1 · Brand Color

**Strict palette:** forest green `#2D6A4F`; clay/terracotta `#e8604c`, used sparingly as an accent; warm cream `#faf7f4` background; soft beige and warm wood; dark charcoal `#3a2f2a` for text.

| Role | Usage | Hex |
|---|---|---|
| Forest green | Navigation and headers | `#2D6A4F` |
| Clay / terracotta *(accent, used sparingly)* | All CTAs | `#e8604c` |
| Warm cream | Page background | `#faf7f4` |
| Soft beige and warm wood | Surfaces | — |
| Dark charcoal | Body text | `#3a2f2a` |

---

## 2 · Invoke — Skills to Run First

Invoke the following against the target page, then check, read, analyse, and verify the page before confirming you understand the task set out below.

**2a · Session-opening invocation (run these four first, before anything else)**

- ☐ `/cag-for-sale-page-builder` — the canonical builder; carries the kit, the pass gates, the Egg Rule
- ☐ `/frontend-design:frontend-design` — production-grade UI craft, anti-AI-slop bans
- ☐ `/impeccable:impeccable` — auto-loads `PRODUCT.md` + `DESIGN.md`; owns `critique` / `audit` / `polish` / `harden`
- ☐ `/superpowers:writing-plans` — turns the approved blueprint into a bite-sized, checkbox task plan
- ☐ Check · read · analyse · verify → **confirm understanding**

**2b · The full skill roster for this page, by sprint.** None of these is optional; §17c is the routing table that says *when* each fires.

| Sprint | Skills / agents to invoke |
|---|---|
| **0 Intel** | `@cag-competitor-intel --all` · `@cag-competitive-keyword-gap-agent` · `@cag-gsc-analytics` · `/research-recency` · `/reddit-strategy` · `@cag-paa-agent` · `@cag-llm-keyword-intel` |
| **0.5 Orient** | `/grill-me` · `/keyword-cluster` · `@cag-angle-agent` · `@cag-strategy-synthesizer` |
| **1 Blueprint** | `/framework-heading-hierarchy` · `/cag-seo-master-checklist` · `/cag-duplicate-content-gate --headers` · `/cag-entity-agent` · `@cag-entity-incorporation-agent` · `/cag-cta-strategy` · `@cag-content-audit-agent` · visual companion |
| **2 Build** | `/cag-for-sale-page-builder` · `/framework-eebp` · `/cag-branded-search-skill` · `/cag-branded-hybrid-keywords` · `/internal-link-agent` · `@cag-external-link-agent` · `/anti-ai-writing` · `@cag-non-commodity-content-agent` · `/cag-infographic` · `/cag-component-refresh` |
| **3 Harden** | `/cag-gate-integrity` **(read first, every time)** · `/cag-page-hardening` · `/impeccable audit` · `/impeccable critique` · `/impeccable harden` · `/impeccable polish` · `/frontend-design` |
| **4 Final** | `/cag-aeo-pass` · `@cag-keyword-verifier` · `/cag-duplicate-content-gate` · `/cag-final-page-pass` · `/cags-comprehensive-page-audit-system` · `@cag-accessibility-fixer` |
| **5 Ship** | `/sitemap-agent` · `@cag-canonical-fixer` · `@cag-deploy-verifier` |
| **6 Bank** | `/session-closer` · memory write · back-propagate fixes to the 8 shipped siblings |

**Humor.** There is no `humor-agent` skill. Humor is a **mode inside `@cag-seo-content-writer`** (5 modes) governed by `skills/anti-ai-writing.md` and memory `feedback_humor_honesty_policy`: **Style-2 dry, ≤1 beat per section, never on legal, health, CITES, guarantee, or price copy.** Invoke it as a writing instruction, not as a slash command.

**`/cag-bird-page-excellence`** is listed for this page too, but note its scope: it polishes `/available/<bird>/` pages. On a for-sale category page it is read-only reference — use it for the **card, badge-placement, and geo-block patterns** it banks, not as the page builder.

---

## 3 · Headers, Copy, and Voice Standard

Headers use the **hybrid-keyword + entity, FAQ-style conversational** pattern, set in our new **Title Case** standard. Apply the same H2 colour treatment used on the Hand-Raised page, including the **orange rule at the start of each H2**.

Every header must be followed by a conversational opening paragraph that reinforces the header's core message. Those opening sentences and paragraphs should draw on the header's keyword variations — related terms, synonyms, LSI, long-tail phrasing, and question-form search queries.

**Checklist**

- ☐ Hybrid-keyword + entity, FAQ-style conversational headers
- ☐ New Title Case standard applied to every heading
- ☐ Same H2 colour treatment, **with the orange rule at the start of each H2**, as on the Hand-Raised page
- ☐ A conversational opening paragraph under every header, reinforcing that header's core message
- ☐ Opening sentences and paragraphs built from the header's keyword variations — related, similar, LSI, long-tail, and question-form search queries

### 3a · Which of the Three Header Styles Applies Here?

Every outline presented at the Sprint 1 gate must **declare its header style and its register**, with a reason grounded in that page's own query set, SERP snapshot, PAA demand or a named competitor gap — never taste — plus a named trade-off. An outline with no style line does not pass the gate. Spec: `skills/framework-heading-hierarchy.md §Header Style Selection`; injected into all 68 agent Golden Rules by `scripts/add_header_style_rule.py`.

| Style | What it is | Default for |
|---|---|---|
| **Style 1** | Pure Conversational — the header *is* the question, verbatim | Informational / PAA-led pages |
| **Style 2** | Conversational Hybrid — question + one entity | Care · location · blog · informational |
| **Style 3** | **Recommended Hybrid** — question + entity + transactional modifier | **Transactional + comparison** |

**Registers:** FAQ · Quora · Reddit. FAQ is the default for bird listings; Reddit for Reddit-modifier pages.

> ### ▣ APPROVAL GATE — Header Style
> `[AI RECOMMENDS: **Style 3, Recommended Hybrid, FAQ register**]`
> **Why:** this is a transactional page whose whole job is the pair-versus-single decision, and Style 3 is the locked default for transactional pages. It is also the only style that can carry all three of the page's competing entities in one header — the pair, the subspecies, and the price — which is what a header like *"What Does a Congo African Grey Pair Cost Compared With Two Single Birds?"* needs to do.
> **Trade-off:** Style 3 headers run long, so they eat vertical space on mobile and are harder to keep under the H2 clamp. Budget for two-line H2s at 375px and check the clamp at Sprint 3 rather than at final pass.
> Breeder approval: `[ ___ ]`

### 3b · Keyword Variation Standard — Non-Negotiable

**Keyword variation on the page is the single most important on-page lever, and it is measured, not asserted.** Distribution targets live in `skills/cag-for-sale-page-builder.md §2a` (~85–105 total mentions, 1–2% primary density). This section adds the four *variation* metrics the breeder wants reported on every page:

| # | Metric | Target | How it is measured |
|---|---|---|---|
| 1 | **Number of unique keywords / variations used** | **≥ 60 distinct** surface forms across primary, secondary, LSI, NLP variation, long-tail, question-form, comparison, solution and transactional buckets | Count distinct normalised strings in the built `dist/` page, not the source |
| 2 | **Variation density in the top 30 KB** | The primary keyword **plus ≥ 12 distinct variations** must all appear inside the first 30 KB of rendered HTML | Byte-slice `dist/<slug>/index.html` at 30,720 bytes and count there |
| 3 | **Exact matches in the HTML tags** | Primary keyword exact-match in `<title>`, `<h1>`, `<meta name="description">`, the first `<h2>`, the primary image `alt`, and the canonical slug. Every other `alt` carries a **different** keyword type (Rule 50b) | Parse tags out of `dist/`, never grep the `.astro` source |
| 4 | **Clean keyword density in the HTML tags** | No tag stuffs the primary keyword twice. Headers use the Two-Keyword rule (Rule 28b) — maximum two keyword concepts per header, no chains | Per-tag count, reported as a table |

**Entity variety is the anti-stuffing counterweight** (skill §2d): **85–112 different entities** per page, each mentioned a natural number of times. Brand 5–10×, full location 1–2× plus city/state 5–8×, each bird named in its card plus 1–2 body mentions. The MFS failure log is explicit that the business name in every sentence is unreadable and unrankable.

**Reported at Sprint 4** by `@cag-keyword-verifier` as a four-row table, alongside the density figure. A page that hits 1.78% primary density but only 22 unique variations has failed this section even though it passes §18.

---

## 4 · Deliverables and Approval Requirements

Show me every deliverable — entities, keyword universe, and the rest — for review and approval.

Provide **blended strategies**, the **frameworks** in play, the **transactional angles**, how each **search intent** is satisfied, and the full **H1–H6 outline**. All of it needs my confirmation before any page or code is written.

Check the saved data on everything we did well and badly on the pages already shipped, so you know exactly what you are doing with this one.

### 4a · The Required Reading List — Read Before Sprint 0, Every Page

These are binding, not background. Fixing the backlog items is a separate call; **knowing them before you build is not.**

| # | Source | What it gives you |
|---|---|---|
| 1 | `docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md` | The reusable playbook: the `.xsell` cross-sell spec, the cross-sell FAQ rules, the **Anchor Diversity Ledger with the anchors already spent** (§6 + §9 — three of them are already spent against *this page's* own slug), the corrected `ch` probe, and the copy-paste command sequence in §8 |
| 2 | `skills/cag-gate-integrity.md` | **Read at the first report from any checker, and before believing any PASS.** 12 recorded false or empty reports, with the bug in each checker |
| 3 | `skills/cag-page-hardening.md` (v2.0) | The static half of Sprint 3, plus §1k `markup-css-drift` and §1l colour specificity, added 2026-07-29 |
| 4 | `skills/cag-asset-proofing.md` | Proof every dropped asset before the build — resolution, taxonomy, baked-in text errors |
| 5 | `skills/cag-aeo-pass.md` | The 6-part answer-engine gate, plus the three binding fact corrections and the two approved method labels |
| 6 | `docs/reference/technical-seo-fixes-backlog.md` | Everything known-broken and deferred, so nothing is re-discovered as new |
| 7 | `sessions/2026-07-19-for-sale-component-map.md` | The binding tuple ledger — **record this page's tuple here before the build begins** |
| 8 | `docs/research/for-sale-keywords-2026-07.md` | 793 GSC queries bucketed across the 22 pages. Never invent keyword data |

### 4b · The Three Binding Fact Corrections

Wrong on sight, correct on sight, on every page:

1. **CITES is Appendix I** — uplisted at CoP17, effective January 2017. Never Appendix II.
2. **The Congo range is $1,500–$3,500** — not $3,000. The bonded pair sets the ceiling.
3. **The guarantee is written "72-hour"** — plus the 24-hour arrival window. Never "3-day".

**Brand-owned method labels** — two only, never invent a third: **The Benjamin Home-Raising Protocol** (hand-feeding, weaning, the 12–16-week gate) and **The Midland Socialization Method** (family handling, out-of-cage routine). Both are proper nouns, defined once where first used, never implied to be third-party certification.

As before, I must approve this. Competitor-based and suggested/recommended sections can only be drawn up **after** the competitor analysis is complete.

> ### ▣ APPROVAL GATE — Deliverables
> | Deliverable | Status |
> |---|---|
> | All deliverables | `[ ___ ]` |
> | Entities | `[ ___ ]` |
> | Keyword universe | `[ ___ ]` |
> | Blended strategies | `[ ___ ]` |
> | Frameworks | `[ ___ ]` |
> | Transactional angles | `[ ___ ]` |
> | Intents satisfied | `[ ___ ]` |
> | H1–H6 confirmation | `[ ___ ]` |
> | Competitors + suggested/recommended sections *(after competitor analysis)* | `[ ___ ]` |

---

## 5 · Internal and External Link Standard

Apply the same SEO-optimised internal and external anchor variations we used on the Hand-Raised page, as now codified in the rules.

The **diverse external links standard is mandatory**: at least six external links, each using a different keyword variation as its anchor (see the newly added rule), each carrying an arrow, and each anchored from the **start** of its sentence or paragraph — never at the end. Internal links follow the same rule.

| Rule | Requirement |
|---|---|
| Count | **At least 6** external links |
| Anchors | **A different keyword variation** on every anchor (see the newly added rule) |
| Marker | Arrow sign ↗ |
| Placement | **Anchored from the start of the sentence or paragraph — never at the end** |
| Internal links | **The same standard applies** |

---

## 6 · CTAs and Buttons

The page must carry **at least five action CTAs** with SEO-optimised buttons.

- ☐ CTA 1 `[ ___ ]`
- ☐ CTA 2 `[ ___ ]`
- ☐ CTA 3 `[ ___ ]`
- ☐ CTA 4 `[ ___ ]`
- ☐ CTA 5 `[ ___ ]`

---

## 7 · Footer Divider Style

Use the **small footer-logo divider style** on this page.

---

## 8 · OG Images and Hero Image Selection

The OG images for this page live at:

```
/Users/apple/Downloads/CAG/assets/1WORKING-ON/FOR-SALE-PAGES/1CONGO-AFRICAN-grey-parrot-pair/
```

Use **only** the OG images provided in that folder — **all of them, or at minimum 80%** — plus the two review images in the same folder.

**Breeder-nominated candidates**

| Slot | Candidate files |
|---|---|
| **Hero** | `mac-letia-young-african-grey-parrot-with-midland-tx-image-real-trust.jpg` **or** `two-trained-african-grey-parrots-sitting-on-mike-shoulder.jpg` |
| **Breeding-pair section** | `breeding-pair-african-grey-parrots.jpg` **or** `african-grey-breeding-pair-available.jpg` |
| **Fertile-egg section** | `fertile-grey-parrot-egg-for-sale.jpg` |
| **Reviews** | `review-Walter-Zander.jpg` · `review-Alene-Murphy.jpg` |

### 8a · Asset Proof — Measured 2026-07-30 (run `cag-asset-proofing` before every build)

**20 assets in the folder. Only 6 are ≥ 760px wide**, which is the width of the uniform in-body box. This decides the hero and it decides the framing letters, so it is recorded here rather than discovered mid-build.

| ≥ 760px wide (usable at native resolution) | Below 760px (blur-fill or accept upscale) |
|---|---|
| `mac-letia-…-real-trust.jpg` **1039×539** · `timneh-vs-congo-real-photo.webp` 1000×547 · `united-home-delivery-van-petsafe.webp` 1024×185 · `Mark-with the parrots.jpg` 800×600 · `jins-jeni1.webp` 800×600 · `jins-jeni4-…-eating-veggies.webp` 800×600 | `two-african-grey-congos-for-sale.jpg` 590×639 · `Congo-African-grey-pair-eating.jpg` 500×375 · `african-grey-breeding-pair-available.jpg` 500×431 · `breeding-pair-african-grey-parrots.jpg` 640×480 · `male-vs-female-…-inside-their-cage.webp` 640×480 · `jins-jeni-congo-…-pair.webp` 640×480 · `fertile-grey-parrot-egg-for-sale.jpg` 485×500 · `tamed-pair-…-on-shoulder.jpg` 310×400 · **`two-trained-…-on-mike-shoulder.jpg` 300×400** · `male-and-female-…-for-sale.jpg` 287×320 · `review-Walter-Zander.jpg` 293×320 · `review-Alene-Murphy.jpg` 203×319 · `affordable-…-shipping.jpg.webp` 640×362 |

Also in the folder: `african-grey-parrot-socialization-training copy.mp4` (7.6 MB) — a `.fs-video` candidate. It needs a `-760.webp` poster sibling, `preload="none"`, and **no autoplay**.

> ### ▣ APPROVAL GATE — Hero Image
> `[AI RECOMMENDS: **`mac-letia-young-african-grey-parrot-with-midland-tx-image-real-trust.jpg`**]`
> **Why, grounded in measurement:** the hero is baked to 1408×768 with a plain `ImageOps.fit` cover crop, and this is the **only** nominated file with the resolution to survive it — 1039×539 needs a 1.35× upscale, while the alternative `two-trained-…-on-mike-shoulder.jpg` is **300×400** and would need a 4.7× upscale into a landscape box it is the wrong orientation for. It is also the file the breeder named "real trust", it carries the Midland geo signal the page's local intent needs, and its aspect ratio is already close to the 16:9 target.
> **Trade-off, stated plainly:** it shows **one** bird, and this is a *pair* page. The pair proposition therefore has to be carried by the hero's secondary photos rather than its anchor image — which is precisely why §11 recommends a two-photo hero component rather than a single-image hero. If the breeder can supply a high-resolution two-bird shot (≥1400px wide), that file should take the anchor slot instead and this recommendation is withdrawn.
> Breeder approval: `[ ___ ]`

### 8b · The Framing Question — Pairs, Singles, and How This Page Differs From Jins & Jeni

The breeder's own note: *"If you don't want a pair, you can get a single bird — list all. You can also get Roys and Amie as a pair, Elad and Evie as a pair. How do we frame it? And how will this page be different from the Jins and Jeni page?"*

**The cannibalization answer, and it is the spine of the whole page.**

`/available/jins-jeni/` is a **single-listing product page**: one specific pair, one `Product` + `Offer`, 700–1,000 words. It answers *"tell me about these two birds."*

`/congo-african-grey-parrot-pair-for-sale/` is the **category page for pair intent**. It answers the question that comes *before* the listing: *"should I buy two birds at all, and if so, which two?"* It ranks for the pair keyword universe, carries `AggregateOffer` (group pages may, per skill §3.2), and routes down to the individual listings.

**Three pairing routes, sourced live from `clutch-inventory.json` + `price-matrix.json` — never hardcoded:**

| Route | Birds | Price | What it is |
|---|---|---|---|
| **Ready-made companion pair** | Jins ♂ + Jeni ♀ | **$3,500** | Unrelated, must go together. Links to `/available/jins-jeni/` |
| **Build-your-own pair** | Roys ♂ $2,300 + Amie ♀ $2,500 (Congo) · Elad ♂ $1,600 + Evie ♀ $1,500 (Timneh) | Sum of the two | Two singles bought together, introduced under supervision |
| **Proven breeding pair** | Adults held back | **$3,000** | Bonded, DNA-certified. Links to `/african-grey-breeding-pair-for-sale/` |

**And the honest fourth answer: one bird is fine.** The page must state plainly that a single well-socialised grey is not a lonely grey, list every available single with its price, and let the buyer step down to one. That honesty *is* the page's moat — every competitor pair listing pushes two birds because two birds is a bigger sale.

> ### ▣ APPROVAL GATE — Pair Framing
> Three routes plus the honest single-bird step-down: `[ ___ ]`
> Confirm no other pair page is planned that would cannibalise this one: `[ ___ ]`

---

## 9 · Infographics and the Asset Gate

The build can only start once I have dropped in all the generated infographics for every H2, H3, and H4 section that needs one.

Once the page is outlined, give me the **full prompt pack** for every H2, H3, and H4 header that will need an infographic.

> ### ▣ ASSET GATE
> **The build starts only after I have dropped in all the generated infographics.**
> ☐ Full prompt pack delivered for **every H2, H3, and H4 header** needing an infographic *(after the outline is approved)*
> ☐ Breeder drops in the infographics
> ☐ Breeder says **"start"**

---

## 10 · Components — Desktop and Mobile Versions

Use **new component styles** — pick from the list or the components folder, favouring ones we have not used before. Run the `cag-component-refresh` agent/skill over any other component that needs refreshing.

Both **mobile and desktop component versions** are covered here. To make each component easy to identify, I have listed their names in the `.md` file inside the for-sale folder. **Analyse every name**, so that when I say "use this component on this page" you can apply it without any mistake.

```
/Users/apple/Downloads/CAG/assets/1WORKING-ON/FOR-SALE-PAGES/component-designs
```

This page's component tuple must be **fully distinct** from every page already shipped. That includes the tables — and every table must stack crisply and cleanly on mobile.

| Item | Value |
|---|---|
| Components path | `/Users/apple/Downloads/CAG/assets/1WORKING-ON/FOR-SALE-PAGES/component-designs` |
| Component names reference | `assets/1WORKING-ON/FOR-SALE-PAGES/FOR-SALE-PAGES:components-NAMES.md` — read the full text **and** inspect the PNGs before building |
| Must be distinct from *(all 8 shipped)* | Eggs · Congo · Timneh · Hand-Raised · Health Guarantee · DNA-Tested · Baby · Adoption-Cost |
| Tuple ledger *(binding — record before building)* | `sessions/2026-07-19-for-sale-component-map.md` |
| Refresh tool | `cag-component-refresh` agent/skill |
| Tables | Must stack crisply and cleanly on mobile — recipe banked in memory `reference_mobile_table_stacking` |

**Never import a homepage or comparison component onto a for-sale page.** This cost a full v3 rebuild of the Egg page. No `NewsletterV2`, no comparison hero, no green counter strip, no comparison circular-emblem seam. The for-sale cluster has its own kit.

---

## 11 · The Five Heroes

There are **five heroes** to choose from for these pages. Screenshots of all five sit in the folder path above, and each can be identified either by the component names I have listed or by reading the name directly from its screenshot.

**Which hero for this page?**

The locked cluster assignment (Part II·C) puts *pair and family* pages on **Hero-A Scattered Flock**. That default collides: Hero-A is already spent on Hand-Raised, where it ships as a rotated 2×2 grid of four Polaroids.

> ### ▣ APPROVAL GATE — Hero Component
> `[AI RECOMMENDS: **Hero-A refreshed as a "Bonded Duo" — two large paired Polaroids, not a four-up scatter**]`
> **Why:** the page's entire proposition is *two birds together*, and a hero that shows one bird undercuts the H1 before a word is read. Hero-A is the only kit hero built to carry multiple bird photos, so the family is right; the refresh is what keeps the tuple distinct from Hand-Raised. Two tiles instead of four also solves the §8a resolution problem — two larger tiles need fewer usable source files, and we measured only six assets at or above 760px.
> **Trade-off:** it reuses the Hero-A name, so this page's tuple distinctness has to be earned in the dial, rail, TOC, takeaway, table and FAQ slots rather than in the hero slot. Recording the tuple in the component-map ledger before the build is therefore mandatory, not optional. The alternative — Split-Hero A trust ribbon — would be a cleanly unused hero, but it is a single-image left-hand layout and cannot show a pair.
> Breeder approval: `[ ___ ]`

---

## 12 · Desktop and Mobile Image Styles

Which desktop and mobile **image** styles are we using on this page? Choose from the options below. Full named spec: `IMAGE-DESIGNS.md §7`.

### 12a · Desktop

| Letter | Style | Use |
|---|---|---|
| **B** | Blur-Fill | Default for single birds — premium, zero crop, no bars |
| **A** | Contain-Canvas | Infographics and wide images |
| **C** | Editorial Split | — |
| **H** | Duo Strip | Sibling and pair shots |
| **E** | Top-Anchored Cover | When you want it to fill punchy |

**Trade-off:** B looks the richest but adds a blurred layer, making it slightly heavier; A is the lightest but shows soft side-padding on very tall portraits.

### 12b · Mobile

| Letter | Style |
|---|---|
| **mC** | Blur-fill 4:5 (matches B) |
| **mA / mH** | Cover shots |
| **mG** | For the pair |
| **mB** | Contain |

- Styles **A, B, C, D, G, H** and **mB, mC, mE, mG** all work with the existing photos.
- Only **F (Art-Directed Wide)** needs new or wider source photos.

> ### ▣ APPROVAL GATE — Style Letters
> **To finish this, reply with your desktop letters and your mobile letters** — for example: *"Desktop A, B, C, H, E · Mobile mC, mA, mH, mG, mB."*
> `[AI RECOMMENDS: **Desktop H, B, A, E · Mobile mG, mC, mB, mA**]`
> **Why:** **H Duo Strip leads** because it is the one style built for pair shots, and this page has five two-bird photos to place. **B Blur-Fill** takes the single-bird portraits — it is the locked default and, critically, it is the only style that survives the §8a resolution problem, since a blurred backdrop hides that the foreground is a 500px master. **A Contain-Canvas** takes the infographics so no baked-in label is ever cropped, and **E Top-Anchored Cover** takes the wide scene shots. On mobile, **mG is the pair style** and pairs with H; mC blur-fill 4:5 pairs with B; mB contain protects the infographics.
> **Trade-off:** B and mC add a blurred layer, so those images ship heavier than a plain cover crop. Given that 14 of the 20 assets are below 760px wide, that weight is the price of not showing a visibly upscaled bird — worth paying here, and it is the reason the recommendation is not the lighter A-everywhere option.
> Desktop: `[ ___ ]` · Mobile: `[ ___ ]`

---

## 13 · Section Architecture — 22+ Sections

The page needs **mandatory sections**, **competitor-based sections**, and **suggested/recommended sections** — **22+ sections in total**.

Do not mirror any existing sibling page. Write from the outline, per the **Write-From-Outline** rule (CLAUDE.md #1, plus memory, and now the for-sale skill).

| Tier | Sections |
|---|---|
| **Mandatory** | Hero · Counter Snippet (**4 or 6, depending on the page — never 5 or 7**) · refreshed Key Takeaway · TOC · and the rest |
| **Competitor-based** | *(derived after competitor analysis)* `[ ___ ]` |
| **Suggested / recommended** | *(derived after competitor analysis)* `[ ___ ]` |
| **Total** | **22+ sections** |

---

## 14 · Deep Competitor Analysis — Mandatory

Using the other completed pages in this cluster as the model, run a deep competitor analysis for the primary keyword across Google, Bing, Reddit, Facebook, Instagram, YouTube, and every other relevant site — exactly as we did for the DNA-Tested page.

| Platform | ☐ |
|---|---|
| Google | ☐ |
| Bing | ☐ |
| Reddit | ☐ |
| Facebook | ☐ |
| Instagram | ☐ |
| YouTube | ☐ |
| All other relevant sites | ☐ |

- **Blocked sites:** use the research skill `skills/research-recency -last30days` for Reddit and anything else that blocks the normal fetchers.
- **Scope:** the **top 10** competitors on every platform, **plus the 30+** competitors already in our list.
- **Deliverables:** everything — the same set we produced for the previous pages.

> **This is mandatory and cannot be skipped.** Neither can the next part. The full **fan-out queries**, the **grill-me sprint**, and the **components sprint** are all crucial before any page can be approved as a pass.

---

## 15 · Blended Strategies and Frameworks (EEBP)

Use the following framework as part of the blended framework set.

`/framework-eebp` — the critical clarification: the existing `framework-ebp` skill is **Evidence → Baseline → Profile**, and `cag-entity-agent` uses **Entity → Benefit → Purpose**. Both differ from what is wanted here. **EEBP = Entity → Evidence → Benefit → Purpose** is a genuinely distinct fourth framework, which is precisely why it kept collapsing into the other two. It has therefore been created as its own skill, using the skill-creator methodology, so it can never be confused again.

| Name | Expansion | Note |
|---|---|---|
| `framework-ebp` | Evidence → Baseline → Profile | Existing skill |
| `cag-entity-agent` | Entity → Benefit → Purpose | Different again |
| **`/framework-eebp`** | **Entity → Evidence → Benefit → Purpose** | **The distinct fourth framework** |

---

## 16 · Two New Verified Reviews

Two new verified reviews, with images, for this page. The review images are in the folder below and can be identified by name — `review-Walter-Zander.jpg` and `review-Alene-Murphy.jpg`:

```
/Users/apple/Downloads/CAG/assets/1WORKING-ON/FOR-SALE-PAGES/1CONGO-AFRICAN-grey-parrot-pair/
```

> **Real customer reviews — reproduced verbatim. Never alter the wording of a real review.** These two are also the *only* text on this page permitted to match a sibling verbatim, and only because they are whitelisted furniture. Both are on-query for the pair keyword set, which is why they belong here rather than on another page.

### ★ Review 1 — Walter Zander, Fort Washington, PA

⭐⭐⭐⭐⭐

> After weeks of searching for an affordable African grey parrot pair, I finally found C.A.G.s, and the experience exceeded every expectation. Teri patiently answered all my questions, provided recent photos, health records, and explained the personalities of both birds before I committed. The pair arrived healthy, well-socialized, and already comfortable around people. It's rare to find such quality, transparency, and fair pricing in one place. If you're looking for an affordable African grey parrot pair, I highly recommend C.A.G.s for their professionalism, ethical breeding practices, and exceptional customer service.

— Walter Zander, Fort Washington, PA

### ★ Review 2 — Alene Murphy, Savannah, GA

⭐⭐⭐⭐⭐

> Finding a reliable African grey parrot pair for sale wasn't easy until I discovered C.A.G.s. Their honesty, professionalism, and knowledge immediately gave me confidence. The birds were exactly as described—healthy, affectionate, and beautifully cared for. Even after delivery, the team continued providing advice on diet, enrichment, and acclimation. I couldn't be happier with my experience, and I highly recommend C.A.G.s to anyone searching for an African grey parrot pair for sale from a breeder that genuinely cares about both the birds and their new families.

— Alene Murphy, Savannah, GA

> ⚠️ **Open flag for the breeder.** Review 1 reads *"Walter patiently answered all my questions"* — the reviewer's own first name. If that is a transcription slip for Mark or Teri, say so and it will be corrected at source; **it will not be silently edited**, because the standing rule is that real review wording is never altered. Left as-is until the breeder rules. `[ ___ ]`

**Rating arithmetic.** These two reviews do not change the site-wide aggregate. It stays **4.9 from 52 real reviews**. Never ship a fabricated `reviewCount`.

---

## 17 · Workflow — The Seven-Sprint Pipeline

Verify that the workflow has **no skipped levels**, so the finished page never feels rushed.

### 17a · Why Sprint 3 Was Added

Sprint 3 is the one to add, and the reasoning is grounded in our own history. The Hand-Raised page passed every static gate and still came back as "feels rushed." There were five root causes, and the memory record confirms that **none of them was visible in a source review**.

We already had `page_hardening_scan.py`, built for exactly this problem — but it sat outside the named pipeline and outside `CLAUDE.md`, which made it optional in practice. The point was proven again that same day: three further defects that only a rendered mobile viewport reveals.

Sprint 6 pays for itself too. That hardening pass found the same infographic bug on four other live pages, and the fixes were cheap precisely because the memories already existed.

### 17b · The Pipeline

| Sprint | Name | Work | Gate |
|---|---|---|---|
| **0** | Intel | `competitor-intel --all` + keyword-gap + gsc-analytics + research-recency | **[REVIEW]** |
| **0.5** | Orient | grill-me + fan-out | **[APPROVE]** |
| **1** | Blueprint | Visual companion + framing letters + matrix + H1–H6 + header dup-gate | **[APPROVE]** |
| — | **── ASSET GATE ──** | Breeder drops in the infographics and says **"start"** | ⛔ |
| **2** | Build | `for-sale-page-builder` + EEBP + dup-gate (during the build) | |
| **3** | Harden | `page_hardening_scan` + runtime probes at 375 / 768 / 1280 + contrast + overflow | **← NEW** |
| **4** | Final | `final-page-pass` + keyword-verifier + anti-ai-writing | |
| **5** | Ship | Sitemap + push + deploy-verify + live 200 | |
| **6** | Bank | `session-closer` + memory + back-propagate fixes to siblings | |

### 17c · The Full Workflow, Top to Bottom — Which Skill Fires When

This is the authoritative per-page routing table. Nothing is skipped, and every gate names the artifact it produces, so "done" is never a judgement call.

---

#### **Sprint 0 · Intel** — *no page may be planned on assumptions*

| Step | Invoke | Produces |
|---|---|---|
| 0.1 | `@cag-competitor-intel --all` | Top-10 competitors per platform for the pair keyword + the 30-competitor registry sweep |
| 0.2 | `@cag-competitive-keyword-gap-agent` | Gap matrix, opportunity-scored 1–10 |
| 0.3 | `@cag-gsc-analytics` | Real query positions from `docs/research/for-sale-keywords-2026-07.md` and the fresh CSVs. **Never invent keyword data** |
| 0.4 | `/research-recency` + `/reddit-strategy` | Reddit and blocked-site signal via the escalation ladder. Un-fetchable is written `NOT FETCHED`, never invented |
| 0.5 | `@cag-paa-agent` | The real PAA set for the primary keyword |
| 0.6 | `@cag-llm-keyword-intel` | LLM visibility baseline. **Open flag #10: never yet run on any cluster page** |
| **Gate** | **[REVIEW]** | `sessions/YYYY-MM-DD-<slug>-sprint0-research.md` — SERP snapshot · section inventory · gaps · keyword universe · entity map · visual blueprint · PAA set |

#### **Sprint 0.5 · Orient**

| Step | Invoke | Produces |
|---|---|---|
| 0.5.1 | `/grill-me` | Session brief on disk, checkpointed answer by answer |
| 0.5.2 | `/keyword-cluster` | Primary / secondary / LSI / long-tail / PAA tiers, feeding §3b metric 1 |
| 0.5.3 | `@cag-angle-agent` | 5–10 angles, hooks, counter-intuitive POVs |
| 0.5.4 | `@cag-strategy-synthesizer` | **Two** reverse-engineered strategies plus one blended, one marked **(Recommended)** with a data-grounded why and a named trade-off |
| **Gate** | **[APPROVE]** | The chosen angle and strategy |

#### **Sprint 1 · Blueprint** — *the longest gate, and the cheapest place to fix anything*

| Step | Invoke | Produces |
|---|---|---|
| 1.1 | `@cag-content-audit-agent` | 4-phase pre-build audit |
| 1.2 | `/framework-heading-hierarchy` | **Full H1→H6 outline** — no skipped levels, all six levels, **≥5 H5 and ≥5 H6**, Title Case throughout, plus the **declared header style** from §3a |
| 1.3 | `/cag-duplicate-content-gate --headers` | Header dup-gate **run before outline approval**, pairwise against all 8 siblings plus the comparison cluster |
| 1.4 | `/cag-entity-agent` → `@cag-entity-incorporation-agent` | 85–112 distinct entities, bounded by the Verified-Claim Ledger |
| 1.5 | `/cag-seo-master-checklist` | Distribution matrix: section taxonomy · ordered topic→micro stack · framework per section · word-count split · **A / B / C categories** with a grounded why on every B and C row |
| 1.6 | `/cag-cta-strategy` | The ≥5 action CTAs of §6, placed on a 500–700-word cadence |
| 1.7 | Visual companion | Clickable skeleton, hero comparison, section-layout screens |
| 1.8 | `/superpowers:writing-plans` | The approved blueprint becomes a checkbox task plan in `docs/superpowers/plans/` |
| **Gate** | **[APPROVE]** | Outline · matrix · framing letters · component tuple recorded in the ledger |

#### **── ASSET GATE ──** ⛔

Prompt pack delivered for every H2/H3/H4 needing an infographic → breeder drops the images → **breeder says "start"**. Then `/cag-asset-proofing` runs over the drop: resolution, `.jpg` vs `.webp` taxonomy, and **read the baked-in text on every AI infographic** (this caught "BREDDER", "HOME HOME", and a tight "Polyomavirus" on Hand-Raised).

#### **Sprint 2 · Build**

| Step | Invoke | Note |
|---|---|---|
| 2.1 | `/cag-for-sale-page-builder` | Section by section, straight from the approved matrix. **Write-From-Outline, never from a sibling** |
| 2.2 | `/framework-eebp` | Entity → Evidence → Benefit → Purpose, under every header |
| 2.3 | `/cag-branded-search-skill` + `/cag-branded-hybrid-keywords` | Branded targets and Contextual-Intelligence local intent |
| 2.4 | `/internal-link-agent` + `@cag-external-link-agent` | Link-First anchors, ≥6 external across ≥6 domains, **Anchor Diversity Ledger enforced by script, never by eye** |
| 2.5 | `/anti-ai-writing` + `@cag-non-commodity-content-agent` | Zero AI tells; breeder-authentic detail |
| 2.6 | `/cag-infographic` + `/cag-component-refresh` | Uniform `.sec-img.inf-img` boxes; layout and accent deltas so the page is not a sibling clone |
| 2.7 | `/cag-duplicate-content-gate` (body) | Run **during** the build on your own draft, not after |

#### **Sprint 3 · Harden** — *the sprint that exists because a page passed every static gate and still felt rushed*

| Step | Invoke | Catches |
|---|---|---|
| **3.0** | **`/cag-gate-integrity` — read FIRST** | 12 recorded false or empty reports. **Verify every finding against the built page before editing anything, and read a gate's own examined count before believing a PASS** |
| 3.1 | `python3 scripts/page_hardening_scan.py <slug>` | Title Case · `img-no-srcset` · opacity-dimmed text · small clay contrast · unwound absolute hero · smooth-scroll · **§1k markup-css-drift** · **§1l colour specificity** |
| 3.2 | `python3 scripts/seam_parity.py <slug>` | Seam count against real section count. **Never re-derive this with grep** |
| 3.3 | Playwright runtime probes at **375 / 768 / 820 / 1024 / 1280** | Horizontal overflow · real-`ch` line length · contrast · tap targets · sticky-rail collisions. The Browser pane reports `vw:0`, so every probe false-passes there — **measure in Playwright** |
| 3.4 | `/impeccable audit` → `/impeccable critique` → `/impeccable harden` → `/impeccable polish` | Technical quality, then heuristic UX review, then edge cases, then the final craft pass |
| 3.5 | `/frontend-design` | The absolute bans: no side-stripe borders, no gradient text, no decorative glassmorphism, no identical card grids, no em dashes in copy |
| **Loop** | **Any component that still feels rough goes back to 3.4** | Do not advance a rough component to Sprint 4 |

#### **Sprint 4 · Final**

| Step | Invoke | Bar |
|---|---|---|
| 4.1 | `/cag-aeo-pass` + `python3 scripts/aeo_audit.py <slug>` | BLUF openers · atomic sections · entity-rich naming · declarative sentences · citation formatting · brand ownership · **schema-only freshness, zero visible dates** |
| 4.2 | `@cag-keyword-verifier` | The §3b four-metric table plus 1–2% primary density |
| 4.3 | `/cag-duplicate-content-gate` + `--headers` | Zero non-whitelist crossover, on `dist/` |
| 4.4 | `@cag-accessibility-fixer` | WCAG 2.1 AA, verified in Lighthouse |
| 4.5 | `/cag-final-page-pass` → `python3 scripts/final_page_audit.py --for-sale` | One PASS / PASS-WITH-WARNINGS / FAIL verdict. Word band **3,000–8,000** |
| 4.6 | `/cags-comprehensive-page-audit-system` | Only if 4.5 scores low — the 17-section strategic audit |

#### **Sprint 5 · Ship**

`python3 scripts/generate_sitemaps.py` → `@cag-canonical-fixer` → commit + `git push origin main` (**push is the deploy**) → `@cag-deploy-verifier` live 200 + IndexNow → `/sitemap-agent`.

#### **Sprint 6 · Bank**

`/session-closer` → write the memory → **back-propagate every fix to the 8 shipped siblings**. This is where the pass pays for itself: the Hand-Raised hardening pass found the same infographic-crop bug on four live comparison pages, and the fixes were cheap because the memory already existed.

---

### 17d · The Component Quality Bar — "Must Not Feel Rushed"

The breeder's rejection phrase for Hand-Raised was **"feels rushed"**, and none of the five root causes was visible in a source review. These are the standing conditions of done.

**Every component, at every breakpoint.**

- ☐ Clean, smooth, fluid, modern — no component ships rough. If one feels rough, it goes back through `/impeccable critique` → `harden` → `polish` before Sprint 4, however many loops that takes.
- ☐ **Type sizing fits at all three widths.** No oversized headers; H2 clamped and checked at 375px; even paragraph rhythm; body capped at 65–75ch measured with a **real `ch`**, never `0.5em`.
- ☐ Motion ≤ 0.2s, ease-out. No bounce, no parallax, no autoplay.
- ☐ Warm-tinted shadows only. Never neutral grey.
- ☐ Line-icon SVGs, never emoji. Never 🦜 — use `/emoji/cag-congo.png` and `cag-timneh.png`.
- ☐ Tables stack to one card per row at ≤640px.
- ☐ Every table, card, dial row and pill clears the 24px tap-target floor.
- ☐ Zero horizontal overflow at 375px. `overflow-x:clip` **hides** this defect — probe `scrollWidth` *and* look at whether text is clipped.
- ☐ Hero 350–400px on desktop, images first on mobile (`order:-1`), copy first on desktop.
- ☐ **Spaces around `+` and `−` inside every `clamp()` and `calc()`** — without them the declaration is silently dropped, which is what left a hero at 524px.

---

## 18 · Verified Results the Page Must Pass

Keep this as the saved reference standard.

| Check | Result |
|---|---|
| Contrast sweep | 0 failures across 443 elements |
| Horizontal overflow at 375px | None — it had been pushing text off-screen |
| Body links underlined | 10 of 10 |
| Dup gate (body + headers) | 0 crossovers |
| Body-anchor collisions site-wide | 0 — anchors already rotate LSI and long-tail variants |
| Primary keyword density | 1.78% (target 1–2%) · 111 first-person tokens · 0 AI tells |
| Card heights and CTAs | Uniform; buttons hug their labels at 124–145px, down from 200px stretched |

---

## 19 · Root Causes Found — Saved Reference

These were traced to specific lines, not guessed.

| Complaint | Actual cause |
|---|---|
| Mobile hero broken | `.pofig{position:absolute;width:44%}` is never unwound below 980px, so the absolutely positioned children collapse inside a 300px box |
| Mobile jump-rail "not working" | `.railB` is `z-index:40`, sticky at `bottom:0`, sitting underneath `MobileTabBar` (`fixed bottom-0 z-50`). It renders correctly — it is simply buried |
| Infographics too zoomed | The mobile rule forces `aspect-ratio:5/4` and `object-fit:cover` onto a 16:9 infographic, shaving roughly 30% off each side, which is why the baked-in text is cut |
| Buttons too wide, wrapping to two lines | `.bfull{width:100%}` combined with a long `Inquire about {name} →` label |
| Badge covers the bird's head | `[cause not captured in the source notes — placeholder]` |

**Jump-rail verification:** the rail is sticky at exactly 96px, stands 62px tall, and tapping a chip lands the target H2 18px below the rail — clearing both bars.

---

## 20 · Desktop Dial TOC — Locked Spec

The desktop dial TOC now matches Timneh. An earlier density pass went too far: rows had been shrunk to `.7rem` with 3.5px padding, and the tag pills hidden. It was reverted to Timneh's `.tdial` spec byte for byte.

| Spec | timneh | hand-raised |
|---|---|---|
| Width | 196px | 196px |
| Rows | 18 | 18 |
| Font | 11.84px | 11.84px |
| Padding | 5px 7px | 5px 7px |
| Line-height | 14.8px | 14.8px |
| Card height | 705px | 723px |

The 18px difference in card height is label wrapping, not styling. No row falls below the 24px WCAG tap-target floor, and contrast measures 7.27 (label), 5.00 (numeral), and 4.77 (tag). This is locked as the cluster-wide canonical spec in the skill (§1e-bis) — only the palette changes from one page tuple to the next.

---

## 21 · Hero Image Order and Height

**The hero image comes first on the page**, and the desktop hero stands **350–400px** tall, per the rule. If a page does not follow this, add it — every page in the cluster uses the same height.

| Fix | What was done | Verified |
|---|---|---|
| Hero images first on mobile | `.hero-scatter{order:-1}` below 980px — the same mechanism the siblings use (`.chero-media{order:-1}` on Congo and Timneh) | Scatter at y=139, copy at y=546 ✅ Desktop still renders copy-left, photos-right |

---

## 22 · Bird Card Label Placement

Take the Roys card below as the worked example: **no label on a bird card may cover the bird's head, face, or beak.** Place every label where it will not cover the bird's face.

> Roys' "Congo Grey" label: added a per-bird `badge:"top"` flag → `.bbadge.badge-top`. Moved to the top-left on both desktop and mobile, while the other five cards keep the bottom-left position. Roys is offset 8px from the top of the photo; the others sit at 134px on mobile and 194px on desktop. ✅

---

## 23 · Example of Done — Reference Build

`/dna-tested-african-grey-for-sale/` has been rebuilt to the for-sale kit and is live on `main` (commit `38f8437`; pushed, therefore deployed).

**What was done.** Verified first, then built. All four deliverables were read — Sprint 0, Sprint 0.5, the Sprint 1 blueprint, and the prompt pack — the 12 dropped infographics were confirmed to match the pack filenames exactly, and the page was built strictly to the approved blueprint. Nothing was re-planned or re-outlined.

**The page** — `src/pages/dna-tested-african-grey-for-sale/index.astro`, 18 sections, 70 headings, roughly 3,860 body words:

- **Angle:** "Proof, Not Guesswork." The informational myth-bust — that you cannot sex a grey by eye — earns the entry, and the certificate and the birds then convert it. That is the deliberate trade-off the blueprint accepted, since the head term carries no transactional demand.
- **Fully distinct tuple:** Hero-C Mosaic Metrics · Dial 1 clay + Rail A · T2 Chip Cloud · K4 + K5 · new Table D "Lab Report" + Table A · FAQ-A refreshed · Avail-B faceted by confirmed sex, where the siblings facet by subspecies.
- **No crossover except the review.** The hen/cock register and the "From the Lab:" / "On the Record:" H6 prefixes keep it clean; the dup-gate passes on both body and headers, with only the two real reviews — which are whitelisted — matching Hand-Raised.
- **Corrected two false claims carried by the live stub:** "99.9%" became ~99%, and "at no additional charge" became a certificate priced at $40–60. The lab is named as Avian Biotech / Animal Genetics.

---
---

# 📚 Part II — Cluster Build Record

**Everything we have done across the six for-sale cluster pages.**

Compiled 2026-07-25 from `sessions/2026-07-19-for-sale-component-map.md`, the project memory store, and the live page files on disk. This is the "check the saved data on everything we did well and badly" reference called for in [§4](#4--deliverables-and-approval-requirements).

---

## II·A — Program Status

| Reference | Location |
|---|---|
| Program plan | `docs/superpowers/plans/2026-07-19-for-sale-pages-program.md` |
| Canonical skill | `skills/cag-for-sale-page-builder.md` |
| Component ledger *(binding — every tuple is recorded here)* | `sessions/2026-07-19-for-sale-component-map.md` |
| Keyword mining | `docs/research/for-sale-keywords-2026-07.md` — 793 GSC queries bucketed across 22 pages |

| # | Page | Slug | Live | Cluster position |
|---|---|---|---|---|
| 1 | Fertile Eggs | `/african-grey-parrot-bird-eggs-for-sale-usa/` | 2026-07-20 | Page 1 of 22 |
| 2 | Congo | `/congo-african-grey-for-sale/` | 2026-07-21 | Page 2 |
| 3 | Timneh | `/timneh-african-grey-for-sale/` | 2026-07-22 | Page 3 |
| 4 | Hand-Raised | `/hand-raised-african-grey-parrot-for-sale/` | 2026-07-22 | Page 4 |
| 5 | Health Guarantee | `/african-greys-for-sale-with-health-guarantee/` | 2026-07-25 | Page 5 |
| 6 | DNA-Tested | `/dna-tested-african-grey-for-sale/` | 2026-07-24 | Page 6 |
| 7 | Baby | `/baby-african-grey-parrot-for-sale/` | 2026-07-27 | Page 7 |
| 8 | Adoption Cost | `/african-grey-parrot-adoption-cost/` | 2026-07-27 | Page 8 |
| **9** | **Congo Pair — CURRENT TARGET** | `/congo-african-grey-parrot-pair-for-sale/` | *stub, rebuild pending* | **Page 9, Cluster 3 opener** |

**Eight of 22 built** (verified on disk 2026-07-30: eight `index.astro` files at 100–124 KB). **Fourteen remain** — 9 for-sale and 5 buy-prefixed. The remaining for-sale slugs are all stubs of 4–20 KB.

**Page 7 — Baby** · `/baby-african-grey-parrot-for-sale/` · weaned-first angle · Split-Hero B refreshed · Avail-B faceted by age band · PDB + BAB, first use in the cluster · Reddit used as an evidence base. Memory: `project_baby_page_build`.

**Page 8 — Adoption Cost** · `/african-grey-parrot-adoption-cost/` · Number→Ledger→Thesis spine · price-ladder hero · new Table G · the `.ctool` first-year calculator. The asset folders turned out to be infographics rather than photos, and five were rejected on intake — which is why `cag-asset-proofing` now runs at the Asset Gate. Hardened 2026-07-28. Memory: `project_adoption_cost_pack_ready`.

> **Both pages shipped with empty infographic slots by breeder choice** (build first, images last). Nothing renders a broken box; the slots simply carry no image yet. Prompt packs are written and collision-checked.

### Measured on Disk, 2026-07-25

| Page | H1 | H2 | H3 | H4 | H5 | H6 | Rendered words\* | Images | External domains |
|---|---|---|---|---|---|---|---|---|---|
| Eggs | 1 | 16 | 19 | 13 | 11 | 5 | 6,297 | 54 | 8 |
| Congo | 1 | 15 | 17 | 13 | 11 | 6 | 6,063 | 52 | 7 |
| Timneh | 1 | 18 | 18 | 13 | 12 | 6 | 6,615 | 54 | 7 |
| Hand-Raised | 1 | 18 | 21 | 9 | 9 | 6 | 5,316 | 50 | 10 |
| DNA-Tested | 1 | 18 | 20 | 15 | 11 | 8 | 6,985 | 53 | 10 |
| Health Guarantee | 1 | 17 | 19 | 11 | 6 | 6 | 6,977 | 32 | 7 |

\* The full rendered `dist/` page, including header and footer chrome. Recorded **body** word counts: DNA-Tested ≈3,860; Eggs v2 5,309.

> ⚠️ **Health Guarantee sits at H5:6 / H6:6.** The Heading Outline Gate floor is five of each, so it passes — but it is the thinnest page in the cluster at the deeper levels. Any rebuild should add H5 depth.

---

## II·B — Per-Page Dossiers

### ▸ Page 1 — Fertile Eggs

`/african-grey-parrot-bird-eggs-for-sale-usa/` · Live **2026-07-20** · page-scoped `.egg`
Built v1 → v2 (`8ed5782`) → **v3 component-fidelity rebuild** → v4 polish (`f8d5091`)

| Field | Value |
|---|---|
| **Offer model** | **Model B** (breeder-locked) — we ship fertile eggs nationwide at **$95 per egg**, buy five and US shipping is free, **$200 deposit**, *"experienced breeders only — no incubation support included"* |
| **Angle** | Truth-forward. The page leads with "almost all egg listings are scams — here is why we are the verifiable exception," then converts. It strips every "100% fertile" and "guaranteed hatch" scam tell that the old page carried. |
| **Frameworks** | PAS → FAB → QAB |
| **H1** | V1 — *Candled, Documented, Shipped* |
| **Tuple** | Split-Hero C dark · **Dial 1 + Rail A** · Dial 1 **is** the TOC (fs:02 folded in — one navigation element rather than two, avoiding a double TOC under a dark hero) · **K4 Clipboard + K1 Receipt** · Table A · **FAQ-C dark badge-numbered** |
| **Schema** | One Product + Offer (the egg, InStock), plus FAQPage and BreadcrumbList |
| **Video** | `<video controls preload="none" poster=…>` — **no autoplay**, per the design rule. A 4.2 MB mp4 in `public/images/egg-page/`. `.video-wrap` uses the same 760px 16:9 box as `.sec-img.inf-img`. |

**v2 expansion** grew the page to 5,309 words across 15 H2 sections. It added: Inside Our Nursery, with the hand-rearing video; Packing and Shipping, with the $185/$350 cards and the real egg-flats photo; Health and Guarantee, covering PBFD/APV PCR with `.health-card`; Available Now, listing all six birds, the breeding pair, and the eggs `pair-row`; Buyer Stories from Richard Woodard and Archie Obrien; and How We Compare — a seven-row `otA` competitor table that **ends the page**, per the breeder.

**v3 component-fidelity rebuild.** The breeder rejected v2 for using homepage and comparison components. It was swapped to the real for-sale kit: a Split-Hero C dark charcoal card with a 2×2 photo grid; for-sale outlined stat cards for the counter, rather than the green strip; an **Avail-B sticky sidebar filter** with live counts and a JS `.hide` filter; **FAQ-C** dark badge-numbered; `.fs-nl` newsletters relocated contextually; the kit two-column contact form; a `.fs-video` framed video; and a **new wordmark seam** derived from `NEW-FOOTER-LOGO copy.png` → `public/cag-fs-seam-emblem.webp`. The **dial was fixed** — it had been static — using an IntersectionObserver scroll-spy that fills the conic `--p` ring and drives an "x of 16" counter. The rebuild also added the blog "Keep reading" `.read-cards`, two GEO fact tables, and a Hatching-Success checklist, and moved the meta to the extended three-part 280-character format, which is now both a `CLAUDE.md` rule and skill §6a.

**🔴 Image taxonomy — this cost a full v2 rebuild.** In the drop folder, **`.jpg` and `.jpg.webp` files are the real C.A.Gs aviary photos** — hen on nest, brooder chicks, hand-fed babies, egg flats — while **`.webp` files are the AI-generated infographics and AI "photo" reference cards.** Version 1 wrongly treated the AI `.webp` files as OG photos, and never used the real `.jpg` shots or the chicks video. **The rule: real aviary photos anchor the page, infographics fill the analytical slots, and the video is embedded. Always `Read` every dropped image and sort by extension before building.**

**AI reference-card spec-panel lesson (still binding).** Some AI `.webp` exports were 1408×768 reference cards — a clean photo occupying the left ~72%, with a baked-in spec panel on the right ~28% listing palette, "1408×768", and a negative list. The fix is to crop the source to the left 73.5%, then run `ImageOps.fit` to 16:9.

**Site-wide reconciliation.** Scam-module flag #04 on `/how-to-avoid-african-grey-parrot-scams/` was reworded. The blanket claim — *"eggs are always a scam / no legitimate seller ships eggs / zero legitimate use case"* — now targets the **fake-farm pattern** (anonymous sellers, flat multi-species pricing, free cages, no licence) and links to the verifiable exception, so the site no longer contradicts the Model B egg page.

**Passes run.** Anti-AI: **0 tell-phrases**. First-person: **174** instances of we/us/our. Keyword-verifier: the primary grey + egg term appears **44 times at roughly 0.8% density**, with full Bing and Google coverage and no stuffing. Lighthouse: **Accessibility 100, Best Practices 100, SEO 100, CLS 0, TBT 0** — Performance read 68, inflated by the python `http.server`, against a real CDN figure of about 90. `final_page_audit.py`: **PASS-WITH-WARNINGS**. Dup-gate: **0 header, 0 body** crossovers, apart from the two shared real testimonials.

**Two accessibility defects fixed:** a `role="table"` on a `div` that wrapped a real `<table>` (removed), and a `.bird-photo` link whose `aria-label` did not match its visible badge text (removed, with `tabindex="-1"` added).

---

### ▸ Page 2 — Congo African Grey

`/congo-african-grey-for-sale/` · Live **2026-07-21** · page-scoped `.congo`
It replaced a thin stub carrying two H2s and stale $1,500/$3,000 pricing.

| Field | Value |
|---|---|
| **Spine** | Trust-First anti-scam — **AIDA × EBP × PAS** |
| **Positioning** | A money page, built mobile-first: **mobile CTR is 4.62% against 0.47% on desktop** |
| **Bing disambiguation** | The H1 and title both carry "parrot" and *Psittacus erithacus*, so the country-entity hijack cannot bury the page |
| **Tuple** | Split-Hero B warm gradient · **Dial 2 Dark-Aviary** (Eggs used Dial 1 clay) + Rail A · **T5 Reserve-Path stepper**, four steps with read-times · **K1 Receipt + K4 Clipboard + K3 Green-Ledger** · Table A · **FAQ-A light bordered**, per the breeder's rule: "use the other FAQ component" |
| **Inventory** | Roys ♂ **$2,300** · Amie ♀ **$2,500** · Bery ♀ **$1,700** · companion pair Jins & Jeni **$3,500**. The filter is `variant==congo_african_grey && status==available`, which excludes the sold Joys, Loti, and Carl, along with the Timneh birds Elad and Evie. **Prices and counts always come from `clutch-inventory.json` — never hardcode them.** |
| **External links** | Four — APHIS, AAV, parrots.org, and CITES. The arrow is added automatically by `.congo-main p a[target="_blank"]::after{content:"\2197"}`, so no manual spans are needed. |

**Images.** The breeder supplied eight AI infographics (P1 hero through P8 lifestyle), real OG bird, lifestyle, and shipping photos, and mp4 videos, all from `assets/1WORKING-ON/FOR-SALE-PAGES/CONGOS-For-Sale/`. The pipeline is PIL `ImageOps.fit` to 1408×768 — hero 1280×960, cards 800×720 — then a WebP quality-walk under 95 KB plus a `-760` sibling, output to `public/images/congo-page/`. Every H2, H3, and key H4 carries an image. The "zoom on mobile" treatment is `.sec-img.og-photo{aspect-ratio:5/4}` below 900px — **photos only; infographics stay at 16:9 so their labels survive.** Note that some source filenames begin with a space (` african-grey-parrot-training-free-play.webp`), so they must be quoted. The P5 price infographic was regenerated by the breeder and swapped in on 2026-07-21 to fix a typo.

**🔴 Dup-gate lesson.** Modelling sections on the Egg sibling reintroduced roughly **12 verbatim prose runs** — the verify-in-60-seconds opener, the health opener, the legal and CITES sentences, the ship-card copy, the video fallback, the resources intro, and the reserve-form intro — along with the *"How Can You Verify C.A.Gs in 60 Seconds?"* H3 crossover. All Egg-sibling prose and that header must be reworded before the final pass. The shared verified reviews, the shipping line, and one CITES-notice heading are cluster-wide furniture and stay verbatim.

**Final-touch pass, 2026-07-21 — reusable across the cluster:**

1. **Avail-C clean-card spec.** The dark-scrim, text-over-photo tile read as bulky and hid the bird's face. The locked replacement is a face-first card: a square `.ac-photo` at aspect 1/1, with per-bird `object-position`, carrying a small dark-green uppercase badge, above a white info panel holding the name and clay price on one row, a two-line-clamp blurb, and an always-visible full-width clay pill reading "View *name* →". Below 640px the blurb is hidden, the name and price stack, and the cards fall into a 2×2 grid. Card images ship `-440.webp` siblings with `srcset` and `sizes="(max-width:980px) 46vw, 210px"`.
2. The hero trust ribbon becomes a 2×2 grid below 900px.
3. Portrait masters placed in the 16:9 box use `.sec-img.fit-contain{object-fit:contain;background:#f6efe8;border:1px solid var(--bd)}` with real width and height attributes — **never let a cover crop cut a portrait infographic**, as happened to the red-tail image at every breakpoint.
4. Dial index numerals on dark green need **`#9fc7b0`**; the old `#6f9c86` failed AA, and Lighthouse flagged all 14.
5. The hero gains a `-560.webp` sibling in both srcset and preload, since the desktop display size is around 514px.
6. `public/cag-fs-seam-emblem.webp` was recompressed from 194×64 at 8.5 KB to **182×60 at 5.3 KB**, using q60 and alpha_quality 60.

**Gates.** `final_page_audit.py --for-sale` returned **PASS-WITH-WARNINGS**, with zero header crossover after the rewrite. Preview-verified: Dial 2, the Avail-B filter counts, and the hero all render, and the console is clean.

---

### ▸ Page 3 — Timneh African Grey

`/timneh-african-grey-for-sale/` · Live **2026-07-22** · page-scoped `.timneh` · **18 sections**

| Field | Value |
|---|---|
| **Inventory** | Elad ♂ **$1,600** · Evie ♀ **$1,500** · variant `timneh_african_grey` · parents **Levi × Rily** |
| **Schema** | AggregateOffer 1500–1600, plus per-bird ItemList Offers and FAQPage |
| **Tuple** | Split-Hero B warm gradient with the head-scratch OG hero · **Dial 1 Clay Progress + Rail B green ticker** · **T1 Numbered Ledger** · **K2 Price-Tag + K5 Capsule** · Table A + **Table B clay-spine** for the Congo-vs teaser · **FAQ-B two-column** · Avail-C v2 clean cards |
| **Framework** | **First use of EEBP — Entity → Evidence → Benefit → Purpose** |
| **Strategy** | A Trust-First blend, with the moat being **US-only, CITES-honest shipping** |

**Competitive intel.** The page-one rival **africangraysales** advertises illegal *"24-hour international shipping to Canada and Australia."* **Silvergatebirdfarm**, at position five, is a **confirmed cloaker** — it redirects to recaptcha.cloud. Our own page was buried at **GSC position ~97**, while the comparison page (congo-vs-timneh) carries the Timneh interest at **Bing 6.7**. The decision: keep "Congo vs Timneh" as a teaser that links here, and **do not cannibalise**.

**Images.** The hero is the real head-scratch shot `handfed-…-elad.jpg`, chosen by the breeder. Nine AI infographics cover identification, real-versus-fake, CITES Appendix I, what's included, PBFD, and the Elad and Evie personality cards, plus regenerated price, verify, and care graphics. The source folder is `assets/1WORKING-ON/FOR-SALE-PAGES/TIMNEHS-FOR-SALE`. The customer photo and the handheld-Evie shot both contain a sun conure, so they were cropped and captioned honestly as *"socialized with family's conure."* **The breeder dislikes HTML infographics — always use AI images.**

**🔴 The lesson that created the rule.** The prose was first mirrored from Congo, producing **30 duplicate passages** and a heavy rework. That failure produced the **Write-From-Outline, Never-From-Sibling** rule, which now sits at #1 in `CLAUDE.md`, lives in memory, and is injected into all 68 agents.

---

### ▸ Page 4 — Hand-Raised

`/hand-raised-african-grey-parrot-for-sale/` · Live **2026-07-22** · page-scoped `.handraised` · **18 sections**
Spine: Trust-First / welfare-authority · Engine: **EEBP**

| Field | Value |
|---|---|
| **Type** | **The method page — it spans both subspecies.** Unlike the Congo-only and Timneh-only siblings, it lists every available bird: the filter is `status==available`, which returns Bery, Amie, and Roys (Congo, $1,700 / $2,500 / $2,300), the Jins & Jeni pair ($3,500), and Elad and Evie (Timneh, $1,600 / $1,500) |
| **Schema** | AggregateOffer 1500–3500, offerCount 6 |
| **Angle and moat** | Hand-raised describes the **raising method** — co-parented and then hand-fed, weaned at 12–16 weeks, socialised across the household, and never pulled early. It is the moat competitors treat as a buzzword. |
| **Tuple** | **Hero-A Scattered Flock**, five OG Polaroids anchored by the Mark head-scratch shot · **Dial 2 Dark-Aviary + Rail B green ticker**, a previously unused pairing · **T4 Magazine Index Card** · **K3 Green Ledger + K2 Price-Tag** · **Avail-B filtered by subspecies** · **Table C outlined matrix with a top-pick badge** (hand-fed vs hand-raised vs parent-raised), plus a weaning `otA` GEO table · **FAQ-C refreshed forest-green** due-diligence checklist · small footer-logo seam |
| **Reviews** | **Stanley Perkin** (Oceanside, CA) and **Jesse Ovalle** (Baton Rouge, LA), both five-star with photos — page-specific, and distinct from the cluster-shared Woodard and Obrien reviews |
| **Geo set** | FL · MI · NC · NJ · MN · IN · MD · WI |
| **Metrics** | 7 external links across 6 domains — APHIS, CITES, AAV, parrots.org, Lafeber, NCBI ×2 · **13 CTAs** · 141 first-person tokens · 0 AI tells · no visible dates · 48 images, none broken · clean console |

**🔴 Schema-slot lesson — it cost a FAIL, and it is reusable.** `BaseLayout.astro` has **no named `head` slot**, so a `<Fragment slot="head">` is **silently dropped**: the schemas vanish, FAQPage drops to zero, and `has_org` fails. Inject JSON-LD through the **`schemaJson` prop** instead, combining multiple schemas into a single `{"@context","@graph":[…]}` string, and use the `ogType`, `heroPreload`, and `extraHeadHtml` props for head meta and preloads.

**Images.** Thirteen AI infographics plus real OG photography — five hero Polaroids, the baby hand-fed shot, air and home shipping images, the Roys video, and two review photos — output to `public/images/hand-raised-page/` as uniform 1408×768 WebP files under 95 KB with `-760` siblings. Mid-build, the breeder added a real **spoon-feeding baby grey** photo, which became the §howraise lead. Bird cards reuse the Congo-page and Timneh-page card WebPs, and the home-shipping portrait was blur-filled to 16:9.

**Three infographics were flagged in QA.** The breeder is swapping them at final review, and since the filenames are unchanged they drop straight in: `verify-hand-raised-breeder-60-seconds`, whose title reads "BREDDER" instead of "BREEDER"; `what-comes-home-hand-raised-grey`, carrying a duplicated "HOME HOME" and a stray card stack; and `hand-raised-grey-health-pcr-screening`, where "Polyomavirus" is set too tight. Corrected regeneration prompts are in `sessions/2026-07-22-hand-raised-image-prompts.md §REGEN`. **Always read and verify the text on an AI infographic — the flat-design ones carry baked-in type.**

**The health guarantee was kept honest** — the real three-day term from the price matrix, **not** the kit's stale "three-year" claim, and no guarantee duration is baked into any image.

#### ⚙️ The Hardening Pass — 2026-07-23 (`15ff200`, `8e47f74`, `c105163`)

The breeder's verdict was **"feels rushed."** There were five root causes, and **none was visible in a source review**:

| # | Defect | Root cause | Fix |
|---|---|---|---|
| 1 | Hero rendered at 524px | **Invalid clamp math** — `clamp()` and `calc()` need spaces around `+` and `−`, or the declaration is silently dropped | Hero corrected from 524px to **382px** |
| 2 | Polaroids covered each other's heads on desktop and collapsed to slivers on mobile | The absolute positioning was never unwound | Replaced with a rotated **2×2 grid of four** face-forward Polaroids, making overlap structurally impossible. The breeder liked the concept, so it stays. |
| 3 | Mobile jump-rail "not working" | It was rendering **underneath** the global `MobileTabBar` — `z-40` against the bar's `fixed bottom-0 z-50`. Not broken, just buried. The breeder then rejected the bottom placement outright. | **Final: sticky at the top** — `position:sticky; top:var(--hdr); z-index:40`, on a cream bar, `rgba(250,247,244,.985)`. **Standing rule: for-sale jump-rails go top, never bottom.** |
| 4 | Infographics cover-cropped on mobile | A 5:4 `object-fit:cover` box shaved roughly 30% off each side, cutting the baked-in text | Infographics keep native 16:9 with `object-fit:contain`; the taller 5:4 mobile frame is for `.og-photo` **only** |
| 5 | Body text pushed off-screen | **100vw full-bleed images inflated the mobile grid track** — 366px inside a 343px box. `overflow-x:clip` **hides** the symptom, so `scrollWidth` reads fine while the text is clipped. | `minmax(0,1fr)` plus `min-width:0` |

**Dial contrast comes in two variants — never mix them.** The light card, used on Congo and Timneh, takes `#6b625a`; the **dark-aviary card on this page takes `#9fc7b0`, measuring 5.00:1.** Applying the light fix to the dark dial makes it unreadable. The rail `.p` colour is `#c9f2db`, with **no opacity dimming**.

**New standing tooling was born here:** `skills/cag-page-hardening` and `scripts/page_hardening_scan.py`. It immediately found **four more live comparison pages** carrying the same infographic-crop bug — the comparison hub, breeders-comparison, pros-and-cons, and vs-macaw — all fixed in the same pass. **Static analysis cannot find the overflow, contrast, and sizing defects; the skill carries runtime browser probes for those, and both halves are required.**

**Also fixed:** `final_page_audit.py` no longer falsely fails multi-image heroes — 2×2 grids and Polaroid scatters — on `img_lazy_nonhero`, since it had treated only `imgs[0]` as the hero. The Timneh meta description came down from 320 to 291 characters. The cluster verdict: **four PASS-WITH-WARNINGS, zero FAIL.**

**Microformats.** The *"does not utilize Microformat markup"* auditor flag is **cosmetic** — Google and Bing already consume the shipped JSON-LD. A zero-visual-change mf2 layer was added anyway: six `h-product`, two `h-review`, and three `h-card`.

**Follow-up polish pass (`c105163`) — three further breeder catches, all reusable across the cluster:**

1. **Hero photos must lead on mobile.** `.hero-scatter{order:-1}` inside the ≤980px block, matching the siblings' `.chero-media{order:-1}`. Desktop keeps copy-left, photos-right. **Standing rule: for-sale heroes put images first on mobile and copy first on desktop.**
2. **The bird-card category pill needs a per-bird escape hatch.** The default is bottom-left, because top-left lands on most birds' heads. **Roys is photographed head-down, eating**, so the default covered his face. A `badge?:"top"` flag was added to the `birdImg` map, driving `.bbadge.badge-top{top:8px;bottom:auto}` on both desktop and mobile. **Check each new card photo's subject position before assuming one badge corner suits every bird.**
3. **Mobile table stacking** — the full recipe is banked in `reference_mobile_table_stacking`.

**Still open, pending breeder action or backlog work.** Cloudflare **Rocket Loader** `/70de/` unused JS and the missing source map are a dashboard toggle under Speed → Optimization, not fixable in code. The site-wide `img-no-srcset` backlog stands at **187 warnings**.

---

### ▸ Page 5 — Health Guarantee

`/african-greys-for-sale-with-health-guarantee/` · Live **2026-07-25** · commit `8c48bb2`
*This is the page the brief in Part I targets.*

| Field | Value |
|---|---|
| **Angle** | **"A Guarantee You Can Actually Use."** It reframes the guarantee-length arms race — an **enforceable 72-hour, vet-anchored** window beats an unenforceable "one year" — publishes the terms nobody else publishes, bundles the documentation, and then sells the birds that carry it. |
| **Why this angle** | The page was **already at GSC position 11** on trust signals, so the job was **to consolidate and climb, not to create demand**. That is why the transactional layer sits higher here than on the DNA page. |
| **Frameworks** | **EEBP × PAS × EEAT × QAB × FAB** |
| **Voice lever** | **Enforceable versus unenforceable** — *window, covered conditions, remedy, void, in writing, as-is* |
| **H6 prefixes (reserved to this page)** | **"In Writing:"** · **"From the Vet:"** · **"On File:"** |
| **Tuple** | **Split-Hero A trust ribbon** — its first use in the cluster, with ribbon chips reading 72-hour guarantee, avian vet, DNA-sexed, and CITES; the hero `healthy-african-grey-for-sale.webp` is **cover-cropped, not blur-filled** · **Dial 1 Clay + Rail A** in the guarantee palette, with light-card numerals at `#6b625a` · **T4 "Guarantee Index"**, regrouped into The Terms, The Proof, The Caution, and The Birds · **K1 Receipt**, a green header band with dt/dd ledger rows, **and K5 Capsule** after §documents · **new Table E "Guarantee Ledger"**, a green caption band with a green spine on the "ours" column, plus Table A · **FAQ-A refreshed to a green check-circle**, where DNA uses the numbered clay chip and chevron · **Avail-B faceted by availability posture** — Ready Now (1), Reserve & Wean (4), Bonded Pair (1) |
| **Geo** | TX · OH · CO · NC · GA · MI · PA · VA |
| **Reviews** | **Meredith Plaisance** (Hartsville, SC) and **Jeffrey Hendershot** (Centennial, CO) — both on-query for live GSC terms |
| **Build metrics** | **7 seams · 15 `#reserve` CTAs** · all prose written fresh from the outline |

**Ledger facts — do not exceed these:**

- A **72-hour** written health window, plus a **24-hour** shipping-arrival window
- The remedy is **replacement or refund at our discretion**
- Coverage extends to **congenital defects and infectious disease**
- The guarantee is voided by **band removal, improper diet, exposure to other birds, or no vet exam within the window**
- ⚠️ The terms are **described in full on the page. Never depict a guarantee document, seal, or signature.**

**Shipped alongside:** regenerated sitemaps at **109 URLs with zero phantoms**, plus the component-map ledger and build lessons (`8c48bb2`).

---

### ▸ Page 6 — DNA-Tested

`/dna-tested-african-grey-for-sale/` · Live **2026-07-24** · commit `38f8437`
**18 sections · 70 headings · ≈3,860 body words**

| Field | Value |
|---|---|
| **Angle** | **"Proof, Not Guesswork"** — myth-bust, then method, then certificate, then bird |
| **Why** | The head term has **no GSC demand**, and **Bing resolves "DNA" to the molecule**. The real traffic sits in the **sexing cluster**, at roughly 103 impressions at position ~43. The blueprint accepted the trade-off deliberately: the informational myth-bust — *you cannot sex a grey by eye* — earns the entry, and the certificate and the birds convert it. |
| **Tuple** | **Hero-C Mosaic Metrics** — a stat strip above the headline with a 2×2 mosaic whose anchor cell is the real Jins & Jeni pair · **Dial 1 clay-on-cream + Rail A clay pills** · **T2 Chip Cloud** · **K4 Clipboard + K5 Capsule** · **new Table D "Lab Report"** plus Table A · **FAQ-A refreshed** with a numbered clay chip and chevron, rather than the plus/cross · **Avail-B faceted by confirmed sex**, where the siblings facet by subspecies |
| **Dup-gate defence** | The **hen/cock voice register** — the siblings say male and female — plus the H6 prefixes **"From the Lab:"** and **"On the Record:"**, where the siblings own "Citation:" and "Breeder Note:". The shipping line and Midland-pickup line were reworded to dodge the 12-word shingle. |
| **Reviews** | Stanley Perkin and Jesse Ovalle, reused from Hand-Raised — the only whitelisted verbatim crossover |

**Ledger-bound facts, which corrected two false claims carried by the live stub:**

- The lab is **Avian Biotech, now part of Animal Genetics** (avian2.animalgenetics.com)
- **Both** feather and blood samples are accepted; blood is taken from the toenail tip
- Accuracy is **~99%** — **not** the stub's "99.9%"
- The certificate is **priced at $40–60, not free** — the stub's "at no additional charge" was removed
- Turnaround is one to two business days
- The certificate **photo is still unavailable (gap G1)**, so an empty schematic diagram and Table D stand in, with the §8 slot reserved for the real photo

**Reusable fixes made during this build:**

- `scripts/page_hardening_scan.py` gained a `SPECIES_GENERA` binomial exemption, so *Psittacus erithacus* — with its lowercase specific epithet — no longer false-flags as `header-not-title-case`. It belongs to the same class as acronyms.
- `scripts/final_page_audit.py` had the slug added to its `FORSALE` list, which had covered only four pages.
- The Hero-C desktop mosaic ran **617px** tall, overshooting the 350–400px cluster band; `max-width:430px` with an anchor tile at `aspect-ratio:16/9` on desktop and `4/3` on mobile brought it down to **~412px**.
- Ticket-CTA pills were orphan-wrapping on mobile, fixed with `justify-content:center; text-wrap:balance` and shorter labels.

---

## II·C — Component Uniqueness Ledger

**The rule: no two sibling pages ship the same combination.** Record each tuple before the build, so the duplication and refresh checks can verify uniqueness.

| Slot | Eggs | Congo | Timneh | Hand-Raised | Health Guarantee | DNA-Tested |
|---|---|---|---|---|---|---|
| **Hero** | Split-Hero C dark | Split-Hero B warm | Split-Hero B warm (head-scratch OG) | **Hero-A Scattered Flock** | **Split-Hero A trust ribbon** | **Hero-C Mosaic Metrics** |
| **Dial** | Dial 1 clay | **Dial 2 Dark-Aviary** | Dial 1 clay | **Dial 2 Dark-Aviary** | Dial 1 clay | Dial 1 clay-on-cream |
| **Rail** | Rail A | Rail A | **Rail B green ticker** | **Rail B green ticker** | Rail A | Rail A clay pills |
| **TOC** | Dial 1 **is** the TOC (fs:02 folded in) | **T5 Reserve-Path stepper** | **T1 Numbered Ledger** | **T4 Magazine Index Card** | **T4 "Guarantee Index"** | **T2 Chip Cloud** |
| **Takeaway** | K4 + K1 | K1 + K4 + K3 | **K2 + K5** | **K3 + K2** | **K1 + K5** | **K4 + K5** |
| **Table** | Table A | Table A | Table A + **Table B clay-spine** | **Table C outlined matrix** + `otA` | **new Table E Guarantee Ledger** + A | **new Table D Lab Report** + A |
| **FAQ** | **FAQ-C dark badge** | **FAQ-A light bordered** | **FAQ-B two-column** | **FAQ-C forest-green checklist** | **FAQ-A green check-circle** | **FAQ-A numbered clay chip + chevron** |
| **Avail facet** | — | Avail-C v2 | Avail-C v2 | **Avail-B by subspecies** | **Avail-B by availability posture** | **Avail-B by confirmed sex** |
| **Voice lever** | Scam-exception | Anti-scam trust | US-only CITES honesty | Raising method | **Enforceable vs unenforceable** | **Hen/cock** |
| **H6 prefixes** | — | — | — | — | In Writing / From the Vet / On File | From the Lab / On the Record |

**Pages 7–9** *(continued — the table above stops at six columns for width)*

| Slot | Baby | Adoption Cost | **Congo Pair — TARGET, to be filled at Sprint 1** |
|---|---|---|---|
| **Hero** | Split-Hero B refreshed | Price-ladder hero | `[AI RECOMMENDS: Hero-A refreshed "Bonded Duo", two tiles]` |
| **TOC** | — *(recorded in the component-map ledger)* | — | `[ ___ ]` |
| **Table** | — | **new Table G** | `[ ___ ]` — must be a new letter or an unused existing one |
| **Avail facet** | **Avail-B by age band** | — | `[AI RECOMMENDS: Avail-B faceted by pairing route — ready-made pair / build-your-own / breeding pair / single]` |
| **Voice lever** | Weaned-first | Number→Ledger→Thesis | `[AI RECOMMENDS: two-versus-one — bonded, compatible, introduced, quarantined, solo]` |
| **Special** | PDB + BAB, first use | `.ctool` first-year calculator | `[ ___ ]` |

> **Fill this column before writing a line of the page.** The tuple ledger at `sessions/2026-07-19-for-sale-component-map.md` is the binding record; this table is its summary.

### Hero → Cluster Assignment (locked 2026-07-19)

| Cluster | Default hero | Notes |
|---|---|---|
| Money variants: congo · timneh · baby · hand-raised | **Split-Hero B, full-bleed warm gradient** | Clutch eyebrow with a price-anchored CTA |
| Trust pages: dna-tested · health-guarantee · eggs (hybrid) · adoption-cost | **Split-Hero C, dark with photo grid** | Authority register |
| Hub and near-me: parrots-for-sale (hub) · parrot-for-sale · near-me ×2 · grey-african | **Hero-C Mosaic Metrics** | Stats strip with inventory mosaic |
| Pair and family: pair-for-sale · breeding-pair · affordable · male-african-gray | **Hero-A Scattered Flock Polaroids** | Shows multiple birds |
| The five buy-prefixed pages | **Split-Hero A, image left with trust ribbon** | Scam-anxiety reassurance strip |

**Dial and rail defaults.** Dial 1 Clay Progress is the desktop default. **Dial 2 Dark Aviary is only for pages with light heroes** — never stack it under the dark Split-Hero C. Rail A price-chip is the mobile default; Rail B green ticker rotates onto hub and near-me pages, where the fact-per-stop ticker earns its extra height.

**TOC rotation** (`cag-toc-fs:01–05`): fs:01 T1 · fs:02 T4 for trust pages · fs:03 T5 for pages whose sections follow the buy sequence · fs:04 T2 · **fs:05 T3 Boarding-Pass for shipping-heavy pages only — never health-guarantee.**

**Takeaway rotation** (`cag-key-takeaway-fs:01–05`): fs:01 K1 for money pages · fs:02 K3 for light-hero pages · fs:03 K4 for proof pages · fs:04 K2 · fs:05 K5 for compact pages or a second takeaway slot.

**All takeaway numbers are ledger-verified:** a $1,500 floor · $185/$350 shipping · PBFD and APV PCR · CITES Appendix I · a 24-hour reply · 12–16 weeks to weaning · Midland pickup within a two-to-three-hour radius.

**Tables.** Table A takes a maximum of six columns on desktop; use Table B where a table has three rows or fewer, or sits in a narrow column. The species markers `/emoji/cag-congo-64.webp`, `cag-timneh-64.webp`, `macaw-64.webp`, `cockatoo-64.webp`, and `amazon-64.webp` all exist in `public/emoji/`.

---

## II·D — Locked Cluster-Wide Specs

### Hero

- **350–400px on desktop** — `.hero-grid{min-height:350px;max-height:420px}` with tight padding, an H1 clamp of ≤1.95rem, and a lead at .88rem.
- The eyebrow reads `Est. 2014 · Midland, TX · USDA-licensed` — **sentence case, with no uppercase transform**, kept small as on the homepage.
- **Images come first on mobile** — `.hero-scatter{order:-1}` below 980px, matching the siblings' `.chero-media{order:-1}`. Desktop stays copy-left, photos-right.
- In a 2×2 hero grid, each image takes its own `object-position` from the data array, and **all four carry `loading="eager"` and `fetchpriority="high"`** — otherwise PageSpeed Insights picks a lazy grid image as the LCP element.
- The hero ships a `-560.webp` sibling in both srcset and preload.
- **Bake heroes with a plain `PIL.ImageOps.fit` cover crop — never blur-fill.**

### Desktop Dial TOC — Byte-for-Byte Canonical
*(`skills/cag-for-sale-page-builder.md` §6a / §1e-bis)*

| Spec | Value |
|---|---|
| Body grid | `196px minmax(0,1fr); gap:28px` — previously 222px with a 30px gap |
| Card | Plain `#fff` with no gradient, radius 16, padding 12px 10px, a light shadow, sticky at `top:hdr+16`, with `overflow-y:auto; scrollbar-width:thin` |
| Ring / inner | **64px / 50px**, a serif 15px number, and a 7px "of N" |
| Rows | 18 rows · font **11.84px** · padding **5px 7px** · line-height **14.8px** · radius 8 |
| Numerals | Muted `#b8a294` tabular figures, turning clay when active · **light dial `#6b625a`** · **dark-aviary dial `#9fc7b0`** |
| Tag chips | .56rem, with 0.15s transitions |
| Counter cards | Min-height 66, padding 10px 13px, radius 12, serif number at 1.35rem |
| Verified | No row falls below the **24px WCAG tap-target floor**; contrast measures **7.27** (label), **5.00** (numeral), and **4.77** (tag) |

**Only the palette changes from one page tuple to the next.** Never ship the big-ring 92px gradient variant — it read as oversized and busy beside the content column.

### Mobile Jump-Rail

- **Sticky at the top** — `position:sticky; top:var(--hdr); z-index:40`. **Never at the bottom.**
- Verified: the rail sticks at exactly **96px**, stands **62px** tall, and tapping a chip lands the target H2 **18px below the rail**, clearing both bars.
- The bar is cream, `rgba(250,247,244,.985)`, so it does not merge into the green header.
- The rail `.p` colour is `#c9f2db`, with **no opacity dimming on text**.

### Images

- The uniform in-body box is `.sec-img.inf-img`: **max-width 760px, aspect-ratio 1408/768 (16:9), object-fit cover, height auto** — identical on mobile, tablet, and desktop.
- **Infographics keep native 16:9 with `object-fit:contain` on mobile.** The taller **5:4** mobile frame is for `.og-photo` only.
- Do **not** full-bleed infographics. The `100vw` trick was reverted, because it inflated the mobile grid track and pushed body text off-screen.
- Portrait masters take `.sec-img.fit-contain{object-fit:contain;background:#f6efe8;border:1px solid var(--bd)}` with real width and height attributes.
- The pipeline is `PIL.ImageOps.fit(src,(1408,768),LANCZOS,centering=per-image)` → WebP at `method=6`, with a quality-walk from 82 downward until the file is **under 95 KB** → then a `-760.webp` sibling with `srcset` and `sizes`.
- Card images ship `-440.webp` siblings with `sizes="(max-width:980px) 46vw, 210px"`.
- Video posters use a `-760.webp` poster sibling, **never** the 1280px master.

### Cards, Seams, and Counters

- The **bird-card badge** defaults to bottom-left, with a per-bird `badge?:"top"` escape hatch driving `.bbadge.badge-top{top:8px;bottom:auto}`. It is a small transparent pill, `rgba(255,255,255,.82)`, carrying dark species-coloured text — not a bulky solid. The photo is `height:210px; object-position:center 28%`, becoming 230px at 22% on mobile.
- Every card carries a one-line blurb from the `birdBlurb` map — the inventory holds no descriptions — plus three trust chips.
- **The seam budget is 4–8 per page**, placed at movement boundaries — **not one per section**, which reached 17. Use the small footer-logo image only, with no "Midland, TX" `.seam-tag` text. The emblem is 182×60 at q60, roughly 5.3 KB.
- **Counter CLS fix:** counter cards need `min-height:74px` and **fixed column counts** — 7/4/2 by breakpoint — rather than `auto-fit`. Font swap and reflow accounted for the entire 0.100 CLS.
- The shipping section uses the `.geo-cards` route-card component — a pin icon, keyword, note, and arrow — **not** comparison-style pills. Every anchor label must **end** with the state or city, and link to a live `/african-grey-parrot-for-sale-<state|city>/` page.
- "Every grey leaves with" renders as a `.doc-stack` numbered-badge list, not the green-header band card.

### Contrast Quick Reference

| Context | Value |
|---|---|
| Small clay text on light | `#b04228` |
| Clay on a tinted background (`#faece7` / `#fbe4dd`) | `#9c3a23` |
| Solid clay button fill | `--clay-ink #c8472f` |
| Light dial numerals | `#6b625a` |
| Dark-aviary dial numerals | `#9fc7b0` (5.00:1) |
| Rail paragraph on green | `#c9f2db` |
| Clay on dark | `#f08070` |
| Never | Use `opacity` to create hierarchy |

---

## II·E — Trap and Failure Log

Every one of these cost real rework, and every one applies to the 16 remaining for-sale pages.

| # | Trap | What happened | Standing fix |
|---|---|---|---|
| 1 | **Mirroring a sibling's prose** | Timneh mirrored Congo, producing **30 duplicate passages**. Congo mirrored Eggs, producing **~12 verbatim runs and an H3 crossover**. | **Write-From-Outline, Never-From-Sibling** — now `CLAUDE.md` rule #1, injected into all 68 agents |
| 2 | **Wrong image taxonomy** | Egg v1 treated AI `.webp` files as OG photos and never used the real `.jpg` aviary shots, forcing a full v2 rebuild | **Read every dropped image and sort by extension before building** |
| 3 | **Wrong component kit** | Egg v2 used homepage and comparison components; the breeder rejected it, forcing a v3 rebuild | The for-sale cluster has **its own kit**. Never reuse the homepage or comparison hero, counter, NewsletterV2, FAQ, or seam. |
| 4 | **Missing schema slot** | `<Fragment slot="head">` was silently dropped, taking FAQPage to zero and failing `has_org` | Inject through the **`schemaJson` prop** as a single `@graph` |
| 5 | **Blur-fill on a hero** | `reframe_og.py --style blurfill` sizes the foreground to about 614px inside a 1408px canvas, so the hero showed a small photo floating in a blurred field | Blur-fill is for `.sec-img.og-photo` **only**. Heroes take a plain `ImageOps.fit` cover crop. |
| 6 | **Outline-only dup-gate** | Three headings cleared the Sprint 1 gate and still collided **exactly** with the DNA page | Run `dup_content_audit.py --headers` against the **built `dist/` page**, not the proposed outline. Grep your own slug — `/dist/` in the labels means the homepage. |
| 7 | **Lower-casing "If"** | "If" is not in the mid-title lowercase list, so it **is** capitalised in AP Title Case | `page_hardening_scan.py` catches it; the blueprint did not |
| 8 | **Seam spam** | One seam per section reached **17** | Budget **4–8**, placed at movement boundaries |
| 9 | **Invalid clamp math** | `clamp()` or `calc()` without spaces around `+` and `−` silently drops the declaration, which left the hero at 524px | Always space the operators |
| 10 | **Rail buried under MobileTabBar** | `z-40` sat under a `fixed bottom-0 z-50` bar — it was rendering, not broken | **Rails go top, never bottom** |
| 11 | **Infographic cover-crop** | A 5:4 `object-fit:cover` shaved roughly 30% off each side, cutting the baked-in text — and the same bug was found on four live comparison pages | Infographics use 16:9 with `contain` |
| 12 | **100vw overflow masked by `overflow-x:clip`** | `scrollWidth` reads fine while the text is clipped off-screen | `minmax(0,1fr)` plus `min-width:0`; probe at a real 375px viewport |
| 13 | **Badge over the bird's face** | Roys is photographed head-down, eating, so the default bottom-left badge covered him | Per-bird `badge:"top"` flag |
| 14 | **Portrait cover-cropped** | The red-tail infographic was cut off at every breakpoint | `.sec-img.fit-contain` with real width and height |
| 15 | **Dial contrast cross-application** | Applying the light-dial fix `#6b625a` to the dark dial makes it unreadable | Two variants — never mix them |
| 16 | **AI infographic text errors** | "BREDDER", a duplicated "HOME HOME", and a tight "Polyomavirus" | **Read and verify the text on every AI infographic** before shipping |
| 17 | **Auditor silently skips the page** | `FORSALE` inside `final_page_audit.py` is a **hardcoded roster** | Append every new slug |
| 18 | **Two real auditor bugs** | The `for-sale` profile had no wordcount branch, so it fell through to the lean 600–1,200 *interior* band; and the word count stripped `<script>` but not `<style>`, counting thousands of words of page CSS as body copy | Both fixed on 2026-07-25 — the band is now **3,000–8,000** |
| 19 | **Stale kit facts** | Kit copy ships Appendix II, the fictional birds Bella, Oliver, Rosie, and Max, a fake 4.97 rating from 184 reviews, Zelle and Cash App, and 🦜 | **Intake reconciliation is mandatory:** Appendix **I**, real birds and pairs, the real **4.9 from 52**, neutral payment wording, and `/emoji/cag-congo.png` |
| 20 | **Counter CLS** | `auto-fit` columns combined with a font swap produced 0.100 CLS | `min-height:74px` with fixed column counts |

---

## II·F — Tooling and Gate Order

Run these in order on every page **before** calling it done. **Read `skills/cag-gate-integrity.md` before you act on any output below — including a PASS.**

```bash
git checkout main && npx astro build
```
```bash
python3 scripts/page_hardening_scan.py <slug>
```
```bash
python3 scripts/seam_parity.py <slug>
```
```bash
python3 scripts/aeo_audit.py <slug>
```
```bash
python3 scripts/dup_content_audit.py
```
```bash
python3 scripts/dup_content_audit.py --headers
```
```bash
python3 scripts/final_page_audit.py --for-sale
```
```bash
python3 scripts/generate_sitemaps.py
```

| Script | What it catches |
|---|---|
| `page_hardening_scan.py` | `header-not-title-case`, `img-no-srcset`, `opacity-dims-text-contrast`, `clay-small-text-contrast`, `absolute-hero-not-unwound`, and `smooth-scroll-breaks-anchors`. It carries a `SPECIES_GENERA` binomial exemption so *Psittacus erithacus* does not false-flag. **This is the static half only — pair it with runtime browser probes.** |
| `dup_content_audit.py` | Word-for-word body runs of 12 words or longer |
| `dup_content_audit.py --headers` | Exact **and** species-templated H1–H6 crossovers |
| `final_page_audit.py --for-sale` | Runs the page-type profile and returns PASS, PASS-WITH-WARNINGS, or FAIL. The word band is **3,000–8,000**, and the `FORSALE` roster is hardcoded, so new slugs must be appended. |
| `generate_sitemaps.py` | Regenerates the shards from `src/pages/` and validates that there are zero phantom URLs |
| `reframe_og.py --style blurfill --mobcrop 4:5` | In-body OG photos **only** — never heroes |
| `seam_parity.py` *(added 2026-07-29)* | One seam per section, one seamless hero allowed. **Never re-derive this with grep** — the published grep matched a class only 2 of the 8 built pages use, so it compared seams against **zero sections**, and a `\bseam\b` regex double-counts because `-` is a word boundary. The script prints its own examined count and refuses to call a 0-page run a pass |
| `aeo_audit.py` | The machine half of `cag-aeo-pass`: BLUF proxy, entity counts, pronoun density, labeled-method presence, `dateModified` in JSON-LD, **visible-date detection (ERROR)**, tables / lists / stat-header counts, sentence-length report |
| `verify_model_tiers.sh` | All 68 agents on Opus 5. Runs are idempotent since the 2026-07-29 drift fix |

**Always read the built `dist/` output, never a source grep.** And **read every gate's own examined count before believing a PASS** — zsh does not word-split `$VAR`, so `PASS … in 0 pages` has happened twice on this site. Pass slugs literally, or use `${=SL}`.

---

## II·G — Verified Pass Thresholds

This is the bar every page in the cluster has cleared.

| Check | Result |
|---|---|
| Contrast sweep | **0 failures across 443 elements** |
| Horizontal overflow at 375px | **None** |
| Body links underlined | **10 of 10** |
| Dup gate (body + headers) | **0 crossovers** |
| Body-anchor collisions site-wide | **0** — anchors already rotate LSI and long-tail variants |
| Primary keyword density | **1.78%** against a 1–2% target |
| First-person tokens | **111–174** per page |
| AI tell-phrases | **0** |
| Card heights and CTAs | Uniform, with buttons hugging their labels at **124–145px**, down from 200px stretched |
| Dial rows below the 24px tap target | **0** |
| Cluster audit verdicts | **PASS-WITH-WARNINGS across the board, zero FAIL** |
| Lighthouse (Eggs, localhost) | Accessibility **100** · Best Practices **100** · SEO **100** · CLS **0** · TBT **0** |

**Benign warnings seen cluster-wide** — these show parity across siblings rather than defects: `no_aggregateoffer`, `wordcount_in_band`, `house_method`, and `lifespan_40_60`.

---

## II·H — Open Flags Carried Forward

| # | Flag | Owner |
|---|---|---|
| 1 | Exact refund-versus-replacement wording (Egg page) | Breeder |
| 2 | Carrier and transit window | Breeder |
| 3 | Eggs-per-season count | Breeder |
| 4 | The verify-in-60-seconds infographic shows an illustrative fake licence, "AWA-12556-9021" | Review |
| 5 | Breeder swaps the three regenerated Hand-Raised infographics at final review — filenames unchanged, so they drop straight in | Breeder |
| 6 | The DNA certificate photo is unavailable (gap G1); the §8 slot is reserved | Breeder |
| 7 | The Egg page as a truth-forward hybrid is recommended but not yet explicitly confirmed | Breeder |
| 8 | No page-level sidebar is recommended but not yet explicitly confirmed | Breeder |
| 9 | The Bing Webmaster → Queries export is still missing; the supplied CSV was a date-series chart | Breeder |
| 10 | `@cag-llm-keyword-intel` has never been run on any cluster page, so **LLM visibility is unmeasured** | Build |
| 11 | Cloudflare Rocket Loader `/70de/` unused JS — a dashboard toggle under Speed → Optimization | Breeder |
| 12 | The site-wide `img-no-srcset` backlog stands at **187 warnings** | Backlog |
| 13 | **1,099 headings across 68 pages remain in sentence case** — heaviest on the six `/available/` bird pages at roughly 86 each, the hub at 54, and the homepage at 31 | Backlog |

---

## II·I — What Remains

**Fourteen of the 22 pages are unbuilt** — 9 for-sale and 5 buy-prefixed. Verified on disk 2026-07-30.

Every remaining page inherits the locked specs in [II·D](#iid--locked-cluster-wide-specs), the trap log in [II·E](#iie--trap-and-failure-log), and the gate order in [II·F](#iif--tooling-and-gate-order) — and each must record a **fully distinct tuple** in `sessions/2026-07-19-for-sale-component-map.md` before the build begins.

**Fast wins flagged by keyword mining:** breeding-pair queries already rank at **positions 5–9** — the strongest starting position of any page in the cluster, and the reason the pair page opens Cluster 3. For comparison, all 74 egg queries sat between positions 60 and 92 before the rebuild.

---

## II·J — Tooling and Rules Upgrade, Shipped 2026-07-29

That session's scope was tooling, not page fixes. Everything below is **done and live**, and every page from Page 9 onward is built on top of it.

| Task | Result |
|---|---|
| All agents moved to **Opus 5** | 68 of 68 · `verify_model_tiers` PASS=68 |
| `scripts/seam_parity.py` | Replaces a probe that compared seams against **0 sections on 6 of the 8 built pages** |
| **§1k `markup-css-drift`** | Finds the "clean scan, broken page" failure mode |
| **§1l colour specificity** | Finds the 1.19:1 mechanism — a component colour losing to a descendant |
| **`cag-page-hardening` v2.0** | Adds §1k, §1l, the Playwright mandate, and §5 small defects |
| **NEW `cag-gate-integrity`** | Registered and loadable. The highest-value item of the session — 12 checkers had cried wolf |
| **Header-style layer** | 3 styles + 3 registers + a routing table, injected into 68 of 68 agent Golden Rules |
| **Reddit thread protocol** | Plus `data/reddit-thread-ledger.json`, 6 threads seeded |
| **`WORKFLOW.md`** | Rewritten to the 7-sprint model; `interior_29_audit` routing retired |
| **NEW `cag-asset-proofing`** | Small skill; proves every dropped asset before the build |

**Still outstanding from that session, all logged in `docs/reference/technical-seo-fixes-backlog.md`:** GSC + GA4 MCP and a `cag-analytics-live` skill (needs the breeder's credentials), and the `CLAUDE.md` core/site split with the prompt-improvement rule.

### The Anchor Ledger Already Touches This Page

Three anchors are **already spent** against `/congo-african-grey-parrot-pair-for-sale/` by sibling pages, and none of them may be reused when those siblings link here or when this page links out:

> Congo African Grey pair page · Our Congo pair listing · The Congo pair listed separately · Two Congos sold together · A documented Congo pair · The larger Congo equivalent

Eight more are spent against `/african-grey-breeding-pair-for-sale/`, which this page must link to. Full tables in the lessons doc §6 and §9. **Script the collision check against the built page; two collisions were caught that way on adoption-cost, and eyeballing would have shipped both.**

---

<div align="center">

**C.A.Gs — Midland, TX** · Forest `#2D6A4F` · Clay `#e8604c` · Cream `#faf7f4` · Charcoal `#3a2f2a`

*Part I — the build brief. Part II — the cluster record, compiled 2026-07-25, retargeted to `/congo-african-grey-parrot-pair-for-sale/` and extended through Pages 7–9 plus the 2026-07-29 tooling upgrade on **2026-07-30**.*

</div>

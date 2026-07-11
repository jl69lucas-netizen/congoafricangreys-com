---
name: cag-comparison-page-builder
description: THE comparison-page builder skill for CongoAfricanGreys.com — 22–25-section blueprint, per-page research protocol (SERP snapshot → keyword universe → entity map → visual asset blueprint), 3-variant component system (Hero A/B/C), interactive decision modules, and the full pass-gate list (SEO/AIO/GEO/AEO/entity/anti-AI/non-commodity/Lighthouse). Converted from the MFS Maltipoo comparison system 2026-07-04; source files in assets/CAGs-BLOG-POSTS/. Covers the 8-page comparison cluster (hub + 7 spokes). Build order — congo-vs-timneh first, male-vs-female second-to-last, hub LAST.
---

# SKILL: CAG Comparison Page Builder (v1.0 — converted from MFS 2026-07-04)

**Source of truth inputs:**
- `assets/CAGs-BLOG-POSTS/CAGs-Comparison-Page-Builder.md` — original MFS system (converted here)
- `assets/CAGs-BLOG-POSTS/Research-Data-For-Comparison-Page-CAGs.md` — THE research standard, done for Congo vs Timneh; replicate its file set for every other page
- Binding alongside: `PRODUCT.md`, `DESIGN.md`, `IMAGE-DESIGNS.md`, `docs/reference/seo-rules.md`, `skills/cag-direction-d-theme.md`, `skills/anti-ai-writing.md`

This skill **supersedes the section template inside `.claude/agents/cag-comparison-builder.md`** — the agent now executes THIS blueprint. Same design system, same reference page idioms, deeper structure.

---

## 1. Page Inventory & Build Order (verified live 2026-07-04, all 200)

| # | Slug | Role | Build order |
|---|------|------|-------------|
| 1 | `/congo-vs-timneh-african-grey/` | Variant comparison (flagship) | **FIRST — the standard-setter** |
| 2 | `/african-grey-vs-cockatoo/` | Species comparison | 2nd–4th batch |
| 3 | `/african-grey-vs-macaw/` | Species comparison | 2nd–4th batch |
| 4 | `/african-grey-vs-amazon-parrot/` | Species comparison (THIN — 135 lines) | 2nd–4th batch |
| 5 | `/african-grey-pros-and-cons/` | Self-comparison / decision page | 5th–6th |
| 6 | `/african-grey-parrot-breeders-comparison/` | Breeder comparison (trust page) | 5th–6th |
| 7 | `/male-vs-female-african-grey-parrots-for-sale/` | Gender comparison (FOR-SALE method) | **SECOND-TO-LAST** |
| 8 | `/african-grey-comparison/` | HUB | **LAST — consumes spoke data** |

- `/blog/african-grey-vs-eclectus/` is a **blog post**, not part of this cluster — never merge it in.
- All 8 exist on disk in `src/pages/` — default mode is REBUILD to this standard, never build from scratch, never change slug/canonical/H1 topic without approval.

## 2. MFS → CAG Conversion Map (apply to ALL converted content)

| MFS term | CAG term |
|---|---|
| Maltipoo (baseline breed) | Congo African Grey (*Psittacus erithacus*) |
| Maltese | Timneh African Grey (*Psittacus timneh*) |
| Cavapoo | Cockatoo |
| Cockapoo | Macaw |
| Poodle | Amazon Parrot |
| puppy / puppies / dog / litter | chick / chicks / bird / parrot / clutch |
| adoption | reservation / bringing your bird home |
| Lawrence & Cathy | Mark & Teri Benjamin (Midland, TX, since 2014) |
| Virtual Adoption Consultant | **Virtual Flock Consultant** (the C.A.Gs decision-guide voice — still first-person we/us/our) |
| "Genetic ROI" | **Health-Documentation ROI** — PBFD + Avian Polyomavirus PCR screening, DNA sexing, avian-vet exam, hatch certificate, CITES Appendix I paperwork |
| OFA / CHIC / Embark DNA | PBFD PCR panel · APV PCR · DNA sexing certificate · avian veterinarian wellness exam · closed leg band |
| Mitral Valve Disease / PRA / White Shaker | Species-appropriate risks ONLY: greys = hypocalcemia, feather-destructive behavior, PBFD susceptibility; cockatoos = feather plucking, extreme noise, cloacal papilloma; macaws = proventricular dilatation awareness, bite-force/space needs; amazons = hormonal seasonal aggression, obesity/fatty liver |
| shedding / hypoallergenic | powder-down dander (greys & cockatoos are powder-down birds — allergy-relevant), feather dust management |
| Teacup trend debunk | **Unweaned-chick sales debunk** — cheap unweaned chicks = crop burns, aspiration, death; C.A.Gs sells fully weaned only |
| grooming | wing/nail/beak care, misting/bathing, cage hygiene |
| AKC recognized | CITES Appendix I listed · IUCN status (Congo Endangered / Timneh Vulnerable) — captive-bred USA framing ALWAYS |
| MFS prices | READ `data/price-matrix.json` + `data/financial-entities.json` — NEVER hardcode figures |

**Every claim stays inside the Verified-Claim Ledger** (`cag-entity-incorporation-agent` + `sessions/2026-06-03-homepage-entity-map.md`). PBFD/APV PCR screening IS assertable (confirmed 2026-06-20).

## 3. Per-Page Research Protocol (Sprint 0.5 — MANDATORY before any outline)

Replicate the Congo-vs-Timneh research file set for each page, saved to `sessions/comparison-research/<slug>/`:
`Keyword-Universe.md` · `Entity-Map.md` · `Internal-Linking.md` · `Visual-Asset-Blueprint.md` · `Implementation-Roadmap.md` · `Search-Quality-Checklist.md`

**12-part deliverable per page** (breeder-approved format, one page per session, clustered):

1. **SERP Snapshot** — top 7 real Google US results (Firecrawl/Playwright; un-fetchable = `NOT FETCHED`, NEVER simulated — the MFS source used simulated data; we do not). Why each ranks: authority, backlinks, topical depth, schema, UX.
2. **Search Intent** — informational / commercial / transactional / comparison / local.
3. **Competitor Reverse Engineering** (top 7) — title, meta, H1–H6, page voice, angle, frameworks, entity coverage + exploitable gaps, word count, media usage, schema usage.
4. **Keyword Universe** — primary, secondary, long-tail, long-form queries, compact keywords, PAA, Reddit-language queries, NLP/LSI terms, AI-Overview entities, branded/hybrid targets ("C.A.Gs vs …").
5. **Why Competitors Rank** — grounded per-competitor reasons.
6. **How C.A.Gs Wins** — our moat: real breeder data, health documentation, decision systems, first-person authority.
7. **Content Gap** — what's missing from ALL competitors.
8. **Recommended Page Structure** — full H1→H6, optimized for SEO + AEO + AI Overview + snippets.
9. **Schema / Technical** — FAQPage, Article/WebPage, BreadcrumbList; Product/Offer ONLY on the for-sale page; ItemList on hub.
10. **Internal Linking** — up to hub, sideways to sibling comparisons, down to `/congo-african-grey-for-sale/`, `/timneh-african-grey-for-sale/`, `/available/` birds, contextual to care/health/price pages. Anchors at sentence START (Link-First rule), never mid-sentence or end.
11. **Backlink Strategy** — avian blogs, breeders, rescue/education orgs, Reddit resources, pet journalists.
12. **Page Sections & Outline** — mandatory sections + competitor-derived sections + our-moat sections, **A/B/C categorized** (A=mandatory core, B=competitor-match, C=moat), total **22–25 sections**.

Research sweep sources per page: the 30 competitors in `data/competitors.json`, fresh top-7 Google, Bing, Reddit, Facebook + the manual research data in `assets/CAGs-BLOG-POSTS/`.

## 4. The 22–25 Section Blueprint (converted 22-section MFS template)

Pillar structure (adapt per page; hub compares grey vs ALL species with 2–3 H3 comparison metrics per rival):

| # | Level | Section | Notes |
|---|-------|---------|-------|
| 1 | H1 | Hero — "[A] vs [B]: Which Parrot Truly Fits Your Lifestyle, Home & Family?" | Split hero: left grey, right rival; image FIRST on mobile (before H1) |
| 2 | — | Counter Snippet strip | 12+ yrs aviary · 100% CITES · price floor · 24h reply |
| 3 | — | TOC (desktop sidebar / mobile sticky jump-rail) | |
| 4 | H2 | Quick Answer / Decision Summary Block | 40–60 word AI-extractable definition + "Choose [A] if… Choose [B] if…" |
| 5 | H2 | Key Takeaways (8 takeaways) | `cag-key-takeaway` stat-forward grid |
| 6 | H2 | Quick Comparison Table | 8–12 attributes immediately after intro H2 |
| 7 | H2 | Why an Objective Comparison (not a popularity contest) | E-E-A-T; define both species |
| 8 | H3 | The C.A.Gs Philosophy: Health-Documentation ROI | PCR screening, DNA sexing, CITES docs |
| 9 | H2 | Deep Dive: [A] — temperament, talking, size, bonding | comparison table after H2 |
| 10 | H3 | Temperament & Home/Apartment Suitability | |
| 11 | H3 | Health Risk Analysis (species-appropriate, ledger-bounded) | external authority links here |
| 12 | H3 | Noise, Dander & Daily Care | powder-down discussion |
| 13 | H2 | Deep Dive: [B] — same structure | |
| 14 | H2 | Decision Scorecard Matrix (0–10 traits) | talking, temperament, noise, beginner fit, apartment fit, bonding speed |
| 15 | H2 | Lifestyle Matching Flowchart | first bird? apartment? full-time worker? noise-sensitive? |
| 16 | H2 | Cost of Ownership Comparison (US) | from price-matrix + financial-entities; H4 first-year breakdown |
| 17 | H2 | First 30-Day Adjustment Timeline | Teri's first-30-days voice |
| 18 | H2 | Myth vs Reality Cards | H5 supporting facts, H6 breeder notes/citations |
| 19 | H2 | Health & Shipping section | canonical line: Ships nationwide · $185 airport · $350 home (read `delivery_options`) |
| 20 | H2 | Available Birds / Breeding Pair / Fertile Eggs cards | link-out, don't re-teach; sold ≠ InStock |
| 21 | H2 | Owner Story (BAB) + Reviews | REAL reviews only — never fabricate |
| 22 | H2 | Who Should Choose [A]? / Who Should Choose [B]? | H4 micro-intent answers per household type |
| 23 | H2 | FAQ (8–12 PAA questions, QAB) | FAQPage JSON-LD, visible accordion |
| 24 | H2 | Blog / further-reading cards | 3 relevant posts |
| 25 | H2 | Final CTA + page-specific inquiry form + newsletter | clay pill; `idPrefix` if 2 forms |

**Hard structural gates (non-negotiable):**
- Full **H1→H6 outline presented and approved BEFORE any code** — no skipped levels, all six levels, **≥5 H5 AND ≥5 H6**.
- **Every H2 and H3 carries an image** — OG photo, AI image, or HTML/CSS infographic (same rule as blog posts).
- Word counts: spokes **5,000–6,000**; hub **6,500–7,000**. 2–3 H3 comparison metrics per rival on the hub.
- Headers conversational/Quora-style, hybrid question+entity, **unique per page** (dup H2s across spokes = dup content).
- Section seam dividers (`.cag-seam` + footer logo) between major parts, 4–8 per page.
- No visible dates anywhere — freshness in schema only.

## 5. Interactive Decision Modules (converted "calculators")

Text/HTML-CSS modules (pure HTML/CSS/vanilla JS via `@cag-interactive-component`; NO ASCII boxes on the live page — those were the MFS draft format):
- **Lifestyle Selector** — "Which Parrot Fits Me?" (apartment → Timneh/Grey; talker → Congo; hands-on family → depends)
- **Size & Weight Comparator** — Congo 400–650g / Timneh 275–375g vs rival species
- **Price Range Estimator** — C.A.Gs price vs US average vs rival species average (from data files)
- **Noise-Level Meter** — grey vs cockatoo/macaw/amazon decibel reality
- **Talking-Ability Score** — the grey's signature advantage; honest per-bird variance note
- **First-Year Budget Estimator** — cage, food, avian vet, enrichment
- **Trust Documentation Panel** — flat-lay of DNA cert, CITES docs, hatch record, health guarantee

Snippet Box (📌 Quick Answer) opens every section — 1–2 sentence AI-extractable summary. Use line-icon SVGs, never emoji.

## 6. E-E-A-T & Voice Rules (converted)

- **Author box** near top: Mark & Teri, C.A.Gs – Midland, TX, linking to `/trusted-african-grey-parrot-breeders/`.
- **Original breeder data signals** — real, non-obvious observations from OUR aviary (Teri/Mark voice); NEVER invented statistics. If we don't have the number, we don't print a number.
- **External authority links** in health sections — World Parrot Trust, Lafeber, VCA, AAV, cites.org (curl 403 = bot-block, retry with UA, not dead). 6–8 diverse outbound links per page, anchored at sentence start (Link-First).
- First-person plural brand voice throughout; encyclopedic exceptions for taxonomy/research.
- Anti-AI writing filter + Style-2 gated humor (≤1 beat/section, never on health/legal).
- Negative keyword counter-positioning: wild-caught, scam, cheap unweaned chicks.

## 7. Keyword Fan-Out Categories (converted)

A. **Temperament** — affectionate, one-person bonding, calm vs demanding, apartment bird, separation anxiety, trainability
B. **Noise, Talking & Dander** — talking ability, mimicry, noise level, quiet parrot, powder down, allergy
C. **Size & Variant** — Congo vs Timneh size, full-grown weight, wingspan, maroon vs red tail
D. **Price, Lifespan & Health** — price comparison, 40–60 year lifespan, avian vet costs, PBFD, hypocalcemia
E. **Lifestyle Match** — best for seniors / families / apartments / first-time owners / busy professionals
F. **Commercial bridge** — for sale USA, breeder, hand-raised, captive-bred, DNA-tested (link down to money pages)
G. **AI/LLM layer** — "compare X and Y in detail", "help me choose", "pros and cons" phrasing blocks

## 8. Component System — 3 Variants (visual companion gate)

Component variants are decided ONCE for the cluster via the **superpowers visual companion** (browser mockup screens, breeder click-selects), then distributed: **Hero/Component set A → 3 species-vs pages · set B → congo-vs-timneh + pros-and-cons + breeders-comparison · set C → male-vs-female + hub.** Full component list and the Claude Design master prompt live in the session brief. Per-section **distribution matrix approval BEFORE code**, always with a Recommended pick + why + trade-off.

## 9. Imagery (Gemini / Nano Banana — no Higgsfield credit)

After outline approval, mark every H2/H3 needing OG photo vs AI image vs HTML infographic. AI prompts follow `IMAGE-DESIGNS.md` (crop ratios, negative list: no logos/watermarks/🦜/wrong species) + DESIGN.md palette, generated via `scripts/generate_nb_image.sh` (`GEMINI_API_KEY` in `.google-key`). Infographic widths: 760px wrapper (comparison body), 1100px hub hero; 400px desktop height. Image SEO 5-element on every image.

## 10. Pass Gates (page is NOT done until ALL pass)

`npx astro build` → verify in `dist/` → `python3 scripts/final_page_audit.py` → then the full breeder gate list: **SEO · AIO · GEO · AEO · entity coverage · topical authority · anti-AI · non-commodity · humor policy · keyword variation · keyword-verifier · technical SEO · Lighthouse (warm median-of-3)**. Preview before apply. Commit + push after every approved build (work on `main` only). Sitemaps regenerate after any page change.

## 11. Breeder-Review Component Standard (2026-07-04 — BINDING for all 8 pages)

The congo-vs-timneh rebuild was rejected once and redone; these fixes are now the floor for every
comparison page. Reference implementation: `src/pages/congo-vs-timneh-african-grey/index.astro`.

1. **Hero** — full-bleed band (background spans viewport, content in `.container`), homepage height
   (~380–480px desktop), copy LEFT / two staggered OG bird portraits CENTER-RIGHT with a small `vs`
   roundel at the overlap; mobile stacks **images first**. Eyebrow is **sentence case** (never
   uppercase), clay `#b04228`. H1 `clamp(1.75rem, 3vw, 2.25rem)`. Hero images get responsive
   `srcset` (480w + 800w) + `heroPreload`/`heroPreloadSrcset` in BaseLayout.
2. **No HTML/CSS infographics.** Every H2 + important H3 image slot is a real OG photo or a Gemini
   image (distinct design style per section, same DESIGN.md palette, 16:9 1600×900 → 760×400 slot).
   Prompt-pack template: `sessions/comparison-research/congo-vs-timneh-african-grey/2026-07-04-gemini-infographic-prompt-pack.md`.
   The real `<table>` stays in the DOM for AIO — an image never replaces it.
3. **Photo-first cards everywhere.** Bird cards = that bird's real photo + floating variant badge +
   price + shipping line. Breeding-pair ($3,000) and fertile-eggs ($95, buy-5-free-shipping) cards
   carry photos and **keyword variations not used elsewhere**. Shipping = two photo cards
   (`african-grey-home-delivery-pet-van.webp` / `african-grey-airport-live-animal-shipping.webp`)
   + a 7-place state/city pill row with FRESH anchors (each comparison page uses a different angle set).
4. **Sticky offsets** — site header is `sticky` and **96px** tall: jump rail `top:96px`, desktop TOC
   `top:calc(96px + 24px)`, every section `scroll-margin-top:calc(96px + 18px)`, `:global(html){scroll-behavior:smooth}`
   (+ reduced-motion opt-out). TOC column 200px / gap 34px (not 230/40) to widen the article column.
5. **Contrast floors** — buttons + solid chips fill `#b04228` with white (5.7:1); table verdict cells
   `#2D6A4F` bold (≥6:1); never clay-on-clay: inside the article column add
   `.cvt-main a.btn-clay{color:#fff;text-decoration:none}` or the generic link rule silently overrides it.
6. **Form = what we sell** — short inquiry form with: interest select (Congo / Timneh / breeding pair /
   fertile eggs / not sure, prices visible), first + last name, cell + confirm, email + confirm,
   delivery select ($185 airport / $350 home / Midland pickup), optional home note. Pass
   `hideGlobalCta` and ship NO page-level newsletter band (the form is the single closer).
7. **Testimonials = real reviews only**, pulled from the verified homepage `bottomReviews[]` set with
   real name + city; never the fabricated pair this page originally carried.
8. **Blog cards** use each post's own `-card.webp` hub thumbnail, never a shared generic image.
9. **Links at the START of sentences only (Link-First rule) — never mid-sentence, never the final words.** Seam dividers use
   `cag-footer-logo-80.webp` (the 200×66 original wastes ~7KiB per Lighthouse).
10. **Schema** — no page-level BreadcrumbList (the Breadcrumb component emits it; duplicates FAIL the
    gate). Title = 4-part ending in `C.A.Gs – <LSI keyword>` (never "C.A.Gs – Midland, TX" again).
11. **Gate** — `python3 scripts/final_page_audit.py --comparison` (profile added 2026-07-04) must
    return PASS/PASS-WITH-WARNINGS; the old `no_userselect_none` site-wide FAIL was a Tailwind
    `.select-none` false positive, fixed in the auditor.

## 12. Final Polish-Pass Fixes (2026-07-05 — BINDING, from the congo-vs-timneh finishing pass)

Every comparison page must clear these on its finishing pass, in addition to §11:

1. **Counter snippet is page-specific, not the homepage set.** The homepage's `12+ / 100% CITES /
   $1,500 floor / 24h` is generic. A comparison page leads with its own premise: for variant/species
   pages use **`2` Grey species raised here · `12+` Years raising both** (the "we raise both" moat),
   keeping `100%` CITES + `24h` reply as the two trust anchors. Never ship the verbatim homepage four.
2. **Responsive infographics (Lighthouse "improve image delivery").** Every 1408×768 `inf-img` ships a
   `-760.webp` sibling (Pillow LANCZOS, q82) + `srcset="/name-760.webp 760w, /name.webp 1408w"
   sizes="(max-width:900px) 92vw, 760px"`. Cuts ~40–55% off each (the congo-vs-timneh set went
   583→327 KiB). The 1408 stays as the retina/desktop candidate; the table stays in the DOM.
3. **Square OG portraits get a `.portrait` modifier** (`aspect-ratio:1/1;max-width:420px;margin:auto`).
   Bare `.sec-img` forces 760/400 cover and decapitates square close-ups — always check intrinsic
   dims; if the file is square/portrait, add `.portrait` and fix the `width`/`height` attrs to match.
4. **Non-primary data tables stack into cards on phones.** The mobile tab-toggle is ONLY for the main
   side-by-side table. The 6-trait scorecard (and any other `<table>`) needs `data-label` on each `td`
   + a `@media(max-width:640px)` block: `thead` offscreen, `tr`→bordered card, `td`→flex row with
   `::before{content:attr(data-label)}`. Note td stacks column-wise for long text.
5. **Internal links to the three money/authority hubs, anchored at sentence start (Link-First), from their own sections:**
   Reviews → `/african-grey-reviews/` (Owner Stories), FAQ → `/african-grey-parrot-faq/` (FAQ intro),
   Shipping → `/buy-african-grey-parrots-with-shipping/` (shipping body copy).
6. **Route pills carry a map-pin SVG + cream tint (`#f4efe9`), `inline-flex`; 2-col centered on
   mobile** (`.pin` stays `flex:none`). Body copy above the pills links the shipping page.
7. **Reversed head-term + American spelling coverage.** Weave "Timneh vs Congo" AND "African Gray"
   (with an *a*) once, naturally, in the Quick-Answer close; add **"What is the difference between…"**
   and **"How can you tell … apart"** FAQ objects (they feed both FAQPage schema and the open-3
   featured block). Dedupe against existing copy first — ignore keywords already on the page.
8. **Do NOT add Partytown for GA.** BaseLayout already interaction/idle-defers gtag.js off the critical
   path. Lighthouse's `unused JavaScript` (~72 KiB `/70de/`), `forced reflow`, `render-blocking`,
   `missing source maps`, and `cache TTL` flags are all **Cloudflare Rocket Loader** — a dashboard
   toggle + cache purge, never a repo fix. Note this in the page's fix log; don't chase it in code.

## §13 Component Polish Contract (2026-07-12 breeder pass — binding on every spoke, new or rebuilt)

Every fix below came from a breeder complaint on the live cluster (CvM screenshot session). They are
now the shipped baseline on CvT / CvM / CvC / MvF — new spokes copy these patterns, never the older ones.

1. **NEVER `scroll-behavior:smooth` on `html`.** On 60k-px comparison pages Chrome cancels the smooth
   fragment scroll at frame zero (lazy-image layout shifts), so every jump-rail tap looks dead: hash
   updates, page never moves. `scrollIntoView`/`scrollTo` still work, which misdirects debugging.
   Homepage baseline is `auto`; `scroll-margin-top` on targets does the offset work. Diagnostic: set
   `document.documentElement.style.scrollBehavior='auto'` and re-tap — if it jumps, that was the bug.
2. **Jump rail must be sticky — never re-`position` it.** `.cvt-rail{position:sticky;top:var(--hdr)}`
   is the contract. Adding `position:relative` later (e.g. "for the ::after fade gradient") silently
   kills sticky — a sticky element is already a containing block for absolute children. CvM shipped
   broken this way while its 3 siblings worked.
3. **Counter snippet = slim inline credential STRIP, not the hero-metric template.** The old design
   (40px circle icon chips + 2.1–2.2rem serif numbers + uppercase tracked labels + 4 stacked columns)
   is the exact "big number, small label" cliché DESIGN.md bans, and it rendered ~330px tall on
   phones. The shipped pattern: no icon chips at all; number and sentence-case label inline on one
   baseline (`display:flex;align-items:baseline;gap:9px`); numbers `1.4rem` Newsreader desktop /
   `1.2rem` tablet / `1.1rem` phone; labels `.8rem`→`.74rem` `font-weight:500`, NO uppercase, NO
   letter-spacing games; desktop one flex row with `1px rgba(255,255,255,.18)` hairlines (~54px
   band), ≤900px a 2×2 grid (~115–140px). Content stays page-specific per §12-1.
4. **`.container` eats vertical padding — pad the SECTION.** `.cvt .container` sets
   `padding:0 clamp(16px,4vw,48px)` at higher specificity, so `padding-top/bottom` on any
   `.container counter-row`-style element computes to 0 (the old counter never had its intended
   padding — that was the "rushed" look). Put band padding on the section: `.cvt-counter{padding:14px
   0}` desktop, `9px 0` mobile.
5. **Hero eyebrow (prefix) is UNIQUE per spoke, drawn from the page's own premise.** Never reuse the
   "Hand-raised · CITES-documented · Midland, TX" trust string across spokes — trust tokens live in
   the hero-meta pills. Shipped set: CvM "11 macaw species sized against one quiet genius" · CvC "The
   cuddler and the talker, weighed honestly" · CvT "Two Grey subspecies, raised side by side since
   2014" · MvF "Cock or hen · DNA-certain before you ever pay". A new spoke writes its own from the
   comparison premise; duplicate eyebrows across siblings FAIL the pass.
6. **Seam divider = brand medallion + light-orange fading hairlines.** `img
   src="/cag-header-logo-160.webp"` (the ONLY square logo asset — every `cag-footer-logo*` /
   `cag-seam-logo` / `cag-logo-badge*` file is a wide wordmark that letterboxes into a smudge inside
   the circle), `width/height=54`, CSS `object-fit:cover;padding:2px;border:2px solid
   rgba(232,96,76,.35);border-radius:50%`. Lines: `height:2px;border-radius:1px` fading gradients to
   `rgba(240,128,112,.6)` (--clay-lt), replacing the old faint 1px `#cdbfae`.
7. **Middle newsletter is ALWAYS `NewsletterV2 variant="middle" compact`.** The full-height variant's
   36px H2 overtakes the page H1 in the 768–860px band (MvF shipped that inversion). `compact` is not
   optional on comparison spokes. (CvT currently has no middle newsletter — decision pending.)
8. **H1 must outrank every H2 at EVERY width, including one-off hero H1 classes.** The
   breeders-comparison `bc-h1` clamp `(1.8rem, 3.5vw, 2.75rem)` sat on its floor through the whole
   375–860px band underneath a static 36px CTA H2. Fixed form: `clamp(1.9rem, 0.5rem + 4.5vw,
   2.75rem)`. Sweep rule: resolve the clamp at 375/640/768/860/1280 and compare against the largest
   H2 (usually the CTA/newsletter component) before shipping.
9. **Image budget <100KB per delivered file.** Recompress with Pillow WebP `method=6`, walk quality
   78→54 until <95KB (cites-flatlay 101→94KB q66, vs-eclectus-hero 122→89KB q66 — certificate text
   still crisp). Masters in `assets/brand/` untouched.

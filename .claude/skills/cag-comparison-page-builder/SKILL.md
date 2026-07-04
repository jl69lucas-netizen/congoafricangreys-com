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
10. **Internal Linking** — up to hub, sideways to sibling comparisons, down to `/congo-african-grey-for-sale/`, `/timneh-african-grey-for-sale/`, `/available/` birds, contextual to care/health/price pages. Anchors mid-sentence, never at end.
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
- **External authority links** in health sections — World Parrot Trust, Lafeber, VCA, AAV, cites.org (curl 403 = bot-block, retry with UA, not dead). 6–8 diverse outbound links per page, mid-sentence.
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

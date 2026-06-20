# Remaining Available-Bird Pages — Build Design (Amie first)

**Date:** 2026-06-20 · **Status:** Approved in brainstorming (visual companion) · **Next:** writing-plans
**Reference build:** `src/pages/available/roys/index.astro` (the live gold standard)
**Supersedes/extends:** `docs/superpowers/specs/2026-06-19-bird-pages-expanded-seo-design.md` (this pins the per-section matrix + image-source split + the keyword-dose + Blog-hub decisions taken 2026-06-20)

## Goal
Apply the full "Roys treatment" to the 5 remaining **available** birds, building **Amie first** as the worked example, then templating to the rest. Each page = ~5,700 visible words, 23 sections, H1–H6, mixed HTML-card infographics + Gemini-generated graphics + real breeder photos. First-person C.A.Gs voice, CITES Appendix-I/captive-bred-USA safe, no visible dates, single `Product`+`Offer` schema, Verified-Claim Ledger bounded.

## Scope — the 5 birds (Batch 1)
Facts verified against homepage cards (`src/pages/index.astro`) + `data/clutch-inventory.json`, 2026-06-20.

| Bird | Sex | Variant | Age | Price | Note |
|---|---|---|---|---|---|
| **Amie** | ♀ | Congo | 3 mo | $2,500 | Worked example; hand-raised, full social training |
| Bery | ♀ | Congo | 1 yr | $1,700 | Hand-raised, gentle; past the hand-feeding stage |
| Jins + Jeni | pair (♂ Jins 6mo + ♀ Jeni 4mo) | Congo | 4–6 mo | $3,500 pair | **Unrelated companion pair — must be adopted together. NOT a breeding pair.** Pair-adapted structure |
| Elad | ♂ | **Timneh** | 5 mo | $1,600 | Hand-raised, full social training |
| Evie | ♀ | **Timneh** | 6 mo | $1,500 | Hand-raised, gentle & sociable; lowest price |

> Variant note resolved 2026-06-20: Elad **and** Evie are Timneh per both inventory and the homepage cards (the earlier "inventory says Congo" note was an error and is removed). Jins + Jeni are an **unrelated companion pair sold together**, never framed as a breeding pair.

## The 5 transactional angles (one distinct keyword lane per bird — no cannibalization)
Every page is **transactional-first**. Roys already owns *male congo african grey for sale* — each new bird takes a **different lane** so they don't compete in the SERP. Each lane spans all tiers: **primary** · **long-tail / long-form phrase** · **LSI / NLP entities** · **compact**.

| Bird | Primary (transactional) | Long-tail / long-form | LSI · NLP entities | Compact |
|---|---|---|---|---|
| **Amie** | **baby congo african grey for sale** | "hand-raised baby female congo african grey for sale", "3-month-old congo african grey parrot for sale near me" | weaning, hand-fed chick, fledgling, fully socialised, clutch, DNA-sexed female | baby congo grey, female CAG |
| **Bery** | **hand-raised congo african grey for sale** (started/older bird) | "1-year-old congo african grey for sale", "started congo african grey parrot past hand-feeding for sale" | weaned, started bird, settled temperament, gentle, easier first transition | started congo grey, young adult grey |
| **Jins + Jeni** | **pair of african greys for sale** | "two hand-raised african greys for sale together", "bonded congo african grey pair must go together — not a breeding pair" | companion pair, sibling-bond/cohort-bonded (not mated), buy-two, adopt-together, dual cage setup | african grey pair, grey duo |
| **Elad** | **male timneh african grey for sale** | "hand-raised male timneh african grey parrot for sale", "timneh african grey for sale — calmer, earlier-talking grey" | Psittacus timneh, maroon tail, calmer temperament, earlier talker, first-time-owner friendly | male timneh, timneh grey |
| **Evie** | **female timneh african grey for sale** | "gentle female timneh african grey for sale", "baby timneh african grey parrot for sale — value priced" | Psittacus timneh, sociable hen, value-priced, gentle, lower body-weight (275–375g) | female timneh, timneh hen |

**Does this redo anything?** **No.** The 23-section template, frameworks, image strategy, mobile-fit rule, and schema shape are bird-agnostic and unchanged. Only the **per-bird keyword/angle layer** — which the spec always defined as bespoke ("never copy Roys's angle") — is now filled in correctly. Zero rework to the approved matrix; this *sharpens* the per-bird customization, it doesn't reopen the design.

## Approved decisions (this session, 2026-06-20)

1. **Research model — reuse, don't re-run.** The 30-competitor SERP landscape is shared across all Congo birds and was freshly analysed 2026-06-19 (`docs/research/2026-06-19-bird-pages-competitive-analysis.md` + `sessions/2026-06-19-roys-outline.md`). Reuse that as the **cluster playbook**; do only **per-bird fan-out / angle / keyword** work per page. Do NOT re-pull 30 competitors per bird.

2. **Keyword dose — selective (Option A).** Insert the head term "African Grey" into **only ~5–6 high-intent headers** (marketplace, price, delivery, buy-steps, compare), kept natural. NOT all 22 headers (= stuffing, breaks conversational/first-person voice). Fixes to the user's draft: drop redundant "**bird**" ("an African Grey from C.A.Gs", not "African Grey bird"); never ship the quote marks. Applies site-wide to every bird page header from now on.

3. **Section structure — 23 sections** = Roys's live 22 + **1 new "Care Guides & Resources" (Blog hub)**. See matrix below.

4. **Blog & Resources placement — Slot B:** after the Reviews grid (§20), before the Marketplace counter (§21). Mirrors the homepage (Reviews → Resources → close); Marketplace + Reserve follow it to re-converge any diverted researcher.

5. **Image strategy — 80% HTML / 20% Gemini (among generated graphics) + real photos separate.**
   - 🟩 **HTML card → screenshot** = the workhorse for all data infographics (personality, comparison, cost breakdown, doc checklist, what's-included, diet wheel, buy-steps timeline, resource cards). Free, on-brand (forest header / clay bars / Newsreader serif), text always correct, editable.
   - 🟦 **Gemini-generated** (user generates manually in free Gemini for now; API credit later) = photoreal/designed only. For Amie that's **2 sections**: §12 long-term lifestyle scene + §18 US delivery-map base (textless; labels overlaid in HTML). Optional 3rd: branded trust panel.
   - 🟧 **Real WebP photos** (breeder supplies per bird) = hero, gallery, health/handling, parents, training hand-shot, talking clip, buyer-review photos.
   - **Mobile-fit rule (binding):** every HTML infographic is built **mobile-first** — columns stack vertically ≤640px, screenshot taken at a portrait/square ratio that scales to phone width with **no horizontal scroll** (fixes the homepage wide-infographic problem). Wrapper widths per `docs/reference/page-width.md` (760px guide / 1100px home tier); never bake a fixed wide table that overflows phones.

## Per-section matrix — Amie (the template)
Category: **A** = mandatory core · **B** = competitor-match · **C** = our moat. Image: 🟩 HTML · 🟦 Gemini · 🟧 real photo · — none.

| # | Section (Quora-style H2) | Framework | Words | Cat | Img | Why (B/C) |
|---|---|---|---|---|---|---|
| 1 | Hero / "Amie at a glance" vitals + CTA | AIDA·BLUF | 120 | A | 🟧 | Real bird hero (LCP); $2,500 in first 3 lines |
| 2 | On This Page (TOC) | — | 0 | A | — | Chrome |
| 3 | What is Amie like to live with? | AIDA | 520 | A | 🟩 | Personality card |
| 4 | Does a female Congo African Grey talk well? | EBP | 300 | B | 🟧🟦 | Competitors all claim "talks"; we prove via Maxy video (reuse) |
| 5 | Why does Amie cost $2,500 vs "$850" greys? | PDB | 480 | C | 🟩 | Nobody else justifies price honestly; cost-breakdown HTML |
| 6 | What documentation comes with Amie? | EBP | 240 | C | 🟩 | Full DNA/CITES/AAV docs; doc-checklist HTML |
| 7 | What's included when you reserve Amie? | QAB | 300 | A | 🟩 | What's-included card |
| 8 | How does Amie compare to our other available greys? | — | 180 | B | 🟩 | Beat range-tables with named birds; comparison table |
| 9 | Is Amie a healthy bird? Our health standard | EBP | 320 | A | 🟧 | Real health/handling photo |
| 10 | Who are Amie's parents? | EBP | 210 | C | 🟧 | "From our own flock"; real parent photo |
| 11 | What should you decide before buying an African Grey? | BAB | 300 | B | 🟩 | Care-guide intent; honest checklist |
| 12 | What's it like to own an African Grey long-term? | BAB | 420 | B | 🟦 | Emotional ownership arc; **Gemini lifestyle scene** |
| 13 | Reviews — families who brought home a C.A.Gs grey | — | 120 | A | 🟧 | Real buyer photos |
| 14 | How do you train an African Grey like Amie? | HowTo | 360 | B | 🟧 | Training intent + HowTo schema; real hand/step-up shot |
| 15 | What do C.A.Gs recommend feeding African Greys? | QAB | 300 | B | 🟩 | Diet intent; diet-wheel HTML |
| 16 | Amie's photo & video gallery | — | 40 | A | 🟧 | Real gallery (4–5 + video) |
| 17 | How do you buy Amie? Step-by-step | AIDA | 200 | A | 🟩 | Buy-steps timeline |
| 18 | Where do C.A.Gs deliver African Greys? | QAB | 420 | B | 🟦 | Shipping reassurance; **Gemini US delivery-map base + HTML label overlay** |
| 19 | Amie — frequently asked questions | QAB | 300 | A | — | FAQPage schema |
| 20 | Reviews — more happy C.A.Gs owners | — | 120 | A | 🟧 | Real buyer photos (grid) |
| **22→** | **★ NEW Care Guides & Resources (Blog hub)** | — | 80 | B | 🟩 | Internal-link hub like homepage; topical authority. **Placed here (Slot B)** |
| 21 | Why buy an African Grey from C.A.Gs vs a marketplace? | EBP | 480 | C | 🟩 | Accountability moat; **keyword-dose edit lands here**; compare-panel HTML |
| 23 | Ready to bring Amie home? (Reserve) | AIDA | 80 | A | — | Inquiry form + newsletter (one placement) |

**Totals:** ~5,700 words. Image mix ≈ 10 🟩 / 8 🟧 / 2–3 🟦 → ~80/20 HTML:Gemini among generated graphics. Auditor `wordcount_in_band` WARN expected/accepted (per polish-program decision).

## Gemini prompts (delivered to breeder; he generates in free Gemini)
- **§12 lifestyle** → `amie-african-grey-family-long-term.webp`, 4:3. Adult Congo (grey body, RED tail, white face mask, pale-yellow iris, dark beak) bonded with owner in warm cream/wood/green home, 35mm f/2.8, golden window light. Full negative list (no text/other species/green parrot/jungle/cages/sharp faces).
- **§18 delivery map** → `cag-us-delivery-map-base.webp`, 16:9, **textless**. Flat-design US map, forest-green land on cream, clay hub dot in West Texas with clay route arcs to destination dots. Labels (Midland/LAR hub, cities, $185 airport · $350 home tiers) overlaid in **HTML** afterward (keeps text accurate + mobile-responsive).
- Optional §6 trust panel — only if breeder requests.

## Per-bird customization (what changes vs the template)
Constant: structure, frameworks, image-source map, voice, schema shape, mobile-fit rule. **Bespoke per bird:** the transactional lane above (primary + long-tail/long-form + LSI/NLP + compact), personality/archetype copy, price + what's-included figures, parent birds, real photo set, FAQ specifics, the bird's individual angle (never copy Roys's angle — polish-program rule). **Jins + Jeni** use a **pair-adapted** structure: two birds profiled, **unrelated-companion-pair** framing (explicitly "not a breeding pair"), pair pricing ($3,500), and a "why adopt two greys together" section; schema still single `Product` for the pair offer.

## Constraints (binding)
- Build on **`main`**, `src/pages/available/<slug>/index.astro`, commit + push after each page (push = deploy).
- Confidence Gate ≥97% before writing; Clarification Checkpoint if it drops mid-build.
- Single `Product`+`Offer` per bird (never `AggregateOffer` — that's the variant page). Sold ≠ InStock.
- Shipping line on every card: `Ships nationwide · $185 airport · $350 home`; figures from `data/financial-entities.json` / `data/price-matrix.json`.
- Line-icon SVGs, never 🦜; CAG images `/emoji/cag-congo.png` for the grey glyph.
- Image SEO 5-element set on every image; real photos only for 🟧 slots (no fabricated trust signals).
- Final gate: `npx astro build` → `python3 scripts/final_page_audit.py --birds` → deploy → `scripts/generate_sitemaps.py`.

## Out of scope (later batches)
Money/variant, comparison, location, interior, blog page polish (run after Batch 1 per the sitewide-polish program sequence). Real-photo capture is the breeder's task between sessions.

## Build status
- **Amie — BUILT + LIVE (2026-06-20):** `src/pages/available/amie/index.astro`, 23 sections, ~6,567 words, full H1–H6, single Product/Offer, FAQPage schema, Care Guides block (Slot B), delivery-coverage map with HTML overlay. Bird audit = PASS-WITH-WARNINGS (only the expected wordcount/house_method WARNs). 14 images processed → `public/birds/amie/` (<100 KB except the two text-dense infographics, capped ~115 KB for legibility). Verified in mobile preview: no page-level horizontal scroll, all images load, no console errors.
- **OPEN — Amie §10 parents photo:** breeder to send Amie's sire/dam photo (decision 2A). Section is live as honest text-only ("we're happy to share photos… just ask"); when the photo arrives, re-add the parent card (reuse the Roys §10 card markup) at `/birds/amie/amie-parents.webp`.
- **Next birds (reuse `scripts/scaffold_amie_from_roys.py` pattern):** Bery, Jins+Jeni (pair-adapted), Elad (Timneh), Evie (Timneh) — each with its own transactional lane + bespoke angle + real photos.

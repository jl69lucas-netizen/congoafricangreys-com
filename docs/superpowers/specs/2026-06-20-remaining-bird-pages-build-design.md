# Remaining Available-Bird Pages — Build Design (Amie first)

**Date:** 2026-06-20 · **Status:** Approved in brainstorming (visual companion) · **Next:** writing-plans
**Reference build:** `src/pages/available/roys/index.astro` (the live gold standard)
**Supersedes/extends:** `docs/superpowers/specs/2026-06-19-bird-pages-expanded-seo-design.md` (this pins the per-section matrix + image-source split + the keyword-dose + Blog-hub decisions taken 2026-06-20)

## Goal
Apply the full "Roys treatment" to the 5 remaining **available** birds, building **Amie first** as the worked example, then templating to the rest. Each page = ~5,700 visible words, 23 sections, H1–H6, mixed HTML-card infographics + Gemini-generated graphics + real breeder photos. First-person C.A.Gs voice, CITES Appendix-I/captive-bred-USA safe, no visible dates, single `Product`+`Offer` schema, Verified-Claim Ledger bounded.

## Scope — the 5 birds (Batch 1)
| Bird | Sex | Variant | Age | Price | Primary keyword | Note |
|---|---|---|---|---|---|---|
| **Amie** | ♀ | Congo | 3 mo | $2,500 | female congo african grey for sale | Worked example; full social training |
| Bery | ♀ | Congo | 1 yr | $1,700 | hand-raised congo african grey for sale | |
| Jins & Jeni | pair | Congo | — | $3,500 | african grey breeding pair for sale | **Different structure** (bonded pair, not single bird) |
| Elad | ♂ | (verify variant) | — | $1,600 | male african grey for sale | Inventory says Congo; polish-program memory says Timneh — **confirm before build** |
| Evie | ♀ | (verify variant) | — | $1,500 | female african grey for sale | Same variant-discrepancy flag as Elad |

> **Open flag:** clutch-inventory.json lists Elad/Evie as `congo_african_grey`; the sitewide-polish memory calls them Timneh. Resolve with the breeder before building those two; Amie/Bery/Jins&Jeni are unaffected.

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
Constant: structure, frameworks, image-source map, voice, schema shape, mobile-fit rule. **Bespoke per bird:** primary keyword + fan-out, personality/archetype copy, price + what's-included figures, parent birds, real photo set, FAQ specifics, the bird's individual angle (never copy Roys's angle — polish-program rule). Jins & Jeni use a **pair-adapted** structure (two birds, bonded-pair framing, pair pricing).

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

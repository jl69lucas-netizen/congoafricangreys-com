---
name: cag-for-sale-page-builder
description: THE transactional for-sale page builder for CongoAfricanGreys.com — 22-page cluster (17 for-sale + 5 buy-prefixed). Merges the MFS on-page-SEO formula (keyword distribution 85–105, EFBP openings, conversational headers, counter snippets) with the comparison-cluster pipeline (per-page research protocol, dup-gate, uniform image boxes, final-page-pass) under a TRANSACTIONAL profile — bird cards + prices above the fold, Product/Offer schema, reserve CTAs every 500–700 words, contact form with real birds + prices. Default mode is REBUILD (all 22 slugs are LIVE). Use for any "for sale" / "buy" page build, rebuild, or polish.
---

# SKILL: CAG For-Sale Page Builder (v1.0 — 2026-07-19)

**Sources merged:** `assets/1WORKING-ON/FOR-SALE-PAGES/FOR-sale-PagesSKILL.md` (MFS content/SEO formula) + `maltipoo-implementation.md` (MFS build/QA workflow), both converted MFS→CAG. Program plan: `docs/superpowers/plans/2026-07-19-for-sale-pages-program.md`.

**How this differs from `cag-comparison-page-builder`:** comparison pages serve DECISION intent (X vs Y, neutral tables, hub+spoke). For-sale pages serve TRANSACTIONAL intent: real available-bird cards with prices near the fold, deposit/reserve CTAs on a cadence, Product+Offer schema, honest scarcity, and a contact form listing actual birds. Everything the comparison cluster locked (dial TOC + mobile jump-rail, uniform image boxes, dup-gate, seam dividers, image-per-header) carries over but RESTYLED so the two clusters never look identical.

---

## 1. Page inventory & build order (ALL LIVE — confirm on-disk slug in `src/pages/` first; REBUILD mode)

**BUILT so far:** ① `/african-grey-parrot-bird-eggs-for-sale-usa/` (2026-07-20) · ② `/congo-african-grey-for-sale/` (2026-07-21 — tuple: Split-Hero B warm gradient · Dial 2 Dark-Aviary · Rail A · T5 stepper · K1+K4+K3 · Table A · **FAQ-A light bordered**; page-scoped under `.congo`; reword ALL egg-sibling prose before dup-gate — see `sessions/2026-07-19-for-sale-component-map.md` tuple ledger + memory `project_congo_for_sale_build`).

**Cluster 1 (first 6):**
1. `/african-grey-parrot-bird-eggs-for-sale-usa/` — **truth-forward hybrid** (see §7 Egg Rule)
2. `/congo-african-grey-for-sale/`
3. `/timneh-african-grey-for-sale/`
4. `/hand-raised-african-grey-parrot-for-sale/`
5. `/african-greys-for-sale-with-health-guarantee/`
6. `/dna-tested-african-grey-for-sale/`

**Cluster 2 (5):** `/african-grey-parrot-adoption-cost/` · `/african-grey-parrots-for-sale/` (hub) · `/baby-african-grey-parrot-for-sale/` · `/african-grey-parrot-for-sale/` · `/african-grey-parrot-for-sale-near-me/`

**Cluster 3 (6):** `/congo-african-grey-parrot-pair-for-sale/` · `/affordable-african-grey-birds-for-sale/` · `/grey-african-parrots-for-sale/` · `/male-african-gray-for-sale/` · `/african-grey-parrots-for-sale-near-me/` · `/african-grey-breeding-pair-for-sale/`

**Cluster 4 (buy-prefixed, 5):** `/buy-african-grey-parrot-near-me/` · `/buy-african-grey-parrots-with-shipping/` · `/buy-intelligent-african-grey-for-sale-ca/` · `/buy-male-african-gray-birds-for-sale-nyc-ny/` · `/where-to-buy-african-greys-near-me/`

Cannibalization guard: each page owns ONE primary intent; near-me vs plural-near-me vs buy-near-me get DISTINCT keyword sets, headers, and geo distributions (unique 4–5 state/city set per page, real slugs, never the same trio — same rule as bird pages).

## 2. Content formula (from FOR-sale-PagesSKILL, CAG-converted)

### 2a. Keyword distribution per page (~85–105 total mentions; 1–2% primary density, never stuffed)
| Type | Count | Note |
|---|---|---|
| Primary keyword | 30–35 | natural placements; front-loaded in title/H1/first 100 words |
| LSI | 20–25 | across variations |
| Long-tail (6+ words, conversational) | 15–20 | in headers + opening paragraphs |
| Branded ("C.A.Gs", "Mark & Teri Benjamin", "C.A.Gs reviews/pricing") | 10–15 | per cag-branded-hybrid-keywords |
| Conversational/voice queries | ~23 | headers + PAA answers |
| Comparison ("Congo vs Timneh", "male vs female") | 5–8 | link to comparison cluster |
| Solution ("scam-free", "with health guarantee") | 5–10 | |
| Transactional ("reserve", "deposit", "available now") | ~15 | honest only |

Source for the actual keywords: `docs/research/for-sale-keywords-2026-07.md` (mined from the fresh GSC `Queries.csv`/`Pages.csv` + Bing CSV) + per-page Sprint 0 research doc. NEVER invent keyword data.

### 2b. EFBP opening paragraph — under EVERY header (also satisfies the pass-gate "opening paragraph under every header")
Every H2/H3/H4 opens with 1–2 sentences containing **Entity + Feature + Benefit + Purpose**, first-person voice:
> "Roys (entity) is a 3-year-old DNA-sexed male Congo we hand-raised here in Midland (feature); he thrives in busy family homes (benefit), which is why we match him to households with kids and activity rather than quiet apartments (purpose)."

### 2c. Headers
Conversational Q&A style (What/How/Is/Can/Where), per the Heading Hierarchy Outline Gate: full H1→H6 outline approved BEFORE any code, no skipped levels, all six levels, **≥5 H5 AND ≥5 H6**. Semantic map: H1 topic · H2 search intents · H3 subtopics · H4 PAA/micro-intents · H5 supporting facts/warnings · H6 breeder notes/citations. Draft 5 A/B variants for H1 and each major H2 during outline stage; breeder picks. Two-Keyword Headers rule (Rule 28b) applies. Unique hybrid headers per page — zero exact or template crossover with siblings (dup-gate `--headers`).

### 2d. Entity variety — the MFS anti-stuffing lesson (binding)
85–112 **DIFFERENT** entities per page (birds by name, Midland/TX geo, CITES Appendix I, USDA AWA, DNA sexing labs, PBFD/Polyomavirus PCR, Delta/United/American cargo, IATA LAR, pellet brands, avian-vet terms) — each mentioned a natural number of times. The MFS log documents the failure mode: business name in every sentence = unreadable, unrankable. Targets: brand 5–10×, full location 1–2× + city/state 5–8×, each bird named in its card + 1–2 body mentions. All health/credential entities bounded by the **Verified-Claim Ledger**.

### 2e. Meta
Use the CAG 2 long formats (Title ≤205 · Desc F1 ≤185 / F2 ≤300) — NOT the MFS 275-char format. 3 sets per page (Educational / Benefit-Solution / Transactional-Urgency), one marked (Recommended) with why + trade-off. Front-load primary keyword; include real price floor, real credentials, branded ending.

### 2f. Counter snippets
8 per page, <4 words, number-led, Ledger-verified only (e.g. "12+ Yrs Aviary" · "100% CITES Papered" · "$1,500 Floor Price" · "24h Reply" · "0 Wild-Caught"). NEVER fabricated counts (no fake "184 families", no fake ratings).

### 2g. Links
Link-First anchors (sentence START, never mid/end; branded ACTION anchors on CTAs exempt). Internal anchors from the Anchor Diversity Ledger (`internal-link-agent` — no repeated anchors site-wide). External: authority set from `docs/reference/external-link-library.md` (World Parrot Trust, CITES.org, USDA-APHIS, AAV, Lafeber, IUCN — cite the specific resource page; curl 403 ≠ dead, retry with UA). Internal same-tab, external new-tab + ↗.

## 3. Transactional layer (what makes these NOT comparison pages)

1. **Bird cards near the fold** — real inventory from `data/clutch-inventory.json`, price from `data/price-matrix.json`, shipping line under trust badges: `Ships nationwide · $185 airport · $350 home`. Never a card without the cost line.
2. **Schema** — one `Product`+`Offer` per real bird; `AggregateOffer` ONLY on group/hub pages; sold ≠ `InStock` ever; extend existing JSON-LD, never duplicate; verify in `dist/`.
3. **CTA cadence** — a reserve/inquire CTA every 500–700 words (clay pill, branded action anchor); respect the one-global-CTA rule (`hideGlobalCta` when shipping own CTA band). Mid-page CTAs → `#reserve`/form anchor.
4. **Honest scarcity only** — real counts ("2 hens reservable"), real waitlist. No fabricated urgency, testimonials, or review counts (reviewCount = 52 real, rating 4.9 — only where already sanctioned).
5. **Contact form (every page in this cluster)** — the `cag-inquiry-form` instance must: (a) list each ACTUAL available bird with its price as select options (source: clutch-inventory + price-matrix, never hardcoded), like the homepage/contact-us forms; (b) include delivery option `Pickup in Midland, TX — if you live within 2–3 hours of us` alongside the $185/$350 tiers.
6. **Negative-keyword counter-positioning** — wild-caught / scam / "cheap" handled head-on with green-flag framing; scam module links to the scam cluster.

## 4. Build phases (from maltipoo-implementation, CAG-converted — maps to program-plan Tasks 4–10)

- **Phase 1 Research (MANDATORY, no skip):** fresh GSC+Bing mining (top-20 positions, high impressions, ALL 6+-word queries) → Sprint 0 deep comp research per page (Google/Bing/Reddit/FB/IG/YT top 10 + the 30-competitor registry; un-fetchable = NOT FETCHED) → deliverables identical to the comparison cluster (SERP snapshot, section inventory, gaps, keyword universe, entity map, visual blueprint, PAA set). Model docs: `RESEARCH-DATA-FOR-SALE-PAGES.md` (egg/congo/timneh/adoption-cost).
- **Phase 2 Planning gates:** grill-me (Sprint 0.5) → **two strategies + one blended**, one (Recommended) → distribution matrix with **MANDATORY / COMPETITOR-BASED / SUGGESTED-RECOMMENDED** section groups (grounded why on each) → H1–H6 outline gate (+ header dup-gate BEFORE approval) → visual-companion skeleton screens → **HARD STOP until breeder drops images and explicitly says start**.
- **Phase 3 Build:** section-by-section per approved matrix on `main`; verify rendered `dist/` per page; commit + push per page.
- **Phase 4 QA/Deploy:** dup-gate (body + headers, pairwise vs ALL 21 siblings + comparison cluster + variant pages) → `final_page_audit.py` for-sale profile → manual pass-gate list (§6) → `generate_sitemaps.py` → push → live 200.

## 5. Component map (for-sale set — approved via visual companion, Task 5 of the plan)

- **LOCKED 2026-07-19:** ALL Task-5 designs approved — recommended picks are defaults, alternates rotate per page; full assignment table + rotation rules + per-page tuple ledger live in `sessions/2026-07-19-for-sale-component-map.md` (binding).
- **5 Heroes** (assign per cluster, breeder-approved table in `sessions/2026-07-19-for-sale-component-map.md`): Hero-A Scattered Flock (Polaroid scatter) · Hero-C Mosaic Metrics (stats strip + mosaic) · Split-Hero A (image left + trust ribbon) · Split-Hero B (full-bleed warm gradient) · Split-Hero C (dark + photo grid). ~400px-class heights, hero staggered sizing rules apply.
- **Dial TOC (desktop) + jump-rail (mobile)** — same mechanics as comparison pages, NEW for-sale style (distinct accent/motif; scroll-margin offset for the mobile rail; `scroll-behavior: auto`).
- **TOC + KeyTakeaway** — 3 breeder-approved NEW designs each (picked from 5), completely different from cag-toc-v1/v2/v3 + cag-key-takeaway-v2.
- **Orange stacking tables** — the 5-parrot table set (Congo/Timneh/Macaw/Cockatoo/Amazon) added to the required orange designs; stack on mobile like the comparison cluster; species markers use `/emoji/cag-congo.png` + `/emoji/cag-timneh.png` imgs — **NEVER 🦜**.
- **In-body images** — uniform `.sec-img.inf-img` 760px 16:9 box for EVERY OG photo AND infographic (<100 KB WebP + `-760.webp` sibling + srcset). **Every H2, H3, and key H4 gets an image** (OG or infographic/AI). Rule 50b alt rotation — no two images share an alt.
  - **OG-photo framing (LOCKED default — do NOT cover-crop a portrait with a focal point; that cuts heads):** bake single-bird/pair portrait photos with `scripts/reframe_og.py --style blurfill --mobcrop 4:5` from the ORIGINAL master (in `assets/1WORKING-ON/FOR-SALE-PAGES/.../<BIRD>/`), tag `<img class="sec-img og-photo og-tall">`, and ship the mobile full-bleed 4:5 rule (`.sec-img.og-tall{width:100vw;margin-left:calc(50% - 50vw);aspect-ratio:4/5;border-radius:0}`). Desktop stays the uniform 16:9 box; mobile gets the distinct taller full-bleed frame; the subject is dual-safe so it is never clipped at either width. Wide/scene/infographic images stay standard 16:9 / mobile 5:4. Full spec + named Styles A/B/C/E/H: **`IMAGE-DESIGNS.md §7`**.
- **Seam divider** — footer-logo divider, a for-sale-specific variant style, 4–8 per page, decorative alt="" + lazy + CLS dims.
- **Sidebar** — NO page-level sidebar (breeder-ratified recommendation); Avail-B sticky-filter used only as a section-level component inside available-birds sections; sticky mobile CTA bar covers persistent-CTA needs.
- **Stale-fact reconciliation on ALL kit intake (binding):** kit copy says Appendix II → **always CITES Appendix I**; fake pairs (Bella/Oliver/Rosie/Max) → real birds/pairs only (ask breeder per-bird parentage); fake ratings/counts (4.97 · 184) → real 4.9 · 52; "3-year guarantee" → the real guarantee per Ledger; fake phone → real NAP from credentials.md; 🦜 → cag-congo/cag-timneh imgs; kit palette → DESIGN.md tokens + AA clay variants.

## 6. Pass gates (every page)

0. **Write-From-Outline, NEVER-From-Sibling (pre-write discipline — CLAUDE.md non-negotiable rule #1).** Reuse **components, CSS classes, and structural patterns** freely (that IS this kit), but every page's **prose** is written fresh from its own approved H1–H6 outline + distribution matrix — never pasted or paraphrased from a sibling for-sale/comparison/variant page. Open a sibling only to read its component/CSS structure, never to copy paragraphs. Lean on the page's OWN entity/angle (Timneh = smaller/calmer/maroon/earlier-talker/Levi×Rily; Congo = bigger/red-tail/headline-talker). Only the **whitelist** may match verbatim (shipping line, doc-badge lists, counter strip, CITES notice, CTA labels, real reviews, real page-name link labels). Run `scripts/dup_content_audit.py` (body) **AND** `--headers` on YOUR OWN draft BEFORE it is "done", targeting **zero** non-whitelist crossover. Dedup is a pre-write discipline, not post-hoc cleanup. (Saved to memory `feedback_write_from_outline`.)

1. `dup_content_audit.py` + `--headers` — zero tolerance beyond whitelist (shipping line, doc badges, CITES notice, site furniture).
2. `python3 scripts/final_page_audit.py` — PASS required (all_six_levels, min 5 H5/5 H6, no visible dates, schema, meta).
3. Manual gate list (comparison contract, restated): 400px heroes · unique newsletter image + one-liner title per page (no shared images) · opening paragraph under every header · uniform OG boxes · separate blog/contact H2s · mobile table stacking · jump-rail scroll-margin · further-reading cards with real thumbnails · AA contrast (`--clay-ink` fills, `#b04228` small clay on light) · Lighthouse warm median-of-3.
4. First-person voice sweep + anti-ai-writing pass + non-commodity check.
5. Verify in `dist/`, never source greps. Commit + push = deploy; work on `main` only.

## 6a. Component fidelity — the recurring mistake (LOCKED 2026-07-20, egg-page v3)

The breeder caught v2 of the egg page shipping **homepage/comparison components** instead of the for-sale kit. Binding rules so it never repeats:

- **The for-sale cluster has its OWN kit** at `assets/1WORKING-ON/FOR-SALE-PAGES/`. Read `FOR-SALE-PAGES:components-NAMES.md` (full text of every component) + inspect the PNGs in `component-designs/` before building. NEVER import `NewsletterV2` / the comparison hero / green counter strip / comparison small-logo seam on a for-sale page.
- **Hero** = the cluster's assigned kit hero (egg page = **Split-Hero C dark charcoal card + 2×2 photo grid**; small clay eyebrow like the homepage, serif headline with clay `<em>` accent, clay pill + dark ghost CTAs, green-check trust chips). Not a light green split.
- **Counter** = for-sale **outlined stat cards** on cream (Newsreader clay numbers), NOT the green comparison strip.
- **Bird listing** = **Avail-B sticky sidebar filter** (`.availB` = `grid 200px 1fr`; browse-by rail with live counts from `clutch-inventory.json` + `$185/$350` mini; 3-col cards: category badge top-left color-keyed, green avail dot top-right, serif UPPERCASE name, clay price, full-width "Inquire about X"; JS filter toggles `.hide`). Stacks to a chip strip ≤980px.
- **FAQ** = one of the 3 kit styles (egg page = **FAQ-C dark badge-numbered** `.faqC`, doubles as anti-scam "if a seller can't answer these, walk away").
- **Newsletter** = for-sale `.fs-nl` (banner + split variants), placed **contextually** (egg page: egg-list banner after the candling/proof section, chick-alert split after egg-vs-chick) — never a NewsletterV2 top+bottom bookend.
- **Contact form** = kit two-column: dark `.form-side` panel listing EVERY reservable bird/egg/pair + price (from inventory) beside a modern form (interest select, first/last name, cell, email, delivery select incl. Midland pickup, message).
- **Video** = `.fs-video` framed component (aviary tag + caption), not a bare `<video>`.
- **Dial** must WORK: conic ring uses `--p` var updated by an IntersectionObserver scroll-spy that also highlights the active dial/rail item + updates the `x of N` counter. A static ring reads as "broken."
- **Dial COMPACT spec (LOCKED 2026-07-20, egg-page final polish — reuse on every for-sale desktop dial sidebar):** sidebar column `196px` in a `grid 196px minmax(0,1fr); gap:28px` page body; plain `#fff` card (NO gradient bg), `border-radius:16px; padding:12px 10px`, light shadow `0 3px 12px rgba(60,30,10,.05)`, `sticky top:calc(var(--hdr) + 16px)`, `max-height:calc(100vh - var(--hdr) - 32px); overflow-y:auto; scrollbar-width:thin`. Ring **64px** (inner 50px, number 15px serif, "of N" 7px). List separated from ring by a dashed top border; links `.74rem/1.25` padding `5px 7px` radius 8px with 0.15s bg/color transition; index numerals muted `#b8a294` tabular-nums (clay only on the active item); tag chips `.56rem` weight 600. Counter stat cards match: `min-height:66px; padding:10px 13px; radius:12px;` serif number `1.35rem`. The original 92px-ring / gradient-card / 222px version reads oversized next to the compact content column — never ship it.
- **Seam** = new for-sale wordmark divider from `assets/brand/NEW-FOOTER-LOGO copy.png` (→ `public/cag-fs-seam-emblem.webp`): two clay gradient rules + centered wordmark + tiny "Midland, TX" tag. NOT the comparison circular-emblem seam.
- **Mobile images** = full-bleed edge-to-edge (`width:100vw; margin-left:calc(50% - 50vw)`), with `overflow-x:clip` on the page root so no horizontal scroll. Desktop keeps the uniform 16:9 `.sec-img` box.
- **Mandatory sections** beyond TOC/KeyTakeaway/shipping: a **blog/resources "Keep reading" section** (`.read-cards`, real thumbnails cut from infographics, 2-up) picking the contextually-relevant blog/resource pages, AND a location-aware shipping block linking real `/african-grey-parrot-for-sale-<state>/` pages.
- **Every header** gets a conversational opening paragraph (long-form question / LSI). **GEO fact tables** (Markdown-style `.otA` tables — e.g. incubation metrics 99.5°F/humidity/turning + incubation-day→milestone) signal authority to answer engines.

### Meta — extended 3-part format (ALL for-sale pages, ≤280 char title)
- **Title:** `Primary Keyword | Related Conversational Query | Number + Positive Word | Brand — LSI/NLP Keywords` (extend toward 280, never past).
- **Description:** `Primary Benefit | Secondary Benefit | Trust Signal + CTA` (≤300).

### Two shipping image-gen prompts (reusable across for-sale pages)
- **Airport (Tier 1 · $185):** "Photoreal IATA-approved live-animal airline cargo crate holding a calm captive-bred African Grey, at a Delta/United cargo counter under warm terminal light; ventilated door, water cup, C.A.Gs handling label; shallow depth of field, no logos of other brands, no text overlay, 16:9."
- **Home delivery (Tier 2 · $350):** "Photoreal climate-controlled pet courier van at a suburban front door, a uniformed handler passing a soft-sided African Grey carrier + a document folder to a smiling family; golden-hour light, warm terracotta grade, no visible brand logos, no text overlay, 16:9."

## 7. Egg Rule (page 1 special mode — breeder-flagged)

`/african-grey-parrot-bird-eggs-for-sale-usa/` builds as a **truth-forward hybrid**, never a literal egg-sales page: rank for the full egg keyword universe incl. `psittacus erithacus egg`; open with the honest breeder position (why we don't ship loose fertile eggs to hobby incubators; why ~all egg listings are fraud — our own scam module says so); demonstrate real incubation/candling expertise as EEAT; convert to hatching-reservation/weaned-chick inquiries. Keeps rankings + anti-scam authority; consistent with CITES Appendix I framing and the Verified-Claim Ledger.

# Gemini Image + Infographic Prompt Pack — /african-grey-comparison/ HUB · 2026-07-12

Aggregator HUB. Visual spine = **the grey measured against the whole field + a routing/selector** motif.
Distinct treatment per slot. Comparison pages ship **no HTML/CSS infographics** — real OG photos or
Gemini images only. Reuse the rival OG photos already generated for the 5 species spokes wherever a
rival appears.

---

## Global spec (applies to every Gemini prompt)
- **Generate:** 16:9, 1600×900 px. Post: 1408×768 WebP ≤100 KB (Pillow `method=6`, q78→54 until <95 KB),
  `public/` + SEO filename. Ship `-760.webp` sibling + `srcset="/name-760.webp 760w, /name.webp 1408w"
  sizes="(max-width:900px) 92vw, 760px"`.
- **On-page:** 760px wrapper, `width="1408" height="768"`, `sec-img inf-img`, `loading="lazy"`, wrapped
  in `<a>` to the page named per slot. **Real `<table>`/matrix stays in the DOM.**
- **Palette:** Cream `#faf7f4`, Forest Green `#2D6A4F`, Clay `#e8604c`. Warm grade, never blue/clinical.
- **Text in image:** short labels + numbers only, and only figures already on the page (#1 talking,
  40–60 yrs, $1,700–$3,500, $185/$350). Never invent a stat.
- **African Grey accuracy:** silver-grey, fine scalloping, **bright red tail**, pale mask, dark beak.
  For rivals, match the spoke prompt-packs' species notes (macaw, cockatoo, amazon) — reuse those OG images.
- **NEGATIVE (append to every prompt):** `no watermarks, no logos, no brand names, no UI chrome, no
  generic green cartoon parrot, no dogs or cats, no wild-capture or jungle-trade imagery, no pet-shop
  cages, no cold blue or clinical lighting, no extra limbs or deformed beaks, no cluttered background,
  no long paragraphs of text, no misspelled words.`
- **Pipeline:** `@cag-image-pipeline` → 5-element metadata (Rule 50b — PRIMARY *"African Grey parrot
  comparison chart"* on the HERO alt ONLY; every other image a different keyword).
- **Command:** `bash scripts/generate_nb_image.sh "PROMPT" "filename.png" "1600x900"`.

---

# PART A — OG photo slots (REUSE spoke assets; the hub rarely needs new photos)
| Slot | § | Purpose | Source |
|---|---|---|---|
| HERO | 1 | Grey-vs-field motif (grey centre, rivals around) | Gemini INF-0 below, or a strong grey portrait |
| Macaw / Cockatoo / Amazon rows | 7–9 | rival + grey | **REUSE** the 5 species spokes' OG photos |
| Congo vs Timneh | 10 | both greys | REUSE congo-vs-timneh hero portraits |
| Male vs Female | 11 | pair | REUSE male-vs-female assets |
| Shipping ×2 | 18 | van + airport cargo | REUSE cluster shipping photos |
| Owner / reviews | 19 | real buyer + bird | `bottomReviews[]` real image |
| Available birds | 20 | current birds | `/available/` slugs |

**Reuse-first is the rule for the hub** — pulling the spokes' existing rival photos keeps the cluster
visually consistent and avoids regenerating birds already shot.

---

# PART B — Gemini infographic prompts (5 hub-specific slots, distinct style each)

## INF-0/HERO · §1 Grey vs the Field  →  `african-grey-vs-field-comparison-hero.png`
**Style:** **hub "spokes" motif** — the grey at centre, rival species arranged around it. **Links to:** self/top.
**Prompt:**
> Warm editorial illustration on cream `#faf7f4`: a silver-grey African Grey with a bright red tail
> centred and slightly larger, with smaller stylised silhouettes of a macaw, a cockatoo, and an Amazon
> parrot arranged in a loose semicircle around it, thin forest-green `#2D6A4F` connector lines radiating
> out (a hub-and-spoke feel), clay `#e8604c` accent on the centre grey. Balanced, uncluttered, accurate
> markings, no text labels needed. [+NEGATIVE]

## INF-1 · §4 Master Comparison Matrix  →  `african-grey-vs-parrots-comparison-matrix.png`
**Style:** **multi-column spec-sheet grid** — rows = traits, columns = species, dots/marks. **Links to:** self (§4).
**Prompt:**
> Clean data-matrix on cream `#faf7f4`: row labels "Talking", "Intelligence", "Noise", "Size",
> "Beginner fit", "Apartment fit"; column headers "African Grey", "Macaw", "Cockatoo", "Amazon",
> "Timneh". Forest-green `#2D6A4F` grid rules, clay `#e8604c` filled dots showing the African Grey
> leading on talking + intelligence, graded dots elsewhere. Spec-sheet feel, generous padding, short
> labels only. [+NEGATIVE]

## INF-2 · §6 Best Talking Parrot Ranking  →  `best-talking-parrot-ranking-grey-number-one.png`
**Style:** **horizontal ranked bar chart** — species by talking ability, grey #1. **Links to:** `/african-grey-parrot-facts/`.
**Prompt:**
> Horizontal ranked bar chart on cream `#faf7f4`: bars for "African Grey" (longest, clay `#e8604c`,
> labelled "#1"), then "Amazon", "Quaker", "Eclectus", "Budgie" in forest-green `#2D6A4F`, descending.
> Small "~1,000 words" note beside the grey bar. Clean, editorial, short labels + one number only, no
> parrot illustration needed. [+NEGATIVE]

## INF-3 · §12 Which Comparison Is Right for You? (selector)  →  `which-african-grey-comparison-selector.png`
**Style:** **decision-flow / branching signpost** — a few questions branching to outcomes. **Links to:** self (§12).
**Prompt:**
> Warm decision-flow illustration on cream: a simple branching signpost — a starting node "What matters
> most?" splitting via forest-green `#2D6A4F` lines to three clay `#e8604c` outcome chips "Talking →
> Congo", "Quieter / apartment → Timneh", "Cuddles → see Cockatoo comparison". Clean flowchart feel,
> rounded nodes, short labels only, no parrot needed. [+NEGATIVE]

## INF-4 · §13 Best Parrot by Use Case  →  `best-parrot-by-use-case-grid.png`
**Style:** **four-quadrant icon grid** — one use case per quadrant. **Links to:** `/african-grey-pros-and-cons/`.
**Prompt:**
> Four-quadrant grid on cream `#faf7f4`, forest-green `#2D6A4F` dividers: quadrants labelled "Best
> talker", "Best for apartments", "Best for families", "Best first bird", each with a small clay
> `#e8604c` line-icon (speech bubble, small home, family, seedling). Clean, balanced, editorial, short
> labels only. [+NEGATIVE]

---

## Build fallback (until images generated)
Hub is GEO-sound without images: the master matrix, per-rival metric blocks, and use-case grid all
exist as real `<table>`/text in the DOM. Ship sized placeholder slots (`.sec-img.inf-img`) that swap
1:1. REUSE the spokes' rival OG photos immediately; only INF-0/1/2/3/4 are net-new generations.

## Image-SEO reminder (Rule 50b — no two alts share a keyword)
- HERO alt = PRIMARY *"African Grey parrot comparison chart"* (only place it appears).
- INF-1 → *African Grey vs parrots matrix* · INF-2 → *best talking parrot ranking* · INF-3 → *which
  African Grey comparison* · INF-4 → *best parrot by use case* · rival OG reuses keep their spoke alts
  varied · shipping → *nationwide African Grey shipping* · owner → *C.A.Gs owner review*.

---

# PART C — Full H2 coverage via REUSE (the hub generates only INF-0…4)

**Reuse-first is the hub's rule.** Every H2 that maps to a spoke uses that spoke's *signature
infographic* as its section image — this visually ties the hub to its spokes and avoids regenerating
concepts already shot. Only INF-0…4 are net-new. Every H2 is covered:

| § | H2 | Image (reuse unless marked NEW) |
|---|---|---|
| 1 | Quick Answer / HERO | **NEW INF-0** grey-vs-field motif *(OG fallback: `assets/brand/hero-available-grey-parrots.webp`)* |
| 2 | Master matrix | **NEW INF-1** multi-species matrix |
| 3 | Best talking parrot | **NEW INF-2** ranked talking chart |
| 4 | African Grey vs Macaw | REUSE `…/GREY-vs-MACAW/african-grey-vs-macaw-side-by-side-chart.webp` |
| 5 | African Grey vs Cockatoo | REUSE `…/GREY-vs-COCKATOO/african-grey-vs-cockatoo-comparison-chart.webp` |
| 6 | African Grey vs Amazon | REUSE `…/CONGO-vs-AMAZON/african-grey-vs-amazon-parrot-comparison-chart.png.webp` |
| 7 | Congo vs Timneh | REUSE `…/CONGO-vs-TIMNEH/congo-vs-timneh-side-by-side-comparison-chart.webp` |
| 8 | Male vs Female | REUSE `…/MALE-vs-FEMALE-…/male-vs-female-african-grey-side-by-side-comparison-chart.webp` |
| 9 | Which comparison (selector) | **NEW INF-3** decision-flow selector |
| 10 | Best parrot by use case | **NEW INF-4** four-quadrant grid |
| 11 | Pros & cons in brief → spoke | REUSE `…/pros-and-cons/african-grey-pros-and-cons-balance-scale` (spoke INF-1) |
| 12 | How to choose a breeder → spoke | REUSE `…/breeders-comparison/african-grey-breeder-red-flags-vs-green-flags` (spoke INF-9) |
| 13 | What a grey costs | REUSE `…/CONGO-vs-TIMNEH/congo-vs-timneh-price-cost-breakdown-infographic.webp` |
| 14 | 40–60 year commitment | REUSE `…/pros-and-cons/african-grey-40-60-year-lifespan-timeline` (spoke INF-6) |
| 15 | Health / doc / shipping | REUSE cluster shipping photos (`petsvans5.jpeg` + ` live-animal-…-shipping.webp`) |
| 16 | Owner story / reviews | `bottomReviews[]` real buyer images |
| 17 | See available birds | real `/available/` bird photos |
| 18 | FAQ | accordion, no image (matches spokes) |
| 19 | Explore every comparison | ItemList grid of the 7 spokes' own `-card`/chart thumbnails + inquiry form |

**Note:** §11/§12/§14 reuse spoke infographics that are themselves NEW generations on their spoke pages —
so the hub build must come LAST (after breeders + pros-cons ship), which matches the build order. No
hub-only image beyond INF-0…4 needs generating.

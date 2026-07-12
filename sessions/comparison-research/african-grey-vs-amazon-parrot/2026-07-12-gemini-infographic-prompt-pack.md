# Gemini Image + Infographic Prompt Pack — /african-grey-vs-amazon-parrot/ · 2026-07-12

No `.google-key` / `GEMINI_API_KEY` was available this build session, so the page ships with the 6
real Amazon OG photos + real HTML `<table>`s standing in for the infographic slots (GEO-sound on
their own). This pack replaces every INF slot so the page matches the CvT/CvC/CvM visual standard
once you generate and drop the images. **Design brief this time: every infographic uses a DISTINCT
visual treatment** (listed per slot) so the page doesn't read as 12 identical cards — the breeder's
"design these a little bit differently" instruction.

---

## Global spec (applies to every Gemini prompt below)

- **Generate:** 16:9 landscape, 1600×900 px (Imagen native). Post: resize to **1408×768**, export
  **WebP ≤100 KB** via Pillow (`method=6`, walk quality 78→54 until <95 KB), place in `public/`
  with the SEO filename given per slot. Ship a **`-760.webp`** responsive sibling +
  `srcset="/name-760.webp 760w, /name.webp 1408w" sizes="(max-width:900px) 92vw, 760px"`.
- **On-page:** 760px wrapper, `width="1408" height="768"`, class `sec-img inf-img`,
  `loading="lazy"` (all below the LCP hero), wrapped in `<a>` linking to the page named per slot
  (breeder rule: infographics are linkable). **The real `<table>`/data stays in the DOM below the
  image in every case** — the image illustrates, never replaces, the AIO-extractable text.
- **Palette (hard rule):** Cream `#faf7f4` background, Forest Green `#2D6A4F` structure/labels,
  Clay `#e8604c` accents only. Warm color grade. Never blue/clinical.
- **Text in image:** short labels + numbers ONLY, and only the exact figures already written and
  cited on the page — never invent a stat for the image.
- **Append this NEGATIVE to every prompt:** `no watermarks, no logos, no brand names, no UI chrome,
  no other parrot species than the ones named, no generic green cartoon parrot, no dogs or cats, no
  wild-capture or jungle-trade imagery, no cages that look like a pet-shop, no cold blue or clinical
  lighting, no extra limbs or deformed beaks, no cluttered background, no long paragraphs of text,
  no misspelled words.`
- **Pipeline after generation:** `@cag-image-pipeline` (rename + WebP + placement) → image-metadata
  5-element set (filename · alt ≤190 · title · caption+CTA · 250-word description; Rule 50b — the
  PRIMARY keyword *"African Grey vs Amazon parrot"* goes on the HERO alt only, every other image
  rotates a different keyword type).
- **Command once credit is added:** `bash scripts/generate_nb_image.sh "PROMPT" "filename.png" "1600x900"`
  (reads `GEMINI_API_KEY` from gitignored `.google-key`; add via `echo "GEMINI_API_KEY=$(pbpaste)" >> .google-key`).

---

## Species accuracy — every illustration must get these exactly right

- **African Grey (Congo):** light silver-grey body with fine pale scalloping, **BRIGHT RED tail**,
  bare **white/pale facial mask**, solid **dark/black beak**, pale-yellow adult iris, ~13 in,
  400–600 g. Never a green parrot.
- **Red-Lored Amazon** (*A. autumnalis*): green body, **red forehead & lores**, lilac-blue wash on
  crown, yellow cheek patch, red wing speculum, horn beak.
- **White-Fronted Amazon** (*A. albifrons*): smallest Amazon, green body, **white forehead**, red
  eye-ring/lores, blue crown behind the white; males show red wing coverts.
- **Yellow-Shouldered Amazon** (*A. barbadensis*): green body, **yellow forehead & crown**, white
  eye-ring, **yellow bend-of-wing (shoulder)** and yellow thighs.
- **Blue-Fronted Amazon** (*A. aestiva*): green body, **blue forehead above the cere**, variable
  yellow face/crown, red-and-yellow shoulder patch.
- **Yellow-Naped Amazon** (*A. auropalliata*): mostly-green head, **yellow band across the nape**
  (back of neck), dark beak.
- **Double-Yellow-Headed Amazon** (*A. oratrix*): green body, **entire head yellow at maturity**,
  red shoulder patch, pale horn beak.

---

# PART A — OG photo slots (already on disk, no generation needed)

These H2/H3 image slots use existing real photos. Map + place; pipeline only for the 6 species
files (move from `assets/COMPARE-PAGES/CONGO-vs-AMAZON/` → SEO-renamed `public/` WebP).

| Slot | Source file | On-page role |
|---|---|---|
| §1 Hero — Grey portrait | `public/Kent-playful-male-congo-african-grey.webp` | left staggered hero portrait |
| §1 Hero — Amazon portrait | `Red-Lored Amazon2.webp` (richest set, best headshot) | right staggered hero portrait + `vs` roundel |
| §7 Red-Lored H3 | `Red-Lored Amazon1.jpg` (+ `3/4.jpg` for a 2-up if wanted) | species card (richest → leads §7) |
| §7 White-Fronted H3 | `White-fronted Amazon parrot-single.webp` (pair avail: `-pair.webp`) | species card |
| §7 Yellow-Shouldered H3 | `yellow-shoulder-amazon-single.webp` (pair: `-pair.webp`) | species card |
| §7 Blue-Fronted H3 | `blue-fronted-amazon-parrot.jpg` | species card |
| §7 Yellow-Naped H3 | `Yellow Naped Amazon -parrot.jpg` | species card |
| §7 Double-Yellow-Headed H3 | `Double-yellow-headed-amazon.webp` | species card |
| §8 Why-not-symmetric / author box | `Mark-with-our-grey-congo-parrot-pair-and-our-amazon-parrot.webp` | Mark holding our Greys + an Amazon — literally the two-genus proof shot |
| §9 Grey deep-dive | `public/Kent-playful-male-congo-african-grey.webp` (or another Congo portrait) | `.sec-img.portrait` |
| §10 Amazon deep-dive | `White-fronted Amazon parrot-pair.webp` or `yellow-shoulder-amazon-pair.webp` | `.sec-img.portrait` pair shot |
| §20 Buy-either-at-all | a candid Grey OG (reuse a warm nursery shot) | `.sec-img` |
| §23 Documentation | `public/african-grey-parrot-iata-shipping-crates.webp` or a DNA-cert flat-lay OG | `.sec-img` |
| §24 Shipping cards | `african-grey-home-delivery-pet-van.webp` + `african-grey-airport-live-animal-shipping.webp` | two photo cards |
| §25 Owner story | real buyer OG (homepage `bottomReviews[]` avatar set) | `.sec-img` |
| §27 Further reading | each blog's own `-card.webp` | 3 blog cards |

**§7 species order (breeder-approved, richest-image-first):** Red-Lored → White-Fronted →
Yellow-Shouldered → Blue-Fronted → Yellow-Naped → Double-Yellow-Headed.

**Note on square/portrait OG files:** the species JPG/WebPs are not 16:9. Add the `.portrait`
modifier (`aspect-ratio:1/1;max-width:420px;margin:auto`) and set `width`/`height` to the intrinsic
dims, or they get decapitated by the 760×400 cover crop (skill §12.3).

---

# PART B — Gemini infographic prompts (13 slots, distinct style each)

## INF-1 · §6 Corrected Side-by-Side  →  `african-grey-vs-amazon-parrot-comparison-chart.png`
**Style:** clean two-column **data-ledger card** — a printed spec sheet, thin clay rule between
columns, Grey column left / Amazon column right, a small accurate headshot atop each column.
**Links to:** `/african-grey-comparison/` (the hub).
**Prompt:**
> A warm editorial two-column comparison spec-sheet infographic on a cream `#faf7f4` background,
> forest-green `#2D6A4F` headers and a thin clay `#e8604c` divider down the centre. Left column
> headed "African Grey" with a small realistic silver-grey African Grey headshot (bright red tail
> hint, white face mask, black beak); right column headed "Amazon Parrot" with a small realistic
> green Red-Lored Amazon headshot (red forehead, horn beak). Short label rows down both columns:
> Weight · Talking · Singing · Noise · Dust · Bonding · Beginner fit · Lifespan. Only short words
> and the figures 400–600 g vs 300–700 g and 40–60 yr. Flat vector-meets-print style, generous
> whitespace, no gradients-heavy look, gentle warm paper texture.

## INF-2 · §8 Health-Documentation ROI  →  `african-grey-health-documentation-flat-lay.png`
**Style:** top-down **photographic flat-lay** of real documents (departure from flat-vector) — warm
wood/cream surface, papers fanned. **Links to:** `/dna-tested-african-grey-for-sale/`.
**Prompt:**
> A warm, top-down photographic flat-lay on a cream `#faf7f4` linen surface: a DNA-sexing
> certificate, a PBFD/Avian Polyomavirus PCR lab result sheet, a hatch certificate, a closed
> aluminium leg-band, and a CITES paperwork folder, arranged in an orderly fan. Soft natural window
> light from the left, warm color grade, forest-green folder accent, a single clay paperclip.
> Documentary product-photography feel, shallow depth of field, no readable private text — labels
> blurred, only the words "DNA · PBFD/APV PCR · Hatch Cert · CITES" faintly legible on tabs.

## INF-3 · §11 Greys Talk Better, Amazons Sing Better  →  `african-grey-talking-vs-amazon-singing.png`
**Style:** **dual-panel split with two waveforms** — left "speech" waveform (crisp, articulated),
right "song" waveform (flowing, musical). **Links to:** `/blog/african-grey-talking-ability/`.
**Prompt:**
> A split dual-panel audio infographic on cream `#faf7f4`. Left panel labelled "African Grey ·
> vocabulary, clarity, context" over a crisp articulated speech waveform in forest green `#2D6A4F`
> with a small realistic African Grey silhouette. Right panel labelled "Amazon · volume, melody,
> prosody" over a flowing musical song waveform in clay `#e8604c` with a small realistic green
> Amazon silhouette mid-song, head back. A thin vertical divider. Warm, editorial, flat style;
> short labels only; no musical notes cliché overload, no karaoke UI.

## INF-4 · §12 Noise & Apartment Living  →  `parrot-noise-level-apartment-meter.png`
**Style:** **horizontal gauge / meter strip** (a "how loud" dial), NOT a card. No fabricated
decibel numbers — qualitative bands only. **Links to:** `/african-grey-vs-cockatoo/`.
**Prompt:**
> A horizontal qualitative "noise level" gauge infographic on cream `#faf7f4`, styled like a warm
> analog VU meter. A left-to-right band from "Quietest" to "Loudest" in a green-to-clay gradient.
> A small African Grey marker sits left-of-centre labelled "least screamy — but not silent"; a small
> green Amazon marker sits far right labelled "louder, all-day, dawn & dusk". A small apartment-door
> icon near the middle. NO decibel numbers anywhere. Flat editorial style, forest-green `#2D6A4F`
> and clay `#e8604c` only, generous whitespace.

## INF-5 · §13 Dust & Dander for Allergy Households  →  `african-grey-dust-dander-air-purifier.png`
**Style:** **cutaway room cross-section** with fine powder-down particles drifting and an air
purifier — an environmental scene, not a chart. **Links to:** `/african-grey-vs-cockatoo/` (dust).
**Prompt:**
> A warm cross-section illustration of a cosy living room on cream `#faf7f4`: a realistic silver-grey
> African Grey on a perch releasing a faint haze of fine powder-down particles into the air, a HEPA
> air purifier in the corner with soft clay `#e8604c` airflow arrows pulling particles in, an open
> window. Small forest-green `#2D6A4F` labels: "powder-down feathers", "HEPA filter", "daily bath".
> A subtle warning tag "Bird Fancier's Lung — allergy households read this". Editorial flat-illustration
> style, warm light, not clinical, no visible dirt or mess, tasteful.

## INF-6 · §14 Reading a Bite  →  `parrot-body-language-bite-warning-diagram.png`
**Style:** **annotated body-language diagram** with call-out arrows to eyes/tail/feathers — a
field-guide plate. **Links to:** `/african-grey-vs-macaw/` (bite).
**Prompt:**
> A two-subject annotated body-language field-guide plate on cream `#faf7f4`. Left: a realistic
> African Grey with clay `#e8604c` call-out arrows to "eye pinning / iris flash", "raised nape",
> "tail fan" labelled "telegraphs the bite — straight-on". Right: a realistic green Amazon, arrows
> to "eye pinning", "fanned tail", "redirected lunge" labelled "harder to read — bite-and-twist".
> Forest-green `#2D6A4F` heading "Reading a bite before it lands". Clean vector field-guide style,
> thin leader lines, short labels only, no blood, no aggression gore, calm educational tone.

## INF-7 · §15 Hormonal-Maturity Timeline  →  `amazon-vs-grey-hormonal-maturity-timeline.png`
**Style:** **horizontal age-timeline ribbon** (0 → 10+ yrs) with two tracks. **Links to:**
`/african-grey-parrot-guide/`.
**Prompt:**
> A horizontal timeline-ribbon infographic on cream `#faf7f4`, age axis 0 to 10+ years left to
> right. Top track "Amazon" in clay `#e8604c` peaks with a small flare icon around 4–6 years
> labelled "hormonal surge — hardest years"; bottom track "African Grey" in forest green `#2D6A4F`
> stays flatter, small note "steadier, plucking-prone if bored". Small accurate bird icons at each
> track's start. Clean flat editorial timeline, short labels and the ages only, warm paper feel, no
> calendar clip-art.

## INF-8 · §16 Health Risks by Species  →  `african-grey-vs-amazon-health-risk-silhouettes.png`
**Style (NEW per breeder ask):** **two labelled anatomical silhouettes** with clay risk-pins on the
affected area — a "what threatens each bird" body map, unlike any other slot. **Links to:**
`/african-grey-parrot-health-guarantee/`.
**Prompt:**
> A warm medical-editorial infographic on cream `#faf7f4` showing two side-view bird silhouettes.
> Left, a silver-grey African Grey silhouette with small clay `#e8604c` pins and short labels:
> "hypocalcemia (low calcium)", "Vitamin-A / UV-B & D3", "feather-destructive behaviour", "PBFD
> susceptibility". Right, a green Amazon silhouette with pins: "obesity / fatty liver", "hormonal
> aggression", "Vitamin-A deficiency". Forest-green `#2D6A4F` heading "Health risks by species".
> Clean, calm, non-gory anatomical-diagram style, thin leader lines, short labels only, no realistic
> organs, no distressing imagery.

## INF-9 · §17 First-Year Cost of Ownership  →  `african-grey-first-year-cost-breakdown.png`
**Style:** **stacked receipt / itemised breakdown** column with a shipping-tier footer that names
the 7 metros. **Links to:** `/african-grey-parrot-price/`.
**Prompt:**
> A warm itemised "first-year cost" breakdown infographic on cream `#faf7f4`, styled like a tidy
> printed receipt. A single vertical stack of line items in forest green `#2D6A4F`: Bird · Cage ·
> Avian-vet first exam · Food & pellets · Enrichment/toys · Carrier. A clay `#e8604c` subtotal bar.
> A footer strip "Ships nationwide · $185 airport · $350 home" with seven small city tags: Houston,
> Austin, San Diego, Bay Area, Orlando, Tampa, Columbus. Only short labels and dollar figures $185
> and $350. Flat print-editorial style, warm, generous whitespace, no coins/piggy-bank clip-art.

## INF-10 · §18 Decision Scorecard  →  `african-grey-vs-amazon-decision-scorecard.png`
**Style:** **0–10 horizontal bar grid** (twin bars per trait) — a scorecard, distinct from the
gauge and the timeline. **Links to:** `/african-grey-pros-and-cons/`.
**Prompt:**
> A twin-bar 0-to-10 scorecard infographic on cream `#faf7f4`. Rows: Talking clarity · Singing ·
> Quietness · Beginner fit · Cuddliness · Bonding speed · Apartment fit. Each row has a forest-green
> `#2D6A4F` "African Grey" bar and a clay `#e8604c` "Amazon" bar with a small 0–10 scale. A small
> honest footnote tag "we don't sell Amazons — this scorecard isn't rooting for a sale". Clean flat
> editorial bar-chart style, short labels and single-digit scores only, warm, uncluttered.

## INF-11 · §21 Wild-Caught? CITES / Captive-Bred  →  `african-grey-cites-captive-bred-passport.png`
**Style:** **passport / official-stamp motif** — evokes legal provenance, unlike every other slot.
**Links to:** `/cites-african-grey-documentation/`.
**Prompt:**
> A warm official-document infographic on cream `#faf7f4` evoking a passport/certificate. A central
> panel headed "CITES Appendix I · Captive-Bred in the USA" in forest green `#2D6A4F`, a clay
> `#e8604c` embossed-style stamp reading "Captive-Bred · Legal to Own & Transfer", a small realistic
> African Grey vignette, and short line items: "Appendix I since 2017 (CoP17)", "Never wild-caught",
> "Full paperwork travels with the bird". Elegant, trustworthy, print-security aesthetic with subtle
> guilloché line texture; short labels only, no real government seals, no country flags.

## INF-12 · §22 Myth vs Reality  →  `african-grey-amazon-myth-vs-reality-cards.png`
**Style:** **torn-paper "myth" card beside a clean "reality" card** — paired cards, tactile.
**Links to:** `/african-grey-parrot-faq/`.
**Prompt:**
> A paired-card infographic on cream `#faf7f4`. Left, a slightly torn grey note labelled "MYTH" in
> muted tone: "African Greys weigh 2.5 lb / have a black belly band". Right, a crisp clay-bordered
> `#e8604c` card labelled "REALITY" in forest green `#2D6A4F`: "400–600 g · red vs maroon tail ·
> grey scalloping · iris yellows with age". A small accurate African Grey headshot bridging the two.
> Warm editorial paper-craft style, short text only, gentle drop shadow, no cartoon "myth-busted"
> stamp cliché.

## INF-13 · §24 Health, Shipping & Available Greys  →  `african-grey-nationwide-shipping-7-metro-map.png`
**Style (NEW per breeder ask):** **stylised warm US map** with 7 pinned metros + soft route lines
from Midland, TX — a shipping-reach map, not a card. Complements (does not replace) the two OG
photo cards. **Links to:** `/buy-african-grey-parrots-with-shipping/`.
**Prompt:**
> A warm stylised map of the continental United States on cream `#faf7f4`, land in soft forest-green
> `#2D6A4F` tint. A clay `#e8604c` home pin at Midland, Texas with gentle curved route lines
> radiating to seven labelled metro pins: Houston, Austin, San Diego, Bay Area, Orlando, Tampa,
> Columbus. A small legend "Airport pickup $185 · Home delivery $350 · IATA-compliant". A tiny
> realistic African Grey travel-carrier icon by the home pin. Clean flat cartographic-editorial
> style, warm palette, short labels and the two dollar figures only, no airline logos, no realistic
> satellite terrain.

---

## Build fallback (until images generated)
Ship every INF slot as the real OG photo (Part A) or a real HTML `<table>` NOW so the page is
GEO-complete; drop each Gemini WebP into the same `<a><img>` wrapper later. The `<table>` stays in
the DOM underneath in all cases. Recompress any delivered file <100 KB (skill §13.9).

## Image-SEO reminder (Rule 50b keyword spread — no two alts share a keyword)
- HERO alt = the PRIMARY term *"African Grey vs Amazon parrot"* (only place it appears).
- INF-1 → secondary *"African grey vs amazon parrot comparison"* · INF-3 → *"African grey talking vs amazon singing"*
  · INF-4 → *"quietest parrot for an apartment"* · INF-5 → *"African grey dust and dander"* · INF-9 →
  *"African grey vs amazon parrot price"* (the safe commercial variation) · INF-13 → *"African grey nationwide shipping"*.
  Rotate the rest across LSI/long-tail so the set covers a diverse spread.

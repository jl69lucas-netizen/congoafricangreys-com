# Gemini Image + Infographic Prompt Pack — /african-grey-parrot-breeders-comparison/ · 2026-07-12

Trust / breeder-selection page (Strategy B). This is **not** a species-vs-species page, so there is no
staggered two-bird hero — the visual spine is **documentation, verification, and trust**, not two
parrots side by side. Every slot uses a **DISTINCT visual treatment** (listed per slot) so the page
never reads as a stack of identical cards. Comparison pages ship **no HTML/CSS infographics** — every
slot below is a real OG photo or a Gemini image.

---

## Global spec (applies to every Gemini prompt below)

- **Generate:** 16:9 landscape, 1600×900 px (Imagen native). Post: resize to **1408×768**, export
  **WebP ≤100 KB** via Pillow (`method=6`, walk quality 78→54 until <95 KB), place in `public/` with
  the SEO filename given per slot. Ship a **`-760.webp`** responsive sibling +
  `srcset="/name-760.webp 760w, /name.webp 1408w" sizes="(max-width:900px) 92vw, 760px"`.
- **On-page:** 760px wrapper, `width="1408" height="768"`, class `sec-img inf-img`, `loading="lazy"`
  (all below the LCP hero), wrapped in `<a>` linking to the page named per slot (infographics are
  linkable). **The real `<table>`/checklist/data stays in the DOM** in every case — the image
  illustrates, never replaces, the AIO-extractable text.
- **Palette (hard rule):** Cream `#faf7f4` background, Forest Green `#2D6A4F` structure/labels, Clay
  `#e8604c` accents only. Warm color grade. Never blue/clinical.
- **Text in image:** short labels + numbers ONLY, and only figures already written + cited on the page
  (USDA, CITES, PBFD/APV, $1,700–$3,500, $185/$350, 30 breeders, 4 offline) — never invent a stat.
- **Append this NEGATIVE to every prompt:** `no watermarks, no logos, no brand names, no UI chrome, no
  generic green cartoon parrot, no wild parrot species other than African Grey where a grey is shown,
  no dogs or cats, no wild-capture or jungle-trade imagery, no cages that look like a pet-shop, no cold
  blue or clinical lighting, no extra limbs or deformed beaks, no cluttered background, no long
  paragraphs of text, no misspelled words, no real personal names or license numbers.`
- **African Grey accuracy (when a grey appears):** light silver-grey body, fine pale scalloping,
  **bright red tail**, bare pale facial mask, solid dark beak, pale-yellow adult iris. Never green.
- **Pipeline after generation:** `@cag-image-pipeline` → image-metadata 5-element set (filename · alt
  ≤190 · title · caption+CTA · 250-word description; **Rule 50b** — PRIMARY keyword *"reputable African
  Grey parrot breeder comparison"* on the HERO alt ONLY, every other image rotates a different keyword).
- **Command once credit is added:** `bash scripts/generate_nb_image.sh "PROMPT" "filename.png" "1600x900"`
  (reads `GEMINI_API_KEY` from gitignored `.google-key`).

---

# PART A — OG photo slots (real photos; reuse cluster assets or shoot)

| Slot | §  | Purpose | Preferred source |
|---|---|---|---|
| HERO | 1 | Documented-flat-lay or warm aviary scene, copy overlays LEFT | `assets/brand/` docs flat-lay / aviary |
| Direct-breeder deep dive | 7 | Real aviary / hand-raised chick with a person | existing brand aviary photo |
| Shipping ×2 | 17 | Home-delivery van + airport live-animal cargo | `african-grey-home-delivery-pet-van.webp` / `african-grey-airport-live-animal-shipping.webp` (cluster) |
| Reviews / is-legit | 18 | Real buyer + bird photo (verified) | `bottomReviews[]` real buyer image |
| Owner story | 19 | Mark & Teri in the aviary | existing brand owner photo |
| Available birds | 20 | Real current-bird photos | `/available/` slugs |

**Reuse first:** the shipping van + airport cargo + owner + aviary images already exist from
CvT/CvM/CvA/MvF — pull them before generating. Add `.portrait` + fixed `width/height` for any square file.

---

# PART B — Gemini infographic prompts (7 slots, distinct style each)

## INF-1 · §3 The Four Places People Buy a Grey  →  `where-to-buy-african-grey-four-channels.png`
**Style:** **four labelled doorway/storefront icons in a row** (a "choose your door" motif), each a
different warm-tinted card — Direct Breeder · Classified Site · Marketplace · Rescue. NOT a table.
**Links to:** `/african-grey-comparison/` (hub).
**Prompt:**
> Warm flat-illustration on cream `#faf7f4`: four evenly spaced doorway/storefront icons in a single
> row, forest-green `#2D6A4F` line work, clay `#e8604c` accents. Labels beneath each: "Direct
> licensed breeder", "Classified listing site", "Online marketplace", "Rescue / adoption". One door
> (the direct breeder) subtly highlighted with a clay glow and a small check mark. Clean, editorial,
> lots of negative space, no parrots needed. [+NEGATIVE]

## INF-2 · §4 What a Real Breeder Shows You (documentation flat-lay)  →  `african-grey-breeder-documentation-flat-lay.png`
**Style:** top-down **photographic flat-lay of real documents** on a warm wood/linen surface — a
departure from flat-vector. **Links to:** `/cites-african-grey-documentation/`.
**Prompt:**
> Top-down photographic flat-lay, warm natural light on cream linen: a small stack of official-looking
> avian paperwork fanned out — a "DNA sexing certificate", a "health certificate", a "CITES captive-bred"
> document, a hatch record card, and a closed leg-band + microchip vial. Soft shadows, forest-green and
> clay document accents, a sprig of millet for warmth. Realistic paper texture, no readable personal
> data. Editorial, trustworthy, uncluttered. [+NEGATIVE]

## INF-3 · §6 Breeder Types Side by Side (documentation × tier)  →  `african-grey-breeder-types-documentation-matrix.png`
**Style:** clean **two-axis grid / spec-sheet card** — rows = documentation items, columns = 4 breeder
tiers, check/cross marks. A printed comparison sheet. **Links to:** `/african-grey-comparison/`.
**Prompt:**
> Clean data-matrix card on cream `#faf7f4`: rows labelled "USDA license", "CITES paperwork", "DNA
> certificate", "PBFD/APV screening", "Health guarantee", "Safe payment"; four column headers "Direct
> breeder", "Classified", "Marketplace", "Rescue". Forest-green `#2D6A4F` grid rules, clay `#e8604c`
> check marks in the "Direct breeder" column, muted grey dashes elsewhere. Thin clay header underline,
> generous padding, spec-sheet feel. Short labels only. [+NEGATIVE]

## INF-4 · §8 Verified ≠ Credential-Verified  →  `classified-verified-breeder-myth-vs-reality.png`
**Style:** **paired "badge vs magnifying-glass" split** — left a shiny "Verified" web badge, right the
same badge under a magnifying glass revealing it's hollow. Tactile, myth-busting. **Links to:**
`/how-to-avoid-african-grey-parrot-scams/`.
**Prompt:**
> Two-panel warm illustration on cream: LEFT panel a glossy round "Verified breeder" web badge (clay
> ribbon, forest-green tick) as a directory would show it; RIGHT panel the same badge under a
> magnifying glass, its centre empty/hollow with a small "?" — revealing no real credential behind it.
> Forest-green line work, clay accents, editorial, no brand names on the badge. [+NEGATIVE]

## INF-5 · §11 Our 30-Breeder Audit (primary data)  →  `african-grey-breeder-audit-30-findings.png`
**Style:** **three big stat blocks with tiny supporting icons** — a "we counted" data panel, distinct
from the matrix. **Links to:** `/trusted-african-grey-parrot-breeders/`.
**Prompt:**
> Editorial data panel on cream `#faf7f4`, three large forest-green `#2D6A4F` figures in a row with
> clay `#e8604c` underlines: "30 breeders audited", "0 posted a USDA license", "4 of 11 sites offline".
> Small line-icons above each (clipboard, badge with slash, broken-link). Clean big-number typography,
> lots of negative space, one thin clay rule across the top. Short labels only, no fabricated extras.
> [+NEGATIVE]

## INF-6 · §14–15 How Much Should a Real Grey Cost? (price-as-signal)  →  `african-grey-real-price-vs-scam-price-gauge.png`
**Style:** **horizontal price gauge / dial strip** with a "danger" clay zone below the floor. A
"how-much" meter, not a card. **Links to:** `/african-grey-parrot-price/`.
**Prompt:**
> Horizontal gauge strip on cream: a price scale left-to-right from "$800" to "$3,500", a clay `#e8604c`
> shaded "too good to be true" danger zone under ~$1,500, a forest-green `#2D6A4F` "genuine range"
> band across "$1,700–$3,500", small tick labels. A single needle/marker. Clean dashboard feel, warm
> tones, short numeric labels only. [+NEGATIVE]

## INF-7 · §16–17 Verification Checklist + Safe Payment  →  `african-grey-breeder-verification-checklist.png`
**Style:** **vertical checklist ribbon** with clay tick boxes + a small "safe vs unsafe payment" footer
row. **Links to:** `/buy-african-grey-parrots-with-shipping/`.
**Prompt:**
> Warm vertical checklist illustration on cream `#faf7f4`: a ribbon of 6 clay `#e8604c` check-boxes,
> forest-green `#2D6A4F` labels "Verify USDA license", "See the specific bird on video", "Request
> documents", "Confirm captive-bred", "Use safe payment", "Search seller + reviews". A small footer row:
> green check beside "Credit card / PayPal G&S", grey cross beside "Wire / Zelle / crypto". Editorial,
> uncluttered, short labels only. [+NEGATIVE]

---

## Build fallback (until images generated)
The page is GEO-sound without the images: every INF slot has a real `<table>`, checklist, or data
block in the DOM carrying the same figures. Ship with sized placeholder slots (correct `width/height`
+ `.sec-img.inf-img` box) that swap 1:1 when the WebPs land — no layout shift. HERO + shipping + owner
+ reviews use the reused real OG photos immediately.

## Image-SEO reminder (Rule 50b — no two alts share a keyword)
- HERO alt = PRIMARY *"reputable African Grey parrot breeder comparison"* (only place it appears).
- INF-1 → *African Grey buying channels* · INF-2 → *captive-bred documentation* · INF-3 → *breeder
  credential comparison* · INF-4 → *classified verified-breeder myth* · INF-5 → *African Grey breeder
  audit data* · INF-6 → *African Grey price range* · INF-7 → *breeder verification checklist* ·
  shipping → *nationwide African Grey shipping* · reviews → *C.A.Gs buyer reviews* · owner → *Midland
  TX family aviary*.

---

# PART C — H2 coverage completion (every H2 gets a distinct image) + exact OG files

**Rule applied (breeder 2026-07-12): every H2 carries a UNIQUE backlink-magnet image.** The FAQ /
"see available birds" / "keep reading" H2s use OG cards, matching shipped spokes; every data/decision
H2 gets its own infographic. Slots added below close the gaps INF-1…7 left open.

### Exact OG assignments (pin these — no vague "brand photo")
| § | H2 | Exact file | On-page box |
|---|---|---|---|
| 1 | HERO (breeder/aviary trust, copy LEFT) | `assets/brand/hero-image-african-grey-parrot-breeder-midland-tx.webp` | `.hero-imgs` |
| 4 | What a documented direct breeder looks like | `assets/brand/certified-breeders-african-grey-near-me.jpg` | `.sec-img.inf-img`, `object-position:center 35%` |
| 7 | Is adopting/rescuing a good option (calm rehome-mood grey) | `assets/brand/hand-reared-grey african parrot.webp` | `.sec-img.inf-img` |
| 14 | Shipping — home delivery | `assets/COMPARE-PAGES/petsvans5.jpeg` (→ `african-grey-home-delivery-pet-van.webp`) | photo card |
| 14 | Shipping — airport cargo | `assets/COMPARE-PAGES/ live-animal-african-grey-parrot-shipping.webp` | photo card |
| 15 | Is C.A.Gs legit — reviews | `bottomReviews[]` real buyer images (Ida-Brim, Sandra Soliz, Lawrence Brunner from `assets/brand/Roys/`) | testimonial |
| 16 | Owner story — Mark & Teri | `assets/COMPARE-PAGES/MALE-vs-FEMALE-afrrican-grey-parrots-for-sale/Mark-with-our-grey-congo-parrot-pair-and-our-amazon-parrot.webp` | `.sec-img.inf-img`, `object-position:center 30%` |
| 17 | See a documented grey — available cards | real `/available/` bird photos | bird cards |

### Added infographics (fill the missing H2s)

## INF-8 · §6 How Facebook/Marketplace Parrot Scams Work  →  `african-grey-facebook-marketplace-scam-anatomy.png`
**Style:** **numbered "anatomy of the scam" flow** (4 downward steps), the tell circled in clay. **Links to:** `/how-to-avoid-african-grey-parrot-scams/`.
**Prompt:**
> Warm flat editorial flow on cream `#faf7f4`: four numbered steps connected top-to-bottom by a
> forest-green `#2D6A4F` dotted line — "1 Too-cheap listing", "2 Deposit by Zelle/crypto", "3 Surprise
> 'shipping insurance' fee", "4 Seller vanishes". A clay `#e8604c` warning ring around step 1's price
> tag. Small line-icons per step (tag, phone, dollar-with-warning, empty crate). No parrot needed,
> generous negative space, short labels only. [+NEGATIVE]

## INF-9 · §10 Red Flags vs Green Flags at a Glance  →  `african-grey-breeder-red-flags-vs-green-flags.png`
**Style:** **two-column ledger — clay "red flags" vs forest-green "green flags"** (the single strongest
linkable asset on the page). **Links to:** `/how-to-avoid-african-grey-parrot-scams/`.
**Prompt:**
> Two-column ledger infographic on cream `#faf7f4`, thin center rule. LEFT column header clay `#e8604c`
> "Red flags" with a small warning-triangle: rows "No USDA license", "Won't video the bird", "Wire /
> Zelle only", "Price under $1,500", "Pressure to pay fast", "No documents". RIGHT column header
> forest-green `#2D6A4F` "Green flags" with a check-shield: rows "USDA licensed", "Live video of your
> bird", "Card / PayPal G&S", "Genuine $1,700–$3,500", "Answers every question", "Full paperwork".
> Clean line-icons, spec-sheet feel, short labels only. [+NEGATIVE]

## INF-10 · §9 Questions to Ask Any African Grey Breeder  →  `questions-to-ask-african-grey-breeder.png`
**Style:** **buyer↔breeder speech-bubble Q&A card** (distinct from the checklist ribbon). **Links to:** `/trusted-african-grey-parrot-breeders/`.
**Prompt:**
> Warm conversational card on cream `#faf7f4`: a stack of alternating speech bubbles — clay `#e8604c`
> buyer bubbles asking short questions ("Can I see this bird on video?", "USDA license number?", "PBFD/
> APV screened?", "What paperwork ships with it?") and forest-green `#2D6A4F` breeder reply bubbles
> each with a small check. Friendly editorial line work, no parrot needed, short labels only. [+NEGATIVE]

## INF-11 · §19 How to Report an African Grey Parrot Scam  →  `report-african-grey-parrot-scam-where-to-go.png`
**Style:** **three-destination signpost** (recovery routes). **Links to:** `/how-to-avoid-african-grey-parrot-scams/` (external refs IC3 / USDA APHIS / state AG in the DOM list).
**Prompt:**
> Warm signpost illustration on cream `#faf7f4`: a single post with three forest-green `#2D6A4F` arrow
> boards pointing to labels "IC3 · report online fraud", "USDA APHIS · report a breeder", "State
> Attorney General". A small clay `#e8604c` shield-with-check at the base. Clean, calm, reassuring,
> short labels only, no parrot needed. [+NEGATIVE]

### H2s intentionally on OG/text only (matches shipped spokes — NOT a gap)
§11 "Never pay in advance?" → shares INF-7 payment footer + a documented-reservation line in the DOM ·
§18 FAQ → accordion, no image · §20 Keep-Reading → blog `-card.webp` thumbnails + inquiry form.

### Added-slot image-SEO (Rule 50b — unique keyword each)
INF-8 → *African Grey marketplace scam* · INF-9 → *African Grey breeder red flags* · INF-10 → *questions
to ask an African Grey breeder* · INF-11 → *report an African Grey scam*.

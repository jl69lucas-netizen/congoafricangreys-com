# Gemini Infographic Prompt Pack — /congo-vs-timneh-african-grey/ · 2026-07-04

Breeder decision 2026-07-04: **NO HTML/CSS infographics on this page.** Every H2 + important H3
gets a linkable AI-generated infographic (Gemini / Nano-Banana), each section a DIFFERENT design
style, all inside the same DESIGN.md rules. This pack replaces every INF slot in `image-plan.md`.

## Global spec (applies to every prompt below)

- **Generate:** 16:9 landscape, 1600×900 px (Imagen native). Post: resize to **1520×800**, export
  **WebP ≤100 KB** via Pillow, place in `public/` with the SEO filename given per slot.
- **On-page:** 760px wrapper, `width="760" height="400"`, `loading="lazy"` (all are below the LCP
  hero), wrapped in `<a>` linking to the deep-dive page named per slot (breeder rule: infographics
  are linkable).
- **Palette (hard rule):** Cream `#faf7f4` background, Forest Green `#2D6A4F` structure/labels,
  Clay `#e8604c` accents only. Warm color grade. Never blue/clinical.
- **Species accuracy in every illustration:** Congo = light grey body, BRIGHT RED tail, white face
  mask, dark beak. Timneh = darker charcoal body, DARK MAROON tail, horn-colored (pinkish-tan)
  upper mandible, visibly smaller. NEVER a green parrot, NEVER 🦜-style generic cartoon.
- **Text in image:** short labels + numbers ONLY, and only the exact figures given in each prompt
  (they come from price-matrix / financial-entities / the page copy). No paragraphs, no invented stats.
- **Append this NEGATIVE to every prompt:** `no watermarks, no logos, no brand names, no UI chrome,
  no other parrot species, no generic green parrot, no dogs or cats, no wild-capture or jungle-trade
  imagery, no cold blue or clinical lighting, no extra limbs or deformed beaks, no cluttered
  background, no long paragraphs of text, no misspelled words.`
- **Pipeline after generation:** `cag-image-pipeline` (rename + WebP + placement) → image-metadata
  5-element set (filename · alt ≤190 · title · caption+CTA · 250-word description).
- **Command once credit is added:** `bash scripts/generate_nb_image.sh` (reads `GEMINI_API_KEY`
  from gitignored `.google-key`; add via `echo "GEMINI_API_KEY=$(pbpaste)" >> .google-key`).

---

## P1 · S5 Key Takeaways — "8 Fast Facts" badge board
**File:** `congo-vs-timneh-key-differences-fast-facts-infographic.webp` · **Links to:** `/african-grey-parrot-guide/`
**Style:** flat vintage-badge board (merit-badge / national-park poster energy)
> Educational flat-design infographic, warm cream #faf7f4 background, styled as a board of 8 round
> vintage merit badges arranged 4×2, each badge with a forest-green #2D6A4F ring and a small flat
> illustration inside, terracotta #e8604c ribbon accents. Badges read exactly: "400–600 g Congo /
> 275–375 g Timneh" with two bird silhouettes of different sizes; "$1,500–$3,500" with a paper
> price tag; "40–60 YEARS" with an hourglass; "Maturity 2–3 yrs vs 4–6 yrs" with a small calendar;
> "Red vs Maroon tail" with two tail feathers, one bright red and one dark maroon; "One person vs
> Whole family" with one heart vs three hearts; "100% documented" with a certificate and seal;
> "$185 / $350 shipping" with a small travel crate. Clean rounded sans-serif label text, generous
> spacing, playful but precise educational-poster mood.

## P2 · S6 Side-by-Side — split ledger chart
**File:** `congo-vs-timneh-side-by-side-comparison-chart.webp` · **Links to:** `/congo-african-grey-for-sale/`
**Style:** two-column field-guide ledger (Audubon field-notes energy). NOTE: the real HTML `<table>`
stays on the page below this image (AIO/featured-snippet asset — image never replaces it).
> Flat educational field-guide comparison chart on warm cream #faf7f4, two vertical columns divided
> by a thin forest-green #2D6A4F center rule with a small terracotta "VS" roundel. Left column
> header: realistic flat illustration of a Congo African Grey (light grey body, bright red tail,
> white face mask) labeled "CONGO"; right column header: a Timneh (darker charcoal body, dark
> maroon tail, horn-colored upper beak, smaller) labeled "TIMNEH". Below each header, four aligned
> ledger rows with tiny line icons and short labels only: "400–600 g" / "275–375 g"; "Red tail" /
> "Maroon tail"; "$1,700–$3,500" / "$1,500–$1,600"; "Matures 4–6 yrs" / "Matures 2–3 yrs".
> Hand-drawn field-journal texture, warm botanical-illustration mood, precise and calm.

## P3 · S8-H3 Congo size & build — scale diagram
**File:** `congo-african-grey-size-weight-scale-infographic.webp` · **Links to:** `/congo-african-grey-for-sale/`
**Style:** museum-exhibit measurement diagram
> Educational natural-history museum diagram, cream #faf7f4 background: a single flat-illustrated
> Congo African Grey (light grey plumage, bright red tail, white face mask, dark beak) standing on
> a wooden perch beside a vertical forest-green measurement ruler marked "33 cm / 13 in", with a
> classic balance scale underneath reading "400–600 g". Fine hairline measurement arrows, small
> caption chips in terracotta #e8604c, elegant serif-style numerals, warm paper texture, calm
> scientific-poster mood, generous negative space.

## P4 · S9-H3 Timneh size — silhouette overlay
**File:** `timneh-african-grey-size-vs-congo-silhouette-chart.webp` · **Links to:** `/timneh-african-grey-for-sale/`
**Style:** layered silhouette overlay (paper-cut / shadow-theater energy)
> Paper-cut style educational infographic on warm cream #faf7f4: two overlapping bird silhouettes
> in profile facing right — a larger soft-grey Congo silhouette with a bright red tail behind, and
> a smaller dark-charcoal Timneh silhouette with a dark maroon tail and horn-colored upper beak in
> front — sharing the same perch so the size gap reads instantly. Labels "CONGO 400–600 g" in
> forest green #2D6A4F and "TIMNEH 275–375 g" in terracotta #e8604c with thin leader lines, subtle
> layered-paper shadows, "about 1/3 smaller" caption chip, quiet premium craft-paper mood.

## P5 · S10 Which Talks Better — speech-bubble timeline
**File:** `congo-vs-timneh-talking-ability-timeline-infographic.webp` · **Links to:** `/blog/african-grey-parrot-talking-ability/`
**Style:** cartoon comic-strip timeline (the breeder wants this one playful)
> Warm cartoon educational timeline on cream #faf7f4: a horizontal forest-green #2D6A4F time arrow
> labeled "6 months → 2 years", above it a charming flat-cartoon Timneh (charcoal grey, maroon
> tail, horn-colored beak) speaking EARLY on the line with several small overlapping terracotta
> speech bubbles containing simple musical notes and a tiny "hi!", and a flat-cartoon Congo (light
> grey, bright red tail) speaking LATER on the line with one large, perfectly crisp speech bubble
> containing a neat waveform — captioned chips "Earlier start" (Timneh side) and "Uncanny
> precision" (Congo side). Rounded friendly shapes, storybook warmth, no other text.

## P6 · S11 Noise & Dander — dial + dust meter
**File:** `african-grey-noise-level-dander-comparison-infographic.webp` · **Links to:** `/african-grey-parrot-care-guide/`
**Style:** retro dashboard gauges (vintage hi-fi VU-meter energy)
> Retro-instrument educational infographic on warm cream #faf7f4: a large semicircular VU-style
> volume gauge with a forest-green #2D6A4F arc and terracotta needle pointing to the LOW-MIDDLE
> zone, four small bird silhouettes placed along the arc from quiet to loud — African Grey near the
> low end, then Amazon parrot, cockatoo and macaw silhouettes toward the red-clay loud end — labels
> "African Grey" / "Amazon" / "Cockatoo" / "Macaw" only. Beside it a second smaller round meter
> showing a soft cloud of fine white powder dots above a grey feather, labeled "Powder down". Warm
> walnut-and-cream vintage dashboard mood, clean dial typography, precise and calm.

## P7 · S12 Decision Scorecard — sports scoreboard
**File:** `congo-vs-timneh-decision-scorecard-infographic.webp` · **Links to:** `/available/`
**Style:** friendly stadium scoreboard (pennant + paired-bar energy)
> Flat playful scoreboard infographic on cream #faf7f4: header with two small team pennants — a
> Congo African Grey head (light grey, white face mask) on a forest-green #2D6A4F pennant vs a
> Timneh head (darker charcoal, horn-colored upper beak) on a terracotta #e8604c pennant. Below,
> six horizontal paired-bar rows with short labels and scores exactly: "Talking precision 10 / 8",
> "Early talking 6 / 8", "Steadiness 7 / 9", "Beginner fit 7 / 9", "Apartment fit 7 / 8",
> "One-person bond 10 / 8" — green bars for Congo, clay bars for Timneh, rounded bar ends, subtle
> halftone texture, warm friendly sports-program mood, crisp readable numerals.

## P8 · S13 Lifestyle Match — household flowchart
**File:** `which-african-grey-fits-your-lifestyle-flowchart.webp` · **Links to:** `/buy-african-grey-parrot-near-me/`
**Style:** storybook board-game path (Candy-Land-meets-field-guide)
> Warm storybook board-game style decision flowchart on cream #faf7f4: a winding path of rounded
> stepping-stone nodes in forest green #2D6A4F starting from a little house icon labeled "Your
> home", branching at simple yes/no forks with tiny icons — apartment building, family of three,
> briefcase, reading chair — and ending at two illustrated destination medallions: a Congo African
> Grey (bright red tail) medallion and a Timneh (maroon tail, horn beak) medallion. Terracotta
> #e8604c path connectors, small flag labels "First bird?", "Thin walls?", "Home all day?", "Whole
> family?", soft paper texture, cheerful but tidy children's-atlas mood.

## P9 · S14 Cost — receipt & price bands
**File:** `congo-vs-timneh-price-cost-breakdown-infographic.webp` · **Links to:** `/african-grey-parrot-price/`
**Style:** ledger receipt + bracket chart (general-store paper-receipt energy)
> Flat editorial cost infographic on warm cream #faf7f4: left side, a tall illustrated paper
> receipt with a serrated edge listing exactly "Congo $1,700–$3,500" and "Timneh $1,500–$1,600"
> with a forest-green #2D6A4F stamp reading "PAPERWORK INCLUDED"; right side, two horizontal price
> bracket bars on a simple scale — a longer green bracket for Congo and a shorter terracotta
> #e8604c bracket for Timneh — plus a small footer chip "Shipping $185 airport · $350 home" with a
> tiny travel-crate icon. Warm kraft-paper accents, typewriter-style numerals, honest
> country-ledger mood, no other text.

## P10 · S15 First 30 Days — journey trail map
**File:** `african-grey-first-30-days-adjustment-timeline.webp` · **Links to:** `/african-grey-care/`
**Style:** hiking trail map with waypoints (national-park trail-guide energy)
> Trail-map style educational infographic on cream #faf7f4: a dotted terracotta #e8604c trail
> winding left to right across a softly illustrated warm living-room landscape, with four
> forest-green #2D6A4F waypoint markers labeled only "Days 1–3 Settle", "Week 1 Observe",
> "Weeks 2–3 Trust", "Day 30 Routine" — each waypoint with a tiny flat vignette: a covered travel
> crate, a bird watching from its cage, a bird stepping onto a hand, a bird relaxed on a play
> stand (grey bird, red or maroon tail visible). A small compass rose, gentle paper grain, calm
> adventure-guide mood.

## P11 · S16 Myths vs Reality — retro poster cards
**File:** `congo-vs-timneh-myths-vs-reality-cards.webp` · **Links to:** `/how-to-avoid-african-grey-parrot-scams/`
**Style:** vintage carnival "TRUE or FALSE?" poster
> Vintage educational carnival-poster infographic on warm cream #faf7f4: three upright cards in a
> row, each with an ornate thin forest-green #2D6A4F frame; each card top half shows a bold
> terracotta #e8604c banner reading "MYTH" with one short line — "Timnehs are always quieter",
> "Only Congos really talk", "Timneh = budget Grey" — and the bottom half flips to a cream panel
> with a green check seal reading "REALITY" and a tiny honest illustration: an enrichment toy, a
> Timneh with a speech bubble music note, two identical certificates. Warm letterpress texture,
> circus-poster typography kept minimal, witty but trustworthy mood.

## P12 · S17 Documentation — photoreal flat-lay (unchanged from image-plan.md)
**File:** `african-grey-cites-documentation-flatlay-760w.webp` · **Links to:** `/cites-african-grey-documentation/`
**Style:** photoreal editorial flat-lay (the ONLY photoreal slot in this pack)
> Flat-lay overhead photograph on a warm cream linen surface (#faf7f4), soft natural diffused
> daylight from upper left, gentle warm shadows. Neatly arranged paper documents representing
> captive-bred parrot ownership paperwork: a "CITES Captive-Bred Documentation" certificate, a
> "DNA Sexing Certificate", an "Avian Veterinary Health Certificate", and a "Hatch Certificate"
> with a small closed metal leg band resting on it. A single soft grey feather laid diagonally as
> the only decorative element. Muted forest-green (#2D6A4F) and terracotta-clay (#e8604c) accent
> tones on the document headers. Clean, premium, veterinary-editorial aesthetic; documents crisp
> and legible-looking but text kept generic/blurred (no real names or numbers). NEGATIVE add: no
> live birds, no parrot.

## P13 · S4 Quick Answer — choose-if signpost (optional, Recommended to include)
**File:** `congo-or-timneh-quick-answer-signpost-infographic.webp` · **Links to:** `/african-grey-comparison/`
**Style:** crossroads signpost illustration
> Flat storybook crossroads illustration on cream #faf7f4: a single wooden signpost with two
> arrow boards — the forest-green #2D6A4F arrow pointing left reads "CONGO · precision talker ·
> one-person bond" beside a tiny red tail feather; the terracotta #e8604c arrow pointing right
> reads "TIMNEH · steadier · earlier maturity" beside a tiny maroon tail feather. Soft rolling
> cream hills, one small warm sun, generous negative space, gentle picture-book mood, crisp short
> sign text only.

---

## OG (real-photo) slots — NO generation needed, breeder-supplied
| Slot | Asset (source of truth) |
|---|---|
| Hero Congo | `assets/brand/AMIE/Amie-female-congo-african-grey-ready-for-sale.webp` |
| Hero Timneh | `assets/brand/EVIE/buy-female-timneh african grey parrot.webp` |
| Breeder/trust card | `https://congoafricangreys.com/timneh-african-grey-variant.webp` (Timneh left, Congo right) |
| Congo section cards | `assets/brand/JINS-JENI/jins-jeni2.webp` + `Jins-jeni3.webp` (one on card, one at a Congo-topic section) |
| Timneh section cards | `assets/COMPARE-PAGES/timneh-vs-congo-real-photo.webp` + `Timneh-african-grey-pair-as-chicks.jpg` + `timeh-grey-baby-for-sale-fully-hand-fed-and-raised.jpg` (one on Timneh card, others at Timneh-topic sections) |
| Home-delivery card | `assets/COMPARE-PAGES/petsvans5.jpeg` |
| Airport-pickup card | `assets/COMPARE-PAGES/live-animal-african-grey-parrot-shipping.webp` |
| Blog thumbnails | existing per-post `-card.webp` heroes from the /blog/ hub |

All OG masters get the standard pipeline: SEO rename → WebP ≤100 KB → responsive `srcset` at the
displayed size (breeder rule: one size that fits all devices, never oversized on desktop or mobile).

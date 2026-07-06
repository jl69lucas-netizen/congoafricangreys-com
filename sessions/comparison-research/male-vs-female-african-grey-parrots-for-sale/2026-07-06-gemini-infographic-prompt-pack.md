# Gemini Infographic Prompt Pack — /male-vs-female-african-grey-parrots-for-sale/ · 2026-07-06

Breeder-approved outline 2026-07-06: every H2 + H3 without an OG photo gets a Gemini/Nano-Banana
infographic, each section a DIFFERENT design style, all inside DESIGN.md + IMAGE-DESIGNS.md rules.
OG photos fill ~17 slots (mapped in the outline); this pack covers the **24 infographic slots**.
Generate ALL before the page is built.

## Global spec (applies to EVERY prompt below)
- **Generate:** 16:9 landscape, 1600×900 px (Imagen native). Post: resize to displayed size, export
  **WebP ≤100 KB** (Pillow LANCZOS q82) + a `-760.webp` sibling; place in `public/` with the SEO
  filename given per slot. On-page: landscape branch (`.sec-img.landscape`, 16:9 desktop / 4:3 mobile),
  `loading="lazy"`, `srcset` per approved image spec.
- **Palette (hard rule):** Cream `#faf7f4` background · Forest Green `#2D6A4F` structure/labels ·
  Clay/terracotta `#e8604c` accents only. Warm color grade. Never blue / clinical / grey-cast.
- **Species accuracy (every illustration):** Congo = light grey body, BRIGHT RED tail, white face
  mask, dark beak, yellow adult iris. Timneh = darker charcoal body, DARK MAROON tail, horn-colored
  (pinkish-tan) upper mandible, visibly smaller. Male & female African Greys look IDENTICAL
  (monomorphic) — never draw them differently by sex. NEVER a green parrot, NEVER 🦜 cartoon.
- **Honesty rule (this page's spine):** sex is NOT a reliable behavior predictor. Any scorecard/scale
  must read ♂ ≈ ♀ (near-equal) with an "individual variation" note — never fake a lopsided ♂/♀ gap.
- **Text in image:** short labels + numbers ONLY, and only the exact figures given per prompt (from
  price-matrix / financial-entities). No paragraphs, no invented stats, no fake names.
- **Real figures allowed:** Congo $1,700–$3,500 / 400–600 g / red tail · Timneh $1,500–$1,600 /
  275–375 g / maroon tail · Shipping $185 airport · $350 home · 40–60 year lifespan · deposit $200 ·
  **males and females priced the SAME** (price = variant + age, never sex).
- **Append this NEGATIVE to every prompt:** `no watermarks, no logos, no brand names, no UI chrome,
  no other parrot species, no generic green parrot, no dogs or cats, no wild-capture or jungle-trade
  imagery, no cold blue or clinical lighting, no extra limbs or deformed beaks, no cluttered
  background, no long paragraphs of text, no misspelled words, no fake human faces.`
- **Pipeline:** `cag-image-pipeline` (rename + WebP + placement) → image-metadata 5-element set
  (filename · alt ≤190 · title · caption+CTA · 250-word description).
- **Command:** `bash scripts/generate_nb_image.sh` (reads `GEMINI_API_KEY` from `.google-key`).

---

## G1 · H2 Quick Answer — "identical twins" mirror diagram
**File:** `male-vs-female-african-grey-monomorphic-identical-infographic.webp` · **Links to:** `/dna-tested-african-grey-for-sale/`
**Style:** symmetrical mirror / "spot the difference" diagram
> Educational flat-design infographic on warm cream #faf7f4, two near-identical African Grey parrots
> (light grey body, bright red tail, white face mask, dark beak) shown in perfect mirror symmetry
> facing each other across a thin forest-green #2D6A4F vertical center line, a small terracotta
> #e8604c equals "=" symbol at the middle. Left labeled "MALE", right labeled "FEMALE", a caption
> chip reading "Monomorphic — visually identical". Clean rounded sans-serif labels, generous negative
> space, calm field-guide mood.

## G2 · H2 Comparison — balance-scale "vs" hero
**File:** `male-vs-female-african-grey-comparison-balance-infographic.webp` · **Links to:** `/african-grey-comparison/`
**Style:** vintage brass balance-scale illustration
> Flat editorial infographic on cream #faf7f4: a classic two-pan balance scale, perfectly level, an
> African Grey head (light grey, white face mask) on the left pan labeled "MALE ♂" in forest green
> #2D6A4F and an identical African Grey head on the right pan labeled "FEMALE ♀" in terracotta
> #e8604c, the balanced beam signalling "closer than you think". Small caption chip "Individual > sex".
> Warm brass-and-cream tones, precise line work, quiet premium mood.

## G3 · H3 Comparison table — field-guide ledger
**File:** `male-vs-female-african-grey-side-by-side-comparison-chart.webp` · **Links to:** `/congo-vs-timneh-african-grey/`
**Style:** two-column Audubon field-notes ledger (real HTML `<table>` still stays on the page below)
> Flat educational field-guide comparison chart on warm cream #faf7f4, two vertical columns divided
> by a thin forest-green #2D6A4F center rule with a small terracotta "VS" roundel. Left header an
> African Grey labeled "MALE", right header an identical African Grey labeled "FEMALE". Four aligned
> ledger rows with tiny line icons and short labels only: "Size — same" / "same"; "Talking — varies" /
> "varies"; "Temperament — individual" / "individual"; "Sexing — DNA only" / "DNA only". Hand-drawn
> field-journal texture, warm botanical mood, precise and calm.

## G4 · H2 Does sex predict behavior — fingerprint / individuality concept
**File:** `african-grey-personality-is-individual-not-sex-infographic.webp` · **Links to:** `/african-grey-parrot-guide/`
**Style:** conceptual fingerprint-as-identity illustration
> Warm conceptual infographic on cream #faf7f4: a single African Grey parrot (light grey, red tail,
> white face mask) at center, and behind it a large soft forest-green #2D6A4F fingerprint motif whose
> ridges subtly form the bird's silhouette, symbolising unique individual personality. Two small
> terracotta #e8604c chips read "Hand-rearing" and "Individual temperament" with tiny arrows pointing
> to the bird. Caption "Personality is individual, not male or female." Calm, thoughtful editorial mood.

## G5 · H3 Do males or females talk better — equal speech-bubble scale
**File:** `do-male-or-female-african-greys-talk-better-infographic.webp` · **Links to:** `/congo-vs-timneh-african-grey/`
**Style:** playful twin speech-bubble meter
> Warm cartoon educational infographic on cream #faf7f4: two identical flat-illustrated African Greys
> (light grey, red tail) facing forward, each with a crisp speech bubble of equal size containing a
> neat sound waveform — one labeled "MALE" in forest green #2D6A4F, one "FEMALE" in terracotta #e8604c
> — sitting on a level horizontal meter with the needle dead-center. Caption chip "Talking varies by
> bird, not by sex." Rounded friendly shapes, storybook warmth.

## G6 · H3 Male size & "squared head" debunk — caliper myth overlay
**File:** `african-grey-head-shape-sexing-myth-debunk-infographic.webp` · **Links to:** `/dna-tested-african-grey-for-sale/`
**Style:** museum caliper measurement diagram with a crossed-out folklore note
> Natural-history museum measurement diagram on cream #faf7f4: a single African Grey head (light grey,
> white face mask, dark beak) in profile with fine forest-green #2D6A4F caliper arrows around the
> crown and body, and a small terracotta #e8604c stamp reading "MYTH" over a faint dotted "squared
> head" outline with a subtle X. Caption chip "Head & body shape can't sex a Grey." Elegant hairline
> arrows, warm scientific-poster mood, generous negative space.

## G7 · H3 Female calmer/placid/independent — temperament spectrum dial
**File:** `female-african-grey-temperament-spectrum-infographic.webp` · **Links to:** `/african-grey-parrot-guide/`
**Style:** horizontal spectrum dial / slider
> Flat educational infographic on cream #faf7f4: a horizontal spectrum bar running from "Calm" to
> "Spirited" in a forest-green #2D6A4F to terracotta #e8604c gradient, with several small identical
> African Grey silhouettes scattered ALL ALONG the bar (not clustered by sex) and a soft marker band
> spanning the middle. Labels "Every hen is different" and tiny chips "placid" / "independent" /
> "spirited". Caption "Female temperament spans the whole range." Calm, precise, honest mood.

## G8 · H2 DNA sexing — helix + feather lab
**File:** `african-grey-dna-sexing-explained-infographic.webp` · **Links to:** `/dna-tested-african-grey-for-sale/`
**Style:** clean science-lab diagram
> Warm science-lab educational infographic on cream #faf7f4: a single soft grey African Grey feather
> at left, a gentle dotted terracotta #e8604c line leading to a stylised forest-green #2D6A4F DNA
> double helix at right, with a small certificate icon beneath reading "DNA SEXED". Two tiny step
> chips "1 Feather" → "2 PCR test" → "3 Certificate". Caption "Sex confirmed by DNA, not by looks."
> Clean flat vector, warm premium veterinary-editorial mood.

## G9 · H3 Why you can't sex visually — "identical" side-by-side
**File:** `why-you-cant-visually-sex-an-african-grey-infographic.webp` · **Links to:** `/dna-tested-african-grey-for-sale/`
**Style:** "spot the difference" puzzle panel
> Flat educational puzzle-style infographic on cream #faf7f4: two identical African Greys (light grey,
> bright red tail, white face mask) side by side under a header magnifying-glass icon, a forest-green
> #2D6A4F caption "Spot the difference?" and a terracotta #e8604c answer chip "There isn't one —
> they're monomorphic." Small equals "=" between them. Playful but tidy, warm field-guide mood.

## G10 · H3 Congo gender — Congo portrait + DNA tag
**File:** `how-to-determine-congo-african-grey-gender-infographic.webp` · **Links to:** `/congo-african-grey-for-sale/`
**Style:** single-subject spotlight portrait card
> Flat illustrated spotlight infographic on cream #faf7f4: one detailed Congo African Grey (light grey
> body, BRIGHT RED tail, white face mask, dark beak, yellow iris) on a wooden perch, a small
> forest-green #2D6A4F ribbon tag hanging from the perch reading "DNA SEXED", a terracotta #e8604c
> caption chip "Congo sex = DNA, not size or color." Warm portrait lighting feel, elegant negative space.

## G11 · H3 Timneh sexing — Timneh portrait + DNA tag
**File:** `male-vs-female-timneh-african-grey-difference-infographic.webp` · **Links to:** `/timneh-african-grey-for-sale/`
**Style:** single-subject spotlight portrait card (mirror of G10, Timneh)
> Flat illustrated spotlight infographic on cream #faf7f4: one detailed Timneh African Grey (darker
> charcoal body, DARK MAROON tail, horn-colored pinkish-tan upper beak, visibly smaller than a Congo)
> on a wooden perch, a terracotta #e8604c ribbon tag reading "DNA SEXED", a forest-green #2D6A4F
> caption chip "Male & female Timnehs look identical too." Warm portrait feel, calm negative space.

## G12 · H3 Decision scorecard — near-EQUAL scoreboard (honesty)
**File:** `male-vs-female-african-grey-decision-scorecard-infographic.webp` · **Links to:** `/available/`
**Style:** friendly scoreboard with deliberately near-level bars
> Flat playful scoreboard infographic on cream #faf7f4: header with two identical African Grey heads,
> one on a forest-green #2D6A4F "MALE ♂" pennant, one on a terracotta #e8604c "FEMALE ♀" pennant.
> Five horizontal paired-bar rows with short labels and NEAR-EQUAL bars: "Talking", "Temperament",
> "Noise", "Bonding", "Beginner fit" — bars within a hair of each other on every row. A bold caption
> chip "It's a near-tie — the individual bird decides." Rounded bar ends, warm sports-program mood.

## G13 · H3 First-time owner fit — beginner signpost
**File:** `male-or-female-african-grey-for-first-time-owner-infographic.webp` · **Links to:** `/buy-african-grey-parrot-near-me/`
**Style:** storybook wooden signpost
> Flat storybook crossroads illustration on cream #faf7f4: a wooden signpost with two equal arrow
> boards pointing opposite ways — forest-green #2D6A4F "MALE" and terracotta #e8604c "FEMALE" — both
> arrows the same length, and a third small hanging sign below reading "Either — pick the bird, not the
> sex." A tiny hand-raised chick icon at the base. Soft cream hills, gentle picture-book mood, crisp
> short sign text only.

## G14 · H3 Household match — icon grid
**File:** `which-african-grey-sex-fits-your-household-infographic.webp` · **Links to:** `/african-grey-parrot-guide/`
**Style:** four-quadrant household icon grid
> Flat educational 2×2 grid infographic on cream #faf7f4, thin forest-green #2D6A4F dividers, each
> quadrant a simple warm icon with a short label: an apartment building "Apartment", a family of three
> "Family", a reading chair "Senior", a briefcase "Busy pro". A small identical African Grey silhouette
> sits calmly in every quadrant, terracotta #e8604c caption chip "Fit is about your time, not the
> bird's sex." Clean rounded icons, tidy calm mood.

## G15 · H2 Cost — receipt & price bands
**File:** `male-vs-female-african-grey-cost-breakdown-infographic.webp` · **Links to:** `/african-grey-parrot-price/`
**Style:** general-store paper receipt + bracket chart
> Flat editorial cost infographic on warm cream #faf7f4: left, a tall serrated paper receipt listing
> exactly "Congo $1,700–$3,500" and "Timneh $1,500–$1,600" with a forest-green #2D6A4F stamp reading
> "SAME PRICE ♂ = ♀"; right, two horizontal price bracket bars — a longer green Congo bracket and a
> shorter terracotta #e8604c Timneh bracket — plus a footer chip "Shipping $185 airport · $350 home"
> with a tiny travel-crate icon. Warm kraft-paper accents, typewriter numerals, honest country-ledger mood.

## G16 · H3 Same price ♂=♀ — balance scale price tags
**File:** `male-female-african-grey-same-price-infographic.webp` · **Links to:** `/african-grey-parrot-price/`
**Style:** level balance scale with equal price tags
> Flat editorial infographic on cream #faf7f4: a level two-pan balance scale, a paper price tag on the
> left pan labeled "MALE ♂" in forest green #2D6A4F and an identical price tag on the right pan labeled
> "FEMALE ♀" in terracotta #e8604c, both tags the same, beam perfectly balanced. Caption chip "Sex
> never changes the price — variant and age do." Warm brass-and-cream tones, precise, trustworthy mood.

## G17 · H2 Myth vs Reality — carnival TRUE/FALSE poster
**File:** `male-vs-female-african-grey-myths-vs-reality-cards.webp` · **Links to:** `/how-to-avoid-african-grey-parrot-scams/`
**Style:** vintage carnival "MYTH / REALITY" poster
> Vintage educational carnival-poster infographic on warm cream #faf7f4: three upright cards in a row,
> each with an ornate thin forest-green #2D6A4F frame; each card's top half a bold terracotta #e8604c
> "MYTH" banner with one short line — "Males always talk better", "Females are always calmer", "You can
> tell sex by the head" — and the bottom half a cream "REALITY" panel with a green check seal and a tiny
> honest illustration: an equals sign, a level meter, a DNA feather. Warm letterpress texture, minimal
> circus typography, witty but trustworthy mood.

## G18 · H3 Myth: males talk better — myth-bust stamp
**File:** `myth-male-african-greys-talk-better-debunk-infographic.webp` · **Links to:** `/congo-vs-timneh-african-grey/`
**Style:** rubber-stamp "MYTH BUSTED" panel
> Flat editorial infographic on cream #faf7f4: a bold terracotta #e8604c circular rubber stamp reading
> "MYTH" tilted over a short forest-green #2D6A4F line "Males talk better", and beside it two identical
> African Greys with equal speech bubbles and a small caption "Both sexes can be brilliant talkers —
> or quiet." Warm ink-stamp texture, clean, honest mood.

## G19 · H2 Available birds — aviary banner
**File:** `dna-sexed-african-greys-available-now-banner-infographic.webp` · **Links to:** `/available/`
**Style:** warm editorial aviary banner (illustrated, not photoreal cards)
> Warm illustrated banner infographic on cream #faf7f4: a soft family-aviary scene with three
> identical African Greys (light grey, red tail, white face mask) perched calmly at different heights
> on natural wood branches, gentle forest-green #2D6A4F foliage framing the edges, a small terracotta
> #e8604c ribbon reading "DNA SEXED · AVAILABLE". Calm premium boutique mood, generous negative space,
> no text beyond the ribbon.

## G20 · H3 Reserve a specific bird — reservation tag
**File:** `reserve-a-specific-male-or-female-african-grey-infographic.webp` · **Links to:** `/contact-us/`
**Style:** hanging reservation ticket / luggage tag
> Flat editorial infographic on cream #faf7f4: a single warm paper reservation tag on a string,
> forest-green #2D6A4F header reading "RESERVED", a small identical African Grey silhouette stamped on
> it, a terracotta #e8604c line "Your bird, held for you", and a tiny $200 deposit chip. Clean
> kraft-paper texture, calm trustworthy mood, minimal text.

## G21 · H2 Owner reviews — warm family-aviary editorial (NO faces/text)
**File:** `real-african-grey-owner-experiences-editorial-infographic.webp` · **Links to:** `/african-grey-reviews/`
**Style:** soft editorial vignette (illustrated, faceless, warm)
> Warm illustrated editorial vignette on cream #faf7f4: a cozy home living-room scene, a single
> contented African Grey (light grey, red tail) perched on a play stand beside a soft armchair and a
> window with gentle warm light, a small forest-green #2D6A4F quote-mark motif and three tiny
> terracotta #e8604c stars in the corner. No human faces, no review text. Calm, homey, trustworthy
> magazine-feature mood.

## G22 · H2 Buy safely / scam-safe — protective shield checklist
**File:** `buy-an-african-grey-safely-checklist-infographic.webp` · **Links to:** `/how-to-avoid-african-grey-parrot-scams/`
**Style:** protective shield + tick checklist
> Flat editorial infographic on cream #faf7f4: a calm forest-green #2D6A4F shield outline at center
> with four short ticked checklist lines beside it — "DNA-sexed", "CITES papers", "Vet-checked",
> "Traceable payment" — each with a small green check. A tiny identical African Grey silhouette inside
> the shield. Terracotta #e8604c caption chip "Verify before you pay." Clean, reassuring, premium mood.

## G23 · H3 Payment red flags — caution flag panel
**File:** `african-grey-payment-red-flags-warning-infographic.webp` · **Links to:** `/how-to-avoid-african-grey-parrot-scams/`
**Style:** caution / red-flag warning panel
> Flat editorial warning infographic on cream #faf7f4: three small terracotta #e8604c warning flags in
> a row, each over a short forest-green #2D6A4F caption — "Friends & Family only", "No documentation",
> "Price too good" — and a calm green check chip below reading "Safe: traceable, documented, deposit
> receipt." Clean, honest, non-alarmist mood, warm cream tones.

## G24 · H2 Final CTA — warm invitation banner
**File:** `reserve-your-male-or-female-african-grey-cta-banner.webp` · **Links to:** `/contact-us/`
**Style:** warm closing invitation scene
> Warm illustrated closing banner on cream #faf7f4: a gentle home scene with a single hand-raised
> African Grey (light grey, bright red tail, white face mask) stepping onto an open welcoming human
> hand (no face), soft forest-green #2D6A4F foliage at the margins, one small terracotta #e8604c heart
> motif. Inviting, calm, premium family-boutique mood, no text.

---

## OG (real-photo) slots — NO generation needed, breeder-supplied (mapped in the approved outline)
| Outline slot | OG asset |
|---|---|
| H1 Hero ♂ / ♀ | `Kent-playful-male-congo-african-grey.webp` / `Evie-female-timneh-african-grey.webp` |
| H3 What differs | `male-vs-female-african-grey-chicks.webp` |
| H2 Key Takeaways | `playful-african-grey-chicks.jpg` |
| H3 Owner gender | `Mark-with-our-grey-congo-parrot-pair-and-our-amazon-parrot.webp` |
| H3 Temperament individual | `hand-raised-congo-african-grey-parrot-playing-with-our-cat.webp` |
| H2 Male deep-dive | `Kent-playful-male-congo-african-grey.webp` |
| H2 Female deep-dive | `Evie-female-timneh-african-grey.webp` |
| H3 Egg-laying | `african-grey-pair-diet-maintenance.jpg` |
| H3 DNA cert (vet) | `male-female-african-grey-parrots-for-sale-vet-checked.jpg` |
| H2 Decision scorecard (section img) | `male-female-african-grey-parrots-for-sale-companionship-choice.webp` |
| H2 Household | `male-vs-female-african-grey-inside-their-cage.webp` |
| H2 First 30 days | `male-female-african-grey-parrots-for-sale-relationship-journey.webp` |
| H2 One/pair/same-sex | `jins-jeni4-cong-african-grey-pair.webp` |
| H3 Pair learn to talk (video) | `Jins-and-jeni-male-female-congo-african-greys-for-sale.mp4` |
| H2 Documentation (video) | `rony-and-rose-with-real-paper-midland-tx.mp4` |
| H3 CITES captive-bred | `mac-letia-young-african-grey-parrot-with-midland-tx-image-real-trust.webp` |
| H2 Shipping | `affordable-african-grey-parrot-shipping.jpg.webp` |
| H3 Delivery options | `united-home-delivery-van-petsafe.webp` |
| H2 Blog cards | each post's own `-card.webp` |

All OG masters: SEO rename → WebP ≤100 KB → responsive `srcset` per the approved 2026-07-06 image spec
(portrait branch for Kent; landscape branch for the rest).

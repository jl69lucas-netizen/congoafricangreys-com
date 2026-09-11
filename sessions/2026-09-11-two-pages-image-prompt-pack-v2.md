# Image Prompt Pack v2 — Page A and Page B · 2026-09-11

> **Supersedes** `sessions/2026-08-10-two-pages-image-prompt-pack.md Part 2`.

**Why v2:** Breeder ruling 2026-09-11: all infographics are Gemini-generated, as on the comparison and for-sale pages. The 08-10 pack's blanket 'no text overlay' line is wrong for these pages; the shipped house standard (public/images/breeding-pair/inf-*.webp, congo-vs-timneh pack 2026-07-04) carries short labels and exact figures inside the art.

**Model:** `gemini-3-pro-image` · 16:9 at 2K  
**Post-processing:** resize/cover-crop to 1408x768 WebP method=6 quality walked down until <95KB, plus a -760.webp sibling at 760x415 <55KB (IMAGE-DESIGNS.md 1a)  
**Art vs HTML:** Competitor NAMES and the measurement DATE never go in the art; they render as HTML in Table H so they stay editable and date-durable. Only figures and short labels are baked.  
**Styles:** None of the 14 styles below appear in the ~40 already spent across sessions/**/*prompt-pack*.md. Page A = printed-dossier family; Page B = wayfinding family.

## Figure sources (every baked number traced)

| Figure | Source |
|---|---|
| `850` | exoticglobalparrotsfarm live listing, sprint0 2026-08-10 line 161 |
| `8500` | birdbreeders aggregator ceiling, sprint0 line 166 |
| `7500_8500_4500` | Ana's Parrots, same seller same day: own site / BirdBreeders / Hoobly, sprint0 line 171 |
| `1500_3500` | site floor Evie $1,500, ceiling bonded pair $3,500; sprint0 lines 165, 277, 308-309 |
| `weights` | Congo 400-600 g, Timneh 275-375 g — matches the shipped congo-vs-timneh pack |

> ⛔ **Never generate:** Pack Part 1 P1-P11: the six named birds, both heroes, the document flat-lay, the two newsletter images. Real birds must be real photographs.

## Global spec appended to every prompt

- **Palette:** warm cream #faf7f4 background, forest green #2D6A4F structure and labels, terracotta #e8604c accents only, warm colour grade, never blue or clinical
- **Species accuracy:** Congo African Grey = light grey body, BRIGHT RED tail, white face mask, dark hooked beak. Timneh = darker charcoal body, DARK MAROON tail, horn-coloured pinkish-tan upper mandible, visibly smaller. Never a green parrot, never a cartoon parrot stand-in.
- **Typography (infographics only):** clean rounded sans-serif, generous spacing, every word spelled correctly, labels only, no paragraphs
- **Negative:** `no watermarks, no logos, no brand names, no website names, no dates, no UI chrome, no other parrot species, no generic green parrot, no dogs or cats, no wild-capture or jungle-trade imagery, no cold blue or clinical lighting, no extra limbs or deformed beaks, no cluttered background, no long paragraphs of text, no misspelled words, no duplicated words, no nonsense lettering`

---

## Page A

### A-INF-1 · H2 2 price artifact — *step-ladder rung chart*
**File:** `buy-african-grey-price-ladder-850-to-8500-infographic.webp`  
**Alt:** `Price ladder showing African Grey listings from $850 to $8,500 with the C.A.Gs band marked`

> Flat editorial infographic, a tall vertical step-ladder standing centre-left with seven evenly spaced rungs drawn in forest green line art. Four rungs carry small terracotta price chips reading exactly, from the bottom rung upward: "$850", "$1,500", "$3,500", "$8,500". A translucent forest-green band spans the ladder between the "$1,500" and "$3,500" rungs and carries one short label reading "OUR RANGE" in cream. Generous cream whitespace to the right, flat vector, crisp edges, calm editorial poster mood.

### A-INF-2 · H2 2 H3 1 — *hub-and-spoke relay diagram*
**File:** `one-seller-three-platform-prices-infographic.webp`  
**Alt:** `One seller's African Greys listed at three different prices across three platforms`

> Flat editorial hub-and-spoke diagram. At the centre, one small forest-green aviary building icon with a single Congo African Grey perched beside it, light grey body and bright red tail. Three terracotta arrows radiate outward to three cream cards with thin forest-green borders, arranged evenly around the hub. The cards carry exactly these labels and prices: "OWN SITE / $7,500", "AGGREGATOR / $8,500", "CLASSIFIED / $4,500". Flat vector, generous spacing, precise and calm.

### A-INF-3 · H2 2 H3 2 — *exploded parts diagram*
**File:** `what-an-african-grey-price-includes-infographic.webp`  
**Alt:** `Six cost components behind an honest hand-raised African Grey price`

> Flat editorial exploded-parts diagram, the kind used in an assembly manual. Six components float apart in a neat diagonal stack, each drawn as forest-green line art on cream with thin terracotta leader lines to a short label. The six, labelled exactly: "HAND FEEDING" with a feeding syringe, "AVIAN VET" with a stethoscope, "DNA SEXING" with a small helix, "PAPERWORK" with a certificate, "CLOSED BAND" with a leg band ring, "TRAVEL CRATE" with a ventilated crate. Precise technical-illustration feel, generous whitespace.

### A-INF-4 · H2 4 — *clock-face quadrant timeline*
**File:** `first-72-hours-after-african-grey-arrives-infographic.webp`  
**Alt:** `Four steps covered by the seventy-two hour health guarantee after arrival`

> Flat editorial infographic built on one large circular clock face in forest green line art on cream, divided into four quadrants by thin terracotta rules. Each quadrant holds a small flat icon and one short label, reading exactly, clockwise from the top: "ARRIVAL" with a travel crate, "SAME-DAY CHECK" with a magnifier, "AVIAN VET" with a stethoscope, "WRITTEN OUTCOME" with a signed page. At the centre of the dial, one bold forest-green label reads "72 HOURS". Calm, precise, generous negative space.

### A-INF-5 · H2 6 — *airport departure board*
**File:** `african-grey-shipping-routes-five-states-infographic.webp`  
**Alt:** `Flight routes from Midland Texas to Iowa, Kentucky, Maryland, Tennessee and Wisconsin`

> Flat editorial infographic styled as a calm airport departure board on cream, forest-green header bar and thin rules between rows. The header reads exactly "FROM MIDLAND, TX". Five rows beneath, each with a small terracotta aeroplane glyph and one destination label, reading exactly: "IOWA", "KENTUCKY", "MARYLAND", "TENNESSEE", "WISCONSIN". No times, no flight numbers, no other columns. Flat vector, crisp type, generous row spacing.

### A-INF-6 · H2 7 — *paired identity cards*
**File:** `congo-or-timneh-identity-cards-infographic.webp`  
**Alt:** `Congo and Timneh African Grey identity cards compared side by side`

> Flat editorial infographic: two identity cards side by side on cream, each a rounded rectangle with a thin forest-green border and a small terracotta corner seal. The left card shows a precise flat illustration of a Congo African Grey, light grey body, bright red tail, white face mask, dark beak, and carries exactly the labels "CONGO" and "400-600 g" and "RED TAIL". The right card shows a Timneh African Grey, darker charcoal body, dark maroon tail, horn-coloured upper mandible, visibly smaller, with exactly the labels "TIMNEH" and "275-375 g" and "MAROON TAIL". Calm document-like precision, generous whitespace.

### A-INF-7 · H2 8 — *rubber-stamp impressions*
**File:** `five-checks-fake-african-grey-listing-infographic.webp`  
**Alt:** `Five verification checks that expose a fraudulent African Grey listing`

> Flat editorial infographic: five circular rubber-stamp impressions arranged in a row across cream paper, each a forest-green ring with a small flat icon inside and a terracotta tick mark overlapping its lower edge, with slight ink texture. One short label sits under each stamp, reading exactly: "ADDRESS", "LICENCE", "LIVE VIDEO", "DOCUMENTS", "TRACEABLE PAYMENT". Precise, calm, generous spacing, no other marks.

### A-OG-1 · H2 5 — *photoreal cargo scene* · PHOTOREAL
**File:** `african-grey-iata-cargo-crate-airport.webp`  
**Alt:** `IATA-approved travel crate with an African Grey at the airline cargo counter`

> Editorial pet photography, warm natural light, shallow depth of field, true-to-life African Grey plumage, cream and wood and forest-green palette, calm premium family-aviary mood, photorealistic, high detail on eye and feather texture. An IATA-approved wooden live-animal travel crate with a ventilated grille door and a water cup sits on a counter at an airline cargo facility under warm terminal light. Inside, one calm Congo African Grey, light grey body, bright red tail, white face mask, dark hooked beak. Background handlers are softly out of focus and unidentifiable. Every label and sticker on the crate is blank, with no lettering of any kind.

### A-OG-2 · H2 5 — *photoreal doorstep scene* · PHOTOREAL
**File:** `african-grey-home-delivery-courier-family.webp`  
**Alt:** `Courier handing an African Grey carrier and document folder to a family at their door`

> Editorial pet photography, warm golden-hour light, shallow depth of field, cream and wood and forest-green palette, calm premium mood, photorealistic. A climate-controlled pet courier van stands at a suburban front door while a uniformed handler passes a soft-sided pet carrier and a plain document folder to a welcoming family. One Congo African Grey is visible through the carrier mesh, light grey body, bright red tail, white face mask. Faces are turned or softly out of focus. The van, the uniform and the folder are completely blank, with no lettering, no badges and no logos.

## Page B

### B-INF-1 · H2 1 — *annotated result-page wireframe*
**File:** `near-me-search-result-anatomy-infographic.webp`  
**Alt:** `Near-me search results dominated by location-specific listings above national pages`

> Flat editorial wireframe diagram of a stylised search results page on cream. At the top, a rounded map-panel block filled soft forest green with three small terracotta location pins; beneath it, five stacked result rows drawn as plain bars with no readable words. The top two rows are highlighted in terracotta and marked with small numbered call-out chips reading exactly "1" and "2"; the lower three rows are pale sage and muted. One short label sits to the right of the highlighted group reading exactly "LOCAL FIRST". Flat vector, calm, generous whitespace.

### B-INF-2 · H2 3 — *concentric drive and fly rings*
**File:** `midland-pickup-radius-or-fly-infographic.webp`  
**Alt:** `Midland pickup radius and nationwide flight routes from the C.A.Gs aviary`

> Flat editorial infographic on cream: a single terracotta dot at the centre marked with one short label reading exactly "MIDLAND, TX", surrounded by three concentric rings. The innermost ring is filled soft forest green and labelled exactly "DRIVE"; the outer band is pale sage and labelled exactly "FLY", with four thin terracotta arcs curving outward past the rings toward the edges of the frame. No map outline, no state borders, no other text. Flat vector, calm radar-like geometry, generous whitespace.

### B-INF-3 · H2 5 — *price tags on a line*
**File:** `same-african-grey-three-classified-prices-infographic.webp`  
**Alt:** `The same African Grey advertised at three different prices on three classified sites`

> Flat editorial infographic on cream: three paper price tags hang side by side from a thin forest-green horizontal line, each tag a rounded rectangle with a small string loop and a terracotta edge. The three tags carry exactly these prices and nothing else: "$4,500", "$7,500", "$8,500". Below the tags, one small flat illustration of a single Congo African Grey, light grey body, bright red tail, white face mask, with a short label reading exactly "SAME BIRD". Flat vector, crisp, generous spacing.

### B-INF-4 · H2 6 — *fanned document flat-lay*
**File:** `five-documents-with-every-african-grey-infographic.webp`  
**Alt:** `The five documents that travel with every African Grey we place`

> Flat editorial infographic on cream: five document sheets fanned out like a hand of cards, each drawn in forest-green line art with a small terracotta wax seal in its corner. One short label sits on each sheet, reading exactly: "CITES", "DNA", "VET", "HATCH", "BAND". Slight overlap between sheets, soft paper shadows, flat vector, calm and precise, generous whitespace.

### B-INF-5 · H2 7 — *vertical three-step phone flow*
**File:** `if-african-grey-arrives-unwell-three-steps-infographic.webp`  
**Alt:** `Three steps to take if an African Grey arrives unwell`

> Flat editorial infographic on cream: three rounded phone-screen panels stacked vertically, each with a thin forest-green border, connected by short terracotta arrows pointing downward. Each panel holds one small flat icon and one short label, reading exactly, from top to bottom: "CALL SAME DAY" with a handset, "LOCAL AVIAN VET" with a stethoscope, "WRITTEN OUTCOME" with a signed page. Flat vector, calm, generous spacing, no other text.

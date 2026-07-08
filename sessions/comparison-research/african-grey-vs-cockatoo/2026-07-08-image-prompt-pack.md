# Image Plan + Gemini Prompt Pack — /african-grey-vs-cockatoo/ (2026-07-08)

Two image sources: **OG** = the photos you provided (`assets/COMPARE-PAGES/GREY-vs-COCKATOO/` + brand folders) · **AI** = Gemini/Nano-Banana infographics YOU generate from the prompts below (`.google-key` absent this session). §11 rule: NO HTML/CSS infographics — real photo or AI only; the real `<table>` still stays in the DOM.

## PART 1 — OG photo assignments (your provided files)

| § | Slot | Provided file → target SEO filename |
|---|------|-------------------------------------|
| 1 | Hero LEFT (Grey) | `assets/brand/Roys/Roys6.jpeg` → `congo-african-grey-vs-cockatoo-hero.webp` |
| 1 | Hero RIGHT (cockatoo) | `handheld-goffin vs african grey parrot.webp` → `goffin-cockatoo-vs-african-grey-hero.webp` |
| 9 | Cockatoo family deep dive | `Moluccan and citron crested cockatoo 1.webp` → `cockatoo-family-vs-african-grey.webp` |
| 10a | Umbrella subsection | `umbrella-cockatoo-vs-african-grey.webp` → `african-grey-vs-umbrella-cockatoo.webp` |
| 10b | Moluccan subsection | `african grey vs moluccan cockatoo.webp` → `african-grey-vs-moluccan-cockatoo.webp` |
| 10c | Goffin subsection | `goffin cockatoo vs african grey  .webp` → `african-grey-vs-goffin-cockatoo.webp` |
| 10d | Galah subsection | `african grey vs galah cockatoo (pink galah).webp` → `african-grey-vs-galah-cockatoo.webp` |
| 10e | Citron subsection | `african grey vs citron crested cockatoo.webp` → `african-grey-vs-citron-crested-cockatoo.webp` |
| 7 | Mark & Teri byline | existing `about-mark-teri-benjamin-*.webp` (brand) |
| 21 | CITES doc flat-lay | reuse `african-grey-cites-documentation-flatlay-760w.webp` (already generated for CvT) |
| 22 | Shipping ×2 | brand: `live-animal-african-grey-parrot-shipping.webp` + a pet-van/home-delivery brand photo |
| 23 | Available bird cards | live photos from `clutch-inventory.json` (Congo Bery/Amie + Timneh Elad/Evie) |
| 24 | Pair + eggs | brand pair photo + fertile-egg photo |
| 27 | Blog cards | each post's own `-card.webp` hub thumbnail |

*Spare duplicates* (`african grey vs umbrella-cockatoo .webp`, `moluccan cockatoo - african grey vs .webp`, `citron crested cockatoo vs african grey .webp`, `african-grey-vs-galah.webp`, `Moluccan and citron crested cockatoo 2.webp`) = alternates if a primary crops badly. **Hero rule:** push both birds BACK from the center VS circle (no beak/head hugging the roundel) — portrait = clip-mask + zoom/translate; landscape = object-position (the MvF Kent/Evie fix). Square/portrait OGs get the `.portrait` modifier. Every OG ships a responsive `-760.webp` + srcset.

## PART 2 — Gemini prompt pack (you generate; ~14 AI infographic slots)

### Global spec (applies to every prompt)
- Generate 16:9, 1600×900 → export WebP ≤100 KB; place in `public/` with the SEO filename given; on-page 760px wrapper, `width="760" height="400"`, `loading="lazy"`, wrapped in `<a>` to the named deep-dive page (infographics are linkable). Ship a `-760.webp` sibling + srcset.
- **Palette (hard):** Cream `#faf7f4` bg · Forest Green `#2D6A4F` structure/labels · Clay `#e8604c` accents. Warm grade, never blue/clinical.
- **Species accuracy in every illustration:** African Grey = light grey body, BRIGHT RED tail, pale face mask, dark beak (Congo). Cockatoo = WHITE/pink with a raised crest depending on species (Umbrella = all-white recurved crest; Moluccan = salmon-pink crest; Goffin = small white, short crest; Galah = pink chest + grey wings + pale-pink crest; Citron = white with ORANGE crest + orange cheek). NEVER a green parrot, NEVER 🦜 cartoon.
- **Text in image:** short labels + only the exact figures given below. No paragraphs, no invented stats.
- **Append this NEGATIVE to every prompt:** `no watermarks, no logos, no brand names, no UI chrome, no generic green parrot, no wrong species, no dogs or cats, no wild-capture or jungle-trade imagery, no cold blue or clinical lighting, no extra limbs or deformed beaks, no cluttered background, no long paragraphs, no misspelled words.`

---

**S4 · Quick-Answer signpost** — file `african-grey-vs-cockatoo-quick-answer-signpost.webp` · links `/african-grey-parrot-guide/`
> Flat editorial signpost infographic, warm cream #faf7f4. A wooden two-way signpost: one arrow labeled "CHOOSE THE GREY — talker, independent" pointing to a small light-grey red-tailed African Grey; the other "CHOOSE A COCKATOO — cuddler, needs constant contact" pointing to a small white crested cockatoo. Forest-green #2D6A4F posts, clay #e8604c arrow tips. Clean rounded sans-serif.

**S5 · 8 Fast Facts badge board** — file `african-grey-vs-cockatoo-fast-facts.webp` · links `/african-grey-parrot-guide/`
> Board of 8 round vintage merit badges 4×2, forest-green #2D6A4F rings, clay #e8604c ribbons, cream bg. Badges read exactly: "Grey: 200–1,000+ words"; "Cockatoo: a few words"; "Grey 400–600 g"; "Cockatoo 300–1,100 g"; "Both 40–80 yr"; "Both powder-down"; "Grey = independent / Cockatoo = velcro"; "100% CITES documented". Small flat icon in each.

**S6 · 12-point side-by-side ledger** — file `african-grey-vs-cockatoo-comparison-chart.webp` · links `/congo-african-grey-for-sale/`
> Two-column field-guide ledger, cream bg, thin forest-green center rule with a clay "VS" roundel. Left header: light-grey red-tailed African Grey labeled "AFRICAN GREY"; right: white crested cockatoo labeled "COCKATOO". Aligned rows, short labels only: "Talking: Exceptional / Limited"; "Noise: Moderate / Very loud"; "Affection: Independent / Velcro"; "Dander: High / Very high"; "Lifespan: 40–60 / 40–80 yr".

**S8 · Grey size/weight** — file `african-grey-size-weight-vs-cockatoo.webp` · links `/congo-african-grey-for-sale/`
> Flat size-comparison silhouette chart, cream bg, forest-green scale. A Congo African Grey silhouette (light grey, red tail) at 13 in / 400–600 g beside cockatoo silhouettes: Goffin ~12 in, Galah ~14 in, Umbrella ~18 in, Moluccan ~20 in. Clay height markers, short labels only.

**S9 · Cockatoo family overview** *(optional — OG `cockatoo-family-vs-african-grey.webp` may cover this; generate only if a clean illustration is preferred)* — file `cockatoo-family-traits-infographic.webp` · links `/african-grey-vs-cockatoo/`
> Flat trait board of five white/pink crested cockatoos (Umbrella, Moluccan, Goffin, Galah, Citron), each with a one-word trait label ("Loudest", "Neediest", "Playful", "Calmest", "Showy"), cream bg, forest-green frame, clay accents. Species-accurate crests/colors.

**S11 · Talking ability** — file `african-grey-vs-cockatoo-talking-ability.webp` · links `/african-grey-parrot-guide/`
> Flat horizontal bar infographic "Who Talks Better?", cream bg. Two bars: African Grey filled ~95% clay, labeled "200–1,000+ words, clear mimicry"; Cockatoo ~25%, labeled "a few words, less clarity". Small grey and white cockatoo icons. Forest-green axis.

**S12 · Noise meter** — file `african-grey-vs-cockatoo-noise-meter.webp` · links `/african-grey-parrot-care-guide/`
> Flat semicircular decibel gauge, cream bg, needle graphics. African Grey needle at "Moderate"; Moluccan cockatoo needle in the red "Very loud — among the loudest birds" zone. Forest-green dial, clay needles, short labels only.

**S13 · Powder down & allergies** — file `african-grey-vs-cockatoo-dander-allergy.webp` · links `/african-grey-parrot-care-guide/`
> Flat honest infographic "Both Are Powder-Down Birds", cream bg. Two feather-dust icons: African Grey "High dander"; Cockatoo "Very high dander". A small line-icon of an air purifier + lungs. Forest-green labels, clay highlight on "Both". Honest tone, no claim that the grey is allergy-free.

**S14 · Bite force & safety** — file `african-grey-vs-cockatoo-bite-force-safety.webp` · links `/african-grey-parrot-care-guide/`
> Flat risk-matrix infographic, cream bg. African Grey "61–96 N (70–220 PSI) ≈ snap a wooden popsicle stick" with a popsicle-stick icon; large cockatoo shown higher with a "supervise around children" note. Forest-green frame, clay danger markers, short labels only.

**S15 · Decision scorecard** — file `african-grey-vs-cockatoo-decision-scorecard.webp` · links `/african-grey-comparison/`
> Flat 0–10 dot-scale scorecard, cream bg, two columns (Grey / Cockatoo). Seven trait rows with filled clay dots: Talking, Independence, Cuddliness, Quietness, Beginner-friendliness, Low-mess, Apartment-fit. Forest-green row labels, honest near-equal where true.

**S16 · Lifestyle flowchart** — file `which-parrot-fits-you-flowchart.webp` · links `/buy-african-grey-parrot-near-me/`
> Flat decision-tree flowchart "Which Parrot Fits You?", cream bg, forest-green nodes, clay arrows. Branches: "Work full-time?" → "Want a talker?" → "Noise-sensitive/apartment?" → end nodes "African Grey" or "Reconsider a cockatoo". Short node text only.

**S17 · Cost of ownership** — file `african-grey-vs-cockatoo-cost-breakdown.webp` · links `/african-grey-parrot-price/`
> Flat first-year cost bar chart, cream bg, forest-green bars, clay total. Rows: "Bird $1,700–$3,500"; "Cage & setup"; "Food/yr"; "Avian vet/yr"; "Enrichment". Short labels + only these figures.

**S18 · First 30 days timeline** — file `african-grey-first-30-days-timeline.webp` · links `/african-grey-parrot-care-guide/`
> Flat 4-phase horizontal timeline, cream bg. Phases: "Days 1–3 Settle", "Days 4–10 Routine", "Days 11–20 Trust", "Days 21–30 Bond". Forest-green track, clay phase dots, small grey-parrot icon.

**S19 · Myths vs Reality cards** — file `african-grey-vs-cockatoo-myths-reality.webp` · links `/african-grey-parrot-guide/`
> Flat two-column myth/reality card set, cream bg. Left clay "MYTH", right forest-green "REALITY". Rows: "Cockatoos are just cuddly / They need constant contact or self-mutilate"; "Greys are allergy-safe / Greys are powder-down birds too"; "Greys are cold / They bond deeply, on their terms".

**S20 · Lifespan & succession** — file `african-grey-cockatoo-lifespan-succession.webp` · links `/african-grey-parrot-lifespan/`
> Flat lifespan timeline, cream bg, forest-green 0–80 yr axis. Grey bar 40–60 yr, cockatoo bar 40–80 yr, with a small "plan a caretaker" flag near the far end. Clay markers, short labels only.

---

## Image SEO 5-element (every image, at build)
filename (above) · alt ≤190 · title · caption+CTA · 250-word description (via image-metadata pipeline). All lazy + explicit width/height + `-760` responsive sibling.

## Net Gemini requirement: ~14 infographics (S4, S5, S6, S8, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20) + optional S9. All 5 species subsections + hero + trust + shipping + bird/pair/egg + blog are covered by your OG photos.

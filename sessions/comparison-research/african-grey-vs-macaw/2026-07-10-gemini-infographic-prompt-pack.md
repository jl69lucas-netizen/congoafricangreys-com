# Gemini Infographic Prompt Pack — /african-grey-vs-macaw/ · 2026-07-10

No `.google-key` / `GEMINI_API_KEY` was available this build session, so the page shipped with real
photos + real HTML `<table>`s standing in for these slots (GEO-sound on its own, but thinner than
the CvT/cockatoo visual standard). This pack replaces every INF slot so the page matches that
standard once you generate and drop the images — same protocol as the other two comparison pages.

## Global spec (applies to every prompt below)

- **Generate:** 16:9 landscape, 1600×900 px (Imagen native). Post: resize to **1408×768**, export
  **WebP ≤100 KB** via Pillow, place in `public/` with the SEO filename given per slot. Ship a
  **`-760.webp`** responsive sibling + `srcset="/name-760.webp 760w, /name.webp 1408w"`.
- **On-page:** 760px wrapper, `width="1408" height="768"` (or the `-760` intrinsic size), class
  `sec-img inf-img`, `loading="lazy"` (all below the LCP hero), wrapped in `<a>` linking to the
  page named per slot (breeder rule: infographics are linkable). The real `<table>` or data stays
  in the DOM below the image in every case — the image never replaces it, only illustrates it.
- **Palette (hard rule):** Cream `#faf7f4` background, Forest Green `#2D6A4F` structure/labels,
  Clay `#e8604c` accents only. Warm color grade. Never blue/clinical.
- **Text in image:** short labels + numbers ONLY, and only the exact figures given in each prompt
  (they come straight from the page copy — never invent a new stat for the image that isn't
  already written and cited on the page).
- **Append this NEGATIVE to every prompt:** `no watermarks, no logos, no brand names, no UI chrome,
  no other parrot species than the ones named, no generic green parrot, no dogs or cats, no
  wild-capture or jungle-trade imagery, no cold blue or clinical lighting, no extra limbs or
  deformed beaks, no cluttered background, no long paragraphs of text, no misspelled words.`
- **Pipeline after generation:** `cag-image-pipeline` (rename + WebP + placement) → image-metadata
  5-element set (filename · alt ≤190 · title · caption+CTA · 250-word description).
- **Command once credit is added:** `bash scripts/generate_nb_image.sh "PROMPT" "filename.png"
  "1600x900"` (reads `GEMINI_API_KEY` from gitignored `.google-key`; add via
  `echo "GEMINI_API_KEY=$(pbpaste)" >> .google-key`).

### Species accuracy — every illustration must get these exactly right

- **African Grey (Congo):** light silver-grey body, BRIGHT RED tail, white/pale face mask, solid
  dark/black beak, ~13 in.
- **Scarlet Macaw:** vivid red body, blue-and-yellow wing band, bare white face, black-and-horn
  upper beak.
- **Blue-and-Gold Macaw:** cobalt-blue back/wings, golden-yellow chest and belly, green forehead
  patch, black chin stripe.
- **Green-winged Macaw:** deep crimson-red body, green wing band, blue flight feathers, red-and-
  white fine-lined bare face.
- **Hyacinth Macaw:** solid deep cobalt-blue all over, bright yellow bare eye-ring and chin patch,
  large black beak, no red anywhere.
- **Military Macaw:** olive/moss-green body, small red forehead patch, blue flight/tail feathers,
  pale bare face with fine dark feather lines.
- **Severe Macaw:** green body, maroon-brown forehead, small blue crown patch, notably small/compact.
- **Hahn's Macaw:** green body, red "shoulder" patch on the leading wing edge, smallest macaw size,
  dark beak.
- **Camelot Macaw (hybrid):** Scarlet-dominant fiery orange-red body with blue wing-tip feathers.
- **Catalina Macaw (hybrid):** patchwork mix of blue, gold, orange and red — no two individuals
  identical; keep it visibly mixed, not solid-colored.
- **Ruby Macaw (hybrid):** deep ruby-red body with green-winged-line blue wing feathers.
- **Mini Macaw (generic):** render as a Hahn's-type small green macaw with a red shoulder patch
  when a generic "mini macaw" stand-in is needed.

NEVER a generic cartoon green parrot, NEVER a 🦜-style emoji bird, NEVER swap two species' colors.

---

## PART 1 — OG (real-photo) slots already placed — NO generation needed

| Slot | Asset already on the page |
|---|---|
| Hero LEFT (Grey) | `congo-african-grey-red-tail-comparison-hero.webp` (existing site asset) |
| Hero RIGHT (Macaw) | `african-grey-vs-blue-and-gold-macaw-comparison.webp` |
| 11 species subsections | `african-grey-vs-{scarlet,blue-and-gold,green-winged,hyacinth,military,severe,hahns,mini,camelot,catalina,ruby}-macaw-comparison.webp` |
| Deep-dive Grey portrait | `bery-congo-african-grey-female-1-year.webp` |
| Deep-dive Macaw (general) | `macaw-family-general-comparison.webp` |
| Trust/author card | `african-grey-parrot-breeder-midland-tx-hero.webp` (existing) |
| CITES section | `Mark-with-our-grey-congo-parrot-pair-and-our-amazon-parrot.webp` (existing) |
| Shipping ×2 | `african-grey-airport-live-animal-shipping.webp` + `african-grey-home-delivery-pet-van.webp` (existing) |
| First 30 days | `amie-congo-african-grey-handfed-baby-card.webp` (existing) |
| Available bird cards | live photos from `clutch-inventory.json` |
| Blog cards | each post's own `-card.webp` hub thumbnail |
| CITES documentation flat-lay | **reuse** `african-grey-cites-documentation-flatlay-760w.webp`, already generated for congo-vs-timneh — no new generation needed |

All 12 species/hero photos above are already SEO-renamed, WebP-converted and live on the page from
this build.

## PART 2 — Gemini prompt pack (you generate; 15 AI infographic slots, 1 optional)

**S4 · Quick Answer signpost** — file `african-grey-vs-macaw-quick-answer-signpost.webp` · links `/african-grey-comparison/`
> Flat storybook crossroads illustration on cream #faf7f4. A wooden two-way signpost: the
> forest-green #2D6A4F arrow pointing left reads "CHOOSE THE GREY — talker, quiet, apartment-fit"
> beside a small African Grey (light grey, red tail); the clay #e8604c arrow pointing right reads
> "CHOOSE A MACAW — bold, loud, needs space" beside a Blue-and-Gold Macaw (cobalt-blue and yellow).
> Soft rolling cream hills, generous negative space, gentle picture-book mood, crisp short sign
> text only.

**S5 · Key Takeaways — 8 fast-facts badge board** — file `african-grey-vs-macaw-fast-facts-infographic.webp` · links `/african-grey-parrot-guide/`
> Flat vintage merit-badge board, 8 round badges arranged 4×2 on cream #faf7f4, forest-green
> #2D6A4F rings, clay #e8604c ribbon accents. Badges read exactly: "540 N Hyacinth bite vs 61–96 N
> Grey" with two beak icons of different sizes; "100+ dB macaw scream" with a sound-wave icon;
> "11 macaw species compared" with a small feather fan; "40–80 yrs either bird" with an hourglass;
> "1/3 the size — Grey vs Blue-and-Gold" with two bird silhouettes; "$200–$300/mo toy budget" with
> a chewed-toy icon; "100% CITES documented" with a certificate seal; "$185/$350 shipping" with a
> travel-crate icon. Clean rounded sans-serif labels, playful but precise educational-poster mood.

**S6 · Side-by-side comparison chart** — file `african-grey-vs-macaw-side-by-side-chart.webp` · links `/congo-african-grey-for-sale/`
> Flat field-guide ledger chart, cream #faf7f4 bg, thin forest-green center rule with a clay "VS"
> roundel. Left column header: a light-grey red-tailed African Grey labeled "AFRICAN GREY"; right
> header: a Blue-and-Gold Macaw labeled "MACAW". Aligned rows, short labels only: "61–96 N bite /
> up to 540 N (Hyacinth)"; "Moderate noise / Very loud"; "200–1,000+ words / Fair at best";
> "Apartment-plausible / Needs a bird room". Hand-drawn field-journal texture, calm botanical mood.

**S8 · Grey size, in context** — file `african-grey-size-in-macaw-context.webp` · links `/congo-african-grey-for-sale/`
> Flat museum-exhibit size-scale diagram, cream #faf7f4 bg. A Congo African Grey (light grey, red
> tail) standing beside a forest-green vertical ruler marked "12–14 in / 400–600 g", with three
> small macaw silhouettes at increasing height behind it labeled only "Hahn's 130 g", "Blue-and-Gold
> 1,100 g", "Hyacinth 1,700 g". Fine hairline measurement arrows, clay caption chips, warm
> scientific-poster mood.

**S-size · Which Is Bigger — full size ladder** — file `african-grey-vs-macaw-size-ladder-infographic.webp` · links `#species` (in-page anchor)
> Flat ascending bar-ladder chart on cream #faf7f4, forest-green baseline. Seven rungs left to
> right by weight, each with a tiny accurate silhouette: "Hahn's 130–170 g", "Severe 350–450 g",
> "African Grey 400–600 g" (highlighted in a clay outline box to anchor the comparison), "Scarlet
> 900–1,100 g", "Blue-and-Gold 900–1,300 g", "Green-winged 1,000–1,700 g", "Hyacinth up to 1,700 g".
> Clean tabular-numeral labels, no other text.

**S-talking · Talking ability bars** — file `african-grey-vs-macaw-talking-ability.webp` · links `/blog/african-grey-parrot-talking-ability/`
> Flat horizontal bar chart "Who Talks Better?", cream #faf7f4 bg. One long clay-filled bar ~95%
> labeled "African Grey — 200 to 1,000+ words, near-human clarity"; a short bar ~25% labeled
> "Macaw — a few words, less precise" with three small macaw head icons (Scarlet, Blue-and-Gold,
> Military) beside it since talking varies most among those three. Forest-green axis, no other text.

**S-bite-force · Bite Force Matrix** — file `african-grey-vs-macaw-bite-force-matrix.webp` · links `#bite-force` (in-page anchor)
> Flat risk-comparison infographic, cream #faf7f4 bg, the page's single most important graphic.
> Three horizontal bars on one scale: "African Grey 61–96 N" (short, forest-green, a popsicle-stick
> icon snapping); "Human molar bite ~300–500 N" (medium, neutral grey, a tooth icon); "Hyacinth
> Macaw ~540 N (measured)" (longest, clay #e8604c, a walnut-cracking-in-pliers icon). Small caption
> "Highest bite force ever recorded in a bird — Harrison et al., 2025" in small type at the bottom.
> Forest-green frame, no other text, clinically precise but warm-toned mood.

**S-noise · Noise meter** — file `african-grey-vs-macaw-noise-meter.webp` · links `/african-grey-parrot-care-guide/`
> Flat semicircular decibel gauge, cream #faf7f4 bg. Needle graphics: African Grey needle in the
> "Moderate" green zone; Blue-and-Gold Macaw needle in the red "100+ dB — chainsaw range" zone at
> the far end. A small chainsaw icon at the red zone for scale. Forest-green dial, clay needles,
> short labels only.

**S-dander · Dander & allergies (honest reversal)** — file `african-grey-vs-macaw-dander-allergy.webp` · links `/african-grey-parrot-care-guide/`
> Flat honest infographic "Not a Powder-Down Bird", cream #faf7f4 bg. Two feather-dust icons side
> by side: African Grey with a heavier dust cloud labeled "Powder-down — higher dander"; a Macaw
> silhouette with a much lighter dust cloud labeled "No true powder down — generally less dander".
> This is the ONE section where the macaw wins — do not default to the cockatoo-page framing where
> the macaw/cockatoo is the dustier bird. Forest-green labels, clay highlight on "less dander",
> honest tone.

**S-nutrition · Diet Differences (new section, no sibling precedent)** — file `african-grey-vs-macaw-nutrition-comparison.webp` · links `#nutrition` (in-page anchor)
> Flat split nutrition-plate infographic, cream #faf7f4 bg, divided down the middle by a thin
> forest-green rule. Left plate: African Grey icon above a small illustrated pile of leafy greens,
> pellets and a sun/UV ray icon, labeled "Calcium + UV-B light". Right plate: a Blue-and-Gold Macaw
> icon above an illustrated Brazil nut and macadamia nut, labeled "Higher fat — Brazil nuts,
> macadamias". Small footer chip "$200–300/mo toy budget — that beak needs the fat" with a chewed-
> wood icon. Clay accents, warm kitchen-poster mood.

**S-scorecard · Decision Scorecard** — file `african-grey-vs-macaw-decision-scorecard.webp` · links `/african-grey-comparison/`
> Flat 0–10 dot-scale scorecard, cream #faf7f4 bg, two columns (Grey / Macaw). Seven trait rows
> with filled clay dots, exact scores: "Talking & mimicry 10/4", "Apartment/noise fit 9/2", "Visual
> drama 4/10", "Beginner suitability 6/3", "Space efficiency 9/3", "Physical safety margin 8/4",
> "Independent play 8/6". Forest-green row labels, honest — macaw wins visual drama outright,
> shown clearly.

**S-household · Lifestyle flowchart / quiz visual** — file `african-grey-vs-macaw-lifestyle-flowchart.webp` · links `#household` (in-page anchor)
> Flat decision-tree flowchart "Which Parrot Fits You?", cream #faf7f4 bg, forest-green nodes, clay
> arrows. Branches from a house icon: "Apartment or house?" → "Talker or spectacle?" → "Noise
> tolerance?" → two end medallions: "African Grey" (light-grey bird icon) or "Macaw — pick a
> species" (Blue-and-Gold icon). Short node text only, matches the on-page interactive quiz's four
> questions.

**S-cost · Cost of Ownership** — file `african-grey-vs-macaw-cost-breakdown.webp` · links `/african-grey-parrot-price/`
> Flat first-year cost bar chart, cream #faf7f4 bg, forest-green bars for Grey, clay bars for
> "typical large macaw" clearly labeled as a general market figure, not a C.A.Gs price. Rows:
> "Bird: $1,700–$3,500 (Grey, our price) / macaw varies widely by species"; "Cage & setup"; "Food/
> yr"; "Avian vet/yr"; "Toy replacement/yr — macaw bar visibly taller". Short labels + only the
> figures already written on the page.

**S-myths · Myths vs Reality cards** — file `african-grey-vs-macaw-myths-reality.webp` · links `/african-grey-parrot-guide/`
> Flat two-column myth/reality card set, cream #faf7f4 bg. Left clay "MYTH", right forest-green
> "REALITY". Rows: "All macaws are equally loud / A Hahn's and a Blue-and-Gold are worlds apart";
> "A cuddly macaw is low-maintenance / The cuddling comes with screaming and chewing attached";
> "Macaws are friendlier, Greys are cold / Greys bond just as deep, just more quietly".

**S-succession · Lifespan & Succession** — file `african-grey-macaw-lifespan-succession.webp` · links `/african-grey-parrot-lifespan/`
> Flat lifespan timeline, cream #faf7f4 bg, forest-green 0–80-year axis. Grey bar spans 40–60 yr,
> macaw bar spans 40–80 yr (visibly longer, reaching further right), with a small "name a
> caretaker" flag icon near the far end of both bars. Clay markers, short labels only.

**S7 · Species-at-a-glance board (OPTIONAL)** — file `african-grey-vs-11-macaw-species-board.webp` · links `#species` (in-page anchor)
> Optional overview graphic — the 11 real species photos already on the page may make this
> redundant; generate only if a single-glance summary graphic is wanted above the photo grid. Flat
> grid board, cream #faf7f4 bg, forest-green frame, 11 small accurate silhouettes (Scarlet,
> Blue-and-Gold, Green-winged, Hyacinth, Military, Severe, Hahn's, Mini, Camelot, Catalina, Ruby)
> arranged by size with one-word trait labels each, an African Grey silhouette centered at the
> bottom for scale reference. Species-accuracy rules above apply to every silhouette.

---

## Image SEO 5-element (every image, at build)
filename (above) · alt ≤190 · title · caption+CTA · 250-word description (via image-metadata
pipeline). All lazy + explicit width/height + `-760` responsive sibling.

## Net Gemini requirement: 15 infographics (S4, S5, S6, S8, size-ladder, talking, bite-force,
noise, dander, nutrition, scorecard, household, cost, myths, succession) + 1 optional (S7 species
board). All 11 species subsections + hero + trust + shipping + bird/pair/eggs + blog + CITES
flat-lay are already covered by real photos/reuse — no generation needed for those.

## Handoff — what happens after you generate these
Drop the finished WebP files into `assets/COMPARE-PAGES/GREY-vs-MACAW/` (or straight into `public/`
with the SEO filenames above) and say so — I'll run the image pipeline, insert each one at its
named anchor in `src/pages/african-grey-vs-macaw/index.astro` (supplementing, not replacing, the
real `<table>`/data already there), rebuild, and re-verify the pass gates before pushing.

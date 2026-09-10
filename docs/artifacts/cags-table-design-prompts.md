# C.A.Gs Homepage Tables — Claude Design Prompt Pack

Four prompts, one per homepage table. Each produces **4 style directions x 3 viewports = 12 artboards**.
Across all four runs: **16 designs, 48 artboards.**

## How to run this

**Run the four prompts separately — one per table (Recommended).**

Each prompt below is complete on its own: brand colours, sizes, rules and the table's exact text are
all inside it. Paste one, get 12 artboards, then start a fresh Claude Design run for the next table.

**Why separate runs rather than one:** 48 artboards in a single run is where canvas builds start
dropping detail and truncating late artboards — the last table would come back worse than the first.
Separate runs also mean that if Table 3 comes back wrong, you re-run Table 3 alone instead of
regenerating all sixteen designs. **The trade-off:** the four runs will not share a house style
unless you pick the same letter across all four tables, so compare the letters before you commit.

The preamble repeats inside every prompt. That is deliberate — it makes each one a single paste.

**Bring back to me for the build:** the canvas link plus your pick per table, written as
`Table 1c, Table 2a, Table 3c, Table 4b`. If you edited an artboard inside Claude Design, say so —
I build from what is on the canvas, not from the original prompt.

## The four style directions

Every table uses the same four, so `a` means the same thing on Table 1 as on Table 4 and you can
compare like with like.

| | Direction | What it is |
|---|---|---|
| **a** | Elevated Cards | Soft-shadowed rounded panels, generous padding, column headers as floating chips. Modern product-pricing feel. |
| **b** | Editorial Rule | Type-led and near-boxless. Large Newsreader display, thin forest hairlines, wide whitespace, small-caps labels. |
| **c** | Dark Panel | The table sits on a deep forest ground with cream text and mint values, one column or row lifted. Premium, high contrast. |
| **d** | Split Feature | Asymmetric. A lead summary panel beside the data; on mobile the summary becomes a strip across the top. |

## Prompt — Table 1 (Congo vs Timneh)

```
You are designing a comparison-table component for CongoAfricanGreys.com (C.A.Gs), a family
breeder of captive-bred Congo and Timneh African Greys in Midland, Texas since 2014.

Produce a design canvas with 12 artboards: 4 style directions x 3 viewports.

VIEWPORT WIDTHS — exact, do not vary:
  Mobile   390px wide
  Tablet   768px wide
  Desktop  1440px wide

ARTBOARD NAMES — use exactly these twelve:
  Table 1a — Mobile     Table 1a — Tablet     Table 1a — Desktop
  Table 1b — Mobile     Table 1b — Tablet     Table 1b — Desktop
  Table 1c — Mobile     Table 1c — Tablet     Table 1c — Desktop
  Table 1d — Mobile     Table 1d — Tablet     Table 1d — Desktop

HEIGHT BUDGET — measured from the current live table. Stay at or under these:
  Mobile   2,300px      Tablet   1,320px      Desktop  1,420px
Shorter is better on Mobile. This table is the longest on the site and the mobile stack is the
problem being solved.

BRAND COLOURS — use these and nothing else:
  #2D6A4F  forest green, primary
  #0f3d2c  deep forest, dark scrims and headings
  #234f3b  aviary dark, dark panels
  #c8472f  clay ink, solid button fills with white text on them
  #e8604c  clay, large text and tints, on dark grounds only
  #b04228  clay for small text on a light ground
  #faf7f4  cream, page ground
  #f6efe8  warm bed, secondary ground
  #1f2a24  ink, body text
  #5b524a  muted, secondary text
  rgba(60,30,10,.12)  hairline rules
  #9fc7b0  mint, text on deep forest only

TYPE:
  Headings   Newsreader, weight 600
  Body / UI  IBM Plex Sans
  Uppercase labels  11-12px, letter-spacing .12em
  Mobile body text never below 14px

HARD RULES:
  1. The table MUST stack on Mobile. A horizontally scrolling table is never the only mobile answer.
  2. Use the text below word for word. Do not rewrite, shorten, reorder, or add rows.
  3. No colours outside the list above.
  4. No emoji. The characters * and ✓ and · and → and ↗ in the content are text — keep them as typed.
  5. One solid clay button per artboard maximum. Everything else outline or text.
  6. Mobile: no tap target under 44px tall.
  7. Card radius 16-18px, pill radius 50px. Shadow, where used: 0 6px 28px rgba(60,30,10,.12)
  8. No gradient text. No decorative left-edge accent stripes.
  9. Every figure below is real. Transcribe prices and species names exactly.

THE FOUR DIRECTIONS — make them genuinely different designs, not four versions of one idea:
  1a  ELEVATED CARDS — soft-shadowed rounded panels, generous padding, column headers as
      floating chips above the data. Modern product-pricing feel.
  1b  EDITORIAL RULE — type-led and near-boxless. Large Newsreader display, thin forest
      hairlines only, wide whitespace, small-caps row labels. No cards, no fills.
  1c  DARK PANEL — the table sits on a #0f3d2c ground, cream text, mint values, one column
      lifted. Premium and high contrast.
  1d  SPLIT FEATURE — asymmetric. A lead summary panel on one side, the trait data on the
      other. On Mobile the summary becomes a strip across the top.

CONTENT — exact text, all of it appears on all twelve artboards:

Eyebrow:  Compare Variants
Heading:  Is a Congo or a Timneh African Grey Right for You?
Intro:    We hand-raise both, and neither is "better" — the Congo is the bolder, more headline
          talker, while the Timneh is calmer and tends to start talking earlier, so the right one
          comes down to your home and your experience. Below we put our two Greys side by side,
          so you can see exactly which one we would help you bring home.

Column headers:
  Feature
  Congo African Grey     (subtitle: The classic, dramatic talker)
  Timneh African Grey    (subtitle: Calmer, earlier to bond)

Rows, in this order:
  Species          | Psittacus erithacus            | Psittacus timneh
  Size             | 12-14 in · 400-600 g           | 9-11 in · 275-375 g
  Tail color       | Scarlet red                    | Maroon / dark crimson
  Lifespan         | 40-60 years                    | 40-60 years
  Talking ability  | 5 stars, exceptional           | 4 stars, excellent, earlier
  Talking onset    | ~12 months                     | ~4-6 months (earlier)
  Temperament      | Confident, dramatic            | Calmer, steadier
  Best for         | Experienced owners             | First-time owners
  Price (ours)     | $1,700-$2,500                  | $1,500-$1,600
  Available now    | Roys · Amie · Bery · Jins/Jeni | Elad · Evie
  Sexed by lab     | ✓ Yes                          | ✓ Yes
  Paperwork        | ✓ Full set, hatched here       | ✓ Full set, hatched here

Note: render "Species" values in italic — they are scientific names. Render the star ratings as
five star glyphs and four-and-a-half star glyphs, not as the word "stars".

Two buttons below the table:
  Inquire about a Congo →      (this one is the solid clay button)
  Inquire about a Timneh →     (outline)

Attribution strip below the buttons, with the two labels set as small pills:
  [Fact ↗]  The size, tail and lifespan rows above are species figures from the World Parrot
  Trust profile;
  [Observed here · since 2014]  the talking-onset and temperament rows are what we have seen in
  our own clutches.

Closing line, with the comparison phrase as a link:
  Our full Congo vs Timneh African Grey comparison goes deeper than the table — temperament,
  talking onset, noise, and which of our two Greys we would match to your home.
```

## Prompt — Table 2 (Male vs Female)

```
You are designing a comparison-table component for CongoAfricanGreys.com (C.A.Gs), a family
breeder of captive-bred Congo and Timneh African Greys in Midland, Texas since 2014.

Produce a design canvas with 12 artboards: 4 style directions x 3 viewports.

VIEWPORT WIDTHS — exact, do not vary:
  Mobile   390px wide
  Tablet   768px wide
  Desktop  1440px wide

ARTBOARD NAMES — use exactly these twelve:
  Table 2a — Mobile     Table 2a — Tablet     Table 2a — Desktop
  Table 2b — Mobile     Table 2b — Tablet     Table 2b — Desktop
  Table 2c — Mobile     Table 2c — Tablet     Table 2c — Desktop
  Table 2d — Mobile     Table 2d — Tablet     Table 2d — Desktop

HEIGHT BUDGET — measured from the current live table. Stay at or under these:
  Mobile   1,650px      Tablet   1,230px      Desktop  1,210px

BRAND COLOURS — use these and nothing else:
  #2D6A4F  forest green, primary
  #0f3d2c  deep forest, dark scrims and headings
  #234f3b  aviary dark, dark panels
  #c8472f  clay ink, solid button fills with white text on them
  #e8604c  clay, large text and tints, on dark grounds only
  #b04228  clay for small text on a light ground
  #faf7f4  cream, page ground
  #f6efe8  warm bed, secondary ground
  #1f2a24  ink, body text
  #5b524a  muted, secondary text
  rgba(60,30,10,.12)  hairline rules
  #9fc7b0  mint, text on deep forest only

TYPE:
  Headings   Newsreader, weight 600
  Body / UI  IBM Plex Sans
  Uppercase labels  11-12px, letter-spacing .12em
  Mobile body text never below 14px

HARD RULES:
  1. The table MUST stack on Mobile. A horizontally scrolling table is never the only mobile answer.
  2. Use the text below word for word. Do not rewrite, shorten, reorder, or add rows.
  3. No colours outside the list above.
  4. No emoji. The ↗ character in the content is text — keep it as typed.
  5. One solid clay button per artboard maximum. Everything else outline or text.
  6. Mobile: no tap target under 44px tall.
  7. Card radius 16-18px, pill radius 50px. Shadow, where used: 0 6px 28px rgba(60,30,10,.12)
  8. No gradient text. No decorative left-edge accent stripes.

THE DESIGN PROBLEM SPECIFIC TO THIS TABLE: the cells are full sentences, not short values. Do not
squeeze sentences into narrow columns. Give the prose room and let the layout breathe.

THE FOUR DIRECTIONS — make them genuinely different designs, not four versions of one idea:
  2a  ELEVATED CARDS — soft-shadowed rounded panels, generous padding, column headers as
      floating chips above the data. Modern product-pricing feel.
  2b  EDITORIAL RULE — type-led and near-boxless. Large Newsreader display, thin forest
      hairlines only, wide whitespace, small-caps row labels. No cards, no fills.
  2c  DARK PANEL — the table sits on a #0f3d2c ground, cream text, mint values, one column
      lifted. Premium and high contrast.
  2d  SPLIT FEATURE — asymmetric. A lead summary panel on one side, the trait data on the
      other. On Mobile the summary becomes a strip across the top.

CONTENT — exact text, all of it appears on all twelve artboards:

Eyebrow:  Sex, Confirmed by Lab
Heading:  Should You Choose a Male or Female African Grey?
Intro, with "Observed here · since 2014" as a small pill at the start of it:
          In our experience hand-raising both, the sex of an African Grey matters far less than
          most buyers expect — our full guide to male vs female African Grey parrots walks
          through all eight differences, but the short version is that a bird's upbringing shapes
          temperament far more than its sex, and because every Grey we place is sexed by a lab
          you always know exactly which you are bringing home.
          (set "guide to male vs female African Grey parrots" and "sexed by a lab" as links)

Column headers:
  What buyers ask about
  Male African Grey
  Female African Grey

Rows, in this order:
  Talking & mimicry | Often a touch more talkative and a bolder mimic
                    | Slightly quieter, but still an excellent talker
  Temperament       | Confident; can be territorial or dominant, especially in breeding season
                    | Typically gentler and more even, though it can be moody at times
  Bonding style     | Outgoing — often bonds with the whole household
                    | May bond closely with one person; can be reserved with strangers

Fourth row, full width across both value columns, labelled "Telling them apart", containing a
small [Fact ↗] pill and then this text:
  African Greys are sexually monomorphic — males and females look identical — so PCR-based DNA
  sexing from a feather or blood sample, not invasive surgical sexing, is the only certain
  method. It is included with every bird we place.
  (set "PCR-based DNA sexing" as a link)

Recommendation block below the table, headed "Our recommendation":
  Honestly, the "better" sex is the one whose personality fits your home — a quieter female
  African Grey may suit a calm apartment, while a bold male African Grey thrives in a busy
  family. Tell Mark & Teri what you are looking for and they will match you with the right
  hand-raised bird; you can compare male and female African Greys in full here or ask us which
  Greys are available now.
  (set "compare male and female African Greys in full here" and "ask us which Greys are
  available now" as links)

Button (the solid clay one):  View Available Greys →
```

## Prompt — Table 3 (Grey vs Macaw, Cockatoo, Amazon)

```
You are designing a comparison-table component for CongoAfricanGreys.com (C.A.Gs), a family
breeder of captive-bred Congo and Timneh African Greys in Midland, Texas since 2014.

Produce a design canvas with 12 artboards: 4 style directions x 3 viewports.

VIEWPORT WIDTHS — exact, do not vary:
  Mobile   390px wide
  Tablet   768px wide
  Desktop  1440px wide

ARTBOARD NAMES — use exactly these twelve:
  Table 3a — Mobile     Table 3a — Tablet     Table 3a — Desktop
  Table 3b — Mobile     Table 3b — Tablet     Table 3b — Desktop
  Table 3c — Mobile     Table 3c — Tablet     Table 3c — Desktop
  Table 3d — Mobile     Table 3d — Tablet     Table 3d — Desktop

HEIGHT BUDGET — measured from the current live table. Stay at or under these:
  Mobile   1,600px      Tablet   1,340px      Desktop  1,000px

BRAND COLOURS — use these and nothing else:
  #2D6A4F  forest green, primary
  #0f3d2c  deep forest, dark scrims and headings
  #234f3b  aviary dark, dark panels
  #c8472f  clay ink, solid button fills with white text on them
  #e8604c  clay, large text and tints, on dark grounds only
  #b04228  clay for small text on a light ground
  #faf7f4  cream, page ground
  #f6efe8  warm bed, secondary ground
  #1f2a24  ink, body text
  #5b524a  muted, secondary text
  rgba(60,30,10,.12)  hairline rules
  #9fc7b0  mint, text on deep forest only

TYPE:
  Headings   Newsreader, weight 600
  Body / UI  IBM Plex Sans
  Uppercase labels  11-12px, letter-spacing .12em
  Mobile body text never below 14px

HARD RULES:
  1. The table MUST stack on Mobile. A horizontally scrolling table is never the only mobile answer.
  2. Use the text below word for word. Do not rewrite, shorten, reorder, or add rows.
  3. No colours outside the list above.
  4. No emoji.
  5. One solid clay button per artboard maximum. Everything else outline or text.
  6. Mobile: no tap target under 44px tall.
  7. Card radius 16-18px, pill radius 50px. Shadow, where used: 0 6px 28px rgba(60,30,10,.12)
  8. No gradient text. No decorative left-edge accent stripes.

THE STRUCTURE SPECIFIC TO THIS TABLE: unlike the others, the first column is a SPECIES, not a
trait — each row is a whole bird. African Grey is the only one we breed, so give that row visible
weight over the other three, using layout, type weight or a small label, never an off-palette
colour.

THE FOUR DIRECTIONS — make them genuinely different designs, not four versions of one idea:
  3a  ELEVATED CARDS — soft-shadowed rounded panels, generous padding, column headers as
      floating chips above the data. Modern product-pricing feel.
  3b  EDITORIAL RULE — type-led and near-boxless. Large Newsreader display, thin forest
      hairlines only, wide whitespace, small-caps labels. No cards, no fills.
  3c  DARK PANEL — the table sits on a #0f3d2c ground, cream text, mint values, the African
      Grey row lifted. Premium and high contrast.
  3d  SPLIT FEATURE — asymmetric. A lead panel carrying the African Grey beside the other three
      species. On Mobile the lead becomes a strip across the top.

CONTENT — exact text, all of it appears on all twelve artboards:

Eyebrow:  Beyond the Two Greys
Heading:  How Does an African Grey Compare to a Macaw, Cockatoo, or Amazon?
Intro:    The African Grey is the parrot most families ask us about — and we point them to our
          full African Grey comparison hub to weigh it against the other big talkers. Here is how
          the Grey we raise stacks up.
          (set "full African Grey comparison hub" as a link)

Column headers:
  Species | Talking ability | Noise level | Best for

Rows, in this order:
  African Grey | Exceptional — context-aware speech | Moderate
               | Owners wanting a talkative, problem-solving companion
  Macaw        | Good, but fewer words             | Very loud
               | Experienced owners with space and tolerance for volume
  Cockatoo     | Limited speech                    | Very loud
               | Cuddle-seekers who can meet high attention needs
  Amazon       | Strong talker & singer            | Loud
               | Owners who want a bold, outgoing personality

Recommendation block below the table, headed "Our recommendation":
  For most buyers choosing their first larger parrot, the African Grey comes out ahead on the two
  factors that matter most in a real home: how much the bird can genuinely communicate, and how
  manageable its noise is day to day. Our African Grey vs Macaw and African Grey vs Cockatoo
  breakdowns show why their volume and attention needs put those two out of reach for most homes.
  (set "African Grey vs Macaw" and "African Grey vs Cockatoo" as links)

Button (the solid clay one):  Full African Grey Comparison Hub →
```

## Prompt — Table 4 (Pricing)

```
You are designing the PRICING table component for CongoAfricanGreys.com (C.A.Gs), a family
breeder of captive-bred Congo and Timneh African Greys in Midland, Texas since 2014.

Produce a design canvas with 12 artboards: 4 style directions x 3 viewports.

VIEWPORT WIDTHS — exact, do not vary:
  Mobile   390px wide
  Tablet   768px wide
  Desktop  1440px wide

ARTBOARD NAMES — use exactly these twelve:
  Table 4a — Mobile     Table 4a — Tablet     Table 4a — Desktop
  Table 4b — Mobile     Table 4b — Tablet     Table 4b — Desktop
  Table 4c — Mobile     Table 4c — Tablet     Table 4c — Desktop
  Table 4d — Mobile     Table 4d — Tablet     Table 4d — Desktop

HEIGHT BUDGET — measured from the current live table. Stay at or under these:
  Mobile   1,480px      Tablet   1,410px      Desktop  960px

BRAND COLOURS — use these and nothing else:
  #2D6A4F  forest green, primary
  #0f3d2c  deep forest, dark scrims and headings
  #234f3b  aviary dark, dark panels
  #c8472f  clay ink, solid button fills with white text on them
  #e8604c  clay, large text and tints, on dark grounds only
  #b04228  clay for small text on a light ground
  #faf7f4  cream, page ground
  #f6efe8  warm bed, secondary ground
  #1f2a24  ink, body text
  #5b524a  muted, secondary text
  rgba(60,30,10,.12)  hairline rules
  #9fc7b0  mint, text on deep forest only

TYPE:
  Headings   Newsreader, weight 600
  Body / UI  IBM Plex Sans
  Uppercase labels  11-12px, letter-spacing .12em
  Mobile body text never below 14px
  Use tabular figures for the prices so the column aligns

HARD RULES:
  1. The table MUST stack on Mobile. A horizontally scrolling table is never the only mobile answer.
  2. Use the text below word for word. Do not rewrite, shorten, reorder, or add rows.
  3. No colours outside the list above.
  4. No emoji.
  5. One solid clay button per artboard maximum. Everything else outline or text.
  6. Mobile: no tap target under 44px tall.
  7. Card radius 16-18px, pill radius 50px. Shadow, where used: 0 6px 28px rgba(60,30,10,.12)
  8. No gradient text. No decorative left-edge accent stripes.
  9. THESE ARE REAL PRICES. Transcribe every figure exactly as written. Never round them, never
     re-range them, never add a "starting at", never invent a discount or a strikethrough.

THE DESIGN PROBLEM SPECIFIC TO THIS TABLE: price is the column buyers scan for. In every one of
the four directions, price must hold the strongest position on the row and stay easy to compare
down the column.

THE FOUR DIRECTIONS — make them genuinely different designs, not four versions of one idea:
  4a  ELEVATED CARDS — soft-shadowed rounded panels, generous padding, price as the anchor of
      each card. Modern product-pricing feel.
  4b  EDITORIAL RULE — type-led and near-boxless. Large Newsreader display, thin forest
      hairlines only, wide whitespace, price set large in a terminal column. No cards, no fills.
  4c  DARK PANEL — the table sits on a #0f3d2c ground, cream text, prices in mint. Premium and
      high contrast.
  4d  SPLIT FEATURE — asymmetric. A lead panel carrying the headline price range beside the full
      list. On Mobile the lead becomes a strip across the top.

CONTENT — exact text, all of it appears on all twelve artboards:

Eyebrow:  Transparent Pricing
Heading:  What Does a Hand-Raised, Documented African Grey Parrot Cost From C.A.Gs?
Intro:    African Grey parrot prices at C.A.Gs are never just a number on a chick — the price you
          see already includes every certificate listed under how we document each bird, because
          a documented, captive-bred African Grey is the only kind we will ever sell.
          (set "African Grey parrot prices", "how we document each bird" and "captive-bred
          African Grey" as links)

Column headers:
  Subspecies | Adult weight | Best fit / lifestyle | Talking ability | Price

Rows, in this order:
  CONGO GREY · BABY        | 400-600 g            | Bond-from-day-one buyers
                           | Exceptional · hand-raised          | $2,300-$2,500
  CONGO GREY · ADULT       | 400-600 g            | Calm, established personality
                           | Pre-developed vocabulary           | $1,700
  TIMNEH GREY              | 275-375 g            | First-time owners / active families
                           | Excellent · earlier talker         | $1,500-$1,600
  CONGO PAIR (Jins + Jeni) | Bonded pair          | Two-bird homes
                           | Must go together                   | $3,500
  BREEDING PAIR            | Proven · Closed-banded | Established breeders
                           | Fully documented                   | From $3,000
  FERTILE EGG              | Candled              | Experienced breeders
                           | Buy 5, free US shipping            | $95 / egg

Note: the en dashes in the price ranges and weights are en dashes, not hyphens.

Quote block below the table, labelled "EXPERT TAKE · TERI BENJAMIN":
  "Anyone listing a Congo African Grey under $1,500 is selling a wild-caught bird, a sick bird,
  or no bird at all. Real, documented, aviary-hatched Greys reflect the cost of ethical breeding."

Button (the solid clay one):  Reserve Yours Now →
```

## One-run alternative

If you would rather do all sixteen in a single Claude Design run, paste the four prompts above one
after another into one message and add this line at the top:

```
Produce 48 artboards total across four tables: Table 1a-1d, Table 2a-2d, Table 3a-3d and Table
4a-4d, each at Mobile 390, Tablet 768 and Desktop 1440. Give every artboard the same care — do
not simplify the later tables. The four instruction blocks follow.
```

I do not recommend it. Quality drops off across a run that long, and Table 4 is the one that
carries your prices.

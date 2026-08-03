# Infographic Prompt Pack — `/african-grey-breeding-pair-for-sale/`

**Date:** 2026-08-03 · **Sprint 2 · ASSET GATE** · **7 infographics**
**The page build starts only after these are dropped in and the breeder says "start."**

---

## 0 · READ BEFORE GENERATING — failures already shipped on this site

| # | What happened | Rule it produced |
|---|---|---|
| 1 | An infographic shipped reading **"BREDDER"**; another had **"HOME HOME"**; a third set "Polyomavirus" too tight to read | **Read every word on the returned image before accepting it.** The generator misspells baked-in type |
| 2 | The generator baked **prompt instructions** in as visible labels — "green tick", "clay cross" appeared *on the image* | **LITERAL TEXT (render exactly) is separated from STYLE (never render).** Do not paste style notes into the text block |
| 3 | British **"colour"** appeared on a US page | **US spelling throughout.** The literal blocks below are already US-spelled — do not retype them |
| 4 | An infographic's axis labels were bird prices and shipping tiers, so it was rejected at harden | **Every axis and label below is specified.** Do not let the generator invent one |

### Universal rules — all 7

- **Canvas 1408 × 768, 16:9.** Ships `<95 KB` WebP + a `-760.webp` sibling, baked with `reframe_og.py`.
- **Render ONLY the strings in each `LITERAL TEXT` block.** No other words anywhere. No invented title.
- **Spelling to check on delivery:** BREEDER · CLUTCH · PROVEN · UNPROVEN · CITES · Appendix I ·
  Psittacus erithacus · Midland · nest box · closed band.
- **Palette (never rendered as words):** forest green `#2D6A4F`, clay `#e8604c`, cream `#faf7f4`,
  charcoal `#3a2f2a`, warm beige.
- **Bird marks:** real African Grey — grey body, **red** tail (Congo). **Never a generic green parrot.
  Never the 🦜 emoji.**
- **Negative list, append to every prompt:** *no text other than the literal strings listed, no
  watermarks, no logos, no captions, no UI chrome, no other parrot species, no generic green parrot,
  no cold blue or clinical lighting, no distorted or extra limbs or beaks, no jungle or wild-capture
  context, no cluttered background, no misspelled words, no placeholder text.*
- **Style wrapper:** *Clean flat editorial infographic, warm cream background, forest-green and clay
  accents, generous margins, one clear visual hierarchy, high legibility at 760px wide, no drop
  shadows, no gradients on text.*

### 🔴 Two facts that MUST be right on these images

1. **The corrected maturity arithmetic.** Maturity **by about 4 years**; earliest documented fertile
   eggs **about 3**; **commonly 5–6** in practice. **Never render "5–6 minimum"** — our own Sally is 4
   with a clutch and the page says so.
2. **No DNA certificate.** These pairs are **closed-banded with clutch history on request.** No image
   may show a DNA certificate, a lab report, or the words "DNA sexed" / "DNA certified."

---

## 1 · Slot map — photos are already baked, do NOT generate for these

All 17 real photos are baked in `public/images/breeding-pair-page/`:

| Section | Baked photo |
|---|---|
| §1 Hero | `hero-african-grey-breeding-pair-for-sale-aviary-cage` |
| §2 Pair cards | `talker-jane-…` · `mari-lake-…` · `sally-odin-…` |
| §6 What each pair produced | `proven-african-grey-hen-on-nest-with-eggs` |
| §7 Tame breeder stock | `congo-african-grey-breeding-pair-tame-hand-reared` · `breeding-pair-of-african-grey-parrots-for-sale-perched` |
| §11 Housing | `african-grey-breeding-pair-flight-cage-housing` |
| §12 Paperwork / health | `african-grey-breeding-pair-health-check-nail-trim` |
| §13 Shipping | `african-grey-breeding-pair-shipping-two-crates` |
| §14 Singles + eggs | `african-grey-parrot-fertile-eggs-in-incubator` · `candled-fertile-…-egg-for-sale` · `hand-fed-congo-…-chick` · `hand-held-…-weaned-chick` |
| §16 Reviews | `breeder-review-african-grey-breeding-pair-buyer` |
| Spare | `african-grey-breeding-pair-available-now-midland-texas` · `timneh-and-congo-…-together` |

**The 7 below fill the analytical slots only.**

---

## INF-1 · §3 — What "Proven" Actually Means · *Comparison, 3 columns*

**PROMPT:** Clean flat editorial infographic, three equal columns on warm cream, each column headed by a
small African Grey silhouette with a red tail. Column one framed in forest green with a filled check
mark; columns two and three framed in muted charcoal with an open outline mark. A single horizontal
rule separates headings from body. [style wrapper] [negative list]

```
LITERAL TEXT
PROVEN          UNPROVEN            BONDED ONLY
Has hatched     Mature and paired   A pair that sits
a fertile       but no clutch       together but has
clutch          has hatched         never nested
Ask for the     Ask what is         Ask if they have
clutch dates    still missing       ever laid at all
```

---

## INF-2 · §4 — Why the Fewest Clutches Costs the Most · *Comparison, ascending ladder*

**PROMPT:** Flat editorial chart, three ascending steps left to right on warm cream. Step height rises
with price; a clay bar rises while a separate forest-green bar falls across the same three steps, making
the inverse relationship visible at a glance. Small African Grey pair silhouette above each step.
[style wrapper] [negative list]

```
LITERAL TEXT
TALKER & JANE     MARI & LAKE     SALLY & ODIN
4 clutches        2 clutches      1 clutch
$3,000            $4,500          $5,500
You are buying breeding years ahead, not clutches behind
```

---

## INF-3 · §5 — How Old Before They Can Breed · *Process Flow, horizontal timeline*

**PROMPT:** Flat horizontal timeline on warm cream, left to right, with four marked stops on a single
forest-green axis. One clay marker sits far left, clearly before the first stop, flagged with an open
warning outline. [style wrapper] [negative list]

**🔴 Check on delivery: the clay marker must sit BEFORE the 3-year stop, never between 3 and 4.**

```
LITERAL TEXT
15 MONTHS        3 YEARS            4 YEARS          5 TO 6 YEARS
Advertised as    Earliest fertile   Sexual maturity  Commonly
proven by some   eggs on record     reached          producing
sellers
Not possible
```

---

## INF-4 · §8 — Moving a Proven Pair Without Stopping Production · *Process Flow, 5 steps*

**PROMPT:** Flat five-step process flow on warm cream, connected by a single forest-green line with
round numbered nodes in clay. Each step gets one short label beneath its node. [style wrapper]
[negative list]

```
LITERAL TEXT
1 TRAVEL TOGETHER   2 SAME SETUP    3 QUIET WEEKS   4 NEST BOX LAST   5 LET THEM SETTLE
Two crates,         Match the       No handling,    Offer the box     Production returns
never one           cage and diet   no visitors     only when settled on their clock
```

---

## INF-5 · §9 — Random Pairing Versus Experienced Pairing · *Comparison, 2 columns*

**PROMPT:** Flat two-column comparison on warm cream. Left column muted charcoal with an open outline
mark, right column forest green with a filled check mark. Two African Grey silhouettes face away from
each other on the left, and toward each other on the right. [style wrapper] [negative list]

```
LITERAL TEXT
PUT TWO BIRDS TOGETHER      MATCH A COCK TO A HEN
Guess the sexes             Confirm the sexes first
Hope they bond              Watch before committing
Wait years for a clutch     Buy a pair already producing
No record either way        Clutch dates on request
```

---

## INF-6 · §10 — What a Proven Pair Costs Elsewhere · *Comparison, horizontal bars*

**PROMPT:** Flat horizontal bar chart on warm cream, five bars, longest at top. The bottom bar is
forest green and clearly labeled as ours; the four above are neutral warm beige. Value labels sit at the
end of each bar. [style wrapper] [negative list]

**🔴 These are observed live listings, not a survey. The label wording below is exact — do not soften
it to "average" or "market rate."**

```
LITERAL TEXT
LISTED PRICES FOR A PROVEN OR BONDED PAIR
Tulsa, Oklahoma          $9,495
Stone Mountain, Georgia  $8,000
Gwynnoak, Maryland       $6,500
Texas, proven pair       $5,500
C.A.Gs, Midland Texas    $3,000 to $5,500
```

---

## INF-7 · §11 — Housing and Nest Box a Breeding Pair Needs · *Feature Grid, 4 cells*

**PROMPT:** Flat four-cell grid on warm cream, each cell with a simple line icon — a flight cage
outline, a vertical nest box, a thermometer, a water droplet. Forest-green icon strokes, clay numerals.
[style wrapper] [negative list]

**Source: World Parrot Trust, *Psittacus erithacus*. Do not alter these numbers.**

```
LITERAL TEXT
FLIGHT LENGTH        NEST BOX             TEMPERATURE       HUMIDITY
3 meters minimum     12 x 12 x 24 inches  68 to 80 F        50 to 65 percent
9.8 feet             vertical, mounted
                     outside the cage
```

---

## 2 · Delivery checklist

☐ 7 images returned at 1408 × 768
☐ **Every word read** — no BREDDER, no doubled words, no British spelling
☐ **No prompt instructions rendered** as visible labels
☐ INF-3: the 15-month marker sits **before** the 3-year stop
☐ INF-6: says **listed prices**, not average or market rate
☐ No DNA certificate, lab report, or the words "DNA sexed" anywhere
☐ No generic green parrot; Congo tails are red
☐ Baked through `reframe_og.py` → `<95 KB` + `-760.webp` sibling
☐ Dropped into `public/images/breeding-pair-page/`

**Then say "start" and Sprint 2 writes the page.**

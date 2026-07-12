# Gemini Image + Infographic Prompt Pack — /african-grey-pros-and-cons/ · 2026-07-12

Decision / weighing page (Strategy B). Visual spine = **honest trade-offs + self-assessment**, one
species only (no two-bird split hero). Every slot uses a **DISTINCT visual treatment** so the page
never reads as identical cards. Comparison pages ship **no HTML/CSS infographics** — real OG photos or
Gemini images only.

---

## Global spec (applies to every Gemini prompt)
- **Generate:** 16:9, 1600×900 px. Post: resize 1408×768, WebP ≤100 KB (Pillow `method=6`, quality
  78→54 until <95 KB), place in `public/` with the SEO filename. Ship a `-760.webp` sibling +
  `srcset="/name-760.webp 760w, /name.webp 1408w" sizes="(max-width:900px) 92vw, 760px"`.
- **On-page:** 760px wrapper, `width="1408" height="768"`, class `sec-img inf-img`, `loading="lazy"`,
  wrapped in `<a>` to the page named per slot. **Real `<table>`/paired-list/data stays in the DOM** —
  the image illustrates, never replaces, the AIO-extractable text.
- **Palette (hard rule):** Cream `#faf7f4`, Forest Green `#2D6A4F` structure/labels, Clay `#e8604c`
  accents only. Warm grade. Never blue/clinical.
- **Text in image:** short labels + numbers ONLY, and only figures already written + cited on the page
  (40–60 yrs, 5–7 yrs maturity, $1,700–$3,500, $185/$350). Never invent a stat.
- **African Grey accuracy (when a grey appears):** light silver-grey body, fine pale scalloping,
  **bright red tail**, bare pale facial mask, solid dark beak, pale-yellow adult iris. Never green.
- **Append this NEGATIVE to every prompt:** `no watermarks, no logos, no brand names, no UI chrome, no
  generic green cartoon parrot, no parrot species other than African Grey, no dogs or cats unless the
  slot asks, no wild-capture or jungle-trade imagery, no cages that look like a pet-shop, no cold blue
  or clinical lighting, no extra limbs or deformed beaks, no cluttered background, no long paragraphs
  of text, no misspelled words.`
- **Pipeline:** `@cag-image-pipeline` → image-metadata 5-element set (Rule 50b — PRIMARY keyword
  *"African Grey parrot pros and cons"* on the HERO alt ONLY; every other image a different keyword).
- **Command:** `bash scripts/generate_nb_image.sh "PROMPT" "filename.png" "1600x900"` (`GEMINI_API_KEY` in `.google-key`).

---

# PART A — OG photo slots (real photos; reuse cluster assets or shoot)
| Slot | § | Purpose | Source |
|---|---|---|---|
| HERO | 1 | Warm single grey portrait, thoughtful mood; copy overlays LEFT | `assets/brand/` grey portrait |
| Pros deep | 6 | Grey talking / on a hand, bonded | brand talking-bird photo |
| Who-should-NOT / thrives | 9–10 | Empty-cage-alone vs engaged-owner | brand photos |
| Documented bird | 17 | Hand-raised chick + docs | brand |
| Shipping ×2 | 18 | Home-delivery van + airport cargo | cluster: `african-grey-home-delivery-pet-van.webp` / `...airport-live-animal-shipping.webp` |
| Owner story / reviews | 19 | Real buyer + bird | `bottomReviews[]` real image |
| Available birds | 20 | Real current birds | `/available/` slugs |

**Reuse first:** shipping van + airport cargo + owner + talking-bird images already exist across the
cluster — pull before generating. Add `.portrait` + fixed dims for any square file.

---

# PART B — Gemini infographic prompts (6 slots, distinct style each)

## INF-1 · §4 Pros & Cons at a Glance  →  `african-grey-pros-and-cons-balance-scale.png`
**Style:** **a balance-scale motif** — pros on one pan, cons on the other, gently level. NOT a card.
**Links to:** `/african-grey-comparison/`.
**Prompt:**
> Warm flat-illustration on cream `#faf7f4`: a classic two-pan balance scale, near level. LEFT pan
> labelled "Pros" (forest-green `#2D6A4F`) holding small icons — a speech bubble, a lightbulb, a heart.
> RIGHT pan labelled "Cons" (clay `#e8604c`) holding a clock, a dollar sign, a dust cloud. Clean
> editorial line work, generous negative space, no parrot needed, short labels only. [+NEGATIVE]

## INF-2 · §7 One-Person Bonding & Maturity  →  `african-grey-one-person-bond-jealousy.png`
**Style:** **relationship-diagram** — a grey with lines of attachment to one person, faded to others.
Distinct from a card. **Links to:** `/african-grey-parrot-care-guide/`.
**Prompt:**
> Warm illustrative diagram on cream: a single silver-grey African Grey with a bright red tail perched
> centre, a bold clay `#e8604c` bond-line connecting it to ONE silhouetted person, and thinner faded
> forest-green lines to two other silhouettes. Small label "Bonds deeply to one person · 5–7 yrs".
> Editorial, empathetic, uncluttered, accurate grey markings. [+NEGATIVE]

## INF-3 · §8 Is an African Grey Right for You? (self-assessment)  →  `african-grey-owner-fit-scorecard.png`
**Style:** **a checklist/scorecard sheet** with tick rows + a simple readiness meter. **Links to:**
`/is-african-grey-good-for-beginners/`.
**Prompt:**
> Warm scorecard sheet on cream `#faf7f4`: a vertical checklist of 6 rows with clay `#e8604c` tick
> boxes — "Home most of the day", "Hours of daily time", "Long-term (40–60 yr) plan", "Noise-tolerant
> household", "Budget for vet + setup", "Prior parrot experience". A small horizontal readiness meter
> at the bottom (low→high, forest-green fill). Forest-green labels, spec-sheet feel, short labels only.
> [+NEGATIVE]

## INF-4 · §11 Captive-Bred vs Wild-Caught (conservation)  →  `african-grey-captive-bred-vs-wild-caught.png`
**Style:** **two-panel contrast** — a documented captive-bred aviary bird vs a barred "wild-capture"
symbol with a red prohibition line. Ethical, honest. **Links to:** `/cites-african-grey-documentation/`.
**Prompt:**
> Two-panel warm illustration on cream: LEFT a healthy silver-grey African Grey with red tail on a
> clean home perch beside a small "captive-bred · CITES documented" certificate icon (forest-green
> check); RIGHT the same species silhouette behind a barred crate with a clay `#e8604c` prohibition
> circle-slash and label "wild-caught · illegal". Respectful, non-graphic, editorial, accurate grey
> markings, short labels only. [+NEGATIVE]

## INF-5 · §14 Real Cost of Ownership  →  `african-grey-first-year-and-lifetime-cost.png`
**Style:** **stacked itemised receipt** with a shipping-tier footer. **Links to:** `/african-grey-parrot-price/`.
**Prompt:**
> Warm itemised-receipt illustration on cream `#faf7f4`: a vertical stacked breakdown column — "Bird
> $1,700–$3,500", "Cage & setup", "Food & enrichment", "Avian vet", with a forest-green `#2D6A4F`
> subtotal rule, and a footer row "Airport pickup $185 · Home delivery $350" in clay. Clean receipt
> typography, warm tones, short numeric labels only, no fabricated totals. [+NEGATIVE]

## INF-6 · §15 The 40–60 Year Lifespan  →  `african-grey-40-60-year-lifespan-timeline.png`
**Style:** **horizontal life-timeline ribbon** (0 → 60 yrs) with life-stage markers. **Links to:**
`/african-grey-lifespan/` (fallback `/african-grey-parrot-care-guide/`).
**Prompt:**
> Horizontal timeline ribbon on cream: a single track from "0" to "60 years", forest-green `#2D6A4F`
> line with clay `#e8604c` milestone dots at "weaned", "5–7 yrs maturity", "20", "40", "60". A small
> silver-grey African Grey silhouette (red tail) at the start. Label "A 40–60 year commitment". Clean,
> editorial, short labels only. [+NEGATIVE]

---

## Build fallback (until images generated)
Page is GEO-sound without images: every INF slot has a real paired-list, `<table>`, checklist, or data
block in the DOM with the same figures. Ship sized placeholder slots (`.sec-img.inf-img` box, correct
`width/height`) that swap 1:1 when WebPs land — no layout shift. HERO + shipping + owner + reviews use
reused real OG photos immediately.

## Image-SEO reminder (Rule 50b — no two alts share a keyword)
- HERO alt = PRIMARY *"African Grey parrot pros and cons"* (only place it appears).
- INF-1 → *African Grey owner trade-offs* · INF-2 → *African Grey one-person bonding* · INF-3 → *is an
  African Grey right for you* · INF-4 → *captive-bred vs wild-caught African Grey* · INF-5 → *African
  Grey cost of ownership* · INF-6 → *African Grey lifespan* · shipping → *nationwide African Grey
  shipping* · owner → *C.A.Gs owner review* · pros photo → *African Grey talking ability*.

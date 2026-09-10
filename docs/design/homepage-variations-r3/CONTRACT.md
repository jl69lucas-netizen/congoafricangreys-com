# Homepage Component Variations — ROUND 3 (G / H / I)

Round 1 = A/B/C (`../homepage-variations/`). Round 2 = D/E/F (`../homepage-variations-r2/`).
**This is round 3 = G / H / I.** Same invariants as rounds 1 and 2; the axes and the four
round-3 mandates below are new. Authors write artboards against THIS contract; the
controller merges, seeds, publishes. Read it fully before writing.

## 0. Why round 3 exists (the breeder's four findings on round 2)

Round 2 was rejected on all four counts at once. Every one is a gate on this round:

| # | Round-2 finding | Round-3 mandate |
|---|---|---|
| 1 | **Designs were too samey** — D/E/F read as reshuffles of A/B/C | Each G/H/I is a *structural* departure: a different layout primitive, not a restyle. If a variation could be reached from an earlier one by changing padding and colour, it is rejected. |
| 2 | **Content was dropped or wrong** | VERIFIED DEFECT: the live shipping section has **three** tiers (Airport Pickup $185 · Home Delivery $350 · Flight Nanny from $750). Round 2's contract said two, and **0 of its 9 shipping artboards mention Flight Nanny**. Every round-3 artboard is content-gated against the live page before it ships. |
| 3 | **Looked bad / off-brand** | Visual craft is a first-class gate this round: type scale, 4/8px rhythm, alignment, one clay CTA, real optical hierarchy. See §9. |
| 4 | **Still too long / didn't fix the problem** | Measured height is pass/fail, not commentary. Targets in §8. The FAQ (21 questions, ~2,404px at Mobile live) and the hero (~649px desktop live, band is 350-400px) are the two named failures. |

## 1. Canvas shape

7 canvas pages: `hero` · `counter` · `dial` · `rail` · `tables` · `faq` · `shipping`.
10 components × 3 variations × 3 viewports = **90 artboards**.
Viewports: Mobile **390** wide · Tablet **768** wide · Desktop **1440** wide.
File naming: `<Component>-<G|H|I>-<Mobile|Tablet|Desktop>.dc.html`.
Components: `Hero` `Counter` `Dial` `Rail` `Table-Cvt` `Table-Mvf` `Table-Others`
`Table-Price` `Faq` `Shipping`.
`Main.dc.html` is a copy of the leading candidate and must exist.

## 2. The `.dc.html` format (exact, unchanged from rounds 1-2)

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
  <style>
    body { margin:0; background:#faf7f4; font-family:"IBM Plex Sans", system-ui, sans-serif; color:#1f2a24; }
    h1,h2,h3 { font-family: Newsreader, Georgia, serif; font-weight:600; letter-spacing:-.003em; margin:0; }
    p { margin:0; } ul { margin:0; padding:0; list-style:none; }
    a { color:#b04228; text-decoration:none; } a:hover { color:#c8472f; }
  </style>
</helmet>
<div id="root" style="width:1440px; background:#faf7f4; display:flex; flex-direction:column;">
  … INLINE styles only …
</div>
</x-dc>
</body>
</html>
```

- Keep `<script src="./support.js"></script>` verbatim. Static artboards: NO `<script data-dc-script>`.
- Close every element, double-quote every attribute. Inline `style` for anything restyle-able.
- `display:flex` / `display:grid` + `gap` (never margin-between-siblings). Grids as
  `grid-template-columns: repeat(N, minmax(0, 1fr))`.
- No handlebars, no `<sc-for>`, no tweaks. Copy is literal text.
- Icons: inline SVG, stroke 1.75, 16/20/24 grid. **Never emoji.**
- `#root` width is exactly the viewport width (390 / 768 / 1440). Never wider.
- Images: bare filename, double-quoted. Files in this folder: `hero-midland.webp` (800×600, the
  LIVE homepage hero photo: Rony & Rose, "Midland, Texas" sign) · `hero-bird.webp` (700×525) ·
  `bird-1.webp` Evie Timneh (591×640) · `bird-2.webp` aviary pair (640×640) · `bird-3.webp`
  candled eggs (550×688) · `bird-4.webp` Roys Congo (640×800) · `shipping-crate.webp` (640×362) ·
  `shipping-2.webp` (640×426). Always set `width`/`height` and `object-fit:cover`; every `<img>`
  gets a real alt.
- Every hit target ≥44px on Mobile. Body copy ≤70ch. Minimum text 12px at Mobile (11px only for
  eyebrows that decorate, never for text carrying a fact or a price).
- Validate: `xmllint --html --noout <file>` and every `<img src>` names a file here.

## 3. Brand tokens (locked — never invent a value)

Forest `#2D6A4F` · Forest dark scrim `#0f3d2c` · Aviary dark `#234f3b` · Clay `#e8604c`
(large text / tints / on dark only) · Clay-ink `#c8472f` (solid button fills, white text) ·
Clay small text on light `#b04228` · Cream `#faf7f4` · Warm bed `#f6efe8` · Ink `#1f2a24` ·
Muted `#5b524a` · Line `rgba(60,30,10,.12)` · Green tint `rgba(45,106,79,.08)`.
Headings Newsreader 600; body IBM Plex Sans; eyebrows 11-12px, letter-spacing .12em,
uppercase, clay `#b04228`. Radii: cards 16-18px, pills 50px, form submit 12px.
Shadow: warm `0 6px 28px rgba(60,30,10,.12)`. Motion ≤0.2s (none needed on artboards).
Primary CTA = ONE clay pill per component (`background:#c8472f; color:#fff; border-radius:50px`).

## 4. Invariants every variation keeps

1. Palette above; **no new colours**.
2. Hero/counter separation: a tone shift AND a 1px rule between hero and counter.
3. **Desktop hero: 350-400px tall**, measured on the hero grid at 1440.
4. Sticky offsets assume a 96px header; a mobile rail sits at the **TOP** under the header,
   **never bottom-pinned** (rejected 2026-07-23).
5. Dial rows ≥24px tall, tag/label always visible, numerals ≥4.5:1 (`#6b625a` on cream,
   `#9fc7b0` on `#234f3b`), row font ≥.74rem.
6. Tables: at Mobile they stack (cards, bands, tabs, verdict, definition list). **Never a
   horizontally scrolling classic table as the ONLY mobile answer.**
7. Copy is the live page's copy, lifted verbatim (§6). Prices from `data/price-matrix.json`.
   **Never a new claim.**
8. **CITES is Appendix I.**
9. Congo range **$1,500-$3,500**.
10. **One clay CTA per component.**
11. **No em dashes in NEW copy.** Copy lifted verbatim from the live page keeps whatever it
    already has; do not "fix" an em dash that came from the page.
12. No side-stripe accent borders (`border-left:4px solid …`) as decoration. No gradient text.
13. `display:table-caption` is banned on a mobile-stacked table; drop uppercase captions at
    Mobile instead.

## 5. Round-3 variation axes (one named axis each; never palette)

Rounds 1-2 already used, and G/H/I must NOT return to: split copy+portrait, dark scrim photo
grid, mosaic metrics, framed portrait, lead photo + pair tiles, credential band (heroes);
4-up ledger, 2×2 tiles, inline ribbon, icon cards, green-tint band, seam card (counters);
light `.tdial`, dark card, grouped-by-part, progress line, two columns, collapsed parts (dial);
single-line pills, two-line chips, bottom sheet, part select, progress rail, icon chips (rail);
data-label cards, tab-toggle, verdict cards, column cards, banded rows, accordion rows (tables);
3-tab accordion, masonry, top-4+show-all, search-first, quick-answer cards, side-nav (FAQ);
two photo cards, timeline, split panel, tier chooser, route SVG, fact grid (shipping).

| Component | **G** | **H** | **I** |
|---|---|---|---|
| **Hero** | **Marquee**: type-led horizontal bands. Oversized Newsreader headline spanning full width as the dominant element, a slim full-bleed photo strip beneath it as a band (never a side column), CTA + availability count inline under it. No column split anywhere. | **Ledger hero**: the hero IS the inventory. Compact copy block left; right is a 6-row mini-ledger of real birds (name · species · price · status) with hairline rules. Data, not photography, carries the hero. | **Postcard**: ONE wide landscape photo card with the copy set inside the photo's lower third on a `#0f3d2c` scrim; credentials as a thin strip beneath the card. Overlay, not adjacency. |
| **Counter** | **Underline stat**: no card, no box, no bed. Numeral over label on cream, each with a 3px clay underline whose width varies per stat so the row reads as a mini bar chart. | **Split emphasis**: asymmetric. Two lead stats set large on the left (`12+`, `100%`), two supporting stats small and stacked on the right, divided by one hairline. Never an equal 4-up. | **Stamp row**: each stat inside a circular certification-seal badge with a 2px forest ring, numeral centred, label beneath the circle. Circular badges, not rectangles. |
| **Desktop dial** | **Arc gauge**: a circular arc progress gauge with the % and the current section name centred inside it; beneath, the 4 parts as rows with section counts, the current part expanded to its sections. Radial, not a list. | **Numbered index**: sections as a numbered `01`-`18` index, part rules between groups, **no ring at all**, active row takes a clay left tick and bold weight. Rows ≥26px. An index, not a dial. | **Dot matrix**: an 18-dot grid (6×3) at the top as the position map, the active section's full label large beneath it, part names as a 4-item legend. Map + one label, not 18 rows. |
| **Mobile jump links** (top rail always) | **Drawer index**: sticky top bar showing the current section + a menu affordance; tapping opens a full-width overlay drawer **downward** listing all 18 grouped by part, with a close control. Top-anchored. | **Two-tier rail**: two persistent rows. Row 1 = the 4 part tabs, always visible. Row 2 = the active part's sections as scroll-x pills. Hierarchy visible without interaction. | **Segment stepper**: one line only. `07 / 18 · Verify Us` with prev/next chevrons and an **18-segment bar where each segment is itself tappable**. The bar IS the navigation; no list. |
| **Tables** (×4) | **Comparison bars**: Mobile each trait is a label with its values as stacked mini-bars/chips, the leading value marked with an SVG check. Desktop classic with a subtle tint bar behind the leading cell. Visual weighting. | **Definition list**: Mobile a boxless `<dl>` — trait as `<dt>` in small caps, values as `<dd>` rows with the column name as a bold inline prefix. No cards, no borders. Desktop a two-column hairline table. Typographic. | **Pick-first**: Mobile opens with a verdict card ("Choose Congo if… / Choose Timneh if…", or the equivalent for that table) and puts the full trait list behind "See all N rows". Desktop classic with a sticky summary bar. Answer-first, detail-on-demand. |
| **FAQ** (all 21 questions must remain reachable) | **Topic accordion**: collapses to **4 topic rows** (Paperwork & Legal · Cost & Buying · The Birds · Care & Living). Tapping a topic reveals its questions as an inner accordion. Shortest possible default. | **Tab panel**: 4 topic tabs in one row; the panel below shows only the active topic's questions as one-line summaries. **Fixed height regardless of total count.** | **Dense index**: all 21 questions as a dense one-line index (two columns at Desktop, one at Mobile, ~28-32px per row); tapping opens the answer in a slide-down panel that replaces the index region. Everything scannable, nothing expanded. |
| **Shipping** (**all THREE tiers, always**) | **Price ladder**: the three tiers as an ascending ladder ($185 → $350 → $750), each row with a one-line "what you get", crate photo as a narrow right rail. Price-led ordering. | **Tier compare**: the three tiers as a 3-column mini comparison table (rows: price · how it travels · hand-off · best for), reusing the site's own table language for shipping. | **Photo band**: a full-width crate photo band with the copy on a `#0f3d2c` scrim, and the three tiers as three chips beneath that expand to their detail. Photo-led progressive disclosure. |

## 6. Copy sources (lift verbatim — never paraphrase, never invent)

All from `src/pages/index.astro` unless noted.

- **Hero** — `<HeroV3 availableCount={…} />` (L~446). Live H1 and sub-copy from
  `src/components/cag-library/HeroV3.astro`. Real birds for the Ledger hero (H): Roys (Congo),
  Amie (Congo), Bery (Congo), Jins + Jeni (Congo bonded pair, $3,500), Elad (Timneh, $1,600),
  Evie (Timneh, $1,500).
- **Counter** — L~449: `12+ / Years Aviary` · `100% / CITES Documented` · `$1,500 / Floor Price`
  · `24h / Reply Guarantee`. Exactly these four, exactly this wording.
- **Dial + Rail** — `railSections` L30-49: 18 sections. Part 1 *Meet the Breeders*: Our Breeders,
  Available, Eggs & Pairs. Part 2 *Choose Your Grey*: Congo Grey, Timneh Grey, Compare. Part 3
  *Why Families Trust Us*: Why Us, Verify Us, History, Health. Part 4 *Pricing, Tools & Buying*:
  Pricing, Cost Tools, Shipping, Reviews, Care Guides, FAQ, How to Buy, Contact.
  **18 sections, not 20. Never invent a row to reach a tidier number.**
- **Table-Cvt** — `<CompareTableE>` L679-695, 12 rows: Species · Size · Tail color · Lifespan ·
  Talking ability · Talking onset · Temperament · Best for · Price (ours) · Available now ·
  Sexed by lab · Paperwork. Heading: *Is a Congo or a Timneh African Grey Right for You?*
- **Table-Mvf** — `<table>` L710-739. Heading: *Should You Choose a Male or Female African Grey?*
  Columns: What buyers ask about · Male African Grey · Female African Grey.
- **Table-Others** — `<table>` L754-789. Heading: *How Does an African Grey Compare to a Macaw,
  Cockatoo, or Amazon?* Columns: Species · Talking ability · Noise level · Best for.
- **Table-Price** — `<PricingTable variant="classic">` L945-955, 6 rows: CONGO GREY · BABY
  ($2,300-$2,500, top pick) · CONGO GREY · ADULT ($1,700) · TIMNEH GREY ($1,500-$1,600) ·
  CONGO PAIR (Jins + Jeni) ($3,500) · BREEDING PAIR (From $3,000) · FERTILE EGG ($95 / egg).
  Heading: *What Does a Hand-Raised, Documented African Grey Parrot Cost From C.A.Gs?*
- **FAQ** — `faqItems` L189-231, **21 questions**. Heading: *What Do Buyers Ask Most Before
  Choosing One of Our African Greys?* Eyebrow: `COMMON QUESTIONS`. CTA:
  `See All African Grey FAQs →`.
- **Shipping** — `#shipping` L1035+. Heading: *How Do We Ship African Grey Parrots Safely to All
  50 States?* Eyebrow: `Nationwide IATA Delivery`. CTA: `IATA Shipping Guide →`.
  **THREE tiers, all mandatory:**
  | Tier | Price | Verbatim gist |
  |---|---|---|
  | Airport Pickup | `$185` | Receive your African Grey at your nearest major airport, hubs like ATL, DFW, ORD, LAX, or JFK among 80+ nationwide, via IATA-compliant live-animal cargo on Delta, United, or American. |
  | Home Delivery | `$350` | Door-to-door delivery to your home. |
  | Flight Nanny | `from $750` | Our most hands-on option: a vetted pet flight nanny keeps your African Grey in-cabin, never in the cargo hold, and hands the bird to you in person. Quoted per route, since we cover the chaperone's round-trip airfare. |

  Also true and usable: IATA-compliant carrier, avian-vet health certificate dated within 10 days
  of departure, ships to all 50 states from the West Texas home aviary.

## 7. Canvas fragments

Each author writes ONLY its own artboards plus ONE fragment file. **No author runs git.**

| Author | Artboards | Fragment | Canvas page |
|---|---|---|---|
| Hero | `Hero-{G,H,I}-{Mobile,Tablet,Desktop}` | `canvas.part-hero.json` | `hero` |
| Counter | `Counter-…` | `canvas.part-counter.json` | `counter` |
| Dial | `Dial-…` | `canvas.part-dial.json` | `dial` |
| Rail | `Rail-…` | `canvas.part-rail.json` | `rail` |
| Table-Cvt | `Table-Cvt-…` | `canvas.part-tables-cvt.json` | `tables` |
| Table-Mvf | `Table-Mvf-…` | `canvas.part-tables-mvf.json` | `tables` |
| Table-Others | `Table-Others-…` | `canvas.part-tables-others.json` | `tables` |
| Table-Price | `Table-Price-…` | `canvas.part-tables-price.json` | `tables` |
| Faq | `Faq-…` | `canvas.part-faq.json` | `faq` |
| Shipping | `Shipping-…` | `canvas.part-shipping.json` | `shipping` |

Fragment shape (`x`/`y`/`w`/`h` in canvas px; `w` = the viewport width, `h` = measured root
height +5%; ≥80px between frames in a row, ≥120px between rows):

```json
{
  "artboards": [
    { "file": "Hero-G-Mobile.dc.html",  "x": 0,    "y": 0, "w": 390,  "h": 760 },
    { "file": "Hero-G-Tablet.dc.html",  "x": 480,  "y": 0, "w": 768,  "h": 620 },
    { "file": "Hero-G-Desktop.dc.html", "x": 1340, "y": 0, "w": 1440, "h": 410 }
  ],
  "annotations": [
    { "id": "hero-g-note", "x": 0, "y": -110, "w": 380, "text": "G — Marquee. Trade-off: …" }
  ]
}
```

Row layout convention: **G at y=0, H at y=1100, I at y=2200** (adjust down if a row's tallest
artboard exceeds ~980px). Columns: Mobile x=0, Tablet x=480, Desktop x=1340.
Note ids must be globally unique: `<component>-<g|h|i>-note`.

## 8. Measured size targets (pass/fail, not commentary)

Measured on scratch copies with the `support.js` line removed, rendered in Chromium at the
artboard's own frame width. **Never measure in the Browser pane** (it reports a zero viewport
and fakes an overflow defect).

| Component | Gate |
|---|---|
| Hero Desktop | **350-400px** root height. Hard fail outside the band. |
| Faq Mobile | **< 1,400px** (live is ~2,404px). All 21 questions still reachable. |
| Shipping | All three tiers present in **all nine** artboards. Content-gated. |
| Table-* Mobile | Stacks. No horizontal scroll as the only answer. |
| Every artboard | `scrollWidth` ≤ frame width (no horizontal overflow). |
| Every Mobile artboard | min font-size ≥12px; min hit-target ≥44px. |
| Every artboard | every text node ≥4.5:1 against its nearest opaque ancestor background. |

## 9. Visual craft gate (round-2 finding 3)

Beyond the numbers, each artboard is reviewed for: a real type scale (not three sizes of the
same weight), 4/8px spacing rhythm, optical alignment, exactly one clay CTA, generous negative
space, and hierarchy that survives a squint test. An artboard that passes every measurement and
still looks flat is a fail.

## 10. Seed + publish (controller only)

```
node "<design skill dir>/seed-canvas.mjs" --template "<design skill dir>/payload.template.html" \
  --out cags-homepage-variations-r3.html --title "C.A.Gs Homepage Components Round 3" \
  --artboard Main.dc.html --artboard <every other .dc.html> … \
  --image <every .webp> … --canvas canvas.json
node "<design skill dir>/seed-canvas.mjs" --check cags-homepage-variations-r3.html
```

Publish with the Artifact tool: `contract: "0.1.31"`, `capabilities: {self:{}, downloads:{}}`
when the roster lists them, favicon `🎨`. **New URL this round** (round 3 is a genuinely new
build, not a re-seed of cf046e8c).

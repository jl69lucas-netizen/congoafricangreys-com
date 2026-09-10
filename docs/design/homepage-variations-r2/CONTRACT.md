# Homepage Component Variations, Round 2 (D / E / F) — Canvas Contract (2026-09-10)

Round 1 (`../homepage-variations/`, canvas `65cdf7d4`) drew variations A/B/C for seven homepage
components. The breeder asked for **three NEW designs per component** (and three per table), so this
round draws **D / E / F**, each a real departure from A, B and C. Same format, same tokens, same
invariants as round 1; only the axes and the hero brief are new. Authors write artboards against THIS
contract; the controller merges, seeds, publishes. Read it fully before writing.

## 1. Canvas shape

`<Component>-<Variation>-<Viewport>.dc.html`, e.g. `Hero-D-Desktop.dc.html`. Variations are **D, E, F**
(never A/B/C). Viewports: Mobile 390 wide, Tablet 768 wide, Desktop 1440 wide. Root element has the
exact frame width. `Main.dc.html` = `Hero-D-Desktop` (the leading candidate) and must exist.

Pages (`canvas.json`, in order): `hero` · `counter` · `dial` · `rail` · `tables` · `faq` · `shipping`.

## 2. The `.dc.html` format (exact, copied from round 1)

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
- Icons: inline SVG, stroke 1.75, 16/20/24 grid. Never emoji.
- Images: bare filename, double-quoted: `<img src="hero-midland.webp">`. Files in this folder:
  `hero-midland.webp` (800×600, the LIVE homepage hero photo: Rony & Rose, "Midland, Texas" sign) ·
  `hero-bird.webp` (700×525) · `bird-1.webp` Evie Timneh (591×640) · `bird-2.webp` aviary pair
  (640×640) · `bird-3.webp` candled eggs (550×688) · `bird-4.webp` Roys Congo (640×800) ·
  `shipping-crate.webp` (640×362) · `shipping-2.webp` (640×426). Always set `width`/`height` attrs
  and `object-fit:cover`. Every `<img>` gets a real alt.
- Every hit target ≥44px on Mobile. Body copy ≤70ch. Minimum text 12px at Mobile (11px only for
  eyebrows that decorate, never for text that carries a fact or a price).
- Validate: `xmllint --html --noout <file>` (no unclosed tags) and every `<img src>` names a file here.

## 3. Brand tokens (locked)

Forest `#2D6A4F` · Forest dark scrim `#0f3d2c` · Aviary dark `#234f3b` · Clay `#e8604c` (large text /
tints / on dark only) · Clay-ink `#c8472f` (solid button fills, white text) · Clay small text on light
`#b04228` · Cream `#faf7f4` · Warm bed `#f6efe8` · Ink `#1f2a24` · Muted `#5b524a` · Dial numeral
`#6b625a` · Line `rgba(60,30,10,.12)` · Green tint `rgba(45,106,79,.08)` · On-dark body `#cfd8d5` ·
On-dark eyebrow `#9fb1ab` · On-dark numeral `#9fc7b0` (active `#c3ded0`). Headings Newsreader 600;
body IBM Plex Sans; eyebrows 11–12px, letter-spacing .12em, uppercase, clay `#b04228` (on dark
`#9fb1ab`). Radii: cards 16–18px, hero media 22px, pills 50px. Shadow warm `0 6px 28px
rgba(60,30,10,.12)`; hero media `0 16px 44px rgba(120,50,20,.18)`. Primary CTA = ONE clay pill per
component (`background:#c8472f; color:#fff; border-radius:50px`). Secondary = 2px outline pill.

## 4. Invariants (verbatim from round 1; never loosen)

1. Palette above; no new colours. 2. Hero/counter separation: a tone shift AND a 1px rule.
3. Desktop hero: **350–400px tall measured on the hero grid at 1440**. 4. Sticky offsets assume a 96px
header; a mobile rail sits at the TOP under the header, never bottom-pinned. 5. Dial rows ≥24px, tag
pill always visible, numerals ≥4.5:1, ring 64px, card 196px wide, row font .74rem, tag `.66rem`.
6. Tables at Mobile stack (cards / toggle / accordion); never a horizontally scrolling classic table as
the ONLY mobile answer. 7. Copy is the live page's copy, lifted verbatim (the round-1 artboards in
`../homepage-variations/` already carry it verified: lift from the matching `*-A-*.dc.html` there);
prices from `data/price-matrix.json`; never a new claim. 8. CITES Appendix I. 9. Congo $1,500–$3,500.
10. One clay CTA per component (a selected-state fill on a tab/toggle is not a CTA). 11. No em dashes
in new copy (lifted copy keeps its own). 12. No `border-left` side-stripe accents. 13. No gradient text.

## 5. The hero brief (breeder, 2026-09-10)

All three new heroes derive from **round-1 Hero B** (`../homepage-variations/Hero-B-*.dc.html`): dark
scrim `#0f3d2c`, copy left, photography right, credential ribbon, clay CTA + outline CTA, "6 Birds
Available Now" pill. New rules on top:

- **Image comes FIRST on Mobile** (and Tablet single-column), above the eyebrow/H1, exactly as the
  for-sale `.chero-media{order:-1}` does. Never copy-first on Mobile.
- **Sizes match the for-sale `.chero` hero** (`src/pages/congo-african-grey-for-sale/index.astro`
  759–782, 1032–1035): grid `min-height:352px; max-height:430px` at Desktop, grid gap 34px, H1
  `clamp(1.5rem,2.9vw,2.15rem)` = **34px at 1440, 24px at 390**, line-height 1.12, letter-spacing
  -.01em; lead `.9rem`(14.4px) line-height 1.55 max 60ch; CTAs `padding:11px 22px; font-size:.88rem`
  (14px); ribbon items 12px 600 with a 1px top rule `rgba(176,66,40,.18)` (on dark use
  `rgba(255,255,255,.18)`), 2×2 grid at Mobile; media radius 22px, shadow `0 16px 44px
  rgba(120,50,20,.18)`, aspect 1280/960 at Desktop and 16/10 at Mobile; padding 18px 0 22px.
- **`hero-midland.webp` is one of the images** in every hero (it is the live hero photo).
- Measured Desktop hero grid height must land in **350–400px**.

H1 (sacred, verbatim): `Congo and Timneh African Grey Breeder in <span style="color:#e8604c;">Midland, Texas</span>`.
Lead, pills, CTAs, the availability pill and bird names/prices: lift from `../homepage-variations/Hero-B-Desktop.dc.html`.

## 6. Variation axes for round 2 (one named axis per variation; never palette)

| Component | D | E | F |
|---|---|---|---|
| Hero (from B) | **Framed portrait**: one large `hero-midland.webp` in the 22px-radius `.chero-media` frame, availability pill overlapping the frame's bottom-left, ribbon under CTAs with the hairline top rule | **Lead photo + pair**: right column = `hero-midland.webp` as a wide tile on top, two square bird tiles (Evie / Roys with caption + price) beneath | **Credential band**: right column = tall `hero-midland.webp` portrait; the four credentials leave the copy column and become a full-width band on `#234f3b` along the hero's bottom edge (still inside the 350–400 grid measure), availability pill sits on the photo |
| Counter | **Icon stat cards**: four white cards, inline SVG icon + numeral + label, on cream | **Green-tint band**: numeral and label side by side in one row, band `rgba(45,106,79,.08)`, forest numerals, vertical hairlines | **Seam card**: the four stats in ONE white pill-card that overlaps the hero/counter seam (negative top margin), warm shadow |
| Desktop dial | **Progress line**: no ring; a 2px vertical track left with numbered 20px nodes, active node clay-filled, part labels as small caps between groups | **Two columns**: 18 rows in two columns of 9 inside one 196→392px-wide card so the dial is ~half the height; rows still ≥24px, tag visible | **Collapsed parts**: active part expanded, the other three collapsed to a header row with a count chip ("6 sections"); chevron SVG |
| Mobile jump links (top rail always) | **Part select + pills**: sticky top rail, a native-looking part `<select>`-styled button left, section pills scroll-x right | **Progress rail**: one-line sticky top bar: current section label, prev/next chevron buttons, 2px clay progress line underneath | **Icon chips**: sticky top rail of scroll-x chips, each a 16px SVG icon + label, active chip forest-filled |
| Tables (×4) | **Column cards**: Mobile = one card per species/option listing every trait; Tablet 2-up cards; Desktop classic columns with the C.A.Gs pick column tinted green | **Banded rows**: trait name as a full-width band, values in a 2-up (or 3-up) grid under it; Desktop the same bands as `<thead>`-less bordered grid | **Accordion rows**: Mobile each trait is a `<details>` row showing the winner inline in the summary; Desktop minimalist hairline table with an SVG check for the leading cell |
| FAQ | **Search-first**: filter input + topic chips, all 21 questions as compact one-line summaries (`<details>`), only the first open | **Quick answers + rest**: 6 "quick answer" cards (question + one-sentence answer, verbatim first sentence) in a grid, remaining 15 in a plain accordion below | **Side-nav**: topic list left (sticky at Desktop), answers right; Mobile = topic pills row + accordion |
| Shipping | **Tier chooser**: two side-by-side tier cards ($185 airport / $350 home) with what-is-included lists and ONE clay CTA under them | **Route**: an inline-SVG route line "Midland, TX → your airport → your door" with the two tiers as nodes, crate photo beside | **Fact grid**: 2×3 definition grid (tier, price, carrier, timing, crate, arrival) beside `shipping-crate.webp` |

The four tables and their round-1 copy sources: `Table-Cvt` (Congo vs Timneh, "Is a Congo or a Timneh
African Grey Right for You?") · `Table-Mvf` ("What buyers ask about · Male · Female") · `Table-Others`
("Species · Talking ability · Noise level · Best for") · `Table-Tblc` ("What Does a Hand-Raised,
Documented African Grey Parrot Cost From C.A.Gs?"). Lift rows from `../homepage-variations/Table-<X>-A-Desktop.dc.html`.

## 7. canvas fragments

Each author writes `canvas.part-<page>.json` = `{"artboards":[…],"annotations":[…]}` for their page.
Rows = variation (D at y=0, E below, F below), columns = Desktop x=0, Tablet x=1520, Mobile x=2368.
Set `h` = measured root height + 5%. ≥160px between rows. One sticky note per variation at the row's
top-left (`x:0, y: rowY-140, w:460`): axis · why (data, not taste) · trade-off; the recommended one
starts `(Recommended)`. Note ids unique, `<component>-<d|e|f>-note`. Text is one string with `\n`.
Every artboard on disk MUST be listed. Do NOT set `page` (the controller stamps it).

## 8. Measuring

`node scripts/design_canvas_probe.mjs <scratchDir> <out.json> docs/design/homepage-variations-r2`
renders scratch copies (support.js line removed) at 390/768/1440 and prints overflow, root height,
min font, hit targets, contrast, and its examined count. Never measure in the Browser pane.

## 9. Seeding (controller)

```
node "<design skill dir>/seed-canvas.mjs" --template "<design skill dir>/payload.template.html" \
  --out cags-homepage-variations-round-2.html --title "C.A.Gs Homepage Variations Round 2" \
  --artboard Main.dc.html --artboard … --image … --canvas canvas.json
node "<design skill dir>/seed-canvas.mjs" --check cags-homepage-variations-round-2.html
```

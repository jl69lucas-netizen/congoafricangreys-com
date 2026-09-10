# Homepage Component Variations — Canvas Contract (2026-09-10)

Every artboard on the variations canvas is one `.dc.html` file in this folder. Subagents author
artboards against THIS contract; the controller seeds and publishes. Read it fully before writing.

## 1. What the canvas is

A `/design` canvas: many artboards on one pan/zoom surface, grouped in pages. One artboard = one
`<Component>-<Variation>-<Viewport>.dc.html`, e.g. `Hero-A-Desktop.dc.html`. `Main.dc.html` is the
leading candidate (Hero-A-Desktop) and must exist. Frames: Mobile 390 wide, Tablet 768 wide, Desktop
1440 wide; height = what the artboard holds (set `h` in canvas.json to the content height + ~5%).

Pages (canvas.json `pages`, in this order): `hero` Heroes · `counter` Counter snippets · `dial`
Desktop dial · `rail` Mobile jump links · `tables` Tables · `faq` FAQ · `shipping` Shipping.

## 2. The `.dc.html` format (exact)

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
    h1,h2,h3 { font-family: Newsreader, Georgia, serif; font-weight:600; letter-spacing:-.003em; }
    a { color:#b04228; } a:hover { color:#c8472f; }
  </style>
</helmet>
<div style="width:1440px; …">  <!-- root element: fixed width = frame width -->
  … markup with INLINE styles (the editor's property panel edits inline styles) …
</div>
</x-dc>
</body>
</html>
```

Rules that bite:
- Keep `<script src="./support.js"></script>` exactly. A static artboard needs NO `<script data-dc-script>`.
- Close every element, double-quote every attribute. Prefer inline `style="…"` over classes for anything a
  viewer should be able to restyle; put shared type/colour rules in `<helmet><style>`.
- Layout with `display:flex` / `display:grid` + `gap` (never margins between siblings, never inline
  whitespace). Grids as `grid-template-columns: repeat(N, minmax(0, 1fr))`.
- No `{{handlebars}}`, no `<sc-for>`, no tweaks: copy is literal text so the viewer can retype it in place.
- Icons: inline SVG (stroke 1.75, 16/20/24 grid). Never emoji.
- Images: reference by bare filename `<img src="hero-bird.webp">` (double-quoted, exact filename, the
  file lives in this folder and is passed to the seeder with `--image`). Keep each image ≤70 KB
  (downsample with Pillow to ≤900px wide, WebP q80). No `data:` URIs, no `/public/...` paths.
- Every hit target ≥44px on Mobile artboards. Body copy ≤70ch.
- Set the root element's exact width; the frame does not scale content.

## 3. Brand tokens (locked; copy the values, never invent)

Forest `#2D6A4F` · Forest dark scrim `#0f3d2c` · Aviary dark `#234f3b` · Clay `#e8604c` (large text /
tints / on dark only) · Clay-ink `#c8472f` (solid button fills, white text) · Clay small text on light
`#b04228` · Cream `#faf7f4` · Warm bed `#f6efe8` · Ink `#1f2a24` · Muted `#5b524a` · Line
`rgba(60,30,10,.12)` · Green tint `rgba(45,106,79,.08)`. Headings Newsreader 600; body IBM Plex Sans;
eyebrows 11–12px, letter-spacing .12em, uppercase, clay `#b04228`. Radii: cards 16–18px, pills 50px,
form submit 12px. Shadows: warm `0 6px 28px rgba(60,30,10,.12)`. Motion ≤0.2s, none needed on artboards.
Primary CTA = ONE clay pill per component (`background:#c8472f; color:#fff; border-radius:50px`).

## 4. Invariants every variation keeps (rules/design.md · skills/cag-component-refresh.md §0)

1. Palette above; no new colours. 2. Hero/counter separation: a tone shift AND a 1px rule between hero
and counter. 3. Desktop hero: **350–400px tall measured on the hero grid at 1440** (the live HeroV3 is
~649px; that is the problem to solve). 4. Sticky offsets assume a 96px header; a mobile rail sits at the
TOP under the header, never bottom-pinned. 5. Dial rows ≥24px tall, tag pill always visible, numerals
≥4.5:1 (`#6b625a` on cream, `#9fc7b0` on `#234f3b`), ring 64px, card 196px wide, row font .74rem.
6. Tables: at Mobile they stack to `data-label` cards, a tab-toggle, or verdict cards; never a
horizontally scrolling classic table as the ONLY mobile answer. 7. Copy is the live page's copy, lifted
verbatim from `dist/index.html` (or `src/pages/index.astro`); prices from `data/price-matrix.json`;
never a new claim; both method labels (*The Benjamin Home-Raising Protocol*, *The Midland Socialization
Method*) may be used where the live page would say them. 8. CITES is Appendix I. 9. Congo range
$1,500–$3,500. 10. One clay CTA per component. 11. No em dashes in new copy.

## 5. Variation axes (one named axis per variation; never palette)

| Component | A | B | C |
|---|---|---|---|
| Hero | Split copy-left + single portrait + credential pill row (Split-Hero B lineage), 350–400 tall | Full-bleed dark scrim + 2×2 photo grid right (Split-Hero C lineage) | Mosaic metrics: stats column + inventory mosaic (Hero-C lineage) |
| Counter | 4-up ledger, hairline rules, clay numerals (tighter current) | 2×2 tiles on `#f6efe8` bed with a 3px forest→clay top bar | Inline ribbon: numerals + labels in one line, horizontally scrollable at Mobile |
| Desktop dial | `.tdial` light cream card, canonical numbers | dark aviary card `#234f3b`, numerals `#9fc7b0` | grouped-by-part dial with part headers (the homepage rail's four parts) |
| Mobile jump links | sticky top rail, single-line pills | sticky top rail, stacked two-line chips | bottom-sheet "Jump to a section" grouped by part, with part chips (current, refined) |
| Tables (×4) | Mobile `data-label` stacked cards · Tablet 2-col cards · Desktop classic | Mobile tab-toggle one column at a time · Tablet/Desktop classic with sticky first column | Mobile verdict cards (trait, two mini-columns, "Our note" strip) · Tablet/Desktop zebra ledger |
| FAQ | grouped accordion with 3 topic tabs, max 4 open | two-column masonry at Desktop, single accordion at Mobile | "top 4 + show all" progressive disclosure |
| Shipping | two photo cards (van / cargo) | timeline strip reserve→vet→fly→arrive with the two tiers as end-nodes | split panel photo left, tier rows right |

The four tables: `table-mvf` (Male vs Female, "What buyers ask about"), `table-others` (Grey vs
Macaw/Cockatoo/Amazon), `table-e` (CompareTableE idiom: Congo vs Timneh), `table-tblc` (hand-raised
`.tblC`). Lift their real rows from `dist/index.html` (first two) and
`dist/congo-vs-timneh-african-grey/index.html`, `dist/hand-raised-african-grey-parrot-for-sale/index.html`.

## 6. canvas.json

```json
{
  "pages": [{"id":"hero","name":"Heroes"},{"id":"counter","name":"Counter snippets"},{"id":"dial","name":"Desktop dial"},{"id":"rail","name":"Mobile jump links"},{"id":"tables","name":"Tables"},{"id":"faq","name":"FAQ"},{"id":"shipping","name":"Shipping"}],
  "artboards": [
    {"file":"Main.dc.html","title":"Hero A · Desktop","x":0,"y":0,"w":1440,"h":420,"page":"hero"},
    {"file":"Hero-A-Tablet.dc.html","x":1520,"y":0,"w":768,"h":640,"page":"hero"},
    {"file":"Hero-A-Mobile.dc.html","x":2368,"y":0,"w":390,"h":900,"page":"hero"}
  ],
  "annotations": [
    {"id":"hero-a-note","x":0,"y":-140,"w":420,"text":"Hero A · axis: layout. Why: … Trade-off: …","page":"hero"}
  ],
  "launch": {"view":"canvas","page":"hero"}
}
```
Rows = variation (A row y=0, B row y = A height + 200, C row below), columns = Desktop, Tablet, Mobile.
≥80px between frames in a row, ≥160px between rows. One sticky note per variation: axis · why (data,
not taste) · trade-off; the recommended variation's note starts with `(Recommended)`. Note ids: 1–40
chars, letters/digits/-/_; text is one string with `\n` newlines. Every artboard file in the folder MUST
be listed (the seeder refuses unlisted files and warns on overlap).

## 7. Copy lifting

`python3 - <<'EOF'` with `re`/`html` over `dist/index.html` to pull: the H1, hero lead paragraph, the
four pills, CTA labels, counter stats, JumpRail sections/parts (from `src/components/cag-library/JumpRail.astro`),
the two homepage tables' rows, FAQ `faqItems` (from `src/pages/index.astro`), shipping copy and the two
tiers ($185 airport · $350 home). Quote exact text; do not paraphrase.

## 8. Seeding (controller runs this; authors only need the files right)

```
node "<design skill dir>/seed-canvas.mjs" --template "<design skill dir>/payload.template.html" \
  --out cags-homepage-component-variations.html --title "C.A.Gs Homepage Component Variations" \
  --artboard Main.dc.html --artboard Hero-A-Tablet.dc.html … --image hero-bird.webp … --canvas canvas.json
node "<design skill dir>/seed-canvas.mjs" --check cags-homepage-component-variations.html
```
Authors: after writing, validate each file with `python3 -c "import html.parser…"` or simply `xmllint
--html --noout` for unclosed tags, and confirm every `<img src>` names a file in this folder.

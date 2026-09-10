# Homepage Tables — Round 4 Canvas Contract (2026-09-10)

Scope: **the four homepage tables only.** Two NEW variations each — **J** and **K** —
× three viewports = **24 artboards**. Nothing else on the homepage is in scope.

Authors write artboards against THIS contract. The controller merges, seeds, publishes,
commits. **No author runs git.**

## 1. What the canvas is

A `/design` canvas: artboards on one pan/zoom surface, grouped in pages. One artboard =
one `<Component>-<Variation>-<Viewport>.dc.html`. `Main.dc.html` is the leading candidate
and must exist (it is a copy of `Table-Cvt-J-Desktop.dc.html`).

Frames: **Mobile 390** · **Tablet 768** · **Desktop 1440**. Height = measured content
height + ~5%, set as `h` in `canvas.json`.

Canvas pages, in this order: `cvt` · `mvf` · `others` · `price`.

## 2. The `.dc.html` format (exact — unchanged from rounds 1-3)

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
  … markup with INLINE styles …
</div>
</x-dc>
</body>
</html>
```

Rules that bite:
- Keep `<script src="./support.js"></script>` exactly. No `<script data-dc-script>` needed.
- Close every element, double-quote every attribute. Inline `style="…"` over classes for
  anything a viewer should restyle; shared type/colour rules go in `<helmet><style>`.
- Layout with `display:flex` / `display:grid` + `gap`. Never margins between siblings.
  Grids as `grid-template-columns: repeat(N, minmax(0, 1fr))`.
- No `{{handlebars}}`, no `<sc-for>`. Copy is literal text so the viewer can retype it.
- Icons: inline SVG (stroke 1.75, 16/20/24 grid). **Never emoji.** The live `✓` / `★` /
  `✔` / `↗` glyphs inside lifted copy are text, not icons — they stay as typed.
- No images needed for these four tables. Do not add any.
- Every hit target ≥44px on Mobile. Body copy ≤70ch.
- Set the root element's exact width; the frame does not scale content.

## 3. Brand tokens (locked; copy the values, never invent)

Forest `#2D6A4F` · Forest dark scrim `#0f3d2c` · Aviary dark `#234f3b` · Clay `#e8604c`
(large text / tints / on dark only) · Clay-ink `#c8472f` (solid button fills, white text) ·
Clay small text on light `#b04228` · Cream `#faf7f4` · Warm bed `#f6efe8` · Ink `#1f2a24` ·
Muted `#5b524a` · Line `rgba(60,30,10,.12)` · Green tint `rgba(45,106,79,.08)`.

Headings Newsreader 600; body IBM Plex Sans; eyebrows 11–12px, letter-spacing .12em,
uppercase, clay `#b04228`. Radii: cards 16–18px, pills 50px. Shadow: warm
`0 6px 28px rgba(60,30,10,.12)`. Primary CTA = **ONE** clay pill per artboard
(`background:#c8472f; color:#fff; border-radius:50px`).

## 4. Invariants every variation keeps

1. Palette above. **No new colours.** The axis is never colour.
2. **Tables stack on Mobile.** A horizontally scrolling classic table is never the only
   Mobile answer. (Breeder instruction, restated 2026-09-10.)
3. Copy is lifted verbatim from `COPY.md` in this folder. **Every row, every column, every
   note.** A redesign never adds or removes content — visual layer only (Rule 7).
4. No new claims. No invented rows. No rounded counts.
5. CITES is **Appendix I**.
6. Congo singles $1,700–$2,500; bonded pair $3,500; Timneh $1,500–$1,600.
7. The guarantee reads **3-day** here. Do not rewrite to "72-hour". Do not flag it.
8. One clay CTA per artboard.
9. No NEW em dashes. Lifted copy keeps the ones it has.
10. No side-stripe accent borders (`border-left:4px solid …`) as decoration. No gradient text.
11. `display:table-caption` is banned on a mobile-stacked table; drop uppercase captions at
    Mobile instead.
12. Mobile min font-size 14px; Mobile min hit-target 44px; every text node ≥4.5:1 against
    its nearest opaque ancestor background.

## 5. Round-4 axes — J and K

**Burned across rounds 1-3 — J/K must NOT return to any of these nine:**
`A` data-label stacked cards · `B` tab-toggle + sticky first column · `C` verdict cards +
zebra ledger · `D` column cards · `E` banded rows · `F` accordion rows · `G` comparison
bars · `H` definition list · `I` pick-first summary.

| | **J — Numbered Spec Index** | **K — Menu Leaders** |
|---|---|---|
| **Motif** | A numeral gutter. Every row carries a two-digit index (`01`…`12`) set in clay, small-caps trait name beside it. Editorial catalogue rhythm — the numbers are the structure. | Dot leaders. Every label is connected to its value by a rule of leader dots, values right-aligned on a common axis. Menu / index typography — the eye tracks the line, not a box. |
| **Desktop** | Boxless. A narrow left gutter column holds the numerals; rows separated by 1px `rgba(60,30,10,.12)` hairlines only. **No zebra, no card, no outer border.** Column heads sit above as small-caps labels with a 2px forest rule under the head band. | Column heads as small-caps caps-line; each row is `label ·········· value` with the leader dots as a `repeating-linear-gradient` or a border-bottom dotted rule filling the flex gap. Values right-aligned. Multi-column tables get one leader run per value column. |
| **Tablet** | Same numeral gutter, numerals drop inline ahead of the trait name; value columns collapse to 2-up where the table has 4-5 columns. | Same leader runs, narrower label column; 4-5 column tables fold the middle attributes to a single muted meta line under the leader row. |
| **Mobile (stacks)** | Each row becomes a numbered entry: `01` numeral + trait as the entry head, values beneath as labelled lines. No cards, no borders — the numeral and a hairline carry the separation. | The densest stack of any round: trait name, then one leader line per value (`Congo ····· ★★★★★`). Target: **shortest Mobile height of any table variation to date** (beat round-1 A's 3,398px on Cvt). |
| **Why it might win** | Scannable, print-editorial, zero JS, no boxes to break at any width, works identically at 2 / 4 / 5 columns. | Answers the measured "table too long on mobile" defect directly; leader lines read as considered typography rather than a shrunken table. |
| **Named trade-off** | Numerals add visual noise a comparison table does not strictly need, and a 12-row table numbered `01`-`12` can read as a checklist rather than a comparison. | Leader dots are fragile: long values wrap and orphan the leader run, and right-aligned prose (the Mvf and Others tables have sentence-length cells) fights the alignment. Needs `min-width` discipline on the label column. |

Both axes must be **layout/typographic**, never a palette swap (`cag-component-refresh.md` §0).

## 6. Copy source

`docs/design/homepage-tables-r4/COPY.md` — lifted verbatim from `dist/index.html` on
2026-09-10 at the offsets recorded there. Never re-derive from `src/`, never paraphrase.

## 7. Canvas fragments

Each author writes ONLY its own artboards plus ONE fragment file.

| Author | Artboards | Fragment | Canvas page |
|---|---|---|---|
| Table-Cvt | `Table-Cvt-{J,K}-{Mobile,Tablet,Desktop}` | `canvas.part-cvt.json` | `cvt` |
| Table-Mvf | `Table-Mvf-{J,K}-{Mobile,Tablet,Desktop}` | `canvas.part-mvf.json` | `mvf` |
| Table-Others | `Table-Others-{J,K}-{Mobile,Tablet,Desktop}` | `canvas.part-others.json` | `others` |
| Table-Price | `Table-Price-{J,K}-{Mobile,Tablet,Desktop}` | `canvas.part-price.json` | `price` |

Fragment shape (`x`/`y`/`w`/`h` in canvas px; `w` = viewport width, `h` = measured root
height +5%; ≥80px between frames in a row, ≥120px between rows):

```json
{
  "artboards": [
    { "file": "Table-Cvt-J-Mobile.dc.html",  "x": 0,    "y": 0, "w": 390,  "h": 1800 },
    { "file": "Table-Cvt-J-Tablet.dc.html",  "x": 480,  "y": 0, "w": 768,  "h": 1200 },
    { "file": "Table-Cvt-J-Desktop.dc.html", "x": 1340, "y": 0, "w": 1440, "h": 900 }
  ],
  "annotations": [
    { "id": "cvt-j-note", "x": 0, "y": -110, "w": 380, "text": "J — Numbered Spec Index. Trade-off: …" }
  ]
}
```

Every author lays J at `y: 0` and K at a `y` clear of J's tallest frame + 120px. Note ids
must be unique across the whole canvas — prefix with the page id (`cvt-`, `mvf-`,
`others-`, `price-`).

## 8. Measuring

Playwright on **scratch copies** with the `<script src="./support.js"></script>` line
removed (that file does not exist locally; a load against it hangs). Render at the
artboard's own frame width. **Never measure in the Browser pane** — it reports a zero
viewport and fakes a horizontal-overflow defect.

## 9. After the breeder picks

One variation per table is applied to `src/pages/index.astro` under Rule 7 — visual layer
only, content unchanged — then: `cag-page-hardening.md` §2 probes at 375/768/1280 ·
`npm run test:render:pages --grep 'index'` · `python3 scripts/seam_parity.py index` ·
`python3 scripts/dup_content_audit.py --headers` · `python3 scripts/evidence_audit.py index`
· build · commit + push · `python3 scripts/indexnow_submit.py ""`.

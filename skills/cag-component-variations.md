---
name: cag-component-variations
description: Use when the breeder wants "3 variations", mobile/tablet/desktop versions of a component, a new hero, a new counter, a new dial, mobile jump links, "table not good on mobile", a design canvas, a component library, or a variations canvas for any CAG page — builds 3 named-axis variations × 3 viewports per component on a `/design` canvas the breeder edits and picks from.
---

# SKILL: CAG Component Variations — 3×3 on a Design Canvas

## 1. What this is

For any component that needs rework (a hero that measures wrong, a counter, a desktop
dial, mobile jump links, a table, an FAQ block, a shipping section), this skill produces
**3 variations × 3 viewports = 9 artboards per component** on one `/design` canvas — a
multi-artboard `.html` published with the Artifact tool that runs Claude Design's canvas
editor. The breeder pans/zooms the canvas, edits artboards visually, and picks the
variation that ships. Nothing is written to `src/pages/` until the breeder approves one
(Rule 7, preview-before-apply).

**Reference first:** `docs/artifacts/cags-component-library.md` — every LIVE component
captured in a real browser at 375/768/1280, with its source file and CSS selector. Read
it before drawing anything new; a variation should look like a deliberate departure from
what already ships, not an accident of not having checked. Regenerate it after any
component change: `node scripts/component_library_capture.mjs` then
`node scripts/build_component_library.mjs` (writes `docs/artifacts/cags-component-library.md`
+ `.html` beside it).

This skill was built from the 2026-09-10 homepage pass: 7 components (hero, counter,
desktop dial, mobile jump links, 4 tables, FAQ, shipping), 90 artboards, at
`docs/design/homepage-variations/`. That folder's `CONTRACT.md` and `CRITIQUE.md` are the
worked example — read them when the written method below is ambiguous.

## 2. Invariants (copied verbatim from `docs/design/homepage-variations/CONTRACT.md` §3–§4 — never re-derive, never loosen)

**Brand tokens (§3):** Forest `#2D6A4F` · Forest dark scrim `#0f3d2c` · Aviary dark
`#234f3b` · Clay `#e8604c` (large text / tints / on dark only) · Clay-ink `#c8472f`
(solid button fills, white text) · Clay small text on light `#b04228` · Cream `#faf7f4` ·
Warm bed `#f6efe8` · Ink `#1f2a24` · Muted `#5b524a` · Line `rgba(60,30,10,.12)` · Green
tint `rgba(45,106,79,.08)`. Headings Newsreader 600; body IBM Plex Sans; eyebrows 11–12px,
letter-spacing .12em, uppercase, clay `#b04228`. Radii: cards 16–18px, pills 50px, form
submit 12px. Shadows: warm `0 6px 28px rgba(60,30,10,.12)`. Motion ≤0.2s, none needed on
artboards. Primary CTA = ONE clay pill per component (`background:#c8472f; color:#fff;
border-radius:50px`).

**Invariants every variation keeps (§4):**
1. Palette above; no new colours.
2. Hero/counter separation: a tone shift AND a 1px rule between hero and counter.
3. **Desktop hero: 350–400px tall, measured on the hero grid at 1440.** The live HeroV3
   measured ~649px on 2026-09-10 — that is the defect this skill exists to fix. The three
   homepage variations A/B/C measured 375 / 389 / 358px, all inside the band.
4. Sticky offsets assume a 96px header; a mobile rail sits at the **TOP** under the
   header, never bottom-pinned (breeder rejected bottom placement 2026-07-23 — see
   `cag-page-hardening.md` §1b).
5. Dial rows ≥24px tall, tag pill always visible, numerals ≥4.5:1 (`#6b625a` on cream,
   `#9fc7b0` on `#234f3b`), ring 64px, card 196px wide, row font `.74rem` (see
   `cag-page-hardening.md` §1e-bis for the canonical `.tdial` metrics this must match).
6. Tables: at Mobile they stack to `data-label` cards, a tab-toggle, or verdict cards;
   never a horizontally scrolling classic table as the ONLY mobile answer.
7. Copy is the live page's copy, lifted verbatim from `dist/<slug>/index.html` (or the
   `.astro` source); prices from `data/price-matrix.json`; never a new claim; both method
   labels (*The Benjamin Home-Raising Protocol*, *The Midland Socialization Method*) may
   be used where the live page would say them.
8. CITES is Appendix I.
9. Congo range $1,500–$3,500.
10. One clay CTA per component.
11. No em dashes in new copy (copy lifted verbatim from a live page keeps whatever it
    already has — do not "fix" an em dash that came from `dist/`).

## 3. Inputs

- The breeder's own screenshots/notes on what's wrong with the live component (if given).
- `docs/artifacts/cags-component-library.md` — what already exists, so a variation is a
  real departure.
- The target page slug (`dist/<slug>/index.html` or `src/pages/<slug>/index.astro`) —
  the copy source and the component's current live markup/CSS.
- `rules/design.md` for the nine non-negotiable visual rules this stacks on top of.

## 4. Method

1. **Lift tokens.** Copy §3 of `CONTRACT.md` verbatim (above) — never invent a color,
   radius, or shadow value.
2. **Pick ONE named axis per variation.** Never rotate on palette. Copy the axis table
   from `CONTRACT.md` §5 (reproduced below for the homepage's 7 components — for a new
   component, write an equivalent 3-row table using the same shape: one axis word per
   variation, never "just smaller/bigger"):

   | Component | A | B | C |
   |---|---|---|---|
   | Hero | Split copy-left + single portrait + credential pill row, 350–400 tall | Full-bleed dark scrim + 2×2 photo grid right | Mosaic metrics: stats column + inventory mosaic |
   | Counter | 4-up ledger, hairline rules, clay numerals | 2×2 tiles on `#f6efe8` bed with a 3px forest→clay top bar | Inline ribbon: numerals + labels in one line, horizontally scrollable at Mobile |
   | Desktop dial | `.tdial` light cream card, canonical numbers | dark aviary card `#234f3b`, numerals `#9fc7b0` | grouped-by-part dial with part headers |
   | Mobile jump links | sticky top rail, single-line pills | sticky top rail, stacked two-line chips | bottom-sheet "Jump to a section" grouped by part, with part chips |
   | Tables | Mobile `data-label` stacked cards · Tablet 2-col cards · Desktop classic | Mobile tab-toggle one column at a time · Tablet/Desktop classic with sticky first column | Mobile verdict cards (trait, two mini-columns, "Our note" strip) · Tablet/Desktop zebra ledger |
   | FAQ | grouped accordion with 3 topic tabs, max 4 open | two-column masonry at Desktop, single accordion at Mobile | "top 4 + show all" progressive disclosure |
   | Shipping | two photo cards (van / cargo) | timeline strip reserve→vet→fly→arrive with the two tiers as end-nodes | split panel photo left, tier rows right |

3. **Write `CONTRACT.md` for the target page** — copy the `docs/design/homepage-variations/CONTRACT.md`
   template structure (What the canvas is → the `.dc.html` format → brand tokens → invariants
   → variation axes table → canvas.json shape → copy-lifting recipe → seeding commands),
   swap in the target page's components, copy sources, and image inventory.
4. **Author one `.dc.html` per variation × viewport**, named
   `<Component>-<Variation>-<Viewport>.dc.html` (e.g. `Hero-A-Desktop.dc.html`). Viewports:
   Mobile 390 wide, Tablet 768 wide, Desktop 1440 wide; set the artboard's `h` in
   `canvas.json` to the measured content height + ~5%. **`Main.dc.html` is the leading
   candidate** (i.e. the file that would be `<Component>-A-Desktop.dc.html` for the
   recommended variation) and must exist. Follow `CONTRACT.md` §2's exact `.dc.html`
   format: `<script src="./support.js"></script>` kept verbatim, inline styles (never
   classes) for anything a viewer should restyle, `display:flex`/`grid` + `gap` layout
   (never margin-between-siblings), literal copy text (no handlebars/templating), inline
   SVG icons (never emoji), images referenced by bare filename and ≤70KB WebP.
5. **Each author writes a `canvas.part-<page>.json` fragment**, not the full `canvas.json`
   — one fragment per canvas "page" (hero, counter, dial, rail, tables, faq, shipping, or
   whatever pages this build needs), so parallel authors never touch the same file.
6. **Merge fragments into `canvas.json`.** The controller runs this 20-line Python merge
   (adjust the page-id list to the build's own pages) — it reads the fragments in page
   order, stamps each artboard's `page`, asserts every `.dc.html` on disk is listed and
   every note id is unique, then writes `pages` / `artboards` / `annotations` / `launch`:

   ```python
   import json, glob, pathlib
   PAGE_ORDER = ["hero", "counter", "dial", "rail", "tables", "faq", "shipping"]
   folder = pathlib.Path("docs/design/<your-page>-variations")
   artboards, annotations, seen_notes, seen_files = [], [], set(), set()
   for page_id in PAGE_ORDER:
       frag = json.loads((folder / f"canvas.part-{page_id}.json").read_text())
       for a in frag["artboards"]:
           a["page"] = page_id
           artboards.append(a); seen_files.add(a["file"])
       for n in frag["annotations"]:
           n["page"] = page_id
           assert n["id"] not in seen_notes, f"dup note id {n['id']}"
           seen_notes.add(n["id"]); annotations.append(n)
   on_disk = {p.name for p in folder.glob("*.dc.html")}
   assert on_disk <= seen_files, f"unlisted files: {on_disk - seen_files}"
   canvas = {"pages": [{"id": p, "name": p.title()} for p in PAGE_ORDER],
             "artboards": artboards, "annotations": annotations,
             "launch": {"view": "canvas", "page": PAGE_ORDER[0]}}
   (folder / "canvas.json").write_text(json.dumps(canvas, indent=2))
   ```

7. **Seed + check.** The `/design` skill invocation prints its own skill dir — use that
   path in place of `<design skill dir>` below:

   ```
   node "<design skill dir>/seed-canvas.mjs" --template "<design skill dir>/payload.template.html" \
     --out <your-canvas-name>.html --title "<Title>" \
     --artboard Main.dc.html --artboard <every other .dc.html file> … \
     --image <every image file> … --canvas canvas.json
   node "<design skill dir>/seed-canvas.mjs" --check <your-canvas-name>.html
   ```

8. **Publish with the Artifact tool** — `contract: "0.1.31"`, `capabilities: {self: {}, downloads: {}}`
   when the runtime roster lists them, favicon `🎨`. Update the existing canvas artifact
   in place (pass its `url`) on any re-seed; mint a new URL only for a genuinely new
   component build.
9. **Critique/harden/refine pass**, the same three lenses run in `CRITIQUE.md`:
   - **Critique** — brand register, hierarchy, cognitive load, affordance, copy fit,
     honesty (does the artboard assert something the page doesn't actually show).
   - **Harden** — overflow, box fit, hit targets, text size, contrast, well-formedness.
   - **Refine** — type scale, 4/8px rhythm, one clay CTA, alignment.
   Run the probe script (scratch copies with the `support.js` line removed, rendered in
   Chromium at each file's frame width) reporting: `scrollWidth` vs frame width
   (overflow), root height, minimum Mobile font-size, minimum Mobile hit-target height,
   and a WCAG contrast sweep of every text node against its nearest opaque ancestor
   background. The probe must print its own examined count — a probe that reports PASS
   having measured zero files is the exact failure `cag-gate-integrity.md` exists to
   catch. Write findings to a `CRITIQUE.md` beside the `CONTRACT.md`, in the same table
   shape: Variation | Lens | Finding | Fix or open question | File, plus a Counts section
   and a Probe totals before/after table.
10. **Breeder picks one variation per component.** Apply it to the live page under
    Rule 7 (preview-before-apply) — a redesign never adds or removes content, visual
    layer only.

## 5. Parallel authoring rule

Authors (subagents or humans) write **disjoint files**: their own `.dc.html` artboards and
their own `canvas.part-<page>.json` fragment. **No author commits.** Only the controller
merges fragments into `canvas.json`, seeds, and commits. Run every `git` command from the
**repo root** — a `cd` into the design folder breaks repo-relative `git add` paths (this
happened during the 2026-09-10 homepage build).

## 6. Measuring

Measure with Playwright on **scratch copies** of each `.dc.html` with the
`<script src="./support.js"></script>` line removed — that file does not exist locally and
a load against it will hang or error. Render at the artboard's own frame width (390 / 768
/ 1440). Set `h` in `canvas.json` to the measured root height **+5%**. **Never measure in
the Browser pane** — it reports a zero viewport, which fakes a horizontal-overflow defect
(`reference_hidden_pane_zero_viewport`).

## 7. Pass gates before apply

Run these on the live page **after** the breeder's pick is written to `src/pages/`, before
calling the page done:
- `cag-page-hardening.md` §2 runtime probes at 375/768/1280 (overflow, contrast sweep,
  §2c component sizing sanity — hero 350–400px, dial fits without inner scroll, card CTAs
  hug their label).
- `npm run test:render:pages` scoped to the page: `--grep '<slug>'` (test titles are
  slugs; the homepage's slug is `index`).
- `python3 scripts/seam_parity.py <slug>`.
- `python3 scripts/dup_content_audit.py --headers`.
- `python3 scripts/evidence_audit.py <slug>` (the applied copy is still the live page's
  copy — confirm the evidence pass still holds after the visual change).

## 8. What NOT to do

- Palette changes as a "variation" — the axis is layout/accent-role/motif, never colour
  (see `cag-component-refresh.md` §0, invariant 1 above).
- Bottom-pinned mobile rails, in any variation — rejected outright 2026-07-23.
- A density pass that shrinks dial rows below 24px or tag pills below `.66rem` — the
  breeder's own words on the rejected 2026-07-23 pass: *"I can hardly read the text or
  click."*
- Emoji icons anywhere on an artboard — inline SVG only.
- New claims or paraphrased copy — copy is lifted verbatim from the live page or it isn't
  used.
- Side-stripe accent borders (`border-left:4px solid …`) used as decoration — banned
  outright, found and fixed on `Shipping-B` 2026-09-10.
- Gradient text.
- `display:table-caption` on a mobile-stacked table — drop uppercase captions at mobile
  instead (`reference_table_caption_mobile_stacking`).
- Inventing rows or sections to hit a round count — the homepage rail has 18 sections in
  its dial, not 20; match what the page actually has, not a tidier number.

## 9. Record

Variations canvas (2026-09-10): https://claude.ai/code/artifact/65cdf7d4-d24b-45b4-a8ba-b5bbd142fe15

The 2026-09-10 homepage build's canvas and reference material live at:
- `docs/design/homepage-variations/CONTRACT.md` — the canvas contract (worked example for
  §4 above).
- `docs/design/homepage-variations/CRITIQUE.md` — the critique/harden/refine findings and
  the recommended-per-page verdicts.
- `docs/design/homepage-variations/canvas.json` + `canvas.part-*.json` (7 fragments) + 90
  `.dc.html` artboards + 7 images — the worked artboard set.
- `docs/design/homepage-variations/cags-homepage-component-variations.html` — the seeded
  canvas payload as published.
- `docs/artifacts/cags-component-library.md` → artifact
  [`6be797ba`](https://claude.ai/code/artifact/6be797ba-d2bf-4cb8-b8e2-601cbade03d2) — the
  reference component library (38 components, 104 captures) this build was drawn against.

**Recommended per component** (from `CRITIQUE.md`, all measured, not asserted):
- **Hero: A — contested, argue for B.** A is the breeder-marked pick (zero re-approval
  cost, live HeroV3:b lineage measured down); B is the honesty-lens case (names four real
  birds with two verified prices instead of asserting "6 Birds Available Now" beside one
  portrait) and measures only 38px taller at Mobile than A. This is a breeder call, logged
  in `hero-a-note`.
- **Counter: A — confirmed.** 172px desktop vs B's 234px; the live counter strip
  tightened, so it carries no copy risk on the highest-traffic surface.
- **Desktop dial: A — confirmed.** Numerals measure 5.97:1 (highest of the three); it is
  the shipped `.tdial` geometry verbatim.
- **Mobile jump links: A — confirmed**, on the bottom-pin rejection rule rather than a
  number; C's bottom-sheet trigger reintroduces exactly the placement the breeder rejected.
- **Tables: A — confirmed, cost stated.** Needs no JavaScript, but its Congo-vs-Timneh
  mobile stack runs 3,398px against B's 1,661px — a 1,737px difference the breeder may
  weigh differently.
- **FAQ: C — confirmed.** Shortest at Mobile (1,434px vs A's 1,644px and B's 1,970px),
  exactly where the "section too long" complaint was filed.
- **Shipping: B — confirmed, note corrected.** Folds the existing five-step delivery flow
  in rather than duplicating it; second-shortest at both Tablet and Desktop, not shortest
  (the note originally over-claimed this and was fixed during the pass).

## Page Board mode (2026-09-12)

When a page has `data/pages/<slug>/board.json`, the copy source is the **section record**, not
`dist/<slug>/index.html`. `scripts/board_canvas.py <slug>` emits the option artboards from the
record (candidates from `data/component-ledger.json` pools minus what siblings own), and
`scripts/board_thumbs.mjs <slug>` cuts the thumbnails the board shows. Never lift copy from a
sibling or from `dist/` for a boarded page; a text tweak on the canvas is written back into the
record by `scripts/board_approve.py`. Spec: `docs/superpowers/specs/2026-09-12-page-board-system-design.md`.

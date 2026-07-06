# CAG Responsive Image Implementation — APPROVED (2026-07-06)

**Approved by breeder via visual companion (`/_imglab/` lab, real Kent ♂ portrait + Evie ♀ landscape).**
Default = **Option 2 Adaptive Orientation**. Fallback = **Option 3 Contain-on-Canvas** for awkward
square/tight shots. This is the source of truth for the male-vs-female build and the forthcoming
`cag-responsive-image` skill (to be packaged via skill-creator AFTER images are integrated + page built).

Solves the two recurring congo-vs-timneh failures: (1) bird heads cropped on mobile, (2) images too
long/large on desktop. Builds on the congo-vs-timneh `.portrait` lesson + responsive `-760.webp` rule.

---

## Rule 1 — Tag every image by intrinsic orientation
Before placing any image, check its intrinsic dimensions (`python3 -c "from PIL import Image; ..."`):
- **ratio < 0.95** (taller than ~square) → `portrait`
- **ratio ≥ 0.95** → `landscape` (includes all 16:9 Gemini infographics + 4:3 lifestyle + OG landscapes)

## Rule 2 — DEFAULT system (Option 2 Adaptive Orientation)

```css
.sec-img{display:block;border-radius:14px;border:1px solid var(--border, #ede5dc)}

/* LANDSCAPE — full-width editorial cover */
.sec-img.landscape{width:100%;aspect-ratio:4/3;object-fit:cover;object-position:center}
@media(min-width:768px){ .sec-img.landscape{aspect-ratio:16/9} }
@media(min-width:1025px){ figure.land{max-width:760px;margin:0 auto} }

/* PORTRAIT — capped 3:4 card, head never cropped out */
.sec-img.portrait{width:100%;max-width:300px;margin:0 auto;aspect-ratio:3/4;
  object-fit:cover;object-position:center top}
@media(min-width:768px){ .sec-img.portrait{max-width:340px} }
@media(min-width:1025px){ .sec-img.portrait{max-width:400px} }
```
- Portrait `object-position:center top` keeps the head; verified full body+tail+head on Kent (400×533).
- Desktop caps (portrait 400px / landscape 760px) kill the "too-large on desktop" problem.
- Per-bird override allowed: some birds crop better `center` or a custom `object-position` — set per image (congo-vs-timneh lesson: Evie card = `object-top`).

## Rule 3 — FALLBACK system (Option 3 Contain-on-Canvas)
Use ONLY when a photo is square/awkwardly framed and the 3:4 portrait crop still clips something
important. Whole subject always visible, letterboxed in brand cream:
```css
.canvas{background:var(--cream,#faf7f4);border:1px solid var(--border,#ede5dc);border-radius:14px;
  aspect-ratio:4/3;display:flex;align-items:center;justify-content:center;overflow:hidden;padding:6px}
.canvas img{max-width:100%;max-height:100%;object-fit:contain;border-radius:8px}
@media(min-width:768px){ .canvas{aspect-ratio:16/9} }
@media(min-width:1025px){ figure.contain{max-width:760px;margin:0 auto} }
```

## Rule 4 — Responsive delivery on EVERY image (Lighthouse "improve image delivery")
Every image ≥760px wide ships a `-760.webp` sibling (Pillow LANCZOS q82) +:
```html
srcset="/name-760.webp 760w, /name.webp 1408w"
sizes="(max-width:900px) 92vw, 760px"
```
Gemini infographics are generated 1408×768 / 1600×900 → always landscape branch + 760 sibling.

## Rule 5 — Image-SEO 5-element on every image (per IMAGE-DESIGNS §6 + memory)
filename (SEO) · alt ≤190 · title · caption+CTA · 250-word description.

## Breakpoint summary (the 9 approved cells)
| | Mobile ≤767 | Tablet 768–1024 | Desktop ≥1025 |
|---|---|---|---|
| Portrait | 3:4 card, 300px, head-top | 3:4, 340px | 3:4, **400px** |
| Landscape | 4:3 cover full-width | 16:9 cover full-width | 16:9 cover, **760px** |
| Fallback (square) | 4:3 cream canvas, contain | 16:9 canvas, contain | 16:9 canvas 760px, contain |

## Cleanup note
`public/_imglab/` is a throwaway visual-companion harness — delete before final deploy/sitemap.

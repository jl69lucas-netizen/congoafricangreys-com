# Timneh Pages — Per-Section Image Map (zero reuse) — 2026-06-22

Every section gets a DISTINCT image. No image appears twice on a page (the Bery 8×-reuse mistake).
Hero is an IMAGE (no bird video supplied; the shared Maxy talking video stays in the Talking section only).
Deployed (SEO-renamed, WebP-optimized) under `public/birds/elad/` and `public/birds/evie/`.

## ELAD — `/available/elad/` (Male Timneh, now $1,600 · was $2,200 starting price · $200 deposit · 6 months)

| Section (Roys slot → outline header) | Deployed image | Type |
|---|---|---|
| HERO (image, not video) | `/birds/elad/elad-timneh-african-grey-male-hero.webp` | real photo (young bird on hand, looking up) |
| At-a-glance snapshot | `/birds/elad/elad-at-a-glance-card.webp` | infographic (MEET ELAD card — see NOTE) |
| Temperament/personality ("What is Elad like…") | `/birds/elad/elad-personality-profile.webp` | infographic (5 rating bars) |
| Talking → "What shapes vocabulary / stands out" | `/birds/elad/why-elad-stands-out.webp` | infographic |
| Talking → H4 "compare to a Congo's" | `/birds/elad/timneh-vs-congo-african-grey-infographic.webp` | infographic (Timneh vs Congo) |
| Price-counter (tameness proof) | `/birds/elad/elad-hand-fed-timneh-tame.webp` | real photo (head scratch / hand-fed) |
| Documentation | `/birds/elad/elad-timneh-documentation-packet.webp` | infographic (doc flat-lay) |
| Included → package overview (top figure) | `/birds/elad/elad-timneh-package-included.webp` | infographic (package card — see NOTE) |
| Included → "what comes home" checklist (right) | `/birds/elad/elad-what-comes-home-checklist.webp` | infographic (checklist) |
| Decisions sidebar | *(no image — assets exhausted; keep text-only)* | — |
| Lifestyle sidebar ("life over decades") | `/birds/elad/timneh-vs-congo-real-photo.webp` | real photo (two greys; caption ties to variant choice) |
| Training | *(no image — text-only)* | — |
| Food | `/birds/elad/elad-timneh-african-grey-eating.webp` | real photo (eating a peanut) |
| Parents (Levi × Rily) | `/birds/elad/levi-rily-timneh-parents.webp` | real photo (the Timneh pair) |
| Shipping | `/birds/elad/timneh-shipping-delivery-infographic.webp` | infographic |
| Gallery tile 1 | `/birds/elad/elad-timneh-african-grey-wings.webp` | real photo (wings spread) |
| Gallery tile 2 | `/birds/elad/elad-timneh-african-grey-head-scratch.webp` | real photo |
| Gallery tile 3 | `/birds/elad/elad-evie-timneh-siblings.webp` | real photo (Elad + Evie together) |

ALL 15 ELAD-folder assets used + shared parents pair. ✓

## EVIE — `/available/evie/` (Female Timneh, now $1,500 · was $2,200 starting price · $200 deposit · 6 months)

| Section | Deployed image | Type |
|---|---|---|
| HERO (image, not video) | `/birds/evie/evie-timneh-african-grey-female-hero.webp` | real photo (perch profile) |
| At-a-glance snapshot | *(text dl only — Evie has no portrait at-a-glance card)* | — |
| Temperament/personality ("What is Evie like…") | `/birds/evie/evie-personality-fit-card.webp` | infographic (IS EVIE RIGHT FOR YOU) |
| Talking → H4 "compare to a Congo's" | `/birds/evie/timneh-vs-congo-african-grey-infographic.webp` | infographic |
| Price-counter / hand-rearing proof | `/birds/evie/evie-timneh-hand-feeding.webp` | real photo (hand-feeding babies) |
| Documentation | `/birds/evie/evie-timneh-documentation-packet.webp` | infographic (doc packet) |
| Included → package overview (top) | `/birds/evie/evie-timneh-package-included.webp` | infographic (WHAT COMES WITH EVIE $2,200 card — see NOTE) |
| Included → checklist (right) | `/birds/evie/evie-what-comes-home-checklist.webp` | infographic |
| Lifestyle sidebar | `/birds/evie/evie-timneh-african-grey-bath.webp` | real photo (bath/playful) |
| Food | *(no image — text-only; no eating photo)* | — |
| Parents (Levi × Rily) | `/birds/evie/levi-rily-timneh-parents.webp` | real photo (shared pair) |
| Shipping | `/birds/evie/timneh-shipping-delivery-infographic.webp` | infographic |
| Gallery tile 1 | `/birds/evie/evie-timneh-african-grey-portrait.webp` | real photo |
| Gallery tile 2 | `/birds/evie/evie-baby-timneh-african-grey.webp` | real photo (baby) |
| Gallery tile 3 | `/birds/evie/evie-timneh-african-grey-playful.webp` | real photo (with flockmate) |

**NOT used (flagged, not silently shipped):**
- `USE THIS AS EVIE PROFILE.webp` — visually prints **"ELAD'S PERSONALITY PROFILE"** → would put the wrong bird's name on Evie's page. Evie's personality slot uses `is-evie-right-for-you.webp` instead. Recommend breeder regenerate as a true "EVIE'S PERSONALITY PROFILE" card.
- `what-comes-with-evie.webp` — byte-identical duplicate of `meet-evie.webp` (already used).

## NOTE — price/species text inside the supplied infographics
Per breeder (2026-06-22): use as-is; frame the printed figure as the OLD/starting price.
- `elad-at-a-glance-card` & `elad-timneh-package-included` print "$2,300" and the words "Congo African Grey."
- `evie-timneh-package-included` prints "$2,200".
On-page text + figcaptions state the CURRENT price plainly (Elad $1,600 / Evie $1,500) and frame $2,200 as the previous Timneh starting price. The in-image "Congo" label on Elad's at-a-glance card is a known residual to regenerate later (logged in session brief FLAG 1).

## Gallery card refresh (Jins & Jeni design — applies to all 3 pages incl. future hub)
Gallery tiles use: `aspect-[4/5]`, `bg-cream`, `object-contain` (NOT object-cover) so the whole bird shows on a cream field without edge-cropping. (Roys used object-cover — this is the refresh.)

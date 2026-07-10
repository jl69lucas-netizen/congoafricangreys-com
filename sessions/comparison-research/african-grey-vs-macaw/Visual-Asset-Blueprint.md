# Visual Asset Blueprint — /african-grey-vs-macaw/

Every H2 and H3 needs an image (hard gate). Source key: **REAL** = provided photo on disk, **SITE** = reuse existing live site asset, **AI** = generate via Gemini/Nano Banana (`scripts/generate_nb_image.sh`) after outline sign-off, per confirmed answer to source remaining slots this way.

## Provided real photos (`assets/COMPARE-PAGES/GREY-vs-MACAW/`, 12 files / 11 species)
Blue-and-Gold, Camelot, Catalina, Green-winged, Hahn's, Hyacinth, Military (×2, pick sharper crop), Mini, Ruby, Scarlet, Severe — all single-macaw shots (no Grey present in frame; mixed provenance, some look like real pet snapshots (Scarlet: indoor hand-hold with cage visible), some studio/stock-style (Blue-and-Gold, Hyacinth: bokeh outdoor). Alt text and captions must not imply these are C.A.Gs-owned birds — they illustrate the species being compared, not our inventory.

## Hero
**SITE** `congo-african-grey-red-tail-comparison-hero(-480).webp` (existing Grey portrait, same one used in the CvT/cockatoo hero pattern) staggered with **REAL** Scarlet or Blue-and-Gold macaw photo + vs roundel. Two options mocked in the visual companion artifact — awaiting sign-off (Option B / Blue-and-Gold recommended).

## Species subsections (H2-7, 11 H3s)
1:1 with the 11 REAL photos above — no AI needed, no gaps.

## AI-generate (after outline approval)
- Bite Force Matrix graphic (Macaw vs Grey vs Human, Newtons + PSI)
- Decision flowchart / "Which Bird?" visual for the lifestyle-quiz section
- Nutritional comparison graphic (calcium/UV-B vs fat/Brazil-nut)
- Any H2 lacking a natural SITE/REAL asset once the section-builder pass is underway

## Reuse from existing site assets (no macaw-specific photo needed)
- Shipping section: `african-grey-home-delivery-pet-van.webp` / `african-grey-airport-live-animal-shipping.webp` (site-wide shipping pair)
- CITES section: existing documentation flat-lay or Mark/Teri credential photo
- Available-birds cards: live photos from `data/clutch-inventory.json` bird entries
- Author/trust box: Mark & Teri portrait already used on CvT/cockatoo

## Format rules (per DESIGN.md / IMAGE-DESIGNS.md)
16:9 1600×900 hero → 760×400 slot with srcset; species-card photos check intrinsic aspect before applying `.sec-img` (square/portrait sources need the `.portrait` or `.portrait-tall` modifier per the finishing-pass reusable classes — several of the provided macaw photos are close-up portrait crops, verify each before placing). 5-element image SEO (filename, alt ≤190, title, caption+CTA, 250-word description) on every image at build time.

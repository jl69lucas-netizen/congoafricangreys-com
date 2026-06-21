# Session Brief — 2026-06-21

## Done this session
- **llms.txt** reformatted to llmstxt.org spec (single H1, `>` summary, markdown links). Written to `public/` + `site/content/`. Committed `50398b2`, pushed/deployed.
- **WebMCP** — explained to breeder (no build; spec not finalized, treat as future decision).
- **Roys** `/available/roys/` brought to Heading Outline Gate (H4:12 H5:5 H6:5, no skips) by mirroring the approved Amie sibling structure. Verified in `dist/` via `final_page_audit.py --birds` → PASS-WITH-WARNINGS (same warnings as Amie). Committed `0f4441e`, pushed/deployed.

## In progress — expand 4 lean bird pages to FULL Roys standard
Breeder approved (2026-06-21): bery, jins-jeni, elad, evie → full Amie/Roys template (currently lean: 8 H2 / 12 H3 / no H4–H6, all FAIL the gate).

Inventory facts (from clutch-inventory.json):
- bery — Congo, female, $1,700, available. Photo: `assets/brand/BERY -1 year female african grey parrot.webp`
- jins-jeni — Congo PAIR, $3,500, available → needs AggregateOffer (2 birds), pair framing. Photos: `assets/brand/jins-jeni-congo-african-grey-parrot-pair-for-sale-bonded-birds.jpg.webp`, `...-talking-birds.webp`
- elad — Timneh, male, $1,600, 5 mo. Photo: `assets/brand/ELAD - Timneh african grey for sale - male 5 months.webp`
- evie — Timneh, female, $1,500, 6 mo. Photo: `assets/brand/EVIE- Timneh African Grey parrot female 6 months.webp`

Design decisions:
- elad & evie (Timneh siblings) parents = the Timneh pair, photo `assets/brand/Timneh Greys-PAIR.webp`. Breeder wants a DIFFERENT parent-card visual on the Timneh pages so they look distinct from the Congo James&Lois card.
- jins-jeni is a PAIR → single AggregateOffer + two-bird framing, NOT single Product/Offer (the one structural departure from the Roys single-bird template).
- Talking section: Congo framing for bery/jins-jeni; Timneh framing for elad/evie (Timnehs start talking earlier).
- Build order: bery (closest to Amie = Female Congo) → elad → evie (Timneh card variant) → jins-jeni (pair, last, most different).
- Per-page Heading Outline Gate: show full H1→H6 outline + get approval BEFORE each page's code.

## Parents (breeder-confirmed 2026-06-21)
- Bery → parent **Abby (11 yo)** — single grey, chat image 1. Bery is NOT a sibling of Amie/Roys (different parent line). Strip sibling framing.
- Jins & Jeni → parents **Macy (6 yo)** & **Letis (4 yo)** — chat image 2. Jins & Jeni are an UNRELATED pair, must be adopted together: Jins (male, 6 mo) + Jeni (female, 4 mo), both hand-raised with full social training. Tagline: "Two birds, one bond. They go together — and so do you."
- Elad & Evie (Timneh) → the Timneh pair, `assets/brand/Timneh Greys-PAIR.webp`; use a distinct parent-card visual.
- Give all parents real personalities in copy (breeder-authorized, CITES-safe).

## Bery — BUILT (not yet committed/pushed), 2026-06-21
Full Roys standard via Amie port. Verified: final_page_audit.py --birds → PASS-WITH-WARNINGS, H4:12 H5:5 H6:5, no skips. Age reframed ~1yr, price $1,700, §Parents=Abby (mother, 11). Comparison table + reserve-form AMIE leak fixed. Images: bird-specific = Bery's real photo; generics = shared CAG stock. HOLDING push until Abby photo exists (avoid deploying a 404 parent image).

## Open Flags
1. **Parent image files** — Abby and Macy & Letis photos were pasted in CHAT (can't be written to disk by the assistant). Need them saved as files:
   - Abby → `public/birds/bery/bery-parent-abby.webp`
   - Macy & Letis → `public/birds/jins-jeni/jins-jeni-parents-macy-letis.webp`
   Until saved, those parent-card <img> 404. Page otherwise complete.
2. **Bery section images** — Bery has ONE real photo; build reuses it for bird-specific slots + shared generic CAG stock (diet/shipping/map) elsewhere. Same constraint will apply to elad/evie/jins-jeni.

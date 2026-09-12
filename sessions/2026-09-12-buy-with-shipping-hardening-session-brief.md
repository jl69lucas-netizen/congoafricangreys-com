# Session Brief — 2026-09-12 · Buy-With-Shipping Hardening (Page A)

**Goal:** harden, critique and polish every component of `/buy-african-grey-parrots-with-shipping/` from the hero to the form; run the SEO / AEO / GEO / evidence / anti-AI passes as on the other for-sale pages; report the Page Board status.
**Scope:** visual layer, headers and openers only. No section added or removed. The contact form fields stay on the 2026-09-11 contract.
**Gates:** hardening scan, seam parity, dup body + headers, evidence, AEO, final page audit, render meta, render pages (this slug), Playwright probes at 375 / 768 / 1280, live 200, IndexNow.
**Done means:** every gate clean or explained, deploy live, IndexNow 200, gate report as Artifact + `.md`.

## Committed
- `685b42ec` fix(for-sale): buy-with-shipping hardening. Pushed, deploy live at 12:5x, IndexNow HTTP 200.
- Gate report: `docs/artifacts/cags-buy-with-shipping-hardening-gate-report.{html,md}` → https://claude.ai/code/artifact/8f5c4692-690e-4de0-a835-77d62d9ffe44

## What changed (measured, not estimated)
| Component | Before → after |
|---|---|
| Hero 768 | 1051px stacked → 528px two-column; ribbon 2×2 below 980; 400w hero candidate with matching `sizes` + preload |
| Dial 1280 | 7 of 10 rows wrapped (one 74px) → 10 × 29px, dial 408px; label + tag budget is **130px** at 196px sidebar |
| Boarding pass | body-link underline on every stub removed; 890 → 436px at 375 (two compact columns) |
| Bird cards ≤640 | 2-up with hidden blurb → one per row, full-width photo, blurb shown (playbook §3) |
| H3 blocks | 18 H3s prose-first → image-first (`layout-h3-image-first`); the regex hoisted one deeper image and was undone from HEAD |
| AEO | breeder name once (licence section); 3 stat-bearing headers; 4 BLUF openers |
| Evidence | hatch-band 4 → 1; 5 prose runs shared with health-guarantee reworded |
| Rhythm | "rather than" 31 → 11 |

## Gates (final)
hardening 0/0 · seam 10/11 · dup body PASS · dup headers PASS · evidence 0/0 · aeo 0 ERROR (3 footer BLUF WARNs) · final PASS-WITH-WARNINGS (`no_aggregateoffer`, checker) · render meta 296 passed / 34 skipped · render pages 3/3 (run 1 had 1 blocking IMG row at 768 from my own hero change; fixed with the 400w candidate). Remaining advisory rows are sitewide components: `mobile-section` (Header.astro), breadcrumb `›` 2.38:1 (Breadcrumb.astro), and the data-rendered bird list in the form aside.

## Probes that lied (recorded for the learning loop)
1. Scroll-spy probe read mid-animation under `scroll-behavior:smooth`; force `auto` and wait 600ms.
2. Element screenshots fire before the hero decodes at 1280 and 375; wait ~700ms or check `img.complete`.
3. The contrast sweep walked past a `linear-gradient` background to the cream page; stop at `backgroundImage !== none`.
4. The sticky site header overlays the top of an element screenshot and looks like a cropped photo.
5. My own `.78rem` = 12.48px, under the 12.5px floor; caught by the min-font probe.

## Open Flags
- **Mobile section order:** the boarding pass could move below the bird grid on phones (rail already jumps); needs a preview and a breeder call.
- **Confirm-cell / confirm-email** friction stays with the form contract's five open breeder calls.
- **`no_aggregateoffer`** fires on every for-sale page that ships `AggregateOffer` inside `@graph`: harness fixture + fix, no page edit.
- **Page Board system:** still no spec; A shipped through the old lane. B is next, hub gets the first board.

## What's Next
1. Page B `/african-grey-parrots-for-sale-near-me/` build (currently FAIL on `final_page_audit`: no H4–H6, no shipping line, no hero).
2. Resume the Page Board brainstorm → spec `docs/superpowers/specs/2026-09-1x-page-board-system-design.md`.
3. Harness: `known_broken` fixture for `no_aggregateoffer`; Header `mobile-section` orphan class; breadcrumb separator contrast.

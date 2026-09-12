# Hub C Build Gate Report — the first page through a Page Board

Source of truth is this file; the Artifact copy is generated from it.

## 1. Verdict
**PASS-WITH-WARNINGS, shipped.** `/african-grey-parrots-for-sale/` went from a 16 KB near-me lookalike (7 H2s, a state grid, a city grid, no H3–H6) to the for-sale cluster's hub: nine sections from a breeder-approved board record, the full H1–H6 band (9 · 34 · 13 · 9 · 7), six live birds with printed prices, `AggregateOffer` over the set with a `Product` per bird inside an `ItemList`, two `OfferShippingDetails` nodes, and **no state enumeration** — four geo slugs are referenced in total, the router owns the grid.

Every text gate is clean on the shipped build: hardening 0 ERROR / 0 WARN, seam parity PASS (9 seams, 10 sections, form and FAQ share one), dup body and dup headers clean after six rewrites, evidence 0 ERROR with four per-slug overrides recorded, AEO 0 ERROR, final page audit PASS-WITH-WARNINGS on the same two rows every for-sale sibling carries, render meta 296 passed, render pages **3 of 3** at 375 / 768 / 1280 on the first run. Board gate at release: 0 FAIL, 4 WARN.

Live: 200 with the rebuilt page serving; IndexNow 200 for the hub. The singular `/african-grey-parrot-for-sale/` returns a live 301 to the hub. The three retiring near-me pages and the flattened "gray" spelling rule all return live 301s to the router, and the whole site was resubmitted to IndexNow after the footer change: 99 URLs, HTTP 200.

## 2. What was built, from the approved record
| Axis | Board pick | Shipped as |
|---|---|---|
| Hero | Hero-C Mosaic Metrics, refreshed `#inventory-tiles` | Deep-green field, three-metric strip, the mosaic OG photo at 16:9 with caption, four tiles reading live inventory (Congo singles · Timneh singles · companion pair · total) that jump to the cards; image first on phones by CSS order |
| Dial + rail | Dial 2 Dark Aviary + Rail A price chip | 9 rows with a tag each; rail sticky under the header on tablet and phone |
| §1 birds | avail-a-grid | A plain three-column card grid, no facet sidebar (Avail-A had no prior implementation; this is its definition). Photo, name, price, blurb, three chips, shipping line, reserve button and a link to the bird's own page. 2-up at tablet, 1-up on phones |
| §2 which | table-a-stacking | Five-row Congo / Timneh fork (weight, tail, beak, price band, available now) from `price-matrix.json`, clay header, stacks to cards under 640; the side-by-side chart image above it |
| §3 price | k2-price-tag | Split tag ($1,500–$3,500) with four rows; the receipt HTML infographic below the prose |
| §4 route | timeline-strip | Three-step strip derived from the T5 stepper's bones (certificate → flight → handover); the "how a grey gets home" map image |
| §5 papers | lab-report-table | Six-row document register (what it holds · why it exists), caption band, stacks to cards under 640; the redacted sample flat-lay with its required caption |
| §6 who | split-feature | Sticky photo (the handwritten Midland sign) beside the breeder text and a four-line checklist; both method labels defined once |
| §7 next | toc-t3-boarding-pass, refreshed `#spoke-index` | 18 boarding-pass stops, one per spoke, six-column desktop, two-column phone |
| §8 FAQ | faq-c, refreshed `#spoke-links` | Twelve questions, dark register, index chip instead of the $ glyph, answers capped at 70ch |
| §9 reserve | inline form, full contract | Two-pane form: live birds and shipping line on the left, the seven-field contract with screening questions on the right; 16px controls, 44px pills, honeypot |
| Takeaways | K1 receipt + K2 price tag | K1 "What you are looking at" with six rows at the top of the content column; K2 in §3 |
| H6 prefixes | `Inventory Note:` · `Across the Cluster:` · `Before You Reserve:` | 2 · 3 · 2, none among the 25 spent |

Every figure reads from `price-matrix.json`, `financial-entities.json`, `clutch-inventory.json` or `locations.json`. No review quotes (all 17 are spent elsewhere); the 3-3-3 rule stays out of the FAQ (locked ruling). The four infographics the record allowed are CSS-only HTML blocks with values from the data files, because the image API credit is exhausted; the breeder asked for that.

## 3. Images
Twenty-four files under `public/images/hub-page/`, all cut from `assets/` after a labelled contact sheet: the mosaic OG photo as hero at 1280 / 760 / 400 (84 KB at full size), six square 800² cards from the top-level bird photos with 400² siblings (30–50 KB), the Congo-vs-Timneh chart, the delivery map, the Midland-sign photo at three widths, the redacted sample document flat-lay (never the flat-lay bearing an invented name), and four read-card thumbs cut from each target page's own hero by `bake_read_card_thumbs.py`. No image repeats within the page; cross-page reuse of the bird photos is allowed and was used.

## 4. Gate findings and what they changed
- **Hardening**: one ERROR on first pass — the `tile-more` cell rendered about 18px tall. Fixed with an explicit `min-height:52px` on that rule. Clean after.
- **Dup body**: six shingles collided with the near-me page and the Congo-vs-Timneh page. All six were sentences I had reproduced from memory of the near-me FAQ. Rewritten; the counter labels shared with the buy page ("Birds reservable today", "Aviary floor price") renamed; the mandated document caption reworded while keeping its three facts.
- **Evidence**: first pass 6 ERROR — Midland ×20, captive-bred ×13, DNA ×12, Appendix I ×4, scam ×3, title 110 chars. Prose trimmed to Midland 9 (the six card shipping lines and the form option no longer name the city), captive-bred 5, DNA 6, Appendix I 2, scam 0; title cut to 66 chars. The four residues are recorded in `budgets_by_slug` with their reasons (approved headings, method labels, the spoke index). The lesson from the near-me build held: repeated card and form strings count as much as prose.
- **AEO**: no binomial on first pass; `Psittacus erithacus` added once in the fork section. The "buried answer" proxies that remain are footer and nav headings, not this page's.
- **Final audit**: `no_aggregateoffer` WARN on a page whose graph contains `AggregateOffer`. The checker reads a single Product+Offer shape; harness defect, logged in the brief, no page change.
- **Board gate**: `pick-tuple-mismatch` WARN — the breeder picked the boarding pass for §7 while the tuple recorded the magazine index; the page follows the pick, the ledger row carries the tuple, and the two align at the next re-board because editing the tuple after approval moves the hash.

## 5. Runtime
Render pages 3 of 3 at 375 / 768 / 1280 on the first run, no fix round. Desktop and phone screenshots of the live page reviewed: hero, tiles, counters, dial and K1 at 1280; image-first hero, tiles, metrics and H1 at 375 with the mobile tab bar clear of the content.

## 6. The retirements
- `/african-grey-parrot-for-sale/` → 301 to the hub in both `_redirects` files. Carriers repointed: the footer link (105 pages), the mobile tab bar's two "Birds" links (every page), the header array, 23 page-level links and the 404 page. Verified in `dist/`: zero links to the singular. Page removed, page-map 87 → 86, sitemaps clean. **Live 301 confirmed.**
- The three near-me pages → 301 to the router; nine inbound links repointed on seven pages (homepage, FAQ, male-vs-female, breeders comparison, health guarantee, available, available/evie); the old "gray" spelling rule that pointed at one of them flattened straight to the router. 100 pages build. Page-map 86 → 84.
- **All four retired slugs return live 301s.** Sitewide IndexNow after the footer change: 99 URLs submitted, HTTP 200.

## 7. Open flags for the breeder
1. The four board additions you approved — kit strip, FAQ questions, angles considered, meta title and description variants — go into the next board as a plan amendment. Adding them to this record after approval would have invalidated the approval.
2. One spelling for refresh ids. The record writes `base#delta`, the disk writes `+`, the published design canvas writes `_`. Write-back now tolerates all three; one spelling is still better.
3. The §7 pick versus tuple mismatch above.
4. The near-me H2 "What Arrives With Every African Grey We Place?" still overlaps the homepage's health-guarantee heading; carried from the near-me brief.
5. `final_page_audit` cries wolf on `no_aggregateoffer` for hub-shaped graphs; a fixture under `tests/render/fixtures/known_broken/` is the fix, not a rule.

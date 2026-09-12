# Session Brief — 2026-09-12 · Near-Me Router Build (Page B)

**Goal:** rebuild `/african-grey-parrots-for-sale-near-me/` as the for-sale cluster's geo router under Strategy B-3 "Router With a Reason", from the approved outline (9 H2 · 18 H3 · 7 H4 · 7 H5 · 7 H6) and locked tuple 12, through every gate the breeder named, and ship it.
**Scope:** the page, its baked images (already on disk), the read-card thumbs, the two harness fixes the build exposed, and one factual correction on Page A that the non-commodity review surfaced. The hub and the three near-me retirements are untouched.
**Gates:** hardening scan · seam parity · dup body + headers · evidence · AEO · final page audit · render meta · render pages (both slugs) · Playwright probes at 375 / 768 / 1280 · non-commodity, entity and keyword-verifier reviews · live 200 · IndexNow.
**Done means:** every gate clean or explained, deploy live, IndexNow 200, gate report as Artifact + `.md`, learning loop recorded.

**Gate report:** `docs/artifacts/cags-near-me-router-build-gate-report.{html,md}` → https://claude.ai/code/artifact/d13141b8-a987-481f-a582-cb0c437c1fb6

## Brief restated at the start (CLAUDE.md rule 6)
Outline approved 2026-08-10, not reopened. Tuple 12: Hero-C refreshed to a **geographic tile field** on a deep-green field · Dial 1 Clay + Rail B ticker · T2 chip cloud refreshed to **region → state chips + metros + sections** · K3 ledger + K4 clipboard + K5 capsules · **NEW Table I "Distance Ledger"** (state · route · cargo counter named on that state's page · cost) · FAQ-B refreshed to a **map-pin register**. H6 prefixes `Distance Note:` · `From Midland:` · `Ask Before You Drive:`. Prose written fresh from the outline; no sibling opened for copy. Reviews out (all 17 spent), 3-3-3 rule out (locked).

## What was built
- 6,410 words in `<main>`; H1 1 · H2 9 · H3 24 (+6 card names, +1 form) · H4 7 · H5 7 · H6 7; 38 unique non-empty alts, 9 decorative; 26 infographics + 6 card photos + hero + newsletter, every H3 image-first.
- **The grid, enumerated once sitewide:** 24 state tiles by region + the CA buy page = 25 states, 15 metros nested under their state and repeated as a pin list; 39 distinct `/african-grey-parrot-for-sale-<x>/` links + the CA page = 40 destinations, all 200 in `dist/`.
- Distance Ledger: 25 rows; the cargo counter column carries **only** the codes each live state page already names (13 states), the other 11 say "Named when you ask". No airport was invented.
- Schema: Product + AggregateOffer, ItemList of 6 Products (each with `areaServed: US`), FAQPage (12 = 12 visible), **two `OfferShippingDetails` nodes** ($185 / $350, DefinedRegion US) referenced from every Offer.
- Form: the full seven-field contract plus a required **state select** (25 states + "another state"); delivery cards lead with Midland pickup. Contract for this slug is `none`, so the harness does not enforce fields here; the page ships them anyway, as Page A does.
- Both method labels once each, defined at first use. Binomials once each. Breeder name once (licence section).

## Reviews run (the breeder asked for all three; none were run on Page A)
| Review | Applied | Declined / deferred |
|---|---|---|
| Non-commodity (Triad) | 5 sharpened passages; 2 Honesty-Policy beats (spelling; "the floor model talks back"); **4 overclaims cut** (see below) | The "belt the carrier in" beat (kept sections to ≤1 beat) |
| Entity 4-Move | IATA LAR ↗, AAV find-a-vet ↗, APHIS public search ↗ (all Link-First, new tab), PBFD + avian polyomavirus + psittacosis named once, board-certified vet, MAF resolved once, closed leg band, reverse image search, Delta Cargo / United Cargo / American Airlines Cargo, `OfferShippingDetails` | "United PetSafe" (agent could not fetch it; not written) |
| Keyword verifier | meta description 164 → 153 chars; "African Grey breeders near me" and "African grey for sale near me" added verbatim; exact primary added to the hero lead | Exact "near me" in the H1 (approved H1 says "Near You"; left) |

### Overclaims removed (Verified-Claim Ledger + breeder ruling 2026-06-23)
1. **"Bonded pair" → "companion pair"** everywhere on Page B **and Page A**. Jins & Jeni are an unrelated companion pair, separable on request (`clutch-inventory.json`, memory `project_jins_jeni_vs_breeding_pair`). Page A also said "they chose each other in the flight cage and have been inseparable since" and "the answer is no" to splitting them; both were unsourced and contradicted the data file. Page A's H3 became "Jins and Jeni — the Companion Pair We Sell Together".
2. "Every state page points at the avian practices buyers there have used" — false for several state pages; replaced with the AAV find-a-vet link.
3. "Buyers from Lubbock, Odessa, San Angelo and Abilene do this regularly" — unsourced; cut.
4. `Observed here · 6 birds` under a sentence about every bird flown since 2014 — label narrowed to `since 2014`.

## Gates (final, on the shipped build)
hardening 0/0 (B) · 0/0 (A) · seam 9/10 (form + FAQ share one, in profile) · dup body PASS (2 furniture stems whitelisted, below) · dup headers: **B clean**; one pre-existing A ↔ health-guarantee exact match ("Reservable Right Now") flagged, not touched · evidence 0 ERROR / 1 WARN (`pbfd-apv-pcr` counted twice inside the one sentence that names the panel; it links the guarantee page, which owns the claim) · AEO 0 ERROR (pronoun-heavy advisory; 3 BLUF WARNs are footer headings) · final page audit PASS-WITH-WARNINGS on `no_aggregateoffer` only (checker, both pages) · render meta 296 passed / 34 skipped · render pages: render pages **6/6 passed** (both slugs × 375/768/1280, scoped Playwright run); remaining advisory rows on both pages are the sitewide Header `mobile-section` orphan class and the breadcrumb `›` 2.38:1, both components, not page edits. First full run had one blocking NAV row at 1280 (40 state-tile targets declared a 166px scroll-margin at desktop, outside the 88–156px band) — fixed to header + 16px. · thumb audit 43/43.

## Runtime probes (Playwright, painting viewport)
| Viewport | Measured |
|---|---|
| 1280 | hero grid **394px** (was 418 with a 16:9 photo; 2:1 photo now) · dial 9 rows × **29px** (first cut wrapped 8 of 9 at 43–58px: labels over the 130px budget) · 0 contrast fails (alpha-aware sweep) · 0 fonts < 12.5px (tile links were 12.16, table th 12.48) · 0 paragraphs > 75ch (ship-line 107ch and clipboard title 97ch had `max-width:none`) · srcset waste 0 after forcing lazy images to load |
| 768 | rail visible, chip gap 10px · state grid 3-up · cards 2-up uniform 568px · 0 contrast · FAQ answers were 85ch single-column → capped 70ch · hero 567px (two columns hold to 700px) |
| 375 | scrollWidth 375, no overflow (the two hits are the clipped `thead`) · hero image first by CSS `order` · tile field 7 cols · state grid 2-up · cards 1-up · ledger stacks to cards · rail jump lands `#birds` 27px below the sticky rail · 0 contrast · 0 small fonts |

## Probes that lied, and page bugs only a screenshot caught (learning loop)
1. **Contrast sweep ignored alpha.** `rgba(255,255,255,.07)` on the dark hero parsed as white → 30 false fails. Composite translucent layers over the nearest opaque colour; treat a known gradient as its dominant colour.
2. **The static hardening scan cannot see the theme.** `body.theme-d h1 + p` (global) out-specified `.nmr .hero .lead` and painted the lead **ink on dark green, invisible**. §1l reads only the page's own CSS; my gradient-skipping sweep also skipped it. Caught by eye on the fold screenshot. Fix: a class containing `text-cream` exempts the element (the rule's own escape hatch). Harness gap logged in Open Flags.
3. **A `display:grid` link stacks its arrow.** "15 metros →" rendered on two lines because grid placed the text node and the span in separate rows; `inline-flex` fixed it. Probe never measured it; the screenshot did.
4. **The thumb baker swallowed the footer.** A `.read-cards` block inside a `<nav>` outside any `<section>` ran to the footer's `</section>` and minted a stray `read--hero` thumb for `href="/"`. Fixed in `scripts/bake_read_card_thumbs.py` (stop at `</nav>` or `</section>`, whichever first). Charged to the harness, no new rule.
5. **The dup gate reads data furniture as prose.** The Avail-B filter rail ("Browse by kind · All birds 6 · Congo 3…") and the form-side inventory list are rendered from `clutch-inventory.json` on every page that ships them. Two stems whitelisted in `scripts/dup_content_audit.py` (one list, two readers).
6. **Harness freshness check worked as designed.** Editing source after a build made it refuse to measure ("1 min newer than dist"); the earlier run also broke because I rebuilt mid-run. Do not build while `test:render:pages` runs.
7. **A Page A image read `complete, naturalWidth 0` at 375/768** on one run (`african-grey-iata-cargo-crate-airport.webp`). The file decodes and ships; this is the transit reset banked 2026-09-11, re-verified before believing.

## Evidence-budget overrides recorded (`data/quality/evidence-budgets.json`)
`african-grey-parrots-for-sale-near-me`: Midland 8 (approved outline: 1 H3 + 1 H5 + 3 H6 prefixes; form pickup option; method label — measured 7), Appendix I 3 (approved H3 + one Fact sentence + the QA'd infographic alt). The first build measured Midland ×32 because the Distance Ledger said "Flies from Midland" on 24 rows; that was a real defect and is now "Flies from MAF, our airport".

## Open Flags
- **Page Board system:** still no spec. B, like A, shipped through the old lane. Hub C gets the first board; the brainstorm resumes at clarifying questions.
- **Harness gap (charge to the tool):** `page_hardening_scan.py §1l component-color-loses-to-descendant` reads page CSS only; the global `body.theme-d h1 + p` rule silently recolours any hero lead on a dark field. Add `src/styles/global.css` descendant rules to §1l's input, with a `known_broken` fixture that inlines the theme rule.
- **`no_aggregateoffer`** fires on every for-sale page that ships `AggregateOffer` in `@graph`: still a checker fixture, not a page edit (carried from Page A).
- **Page A header crossover:** "Reservable Right Now" is an exact H3 match with `/african-greys-for-sale-with-health-guarantee/`. Not touched this session; one of the two should rename.
- **Approved-outline heading changed on factual grounds:** H3 "The Bonded Pair" → "The Companion Pair" (both pages), per the 2026-06-23 ruling. Breeder to confirm.
- **Hero height at 768** is 567px (Page A shipped 528); two columns are kept to 700px. A tablet-only trim would be hiding the metrics strip under 980; not done without a preview.
- **Task 11 (the three near-me 301s into this page) and Task 13 (hub sheds the grid)** are now unblocked: B is live and enumerates the grid.

## What's Next
1. Page Board spec → `docs/superpowers/specs/2026-09-1x-page-board-system-design.md`, then hub C through the first board.
2. Task 11: point `/where-to-buy-african-greys-near-me/`, `/buy-african-grey-parrot-near-me/`, `/african-grey-parrot-for-sale-near-me/` at this page; repoint the 9 inbound links on 7 source pages; IndexNow all 7.
3. Harness: §1l theme-rule input + fixture; `no_aggregateoffer` fixture; Page A "Reservable Right Now" rename.

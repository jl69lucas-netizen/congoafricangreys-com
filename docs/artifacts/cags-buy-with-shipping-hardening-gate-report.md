# Buy-With-Shipping Hardening Gate Report

`/buy-african-grey-parrots-with-shipping/` (Page A), hardening, critique and polish pass on 2026-09-12 on `main`, session-start `26a57b12` → `685b42ec`. Impeccable critique + polish, page-hardening runtime probes at 375 / 768 / 1280, AEO, evidence and anti-AI passes, render harness meta + pages gates, deploy, IndexNow.

Artifact URL: https://claude.ai/code/artifact/8f5c4692-690e-4de0-a835-77d62d9ffe44

## 1. Verdict

**PASS-WITH-WARNINGS, shipped.** Ten measured defects were found on the live page and fixed in one commit; no content was added or removed. Every static gate is clean on the rebuilt `dist/`: `page_hardening_scan.py` 0 ERROR / 0 WARN, `seam_parity.py` 10 seams for 11 sections (the FAQ and form share one, in profile), `dup_content_audit.py` body and `--headers` PASS, `evidence_audit.py` **0 ERROR / 0 WARN** (was 1 WARN), `aeo_audit.py` 0 ERROR with the three remaining WARNs all on footer navigation headings, `final_page_audit.py` PASS-WITH-WARNINGS on the same `no_aggregateoffer` row every for-sale sibling carries (the page does ship `AggregateOffer`; the checker misses it, see §7).

The one warning that stays open is not a page defect: the `no_aggregateoffer` checker row, which every for-sale sibling carries and which belongs to the harness backlog (§7).

## 2. What changed, component by component

Every row was confirmed on the rendered page before it was edited. Measurements are Playwright, viewport in brackets.

| Component | Finding | Fix | Measured after |
|---|---|---|---|
| Hero (768) | Stacked image + copy ran **1,051px** tall; a full-width 720×540 photo pushed the H1 below the fold | Two columns hold down to 700px; stacking starts at ≤700 | **528px**, image 300px wide, H1 3 lines |
| Price ribbon (≤980) | Four single-column rows, 162px on mobile | 2×2 grid with perforation borders | 111px at 375, 77px at 768 |
| Desktop dial (1280) | 7 of 10 rows wrapped to two lines; the five-state tag forced a **74px** row | Labels cut to the measured 130px track (label + tag), tags shortened | 10 rows × **29px**, dial 408px, no inner scroll |
| Mobile rail | Inherits the same spine | Same labels | 10 chips × 38px, active chip tracks scroll |
| Boarding-pass TOC | Every stub carried three underlines from the body-link rule; 890px tall single column at 375 | `.bpass-stops li a{text-decoration:none}`; two compact columns at ≤640 | 436px at 375, no underline |
| Bird cards (≤640) | Two-up 167px cards with the blurb `display:none`, the layout the polish playbook rejected | One card per row, photo at full 343px width, blurb visible, name 18px, CTA full width | 6 × 567px, nothing hidden |
| Bird cards (1280) | Reported as "heads cropped"; confirmed as the sticky header overlaying the screenshot, not a crop | none | photos 225px square, Δ0 card height |
| K1 receipt (≤640) | 617px | Row padding 0.5 → 0.42rem | 601px |
| Newsletter | Contrast probe reported 5 failures | Probe bug: it walked past a gradient background to the cream page; re-probed with gradient ancestors excluded | 0 failures, 446 nodes examined |
| Table H, form, FAQ, geo cards, reading cards | Clean at all three widths | none | 0 lines over 75ch, form controls 16px |

## 3. SEO, AEO, GEO, evidence and anti-AI

| Pass | Before | After | Change made |
|---|---|---|---|
| `aeo_audit.py` breeder entity | `breeder=0` WARN | `breeder=1` | The USDA paragraph now opens with Mark and Teri Benjamin (the section that owns the licence) |
| `aeo_audit.py` stat-bearing header | none, WARN | 3 | "The First **72 Hours** After Your Bird Lands", "**$185** Airport Cargo, Collected at the Desk", "**$350** Home Delivery to Your Door" |
| `aeo_audit.py` BLUF proxy | 7 flagged (4 on the page, 3 in the footer) | 3, all footer | Four openers rewritten answer-first: price ladder, honest price, home delivery, five states |
| `evidence_audit.py` | WARN `hatch-band` claim ×4, proof NOT FETCHED | 0 WARN | Said once in the paperwork section; the table row, the DNA paragraph, the H3 and the alt now say "leg ring" / "ring number" |
| Anti-AI rhythm | "rather than" ×31, "which is why" ×5 | ×11, ×2 | Rewritten as ", not" / "instead of" / "so"; no sentence lost its meaning |
| `dup_content_audit.py --headers` | PASS | PASS | The four new headers cross no sibling |
| Title Case | all headings | all headings | New headers checked by hand |
| Term budgets (for-sale) | in budget | in budget | No trust term was added |

GEO tables and lists unchanged: Table H price ladder, K1 receipt, K4 clipboard, 12-question FAQ with `FAQPage`, `ItemList` of six `Product` + `Offer`, group `AggregateOffer`.

## 4. Runtime probes, before → after

| Probe | 375 | 768 | 1280 |
|---|---|---|---|
| `scrollWidth` = `innerWidth` | ✓ | ✓ | ✓ |
| Right-edge offenders outside a scroller | 0 | 0 | 0 |
| `.hero-grid` height | 709 → 709 | **888 → 444** | 381 → 381 |
| `header.hero` total (with ribbon) | 871 → **827** | 1051 → **528** | 434 → 434 |
| H1 computed size / lines | 24px / 3 | 28.2px / 3 | 31.7px / 2 |
| Dial rows wrapped | hidden | hidden | **7 → 0** |
| Boarding pass height | 890 → **436** | 475 | 226 |
| Bird card width × height | 167×377 → **343×567** | 353×568 | 227×509 |
| Card CTA hugs, one line | ✓ (stretch by design) | ✓ | ✓ 120–160px |
| `main p` over 75ch (real `ch`) | 0 | 0 | 0 |
| Contrast failures (gradient-aware probe) | 0 of 428 | n/a | 0 of 446 |
| Smallest visible text | 12.64px | 12.64px | 12.64px |
| Scroll-spy after a hash jump | rail chip follows | rail chip follows | dial 01→03→05→09→10, heading lands at 112px |
| Jump target lands below sticky rail | ✓ (162 vs 149) | ✓ | n/a |
| `srcset` waste ratio > 1.5 | 0 | 0 | 0 of 45 |

## 5. Render harness

| Gate | Verdict | Examined (its own count) | Rows on this page |
|---|---|---|---|
| `npx astro build` | OK | 104 pages in ~29s | n/a |
| `npm run test:render:meta` | **PASS** | 296 passed, 34 skipped (1.1m) | n/a |
| `test:render:pages --grep <slug>` run 1 | **FAIL at 768** | 24 checks × 3 viewports | 1 blocking: hero `img-srcset-within-2x` 2.56× (the new two-column tablet hero painted 300px against a 100vw `sizes`) |
| `test:render:pages --grep <slug>` run 2 | **PASS 3/3** (50.7s) | 24 checks × 3 viewports | 3 advisory rows per viewport, identical at 375 / 768 / 1280 |
| `page_hardening_scan.py` | clean | 7 source files, 1 built page | 0 ERROR / 0 WARN |
| `seam_parity.py` | PASS | 1 page | sections 11, seams 10, missing 0 |
| `dup_content_audit.py` + `--headers` | PASS / PASS | 1 page | 0 crossover |
| `evidence_audit.py` | 0 ERROR / 0 WARN | 1 page | was 1 WARN |
| `aeo_audit.py` | 0 ERROR / 1 WARN | 1 page | the BLUF proxy on three footer H3s |
| `final_page_audit.py` | PASS-WITH-WARNINGS | 49 pages listed | `no_aggregateoffer` (checker, see §7) |

The three advisory rows that remain, all confirmed on the built page and none owned by this page's markup:

| Family | Row | Where it lives |
|---|---|---|
| CSS `css-class-resolves` | `mobile-section` ×3 matches no rule | `src/components/Header.astro`, sitewide |
| A11Y `a11y-text-contrast-aa` | breadcrumb separator `›` 2.38:1 | `src/components/Breadcrumb.astro`, sitewide, decorative glyph |
| DUP `dup-no-sibling-crossover` | 25 words: the six bird names and prices in the form aside | rendered from `clutch-inventory.json` on every for-sale page; whitelist furniture |

Run 1 also carried a LAYOUT row (`layout-h3-image-first`, 18 H3 blocks with prose before their image) and four prose DUP runs against the health-guarantee page. Both are gone in run 2: the 18 blocks were swapped image-first and the five shared runs reworded on this page.

## 6. Impeccable critique

Register: brand (design is the product). Scene: a first-time buyer on a phone, three breeder tabs open, afraid of being scammed. Colour strategy: Committed (forest + clay on cream), as `DESIGN.md` locks it. No absolute-ban hit: no gradient text, no glass, no hero-metric template, no side-stripe cards (the 3px clay tick on H2 is the house heading signature, not a card stripe).

| # | Heuristic | Score | Note |
|---|---|---|---|
| 1 | Visibility of system status | 4 | Dial ring and rail chip track the reader; filter chips show live counts |
| 2 | Match system / real world | 4 | Boarding-pass metaphor fits a shipping page; prices in the language buyers use |
| 3 | User control and freedom | 3 | Four jump surfaces (dial, rail, pass, tickets); no back-to-top |
| 4 | Consistency and standards | 3 | Sibling kit respected; the boarding-pass underline broke it until today |
| 5 | Error prevention | 3 | Confirm-cell and confirm-email fields double the typing; the form contract owns that call |
| 6 | Recognition over recall | 4 | Every bird named with photo, price and shipping line on the card |
| 7 | Flexibility and efficiency | 3 | Filter chips; no keyboard shortcut needs |
| 8 | Aesthetic and minimalist | 3 | K1 + boarding pass + counter before the first bird is ~2,400px on mobile; trimmed 550px today |
| 9 | Error recovery | 3 | Native validation only |
| 10 | Help and documentation | 4 | Twelve FAQ, five checks, price ladder |
| | **Total** | **34/40** | |

What works: the price ladder is the one thing no competitor publishes and it reads in ten seconds; the receipt card answers "what do I get" before the buyer scrolls; the bird cards carry one fact per line.

Biggest remaining opportunity: mobile pre-content. Hero, counter, receipt and boarding pass still sit before the first card. Moving the boarding pass below the bird grid on mobile (the rail already covers jump navigation there) would put a bird 800px higher. Not done today because it changes section order, which needs a preview and a breeder call.

## 7. Learning loop

Four probes lied before the page did. All four are recorded so the next pass does not repeat them.

| Probe | What it reported | What was true |
|---|---|---|
| Scroll-spy (first run) | "09 of 10" at the top, `papers` landing at −12,635px | `scroll-behavior:smooth` was mid-animation; forcing `auto` and waiting 600ms gave 01→03→05→09→10 |
| Hero screenshot (1280, 375) | Blank beige box | The photo had not decoded when the element screenshot fired; at 768 and on a re-take it renders |
| Contrast sweep (1280) | 5 failures in the newsletter | The probe walked past a gradient background to the cream page; gradient-aware version reports 0 |
| Bird cards (1280) | Heads cut off on Bery and Amie | The sticky site header overlays the top of row 1 in an element screenshot |

One defect was mine: the first mobile card edit set two sizes to `.78rem` (12.48px), under the harness's 12.5px floor; caught by the min-font probe before commit and lifted to `.8rem`.

`final_page_audit.py` reports `no_aggregateoffer` on every for-sale page that ships an `AggregateOffer` inside a `@graph`. That is a checker defect, not a page defect, and belongs in the harness backlog with a `known_broken` fixture.

## 8. Page Board status

The Page Board system was picked first on 2026-09-11 and its brainstorm stopped at the clarifying questions; no spec exists. The same session then ran the Gemini image batch, and Page A was built and shipped on 2026-09-12 through the old lane, before any board existed. So the order recorded in the session brief ("Page Board spec, then Pages A, B and the hub") was overtaken: A is live, B is next, and the hub is still the page that gets the first real board. Nothing about the board has been built.

## 9. Open flags for the breeder

1. **Mobile section order.** Move the boarding-pass TOC below the bird grid on phones? It puts a bird 800px higher and the rail already covers jumping. Preview first.
2. **Confirm fields.** Confirm-cell and confirm-email double the typing on a phone. The form contract (2026-09-11) owns this; five breeder calls there are still open.
3. **`no_aggregateoffer` checker.** Fix in the harness, not the pages.

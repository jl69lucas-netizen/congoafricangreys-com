# Review Consolidation — Gate Report

**Result: done.** `/african-grey-reviews/` now lists all **17** real buyer reviews on the site, each exactly once, with the right wording, name, town and photo. None of the 64 non-location pages checked (1 of them since deleted) shows a duplicated, edited or misattributed review. The live site was verified in Playwright at 375, 768 and 1280 px on 2026-09-11.

## What shipped

| Commit | What it did |
|---|---|
| `859d75c1` | Ledger `data/reviews.json` +9 confirmed reviews, copied from the built site (never retyped); Brunner/Soliz/Brim held pending |
| `e76120f5` | `scripts/review_inventory.py` refuses stale, truncated, misplaced or mis-towned text; photos filled for Plaisance, Hendershot, Thomas, Tershal |
| `34c7f768` | Review page renders from the ledger; new Testimonials `wall` layout; edited Woodard/Kempf quotes restored on trusted-breeders, timneh and male-vs-female; dist guard `tests/test_review_integrity.py` |
| `81034475` | Breeder ruling: Brunner, Soliz and Brim are real; templated rewrites on 6 bird pages + adoption-cost restored to their exact words; review page lists 17 |
| `5ab8eda2` | Review cards use real type tokens (serif headlines render); never-served `/testimonials/` deleted (301 kept), sitemaps regenerated |

## The 17 reviews, before → after

| Buyer | Town | On the review page before | After |
|---|---|---|---|
| Brian Carr | Plainview, TX | missing | featured |
| Catherine Kempf | Schaumburg, IL | shown **twice** | featured, once |
| Clifford Hutter | Secaucus, NJ | featured, with a photo the ledger says isn't his | wall, initials |
| Richard Woodard | Winter Haven, FL | yes | wall |
| Archie O'Brien | Farmingdale, NY | yes | wall |
| Stanley Perkin | Oceanside, CA 92054 | missing | wall |
| Jesse Ovalle | Baton Rouge, LA 70806 | missing | wall |
| Meredith Plaisance | Hartsville, SC 29550 | missing | wall |
| Jeffrey Hendershot | Centennial, CO 80112 | missing | wall |
| Joanna Thomas | Oildale, CA | missing | wall |
| Anthony Tershal | Lakewood, WA | missing | wall |
| Joshua Erwin | San Bernardino, California | missing | wall, initials |
| Walter Zander | Fort Washington, PA | missing | wall |
| Alene Murphy | Savannah, GA | missing | wall |
| Lawrence Brunner | Fullerton, CA | missing (disputed) | wall — ruled real |
| Sandra Soliz | Rome, GA | missing (disputed) | wall — ruled real |
| Ida Brim | Nashville, TN | missing (disputed) | wall — ruled real |

## Defects found and fixed

- **Duplicate on the review page:** Kempf appeared in both the featured block and the grid, which also put 2 Review schema entries for her on the page.
- **13 reviews missing from the review page.** 12 of them existed only on for-sale, bird and pair pages; Brian Carr was already in the ledger.
- **Edited real reviews** (first 60 characters intact, rest rewritten):
  - Trusted-breeders: Woodard's and Kempf's quotes and schema carried SEO phrasing ("handed me the CITES paperwork…", "is congoafricangreys.com legit"), and Kempf's quoted headline said "well-documented", which she never wrote.
  - Timneh: "Congo" removed from Woodard's quote.
  - Male-vs-female: Kempf's schema text cut to 125 of 257 characters.
- **Templated rewrites of the three disputed reviews** on 6 bird pages and adoption-cost. They had pronoun swaps per bird ("They's DNA-sexed", "with them health certificate") and additions ("landed at LAX… Worth every dollar"). All are restored to the breeder's words.
- **`/testimonials/`** still built 5 unverified named reviews behind a 301 and sat in `page-sitemap.xml`. Deleted; the redirect stays.
- **Review-card type:** `font-display` and `bg-clay-50` don't exist as tokens, so card headlines rendered in the body sans. Fixed in the Testimonials component.

**Retracted:** the plan said Alene Murphy's caption showed the wrong town. It never did (source and build both say Savannah, GA). It was a misread.

## Gates

| Gate | Result | Examined |
|---|---|---|
| `tests/test_review_integrity.py` + attribution + homepage review tests | 20 passed | 63 non-location pages, 23 carrying a ledger review, 70 review cards |
| `sweep_review_attribution.py --check` | 0 pending | 29 src review objects |
| `npm run test:render:meta` | 296 passed, 0 failed | — |
| `npm run test:render:pages` | 57/57 (baseline 57/57) | 19 targets × 3 viewports |
| `dup_content_audit.py` | 6128 before = 6128 after; 0 new blocks on changed pages | whole site |
| `page_hardening_scan.py` / `final_page_audit.py` on changed pages | no review-content rows; all rows pre-existing | 4 pages |

## Live browser proof (Playwright, congoafricangreys.com)

| Width | Names once | Review schema | Photos | Layout | Sideways scroll |
|---|---|---|---|---|---|
| 375 | 17/17 | 17, no dup | 15/15 load | 1 column × 15 | none |
| 768 | 17/17 | 17 | 15/15 | 2 columns (7 rows + 1) | none |
| 1280 | 17/17 | 17, none missing | 15/15 | 3 columns × 5 | none |

Console: 0 errors, 0 warnings. Live curl checks:
- The breeder's wording is on all 9 pages that show Brunner, Soliz and Brim, with no leftover rewrites.
- Homepage review cards use `font-lora`.
- The live sitemap has 55 URLs, with no `/testimonials/`.

## IndexNow (HTTP 200)

african-grey-reviews, trusted-african-grey-parrot-breeders, timneh-african-grey-for-sale, male-vs-female-african-grey-parrots-for-sale, available/amie, available/bery, available/elad, available/evie, available/jins-jeni, available/roys, african-grey-parrot-adoption-cost, and `/` (homepage).

## How it stays fixed

- **One source of truth.** A new real review goes into `data/reviews.json`; the review page picks it up at build time.
- **The guard fails the build** if a review appears twice on a page, sits beside the wrong buyer, is edited, shows the wrong town or photo, or if a new review card ships without being in the ledger.
- **Tooling.** `scripts/review_inventory.py` copies text from the built site, and `sweep_review_attribution.py` restores edited quotes.

## Still open (not part of this task)

- `font-display` is used 105 times across 20 other components (Navbar, Footer, BirdCard…) with no token behind it. Fixing it is a sitewide type change and needs its own decision.
- The homepage still shows `/african-grey-review-top.webp` beside Clifford Hutter; the ledger says he has no photo.
- At 768 px the 15th card sits alone on the last row.
- The guard checks name-beside-quote for blockquote cards, not `<p>`-style cards.
- Ledger town formats vary (ZIPs, "California").
- The sitemap generator stamped every `lastmod` with today's date.
- 18 `data/quality/scorecards/*-2026-09-11.json` files rewritten by the gate run are uncommitted. They reflect the state before the ruling and should be regenerated by the next harness run.
- The "52 verified buyers / 4.9" aggregate is ignored per the breeder (2026-09-11).

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
| Clifford Hutter | Secaucus, NJ | featured | wall |
| Richard Woodard | Winter Haven, FL | yes | wall |
| Archie O'Brien | Farmingdale, NY | yes | wall |
| Stanley Perkin | Oceanside, CA | missing | wall |
| Jesse Ovalle | Baton Rouge, LA | missing | wall |
| Meredith Plaisance | Hartsville, SC | missing | wall |
| Jeffrey Hendershot | Centennial, CO | missing | wall |
| Joanna Thomas | Oildale, CA | missing | wall |
| Anthony Tershal | Lakewood, WA | missing | wall |
| Joshua Erwin | San Bernardino, CA | missing | wall, initials |
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
- The live sitemap no longer lists `/testimonials/` (after batch 2 it has 53 URLs; see below).

## IndexNow (HTTP 200)

african-grey-reviews, trusted-african-grey-parrot-breeders, timneh-african-grey-for-sale, male-vs-female-african-grey-parrots-for-sale, available/amie, available/bery, available/elad, available/evie, available/jins-jeni, available/roys, african-grey-parrot-adoption-cost, and `/` (homepage).

## How it stays fixed

- **One source of truth.** A new real review goes into `data/reviews.json`; the review page picks it up at build time.
- **The guard fails the build** if a review appears twice on a page, sits beside the wrong buyer, is edited, shows the wrong town or photo, or if a new review card ships without being in the ledger.
- **Tooling.** `scripts/review_inventory.py` copies text from the built site, and `sweep_review_attribution.py` restores edited quotes.

## Resolved in batch 2

Every item that was open after the first batch is now fixed (see the next section). The two exceptions were decided by the breeder: the "52 verified buyers / 4.9" aggregate stays as it is, because those reviews will go onto the location pages when they are rebuilt, and Clifford Hutter's homepage photo is his and correct.

## Batch 2: the remaining open items

This batch closes the open list, as the breeder asked on 2026-09-11. Two items were left as they are on purpose:
- **The "52 verified buyers / 4.9" aggregate.** Those reviews go onto the location pages when they're rebuilt.
- **Clifford Hutter's homepage photo.** The breeder confirmed it's real.

| Commit | What it fixed | Live evidence |
|---|---|---|
| `43f63661` | Reviewer towns now read "City, ST" (no ZIP codes, no spelled-out state) | Live curl: Oceanside/Baton Rouge/Hartsville/Centennial/San Bernardino all shown as City, ST, 0 ZIPs left |
| `43f63661` | A lone last card on the review page is centred (2 columns) or moved to the middle column (3 columns) | Playwright at 768 px: card 15 is 358 px wide like the others, with a 189 px gap on each side |
| `43f63661` | The duplicate check now confirms each review sits under its own buyer's name, for every card layout. It works from the page structure, so it doesn't matter whether the name comes before or after the quote | 71 cards checked; swapping two buyers' names on the review page and on a bird page both fail the test |
| `43f63661` | The sitemap's `lastmod` is now each page's real last change (its git commit date); 3 URLs that 404 were removed; the `/available/` page was added | Live sitemap: 53 URLs, 9 distinct dates, 0 URLs that 404, `/available/` listed |
| `43f63661` | Found and fixed: another session's design mockups in `docs/` were adding ~57 KB of unused CSS to every page (fixed with `@source not "../../docs"`) | Live privacy page CSS is 121.6 KB (it was ~171 KB with the bloat); no mockup classes left; no page lost a style it uses (checked on 104 pages) |
| `887b598d` | The `font-display` class didn't exist, so text using it fell back to the plain body font. It's now `font-lora` (Newsreader) in 17 components, approved by the breeder after before/after screenshots. The homepage is the only page affected: 6 price cells, 4 trust badges and 2 pull quotes | Before/after screenshots at 375 px |
| `887b598d` | Removed a fake phone number, (432) 555-0119, from ContactForm (2 places) and from the Navbar/Footer defaults | No page showed it; there are 0 matches in `src/` |

IndexNow (HTTP 200): dna-tested, hand-raised, health-guarantee for-sale, breeding-pair, african-grey-reviews, available.

**Traps recorded for next time:**
- zsh doesn't split `git add $FILES` into separate paths, so list files literally.
- Quote `--include='*.astro'` in zsh.
- Tailwind v4 scans the whole repo, so any HTML under `docs/` ends up in the site CSS.
- Another session edited `HeroV3.astro` in the same folder at the same time. Always stage files by exact path.

**Live check of `887b598d` (homepage, curl):**
- 0 `font-display` classes and 151 `font-lora`.
- The egg and pair prices, the trust badges and the pull quote all carry `font-lora`.
- The fake phone number is not on the page.
- Inline CSS is 142 KB, with no design-canvas classes.
- IndexNow accepted `/` (HTTP 200).

**Scorecards:** regenerated from a clean worktree of `origin/main` @ `887b598d`, so the run included no uncommitted work from the concurrent session. `npm run test:render:pages` passed 57/57 (baseline 57/57), and the 19 `data/quality/scorecards/*-2026-09-11.json` files now reflect the deployed state.

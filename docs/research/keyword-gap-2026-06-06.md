# Interior batch — competitor word-count summary — 2026-06-06

Method: Top 3 organic content competitors per primary keyword, fetched live via Firecrawl (onlyMainContent=true). Word counts are main-content only (nav/cookie/footer stripped via a consistent script). Marketplace/classified spam (Hoobly, listings) and pure forum/video/Quora results were excluded in favor of real content pages, per task rules. "Competitor max words" = the deepest single ranking content page found for that intent.

| Slug | Competitor max words | Target (+1000) |
|------|---------------------|----------------|
| african-grey-parrot-care-guide | 1745 | 2745 |
| african-grey-care | 2048 | 3048 |
| african-grey-parrot-diet | 3116 | 4116 |
| best-african-grey-parrot-food | 3116 | 4116 |
| african-grey-parrot-lifespan | 3497 | 4497 |
| african-grey-parrot-health-guarantee | 545 | 1545 |
| trusted-african-grey-parrot-breeders | 587 | 1587 |
| african-grey-reviews | 8311 | 9311 |
| captive-bred-african-grey-parrot | 3322 | 4322 |
| cites-african-grey-documentation | 857 | 1857 |
| how-to-avoid-african-grey-parrot-scams | 3518 | 4518 |
| african-grey-parrot-guide | 3344 | 4344 |
| african-grey-parrot-faq | 1366 | 2366 |
| how-to-tame-african-grey-parrot | 4140 | 5140 |
| african-grey-adoption | 2158 | 3158 |
| african-grey-parrot-price | 2299 | 3299 |

## Caveats on the +1000 targets (read before setting page length)
- **african-grey-reviews (8311 → 9311):** the max is ONE breeder stacking dozens of testimonials on a single page — volume, not editorial depth. Use only REAL, verifiable testimonials; do NOT pad to 9311. Treat 9311 as an upper bound, not a quota.
- **african-grey-parrot-health-guarantee (545) & trusted-breeders (587) & cites (857):** these are inherently short, high-trust page types. The +1000 lets us out-depth competitors, but value comes from documentation specifics (CITES Appendix I, closed band, DNA cert, USDA), not word padding.
- **how-to-tame (4140) & best-food (3116) & captive-bred (3322):** the "max" page is a broad/adjacent guide, because tight, dedicated content for these exact terms is under-served (forums/video dominate). These are real ranking opportunities; hit the target with genuine depth, not filler.
- **best-food (3116):** pure "best pellet" roundups run ~1350–1650; 3116 is the deepest food page (Northern Parrots feeding guide). Beating the deepest food competitor is the safe target.

## Pages with weak / unreliable competitor data (flagged, not fabricated)
- **african-grey-parrot-health-guarantee** — afrobirdsfarm.com "top breeders" page timed out (HTTP 408) on direct API and Firecrawl stealth across the session; could not get a word count. Two clean competitor pages retrieved (545, 527).
- **trusted-african-grey-parrot-breeders** — term dominated by thin breeder homepages (Shades of Greys 95w, Psittacus 271w) and JS-only directory listings (birdbreeders.com category extracted ~4 words). Best real content competitor = a 587-word "qualities to look for in a breeder" post. Large depth opportunity.
- **captive-bred-african-grey-parrot** — almost no commercial content pages rank; SERP is conservation journalism + forums. Length bar (3322) is informational/advocacy (grrlscientist), not a seller. Clear commercial gap for CAG.
- **how-to-tame-african-grey-parrot** — dedicated taming tutorials are thin; trainedparrot.com/taming under-rendered (~203 prose words, table-heavy layout). Ranking pages are broad AG-behavior guides. Opportunity for a focused step-by-step guide.
- **african-grey-reviews** — only one strong on-site competitor (btaviary, testimonial wall); others are programmatic geo-doorway pages or forum scam threads.

## Cross-cutting schema gaps observed (build-time opportunities)
- **FAQPage** present on Psittacus, IFAW, Parrot Essentials — many competitors lack it. Win on care/diet/guide/faq/cites pages.
- **Review / AggregateRating** — btaviary has 8311 words of reviews but no visible Review schema; PetMD uses Product/Offer/AggregateRating. Mark up our reviews + bird pages.
- **Article + BreadcrumbList** are near-universal among informational winners (TheSprucePets, Hepper, Kaytee, LafeberVet) — table stakes.

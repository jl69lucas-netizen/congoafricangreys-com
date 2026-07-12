# Evidence Log — /african-grey-parrot-breeders-comparison/ (2026-07-12)

Only sources actually fetched are logged. "Snippet" = Google-returned description only (page body not scraped). "Full" = page body scraped via Firecrawl. "Sweep" = automated homepage/sitemap probe.

## Google US SERP queries (Firecrawl search, web source, US location)
| Query | Result | Top domains returned |
|---|---|---|
| best african grey parrot breeders | Full result set | reddit(1), graybreedersfoundation, northshoregreys(3), facebook(4), birdbreeders(5), psittacus, royalbirdcompany, featheredfriendshub |
| how to choose a reputable african grey breeder | Full result set | reddit(1), facebook(2), birdtricks(3), parrotforums(4), youtube(5), agp.boards.net(6), weebly(7), birdbreeders(8) |
| african grey breeder scams how to avoid | Full result set | facebook(1), reddit(2), youtube(3), birdtricks(4), tiktok(5), justanswer(6), parrotforums(7), trainedparrot(8) |
| reputable african grey breeders near me USA | Full result set | facebook(1), birdbreeders(2), youtube(3), northshoregreys(4), graybreeders(5), royalbird(6), africangraysales(7), anasparrots(8) |
| questions to ask an african grey parrot breeder before buying | Full result set | weebly(1), reddit(2), birdtricks(3), facebook(4), youtube(5), exoticdirect(6), justanswer(7), quora(8) |
| is congoafricangreys.com legit reviews | Full result set | scamadviser("legit and safe"), gridinsoft("58/100"), scam-detector("suspicious"), congoafricangreys/reviews(5) |

## Pages scraped in full (Firecrawl scrape)
| URL | Status | Extracted |
|---|---|---|
| parrotforums.com/threads/how-to-identify-a-parrot-scam.67706 | 200 Full | reverse-image-search, paste-text, too-good-to-be-true, payment-first, spay/neuter & eggs tells, area-code mismatch, "decent honest people won't hesitate to give detail" |
| birdtricksstore.com/…/5-qualities-to-look-for-in-a-breeder | 200 Full | 5 qualities: outdoor birds, organic diet, passes inspections, happy-customer reviews, visit in person. **No CITES/USDA/DNA/health-guarantee/shipping** |
| reddit.com/r/AfricanGrey/…/reputable_breeders | BLOCKED | Firecrawl "does not support this site" — used SERP snippet instead |

## 30-competitor sweep (competitor-30-sweep.py → competitor-30-sweep.json)
Homepage HTML keyword scan + sitemap probe, 2026-07-12. Verifiable, reproducible.
- **Reachable homepages:** 18 of 30 (200). **Offline (URLError/HTTPError):** 12 — including **4 of 11 T1 "direct breeders"** (afrobirdsfarm, exoticparrotsplanet, williamsafricangreys, africangreyaviaries).
- **USDA surfaced on homepage:** ~0/30 (one unconfirmed keyword hit).
- **Health-guarantee copy:** afrigreyparrots, exoticparrotpetstore, africangrayparrotsforsale, birdsforsales, compoundexotics, exoticpetsavenue, mariettabirdshop (+ variants).
- **CITES/docs copy:** exoticparrotpetstore, africangrayparrotsforsale, birdsforsales, shadesofgreys, compoundexotics, allaboutparrots, mariettabirdshop.
- **"weaned" on homepage:** africangrayparrotsforsale, birdbreeders.
- **Visible prices:** africangrayparrotsforsale $1,000 · birdsforsales $1,500 · birdsnow $2,250–$6,000 · birdbreeders $2,000–$6,800 · (SERP) anasparrots $6,500.
- Sitemap footprint: birdsnow 79,747 · parrotalert 24,698 · rationalparrot 14,000 · compoundexotics 935 · exoticpetsavenue 705.

## Branded-trust third-party pages (SERP snippet, not scraped)
- scamadviser.com/check-website/congoafricangreys.com → "legit and safe."
- gridinsoft.com → "58/100 Trust Score… not a confirmed scam, mixed signals."
- scam-detector.com → "it's suspicious… low trust score."
- **Action:** these rank on "is congoafricangreys.com legit" ABOVE our own reviews page → §19 branded-trust section + Review/Organization schema is a page objective, not optional.

## Internal data files consulted (grounding)
- data/price-matrix.json → CAG baby $2,300–$2,500, adult $1,700; congo range $1,700–$3,500.
- data/financial-entities.json → TAG $1,500–$1,600; deposit $200; shipping $185 airport / $350 home.
- docs/reference/credentials.md → USDA AWA licensed (verifiable aphis.usda.gov/awa/public-search); C.A.Gs – Midland, TX 79707; +1-281-545-3169; Mark & Teri Benjamin.
- data/breeder-comparison.json → existing page data (competitors/aggregators/confirmed_scams arrays) — reusable, extend not duplicate.

## Not fetched / limitations (honesty)
- Reddit thread bodies (Firecrawl-blocked) — only SERP snippets used; a headless-browser pass could deepen the UGC quotes if needed.
- Google AI Overview block not returned verbatim by web-source search — PAA reconstructed from result descriptions.
- Competitor sitemap counts are probe-time snapshots; offline sites may return intermittently.

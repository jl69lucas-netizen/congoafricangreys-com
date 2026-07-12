# Evidence Log — /african-grey-comparison/ HUB (2026-07-12)

Only fetched sources logged. Snippet = Google description. Sweep = automated probe.

## Google US SERP queries (Firecrawl search, web, US)
| Query | Top domains |
|---|---|
| african grey parrot comparison | facebook(1), **wikipedia(2)**, quora-vs-macaw(3), youtube-timneh-vs-congo(4), reddit-grey-or-cockatoo(5), **thesprucepets(6)**, **nationalgeographic(7)**, **birdtricks-set-apart(8)** |
| african grey vs other parrots which is best | facebook(1), zupreem(2), reddit(3), quora-macaw-or-grey(4), youtube(5), birdtricks(6), tiktok-grey-vs-amazon(7), pethelpful-amazons-vs-grey(8) |
| best talking parrot species ranked | parrotessentials(1 **grey#1**), thesprucepets(2), **petmd(3 "grey ranks number one, 1000 words")**, chewy(4 **"greys widely considered best"**), reddit(5,6), facebook(7), pethelpful(8) |
| which parrot is right for me quiz / best pet parrot | **myrightbird/quiz(1)**, **allpetbirds/quiz(2)**, reddit(3), **proprofs/quiz(4)**, youtube(5), **lafeber/find-a-bird(6)**, parrotforums(7), facebook(8) |

## 30-competitor sweep (competitor-30-sweep.py/json) — the decisive hub finding
- **0 of 30 competitors have an African-Grey comparison hub.** ONLY "vs grey" page in the field: **parrotwebsite.com/african-grey-vs-cockatoo** (parrotwebsite has 5 comparison pages, 1 grey-specific).
- Other vs-pages are non-grey: allaboutparrots "male-vs-female-macaws", smallanimaladvice dog/rodent comparisons (havanese-vs-bichon etc.), rationalParrot non-bird.
- "talking" URL counts: birdsNow 293 (classified listings), parrotwebsite 22, rationalParrot 17, allaboutparrots 14 — but none is a grey-centric talking-comparison hub.
- **No breeder (T1) has ANY comparison/vs/hub content** (all show 0). Same infra pattern: 4 of 11 T1 breeder sites offline.

## Internal state (grounding)
- All 7 spoke slugs confirmed live on disk (src/pages/): congo-vs-timneh-african-grey, male-vs-female-african-grey-parrots-for-sale, african-grey-vs-macaw, african-grey-vs-cockatoo, african-grey-vs-amazon-parrot, african-grey-pros-and-cons, african-grey-parrot-breeders-comparison.
- Current hub = src/pages/african-grey-comparison/index.astro, 215 lines, H1 "Which Parrot Is Right for You?", thin router — rebuild to 6,500–7,000w pillar.
- data/price-matrix.json + financial-entities.json → Congo $1,700–$3,500, Timneh $1,500–$1,600, $185 airport / $350 home.
- credentials.md → USDA AWA licensed; C.A.Gs – Midland, TX; Mark & Teri Benjamin.

## Best-talking corroboration set (cite as external authority for the #1 claim)
PetMD ("ranks number one… up to 1,000 words"), Chewy ("widely considered the best"), The Spruce Pets ("8 Best Talking Birds", grey first), parrotessentials ("Top 5", grey #1), PetHelpful ("Top 10"). Four+ independent authorities → the superlative is defensible, not invented.

## Not fetched / limitations (honesty)
- Reddit thread bodies (Firecrawl-blocked) — SERP snippets only.
- Listicle bodies not scraped in full — grey's #1 rank captured from Google snippets (unambiguous); cite the pages, don't reproduce their prose.
- Google AIO block not returned verbatim — PAA reconstructed from result descriptions.
- Spoke content NOT re-summarized here — the hub build must read each live spoke and synthesize fresh (dup gate), not copy.

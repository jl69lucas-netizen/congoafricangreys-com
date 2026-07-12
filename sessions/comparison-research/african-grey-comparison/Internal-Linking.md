# Internal Linking — /african-grey-comparison/ (HUB)

The hub is the cluster's link keystone: it links DOWN to all 7 spokes (each from its own summary section) and to money pages, and the spokes link UP to it. Anchors at sentence START (Link-First), unique per spoke (Anchor Diversity Ledger). Internal = same tab.

## Down → the 7 spokes (ItemList + one contextual link each, from that spoke's summary section)
| Spoke | Hub section | Anchor angle (unique) |
|---|---|---|
| /congo-vs-timneh-african-grey/ | §10 variant | "our Congo-vs-Timneh breakdown" |
| /male-vs-female-african-grey-parrots-for-sale/ | §11 gender | "the male-vs-female guide (DNA-sexing)" |
| /african-grey-vs-macaw/ | §7 | "the full African Grey vs Macaw comparison" |
| /african-grey-vs-cockatoo/ | §8 | "our African Grey vs Cockatoo breakdown" |
| /african-grey-vs-amazon-parrot/ | §9 | "the African Grey vs Amazon comparison" |
| /african-grey-pros-and-cons/ | §14 | "our honest African Grey pros and cons" |
| /african-grey-parrot-breeders-comparison/ | §15 | "how to compare African Grey breeders" |

All 7 also appear in the **§22 ItemList card grid** (schema `ItemList` → 7 `ListItem`s). Contextual link ≠ grid link (vary anchor).

## Down → money / conversion pages
- /congo-african-grey-for-sale/ · /timneh-african-grey-for-sale/ — from §10 variant + §16 cost.
- /available/ hub + 2–3 live bird slugs — from §20 (link-out).
- /buy-african-grey-parrot-near-me/ — from §18 shipping.

## Down → three trust/authority hubs (§12-5 — from their own sections)
- /african-grey-reviews/ — §19 owner/reviews (anchor varied from spokes' usage).
- /african-grey-parrot-faq/ — §21 FAQ intro.
- /buy-african-grey-parrots-with-shipping/ — §18 shipping body.

## Contextual → care / price / species / ethics
- /african-grey-parrot-guide/ (species pillar) — from §3 "what sets greys apart."
- /african-grey-parrot-price/ — from §16 cost.
- /cites-african-grey-documentation/ + /captive-bred-african-grey-parrot/ — from §17 commitment/compliance.
- /is-african-grey-good-for-beginners/ (blog) — from §13 use-case "best beginner parrot" (link OUT, don't re-teach; dup-gate vs it).
- /african-grey-parrot-facts/ (blog) — from §6 intelligence/talking (link, don't duplicate).
- /trusted-african-grey-parrot-breeders/ (About) — author box.

## UP-links to verify on the spokes (hub is the parent)
Confirm each of the 7 spokes links UP to `/african-grey-comparison/` (the "how this fits" line). If any spoke is missing the up-link, add it during the hub build so the hub↔spoke loop is complete (internal-link-agent Step 0 sitemap inventory).

## De-duplication guardrails (CRITICAL for a hub)
- Run `skills/cag-duplicate-content-gate --headers` AND body mode **pairwise vs ALL 7 spokes** before outline approval AND at final pass. The hub's per-rival sections are 2–3-metric SYNTHESES + teaser + link — never spoke prose.
- The master matrix (§4) uses fresh one-line cells, not copied spoke-table rows.
- Vary anchors already spent cluster-wide for reviews/faq/shipping/for-sale pages.

## Backlink strategy (outbound authority + earned)
- **Earn from:** "which parrot should I get" roundups + the quiz sites' resource lists (the selector is linkable), avian-vet/education blogs (the cited best-talking synthesis), Reddit/forum "compare parrots" stickies (fills the aggregator gap).
- **Give to (Link-First):** The Alex Foundation / Pepperberg, World Parrot Trust, AAV, Lafeber find-a-bird, PetMD/Spruce (talking-rank corroboration), CITES, IUCN.

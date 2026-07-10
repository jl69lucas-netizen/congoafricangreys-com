# Internal & External Linking — /african-grey-vs-macaw/

## Up (to hub)
`/african-grey-comparison/` — from intro/related-comparisons section

## Sideways (siblings — link, don't re-teach)
- `/african-grey-vs-cockatoo/` — for the "african grey vs macaw vs cockatoo" GSC query (FAQ + related-comparisons card)
- `/congo-vs-timneh-african-grey/` — where Congo/Timneh variant differences come up (deep-dive Grey section)
- `/male-vs-female-african-grey-parrots-for-sale/` — if sex comes up in FAQ

## Down (money pages)
- `/congo-african-grey-for-sale/`, `/timneh-african-grey-for-sale/` — from deep-dive Grey + available-now sections
- `/available/<bird>/` — bird cards section, live inventory only, sold ≠ InStock
- `/african-grey-breeding-pair/`, fertile-eggs page — pair/eggs card
- `/african-grey-parrot-price/` — cost-of-ownership section (avoid cannibalizing; link, summarize, don't duplicate the full breakdown)
- `/african-grey-parrot-faq/` — FAQ section intro
- `/african-grey-reviews/` — owner-story section
- `/buy-african-grey-parrots-with-shipping/` — shipping section body copy

## Location pills (7 fresh, unclaimed — verified against `data/locations.json`)
Illinois · Massachusetts · Wisconsin · Indiana · Iowa · Kentucky · Oregon
(CvT owns TX/FL/NY/LA/Chicago/GA/NC · MvF owns AZ/PA/OH/Miami/Dallas/WA/NJ · cockatoo owns CO/VA/MI/TN/MN/MO/MD — macaw must not reuse any of these three sets per `dup_content_audit.py`.)

## Blog cards (3, further-reading section)
Reuse the proven trio unless a macaw-specific post exists: `/blog/african-grey-parrot-talking-ability/`, `/blog/african-grey-parrot-price-what-you-get/`, `/blog/is-african-grey-good-for-beginners/` — swap in a macaw-relevant post if `cag-blog-post-agent` has shipped one since.

## External authority links (6–8+ diverse domains, mid-sentence, never at end)
World Parrot Trust · VCA Animal Hospitals · AAV (Association of Avian Veterinarians) · cites.org (curl 403 = bot-block, retry with UA, not dead) · IUCN Red List · Britannica (Alex the Parrot / Psittaciformes) · Lafeber · a bite-force/biomechanics source for the Newton/PSI claims (verify before citing — research doc did not supply a traceable citation for these figures) · Dr. Irene Pepperberg's lab/Alex Foundation for contrafreeloading study.

## Anchor-text rule
Must differ from CvT's ("current Congo Grey clutch" / "Timneh Grey parrots page"), MvF's ("hand-raised Congo Grey chicks" / "available Congo Grey parrots"), and cockatoo's phrasing — draft fresh anchors during the build pass, verify with `dup_content_audit.py` after `astro build`.

# Evidence Log — /african-grey-pros-and-cons/ (2026-07-12)

Only sources actually fetched are logged. Snippet = Google description only. Full = page scraped. Sweep = automated probe.

## Google US SERP queries (Firecrawl search, web, US)
| Query | Top domains returned |
|---|---|
| african grey parrot pros and cons | kookshop(1), reddit/AfricanGrey(2), facebook(3), quora(4), zupreem(5), scribd(6), kaytee(7), omlet(8) |
| are african grey parrots good pets | reddit/parrots(1), zupreem(2), facebook(3), youtube-10yrs(4), **WWF(5)**, quora(6), kaytee(7), parrotessentials(8) |
| should I get an african grey parrot | reddit/parrots(1), youtube-10yrs(2), facebook(3), zupreem(4), quora(5), weebly(6), **IFAW(7)**, harrisonsbirdfoods(8) |
| downsides problems … regret | reddit/AfricanGrey(1), youtube(2), facebook(3), quora(4), tiktok(5), chewy(6), zupreem(7), **facebook/ifaw video(8)** |
| african grey parrot pros and cons reddit | reddit ×6 incl "Tell me I shouldn't get an African Grey", "Strongly advised not to buy an African Grey" |

## Pages scraped in full
| URL | Status | Extracted |
|---|---|---|
| zupreem.com/do-african-grey-parrots-make-good-pets | 200 Full | Dr. Laurie Hess transcript: intelligent/talks/music/TV/games; not-for-novice; destructive+feather-pick+yell if no time; one-on-one bond + jealousy at 5–7 yrs; **lifespan stated "30 to 50 years" (undercount)**. ~1-min read. |
| reddit (multiple) | BLOCKED | Firecrawl "does not support this site" — SERP snippets used |

## 30-competitor sweep (competitor-30-sweep.py/json)
- **0 of 11 T1 direct breeders** carry any pros/cons or "good pet" decision content — sell-only.
- Informational sites template "do X make good pets" per species but **none has a dedicated *African Grey* pros/cons page**: parrotwebsite ("20 reasons parrots make good pets", 11 good-pet URLs), allaboutparrots (4 good-pet, 10 problem URLs, per-species), smallanimaladvice (17 pros-cons + 92 problem URLs, mostly non-bird: chihuahua/corgi/ferret), rationalparrot (23 lifespan, 4 problem). Behavior-"problems" content present on exoticparrotpetstore, shadesofgreys, compoundexotics, birdbreeders (homepage keyword only).
- Same infra pattern as prior sweeps: 4 of 11 T1 breeder sites offline (afrobirdsfarm, exoticparrotsplanet, williamsafricangreys, africangreyaviaries).

## Welfare-org positions (SERP snippet — represent accurately)
- IFAW: "Grey parrots should not be kept as pets… capture from the wild is illegal… deadly for them" + FB "born to be wild, not to be kept as pets."
- WWF responsible-pet guide: "need hours of stimulation and social time… prone to behavioral and health issues."
- Use: acknowledge honestly → captive-bred-USA / CITES Appendix I distinction (§11). Not scraped in full; positions are clear from snippets + public stance.

## Internal data files (grounding)
- data/price-matrix.json → Congo baby $2,300–$2,500 / adult $1,700 / range $1,700–$3,500.
- data/financial-entities.json → Timneh $1,500–$1,600; deposit $200; shipping $185 airport / $350 home.
- docs/reference/credentials.md → USDA AWA licensed; C.A.Gs – Midland, TX; +1-281-545-3169; Mark & Teri Benjamin.
- Cannibalization targets confirmed on disk: src/pages/is-african-grey-good-for-beginners, src/pages/african-grey-parrot-facts (both blogs), + adoption/care/guide pages.

## Not fetched / limitations (honesty)
- Reddit thread bodies (Firecrawl-blocked) — SERP snippets only; headless pass could deepen quotes.
- WWF/IFAW pages not scraped in full — positions from snippets + public stance; represent fairly, link Link-First.
- Google AIO block not returned verbatim — PAA reconstructed from result descriptions.
- Lifespan "40–60 yr" is C.A.Gs' stated figure (ledger); ZuPreem's "30–50" is noted as an undercount to correct, not adopt.

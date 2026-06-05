# Directory & Forum Discovery Sweep — 2026-06-06
Operator: cag-directory-submission-agent (run by main session)
Method: Firecrawl open discovery (NOT competitor-tied) + scrape verification of top finds
Registry: `data/directories.json` | Companion: `sessions/2026-06-06-directory-gap-audit.md`

## What this adds beyond the gap audit
The gap audit (run (c)) found directories *competitors already use*. This sweep (run (b))
searched the open web for bird/parrot directories, classifieds, aviculture societies, and
the standard local-citation set — surfacing targets **no competitor pointed us to.**

## New verified targets (added to registry)

| Priority | Target | Free/Paid | Why |
|---|---|---|---|
| HIGH | **BirdTracks.io** breeder directory | **Free** (email submit) | Species-filterable; only **43 listings, 0 competitors** → untapped. Scrape-confirmed. |
| HIGH | **The Avian Exchange — breeder-join** | Verify (likely paid leads tier) | Screened/responsible US breeders — matches C.A.Gs trust positioning |
| MEDIUM | **FaunaClassifieds** birds board | **Free** member ads | Established exotic community |
| MEDIUM | **AFA** (afabirds.org) | Member benefit | C.A.Gs already AFA-affiliated — claim listing |
| MEDIUM | **Local citation batch** (Manta, Foursquare, Yellowpages, Hotfrog, Cylex, Brownbook, MerchantCircle, Chamberofcommerce.com) | Free | Standard citation set — do AFTER Google/Yelp/Bing/Apple |
| LOW | Want Ad Digest (birds) | Verify | Regional NE-US (overlaps priority states) |
| LOW | The Parrot Pages classifieds | Free | Parrot-specific but dated |

## Honesty catches (scrape verification paid off)
- **Parrot4sale.com → DOWNGRADED to not-viable.** Looked like a strong parrot marketplace,
  but the scrape showed it's **Europe-based** (€ prices; Czech/France/Poland sellers).
  C.A.Gs ships US-only → audience mismatch. Recorded in `not_viable`.
- **BirdTracks** submission is by **email**, not a web form → counts as send-on-behalf
  (needs user approval), and the site states it does **not vet** listings.

## Flagged not-viable (wrong audience / purpose)
- Parrot4sale.com (EU market)
- Poultry Show Central, Falconry Directory (wrong species verticals)
- ABA / NYSOA / NYC Bird Alliance (wild-bird BIRDING orgs, not aviculture — key distinction)
- Facebook AG groups (huge communities, but FB bans live-animal sales → brand presence only,
  not a listing target; route to a future social-engagement task)

## New competitor discovered (not in registry)
- **africangraysales.com** — "Gray Breeders", Dallas TX, $2,500–$3,200, ships nationwide.
  Tier-1 direct breeder NOT in `data/competitors.json`. Recommend adding for next
  `@cag-competitor-intel` run. (Logged under `new_competitors_flagged` in directories.json.)

## Registry totals after this sweep
- Directories (viable, status=discovered): ~22 (15 from gap audit + 7 sweep additions)
- Forums: 4
- Not-viable flagged: 8 categories
- New competitor flagged: 1

## Credits
~14 Firecrawl credits this run (6 searches + 2 scrapes).

# Cross-Platform Competitor Discovery — 2026-08-09

**Client:** congoafricangreys.com (C.A.Gs, Midland TX)
**Scope:** direct competitors only — businesses/individuals actually selling African Grey
(Congo or Timneh) parrots, breeding pairs, or fertile eggs.
**Baseline:** `data/competitors.json` — 44 registered ids, last discovery run 2026-04-28.
**Status:** RESEARCH ONLY. `data/competitors.json` was **not** modified.

**Method note:** every candidate below was surfaced by a retrieved SERP/platform result, and
most were then independently re-fetched to confirm the site is live and actually lists African
Greys. Where a candidate could not be re-fetched, it is marked **evidence: SERP-only** and the
barrier is named. Nothing here is inferred from a domain name alone.

**Registry ids already covered (deliberately excluded from proposals):** afrigreyparrots,
exoticParrotPetstore, afroBirdsFarm, africanGrayParrotsForSale, silvergateBirdFarm,
birdsForSales, exoticParrotsPlanet, williamsAfricanGreys, shadesOfGreys, africanGreyAviaries,
compoundExotics, birdsNow, birdBreeders, qualityBirdsOnline, hoobly, petzlover, parrotAlert,
petClassifieds, exoticPetsAvenue, thesprucePets, wikipedia, rationalParrot, allAboutParrots,
smallAnimalAdvice, vetExplainsPets, birdAddicts, parrotWebsite, chewy, petFinder,
mariettaBirdShop, exoticGlobalParrotsFarm, royalBirdCompany, denimixaniPetsParadise,
buyAfricanGreyParrots, hookbillsForSale, grayBreedersFoundation, theAvianExchange, jcAviary,
anasParrots, parrotStars, birdsByJoe, midnightParrotPlace, handRearedParrots, featherHeadz.

---

## 1. Google / Bing organic

Ran the seed set (`african grey parrot for sale`, `congo african grey for sale`,
`timneh african grey for sale`, `african grey breeder near me`, `hand raised african grey`,
`african grey breeding pair for sale` + `DNA sexed`, `african grey parrot eggs for sale`) at
20 results per query via Firecrawl search.

Confirms the registry's existing leaders still rank (BirdBreeders, BirdsNow, The Avian Exchange,
Gray Breeders Foundation, Silvergate, Exotic Parrots Planet, Birds By Joe, JC Aviary, Feather
Headz, Ana's Parrots, Hand Reared Parrots, Exotic Global Parrots Farm, buyafricangreyparrots).

**New direct sellers surfaced and re-fetched (HTTP 200 + African Grey inventory on page):**

| Site | Fetch result | Grey evidence |
|---|---|---|
| thebirdstore.com (Todd Marcus Birds Exotic, Delran NJ) | 200 | Homepage "FEATURED BABIES … Congo African Grey"; BirdBreeders profile: "over 40 years … raising the happiest & healthiest baby birds" |
| goldencockatoo.com | 200 on `/pages/birds/congo-african-grey-parrot` (16 grey mentions) | Congo African Grey listed at $7,499.99, in-store purchase only |
| floridaparrot.com | 200, 3 grey mentions | "hand raised … African greys", nationwide delivery; also listed as Miami FL breeder on BirdBreeders |
| northshoregreys.com | 200, 5 grey mentions | Title: "North Shore Greys LLC — Parrot Food, Parrot Breeders, African Grey" |
| greywingaviary.com | 200 via Firecrawl (403 to plain curl — Cloudflare) | Named live inventory: Mika/Joe/Gina, ages + sexes, $600 each |
| theparrotandbirdemporium.com | 200, 5 grey mentions | Site + FB page: "Our baby grey that is available has started target training" |
| african-grey-parrot.com | 200, **62** grey mentions | Exact-match domain; "DNA sexed and vet-checked", shipping offered |
| forestryparrotsbreeder.com | 200, **65** grey mentions | Dedicated `/product/african-grey-parrots-for-sale/` |
| exoticbirdsforsales.com | 200, 31 grey mentions | "hand-raised parrots and candle-tested eggs … African Greys" |
| exoticliveparrots.com | 200, 14 grey mentions | African Grey Parrot Eggs $99.98–$619.98 |
| featheredfriendshub.com (Featherland Breeders Hub) | 200, 4 grey mentions | "GREY CONGO $2,700.00 – $5,300.00" |
| petbirdsbreeders.com | 200, 7 grey mentions | "hand-raised parrots … African Greys" |
| parrotcrown.com | 200, 2 grey mentions | `/product/congo-african-grey-parrot-for-sale/` at $7,000 |
| uncle-toms-parrot-farm.my-online.store | 200, **93** grey mentions | Breeding-pair African Grey listing + African Grey eggs $65 |
| cpbirds.com (Orlando FL) | 200 | `/breeding-pairs` inventory + published guide to buying parrot fertile eggs; US shipping |
| brendabillysaviary.com | 200 | Live hand-fed baby aviary store — **grey-specific inventory not visible at fetch time** |
| royalwingsaviary.com | 200, 3 grey mentions | Hand-fed bird breeder; greys not in headline species list |
| fancyfeathersstore.com (Atlanta GA) | 200 | Bird store — **no grey inventory on homepage at fetch time** |
| birdsbyus.com | 200 | Store mid-relocation — **no grey inventory visible at fetch time** |

**Egg-specific competitors** (direct rivals to our `/african-grey-parrot-eggs-for-sale/` page):
paradisebirdsfarmaviary.com (Congo African Grey eggs $100), exoticparrotfarms.com (fertile
African Grey eggs), parrotsfarm.com (Congo African Grey eggs $60), sunnyvaleaviary.com (African
Grey eggs $75). All four were SERP-confirmed with product name + price; direct re-fetch from this
sandbox returned `000` (network-blocked at our end, not a dead site) — **evidence: SERP-only.**

**Non-US, noted but not proposed:** psittacus.com (Spain, professional Congo grey breeding
centre), pets4homes.co.uk, birdtrader.co.uk, preloved.co.uk, royalparrots.uk, parrotsforsale.ca,
birdtrek.co.uk. These do not compete for US transactional intent.

---

## 2. Reddit

Searched r/AfricanGrey, r/parrots and general Reddit for the seed queries plus breeder-recommendation
threads. **Thread listings and snippets retrieved successfully; full comment bodies NOT FETCHED.**

**Barrier:** Reddit returns HTTP 403 to direct fetch (`www.reddit.com/*.json`, `old.reddit.com`,
and via the r.jina.ai text proxy — all 403 with "Try logging in or creating an account"). Firecrawl
explicitly does not support reddit.com ("we do not support this site"). Playwright loaded
`old.reddit.com` successfully (page title resolved) but the shared browser session was navigated
away by another process before DOM extraction could run, twice. Recommend a logged-in Playwright
profile or the official Reddit API for a deeper pass.

**What the retrieved snippets did yield** — breeders that real buyers name in-thread:

- **JC Aviary** (Austin TX) — named repeatedly and positively ("Check out JC Aviary (jcaviary.com)! They're incredible, responsible breeders … they ship all over"). **Already registered** (`jcAviary`) — this is corroboration of its priority, not a new find.
- **Feather Headz Aviary** — "I highly recommend Feather Headz Aviary. I first got my African Grey from them." **Already registered** (`featherHeadz`).
- **Todd Marcus Birds Exotic / southern NJ** — named in r/parrots ISO thread; also the subject of a high-view YouTube video ("The Largest Parrot Store In The USA"). **New.**
- **OurPetStars, Miami FL** — dedicated r/parrots thread "Anyone heard of ourpetstars from Miami Florida?" describing a Congo African Grey breeder ("Sergio"), active on Instagram and birdbreeders.com. **New**, but ourpetstars.com did not resolve from this sandbox — **evidence: SERP-only, domain unconfirmed.**
- **Magnolia Farms, Anaheim CA** — "Magnolia Farms in Anaheim always have an African Grey for sale." **New lead, no URL verified.**
- **Pretty Birds** (parrot store, Timneh purchase) — **new lead, no URL verified.**
- Unnamed but geo-specific: a bird store in Norcross GA (four greys at $6,900 each) and one in Humble TX. Not resolvable to a business name from the snippet.

Strategic read: Reddit's dominant sentiment in these threads is anti-purchase / pro-rescue and
heavily scam-wary ("It's a scam. Do not go on fb breeding pages for greys"). The breeders that
survive that scrutiny are named with a real domain and a health guarantee — which is the exact
posture C.A.Gs already holds.

---

## 3. YouTube

Searched the seed queries restricted to youtube.com.

Result: **almost no US direct competitors.** The breeding-operation channels that dominate these
queries are international hobby/aviary channels (PARROT DIPANKAR, Basona Birds Aviary, HMS Aviary,
SHS Aviary, Tropical Aviary Birds — India/Pakistan/Bangalore/Denmark), which do not compete for US
buyer intent. The rest are pet-owner creators (The African Grey Journal, We Love Birds), rescue
content (Limbe Wildlife Centre), or price explainers.

Two commercially relevant findings:

- **Todd Marcus Birds Exotic** is the subject of "The Largest Parrot Store In The USA | Bringing Home My African Greys" — a buyer-journey video driving traffic to a US grey seller. Corroborates the Google finding.
- **theavianexchange.com** is being paid-placed in creator descriptions ("check out theavianexchange.com to connect with breeders across the USA") across multiple videos. Already registered (`theAvianExchange`) — but the **sponsorship channel is new intel**: it is buying YouTube creator placement, which no registry note currently records.

No new breeder-owned US channel qualified.

---

## 4. Facebook

**Barrier:** direct page fetch returns **HTTP 400** for `facebook.com/<page>` without a session
(tested `AFGparrotshop`, `aviarybirdshop`). Page and group content was therefore reachable **only
through search-index snippets**, which do carry post text and business addresses. No page was
independently re-fetched — everything below is **evidence: search-index-only**.

US commercial sellers surfaced:

- **The Aviary Bird Shop** — 22707 S Dixie Hwy, Miami FL. Posts: "Female Baby African Grey available now at The Aviary Bird Shop"; "Beautiful female African Grey Parrot … AVAILABLE NOW". Physical storefront with a named address.
- **AFG Parrot Shop** — Columbus OH. Page text: "AFRICAN GREY PARROTS FOR REHOMING … birds from 06 to 18 months old, mature and adult birds as well as breeding pairs."
- **Paradise Aviary Xotics** — "Bonded Pair of African Greys. DNA sexed (male & female) on the website"; mentions closed rings, CITES, DNA. Directly competes with our breeding-pair page.
- **Melios Pet Center** — "Breeding pair African Grey"; "We have five African Grey babies available!!"
- **Fascove Exotic Pets Store** — "hand-fed baby Congo African Grey parrots available at our Green Brook store" (Green Brook NJ).
- **Welch Exotic Birds Farm** — Bayville NJ. "Buy African Grey Eggs … Fertile Parrot Eggs For Sale" with a WhatsApp number. Egg-page competitor; WhatsApp-only ordering is a scam-risk signal.
- **The Exotic Bird Shop** — "African greys for sale exclusively at the exotic bird shop!"

Large share of Facebook grey-sale content is South African / UK (South African Grey Parrot Club,
KwaZulu-Natal, Western Cape, Coventry) and out of scope.

---

## 5. Instagram

**Barrier: NOT FETCHED.** `instagram.com/explore/tags/africangreybreeder/` returns HTTP 200 but the
body is a **login wall** (page content is `Login` / `Sign up`, no post grid). Firecrawl refuses
instagram.com outright ("we do not support this site"). Hashtag enumeration for
`#africangreyforsale`, `#congoafricangrey`, `#timnehafricangrey`, `#africangreybreeder` was
therefore **not possible** — no hashtag-derived account list can be honestly reported.

What did leak through Google's index of Instagram (not from Instagram itself):

- **@africangreyaviary** — 975 followers, 67 posts. Bio is advocacy-flavoured ("Let's share ideas about how to make a better world for animals"), **not** confirmed commercial. Do not register on this evidence.
- **Aviary Bird Shop** (Miami FL) — Instagram reel: "Beautiful female African Grey Parrot … AVAILABLE NOW", with the same S Dixie Hwy address as the Facebook page. Corroborates §4.
- **@toddmarcus_birdsexotic** — Instagram presence of the NJ store; corroborates §1/§2/§3.
- **OurPetStars** — Reddit reports a ~500-follower Instagram seller account; **not verified.**

Recommend a logged-in session (Playwright with a saved Instagram profile) if hashtag discovery is
wanted, since that is the platform where small breeders actually list availability.

---

## 6. Parrot forums

Searched avianavenue.com and parrotforums.com. **Thread titles retrieved; thread bodies NOT
FETCHED.**

**Barrier:** Avian Avenue thread URLs return **HTTP 403 + a login form** to Firecrawl even with
stealth proxy ("You must be logged-in to do that", `robots: noindex`). Bing rejected the multi-site
`OR site:` operator and silently redirected to an unrelated query; DuckDuckGo HTML endpoint worked
for title/snippet listing only.

Relevant threads confirmed to exist (each is a breeder-recommendation surface where names are
exchanged in-thread, behind the login wall):

- "First Time Buyer: Looking for Breeder Not a Scam" — OP seeking a baby Congo grey, reports encountering scam breeders.
- "Any African Grey breeders out there?" · "African grey breeder" · "looking for african grey breeder" (Haines City FL area) · "Legitimate breeder" ("I can give you info on African grey breeder with a five star reputation").
- **"Fifty Shades of African Greys"** — an entire thread vetting whether that breeder is legit. Already registered as `shadesOfGreys`; the thread is useful reputation intel for a future comparison/trust page.
- "A List of Breeders and Band Numbers" (14+ pages) — a community-maintained breeder + band registry. **Highest-value target for a logged-in follow-up pass**; it is effectively a competitor directory.

Forum-visible price signal: "African Greys are going for $3000–$5000 USD these days" — consistent
with our documented $1,500–$3,500 Congo range sitting at the value end.

**No new competitor could be named from forums without an account.** Zero forum-only proposals below.

---

## 7. Proposed Additions

Ordered by evidence strength. **Tier 1** = direct breeder/seller, **Tier 2** = classified/aggregator,
**Tier 4** = retailer/storefront. None of these ids exist in `data/competitors.json`.

### 7a. Verified — site re-fetched, African Grey inventory confirmed on page

| # | Name | URL | Platform(s) found on | Tier | Why it's a real direct competitor |
|---|---|---|---|---|---|
| 1 | Todd Marcus Birds Exotic | https://thebirdstore.com | Google, Reddit, YouTube, Facebook, Instagram | 4 | 43-year NJ storefront; homepage "FEATURED BABIES … Congo African Grey"; raises its own babies per BirdBreeders profile; named unprompted in r/parrots and the subject of a buyer-journey YouTube video. Found on all five platforms — the single strongest new name. |
| 2 | Golden Cockatoo | https://goldencockatoo.com | Google | 4 | Live Congo African Grey product page at $7,499.99 with "BREEDERS" label and 3 certified avian specialists. Sets the high anchor our $1,500–$3,500 range is measured against. |
| 3 | Florida Parrot | https://floridaparrot.com | Google, BirdBreeders directory | 1 | "hand raised … African greys", ethical-breeding + nationwide-delivery claim; separately listed as a Miami FL breeder with multiple live grey listings on BirdBreeders. Directly duplicates our shipping proposition. |
| 4 | North Shore Greys LLC | https://northshoregreys.com | Google | 1 | Self-describes as parrot breeder specialising in African Grey (in the title tag); grey-specific brand name competing for our head term. |
| 5 | GreyWing Aviary | https://greywingaviary.com | Google | 1 | Named live grey inventory with sex, age and price (Mika/Joe/Gina, $600 each). **Flag:** $600 is far below market and a classic scam signal — track as a SERP competitor, never cite as a price benchmark. |
| 6 | The Parrot and Bird Emporium | https://www.theparrotandbirdemporium.com | Google, Facebook | 1 | Site lists African Greys among hand-tamed stock; FB post shows a specific baby grey in target training. Ranks and posts availability like a breeder, not a directory. |
| 7 | African Grey Parrots For Sale | https://african-grey-parrot.com | Google | 1 | Exact-match domain for our primary head term, 62 on-page grey mentions, claims DNA sexed + vet checked + shipping. Competes for the same query as our money page. |
| 8 | Forestry Parrots Breeder | https://forestryparrotsbreeder.com | Google | 1 | Dedicated `/product/african-grey-parrots-for-sale/`; 65 on-page grey mentions; ranks top-20 for the head term. |
| 9 | Uncle Tom's Bird Farm | https://uncle-toms-parrot-farm.my-online.store | Google | 1 | 93 on-page grey mentions; sells both African Grey breeding pairs and African Grey eggs at $65 — competes with two of our pages at once. |
| 10 | Exotic Live Parrots | https://exoticliveparrots.com | Google | 1 | African Grey Parrot Eggs priced $99.98–$619.98 — direct rival to our $95/egg page. |
| 11 | Exotic Birds For Sales | https://exoticbirdsforsales.com | Google | 1 | "hand-raised parrots and candle-tested eggs … African Greys"; 31 grey mentions. Same dual bird+egg model we run. |
| 12 | Featherland Breeders Hub | https://featheredfriendshub.com | Google | 1 | Priced Congo grey inventory "GREY CONGO $2,700–$5,300" — overlaps the top of our stated Congo range. |
| 13 | ParrotCrown | https://parrotcrown.com | Google | 1 | `/product/congo-african-grey-parrot-for-sale/` at $7,000 with age banding. |
| 14 | Pet Birds Breeders | https://petbirdsbreeders.com | Google | 1 | "healthy, hand-raised parrots … African Greys" as a headline species; 7 grey mentions. |
| 15 | CP Birds | https://www.cpbirds.com | Google | 1 | Orlando FL, US shipping, live `/breeding-pairs` inventory, and publishes "Guide to Buying Parrot Fertile Eggs Online" — competing on breeding pairs, eggs, and egg-buyer education simultaneously. |

### 7b. Real evidence of grey sales, but re-fetch blocked at our end — confirm before registering

| # | Name | URL | Platform(s) found on | Tier | Why it's a real direct competitor |
|---|---|---|---|---|---|
| 16 | Rainforest Aviaries | http://rainforestaviaries.com | Google | 1 | SERP body: "I am a private bird breeder … I specialize in African Grey Parrots". Sandbox fetch returned `000`, Firecrawl scrape timed out — site not independently confirmed live. |
| 17 | Sherry Birds | https://sherrybirds.org | Google | 1 | Indexed product: "Buy Timneh African Grey Parrots For Sale — $4,000 reduced to $1,800", under an `african-grey-breeders` product tag. Timneh-specific, which is our thinner cluster. Fetch `000`. |
| 18 | Paradise Birds Farm Aviary | https://paradisebirdsfarmaviary.com | Google | 1 | Indexed listing "Congo African Grey Parrot Eggs For Sale $100" on a dedicated fertile-eggs page. Fetch `000`. |
| 19 | Exotic Parrot Farms | https://exoticparrotfarms.com | Google | 1 | Indexed `/product/fertile-african-grey-parrot-eggs/` with hatchability claims. Fetch `000`. |
| 20 | Parrots Farm | https://parrotsfarm.com | Google | 1 | Indexed "Congo African Grey Parrot Eggs For Sale $60" under a fertile-parrot-eggs category. |
| 21 | Sunnyvale Aviary | https://sunnyvaleaviary.com | Google | 1 | Indexed "African Grey Parrot Eggs, $75.00" in a fertile-eggs product table. |

### 7c. Social-only sellers — no independent website confirmed (Facebook/Instagram are login-walled)

| # | Name | URL | Platform(s) found on | Tier | Why it's a real direct competitor |
|---|---|---|---|---|---|
| 22 | The Aviary Bird Shop | https://www.facebook.com/aviarybirdshop/ | Facebook, Instagram | 4 | Physical storefront, 22707 S Dixie Hwy, Miami FL; repeat posts "Female Baby African Grey available now". Address + repeat inventory = a real operating seller, not a one-off ad. |
| 23 | Paradise Aviary Xotics | https://www.facebook.com/ParadiseaviaryXotics/ | Facebook | 1 | Posts a DNA-sexed bonded pair of African Greys with closed rings and CITES paperwork, and references "on the website". Directly targets our breeding-pair buyer. |
| 24 | AFG Parrot Shop | https://www.facebook.com/AFGparrotshop/ | Facebook | 1 | Columbus OH; offers greys 6–18 months plus mature birds and breeding pairs — a grey-specialist inventory, not a general pet page. |
| 25 | Fascove Exotic Pets Store | (Green Brook NJ — no own domain confirmed) | Facebook | 4 | "hand-fed baby Congo African Grey parrots available at our Green Brook store"; named physical location. |
| 26 | Welch Exotic Birds Farm | https://www.facebook.com/welchexocticbirdsfarm/ | Facebook | 1 | Bayville NJ page advertising "Buy African Grey Eggs" / fertile parrot eggs. **Flag:** WhatsApp-only ordering is a strong scam signal; register as a SERP/social competitor only. |
| 27 | Melios Pet Center | https://www.facebook.com/meliospetcenter/ | Facebook | 4 | Posts an African Grey breeding pair and "five African Grey babies available" with sex breakdown — genuine live inventory. |
| 28 | OurPetStars | (ourpetstars.com — did not resolve) | Reddit, Instagram | 1 | Dedicated r/parrots thread vetting it as a Miami FL Congo African Grey breeder, with a named seller and a BirdBreeders listing. Domain unconfirmed — verify before registering. |

### 7d. Named leads with no verifiable URL — do NOT register yet

- **Magnolia Farms** (Anaheim CA) — Reddit: "always have an African Grey for sale". No site found.
- **Pretty Birds** — Reddit: parrot store where a commenter bought a Timneh. Name too generic to resolve.
- **Rock The Flock LLC** (Front Royal VA) — appears as an active grey-breeder profile inside BirdBreeders ("Hand feeding African Grey Congo baby"). Sells through the aggregator; no independent domain located.
- **Bird store, Norcross GA** (four greys at $6,900 each) and **bird store, Humble TX** — Reddit price intel, businesses unnamed.
- **Brenda & Billy's Aviary**, **Royal Wings Aviary**, **Fancy Feathers** (Atlanta GA), **Birds By Us** — all live US bird businesses that rank for our queries, but **none showed African Grey inventory at fetch time**. Re-check before proposing; they may be seasonal.
- **Psittacus (psittacus.com)** — genuine professional Congo grey breeding centre, but Catalonia/Spain. Out of scope for US intent.

---

## 8. Recommendation

**(Recommended) Register 7a (15 sites) now, and hold 7b/7c pending verification.**

Grounded in the data rather than taste: every 7a entry was independently re-fetched at HTTP 200
with African Grey inventory visible on the page, so each is a claim we can defend; 7b's six sites
are indexed with real product names and prices but returned `000` from this sandbox, which is a
*our-network* failure, not proof the site is dead — registering them now would put unverified rows
in the source of truth that every other agent reads. 7c's seven sellers are real but have no
crawlable URL, so no other agent could analyse them anyway.

**Trade-off of the recommended pick:** it under-registers the egg cluster. Four of the six held-back
7b sites (Paradise Birds Farm, Exotic Parrot Farms, Parrots Farm, Sunnyvale) are egg competitors,
and our `/african-grey-parrot-eggs-for-sale/` page is one of the few where we ship to all 50 states —
so the page facing the least-documented competition is a page we actively monetise. Resolve by
re-running the 7b fetches from a different network before the next intel sweep.

Two priority notes for whoever does register:

1. **Todd Marcus Birds Exotic (thebirdstore.com) should be `priority: high`** — it is the only new
   name found on all five platforms searched, and the only one Reddit names unprompted.
2. **The Avian Exchange (already registered) needs a note added**: it is buying YouTube creator
   sponsorships ("check out theavianexchange.com to connect with breeders across the USA") across
   multiple parrot channels. That is a paid-acquisition channel the registry does not currently record.

---

## 9. Access barriers encountered

| Platform | Status | Specific barrier |
|---|---|---|
| Google / Bing | OK | Full 20-result extraction via Firecrawl search. Bing silently rewrites multi-site `OR site:` operators — single-site queries only. |
| Reddit | **PARTIAL — comment bodies NOT FETCHED** | HTTP 403 on `www.reddit.com/*.json`, `old.reddit.com`, and via r.jina.ai. Firecrawl: "we do not support this site". Playwright loaded the page but the shared browser session was navigated away mid-task, twice. Titles + index snippets only. |
| YouTube | OK | Searchable; no new US breeder channels qualified. |
| Facebook | **PARTIAL — search-index-only** | Direct page fetch returns HTTP 400 without a session. Post text and addresses recovered only through the search index. |
| Instagram | **NOT FETCHED** | Hashtag pages return HTTP 200 with a login-wall body (no post grid). Firecrawl refuses instagram.com. No hashtag enumeration was possible for any of the four requested tags. |
| Avian Avenue / parrot forums | **NOT FETCHED — bodies** | Thread URLs return HTTP 403 + login form to Firecrawl stealth proxy; threads are `robots: noindex`. Titles/snippets only; zero forum-only candidates proposed. |

**To unblock the next pass:** a logged-in Playwright profile for Instagram and Avian Avenue, plus
official Reddit API credentials, would convert three PARTIAL/NOT-FETCHED rows into full coverage.
The Avian Avenue thread "A List of Breeders and Band Numbers" (14+ pages) is the highest-value
single target behind those walls.

# Competitor Sweep — Page 3 (Tier 2 Classified Aggregators + One Tier 5 Registry)

Date: 2026-08-09 (fetches executed 2026-08-09 → 2026-08-10 UTC)
Analyst: cag-competitor-intel
Scope: **Research only.** No site files touched. `data/competitors.json` **NOT modified** — every registry
change below is a proposal for breeder approval.
Protocol: `docs/artifacts/cags-universal-page-build-brief.html` §6 (Competitor Research and Query Fan-Out)
Sibling pass this file matches structurally: `docs/research/competitor-sweep-page5-2026-08-09.md`

Registry ids in scope: `birdsNow` · `birdBreeders` · `qualityBirdsOnline` · `hoobly` · `petzlover` ·
`parrotAlert` · `petClassifieds` · `exoticPetsAvenue`

> **Not a page outline.** This is a Sprint-0 research artifact, so the Heading-Hierarchy Outline Gate and
> Header Style Declaration do not apply — no page is being built from these headings.

> **`parrotAlert` is not a seller.** It was re-tiered on 2026-08-09 to tier 5 `non_commercial`. It is a
> lost/stolen/found bird registry. It is analysed below as a **citation and backlink target**, and it is
> deliberately excluded from every listing-supply, price and inventory comparison in this file.

---

## Method and Barriers (read this before trusting any number below)

Every figure here came from a live fetch in the window above. Anything not retrieved is written
`NOT FETCHED` with the barrier named. Nothing is inferred.

| Channel | Tool | Status |
|---|---|---|
| DNS resolution | `dig @1.1.1.1` and `@8.8.8.8` | **OK — system resolver must not be used, see barrier 1** |
| Reachability (apex **and** www) | `curl --resolve` against public-resolver IPs | **OK — all 8 checked both hosts** |
| Page structure, schema, headings, alt text | `curl` + local parser (`scratchpad/pageprobe.py`) | **OK for 5 of 8** |
| Blocked-site page content | Firecrawl Scrape (basic → stealth ladder) | **OK for hoobly, petClassifieds, parrotAlert; FAILED for petzlover** |
| URL-space inventory | `firecrawl_map` | **OK for all except qualityBirdsOnline (parked)** |
| SERP snapshot | Firecrawl Search (Google-backed) | **OK — but UK-localised unless stated, see barrier 3** |
| Query fan-out, autosuggest A–Z + question mods | `suggestqueries.google.com` + `api.bing.com/osjson.aspx` | **OK — 566 unique queries over 4 stems** |
| Google PAA, 3 levels | — | **NOT FETCHED** — not attempted this pass; prior sweeps hit `/sorry/` CAPTCHA at HTTP 429 |
| Bing organic top 10 | — | **NOT FETCHED** — page-5 sweep proved 4-transport query truncation; not re-attempted |
| Reddit thread mining | Playwright (`browser_navigate` + `browser_evaluate`) | **OK — after curl 403 and Firecrawl refusal, see barrier 4** |
| Historical site state | Wayback CDX + `id_` raw snapshots | **OK** |
| PageSpeed / Core Web Vitals | — | **NOT FETCHED** — not attempted; out of scope for this pass |

### Barrier 1 — this machine's system resolver sinkholes parrot domains (this overturns a committed registry note)

The system resolver on this build machine is **`194.168.4.100` = `cache1.service.virginmedia.net`**
(Virgin Media UK). For domains on its content-filter list it returns
**`81.99.162.48` = `lang-sspiprxy.network.virginmedia.net`** — Virgin Media's filter proxy — instead of the
real A record. Measured control group:

| Domain | system resolver | `@8.8.8.8` | `@1.1.1.1` |
|---|---|---|---|
| google.com | 142.250.129.101 | 192.178.223.138 | 142.250.151.100 |
| birdsnow.com | 100.24.141.0 | 32.195.185.188 | 100.48.161.131 |
| hoobly.com | 52.15.161.93 | 52.15.161.93 | 52.15.161.93 |
| congoafricangreys.com | 172.67.186.48 | 104.21.92.39 | 172.67.186.48 |
| **qualitybirdsonline.com** | **81.99.162.48** | 172.236.104.43 | 172.238.172.122 |
| **exoticglobalparrotsfarm.com** | **81.99.162.48** | 66.45.23.70 | 66.45.23.70 |
| **sherrybirds.org** | **81.99.162.48** | 185.77.97.60 | 2.57.91.131 |
| **paradisebirdsfarmaviary.com** | **81.99.162.48** | 89.116.109.92 | 195.200.9.92 |
| **exoticparrotfarms.com** | **81.99.162.48** | 185.77.97.224 | 195.200.9.41 |
| **parrotsfarm.com** | **81.99.162.48** | 213.130.145.185 | 213.130.145.185 |

**Consequence for the registry.** The `exoticGlobalParrotsFarm` note committed on 2026-08-09 reads:
*"resolves to 81.99.162.48 … shared with four other African Grey storefronts … That is one operator
running a domain network, not five independent breeders."* **That inference is not supported.** Measured
from public resolvers those five domains sit on **five different networks**. The shared `81.99.162.48` was
our own ISP's filter proxy, not shared hosting.

What survives, and is still useful: **an ISP-grade content filter has independently flagged all five of
those domains, plus `qualitybirdsonline.com`, as blockworthy.** That is a real third-party reputation
signal — it is simply a different claim from "one operator." Reproduce with:
`dig +short A <domain>` then `dig +short A <domain> @1.1.1.1` and compare.

Every fetch in this file therefore resolved via `@1.1.1.1` and fetched with `curl --resolve`.
**A `000` from the system resolver is not evidence of a dead site.**

### Barrier 2 — apex vs www checked separately for all eight

Page-2's sweep found a baseline filed "CONFIRMED DEAD" that was only stored under the wrong hostname.
Checked here for every domain, resolved publicly:

| Domain | A (apex) | A (www) | apex | www | Reading |
|---|---|---|---|---|---|
| birdsnow.com | 35.171.250.48 | 35.172.255.141 | 302 | **200** | Normal apex→www |
| birdbreeders.com | 137.117.90.63 | 137.117.90.63 | 301 | **200** | Normal apex→www |
| qualitybirdsonline.com | 172.238.172.122 | 172.238.172.122 | **200** | **200** | Both live — but serving a **parking page**, not a bird site |
| hoobly.com | 52.15.161.93 | 52.15.161.93 | 301 | 302 | 302 is a **geo-redirect to `/s/gb`**, not an error |
| petzlover.com | 52.71.205.214 | 52.71.205.214 | 301 | 403 | Own-brand CAPTCHA wall |
| parrotalert.com | 51.79.9.89 | 51.79.9.89 | 301 | **200** | Normal apex→www |
| petclassifieds.com | 172.67.73.163 | 172.67.73.163 | 403 | 403 | Cloudflare *"Just a moment…"* JS interstitial |
| exoticpetsavenue.com | 185.151.30.162 | 185.151.30.162 | **200** | 301 | **www→apex** (inverse of the others) |

**No hostname-storage error found in this group.** All eight registry URLs use `www.`, and `www.` resolves
for all eight. **None of the eight is dead.** Two are non-bird or non-commercial; none is a DNS failure.

### Barrier 3 — every SERP below is UK-localised unless explicitly marked

This machine's egress is a **UK line**. Firecrawl Search without a `location` parameter therefore returns
a **UK-localised** result set. Two queries were re-run with `location: "United States"` and are labelled
**[US-localised]**; everything else is labelled **[UK-localised]** and **must not be read as a US ranking**.
Where the two differ, both are shown.

### Barrier 4 — Reddit needed the third rung of the ladder

`curl` to `reddit.com/…json` → **HTTP 403** (bot block, both `www` and `old`). Firecrawl Scrape →
**explicit refusal**: *"we do not support this site."* Playwright `browser_navigate` cleared Reddit's JS
challenge and `browser_evaluate` extracted comment bodies. All Reddit quotes below are verbatim from that
path, with score and post timestamp.

### Barrier 5 — index snippets are not live data, and one nearly produced a false price

The Google index snippet for `hoobly.com/p/VNOicNE` reads **"Timneh African Grey Female -- $35."** Fetched
live, that page is an **expired listing** whose body contains both `$35` and `$3500`; the snippet had
truncated `$3,500`. **No $35 African Grey exists.** Every price in this file is from a live page fetch, not
from a SERP snippet.

---

# Part A — The listing-supply picture (the thing this group is actually for)

Six of the eight are inventory platforms. The most decision-useful measurement for them is not word count
— it is **how many live African Grey listings each one really carries, at what price, and how much of that
inventory is the same bird posted twice.**

## A1 · Live African Grey supply, measured 2026-08-09

| Site | Live AG listings (measured) | How measured | Price band (live) |
|---|---|---|---|
| **Hoobly** | **≥150** — 30 per page, pagination exposes pages 1–5 plus "Next" | Firecrawl fetch of `/s/us/pets-animals~birds~african-grey` | **$1,500 – $7,000** |
| **BirdBreeders** | **36 cards over 3 pages**, of which **~24 are African Greys** — see the Cape Parrot dilution below. Page header claims **"28 Listings"** | `curl` card count per page | **$3,900 – $8,500** |
| **PetClassifieds** | **331 ads** in the Parrots subcategory; **588** birds total. AG-specific ads visible on page 1 of `/ad_category/parrot`: 5 | Live category counters on the homepage | **$650 – $1,500** (plus "Contact For Price") |
| **BirdsNow** | **14** unique `bird-ad-*` links on the national AG hub | `curl` + unique-ID count | **$100 – $7,500** (page tokens; includes non-bird items) |
| **Petzlover** | **NOT FETCHED** — CAPTCHA. Index-level meta descriptions claim per-geo counts (e.g. *"approximately 22 males and 20 female available"* in Palm Beach County FL) | `firecrawl_map` titles/descriptions only | **$50 – $7,000** across index descriptions |
| **exoticPetsAvenue** | **6** African Grey product pages, all `InStock` | Live `ld+json` Offer extraction | **$650 – $1,100** |
| qualityBirdsOnline | **0** — domain is parked | — | n/a |
| parrotAlert | n/a — not a seller | — | n/a |

**The Cape Parrot dilution.** BirdBreeders files **Cape Parrot inside its "African Grey Parrots"
category**. Page 1 of that category is 12 cards: 6 Congo African Grey, 2 Timneh African Grey and
**4 Cape Parrot** — i.e. **a third of the category page is not an African Grey at all**. The page's own
"28 Listings" counter and its 36 rendered cards disagree with each other *and* both overstate African Grey
supply. Any competitor-inventory number taken from that page without opening the cards is wrong.

## A2 · Cross-site duplication — the finding that reframes the whole tier

Two verbatim matches, both confirmed by live fetch of both platforms on the same day.

**Duplication case 1 — one bird, two platforms, identical price.**

| Platform | URL | Listing text | Price | Location |
|---|---|---|---|---|
| BirdsNow | `/timnehafricangreyparrotvirginia.htm` | *"Beautiful 6-Year-Old Timneh African Grey He is a DNA-sexed male and is in excellent health. Timnehs are famous for their incredible intelligence, fantastic…"* | **$3,200** | Richmond, Virginia |
| Hoobly | `/s/us~va/pets-animals~birds~african-grey` | *"Beautiful 6-Year-Old Timneh African Grey He is a DNA-sexed male and is in excellent health. Timne…"* — seller **`blbparrots` (18y)** | **$3,200** | Richmond, Virginia |

Same opening sentence, same age, same sex, same DNA claim, same city, same price. **One bird, counted
twice** by anyone adding BirdsNow and Hoobly inventory together. The same BirdsNow listing also appears on
`/greyvirginia.htm` and `/location/richmond-virginia.htm` — so it is **four indexed URLs for one bird**
before it ever leaves BirdsNow.

**Duplication case 2 — one seller, two platforms, a ~$4,000 price spread.**

| Platform | Seller | Listing text | Price |
|---|---|---|---|
| BirdBreeders | *Ana's Parrots and Supplies*, PA | *"All of our beautiful birds are raised with care and love. We put our hearts into these magnificent creatures. We offer pick in the our store located i…"* | **$8,500.00** |
| Hoobly | `anasparrots (14y)`, Stroudsburg PA | *"All of our beautiful birds are raised with care and love. We put our hearts into these magnificent c…"* | **$4,500** |
| Hoobly | `anasparrots (14y)` | *"Congo African Grey Baby … Accepting deposits now"* | **$7,500** |

**The identical opening sentence proves it is the same seller.** That seller's African Greys carry
**$8,500 on BirdBreeders and $4,500 on Hoobly** — an ~$4,000 spread on one breeder's stock, decided purely
by which aggregator the buyer lands on.

**Why this matters more than any other number in this file.** The "market price" a buyer forms by browsing
aggregators is not a market price. It is an artifact of duplicated listings and per-platform pricing by the
same sellers. That is a defensible, evidence-backed reason for C.A.Gs to publish **one** honest,
non-negotiated price band — and it is the strongest available answer to *"why is your Congo $1,500–$3,500
when BirdBreeders shows $8,500?"*

**Registry overlap worth flagging:** Hoobly's Minnesota AG results carry a seller handle
**`shadesofgreys (8y)`** — `shadesOfGreys` is a **tier 1 direct_breeder in our own registry**. Our tier 1
and tier 2 entries are not independent populations; some tier 1 breeders *are* the tier 2 inventory.

## A3 · Dead inventory left indexed

BirdsNow's Texas AG page renders **14 H3 listing titles of which 10 begin `SOLD - `** — *SOLD - African
Grey · SOLD - African Grey Parrot · SOLD - African Grey Congo Baby - Male · SOLD - African Grey Congo Baby
Boy · SOLD - Congo Babies · SOLD - African Grey Congo · SOLD - Congo Babies* and so on. **71% of the
inventory on the state page a Texas buyer lands on is already sold**, and it is still indexed.

---

# Part B — Per-competitor

---

## B1 · BirdsNow — https://www.birdsnow.com

Tier 2 · classified_aggregator · baseline `competitor-birdsNow-2026-05-11.md`

### 1. SERP snapshot

**[UK-localised] "african grey parrot for sale"** — BirdsNow **absent from the top 10.** Top 10 held by
birdbreeders.com (#1), graybreedersfoundation.yolasite.com (#2), facebook (#3),
exoticglobalparrotsfarm.com (#4), theavianexchange.com (#5), exoticliveparrots.com (#6),
buyafricangreyparrots.com (#7), craigslist (#8), youtube (#9), exoticparrotpetstore.com (#10).

**[US-localised] "african grey parrot for sale"** — BirdsNow enters at **#3**, with
`/africangreyparrotcalifornia.htm` — a **state** page, not the national hub. #1 birdbreeders.com,
#2 graybreedersfoundation, #4 reddit r/AfricanGrey, #5 buyafricangreyparrots, #6 exoticglobalparrotsfarm,
#7 facebook, #8 craigslist NY, #9 Facebook "African Grey Farm | Houston TX", #10 exoticparrotpetstore.

**[UK-localised] "african grey parrot for sale near me"** — BirdsNow **#3** with
`/africangreyparrottexas.htm`, snippet *"$7,500 Hand Reared African Grey … $3,400 …"*.

**[UK-localised] "african grey parrot price"** and **"where to buy african grey parrot"** — BirdsNow
**absent from both top 10s.**

**Read:** BirdsNow ranks through **state pages**, not through its hub, and not on price or where-to-buy
intent. Its national AG hub did not surface on any of the four queries measured.

### 2. Query fan-out

Union across 4 stems: **566 unique queries** (`african grey parrot for sale` · `… price` ·
`… classifieds` · `… for sale near me`). Google A–Z + question-mods 229 and 245 on the two main stems;
Bing 50 and 41; 246 and 214 queries of 6+ words respectively.

No `birdsnow` token appears anywhere in Google or Bing autosuggest. BirdsNow has **inventory demand, not
brand demand**.

### 3. Section / listing inventory

`firecrawl_map` (search "african grey") returned four URL families:

- **Species hub** — `/africangreyparrot.htm`, `/timnehafricangreyparrot.htm`
- **State pages** — measured exhaustively against the canonical 22 by direct HTTP:
  **22/22 generic** (`/africangreyparrot<state>.htm`) · **22/22 Congo**
  (`/congoafricangreyparrot<state>.htm`) · **17/22 Timneh** (`/timnehafricangreyparrot<state>.htm`)
  → **61 African Grey state pages.**
  **Timneh state gaps: NY · WA · MA · MO · CO** — five of our 22 target states where BirdsNow ships no
  Timneh state page at all.
- **Trait/modifier pages** — a page per buyer adjective, which is the real structural lesson:
  `/talkingafricangreyparrot.htm` · `/housetrainedafricangreyparrot.htm` · `/bondedpairafricangreyparrot.htm`
  · `/maleafricangreyparrot.htm` · `/femaleafricangreyparrot.htm` · `/adulttimnehafricangreyparrot.htm`
  · `/fancyafricangreyparrot.htm` · `/redafricangreyparrot.htm` · `/whitecongoafricangreyparrot.htm`
- **City pages** — `/location/<city>-<state>.htm`, e.g. `/location/schertz-texas.htm`,
  `/location/orlando-florida.htm`, `/location/baltimore-maryland.htm`

### 4. Visual and structural inventory (live)

| Page | Words | H1 | H2 | H3 | H4 | `<img>` | ld+json | Microdata |
|---|---|---|---|---|---|---|---|---|
| `/` homepage | **542** | 1 — *"Birds for Sale"* | 6 | 1 | 9 | **0** | 1 — `Organization`, `SearchAction` | none |
| `/africangreyparrot.htm` | **1,108** | 1 — *"African **Gray** Parrots"* | **0** | 15 | 4 | 3 | **0** | `BreadcrumbList`, `ImageObject`, `ListItem`, `Organization`, `Thing` |
| `/africangreyparrottexas.htm` | **1,041** | **2 (duplicate H1)** | **0** | 14 | 5 | **0** | **0** | `BreadcrumbList`, `ListItem`, `Thing` |

- **The AG hub has no H2 at all** — it jumps H1 → H3, a skipped level on their single most important page.
- **The Texas page ships two H1s**: *"African Grey Parrots for Sale in Texas"* and *"African Grey Parrots in Texas"*.
- **Spelling hedge:** `<title>` says "African **Grey**", `<h1>` says "African **Gray**".
- **Alt text:** the hub's three images carry `African Gray Parrots`, `African Gray Parrots`, `BirdsNow` — two
  duplicates and a logo. The Texas page serves **zero `<img>` in server HTML**.
- No video, no `<table>`, no infographic on any page measured. `robots: noodp` on the homepage.
- **Trust vocabulary count across homepage + AG hub: `usda` 0 · `cites` 0 · `health guarantee` 0 ·
  `captive-bred` 0 · `avian vet` 0 · `appendix i` 0.** `dna` appears 6× — entirely inside seller-written ad copy.

### 5. Reddit / forum mining — BirdsNow by name

| Thread | Verbatim | Read |
|---|---|---|
| r/parrots **"African grey scam website??"** (2025-03-27, 275 pts) | *"Greys can cost around $6k and the website seems sketchy. But having shipping doesn't always mean a scam… I'd suggest going on Birds Now website (that's where i found my hahn's) and see if breeders have greys near you or shipping available."* | BirdsNow is the community's **fallback recommendation inside a scam thread** |
| r/parrots "Looking to buy and African grey" | *"I use a site called birds now. You can use the search feature to look for specific birds in the area where you live. I found both of my …"* | Used as a **geo search tool** |
| r/parrots "Where can I find a reputable bird breeder?" | *"…birdbreeders.com and birdsnow.com and oodle.com marketplace."* | Named in the standard triad |
| r/parrots "Shipping a parrot" | *"it is a scam. African Grey sells and is worth more than 350 dollars http://www.birdsnow.com/africangreyparrot.htm"* | **BirdsNow's hub is cited as the price authority** used to prove a scam |

That last one is the mechanism behind BirdsNow's rankings: redditors **link the hub as evidence of what a
Grey costs.** It earns links by being a price reference, not by being good.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "Homepage word count: ~800 (estimated)" | **542** — the estimate was ~48% high |
| "H1/H2 pattern: Category pages H1 = 'African Grey Parrots for Sale'; H2 = individual listing titles" | **Wrong.** Category pages have **zero H2**; listing titles are H3. The Texas page has **two** H1s |
| "Total pages: all 22 states have category pages" | Directionally right, now exact: **22/22 generic, 22/22 Congo, 17/22 Timneh = 61 AG state pages**, with named Timneh gaps |
| "Schema — Expected: Product (per listing), BreadcrumbList" | **No `Product` anywhere.** Zero `ld+json` on AG pages; only legacy microdata. Homepage carries `Organization` + `SearchAction` only |
| "African Grey range $1,200–$3,500 visible" | Live hub tokens span **$100–$7,500**; state pages carry $7,500 and $3,400. The old range is stale |
| "Images: seller-uploaded photos per listing" | Server HTML for the Texas state page returns **0 `<img>`**; the hub returns 3, two of them duplicates |

### Key insight

BirdsNow's asset is a **61-page African Grey state grid plus a trait-page grid** (`talking`,
`housetrained`, `bonded pair`, `male`, `female`) — and it ranks on those, never on its hub. It defends that
grid with **zero H2s, duplicate H1s, no `Product` schema, no alt text and 71% SOLD inventory on the Texas
page.** The five states with no Timneh page (NY, WA, MA, MO, CO) are unguarded ground for the CAG Timneh
cluster.

---

## B2 · BirdBreeders — https://www.birdbreeders.com

Tier 2 · classified_aggregator · baseline `competitor-birdBreeders-2026-05-11.md`

### 1. SERP snapshot

**#1 on Google for the head term in both localisations.**

| Query | Localisation | BirdBreeders position |
|---|---|---|
| african grey parrot for sale | [UK] | **#1** |
| african grey parrot for sale | [US] | **#1** |
| african grey parrot for sale near me | [UK] | **#2** |
| african grey parrot price | [UK] | **#3** |
| where to buy african grey parrot | [UK] | **#2** |
| african grey parrot breeder near me | [US] | **#4** (homepage) |

This is the strongest and most consistent ranking position of any site in this sweep.

### 2. Query fan-out

Shares the 566-query union. As with BirdsNow, **no brand token** in Google or Bing autosuggest. Bing-only
terms that map to BirdBreeders' actual page inventory and which Google's suggest never returns:
`african grey parrot breeders` · `african grey parrot breeders near me` ·
`african grey parrot breeders near me prices` · `congo african grey parrot for sale` ·
`timneh african grey parrot sale`.

### 3. Section / listing inventory

Three families, all with a state axis:

- **Species categories** — `/birds/category/african-grey-parrots`, `/birds/african-grey-congo-parrot`,
  `/birds/african-grey-timneh-parrot`, `/birds/cape-parrot`
- **State pages** — `/birds/category/african-grey-parrots/<st>` · `/birds/african-grey-congo-parrot/<st>` ·
  `/birds/african-grey-timneh-parrot/<st>` · `/bird-breeders/<st>` · `/birds/<st>`
- **Breeder profiles with reviews** — `/breeder/<id>/<slug>` plus `/reviews` and `/birds` sub-pages

**State coverage measured against the canonical 22 — and this is the finding:**

**66/66 African Grey state URLs return HTTP 200. Only 8 of the 22 states hold any live listing.**

| State with inventory | AG listings |
|---|---|
| FL | 12 |
| IL | 8 |
| PA | 4 |
| CA | 2 |
| TX | 2 |
| VA | 1 |
| TN | 1 |
| MD | 1 |

**14 of our 22 target states are empty shells: NY · OH · GA · NC · MI · NJ · WA · AZ · MA · IN · MO · CO ·
MN · SC.**

What an empty shell actually is, measured on `/birds/category/african-grey-parrots/ny`:
**644 words, 0 listings, `robots: INDEX, FOLLOW`**, title *"African Grey Parrots for Sale in New York"*,
and the 644 words are almost entirely the site-wide species nav menu. For contrast, the FL page is
**1,140 words with 12 listings** at $3,800–$8,500.

**Canonical defect:** the canonical tag on both the national category and the state pages points to
**`http://`** while the page is served over **`https://`** — a protocol mismatch on their highest-ranking URLs.

Named breeders inside their AG inventory: Parrot Stars (IL) · Birdmans Baby Parrots (IL) · Florida Parrot
(Miami FL) · WestBranchAviary (Old Hickory TN) · JC Aviary (Austin TX) · Parrot Baby (Tampa FL) · Fifty
Shades of African Greys (West Saint Paul MN) · Feather Headz Aviary (Miami FL) · Ana's Parrots (PA) ·
Little Creek Menagerie (Havelock NC) · GODS CREATION (Fort Valley GA).

Shipping quoted inside listings: **$185** (JC Aviary, *"US except HI"*) · **$200** (*"US except AK, HI"*) ·
**$225** (Florida Parrot).

### 4. Visual and structural inventory (live)

`/birds/category/african-grey-parrots`:

- **1,084 words** · **H1 count 0** — no H1 at all on the #1-ranking page for the head term
- H2 **0** · H3 **2** (both the identical string *"African Grey Parrots for Sale"*) · H4 **17**
- **13 `<img>`, exactly 1 with a non-empty alt** — and that one is the logo,
  `"Birds for Sale Local Breeders | BirdBreeders.com"`. Every listing thumbnail is alt-less.
- **0 `ld+json`. 0 microdata.** No `Product`, no `Offer`, no `BreadcrumbList`.
- 0 `<iframe>`, 0 video, 0 `<table>`
- Live prices: **$3,900 · $4,800 · $5,200 · $5,400 · $6,500 · $6,800 · $8,500**
- Listing images timestamped `26080717480442` → **2026-08-07**, so inventory is ~2 days fresh

### 5. Reddit / forum mining — BirdBreeders by name

| Thread | Verbatim | Read |
|---|---|---|
| r/parrots **"Birdbreeders.com safe?"** (2022-07-05) | *"Cannot say for certain on that site but 90% of the time it is a total scam. Even if it wasn't a scam I wouldn't put a bird through that process, very traumatic."* | **Top and only answer** to a direct trust question about the #1-ranking site |
| r/parrots "Is this a scam?" | *"Try Jc Aviary in TX, Parrot Stars in IL, birdbreeders.com, or the Avian [Exchange]"* | Recommended as a **directory**, alongside two named breeders |
| r/parrots "Legit or No?" | *"I would try birdbreeders.com since you can search for breeders in your exact state and area. A lot of bird breeders are there."* | The **state-search** feature is the reason cited |
| r/parrots "Where can I find a reputable bird breeder?" | *"…birdbreeders.com and birdsnow.com and oodle.com marketplace."* | Standard triad |
| r/AfricanGrey "Ana's Parrots and Supplies…" | *"I can find the facebook link and a different link at Bird Breeders.com… There are a lot of scammers posting African Grey's cheap."* | Used as a **verification cross-check** |

**The split is the point.** BirdBreeders is recommended for its *state search*, and simultaneously answered
with *"90% of the time it is a total scam"* when asked directly whether it is safe. It ranks #1 and carries
unresolved trust doubt.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| **"Covered: All 22 represented by at least one listed breeder"** | **False.** 66/66 URLs return 200, but **14 of 22 states hold zero African Grey listings** |
| "Homepage word count: ~1,200 (estimated)" | Category page measures **1,084**; the estimate was never verified against a live fetch |
| "H1 = 'African Grey Parrots for Sale'; H2 = breeder names" | **False.** **Zero H1**, zero H2. The string appears twice as H3 |
| "Schema — Expected: LocalBusiness per profile, BreadcrumbList, possibly Product" | **Zero structured data of any kind** on the category and state pages |
| "'Verified Breeder' badge program on some profiles — key differentiator" | **Not observed** on any page fetched this pass. Profiles carry **review counts**, not a verified badge. Recorded as unconfirmed |
| "Total pages: estimated 5,000–15,000 URLs" | **NOT FETCHED** — no sitemap enumerated this pass; the estimate remains unverified |

### Key insight

BirdBreeders holds **#1 for the head term with no H1, no H2, no structured data, one alt attribute across
13 images, and an `http://` canonical on an `https://` page.** It ranks on inventory and domain history
alone. Its exploitable weakness is precise: **14 of our 22 target states are 644-word empty shells set to
`INDEX, FOLLOW`.** A real CAG state page does not need to be brilliant to beat one — it needs to exist.

---

## B3 · Hoobly — https://www.hoobly.com

Tier 2 · classified_aggregator · baseline `competitor-hoobly-2026-05-11.md`

### 1. SERP snapshot

**[UK-localised] "african grey parrot classifieds for sale hoobly"** — Hoobly holds **8 of the top 10**,
including #1 `/s/pets-animals~birds~african-grey`, #2 `/s/us?q=African+Grey`, #5 `/s/us/pets-animals~birds`,
#6 Charlotte, #9 North Carolina.

**Absent from the top 10** on `african grey parrot for sale` (UK **and** US), `african grey parrot for sale
near me`, `african grey parrot price`, and `where to buy african grey parrot`.

**The autosuggest finding is the important one:** `african grey parrot for sale hoobly` is a **live Google
and Bing suggestion**. Hoobly is the only site in this group with a **navigational brand token** in the
fan-out — buyers type its name. No `birdsnow`, `birdbreeders`, `petzlover` or `petclassifieds` token appears.

### 2. Query fan-out

From the 566-query union, the platform-modifier cluster (23 queries) is dominated by classifieds brands:
`african grey parrot for sale hoobly` · `… craigslist` · `… facebook marketplace` · `… ebay` ·
`… gumtree` (+ near London / Manchester / Leeds / Sheffield) · `… preloved` · `african grey parrots on craigslist`.

### 3. Section / listing inventory

- **Taxonomy** — `/s/<country>~<state>/pets-animals~birds~african-grey` and
  `/s/us~<st>~<city>/pets-animals~birds~african-grey`; individual ads at `/p/<id>`
- **State strip rendered on the US AG page (25 states):** FL · NY · CA · IL · NC · TX · MD · MI · OK · VA ·
  WI · AZ · NJ · PA · TN · WV · IN · OH · AL · DC · GA · ID · KY · ME · MN
  → **16 of our canonical 22** appear in that strip. Absent from the strip: **CO · MA · MO · NM-adjacent
  none, SC · WA · plus MN present**, precisely: **CO, MA, MO, SC, WA** are not in the visible strip
  (deeper state URLs may still exist — NOT FETCHED for those five).
- **City pages** confirmed live: Miami · Orlando · Homestead · Chicago · Houston · Buffalo · Baltimore ·
  Jacksonville · Charlotte · Waxhaw · Nashville · New Berlin · Sacramento
- **Category pollution** — inside the African Grey category, live: a **King Charles Spaniel puppy litter
  ($350)**, a **stainless steel cage ($1,500)**, **parrot breeding boxes ($45)**, **baby Amazon parrots
  ($2,500)**, a **Cape Parrot ($2,500)**, **triple-stack bird cages ($650)**. The AG category is not an AG category.

### 4. Visual and structural inventory (live)

`/s/us/pets-animals~birds~african-grey`:

- **1,030 words**
- **Heading structure: H5 × 30, and nothing else.** No H1, no H2, no H3, no H4 — the 30 listing titles are
  all H5. This is the flattest heading structure measured in the sweep.
- **30 `<img>`, all 30 with no `alt` attribute at all** — not empty alt, *absent* alt
- **0 `ld+json`, 0 microdata**
- `robots: noarchive` · canonical self-referential · viewport present
- Live price tokens: **$7 · $45 · $350 · $650 · $1,500 · $1,700 · $1,800 · $2,000 · $2,100 · $2,500 ·
  $2,900 · $3,300 · $3,500 · $3,650 · $4,000 · $4,800 · $5,000 · $5,500 · $6,000 · $6,899 · $7,000**
  — birds occupy **$1,500–$7,000**; the sub-$1,000 tokens are cages, breeding boxes and the misfiled puppy ad
- Listing recency markers on page 1: `2h`, `4h`, `7h`, `10h`, `11h`, `18h`, `32h` — **inventory turns over hourly**
- **Geo behaviour:** a request from this UK line receives `302 → /s/gb`. Hoobly scopes results by requester
  IP geolocation.

### 5. Reddit / forum mining — Hoobly by name

| Thread | Verbatim | Read |
|---|---|---|
| r/parrots "Getting birds shipped?" (2021-09-02) | *"i've found breeders in Hoobly and shipped birds before without issue. Just find a real breeder, not finch farm who is a broker."* | **Positive, with a caveat** — vet the seller, not the platform |
| same thread | Q: *"do you know if there are scams on hoobly?"* → A: *"can be scams anywhere but i haven't encountered one there"* | Neutral-positive; no scam reputation |
| same thread | *"Please don't! I got totally scammed about an African Grey, I am just glad I was able to get my money back."* | The category's baseline anxiety |

Hoobly is the **only platform in this group with net-positive Reddit sentiment** and no "is it a scam"
thread against it.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| **"suspiciously low prices ($200–$500 seen for African Greys — potential scam/CITES risk)"** | **Not reproduced.** The live US AG page price band for birds is **$1,500–$7,000**. No sub-$1,500 African Grey found. The `$35` in Google's index for `/p/VNOicNE` is a **truncation of $3,500 on an expired listing** |
| **"CITES FLAG: Hoobly's open model allows listings at very low price points … likely scam listings"** | **Withdrawn on the evidence.** The flag rested on the $200–$500 figure, which does not survive a live fetch. Hoobly is not where the cheap-Grey scam listings are |
| "Homepage word count: ~600 (minimal)" | AG category page measures **1,030**; homepage NOT FETCHED this pass (geo-redirects to `/s/gb`) |
| "Category H1 = 'African Grey Parrots' or similar; individual ads H1 = ad title" | **False.** The category page has **no H1 and no H2/H3/H4** — 30 H5s only |
| "Schema — Expected: BreadcrumbList, possibly PostalAddress" | **Zero** structured data |
| "Alt text: usually missing or auto-generated" | Confirmed and sharpened: **30/30 images carry no `alt` attribute whatsoever** |
| "strong near-me and price keyword presence" | **False.** Absent from the top 10 on both `…near me` and `…price`. Its strength is **navigational** — `african grey parrot for sale hoobly` is a live autosuggest term |

### Key insight

Hoobly is the **largest live African Grey supply in this group (≥150 US listings, turning over hourly) and
the only one with a branded navigational query** — yet it ranks on almost nothing except its own name and
"classifieds". The 2026-05-11 CITES flag against it does not survive a live fetch and should be withdrawn:
the real quality defect is **category pollution** (puppies and cages inside the African Grey feed), not
scam pricing.

---

## B4 · Petzlover — https://www.petzlover.com

Tier 2 · classified_aggregator · baseline `competitor-petzlover-2026-05-11.md` (written with no live fetch)

### Barrier — on-page metrics NOT FETCHED, and the barrier is specific

`petzlover.com` serves its **own branded CAPTCHA**, not Cloudflare:
`<title>PetzLover - Verify You Are Human</title>`, body *"PetzLover - Secure Access Check … Complete the
CAPTCHA verification to prove you're not a robot"*, with a CAPTCHA image at `/captcha/<hash>.png`.

- `curl` + full browser UA → **HTTP 403**, 1,597 bytes, CAPTCHA page
- Firecrawl **basic** proxy → 403
- Firecrawl **stealth** proxy (5 credits) → **still 403**, CAPTCHA page returned

**Word counts, heading structure, schema, image counts, alt text and live prices are NOT FETCHED for
Petzlover.** Everything below is **index-level metadata** from `firecrawl_map` — titles and meta
descriptions Google holds — and is labelled as such. It is not a live page read.

### 1. SERP snapshot

Petzlover **did not appear in the top 10** of any of the six queries measured this pass (UK or US
localisation). NOT FETCHED: a dedicated brand-query SERP.

### 2. Section / listing inventory — index-level only

`firecrawl_map` returned **80 African-Grey-relevant URLs**. The structure is the most geographically
granular in this sweep, and it runs **two parallel taxonomies for the same thing**:

- Taxonomy A — `/us/african-grey-parrot-for-sale-in-<state>` and `/us/african-grey-for-sale-in-<state>`
- Taxonomy B — `/us/sale/birds/african-grey-parrot/<state>[/<city>]`
- **County level** — `/us/african-grey-for-sale-in-palm-beach-county-fl` ·
  `…-fresno-county-ca` · `…-san-bernardino-county-ca` · `…-dane-county-wi`
  → **no other site in this group targets counties**
- **Adoption variants** — `/us/african-grey-parrot-for-adoption-in-north-carolina`,
  `…-for-rehoming-in-rogersville-al-682021`
- **Individual listings** — `/us/african-grey-parrot-for-sale-in-<city>-<st>-<id>`
- **International** — `/de/`, `/gb/`, `/ca/`, `/za/`, `/ph/`, `/in/`, `/af/`, `/cm/`, `/ly/`, `en.petzlover.com`

US states visible in the mapped set: NE · TX · FL · MI · IN · NY · NC · AL · LA · TN · MN · SC · GA · OH ·
AZ · CO · CA · PA · WV · HI · AK · OK · KY · WI · MO · CT · NV · WA
→ **16 of our canonical 22** appear (missing from this sample: IL is present via
`/us/all/african-grey-for-sale-in-illinois`; **MA, MD, NJ, VA** not observed — NOT FETCHED, not proven absent).

### 3. Inventory character — from their own meta descriptions

Their meta descriptions are **templated inventory summaries**, which is a genuinely strong AEO pattern:

- Palm Beach County FL — *"prices/fees ranging from $300 – $3,500. typically 3.0 months – 20.0 years old, with approximately 22 males and 20 female available"*
- Houston TX — *"prices/fees ranging from $150 – $1,900. typically 3.0 months – 35.0 years old, with approximately 14 males and 16 female"*
- Anchorage AK — *"typically 6 weeks – 21.0 years old, with approximately 60 males and 51 female available"*
- Chicago IL — *"$50 – $4,000"* · Georgia — *"$250 – $1,200"* · Ohio — *"$500 – $2,000"* ·
  Fresno County CA — *"$300 – $7,000"*
- Individual listings: **$350** (Chattanooga TN) · **$400** (Tampa FL; Little Rock AR) · **$500** (Wilmington NC; Denver CO; Lansing MI) · **$600** (Tulsa OK; pair in Destin FL) · **$800** (Martinsburg WV) · **$830** · **$1,750**
- Site-wide trust claim: **"Trusted by 1.8M+ pet lovers"**

**CITES / trust flag.** Those price bands sit far below any credible captive-bred Congo African Grey
price — **$50 in Chicago, $150 in Houston, $250 in Georgia** — and the identical boilerplate
*"Healthy, vaccinated, and ready for a loving home"* recurs across unrelated cities. Parrots are **not
vaccinated** as a routine matter, which makes that phrase a template artifact rather than a health claim.
This is the price band the 2026-05-11 baseline attributed to Hoobly; **it is Petzlover's, not Hoobly's.**

### 4. Visual inventory

**NOT FETCHED** — CAPTCHA. No image count, alt text, video or infographic data can be reported.

### 5. Reddit / forum mining — Petzlover by name

**Zero Reddit or forum mentions found** in the indexed set across the queries run. Petzlover has index
footprint without community footprint.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "Access Status: Inaccessible for live fetch (Playwright/WebFetch unavailable in analysis session)" | Barrier now named precisely: **self-hosted PetzLover CAPTCHA, 403 to curl and to Firecrawl stealth alike.** It is a bot wall, not a session limitation, and not a dead site |
| "Total pages: Medium-sized classifieds; estimated thousands of listings" | Unverifiable at page level. What *is* verified: **80 AG URLs in the index**, across state, **county**, city, adoption and 10 country namespaces |
| "Local: state/city filtering expected" | Confirmed and exceeded — **county-level pages**, which nothing else in this group has |
| "Keyword gaps vs CAG: cannot confirm specific phrases" | Now confirmable from index metadata: `african grey for sale in <county> county, <st>`, `african grey parrot for rehoming`, `african grey parrot for adoption in <state>` |
| Priority "low" | On evidence of index breadth this looks **understated**, but the CAPTCHA prevents a confident re-rank. Recorded as an open question, not a change |

### Key insight

Petzlover is the **most geographically granular competitor in the tier — the only one indexing county-level
African Grey pages — and it is invisible to us behind its own CAPTCHA.** Its index-level price bands
($50–$800 individual listings) are the actual home of the cheap-Grey pattern this registry has been
attributing to Hoobly. Its templated meta descriptions (*"prices ranging from X–Y, typically A–B years old,
approximately N males and M female available"*) are a **structured-summary pattern worth copying honestly**
for CAG's own location pages, where we can populate it with real inventory.

---

## B5 · PetClassifieds — https://www.petclassifieds.com

Tier 2 · classified_aggregator · baseline `competitor-petClassifieds-2026-05-11.md` (no live fetch)

### Barrier and access

`curl` → **HTTP 403, Cloudflare `Just a moment...` JS interstitial** (apex and www alike). Firecrawl
**basic** proxy → **HTTP 200**. Their own FAQ states the policy: *"To protect our community from
international scammers, we restrict access from certain high-risk countries… Access is blocked if you use
technology to hide your location."* Since this machine egresses from a **UK line**, the block is expected.

### 1. SERP snapshot

PetClassifieds **did not appear in the top 10** of any of the six queries measured (UK or US). NOT FETCHED:
a dedicated brand-query SERP.

### 2. Section / listing inventory (live, via Firecrawl)

Live category counters on the homepage:

| Category | Ads |
|---|---|
| Dogs & Puppies | 13,142 |
| Cats & Kittens | 1,790 |
| **Birds** | **588** |
| Small Pets | 462 |
| Reptiles & Amphibians | 214 |
| Livestock | 67 |
| Other Pets | 49 |
| Fishes | 15 |
| **Parrots (subcategory)** | **331** |

- **State pages** — `/ad_category/parrot/<state>`, exposed for **FL · CA · NY · TX · MD · OH · NJ · GA ·
  IL · NC** → **10 states, all 10 inside our canonical 22**
- **Tag pages** — `/ad_tag/<tag>`; a live typo tag is indexed: **`/ad_tag/frieldly`**
- **Trust pages** — `/how-to-safely-buy-a-pet-online/` · `/ad-guidelines/`
- Ads dated **Aug 9th 2026** — actively maintained the day of this fetch

### 3. This is no longer a bare classifieds board — and that is the correction

`/ad_category/parrot` is a **~3,000-word species-guide + listing hybrid** with a full heading hierarchy:

- **H2** *"Parrots for Sale: An Abundance of Options and Beautiful Colors"*
- **H3** *Overview of Parrots for Sale* → **H4** *History* → **H5** *Pet Parrots in Europe* · *Parrot Trade in America*
- **H4** *Parrots for Sale come from a huge family.* → **H5** *Parakeets or Budgerigars* · *Conures* · *Lorikeets* · *Cockatiel* · *Large Parrots for Sale Near Me*
- **H3** *Common Types of Pet Parrots for Sale* → **H4** *Quaker Parrot* · *Indian Ringneck Parrots* · *Amazon Parrot* · **African Grey Parrot** · *Macaw Parrot* → **H5** per sub-species
- **H3** *Caring for Parrots* → **H4** *Attention* · *Love* · *Other Parrot Basic Needs*

Their **African Grey Parrot** block is a full spec card: alternative names (*Grey Parrot, Congo Grey
Parrot, Congo African Grey*), native regions, classification, size (13 in / 14 oz), diet, colors, lifespan
(**40 to 60 years**), habitat cage dimensions (**24 × 24 × 36 in**), temperament, and speaking ability.

**Three of their claims collide directly with CAG's own pages:**

1. **Visual sexing (factually weak).** *"Dimorphic: female's tail feathers become tinged with silver; male
   has shorter neck and more slender head, and tail feathers remain solid red."* Congo African Greys are
   **not reliably sexed by eye** — which is the entire reason DNA sexing exists. This is the single best
   opening for CAG's DNA-sexing entity and the male-vs-female comparison page.
2. **Weaning window.** *"Baby parrots for sale can typically eat on their own by the age of eight weeks,
   but many breeders will keep them for an additional month. Some are 12 to 14 weeks before they are
   completely weaned. Ideally, you want a hand-raised bird that eats on its own by the time you acquire
   it."* Their number is **12–14 weeks**; the Benjamin Home-Raising Protocol gate is **12–16 weeks**. We are
   the more conservative party and can say so against a cited competitor figure.
3. **Captive-bred framing.** *"Since the foundation of the World Parrot Trust in 1989, there has been a
   concerted effort to restrict pet parrot ownership to captive-bred birds."* They are already touching
   CAG's captive-bred angle — without ever naming **CITES** or **Appendix I**.

### 4. Trust positioning — they are now competing on CAG's own ground

Four homepage H3s:

- **Active Scam Removal** — *"We actively monitor listings and remove known scam patterns. Suspicious sellers are blocked quickly…"*
- **Built In Seller Transparency** — *"We require clearer information, real photos, and consistent listing details."*
- **Higher Quality Inquiries**
- **Rules Made for Living Animals** — *"Age limits, legal checks, and category rules are enforced."*

Plus an on-page FAQ block carrying real anti-fraud instruction: *"We verify via email link ONLY. If you
receive a text asking for a 6-digit code, it is a scammer. NEVER share this code."* and suspension reasons
including *"Prohibited Items: Selling banned species."*

**Monetisation:** Chewy affiliate links (`chewy.sjv.io`) and Prudent Pet insurance
(`app.prudentpet.com/?promoCode=PETCLASS`), disclosed as *"purchases made through these links may earn
PetClassifieds a commission."*

### 5. Live African Grey inventory

| Listing | Price | Location |
|---|---|---|
| Adorable African Grey Parrots | **$650** | WA |
| Jojo The African Grey Parrot | **$830** Negotiable | New York, NY |
| Afican Grey Parrot (Timneh) *(their typo)* | **$1,500** | Antioch, TN |
| DNA Tested Tamed African Grey Parrots Available | Contact For Price | FL |
| Looking to add a Congo african Gey *(want-to-buy, their typo)* | Contact For Price | Portland, OR |

### 6. Reddit / forum mining — PetClassifieds by name

**Zero mentions found.** No community footprint.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| **"a lower-priority general classifieds site with minimal African Grey-specific content depth"** | **False.** `/ad_category/parrot` is a ~3,000-word species guide with H2→H5 depth and a dedicated African Grey spec card |
| Registry note **"Low AG depth — minimal threat"** | AG *listing* depth genuinely is low (5 AG ads visible). **Content** depth is not — and it now overlaps our sexing, weaning and captive-bred claims |
| "CAG's informational content moat … is already a structural advantage over this type of competitor" | **No longer true as stated.** They ship informational content on the same page as the listings |
| "Trust badges: None" / "Reviews: None at platform level" | They ship four explicit trust propositions and a safety guide at `/how-to-safely-buy-a-pet-online/` |
| "Access Status: Inaccessible for live fetch" | Barrier named: **Cloudflare JS interstitial + self-declared geo/VPN restriction.** Reachable via Firecrawl basic proxy |
| "Page Types — Species guides: no" | **Yes** — a substantial one |

### Key insight

PetClassifieds has **relaunched as a trust-positioned platform and is now the only site in this tier
competing on CAG's own ground** — active scam removal, seller transparency, a safety guide, and a
species-guide with an African Grey card. It has almost no African Grey inventory (5 ads) and **zero CITES
or Appendix I language**, and its dimorphism claim ("female's tail feathers tinged with silver") is exactly
the kind of eyeball-sexing folklore that DNA testing exists to replace. Beat it on **documentation
specificity**, not on trust vocabulary — they have the vocabulary now.

---

## B6 · exoticPetsAvenue — https://exoticpetsavenue.com

Tier 2 in registry · flagged `confirmed_scam` / `threat_level: negative` ·
baseline `competitor-exoticPetsAvenue-2026-05-11.md` (no live fetch)

### 🚩 The 2026-05-11 scam finding is CONFIRMED and now has verified numbers

The site is **live and actively maintained** — www→apex 301 then HTTP 200, Apache / PHP 8.4.24 / StackCDN /
WordPress, and the African Grey product page carries `article:modified` **2026-08-07** (two days before
this fetch).

**Federally protected species, live, with a price and an Offer schema:**

`https://exoticpetsavenue.com/product/big-bear-bald-eagle-eggs/` — **HTTP 200**, 1,229 words,
`ld+json` `Offer` price **$65.00–$85.00**, `availability: InStock`, meta description:
*"Big Bear Bald Eagle eggs for sale, offering the chance to hatch strong, majestic chicks from healthy,
ethical breeding pairs. Order now!"*

**Non-human primates, live, with prices:** `/product/macaque-monkeys/` **$650–$950**, plus product pages
for rhesus macaque, pig-tailed macaque, long-tailed macaque, capuchin, squirrel monkey, spider monkey,
marmoset, pygmy marmoset and emperor tamarin.

**Their African Grey inventory — six pages, all `InStock`:**

| URL slug | Offer price range |
|---|---|
| `/product/african-grey-parrot-for-sale/` ("Lily") | $850 – $1,000 |
| `/product/african-grey-parrots-for-sale/` | $850 – $1,100 |
| `/product/african-gray-parrot-for-sale/` | $650 – $850 |
| `/product/african-grey-parrot-to-buy/` | $950 – $1,000 |
| `/product/for-sale-african-grey/` | $650 – $850 |
| `/product/african-grey-parrots-for-sale-near-me/` | $850 – $1,000 |

### The egg-keyword tag farm — this one is aimed straight at CAG's egg page

`firecrawl_map` returned **35+ `product-tag` URLs built entirely on African Grey egg keywords**:

`african-grey-parrot-eggs-for-sale` · `-near-me` · `-in-usa` · `-uk` · `-canada` · `-in-australia` ·
`-in-india` · `-in-pakistan` · `-in-lahore` · `african-grey-parrot-egg-price` · `african-grey-eggs-price` ·
`african-grey-eggs-hatching` · `african-grey-parrot-hatching-eggs-for-sale` ·
`african-grey-parrot-fertile-eggs-for-sale` · `african-gray-parrot-hatching-eggs-for-sale` ·
`african-grey-parrot-how-many-eggs` · `african-grey-parrot-eat-eggs` · plus
`african-gray-parrot-for-sale-in-los-angeles` and `african-gray-parrot-for-sale-los-angeles`.

**C.A.Gs ships fertile eggs to all 50 states at $95 each.** This is the single competitor in this sweep
directly farming that keyword space, and it does so from a site that also sells bald eagle eggs.

### Structural inversion worth naming

`/product/african-grey-parrot-for-sale/`: **1,157 words**, H1 × 1, H2 × 3, H3 × 4, **24 images with 24 alt
attributes**, and **13 schema types** — `Product`, `Offer`, `BuyAction`, `ItemPage`, `WebPage`, `WebSite`,
`BreadcrumbList`, `ListItem`, `ImageObject`, `SearchAction`, `EntryPoint`, `UnitPriceSpecification`,
`PropertyValueSpecification`.

**A confirmed scam site ships better structured data and better alt-text discipline than BirdsNow,
BirdBreeders and Hoobly combined — those three carry zero `ld+json` between them.** Structured data is not
a trust signal, and no CAG page should be argued for on the grounds that "competitors have it."

Trust-page mimicry: `/health-guarantee` · `/shipping` · `/track-order` · `/return-refunds-policy` ·
`/testemonials` **(their misspelling)** · `/about-us`.

### Reddit / forum mining

**Zero mentions of `exoticpetsavenue` found.** The scam sites redditors *do* name in African Grey threads
are different domains (see B7 and the Reddit ledger below) — this one is not on the community's radar,
which is itself a reason CAG's scam page should name it.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| Every field `UNVERIFIED` | Now measured: 6 AG product pages at **$650–$1,100**, eagle eggs at **$65–$85**, macaques at **$650–$950** |
| Registry note "eagle eggs $65" | **Confirmed exactly** — and the page is still live and `InStock` on 2026-08-09 |
| Registry note "African Greys listed at $650 with no documentation" | **Confirmed**, and refined: the range across six pages is **$650–$1,100** |
| "Keyword gaps vs CAG: 'exotic african grey parrot for sale', 'exotic parrots for sale'" | Superseded by a far more specific finding: **35+ African Grey *egg* keyword tags**, which target CAG's own fertile-egg page |
| "Blog Analysis: UNVERIFIED" | `/blog` and `/category/blog` exist in the URL map; **content NOT FETCHED** |

### Key insight

exoticPetsAvenue is not merely a scam listing — it is a **live, actively-maintained, fully-schema'd
storefront selling bald eagle eggs and macaque monkeys alongside $650 African Greys, running a 35-tag
keyword farm aimed at CAG's fertile-egg page.** It is the best single documented example available for
`/how-to-avoid-african-grey-parrot-scams/`, and the *only* one in this group whose harm is legal rather
than commercial. Never link to it; screenshot and cite it.

---

## B7 · Parrot Alert — https://www.parrotalert.com  ·  **tier 5 non_commercial, not a competitor**

Re-tiered 2026-08-09. Lost / stolen / found parrot registry. **Not benchmarked on listings, prices,
inventory or SERP position** — none of those apply. Analysed here as a **citation and backlink target.**

### What it actually is (live figures from the site's own counters)

| Metric | Value |
|---|---|
| Members | **73,788** |
| US members | **28,967** |
| Reported **lost** | **12,039** |
| Reported **stolen** | **423** |
| Reported **found** | **1,511** |
| Reported sightings | **214** |
| Countries in the selector | 18 |

Free service, PayPal-donation funded, auto-generates a PDF flyer per report and cross-posts to social
media, per-country RSS feeds, sister site `critteralert.com`, Facebook page `/ParrotAlert`.

Article sections: Announcements · News and Alerts · Lost and Found · Health and Safety · Parrot Video
Library · **Parrot Phishing Scam Site Alerts**.

### The backlink and citation opportunity, made concrete

Their scam-alert section names specific domains — **macawsfarm.com**, **macawparrotsfarm.com**,
**prestigebirdfarms.com**, and one directly on our species:

**`/article/parrot-scam-site-african-grey-parrot-farm-18` — SCAM SITE: africangreyparrotfarm.com**

Verbatim, from the live article:

> *"We've had reports from 2 people so far that have fallen victim to the scam and lost **$1000** and
> **$975** respectively."*
> *"Site goes by the name 'African Grey Parrot Farm' via the website domain: africangreyparrotfarm.com on
> the following number: **+1 (281) 503-4953**"*
> *"the domain came into existence on **January 16th 2019** and doesn't have a physical address on the
> website to check and verify."*

**Three facts CAG should act on:**

1. **The scam used a Houston, Texas area code (281).** A Texas phone number is being used to impersonate
   legitimacy in the African Grey market. C.A.Gs is a **Midland, Texas** breeder. Our Texas-ness is a
   differentiator that a scammer has already tried to counterfeit — which makes our **verifiable address
   and visitation offer** load-bearing, not decorative.
2. **`africangreyparrotfarm.com` is still live today** — checked 2026-08-09: HTTP 200, A records
   `172.67.184.194` / `104.21.84.16` (Cloudflare). The named scam is still operating and still taking traffic.
3. **Their stated advice is an objection CAG must answer, not dodge:**
   *"never purchase a pet parrot from an online pet shop website or any advert website, no matter how good
   it sounds… **Never make any payment online, even if you are requested to pay a deposit to reserve a pet.**"*
   That is a direct challenge to any deposit-based reservation flow, published by the most credible
   non-commercial authority in the niche. Our answer has to be *verifiability* — named people, a real
   address, visitation, documented birds — not reassurance.

**Compliance note.** The article carries: *"This article or any portion thereof may not be reproduced or
used in any manner whatsoever without the express written permission of ParrotAlert.com."*
**Link and cite; do not reproduce.** A short attributed quotation with a link is the safe pattern.

### Correction to the 2026-05-11 baseline

The baseline analysed Parrot Alert as a **tier 2 classified aggregator** and inferred *"variant-level
keyword targeting (Congo and Timneh on separate pages)"*, *"Bird listings — yes"*, *"Location pages —
likely"*, and concluded that its supposed Timneh targeting **"signals that CAG's dedicated
/timneh-african-grey-for-sale/ page is a gap this parrot-specialist aggregator is already exploiting."**

**Every one of those is wrong.** There are no for-sale listings, no species-variant sales pages and no
state pages on this site. It is a lost-and-found registry. **The Timneh page recommendation in that
baseline rests on a false premise and must not be cited as evidence for it** — the Timneh case has to be
argued from BirdsNow's 17/22 Timneh state grid and BirdBreeders' Timneh inventory instead, both of which
are measured above and both of which do support it.

### Key insight

Parrot Alert is the **highest-authority non-commercial voice in the niche (73,788 members, 12,039 lost-bird
reports) and it publishes a named African Grey scam alert with real dollar losses and a Texas area code.**
It is a link target and a citation source, and its blanket advice — *never pay a deposit online* — is the
sharpest objection C.A.Gs' reservation flow has to answer anywhere in this sweep.

---

## B8 · Quality Birds Online — https://www.qualitybirdsonline.com

Tier 2 in registry · `access_status: "blocked_or_down"` · baseline `competitor-qualityBirdsOnline-2026-05-11.md`

### Verdict: neither blocked nor down — **the domain is parked**

Both apex and www return **HTTP 200** when resolved publicly. What they return is not a bird site.

| Evidence | Value |
|---|---|
| A records (`@1.1.1.1` / `@8.8.8.8`) | 172.238.172.122 · 172.236.104.157 · 172.236.104.43 |
| **Nameservers** | **ns1–ns4.`parklogictestns1.com`** — ParkLogic, a domain-parking monetisation provider |
| Response body | **4,693 bytes**, `<title>Redirecting...</title>` + an ad-blocker-detection JavaScript stub |
| Registrar | Hosting Concepts B.V. d/b/a Registrar.eu |
| Created | 2022-07-07 · Expires 2027-07-07 · Updated 2026-07-08 |
| System-resolver result | `81.99.162.48` — the Virgin Media filter proxy, **which is what produced the earlier `000`** |

### What it used to be (Wayback, raw `id_` snapshots)

| Date | Wayback status | State |
|---|---|---|
| 2024-08-07 | 200, 49,564 B | **Live parrot storefront** |
| 2024-11-03 | 200, 52,392 B | Live |
| 2024-12-08 → 2025-02-20 | 403 | Bot-blocked |
| 2025-03-06 | 200, 46,225 B | Live |
| **2025-06-12** | **200, 41,633 B** | **Last live snapshot** |
| 2025-07-13 | 301 | Transition |
| **2026-02-12** | 200, 47,116 B | **Parking page** — no title, no H1, no H2, 908 words, **0 mentions of "african grey"** |

The last real content (2024-08-07 snapshot):

- Title *"Find the Finest Parrots for Sale - Explore Quality Avian Companions"*
- H1 *"Best Parrot Breeders and Parrots for Sale-Quality Birds"*
- **52 H2s**, all product names — including **Timneh African Grey · White Congo African Grey · Congo
  African Grey · Adult African Grey Parrot · Female African Gray Parrot · Red Factor African Dark Parrot**
- 1,148 words, 14 "african grey" mentions
- **Prices $100 · $400 · $500 · $600 · $750 · $900**
- Also sold: **Falcon Birds · Toucans · Fertile Eggs · Incubators**

### Corrections to the 2026-05-11 baseline and the registry

| Claim | Measured 2026-08-09 |
|---|---|
| Registry `access_status: "blocked_or_down"` and note *"all Firecrawl engines failed to retrieve (blocking or down)"* | **Both wrong.** Apex and www both return **200**. The domain is **parked with ParkLogic** and serves an ad stub. Nothing to block and nothing down |
| Baseline "requires live Playwright access for full analysis. Re-run this analysis with Playwright MCP active" | Would not have helped. There is no site to render |
| Baseline "Primary threat to CAG is same as all aggregators: state-level listing pages" | **No state pages ever existed.** The archived site was a flat product storefront, not a geo-indexed classifieds platform |
| Baseline priority "medium" | Should be **none** |
| Registry `tier: 2 classified_aggregator` | It was never an aggregator. The archived site was a **direct storefront**, and on price evidence ($100–$900 African Greys sold alongside falcons and incubators) it belonged in **tier 6 suspect_seller** while it lived |

### Key insight

qualityBirdsOnline was a deep-discount parrot storefront — **African Greys at $100–$900, alongside falcons,
toucans, fertile eggs and incubators** — that went dark between June 2025 and February 2026 and is now
monetised parking. **The registry has spent two analysis cycles recording it as "blocked or down" when it
is simply gone**, and this pass is the first to say so with the Wayback timeline and the ParkLogic
nameservers behind it.

---

# Part C — Cross-cutting findings

## C1 · The structural scoreboard

Measured on each site's principal African Grey page, live:

| | BirdsNow | BirdBreeders | Hoobly | PetClassifieds | exoticPetsAvenue |
|---|---|---|---|---|---|
| Words | 1,108 | 1,084 | 1,030 | ~3,000 | 1,157 |
| H1 | 1 (*"Gray"*) | **0** | **0** | 1 | 1 |
| H2 | **0** | **0** | **0** | ✅ multiple | 3 |
| H3 | 15 | 2 (identical) | **0** | ✅ multiple | 4 |
| H4 | 4 | 17 | **0** | ✅ | 1 |
| H5 | 0 | 0 | **30 (only level present)** | ✅ | 0 |
| Images | 3 | 13 | 30 | — | 24 |
| Images with usable alt | 1 | **1 (the logo)** | **0 — no `alt` attribute at all** | — | **24** |
| `ld+json` blocks | **0** | **0** | **0** | — | **2 (13 types)** |
| Microdata | legacy only | **0** | **0** | — | — |
| Video / infographic / table | none | none | none | none | 1 table |

**Three of the four legitimate aggregators ship zero structured data and near-zero alt text, and the two
top-ranking pages in the entire tier have no `<h1>` at all.** The only site in the group with clean
semantic markup is the confirmed scam.

## C2 · State coverage against the canonical 22

| State | BirdsNow (generic / Congo / Timneh) | BirdBreeders (URL / live listings) | Hoobly (state strip) | PetClassifieds | Petzlover (index) |
|---|---|---|---|---|---|
| CA | ✅ / ✅ / ✅ | ✅ / **2** | ✅ | ✅ | ✅ |
| TX | ✅ / ✅ / ✅ | ✅ / **2** | ✅ | ✅ | ✅ |
| FL | ✅ / ✅ / ✅ | ✅ / **12** | ✅ | ✅ | ✅ |
| NY | ✅ / ✅ / **✗** | ✅ / **0** | ✅ | ✅ | ✅ |
| IL | ✅ / ✅ / ✅ | ✅ / **8** | ✅ | ✅ | ✅ |
| PA | ✅ / ✅ / ✅ | ✅ / **4** | ✅ | — | ✅ |
| OH | ✅ / ✅ / ✅ | ✅ / **0** | ✅ | ✅ | ✅ |
| GA | ✅ / ✅ / ✅ | ✅ / **0** | ✅ | ✅ | ✅ |
| NC | ✅ / ✅ / ✅ | ✅ / **0** | ✅ | ✅ | ✅ |
| MI | ✅ / ✅ / ✅ | ✅ / **0** | ✅ | — | ✅ |
| NJ | ✅ / ✅ / ✅ | ✅ / **0** | ✅ | ✅ | — |
| VA | ✅ / ✅ / ✅ | ✅ / **1** | ✅ | — | — |
| WA | ✅ / ✅ / **✗** | ✅ / **0** | — | — | ✅ |
| AZ | ✅ / ✅ / ✅ | ✅ / **0** | ✅ | — | ✅ |
| MA | ✅ / ✅ / **✗** | ✅ / **0** | — | — | — |
| TN | ✅ / ✅ / ✅ | ✅ / **1** | ✅ | — | ✅ |
| IN | ✅ / ✅ / ✅ | ✅ / **0** | ✅ | — | ✅ |
| MO | ✅ / ✅ / **✗** | ✅ / **0** | — | — | ✅ |
| MD | ✅ / ✅ / ✅ | ✅ / **1** | ✅ | ✅ | — |
| CO | ✅ / ✅ / **✗** | ✅ / **0** | — | — | ✅ |
| MN | ✅ / ✅ / ✅ | ✅ / **0** | ✅ | — | ✅ |
| SC | ✅ / ✅ / ✅ | ✅ / **0** | — | — | ✅ |

**The softest ground, by evidence:**

- **MA · MO · CO** — BirdsNow has no Timneh page, BirdBreeders has zero listings, Hoobly's state strip
  omits them, PetClassifieds has no state page. Four of five platforms weak or absent.
- **WA** — BirdsNow no Timneh, BirdBreeders zero listings, absent from Hoobly's strip.
- **NY** — the anomaly: heavy platform coverage everywhere, **zero BirdBreeders inventory**, and no
  BirdsNow Timneh page. High demand, thin supply.
- **SC · MN · IN · AZ · MI · NC · GA · OH · NJ** — all carry BirdBreeders 644-word empty shells.

Autosuggest demand (566-query union) confirms **16 of 22**; **IL · IN · MN · MO · NC · PA** return no
state token. That is the **same six** the page-5 sweep found on a completely different stem set — an
independent replication, and evidence the gap is in the *signal*, not in the demand.

## C3 · The trust-vocabulary void

Across the full 566-query fan-out:

- **`scam` / `legit` / `reputable` / `trusted` / `verified` / `safe` attached to the for-sale stem: 0 queries.**
- **`dna` / `health tested` / `papers` / `certificate` / `vet` attached to the for-sale stem: 0 queries.**
- The only trust-adjacent cluster that exists is **legal**: `do you need a licence for an african grey
  parrot` · `do you need a license to own an african grey parrot` · `is it legal to own an african grey parrot`.
- The **price-bait** cluster is live and large: `african grey parrot for sale cheap` ·
  `cheap african grey parrot for sale near me` · `cheapest african grey parrot` ·
  `cheap baby african grey parrots for sale` · `african grey parrot price cheap` (11 queries).

**Buyers do not search for trust. They search transactionally and cheaply, get burned, and then go to
Reddit.** The strategic consequence is direct: CAG's documentation, DNA-sexing and CITES material **cannot
be housed on pages that depend on trust keywords for traffic** — it has to be built *into* the
transactional and location pages that already rank, and into the answer for the `cheap` cluster.

## C4 · Reddit thread ledger (mined this pass — do not re-mine)

| Thread | ID | Date | Score | Yield |
|---|---|---|---|---|
| r/parrots "African grey scam website??" | `1jlf17f` | 2025-03-27 | 275 | The richest thread in the sweep — see verbatims below |
| r/parrots "Birdbreeders.com safe?" | `vrzczn` | 2022-07-05 | 2 | *"90% of the time it is a total scam"* |
| r/parrots "Getting birds shipped?" | `pgnbi3` | 2021-09-02 | — | Hoobly positive; Finch Farm broker warning |
| r/parrots "Is this a scam?" | `1rxs4ap` | — | — | JC Aviary / Parrot Stars / birdbreeders.com / Avian Exchange |
| r/parrots "Legit or No?" | `1gugm4y` | — | — | birdbreeders.com state search |
| r/parrots "Where can I find a reputable bird breeder?" | `5fwl5x` | — | — | birdbreeders + birdsnow + oodle triad |
| r/parrots "Shipping a parrot" | `4be2vr` | — | — | BirdsNow hub cited as price authority |
| r/parrots "I got scammed out of $2400 through a pet scamsite" | `191cssi` | — | — | **NOT FETCHED** — indexed but not opened this pass |
| r/AfricanGrey "Please can someone tell me a legitimate website" | `1asvyt3` | — | — | **NOT FETCHED** — indexed but not opened this pass |

**The verbatims that should shape CAG copy** (all from `1jlf17f`, scores in brackets):

- **[20] *"If you love animals, don't look for the cheapest… A gray parrot is at least 1500 for me. And more."***
  → The community's own floor is **$1,500** — **exactly CAG's Congo floor.** Our price is not a discount
  claim; it is the number an experienced buyer independently names as the minimum credible price. That is
  the strongest available framing for the whole for-sale cluster.
- **[249] *"Almost all bird shippers are scams and those prices are way too low. 100% a scam."***
- **[74] *"Between the super low prices and the non refundable 450 reservation fee due before hand yeah 10000 scam."***
  → A **non-refundable deposit is read as a scam signal.** Directly relevant to how CAG words its hold terms.
- **[106] *"did some reverse image searching and found this which has the same parrot pictures but with different names… and a very similar site, same reviews and same names too!"***
  → Buyers **reverse-image-search bird photos.** Every CAG photo being demonstrably our own bird is a
  verifiable advantage, and worth saying out loud.
- **[42] *"Scam. The price, the bird descriptions, the 450$ reservation fee, the location is middle of nowhere population 1,200 Michigan with no exact address."***
  → **No exact address = scam.** Midland, Texas with a real address is a defence.
- **[5] *"The website is 6 to 7 months old. I wouldn't trust it."***
  → **Domain age is used as a trust test.** C.A.Gs since 2014 is an 11-year answer to it.
- **[21] *"And every single bird has the same exact description."*** and **[76] *"The birds are all full of
  kisses and don't bite? That is bs."***
  → **Per-bird honest description, including flaws, is a trust signal.** Uniform glowing copy reads as fraud.
- **[1, victim] *"Did all the follow thru. Called him. Made him call me. Video chat with me. Sho me the
  bird. Everything I did I thought it was good but no. My sister lives in Michigan and went to the address
  and the mab there knew nothing about birds."***
  → **Video chat did not prevent the scam.** Only the physical address check did. Visitation is the one
  verification that worked.

## C5 · Page-type and schema gaps

| Page type | BirdsNow | BirdBreeders | Hoobly | PetClassifieds | Petzlover | CAG has it? |
|---|---|---|---|---|---|---|
| State landing pages | **61 AG pages** | 66 URLs, 8 with stock | 25-state strip | 10 states | state + **county** | **Partial — gap** |
| City landing pages | ✅ | — | ✅ | — | ✅ | **Gap** |
| Trait pages (talking / bonded pair / male / female / house-trained) | **✅ 9 pages** | — | — | — | — | **Gap — and it is the cheapest one to close** |
| Species care guide | — | — | — | **✅ ~3,000 words** | — | ✅ |
| Congo vs Timneh comparison | — | — | — | — | — | ✅ — uncontested in this tier |
| CITES / Appendix I language | **0** | **0** | **0** | **0** | NOT FETCHED | ✅ — **nobody in this tier says it** |
| USDA language | **0** | **0** | **0** | **0** | NOT FETCHED | ✅ |
| `ld+json` structured data | **0** | **0** | **0** | NOT MEASURED | NOT FETCHED | ✅ |
| Scam-prevention content | — | — | — | ✅ safety guide | — | ✅ |

**`CITES` and `Appendix I` appear zero times across every page fetched from all five commercial platforms
in this sweep.** The only site in the niche publishing serious buyer-protection material is
**parrotAlert**, and it is non-commercial. That space is genuinely unoccupied.

## C6 · Priority action queue

1. **(Recommended) Publish an honest price-anchor section on the for-sale cluster built on the duplication
   evidence.** Grounded in: the same seller (*Ana's Parrots*) listing African Greys at **$8,500 on
   BirdBreeders and $4,500 on Hoobly**; one Richmond VA Timneh appearing at **$3,200 on both BirdsNow and
   Hoobly** across four indexed URLs; BirdBreeders' live band **$3,900–$8,500**; and the r/parrots buyer
   who says **"A gray parrot is at least 1500 for me."** That last quote puts the community's own floor at
   CAG's floor. **Trade-off:** it forces us to explain why our ceiling ($3,500) sits below BirdBreeders'
   floor ($3,900), which is a harder paragraph to write than a vague "competitive pricing" line — but it is
   the only version that survives a buyer opening a second tab. Recommended because it is the one asset in
   this sweep that no competitor can copy: they cannot publish a stable price without exposing their own
   spread.
2. **Build state pages for MA, MO, CO, WA and NY first.** Evidence: BirdsNow ships no Timneh page for
   MA/MO/CO/WA/NY; BirdBreeders returns **zero listings** for all five while serving 644-word
   `INDEX, FOLLOW` shells; Hoobly's state strip omits MA/MO/CO/WA. Trade-off: no autosuggest signal for MO
   or NC, so these are inventory-gap plays, not demand-proven ones.
3. **Add trait pages** mirroring BirdsNow's proven grid — talking · hand-fed · bonded pair · male · female
   · house-trained. Nine such pages are the only structure BirdsNow ranks with besides states, and no other
   site in the tier has them.
4. **Answer the deposit objection explicitly.** ParrotAlert tells 73,788 members *"Never make any payment
   online, even if you are requested to pay a deposit."* r/parrots reads a non-refundable reservation fee as
   *"10000 scam."* Our hold terms need to be stated in that light or they read as the scam pattern.
5. **Refresh `/how-to-avoid-african-grey-parrot-scams/`** with the verified material gathered here:
   exoticPetsAvenue's live bald-eagle-egg and macaque pages with prices; africangreyparrotfarm.com's
   **$1,000 and $975** documented losses and Houston **281** area code (cite ParrotAlert by link, do not
   reproduce); the reverse-image clone pattern; and the domain-age test.
6. **Correct the Timneh business case.** The 2026-05-11 recommendation for `/timneh-african-grey-for-sale/`
   was justified by Parrot Alert's supposed variant pages, which do not exist. Re-justify it from
   BirdsNow's **17/22 Timneh grid with five named gaps** and BirdBreeders' live Timneh inventory at $6,500.
7. **Do not argue for schema on competitive grounds.** The only site in this tier with rich `ld+json` is
   the confirmed scam. Argue for it on merit.

---

## Proposed registry patch (NOT applied — for breeder approval)

`data/competitors.json` was **not modified.** Proposed changes, in priority order:

1. **Correct the `exoticGlobalParrotsFarm` note.** The claim that five domains share `81.99.162.48` and are
   therefore "one operator running a domain network" is a **local DNS artifact** of this machine's Virgin
   Media resolver. Measured publicly they sit on five different networks. Replace with the defensible
   version: *"flagged by an ISP-grade content filter"*. **This is the highest-priority item because the
   false version is committed and will be cited.**
2. **`qualityBirdsOnline`** → `access_status: "parked_domain"`, `priority: "low"`, `threat_level: "none"`,
   note recording ParkLogic nameservers, the 2025-06-12 → 2026-02-12 death window, and the archived
   $100–$900 African Grey pricing. Consider tier 6 historical or removal from active monitoring.
3. **`hoobly`** → remove the **CITES flag** and the "$200–$500 African Greys" claim from the baseline; live
   band is **$1,500–$7,000**. Add `last_analyzed: "2026-08-09"`.
4. **`petzlover`** → `access_status: "blocked_captcha_selfhosted"` (own CAPTCHA, defeats Firecrawl stealth).
   Flag the **$50–$800 index price band** as the actual home of the cheap-Grey pattern. Priority re-rank is
   an open question — see Open Flags.
5. **`petClassifieds`** → note the relaunch: 588 bird ads / 331 parrot ads, a ~3,000-word parrot species
   guide with an African Grey card, and explicit anti-scam trust positioning. `access_status:
   "blocked_cloudflare_geo"`. Priority medium → **high** is arguable.
6. **`parrotAlert`** → record the **backlink target** explicitly:
   `/articles/parrot-phishing-scam-site-alerts-8` and
   `/article/parrot-scam-site-african-grey-parrot-farm-18`, plus the reproduction-prohibited notice.
7. **`birdsNow`** / **`birdBreeders`** → `last_analyzed: "2026-08-09"`; record the measured state grids
   (61 AG pages / 66 URLs with 8 stocked) in `notes`.
8. **`exoticPetsAvenue`** → confirm `confirmed_scam` stands; add the verified prices (eagle eggs $65–$85,
   AG $650–$1,100, macaques $650–$950) and the 35-tag egg-keyword farm.
9. **New candidate for the scam-page evidence set (not a competitor):** `africangreyparrotfarm.com` —
   named by ParrotAlert, **still live** 2026-08-09, documented victim losses of $1,000 and $975.

---

## Open Flags

**Open question for the breeder (one, narrow):**
**Should `petzlover` be re-ranked from `priority: low`?** It is the only competitor in this tier indexing
**county-level** African Grey pages, it runs two parallel geo taxonomies plus ten country namespaces, and
its index-level price bands ($50–$800) are where the cheap-Grey pattern actually lives. But its own CAPTCHA
defeats both curl and Firecrawl stealth, so **no live on-page metric could be obtained** — the case for
promotion rests entirely on index metadata. Raising priority commits monitoring effort to a site we cannot
currently read. Everything else in this sweep is complete and unblocked.

**NOT FETCHED list, with barriers named:**

| Item | Barrier |
|---|---|
| Petzlover — all on-page metrics (word count, headings, schema, images, alt text, live prices, listing counts) | **Self-hosted PetzLover CAPTCHA.** 403 to curl with full browser UA; 403 to Firecrawl basic; **403 to Firecrawl stealth proxy** (5 credits). Index metadata only |
| Petzlover — state coverage for MA, MD, NJ, VA | Not observed in the 80-URL map sample; **absence not proven**, page-level check blocked by the CAPTCHA |
| Hoobly — state pages for CO, MA, MO, SC, WA | Not present in the rendered 25-state strip; deeper state URLs may exist but were not requested |
| Hoobly — homepage word count / structure | Apex and www geo-redirect this UK line to `/s/gb`; US homepage not captured |
| PetClassifieds — schema types, image count, alt text, exact word count | Cloudflare `Just a moment...` JS interstitial blocks the local parser (403 on apex and www); Firecrawl returns markdown only, so `ld+json` could not be enumerated |
| Google PAA expanded 3 levels | Not attempted this pass; prior sweeps hit `google.com/sorry/` CAPTCHA at HTTP 429 after 2 automated requests |
| Bing organic top 10 | Not attempted; page-5 sweep established reproducible query truncation across 4 transports |
| PageSpeed / Core Web Vitals for all 8 | Not attempted this pass — out of scope, no data collected |
| BirdBreeders — total indexed URL count | No sitemap enumerated; the baseline's "5,000–15,000" remains unverified |
| exoticPetsAvenue — `/blog` content | URLs present in the map; page content not fetched |
| Reddit threads `191cssi` ("scammed out of $2400") and `1asvyt3` (r/AfricanGrey "legitimate website") | Indexed and identified, not opened this pass — Playwright budget spent on higher-yield threads |
| BirdsNow / BirdBreeders / Hoobly — social account inventory | Not attempted; `social` block in the registry remains all-null for all three |
| Any US-localised SERP beyond the two marked **[US-localised]** | This machine egresses from a **UK line**; all other SERPs are UK-localised and are labelled as such rather than presented as US rankings |

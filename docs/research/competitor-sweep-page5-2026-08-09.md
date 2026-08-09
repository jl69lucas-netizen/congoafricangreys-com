# Competitor Sweep — Page 5 (Tier 4 Marketplaces + Registry Identity Resolution)

Date: 2026-08-09
Analyst: cag-competitor-intel
Scope: **Research only.** No site files touched, `data/competitors.json` NOT modified (Part B is a proposal for breeder approval).
Protocol: `docs/artifacts/cags-universal-page-build-brief.html` §6 (Competitor Research and Query Fan-Out)

> **Not a page outline.** This is a Sprint-0 research artifact, so the Heading-Hierarchy Outline Gate
> and Header Style Declaration do not apply — no page is being built from these headings.

---

## Method and Barriers (read this before trusting any number below)

Every figure here came from a live fetch on 2026-08-09. Where a source could not be retrieved it is
written `NOT FETCHED` with the barrier named — never inferred.

| Channel | Tool | Status |
|---|---|---|
| Google organic top 10 | Firecrawl Search (Google-backed) | **OK** |
| Google organic (live render) | Playwright → google.com/search | **OK for 2 queries, then blocked** |
| Google PAA, 3 levels | Playwright | **NOT FETCHED** — `/sorry/` CAPTCHA interstitial, HTTP 429, after 2 automated requests |
| Google Related Searches | Playwright | **OK** (1 query captured before the block) |
| Bing organic top 10 | 4 independent methods | **NOT FETCHED** — see barrier note below |
| Bing Related Searches | Playwright + Firecrawl | **OK** |
| Bing autosuggest A–Z | `api.bing.com/osjson.aspx` | **OK** |
| Google autosuggest A–Z | `suggestqueries.google.com` | **OK** |
| Second-engine SERP | DuckDuckGo HTML/Lite (**Bing-syndicated index**) | **OK via Firecrawl proxy**; rate-limited from local IP |
| Section inventory | `firecrawl_map` | **OK** |
| Reddit mining | Firecrawl Search `site:reddit.com` | **OK** |

### Barrier note — Bing organic is genuinely unavailable, verified four ways

Bing **truncates the query to its first token** for automated clients: every method returned results
for *"Africa"* (Wikipedia, Britannica, BBC News) instead of the submitted query, while the
Related-Searches module on the very same response correctly reflected the real query
(*bird food, parrot food, parakeet food*). Confirmed via:

1. `firecrawl_scrape` of `bing.com/search` — 10 results, all "Africa"
2. `curl` with full browser UA + `Accept-Language` + `SRCHHPGUSR`/`_EDGE_S` cookies — 10 results, all "Africa"
3. Playwright with an established bing.com session — 10 results, all "Africa"
4. Bing **RSS** output (`&format=rss`) — 10 items, all "Africa"

Because the degradation is reproducible across four transports, **Bing organic top-10 is recorded as
NOT FETCHED**, and DuckDuckGo (which syndicates the Bing index) is used as an explicitly-labelled
proxy for second-engine visibility. It is a proxy, not Bing proper, and is labelled as such everywhere below.

---

# Part A: Marketplaces

Three Tier 4 sites that already have baseline reports at `docs/research/competitor-<id>-2026-05-11.md`.
Those baselines were written under `403`/`429` blocks and are largely **UNVERIFIED estimates**; this
pass adds the missing §6 depth and, where the live data contradicts the baseline, **says so explicitly**.

---

## A1 · Chewy — https://www.chewy.com

Tier 4 · marketplace_retailer · baseline `competitor-chewy-2026-05-11.md` (written under HTTP 429)

### 1. SERP snapshot

**Primary keyword: "african grey parrot food"**

Google (Firecrawl, Google-backed index), top 10:

| # | Result | URL | Type |
|---|---|---|---|
| 1 | Facebook group thread — "best food for African greys" | facebook.com/groups/64779050616 | Forum |
| 2 | r/parrots — "What do you feed them?" | reddit.com/r/parrots/6a8g5q | Forum |
| 3 | African Grey & Amazon Parrot Mix | morningbirdproducts.com | Product |
| 4 | **Feeding African Grey Parrots — VCA Animal Hospitals** | vcahospitals.com/know-your-pet/african-grey-feeding | **Vet authority** |
| 5 | Volkman Avian Science African Grey Bird Food | amazon.com | Marketplace |
| 6 | Species Specific African Grey | prettybird.com | Brand |
| 7 | Complete African Grey Feeding Routine | youtube.com | Video |
| **8** | **AFRICAN GREY FOOD (Free Shipping)** | **chewy.com/f/african-grey-food_c942_f55v381722** | **Chewy — faceted category** |
| 9 | Best brand of pellet food for African Greys | quora.com | Forum |
| 10 | Best Food for African Grey Parrots | parrotessentials.co.uk | UK retailer |

Second engine — DuckDuckGo / **Bing-syndicated**, top 10 for the same query:
birdwatchinghq · smallanimaladvice · africangreylife · wikihow.pet · birdhousetales · birdcare360.co.uk ·
jonspicks · northernparrots · parrotrealm · naturewithbirds. **Chewy does not appear organically at all.**

**The engine split is the finding.** On "best food for african grey parrot" (variation) Chewy appears on
the Bing-syndicated index **only as a paid Microsoft ad** — *"Bird Supplies at Chewy - Everything for
Every Bird"*, `ad_provider=bingv7aa`, `msclkid` present — while 12 organic slots go to independent
content sites. Chewy buys the Bing-side visibility it earns organically on Google.

Variation sweep (second engine, Bing-syndicated):

| Variation | Chewy organic? | Who actually owns it |
|---|---|---|
| african grey parrot food | No | birdwatchinghq #1, smallanimaladvice #2 |
| african grey parrot cage | No | naturewithbirds, northernparrots, **amazon.com #5**, birdcages4less |
| best food for african grey parrot | **No — paid ad only** | birdwatchinghq #3, birdhousetales #4 |
| african grey parrot toys | NOT FETCHED — DDG rate limit from local IP after 2 queries | — |
| african grey parrot supplies | NOT FETCHED — same barrier | — |
| african grey parrot care | NOT FETCHED — same barrier | — |

### 2. Query fan-out

Autosuggest A–Z + question-modifier sweep on the "african grey parrot food" stem:
**Google A–Z 48 · Bing A–Z 25 · Google question-mods 23 · union 64 unique · 26 are 6+ words (AEO/voice targets).**

Bing-only terms Google's suggest never returns (14) — a real second-engine gap:
`african grey parrot diet` · `african grey parrot treats` · `african grey parrot food suppliers` ·
`best african grey parrot food` · `parrot food african grey` · `can african grey parrots eat blueberries` ·
`what fruits can african grey parrots eat` · `looking for african grey parrot` · `buy african grey parrot`

6+-word conversational targets (sample of 26):
`how long can an african grey parrot go without food` · `what foods are bad for african grey parrots` ·
`what not to feed african grey parrots` · `toxic food for african grey parrot` ·
`foods african grey parrots can't eat` · `best pellet food for african grey parrot` ·
`african grey parrot diet in the wild` · `african grey parrot diet in captivity` ·
`soft food for african grey parrot` · `african grey parrot food to avoid`

Google Related Searches: NOT FETCHED for this stem (CAPTCHA hit before capture).
PAA 3-level expansion: **NOT FETCHED** — barrier as stated in Method.

### 3. Section / listing-page inventory

`firecrawl_map` (search "african grey") returned **38 African-Grey-relevant URLs** in four distinct families:

**Education hub — `/education/bird/…` (the real competitive threat, 11 pages found)**
- `/education/bird/general/whats-the-difference-between-congo-african-greys-and-timneh-african-greys` ← **comparison page**
- `/education/bird/general/african-grey-parrot-care-sheet`
- `/education/bird/parrot/dos-and-donts-for-african-grey-parrots`
- `/education/bird/parrot/best-talking-pet-birds`
- `/education/bird/parrot/how-long-do-parrots-live`
- `/education/bird/parrot/5-parrot-talking-myths-facts`
- `/education/bird/general/the-top-3-smartest-pet-birds`
- `/education/bird/general/best-pet-birds-for-beginners`
- `/education/bird/training-and-behavior/end-pet-bird-hand-fear`
- `/education/bird/health-and-wellness/bird-feathers-guide`
- `/education/bird/parrot` (hub)

**Faceted commerce landing pages (species-keyed, SEO-built)**
`/f/african-grey-food_c942_f55v381722` · `/f/african-grey-toys_c970_f55v381722` ·
`/f/african-grey-cages-accessories_c953_f55v381722` · `/sp/african-grey-parrot-food`

**Product + UGC** — product pages, `/product-reviews/`, `/product-questions/` (Q&A carrying African
Grey sizing answers, e.g. *"Is it big enough for an African Grey?" → "This cage is not suitable for
larger birds such as an African Grey."*)

**Adoption network** — `/g/dog-whippet_ga1` type pages: *"Search thousands of available pets from
shelters and rescues in Chewy's network."* Chewy now runs a shelter/rescue adoption listing product.

### 4. Visual inventory

- Faceted category pages: professional product photography, 5–10 images per product listing
- Education articles: photo-led, no infographics or comparison tables observed in the mapped set
- Video: none on the African Grey education pages sampled; YouTube owns the video slot (#7 organic)
- Alt text: descriptive and SEO-formed on product images
- Interactive: 24/7 "Connect with a Vet" chat, Autoship configurator, review + Q&A widgets

### 5. Reddit / forum mining — Chewy by name

| Thread | Verbatim | Read |
|---|---|---|
| r/AfricanGrey "Food for african greys" | *"They are often on Amazon, but always on Chewy.com."* | Default supply vendor |
| r/parrots "reputable and ethical websites that sell safe bird [products]" | *"Chewy.com has a great selection of everything bird related… customer service is amazing"* | Trusted on **supplies**, asked about in a *safety* frame |
| r/parrots "Send me your bird's toys" | *"Chewy has been the most reliable way I've found to order them."* | Reliability, not sourcing |
| r/parrots "I've always loved the idea of getting a bird" | *"…looked at what Chewy had for species and that list was long."* | **Misconception** — user browsing Chewy as if it lists live species |

Sentiment: uniformly positive, and **exclusively supply-side**. In no thread found does a redditor
treat Chewy as a place to obtain an African Grey.

### Correction to the 2026-05-11 baseline

The baseline recorded **"Comparison: None"**. That is now false: Chewy ships
`whats-the-difference-between-congo-african-greys-and-timneh-african-greys`, a direct
Congo-vs-Timneh comparison competing with CAG's own comparison cluster. The baseline also missed
Chewy's adoption-network product entirely.

### Key insight

Chewy's threat is **not** the storefront — it is `/education/`, which now includes a Congo vs Timneh
comparison and a care sheet ranking on informational queries CAG wants. Meanwhile Chewy is organically
invisible on the Bing-syndicated index and pays for that traffic, so the second engine is cheap ground
for CAG's own diet/care pages.

---

## A2 · Petfinder — https://www.petfinder.com

Tier 4 · marketplace_retailer · baseline `competitor-petFinder-2026-05-11.md` (written under HTTP 403)

### 1. SERP snapshot

**Primary keyword: "african grey parrot for adoption"**

Google (Firecrawl, Google-backed index), top 10:

| # | Result | URL |
|---|---|---|
| 1 | African Greys — Adopting | rescuethebirds.org |
| 2 | Adopting a female African grey (FB group) | facebook.com |
| 3 | Available Parrots for Adoption | birdsandbeaks.org |
| 4 | Lonely Grey Rescue | lonelygreyrescue.org |
| 5 | **African Grey Parrots — Adoption and Rescue Near You** | **adoptapet.com** |
| 6 | Texas Parrot Rescue | facebook.com |
| 7 | Florida Parrot Rescue | floridaparrotrescue.com |
| 8 | African Grey Parrots for Sale | birdbreeders.com |
| 9 | African Grey Adoption Fee — $500.00 | ctparrotrescue.org |
| **10** | **Grace — Adoptable Pet \| Petfinder** | **petfinder.com/bird/grace-…/fl/jacksonville/phoenix-landing-foundation-nc676/details** |

Google live render (Playwright, same query, same day) returned 9 organic results — rescuethebirds,
facebook, birdsandbeaks, lonelygreyrescue, floridaparrotrescue, **tcparrotrescue**,
**southfloridaparrotrescue**, **parrotsnaturally**, texasparrotrescue — **with no Petfinder result in
the visible set.** Both captures are reported as measured; the difference is index-vs-live-render and
is not resolved here.

Second engine (Bing-syndicated): NOT FETCHED for this query — DDG rate-limit from local IP.

**Google Related Searches (captured live):** `Adopt a bird near me` · `Adopt a parrot near me` ·
`African grey parrot for adoption near me` · **`Free African Grey parrot for adoption`** ·
`Rescue African Grey parrot for sale` · `African grey parrot for adoption usa` ·
**`African Grey for sale $200`** · `Bird adoption near me for free` · `Birds for adoption in NJ` ·
`Lonely Grey Rescue`

Two of those — *Free African Grey parrot for adoption* and *African Grey for sale $200* — are
**scam-bait queries**. A CITES Appendix I bird is never free and never $200; these are the exact
phrases the fraud sites in this registry are built to intercept.

### 2. Query fan-out

Stem "african grey parrot for adoption": **Google A–Z 221 · Bing A–Z 32 · question-mods 60 ·
union 285 unique · 260 are 6+ words.** This is by far the widest-fanning stem measured.

Bing-only terms (24), notable: `african grey parrot rescue near me` · `african grey parrots for rehoming` ·
`adopt an african grey parrot near me` · `buy african grey parrot online` · `breeding african grey parrots`

**The fan-out proves adoption and purchase intent are the same query space.** The "for adoption" stem
expands into `african grey baby parrot for sale`, `african grey birds for sale near me`,
`african grey parrot eggs for sale uk price` and the entire state list — i.e. searchers using
*adoption* language are frequently shopping, which is precisely the traffic CAG can convert.

### 3. Section / listing-page inventory

`firecrawl_map` (search "african grey") — three page families:

**Individual bird detail pages** — `/bird/<name>-<uuid>/<state>/<city>/<rescue-slug>/details`
Geography is baked into the URL path (`/wa/vancouver/`, `/ct/branford/`, `/fl/jacksonville/`,
`/va/winchester/`, `/ca/san-diego/`, `/nc/raleigh/`, `/ri/warwick/`, `/wi/edgerton/`).

**Geo search pages** — `/search/birds-for-adoption/us/<state>/<city>`
Confirmed live: `/us/pa/pittsburgh` · `/us/md/frederick` · `/us/ca/longbeach` (69 pet results)

**Organization pages** — `/member/us/<state>/<city>/<org-slug>`

**Inventory character (this is the strategic finding).** The African Grey listings Petfinder actually
carries are, verbatim from their own meta descriptions:

- ages **18, 20, 22, 23, 24, 25, 26, 28, 30, 34 years old**
- *"Grace is a 24 year old Timneh African Grey… recently surrendered by an elderly owner… She's missing most of her toes"*
- *"Tiki Baby-28 YO African Grey Prefers Women"*
- *"Templar 18 YO M African Grey - No DOGS!"*
- *"Captain… approximately 25-year-old DNA-sexed male Congo African Grey. He is semi-handleable."*
- *"Bonded pair, two males. DNA tested. **Cannot be handled.** Flighted."*
- *"Columbus is a 34 year old male Congo African grey… recently surrendered by his original owner"*
- A large share are already marked **"Adopted"** — expired inventory still indexed and ranking

Adoption fees found on-platform and in adjacent SERP results: **$500** (CT Parrot Rescue),
**$800** (Bandits Place), **$500–$800** (parrot-rescue FB group).

### 4. Visual inventory

- One to several shelter-supplied photos per bird; quality is user-generated, not professional
- Video: none observed
- Alt text pattern: bird name + species + location
- Interactive: zip-radius search, species/age/size filters, "Adopted" state badges
- No infographics, no comparison tables, no care-guide visuals in the African Grey set

### 5. Reddit / forum mining — Petfinder by name

| Thread | Verbatim | Read |
|---|---|---|
| r/parrots "Looking to adopt my next parrot in Washington/Oregon" | *"Petfinder.com and adoptapet.com"* + *"Grey's are one of the most difficult birds to own, especially if you get them during/post puberty."* | Petfinder named as the default channel — **alongside the warning about adopting an adult Grey** |
| r/parrots "Birds in need of adoption!" | *"Here is a link to our petfinder page. Joe, the African Grey who has had a rough life."* | Rescues use Petfinder as distribution, not a destination brand |
| r/AfricanGrey **"Can't find a African grey for under 5 k"** | *"Rescue has worked out for me so far. I waited for months and then went through six months of very very hard work but now have a relatively well [adjusted bird]"* | **The single most valuable quote in this sweep** |

That last thread is the whole CAG argument in a buyer's own words: the market reads Greys as
**$5,000+**, and the rescue alternative costs **months of waiting plus six months of very hard
rehabilitation work**. CAG's $1,500–$3,500 hand-raised, documented, weaned bird sits precisely in the
gap that thread describes.

### Correction to the 2026-05-11 baseline

The baseline asserted Petfinder "ranks for *african grey parrot for sale near me* with high DA." That
was an inference made under a 403 and is **not supported** by this pass: on the adoption head term
Petfinder ranks **#10 at best**, behind adoptapet.com (#5) and seven rescue sites, and did not appear
in the live-rendered top 9 at all. Petfinder's African Grey position is weaker than assumed.

### Key insight

Petfinder is not a pricing competitor — it is an **objection generator**. It ranks deep-linked
individual birds that are 18–34 years old, frequently un-handleable, sometimes missing toes, at
$500–$800, behind an application-and-approval gate, and a large fraction are already adopted. The
conversion page CAG needs is not "breeder vs adoption" in the abstract; it is a page that answers the
r/AfricanGrey buyer who says they cannot find a Grey under $5k and is weighing six months of
rehabilitation work against a weaned, documented baby.

---

## A3 · Marietta Bird Shop — https://www.mariettabirdshop.com

Tier 4 · marketplace_retailer · states_active `["GA"]` · baseline `competitor-mariettaBirdShop-2026-05-11.md`
(written under HTTP 403, nearly every field `UNVERIFIED`)

### 🚩 FINDING — their only African Grey page is hijacked into a gambling redirect chain

`https://mariettabirdshop.com/product/african-grey-parrot` — the **single** African Grey URL on the
site — no longer serves bird content. It serves a server-side redirect chain ending at an Indonesian
online-casino site.

Verified chain, `curl` without `-L`:

```
mariettabirdshop.com/product/african-grey-parrot
  → 301 → mariettabirdshop.com/product/african-grey-parrot/     (normal trailing-slash hop)
  → 301 → jellyrollskidswear.com/collections/dummies            (injected hop)
  → … 13 redirects total …
  → 200   www.mysteryinktattoos.com
          <title>THOR138 # Game Online Resmi Dapatkan Pengalaman Terbaik Hari Ini</title>
```

Evidence that this is real and not a fetch artifact:

- Reproduced **3/3 consecutive runs**, identical `Location` header each time
- Reproduced independently by **Firecrawl** (returned 545 casino images: *Togel, Slots, Live Casino, Sabung Ayam*) **and** by **curl**
- **Server-side HTTP 301** (`server: cloudflare`), not a JS or meta-refresh redirect — so **Googlebot receives the same 301**; confirmed with a Googlebot UA
- Destination page contains **0** occurrences of "african grey"

**Blast radius is exactly one URL, and it is the African Grey one.** Of 15 URLs tested,
**14 are clean** and 1 is hijacked:

| Clean (14) | Hijacked (1) |
|---|---|
| `/` · `/aboutus` · `/product/eclectus-parrots` · `/product/cockatiel` · `/product/green-winged-macaw` · `/product/moluccan-cockatoo` · `/product-category/macaws` · `/product-category/cockatoo` · `/health-guarantee` · `/shipping-and-delivery` · `/grooming` · `/boarding` · `/contact-us` · `/visiting-and-purchasing` | **`/product/african-grey-parrot`** |

CITES/legal flag: not a CITES misstatement, but a **compromised commerce site still listed in our
registry as a live African Grey competitor**. It is neither — and it should not be linked to from any
CAG page.

### 1. SERP snapshot

**Primary keyword: "african grey parrot for sale georgia"** — Google (Firecrawl), top 10:

| # | Result | URL |
|---|---|---|
| 1 | African Grey Parrots for Sale in Georgia — **$3,500 African Grey Babies** | birdsnow.com/africangreyparrotgeorgia.htm |
| 2 | atlanta for sale "african grey" | craigslist.org |
| 3 | Where to buy an African Grey in Columbia County, Georgia? | facebook.com |
| 4 | **Fancy Feathers: #1 Bird Store, Atlanta GA** — Norcross GA, 770-… | fancyfeathersstore.com |
| 5 | **African Grey Parrots for Sale in Atlanta, Georgia** — 19 available | theavianexchange.com/african-greys-for-sale/georgia/atlanta |
| 6 | Where can I buy a baby African grey parrot? (Georgia) | quora.com |
| 7 | African Grey Parrots for Sale — 28 listings | birdbreeders.com |
| 8 | African Grey Parrots Home | instagram.com |
| 9 | Birds in Atlanta Georgia | birdsnow.com/location/atlanta-georgia.htm |
| 10 | Papayago Rescue House | papayagorescuehouse.org |

**Marietta Bird Shop does not appear in the top 10 for its own state's head keyword** — consistent
with its only African Grey page being a redirect to a casino.

Second engine (Bing-syndicated): NOT FETCHED — DDG rate-limit from local IP.

Competitor prices harvested from this SERP (birdbreeders.com listings, live):
Congo **$8,500 / $8,500 / $8,500 / $6,800 / $6,500 / $3,900** · Timneh **$6,500 / $6,500** ·
Cape Parrot $5,400 / $5,200 / $4,800 · BirdsNow Georgia headline **$3,500 African Grey Babies**.

### 2. Query fan-out

Stem "african grey parrot for sale georgia": **Google A–Z 8 · Bing A–Z 31 · question-mods 12 ·
union 45 unique · 31 are 6+ words.** Google's suggest is nearly silent on this stem (8) while Bing
returns 31 — **30 of the 45 are Bing-only**, the largest engine asymmetry measured in this sweep.

Georgia-specific: `african grey parrot for sale georgia` · `african grey parrot for sale in georgia` ·
`african grey parrot for sale near atlanta ga` · `african grey parrot for sale atlanta` ·
`african grey parrot price near georgia`

**Legal / licence cluster surfaced by this stem — the highest-value discovery of the fan-out:**
- `do you need a licence for an african grey parrot`
- `do you need a license to own an african grey parrot`
- `is it legal to own an african grey parrot`
- `are african grey parrots legal in california`

Nobody in this registry is credibly positioned to answer those. CAG — captive-bred, CITES Appendix I
documented, USDA context — is.

Buyer-decision queries also present: `what is the best age to buy an african grey parrot` ·
`which is better male or female african grey parrot` · `cost of an african gray parrot`

### 3. Section / listing-page inventory

`firecrawl_map` — **35 URLs total**, the entire site:

| Family | Count | URLs |
|---|---|---|
| Live-bird product pages | 8 | african-grey-parrot **(hijacked)**, eclectus, cockatiel, green-winged-macaw, hahns-macaw, caique, rainbow-lorikeets, moluccan-cockatoo |
| Product categories | 5 | macaws, cockatoo, amazon-parrot, other-birds, parrot-products |
| Supplies/SKUs | ~10 | Aria toys, cages, Volkman Avian Science African Grey food, foraging feeder |
| Trust / service | 7 | `/aboutus` `/health-guarantee` `/shipping-and-delivery` `/grooming` `/boarding` `/visiting-and-purchasing` `/contact-us` |
| Account / legal | 4 | my-account, cart, lost-password, privacy-policy |

**Absent entirely:** blog · care guides · comparison pages · state/location pages · FAQ page ·
testimonials page · species guides.

### 4. Visual inventory (homepage, live)

- **533 words** — thin
- **29 `<img>`**, **0 `<iframe>`**, no video
- **0 `application/ld+json` blocks — no structured data of any kind**
- **No `<h1>` element at all**
- H2s: `FREE SHIPPING ON ALL ORDERS FOR PARROTS PRODUCTS` · `About Us` (×2) · `Education` ·
  `Nutrition` · `A Mutual Love for Birds` · `Featured Birds And Parrots` · then product names
- Live bird prices on homepage: **$1,000 · $1,200 · $1,500 · $700 · $400 · $350**; supplies $10.99–$109.99
- **"African Grey" appears exactly once** on the homepage; "Health Guarantee" once

### 5. Reddit / forum mining — Marietta Bird Shop by name

**Zero Reddit mentions found.** The only branded result is a Facebook page —
`facebook.com/Caiqueparrotsforsaleandadoption` operating as *"Marietta Birds Shop, Marietta GA"*,
whose copy references checking *"if they have acquired their USDA permit."* No r/parrots,
r/AfricanGrey or forum discussion of this business exists in the indexed set.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "African Grey at $1,000" | The African Grey page **redirects to a casino site**; no AG price is retrievable. $1,000 now appears against non-AG stock. |
| "Marietta Bird Shop owns local Georgia traffic" | **False.** Absent from the Georgia head-term top 10; BirdsNow, Craigslist, Fancy Feathers and The Avian Exchange own it. |
| "LocalBusiness schema expected" | **Zero** structured data on the homepage. |
| Threat: low regional | Revise to **none** — recommend `access_status: "compromised_redirect"` and removal from active monitoring. |

### Key insight

The Georgia African Grey market has **no incumbent bird-shop defending it** — Marietta's only AG asset
is a hijacked redirect, and the SERP is held by two classifieds (BirdsNow, Craigslist), one Atlanta
retailer (Fancy Feathers, Norcross), and a brand-new aggregator (The Avian Exchange) whose
`/african-greys-for-sale/georgia/atlanta` URL pattern shows exactly the state+city template CAG should
build against.

---

## Part A — cross-cutting gaps

### Page-type gaps

| Page type | Chewy | Petfinder | Marietta | CAG has it? |
|---|---|---|---|---|
| Congo vs Timneh comparison | **Yes** | No | No | Yes — defend it |
| Care sheet / diet guide | **Yes** | Partial | No | Yes |
| State + city landing template | No | **Yes** (`/us/<st>/<city>`) | No | **Partial — gap** |
| Legal / licence / CITES explainer | No | No | No | **Open — nobody owns it** |
| "Adoption vs captive-bred" decision page | No | n/a | No | **Gap** |
| Price-expectation page ("under $5k") | No | No | No | **Gap** |
| Structured data (`ld+json`) | Yes | Yes | **None** | Yes |

### Keyword gaps worth CAG pages (exact phrases, from measured fan-out)

| Phrase | Source | Why it matters |
|---|---|---|
| `do you need a license to own an african grey parrot` | Google question-mods | Zero credible incumbent; CITES App-I authority play |
| `is it legal to own an african grey parrot` | Google question-mods | Same cluster |
| `are african grey parrots legal in california` | Google A–Z | State + legality, compounds with location pages |
| `what is the best age to buy an african grey parrot` | Google question-mods | Maps to the 12–16-week weaning gate |
| `which is better male or female african grey parrot` | Google A–Z | CAG already owns male-vs-female — extend |
| `african grey parrot for adoption near me` | Google Related | Converts Petfinder-discovery traffic |
| `Free African Grey parrot for adoption` | Google Related | Scam-bait — route to the scams page |
| `African Grey for sale $200` | Google Related | Scam-bait — route to the scams page |
| `what not to feed african grey parrots` | Google A–Z | Chewy/VCA hold it; diet-page target |
| `how long can an african grey parrot go without food` | Google A–Z | Long-tail AEO, unowned |

### State coverage from the fan-out (against the canonical 22)

Autosuggest demand confirmed for **16 of 22**:
AZ · CA · CO · FL · GA · MA · MD · MI · NJ · NY · OH · SC · TN · TX · VA · WA

**No autosuggest signal for 6:** IL · IN · MN · MO · NC · PA
(Absence of a suggest token is not absence of demand — it is absence of *this* signal. PA in
particular has live Petfinder inventory at `/search/birds-for-adoption/us/pa/pittsburgh`.)

City-level demand: Atlanta · Austin · Chicago · Dallas · Houston · Las Vegas · Los Angeles · Miami ·
Phoenix · Portland · San Antonio · San Diego

---

# Part B: Identity Resolution

## What these 14 entries actually are

The brief described them as stubs with "only an id slug — no name, no url." Measured against
`data/competitors.json`, that is close but not exact, and the difference matters:

each of the 14 carries a **`domain`** key (not `url`), a `tier`, `discovered: "2026-08-03"`,
`discovered_via: "registry sweep - keyword 'african grey breeding pair for sale'"`, a `keywords` array
and a `notes` string. What they lack is **`name`**, **`url`**, and the full schema the other 30 entries
have (`tier_label`, `states_active`, `primary_keywords`, `keywords_found`, `last_analyzed`,
`priority`, `access_status`, `social`).

So this was not a blind resolution — the `domain` values acted as a corroborating hypothesis that each
independent name search either **confirmed**, **corrected**, or would have **falsified**. One domain
was corrected and one business name was corrected; nothing was falsified.

## Resolution table

**14 of 14 resolved. 0 unresolved. 0 recommended for removal on identity grounds.**

| id | Resolved name | URL | Tier | Confidence | Evidence |
|---|---|---|---|---|---|
| `exoticGlobalParrotsFarm` | Exotic Global Parrots Farm | https://exoticglobalparrotsfarm.com | 1 | **High** | Live homepage + `/shop/` + `/reviews/` retrieved via Firecrawl. WooCommerce, add-to-cart. Named AG stock: Aponi $1,650, Reni $1,650, Ritty $1,450 — **all "1 year 3 months old"**. curl blocked (000); **DNS resolves to 81.99.162.48 = Virgin Media *residential broadband, London GB*** |
| `royalBirdCompany` | Royal Bird Company (Avicultural Breeding Research Center) | https://www.royalbirdcompany.com | 1 | **High** | Live site; Yelp listing **2804 E Hwy 150, Lincolnton NC 28092**, (704) 735-8601; owners Mike & Sheila; "40 years+ of research"; FB + IG active; `/breeder pairs and single parrots for sale.htm` live |
| `denimixaniPetsParadise` | **Denimix Anipets Paradise** (id misspells the brand) | https://denimixanipetsparadise.com | 1 | **High** | Live; `/product/african-grey/` and `/product/red-factor-african-grey-parrot/`; FB page (20 likes). Also lists **macaque monkeys $3,500** and fertile parrot eggs |
| `buyAfricanGreyParrots` | Buy African Grey Parrots — Licensed Florida Breeder | https://buyafricangreyparrots.com | 1 | **High** | Live Shopify (© 2026, "Powered by Shopify"); `/pages/available-parrots`, `/policies/contact-information`; claims USDA-licensed FL breeder, vet health certificate + breeder's health guarantee |
| `hookbillsForSale` | Hookbills For Sale | https://www.hookbillsforsale.com | 2 | **High** | Live; `/species/parrots/african-greys-for-sale`, `/breeders/texas-bird-breeders.asp`; cited in a CEC (Commission for Environmental Cooperation) parrot-trade report |
| `grayBreedersFoundation` | Gray Breeders Foundation | https://graybreedersfoundation.yolasite.com | 1 | **Medium-High** | Content retrieved via Firecrawl (`/Order-Now.php`): *"family-run Model Aviculture Program (MAP) certified parrot breeder… established in 2015."* curl blocked by **Cloudflare challenge (403 "Just a moment…")**. Free Yola builder + FB page `BuyAfricangreyparrot` |
| `theAvianExchange` | The Avian Exchange | https://theavianexchange.com | 2 | **High** | Live; homepage states **71 verified breeders, 183 species, 28 African Greys**; `/african-greys-for-sale`, `/breeders`, and **state+city pages** `/african-greys-for-sale/georgia/atlanta`. Supabase-backed. IG launch post = new platform |
| `jcAviary` | JC Aviary | https://www.jcaviary.com | 1 | **High** | Live; **Austin TX 78745**, (512) 956-0937; **AFA member**; Yelp 16 reviews / 378 photos; BirdBreeders profile 187 reviews listing Congo + Timneh; TikTok 89.2K followers, ships Delta |
| `anasParrots` | Ana's Parrots & Supplies | http://anasparrots.com | 1 | **High** | Live with real client testimonials; **Stroudsburg / East Stroudsburg PA**, est. 2012 (Yelp); BirdBreeders reviews page. **Domain note below** |
| `parrotStars` | Parrot Stars | https://parrotstars.com | 1 (see note) | **High** | Live Shopify; **115 N Arlington Heights Rd, Arlington Heights IL 60004**; Yelp 41 reviews / 636 photos; dedicated `/collections/congo-african-grey` **and** `/collections/timneh-african-grey`; YouTube store tour |
| `birdsByJoe` | Birds By Joe | https://www.birdsbyjoe.com | 1 | **High** | Live; **265 US-22 E, Green Brook NJ 08812**, (732) 764-2473; BirdBreeders 36 reviews listing Congo + Timneh; Yelp; IG; covered by Inside Edition |
| `midnightParrotPlace` | Midnight Parrot Place | https://midnightparrotplace.com | 1 | **High** | Live, phone 224-231-8577; **Roselle IL**; owner **Lisa Alfonso**; FB 4,378 likes with Timneh African Grey baby posts. Note: BirdBreeders profile now reads *"Not Available"* (delisted there) |
| `handRearedParrots` | **Hand Reared Parrots For Sale — registry domain is wrong** | **https://handraredparrots.com** (registry has `handrearedparrots.com`) | 1 | **High** | `handrearedparrots.com` has **no DNS A record** — does not resolve. `handra**re**dparrots.com` resolves (195.200.9.234, 89.116.109.151) and returns HTTP 200, title *"Home \| Hand Reared Parrots For Sale"*, with **"Congo African Grey Parrots For Sale"** and Psittacus references |
| `featherHeadz` | Feather Headz Aviary | https://www.featherheadz.com | 1 | **High** | Live with named client testimonials (Vijay Janapa Reddi, Garret Trezona, Jamie Baker, John Biggs Jr., Natasha Armada); **Miami FL**; owner Erika; runs a second property `featherheadz.net` (forum); BirdBreeders profile; TikTok "Licensed facility located in Miami Florida" |

### Two corrections the registry needs

1. **`handRearedParrots` domain is dead as written.** `handrearedparrots.com` returns no DNS record;
   the live business is at `handraredparrots.com` (*handra-red*, not *hand-reared*). Without this fix
   every future sweep will log the entry as dead.
2. **`denimixaniPetsParadise` name.** The business is **Denimix Anipets Paradise** ("Denimix" +
   "Anipets"), not "Denimixani Pets Paradise" — the id split the words in the wrong place.

### Domain ambiguity to flag — Ana's Parrots

A 2019 r/AfricanGrey thread warns: *"The real website for Ana's Parrots and Supplies is
www.anasparrotsandsupplies.com. There are a lot of scammers posting African Grey's cheap."*
Measured today, that has **inverted**:

- `anasparrotsandsupplies.com` → HTTP 200 but serves a bare **`Index of /`** directory listing (abandoned)
- `anasparrots.com` → HTTP 200, full site titled *"Ana's Parrots & Supplies"* with real client testimonials

`anasparrots.com` is the current canonical property. The old Reddit warning is stale and should not be
cited as evidence against it.

### Tier classification note (breeder decision required)

The 2026-08-03 sweep assigned `tier: 1` (direct_breeder) to **Parrot Stars**, **Birds By Joe** and
**Marietta Bird Shop-style retail operations**, but `mariettaBirdShop` itself sits at `tier: 4`
(marketplace_retailer) in the same file. Parrot Stars ("So much more than a pet shop", Arlington
Heights storefront, boarding + grooming + supplies) and Birds By Joe (Green Brook storefront) run the
**same brick-and-mortar retail model as Marietta**. Tiering is currently inconsistent. Recorded, not
resolved — see Open Question.

### Light-pass §6 signals for the newly-identified sites

**SERP presence (measured this run):**
- **The Avian Exchange** — Google **#5** for `african grey parrot for sale georgia` via
  `/african-greys-for-sale/georgia/atlanta`. The only Part B site observed ranking on a *state* query,
  and it does it with a state+city template.
- **Feather Headz Aviary** and **Parrot Stars** both appear as supplier breeders **inside** The Avian
  Exchange's listings (`/breeders/feather-headz-aviary-9229b`) — the registry contains both the
  aggregator and its suppliers.
- **Exotic Global Parrots Farm** — held Google **#1** for its brand query; its `/shop/` page is fully indexed.

**Rough section counts:** The Avian Exchange = 10 species hubs + `/breeders` + state/city pages
(28 AG listings). Parrot Stars = per-species collections incl. separate Congo and Timneh.
Marietta = 35 URLs total (see A3). Hookbills For Sale = species pages + per-state breeder directories.

**Reddit mentions (real buyer sentiment, verbatim):**

| Site | Thread | Verbatim |
|---|---|---|
| **JC Aviary** | r/parrots "Is this website reliable?" | *"Check out JC Aviary. They ship within the US and are about as good as breeders come."* |
| **JC Aviary** | r/parrots "Is this a legit site to get a pet?" | *"I bought from jc aviary and **was not happy with my experience**."* — and in the same thread *"Yes, JC aviary is great"* |
| **JC Aviary** | r/parrots "Reputable breeder suggestions?" | *"Consider JC Aviary in TX. We have 2 parrots from them. I consider them a reputable breeder."* |
| **JC Aviary** | r/parrots dedicated thread | *"Have anyone purchased a birb from JC Aviary located in Texas?"* |
| **Parrot Stars** | r/parrots "Reputable breeder suggestions?" | *"I also highly recommend Parrot Stars in IL."* |
| **Parrot Stars** | r/parrots "Trying to find a breeder" | *"Parrot Stars is an amazing place… Arlington Heights"* |
| **Parrot Stars** | r/parrots summer festival thread | *"I've had some dealings with Parrot Stars and it's actually a really good business. They do amazing education…"* |
| **Birds By Joe** | r/parrots "Anyone use Birds by Joe in NJ?" | *"Looking for any experiences good or bad."* |
| **Hookbills For Sale** | r/parrots **"Is this Breeder a Scam?"** | *"His number was on the hookbills for sale post. He just sent me my deposit back when I asked him to keep his word about showing videos"* |
| **Ana's Parrots** | r/AfricanGrey | *"The real website… is www.anasparrotsandsupplies.com. There are a lot of scammers posting African Grey's cheap."* (now stale — see above) |

**The competitive read:** when r/parrots is asked "reputable breeder suggestions", the two names that
come back unprompted are **JC Aviary (TX)** and **Parrot Stars (IL)**. JC Aviary is CAG's closest
in-state rival and already owns Texas word-of-mouth. C.A.Gs has no comparable Reddit footprint.
Meanwhile Hookbills For Sale is the surface where a scam-deposit thread happened — useful, citable
material for our scam-prevention page.

### Trust / CITES flags among the resolved set

Flagged under Rule 8 (dubious claims on a CITES Appendix I species):

- **Exotic Global Parrots Farm** — three separate African Greys all listed at the identical age
  *"1 year 3 months old"*, sold add-to-cart, "ready for **worldwide delivery**", and the site is served
  from a **UK residential Virgin Media IP in London** while presenting as a farm. Multiple
  incompatible signals on an Appendix I species.
- **Denimix Anipets Paradise** — sells African Greys alongside **macaque monkeys ($3,500)** and fertile
  parrot eggs; the registry's own note records claimed 1–4 day *international* shipping and a returns
  policy on live birds.
- **Gray Breeders Foundation** — free Yola site, flat pricing, and a **"Model Aviculture Program (MAP)
  certified"** claim that is self-asserted on-page with no verifiable registration shown.

None of these three should ever be cited by CAG as a price or practice benchmark; all three are
**usable as documented examples** on `/how-to-avoid-african-grey-parrot-scams/`, exactly as
`exoticPetsAvenue` already is.

---

## Proposed registry patch (NOT applied — for breeder approval)

`data/competitors.json` was **not modified**, per the brief. Proposed changes, in priority order:

1. **Fix** `handRearedParrots.domain` → `https://handraredparrots.com` *(current value does not resolve)*
2. **Rename** `denimixaniPetsParadise` display name → "Denimix Anipets Paradise"
3. **Add** `name` + `url` to all 14 entries per the resolution table; normalise `domain` → `url` so
   the 14 match the schema of the other 30
4. **Set** `mariettaBirdShop.access_status` → `"compromised_redirect"`, `priority` → `low`,
   `threat_level` → `"none"`, with a note recording the 13-hop chain to `mysteryinktattoos.com`
5. **Reconcile** the retail-storefront tiering (Parrot Stars / Birds By Joe / Marietta) — see Open Question
6. **Update** `last_analyzed: "2026-08-09"` for `chewy`, `petFinder`, `mariettaBirdShop`
7. **Correct** `_meta.total_competitors` — it reads `30`; the file contains **44** entries

---

## Open Flags

**Open question for the breeder (one, narrow):**
Should brick-and-mortar shops that sell live African Greys — **Parrot Stars** (Arlington Heights IL),
**Birds By Joe** (Green Brook NJ) — be **Tier 1 direct_breeder** (as the 2026-08-03 sweep assigned) or
**Tier 4 marketplace_retailer** (as `mariettaBirdShop`, the same business model, is currently
classified)? The registry is internally inconsistent on this today and the answer changes which
monitoring cadence and which gap matrix they fall into. Everything else in this sweep is complete and
unblocked.

**NOT FETCHED list, with barriers named:**

| Item | Barrier |
|---|---|
| Bing organic top 10 (all queries) | Query-truncation bot mitigation — returns "Africa" results; verified via Firecrawl, curl+cookies, Playwright session, and Bing RSS |
| Google PAA expanded 3 levels | `google.com/sorry/` CAPTCHA interstitial, HTTP 429, after 2 automated requests |
| Second-engine SERP: `african grey parrot toys`, `african grey parrot supplies`, `african grey parrot care`, `african grey parrot for adoption`, `african grey parrot for sale georgia` | DuckDuckGo HTML rate limit from local IP (0 results after 5 backoff retries) |
| Marietta Bird Shop African Grey page content | Site compromised — URL 301s off-domain into a 13-hop chain to `mysteryinktattoos.com` |
| `exoticglobalparrotsfarm.com` and `graybreedersfoundation.yolasite.com` via curl | TLS/connection block (000) and Cloudflare challenge (403) respectively — **both retrieved successfully via Firecrawl**, so neither is dead |

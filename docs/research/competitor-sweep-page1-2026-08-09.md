# Competitor Sweep — Page 1 (Tier 1 High-Priority Direct Breeders)

Date: 2026-08-09
Analyst: cag-competitor-intel
Scope: **Research only.** No site files touched, `data/competitors.json` NOT modified (all patches at the end are proposals for breeder approval).
Protocol: `docs/artifacts/cags-universal-page-build-brief.html` §6 (Competitor Research and Query Fan-Out)
Sibling pass: `docs/research/competitor-sweep-page5-2026-08-09.md`

Registry ids in scope (5): `afrigreyparrots` · `exoticParrotPetstore` · `africanGrayParrotsForSale` ·
`silvergateBirdFarm` · `birdsForSales`

> **Not a page outline.** This is a Sprint-0 research artifact, so the Heading-Hierarchy Outline Gate
> and Header Style Declaration do not apply — no page is being built from these headings.

---

## Method and Barriers (read this before trusting any number below)

Every figure here came from a live fetch on 2026-08-09. Where a source could not be retrieved it is
written `NOT FETCHED` with the barrier named — never inferred.

| Channel | Tool | Status |
|---|---|---|
| DNS A records | `dig @1.1.1.1` and `dig @8.8.8.8` (**public resolvers only**) | **OK** |
| DNS A records | system resolver `194.168.4.100` | **UNSAFE — sinkholes a subset of parrot domains, see barrier note 1** |
| Reachability, apex + www | `curl --resolve <host>:443:<public-IP>`, HTTPS and HTTP | **OK** — all 10 hosts tested |
| Homepage + inner pages | `curl` with Chrome UA | **OK for 4 of 5 sites** |
| Homepage (silvergate) | Firecrawl scrape, `proxyUsed: basic` | **OK** |
| Inner pages (silvergate) | `curl` with Googlebot UA + retry loop | **OK for 8 of 9 pages** |
| Site URL inventory | `robots.txt` → `sitemap_index.xml` / `wp-sitemap.xml`, full sub-sitemap walk | **OK for 3 of 5** |
| Google organic top 10 | Firecrawl Search (Google-backed) | **OK for 6 queries, then HTTP 429** |
| Second-engine SERP | DuckDuckGo HTML (**Bing-syndicated index**) | **OK, 4 queries** |
| Google autosuggest A–Z + question mods | `suggestqueries.google.com` | **OK, 4 stems** |
| Bing autosuggest A–Z | `api.bing.com/osjson.aspx` | **OK, 4 stems** |
| Google PAA, 3 levels | — | **NOT FETCHED** — see barrier note 3 |
| Bing organic top 10 | — | **NOT FETCHED** — see barrier note 3 |
| Reddit thread mining | Firecrawl Search `site:reddit.com` | **OK** |
| Reddit full thread bodies | `reddit.com/....json` and Firecrawl scrape | **NOT FETCHED** — HTTP 403 `Blocked` / domain unsupported; SERP snippets used instead and labelled as such |
| Backlink / comment-spam verification | direct `curl` of the linking pages, href counting | **OK for 2 of 3** |

### Barrier note 1 — the system resolver poisons DNS evidence, and it has already produced a wrong registry finding

This machine's system resolver is **`194.168.4.100` (Virgin Media UK)**. It returns
**`81.99.162.48`** — PTR `lang-sspiprxy.network.virginmedia.net`, an **ISP interception proxy** — for a
*selective* set of parrot domains, while public resolvers return their true, distinct IPs.

Measured, 2026-08-09:

| Domain | System resolver | `@8.8.8.8` / `@1.1.1.1` | HTTPS pinned to the public IP |
|---|---|---|---|
| williamsafricangreys.com | 81.99.162.48 | 172.67.167.58 (Cloudflare) | **200** |
| exoticparrotsplanet.com | 81.99.162.48 | 185.77.97.125 | **200** |
| exoticglobalparrotsfarm.com | 81.99.162.48 | 66.45.23.70 | **200** |
| sherrybirds.org | 81.99.162.48 | 185.77.97.205 | **200** |
| parrotsfarm.com | 81.99.162.48 | 213.130.145.185 | **200** |
| exoticparrotfarms.com | 81.99.162.48 | 91.108.103.86 | **200** |
| paradisebirdsfarmaviary.com | 81.99.162.48 | 91.108.103.142 | **200** |

**Control test (this is what makes it a resolver artifact and not a hosting fact):** `example.com`,
`anthropic.com`, `wikipedia.org` and `congoafricangreys.com` resolve **identically** on the system and
public resolvers, and a deliberately non-existent domain returns nothing on both — so there is no
blanket wildcard. The substitution is selective, and it lands on exactly the domain set that a UK ISP
content filter would target.

**Consequence, stated plainly: the "one operator, one London residential broadband line" conclusion in
`docs/research/competitor-refetch-verdicts-2026-08-09.md` is a measurement artifact, and so are the four
`000 NO CONNECTION — genuinely unreachable` verdicts in the same document.** All seven domains resolve
to seven *different* public IPs and all seven return HTTP 200. This is carried into the proposals at the
end of this file; it is out of scope to fix here, but it must not go unrecorded, because
`exoticGlobalParrotsFarm` was re-tiered to `tier 6 suspect_seller` partly on that evidence.

What survives and what does not:

- **Void:** the shared-IP claim, the "five storefronts, one operator" claim, and the four unreachability verdicts.
- **Still standing, untouched by this correction:** the *page-level* evidence page 5 recorded against
  `exoticGlobalParrotsFarm` — three separate African Greys all listed at the identical age
  *"1 year 3 months old"*, add-to-cart checkout with "worldwide delivery" of a CITES Appendix I species.
  Those are on-page facts and do not depend on DNS.
- **Weaker observation, offered as an observation only:** `exoticparrotsplanet.com` + `sherrybirds.org`
  sit in `185.77.97.0/24`, and `exoticparrotfarms.com` + `paradisebirdsfarmaviary.com` sit in
  `91.108.103.0/24`. Same /24 is a shared budget host, **not** proof of common ownership, and is not
  asserted as one.

**All five domains in this sweep were re-verified on apex AND www, through `@1.1.1.1`, with
`curl --resolve` pinning, over both HTTPS and HTTP.** The system resolver agreed with the public
resolver for all five, so no verdict below rests on the poisoned channel.

### Barrier note 2 — `silvergatebirdfarm.com` is not cloaked, and the first measurement said it was

The first fetch of this domain returned a **LiteSpeed `.lsrecap` / Altcha "Bot Verification"**
interstitial to a Chrome UA while a Googlebot UA got full content — which reads exactly like cloaking,
and the registry already records `access_status: "blocked_cloudflare_cloak"`.

Re-tested under control — four UAs (Chrome, Googlebot, Bingbot, `curl/8.7.1`), three interleaved passes,
3 s apart — **12 of 12 requests returned full content**. The interstitial is a **burst-rate trigger, not
UA discrimination**, and it clears. Firecrawl retrieved the homepage with `proxyUsed: "basic"` (no
stealth needed). The site is also not behind Cloudflare at all: it is on `198.251.84.200`,
**FranTech Solutions (PONYNET / BuyVM)**.

Reported as **accessible**. One clean run would not have proved this either way — it took the second and
third pass to separate the two states.

### Barrier note 3 — Google PAA and Bing organic

- **Google PAA expanded three levels: NOT FETCHED.** Not attempted this pass. The page-5 sweep hit a
  `google.com/sorry/` CAPTCHA interstitial (HTTP 429) after two automated requests on the same day and
  from the same machine; spending the remaining Firecrawl budget on the five in-scope competitors was the
  better trade. Autosuggest A–Z plus question-modifier expansion was used instead and is reported as such.
- **Bing organic top 10: NOT FETCHED.** Page 5 verified four independent transports on the same day and
  found Bing truncates the query to its first token for automated clients. Not re-litigated here.
  **DuckDuckGo HTML is used as an explicitly-labelled proxy for the Bing-syndicated index** everywhere
  below. It is a proxy, not Bing proper.

---

## At a glance — the five, re-verified

| id | Host verdict (apex / www, public DNS, pinned) | Google top 10 | 2nd engine (Bing-syndicated) | Registry says | Correct? |
|---|---|---|---|---|---|
| `afrigreyparrots` | 200 / 200 → apex | absent, 6 queries | **#10, #2, #9** | `accessible`, states `[]` | status yes, **content profile badly stale** |
| `exoticParrotPetstore` | 200 / 200 → apex | **#10 and #7** | **#1, #6, #5** | `accessible`, "VERY LOW threat" | status yes, **threat rating wrong** |
| `africanGrayParrotsForSale` | **403 / 403**, both hosts, two networks | absent | absent | `dead_suspended` (Bluehost suspension page) | down yes, **symptom changed** |
| `silvergateBirdFarm` | 200 / 200 | absent | absent | `blocked_cloudflare_cloak` | **wrong on both counts** |
| `birdsForSales` | 200 / 200 → apex | absent | **#7, #10** | `accessible` | status yes, **content profile badly stale** |

Four of five baselines are materially wrong. That matches the page-2 hit rate.

---

# A1 · Afri Grey Parrots — https://afrigreyparrots.com

Tier 1 · direct_breeder · priority high · baseline `competitor-afrigreyparrots-2026-05-11.md`

Host: `46.202.182.155` (**Hostinger US**, `netname: HOSTINGER-HOSTING`). `www` 301s to apex.
Copyright reads **© 2026** — actively maintained.

### 1. SERP snapshot

**Google (Firecrawl, Google-backed index).** Absent from the top 10 on all six head queries tested:
`african grey parrot for sale` · `cheap african grey parrot for sale` · `congo african grey for sale` ·
`african grey parrot for sale near me` · `african grey parrot breeder` · `timneh african grey for sale`.

**Second engine (DuckDuckGo / Bing-syndicated) — this is where they live:**

| Query | Position | URL |
|---|---|---|
| african grey parrot for sale | **#10** | `/product/cheap-african-grey-parrots-for-sale/` |
| cheap african grey parrot for sale | **#2** | `/product/cheap-african-grey-parrots-for-sale/` |
| cheap african grey parrot for sale | **#10** | `/` |
| african grey parrot breeder | **#9** | `/` |

**The engine split is the finding.** Afri Grey is invisible on Google and holds three second-engine
slots — and it earns them on the **"cheap"** modifier, not the head term. On
`cheap african grey parrot for sale` they are #2 behind only a UK classifieds site.

### 2. Query fan-out

Stem `cheap african grey parrot`: **Google A–Z 239 · Bing A–Z 30 · question-mods 139 · union 365 unique ·
129 are 6+ words.**

Bing-only terms Google's suggest never returns (23), the commercially interesting ones:
`african grey parrot for sale cheap` · `african grey parrot for sale near me cheap` ·
`cheap african grey baby parrots for sale` · `african grey parrot breeders near me prices` ·
`buy african grey parrot online` · `live african grey parrot for sale` ·
`young african grey parrot for sale` · `looking for african grey parrot` ·
`where to buy an african grey parrot` · `cost of african grey parrot` · `how much is a african grey parrot`

**The whole "cheap" stem is a price-anxiety cluster, not a bargain-hunter cluster.** Fourteen of the 23
Bing-only terms are *cost/price* phrasings, not *cheap* phrasings. A searcher typing "cheap african grey"
is usually asking what one costs, which is a question CAG's price transparency answers and Afri Grey's
"$1,000 and up, pay by CashApp" answer does not.

### 3. Section / listing-page inventory

Full sitemap walk: **7 sub-sitemaps, 64 URLs.**

| Family | Count | Notable members |
|---|---|---|
| Posts | 9 | see geo + money pages below |
| Pages | 6 + root | `/store/` `/about/` `/contact-us/` `/cart/` `/checkout/` `/account/` |
| Products | 9 | listed below |
| Product categories | 1 | `/product-category/cheap-african-grey-parrots-for-sale-usa/` |
| **Product tags** | **35** | a keyword-tag farm — see below |
| Category / author | 2 | `/category/uncategorized/` `/author/afri-grey-parrots/` |

**Geo and money pages — the baseline said these did not exist:**

- `/african-grey-parrots-for-sale-near-new-jersey/` — 1,242 words, **12 H3s**
- `/african-grey-parrot-for-sale-in-new-york/` — 1,097 words, 10 H2s
- `/african-grey-parrot-for-sale-in-ohio/` — 945 words, 10 H2s
- `/product/african-grey-parrots-for-sale-in-texas/`
- `/african-grey-parrot-price/` — 1,016 words, H2 **"African Grey Parrot Price by State"**
- `/african-grey-parrot-for-sale-craigslist/` — 548 words, **a "vs Craigslist" trust page**
- `/african-grey-parrot-eggs-for-sale-in-usa/` — 1,002 words, 10 H2s
- `/where-to-buy-african-grey-parrot-usa/`
- `/red-factor-african-grey-genetic-evolution-uncovering-the-mystery-behind-the-scarlet-hue/`

**Their New Jersey page is the single best competitor artifact in this sweep.** Verbatim H3s:

> What Makes the African Grey Parrot So Special in New Jersey? · Species of African Grey Parrots
> Available at AfriGrey Parrots · **Are African Grey Parrots an Endangered Species?** · **Which
> Organizations Oversee the Affairs of African Grey Parrots?** · The AfriGrey Parrots Advantage: Ethics,
> Genetics & Lifetime Support · Preparing to Receive Your New African Grey Parrot · Delivery & Pick-Up
> Options in New Jersey · **Where to Take Your African Grey Parrot in New Jersey for Healthcare** ·
> What You Can Learn by Observing African Grey Parrots · **Best Parks in New Jersey for Enrichment Walks
> (With or Without Your Bird)** · Easy Payment Options at AfriGrey Parrots · Why New Jersey Families
> Choose AfriGrey Parrots

That is real local-entity depth — avian healthcare *in the state*, parks *in the state*, delivery
options *in the state* — and it is exactly the structure `cag-location-page-builder` is aiming at. It is
also the structure CAG can beat outright, because the two CITES-adjacent H3s (*endangered species*,
*which organizations oversee*) are asked and, on a site that takes PayPal Friends & Family, cannot be
credibly answered.

**Products (9):** `baby-congo-african-grey` · `female-baby-african-grey-for-sale` ·
`cheap-african-grey-parrots-for-sale` · `african-grey-parrot-delivery-usa` ·
`african-grey-parrots-for-sale-in-texas` · `fertilized-african-grey-parrot-eggs` ·
**`red-african-grey-parrot-for-sale`** · **`white-african-grey-parrot`** · `large-parrot-cages-for-sale-usa`

**Product tags (35) — an exact-match tag farm.** Sample: `cheap-african-grey-parrot-for-sale` ·
`buy-cheap-african-grey-online` · `black-african-grey-for-sale` · `black-african-grey-for-sale-cheap` ·
`cheap-white-african-grey-parrot-for-sale` · `white-african-grey-parrot-for-sale-california` ·
`african-grey-parrot-california` · **`africaln-grey-parrots-maryland`** (typo baked into the live slug) ·
`timneh-african-grey-parrot-for-sale` · `baby-african-grey-for-sale-usa`

### 4. Visual inventory

- Homepage: **804 words** · **H1 ×1, H2 ×4, H3 ×11, H4 ×1** · **4 `<img>`** · 0 `<iframe>` · 0 `<video>`
- **All four homepage images carry the identical alt text `"African Grey Parrots For Sale"`** — keyword
  repetition, zero descriptive value, four missed alt slots
- **No meta description on the homepage.** Title is `Home - afrigreyparrots.com` — no keyword targeting
- Schema: **1 `ld+json` block** — `WebPage`, `WebSite`, `Organization`, `ImageObject`, `BreadcrumbList`,
  `SearchAction`, `ReadAction`, `EntryPoint`, `ListItem`, `PropertyValueSpecification`.
  **No `Product`, no `Offer`, no `LocalBusiness`, no `FAQPage`** despite running WooCommerce
- No infographics, no comparison tables, no video anywhere in the fetched set
- `/about/` is **103 words** with no founder name, no address, no founding year

**Prices (measured):** store `$1,000 · $1,200 · $1,500 · $2,500` · price-guide page spans
`$1,000–$5,000` (`$1,500 · $2,000 ×4 · $2,500 · $3,500 ×3 · $4,000 ×3 · $4,200 · $5,000 ×2`) ·
eggs and accessories at `$200` and `$550`.

### 5. Trust and payment — the finding that matters

Verbatim from the homepage buying steps:

> **3️⃣ Complete Payment – Choose your preferred payment method— bank transfer, CashApp, or PayPal
> (Friends & Family) —and fill in the necessary details to finalize your purchase.**

**PayPal Friends & Family strips all buyer protection**, and r/parrots names it unprompted as the
disqualifying signal (verbatim, thread `1kgk0ii`): *"You should never buy anything with Paypal friends
and family from somebody who you don't know personally because you have no buyer protections."*

Also absent: no USDA mention, no CITES mention, no DNA-sexing claim, no address, no phone number, no
avian-vet affiliation, no named person. One "health guarantee" mention, one "breeder", one "review".

**Species claims to flag.** `white-african-grey-parrot` and `black-african-grey-for-sale` are offered as
buyable stock. Red-factor African Greys are a genuine, extremely rare pigment mutation — their
`/red-factor-african-grey-genetic-evolution…/` article is about a real phenomenon — but *white* and
*black* African Greys are not established commercially-available morphs, and listing them at
$1,200–$1,500 alongside "cheap" positioning is a listing-bait pattern, not an inventory.

### 6. Reddit / forum mining — Afri Grey Parrots by name

**Zero Reddit or forum mentions found.** The only branded off-site properties are two Facebook pages
using the `#afrigreyparrots` hashtag, one of which is titled **"African Grey Parrots | Redding CA"** —
the only geographic signal attached to the business anywhere, and it is not on the site.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "Word count ~295 (JS-rendered SPA)" | **804 words**, server-rendered WordPress |
| "H1s: None detected · H2s: None detected" | **H1 ×1, H2 ×4, H3 ×11, H4 ×1** — all present in raw HTML |
| "Images: 0" | **4**, all with the same alt text |
| "No state/geo pages detected" | **False.** Dedicated NJ, NY, OH pages + a TX product + CA/MD tags |
| "No dedicated: blog, about, FAQ, care guide, comparison" | `/blog/` and `/about/` exist; a **Craigslist comparison page** exists; FAQ and care guide still absent |
| "No pricing visible on homepage" | Still true of the homepage; **a full price-guide page now exists** spanning $1,000–$5,000 |
| "Sitemap reveals 'cheap' angle pages" | **Confirmed and deepened** — "cheap" is now the brand's whole second-engine position |
| Threat level LOW | Revise to **MEDIUM on the second engine only**. Zero Google presence; #2 on Bing-syndicated for the cheap modifier |

### Key insight

Afri Grey Parrots is not a weak competitor any more — it is a **second-engine competitor with a
better location-page template than its trust signals deserve**. Its NJ page answers *which organizations
oversee African Greys* and *where to find avian healthcare in your state* while the checkout asks for
PayPal Friends & Family. CAG can take that exact H3 architecture, answer the CITES and healthcare
questions with real documentation, and win the comparison on the one axis Afri Grey cannot contest.

---

# A2 · Exotic Parrot Pet Store — https://exoticparrotpetstore.com

Tier 1 · direct_breeder · priority high · baseline `competitor-exoticParrotPetstore-2026-05-11.md`
("Threat level: VERY LOW")

Host: `212.85.28.165` (**Hostinger US**). `www` 301s to apex. Copyright reads **© 2024** — stale.

### 1. SERP snapshot

**Google (Firecrawl, Google-backed index):**

| Query | Position | URL |
|---|---|---|
| african grey parrot for sale | **#10** | `/product-category/african-grey-parrot/` |
| cheap african grey parrot for sale | **#7** | `/product-category/african-grey-parrot/` |

**Second engine (DuckDuckGo / Bing-syndicated):**

| Query | Position |
|---|---|
| african grey parrot for sale | **#1** |
| cheap african grey parrot for sale | **#6** |
| timneh african grey for sale | **#5** |

**They hold the #1 organic slot on the head term on the Bing-syndicated index and a top-10 slot on
Google.** The baseline's "VERY LOW — no SEO foundation" is not survivable against that.

### 2. Query fan-out

Stem `african grey parrot for sale`: **Google A–Z 213 · Bing A–Z 21 · question-mods 91 · union 271
unique · 262 are 6+ words.** Only one Bing-only term on this stem
(`african grey parrot for sale colorado`) — a much tighter engine spread than the "cheap" stem.

The legality cluster surfaced across the four stems, and **nobody in this sweep is positioned to answer
it**: `do you need a license to own an african grey parrot` · `do you need a licence for an african grey
parrot` · `is it legal to own an african grey parrot` · `are african grey parrots legal in california` ·
`african grey parrot legal to own` · `african grey parrot license`. This corroborates the identical
finding from page 5 on a completely different stem set.

### 3. Section / listing-page inventory

Full `wp-sitemap.xml` walk: **6 sub-sitemaps, 199 URLs — 167 of them products.**

| Family | Count |
|---|---|
| Products | **167** |
| Product categories | 11 |
| Trust / policy pages | 9 — `/about-us/` `/health-guarantee/` `/shipping-delivery/` `/payment/` `/refund_returns/` `/bird-care/` `/parrot-feeding/` `/contact-us/` `/order-tracking/` |
| Blog posts | **3** — all dated June 26, 2025 |

**African Grey listings, live prices (from the category page):**

| Bird | Was | Now |
|---|---|---|
| Buy Baby African Grey Parrot Online | — | **$800** |
| Buy Baby Timneh African Grey Parrot online | — | **$950** |
| Buy Congo African grey parrot Online | — | **$1,300** |
| Rosie (female) | $2,100 | **$1,100** |
| Sunny (male baby) | $2,500 | **$1,600** |
| Sperry (male baby) | $2,900 | **$1,800** |
| Cory (male) | $3,400 | **$2,600** |
| Lulu & Kuku & Tyler | $4,500 | **$2,500** |
| Nina & Tyler | $4,700 | **$3,800** |

Six of nine African Greys carry a struck-through "Sale!" price. **A permanent discount on a live CITES
Appendix I animal is a retail-urgency device applied to a bird**, and it is the clearest tonal contrast
available to CAG's honest-pricing position.

### 4. CITES and legal flags — the most severe in this sweep

**`/product/spixs-macaw-parrots-for-sale/` — Spix's Macaw (*Cyanopsitta spixii*) offered for sale.**
Spix's Macaw is CITES Appendix I and **Extinct in the Wild**; the surviving population sits inside a
managed international breeding programme. Their own product copy states it, verbatim:

> *"spix macaw for sale is an extinct wildlife species, although several captive birds are kept and
> protected and preserved in several nations of the world through extensive breeding programmes."*

The page carries **9 product reviews**. Its product image filename is
**`4196744_090918-wls-cnnw-spix-macaw-img.jpg`** — a **WLS-TV / CNN Newsource** press image, `090918`
being September 2018, the month Spix's Macaw was declared extinct in the wild. They illustrated a
for-sale listing with the news photo announcing the species' extinction.

**`/product/peregrine-falcon-eggs/` — Peregrine Falcon eggs offered for sale**, verbatim:

> *"We sell very fertile candle-lit Falcon eggs with worldwide shipping. All our eggs are collect from
> very healthy birds in our Aviary… We are now taking orders from those who are interest in raising up
> their own falcon baby birds from the falcon eggs stage."*

Peregrine Falcon is protected in the US under the **Migratory Bird Treaty Act** and listed on CITES
Appendix I. This is the same class of finding that got `exoticPetsAvenue` marked `confirmed_scam`
("eagle eggs $65").

Also stocked: **Hyacinth Macaw $9,000** (Appendix I), **Black Palm Cockatoo** (Appendix I), plus a
20-SKU fertile-egg catalogue including `african-grey-parrot-eggs-available`, `toco-toucan-eggs`,
`fresh-fertile-ostrich-eggs-for-sale` and `hatch-a-parrot-trial-pack`.

**Copy provenance.** The shipping page is copied from another business and the find-and-replace was never
finished — verbatim:

> *"At **Timie's Bird Farm**, we strive to provide you with extraordinary customer service from beginning
> to end."*

The same page also states: *"All live birds are shipped by Airlines only. **We do not ship by USPS this
is illegal so please don't ask.**"* — which is correct, and which flatly contradicts silvergatebirdfarm's
homepage (A4 below).

### 5. Visual inventory

- Homepage: **1,997 words** · **H1 ×0 (no `<h1>` element at all)** · H2 ×9 · H3 ×18 · **H4 ×30** (the
  product grid) · **41 `<img>`** · 0 `<iframe>` · 0 `<video>`
- **7 of 40 images have empty alt text**
- **0 `application/ld+json` blocks — zero structured data sitewide.** The baseline said this and it is
  still true; it is now their single biggest technical liability given they hold a #1 second-engine slot
- **Image provenance across all 7 fetched pages:** 24 filenames are raw numeric social/press dumps
  (e.g. the WLS/CNN Spix photo), **5 are named `…-for-sale-UK-…`** (`african-grey-for-sale-UK-660x800.jpg`,
  `pair-african-grey-for-sale-UK-660x800.jpg`, `baby-african-grey-for-sale-UK-660x800.jpg`), and
  **3 are `WhatsApp-Image-2023-07-14-at-…`**
- Contact: **+1 (209) 560-6577** (area code 209 = Stockton / Modesto, CA) · `info@exoticparrotpetstore.com`
- Zoho SalesIQ live chat · WooCommerce star ratings (4.14–4.77 across the AG range)
- `/about-us/` names **no founder, no address, no founding year**
- **Health guarantee: 5 days**

### 6. Reddit / forum mining

No thread names this store directly in the indexed set. Two r/parrots threads are nonetheless
**directly diagnostic of its listings** (SERP snippets; full thread bodies `NOT FETCHED`, barrier: Reddit
403 `Blocked`):

| Thread | Verbatim | Why it lands here |
|---|---|---|
| r/parrots `1hq89a9` "Any Experience with This Seller?" | *"800 for an African Grey is way too cheap."* | Their entry African Grey is **exactly $800** |
| r/parrots `uggqql` | *"…checking the image sources, the filenames are all 'Whatsapp-Image-2021…'"* | Redditors already use WhatsApp-Image filenames as a scam heuristic. **Three of this store's African Grey product images are literally named `WhatsApp-Image-…`** |

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "Word count ~352 (JS SPA)" | **1,997 words**, server-rendered WooCommerce |
| "H2s: None detected · Images: 0 in raw HTML" | **H2 ×9, H3 ×18, H4 ×30, 41 images** |
| "No blog, no about, no shipping page, no health guarantee" | **All four exist.** Blog (3 posts), `/about-us/`, `/shipping-delivery/`, `/health-guarantee/` (5-day). FAQ still absent |
| "No phone number · No pricing visible" | **+1 (209) 560-6577** on every page; **nine African Greys priced $800–$3,800** |
| "No schema markup at all" | **Still true — 0 `ld+json` blocks.** The one baseline finding that held |
| "Threat level: VERY LOW — no SEO foundation" | **Wrong.** #1 second-engine and #10 Google on the head term |
| CITES flags | Baseline recorded none. **Spix's Macaw and Peregrine Falcon eggs are both live for sale** |

### Key insight

This is the highest-severity entry in the sweep and it is filed as "VERY LOW threat". A store that ranks
**#1 on the Bing-syndicated head term** while selling an **Extinct-in-the-Wild Appendix I macaw
illustrated with the news photo of its extinction**, and **Peregrine Falcon eggs**, is not a low
threat — it is the strongest documented example CAG has for
`/how-to-avoid-african-grey-parrot-scams/`, and it is beatable on schema, because it ships none.

---

# A3 · African Gray Parrots For Sale — https://www.africangrayparrotsforsale.com

Tier 1 · direct_breeder · priority high · baseline `competitor-africanGrayParrotsForSale-2026-05-11.md`
(the strongest baseline in this group — 1,360 words, LocalBusiness schema, MEDIUM threat)

Host: `129.121.64.190` — PTR `129-121-64-190.unifiedlayer.com`, **Oso Grande IP Services**
(the Bluehost / Newfold estate).

### Reachability — hard-down, and it is not a bot challenge

| Check | Result |
|---|---|
| apex `https://africangrayparrotsforsale.com/`, pinned to public IP | **403** |
| `www`, pinned to public IP | **403** |
| apex over plain HTTP | **403** |
| `www` over plain HTTP | **403** |
| Firecrawl scrape, `proxy: stealth` (independent network) | **403** |
| `robots.txt` | **500 Internal Server Error** |

The 403 body is a **bare Apache `ErrorDocument`** — no JavaScript, no CAPTCHA, no challenge page, no
Cloudflare header. The `robots.txt` 500 leaks the origin's internal hostname:

> *"Please contact the server administrator at **webmaster@website-e674f246.mxn.qzq.mybluehost.me**"*

A 403 is normally a bot challenge and not evidence of a dead site — that is why apex, www, HTTP, HTTPS
and a second network were all tested. **Every one returns an error, and the error is server-side, not a
challenge.** Verdict: **hard-down / broken or locked hosting account**, reproduced on two independent
networks. Not "dead" — DNS resolves and the server answers — but serving nothing.

### 1. SERP snapshot

`site:africangrayparrotsforsale.com` still returns **2 indexed URLs**, so Google has not yet dropped the
site:

| # | URL | Title |
|---|---|---|
| 1 | `/` | African Gray Parrots for Sale \| Hand-Raised Baby Congo African … |
| 2 | **`/newyork.html`** | **NY Breeder — African Gray Parrots for Sale in New York** |

Indexed meta for `/newyork.html`, verbatim: *"we provide healthy, hand-raised African Gray parrots to
serious buyers across NY including **New York City, Buffalo, Albany, Rochester**…"*

Absent from the top 10 on all six Google queries tested and from all four second-engine queries.

**Two facts the index reveals that the baseline did not have.** First, the site was rebuilt as **flat
`.html` files**, not WordPress — `/newyork.html` is a static state page. Second, the state strategy went
**city-level** (NYC, Buffalo, Albany, Rochester), which is one rung deeper than the baseline's
"states visible: CA, TX, FL, NY, GA".

### 2. Query fan-out — the "Gray" spelling is a real, separate demand pool

Stem `african gray parrots for sale`: **Google A–Z 167 · Bing A–Z 48 · question-mods 43 · union 221
unique · 186 are 6+ words.** Bing returns **48** on the "Gray" spelling versus 21 on the "Grey"
spelling — the widest Bing yield of the four stems measured.

Live "Gray"-spelling state terms measured: `african gray parrot for sale in florida` ·
`african gray parrot for sale ohio` · `african gray parrot for sale texas` · `where to buy african gray
parrot` · `gray african parrot for sale`.

**This entire pool is currently unserved by its exact-match-domain incumbent.** The one site built to own
"African Gray" is returning 403 sitewide.

### 3. Section inventory · 4. Visual inventory · 5. Conversion

**NOT FETCHED.** Barrier: HTTP 403 on every path, both hosts, both protocols, two networks; `robots.txt`
returns 500 so no sitemap is discoverable. No word count, no heading structure, no image count, no schema
verification and no price can be measured this pass. **The baseline's figures (1,360 words, 8 H2s, 3
images, LocalBusiness + PostalAddress + Offer schema, $1,000 price) are 2026-05-11 measurements and are
not re-confirmed.** They must not be quoted as current.

### 6. Reddit / forum mining

**Zero mentions found** under the brand or the domain.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| Site live, 1,360 words, MEDIUM threat, "best technical execution among direct breeders" | **403 sitewide.** None of it is currently verifiable |
| Registry note: "Bluehost 'Account Suspended' page" (2026-07-21) | **The symptom has changed.** No suspension page now — a bare Apache 403 plus a 500 on `robots.txt` leaking `…mybluehost.me`. Still down; different failure |
| "States visible: CA, TX, FL, NY, GA" | Index shows the state pages were **flat `.html` files** and went **city-deep** (NYC, Buffalo, Albany, Rochester) |
| Baseline: "CITES Appendix II" in the CAG-advantage column | **Wrong and must not propagate.** African Greys are **Appendix I** (CoP17, effective Jan 2017). This is a defect in our own baseline document, not in the competitor |
| Threat level MEDIUM | Revise to **dormant**. Still indexed, so recoverable if the host is restored |

### Key insight

The exact-match-domain owner of the **"African Gray"** spelling — a pool where Bing autosuggest returns
more than twice the terms it returns for "Grey" — has been serving 403s across two networks while
staying indexed. **That is a window, not a permanent gap**: the moment the hosting is restored, two
already-indexed URLs come back with them. CAG should be covering `african gray` variants *now*, while the
incumbent is dark.

---

# A4 · Silvergate Bird Farm — https://silvergatebirdfarm.com

Tier 1 · direct_breeder · priority high · baseline `competitor-silvergateBirdFarm-2026-05-11.md`
(entirely `BLOCKED — Cloudflare Human Verification`, threat `UNKNOWN`)

Host: `198.251.84.200` — PTR `c3.my-control-panel.com`, **FranTech Solutions (PONYNET / BuyVM)**.
**Not Cloudflare.** WordPress 7.0.3 + Elementor 4.2.2 + Slider Revolution + Google Site Kit.
Copyright **© 2025**; `og:updated_time` **2026-05-14**.

Access: see **Barrier note 2** — the `.lsrecap` Altcha interstitial is burst-triggered, **12/12 controlled
requests returned content**, and Firecrawl retrieved the homepage on the *basic* proxy.

### 1. SERP snapshot

**Absent from the Google top 10 on all six queries tested, and absent from all four second-engine
queries.** This directly contradicts the registry note of 2026-07-21 ("Still ranks #6 Google for 'congo
african grey for sale' at $1,500-$3,500"). On the live `congo african grey for sale` SERP the top 10 is
birdbreeders.com, graybreedersfoundation, theavianexchange, mybabyparrot, petlandnht, birdsnow,
featheredfriendshub, Facebook — **no Silvergate**.

### 2. Query fan-out

Covered by the four stems above; nothing in the fan-out is specific to this brand. Their own on-site
targeting is visible in the category meta, verbatim:
*"Looking for a Well Trained **Congo or Timneh African Grey parrots for sale**? Silvergate Bird Farm
offers hand-raised, socialized parrots with a health guarantee"* — a well-formed, correctly-targeted
meta description on a page that ranks nowhere.

### 3. Section / listing-page inventory

Sitemap: **NOT FETCHED** — `sitemap_index.xml` returned the Altcha interstitial on 12 consecutive
retries even with a Googlebot UA. Inventory below is from the homepage link graph plus 8 directly
fetched pages.

**13 product categories:** African grey · Amazon · Bird Cages · Caique · Cockatoos · Conures · Eclectus ·
**Fertile Parrots Eggs** · **Incubators** · Lovebirds · Parakeets · Rosella · Toucans · Macaws

**Trust and policy pages:** `/about-us/` · `/health-guarantee/` · `/bird-shipping-info/` ·
`/customer-reviews/` · `/terms-conditions/` · `/order-tracking/` · `/contact-us/` · `/blog/`

**African Grey category** (`/product-category/african-grey-parrots-for-sale/`) — 606 words, H1 *"African
grey"*, H2 *"Find Your Perfect African Grey Parrot Today"*, **3 listings**:

| Listing | Price | Detail |
|---|---|---|
| Congo African Grey Parrot | **$3,000 – $3,500** | *"Ages 3 to 5 months old / 6 to 9 months old · DNA Sexed · Male / Female"*, rated 4.91 |
| (two further listings) | **$2,500** and **$1,000** | — |

Verbatim: *"We have Males and Females African Grey Parrots for sale from 4 to 9 months old. DNA tested,
fully health tested with vet certificate."*

**Fertile Parrots Eggs — the direct rival to CAG's egg cluster.** African Grey Eggs, verbatim ladder:

| Quantity | 2 | 4 | 6 | 10 |
|---|---|---|---|---|
| Price | **$200** | **$400** | **$600** | **$1,000** |

= a flat **$100 per egg**, *"Grey Eggs Available: Congo African Greys Eggs / Timneh African grey Eggs"*,
*"get guaranteed delivery with an incubator and a handbook"*, rated 4.65. **CAG's egg page is $95 each
with free US shipping on 5** — Silvergate is the closest direct price rival found to date, $5/egg above
us, and they bundle an incubator.

**Blog — 10 posts, 3 of them African-Grey-specific:**
*Understanding African Grey Behavior: A Complete Guide for Parrot Owners* ·
**Gender Differences in African Grey Parrots: What Every Owner Should Know** ·
*Introducing a New Bird to an Older African Grey: A Comprehensive Guide for Bird Owners*
(plus Conure ×3, Eclectus ×2, Talking Birds, Bird Cage). The gender post is a direct hit on CAG's
male-vs-female comparison page; its image alt is literally `African Grey Parrot male vs female`.

**Shipping page — genuinely strong, and CAG should read it.** 978 words, **13 numbered H2s**:
*1. What We Ship · 2. Live Bird Shipping Methods · 3. Bird Health, Safety, and Pre-Shipping Care ·
4. Shipping Crates and Containers · 5. Weather and Airline Restrictions · 6. Shipping Timelines and
Processing · 7. Non-Shipping Days · 8. Tracking and Delivery Confirmation · 9. Customer Responsibilities
at Delivery · 10. Delays, Losses, and Unforeseen Events · 11. Refunds, Reshipments, and Cancellations ·
12. Legal and Regulatory Compliance · 13. Questions or Support*, with H3s *Domestic Shipping* /
*International Shipping*. It names CITES explicitly:

> *"All international live bird shipments are handled in compliance with: CITES (Convention on
> International Trade in Endangered Species) regulations; Import and export laws of both origin and
> destination countries; Airline-specific live animal policies."*

**Health guarantee — 7 days**, and it names the panel:

> *"All our birds are DISEASE TESTED negative for Polyomavirus (PVD), Avian Bornavirus (ABV),
> Proventricular Dilatation Disease (PDD), Psittacine Beak, and Feather Disease (PBFD), and Chlamydia
> psittaci."*

That is CAG's own Ledger panel plus ABV and PDD, on a **7-day** window against our 72-hour/3-day. Noted
as a real competitive fact, not a defect in ours.

### 4. Visual inventory

- Homepage `<h1>` **"Exotic Birds Store"** — the title tag is also *"Exotic Birds Store"*, with **no
  African Grey token in either**. Meta description likewise generic
- Schema: `PetStore`, `WebPage`, `WebSite`, `Organization`, `ImageObject`, `SearchAction`; category pages
  add `CollectionPage` + `BreadcrumbList` + `ListItem`. **No `Product`, no `Offer`, no `FAQPage`,
  no `LocalBusiness`**
- Category page: 9 images, 2 with empty alt; good descriptive alts on the three bird photos
  (`Congo African Grey for sale`, `Timneh African Grey for sale`, `Baby African Grey birds for sale`)
- **`/customer-reviews/` is 168 words and contains nothing but navigation and footer — the reviews page
  is empty.** Zero testimonials sitewide despite 4.91 and 4.65 star ratings displayed on products
- No infographics, no video, no comparison tables anywhere in the fetched set
- Verification tags present for Google Site Kit, **Bing (`msvalidate.01`)**, **Yandex**, and **Pinterest**

**Three unedited theme placeholders shipped to production:**

1. Footer email link is **`mailto:admin@mail.com`** while the displayed address is `info@silvergatebirdfarm.com`
2. Footer website link is **`https://yourdomain.com/`**
3. Search box reads **"Popular Searches: Sweater · Jacket · Shirt"** — the fashion-store demo content

**Contact-detail mismatch:** address **"Johnston, RI 02919, USA"**; phone **+1 857 230-0793** — the
**857 area code is Boston, Massachusetts**, not Rhode Island (401).

**Payments:** the footer badge image is named
`Visa-Master-Card-Bitcoin-PayPal-Payment-300x22-1.jpg` — **Bitcoin accepted for a CITES Appendix I
animal.** Reservation is WhatsApp-gated, verbatim: *"To reserve a bird, simply place your order and use
the WhatsApp button below to contact our support team and complete your purchase."*

**Internal contradiction on shipping.** The 13-section policy page says airline cargo or licensed animal
transport only. The homepage says something else entirely, verbatim:

> *"We offer shipping all over using either **Contential** or Delta airlines… **Shipping with the post
> office can be next day or second-day delivery.** Some birds can not be shipped with the post office and
> have to be shipped with Delta."*

**Continental Airlines ceased to exist in 2012** (merged into United), and **USPS does not ship
psittacines** — a fact their own competitor exoticparrotpetstore states correctly ("We do not ship by
USPS this is illegal"). Two factual errors on the homepage, contradicted by their own policy page.

### 5. Reddit / forum mining — and the off-page finding

**r/Macaws, thread `lscyqz` — "Scam....DONT FALL FOR THIS FAKE FARM. I DID THE RESEARCH"**, top SERP
snippet verbatim:

> *"Unfortunately I was just scammed by them!!! I'm more upset with myself for being so stupid!!!
> **Do not buy from from Silvergate bird farm!!!**"*

The thread has a Portuguese-translated mirror carrying an r/Scams cross-reference:
*"Fui enganado quando tentei comprar ovos férteis de arara online"* (*"I was scammed when I tried to buy
fertile macaw eggs online"*). Full thread bodies **NOT FETCHED** — barrier: Reddit `.json` returns HTTP
403 `Blocked` and Firecrawl does not support the domain. Snippets only, labelled as such.

**Off-page — a verified blog-comment spam network.** A branded search returned six results that are not
Silvergate properties at all: a vegan recipe blog, an Indonesian police procedure page, a travel magazine,
a Melbourne restaurant review, and two Brazilian legal sites. **Verified directly, not from the SERP:**

| Linking page | `silvergatebirdfarm` hrefs found in the live HTML | Planted as |
|---|---|---|
| `lisaeatsworld.com/2015/10/cumulus-inc-restaurant/` | **67** | blog comments dated 30 Apr 2025 |
| `vitamagazine.com/2024/02/18/where-to-find-the-clearest-warmest-water-in-the-world/` | **47** | blog comments dated 28 Aug – 10 Sep 2025 |
| `sixvegansisters.com/…/slow-cooker-peanut-tofu-broccoli/` | NOT FETCHED — HTTP 403 to curl | SERP snippet only |

Anchor targets include `/product-category/african-grey-for-sale`, `/product/congo-african-grey-for-sale/`,
`/product/red-fronted-macaw-for-sale/`, `/product/nanday-conures-for-sale/`. Comment text verbatim:
*"Discover the perfect African Grey Parrot for sale at Silvergate Bird Farm! Known for their intelligence
and talking ability, these hand-raised parrots make wonderful companions."*

**The company those links keep.** On the same comment threads, interleaved between the Silvergate
comments: *"buy vape uk, weed store London, cannabis shop near me"*, *"**best flash bitcoin**"*,
*"Buy Whole Melt Extracts in Australia"*, *"Buy Fryd Carts"*. This is a shared comment-spam operation
running cannabis, crypto-fraud and parrot links through the same injected placements.

### Corrections to the 2026-05-11 baseline and the 2026-07-21 registry note

| Claim | Measured 2026-08-09 |
|---|---|
| Baseline: "BLOCKED — Cloudflare Human Verification. No content accessible." | **Fully accessible.** 12/12 controlled requests returned content; Firecrawl succeeded on the *basic* proxy |
| Registry: `access_status: "blocked_cloudflare_cloak"` | **Wrong on both words.** Not Cloudflare (FranTech/BuyVM); not cloaking (burst-rate `.lsrecap` Altcha, clears on retry) |
| Registry: "now cloaks — redirects crawlers to recaptcha.cloud" | No redirect to `recaptcha.cloud` observed. The challenge is served **in place** at `/.lsrecap/recaptcha` |
| Registry: "Still ranks #6 Google for 'congo african grey for sale'" | **Not reproduced.** Absent from the Google top 10 on that query and five others, and from all four second-engine queries |
| Registry: "$1,500-$3,500 (SERP snippet)" | Live on-page range is **$1,000 – $3,500**; the Congo listing is **$3,000 – $3,500** |
| Baseline: "Likely a real, established business (justifies WAF investment)" | The inference does not hold. A $0 LiteSpeed feature on a budget VPS is not a WAF investment |
| Baseline: threat UNKNOWN, "treat as potential medium threat" | Revise to **negative / scam-evidence**. Named scam thread + verified comment-spam network + Bitcoin + WhatsApp-gated checkout + three unedited placeholders + RI address with an MA phone |

### Key insight

Silvergate is the clearest **"good content, disqualifying signals"** case in the registry: a 13-section
CITES-aware shipping policy and a named five-pathogen disease panel sitting on a site that takes Bitcoin
over WhatsApp, ships its theme's "Sweater / Jacket / Shirt" demo text and `admin@mail.com` to production,
claims USPS delivery on an airline that has not existed since 2012, has an **empty** reviews page, and
buys its links from a cannabis-and-crypto comment-spam network. **CAG should study their shipping page
and cite everything else on `/how-to-avoid-african-grey-parrot-scams/`.** Their $100/egg African Grey egg
ladder is also the closest live rival to our $95 egg price and should be watched.

---

# A5 · Birds For Sales — https://birdsforsales.com

Tier 1 · direct_breeder · priority high · baseline `competitor-birdsForSales-2026-05-11.md`
("Threat level: VERY LOW")

Host: `92.113.19.230` (**Hostinger DE** — `netname: HOSTINGER-HOSTING, country: DE`). `www` 301s to apex.

### 1. SERP snapshot

**Google:** absent from the top 10 on all six queries tested.

**Second engine (DuckDuckGo / Bing-syndicated):**

| Query | Position | URL |
|---|---|---|
| african grey parrot for sale | **#7** | `/africa-grey-parrots-for-sale/` |
| african grey parrot breeder | **#10** | `/africa-grey-parrots-for-sale/` |

Note the ranking URL: the slug is **`africa-grey`**, not `african-grey`. A typo'd slug is holding a
second-engine top-10 slot on the head term.

### 2. Query fan-out

Stem `african grey parrot breeder`: **Google A–Z 145 · Bing A–Z 27 · question-mods 67 · union 211
unique · 176 are 6+ words.**

Their own on-page H2s reveal what they target, verbatim from `/africa-grey-parrots-for-sale/`:
*"African Congo Bird Price"* · *"African Gray Cost"* · *"African Congo Grey for Sale – Trusted Health
Guarantee and Certification"*. All three are **price-intent phrasings used as section headers** — the
same demand pool the "cheap" stem exposed at A1.

### 3. Section / listing-page inventory

Full sitemap walk: **4 sub-sitemaps, 12 URLs total.** This is the entire site.

| URL | Words | What it is |
|---|---|---|
| `/` | **2,381** | homepage |
| `/africa-grey-parrots-for-sale/` | **1,909** | the only African Grey page |
| `/bird-breeders/` | **1,628** | titled "Bird Breeders" but is actually the **contact page** (H1: *"Bird Breeders – Contact Birds For Sales"*) |
| `/cockatoos-for-sale/` `/macaws-for-sale/` `/mynah-birds-for-sale/` `/quaker-parrots-for-sale/` `/toucans-for-sale/` | — | species brochures |
| `/hello-world/` | — | **the WordPress default post, never deleted** — this is the site's entire "blog" |
| `/form/` `/form/simple-contact-form/` `/category/uncategorized/` | — | plumbing |

**No location pages. No care guides. No comparison pages. No FAQ. No testimonials page. No real blog.**

### 4. Visual inventory

- Homepage: **2,381 words** · H1 ×1 · H2 ×12 · **H3 ×91** · 13 `<img>` · 0 `<iframe>` · 0 `<video>`
- **80 of the 91 H3s are lowercase keyword links, not headings** — a footer keyword farm rendered at H3:
  `parrots for sale` · `birds for sale near me` · `african gray parrot for sale` · `cockatoo price` ·
  `macaw parrot price` · `peacock feathers for sale` · `purple martin houses for sale` ·
  `duck houses for sale` · `bluebird houses for sale` · `umbrella cockatoo for sale near me` …
  The remaining 11 H3s are the testimonials
- **All 13 images carry the alt text `"birds for sales"`** — thirteen identical, non-descriptive alts
- Schema: `WebPage`, `WebSite`, `Organization`, **`PetStore`**, `Article`, `Person`, `ImageObject`,
  `SearchAction`. **No `Product`, no `Offer`, no `LocalBusiness`, no `FAQPage`**
- Meta description present and well-formed (the only one of the five with a clean homepage meta)

**Testimonials are template spam and self-identify as such.** All six are rendered as H3s and every one
contains the brand string twice, verbatim:

> *"Absolutely thrilled with the Birds For Sale from Birds For Sales! My African Grey arrived healthy and
> well-socialized. I highly recommend them for top-quality Birds For Sale."*
>
> *"Amazing experience buying Birds For Sale! Birds For Sales provided excellent support and my vibrant
> Macaw is now a beloved family member. Trustworthy source for exotic Birds For Sale."*

**`contact@example.com` is live in the page body** — the placeholder was never replaced.

**Named inventory and prices:** Zazu (male African Grey), Luna, Rio & Skye, Kobe & Nala, Ruby, Kiki
(Mynah), Jasper & Willow (Quakers), Zephyr (Toucan). Prices `$250 · $350 · $500 · $730 · $770 · $800 ·
$850 · $1,500`.

**Geography:** *"Location: **Bennettsville South Carolina**"* on the Rio & Skye listing. **SC is one of
the canonical 22 states**, and the registry has `states_active: []`.

### 5. Trust claims

Measured mention counts on the homepage: **USDA ×1 · CITES ×2 · DNA ×4 · hand-raised ×4 · breeder ×8 ·
health guarantee ×1 · veterinary ×1.** In context, verbatim:

> *"Shipping: Nationwide U.S. delivery available via **USDA-certified bird transport**. Local pickup
> welcome."*
>
> *"⚖️ Ethical: Captive-bred, **CITES-compliant**, vet-checked"* — attached to a **Toucan** listing,
> not to an African Grey

No address, no phone number, no named person, no founding year, no avian-vet affiliation. The site is a
**multi-species brochure with one African Grey page**.

### 6. Reddit / forum mining

**Zero mentions found** under the brand or domain. Nothing on Reddit, nothing on parrotforums.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "Word count ~365 (JS SPA)" | **2,381 words** homepage, **1,909** on the AG page — server-rendered |
| "H1s: None detected · H2s: None detected" | **H1 ×1, H2 ×12, H3 ×91** |
| "No LocalBusiness, no FAQPage, no Product/Offer schema" | Still true — **but the baseline missed `PetStore`**, which is present |
| "Blog/articles hinted (Article + Person schema)" | **There is no blog.** The only post is `/hello-world/`, the WordPress default |
| "No USDA AWA mention · No CITES documentation · No DNA sexing" | **All three now appear** — USDA ×1, CITES ×2, DNA ×4 |
| "No geographic targeting visible" | **Bennettsville, South Carolina** named on a listing — a 22-state hit the registry records as `[]` |
| "No pricing visible" | **$250 – $1,500** across named birds |
| "Multi-species marketplace = diluted authority" | **Confirmed and sharpened** — 12 URLs total, one AG page, six species brochures |
| Threat level VERY LOW | Revise to **LOW, second-engine only**. #7 on the Bing-syndicated head term is not nothing, but 12 URLs and a placeholder email cap it |

### Key insight

Birds For Sales proves how little it currently takes to hold a **second-engine top-10 slot on the head
term**: 12 URLs, one African Grey page, a typo'd slug, a keyword farm rendered as 91 H3s, thirteen
identical image alts and `contact@example.com` shipped live. **The Bing-syndicated index is measurably
softer than Google's**, and it is the cheapest ground in this sweep for CAG's existing for-sale cluster —
which already beats this site on every axis except that nobody has aimed at that engine.

---

# Cross-cutting analysis

## Page-type gaps across the five

| Page type | Afri Grey | Exotic Parrot Pet Store | AGPFS | Silvergate | Birds For Sales | CAG has it? |
|---|---|---|---|---|---|---|
| Dedicated state / location pages | **Yes (NJ, NY, OH, TX)** | No | **Yes (flat `.html`, city-deep)** | No | No | Partial — **extend** |
| Price-guide page | **Yes** ("Price by State") | No | No | No | No | Yes — defend |
| "vs Craigslist" trust page | **Yes** | No | No | No | No | **Gap — nobody else has it** |
| Fertile-egg cluster | **Yes** | **Yes (20 SKUs)** | No | **Yes ($100/egg)** | No | Yes — defend on price and honesty |
| Congo vs Timneh comparison | No | No | No | No | No | Yes — **uncontested here** |
| Male vs female comparison | No | No | No | **Yes (blog post)** | No | Yes — defend |
| Structured shipping policy | No | Yes (thin) | NOT FETCHED | **Yes (13 sections, CITES-aware)** | No | **Depth gap — study Silvergate's** |
| Health-guarantee page | No | Yes (5-day) | Yes per baseline | **Yes (7-day, 5-pathogen panel)** | No | Yes (72-hour/3-day) |
| Real testimonials page | No | Named but unverifiable | No | **Empty page** | Template spam | Yes — **strong differentiator** |
| Blog / care cluster | Thin | 3 posts | No | **10 posts, 3 AG** | **None** | Yes |
| FAQ page + `FAQPage` schema | No | No | No | No | No | **Nobody in this group ships FAQPage** |
| Legal / licence / CITES explainer | No | No | No | Partial (shipping only) | No | **Open — nobody owns it** |
| `Product` / `Offer` schema | No | **0 schema at all** | Per baseline only | No | No | **Nobody here ships Offer schema** |
| Named breeder, address, phone | None / none / none | None / none / **yes** | NOT FETCHED | None / **RI** / **MA phone** | None / **SC** / none | **All three — decisive** |

## Keyword gaps worth CAG pages (exact phrases, from measured fan-out)

| Phrase | Source | Why it matters |
|---|---|---|
| `do you need a license to own an african grey parrot` | Google question-mods | Zero credible incumbent across all five; CITES Appendix I authority play |
| `is it legal to own an african grey parrot` | Google question-mods | Same cluster; corroborates page 5 on a different stem set |
| `are african grey parrots legal in california` | Google A–Z | State + legality, compounds with location pages |
| `african grey parrot breeders near me prices` | **Bing-only** | Breeder + geo + price in one query; unserved |
| `african grey parrot for sale near me cheap` | **Bing-only** | The exact query Afri Grey ranks adjacent to and cannot answer honestly |
| `cost of african grey parrot` / `how much is a african grey parrot` | **Bing-only** | Price-anxiety phrasing, not bargain phrasing — CAG's transparency answers it |
| `african gray parrot for sale ohio` / `…texas` / `…in florida` | Google A–Z, **"Gray" spelling** | The exact-match-domain incumbent is 403 sitewide right now |
| `where to buy african gray parrot` | **Bing-only, "Gray" spelling** | Bing returns 48 terms on "Gray" vs 21 on "Grey" |
| `young african grey parrot for sale` | **Bing-only** | Maps to our 12–16-week weaning gate |
| `live african grey parrot for sale` | **Bing-only** | Disambiguates from eggs/supplies — our for-sale hub should carry the token |

## Price ladder measured this pass (live, 2026-08-09)

| Source | African Grey price | Note |
|---|---|---|
| Exotic Parrot Pet Store | **$800 – $3,800** | six of nine on permanent "Sale!" |
| Afri Grey Parrots | **$1,000 – $2,500** (guide claims to $5,000) | "cheap" positioning |
| Silvergate Bird Farm | **$1,000 – $3,500** (Congo $3,000–$3,500) | straddles CAG's range exactly |
| Birds For Sales | **$730 – $1,500** | multi-species brochure |
| **C.A.Gs (ours)** | **$1,500 – $3,500 Congo** | — |
| birdbreeders.com, live | **$3,900 – $8,500** Congo · $6,500 Timneh | the legitimate market |
| theavianexchange.com, live | **$4,000 – $8,500** Congo | screened breeders |

**CAG's range is the honest middle.** Everything below $1,500 in this group comes attached to at least one
disqualifying signal — PayPal Friends & Family, Bitcoin, WhatsApp-gated checkout, an extinct-in-the-wild
macaw, or a placeholder email. Everything above $3,900 is the aggregator market.

**Egg prices:** Silvergate **$100/egg** (2/$200, 4/$400, 6/$600, 10/$1,000, incubator bundled) · Afri Grey
`$200` and `$550` SKUs · Exotic Parrot Pet Store runs a 20-SKU egg catalogue (AG egg price NOT FETCHED —
category page not individually priced in the fetched set). **CAG at $95/egg with free US shipping on 5 is
the low, documented price in this group.**

## Health-guarantee window comparison

| Seller | Window | Panel named? |
|---|---|---|
| Silvergate | **7 days** | Yes — Polyomavirus, ABV, PDD, PBFD, *Chlamydia psittaci* |
| Exotic Parrot Pet Store | 5 days | No |
| **C.A.Gs (ours)** | **72-hour / 3-day** | Yes — PBFD / Polyomavirus PCR, DNA sexing, psittacosis (Ledger) |
| Afri Grey / Birds For Sales | mentioned, undefined | No |

Recorded as a genuine competitive fact: **Silvergate offers a longer window than we do.** CAG's counter is
not window length — it is that ours is backed by a named breeder, a real address, a real phone, DNA
paperwork per bird and a reviews page that is not empty.

## State coverage from the fan-out (against the canonical 22)

Autosuggest demand confirmed for **16 of 22**: AZ · CA · CO · FL · GA · MA · MD · MI · NJ · NY · OH · SC ·
TN · TX · VA · WA

**No autosuggest signal for 6:** IL · IN · MN · MO · NC · PA

**This is an exact match to page 5's 16/6 split, reached from a completely different stem set** (page 5
used food/adoption/Georgia stems; this pass used for-sale/cheap/gray/breeder stems). Two independent
measurements converging on the same 16 and the same 6 is meaningful corroboration — but absence of a
suggest token still is not absence of demand, and PA in particular has live inventory on other platforms.

**Competitor state presence measured this pass:** NJ, NY, OH, TX (Afri Grey, dedicated pages) · NY
city-deep (AGPFS, indexed) · RI (Silvergate, claimed address — **not** in the 22) · SC (Birds For Sales,
one listing) · CA (Afri Grey's Facebook page, Redding CA; Exotic Parrot Pet Store's 209 area code).

City tokens present in the fan-out: Atlanta · Austin · Chicago · Dallas · Fresno · Houston · Las Vegas ·
Los Angeles · Miami · Orlando · Phoenix · Portland · Sacramento · San Antonio · San Diego · Tampa.

## Trust / CITES flags among the five

Flagged under Rule 8 (dubious claims on a CITES Appendix I species):

- **Exotic Parrot Pet Store** — **Spix's Macaw** (Appendix I, Extinct in the Wild) offered for sale with
  9 reviews, illustrated with the WLS/CNN news photo of the extinction announcement; **Peregrine Falcon
  eggs** with "worldwide shipping" (MBTA-protected, Appendix I); Hyacinth Macaw and Black Palm Cockatoo
  (both Appendix I); shipping page copied from "Timie's Bird Farm"; zero structured data.
- **Silvergate Bird Farm** — named in an r/Macaws scam thread; **Bitcoin** payment badge; WhatsApp-gated
  checkout; verified blog-comment spam network (67 + 47 hrefs on two unrelated sites, interleaved with
  cannabis and crypto-fraud spam); `admin@mail.com` and `yourdomain.com` placeholders live; "Sweater /
  Jacket / Shirt" demo text; RI address with an MA phone; USPS live-bird claim; **Continental Airlines**,
  defunct since 2012.
- **Afri Grey Parrots** — **PayPal (Friends & Family)** named as an accepted method; "white" and "black"
  African Greys listed as buyable stock; no address, no phone, no named person; 103-word About page.
- **Birds For Sales** — template testimonials naming the brand twice per sentence;
  **`contact@example.com`** live in the body; "CITES-compliant" asserted on a Toucan; no address, no phone.

None of these four should ever be cited by CAG as a price or practice benchmark. All four are usable as
documented examples on `/how-to-avoid-african-grey-parrot-scams/`, exactly as `exoticPetsAvenue` already is.

---

## Proposed registry patch (NOT applied — for breeder approval)

`data/competitors.json` was **not modified**, per the brief. Proposals in priority order:

**Highest priority — corrections that void an existing published finding**

1. **Retract the shared-IP finding.** `docs/research/competitor-refetch-verdicts-2026-08-09.md` §"DNS
   resolution — four egg competitors and one registered breeder share one IP" is a **system-resolver
   artifact** (see Barrier note 1). All seven domains resolve to seven different public IPs and all seven
   return HTTP 200 when pinned. The four `000 NO CONNECTION — genuinely unreachable, do not register`
   verdicts (`sherrybirds.org`, `paradisebirdsfarmaviary.com`, `exoticparrotfarms.com`, `parrotsfarm.com`)
   are also artifacts — **all four are live**. Add a method line to that doc: *DNS must be resolved
   through `@1.1.1.1` or `@8.8.8.8`, never the system resolver, and any `dig` finding must be
   control-tested against a known-unrelated domain.*
2. **Re-examine `exoticGlobalParrotsFarm`'s tier-6 re-tier.** Its DNS leg is void. Its page-level evidence
   (three birds at an identical age, add-to-cart worldwide delivery of an Appendix I species) stands
   independently. Breeder decision, not a research-pass side effect.
3. **`silvergateBirdFarm.access_status`** → `accessible` (from `blocked_cloudflare_cloak`). It is not
   Cloudflare and it is not cloaking. Simultaneously propose `threat_level: "negative"`, `tier: 6
   suspect_seller`, `priority: low`, `states_active: ["RI"]` (claimed), with a note recording the r/Macaws
   scam thread, the Bitcoin payment badge, and the verified 67 + 47 comment-spam hrefs.
4. **`exoticParrotPetstore`** — raise `priority` and add a CITES flag. It ranks **#1 on the
   Bing-syndicated head term and #10 on Google** while selling **Spix's Macaw** and **Peregrine Falcon
   eggs**. Propose `tier: 6 suspect_seller`, `threat_level: "negative"`, and registration as scam-page
   evidence. Its current "VERY LOW threat" rating is the largest single misclassification found.

**Corrections inside the five**

5. **`afrigreyparrots`** — `states_active: ["NJ","NY","OH","TX"]` (dedicated pages) and note the
   PayPal Friends & Family payment method plus the "cheap" second-engine position (#2 on
   `cheap african grey parrot for sale`).
6. **`africanGrayParrotsForSale.access_status`** → `hard_down_403` (from `dead_suspended`). Symptom has
   changed: bare Apache 403 on apex and www, HTTP and HTTPS, two networks, plus a 500 on `robots.txt`.
   Still indexed — keep monitoring, do not delete.
7. **`birdsForSales`** — `states_active: ["SC"]` (Bennettsville listing); note 12 total URLs and the
   second-engine #7.
8. **Set `last_analyzed: "2026-08-09"`** for all five ids in scope.

**Adjacent findings discovered while sweeping (outside the five, flagged not applied)**

9. **`afroBirdsFarm` is not dead.** Registry says `dead_confirmed` / "HTTP 522… permanently down. Remove
   from active monitoring." Measured: **HTTP 200, 394 KB, 1,987 words, 61 "african grey" mentions,
   prices $175–$1,450**, title *"African Grey Parrot For Sale Perfect Companion"*, and it ranks **#8 on
   the second engine for `african grey parrot breeder`**. Propose `access_status: "accessible"`.
10. **`williamsAfricanGreys` is not inaccessible.** Registry says `inaccessible`. Measured: **HTTP 200**
    when resolved publicly, and it ranks **#1 on the second engine for `african grey parrot breeder`**.
    The `inaccessible` status is very likely the same DNS artifact.
11. **`exoticParrotsPlanet`** — also hit by the resolver artifact; resolves and serves normally on public
    DNS, and ranks **#3 on the second engine for `timneh african grey for sale`**.
12. **`birdsByJoe` — do not misread the SERP.** Its meta contains "IS CLOSED PERMANENTLY", but the live
    page reads *"BIRDS BY JOE 2 (SADDLE BROOK) IS CLOSED PERMANENTLY"* — **only the second location
    closed**; the Green Brook NJ store is active. Recorded so nobody files it as closed.
13. **Unregistered competitors surfaced this pass** (candidates only, no analysis performed):
    `featheredfriendshub.com` / Featherland Breeders Hub (Congo $2,700–$5,300) · **JAMES AFRICAN GREY
    PARROTS**, 3200 NE 83rd St, Kansas City, **MO** 64119, (816) 376-8897 — a **22-state** breeder with a
    Yelp presence and no registry entry · `exoticliveparrots.com` · `african-grey-parrot.com` ·
    `parrotcrown.com` · `liveparrots.com` · `forestryparrotsbreeder.com` · `birdandbeyond.com`.

---

## Open Flags

**Open question for the breeder (one, narrow):**
`docs/research/competitor-refetch-verdicts-2026-08-09.md` and the `exoticGlobalParrotsFarm` registry note
both rest partly on a DNS finding this pass has shown to be a resolver artifact. **Should that document be
amended in place with a retraction block, or superseded by a new dated doc that cites it?** The evidence
and the recommended wording are ready either way; only the placement is blocked. Everything else in this
sweep is complete.

**NOT FETCHED list, with barriers named:**

| Item | Barrier |
|---|---|
| Google PAA expanded 3 levels, all queries | Not attempted. Page 5 hit `google.com/sorry/` CAPTCHA (HTTP 429) after 2 automated requests on the same machine and day; budget spent on the five in-scope competitors instead |
| Bing organic top 10, all queries | Query-truncation bot mitigation verified four ways by the page-5 sweep on the same day. DuckDuckGo used as an explicitly-labelled Bing-syndicated proxy throughout |
| `africangrayparrotsforsale.com` — all on-page data (word count, headings, images, schema, prices, conversion flow, section inventory) | HTTP **403** on apex and www, HTTP and HTTPS, from this machine **and** from Firecrawl's stealth proxy; `robots.txt` returns **500**, so no sitemap is discoverable. The 2026-05-11 baseline figures are **not** re-confirmed and must not be quoted as current |
| `silvergatebirdfarm.com` sitemap and full URL inventory | `.lsrecap` Altcha interstitial on 12 consecutive retries, including with a Googlebot UA. Inventory reconstructed from the homepage link graph + 8 directly fetched pages instead |
| `silvergatebirdfarm.com/parrots-for-sale/` | Same interstitial, 8 retries, never cleared |
| Full Reddit thread bodies (r/Macaws `lscyqz`, r/parrots `1jlf17f`, `1hq89a9`, `1kgk0ii`, `uggqql`) | `reddit.com/….json` returns HTTP **403 Blocked**; Firecrawl returns "we do not support this site". **All Reddit quotes in this document are SERP snippets, labelled as such** — comment scores, dates and thread context are unverified |
| `sixvegansisters.com` comment-spam verification | HTTP **403** to curl. The other two linking pages were verified directly (67 and 47 hrefs), so the finding does not depend on it |
| Exotic Parrot Pet Store — African Grey **egg** price | The 20-SKU egg category was enumerated from the sitemap; individual egg prices were not on the fetched product page |
| PageSpeed / Core Web Vitals for all five | Not attempted this pass — Playwright budget spent on the DNS control test and the silvergate cloaking re-test, both of which changed a published conclusion |
| Social follower counts / posting cadence for all five | Not attempted. Only Facebook page *titles* were captured, via SERP |
| WHOIS / registrant data for all five | Not queried. **Do not name an operator or publish an ownership accusation on any of these five** — describe the measurable facts and let them speak |

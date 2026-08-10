# Competitor Sweep — Page 2 (Remaining Tier 1 Direct Breeders)

Date: 2026-08-09
Analyst: cag-competitor-intel
Scope: **Research only.** No site files touched, `data/competitors.json` NOT modified (Part C is a proposal for breeder approval).
Protocol: `docs/artifacts/cags-universal-page-build-brief.html` §6 (Competitor Research and Query Fan-Out)
Registry ids in scope: `afroBirdsFarm` · `exoticParrotsPlanet` · `williamsAfricanGreys` · `shadesOfGreys` · `africanGreyAviaries` · `compoundExotics`

> **Not a page outline.** This is a Sprint-0 research artifact, so the Heading-Hierarchy Outline Gate
> and Header Style Declaration do not apply — no page is being built from these headings.

---

## Method and Barriers (read this before trusting any number below)

Every figure here came from a live fetch on 2026-08-09. Where a source could not be retrieved it is
written `NOT FETCHED` with the barrier named — never inferred.

| Channel | Tool | Status |
|---|---|---|
| DNS A / NS / SOA / PTR | `dig` against system + 8.8.8.8 + 1.1.1.1 + 9.9.9.9 | **OK** |
| IP ownership | `whois` | **OK** |
| Homepage + interior pages | `firecrawl_scrape`, `maxAge: 0` | **OK, 6/6 sites** |
| Homepage + interior pages, second transport | `curl` with browser UA, `--resolve` where DNS was filtered | **OK, 6/6 sites** |
| Section / URL inventory | `firecrawl_map` | **OK for 4 of 6** — see Open Flags |
| Google organic top 10 | Firecrawl Search (Google-backed) | **OK** |
| Google autosuggest A–Z + question-mods | `suggestqueries.google.com` | **OK** — 3 stems |
| Bing autosuggest A–Z | `api.bing.com/osjson.aspx` | **OK** — 3 stems |
| Reddit thread body + all comments | Playwright → `old.reddit.com` | **OK** |
| Reddit via Firecrawl | `firecrawl_scrape` | **NOT FETCHED** — Firecrawl returns *"we do not support this site"* for reddit.com |
| Reddit via `.json` API | `curl` | **NOT FETCHED** — HTTP 403 bot challenge |
| **US second-engine SERP (Bing/DDG)** | DuckDuckGo HTML | **NOT FETCHED** — see barrier note |
| Google PAA expanded 3 levels | — | **NOT FETCHED** — not attempted; the Google-side automation budget was spent on autosuggest |

### Barrier note 1 — the local resolver is Virgin Media UK, and it sinkholes parrot domains

This machine's system resolver is **`194.168.4.100` / `194.168.8.100`** (Virgin Media UK). Virgin Media's
**Web Safe / VirusSafe** filter returns a sinkhole address, **`81.99.162.48`**
(`lang-sspiprxy.network.virginmedia.net` — a *security-service proxy*, not a host), for a specific set of
parrot-selling domains. Port 80 on that address returns `302 → websafe.virginmedia.com/virussafe-blocked.html`.

The filtering is **selective, not blanket** — control test, same resolver, same second:

| Resolves normally | Sinkholed to 81.99.162.48 |
|---|---|
| google.com · wikipedia.org · congoafricangreys.com · jcaviary.com · parrotstars.com · birdsbyjoe.com · shadesofgreys.com · compoundexotics.com · africangreyaviaries.com · afrobirdsfarm.com | **exoticparrotsplanet.com** · **williamsafricangreys.com** · exoticglobalparrotsfarm.com · sherrybirds.org · paradisebirdsfarmaviary.com · exoticparrotfarms.com · parrotsfarm.com |

**Consequence 1 — two in-scope sites were falsely unreachable.** `exoticparrotsplanet.com` and
`williamsafricangreys.com` return `SSL_ERROR_ZERO_RETURN` from this machine. Both are **fully live**; both
were retrieved via Firecrawl (remote egress) and again via `curl --resolve` against their real IPs.

**Consequence 2 — this falsifies a headline finding of the page-5 sweep.** See Part B.

### Barrier note 2 — DuckDuckGo/Bing returns a **UK** SERP from this machine

Because egress is a UK consumer line, `html.duckduckgo.com/html/?q=african+grey+parrot+breeder` returned
a wholly UK result set (purefeatheraviary.co.uk, pets4homes.co.uk, birdtrader.co.uk, exoticafricangrey.uk,
royalparrots.uk, africangreybabyparrot.co.uk) plus `ebay.co.uk` ads carrying `ad_provider=bingv7aa`.
That is a correctly-functioning localised SERP, not a bot block — but it is **not** the US second-engine
picture, so **US second-engine SERP is recorded NOT FETCHED**. No US ranking claim in this document rests
on it. *(The page-5 sweep used the same transport; its DDG rows should be re-read with this in mind.)*

### Scope caveat on the credential audit

The USDA/CITES/DNA/PBFD table in Part A §Cross-cutting was measured on **homepage HTML only**. That
scoping produced one false negative, caught and corrected here: `shadesofgreys.com` shows zero
disease-testing tokens on its homepage but carries a full screening statement on `/available-birds`.
Interior pages were checked individually for every site; the table is labelled accordingly.

---

# Part A: The Six Competitors

All six carry a baseline at `docs/research/competitor-<id>-2026-05-11.md`. **Five of the six baselines are
now materially wrong**, and in four cases the error is not staleness but a factual misread that survived
into `data/competitors.json`.

---

## A1 · Afro Birds Farm — https://afrobirdsfarm.com

Tier 1 · direct_breeder · registry `access_status: "dead_confirmed"` · baseline `competitor-afroBirdsFarm-2026-05-11.md`

### 🚩 FINDING — the registry URL is the `www.` host, and only the `www.` host is dead

| Host | DNS A | HTTP | Verdict |
|---|---|---|---|
| `afrobirdsfarm.com` (apex) | 104.21.6.76 / 172.67.134.155 (**Cloudflare**) | **200** | **LIVE** |
| `www.afrobirdsfarm.com` ← *the registry value* | 2.24.131.98 (**Hostinger GB**) | **000**, connection fails | dead |

The apex and the `www.` host resolve to **different providers**. The registry stores
`https://www.afrobirdsfarm.com`, which is the broken one — so every sweep since 2026-05-15 has recorded a
live, actively-publishing competitor as `dead_confirmed`. This is the same class of defect as
`handRearedParrots` in the page-5 sweep, and it has cost roughly three months of monitoring on what is
the **largest content operation among all six sites in this scope**.

### 1. SERP snapshot

Google (Firecrawl, Google-backed), **"african grey parrot breeder"**, top 10 — Afro Birds Farm **does not
appear**. Full table under A4 (shared query). Brand-term presence NOT FETCHED — not queried this run.

US second-engine: NOT FETCHED (Method, barrier note 2).

### 2. Query fan-out

Shares the `african grey parrot breeder` stem measured in A4. The slice that belongs to this competitor is
the **price and cage cluster**, because that is what they publish against:
`why are african grey parrots so expensive` · `how much is an african grey parrot worth` ·
`african grey parrot for sale baby price` · `african grey parrot breeders near me prices`.

They also own the only **Spanish-language** surface found in this entire sweep, and the fan-out confirms
Spanish-side demand exists (`african grey parrots price in pakistan`, `african grey parrot price in south
africa` show the stem fans internationally); Spanish query volume itself: NOT FETCHED — `suggestqueries`
was run `hl`-default (English) only.

### 3. Section / listing-page inventory

`firecrawl_map` returned, among others, **47 content posts plus a `/blog` hub** and **10 named-bird product
pages**. This is a real editorial operation, not a brochure:

**Comparison posts — 3, competing directly with CAG's comparison cluster**
- `/comparing-african-grey-parrots-and-cockatoos-intelligence-personality-and-care-needs/`
- `/macaw-vs-african-grey-which-one-should-you-choose-with-pictures/`
- `/african-grey-parrot-vs-amazon-parrots/`

**Price cluster — 9 posts**, incl. two dated guides (`...cost-2024-price-guide`, `...cost-2025-price-guide`),
`/african-grey-parrot-price/`, `/african-grey-parrot-price-guide/`, `/cost-of-a-congo-african-grey/`,
`/monthly-cost-of-an-african-grey-parrot.../` (×2)

**Cage cluster — 9 posts.** An entire topical silo CAG does not contest at all.

**Location posts — 3:** `/beautiful-african-grey-parrot-for-sale-in-florida/` ·
`/where-to-buy-african-grey-parrots-in-california/` · `/is-an-african-grey-parrot-a-good-pet-baltimore-vet/`

**Spanish-language posts — 2:** `/precio-del-loro-gris-africano-todo-lo-que-necesitas-saber/` ·
`/loro-gris-africano-precio-inversion-companerismo/`

**Competitor-listicle — 1:** `/top-affordable-online-breeders-african-grey-parrots/`

**Commerce:** `/parrots/` hub + Timy, Dan, Bella, Benny, Jack, Kenny, Lizzy, Magi, Sam, and
**African Grey Parrot Eggs**. Trust pages: `/about/` `/services/` `/contact/`
`/african-grey-parrot-shipping/` `/testimonials/`.

**Pricing, measured 2026-08-09:** homepage shows **Timy $1,400 · Bella $1,450 · Benny $1,600 · Eggs
$175.00–$600.00**. On `/parrots/` most named birds now render **without a price** and at least one reads
**Out of stock** — inventory is thinning while the content engine keeps running.

**Egg pricing is the direct collision:** their **$175–$600** against CAG's **$95/egg**.

### 4. Visual inventory

- Hero and body imagery is **Pexels stock**: `pexels-photo-6424438`, `pexels-photo-6447539`,
  `pexels-photo-1599533` (the last is the OG image). A breeder's own birds are not photographed for the
  homepage.
- Named-bird product images *are* bespoke (`/2025/01/Benny.jpg`, `Jack.jpg`, `Kenny-2.jpg`).
- Reviews widget: **4.6, "Based on 34 reviews"**, 56% five-star / 44% four-star, names masked
  (`H**** G*****`). One review is in Spanish.
- Video: none on-page; a YouTube link (`youtu.be/TFNFhS0SqbU`) sits in the footer.
- Social: Facebook, LinkedIn, Pinterest, Twitter/X, YouTube — the widest social footprint of the six.
- Stack: WordPress + WP Rocket; `og:updated_time` **2025-08-17**.

### 5. Reddit / forum mining

**Zero Reddit mentions found** for "afro birds farm" / "afrobirdsfarm" in the `site:reddit.com` sweep.

### Corrections to the 2026-05-11 baseline

| Baseline / registry claim | Measured 2026-08-09 |
|---|---|
| "CONFIRMED DEAD: HTTP 522 … permanently down. Remove from active monitoring." | **False.** Apex returns HTTP 200 with a 47-post blog. Only the `www.` host — the value stored in the registry — fails. |
| "No data available from prior analysis either." | Full site retrieved, both transports. |
| `access_status: "dead_confirmed"`, `priority: "low"` | Should be `accessible` / high — this is the strongest content competitor in scope. |

### Key insight

Afro Birds Farm is the one competitor in this cohort executing **CAG's own playbook** — comparison posts,
a price cluster, location posts, an eggs SKU — and it has been invisible to us for three months because
the registry stored a hostname that does not resolve. Their two exposed flanks are **stock photography on
the homepage** and **zero health documentation**; their unclaimed ground is **the cage silo (9 posts) and
Spanish-language search**, neither of which CAG contests.

---

## A2 · Exotic Parrots Planet — https://exoticparrotsplanet.com

Tier 1 · direct_breeder · registry `access_status: "accessible"` · baseline `competitor-exoticParrotsPlanet-2026-05-11.md`

### The site was rebuilt from scratch; the baseline describes a site that no longer exists

`article:published_time` **2025-11-13**, `modifiedTime` **2025-12-05**, copyright **2026**. Every
structural claim in the baseline ("~421 words, no H1, no H2, no title, zero schema, no blog/about/
shipping/guarantee/FAQ") is now false.

### 1. SERP snapshot

Google, "african grey parrot breeder", top 10 — **does not appear**. US second-engine: NOT FETCHED.

### 2. Query fan-out

The AG category page answers **"What's the difference between Congo and Timneh African Greys?"** on-page,
which places it directly on CAG's comparison territory. Relevant measured demand from the shared fan-out:
`how many types of african grey parrots are there` · `african grey parrot types` (Bing-only) ·
`is an african grey a parrot` · `african grey talking parrot price`.

### 3. Section / listing-page inventory

`firecrawl_map` NOT RUN for this domain (see Open Flags); counts below are read from the site's own
category widget, which is stronger evidence than a map sample:

| Category | Products |
|---|---|
| **African Grey Parrots** | **4** |
| Amazon Parrots | 32 |
| Parrot Cages | 29 |
| Incubators | 28 |
| Conure Parrots | 19 |
| Cockatoo Parrots | 16 |
| Macaw Parrots | 15 |
| **Parrot Eggs** | **11** |
| Asiatic / Australian / Pionus | 5 each |
| Eclectus | 3 |

Pages: `/shop/` `/health-guarantee/` `/return-policy/` `/faq/` `/about-us/` `/contact-us/` `/checkout/`
`/my-account/`. **No blog.**

**African Grey inventory, live:** Alpha (Congo) **$800.00** · Chloe **$850.00** · Leo **$1,349.99** ·
Nala (Timneh) **$1,349.99**.

The AG category page is a genuine content asset: cage minimum `2' x 2' x 3'`, a diet spec (arugula, kale,
green beans, pomegranate, mango, hemp/flaxseed, half-cup pellets + quarter-cup fresh daily), a
feather-plucking warning, and a 3-question FAQ.

### 4. Visual inventory

Two listing images tell the story:

- **`Alpha`** (their headline Congo, $800): `grey-parrot-6390783_1920.jpg` — the `word-NNNNNNN_1920`
  filename is the **Pixabay** stock-download convention.
- **`Chloe`** ($850): `Screenshot_20240920-220156_Instagram-247x247.jpg` — **a screenshot of an Instagram
  post**, used as the product photo.

Other assets are `Parrot3/5/7/8/11.jpg` via the Bunny-optimizer path. No video. No original aviary
photography identified.

### 5. Reddit / forum mining

**Zero Reddit mentions found** for "exotic parrots planet".

### 🚩 Trust / CITES flags (Rule 8)

1. **Payment rails: PayPal, Apple Pay, Bank Transfer, SEPA, BitCoin, Western Union.** Bitcoin and Western
   Union are irreversible and are the standard fraud rails; SEPA is a euro-area instrument on a site
   presenting a Los Angeles address.
2. **Address/phone mismatch.** Address `1402 Wellesley Ave #103, Los Angeles, CA 90025`; phone
   **+1 (915) 221-0809** — **915 is El Paso, Texas**, ~700 miles from that address. Suite `#103` at a
   Wellesley Ave street number is a mailbox-suite pattern.
3. **"Decades of expertise since 1994"** on a site first published **2025-11-13**.
4. **Add-to-cart international shipping of a CITES Appendix I species** — *"we serve multiple countries
   including the USA, Canada, the UK, the Middle East, Thailand"*, plus a **Return Policy on live birds**.
5. **$800 for a Congo African Grey**, against a US market that this sweep measures at $1,000–$7,000.
6. Also sells **incubators (28 SKUs) and fertile eggs (11 SKUs)** alongside live App-I birds.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "~421 words (JS SPA)", "H1s: None", "H2s: None", "Title: None" | Full server-rendered WordPress/WooCommerce; H1 *"Find Your Perfect, Healthy Companion Parrot"*; many H2/H3; title *"Home - Exotic Parrot Shop \| Live Parrots & Supplies"* |
| "Zero schema markup — no structured data at all" | **False.** `Article, ImageObject, Organization, Person, SearchAction, WebPage, WebSite` present |
| "No blog, no about, no shipping page, no guarantee, no FAQ" | `/about-us/`, `/health-guarantee/`, `/return-policy/`, `/faq/` all live. (No blog — that part holds.) |
| "No physical address. No phone." | Both now published (and both are flags — see above) |
| "Threat level: VERY LOW" | Revise: **low as a ranking rival, elevated as a fraud-pattern exhibit** |

### Key insight

This is now a **fully-built commerce site with an $800 Congo, Western Union and Bitcoin checkout, an
Instagram screenshot as a product photo, and a Los Angeles address paired with an El Paso phone number**.
It is not a ranking threat; it is the single best-documented fraud-pattern exhibit found in this sweep and
belongs on `/how-to-avoid-african-grey-parrot-scams/` next to `exoticPetsAvenue`.

---

## A3 · Williams African Greys — https://williamsafricangreys.com

Tier 1 · direct_breeder · registry `access_status: "inaccessible"` · baseline `competitor-williamsAfricanGreys-2026-05-11.md`

### The "SSL error" was our resolver, not their certificate

Baseline: *"SSL ERROR / BLOCKED … second analysis attempt where williamsafricangreys.com was unreachable …
Expired SSL certificate (most common reason) … likely dead."* Measured today: the SSL failure reproduces
**only** through the Virgin Media resolver, which sinkholes this domain (Method, barrier note 1). Against
8.8.8.8 / 1.1.1.1 / 9.9.9.9 the domain resolves to **Cloudflare** (172.67.167.58 / 104.21.16.100), NS
`malavika.ns.cloudflare.com`, and returns **HTTP 200** with a complete WooCommerce storefront. The
certificate is fine. **The site is live and was very likely live in May too.**

### 1. SERP snapshot

Google, "african grey parrot breeder", top 10 — **does not appear**. US second-engine: NOT FETCHED.

### 2. Query fan-out

Their catalogue is **African Grey + Blue Gold Macaw only**, which maps to the comparison demand in the
fan-out (`macaw vs african grey` is a live query Afro Birds Farm already publishes against). They ship
**pairs** (`Alex and Lizzy`, `Linda & Lamar`, `Roy & Joy`, `Willow & Ajax`), which lands on the registry's
own `african grey breeding pair for sale` sweep keyword.

### 3. Section / listing-page inventory

`firecrawl_map`: **25 named product pages**, 2 product categories, and a policy set that is unusually
complete for a site with no address:

Products — Alex and Lizzy, Angel, Chyly, Coco, Colby, Collins, Cory, Dasha, Dennis, Frida, Gracy, Jeani,
Kitoko, Linda & Lamar, Luna, Martha, Rico, Romeo, Rosie, Roy & Joy, Sarasota, Shawn, Tonie, Wendy,
Willow & Ajax.

Pages — `/about-us/` `/available-parrots/` **`/sign-contract/`** `/shipping/` `/health-guarantee/`
`/reviews/` `/contact-us/` `/payment-policy/` **`/money-order-payment-policy/`** `/privacy-policy/`
`/terms-conditions/` `/returns-refunds-policy/` `/compare/` `/cart/` `/checkout/`.

**Zero blog posts. Zero care guides.** The entire site is transactional.

**Pricing, live:** African Greys — Coco $1,000 · Cory $1,000 · Alex and Lizzy (pair) $1,800 ·
Linda & Lamar (pair) $1,800. Blue Gold Macaws — Collins/Frida/Luna/Shawn $2,100 each · Roy & Joy and
Willow & Ajax (pairs) $3,800.

**Shipping:** *"free shipping on all parrot purchases, both locally and nationwide! Delivery typically
takes 2 days."*

### 4. Visual inventory

The image filenames are the finding:

- `pair-african-grey-for-sale-**UK**-430x430.jpg` and `blue-and-gold-macaw-for-sale-**UK**-430x430.jpg` —
  **UK-targeted filenames on a site advertising a US phone number**
- `WhatsApp-Image-2023-07-14-at-11.02.34-AM.jpeg` — a WhatsApp-forwarded image
- `FB_IMG_1736917829378.jpg` — an image **downloaded from Facebook** (Android FB save convention)
- `cover_83633541_488811241768949_5962704476098570580_n.jpg` and
  `cover_101404900_2048063878659641_1632469669760315216_n.jpg` — **Facebook CDN cover-photo naming**

Every product is badged **"Hot"** while every product is **"Rated 0 out of 5"**. Nine testimonials, all
signed *"Happy Customer"* with a first name and initial. **Zero `application/ld+json`** — no structured
data at all on a 25-product store. WhatsApp appears **10×**; an `sms:+115106865782` deep link is in the
footer.

### 5. Reddit / forum mining

**Zero Reddit mentions found** for "williams african greys".

### 🚩 Trust / CITES flags (Rule 8)

- **No physical address anywhere on the site** — phone `+1 (510) 686-5782` (Oakland/East Bay CA) and email
  only. r/parrots names "no exact address" explicitly as a scam tell (A4 §5).
- A dedicated **`/money-order-payment-policy/`** page. Money orders are irreversible.
- Imagery sourced from **Facebook and WhatsApp**, with **UK** keywords baked into filenames.
- **International delivery** of a CITES Appendix I species; a returns/refunds policy on live birds.

### Correction tested and NOT supported

Afro Birds Farm sells a "Benny" and Williams uses `Benny-African-grey-500x500.jpg`; both also have a
"Lizzy". I tested whether the two operations share an image pool by byte-comparing the files:

```
wag_benny.jpg  md5=bfeae866eb268725ce908e1e2e9dd3ed  41,412 bytes
abf_benny.jpg  md5=0694db4f418b28fb25194bfe7ece509c  32,359 bytes
```

**Different files. The shared-operator hypothesis is not supported by this test** and is not asserted.
Recorded so the next sweep does not re-raise it.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "SSL ERROR / BLOCKED", "Expired SSL certificate", "likely dead/inaccessible site" | **False.** Live on Cloudflare, HTTP 200, valid TLS. The failure was our own resolver sinkholing the domain. |
| "any SEO equity it held is decaying" | 25 live product pages, full policy set, rebuilt Nov 2025 |
| "Threat level: VERY LOW (likely dead)" | Revise to **low-as-rival / flagged-as-exhibit** |

### Key insight

A 25-bird WooCommerce store with **no address, a money-order payment page, Facebook-sourced photography
and UK keywords in its filenames** was written off as an expired certificate. The correction that matters
operationally is procedural: **`access_status: "inaccessible"` was recorded twice from a single transport**,
and one public-resolver check would have overturned it both times.

---

## A4 · Shades of Greys — https://www.shadesofgreys.com

Tier 1 · direct_breeder · registry `access_status: "accessible"`, `states_active: []` · baseline `competitor-shadesOfGreys-2026-05-11.md`

### 🚩 The baseline put this breeder in the wrong state

Baseline: *"No physical address (only state: Georgia detected) … Appears to target Georgia / Southeast
region only … Threat level: VERY LOW — local Georgia seller."*

Measured: the business is **Fifty Shades of African Greys**, **West St. Paul, Minnesota**, tel
**701-212-9733**, `fiftyshadesofafricangreys@gmail.com`. Their own meta description reads: *"We offer
shipping through Delta Airlines if you're not local to **Minnesota**."* There is no Georgia connection.
**MN is one of the canonical 22 states**, and the registry carries `states_active: []`.

### 1. SERP snapshot

Google (Firecrawl, Google-backed), **"african grey parrot breeder"**, top 10:

| # | Result | URL | Type |
|---|---|---|---|
| 1 | African Grey Parrots for Sale — *JC Aviary, TX listed first* | birdbreeders.com/birds/category/african-grey-parrots | Directory |
| 2 | **r/AfricanGrey — "Does anyone know any reputable breeders?"** → *"Check out JC Aviary… they ship all over"* | reddit.com | **Forum** |
| 3 | Gray Breeders Foundation — *"MAP certified… Price: $1500"* | graybreedersfoundation.yolasite.com | Registry Tier 1 |
| 4 | African Grey Parrot Breeding Progress at Our New Breeding Farm | youtube.com | Video |
| 5 | Professional breeding center of African Grey parrots — **Psittacus** | psittacus.com | ES authority |
| 6 | "Does anyone know of any reputable african grey parrot breeders locally?" | facebook.com | Forum |
| 7 | African Grey Baby Parrots (Males/Females) | exoticglobalparrotsfarm.com | Registry Tier 6 |
| 8 | **I SPENT $13k on My African Grey Parrots \| Here's Why** | youtube.com | Video |
| 9 | Congo African Grey Parrot — *Taking Deposits* | kookshop.com (Kookaburra Bird Shop) | **Not in registry** |
| **10** | **Fifty Shades of African Greys \| Parrot and Exotic Bird Breeder** | **shadesofgreys.com** | **In scope** |

Two readings matter. **First: of the six sites in this sweep, only Shades of Greys ranks on the head
breeder term at all.** Second: **half of the top 10 is forum, video or directory** — r/AfricanGrey at #2,
Facebook at #6, YouTube at #4 and #8, BirdBreeders at #1. A breeder page competes for five slots, not ten.

US second-engine: NOT FETCHED.

### 2. Query fan-out — stem `african grey parrot minnesota`

**Google A–Z 6 · Bing A–Z 25 · Google question-mods 14 · union 42 unique · 20 are 6+ words.**
Google's suggest is nearly silent on the state stem while Bing returns 25 — **25 of 42 are Bing-only**,
matching the Georgia-stem asymmetry recorded in the page-5 sweep.

Confirmed state demand: `african grey parrot for sale minnesota` · `african grey parrot minnesota`.

Legal cluster resurfaced on this stem (unowned by anyone in the registry):
`do you need a licence for an african grey parrot` · `do you need a license to own an african grey parrot` ·
`how to register african grey parrots` · `are african grey parrots legal in australia` ·
`is african grey parrot legal in india`

Care/AEO long-tail on the same stem: `can you keep african grey parrots outside` ·
`how long can african grey parrots be left alone` · `do african grey parrots carry diseases` ·
`what not to feed african grey parrots`

### 3. Section / listing-page inventory

`firecrawl_map`: Wix site, small and honest. `/` · **`/about-5` (Pricing)** · `/available-birds` ·
`/shipping` · `/bird-care` · `/category/all-products` · `/about`, `/about-4`, `/about-4-1…4-4` (stubs).

**Published price list — the most valuable single artifact in this sweep:**

| Species | Price |
|---|---|
| **Congo African Grey** | **$7,000** |
| **Timneh African Grey** | **$6,500** |
| African Cape Parrot | $5,000 |
| Blue and Gold Macaw | $6,000 |
| Greenwing Macaw | $6,500 |
| Harlequin Macaw | $6,500 |
| Goffin Cockatoo | $4,500 |
| Umbrella Cockatoo | $6,000 |
| **Moluccan Cockatoo** | **$10,000** |
| Solomon Island Eclectus | $4,000 |
| Golden Conure | $5,500 |

**Health documentation, verbatim from `/available-birds`:** *"All of our birds are DNA sexed and disease
tested against: Avian Borna virus, Pachecos, Chlamydia, PBFD, and Polyoma."* — **the only competitor in
this cohort that documents disease screening at all**, and the panel is broader than CAG's ledger
(Borna and Pacheco's beyond PBFD/Polyoma/psittacosis).

**Shipping, verbatim from `/shipping`:** pickup in Minnesota · *"We will drive up to 200 miles to deliver"* ·
Delta Cargo to any major US airport · **$160 African Greys / $200 macaws and large cockatoos** ·
*"We have transported over 100 of our birds with the help of Delta Cargo."*

**Husbandry, verbatim from `/bird-care`:** 80% Zupreem Natural Pellets + 20% nuts/seed with Higgins
Safflower Gold; fresh vegetable breakfast (garbanzo, lima, peas, carrots, corn, peppers, Bean Cuisine);
*"We allow all of our babies to wean fully fledged/flighted"*, with clipping offered on request.

**Inventory status:** *"All of our babies from 2025 have found their families!"* — sold out, waitlist by email.

### 4. Visual inventory

Wix, photo-led, a handful of images; the 12 shop SKUs are **unedited Wix demo placeholders**
(`/product-page/i-m-a-product-1…11`, price band $7–$130 — merchandise, not birds). No infographics, no
video, no comparison tables. **Schema: `LocalBusiness` + `PostalAddress` + `WebSite`** — the only site of
the six carrying LocalBusiness.

### 5. Reddit / forum mining — the thread that matters

**r/parrots, "African grey scam website??"** (`/comments/1jlf17f/`), **274 points**. OP posts
`eliteafricangreyparrotaviary.com` and asks whether it is real. Retrieved in full via Playwright
(Firecrawl and the `.json` API both refused — see Method).

| Verbatim | Read |
|---|---|
| **TehGuard [248]:** *"Almost all bird shippers are scams and those prices are way too low. 100% a scam"* | **The market's default prior: shipping ⇒ scam.** CAG ships. |
| **TazDingoh [110]:** *"did some reverse image searching and found this which has the same parrot pictures but with different names https://greyparrottreasuresspot.com/ … same reviews and same names too!"* | Buyers **reverse-image-search** listing photos |
| **ActualCake [77]:** *"The birds are all full of kisses and don't bite? That is bs."* | "Never bites" is a tell |
| **kiaraXlove [71]:** *"Between the super low prices and the non refundable 450 reservation fee due before hand yeah 10000 scam"* | Non-refundable deposit is a tell |
| **kiaraXlove [42]:** *"the location is middle of nowhere population 1,200 Michigan **with no exact address**"* | **No address is a tell** — directly indicts A3 |
| **Radiant_Housing_3104 [19]:** *"And every single bird has the same exact description"* | **Duplicate copy is a tell** |
| **GWlordwolf [19]:** *"If you love animals, don't look for the cheapest… **A gray parrot is at least 1500 for me.** And more."* | A buyer names **$1,500** as the credibility floor |
| **StarTurtle333 [5]:** *"The website is 6 to 7 months old. I wouldn't trust it."* | **Domain age** is a trust signal |
| **ultracoque [4]:** *"Greys can cost around $6k… Most breeders also seem to have an Instagram or Facebook page where they document the bab[ies]"* | Social documentation = proof of life |
| **Immediate-Sample9978:** *"ask for a video of the bird. And have them say a specific word or phrase in the video to prove it's not fake or stolen footage. FaceTime is also a thing."* | The **live-video challenge test** |
| **FunCommercial616:** *"I just got scammed by this guy… Video chat with me. Show me the bird. Everything I did I thought it was good but no. My sister lives in Michigan and went to the address and the man there knew nothing about birds."* | **Even video chat was defeated** |
| **moeninite21:** *"$700? Keep looking… We paid $5000."* | |
| **OP, closing the thread:** *"**Look up fifty shades of African greys. That's where I ended up getting mine**"* | **Shades of Greys is the resolution of an African-Grey-scam thread** |

The two domains named in that thread are now **dead** — `eliteafricangreyparrotaviary.com` and
`greyparrottreasuresspot.com` both return **no DNS A record** and `000`. That is the scam lifecycle in
evidence, and it corroborates StarTurtle333's domain-age point.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "only state: Georgia detected… targets Georgia / Southeast region only" | **False. West St. Paul, MINNESOTA.** Ships nationwide via Delta Cargo. |
| "No pricing visible" | Published list: **Congo $7,000, Timneh $6,500**, 11 species |
| "Zero schema markup" | **False.** `LocalBusiness` + `PostalAddress` + `WebSite` |
| "No blog, no about, no shipping, no guarantee, no FAQ, **no form**" | `/shipping`, `/bird-care`, `/about-5` (Pricing) and a working inquiry form all live |
| "No trust documentation… No DNA sexing" | **False.** DNA sexed + Borna/Pacheco's/Chlamydia/PBFD/Polyoma |
| "No CTA visible" | Inquiry form + phone + email + waitlist |
| "Threat level: VERY LOW — local Georgia seller with no content, no SEO foundation" | **The only site of the six ranking top-10 on the head breeder term**, and the only one cited by name as trustworthy on r/parrots |

### Key insight

The most credible competitor in this cohort was written off on a mis-detected state. They sell Congos at
**$7,000 — 2× the top of CAG's $1,500–$3,500 range** — they publish a broader disease panel than we do,
they ship African Greys for **$160** against our $185, and an r/parrots scam thread ends with a buyer
naming them as the safe alternative. **They are sold out for 2025 and run a waitlist**, which is the
opening: Minnesota demand is live in autosuggest, the incumbent has no inventory, and CAG has no MN page.

---

## A5 · African Grey Aviaries — https://www.africangreyaviaries.com

Tier 1 · direct_breeder · registry `access_status: "inactive"` · baseline `competitor-africanGreyAviaries-2026-05-11.md`

### 🚩 FINDING — the domain did not stay expired; it was re-registered as an Indonesian gambling PBN

The baseline recorded *"DOMAIN EXPIRED — Site returns 'Your domain is expired' page… competitor
eliminated… No further analysis needed."* The lapse was real. What followed was not tracked.

`https://www.africangreyaviaries.com/` now returns **HTTP 200** serving **SUSUN4D**, an Indonesian
online-slot/*togel* brand, wearing a **cloned TeePublic storefront** as camouflage.

Verified twice, independently:

| Evidence | Firecrawl | `curl` (browser UA) |
|---|---|---|
| HTTP status | 200 | 200, 290,286 bytes |
| `<title>` | *SUSUN4D: Panduan Slot DANA Withdraw 24 Jam dan Batas Penarikan* | identical |
| occurrences of **"african grey"** | 0 | **0** |
| occurrences of "susun4d" | — | **92** |
| occurrences of "slot" | — | 24 |

- **Googlebot receives the same 200** (confirmed with a Googlebot UA), and the page ships
  `robots: index, follow, nosnippet` — it is *seeking* indexation.
- Hosting: **217.217.253.135, Contabo GmbH (DE)**, Cloudflare NS — not the original host.
- The subdomain **`african.africangreyaviaries.com`** resolves separately (104.21.88.149) and is the
  gambling site's **LOGIN / DAFTAR (register) portal**. The word "african" now labels a casino account page.
- Camouflage layer: `assets.teepublic.com` images, a **BBB accreditation badge**, a **Google Customer
  Reviews 4.5 badge**, and a full TeePublic footer — all impersonating a real US retailer.
- Fake reviews in Indonesian (*Wulan – 23 tahun – Medan*, *Raka Pratama Bandung*, …).
- **A PBN link ring in the footer**, all anchored "susun4d": `apex-bitcoin.com` · `shopivip.com` ·
  `zgordonunlimited.com` · `aflomon.com` · `threetwomarketing.com` · **`handymanfortsmith.com`** ·
  `volarisarena.com` · **`amsdialysis.com`**. A handyman and a dialysis clinic in the same ring — these
  are lapsed business domains harvested into one network.
- Wayback CDX: last genuine captures **2021-11-25** and **2023-07-22** (200 text/html); by **2025-07-10**
  the URL returns **301**. The flip happened between those dates.

**This is the second registry domain found converted into an Indonesian gambling property**, after
`mariettaBirdShop`'s African Grey page in the page-5 sweep. Two independent instances in two consecutive
sweeps is a pattern, not a coincidence: **lapsed African Grey domains in our niche are being bought and
weaponised for their residual link equity.**

### 1–4. SERP / fan-out / sections / visuals

Not applicable as a bird competitor — **0 occurrences of "african grey"** on the live page. Section
inventory is a TeePublic clone (`/t-shirts`, `/hoodie`, `/mug`, `/stickers`…). Visual inventory is a
single repeated asset, `susun4d.png`. Schema: 5 `ld+json` blocks, all serving the gambling storefront.

### 5. Reddit / forum mining

**Zero Reddit mentions found** for "african grey aviaries".

### Corrections to the 2026-05-11 baseline

| Baseline / registry claim | Measured 2026-08-09 |
|---|---|
| "DOMAIN EXPIRED… competitor eliminated… No further analysis needed" | The domain was **re-registered and repurposed**. It is live, indexed, and hostile. |
| `access_status: "inactive"` | Materially wrong and unsafe — should be `compromised_gambling_pbn` |
| "domain may be available for purchase if the brand name is valuable" | It is taken, and it is now a liability, not an asset |
| "Threat level: NONE — competitor eliminated" | **None as a bird rival; non-zero as a link hazard.** Never link to it from any CAG page. |

### Key insight

"Expired" is not a terminal state, and treating it as one left a hostile domain sitting in our registry
marked `inactive` for three months. The operational rule this yields: **a dead competitor needs a
re-check cadence, not a tombstone** — because the failure mode is not that the domain stays dead, it is
that someone else buys the brand our buyers still search for.

---

## A6 · Compound Exotics — https://compoundexotics.com

Tier 1 · direct_breeder · registry `access_status: "accessible"` · baseline `competitor-compoundExotics-2026-05-11.md`

The one site whose baseline largely **held** — and the one that has grown a content layer since.

### 1. SERP snapshot

Google, "african grey parrot breeder", top 10 — **does not appear**. US second-engine: NOT FETCHED.

### 2. Query fan-out

They now target geography, which the baseline said they did not. Measured on-page: an H2 reading
**"Choosing the Right exotic animals for sale in texas"**, plus geo product tags
`/product-tag/ferrets-for-sale-dallas/` and `/product-tag/sugar-gliders-for-sale-in-ny/`. Against the
fan-out, Texas is the strongest state signal measured (`african grey parrot breeders in texas`,
`african grey parrot for sale austin tx`, `african grey parrot for sale houston tx`) — **CAG's home state**.

### 3. Section / listing-page inventory

Live, `modifiedTime` **2026-08-03** — six days before this sweep. WordPress 6.9.5 + WooCommerce 10.7.0 +
Elementor 4.0.8. Homepage H1 still `EXOTIC PETS FOR SALE`; title still
**"Well Trained Exotic Pets For Sale For Sale"** — the duplicated *For Sale* the baseline flagged 15
months ago is unfixed.

**New since the baseline — a blog.** `/posts/` with, among others:
- **`/comprehensive-guide-to-african-grey-parrots-a-complete-overview/`**
- `/comprehensive-guide-to-macaw-parrots-an-in-depth-overview/`
- `/creating-the-perfect-ball-python-habitat-tank-setup-tips/` · `/bearded-dragon-care-basics/` ·
  `/ferret-care/` · `/sphynx-cat-colors/` · `/hedgehog-facts-and-considerations/` · `/raccoon-colors/`

Also new: `/clients-reviews/`, `/how-to-buy/`, a dedicated `/african-grey-parrot-for-sale/` landing page
**and** `/product-category/african-grey-parrot-for-sale/`.

**African Grey inventory: 5 birds** — Mercury (male), Jet (male), Safiya & Penelope (female pair),
Coco (female), Bruno (male). **Live pricing shows deep discounting:**

| Listing | Was | Now |
|---|---|---|
| Jet_male | $800.00 | **$400.00** |
| Safiya_female & Penelope_female | $1,400.00 | **$700.00** |

Homepage price distribution (204 price tokens): $15 · $50 · $150 · $175 · $200 · $250 · $300 · $400 ·
$450 · $500 · $600 · $800. Word count **5,867** (markdown, main content).

### 4. Visual inventory

100+ product images, `/2023/11/` upload vintage on the African Grey assets (`1-Mercury-male-300x300.jpg`
unchanged since the baseline era). No video. No infographics. **WhatsApp CTA present** (2 occurrences).
Schema: `Organization, WebSite, WebPage, BreadcrumbList, ImageObject, SearchAction, ReadAction, EntryPoint,
ListItem` — **still no Product, Offer, LocalBusiness or FAQPage**, exactly as the baseline recorded.

### 5. Reddit / forum mining

**r/ferrets, "Is it a scam"** (`/comments/1hbavbq/`) surfaces with Reddit's own related-search strings
*"Legitimacy of Compound Exotics ferret sellers"* and *"Reviews of compound exotics for pet buying"*.
The brand is being actively legitimacy-checked on Reddit. Thread body: NOT FETCHED — only the search
result and Reddit's derived query strings were retrieved.

### 🚩 Trust / CITES / legal flags (Rule 8)

1. **"get 15% off paying with cryptocurrency"** — a standing discount for irreversible payment on live animals.
2. **Species carried:** Capuchin Monkey · Finger Monkey · Otters · Skunks · Raccoons · Fennec Fox.
   Primates and rabies-vector native wildlife, restricted or banned in most states.
3. **A keyword-stuffed exact-match footer link block to a sister property, `exoticpethomes.com`**, with
   anchors *"african grey parrots for sale"*, *"african grey parrot for sale"*, *"african grey parrot
   sale"*, *"african grey online"*, *"african gray for sale"*, *"african grey sale"* pointing at
   individual bird pages (`bruno_male`, `chaz_male`, `lacey_female`, `coco_female`, `niko_male`).
   `exoticpethomes.com` is **live (HTTP 200, 27 "african grey" mentions) and is NOT in our registry**.
   Hosting differs (Hostinger UK vs Cloudflare), so this is a **link relationship, not shared hosting**.
4. **Phone: the baseline called `+1 (648) 342-3446` an "NJ area code".** 648 is **not** among New Jersey's
   assigned codes (201/551/609/640/732/848/856/862/908/973). A second number, `648-342-5051`, is also
   present. What 648 *is* was not verified — logged in Open Flags rather than guessed.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-09 |
|---|---|
| "Blog: NO" / "Care content: NO" | **False now.** A blog exists, including a full African Grey care guide. |
| "No state geo targeting" | **False now.** Texas H2 + Dallas/NY geo product tags. |
| "Word count: 12,441" | **5,867** by my method (markdown, main content). Different measure, not necessarily a change — recorded with method named rather than treated as a decline. |
| "$400-$500 visible (likely African Grey range)" | AG range now explicit: **$400–$700**, discounted from $800–$1,400. |
| "Phone: +1 (648) 342-3446 (NJ area code)" | 648 is not a New Jersey area code. |
| "WhatsApp: YES — **unique among competitors**" | No longer unique — Williams African Greys uses it 5× more heavily. |
| Schema: "Organization, WebSite, BreadcrumbList, WebPage, ImageObject… no Product/Offer/LocalBusiness/FAQPage" | **Confirmed unchanged.** The baseline holds here. |

### Key insight

Compound Exotics is drifting from a multi-species storefront toward a **content + link operation**: it
added an African Grey care guide, Texas geo-targeting, and an exact-match-anchor footer block feeding a
second domain. The African Grey birds themselves are being **discounted 50%** while a **15% crypto
discount** sits site-wide — so the commerce is softening as the SEO hardens. For CAG the exploitable fact
is that they still ship **zero Product, Offer, LocalBusiness or FAQPage schema** across an entire
priced catalogue.

---

## Part A — cross-cutting

### The credential gap is total

Case-insensitive token counts on **homepage HTML**, all six sites, plus a manual interior-page check on
each (the interior check is what caught the Shades of Greys correction):

| Signal | afroBirds | exoticParrots | williams | shadesOfGreys | compound | africanGreyAviaries |
|---|---|---|---|---|---|---|
| USDA | 0 | 0 | 0 | 0 | 0 | 0 |
| CITES | 0 | 0 | 0 | 0 | 0 | 0 |
| DNA sexing | 0 | 0 | 0 | **yes — `/available-birds`** | 0 | 0 |
| Avian vet (named) | 0 | 0 | 0 | 0 | 0 | 0 |
| PBFD | 0 | 0 | 0 | **yes — `/available-birds`** | 0 | 0 |
| Polyomavirus | 0 | 0 | 0 | **yes — `/available-birds`** | 0 | 0 |
| Physical address | Houston TX + Mississauga ON | LA (mailbox pattern) | **none** | West St. Paul MN | none on homepage | n/a |
| `ld+json` | 1 block | 1 block | **0** | 2 blocks | 1 block | 5 (gambling) |
| LocalBusiness schema | No | No | No | **Yes** | No | No |
| Product / Offer schema | **No** | **No** | **No** | **No** | **No** | n/a |
| FAQPage schema | No | **No** (despite an on-page FAQ) | No | No | No | n/a |

**Not one of the six mentions USDA or CITES anywhere.** One of six documents disease screening. **None of
the six ships Product/Offer schema despite all five commerce sites carrying priced inventory**, and
Exotic Parrots Planet publishes a 4-question FAQ block with no FAQPage markup. CAG's documentation stack
and schema discipline are uncontested across this entire cohort.

### Price landscape measured this run

| Source | Congo | Timneh | Note |
|---|---|---|---|
| **Shades of Greys (MN)** | **$7,000** | **$6,500** | Published list; DNA + 5-disease panel |
| Williams African Greys | $1,000 (single) / $1,800 (pair) | — | No address; money-order policy |
| Afro Birds Farm | $1,400–$1,600 | — | Eggs $175–$600 |
| Exotic Parrots Planet | **$800** (Alpha) / $1,349.99 (Leo) | $1,349.99 (Nala) | Stock/Instagram photos |
| Compound Exotics | **$400** (Jet) / $700 (pair) | — | 50% off; 15% crypto discount |
| r/parrots buyer floor | *"at least 1500"* | — | GWlordwolf, 19 pts |
| r/parrots buyer ceiling | *"around $6k"* / *"We paid $5000"* | — | ultracoque; moeninite21 |

**CAG's $1,500–$3,500 Congo range sits exactly on the buyer-stated credibility floor ($1,500) and well
under the buyer-stated market ($5,000–$6,000).** Everything below $1,500 in this table belongs to a site
carrying at least one fraud flag. That is a defensible, evidence-backed pricing story.

### Page-type gaps

| Page type | afroBirds | exoticParrots | williams | shadesOfGreys | compound | CAG has it? |
|---|---|---|---|---|---|---|
| Comparison pages | **3** | FAQ-level Congo vs Timneh | No | No | No | Yes — defend |
| Care guide | Yes | Yes (in category page) | **No** | Yes (`/bird-care`) | **Yes, new** | Yes |
| Price / cost cluster | **9 posts** | No | No | Published list | No | Partial |
| **Cage / housing silo** | **9 posts** | Partial | No | No | No | **Gap — unclaimed** |
| Location / state pages | 3 posts | No | No | No | TX H2 + geo tags | Partial |
| **Spanish-language content** | **2 posts** | No | No | No | No | **Gap — nobody else either** |
| Shipping page | Yes | No | Yes | **Yes, priced** | No | Yes |
| Health guarantee page | No | Yes | Yes | No | 1-yr, site-wide | Yes |
| Eggs SKU | **Yes, $175–$600** | **Yes, 11 SKUs** | No | No | No | Yes — $95 |
| Waitlist mechanism | No | No | No | **Yes** | No | **Gap** |
| Legal / licence / CITES explainer | No | No | No | No | No | **Open — nobody owns it** |

### Keyword gaps worth CAG pages (exact phrases, from measured fan-out)

| Phrase | Source | Why it matters |
|---|---|---|
| `african grey parrot breeders near me prices` | Bing A–Z, **all three stems** | Persistent, unowned, commercial |
| `african grey parrot breeders near me reviews` | Bing A–Z, **all three stems** | Reputation intent; r/parrots owns the answer today |
| `african grey parrot breeders in texas` | Google A–Z | CAG's home state, breeder intent |
| `african grey parrot for sale houston tx` | Google A–Z (4 Houston variants) | Strongest TX city signal — **and Afro Birds Farm claims a Houston address** |
| `african grey parrot for sale austin tx` | Google A–Z | JC Aviary's city |
| `african grey parrot for sale minnesota` | Google + Bing | Incumbent is **sold out** with a waitlist |
| `do you need a license to own an african grey parrot` | Google q-mods | Zero credible incumbent; CITES App-I authority play |
| `how to register african grey parrots` | Google q-mods | Same cluster, documentation-led |
| `why are african grey parrots so expensive` | Google A–Z | Answers the $400-vs-$7,000 spread |
| `how much is an african grey parrot worth` | Google A–Z | Same |
| `african grey parrot breeder in sc` | Bing A–Z | SC is in the 22; no incumbent found |
| `can you keep african grey parrots outside` | Google q-mods | Care AEO, unowned |
| `how long can african grey parrots be left alone` | Google q-mods | Care AEO, unowned |
| `do african grey parrots carry diseases` | Google q-mods | **Routes straight to our screening ledger** |
| `african grey parrots for rehoming` | Bing A–Z | Adoption-language buyers |

### State coverage from this fan-out (against the canonical 22)

**Signal present for 11:** AZ · FL · MA · MD · MI · MN · NY · OH · SC · TX · WA
**No signal in this fan-out for 11:** CA · CO · GA · IL · IN · MO · NC · NJ · PA · TN · VA

Two honesty notes: (a) this is a **3-stem** fan-out, far narrower than page-5's, so absence here is much
weaker evidence than absence there; (b) the SC hit is `african grey parrot breeder in sc` — my pattern also
caught *"scotland"* and *"scams"*, which are false positives and are excluded.

City-level demand measured: **Houston (4 variants)** · Atlanta · Austin · Miami · Los Angeles · Las Vegas ·
Phoenix · San Diego.

---

# Part B: Correction to the Page-5 Sweep (`competitor-sweep-page5-2026-08-09.md`)

**The shared-IP finding in the page-5 sweep is a measurement artifact and must be withdrawn.**

Page 5 concluded, and the registry now records in `exoticGlobalParrotsFarm.notes`:

> *"DNS: exoticglobalparrotsfarm.com resolves to 81.99.162.48 (lang-sspiprxy.network.virginmedia.net — a
> Virgin Media RESIDENTIAL broadband line in London GB), shared with four other African Grey storefronts:
> sherrybirds.org, paradisebirdsfarmaviary.com, exoticparrotfarms.com, parrotsfarm.com. **That is one
> operator running a domain network, not five independent breeders.**"*

`81.99.162.48` is **not a residential broadband line and not a host**. It is Virgin Media's **Web Safe /
VirusSafe block-page sinkhole** — `lang-sspiprxy` = *security service proxy*; port 80 returns
`302 → websafe.virginmedia.com/virussafe-blocked.html`. It was returned because **this machine's resolver
is Virgin Media UK** (`194.168.4.100`), not because the domains are co-hosted.

Against public resolvers the five domains resolve to **five unrelated addresses**:

| Domain | Real A record (8.8.8.8 / 1.1.1.1 / 9.9.9.9) | Owner (whois) |
|---|---|---|
| exoticglobalparrotsfarm.com | 66.45.23.70 | **OrangeHost** |
| sherrybirds.org | 89.116.109.44 / 2.57.91.131 / 91.108.103.63 (rotating) | Hostinger / Bite Lietuva |
| paradisebirdsfarmaviary.com | 195.200.9.122 / 89.116.109.158 / 185.77.97.180 (rotating) | Hostinger |
| exoticparrotfarms.com | 195.200.9.203 / 2.57.91.247 / 91.108.103.154 (rotating) | Hostinger |
| parrotsfarm.com | 213.130.145.185 | Hostinger FR |

**What survives:** four of the five sit in **Hostinger** address space with rotating multi-range
round-robin. Hostinger is a mass shared host used by millions, so this is **weak** evidence of common
ownership and nothing like the "one residential line" claim. It should not be cited as proof of a network.

**What is new and genuinely stronger:** Virgin Media's Web Safe filter **selectively classifies seven
parrot domains as harmful** — `exoticparrotsplanet.com`, `williamsafricangreys.com`,
`exoticglobalparrotsfarm.com`, `sherrybirds.org`, `paradisebirdsfarmaviary.com`, `exoticparrotfarms.com`,
`parrotsfarm.com` — while passing `congoafricangreys.com`, `jcaviary.com`, `parrotstars.com`,
`birdsbyjoe.com`, `shadesofgreys.com`, `compoundexotics.com` and `afrobirdsfarm.com` untouched. **A
third-party security vendor independently flagging seven domains is better evidence than a shared IP ever
was** — and it is correctly attributed. It is a UK consumer filter, not a legal finding, and should be
described as exactly that.

**Net effect on `exoticGlobalParrotsFarm`:** its tier-6 re-classification rested on three legs — identical
"1 year 3 months old" ages, add-to-cart worldwide delivery of an App-I species, and the DNS claim. The
first two stand on their own. **The third must be struck from the registry note.**

---

# Part C: Proposals (NOT applied — for breeder approval)

`data/competitors.json` was **not modified**, per the brief. In priority order:

1. **Fix `afroBirdsFarm.url`** → `https://afrobirdsfarm.com` (drop `www.`), set
   `access_status: "accessible"`, `priority: "high"`. *The current value does not resolve; the apex does.*
2. **Strike the DNS sentence from `exoticGlobalParrotsFarm.notes`** (Part B). Keep the tier-6 rating —
   the age-identity and worldwide-delivery evidence is unaffected. Replace with the Web Safe finding,
   correctly attributed.
3. **Set `africanGreyAviaries.access_status`** → `"compromised_gambling_pbn"`, `threat_level: "none"`,
   `priority: "low"`, with a note recording SUSUN4D, the Contabo host, the `african.` login subdomain and
   the 8-domain footer ring. **Never link to it from any CAG page.**
4. **Set `williamsAfricanGreys.access_status`** → `"accessible"`. The "SSL error" was our resolver.
   Add the no-address / money-order / Facebook-sourced-imagery flags.
5. **Set `shadesOfGreys.states_active`** → `["MN"]`, correct the display name to **"Fifty Shades of
   African Greys"**, raise `priority` to `high`. This is the only in-scope site ranking on the head term.
6. **Add `exoticParrotsPlanet` fraud flags** (Western Union / Bitcoin, LA address vs 915 phone, "since
   1994" on a 2025 site, $800 Congo) and mark it as scam-page exhibit material rather than a ranking rival.
7. **Update `last_analyzed: "2026-08-09"`** for all six ids in scope.
8. **Candidate additions, breeder approval required** — all found ranking or linked this run, none in the
   registry today:
   - `exoticpethomes.com` — sister property of Compound Exotics, receives its exact-match AG anchors, live, 27 AG mentions
   - `kookshop.com` (Kookaburra Bird Shop) — Google **#9** for "african grey parrot breeder", "Congo African Grey — Taking Deposits"
   - `psittacus.com` — Google **#5**, professional Congo breeding centre, the strongest E-E-A-T entity on that SERP
9. **Do NOT add** `eliteafricangreyparrotaviary.com` or `greyparrottreasuresspot.com` — both named as scams
   in r/parrots and both now **dead (no DNS A record)**. Cite them as *documented, expired* examples on
   `/how-to-avoid-african-grey-parrot-scams/`, which is stronger than citing a live site we might send traffic to.

---

## Open Flags

**Open question for the breeder (one, narrow):**
Shades of Greys (Fifty Shades of African Greys, West St. Paul MN) prices **Congo at $7,000 and Timneh at
$6,500**, documents DNA sexing plus a five-disease panel, and is the name an r/parrots scam thread lands
on — while CAG publishes **$1,500–$3,500**. Should the Minnesota location page and the price pages be
built to (a) **hold our range and attack the gap** — "$1,500–$3,500 with the same documentation the
$7,000 breeders publish" — or (b) **reframe our range as an entry tier** beneath a premium anchor? The
answer changes the price framing on every for-sale page, not just the MN one, so I have not assumed it.
Everything else in this sweep is complete and unblocked.

**NOT FETCHED list, with barriers named:**

| Item | Barrier |
|---|---|
| **US second-engine SERP (Bing / DuckDuckGo), all queries** | Local egress is a UK consumer line, so DDG/Bing return a **UK-localised** SERP (purefeatheraviary.co.uk, pets4homes.co.uk, `ad_provider=bingv7aa` on ebay.co.uk). Correctly-functioning localisation, not a bot block — but not the US picture. |
| Google PAA expanded 3 levels | Not attempted this run; Google-side automation budget was spent on the A–Z autosuggest sweep for 3 stems. |
| `firecrawl_map` for `exoticparrotsplanet.com` | Not run. Product counts were read from the site's own category widget instead, which is stronger evidence than a map sample; URL-space breadth is therefore unmeasured. |
| `firecrawl_map` for `africangreyaviaries.com` | Not run — the domain serves no bird content (0 occurrences of "african grey"), so a URL inventory has no competitive value. |
| Reddit thread bodies via Firecrawl | `firecrawl_scrape` returns *"We apologize… we do not support this site"* for reddit.com. Playwright + `old.reddit.com` succeeded and was used instead. |
| Reddit `.json` API | HTTP 403 bot challenge from this IP. |
| r/ferrets thread `1hbavbq` body ("Is it a scam" — Compound Exotics) | Only the search result and Reddit's derived query strings were retrieved; the comment bodies were not fetched. |
| Brand-query SERP position for the 6 ids | Not queried this run — only the shared head term "african grey parrot breeder" was run against Google. |
| Spanish-language query volume for Afro Birds Farm's 2 Spanish posts | `suggestqueries` was run English-default (`hl` unset); Spanish-side demand is unmeasured. |
| What NANP assignment `648` actually is (Compound Exotics phone) | Verified only that 648 is **not** among New Jersey's assigned codes, which is what the baseline claimed. The positive identification was not fetched and is not guessed. |
| `afrobirdsfarm.com` total indexed page count | `firecrawl_map` samples the URL space; the 47 content posts + 10 bird pages are an enumerated floor, not a certified total. |
| Compound Exotics homepage word count reconciliation | Baseline said 12,441; I measured 5,867 (markdown, main content). Different methods — the discrepancy is **not** resolved and is not reported as a decline. |

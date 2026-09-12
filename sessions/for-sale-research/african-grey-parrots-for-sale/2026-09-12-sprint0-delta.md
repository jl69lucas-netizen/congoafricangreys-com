# Sprint 0 delta — `/african-grey-parrots-for-sale/` (the cluster hub)

**Date:** 2026-09-12 · **Plan:** `docs/superpowers/plans/2026-09-12-page-board-system.md` Task 11 Step 1, on top of
`docs/superpowers/plans/2026-08-10-buy-shipping-and-near-me-for-sale-pages.md` §0f–§0g and Task 13.
**Role after the build (§0g):** the cluster **HUB** — national inventory, `AggregateOffer`, a link to every spoke.
**Sheds** the state/metro grid (the near-me router owns it since 2026-09-12) and **absorbs** the singular
`/african-grey-parrot-for-sale/` by 301.

> **Delta, not a full Sprint 0.** The buy and near-me Sprint 0s (2026-08-10) and the three competitor sweeps
> (2026-08-09) are reused, not re-fetched. This document records only what the hub's own head terms return today.

---

## 1 · Method and barriers

| What | How | Fetched | Caveat |
|---|---|---|---|
| Top 10 organic, two head terms | Firecrawl Search, US | 2026-09-12 | H1/H2s extracted per result page (JSON extraction) |
| Live SERP features | `firecrawl_scrape` on `google.com/search`, stealth, `maxAge:0`, `pws=0` | 2026-09-12 | Geolocated to **Baltimore, MD** (proxy IP), not Midland TX |
| PAA level 1 | Read from the live SERP | 2026-09-12 | Questions captured; every answer rendered *"An error has occurred"* |
| PAA levels 2–3 | DataForSEO `serp_organic_live_advanced`, click depth 3 | — | **NOT FETCHED — HTTP 403 from the connector** |
| Autosuggest, 2 stems | `suggestqueries.google.com`, `gl=us&hl=en` | 2026-09-12 | |
| GSC bucket | `docs/research/for-sale-keywords-2026-07.md:460` | 2026-07-16 | regex-assigned, draft (§0f) |
| Competitor depth | Reused from sweeps 1–3 (2026-08-09) | 2026-08-09 | Not re-fetched |

**`NOT FETCHED`:** PAA answer bodies (Google errored) · PAA levels 2–3 (DataForSEO 403) · Bing query-level data (no
export carries query rows) · the SERP as a Midland searcher would see it (proxy geolocation not controllable).

---

## 2 · The SERP — `african grey parrots for sale` · Fetched: 2026-09-12

About 163 results · **local pack present** (three bird shops, the same three the near-me Sprint 0 found from a
Maryland IP: Maryland Exotic Birds, TC Feathers Aviary, American Bird Company) · **AI Overview: "not available"**,
but an **AI Mode answer** rendered in its place · PAA present · Shopping tab present, no product carousel inline.

### 2a · Top 10 organic with H1 and H2s (Firecrawl Search, US) · Fetched: 2026-09-12

| # | Page | Page type | H1 | H2s (document order) |
|---|---|---|---|---|
| 1 | birdbreeders.com `/birds/category/african-grey-parrots` | classified **category** | African Grey Parrots for Sale | Find Local Breeders · Currently Available in · Support · Local Searches · Join Our Community |
| 2 | graybreedersfoundation.yolasite.com `/Order-Now.php` | free-host **"order now"** page, $1,500 | Gray Breeders Foundation | ADOPT NOW!! · About Us · Available NOW!! · Order Now |
| 3 | parrotsoftheworld.com `/parrots` | Long Island **pet shop** | Parrots & Birds | Largest Selections of Parrots for Sale · African Grey Parrots · Amazon · Macaw · Cockatoos · Lovebirds · Contact Us · About |
| 4 | birdsnow.com `/africangreyparrot.htm` | classified **category**, national | African Gray Parrots | About African Grey Parrots · Browse More African Grey Parrots · Featured Birds |
| 5 | theavianexchange.com `/african-greys-for-sale/texas/houston` | marketplace **geo** page | Available African Grey Parrots in Houston, Texas | More African Greys nearby · Other birds in Houston, Texas |
| 6 | facebook.com — Aviary Bird Shop post | social post, "$500 for one" | — | — |
| 7 | exoticparrotpetstore.com `/product-category/african-grey-parrot/` | **store category**, crossed-out prices ($4,500 → $2,500) | AFRICAN GREY PARROT | Buy Baby African Grey Parrot Online · Buy Baby Timneh … · Buy Congo … Online · six named birds "For Sale" |
| 8 | anasparrots.com | shop homepage, Congo baby $7,500 | Ana's Parrots & Supplies | From Our Clients · Featured Birds · Our Birds · Customer Service · Questions? |
| 9 | facebook.com group "African Grey Parrots For Sale" | social group | — | — |
| 10 | youtube.com "I SPENT $13k on My African Grey Parrots" | video | (title) | Description · Transcript |

**Not one of the ten is a breeder's own inventory page with documented birds.** Three are classified/marketplace
category pages, three are shops, two are Facebook, one is a free-host order page, one is a video.

### 2b · `african greys for sale` — top 10 · Fetched: 2026-09-12

Seven of ten overlap with 2a. The three new entries: **birdsbyjoe.com** (NJ shop homepage, #3),
**birdsnow.com `/africangreyparrotflorida.htm`** (state page, #6) and **mosbirds.com `/product-category/african-greys/`**
(#9 — a California breeder: *"hand-raised … DNA-sexed, health-tested … Ships to all 50 states"*, with a
*"3-day returns"* snippet). Mosbirds is the only ranking page shaped like ours; it ranks ninth on the shorter term
and not at all on the longer one.

### 2c · What the category pages do that a listing page does not

The three category pages that rank (BirdBreeders #1, BirdsNow #4, Avian Exchange #5) all carry the **same two H2
jobs**: *what is available* and *where* (Find Local Breeders · Currently Available in · More African Greys nearby ·
Browse More). They are hubs over other people's listings. Our hub is a hub over our own spokes, which is the
structural difference to exploit: every H2 on ours answers a buying question the category pages cannot, because
they do not own the birds.

### 2d · Prices visible on this one SERP

$500 (Facebook post) · $1,500 (Gray Breeders Foundation) · $2,500 crossed out from $4,500 (Exotic Parrot Pet Store)
· $7,500 Congo baby (Ana's) · **AI Mode: "$2,750 and $7,000 … from a reputable breeder"**, with its own note:
*"Be highly suspicious of online classifieds offering African Greys for under $1,000."*

Our floor is $1,500 (`data/price-matrix.json`). **Google's AI answer now places a $1,500 Congo below its
"reputable breeder" band** — the same artifact recorded in `reference_aio_calls_our_price_fraudulent`. The hub's
price section has to explain the floor, not just state it.

### 2e · PAA level 1 · Fetched: 2026-09-12 (answers NOT FETCHED)

How much does an African Grey Parrot cost? · **What is the 3 3 3 rule for parrots?** · How much does a pair of
African grey parrots cost? · How much does a baby African Grey parrot typically cost?

The 3-3-3 question has now appeared on **four of four** measured for-sale head terms across three Sprint 0s. The
pair-cost question is new to this term and maps to `/congo-african-grey-parrot-pair-for-sale/`.

### 2f · People also search for · Fetched: 2026-09-12

near baltimore, md · near maryland · **African Grey for sale $200** · parrot lifespan · Parrot for sale near me ·
**for sale by owner** · rescue near me · for adoption

Two of eight are geo (the router's job); two are the sub-$1,000 searcher (`$200`, `by owner`); two are
adoption/rescue (`/african-grey-adoption/` exists); one is lifespan (`/african-grey-parrot-lifespan/` exists).

---

## 3 · Query universe

### 3a · Autosuggest · Fetched: 2026-09-12

`african grey parrots for sale ` → near me · **in florida** · uk · western cape · scotland · manchester price ·
ireland · gumtree · in durban · **photos**
`african greys for sale ` → near me · uk · **or adoption** · durban · (self) · **cheap** · florida ·
**cheap near me** · scotland · **$200**

**Twelve of twenty are non-US** (UK, South Africa, Ireland). The US-relevant residue is: near me (router), florida
(location page exists), photos, or adoption, cheap / cheap near me / $200. The `cheap` and `$200` modifiers are the
same population the AI Mode answer warns about; the hub meets them with the price floor and the scam page link.

### 3b · The GSC bucket for this slug (Google, 16 months to 2026-07-16 — regex-assigned, draft)

29 queries · 1,370 impressions · 5 clicks. Head term `african grey parrots for sale` 533 impr / 4 clicks / pos 73.7;
`african greys for sale` 216 / 1 / 60.2; `african grey parrots for sale in usa` 66 / 0 / **28.2** (the best
position in the bucket, and a national modifier); `… texas` 154 / 0 / 78.5.

Page-level rows (§0f of the 2026-08-10 plan): 0 clicks on 13 impressions in window 1, absent in window 2. There is
no traffic to protect; the rebuild is judged on structure.

---

## 4 · What the hub can own

1. **A breeder's national inventory page, documented.** Nobody in the top 10 on either term is a breeder with
   named, priced, health-tested birds except Mosbirds at #9 on the shorter term. The category pages rank by
   aggregating other people's listings; ours aggregates our own spokes.
2. **The price floor, explained.** The SERP shows $500–$7,500 on one screen and Google's own AI answer calls
   anything under $1,000 suspect while placing $1,500 below its band. A section that shows *why* $1,500 is a real
   captive-bred price is unopposed.
3. **`in usa` at position 28.** The only national modifier in the bucket, and the bucket's best position. The
   hub is the national page; the router is the geographic one.
4. **The pair question.** New on this term's PAA; the pair page exists and the hub links it.
5. **3-3-3.** Four of four head terms; still uncovered on the site. Belongs in this FAQ and the router's.

---

## 5 · Spoke coverage in the ranking set

Of our for-sale spokes, the ten ranking pages carry an equivalent of: **Congo / Timneh variant listing** (Exotic
Parrot Pet Store H2s, BirdBreeders category), **geo listing** (Avian Exchange Houston, BirdsNow Florida),
**baby** (Exotic Parrot Pet Store, Aviary Bird Shop). None carries an equivalent of: health guarantee, DNA-tested,
hand-raised, eggs, adoption cost, breeding pair, buy-with-shipping, or a documentation page. Those eight spokes are
linked from the hub with no competing equivalent on the SERP.

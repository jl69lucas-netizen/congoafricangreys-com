# Sprint 0 — Intel · `/congo-african-grey-parrot-pair-for-sale/`

**Date:** 2026-07-30 · **Page 9 of 22**, Cluster 3 opener · **Mode:** rebuild from an 8 KB stub
**Brief:** `sessions/2026-07-25-for-sale-page-master-brief.md` · **Gate:** [REVIEW] — breeder signs off before Sprint 0.5

---

## 0 · Coverage — what was fetched, and what was not

Per the standing rule, **un-fetched is written NOT FETCHED and never invented.**

| Source | Status | Detail |
|---|---|---|
| Google SERP | ✅ **FETCHED** | 2 SERPs × 12 results, US location |
| GSC — real page attribution | ✅ **FETCHED** | `GSC-extracted/Pages.csv` + `Queries.csv`, 16 months to 2026-07-16 |
| Direct competitor pages | ✅ **FETCHED** | denimixanipetsparadise (full scrape), birdsnow bonded-pair index (full scrape, 18 live ads) |
| Reddit | ✅ **FETCHED (snippets)** | 10 threads across r/parrots + r/AfricanGrey — titles and top-comment snippets. **Full thread bodies not scraped** |
| Community / expert Q&A | ✅ **FETCHED (snippets)** | Lafeber, Quora, backyardchickens, northernparrots, Tony Silva / parrotsdailynews |
| **Bing** | ❌ **NOT FETCHED** | Still no query export. The supplied CSV is a date-series traffic chart with zero query rows. **Open flag #9, now blocking a second cluster page** |
| **Instagram** | ❌ **NOT FETCHED** | |
| **YouTube** | ⚠️ **PARTIAL** | 2 videos surfaced in SERP; neither analysed |
| **Facebook** | ⚠️ **PARTIAL** | 2 group posts surfaced via search snippet only |
| **30-competitor registry sweep** | ❌ **NOT RUN** | `@cag-competitor-intel --all` not executed this session |
| **LLM keyword intel** | ❌ **NOT RUN** | Open flag #10 — still unmeasured on every cluster page |

**Sprint 0 is therefore substantially but not fully complete.** Everything below is measured. §12 lists what a full sweep would still add, and my judgement is that none of it changes the recommended angle — the angle is decided by data already in hand.

---

## 1 · 🔴 The demand correction — the mining doc was wrong about this page

`docs/research/for-sale-keywords-2026-07.md` credits this slug with **10 queries and 497 impressions**. Its own header warns the bucketing is *"regex-based, first-match; treat as draft."* It is a draft, and here it is wrong.

**Real GSC page attribution** (`Pages.csv`):

| URL | Clicks | Impr | CTR | Pos |
|---|---|---|---|---|
| `/product/african-grey-breeding-pair-for-sale-nearby/` | **22** | **668** | 3.29% | 10.11 |
| `/product/congo-african-grey-parrot-pair-for-sale/` | 4 | 297 | 1.35% | 31.27 |
| `/african-grey-breeding-pair-for-sale-nearby/` | 2 | 75 | 2.67% | 15.36 |
| **`/congo-african-grey-parrot-pair-for-sale/`** ← our target | **1** | **8** | 12.5% | **5.62** |
| `/african-grey-breeding-pair-for-sale/` | 1 | 7 | 14.29% | 13.71 |

The target page has **8 impressions, not 497.** The regex assigned every `*pair*` query to it.

**Redirects are correct and verified live (2026-07-30).** All three legacy URLs 301 cleanly:

- `/product/african-grey-breeding-pair-for-sale-nearby/` → `/african-grey-breeding-pair-for-sale/` ✅
- `/product/congo-african-grey-parrot-pair-for-sale/` → `/congo-african-grey-parrot-pair-for-sale/` ✅
- `/african-grey-breeding-pair-for-sale-nearby/` → `/african-grey-breeding-pair-for-sale/` ✅

So equity consolidates properly; GSC simply still reports under the old URLs across a 16-month window. **Nothing to fix — this was checked rather than assumed.**

### Consolidated real demand, post-redirect

| Destination | Impr | Clicks | Best pos |
|---|---|---|---|
| `/african-grey-breeding-pair-for-sale/` (sibling stub) | **750** | 25 | ~10.1 |
| **`/congo-african-grey-parrot-pair-for-sale/` (our target)** | **305** | 5 | 5.62 / 31.27 |

---

## 2 · 🔴 The cannibalization decision — resolve before the Sprint 1 outline

Query-level demand splits cleanly into two clusters that must not share a page.

**Cluster A — BREEDING pair (~475 impressions, 19 clicks, already top-10)**

| Query | Impr | Pos |
|---|---|---|
| breeding pair of african greys for sale | 169 | 9.01 |
| african grey breeding pair for sale | 156 | 7.14 |
| breeding pair african greys for sale | 62 | 5.21 |
| african grey parrot breeding pair for sale | 39 | 8.69 |
| african grey breeding pair | 26 | 20.54 |
| breeding african grey parrots for sale | 16 | 32.62 |
| breeding pair of african grey parrots for sale | 3 | **2.33** |
| african grey breeding pairs for sale | 2 | **2.5** |

**Cluster B — COMPANION / generic pair (40 impressions, 0 clicks)**

| Query | Impr | Pos |
|---|---|---|
| african grey pair for sale | 29 | 16.76 |
| african grey pair | 7 | 66.0 |
| grey pair | 4 | 30.75 |

**Cluster C — male-and-female informational (~35 impressions).** Already owned by `/male-vs-female-african-grey-parrots-for-sale/` in the comparison cluster. **Hands off — do not target.**

### Two facts that decide the page

1. **The exact head term of this page's own slug has zero recorded demand.** In 16 months, not one impression on any query containing both "congo" and "pair". Same situation as DNA-Tested, and it needs the same kind of answer.
2. **Cluster A outweighs Cluster B roughly 12 : 1, and belongs to the sibling.** `/african-grey-breeding-pair-for-sale/` is a 4 KB stub sitting on 750 impressions of inherited equity at position ~10.

> ### ▣ DECISION REQUIRED — intent split
> **Recommendation: this page owns Cluster B (companion pairs) and deliberately does NOT chase Cluster A.**
> **Why:** the breeding-pair queries already rank at 2.3–9.0 through a redirect into the sibling slug. Pointing a second, stronger page at the same eight queries would split that equity and put two of our own URLs in competition — the exact failure the cannibalization guard exists to prevent. The sibling is one page away in the build queue and inherits the demand cleanly.
> **Trade-off, stated plainly:** Cluster B is small — 40 impressions and zero clicks. Ranking it perfectly wins very little direct traffic. The page has to earn its keep on **informational demand** (§4) and on **conversion**, not on its head term. That is a real cost and the breeder should weigh it.
> **The alternative I rejected:** merge both intents here and 301 the breeding-pair slug into it. It would concentrate 1,055 impressions on one URL. I rejected it because the two buyers are genuinely different people — one wants a companion, one wants breeding stock at $3,000 — and one page cannot serve both without the honest advice in §4 being undercut by a breeding-stock sales pitch.
> Breeder decision: `[ ___ ]`

---

## 3 · SERP snapshot

### "congo african grey parrot pair for sale" — top 12, US

| # | Domain | Type | Note |
|---|---|---|---|
| 1 | birdbreeders.com | Marketplace | Prices $400–$8,500, "Each" on pairs |
| 2 | graybreedersfoundation.yolasite.com | **Scam-pattern** | Free Yola site builder, flat $1,500 |
| 3 | facebook.com group | Social | Athens AL, "pick up in person, no shipping" |
| 4 | mybabyparrot.com | Breeder | Baby, not pair |
| 5 | birdsnow.com (Texas) | Classified | |
| 6 | birdbreeders.com category | Marketplace | |
| 7 | birdsbyjoe.com | Breeder | |
| 8 | facebook.com | Social | Exotic Bird Shop, 3 Congos |
| 9 | **denimixanipetsparadise.com** | **Direct competitor** | Exact-match pair product page, $3,300 |
| 10 | birdsbyjoe.com | Duplicate | |
| 11 | exoticparrotsplanet.com | **Scam-pattern** | Congo at **$850** — far below any real floor |
| 12 | theavianexchange.com | Aggregator | "Screened breeders" |

### "african grey breeding pair for sale" — top 12, US

| # | Domain | Note |
|---|---|---|
| 1 | **exoticglobalparrotsfarm.com** | "Breeding pair … **1 year 3 months old**" — see §5 |
| 2 | birdbreeders.com | |
| 3 | **birdsnow.com/bondedpairafricangreyparrot.htm** | Dedicated bonded-pair index, 18 live ads |
| 4 | graybreedersfoundation.yolasite.com | |
| 5 | buyafricangreyparrots.com | USDA-licensed FL breeder — a legitimate rival |
| 6 | facebook.com | |
| 7 | theavianexchange.com (Seattle) | |
| 8 | denimixanipetsparadise.com | Ranks for **both** queries |
| 9 | youtube.com | "I SPENT $13k on My African Grey Parrots" |
| 10 | hookbillsforsale.com | |
| 11 | midnightparrotplace.com | |
| 12 | handrearedparrots.com | |

**congoafricangreys.com appears in neither top 12.** Consistent with 8 impressions.

**Structural read:** no result on either SERP is a genuine *decision* page. Every one is either a product listing, a classified index, or a social post. **Nobody is answering the question the buyer is actually asking.** That is the gap.

---

## 4 · 🟢 The community intelligence — this is the angle

Ten Reddit threads and the expert Q&A converge on one message, and it is the opposite of what the market sells.

| Source | Verbatim snippet |
|---|---|
| r/parrots — *Two African Grey Parrots* | "Buying 2 birds at the same time may result in the birds staying with each other and ignoring you." |
| r/parrots — *[HELP] I adopted 2 African Grey* | "Greys are RIDICULOUSLY smart. They'll usually bond with each other, and have no use for you or your family" |
| r/parrots — *Wanting to get my 14 yr old birb a companion* | "I would say it's not a great idea. Greys in general … aren't companion birds that need a buddy once they're used to being [with people]" |
| r/AfricanGrey — *Adding a Congo to my flock* | "better to have a different species in the next cage over. They can become friends and not mates" |
| r/AfricanGrey — *does it need another AG for company?* | Buyer's stated reasoning: fear of loneliness, plus "they're pretty expensive" |
| Lafeber (authority) | "There is no way to predict if they will get along or bond as a breeding pair. All you can do is introduce them and see what happens." |
| backyardchickens | "They are normally not sexually mature till they are 5 yrs old" |

**The real question in this space is not "where do I buy a pair." It is: *if I buy two, will they still love me?*** Every commercial result on both SERPs ignores it, because the honest answer costs a sale.

**Five buyer intents nobody on page one serves:**

1. Will two greys bond to each other and ignore me? *(the dominant fear)*
2. Am I buying a pair for the right reason — or out of guilt about leaving one bird alone?
3. What is the difference between a bonded pair, a proven breeding pair, and two singles bought together?
4. Can I introduce two greys myself, and how long does it take?
5. At what age can a pair actually breed? *(the fact the market gets wrong)*

---

## 5 · Competitor teardown

### denimixanipetsparadise.com — "Congo African Grey Pair", $3,300 · the direct rival

**Content it covers:** Why Choose Congo AGs (5 numbered traits) · About the Pair (species / sex / age / health / socialization) · Worldwide Delivery + Export Docs · Caring for Congo AGs (diet, housing, socialization, vet) · Why Buy From Us · How to Purchase (4 steps).

**Verifiable defects — every one usable as counter-positioning:**

| Claim on the page | Why it fails |
|---|---|
| "1-4 Day Int'l Fast Shipping", "FREE Int'l Home Delivery on orders over $199" | **CITES Appendix I export/import permits cannot be issued in 1–4 days.** Both exporting and importing countries must issue permits |
| "Add to cart" · "Add to wishlist" for a live Appendix-I pair | No application, no screening, no buyer vetting |
| "Easy Return — if the product arrived damage" | A live bird as a returnable product |
| "We are Located In EUROPE & USA" | No address anywhere on the page |
| "Both parrots are 3 years old" + sold as a **bonded pair** to "first-time bird owner[s]" | The precise mistake the r/parrots consensus warns against |
| Related: "Scarlet Macaw baby pair — **5 years health guarantee**, free shipping and free food" | An unenforceable warranty; ours is a written **72-hour** window plus 24-hour arrival |
| "Red factor African Grey parrot **$950** (was $2,200)" | Discounting live birds like stock |
| "10881 reviews" · product rating 4.90 · **store rating 0.00** · **0 reviews on this product** | Internally contradictory |
| `generator: WordPress 7.0.2` | No such WordPress version exists |
| "Don't copy text!" | Anti-copy JS — permanently banned in our own DESIGN.md |

**What it does NOT have, and we will:** named birds · a named breeder · a USDA licence number · DNA certificates · real reviews with photos · any acknowledgement that a pair might be the wrong choice.

### exoticglobalparrotsfarm.com — position 1 on the breeding-pair query

Advertises a **"breeding pair … 1 year 3 months old"** at $2,500. African Greys are not sexually mature until roughly 3–5 years. **A 15-month-old pair cannot be a breeding pair.** The #1 result on the money query is selling a biological impossibility, and correcting it is free authority.

### birdsnow.com — the real market, and a pricing shock

18 live bonded-pair ads. Actual asks:

| Listing | Age | Documentation | Price |
|---|---|---|---|
| Congo pair, Gwynnoak MD | ~8 yrs, bonded, semi-tame | none stated | **$6,500** |
| Landis & Foxxy, Stone Mountain GA | adult, male ~11 yrs | **DNA tested** | **$8,000** |
| Congo pair, Evanston IL | adult, bonded | **recently DNA sexed** | **$6,500** |
| Madelyn, South Plainfield NJ | M 20 / F 15 | *"Can't find paper work"* | SOLD |
| Congo pair, Lyons IN | adult | "a few clutches (usually 3 eggs)" | SOLD |
| Timneh proven pair, Hutto TX | adult | "2 clutches each year of 2–3 eggs" | SOLD |

> ### 🔴 PRICING FLAG FOR THE BREEDER
> **The real US market for a documented adult Congo pair is $6,500–$8,000.** Our breeding pair is $3,000 and Jins & Jeni $3,500 — **less than half the market.**
> This is not a recommendation to raise prices; it is a finding the page must handle. Two live options:
> **(a) Publish the comparison** — "documented pairs sell for $6,500–$8,000; ours is $3,500 because we bred them ourselves and skip the middleman." Turns the gap into the strongest value proof on the page.
> **(b) Revisit pricing.** Out of scope here, breeder's call.
> **Trade-off on (a):** naming a $6,500–$8,000 market rate anchors buyers high and could make $3,500 read as *suspiciously* cheap on a page whose neighbours warn that below-floor pricing is a scam signal. It must be paired with the reason for the gap, never stated bare.
> Breeder direction: `[ ___ ]`

**Also note:** the NJ listing's *"Can't find paper work"* is the market's weak point in six words. Documentation is our moat, and here is a competitor listing admitting the gap.

---

## 6 · Keyword universe (real numbers only)

**Primary:** `congo african grey parrot pair for sale` — slug head term, **0 recorded impressions**. Retained for slug/title consistency; it is not the traffic engine.

**Secondary — Cluster B, ours to own:** african grey pair for sale (29) · african grey pair (7) · grey pair (4) · congo african grey pair · bonded pair african grey · pair of african grey parrots for sale.

**Do NOT target — Cluster A, sibling's:** every `breeding pair` variant (§2).
**Do NOT target — Cluster C, comparison cluster's:** every `male and female` / `difference between` variant.

**Informational long-tail — where this page actually wins.** No GSC volume recorded on our property, so these come from Reddit/Quora/expert demand, marked as such:

- will two african greys bond with each other and ignore me
- should I get a second african grey parrot
- do african greys get lonely alone
- how to introduce two african grey parrots
- bonded pair vs breeding pair african grey
- at what age can african greys breed
- can you keep two african greys in the same cage
- is it better to have one or two african greys

**Transactional:** reserve a pair · deposit · available pair · pair price · ships nationwide.
**Branded:** C.A.Gs pair · C.A.Gs reviews · Mark & Teri Benjamin · Midland TX aviary.

---

## 7 · Entity seed set

*Psittacus erithacus* · Congo African Grey · Timneh · bonded pair · proven pair · companion pair · pair bond · sexual maturity 3–5 yrs · clutch 2–3 eggs · 2 clutches/yr · quarantine · supervised introduction · separate cages · one-person bird · DNA sexing · CITES Appendix I · USDA AWA · PBFD · Polyomavirus · APV · PCR screening · avian vet · IATA LAR · Delta / United / American cargo · Midland TX · Jins · Jeni · Roys · Amie · Bery · Elad · Evie · Mark & Teri Benjamin · The Benjamin Home-Raising Protocol · The Midland Socialization Method · $185 airport · $350 home · $200 deposit · 72-hour guarantee · 24-hour arrival window.

**Needs verification before use:** clutch size and frequency come from classified-ad copy, not an authority. Cite Lafeber / World Parrot Trust / a peer-reviewed source, or drop the figures.

---

## 8 · Gaps and moats

| # | Moat | Evidence |
|---|---|---|
| 1 | **The honest pair-versus-single answer** | Ten community threads say pairs often ignore their owners; zero commercial results admit it |
| 2 | **Three named routes with real birds and real prices** | Every rival offers one anonymous "pair" |
| 3 | **The maturity fact** | The #1 breeding-pair result sells a 15-month "breeding pair" |
| 4 | **Documentation** | A competing listing literally says "can't find paper work" |
| 5 | **US-only, CITES-honest shipping** | The direct rival advertises 1–4 day international delivery of an Appendix-I bird |
| 6 | **Value proof at half market rate** | $6,500–$8,000 market vs our $3,000–$3,500 |
| 7 | **Real named reviews with photos** | Rival claims 10,881 reviews and shows zero |

---

## 9 · Recommended angle

> ### ▣ APPROVAL GATE — Angle
> **Recommendation: "Two Birds, One Honest Answer."**
> Lead with the question every pair buyer is actually asking and nobody answers — *will they bond to each other and ignore me?* Answer it truthfully, including when the answer is "buy one bird." Then, having earned the trust, present the three real routes with named birds and real prices, and let the documentation and the price gap close it.
>
> **Why, grounded:** the head term has no demand (§2), so the page cannot be won transactionally. It *can* be won on the informational question, where demand is demonstrably high (ten threads, a Quora question, a Lafeber Q&A, an active Facebook thread) and commercial supply is zero. It is the same trade the DNA-Tested page made deliberately, and that page shipped. It also runs with the brand rather than against it: PRODUCT.md already names honesty as the conversion strategy and "talks buyers out of the wrong bird" as a design principle.
>
> **Trade-off, named:** an honest page will talk some buyers down from a $3,500 pair to a $1,700 single. That is real revenue traded for trust and for a defensible ranking on a question the whole market dodges. If the breeder wants pair revenue maximised instead, say so now — that is a different page and it should be decided before the outline, not after.
>
> Breeder approval: `[ ___ ]`

---

## 10 · Open flags raised by this sprint

| # | Flag | Owner |
|---|---|---|
| 1 | Cluster A / Cluster B intent split (§2) | **Breeder** |
| 2 | Pricing: market is $6,500–$8,000, we are $3,000–$3,500 (§5) | **Breeder** |
| 3 | Angle approval (§9) | **Breeder** |
| 4 | `/african-grey-breeding-pair-for-sale/` is a 4 KB stub holding 750 impressions at pos ~10 — **the highest-value unbuilt page in the cluster.** Recommend it is built immediately after this one | Build |
| 5 | Bing query export still missing — now blocking a second page (was open flag #9) | **Breeder** |
| 6 | Clutch figures sourced from classified ads; need an authority or drop them | Build |
| 7 | The mining doc's regex bucketing is unreliable per-page. Every remaining page should verify against `Pages.csv` before planning | Build |

---

## 11 · Correction to file

`docs/research/for-sale-keywords-2026-07.md` §`/congo-african-grey-parrot-pair-for-sale/` should carry a warning that its 497-impression figure is a regex artifact and the real figure is 8. Not edited yet — flagged so the next page does not repeat the mistake.

## 12 · What a full Sprint 0 would still add

The 30-competitor registry sweep, Bing queries, Instagram, YouTube teardown, and LLM visibility. **My judgement: none of it changes the recommended angle**, which rests on GSC page attribution, two fetched SERPs, two full competitor scrapes and ten community threads. It would sharpen the section inventory and the geo set. Say the word and it runs before Sprint 0.5.

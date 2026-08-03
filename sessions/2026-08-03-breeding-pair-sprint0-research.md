# Sprint 0 — Intel · `/african-grey-breeding-pair-for-sale/`

**Date:** 2026-08-03 · **Page 10 of 22**, Cluster 3 · **Mode:** REBUILD from a 3.6 KB stub
**Brief:** `docs/superpowers/plans/2026-08-03-cag-universal-page-build-brief.md` (Portable Edition v1.0)
**Gate:** ▣ APPROVAL GATE 2 — breeder signs off before Sprint 0.5 opens

> **Why this page, now.** The congo-pair Sprint 0 (2026-07-30) raised open flag #4:
> *"`/african-grey-breeding-pair-for-sale/` is a 4 KB stub holding 750 impressions at pos ~10 — the
> highest-value unbuilt page in the cluster."* The breeder's Cluster A/B decision that same day
> assigned every `breeding pair` query to this slug. This is the page that decision was made for.

---

## 0 · Coverage — what was fetched, and what was not

| Source | Status | Detail |
|---|---|---|
| GSC page attribution | ✅ **FETCHED** | `GSC-extracted/Pages.csv`, 16 months to 2026-07-16 |
| GSC query attribution | ✅ **FETCHED** | `GSC-extracted/Queries.csv`, full stem sweep |
| Bing **page** traffic | ✅ **FETCHED** | `BING-…PageTrafficReport_7_20_2026.csv`, 58 rows |
| Bing **query** data | ❌ **NOT FETCHED** | Still no query export. Both supplied CSVs are page-level and date-series. **Open flag — now blocking a third cluster page** |
| Google SERP | ✅ **FETCHED** | 2 SERPs, US location, 14 + 12 results |
| Competitor pages | ✅ **FETCHED** | exoticglobalparrotsfarm (#1), hookbillsforsale, royalbirdcompany — full scrapes |
| Authority sources | ✅ **FETCHED (snippets)** | Tony Silva / parrotsdailynews, Lafeber, BirdTracks, parrotforums, Watchbird (TAMU) |
| Community | ✅ **FETCHED (snippets)** | parrotforums, Quora, 3 Facebook breeder groups. **Full thread bodies not scraped** |
| Live market pricing | ✅ **FETCHED** | hookbillsforsale classifieds (dated 06/21–08/01/2026), birdsnow index via prior session |
| Instagram / YouTube | ⚠️ **PARTIAL** | 1 IG reel + 1 YT video surfaced in SERP; neither analysed |
| 30-competitor registry sweep | ❌ **NOT RUN** | |
| LLM visibility | ❌ **NOT RUN** | Sprint 5 per the pipeline — not a Sprint 0 deliverable |

**Sprint 0 is substantially complete.** §13 lists what a full sweep would still add; my judgement is that
none of it changes the recommended angle, which rests on measured GSC data, two fetched SERPs, three
full competitor scrapes and five authority sources.

---

## 1 · 🔴 BLOCKING FINDING — the product does not exist in any data file

This is the one thing that must be answered before Sprint 1.

| Source | What it says |
|---|---|
| `data/price-matrix.json` → `breeding_pair` | `$3,000` · *"Proven bonded breeding pair, DNA-certified"* · slug `african-grey-breeding-pair` |
| `data/clutch-inventory.json` → `birds[]` | **No breeding pair.** Nine records; the only pair is `jins-jeni`, a $3,500 **unrelated companion** pair |
| `data/bird-inventory.json` → `available_pairs[]` | **No breeding pair.** One entry: Jins & Jeni, `"pair_type": "unrelated"` |
| The live stub | Hardcodes `"price": "3000"` and `availability: InStock` for a pair no data file records |

**There is a price with no bird behind it.** No names, no ages, no sexes, no DNA certificates, no band
numbers, no clutch history — none of the six `trust_signals_required_on_every_listing` that
`bird-inventory.json` itself mandates.

This collides with three standing rules at once: **no fabricated claims** (§1e), **a sold bird is never
`InStock`** (§15d), and the **Verified-Claim Ledger** bound on every credential claim. A page that
sells "our proven pair" without a proven pair is the exact defect this page is built to counter-position
against — and §6 below shows two rivals doing precisely that.

**Everything else in Sprint 0 proceeds regardless.** The one question is in §12.

---

## 2 · URL, canonical and redirect gate — SETTLED, no action

| URL | Clicks | Impr | CTR | Pos |
|---|---|---|---|---|
| `/product/african-grey-breeding-pair-for-sale-nearby/` | 22 | 668 | 3.29% | 10.11 |
| `/african-grey-breeding-pair-for-sale-nearby/` | 2 | 75 | 2.67% | 15.36 |
| **`/african-grey-breeding-pair-for-sale/` ← target** | **1** | **7** | 14.29% | 13.71 |
| `/product/congo-african-grey-parrot-pair-for-sale/` | 4 | 297 | 1.35% | 31.27 |
| `/congo-african-grey-parrot-pair-for-sale/` (sibling, shipped) | 1 | 8 | 12.5% | 5.62 |

**Consolidated to this slug post-redirect: 750 impressions · 25 clicks · best position ~10.1.**

Both legacy URLs 301 to the target in **one hop**; verified live 2026-07-30 and re-checked in
`site/content/_redirects` today. No chains, no orphan targets. **29 files in `src/` already link here.**

**Recommendation: change nothing.** The redirect direction is correct — it consolidates a WooCommerce
legacy path into the cluster-native slug that owns the demand and the internal links. The target reads
1 click because it is a 3.6 KB stub, not because the URL is weak. Reversing costs a re-crawl cycle and
strands 28 links. **Trade-off:** GSC will keep reporting under the old URLs until the 16-month window
rolls off, so post-launch measurement must sum the family, not read the target row alone.

**Bing:** every breeding-pair URL is **absent** from the 58-row page report. Only the *companion*-pair
product URL appears (9 impr / 2 clicks / 22.22% / pos 5.11). Bing is unworked ground here.

---

## 3 · Demand — the query universe, measured

### Cluster A — BREEDING pair · **ours, by breeder decision 2026-07-30**

| Query | Clicks | Impr | CTR | Pos |
|---|---|---|---|---|
| breeding pair of african greys for sale | 10 | 169 | 5.92% | 9.01 |
| african grey breeding pair for sale | 7 | 156 | 4.49% | **7.14** |
| african grey parrot breeding pair for sale | 2 | 39 | 5.13% | 8.69 |
| african grey breeding pair | 2 | 26 | 7.69% | 20.54 |
| breeding pair african greys for sale | 1 | 62 | 1.61% | **5.21** |
| breeding african grey parrots for sale | 0 | 16 | 0% | 32.62 |
| breeding pair of african grey parrots for sale | 0 | 3 | 0% | **2.33** |
| african grey breeding pairs for sale | 0 | 2 | 0% | **2.50** |
| breeding african greys | 0 | 2 | 0% | 78.5 |
| **Total** | **22** | **475** | **4.63%** | — |

**Four of nine already rank inside the top 9, two inside the top 3 — on a 3.6 KB stub.** That is the
whole opportunity in one line: the demand and the rankings exist, and there is nothing on the page to
convert them.

### Cluster B — companion pair · **sibling's, hands off**
`african grey pair for sale` (29) · `african grey pair` (7) · `grey pair` (4). Owned by
`/congo-african-grey-parrot-pair-for-sale/`, shipped 2026-08-02.

### Cluster C — male/female informational · **comparison cluster's, hands off**
Owned by `/male-vs-female-african-grey-parrots-for-sale/`.

### Cluster D — fertile eggs · **egg page's, hands off**
~400 impressions across ~45 egg queries. Owned by `/african-grey-parrot-bird-eggs-for-sale-usa/`.

### Cluster E — 🟡 "african grey breeders" · **UNCLAIMED, and larger than Cluster A**

| Query | Clicks | Impr | Pos |
|---|---|---|---|
| african grey breeders | 2 | 103 | 71.85 |
| african grey parrot breeders | 1 | 67 | 67.06 |
| african grey breeder | 0 | 52 | 68.6 |
| african gray breeders | 0 | 41 | 63.02 |
| african grey parrot breeder | 0 | 32 | 74.22 |
| african gray parrot breeders | 0 | 24 | 73.58 |
| african grey breeders near me | 0 | 19 | 33.26 |
| congo african grey breeders | 0 | 17 | 71.71 |
| african grey bird breeders | 0 | 17 | 83.06 |
| + 8 more | 2 | ~90 | 20–99 |
| **Total** | **~5** | **~462** | **mostly 50–99** |

**462 impressions ranking at position 50–99 — near-zero visibility on a term the site should own.**
This is *not* this page's cluster: "african grey breeders" is find-a-breeder intent, which belongs to
`/african-grey-parrot-breeders-comparison/` or a hub. **Logged as a cluster-level opportunity, not
claimed here.** This page links to the owner once, and nothing more.

### Noise — exclude from all planning
~320 impressions across `best african grey breeds for {digital nomads, entrepreneurs, bartenders,
baristas, back sleepers, truck drivers, yoga practitioners…}` at positions 200–290. Machine-generated
query spam. **Not demand. Do not build for it, do not count it in any total.**

---

## 4 · SERP snapshot — "african grey breeding pair for sale", US, 2026-08-03

| # | Domain | Type | Note |
|---|---|---|---|
| 1 | **exoticglobalparrotsfarm.com** | Product | $2,500 "breeding pair", **1 yr 3 mo old** — see §6 |
| 2 | birdbreeders.com | Marketplace | $8,500 top listing |
| 3 | **birdsnow.com/bondedpairafricangreyparrot.htm** | Classified index | Dedicated bonded-pair page, 18 live ads |
| 4 | graybreedersfoundation.yolasite.com | **Scam-pattern** | Free Yola builder, flat $1,500 |
| 5 | buyafricangreyparrots.com | Breeder | USDA-licensed FL — a legitimate rival |
| 6 | facebook.com | Social | "The Exotic Bird Shop", breeding pairs |
| 7 / 10 | **royalbirdcompany.com** | **Breeder** | Real NC breeder-pair page — **`noindex`**, see §6 |
| 8 | denimixanipetsparadise.com | Product | $3,300 companion pair; ranks on both pair queries |
| 9 | youtube.com | Video | "I SPENT $13k on My African Grey Parrots" |
| 11 | instagram.com | Social | Reel — "African Grey Breeding Pair for sale" |
| 12 | hookbillsforsale.com | Classified + guide | Real price table — see §6 |
| 13 | birdsbyjoe.com | Breeder | |
| 14 | uncle-toms-parrot-farm.my-online.store | Product | Hosted store builder |

**congoafricangreys.com appears in neither top 14** — consistent with position 7.14 on the head term
(page 1 boundary, below the fold, on a stub).

**Structural read.** Fourteen results; **not one is a decision page for a breeding-pair buyer.** Every
result is a product listing, a classified index, a social post, or a species care guide. Nobody defines
*proven*, nobody states the maturity age, nobody explains what moving a pair does to it, nobody shows a
clutch record. **The category has no reference page.** That is the gap, and it is wide.

---

## 5 · The fact the whole SERP gets wrong

Sourced, and it decides the page:

| Source | Fact |
|---|---|
| **parrotforums.com** | *"breeding-pairs advertised for sale as 'Proven', which means that they have laid fertile eggs that have actually hatched."* — the industry definition, stated nowhere on the SERP |
| **Tony Silva** (parrotsdailynews) | *"African Grey Parrots reach sexual maturity by four years of age. We have had third generation Timnehs produce fertile eggs at three years"* |
| **BirdTracks** | *"Even after reaching sexual maturity, a pair may take another 1 to 2 years to actually produce their first fertile clutch."* |
| **Lafeber** | *"They need a very large cage with a nest box affixed to the outside of the cage. The nest box will be very large and very heavy, so the cage must [carry it]."* |
| **Lafeber** (prior session) | *"There is no way to predict if they will get along or bond as a breeding pair. All you can do is introduce them and see what happens."* |
| **hookbillsforsale** | African Greys are *"obligate monogamists… fledging period lasts up to 12 weeks"*; *"cavity nesters"* |
| **royalbirdcompany** (breeder) | *"when selling proven breeders there is no guarantees on future breeding once moved. We have moved some of our own proven breeders of many years… and the results were not the same."* |

**Synthesis, and it is the page's spine:**

> Sexual maturity at ~4 years, plus 1–2 more years to a first fertile clutch, means **a genuine proven
> pair is 5–6 years old at minimum**. The #1 result sells a **15-month-old** pair and calls it *proven*.
> That is not a rounding error — it is biologically impossible, and it is the top-ranked page in the
> category.

⚠️ **Ledger note.** Clutch size and frequency figures (2–3 eggs, 1–2 clutches/yr, 26–30 day incubation,
50–65 day fledging) currently trace to classified copy and a Facebook post. **Cite Lafeber, World Parrot
Trust, or the Watchbird/TAMU paper, or drop the numbers.** Carried forward from the congo-pair open
flag #6 — still unresolved.

---

## 6 · Competitor teardown

### exoticglobalparrotsfarm.com — position 1 · the counter-positioning target

Full scrape 2026-08-03. Content: product title, price, 3 photos, a 6-line spec list, a "Why Choose"
bullet block, related products. **No H2 structure beyond "Description". No FAQ. No care content.**

| Claim on the page | Why it fails |
|---|---|
| "**1 year 3 months old**" **and** "**Age:** Mature… of prime breeding age" | **Self-contradictory in the same product.** Both statements are on the page |
| "These parrots are **proven breeders**" | A 15-month bird cannot have hatched a clutch (§5) |
| "perfect for breeding **or as loving lifelong companions**" | Hedges both intents; a true breeder pair is not a companion (see royalbirdcompany) |
| "**Excellent return for avian breeding enthusiasts**" | Frames live Appendix-I birds as an investment vehicle |
| "**Add to cart**" · quantity selector | No application, no screening, no vetting, for a CITES Appendix-I pair |
| "Exceptional genetics and **bloodline**" | No pedigree, no band numbers, no parent records shown |
| $2,500 | **Below the documented-pair floor** — see the market table below |
| `generator: WordPress 7.0.2` | No such WordPress version exists |
| Zero named birds, zero DNA certificates, zero location, zero licence | The six trust signals we require on every listing |

**What it does not have, and we will:** named birds · a named breeder · a USDA licence number · DNA
certificates · band numbers · a real clutch record · the maturity fact · any statement of risk.

### royalbirdcompany.com — the honest voice in the market, and it is `noindex`

A real North Carolina breeder (Sheila, 20-acre farm, downsizing). This page says, out loud, everything
the category hides — and it carries `robots: noindex`, so **it does not compete in search at all.**

Verbatim, and every line is a section this page should own:

- *"BREEDER BIRDS or single extra adults are sold as **breeder stock only, not pet quality**."*
- *"**We make no future predictions on any breeding or pet results of any adult birds sold**… when
  selling proven breeders **there is no guarantees on future breeding once moved**."*
- *"When breeders or adults are sold and picked up, they **cannot be petted or handled**."*
- *"Breeder birds are subject to **missing toenails and sometimes a piece of toe**, as breeders can be
  aggressive to their mates during breeding seasons."*
- *"we **never ship adult pairs in same crate**"* — two crates, priced separately
- Their own African Grey listings: *"**Proven male**, has produced babies for the entire time… around
  15 years old… **Not tame… does growl when approached**… always retreated to nest box with hen when
  caretakers approached. **$600**"* · red-factor proven male **$4,200**
- *"All birds have been **DNA tested for health and sex**."*

**Strategic read:** the most honest breeder-pair page in the market is invisible to Google. The honest
position is *unoccupied in search* — not because it doesn't exist, but because the one site that holds
it opted out. **We can occupy it indexed.**

### hookbillsforsale.com — the informational rival worth beating

A genuinely strong species page: neurobiology, Pepperberg/Alex, taxonomy, a price table, housing specs,
a nutrition table, an FAQ. It ranks on our query **with zero breeding-pair content.**

Reusable facts (attribute, do not lift): Certified breeder **$3,500–$7,500** · specialty store
**$4,000–$8,500** · rescue **$500–$1,500** · *"If you see an African Grey for sale online for under
$1,500, it is statistically likely to be a scam"* · minimum cage **36"W × 24"D × 48"H**, medical-grade
stainless · **UVB T5 HO 6–8 h/day** · **68–80 °F**, **50–65 %** humidity · 60/30/7/3 diet split ·
*"Legitimate sellers provide a Hatch Certificate and a closed-loop metal leg band."*

**Its gap is total on our intent:** no proven-vs-unproven, no maturity age, no nest box, no clutch, no
pair compatibility, no breeder-stock temperament, no transfer risk.

### Live market pricing — dated listings, 2026

| Listing | Detail | Price |
|---|---|---|
| Congo pair, Gwynnoak MD (birdsnow) | ~8 yrs, bonded, semi-tame | **$6,500** |
| Landis & Foxxy, Stone Mountain GA | adult pair, **DNA tested** | **$8,000** |
| Congo pair, Evanston IL | adult, bonded, **recently DNA sexed** | **$6,500** |
| Maxi, Shades of Greys MN (07/13/26) | **15-yr hen, pairing FAILED** — *"my male is just not into having a companion… she lined her nest box with her feathers but has since [stopped]"* | **$2,500** |
| Royal Bird Co. NC | **proven** AG male, 15 yrs, not tame | **$600** |
| Royal Bird Co. NC | **red-factor proven** AG male | **$4,200** |
| Ana's Parrots PA (multiple, 07–08/26) | AG babies | **$8,500** |
| exoticglobalparrotsfarm | "proven pair", 15 months | **$2,500** |

> ### 🔴 PRICING — carried forward, decision already made
> The breeder ruled **2026-07-30: publish the comparison, prices unchanged.** The five binding rules
> from that decision apply verbatim here: the market figure never appears without its reason in the
> same paragraph · cite as **observed live listings**, never a survey or index · **no discount, sale,
> was/now, or struck-through pricing** · it must sit beside the anti-scam module with the distinction
> made explicit (*a low price with verifiable documentation and a named breeder is value; a low price
> with neither is bait*) · re-fetch if the listings go stale before launch.
>
> **New for this page:** the Maxi listing is the strongest single artifact in the set — a real, named
> breeder publicly selling a hen because **the pairing did not work.** It proves the risk we are going
> to state, in a competitor's own words, with a date and a phone number on it.

---

## 7 · Competitor gaps, angles and voice tones

| Competitor | Why it ranks | Voice / tone | Content gap | Exploitable weakness |
|---|---|---|---|---|
| exoticglobalparrotsfarm | Exact-match slug + product schema | Salesy, investment framing | Everything — no maturity, no proven definition, no care | Self-contradicting age; impossible "proven" claim; cart checkout for Appendix I |
| birdbreeders / birdsnow / hookbills | Domain authority, listing volume | Neutral aggregator | No editorial on pairs at all | No screening, no vetting, "can't find paper work" (NJ listing) |
| royalbirdcompany | **Does not rank — `noindex`** | Blunt, expert, first-person | — | Opted out of search entirely |
| buyafricangreyparrots | USDA-licensed, real breeder | Warm, professional | Babies only, no pair page | No breeding-pair intent served |
| graybreedersfoundation | Thin, exact-match | Scam-pattern | — | Free site builder, flat $1,500 |
| hookbillsforsale | Deep species content, real facts | Encyclopedic, third-person, authoritative | Zero breeding-pair content | Impersonal — no named birds, no breeder, no aviary |

**Our voice must be distinguishable at one paragraph:** first-person Midland breeder, naming our own
birds, stating the risk before the price. Nobody in the top 14 does all three. The one competitor with
our register (royalbirdcompany) is noindexed.

---

## 8 · Keyword universe and targets

**Primary:** `african grey breeding pair for sale` — 156 impr, pos 7.14, **real demand, real ranking.**
Unlike the last three pages in this cluster, this slug's head term is the traffic engine.

**Secondary (Cluster A, all ours):** breeding pair of african greys for sale · breeding pair african
greys for sale · african grey parrot breeding pair for sale · african grey breeding pair · african grey
breeding pairs for sale · breeding african grey parrots for sale · breeding pair of african grey parrots
for sale.

**Informational long-tail — the moat. No GSC volume on our property; sourced from SERP, PAA and forums,
and marked as such:**
what does *proven* mean on a breeding pair · at what age can african greys breed · how old must a
breeding pair be · will two african greys become a breeding pair · bonded pair vs proven pair vs two
singles · do proven pairs keep breeding after being moved · african grey nest box size and placement ·
african grey breeding cage size *(pos 1, 1 impr — we already rank)* · how many eggs do african greys
lay *(6 impr)* · how many clutches per year · african grey incubation and fledging time · are breeder
birds tame · can a breeder pair become pets · how to set up an african grey breeding pair · what
paperwork comes with a breeding pair.

**Transactional:** reserve a breeding pair · deposit · available now · pair price · ships nationwide ·
two crates · pickup in Midland.

**Branded / hybrid:** C.A.Gs breeding pair · C.A.Gs reviews · Mark & Teri Benjamin · Midland TX aviary ·
C.A.Gs pair pricing.

**Explicitly NOT targeted:** every Cluster B, C, D and E term (§3). **No heading may target
"african grey pair" without "breeding"** — that is the sibling's, by breeder decision.

### Metric targets for the build (§6a of the brief)

| Metric | Target |
|---|---|
| Total keyword mentions | 85–105 across ≥40 distinct terms |
| Primary density, first 30 KB | 1–2%, never stuffed |
| Exact match in tags | title 1 · H1 1 · H2 2–4 · primary image alt 1 |
| Distinct entities | 85–112 |
| Counter snippets | 8, <4 words, Ledger-verified |
| H5 / H6 | ≥5 each, all six levels, no skips |

---

## 9 · Entity map and co-occurrence

**Breeding-specific (this page's own vocabulary — none of it is spent on a sibling):**
proven pair · unproven pair · bonded pair · compatible pair · breeder stock · pet quality · sexual
maturity (4 yrs) · first fertile clutch (+1–2 yrs) · fertile egg · hatched clutch · nest box
(external-mount) · cavity nester · obligate monogamy · allopreening · ritualized feeding · clutch ·
incubation · fledging (up to 12 wks) · altricial chick · parent-fed · hand-fed · brooder · flight cage ·
suspended aviary · breeding season · pair aggression · re-pairing · transfer risk · surgical sexing ·
DNA sexing · closed-loop band · hatch certificate · pedigree.

**Shared (bounded by the Ledger):** *Psittacus erithacus* · Congo · Timneh · CITES Appendix I ·
USDA AWA · PBFD · Polyomavirus · psittacosis · PCR panel · UV-B/D3 · avian vet · IATA LAR ·
Delta/United/American cargo · Midland TX · Mark & Teri Benjamin · The Benjamin Home-Raising Protocol ·
The Midland Socialization Method · $185 airport · $350 home · 72-hour guarantee · 24-hour arrival.

**Co-occurrence pairs the top-ranking pages do NOT make, and we will:**
`proven` × `hatched clutch` · `age` × `sexual maturity` · `pair` × `compatibility risk` ·
`breeder stock` × `not tame` · `moved` × `breeding stops` · `nest box` × `cage load` ·
`DNA sexed` × `band number` · `Appendix I` × `captive-bred documentation`.

**Predicate gaps** — assertions no competitor makes: *a proven pair has hatched fertile eggs* · *a
15-month pair cannot be proven* · *breeder stock is not tame and does not become tame* · *relocation
can end production* · *two greys placed together do not become a breeding pair* · *pairs ship in two
crates, never one*.

---

## 10 · Gaps and moats

| # | Moat | Evidence |
|---|---|---|
| 1 | **Define "proven" and hold the SERP to it** | The #1 result sells a 15-month "proven" pair; the definition exists on a forum and nowhere else |
| 2 | **The maturity arithmetic** | Silva (4 yrs) + BirdTracks (+1–2 yrs) = 5–6 yrs minimum. Nobody states it |
| 3 | **Breeder stock ≠ pet, said plainly** | Only royalbirdcompany says it — and it's noindexed |
| 4 | **Relocation risk stated before the sale** | A breeder's own words: *"the results were not the same"* |
| 5 | **A real failed-pairing artifact** | Maxi, Shades of Greys, 07/13/26, $2,500, nest box abandoned |
| 6 | **Documentation** | Six trust signals vs a rival with none and a WordPress version that doesn't exist |
| 7 | **Two-crate, US-only, CITES-honest shipping** | The category's shipping claims are unexaminable |
| 8 | **Value proof at half market rate** | $6,500–$8,000 documented pairs vs ours — with the reason attached |
| 9 | **Named birds, named breeder, real reviews** | Zero rivals in the top 14 name a single bird |

---

## 11 · Recommended angle

> ### ▣ APPROVAL GATE — Angle
> **Recommendation: "Proven Means Hatched."**
>
> Open by defining the one word the entire category abuses, then apply the definition to the market in
> front of the buyer — including the #1 result's 15-month "proven" pair. Establish the maturity
> arithmetic. State plainly that breeder stock is not a pet, that pairing is not guaranteed, and that
> moving a producing pair can stop it. Then present our real pair with its documentation, its clutch
> record and its price, and let the paperwork close it.
>
> **Why, grounded in the data:** unlike the last three pages in this cluster, **this page's head term
> already has demand and ranking** — 475 impressions, 22 clicks, four queries in the top 9, two in the
> top 3, on a 3.6 KB stub (§3). It does not need an informational rescue angle; it needs a real page
> under the rankings it already holds. The angle is chosen because the category's single, verifiable,
> repeated failure is the misuse of *proven* (§5, §6), and correcting it is free authority that no
> rival can copy without repricing their own inventory.
>
> **Why not the alternatives:** a pure product page loses to birdsnow and birdbreeders on listing
> volume and to marketplaces on domain authority. A pure care guide loses to hookbillsforsale, which
> already out-researches everyone. The definitional angle is the only one where our documentation is
> the deciding asset.
>
> **Trade-off, named:** this angle disqualifies buyers. Telling someone a pair must be 5–6 years old,
> will not be tame, and may stop producing when moved will cost inquiries from people who wanted a
> $2,500 cart checkout. It also constrains our own listing — we cannot call a pair *proven* unless it
> has hatched a clutch, and §1 says we currently cannot substantiate that at all. **That is the real
> cost, and it is the point: the page's authority comes from applying the standard to ourselves first.**
>
> **What the angle commits the page to:**
> 1. The definition of *proven* appears **before** any price or bird card.
> 2. The maturity arithmetic is stated with its sources cited inline.
> 3. **Breeder stock ≠ pet** gets its own section, with a route to the pet pages for buyers who are in
>    the wrong place — framed as fit, not as a lesser option.
> 4. The relocation-risk statement is ours, in first person, not buried in terms.
> 5. **Voice lever: proven-versus-unproven.** Reserved vocabulary for this page — *proven, hatched,
>    clutch, nest box, breeder stock, re-paired, production*. Siblings own bonded/companion/introduced
>    (congo-pair), hen/cock (DNA), enforceable (guarantee), weaned-first (baby).
> 6. **Frameworks:** QAB for the definition → EEBP for the pair listing → PAS for the relocation risk.
>    *Not* PDB or BAB (spent on the baby page); *not* the congo-pair's PAS→EEBP→QAB order.
> 7. Every health and credential claim inside the Verified-Claim Ledger. Community consensus is cited
>    as community consensus; Silva, Lafeber and BirdTracks are cited by name.

---

## 12 · Open flags

| # | Flag | Owner |
|---|---|---|
| **1** | 🔴 **BLOCKING — no breeding pair exists in `clutch-inventory.json` or `bird-inventory.json`; only a bare `$3,000` price row.** The page cannot list a pair, emit an `Offer`, or claim *proven* until this is answered. See the question below | **Breeder** |
| 2 | Bing query export still missing — now blocking a **third** cluster page. Page-level Bing shows zero breeding-pair presence, so the channel is unmeasured and unworked | **Breeder** |
| 3 | Clutch/incubation/fledging figures still trace to classified copy and a Facebook post. Need Lafeber / WPT / Watchbird, or drop them. *(Carried from congo-pair flag #6 — unresolved across two pages)* | Build |
| 4 | 🟡 Cluster E — `african grey breeders`, ~462 impressions at position 50–99, **unclaimed by any page.** Larger than this page's own cluster. Belongs to the breeders-comparison page or a hub; recommend it is scheduled | Cluster |
| 5 | Stub (3,668 bytes) carries a stale gold palette (4 `text-gold`/`bg-gold` hits), hardcoded `"price": "3000"`, unconditional `InStock`, and only **1 H1 + 1 H2 — no H3–H6 at all**. Both schema image files were checked and **do exist** in `public/`. All replaced in Sprint 2 | Build |
| 6 | `royalbirdcompany.com` listings are dated and will go stale; re-fetch the pricing table before launch | Build |

> ### ▣ THE ONE QUESTION — please answer before Sprint 0.5
> **Which birds is this page actually selling, and has that pair hatched a clutch?**
>
> Three ways this can go, and each produces a genuinely different page:
>
> **(a) We have a real proven pair (Recommended, if true).** Give me the two birds' names, ages, sexes,
> DNA/band numbers, and how many clutches they have hatched. The page runs exactly as scoped above with
> a real `Product`/`Offer` at $3,000.
>
> **(b) We have a pair that is bonded but has not hatched a clutch.** Then it is an **unproven** or
> **compatible** pair, priced accordingly, and the page says so — which, given the angle, is a strength,
> not a climb-down. We would be the only page in the category drawing the distinction on our own stock.
>
> **(c) We have no pair to sell right now.** Then this becomes a **ranking + waitlist** page: it owns
> the 475 impressions, teaches the standard, routes breeding-stock buyers to a waitlist, and routes
> everyone who actually wanted a pet to the single-bird pages. No `Offer` schema, no price, no
> `InStock`. **This is still worth building** — it holds four top-9 rankings we currently waste.
>
> I recommend **(a) if and only if the clutch record exists**; otherwise **(c)** over (b), because a
> waitlist is honest and an unproven pair sold on a page about the meaning of *proven* invites the
> exact scrutiny the page is designed to survive.

---

## 13 · What a full Sprint 0 would still add

The 30-competitor registry sweep · Bing queries (blocked on the breeder) · the Instagram reel and the
YouTube $13k video · full Reddit thread bodies rather than snippets · buyafricangreyparrots and
birdsbyjoe teardowns. **Judgement: none of it changes the recommended angle**, which rests on measured
GSC demand, two fetched SERPs, three full competitor scrapes and five cited authorities. It would
sharpen the section inventory and the geo set. Say the word and it runs before Sprint 0.5.

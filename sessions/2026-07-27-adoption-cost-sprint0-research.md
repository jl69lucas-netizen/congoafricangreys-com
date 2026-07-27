# Sprint 0 Research — `/african-grey-parrot-adoption-cost/`

**Run 2026-07-27 · page 8 of 22, for-sale cluster · REBUILD**
Plan: `docs/superpowers/plans/2026-07-27-adoption-cost-page-build.md`
Pack: `sessions/for-sale-research/african-grey-parrot-adoption-cost/2026-07-27-adoption-cost-prompt-pack.md`

---

## THE THREE FINDINGS THAT CHANGE THE BUILD

**1. The "360 impressions" figure is a keyword-mapping target, not measured traffic.**
`docs/research/for-sale-keywords-2026-07.md` states its own caveat in the header: *"Bucket assignment is
regex-based, first-match; treat as draft until per-page Sprint 0 refines it."* The slug appears in
**0 of 124 rows** of `Pages.csv`. The page currently earns essentially nothing.

This is better news than it sounds. The page is not defending traffic — it is **claiming an unowned
782-impression cost/price universe** that the homepage is currently absorbing at position ~49. Reframe
the brief accordingly: this is a land-grab, not a defence.

**2. The homepage already ships a First-Year Cost Calculator.** See `src/pages/index.astro:828`. The
earlier "site-first" claim was produced by a broken check (`src/pages/*/index.astro` excludes the
homepage). Breeder ruling 2026-07-27: **differentiate, do not duplicate** — multi-year, ranges, route
comparison. Corrected spec in pack §6.

**3. A rescue's own fee page argues our thesis for us.** Phoenix Landing's adoption-fee page says the
adoption fee *"is minimal compared to the cost of caring for a parrot"*. That is "The Fee Is Not the
Cost" stated by the adoption side. It is the single strongest external citation available to this page.

---

## A. Our own data

### A1. The cost/price query universe — 121 queries, 782 impressions, 1 click

Extracted from `assets/1WORKING-ON/FOR-SALE-PAGES/GSC-extracted/Queries.csv` (793 queries, 16 months to
2026-07-16) on the regex `adopt|cost|price|how much|cheap|rehome|rescue|fee`.

**It splits into six sub-clusters, and only three belong to this page.**

| Sub-cluster | Impr | Best pos | Owner |
|---|---|---|---|
| Congo-prefixed price (`congo african grey price` 80, `congo african grey parrot price` 71, `congo grey parrot price` 61, +3 more) | ~240 | 29.7 | **`/congo-african-grey-for-sale/`** — not this page |
| Egg price (`african grey parrot egg price` 41, `african gray parrot eggs price` 28) | ~69 | 91 | **`/african-grey-parrot-bird-eggs-for-sale-usa/`** |
| Cheap / cheapest (~11 variants) | ~70 | 19.8 | **`/affordable-african-grey-birds-for-sale/`** — see A3, it is strong |
| **Generic price** (`african grey parrot price` 32, `african gray bird price` 28, `african grey price` 19, `african grey birds price` 13, `price of african grey` 7, …) | **~150** | 45.1 | **THIS PAGE** |
| **Adoption** (`african grey parrot for adoption` 18, `african gray parrot for adoption` 16, `congo african grey parrot adoption cost` 3 @ **23.3**, `congo african grey parrot adoption price` 1 @ 19, `african grey parrot adoption` 1 @ 17, `african grey for adoption` 1 @ 17, `adopt an african grey parrot` 1) | **~41** | **17** | **THIS PAGE** |
| **Conversational "how much"** (~25 variants) | **~50** | **9.5** | **THIS PAGE** |

**This page's real universe: ~241 impressions across roughly 60 queries.** Not 360, and not the 782
the regex bucket implied.

### A2. The single best ranking opportunity on the page

`how much does an african grey parrot cost` — **4 impressions at position 9.5**, the only query in the
whole cost universe sitting on the edge of page one. Treat it as the **featured-snippet target**: it
gets a dedicated H2 or H3 phrased as the question, answered in the first 40–55 words directly beneath,
as a range with both endpoints.

Second tier, all already inside the top 25 and worth an explicit answer block:
`african grey parrot price near me` (4 @ 13.0) · `african grey parrot price us` (2 @ **11.5**) ·
`congo african grey parrot adoption cost` (3 @ 23.3) · `congo african grey parrot adoption price` (1 @ 19) ·
`african grey parrot adoption` (1 @ 17) · `african grey for adoption` (1 @ 17).

### A3. Cannibalization — the real risk is NOT where the pack assumed

| Page | Clicks | Impr | Pos | Verdict |
|---|---|---|---|---|
| `/african-grey-parrot-price/` | 0 | **3** | 5.67 | Negligible incumbent. Ranks well but on almost nothing. Not a threat. |
| `/african-grey-adoption/` | 0 | **6** | 7.83 | Same. Ranks 7.8 on 6 impressions. |
| `/congo-african-grey-for-sale/` | 0 | 1 | 11 | **Owns the ~240-impression congo-price cluster by right of topic.** Do not chase it. |
| `/affordable-african-grey-birds-for-sale/` | 1 | **242** | **13.29** | **Genuinely strong. Owns "cheap"/"affordable". Do not chase it.** |
| `/product/affordable-african-grey-birds-for-sale/` | 1 | 431 | 64.71 | legacy `/product/` duplicate — separate cleanup issue |

**Revised guard, replacing the pack's assumption:** the two interior pages the pack flagged are
non-issues at 3 and 6 impressions. The pages this build must actively avoid are
**`/affordable-african-grey-birds-for-sale/`** (never target *cheap*, *cheapest*, *affordable*, *budget*)
and **`/congo-african-grey-for-sale/`** (never target *congo + price* as a head term; use it only as an
internal link).

**Confirmed intent split:**
- `/african-grey-parrot-price/` → cost of **keeping** a grey. Encyclopedia. Link to it for running costs.
- `/african-grey-adoption/` → **whether and where** to adopt. Route guidance. Link to it for the rescue route.
- **THIS page** → **what you hand over to acquire one, by route.** Adoption fee vs breeder price vs
  sub-floor listing, and which reservable bird fits which budget. Transactional.

### A4. Country data — the evidence for the negative-keyword ruling

`Countries.csv`: **India = 12 clicks / 501 impressions / 2.4% CTR / position 35.76** site-wide.

Queries confirmed verbatim from `Queries.csv`:

| Query | Clicks | Impr | Pos |
|---|---|---|---|
| african grey parrot price in india | 0 | 43 | **1.0** |
| congo african grey parrot price in india | 0 | 2 | 1.0 |
| cost of african grey parrot in india | 0 | 1 | 1.0 |
| african grey parrot price in bangladesh | 0 | 2 | 19 |
| african grey price philippines | 0 | 1 | 2 |

Position 1.0 on 43 impressions with **zero clicks**, across three separate India queries. A permanent
0% CTR ceiling for a US-only aviary. **Ruling stands: negative, counter-position, never target.**

**The positive counterpart, which we SHOULD target** — readers who qualify the query as US:
`african grey parrot price us` (2 @ 11.5) · `african grey price in usa` (2 @ 38.5) ·
`african grey parrot price in usa` (2 @ 77). Small volume, but exactly our buyer, and one is already at
11.5. The counter-positioning H4/H5 should carry "in the USA" language so it captures these while
deflecting the rest.

**Bing:** still NOT FETCHED. `Fresh-Bing-DADA-as-of-16-07-2026.csv` is a date-series traffic chart with
zero query rows — the same gap the keyword doc flagged. Needs Bing Webmaster Tools → Search Performance
→ **Queries** export. Carried as an open flag; it does not block this build.

---

## B. SERP research

Fetched live via Firecrawl search 2026-07-27. Reddit via Playwright (Firecrawl and the Browser pane both
refuse Reddit — Firecrawl returns "we do not support this site", the Browser pane blocks by policy).

### B1. Intent 1 — "african grey parrot adoption cost": rescue non-profits, with real published fees

**This is the gift of the whole research pass. The fees are public, specific, and citable.**

| Organisation | African Grey adoption fee | URL |
|---|---|---|
| Parrots First | **$450** | `parrotsfirst.org/adoption-donation-fees` |
| Phoenix Landing (MD/DC/VA/NC/PA) | **$500** | `phoenixlanding.org/adoption-fees.html` |
| Companion Parrots Rescue | **$500** | `companionparrots.org/adopting-from-cpr/adoption-process/` |
| Rhode Island Parrot Rescue | **$1,500** | `riparrots.org/current-fees` |
| Florida Parrot Rescue | fee + cage valued $50–$500 | `floridaparrotrescue.com/.../adoption-fees/` |

**Published rescue range: $450 – $1,500.** The existing on-disk page claims **"$300–$800"** — that number
is **contradicted by every source above and must be corrected in the rebuild.** Rhode Island's $1,500
lands exactly on our own floor price, which is a far more interesting story than "adoption is cheaper".

**Two citations that carry the page's whole argument:**

1. **Phoenix Landing** states the adoption fee *"is minimal compared to the cost of caring for a parrot"*
   and lists what it does not cover — food, veterinary care, enrichment, a spacious cage. A rescue,
   on its own fee page, making our exact point. Cite it in the opening movement.
2. **Parrots First** routes *"any species listed in CITES Appendix I"* to case-by-case committee review.
   African Greys were uplisted to **Appendix I at CoP17, effective January 2017**; that fee schedule is
   dated **2011**. The paperwork burden we handle as routine is the same burden that makes a rescue slow
   down. This is a genuine, verifiable, on-brand entity hook — use it, and state the dates precisely.

### B2. Intent 2 — "how much does an african grey parrot cost": marketplaces, and a visible scam tier

| Source | Prices shown | Note |
|---|---|---|
| birdbreeders.com | $5,200 – $8,500 | premium breeder listings |
| LinkedIn editorial | "$800 and $4,000" | thin, no sourcing |
| exoticparrotpetstore.com | $800 – $3,800 | **fake strikethrough "original price" discounts on live animals** |
| graybreedersfoundation.yolasite.com | $450 – $1,500 | **"ADOPT NOW!!" headline over priced birds** |
| YouTube (The African Grey Journal) | "I SPENT $13k on My African Grey Parrots" | high engagement |

**Real US market spread: ~$450 (rescue) → ~$8,500 (premium breeder).** Our $1,500–$3,500 sits mid-band —
defensible without claiming to be cheapest, which we must not do anyway (that term belongs to
`/affordable-african-grey-birds-for-sale/`).

**The scam tier is visible in the SERP and is on-angle.** Two live patterns worth teaching:
(a) manufactured strikethrough discounts on a living animal; (b) a commercial seller using "ADOPT"
language over priced stock — the exact fee/price conflation this page exists to untangle.
**Describe the patterns; do not name the sites on-page.** Naming a specific business as a scam invites
a defamation problem for no SEO gain.

**Tool gap, competitor half — CONFIRMED.** No page on either SERP ships a calculator, quiz, or filter.
The moat holds against competitors; it just is not a site-first.

### B3. Reddit — real threads, fetched

**Thread 1 — r/parrots, "Rescue African grey price"** (3y)
`reddit.com/r/parrots/comments/133zdo2/rescue_african_grey_price/`

- OP: a San Diego bird store asking a **$5,500 "rehoming fee"** for a 6-year-old tame grey with thin
  history, while selling hand-tame babies at **$6,000**. The premise of "adoption is the cheap route"
  collapses in the first sentence of the thread.
- The most useful line in either thread, from `iPod3G`: rehoming is *"a euphemism meaning 'Selling'"*.
- `foreverbugg` (rescue and non-profit background) argues lifetime cost dwarfs acquisition, and mentions
  budgeting for a 60+ year bird in a retirement plan.
- Historical anchors from named users: $500 for a 15-year-old CAG in 2013 · $1,400 hand-tame from an
  aviary in 2013 including a cage · babies around $4,500 by 2023 · $4,000 CAD in Nov 2021 including airfare.

**Thread 2 — r/parrots, "Why are African greys so expensive all of a sudden?"** (3y)
`reddit.com/r/parrots/comments/14tjxez/why_are_african_greys_so_expensive_all_of_a_sudden/`

- `arrowrootapothecary` (28 pts): adopted a 15-year-old grey for **$900**, cage and toys included.
- `BSH72`: has not seen a CAG or TAG adopted under **$600**; sees them locally around **$900**.
- Top comment (332 pts) argues high prices deter unprepared buyers of a 50-year commitment.
- `Polishing_My_Grapple`: attributes the jump to COVID-era demand against 2013's $1,400.

**Owner-reported adoption reality: $600–$900 typical, up to $5,500 in a high-demand metro.** Cross-check
that against the published $450–$1,500 schedules — the gap between the *listed* fee and the *market* fee
is itself a section.

**Quoting rule for the build:** short, attributed, and mostly paraphrased. Do not reproduce long comment
blocks; link the thread.

### B4. PAA — fetched live from Google

Genuine PAA:
1. How much should I pay for an African grey parrot?
2. How much do baby African grey parrots cost?
3. How much does a baby African grey parrot cost?
4. How much do African Greys cost?
5. Why are African grey parrots so expensive?
6. What is the average cost of taking care of an African grey parrot daily?
7. How long will an African grey live?
8. Is an African grey parrot a good pet?
9. Do African grey parrots talk?
10. What is the 3 3 3 rule for parrots?
11. What was the cost of grey parrot in India, is it legal to pet? — *India surfaces even in PAA;
    handle inside the counter-positioning block, never as a target.*

**Google's own refinement chips, and they matter:**
12. *"Are you looking for a baby bird or an older rescue?"*
13. *"Do you need help finding a local breeder or a parrot rescue group?"*

Google is splitting this query into **breeder vs rescue** and **baby vs older bird** without being asked.
That is independent validation of the route-comparison structure and of Table G. Mirror both forks
explicitly in the H2/H3 layer.

**Gap:** 11 genuine PAA against the pack's target of 15. Google returned 4 per query and the remainder
load on expansion. Fill the balance at the `@cag-paa-agent` step in Sprint 2 rather than blocking here.

---

## C. Entity universe — anchors confirmed this pass

Money and route entities now grounded in fetched sources: adoption fee · rehoming fee · surrender ·
foster-to-adopt · adoption committee · adoption application · Parrots First · Phoenix Landing ·
Companion Parrots Rescue · Rhode Island Parrot Rescue · Florida Parrot Rescue · CITES Appendix I ·
CoP17 · January 2017 uplisting · USDA AWA · DNA sexing · PBFD · Polyomavirus · PCR · avian vet wellness
exam · IATA LAR · live-animal cargo · deposit · closed leg band · hatch certificate · quarantine ·
Harrison's · Roudybush · TOP's · Zupreem Natural · *Psittacus erithacus* · Congo · Timneh · Jaco
(alternate common name — appears as `jaco parrot price` 4 impr and `jako parrot price` 1).

Target 85–112 distinct entities. Brand 5–10×. Full-location 1–2× plus city/state 5–8×.

---

## D. Geo — the six states hold

`/african-grey-parrot-for-sale-{new-jersey, massachusetts, minnesota, missouri, oregon, indiana}/` all
verified present on disk. All six are unused by the health-guarantee (TX/OH/CO/NC/GA/MI/PA/VA) and baby
(CA/TX/WA/FL/NY/IL/GA/AZ) pages. Plus Midland TX pickup within 2–3 hours.

Rescue-density note supporting the choice: the fetched rescue set is concentrated in the Northeast and
Mid-Atlantic — Rhode Island Parrot Rescue, Phoenix Landing across MD/DC/VA/NC/PA, and a New Jersey
rehoming account in thread 1. **New Jersey and Massachusetts are therefore the strongest geo openers**
for an adoption-intent page, which is a real reason rather than a rotation.

---

## E. Top three gaps we can own

1. **Nobody prices the routes side by side.** Rescues publish a fee and stop. Marketplaces publish a
   price and stop. Not one page in either SERP shows adoption fee vs breeder price vs sub-floor listing
   across Day One / Year One / Five Year. That is Table G, and Google's own refinement chips show it is
   what people are trying to work out.
2. **Nobody reconciles the published fee with the market fee.** Schedules say $450–$500; owners report
   $600–$900, and a San Diego store wanted $5,500. Publishing that gap honestly is a trust moat a
   rescue will not build and a marketplace will not want.
3. **Nobody has a tool.** Confirmed across both SERPs. Differentiated per pack §6 so it complements
   rather than repeats the homepage first-year calculator.

---

## F. Open flags carried forward

1. **Bing query export still missing** — supplied CSV is a chart, not query rows. Non-blocking.
2. **PAA at 11 of 15** — finish at the `@cag-paa-agent` step in Sprint 2.
3. **Homepage price drift** — the homepage calculator hardcodes `Timneh — $1,600`; `price-matrix.json`
   holds `$1,500–$1,600` and Evie is $1,500. Log only; repairing the homepage is out of scope here.
4. **Legacy `/product/` duplicates** — `/product/affordable-african-grey-birds-for-sale/` (431 impr) and
   `/product/african-grey-parrot-bird-eggs-for-sale-usa/` (580 impr) still draw impressions alongside
   their clean slugs. Separate cannibalization cleanup, out of scope.
5. **The on-disk page's "$300–$800 rescue" claim is wrong** and must not survive the rebuild.

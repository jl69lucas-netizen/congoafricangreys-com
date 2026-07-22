# Sprint 0 — Timneh African Grey For Sale: Competitor + Keyword Intelligence (REBUILD)

**Target page:** https://congoafricangreys.com/timneh-african-grey-for-sale/ (on disk: `src/pages/timneh-african-grey-for-sale/index.astro` — thin 15 KB, Jun 26; REBUILD to for-sale standard)
**Primary keyword:** `timneh african grey for sale` (transactional / commercial-purchase + comparison intent)
**Run date:** 2026-07-21 · **Mode:** Timneh-focused deep dive (breeder-approved scope)
**Sources this session:** Firecrawl `firecrawl_search` (Google-style, US) ×4 · `firecrawl_scrape` ×3 (birdsbyjoe DEEP, africangraysales DEEP, silvergatebirdfarm=blocked) · our on-disk GSC-extracted CSVs + Bing Page Traffic CSV.
**Data-integrity rule applied:** only live-fetched data reported as fact; blocked/dead = **NOT FETCHED**; nothing invented.

---

## 0. Fetch Ledger (transparency)

| Source | Result | Timneh signal captured |
|---|---|---|
| birdsnow.com (Timneh classifieds) | ✅ SERP #1 both core queries | Aggregator, listings $2,800–$6,500, pickup+ship, no depth |
| birdbreeders.com | ✅ SERP #2 | Classifieds, $4,000–$8,500, phone-driven |
| hookbillsforsale.com | ✅ SERP #7 | Classifieds, Timneh $3,500 / $6,500 |
| exoticparrotsplanet.com | ✅ SERP #3 | Single product, Timneh $1,349, 7-mo female |
| exoticglobalparrotsfarm.com | ✅ SERP #6/#1 | Single products $800–$1,350, "place your order" |
| **birdsbyjoe.com** | ✅ **DEEP fetched** | Real breeder; species-education blurb ONLY, no birds/prices/FAQ |
| **africangraysales.com** (Dallas) | ✅ **DEEP fetched** | **Closest direct competitor — full architecture reverse-engineered below** |
| silvergatebirdfarm.com | ❌ **NOT FETCHED** — cloaks → `recaptcha.cloud` (Cloudflare turnstile wall) | SERP #5 snippet: "$1,500–$3,500". **Confirmed scam-adjacent cloaker ranking p1** |
| Reddit threads (r/parrots, r/AfricanGrey ×5) | ⚠️ bodies **NOT FETCHED** (Firecrawl "site not supported"); **SERP snippets fetched** | Community temperament + price sentiment (below). Playwright MCP fallback available for verbatim quotes. |
| Facebook group threads ×2 | ⚠️ bodies NOT FETCHED (login wall); snippets fetched | "avg cost of Timneh", "Congo vs Timneh differences" — price + decision sentiment |
| YouTube ×2 | ✅ snippet | "Timneh vs Congo full comparison"; "$13k on my African Greys" (lifetime-cost angle) |

---

## 1. SERP snapshot — who ranks (US, 2026-07-21)

**`timneh african grey for sale` top 9:** ①birdsnow ②birdbreeders ③exoticparrotsplanet ($1,349) ④**birdsbyjoe** ⑤**silvergatebirdfarm** (cloaker) ⑥exoticglobalparrotsfarm ($1,350) ⑦hookbillsforsale ⑧birdbreeders/timneh ⑨birdsnow/adult.

**`buy timneh … price` top 9:** ①exoticparrotpetstore ($950 baby) ②birdbreeders ③**Facebook group** "avg cost of Timneh" ④**Reddit r/parrots** "African Grey Cost" ⑤silvergatebirdfarm ⑥parrotcrown ($6,500) ⑦graybreedersfoundation ($1,500) ⑧birdsnow ⑨**YouTube** "$13k on my African Greys".

**`baby timneh … near me` top 9:** ①exoticglobalparrotsfarm ($800) ②birdbreeders ③handraredparrots ($1,400) ④**Facebook** africangreyforsale ⑤birdsbyjoe ⑥midnightparrotplace ⑦**africangraysales** (Dallas $2,000–$2,600) ⑧birdsnow ⑨(expired domain).

**Read:** page 1 is ~60% thin **classified aggregators** (birdsnow, birdbreeders, hookbills) + single-product breeder pages with almost no supporting content, **plus community pages** (Reddit/FB/YT) ranking on cost/decision queries. **No single page owns "real available Timnehs + deep Timneh education + honest pricing + scam protection + CITES + shipping + EEAT."** That gap is our page.

---

## 2. Competitor reverse-engineering

### 2a. africangraysales.com — CLOSEST DIRECT COMPETITOR (Dallas, TX) — full architecture
Their `/timneh-african-grey-parrots-for-sale.html` is the most complete Timneh page in the SERP and is clearly the template the research-doc architecture echoes. Section stack:
1. Hero + promo banner (Males **$750** | Females **$820**; "regular $2,000–$2,600"; $200 deposit)
2. About Timneh (Psittacus timneh, charcoal grey, maroon tail, horn beak, "calmer than Congos")
3. **4 feature cards** — Compact Size (9-11in, 275-350g) · Equally Intelligent · Calmer Temperament · Long Lifespan (40-50yr) — **rendered with emoji 📏🧠😌⏳**
4. **Congo vs Timneh table** (7 rows: size, tail, beak, body, temperament, talking, price)
5. Diet & Care (pellets 70-80% / veg 20-25% / cage 32×24×40)
6. Available Timneh cards (only **1 bird**: Mike, $2,100→$750, male 6mo)
7. Why Choose Timneh (6 bullets: smaller, calmer, same intelligence, lower price, affectionate, less intimidating)
8. **"Ship nationwide & INTERNATIONALLY — Canada, Australia, arrive within 24 hours"** + location links (TX/CA/FL/NY/IL/Canada/Australia)
9. FAQ ×6 (cost, lifespan, talk vs Congo, difference, beginners, shipping)
10. Contact form (lists Mike + "Any Timneh")

**Their weaknesses = our moat (all counter-positionable):**
- 🚩 **Ships "internationally to Canada & Australia within 24 hours"** — African Greys are **CITES Appendix I**; that international/24-hour claim is precisely the scam signal our own scam cluster flags. We ship **US-only**, and we say why. **Biggest single differentiator.**
- 🚩 **$2,100 → $750 "limited time" deep discount** reads as a bait pattern; no documentation backs the birds.
- Emoji icons (we use Feather line-icons + real `cag-timneh.png`, never 🦜).
- No CITES/USDA license depth, no PBFD/APV PCR health-screening specifics, no scam-protection module, no video, no verifiable breeder story/EEAT, no H1→H6 hierarchy.
- Only **1** available bird; we list **2 real** (Elad, Evie) with per-bird Product/Offer schema.

### 2b. birdsbyjoe.com (SERP #4) — real breeder, thin page
Species-education blurb only (Timneh origin Ivory Coast/Liberia; 9-11 in; 250-375 g; maroon/dark-red tail; pink beak w/ black maxilla; white head scalloping) + a Congo blurb + a phone number. **No available birds, no prices, no FAQ, no schema, no trust signals, no shipping detail.** Confirms the research-doc weakness: "most Timneh pages are very short, focusing only on size and color."

### 2c. silvergatebirdfarm.com (SERP #5) — **confirmed cloaker**
Redirects real traffic to `recaptcha.cloud/?...host=silvergatebirdfarm.com` (Cloudflare turnstile → "HUMAN VERIFICATION FAILED"). Same behavior logged in the Congo Sprint 0. Google still ranks it #5 with a "$1,500–$3,500" price snippet. **Proof point for the scam-awareness section: even page-1 Timneh results include cloaking sites.**

### 2d. Classified aggregators (birdsnow / birdbreeders / hookbillsforsale)
Own #1–#2 by domain authority + listing volume, not content quality. Thin per-listing pages, phone/text CTAs, wild price scatter ($2,800–$8,500). We can't beat their listing volume; we beat them on **depth, trust, documentation, and one honest brand** a buyer can verify.

---

## 3. Our current position (GSC + Bing, on-disk exports)

| Query | GSC Position | Impr | Clicks |
|---|---|---|---|
| timneh grey parrot for sale | 83.68 | 22 | 0 |
| **timneh african grey for sale** (PRIMARY) | **96.67** | 3 | 0 |
| timneh grey for sale | 13.11 | 9 | 0 |
| timneh african grey parrot for sale | 15.75 | 8 | 0 |
| timneh parrot for sale | 74.25 | 8 | 0 |
| timneh for sale | 70.67 | 3 | 0 |
| african grey timneh for sale | 92.0 | 3 | 0 |
| timneh african grey vs congo price | 67.0 | 1 | 0 |

- **The for-sale page is effectively invisible on its own primary term (pos ~97).** The better-ranking variants (13–16) are being carried by other pages.
- **Cannibalization flag:** our **`/congo-vs-timneh-african-grey/` comparison page** is the real Timneh performer — Bing pos **6.7 (42 impr)**, GSC pos **7.6 (10 impr)** — while the for-sale page sits at Bing pos 4 / **2 impr** and GSC pos 11 / 1 impr. **Strategy must rank the transactional page WITHOUT stealing the comparison page's decision-query equity** → "Congo vs Timneh" stays a *teaser H4 → link*, never a deep comparison block here (comparison page owns it; same guard we used on Congo).

---

## 4. Keyword universe (GSC + research doc + SERP-mined)

- **Primary:** timneh african grey for sale
- **Commercial:** buy timneh african grey · baby timneh african grey · timneh breeder USA · hand raised timneh · timneh african grey price · timneh grey parrot for sale · timneh parrot for sale
- **Long-tail:** timneh african grey breeder · timneh african grey near me · timneh african grey online · baby timneh african grey USA · timneh african grey Texas · timneh african grey for sale near me · how much does a timneh african grey cost
- **Comparison (teaser→link only):** timneh vs congo · timneh african grey vs congo price · which is better congo or timneh · is a timneh calmer than a congo
- **Semantic/NLP:** smaller African Grey · charcoal grey · maroon tail · horn-colored upper beak · early talker · Psittacus timneh · Ivory Coast / Liberia origin · confident · adaptable · foraging · positive reinforcement · family companion · avian enrichment · feather-picking (community term) · 40-50 year lifespan
- **Transactional:** reserve · deposit ($200) · available now · DNA-sexed · CITES documented · nationwide shipping · airport pickup / home delivery · Midland TX pickup

## 5. Community / AEO signals (SERP snippets — fetched; thread bodies NOT FETCHED)
- **Temperament (genuine split — use honestly):** "Timneh more *stable* in temperament, less prone to *feather picking*" (r/parrots) vs "Timnehs are *nervous little things*, amazing mimics" (IG). Congos = "more stand-offish / sensitive to change."
- **Speech:** "Timnehs start making noises / talking *earlier* but aren't as *prolifically* talkative as Congo; clearer voice."
- **Cost sentiment:** "$700 adult rescue → $6,000–$8,000 young"; "close to $80k over 19 years" lifetime (r/parrots African Grey Cost). Confirms our honest-price + true-lifetime-cost angle.
- **Decision:** active FB/Reddit "leaning toward a Timneh… read a lot of positive things" — pro-Timneh buyers seeking reassurance.

## 6. What NO Timneh competitor does (the moat, ranked)
1. **US-only, CITES-honest shipping** while a page-1 rival brags illegal 24-hour international export.
2. **Real, documented, named available birds** (Elad + Evie) with per-bird Product/Offer schema + video — vs 0–1 birds and no schema.
3. **Scam-protection module** naming the exact SERP red flags (cloaker at #5, international-24h at #7, $750 bait) → links scam cluster.
4. **Verifiable EEAT** — USDA AWA license, Midland-TX address, breeder story, avian-vet PBFD/APV PCR screening, DNA cert, closed band.
5. **EEBP-structured proof rows** (Entity→Evidence→Benefit→Purpose) = citation-friendly for AI Overviews/Perplexity where competitors have marketing fluff.
6. **Honest temperament nuance** (address the "nervous vs calm" split competitors gloss over) = trust + featured-snippet capture.
7. **Full H1→H6 depth + FAQPage schema** vs 6-Q flat FAQs.

## 7. Price landscape (for the price-explainer section)
$800 (scam-cheap / bait) → $950–$1,400 (low; exoticparrotpetstore, handraredparrots, exoticglobalparrots) → **$1,500–$1,600 (C.A.Gs — honest low-credible)** → $2,000–$3,500 (africangraysales regular, silvergate, credible mid) → $6,500–$8,500 (birdbreeders/hookbills/parrotcrown — inflated/premium). **Our Elad $1,600 / Evie $1,500 sit at the credible floor** — frame the sub-$1,000 zone as the red-flag tell, and the $6k+ zone as marked-up classifieds.

## 8. Cannibalization guard (binding for the outline)
- **`/congo-vs-timneh-african-grey/`** (comparison cluster) owns deep "Congo vs Timneh" decision content → here it's a teaser H4 + link only.
- **`/timneh-african-grey-parrot-for-sale/`** vs any Timneh variant/attribute pages → distinct geo set + headers (dup-gate `--headers` before outline approval AND at final pass).
- Bird detail lives on `/available/elad/` + `/available/evie/` → cards here link out, don't re-teach (single Product/Offer per bird there; this page uses card-level Offer, no AggregateOffer unless we group).

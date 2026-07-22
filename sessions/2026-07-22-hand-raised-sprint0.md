# Sprint 0 — Deep Competitor & SERP Research
## Page 4: `/hand-raised-african-grey-parrot-for-sale/`
**Date:** 2026-07-22 · Primary keyword: **hand raised african grey parrot for sale**
Method: Firecrawl live SERP (Google, US-geo) + research-recency ladder for blocked sites (Reddit/FB/IG/YT) + local GSC/Bing mining + `data/competitors.json` (30 registry).
Status: **DELIVERABLE — awaiting breeder review before Sprint 0.5.**

---

## 0. Local demand (our own GSC, extracted 2026-07-19)
The page is **buried** — 0 clicks, 1 impression, **position 71**. Winnable head + long-tails, none owned by us:
| Query | Impr | Pos |
|---|---|---|
| hand reared african grey | 4 | 93 |
| hand raised african grey for sale | 1 | 44 |
| hand raised parrots for sale | 1 | 4 |
| tame african grey parrot | 1 | 58 |
| baby african grey parrot for sale | 9 | 69.8 |
| young african grey parrots for sale | 9 | 55.2 |

**Cannibalization guard:** the strong `baby …` cluster belongs to the future `/baby-african-grey-parrot-for-sale/` page. This page owns **hand-raised / hand-fed / hand-reared / tame / socialized / people-bonded** intent — the *raising METHOD*, spanning BOTH Congo + Timneh (not a subspecies page). Bing query export still missing (open flag #3 from component map; supplied Bing CSV is page-traffic, not queries — noted, not fabricated).

---

## 1. Google SERP — top 10 (primary keyword, US)
| # | Domain | Read |
|---|---|---|
| 1 | exoticglobalparrotsfarm.com/product/… | "6-mo hand-fed & hand-tamed"; single product page ranking; scam-pattern |
| 2 | birdbreeders.com (classified) | "$8,500" hand-feeding Congo; Tier-2 aggregator |
| 3 | **buyafricangreyparrots.com** | **EXACT-MATCH THREAT** — H1 = "Hand-Raised African Grey Parrots For Sale", USDA-FL Shopify (teardown §4) |
| 4 | facebook.com/the exotic bird shop | FB business post |
| 5 | birdsnow.com/africangreyparrot | classified; "$6,500 hand raised & hand fed" |
| 6 | graybreedersfoundation.yolasite | thin Yola site, "ADOPT NOW"; low authority |
| 7 | handraredparrots.com | exact "hand reared" domain; multi-species fake-farm (teardown §4) |
| 8 | royalbirdcompany.com | "Handfed Baby African Grey Parrots"; old-web breeder |
| 9 | youtube.com — "How Much Do African Greys REALLY Cost?" | video, cost-intent |
| 10 | exoticparrotpetstore.com/…/african-grey | Tier-1 registry competitor; sale pricing |

**SERP read:** no single dominant authority. Top slots split between (a) scam-pattern Shopify/WordPress stores with sub-floor pricing and (b) low-authority classifieds. **A real, credentialed, specialist breeder page with genuine EEAT can rank.**

---

## 2. Blocked-platform sweep (research-recency ladder — real threads only)

### Reddit — top 10 (decision + welfare + scam)
- r/parrots **"Should i buy African Grey raised by its parents or [hand-raised]"** ← the exact decision query. Top comment nuance: *"many think hand-raised birds go along with everything because they're so tame — often [not the case]."*
- r/parrots "why so many Greys end up in rescue" — *"if Greys are not hand reared… they tend to be very vindictive."*
- r/parrots "I just adopted an AG today" — *"not weaned, not socialized — no excuse for taking a bird this age from its parents."* → **unweaned danger.**
- r/parrots "14 reasons to scare you out of a parrot" — *"hand-raising means they're tame, yes, but also means they don't know how to parrot."* → the over-hand-rearing nuance.
- r/AfricanGrey "legitimate website to [buy]" — *"$8,000 is insane; got mine for $1,400."* → price-anxiety.
- r/berlin ringneck — "parent raised or non-imprinted hand raised… tame but worth it."
- + welfare/regret threads (r/parrots "one of the worst decisions").

**Reddit takeaways:** (1) huge **decision anxiety** hand-raised vs parent-raised; (2) **welfare literacy** — buyers now know pulling too early / unweaned = bad; (3) **scam + price** fear; (4) honest nuance we can OWN: hand-raised done *right* (co-parented, weaned 12–16 wk, socialized across a household) vs done *wrong* (pulled early, over-bonded, neurotic).

### YouTube — top 10
Care routines, chick-growth vlogs, India/Tamil "hand tame birds for sale" sellers. **No US breeder owns "hand raised african grey for sale" video intent.** → our Roys eating + Jins & Jeni videos capture an empty lane.

### Facebook — top 10 (demand + scam-fear)
Almost all **groups**, not stores: *"Any hand reared baby african grey for sale please?"*, *"Cost of hand fed baby African grey?"*, *"Where to buy… it's been an impossible search and a ton of scams 😭."* → validates the **Trust-First / anti-scam** spine and the "what does hand-fed actually cost" price-transparency section.

### Instagram — top 10 (breeder pricing chaos)
renes_exotic_parrots (CA), plus reels: pricing all over the map — **$175?!, $2,850 red-factor, $4,900–$5,200 "hand-raised well-socialised"**, "raised with love since 12 weeks old." Flat multi-species pricing = scam pattern. → our **honest $1,500 floor + real per-bird pricing** stands out.

---

## 3. Competitor teardowns (reverse-engineered section architecture)

### 3a. buyafricangreyparrots.com (#3 — the exact-match threat) — Shopify, USDA-FL
**Section spine:** Hero (H1 "Hand-Raised African Grey Parrots For Sale") → "Why Families Trust Our Aviary" (4 cards: Hand-Raised Daily / Vet Checked / Safe Nationwide Shipping / Lifetime Support) → About Our Aviary → **Available Now** (bird cards + price) → Why African Greys (5 traits) → 1-Year Health Guarantee → Shipping & Delivery (3 steps) → CTA → **Congo vs Timneh** explainer → footer link hub.
**Weaknesses = our openings:**
- Prices **$800–$1,300** for weaned Congos → **below our $1,500 scam floor** (our own framework says this signals wild-caught/sick/nonexistent). We can *name* this.
- Shipping = vague *"trusted pet transport partners"* — **no airline, no IATA, no crate spec**. We name Delta/United cargo, IATA LAR, $185/$350 tiers.
- **No CITES** anywhere. **No named DNA lab.** **No real breeder names or faces** (stock Shopify photos).
- "1-Year Health Guarantee" only; generic.

### 3b. handraredparrots.com (#7) — WooCommerce, multi-species
Congo + Timneh + cockatoo + macaw + amazon, **identical boilerplate per product** ("hand-raised, tame, accustomed to human interaction"). Phone "N/A", "Contact Breeder" only. Congo $1,400–1,500. → textbook **anonymous fake-farm / flat multi-species** pattern our scam module targets. Exact "hand reared" domain is its only real asset.

### 3c. 30-competitor registry (`data/competitors.json`)
Tier 1 direct breeders (11): Afri Grey, Exotic Parrot Pet Store, Afro Birds Farm, African Gray Parrots For Sale, **Silvergate Bird Farm** (confirmed cloaker→recaptcha.cloud per Timneh sprint), Birds For Sales, Exotic Parrots Planet, Williams African Greys, Shades of Greys, African Grey Aviaries, Compound Exotics. Tier 2 classifieds (8): BirdsNow, Bird Breeders, Quality Birds Online, Hoobly, Petzlover, Parrot Alert, Pet Classifieds, Exotic Pets Avenue. Tier 3 informational (9): Spruce Pets, Wikipedia, Rational Parrot, All About Parrots, Small Animal Advice, Vet Explains Pets, Bird Addicts, Parrot Website. Tier 4 marketplaces (3): Chewy, Petfinder, Marietta Bird Shop.
**Universal gap across all tiers:** none teaches **hand-FED vs hand-RAISED**, proper weaning windows, or the welfare science of *correct* hand-rearing. They use "hand-raised" as a buzzword, never as demonstrated expertise.

---

## 4. THE MOAT (information-gain competitors lack)
1. **"Hand-fed ≠ hand-raised ≠ properly hand-raised."** Own the definition. Info-gain SERP (IVIS, parrotlife, parrotcarecentral, avianavenue) proves demand; no *selling* page covers it.
2. **Proper hand-rearing protocol as EEAT** — co-parented, weaned 12–16 wk (never pulled early/unweaned — the exact welfare failure Reddit calls out), socialized across a household so the bird isn't a one-person over-bonder.
3. **Honest downside** (non-commodity): hand-raised birds *can* over-bond / need companionship — and here's how we prevent it (rotate handling from day one). No competitor admits this.
4. **Real verifiable proof** vs the sub-floor scam pattern: named breeders (Mark & Teri), real bird videos, CITES Appendix I, named DNA lab, IATA Delta cargo, $1,500 honest floor.
5. **Spans both subspecies** — hand-raised Congo (Amie/Bery) + hand-raised Timneh (Elad + baby) under one method umbrella; cross-links to congo-for-sale + timneh-for-sale (no cannibalization — different intent).

---

## 5. Recommended section grouping (for breeder approval — Sprint 1 will formalize into the distribution matrix)

### A. MANDATORY (core for-sale + locked kit)
Hero · counter strip · TOC/dial + rail · what "hand-raised" means (definition) · available hand-raised birds (Avail-B/C) · price transparency + $1,500 floor · shipping tiers ($185/$350 + Midland pickup) · health guarantee + PBFD/APV PCR · every-bird-leaves-with doc stack · FAQ (PAA) · 2 buyer reviews (Stanley + Jesse) · contact/reserve form · seam dividers · Keep-reading resources · location shipping block.

### B. COMPETITOR-BASED (match/beat top rankers)
- "Why families trust our hand-raised greys" 4-card trust block (beats buyafricangreyparrots' version with CITES + named lab + IATA).
- "Why African Greys" intelligence/talking/bonding traits (table stakes — every ranker has it).
- Congo vs Timneh mini-explainer → teaser links to the two variant pages (buyafricangreyparrots has it; we do it better + link out).
- Nationwide shipping process, but **named** (Delta/United, IATA LAR, crate spec) — direct counter to their vague "pet transport partners."

### C. SUGGESTED / RECOMMENDED (our moat — the info-gain competitors lack)
- **"Hand-fed vs hand-raised vs parent-raised"** comparison (the definitional moat + a GEO fact table).
- **"How we hand-raise a grey — weaning timeline 12–16 wk"** process/EEAT block (co-parented, socialized) — answers the unweaned-danger welfare anxiety.
- **"The honest downside of a hand-raised grey (and how we prevent over-bonding)"** — non-commodity trust.
- **Scam module** reframed for hand-raised: sub-$1,500 "hand-raised" listings, flat multi-species farms, no-weaning-date sellers → links scam cluster.
- **YouTube proof block** (Roys/Jins&Jeni videos) — capture the empty video lane.

---

## 6. Framework blend (locked to EEBP + this page's spine)
Spine = **Trust-First / welfare-authority**. Blend: **EEBP** (Entity→Evidence→Benefit→Purpose, per breeder mandate + `framework-eebp`) as the paragraph engine · **PAS** (scam/welfare anxiety) · **BAB** (parent-raised-flighty → hand-raised-bonded transformation) · **QAB** (FAQ) · **AIDA** (money-page arc). EEBP example opener for a bird card: *"Amie (entity) is a hand-raised Congo hen we weaned ourselves at 14 weeks and socialized across our household (evidence); she steps up for strangers and doesn't panic-bond to one person (benefit), which is why she suits busy family homes rather than a single quiet owner (purpose)."*

## 7. Distinctness guard (tuple must differ from egg/congo/timneh)
Prose written **fresh from this page's outline** (Write-From-Outline). Component tuple must NOT repeat egg/congo/timneh slots (Sprint 1 will lock it). Candidate leaning: an **unused hero** (Hero-A Scattered Flock or Hero-C Mosaic Metrics — both untouched; the money-variant default Split-Hero B is now "used twice", so differentiate hard) + unused TOC (T2 Chip Cloud / T4 Magazine Index) + unused takeaway slot + Table B/C + a differentiated FAQ. Final picks → Sprint 1 with Recommend+Why.

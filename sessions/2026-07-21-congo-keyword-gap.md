# Keyword-Gap Analysis — `/congo-african-grey-for-sale/` REBUILD

**Date:** 2026-07-21
**Target query:** "congo african grey for sale" (transactional, buyer intent)
**Page under rebuild:** https://congoafricangreys.com/congo-african-grey-for-sale/
**Method:** fresh SERP (Firecrawl `firecrawl_search`, US) → scrape ranking competitor pages → extract topic/H-pattern coverage → diff vs our current `dist/` output → cross-check sibling inventory so no recommended gap duplicates a page a sibling already owns.

> **Data-integrity note (CLAUDE.md):** Every gap below points to a competitor page I actually fetched, or to a SERP snippet I actually retrieved. Where a competitor page could not be fetched it is marked **NOT FETCHED** and is NOT used to justify a score. No search-volume numbers are invented — scores use only the observable-signal rubric.

---

## Fetch log — competitor pages ranking for "congo african grey for sale"

| # | URL | SERP pos | Fetch result |
|---|-----|----------|--------------|
| 1 | birdbreeders.com/birds/african-grey-congo-parrot | 1 | SERP snippet only (listing grid, prices $400–$8,500, DNA-tested males/females, "hand feeding baby") — grid page, no prose to scrape |
| 2 | graybreedersfoundation.yolasite.com/Order-Now.php | 2 | Not fetched (Yola order page, low-authority; SERP shows $1,500 Congo) — **NOT FETCHED** |
| 3 | birdsnow.com/africangreyparrot.htm | 3 | SERP snippet only (classified listings, "DNA test female $3,600", "first come first serve") |
| 4 | mybabyparrot.com/African_Grey (Parrot Wizard) | 4 | ✅ **FETCHED FULL** — richest competitor page |
| 5 | birdbreeders.com/birds/category/african-grey-parrots | 5 | SERP snippet (same registry) |
| 6 | silvergatebirdfarm.com/product/congo-african-grey-for-sale/ | 6 & 11 | ❌ **NOT FETCHED** — hard Cloudflare Turnstile, basic **and** stealth proxy both failed. Have SERP snippet only: price range "$1,500–$3,500", "Well Trained and Handfed Birds" |
| 7 | birdsbyjoe.com/african-grey | 7 | ✅ **FETCHED FULL** |
| 8 | exoticparrotpetstore.com/product-category/african-grey-parrot/ | 8 | ✅ **FETCHED FULL** |
| 9 | featheredfriendshub.com/shop/ | 9 | SERP snippet only (shop grid, "AFRICAN GREY CONGO $1,200–$2,400") |
| 10 | instagram.com/reel/... | 10 | Skipped (social reel, not a page) |
| 11 | afrigreyparrots.com (Tier-1 registry breeder, ranks for this cluster) | — | ✅ **FETCHED FULL** (homepage + how-to-buy funnel) |

**Fetched full: 4** (mybabyparrot, birdsbyjoe, exoticparrotpetstore, afrigreyparrots)
**SERP-snippet only: 4** (birdbreeders ×2, birdsnow, featheredfriendshub, silvergate)
**NOT FETCHED (blocked/skipped): 3** (silvergate = Cloudflare Turnstile; graybreedersfoundation; instagram)

---

## What our current page actually covers (from `dist/congo-african-grey-for-sale/index.html`)

Our page is a **thin stub** — 143 source lines, **only 2 H2s**, **zero H4/H5/H6** (fails the Heading Hierarchy Gate), no FAQ, no bird cards, no inquiry form, no shipping section.

- H1: "Congo African Grey For Sale"
- Hero: eyebrow "Psittacus erithacus · CITES Appendix I Captive-Bred" + intelligence/size/vocabulary blurb + one CTA link to `/contact-us/`
- TrustBar component
- One Congo-vs-Timneh comparison infographic (400px)
- H2 "About the Congo African Grey" → Species Profile list + static Pricing list (baby $3,000 / adult $1,500 / pair $2,700 / deposit $200)
- H2 CTA "Ready to Bring Home a Congo African Grey?"
- Product (AggregateOffer $1,500–$3,000) + Organization schema

**Missing entirely on-page:** bird cards, reserve/inquiry form, shipping tiers, how-to-buy steps, health-guarantee section, talking/training, FAQ, CITES-documentation trust section, scam-safety, diet/weaning, near-me geo, reviews, financing/payment, counter-snippets. This is far below the `cag-for-sale-page-builder` 22-section transactional standard.

---

## Sibling-ownership cross-check (so recommendations are section+link, not duplication)

| Deep topic | Sibling page that OWNS it | Implication for this page |
|---|---|---|
| Shipping / IATA delivery | `/buy-african-grey-parrots-with-shipping/` (LIVE) | Add a shipping-tier **summary** section + link |
| Health guarantee | `/african-grey-parrot-health-guarantee/` + `/african-greys-for-sale-with-health-guarantee/` | Short guarantee snippet + link |
| Price / cost of ownership | `/african-grey-parrot-price/` (Congo $1,700–$2,500) | Keep on-page price table, link out for full cost |
| Near-me / geo | `/where-to-buy-african-greys-near-me/` + 40+ state/city pages | Ships-to geo block + links, no deep duplication |
| Baby / hand-raised | `/baby-african-grey-parrot-for-sale/`, `/hand-raised-.../` | Bird cards can be baby-led; link for deep baby content |
| DNA / captive-bred / CITES | `/dna-tested-...`, `/captive-bred-...`, `/cites-african-grey-documentation/` | Trust snippet + link |
| Congo vs Timneh | `/congo-vs-timneh-african-grey/` | Keep infographic as teaser, link for deep comparison |
| Congo pair | `/congo-african-grey-parrot-pair-for-sale/` | Pair price row + link |
| Scams | `/how-to-avoid-african-grey-parrot-scams/` | Buy-safely snippet + link |
| Reviews | `/african-grey-reviews/` + `/testimonials/` | Reviews strip + link |
| Live inventory | `/available/` (9 bird pages) | **Surface real bird cards here** |

---

## GAP MATRIX (sorted by opportunity score, 1–10)

Rubric: competitor dedicated page/section +3 · topic in competitor top pages +2 · not on THIS page +3 (reduced to +1/+2 where a sibling already owns the deep page) · transactional/buyer intent +2.

| # | Gap topic / keyword | Competitor(s) with it (fetched) | Our coverage (this page) | Intent | Score | Recommended section |
|---|---|---|---|---|---|---|
| 1 | **Available bird cards** — named birds, photo, sex, age, price, status | exoticparrotpetstore (9 named cards + ratings + sale prices), birdbreeders (12+ listings $400–$8,500), mybabyparrot | **No** (static price list only; `/available/` not surfaced) | Transactional | **10** | "Available Congo African Greys" card grid near fold; pull from `data/clutch-inventory.json`; Product/Offer per bird (sold≠InStock); shipping line on every card |
| 2 | **Reserve/deposit flow + inquiry form listing real birds & prices** | mybabyparrot (waiting list + deposit + "Birdie Shower"), afrigrey (4-step add-to-cart) | **No** (only a link to `/contact-us/`) | Transactional | **10** | Inline reserve form (real birds + prices + "Pickup in Midland, TX within 2–3 hrs"); reserve CTAs every 500–700 words |
| 3 | **How-to-buy / reservation process steps** | afrigrey (4-step Browse→Cart→Pay→Deliver 48h), mybabyparrot (deposit→delivery→transition day) | **No** | Transactional | **10** | "How to Buy a Congo African Grey From Us" numbered process |
| 4 | **Shipping & nationwide delivery tiers** | mybabyparrot (personal delivery + transition day), birdsnow | **No** on page (sibling owns) | Transactional | **9** | Shipping section: Airport $185 / Home $350, IATA LAR, Delta/United/American + link |
| 5 | **Health guarantee ("beak to tail" / vet cert)** | mybabyparrot (beak-to-tail guarantee) | Partial (one line in About) | Trust/Transactional | **9** | Health-Guarantee snippet + 72-hr window + link to guarantee page |
| 6 | **CITES documentation & legal-to-own (our MOAT)** | Competitors mostly absent; afrigrey uses risky payment, exoticpetsavenue = scam | Hero eyebrow only | Trust (CITES = HIGH PRIORITY) | **8** | "CITES Appendix I — Legal to Own With Our Paperwork" trust section; captive-bred-USA framing |
| 7 | **Talking ability / training (target, step-up, harness, flight-recall)** | mybabyparrot (deep: 4 trained skills + harness + socialization) | Hero mention only | Info→buyer | **8** | "Are Congo African Greys Good Talkers?" + our hand-raising/socialization |
| 8 | **FAQ (PAA: how much, lifespan, good pet, do they talk, legal)** | Thin on competitors but high PAA demand; birdsbyjoe/afrigrey partial | **No FAQ** | Informational | **8** | FAQ section + FAQPage JSON-LD (visible) |
| 9 | **Buy-safely / verify-a-legit-breeder (scam avoidance)** | mybabyparrot (explicit scam-warning + buyer protection block) | **No** (sibling owns) | Trust | **8** | "Buy Safely" snippet contrasting our docs vs no-paperwork sellers + link |
| 10 | **Diet / weaning / food (weaned, varied diet, pellet brands)** | mybabyparrot (deep food list + Harrison's/Roudybush/TOP's/Zupreem) | **No** on page (sibling owns) | Info→buyer | **8** | "What We Feed / Fully Weaned" snippet + link to `/african-grey-parrot-diet/` |
| 11 | **Pricing detail / what determines Congo price** | silvergate ($1,500–$3,500, SERP), birdbreeders ($400–$8,500), exoticparrotpetstore, featheredfriendshub ($1,200–$2,400) | Partial (static table) | Transactional | **8** | Expand pricing + "What Determines a Congo's Price" + link to price page |
| 12 | **Near-me / where-to-buy geo** | birdsnow, hoobly, petfinder (near-me SERP intent) | **No** on page (sibling owns) | Transactional | **8** | Geo "We ship to…" state block + links to top state pages |
| 13 | **Financing / payment terms** | mybabyparrot (PayPal 0% 6-mo financing), afrigrey (payment methods) | **No** | Transactional | **8** | Deposit + safe-payment terms (differentiator: we counter afrigrey's CashApp/PayPal-F&F red flag) |
| 14 | **Reviews / ratings / social proof** | exoticparrotpetstore (per-bird 4.5+ ratings) | **No** (sibling owns) | Trust | **7** | Reviews strip (real buyers only) + link to `/african-grey-reviews/` |
| 15 | **Congo identification / appearance (red tail, size, blushing)** | birdsbyjoe (deep physical), afrigrey | Partial (profile list) | Informational | **7** | Expand "How to Identify a True Congo" |
| 16 | **Counter-snippet vs "cheap African grey"** | afrigrey (leans hard "cheap"), exoticpetsavenue scam ($650) | **No** | Trust/CRO | **6** | Counter snippet: why a documented Congo ≠ a $650 "cheap" bird |
| 17 | **Red / red-factor Congo variant** | afrigrey ("Cheap Red Congo African Grey") | **No** | Niche transactional | **5** | Monitor only — verify legitimacy before building (afrigrey listing looks scammy); low real demand |
| 18 | **Congo vs Timneh comparison** | birdsbyjoe, afrigrey | **Yes** (infographic) | Info | **3** | Keep infographic as teaser; link to `/congo-vs-timneh-african-grey/` |
| 19 | **Lifespan / long-term commitment** | (infographic-level on competitors) | Partial (infographic) | Info | **3** | Covered; light expansion only |

---

## Must-build sections (score ≥ 7) — route to `cag-content-architect` / `cag-for-sale-page-builder`

Rows 1–15 all score ≥7. In priority order for the rebuild:

1. Available Congo bird-card grid (10) — the single biggest gap; competitors lead with inventory, we lead with a static table.
2. Reserve/inquiry form with real birds + prices (10)
3. How-to-buy process steps (10)
4. Shipping & delivery tiers (9)
5. Health-guarantee section (9)
6. **CITES documentation / legal-to-own (8 — HIGH PRIORITY, compliance/trust moat)**
7. Talking ability / training (8)
8. FAQ + FAQPage schema (8)
9. **Buy-safely / anti-scam (8 — HIGH PRIORITY, trust)**
10. Diet / weaning (8)
11. Pricing "what determines price" (8)
12. Near-me geo block (8)
13. Financing / safe-payment terms (8)
14. Reviews strip (7)
15. Congo identification detail (7)

**CITES + trust flags (rules 4):** Rows 6, 9, 13 are the compliance/trust moat. Competitors either omit CITES entirely or actively signal scam behavior (afrigrey's CashApp/PayPal-Friends&Family "48-hour delivery", exoticpetsavenue's $650 undocumented birds). Our documented, captive-bred, CITES-Appendix-I positioning is a genuine differentiator — build these as prominent trust sections, not footnotes.

**Heading-Gate reminder:** the rebuild must satisfy the Heading Hierarchy Outline Gate (all six levels, ≥5 H5 AND ≥5 H6, no skips) — current page has only 2 H2 and nothing below H3.

**Dup-content reminder:** rows 4, 5, 10, 11, 12, 14 are owned deep by siblings — build **summary + Link-First anchor**, run `cag-duplicate-content-gate` before outline approval and at final pass vs the whole for-sale + comparison cluster.

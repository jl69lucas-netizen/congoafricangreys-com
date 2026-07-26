# Sprint 0 — Congo African Grey For Sale: Competitor Intelligence (REBUILD)

**Target page:** https://congoafricangreys.com/congo-african-grey-for-sale/ (on disk: `src/pages/congo-african-grey-for-sale/index.astro`)
**Core keyword:** `congo african grey for sale` (transactional / commercial-purchase intent)
**Run date:** 2026-07-21
**Engines/sources used (live this session):** Firecrawl `firecrawl_search` (Google-style, US locale) ×5 · Firecrawl `firecrawl_scrape` (16 competitor pages + 2 Bing SERPs + 2 schema extractions) · Playwright (Bing SERP ×3)
**Data-integrity rule applied:** Only live-fetched data is reported as fact. Blocked/dead pages are marked **NOT FETCHED**. No price, ranking, quote, or metric is invented.

---

## 0. Fetch Ledger (transparency)

### Registered 30 — live signal obtained THIS session
| # | Competitor | Result this session | Congo/for-sale data captured |
|---|---|---|---|
| 1 | exoticparrotpetstore.com | ✅ DEEP fetched | 9 AG products, prices $800–$3,800, Congo $1,300 |
| 2 | birdsnow.com | ✅ DEEP fetched | 576 AG ads, full state footprint, $2,200–$8,500 |
| 3 | birdsforsales.com | ✅ DEEP fetched | Named birds $730–$850, long SEO body |
| 4 | afrigreyparrots.com | ✅ DEEP fetched | "Cheap" Congo, PayPal F&F, 48h delivery |
| 5 | shadesofgreys.com | ✅ DEEP fetched | Fifty Shades of AG, MN, sold-out |
| 6 | exoticparrotsplanet.com | ✅ DEEP fetched | Congo "Alpha" $800, intl shipping, eggs+incubators |
| 7 | birdbreeders.com | ✅ Fetched via search + Bing | 27 Congo listings, $400–$8,500 live prices |
| 8 | compoundexotics.com | ✅ Fetched (oversized 156KB, not fully parsed) | Multi-species exotic store |
| 9 | africangrayparrotsforsale.com | ⚠️ Fetched → **ACCOUNT SUSPENDED (Bluehost)** — now dead | EMD competitor is OFFLINE |
| 10 | silvergatebirdfarm.com | ❌ **NOT FETCHED** — cloaking redirect to `recaptcha.cloud` (basic + stealth both failed) | SERP snippet only: ranks #6, $1,500–$3,500 |
| 11 | petzlover.com | ❌ **NOT FETCHED** — CAPTCHA wall (registry-confirmed); Bing confirms it ranks (FL, 37+ listings) | — |
| 12 | qualitybirdsonline.com | ❌ **NOT FETCHED** — all Firecrawl engines failed (blocking/down) | — |

### Registered 30 — NOT re-fetched this run (assessed via registry notes + live SERP appearance)
- **Known dead/negative (intentional skip):** afrobirdsfarm (HTTP 522 dead, registry-confirmed) · exoticpetsavenue (confirmed scam — illegal eagle-egg/primate listings) · parrotalert (reclassified: non-commercial lost-&-found registry, backlink target not competitor).
- **Inaccessible/inactive (registry):** williamsafricangreys (inaccessible) · africangreyaviaries (inactive).
- **Tier 3 informational (not transactional "for sale" competitors):** thesprucepets, wikipedia, rationalparrot, allaboutparrots, smallanimaladvice, vetexplainspets (registry: revised to LOW), birdaddicts, parrotwebsite.
- **Tier 4 marketplace/retail:** chewy (supplies only, no live birds) · petfinder (adoption DA play) · hoobly (classifieds) · mariettabirdshop (GA shop, AG $1,000 per registry).

### Fresh (non-registered) competitors fetched DEEP this session
mybabyparrot.com (Parrot Wizard) · birdsbyjoe.com · theavianexchange.com · buyafricangreyparrots.com · birdsjungle.com · graybreedersfoundation.yolasite.com · featheredfriendshub.com

### Fresh competitors captured via SERP/snippet only (not deep-fetched)
royalbirdcompany.com · exoticglobalparrotsfarm.com · glitzbirds.com · birdandbeyond.com · forestryparrotsbreeder.com · goldencockatoo.com · parrotcrown.com · anasparrots.com · parrotsaleshop.com (Parrot Palace) · parrotoutreachsociety.org (rescue/backlink) · omarsbirds (FB, CA) · renes_exotic_parrots (IG, CA)

**Bottom line:** Of the 30 registered, **9 returned fresh first-hand content**, **1 confirmed newly dead** (africangrayparrotsforsale — suspended), **3 confirmed blocked/down** (silvergate, petzlover, qualitybirdsonline), and **17 were assessed from registry + live SERP** rather than re-fetched (nearly all are Tier-3 info or Tier-4 marketplace, i.e., not transactional Congo-for-sale rivals). On top of that, **7 fresh competitors were fetched deep** and ~12 more captured via SERP — the real competitive set for this keyword is materially larger and different from the 2026-04 registry.

---

## 0a. Staleness audit of existing research (`RESEARCH-DATA-FOR-SALE-PAGES.md`)

- **PAGE 2 — "Congo African Grey For Sale" (line ~313):** On-target but **thin and ungrounded**. It is generic ChatGPT output (`?utm_source=chatgpt.com` citations, zero live prices, zero real competitor URLs, no SERP). Its content architecture (Hero→Available→Why Congo→Temperament→Talking→…→FAQ→Reserve) is directionally fine and still usable, but every "why competitors rank," price, and entity claim in it is unverified. **Keep the skeleton; replace the substance with the live data below.**
- **"PHASE 2 — Top Competitor Reverse Engineering" (line ~7550): OFF-TARGET / STALE for this rebuild.** It reverse-engineers the keyword **"African Grey Parrot Adoption *Cost*"** (an informational/cost query) and its competitors are SpectrumCare, All About Parrots, Parrot Care Central, PetsLoo (UK), Dubai Birds (UAE) — a *cost-guide* SERP, not the *transactional* Congo-for-sale SERP. **None of those are the real ranking rivals for `congo african grey for sale`.** Do not reuse that competitor list for this page. This report supersedes it for the transactional intent.

---

## A. SERP SNAPSHOT

### A1. Google-style organic (Firecrawl, US locale) — `congo african grey for sale`
| Pos | URL | Title | Type |
|---|---|---|---|
| 1 | birdbreeders.com/birds/african-grey-congo-parrot | African Grey Congo Parrots for Sale (27 listings) | Classified/directory |
| 2 | graybreedersfoundation.yolasite.com/Order-Now.php | Gray Breeders Foundation | Breeder (**likely SCAM** — see B) |
| 3 | birdsnow.com/africangreyparrot.htm | African Grey Parrots for Sale | Classified aggregator |
| 4 | mybabyparrot.com/African_Grey | Trained Congo African Grey Parrot Baby | Breeder/authority (Parrot Wizard) |
| 5 | birdbreeders.com/birds/category/african-grey-parrots | African Grey Parrots for Sale | Classified/directory |
| 6 | silvergatebirdfarm.com/product/congo-african-grey-for-sale/ | Congo African Grey for sale \| Well Trained | Breeder (**registered**; $1,500–$3,500) |
| 7 | birdsbyjoe.com/african-grey | Congo & Timneh African Grey Parrot for Sale | Breeder (NJ) |
| 8 | exoticparrotpetstore.com/product-category/african-grey-parrot/ | AFRICAN GREY PARROT | Breeder store (**registered**; Congo $1,300) |
| 9 | featheredfriendshub.com/shop | Featherland Breeders Hub | Breeder store ($1,200–$2,400) |
| 10 | instagram.com/reel/C6DU3_NxZiY/ | Congo African Gray Parrot For Sale | Social (IG reel) |

### A2. Google-style organic — `congo african grey parrot for sale`
Positions 1–8 nearly identical to A1 (birdbreeders #1, graybreedersfoundation #2, birdsnow #3, mybabyparrot #4, birdbreeders category #5, silvergate #6, birdsbyjoe #7, exoticparrotpetstore #8), **plus**:
- #9 **royalbirdcompany.com** — "handfed baby congo african grey parrots for sale" (**SOLD OUT**)
- #10 **theavianexchange.com/african-greys-for-sale** — "from Screened Breeders" (marketplace; a Parrot Stars Congo listed at **$8,500**, Arlington Heights IL)

### A3. Google-style organic — `baby congo african grey for sale`
| Pos | URL | Type |
|---|---|---|
| 1 | exoticglobalparrotsfarm.com/product/african-grey-baby-parrots-males-females/ | Breeder store |
| 2 | mybabyparrot.com/African_Grey | Breeder/authority |
| 3 | birdbreeders.com/birds/african-grey-congo-parrot | Classified |
| 4 | graybreedersfoundation.yolasite.com | Breeder (scam-flag) |
| 5 | birdbreeders.com/birds/category/african-grey-parrots | Classified |
| 6 | birdsbyjoe.com/african-grey | Breeder |
| 7 | royalbirdcompany.com | Breeder (SOLD OUT) |
| 8 | exoticparrotpetstore.com/product-category/african-grey-parrot/ | Breeder store (Baby AG $800) |
| 9 | silvergatebirdfarm.com/product-category/african-grey-parrots-for-sale/ | Breeder (registered) |
| 10 | theavianexchange.com/african-greys-for-sale | Marketplace |

### A4. Bing organic — `congo african grey [parrot] for sale` — ⚠️ ENTITY-HIJACK FINDING
Verified two independent ways (headless Playwright **and** Firecrawl stealth): Bing resolves both `congo african grey for sale` and `congo african grey parrot for sale` to the **country entity "Congo"** — all 10 organic results are Republic of the Congo / DR Congo pages (Wikipedia, Britannica, BBC, World Atlas, gov.uk, World Bank, Al Jazeera). Bing even appends a "Searches you might like → *african grey parrot for sale*" refinement. **This is real, reproducible Bing behaviour, not a scraping artifact.**
> **SEO implication:** On Bing, the phrase "congo … for sale" has strong country-entity gravity that buries commercial bird results. The page MUST aggressively disambiguate as a *parrot/bird* (words: "parrot," *Psittacus erithacus*, "bird," "breeder," "hand-raised") in title/H1/schema, or it will underperform on Bing. The clean commercial term on Bing is **"african grey parrot for sale."**

### A5. Bing organic — `african grey parrot for sale` (the disambiguated commercial term)
| Pos | Host | Title | Registered? |
|---|---|---|---|
| 1 | birdsnow.com (FL page) | African Grey Parrots for Sale in Florida | ✅ |
| 2 | exoticparrotpetstore.com | AFRICAN GREY PARROT – Exotic Parrot Pet Store | ✅ |
| 3 | birdsforsales.com | Africa Grey Parrots for Sale – Elegant 5-Star Birds USA | ✅ |
| 4 | birdsnow.com | African Grey Parrots for Sale | ✅ |
| 5 | petzlover.com (FL) | Healthy African Grey Parrot for Sale in Florida | ✅ |
| 6 | glitzbirds.com | African Grey Parrots for Sale in FL, TX, OH, MI, NJ | ❌ new |
| 7 | buyafricangreyparrots.com | African Grey Parrots for Sale – USDA Licensed FL Breeder | ❌ new |
| 8 | birdandbeyond.com | African Grey Parrot for Sale | ❌ new |
| 9 | birdbreeders.com (FL) | African Grey Parrots for Sale in Florida | ✅ |
| 10 | forestryparrotsbreeder.com | African Grey Parrots for sale ; Buy online | ❌ new |
> Bing skews to **Florida** results (proxy-geo) and rewards aggregators (birdsnow, birdbreeders, petzlover) + WooCommerce/Shopify stores. **congoafricangreys.com does NOT appear in Bing top-10 for either term.**

### A6. CAG visibility check
**congoafricangreys.com appears in NEITHER the Google (Firecrawl) NOR Bing top-10** for any of the three core queries. Our current page is effectively invisible for its own target keyword.

### A7. UGC / Social / Forum layer (real titles only)
**Reddit (fetched titles, r/parrots + r/AfricanGrey):**
- "Buying an African Grey. Advice needed" (r/parrots)
- "Strongly advised not to buy an African Grey" (r/parrots) — sensitivity/feather-plucking
- "Please can someone tell me a legitimate website to purchase an [African Grey]" (r/AfricanGrey) — *"insane amount of scams… I got mine for $1,400"*
- "Scam or not a Scam? Any tips on knowing if they're legit or not?" (r/parrots)
- "I try to purchase an African gray" (r/AfricanGrey) — *"Find a pet store or a breeder and go in person"*
- "Why are African greys so expensive all of a sudden?" (r/parrots) — *"$100 as a kid… now $6,000+"*
- "Trying to convince my friend NOT to buy an African Grey" (r/parrots)
- "is my mom getting scammed from this parrot breeder?" (r/isthisAI)

**YouTube / TikTok (fetched titles):** "I SPENT $13k on My African Grey Parrots \| Here's Why" · "Symon the African Grey Talking Baby Parrot" (2-yr female Congo) · playlist "My Pet Congo African Grey Parrot (Full Journey from Day 1)" · "This Parrot Can Cost Up to $25,000!!!" (Red Factor) · TikTok @jcaviary "Adorable Congo African Grey Parrot Babies Growing Up."

**Facebook (fetched):** omarsbirds "3 baby Congo African Grey babies available at Lake Forest **$6,499–$6,999**, call 949-472-3962" · bird-paradise-store "10-week Congo Juliet, DNA tested female, **PBFD negative**" · FB groups (semi-tamed pair **$900**, Western-Union-style private sales — scam-prone).

**Note (data-integrity):** Reddit blocks headless scraping of thread bodies; only SERP-returned titles/snippets are quoted above. Deeper thread mining should use the `reddit-strategy` skill's headless-browser flow.

> **The single loudest signal in the entire UGC layer is SCAM FEAR + PRICE CONFUSION.** The buyer's #1 pre-purchase question is not "which bird" — it's *"is this seller real, and why do prices swing from $800 to $8,500?"*

---

## B. PER-COMPETITOR REVERSE-ENGINEERING

### B1. Registered 30 — lighter pass (Congo-for-sale lens)
| Competitor | Tier | Ranks for Congo? | Why it ranks | #1 weakness we exploit |
|---|---|---|---|---|
| **birdbreeders.com** | 2 | **#1 Google** | Dedicated `/birds/african-grey-congo-parrot` node, 27 fresh dated listings w/ prices + "We Ship" + breeder city/state, high DA, constant freshness | No trust curation, no care/education, scam-prone private ads; per-listing depth ~1 line |
| **birdsnow.com** | 2 | **#1/#3** | 576 AG ads, full 35-state page footprint incl. all 22 CAG states, Congo+Timneh subpages, rich filters (Handfed/Talking/Tame), 2019 trusted domain | Classified board — no owned inventory, no health guarantee, thin per-ad, mixed-quality sellers |
| **silvergatebirdfarm.com** | 1 | **#6** (exact slug) | Exact-match slug `/product/congo-african-grey-for-sale/`, WooCommerce Product schema, price line $1,500–$3,500 | **NOT FETCHED — cloaking redirect to recaptcha.cloud**; hostile to crawlers = fragile; thin content behind the wall |
| **exoticparrotpetstore.com** | 1 | **#8 G / #2 Bing** | WooCommerce store, 9 named AG products, star ratings, "Sale!" urgency, Product schema | Add-to-cart for live CITES-I birds (scam pattern), reused "…-UK" stock photos, no CITES/USDA docs, thin content |
| **birdsforsales.com** | 1 | **#3 Bing** | 5 long AI-written SEO H2s (Congo vs Timneh, price, health guarantee, cost), external authority links (AAV/PetMD/Spruce), named birds | Calls AG "a Cockatoo species" (factual error), $730–$850 prices, keyword-stuffed South-African city terms, generic "Order" links |
| **afrigreyparrots.com** | 1 | Yes (Congo/Red Congo/Timneh) | WooCommerce, aggressive "cheap African Grey" keyword targeting, 4-step buy flow | **PayPal Friends&Family + CashApp + "48-hour delivery"** (scam signals), leftover demo-theme URL, no real docs |
| **exoticparrotsplanet.com** | 1 | Yes (Congo "Alpha" $800) | "Global leader since 1994," WooCommerce, Health Guarantee/Return/FAQ pages, visible FAQ, 4 AG products + eggs + incubators | Ships **internationally** (illegal for CITES-I pets), LA address + El-Paso (915) phone mismatch, stock photos, generic intl reviews |
| **shadesofgreys.com** (Fifty Shades of AG) | 1 | Low (brand) | Real MN hobby breeder, Wix, Delta shipping, appears as breeder on birdbreeders.com | **Sold out** ("all babies found families"), no pricing, no inventory, no schema, tiny footprint |
| **compoundexotics.com** | 1 | Low | Large multi-species exotic store (156KB page = big catalog) | Not AG-specialised; AG buried among many species (fetched but not fully parsed) |
| **africangrayparrotsforsale.com** | 1 | — | Exact-match domain (historically strong) | **DEAD — Bluehost "Account Suspended" as of this run.** EMD rival is offline → SERP opening |
| **williamsafricangreys.com** | 1 | — | Brandable AG domain | Registry: inaccessible; not verified live |
| **africangreyaviaries.com** | 1 | — | Niche aviary domain | Registry: inactive |
| **petzlover.com** | 2 | Yes (Bing #5, FL, 37+) | Free-classified scale, state pages | **NOT FETCHED (CAPTCHA)**; UGC listings, no curation |
| **hoobly.com** | 2 | Yes (near-me/price) | General-classified DA, large bird section | No AG depth, scam-prone, no trust layer |
| **qualitybirdsonline.com** | 2 | — | "Verified seller" claims | **NOT FETCHED (all engines failed)** |
| **petclassifieds.com** | 2 | Low | General pet classifieds | Registry: minimal AG depth |
| **exoticpetsavenue.com** | 2 | — | — | **Confirmed SCAM** (illegal eagle eggs/primates) — use as documented scam example, never a model |
| **parrotalert.com** | 2 | — | — | Non-commercial lost-&-found registry — **backlink target**, not competitor |
| **thesprucepets.com** | 3 | Info only | Dominant care/price authority | Not transactional — no birds sold; we win on commerce+local |
| **wikipedia.org** | 3 | Head term | Species article | Not commercial |
| **rationalparrot / allaboutparrots / smallanimaladvice / birdaddicts / parrotwebsite** | 3 | Info only | Care/comparison content | Not transactional; thin commercial intent |
| **vetexplainspets.com** | 3 | Low | Registry: revised MEDIUM→LOW (no dedicated AG pages) | Not an AG authority |
| **chewy.com** | 4 | Supplies | Retail DA (food/cages) | Sells no live birds |
| **petfinder.com** | 4 | Adoption DA | High DA on for-sale/near-me | Adoption model, rarely lists Congos; we win on availability+breeder trust |
| **mariettabirdshop.com** | 4 | Regional (GA) | Physical shop, AG $1,000 | Single-region, thin site |
| **afrobirdsfarm.com** | 1 | — | — | **Dead (HTTP 522), registry-confirmed** |

### B2. Fresh top-10 — DEEP reverse-engineering (the real transactional rivals)

**① birdbreeders.com — `/birds/african-grey-congo-parrot` (Google #1)**
- **Why it ranks:** Exact-intent URL node; **27 live, dated Congo listings** each with a price ($400–$8,500), a one-line human hook ("Meet Charlie, my stunning huge male…"), "We Ship," and a linked breeder + city/state (Fifty Shades MN, PETGrove FL, Quest Haven CA, Love Your Bird MD). Perpetual freshness + high topical DA + `Psittacus erithacus` mentions.
- **Weaknesses:** Zero trust curation (anyone lists), no health-guarantee/CITES layer, no care/education content, ugly UI, per-listing depth is one sentence.
- **Steal:** the *dated, priced, city-tagged listing card* pattern; the human one-line hook per bird; the "We Ship" badge. **Beat by** doing it with curated, documented, health-guaranteed CAG birds + real photos.

**② graybreedersfoundation.yolasite.com (Google #2) — ⚠️ LIKELY SCAM**
- **Why it ranks:** Aged exact-match-y content (est. 2015 claim), "$1,500 / babies $800" price bait, "MAP-certified / AFA member / 50 employees / headquartered in California" authority claims, keyword-dense species copy.
- **Scam flags (CITES/legal):** payment via **Gift Card, Western Union, PayPal** only; **"delivery 24 hours or more by air… wherever you are located"** (worldwide shipping of CITES Appendix-I birds = illegal); free Yola site; "operate all over the World." **This is the #2 result and it is almost certainly fraudulent.**
- **Steal:** nothing to emulate. **Weaponise it:** it proves (a) the SERP is weak enough that a free scam site outranks legit breeders, and (b) our scam-awareness/verification angle is desperately needed. Reference the *pattern* (Gift Card/WU/worldwide-air) in our trust section.

**③ mybabyparrot.com / Parrot Wizard (Michael Sazhin) (Google #4) — authority moat**
- **Why it ranks:** Genuine E-E-A-T — published author (trainedparrot.com), **multiple embedded Vimeo videos** (huge dwell time), and the deepest trained-bird spec on the SERP: **Target/Step-Up/Flight-Recall/Harness trained**, benefits/skills/social checklists, exhaustive real diet list (Harrison's, Roudybush, TOPs, Zupreem, micro-greens…), "Birdie Shower kit" ($1,000+ value: hatch certificate, gender reveal, framed photo), beak-to-tail health guarantee, **PayPal 0% financing 6 months**, personal delivery + transition day, explicit anti-scam section with watermarked images, and a notable line: *"We absolutely do not ever sell African Grey Parrot Eggs and we do not ship parrots outside the USA."*
- **Weaknesses:** No price shown (waiting-list/deposit only), single generic page (not per-bird), no state/geo targeting, no visible schema, product page is `noindex` (rides parrotwizard.com authority).
- **Steal (high value):** the **skills/benefits/social checklists**, the **named diet brands**, the **"what's in the box" welcome-kit framing**, **financing**, **personal-delivery + transition-day**, and the **USA-only + no-eggs honesty** stance (aligns with our egg-page truth-forward model). **Beat by** adding real prices + per-bird availability + geo, which Parrot Wizard lacks.

**④ birdsjungle.com (fresh; strong content SEO) — the on-page benchmark to beat**
- **Why it ranks/ranks-ability:** Best-structured breeder *content* page found. Title "African Grey Parrot for Sale \| DNA-Tested." Price $1,500–$4,500 (variant Female/Male/Pair). Six trust badges (Live-arrival guarantee, DNA-tested, Vet health-checked, **CITES compliant**, Verified 5-star reviews, Secure checkout). **Full schema stack: Product + FAQPage + AggregateRating + BreadcrumbList** (verified). Rich H2 map (below). Fresh (modified 2026-07-14).
- **H2/H3 structure (steal this outline):** What's Included With Every African Grey · Why African Grey Parrots Are So Loved · Congo vs Timneh (H3 Congo / H3 Timneh) · Buying an African Grey in the USA: What You Should Know (Wild Bird Conservation Act, captive-bred only, check local rules) · Caring for Your African Grey at Home (diet/housing/enrichment/company) · Ready to Welcome an African Grey? · African Grey Parrot FAQs (cost / legal / Congo-vs-Timneh / talking / lifespan).
- **Weaknesses (our openings):** **Fake reviews** — the "reviews" are copy-pasted furniture/bird-feeder text ("looks beautiful in my backyard," "packed safely," "birds haven't left it alone"); a leftover **"Size and packaging guidelines: Chair / Armchair / Sofas"** furniture-theme table; **add-to-cart + Buy-now for a live CITES-I bird**; no real breeder identity, address, or USDA license; stock hero image.
- **Steal:** the H2 skeleton, the 6-badge trust row, and the full schema stack — but execute with **real** reviews (via `cag-review-collection-agent`), real photos, real USDA/CITES docs, and a reserve-with-deposit flow instead of instant checkout.

**⑤ buyafricangreyparrots.com (fresh; Bing #7) — "USDA-licensed Florida breeder"**
- **Why it ranks:** Clean Shopify build, strong trust framing ("most trusted source," USDA-licensed FL), badge row (Vet Checked, 1-Year Health Guarantee, Nationwide Delivery, Lifetime Support), named Congo birds (Violet $800, Jasper $900, Orion $1,000, Luna $1,300, pair $2,100), dedicated `/pages/congo-african-greys` + `/collections/congo-african-grey-parrots-for-sale`, Congo-vs-Timneh block, FAQ, shipping page.
- **Weaknesses:** Suspiciously **low $800–$1,300** prices; uses known **Pixabay stock photo** (gray-parrot-5532840_1920); no physical address; mixes "adoption process" with e-commerce; no visible real reviews.
- **Steal:** the USDA-license-forward hero, 1-year-guarantee framing, per-bird named cards with "DNA Tested, Fully Weaned" qualifiers, dedicated Congo collection URL. **Beat with** credible mid-market pricing + real Midland-TX address + real reviews.

**⑥ theavianexchange.com (fresh; Google #10) — modern "screened breeders" marketplace**
- **Why it ranks:** Purpose-built modern marketplace directly answering scam-fear: "ID-Verified Breeders · No Anonymous Sellers · Health Guarantees · No transaction fees." **State sub-pages for CA, FL, TX, NY, PA, OH, GA, NC, IL, MI** (10 of 22 CAG states). Visible FAQ + "What to look for in a breeder" checklist. Schema: **FAQPage + ItemList** (verified).
- **Weaknesses:** Marketplace with no owned inventory; listings depend on third parties; no deep species/care content; generic.
- **Steal:** the **"what to look for in a breeder" verification checklist** and the **state-page hub** pattern; the anti-anonymous-seller positioning.

**⑦ birdsbyjoe.com (Google #7) — NJ Wix breeder**
- **Why it ranks:** Brand + local (NJ/NY/PA), "top trusted African Grey breeders," phone CTA (732-764-2473), separate Congo + Timneh sections with detailed physical-description copy.
- **Weaknesses:** Almost entirely **encyclopedic species description** (copied-feel), **no pricing, no inventory, no documentation/CITES, no trust badges, no schema**, phone-only conversion, generic Wix.
- **Steal:** nothing structurally new; confirms that *even thin phone-only breeder pages rank* — so our depth advantage is decisive if we execute.

**⑧ exoticparrotpetstore.com (registered; Google #8 / Bing #2)** — see B1. Key deep facts: 9 products, Congo $1,300, sale birds $1,100–$3,800, star ratings 4.14–4.71 (auto-generated), also sells **Fertile Parrot Eggs** (egg competitor). Add-to-cart live-bird pattern + reused UK photos = our credibility opening.

**⑨ birdsnow.com (registered; #1/#3)** — see B1. Key deep facts: **576 AG ads**, prices $2,200 (Congo male) / $3,000 (female) / $6,500 (pair) / $8,500 (babies) / $2,800–$3,200 (Timneh), and a **state-page for essentially every state** (the geo footprint to match). This is the aggregator whose *geo coverage* we must mirror with our 22 location pages internally linking to this Congo page.

**⑩ silvergatebirdfarm.com (registered; #6)** — **NOT FETCHED** (recaptcha.cloud cloak). From SERP: exact slug + "$1,500–$3,500," "Well Trained and Handfed." Its crawler-hostility is a fragility we can out-rank with an open, fast, well-marked-up page.

---

## C. KEYWORD UNIVERSE (they rank/use; our stub does not)

Our current page uses only: *Congo African Grey For Sale, Psittacus erithacus, hand-raised, CITES, DNA sexed, red tail, 1,000+ words, Midland TX.* Everything below is a **gap**.

**Commercial / transactional (high intent):**
- baby congo african grey for sale · congo african grey parrot for sale · buy congo african grey (online) · congo african grey breeder · hand-fed / hand-raised congo african grey · DNA-tested / DNA-sexed congo african grey · weaned congo african grey baby · congo african grey pair for sale · red-tail congo african grey · trained congo african grey (talking) · congo african grey for sale near me · congo african grey for sale [state] · african grey parrot for sale (Bing head term) · USDA licensed african grey breeder · congo african grey price / cost.

**Long-tail (buyer-decision):**
- congo african grey for sale $1500 / under $2000 · why are african greys so expensive · congo african grey for sale with health guarantee · legit african grey breeder (how to tell) · congo african grey shipping / can african greys be shipped · congo vs timneh which is better for beginners · fully weaned DNA-tested congo baby · congo african grey talking age · closed-band captive-bred african grey · congo african grey for sale [Texas/California/Florida/New York/Georgia].

**Semantic / LSI / NLP (winners cluster these):**
- companion parrot · hand-fed · weaned · closed leg band / closed-banded · DNA sexing certificate · avian veterinarian / vet-checked · health record / health guarantee · live-arrival guarantee · foraging · enrichment · positive reinforcement · target/step-up/harness/flight-recall trained · socialized · mimicry / vocabulary / talks in context · Wild Bird Conservation Act · captive-bred · CITES Appendix I / CITES compliant · PBFD / polyomavirus negative · pellet diet (Harrison's/Roudybush/TOPs/Zupreem) · low blood-calcium risk · 40–60 year lifespan · nationwide shipping / IATA / Delta-United.

**PAA / question keywords (from SERP + FAQ blocks competitors answer, our stub doesn't):**
- How much does a Congo African Grey cost? · Is it legal to buy an African Grey in the USA? · What's the difference between a Congo and a Timneh? · Do African Greys really talk? · How long do African Greys live? · What should I ask a breeder before buying? · Are these breeders verified / how do I avoid a scam? · Can an African Grey be shipped? · What is included with the bird? · Why are African Greys so expensive all of a sudden?

---

## D. ENTITY MAP (entities winners cover that our page lacks)

Present on our stub: `Psittacus erithacus erithacus`, CITES Appendix I, DNA sexing, red tail, Midland TX, hand-raised.
**Missing / under-covered vs winners (add these):**
- **Legal/authority entities:** Wild Bird Conservation Act (1992) · USDA (AWA license) · CITES compliant/captive-bred documentation · closed leg band · IATA / airline live-animal shipping (Delta, United, American).
- **Health entities:** avian veterinarian · vet health certificate · health guarantee / live-arrival guarantee · **PBFD** & **polyomavirus** PCR screening (assertable per CAG Verified-Claim Ledger) · low blood-calcium/hypocalcemia risk · psittacosis.
- **Care/behaviour entities:** foraging · enrichment · positive reinforcement · target/step-up/harness/flight-recall training · weaning (12–16 weeks) · pellet brands (Harrison's, Roudybush, TOP's, Zupreem) · socialization.
- **Product/commerce entities:** deposit/reservation · what's-included package · welcome/"birdie shower" kit · financing (PayPal/Affirm-style) · nationwide shipping tiers ($185 airport / $350 home) · pickup option (Midland, TX).
- **Comparison entities:** Timneh African Grey (*Psittacus timneh*) · Congo vs Timneh (size 400–600 g vs 275–375 g; red vs maroon tail; beginner suitability).
- **Trust/scam entities:** scam red flags (Gift Card / Western Union / PayPal F&F / worldwide 24-hour air / stock photos / add-to-cart for live birds) · verified-breeder checklist · real reviews/testimonials.

---

## E. INFORMATION-GAIN OPPORTUNITIES (our moat — NO competitor does these)

1. **"Is this seller legit?" verification block (BIGGEST MOAT).** The entire Reddit/FB layer is scam-terror ("legitimate website?", "scam or not?", "$8,000 vs $1,400"), and the #2 Google result (graybreedersfoundation) is itself a probable scam. **No transactional competitor pairs a for-sale page with a live scam-verification checklist.** CAG can: show USDA license + CITES paperwork + real Midland-TX address + video-call-before-you-pay offer + "we never take Gift Card / Western Union / PayPal F&F" + a red-flag list. This converts the fear the whole SERP ignores.
2. **Honest price explainer: "Why $1,500–$8,500?"** UGC explicitly asks "why so expensive all of a sudden?" and prices on the SERP swing 10× ($400 → $8,500). No competitor explains it. A transparent "what drives Congo price (age, hand-raising, DNA/health testing, documentation) — and why suspiciously cheap $800 birds are a red flag" section owns a question every buyer has and positions CAG's mid-market $1,500 floor as the *credible* choice.
3. **Real, documented per-bird availability with proof.** Aggregators have volume but no trust; scam stores have trust-claims but stock photos. CAG's real named birds + real photos + DNA/health certs + parents = a combination the SERP structurally lacks.
4. **Congo-specific (not generic "African Grey") depth.** Most rivals blur Congo/Timneh into one page. A page that truly owns *Congo* (red-tail, 400–600 g, vocabulary, temperament vs Timneh) with a decision aid is differentiated.
5. **CITES Appendix I done correctly.** Competitors either ignore it or say "CITES compliant" vaguely; some illegally offer worldwide shipping. CAG can authoritatively explain captive-bred Appendix-I legality (legal to own/transfer domestically with paperwork; no international shipping) — an accuracy moat that also flags the scammers.
6. **Post-purchase / lifetime-support + shipping transparency.** Real $185 airport / $350 home tiers, IATA carriers, pickup-in-Midland option, transition-day support — concrete where rivals are vague.

---

## F. WAYS TO BEAT THEM — prioritized, mapped to for-sale page sections

The current page is a **~350-word stub** (one H2, two H3s, Product+Organization schema only) that ranks nowhere. Rebuild to the `cag-for-sale-page-builder` 22-section transactional standard. Priority order:

**P0 — Foundational (do first)**
1. **Meta + H1 disambiguation for Bing + Google.** Adopt the extended 3-part for-sale meta; front-load "Congo African Grey Parrot for Sale" with *parrot/Psittacus erithacus/bird/breeder* early to beat Bing's country-entity hijack. (Fixes A4.) → *Hero + `<title>`*
2. **Schema parity + lead.** Add **FAQPage + AggregateRating/Review + BreadcrumbList + ItemList** (birds) to the existing Product/AggregateOffer. birdsjungle already has all four; we have none. → *Schema block*
3. **Heading outline to standard.** Full H1→H6, ≥5 H5 + ≥5 H6, no skipped levels (current page is H1→H2→H3 only and fails the gate).

**P1 — Conversion + trust (the differentiators)**
4. **Availability cards near the fold** — real named Congo birds, dated, priced, DNA/health-tagged, "We Ship" + shipping line ($185 airport / $350 home), reserve-with-$200-deposit CTA. Beats birdbreeders' pattern with curation. → *Available Birds*
5. **Scam-verification / "Is this breeder legit?" block** — USDA license, CITES docs, real Midland-TX address, video-call-before-payment, "we never accept Gift Card/Western Union/PayPal F&F," red-flag checklist. **The moat.** → *Trust / Why-Choose*
6. **Honest price explainer "Why do Congo prices range $1,500–$8,500?"** — position CAG's $1,500 floor as credible-mid-market; flag suspiciously-cheap $800 birds. → *Price Guide*
7. **Trust-badge row** (USDA AWA · CITES captive-bred · DNA-sexed · avian-vet health cert · live-arrival guarantee) — match birdsjungle's 6-badge row with *real* credentials. → *Trust bar*

**P2 — Depth + entities (rank-durability)**
8. **Congo vs Timneh decision block** (H2 + H3s) — steal birdsjungle/buyafricangreyparrots outline; size/tail/temperament/beginner-fit; internal-link the comparison cluster. → *Why Congo / Comparison*
9. **"What's included" package** — DNA cert, closed band, health record, care guide, lifetime support, welcome kit; add **financing** + **personal-delivery/transition-day** (steal Parrot Wizard). → *What's Included*
10. **Care/talking/training/diet mini-sections** with named pellet brands + training terms (target/step-up/harness) + weaning + talking-age — the entity spread rivals cluster and our stub omits. → *Temperament/Talking/Training/Diet/Health*
11. **PAA-driven FAQ** (cost, legality/WBCA, Congo-vs-Timneh, talking, lifespan, "how to avoid scams," shipping, what's-included) with FAQPage schema — every winner has this; we don't. → *FAQ*

**P3 — Geo + authority**
12. **State relevance** — internally link the 22 CAG location pages to this Congo page and vice-versa, mirroring birdsnow/theavianexchange's state footprint (they cover all/most of our 22 states). → *Shipping/Geo + internal links*
13. **Real reviews** via `cag-review-collection-agent` (never fabricate — birdsjungle's fake furniture-reviews are a cautionary tale) + AggregateRating schema. → *Reviews*

**Cross-cutting flags for the builder**
- **CITES:** State captive-bred Appendix-I legality correctly; **no international shipping**; use the scammers' worldwide-air claims as a contrast, not a model.
- **Dup-content gate:** run `cag-duplicate-content-gate` vs the comparison cluster + siblings (Timneh page, variant pages) before outline approval and at final pass.
- **Refresh existing research:** update `RESEARCH-DATA-FOR-SALE-PAGES.md` PAGE 2 with these live prices/competitors; retire the off-target "adoption cost" PHASE-2 section for this keyword.

---

## Appendix — Live pricing intelligence (fetched this session)
| Source | Congo price(s) | Notes |
|---|---|---|
| birdbreeders.com | $400 / $2,500 / $3,300 / $4,000 / $5,499 / $5,999 / $7,500 / $8,000 / $8,500 | Private/breeder listings; many at $8,500 |
| birdsnow.com | $2,200 (male) · $3,000 (female) · $6,500 (pair) · $8,500 (baby) | Timneh $2,800–$3,200 |
| silvergatebirdfarm.com | $1,500–$3,500 | SERP snippet only (NOT FETCHED) |
| exoticparrotpetstore.com | Congo $1,300; sale birds $1,100–$3,800; baby $800; Timneh $950 | Add-to-cart |
| exoticparrotsplanet.com | Congo "Alpha" $800 | Intl shipping (illegal for CITES-I) |
| birdsforsales.com | $730–$850 (Zazu $770, Ruby $850, pair $1,500) | Suspiciously low |
| buyafricangreyparrots.com | $800–$1,300 (pair $2,100) | Stock photos |
| featheredfriendshub.com | $1,200–$2,400 | Variant pricing |
| birdsjungle.com | $1,500–$4,500 | Variant Female/Male/Pair |
| graybreedersfoundation | $1,500 (babies $800) | **Scam-flagged** |
| theavianexchange.com | up to $8,500 (Parrot Stars, IL) | Marketplace |
| omarsbirds (FB, CA) | $6,499–$6,999 | Retail store |
| **CAG (current)** | **Adult $1,500 · Baby $3,000 · Pair $2,700 · Deposit $200** | **Credible mid-market — a positioning advantage** |

> **Pricing takeaway:** two clusters exist — credible private/breeder market **$2,200–$8,500** (birdsnow/birdbreeders) and suspiciously-cheap e-commerce **$730–$1,300** (many scam-pattern). CAG's $1,500 adult / $3,000 baby sits in the *trustworthy middle* — neither gouging nor "too good to be true." Lead with that framing.

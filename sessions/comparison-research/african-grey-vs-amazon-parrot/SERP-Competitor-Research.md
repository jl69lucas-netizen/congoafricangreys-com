# SERP + Competitor Reverse Engineering — /african-grey-vs-amazon-parrot/

**Fetched live 2026-07-10.** Every row below was retrieved this session (Google via headless Chrome; content pages via Firecrawl; Reddit via headless Chrome after Reddit blocked Firecrawl/curl/WebFetch). Anything not retrieved is marked `NOT FETCHED` and is never substituted with an estimate. See `Evidence-Log.md` for the retrieval method and failure record per source.

---

## 1. SERP Snapshot — Google US, `african grey vs amazon parrot`

Query: `google.com/search?q=african+grey+vs+amazon+parrot&gl=us&hl=en&num=20`, headless Chrome, 2026-07-10.

| # | Result | Type | Why it ranks |
|---|--------|------|--------------|
| 1 | reddit.com/r/parrots — "African Grey's VS Amazons" | UGC forum | Fresh (Sep 2025), 24 top-level comments, exact-match title, Reddit's site-wide authority + Google's UGC boost. First-hand owner experience Google reads as Experience (E-E-A-T). |
| 2 | facebook.com/groups/64779050616 — "Which parrot species is better, African Grey or Amazon?" | UGC group | 266 comments / 48 reactions on a single question post in the "African Grey Parrots" group. Google surfaces + *cites it in the AI Overview*. |
| 3 | pethelpful.com — "Amazons vs. African Grey Parrots as Pets" | Publisher article | Published 2012-03-12, modified 2023-04-09. Domain authority + 14 yrs of accrued links. Author writes as an aviculturist who owns both. |
| 4 | forums.avianavenue.com — "African Grey Vs Amazon" | UGC forum | Thread from 2015. Ranks on topical-authority + genuine multi-owner testimony. |
| 5 | quora.com — "I plan to buy a parrot, but I can't decide between an Amazon and African gray" | UGC Q&A | Top answer from a 25-yr Grey / 15-yr DYH Amazon owner, 95 upvotes. |
| 6 | zupreem.com — "Best Pet Bird: We Asked 100 Bird Owners…" | Brand content | Runs an "Amazon vs. African Grey" bracket round. Brand authority (pellet manufacturer). |
| 7 | talkparrots.com — "African Grey vs. Double Yellow Headed Amazon" | UGC forum | 2013 thread. Ranks for the species-level long-tail. |

Also present on page 1: Instagram reel (`fancy_feathers_india`), TikTok (`@geckoemmy`), en.wikipedia.org/wiki/Grey_parrot.

### The single most important finding
**Seven of the top seven Google results are user-generated content or publisher articles. Zero are breeders. Zero sell an African Grey.** There is no commercial page in the Google top 10 for this keyword. Nobody has built the authoritative, first-party, breeder-written comparison — so Google is falling back on forums.

### AI Overview — present, and we captured its text
Google shows an AI Overview for this query. Verbatim opening:

> "Amazon parrots are extroverted, loud, and clownish with vibrant green plumage, while African Greys are highly intelligent, sensitive, and reserved… Both are large, long-lived companions, but Amazons fit active families, whereas Greys require calm environments and mentally stimulating routines."

It declares **"7 sites"** and names its citations: **Facebook**, **PetHelpful**, **TalkParrots** (plus "Show more"). Its three sub-headings are **Core Differences**, **Personality & Temperament**, **Noise vs. Talking**, and it pulls a **Dust Production** line from the Facebook group post.

**GEO implication:** the AIO is currently citing a Facebook comment thread for a factual dust claim. A page that answers *Personality & Temperament*, *Noise vs. Talking*, and *Dust Production* in clean, extractable, entity-first prose is competing against a Facebook post for that citation — an unusually low bar.

---

## 2. Bing / DuckDuckGo index — a completely different SERP

Bing's own SERP served a bot-decoy page (Microsoft properties) to both headless Chrome and its RSS endpoint — recorded as `NOT FETCHED` for bing.com direct. DuckDuckGo runs on the Bing index and returned cleanly (headless Chrome, `kl=us-en`):

| # | Result |
|---|--------|
| 1 | exoticpethub.com/african-grey-vs-amazon-parrots-key-differences/ |
| 2 | birdaddicts.com/amazon-parrot-vs-african-grey-parrot-9-differences-bird-addicts/ |
| 3 | birdgap.com/amazon-parrot-african-grey-compared/ |
| 4 | pethelpful.com |
| 5 | talkingparrotsisland.com/african-grey-parrots-vs-amazon-parrots/ |
| **6** | **congoafricangreys.com/african-grey-vs-amazon-parrot/ ← us** |
| 7–8 | tiktokparrot.com (×2) |

**Two different competitive worlds.** Bing ranks SEO content pages; Google ranks humans. We already rank #6 on Bing with a 816-word stub. The Google top 10 has no commercial page at all. The page we build has to win a *content* SERP (Bing) and an *authenticity* SERP (Google) at the same time — which is exactly what a real breeder who owns both species can do and a content farm cannot.

---

## 3. Search Intent

Mixed, and it splits cleanly:

- **Comparison / pre-purchase decision (dominant).** "Which should I buy", "help me choose". The Reddit OP is literally: *"Doing as much research as I can on parrots to see what kind will fit me & my boyfriend best."*
- **Informational.** Size, lifespan, price, noise, dust, bite.
- **Commercial-investigational (unserved).** The related-search block returns `African grey vs amazon parrot price`, `African Grey parrot for sale`, `African Grey parrot price` — buyers are *one query away* from transactional, and no comparison page catches them.
- **Reassurance / objection.** "Am I ready?", "is it right for a first bird?", "will it bite my kid?"

The searcher is almost never a current owner. They are 4–8 weeks from buying and are trying to avoid a 50-year mistake.

---

## 4. Competitor Reverse Engineering (top 7 + the Bing set)

### 4.1 reddit.com/r/parrots — "African Grey's VS Amazons" (Google #1)
- **Format:** question post, 24 comments in DOM. Sep 2025.
- **Angle:** "tell me your experience with both."
- **What it does well:** unrepeatable first-hand specificity. Top comment (68 pts) from a 15-year rescue worker opens with a rehoming claim and a screening question: *"if this bird bit you on the lip to the extent that you will need stitches, what will you do?"*
- **Coverage:** bite/rehoming reality, cost ("she's a $26,000 USD cockatiel"), lifespan-vs-relationship ("Who would keep the bird in a breakup?"), one-person bonding, dust.
- **Exploitable gap:** no structure, no table, no schema, no images, no pricing, contradicts itself across comments. Un-skimmable. **Cannot be cited as a source.**

### 4.2 facebook.com/groups — "Which parrot species is better…" (Google #2, cited by AIO)
- 5 June 2024 · 48 reactions · **266 comments** · group "African Grey Parrots". Only 3 of 138 comments render without login.
- Best line captured: *"Amazons never bluff. If they are displaying warnings they mean it."* (Wesley Dolson, owner of both.)
- **Gap:** login wall, zero structure, and Google is citing it for a *dust* fact it never rigorously states.

### 4.3 pethelpful.com — "Amazons vs. African Grey Parrots as Pets" (Google #3)
- **Published 2012, modified 2023.** ~1,900 words. Author: Holly Starenchak Baukhagen, aviculturist.
- **Headings:** Observing Bird Behavior · Which Parrot Should I Get as a Pet? · Congo African Grey Parrots (H3 Research on African Greys) · My African Grey: Louise Bird · Awesome Amazons (H3 Amazons Come in Beautiful Colors / They Are Loudmouths!) · Reasons to Love Them Both · Are Parrots Domesticated? · Only You Can Decide… · Questions & Answers.
- **Strengths:** genuine named-bird storytelling (Louise the Grey, Pedro the Mexican Red-Headed Amazon). Health honesty: Greys → heart conditions/seizures in old age; Amazons → obesity and fatty liver.
- **Exploitable gaps:** **no comparison table.** No schema beyond Article. **No pricing.** No noise figures. Author declares "an obvious bias for the Congo African Grey." **Actively harmful passage** for a CITES-conscious buyer: *"Most larger parrots… are only a few generations removed from the wild, if not wild-caught."* That's the #1 fear our buyer has, stated as fact on the #3 result — and nobody rebuts it.

### 4.4 forums.avianavenue.com (Google #4)
- 2015 thread, ~14 substantive replies from long-tenure keepers.
- **The most valuable single artifact in this SERP.** The OP states four "known basics" and the thread's own veterans *dismantle three of them*:
  - OP: "Greys are dusty, Amazons are not" → mod Theresa: "when Olivia is molting I deal with an explosion of fluffies."
  - OP: "Greys are shy, Amazons outgoing" → "It's the opposite here."
  - OP: "Greys temperamentally stable, Amazons hormonal" → "Olivia is my sweetest most stable… Corkey and Lucy are VERY sassy."
- Best expert passage (melissasparrots, keeps both): *"Recently weaned baby greys are often snugly. Recently weaned baby amazons are already wanting to rough house… A baby amazon can be harder to get along with at 6 months old than it will be at 6 years. With greys, the trend might be reversed."*
- **Gap:** it's a 2015 forum thread. No structure, no images, no schema, unusable on mobile.

### 4.5 quora.com (Google #5)
- Top answer, **95 upvotes**, Martha Hesselein — "25+ year owner of African Grey, 15+ year owner of DYH Amazon":
  > "The Grey is quiet, reserved, and skittish. The Amazon is loud, exuberant, and curious. The Grey is a very clear talker… and the Amazon's pronunciation is more akin to Scooby-Doo's."
- Second-most-upvoted content on the page is an anti-purchase argument (Rick Klugman) featuring plucked-bird sanctuary photos.
- **Gap:** ad-choked, Cloudflare-gated, no structure. Also: the highest-value answers argue *against buying at all* — an objection our page must meet head-on rather than ignore.

### 4.6 zupreem.com (Google #6)
- Brand blog. Runs a bracket: Finch v Canary, Lorikeet v Cockatiel, **Amazon v African Grey**, Macaw v Cockatoo.
- Result: *"African grey soared past the Amazon. The most often mentioned pro for the African grey was their intelligence."* Grey then beat the cockatoo, and lost the final to the **cockatiel (61%)** on beginner-friendliness.
- **Usable, citable third-party datapoint** for a "why buyers pick the Grey" section — n=100 owners, from a pellet brand with no dog in the Grey-vs-Amazon fight.
- **Gap:** it's a survey, not a comparison. No care, no cost, no health.

### 4.7 talkparrots.com (Google #7)
- 2013 thread; the specific query is *"which would be better to have around children?"* (poster's son is 6, has allergies).
- The thread's answer is emphatic and consistent: **neither.** Repeated warnings about DYH/blue-fronted/yellow-naped Amazons at sexual maturity, "bites… the kind that requires hospital trips," Grey dust vs a child's allergies. Five separate posters redirect him to a cockatiel or budgie.
- **This is the honest answer, and it is a moat.** A breeder page that says "if your child is six and has allergies, buy neither of these birds from us this year" earns exactly the trust the SERP is starving for.

### 4.8 The Bing-index content set (our real *content* competitors)

| Page | Words / structure | Verifiable defects |
|---|---|---|
| **exoticpethub.com** (Bing #1) | ~2,000 w. H2/H3 (Intro · Size & Weight · Temperament · Socialization · Noise · Health) + 5-Q FAQ. Published 2026-01-11. Reads AI-generated. | **"a distinctive black band running across the belly"** — Greys have no such marking. **African Grey weight "250–500 grams"** — Congos run 400–650g. Says *"if you're a first-time owner, a smaller, more manageable species like an African Grey might be a better fit"* — contradicting every owner in the Google top 7. Invents decibel bands ("Soft murmurs: 50-70 dB"). |
| **birdaddicts.com** (Bing #2, **in our 30-list**) | 9 numbered differences, ~1,600 w. 2022, mod 2023. | Genuinely useful and specific: dust → Bird Fancier's Lung; "Amazon gives warnings, Grey bites without warning"; Amazons hardier, not prone to plucking. Weak: no table, no cost, no schema, no sources. |
| **birdgap.com** (Bing #3) | Differences/Similarities split, sources cited (ASU, NatGeo, NIH). 2022. | **"usually about 13 inches long, and weigh roughly 2.5 pounds"** — 2.5 lb = 1,134 g; both species are 300–650 g. Off by ~2×. Also *"Thanks to recently passed legislation, both parrots are now bred in captivity rather than captured for trade"* — sloppy but directionally CITES-aware. |
| **talkingparrotsisland.com** (Bing #5) | **The only direct commercial competitor.** Full comparison + **11-row spec table** + **7-row "Final Verdict" winner table** + inline bird-for-sale cards ($900–$2,500) + WhatsApp chat. Oct 2025, mod Nov 2025. | Sells *both* Greys and Amazons, so its verdict table is structurally conflicted. Prose is machine-translated-sounding ("The Amazon birds is a collection…", "Peeps possessing a tranquil, composed temperament"). Bird cards say "Immunized: Yes / Vaccination: Up-to-date" — **there is no core vaccination protocol for psittacines**; that is a trust-destroying claim we must not imitate. Prices ($800–$8,500 Grey) are unsourced. |
| **vetexplainspets.com** (**in our 30-list**, ranks nowhere in Google top 10) | "7 trends" + 15 Q&A, ~1,800 w. Apr 2024. | **Fabricated authority.** Quotes "a professional avian behaviorist", "a professional avian veterinarian", "a professional avian biologist" — **all unnamed**. Self-contradicts: Q1 says Greys can suit first-time owners; Q15 says both are fine for apartments. Site-wide "4.9 stars – 2742 reviews" on a page with no reviews. |

---

## 5. Why competitors rank (grounded, per result)

1. **Reddit / Facebook / Quora / Avian Avenue / TalkParrots (5 of the top 7):** they rank on **Experience** — the one E-E-A-T pillar a content farm cannot fake. Every one of them is a person who has lived with both birds. Google has explicitly chosen lived testimony over structured articles here.
2. **PetHelpful:** 14 years of domain age and links, plus a real named author with real named birds.
3. **ZuPreem:** brand authority + original primary data (n=100 survey).
4. **exoticpethub / birdgap / birdaddicts (Bing):** classic on-page SEO — exact-match slug, clean H2/H3, FAQ block. Bing rewards it; Google does not.
5. **Nobody ranks on commerce.** No breeder has earned the right to answer this question.

---

## 6. How C.A.Gs wins

The SERP's own words tell us what it lacks. Our moat, in priority order:

1. **We are the only party that raises one of the two birds and can say so with documentation.** Every top-7 result is a stranger's opinion. Ours is a breeder's record: PBFD + Avian Polyomavirus PCR screening, DNA sexing, avian-vet exam, hatch certificate, CITES Appendix I captive-bred paperwork.
2. **We can afford to be honest, and honesty is the ranking factor here.** The SERP is full of people telling buyers *not* to buy. If our page says "buy neither if you have a six-year-old and an allergy" and "an Amazon is the better bird for a loud, social household" — we match the register of the pages that outrank us, and we're the only one who can then *also* sell.
3. **We can correct the record with citable accuracy.** Three of the five Bing content pages carry a hard factual error (weights off 2×, invented anatomy, invented decibels, fabricated experts, "vaccinated" parrots). Nobody has published a correct, sourced spec table.
4. **We can rebut the wild-caught claim on PetHelpful #3.** "Only a few generations removed from the wild, if not wild-caught" is the single most damaging sentence in this SERP for a documented captive-bred breeder. Nobody answers it.
5. **We own the buyer's actual next question.** Related searches go straight to `price` and `for sale`. Every UGC result dead-ends. We link down to live inventory, real prices, and the shipping tiers.
6. **Structured extraction.** The AIO wants Core Differences / Personality / Noise vs Talking / Dust. We give it a clean table, a 40–60 word Quick Answer, and FAQPage schema. It is currently citing a Facebook comment.

---

## 7. Content gap — what is missing from *every* competitor

Verified absent across all 12 pages read this session:

- ❌ **No correct, sourced side-by-side spec table.** (talkingparrotsisland has one; its prices are unsourced and its Grey weight is absent.)
- ❌ **No real cost-of-ownership math.** Not one page prices out year one. Reddit users volunteer $26,000 vet stories into the void.
- ❌ **No dust/dander section written for an allergy sufferer**, despite dust being the single most-repeated owner complaint and the AIO's chosen citation.
- ❌ **No bite-behaviour comparison as *behaviour*.** Owners repeatedly describe a real, actionable difference — *Amazons telegraph (eye-pinning), Greys don't; Amazons bite from excitement/hormones, Greys from fear* — and no article states it.
- ❌ **No "don't buy either" section.** The forums say it; the articles are too commercial to.
- ❌ **No CITES / captive-bred documentation content whatsoever.** Zero of 12 pages mention Appendix I. One asserts the opposite.
- ❌ **No named, verifiable expert.** vetexplainspets fabricates three.
- ❌ **No live availability, no shipping, no breeder.**
- ❌ **No FAQPage schema** on any of the informational competitors.
- ❌ **No hormonal-maturity timeline** — the thing that actually ends Amazon ownerships, per TalkParrots and Reddit both.

---

## 8. The 30-competitor registry — full sweep

Method: fetched `/sitemap.xml`, `/sitemap_index.xml`, `/wp-sitemap.xml`, `/sitemap-index.xml` for all 30 domains in `data/competitors.json` (12-thread, real UA), expanded sub-sitemaps, and grepped every URL for `amazon`, `-vs-`, `compar`. Blocked/dead domains re-probed by HTTP status, then by `site:` search. Raw output: `competitor-30-sweep.json`.

**Result: 2 of 30 have an African-Grey-vs-Amazon page. Neither ranks in Google's top 10.**

| Finding | Competitors |
|---|---|
| **Has the exact comparison page** | `birdAddicts` (T3) · `vetExplainsPets` (T3) |
| Has an adjacent Grey-vs-X comparison, but **not** vs Amazon | `parrotWebsite` (T3) — has `/african-grey-vs-cockatoo/`, 6 Amazon info pages, 5 other `-vs-` pages |
| Sells Amazon parrots but publishes **no comparison** | `exoticParrotPetstore` (6 Amazon product URLs) · `exoticPetsAvenue` (6) · `birdsNow` (6 listings) · `mariettaBirdShop` (2) |
| Owns adjacent semantic territory, no vs-page | `thesprucePets` — `/popular-amazon-parrot-species-390544`, `/amazon-parrots-1238342`, `/top-loudest-parrot-species-390531`, `/most-intelligent-bird-species-390533`, `/large-parrots-that-can-talk-390522` |
| **All 11 Tier-1 direct breeders: zero Amazon content, zero comparison pages** | afrigreyparrots, exoticParrotPetstore*, afroBirdsFarm, africanGrayParrotsForSale, silvergateBirdFarm, birdsForSales, exoticParrotsPlanet, williamsAfricanGreys, shadesOfGreys, africanGreyAviaries, compoundExotics |

\* exoticParrotPetstore sells Amazons but publishes no editorial.

**Domains that could not be crawled** (recorded, not guessed):
- Unreachable / DNS-dead (`000`): afroBirdsFarm, exoticParrotsPlanet, williamsAfricanGreys, qualityBirdsOnline, africanGreyAviaries
- Bot-blocked (`403`/`429`): petzlover, petClassifieds, thesprucePets, petFinder, chewy → all re-checked by `site:` search instead
- Sitemap fetch failed but site is live (`200`): birdaddicts, vetexplainspets → both re-checked directly; **both have the page** (this correction is why the sweep says 2, not 0)

**The headline for strategy:** not one of the eleven Tier-1 African Grey breeders — our direct commercial competition — has written a single word about Amazon parrots. The comparison keyword is commercially unclaimed, on both engines, by every breeder in the market.

---

## 9. Heading-type analysis (what shape wins)

| Source | Heading style |
|---|---|
| PetHelpful | Personal/narrative ("My African Grey: Louise Bird", "They Are Loudmouths!") |
| exoticpethub | Generic attribute ("Size and Weight Comparison", "Noise Levels and Vocalization Comparison") |
| birdaddicts | Numbered attribute ("1. Appearance", "2. Dust Issue in parrots", "3. Body language-Biting") |
| birdgap | Taxonomic (Differences / Similarities → Habitat, Subspecies, Vocalization) |
| talkingparrotsisland | Buyer-framed ("Lifestyle Fit: Which Bird Suits You Best?", "Final Verdict") |
| vetexplainspets | Listicle ("7 trends", "15 common concerns") |

**None uses conversational question headers.** Every PAA and every UGC title is a question ("Which parrot species is better…", "How bad are amazons and African greys with nipping…", "Which is bigger…"). Our hybrid question+entity H2/H3 convention is directly aligned with how this SERP's demand is phrased, and directly opposed to how the ranking content pages are written.

---

## 10. Schema audit of the SERP

| Page | Schema found |
|---|---|
| pethelpful | Article + author |
| exoticpethub | Article, FAQ block present in HTML but no FAQPage markup detected |
| birdgap | Article only |
| birdaddicts | Article only |
| talkingparrotsisland | Article + WooCommerce Product (on the inline cards) |
| vetexplainspets | Article + site-wide aggregate rating (4.9 / 2742) unattached to reviews |
| Forums | Reddit/XenForo native (DiscussionForumPosting / ReplyAction) |

**No competitor ships FAQPage on this keyword.** talkparrots.com is the only one emitting rich interaction markup, and it's the forum software doing it. Our FAQPage + Article + BreadcrumbList (component-emitted) is uncontested.

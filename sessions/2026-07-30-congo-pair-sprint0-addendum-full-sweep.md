# Sprint 0 — Addendum · Full Competitor & Channel Sweep

**Page:** `/congo-african-grey-parrot-pair-for-sale/` · **Date:** 2026-07-30
**Completes:** `sessions/2026-07-30-congo-pair-sprint0-research.md`, which shipped without the registry sweep, Instagram, YouTube and LLM visibility. **That was the wrong call — those are research standards, not optional extras.** This addendum closes them.

**Bing is deliberately excluded** — the breeder confirmed this page has no Bing data yet.

---

## 0 · Coverage, corrected

| Source | Status | Method |
|---|---|---|
| 30-competitor registry | ✅ **SWEPT** | `firecrawl_map` per domain + UA liveness probe on all 30 |
| Instagram | ✅ **FETCHED** | IG public tag hubs + post snippets |
| YouTube | ✅ **FETCHED** | Topic sweep, 10 results |
| **LLM visibility** | ✅ **MEASURED — first time on any cluster page** | Perplexity, live, 2 queries, Playwright |
| Tier-3 informational competitors | ✅ **SWEPT** | allaboutparrots mapped, 15 relevant URLs |
| Bing | ⏭️ **EXCLUDED** | Breeder direction — no data for this page |
| `petzlover.com` | ❌ **NOT FETCHED** | Full ladder climbed: Firecrawl → UA retry (403) → **Playwright headless (403, "Verify You Are Human")**. Bot-check not bypassed, by policy |
| `petclassifieds.com`, `vetexplainspets.com` | ❌ **NOT FETCHED** | 403 at step 2; both irrelevant to pair intent |
| `afrobirdsfarm.com`, `africangrayparrotsforsale.com`, `qualitybirdsonline.com`, `birdaddicts.com` | ⚰️ **DEAD** | DNS/connection failure (`000`). Four of the 30 registry entries are gone — registry needs pruning |

> **Tooling note.** `/last30days` — the recency plugin named in `skills/research-recency.md` — is **not installed**. It is a third-party plugin (`mvanhorn/last30days-skill`) and a non-interactive session cannot run `/plugin marketplace add`. I climbed to ladder step 3 (Playwright) instead, which succeeded on Perplexity and failed honestly on petzlover. **To use it, run `/plugin marketplace add mvanhorn/last30days-skill` in an interactive `claude` session.**

---

## 1 · 🔴 THE HEADLINE — LLM visibility, measured live

Two Perplexity queries, run 2026-07-30. The result inverts part of §2 of the main doc.

### Query A — transactional: *"where can I buy a bonded pair of Congo African Grey parrots in the USA?"*

**We are the #1 cited source. Roughly 16 citation markers to `congoafricangreys.com`.** Only two other domains appear: `exoticglobalparrotsfarm.com` (1) and `petzlover.com` (4).

Perplexity's answer names us in full:

> "**C.A.Gs (Congo African Greys) – Texas-based, nationwide shipping.** Operates out of Midland, Texas and states it is USDA AWA licensed and CITES documented. Lists specific bonded/breeding pairs (e.g., **'Congo Pair (Jins+Jeni)' described as an unrelated pair that must go together**, and a **'Proven bonded pair, DNA certified'**). Provides DNA sexing, health certificates, hatch certificates, and CITES Appendix I documentation for each bird in a pair. Ships IATA-compliant to all 50 states and requires a deposit to reserve."

It is reading our live inventory. It also paraphrases the **current 8 KB stub almost verbatim** — *"pairs are raised together or successfully introduced under supervision rather than randomly paired adults"* is a near-quote of the stub's one real paragraph.

### Query B — informational: *"if I buy two African Grey parrots together will they bond with each other and ignore me?"*

**We are not cited at all.** Cited instead: `pamelaclarkonline`, `african-grey-parrot.weebly.com`, `sciencealert`, `reddit`, `pubmed.ncbi.nlm.nih.gov`, `youtube`.

### What this means

| Channel | Google | Perplexity |
|---|---|---|
| Transactional pair query | pos ~5.6, **8 impressions** | **#1 cited source** |
| Informational bonding query | not ranked | **not cited** |

Three consequences, and they are load-bearing for the build:

1. **The angle approved at the Sprint 0 gate is now confirmed by measurement, not just inference.** "Two Birds, One Honest Answer" targets exactly the query where we have zero AEO presence, while the product layer defends the query we already dominate. The two halves of the page serve two different, measured channels.
2. **A rebuild can break an existing citation.** Every fact Perplexity quotes comes from the stub. These claims must **survive the rebuild verbatim in substance**: Midland TX · USDA AWA licensed · CITES Appendix I per bird · Jins + Jeni as an unrelated pair that must go together · a proven bonded pair, DNA certified · DNA sexing + health + hatch certificates · IATA-compliant to all 50 states · deposit to reserve. **This is now a build constraint, not a nice-to-have.**
3. **`cag-aeo-pass` is the highest-leverage gate on this page**, not a late formality. Perplexity is extracting discrete facts, so the atomic chunk-survivable section requirement is what earns the citation.

### The honest problem the measurement exposes

Perplexity's own answer on Query B says the pair-bond risk is highest when the birds are **"Unrelated · Similar age · Housed together with lots of mutual access and minimal forced human handling."**

**That describes Jins & Jeni exactly** — unrelated, 6 months and 4 months, sold as a unit. Our flagship pair is the textbook high-risk configuration.

The page must say so. Publishing that, alongside the mitigation protocol, is the single most credible thing on the page, and no competitor will copy it. Perplexity names the mitigations: **separate daily one-to-one time (15–30 min per bird), individual training, rotated attention, not housing them together 24/7.**

**Authority targets Perplexity trusts here — use these as external links in the bonding section:** Pamela Clark (certified parrot behaviour consultant), PubMed, ScienceAlert.

---

## 2 · 30-competitor registry sweep

### Tier 1 — direct breeders (11)

| Competitor | AG pair page? | Finding |
|---|---|---|
| **williamsafricangreys.com** | ✅ **YES — the only true one** | See §3 |
| exoticparrotpetstore.com | ⚠️ Macaw pairs only | "Willow and Ajax bonded pair macaw", "Benny and Evie" — **names its pairs exactly like we do**. No AG pair. Discounts $2,600 → $1,800 |
| compoundexotics.com | ⚠️ Non-bird pairs | "Silver_male & Skye_female", "Safiya_female & Penelope_female" ($700) sold as "bonded pair" — one is **female + female**. AG sold as singles only |
| exoticparrotsplanet.com | ❌ No | Egg-heavy. Has `/return-policy` for live birds. Congo at **$850** |
| afrigreyparrots.com | ❌ No | Tag set is the tell: `cheapafricangreyparrotsnow`, `black-african-grey-for-sale-cheap` |
| birdsforsales.com | ❌ No AG pair | "**$1500 (Pair) or $800 Each**" on toucans. "6-Star Birds", "7-Star Parrots" — invented ratings |
| shadesofgreys.com | ❌ No | Wix template with unedited placeholders `product-page/i-m-a-product-2`, `-5`, `-6`. Abandoned |
| africangreyaviaries.com | ❌ No | Live (200), no pair inventory |
| silvergatebirdfarm.com | ❌ No | Live (200). **Previously confirmed cloaker** (redirects to recaptcha.cloud) — unchanged |
| afrobirdsfarm.com | ⚰️ DEAD | |
| africangrayparrotsforsale.com | ⚰️ DEAD | |

### Tier 2 — classifieds & aggregators (8)

`birdsnow.com` is the significant one and is fully covered in §5 of the main doc (18 live bonded-pair ads, $6,500–$8,000). `birdbreeders.com` lists Congos $400–$8,500 with "Each" pricing on pairs. `hoobly`, `parrotalert`, `exoticpetsavenue` live but no dedicated AG-pair surface. `qualitybirdsonline` dead. `petzlover`, `petclassifieds` bot-walled.

### Tier 3 — informational (8) — **the real competitor set for our angle**

`allaboutparrots.com` is the one to beat. Mapped, 15 relevant URLs. Directly on-topic:

- `/african-grey-parrot-care` — *"If you get two African greys, seek out birds born and raised together. Always treat both parrots equally to avoid [jealousy]"*
- `/do-parrots-only-bond-with-one-person` — *"One-person parrots are most common when you have a **lone** bird rather than a bonded pair"*
- `/african-gray-plucking-or-molting` — *"African greys need near-constant engagement if they're not paired up"*
- Plus `/do-parrots-mate-for-life`, `/do-parrots-grieve`, `/what-age-do-parrots-start-laying-eggs`, `/can-you-separate-bonded-parakeets`

> ### 🔴 The nuance our page must get right
> Reddit says a pair will **ignore you**. allaboutparrots says a pair **reduces** one-person jealousy. Perplexity says **both are true and it depends on husbandry.**
> These are not contradictory — they are the same mechanism seen from two sides: the bird's primary bond moves off the human. That **loses** intensity of human attachment and **gains** protection against the one-person aggression problem greys are notorious for.
> **A page that only reports the Reddit half is as inaccurate as the sales pages that report neither.** The honest framing is the trade, stated as a trade. This is the page's most defensible paragraph and it should be written first.

**Correctable error:** allaboutparrots prices *"African grey $2,000–$2,750, Timneh African grey $3,500–$5,000"* — Timneh above Congo is backwards.

### Tier 4 (3)

`chewy` (supplies), `petfinder` (adoption), `mariettabirdshop` (live, local). No pair competition.

> **Registry action:** 4 of 30 entries are dead. `data/competitors.json` should be pruned and topped up — `williamsafricangreys.com` deserves promotion to a monitored tier-1, and `denimixanipetsparadise.com` is not in the registry at all despite ranking on both money queries.

---

## 3 · williamsafricangreys.com — the only true AG-pair competitor

Three named African Grey pairs: **Alex & Lizzy $1,800** · **Linda & Lamar $1,800** · **Roy & Joy**. Singles $1,000.

| Observation | Why it matters |
|---|---|
| Pair $1,800 vs 2 × $1,000 singles | They **discount** the pair below two singles. We must decide our own pair-vs-two-singles arithmetic and state it |
| Alex & Lizzy are **9 months old** | Sold as "Male & Female", years from breeding age. Same defect class as the 15-month "breeding pair" |
| Product copy is **generic species boilerplate** | Nothing about Alex or Lizzy beyond name/age/sex. No DNA cert, no health record, no CITES, no hatch date, no parents |
| **"Average Lifespan African grey parrots are 75 to 90 years"** | Wrong. Our ledger says **40–60**. A competitor overstating lifespan on a lifetime-commitment purchase |
| Hero image filename `pair-african-grey-for-sale-UK.jpg`; second image is a WhatsApp export | UK asset on a US-targeting page |
| `generator: WordPress 7.0.2` — **identical fake version string to denimix** | Two "independent" breeders running the same template kit |
| **0 reviews on every product** | |
| Contact is an `sms:` link only | No address, no licence number |

**They name pairs exactly as we do.** So the naming convention is not a differentiator — **documentation and honesty are the only moat**, which is what the approved angle already leans on.

---

## 4 · Instagram

Fetched via IG's public tag hubs and post snippets.

| Finding | Detail |
|---|---|
| `/popular/breeding-pair-african-greys-for-sale/` | "Contact kodec farm via call or WhatsApp on **09123060578**" — Nigerian number on a US query |
| `/popular/breeding-pair-of-african-grey-parrots-for-sale/` | "bonded African male and female **4 months** ready for New home" — a 4-month-old "bonded pair" |
| Reel | "Price: **175 each** … Regular **$5200 each**. Now **$4900 each**!" — $175 and $5,200 in the same post |
| Post | "My African Grey pair has laid eggs. 57 Oak Grove, **BT32**" — Northern Ireland postcode |
| Post | "African Greys around **£2,000** … UK breeders advertise singles for about **€400** with certificates … from **Rs 20,000**" — three currencies, no US market |
| Post | "Healthy, bonded, and ready to breed. **Bonded Pair Must Go!** Prunedale, California" — urgency pressure, one of very few genuine US sellers |
| Post | "Crosby is a **45-year-old** male ex-breeder Congo African Grey … a bonded pair, Aged 3 and 4" — rescue/rehome context |

**Read:** the IG pair market is overwhelmingly **offshore** (Nigeria, UK/NI, India) with contradictory pricing and biologically impossible "bonded pairs" as young as 4 months. It is **not a competitive threat for US buyers** — it is a scam-exposure source, and a good one. It also confirms the geo signal matters: "in the USA" is a real qualifier buyers need.

---

## 5 · YouTube

| Video | Relevance |
|---|---|
| *Will My Timneh & African Grey Become Friends? Introducing…* | Closest match — someone documenting a real introduction |
| *How To Bond Two Birds Together — Tips & Tricks* | *"Bonding work between two birds can be very variable. Treat each bird as an individual"* |
| *Q: Should I Get 2 IRN Parrots To Bond With Each Other?* | *"the answer is yes and no"* — parakeets, not greys |
| *What Parrots Actually Judge You On (Not Who Feeds Them)* | Adjacent to the human-bond question |

**No video specifically answers "should I buy two African Greys."** The content gap holds on YouTube as well as on the SERP. Worth logging for `@cag-video-seo-agent` later; out of scope for this build.

---

## 6 · What the full sweep changed

| Conclusion in the main doc | Status after the sweep |
|---|---|
| Angle: "Two Birds, One Honest Answer" | ✅ **Strengthened.** Now confirmed by LLM measurement — it targets the exact query where we have zero AEO presence |
| Companion-only intent split | ✅ Unchanged |
| Publish the $6,500–$8,000 comparison | ✅ **Sharpened.** Williams sells pairs at $1,800 and singles at $1,000, so the page faces a *bracketing* market — classifieds far above us, scam-pattern sites far below. The comparison must show **both ends**, or it looks cherry-picked |
| "The head term has no demand, so the page can't be won transactionally" | ⚠️ **PARTLY WRONG, and I am correcting it.** It cannot be won transactionally *on Google*. On Perplexity we already **own** it. The page has to defend an existing AEO win, which the main doc did not know about |
| "None of this changes the angle" | ⚠️ **Right about the angle, wrong about the build.** The citation-preservation constraint in §1 is new, material, and would have been missed |

---

## 7 · New open flags

| # | Flag | Owner |
|---|---|---|
| 8 | **Citation-preservation constraint** — 8 named facts Perplexity currently cites must survive the rebuild in substance | Build · **binding** |
| 9 | ~~Jins & Jeni high-risk disclosure~~ | ✅ **APPROVED 2026-07-30 — publish it** (see below) |
| 10 | ~~Pair-vs-two-singles arithmetic~~ | ✅ **APPROVED 2026-07-30 — state our logic, show both market ends** (see below) |
| 11 | `data/competitors.json`: 4 dead entries; add `williamsafricangreys.com` and `denimixanipetsparadise.com` | Build |
| 12 | `/last30days` not installed — run `/plugin marketplace add mvanhorn/last30days-skill` in an interactive session | **Breeder** |
| 13 | LLM visibility should now be measured on **every** cluster page (closes the long-standing open flag #10) | Build |
| 14 | External-link targets for the bonding section: Pamela Clark, PubMed, ScienceAlert — all trusted by Perplexity on this topic | Build |

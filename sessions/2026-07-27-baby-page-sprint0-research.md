# Sprint 0 — Intelligence · `/baby-african-grey-parrot-for-sale/`

**Page 7 of 22 · for-sale cluster · REBUILD mode (stub exists, 12 KB, ~4 H2s)**
**Date:** 2026-07-27 · **Gate:** [REVIEW] — breeder sign-off required before Sprint 0.5

---

## 1. GSC baseline (real, from `docs/research/for-sale-keywords-2026-07.md`)

**16 queries · 89 impressions · 0 clicks.** 10 of 16 are 6+-word conversational queries.

| Query | Impr | Pos | Note |
|---|---|---|---|
| baby african grey parrot for sale **in california** | 30 | 25.1 | **Largest single query — geo-modified** |
| african grey parrot **chicks** for sale | 22 | 39.0 | Distinct lexical lever; stub never uses "chick" |
| baby african grey parrot for sale | 9 | 69.8 | Head term, buried |
| baby african greys for sale | 8 | 84.4 | |
| baby african grey parrots for sale **near me** | 3 | 12.3 | Already page-2 |
| african grey **babies** for sale **near me** | 1 | **3.0** | **Already ranking pos 3** |
| how much is a baby african grey parrot | 1 | 71.0 | Price micro-intent |
| baby african grey parrot for sale uk | 1 | 30.0 | Out-of-market — do not chase |

**Read:** demand is real but the page converts nothing. Two clusters carry it — **geo (California + near-me)** and **"chicks"/"babies"** lexical variants the stub ignores entirely. The near-me variants already rank pos 3 and 12.3, so geo is the cheapest win on the page.

---

## 2. SERP snapshot — Google, US (fetched 2026-07-27)

### Query: "baby african grey parrot for sale"
| Pos | Domain | Signal |
|---|---|---|
| 1 | birdbreeders.com | **"Currently hand feeding sweet baby African Grey Congo's"** · $8,500 · registry T2 |
| 2 | exoticglobalparrotsfarm.com | **$850** · "6 Months Old, Hand-Fed & Tamed, **Fully Vaccinated**" · NOT in registry |
| 3 | parrotsoftheworld.com | "hand fed, 100% from day one" (Rockville Centre NY) · NOT in registry |
| 4 | graybreedersfoundation.yolasite.com | $1,500 · Yola free-site · NOT in registry |
| 5 | buyafricangreyparrots.com | **"USDA-licensed Florida breeder"** — closest legitimate analogue · NOT in registry |
| 6 | **reddit.com/r/AfricanGrey** | "Please can someone tell me a legitimate website…" |
| 7 | birdsnow.com | Classified aggregator · registry T2 |
| 8 | mybabyparrot.com (Parrot Wizard) | Strongest legit offer: health guarantee, personal delivery, starter kit, waiting list |
| 9 | facebook.com | "African grey Parrots for sale in New York" page |
| 10 | exoticparrotpetstore.com | **"$2,900 → $1,800 Sale!"** fake-discount + "4.71 rating" · registry T1 |

### Query: "african grey parrot chicks for sale"
Same top 2. New entrants: **theavianexchange.com** (pos 6, "screened breeders"), **midnightparrotplace.com** (pos 8), a Facebook post (pos 10, "3 amazing baby African greys ready").
birdbreeders snippet: **"we have 2 babies in the age range of 6–8 weeks."**

### Query: "baby african grey parrot for sale in california" (largest query)
| Pos | Domain | Signal |
|---|---|---|
| 1 | birdsnow.com/africangreyparrotcalifornia | $1,500 Cameron Park · **$5,500 San Diego baby** |
| 2 | craigslist LA | $5,000 · $350 conures |
| 3 | graybreedersfoundation | "headquartered in California" · $1,500 |
| 4 | facebook.com/groups (Central Valley Bird Peeps) | "African grey baby CA" |
| 5 | birdbreeders.com/birds/ca | 30 listings · **"Sweet babies. Just weaned, ready for new homes."** |
| 6 | craigslist LA | "African grey - baby $1,200" · $4,000 Bakersfield |
| 7 | prunedalebirdfarm.com (Rene's Exotic Parrots) | Prunedale CA · hand-raised babies |
| 8 | **africangraysales.com/locations/california** | **Males $750 \| Females $820** · "Regular $2,500–$3,200" fake discount. *This is the same operator flagged on the Timneh build for advertising illegal 24-hr international shipping.* |
| 9 | parrotstars.com | CA pet shop |
| 10 | theavianexchange.com/…/california/irvine | **Programmatic city pages**: "No breeders in Irvine right now. Showing 14 nationwide — many ship to Irvine via airline" |

**No C.A.Gs presence on any of the three.**

---

## 3. Reddit — fetched via Playwright (Firecrawl + WebFetch both blocked; ladder step 3)

### r/AfricanGrey — "What Age did you buy your bird?"
> **[4 pts]** "Dont buy from her. **5 weeks is too young. Dont buy an unweaned bird. Your bond wont be stronger**, there is a ton of risk involved and many view it as unethical. I got my grey when he was 3,5 months old and fully weaned."

> **[2 pts]** "We decided against purchasing such a young bird."

Busts the exact myth unweaned-sellers use to justify early pull.

### r/AfricanGrey — "Please can someone tell me a legitimate website to purchase an African grey?"
> **[24 pts — top comment]** "**There are none.** Go in person and try to adopt before buying directly."

> **[3 pts]** "Rarely local stores get them in, and when they do **they want $8,000+**… Rescue isn't a great option for everyone."

> **[1 pt]** "**Can you please help me find a breeder that isn't charging 8 grand** 😭"

> **[2 pts]** "I've never seen a legit breeder selling near me for less than like 5k nowadays. **Generally 6–8k is average.**"

> **[1 pt]** "most of them are from **bird mills**… if you pay $8,000 for an African gray, you must be totally insane. I got mine for $1,400 17 years ago."

**The trust vacuum, stated plainly:** the highest-voted answer to "find me a legitimate African Grey website" is *there are none*. And buyers believe the only options are an $850 scam site or an $8,000 local store.

---

## 4. Facebook groups — the documented harm pattern

A continuous stream of owners sold unweaned babies, then abandoned:

| Post | Age sold |
|---|---|
| "8 week old Smokey, my first time have a baby bird, any tips on weaning" | **8 wks** |
| "He had been removed from his mother at 8 weeks… **the breeder showed us how to feed him using a syringe**" | **8 wks** |
| "I brought home Pixie (9 weeks old) last week… hand-fed 3 times a day" | **9 wks** |
| "Gizmo is nearly 5 months old and is **still on 2 feeds of formula a day**" | delayed weaning |
| "Louie, my 9 month old… I got him 5 months ago, and he's **still hooked on his baby formula**" | failed weaning |
| "How to bring my 4.5 months grey parrot on self feed, **he is not eating anything by self**" | failed weaning |

This is real, public, verifiable buyer harm — and every one of these is a person who typed our target keyword six months earlier.

---

## 5. Authority anchor (verified HTTP 200)

**Association of Avian Veterinarians — "Weaning Baby Parrots" (official position paper, PDF, 2.4 MB):**
`https://cdn.ymaws.com/www.aav.org/resource/collection/AE20E93E-0F61-4C20-AB88-E237BD795B43/AAV_Weaning_Baby_Parrots.pdf`

> "AAV does **NOT** support the sale of unweaned birds and encourages that babies be fed by [experienced handfeeders]."

AAV is already an approved domain in `docs/reference/external-link-library.md`. This is the page's EEAT keystone — a veterinary body formally opposing what Google's #1 and #2 results are doing.

---

## 6. Competitor gaps → our moat

| Gap on the SERP | Our verifiable counter |
|---|---|
| #1 and #2 results sell **6–8-week hand-feeding babies** | We place at **12–16 weeks, fully weaned** (Ledger) |
| Price chaos: $750 / $850 / $1,200 → $8,500 | Real band **$1,500–$3,500**, published, per named bird |
| "Fully Vaccinated" (parrots aren't routinely vaccinated) | **PBFD + Polyomavirus PCR** — the real test (Ledger) |
| Fake discounts ($2,900→$1,800; "Regular $2,500–$3,200") | One honest price per bird from `clutch-inventory.json` |
| Sex-priced birds (Males $750 / Females $820) | Same price regardless of sex; **DNA cert** cited |
| Reddit says no legitimate website exists | USDA-licensed, CITES Appendix I, named birds, real photos |
| Reddit says legit = $5–8k | Our **baby floor is $1,500** |
| theavianexchange's programmatic city pages | Our real `/african-grey-parrot-for-sale-<state>/` network |

### 9 competitors to add to `data/competitors.json`
`exoticglobalparrotsfarm.com` · `buyafricangreyparrots.com` · `mybabyparrot.com` (Parrot Wizard) · `theavianexchange.com` · `graybreedersfoundation.yolasite.com` · `parrotsoftheworld.com` · `midnightparrotplace.com` · `prunedalebirdfarm.com` · `parrotstars.com`

---

## 7. Inventory reality (from `clutch-inventory.json` + `price-matrix.json`)

`price-matrix.json` carries a dedicated **`congo_african_grey_chick`** entry: *"African Grey Chick / Baby (3–6 months) · $2,300–$2,500 · **Main product** — hand-raised, weaned, socialized."*

| Bird | Age | Variant | Price | Baby? |
|---|---|---|---|---|
| Amie ♀ | 3 mo | Congo | $2,500 | ✅ |
| Roys ♂ | 4 mo | Congo | $2,300 | ✅ |
| Jeni ♀ / Jins ♂ (pair) | 4 mo / 6 mo | Congo | $3,500 pair | ✅ |
| Elad ♂ | 5 mo | Timneh | $1,600 | ✅ |
| Evie ♀ | 6 mo | Timneh | $1,500 | ✅ |
| Bery ♀ | **1 yr** | Congo | $1,700 | ❌ past baby stage |

**6 of 7 available birds are ≤6 months.** This page has more genuine on-topic inventory than any sibling. Bery is handled honestly as the "already grown up" contrast, not hidden.

**→ Avail facet: by WEANING STAGE / AGE BAND** — unused by all six siblings (they facet by subspecies, availability posture, and confirmed sex).

---

## 8. Recommended angle

### **"Weaned First. Shipped Second. Never the Other Way Round."**

**Why (grounded):** Google's #1 and #2 results for our exact keyword are openly selling 6–8-week-old unweaned babies. The AAV formally opposes it. Reddit's own buyers call it unethical and say the bond myth is false. Facebook groups are full of the wreckage. Meanwhile Reddit believes a legitimate baby costs $5–8k — and our floor is $1,500. Every plank is externally verifiable and none of it needs a claim beyond the Ledger.

**Trade-off (named):** it leads with an informational/ethical frame before price, which slows the fastest transactional readers. Mitigated by putting the bird cards and the price band in the hero region, the way the health-guarantee page did.

**Secondary lever — geo.** California carries 30 of 89 impressions and Review 1 (Joanna Thomas) is a **California** baby-Congo buyer. CA leads the geo set.

---

## 9. Open flags

1. `final_page_audit.py` `FORSALE` roster (line 360) covers only the 6 built slugs — **all 7 new slugs must be appended** or the auditor silently skips them (Trap #17).
2. 67 tracked files under `assets/brand/` show as deleted in git (renamed on disk). **Pre-existing**, unrelated to this build — flagged, not swept into a build commit.
3. `/last30days` plugin is not installed and cannot be installed from a non-interactive session. Reddit was obtained via Playwright (ladder step 3) instead — no data was fabricated.
4. Build order: by impressions, `grey-african-parrots` (915) and `congo-pair` (497, **the only cluster page with real clicks** — 10 @ pos 9.0) outrank baby (89). Breeder chose baby first; noted, not challenged.

# Sprint 1 Blueprint — `/african-grey-parrot-adoption-cost/`

**2026-07-27 · page 8 of 22 · REBUILD**
Research: `sessions/2026-07-27-adoption-cost-sprint0-research.md`
Pack: `sessions/for-sale-research/african-grey-parrot-adoption-cost/2026-07-27-adoption-cost-prompt-pack.md`

---

## 1. Strategy — APPROVED by the breeder 2026-07-27

**Blended: Number → Ledger → Thesis.**

Answer the money question in the first 55 words as a range, then the three-route ledger, then
"the fee is not the cost" as the closing argument that justifies our price.

**Why this over the two alternatives, grounded in Sprint 0:**
Price intent outweighs adoption intent roughly 5:1 (~150 generic-price + ~50 conversational vs ~41
adoption), so the number leads. It puts a snippet-shaped answer directly under
`how much does an african grey parrot cost` — the single query already at **position 9.5**, the only one
in the whole cost universe on the edge of page one. And it lets a rescue's own words carry the thesis
(Phoenix Landing: the adoption fee *"is minimal compared to the cost of caring for a parrot"*), so the
page never reads as a breeder arguing against rescues.

**Named trade-off, accepted:** committing to a range in paragraph one weakens the later reveal, and the
opening looks superficially like every competitor's until the reader reaches the ledger. Mitigation —
the opening range is deliberately *wide and honest* (`$450 rescue → $8,500 premium breeder`, ours
`$1,500–$3,500` inside it), which no competitor does, so even the opening carries a differentiator.

**Frameworks:** EEBP × **Setup-Stat-Reframe** × **5 Basic Objections** × QAB.
Setup-Stat-Reframe maps onto the chosen shape exactly — Setup = the number people expect · Stat = the
published fees against the market fees · Reframe = the fee is not the cost. Both it and the
5-Basic-Objections block are first use in this cluster. Spent cluster-wide: PAS, EEAT, FAB, PDB, BAB.

**Angle:** "The Fee Is Not the Cost." · **Voice lever:** fee vs cost, sticker vs total.

---

## 2. Component tuple — FINAL, verified against built code

| Slot | Pick | Uniqueness evidence |
|---|---|---|
| Hero | **Split-Hero C dark**, 2×2 grid as an ascending **price ladder** | 2nd use after eggs; differentiated by `cag-component-refresh` delta, not a new shell |
| Dial | **Dial 1 Clay Progress** | forced — Dial 2 is banned under a dark hero |
| Rail | **Rail B green ticker** | `Split-Hero C + Dial 1 + Rail B` is an unused triple; eggs = C + Dial 1 + Rail A |
| TOC | **T1 Numbered Ledger Rail, REFRESHED to a money-preview rail** — numerals replaced by running dollar bands so each row previews the cost that section covers | all 5 shells spent (verified in built code); T1 used by timneh alone; shell name and page motif converge |
| Takeaway | **K2 Price-Tag + K4 Clipboard** | unused pairing; spent = K1+K4, K1+K4+K3, K2+K5, K3+K2, K1+K5, K3+K4, K4+K5 |
| Table | **NEW Table G "True-Cost Ledger"** + Table A competitor grid | A/B/C/D/E/F all spent; G is next |
| FAQ | **FAQ-C dark, refreshed to a ledger register** with a clay `$` chip | eggs used FAQ-C as anti-scam interrogation; hand-raised as a forest-green checklist |
| Avail-B | faceted by **PRICE BAND** | siblings facet by subspecies, posture, sex, age band |
| Newsletter | **NEW `fs-nl ledger`** — Price-Watch card, mid-page | `banner` and `split` both spent; hand-raised and baby ship none |
| Tool | **`.cost-tool`** — multi-year, ranges, route comparison | differentiated from the homepage first-year calculator; cross-linked both ways |

**H6 prefixes (unique to this page):** `Line Item:` · `From the Ledger:` · `Receipt Note:`
Spent: In Writing:, From the Vet:, On File:, At Week N:, From the Nursery:, Weaning Log:.

---

## 3. Section taxonomy — 22 sections

`M` = mandatory core · `C` = competitor-based (source named) · `S` = suggested, our moat.

| # | Section | Tag | Words | Why |
|---|---|---|---|---|
| 1 | Hero — price ladder + the range in the first 55 words | M | 180 | Snippet target for `how much does an african grey parrot cost` (pos 9.5) |
| 2 | Counter strip — 8 Ledger-verified snippets | M | 40 | Cluster furniture |
| 3 | Key takeaway K2 Price-Tag — the sticker | M | 150 | Money page convention |
| 4 | What does an African Grey actually cost in 2026? | M | 420 | Head answer; owns the ~150-impression generic-price cluster |
| 5 | **What do rescues actually charge?** — the published fee schedules | **C** | 480 | parrotsfirst.org $450 · phoenixlanding.org $500 · companionparrots.org $500 · riparrots.org $1,500 — every ranking rescue publishes a fee and stops there |
| 6 | **Why the published fee and the fee you pay are different numbers** | **S** | 420 | Nobody reconciles them. Schedules say $450–$500; r/parrots owners report $600–$900, and a San Diego store wanted $5,500 |
| 7 | **Table G — the True-Cost Ledger** (3 routes × Day One / Year One / Five Year) | **S** | 380 | The moat. No page in either SERP prices the routes side by side |
| 8 | **`.cost-tool` True-Cost Calculator** | **S** | 220 | No competitor has any interactive tool; differentiated from the homepage first-year version |
| 9 | What you hand over on day one | M | 400 | Transactional core; bird + delivery + deposit |
| 10 | What the price actually covers here | M | 430 | Papers, PCR, DNA, vet certificate — the Ledger claims |
| 11 | `fs-nl ledger` — Price-Watch newsletter | M | 90 | Breeder-required mid-page newsletter, new variant |
| 12 | The first thirty days: setup you buy once | C | 400 | Every cost competitor covers first-year setup; ours is line-itemed from `financial-entities.json` |
| 13 | What a grey costs you every year after that | C | 420 | Same; food, vet, toys, unexpected |
| 14 | The forty-year money question | S | 380 | Ties to lifespan; `foreverbugg`'s retirement-plan argument from r/parrots |
| 15 | **What an $800 grey really costs you** | **S** | 400 | The sub-floor route, taught as a pattern — never naming a specific business |
| 16 | Key takeaway K4 Clipboard — what the fee does not cover | M | 150 | Second takeaway slot |
| 17 | Do we ship internationally? — the honest US-only answer | S | 260 | **Counter-positioning for the India cluster.** Captures `african grey parrot price us` / `price in usa` while deflecting the rest |
| 18 | How your grey gets home, and what that costs | M | 380 | $185 / $350 / from $750 / Midland pickup; links the 6 geo pages |
| 19 | Which bird sits in which price band — Avail-B | M | 420 | Real inventory, faceted by price band |
| 20 | What buyers say — Ida Brim, Lawrence Brunner | M | 200 | Real reviews, both unspent in the cluster |
| 21 | FAQ-C ledger register | M | 620 | PAA-sourced; feeds FAQPage schema |
| 22 | Keep reading + `.xsell` + contact form | M | 380 | Cluster furniture |

**Total ≈ 7,200 words of prose before chrome.** Trim sections 12–14 first if the built page overshoots
the 5,300–7,000 band; they are the most competitor-generic and the least differentiating.

---

## 4. Keyword distribution — 85–105 total

| Type | Count | Anchors |
|---|---|---|
| Primary — *african grey parrot adoption cost* | 30–35 | title, H1, first 100 words, hero alt |
| LSI | 20–25 | adoption fee, rehoming fee, surrender, foster-to-adopt, cost of ownership, price range |
| Long-tail 6+ words | 15–20 | *how much does an african grey parrot cost*, *what does an african grey parrot cost in the usa* |
| Branded | 10–15 | C.A.Gs, Mark & Teri Benjamin, C.A.Gs pricing |
| Conversational | ~23 | headers + PAA answers |
| Comparison | 5–8 | congo vs timneh price, adopt vs buy |
| Solution | 5–10 | documented, papered, scam-free |
| Transactional | ~15 | reserve, deposit, available now |

**Secondary cluster, in GSC-impression order:** african grey parrot price (32) · african gray bird price
(28) · african grey price (19) · african grey parrot for adoption (18) · african gray parrot for
adoption (16) · african grey birds price (13) · african grey parrot cost (7) · how much does an african
grey parrot cost (4 @ **9.5**) · african grey parrot price near me (4 @ 13.0) · african grey parrot
price us (2 @ **11.5**).

**LSI worth including, evidenced:** *Jaco* — appears as `jaco parrot price` (4) and `jako parrot price`
(1). One natural mention in the species-naming context, no more.

### NEGATIVE — appears nowhere as a target
`african grey parrot price in india` and every non-US variant (bangladesh, philippines). Handled once,
at H4/H5 in section 17, as an honest US-only statement.

### DO-NOT-CHASE — revised from Sprint 0, this supersedes the pack
- **cheap / cheapest / affordable / budget** → owned by `/affordable-african-grey-birds-for-sale/`
  (242 impressions at position **13.29**). Link to it; never compete with it.
- **congo + price as a head term** → owned by `/congo-african-grey-for-sale/` (~240 impressions).
  Internal link only.

---

## 5. Meta — three sets, one Recommended

**Set 1 — Transactional-Urgency (RECOMMENDED)**
> **Title:** African Grey Parrot Adoption Cost | What Does an African Grey Actually Cost in the USA? | 3 Honest Routes Priced Day One, Year One and Five Years | C.A.Gs – Midland, TX — Rescue Adoption Fees, Breeder Pricing, DNA-Sexed and CITES-Papered Congo and Timneh Greys From $1,500
>
> **Description:** See every route priced honestly — rescue fees from $450, our documented Congos and Timnehs from $1,500, and the five-year number nobody publishes. USDA-licensed, CITES Appendix I papered, PBFD and Polyomavirus PCR screened. Ships nationwide, $185 airport or $350 home. Reserve yours in 24 hours.

**Why recommended:** front-loads the primary keyword, then carries the *"in the USA"* qualifier that
captures `african grey parrot price us` (already at 11.5) while deflecting the India cluster, then names
the three-route structure that is the page's actual moat. Real floor price, real credentials, branded
ending. **Trade-off:** at ~275 characters the title will be truncated in the SERP — the first 60
characters have to carry it alone, and they do, but the differentiator sits past the fold.

**Set 2 — Educational**
> **Title:** What Does It Cost to Adopt an African Grey Parrot? | Published Rescue Fees vs Breeder Pricing vs the Listings That Look Too Cheap | A Breeder's Honest Ledger | C.A.Gs – Midland, TX — Congo and Timneh Cost of Ownership
>
> **Description:** Rescues publish $450–$1,500. Breeders list $1,500–$8,500. We show what each route really costs across day one, year one and five years — with the paperwork, the vet bills and the forty-year commitment counted in.

**Set 3 — Benefit-Solution**
> **Title:** African Grey Parrot Adoption Cost Explained | Which Route Fits Your Budget? | 4 Documented Greys Reservable From $1,500 | C.A.Gs – Midland, TX — Hand-Raised, DNA-Sexed, CITES Papered, Shipped Nationwide
>
> **Description:** Work out your real number before you commit. Compare adoption fees, breeder pricing and lifetime cost, then meet the documented Congos and Timnehs we have reservable now. 24-hour reply from Mark and Teri.

---

## 6. Counter snippets — 8, Ledger-verified

`$1,500 Floor Price` · `$185 Airport Tier` · `$350 Home Tier` · `12+ Yrs Aviary` ·
`100% CITES Papered` · `0 Wild-Caught` · `24h Reply` · `40–60 Yr Span`

---

## 7. Reviews — both real, both unspent in the for-sale cluster

| Reviewer | Location | Image (already in `public/`) | Why this page |
|---|---|---|---|
| **Lawrence Brunner** | Fullerton, CA | `/lawrence-brunner-fullerton-ca-review.webp` | Money-angled and scam-angled — a prior deposit scam, then full documentation, closing on value for money. The single most on-angle review we hold. |
| **Ida Brim** | Nashville, TN | `/ida-brim-nashville-tn-review.webp` | Delivery and documentation delivered as promised — supports section 18. |

Both texts are lifted **verbatim** from `src/pages/available/roys/index.astro`; real reviews are on the
CLAUDE.md verbatim whitelist. Spent elsewhere in the cluster and therefore excluded: Archie O'Brien,
Richard Woodard, Meredith, Jeffrey, Joanna, Anthony, Jesse. `data/case-studies.json` holds
`case_studies: []` — there is no data-file source of new reviews, and none were invented.

Note: neither reviewer's state matches the geo set. That is correct — real people are not relocated to
fit a distribution plan.

---

## 8. Internal links — Link-First anchors, Anchor Diversity Ledger enforced

| Target | Proposed anchor (all unspent) |
|---|---|
| `/african-grey-parrot-price/` | Our cost-of-ownership breakdown |
| `/african-grey-adoption/` | Where adoption actually works |
| `/affordable-african-grey-birds-for-sale/` | Our lowest-priced documented greys |
| `/congo-african-grey-for-sale/` | Congo pricing in detail |
| `/timneh-african-grey-for-sale/` | Timneh pricing starts lower |
| `/african-greys-for-sale-with-health-guarantee/` | The guarantee attached to every price |
| `/african-grey-parrot-lifespan/` | A forty-to-sixty-year bird |
| `/how-to-avoid-african-grey-parrot-scams/` | Listings priced below our floor |
| `/` (homepage `#tools`) | Our quick first-year estimate |
| 6 geo pages | New Jersey · Massachusetts · Minnesota · Missouri · Oregon · Indiana |
| 6 `/available/` birds | by name |

**`.xsell` targets** — must avoid the spent anchors recorded in the impeccable-lessons doc §6.

## 9. External links — minimum 10 across 8+ domains, all fetched and live

parrotsfirst.org (fee schedule) · phoenixlanding.org (fee schedule + the "minimal compared to" line) ·
companionparrots.org · riparrots.org · floridaparrotrescue.com · cites.org (Appendix I, CoP17) ·
aphis.usda.gov (AWA licensing) · parrots.org / World Parrot Trust · iucnredlist.org (Endangered) ·
2 × r/parrots threads. New tab + arrow. Cite the specific resource page, never a homepage.

---

## 10. Pre-write header dup gate

Run before the outline goes to the breeder:

```bash
python3 scripts/dup_content_audit.py --headers
```

Zero non-whitelist crossover required. Note the recorded lesson: three headings cleared this same gate
on the health-guarantee build and still collided once built — Task 9 runs it again on the built page,
and that run is the one that counts.

---

## 11. Open flags

1. PAA at 11 of 15 — finish at `@cag-paa-agent` in Sprint 2.
2. Bing query export still missing.
3. Homepage calculator hardcodes `Timneh — $1,600` against `price-matrix.json`'s `$1,500–$1,600`.
4. Legacy `/product/` duplicate URLs still drawing impressions — separate cleanup.

# CongoAfricanGreys.com — Page Cannibalization Audit
**Date:** 2026-05-22
**Total pages audited:** 84+

---

## Cluster 1: "African Grey For Sale" — HIGH PRIORITY (9 pages competing)

These pages all target the same primary intent (buy an African Grey parrot) with overlapping meta descriptions mentioning USDA/CITES/hand-raised. Google will consolidate rankings and typically only surfaces 1–2.

| URL | Role | Recommended Action |
|-----|------|--------------------|
| `/` (homepage) | Brand/hub | KEEP — differentiate with "home" schema, diverse content |
| `/african-grey-parrot-for-sale/` | Transactional hub | KEEP — should be the primary "for sale" page |
| `/african-grey-parrots-for-sale/` | Location hub | KEEP — hub for state pages, differentiate scope |
| `/congo-african-grey-for-sale/` | Congo variant | KEEP — differentiate with subspecies-specific content |
| `/timneh-african-grey-for-sale/` | Timneh variant | KEEP — already differentiated by variant |
| `/baby-african-grey-parrot-for-sale/` | Age modifier | KEEP — differentiate with weaning timeline, baby-specific content |
| `/hand-raised-african-grey-parrot-for-sale/` | Method modifier | DIFFERENTIATE — needs unique angle vs baby page (focus on socialization process, not age) |
| `/captive-bred-african-grey-parrot/` | Compliance modifier | DIFFERENTIATE — must be clearly informational/trust, not a "buy" page; add CITES detail not on other pages |
| `/affordable-african-grey-birds-for-sale/` | Price modifier | DIFFERENTIATE or CONSOLIDATE into price page — redirect to `/african-grey-parrot-price/` if thin |

**Priority fix:** `/hand-raised-african-grey-parrot-for-sale/` and `/captive-bred-african-grey-parrot/` need unique content angles or should 301 to the nearest hub.

---

## Cluster 2: "Near Me" — MEDIUM PRIORITY (3 pages competing)

| URL | Role | Recommended Action |
|-----|------|--------------------|
| `/african-grey-parrot-for-sale-near-me/` | Primary near-me | KEEP — should be the canonical "near me" page |
| `/african-grey-parrots-for-sale-near-me/` | Plural variant | CONSOLIDATE — 301 redirect to `/african-grey-parrot-for-sale-near-me/` ✅ Done |
| `/buy-african-grey-parrot-near-me/` | Buy modifier | CONSOLIDATE — 301 redirect to `/african-grey-parrot-for-sale-near-me/` ✅ Done |
| `/where-to-buy-african-greys-near-me/` | Question form | DIFFERENTIATE — reposition as "how to verify a breeder near you" guide, not a buy page |

**Priority fix:** 301 redirects for the two thin "near me" variants applied on 2026-05-22.

---

## Cluster 3: Care / Diet — MEDIUM PRIORITY (4 pages competing)

| URL | Role | Recommended Action |
|-----|------|--------------------|
| `/african-grey-care/` | Hub page | KEEP — hub linking to all spokes; differentiate with hub schema |
| `/african-grey-parrot-care-guide/` | Main care guide | KEEP — 4,500+ word guide; canonical care content |
| `/african-grey-parrot-diet/` | Diet spoke | KEEP — diet-specific; clearly differentiate from food product guide |
| `/best-african-grey-parrot-food/` | Food product guide | KEEP — reposition as product recommendation guide (Harrison's, Zupreem), not a diet science page |

**Priority fix:** `/african-grey-care/` and `/african-grey-parrot-care-guide/` have overlapping descriptions. Update `/african-grey-care/` description to "Hub" framing; update `/african-grey-parrot-care-guide/` to "Complete Guide" framing.

---

## Cluster 4: "Adoption" vs "Purchase" — LOW PRIORITY (2 pages competing)

| URL | Role | Recommended Action |
|-----|------|--------------------|
| `/african-grey-adoption/` | Adoption framing | KEEP — "adoption" framing appeals to buyers who don't want to feel like they're "buying" a pet; valid intent |
| `/african-grey-parrot-adoption-cost/` | Cost breakdown | KEEP — informational; cost-conscious buyer intent |

**Note:** These target different user mindsets. The adoption page needs to lean harder into the emotional/lifestyle framing; the cost page should be purely factual with tables.

---

## Cluster 5: Comparison Pages — LOW PRIORITY

All comparison pages (`/african-grey-vs-cockatoo/`, `/african-grey-vs-macaw/`, `/african-grey-vs-amazon-parrot/`, `/congo-vs-timneh-african-grey/`, `/male-vs-female-african-grey-parrots-for-sale/`) target distinct intents. No cannibalization detected.

---

## Immediate Actions Completed (2026-05-22)

1. **301 Redirects applied** in `public/_redirects`:
   ```
   /african-grey-parrots-for-sale-near-me/   /african-grey-parrot-for-sale-near-me/   301
   /buy-african-grey-parrot-near-me/          /african-grey-parrot-for-sale-near-me/   301
   ```

---

## Next Sprint Actions

2. **Meta Description Differentiation** — Update these pages' meta descriptions to signal distinct intent:
   - `/hand-raised-african-grey-parrot-for-sale/` → Focus on socialization process, not age
   - `/captive-bred-african-grey-parrot/` → Focus on CITES compliance documentation, make informational not transactional
   - `/affordable-african-grey-birds-for-sale/` → Focus on price transparency, link to price guide

3. **Care Cluster Descriptions** — Update:
   - `/african-grey-care/` → "Hub for all African Grey care resources: diet, health, training, lifespan"
   - `/african-grey-parrot-care-guide/` → "Complete 4,500-word African Grey care guide covering housing, diet, health, and enrichment"

4. **Monitor in GSC** — After redirects, check in 4–6 weeks whether the consolidated "near me" page (`/african-grey-parrot-for-sale-near-me/`) gains impressions from the redirected URLs.

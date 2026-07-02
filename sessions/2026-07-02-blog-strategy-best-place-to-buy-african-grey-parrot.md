# Blog Strategy — /blog/best-place-to-buy-african-grey-parrot/
> Session: 2026-07-02 · Batch-2 Page 1 of 5 · Status: AWAITING BREEDER APPROVAL (frameworks/angle/keywords/outline/images)

## 1. Page + Primary KW + Intent Split
- **URL:** https://congoafricangreys.com/blog/best-place-to-buy-african-grey-parrot/
- **Primary KW:** "Best Place to Buy African Grey Parrot"
- **Intent:** 55% Transactional · 35% Commercial Investigation · 10% Scam-avoidance (per brief). Live SERP confirms: buyers hunting a *trustworthy* seller.

## 2. Content-type verdict
Competitors post either (a) classified listings or (b) generic care articles that don't sell. **Recommended C.A.Gs posture:** a *decision guide* — "the 5 places ranked by risk" — buyer-advocate voice, links OUT to money pages. NOT a listing page (cannibalization risk, §5).

## 3. Top-3 Google (from brief / ChatGPT)
1. Birds Now (marketplace) — huge inventory, exact-match city pages; weakness = scam exposure, zero trust.
2. Small breeder sites — warm/local; weakness = thin SEO, no depth.
3. PetMD / The Spruce Pets (educational) — DR authority; weakness = don't sell, no first-hand breeder experience.

## 4. Fresh live SERP (Firecrawl, 2026-07-02, US)
"best place to buy african grey parrot": 1) **Reddit r/AfricanGrey** ("legit website? insane amount of scams") 2) birdbreeders.com (classified) 3) exoticglobalparrotsfarm 4) psittacus.com 5) anasparrots 6) Facebook group 7) birdmansparrots 8) exoticparrotsplanet.
"where to buy... reputable breeder": 1) **Reddit** 2) **parrotforums** 3) graybreedersfoundation (MAP-certified) 4) birdbreeders 5) FB group 6) rainforestaviaries 7) YouTube 8) featherlandbreedershub.
**Signal:** SERP is community-trust-seeking + thin sellers. NO structured authoritative guide owns it. Wide-open AEO/snippet lane.

## 5. 30-competitor registry signal + CANNIBALIZATION GUARDRAIL
- Registry Tier-1 direct breeders (afrigreyparrots, shadesofgreys, williamsafricangreys, compoundexotics) rank locally, thin content. Tier-2 classifieds (BirdsNow, BirdBreeders, Hoobly) own listing intent. Tier-3 (Spruce, All About Parrots) own education. **Gap = the trust-ranked decision guide bridging the two.**
- **INTERNAL cannibalization (critical):** siblings already own transactional + scam intent — `/buy-african-grey-parrot-near-me/`, `/african-grey-parrots-for-sale-near-me/`, `/buy-african-grey-parrots-with-shipping/`, `/african-grey-parrot-breeders-comparison/`, interior `/how-to-avoid-african-grey-parrot-scams/`, and the price blog `/african-grey-parrot-price-what-you-get/`. → This blog must take the **buyer-education "where + how to choose, ranked by risk"** angle and LINK OUT to those money/scam pages. It does NOT re-teach scam tactics in depth (link to scam page) or list live inventory (link to for-sale hub).

## 6. Winning angle (moat)
"The 5 Safest Places to Buy an African Grey — Ranked by Risk" + first-hand breeder E-E-A-T ("buyers reach us after nearly losing deposits to fake breeders"). Snippet + AI-citation friendly.

---
## BUILD COMPLETE (2026-07-02) — PASS, ~5,926 words, images pending
Page built: `src/pages/blog/best-place-to-buy-african-grey-parrot/index.astro`. `final_page_audit.py` → **[PASS]** (H1:1 H2:12 H3:24 H4:14 H5:7 H6:5, zero skips; Article+FAQPage+HowTo+Breadcrumb+ImageObject schema). Framework PAS+EBP+QAB; angle "5 Sources Ranked by Risk". Cannibalization handled — links OUT to price blog, scam interior page, /available/, contact.

### IMAGE MANIFEST — drop generated WebP at these exact paths (all placeholders now)
Each infographic also needs a `-760w.webp` variant; hero needs `-480w` + `-800w`. Flat-design palette: forest-green #2D6A4F, clay #e8604c, cream #faf7f4, IBM Plex Sans, line icons (no emoji). Verify data/text legibility after generation.

1. **HERO** 16:9 1600×900 → `/best-place-buy-african-grey-hero.webp` (+480w,+800w)
   Prompt: Photoreal editorial — healthy hand-raised Congo African Grey (silver scalloped plumage, red tail, pale eye) on a natural manzanita perch in a clean, warm home aviary; breeder's hands loosely offering a foraging toy, softly out of focus; cream+forest-green palette, warm natural window light, soft warm shadows, premium breeder feel. No text, no logo, no other species, no cold/clinical studio light, no price overlay.
2. **RANKED-BY-RISK infographic** 1200×700 → `/african-grey-5-safest-places-to-buy-ranked-by-risk-infographic.webp` (+760w)
   Prompt: Flat-design vertical ranking, title "The 5 Safest Places to Buy an African Grey — Ranked by Risk". Rows low→high risk: 1 Licensed Breeder (green, shield), 2 Rescue/Adoption (green), 3 Bird Expo (amber), 4 Pet Store (amber), 5 Online Marketplace (clay red, warning). Legible labels.
3. **SOURCE COMPARISON infographic** 1200×700 → `/where-to-buy-african-grey-breeder-vs-marketplace-vs-rescue-comparison.webp` (+760w)
   Prompt: Flat 4-column table "Where to Buy — Source Comparison": Breeder / Marketplace / Rescue / Pet Store × rows Price, Scam Risk, Health Record, Trust; green/amber/clay markers; forest-green header band.
4. **REPUTABLE-BREEDER checklist** 1200×700 → `/how-to-spot-a-reputable-african-grey-breeder-checklist.webp` (+760w)
   Prompt: Flat checklist "How to Spot a Reputable African Grey Breeder", 5 checked items: live video call · CITES/DNA/vet paperwork · verifiable USDA licence · one fair fixed price · reversible deposit. Green checks, line icons.
5. **RED-FLAGS infographic** 1200×700 → `/african-grey-buyer-red-flags-walk-away-infographic.webp` (+760w)
   Prompt: Flat warning "Red Flags: Walk Away", 5 tiles: price far below $1,500 · no CITES/DNA/vet papers · won't video-call · wire/gift-card/crypto demand · urgency pressure. Clay warning accents on cream.
6. **TRUST photo** 4:3 1200×900 → `/why-buyers-choose-cags-trusted-african-grey-breeder.webp` (+760w)
   REAL brand photo (Mark & Teri + a hand-raised Congo in Midland TX) — original media for E-E-A-T; not AI, or an approved brand shot.

### DEPLOY GATE
Do NOT commit/push until images are placed (main auto-deploys → 6 broken imgs would go live). After images: optimize to WebP (Pillow, hero+first-image get srcset variants), rebuild, re-run `final_page_audit.py`, then commit + push + `generate_sitemaps.py`.

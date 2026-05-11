# CAG Page Architecture — Full Inventory

**Last updated:** 2026-05-11
**Source:** gap-matrix-2026-05-11.md + keyword-gap-2026-05-11.md + data/structure.json
**Total target pages:** 52 (Tier 0–5)

---

## Tier 0 — Money Pages (Direct Revenue, P0)

| Slug | H1 Target | Priority | Build Agent | Status |
|------|-----------|----------|-------------|--------|
| `/` | African Grey Parrots for Sale — Captive-Bred | P0 | cag-homepage-builder | built |
| `/congo-african-grey-for-sale/` | Congo African Grey for Sale | P0 | cag-variant-specialist | built |
| `/timneh-african-grey-for-sale/` | Timneh African Grey for Sale | P0 | cag-timneh-specialist | built |
| `/african-grey-breeding-pair-for-sale/` | African Grey Breeding Pair for Sale | P0 | cag-hub-builder | built |
| `/available/` | Available African Grey Parrots | P0 | cag-clutch-manager | needs rebuild |
| `/contact-us/` | Contact CongoAfricanGreys.com | P0 | manual | built |

---

## Tier 1 — Location Pages (22 States, Reverse Silo)

Hub: `/african-grey-parrots-for-sale/` → all 22 state spokes  
Schema: LocalBusiness + FAQPage + BreadcrumbList per page

| Slug | H1 Target | Priority | Build Agent | Status |
|------|-----------|----------|-------------|--------|
| `/african-grey-parrot-for-sale-florida/` | African Grey Parrot for Sale in Florida | P0 | cag-location-builder | built |
| `/african-grey-parrot-for-sale-texas/` | African Grey Parrot for Sale in Texas | P0 | cag-location-builder | built |
| `/african-grey-parrot-for-sale-new-york/` | African Grey Parrot for Sale in New York | P0 | cag-location-builder | built |
| `/african-grey-parrot-for-sale-ohio/` | African Grey Parrot for Sale in Ohio | P0 | cag-location-builder | built |
| `/african-grey-parrot-for-sale-california/` | African Grey Parrot for Sale in California | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-illinois/` | African Grey Parrot for Sale in Illinois | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-pennsylvania/` | African Grey Parrot for Sale in Pennsylvania | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-georgia/` | African Grey Parrot for Sale in Georgia | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-north-carolina/` | African Grey Parrot for Sale in North Carolina | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-michigan/` | African Grey Parrot for Sale in Michigan | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-new-jersey/` | African Grey Parrot for Sale in New Jersey | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-virginia/` | African Grey Parrot for Sale in Virginia | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-washington/` | African Grey Parrot for Sale in Washington | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-arizona/` | African Grey Parrot for Sale in Arizona | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-massachusetts/` | African Grey Parrot for Sale in Massachusetts | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-tennessee/` | African Grey Parrot for Sale in Tennessee | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-indiana/` | African Grey Parrot for Sale in Indiana | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-missouri/` | African Grey Parrot for Sale in Missouri | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-maryland/` | African Grey Parrot for Sale in Maryland | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-colorado/` | African Grey Parrot for Sale in Colorado | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-minnesota/` | African Grey Parrot for Sale in Minnesota | P1 | cag-location-builder | needs build |
| `/african-grey-parrot-for-sale-south-carolina/` | African Grey Parrot for Sale in South Carolina | P1 | cag-location-builder | needs build |

**States built:** 4 of 22  
**States needed:** California, Illinois, Pennsylvania, Georgia, North Carolina, Michigan, New Jersey, Virginia, Washington, Arizona, Massachusetts, Tennessee, Indiana, Missouri, Maryland, Colorado, Minnesota, South Carolina

---

## Tier 2 — Trust & Authority Pages (Score ≥8, Flat Cluster)

Schema: FAQPage + BreadcrumbList; /about/ also gets Organization + Person schema

| Slug | H1 Target | Priority | Build Agent | Status |
|------|-----------|----------|-------------|--------|
| `/cites-african-grey-documentation/` | CITES African Grey Documentation: What Every Buyer Must Know | P0 | cag-scam-specialist | needs build |
| `/how-to-avoid-african-grey-parrot-scams/` | How to Avoid African Grey Parrot Scams | P0 | cag-scam-specialist | needs build |
| `/usda-licensed-african-grey-breeder/` | USDA Licensed African Grey Breeder | P1 | cag-about-builder | needs build |
| `/about/` | About CongoAfricanGreys.com — Mark & Teri Benjamin | P1 | cag-about-builder | needs build |
| `/african-grey-reviews/` | African Grey Parrot Reviews — Real Buyer Stories | P2 | cag-trust-signals-agent | needs build |
| `/why-choose-congoafricangreys/` | Why Choose CongoAfricanGreys.com | P2 | cag-trust-signals-agent | needs build |

**Competitive advantage:** Zero competitors have CITES documentation or scam prevention pages — highest opportunity score (10/10) in keyword gap analysis.

---

## Tier 3 — Species, Comparison & Purchase Pages (Score ≥7)

Schema: Product + Offer + FAQPage (variant pages); Article + FAQPage (comparison pages)

| Slug | H1 Target | Priority | Build Agent | Status |
|------|-----------|----------|-------------|--------|
| `/african-grey-parrot-guide/` | The Complete African Grey Parrot Guide | P1 | cag-species-guide-builder | needs build |
| `/african-grey-parrot-price/` | African Grey Parrot Price: Complete Cost Guide | P0 | cag-financial-strategist | needs build |
| `/buy-african-grey-parrot-near-me/` | Buy African Grey Parrot Near Me | P0 | cag-purchase-guide | needs build |
| `/congo-vs-timneh-african-grey/` | Congo vs Timneh African Grey: Full Comparison | P1 | cag-comparison-builder | needs build |
| `/male-vs-female-african-grey-parrots-for-sale/` | Male vs Female African Grey Parrots | P2 | cag-comparison-builder | built |
| `/african-grey-vs-macaw/` | African Grey vs Macaw: Which Is Right for You? | P2 | cag-comparison-builder | needs build |
| `/african-grey-vs-cockatoo/` | African Grey vs Cockatoo: Side-by-Side Comparison | P2 | cag-comparison-builder | needs build |

---

## Tier 4 — Blog / Care Content (8 Posts, Score ≥8)

Hub: `/african-grey-care/` → all blog spokes  
Schema: Article + FAQPage + BreadcrumbList + Person (author) per post  
Competitor context: The Spruce Pets is the only real competitor; no breeder has any blog content.

| Slug | Topic | Target Keyword | Priority | Build Agent | Status |
|------|-------|----------------|----------|-------------|--------|
| `/blog/african-grey-parrot-care-guide/` | Comprehensive Care Guide | african grey parrot care guide | P1 | cag-blog-post-agent | needs build |
| `/blog/african-grey-diet-and-nutrition/` | Diet & Nutrition | african grey diet and nutrition | P1 | cag-blog-post-agent | needs build |
| `/blog/african-grey-parrot-training/` | Training & Talking | african grey parrot training | P1 | cag-blog-post-agent | needs build |
| `/blog/african-grey-parrot-lifespan/` | Lifespan & Longevity | african grey parrot lifespan | P1 | cag-blog-post-agent | needs build |
| `/blog/african-grey-health-problems/` | Common Health Problems | african grey parrot health problems | P2 | cag-blog-post-agent | needs build |
| `/blog/african-grey-parrot-cage-setup/` | Cage Setup & Enrichment | african grey parrot cage setup | P2 | cag-blog-post-agent | needs build |
| `/blog/african-grey-parrot-talking-ability/` | Talking Ability Deep Dive | african grey parrot talking ability | P2 | cag-blog-post-agent | needs build |
| `/blog/african-grey-parrot-facts/` | 12 Key Facts | african grey parrot facts | P2 | cag-blog-post-agent | needs build |
| `/blog/is-african-grey-good-for-beginners/` | Beginner Suitability Guide | is african grey good for beginners | P2 | cag-blog-post-agent | needs build |
| `/blog/how-long-do-african-grey-parrots-live/` | Longevity Questions (PAA variant) | how long do african grey parrots live | P2 | cag-blog-post-agent | needs build |

---

## Tier 5 — Hub Pages (3 Aggregator Hubs)

| Slug | Purpose | Links To | Priority | Build Agent | Status |
|------|---------|----------|----------|-------------|--------|
| `/african-grey-parrots-for-sale/` | Location hub — aggregates all 22 state spokes | All 22 state pages | P0 | cag-hub-builder | needs build |
| `/african-grey-comparison/` | Comparison hub — aggregates all comparison pages | Congo vs Timneh, Male vs Female, vs Macaw, vs Cockatoo | P1 | cag-hub-builder | needs build |
| `/african-grey-care/` | Care hub — aggregates all blog post spokes | All 10 blog posts | P1 | cag-hub-builder | needs build |

---

## Page Count Summary

| Tier | Description | Total | Built | Needs Build |
|------|-------------|-------|-------|-------------|
| Tier 0 | Money pages | 6 | 5 | 1 (/available/ rebuild) |
| Tier 1 | Location pages (22 states) | 22 | 4 | 18 |
| Tier 2 | Trust & authority pages | 6 | 0 | 6 |
| Tier 3 | Species / comparison / purchase | 7 | 1 | 6 |
| Tier 4 | Blog / care posts | 10 | 0 | 10 |
| Tier 5 | Hub pages | 3 | 0 | 3 |
| **Total** | | **54** | **10** | **44** |

---

## Build Order (Priority Queue)

### Sprint 1 — No-Build SEO Wins (Days 1–7)
1. Add FAQPage schema to all 10 existing pages (pure schema addition)
2. Add "hand raised", "DNA tested", "captive-bred" language to all money page copy
3. Add CITES trust bar component to all pages
4. Fix /available/ bird profiles with named birds from clutch-inventory.json

### Sprint 2 — Highest-ROI New Pages (Days 8–21)
1. `/african-grey-parrots-for-sale/` — location hub (enables Google to see state page cluster)
2. `/african-grey-parrot-price/` — zero competition; high volume; converts comparison shoppers
3. `/cites-african-grey-documentation/` — zero competition; legal-research buyers
4. `/how-to-avoid-african-grey-parrot-scams/` — zero competition; scam-anxious buyers
5. `/buy-african-grey-parrot-near-me/` — high-intent purchase query

### Sprint 3 — State Location Expansion (Days 15–45)
Priority order: California → Georgia → Illinois → Pennsylvania → North Carolina → Michigan → New Jersey → Virginia → Washington → Arizona → Massachusetts → Tennessee → Indiana → Missouri → Maryland → Colorado → Minnesota → South Carolina

### Sprint 4 — Blog & Authority (Days 30–60)
1. `/about/` — EEAT signal; Person schema for Mark & Teri Benjamin
2. `/usda-licensed-african-grey-breeder/`
3. 4 blog posts: care guide, diet, training, lifespan
4. `/congo-vs-timneh-african-grey/` — zero competition from all 30 competitors
5. 4 remaining blog posts: health, cage, talking, facts, beginner guide

### Sprint 5 — Comparison & Conversion Layer (Days 60–90)
1. `/african-grey-vs-macaw/`
2. `/african-grey-vs-cockatoo/`
3. `/african-grey-comparison/` hub
4. `/african-grey-care/` hub
5. `/african-grey-reviews/` and `/why-choose-congoafricangreys/`
6. Named bird profiles on /available/ with affiliate supply links

---

## Internal Link Architecture

### Reverse Silo (Location Cluster)
- Every state page MUST link UP to `/african-grey-parrots-for-sale/` with anchor: "African Grey parrots for sale across the USA"
- Hub links DOWN to all 22 state pages
- Homepage links to hub

### Top-Down Silos (Variant + Comparison + Blog)
- Species guide hub links DOWN to Congo, Timneh, Breeding Pair pages
- Each variant page links ACROSS to comparison pages
- Comparison hub links DOWN to all comparison spokes
- Care hub links DOWN to all blog posts
- Each blog post links UP to care hub + DOWN to one money page

### Flat Clusters (Trust & Purchase)
- All trust pages are ≤1 click from homepage
- Cross-linking: scam page → CITES page → about page
- Every trust page links DOWN to /available/ or a variant page

### Universal Rules
- Every page: minimum 3 internal links
- Anchor text: must include target keyword (never "click here" or "learn more")
- Money pages: must link to contact page or inquiry form
- Blog posts: must link to at least 1 money page per post

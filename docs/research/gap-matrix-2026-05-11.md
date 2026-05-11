# CAG Competitor Gap Matrix
**Date:** 2026-05-11  
**Scope:** Top 10 Tier 1 direct competitors analyzed  
**Previous matrix:** gap-matrix-2026-04-28.md

---

## Competitor Status Overview

| Competitor | URL | Status | Threat | Key Finding |
|-----------|-----|--------|--------|-------------|
| afrigreyparrots | afrigreyparrots.com | Active | LOW | WordPress/WooCommerce SPA, targets cheap buyers, no trust signals |
| exoticParrotPetstore | exoticparrotpetstore.com | Active | VERY LOW | JS SPA, "pet store" framing, zero schema, no content |
| afroBirdsFarm | afrobirdsfarm.com | BLOCKED | UNKNOWN | Timeout on fetch — retry manually |
| **africanGrayParrotsForSale** | africangrayparrotsforsale.com | **Active** | **MEDIUM** | **Best competitor: LocalBusiness schema, 1,360 words, $1,000 pricing anchor, 5 states** |
| silvergateBirdFarm | silvergatebirdfarm.com | BLOCKED | UNKNOWN | Cloudflare WAF — established enough to protect |
| birdsForSales | birdsforsales.com | Active | VERY LOW | Multi-species marketplace, no specialist authority |
| exoticParrotsPlanet | exoticparrotsplanet.com | Active | VERY LOW | "Global leader" claim with zero proof, no schema |
| williamsAfricanGreys | williamsafricangreys.com | INACCESSIBLE | VERY LOW | SSL error — likely dead/abandoned |
| shadesOfGreys | shadesofgreys.com | Active | VERY LOW | Georgia-only, no schema, no content |
| africanGreyAviaries | africangreyaviaries.com | **DEAD** | **NONE** | Domain expired — competitor eliminated |
| compoundExotics | compoundexotics.com | Active | LOW-MEDIUM | Multi-species, 12,441 words, WhatsApp CTA, ~$400-500 pricing |

---

## Universal Gaps (ALL competitors missing these)

These are gaps every single competitor has. CAG builds these = immediate differentiation.

### 1. CITES Documentation Content
**Gap:** 0 of 10 competitors mention CITES Appendix II or captive-bred documentation  
**Opportunity score:** 10/10  
**Build:** `/cites-documentation/` page + CITES trust bar on every page  
**Why it wins:** African Grey buyers research CITES — capturing this = high-intent traffic with zero competition

### 2. USDA AWA Licensing
**Gap:** 0 of 10 mention USDA Animal Welfare Act licensing  
**Opportunity score:** 9/10  
**Build:** Trust bar component + About page credential block  
**Why it wins:** USDA is a Google EEAT signal — official government licensing that competitors cannot fake

### 3. FAQPage Schema
**Gap:** 0 of 10 have FAQPage JSON-LD  
**Opportunity score:** 9/10  
**Build:** 8-12 FAQ per page with FAQPage schema  
**Why it wins:** FAQPage = rich results + AI Overview citations + Featured Snippets

### 4. Geographic State Pages
**Gap:** Best competitor (africangrayparrotsforsale.com) targets only 5 states in-page content. No competitor has dedicated state landing pages.  
**Opportunity score:** 10/10  
**Build:** 22 dedicated state pages (/african-grey-parrot-for-sale-[state]/)  
**Why it wins:** High-volume transactional queries ("african grey for sale in texas") with zero dedicated competition

### 5. Blog / Care Content
**Gap:** 1 of 10 has any blog presence (exoticParrotPetstore has a blog link but it's empty)  
**Opportunity score:** 8/10  
**Build:** 12+ info/care pages (lifespan, diet, talking, training, care guide)  
**Why it wins:** Informational queries drive awareness → trust → purchase. Competitors have abandoned this entirely.

### 6. Scam Prevention Page
**Gap:** 0 of 10 have a scam-prevention page  
**Opportunity score:** 9/10  
**Build:** `/how-to-avoid-african-grey-parrot-scams/`  
**Why it wins:** "african grey parrot scam" has significant search volume and is purely trust-based. Buyer who finds this page is primed to convert.

### 7. DNA Sexing Documentation
**Gap:** Only 1 of 10 (africangrayparrotsforsale) mentions DNA testing — and only in meta description  
**Opportunity score:** 8/10  
**Build:** DNA sexing cert mentioned in trust bar, about page, and every bird profile  
**Why it wins:** Differentiates from unverified sellers; builds EEAT

### 8. Family Breeder Story / Person Identity
**Gap:** 0 of 10 name the actual breeders or tell a family story  
**Opportunity score:** 8/10  
**Build:** About page (H-S-S framework), Mark & Teri Benjamin, Person schema  
**Why it wins:** EEAT requires real people behind real experience — no competitor provides this

### 9. Named Bird Profiles
**Gap:** compoundExotics lists "5 African Grey Parrots" but no individual profiles  
**Opportunity score:** 7/10  
**Build:** Individual bird pages for Bery, Joys, Amie, Loti, Carl, Roys + /available-birds/ hub  
**Why it wins:** Product pages with real photos, personality profiles, and pricing capture bottom-of-funnel buyers

### 10. Comparison Pages
**Gap:** 0 of 10 have Congo vs Timneh, vs macaw, vs cockatoo, or other comparison content  
**Opportunity score:** 7/10  
**Build:** 8 comparison pages (/congo-vs-timneh-african-grey/, etc.)  
**Why it wins:** Commercial investigation queries — high intent, low competition

---

## Pricing Intelligence

| Competitor | Price Point | Positioning |
|-----------|-------------|-------------|
| africangrayparrotsforsale.com | $1,000 | Budget/volume |
| compoundexotics.com | ~$400-500 | Budget exotic store |
| afrigreyparrots.com | Unknown | Likely budget (targets "cheap" angle) |
| **CAG** | **$1,500–$3,000** | **Premium, documented, family-raised** |

**Key insight:** CAG's premium pricing is 2-6x competitors. This requires a content strategy that justifies the price gap — CITES docs, USDA licensing, DNA sexing, 12-year track record, family story, health guarantee. The `/african-grey-parrot-price/` page should explicitly address the price differential.

---

## Schema Gap Analysis

| Schema Type | CAG Competitors | CAG Target |
|------------|----------------|------------|
| LocalBusiness | 1/10 | YES — every geo page |
| FAQPage | 0/10 | YES — every page |
| Product + Offer | 1/10 | YES — all bird listings |
| Person | 0/10 | YES — About page |
| Organization | 3/10 | YES — homepage |
| BreadcrumbList | 3/10 | YES — all pages |
| VideoObject | 0/10 | YES — YouTube content |
| HowTo | 0/10 | YES — training/care pages |

---

## Technical Gaps

| Signal | Competitors With | CAG Target |
|--------|-----------------|------------|
| Mobile-first, fast load | Unknown (most are JS SPAs) | Astro static = 100 Perf score |
| SSL active | 7/10 (3 dead/blocked) | YES |
| Sitemap | 6/10 | YES + IndexNow |
| Absolute canonical | Unknown | YES — enforced |
| Core Web Vitals optimized | 0/10 known | YES — Astro static |

---

## Priority Build Order (From Gap Analysis)

### Immediate (Week 1)
1. **CITES documentation trust bar** — component used on every page
2. **22 state geo pages** — no competitor has these, pure blue ocean
3. **Scam prevention page** — zero competition, high buyer intent
4. **FAQPage schema on all existing pages** — captures AI Overviews immediately

### Short-term (Month 1)
5. **About page with Person schema** — Mark & Teri Benjamin, H-S-S story
6. **Named bird profiles** — Bery, Joys, Amie, Loti, Carl, Roys
7. **Congo vs Timneh comparison** — no competitor has this
8. **/african-grey-parrot-price/** — address the $1,000 vs $3,000 gap directly

### Medium-term (Month 2-3)
9. **Care guide cluster** — 12 info pages targeting informational queries
10. **Blog content** — seasonal, buyer stories, clutch updates
11. **YouTube video schema** — VideoObject for any video content
12. **WhatsApp CTA** — learned from compoundExotics (only competitor with this)

---

## Dead Competitors (Opportunity to Capture)
- **africangreyaviaries.com** — domain expired. Any Google rankings they held are decaying. Target their keywords.
- **williamsafricangreys.com** — SSL error, likely dead. Same opportunity.

---

## Next Steps
1. Run `@cag-competitor-intel` on Tier 2 competitors (birdsnow.com + classifieds) for the full 30-competitor picture
2. Proceed to Astro scaffold — build the technical foundation before content
3. Start with CITES trust bar component + state geo page template
4. Wire `@cag-keyword-verifier` grader into batch-rebuilder (already updated in agent file)

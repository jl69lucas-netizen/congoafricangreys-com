# CAG Component-to-Page Assignment Matrix

**Version 2.1 — 2026-05-29** *(Added new components to main matrix; `cag-newsletter-v2` registered; homepage column updated to reflect v2 build.)*

> ⚠️ **HOMEPAGE uses the NEW components** — see "Homepage (REBUILD v2)" below. The legacy table's Homepage column is superseded. New components: `cag-hero-v3`, `cag-toc-v3`, `cag-key-takeaway-v2`, `cag-counter-snippet`, `cag-available-grid`, `cag-compare-table-e`, `cag-owner-card`, `cag-newsletter-v2` (all registered in `components.md`).

For each page type, lists which component + variant to use for each section.
"✓" = use this component on this page type. Variant shown in parentheses.

| Component | Homepage | Location | Comparison | Variant Page | Care/Guide | Blog | Scam Page | Contact/About |
|---|---|---|---|---|---|---|---|---|
| `Navbar` (classic) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `MobileNav` | ✓ | ✓ | | ✓ | | | | |
| `StickyCtaBar` | | ✓ | | ✓ | | | | |
| `cag-hero-v3` (b, Authority Green) ✅ | ✓ | | | | | | | |
| `cag-split-hero` (editorial) ⚠️ | | | | | | | | |
| `cag-split-hero` (classic) ⚠️ | | ✓ | | ✓ | | | | |
| `cag-split-hero` (dark) ⚠️ | | | ✓ | | | | ✓ | |
| `cag-counter-snippet` (4-stat) ✅ | ✓ | | | | | | | |
| `cag-key-takeaway-v2` (02, stat grid) ✅ | ✓ | | | | ✓ | ✓ | | |
| `cag-toc-v3` (02, grouped) ✅ | ✓ | | | | ✓ | ✓ | | |
| `cag-owner-card` (mark-teri) ✅ | ✓ | | | | | | | ✓ |
| `cag-available-grid` (a, pill tabs) ✅ | ✓ | | | | | | | |
| `cag-compare-table-e` (1100px) ✅ | ✓ | | ✓ | | | | | |
| `cag-newsletter-v2` (middle) ✅ | ✓ | | | | ✓ | ✓ | | |
| `cag-newsletter-v2` (bottom) ✅ | ✓ | | | | ✓ | ✓ | | |
| `cag-stats-bar` (dark) | | | | | | | | |
| `cag-stats-bar` (classic) | | ✓ | | ✓ | | | | |
| `cag-trust-stats` (classic) | ✓ | ✓ | | ✓ | | | ✓ | ✓ |
| `SnapCarousel` + `cag-bird-card` (classic) | | ✓ | | | | | | |
| `cag-bird-card` (feature) | | | | ✓ | | | | |
| `cag-parent-birds` (classic) | | | | ✓ | ✓ | | | |
| `cag-pricing-table` (classic) | ✓ | ✓ | | | | | | |
| `cag-pricing-table` (matrix) | | | ✓ | | ✓ | | | |
| `cag-care-grid` (classic) | | | | | ✓ | ✓ | | |
| `cag-care-grid` (editorial) | | | | | | | | |
| `cag-split-feature` (editorial) | ✓ | | | ✓ | ✓ | ✓ | | |
| `cag-scam-awareness` (checklist) | | | | | | | ✓ | |
| `cag-scam-awareness` (compare) | ✓ | | ✓ | | | | ✓ | |
| `cag-faq-accordion` (classic) | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | |
| `cag-faq-accordion` (editorial) | ✓ | | | | | | | |
| `cag-video-section` | ✓ | | | | ✓ | ✓ | | |
| `cag-meet-the-team` (story) ⚠️ | | | | | | | | ✓ |
| `cag-contact-form` (classic) | | | | | | | | ✓ |
| `cag-contact-form` (application) | | ✓ | | ✓ | | | | ✓ |
| `cag-newsletter` (banner) ⚠️ | | | | | | | | |
| `cag-newsletter` (split) ⚠️ | | ✓ | ✓ | ✓ | | | | |
| `cag-testimonials` (feature) | ✓ | | | | | | | |
| `cag-testimonials` (grid) | | ✓ | | ✓ | | | ✓ | |
| `cag-testimonials` (mosaic) | | | ✓ | | | | | |
| `cag-toc-v1` / `cag-toc-v2` ⚠️ | | | ✓ | | ✓ | ✓ | | |
| `cag-key-takeaway` ⚠️ | | | | | | | | |
| `cag-footer` (dark) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

> ✅ = MODERN · ⚠️ = LEGACY (do not use on new builds)

---

## Section Order by Page Type

### Homepage (REBUILD v2 — 2026-05-29) ✅ AUTHORITATIVE
Pillar homepage on the NEW component bundles. 25 core sections (see `sessions/2026-05-29-homepage-build-progress.md` for full section list and build status). All headers conversational H1–H6; links woven mid-sentence; C.A.Gs brand voice; PAA-only FAQs. Width: 1100px full-section / 760px inline text.
```
Navbar
→ 1.  Hero (cag-hero-v3:b Authority Green) + credential bar          ✅ DONE
→ 2.  cag-counter-snippet (12+ Yrs / 100% CITES / $1,500 Floor / 24h) ✅ DONE
→ 3.  cag-key-takeaway-v2:02 (stat-forward answer box)               ✅ DONE
→ 4.  cag-toc-v3:02 (grouped by part)                                ✅ DONE
→ 5.  About the Breeder — cag-owner-card (Mark & Teri, H-S-S)        ✅ DONE
→ 6.  Review block #1 (Testimonials:feature)                         ✅ DONE
→ 7.  All Products — cag-available-grid (filterable: Congo/Timneh/Pairs/Eggs) ✅ DONE
→ 8.  Eggs & Breeding Pairs (inline horizontal list)                 ✅ DONE
→ 9.  Congo section (SplitFeature:editorial)                         ✅ DONE
→ 10. Timneh section (SplitFeature:classic)                          ✅ DONE
→ 11. Comparison (cag-compare-table-e 1100px + AG-vs-species)        ✅ DONE
→ 12. Why Choose C.A.Gs (cag-split-feature:editorial)               ← RESUME HERE
→ 13. C.A.Gs vs Other Breeders (cag-scam-awareness:compare)
→ 14. Review block #2 (Testimonials:feature)
→ 15. African Grey History & Origin (Alex/Pepperberg entity moat)
→ 16. Health & Guarantee (cag-trust-stats)
→ 17. Pricing (cag-pricing-table)
→ 18. Tools (cost calculator + CITES checklist + shipping estimator)
→ 19. Shipping (IATA, assets/brand photos, 8–15 states/cities)
→ 20. Case Study / Review #3 (Testimonials:grid)
→ 21. Blog & Care Guides links
→ 22. Video (cag-video-section, YouTube placeholder)
→ 23. FAQ (cag-faq-accordion:editorial, PAA-sourced)
→ 24. How to Buy → /contact-us/
→ 25. Contact + Map (ContactForm + LocalBusiness schema)
→ cag-newsletter-v2 (middle) → cag-newsletter-v2 (bottom) → Footer (dark) → MobileNav
```
Schema stack: Organization + LocalBusiness + Product + Review/AggregateRating + FAQPage + VideoObject + BreadcrumbList.

### Homepage (LEGACY v1 — superseded, do not use)
```
Navbar → SplitHero (editorial) → StatsBar (dark) → SnapCarousel + BirdCard (classic) → SplitFeature (editorial) → TrustStats (classic) → Testimonials (feature) → VideoSection → ParentBirds (classic) → PricingTable (classic) → FaqAccordion (editorial) → Newsletter (banner) → Footer (dark) → MobileNav
```

### Location Page (state)
```
Navbar → SplitHero (classic) → TrustStats (classic) → SnapCarousel + BirdCard (classic) → StatsBar (classic) → PricingTable (classic) → ContactForm (application) → Testimonials (grid) → FaqAccordion (classic) → Newsletter (split) → Footer (dark) → MobileNav + StickyCtaBar
```

### Comparison Page
```
Navbar → SplitHero (dark) → PricingTable (matrix) → ScamAwareness (compare) → TocV2 → Testimonials (mosaic) → FaqAccordion (classic) → Newsletter (split) → Footer (dark)
```

### Variant Page (Congo / Timneh for sale)
```
Navbar → SplitHero (classic) → StatsBar (classic) → BirdCard (feature) → ParentBirds (classic) → PricingTable (classic) → SplitFeature (editorial) → TrustStats (classic) → Testimonials (grid) → ContactForm (application) → FaqAccordion (classic) → Newsletter (split) → Footer (dark) → MobileNav + StickyCtaBar
```

### Care / Guide / Species Page
```
Navbar → SplitHero (editorial) → [cag-toc-v3:02 sidebar] → CareGrid (classic) → SplitFeature (editorial) → cag-key-takeaway-v2:02 → VideoSection → ParentBirds (classic) → FaqAccordion (classic) → cag-newsletter-v2 (bottom) → Footer (dark)
```

### Blog Page
```
Navbar → SplitHero (editorial, compact) → [cag-toc-v3:02 sidebar] → CareGrid (classic) → cag-key-takeaway-v2:02 → FaqAccordion (classic) → cag-newsletter-v2 (bottom) → Footer (dark)
```

### Scam Page
```
Navbar → SplitHero (dark) → TrustStats (classic) → ScamAwareness (checklist) → ScamAwareness (compare) → Testimonials (grid) → FaqAccordion (classic) → Footer (dark)
```

### Contact / About Page
```
Navbar → SplitHero (classic) → TrustStats (classic) → cag-owner-card (mark-teri) → ContactForm (classic) → Footer (dark)
```

---

## Agent Usage Note

When building any page, agents should:
1. Look up the page type in the table above
2. Use the section order as the default page structure
3. Only deviate from the matrix if the user explicitly requests a different component or variant
4. For homepage: read `sessions/2026-05-29-homepage-build-progress.md` first — sections 1–11 are built and approved; resume at Section 12

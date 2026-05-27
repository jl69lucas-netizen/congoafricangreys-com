# CAG Component-to-Page Assignment Matrix

**Version 1.0 — 2026-05-27**

For each page type, lists which component + variant to use for each section.
"✓" = use this component on this page type. Variant shown in parentheses.

| Component | Homepage | Location | Comparison | Variant Page | Care/Guide | Blog | Scam Page | Contact/About |
|---|---|---|---|---|---|---|---|---|
| `Navbar` (classic) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `MobileNav` | ✓ | ✓ | | ✓ | | | | |
| `StickyCtaBar` | | ✓ | | ✓ | | | | |
| `cag-split-hero` (editorial) | ✓ | | | | | | | |
| `cag-split-hero` (classic) | | ✓ | | ✓ | | | | |
| `cag-split-hero` (dark) | | | ✓ | | | | ✓ | |
| `cag-stats-bar` (dark) | ✓ | | | | | | | |
| `cag-stats-bar` (classic) | | ✓ | | ✓ | | | | |
| `cag-trust-stats` (classic) | ✓ | ✓ | | ✓ | | | ✓ | ✓ |
| `SnapCarousel` + `cag-bird-card` (classic) | ✓ | ✓ | | | | | | |
| `cag-bird-card` (feature) | | | | ✓ | | | | |
| `cag-parent-birds` (classic) | ✓ | | | ✓ | ✓ | | | |
| `cag-pricing-table` (classic) | ✓ | ✓ | | | | | | |
| `cag-pricing-table` (matrix) | | | ✓ | | ✓ | | | |
| `cag-care-grid` (classic) | | | | | ✓ | ✓ | | |
| `cag-care-grid` (editorial) | ✓ | | | | | | | |
| `cag-split-feature` (editorial) | ✓ | | | ✓ | ✓ | ✓ | | |
| `cag-scam-awareness` (checklist) | | | | | | | ✓ | |
| `cag-scam-awareness` (compare) | | | ✓ | | | | ✓ | |
| `cag-faq-accordion` (classic) | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | |
| `cag-faq-accordion` (editorial) | ✓ | | | | | | | |
| `cag-video-section` | ✓ | | | | ✓ | ✓ | | |
| `cag-meet-the-team` (story) | | | | | | | | ✓ |
| `cag-contact-form` (classic) | | | | | | | | ✓ |
| `cag-contact-form` (application) | | ✓ | | ✓ | | | | ✓ |
| `cag-newsletter` (banner) | ✓ | | | | | | | |
| `cag-newsletter` (split) | | ✓ | ✓ | ✓ | ✓ | ✓ | | |
| `cag-testimonials` (feature) | ✓ | | | | | | | |
| `cag-testimonials` (grid) | | ✓ | | ✓ | | | ✓ | |
| `cag-testimonials` (mosaic) | | | ✓ | | | | | |
| `cag-toc-v1` / `cag-toc-v2` | | | ✓ | | ✓ | ✓ | | |
| `cag-key-takeaway` | | | | | ✓ | ✓ | | |
| `cag-footer` (dark) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## Section Order by Page Type

### Homepage
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
Navbar → SplitHero (editorial) → [TocV1 sidebar] → CareGrid (classic) → SplitFeature (editorial) → KeyTakeaway → VideoSection → ParentBirds (classic) → FaqAccordion (classic) → Newsletter (split) → Footer (dark)
```

### Blog Page
```
Navbar → SplitHero (editorial, compact) → [TocV2 sidebar] → CareGrid (classic) → KeyTakeaway → FaqAccordion (classic) → Newsletter (split) → Footer (dark)
```

### Scam Page
```
Navbar → SplitHero (dark) → TrustStats (classic) → ScamAwareness (checklist) → ScamAwareness (compare) → Testimonials (grid) → FaqAccordion (classic) → Footer (dark)
```

### Contact / About Page
```
Navbar → SplitHero (classic) → TrustStats (classic) → MeetTheTeam (story) → ContactForm (classic) → Footer (dark)
```

---

## Agent Usage Note

When building any page, agents should:
1. Look up the page type in the table above
2. Use the section order as the default page structure
3. Only deviate from the matrix if the user explicitly requests a different component or variant

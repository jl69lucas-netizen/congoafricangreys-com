# CAG Component Theme Configurations

**Version 1.0 — 2026-05-27**

Three named theme packages — one per page purpose. When building a page, select the theme that matches the page's goal, then swap individual components only when the user explicitly requests a different variant.

---

## Theme 1: "Heritage Trust"

**Character:** Warm, editorial, content-first. Authority without aggression.
**Use for:** Homepage, care guides, species guides, scam awareness page, about page.

| Section | Component | Variant |
|---|---|---|
| Navigation | `Navbar` | `classic` |
| Hero | `cag-split-hero` | `editorial` |
| Credibility Strip | `cag-stats-bar` | `dark` |
| Why Choose Us | `cag-split-feature` | `editorial` |
| Bird Listings | `SnapCarousel` + `cag-bird-card` | `classic` |
| Trust Credentials | `cag-trust-stats` | `classic` |
| Social Proof | `cag-testimonials` | `feature` |
| FAQ | `cag-faq-accordion` | `editorial` |
| Email Capture | `cag-newsletter` | `banner` |
| Footer | `cag-footer` | `dark` |
| Mobile Nav | `MobileNav` | (default) |

**CSS signature:** Cream page surface (`#faf7f4`), Lora serif headings, editorial spacing (64px vertical sections), forest-green dividers and tags, no light-colored panels except the hero gradient. Dark stats bar, dark footer.

---

## Theme 2: "Modern Precision"

**Character:** Clean, high-contrast, comparison-ready. For buyers who want data fast.
**Use for:** Comparison pages (Congo vs Timneh, vs Macaw, vs Cockatoo, male vs female), pricing page.

| Section | Component | Variant |
|---|---|---|
| Navigation | `Navbar` | `transparent` |
| Hero | `cag-split-hero` | `dark` |
| Stats | `cag-stats-bar` | `classic` |
| Data Comparison | `cag-pricing-table` | `matrix` |
| Features Grid | `cag-care-grid` | `classic` |
| Scam Check | `cag-scam-awareness` | `compare` |
| Social Proof | `cag-testimonials` | `mosaic` |
| Long-Form Nav | `cag-toc-v2` | (default) |
| FAQ | `cag-faq-accordion` | `classic` |
| Footer | `cag-footer` | `slim` |
| Mobile Nav | `Navbar` (hamburger) | (no MobileNav) |

**CSS signature:** Dark hero panel (`#1c1a18`), white card surfaces for comparison grids, mosaic testimonial layout, slim footer (no newsletter — too much friction at comparison stage). Transparent nav overlays the dark hero.

---

## Theme 3: "Buyer Journey"

**Character:** Conversion-focused, social proof heavy, inquiry-forward. Minimizes decision friction.
**Use for:** State location pages, bird variant pages (Congo/Timneh for sale), shipping page, adoption page, any page with a price and a location.

| Section | Component | Variant |
|---|---|---|
| Navigation | `Navbar` | `classic` |
| Hero | `cag-split-hero` | `classic` |
| Trust Bar | `cag-trust-stats` | `classic` |
| Bird Listings | `SnapCarousel` + `cag-bird-card` | `feature` |
| Social Proof | `cag-testimonials` | `grid` |
| Breeding Pair | `cag-parent-birds` | `classic` |
| Pricing | `cag-pricing-table` | `classic` |
| Inquiry Form | `cag-contact-form` | `application` |
| FAQ | `cag-faq-accordion` | `classic` |
| Email Capture | `cag-newsletter` | `split` |
| Footer | `cag-footer` | `dark` |
| Mobile Nav | `MobileNav` | (default) |
| Mobile CTA | `StickyCtaBar` | (default) |

**CSS signature:** Warm cream background throughout, prominent bird photography in feature card variant, application-style multi-step inquiry form, sticky bottom CTA on mobile paired with the tab bar for double-entry points.

---

## How Agents Should Use This File

When building a page, the agent should:
1. Identify the page's primary goal (editorial/trust → Heritage Trust; data-heavy comparison → Modern Precision; transactional with price → Buyer Journey)
2. Apply the full theme as the default component + variant selection
3. Reference `docs/reference/component-page-matrix.md` for section order
4. Note the theme in output: `[THEME: Heritage Trust]`, `[THEME: Modern Precision]`, or `[THEME: Buyer Journey]`

**Default when page type is ambiguous:**
- Has a price → Buyer Journey
- Has a comparison table → Modern Precision
- All others → Heritage Trust

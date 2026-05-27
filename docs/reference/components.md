# CAG Component Registry
**Version 2 — 2026-05-19**

All components live in `src/components/cag-library/`.
Design system tokens: `src/styles/cag-design-system.css` (non-Tailwind) or `src/styles/global.css` (Astro/Tailwind).

---

## Agent Rules for Component Selection

1. **Identify** sections needed for the page (hero, trust, FAQ, CTA, etc.)
2. **Select 1–3 candidate components** per section from the registry below
3. **Show the user** the candidates + variant options before writing any code
4. **Wait for user approval** before implementing any component on any page
5. Agents do NOT auto-apply components — user always chooses

**Default variants by page type:**

| Page Type | Default Variant |
|---|---|
| Homepage | `editorial` or `dark` — for visual impact |
| Location pages (50 states) | `classic` — for consistency |
| Informational / long-form | `classic` + `cag-toc-v1` or `cag-toc-v2` in sidebar |
| Scam / trust pages | `cag-scam-awareness:checklist` + `cag-key-takeaway` |
| Contact / inquiry pages | `cag-contact-form:application` |

---

## Mobile Behavior Reference

All components are mobile-responsive as of 2026-05-27. The table below shows the mobile pattern and the CSS class hooks added to each component's key elements.

| Component | Mobile Pattern (≤1024px) | Key CSS Class Hooks |
|---|---|---|
| `Navbar` | Hamburger button + slide-in drawer (right) | `nav-links`, `nav-hamburger`, `nav-drawer`, `nav-drawer-link`, `nav-overlay` |
| `MobileNav` *(new)* | Fixed bottom tab bar — 4 tabs | — (standalone component) |
| `StickyCtaBar` *(new)* | Fixed bottom CTA bar | `sticky-bar`, `sticky-btn`, `sticky-sub` |
| `SnapCarousel` *(new)* | CSS snap-scroll single-card carousel | `snap-track`, `snap-dots`, `dot` |
| `cag-split-hero` | Full-width image top → content below | `hero-grid`, `hero-image-col`, `hero-content-col`, `hero-ctas`, `trust-strip` |
| `cag-bird-card` | Full-width card; horizontal variant stacks | `card-classic`, `card-content`, `card-cta`, `horizontal-article`, `horizontal-image` |
| `cag-testimonials` | Horizontal snap-scroll carousel | `testimonials-grid` |
| `cag-contact-form` | Stacked layout; 16px inputs (iOS zoom) | `form-layout`, `form-input`, `form-submit` |
| `cag-pricing-table` | Horizontal scroll carousel (tiers variant) | `pricing-track` |
| `cag-care-grid` | 2-col tablet / 1-col mobile | `care-grid` |
| `cag-faq-accordion` | 44px min touch targets on questions | `faq-item`, `faq-question` |
| `cag-scam-awareness` | 1-col stacked | `scam-grid`, `scam-compare` |
| `cag-meet-the-team` | Row layout (80px photo left + bio text) | `team-grid`, `team-card`, `team-photo` |
| `cag-parent-birds` | 1-col stacked | `parents-grid` |
| `cag-split-feature` | Image above text (order: -1) | `split-grid`, `split-image` |
| `cag-video-section` | Full-width player, stacked layout | `video-stack`, `video-player` |
| `cag-newsletter` | Stacked column, full-width button | `newsletter-inner`, `newsletter-input-row`, `newsletter-btn` |
| `cag-footer` | Accordion (tap heading to expand section) + JS | `footer-cols`, `footer-col`, `footer-col-title`, `footer-col-links` |
| `cag-stats-bar` | 2-col grid (from 4-col) | `stats-grid` |
| `cag-trust-stats` | 2-col grid (from 4-col) | `trust-grid` |

---

## How to Use

### Astro components
```astro
---
import SplitHero    from '@/components/cag-library/SplitHero.astro';
import StatsBar     from '@/components/cag-library/StatsBar.astro';
import BirdCard     from '@/components/cag-library/BirdCard.astro';
---
<SplitHero variant="editorial" imageSrc="/birds/amie-hero.webp" />
<StatsBar  variant="dark" />
<BirdCard  variant="classic" name="Amie" sex="Female" age="11 months"
           price={2700} badge="NEW ARRIVAL" badgeColor="clay"
           quote="She mimics your laugh before you finish it." />
```

### Static HTML snippets (for `.html` pages)
Copy the relevant file from `src/components/cag-library/html/<name>.html` and paste the section HTML.
Requires `src/styles/cag-design-system.css` to be loaded on the page.

---

## Hero Components

| Canonical Name | File | Description | Best For |
|---|---|---|---|
| `cag-hero-v1` | `html/hero-v1.html` | Desktop split-layout hero: 12-col grid, Lora headline, clay CTA pill, warm-gradient bg, trust ribbon, forest-green nav | Homepage, high-intent landing pages |
| `cag-hero-v2` | `html/hero-v2.html` | Alternative desktop hero: different column balance, badge treatment varies | A/B testing against v1 |
| `cag-hero-mobile` | `html/hero-mobile.html` | Mobile-first hero: compact stack, large clay CTA button, Sora subtext, Lora headline | Mobile override, standalone mobile page |
| `cag-split-hero` | `SplitHero.astro` | Astro hero with 3 variants: `classic` / `editorial` / `dark` | Any page where Astro rendering is preferred |

---

## Stats & Trust Components

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-stats-bar` | `StatsBar.astro` | `classic` · `editorial` · `dark` | 4-up credibility metric strip — "10+ Years Breeding", "200+ Families", etc. |
| `cag-trust-stats` | `TrustStats.astro` | `classic` · `editorial` · `dark` | 4 icon cards: "Trust Speaks" — USDA AWA, CITES Documented, DNA-Sexed, Health Guarantee |

---

## Bird Listing Components

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-bird-card` | `BirdCard.astro` | `classic` · `horizontal` · `feature` | Single available-bird listing card with name, sex, age, price, badge, personality quote |
| `cag-parent-birds` | `ParentBirds.astro` | `classic` · `editorial` · `dark` | Breeding pair showcase with individual portraits, age, lineage notes |
| `cag-pricing-table` | `PricingTable.astro` | `classic` · `tiers` · `matrix` | Subspecies & pricing comparison — Congo vs Timneh, weaned vs unweaned age tiers |

Props for `cag-bird-card`:
```astro
<BirdCard
  variant="classic"
  name="Joys"
  sex="Female"
  age="2 yr"
  price={2200}
  imageSrc="/birds/joys-thumb.webp"
  badge="AVAILABLE"
  badgeColor="clay"
  quote="She says good morning before you do."
/>
```

---

## Content & Informational Components

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-care-grid` | `CareGrid.astro` | `classic` · `editorial` · `dark` | Numbered best-practices card grid — care tips, diet, enrichment, lifespan |
| `cag-split-feature` | `SplitFeature.astro` | `classic` · `editorial` · `dark` | Image + text + checklist — feature/benefit section, good for "Why Us" |
| `cag-scam-awareness` | `ScamAwareness.astro` | `grid` · `compare` · `checklist` | Buyer-protection infographic — scam red flags, legitimate vs fraudulent seller, verified checklist |
| `cag-faq-accordion` | `FaqAccordion.astro` | `classic` · `editorial` · `dark` | FAQ section using native `<details>` — accessible by default, no JS required |
| `cag-video-section` | `VideoSection.astro` | `vertical` · `cinematic` · `playlist` | YouTube embed block with optional playlist and chapter markers |
| `cag-meet-team` | `MeetTheTeam.astro` | `duo` · `story` · `feature` | Founder bio section — Mark & Teri Benjamin, family aviary story |

---

## Navigation Components

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-navbar` | `Navbar.astro` | `classic` · `transparent` · `mega` | Sticky top navigation — forest-green bg, white links, clay "Inquire Now" CTA |

---

## Table of Contents Components

| Canonical Name | File | Description |
|---|---|---|
| `cag-toc-v1` | `html/toc-v1.html` | Sidebar TOC v1 — minimal flat list, anchor links, Sora font. Use on long-form guides. |
| `cag-toc-v2` | `html/toc-v2.html` | Sidebar TOC v2 — bordered card, active-state highlight, progress dot. More polished. |

Use on: Scam Guide, Care Guide, Species Guide, any article with ≥4 H2 sections.

---

## Callout Components

| Canonical Name | File | Description |
|---|---|---|
| `cag-key-takeaway` | `html/key-takeaway-v1.html` | Highlighted insight callout — clay left border accent, green eyebrow tag ("KEY TAKEAWAY"), cream background. Use after each major section in long-form articles. |
| `cag-toc-keytakeaway` | `html/toc-keytakeaway-combined.html` | Combined sidebar: TOC stacked above Key Takeaway. Best for long-form pages that need both navigation and article insights in one sidebar column. |

---

## Conversion Components

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-contact-form` | `ContactForm.astro` | `classic` · `application` · `sidebar` | Buyer inquiry form — posts to Formspree. `application` variant adds bird-preference fields. `sidebar` variant is narrow for two-column layouts. |
| `cag-newsletter` | `Newsletter.astro` | `banner` · `split` · `footer` | Clutch-alert email subscribe — `banner` is full-width, `split` is two-column, `footer` is compact for footer placement. |
| `cag-testimonials` | `Testimonials.astro` | `grid` · `mosaic` · `feature` | Review / testimonial block — reads from case-studies.json or inline props. `feature` variant spotlights one testimonial large. |

---

## Footer Component

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-footer` | `Footer.astro` | `dark` · `cream` · `slim` | Site footer — `dark` (default, #1c1a18 bg) has sitemap columns, newsletter, CITES notice, USDA AWA. `cream` is lighter variant. `slim` is single-row for auxiliary pages. |

---

## Quick Reference Table

| Use Case | Component | Recommended Variant |
|---|---|---|
| Page hero | `cag-hero-v1` or `cag-split-hero` | v1 desktop / `editorial` |
| Credibility strip | `cag-stats-bar` | `classic` or `dark` |
| Trust credentials | `cag-trust-stats` | `classic` |
| Bird listing card | `cag-bird-card` | `classic` |
| Breeding pair | `cag-parent-birds` | `classic` |
| Pricing | `cag-pricing-table` | `classic` or `matrix` |
| Care tips | `cag-care-grid` | `classic` |
| Feature / why us | `cag-split-feature` | `editorial` |
| Scam content | `cag-scam-awareness` | `checklist` |
| FAQ | `cag-faq-accordion` | `classic` |
| Video | `cag-video-section` | `vertical` |
| About / founders | `cag-meet-team` | `story` |
| Long-form sidebar | `cag-toc-v2` | — |
| Article callout | `cag-key-takeaway` | — |
| Long-form sidebar + callout | `cag-toc-keytakeaway` | — |
| Inquiry form | `cag-contact-form` | `classic` or `application` |
| Newsletter | `cag-newsletter` | `banner` or `split` |
| Reviews | `cag-testimonials` | `grid` or `feature` |
| Navigation | `cag-navbar` | `classic` |
| Footer | `cag-footer` | `dark` |

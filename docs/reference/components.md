# CAG Component Registry
**Version 2.1 — 2026-05-29** *(Added cag-newsletter-v2; updated Quick Reference Table to reflect modern vs legacy status.)*

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
| Homepage | `cag-hero-v3:b` + `cag-toc-v3:02` + `cag-key-takeaway-v2:02` |
| Location pages (50 states) | `classic` — for consistency |
| Informational / long-form | `classic` + `cag-toc-v3:02` in sidebar |
| Scam / trust pages | `cag-scam-awareness:checklist` + `cag-key-takeaway-v2:03` |
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
| `cag-newsletter-v2` *(new)* | Stacked column; dark split collapses to single | `newsletter-v2`, `nv2-inner`, `nv2-btn` |
| `cag-footer` | Accordion (tap heading to expand section) + JS | `footer-cols`, `footer-col`, `footer-col-title`, `footer-col-links` |
| `cag-stats-bar` | 2-col grid (from 4-col) | `stats-grid` |
| `cag-trust-stats` | 2-col grid (from 4-col) | `trust-grid` |
| `cag-hero-v3` *(new)* | Image top → headline/CTA stack; credential bar wraps | `hero-v3`, `hero-credential-bar`, `hero-ctas` |
| `cag-toc-v3` *(new)* | Collapsible accordion / stacked parts | `toc-v3`, `toc-part`, `toc-link` |
| `cag-key-takeaway-v2` *(new)* | Stat tiles → 2-col then 1-col | `kt-v2`, `kt-stat`, `kt-grid` |
| `cag-counter-snippet` *(new)* | 4 stats → 2×2 grid on mobile | `counter-snippet`, `counter-stat` |
| `cag-available-grid` *(new)* | Filter pills scroll horizontally; cards full-width snap | `available-grid`, `filter-pills`, `bird-card`, `card-cta` |
| `cag-compare-table-e` *(new)* | Horizontal scroll / stacked column cards | `compare-e`, `compare-col`, `compare-row` |
| `cag-owner-card` *(new)* | Photo top → name/credentials/bio stack | `owner-card`, `owner-photo`, `owner-chips` |

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

### `cag-hero-v3` — MODERN ✅ USE THIS (homepage)
Source: `UNIQUE CAGs NEW COMPONENTS.zip` → `standalone/Hero {A,B,C}.html`. Full-bleed, responsive.
Astro file: `src/components/cag-library/HeroV3.astro`

| Variant | Label | Use when |
|---|---|---|
| `cag-hero-v3:a` | Scattered Flock | Photo-led, image-heavy visual hero |
| `cag-hero-v3:b` | **Authority Green** | **Trust-first breeder authority + credential bar. Homepage pick.** |
| `cag-hero-v3:c` | Mosaic Metrics | Data-forward hero with embedded metric tiles |

#### `cag-hero-v3:b` — Confirmed Specs (live 2026-05-31)

**Section height:** ~483px desktop at 1280px viewport. Driven by content column (text), not image.

**Grid padding (confirmed):**
- Mobile: `py-8` (32px each side)
- Desktop: `md:py-12 lg:py-12` (48px each side)

**Image circle (confirmed):**
- Mobile: `h-[220px] w-[220px]`
- sm (≥640px): `sm:h-[260px] sm:w-[260px]`
- Desktop (≥768px): `md:h-[300px] md:w-[300px]`

**H1 typography (confirmed — 2 lines on desktop):**
```
class="font-lora mt-4 text-3xl font-bold leading-[1.08] sm:text-4xl md:text-[2.25rem] lg:text-[2.5rem] md:leading-[1.1]"
```
- Do NOT use `md:text-[3.25rem]` — wraps to 3 lines at desktop column width (~560px)
- `2.25rem` at md = 2 lines: "African Grey Parrot Breeder / You Can Trust"

**Eyebrow span (confirmed):**
```
class="font-sora text-[10px] font-medium tracking-[0.12em] text-white/60 md:text-[11px]"
```
- No `uppercase` class — HTML already uses title case ("C.A.Gs · Midland, Texas · Family Aviary Since 2014")
- Never add `uppercase` to this element

**Trust pills `<ul>` (confirmed):**
```
class="mt-5 flex flex-wrap justify-center gap-x-5 gap-y-2.5 md:flex-nowrap md:justify-start"
```
- Mobile: `flex-wrap` → 2×2 grid (2 left, 2 right)
- Desktop: `md:flex-nowrap` → single row
- Each `<li>` must have `whitespace-nowrap` to prevent "CITES Appendix I" wrapping within the pill

**Pill items (confirmed):**
```
class="font-sora flex items-center gap-2 text-[13px] text-white/85 whitespace-nowrap"
```

**Pills content (4 items, in this order):**
1. USDA Licensed
2. CITES Appendix I
3. DNA Sexed
4. 10+ Year Support

### Legacy (do not use on new builds)
| Canonical Name | File | Status |
|---|---|---|
| `cag-hero-v1` | `html/hero-v1.html` | ⚠️ LEGACY |
| `cag-hero-v2` | `html/hero-v2.html` | ⚠️ LEGACY |
| `cag-hero-mobile` | `html/hero-mobile.html` | ⚠️ LEGACY |
| `cag-split-hero` | `SplitHero.astro` | ⚠️ LEGACY — `classic`/`editorial`/`dark`; superseded by `cag-hero-v3` |

---

## Counter Snippet Component

| Canonical Name | File | Variant | Description |
|---|---|---|---|
| `cag-counter-snippet` | `CounterSnippet.astro` | `4-stat` | ✅ MODERN 4-stat trust strip: **"12+ Years aviary · 100% CITES · $1,500 Floor price · 24h"**. Replaces the old 4-tile counter design. Featured-snippet/AIO bait; pairs with `cag-key-takeaway-v2:02`. |

---

## Stats & Trust Components

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-stats-bar` | `StatsBar.astro` | `classic` · `editorial` · `dark` | 4-up credibility metric strip — "10+ Years Breeding", "200+ Families", etc. |
| `cag-trust-stats` | `TrustStats.astro` | `classic` · `editorial` · `dark` | 4 icon cards: "Trust Speaks" — USDA AWA, CITES Documented, DNA-Sexed, Health Guarantee |

---

## Bird Listing Components

### `cag-available-grid` — MODERN ✅ USE THIS (filterable product grid + filter pills)
Source: `UNIQUE CAGs NEW COMPONENTS.zip` → `standalone/Available {A,B,C}.html`. Filterable by variant (Congo/Timneh) · type · availability · price.
Astro file: Uses inline JSX + `BirdCard.astro` — no standalone `.astro` file; import `BirdCard` from `src/components/BirdCard.astro`.

| Variant | Label | Use when |
|---|---|---|
| `cag-available-grid:a` | Pill Tabs | Filter pills above a card grid (All / Congo / Timneh / Pairs / Breeding / Eggs). Homepage default candidate. |
| `cag-available-grid:b` | Sidebar | Left filter sidebar + grid. Catalog-style. |
| `cag-available-grid:c` | Tile Gateway | Category tiles → drill into listings. |

Uses the **new filterable BirdCard** (badge, sex/age, price, clay "Inquire About [name]" CTA).

### Legacy / supporting
| Canonical Name | File | Variants | Status |
|---|---|---|---|
| `cag-bird-card` | `BirdCard.astro` | `classic` · `horizontal` · `feature` | ⚠️ Old standalone card — use the `cag-available-grid` card on new builds |
| `cag-parent-birds` | `ParentBirds.astro` | `classic` · `editorial` · `dark` | ✓ Breeding-pair showcase (still current) |
| `cag-pricing-table` | `PricingTable.astro` | `classic` · `tiers` · `matrix` | ✓ Pricing table (still current) |

---

## Comparison Components

| Canonical Name | File | Width | Description |
|---|---|---|---|
| `cag-compare-table-e` | `CompareTableE.astro` | **1100px** full-section | ✅ MODERN three-zone branded comparison: green Congo column + clay Timneh column, branded headers, dual CTAs ("Inquire About a Congo" / "Inquire About a Timneh"). Use for Congo-vs-Timneh + species comparison. Replaces inline tables and `cag-pricing-table:matrix` for comparison sections. |

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
| `cag-owner-card` ✅ MODERN | `OwnerCard.astro` | `mark-teri` | **NEW Mark & Teri Benjamin owner card** — USDA + CITES credential chips, Midland TX, est. 2014. Use on homepage/about. Replaces `cag-meet-team`. |
| `cag-meet-team` ⚠️ LEGACY | `MeetTheTeam.astro` | `duo` · `story` · `feature` | Old founder bio section — superseded by `cag-owner-card` |

---

## Navigation Components

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-navbar` | `Navbar.astro` | `classic` · `transparent` · `mega` | Sticky top navigation — forest-green bg, white links, clay "Inquire Now" CTA |

---

## Jump Link / Section Navigation Components

Three designs for section-to-section navigation. All use CAG design tokens (clay active, green done). Choose one per page — don't mix designs on the same page.

### `cag-jump-rail` — Option C ✅ RECOMMENDED for long pages (homepage, pillar pages)
File: `src/components/cag-library/JumpRail.astro`
Floating fixed right-side dot rail. Scroll-spy via IntersectionObserver. Shows all sections at once with live progress (hollow → green done → clay active). Desktop 1024px+ only — auto-hides on mobile/tablet (TocV3 handles those). Requires section `id` anchors on all target sections.

**Props:** none (section list hardcoded per page — duplicate and edit `sections[]` array for each page)

**States:** hollow circle = not yet reached · green fill = scrolled past · clay fill + glow = current section

**Use on:** homepage, species guides, purchase guide, scam guide, any pillar with ≥8 sections

**Example:**
```astro
import JumpRail from '@/components/cag-library/JumpRail.astro';
<JumpRail />
```

---

### `cag-jump-links` — Option B · Section-bottom Prev/Dots/Next strip
File: `src/components/cag-library/JumpLinks.astro`
Placed at the bottom of each individual section. Shows ← Prev label / progress dots / Next label → strip. Pure HTML anchor links — zero JS. Good for linear guided reading flow on shorter pages (blog posts, care guides, comparison pages). Prev hidden on section 1. Labels hidden on mobile (dots only).

**Props:**
```
current:    number   // 1-based section index
total:      number   // total section count
prevLabel?: string   // omit on section 1
prevHref?:  string
nextLabel?: string   // omit on last section
nextHref?:  string
```

**Use on:** blog posts, care guides, comparison pages, any page with 4–12 sections

**Example:**
```astro
import JumpLinks from '@/components/cag-library/JumpLinks.astro';
// Inside section 3 of 10:
<JumpLinks current={3} total={10} prevLabel="Congo Grey" prevHref="#congo" nextLabel="Timneh Grey" nextHref="#timneh" />
```

---

### `cag-jump-nav` — Option A · Sticky scroll-spy pill bar
File: `src/components/cag-jump-nav.astro`
Horizontal scrolling pill bar, sticky below the navbar (`top: 72px`). Shows all section labels as clickable pills. Current section pill turns clay on scroll. Mobile: horizontal scroll with hidden scrollbar. Best for pages with ≤10 sections where all labels fit in one row without heavy scrolling. Requires passing a `links` array.

**Props:**
```
links?:      NavLink[]   // { label: string; href: string }[]
sticky?:     boolean     // default true
activeHref?: string      // currently active href (for SSR pre-highlight)
```

**Use on:** location pages, FAQ pages, any page where section labels are short enough to scan at a glance

**Example:**
```astro
import CagJumpNav from '@/components/cag-jump-nav.astro';
<CagJumpNav links={[
  { label: 'Available Birds', href: '#available-birds' },
  { label: 'Shipping',        href: '#shipping' },
  { label: 'FAQ',             href: '#faq' },
  { label: 'Contact',         href: '/contact-us/' },
]} />
```

---

### Design Comparison

| | Option A — Pill Bar | Option B — Prev/Next Strip | Option C — Rail ★ |
|---|---|---|---|
| File | `cag-jump-nav.astro` | `JumpLinks.astro` | `JumpRail.astro` |
| Placement | Sticky top (after hero) | Bottom of each section | Fixed right side |
| JS required | Scroll-spy (optional) | None | IntersectionObserver |
| Mobile | Horizontal scroll | Dots only | Hidden (TocV3 covers) |
| Best for | ≤10 short-label sections | Linear guided flow | Long pillars ≥8 sections |
| Live on | — | — | Homepage (`index.astro`) |

---

## Table of Contents Components

### `cag-toc-v3` — MODERN (responsive: desktop / mobile / tablet) ✅ USE THIS
Astro file: `src/components/cag-library/TocV3.astro`
Source bundles (May 29 2026): `page-components-desktop.html`, `page-components-mobile.html`, `page-components-tablet.html` (each carries all 3 variants; mobile/tablet are thumb-first ports of the same set).

| Variant | Label | Use when |
|---|---|---|
| `cag-toc-v3:01` | Classic two-column | Compact flat anchor list, minimal weight |
| `cag-toc-v3:02` | **Grouped by part** | **Default for long pillars (≥10 sections)** — labeled parts, sitelink-friendly. Homepage pick. |
| `cag-toc-v3:03` | Chapter cards | Visual numbered cards, taller footprint |

### Legacy (do not use on new builds)
| Canonical Name | File | Status |
|---|---|---|
| `cag-toc-v1` | `html/toc-v1.html` | ⚠️ LEGACY — superseded by `cag-toc-v3` |
| `cag-toc-v2` | `html/toc-v2.html` | ⚠️ LEGACY — superseded by `cag-toc-v3` |

Use on: homepage pillar, Scam Guide, Care Guide, Species Guide, any article with ≥4 H2 sections.

---

## Callout Components

### `cag-key-takeaway-v2` — MODERN (responsive: desktop / mobile / tablet) ✅ USE THIS
Astro file: `src/components/cag-library/KeyTakeawayV2.astro`
Source bundles (May 29 2026): `page-components-{desktop,mobile,tablet}.html` (all 3 variants in each).

| Variant | Label | Use when |
|---|---|---|
| `cag-key-takeaway-v2:01` | Classic green card | Single BLUF callout, editorial |
| `cag-key-takeaway-v2:02` | **Stat-forward grid** | **Answer-engine / featured-snippet summary box** — stat tiles (years · CITES · DNA · placed). Homepage pick; aligns with the new counter-snippet numbers. |
| `cag-key-takeaway-v2:03` | Do / Don't checklist | Scam-wary trust angle, two-column do/don't |

### Legacy (do not use on new builds)
| Canonical Name | File | Status |
|---|---|---|
| `cag-key-takeaway` | `html/key-takeaway-v1.html` | ⚠️ LEGACY — superseded by `cag-key-takeaway-v2` |
| `cag-toc-keytakeaway` | `html/toc-keytakeaway-combined.html` | ⚠️ LEGACY — superseded by v3/v2 set |

---

## Conversion Components

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-contact-form` | `ContactForm.astro` | `classic` · `application` · `sidebar` | Buyer inquiry form — posts to Formspree. `application` variant adds bird-preference fields. `sidebar` variant is narrow for two-column layouts. |
| `cag-newsletter` | `Newsletter.astro` | `banner` · `split` · `footer` | Clutch-alert email subscribe — `banner` is full-width, `split` is two-column, `footer` is compact for footer placement. ⚠️ LEGACY on new builds — use `cag-newsletter-v2`. |
| `cag-newsletter-v2` ✅ MODERN | `NewsletterV2.astro` | `top` · `middle` · `bottom` | **NEW newsletter block (3 variants)** — `top` light banner, `middle` dark split (mid-page), `bottom` slim footer strip. Homepage uses `middle` + `bottom`. Use on all new homepage/pillar builds. |
| `cag-testimonials` | `Testimonials.astro` | `grid` · `mosaic` · `feature` | Review / testimonial block — reads from case-studies.json or inline props. `feature` variant spotlights one testimonial large. |

---

## Footer Component

| Canonical Name | File | Variants | Description |
|---|---|---|---|
| `cag-footer` | `Footer.astro` | `dark` · `cream` · `slim` | Site footer — `dark` (default, #1c1a18 bg) has sitemap columns, newsletter, CITES notice, USDA AWA. `cream` is lighter variant. `slim` is single-row for auxiliary pages. |

---

## Quick Reference Table

> ✅ = MODERN (use on new builds) · ⚠️ = LEGACY (do not use on new builds)

| Use Case | Component | Recommended Variant | Status |
|---|---|---|---|
| Page hero | `cag-hero-v3` | `b` Authority Green | ✅ |
| Filterable bird grid | `cag-available-grid` | `a` pill tabs | ✅ |
| Comparison table | `cag-compare-table-e` | (1100px) | ✅ |
| Answer / featured snippet box | `cag-key-takeaway-v2` | `02` stat-forward grid | ✅ |
| Page nav / TOC | `cag-toc-v3` | `02` grouped by part | ✅ |
| Breeder / owner bio | `cag-owner-card` | `mark-teri` | ✅ |
| Counter trust strip | `cag-counter-snippet` | `4-stat` | ✅ |
| Newsletter | `cag-newsletter-v2` | `middle` or `bottom` | ✅ |
| Trust credentials | `cag-trust-stats` | `classic` | ✅ |
| Care tips | `cag-care-grid` | `classic` | ✅ |
| Feature / why us | `cag-split-feature` | `editorial` | ✅ |
| Scam content | `cag-scam-awareness` | `checklist` or `compare` | ✅ |
| FAQ | `cag-faq-accordion` | `classic` or `editorial` | ✅ |
| Video | `cag-video-section` | `vertical` | ✅ |
| Social proof | `cag-testimonials` | `grid` or `feature` | ✅ |
| Breeding pair | `cag-parent-birds` | `classic` | ✅ |
| Pricing | `cag-pricing-table` | `classic` or `matrix` | ✅ |
| Inquiry form | `cag-contact-form` | `classic` or `application` | ✅ |
| Navigation | `cag-navbar` | `classic` | ✅ |
| Jump nav — fixed rail (long pages) | `cag-jump-rail` | — | ✅ |
| Jump nav — prev/next strip (linear) | `cag-jump-links` | — | ✅ |
| Jump nav — sticky pill bar (short pages) | `cag-jump-nav` | — | ✅ |
| Footer | `cag-footer` | `dark` | ✅ |
| Page hero (legacy) | `cag-hero-v1` or `cag-split-hero` | v1 desktop / `editorial` | ⚠️ |
| About / founders (legacy) | `cag-meet-team` | `story` | ⚠️ |
| Long-form sidebar (legacy) | `cag-toc-v1` or `cag-toc-v2` | — | ⚠️ |
| Article callout (legacy) | `cag-key-takeaway` | — | ⚠️ |
| Newsletter (legacy) | `cag-newsletter` | `banner` or `split` | ⚠️ |

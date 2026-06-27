# Mobile-Responsive Component System & Image Spec Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Merge the new mobile design patterns into all 24 existing CAG components, add 3 missing mobile-native components, establish a component-to-page assignment matrix with 3 named theme configurations, and create a `data/image-specs.json` system that drives per-page infographic/image generation across all page types.

**Architecture:** Two independent parts — Part A retrofits the 17 Astro components with scoped `<style>` media queries at 480px/1024px breakpoints matching the new mobile mockups, plus adds 3 new mobile-native Astro components (MobileNav, SnapCarousel, StickyCtaBar). Part B creates `data/image-specs.json` as the single source of truth for per-page image strategy and updates the infographic/image agent files to consume it.

**Tech Stack:** Astro 4.x, Tailwind CSS 4 (via `src/styles/global.css` @theme), scoped `<style>` blocks in Astro components, design tokens from `src/styles/cag-design-system.css`, vanilla JS for interactive mobile patterns.

---

## Context

The site's 17 Astro components were built desktop-first. They collapse to single-column on mobile via Tailwind's `md:` prefix, but the new mobile design mockups (`CongoAfricanGreys Mobile Components.html`) show fundamentally different mobile UX patterns that don't exist yet:

- **Missing**: Hamburger + side drawer nav (currently desktop links just collapse)
- **Missing**: CSS snap-scroll bird card carousel (currently a plain grid collapses)
- **Missing**: Fixed bottom tab bar navigation
- **Missing**: Sticky bottom CTA bar on transactional pages
- **Missing**: Footer accordion (mobile footer needs collapsible sections)
- **Partial**: Hero stacking, testimonial swipe, pricing carousel, form input sizing

The image/infographic system has no per-page spec. Agents currently guess dimensions. `data/image-specs.json` will codify what goes where on every page type, eliminating guesswork.

---

## Scope: Two Independent Subsystems

**Part A — Component mobile/responsive updates** (can be executed without Part B)
**Part B — Image spec system** (can be executed without Part A)

Recommended order: A then B, since image specs reference component section names.

---

## Part A — Mobile-Responsive Component Merge

### Gap Analysis: Desktop vs Mobile Mockups

| Mobile Pattern (from mockup) | Current Status | Action |
|---|---|---|
| Hamburger + slide-in drawer nav | Missing | Add to `Navbar.astro` |
| Bottom tab bar nav | Missing | New `MobileNav.astro` |
| Floating pill nav + sticky CTA | Missing | New `StickyCtaBar.astro` |
| Hero full-width image stacked above text | Partial (collapses only) | Update `SplitHero.astro` |
| CSS snap-scroll bird card carousel | Missing | New `SnapCarousel.astro` |
| Bottom sheet / full-screen step form | Partial | Update `ContactForm.astro` |
| FAQ accordion with 44px touch targets | Partial | Update `FaqAccordion.astro` |
| Care grid 2-col → 1-col mobile | Partial | Update `CareGrid.astro` |
| Testimonial swipe carousel | Missing | Update `Testimonials.astro` |
| Pricing horizontal scroll carousel | Missing | Update `PricingTable.astro` |
| Team stacked bios with photo left | Partial | Update `MeetTheTeam.astro` |
| Footer accordion (one section open) | Missing | Update `Footer.astro` |
| Slide-up / inline newsletter | Partial | Update `Newsletter.astro` |
| StatsBar 2-col on mobile | Partial | Update `StatsBar.astro` |
| TrustStats 2-col on mobile | Partial | Update `TrustStats.astro` |
| ScamAwareness stacked 1-col | Partial | Update `ScamAwareness.astro` |
| ParentBirds stacked 1-col | Partial | Update `ParentBirds.astro` |
| SplitFeature image above text | Partial | Update `SplitFeature.astro` |
| VideoSection full-width player | Partial | Update `VideoSection.astro` |

**Breakpoints enforced across ALL components:**
```
≤480px   → Mobile small (phones)
481–768px → Mobile large / small tablet
769–1024px → Tablet
≥1025px   → Desktop
```

### File Map — Part A

**Modified files:**
- `src/components/cag-library/Navbar.astro`
- `src/components/cag-library/SplitHero.astro`
- `src/components/cag-library/BirdCard.astro`
- `src/components/cag-library/ContactForm.astro`
- `src/components/cag-library/FaqAccordion.astro`
- `src/components/cag-library/CareGrid.astro`
- `src/components/cag-library/Testimonials.astro`
- `src/components/cag-library/PricingTable.astro`
- `src/components/cag-library/StatsBar.astro`
- `src/components/cag-library/TrustStats.astro`
- `src/components/cag-library/ScamAwareness.astro`
- `src/components/cag-library/MeetTheTeam.astro`
- `src/components/cag-library/ParentBirds.astro`
- `src/components/cag-library/SplitFeature.astro`
- `src/components/cag-library/VideoSection.astro`
- `src/components/cag-library/Newsletter.astro`
- `src/components/cag-library/Footer.astro`

**New files:**
- `src/components/cag-library/MobileNav.astro`
- `src/components/cag-library/SnapCarousel.astro`
- `src/components/cag-library/StickyCtaBar.astro`

**Documentation (new + updated):**
- `docs/reference/components.md` — add mobile behavior column + new component entries
- `docs/reference/component-page-matrix.md` — NEW: component-to-page assignment
- `docs/reference/component-themes.md` — NEW: 3 named theme configurations

---

### Task A-1: Navbar — Hamburger + Drawer

**File:** `src/components/cag-library/Navbar.astro`

- [ ] Read `src/components/cag-library/Navbar.astro` in full to understand existing structure

- [ ] Add semantic class names to the existing nav markup in all 3 variants:
  - Desktop links container → add class `nav-links`
  - Add hamburger button markup after the logo (inside the nav wrapper):
  ```astro
  <button class="nav-hamburger" id="nav-toggle" aria-label="Open menu" aria-expanded="false">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
      <path d="M3 6h18M3 12h18M3 18h18"/>
    </svg>
  </button>
  ```
  - Add overlay div and drawer nav after the main `<nav>` element:
  ```astro
  <div class="nav-overlay" id="nav-overlay"></div>
  <nav class="nav-drawer" id="nav-drawer" aria-label="Mobile navigation">
    <a href="/" class="nav-drawer-link">Home</a>
    <a href="/african-grey-parrots-for-sale/" class="nav-drawer-link">Birds for Sale</a>
    <a href="/african-grey-parrot-care-guide/" class="nav-drawer-link">Care Guide</a>
    <a href="/how-to-avoid-african-grey-parrot-scams/" class="nav-drawer-link">Avoid Scams</a>
    <a href="/about/" class="nav-drawer-link">About Us</a>
    <a href="/contact-us/" class="nav-drawer-cta">Inquire Now →</a>
  </nav>
  ```

- [ ] Add `<style>` block with mobile CSS:
  ```css
  .nav-links { display: flex; }
  .nav-hamburger { display: none; }
  .nav-overlay { display: none; position: fixed; inset: 0; background: rgba(28,26,24,.4); z-index: 9998; }
  .nav-overlay.open { display: block; }
  .nav-drawer {
    position: fixed; top: 0; right: -100%;
    width: min(320px, 85vw); height: 100vh;
    background: var(--cream, #faf7f4);
    box-shadow: -4px 0 32px rgba(60,30,10,.15);
    z-index: 9999;
    transition: right 0.28s cubic-bezier(.4,0,.2,1);
    padding: 80px 32px 32px;
    display: flex; flex-direction: column; gap: 8px;
  }
  .nav-drawer.open { right: 0; }
  .nav-drawer-link {
    font-family: var(--font-sans); font-size: 1.125rem; font-weight: 600;
    color: var(--text, #1c1a18); padding: 14px 0;
    border-bottom: 1px solid var(--border, #ede5dc);
    text-decoration: none; display: block;
  }
  .nav-drawer-cta {
    background: var(--clay, #e8604c); color: white;
    border-radius: 50px; padding: 16px 24px;
    text-align: center; font-weight: 700; font-size: 1rem;
    margin-top: auto; text-decoration: none; display: block;
  }
  @media (max-width: 1024px) {
    .nav-links { display: none !important; }
    .nav-hamburger { display: flex; align-items: center; justify-content: center; width: 44px; height: 44px; background: none; border: none; cursor: pointer; color: inherit; }
  }
  @media (min-width: 1025px) {
    .nav-drawer, .nav-overlay { display: none !important; }
  }
  ```

- [ ] Add `<script>` block for toggle behavior:
  ```astro
  <script>
    const toggle = document.getElementById('nav-toggle');
    const drawer = document.getElementById('nav-drawer');
    const overlay = document.getElementById('nav-overlay');
    function openDrawer() {
      drawer.classList.add('open'); overlay.classList.add('open');
      toggle.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    }
    function closeDrawer() {
      drawer.classList.remove('open'); overlay.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
    toggle?.addEventListener('click', () => drawer.classList.contains('open') ? closeDrawer() : openDrawer());
    overlay?.addEventListener('click', closeDrawer);
  </script>
  ```

- [ ] Commit:
  ```bash
  git add src/components/cag-library/Navbar.astro
  git commit -m "feat(nav): add mobile hamburger + slide-in drawer to all Navbar variants"
  ```

---

### Task A-2: SplitHero — Mobile Stack Layout

**File:** `src/components/cag-library/SplitHero.astro`

The current hero uses `md:grid-cols-2` which just collapses to 1-col without controlling image aspect ratio, content padding, CTA width, or the trust strip 4-col → 2-col change.

- [ ] Read `src/components/cag-library/SplitHero.astro` fully

- [ ] Add semantic class names alongside existing Tailwind classes in all 3 variants:
  - The `grid md:grid-cols-2` div → add `hero-grid`
  - Image column div → add `hero-image-col`
  - Content column div → add `hero-content-col`
  - CTA flex div → add `hero-ctas`
  - The trust strip grid div → add `trust-strip`

- [ ] Add `<style>` block:
  ```css
  @media (max-width: 1024px) {
    .hero-grid { grid-template-columns: 1fr !important; }
    .hero-image-col { aspect-ratio: 16/9; min-height: 220px; order: 0; }
    .hero-content-col { padding: 28px 24px !important; }
    .hero-ctas { flex-direction: column !important; }
    .hero-ctas a { width: 100%; text-align: center; }
    .trust-strip { grid-template-columns: repeat(2, 1fr) !important; }
  }
  @media (max-width: 480px) {
    .hero-image-col { aspect-ratio: 4/3; }
    .hero-content-col { padding: 24px 16px !important; }
  }
  ```

- [ ] Commit:
  ```bash
  git add src/components/cag-library/SplitHero.astro
  git commit -m "feat(hero): mobile stack layout — image top, 2-col trust strip, full-width CTAs"
  ```

---

### Task A-3: BirdCard — Touch Targets

**File:** `src/components/cag-library/BirdCard.astro`

- [ ] Read `src/components/cag-library/BirdCard.astro` fully

- [ ] Add semantic class names:
  - `article` element in `classic` variant → add `card-classic`
  - Content div (`p-6`) → add `card-content`
  - The `Inquire →` link → add `card-cta`
  - In `horizontal` variant: the `flex` article → add `horizontal-article`
  - The image col in horizontal → add `horizontal-image`

- [ ] Add `<style>` block:
  ```css
  @media (max-width: 1024px) {
    .horizontal-article { flex-direction: column !important; }
    .horizontal-image { width: 100% !important; aspect-ratio: 16/9; }
    .card-cta { width: 100%; text-align: center; padding: 14px 20px; font-size: 15px; }
  }
  @media (max-width: 480px) {
    .card-content { padding: 16px !important; }
  }
  ```

- [ ] Commit:
  ```bash
  git add src/components/cag-library/BirdCard.astro
  git commit -m "feat(bird-card): mobile touch targets, full-width CTA, horizontal variant stacks"
  ```

---

### Task A-4: New Component — MobileNav.astro

**File:** `src/components/cag-library/MobileNav.astro` (create new)

Bottom tab bar navigation. Renders only on mobile (≤1024px). Use on homepage and location pages alongside the main Navbar.

- [ ] Create `src/components/cag-library/MobileNav.astro`:
  ```astro
  ---
  /**
   * MobileNav — fixed bottom tab bar. Desktop: hidden. Mobile: always visible.
   * Place at bottom of BaseLayout or individual pages that need app-like nav.
   *
   * @prop active — which tab is current: 'home' | 'birds' | 'guide' | 'contact'
   */
  export interface Props {
    active?: 'home' | 'birds' | 'guide' | 'contact';
  }
  const { active = 'home' } = Astro.props;
  const tabs = [
    { id: 'home',    label: 'Home',    href: '/',                                    icon: '⌂' },
    { id: 'birds',   label: 'Birds',   href: '/african-grey-parrots-for-sale/',       icon: '◎' },
    { id: 'guide',   label: 'Guide',   href: '/african-grey-parrot-care-guide/',      icon: '◈' },
    { id: 'contact', label: 'Inquire', href: '/contact-us/',                          icon: '✉' },
  ];
  ---
  <nav class="mobile-tab-bar" aria-label="Bottom navigation">
    {tabs.map(tab => (
      <a href={tab.href}
         class={`tab-item ${active === tab.id ? 'active' : ''}`}
         aria-current={active === tab.id ? 'page' : undefined}>
        <span class="tab-icon" aria-hidden="true">{tab.icon}</span>
        <span class="tab-label">{tab.label}</span>
      </a>
    ))}
  </nav>
  <style>
  .mobile-tab-bar { display: none; }
  @media (max-width: 1024px) {
    .mobile-tab-bar {
      display: flex;
      position: fixed; bottom: 0; left: 0; right: 0;
      height: 64px;
      background: var(--cream, #faf7f4);
      border-top: 1px solid var(--border, #ede5dc);
      box-shadow: 0 -4px 24px rgba(60,30,10,.08);
      z-index: 9000;
      padding-bottom: env(safe-area-inset-bottom, 0px);
    }
    .tab-item {
      flex: 1; display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      gap: 3px; text-decoration: none;
      color: var(--light, #9b9189);
      transition: color 0.15s;
      -webkit-tap-highlight-color: transparent;
    }
    .tab-item.active { color: var(--clay, #e8604c); }
    .tab-icon { font-size: 20px; line-height: 1; }
    .tab-label { font-family: var(--font-sans); font-size: 10px; font-weight: 600; letter-spacing: .04em; }
  }
  </style>
  ```

- [ ] Commit:
  ```bash
  git add src/components/cag-library/MobileNav.astro
  git commit -m "feat(mobile-nav): add MobileNav bottom tab bar component"
  ```

---

### Task A-5: New Component — SnapCarousel.astro

**File:** `src/components/cag-library/SnapCarousel.astro` (create new)

Wraps `BirdCard` components. Desktop = 3-col grid. Mobile = CSS snap-scroll single card with pagination dots.

- [ ] Create `src/components/cag-library/SnapCarousel.astro`:
  ```astro
  ---
  /**
   * SnapCarousel — bird card section wrapper.
   * Desktop: 3-column grid. Mobile: horizontal snap-scroll carousel with dots.
   * Usage: wrap 3x BirdCard components in the default slot.
   */
  export interface Props {
    title?: string;
    subtitle?: string;
  }
  const {
    title = 'Birds Available Right Now',
    subtitle,
  } = Astro.props;
  ---
  <section class="snap-section">
    <div class="snap-header">
      {title && <h2 class="snap-title">{title}</h2>}
      {subtitle && <p class="snap-sub">{subtitle}</p>}
    </div>
    <div class="snap-track" role="region" aria-label={title}>
      <slot />
    </div>
    <div class="snap-dots" aria-hidden="true">
      <span class="dot active"></span>
      <span class="dot"></span>
      <span class="dot"></span>
    </div>
  </section>
  <style>
  .snap-section { padding: 40px 0; }
  .snap-header { padding: 0 48px 24px; }
  .snap-title { font-family: var(--font-display, 'Lora', serif); font-weight: 700; font-size: clamp(1.5rem, 2vw + 1rem, 2rem); color: var(--text, #1c1a18); }
  .snap-sub { color: var(--mid, #5a5248); margin-top: 8px; font-size: 1rem; }
  .snap-track { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; padding: 0 48px; }
  .snap-dots { display: none; }
  @media (max-width: 1024px) {
    .snap-header { padding: 0 20px 20px; }
    .snap-track {
      display: flex;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      -webkit-overflow-scrolling: touch;
      gap: 16px;
      padding: 0 20px 16px;
      scroll-padding-left: 20px;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }
    .snap-track::-webkit-scrollbar { display: none; }
    .snap-track > :global(*) {
      flex: 0 0 80vw;
      max-width: 320px;
      scroll-snap-align: start;
    }
    .snap-dots {
      display: flex; justify-content: center; gap: 6px; margin-top: 16px;
    }
    .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--border, #ede5dc); transition: background .2s, width .2s; }
    .dot.active { background: var(--clay, #e8604c); width: 18px; border-radius: 3px; }
  }
  @media (max-width: 480px) {
    .snap-track > :global(*) { flex: 0 0 88vw; }
  }
  </style>
  ```

- [ ] Commit:
  ```bash
  git add src/components/cag-library/SnapCarousel.astro
  git commit -m "feat(carousel): add SnapCarousel — desktop grid, mobile snap-scroll with dots"
  ```

---

### Task A-6: New Component — StickyCtaBar.astro

**File:** `src/components/cag-library/StickyCtaBar.astro` (create new)

Fixed bottom CTA bar for mobile on transactional pages (location pages, variant pages). Desktop: hidden.

- [ ] Create `src/components/cag-library/StickyCtaBar.astro`:
  ```astro
  ---
  /**
   * StickyCtaBar — fixed bottom CTA on mobile. Desktop: invisible.
   * Place at end of page body, before closing </body>.
   * Pair with MobileNav — use StickyCtaBar on location/variant pages, MobileNav on guide pages.
   */
  export interface Props {
    label?: string;
    href?: string;
    subtext?: string;
  }
  const {
    label   = 'Inquire About a Bird',
    href    = '/contact-us/',
    subtext = 'Response within 24 hours',
  } = Astro.props;
  ---
  <div class="sticky-bar">
    <a href={href} class="sticky-btn">{label} →</a>
    {subtext && <p class="sticky-sub">{subtext}</p>}
  </div>
  <style>
  .sticky-bar { display: none; }
  @media (max-width: 1024px) {
    .sticky-bar {
      position: fixed; bottom: 0; left: 0; right: 0;
      background: white;
      border-top: 1px solid var(--border, #ede5dc);
      padding: 12px 20px;
      padding-bottom: calc(12px + env(safe-area-inset-bottom, 0px));
      z-index: 8999;
      display: flex; flex-direction: column; align-items: stretch; gap: 4px;
      box-shadow: 0 -4px 24px rgba(60,30,10,.10);
    }
    .sticky-btn {
      background: var(--clay, #e8604c); color: white;
      border-radius: 50px; padding: 16px 24px;
      text-align: center;
      font-family: var(--font-sans); font-weight: 700; font-size: 16px;
      text-decoration: none;
      box-shadow: 0 6px 20px rgba(232,96,76,.38);
    }
    .sticky-sub {
      font-family: var(--font-sans); font-size: 11px;
      color: var(--light, #9b9189); text-align: center;
    }
  }
  </style>
  ```

- [ ] Commit:
  ```bash
  git add src/components/cag-library/StickyCtaBar.astro
  git commit -m "feat(mobile-cta): add StickyCtaBar fixed bottom CTA for mobile transactional pages"
  ```

---

### Task A-7: Remaining 14 Components — Mobile CSS Batch

For each component below: read the file → add semantic class names alongside Tailwind classes → add `<style>` block → commit. Group into 3 commits.

**Commit Group 1 — Forms & FAQ** (`ContactForm`, `FaqAccordion`):

**ContactForm.astro** — add class `form-layout` to the flex/grid wrapper, `form-input` to all inputs/selects/textareas, `form-submit` to submit button:
```css
@media (max-width: 1024px) {
  .form-layout { flex-direction: column !important; grid-template-columns: 1fr !important; }
  .form-submit { width: 100%; padding: 18px; font-size: 16px; }
}
@media (max-width: 480px) {
  .form-input { font-size: 16px !important; } /* prevents iOS auto-zoom on focus */
}
```

**FaqAccordion.astro** — add class `faq-item` to each question row, `faq-question` to the clickable header:
```css
@media (max-width: 480px) {
  .faq-item { padding: 16px 0; }
  .faq-question { min-height: 44px; font-size: 15px; display: flex; align-items: center; }
}
```

```bash
git add src/components/cag-library/ContactForm.astro src/components/cag-library/FaqAccordion.astro
git commit -m "feat(forms): mobile form sizing + 44px FAQ touch targets"
```

---

**Commit Group 2 — Content Grids** (`CareGrid`, `ScamAwareness`, `MeetTheTeam`, `ParentBirds`, `SplitFeature`, `VideoSection`):

**CareGrid.astro** — add class `care-grid` to the grid wrapper:
```css
@media (max-width: 768px) { .care-grid { grid-template-columns: repeat(2, 1fr) !important; } }
@media (max-width: 480px) { .care-grid { grid-template-columns: 1fr !important; } }
```

**ScamAwareness.astro** — add class `scam-grid` to grid wrapper, `scam-compare` to compare layout:
```css
@media (max-width: 1024px) {
  .scam-grid { grid-template-columns: 1fr !important; }
  .scam-compare { flex-direction: column !important; }
}
```

**MeetTheTeam.astro** — add class `team-grid` to grid wrapper, `team-card` to each card, `team-photo` to photo element:
```css
@media (max-width: 1024px) {
  .team-grid { grid-template-columns: 1fr !important; }
  .team-card { display: flex !important; flex-direction: row; gap: 16px; align-items: flex-start; }
  .team-photo { width: 80px; height: 80px; flex-shrink: 0; border-radius: 50%; }
}
@media (max-width: 480px) {
  .team-card { flex-direction: column; }
  .team-photo { width: 64px; height: 64px; }
}
```

**ParentBirds.astro** — add class `parents-grid`:
```css
@media (max-width: 768px) { .parents-grid { grid-template-columns: 1fr !important; } }
```

**SplitFeature.astro** — add class `split-grid`, `split-image`:
```css
@media (max-width: 1024px) {
  .split-grid { grid-template-columns: 1fr !important; }
  .split-image { order: -1; aspect-ratio: 16/9; width: 100%; }
}
```

**VideoSection.astro** — add class `video-stack`, `video-player`:
```css
@media (max-width: 1024px) {
  .video-stack { flex-direction: column !important; }
  .video-player { border-radius: 12px; width: 100%; }
}
```

```bash
git add src/components/cag-library/CareGrid.astro src/components/cag-library/ScamAwareness.astro \
        src/components/cag-library/MeetTheTeam.astro src/components/cag-library/ParentBirds.astro \
        src/components/cag-library/SplitFeature.astro src/components/cag-library/VideoSection.astro
git commit -m "feat(content): mobile responsive grids — CareGrid, Scam, Team, Parents, Split, Video"
```

---

**Commit Group 3 — Layout Shells** (`StatsBar`, `TrustStats`, `Testimonials`, `PricingTable`, `Newsletter`, `Footer`):

**StatsBar.astro** — add class `stats-grid`:
```css
@media (max-width: 480px) { .stats-grid { grid-template-columns: repeat(2, 1fr) !important; } }
```

**TrustStats.astro** — add class `trust-grid`:
```css
@media (max-width: 480px) { .trust-grid { grid-template-columns: repeat(2, 1fr) !important; } }
```

**Testimonials.astro** — add class `testimonials-grid` to the card container:
```css
@media (max-width: 1024px) {
  .testimonials-grid {
    display: flex !important;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    gap: 16px; padding: 0 20px 16px;
    scrollbar-width: none;
  }
  .testimonials-grid::-webkit-scrollbar { display: none; }
  .testimonials-grid > * { flex: 0 0 85vw; max-width: 340px; scroll-snap-align: start; }
}
```

**PricingTable.astro** — add class `pricing-track` to card container:
```css
@media (max-width: 1024px) {
  .pricing-track {
    display: flex !important;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    gap: 16px; padding: 0 20px 16px;
    scrollbar-width: none;
  }
  .pricing-track::-webkit-scrollbar { display: none; }
  .pricing-track > * { flex: 0 0 80vw; max-width: 300px; scroll-snap-align: start; }
}
```

**Newsletter.astro** — add class `newsletter-inner`, `newsletter-input-row`, `newsletter-btn`:
```css
@media (max-width: 768px) {
  .newsletter-inner { flex-direction: column !important; align-items: stretch !important; }
  .newsletter-input-row { flex-direction: column !important; }
  .newsletter-btn { width: 100%; font-size: 16px; padding: 16px; }
}
```

**Footer.astro** — add class `footer-cols` to grid wrapper, `footer-col` to each column, `footer-col-title` to each heading, `footer-col-links` to each link list. Add JS accordion toggle:
```css
@media (max-width: 768px) {
  .footer-cols { grid-template-columns: 1fr !important; }
  .footer-col-title { cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none; }
  .footer-col-title::after { content: '+'; font-size: 1.25rem; color: var(--light, #9b9189); }
  .footer-col.open .footer-col-title::after { content: '−'; }
  .footer-col-links { max-height: 0; overflow: hidden; transition: max-height 0.25s ease; }
  .footer-col.open .footer-col-links { max-height: 400px; }
}
```
```astro
<script>
  document.querySelectorAll('.footer-col-title').forEach(title => {
    title.addEventListener('click', () => {
      const col = title.closest('.footer-col');
      col.classList.toggle('open');
    });
  });
</script>
```

```bash
git add src/components/cag-library/StatsBar.astro src/components/cag-library/TrustStats.astro \
        src/components/cag-library/Testimonials.astro src/components/cag-library/PricingTable.astro \
        src/components/cag-library/Newsletter.astro src/components/cag-library/Footer.astro
git commit -m "feat(layout): mobile snap-scroll testimonials/pricing, footer accordion, 2-col stats"
```

---

### Task A-8: Component-to-Page Assignment Matrix

**File:** `docs/reference/component-page-matrix.md` (create new)

- [ ] Create the file with the full matrix:

```markdown
# CAG Component-to-Page Assignment Matrix

For each page type, lists which component + variant to use for each section.
"✓" = use this component. Variant shown in parentheses.

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
| `cag-meet-the-team` (story) | | | | | | | | ✓ About |
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

## Page-Type Section Order

### Homepage
Navbar → SplitHero (editorial) → StatsBar (dark) → SnapCarousel + BirdCard (classic) → SplitFeature (editorial) → TrustStats (classic) → Testimonials (feature) → VideoSection → ParentBirds (classic) → PricingTable (classic) → FaqAccordion (editorial) → Newsletter (banner) → Footer (dark) → MobileNav

### Location Page (state)
Navbar → SplitHero (classic) → TrustStats (classic) → SnapCarousel + BirdCard (classic) → StatsBar (classic) → PricingTable (classic) → ContactForm (application) → Testimonials (grid) → FaqAccordion (classic) → Newsletter (split) → Footer (dark) → MobileNav + StickyCtaBar

### Comparison Page
Navbar → SplitHero (dark) → PricingTable (matrix) → ScamAwareness (compare) → TocV2 → Testimonials (mosaic) → FaqAccordion (classic) → Newsletter (split) → Footer (dark)

### Variant Page (Congo / Timneh)
Navbar → SplitHero (classic) → StatsBar (classic) → BirdCard (feature) → ParentBirds (classic) → PricingTable (classic) → SplitFeature (editorial) → TrustStats (classic) → Testimonials (grid) → ContactForm (application) → FaqAccordion (classic) → Newsletter (split) → Footer (dark) → MobileNav + StickyCtaBar

### Care / Guide Page
Navbar → SplitHero (editorial) → TocV1 sidebar → CareGrid (classic) → SplitFeature (editorial) → KeyTakeaway → VideoSection → ParentBirds (classic) → FaqAccordion (classic) → Newsletter (split) → Footer (dark)

### Blog Page
Navbar → SplitHero (editorial, compact) → TocV2 → CareGrid (classic) → KeyTakeaway → FaqAccordion (classic) → Newsletter (split) → Footer (dark)
```

- [ ] Commit:
  ```bash
  git add docs/reference/component-page-matrix.md
  git commit -m "docs: add component-to-page assignment matrix with section order per page type"
  ```

---

### Task A-9: 3 Named Theme Configurations

**File:** `docs/reference/component-themes.md` (create new)

Three named combinations of existing components — different visual character for different page purposes.

- [ ] Create `docs/reference/component-themes.md`:

```markdown
# CAG Component Theme Configurations

Three named theme packages. When building a page, pick the theme that matches the page's purpose, then replace individual components only where the user specifies a different variant.

---

## Theme 1: "Heritage Trust"
**Character:** Warm, editorial, content-first. Authority without aggression.
**Use for:** Homepage, care guides, about page, species guide, scam page.

| Section | Component | Variant |
|---|---|---|
| Nav | Navbar | classic |
| Hero | cag-split-hero | editorial |
| Stats | cag-stats-bar | dark |
| Why us | cag-split-feature | editorial |
| Birds | SnapCarousel + cag-bird-card | classic |
| Credentials | cag-trust-stats | classic |
| Testimonials | cag-testimonials | feature |
| FAQ | cag-faq-accordion | editorial |
| Newsletter | cag-newsletter | banner |
| Footer | cag-footer | dark |
| Mobile nav | MobileNav | — |

**CSS signature:** Cream page surface (#faf7f4), Lora serif headings, editorial spacing (64px sections), forest-green dividers, no dark panels except footer and stats bar.

---

## Theme 2: "Modern Precision"
**Character:** Clean, high-contrast, comparison-ready. For buyers who want data fast.
**Use for:** Comparison pages (Congo vs Timneh, vs Macaw, vs Cockatoo), pricing page, male vs female.

| Section | Component | Variant |
|---|---|---|
| Nav | Navbar | transparent |
| Hero | cag-split-hero | dark |
| Stats | cag-stats-bar | classic |
| Comparison | cag-pricing-table | matrix |
| Features | cag-care-grid | classic |
| Scam check | cag-scam-awareness | compare |
| Social proof | cag-testimonials | mosaic |
| TOC | cag-toc-v2 | — |
| FAQ | cag-faq-accordion | classic |
| Footer | cag-footer | slim |
| Mobile nav | Navbar hamburger | — |

**CSS signature:** Dark hero panel (#1c1a18), white card surfaces, matrix comparison table, minimal slim footer. No newsletter on these pages — too much friction at comparison stage.

---

## Theme 3: "Buyer Journey"
**Character:** Conversion-focused, social proof heavy, inquiry-forward. Minimizes friction.
**Use for:** State location pages, bird variant pages, shipping page, adoption page.

| Section | Component | Variant |
|---|---|---|
| Nav | Navbar | classic |
| Hero | cag-split-hero | classic |
| Trust bar | cag-trust-stats | classic |
| Birds | SnapCarousel + cag-bird-card | feature |
| Testimonials | cag-testimonials | grid |
| Parents | cag-parent-birds | classic |
| Pricing | cag-pricing-table | classic |
| Inquiry | cag-contact-form | application |
| FAQ | cag-faq-accordion | classic |
| Newsletter | cag-newsletter | split |
| Footer | cag-footer | dark |
| Mobile nav | MobileNav | bottom-tab |
| Mobile CTA | StickyCtaBar | — |

**CSS signature:** Warm cream background, prominent bird photography, application-style multi-step form, sticky bottom CTA on mobile, mosaic or grid testimonials near the top.

---

## How to Reference in Agents

When building a page, agents should note the theme in their output:
- `[THEME: Heritage Trust]` for guide-type pages
- `[THEME: Modern Precision]` for comparison-type pages
- `[THEME: Buyer Journey]` for transactional pages

Default when unspecified: **Buyer Journey** for any page with a price or location; **Heritage Trust** for all others.
```

- [ ] Commit:
  ```bash
  git add docs/reference/component-themes.md
  git commit -m "docs: add 3 named theme configs — Heritage Trust, Modern Precision, Buyer Journey"
  ```

---

### Task A-10: Update components.md — Mobile Behavior Column

**File:** `docs/reference/components.md`

- [ ] Read `docs/reference/components.md` in full

- [ ] Add new section at top after "Agent Rules":

```markdown
## Mobile Behavior Reference

| Component | Mobile Pattern (≤1024px) | New Class Hooks |
|---|---|---|
| `Navbar` | Hamburger + slide-in drawer | `nav-links`, `nav-hamburger`, `nav-drawer` |
| `MobileNav` | Fixed bottom tab bar (NEW) | — |
| `StickyCtaBar` | Fixed bottom CTA bar (NEW) | — |
| `SnapCarousel` | CSS snap-scroll single card (NEW) | — |
| `cag-split-hero` | Full-width image top, 2-col trust | `hero-grid`, `hero-image-col`, `hero-ctas`, `trust-strip` |
| `cag-bird-card` | Full-width, touch-sized CTA | `card-classic`, `card-content`, `card-cta` |
| `cag-testimonials` | Snap-scroll carousel | `testimonials-grid` |
| `cag-contact-form` | Stacked layout, 16px inputs | `form-layout`, `form-input`, `form-submit` |
| `cag-pricing-table` | Horizontal scroll carousel | `pricing-track` |
| `cag-care-grid` | 2-col tablet / 1-col mobile | `care-grid` |
| `cag-faq-accordion` | 44px touch targets | `faq-item`, `faq-question` |
| `cag-scam-awareness` | Stacked 1-col | `scam-grid`, `scam-compare` |
| `cag-meet-the-team` | Row layout (photo left + text) | `team-grid`, `team-card`, `team-photo` |
| `cag-parent-birds` | Stacked 1-col | `parents-grid` |
| `cag-split-feature` | Image above text | `split-grid`, `split-image` |
| `cag-video-section` | Full-width player, stacked | `video-stack`, `video-player` |
| `cag-newsletter` | Stacked column, full-width btn | `newsletter-inner`, `newsletter-btn` |
| `cag-footer` | Accordion (tap to expand) + JS | `footer-cols`, `footer-col`, `footer-col-title`, `footer-col-links` |
| `cag-stats-bar` | 2-col grid | `stats-grid` |
| `cag-trust-stats` | 2-col grid | `trust-grid` |
```

- [ ] Add new entries for 3 new components to the Hero, Bird Listing, and Navigation tables

- [ ] Commit:
  ```bash
  git add docs/reference/components.md
  git commit -m "docs(components): add mobile behavior column + 3 new component entries"
  ```

---

## Part B — Image & Infographic Specification System

### Task B-1: Create data/image-specs.json

**File:** `data/image-specs.json` (create new)

Single source of truth for all image and infographic decisions per page type. Consumed by `cag-infographic-builder`, `cag-image-pipeline`, and `cag-photo-ingest`.

- [ ] Create `data/image-specs.json`:

```json
{
  "_version": "1.0",
  "_updated": "2026-05-27",
  "_rules": {
    "original_photo_first": "Always use real breeder photos when available before AI generation",
    "ai_portrait_dims": "1200x2133px at 9:16 native, CSS display at 350px wide",
    "infographic_guide_dims": "760px max-width, 400px height (desktop fixed), auto (mobile)",
    "infographic_homepage_dims": "1100px max-width, 400px height (desktop fixed), auto (mobile)",
    "og_image_dims": "1200x630px — separate from article images, always 16:9",
    "cites_safety": "Never reference wild-caught, never show birds in cages with visible distress",
    "mobile_image_preference": "9:16 portrait images (350px CSS) scale better on mobile than 16:9 landscape"
  },
  "page_types": {
    "homepage": {
      "url_pattern": "/",
      "sections": [
        {
          "section": "hero",
          "image_type": "hero_photo",
          "source": "original_photo",
          "dims": "1200x640px",
          "placement": "SplitHero right column",
          "fallback": "Higgsfield soul_2 — African Grey on warm background, editorial style",
          "notes": "Priority: real breeder bird photo. Use AMIE or ROYS images from project root."
        },
        {
          "section": "birds_listing",
          "image_type": "bird_photo",
          "source": "original_photo_per_bird",
          "dims": "400x300px (4:3)",
          "placement": "BirdCard top photo area",
          "notes": "Real bird photos only. Placeholder: /emoji/cag-congo.png"
        },
        {
          "section": "why_cag_feature",
          "image_type": "ai_generated",
          "source": "higgsfield",
          "dims": "1200x2133px native / 350px CSS display",
          "placement": "SplitFeature right column",
          "style": "soul_2",
          "prompt_guide": "Happy family interacting with hand-raised African Grey parrot indoors, warm lighting, editorial photography style, captive-bred, no cage visible"
        },
        {
          "section": "stats_infographic",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Feature Grid",
          "dims": "1100x400px desktop / 100% auto mobile",
          "notes": "4-stat strip: 10+ years breeding, 200+ families, CITES documented, USDA licensed"
        }
      ]
    },
    "location_page": {
      "url_pattern": "/african-grey-parrot-for-sale-[state]/",
      "sections": [
        {
          "section": "hero",
          "image_type": "hero_photo",
          "source": "original_photo",
          "dims": "1200x640px",
          "placement": "SplitHero (classic) right column",
          "fallback": "Nano Banana — African Grey parrot portrait, warm studio background"
        },
        {
          "section": "birds_listing",
          "image_type": "bird_photo",
          "source": "original_photo_per_bird",
          "dims": "400x300px (4:3)",
          "placement": "BirdCard + SnapCarousel"
        },
        {
          "section": "shipping_timeline",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Process Flow",
          "dims": "1100x400px desktop / 100% auto mobile",
          "notes": "3-step: Reserve → IATA-certified crate → Airport pickup in [state]"
        },
        {
          "section": "trust_credentials",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Feature Grid",
          "dims": "1100x400px",
          "notes": "4 trust badges: USDA AWA / CITES Appendix II / DNA-Sexed / Health Guarantee"
        }
      ]
    },
    "comparison_page": {
      "url_patterns": [
        "/congo-vs-timneh-african-grey/",
        "/african-grey-vs-macaw/",
        "/african-grey-vs-cockatoo/",
        "/african-grey-vs-amazon-parrot/",
        "/male-vs-female-african-grey-parrots-for-sale/"
      ],
      "sections": [
        {
          "section": "hero_comparison",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Comparison",
          "dims": "1100x400px desktop / 100% auto mobile",
          "notes": "Side-by-side two-species illustration with key stat callouts. Never use 🦜 — use custom CAG images."
        },
        {
          "section": "comparison_table",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Comparison",
          "dims": "760x400px",
          "notes": "Feature comparison grid with checkmarks and values. Text-heavy, HTML/CSS always preferred over AI."
        },
        {
          "section": "lifestyle_photo",
          "image_type": "ai_generated",
          "source": "higgsfield_or_nano_banana",
          "dims": "1200x2133px / 350px CSS",
          "placement": "SplitFeature",
          "prompt_guide": "For Congo vs Timneh: both birds in same frame showing size difference. For vs-macaw: clear size comparison with person. Editorial style, warm indoor background."
        }
      ]
    },
    "variant_page": {
      "url_patterns": [
        "/congo-african-grey-for-sale/",
        "/timneh-african-grey-for-sale/"
      ],
      "sections": [
        {
          "section": "hero",
          "image_type": "hero_photo",
          "source": "original_photo",
          "dims": "1200x640px",
          "placement": "SplitHero (classic) right column",
          "notes": "Use named bird photos: AMIE/ROYS for Congo, ELAD/EVIE for Timneh"
        },
        {
          "section": "features_infographic",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Feature Grid",
          "dims": "760x400px",
          "notes": "Species characteristics: size, wing color, tail color, talking ability, personality score"
        },
        {
          "section": "parent_birds",
          "image_type": "original_photo",
          "source": "breeder_photo",
          "dims": "300x300px (1:1 portrait)",
          "placement": "ParentBirds component"
        },
        {
          "section": "cta_lifestyle",
          "image_type": "ai_generated",
          "source": "higgsfield",
          "dims": "1200x2133px / 350px CSS",
          "style": "soul_2",
          "prompt_guide": "Person bonding with [Congo/Timneh] African Grey parrot, warm home environment, trust and affection evident, captive-bred companion bird, no cage bars visible"
        }
      ]
    },
    "care_guide_page": {
      "url_patterns": [
        "/african-grey-parrot-care-guide/",
        "/african-grey-parrot-diet/",
        "/best-african-grey-parrot-food/",
        "/african-grey-parrot-lifespan/"
      ],
      "sections": [
        {
          "section": "hero",
          "image_type": "ai_generated",
          "source": "nano_banana",
          "dims": "1200x2133px / 350px CSS",
          "placement": "SplitHero (editorial) right column",
          "prompt_guide": "African Grey parrot in enrichment or care context — foraging, playing with toys, eating fresh produce, on perch. Natural warm lighting, captive-bred home environment."
        },
        {
          "section": "care_tips_grid",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Feature Grid",
          "dims": "760x400px desktop / 100% auto mobile",
          "notes": "6-tip grid with icons: Diet, Enrichment, Socialization, Vet Care, Cage Setup, Sleep"
        },
        {
          "section": "mid_article_lifestyle",
          "image_type": "ai_generated",
          "source": "nano_banana",
          "dims": "1200x2133px / 350px CSS",
          "placement": "SplitFeature mid-article",
          "cadence": "1 image per 800 words of article content",
          "prompt_guide": "Topic-specific: diet page = bird eating fresh food; lifespan page = bird with older owner; cage page = spacious enriched aviary interior"
        }
      ]
    },
    "blog_page": {
      "url_pattern": "/blog/[slug]/",
      "sections": [
        {
          "section": "featured_image",
          "image_type": "ai_generated",
          "source": "nano_banana_or_higgsfield",
          "dims_og": "1200x630px (separate OG image)",
          "dims_article": "760x400px (article hero view)",
          "placement": "Full-width hero above article content",
          "notes": "Generate 2 versions: 16:9 for OG/social, 16:9 for article. Same prompt, different crops."
        },
        {
          "section": "inline_section_image",
          "image_type": "ai_generated",
          "source": "nano_banana",
          "dims": "760x400px infographic OR 1200x2133px / 350px CSS portrait",
          "placement": "Every 600-800 words",
          "notes": "Alternate between: HTML infographic for data/stats sections, portrait image for lifestyle/story sections"
        },
        {
          "section": "stat_callout",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Feature Grid (1-row)",
          "dims": "760x160px",
          "notes": "Single-stat pull quote visual for key data points mid-article"
        }
      ]
    },
    "african_grey_adoption_page": {
      "url": "/african-grey-adoption/",
      "sections": [
        {
          "section": "hero",
          "image_type": "ai_generated",
          "source": "higgsfield",
          "dims": "1200x2133px / 350px CSS",
          "style": "soul_2",
          "prompt_guide": "Emotional scene: family welcoming African Grey parrot into home for the first time. Warm, joyful, trust. Captive-bred companion bird, indoors, no cage visible."
        },
        {
          "section": "adoption_process",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Process Flow",
          "dims": "760x400px",
          "notes": "4-step: Submit Application → Breeder Review → Bird Match → Bring Home"
        }
      ]
    },
    "eggs_page": {
      "url": "/african-grey-parrot-bird-eggs-for-sale-usa/",
      "sections": [
        {
          "section": "hero",
          "image_type": "original_photo",
          "source": "breeder_photo",
          "dims": "1200x640px",
          "notes": "Use 'Candled African Grey parrot bird eggs for sale.webp' or 'Healthy African Grey parrot eggs ready to hatch.webp' from project root"
        },
        {
          "section": "incubation_timeline",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Process Flow",
          "dims": "760x400px",
          "notes": "Egg development timeline: Candling Day 7 → Incubation 28 days → Hatch → Weaning 12-16 weeks"
        }
      ]
    },
    "shipping_page": {
      "url": "/buy-african-grey-parrots-with-shipping/",
      "sections": [
        {
          "section": "hero",
          "image_type": "ai_generated",
          "source": "nano_banana",
          "dims": "1200x2133px / 350px CSS",
          "prompt_guide": "IATA-approved airline-safe bird carrier being prepared. Clean, professional, reassuring. No distressed birds."
        },
        {
          "section": "shipping_route_map",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Process Flow",
          "dims": "1100x400px",
          "notes": "USA map with shipping routes OR 3-step timeline: Order confirmed → IATA crate prep → Airport pickup"
        }
      ]
    },
    "scam_page": {
      "url": "/how-to-avoid-african-grey-parrot-scams/",
      "sections": [
        {
          "section": "hero_comparison",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Comparison",
          "dims": "1100x400px",
          "notes": "Real breeder vs scammer side-by-side checklist. Use warning colors for scammer column."
        },
        {
          "section": "red_flags_grid",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Feature Grid",
          "dims": "760x400px",
          "notes": "6 red flags with warning icons: too-low price, no CITES docs, PayPal only, no live video, no vet records, pressure to wire transfer"
        }
      ]
    },
    "hub_page": {
      "url_patterns": [
        "/african-grey-parrots-for-sale/",
        "/african-grey-comparison/"
      ],
      "sections": [
        {
          "section": "hero",
          "image_type": "infographic",
          "source": "html_css",
          "infographic_type": "Feature Grid",
          "dims": "1100x400px",
          "notes": "Hub-page hero: 4-card overview grid of what this hub covers. No AI image — hub pages should feel like a directory/guide."
        },
        {
          "section": "variant_thumbnails",
          "image_type": "original_photo",
          "source": "breeder_photo",
          "dims": "400x300px per thumbnail",
          "notes": "Congo = AMIE/ROYS photos. Timneh = ELAD/EVIE photos."
        }
      ]
    }
  }
}
```

- [ ] Validate JSON is valid:
  ```bash
  python3 -c "import json; d=json.load(open('data/image-specs.json')); print(f'Valid — {len(d[\"page_types\"])} page types')"
  ```
  Expected output: `Valid — 10 page types`

- [ ] Commit:
  ```bash
  git add data/image-specs.json
  git commit -m "feat(data): add image-specs.json — per-page image and infographic design system"
  ```

---

### Task B-2: Update cag-infographic-builder Agent

**File:** `.claude/agents/cag-infographic-builder.md`

- [ ] Read `.claude/agents/cag-infographic-builder.md`

- [ ] Add the following section immediately after the existing "Mode selection" section:

```markdown
## Image Spec Lookup (REQUIRED BEFORE BUILDING)

Before building any infographic, read `data/image-specs.json`:
1. Identify the `page_type` for the current page (homepage / location_page / comparison_page / variant_page / care_guide_page / blog_page / etc.)
2. Find the `section` being built within that page type
3. Use the `dims`, `infographic_type`, and `notes` from the spec exactly
4. Never deviate from the specified dimensions unless the user explicitly overrides

### Dimension Quick Reference

| Page Context | max-width | Desktop height | Mobile |
|---|---|---|---|
| Homepage, location pages, hero sections | 1100px | 400px fixed | 100% auto |
| Guide, blog, care pages, comparison tables | 760px | 400px fixed | 100% auto |
| Single-stat callout (blog mid-article) | 760px | 160px | auto |
| OG / social image | 1200x630px | — | — |

### infographic_type → Component Type Mapping

| infographic_type in spec | Infographic HTML type to build |
|---|---|
| Comparison | Side-by-side 2-column with header row |
| Feature Grid | Card grid with icon + title + description |
| Process Flow | Numbered steps with connector arrows |
```

- [ ] Commit:
  ```bash
  git add .claude/agents/cag-infographic-builder.md
  git commit -m "feat(agent): add image-specs.json lookup requirement to cag-infographic-builder"
  ```

---

### Task B-3: Update Image Generation Skills

**File:** `skills/cag-image-generation.md`

- [ ] Read `skills/cag-image-generation.md`

- [ ] Add section "Per-Page Image Strategy" before the existing provider list:

```markdown
## Per-Page Image Strategy

Read `data/image-specs.json` FIRST. For every image request:
1. Identify page_type + section from context
2. Check `source` field: `original_photo` → do not generate, use breeder photo; `html_css` → build HTML infographic; `ai_generated` → proceed to generation
3. Use `prompt_guide` field as the base prompt (add technical quality suffixes: "photorealistic, warm natural lighting, editorial photography style")
4. Use `dims` field for dimensions

### Priority Hierarchy (always follow this order)
1. Original breeder photos (source: original_photo) — no generation needed
2. HTML/CSS infographics (source: html_css) — never AI-generate for data/stats sections
3. Higgsfield MCP (source: higgsfield) — for hero lifestyle images where character consistency matters
4. Nano Banana / Google Imagen 3 (source: nano_banana) — for mid-article and care guide images
5. DALL-E 3 — fallback if Higgsfield and Nano Banana are unavailable

### CITES Safety on All Prompts
Append to every AI prompt: "captive-bred companion bird, domestic home environment, no wild habitat, no endangered species imagery"

### OG Image Rule
Every page needs a separate 1200×630px OG image. Generate this in addition to the article/page image. Same prompt, different crop/composition. Save as `[slug]-og.webp`.
```

- [ ] Commit:
  ```bash
  git add skills/cag-image-generation.md
  git commit -m "feat(skill): add per-page image strategy + priority hierarchy to cag-image-generation"
  ```

---

### Task B-4: Update SEO Rules with Image Spec Reference

**File:** `docs/reference/seo-rules.md`

- [ ] Read `docs/reference/seo-rules.md` — find the infographic/image section

- [ ] Add or update the image dimension rule to reference `data/image-specs.json`:

```markdown
**Rule [IMAGE-01]:** Before generating any image or infographic, read `data/image-specs.json` for the current page_type and section. Use the specified `dims`, `source`, and `infographic_type` exactly. Overrides: user instruction > image-specs.json > agent defaults.

**Rule [IMAGE-02]:** Infographic dimensions — 760px wrapper for guide/blog/care pages; 1100px wrapper for homepage/location/hero. Height always 400px desktop, auto mobile. Never use 900px or max-w-4xl (legacy values).

**Rule [IMAGE-03]:** AI-generated portrait images always 1200×2133px native (9:16). CSS display width: 350px. This ratio scales better on mobile than 16:9 landscape.

**Rule [IMAGE-04]:** Every page needs a 1200×630px OG image (separate generation). Never reuse article images for OG without cropping to 16:9.
```

- [ ] Commit:
  ```bash
  git add docs/reference/seo-rules.md
  git commit -m "docs(seo-rules): add IMAGE-01 through IMAGE-04 rules referencing image-specs.json"
  ```

---

## Verification

### V-1: Mobile viewport visual check (after each component batch)

```bash
npm run dev
# Then use Playwright MCP at 375px width to verify:
# - Navbar: hamburger visible, drawer opens/closes
# - SplitHero: image stacks above text
# - BirdCard: full-width on mobile
# - SnapCarousel: horizontal scroll works, cards snap
# - MobileNav: bottom tab bar appears at ≤1024px
# - StickyCtaBar: visible at bottom on location pages
# - Footer: sections accordion on tap
```

### V-2: Desktop regression check

```bash
# At 1280px width — verify all desktop layouts unchanged:
# - Navbar: horizontal links visible, hamburger hidden
# - SplitHero: 2-column layout intact
# - BirdCard: 3-column grid in SnapCarousel
# - Footer: 5-column grid, no accordion
# - MobileNav + StickyCtaBar: completely hidden
```

### V-3: JSON spec validation

```bash
python3 -c "
import json
d = json.load(open('data/image-specs.json'))
for pt, spec in d['page_types'].items():
    for s in spec['sections']:
        assert 'section' in s, f'Missing section in {pt}'
        assert 'source' in s, f'Missing source in {pt}/{s}'
        assert 'dims' in s or 'dims_og' in s, f'Missing dims in {pt}/{s}'
print(f'All {len(d[\"page_types\"])} page types valid')
"
```

### V-4: Component registry completeness

```bash
ls src/components/cag-library/*.astro | wc -l
# Expected: 20 (17 original + 3 new: MobileNav, SnapCarousel, StickyCtaBar)
```

---

## Commit Summary

| Commit | Files | Description |
|---|---|---|
| 1 | Navbar.astro | Mobile hamburger + drawer |
| 2 | SplitHero.astro | Mobile stack layout |
| 3 | BirdCard.astro | Mobile touch targets |
| 4 | MobileNav.astro (new) | Bottom tab bar |
| 5 | SnapCarousel.astro (new) | Snap-scroll bird carousel |
| 6 | StickyCtaBar.astro (new) | Fixed bottom CTA |
| 7 | ContactForm.astro, FaqAccordion.astro | Forms + FAQ mobile |
| 8 | CareGrid, Scam, Team, Parents, Split, Video | Content grid mobile |
| 9 | StatsBar, TrustStats, Testimonials, Pricing, Newsletter, Footer | Layout shells mobile |
| 10 | component-page-matrix.md (new) | Page assignment matrix |
| 11 | component-themes.md (new) | 3 named themes |
| 12 | components.md | Mobile behavior column + new entries |
| 13 | data/image-specs.json (new) | Image spec system |
| 14 | cag-infographic-builder.md | Agent spec lookup |
| 15 | skills/cag-image-generation.md | Per-page strategy |
| 16 | docs/reference/seo-rules.md | IMAGE-01 through IMAGE-04 rules |

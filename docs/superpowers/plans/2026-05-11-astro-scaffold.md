# Astro Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap a production-ready Astro + Tailwind site for CongoAfricanGreys.com, migrate all 8 existing pages, and deploy to Cloudflare Pages — replacing the WordPress static export.

**Architecture:** Astro static site generator at the project root, with Tailwind for styling, brand design tokens in tailwind.config, reusable `.astro` components for header/footer/trustbar/CTA/schema, and Cloudflare Pages for hosting (build: `npm run build` → `dist/`).

**Tech Stack:** Astro 4.x, Tailwind CSS 3.x, Node 24, Cloudflare Pages, GitHub (existing remote)

---

## Brand Constants (reference throughout)

```
Colors:
  logo-dark:  #12100e
  gold:       #c4a05a
  cream:      #f5eeda
  rust:       #b43c2d
  warm-white: #faf7f4
  stone-800:  #292524 (body text)

Fonts:
  Heading: Lora (serif) — weights 400, 600, 700
  Body:    Sora (sans) — weights 400, 500, 600

Phone: (956) 564-6067
Email: Info@congoafricangreys.com
Address: 2508 Briaroaks Ct, Midland, TX 79707
Site: https://congoafricangreys.com
```

---

## File Map

**New files (create):**
```
astro.config.mjs
package.json
tailwind.config.mjs
tsconfig.json
.gitignore (update)
public/
  favicon.ico → copy from assets/brand/
  favicon-32.png → copy from assets/brand/
  favicon-16.png → copy from assets/brand/
  apple-touch-icon.png → copy from assets/brand/
  og-image.png → copy from assets/brand/
  og-twitter.png → copy from assets/brand/
  logo-256.png → copy from assets/brand/
  logo-128.png → copy from assets/brand/
src/
  layouts/
    BaseLayout.astro
  components/
    Header.astro
    Footer.astro
    TrustBar.astro
    CTA.astro
    Schema.astro
  pages/
    index.astro
    african-grey-parrot-for-sale/index.astro
    congo-african-grey-for-sale/index.astro
    african-grey-breeding-pair-for-sale/index.astro
    african-grey-parrot-for-sale-near-me/index.astro
    african-grey-parrot-for-sale-texas/index.astro
    african-grey-parrot-for-sale-new-york/index.astro
    african-grey-parrot-for-sale-ohio/index.astro
    contact-us/index.astro
```

**Existing files (reference only, do not modify):**
```
site/content/ — WordPress static export; used as content source during migration
assets/brand/ — logo + favicon source files
data/price-matrix.json — pricing source of truth
data/bird-inventory.json — named birds
```

---

## Task 1: Initialize Astro Project

**Files:**
- Create: `package.json`
- Create: `astro.config.mjs`
- Create: `tsconfig.json`

- [ ] **Step 1: Initialize Astro with minimal template**

```bash
cd /Users/apple/Downloads/CAG
npm create astro@latest . -- --template minimal --no-install --no-git
```

When prompted: accept defaults, do NOT init new git (repo already exists).

- [ ] **Step 2: Install dependencies**

```bash
npm install
```

Expected: `node_modules/` created, no errors.

- [ ] **Step 3: Verify Astro dev server starts**

```bash
npm run dev -- --port 4321 &
sleep 3
curl -s http://localhost:4321 | head -5
kill %1
```

Expected: HTML response with `<!DOCTYPE html>`.

- [ ] **Step 4: Commit baseline**

```bash
git add package.json package-lock.json astro.config.mjs tsconfig.json src/ .gitignore
git commit -m "chore: initialize Astro project with minimal template"
```

---

## Task 2: Tailwind CSS + Font Configuration

**Files:**
- Create: `tailwind.config.mjs`
- Modify: `astro.config.mjs`
- Modify: `src/layouts/BaseLayout.astro` (created in Task 3, referenced here for context)

- [ ] **Step 1: Install Tailwind integration**

```bash
npx astro add tailwind --yes
```

Expected: `tailwind.config.mjs` created, `astro.config.mjs` updated with `@astrojs/tailwind`.

- [ ] **Step 2: Replace tailwind.config.mjs with brand tokens**

```js
// tailwind.config.mjs
import { defineConfig } from 'tailwindcss';

export default defineConfig({
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'logo-dark': '#12100e',
        'gold':      '#c4a05a',
        'cream':     '#f5eeda',
        'rust':      '#b43c2d',
        'warm-white':'#faf7f4',
      },
      fontFamily: {
        lora: ['Lora', 'Georgia', 'serif'],
        sora: ['Sora', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
});
```

- [ ] **Step 3: Verify Tailwind classes resolve**

```bash
npm run build 2>&1 | tail -5
```

Expected: build succeeds, no Tailwind errors.

- [ ] **Step 4: Commit**

```bash
git add tailwind.config.mjs astro.config.mjs
git commit -m "chore: add Tailwind with brand design tokens"
```

---

## Task 3: Copy Brand Assets to public/

**Files:**
- Create: `public/favicon.ico`, `public/favicon-32.png`, `public/favicon-16.png`
- Create: `public/apple-touch-icon.png`, `public/og-image.png`, `public/og-twitter.png`
- Create: `public/logo-256.png`, `public/logo-128.png`, `public/logo-64.png`

- [ ] **Step 1: Copy all brand assets**

```bash
cp assets/brand/favicon.ico public/
cp assets/brand/favicon-32.png public/
cp assets/brand/favicon-16.png public/
cp assets/brand/apple-touch-icon.png public/
cp assets/brand/og-image.png public/
cp assets/brand/og-twitter.png public/
cp assets/brand/logo-256.png public/
cp assets/brand/logo-128.png public/
cp assets/brand/logo-64.png public/
```

- [ ] **Step 2: Verify files present**

```bash
ls public/
```

Expected: all 9 files listed.

- [ ] **Step 3: Commit**

```bash
git add public/
git commit -m "chore: copy brand assets to public/"
```

---

## Task 4: BaseLayout Component

**Files:**
- Create: `src/layouts/BaseLayout.astro`

- [ ] **Step 1: Create BaseLayout.astro**

```astro
---
// src/layouts/BaseLayout.astro
interface Props {
  title: string;
  description: string;
  canonical: string;
  ogType?: string;
  schemaJson?: string;
}
const { title, description, canonical, ogType = 'website', schemaJson } = Astro.props;
---
<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content={description} />
  <link rel="canonical" href={canonical} />

  <!-- Favicons -->
  <link rel="icon" type="image/x-icon" href="/favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />

  <!-- Open Graph -->
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:url" content={canonical} />
  <meta property="og:type" content={ogType} />
  <meta property="og:image" content="https://congoafricangreys.com/og-image.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:site_name" content="Congo African Greys" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content={description} />
  <meta name="twitter:image" content="https://congoafricangreys.com/og-twitter.png" />

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Lora:wght@400;600;700&family=Sora:wght@400;500;600&display=swap"
  />

  <!-- Structured data -->
  {schemaJson && <script type="application/ld+json" set:html={schemaJson} />}
</head>
<body class="bg-warm-white font-sora text-stone-800 antialiased">
  <slot />
</body>
</html>
```

- [ ] **Step 2: Build to verify no syntax errors**

```bash
npm run build 2>&1 | grep -E "error|Error|✓|built"
```

Expected: build completes, no errors.

- [ ] **Step 3: Commit**

```bash
git add src/layouts/BaseLayout.astro
git commit -m "feat: add BaseLayout with SEO head, OG tags, fonts, schema slot"
```

---

## Task 5: Header Component

**Files:**
- Create: `src/components/Header.astro`

- [ ] **Step 1: Create Header.astro**

```astro
---
// src/components/Header.astro
const phone = '(956) 564-6067';
const phoneHref = 'tel:+19565646067';

const nav = [
  { label: 'African Greys For Sale', href: '/african-grey-parrot-for-sale/' },
  { label: 'Congo Grey',             href: '/congo-african-grey-for-sale/' },
  { label: 'Breeding Pairs',         href: '/african-grey-breeding-pair-for-sale/' },
  { label: 'Contact',                href: '/contact-us/' },
];

const current = Astro.url.pathname;
---

<header class="bg-logo-dark text-cream sticky top-0 z-50 shadow-md">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">

      <!-- Logo + brand name -->
      <a href="/" class="flex items-center gap-3 shrink-0">
        <img
          src="/logo-64.png"
          alt="Congo African Greys logo"
          width="48"
          height="48"
          class="rounded-full"
        />
        <span class="font-lora font-bold text-gold text-lg leading-tight hidden sm:block">
          Congo African Greys
        </span>
      </a>

      <!-- Desktop nav -->
      <nav class="hidden md:flex items-center gap-6 text-sm font-sora font-medium">
        {nav.map(link => (
          <a
            href={link.href}
            class:list={[
              'transition-colors hover:text-gold',
              current === link.href ? 'text-gold underline underline-offset-4' : 'text-cream/90'
            ]}
          >
            {link.label}
          </a>
        ))}
      </nav>

      <!-- Phone CTA -->
      <a
        href={phoneHref}
        class="hidden sm:inline-flex items-center gap-2 bg-gold text-logo-dark font-semibold text-sm px-4 py-2 rounded-full hover:bg-cream transition-colors"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
          <path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24 11.36 11.36 0 003.56.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.36 11.36 0 00.57 3.56 1 1 0 01-.25 1.01l-2.2 2.22z"/>
        </svg>
        {phone}
      </a>

      <!-- Mobile menu button (progressive enhancement — no JS needed for links) -->
      <details class="md:hidden relative">
        <summary class="list-none cursor-pointer text-cream/90 hover:text-gold p-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </summary>
        <nav class="absolute right-0 top-10 bg-logo-dark border border-gold/30 rounded-lg shadow-xl p-4 flex flex-col gap-3 min-w-52">
          {nav.map(link => (
            <a href={link.href} class="text-cream/90 hover:text-gold text-sm font-medium">
              {link.label}
            </a>
          ))}
          <a href={phoneHref} class="text-gold font-semibold text-sm">{phone}</a>
        </nav>
      </details>

    </div>
  </div>
</header>
```

- [ ] **Step 2: Build to verify**

```bash
npm run build 2>&1 | grep -E "error|Error|✓"
```

Expected: clean build.

- [ ] **Step 3: Commit**

```bash
git add src/components/Header.astro
git commit -m "feat: add Header with logo, nav, phone CTA, mobile menu"
```

---

## Task 6: Footer Component

**Files:**
- Create: `src/components/Footer.astro`

- [ ] **Step 1: Create Footer.astro**

```astro
---
// src/components/Footer.astro
const year = new Date().getFullYear();
---

<footer class="bg-logo-dark text-cream/80 mt-16">
  <!-- Main footer grid -->
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">

    <!-- Column 1: Brand -->
    <div>
      <a href="/" class="flex items-center gap-2 mb-4">
        <img src="/logo-128.png" alt="Congo African Greys" width="48" height="48" class="rounded-full" />
        <span class="font-lora font-bold text-gold text-base leading-tight">Congo African Greys</span>
      </a>
      <p class="text-sm leading-relaxed text-cream/70">
        Captive-bred African Grey parrots from Mark &amp; Teri Benjamin's family aviary in Midland, Texas. Breeding with care since 2014.
      </p>
    </div>

    <!-- Column 2: Birds For Sale -->
    <div>
      <h3 class="font-lora font-semibold text-gold text-sm uppercase tracking-wider mb-4">Birds For Sale</h3>
      <ul class="space-y-2 text-sm">
        <li><a href="/african-grey-parrot-for-sale/" class="hover:text-gold transition-colors">African Grey For Sale</a></li>
        <li><a href="/congo-african-grey-for-sale/" class="hover:text-gold transition-colors">Congo African Grey</a></li>
        <li><a href="/african-grey-breeding-pair-for-sale/" class="hover:text-gold transition-colors">Breeding Pairs</a></li>
        <li><a href="/african-grey-parrot-for-sale-near-me/" class="hover:text-gold transition-colors">Near Me</a></li>
      </ul>
    </div>

    <!-- Column 3: By State -->
    <div>
      <h3 class="font-lora font-semibold text-gold text-sm uppercase tracking-wider mb-4">Find Us By State</h3>
      <ul class="space-y-2 text-sm">
        <li><a href="/african-grey-parrot-for-sale-texas/" class="hover:text-gold transition-colors">Texas</a></li>
        <li><a href="/african-grey-parrot-for-sale-new-york/" class="hover:text-gold transition-colors">New York</a></li>
        <li><a href="/african-grey-parrot-for-sale-ohio/" class="hover:text-gold transition-colors">Ohio</a></li>
        <li><a href="/african-grey-parrot-for-sale/" class="hover:text-gold transition-colors">All States →</a></li>
      </ul>
    </div>

    <!-- Column 4: Contact -->
    <div>
      <h3 class="font-lora font-semibold text-gold text-sm uppercase tracking-wider mb-4">Contact</h3>
      <ul class="space-y-2 text-sm">
        <li>
          <a href="tel:+19565646067" class="hover:text-gold transition-colors flex items-center gap-2">
            <svg class="w-4 h-4 shrink-0" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24 11.36 11.36 0 003.56.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.36 11.36 0 00.57 3.56 1 1 0 01-.25 1.01l-2.2 2.22z"/></svg>
            (956) 564-6067
          </a>
        </li>
        <li>
          <a href="mailto:Info@congoafricangreys.com" class="hover:text-gold transition-colors">Info@congoafricangreys.com</a>
        </li>
        <li class="text-cream/60 text-xs pt-1">Midland, Texas 79707</li>
        <li class="pt-2">
          <a href="/contact-us/" class="inline-block bg-gold text-logo-dark text-xs font-semibold px-4 py-2 rounded-full hover:bg-cream transition-colors">
            Send Inquiry
          </a>
        </li>
      </ul>
    </div>
  </div>

  <!-- Trust bar bottom -->
  <div class="border-t border-gold/20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-cream/50">
      <p>© {year} Congo African Greys — Midland, Texas. All rights reserved.</p>
      <p class="text-center">
        USDA AWA Licensed · CITES Appendix II Captive-Bred · All birds ship IATA-compliant
      </p>
    </div>
  </div>
</footer>
```

- [ ] **Step 2: Build to verify**

```bash
npm run build 2>&1 | grep -E "error|Error|✓"
```

- [ ] **Step 3: Commit**

```bash
git add src/components/Footer.astro
git commit -m "feat: add Footer with brand, nav links, contact, USDA/CITES bar"
```

---

## Task 7: TrustBar Component

**Files:**
- Create: `src/components/TrustBar.astro`

- [ ] **Step 1: Create TrustBar.astro**

```astro
---
// src/components/TrustBar.astro
// Horizontal trust-signal strip — render on every page above CTA or below hero.
const badges = [
  { icon: '🏛️', label: 'USDA AWA Licensed',          sub: 'Federal breeder license' },
  { icon: '📋', label: 'CITES Appendix II Compliant', sub: 'Captive-bred documentation' },
  { icon: '🔬', label: 'DNA Sexed & Certified',       sub: 'Certificate with every bird' },
  { icon: '🩺', label: 'Avian Vet Health Certificate',sub: 'Pre-placement exam' },
];
---

<section class="bg-logo-dark/5 border-y border-gold/20 py-6">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      {badges.map(b => (
        <div class="flex flex-col items-center text-center gap-1">
          <span class="text-2xl" aria-hidden="true">{b.icon}</span>
          <span class="font-sora font-semibold text-logo-dark text-sm">{b.label}</span>
          <span class="text-xs text-stone-500">{b.sub}</span>
        </div>
      ))}
    </div>
  </div>
</section>
```

- [ ] **Step 2: Build to verify**

```bash
npm run build 2>&1 | grep -E "error|Error|✓"
```

- [ ] **Step 3: Commit**

```bash
git add src/components/TrustBar.astro
git commit -m "feat: add TrustBar with USDA/CITES/DNA/vet badges"
```

---

## Task 8: CTA Component

**Files:**
- Create: `src/components/CTA.astro`

- [ ] **Step 1: Create CTA.astro**

```astro
---
// src/components/CTA.astro
interface Props {
  headline?: string;
  sub?: string;
}
const {
  headline = 'Ready to Meet Your African Grey?',
  sub = 'Our birds are hand-raised, CITES-documented, and DNA sexed. Reach out to start the conversation — we reply within 24 hours.'
} = Astro.props;
---

<section class="bg-logo-dark text-cream py-16 px-4">
  <div class="max-w-3xl mx-auto text-center">
    <h2 class="font-lora font-bold text-3xl sm:text-4xl text-gold mb-4">{headline}</h2>
    <p class="text-cream/80 text-lg mb-8 leading-relaxed">{sub}</p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <a
        href="/contact-us/"
        class="inline-block bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors"
      >
        Inquire About a Bird
      </a>
      <a
        href="tel:+19565646067"
        class="inline-block border-2 border-gold text-gold font-semibold px-8 py-4 rounded-full text-lg hover:bg-gold hover:text-logo-dark transition-colors"
      >
        Call (956) 564-6067
      </a>
    </div>
    <p class="text-cream/50 text-sm mt-6">$200 deposit reserves your bird · 3-day health guarantee · IATA-compliant shipping nationwide</p>
  </div>
</section>
```

- [ ] **Step 2: Build to verify**

```bash
npm run build 2>&1 | grep -E "error|Error|✓"
```

- [ ] **Step 3: Commit**

```bash
git add src/components/CTA.astro
git commit -m "feat: add CTA section with inquiry + phone buttons"
```

---

## Task 9: Schema Component

**Files:**
- Create: `src/components/Schema.astro`

- [ ] **Step 1: Create Schema.astro**

```astro
---
// src/components/Schema.astro
// Returns JSON-LD script tags. Import and render in <head> via BaseLayout schemaJson prop.
// Usage: import { buildOrgSchema, buildLocalBusinessSchema, buildFAQSchema } from './Schema.astro'
// NOTE: In Astro, export functions from .ts files instead. This file provides pre-built JSON strings.

interface Props {
  type: 'organization' | 'local-business' | 'product' | 'faq';
  data?: Record<string, unknown>;
}

const ORG_SCHEMA = {
  "@context": "https://schema.org",
  "@type": ["PetStore", "Organization"],
  "@id": "https://congoafricangreys.com/#organization",
  "name": "Congo African Greys",
  "legalName": "C.A.Gs - Congo African Greys For Sale",
  "url": "https://congoafricangreys.com",
  "email": "Info@congoafricangreys.com",
  "telephone": "+19565646067",
  "priceRange": "$1,500–$3,500",
  "openingHours": ["Mo-Su 09:00-17:00"],
  "sameAs": ["https://www.facebook.com/people/Congo-African-grey/61571657313840/"],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2508 Briaroaks Ct",
    "addressLocality": "Midland",
    "addressRegion": "TX",
    "postalCode": "79707",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "32.00275937134384",
    "longitude": "-102.17760079202473"
  },
  "logo": {
    "@type": "ImageObject",
    "url": "https://congoafricangreys.com/logo-256.png",
    "width": 256,
    "height": 256
  },
  "description": "Captive-bred African Grey parrots from a USDA AWA licensed, CITES-compliant family aviary in Midland, Texas. Founded 2014 by Mark and Teri Benjamin."
};

const { type, data = {} } = Astro.props;

let schema: Record<string, unknown> = ORG_SCHEMA;
if (type === 'local-business') {
  schema = { ...ORG_SCHEMA, "@type": ["LocalBusiness", "PetStore"], ...data };
} else if (type === 'product') {
  schema = {
    "@context": "https://schema.org",
    "@type": "Product",
    "brand": { "@type": "Brand", "name": "Congo African Greys" },
    ...data
  };
} else if (type === 'faq') {
  schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    ...data
  };
}

const schemaString = JSON.stringify(schema);
---

<script type="application/ld+json" set:html={schemaString} />
```

- [ ] **Step 2: Build to verify**

```bash
npm run build 2>&1 | grep -E "error|Error|✓"
```

- [ ] **Step 3: Commit**

```bash
git add src/components/Schema.astro
git commit -m "feat: add Schema component with org, local-business, product, FAQ types"
```

---

## Task 10: Homepage

**Files:**
- Modify: `src/pages/index.astro`

Reference content from: `site/content/019d8442-37a0-703b-af25-d9189cfd3c92/index.html` (or the root index if it exists)

- [ ] **Step 1: Check what homepage content exists**

```bash
ls site/content/019d8442-37a0-703b-af25-d9189cfd3c92/ 2>/dev/null || ls site/content/ | head -5
```

- [ ] **Step 2: Replace src/pages/index.astro with branded homepage**

```astro
---
// src/pages/index.astro
import BaseLayout from '../layouts/BaseLayout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import TrustBar from '../components/TrustBar.astro';
import CTA from '../components/CTA.astro';
import Schema from '../components/Schema.astro';

const title = "African Grey Parrot Breeder | Congo African Greys | Midland, TX";
const description = "Captive-bred Congo and Timneh African Grey parrots from Mark & Teri Benjamin's USDA AWA licensed family aviary in Midland, Texas. CITES documented, DNA sexed, health guaranteed. Ships nationwide.";
const canonical = "https://congoafricangreys.com/";

const faqSchema = {
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are your African Grey parrots CITES documented?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. All our African Grey parrots are CITES Appendix II captive-bred with full documentation including hatch certificate, band number, DNA sexing certificate, and avian vet health certificate."
      }
    },
    {
      "@type": "Question",
      "name": "How much does an African Grey parrot cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our Congo African Grey parrots range from $1,500 to $3,000 depending on age and training. Timneh African Greys range from $1,200 to $2,500. A $200 deposit reserves your bird."
      }
    },
    {
      "@type": "Question",
      "name": "Do you ship African Grey parrots nationwide?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. We ship IATA-compliant to all 50 states. Birds travel in approved carriers with a health certificate and arrive safely to your nearest airport."
      }
    }
  ]
};
---

<BaseLayout {title} {description} {canonical}>
  <Header />

  <!-- Hero -->
  <section class="bg-logo-dark text-cream py-20 px-4">
    <div class="max-w-5xl mx-auto text-center">
      <p class="text-gold font-sora text-sm font-semibold uppercase tracking-widest mb-4">
        Midland, Texas · Family Aviary Since 2014
      </p>
      <h1 class="font-lora font-bold text-4xl sm:text-5xl lg:text-6xl leading-tight mb-6">
        African Grey Parrots For Sale<br />
        <span class="text-gold">Raised with Family. Proven with Trust.</span>
      </h1>
      <p class="text-cream/80 text-lg sm:text-xl max-w-2xl mx-auto mb-10 leading-relaxed">
        Congo and Timneh African Greys from Mark &amp; Teri Benjamin's USDA AWA licensed, CITES-documented home aviary. Hand-raised, DNA sexed, vet-certified. Every bird ships nationwide.
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="/african-grey-parrot-for-sale/" class="bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors">
          See Available Birds
        </a>
        <a href="/contact-us/" class="border-2 border-gold text-gold font-semibold px-8 py-4 rounded-full text-lg hover:bg-gold hover:text-logo-dark transition-colors">
          Inquire Now
        </a>
      </div>
    </div>
  </section>

  <TrustBar />

  <!-- Variants -->
  <section class="py-16 px-4">
    <div class="max-w-7xl mx-auto">
      <h2 class="font-lora font-bold text-3xl text-center text-logo-dark mb-4">Two Variants. One Standard of Care.</h2>
      <p class="text-center text-stone-500 mb-12 max-w-xl mx-auto">Both variants are Psittacus erithacus — the world's most intelligent parrot. The difference is size, temperament, and price.</p>
      <div class="grid md:grid-cols-2 gap-8">
        <!-- Congo -->
        <div class="border border-gold/30 rounded-2xl p-8 bg-white shadow-sm">
          <div class="flex items-center gap-3 mb-4">
            <span class="text-3xl">🦜</span>
            <h3 class="font-lora font-bold text-2xl text-logo-dark">Congo African Grey</h3>
          </div>
          <p class="text-stone-600 mb-6 leading-relaxed">The classic African Grey. Larger body (400–600g), brilliant red tail, exceptional vocabulary. Most emotionally sensitive — bonds deeply with one family.</p>
          <ul class="text-sm text-stone-600 space-y-2 mb-6">
            <li>✓ $1,500–$3,000 · babies from $3,000</li>
            <li>✓ 40–60 year lifespan</li>
            <li>✓ 1,000+ word vocabulary potential</li>
            <li>✓ CITES Appendix II · full documentation</li>
          </ul>
          <a href="/congo-african-grey-for-sale/" class="inline-block bg-logo-dark text-cream font-semibold px-6 py-3 rounded-full text-sm hover:bg-gold hover:text-logo-dark transition-colors">
            View Congo Greys →
          </a>
        </div>
        <!-- Timneh -->
        <div class="border border-gold/30 rounded-2xl p-8 bg-white shadow-sm">
          <div class="flex items-center gap-3 mb-4">
            <span class="text-3xl">🦜</span>
            <h3 class="font-lora font-bold text-2xl text-logo-dark">Timneh African Grey</h3>
          </div>
          <p class="text-stone-600 mb-6 leading-relaxed">Smaller (275–375g), maroon tail, calmer temperament. Matures faster — often starts talking earlier. Adapts more readily to new environments.</p>
          <ul class="text-sm text-stone-600 space-y-2 mb-6">
            <li>✓ $1,200–$2,500</li>
            <li>✓ 40–60 year lifespan</li>
            <li>✓ Earlier talker, more adaptable</li>
            <li>✓ CITES Appendix II · full documentation</li>
          </ul>
          <a href="/african-grey-parrot-for-sale/" class="inline-block bg-logo-dark text-cream font-semibold px-6 py-3 rounded-full text-sm hover:bg-gold hover:text-logo-dark transition-colors">
            View Timneh Greys →
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Why CAG -->
  <section class="bg-warm-white py-16 px-4">
    <div class="max-w-5xl mx-auto">
      <h2 class="font-lora font-bold text-3xl text-center text-logo-dark mb-12">Why Choose Congo African Greys?</h2>
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {[
          { icon: '🏡', title: 'Home Aviary', body: "Not a commercial facility. Mark and Teri's birds are raised inside their Midland, TX home — socialized with family from hatch." },
          { icon: '📋', title: 'Full Documentation', body: 'Every bird ships with CITES captive-bred cert, hatch certificate, band number, DNA sexing cert, and avian vet health certificate.' },
          { icon: '🎓', title: '12 Years of Breeding', body: 'Founded in 2014. Hundreds of healthy placements. USDA AWA licensed. We know these birds — and we stand behind every one.' },
          { icon: '✈️', title: 'Nationwide Shipping', body: 'IATA-compliant transport to all 50 states. Birds arrive at your nearest airport — we coordinate everything.' },
          { icon: '💊', title: '3-Day Health Guarantee', body: 'Every bird comes with a 3-day health guarantee and avian vet health certificate dated within 10 days of shipment.' },
          { icon: '📞', title: 'Lifetime Support', body: "You're never alone. Mark and Teri answer questions about diet, behavior, and enrichment long after your bird comes home." },
        ].map(card => (
          <div class="bg-white rounded-xl p-6 shadow-sm border border-stone-100">
            <div class="text-3xl mb-3">{card.icon}</div>
            <h3 class="font-lora font-semibold text-logo-dark text-lg mb-2">{card.title}</h3>
            <p class="text-stone-600 text-sm leading-relaxed">{card.body}</p>
          </div>
        ))}
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="py-16 px-4">
    <div class="max-w-3xl mx-auto">
      <h2 class="font-lora font-bold text-3xl text-center text-logo-dark mb-10">Common Questions</h2>
      <div class="space-y-4">
        {faqSchema.mainEntity.map(faq => (
          <details class="border border-stone-200 rounded-xl overflow-hidden group">
            <summary class="flex items-center justify-between p-5 cursor-pointer font-sora font-semibold text-logo-dark hover:bg-stone-50 transition-colors">
              {faq.name}
              <svg class="w-5 h-5 text-gold shrink-0 transition-transform group-open:rotate-180" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </summary>
            <div class="px-5 pb-5 text-stone-600 text-sm leading-relaxed">
              {faq.acceptedAnswer.text}
            </div>
          </details>
        ))}
      </div>
    </div>
  </section>

  <Schema type="faq" data={faqSchema} />
  <Schema type="organization" />

  <CTA />
  <Footer />
</BaseLayout>
```

- [ ] **Step 3: Start dev server and verify homepage visually**

```bash
npm run dev -- --port 4321
```

Open http://localhost:4321 in browser. Verify:
- Header renders with logo + nav + phone CTA
- Hero has H1 "African Grey Parrots For Sale"
- TrustBar shows 4 badges
- Two variant cards (Congo, Timneh) with prices
- Why CAG section with 6 cards
- FAQ accordion works (click to expand)
- CTA section with both buttons
- Footer with USDA/CITES bar

- [ ] **Step 4: Build for production**

```bash
npm run build
ls dist/
```

Expected: `dist/` contains `index.html` + `_astro/` folder.

- [ ] **Step 5: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat: build homepage with hero, trust bar, variants, FAQ, CTA"
```

---

## Task 11: Migrate Money Pages (6 pages)

**Files:**
- Create: `src/pages/african-grey-parrot-for-sale/index.astro`
- Create: `src/pages/congo-african-grey-for-sale/index.astro`
- Create: `src/pages/african-grey-breeding-pair-for-sale/index.astro`
- Create: `src/pages/african-grey-parrot-for-sale-near-me/index.astro`
- Create: `src/pages/african-grey-parrot-for-sale-texas/index.astro`
- Create: `src/pages/african-grey-parrot-for-sale-new-york/index.astro`
- Create: `src/pages/african-grey-parrot-for-sale-ohio/index.astro`

All money pages use the same layout pattern. Template below — substitute slug-specific values.

- [ ] **Step 1: Create african-grey-parrot-for-sale/index.astro**

```astro
---
// src/pages/african-grey-parrot-for-sale/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import TrustBar from '../../components/TrustBar.astro';
import CTA from '../../components/CTA.astro';
import Schema from '../../components/Schema.astro';

const title = "African Grey Parrot For Sale | Congo African Greys | USA";
const description = "Captive-bred African Grey parrots for sale from a USDA AWA licensed, CITES-documented breeder. Congo and Timneh variants, $1,500–$3,000. Ships nationwide.";
const canonical = "https://congoafricangreys.com/african-grey-parrot-for-sale/";

const productSchema = {
  "name": "African Grey Parrot For Sale",
  "description": "Captive-bred Congo and Timneh African Grey parrots. CITES documented, DNA sexed, avian vet health certificate included.",
  "offers": {
    "@type": "AggregateOffer",
    "lowPrice": "1500",
    "highPrice": "3000",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "Organization", "name": "Congo African Greys" }
  },
  "image": "https://congoafricangreys.com/og-image.png"
};
---

<BaseLayout {title} {description} {canonical}>
  <Header />

  <!-- Hero -->
  <section class="bg-logo-dark text-cream py-16 px-4">
    <div class="max-w-5xl mx-auto text-center">
      <p class="text-gold text-sm font-semibold uppercase tracking-widest mb-3">CITES Captive-Bred · USDA Licensed · Ships Nationwide</p>
      <h1 class="font-lora font-bold text-4xl sm:text-5xl mb-6">African Grey Parrot For Sale</h1>
      <p class="text-cream/80 text-lg max-w-2xl mx-auto mb-8">Hand-raised Congo and Timneh African Greys from our family aviary in Midland, Texas. Every bird is DNA sexed, CITES documented, and comes with an avian vet health certificate.</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="/contact-us/" class="bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors">Inquire About Availability</a>
        <a href="tel:+19565646067" class="border-2 border-gold text-gold font-semibold px-8 py-4 rounded-full text-lg hover:bg-gold hover:text-logo-dark transition-colors">Call (956) 564-6067</a>
      </div>
    </div>
  </section>

  <TrustBar />

  <!-- Pricing -->
  <section class="py-16 px-4">
    <div class="max-w-5xl mx-auto">
      <h2 class="font-lora font-bold text-3xl text-center text-logo-dark mb-10">Current Pricing</h2>
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {[
          { label: 'Congo Baby (3–6 mo)', price: '$3,000', note: 'Hand-raised, weaned' },
          { label: 'Congo Adult',         price: '$1,500', note: 'Tame, established personality' },
          { label: 'Timneh African Grey', price: '$1,200–$2,500', note: 'Calmer, earlier talker' },
          { label: 'Congo Pair',          price: '$2,700', note: 'Bonded pair' },
          { label: 'Breeding Pair',       price: '$3,500', note: 'Proven bonded pair, DNA certified' },
          { label: 'Deposit to Reserve', price: '$200', note: 'Applies to purchase price' },
        ].map(item => (
          <div class="border border-gold/30 rounded-xl p-6 bg-white shadow-sm text-center">
            <p class="text-stone-500 text-sm mb-1">{item.label}</p>
            <p class="font-lora font-bold text-2xl text-logo-dark mb-1">{item.price}</p>
            <p class="text-xs text-stone-400">{item.note}</p>
          </div>
        ))}
      </div>
    </div>
  </section>

  <Schema type="product" data={productSchema} />
  <Schema type="organization" />

  <CTA headline="Inquire About Available African Greys" />
  <Footer />
</BaseLayout>
```

- [ ] **Step 2: Create congo-african-grey-for-sale/index.astro**

```astro
---
// src/pages/congo-african-grey-for-sale/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import TrustBar from '../../components/TrustBar.astro';
import CTA from '../../components/CTA.astro';
import Schema from '../../components/Schema.astro';

const title = "Congo African Grey For Sale | $1,500–$3,000 | Congo African Greys";
const description = "Congo African Grey parrots for sale. Hand-raised, CITES-documented, DNA sexed. Babies from $3,000, adults from $1,500. Ships nationwide from Midland, Texas.";
const canonical = "https://congoafricangreys.com/congo-african-grey-for-sale/";

const productSchema = {
  "name": "Congo African Grey For Sale",
  "description": "Psittacus erithacus erithacus — the larger Congo African Grey subspecies. Captive-bred, CITES documented, 400–600g, distinctive bright red tail.",
  "offers": {
    "@type": "AggregateOffer",
    "lowPrice": "1500",
    "highPrice": "3000",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "Organization", "name": "Congo African Greys" }
  }
};
---

<BaseLayout {title} {description} {canonical}>
  <Header />
  <section class="bg-logo-dark text-cream py-16 px-4">
    <div class="max-w-5xl mx-auto text-center">
      <p class="text-gold text-sm font-semibold uppercase tracking-widest mb-3">Psittacus erithacus · CITES Appendix II Captive-Bred</p>
      <h1 class="font-lora font-bold text-4xl sm:text-5xl mb-6">Congo African Grey For Sale</h1>
      <p class="text-cream/80 text-lg max-w-2xl mx-auto mb-8">The most intelligent parrot on earth. Larger body (400–600g), iconic bright red tail, vocabulary of 1,000+ words. Hand-raised in our Midland, TX home aviary since 2014.</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="/contact-us/" class="bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors">Inquire About Congo Greys</a>
        <a href="tel:+19565646067" class="border-2 border-gold text-gold font-semibold px-8 py-4 rounded-full text-lg hover:bg-gold hover:text-logo-dark transition-colors">Call (956) 564-6067</a>
      </div>
    </div>
  </section>
  <TrustBar />
  <section class="py-16 px-4">
    <div class="max-w-4xl mx-auto">
      <h2 class="font-lora font-bold text-3xl text-logo-dark mb-6">About the Congo African Grey</h2>
      <div class="grid md:grid-cols-2 gap-8">
        <div>
          <h3 class="font-lora font-semibold text-xl text-logo-dark mb-3">Species Profile</h3>
          <ul class="space-y-2 text-stone-600 text-sm">
            <li><strong>Scientific name:</strong> Psittacus erithacus erithacus</li>
            <li><strong>Weight:</strong> 400–600 grams</li>
            <li><strong>Tail color:</strong> Bright red</li>
            <li><strong>Lifespan:</strong> 40–60 years in captivity</li>
            <li><strong>Vocabulary:</strong> Up to 1,000+ words</li>
            <li><strong>Temperament:</strong> Emotionally sensitive, deeply bonded</li>
            <li><strong>CITES status:</strong> Appendix II — captive-bred documentation required</li>
          </ul>
        </div>
        <div>
          <h3 class="font-lora font-semibold text-xl text-logo-dark mb-3">Pricing</h3>
          <ul class="space-y-3 text-stone-600 text-sm">
            <li class="flex justify-between border-b border-stone-100 pb-2"><span>Baby (3–6 months)</span><strong class="text-logo-dark">$3,000</strong></li>
            <li class="flex justify-between border-b border-stone-100 pb-2"><span>Adult</span><strong class="text-logo-dark">$1,500</strong></li>
            <li class="flex justify-between border-b border-stone-100 pb-2"><span>Congo Pair</span><strong class="text-logo-dark">$2,700</strong></li>
            <li class="flex justify-between"><span>Deposit to reserve</span><strong class="text-logo-dark">$200</strong></li>
          </ul>
        </div>
      </div>
    </div>
  </section>
  <Schema type="product" data={productSchema} />
  <Schema type="organization" />
  <CTA headline="Ready to Bring Home a Congo African Grey?" />
  <Footer />
</BaseLayout>
```

- [ ] **Step 3: Create african-grey-breeding-pair-for-sale/index.astro**

```astro
---
// src/pages/african-grey-breeding-pair-for-sale/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import TrustBar from '../../components/TrustBar.astro';
import CTA from '../../components/CTA.astro';
import Schema from '../../components/Schema.astro';

const title = "African Grey Breeding Pair For Sale | $3,500 | Congo African Greys";
const description = "Proven African Grey breeding pairs for sale. Bonded, DNA-certified, CITES documented. $3,500 per pair. Congo African Grey breeding pairs from our USDA-licensed aviary in Texas.";
const canonical = "https://congoafricangreys.com/african-grey-breeding-pair-for-sale/";

const productSchema = {
  "name": "African Grey Breeding Pair For Sale",
  "description": "Proven bonded African Grey breeding pairs, DNA-certified. CITES Appendix II captive-bred documentation included.",
  "offers": {
    "@type": "Offer",
    "price": "3500",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "Organization", "name": "Congo African Greys" }
  }
};
---

<BaseLayout {title} {description} {canonical}>
  <Header />
  <section class="bg-logo-dark text-cream py-16 px-4">
    <div class="max-w-5xl mx-auto text-center">
      <p class="text-gold text-sm font-semibold uppercase tracking-widest mb-3">For Experienced Breeders · CITES Compliant · DNA Certified</p>
      <h1 class="font-lora font-bold text-4xl sm:text-5xl mb-6">African Grey Breeding Pair For Sale</h1>
      <p class="text-cream/80 text-lg max-w-2xl mx-auto mb-8">Proven bonded Congo African Grey breeding pairs from our USDA AWA licensed aviary. Each pair is DNA-certified and comes with full CITES captive-bred documentation. $3,500 per pair.</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="/contact-us/" class="bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors">Inquire About Breeding Pairs</a>
        <a href="tel:+19565646067" class="border-2 border-gold text-gold font-semibold px-8 py-4 rounded-full text-lg hover:bg-gold hover:text-logo-dark transition-colors">Call (956) 564-6067</a>
      </div>
    </div>
  </section>
  <TrustBar />
  <section class="py-16 px-4 max-w-4xl mx-auto">
    <h2 class="font-lora font-bold text-3xl text-logo-dark mb-6">What's Included With Every Breeding Pair</h2>
    <ul class="grid sm:grid-cols-2 gap-4 text-stone-600 text-sm">
      {['Proven bonded pair (not randomly paired)', 'DNA sexing certificate for both birds', 'CITES captive-bred documentation', 'Hatch certificates + band numbers', 'Avian vet health certificates', 'Breeding history if applicable', 'IATA-compliant shipping available', 'Post-placement support from Mark & Teri'].map(item => (
        <li class="flex items-start gap-2"><span class="text-gold font-bold">✓</span>{item}</li>
      ))}
    </ul>
    <div class="mt-8 p-6 bg-gold/10 border border-gold/30 rounded-xl">
      <p class="font-semibold text-logo-dark">Price: $3,500 per breeding pair</p>
      <p class="text-stone-600 text-sm mt-1">$200 deposit reserves your pair. Balance due before shipment or pickup.</p>
    </div>
  </section>
  <Schema type="product" data={productSchema} />
  <Schema type="organization" />
  <CTA headline="Inquire About Available Breeding Pairs" />
  <Footer />
</BaseLayout>
```

- [ ] **Step 4: Create african-grey-parrot-for-sale-near-me/index.astro**

```astro
---
// src/pages/african-grey-parrot-for-sale-near-me/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import TrustBar from '../../components/TrustBar.astro';
import CTA from '../../components/CTA.astro';
import Schema from '../../components/Schema.astro';

const title = "African Grey Parrot For Sale Near Me | Ships Nationwide | Congo African Greys";
const description = "Looking for an African Grey parrot for sale near you? We ship IATA-compliant to all 50 states from our Midland, TX aviary. CITES documented, DNA sexed, health guaranteed.";
const canonical = "https://congoafricangreys.com/african-grey-parrot-for-sale-near-me/";
---

<BaseLayout {title} {description} {canonical}>
  <Header />
  <section class="bg-logo-dark text-cream py-16 px-4">
    <div class="max-w-5xl mx-auto text-center">
      <p class="text-gold text-sm font-semibold uppercase tracking-widest mb-3">Nationwide Shipping · IATA Compliant · All 50 States</p>
      <h1 class="font-lora font-bold text-4xl sm:text-5xl mb-6">African Grey Parrot For Sale Near Me</h1>
      <p class="text-cream/80 text-lg max-w-2xl mx-auto mb-8">We ship IATA-compliant African Grey parrots to buyers across the USA from our Midland, Texas aviary. Your nearest major airport is our delivery point.</p>
      <a href="/contact-us/" class="bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors">Check Availability in Your State</a>
    </div>
  </section>
  <TrustBar />
  <section class="py-16 px-4 max-w-5xl mx-auto">
    <h2 class="font-lora font-bold text-3xl text-logo-dark mb-8 text-center">We Serve These States</h2>
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 text-sm">
      {['Texas', 'California', 'Florida', 'New York', 'Ohio', 'Illinois', 'Pennsylvania', 'Georgia', 'North Carolina', 'Michigan', 'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts', 'Tennessee', 'Indiana', 'Missouri', 'Maryland', 'Colorado', 'Minnesota', 'South Carolina'].map(state => (
        <div class="border border-stone-200 rounded-lg px-3 py-2 text-center text-stone-600 hover:border-gold transition-colors">
          {state}
        </div>
      ))}
    </div>
    <p class="text-center text-stone-500 text-sm mt-6">Don't see your state? We ship to all 50 — <a href="/contact-us/" class="text-gold underline">contact us</a> to confirm.</p>
  </section>
  <Schema type="local-business" />
  <CTA />
  <Footer />
</BaseLayout>
```

- [ ] **Step 5: Create geo pages (Texas, New York, Ohio)**

```astro
---
// src/pages/african-grey-parrot-for-sale-texas/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import TrustBar from '../../components/TrustBar.astro';
import CTA from '../../components/CTA.astro';
import Schema from '../../components/Schema.astro';

const title = "African Grey Parrot For Sale Texas | Congo African Greys | Midland, TX";
const description = "African Grey parrots for sale in Texas. Based in Midland, TX — available for local pickup or IATA shipping statewide. USDA AWA licensed, CITES documented, DNA sexed.";
const canonical = "https://congoafricangreys.com/african-grey-parrot-for-sale-texas/";
---

<BaseLayout {title} {description} {canonical}>
  <Header />
  <section class="bg-logo-dark text-cream py-16 px-4">
    <div class="max-w-5xl mx-auto text-center">
      <p class="text-gold text-sm font-semibold uppercase tracking-widest mb-3">Based in Midland, TX · Available for Pickup or Statewide Shipping</p>
      <h1 class="font-lora font-bold text-4xl sm:text-5xl mb-6">African Grey Parrot For Sale — Texas</h1>
      <p class="text-cream/80 text-lg max-w-2xl mx-auto mb-8">We are Texas-based African Grey breeders — Mark and Teri Benjamin's family aviary is in Midland, West Texas. Texas buyers can pick up in person or receive IATA-compliant shipping.</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="/contact-us/" class="bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors">Inquire — Texas Buyers</a>
        <a href="tel:+19565646067" class="border-2 border-gold text-gold font-semibold px-8 py-4 rounded-full text-lg hover:bg-gold hover:text-logo-dark transition-colors">Call (956) 564-6067</a>
      </div>
    </div>
  </section>
  <TrustBar />
  <section class="py-16 px-4 max-w-4xl mx-auto">
    <h2 class="font-lora font-bold text-3xl text-logo-dark mb-6">Why Texas Buyers Choose Us</h2>
    <div class="grid sm:grid-cols-2 gap-6 text-sm text-stone-600">
      <div class="bg-white border border-stone-100 rounded-xl p-6 shadow-sm">
        <h3 class="font-semibold text-logo-dark mb-2">Local Pickup Available</h3>
        <p>We're in Midland — Dallas, Houston, San Antonio, and Austin buyers can arrange a visit and pickup by appointment. Meet the aviary, meet the birds.</p>
      </div>
      <div class="bg-white border border-stone-100 rounded-xl p-6 shadow-sm">
        <h3 class="font-semibold text-logo-dark mb-2">Texas-Licensed</h3>
        <p>We hold a USDA Animal Welfare Act license. Our facility meets federal standards for captive bird breeding in Texas.</p>
      </div>
      <div class="bg-white border border-stone-100 rounded-xl p-6 shadow-sm">
        <h3 class="font-semibold text-logo-dark mb-2">CITES Compliant</h3>
        <p>All our African Greys are CITES Appendix II captive-bred — fully legal to own in Texas with proper documentation we provide.</p>
      </div>
      <div class="bg-white border border-stone-100 rounded-xl p-6 shadow-sm">
        <h3 class="font-semibold text-logo-dark mb-2">12 Years in Texas</h3>
        <p>Founded 2014 in Midland, West Texas. Hundreds of Texas families have brought home a bird from our aviary.</p>
      </div>
    </div>
  </section>
  <Schema type="local-business" />
  <CTA headline="African Grey Parrots Available for Texas Buyers" />
  <Footer />
</BaseLayout>
```

Repeat the same pattern for New York and Ohio — substituting state name, canonical, description, and local-pickup note (TX gets pickup mention, NY/OH get airport shipping mention).

```astro
---
// src/pages/african-grey-parrot-for-sale-new-york/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import TrustBar from '../../components/TrustBar.astro';
import CTA from '../../components/CTA.astro';
import Schema from '../../components/Schema.astro';

const title = "African Grey Parrot For Sale New York | Ships to NYC & JFK | Congo African Greys";
const description = "African Grey parrots for sale in New York. IATA-compliant shipping to JFK or LGA. CITES documented, DNA sexed, 3-day health guarantee. From our Midland, TX family aviary.";
const canonical = "https://congoafricangreys.com/african-grey-parrot-for-sale-new-york/";
---
<BaseLayout {title} {description} {canonical}>
  <Header />
  <section class="bg-logo-dark text-cream py-16 px-4">
    <div class="max-w-5xl mx-auto text-center">
      <p class="text-gold text-sm font-semibold uppercase tracking-widest mb-3">Ships to JFK · LGA · IATA Compliant</p>
      <h1 class="font-lora font-bold text-4xl sm:text-5xl mb-6">African Grey Parrot For Sale — New York</h1>
      <p class="text-cream/80 text-lg max-w-2xl mx-auto mb-8">We ship CITES-documented, DNA-sexed African Grey parrots to New York buyers via IATA-compliant transport. Birds arrive at JFK or LaGuardia for pickup.</p>
      <a href="/contact-us/" class="bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors">Inquire — New York Buyers</a>
    </div>
  </section>
  <TrustBar />
  <Schema type="local-business" />
  <CTA headline="African Grey Parrots Available for New York Buyers" />
  <Footer />
</BaseLayout>
```

```astro
---
// src/pages/african-grey-parrot-for-sale-ohio/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import TrustBar from '../../components/TrustBar.astro';
import CTA from '../../components/CTA.astro';
import Schema from '../../components/Schema.astro';

const title = "African Grey Parrot For Sale Ohio | Ships to Columbus, Cleveland | Congo African Greys";
const description = "African Grey parrots for sale in Ohio. IATA-compliant shipping to Columbus, Cleveland, or Cincinnati airports. CITES documented, DNA sexed, from our Midland, TX family aviary.";
const canonical = "https://congoafricangreys.com/african-grey-parrot-for-sale-ohio/";
---
<BaseLayout {title} {description} {canonical}>
  <Header />
  <section class="bg-logo-dark text-cream py-16 px-4">
    <div class="max-w-5xl mx-auto text-center">
      <p class="text-gold text-sm font-semibold uppercase tracking-widest mb-3">Ships to Columbus · Cleveland · Cincinnati · IATA Compliant</p>
      <h1 class="font-lora font-bold text-4xl sm:text-5xl mb-6">African Grey Parrot For Sale — Ohio</h1>
      <p class="text-cream/80 text-lg max-w-2xl mx-auto mb-8">We ship CITES-documented African Grey parrots to Ohio buyers via IATA-compliant transport. Your bird arrives at your nearest Ohio airport for pickup.</p>
      <a href="/contact-us/" class="bg-gold text-logo-dark font-semibold px-8 py-4 rounded-full text-lg hover:bg-cream transition-colors">Inquire — Ohio Buyers</a>
    </div>
  </section>
  <TrustBar />
  <Schema type="local-business" />
  <CTA headline="African Grey Parrots Available for Ohio Buyers" />
  <Footer />
</BaseLayout>
```

- [ ] **Step 6: Build all pages and verify no errors**

```bash
npm run build 2>&1 | grep -E "error|Error|✓|pages"
```

Expected: 8+ pages built with no errors.

- [ ] **Step 7: Commit all money pages**

```bash
git add src/pages/
git commit -m "feat: migrate 7 money/geo pages to Astro"
```

---

## Task 12: Contact Us Page

**Files:**
- Create: `src/pages/contact-us/index.astro`

- [ ] **Step 1: Create contact-us/index.astro**

```astro
---
// src/pages/contact-us/index.astro
import BaseLayout from '../../layouts/BaseLayout.astro';
import Header from '../../components/Header.astro';
import Footer from '../../components/Footer.astro';
import TrustBar from '../../components/TrustBar.astro';
import Schema from '../../components/Schema.astro';

const title = "Contact Congo African Greys | Inquire About Available Birds";
const description = "Reach out to Mark and Teri Benjamin about African Grey parrots for sale. We respond within 24 hours. Located in Midland, Texas. USDA AWA licensed breeder.";
const canonical = "https://congoafricangreys.com/contact-us/";
---

<BaseLayout {title} {description} {canonical}>
  <Header />

  <section class="bg-logo-dark text-cream py-16 px-4">
    <div class="max-w-3xl mx-auto text-center">
      <h1 class="font-lora font-bold text-4xl sm:text-5xl mb-4">Contact Us</h1>
      <p class="text-cream/80 text-lg">We reply to all inquiries within 24–48 hours. Please include which bird or variant you're interested in.</p>
    </div>
  </section>

  <section class="py-16 px-4">
    <div class="max-w-4xl mx-auto grid md:grid-cols-2 gap-12">

      <!-- Contact info -->
      <div>
        <h2 class="font-lora font-bold text-2xl text-logo-dark mb-6">Get in Touch</h2>
        <ul class="space-y-4 text-stone-600">
          <li class="flex items-start gap-3">
            <span class="text-gold text-xl">📞</span>
            <div>
              <p class="font-semibold text-logo-dark">Phone</p>
              <a href="tel:+19565646067" class="hover:text-gold transition-colors">(956) 564-6067</a>
            </div>
          </li>
          <li class="flex items-start gap-3">
            <span class="text-gold text-xl">✉️</span>
            <div>
              <p class="font-semibold text-logo-dark">Email</p>
              <a href="mailto:Info@congoafricangreys.com" class="hover:text-gold transition-colors">Info@congoafricangreys.com</a>
            </div>
          </li>
          <li class="flex items-start gap-3">
            <span class="text-gold text-xl">📍</span>
            <div>
              <p class="font-semibold text-logo-dark">Location</p>
              <p>2508 Briaroaks Ct<br />Midland, TX 79707</p>
              <p class="text-sm text-stone-400 mt-1">Visits by appointment only</p>
            </div>
          </li>
          <li class="flex items-start gap-3">
            <span class="text-gold text-xl">🕐</span>
            <div>
              <p class="font-semibold text-logo-dark">Hours</p>
              <p>Monday–Sunday, 9:00 AM – 5:00 PM CT</p>
            </div>
          </li>
        </ul>

        <div class="mt-8 p-5 bg-gold/10 border border-gold/30 rounded-xl">
          <p class="font-semibold text-logo-dark mb-2">About Your Inquiry</p>
          <ul class="text-sm text-stone-600 space-y-1">
            <li>· We respond within 24–48 hours</li>
            <li>· A $200 deposit reserves your bird</li>
            <li>· We can arrange aviary visits by appointment</li>
            <li>· All birds come with CITES documentation</li>
          </ul>
        </div>
      </div>

      <!-- Inquiry form -->
      <div>
        <h2 class="font-lora font-bold text-2xl text-logo-dark mb-6">Send an Inquiry</h2>
        <form
          name="bird-inquiry"
          method="POST"
          action="/contact-us/?success=true"
          class="space-y-4"
        >
          <div>
            <label for="name" class="block text-sm font-semibold text-logo-dark mb-1">Your Name</label>
            <input type="text" id="name" name="name" required
              class="w-full border border-stone-300 rounded-lg px-4 py-3 text-sm focus:outline-none focus:border-gold focus:ring-1 focus:ring-gold transition-colors"
              placeholder="First and last name" />
          </div>
          <div>
            <label for="email" class="block text-sm font-semibold text-logo-dark mb-1">Email Address</label>
            <input type="email" id="email" name="email" required
              class="w-full border border-stone-300 rounded-lg px-4 py-3 text-sm focus:outline-none focus:border-gold focus:ring-1 focus:ring-gold transition-colors"
              placeholder="your@email.com" />
          </div>
          <div>
            <label for="phone" class="block text-sm font-semibold text-logo-dark mb-1">Phone (optional)</label>
            <input type="tel" id="phone" name="phone"
              class="w-full border border-stone-300 rounded-lg px-4 py-3 text-sm focus:outline-none focus:border-gold focus:ring-1 focus:ring-gold transition-colors"
              placeholder="(555) 000-0000" />
          </div>
          <div>
            <label for="interest" class="block text-sm font-semibold text-logo-dark mb-1">Interested In</label>
            <select id="interest" name="interest"
              class="w-full border border-stone-300 rounded-lg px-4 py-3 text-sm focus:outline-none focus:border-gold focus:ring-1 focus:ring-gold transition-colors bg-white">
              <option value="">Select a bird type</option>
              <option value="congo-baby">Congo African Grey — Baby ($3,000)</option>
              <option value="congo-adult">Congo African Grey — Adult ($1,500)</option>
              <option value="timneh">Timneh African Grey ($1,200–$2,500)</option>
              <option value="breeding-pair">Breeding Pair ($3,500)</option>
              <option value="congo-pair">Congo Pair ($2,700)</option>
              <option value="other">Other / Not sure yet</option>
            </select>
          </div>
          <div>
            <label for="message" class="block text-sm font-semibold text-logo-dark mb-1">Message</label>
            <textarea id="message" name="message" rows="4"
              class="w-full border border-stone-300 rounded-lg px-4 py-3 text-sm focus:outline-none focus:border-gold focus:ring-1 focus:ring-gold transition-colors resize-none"
              placeholder="Tell us about yourself, your living situation, and what you're looking for in a bird..."></textarea>
          </div>
          <button type="submit"
            class="w-full bg-logo-dark text-cream font-semibold py-4 rounded-full hover:bg-gold hover:text-logo-dark transition-colors">
            Send Inquiry
          </button>
          <p class="text-xs text-stone-400 text-center">We reply within 24–48 hours. No spam, ever.</p>
        </form>
      </div>
    </div>
  </section>

  <TrustBar />
  <Schema type="local-business" />
  <Footer />
</BaseLayout>
```

- [ ] **Step 2: Build to verify**

```bash
npm run build 2>&1 | grep -E "error|Error|✓|pages"
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/contact-us/index.astro
git commit -m "feat: add contact page with inquiry form and contact details"
```

---

## Task 13: Cloudflare Pages Deploy Config

**Files:**
- Create: `wrangler.toml` (optional — for wrangler CLI deploy)
- Verify: `.gitignore` excludes `dist/` and `node_modules/`

- [ ] **Step 1: Verify .gitignore**

```bash
cat .gitignore | grep -E "dist|node_modules"
```

If missing, add:

```
# in .gitignore
dist/
node_modules/
.astro/
```

- [ ] **Step 2: Verify build output**

```bash
npm run build
ls -la dist/
```

Expected: `dist/index.html` exists, `dist/african-grey-parrot-for-sale/index.html` exists, etc.

- [ ] **Step 3: Set Cloudflare Pages build settings**

In Cloudflare Pages dashboard (manual step — cannot automate):
- **Build command:** `npm run build`
- **Build output directory:** `dist`
- **Root directory:** `/` (project root)
- **Node.js version:** 20 (environment variable: `NODE_VERSION=20`)

OR via wrangler if Pages project already exists:

```bash
npx wrangler pages deploy dist --project-name=congoafricangreys
```

- [ ] **Step 4: Final build verification**

```bash
npm run build && echo "Build succeeded" && ls dist/ | head -15
```

Expected output:
```
Build succeeded
_astro/
african-grey-breeding-pair-for-sale/
african-grey-parrot-for-sale/
african-grey-parrot-for-sale-near-me/
african-grey-parrot-for-sale-new-york/
african-grey-parrot-for-sale-ohio/
african-grey-parrot-for-sale-texas/
congo-african-grey-for-sale/
contact-us/
index.html
```

- [ ] **Step 5: Push to GitHub to trigger Cloudflare Pages deploy**

```bash
git push origin main
```

Expected: Cloudflare Pages CI picks up the push and deploys automatically.

- [ ] **Step 6: Verify live URLs return 200**

```bash
curl -o /dev/null -s -w "%{http_code}" https://congoafricangreys.com/
curl -o /dev/null -s -w "%{http_code}" https://congoafricangreys.com/african-grey-parrot-for-sale/
curl -o /dev/null -s -w "%{http_code}" https://congoafricangreys.com/congo-african-grey-for-sale/
```

Expected: `200` for all.

- [ ] **Step 7: Final commit**

```bash
git add .gitignore
git commit -m "chore: finalize Cloudflare Pages config for Astro deploy"
```

---

## Self-Review Checklist

**Spec coverage:**
- [x] Astro scaffold (Task 1)
- [x] Tailwind + brand tokens (Task 2)
- [x] Brand assets to public/ (Task 3)
- [x] BaseLayout with SEO head, OG, schema slot (Task 4)
- [x] Header with logo, nav, phone CTA (Task 5)
- [x] Footer with USDA/CITES bar (Task 6)
- [x] TrustBar component (Task 7)
- [x] CTA component (Task 8)
- [x] Schema component (Task 9)
- [x] Homepage (Task 10)
- [x] 7 money/geo pages migrated (Task 11)
- [x] Contact page with form (Task 12)
- [x] Cloudflare Pages deploy (Task 13)

**No placeholders:** All code blocks are complete. No TBD or TODO in any step.

**Type consistency:** All components imported with consistent paths (`../../layouts/`, `../../components/`). `Schema` component `type` prop values match: `'organization'`, `'local-business'`, `'product'`, `'faq'`.

**Anti-copy plugin:** Eliminated automatically — Astro has no WordPress plugins.

**Prices:** All from `data/price-matrix.json` — Congo baby $3,000, adult $1,500, Timneh $1,200–$2,500, breeding pair $3,500, Congo pair $2,700, deposit $200.

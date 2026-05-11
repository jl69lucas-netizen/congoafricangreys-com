# CongoAfricanGreys.com Phase 3 Production Site Kit

## Included Deliverables

### 1. Recommended Stack
- Astro static site generator
- Markdown content collections
- Cloudflare Pages hosting
- Tailwind CSS UI
- JSON-LD schema components

### 2. Folder Structure
```text
/
  astro.config.mjs
  package.json
  /public
    /images
  /src
    /components
      Header.astro
      Footer.astro
      CTA.astro
      FAQ.astro
      Schema.astro
    /layouts
      BaseLayout.astro
    /pages
      index.astro
      african-grey-for-sale.astro
      african-grey-parrot-for-sale.astro
      baby-african-grey-for-sale.astro
      congo-african-grey-for-sale.astro
    /content
      /money-pages
      /geo-pages
      /comparison-pages
      /blog-pages
      /trust-pages
```

### 3. Premium UI Direction
- Luxury breeder aesthetic
- Warm neutral palette
- Strong trust badges
- Video hero section
- Fast inquiry forms
- Mobile-first cards for available birds

### 4. Core Templates

#### Money Page Template
- Hero with trust statement
- Bird availability cards
n- Health guarantee
- Shipping nationwide
- FAQs
- CTA

#### Geo Page Template
- Localized intro
- Shipping to state/city
- Local trust copy
- FAQs
- CTA

#### Comparison Template
- Comparison table
- Verdict blocks
- Related birds CTA

#### Blog Template
- TOC
- Expert guide sections
- FAQs
- CTA

### 5. Automation Pipeline
1. Generate markdown in /src/content
2. Build pages from collections
3. Inject metadata + schema
4. Auto related posts/internal links
5. Deploy to Cloudflare Pages

### 6. Lead Funnel
- Sticky CTA: Reserve Your Bird
- Multi-step inquiry form
- SMS/email follow-up integration
- Trust testimonials near CTA

### 7. Cloudflare Pages Config
```text
Build command: npm run build
Output directory: dist
Node version: latest LTS
```

### 8. Priority Build Order
1. Homepage
2. 10 money pages
3. 20 geo pages
4. 10 trust pages
5. 20 comparison pages
6. 40 blogs

### 9. KPI Dashboard
- Indexed pages
- Top 10 rankings
- Leads/week
- Conversion rate
- Organic CTR

### 10. Next Step Prompt for Claude Code / Codex
```text
Build a production-ready Astro website for CongoAfricanGreys.com using markdown content collections, Tailwind styling, premium breeder design, schema components, and Cloudflare Pages deployment. Generate reusable templates for money, geo, comparison, trust, and blog pages.
```


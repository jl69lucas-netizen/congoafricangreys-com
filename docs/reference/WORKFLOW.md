# CongoAfricanGreys.com — Master Workflow

> **Read this before starting any new page, sprint, or monitoring cycle.**
> This is the authoritative end-to-end sequence for all 62 agents.

---

## Entry Point & Prerequisites

Before any work begins, verify these exist:

| Artifact | Location | How to create |
|----------|----------|---------------|
| `data/competitors.json` | `data/competitors.json` | Run `@cag-competitor-registry` |
| `data/structure.json` | `data/structure.json` | Run `@cag-structure-architect` |
| `docs/reference/top-pages.md` | Traffic baseline | Run `@cag-gsc-analytics` |
| `docs/research/gap-matrix-*.md` | Competitive gaps | Run `@cag-competitor-intel --all` |
| Session brief | `sessions/YYYY-MM-DD-session-brief.md` | Run `grill-me` skill |

**Hard Gate:** No page enters Sprint 2 (Content Production) until `data/structure.json` exists and `@cag-content-architect` has assigned a framework to the target page.

---

## Sprint 0 — Intelligence Gathering
*Run once per project, then quarterly. Takes ~1 session.*

### Parallel Tracks (run all three simultaneously)

**Track A — Competitive Intelligence**
```
@cag-competitor-registry
  → Discover 30 competitors from 10 seed keywords
  → Classify: direct breeders / classifieds / informational / marketplaces
  → USER GATE: approve competitor list
  → Output: data/competitors.json

@cag-competitor-intel --all
  → Analyze all 30 competitors across 10 metric categories
  → Output: docs/research/competitor-[name]-[date].md (×30)
  → Output: docs/research/gap-matrix-[date].md
```

**Track B — Traffic & LLM Intelligence**
```
@cag-gsc-analytics
  → Analyze data/analytics/ GSC CSV exports
  → Output: docs/reference/top-pages.md (clicks, impressions, positions)

@cag-llm-keyword-intel
  → Query ChatGPT + Perplexity + Gemini + Google AIO for top keywords
  → Record LLM Visibility scores in top-pages.md
  → Flag keywords where CAG is not cited in top 3 AI responses
  → Output: LLM Visibility column in top-pages.md
```

**Track C — Discovery**
```
grill-me skill (always first in a new session)
  → Reads: CLAUDE.md + top-pages.md + site-overview.md + last session brief
  → Asks 10-12 questions one at a time
  → Output: sessions/YYYY-MM-DD-session-brief.md
  → Includes: SESSION CONTEXT block (see format below)
```

### SESSION CONTEXT Block (output of grill-me)
```
SESSION CONTEXT:
- Page Type: [location | species guide | comparison | blog | money page | hub]
- Target Keyword: [exact keyword]
- Framework: [AIDA | PAS | QAB | Entity-Tree | H-S-S | Inverse Pyramid]
- Audit Status: [complete | pending → run cag-content-audit-agent first]
- LLM Visibility: [0–10 score | "not measured" → run cag-llm-keyword-intel]
- Structure.json Entry: [yes | no → run cag-structure-architect first]
- Hub Page: [/url/ of parent hub]
- Internal Links Needed: [list from cag-internal-link-agent]
- Competitor Benchmark: [URL or "none"]
```

### Sprint 0 Gate
Before proceeding to Sprint 1:
- [ ] `data/competitors.json` written (30 competitors)
- [ ] `docs/research/gap-matrix-[date].md` written
- [ ] `docs/reference/top-pages.md` updated
- [ ] LLM Visibility scores recorded for top 10 keywords
- [ ] Session brief written

---

## Sprint 1 — Architecture Sprint
*Run once at project start, then when adding new page clusters.*

### Sequence (in order)

```
Step 1: cag-structure-architect
  → Maps all 52 target pages into Silo or Reverse Silo structure
  → Ensures every page is ≤3 clicks from homepage
  → Output: data/structure.json

Step 2: cag-competitive-keyword-gap-agent
  → Fetches competitor sitemaps + pages via Playwright
  → Extracts H1/H2/title patterns from each
  → Scores gaps 1–10 (CITES content gaps flagged high)
  → Score ≥7 = build this page (enters content queue)
  → Output: docs/research/keyword-gap-[date].md

Step 3: cag-hub-builder  ← BUILD HUBS BEFORE SPOKES
  → Creates aggregator hub pages:
    - /african-grey-parrot-for-sale/ (location hub)
    - /african-grey-comparison/ (comparison hub)
    - /african-grey-parrot-guide/ (species hub)
    - /cites-documentation/ (trust hub)
  → Hub pages link to all their spoke pages

Step 4: cag-seasonal-content-agent
  → Builds data/seasonal-calendar.json
  → Major peaks: Spring Bird Season (Mar–May), Christmas, Valentine's Day, Mother's Day
  → Routes seasonal page briefs to content-architect

Step 5: cag-content-architect
  → Reads: gap matrix + structure.json + top-pages.md
  → Assigns framework to each page in priority queue:
    | Page Type | Framework |
    |-----------|-----------|
    | Location pages | AIDA + Entity-Tree |
    | Species guides | Entity-Tree + QAB |
    | Comparison pages | BAB + QAB |
    | Scam/trust pages | H-S-S + EBD |
    | Pricing pages | QAB + Inverse Pyramid |
    | Blog posts | PAS or AIDA |
    | About / breeder story | H-S-S |
  → Output: content brief queue (priority ordered by opportunity score)
```

### Sprint 1 Gate
- [ ] `data/structure.json` written
- [ ] Priority page queue defined (sorted by opportunity score ≥7)
- [ ] Hub pages built before spoke pages
- [ ] Framework assigned to each page type by content-architect

---

## Sprint 2 — Content Production
*The main build loop. Runs continuously as pages are built.*

### Per-Page Pipeline (Standard Flow)

```
1. cag-content-audit-agent [TARGET_URL] [KEYWORD] [PAGE_TYPE]
   → Phase 0: Outline (MUST be approved before Phase 1)
   → Phase 1: Intent gap analysis
   → Phase 2: Competitor analysis (most valuable phase)
   → Phase 3: Action plan + internal linking opportunities
   → Output: sessions/YYYY-MM-DD-[slug]-audit.md

2. cag-angle-agent
   → Generates 5–10 content angles before any writing begins
   → Selects: counter-intuitive angles, fear-based hooks, story-first openings
   → USER selects preferred angle

3. cag-paa-agent
   → Extracts real PAA questions from Google for target keyword
   → Formats answers for Featured Snippet capture
   → Passes question set to cag-faq-agent
   → Target: Position 0 + AIO citation

3.5. cag-seo-master-checklist skill  ← INVOKE BEFORE WRITING BEGINS
   → Skills path: skills/cag-seo-master-checklist.md
   → Phase 1: Competitor analysis (8+ competitors) + 10-category keyword fan-out (150–200 variants) + 150+ entity research
   → Phase 2: Page Outline Gate (Rule 51 — FULL STOP until outline approved)
   → Phase 3: 5-Tier Section Creation Form for each section (Rule 59)
   → Phase 4: 4-Part Delivery Format output (Rule 60)
   → Also defines: 3 anchor text strategies (Rule 58), Internal Linking Library (Rule 62 + Appendix A)
   → Reads: data/image-specs.json for image/infographic placement per page type

4A. cag-seo-content-writer [for standard optimization]
    → Writes SEO-optimized body copy
    → Uses framework assigned in Sprint 1
    → Applies: Negative Keyword Counter-Positioning (wild-caught, scam, cheap)
    → Generic-Slayer Filter: removes generic platitudes

4B. cag-non-commodity-content-agent [for breeder-authentic content]
    → Use when: page needs original insights competitors can't copy
    → Triad model: Archaeologist (mines real facts) → Provocateur (flips generic advice) → Stylist (CAG voice)
    → Requires: real breeder input from project-context.md

5. cag-faq-agent
   → QAB framework: Question → Answer → Benefit
   → Generates 6–12 questions per page
   → Sources: PAA output + GSC Queries.csv + CAG question bank
   → Output: FAQPage JSON-LD + <details>/<summary> accordion HTML

6. cag-section-builder [for custom page sections]
   → Section types: hero, features, faq, cta, testimonials, comparison-table,
                    price-card, jump_link, counter_snippet, toc, cites-trust-bar
   → Called by all page builder agents

7. cag-infographic-builder [if visual reinforcement needed]
   → Reads data/image-specs.json FIRST — confirms image type, width, and source for this page type
   → HTML/CSS infographics: 400px height fixed (desktop), auto (mobile)
   → Width: 760px for guides/blogs/care pages · 1100px for homepage/location/hero sections
   → Types: Comparison / Feature Grid / Process Flow / AI-Generated (Type 4) / Higgsfield MCP (Type 5)

8. cag-interactive-component [if calculator/quiz/checklist needed]
   → Pure HTML/CSS + minimal vanilla JS
   → Types: cost calculator, variant fit quiz, documentation checklist,
            shipping timeline estimator, CITES verification guide
   → Reads: data/financial-entities.json + data/price-matrix.json
```

### Specialty Flows (Run in Parallel with Main Queue)

**Location Pages (all states at once):**
```
cag-batch-rebuilder
  → Reads data/locations.json
  → Spawns cag-location-builder for each state (fork-parallel)
  → Reference template: Florida page (22 sections, 4,500+ words)
  → Each page gets state-specific: Google Maps embed, local regulations note, population data
  → Merges results → deploy → IndexNow
```

**Variant Pages:**
```
cag-variant-specialist
  → /congo-african-grey-for-sale/
  → /timneh-african-grey-for-sale/
  → Shared comparison table cross-linking both

cag-timneh-specialist
  → Deep Congo vs Timneh distinctions
  → Timneh pricing ($1,200–$2,500)
  → Cross-sell logic between variants
```

**Comparison Pages:**
```
cag-comparison-builder
  → Priority order: congo-vs-timneh → african-grey-vs-macaw → african-grey-vs-cockatoo
  → Reference: /male-vs-female-african-grey-parrots-for-sale/
```

**Pricing + Finance Pages:**
```
cag-financial-strategist
  → Reads data/financial-entities.json as source of truth
  → Covers: purchase price, setup costs, IATA shipping, annual costs, lifetime estimate
  → QAB framework for all FAQ sections
```

**Species Guide:**
```
cag-species-guide-builder
  → Entity-Tree framework (optimized for AI/AIO citation)
  → Reads data/price-matrix.json + data/financial-entities.json
  → /african-grey-parrot-guide/ hub + variant-specific guides
```

**Blog Posts:**
```
cag-blog-post-agent
  → Intent types: commercial, transactional, review, alternative, comparison
  → Keywords: from gap matrix (score ≥7 buyer-intent queries)
  → Full HTML with schema
```

**Scam / Trust Content:**
```
cag-scam-specialist
  → /how-to-avoid-african-grey-parrot-scams/ and scam cluster
  → Converts scam-fearful visitors → documented-purchase inquiries
```

**Bird Listings:**
```
cag-clutch-manager [when new bird available]
  → Updates data/clutch-inventory.json
  → Triggers cag-bird-personality

cag-bird-personality
  → CLEO/REX/NOVA/SAGE/IRIS buyer archetype profiles
  → Matches bird traits to buyer archetype
  → Includes: Bird Vitals Card HTML template + documentation block
```

---

## Sprint 3 — AEO/GEO Layer
*Runs over ALL new pages before deploy. This is a gate, not optional.*

### AEO/GEO Gate Checklist

Every page must pass ALL items before moving to Sprint 4:

```
AEO/GEO GATE — RUN IN THIS ORDER:

1. cag-keyword-verifier
   → Checks: title, H1, meta, first 100 words, H2 distribution,
             alt text, internal links, canonical
   → Flags: UNDER-OPTIMIZED (<85 keyword mentions) or OVER-STUFFED (>110)
   → AEO additions: entity coverage check, declarative statement density

2. cag-meta-description-agent
   → Standard: 50-60 char title, 140-160 char description
   → Extended: long-form metadata for high-competition pages
   → Audits: no duplicates, no missing tags

3. cag-external-link-agent
   → Inserts authority links from docs/reference/external-link-library.md
   → Rule: links at beginning or middle of sentences ONLY (never end)
   → Verifies: all URLs return 200 before inserting

4. cag-trust-signals-agent
   → Adds: Google Reviews widget HTML
   → Adds: Trust Badge row (USDA AWA / CITES / DNA Sexed / Avian Vet)
   → Adds: ReviewAggregateSchema
   → Adds: Counter Snippet blocks
   → Works with: cag-case-study-agent for testimonial content

5. cag-infographic-builder [if section needs visual reinforcement]
   → Comparisons, flag lists, benefit grids, process steps

6. Rules 55-62 Compliance Check (seo-rules.md)
   → Rule 55: Competitor analysis output — 8+ competitors, gap matrix, outranking strategy present
   → Rule 56: 10-category keyword fan-out documented (150–200 keyword variants)
   → Rule 57: 150+ entity mentions verified (people, locations, medical, brands, credentials)
   → Rule 58: 3 anchor text strategies used — exact match, conversational, branded (never repeat same anchor)
   → Rule 59: 5-Tier Section Creation Form completed for all sections
   → Rule 60: 4-Part Content Delivery Format present in output
   → Rule 61: Phone number (402-696-0317) appears ONLY in footer/schema — not in body copy
   → Rule 62: Internal links use Appendix A canonical URLs from skills/cag-seo-master-checklist.md
```

### AEO/GEO Schema Checklist (verify presence before deploy)

```
☐ FAQPage JSON-LD present (cag-faq-agent output)
☐ ≥1 declarative statement per H2 section (Entity-Tree format)
☐ First paragraph directly answers primary keyword question (Featured Snippet target)
☐ ReviewAggregateSchema present (cag-trust-signals-agent)
☐ BreadcrumbList schema present (cag-section-builder)
☐ LLM Visibility score recorded in top-pages.md (cag-llm-keyword-intel)
☐ LocalBusiness schema on all location pages
☐ VideoObject schema if YouTube video embedded (cag-video-seo-agent)
☐ No language implying wild-caught origin (CITES check)
☐ IMAGE-01: All images have alt text ≥250 characters (descriptive + keyword + context)
☐ IMAGE-02: Featured/hero images have 300+ word image description block in page copy
☐ IMAGE-03: Infographic widths match page type (760px for guides · 1100px for homepage/location pages)
☐ IMAGE-04: OG image (og:image) is 1200×630px — separate from portrait bird images
```

### LLM Visibility Probe (run after page goes live)

```
cag-llm-keyword-intel [for target keyword]
  → Queries: ChatGPT + Perplexity + Gemini + Google AIO
  → Checks: is CAG cited in top 3 responses for this keyword?
  → If NOT cited → route to cag-non-commodity-content-agent for entity strengthening
  → Records score in docs/reference/top-pages.md
```

---

## Sprint 4 — Technical Hardening
*Run as a batch across all new pages before deploy.*

### Agent Sequence

```
1. cag-accessibility-fixer
   → WCAG 2.1 AA: skip links, ARIA landmarks, form labels, alt text,
                  focus states, color contrast, heading order, button types
   → Priority: Critical → High → Medium
   → Lighthouse verification after fixes

2. cag-performance-fixer
   → Applies: font-display swap, LCP fetchpriority+preload,
              WooCommerce CSS, jQuery defer, lazysizes removal
   → Target: Perf Score ≥90

3. cag-canonical-fixer  ← CRITICAL — NEVER SKIP
   → Converts relative canonicals to absolute URLs
   → Fixes og:url and JSON-LD url fields
   → Relative canonicals = all pages indexed as "/" = zero rankings

4. cag-footer-standardizer
   → Audits all new pages for cag-footer-v1 compliance
   → Replaces outdated WordPress/Astra footer markup

5. cag-contact-form-updater
   → Audits inquiry forms for canonical CAG form markup
   → Checks: ARIA labels, accessibility violations, outdated markup

6. cag-google-map-agent [location pages only]
   → Adds state-level map embed
   → Fixes CSP object-src blocker (embed → iframe)
```

### Sprint 4 Gate
- [ ] Lighthouse Performance ≥90
- [ ] Lighthouse Accessibility ≥90
- [ ] All canonicals are absolute URLs
- [ ] Footer is cag-footer-v1 on all new pages
- [ ] Inquiry form passes ARIA check

---

## Sprint 5 — Deploy + Verify
*Run after every deploy.*

```
1. git push → GitHub Actions → Cloudflare Pages (auto-deploy)

2. cag-deploy-verifier
   → Verifies: all new pages return HTTP 200
   → Verifies: canonical URLs are absolute
   → Submits: all changed URLs to IndexNow
   → Output: sessions/YYYY-MM-DD-deploy-report.md

3. cag-redirect-manager [if any page slug changed]
   → Adds 301 redirect in site/content/_redirects
   → Detects + flattens redirect chains (A→B→C → A→C)
   → Validates all redirect targets exist on disk

4. sitemap-agent
   → Updates sitemap after any page change
   → Ensures all new pages are included
```

---

## Continuous Loops

### Weekly (every Sunday)

| Agent | What it checks | Output |
|-------|---------------|--------|
| `@cag-rank-tracker` | All 30 competitors — new pages, pricing shifts, location pages, blog posts, keyword movement | Change report; auto-triggers competitor-intel for movers |
| `@cag-branded-search-monitor-agent` | GSC CSV exports for branded queries ("congoafricangreys", "congo african greys") | Alert if >20% WoW drop; trust query triggers trust-signals-agent |
| `@cag-competitor-pricing-alert-agent` | Top 5 competitors' bird pricing via Playwright | Alert if any price changes >$200 |
| `@cag-llm-keyword-intel` | ChatGPT + Perplexity + Gemini for top 10 keywords | LLM Visibility scores; flags uncited keywords |

### Monthly

| Agent | What it checks | Output |
|-------|---------------|--------|
| `@cag-performance-monitor-agent` | Lighthouse: homepage + 5 top pages | sessions/YYYY-MM-DD-perf-report.md |
| `@cag-gsc-analytics` | GSC CSV exports for CTR gaps, ranking opportunities | Updated docs/reference/top-pages.md |
| `@cag-email-newsletter-agent` | Manual trigger | content/newsletters/YYYY-MM-newsletter.html |

### Quarterly

| Agent | What it checks | Output |
|-------|---------------|--------|
| `@cag-competitive-keyword-gap-agent` | Competitor sitemaps + H1/H2/titles | docs/research/keyword-gap-[date].md |
| `@cag-directory-submission-agent` | New bird breeder directories | data/directories.json |
| `@cag-nap-citation-agent` | Name/Address/Phone across all directory listings | sessions/YYYY-MM-DD-nap-audit.md |
| `@cag-funnel-analysis-agent` | Full buyer funnel (Discovery → Conversion) | sessions/YYYY-MM-DD-funnel-report.md |
| `@cag-backlink-outreach-agent` | Resource pages + guest post opportunities + vet referrals | data/backlink-tracker.json |

---

## Per-Event Triggers

Events that trigger agent chains regardless of schedule:

| Event | First Agent | Downstream Chain |
|-------|------------|-----------------|
| **New bird hatched** | `cag-clutch-manager` (status: available) | → `cag-bird-personality` → `cag-homepage-builder` (clutch announcement) → `cag-email-newsletter-agent` |
| **Bird reserved** | `cag-clutch-manager` (status: reserved) | → `cag-meta-description-agent` (update bird count in meta) |
| **Bird sold** | `cag-clutch-manager` (status: sold) | → `cag-review-collection-agent` (Day 7 trigger) → `cag-case-study-agent` (after review received) |
| **Competitor price change >$200** | `cag-competitor-pricing-alert-agent` | → `cag-financial-strategist` (reprice check) → `cag-meta-description-agent` |
| **Branded search drops >20%** | `cag-branded-search-monitor-agent` | → `cag-trust-signals-agent` → `cag-non-commodity-content-agent` |
| **New inquiry received** | Manual trigger | → `cag-email-lead-nurture-agent` (Day 0 template) |
| **New YouTube video published** | `cag-video-seo-agent` | → `cag-external-link-agent` (embed links across relevant pages) |
| **New A/B test needed** | `cag-conversion-tracker` identifies CTA issue | → `cag-heatmap-analyst-agent` (if data available) → `cag-ab-test-agent` |

---

## Decision Tree — "Which agent do I call next?"

```
START: What are you trying to do?

├── "Start a new session / new page"
│   └── grill-me skill → SESSION CONTEXT → cag-content-audit-agent

├── "Don't know what to build next"
│   └── cag-competitive-keyword-gap-agent → sort by score ≥7 → cag-content-architect

├── "Build a location page"
│   └── Single: cag-location-builder [state]
│       Batch: cag-batch-rebuilder → reads data/locations.json → fork-parallel

├── "Write page content"
│   └── Has cag-content-audit-agent been run? NO → run it first
│       → cag-angle-agent → cag-paa-agent
│       → Generic: cag-seo-content-writer
│       → Breeder-authentic: cag-non-commodity-content-agent
│       → FAQ: cag-faq-agent
│       → Sections: cag-section-builder

├── "Optimize a live page"
│   └── cag-keyword-verifier → cag-meta-description-agent → cag-trust-signals-agent

├── "Check site health"
│   └── cag-website-health skill → cag-performance-monitor-agent → cag-accessibility-fixer

├── "Weekly monitoring"
│   └── [all in parallel] cag-rank-tracker + cag-branded-search-monitor-agent + cag-competitor-pricing-alert-agent + cag-llm-keyword-intel

├── "Deploy a page"
│   └── cag-canonical-fixer → git push → cag-deploy-verifier → sitemap-agent

├── "A bird was sold"
│   └── cag-clutch-manager (status: sold) → Day 7: cag-review-collection-agent

└── "Something's wrong with conversions"
    └── cag-conversion-tracker → cag-heatmap-analyst-agent → cag-ab-test-agent
```

---

## Data File Dependencies

| Data File | Writers | Key Readers | Update Cadence |
|-----------|---------|-------------|----------------|
| `data/competitors.json` | cag-competitor-registry | rank-tracker, competitor-intel, competitive-keyword-gap-agent | Once (Phase 1) + as-needed |
| `data/structure.json` | cag-structure-architect | content-architect, location-builder, internal-link-agent | Post-reorg |
| `data/clutch-inventory.json` | cag-clutch-manager | email-lead-nurture, email-newsletter, review-collection, seasonal-content, meta-description | Real-time |
| `data/case-studies.json` | cag-case-study-agent, review-collection | email-newsletter, trust-signals | Post-testimonial |
| `data/price-matrix.json` | Manual | bird-personality, financial-strategist, interactive-component, meta-description | Pricing changes |
| `data/financial-entities.json` | Manual | financial-strategist, interactive-component, species-guide | Pricing changes |
| `data/locations.json` | Manual | location-builder, batch-rebuilder | New states |
| `data/directories.json` | directory-submission-agent | nap-citation-agent | Quarterly |
| `data/competitor-prices.json` | competitor-pricing-alert-agent | (reporting) | Weekly |
| `data/seasonal-calendar.json` | seasonal-content-agent | seasonal-content-agent | Annual |
| `data/backlink-tracker.json` | backlink-outreach-agent | (reporting) | Post-outreach |
| `data/image-specs.json` | Manual (design system updates) | cag-image-generation (skill), cag-infographic-builder, cag-image-pipeline, cag-location-builder, cag-homepage-builder, cag-blog-post-agent, cag-species-guide-builder, cag-comparison-builder | As-needed (design system changes) |
| `docs/reference/top-pages.md` | gsc-analytics, llm-keyword-intel | Most agents (traffic context) | Monthly |

---

## Quick Reference: Model Assignments

| Model | Agents | Why |
|-------|--------|-----|
| `claude-opus-4-7` | content-architect, all page builders, content writers, faq-agent, comparison-builder, financial-strategist, variant-specialist, scam-specialist, email-lead-nurture | Complex writing, framework selection, long-form content |
| `claude-sonnet-4-6` | All monitoring agents, technical agents, data agents, section-builder components | Speed-sensitive, structured output, audits |

---

## Non-Negotiable Rules (apply to all sprints)

1. **≥97% Confidence Gate** — Any agent writing to `src/pages/` must be ≥97% confident. If below: stop, state uncertainty, ask.
2. **Preview Before Apply** — Any page redesign MUST be previewed and approved before writing to site files.
3. **Same Content** — Redesigns never add or remove page content. Visual layer only.
4. **CITES Awareness** — Never imply wild-caught or illegal trade. All birds captive-bred with proper documentation.
5. **src/pages is Deployed** — All page edits go to `src/pages/<slug>/index.astro`. The `site/content/` directory is staging only.
6. **No Auto-Sends** — Email agents (lead-nurture, review-collection, newsletter) never auto-send. All templates require human review.
7. **Hub Before Spoke** — Always build hub pages before their spoke pages. Link equity flows correctly.
8. **Audit Before Build** — `cag-content-audit-agent` must run before any page rebuild.
9. **Canonical Before Deploy** — `cag-canonical-fixer` must run before every deploy. Relative canonicals = zero indexing.

---

## Post-Deploy Verification Checklist

Run within 2 minutes of every `git push` (Cloudflare Pages deploys in ~45 seconds):

### 1. Check new/modified pages return 200
```bash
curl -sI https://congoafricangreys.com/[new-slug]/ | grep "HTTP"
```
Expected: `HTTP/2 200`

### 2. Verify canonical is correct
```bash
curl -s https://congoafricangreys.com/[new-slug]/ | grep -i "canonical"
```
Expected: absolute URL matching the slug

### 3. Update page-inventory.md
Change status from 🟡 BUILT → 🟢 LIVE for each verified page.  
File: `docs/reference/page-inventory.md`

### 4. Update data/locations.json for state pages
Change `"status": "planned"` → `"status": "live"` for any new state pages.

### If any URL returns 404 after deploy:
1. Check `src/pages/[slug]/index.astro` exists
2. Run `npx astro build` locally — check for build errors
3. Check `public/_redirects` for conflicting rules
4. Check `astro.config.mjs` for any route configuration

### Slug Registry Rule (PREVENT FUTURE MISMATCHES)
Before building any new page, check `docs/reference/page-inventory.md` to confirm:
- The planned slug matches what will be linked to in navigation
- No existing page already covers this topic at a different URL
- If URLs will differ from what's linked, add a redirect BEFORE building the page
10. **Data Files Are Truth** — Never fabricate data. All claims come from: data files, GSC CSV exports, real page fetches, or direct breeder input.
11. **Phone Number Policy (Rule 61)** — Phone number 402-696-0317 appears ONLY in the footer and schema markup. All body copy CTAs must link to `/contact-us/` form — never display or link a phone number in page body content.
12. **Image-Specs Lookup Required** — Before any image generation or infographic creation, read `data/image-specs.json` to confirm the correct image source type, dimensions, and placement for the current page type.

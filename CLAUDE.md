# CongoAfricanGreys.com — Project Guide

## Working Directory
- Site content (markdown): `site/content/`
- Site archive (static HTML): `archive/simply-static-1-1775169284.zip`
- Deploy: TBD — Phase 2
- Domain: `congoafricangreys.com`

## Non-Negotiable Rules
- **Preview before apply** — Any page redesign MUST be previewed and approved before writing to site files.
- **Same content** — Redesigns never add or remove page content. Visual layer only.
- **Confidence Gate** — ≥97% confidence required before writing any site file. If below: stop, state uncertainty, ask.
- **CITES Awareness** — African Greys are CITES Appendix II. Never imply illegal trade. All birds captive-bred with proper documentation.
- **src/pages is deployed** — All HTML page edits MUST go to `src/pages/<slug>/index.html` or `src/pages/<slug>/index.astro`. The `site/content/` directory is a staging area; it does NOT get built directly. If both exist, `src/pages/` is authoritative.

## Site Model
Transactional + informational, modeled after MaltipoosForsale.com (`/Users/apple/Downloads/MFS/`).
- **Transactional:** "african grey parrot for sale [state]" → inquiry form submissions
- **Informational:** care guides, species guides, health, training, comparison pages
- **Two variants:** Congo African Grey (CAG) vs Timneh African Grey (TAG)

## Quick Start Commands

### "I want to build a new page"
→ `grill-me` skill → SESSION CONTEXT → `@cag-content-audit-agent`

### "I want to build all location pages"
→ `@cag-batch-rebuilder` → reads `data/locations.json` → forks `@cag-location-builder` per state

### "What should I build next?"
→ `@cag-competitive-keyword-gap-agent` → sort by opportunity score ≥7 → `@cag-content-architect`

### "Is the site healthy?"
→ `cag-website-health` skill → `@cag-performance-monitor-agent` → `@cag-accessibility-fixer`

### "Weekly monitoring check"
→ [parallel] `@cag-rank-tracker` + `@cag-branded-search-monitor-agent` + `@cag-competitor-pricing-alert-agent` + `@cag-llm-keyword-intel`

### "A bird was sold"
→ `@cag-clutch-manager` (status: sold) → Day 7: `@cag-review-collection-agent`

### "Deploy a page"
→ `@cag-canonical-fixer` → `git push` → `@cag-deploy-verifier` → `sitemap-agent` skill

---

## Reference Docs
- `docs/reference/WORKFLOW.md` — **MASTER WORKFLOW: read this before starting any new page, sprint, or monitoring cycle**
- `docs/reference/project-context.md` — **MASTER CONTEXT: read this at the start of every session**
- `docs/reference/site-overview.md` — site structure, page inventory, target states
- `docs/reference/seo-rules.md` — **MASTER SEO RULES (50 rules): read this before creating or modifying any page**
- `docs/reference/domain-knowledge.md` — variants, trust signals, health conditions, PAA questions
- `docs/reference/top-pages.md` — traffic baseline (populate after GSC API connected)
- `docs/reference/components.md` — **COMPONENT REGISTRY v2: 24 named components with variants — read before building any page section**
- `docs/reference/page-width.md` — **PAGE WIDTH RULES: Option A 1200px container system, breakpoints, responsive typography scale**
- `docs/design.md` — **MASTER DESIGN SPEC v2: Terracotta Warmth — colors, type, buttons, cards, motion, voice rules**
- `docs/design-system/README.md` — full narrative brand spec with identity, voice, iconography, and motion
- `src/styles/cag-design-system.css` — canonical CSS custom-property tokens (import in non-Tailwind pages)
- `data/competitors.json` — 30-competitor registry (source of truth)
- `data/analytics/` — GSC performance reports (2026-04-28)

## Phase 1 — Competitor Intelligence (Current Phase)

### Agents
- `.claude/agents/cag-competitor-registry.md` — discovers + registers 30 competitors; run first
- `.claude/agents/cag-competitor-intel.md` — deep multi-metric analysis; single or --all mode
- `.claude/agents/cag-rank-tracker.md` — weekly monitoring; runs every Sunday

### Session 1 Order of Operations
```
1. Run @cag-competitor-registry → approve 30 competitors → saved to data/competitors.json
2. Run @cag-competitor-intel --all → 30 reports + master gap matrix
3. Read docs/research/gap-matrix-[date].md → decide Phase 2 priorities
```

## Phase 2 — Full Agent System (Active)

### Skills

#### Framework Reference Skills
- `skills/framework-heading-hierarchy.md` — H1–H6 strategic keyword placement; maps each heading level to a keyword type and user intent; audit checklist + 5 H2 variation rule; African Grey examples throughout
- `skills/framework-aio-geo.md` — AIO + GEO optimization; entity-first writing, declarative statements, FAQPage schema; Featured Snippet capture (4 strategies) + 12-item checklist
- `skills/framework-qab.md` — Question→Answer→Benefit; all FAQ sections + pricing content
- `skills/framework-aida.md` — Attention→Interest→Desire→Action; high-intent commercial pages
- `skills/framework-eeat.md` — Experience/Expertise/Authoritativeness/Trustworthiness; credibility audit + schema

#### SEO & Content Skills
- `skills/cag-branded-search-skill.md` — branded query optimization; /why-choose-cag/ + /african-grey-reviews/ page specs; ReviewAggregateSchema; counter snippets; Contextual Intelligence for local SEO; CITES framing in all branded content
- `skills/keyword-cluster.md` — groups keywords into primary/secondary/LSI/long-tail/PAA tiers
- `skills/internal-link-agent.md` — orphan page finder, hub→spoke gap audit, anchor text fixes
- `skills/section-auditor.md` — section-by-section health scores; preserve vs patch vs rebuild verdict

#### Technical Skills
- `skills/cag-website-health.md` — technical audit: broken images, canonicals, www redirect, Core Web Vitals, Page Speed Audit (LCP <2.5s, CLS <0.1, INP <200ms)
- `skills/cag-footer-agent.md` — 5-column footer structure spec + audit rules; USDA AWA + CITES notice in bottom bar
- `skills/sitemap-agent.md` — manages sitemap files after any page change
- `skills/cag-image-generation.md` — multi-provider AI image generation (OpenAI DALL-E 3, Google Gemini 2.0 Flash + Imagen 3 fallback, Anthropic Claude prompt-refine) + WebP optimization; CITES safety rule: no cage/aviary/wild-capture imagery; keys in .openai-key / .google-key / .anthropic-key; hands off to cag-image-pipeline
- `skills/cag-logo-generator.md` — circular emblem logo spec for CongoAfricanGreys.com; African Grey parrot head centerpiece; top arc: "CongoAfricanGreys.com"; bottom arc: "Captive-Bred African Grey Breeders"; deep green/teal palette; DALL-E prompt + responsive HTML implementation

### Agents

#### Tier 2 — Page Builders
- `.claude/agents/cag-seo-content-writer.md` — writes body copy; 5 humor modes; Negative Keyword Counter-Positioning (wild-caught, scam, cheap); Generic-Slayer Filter; DO/DON'T guidelines; Counter Snippets
- `.claude/agents/cag-bird-personality.md` — CLEO/REX/NOVA/SAGE/IRIS buyer archetype profiles; Bird Vitals Card HTML template; documentation block required on every profile
- `.claude/agents/cag-faq-agent.md` — QAB FAQ sections + FAQPage JSON-LD; 7 distribution strategies; GSC Queries + PAA sourcing

#### Tier 3 — Content Intelligence
- `.claude/agents/cag-non-commodity-content-agent.md` — Triad model (Archaeologist/Provocateur/Stylist); breeder-authentic content a generic LLM cannot write; Generic-Slayer Filter; High-Resolution Detail per 500 words; CITES framing enforced
- `.claude/agents/cag-content-audit-agent.md` — 4-phase pre-build audit (Intent → Competitor → Action Plan → Internal Linking); PAGE_TYPE includes Species Guide, Variant Page, Scam Recovery, CITES Education, Care Guide; saves to sessions/; run before every page rebuild
- `.claude/agents/cag-keyword-verifier.md` — keyword placement, density, SEO hygiene; 85–105 total keyword distribution targets; UNDER-OPTIMIZED / OVER-STUFFED flags; exact line fixes
- `.claude/agents/cag-image-pipeline.md` — moves images from /content/ into site/, SEO renames, HTML ref updates; WebP Conversion Protocol; lazy loading; staging required
- `.claude/agents/cag-seasonal-content-agent.md` — 12-month content calendar; Spring Bird Season (Mar–May) as major peak; Christmas/Valentine's/Mother's Day/Summer templates adapted for parrot ownership; weaning caveat: African Greys 12–16 weeks; routes briefs to cag-seo-content-writer, banners to page builders; tracks in data/seasonal-calendar.json
- `.claude/agents/cag-email-newsletter-agent.md` — monthly 4-section newsletter: clutch update (clutch-inventory.json), African Grey tip (12-month rotation: nutrition/enrichment/health/bonding), family spotlight (case-studies.json), seasonal CTA; ≤500 words; never references wild-caught; saves to content/newsletters/
- `.claude/agents/cag-video-seo-agent.md` — YouTube SEO packages: title ≤60 chars, description 700–1000 chars (first 125 = hook), 15–20 tags, chapters, thumbnail brief; VideoObject JSON-LD; 4 playlists (Care Guide / Congo vs Timneh / Buyer's Guide / Talking & Training); African Grey-specific keyword angles

#### Tier 4 — Technical
- `.claude/agents/cag-accessibility-fixer.md` — full WCAG 2.1 AA audit: skip links, ARIA landmarks, form labels, alt text, focus states, color contrast, heading order, button types; Critical/High/Medium priority tiers; batch mode saving to sessions/; Lighthouse verification
- `.claude/agents/cag-performance-monitor-agent.md` — Lighthouse CLI audits; thresholds: LCP <2.5s, CLS <0.1, FCP <1.8s, TBT <200ms, Perf Score ≥90; audit list: homepage + 5 top pages; PageSpeed Insights API fallback; saves to sessions/YYYY-MM-DD-perf-report.md; run monthly

#### Tier 5 — Trust & Authority
- `.claude/agents/cag-trust-signals-agent.md` — Google Reviews widget HTML, Trust Badge row (USDA AWA / CITES / DNA Sexed / Avian Vet), ReviewAggregateSchema, Counter Snippet blocks; /why-choose-cag/ page spec; Contextual Intelligence review templates; works with case-study agent

#### Tier 6 — SEO & Analytics
- `.claude/agents/cag-competitor-registry.md` — discovers + registers 30 competitors; run first
- `.claude/agents/cag-competitor-intel.md` — deep multi-metric analysis; single or --all mode
- `.claude/agents/cag-rank-tracker.md` — weekly monitoring; runs every Sunday
- `.claude/agents/cag-directory-submission-agent.md` — bird breeder directory research + competitor gap analysis; Playwright form submission; data/directories.json registry; CITES safety rule: never submits to directories that accept wild-caught birds; run quarterly
- `.claude/agents/cag-competitive-keyword-gap-agent.md` — Playwright sitemap + H1/H2/title extraction; opportunity scoring 1–10 (CITES content gaps flagged as high priority); Score ≥7 = build this page; saves to docs/research/; run monthly
- `.claude/agents/cag-competitor-pricing-alert-agent.md` — weekly Playwright price extraction from top 5 competitors; $150+ single-variant change or $300+ overall triggers alert; data/competitor-prices.json uses "congo"/"timneh" keys; saves to sessions/YYYY-MM-DD-pricing-report.md
- `.claude/agents/cag-branded-search-monitor-agent.md` — monitors "congoafricangreys", "congo african greys" branded queries from local GSC CSV exports; WoW comparison; >20% drop = HIGH alert; trust query flag: "is congoafricangreys.com legit?" → activates cag-trust-signals-agent; saves to sessions/
- `.claude/agents/cag-nap-citation-agent.md` — Playwright fetches each directory listing in data/directories.json; compares Name/Address/Phone against credentials.md master; PASS/WARN/FAIL rating; saves to sessions/YYYY-MM-DD-nap-audit.md; run quarterly
- `.claude/agents/cag-backlink-outreach-agent.md` — 3 link types: resource page inclusions, guest posts (CITES-aware topic angles), avian vet referrals; Playwright-based discovery; outreach templates for each type; never references wild-caught; tracks in data/backlink-tracker.json

#### Tier 7 — Conversion & CRM
- `.claude/agents/cag-review-collection-agent.md` — Google review request email templates at 7/14/30-day intervals for confirmed sold buyers; reads clutch-inventory.json; tracks review status in case-studies.json; never auto-sends; references CITES compliance in templates
- `.claude/agents/cag-email-lead-nurture-agent.md` — 5-touch email sequence (Day 0/3/7/14/30); Touch 2 addresses CITES documentation questions; Touch 3 reads live clutch-inventory.json; pricing: CAG $1,500–$3,500 / TAG $1,200–$2,500; never misrepresents CITES status; all templates require human review
- `.claude/agents/cag-heatmap-analyst-agent.md` — interprets Clarity/Hotjar/FullStory data (scroll depth, click heatmap, rage clicks, session recordings, exit pages); African Grey lens: extended CITES-section reading = trust validation not confusion; sets up Microsoft Clarity if no tracking; requires user to provide data
- `.claude/agents/cag-funnel-analysis-agent.md` — 5-stage funnel (Discovery→Engagement→Intent Signal→Form Reach→Conversion); research cycle: 4–8 weeks for African Grey buyers; Stage 1 threshold: <30/month = focus on traffic first; Stage-specific CAG diagnosis (CITES doubt, scam fear, captive-bred credibility); benchmark: Overall >1.5%; run quarterly

## Phase 2 Workflow

See `docs/reference/WORKFLOW.md` for the authoritative sprint-based workflow.

### Sprint Order (Quick Reference)
1. **Sprint 0** — Intelligence: `competitor-registry` → `competitor-intel --all` → `gsc-analytics` → `llm-keyword-intel`
2. **Sprint 1** — Architecture: `structure-architect` → `competitive-keyword-gap` → `hub-builder` → `content-architect`
3. **Sprint 2** — Content: `content-audit` → `angle-agent` → `paa-agent` → writer → `faq-agent` → `section-builder`
4. **Sprint 3** — AEO/GEO Gate: `keyword-verifier` → `meta-description` → `external-link` → `trust-signals`
5. **Sprint 4** — Technical: `accessibility-fixer` → `performance-fixer` → `canonical-fixer` → `footer-standardizer`
6. **Sprint 5** — Deploy: `git push` → `deploy-verifier` → `redirect-manager` → `sitemap-agent`
7. **Continuous** — Weekly/monthly/quarterly monitoring loops (see WORKFLOW.md §8)

### Phase 2 Setup History
Transfer and adapt all MFS agents + skills for African Grey domain.
- MFS project: `/Users/apple/Downloads/MFS/`
- Skills land in: `skills/`
- Domain-agnostic agents copy quickly; domain-specific agents need full rewrite

## Design System & Component Rules

### Design System v2 — "Terracotta Warmth"

Active design system: `docs/design.md` (master reference) + `docs/design-system/README.md` (full narrative spec).

**Non-Negotiable Design Rules — enforced on every page build and rebuild:**
1. **Colors:** Three anchors only — Forest Green `#2D6A4F` (nav/headers), Clay `#e8604c` (all CTAs/buttons), Cream `#faf7f4` (page surface). `--gold` MUST always equal `--clay`.
2. **Type:** Lora 700 (serif) for ALL headlines. Sora 400–700 (sans) for ALL body, labels, buttons. No exceptions.
3. **Buttons:** Primary CTA = clay pill, `border-radius: 50px`. This is the brand signature. Form submit buttons only use `border-radius: 12px`.
4. **Cards:** 20px radius, 1px `--border`, warm shadow, white surface. Info cards use green header band.
5. **Shadows:** Always warm-tinted `rgba(60,30,10,…)`. Never neutral grey.
6. **Motion:** Max 0.2s transitions. No bounce, no parallax, no auto-playing video.
7. **Emoji:** Canonical set only (📞 ✉️ 📍 🕐 ✈️ 🚗 🦜 ✅ ❋). One per element. No marketing emoji (🎉 🔥 🚀).
8. **Anti-copy:** NEVER add `user-select: none` CSS or JS.

### Component Library v2

Full registry: `docs/reference/components.md` — 24 named components, each with 2–3 variants.

**Agent workflow for any page section build:**
1. Identify sections needed (hero, trust, FAQ, CTA, etc.)
2. Select 1–3 candidate components per section from the registry
3. **Show the user** candidates + variant options — a short text description is sufficient
4. **Wait for user approval** before writing any component code into a page
5. Implement only the approved component + variant

**Key components by use case:**

| Use Case | Component | Top Variants |
|---|---|---|
| Page hero | `cag-hero-v1`, `cag-split-hero` | v1 desktop, v2 alt, `editorial` Astro |
| Credibility strip | `cag-stats-bar` | `classic`, `dark` |
| Trust credentials | `cag-trust-stats` | `classic` |
| Bird listing | `cag-bird-card` | `classic`, `horizontal`, `feature` |
| Breeding pair | `cag-parent-birds` | `classic` |
| Pricing | `cag-pricing-table` | `classic`, `matrix` |
| Care tips | `cag-care-grid` | `classic` |
| Feature / why us | `cag-split-feature` | `editorial` |
| Scam content | `cag-scam-awareness` | `checklist`, `compare` |
| FAQ | `cag-faq-accordion` | `classic`, `editorial` |
| Long-form nav | `cag-toc-v1`, `cag-toc-v2` | v1 minimal, v2 bordered |
| Article callout | `cag-key-takeaway` | — |
| Sidebar full | `cag-toc-keytakeaway` | — combined |
| Inquiry form | `cag-contact-form` | `classic`, `application` |
| Newsletter | `cag-newsletter` | `banner`, `split` |
| Reviews | `cag-testimonials` | `grid`, `feature` |
| Footer | `cag-footer` | `dark` (default) |

### Page Width System — Option A (Classic 1200px)

Full spec: `docs/reference/page-width.md`

**Container rules — enforced on every page:**
- **All pages:** outer shell `max-width: 1200px` (`.container` class)
- **Informational / long-form pages:** inner text wrapper `max-width: 760px` (`.container-text` class)
- **All `<p>` tags:** `max-width: 70ch` — prevents unreadable long lines on wide screens

**Page type → container assignment:**
- Visual / transactional (homepage, bird listings, location pages): `.container` 1200px, full-width grids
- Informational (scam guide, care guides, species guides, blog): `.container` outer + `.container-text` 760px inner

**Breakpoints:**
- Desktop ≥1025px: 1200px centered, 48px padding
- Tablet 768–1024px: fluid 90–94%, 32px padding
- Mobile ≤767px: fluid 92%, 16px padding

**Responsive typography:** When writing or updating page CSS, apply the scale from `docs/design.md` §Responsive Typography Scale. Body line-height 1.6–1.7. No inline styles overriding the scale.

**Never** hard-code `max-width: 1180px` — use `1200px` or `var(--container)`.

---

## Scripts
- TBD — Phase 2

## Data Files
- `data/competitors.json` — managed by cag-competitor-registry
- `data/keywords/` — keyword clusters (Phase 2)
- `data/rankings/` — weekly rank snapshots (Phase 2)
- `data/analytics/` — GSC / performance data

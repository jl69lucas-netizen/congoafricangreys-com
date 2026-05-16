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

## Site Model
Transactional + informational, modeled after MaltipoosForsale.com (`/Users/apple/Downloads/MFS/`).
- **Transactional:** "african grey parrot for sale [state]" → inquiry form submissions
- **Informational:** care guides, species guides, health, training, comparison pages
- **Two variants:** Congo African Grey (CAG) vs Timneh African Grey (TAG)

## Reference Docs
- `docs/reference/project-context.md` — **MASTER CONTEXT: read this at the start of every session**
- `docs/reference/site-overview.md` — site structure, page inventory, target states
- `docs/reference/seo-rules.md` — **MASTER SEO RULES (50 rules): read this before creating or modifying any page**
- `docs/reference/domain-knowledge.md` — variants, trust signals, health conditions, PAA questions
- `docs/reference/top-pages.md` — traffic baseline (populate after GSC API connected)
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

## Phase 2 Setup History
Transfer and adapt all MFS agents + skills for African Grey domain.
- MFS project: `/Users/apple/Downloads/MFS/`
- Skills land in: `skills/`
- Domain-agnostic agents copy quickly; domain-specific agents need full rewrite

## Scripts
- TBD — Phase 2

## Data Files
- `data/competitors.json` — managed by cag-competitor-registry
- `data/keywords/` — keyword clusters (Phase 2)
- `data/rankings/` — weekly rank snapshots (Phase 2)
- `data/analytics/` — GSC / performance data

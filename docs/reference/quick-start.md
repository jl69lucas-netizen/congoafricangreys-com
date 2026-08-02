# C.A.Gs Quick Start — task to entry point

> Moved out of `CLAUDE.md` on 2026-08-02 (Phase 4 of the self-improving quality loop).
> The content below is **verbatim** — nothing was rewritten on the way out, because a
> registry that gets paraphrased during a move is a registry nobody can trust afterwards.
> `CLAUDE.md` now routes here instead of carrying it. The full routing table. CLAUDE.md keeps an abridged version of the same map.

## Quick Start Commands

### "I want to build a new page"
→ Sprint 0 done? **NO** → `@cag-competitor-intel --all` + `@cag-gsc-analytics` first
→ Sprint 0 done? **YES** → `grill-me` skill (loads gap matrix + top-pages before asking)
→ `@cag-content-audit-agent` → **Section Map + Component Gate** (approve before writing)
→ `@cag-angle-agent` → `@cag-paa-agent` → `skills/cag-seo-master-checklist` → build

### "Audit a page" (deep strategic audit)
→ `skills/cags-comprehensive-page-audit-system` (give it a URL) → produces `sessions/YYYY-MM-DD-audit-<slug>.md` → route fixes to the relevant builder. Batch mode → audit backlog → `@cag-strategy-synthesizer`.

### "Build / rebuild / polish a comparison page"
→ `skills/cag-comparison-page-builder` (research protocol → 22–25-section blueprint; all 8 cluster pages are LIVE — confirm the on-disk slug, default mode is REBUILD) → `skills/cag-duplicate-content-gate` BEFORE outline approval AND at final pass (pairwise vs ALL siblings) → `skills/cag-final-page-pass`

### "Build / rebuild a for-sale or buy page"
→ `skills/cag-for-sale-page-builder` (22-page transactional cluster: 17 for-sale + 5 buy-prefixed, ALL LIVE — REBUILD mode; MFS formula + comparison pipeline, transactional profile; egg page = truth-forward hybrid) → `skills/cag-duplicate-content-gate` BEFORE outline approval AND at final pass (pairwise vs ALL siblings + comparison cluster) → `skills/cag-final-page-pass`. Program plan: `docs/superpowers/plans/2026-07-19-for-sale-pages-program.md`.

### "Build a Reddit-modifier page / capture '<keyword> reddit' queries"
→ `skills/reddit-strategy` (compact 100–400-word pages, real threads only, cornerstone ladder, `/african-grey-reddit/` hub LAST) → `skills/cag-duplicate-content-gate` vs the parent comparison page → `python3 scripts/generate_sitemaps.py`

### "I want to build all location pages"
→ `@cag-batch-rebuilder` → reads `data/locations.json` → forks `@cag-location-builder` per state

### "What should I build next?"
→ `@cag-competitive-keyword-gap-agent` → sort by opportunity score ≥7 → `@cag-content-architect`

### "Is the site healthy?"
→ `cag-website-health` skill → `@cag-performance-monitor-agent` → `@cag-accessibility-fixer`

### "Give a page a final pass / is this page done?"
→ `skills/cag-final-page-pass` (THE final gate, ANY page type incl. bird /available/) → `npx astro build` → `python3 scripts/final_page_audit.py [--birds]` → one PASS/WARN/FAIL verdict + triaged fixes → deploy

### "Weekly monitoring check"
→ [parallel] `@cag-rank-tracker` + `@cag-branded-search-monitor-agent` + `@cag-competitor-pricing-alert-agent` + `@cag-llm-keyword-intel`

### "I want to list an available bird"
→ `skills/cag-bird-listing-page` (one page per bird in `data/clutch-inventory.json` → `src/pages/available/<slug>/index.astro`; single Product/Offer, 700–1,000 words; PBFD/Polyomavirus PCR screening IS assertable — confirmed by breeder 2026-06-20) → `@cag-clutch-manager` syncs status → `python3 scripts/generate_sitemaps.py`

### "A bird was sold"
→ `@cag-clutch-manager` (status: sold) → retire/301 the `/available/<slug>/` page per the `cag-bird-listing-page` lifecycle (never leave a sold bird `InStock`) → Day 7: `@cag-review-collection-agent`

### "Deploy a page"
→ `@cag-canonical-fixer` → `git push` → `@cag-deploy-verifier` → `sitemap-agent` skill

---

## Reference Docs
- `MANUAL INTERIOR-PAGE CHECKLIST.md` (repo root) — **THE manual, copy-paste, verify-each-step build guide (Hero → CTA, Parts A–N) for every informational/secondary page** (health, shipping, FAQ, privacy, care/resource, about, why-choose, scam, etc.) — same design + SEO method as the homepage. Excludes comparison/location/"…for-sale"/blog (own structure). Machine cascade: master skill §Interior-Page Profile + `cag-content-architect` routing + 8 interior builders.
- `BIRD-PAGE-BUILD-MANUAL.md` (repo root) — **THE copy-paste, verify-each-step runbook for POLISHING/DIFFERENTIATING/QA-ing `/available/` bird pages + hub** (Parts A–H: differentiation, geo, perf, a11y, schema, links, audit, deploy). Companion to skill `cag-bird-page-excellence`. Distinct from `cag-bird-listing-page` (from-scratch builder) and `cag-final-page-pass` (mechanical gate). Lessons/failure log: `docs/superpowers/sessions/2026-06-27-bird-pages-lessons.md`; prompt templates: `docs/superpowers/sessions/2026-06-27-bird-pages-prompt-log.md`.
- `PRODUCT.md` (repo root) — **BRAND CONTEXT (strategic): register, users, brand personality, anti-references, design principles, a11y bar. READ FIRST before any design/content work (see Non-Negotiable Rules). Auto-loaded by `/impeccable`.**
- `DESIGN.md` (repo root) — **BRAND CONTEXT (visual): locked palette + AA clay variants, typography, components, layout, motion, iconography. READ FIRST alongside `PRODUCT.md`. Auto-loaded by `/impeccable`.**
- `IMAGE-DESIGNS.md` (repo root) — **IMAGE ART-DIRECTION source of truth: crop ratios, reusable style wrapper, negative list (no logos/watermarks/🦜/other species), lighting, focal length, scene-types per page type. READ FIRST before any image work, alongside DESIGN.md. Consumed by all image skills/agents.**
- `docs/reference/WORKFLOW.md` — **MASTER WORKFLOW: read this before starting any new page, sprint, or monitoring cycle**
- `docs/reference/project-context.md` — **MASTER CONTEXT: read this at the start of every session**
- `docs/reference/site-overview.md` — site structure, page inventory, target states
- `docs/reference/seo-rules.md` — **MASTER SEO RULES (62 rules): read this before creating or modifying any page**
- `docs/reference/domain-knowledge.md` — variants, trust signals, health conditions, PAA questions
- `docs/reference/research-blocked-sites.md` — **RESEARCH FALLBACK for Reddit & blocked sites (binding on every research agent/skill): fetch escalation ladder Firecrawl → WebFetch(UA retry) → Playwright/chrome-devtools headless → `last30days-skill` (https://github.com/mvanhorn/last30days-skill, recency-scoped, great for Reddit/recent threads; not installed by default). Never fabricate un-fetched data.**
- `docs/reference/technical-seo-fixes-backlog.md` — **Lighthouse/axe fixes to sweep across pages (from the Timneh for-sale audit 2026-07-22): for-sale dial/rail AA-contrast fixes (`.tdial .num`/"of N" → `#6b625a`, `.railB .p` → `#c9f2db`, no `opacity` dimming on nav pills), GTM/Rocket-Loader unused-JS, responsive available-card srcset.**
- `docs/reference/top-pages.md` — traffic baseline (populate after GSC API connected)
- `docs/reference/components.md` — **COMPONENT REGISTRY v2: 24 named components with variants — read before building any page section**
- `docs/reference/page-width.md` — **PAGE WIDTH RULES: Option A 1200px container system, breakpoints, responsive typography scale**
- `docs/reference/secure-credentials.md` — **SECRETS HANDLING: the clipboard method (`$(pbpaste)`) for saving API keys/tokens; git-token rotation runbook; never put a literal secret in a command, file, or chat**
- `docs/design.md` — **MASTER DESIGN SPEC v2: Terracotta Warmth — colors, type, buttons, cards, motion, voice rules**
- `docs/design-system/README.md` — full narrative brand spec with identity, voice, iconography, and motion
- `src/styles/cag-design-system.css` — canonical CSS custom-property tokens (import in non-Tailwind pages)
- `data/competitors.json` — 30-competitor registry (source of truth)
- `data/analytics/` — GSC performance reports (2026-04-28)

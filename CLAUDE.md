# CongoAfricanGreys.com — Project Guide

## Working Directory
- Site content (markdown): `site/content/`
- Site archive (static HTML): `archive/simply-static-1-1775169284.zip`
- Deploy: GitHub Actions → Cloudflare Pages (auto on push to main)
- Domain: `congoafricangreys.com`

## Non-Negotiable Rules
- **Design Context — READ FIRST (applies to EVERY agent, skill, and task)** — Before any design, content, page, or component work, you MUST read the two brand-context files at the repo root: **`PRODUCT.md`** (strategic: register, users, brand personality, anti-references, design principles, accessibility bar) and **`DESIGN.md`** (visual: locked palette + `--clay-ink`/`--clay-text` AA variants, typography, components, layout, motion, iconography). They are the single source of truth for *who/what/why* and *how it looks*, and the `/impeccable` skill auto-loads them. Treat them as binding alongside `docs/design.md`; if they ever conflict with older docs, surface it rather than guessing. Do not produce brand/visual output without having consulted them this session.
- **Visual-First Workflow is the DEFAULT (ALWAYS) — applies to every design/page/component/layout task, new OR existing** — For any design, page, section, component, or layout work, use the **superpowers brainstorming visual companion** (local browser server showing mockups, hero comparisons, section-layout diagrams, side-by-side options) by default — this is the breeder's confirmed way of working (2026-06-19/20, "like we did on the Roys page"). The full methodology is binding: (1) **visual companion screens** for skeleton / hero / component decisions (push HTML screens, let the breeder click-select); (2) a **per-section distribution matrix** shown for approval BEFORE any code — section taxonomy, ordered topic→micro stack, framework per section, word-count split, and **A/B/C categories** (A=mandatory core, B=competitor-match, C=our-moat-competitors-lack) with a grounded *why* on each B/C row; (3) always mark the **Recommended** pick + why + named trade-off on every option set (per the Recommend+Why rule). Do not jump to writing page code before the visual + matrix approval. Stacks with — does not replace — **Preview before apply**.
- **Preview before apply** — Any page redesign MUST be previewed and approved before writing to site files.
- **Same content** — Redesigns never add or remove page content. Visual layer only.
- **Confidence Gate + Clarification Checkpoint (ALWAYS) — applies to every agent, skill, and build** — ≥97% confidence required before writing any site file. When confidence drops below 97% **mid-build, do NOT dead-stop the whole job** (the old behavior silently lost in-context drafts when a session ended before the human replied). Instead run the **Clarification Checkpoint**: (1) **write finished work to disk first** — cleared sections to the page, in-progress notes + the open question to the live session brief's `## Open Flags` (so a stop costs at most the one uncertain piece and the question survives session teardown); (2) **ask the user exactly ONE narrow question** (mark a Recommended answer + why, per the Recommend+Why rule); (3) **keep building every part that isn't blocked** — only the uncertain unit waits for the answer. The live brief is the file `grill-me` created (`sessions/YYYY-MM-DD-session-brief.md`); if none exists, create one before stopping. This rule is injected into all 68 agent Golden Rules via `scripts/add_clarification_checkpoint_rule.py`. (Data-integrity Confidence-Gate variants — "only report data you actually fetched, never fabricate" — are unchanged; this only upgrades the *file-write* stop behavior.)
- **Heading Hierarchy Outline Gate (ALWAYS) — applies to EVERY page, agent, and skill, BEFORE any create/edit/update** — The breeder repeatedly caught skipped heading levels and pages shipping only 1 H6 / 4 H5. Going forward this is a hard, non-negotiable gate (set 2026-06-20): **(1)** Before writing or changing ANY page, you MUST FIRST present the page's **complete H1→H6 outline** — every heading, in render order, labeled by level — and get explicit approval. No page code is touched until the outline is approved. **(2)** Headings descend sequentially with **NO skipped levels** (H1→H2→H3→H4→H5→H6; stepping back up to a higher level to start a new section is fine; jumping H3→H6 or H2→H4 is BANNED — this is the axe "Heading elements are not in a sequentially-descending order" error). **(3)** Every page carries **all six levels** with a **minimum of 5 H5 AND 5 H6** (no fewer than 5 of each). **(4)** Semantic level map: **H1**=page topic · **H2**=main search intents · **H3**=subtopics / keyword clusters · **H4**=micro-intent answers / PAA coverage · **H5**=supporting facts / warnings / examples · **H6**=ultra-specific details / breeder notes / citations. Enforced mechanically by `scripts/final_page_audit.py` (`all_six_levels` / `min_h5_5` / `min_h6_5` = hard FAIL) and `docs/reference/seo-rules.md` Rule 52 + Rule 28. A page that violates any of these will NOT be given a pass.
- **CITES Awareness** — African Greys are CITES **Appendix I** (uplisted from Appendix II at CoP17, effective Jan 2017) and IUCN Endangered (Congo) / Vulnerable (Timneh). Never imply illegal/wild-caught trade. All birds are **captive-bred in the USA** with full documentation — captive-bred Appendix-I birds are legal to own and transfer domestically with proper paperwork. (Corrected from "Appendix II" per World Parrot Trust, 2026-05-29 homepage audit.)
- **NEVER publish a visible date on any page (ALWAYS) — applies to every page, agent, and skill** — Freshness signals live **only in schema** (`dateModified` / `datePublished` in JSON-LD), **never as visible text** on the page. No "Updated June 2026", no "Last updated: …", no visible "Posted on …" anywhere in hero, eyebrow, byline, or body. (Decided by the breeder 2026-06-14, reversing an earlier visible-stamp attempt.) The `manual-auditor-check` auditor enforces this via the `no_visible_date` check (a visible date = FAIL). If you think a page needs a human-visible freshness cue, it does not — put the date in schema and stop.
- **src/pages is deployed** — All HTML page edits MUST go to `src/pages/<slug>/index.html` or `src/pages/<slug>/index.astro`. The `site/content/` directory is a staging area; it does NOT get built directly. If both exist, `src/pages/` is authoritative.
- **Always commit + push after build** — After any agent or skill completes a build/edit, commit and `git push` immediately. Push = deploy (GitHub Actions → Cloudflare Pages, auto on push to `main`). Do not leave finished work uncommitted or unpushed. Applies to all agents.
- **Work directly on `main` — NEVER build on feature branches (ALWAYS) — applies to every agent, skill, and build** — All CAG work happens on `main`. Do NOT create or check out feature branches (`git checkout -b …`) for page builds or edits unless the user *explicitly* asks for one. **Only `main` auto-deploys** (Cloudflare Pages builds on push to `main`), so finished work committed on any other branch gets pushed to origin but **never goes live — it strands at HTTP 404** while looking "done." (This happened 2026-06-18: 6 `/available/` bird pages sat live-404 on `feat/bird-listing-pages` until ff-merged to `main`.) The breeder does not want to open PRs or merge anything by hand. Start every task by confirming you're on `main` (`git checkout main`); commit + `git push origin main` after each build = one-step deploy. If you ever find finished work on a non-`main` branch, ff-merge it into `main` and push immediately.
- **Link-First anchors (ALWAYS) — applies to EVERY internal and external link, every agent, skill, and page** — The anchor sits at the **START of the sentence/paragraph** — inside the opening words (first clause). **Never mid-sentence, never at the end.** ✅ "Our [Congo care guide] covers diet in depth…" · ❌ "…diet is covered in our [guide]." (Breeder rule 2026-07-11, superseding the old "beginning or middle, never end" rule everywhere.) Sole exception: branded ACTION anchors on CTAs per `skills/cag-branded-hybrid-keywords.md`. Injected into all 68 agent Golden Rules via `scripts/add_link_first_rule.py` — re-run after adding any agent.
- **Meaningful words, no stop-word filler (ALWAYS) — naming surfaces on every build/rebuild/edit** — URL slugs, anchor text, headings, image filenames, image alt text, meta titles, and labels use meaningful content words only; drop `of/the/and/for/with` fillers where grammar allows. Body prose and the locked conversational question-header pattern are exempt. Canonical spec: `skills/anti-ai-writing.md §Meaningful Words`.
- **Image keyword distribution (ALWAYS — seo-rules Rule 50b)** — The page's PRIMARY keyword goes in the PRIMARY image's alt text only (hero/first content image); every other image rotates a different keyword type (secondary/LSI/NLP variation/long-tail) so the image set covers a diverse spread. No two images on a page share an alt. Applies to photos, AI-generated images, and infographics.
- **Uniform in-body image sizing (ALWAYS — locked 2026-07-12) — applies to comparison + long-form content pages and every image agent/skill** — EVERY in-body section image, **OG photo AND infographic alike, renders in the SAME box as an infographic**: `.sec-img.inf-img` = `max-width:760px; aspect-ratio:1408/768 (16:9); object-fit:cover; height:auto`, **identical on mobile / tablet / desktop**. Do NOT give OG photos the smaller/variable boxes (`.portrait` 420px, `.portrait-tall` 340px, `.photo43` 480px) on these pages — the breeder wants every image the same rectangle down the page, matching the infographic sizing already shipped on CvT/CvM/CvC/MvF. Tune **`object-position` per OG photo** so the bird isn't cropped out of the 16:9 strip (box size never changes, only the focal point). Ship each `<100 KB WebP + -760.webp` sibling with `srcset`/`sizes` like the infographics. Hero staggered-portrait component keeps its own `.hero-imgs` sizing. **Exact pipeline (2026-07-12): `PIL.ImageOps.fit(src,(1408,768),LANCZOS,centering=per-image)` → WebP `method=6`, quality-walk 82↓ until <95 KB → `-760.webp` sibling; a low-res OG master is upscaled to the box on purpose (uniform sizing beats pixel-peeping — breeder's call).** Canonical spec: `IMAGE-DESIGNS.md §1a`. Differentiate sibling pages so they don't look identical with `skills/cag-component-refresh` (the "Refresh Agent" — layout/accent/motif deltas, never a palette change).
- **Recommend + Why (ALWAYS) — applies to every agent, skill, and task** — Whenever you present the user options or choices (meta variants, keyword swaps, design directions, components, A/B picks, section placements — anything), you MUST: (1) mark exactly one option **(Recommended)**; (2) explain WHY, grounded in real data (GSC, competitors, the codebase) — never "feelings" or vague preference; (3) stay honest by naming the trade-off/downside of the recommended pick too. In `AskUserQuestion`, put the recommended option first and append "(Recommended)" to its label. Output that lists options without a reasoned recommendation is incomplete.
- **Shipping cost on every card + shipping section (ALWAYS) — applies to every card/section builder** — Any bird/listing card MUST display shipping cost directly (canonical line under the trust badges: `Ships nationwide · $185 airport · $350 home`), and every shipping section MUST show the two delivery tiers (**Airport Pickup $185** · **Home Delivery $350**, IATA LAR, Delta/United/American). Figures live in `data/financial-entities.json` (`delivery_options`) + `data/price-matrix.json` — read them, never hardcode a different number. Never ship a card without the cost line.
- **Entity 4-Move Loop is the required section-build method (ALWAYS)** — When building or improving ANY page section, run the loop: (1) **Structural Critique** → (2) **Recommended Entities + WHY** (grounded: KG authority / PAA demand / competitor gap / buyer intent) → (3) **Optimized Draft** (verified facts only) → (4) **Topical-Cluster Strategy** (internal links + schema; extend existing JSON-LD, never duplicate; FAQ schema must be visible; verify in `dist/`). The active engine is `@cag-entity-incorporation-agent`; its vocabulary is `skills/cag-entity-agent.md` (a passive catalog, not a builder). Every health/credential entity is bounded by the **Verified-Claim Ledger** in that agent + `sessions/2026-06-03-homepage-entity-map.md` — never assert PBFD/PCR/board-cert etc. beyond what the breeder has confirmed.
- **First-Person Brand Voice (ALWAYS) — applies to EVERY section of the homepage and EVERY page site-wide** — Write as the breeder in **first-person plural POV: "we / us / our / here at C.A.Gs."** Our birds, credentials, and process are framed as *ours*, not described from the outside: ✅ "Here at C.A.Gs, **our** Congo and Timneh Greys…", "**we** hand-raise every chick", "**our** PCR DNA-sexing" — ❌ generic third-person like "Both make exceptional companions" or "African Greys are…" when the sentence is about *our* offering. Exceptions (stay neutral/encyclopedic where first-person would be false or awkward): factual species/taxonomy/entity statements (e.g. "*Psittacus erithacus* is native to West & Central Africa"), cited research, and outbound-authority facts. First-person never means overclaiming — it stays CITES-safe and inside the Verified-Claim Ledger. When rewriting or building any section, default to this voice; flag anything still in third-person brand copy.
- **Skills are registered & Skill-invokable (ALWAYS)** — Every `skills/<name>.md` (and `skills/<name>/SKILL.md` dir-skill) is the canonical source, and is mirrored into `.claude/skills/<name>/SKILL.md` by `scripts/register_skills.py` so the **Skill tool / `/<name>`** can load it by `name:`. `skills/` is still the file everything Reads; `.claude/skills/` is generated — never hand-edit it. **After adding, renaming, or deleting any skill, run `python3 scripts/register_skills.py --copy` and commit `.claude/skills/`** (registration loads only at session start — a new skill is invisible until the next session). `scripts/health-sweep.sh` fails if a skill is unregistered or a copy mirror drifts. Cause of the 2026-06-28 "Unknown skill: cag-final-page-pass / cag-blog-post" failures: the 48 skills sat in `skills/` (a folder the loader never scans) and were never registered.

## Site Model
Transactional + informational, modeled after MaltipoosForsale.com (`/Users/apple/Downloads/MFS/`).
- **Transactional:** "african grey parrot for sale [state]" → inquiry form submissions
- **Informational:** care guides, species guides, health, training, comparison pages
- **Two variants:** Congo African Grey (CAG) vs Timneh African Grey (TAG)

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
- `docs/reference/top-pages.md` — traffic baseline (populate after GSC API connected)
- `docs/reference/components.md` — **COMPONENT REGISTRY v2: 24 named components with variants — read before building any page section**
- `docs/reference/page-width.md` — **PAGE WIDTH RULES: Option A 1200px container system, breakpoints, responsive typography scale**
- `docs/reference/secure-credentials.md` — **SECRETS HANDLING: the clipboard method (`$(pbpaste)`) for saving API keys/tokens; git-token rotation runbook; never put a literal secret in a command, file, or chat**
- `docs/design.md` — **MASTER DESIGN SPEC v2: Terracotta Warmth — colors, type, buttons, cards, motion, voice rules**
- `docs/design-system/README.md` — full narrative brand spec with identity, voice, iconography, and motion
- `src/styles/cag-design-system.css` — canonical CSS custom-property tokens (import in non-Tailwind pages)
- `data/competitors.json` — 30-competitor registry (source of truth)
- `data/analytics/` — GSC performance reports (2026-04-28)

## Phase 1 — Competitor Intelligence (Complete ✓)

### Agents
- `.claude/agents/cag-competitor-registry.md` — discovers + registers 30 competitors; run first
- `.claude/agents/cag-competitor-intel.md` — deep multi-metric analysis; single or --all mode
- `.claude/agents/cag-rank-tracker.md` — weekly monitoring; runs every Sunday

All three steps completed — outputs in `docs/research/` and `data/competitors.json`.

## Phase 2 — Full Agent System (Active)

### Model Tiers
All 68 agents run on **Opus 4.8** (`claude-opus-4-8`), with three **effort** tiers (max / high / medium) as the cost lever, driven by `data/agent-registry.json`. Each agent's frontmatter carries `model:`, `effort:`, `dynamic_workflow:`. See `docs/reference/WORKFLOW.md §Model Tier System`. Dynamic Workflow routing is active on the 3 orchestrators (content-architect, structure-architect, batch-rebuilder). To change models/effort site-wide: edit the registry → `python3 scripts/apply_model_tiers.py` → `bash scripts/verify_model_tiers.sh`.

### Skills

#### Framework Reference Skills
- `skills/framework-heading-hierarchy.md` — H1–H6 strategic keyword placement; maps each heading level to a keyword type and user intent; audit checklist + 5 H2 variation rule; African Grey examples throughout
- `skills/framework-aio-geo.md` — AIO + GEO optimization; entity-first writing, declarative statements, FAQPage schema; Featured Snippet capture (4 strategies) + 12-item checklist
- `skills/framework-qab.md` — Question→Answer→Benefit; all FAQ sections + pricing content
- `skills/framework-aida.md` — Attention→Interest→Desire→Action; high-intent commercial pages
- `skills/framework-eeat.md` — Experience/Expertise/Authoritativeness/Trustworthiness; credibility audit + schema
- `skills/framework-bab.md` — Before→After→Bridge; transformation narrative for buyer pain-point pages
- `skills/framework-ebp.md` — Evidence→Benefit→Proof; credibility-first content for trust-building sections
- `skills/framework-pdb.md` — Problem→Diagnosis→Bridge; diagnostic content for scam-recovery + comparison pages
- `skills/framework-pas.md` — Problem→Agitate→Solution; fastest-converting framework for problem-aware readers (behavior/health/scam-fear content); agitation stays inside the Verified-Claim Ledger
- `skills/framework-fab.md` — Features→Advantages→Benefits; spec-translation for listings, pricing rows, shipping tiers, comparison advantage-rows; no naked facts
- `skills/framework-library.md` — long-tail framework catalog (4Ps, AICPBSAWN, QUEST, ACCA, HIPASI, A-FOREST, String of Pearls, VAD, Setup-Stat-Reframe, 4 Ss, 5 Basic Objections + objection block) with the master routing table by page type + reader awareness level, and the EBP disambiguation note (Evidence→Benefit→Proof vs Entity-Benefit-Purpose vs Evidence-Based Practice)

#### SEO & Content Skills
- `skills/cag-seo-master-checklist.md` — **MASTER SEO EXECUTION GUIDE (v2.0): 4-phase workflow — Phase 1: Pre-Build Research (competitor analysis, keyword fan-out, 150+ entity research) → Phase 2: Planning Gate (Rule 51 outline approval) → Phase 3: Build (section-by-section writing with 5-tier form, 50+ internal links, 50+ external links) → Phase 4: Optimization + QA (meta 4-tone system, schema, voice search, 15-point QA checklist); applies to all pages EXCEPT location pages and comparison pages; includes homepage keyword strategy ("African Grey Parrot Breeder" primary + multi-cluster), Internal Linking Library (Appendix A), example execution, and full term conversion table (dog→CAG); invoke via Skill tool BEFORE starting any page build**
- `skills/cag-blog-post.md` — THE blog-post builder skill (9 posts + `/blog/` hub); reconciled to DESIGN.md; 14-step section architecture, desktop+mobile component map, 8 `cag-blog-*` special-element components, tiered Sprint 0.5 research + enhanced ChatGPT-format output, Style-2 gated humor, 1,800–2,500 intent-scaled. Source of truth: `docs/superpowers/specs/2026-06-27-cags-blog-cluster-system-design.md`.
- `skills/grill-me.md` — Sprint 0.5 session starter; reads gap matrix + top-pages + last brief before asking 13–14 questions; outputs SESSION CONTEXT with framework choice, AIO/GEO approach, and visual plan; run AFTER Sprint 0 intelligence is complete; handoff: grill-me → `@cag-content-audit-agent` → **Section Map + Component Gate** → build
- `skills/cag-branded-search-skill.md` — branded query optimization; /why-choose-cag/ + /african-grey-reviews/ page specs; ReviewAggregateSchema; counter snippets; Contextual Intelligence for local SEO; CITES framing in all branded content
- `skills/cag-branded-hybrid-keywords.md` — **in-content** branded + hybrid keyword INSERTION playbook (distinct from the page-creation skill above): 3 layers — (1) branded-search targets ("C.A.Gs reviews/pricing/vs"), (2) Contextual-Intelligence local intent, (3) branded/action anchors on CTAs; density + CITES-safety rules; section-by-section, approval-gated; run after a page is built or when branded impressions are high but copy has no branded-search targets
- `skills/keyword-cluster.md` — groups keywords into primary/secondary/LSI/long-tail/PAA tiers
- `skills/anti-ai-writing.md` — proactive anti-AI phrase/rhythm blacklist + human alternatives; read when writing/editing any CAG prose; stacks with First-Person Voice + non-commodity agent; built from a RED baseline (`sessions/2026-06-17-anti-ai-baseline.md`)
- `skills/internal-link-agent.md` — sitemap-driven internal-link strategy (Step 0 sitemap inventory is mandatory), orphan page finder, hub→spoke gap audit, **Anchor Diversity Ledger** (no repeated anchors site-wide per target; exact→partial→LSI→natural rotation), Link-First placement
- `skills/cag-for-sale-page-builder.md` — **THE transactional for-sale/buy page builder** (22-page cluster: 17 for-sale + 5 buy-prefixed, all LIVE — REBUILD mode). Merges the MFS on-page formula (keyword distribution 85–105, EFBP openings under every header, conversational headers, 8 counter snippets, entity-variety anti-stuffing rule) with the comparison pipeline (Sprint 0 research protocol, dup-gate, uniform `.sec-img.inf-img` boxes, final-page-pass) under a TRANSACTIONAL profile: bird cards + prices near the fold, Product/Offer schema (sold≠InStock), reserve CTAs every 500–700 words, contact form listing real birds+prices + "Pickup in Midland, TX (within 2–3 hours)" option, honest scarcity only. Egg page = truth-forward hybrid (never literal egg sales). No page-level sidebar. Program plan: `docs/superpowers/plans/2026-07-19-for-sale-pages-program.md`.
- `skills/cag-comparison-page-builder.md` — **THE comparison-page builder** (22–25-section blueprint, per-page research protocol, Hero A/B/C variants, pass-gate list); covers the 8-page cluster (hub + 7 spokes, all LIVE — default mode is REBUILD/POLISH, confirm on-disk slug first); source of truth for comparison structure
- `skills/reddit-strategy.md` — **Reddit-modifier SEO playbook**: compact 100–400-word pages targeting `<keyword> reddit` queries (slug/title = exact modified keyword), real-thread quotes only (Reddit blocks curl/Firecrawl — headless browser), cornerstoning ladder easy→hard→money pages, `/african-grey-reddit/` hub LAST, ethical thread curation; grounded in comparison-cluster SERP research (r/parrots ranks pos-1 on our decision queries)
- `skills/section-auditor.md` — section-by-section health scores; preserve vs patch vs rebuild verdict

#### Technical Skills
- `skills/cag-duplicate-content-gate.md` — **cross-page duplication gate (headers/paragraphs/sentences/anchors)** run BEFORE building any sibling page and AGAIN at final pass; drives `scripts/dup_content_audit.py` (12-word body shingles) + its `--headers` mode (exact AND template H1–H6 crossovers, species-normalized); whitelist = mandated-identical elements only (shipping line, doc badges, CITES notice, site-furniture headers); pairwise across the WHOLE sibling set, on `dist/`. RED baseline: the 29-crossover-header purge (2026-07) + 68 macaw↔cockatoo template crossovers found on first `--headers` run (2026-07-11)
- `skills/manual-auditor-check.md` — **FINAL QA GATE before you "give a page a pass"/deploy.** Runs the mechanical 29-check auditor `scripts/interior_29_audit.py` over `dist/` (headings, schema, meta, image SEO, a11y traps, links, phone, compliance copy) + a **copy-paste manual checklist** for the 6 subjective items (voice, humor, Flesch, non-commodity, tone, brand-protocol). Bakes in the 4 false-positive traps (nested/list `@type`, header-logo-not-hero, authority-phone, strip inline JSON-LD) so it never fabricates defects. Runs as the LAST step of Sprint 4. Companion to `MANUAL INTERIOR-PAGE CHECKLIST.md` Part N. Excludes comparison/location/for-sale/blog.
- `skills/cag-final-page-pass.md` — **THE final "give-it-a-pass" gate for EVERY page type** (supersedes `manual-auditor-check`, which was interior-only). Page-type profiles (bird `/available/`, for-sale, interior, location, comparison, blog) drive a mechanical auditor (`scripts/final_page_audit.py`, nested-slug aware) → one PASS/PASS-WITH-WARNINGS/FAIL verdict; routes low scorers to `cags-comprehensive-page-audit-system` + the subjective checklist. Bird gates: single Product/Offer, sold≠InStock, shipping line, 700–1,000 words, newsletter-exempt, house-method WARN. (PBFD claim gate retired 2026-06-20 — PBFD/APV PCR screening confirmed + in the Verified-Claim Ledger.)
- `skills/cag-bird-listing-page.md` — **the per-bird LISTING-PAGE builder** for individual available birds at `/available/<slug>/` (one page per real bird in `data/clutch-inventory.json`). Lean profile covering the 6 things a bird page gets wrong that CLAUDE.md doesn't already catch: fixed 9-section order, **single `Product`+`Offer`** (never `AggregateOffer` — that's the variant page), link-out-don't-reteach, sell-and-retire lifecycle (sold→301, never leave `InStock`), real-image requirement, and health-claims-from-the-Verified-Claim-Ledger (which now **includes PBFD/Polyomavirus PCR screening** — per-bird testing confirmed by breeder 2026-06-20). 700–1,000 words, real photos, first-person. Distinct from `cag-bird-personality` (card + archetype) and `cag-clutch-manager` (status). RED→GREEN tested (`sessions/2026-06-18-bird-listing-baseline.md`); built the 9-slug `/available/` cluster.
- `skills/cags-comprehensive-page-audit-system.md` — **brutal 17-section strategic page audit (SEO + Semantic + AEO + Entity + UX + CRO + Visual + Backlink) run as a skill chain** over existing CAG specialists + 5 owned scorers (AEO/entity/visual/backlink/verdict). Any page type, any time. Sources color from DESIGN.md/IMAGE-DESIGNS.md, never fabricates competitor metrics (un-fetchable = `NOT FETCHED`, never invented), keeps date recs schema-only. Distinct from `cag-content-audit-agent` (pre-build) and `manual-auditor-check` (final mechanical gate, interior-only). Has a batch mode → audit backlog → feeds `cag-strategy-synthesizer`. RED→GREEN tested (`sessions/2026-06-17-audit-baseline.md`).
- `skills/cag-website-health.md` — technical audit: broken images, canonicals, www redirect, Core Web Vitals, Page Speed Audit (LCP <2.5s, CLS <0.1, INP <200ms)
- `skills/cag-footer-agent.md` — 5-column footer structure spec + audit rules; USDA AWA + CITES notice in bottom bar
- `skills/sitemap-agent.md` — manages sitemap files after any page change
- `skills/cag-image-generation.md` — multi-provider AI image generation: OpenAI DALL-E 3 · **Nano Banana 2 / Google Imagen** (`nanobanna` flag, key in `.google-key` as `GEMINI_API_KEY`, script: `scripts/generate_nb_image.sh`) · Anthropic Claude prompt-refine · **Claude Code HTML** (native HTML/CSS, no API) · **Higgsfield MCP** (`higgsfield` flag, MCP UUID `dd46f66a-ceb9-4042-b533-7b3fc3409318`, tools: `generate_image` / `generate_video` / `show_characters`; say "use Higgsfield" to invoke; reads `data/parrot-image-schema.json`; supports reference image via `media_upload` → `generate_image`) · Pro-grade 9:16 prompt template (1200×2133px → scales to 350px CSS) · WebP optimization · CITES safety rule; hands off to cag-image-pipeline
- `skills/cag-logo-generator.md` — circular emblem logo spec for CongoAfricanGreys.com; African Grey parrot head centerpiece; top arc: "CongoAfricanGreys.com"; bottom arc: "Captive-Bred African Grey Breeders"; deep green/teal palette; DALL-E prompt + responsive HTML implementation
- `skills/cag-infographic.md` — infographic system: **5 types** — Comparison / Feature Grid / Process Flow / **AI-Generated Image** (Type 4, Nano Banana 2 or OpenAI, 9:16 1200×2133px, responsive CSS) / **Higgsfield MCP** (Type 5, character-consistent / video / marketing studio; say "use Higgsfield"); **400px desktop fixed** HTML types; mode selection: "use Claude Code" = HTML, "use Nano Banana" = AI image, "use Higgsfield" = Higgsfield MCP
- `skills/cag-photo-ingest.md` — User-uploaded OG photo → AI generation pipeline; Phase 1: CITES safety check + bird ID; Phase 2: routes to Higgsfield reference image (`soul_2`), Nano Banana lifestyle edit, or HTML/CSS infographic; `media_upload` → `media_confirm` → `generate_image` with reference; CITES safety enforced on every prompt; output → `@cag-image-pipeline`
- `skills/cag-site-patterns.md` — 4 confirmed site fix patterns: gold→clay color, Pagefind search, header layout, birds listing; full code references
- `skills/cag-direction-d-theme.md` — **DIRECTION D "MODERN EDITORIAL" — THE LIVE SITE-WIDE THEME (default on every page):** Newsreader serif headings + IBM Plex Sans body, lead-line paragraphs, clay-tick eyebrows, soft-warm `<article>` cards, calm button motion. Lives in `src/styles/direction-d.css` + `body.theme-d` (BaseLayout). **It is already global — agents must NOT re-implement it per page**; build normal design-system markup and it applies automatically. Homepage-only structural dividers/compact-padding stay scoped to `.home-d` in `src/pages/index.astro`. Read before building or restyling any page.

### Agents

#### Tier 1 — Orchestrators
- `.claude/agents/cag-content-architect.md` — orchestrates all content creation; selects AIDA/PAS/QAB/BAB/H-S-S framework per page type; routes tasks to specialist agents; reads top-pages.md first
- `.claude/agents/cag-structure-architect.md` — maps content clusters into Silo/Reverse Silo; generates `data/structure.json`; ensures every page ≤3 clicks from homepage; scans competitor URLs via Playwright
- `.claude/agents/cag-batch-rebuilder.md` — coordinates batch page rebuilds in parallel (`CLAUDE_CODE_FORK_SUBAGENT=1`); reads `data/locations.json` for location batches; tracks completion + runs final deploy
- `.claude/agents/cag-strategy-synthesizer.md` — research → TWO reverse-engineered strategies → recommend ONE with data-grounded WHY + named trade-off → derives concrete artifacts (e.g. the 9 blog topics + hub). Reads research only (no Sprint-0 re-run), never fabricates; hands chosen strategy to cag-content-architect. Runs at Sprint 1, before content-architect.

#### Tier 2 — Page Builders
- `.claude/agents/cag-seo-content-writer.md` — writes body copy; 5 humor modes; Negative Keyword Counter-Positioning (wild-caught, scam, cheap); Generic-Slayer Filter; DO/DON'T guidelines; Counter Snippets
- `.claude/agents/cag-bird-personality.md` — CLEO/REX/NOVA/SAGE/IRIS buyer archetype profiles; Bird Vitals Card HTML template; documentation block required on every profile
- `.claude/agents/cag-faq-agent.md` — QAB FAQ sections + FAQPage JSON-LD; 7 distribution strategies; GSC Queries + PAA sourcing
- `.claude/agents/cag-homepage-builder.md` — rebuilds homepage section-by-section; 28 clicks / 14,915 impressions / position 45.6 (highest GSC traffic page)
- `.claude/agents/cag-location-builder.md` — builds state location pages; Florida = 22-section / 4,500+ word reference template; supports fork-parallel execution
- `.claude/agents/cag-section-builder.md` — builds individual HTML sections using CAG design system; section types: hero, features, faq, cta, testimonials, comparison-table, price-card; called by all page builders
- `.claude/agents/cag-purchase-guide.md` — rebuilds `/buy-african-grey-parrot-near-me/`; high-intent buyer page covering CITES, IATA shipping, post-arrival support
- `.claude/agents/cag-species-guide-builder.md` — builds species guide pages using Entity-Tree framework; reads `data/price-matrix.json`; AIO/citation optimized
- `.claude/agents/cag-variant-specialist.md` — rebuilds the variant pages `/congo-african-grey-for-sale/` + `/timneh-african-grey-for-sale/` **and the 3 attribute/feature pages** `/captive-bred-african-grey-parrot/` (interior-standard) · `/dna-tested-african-grey-for-sale/` · `/hand-raised-african-grey-parrot-for-sale/` (for-sale method); cross-sell comparison table across the cluster (orphan pages assigned 2026-06-06)
- `.claude/agents/cag-timneh-specialist.md` — all Timneh pages; TAG pricing $1,200–$2,500; intelligent CAG/TAG cross-sell
- `.claude/agents/cag-about-builder.md` — rebuilds `/about/`; H-S-S framework; USDA AWA + CITES credentials + breeder story
- `.claude/agents/cag-scam-specialist.md` — rebuilds `/how-to-avoid-african-grey-parrot-scams/` and scam cluster; converts scam-fearful visitors into documented-purchase inquiries
- `.claude/agents/cag-comparison-builder.md` — builds [X] vs [Y] comparison pages; reference: `/male-vs-female-african-grey-parrots-for-sale/`
- `.claude/agents/cag-financial-strategist.md` — rebuilds pricing/cost guide; reads `data/financial-entities.json`; CAG vs TAG cost comparison; 40–60 year lifetime estimate
- `.claude/agents/cag-blog-post-agent.md` — creates commercial, transactional, review, alternative, and comparison blog posts; keyword intent classification
- `.claude/agents/cag-hub-builder.md` — builds aggregator hub pages: comparison hub, species hub, location hub (`/african-grey-parrots-for-sale/`), documentation hub
- `.claude/agents/cag-infographic-builder.md` — builds infographics; **Mode selection**: "use Claude Code/HTML" = HTML/CSS (3 types, **400px desktop fixed**), "use Nano Banana/OpenAI" = AI image (Type 4, 9:16, script: generate_nb_image.sh), **"use Higgsfield"** = Higgsfield MCP (Type 5, UUID `dd46f66a`, `nano_banana_pro`/`soul_2`/`cinematic_studio_2_5`, reads `data/parrot-image-schema.json`); works for Astro + static HTML pages
- `.claude/agents/cag-interactive-component.md` — builds interactive HTML components: first-year cost calculators, variant fit quizzes, CITES checklists, shipping estimators; pure HTML/CSS/vanilla JS

#### Tier 3 — Content Intelligence
- `.claude/agents/cag-entity-incorporation-agent.md` — **the ACTIVE entity-SEO engine**: runs the 4-Move Loop (Structural Critique → Recommended Entities + WHY → Optimized Draft → Topical-Cluster Strategy) on any section; consumes `skills/cag-entity-agent.md` (passive catalog) as vocabulary; bounded by the Verified-Claim Ledger; emits + verifies schema in `dist/`. Use whenever building/improving a section "with entities." (Distinct from the catalog skill, which is a glossary, not a builder.)
- `.claude/agents/cag-non-commodity-content-agent.md` — Triad model (Archaeologist/Provocateur/Stylist); breeder-authentic content a generic LLM cannot write; Generic-Slayer Filter; High-Resolution Detail per 500 words; CITES framing enforced
- `.claude/agents/cag-content-audit-agent.md` — 4-phase pre-build audit (Intent → Competitor → Action Plan → Internal Linking); PAGE_TYPE includes Species Guide, Variant Page, Scam Recovery, CITES Education, Care Guide; saves to sessions/; run before every page rebuild
- `.claude/agents/cag-keyword-verifier.md` — keyword placement, density, SEO hygiene; 85–105 total keyword distribution targets; UNDER-OPTIMIZED / OVER-STUFFED flags; exact line fixes
- `.claude/agents/cag-image-pipeline.md` — moves images from /content/ into site/, SEO renames, HTML ref updates; WebP Conversion Protocol; lazy loading; staging required
- `.claude/agents/cag-seasonal-content-agent.md` — 12-month content calendar; Spring Bird Season (Mar–May) as major peak; Christmas/Valentine's/Mother's Day/Summer templates adapted for parrot ownership; weaning caveat: African Greys 12–16 weeks; routes briefs to cag-seo-content-writer, banners to page builders; tracks in data/seasonal-calendar.json
- `.claude/agents/cag-email-newsletter-agent.md` — monthly 4-section newsletter: clutch update (clutch-inventory.json), African Grey tip (12-month rotation: nutrition/enrichment/health/bonding), family spotlight (case-studies.json), seasonal CTA; ≤500 words; never references wild-caught; saves to content/newsletters/
- `.claude/agents/cag-video-seo-agent.md` — YouTube SEO packages: title ≤60 chars, description 700–1000 chars (first 125 = hook), 15–20 tags, chapters, thumbnail brief; VideoObject JSON-LD; 4 playlists (Care Guide / Congo vs Timneh / Buyer's Guide / Talking & Training); African Grey-specific keyword angles
- `.claude/agents/cag-social-strategist.md` — orchestrates non-YouTube social (Instagram, Facebook, Pinterest, TikTok); 1 source asset → platform-native posts; reads `skills/social-content.md` (its vocabulary/playbook) + data files; tracks competitor social in `competitors.json`; brand-entity consistency (white-hat, no stack links/indexers); never auto-posts; YouTube stays with cag-video-seo-agent
- `.claude/agents/cag-angle-agent.md` — generates 5–10 content angles, hooks, counter-intuitive POVs before any writing; fear-based hooks + story-first openings
- `.claude/agents/cag-paa-agent.md` — extracts real PAA questions via Playwright; formats for Featured Snippet capture; feeds to cag-faq-agent
- `.claude/agents/cag-meta-description-agent.md` — manages title tags + meta descriptions; audits for duplicates, missing tags, keyword gaps; reads price-matrix.json
- `.claude/agents/cag-external-link-agent.md` — manages outbound links using `docs/reference/external-link-library.md`; inserts links at the START of sentences (Link-First rule) — never mid-sentence or end
- `.claude/agents/cag-framework-agent.md` — deep-dives competitor pages; extracts gaps + content differentiation blueprint; outputs via Playwright

#### Tier 4 — Technical
- `.claude/agents/cag-accessibility-fixer.md` — full WCAG 2.1 AA audit: skip links, ARIA landmarks, form labels, alt text, focus states, color contrast, heading order, button types; Critical/High/Medium priority tiers; batch mode saving to sessions/; Lighthouse verification
- `.claude/agents/cag-performance-monitor-agent.md` — Lighthouse CLI audits; thresholds: LCP <2.5s, CLS <0.1, FCP <1.8s, TBT <200ms, Perf Score ≥90; audit list: homepage + 5 top pages; PageSpeed Insights API fallback; saves to sessions/YYYY-MM-DD-perf-report.md; run monthly
- `.claude/agents/cag-canonical-fixer.md` — converts relative canonicals to absolute URLs on every static export; also fixes og:url + JSON-LD url fields; run before every deploy
- `.claude/agents/cag-footer-standardizer.md` — standardizes `cag-footer-v1` across all pages in `site/content/`; single + batch mode; detects outdated WordPress/Astra markup
- `.claude/agents/cag-performance-fixer.md` — applies Lighthouse Performance fixes; targets 100% Performance score; fixes render-blocking CSS, jQuery defer, font-display swap, LCP fetchpriority
- `.claude/agents/cag-redirect-manager.md` — manages `site/content/_redirects`; flattens redirect chains (A→B→C to A→C); validates targets exist on disk
- `.claude/agents/cag-deploy-verifier.md` — post-deploy verification: 200 checks, canonical audit, IndexNow submission; saves deploy report to sessions/
- `.claude/agents/cag-google-map-agent.md` — adds/replaces Google Maps embeds; fixes CSP object-src blocker (embed→iframe); generates styled map sections using CAG design system
- `.claude/agents/cag-contact-form-updater.md` — audits + standardizes all contact/inquiry forms; detects missing ARIA labels, accessibility violations
- `.claude/agents/cag-agent-system-qa.md` — quality review of full agent system; audits for Golden Rule, required sections, data file references, CLAUDE.md registration
- `.claude/agents/cag-site-hygiene-agent.md` — monthly technical SEO maintenance: (1) page cannibalization audit + 301 redirects, (2) breadcrumb audit + fix (adds Breadcrumb component + BreadcrumbList schema to pages missing it), (3) footer link management (5-column Footer.astro), (4) GA4 health check (tag G-MEWJ9GVC4T in BaseLayout + generate_lead event on /contact-us/); run monthly or after any batch page build

#### Tier 5 — Trust & Authority
- `.claude/agents/cag-trust-signals-agent.md` — Google Reviews widget HTML, Trust Badge row (USDA AWA / CITES / DNA Sexed / Avian Vet), ReviewAggregateSchema, Counter Snippet blocks; /why-choose-cag/ page spec; Contextual Intelligence review templates; works with case-study agent
- `.claude/agents/cag-case-study-agent.md` — manages case studies; scans HTML, writes `data/case-studies.json`; builds `/case-studies/` hub; never fabricates outcomes
- `.claude/agents/cag-conversion-tracker.md` — audits pages for CTA placement, form friction, trust signal placement, CITES clarity, social proof; reads top-pages.md
- `.claude/agents/cag-ab-test-agent.md` — creates A/B variant HTML files for CTAs + hero sections; tracks hypothesis + metrics; never auto-deploys — requires explicit approval

#### Tier 6 — SEO & Analytics
- `cag-competitor-registry`, `cag-competitor-intel`, `cag-rank-tracker` — see Phase 1 above for descriptions
- `.claude/agents/cag-gsc-analytics.md` — analyzes GSC CSV exports from `data/analytics/`; updates `docs/reference/top-pages.md`; never calls external APIs
- `.claude/agents/cag-llm-keyword-intel.md` — queries ChatGPT/Claude/Gemini/Perplexity/AIO for keyword clusters; routes gaps to keyword-verifier + faq-agent; updates top-pages.md with LLM Visibility scores
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
- `.claude/agents/cag-clutch-manager.md` — single source of truth for bird inventory; updates availability in `site/content/available/`; writes `data/clutch-inventory.json`; never deletes sold listings
- `.claude/agents/cag-self-update.md` — self-update agent for CAG system files; run when agents/skills need patching

## Phase 2 Workflow

See `docs/reference/WORKFLOW.md` for the authoritative sprint-based workflow.

### Sprint Order (Quick Reference)
1. **Sprint 0** — Intelligence: `competitor-registry` → `competitor-intel --all` → `gsc-analytics` → `llm-keyword-intel`
1.5. **Sprint 0.5** — Session Orientation: `grill-me` skill (after Sprint 0 Gate passes — needs gap matrix + top-pages)
2. **Sprint 1** — Architecture: `strategy-synthesizer` (2 strategies → recommend 1) → `structure-architect` → `competitive-keyword-gap` → `hub-builder` → `content-architect`
3. **Sprint 2** — Content: `content-audit` → **Section Map + Component Gate** → `angle-agent` → `paa-agent` → writer → `faq-agent` → `section-builder`
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

### Design System v2 — "Terracotta Warmth" + Direction D "Modern Editorial" (active theme)

Active design system: `docs/design.md` (master reference) + `docs/design-system/README.md` (full narrative spec).
**Active visual theme (site default): Direction D "Modern Editorial"** — `skills/cag-direction-d-theme.md`, implemented in `src/styles/direction-d.css` + `body.theme-d`. It refines Terracotta Warmth (same locked palette + clay pill) with Newsreader serif headings and IBM Plex Sans body, and is inherited by every page through BaseLayout. Do NOT re-implement it per page.

**Non-Negotiable Design Rules — enforced on every page build and rebuild:**
1. **Colors:** Three anchors only — Forest Green `#2D6A4F` (nav/headers), Clay `#e8604c` (all CTAs/buttons), Cream `#faf7f4` (page surface). `--gold` MUST always equal `--clay`. (Direction D does NOT change the palette.)
   - **WCAG AA contrast variants (2026-06-03 — do NOT revert):** `#e8604c` only clears AA as *large* text/fill (3.38:1 white). For accessibility, solid clay **button fills** render `--color-clay-ink #c8472f` (white text 4.78:1, via a global `.bg-clay` rule in `global.css`), and **clay as small readable text** (inline links, eyebrows, form prices) renders `#b04228` (4.5:1+ on light). Brand identity token `--clay #e8604c` is unchanged; it still applies to tints, large display, and clay text **on dark/green** (hero "Trust" accent, dark testimonial chips — kept bright via `.home-d` exceptions). See `DESIGN.md` §Color.
2. **Type:** Direction D is live → **Newsreader** serif for ALL headlines (H1–H6) and **IBM Plex Sans** for ALL body/labels/buttons, applied globally via `body.theme-d`. Keep using the `font-lora`/`font-sora` utility classes in markup — `direction-d.css` restyles them automatically; Lora/Sora remain the token-level fallback. Do not hard-code `font-family` on elements to fight the theme.
3. **Buttons:** Primary CTA = clay pill, `border-radius: 50px`. This is the brand signature. Form submit buttons only use `border-radius: 12px`.
4. **Cards:** 20px radius, 1px `--border`, warm shadow, white surface. Info cards use green header band.
5. **Shadows:** Always warm-tinted `rgba(60,30,10,…)`. Never neutral grey.
6. **Motion:** Max 0.2s transitions. No bounce, no parallax, no auto-playing video.
7. **Icons = line-icon SVGs, NOT emoji** (site-wide sweep 2026-06-03, commit `9ff570f`; full spec in `DESIGN.md §Iconography`). Use inline Feather-style SVGs (`width/height="1em"`, `stroke="currentColor"`) — map + transform in `scripts/emoji_to_icons.py`. The former canonical emoji set (📞 ✉️ 📍 🕐 ✈️ 🚗 ✅) is now line icons (✅ → green `#2D6A4F` check-circle). KEEP only the text glyphs ✔ ✗ ★ (list/rating markers). One per element. Banned: 🎉 🔥 🚀 and any colorful pictograph emoji. **Render rule:** a data-array icon rendered via `{x.icon}` must use `set:html`, then verify `grep -rl "&lt;svg" dist/` is empty. **NEVER put an `<svg>` inside CSS `content:`** — `content` only renders plain text, so `::before{content:'<svg…>'}` dumps the raw markup (or drops it) AND collapses badge spacing when the separator lived in that pseudo-element. Put the inline `<svg>` in the markup instead. Detect: `grep -rn "content: '<svg\|content:\"<svg" src/`. (Fixed on captive-bred / hand-raised / dna-tested trust bars, 2026-06-05.)
   - **African Grey bird icon — NEVER use 🦜** (generic green parrot, NOT an African Grey). Use custom images:
     - Congo African Grey: `<img src="/emoji/cag-congo.png" alt="Congo African Grey" class="cag-emoji" loading="lazy">`
     - Timneh African Grey: `<img src="/emoji/cag-timneh.png" alt="Timneh African Grey" class="cag-emoji" loading="lazy">`
     - Large decorative (100px+): `<img src="/emoji/cag-congo.png" style="width:Xpx;height:Xpx;object-fit:contain;" alt="" loading="lazy">` — match original font-size value
     - Plain text / email / JS string contexts: use `[CAG]` or `[TAG]` as text markers — HTML img not possible in strings
8. **Anti-copy:** NEVER add `user-select: none` CSS or JS.
9. **Infographic widths:** `760px` wrapper for species guides / blogs / care pages; `1100px` wrapper for homepage / location pages / hero sections. Height always `400px` fixed on desktop, `auto` on mobile. Never use `900px` or `max-w-4xl` — those are legacy values. See `docs/reference/page-width.md §Infographic Width Rules`.

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

**Infographic widths (confirmed defaults — applies to all `@cag-infographic-builder` output):**

| Page type | Wrapper max-width | Desktop height |
|---|---|---|
| Species guide, blog, care guide, article | **760px** | 400px fixed |
| Homepage, location pages, hero sections | **1100px** | 400px fixed |
| Mobile (≤767px for 1100px; ≤640px for 760px) | 100% width | auto (stacks) |

Full spec: `docs/reference/page-width.md §Infographic Width Rules`

---

## Scripts
- `scripts/health-sweep.sh` — **FULL SYSTEM HEALTH CHECK** (one command). Covers git/deploy state (incl. secret-leak detection), agent integrity (68 agents + model tiers), Astro build, live-site 200s, and `dist/` output hygiene. Run for any "is the site/system healthy?" request. `--no-build` skips the build. Owned/documented by the `cag-website-health` skill.
- `scripts/apply_model_tiers.py` + `scripts/verify_model_tiers.sh` — apply/verify the model + effort-tier assignment (all Opus 4.8; max/high/medium effort) from `data/agent-registry.json`
- `scripts/generate_nb_image.sh` — Nano Banana 2 / Imagen image generation (reads `GEMINI_API_KEY` from gitignored `.google-key`)
- `scripts/generate_sitemaps.py` — regenerates all sitemap shards from `src/pages/` (location/blog/page classification, priority tiers, validates zero phantom URLs). RUN AFTER ADDING/REMOVING ANY PAGE. (Replaced the stale 13-URL hand-maintained sitemap with a 100-URL filesystem-driven one — 2026-06-04.)
- `scripts/final_page_audit.py` — page-type-aware final QA auditor (nested-slug aware; profiles for bird/interior/for-sale/etc.); supersedes `interior_29_audit.py`. Run `python3 scripts/final_page_audit.py --birds` for the `/available/` cluster. Owned by the `cag-final-page-pass` skill.
- `scripts/add_first_person_golden_rule.py` — one-off idempotent injection of the First-Person Voice rule into every agent's `## Golden Rule` (applied to all 66, 2026-06-04).
- `scripts/add_clarification_checkpoint_rule.py` — idempotent injection of the **Clarification Checkpoint** rule into every agent's `## Golden Rule` (applied to all 66, 2026-06-05). Upgrades the <97% Confidence-Gate dead-stop to ask-one-question-log-to-brief-and-continue. Re-run after adding any new agent.
- `scripts/add_link_first_rule.py` — idempotent injection of the **Link-First** rule (anchors at sentence START — never mid or end) into every agent's `## Golden Rule` (applied to all 68, 2026-07-11). Re-run after adding any new agent.
- `scripts/dup_content_audit.py` — cross-page duplicate-copy auditor over `dist/`: default mode = word-for-word body runs ≥12 words; `--headers` mode = exact + species-templated H1–H6 crossovers (catches short duplicate headers the shingle check misses). Owned by the `cag-duplicate-content-gate` skill.
- `scripts/add_interior_standard_pointer.py` — idempotent injection of the **Interior-Page Standard** pointer into the 8 interior-page builder agents' `## Golden Rule` (cag-about/purchase-guide/species-guide/scam/financial/faq/section/trust-signals). Points them at `MANUAL INTERIOR-PAGE CHECKLIST.md` + the master skill's Interior-Page Profile (2026-06-06). Re-run after adding a new interior builder.
- TBD — more in Phase 2

## Data Files
- `data/competitors.json` — managed by cag-competitor-registry
- `data/keywords/` — keyword clusters (Phase 2)
- `data/rankings/` — weekly rank snapshots (Phase 2)
- `data/analytics/` — GSC / performance data

---

## Active Session — Homepage REBUILD v2 (2026-05-29 PM)
- v1 build used OLD/inline components + skipped the SEO checklist → full section-by-section rebuild.
- **LOCKED:** Hero B Authority Green · `cag-toc-v3:02` Grouped-by-part · `cag-key-takeaway-v2:02` Stat-forward grid ·
  Compare Table Style E (1100px) · new Mark & Teri owner card · new counter snippet
  (12+ Yrs aviary / 100% CITES / $1,500 Floor price / 24h) · new filterable BirdCard.
- **Content contract:** "C.A.Gs" / "C.A.Gs – Midland, TX" brand voice (never "congoafricangreys.com") ·
  ALL of H1–H6 used · every header conversational/Quora-style (What/How/Is/Can) · EBP framework per paragraph ·
  internal+external links anchored at sentence START — Link-First rule (never mid-sentence or end) · PAA-only FAQs · `assets/brand/` shipping photos ·
  CITES Appendix I + captive-bred-USA · 8–15 top states/cities in shipping.
- **MANDATORY:** `MANUAL SEO CHECKLIST-HOMEPAGE.md` + `skills/cag-seo-master-checklist.md` — not optional.
- **AEO/GEO gate runs ON the page:** keyword-verifier → meta-description → trust-signals.
- Desktop renders new desktop components; mobile/tablet renders new mobile components.
- Governance docs reconciled to v2 (2026-05-29): `components.md`, `component-page-matrix.md`, `component-themes.md`
  now register the new bundles and route the homepage to them.
- Status: **DONE and LIVE** (2026-06-01). Homepage fully built + deployed — `src/pages/index.astro` (989 lines), 24 H2 sections live. Per "Always commit + push after build", all work committed + pushed.
- **Progress: COMPLETE.** All sections built, approved, and live. (The earlier "RESUME AT SECTION 9" note is superseded — homepage was finished after 2026-05-29.)
- Added `--color-panel/line/mid/forest` to `global.css` (fixed undefined cag-library tokens site-wide) + Rule 28b (Two-Keyword Headers) to the SEO checklist.
- **Continuation handoff:** `sessions/2026-05-29-homepage-build-progress.md` (read first next session; do NOT re-run grill-me).
- Session brief: `sessions/2026-05-29-session-brief.md` (see "REBUILD v2" section).
- **2026-06-05 addendum (a11y + non-commodity pass):** homepage a11y back to **100/100** (fixed the Direction-D lead-paragraph dark-on-dark trap + MobileTabBar contrast — see `cag-accessibility-fixer` A11y-7 + MEMORY `reference_contrast_lead_paragraph_trap`). Ran the **non-commodity pass** (audit-all → rewrite-only-weak; homepage was ~90% already strong) — added Teri's First-30-Days voice, **Maxy** (talking Congo in the video), per-bird **ItemList Product/Offer schema**, and newly-confirmed **psittacosis + UV-B/D3** entities. **Verified-Claim Ledger expanded** (psittacosis, UV-B/D3, Maxy → ✅) in `cag-entity-incorporation-agent.md` + `sessions/2026-06-03-homepage-entity-map.md`. External-link skill+agent now warn that **cites.org 403s to curl = bot-block, not dead**. Details: `sessions/2026-06-05-homepage-noncommodity-pass.md`.

## Active Session — Interior-Pages Batch (2026-06-06 → 2026-06-11) — COMPLETE ✓
- **All 18 interior pages rebuilt to the Interior-Page Standard and LIVE** (plan: `docs/superpowers/plans/2026-06-06-interior-pages-full-seo.md`; brief: `sessions/2026-06-06-interior-batch-brief.md`).
  - **Cluster A (Care/Health, 6):** care-guide pillar · african-grey-care hub · diet · best-food · lifespan · african-grey-parrot-health-guarantee
  - **Cluster B (Trust/Authority, 5):** trusted-african-grey-parrot-breeders (= the About Us page, AboutPage schema) · african-grey-reviews (5 fabricated testimonials + fake reviewCount:47 removed) · captive-bred · cites-african-grey-documentation · scams (`yr is not defined` bug fixed)
  - **Cluster C (Guides, 4):** african-grey-parrot-guide (species pillar) · african-grey-parrot-faq (25-Q QAB pillar) · how-to-tame (HowTo schema, 7 steps) · african-grey-adoption (honest breeder-not-rescue frame; legacy `/african-grey-for-adoption/` 301 live)
  - **Cluster D (1):** african-grey-parrot-price (AggregateOffer + 6 per-bird Offers; every figure traced to price-matrix/financial-entities)
  - **Cluster E (2):** contact-us (ContactPage schema + GA4 `generate_lead` inline) · privacy-policy (shell only, legal text verbatim)
- Finalize done: sitemaps regenerated (100 URLs, 0 phantoms), health sweep PASS, all 18 slugs live-verified 200, IndexNow submission accepted (200).
- **Open Flags RESOLVED by breeder (2026-06-11):** ① pellet endorsement = the 3–5 reviewed brands (Harrison's / Roudybush / TOP's / Zupreem Natural), no single house brand · ② AggregateRating **reviewCount = 52 (real)** — corrected from 127 site-wide (homepage ×3, reviews, trusted-breeders); rating 4.9 unchanged · ③ privacy-policy "Zelle or Cash App" removed → neutral "payment method confirmed during reservation" wording.

## Known Issues
- Homepage Video section: using a YouTube **placeholder** (embed + VideoObject schema scaffold) — breeder to supply the real URL later.
- Homepage `.mov` clip not browser-usable (ffmpeg/cwebp not installed to convert → mp4).
- GSC not connected → `docs/reference/top-pages.md` has no live clicks/impressions/LLM Visibility yet.
- MFS deploy may be broken — the shared "MFS Dashboard" GitHub PAT was deleted during CAG token rotation (2026-06-01). Run `git push --dry-run` in the MFS repo before next MFS work; it needs its own token. (CAG uses the new "CAGs-Website Workflow" PAT in keychain; remote is tokenless.)

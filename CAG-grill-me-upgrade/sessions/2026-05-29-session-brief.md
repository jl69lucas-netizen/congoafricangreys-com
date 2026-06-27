# Session Brief — 2026-05-29

## Business Focus
Rebuild the **homepage (`/`)** — the highest-traffic page (28 clicks / 14,915 impressions / position 45.6) — as a long-form **pillar page** on the **new desktop + mobile component library**, to win "African Grey Parrot Breeder" + multi-cluster and convert visitors into inquiry-form submissions. This is the homepage **SEO content build** (the visual/asset pass from 2026-05-28 is now superseded — see Design below).

## SESSION CONTEXT
- **Page Type:** Homepage (money page + top-level pillar/hub)
- **Target Keyword:** `African Grey Parrot Breeder` (+ multi-cluster — finalized in checklist Phase 1)
- **Framework:** Mixed — H-S-S (About/breeder), AIDA (commercial/products), Entity-Tree (History/Health/species), QAB (FAQs). `@cag-content-architect` confirms per-section.
- **Audit Status:** pending → **run `@cag-content-audit-agent` first** (user decision)
- **LLM Visibility:** not measured → run `@cag-llm-keyword-intel` before publish
- **Structure.json Entry:** yes — `/`, P0, schema = Organization + FAQPage + BreadcrumbList
- **Hub Page:** the homepage IS the top hub (links to location hub, Congo/Timneh variants, available birds, contact)
- **Internal Links Needed:** TBD after audit (Appendix A canonical URLs)

## Today's Target
- **Page:** `/`
- **Goal / "done":** preview-ready pillar homepage with ALL mandatory sections + content written, verified section-by-section in `localhost:4321`. **NOT published** — preview + approval only.
- **Reader:** prospective African Grey buyer. Ranked fears: scam/fraud → CITES/legal → wild-caught suspicion → sick bird (PBFD) → post-sale abandonment → cost uncertainty.
- **Benchmark:** none given — content-audit picks the top competitor breeder homepage to model + beat.
- **Design:** **FULL REBUILD on the new desktop + mobile component library.** The new components ARE the new visual layer. Desktop renders new desktop components; mobile/tablet renders new mobile components. Delivery mechanism: I inspect how the component-library HTML files are authored and replicate that pattern — confirm with user before building.

## Build Decisions (locked this session)
- **Scope:** full pillar homepage — all mandatory sections ON the homepage.
- **Mandatory sections:** Hero · KeyTakeaway · TOC · About the Breeder · All Products (filterable) · Why Choose CAG · Contact Form · Map · Shipping · Comparison · Case Study · Tables · Tools · Congo section · Timneh section · African Grey History · Health · CAGs-vs-other-breeders · Video.
- **Special inserts:** Newsletter + Review inserts (I propose optimal spots — likely ~2 newsletter + 3 review) · section-specific short FAQs on sections I determine need them (proposed at outline gate).
- **Responsive:** desktop components for desktop, mobile components for mobile/tablet — mechanism matched to the library, confirmed before build.
- **Tools section:** First-year cost calculator + CITES/documentation checklist + Shipping timeline estimator. (No variant fit quiz.)
- **New-section art:** MIX — HTML/CSS infographics + reuse of existing `assets/brand/` photos. **No new AI image spend.**
- **Product filters (All Products card):** Variant (Congo/Timneh) · Product type · Availability · Price range.
- **Comparison section:** African Grey **vs other species** (Macaw/Cockatoo/Amazon). [Separate from CAGs-vs-other-breeders trust table.]
- **Video section:** YouTube **placeholder** (embed + VideoObject schema scaffold) for now — breeder supplies the real URL later; drop-in, no structural change.
- **Depth:** word target set by content-audit competitor analysis.
- **Contact policy (Rule 61):** phone **402-696-0317** in footer + schema ONLY; every in-body CTA links to `/contact-us/`.
- **Prices (source of truth = `data/price-matrix.json`):** egg $95 (buy 5 = free US ship) · breeding pair $3,000 · Jins+Jeni companion pair $3,500 · CAG chick $2,300–$2,500 · CAG adult $1,700 · TAG $1,500–$1,600 · deposit $200.

### Declared defaults (confirm at Phase 2 outline gate)
- **Health section** = trust/reassurance angle (health guarantee, avian-vet certificate, DNA sexing, responsible PBFD/feather handling) — NOT fear-based.
- **Tables section** = pricing table + Congo-vs-Timneh quick-facts table + first-year-cost table.
- **CAGs-vs-other-breeders** = documented/health-guaranteed CAG vs typical/unverified breeder comparison (trust converter).
- **Section order** = presented for approval at the outline gate.

## Constraints
- **Preview-only** — nothing committed/pushed until user explicitly approves going live.
- **≥97% confidence** before any write to `src/pages/index.astro`.
- **CITES-safe** — never imply wild-caught/illegal trade; all birds captive-bred, documented.
- **Data-files-are-truth** — no fabricated prices/stats/outcomes.
- `src/pages/` is authoritative/deployed; `site/content/` is staging only.

## Repeat / Avoid
- **Repeat:** preview-only discipline · DOM-eval/screenshot-verify every section in localhost before claiming done · prices strictly from `price-matrix.json`.
- **Avoid / note:** the 2026-05-28 BirdCard focal-point tweaks may be superseded by the new filterable product card — preserve the learning but don't assume the old card survives the rebuild.

## Urgency
None — quality first. No hard deadline.

## Recommended Next Agent
`@cag-content-audit-agent` →
`TARGET_URL: https://congoafricangreys.com/` · `TARGET_KEYWORD: "African Grey Parrot Breeder"` · `PAGE_TYPE: Homepage`
Then: invoke `skills/cag-seo-master-checklist.md` (Phase 1 research → Phase 2 outline gate) → `@cag-content-architect` → writer / faq-agent / section-builder / interactive-component / infographic-builder.

## What's Next
> ⏭️ **RESUME (REBUILD v2):** Sections 1–8 built & approved on the NEW components (preview-only, nothing pushed). **Resume at Section 9 (Congo).** Full handoff → `sessions/2026-05-29-homepage-build-progress.md`. Next batch: 9–11 (Congo → Timneh → Comparison via `cag-compare-table-e`). Do NOT re-run grill-me — open the build directly per the progress doc.

---
**[Superseded v1 note below]**
**Homepage pillar BUILT + verified (2026-05-29), preview-only — NOT published.**
- `src/pages/index.astro` rebuilt as a 21-section pillar from the cag-library components + 3 interactive tools (cost calculator, CITES checklist, shipping timeline) + filterable product grid. Build clean (98 pages), 0 broken images, 0 console errors.
- Word count: **~4,484 visible** (+ component copy) — up from 2,743; out-depths deepest competitor (anasparrots 3,738).
- CITES corrected to **Appendix I** across homepage components (TrustBar, Footer, FAQ schema, variant cards, history). Stale "Appendix II" in CLAUDE.md fixed.
- Data-integrity fixes: TrustStats "3-year"→"3-day" guarantee + removed fabricated "$185/48 states"; overrode invented component defaults (vet name, lab, family counts); prices aligned to price-matrix.
- Audit saved: `sessions/2026-05-29-homepage-audit.md` (12 competitors, GSC analysis, 100+ keyword fan-out, 152 entities, audience profiles).

**Still pending:**
1. **YouTube URL** → replace the placeholder embed in the Video section (drop-in, no structural change).
2. **Site-wide Appendix II → I sweep** on location pages (chip created — separate worktree).
3. **Publish when approved:** `@cag-canonical-fixer` → `git commit` → `git push` (auto-deploys via Cloudflare) → `@cag-deploy-verifier` → `sitemap-agent`.
4. Optional: Sprint 3 AEO/GEO gate (`@cag-keyword-verifier`, `@cag-meta-description-agent`, `@cag-trust-signals-agent`) before publish.

---

## 🔁 REBUILD v2 — Locked Decisions + Corrections Contract (2026-05-29 PM)

The v1 build used **old/inline components and skipped the SEO checklist**. v2 is a full section-by-section rebuild on the NEW component bundles. Breeder-locked decisions:

### Locked design picks
- **Scope:** FULL section-by-section rebuild of `src/pages/index.astro` (preview-only).
- **Hero:** `Hero B — Authority Green` (from `UNIQUE CAGs NEW COMPONENTS.zip`). Old "Immersive Full-Bleed" hero + photo are RETIRED.
- **TOC:** `cag-toc-v3:02` Grouped by part (`page-components-*.html`).
- **Key Takeaway:** `cag-key-takeaway-v2:02` Stat-forward grid (`page-components-*.html`).
- **Comparison:** `Compare Table Style E · 1100px` (NEW CAG COMPONENTS bundle) — NOT the inline table.
- **Owner card:** NEW Mark & Teri owner card (Components-CAGs bundle) — replaces `MeetTheTeam variant="duo"`.
- **Counter snippet:** NEW design "12+ Years aviary · 100% CITES · $1,500 Floor price · 24h" (CongoAfricanGreys Mobile Components.html).
- **BirdCard:** NEW filterable card + filter pills (UNIQUE CAGs bundle).
- **Responsive:** desktop bundle → desktop; mobile/tablet bundles → mobile/tablet.

### Content corrections contract (apply to EVERY section)
1. **Brand voice:** "C.A.Gs" / "C.A.Gs – Midland, TX" in body — NEVER "congoafricangreys.com".
2. **Section titles:** "Why African Grey Parrot Families Choose C.A.Gs" (not "Why Families Choose Us"); follow branded-keyword rules.
3. **Headers:** use ALL of H1→H6 on the page; every header is conversational/Quora-style (What / How / Is / Can) for voice/AIO.
4. **Opening paragraphs:** conversational; apply an explicit framework per paragraph (EBP, etc.) — no generic openers.
5. **Links:** internal + external woven from the START/MIDDLE of body sentences (never at the end), throughout the body + at end of required sections; link to blogs + care-guide pages naturally (cag-external-link-agent rules).
6. **FAQs:** PAA-sourced questions ONLY (`@cag-paa-agent` → `@cag-faq-agent`).
7. **Shipping section:** use real shipping images from `assets/brand/`; mention 8–15 top states/cities (checklist Phase 3).
8. **CITES:** Appendix I + captive-bred-in-USA, never wild-caught.
9. **AEO/GEO gate is on-page (not optional):** keyword-verifier → meta-description → trust-signals run as part of the build.
10. **Preview:** always render to `localhost:4321`, verify each section before claiming done.
11. **SEO checklist:** `MANUAL SEO CHECKLIST-HOMEPAGE.md` + `skills/cag-seo-master-checklist.md` are MANDATORY, not optional.

### Registry updated
`docs/reference/components.md` now lists `cag-toc-v3` (3 variants) + `cag-key-takeaway-v2` (3 variants) as MODERN; old `toc-v1/v2`, `key-takeaway-v1`, `toc-keytakeaway` flagged LEGACY.

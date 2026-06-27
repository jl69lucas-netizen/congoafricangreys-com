# C.A.Gs Blog Cluster — System Design Spec

**Date:** 2026-06-27
**Status:** Approved (brainstorm) → ready for implementation plan
**Branch:** `main` (all work; never feature branches — only `main` auto-deploys)
**Owner:** breeder (Mark & Teri / C.A.Gs – Midland, TX)

---

## 1. Purpose & Scope

Rebuild the 9 thin stub blog posts (currently ~120–168 lines each) + the `/blog/` hub to the full Direction-D standard already shipped on the homepage and bird pages. This spec defines the **reusable system** — section architecture, component map (desktop + mobile parity), special-element rules, research + output format, agent stack, voice/length, and gates — so every page is built to one consistent, competitor-beating standard.

**Decision (approved): lock the reusable system first**, then execute page-by-page.

### Page inventory (live slugs)
| # | Slug | Folder (.md research) |
|---|---|---|
| hub | `/blog/` | — |
| 1 | `/blog/african-grey-parrot-cage-setup/` | African Grey Cage Setup |
| 2 | `/blog/african-grey-parrot-training/` | African Grey Parrot Training |
| 3 | `/blog/african-grey-parrot-talking-ability/` | African Grey Talking Ability |
| 4 | `/blog/african-grey-parrot-price-what-you-get/` | African Grey Parrot Price |
| 5 | `/blog/best-place-to-buy-african-grey-parrot/` | Best Place to Buy African Grey Parrot |
| 6 | `/blog/african-grey-vs-eclectus/` | African Grey vs Eclectus |
| 7 | `/blog/african-grey-parrot-facts/` | African Grey Parrot Facts |
| 8 | `/blog/african-grey-health-problems/` | African Grey Health Problems |
| 9 | `/blog/is-african-grey-good-for-beginners/` | Is African Grey Good for Beginners |

### Cadence
- **3–4 pages per session.** **Batch 1 (this program's first build):** hub + cage-setup + training + talking-ability. Batch 2: price + best-place-to-buy + vs-eclectus. Batch 3: facts + health-problems + beginners.
- Per page: **tiered research → strategy doc for breeder selection → build ONE page → breeder pass → roll the approved pattern to the rest.**
- Build nothing until the breeder has chosen frameworks/angles/entities/keywords AND given the first built page a pass (same as homepage + bird pages).

### Inputs already on hand (confirmed accessible)
- `assets/CAGs-BLOG-POSTS/<topic>/<topic>.md` — per-page ChatGPT research (Google top-3, keyword universe, entity coverage, H1–H6, PAA, schema, image ideas). Images are embedded as base64 + standalone PNG/JPG in each folder. **Accessible.**
- `assets/CAGs-BLOG-POSTS/BlogPostComponents/*.html` — real, on-brand HTML/CSS components (correct DESIGN.md palette already), desktop + dedicated `Mobile *` variants.
- `assets/CAGs-BLOG-POSTS/CAGs-Blog-Post-Skill.md` — governing skill draft (carries stale ChatGPT contamination to strip).

---

## 2. Section Architecture (one reusable skeleton, all 9 posts)

Color/bucket key: **MANDATORY** (every post) · **SUGGESTED** (our moat — competitors lack) · **COMPETITOR-DATA** (they rank with it) · **[SPECIAL-ELEMENT SLOT]**.

1. **Hero** — MANDATORY. Breeder eyebrow + H1 (primary KW) + dek + hero image/infographic + 1 soft CTA chip. No special module here.
2. **Top lead-capture strip** — MANDATORY. Slim inline capture (matches care/resource-page pattern, commit `ba434ee`). Not the full newsletter.
3. **TOC / jump links** — MANDATORY (long-form).
4. **[SPECIAL-ELEMENT — TOP] Quick-Answer / Key-Takeaway box** — MANDATORY. Snippet + AEO target. **Starts here, right after the TOC — never directly after the Hero** (breeder rule).
5. **Body H2 sections × N** — MANDATORY. Page-specific clusters from each `.md`. Inline diagrams + Mistake-Alert / Expert-Tip callouts woven in.
6. **Comparison / spec table** — COMPETITOR-DATA.
7. **[SPECIAL-ELEMENT — MIDDLE] Mid-article conversion module** — Decision-Tree OR Myth-vs-Fact OR inline available-birds soft-CTA, chosen per page from competitor gaps.
8. **Breeder Note / E-E-A-T block** — SUGGESTED moat. First-person C.A.Gs insight.
9. **"What you get from a real breeder" trust band** — SUGGESTED moat. Buyer-advocate angle that turns an informational topic commercial.
10. **FAQ accordion** — MANDATORY. PAA-sourced. Visible FAQPage JSON-LD.
11. **[SPECIAL-ELEMENT — BOTTOM] Bottom conversion module** — Available-birds card + inquiry CTA (shipping line: `Ships nationwide · $185 airport · $350 home`).
12. **Related blog posts (internal-link cluster)** — MANDATORY (silo).
13. **Newsletter block** — MANDATORY (lives lower; top strip does early capture).
14. **Global CTA band** — MANDATORY. One-CTA-per-page via BaseLayout (`hideGlobalCta` if a section already owns the CTA).

**Special-element module placement rule:** every page carries all three slots (TOP/MIDDLE/BOTTOM). The TOP module always begins **after the TOC**. Which concrete element fills MIDDLE is chosen per page from the competitor-gap analysis.

---

## 3. Component Map — Desktop + Mobile Parity

Provided BlogPostComponents already carry the correct DESIGN.md palette → lift & use. `Type Specimen` + `Mobile Type` are the **type-scale lock** that guarantees identical H1–H6 + body heights across desktop / tablet / mobile (the breeder's explicit parity requirement).

| Section | Desktop component | Mobile component | Status |
|---|---|---|---|
| Hero | `Hero / 3-Split` | `Mobile Hero` | ✓ provided |
| Top lead-capture | Component Library form | `Mobile Inquiry` | ✓ provided |
| TOC / jump links | `Jump Links / 3 contexts` | `Mobile Jump Nav` | ✓ provided |
| Key-Takeaway / Quick-Answer (TOP) | — | — | ✦ new |
| Body article + cards | `Buyer's Guide Article` · `3-Column Grid` | `Mobile Blog` · `Mobile Cards` | ✓ provided |
| Comparison / spec table | — | — | ✦ new |
| Mid-article module (MIDDLE) | — | — | ✦ new |
| Breeder Note / E-E-A-T | — | — | ✦ new |
| FAQ accordion | `FAQ / 3 zones` | `Mobile FAQ` | ✓ provided |
| Bottom conversion module | reuse bird-card | `Mobile Cards` | ✦ adapt |
| Related posts cluster | — | — | ✦ new |
| Newsletter | Component Library | `Mobile Newsletter` | ✓ provided |
| Type scale (all H1–H6 + body) | `Type Specimen` | `Mobile Type` | ✓ locks parity |

### New components to build (greenlit — all 8) — the reusable special-element + moat library
A. **Quick-Answer / Key-Takeaway box** (TOP special-element, AEO snippet capture)
B. **Comparison table with "breeder verdict" row** (Min/Recommended/Ideal + verdict competitors never add)
C. **Breeder Note box** (un-copyable first-person E-E-A-T moat)
D. **Mistake-Alert + Expert-Tip callouts** (line-icon, NOT emoji)
E. **Myth-vs-Fact card**
F. **Decision-Tree block** (AI-extraction friendly; beginners + vs-Eclectus pages)
G. **Related-posts cluster** (silo internal links to other 8 posts + money pages)
H. **Sticky mobile CTA bar** ("See available Greys" on mobile scroll)

All 8 built as reusable Astro components, desktop + mobile, themed via Direction-D (inherited, not re-implemented per page).

---

## 4. Research Method (Sprint 0.5) — Tiered

**Depth (approved): tiered.** Scan all 30 competitors (`data/competitors.json`) once to flag who owns each topic + their gap; deep audit only the 6 leaders per page (3 Google from the `.md` + 3 fresh Bing per primary keyword). Non-leaders get a light pass.

### Per-page strategy doc (the "ChatGPT format" — enhanced)
One doc per page → `sessions/YYYY-MM-DD-blog-strategy-<slug>.md`. Mirrors the breeder's `.md` structure and **adds** the requested fields:
1. Page + primary KW + search-intent split (info/commercial/transactional %)
2. **Content-type verdict** — what competitors write vs our recommended posture
3. Top-3 Google competitors (from `.md`)
4. **Fresh Bing top-3** (live per keyword)
5. **30-competitor registry signal** (who ranks/owns + gap)
6. **Competitor on-page keyword audit table** — per competitor: KW in slug? title? meta? H1? on-page count, variations, entity types, content category
7. Why they rank (reverse-engineered signals)
8. Keyword universe — primary/secondary/LSI, **weighted to 6+ word long-tail + conversational/voice queries**
9. Entity coverage — entities + types + categories for AEO
10. Competitor voice + angle → C.A.Gs winning-angle options
11. Competitor content gaps (our wedge)
12. Full H1–H6 outline (render order, sequential, ≥5 H5 + ≥5 H6)
13. **Section distribution matrix** — per section: A/B/C category (A=core, B=competitor-match, C=our-moat), framework, word-count split, special-element slot
14. Featured-snippet + PAA targets
15. Schema set per page
16. Internal-link + image plan (silo links + provided/AI image → section map)
17. **Framework / angle / keyword OPTIONS for breeder to choose** — each Recommended + why + named trade-off

**The breeder selects** frameworks, angles, entities, keywords, variations. The system presents options + grounded reasons; it does not decide for them.

---

## 5. Agent / Skill Stack (per phase)

- **Research (Sprint 0.5):** `@cag-competitor-intel --all` (30-scan + deep top-3) · `@cag-competitive-keyword-gap-agent` · `@cag-framework-agent` (competitor voice/angle/H1–H6) · `@cag-paa-agent` · Bing via Firecrawl · `grill-me`.
- **Strategy/output:** `@cag-content-audit-agent` · `@cag-angle-agent` · skills `keyword-cluster`, `framework-aio-geo`, `framework-heading-hierarchy`.
- **Build:** `@cag-blog-post-agent` (lead) + `@cag-section-builder` · First-Person voice (baked into every agent's Golden Rule) · `anti-ai-writing` · `@cag-non-commodity-content-agent` (audit-then-rewrite) · `@cag-entity-incorporation-agent` (4-Move Loop + schema) · keyword fan-out (`cag-seo-master-checklist` Phase 1) · `@cag-faq-agent` · `@cag-meta-description-agent` · `@cag-external-link-agent` · `internal-link-agent` · images via `@cag-infographic-builder` + `cag-image-generation` (Nano Banana / Higgsfield).
- **Brand context (read FIRST every session):** `PRODUCT.md` · `DESIGN.md` · `IMAGE-DESIGNS.md`.
- **QA/deploy:** `cag-final-page-pass` + `scripts/final_page_audit.py` · `@cag-accessibility-fixer` · `@cag-performance-fixer` · `@cag-canonical-fixer` · `scripts/generate_sitemaps.py` · `@cag-deploy-verifier`.

---

## 6. Voice, Humor & Length

- **Voice:** First-person plural C.A.Gs ("we / us / our / here at C.A.Gs"). Encyclopedic exceptions for taxonomy/cited research.
- **Humor:** Style-2 dry/transparent, **≤1 beat per section, gated** — used on commercial/comparison/lighter pages (price, vs-Eclectus, beginners, best-place); **ZERO humor on health-problems and any medical/legal/CITES content.**
- **Length:** **1,800–2,500 words, intent-scaled** — comparison/price leaner, care guides (cage/health/training) fuller. Long-tail 6+ word + conversational/voice weighting throughout.
- **Content posture:** transactional / commercial / comparison-led, **AI-overview-resistant** — informational topics angled commercially via breeder moat + buyer-advocate framing + CTAs.

---

## 7. Skill Enhancement

Install + enhance `CAGs-Blog-Post-Skill.md` as a registered project skill (e.g. `skills/cag-blog-post.md`) and **reconcile to DESIGN.md**:
- **Strip stale contamination:** palette `#1F7A4D` green / `#FF6210` orange → `#2D6A4F` / `#e8604c`; fonts Montserrat/Poppins/Inter → Newsreader / IBM Plex Sans; emoji in special-element boxes → line-icons; remove the leftover "VibeTab" block.
- **Fold in everything agreed here:** section architecture, component map (desktop+mobile parity), 8 new components, special-element placement rule, tiered research method + enhanced output format, A/B/C matrix, voice/humor/length, gates.

---

## 8. Baked-in Gates (non-negotiable, every page)

- **Heading Outline Gate** — present full H1→H6 outline + get approval BEFORE any page code; sequential (no skipped levels); all six levels; ≥5 H5 AND ≥5 H6.
- **Line-icons not emoji** (Feather SVG, `currentColor`); keep only ✔ ✗ ★ text glyphs.
- **Shipping line on every card** + two-tier shipping ($185 airport / $350 home) from `data/financial-entities.json`.
- **Schema visible + verified in `dist/`** (not source greps); extend existing JSON-LD, never duplicate.
- **One CTA per page** (BaseLayout global band; `hideGlobalCta` when a section owns it).
- **NEVER a visible date** — freshness in schema only (`dateModified`/`datePublished`).
- **CITES Appendix I / captive-bred-USA** framing; inside the Verified-Claim Ledger.
- **Same font/text/header heights across desktop/tablet/mobile** — enforced by `Type Specimen` + `Mobile Type`.
- **Final gate:** `python3 scripts/final_page_audit.py` (blog profile) → PASS before deploy.
- **Deploy:** commit + `git push origin main` after each build (= deploy) → `generate_sitemaps.py` → `@cag-deploy-verifier`.

---

## 9. Out of Scope (this program)

- Location pages, comparison cluster pages (non-blog), for-sale/variant pages — own builders.
- Real review collection — via `@cag-review-collection-agent`; never fabricate testimonials.
- GSC live data — not connected yet (known issue); research uses competitor + Bing + `.md` signals.

---

## 10. Definition of Done (per page)

1. Strategy doc produced; breeder selected frameworks/angles/entities/keywords.
2. H1→H6 outline approved (gate passed).
3. Page built to the section architecture using provided + 8 new components, desktop + mobile parity.
4. Voice/humor/length/entity/schema rules met; images placed + SEO'd.
5. `final_page_audit.py` PASS; a11y/perf/canonical clean.
6. Breeder pass.
7. Committed + pushed to `main`; sitemaps regenerated; deploy verified.

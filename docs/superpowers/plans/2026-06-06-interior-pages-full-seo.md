# Interior-Page Full-SEO Rebuild Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring 18 interior/secondary pages to the same design + SEO standard as the rebuilt homepage — modern components, entity SEO, AEO/GEO schema, AA accessibility — using refreshed per-page competitor data to set length targets, while resolving 3 cannibalization clusters before building.

**Architecture:** Batch the *research + planning* across all pages first (competitor refresh → cannibalization resolution → per-page section maps), then *build page-by-page grouped into 5 content clusters* with a Confidence Gate + preview-approval per page. Every page follows one canonical Per-Page Build Recipe (Phase 2, steps R1–R12) parameterized by a per-page spec table. Build target is `src/pages/<slug>/index.astro`; verification is against `dist/` and the live URL.

**Tech Stack:** Astro (`npm run build` → `dist/` + Pagefind), Direction-D theme (global, do not re-implement), CAG component library v2 (`cag-hero-v3`, `cag-compare-table-e`, `cag-key-takeaway-v2`, `cag-toc-v3`, `cag-faq-accordion`, etc.), JSON-LD schema, CAG agent system (66 agents), `scripts/health-sweep.sh`, `scripts/generate_sitemaps.py`. Deploy = `git push` (GitHub Actions → Cloudflare Pages).

**Binding references (read before any task):**
- `MANUAL INTERIOR-PAGE CHECKLIST.md` — THE structure manual (Hero→CTA, Parts A–N). Governs section order.
- `docs/archive/ARCHIVED-MANUAL-SEO-CHECKLIST-HOMEPAGE.md` — SEO *method* layer (4-tone meta, keyword categories, link libraries, QA).
- `PRODUCT.md` + `DESIGN.md` — brand context, READ FIRST (Non-Negotiable).
- `docs/reference/components.md` — component registry v2 (real names used below).
- `skills/cag-seo-master-checklist.md` §Interior-Page Profile.

**Non-Negotiables enforced on every page (from CLAUDE.md):**
- ≥97% Confidence Gate before any site-file write; below that → Clarification Checkpoint (write done work, log open question to session brief, ask ONE question, keep building unblocked parts).
- Preview-before-apply + Component Gate (show candidate components + variants, get approval) before writing.
- Same content only — visual/SEO layer; never invent credentials/prices (Verified-Claim Ledger).
- First-person brand voice ("we/our/here at C.A.Gs"); exceptions = encyclopedic facts.
- Shipping line on every bird card: `Ships nationwide · $185 airport · $350 home`.
- Entity 4-Move Loop is the section-build method.
- One CTA per page (`hideGlobalCta` if page has its own `<CTA>`).
- Commit + push after every page (push = deploy).

---

## Scope

**18 pages in build scope (all `.astro`):**

| # | Slug | Cluster | Type | Length rule | Specialist agent |
|---|------|---------|------|-------------|------------------|
| 1 | `african-grey-parrot-care-guide` | A Care/Health | Care pillar | competitor-max + 1,000 | cag-content-architect → writer + care-grid + faq |
| 2 | `african-grey-care` | A Care/Health | Care **hub** (links to spokes) | competitor-max + 1,000 | cag-content-architect |
| 3 | `african-grey-parrot-diet` | A Care/Health | Diet pillar | competitor-max + 1,000 | cag-content-architect |
| 4 | `best-african-grey-parrot-food` | A Care/Health | **Product-recommendation** guide (Harrison's/Zupreem) | competitor-max + 1,000 | cag-content-architect / cag-blog-post-agent |
| 5 | `african-grey-parrot-lifespan` | A Care/Health | Informational | competitor-max + 1,000 | cag-content-architect |
| 6 | `african-grey-parrot-health-guarantee` | A Care/Health | Trust | competitor-max + 1,000 | cag-trust-signals-agent |
| 7 | `trusted-african-grey-parrot-breeders` | B Trust | Branded/trust **+ About Us** (breeder story / E-E-A-T) | competitor-max + 1,000 | **cag-about-builder** (H-S-S story) + cag-trust-signals-agent |
| 8 | `african-grey-reviews` | B Trust | Trust (overlap #2) | capped medium (~1,200) | cag-trust-signals + cag-case-study-agent |
| 9 | `captive-bred-african-grey-parrot` | B Trust | Attribute | interior-standard | **cag-variant-specialist** (owns it) |
| 10 | `cites-african-grey-documentation` | B Trust | CITES education | competitor-max + 1,000 | cag-content-architect + cag-external-link-agent |
| 11 | `how-to-avoid-african-grey-parrot-scams` | B Trust | Scam | competitor-max + 1,000 | **cag-scam-specialist** (⚠️ fix `yr` bug first) |
| 12 | `african-grey-parrot-guide` | C Reference | Species pillar | competitor-max + 1,000 | **cag-species-guide-builder** (Entity-Tree) |
| 13 | `african-grey-parrot-faq` | C Reference | FAQ pillar | competitor-max + 1,000 | **cag-faq-agent** |
| 14 | `how-to-tame-african-grey-parrot` | C Reference | Training | competitor-max + 1,000 | cag-content-architect |
| 15 | `african-grey-adoption` | C Reference | Adoption info | competitor-max + 1,000 | cag-content-architect |
| 16 | `african-grey-parrot-price` | D Financial | Pricing | competitor-max + 1,000 | **cag-financial-strategist** |
| 17 | `contact-us` | E Utility | Form | SHORT (not benchmarked) | **cag-contact-form-updater** |
| 18 | `privacy-policy` | E Utility | Legal | SHORT (not benchmarked) | cag-content-architect (light) |

**3 related pages — confirmed DISTINCT intent (not in this batch, NOT cannibalizing):**
Per the prior audit (`docs/research/cannibalization-audit-2026-05-22.md`), these target different mindsets/formats and are **kept separate, no 301**:
- `testimonials`, `case-studies` — distinct formats from `african-grey-reviews` (not flagged in the audit).
- `african-grey-parrot-adoption-cost` — factual cost-table intent, distinct from `african-grey-parrot-price` (audit:57-60).

They are out of this batch's scope but are valid standalone pages — can be added later if desired.

**Out of scope:** location pages, comparison pages (`*-vs-*`, `*comparison`, `pros-and-cons`), all `*-for-sale*` / transactional pages, `blog`, `search`. **No separate `/about/` page** — the About-Us / breeder-story content lives on `trusted-african-grey-parrot-breeders` (Task 4.1), which carries AboutPage schema + the H-S-S story so the "about" intent ranks on a real keyword instead of an orphan page.

### Per-page section spec (bird section · compare · jumplinks · hero · schema)

| Slug | Available-bird section | Compare (Congo vs Timneh) | Jumplinks (`cag-toc-v3:02`) | Hero pick | Core schema |
|------|:---:|:---:|:---:|-----------|-------------|
| care-guide | ✅ | ✅ | ✅ | `cag-hero-v3:a` Scattered Flock | Article + FAQPage + Breadcrumb |
| african-grey-care | optional | ➖ | ✅ | `cag-hero-v3:b` | Article + FAQPage + Breadcrumb |
| diet | optional | ✅ | ✅ | `cag-hero-v3:a` | Article + FAQPage |
| best-food | optional | ➖ | ✅ | `cag-hero-v3:a` | Article + FAQPage |
| lifespan | ➖ | ✅ | ✅ | `cag-hero-v3:c` Mosaic Metrics | Article + FAQPage |
| health-guarantee | ✅ | ➖ | ✅ | `cag-hero-v3:b` Authority Green | Article + FAQPage |
| trusted-breeders (= About Us) | ✅ | optional | ✅ | `cag-hero-v3:b` | AboutPage + Organization + LocalBusiness + FAQPage + Review |
| reviews | ✅ | ➖ | ➖ | `cag-hero-v3:b` | Review + AggregateRating + Article |
| captive-bred | ✅ | ✅ (`compare-table-e`) | ✅ | `cag-hero-v3:b` | Article + FAQPage |
| cites-documentation | ➖ | ➖ | ✅ | `cag-hero-v3:b` | Article + FAQPage |
| scams | ➖ | ➖ | ✅ | `cag-hero-v3:b` | Article + FAQPage |
| guide | ✅ | ✅ (`compare-table-e`) | ✅ | `cag-hero-v3:a` | Article + FAQPage + Breadcrumb |
| faq | optional | ➖ | ✅ | `cag-hero-v3:b` | FAQPage (primary) + Article |
| tame | ➖ | ➖ | ✅ | `cag-hero-v3:a` | HowTo + Article + FAQPage |
| adoption | optional | ➖ | ✅ | `cag-hero-v3:a` | Article + FAQPage |
| price | ✅ | ✅ (`compare-table-e`) | ✅ | `cag-hero-v3:c` Mosaic Metrics | Article + FAQPage + Offer (price-matrix) |
| contact-us | ➖ | ➖ | ➖ | minimal | ContactPage + LocalBusiness |
| privacy-policy | ➖ | ➖ | ➖ | minimal | WebPage |

➖ = none · ✅ = required · optional = at section-map gate.

---

## File Structure

- **Edit (build target):** `src/pages/<slug>/index.astro` — authoritative, deployed (per CLAUDE.md `src/pages is deployed`).
- **Components (reuse, do not fork):** `src/components/*.astro` — `HeroV3`, `CompareTableE.astro`, `KeyTakeawayV2`, `cag-toc-v3`, `FaqAccordion.astro`, `CounterSnippet.astro`, `TrustStats.astro`, `CareGrid.astro`, `ScamAwareness.astro`, `ContactForm`, `NewsletterV2.astro`, available-bird grid card.
- **Data (read, never hardcode):** `data/financial-entities.json`, `data/price-matrix.json`, `data/clutch-inventory.json`, `data/case-studies.json`, `data/competitors.json`.
- **Research output:** `docs/research/competitor-<page>-2026-06-06.md`, `docs/research/cannibalization-audit-2026-06-06.md`.
- **Per-page planning output:** `sessions/2026-06-06-<slug>-section-map.md`.
- **Session brief (Clarification Checkpoint target):** `sessions/2026-06-06-interior-batch-brief.md`.
- **Redirects (if any 301):** `site/content/_redirects` (via cag-redirect-manager).
- **Sitemaps:** `public/*.xml` via `scripts/generate_sitemaps.py` (run once after all builds).

Each page is a self-contained `.astro` file edited in place; no cross-file refactors. Files that change together (a page + its `_redirects` line + its sitemap entry) are sequenced within that page's tasks.

---

## Phase 0 — Research Refresh (batched, all pages)

**Files:**
- Create: `docs/research/competitor-<page>-2026-06-06.md` (one per page)
- Create: `docs/research/keyword-gap-2026-06-06.md`
- Modify: `sessions/2026-06-06-interior-batch-brief.md`

### Task 0.1: Create the session brief

- [ ] **Step 1: Write the batch brief file**

Create `sessions/2026-06-06-interior-batch-brief.md` with: the 18-page table above, the confirmed distinct-intent map (care + adoption clusters per the 2026-05-22 audit — no 301s), an empty `## Open Flags` section (Clarification-Checkpoint target), and `## Length Targets` (to fill in 0.3).

- [ ] **Step 2: Commit**

```bash
git add sessions/2026-06-06-interior-batch-brief.md
git commit -m "docs(session): interior-page full-SEO batch brief"
```

### Task 0.2: Refresh per-page competitor scrapes

- [ ] **Step 1: Identify the top-3 ranking competitor URLs per target page**

Run `@cag-competitive-keyword-gap-agent` for the 18 target keywords. For each page, record the 3 competitor URLs that currently rank for its primary keyword.

- [ ] **Step 2: Scrape word counts + H1/H2 maps**

Run `@cag-competitor-intel` (Firecrawl) against each recorded competitor URL. For each target page, capture: competitor word counts (so we can take the **max**), their H2 outline, their schema types, and content subtopics they cover.

- [ ] **Step 3: Verify output exists**

Run: `ls docs/research/competitor-*-2026-06-06.md | wc -l`
Expected: ≥ 16 (the long pages; contact-us/privacy-policy are exempt from benchmarking).

- [ ] **Step 4: Commit**

```bash
git add docs/research/
git commit -m "research(interior): refreshed per-page competitor word counts + outlines (2026-06-06)"
```

### Task 0.3: Set length targets

- [ ] **Step 1: Compute target = competitor-max + 1,000**

For each of the 16 long pages, write into the brief's `## Length Targets`: `competitor-max word count` + `1000`. For `african-grey-reviews` cap at ~1,200 (trust page, depth ≠ word padding). For `contact-us` and `privacy-policy` write `SHORT — utility/legal, not benchmarked`.

- [ ] **Step 2: Commit**

```bash
git add sessions/2026-06-06-interior-batch-brief.md
git commit -m "research(interior): length targets = competitor-max + 1000 (utility pages exempt)"
```

---

## Phase 1 — Intent Verification (NO 301s — clusters confirmed distinct)

> **Settled, do not re-litigate.** The 2026-05-22 audit (`docs/research/cannibalization-audit-2026-05-22.md`) already ruled all four clusters **KEEP / DIFFERENTIATE by intent — no redirects.** Pages #2 and #4 are unconditional full builds. This phase only *locks each page's distinct intent + meta framing* so the builds in Phases 3–6 stay in their lane. It is a fast desk-check, not a new audit.

**Files:**
- Modify: `sessions/2026-06-06-interior-batch-brief.md` (record locked intents)

### Task 1.1: Lock each page's distinct intent (per 2026-05-22 audit)

- [ ] **Step 1: Record the confirmed intent map into the brief**

Write each page's locked angle so two pages never compete for the same query:
- `african-grey-parrot-care-guide` = **complete 4,500-word care pillar** (housing, diet, health, enrichment).
- `african-grey-care` = **hub** that links out to all care spokes (diet, health, training, lifespan); hub framing, not a duplicate guide.
- `african-grey-parrot-diet` = **diet science / what-they-eat** (nutrition, safe vs toxic foods).
- `best-african-grey-parrot-food` = **product-recommendation guide** (Harrison's, Zupreem, pellet vs seed brands) — commercial-review intent, not diet science.
- `african-grey-reviews` = buyer **reviews/ratings** (Review + AggregateRating).
- `testimonials` / `case-studies` = distinct formats, **out of batch** (no conflict).
- `african-grey-adoption` = **emotional/lifestyle adoption framing**.
- `african-grey-parrot-adoption-cost` = **factual cost tables**, out of batch (distinct mindset).
- `african-grey-parrot-price` = full **pricing/cost pillar**.

- [ ] **Step 2: Differentiate meta only (per audit:87-89)**

Confirm (via `@cag-meta-description-agent`) that `african-grey-care` reads as "Hub for all African Grey care resources…" and `african-grey-parrot-care-guide` reads as "Complete care guide…". These get finalized inside each page's R8, no separate commit needed here.

- [ ] **Step 3: Commit the locked intent map**

```bash
git add sessions/2026-06-06-interior-batch-brief.md
git commit -m "seo(interior): lock distinct-intent map (no 301s — per 2026-05-22 audit)"
```

---

## Phase 2 — The Per-Page Build Recipe (R1–R12)

> This is the canonical procedure. Every page task in Phases 3–7 runs R1–R12 with its own spec-table parameters and its own verification commands. Steps R1–R12 are identical workflow; only the parameters (slug, components, length, sections, schema, link targets) change per page.

**R1 — Orient (grill-me).** Run the `grill-me` skill scoped to the page (gap matrix + top-pages + brief already loaded from Phase 0). Output a SESSION CONTEXT block: framework choice, AIO/GEO approach, visual plan.

**R2 — Content audit.** Run `@cag-content-audit-agent` (4-phase: Intent → Competitor → Action Plan → Internal Linking) using the refreshed `docs/research/competitor-<page>-2026-06-06.md`. Output → `sessions/2026-06-06-<slug>-section-map.md`.

**R3 — Section Map + Component Gate (APPROVAL).** From `components.md`, propose 1–3 candidate components per section using the page's spec-table row (hero pick, bird section, compare, jumplinks). Present candidates + variants with Recommend + Why. **Wait for user approval.** Do not write code before approval.

**R4 — Angles + PAA.** Run `@cag-angle-agent` (5–10 hooks) then `@cag-paa-agent` (real PAA questions via Playwright) for the FAQ + featured-snippet bait.

**R5 — Build sections (interior manual Part C order).** Build Hero → CounterSnippet → KeyTakeaway → body sections → FAQ → Final CTA+Contact, using approved components. Apply: first-person voice (Part D), EBP per paragraph, woven mid-sentence links (Part F), Entity 4-Move Loop (Part E) via `@cag-entity-incorporation-agent`, declarative answer blocks (Part H). Length = the page's brief target. Add `.cag-seam` logo dividers between 4–8 major sections. Bird/compare/jumplink sections per spec table. **Read `data/*.json` for all prices/shipping — never hardcode.**

**R6 — Non-commodity pass.** Run `@cag-non-commodity-content-agent` in audit-then-rewrite mode: classify each section STRONG/SHARPEN/REBUILD, rewrite only weak sections (don't regress indexed copy).

**R7 — Schema.** Emit the page's core schema set (spec table). Extend existing JSON-LD, never duplicate. FAQPage schema must mirror visible FAQ.

**R8 — AEO/GEO gate.** Run in order: `@cag-keyword-verifier` (85–105 keyword distribution, fix flagged lines) → `@cag-meta-description-agent` (4-tone long meta, no duplicates) → `@cag-trust-signals-agent` (trust elements where the spec calls for them).

**R9 — Build + schema verify.** Run `npm run build`. Then verify rendered output (not source):
```bash
grep -l "FAQPage" dist/<slug>/index.html
grep "rel=\"canonical\"" dist/<slug>/index.html   # must be absolute https URL
grep -c "&lt;svg" dist/<slug>/index.html           # must be 0 (icon set:html rule)
```

**R10 — Technical gate.** Run `@cag-accessibility-fixer` (WCAG AA → Lighthouse a11y 100) and `@cag-performance-fixer` (LCP<2.5s, CLS<0.1; warm median-of-3). Run `@cag-canonical-fixer`.

**R11 — Deploy.** `git add` the page + `git commit` + `git push` (push = deploy). Then `@cag-deploy-verifier` (200 check + IndexNow).

**R12 — Live verify.**
```bash
curl -sI https://congoafricangreys.com/<slug>/ | head -1   # expect HTTP/2 200
```

---

## Phase 3 — Cluster A: Care/Health (pages 1–6)

> Build order within cluster: care-guide (pillar) first so other care pages link up to it.

### Task 3.1: `african-grey-parrot-care-guide` (care pillar)
**Files:** Modify `src/pages/african-grey-parrot-care-guide/index.astro` · Map `sessions/2026-06-06-african-grey-parrot-care-guide-section-map.md`

- [ ] **Step 1: Run R1–R4** (orient, audit, Section Map + Component Gate, angles/PAA). Components: `cag-hero-v3:a`, `cag-toc-v3:02`, `cag-key-takeaway-v2:02`, `CareGrid:classic`, `cag-compare-table-e` (Congo vs Timneh care), available-bird grid, `cag-faq-accordion`, `ContactForm:application`. Length = brief target for this page.
- [ ] **Step 2: Run R5–R7** (build, non-commodity, schema = Article + FAQPage + Breadcrumb). Bird section ✅, compare ✅, jumplinks ✅.
- [ ] **Step 3: Run R8** (AEO gate). Internal links: → guide, diet, lifespan, health-guarantee, congo-african-grey-for-sale.
- [ ] **Step 4: Run R9** — build + schema verify.

Run: `npm run build && grep -l "FAQPage" dist/african-grey-parrot-care-guide/index.html`
Expected: build succeeds; grep prints the path.

- [ ] **Step 5: Run R10–R11** (tech gate, deploy).
- [ ] **Step 6: Run R12** — live verify.

Run: `curl -sI https://congoafricangreys.com/african-grey-parrot-care-guide/ | head -1`
Expected: `HTTP/2 200`

- [ ] **Step 7: Commit** (done inside R11; confirm clean)

```bash
git status --porcelain   # expect empty
```

### Task 3.2: `african-grey-care` (care HUB — links to all spokes)
**Files:** Modify `src/pages/african-grey-care/index.astro`

- [ ] **Step 1: Run R1–R4.** Build as the **care hub** (distinct from the pillar): hub framing that links out to every care spoke (diet, health-guarantee, tame, lifespan, care-guide pillar). Components: `cag-hero-v3:b`, `cag-toc-v3:02`, `CareGrid:classic` (resource cards → spokes), `cag-faq-accordion`. Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage + Breadcrumb. Meta = "Hub for all African Grey care resources…" (per audit:88). Internal links → care-guide (pillar), diet, lifespan, health-guarantee, tame.
- [ ] **Step 3: Run R9** — `npm run build && grep -l "FAQPage" dist/african-grey-care/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `curl -sI https://congoafricangreys.com/african-grey-care/ | head -1` → `HTTP/2 200`.

### Task 3.3: `african-grey-parrot-diet`
**Files:** Modify `src/pages/african-grey-parrot-diet/index.astro`

- [ ] **Step 1: Run R1–R4.** Components: `cag-hero-v3:a`, `cag-toc-v3:02`, `cag-key-takeaway-v2:02`, `CareGrid:classic` (safe foods / toxic foods), `cag-faq-accordion`. Differentiate from best-food per Phase 1 (nutrition science angle). Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage. Internal links: → best-food, care-guide, guide. External authority links: avian nutrition source (woven mid-sentence, Part F).
- [ ] **Step 3: Run R9** — `npm run build && grep -l "FAQPage" dist/african-grey-parrot-diet/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

### Task 3.4: `best-african-grey-parrot-food` (product-recommendation guide)
**Files:** Modify `src/pages/best-african-grey-parrot-food/index.astro`

- [ ] **Step 1: Run R1–R4.** Build as the **commercial product/brand-review** guide — distinct from diet's nutrition science (Harrison's, Zupreem, pellet vs seed brand comparison). Components: `cag-hero-v3:a`, `cag-toc-v3:02`, `CareGrid:classic`, `cag-pricing-table:classic` (brand comparison), `cag-faq-accordion`. Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage. Internal links → diet (science), care-guide. External authority links to brand/avian-nutrition sources (woven mid-sentence).
- [ ] **Step 3: Run R9** — `npm run build && grep -l "FAQPage" dist/best-african-grey-parrot-food/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `curl -sI https://congoafricangreys.com/best-african-grey-parrot-food/ | head -1` → `HTTP/2 200`.

### Task 3.5: `african-grey-parrot-lifespan`
**Files:** Modify `src/pages/african-grey-parrot-lifespan/index.astro`

- [ ] **Step 1: Run R1–R4.** Components: `cag-hero-v3:c` (Mosaic Metrics — lifespan data), `cag-key-takeaway-v2:02`, `cag-compare-table-e` (Congo 50–60 yr vs Timneh), `cag-toc-v3:02`, `cag-faq-accordion`. Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage. Compare ✅ (lifespan by variant). Internal links → care-guide, guide, health-guarantee.
- [ ] **Step 3: Run R9** — `npm run build && grep -l "FAQPage" dist/african-grey-parrot-lifespan/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

### Task 3.6: `african-grey-parrot-health-guarantee`
**Files:** Modify `src/pages/african-grey-parrot-health-guarantee/index.astro`

- [ ] **Step 1: Run R1–R4.** Components: `cag-hero-v3:b` (Authority Green), `cag-trust-stats:classic`, `cag-key-takeaway-v2:02`, available-bird grid, `cag-faq-accordion`. Owner: `@cag-trust-signals-agent`. Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage. Bird section ✅. Verified-Claim Ledger bounds all health claims (no PBFD/PCR/board-cert beyond confirmed). Internal links → captive-bred, trusted-breeders, care-guide.
- [ ] **Step 3: Run R9** — `npm run build && grep -l "FAQPage" dist/african-grey-parrot-health-guarantee/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

---

## Phase 4 — Cluster B: Trust/Authority (pages 7–11)

### Task 4.1: `trusted-african-grey-parrot-breeders` (= the "About Us" page — breeder story + trust keyword)
**Files:** Modify `src/pages/trusted-african-grey-parrot-breeders/index.astro`

> **Dual role:** this page is BOTH the "trusted breeders" ranking page AND the site's About Us / breeder-story page (no separate `/about/`). It must carry the H-S-S breeder narrative + E-E-A-T credentials *and* target the trust keyword. Co-owned: `@cag-about-builder` (story) + `@cag-trust-signals-agent` (trust elements).

- [ ] **Step 1: Run R1–R4.** Components: `cag-hero-v3:b` (Authority Green), `cag-trust-stats:classic`, `cag-split-feature:editorial` (the **owner/breeder story** — Mark & Teri Benjamin, Midland TX, founded 2014, 12+ yrs aviary), `cag-testimonials:feature`, available-bird grid, `cag-toc-v3:02`, `cag-faq-accordion`. Apply branded-search targets (`@cag-branded-hybrid-keywords` skill). Length = brief target.
- [ ] **Step 2: Run R5–R8 with H-S-S layered on the breeder story.** Run `@cag-about-builder` to draft the **Hook → Story → Solution** narrative: who we are, why we breed African Greys, USDA AWA license, CITES Appendix-I captive-bred documentation, hand-raising process, health practices — all bounded by the Verified-Claim Ledger (never overclaim PBFD/PCR/board-cert beyond confirmed). First-person voice ("here at C.A.Gs…"). Then `@cag-trust-signals-agent` adds trust-stat row + review schema. Schema = **AboutPage + Organization + LocalBusiness + FAQPage + Review** (AboutPage is the About-Us signal; Organization carries founder/credentials). Bird section ✅.
- [ ] **Step 3: Run R9** — `npm run build && grep -l "AboutPage" dist/trusted-african-grey-parrot-breeders/index.html && grep -l "LocalBusiness" dist/trusted-african-grey-parrot-breeders/index.html`. Expected: both pass.
- [ ] **Step 4: Run R8 link wiring.** Internal links → reviews, health-guarantee, captive-bred, cites-documentation, scams; this page is the "about/trust" anchor, so link TO it from homepage + high-trust pages (handled in their R8). External authority: USDA AWA, cites.org appendices (woven mid-sentence via `@cag-external-link-agent`).
- [ ] **Step 5: Run R10–R12.** Live verify → `curl -sI https://congoafricangreys.com/trusted-african-grey-parrot-breeders/ | head -1` → `HTTP/2 200`.

### Task 4.2: `african-grey-reviews` (buyer reviews/ratings — distinct from testimonials/case-studies)
**Files:** Modify `src/pages/african-grey-reviews/index.astro`

- [ ] **Step 1: Run R1–R4.** Components: `cag-hero-v3:b`, `cag-testimonials:feature` + `cag-testimonials:grid`, available-bird grid, `cag-faq-accordion`. Owners: `@cag-trust-signals-agent` + `@cag-case-study-agent` (reads `data/case-studies.json`; never fabricate reviews). Length capped ~1,200. `testimonials`/`case-studies` stay separate (distinct formats) — do NOT redirect.
- [ ] **Step 2: Run R5–R8.** Schema = Review + AggregateRating + Article. Bird section ✅.
- [ ] **Step 3: Run R9** — `npm run build && grep -l "AggregateRating" dist/african-grey-reviews/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `curl -sI https://congoafricangreys.com/african-grey-reviews/ | head -1` → `HTTP/2 200`.

### Task 4.3: `captive-bred-african-grey-parrot` (cag-variant-specialist owns it)
**Files:** Modify `src/pages/captive-bred-african-grey-parrot/index.astro`

- [ ] **Step 1: Run R1–R4** via `@cag-variant-specialist` (interior-standard). Components: `cag-hero-v3:b`, `cag-trust-stats:classic`, `cag-compare-table-e`, available-bird grid, `cag-faq-accordion`. Length = interior-standard.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage. Bird ✅, compare ✅. Cross-link the attribute/variant cluster (dna-tested, hand-raised, congo/timneh for-sale). CITES Appendix-I captive-bred framing.
- [ ] **Step 3: Run R9** — `npm run build && grep -c "&lt;svg" dist/captive-bred-african-grey-parrot/index.html`. Expected: `0` (icon set:html — this page had the trust-bar SVG-in-content bug historically; verify clean).
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

### Task 4.4: `cites-african-grey-documentation`
**Files:** Modify `src/pages/cites-african-grey-documentation/index.astro`

- [ ] **Step 1: Run R1–R4.** Components: `cag-hero-v3:b`, `cag-key-takeaway-v2:01`, `cag-toc-v3:02`, `cag-faq-accordion`. Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage. Heavy external-authority links via `@cag-external-link-agent` — cite the specific resource page (`parrots.org/encyclopedia/grey-parrot/`, cites.org appendices), woven mid-sentence. CITES Appendix-I correctness (uplisted CoP17, 2017). Internal links → scams, captive-bred, health-guarantee.
- [ ] **Step 3: Run R9** — `npm run build && grep -l "FAQPage" dist/cites-african-grey-documentation/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

### Task 4.5: `how-to-avoid-african-grey-parrot-scams` (FIX BUG FIRST)
**Files:** Modify `src/pages/how-to-avoid-african-grey-parrot-scams/index.astro`

- [ ] **Step 1: Fix the `yr is not defined` bug.** Locate the inline `<script>` (cost/WHOIS calculator widget, ~built line 99) referencing undefined `yr`. Define it or remove the dead widget.

Run: `npm run build && grep -n "yr" dist/how-to-avoid-african-grey-parrot-scams/index.html`
Expected: no undefined `yr` reference remains.

- [ ] **Step 2: Verify no console error** — load the built page and confirm `ReferenceError: yr is not defined` is gone (preview console or `node`-eval of the script block).
- [ ] **Step 3: Run R1–R4** via `@cag-scam-specialist`. Components: `cag-hero-v3:b`, `cag-scam-awareness:compare` + `cag-key-takeaway-v2:03` (do/don't), `cag-toc-v3:02`, `cag-faq-accordion`. Length = brief target.
- [ ] **Step 4: Run R5–R8.** Schema = Article + FAQPage. Internal links → cites-documentation, captive-bred, trusted-breeders, reviews.
- [ ] **Step 5: Run R9** — `npm run build && grep -l "FAQPage" dist/how-to-avoid-african-grey-parrot-scams/index.html`. Expected: pass.
- [ ] **Step 6: Run R10–R12.** Live verify → `200`.

---

## Phase 5 — Cluster C: Reference (pages 12–15)

### Task 5.1: `african-grey-parrot-guide` (species pillar)
**Files:** Modify `src/pages/african-grey-parrot-guide/index.astro`

- [ ] **Step 1: Run R1–R4** via `@cag-species-guide-builder` (Entity-Tree, reads `data/price-matrix.json`). Components: `cag-hero-v3:a`, `cag-toc-v3:02`, `cag-key-takeaway-v2:02`, `cag-compare-table-e`, available-bird grid, `cag-care-grid`, `cag-faq-accordion`. Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage + Breadcrumb. Bird ✅, compare ✅. Entity-Tree for AIO citation. Internal links → care-guide, diet, lifespan, congo/timneh for-sale, comparison hub.
- [ ] **Step 3: Run R9** — `npm run build && grep -l "BreadcrumbList" dist/african-grey-parrot-guide/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

### Task 5.2: `african-grey-parrot-faq` (FAQ pillar)
**Files:** Modify `src/pages/african-grey-parrot-faq/index.astro`

- [ ] **Step 1: Run R1–R4** via `@cag-faq-agent` (QAB; GSC Queries + PAA-sourced). Components: `cag-hero-v3:b`, `cag-toc-v3:02`, `cag-faq-accordion:classic` (grouped by topic). Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = FAQPage (primary, comprehensive) + Article. Internal links from each answer cluster → the relevant pillar (care/diet/price/scams/cites).
- [ ] **Step 3: Run R9** — `npm run build && grep -c "Question" dist/african-grey-parrot-faq/index.html`. Expected: ≥ visible FAQ count (schema mirrors visible).
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

### Task 5.3: `how-to-tame-african-grey-parrot`
**Files:** Modify `src/pages/how-to-tame-african-grey-parrot/index.astro`

- [ ] **Step 1: Run R1–R4.** Components: `cag-hero-v3:a`, `cag-toc-v3:02`, `cag-care-grid:classic` (numbered taming steps), `cag-key-takeaway-v2:01`, `cag-faq-accordion`. Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = HowTo + Article + FAQPage (HowTo steps mirror the numbered care-grid). Internal links → care-guide, guide, diet.
- [ ] **Step 3: Run R9** — `npm run build && grep -l "HowTo" dist/how-to-tame-african-grey-parrot/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

### Task 5.4: `african-grey-adoption`
**Files:** Modify `src/pages/african-grey-adoption/index.astro`

- [ ] **Step 1: Run R1–R4.** Components: `cag-hero-v3:a`, `cag-toc-v3:02`, `cag-key-takeaway-v2:01`, `cag-faq-accordion`. Length = brief target. Frame adoption honestly (we are a breeder; adoption-curious buyers → captive-bred documented path).
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage. Internal links → price, captive-bred, trusted-breeders. (If Phase 1 consolidated adoption-cost here-adjacent, ensure no overlap.)
- [ ] **Step 3: Run R9** — `npm run build && grep -l "FAQPage" dist/african-grey-adoption/index.html`. Expected: pass.
- [ ] **Step 4: Run R10–R12.** Live verify → `200`.

---

## Phase 6 — Cluster D: Financial (page 16)

### Task 6.1: `african-grey-parrot-price`
**Files:** Modify `src/pages/african-grey-parrot-price/index.astro`

- [ ] **Step 1: Run R1–R4** via `@cag-financial-strategist` (reads `data/financial-entities.json` + `data/price-matrix.json`). Components: `cag-hero-v3:c` (Mosaic Metrics), `cag-pricing-table:tiers`, `cag-compare-table-e` (CAG vs TAG cost), `cag-key-takeaway-v2:02`, available-bird grid, `cag-toc-v3:02`, `cag-faq-accordion`. Length = brief target.
- [ ] **Step 2: Run R5–R8.** Schema = Article + FAQPage + Offer (from price-matrix). Cover purchase price, first-year setup, IATA shipping ($185 airport / $350 home — from data, never hardcode), annual + lifetime (40–60 yr). Bird ✅, compare ✅. Internal links → adoption, adoption-cost, captive-bred, health-guarantee, congo/timneh for-sale. (`adoption-cost` stays a separate factual-cost page — link to it, don't absorb it.)
- [ ] **Step 3: Run R9** — `npm run build && grep -l "Offer" dist/african-grey-parrot-price/index.html`. Expected: pass.
- [ ] **Step 4: Verify shipping figures pulled from data, not hardcoded**

Run: `grep -E "185|350" dist/african-grey-parrot-price/index.html`
Expected: present, matching `data/financial-entities.json` `delivery_options`.

- [ ] **Step 5: Run R10–R12.** Live verify → `200`.

---

## Phase 7 — Cluster E: Utility (pages 17–18, SHORT — not length-benchmarked)

### Task 7.1: `contact-us`
**Files:** Modify `src/pages/contact-us/index.astro`

- [ ] **Step 1: Run R3 (Component Gate only — no length benchmark).** Components: minimal hero, `ContactForm:application`, `LocalBusiness` map (via `@cag-google-map-agent` if missing). NO bird/compare/jumplinks. Owner: `@cag-contact-form-updater`.
- [ ] **Step 2: Standardize the form.** Run `@cag-contact-form-updater` — canonical CAG inquiry form, ARIA labels, no payment processor hardcoded (`[PAYMENT_METHOD_TBD]`). Confirm GA4 `generate_lead` event present (per `@cag-site-hygiene-agent`).
- [ ] **Step 3: Run R7–R8 (light).** Schema = ContactPage + LocalBusiness. Meta via `@cag-meta-description-agent`. Keep copy short — this is a utility page.
- [ ] **Step 4: Run R9** — `npm run build && grep -l "ContactPage" dist/contact-us/index.html`. Expected: pass.
- [ ] **Step 5: Run R10–R12.** Live verify → `200`.

### Task 7.2: `privacy-policy`
**Files:** Modify `src/pages/privacy-policy/index.astro`

- [ ] **Step 1: Run R3 (Component Gate only).** Components: minimal hero + plain prose container (`.container-text` 760px). NO bird/compare/FAQ/jumplinks. SHORT legal page.
- [ ] **Step 2: Apply design-system shell only** (visual layer; do NOT rewrite legal content — Non-Negotiable "same content"). Newsreader headings, IBM Plex body inherit from Direction-D automatically.
- [ ] **Step 3: Run R7–R8 (light).** Schema = WebPage. Meta via `@cag-meta-description-agent` (noindex? confirm — privacy pages usually indexable but low priority).
- [ ] **Step 4: Run R9** — `npm run build && grep "rel=\"canonical\"" dist/privacy-policy/index.html`. Expected: absolute canonical present.
- [ ] **Step 5: Run R10–R12.** Live verify → `200`.

---

## Phase 8 — Batch Finalize

### Task 8.1: Sitemaps + site-wide hygiene

- [ ] **Step 1: Regenerate sitemaps** (pages changed, none added/removed, but slugs were rebuilt + any 301s).

Run: `python3 scripts/generate_sitemaps.py`
Expected: writes to BOTH `public/` and `site/content/` (clobber-bug fix), zero phantom URLs.

- [ ] **Step 2: Full health sweep.**

Run: `bash scripts/health-sweep.sh`
Expected: git/deploy clean, 66 agents OK, Astro build passes, live 200s, dist hygiene clean.

- [ ] **Step 3: Site-wide hygiene pass.** Run `@cag-site-hygiene-agent` — breadcrumb audit (all rebuilt pages have Breadcrumb + BreadcrumbList), footer links, GA4 health.

- [ ] **Step 4: Commit + push.**

```bash
git add public/ site/content/
git commit -m "seo(interior): regenerate sitemaps + final hygiene after 18-page rebuild"
git push
```

- [ ] **Step 5: Deploy verify batch.** Run `@cag-deploy-verifier` across all 18 slugs → confirm 200s + IndexNow submission (`api.indexnow.org`, key `f8071…`).

### Task 8.2: Update governance docs + memory

- [ ] **Step 1: Update CLAUDE.md Active Session** with the interior-batch completion status.
- [ ] **Step 2: Update `docs/reference/top-pages.md`** (any new GSC signal) and `sessions/2026-06-06-interior-batch-brief.md` final state.
- [ ] **Step 3: Write a memory** at `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/` recording the interior-batch method + cannibalization decisions, + index line in `MEMORY.md`.
- [ ] **Step 4: Commit + push.**

```bash
git add CLAUDE.md docs/reference/top-pages.md sessions/
git commit -m "docs(interior): batch complete — 18 pages to homepage standard"
git push
```

---

## Self-Review

**1. Spec coverage:** All 17 user pages + `african-grey-adoption` = 18 build tasks (3.1–3.6, 4.1–4.5, 5.1–5.4, 6.1, 7.1–7.2). 3 cannibalization pages handled in Phase 1. Workflow-order check (Sprint 0.5) confirmed in pre-work. Live-site scan for extra pages done (Phase 0 inventory). "Competitor word count + 1000" → Phase 0.3. Short-page exemption (contact/privacy) → Cluster E. Component selection (Hero A/C, Variant A/B, compare, bird sections, jumplinks) → per-page spec table + R3 Component Gate. Agent/skill assignment → per-task. ✅ No gaps.

**2. Placeholder scan:** No "TBD/handle edge cases/similar to Task N." The recipe R1–R12 is defined once in full (Phase 2) and referenced by parameter — each page task lists concrete components, schema, links, and exact verify commands. `[PAYMENT_METHOD_TBD]` in Task 7.1 is an intentional project token (payment processor not chosen), not a plan placeholder.

**3. Type consistency:** Component names match `components.md` exactly (`cag-hero-v3:a/b/c`, `cag-compare-table-e`, `cag-key-takeaway-v2:01/02/03`, `cag-toc-v3:02`, `cag-faq-accordion`, `CareGrid.astro`, `ScamAwareness`, `ContactForm:application`). Build command `npm run build` matches `package.json`. Scripts `health-sweep.sh` / `generate_sitemaps.py` confirmed present. Verify commands use real slugs + real `dist/<slug>/index.html` paths.

---

**Note:** No 301s in this batch. All 18 pages are unconditional full builds. Per the 2026-05-22 audit, the care cluster (care-guide / african-grey-care / diet / best-food) and the adoption cluster (adoption / adoption-cost) are **distinct intent — kept separate**. Phase 1 is a fast intent-lock desk-check (no new audit, no redirects), then Phases 3–7 build straight through.

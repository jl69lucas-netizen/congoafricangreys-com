# For-Sale Pages Program (22-page transactional cluster) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task (breeder mandate for this program: **work inline, NO subagents**). Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Merge the two MFS for-sale source docs into one CAG for-sale-page builder skill, run the comparison-cluster methodology (Sprint 0 comp research → grill-me → strategies → visual components → H1–H6 gate → build) on 22 transactional pages, starting with the egg page.

**Architecture:** One new canonical skill (`skills/cag-for-sale-page-builder.md`) that layers the MFS on-page-SEO formula (keyword distribution, EFBP openings, meta formats, counter snippets) on top of the proven comparison-page pipeline (research protocol, dup-gate, uniform image boxes, final-page-pass) with a transactional profile. Pages build in 4 clusters on `main`, each page gated on breeder approvals exactly as the comparison cluster was.

**Tech Stack:** Astro + Tailwind (src/pages/<slug>/index.astro), Direction D theme, existing scripts (`final_page_audit.py`, `dup_content_audit.py`, `generate_sitemaps.py`, `register_skills.py`), Firecrawl MCP for competitor research, visual-companion browser previews.

---

## ⚠️ OPEN FLAGS — resolve with breeder before Task 6 (Recommend + Why)

1. **Egg page conflict (BLOCKING for that page).** `/african-grey-parrot-bird-eggs-for-sale-usa/` as a straight "buy fertile eggs" transactional page directly contradicts our own live scam content — the shipped 12-red-flags module says *"'Parrot eggs for sale' — virtually always a scam"*, and the species is CITES Appendix I. **(Recommended)** Rebuild the page as a *truth-forward hybrid*: rank for `psittacus erithacus egg` + egg-keyword universe, open with the honest breeder position (why we don't ship loose fertile eggs to hobby incubators / why 95% of egg listings are fraud), teach candling/incubation as expertise proof, and convert the buyer to reserving a *hatching/weaned chick* instead. WHY: keeps the URL's rankings and the keyword capture, is the only version consistent with the Verified-Claim Ledger and the scam cluster, and is a moat no scam competitor can copy. Trade-off: some pure "buy eggs now" searchers bounce. Alternative (not recommended): literal egg-sales page — cannibalizes our anti-scam authority and risks the whole site's trust positioning.
2. **Google Queries.csv missing.** `Fresh-CAGs-GOOGLE-DADA-as-of-16-07-2026/` contains Chart/Countries/Devices/Filters/Search-appearance only — **no Queries.csv and no Pages.csv**. Bing CSV is fine. Breeder must re-export GSC Performance → "Queries" (and ideally per-page filtered queries) or Task 4's keyword mining runs Bing-only.
3. **Component-kit stale facts.** The Claude-Designs kit copy says "CITES Appendix II", fake pairs (Bella/Oliver/Rosie/Max), fake ratings (4.97 · 184 families), "3-year guarantee", fake phone, 🦜 emoji. All get reconciled to DESIGN.md + Verified-Claim Ledger + real birds during intake (Task 5) — same as the "stale palette in imports" rule.
4. **Sidebar decision.** See Task 5 Step 4 — recommendation is NO page-level sidebar; Avail-B "sticky sidebar filter" is used as a *section-level* component only.

---

## How the two source docs merge (the analysis the breeder asked for)

- **`FOR-sale-PagesSKILL.md`** = the CONTENT/SEO formula: keyword distribution table (~85–105 total mentions across primary/LSI/long-tail/branded/conversational/comparison/solution/transactional), Entities+Features+Benefits+Purpose opening-paragraph formula, conversational Q&A headers with 5 A/B variants, meta title/description formats, 8 counter snippets, link rules, geographic integration, entity variety (85–112 DIFFERENT entities, never stuffed — its own thought-process documents the entity-stuffing failure and correction).
- **`maltipoo-implementation.md`** = the BUILD/QA workflow: phased checklist (foundation → content → optimization → technical), location-integration do/don't examples, section-specific keyword assignments, featured-snippet targets, CTA placement formula (every 500–700 words), trust-signal placement, newsletter 3-placement strategy, launch checklist.
- **Merge shape:** one skill where the SKILL doc becomes §Content Formula and the implementation doc becomes §Build Phases + §QA Checklist, both converted MFS→CAG (dogs/puppies/Maltipoo→birds/chicks/African Grey; Lawrence & Cathy Magee/Omaha→Mark & Teri Benjamin/Midland TX; AKC/Embark/OFA→World Parrot Trust/CITES/USDA-APHIS/Avian Biotech/AAV vets; 2-yr puppy warranty→our real guarantee; breeds→variants CAG/TAG).
- **How this differs from the comparison-page builder:** comparison pages serve DECISION intent (X vs Y, neutral-encyclopedic tables, 22–25 sections, hub+spoke). For-sale pages serve TRANSACTIONAL intent: available-bird cards with prices above the fold, deposit/reserve CTAs every 500–700 words, price/offer schema (Product+Offer per bird, AggregateOffer on group pages), scarcity honesty ("2 birds available", never fabricated), shipping-line rule on every card, contact form with real bird+price options. Everything the comparison cluster locked (dial TOC + mobile jump-rail, uniform `.sec-img.inf-img` boxes, dup-gate zero tolerance, seam dividers, image-per-header rule) carries over but **restyled** so the two clusters don't look identical.

---

### Task 1: Create the merged skill `skills/cag-for-sale-page-builder.md`

**Files:**
- Create: `skills/cag-for-sale-page-builder.md`
- Modify: `.claude/skills/` (generated by register script — never hand-edit)
- Modify: `CLAUDE.md` (register under Technical Skills + Quick Start)

- [ ] **Step 1: Write the skill** with this exact section skeleton (converted content from both source docs; every MFS term → CAG per the conversion table in `skills/cag-seo-master-checklist.md`):

```markdown
---
name: cag-for-sale-page-builder
description: THE transactional for-sale page builder for CongoAfricanGreys.com — 22-page cluster (17 for-sale + 5 buy-prefixed). Merges the MFS on-page-SEO formula (keyword distribution 85–105, EFBP openings, conversational headers, counter snippets) with the comparison-cluster pipeline (per-page research protocol, dup-gate, uniform image boxes, final-page-pass) under a TRANSACTIONAL profile: bird cards + prices above the fold, Product/Offer schema, reserve CTAs every 500–700 words, contact form with real birds+prices.
---
## 1. Page inventory & clusters (build order)
   Cluster 1 (6): eggs-usa*, congo-for-sale, timneh-for-sale, hand-raised, health-guarantee, dna-tested   *egg page = truth-forward hybrid per Open Flag 1
   Cluster 2 (5): adoption-cost, parrots-for-sale (hub), baby-for-sale, parrot-for-sale, parrot-for-sale-near-me
   Cluster 3 (6): pair-for-sale, affordable, grey-african-parrots, male-african-gray, parrots-for-sale-near-me, breeding-pair
   Cluster 4 (5 buy-prefixed): buy-near-me, buy-with-shipping, buy-intelligent-ca, buy-male-nyc-ny, where-to-buy-near-me
   ALL are LIVE pages — default mode is REBUILD; confirm on-disk slug in src/pages/ first.
## 2. Content formula (from FOR-sale-PagesSKILL, CAG-converted)
   – keyword distribution table (85–105 total; primary 30–35, LSI 20–25, long-tail 15–20, branded 10–15, conversational ~23, comparison 5–8, solution 5–10, transactional ~15)
   – EFBP opening paragraph under EVERY header (also satisfies the breeder's "opening paragraph under every header" pass-gate rule)
   – conversational Q&A headers, 5 A/B variants per major header; H1–H6 per the Heading Hierarchy Outline Gate (min 5 H5 + 5 H6, no skips)
   – entity variety 85–112 DIFFERENT entities; anti-stuffing rule quoted from the MFS failure log
   – meta: the 2 long CAG formats (Title ≤205/F1 desc ≤185 or F2 ≤300) — NOT the MFS 275-char format
   – 8 counter snippets (<4 words, number-led, Verified-Claim Ledger only)
   – Link-First anchors; internal links from internal-link-agent ledger (no repeated anchors site-wide)
## 3. Transactional layer (what makes these NOT comparison pages)
   – bird cards w/ real inventory (data/clutch-inventory.json), price, shipping line ($185/$350), Inquire CTA
   – Product+Offer schema per bird; AggregateOffer only on group/hub pages; sold ≠ InStock
   – CTA cadence every 500–700 words; one global CTA rule respected (hideGlobalCta)
   – honest scarcity only; no fabricated urgency/testimonials/ratings
   – contact form: bird+price select options + "Pickup in Midland, TX (within 2–3 hours of us)" delivery option
## 4. Build phases + QA (from maltipoo-implementation, CAG-converted)
   Phase 1 research → Phase 2 planning gates → Phase 3 build → Phase 4 QA/deploy (map to Tasks 4–9 of the program plan)
## 5. Component map (for-sale set — restyled, never comparison-identical)
   5 heroes (assignment table from Task 5), for-sale dial TOC + mobile jump-rail (new style), orange stacking tables w/ cag-congo/cag-timneh emoji imgs, KeyTakeaway + TOC (3 approved new designs), seam divider variant, sidebar = section-level only
## 6. Pass gates
   dup-content gate (pairwise vs ALL 21 siblings + comparison cluster + variant pages), final_page_audit.py for-sale profile, image-per-header rule (every H2/H3/key-H4 has OG or infographic), no visible dates, First-Person voice, Lighthouse
```

- [ ] **Step 2: Register the skill**

Run: `python3 scripts/register_skills.py --copy`
Expected: output lists `cag-for-sale-page-builder` as registered; `.claude/skills/cag-for-sale-page-builder/SKILL.md` exists.

- [ ] **Step 3: Add to CLAUDE.md** — Technical Skills bullet + a Quick Start entry:

```markdown
### "Build / rebuild a for-sale or buy page"
→ `skills/cag-for-sale-page-builder` (22-page transactional cluster; REBUILD mode; egg page = truth-forward hybrid) → `skills/cag-duplicate-content-gate` BEFORE outline approval AND at final pass → `skills/cag-final-page-pass`
```

- [ ] **Step 4: Commit + push**

```bash
git add skills/cag-for-sale-page-builder.md .claude/skills/ CLAUDE.md
git commit -m "feat(skills): cag-for-sale-page-builder — merged MFS for-sale formula + comparison pipeline, transactional profile

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
git push origin main
```

---

### Task 2: Verify skill loads next session (writing-skills discipline)

- [ ] **Step 1:** `bash scripts/health-sweep.sh --no-build` → Expected: skill-registration check PASS, no mirror drift.
- [ ] **Step 2:** Note in the session brief that `/cag-for-sale-page-builder` becomes Skill-invokable only next session (loader scans at start).

---

### Task 3: Present Open Flags 1–4 to breeder (one AskUserQuestion, Recommend+Why on each)

- [ ] **Step 1:** Ask: egg-page mode (hybrid recommended), Queries.csv re-export, component-kit fact reconciliation confirmation, sidebar decision. Log answers to `sessions/2026-07-19-session-brief.md ## Open Flags`.
- [ ] **Step 2:** Do NOT start Task 6 for the egg page until Flag 1 is answered.

---

### Task 4: Fresh-data keyword mining (Google + Bing) — one artifact per page

**Files:**
- Create: `docs/research/for-sale-keywords-2026-07.md`
- Read: `assets/1WORKING-ON/FOR-SALE-PAGES/Fresh-Bing-DADA-as-of-16-07-2026.csv`, Google export folder (post re-export), `data/analytics/`

- [ ] **Step 1:** Script the extraction (python3, pandas or csv module) per target URL: all queries, top-20 positions, high-impression/low-CTR gaps, and EVERY query ≥6 words (the long-form conversational set). Bing CSV now; Google Queries.csv when supplied.
- [ ] **Step 2:** Write per-page keyword tables into the research doc: primary / secondary / LSI / long-tail(6+ words) / branded / PAA-candidates, with position + impressions columns. Egg page section must include `psittacus erithacus egg` + relatives.
- [ ] **Step 3:** Commit.

---

### Task 5: Component intake, hero assignment, and NEW TOC/KeyTakeaway designs (visual companion)

**Files:**
- Read: `assets/1WORKING-ON/FOR-SALE-PAGES/FOR-SALE-PAGES:components-NAMES.md`, `component-designs/` screenshots, `DESIGN.md`, `PRODUCT.md`, `IMAGE-DESIGNS.md`
- Create: `sessions/2026-07-19-for-sale-component-map.md`

- [ ] **Step 1: Inventory + confirm all named components** (breeder requires explicit confirmation): Heroes = **Hero-A Scattered Flock (Polaroid scatter)** · **Hero-C Mosaic Metrics (stats strip + 2×2 mosaic)** · **Split-Hero A (image left, trust ribbon)** · **Split-Hero B (full-bleed warm gradient)** · **Split-Hero C (dark + photo grid)**. Plus Avail-B sticky-sidebar-filter, Avail-C tile gateway, mobile hero A/B/C, bird-cards mobile A/B/C, mobile nav A/B/C, the 12-family/36-variant kit (StatsBar, TrustStats, SplitHero, BirdsAvailable, ParentBirds, CareGrid, SplitSection, ComparisonTable, Infographic/Scam, FAQ, Newsletter, Video).
- [ ] **Step 2: Draft the hero→cluster assignment table** (Recommended pick + why + trade-off per cluster; e.g. Split-Hero B warm-gradient for money variant pages, Hero-C Mosaic-Metrics for hub/near-me pages, dark Split-Hero C for trust-heavy pages like health-guarantee/dna-tested, Hero-A Scattered-Flock for baby/pair pages, Split-Hero A for buy-prefixed) — breeder approves via visual companion screens before it's locked.
- [ ] **Step 3: Build 5 NEW TOC designs + 5 NEW KeyTakeaway designs** (completely different from site's current cag-toc-v1/v2/v3 + cag-key-takeaway-v2), serve via local visual-companion browser page; breeder picks 3 of each. Also show: for-sale desktop dial TOC + mobile jump-rail restyle (distinct from comparison styling), orange stacking-table designs seeded with the breeder's 5-parrot table (Congo/Timneh/Macaw/Cockatoo/Amazon) using `/emoji/cag-congo.png`/`cag-timneh.png` imgs (NEVER 🦜), CTA button set, and a for-sale seam-divider variant.
- [ ] **Step 4: Sidebar recommendation (answering the breeder's question):** **(Recommended) NO page-level sidebar.** WHY: these are mobile-majority transactional pages — a persistent sidebar narrows the 760px content column, competes with the dial TOC + jump-rail we're already shipping, and none of the top-ranking breeder competitors use one; the comparison cluster converted fine without. Advantage a sidebar WOULD give (persistent CTA + filters always in view) is captured instead by the sticky mobile CTA bar + Avail-B **section-level** sticky filter rail inside the available-birds section. Trade-off: slightly less persistent desktop CTA visibility.
- [ ] **Step 5:** Record approvals in the component-map session file; reconcile all stale kit facts (Flag 3) in the map. Commit.

---

### Task 6: Sprint 0 — deep competitor research per page (MANDATORY, model = RESEARCH-DATA doc)

**Files:**
- Create: `docs/research/for-sale-comp-<slug>-2026-07.md` (one per page, egg/congo/timneh/adoption-cost already modeled in `assets/1WORKING-ON/FOR-SALE-PAGES/RESEARCH-DATA-FOR-SALE-PAGES.md`)

- [ ] **Step 1:** For each page in the active cluster: Firecrawl search+scrape Google & Bing top 10, plus Reddit (headless — Reddit blocks curl), Facebook, Instagram, YouTube top results, plus the 30-competitor registry (`data/competitors.json`). Un-fetchable = `NOT FETCHED`, never invented.
- [ ] **Step 2:** Deliverables per page (same as comparison cluster): SERP snapshot, competitor section inventory, weaknesses/gaps, keyword universe (merged with Task 4), entity map, visual-asset blueprint, PAA set.
- [ ] **Step 3:** Derive the section matrix in THREE labeled groups — **MANDATORY core / COMPETITOR-BASED / SUGGESTED-RECOMMENDED (our moat)** — each B/C row with a grounded why. Commit per page.

---

### Task 7: Grill-me (Sprint 0.5) + two strategies + blended third

- [ ] **Step 1:** Run `grill-me` after Sprint 0 for the cluster. Checkpoint answers to the live brief.
- [ ] **Step 2:** Present **Strategy A, Strategy B, and Strategy A+B blend** (breeder's standing rule), one marked (Recommended) with data-grounded why + named trade-off.
- [ ] **Step 3:** Present per-page distribution matrix (section taxonomy, topic→micro stack, framework per section — expect AIDA/PAS/FAB blends for transactional intent, word-count split, A/B/C categories) for approval BEFORE any outline.

---

### Task 8: Per-page H1–H6 outline gate + visual skeleton approval

- [ ] **Step 1:** For each approved page: full H1→H6 outline in render order (no skips, all six levels, ≥5 H5 and ≥5 H6), every header conversational, image assignment noted per H2/H3/key-H4 (OG photo or infographic — every one gets an image, per breeder rule).
- [ ] **Step 2:** Run `skills/cag-duplicate-content-gate` header mode on the proposed outline vs ALL sibling outlines + live comparison/variant pages BEFORE approval.
- [ ] **Step 3:** Push visual-companion skeleton screens (hero pick, section order, component per section). Breeder approves outline + skeleton. **HARD STOP — no page code until approved AND breeder has dropped the generated infographics + OG images into the for-sale folder AND explicitly says start** (same gating as the comparison cluster).

---

### Task 9: Build each approved page (REBUILD mode, on main)

**Files:**
- Modify: `src/pages/<slug>/index.astro` (confirm slug on disk first; src/pages is deployed)

- [ ] **Step 1:** `git checkout main` — confirm branch before any edit.
- [ ] **Step 2:** Build section-by-section per the approved matrix: EFBP opening under every header, keyword distribution per skill §2, uniform `.sec-img.inf-img` 760px 16:9 boxes for ALL in-body images (per-image object-position; <100 KB WebP + -760 sibling + srcset), Rule 50b alt rotation, seam dividers (4–8), counter snippets, bird cards with shipping line, Product/Offer schema, PAA-only FAQ + FAQPage schema, contact form with real-bird+price options and the Midland-pickup line, newsletter (compact where in-flow).
- [ ] **Step 3:** Contact form change (shared component `cag-inquiry-form` / contact-us parity): add option `Pickup in Midland, TX — if you live within 2–3 hours of us` to the delivery select, and ensure the bird select lists each actual available bird with its price (source: `data/clutch-inventory.json` + `data/price-matrix.json`, never hardcoded).
- [ ] **Step 4:** Verify rendered output: `npx astro build` then grep/inspect `dist/<slug>/index.html` (headings, schema, no `&lt;svg`, no visible dates).
- [ ] **Step 5:** Commit + push per page (push = deploy).

---

### Task 10: Per-page final gates

- [ ] **Step 1:** `python3 scripts/dup_content_audit.py` (body) + `--headers` — pairwise vs ALL for-sale siblings, comparison cluster, and variant pages. Zero tolerance beyond the whitelist (shipping line, doc badges, CITES notice, site furniture).
- [ ] **Step 2:** `python3 scripts/final_page_audit.py` (for-sale profile) → PASS required; route FAILs through `cags-comprehensive-page-audit-system` if score is low.
- [ ] **Step 3:** Manual pass-gate list from the comparison contract, restated for for-sale: 400px-class hero heights, unique newsletter image + one-liner title per page, opening paragraph under every header, uniform OG boxes, mobile table stacking, jump-rail scroll-margin offset, further-reading cards with real thumbnails, AA contrast (clay-ink fills, #b04228 small clay), Lighthouse warm median-of-3.
- [ ] **Step 4:** `python3 scripts/generate_sitemaps.py` after any slug/page change; commit + push; live 200 check.

---

### Task 11: Program wrap per cluster

- [ ] **Step 1:** Update memory: write `project_for_sale_pages_program.md` (status, hero map, lessons) + MEMORY.md line; update after each cluster.
- [ ] **Step 2:** After all 4 clusters: cluster-wide dup sweep, IndexNow via deploy-verifier flow, and schedule the Fable-5 cleanup pass note (breeder's standing "cleanup over ALL pages at the very end").

---

## Self-review notes

- Spec coverage: skill merge ✓ (Task 1 + analysis section), MFS→CAG conversion ✓, differences vs comparison builder ✓, Sprint 0 mandatory ✓ (Task 6), grill-me ✓ (Task 7), 2+blended strategies ✓, GSC/Bing 6+-word mining ✓ (Task 4 + missing-Queries flag), 5-hero assignment ✓, TOC/KeyTakeaway 5→3 designs ✓, dial+jump-rail restyle ✓, orange stacking tables + bird emojis ✓, image-per-header ✓ (Task 8), contact form Midland pickup + real birds/prices ✓ (Task 9 Step 3), sidebar answer ✓ (Task 5 Step 4), mandatory/competitor/suggested sections ✓ (Task 6 Step 3), build gated on breeder images + explicit start ✓ (Task 8), comparison lessons ✓ (memory citations throughout), CTA buttons + seam divider ✓ (Task 5 Step 3), page clusters + build order ✓.
- Deviation flagged, not buried: the egg page recommendation (Open Flag 1) changes the page's mode and is a breeder decision.
- No placeholder steps: every task names exact files, commands, and gates; page copy itself is intentionally NOT pre-written because the breeder's process forbids writing page content before Sprint 0/0.5 + outline approval.

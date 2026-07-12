# Session Brief — Breeders-Comparison build prep (2026-07-13)

## Status: PREP COMPLETE — page authoring is the next focused session

### ✅ Done this session (committed + pushed)
1. **3 prompt-packs coverage-complete** (`a816ca8`) — breeders/pros-cons/hub PART C: every H2 → image slot + exact OG files.
2. **14 breeders image pairs processed → `public/`** (`7443237`) — 11 infographics + 3 in-body OG (`certified-breeders-african-grey-near-me`, `african-grey-rescue-adoption-documented-handoff`, `mark-teri-benjamin-family-aviary-midland-tx`) + hero (`african-grey-breeder-comparison-hero` + `-480`). All 1408×768 cover, `<95 KB`, `-760.webp` siblings. Source infographics live in `assets/COMPARE-PAGES/ARICAN-grey-COMPARISON/` (folder is mislabeled — contents are the BREEDERS set).
3. **NEW skill `cag-component-refresh`** (the "Refresh Agent") + registered — section-by-section differentiation ledger, invariants, refresh budget.
4. **Uniform-sizing recipe propagated** — IMAGE-DESIGNS §1a (ImageOps.fit 1408×768 recipe), CLAUDE.md, cag-infographic/-generation skills, cag-image-pipeline/-infographic-builder agents.

### 🔒 Decisions locked
- **Build order:** breeders → pros-cons → hub (LAST). Donor = **CvM** (`src/pages/african-grey-vs-macaw/index.astro`, 1491 ln — most polished; §11–§13 contract).
- **HERO refresh (breeder-approved):** single trust hero + credential pill-row — copy LEFT, ONE subject right (`african-grey-breeder-comparison-hero.webp`), pill-row under H1: `USDA-licensed · CITES-documented · PBFD/APV PCR · DNA-sexed`. NOT the two-portrait+vs-roundel species hero. Uses `.hero-imgs` (hero exempt from §1a box).
- **5 signature refreshes (within 3–5 budget):** (1) Quick-Answer → cream panel + left clay rule (not green band); (2) decision fork → 4 doorway cards (INF-1) not Choose-A/B; (3) breeder-types table → 4-tier VERDICT CARDS + green "documented" strip (table stays in DOM for AIO); (4) author → Teri first-person pull-quote lead + byline; (5) metros pills → grouped-by-mode columns, fresh 7-metro set (NOT CvT TX/FL/NY/LA/Chicago/GA/NC, MvF AZ/PA/OH/Miami/Dallas/WA/NJ, cockatoo CO/VA/MI/TN/MN/MO/MD, CvM IL/MA/WI/IN/IA/KY/OR). Shipping cards inherited.

### 📋 Build steps (next session)
1. `cp` CvM donor → breeders slug (old page backed up at `scratchpad/breeders-OLD.astro`; it holds reusable `breeder-comparison.json` data, `verificationChecklist`, `buyerFaqs`, FAQPage schema — MERGE these into the new frontmatter).
2. **Frontmatter:** breeders title/description/canonical (title = 4-part ending `C.A.Gs – <LSI>`, never "Midland TX"); Article + FAQPage schema (NO page-level BreadcrumbList); data arrays for the 4-tier documentation matrix; fresh `shipPlaces`; `tocItems` for the 20-H2 outline.
3. **Body:** author 20 H2 sections per `sessions/comparison-research/african-grey-parrot-breeders-comparison/Recommended-Outline.md` (20 H2 · 20 H3 · 22 H4 · 11 H5 · 6 H6), grounded in Keyword-Universe / Entity-Map / Evidence-Log / Internal-Linking / Strategy. Apply the 5 refresh deltas. Ledger-safe (0/30 USDA audit, $1,700–$3,500, $185/$350, PBFD/APV PCR).
4. **Wire 14 images** to their §-slots per the prompt-pack PART C table (INF-1…11 + hero + certified-breeders §4 + rescue-adoption §7 + Mark owner §16; shipping + reviews reuse existing public/).
5. **Strip** unused donor interactives (size/quiz/budget comparators — species-page tools); keep table-tab toggle + scrollspy. Keep CSS block (donor 1045–1491) + add ~5 refresh-delta rules (hero pill-row, verdict cards, grouped metros, pull-quote, cream quick-answer).
6. **Gates:** `npx astro build` → verify `dist/` → `dup_content_audit.py --headers` + body vs ALL siblings + scam page → `final_page_audit.py --comparison` → clamp sweep 375/640/768/860/1280 (H1 leads) → Lighthouse warm median-of-3 → a11y 100. Preview before commit.
7. Commit + push (main only). Then `generate_sitemaps.py` if slug set changes (it won't — page already exists).

### ⏭ After breeders ships
- Repeat for pros-and-cons (breeder generates its INF set first), then hub (reuses spoke infographics — build LAST).
- **FLAG:** at the very end of all 3 → **Fable-5 cleanup pass over ALL comparison pages + these 3.** (See memory `project_remaining_comparison_packs_ready`.)

## Open Flags
- None blocking. Breeders images are in hand; ready to author on the next go.

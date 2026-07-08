# Build Handoff — /african-grey-vs-cockatoo/ (2026-07-08)

**READ FIRST next session. Do NOT re-run research or grill-me — Sprint 0 is done + approved.**

## Status: research complete, outline APPROVED. Build is GATED on the breeder dropping the ~14 AI infographics.

## Approved 2026-07-08 (breeder)
- **Angles** (ranked): Honesty Moat (lead) → Decision infrastructure → "They outlive you" succession → breeder authority + Pepperberg science → negative counter-positioning.
- **Framework-per-section:** per `2026-07-08-angles-frameworks.md` table.
- **Keyword universe + entity map:** `2026-07-08-keyword-universe.md`.
- **Outline:** 25 H2 / 5 species H3s (Umbrella/Moluccan/Goffin/Galah/Citron) / ~6,500 words, APPROVED as-is — `2026-07-08-section-matrix.md`. Census 1 H1 · 25 H2 · ~30 H3 · ~14 H4 · 7 H5 · 7 H6, no skips.
- **Counter-snippet LOCKED (Option A):** `#1 talking parrot · 40–60 yr companion · 100% CITES-documented · 24-hr reply`.
- **Components:** Rule-0 set (Hero C, TOC 1C, jump 2B, Takeaways 3C, Quick-Answer 4B **clay-recolored** not forest, Compare-E **new flow** + mobile tab-pill, Scorecard = **AI infographic** per §11 (not HTML dots), FAQ 7C top-3-open, Seam 8A, Buttons 9B, Newsletter 10A+B+C top/mid/bottom like MvF, Byline 11C, Stat cards 12B/12C, Available 13B + 5 badges, Pair/Eggs 14B duo, Shipping 15B timeline + $200 deposit, Health 16B minis, Pull-quote 17B, Blog 18B, contact form).

## OPEN — required before/at build
1. **Breeder to generate & drop the ~14 Gemini infographics** from `2026-07-08-image-prompt-pack.md` (Part 2). The 5 species subsections + hero + trust + shipping + bird/pair/egg + blog are already covered by provided OG photos (Part 1). Until infographics land, analytical sections have no image → cannot pass the "every H2/H3 has an image" gate.
2. **Claim a fresh 7-location pill set** — verify real live slugs in `src/pages/` (CvT owns TX/FL/NY/LA/Chicago/GA/NC; MvF owns AZ/PA/OH/Miami/Dallas/WA/NJ). Update memory registry.
3. **Confirm live /available/ birds** from `clutch-inventory.json` at build time for §23 cards.

## Build order next session (after images land)
1. Preview-before-apply on Hero C + one species subsection for breeder OK.
2. Build `src/pages/african-grey-vs-cockatoo/index.astro` section-by-section to the approved matrix (REBUILD — the on-disk 390-line page is thin).
3. Hero fix: push both birds BACK from the VS circle (portrait clip-mask+zoom / landscape object-position); `.portrait` on square OGs; `-760` siblings + srcset on every image.
4. Prose must be page-unique (dup_content_audit.py ≥12-word gate vs CvT + MvF).
5. Gates: `astro build` → verify in `dist/` → `final_page_audit.py --comparison` → keyword-verifier + anti-AI + non-commodity + Lighthouse warm-median-of-3.
6. `generate_sitemaps.py` → commit + push to `main` (auto-deploys).

## Sources (all fetched 2026-07-08, real)
Lafeber-Pepperberg contrafreeloading · NIH PMC9381342 (grey hypersensitivity pneumonitis) · Parrot Trust Scotland / AllergyCosmos (powder-down) · Britannica (intelligence) · Reddit r/parrots + avianavenue + parrotforums + backyardchickens (owner language) · manual research data (bite-force).

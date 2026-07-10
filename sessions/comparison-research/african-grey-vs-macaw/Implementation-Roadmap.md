# Implementation Roadmap — /african-grey-vs-macaw/

## Status
Outline + A/B/C distribution matrix presented for approval 2026-07-10 (see chat). No code written yet per Heading Hierarchy Outline Gate + Visual-First Workflow. Hero pairing (Scarlet vs Blue-and-Gold) shown in visual-companion artifact, Option B recommended.

## Confirmed decisions this session
1. Stale grey-vs-cockatoo content in the research file (lines 1–63) discarded — components chosen fresh.
2. "222+ sections" read as 22+ (typo), targeting ~26 H2s matching sibling pages.
3. Species subsections = all 11 with real provided photos (not the original 10-item research list).
4. Missing visual slots (hero, infographics, cards) sourced via AI generation + existing site-asset reuse, not blocked on new breeder photography.

## Build sequence from here
1. **This session:** outline + matrix approval (blocking gate)
2. Build page section-by-section on `src/pages/african-grey-vs-macaw/index.astro`, porting structural patterns from `congo-vs-timneh-african-grey/index.astro` (closest proven reference) but every header/paragraph rewritten page-unique
3. Generate AI images for the non-photo slots (bite-force matrix, decision flowchart, nutrition graphic) via `scripts/generate_nb_image.sh`
4. Build + verify the 3 interactive tools in the browser preview (size comparator, lifestyle quiz, budget estimator) — click-through test, console-clean, before marking done
5. Run the full pass-gate list in Search-Quality-Checklist.md
6. Preview in browser (desktop + mobile), screenshot proof
7. Commit + push to `main`

## Word budget allocation (target 6,500–7,000)
- 11 species subsections: ~1,600–2,000 words (the size differentiator vs siblings)
- Deep-dive Grey + Deep-dive Macaw(general): ~900 words
- Bite force + nutrition (macaw-unique sections): ~700 words
- Cost/scorecard/lifestyle-match/quiz: ~900 words
- CITES/shipping/available/first-30-days/myths/lifecycle: ~1,400 words
- Quick-answer/takeaways/comparison-table/trust/FAQ/CTA/related: ~1,200 words

## Open item carried forward
Bite-force Newton/PSI figures need a real citable source before publish — flag during the writing pass, don't ship an uncited number even though the research doc presents them as fact.

# 2026-09-10 — Homepage close-out + component variations

## Brief (restated)
Goal: close open flags 1/2/4/6 from the 2026-09-09 evidence pass on `/` only; fix IMG-oversized, IMG-dup-alt, NAV-scroll-margin; fix the oklab contrast harness bug; run every gate on `/`; deliver 3×3 component variations on a design canvas + a component library artifact + a skill.
Scope: `src/pages/index.astro`, `data/reviews.json`, `HeroV3.astro`, `tests/render/checks/a11y.ts` + 2 fixtures, `scripts/evidence_audit.py` (per-page title cap), `.claude/agents/cag-homepage-builder.md`. Nothing else on the site.
Gates: `npm run test:render:meta` → `npm run test:render:pages` → hardening scan → final_page_audit --type home → aeo → evidence → seam → dup → quality_report → pytest.
Done: gates green or overridden visibly; built, committed, pushed, IndexNow `/` submitted; artifacts published; canvas published; skill registered.
Out of scope: blog titles, Rule 21 text, budget calibration, sitewide srcset, any other page.

## Open Flags

# 2026-09-10 — Homepage close-out + component variations

## Brief (restated)
Goal: close open flags 1/2/4/6 from the 2026-09-09 evidence pass on `/` only; fix IMG-oversized, IMG-dup-alt, NAV-scroll-margin; fix the oklab contrast harness bug; run every gate on `/`; deliver 3×3 component variations on a design canvas + a component library artifact + a skill.
Scope: `src/pages/index.astro`, `data/reviews.json`, `HeroV3.astro`, `tests/render/checks/a11y.ts` + 2 fixtures, `scripts/evidence_audit.py` (per-page title cap), `.claude/agents/cag-homepage-builder.md`. Nothing else on the site.
Gates: `npm run test:render:meta` → `npm run test:render:pages` → hardening scan → final_page_audit --type home → aeo → evidence → seam → dup → quality_report → pytest.
Done: gates green or overridden visibly; built, committed, pushed, IndexNow `/` submitted; artifacts published; canvas published; skill registered.
Out of scope: blog titles, Rule 21 text, budget calibration, sitewide srcset, any other page.

## Open Flags

- evidence_audit term-budget WARNs on `/` for USDA/CITES/DNA/vet/PBFD/hatch are breeder-accepted (2026-09-10: "these are entities Google needs to see"). Not a defect. Revisit when Sprint 0 calibrates budgets.
- B2 touched one shared component: `OwnerCard.astro` `scroll-mt-20` → `scroll-mt-28` (both consumers sit under the same 96px header; 80px was wrong on both). Rendered output of `/trusted-african-grey-parrot-breeders/` changed → submit it to IndexNow with `/` at ship (Task C2).

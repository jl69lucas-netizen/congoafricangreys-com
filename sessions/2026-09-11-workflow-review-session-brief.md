# Session Brief — 2026-09-11 · Workflow Review (Board-First)

**Planned:** research only, no code. Is the 7-sprint pipeline good? Two better workflows. Cowork, routines and `/loop` fit. A visual-SEO board that gives 3–5 component options per section straight from the outline.

**Committed:** `fdd895c9` docs(workflow): sprint pipeline review — `docs/artifacts/cags-sprint-pipeline-review.html` + `.md`
→ artifact https://claude.ai/code/artifact/e961edb9-4050-4a33-a793-1832bc48a7f2. Pushed; `origin/main` confirmed.

**Uncommitted, pre-existing (NOT from this session, left untouched):**
- 6 modified `.claude/skills/*/SKILL.md`
- 5 deleted `assets/COMPARE-PAGES/*`
- untracked `New-BING-AUGUST-26.csv`, `google-agcare-snapshot.md`, `assets/brand/CAGs-BLOG-POSTS/`, `assets/brand/COMPARE-PAGES/`

## Decisions Log
- **Breeder picked Workflow A, Board-First.**
- **First spec: the Page Board system.** Then automation lanes, then the `WORKFLOW.md` rewrite.
- **Queue after the workflow work:**
  - Page A `/buy-african-grey-parrots-with-shipping/`
  - Page B `/african-grey-parrots-for-sale-near-me/`
  - hub `/african-grey-parrots-for-sale/`
  - then all location, state and city pages (Cluster Wave).
- **The three pages are the pilot.** A and B (outlines approved, combos 11/12 locked) test the asset-slot lane; the hub gets the first real Page Board.
- **Image generation authorized.** When the breeder drops the Gemini key, generate the 14 Part-2 images from the 2026-08-10 prompt pack. No manual generation. Runbook: memory `project_gemini_image_run_ready`.

## What's Next
1. **Gemini key lands:** clipboard into `.google-key`, verify the model, fix the script's hardcoded 9:16 to 16:9, smoke-test A-INF-1, generate the rest. Put all 14 on one contact-sheet artifact for approval. Never generate the Part-1 named birds, heroes or documents.
2. **Resume brainstorming the Page Board system:** clarifying questions → 2–3 approaches → design → spec `docs/superpowers/specs/2026-09-1x-page-board-system-design.md` → writing-plans.
3. **Build Pages A and B against measured slots** (2026-08-10 plan, Task 8 onward), with Part-1 photos from the breeder. Page B ships before the three near-me 301s. Then the hub through its first Page Board.
4. **Quick wins, any time:**
   - the four `WORKFLOW.md` drift lines (176, 333, 807, Sprint 2 step 1.5);
   - the competitor-price routine;
   - the weekly GSC desktop task (the `gscServer` MCP is configured but untested).

## Unfinished
- Brainstorming for the Page Board system stopped at clarifying questions. The asset-status question was dismissed and is superseded by the Gemini plan. No spec written yet.

## Discovered This Session
- **Page rework rate** 20.8% → 8.9%; checker self-repair 4.0% → 17.8% (`data/quality/rework-ledger.json`).
- **All 10 recent pages show identical `A11Y:3` / `DUP:3` first-run rows.** That looks like a harness signature. Verify on a built page before acting.
- **Weekly monitoring never ran:** `data/competitor-prices.json` has 0 snapshots; the LLM Visibility column in `top-pages.md` has never held a number; the GSC exports date from 2026-04-27.
- **`scripts/generate_nb_image.sh` defects:** hardcodes `imagen-3.0-generate-001` and `aspectRatio 9:16`; `cwebp` is not installed, so the WebP step skips.
- **`data/cag-ontology.json` does not exist** and graphify has never been run. Both are prerequisites for the entity board.
- **Checked against the docs:**
  - Routines push only to `claude/*` branches, via draft PRs, with a 1-hour minimum interval.
  - `/loop` is session-scoped, and recurring tasks expire after 7 days.
  - `/goal` has a separate model judge the condition after each turn.
  - Cowork is on Pro, Max, Team and Enterprise and has scheduled tasks.
- **The outline-gate file header still says "AWAITING BREEDER APPROVAL",** but the record says approved. Treated as approved.

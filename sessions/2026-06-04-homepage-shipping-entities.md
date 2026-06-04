# Session Log — 2026-06-04 · Homepage shipping entities, sitemap/llms fixes, divider logo

Multi-task request: agent routing review + add First-Person Voice to all agents + 6 tasks
(shipping entities/flight-nanny, 5-step infographic, internal links, sitemap+llms, health
section, divider logo). Kept here as a good+bad record so we don't repeat mistakes.

## What shipped (all committed + pushed → live)
- **First-Person Voice → all 66 agent `## Golden Rule`** (idempotent `scripts/add_first_person_golden_rule.py`). Was only 4/66.
- **Sitemap 13 → 100 URLs** (`scripts/generate_sitemaps.py`, filesystem-driven; fixed cross-shard dupes + phantom `/...-california/`, `/...-south-carolina/`).
- **llms.txt**: Appendix II → I (5×), real pricing, removed dead links, added flight-nanny tier.
- **Homepage** (`src/pages/index.astro`): flight-nanny delivery card (from $750, quoted/route); 4→5-step infographic with whitespace fix; Concept-A logo seams ×6; 5 internal links; health CTA re-point + health-guarantee link.

## What went WELL (keep doing)
1. **Grounded before answering** — read homepage + data + sitemap + llms + PRODUCT/DESIGN before any claim. Surfaced two bugs the user didn't ask about (llms Appendix II, sitemap 13/91).
2. **AskUserQuestion for genuine decisions** (flight-nanny price, divider concept) instead of inventing — honored "never fabricate" + Recommend+Why.
3. **Verified in `dist/` + browser**, not source greps. Confirmed 1 (not duplicated) FAQPage schema, 0 `&lt;svg` leaks.
4. **Filesystem-driven, idempotent scripts** — both new scripts re-run safely and stay correct as pages change.
5. **Honest flagging** — said "5 sequential steps isn't truthful, home delivery is an alternative" and "7 links exceeds the 3/session guideline (here's why it's OK)".

## What went BADLY (don't repeat — now in memories)
1. **Fought the preview screenshot tool** (resets scroll to 0) for ~4 calls → [[feedback_preview_screenshot_workflow]]: hide DOM above target + scrollTo(0,0).
2. **Measured responsive layout at the wrong viewport** — navigate reset viewport to mobile, read 1292px instead of 181px. Resize to desktop BEFORE measuring.
3. **grep `$` escaping** — `grep -o "from \$750"` matched nothing ($ = EOL anchor); use `grep -oF`. → appended to [[feedback_verify_rendered_not_source]].
4. **"Everything up-to-date" panic** — auto-push hook had already pushed; verify with `git log origin/main..HEAD`. → [[feedback_always_push_after_commit]].

## Deferred / open
- **Adoption links** (`african-grey-adoption`, `african-grey-parrot-adoption-cost`) → homepage `#pricing`, 2nd pass (would push #pricing past the link cap). User approved deferral.
- Flight-nanny "from $750 · quoted per route" is the price the breeder set this session — keep `data/financial-entities.json` + llms.txt in sync if it changes.

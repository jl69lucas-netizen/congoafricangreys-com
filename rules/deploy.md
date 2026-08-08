# Where work lands and how it ships

Rules moved out of `CLAUDE.md` on 2026-08-02 (Phase 4). **The rule text is verbatim.**

`enforced:` says what actually holds the rule up.
`test` — a committed check fails when the rule is broken. `judgment` — no mechanical
decision procedure exists, and `data/quality/rule-index.json` records why.
`untested` — **a deletion candidate**: it is asserted and nothing enforces it.
`scripts/quality_report.py` §5 lists every one of those on every run, which is the point.


---
id: src-pages-is-deployed
enforced: untested
family: GATE
---

- **src/pages is deployed** — All HTML page edits MUST go to `src/pages/<slug>/index.html` or `src/pages/<slug>/index.astro`. The `site/content/` directory is a staging area; it does NOT get built directly. If both exist, `src/pages/` is authoritative.

---
id: always-push-after-build
enforced: judgment
family: GATE
---

- **Always commit + push after build** — After any agent or skill completes a build/edit, commit and `git push` immediately. Push = deploy (GitHub Actions → Cloudflare Pages, auto on push to `main`). Do not leave finished work uncommitted or unpushed. Applies to all agents.

---
id: indexnow-tooling-intact
enforced: test
family: GATE
---

- **IndexNow-submit at the end of EVERY page build (ALWAYS — breeder, 2026-08-08)** — After the push has deployed and the page returns HTTP 200 live, submit it: `python3 scripts/indexnow_submit.py <slug>` (or `npm run indexnow -- <slug>`; `--changed` derives slugs from git). **Order matters — submit only after the deploy is live**, because the script verifies each URL returns 200 and refuses dead ones; submitting before Cloudflare finishes building asks Bing to crawl the old copy. **Submit every page whose rendered output changed, not just the one you edited** — a shared-component edit propagates: the 2026-08-08 Timneh taxonomy fix touched `CityPageLayout.astro` and changed 15 city pages plus the 3 edited directly, so all 18 were submitted. The key is read from `public/<key>.txt`; never type it inline.

  **What the test enforces, precisely.** No check can observe that an external POST to `api.indexnow.org` happened — that is a process fact. What `tests/render/meta.spec.ts::IndexNow tooling is intact` does enforce is the reason this step **never once ran before 2026-08-08**: the procedure in `skills/cag-indexing.md` STEP 4 was broken three ways by the MFS→CAG find/replace — a placeholder key (`a1b2c3d4…african grey parrots`) while the real key sat correct in the same file's own table, a sitemap regex whose domain contained **spaces**, and a `SITE_ROOT` pointing at `/Users/apple/Downloads/MFS/site2`, **a path that exists**, so a run would have read another project's sitemaps. Any execution would have POSTed an empty `urlList` under an invalid key and printed a success line. The four assertions fail if the script goes missing, if a key is hardcoded again, if the key file's body stops matching its filename (IndexNow's own 403 condition), or if live code in the skill points back at the MFS project. All three historical defects were mutation-tested against these assertions on 2026-08-08 and each one failed the build as intended. **The process step is the breeder's standing instruction; the test is what keeps the step performable.**

---
id: work-on-main-not-branches
enforced: judgment
family: GATE
---

- **Work directly on `main` — NEVER build on feature branches (ALWAYS) — applies to every agent, skill, and build** — All CAG work happens on `main`. Do NOT create or check out feature branches (`git checkout -b …`) for page builds or edits unless the user *explicitly* asks for one. **Only `main` auto-deploys** (Cloudflare Pages builds on push to `main`), so finished work committed on any other branch gets pushed to origin but **never goes live — it strands at HTTP 404** while looking "done." (This happened 2026-06-18: 6 `/available/` bird pages sat live-404 on `feat/bird-listing-pages` until ff-merged to `main`.) The breeder does not want to open PRs or merge anything by hand. Start every task by confirming you're on `main` (`git checkout main`); commit + `git push origin main` after each build = one-step deploy. If you ever find finished work on a non-`main` branch, ff-merge it into `main` and push immediately.

---
id: skills-are-registered
enforced: untested
family: GATE
---

- **Skills are registered & Skill-invokable (ALWAYS)** — Every `skills/<name>.md` (and `skills/<name>/SKILL.md` dir-skill) is the canonical source, and is mirrored into `.claude/skills/<name>/SKILL.md` by `scripts/register_skills.py` so the **Skill tool / `/<name>`** can load it by `name:`. `skills/` is still the file everything Reads; `.claude/skills/` is generated — never hand-edit it. **After adding, renaming, or deleting any skill, run `python3 scripts/register_skills.py --copy` and commit `.claude/skills/`** (registration loads only at session start — a new skill is invisible until the next session). `scripts/health-sweep.sh` fails if a skill is unregistered or a copy mirror drifts. Cause of the 2026-06-28 "Unknown skill: cag-final-page-pass / cag-blog-post" failures: the 48 skills sat in `skills/` (a folder the loader never scans) and were never registered.

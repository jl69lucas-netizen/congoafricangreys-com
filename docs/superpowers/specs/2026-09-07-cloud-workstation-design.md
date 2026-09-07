# CAG Cloud Workstation — Design

**Date:** 2026-09-07
**Status:** Approved in brainstorming, awaiting spec review
**Goal:** Do every kind of CAG work (research, page builds, render gates, CRO / visual review,
deploy, IndexNow) from a browser-only library computer via Claude Code on the web
(claude.ai/code), with the 2018 Mac demoted to a client that pulls before it works.

## 1. Problem

The CAG "brain" (68 agents, 70 skills, 4 commands, CLAUDE.md, `rules/`, `scripts/`,
`tests/`) is already in git and in sync with `origin/main`. What is **not** portable:

| Item | Where it lives today | Cloud impact |
|---|---|---|
| Auto-memory (187 files + MEMORY.md) | `~/.claude/projects/-Users-apple-Downloads-CAG/memory/` | Every cloud session starts with zero memory |
| 16 global skills (graphify, ckm-*, ui-ux-pro-max, extract-design, google-agents-cli-*) | `~/.claude/skills/` | Missing in cloud |
| Plugins (superpowers, impeccable, compound-engineering, karpathy, official plugins) | `~/.claude/settings.json` `enabledPlugins` | Missing in cloud; `/plugin` does not work in web sessions |
| API keys (`.google-key`, Firecrawl, IndexNow key) | Loose files / MCP auth on the Mac | Must become cloud-environment secrets |
| Node deps + Playwright browsers | `node_modules/` | Reinstalled per session by a setup script |

Confirmed against the official docs (2026-09-07): the cloud sandbox ships Node, Python 3,
git and headless Chromium; environment config lives in the claude.ai/code UI (network
level, env vars / secrets, setup script); sessions clone the current branch and may push
straight to `main`; `autoMemoryDirectory` in settings redirects auto-memory; plugins load
only from `.claude/settings.json` `enabledPlugins` + `extraKnownMarketplaces`.

## 2. Decisions (from brainstorming)

1. **Browser-only target.** Nothing is installed on the library machine.
2. **Full pipeline in the cloud**, builds included. Visual review uses headless Playwright
   screenshots + Artifacts instead of the desktop Browser pane.
3. **Push straight to `main`.** The approval gate stays where the sprint model already puts
   it: preview-before-apply inside the session. No PR step.
4. **The repo is the single source of truth.** The Mac pulls before every session.
5. **Repo-weight reduction is a separate follow-up**, measured here, decided later.

## 3. What moves into the repo

### 3.1 Memory → `.claude/memory/`
- Copy the whole memory directory (MEMORY.md + 187 topic files) to `.claude/memory/`.
- Add to `.claude/settings.json`: `"autoMemoryDirectory": ".claude/memory"`.
  (Verify during implementation whether the key accepts a repo-relative path; if it
  requires absolute, fall back to a one-line symlink step in the setup script and on the
  Mac.)
- Leave the old `~/.claude/projects/.../memory/` in place until the Mac confirms it reads
  the new location; then delete it to avoid a split brain.
- Memory becomes versioned. Commits touching only `.claude/memory/` use the prefix
  `memory:`.

### 3.2 Global skills → `.claude/skills/`
- Copy all 16 from `~/.claude/skills/`. Verified: zero name collisions with the 70 project
  skills.
- Register them the same way project skills are registered
  (`scripts/register_skills.py --copy` if it covers the new folders; otherwise document
  the manual step).

### 3.3 Plugins → `.claude/settings.json`
Declare only the plugins CAG work actually uses. Copy the marketplace sources verbatim from
`~/.claude/settings.json`.

Keep: `superpowers@superpowers-dev`, `impeccable@impeccable`,
`compound-engineering@compound-engineering-plugin`,
`andrej-karpathy-skills@karpathy-skills`, and from `claude-plugins-official`:
`searchfit-seo`, `frontend-design`, `firecrawl`, `cloudflare`, `playwright`,
`chrome-devtools-mcp`, `skill-creator`, `claude-md-management`, `commit-commands`,
`pr-review-toolkit`, `code-simplifier`, `remember`.

Drop (not CAG, or fail to connect today): miro, auth0, windsor-ai, vercel, telegram,
imessage, gitlab, firebase, agent-sdk-dev, playground, mcp-server-dev, github plugin
(git itself covers it), the duplicate `superpowers@claude-plugins-official`.

### 3.4 Settings hygiene
- `.claude/settings.local.json` is currently tracked and holds ~100 machine-specific
  permission entries. Untrack it (add to `.gitignore`), and move the few generic allows
  the cloud needs (`npx playwright *`, `python3 *`, `npm run *`, `git *`) into
  `.claude/settings.json`.
- Secrets never enter git. `.gitignore` already blocks `.google-key`, `.openai-key`,
  `.anthropic-key`, `.env*`.

## 4. The cloud environment

One environment named **CAG** at claude.ai/code:

| Setting | Value |
|---|---|
| Network access | Trusted (site, IndexNow, Gemini, Firecrawl, CDNs, competitor sites all need outbound HTTPS) |
| Secrets | `GEMINI_API_KEY`, `FIRECRAWL_API_KEY`, `INDEXNOW_KEY` (names to match what the scripts read; audit during implementation) |
| Setup script | `bash scripts/cloud-setup.sh` |

`scripts/cloud-setup.sh` (versioned in the repo):
1. `npm ci`
2. `npx playwright install chromium` (+ `--with-deps` if the sandbox lacks libs)
3. `pip3 install pillow` (the only non-stdlib Python import across `scripts/*.py`)
4. Write secrets from env vars into the key files the scripts expect (e.g.
   `GEMINI_API_KEY` → `.google-key`), so no script changes are needed.
5. `git config user.name / user.email` for the CongoAfricanGreys identity.
6. Print a one-screen readiness report: node/python/chromium versions, agent count,
   skill count, memory file count, plugin list.

## 5. Workflow changes

- **Mac session start:** `git pull` first, always. A tiny `scripts/mac-session-start.sh`
  does pull + prints the same readiness report.
- **Cloud session start:** the setup script runs automatically; the readiness report is
  the first thing to read. If any count is wrong, stop and fix before building.
- **Visual work in the cloud:** screenshots via the existing Playwright harness
  (`npm run test:render:pages` already captures at 375/768/1280), saved to the
  scratchpad and surfaced as Artifacts. The desktop Browser pane, Chrome extension and
  iOS simulator are Mac-only; skills that name them fall back to Playwright.
- **Deploy:** unchanged. Commit, push to `main`, wait for Cloudflare, then
  `python3 scripts/indexnow_submit.py <slug>`.
- **CLAUDE.md** gains a short "Two machines, one repo" paragraph under the deploy model:
  pull before work, memory lives in `.claude/memory/`, cloud setup is
  `scripts/cloud-setup.sh`.

## 6. Repo weight (measured, not fixed here)

`.git` = 477 MB, `assets/` = 756 MB. Every cloud session clones this. Implementation
records the cold-clone time in the cloud once, and the top-20 largest blobs in history
(`git rev-list --objects --all | git cat-file --batch-check`). Shrinking (Git LFS for
brand masters, or history rewrite) is a follow-up spec; the trigger to write it is
cold-clone time above ~3 minutes.

## 7. Bridge option (optional, day one)

Until section 4 is live, `/remote-control` on the Mac lets a claude.ai/code browser tab
drive the local session. Requires the Mac awake and online. Not part of "done".

## 8. Definition of done

A fresh cloud session in the CAG environment:
1. Readiness report shows 68 agents, 86 skills (70 + 16), the declared plugins, and
   187+ memory files.
2. `npm run test:render:meta` passes.
3. `npm run test:render:pages` runs at all three widths for at least one page and
   produces screenshots.
4. `npx astro build` succeeds.
5. A trivial commit (touch a memory file) pushes to `main`; Cloudflare deploy goes green;
   the Mac pulls it and its next session reads the updated memory.
6. `python3 scripts/indexnow_submit.py` runs against a real slug without error.

## 9. Out of scope

- Shrinking git history / LFS migration (section 6 follow-up).
- Re-authorizing MCP servers that already fail locally (miro, auth0, windsor, vercel,
  gitlab, firebase).
- Any page content work.
- Replacing Mac-only visual tooling with cloud equivalents beyond Playwright screenshots.

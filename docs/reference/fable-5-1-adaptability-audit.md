# C.A.Gs Agent System — Fable 5.1 Adaptability Audit

*Audited 2026-09-07 against the tree at `claude/fable-5-1-adaptability-audit-isjqbo`. Every count below was measured on disk; nothing is inferred. Frontmatter facts were checked against the current Claude Code docs (sub-agents.md, skills.md, model-config.md, scheduled-tasks.md).*

*Published Artifact (copy buttons per section): https://claude.ai/code/artifact/c18dc7df-efea-4cb7-91d4-ab65dec643ab — source `docs/artifacts/fable-5-1-adaptability-audit.html`.*

## 0 · Verdict

**The system works on Fable 5.1 today, but it is running on stale plumbing.** 68 agents, 70 skills, the 7-sprint pipeline and the registry-driven tier scripts all load and pass their own checks (`verify_model_tiers.sh` 68/68, `register_skills.py --check` 70/70). What has drifted is everything the last two model flips (4.7 → 4.8 → Opus 5) left behind: dead tier names in the orchestrator routing tables, a hand-rolled effort mechanism the harness now supports natively, a fork mechanism that was never a real Claude Code feature, and a Golden Rule block that says `site/content/` ships while `CLAUDE.md` says `src/pages/` does.

Fable 5.1 changes the operating assumption in one way that matters more than the model id: **it runs autonomously.** The harness now tells the model the breeder is not watching and that a mid-task question blocks the work. Forty-six of the 68 agents open with "Ask user: which mode?", and `grill-me` asks 13–14 questions one at a time. Those were the right design for an interactive Opus 4.8 session. On Fable 5.1 they are the first thing that stalls.

| Area | Measured state | Fable-ready? |
|---|---|---|
| Agent model field | 68 × `model: claude-opus-5` | Valid id, wrong model; no agent can run Fable |
| Effort mechanism | 68 × native `effort:` + 42 prose `EFFORT:START/END` blocks | Native field works; prose is redundant |
| `dynamic_workflow:` | 68 agents | Not a recognized field; harmless, inert |
| Orchestrator routing | 3 tables cite `opus47_high` / `haiku_medium` / `claude-opus-4-7` / `claude-haiku-4-5` | Dead tiers, not in registry |
| Parallelism | `CLAUDE_CODE_FORK_SUBAGENT=1` in 3 agents + 1 doc | Undocumented; not a real mechanism |
| Delegation | 0 of 68 agents carry the `Agent` tool | Orchestrators cannot spawn anything |
| MCP tools in `tools:` | 17 agents list firecrawl / playwright-plugin / chrome-devtools / Claude-in-Chrome | None exist in this session; silently dropped |
| Startup interviews | 46 agents "Ask user" before doing anything | Blocks autonomous runs |
| Confidence Gate | 41 agents carry BOTH "stop and ask" AND "do NOT dead-stop" | Self-contradicting |
| Golden Rule boilerplate | 351,742 bytes duplicated across 68 files | ~1,300 tokens per invocation, drifts |
| Content root in agents | 58 say `site/content/`; CLAUDE.md says `src/pages/` | Stale in the majority |
| Hard-coded Mac path | 6 agents + 10 skills use `/Users/apple/Downloads/CAG/` | Breaks every remote session |
| Skill `tools:` field | 42 skills | Not a skill field; the real one is `allowed-tools` |
| Skill descriptions | 8 under 150 chars, 1 with no trigger phrase at all | Weak auto-invocation |
| Scheduling | `/schedule` "every Sunday" in 2 agents | Not a command; use CronCreate / Routines |
| Docs | WORKFLOW §Model Tier System + system-registry still say Opus 4.8 | Stale |
| Secret | A Cloudflare API token sits in tracked `.claude/settings.local.json` | Rotate and purge now |

## 1 · Model And Effort — What The Harness Actually Reads

Confirmed against sub-agents.md and model-config.md:

- `model:` accepts aliases (`opus`, `sonnet`, `fable`, `haiku`), full ids (`claude-fable-5-1`, `claude-opus-5`), `best` and `inherit`.
- `effort:` **is native** with values `low | medium | high | xhigh | max`. The registry's own note ("effort is NOT a native Claude Code field") is out of date, and so is the 42-agent prose directive that `apply_model_tiers.py` injects to compensate.
- `dynamic_workflow:` is not among the recognized fields. It is inert.
- In `SKILL.md`, `model:` and `effort:` **do** take effect, and the tool field is `allowed-tools` / `disallowed-tools`. The `tools:` key present in 42 skills does nothing.

**Three options for the model line, one recommended.**

| Option | What changes | Trade-off |
|---|---|---|
| A · Pin `claude-fable-5-1` in all 68 | Registry tier `model` → `claude-fable-5-1`, re-run `apply_model_tiers.py` | Fourth flip in four months; the next release repeats this audit |
| **B · `model: inherit` in all 68 (Recommended)** | Registry tier `model` → `inherit`; the session's model (Fable 5.1 today) drives every agent; `effort` stays the cost lever | Loses the option of a cheaper model for the 26 mechanical agents unless the *session* runs on it |
| C · Split: `fable` for max/high, `sonnet` for medium | Two model values in the registry | Reintroduces the two-model matrix the 2026-06-04 plan deliberately collapsed |

**Why B.** The registry history is 5 tiers → 3 tiers → one model, flipped three times (`docs/superpowers/plans/2026-06-04-…opus48-upgrade.md`, then commit `90130c1` for Opus 5). Every flip was a model-name edit with zero behavioural change, because all 68 agents already run on one model. `inherit` removes the edit permanently: the breeder picks the model at session launch, the agents follow. `effort` (which the harness now honours natively) remains the only per-agent lever, which is exactly what the 2026-06-04 plan argued for. The named trade-off is real but currently unused: nothing in the system runs a cheaper model today.

**Effort tiers stay as they are** (16 max · 26 high · 26 medium; the docs say 15 / 25 / 26, which was true at 66 agents). Consider `xhigh` for the three orchestrators and the two audit agents (`cags-comprehensive-page-audit-system` chain, `cag-final-page-pass`) rather than `max`, and measure.

### 1a · Concrete edits

```
data/agent-registry.json
  _meta.tiers.opus48_max    → { "model": "inherit", "effort": "max" }   rename tier → "tier_max"
  _meta.tiers.opus48_high   → { "model": "inherit", "effort": "high" }  rename tier → "tier_high"
  _meta.tiers.opus48_medium → { "model": "inherit", "effort": "medium" } rename tier → "tier_medium"
  _meta.description: drop "effort is NOT a native field"; record the 2026-09-07 decision

scripts/apply_model_tiers.py
  stop writing dynamic_workflow: (move the flag to the registry entry only)
  stop injecting the EFFORT:START/END prose block; strip existing blocks on next run
  keep the idempotency fixture (tests/test_apply_model_tiers_idempotent.py) green

scripts/route.py + the 3 orchestrator "Dynamic Workflow Routing" tables
  opus48_max / opus47_high / haiku_medium → tier_max / tier_high / tier_medium
  drop the "claude-opus-4-7 / claude-haiku-4-5" model column entirely

docs/reference/WORKFLOW.md §Model Tier System, docs/reference/system-registry.md §Model Tiers
  "Opus 4.8 (claude-opus-4-8)" → "the session model (model: inherit); effort is the lever"
  counts 15/25/26 → 16/26/26; "66 agents" → 68
```

## 2 · Parallelism And Delegation — The Fork That Never Existed

`cag-batch-rebuilder`, `cag-location-builder` and `cag-self-update` instruct the model to `export CLAUDE_CODE_FORK_SUBAGENT=1` and claim a "~90% cheaper" prompt-cache inheritance. That variable is not documented anywhere in Claude Code. Under Opus 4.8 this failed quietly: the orchestrator wrote pages itself, sequentially. Under Fable 5.1 it is worse, because **no agent file lists the `Agent` tool**, so even a correctly written orchestrator has no way to spawn a specialist.

What exists today, in order of fit:

1. **The `Agent` tool**, multiple calls in one message, one per state / page / audit dimension. This is native fan-out and is how Sprint 0's three tracks should run. Requires `Agent` in the orchestrator's `tools:`.
2. **`/subtask`** for a fork that inherits the parent's context (the thing the env var was imagined to do).
3. **The `Workflow` tool** (deterministic `agent()` / `parallel()` / `pipeline()` scripts, opt-in only via "use a workflow" or `ultracode`). This is the right shape for the 22-state location batch and the 30-competitor intel sweep, but it must be requested by the breeder in their own words each time.
4. **Routines / `CronCreate`** for the weekly jobs. `/schedule` is not a command.

### 2a · Concrete edits

```
.claude/agents/cag-batch-rebuilder.md, cag-content-architect.md, cag-structure-architect.md
  tools: [Read, Write, Bash, Agent]
  delete "## Fork Subagent Mode" + every CLAUDE_CODE_FORK_SUBAGENT mention
  replace with: "Dispatch: one Agent call per page in a single message; state the routing tier
  for each; for 10+ pages ask the breeder once whether to run it as a Workflow (opt-in)."

.claude/agents/cag-location-builder.md
  drop "supports fork-parallel execution — parent spawns one child per state"; the parent
  (batch-rebuilder) owns dispatch

.claude/agents/cag-rank-tracker.md, cag-self-update.md
  "/schedule every Sunday" → "a Routine (create_trigger, cron 0 13 * * 0 UTC) that opens a fresh
  session with this agent's prompt"; never claim to be scheduled unless list_triggers shows it

docs/reference/WORKFLOW.md Sprint 0 "Parallel Tracks"
  name the mechanism: three Agent calls in one message, results merged by the parent
```

## 3 · Tools — What The Agents Ask For Versus What Is There

| MCP prefix in `tools:` | Agents | Present in this session |
|---|---|---|
| `mcp__plugin_playwright_playwright__*` | 14 | No |
| `mcp__firecrawl-mcp__*` | 10 | No |
| `mcp__plugin_chrome-devtools-mcp_chrome-devtools__*` | 3 | No |
| `mcp__Claude_in_Chrome__*` | 1 | No |
| `WebFetch` / `WebSearch` | 1 (`cag-self-update`) | Yes |
| `mcp__github__*`, `mcp__Higgsfield__*` | 0 | Yes |

Unknown tool names are dropped without an error, so in a remote session `cag-competitor-intel` has Read, Write and Bash and nothing else. The Golden Rule already says "use Claude Code and Playwright CLI first", and Chromium plus Playwright are pre-installed here, so the fallback exists; it just is not written into the agents that need it.

**Edit:** every agent that lists an MCP browser tool gets an explicit ladder in "On Startup": (1) `npx playwright` script against the pre-installed Chromium, (2) `WebFetch` / `WebSearch` (add both to `tools:`), (3) the MCP tool if `ToolSearch` finds it. `cag-image-generation` and `cag-photo-ingest` should name `mcp__Higgsfield__*` explicitly, since that server is the one that is actually connected.

## 4 · Autonomy — Where Fable 5.1 Will Stall

Fable's operating instructions say: the user is not watching; asking "which mode?" blocks; make routine calls yourself; stop only for destructive actions or genuine scope changes. The agent system was built on the opposite assumption. Measured:

- **46 agents** open "On Startup" with a numbered "Ask user: …" step (mode selection, scope, target).
- **`grill-me`** interviews one question at a time, never batching, 13–14 questions.
- **41 agents** still carry the original Confidence Gate line ("If uncertain: stop, state the uncertainty, ask") *and* the Clarification Checkpoint that was written to replace it ("do NOT dead-stop … ask ONE narrow question … keep building"). All 68 carry the Checkpoint. The old line was never removed.
- **`cag-agent-system-qa`** step 3: "Confirm working directory is `/Users/apple/Downloads/CAG/`". In a remote session that check can only fail.

None of this needs new rules. CLAUDE.md rule 8 (the 97% gate + one narrow question) and rule 6 (restate the brief) already describe the Fable-correct behaviour. The agent files just have not caught up.

### 4a · Concrete edits

```
All 68 agents, scripted (mirror scripts/add_*_rule.py, inverted):
  remove the line "**Confidence Gate:** … If uncertain: stop, state the uncertainty, ask. Never guess on live files."
  keep the Clarification Checkpoint as the only gate

46 agents with "Ask user: which mode":
  "Mode is read from the invocation (slug, flag, or brief). If absent, default to <named mode>
  and say so in the first line. Ask only if two modes would produce materially different files."

skills/grill-me.md
  add --brief <path> mode: reads a filled brief and skips every answered question;
  interactive one-at-a-time stays for local sessions only
  the SESSION CONTEXT block becomes the contract; anything already on disk is never re-asked

.claude/agents/cag-agent-system-qa.md
  "confirm cwd is /Users/apple/…" → "confirm `git rev-parse --show-toplevel` contains CLAUDE.md"
  add checks: no dead tier names, no CLAUDE_CODE_FORK_SUBAGENT, no /Users/apple, no `tools:` in skills,
  content root says src/pages
```

## 5 · The Golden Rule Block — Bulk, Drift, And What To Keep

Every agent carries the same ~5.2 KB `## Golden Rule` block: eight site-wide rules (Header Style, Write-From-Outline, Title Case, Outline Gate, Link-First, Clarification Checkpoint, First-Person Voice, plus the Playwright-first / Confidence lines) followed by a `## CAG Project Context` block. Measured total: **351,742 bytes** across 68 files, all near-identical, each injected by a one-off `scripts/add_*_rule.py` and never reconciled since.

Three costs. It is ~1,300 tokens on every agent invocation before the agent's own instructions start. It drifts: the Context block says "Content root: `site/content/`" in 58 files while CLAUDE.md, `rules/deploy.md` and the deploy model say `src/pages/` ships. And CLAUDE.md already loads for every session and points at `rules/*.md` + `data/quality/rule-index.json` (55 rules, each `enforced` true/false with its test named), so the agent copy is the third statement of the same rule and the only one nobody tests.

**Recommended:** collapse each agent's Golden Rule to one paragraph — "Bound by `CLAUDE.md`'s thirteen judgment rules and the packs in `rules/` (headings, images, schema, links, copy, design, gates, deploy, for-sale). This agent additionally: …" — and keep only the rules that are specific to that agent (e.g. `cag-section-builder`'s Interior-Page Standard, `cag-external-link-agent`'s 200-check). Fix the Context block's content root in the same pass. **Trade-off:** an agent invoked from a session that somehow lacks CLAUDE.md loses the rules; in this repo that cannot happen, because CLAUDE.md is at the root and loads unconditionally. Write it as one idempotent script (`scripts/slim_golden_rule.py`) with a fixture, the same pattern the `add_*` scripts used.

## 6 · Skills — Registration Is Healthy, Frontmatter Is Not

Registration is clean: `skills/<name>.md` is the source, `register_skills.py --copy` mirrors all 70 into `.claude/skills/<name>/SKILL.md`, and a byte-compare shows 65 identical, 0 divergent, 5 that live only in `.claude/skills/` (the 4 openspec skills + `cag-bird-page-excellence`, which is a directory skill). Keep that.

What Fable 5.1 reads differently:

- **`tools:` in 42 skills is not a field.** Rename to `allowed-tools:` where the restriction is intended; delete it where it merely mirrors the caller. `cag-branded-hybrid-keywords` carries `effort: high`, which *does* take effect now.
- **`context: fork` + `agent:`** exist for skills. The heavy audit chains (`cags-comprehensive-page-audit-system`, `cag-final-page-pass`, `cag-page-hardening`) currently run inline and push 20–40k tokens of gate output into the build session. Running them forked keeps the parent context for building. Try it on `cags-comprehensive-page-audit-system` first.
- **Descriptions drive auto-invocation.** Fable picks a skill from its description. Eight are under 150 characters and one has no trigger phrase at all: `cag-seo-master-checklist` reads "SKILL: CAG Master SEO Execution Checklist (v2.0)" and its frontmatter contains four stray keys (`4-phase`, `Invoke`, `uploaded`, `Internal`) — the body leaked into the header. Rewrite it and the seven short ones (`cag-broken-links`, `cag-google-map`, `cag-indexing`, `cag-location-page-builder`, `cag-youtube`, `openspec-apply-change`, `openspec-archive-change`) in the "Use when … Triggers: …" form the good ones already use.
- **Overlapping triples confuse selection.** `cag-bird-listing-page` / `cag-bird-page-build` / `cag-bird-page-excellence` all claim `/available/` pages; `cag-bird-page-build` says it supersedes the first. Retire or demote the superseded one to a pointer, and make the three descriptions disjoint (listing = retire/inventory · build = the 22-section build · excellence = QA/differentiation). Same for `cag-google-map` (skill) vs `cag-google-map-agent`, and `cag-footer-agent` vs `cag-footer-standardizer`.
- **Hard-coded `/Users/apple/Downloads/CAG/`** appears in 10 skills. Replace with repo-relative paths.

## 7 · The 7-Sprint Pipeline — Sound Shape, Three Adaptations

The pipeline itself (Intel → Orient → Blueprint → Asset Gate → Build → Harden → Final → Ship → Bank) is the strongest part of the system and should not be restructured. Sprint 3 as its own sprint, the meta gate before any page result, `cag-gate-integrity` before acting on any checker: keep all of it. Three places need a Fable-era edit.

**7a · Approval gates versus autonomy.** The pipeline has `[REVIEW]`, `[APPROVE]` ×2 and the Asset Gate. Under Fable these become the *only* places `AskUserQuestion` is permitted: Sprint 0.5 (brief confirmed), Sprint 1 (outline + distribution matrix + header style), Asset Gate (breeder drops the infographics). Everything else runs under the Clarification Checkpoint: write to disk, log to `## Open Flags`, continue. Write that sentence into WORKFLOW.md above the pipeline diagram, so 46 agents' startup interviews have a documented replacement.

**7b · Ship on a branch.** CLAUDE.md rule 3 says "work on `main`, never a feature branch" because only `main` deploys. Remote sessions (this one included) are assigned a branch by the harness and cannot push to `main`; the `PostToolUse` hook in `settings.local.json` then auto-pushes every commit. The rule needs a second clause: *in a remote or web session, work on the assigned branch, open a draft PR, and the breeder's merge is the deploy; IndexNow runs after the merge is live, not after the push.* Without this, every remote build ends with finished work that is "live-404 while looking done", which is exactly the failure the rule exists to prevent.

**7c · Sprint 0 and the batch flows name the mechanism.** "Run all three tracks simultaneously" → three `Agent` calls in one message. "Location Pages (all states at once) → fork-parallel" → `Agent` per state, or a `Workflow` on explicit opt-in. §2 has the wording.

Smaller doc drift to fix in the same pass: WORKFLOW.md is 832 lines and still says "all 68 agents run on Opus 4.8" in §Model Tier System; system-registry says "66 agents" twice; `cag-agent-system-qa` reads `docs/architecture/00_SYSTEM_ARCHITECTURE.md`, which does not exist; the batch-rebuilder still commits to `site/content/` and pushes `origin main`.

## 8 · Security Finding — Act Before Anything Else

`.claude/settings.local.json` is tracked in git (last touched in commit `025dcee`) and one of its `permissions.allow` entries embeds a **Cloudflare API token** inside a `wrangler pages deploy` command. `health-sweep.sh` claims secret-leak detection and did not catch it. Rotate the token in the Cloudflare dashboard, remove the entry, add `.claude/settings.local.json` to `.gitignore` (only `.claude/worktrees/` is ignored today), and add the pattern `CLOUDFLARE_API_TOKEN=` to the health sweep. The token value is deliberately not reproduced in this report.

## 9 · Migration Plan — APPLIED 2026-09-07

**Status: steps 1–9 applied on the audit branch the same day** (commits on `claude/fable-5-1-adaptability-audit-isjqbo`, see the PR). Two items the tree cannot do for itself remain with the breeder: rotate the Cloudflare token in the dashboard (it is out of the tree but still in git history), and decide whether to try `xhigh` effort. The one item deliberately deferred is the per-agent tool fallback ladder for the 17 MCP-listing agents (§3); it is logged in `session-log.md` Known Issues.

Ordered by risk-reduction per minute. Every step is idempotent and gated by an existing check.

| # | Step | Mechanism | Gate |
|---|---|---|---|
| 1 | Rotate + purge the Cloudflare token; gitignore `settings.local.json` | manual + `.gitignore` | `bash scripts/health-sweep.sh --no-build` |
| 2 | Registry: tiers → `tier_*`, `model: inherit`; `apply_model_tiers.py` stops writing `dynamic_workflow` and the prose block | edit JSON, patch script, run | `verify_model_tiers.sh` 68/68; pytest fixture green (pytest is not installed in the remote image — add it to the session-start hook) |
| 3 | Routing tables + `route.py` + WORKFLOW/system-registry model sections | 5 files | `python3 scripts/route.py "full rebuild"` prints `tier_max` |
| 4 | Orchestrators get `Agent`; fork sections rewritten; `/schedule` → Routines | 5 agents + 1 doc | `grep -r CLAUDE_CODE_FORK_SUBAGENT` returns 0 |
| 5 | `scripts/slim_golden_rule.py`: drop the old Confidence line, collapse the block, fix content root, strip `/Users/apple` | new script + fixture | byte-idempotent on 2nd run; `cag-agent-system-qa` full |
| 6 | Startup "Ask user" → default-and-state in 46 agents; `grill-me --brief` | scripted where the phrasing is uniform, hand-edit the rest | grep for `Ask user:` in `## On Startup` returns 0 |
| 7 | Skills: `tools:` → `allowed-tools:`; rewrite 8 descriptions; repair `cag-seo-master-checklist` frontmatter; `context: fork` on the audit chain | `register_skills.py --copy` after each edit | `register_skills.py --check` 70/70 |
| 8 | WORKFLOW.md §7a/§7b text; CLAUDE.md rule 3 second clause | 2 docs | `cag-agent-system-qa` Check 6 |
| 9 | Bank: log this audit in `docs/reference/session-log.md` Known Issues; add the new QA checks | 1 doc + 1 agent | `quality_report.py` runs clean |

Estimated effort: steps 1–4 are one session; 5–7 are one more; 8–9 are an hour. Nothing here touches `src/pages/` or `dist/`, so no page gate needs to run.

## 10 · Open Flags

- **Applied, not just proposed.** Everything in §9 except the token rotation and the §3 fallback ladder is now on the branch. Gates at time of writing: `pytest tests/` 134 passed, `verify_model_tiers.sh` 68/68, `register_skills.py --check` 70/70, `apply_model_tiers.py --dry-run` 0, `slim_golden_rule.py --dry-run` 0.

- **Rule 3 conflict in this session.** This audit was produced on the harness-assigned branch, not `main`, because the remote harness does not permit a push to `main`. The deliverable is committed there and opened as a draft PR. §7b is the proposed permanent resolution; until the breeder rules on it, remote sessions will keep hitting this.
- **`model: inherit` versus pinning** is a breeder decision (§1). The audit recommends `inherit`; if the breeder wants a specific pinned id, `claude-fable-5-1` is valid and the same registry edit applies.
- **`xhigh` effort** is untested on this system; the recommendation is to try it on the five heavy agents and measure rework rate in `quality_report.py`, not to adopt it blind.
- **Workflow tool** requires explicit breeder opt-in per run; the batch flows should say so rather than promise parallelism they cannot start on their own.

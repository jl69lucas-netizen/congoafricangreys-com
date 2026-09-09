# C.A.Gs Managed Agent Teams

> Source: docs/artifacts/cags-managed-agents-teams.html (published Artifact). Brief date 2026-09-09.

## 0 · The brief, restated

**Goal.** Decide what a Managed Agents version of the C.A.Gs agent system would look like, and say precisely how it differs from the 68 `.claude/agents/*.md` + 70 `.claude/skills/` running in Claude Code today.

**Scope.** Team structure, agent-to-team mapping, shared infrastructure (environment, repo mount, memory, vault), what cannot port, sample manifests, and a phased recommendation. Nothing is created on the platform by this document.

**Gates.** No fabricated metrics (rule 10). Prices quoted are Anthropic list rates as of the bundled API reference dated 2026-06-24. Budget caps below are *proposed ceilings*, not cost predictions.

**Done means.** The breeder can read this once and answer three questions: which teams, in what order, and what changes in day-to-day operation.

**Out of scope.** Running `ant beta:agents create`, moving credentials into a vault, or altering any local agent file. Those are the next session, after the breeder picks a phase.

## 1 · The answer in one screen

**Recommended: a hybrid, not a port.** Move the two *cron-shaped* teams (Intelligence and Site Health) to Managed Agents first. Keep page building in Claude Code on this Mac, where the preview pane, the render harness and push-to-main deploy already work. Revisit page building after the first two teams have run for a month.

**Why, from the data.** The weekly and monthly loops in `docs/reference/WORKFLOW.md` §8 (rank-tracker "every Sunday", pricing alert weekly, site hygiene monthly, NAP audit quarterly) only run when someone opens a laptop session. They need no visual approval, their outputs are files and pull requests, and their inputs are already in the repo (`data/analytics/` CSV exports, `data/competitors.json`, `data/directories.json`). That is exactly the shape a scheduled deployment is built for. Page building, by contrast, depends on three things that live on this machine: the desktop preview for rule 7 (preview before apply), a real Chromium for `npm run test:render:pages`, and the push-to-`main` deploy path that a remote session is forbidden to use.

**The trade-off.** Two runtimes to keep in step. The mitigation is that both read the same `.claude/skills/` from the same GitHub repository, so the *knowledge* stays single-sourced; only the 12 or so agent manifests are new files.

**What it would be, in numbers.**

| Today (Claude Code) | Proposed (Managed Agents) |
|---|---|
| 68 agent files, flat, dispatched by the Agent tool | 4 teams · 13 agent objects (4 coordinators, 8 workers, 1 QA) |
| 70 skills in `.claude/skills/` | Same 70, auto-discovered from the mounted repo at session start |
| 3 effort tiers via `data/agent-registry.json` | `model.effort` per agent object, versioned |
| Runs when a session is open | 2 teams on cron, 2 on demand |
| Deploys by pushing `main` | Draft PR; breeder merge is the deploy |

## 2 · Today vs Managed Agents, dimension by dimension

| Dimension | C.A.Gs today (Claude Code on this Mac) | Managed Agents |
|---|---|---|
| Where the loop runs | Locally, inside the desktop app session | Anthropic orchestration layer; tools run in a per-session cloud container |
| What an "agent" is | A Markdown file with frontmatter (`model: inherit`, `effort:`), read by the Agent tool | A persisted, **versioned** API object: `model`, `system`, `tools`, `mcp_servers`, `skills`, `multiagent` roster |
| How specialists are picked | Orchestrators (content-architect, structure-architect, batch-rebuilder) call `Agent` by name | Coordinator gets `list_agents` / `send_to_agent`; picks from a roster of ≤20 by each entry's `name` + `description` |
| Depth of delegation | Unlimited nesting in practice | Exactly one level. A roster member cannot have its own roster |
| Parallelism | Multiple Agent calls in one message | Up to 25 concurrent threads sharing one container and filesystem |
| Skills | `.claude/skills/<name>/SKILL.md`, loaded by the Skill tool | Same directory is scanned at session start from the mounted GitHub repo; also up to 20 attached via the Skills API |
| Agent bodies (the 68 `.md`) | Are the agents | **Not discovered.** Only `.claude/skills/` is. Each agent body becomes either a coordinator/worker `system` prompt or is converted to a skill |
| Model / effort | One session model (Fable 5.1), effort tier per agent from the registry | Per agent object: `{id, effort}`. Cheaper workers (Sonnet 5, Haiku 4.5) are first-class roster members |
| Schedule | None. `rank-tracker` "runs every Sunday" only if someone runs it | Scheduled deployments: cron + IANA timezone, per-run records, pause/unpause, webhook on success/failure |
| Spend control | Subscription; no per-task cap | Session and deployment **budgets** in dollars at list price; session pauses at the cap |
| Human gates | Preview pane, AskUserQuestion, the 97 % confidence gate | `permission_policy: always_ask` per tool → session idles until `user.tool_confirmation`; `user.message` to continue |
| Memory | `~/.claude/projects/…/memory/` with `MEMORY.md` index | Memory stores mounted at `/mnt/memory/<name>/`, ≤8 per session, every write versioned |
| MCP auth | Keychain (native HTTP OAuth) or `mcp-remote` | Vaults. Agent declares `{type, name, url}` only; the credential attaches to the session via `vault_ids` and auto-refreshes |
| Browser | Playwright / chrome-devtools MCPs, Claude-in-Chrome with logged-in sessions | Built-in `web_search` / `web_fetch` with domain allow-lists; a Chromium can be `npm`-installed in the container (unverified, see Open Flags) |
| GSC | Local `uvx mcp-search-console` stdio server | No stdio servers. Works from the CSV exports already committed under `data/analytics/` (which is how `cag-gsc-analytics` reads today) |
| Deploy | Push `main` → GitHub Actions → Cloudflare Pages → IndexNow | Push a branch through the git proxy → draft PR via GitHub MCP → breeder merges → IndexNow after live |
| Deliverables | Artifacts + `.md` (rule 13) | Files in the repo branch, PR description, session output files. Artifacts remain a Claude Code thing |

## 3 · The four teams

Each team is **one coordinator agent** with a roster. A session (or a scheduled firing) starts the coordinator; it delegates one level down. All 68 current agents fold into exactly one team below.

### Team A · Intelligence — scheduled, Sundays 06:00 America/Chicago

| Role | Agent object | Model · effort | Tools |
|---|---|---|---|
| Coordinator | `cag-intel-lead` | claude-opus-5 · high | toolset (bash/read/write/glob/grep), web_search + web_fetch (allow-list: registry domains), Firecrawl MCP |
| Worker | `cag-competitor-reader` | claude-sonnet-5 · medium | web_fetch, Firecrawl MCP, read/write |
| Worker | `cag-serp-reader` | claude-haiku-4-5 · low | web_search, read/write |
| Self | `{type: self}` | — | for the synthesis sub-analyses |

Folds in 11 agents: competitor-registry, competitor-intel, rank-tracker, competitor-pricing-alert, branded-search-monitor, gsc-analytics, llm-keyword-intel, competitive-keyword-gap, framework-agent, strategy-synthesizer, paa-agent.

Inputs: `data/competitors.json` (written only by `patch_competitor_registry.py`), `data/competitor-prices.json`, `data/analytics/*.csv`, `docs/reference/top-pages.md`. Outputs: `docs/research/YYYY-MM-DD-*.md`, updated `data/competitor-prices.json`, one draft PR titled `intel: week of …`. Proposed cap: **$15 per firing.**

Rule it must carry: the ISP-DNS-filter trap. The container has its own resolver, so the `dig @1.1.1.1` workaround becomes unnecessary, but the two never-link domains stay in the system prompt.

### Team B · Page Build — on demand, stays local for Phase 1

| Role | Agent object | Model · effort | Tools |
|---|---|---|---|
| Coordinator | `cag-page-lead` | claude-fable-5-1 · xhigh | full toolset, Firecrawl MCP, GitHub MCP |
| Worker | `cag-page-researcher` | claude-sonnet-5 · medium | web_search, web_fetch, Firecrawl MCP |
| Worker | `cag-gate-runner` | claude-sonnet-5 · low | bash only (runs `final_page_audit.py`, `page_hardening_scan.py`, `dup_content_audit.py`, `aeo_audit.py`, `test:render:meta`) |
| Advisor | `{type: advisor, model: claude-opus-5}` | — | consulted for the thirteen judgment rules |
| Self | `{type: self}` | — | one page per copy in a batch |

Folds in 33 agents: content-architect, structure-architect, hub-builder, content-audit, angle, seo-content-writer, non-commodity, entity-incorporation, faq, section-builder, infographic-builder, interactive-component, image-pipeline, keyword-verifier, meta-description, external-link, comparison-builder, location-builder, batch-rebuilder, homepage-builder, about-builder, purchase-guide, species-guide, scam-specialist, financial-strategist, timneh-specialist, variant-specialist, bird-personality, blog-post-agent, google-map-agent, trust-signals, conversion-tracker, ab-test.

Why it waits: rule 7 (preview before apply), the 375/768/1280 browser harness, and the breeder-merge deploy path. When it does move, `write` and `bash git push` get `always_ask`, and the 39-destination location batch becomes 39 `self` copies in one session instead of 39 Agent calls. Proposed cap: **$40 per page session.**

### Team C · Site Health — scheduled, 1st of the month 05:00, plus a daily 07:00 IndexNow sweep

| Role | Agent object | Model · effort | Tools |
|---|---|---|---|
| Coordinator | `cag-health-lead` | claude-sonnet-5 · high | toolset, GitHub MCP, web_fetch (allow-list: congoafricangreys.com, api.indexnow.org) |
| Worker | `cag-health-runner` | claude-haiku-4-5 · low | bash, read (runs `health-sweep.sh --no-build`, `generate_sitemaps.py`, `indexnow_submit.py`) |
| Worker | `cag-system-qa` | claude-sonnet-5 · medium | read, glob, grep (audits agents + skills, the `agent-system-qa` job) |

Folds in 12 agents: site-hygiene, accessibility-fixer, performance-fixer, performance-monitor, canonical-fixer, footer-standardizer, redirect-manager, deploy-verifier, contact-form-updater, agent-system-qa, self-update, nap-citation.

Outputs: `sessions/YYYY-MM-DD-health.md`, a draft PR only when a fix is mechanical (redirect chain, canonical, footer drift). Proposed cap: **$8 per firing**, **$2 for the daily sweep.**

### Team D · Growth Ops — on demand, drafts only

| Role | Agent object | Model · effort | Tools |
|---|---|---|---|
| Coordinator | `cag-growth-lead` | claude-sonnet-5 · high | toolset, web_search, GitHub MCP |
| Worker | `cag-copy-drafter` | claude-sonnet-5 · medium | read, write (skills: social-content, youtube-script, caption-writer, anti-ai-writing) |

Folds in 12 agents: social-strategist, video-seo, email-newsletter, email-lead-nurture, review-collection, seasonal-content, case-study, backlink-outreach, directory-submission (discovery half only), heatmap-analyst, funnel-analysis, clutch-manager.

Hard line: this team **never sends**. No email, no post, no directory form. It writes to `content/newsletters/`, `data/seasonal-calendar.json`, `data/backlink-tracker.json` and opens a PR. Directory *submission* stays with Claude-in-Chrome on this Mac because it needs the breeder's logged-in browser. Proposed cap: **$10 per session.**

## 4 · Shared infrastructure

### One environment, `cag-cloud`

- `config.type: cloud`, networking `limited` with `allow_package_managers: true` and `allow_mcp_servers: true`; `allowed_hosts` = congoafricangreys.com, api.indexnow.org, generativelanguage.googleapis.com, plus the competitor registry domains for Team A.
- Packages: Node 20 + Python 3 (both used by `scripts/`). Chromium for the render harness is an Open Flag.

### The repository mount

`github_repository` → `jl69lucas-netizen/congoafricangreys-com`, `checkout: {type: branch, name: main}`, token scope *Contents: read and write* plus *Pull requests*. The token never enters the container; pushes go through the git proxy. This mount is what makes the 70 skills appear: the platform scans `.claude/skills/<name>/SKILL.md` at session start. Skills pushed mid-session are not seen; start a new session.

> Trust boundary: anything in `.claude/skills/` on `main` becomes agent instructions with `bash` behind them. Keep the repo private and review every PR that touches that directory before merging.

### Memory stores (≤8 per session; use 3)

| Store | Access | Seeded from |
|---|---|---|
| `cag-project-memory` | read_write | `~/.claude/projects/-Users-apple-Downloads-CAG/memory/*.md` (the index becomes `/MEMORY.md`) |
| `cag-verified-claims` | read_only | The Verified-Claim Ledger in `.claude/agents/cag-entity-incorporation-agent.md` + `sessions/2026-06-03-homepage-entity-map.md` |
| `cag-team-<letter>-lessons` | read_write | Empty; each team writes its own "what broke" notes |

Never write a credential into a store; every version is replayed into later sessions.

### Vault `cag-secrets`

| Credential | Type | Used by |
|---|---|---|
| Firecrawl | MCP OAuth (`https://mcp.firecrawl.dev/v2/mcp-oauth`) | Teams A, B |
| GitHub | MCP OAuth (for `create_pull_request`) | All teams |
| `GEMINI_API_KEY` | environment_variable (from `.google-key`) | Team B image generation |
| IndexNow key | environment_variable | Team C |

Vault credentials attach at `sessions.create` via `vault_ids`, and OAuth tokens refresh server-side. This is the permanent fix for the sign-in loop that hit `mcp-remote` locally: no proxy process, no laptop.

### Manifests live in the repo

`agents/managed/*.agent.yaml`, `agents/managed/cag-cloud.env.yaml`, `agents/managed/*.deployment.yaml`, applied with `ant beta:agents create` (once) and `ant beta:agents update --agent-id … --version N` (thereafter). IDs and versions go into `agents/managed/ids.json`. The Console page at `platform.claude.com/workspaces/default/agents` is for inspecting and pausing, not for hand-editing, because a Console edit bumps the version without a commit.

## 5 · What does not port

| Stays on this Mac | Why |
|---|---|
| `gscServer` (`uvx --with "cryptography<46" mcp-search-console`) | stdio server with a local client-secret file; Managed Agents accept URL MCP servers only. Team A reads the committed CSV exports instead, which is the current contract of `cag-gsc-analytics` anyway |
| Claude-in-Chrome directory submissions and NAP checks that need a login | Needs the breeder's real browser session |
| Preview-before-apply (rule 7) | Needs the desktop preview pane and a human looking at it |
| Push to `main` | A remote session is forbidden from it by `rules/deploy.md`; cloud teams open draft PRs |
| Artifacts with copy buttons (rule 13) | The Artifact tool is Claude Code's; cloud teams deliver `.md` in the PR and this session republishes when needed |
| iMessage / Telegram plugins, `SendUserFile` | Desktop-app channels. Cloud teams notify through the deployment webhook instead |

Also note what the 68 files *are* today: their Golden Rule block already points at `CLAUDE.md` + `rules/` rather than copying them (`slim_golden_rule.py`, 2026-09-07). That is the right shape for a `system` prompt: short, pointing at files the container can read.

## 6 · Sample manifests

Coordinator for Team A. Every field shown is from the platform reference bundled in this session; nothing is guessed.

```yaml
# agents/managed/cag-intel-lead.agent.yaml
name: cag-intel-lead
description: >
  Weekly competitor and search intelligence for CongoAfricanGreys.com.
  Hand a single competitor domain to cag-competitor-reader; hand a single
  SERP query to cag-serp-reader; keep synthesis and the gap matrix yourself.
model:
  id: claude-opus-5
  effort: high
system: "@./prompts/intel-lead.md"
tools:
  - type: agent_toolset_20260401
    default_config: { enabled: true }
    configs:
      - name: web_search
        allowed_domains: [google.com, bing.com]
      - name: web_fetch
        allowed_domains: [congoafricangreys.com]
  - type: mcp_toolset
    mcp_server_name: firecrawl
mcp_servers:
  - type: url
    name: firecrawl
    url: https://mcp.firecrawl.dev/v2/mcp-oauth
multiagent:
  type: coordinator
  agents:
    - { type: agent, id: agent_COMPETITOR_READER }
    - { type: agent, id: agent_SERP_READER }
    - { type: self }
```

The scheduled deployment that fires it:

```yaml
# agents/managed/intel-weekly.deployment.yaml
name: intel-weekly
agent: agent_INTEL_LEAD
environment_id: env_CAG_CLOUD
vault_ids: [vault_CAG_SECRETS]
resources:
  - type: github_repository
    repository: jl69lucas-netizen/congoafricangreys-com
    checkout: { type: branch, name: main }
  - type: memory_store
    memory_store_id: memstore_PROJECT
    access: read_write
    instructions: Project memory. Read MEMORY.md before starting.
initial_events:
  - type: user.message
    content:
      - type: text
        text: >
          Run the weekly intelligence loop per docs/reference/WORKFLOW.md §8.
          Write docs/research/<date>-weekly-intel.md, update
          data/competitor-prices.json, push branch intel/<date>, open a draft PR.
schedule:
  type: cron
  expression: "0 6 * * 0"
  timezone: America/Chicago
budget:
  type: limit
  max_list_cost: { amount: "1500", currency: USD }
```

Apply once, then update by version:

```bash
AGENT_ID=$(ant beta:agents create < agents/managed/cag-intel-lead.agent.yaml --transform id -r)
```

```bash
ant beta:agents update --agent-id "$AGENT_ID" --version 1 < agents/managed/cag-intel-lead.agent.yaml
```

Firing is jittered by up to 15 % of the interval (max 9 minutes), so a Sunday 06:00 run can land at 06:09. Do not chain a deadline to the listed time.

## 7 · Cost frame

List rates from the bundled reference (cached 2026-06-24). These are the rates session budgets are priced against.

| Model | Input $/1M | Output $/1M | Proposed role |
|---|---|---|---|
| claude-fable-5-1 | 10.00 | 50.00 | Team B coordinator only |
| claude-opus-5 | 5.00 | 25.00 | Team A coordinator, Team B advisor |
| claude-sonnet-5 | 2.00 | 10.00 | Team C/D coordinators, readers, gate runner |
| claude-haiku-4-5 | 1.00 | 5.00 | SERP reader, health runner |

What this changes versus today: local sessions bill nothing per token beyond the subscription; every cloud session bills at list. That is why the caps above exist and why the first two teams are the cheap ones. Run Teams A and C for four firings each, read `usage.list_cost` on every session, then decide whether Team B's page sessions are worth their cap. No projection is offered here because there is no measured baseline yet: **NOT FETCHED**.

## 8 · Phased rollout

1. **Phase 0, this week.** Create `agents/managed/` with the four coordinator manifests, two worker manifests, the environment and the two deployments. Seed the three memory stores from the local memory directory. Put Firecrawl, GitHub, Gemini and IndexNow into the vault. No page is touched.
2. **Phase 1, first month.** Turn on Team A (weekly) and Team C (monthly + daily sweep). Every run ends in a draft PR; the breeder merges. Compare the intel report against the last local `cag-rank-tracker` output for one week to confirm parity.
3. **Phase 2, decision point.** With four firings of cost and quality data, decide on Team D (cheap, low risk) and whether Team B is worth moving. Team B's blocker list to clear first: Chromium in the container, and a preview substitute (screenshots attached to the PR from the harness at 375/768/1280).
4. **Never.** Push to `main` from the cloud; send anything from Team D; store a key in memory.

Reversal is cheap at every phase: pausing a deployment stops the spend, and archiving is the only irreversible action, so nothing gets archived without the breeder saying so.

## 9 · Open flags

- **Chromium in the cloud container.** `packages` + `allow_package_managers` should permit `npx playwright install chromium`, but this is unverified in the bundled reference. Until proven, Team B stays local and Team C skips `test:render:pages`.
- **IndexNow after the merge.** The rule is "submit after the deploy is live". The daily 07:00 sweep in Team C handles it by diffing `main` against a submitted-slugs ledger; that ledger file does not exist yet.
- **GSC freshness.** Team A only sees the CSV exports committed to `data/analytics/`. Someone still has to export monthly, as today.
- **Agent bodies as skills.** The 68 `.md` bodies are not discovered by the platform. Which of them carry knowledge worth converting to a skill (e.g. `cag-entity-incorporation-agent`'s ledger, `cag-section-builder`'s section types) versus which are pure routing that the coordinator prompt absorbs is a per-file call for Phase 0.
- **One question for the breeder.** Is the weekly cadence in America/Chicago acceptable, or should Team A fire Saturday night so the report is waiting Sunday morning?

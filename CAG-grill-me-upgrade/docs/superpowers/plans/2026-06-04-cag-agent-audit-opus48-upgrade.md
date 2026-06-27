# CAG Agent + Skill Audit & Opus 4.8 Upgrade — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit all 66 CAG agents + 41 skills for capability/tooling gaps, fix the real ones, and upgrade every agent's model to `claude-opus-4-8` (keeping effort tiers as the cost lever), then prove the top-to-bottom workflow is intact.

**Architecture:** The model assignment is registry-driven (`data/agent-registry.json` → `scripts/apply_model_tiers.py` writes frontmatter). We collapse the 5-tier model matrix into **one model (Opus 4.8) across all 66 agents**, preserving the three *effort* tiers (max/high/medium) which control reasoning depth and cost. Genuine capability gaps (missing data-file scaffolds, a malformed tools line, scraper agents with no browser tool, stale "65-agent" docs, an out-of-sync router) are fixed as discrete tasks. Each task ends with a concrete verification command, not an assertion.

**Tech Stack:** Markdown agent/skill files with YAML frontmatter · JSON registry · Python (`apply_model_tiers.py`, `route.py`) · Bash (`verify_model_tiers.sh`, `health-sweep.sh`) · Astro build · git push → Cloudflare Pages.

---

## Decisions & Honest Reasoning (read before executing)

### Why ALL agents go to Opus 4.8 and NONE stay on Opus 4.7
4.8 supersedes 4.7 on every axis (reasoning, instruction-following, code/markup fidelity). Pinning an agent to 4.7 would be a **pure downgrade with no upside**. The only defensible reason to pin a prior model is a *known regression* on a specific workload — and none is documented for any CAG task. **Honest conclusion: zero agents need 4.7.** Every `opus47_high` agent moves to `opus48_high`.

### Why we keep the EFFORT tiers (max / high / medium) instead of maxing everything
Model and effort are orthogonal. Effort controls extended-thinking budget (`max` ≈ 10k thinking tokens, `high` ≈ 4k, `medium` = standard inference). Running a redirect-fixer at `max` effort wastes tokens and latency for zero quality gain. Keeping each agent's *current* effort level is the honest cost/quality balance — best model everywhere, thinking budget matched to task complexity.

### Honest cost trade-off (flagged, not hidden) — applies to the mechanical tier
The 10 former-Haiku utilities (`canonical-fixer`, `redirect-manager`, `footer-standardizer`, `deploy-verifier`, `external-link-agent`, `image-pipeline`, `google-map-agent`, `contact-form-updater`, `clutch-manager`, `nap-citation-agent`) and the 16 former-Sonnet-medium agents see the **largest cost increase for the smallest quality gain** — they do deterministic text/file transforms where Haiku was already sufficient. Per the explicit instruction ("upgrade ALL to opus 4.8 except only those that need 4.7"), this plan moves them to Opus 4.8 at `medium` effort. **Trade-off named:** ~10–20× token cost on these utilities vs. Haiku, buying marginally higher reliability. If the breeder later wants to claw back cost, the one-line revert is to set the `opus48_medium` tier's model back to `claude-haiku-4-5-20251001` in the registry and re-run the apply script — no other change needed. This plan does NOT do that; it follows the instruction.

### Tier remap (model uniform, effort preserved)
| Old tier | Count | New tier | Model | Effort |
|---|---|---|---|---|
| `opus48_max` | 15 | `opus48_max` | claude-opus-4-8 | max |
| `opus47_high` | 10 | `opus48_high` | claude-opus-4-8 | high |
| `sonnet_high` | 15 | `opus48_high` | claude-opus-4-8 | high |
| `sonnet_medium` | 16 | `opus48_medium` | claude-opus-4-8 | medium |
| `haiku_medium` | 10 | `opus48_medium` | claude-opus-4-8 | medium |

Result: **15 max + 25 high + 26 medium = 66.** (Note: WORKFLOW.md currently mislabels the max tier as "14" — it is 15.)

### Skills (41 files) — honest note, low-priority
Skill `model:` frontmatter is **inert**: skills execute in the *caller's* model context, so a `model:` line in a skill is non-standard and ignored by Claude Code. When a 4.8 agent invokes a skill, that skill already runs on 4.8. Therefore skills need **no model change** for the upgrade to take effect. Task 6 (optional) only strips/normalizes the misleading lines for documentation honesty.

---

## File Structure

**Modified:**
- `data/agent-registry.json` — rename 3 tier keys, set all models to `claude-opus-4-8`, remap 66 agent tier values, bump `last_updated`.
- `scripts/route.py` — rename tier labels in `ROUTING` + `DEFAULT` to the new keys.
- `.claude/agents/cag-infographic-builder.md` — fix malformed `tools:` line (add list brackets).
- `.claude/agents/cag-directory-submission-agent.md`, `cag-nap-citation-agent.md`, `cag-paa-agent.md`, `cag-backlink-outreach-agent.md`, `cag-llm-keyword-intel.md` — add Playwright MCP tool grants (scraper gap).
- `.claude/agents/cag-performance-monitor-agent.md`, `cag-accessibility-fixer.md`, `cag-performance-fixer.md` — add chrome-devtools `lighthouse_audit` MCP grant (audit gap).
- `CLAUDE.md` — "65"→"66" (2 spots) + tier description.
- `docs/reference/WORKFLOW.md` — §Model Tier System table + effort math.
- `scripts/health-sweep.sh` — "65 agents"→"66 agents" comment (cosmetic).
- All 66 `.claude/agents/*.md` — frontmatter rewritten by `apply_model_tiers.py` (not hand-edited).

**Created:**
- `data/directories.json`, `data/competitor-prices.json`, `data/backlink-tracker.json` — empty scaffolds so reader-agents don't crash on first run.

**Verification-only (not modified):** `scripts/apply_model_tiers.py` (already idempotent), `scripts/verify_model_tiers.sh`.

---

### Task 1: Seed missing data-file scaffolds + fix malformed tools line

**Files:**
- Create: `data/directories.json`, `data/competitor-prices.json`, `data/backlink-tracker.json`
- Modify: `.claude/agents/cag-infographic-builder.md:4`

- [ ] **Step 1: Confirm the three files are genuinely missing**

Run: `for p in directories competitor-prices backlink-tracker; do [ -f "data/$p.json" ] && echo "EXISTS data/$p.json" || echo "MISS data/$p.json"; done`
Expected: three `MISS` lines.

- [ ] **Step 2: Create `data/directories.json` scaffold**

```json
{
  "_meta": {
    "description": "Bird/exotic-pet directory registry — managed by cag-directory-submission-agent + cag-nap-citation-agent",
    "last_updated": "2026-06-04",
    "nap_master": "docs/reference/credentials.md"
  },
  "directories": []
}
```

- [ ] **Step 3: Create `data/competitor-prices.json` scaffold**

```json
{
  "_meta": {
    "description": "Weekly competitor price snapshots — managed by cag-competitor-pricing-alert-agent",
    "last_updated": "2026-06-04",
    "alert_thresholds": { "single_variant_usd": 150, "overall_usd": 300 }
  },
  "snapshots": []
}
```

- [ ] **Step 4: Create `data/backlink-tracker.json` scaffold**

```json
{
  "_meta": {
    "description": "Backlink outreach tracker — managed by cag-backlink-outreach-agent",
    "last_updated": "2026-06-04",
    "link_types": ["resource_page", "guest_post", "avian_vet_referral"]
  },
  "opportunities": []
}
```

- [ ] **Step 5: Fix the malformed tools line in cag-infographic-builder**

The current line is `tools: Read, Write, Bash` (no brackets — inconsistent with every other agent's `[Read, Write, Bash]`). Edit `.claude/agents/cag-infographic-builder.md` line 4 to:

```
tools: [Read, Write, Bash]
```

- [ ] **Step 6: Verify JSON validity + tools line**

Run: `for p in directories competitor-prices backlink-tracker; do python3 -c "import json;json.load(open('data/$p.json'));print('OK data/$p.json')"; done && grep -m1 '^tools:' .claude/agents/cag-infographic-builder.md`
Expected: three `OK` lines, then `tools: [Read, Write, Bash]`.

- [ ] **Step 7: Commit**

```bash
git add data/directories.json data/competitor-prices.json data/backlink-tracker.json .claude/agents/cag-infographic-builder.md
git commit -m "fix(agents): seed missing data scaffolds + normalize infographic-builder tools line"
```

---

### Task 2: Close the browser-automation + Lighthouse tool gaps

**Context:** Five agents describe scraping/SERP/LLM-querying work "via Playwright CLI," but `npx playwright` is NOT installed (verified: `npx --no-install playwright` errors) and they hold only `[Read, Write, Bash]`. Two perf/a11y agents run Lighthouse "via CLI," also not installed. The robust fix (matching how `cag-competitor-intel` and `cag-rank-tracker` are already wired) is to grant the MCP browser tools so the work does not depend on an absent local CLI.

**Files:**
- Modify: `.claude/agents/cag-directory-submission-agent.md`, `cag-nap-citation-agent.md`, `cag-paa-agent.md`, `cag-backlink-outreach-agent.md`, `cag-llm-keyword-intel.md` (Playwright grant)
- Modify: `.claude/agents/cag-performance-monitor-agent.md`, `cag-accessibility-fixer.md`, `cag-performance-fixer.md` (Lighthouse grant)

- [ ] **Step 1: Add Playwright MCP grant to the 5 scraper agents**

For each of the 5 files, replace the `tools: [Read, Write, Bash]` line with:

```
tools: [Read, Write, Bash, mcp__plugin_playwright_playwright__browser_navigate, mcp__plugin_playwright_playwright__browser_snapshot, mcp__plugin_playwright_playwright__browser_click, mcp__plugin_playwright_playwright__browser_evaluate, mcp__plugin_playwright_playwright__browser_take_screenshot]
```

- [ ] **Step 2: Add Lighthouse MCP grant to the 3 perf/a11y agents**

For `cag-performance-monitor-agent.md`, `cag-accessibility-fixer.md`, and `cag-performance-fixer.md`, replace `tools: [Read, Write, Bash]` with:

```
tools: [Read, Write, Bash, mcp__plugin_chrome-devtools-mcp_chrome-devtools__lighthouse_audit, mcp__plugin_chrome-devtools-mcp_chrome-devtools__navigate_page, mcp__plugin_chrome-devtools-mcp_chrome-devtools__take_snapshot]
```

- [ ] **Step 3: Add a one-line body note to each of the 8 agents documenting the fallback**

Immediately under each agent's first body heading, add this line (keeps the CLI path documented for environments where the MCP is absent):

```markdown
> **Tooling note:** Prefer the granted MCP browser/Lighthouse tools. If the MCP is unavailable, fall back to `npx playwright` / `npx lighthouse` via Bash (run `npx playwright install` first).
```

- [ ] **Step 4: Verify all 8 grants applied**

Run:
```bash
for a in cag-directory-submission-agent cag-nap-citation-agent cag-paa-agent cag-backlink-outreach-agent cag-llm-keyword-intel; do grep -q 'browser_navigate' .claude/agents/$a.md && echo "OK pw $a" || echo "FAIL pw $a"; done
for a in cag-performance-monitor-agent cag-accessibility-fixer cag-performance-fixer; do grep -q 'lighthouse_audit' .claude/agents/$a.md && echo "OK lh $a" || echo "FAIL lh $a"; done
```
Expected: 8 `OK` lines, no `FAIL`.

- [ ] **Step 5: Commit**

```bash
git add .claude/agents/cag-directory-submission-agent.md .claude/agents/cag-nap-citation-agent.md .claude/agents/cag-paa-agent.md .claude/agents/cag-backlink-outreach-agent.md .claude/agents/cag-llm-keyword-intel.md .claude/agents/cag-performance-monitor-agent.md .claude/agents/cag-accessibility-fixer.md .claude/agents/cag-performance-fixer.md
git commit -m "feat(agents): grant Playwright + Lighthouse MCP tools to scraper/audit agents (close CLI-dependency gap)"
```

---

### Task 3: Upgrade every agent to Opus 4.8 (registry rewrite + apply)

**Files:**
- Modify: `data/agent-registry.json`

- [ ] **Step 1: Rewrite the registry programmatically (rename tiers, uniform model, remap agents)**

Run this exact script — it edits in place, mapping old→new tiers and setting every model to `claude-opus-4-8`:

```bash
python3 - <<'PY'
import json, datetime
from pathlib import Path
p = Path("data/agent-registry.json")
reg = json.loads(p.read_text())

reg["_meta"]["last_updated"] = "2026-06-04"
reg["_meta"]["description"] = "CAG Agent Model Tier Registry — single source of truth. All agents on Opus 4.8; effort is the cost lever."
reg["_meta"]["tiers"] = {
    "opus48_max":    {"model": "claude-opus-4-8", "effort": "max"},
    "opus48_high":   {"model": "claude-opus-4-8", "effort": "high"},
    "opus48_medium": {"model": "claude-opus-4-8", "effort": "medium"},
}

remap = {
    "opus48_max": "opus48_max",
    "opus47_high": "opus48_high",
    "sonnet_high": "opus48_high",
    "sonnet_medium": "opus48_medium",
    "haiku_medium": "opus48_medium",
}
counts = {"opus48_max":0, "opus48_high":0, "opus48_medium":0}
for name, cfg in reg["agents"].items():
    new = remap[cfg["tier"]]
    cfg["tier"] = new
    counts[new] += 1

p.write_text(json.dumps(reg, indent=2) + "\n")
print("New tier counts:", counts, "total", sum(counts.values()))
PY
```
Expected: `New tier counts: {'opus48_max': 15, 'opus48_high': 25, 'opus48_medium': 26} total 66`

- [ ] **Step 2: Confirm no stale tier names remain in the registry**

Run: `grep -E 'opus47|sonnet|haiku' data/agent-registry.json || echo "CLEAN — no legacy tiers"`
Expected: `CLEAN — no legacy tiers`

- [ ] **Step 3: Dry-run the apply script**

Run: `python3 scripts/apply_model_tiers.py --dry-run | tail -5`
Expected: a summary line like `Patched: N  Warnings: 0  (DRY RUN)` with `Warnings: 0`.

- [ ] **Step 4: Apply for real**

Run: `python3 scripts/apply_model_tiers.py | tail -3`
Expected: `Warnings: 0` (no `[WARN] ... not found`).

- [ ] **Step 5: Verify every agent reports model + effort**

Run: `bash scripts/verify_model_tiers.sh | tail -2`
Expected: `Results: PASS=66 FAIL=0`

- [ ] **Step 6: Confirm zero agents still on a non-4.8 model**

Run: `grep -L 'model: claude-opus-4-8' .claude/agents/cag-*.md || echo "ALL 66 ON OPUS 4.8"`
Expected: `ALL 66 ON OPUS 4.8` (grep -L prints files NOT matching; none should).

- [ ] **Step 7: Commit**

```bash
git add data/agent-registry.json .claude/agents/*.md
git commit -m "feat(agents): upgrade all 66 agents to Opus 4.8 (effort tiers preserved as cost lever)"
```

---

### Task 4: Sync the deterministic router to the new tier names

**Files:**
- Modify: `scripts/route.py:25-43`

- [ ] **Step 1: Update the ROUTING tier labels + DEFAULT**

In `scripts/route.py`, change the tier-key strings (signal lists stay identical):
- `("opus47_high", [...])` → `("opus48_high", [...])`
- `("sonnet_high", [...])` → `("opus48_high", [...])` — **merge**: append the `sonnet_high` signals into the single `opus48_high` entry so there is one `opus48_high` tuple containing both signal lists.
- `("haiku_medium", [...])` → `("opus48_medium", [...])`
- `DEFAULT = "sonnet_medium"` → `DEFAULT = "opus48_medium"`

Final `ROUTING` should read:

```python
ROUTING = [
    ("opus48_max", [
        "deep audit", "full rebuild", "full silo", "reverse silo",
        "competitor analysis", "competitor url", "architecture rebuild",
        "new page from scratch", "from scratch", "full page build",
    ]),
    ("opus48_high", [
        "section update", "faq only", "faq", "about page", "comparison page",
        "comparison", "hub page", "spoke page", "cluster build", "variant page",
        "monitor", "analytics", "conversion audit", "content calendar",
        "rank track", "keyword gap", "newsletter", "case study",
    ]),
    ("opus48_medium", [
        "canonical fix", "canonical", "redirect", "footer", "link check",
        "internal link audit", "depth check", "orphan scan", "image rename",
        "deploy", "nap citation", "google map",
    ]),
]
DEFAULT = "opus48_medium"
```

- [ ] **Step 2: Update the docstring default note**

Change the docstring line `(a tier is always chosen; default is sonnet_medium).` → `(a tier is always chosen; default is opus48_medium).`

- [ ] **Step 3: Verify router runs against the new registry (no KeyError)**

Run:
```bash
python3 scripts/route.py "rebuild florida page from scratch"
python3 scripts/route.py "faq only update"
python3 scripts/route.py "canonical fix"
python3 scripts/route.py "write a blog post"
```
Expected, respectively:
```
opus48_max	claude-opus-4-8 / max
opus48_high	claude-opus-4-8 / high
opus48_medium	claude-opus-4-8 / medium
opus48_medium	claude-opus-4-8 / medium
```

- [ ] **Step 4: Commit**

```bash
git add scripts/route.py
git commit -m "fix(router): align route.py tier labels with Opus-4.8 registry"
```

---

### Task 5: Reconcile documentation (65→66, tier matrix, effort math)

**Files:**
- Modify: `CLAUDE.md:86`, `CLAUDE.md:312`
- Modify: `docs/reference/WORKFLOW.md` §Model Tier System (the table + effort paragraph)
- Modify: `scripts/health-sweep.sh` (cosmetic comment)

- [ ] **Step 1: Fix CLAUDE.md line 86 (model-tier description)**

Replace the sentence starting "All 65 agents are assigned to a 4-tier model system (Opus 4.8 / Opus 4.7 / Sonnet 4.6 / Haiku 4.5)…" with:

```
All 66 agents run on **Opus 4.8** (`claude-opus-4-8`), with three **effort** tiers (max / high / medium) as the cost lever, driven by `data/agent-registry.json`. Each agent's frontmatter carries `model:`, `effort:`, `dynamic_workflow:`. See `docs/reference/WORKFLOW.md §Model Tier System`. Dynamic Workflow routing is active on the 3 orchestrators (content-architect, structure-architect, batch-rebuilder). To change models/effort site-wide: edit the registry → `python3 scripts/apply_model_tiers.py` → `bash scripts/verify_model_tiers.sh`.
```

- [ ] **Step 2: Fix CLAUDE.md line 312 (health-sweep description)**

Change `agent integrity (65 agents + model tiers)` → `agent integrity (66 agents + model tiers)`.

- [ ] **Step 3: Replace the WORKFLOW.md §Model Tier System table**

Replace the 5-row tier table with:

```markdown
| Tier | Model | Effort | Use For | Count |
|---|---|---|---|---|
| `opus48_max` | `claude-opus-4-8` | max | Orchestrators, deep creative, competitor intelligence, high-traffic builds | 15 |
| `opus48_high` | `claude-opus-4-8` | high | Specialist page builders, narrative/schema content, SEO monitoring, analytics, conversion audits | 25 |
| `opus48_medium` | `claude-opus-4-8` | medium | Technical audits + pure-mechanical utilities + data monitoring | 26 |
```

- [ ] **Step 4: Fix the effort-math paragraph in WORKFLOW.md**

Update the sentence "(39 agents total: 14 max + 25 high)" → "(40 agents total: 15 max + 25 high)". Confirm the rest of the sentence (medium agents get no directive) still holds.

- [ ] **Step 5: Fix the health-sweep.sh comment (if present)**

Run: `grep -n '65' scripts/health-sweep.sh || echo "no 65 literal — skip"`. If a `65` agent-count comment exists, change it to `66`. (The functional check loops over files, so this is cosmetic only.)

- [ ] **Step 6: Verify docs are internally consistent**

Run:
```bash
grep -n '65 agent\|All 65\|Opus 4.7 / Sonnet' CLAUDE.md docs/reference/WORKFLOW.md || echo "NO STALE 65/4-tier REFERENCES"
grep -c 'opus48_' docs/reference/WORKFLOW.md
```
Expected: `NO STALE 65/4-tier REFERENCES`, then a count ≥ 3.

- [ ] **Step 7: Commit**

```bash
git add CLAUDE.md docs/reference/WORKFLOW.md scripts/health-sweep.sh
git commit -m "docs: reconcile model-tier docs to 66 agents on Opus 4.8 (3 effort tiers)"
```

---

### Task 6: (Optional) Normalize inert skill `model:` frontmatter

**Context:** Skills run in the caller's model context, so `model:` in skill frontmatter is ignored by Claude Code. 34 skills carry a (now-misleading) `model:` line; 7 carry none. This task removes the misleading lines so no reader believes a skill pins its own model. **Skip this task if the breeder prefers documentation parity over honesty** — it has zero runtime effect either way.

**Files:**
- Modify: all `skills/*.md` carrying a `model:` line

- [ ] **Step 1: List skills carrying a model line**

Run: `grep -l '^model:' skills/*.md | wc -l`
Expected: `34`

- [ ] **Step 2: Strip the inert model line from every skill**

Run:
```bash
for f in skills/*.md; do
  if grep -q '^model:' "$f"; then
    python3 - "$f" <<'PY'
import sys, re
f = sys.argv[1]
s = open(f).read()
s = re.sub(r'^model:.*\n', '', s, count=1, flags=re.MULTILINE)
open(f, 'w').write(s)
PY
  fi
done
echo "done"
```

- [ ] **Step 3: Verify no skill retains a model line**

Run: `grep -l '^model:' skills/*.md || echo "NO SKILL PINS A MODEL (correct)"`
Expected: `NO SKILL PINS A MODEL (correct)`

- [ ] **Step 4: Confirm skill frontmatter still valid (name + description intact)**

Run: `for f in skills/*.md; do head -1 "$f" | grep -q '^---' || echo "BAD FRONTMATTER $f"; done; echo "checked"`
Expected: `checked` with no `BAD FRONTMATTER` lines.

- [ ] **Step 5: Commit**

```bash
git add skills/*.md
git commit -m "chore(skills): remove inert model: frontmatter (skills run in caller context)"
```

---

### Task 7: End-to-end workflow integrity verification + push

**Files:** none modified — verification + deploy only.

- [ ] **Step 1: Every agent referenced in docs/registry has a file (no dangling handoffs)**

Run:
```bash
cd .claude/agents && ls *.md | sed 's/.md//' | sort > /tmp/files.txt
python3 -c "import json;print('\n'.join(sorted(json.load(open('../../data/agent-registry.json'))['agents'])))" > /tmp/reg.txt
diff /tmp/files.txt /tmp/reg.txt && echo "REGISTRY == FILES (66)"; cd ../..
```
Expected: `REGISTRY == FILES (66)` with no diff output.

- [ ] **Step 2: Sprint workflow agent names in WORKFLOW.md all resolve to real files**

Run:
```bash
grep -oE 'cag-[a-z-]+' docs/reference/WORKFLOW.md | sort -u | while read a; do
  [ -f ".claude/agents/$a.md" ] || [ -f "skills/$a.md" ] && : || echo "DANGLING: $a"
done; echo "workflow ref check done"
```
Expected: `workflow ref check done` with no `DANGLING:` lines (ignore obvious non-agent matches if any surface — investigate each).

- [ ] **Step 3: Router smoke test across all three tiers (re-confirm post-doc-edits)**

Run: `for t in "full silo rebuild" "hub page build" "redirect"; do python3 scripts/route.py "$t"; done`
Expected: `opus48_max`, then `opus48_high`, then `opus48_medium`.

- [ ] **Step 4: Full system health sweep (no build) to confirm agent integrity**

Run: `bash scripts/health-sweep.sh --no-build 2>&1 | tail -20`
Expected: agent-integrity section passes (every agent has `model:`); no `missing model:` failures.

- [ ] **Step 5: Astro build still green (nothing we touched breaks the site build)**

Run: `npx astro build 2>&1 | tail -15`
Expected: `Complete!` / build success, no errors. (If `astro` is unavailable in this environment, note it and rely on the auto-deploy build on push.)

- [ ] **Step 6: Final push (push = deploy, per CLAUDE.md non-negotiable)**

```bash
git push
```
Then confirm: `git status --short` is clean and `git log --oneline -7` shows the seven task commits.

- [ ] **Step 7: Post-deploy spot check**

Run (≈60s after push): `curl -sI https://congoafricangreys.com/ | grep HTTP`
Expected: `HTTP/2 200`.

---

## Self-Review

**Spec coverage:**
- *"Analyse all agents + skills for capability gap + recommend fix, deep compatibilities + tools needed"* → Task 1 (data scaffolds + tools line), Task 2 (Playwright/Lighthouse tool grants — the real "tools needed" gap), Task 6 (skill frontmatter honesty). ✓
- *"Upgrade all to Opus 4.8 except those that need 4.7 with honest reasons"* → Decisions section (honest reasoning: none need 4.7) + Task 3 (registry → all 4.8, effort preserved). ✓
- *"Check the workflow top-to-bottom is intact"* → Task 4 (router sync — would silently KeyError otherwise), Task 5 (doc reconciliation), Task 7 (registry==files, no dangling agent refs, router smoke test, health-sweep, astro build, deploy spot check). ✓

**Placeholder scan:** No "TBD/handle appropriately/etc." — every code/JSON block is complete and every step has an exact command + expected output. ✓

**Type/name consistency:** Tier keys are consistent across registry (Task 3), router (Task 4), and docs (Task 5): `opus48_max` / `opus48_high` / `opus48_medium`. Counts consistent everywhere: 15 / 25 / 26 = 66. The `apply_model_tiers.py` and `verify_model_tiers.sh` scripts are unchanged and already read these keys generically. ✓

**Ordering note:** Task 3 (registry) must run before Task 4 (router) because `route.py` resolves tier→model via the registry `_meta.tiers`; running the router before the registry rename would KeyError. Task 5 docs depend on the final counts from Task 3. Execute in the numbered order.

# Register CAG Skills (Skill-Tool Discovery) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. The skill-authoring steps additionally invoke **superpowers:writing-skills** (the "skill creation skill" the breeder asked for).

**Goal:** Make all 48 CAG skill files in `skills/*.md` discoverable and invokable through the Skill tool (and `/slash` commands), so `Skill cag-final-page-pass`, `Skill cag-blog-post`, etc. stop returning "Unknown skill."

**Architecture:** The canonical skill content stays in `skills/<name>.md` (referenced by ~68 agents, CLAUDE.md, memory, and docs as Read-targets — moving it would break hundreds of references). We add a **registration layer** at `.claude/skills/<name>/SKILL.md` — the only path Claude Code scans for skills — pointing at each canonical file. A generator script (`scripts/register_skills.py`) builds that layer idempotently from `skills/`, defaulting to relative **symlinks** (single source of truth, zero drift), with a `--copy` fallback if the loader doesn't follow symlinks. A QA check wires into `health-sweep.sh` so new skills can never silently go unregistered again.

**Tech Stack:** Python 3 (stdlib only), bash, git, Claude Code skill-discovery (`.claude/skills/*/SKILL.md`).

---

## Key facts (audit, 2026-06-28)

- `skills/` holds **48 `.md` files + 1 dir** (`cag-bird-page-excellence/SKILL.md`). None are discoverable — wrong path.
- **47/48 already have valid `name:`+`description:` frontmatter.** Only `cag-blog-post.md` lacks it.
- `.claude/skills/` **is git-tracked** (the openspec skills live there as real dirs). Only `.claude/worktrees/` is gitignored.
- Agents (`.claude/agents/`) are already registered — do **not** touch them.
- **Registration is read at session start.** After this plan runs, the breeder must start a *new* Claude Code session before the skills appear. Call this out in the handoff.
- Work happens on `main` (per CLAUDE.md "work on main, never feature branches"). No worktree.

### Classification — all 48 get registered

Registering a "passive catalog" as a Skill is harmless (it just becomes loadable by name; agents still Read it). So **register all 48** for simplicity and to honor "fix all." Three are reference/vocabulary catalogs — their descriptions get a "(reference catalog)" prefix so the model knows they're not builders: `cag-entity-agent`, `social-content`, `cag-site-patterns`. The 8 `framework-*` files are legitimate reference skills and register normally.

Full list (name = invocation name): anti-ai-writing, cag-bird-listing-page, cag-bird-page-build, cag-bird-page-excellence, cag-blog-post, cag-branded-hybrid-keywords, cag-branded-search-skill, cag-broken-links, cag-contact-form, cag-cta-strategy, cag-design-rebuild, cag-direction-d-theme, cag-entity-agent, cag-final-page-pass, cag-footer-agent, cag-google-map, cag-header-search, cag-image-generation, cag-indexing, cag-infographic, cag-location-page-builder, cag-logo-generator, cag-multi-agent-design, cag-photo-ingest, cag-seo-master-checklist, cag-site-patterns, cag-website-health, cag-youtube, cags-comprehensive-page-audit-system, caption-writer, framework-aida, framework-aio-geo, framework-bab, framework-ebp, framework-eeat, framework-heading-hierarchy, framework-pdb, framework-qab, grill-me, image-metadata, image-prompt-generator, internal-link-agent, keyword-cluster, manual-auditor-check, section-auditor, session-closer, sitemap-agent, social-content, youtube-script.

---

## File Structure

- Create: `scripts/register_skills.py` — generator: `skills/*.md` → `.claude/skills/<name>/SKILL.md` (symlink default, `--copy` fallback, `--check` mode).
- Modify: `skills/cag-blog-post.md` — prepend YAML frontmatter (only file missing it).
- Create: `.claude/skills/<name>/SKILL.md` × 48 — the registration layer (generated, committed).
- Modify: `scripts/health-sweep.sh` — add a "skills registered" gate calling `register_skills.py --check`.
- Modify: `CLAUDE.md` — add a Non-Negotiable note that skills are Skill-invokable + how to add a new one.
- Modify: `.claude/agents/cag-agent-system-qa.md` — add skill-registration to its audit checklist.
- Create: `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/project_skills_registration.md` + index line in `MEMORY.md`.

---

### Task 1: Decide symlink-vs-copy with a discovery probe

**Files:**
- Create: `.claude/skills/cag-final-page-pass/SKILL.md` (probe — symlink)

- [ ] **Step 1: Create one probe symlink (relative)**

```bash
cd /Users/apple/Downloads/CAG
mkdir -p .claude/skills/cag-final-page-pass
ln -sf ../../../skills/cag-final-page-pass.md .claude/skills/cag-final-page-pass/SKILL.md
```

- [ ] **Step 2: Verify the symlink resolves to real content**

```bash
head -3 .claude/skills/cag-final-page-pass/SKILL.md
```
Expected: prints `---` then `name: cag-final-page-pass` (the loader reads the target, not a broken link).

- [ ] **Step 3: Decision gate (requires a fresh session to confirm discovery)**

The loader only re-scans `.claude/skills/` at session start. Ask the breeder to open a new Claude Code session and run `Skill cag-final-page-pass`.
- If it loads → **symlink mode confirmed**; the generator's default (`symlink`) stands.
- If "Unknown skill" persists in the fresh session → loader is not following symlinks; rerun the generator in Task 4 with `--copy`.

Recommended: **symlink mode (Recommended)** — single source of truth, no content drift between `skills/` and `.claude/skills/`. Trade-off: depends on the loader following symlinks; Step 3 is the empirical check, and `--copy` is the documented fallback (its trade-off: two copies that the `--check` gate must keep in sync).

- [ ] **Step 4: Commit the probe**

```bash
git add .claude/skills/cag-final-page-pass/SKILL.md
git commit -m "chore(skills): probe symlink registration for cag-final-page-pass"
```

---

### Task 2: Fix the one skill missing frontmatter (`cag-blog-post.md`)

**Files:**
- Modify: `skills/cag-blog-post.md:1`

Invoke **superpowers:writing-skills** first to confirm frontmatter rules (name = kebab-case, third-person description with trigger conditions, ≤1024 chars). Then prepend the block. Do NOT delete the existing research body — only add a frontmatter header above line 1.

- [ ] **Step 1: Prepend YAML frontmatter above the current first line**

New first lines of `skills/cag-blog-post.md`:

```markdown
---
name: cag-blog-post
description: Use when building or rebuilding any CongoAfricanGreys.com blog post or the /blog/ hub — the 14-step section architecture, desktop+mobile component map, 8 cag-blog-* special-element components, tiered Sprint 0.5 research, Style-2 gated humor, and 1,800–2,500 intent-scaled word counts. Triggers: "write a blog post", "build the blog", "blog hub", "cage setup post", any /blog/<slug> page. Reconciled to DESIGN.md; source of truth docs/superpowers/specs/2026-06-27-cags-blog-cluster-system-design.md.
tools: [Read, Write, Bash]
---

```
(The existing `THIS PAGE CONTAIN THE CHATGTP RESEARCH WORK…` line becomes the first body line, immediately after the closing `---` + blank line.)

- [ ] **Step 2: Verify frontmatter parses**

```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
import re,sys
t=open('skills/cag-blog-post.md').read()
m=re.match(r'^---\n(.*?)\n---\n', t, re.S)
print("OK" if m and 'name: cag-blog-post' in m.group(1) and 'description:' in m.group(1) else "FAIL")
PY
```
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add skills/cag-blog-post.md
git commit -m "fix(skills): add name/description frontmatter to cag-blog-post"
```

---

### Task 3: Write the registration generator `scripts/register_skills.py`

**Files:**
- Create: `scripts/register_skills.py`

- [ ] **Step 1: Write the script**

```python
#!/usr/bin/env python3
"""Register CAG skills for Claude Code Skill-tool discovery.

Source of truth: skills/<name>.md (and skills/<name>/SKILL.md dir-skills).
Target (scanned by the loader): .claude/skills/<name>/SKILL.md

Modes:
  (default)   create/refresh relative symlinks
  --copy      copy file contents instead of symlinking (loader-without-symlink fallback)
  --check     verify every source skill is registered & in sync; exit 1 if not (CI/health gate)
"""
import os, re, sys, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "skills"
DST = ROOT / ".claude" / "skills"

def sources():
    """Yield (name, source_path) for every skill: flat .md files and <name>/SKILL.md dirs."""
    for p in sorted(SRC.glob("*.md")):
        yield p.stem, p
    for d in sorted(SRC.iterdir()):
        sk = d / "SKILL.md"
        if d.is_dir() and sk.exists():
            yield d.name, sk

def has_frontmatter(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    return bool(m and re.search(r"^name:\s*\S", m.group(1), re.M)
                  and re.search(r"^description:\s*\S", m.group(1), re.M))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check():
    bad = []
    for name, src in sources():
        if not has_frontmatter(src):
            bad.append(f"  MISSING FRONTMATTER: skills/{src.relative_to(SRC)}")
            continue
        tgt = DST / name / "SKILL.md"
        if not tgt.exists():
            bad.append(f"  NOT REGISTERED: {name}")
        elif not tgt.is_symlink() and sha(tgt) != sha(src):
            bad.append(f"  OUT OF SYNC (copy drift): {name} — rerun register_skills.py")
    if bad:
        print("Skill registration FAIL:")
        print("\n".join(bad))
        return 1
    print(f"Skill registration OK — {sum(1 for _ in sources())} skills registered.")
    return 0

def build(copy=False):
    n = 0
    for name, src in sources():
        if not has_frontmatter(src):
            print(f"  SKIP (no frontmatter): {name}")
            continue
        d = DST / name
        d.mkdir(parents=True, exist_ok=True)
        tgt = d / "SKILL.md"
        if tgt.exists() or tgt.is_symlink():
            tgt.unlink()
        if copy:
            tgt.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        else:
            rel = os.path.relpath(src, d)
            tgt.symlink_to(rel)
        n += 1
    print(f"Registered {n} skills ({'copy' if copy else 'symlink'} mode) -> .claude/skills/")
    return 0

if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    sys.exit(build(copy="--copy" in sys.argv))
```

- [ ] **Step 2: Make it executable and dry-verify the source list (no writes yet)**

```bash
cd /Users/apple/Downloads/CAG
chmod +x scripts/register_skills.py
python3 - <<'PY'
import importlib.util, pathlib
spec=importlib.util.spec_from_file_location("r","scripts/register_skills.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
src=list(m.sources())
print("source skills found:", len(src))
print("missing frontmatter:", [n for n,p in src if not m.has_frontmatter(p)])
PY
```
Expected: `source skills found: 49` and `missing frontmatter: []` (48 flat + 1 dir, after Task 2 fixed cag-blog-post).

- [ ] **Step 3: Commit the script**

```bash
git add scripts/register_skills.py
git commit -m "feat(skills): add register_skills.py generator (symlink/copy/check)"
```

---

### Task 4: Generate the full registration layer

**Files:**
- Create: `.claude/skills/<name>/SKILL.md` × 49 (generated)

- [ ] **Step 1: Run the generator (symlink mode, or --copy if Task 1 Step 3 said so)**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/register_skills.py            # add --copy ONLY if symlink discovery failed
```
Expected: `Registered 49 skills (symlink mode) -> .claude/skills/`

- [ ] **Step 2: Verify all targets resolve and frontmatter is reachable through them**

```bash
cd /Users/apple/Downloads/CAG
fail=0
for d in .claude/skills/*/; do
  n=$(basename "$d")
  [ "$n" = openspec-* ] && continue
  f="$d/SKILL.md"
  if [ ! -e "$f" ]; then echo "BROKEN: $n"; fail=1; continue; fi
  head -1 "$f" | grep -q '^---$' || { echo "NO FRONTMATTER VIA TARGET: $n"; fail=1; }
done
echo "fail=$fail"; python3 scripts/register_skills.py --check
```
Expected: `fail=0` then `Skill registration OK — 49 skills registered.`

- [ ] **Step 3: Commit the registration layer**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/skills/
git commit -m "feat(skills): register all 49 CAG skills for Skill-tool discovery"
```

---

### Task 5: Confirm discovery in a fresh session (acceptance test)

**Files:** none (verification only)

This is the real acceptance test — registration only loads at session start, so it cannot be confirmed in the building session.

- [ ] **Step 1: Open a new Claude Code session in the repo**

Tell the breeder to start a fresh session (registration is read at startup).

- [ ] **Step 2: Confirm the two originally-failing skills now load**

In the fresh session run, one at a time:
```
Skill cag-final-page-pass
Skill cag-blog-post
```
Expected: both launch (the SKILL.md body is presented), neither returns "Unknown skill."

- [ ] **Step 3: Spot-check three more across categories**

```
Skill grill-me
Skill cag-seo-master-checklist
Skill framework-qab
```
Expected: all three load. If any returns "Unknown skill," rerun `python3 scripts/register_skills.py --copy`, recommit `.claude/skills/`, and retest in another fresh session.

---

### Task 6: Sync docs, workflow, and memory

**Files:**
- Modify: `CLAUDE.md` (Non-Negotiable Rules section)
- Modify: `.claude/agents/cag-agent-system-qa.md`
- Create: `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/project_skills_registration.md`
- Modify: `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/MEMORY.md`

- [ ] **Step 1: Add a Non-Negotiable rule to CLAUDE.md**

Insert after the existing rules block (keep house wording/bolding style):

```markdown
- **Skills are registered & Skill-invokable (ALWAYS)** — Every `skills/<name>.md` (and `skills/<name>/SKILL.md` dir-skill) is the canonical source, and is mirrored into `.claude/skills/<name>/SKILL.md` by `scripts/register_skills.py` so the **Skill tool / `/<name>`** can load it by `name:`. `skills/` is still the file everything Reads; `.claude/skills/` is generated — never hand-edit it. **After adding, renaming, or deleting any skill, run `python3 scripts/register_skills.py` and commit `.claude/skills/`** (registration loads only at session start — a new skill is invisible until the next session). `health-sweep.sh` fails if a skill is unregistered or a `--copy` mirror drifts. Cause of the 2026-06-28 "Unknown skill: cag-final-page-pass / cag-blog-post" failures: the 48 skills sat in `skills/` (not scanned) and were never registered.
```

- [ ] **Step 2: Add skill-registration to the QA agent's checklist**

In `.claude/agents/cag-agent-system-qa.md`, add to its audit list:
```markdown
- **Skill registration:** run `python3 scripts/register_skills.py --check`. Every `skills/*.md` must have `name:`+`description:` frontmatter AND a matching `.claude/skills/<name>/SKILL.md`. A missing or drifted entry is a FAIL — fix by rerunning the generator and committing `.claude/skills/`.
```

- [ ] **Step 3: Write the memory file**

Create `project_skills_registration.md`:
```markdown
---
name: project-skills-registration
description: CAG skills must be registered into .claude/skills/ to be Skill-invokable; skills/ alone is not scanned
metadata:
  type: project
---

CAG's 48 `skills/*.md` files were never discoverable by the Skill tool — Claude Code only scans `.claude/skills/<name>/SKILL.md`, plugins, and `~/.claude/skills/`. `skills/` is a plain docs folder. This caused `Skill cag-final-page-pass` / `cag-blog-post` → "Unknown skill" (2026-06-28). Agents (`.claude/agents/`) were always fine; only skills were affected.

**Fix:** `scripts/register_skills.py` mirrors each `skills/<name>.md` into `.claude/skills/<name>/SKILL.md` (relative symlink by default; `--copy` fallback if the loader won't follow symlinks; `--check` for CI). `skills/` stays the canonical Read-target for ~68 agents + CLAUDE.md; `.claude/skills/` is generated, never hand-edited. Registration loads **only at session start** — a freshly added skill is invisible until the next session. Run the generator + commit `.claude/skills/` after any skill add/rename/delete; `health-sweep.sh` and [[reference_interior_page_standard]]'s QA gate enforce it. Only `cag-blog-post.md` was missing frontmatter (fixed). See [[project_blog_cluster_phase_c]].
```

- [ ] **Step 4: Add the MEMORY.md index line**

Append under the index:
```markdown
- [Skills Registration](project_skills_registration.md) — skills/ isn't scanned by the Skill tool; register_skills.py mirrors into .claude/skills/; run + commit after any skill change; loads only at session start
```

- [ ] **Step 5: Commit doc + memory sync**

```bash
cd /Users/apple/Downloads/CAG
git add CLAUDE.md .claude/agents/cag-agent-system-qa.md
git commit -m "docs(skills): document skill registration in CLAUDE.md + QA agent"
```
(Memory files live outside the repo — they save on Write, no commit needed.)

---

### Task 7: Wire the regression guard into health-sweep

**Files:**
- Modify: `scripts/health-sweep.sh`

- [ ] **Step 1: Add a skills gate near the agent-integrity check**

Insert a block (match the script's existing echo/section style):
```bash
echo "== Skill registration =="
if python3 scripts/register_skills.py --check; then
  echo "  skills: PASS"
else
  echo "  skills: FAIL (run: python3 scripts/register_skills.py && git add .claude/skills/)"
  HEALTH_FAIL=1   # use whatever the script's existing failure flag is named
fi
```
Read the script first to match its real failure-flag variable and section format — do not invent a new flag name.

- [ ] **Step 2: Run the sweep gate in isolation**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/register_skills.py --check && echo "GATE OK"
```
Expected: `Skill registration OK — 49 skills registered.` then `GATE OK`.

- [ ] **Step 3: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add scripts/health-sweep.sh
git commit -m "chore(health): fail health-sweep when a skill is unregistered"
git push origin main
```

---

## Self-Review

**1. Spec coverage**
- "Skills failed to load like the blog hub / cage-setup build" → root cause (wrong path) fixed by Tasks 1, 3, 4; acceptance-tested in Task 5.
- "Audit which skills are registered vs unknown" → done in this plan's audit section (all 48 unregistered; agents fine); `--check` makes it a standing, re-runnable audit.
- "Use the superpowers skill-creation skill to register them" → `writing-skills` invoked in Task 2 (frontmatter) and referenced for any rewrite; registration mechanized in Task 3.
- "Check full workflow, CLAUDE.md, memories" → Task 6 (CLAUDE.md rule, QA agent, memory + index) + Task 7 (health-sweep).

**2. Placeholder scan** — No TBDs. Every code/step has concrete content. The only deliberately deferred decision (symlink vs copy) has an explicit empirical gate (Task 1 Step 3) and a named fallback.

**3. Type/name consistency** — Generator function names (`sources`, `has_frontmatter`, `sha`, `check`, `build`) are used identically in Tasks 3, 4, 7. The `--check`/`--copy` flags are referenced consistently everywhere. Count "49" = 48 flat `.md` + 1 dir-skill, used consistently after Task 2 fixes the lone missing-frontmatter file.

**Open risk (not a blocker):** if Claude Code's loader requires the dir name to equal frontmatter `name:`, the generator already keys the dir off `name`/stem so they match. If a future skill's `name:` ≠ filename, `--check` won't catch the mismatch — add a name==stem assertion to `check()` if that ever happens.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-28-register-cag-skills.md`. Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration. Best here because Task 4 generates 49 files and Task 6 touches several docs — isolated review per task keeps it clean.

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints.

Note: **Task 5 (acceptance test) requires you to start a fresh Claude Code session** — registration only loads at startup, so neither execution mode can self-verify discovery without a restart.

Which approach?
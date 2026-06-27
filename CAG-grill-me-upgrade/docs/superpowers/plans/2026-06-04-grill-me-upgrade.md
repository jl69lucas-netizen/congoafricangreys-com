# Grill-Me Skill Upgrade + Site-Wide Mid-Build Clarification Checkpoint — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Evolve `skills/grill-me.md` from a front-loaded interview into a checkpointed discovery system, and add a site-wide rule so build agents ask one clarifying question mid-build (instead of stopping or guessing) whenever the existing ≥97% Confidence Gate is not met.

**Architecture:** Two parts. **Part A** rewrites `skills/grill-me.md` to add real-time checkpointing (write the brief incrementally, after every answer), a verbatim Q&A Log, a Key Decisions log, an Open Flags section, a codebase-first "don't ask what the repo knows" rule, scaled relentless/branch-by-branch interviewing (full for complex builds, fast path for simple fixes), a `--resume` re-grill mode, and a downstream-doc feedback loop. **Part B** adds a non-negotiable **Clarification Checkpoint** rule to `CLAUDE.md` and injects it into all 66 agent Golden Rules via a new idempotent script `scripts/add_clarification_checkpoint_golden_rule.py` (modeled on the existing `scripts/add_first_person_golden_rule.py`). The checkpoint reuses the existing Confidence Gate as its trigger and writes mid-build questions into the same live session-brief file Part A maintains.

**Tech Stack:** Markdown skill/agent files, Python 3 (stdlib only) for the injection script, Bash for verification, git for deploy. No new dependencies.

**Testing note (Iron Law — writing-skills TDD):** No skill edit ships without a failing baseline test first. Task 1 runs pressure scenarios against the *current* skill and records the failures. Task 12 re-runs them to prove the upgrade fixes them. Tests here = subagent pressure scenarios, per `superpowers:writing-skills` → `testing-skills-with-subagents.md`.

---

## File Structure

| File | Responsibility |
|---|---|
| `skills/grill-me.md` (modify) | The upgraded session-starter skill: checkpointing, Q&A log, open flags, codebase-first, scaled interviewing, `--resume`, feedback loop |
| `scripts/add_clarification_checkpoint_golden_rule.py` (create) | Idempotent injection of the Clarification Checkpoint blockquote line into every `.claude/agents/*.md` Golden Rule |
| `CLAUDE.md` (modify) | Add Clarification Checkpoint to `## Non-Negotiable Rules`; register the new script under `## Scripts` |
| `.claude/agents/*.md` (modified by script) | Each gains one Golden Rule line — written by the script, not by hand |
| `docs/superpowers/plans/2026-06-04-grill-me-upgrade.md` (this file) | The plan |
| `sessions/2026-06-04-grill-me-baseline.md` (create in Task 1) | Recorded baseline failures (the RED evidence) |

---

## Task 1: RED — Record baseline failures of the current skill

**Files:**
- Create: `sessions/2026-06-04-grill-me-baseline.md`
- Read-only: `skills/grill-me.md`

- [ ] **Step 1: Run three pressure scenarios against the CURRENT skill (no edits yet)**

Dispatch a subagent (general-purpose) once per scenario with this exact framing, and record verbatim what it does:

1. **Context-loss scenario:** "You are running the grill-me skill for a homepage rebuild. The session has gone 40 messages deep. The user now asks 'what did I say in Q3 about the worst-performing page?' Show how you retrieve it." — *Expected failure:* no verbatim Q&A is persisted; the agent reconstructs from memory or cannot answer.
2. **Resume scenario:** "A `sessions/2026-06-02-session-brief.md` already exists. The user says 'grill me again, I have new breakthroughs on the Florida page.' Run grill-me." — *Expected failure:* skill has no `--resume` path; it starts a fresh full interview or overwrites.
3. **Mid-build clarity scenario:** "You are `cag-section-builder` building a hero. The brief doesn't say which CTA label to use and you're ~85% confident. What do you do?" — *Expected failure:* agent either dead-stops (current Confidence Gate) or guesses; it does not ask one question, log it, and continue.

- [ ] **Step 2: Write the baseline record**

Create `sessions/2026-06-04-grill-me-baseline.md` containing, for each scenario: the verbatim agent behavior, the exact rationalization/limitation observed, and which upgrade task addresses it. This is the RED evidence the GREEN phase (Task 12) must overturn.

- [ ] **Step 3: Commit the baseline**

```bash
git add sessions/2026-06-04-grill-me-baseline.md
git commit -m "test(grill-me): record baseline failures before upgrade (RED)"
```

---

## Task 2: Add real-time checkpointing (write the brief skeleton before Q1)

**Files:**
- Modify: `skills/grill-me.md` (the `## Startup Sequence` section, end of it, and `## Purpose`)

- [ ] **Step 1: Add a checkpointing principle to the Purpose section**

In `skills/grill-me.md`, find the Purpose paragraph that ends with "Every answer shapes the session brief you write at the end." Replace that sentence with:

```markdown
You ask questions one at a time. Never batch them. Never rush.

**Checkpointing (non-negotiable):** You do NOT hold answers in your head until the end. You create the session-brief file *before Q1* and append each answer to it the moment you receive it. In long sessions the context window fills and earlier answers drift — the file on disk is the source of truth, not your memory. After every single answer: write to the file, then ask the next question.
```

- [ ] **Step 2: Add a "write the skeleton brief" step at the end of the Startup Sequence**

In `## Startup Sequence — Do This First, In Order`, after the "Announce that you've loaded the project context" block, add:

```markdown
After announcing context is loaded, **immediately create the skeleton brief** at `sessions/YYYY-MM-DD-session-brief.md` (today's date) with all section headings present but empty:

\`\`\`markdown
# Session Brief — YYYY-MM-DD

## Discovery Summary
_(filled after the interview)_

## Q&A Log
_(appended after every answer — verbatim)_

## Key Decisions
_(appended as decisions are made)_

## Open Flags
_(unresolved items / needs another source / revisit)_

## SESSION CONTEXT
_(synthesized at the end)_

## Today's Target

## Constraints

## Repeat / Avoid

## Urgency

## Recommended Next Steps

## Clarification Log (mid-build)
_(appended by build agents when the Confidence Gate fires — see CLAUDE.md Clarification Checkpoint)_

## What's Next
_(filled at end of build session)_
\`\`\`

Confirm: "Skeleton brief created at `sessions/YYYY-MM-DD-session-brief.md` — I'll update it after every answer." Then ask Q1.
```

- [ ] **Step 3: Verify the edit is coherent**

Run: `grep -n "Checkpointing (non-negotiable)" skills/grill-me.md` and `grep -n "skeleton brief" skills/grill-me.md`
Expected: each returns at least one line.

- [ ] **Step 4: Commit**

```bash
git add skills/grill-me.md
git commit -m "feat(grill-me): real-time checkpointing — skeleton brief before Q1"
```

---

## Task 3: Add the Q&A Log, Key Decisions, and Open Flags append behavior

**Files:**
- Modify: `skills/grill-me.md` (new subsection after `## Question Framework` intro; and the `## After the Last Answer` template)

- [ ] **Step 1: Add an "After Each Answer" subsection**

In `skills/grill-me.md`, immediately before `### Business Layer (always asked first — Q1 through Q5)`, insert:

```markdown
### After EACH Answer — Append Before Asking the Next Question

The moment the user answers any question, do this **before** asking the next one:

1. **Append to `## Q&A Log`** in the brief, verbatim:
   \`\`\`
   **Q{n} — {short topic}** ({HH:MM})
   > {the exact question you asked}

   {the user's answer, verbatim — do not paraphrase}
   \`\`\`
2. **If the answer settled a decision**, append a one-line entry to `## Key Decisions`:
   `- {decision} — chosen because {reason from the answer}`
3. **If the answer revealed a gap** (missing data, needs another person/source, "I'm not sure"), append to `## Open Flags`:
   `- [ ] {what's unresolved} — {where the answer might come from}`

Only after the file is updated do you ask the next question. If you skip the append, you have violated the checkpointing rule.
```

- [ ] **Step 2: Replace the end-of-session brief template's top with the new structured sections**

In `## After the Last Answer → ### Step 1 — Write the Session Brief`, the template currently starts with `## Business Focus`. Replace the line `## Business Focus\n[1-2 sentences synthesizing Q1-Q4 answers]` with:

```markdown
## Discovery Summary
[3-4 sentence high-level synthesis of Q1–Q5: what the user needs today and why]

## Business Focus
[1-2 sentences synthesizing Q1-Q4 answers]
```

(The `## Q&A Log`, `## Key Decisions`, `## Open Flags`, and `## Clarification Log` sections already exist from the skeleton in Task 2 — at the end you only *finalize/clean* them, you do not recreate them.)

- [ ] **Step 3: Add a finalize note**

At the end of `### Step 1`, before the "Confirm to user" line, add:

```markdown
Before confirming, re-read the on-disk `## Q&A Log` to write `## Discovery Summary`, `## SESSION CONTEXT`, and `## Recommended Next Steps` — synthesize from the persisted log, not from memory. Leave `## Open Flags` and `## Clarification Log` intact for the build session.
```

- [ ] **Step 4: Verify**

Run: `grep -n "After EACH Answer" skills/grill-me.md && grep -n "Discovery Summary" skills/grill-me.md && grep -n "verbatim — do not paraphrase" skills/grill-me.md`
Expected: all three return a line.

- [ ] **Step 5: Commit**

```bash
git add skills/grill-me.md
git commit -m "feat(grill-me): verbatim Q&A log + key-decisions + open-flags append after each answer"
```

---

## Task 4: Add codebase-first rule + scaled relentless / branch-by-branch interviewing

**Files:**
- Modify: `skills/grill-me.md` (`## Rules You Must Follow`; and a new subsection after the Workflow Gate Check / before Q7, plus a task-classification step at Q6)

- [ ] **Step 1: Add the codebase-first rule and the relentless/branch rules to "Rules You Must Follow"**

In `## Rules You Must Follow`, append these numbered rules after the existing rule 6:

```markdown
7. **Codebase-first — never ask what the repo already answers.** Before asking any question, check whether the answer is already in the repo (the files from the Startup Sequence, `data/`, `src/pages/`, `sessions/`). If it is, state the finding and ask only for confirmation — do not ask an open-ended question. Example: don't ask "what's the Timneh price?" — read `data/price-matrix.json`, state it, ask "still $1,200–$2,500?"
8. **Relentless until shared understanding — on COMPLEX builds only.** If an answer is vague ("make it better", "the usual"), ask a focused follow-up before moving on. Resolve one branch of the design tree fully before opening the next. Cap follow-ups at 2 per question so you dig without interrogating.
9. **Fast path for SIMPLE tasks.** Classify the task at Q6 (see below). For SIMPLE tasks, skip the relentless follow-ups and the full question set — speed matters more than depth on a 5-minute fix.
```

- [ ] **Step 2: Add a task-classification step at Q6**

In the Task Layer, immediately after the `**Q6 — Specific Target**` block and before the "After Q6, run the Workflow Gate Check" line, insert:

```markdown
**After Q6, classify the task (silently) before the gate check:**

- **SIMPLE** = single-section edit, copy tweak, one-image swap, a known bug fix, or a metadata change. → Run only Q1, Q6, Q7, the Workflow Gate Check, and Q14. Skip Q2–Q5, Q8–Q13 and all relentless follow-ups. Write the brief with the skipped fields marked `n/a (simple task)`.
- **COMPLEX** = new page, full rebuild, multi-section build, new content cluster, or anything touching ≥3 sections. → Run the full question set with relentless follow-ups (Rule 8) and branch-by-branch exploration.

State your classification to the user in one line and let them override: "I'm treating this as a {SIMPLE|COMPLEX} task — say 'switch' if that's wrong." Then proceed.
```

- [ ] **Step 3: Verify**

Run: `grep -n "Codebase-first" skills/grill-me.md && grep -n "Relentless until shared understanding" skills/grill-me.md && grep -n "classify the task" skills/grill-me.md`
Expected: all three return a line.

- [ ] **Step 4: Commit**

```bash
git add skills/grill-me.md
git commit -m "feat(grill-me): codebase-first rule + scaled relentless/branch interviewing (simple vs complex)"
```

---

## Task 5: Add the `--resume` re-grill mode

**Files:**
- Modify: `skills/grill-me.md` (new top-level section after `## Purpose`)

- [ ] **Step 1: Add the Resume Mode section**

In `skills/grill-me.md`, immediately after the `## Purpose` section (before `## Startup Sequence`), insert:

```markdown
## Modes

`grill-me` runs in two modes:

- **Fresh (default):** full Startup Sequence + interview, new dated brief.
- **Resume:** triggered by `grill-me --resume`, "grill me again", or "I have new breakthroughs". Use when a brief already exists for work still in progress.

### Resume Mode — Do This Instead of a Fresh Interview

1. **Run** `ls -t sessions/*-session-brief.md | head -1` via Bash to find the latest brief. If none exists, fall back to Fresh mode and say so.
2. **Read** that brief in full — especially `## Key Decisions`, `## Open Flags`, and `## What's Next`.
3. **Replay context** to the user in one message: "Resuming `{filename}`. Last we decided: {top 2–3 decisions}. Still open: {open flags}. What's the new breakthrough or change?"
4. **Append, never overwrite.** Add a new dated round to the existing brief:
   \`\`\`markdown
   ---
   ## Re-Grill — YYYY-MM-DD HH:MM
   {new Q&A appended to ## Q&A Log as usual}
   {new decisions appended to ## Key Decisions}
   {resolved flags: check the box in ## Open Flags; add new ones}
   \`\`\`
5. Walk only the branches the breakthrough touches — do not re-ask settled questions (codebase-first + Key Decisions already answer them).
6. Update `## Recommended Next Steps` to reflect the new state.
```

- [ ] **Step 2: Verify**

Run: `grep -n "Resume Mode" skills/grill-me.md && grep -n "grill me again" skills/grill-me.md && grep -n "Append, never overwrite" skills/grill-me.md`
Expected: all three return a line.

- [ ] **Step 3: Commit**

```bash
git add skills/grill-me.md
git commit -m "feat(grill-me): --resume re-grill mode (append new round, never re-ask settled decisions)"
```

---

## Task 6: Extend the feedback loop beyond CLAUDE.md

**Files:**
- Modify: `skills/grill-me.md` (`### Step 2 — Propose CLAUDE.md Patch` → broaden to downstream docs)

- [ ] **Step 1: Add a downstream-doc check after the CLAUDE.md patch**

In `### Step 2 — Propose CLAUDE.md Patch`, after the line `If yes → write. If skip → move on.`, insert:

```markdown
**Then — Downstream Doc Check (feedback loop).** A grill session often surfaces a reusable nuance that belongs in a skill or guide, not just today's brief. Scan for these and propose (do not auto-write) updates:

| If the session revealed… | Propose updating… |
|---|---|
| A new repeatable build technique or gotcha | the relevant `skills/*.md` |
| A new framework/component choice rule | `docs/reference/components.md` or `docs/reference/seo-rules.md` |
| A new factual constraint (pricing, CITES, credential) | `data/*.json` + the Verified-Claim Ledger |
| A recurring question worth a permanent answer | this skill (`skills/grill-me.md`) — but only via the writing-skills TDD process |

For each, show the exact proposed change and ask "write this? (yes / skip)". Never auto-edit a downstream doc. Editing `grill-me.md` itself requires a failing test first (writing-skills Iron Law) — flag it for a separate session, don't do it inline.
```

- [ ] **Step 2: Verify**

Run: `grep -n "Downstream Doc Check" skills/grill-me.md`
Expected: returns a line.

- [ ] **Step 3: Commit**

```bash
git add skills/grill-me.md
git commit -m "feat(grill-me): close the feedback loop — propose downstream-doc updates after session"
```

---

## Task 7: Update the frontmatter description for CSO (triggering-only, no workflow summary)

**Files:**
- Modify: `skills/grill-me.md:2-4` (frontmatter `description`)

- [ ] **Step 1: Replace the description**

The current description summarizes the workflow ("grills you on… 12–13 questions…writes a session brief…proposes a CLAUDE.md patch"). Per `superpowers:writing-skills` CSO, descriptions must state *when to use*, not *what it does*. Replace the `description:` line (line 3) with:

```yaml
description: Use when starting a CAG work session, before building or fixing any page; also use to resume an in-progress session ("grill me again" / new breakthroughs) or when a prior session brief exists and needs continuing. Run after Sprint 0 intelligence is complete.
```

- [ ] **Step 2: Verify frontmatter still parses (name + description present, no stray colons breaking YAML)**

Run: `head -5 skills/grill-me.md`
Expected: lines 1–5 show `---`, `name: grill-me`, the new `description:`, `tools: [Read, Write, Bash]`, `---`.

- [ ] **Step 3: Commit**

```bash
git add skills/grill-me.md
git commit -m "docs(grill-me): CSO — description states triggers only, adds resume trigger"
```

---

## Task 8: Create the Clarification Checkpoint injection script

**Files:**
- Create: `scripts/add_clarification_checkpoint_golden_rule.py`
- Reference (do not modify): `scripts/add_first_person_golden_rule.py`

- [ ] **Step 1: Write the script**

Create `scripts/add_clarification_checkpoint_golden_rule.py` with exactly this content:

```python
#!/usr/bin/env python3
"""Inject the Clarification Checkpoint rule into every agent's Golden Rule block.

Idempotent: skips any file that already contains the marker phrase.
Inserts the rule as the first blockquote line directly under `## Golden Rule`.
Pairs with the CLAUDE.md Non-Negotiable rule of the same name.
"""
import pathlib
import sys

AGENTS = pathlib.Path(__file__).resolve().parent.parent / ".claude" / "agents"
MARKER = "Clarification Checkpoint (ALWAYS)"
LINE = (
    "> **Clarification Checkpoint (ALWAYS):** The ≥97% Confidence Gate is not a dead "
    "stop. When confidence drops below 97% mid-build, do NOT guess and do NOT silently "
    "halt — ask the user ONE focused question, append it to the live "
    "`sessions/YYYY-MM-DD-session-brief.md` under `## Clarification Log (mid-build)` "
    "(question + answer, verbatim), apply the answer, and continue. Codebase-first: if "
    "the repo answers it, read it instead of asking.\n"
)

changed, skipped, no_rule = [], [], []

for f in sorted(AGENTS.glob("*.md")):
    text = f.read_text()
    if MARKER in text:
        skipped.append(f.name)
        continue
    lines = text.splitlines(keepends=True)
    out, inserted = [], False
    for ln in lines:
        out.append(ln)
        if not inserted and ln.strip() == "## Golden Rule":
            out.append(LINE)
            inserted = True
    if not inserted:
        no_rule.append(f.name)
        continue
    f.write_text("".join(out))
    changed.append(f.name)

print(f"changed: {len(changed)}")
print(f"skipped (already had marker): {len(skipped)}")
print(f"NO '## Golden Rule' heading: {len(no_rule)} -> {no_rule}")
if no_rule:
    sys.exit(0)  # report, don't fail
```

- [ ] **Step 2: Dry-run sanity check (do NOT run the injection yet)**

Run: `python3 -c "import ast; ast.parse(open('scripts/add_clarification_checkpoint_golden_rule.py').read()); print('syntax OK')"`
Expected: `syntax OK`

- [ ] **Step 3: Commit the script (before running it, so the injection is a separate reviewable commit)**

```bash
git add scripts/add_clarification_checkpoint_golden_rule.py
git commit -m "feat(scripts): add Clarification Checkpoint Golden Rule injector"
```

---

## Task 9: Run the injection across all 66 agents

**Files:**
- Modified by script: `.claude/agents/*.md`

- [ ] **Step 1: Run the injector**

Run: `python3 scripts/add_clarification_checkpoint_golden_rule.py`
Expected output form:
```
changed: 66
skipped (already had marker): 0
NO '## Golden Rule' heading: 0 -> []
```
(If `changed` < 66, the difference must equal `skipped` + `no_rule`. Any `no_rule` file is an agent missing a `## Golden Rule` heading — note it; do not hand-edit in this task.)

- [ ] **Step 2: Verify injection landed correctly on a sample agent**

Run: `sed -n '/## Golden Rule/,/^---/p' .claude/agents/cag-section-builder.md`
Expected: the first blockquote line under `## Golden Rule` is the Clarification Checkpoint line, followed by the existing First-Person, Golden Rule, and Confidence Gate lines.

- [ ] **Step 3: Verify count across the whole tree**

Run: `grep -rl "Clarification Checkpoint (ALWAYS)" .claude/agents/ | wc -l`
Expected: `66` (or `66 minus any no_rule files`).

- [ ] **Step 4: Re-run the injector to prove idempotency**

Run: `python3 scripts/add_clarification_checkpoint_golden_rule.py`
Expected: `changed: 0`, `skipped (already had marker): 66`.

- [ ] **Step 5: Commit**

```bash
git add .claude/agents/
git commit -m "feat(agents): inject Clarification Checkpoint into all 66 Golden Rules"
```

---

## Task 10: Add the non-negotiable rule to CLAUDE.md + register the script

**Files:**
- Modify: `CLAUDE.md` (`## Non-Negotiable Rules`; `## Scripts`)

- [ ] **Step 1: Add the Clarification Checkpoint to Non-Negotiable Rules**

In `CLAUDE.md`, in `## Non-Negotiable Rules`, immediately after the `**Confidence Gate**` bullet, add this bullet:

```markdown
- **Clarification Checkpoint (ALWAYS) — applies to every agent, skill, and build** — The Confidence Gate is not a dead stop. Mid-build, whenever confidence on a decision drops below 97% (a CTA label, a component pick, an ambiguous instruction, a missing fact), do NOT guess and do NOT silently halt: ask the user **one** focused question, append it (question + answer, verbatim) to the live `sessions/YYYY-MM-DD-session-brief.md` under `## Clarification Log (mid-build)`, apply the answer, and keep building. Codebase-first: if the repo answers it (`data/`, `src/pages/`, prior briefs), read it instead of asking. This pairs with the `grill-me` skill, which now maintains that brief in real time. Injected into every agent Golden Rule via `scripts/add_clarification_checkpoint_golden_rule.py`.
```

- [ ] **Step 2: Register the script under `## Scripts`**

In `CLAUDE.md`, in `## Scripts`, after the `add_first_person_golden_rule.py` line, add:

```markdown
- `scripts/add_clarification_checkpoint_golden_rule.py` — idempotent injection of the Clarification Checkpoint rule into every agent's `## Golden Rule` (applied to all 66, 2026-06-04). Pairs with the CLAUDE.md Non-Negotiable rule of the same name and the upgraded `grill-me` skill.
```

- [ ] **Step 3: Verify**

Run: `grep -n "Clarification Checkpoint" CLAUDE.md`
Expected: at least two lines (the non-negotiable rule + the script registration).

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs(CLAUDE): register Clarification Checkpoint non-negotiable rule + injection script"
```

---

## Task 11: Update the grill-me skill registration line in CLAUDE.md

**Files:**
- Modify: `CLAUDE.md` (the `skills/grill-me.md` description under `#### SEO & Content Skills`)

- [ ] **Step 1: Update the registration to mention resume + checkpointing**

In `CLAUDE.md`, find the line beginning `` - `skills/grill-me.md` — Sprint 0.5 session starter; ``. Replace its descriptive text with:

```markdown
- `skills/grill-me.md` — Sprint 0.5 session starter; reads gap matrix + top-pages + last brief, then runs a **checkpointed** interview (writes the brief skeleton before Q1, appends a verbatim Q&A log + key decisions + open flags after every answer). Scales depth: full relentless/branch interview for COMPLEX builds, fast path for SIMPLE fixes; codebase-first (never asks what the repo answers). Supports **`--resume` / "grill me again"** to continue an existing brief without re-asking settled decisions. Pairs with the site-wide **Clarification Checkpoint** rule so the same brief captures mid-build questions. Run AFTER Sprint 0; handoff: grill-me → `@cag-content-audit-agent` → Section Map + Component Gate → build.
```

- [ ] **Step 2: Verify**

Run: `grep -n "checkpointed" CLAUDE.md`
Expected: returns the grill-me line.

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs(CLAUDE): update grill-me registration — checkpointing + resume + clarification pairing"
```

---

## Task 12: GREEN — Re-run the baseline scenarios and prove the fix

**Files:**
- Modify: `sessions/2026-06-04-grill-me-baseline.md` (append a "GREEN — Re-test" section)

- [ ] **Step 1: Re-run the three Task 1 scenarios against the UPGRADED skill**

Dispatch the same three subagent scenarios from Task 1, Step 1. Expected results:
1. **Context-loss:** agent reads `## Q&A Log` from the on-disk brief and quotes Q3 verbatim. PASS.
2. **Resume:** agent enters Resume Mode, replays Key Decisions + Open Flags, appends a new dated round, does not re-ask settled questions. PASS.
3. **Mid-build clarity:** agent asks ONE question, appends it to `## Clarification Log (mid-build)`, applies the answer, continues — neither dead-stops nor guesses. PASS.

- [ ] **Step 2: Add a loophole scenario (REFACTOR probe)**

Dispatch one more: "You're `cag-location-builder`, mid-build, 88% confident on whether to use the 1100px or 1200px container. You're in a hurry. What do you do?" — *Pass:* asks one question + logs it (or reads `docs/reference/page-width.md` per codebase-first and proceeds). *Fail:* rationalizes skipping the checkpoint because of time pressure → if so, add an explicit counter to the CLAUDE.md rule and re-test.

- [ ] **Step 3: Record GREEN results**

Append a `## GREEN — Re-test (2026-06-04)` section to `sessions/2026-06-04-grill-me-baseline.md` with verbatim pass/fail for all four scenarios. If any failed, fix the specific rule/skill text, re-commit, and re-run before proceeding.

- [ ] **Step 4: Commit**

```bash
git add sessions/2026-06-04-grill-me-baseline.md
git commit -m "test(grill-me): GREEN — upgraded skill + checkpoint pass all baseline scenarios"
```

---

## Task 13: Final verification + push (deploy)

**Files:** none (verification + git only)

- [ ] **Step 1: Confirm no agent lost its First-Person rule during injection**

Run: `grep -rL "First-Person Brand Voice" .claude/agents/ ; echo "exit: $?"`
Expected: no filenames printed (every agent still has the First-Person line) — injection only adds, never removes.

- [ ] **Step 2: Confirm both Golden Rule lines coexist on a sample**

Run: `grep -c "ALWAYS" .claude/agents/cag-homepage-builder.md`
Expected: ≥2 (First-Person + Clarification Checkpoint both present).

- [ ] **Step 3: Run the system health sweep (no build needed for doc/skill changes)**

Run: `bash scripts/health-sweep.sh --no-build`
Expected: agent integrity check passes (66 agents), no secret leaks, git state clean except intended changes.

- [ ] **Step 4: Push (push = deploy)**

```bash
git push
```
Expected: push succeeds to `main`; GitHub Actions → Cloudflare Pages auto-deploys. (Skill/agent/doc changes do not alter `dist/`, so the live site is unaffected — this is a tooling deploy.)

- [ ] **Step 5: Update the baseline session file's "What's Next"**

Note in `sessions/2026-06-04-grill-me-baseline.md`: the upgrade is live; next real grill session should be run in Resume mode if a brief exists, and the first mid-build Confidence-Gate dip is the live test of the Clarification Checkpoint.

```bash
git add sessions/2026-06-04-grill-me-baseline.md
git commit -m "docs(session): grill-me upgrade complete + live" && git push
```

---

## Self-Review

**Spec coverage** (against the four source concepts + your headline ask):

| Source concept | Task(s) |
|---|---|
| 1. Real-time checkpointing | Task 2 (skeleton before Q1) + Task 3 (append after each answer) |
| 2a. Discovery Notes & Summary | Task 3 (Discovery Summary) |
| 2b. Key Decisions | Task 2 (section) + Task 3 (append) |
| 2c. Step-by-step Q&A log | Task 2 (section) + Task 3 (verbatim append) |
| 2d. Open Flags | Task 2 (section) + Task 3 (append) |
| 3a. Relentless until shared understanding | Task 4 (Rule 8, complex only) |
| 3b. Branch-by-branch | Task 4 (Rule 8) |
| 3c. One at a time | Already present (Rule 1) — preserved |
| 3d. Codebase awareness | Task 4 (Rule 7) |
| 4a. Update downstream docs | Task 6 |
| 4b. Iterative grilling | Task 5 (`--resume`) |
| ★ Mid-build questioning | Task 8–10 (Clarification Checkpoint, tied to ≥97% gate) |
| CSO description fix | Task 7 |
| Registration | Task 10 + Task 11 |
| TDD (Iron Law) | Task 1 (RED) + Task 12 (GREEN/REFACTOR) |

No spec gaps.

**Placeholder scan:** every code/content step contains the literal text to insert and an exact verify command. No "TBD"/"add appropriate"/"similar to Task N".

**Type/name consistency:** the brief section headings are identical everywhere — `## Q&A Log`, `## Key Decisions`, `## Open Flags`, `## Clarification Log (mid-build)`, `## Discovery Summary` — created in Task 2, appended in Task 3/5, written-to by the Task 8 script and the Task 10 CLAUDE.md rule. The marker phrase `Clarification Checkpoint (ALWAYS)` is identical in the script (Task 8), the agent lines, the CLAUDE.md rule (Task 10), and the verify greps (Task 9, 10). The trigger is the existing `≥97% Confidence Gate` throughout.

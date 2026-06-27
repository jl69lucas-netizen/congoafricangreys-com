# Foundations Phase — Image Art-Direction + Anti-AI Voice + Strategy Synthesizer

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the three foundation pieces the 9-blog-posts + hub build depends on — `IMAGE-DESIGNS.md` (image art-direction source of truth), a reusable `anti-ai-writing` skill, and a new `cag-strategy-synthesizer` agent that turns existing research into two reverse-engineered strategies (and derives the 9 blog topics + hub).

**Architecture:** Three independently-shippable deliverables (A: doc, B: skill, C: agent) plus a wiring/verification group (D). Each follows the CAG governance pattern: write the artifact → wire it into consumers via an idempotent script (mirroring `scripts/add_interior_standard_pointer.py`) → register in CLAUDE.md → verify with `cag-agent-system-qa` + `scripts/health-sweep.sh`. The anti-AI skill follows the writing-skills Iron Law (RED baseline before writing). The strategy agent follows the model-tier registry pattern (`data/agent-registry.json` → `apply_model_tiers.py` → `verify_model_tiers.sh`).

**Tech Stack:** Markdown (docs/skills/agents), Python 3 idempotent patch scripts, existing CAG governance scripts, `cag-agent-system-qa` agent, `scripts/health-sweep.sh`.

**Out of scope (later phases, do NOT build here):**
- The 9 blog posts + hub build (Phase 2 — starts once C produces the topic list).
- Social export bridge (#1) — partly exists already (`scripts/social_to_csv.py` hardcodes a launch-week CSV; `scripts/route.py`). Phase 3 = upgrade it to read `content/social/calendar.md` dynamically. Do not touch here.
- Cloudflare super-images (#5b) — deferred; optional mode inside `cag-image-pipeline` only if pursued.
- System hardening / agent-permissions / MCP audit — folded into Task D verification here; full pass is its own later phase.

**Governance constraints (binding on every task):**
- **Confidence Gate ≥97%** before writing any `site/content/` file. (This phase writes docs/skills/agents, not site files, but the strategy agent's *output* must respect it.)
- **Commit + push after each deliverable** (push = deploy). Branch off `main` first — do not commit foundation work directly to `main` without a branch.
- **Recommend + Why** is codified *into* the strategy agent (Task C), not just followed by us.
- **No visible dates, CITES Appendix I + captive-bred-USA, first-person voice, line-icon SVGs (never 🦜)** — apply to all content these artifacts govern.

---

## File Structure

| File | Responsibility | Task |
|---|---|---|
| `IMAGE-DESIGNS.md` (repo root) | Image art-direction source of truth: crop ratios, style wrapper, negative list, lighting, focal length, scene-types per page type | A |
| `scripts/add_image_designs_pointer.py` | Idempotent: inject "read IMAGE-DESIGNS.md first" pointer into the 6 image consumers | A |
| `skills/anti-ai-writing.md` | Reusable anti-AI phrase/rhythm blacklist + human alternatives | B |
| `sessions/2026-06-17-anti-ai-baseline.md` | RED baseline capture (AI-slop tells, verbatim) — the failing test | B |
| `.claude/agents/cag-strategy-synthesizer.md` | New agent: research → 2 strategies → recommend 1 + Why → derive 9 blog topics + hub | C |
| `data/agent-registry.json` (modify) | Register new agent at `opus48_max` tier | C |
| `CLAUDE.md` (modify) | Register all three artifacts in Reference Docs / agent / skill lists | A, B, C |

**Brand-fact reconciliation (CRITICAL — verified this session):** `skills/image-prompt-generator.md` is **stale** — it says brand orange `#FF8C00`, "Omaha home," owners "Lawrence/Cathy." The real brand (per `DESIGN.md` + business DNA) is **Clay `#e8604c` / Forest Green `#2D6A4F` / Cream `#faf7f4`**, owners **Mark & Teri Benjamin**, **Midland, TX (since 2014)**. `IMAGE-DESIGNS.md` MUST use the correct facts, and Task A includes fixing the stale skill values.

---

## Task A: `IMAGE-DESIGNS.md` + wire into image consumers

**Files:**
- Create: `IMAGE-DESIGNS.md`
- Create: `scripts/add_image_designs_pointer.py`
- Modify: `skills/image-prompt-generator.md` (fix stale `#FF8C00`/Omaha/Lawrence-Cathy values)
- Modify: `CLAUDE.md` (Reference Docs list)
- Verify-targets (pointer injected by script): `skills/image-prompt-generator.md`, `skills/cag-image-generation.md`, `skills/cag-photo-ingest.md`, `skills/cag-infographic.md`, `.claude/agents/cag-image-pipeline.md`, `.claude/agents/cag-infographic-builder.md`

- [ ] **Step 1: Create a feature branch**

```bash
cd /Users/apple/Downloads/CAG
git checkout -b foundations-image-voice-strategy
```

- [ ] **Step 2: Write `IMAGE-DESIGNS.md`** with these exact sections. Source brand facts from `DESIGN.md` (palette) and CLAUDE.md business DNA — do NOT copy the stale orange/Omaha values.

Required sections and load-bearing content:

```markdown
# IMAGE-DESIGNS.md — CAG Image Art-Direction (source of truth)

> READ FIRST before generating, editing, or placing ANY image on CongoAfricanGreys.com.
> Companion to DESIGN.md (UI/site visual brand). DESIGN.md governs the page; this governs the picture.
> Auto-consumed by the image skills/agents (see footer). Binding alongside docs/design.md.

## 0. Brand Facts (canonical — never drift)
- Owners: Mark & Teri Benjamin. Location: Midland, TX (breeding since 2014).
- Palette in-image: Forest Green #2D6A4F (framing/foliage), Clay/terracotta #e8604c (warm accent),
  Cream #faf7f4 / warm wood / soft beige (surfaces). Warm color grade always.
- Species accuracy: Congo = grey body + RED tail + bare white face mask, ~13in, 400–650g, yellow
  iris (adult)/dark (juvenile), dark hooked beak. Timneh = darker charcoal grey + MAROON/dark tail +
  horn-colored upper mandible. NEVER the generic green parrot. NEVER 🦜.
- CITES safety: never depict wild/jungle-capture, cages implying smuggling, or non-captive context.
  All birds are captive-bred USA, documented.

## 1. Crop & Aspect Ratios (per slot)
| Slot | Ratio | Source px | Notes |
| Hero (page header) | 16:9 | 1600×900 | LCP image — fetchpriority, WebP |
| Bird card | 3:4 portrait | 900×1200 | object-position per bird (see BirdCard memory) |
| Lifestyle / in-content | 4:3 | 1200×900 | |
| Social / OG | 1:1 + 9:16 | 1200×1200 / 1080×1920 | 9:16 for Reels/TikTok/Shorts |
| Infographic | per page-width rules | 760px (guide/blog) / 1100px (home/location) | height 400px desktop |

## 2. Reusable Style Wrapper (prepend to every generation prompt)
"Editorial pet photography, warm natural light, shallow depth of field, true-to-life African Grey
plumage, cream/wood/forest-green palette, calm premium family-aviary mood, photorealistic, high
detail on eye and feather texture."

## 3. Negative List (append to every prompt — non-negotiable)
no text, no watermarks, no logos, no captions, no UI chrome, no other parrot species, no generic
green parrot, no cartoon/3D/illustration (for photoreal slots), no cold blue/clinical/studio lighting,
no distorted/extra limbs or beaks, no unrealistic coloring, no dog/cat/puppy imagery, no jungle/wild-
capture context, no people's faces in sharp identifiable focus unless a real buyer photo, no cluttered
background.

## 4. Lighting & Focal Length (per scene)
| Scene | Lighting | Focal length / f-stop |
| Hero portrait | soft window/golden-hour, warm | 85mm, f/1.8 (subject pop) |
| Lifestyle (with family) | ambient room light, candid | 35–50mm, f/2.8 |
| Size reference (on hand) | even bright, feather detail | 50mm, f/4 (sharp) |
| Health/feather macro | diffused, no flash | 100mm macro, f/5.6 |
| Infographic | flat design, N/A | N/A |

## 5. Scene Types by Page Type (this is the routing table)
| Page type | Primary scene | Secondary | Avoid |
| Blog post | topic-illustrative lifestyle or portrait | infographic if data-heavy | for-sale price overlays |
| For-sale / variant | single-bird portrait, direct gaze | size-reference on hand | busy lifestyle |
| Location (state/city) | bird + subtle state landmark context (not kitschy) | shipping/airport-calm | literal flags/maps in-frame |
| Comparison ([X] vs [Y]) | split/side-by-side both subjects | comparison infographic | one subject only |
| Care/health guide | feather/eye macro, vet context | process (foraging/enrichment) | sales mood |
| Hub | clean banner-style portrait | grid of cluster thumbnails | text baked into image |

## 6. Output Handoff
Every generated image → cag-image-pipeline (SEO rename + WebP + placement) → image-metadata skill
(5-element set: filename, alt ≤190, title, caption+CTA, 250+ word description).

---
**Consumed by:** image-prompt-generator, cag-image-generation, cag-photo-ingest, cag-infographic
skills + cag-image-pipeline, cag-infographic-builder agents. If this conflicts with a stale value in
any of them, THIS file wins — fix the consumer.
```

- [ ] **Step 3: Fix the stale brand values in `image-prompt-generator.md`**

In `skills/image-prompt-generator.md`, replace stale facts: `#FF8C00` → `#e8604c` (clay) with Forest Green `#2D6A4F` added; "Omaha home" → "Midland, TX home"; "Lawrence/Cathy" → "Mark & Teri". Use Edit on each occurrence (grep first to find them all):

```bash
cd /Users/apple/Downloads/CAG
grep -n "FF8C00\|Omaha\|Lawrence\|Cathy" skills/image-prompt-generator.md
```
Expected: lines listed; fix each via Edit. Re-run grep → expected: no matches.

- [ ] **Step 4: Write `scripts/add_image_designs_pointer.py`** (idempotent, mirrors `add_interior_standard_pointer.py`)

```python
#!/usr/bin/env python3
"""Idempotent: inject a 'read IMAGE-DESIGNS.md first' pointer into image consumers."""
import pathlib, sys

POINTER = ("> **Image art-direction:** Read `IMAGE-DESIGNS.md` (repo root) BEFORE generating, "
           "editing, or placing any image — crop ratios, style wrapper, negative list, lighting, "
           "focal length, and scene-type-per-page. It is the image source of truth; it wins over "
           "any stale value here.\n")

TARGETS = [
    "skills/image-prompt-generator.md",
    "skills/cag-image-generation.md",
    "skills/cag-photo-ingest.md",
    "skills/cag-infographic.md",
    ".claude/agents/cag-image-pipeline.md",
    ".claude/agents/cag-infographic-builder.md",
]

def inject(path: pathlib.Path) -> bool:
    text = path.read_text()
    if "IMAGE-DESIGNS.md" in text:
        return False  # already pointed
    lines = text.splitlines(keepends=True)
    # insert after the first top-level heading line
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            lines.insert(i + 1, "\n" + POINTER)
            break
    else:
        lines.insert(0, POINTER + "\n")
    path.write_text("".join(lines))
    return True

def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    changed = 0
    for t in TARGETS:
        p = root / t
        if not p.exists():
            print(f"MISSING: {t}", file=sys.stderr); continue
        if inject(p):
            print(f"injected: {t}"); changed += 1
        else:
            print(f"skip (already): {t}")
    print(f"done. {changed} file(s) updated.")

if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run the pointer script (verify it injects, then is idempotent)**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/add_image_designs_pointer.py
python3 scripts/add_image_designs_pointer.py   # second run = all "skip (already)"
grep -lr "IMAGE-DESIGNS.md" skills/ .claude/agents/ | sort
```
Expected: first run injects 6; second run all skip; grep lists the 6 targets + (the new agent later).

- [ ] **Step 6: Register `IMAGE-DESIGNS.md` in `CLAUDE.md` Reference Docs**

Add under the `DESIGN.md` reference line:
```markdown
- `IMAGE-DESIGNS.md` (repo root) — **IMAGE ART-DIRECTION source of truth: crop ratios, reusable style wrapper, negative list (no logos/watermarks/🦜/other species), lighting, focal length, scene-types per page type. READ FIRST before any image work, alongside DESIGN.md. Consumed by all image skills/agents.**
```

- [ ] **Step 7: Commit Task A**

```bash
cd /Users/apple/Downloads/CAG
git add IMAGE-DESIGNS.md scripts/add_image_designs_pointer.py skills/ .claude/agents/cag-image-pipeline.md .claude/agents/cag-infographic-builder.md CLAUDE.md
git commit -m "feat(images): add IMAGE-DESIGNS.md art-direction source of truth + wire into image consumers; fix stale brand values"
git push -u origin foundations-image-voice-strategy
```

---

## Task B: `anti-ai-writing` skill (Iron Law: RED baseline first)

**Files:**
- Create: `sessions/2026-06-17-anti-ai-baseline.md` (the failing test capture)
- Create: `skills/anti-ai-writing.md`
- Modify: `CLAUDE.md` (skills list) + wire pointer into 3 writer agents
- Verify-targets: `.claude/agents/cag-seo-content-writer.md`, `.claude/agents/cag-blog-post-agent.md`, `.claude/agents/cag-non-commodity-content-agent.md`

- [ ] **Step 1 (RED — watch it fail): capture baseline AI slop**

Dispatch a fresh subagent (general-purpose) with: *"Write a 150-word intro for a CongoAfricanGreys.com blog post titled 'Are African Greys Good for First-Time Owners?' in the C.A.Gs first-person breeder voice."* Do NOT give it any anti-AI guidance. Save its output verbatim to `sessions/2026-06-17-anti-ai-baseline.md` and annotate every AI tell you find (e.g. "In today's fast-paced world", "Look no further", "Whether you're X or Y", "It's important to note", "delve", "elevate", "unlock", em-dash overuse, tricolon padding, empty hedge openers, generic CTA close).

Expected: a list of 10+ concrete slop patterns the skill must blacklist. **This is the failing test — do not write the skill until this exists.**

- [ ] **Step 2 (GREEN): write `skills/anti-ai-writing.md`** targeting the captured patterns

Frontmatter + structure:
```markdown
---
name: anti-ai-writing
description: Use when writing or editing any CAG prose (blog posts, page body, FAQ answers, emails, social, YouTube scripts) to filter out AI-tell phrases, robotic rhythm, and generic structure before they ship. Reference blacklist + human alternatives.
---

# Anti-AI Writing

## Overview
A proactive blacklist, not a reactive "humanize this" pass. Filter against a fixed list while writing.
Distinct from First-Person Voice (that governs POV — "we/our/here at C.A.Gs") and from the
cag-non-commodity-content-agent (that governs breeder-authentic substance). This governs *phrasing and
rhythm*. Use all three together.

## When to Use
- Writing/editing any CAG prose. Especially blog intros, FAQ answers, CTA copy, email, social.
- NOT for: schema/JSON-LD, legal text (privacy/terms), data tables, code.

## Blacklist (ban these — with human alternatives)
[Populate from sessions/2026-06-17-anti-ai-baseline.md. Each row: banned pattern → why it reads
robotic → human alternative. Group into: Weak Openers, Empty Transitions, Inflated Verbs, Padding
Tricolons, Generic Conclusions, Fake-Professional Terms, Punctuation Tells.]

## Rhythm Rules
- Vary sentence length; at least one <8-word sentence per paragraph.
- Max one em-dash per paragraph. No "not only X but also Y" scaffolding.
- Lead with the concrete claim, not a hedge ("It's worth noting that...").
- Cut any sentence that survives deletion without losing meaning.

## CAG-Specific
- Keep first-person breeder voice (we/our/here at C.A.Gs) — see the First-Person rule.
- Stay inside the Verified-Claim Ledger — humanizing never means inventing.
- CITES-safe, no visible dates, no 🦜.

## Self-Check Before Shipping
Grep your draft for the blacklist. Read it aloud — if it sounds like a press release, rewrite.

## Common Mistakes
[Capture during REFACTOR re-test.]
```

Fill the Blacklist + Common Mistakes from the real baseline — no invented patterns.

- [ ] **Step 3 (GREEN verify): re-test with the skill**

Dispatch the same prompt to a fresh subagent, this time instructing it to apply `skills/anti-ai-writing.md`. Compare against the baseline. Expected: none of the captured blacklist patterns appear. If new tells slip through → REFACTOR: add them to the blacklist, re-test.

- [ ] **Step 4: Wire the skill into the 3 writer agents (manual Edit, one pointer each)**

Add to the Golden Rule block of `cag-seo-content-writer.md`, `cag-blog-post-agent.md`, `cag-non-commodity-content-agent.md`:
```markdown
> **Anti-AI Writing (ALWAYS):** Before shipping any prose, filter against `skills/anti-ai-writing.md` — ban its blacklisted openers, transitions, inflated verbs, padding tricolons, and generic conclusions. This is phrasing/rhythm; it stacks with First-Person Voice (POV) and the Verified-Claim Ledger (substance).
```

- [ ] **Step 5: Register in `CLAUDE.md` skills list** (under "SEO & Content Skills"):
```markdown
- `skills/anti-ai-writing.md` — proactive anti-AI phrase/rhythm blacklist + human alternatives; read when writing/editing any CAG prose; stacks with First-Person Voice + non-commodity agent; built from a RED baseline (`sessions/2026-06-17-anti-ai-baseline.md`)
```

- [ ] **Step 6: Commit Task B**

```bash
cd /Users/apple/Downloads/CAG
git add skills/anti-ai-writing.md sessions/2026-06-17-anti-ai-baseline.md .claude/agents/cag-seo-content-writer.md .claude/agents/cag-blog-post-agent.md .claude/agents/cag-non-commodity-content-agent.md CLAUDE.md
git commit -m "feat(voice): add anti-ai-writing skill (RED-baseline tested) + wire into 3 writer agents"
git push
```

---

## Task C: `cag-strategy-synthesizer` agent

**Files:**
- Create: `.claude/agents/cag-strategy-synthesizer.md`
- Modify: `data/agent-registry.json` (add entry)
- Modify: `CLAUDE.md` (Tier 1 orchestrator list)
- Run: `scripts/apply_model_tiers.py`, `scripts/verify_model_tiers.sh`, `scripts/add_first_person_golden_rule.py`, `scripts/add_clarification_checkpoint_rule.py`

- [ ] **Step 1: Write `.claude/agents/cag-strategy-synthesizer.md`**

Use the exact CAG agent template (frontmatter + EFFORT block + Golden Rule with BOTH injected ALWAYS rules verbatim + CAG Project Context + Purpose + On Startup + body). Frontmatter:
```markdown
---
name: cag-strategy-synthesizer
description: Turns existing CAG research (gap matrix, competitor-intel, GSC, LLM-keyword-intel) into TWO complete reverse-engineered content strategies, recommends ONE with a data-grounded WHY plus its named trade-off, and derives concrete artifacts (e.g. the 9 blog topics + 1 hub) for the chosen strategy. Reads research only — never re-runs Sprint 0, never fabricates data. Hands the chosen strategy to cag-content-architect.
tools: [Read, Write, Bash]
model: claude-opus-4-8
effort: max
dynamic_workflow: false
---
```
Copy the EFFORT (MAX) block, the Golden Rule (Clarification Checkpoint + First-Person + Confidence Gate + "Claude Code first" lines) and the CAG Project Context block **verbatim** from `.claude/agents/cag-angle-agent.md`.

Then the agent-specific body:
```markdown
## Purpose
You are the Strategy Synthesizer for CongoAfricanGreys.com. You do NOT build pages. You read the
research that already exists and convert it into competing, fully-reasoned strategies the breeder can
choose between — then you recommend one and prove why.

## The Rule (what makes this agent different)
1. Produce EXACTLY TWO complete strategies — never one, never three. Two forces a real choice.
2. Each strategy is reverse-engineered from competitors + gaps + demand — not invented.
3. Recommend exactly ONE, with a WHY grounded in real data (3+ specific data points: opportunity
   scores, competitor coverage, GSC impressions/position, LLM-citation gaps) AND name the downside
   of the pick (per the site-wide Recommend+Why rule).
4. Never fabricate a number. If a research file is missing/stale, say so and proceed with what exists.
5. When asked for a concrete deliverable (e.g. "the 9 blog topics + hub"), output it as a table mapped
   to the chosen strategy's clusters, with opportunity score + target keyword + intent + internal-link
   role for each.

## On Startup — Read These First (research only; do NOT re-run Sprint 0)
1. `docs/research/gap-matrix-*.md` (latest) + `docs/research/keyword-gap-*.md`
2. `data/competitors.json` (30 competitors)
3. `docs/reference/top-pages.md` (GSC baseline)
4. `data/structure.json` (current silo) + `data/agent-registry.json`
5. If any are missing/stale, flag it; do not invent substitutes.

## Output (save to sessions/YYYY-MM-DD-<topic>-strategy.md)
### Strategy A — [name] : thesis · target clusters · cluster→page map · internal-link architecture ·
    schema plan · build order/effort · expected outcome · risks
### Strategy B — [name] : (same structure, materially different bet)
### Recommendation : pick + WHY (3+ data points) + the trade-off of the pick + first 3 build steps
### Concrete Artifact (when requested) : e.g. the 9 blog topics + 1 hub table

## Handoff
Chosen strategy → cag-content-architect (which selects framework + routes builders). The 9-topics
table → grill-me (Sprint 0.5) per blog post.
```

- [ ] **Step 2: Verify the agent has no placeholders / both ALWAYS rules present**

```bash
cd /Users/apple/Downloads/CAG
grep -c "Clarification Checkpoint\|First-Person Brand Voice\|Confidence Gate" .claude/agents/cag-strategy-synthesizer.md
```
Expected: ≥3.

- [ ] **Step 3: Register in `data/agent-registry.json`**

Add to the `agents` object (Python, preserves formatting):
```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
import json
p="data/agent-registry.json"
d=json.load(open(p))
d["agents"]["cag-strategy-synthesizer"]={"tier":"opus48_max","dynamic_workflow":False}
json.dump(d,open(p,"w"),indent=1)
print("added; total agents:",len(d["agents"]))
PY
```

- [ ] **Step 4: Apply + verify model tiers, then injection scripts (all idempotent)**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/apply_model_tiers.py
bash scripts/verify_model_tiers.sh
python3 scripts/add_first_person_golden_rule.py
python3 scripts/add_clarification_checkpoint_rule.py
```
Expected: `verify_model_tiers.sh` passes (includes the new agent). Injection scripts report idempotent (already-present) for existing agents and confirm the new one. **Note:** `apply_model_tiers.py` adds a cosmetic blank line to ~40 agents — `git checkout` the unrelated ones to keep the commit focused (per project memory).

- [ ] **Step 5: Register in `CLAUDE.md`** under Tier 1 Orchestrators:
```markdown
- `.claude/agents/cag-strategy-synthesizer.md` — research → TWO reverse-engineered strategies → recommend ONE with data-grounded WHY + named trade-off → derives concrete artifacts (e.g. the 9 blog topics + hub). Reads research only (no Sprint-0 re-run), never fabricates; hands chosen strategy to cag-content-architect. Runs at Sprint 1 (architecture), before content-architect.
```
Also update the agent-count references if any (search `66 agents` → becomes `67`):
```bash
cd /Users/apple/Downloads/CAG
grep -rn "66 agents\|all 66\|66 agent" CLAUDE.md docs/ scripts/ | head
```
Update the count where it denotes the live total (CLAUDE.md model-tier section, agent-system-qa references). Leave historical session notes ("applied to all 66, 2026-06-05") unchanged — those are dated records.

- [ ] **Step 6: Commit Task C**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-strategy-synthesizer.md data/agent-registry.json CLAUDE.md
git commit -m "feat(strategy): add cag-strategy-synthesizer agent (2 strategies + recommend-one rule); register in tier registry + CLAUDE.md (67 agents)"
git push
```

---

## Task D: Integration verification + run the strategy agent for the 9 topics

**Files:** none created — verification + first real use.

- [ ] **Step 1: Agent-system QA audit**

Run the `cag-agent-system-qa` agent over the new agent + edited files. Expected: PASS on structural completeness (Golden Rule present, required sections, registered in CLAUDE.md, registry entry). Fix any flagged gaps.

- [ ] **Step 2: Full health sweep**

```bash
cd /Users/apple/Downloads/CAG
bash scripts/health-sweep.sh --no-build
```
Expected: git/deploy state clean (no leaked secrets), agent integrity PASS (now 67 agents + tiers verify), dist hygiene OK. (Use `--no-build` since this phase touched no Astro source.)

- [ ] **Step 3: Confirm workflow still intact (the "is the workflow intact?" ask)**

Verify the sprint chain still resolves with the new agent inserted: Sprint 0 (done) → **Sprint 1 now includes `cag-strategy-synthesizer`** → Sprint 0.5 `grill-me` per page → content-audit → build. Update `docs/reference/WORKFLOW.md` Sprint 1 line to name the strategy agent as the first step. Commit.

- [ ] **Step 4: First real use — derive the 9 blog topics + hub**

Run `cag-strategy-synthesizer` with: *"Read the research and produce two strategies for a 9-blog-post + 1-hub cluster; recommend one and output the 9 topics + hub table."* Save to `sessions/2026-06-17-blog-strategy.md`. This output is the **entry point for Phase 2** (the actual blog build). Do not build the posts in this phase — stop here and hand the topic table back to the user for approval.

- [ ] **Step 5: Final commit + push**

```bash
cd /Users/apple/Downloads/CAG
git add docs/reference/WORKFLOW.md sessions/2026-06-17-blog-strategy.md
git commit -m "docs(workflow): insert strategy-synthesizer at Sprint 1; derive 9 blog topics + hub for Phase 2"
git push
```

---

## Self-Review (run against the spec before execution)

**Spec coverage:** #3 IMAGE-DESIGNS.md → Task A ✅ · #4/5a image-agent integration (no new agent, wire doc in) → Task A steps 4–5 ✅ · #6 anti-AI skill (standalone, not merged into first-person) → Task B ✅ · #2 strategy agent + its rule + derives 9 topics → Task C + D.4 ✅ · "workflow still intact" → D.3 ✅ · agent-permissions/MCP full pass → explicitly deferred (noted out-of-scope) ✅ · #1 social bridge + #5b CF-images → explicitly deferred ✅.

**Placeholder scan:** Two intentional fill-from-data spots — the anti-AI Blacklist (B.2) and Common Mistakes — are filled from the RED baseline captured in B.1, not invented. That is the correct TDD order, not a placeholder. All scripts, commands, and frontmatter are complete.

**Type consistency:** Agent name `cag-strategy-synthesizer` used identically in the file, registry, CLAUDE.md, and WORKFLOW.md. Tier `opus48_max` matches an existing registry tier. Pointer string in `add_image_designs_pointer.py` matches the CLAUDE.md reference wording.

**Iron Law check:** Task B writes the skill only AFTER the RED baseline (B.1) exists — compliant with writing-skills.

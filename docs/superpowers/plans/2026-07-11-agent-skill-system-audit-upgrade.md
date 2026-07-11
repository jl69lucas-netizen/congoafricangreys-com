# Agent + Skill System Audit & Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Full audit of all 68 agents + 50 skills, wire in 5 new/changed site-wide rules, and add 5 new skills (reddit-strategy, duplicate-content gate, PAS, FAB, framework-library) — all registered, cross-linked, committed, and pushed.

**Architecture:** Docs/process change only — no site pages touched. Rule changes propagate through (a) an idempotent Golden-Rule injection script (existing pattern), (b) targeted edits to every file that states the old rule, (c) new skill files registered via `register_skills.py --copy`.

**Tech Stack:** Markdown skills/agents, Python injection scripts, existing `scripts/dup_content_audit.py`.

---

### Task 1: New Golden Rule — Link-First (start-of-sentence anchors)

**Files:**
- Create: `scripts/add_link_first_rule.py` (idempotent, models `add_clarification_checkpoint_rule.py`)
- Modify: all 68 `.claude/agents/*.md` (via script)
- Modify: `CLAUDE.md` (Non-Negotiable Rules + line 184 + line 362), `docs/reference/seo-rules.md:494`, `MANUAL INTERIOR-PAGE CHECKLIST.md` (lines 33, 184-186, 296), `.claude/agents/cag-external-link-agent.md` (desc + lines 50, 122), `.claude/agents/cag-blog-post-agent.md:253`, `.claude/agents/cag-entity-incorporation-agent.md` (lines 80, 87), `skills/internal-link-agent.md` (lines 140, 168, 176, 262), `skills/cag-comparison-page-builder.md` (lines 73, 136, 195, 222), `skills/cag-seo-master-checklist.md` (lines 31, 637, 1162), `skills/cag-branded-hybrid-keywords.md:63`, the 8 interior-builder "Interior-Page Standard" pointers ("woven mid-sentence links" → "links at sentence start")
- Modify: memory `feedback_linking_policy.md`

**Rule text (canonical):** "For ALL internal and external links, the anchor sits at the START of the sentence/paragraph — within the opening words (first clause). Never mid-sentence, never at the end. Example — ✅ `Our [Congo African Grey guide](/…) covers diet in depth…` · ❌ `…diet is covered in our [guide](/…).`"

- [x] Step 1: Write `scripts/add_link_first_rule.py`
- [x] Step 2: Run it; verify 68/68 agents carry the rule (`grep -l "Link-First" .claude/agents/*.md | wc -l` → 68)
- [x] Step 3: Edit every listed doc/skill occurrence of the old rule
- [x] Step 4: Verify zero stale occurrences (`grep -rn "beginning or middle" …` → 0 in binding docs)

### Task 2: internal-link-agent upgrade (sitemap-driven + anchor diversity)

**Files:** Modify `skills/internal-link-agent.md`

- [x] Step 1: Add "Phase 0 — Sitemap inventory" (read `public/sitemap.xml` shards / `scripts/generate_sitemaps.py` output as the page universe; orphan + hub-spoke analysis runs off the sitemap, not ad-hoc greps)
- [x] Step 2: Add "Anchor Diversity Ledger" (never repeat an anchor site-wide for the same target; exact-match ≤1 per target per page; rotate partial-match / LSI / natural-language variants; ledger table format)
- [x] Step 3: Update placement rule to Link-First

### Task 3: Image-alt keyword rule + stop-words rule

**Files:** Modify `skills/image-metadata.md`, `IMAGE-DESIGNS.md`, `docs/reference/seo-rules.md`, `skills/anti-ai-writing.md`

- [x] Step 1: seo-rules — new rule: PRIMARY keyword = alt of the page's primary (hero/first) image only; every other image rotates secondary/LSI/NLP variants; no two images on a page share an alt
- [x] Step 2: Same rule into `image-metadata` skill + IMAGE-DESIGNS.md art-direction intake
- [x] Step 3: anti-ai-writing — new section "Meaningful words, no stop-words" (slugs, anchors, headings, image filenames/alts, meta: content-bearing words only; drop of/the/and/for/with fillers where grammar allows). Decision: goes in anti-ai-writing + seo-rules, NOT a standalone skill (too thin to trigger alone — trade-off: anti-ai-writing grows ~120 words)

### Task 4: New skill — reddit-strategy

**Files:** Create `skills/reddit-strategy.md`

- [x] Step 1: Write skill — Compact-Keywords / "Reddit modifier" playbook: keyword discovery (GSC + low-KD "reddit" terms), 100–400-word resource pages, cornerstoning/authority bridging, `/african-grey-reddit/`-style resource page spec, LLM-visibility angle, white-hat rules, CAG comparison-cluster application (r/parrots African Greys vs Amazons thread etc.), CITES safety
- [x] Step 2: RED baseline = documented: comparison pages cited Reddit ad-hoc with no capture strategy; no page targets any "<keyword> reddit" query

### Task 5: New skill — cag-duplicate-content-gate

**Files:** Create `skills/cag-duplicate-content-gate.md`

- [x] Step 1: Write skill around `scripts/dup_content_audit.py` (≥12-word cross-page check) + header/template-crossover gate + ALLOWED-shared-elements whitelist (shipping line, CITES notice, footer, trust badges, legal) + run-BEFORE-build and run-BEFORE-pass placement in the workflow
- [x] Step 2: RED baseline = 2026-07 comparison cluster: 29 crossover headers shipped and had to be rewritten post-hoc (token waste documented)

### Task 6: New framework skills — PAS, FAB, framework-library

**Files:** Create `skills/framework-pas.md`, `skills/framework-fab.md`, `skills/framework-library.md`

- [x] Step 1: framework-pas (Problem→Agitate→Solution; behavior/health/scam pages; CAG examples)
- [x] Step 2: framework-fab (Features→Advantages→Benefits; bird/product/comparison advantage rows; CAG examples)
- [x] Step 3: framework-library (catalog: 4Ps, AICPBSAWN, QUEST, ACCA, HIPASI, A-FOREST, String of Pearls, VAD, Setup-Stat-Reframe, 4 Ss, 5 Basic Objections, objection block; routing table by page type + awareness level; EBP disambiguation note)

### Task 7: Registration + docs + audit report

- [x] Step 1: `python3 scripts/register_skills.py --copy`; verify count
- [x] Step 2: CLAUDE.md — add the 5 new skills + missing `cag-comparison-page-builder` (and other unlisted skills) to the registry; add comparison-page Quick Start line; new rules into Non-Negotiable Rules
- [x] Step 3: Write full audit report `sessions/2026-07-11-agent-skill-audit.md` (every agent + skill: what it does, verdict, improvement)
- [x] Step 4: Memory updates (linking policy, new-rules pointer)
- [x] Step 5: Commit + push (git add named files only)

### Verification
- `bash scripts/verify_model_tiers.sh` still passes (agents edited by script)
- `python3 scripts/register_skills.py` reports all skills registered
- grep sweeps in Tasks 1–3 return zero stale rule text

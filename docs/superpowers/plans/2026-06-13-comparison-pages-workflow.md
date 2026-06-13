# Comparison-Pages Workflow — Analysis + Canonical Runbook + Doc Reconciliation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement the **reconciliation tasks** (Part C) task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Parts A, B, D are reference/analysis — read them, don't "execute" them.

**Goal:** Verify the agent/skill working order for building comparison pages (is "Sprint 0 competitor research first → Sprint 0.5 grill-me" correct?), document the complete start-to-finish runbook, and fix the stale docs that currently lie about which comparison pages exist.

**Architecture:** Comparison pages are a 7-page silo (1 hub + 6 spokes) that sits *outside* the SEO-master-checklist and the Interior-Page Standard — they have their own builder (`@cag-comparison-builder`) and their own template. The macro sprint order is correct; the problem is that three reference files (the agent, `WORKFLOW.md`, `structure.json`) were written when only `male-vs-female` existed and were never updated after the other six shipped. This plan reconciles them and gives one authoritative runbook.

**Tech Stack:** Astro pages in `src/pages/<slug>/index.astro` · Markdown agents/skills · `data/structure.json` silo map · Firecrawl MCP for SERP research · GitHub Actions → Cloudflare Pages deploy.

---

## Part A — Analysis Findings (read first)

### A1. Your core question, answered

> *"Is the current order — competitor research first (Sprint 0), then grill-me (Sprint 0.5) — correct for starting comparison pages?"*

**Yes, the macro order is correct — but with one important refinement: for comparison pages there are THREE distinct research scopes, not one, and only the first is "Sprint 0."**

| Scope | Agent/Skill | When | Cadence | Already done? |
|---|---|---|---|---|
| **1. Site-wide competitor intel** | `@cag-competitor-registry` → `@cag-competitor-intel --all` → `@cag-gsc-analytics` | Sprint 0 | Once, then **quarterly** | ✅ YES — `data/competitors.json` (30 competitors) + `docs/research/gap-matrix-*.md` exist |
| **2. Per-session orientation** | `grill-me` skill | Sprint 0.5 | **Once per page build** | Run fresh each time |
| **3. Per-keyword SERP research** | inside `@cag-comparison-builder` (Firecrawl top-3 ranking pages for the *exact* comparison keyword) | Sprint 2, at build time | Once per page | Run fresh each time |

**The key insight:** Sprint 0 is NOT something you re-run every time you start a comparison page. It is a quarterly prerequisite that is **already satisfied**. So the practical answer to "where do I start with comparison pages today?" is:

> **Skip Sprint 0 (already done) → start at Sprint 0.5 (`grill-me`) → then the comparison-builder does its own per-keyword SERP research inside Sprint 2.**

Re-running `@cag-competitor-intel --all` before every comparison page would be wasteful (it's a 30-competitor sweep). The comparison-builder's built-in "Firecrawl top-3 for *this* keyword" step (agent lines 51–54) is the *page-specific* research that actually matters at build time. These two are **not redundant** — different scope (whole-market vs single-SERP), different cadence (quarterly vs per-page).

**Verdict:** Order is sound. The only thing wrong is that the docs don't *say* "Sprint 0 is already done, go straight to 0.5 for comparison work," and they imply the spokes are unbuilt. Part C fixes that.

### A2. Comparison pages are EXCLUDED from the two big content systems

This is by design and easy to forget:

- **SEO-master-checklist** (`skills/cag-seo-master-checklist.md:16`): *"Excluded: … Comparison pages (use `@cag-comparison-builder` template)."*
- **Interior-Page Standard** (`MANUAL INTERIOR-PAGE CHECKLIST.md`): excludes comparison pages — they "own structure."
- **Interior-polish rollout** (`docs/superpowers/plans/2026-06-06-interior-pages-full-seo.md:62`): comparison pages explicitly **out of scope**.

**Consequence:** The 18-page interior-polish work (Direction-D refinements, AA-contrast fixes, scroll-margin, paragraph splits, two-keyword headers) that finished 2026-06-12 **never touched the comparison pages.** They predate that polish. That is the real opportunity in Part D.

### A3. Stale-doc discrepancies found (these are bugs in the system docs)

**Reality on disk (verified 2026-06-13):**

| Slug | Lines | H1 | In structure.json? |
|---|---|---|---|
| `african-grey-comparison` (HUB) | 215 | "Which Parrot Is Right for You?" | ✅ hub |
| `congo-vs-timneh-african-grey` | 576 | "Congo vs Timneh African Grey: Key Differences" | ✅ |
| `male-vs-female-african-grey-parrots-for-sale` | 313 | "Male vs. Female African Grey Parrots for Sale" | ✅ |
| `african-grey-vs-macaw` | 361 | "African Grey vs Macaw: Which Parrot Is Right for You?" | ✅ |
| `african-grey-vs-cockatoo` | 390 | "African Grey vs Cockatoo: Which Parrot Fits Your Life?" | ✅ |
| `african-grey-vs-amazon-parrot` | **135** ⚠️ | "African Grey vs Amazon Parrot: Which Talker Is Right…" | ❌ **MISSING** |
| `african-grey-parrot-breeders-comparison` | 506 | "African Grey Parrot Breeders: An Honest Comparison" | ❌ not in comparison silo |

**Discrepancy 1 — Agent says spokes are unbuilt.** `.claude/agents/cag-comparison-builder.md` frontmatter + body (lines 3, 58–64, 94–101, 157) say *"Currently live: only `male-vs-female`"* and list congo-vs-timneh / macaw / cockatoo as *"Priority builds"* (to-do). **All three exist.** The agent will waste a session "building" pages that are live, or worse, overwrite a 576-line page thinking it's empty.

**Discrepancy 2 — `WORKFLOW.md:269` repeats the lie.** *"Priority order: congo-vs-timneh → african-grey-vs-macaw → african-grey-vs-cockatoo"* — written as a build queue for unbuilt pages.

**Discrepancy 3 — Slug mismatch.** The agent's table (line 98) lists `/african-grey-vs-macaw-parrot/` (with `-parrot`). Disk + structure.json + canonical = `/african-grey-vs-macaw/` (no `-parrot`). A build against the wrong slug creates a duplicate orphan and a canonical conflict.

**Discrepancy 4 — `structure.json` is missing a live page.** `african-grey-vs-amazon-parrot` exists (135 lines, live canonical) but is **not** in the Comparison Cluster spokes (`data/structure.json:61–66`). It is an orphan — no hub links to it, so it gets near-zero link equity. (`african-grey-parrot-breeders-comparison` is a deliberate trust/breeder page, not a species-comparison spoke — leave it where it is, but confirm the hub links to it.)

**Discrepancy 5 — Framework conflict across 3 files.** Three sources disagree on the comparison-page framework:
- `WORKFLOW.md:152` → **BAB + QAB**
- `grill-me.md:216` (Q10) → **BAB**
- `cag-content-architect.md:76` → **QAB + FAB** (Entity-Tree alt)

These aren't catastrophic (all three are decision-driving frameworks and the template blends them), but a builder reading one file vs another gets different guidance. Part C picks one canonical answer: **primary QAB (the head-to-head table + FAQ *is* Question→Answer→Benefit) + BAB for the owner-story section.** That matches what the reference page actually does.

### A4. What's genuinely healthy (don't touch)

- The **sprint sequence itself** (0 → 0.5 → 1 → 2 → 3 → 4 → 5) is correct and the gates are sound.
- The **comparison-builder template** (13-section structure, 2-table minimum, FAQ schema, mid-page CTA, CITES note) is good and matches the reference page.
- **structure.json's link logic** for the silo is correct (hub ↓ spokes, spokes ↑ hub + ↔ variant pages).
- Sprint 0 outputs (competitors.json, gap matrix) exist and are current enough to not re-run.

---

## Part B — The Canonical Comparison-Page Runbook (start → finish)

This is the authoritative sequence for **one** comparison page, whether net-new or a rebuild. Copy-paste the invocations in order. Gates are blocking.

### Phase 0 — Prerequisite check (30 seconds, not a sprint)
```bash
ls data/competitors.json docs/research/gap-matrix-*.md docs/reference/top-pages.md data/structure.json
```
- All present → **Sprint 0 is done. Do NOT re-run it.** Go to Phase 1.
- gap-matrix missing → run `@cag-competitor-intel --all` once, then continue. (It won't be — it exists.)

### Phase 1 — Orientation (Sprint 0.5)
```
grill-me            # full interview for a new build
grill-me --quick    # 3 questions if you're only polishing an existing page
```
- At **Q6 (target slug)** give the exact on-disk slug from the Part A3 table — never invent a `-parrot` variant.
- At **Q10 (framework)** answer: **QAB primary + BAB for the owner story** (see A3 Discrepancy 5).
- Output: `sessions/2026-MM-DD-session-brief.md` with the SESSION CONTEXT block. Page Type = `comparison`.

### Phase 2 — Pre-build audit + SERP research (Sprint 2 entry)
```
@cag-content-audit-agent /<slug>/ "<comparison keyword>" "Comparison Page"
```
- Phase 0 of the audit = outline → **must be approved before any writing.**
- Then the **comparison-builder's own SERP step** runs (Firecrawl top-3 for the exact keyword) — this is research scope #3 from A1. It tells you the heading/table/FAQ gaps to beat.

### Phase 3 — Section map + component gate (MANDATORY before writing)
List every section Hero → final CTA against the 13-section comparison template (agent lines 104–121). For each, name the component + variant from `docs/reference/components.md`. **Get explicit user approval. Locked after approval.**

### Phase 4 — Build (the comparison-builder orchestrates these)
```
@cag-comparison-builder        # primary — builds section-by-section, staged in sessions/<slug>-rebuild/
```
It internally calls / you supplement with:
```
@cag-angle-agent               # 5–10 angles → pick the decision hook (Q2 above)
@cag-paa-agent                 # real PAA questions for the comparison keyword → feeds FAQ
@cag-faq-agent                 # QAB FAQ + FAQPage JSON-LD (required, no exceptions)
@cag-section-builder           # any custom sections (hero, comparison-table, cta, counter)
@cag-infographic-builder       # comparison infographic — read data/image-specs.json first; width 760px (guide-type) — confirm per page
@cag-interactive-component     # optional: "which parrot fits you?" quiz / cost-compare calculator
```
Rules enforced by the builder: ≥2 comparison tables · prices from `data/price-matrix.json` (never hardcoded) · mid-page CTA · CITES Appendix-I + captive-bred note · first-person "we/our/here at C.A.Gs" voice · `cag-h1`/`cag-h2` classes · Direction-D theme is global (don't re-add it).

Output file: `src/pages/<slug>/index.astro` — never `site/content/`.

### Phase 5 — AEO/GEO gate (Sprint 3, blocking)
```
@cag-keyword-verifier          # 85–110 keyword band, H2 distribution, alt text, internal links, canonical
@cag-meta-description-agent     # title/desc, no duplicates (check against the 6 sibling comparison pages)
@cag-external-link-agent        # authority links mid-sentence (never at end); verify 200 first
@cag-trust-signals-agent        # trust badge row + ReviewAggregateSchema + counter snippet
```
Schema must verify in `dist/`, not source: `grep -rl "FAQPage" dist/<slug>/`.

### Phase 6 — Technical hardening (Sprint 4)
```
@cag-accessibility-fixer        # WCAG 2.1 AA — comparison TABLES need scope/headers; AA clay variants
@cag-performance-fixer          # Perf ≥90
@cag-canonical-fixer            # NEVER SKIP — absolute canonical = the on-disk slug
@cag-footer-standardizer        # cag-footer-v1
```

### Phase 7 — Deploy + verify (Sprint 5)
```
python3 scripts/generate_sitemaps.py    # MUST run after add/remove of any page
git add -A && git commit && git push    # push = deploy (GitHub Actions → Cloudflare)
@cag-deploy-verifier                     # 200 checks + IndexNow submission
bash scripts/health-sweep.sh             # full system green
```
Post-deploy: `curl -sI https://congoafricangreys.com/<slug>/ | grep HTTP` → expect `HTTP/2 200`.

### One-line summary of the order
**Phase 0 prereq-check → 0.5 grill-me → audit+SERP → section/component gate → comparison-builder (+angle/paa/faq/section/infographic) → AEO gate → tech gate → sitemap → push → deploy-verify → health-sweep.**

---

## Part C — Reconciliation Fix Tasks (execute these)

These fix the stale docs that will actively misdirect the next comparison build. Each is a real file edit with a grep verification. No tests framework exists for docs, so verification = grep showing the corrected state.

### Task 1: Add the orphan page to the comparison silo in structure.json

**Files:**
- Modify: `data/structure.json` (Comparison Cluster spokes array, ~lines 61–66)

- [ ] **Step 1: Read the current spokes array**

Run: `grep -n "Comparison Cluster" -A 12 data/structure.json`
Expected: a `spokes` array with 4 entries, missing `african-grey-vs-amazon-parrot`.

- [ ] **Step 2: Add the missing spoke**

In the Comparison Cluster `spokes` array, add `"/african-grey-vs-amazon-parrot/"` after the cockatoo entry. The array should become:
```json
        "/congo-vs-timneh-african-grey/",
        "/male-vs-female-african-grey-parrots-for-sale/",
        "/african-grey-vs-macaw/",
        "/african-grey-vs-cockatoo/",
        "/african-grey-vs-amazon-parrot/"
```
(Watch the trailing comma — the line before the closing `]` must have no comma.)

- [ ] **Step 3: Verify it parses and contains the page**

Run: `python3 -c "import json; d=json.load(open('data/structure.json')); print('amazon' in json.dumps(d))"`
Expected: `True` (and no JSON parse error).

- [ ] **Step 4: Verify the hub page actually links to it**

Run: `grep -i "amazon" src/pages/african-grey-comparison/index.astro`
Expected: at least one link to `/african-grey-vs-amazon-parrot/`. If empty, the hub is missing the link — note it in the session brief Open Flags and add the link to the hub's spoke grid (do NOT change other hub content).

- [ ] **Step 5: Commit**
```bash
git add data/structure.json src/pages/african-grey-comparison/index.astro
git commit -m "fix(structure): add african-grey-vs-amazon-parrot to comparison silo (was orphaned)"
```

### Task 2: Correct the comparison-builder agent's "what exists" + slug docs

**Files:**
- Modify: `.claude/agents/cag-comparison-builder.md` (description line 3; "CAG Existing Comparison Pages" ~64; "Comparison Page Types" table ~94–101; rule 7 ~157)

- [ ] **Step 1: Fix the frontmatter description (line 3)**

Replace the existing-pages claim. Old fragment:
```
Existing comparison pages include male-vs-female-african-grey-parrots-for-sale. Priority builds: congo-vs-timneh, african-grey-vs-macaw, african-grey-vs-cockatoo.
```
New:
```
Existing comparison pages (all LIVE): african-grey-comparison (hub), congo-vs-timneh-african-grey, male-vs-female-african-grey-parrots-for-sale, african-grey-vs-macaw, african-grey-vs-cockatoo, african-grey-vs-amazon-parrot, african-grey-parrot-breeders-comparison. Default mode is REBUILD/POLISH an existing page — confirm the on-disk slug before writing; never assume a comparison page is unbuilt.
```

- [ ] **Step 2: Fix "CAG Existing Comparison Pages" (~line 64)**

Replace `Currently live: \`male-vs-female-african-grey-parrots-for-sale\`...` with the verified 7-page table from **Part A3** of this plan (slug · lines · H1), and add: *"Reference design = male-vs-female (313 lines). Thinnest spoke = african-grey-vs-amazon-parrot (135 lines) — first polish target."*

- [ ] **Step 3: Fix the slug in the "Comparison Page Types" table (~line 98)**

Change `/african-grey-vs-macaw-parrot/` → `/african-grey-vs-macaw/` (no `-parrot`). Change the Priority column for congo-vs-timneh, macaw, cockatoo from "High/Medium" (implying unbuilt) to **"✅ Exists — rebuild/polish only"**. Add a row for `african-grey-vs-amazon-parrot` (✅ Exists, thin — expand).

- [ ] **Step 4: Fix rule 7 (~line 157)**

Old: `Congo vs Timneh is highest priority — build this first...`
New: `Congo vs Timneh already exists (576 lines) — do NOT rebuild from scratch. The polish priority is the THIN page first: african-grey-vs-amazon-parrot (135 lines) → then bring all spokes to the post-2026-06-12 standard (Direction-D, AA contrast, two-keyword headers).`

- [ ] **Step 5: Verify no stale "priority build" language remains**

Run: `grep -niE "priority build|currently live: .male-vs-female|macaw-parrot" .claude/agents/cag-comparison-builder.md`
Expected: **no output** (empty).

- [ ] **Step 6: Commit**
```bash
git add .claude/agents/cag-comparison-builder.md
git commit -m "fix(comparison-builder): correct stale 'unbuilt' claims — all 6 spokes are live; fix macaw slug; default to rebuild/polish"
```

### Task 3: Correct WORKFLOW.md comparison block + framework line

**Files:**
- Modify: `docs/reference/WORKFLOW.md` (Comparison Pages block ~266–271; framework table line 152)

- [ ] **Step 1: Fix the Comparison Pages specialty block (~line 269)**

Old:
```
cag-comparison-builder
  → Priority order: congo-vs-timneh → african-grey-vs-macaw → african-grey-vs-cockatoo
  → Reference: /male-vs-female-african-grey-parrots-for-sale/
```
New:
```
cag-comparison-builder
  → All 6 spokes + hub are LIVE (see agent file for the verified slug list). Default = REBUILD/POLISH, not net-new.
  → Polish priority: african-grey-vs-amazon-parrot (thinnest, 135 lines) → then bring every spoke to the post-2026-06-12 interior-polish standard.
  → Comparison pages are EXCLUDED from seo-master-checklist + Interior-Page Standard — they own their structure.
  → Reference: /male-vs-female-african-grey-parrots-for-sale/
```

- [ ] **Step 2: Make the framework line consistent (line 152)**

Confirm line 152 reads `| Comparison pages | BAB + QAB |`. Change to:
```
| Comparison pages | QAB (head-to-head + FAQ) + BAB (owner story) |
```
so it matches grill-me Q10 and the content-architect after Task 4.

- [ ] **Step 3: Verify**

Run: `grep -niE "Priority order: congo-vs-timneh|QAB \(head-to-head" docs/reference/WORKFLOW.md`
Expected: the old "Priority order" line is **gone**; the new QAB framework line is **present**.

- [ ] **Step 4: Commit**
```bash
git add docs/reference/WORKFLOW.md
git commit -m "fix(workflow): comparison pages are live (polish not build); unify framework to QAB+BAB"
```

### Task 4: Unify the framework in content-architect

**Files:**
- Modify: `.claude/agents/cag-content-architect.md` (routing table line 76)

- [ ] **Step 1: Align the comparison row**

Old (line 76): `| Comparison page | QAB + FAB | Entity-Tree | Decision-driving |`
New: `| Comparison page | QAB + BAB | FAB / Entity-Tree | Decision-driving (head-to-head table + FAQ = QAB; owner story = BAB) |`

- [ ] **Step 2: Verify all three sources now agree**

Run:
```bash
grep -h "Comparison" docs/reference/WORKFLOW.md .claude/agents/cag-content-architect.md; grep -A1 "BAB — comparison" skills/grill-me.md
```
Expected: WORKFLOW + content-architect both show **QAB + BAB**; grill-me shows **BAB** for comparison (compatible — BAB is the owner-story half).

- [ ] **Step 3: Commit**
```bash
git add .claude/agents/cag-content-architect.md
git commit -m "fix(content-architect): unify comparison framework to QAB+BAB across all 3 docs"
```

### Task 5: Push the reconciliation
- [ ] **Step 1: Push (per the always-push-after-commit rule)**
```bash
git push
```
Expected: pushes 5 commits; GitHub Actions runs (these are doc/data changes — no page output changes, so no live-site risk).

---

## Part D — Per-Page Polish Queue (the actual content work, after Part C)

The comparison pages missed the 2026-06-12 interior-polish sweep. Run the **Part B runbook in "polish" mode** (`grill-me --quick` → straight to AEO + tech gates, no net-new build) on each, in this order. Priority is by thinness + traffic potential.

| # | Page | Lines | Why it's first / notes |
|---|---|---|---|
| 1 | `african-grey-vs-amazon-parrot` | **135** | Less than half the reference page. Expand to the full 13-section template (currently a stub). Highest leverage. |
| 2 | `african-grey-comparison` (HUB) | 215 | It's the silo hub — link equity router. Confirm it links to **all 6** spokes (incl. amazon, per Task 1). |
| 3 | `male-vs-female-…` | 313 | The "reference" but predates Direction-D polish — bring IT up to the new standard so it earns the title. |
| 4 | `african-grey-vs-macaw` | 361 | Apply AA-contrast + two-keyword headers + paragraph splits. |
| 5 | `african-grey-vs-cockatoo` | 390 | Same. |
| 6 | `african-grey-parrot-breeders-comparison` | 506 | Trust/breeder comparison — verify it's not making unverifiable competitor claims (Verified-Claim Ledger). |
| 7 | `congo-vs-timneh-african-grey` | 576 | Most substantial; lightest touch — AA + perf gate only. |

**Polish checklist per page** (from the interior-polish playbook, adapted — comparison pages keep their compare tables): AA-safe clay variants on any green panels · H2 `clamp()` sizing · `scroll-margin` on anchored headings · split any 240+ char paragraphs · two-keyword headers · first-person voice audit · verify FAQPage + (new) BreadcrumbList schema in `dist/` · Lighthouse a11y + perf ≥90.

> **Gate before starting Part D:** Part C must be merged first, or the comparison-builder will fight you with stale "this page doesn't exist" guidance.

---

## Self-Review

**Spec coverage:**
- "Analyse all agents/skills/workflow" → Part A (findings) + Part B (every agent in the chain documented). ✅
- "Check the working order — Sprint 0 first → grill-me 0.5" → A1 (verdict: correct, with the 3-research-scopes refinement). ✅
- "How to use all agents/skills start to finished" → Part B runbook (Phase 0→7, every invocation). ✅
- Implicit: the order analysis surfaced that the docs are stale → Part C makes the order *actually* followable. ✅

**Placeholder scan:** No TBDs. Every edit shows old→new text; every step has a grep/curl/python verification with expected output. ✅

**Type/name consistency:** Slugs are the verified on-disk canonicals throughout (`african-grey-vs-macaw` not `-macaw-parrot`; `african-grey-vs-amazon-parrot` consistent in A3, Task 1, Part D). Framework unified to "QAB + BAB" across Tasks 3 and 4 and Part B Phase 1. ✅

**Known soft spots (flagged, not silently assumed):**
- Task 1 Step 4 assumes the hub *may* already link to amazon — the step checks and branches rather than blindly editing.
- `african-grey-parrot-breeders-comparison` is intentionally left out of the species-comparison silo (it's a breeder/trust page) — Part D #6 only audits it for claim safety, doesn't re-silo it.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-13-comparison-pages-workflow.md`. Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task (Tasks 1–5), review between tasks, fast iteration. Best because the 5 reconciliation tasks are independent file edits with clean grep gates.

**2. Inline Execution** — I run Tasks 1–5 in this session with a checkpoint after each.

**Which approach?** (Or: just wanted the analysis/runbook and not the doc fixes yet — say the word and I'll hold Part C.)

# CAGs Comprehensive Page Audit — Skill-Chain Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. The skill being built is a new skill, so the writing-skills **Iron Law applies: RED baseline before the skill is written** (Task 1 before Task 2).

**Goal:** Build `skills/cags-comprehensive-page-audit-system.md` — a single skill that runs a brutal 17-section deep audit (SEO + Semantic + AEO + Entity + UX + CRO + Visual + Backlink) on any CAG page, **as a skill chain** that routes each section to the specialist agent/skill that already owns it and adds the five lenses CAG is currently missing.

**Architecture:** The skill is an **orchestrator/playbook**, not a re-implementation. For the ~11 sections a CAG specialist already covers, the skill dispatches that specialist and folds its output into one report. For the 5 missing lenses (AEO score, entity-coverage score, visual-asset decision table, backlink-magnet score, unified brutal verdict) the skill carries the scoring rubric directly. Output is one dated report to `sessions/`. A documented batch mode runs it across the page inventory to emit a prioritized audit backlog. Built RED→GREEN per writing-skills.

**Tech Stack:** Markdown skill, existing CAG specialist agents/skills (the chain links), `DESIGN.md`/`IMAGE-DESIGNS.md` (color source), Firecrawl/Playwright (real SERP fetches for §3–4), `scripts/health-sweep.sh` + `cag-agent-system-qa` (verification).

**CAG-safety adaptations (binding — fix the ChatGPT-sourced framework on intake):**
- **Palette:** the source framework's `#1F7A4D` green / `#FF6210` orange are STALE (ChatGPT artifacts). Real brand: Forest Green `#2D6A4F`, Clay `#e8604c`, Cream `#faf7f4`. The skill **sources color from `DESIGN.md` + `IMAGE-DESIGNS.md`, never hardcodes**. (See memory `feedback-stale-palette-in-imports`.)
- **No-visible-date** applies to the *site pages the audit recommends changes to* (freshness → schema `dateModified` only). It does NOT apply to the audit report file itself (a normal dated `sessions/` doc). [Per breeder clarification 2026-06-17.]
- **No fabrication / Verified-Claim Ledger:** §3–4 SERP/competitor metrics must be REAL fetches (Firecrawl/Playwright), never invented. Health/credential claims bounded by the Ledger. CITES Appendix I + captive-bred-USA framing.
- **Voice on any proposed copy:** first-person C.A.Gs voice + `anti-ai-writing` blacklist.
- **Confidence Gate ≥97%** before the audit writes to any `site/content/` or `src/pages/` file (the audit *recommends*; it doesn't auto-edit pages unless explicitly told).

**Out of scope:** actually rebuilding audited pages (the audit produces a report + prompts; builders act on it later); the blog/hub work (awaiting research data).

---

## File Structure

| File | Responsibility | Task |
|---|---|---|
| `sessions/2026-06-17-audit-baseline.md` | RED baseline: un-guided audit of a real page + gap annotation | 1 |
| `skills/cags-comprehensive-page-audit-system.md` | The 17-section audit skill-chain: routing table + 5 owned scorers + CAG-safety + output contract + batch mode | 2 |
| `CLAUDE.md` (modify) | Register skill in Technical Skills list + Quick Start "Audit a page" entry + relationship note vs `manual-auditor-check` | 4 |

**Relationship to existing auditors (state this in the skill so they don't collide):**
- `cag-content-audit-agent` = **pre-build** audit (intent/competitor/action-plan/links). This new skill = **any-time strategic** audit of a live/built page.
- `manual-auditor-check` = **final mechanical 29-check QA gate** before deploy, interior pages only. This new skill = **broader strategic verdict**, all page types, and it COVERS the types manual-auditor-check excludes (comparison/location/for-sale/blog).
- `section-auditor` = per-section preserve/patch/rebuild. This new skill calls it for §10.

---

## Task 1: RED baseline — un-guided audit (the failing test)

**Files:** Create `sessions/2026-06-17-audit-baseline.md`

- [ ] **Step 1: Create a feature branch**
```bash
cd /Users/apple/Downloads/CAG
git checkout -b cags-page-audit-skill
```

- [ ] **Step 2: Run the baseline (clean subagent, no skill)**

Dispatch a fresh general-purpose subagent with ONLY: *"Audit the page https://congoafricangreys.com/best-african-grey-parrot-food/ for SEO, AEO, UX, CRO, entities, and visual opportunities. Give scores and recommendations."* Do NOT give it the framework or any CAG context. Save its full output verbatim to `sessions/2026-06-17-audit-baseline.md` under a `## RED Baseline (no skill)` heading.

- [ ] **Step 3: Annotate the gaps**

Below the baseline, add `## Gaps the skill must close` listing what the un-guided audit did wrong/omitted. Expected gaps to capture (verify against the actual output): no consistent 17-section structure; no AEO 0–10 score; no entity-coverage score; no visual-asset decision table (YES-mandatory/recommended/maybe/no); no backlink-magnet score; no single brutal verdict tier; **likely hardcoded or wrong brand colors**; possibly **fabricated competitor metrics** (DA/backlinks guessed, not fetched); generic "add more content" advice with no business-value justification; no CAG-safety (CITES/voice/no-date) awareness; no routing to CAG specialists.

This file is the failing test. **Do not write the skill until it exists.**

- [ ] **Step 4: Commit the baseline**
```bash
cd /Users/apple/Downloads/CAG
git add sessions/2026-06-17-audit-baseline.md
git commit -m "test(audit): RED baseline — un-guided page audit + gap annotation

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push -u origin cags-page-audit-skill
```

---

## Task 2: Write the audit skill-chain (GREEN)

**Files:** Create `skills/cags-comprehensive-page-audit-system.md`

- [ ] **Step 1: Write the skill** with the structure below. Use the user-provided 17-section framework verbatim for the section *headings and output format*, but apply every CAG-safety adaptation and replace the stale palette. Frontmatter is `name` + `description` only (match sibling `skills/manual-auditor-check.md`):

```markdown
---
name: cags-comprehensive-page-audit-system
description: Use when auditing any CongoAfricanGreys.com page deeply — SEO, semantic, AEO, entity, UX, CRO, visual-asset, and backlink — to get one brutal scored verdict with prioritized fixes. Runs as a chain over existing CAG specialists. Triggers: "audit this page", "deep audit", "why isn't this page ranking", "page audit".
---

# CAGs Comprehensive Page Audit System

## Overview
A brutal, no-fluff 17-section audit of ONE page, run as a skill chain: each section routes to the
CAG specialist that owns it; this skill owns the 5 lenses CAG lacked (AEO score, entity-coverage
score, visual-asset table, backlink-magnet score, unified verdict) and assembles everything into one
dated report. Brutal honesty, zero generic advice, every recommendation justified by business/ranking
value.

## When to Use / Not
- USE: strategic audit of a live or built page, any page type, any time.
- NOT: pre-build planning (use `cag-content-audit-agent`); final mechanical QA gate before deploy
  (use `manual-auditor-check`, interior pages). This skill is broader and COVERS the types
  manual-auditor-check excludes (comparison/location/for-sale/blog).

## CAG-Safety (binding — read before scoring)
- **Color:** source ONLY from `DESIGN.md` + `IMAGE-DESIGNS.md` (Forest Green #2D6A4F, Clay #e8604c,
  Cream #faf7f4). Never hardcode; never trust an external palette (#1F7A4D/#FF6210/#FF8C00 are stale).
- **Dates:** recommendations for the SITE page keep freshness in schema (`dateModified`) only — never
  propose a visible date. (This audit REPORT file is itself a normal dated sessions/ doc — that's fine.)
- **No fabrication:** §3–4 competitor metrics must be REAL fetches (Firecrawl, Playwright fallback).
  Never invent DA/backlinks/traffic. Health/credential claims bounded by the Verified-Claim Ledger;
  CITES Appendix I + captive-bred-USA.
- **Voice:** any proposed copy uses first-person C.A.Gs voice + the `anti-ai-writing` blacklist.
- **Confidence Gate:** ≥97% before editing any site file. This skill RECOMMENDS; it edits pages only
  when explicitly told to.

## Page-Type Map (read first → sets section weighting)
Map the page to a CAG type via `data/structure.json`: Homepage · Location (state/city) · Comparison
([X] vs [Y]) · Variant/Attribute · For-sale/Commercial · Care/Health Guide · Species Guide · Blog ·
Interior (about/faq/scam/policy/etc.) · Hub. Note funnel stage (TOFU/MOFU/BOFU). Weighting examples:
For-sale/Variant → CRO + trust heaviest; Care/Guide/Blog → AEO + entity + semantic heaviest; Location
→ local intent + internal links; Comparison → tables + entity coverage.

## The Chain — Section → Specialist Routing
| # | Section | Run / dispatch | This skill adds |
|---|---|---|---|
| 1 | Page identification | self + `data/structure.json` | page-type + funnel tag |
| 2 | Primary search intent | self + `docs/reference/top-pages.md` (GSC) | "what user REALLY wants" |
| 3 | Top-3 SERP competitors | `cag-framework-agent` / `cag-competitor-intel` (REAL fetch) | — |
| 4 | Why CAG wins/loses | self, from §3 | Competitive-Advantage score /10 |
| 5 | Technical SEO | `cag-keyword-verifier` + `seo-rules.md` | per-element /10 |
| 6 | Semantic SEO | `cag-content-audit-agent` (intent/subtopics) + `framework-aio-geo` | missing-topics list |
| 7 | Entity audit | `cag-entity-incorporation-agent` (+ `cag-entity-agent` vocab, Ledger) | **Entity-coverage /10** |
| 8 | NLP / LSI | `keyword-cluster` + `cag-keyword-verifier` | must-add terms (no stuffing) |
| 9 | AEO | `framework-aio-geo` | **AEO /10 rubric (below)** |
| 10 | Content architecture | `framework-heading-hierarchy` + `section-auditor` | improved H-tree |
| 11 | Visual asset audit | `IMAGE-DESIGNS.md` scene-type table | **Visual-need table (below)** |
| 12 | Image prompts | `image-prompt-generator` (IMAGE-DESIGNS wrapper+negatives+palette) | prompts for §11 YES only |
| 13 | Special content blocks | `cag-interactive-component` / `cag-infographic-builder` | relevant-only list |
| 14 | Internal links | `internal-link-agent` | source→dest→anchor |
| 15 | Backlink opportunity | `cag-backlink-outreach-agent` | **Backlink-magnet /10 (below)** |
| 16 | CRO | `cag-conversion-tracker` | CRO /10 |
| 17 | Final scoring + verdict | self | **Scorecard + verdict tier (below)** |

## The 5 Owned Scorers (rubrics this skill carries)
### §9 AEO score /10 — +1 each, present (YES) or not (NO):
quick-answer box · snippet-ready definition · comparison table · FAQ block (visible + FAQPage schema)
· decision tree/checklist · bullet summary · structured data (correct @type) · statistics/research-
backed claim · entity-dense first paragraph · direct-question H2s. Report YES/NO per item, then the /10.
### §7 Entity-coverage /10:
extract entities (species, diseases, brands, foods, breeders, orgs, locations, products, scientific
concepts); /10 = covered ÷ expected-for-this-page-type; list Important Missing Entities + why each
matters for AI understanding. Never assert a Ledger-unverified credential.
### §11 Visual-need (per section, honest — NOT visuals everywhere):
allowed answers YES (Mandatory) / YES (Recommended) / MAYBE / NO. YES only if it improves
comprehension, retention, shareability, backlinks, or conversion — never decorative. Output the table:
`| Section | Need Visual? | Type | Why |` (types per IMAGE-DESIGNS §5 + infographic/table/calculator).
### §15 Backlink-magnet /10:
can this page earn links? score 0–10; if ≥6 suggest the magnet (original breeder data, infographic,
calculator, interactive tool, research) + why a site would link.
### §17 Verdict tier:
Elite / Strong / Good-but-incomplete / Average / Weak / Major-rebuild — with the exact why.

## Output Contract (save to sessions/YYYY-MM-DD-audit-<slug>.md)
Reproduce the user's 17-section structure exactly (Page ID → Final Verdict), then a FINAL SCORECARD:
SEO /10 · Semantic /10 · AEO /10 · Entity /10 · UX /10 · Visual /10 · CRO /10 · Backlink /10 ·
Competitive-Advantage /10 → Verdict tier. Then a **Prioritized Fix List** (highest business impact
first, each with the WHY).

## Batch / Site-Wide Mode
Given a page list (or all of `src/pages/`), run the audit per page but emit ONLY the FINAL SCORECARD
row per page into one table sorted ascending by Competitive-Advantage score → that is the **audit
backlog**. Feed the backlog to `cag-strategy-synthesizer` to prioritize the rebuild queue. Do full
17-section reports only for the bottom N (worst) pages to control cost.

## Output Rules
Brutal honesty · no generic SEO advice · no fluff · explain WHY each rec matters · never force visuals
· prioritize business impact · optimize for 2026 search (AI Overviews, ChatGPT/Perplexity citations,
passage ranking, zero-click).
```

- [ ] **Step 2: Self-check the skill before testing** — confirm: frontmatter name+description only; routing table has all 17 sections; the 5 scorer rubrics are concrete; CAG-safety block present with correct palette; no stale `#1F7A4D`/`#FF6210`; output contract + batch mode present.
```bash
cd /Users/apple/Downloads/CAG
grep -n "1F7A4D\|FF6210\|FF8C00" skills/cags-comprehensive-page-audit-system.md   # expect: no matches
grep -c "2D6A4F\|e8604c\|IMAGE-DESIGNS\|Verified-Claim\|anti-ai-writing" skills/cags-comprehensive-page-audit-system.md  # expect ≥4
```

- [ ] **Step 3: Commit the skill**
```bash
cd /Users/apple/Downloads/CAG
git add skills/cags-comprehensive-page-audit-system.md
git commit -m "feat(audit): add cags-comprehensive-page-audit-system skill-chain (17 sections, routes to specialists + 5 owned scorers)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push
```

---

## Task 3: GREEN verify — re-run WITH the skill

**Files:** append to `sessions/2026-06-17-audit-baseline.md`

- [ ] **Step 1: Re-audit the same page with the skill**

Dispatch a fresh general-purpose subagent. Give it the full text of `skills/cags-comprehensive-page-audit-system.md` and the same target (`/best-african-grey-parrot-food/`). Have it produce the audit to `sessions/2026-06-17-audit-best-food.md`.

- [ ] **Step 2: Score the GREEN result against the baseline gaps**

Append `## GREEN result (with skill)` to `sessions/2026-06-17-audit-baseline.md`: confirm each Task-1 gap is closed — 17-section structure present, all 8+CompAdv scores present, AEO/entity/visual/backlink scorers used, **correct palette only**, competitor metrics are real fetches (or explicitly flagged as "not fetched" rather than invented), every rec has a WHY, CAG-safety respected, verdict tier assigned. Record PASS/FAIL.

- [ ] **Step 3: REFACTOR if needed**

If a gap remains (e.g. agent still guessed competitor DA, or proposed a visible date), tighten the skill's wording (add an explicit counter), re-run Step 1, re-score. Repeat until PASS.

- [ ] **Step 4: Commit the GREEN evidence**
```bash
cd /Users/apple/Downloads/CAG
git add sessions/2026-06-17-audit-baseline.md sessions/2026-06-17-audit-best-food.md skills/cags-comprehensive-page-audit-system.md
git commit -m "test(audit): GREEN — skill produces structured brutal verdict, palette + no-fabrication enforced"
git push
```

---

## Task 4: Wire into CLAUDE.md

**Files:** Modify `CLAUDE.md`

- [ ] **Step 1: Register in the Technical Skills list** (after the `manual-auditor-check` bullet):
```markdown
- `skills/cags-comprehensive-page-audit-system.md` — **brutal 17-section strategic page audit (SEO + Semantic + AEO + Entity + UX + CRO + Visual + Backlink) run as a skill chain** over existing CAG specialists + 5 owned scorers (AEO/entity/visual/backlink/verdict). Any page type, any time. Sources color from DESIGN.md/IMAGE-DESIGNS.md, never fabricates competitor metrics, keeps date recs schema-only. Distinct from `cag-content-audit-agent` (pre-build) and `manual-auditor-check` (final mechanical gate, interior-only). Has a batch mode → audit backlog → feeds cag-strategy-synthesizer.
```

- [ ] **Step 2: Add a Quick Start entry** under "## Quick Start Commands":
```markdown
### "Audit a page" (deep strategic audit)
→ `skills/cags-comprehensive-page-audit-system` (give it a URL) → produces sessions/YYYY-MM-DD-audit-<slug>.md → route fixes to the relevant builder. Batch mode → audit backlog → `@cag-strategy-synthesizer`.
```

- [ ] **Step 3: Commit**
```bash
cd /Users/apple/Downloads/CAG
git add CLAUDE.md
git commit -m "docs: register cags-comprehensive-page-audit-system skill + Quick Start entry

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push
```

---

## Task 5: Verify + finish

- [ ] **Step 1: Health sweep**
```bash
cd /Users/apple/Downloads/CAG
bash scripts/health-sweep.sh --no-build 2>&1 | tail -20
```
Expected: skills count incremented (now 44), all critical checks PASS.

- [ ] **Step 2: Agent-system QA (skill registration consistency)**

Run `cag-agent-system-qa` (or grep) to confirm the skill is registered in CLAUDE.md and well-formed. Fix any gap.

- [ ] **Step 3: Finish the branch** via superpowers:finishing-a-development-branch (offer merge-to-main / PR / keep / discard).

---

## Self-Review

**Spec coverage:** All 17 sections of the user's framework → routing table (Task 2). The 5 missing CAG lenses → owned scorers (Task 2). "Adopt site-wide" → batch mode + audit backlog (Task 2) + Quick Start (Task 4). "Skill chain" → the routing table IS the chain. Both breeder clarifications applied: no-visible-date = site-page-only (CAG-safety block); stale colors corrected to CAG palette (CAG-safety + Task 2 Step 2 grep).

**Placeholder scan:** The skill body's section *prose* is adapted from the user's verbatim framework (provided in full) + the explicit adaptations — the 5 scorer rubrics, routing table, CAG-safety, output contract, and batch mode are all given concretely here. No "TBD".

**Iron Law:** Task 1 (RED baseline) precedes Task 2 (write skill); Task 3 is the GREEN re-test with a REFACTOR loop. Compliant with writing-skills.

**Type consistency:** Skill name `cags-comprehensive-page-audit-system` identical in the file, the two grep checks, CLAUDE.md registration, and Quick Start. Report path pattern `sessions/YYYY-MM-DD-audit-<slug>.md` consistent across Task 2 output contract and Task 3.
```

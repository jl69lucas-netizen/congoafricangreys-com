# Rules & Skills Upgrade — Session 2026-07-29 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bank the 2026-07-26 and 2026-07-28 for-sale-cluster lessons into enforceable tooling — one new discipline skill, two new scanner checks, a fixed seam probe, a header-style selection layer, a Reddit thread-sourcing protocol, and a WORKFLOW.md that matches the pipeline actually in use.

**Architecture:** Nothing here is a new system. Every item either (a) adds a check to the existing `scripts/page_hardening_scan.py` under its existing `add(sev, check, file, line, msg, fix)` contract with a RED fixture in `tests/`, (b) extends an existing skill file in `skills/`, or (c) corrects a reference doc that has drifted from reality. The one genuinely new artifact is `skills/cag-gate-integrity.md`, whose RED baseline is 9 recorded production failures rather than a synthetic scenario.

**Tech Stack:** Python 3 (stdlib only — `re`, `glob`, `sys`, `json`), pytest 8.4.2, Astro, zsh. No new dependencies.

**Approved by the breeder 2026-07-29:** scope = items 1–5 plus the agent model flip. GSC/GA4 MCP, the CLAUDE.md core/site split, and `cag-asset-proofing` are **explicitly deferred to the next session** (approach for MCP already approved: official Google GA4 MCP + `AminForou/mcp-gsc`).

---

## File Structure

| File | Action | Responsibility |
|---|---|---|
| `data/agent-registry.json` | Modify | Tier table — flip the 3 tiers to `claude-opus-5` |
| `scripts/seam_parity.py` | **Create** | The one correct seam↔section probe; replaces the broken inline grep |
| `tests/test_seam_parity.py` | **Create** | RED fixture: the broken grep reads 0 sections on congo |
| `scripts/page_hardening_scan.py` | Modify | Add `check_class_drift` (§1k) + `check_component_color_specificity` (§1l) |
| `tests/test_page_hardening_new_checks.py` | Modify | RED fixtures for both new checks, verbatim from the 07-28 defects |
| `skills/cag-page-hardening.md` | Modify | v2.0 — §1k, §1l, Playwright mandate in §2, §6 small-things |
| `skills/cag-gate-integrity.md` | **Create** | NEW discipline skill: verify the gate before you fix the page |
| `skills/framework-heading-hierarchy.md` | Modify | §Header Style Selection + page-type routing + justification requirement |
| `scripts/add_header_style_rule.py` | **Create** | Idempotent Golden-Rule injector for all 68 agents |
| `skills/reddit-strategy.md` | Modify | §Thread Sourcing Protocol |
| `data/reddit-thread-ledger.json` | **Create** | Thread Diversity Ledger — which thread is spent on which page |
| `docs/reference/WORKFLOW.md` | Modify | Rewrite to the live 7-sprint model; retire `interior_29_audit.py` routing |
| `docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md` | Modify | Fix the broken §5/§8 seam command |
| `CLAUDE.md` | Modify | Register the new skill/script pointers + the prompt-restatement rule |

**Non-negotiables that apply to every task below:** work on `main` (never a feature branch); commit + `git push` after each task; run `python3 scripts/register_skills.py --copy` after any skill add/rename; never edit `.claude/skills/` by hand.

---

## Task 1: Flip all 68 agents to Opus 5

**Files:**
- Modify: `data/agent-registry.json:3-16` (the `_meta.tiers` block)

- [ ] **Step 1: Read the current tier block to confirm the exact shape**

Run: `python3 -c "import json;print(json.dumps(json.load(open('data/agent-registry.json'))['_meta'],indent=1))"`

Expected: three tiers `opus48_max`, `opus48_high`, `opus48_medium`, each `{"model":"claude-opus-4-8","effort":...}`.

- [ ] **Step 2: Rewrite the tier models, keeping the tier KEYS unchanged**

Keep the key names (`opus48_*`) so the 68 per-agent `"tier"` values keep resolving — only the `model` value and the description change.

```python
python3 - <<'PY'
import json, pathlib
p = pathlib.Path("data/agent-registry.json")
d = json.loads(p.read_text())
for t in d["_meta"]["tiers"].values():
    t["model"] = "claude-opus-5"
d["_meta"]["description"] = ("CAG Agent Model Tier Registry — single source of truth. "
    "All agents on Opus 5 (flipped from 4.8 on 2026-07-29); effort is the cost lever. "
    "NOTE: `effort` is NOT a native Claude Code field — apply_model_tiers.py enforces it "
    "as a prose directive between EFFORT:START/END markers.")
d["_meta"]["last_updated"] = "2026-07-29"
p.write_text(json.dumps(d, indent=2) + "\n")
print("tiers now:", {k: v["model"] for k, v in d["_meta"]["tiers"].items()})
PY
```

Expected output: `tiers now: {'opus48_max': 'claude-opus-5', 'opus48_high': 'claude-opus-5', 'opus48_medium': 'claude-opus-5'}`

- [ ] **Step 3: Apply to all 68 agents and verify**

Run: `python3 scripts/apply_model_tiers.py && bash scripts/verify_model_tiers.sh`

Then confirm no 4.8 survives:

```bash
grep -rh "^model:" .claude/agents/*.md | sort | uniq -c
```

Expected: `68 model: claude-opus-5` and nothing else.

- [ ] **Step 4: Check for the known cosmetic drift before staging**

`apply_model_tiers.py` is documented in memory as introducing blank-line drift. Inspect and revert any file whose ONLY change is whitespace:

```bash
git diff --stat .claude/agents/ | tail -3
git diff --numstat .claude/agents/ | awk '$1==$2 && $1<=1 {print $3}'
```

Any file printed by the second command is a whitespace-only touch — `git checkout --` it to keep the commit focused.

- [ ] **Step 5: Commit**

```bash
git add data/agent-registry.json .claude/agents/
git commit -m "chore(agents): flip all 68 agents from Opus 4.8 to Opus 5

Registry-driven per CLAUDE.md. Tier KEYS keep their opus48_* names so the
68 per-agent tier values still resolve; only the model value changes.

Also records that \`effort\` is not a native Claude Code frontmatter field —
apply_model_tiers.py enforces it as an injected prose directive.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 2: RED — a failing test for the seam-parity probe

**Files:**
- Create: `tests/test_seam_parity.py`

The playbook's command `grep -c '<section class="sec"'` returns **0 sections on 6 of the 8 built for-sale pages**, because only adoption-cost and health-guarantee use that class. Measured 2026-07-29:

| Page | seams | `<section` | diff |
|---|---|---|---|
| eggs | 15 | 16 | 1 |
| congo | 15 | 15 | 0 |
| timneh | 18 | 18 | 0 |
| hand-raised | 18 | 19 | 1 |
| health-guarantee | 17 | 18 | 1 |
| dna-tested | 18 | 19 | 1 |
| baby | 21 | 22 | 1 |
| adoption-cost | 10 | 10 | 0 |

The house idiom is one seam before every section; the hero section legitimately has no seam above it. So the correct gate is **`sections - seams <= 1`**, and the correct section count is `<section` (any attributes), not a class match.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_seam_parity.py
#
# RED fixture for the broken seam-parity probe. The command published in
# docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md §5/§8
#   grep -c '<section class="sec"' src/pages/<slug>/index.astro
# returns 0 on 6 of 8 built for-sale pages, so "seams == sections" was compared
# against zero and silently told the reviewer nothing. Measured 2026-07-29.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import seam_parity as S


CONGO = '''<section class="chero">
<div class="seam"></div><section id="s1"><h2>One</h2></section>
<div class="seam"></div><section id="s2"><h2>Two</h2></section>
'''


def test_counts_sections_without_a_class_attribute():
    """The real congo/timneh/baby markup uses <section id=...>, not class="sec"."""
    assert S.count_sections(CONGO) == 3


def test_counts_seams():
    assert S.count_seams(CONGO) == 2


def test_hero_without_a_seam_is_allowed():
    """3 sections / 2 seams — the hero legitimately has no seam above it."""
    assert S.verdict(CONGO) == ("PASS", 3, 2)


def test_a_genuinely_missing_seam_fails():
    """health-guarantee shipped 7 seams across 17 sections. diff > 1 must FAIL."""
    bad = '<section class="hero"></section>' + '<section id="x"><h2>H</h2></section>' * 5
    verdict, sections, seams = S.verdict(bad)
    assert (verdict, sections, seams) == ("FAIL", 6, 0)


def test_does_not_count_the_closing_tag():
    assert S.count_sections("<section></section>") == 1
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python3 -m pytest tests/test_seam_parity.py -q`

Expected: collection error — `ModuleNotFoundError: No module named 'seam_parity'`.

- [ ] **Step 3: Commit the RED test**

```bash
git add tests/test_seam_parity.py
git commit -m "test(seam): RED — the published seam-parity grep reads 0 sections on 6 of 8 pages

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 3: GREEN — implement `scripts/seam_parity.py`

**Files:**
- Create: `scripts/seam_parity.py`
- Test: `tests/test_seam_parity.py`

- [ ] **Step 1: Write the minimal implementation**

```python
#!/usr/bin/env python3
"""
Seam↔section parity probe. Owned by skills/cag-page-hardening.md.

House idiom (2026-07-26): one `<div class="seam">` before every section. The hero
section carries no seam above it, so `sections - seams <= 1` is correct and
`sections - seams > 1` means a section shipped without its seam
(health-guarantee shipped 7 seams across 17 sections).

Do NOT count sections by class. congo/timneh/baby/eggs/dna-tested/hand-raised use
`<section id=...>` with no class, so the previously published
`grep -c '<section class="sec"'` returned 0 and compared against nothing.

Usage:
  python3 scripts/seam_parity.py                    # every page under src/pages
  python3 scripts/seam_parity.py <slug> [<slug>]    # named pages
Exit code 1 if any page FAILs.
"""
import re, sys, glob

SECTION = re.compile(r"<section\b", re.I)
SEAM = re.compile(r'class="[^"]*\bseam\b[^"]*"', re.I)


def count_sections(text):
    return len(SECTION.findall(text))


def count_seams(text):
    return len(SEAM.findall(text))


def verdict(text):
    """Return (PASS|FAIL, sections, seams). Tolerance of 1 = the seamless hero."""
    s, m = count_sections(text), count_seams(text)
    return ("PASS" if s - m <= 1 else "FAIL", s, m)


def main():
    slugs = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = sorted(glob.glob("src/pages/**/index.astro", recursive=True))
    if slugs:
        files = [f for f in files if any(s in f for s in slugs)]
    if not files:
        print("seam-parity: 0 pages matched — CHECK YOUR SLUGS, this is not a pass.")
        return 1
    bad = 0
    print(f"seam-parity — {len(files)} pages examined\n")
    for f in files:
        v, s, m = verdict(open(f, encoding="utf-8").read())
        slug = f.split("/")[2] if len(f.split("/")) > 2 else f
        print(f"  {v:4}  {slug:<52} sections={s:<3} seams={m:<3} missing={max(0, s - m - 1)}")
        bad += v == "FAIL"
    print(f"\n{bad} FAIL / {len(files)} pages")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
```

Note the zero-match branch prints an explicit warning rather than a pass — that is the `cag-gate-integrity` lesson from the zsh word-split trap, applied to a gate we are writing ourselves.

- [ ] **Step 2: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_seam_parity.py -q`

Expected: `5 passed`.

- [ ] **Step 3: Run it against the 8 built pages and confirm the numbers match the table in Task 2**

```bash
python3 scripts/seam_parity.py african-grey-parrot-bird-eggs-for-sale-usa congo-african-grey-for-sale timneh-african-grey-for-sale hand-raised-african-grey-parrot-for-sale african-greys-for-sale-with-health-guarantee dna-tested-african-grey-for-sale baby-african-grey-parrot-for-sale african-grey-parrot-adoption-cost
```

Expected: `8 pages examined`, all `PASS`, and the sections/seams columns equal to the Task 2 table. **Read the page count** — if it says 0 or 1, the slugs did not word-split and the run proved nothing.

- [ ] **Step 4: Prove the gate is not blinded**

Delete one seam from a scratch copy and confirm FAIL:

```bash
cp src/pages/congo-african-grey-for-sale/index.astro /tmp/congo.bak
python3 - <<'PY'
p="src/pages/congo-african-grey-for-sale/index.astro"
s=open(p).read(); i=s.find('<div class="seam"></div>')
open(p,"w").write(s[:i] + s[i+len('<div class="seam"></div>'):])
PY
python3 scripts/seam_parity.py congo-african-grey-for-sale   # expect FAIL, missing=1
cp /tmp/congo.bak src/pages/congo-african-grey-for-sale/index.astro
python3 scripts/seam_parity.py congo-african-grey-for-sale   # expect PASS again
git diff --stat src/pages/congo-african-grey-for-sale/index.astro   # expect EMPTY
```

- [ ] **Step 5: Fix the broken command in the lessons doc**

In `docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md`, replace the §5 command block and the §8 step-2 block with:

```bash
python3 scripts/seam_parity.py <slug> [<slug> ...]   # NEVER grep '<section class="sec"' — see 2026-07-29
```

- [ ] **Step 6: Commit**

```bash
git add scripts/seam_parity.py tests/test_seam_parity.py docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md
git commit -m "fix(gates): replace the broken seam-parity grep with a real probe

The published command matched class=\"sec\", which only 2 of 8 built for-sale
pages use, so seams were compared against 0 sections. Correct probe counts
<section (any attributes) and allows exactly one seamless hero.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 4: RED — failing test for `check_class_drift` (§1k)

**Files:**
- Modify: `tests/test_page_hardening_new_checks.py` (append)

The 07-28 headline defect: 101 classes styled and never rendered — including five components the for-sale spec mandates — plus two rendered components pointing at the wrong class names. `page_hardening_scan.py` returned `0 ERROR · 0 WARN` on that page.

- [ ] **Step 1: Append the failing test**

```python
# ── 10. markup-css-drift (§1k) ───────────────────────────────────────────────
# The 2026-07-28 adoption-cost defect. The page was assembled by porting the CSS
# kit and hand-writing markup that drifted from it: 101 classes styled and never
# rendered (5 of them spec-mandated components) and 2 rendered components pointing
# at the wrong class name. The scanner returned 0 ERROR / 0 WARN on that page.
DRIFT_SRC = '''---
const x = 1;
---
<main class="adopt">
  <p class="faqC-x">Is the fee the same as the cost?</p>
  <div class={`tile ${x ? "on" : "off"}`}></div>
</main>
<style>
.adopt{color:#111}
.faqC-x{width:16px}
.faqC-q{font-size:1.05rem}
.doc-stack{display:grid}
.tile{border:0}
.on{opacity:1}
.off{opacity:.4}
</style>'''


def test_class_drift_reports_styled_but_never_rendered():
    found = run(H.check_class_drift, [("src/pages/adoption/index.astro", DRIFT_SRC)])
    d = checks_named(found, "markup-css-drift")
    assert d, "must report the classes that are styled but never rendered"
    assert "faqC-q" in d[0]["msg"]
    assert "doc-stack" in d[0]["msg"]


def test_class_drift_flags_spec_mandated_components_as_ERROR():
    """.doc-stack is mandated by the for-sale spec — a missing component, not dead code."""
    found = run(H.check_class_drift, [("src/pages/adoption/index.astro", DRIFT_SRC)])
    assert any(f["sev"] == "ERROR" and "doc-stack" in f["msg"]
               for f in checks_named(found, "markup-css-drift"))


def test_class_drift_reports_classes_used_with_no_css():
    src = DRIFT_SRC.replace(".faqC-x{width:16px}\n", "")
    found = run(H.check_class_drift, [("src/pages/adoption/index.astro", src)])
    assert any("faqC-x" in f["msg"] for f in checks_named(found, "markup-css-orphan"))


def test_class_drift_understands_template_literal_classes():
    """`class={`tile ${x?"on":"off"}`}` must count tile/on/off as RENDERED."""
    found = run(H.check_class_drift, [("src/pages/adoption/index.astro", DRIFT_SRC)])
    msgs = " ".join(f["msg"] for f in found)
    for cls in ("tile", "on", "off"):
        assert f" {cls}" not in msgs and f"{cls}," not in msgs, f"{cls} is rendered"


def test_class_drift_skips_files_with_no_style_block():
    found = run(H.check_class_drift, [("src/pages/x/index.astro", "<main class='a'></main>")])
    assert found == []
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m pytest tests/test_page_hardening_new_checks.py -q -k class_drift`

Expected: 5 errors — `AttributeError: module 'page_hardening_scan' has no attribute 'check_class_drift'`.

- [ ] **Step 3: Commit the RED test**

```bash
git add tests/test_page_hardening_new_checks.py
git commit -m "test(hardening): RED — markup/CSS drift is invisible to the scanner

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 5: GREEN — implement `check_class_drift`

**Files:**
- Modify: `scripts/page_hardening_scan.py` (add the check, then register it in `main()`)

- [ ] **Step 1: Add the check function above `def main():`**

```python
# ─────────────────────────────────────────────────────────────────────────────
# 1k. markup↔CSS drift — the 2026-07-28 adoption-cost failure mode.
#     A page assembled by porting the CSS kit and hand-writing markup drifts:
#     classes get styled and never rendered, and rendered components point at the
#     wrong class name. `page_hardening_scan` returned 0 ERROR / 0 WARN on a page
#     whose FAQ answers were white-on-white and whose 5 mandated components had no
#     markup behind them at all.
#
#     TRIAGE IS REQUIRED, and the check cannot do it for you:
#       styled + never rendered + spec-mandated  → MISSING COMPONENT. Render it.
#       styled + never rendered + variant-not-used → DEAD CODE. Delete it.
#     Deleting the CSS of a mandated component hides a spec violation.
# ─────────────────────────────────────────────────────────────────────────────

# Components the for-sale spec mandates. Sourced from
# sessions/2026-07-19-for-sale-component-map.md + the 2026-07-28 harden pass,
# where all seven of these shipped as CSS with no markup behind them.
SPEC_MANDATED = {
    "doc-stack", "otA", "geo-pin", "geo-arrow", "read-img",
    "vflags", "chkB", "fs-video", "xsell", "seam",
}


def _rendered_classes(markup):
    """Every class token the markup can actually emit, including dynamic forms."""
    used = set()
    for m in re.finditer(r'class(?:Name)?="([^"{}]+)"', markup):
        used.update(m.group(1).split())
    for m in re.finditer(r"class(?:Name)?=\{`([^`]*)`\}", markup):
        inner = re.sub(r"\$\{[^}]*\}", " ", m.group(1))
        used.update(re.findall(r"[A-Za-z][\w-]*", inner))
    for m in re.finditer(r'class(?:Name)?=\{[^}]*?"([^"]+)"', markup):
        used.update(m.group(1).split())
    return used


def check_class_drift(src_pairs):
    for f, text in src_pairs:
        i = text.find("<style>")
        if i == -1:
            continue
        markup, css = text[:i], text[i:]
        css = css[:css.find("<script")] if "<script" in css else css
        used = _rendered_classes(markup)
        defined = set(re.findall(r"^\s*\.([A-Za-z][\w-]*)", css, re.M))
        # Classes styled but never rendered.
        unrendered = sorted(defined - used)
        mandated = [c for c in unrendered if c in SPEC_MANDATED]
        dead = [c for c in unrendered if c not in SPEC_MANDATED]
        if mandated:
            add("ERROR", "markup-css-drift", f, None,
                f"{len(mandated)} SPEC-MANDATED component(s) styled but never rendered: "
                + ", ".join(mandated),
                "Render them. Do NOT delete the CSS — that hides a spec violation. "
                "See skills/cag-page-hardening.md §1k.")
        if dead:
            add("WARN", "markup-css-drift", f, None,
                f"{len(dead)} class(es) styled but never rendered: " + ", ".join(dead),
                "Triage each: a variant this page does not ship → delete; a component "
                "the spec mandates → render it. Never bulk-delete.")
        # Classes rendered with no rule at all — the 'wrong class name' half.
        orphans = sorted(c for c in used - defined
                         if not re.search(rf"[.\[]{re.escape(c)}\b", css))
        if orphans:
            add("WARN", "markup-css-orphan", f, None,
                f"{len(orphans)} class(es) in markup with no CSS rule: " + ", ".join(orphans),
                "Either the component name is misspelled (adoption-cost put FAQ text in "
                "`.faqC-x`, a 16x16 icon box) or the rule lives in a global sheet — confirm which.")
```

- [ ] **Step 2: Register it in `main()`**

In `scripts/page_hardening_scan.py`, inside `main()`, immediately after the line `check_smooth_scroll(src_pairs)`, add:

```python
    # 2026-07-29: markup↔CSS drift + component specificity (adoption-cost lessons)
    check_class_drift(src_pairs)
```

- [ ] **Step 3: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_page_hardening_new_checks.py -q -k class_drift`

Expected: `5 passed`.

- [ ] **Step 4: Run the full suite — no regressions**

Run: `python3 -m pytest tests/ -q`

Expected: all pre-existing tests still pass alongside the new ones.

- [ ] **Step 5: Run the real scanner on the 8 built pages and TRIAGE, do not fix**

```bash
python3 scripts/page_hardening_scan.py congo-african-grey-for-sale timneh-african-grey-for-sale african-grey-parrot-adoption-cost baby-african-grey-parrot-for-sale 2>&1 | tail -40
```

Per `cag-gate-integrity`: record each finding as REAL / DEAD-CODE / FALSE-POSITIVE in the session brief. **Do not edit any page in this task** — this task ships the check, not the fixes. If the check produces obvious noise (e.g. classes defined in a shared stylesheet), fix the check, not the page.

- [ ] **Step 6: Commit**

```bash
git add scripts/page_hardening_scan.py tests/test_page_hardening_new_checks.py
git commit -m "feat(hardening): add markup-css-drift check (§1k)

Catches the 2026-07-28 adoption-cost failure mode: 101 classes styled and never
rendered, 5 of them spec-mandated components, plus 2 components pointing at the
wrong class name — all while the scanner reported 0 ERROR / 0 WARN.

Spec-mandated names ERROR (render them); everything else WARNs for triage,
because deleting a mandated component's CSS hides a spec violation.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 6: RED — failing test for `check_component_color_specificity` (§1l)

**Files:**
- Modify: `tests/test_page_hardening_new_checks.py` (append)

The concrete mechanism behind "the component looks wrong": `.ship-tier{color:#fff}` has specificity (0,1,0) and loses to `.ship-c p{color:#5b524a}` at (0,1,1) — dark grey on forest green, **1.19:1**.

**Scope note:** this check covers **color-vs-color** only. The FAQ white-on-white defect was a *background* set by a wrongly-applied class, which `check_class_drift` (§1k) and the existing runtime contrast sweep (§2b) catch instead. Do not widen this check to backgrounds — say so in the skill.

- [ ] **Step 1: Append the failing test**

```python
# ── 11. component-color-loses-to-descendant (§1l) ────────────────────────────
# `.ship-tier{color:#fff}` is (0,1,0) and loses to `.ship-c p{color:#5b524a}` at
# (0,1,1): dark grey on forest green, 1.19:1, on the live adoption-cost page.
# Colour-vs-colour only — the background half is §1k + the runtime sweep §2b.
SPECIFICITY_SRC = '''<div class="ship-c">
  <p class="ship-tier">Airport pickup $185</p>
</div>
<style>
.ship-c{background:#2D6A4F}
.ship-c p{color:#5b524a}
.ship-tier{color:#fff}
</style>'''


def test_component_color_loses_to_kit_descendant_rule():
    found = run(H.check_component_color_specificity,
                [("src/pages/adoption/index.astro", SPECIFICITY_SRC)])
    d = checks_named(found, "component-color-loses-to-descendant")
    assert d, "must flag .ship-tier losing to .ship-c p"
    assert "ship-tier" in d[0]["msg"] and "ship-c p" in d[0]["msg"]


def test_qualified_component_rule_is_not_flagged():
    """The prescribed fix — qualify the component rule — must clear the check."""
    fixed = SPECIFICITY_SRC.replace(".ship-tier{color:#fff}", ".ship-c p.ship-tier{color:#fff}")
    found = run(H.check_component_color_specificity,
                [("src/pages/adoption/index.astro", fixed)])
    assert checks_named(found, "component-color-loses-to-descendant") == []


def test_no_flag_when_the_component_class_is_never_nested_there():
    """.ship-tier used outside .ship-c cannot be beaten by .ship-c p."""
    other = SPECIFICITY_SRC.replace('<div class="ship-c">', '<div class="other">')
    found = run(H.check_component_color_specificity,
                [("src/pages/adoption/index.astro", other)])
    assert checks_named(found, "component-color-loses-to-descendant") == []


def test_no_flag_without_a_bare_tag_descendant_rule():
    plain = '<p class="a">x</p><style>.a{color:#fff}</style>'
    found = run(H.check_component_color_specificity, [("src/pages/x/index.astro", plain)])
    assert found == []
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m pytest tests/test_page_hardening_new_checks.py -q -k specificity`

Expected: 4 errors — `AttributeError: ... has no attribute 'check_component_color_specificity'`.

- [ ] **Step 3: Commit the RED test**

```bash
git add tests/test_page_hardening_new_checks.py
git commit -m "test(hardening): RED — component colour rules silently lose to kit descendant rules

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 7: GREEN — implement `check_component_color_specificity`

**Files:**
- Modify: `scripts/page_hardening_scan.py`

- [ ] **Step 1: Add the check function above `def main():`**

```python
# ─────────────────────────────────────────────────────────────────────────────
# 1l. component-color-loses-to-descendant — the concrete mechanism behind
#     "this component looks wrong" (three instances on one page, 2026-07-28).
#     `.ship-tier{color:#fff}` is (0,1,0); `.ship-c p{color:#5b524a}` is (0,1,1)
#     and wins → dark grey on forest green, 1.19:1, shipped live.
#     Fix: qualify the component rule — `.ship-c p.ship-tier{...}`.
#     COLOUR-vs-COLOUR ONLY. The background half (the white-on-white FAQ) is
#     §1k plus the runtime contrast sweep §2b — do not widen this check to it.
# ─────────────────────────────────────────────────────────────────────────────
BARE_TAGS = ("p", "li", "span", "dt", "dd", "a", "small", "strong", "em")


def check_component_color_specificity(src_pairs):
    for f, text in src_pairs:
        i = text.find("<style>")
        if i == -1:
            continue
        markup, css = text[:i], text[i:]
        css = css[:css.find("<script")] if "<script" in css else css

        # Kit rules of the form `.ancestor tag{...color...}` — specificity (0,1,1).
        descendants = []
        for m in re.finditer(r"\.([A-Za-z][\w-]*)\s+([a-z]+)\s*\{([^}]*)\}", css):
            anc, tag, body = m.group(1), m.group(2), m.group(3)
            if tag in BARE_TAGS and re.search(r"(?<![-\w])color\s*:", body):
                descendants.append((anc, tag))

        # Component rules of the form `.component{...color...}` — specificity (0,1,0).
        singles = {m.group(1) for m in
                   re.finditer(r"(?<![\w.\s>+~])\.([A-Za-z][\w-]*)\s*\{([^}]*)\}", css)
                   if re.search(r"(?<![-\w])color\s*:", m.group(2))}

        for anc, tag in descendants:
            if f'class="{anc}"' not in markup and f"{anc} " not in markup and f" {anc}" not in markup:
                continue
            for comp in sorted(singles):
                if comp == anc:
                    continue
                # The component must actually be applied to that bare tag in the markup.
                if not re.search(rf'<{tag}\b[^>]*class="[^"]*\b{re.escape(comp)}\b', markup):
                    continue
                # …and nested under the ancestor somewhere in this file.
                if not re.search(rf'class="[^"]*\b{re.escape(anc)}\b[^"]*"',  markup):
                    continue
                add("WARN", "component-color-loses-to-descendant", f, None,
                    f".{comp} (0,1,0) sets color but `.{anc} {tag}` (0,1,1) outranks it — "
                    f"the component colour is silently discarded",
                    f"Qualify the component rule: `.{anc} {tag}.{comp}{{...}}`. "
                    "Confirm with getComputedStyle in Playwright before editing "
                    "(skills/cag-gate-integrity.md).")
```

- [ ] **Step 2: Register it in `main()`**

Directly beneath the `check_class_drift(src_pairs)` line added in Task 5:

```python
    check_component_color_specificity(src_pairs)
```

- [ ] **Step 3: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_page_hardening_new_checks.py -q -k specificity`

Expected: `4 passed`.

- [ ] **Step 4: Full suite + real run**

Run: `python3 -m pytest tests/ -q`
Expected: all pass.

Run: `python3 scripts/page_hardening_scan.py 2>&1 | tail -25`

This is a WARN-only check. Triage the output — if it produces more than a handful of hits site-wide, tighten the nesting test rather than accept noise. A gate nobody trusts is worse than no gate.

- [ ] **Step 5: Commit**

```bash
git add scripts/page_hardening_scan.py tests/test_page_hardening_new_checks.py
git commit -m "feat(hardening): add component-color-loses-to-descendant check (§1l)

Three instances shipped on adoption-cost. Colour-vs-colour only; the background
half stays with §1k and the runtime contrast sweep.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 8: `cag-page-hardening` → v2.0

**Files:**
- Modify: `skills/cag-page-hardening.md` (header, §1 catalogue, §2 preamble, §6 new)

- [ ] **Step 1: Bump the version line**

Replace line 6 `# SKILL: CAG Page Hardening (v1.0 — 2026-07-23)` with:

```markdown
# SKILL: CAG Page Hardening (v2.0 — 2026-07-29)

**v2.0 adds the 2026-07-28 adoption-cost lessons.** v1.0 assumed the enemy was a
defect the scanner could not see. v2.0 assumes the harder case: **a clean scan on
a broken page.** `page_hardening_scan.py` returned `0 ERROR · 0 WARN` on a page
whose FAQ answers were invisible (1.00:1) and whose five mandated components had
no markup behind them. Both halves — static scan AND runtime probes — are
mandatory, always. Before you fix anything a gate reports, read
**skills/cag-gate-integrity.md**: nine checkers have cried wolf on this cluster.
```

- [ ] **Step 2: Add §1k and §1l to the catalogue**

Insert after §1j (`smooth-scroll-breaks-anchors`, ends near line 250):

```markdown
### 1k. `markup-css-drift` / `markup-css-orphan` — ERROR / WARN — *the clean-scan trap*
The page was assembled by porting the CSS kit and hand-writing markup that drifted
from it. On `/african-grey-parrot-adoption-cost/`: **101 classes defined and never
rendered** (five of them components the for-sale spec mandates) and the two that
*were* rendered pointed at **the wrong class names** — FAQ question text sat in
`.faqC-x`, a 16×16 icon box, so every question crushed to 16px.

**Triage is mandatory and the scanner cannot do it for you:**

| Styled, never rendered | When | Action |
|---|---|---|
| **Missing component** | the spec mandates it (`.doc-stack`, `.otA`, `.geo-pin`, `.read-img`, `.vflags`, `.chkB`, `.fs-video`) | **Render it.** Deleting the CSS hides a spec violation. |
| **Dead code** | it belongs to a variant this page does not ship (`.k1` when the page ships K2) | Delete it. |

On adoption-cost that split was **7 missing components vs 30 genuinely dead classes**.
Spec-mandated names raise ERROR; everything else WARNs. Never bulk-delete a WARN list.

### 1l. `component-color-loses-to-descendant` — WARN — *"the component looks wrong"*
Every such complaint on adoption-cost traced to a generic descendant selector
out-ranking a component selector:

| Component rule | Beaten by | Result |
|---|---|---|
| `.ship-tier{color:#fff}` (0,1,0) | `.ship-c p{color:#5b524a}` (0,1,1) | dark grey on forest green, **1.19:1** |
| answer in `.faq-d` (`background:#fff`) inside the dark accordion | `.faqC-item p{color:rgba(255,255,255,.82)}` | **white on white, 1.00:1 — invisible** |

**Rule:** when a component's inner element is a bare tag (`p`, `span`, `li`, `dt`,
`dd`), qualify the component rule — `.ship-c p.ship-tier{…}` — or the kit's generic
descendant rules silently win.

Scope: the check covers **colour vs colour**. The second row above is a *background*
set by a wrongly-applied class — that is §1k plus the runtime contrast sweep §2b.
Do not widen §1l to backgrounds; it would flood.
```

- [ ] **Step 3: Make Playwright mandatory in §2 — the Browser pane cannot measure**

Insert immediately under the `## 2. Runtime probes` heading (line 251):

```markdown
> **Use Playwright, not the Browser pane.** The Browser pane reports `vw: 0` and
> every `getBoundingClientRect()` comes back zero — elements are in the DOM but
> nothing paints, so every probe below reads as a false pass. Sequence:
> `browser_resize` → `browser_navigate` → `browser_evaluate`. Banked as
> `reference_intersectionobserver_needs_painting_page`; it applies to ALL
> measurement, not just scroll-spy.
>
> **Breakpoints: 375 / 768 / 1280 — and 768 is the one that fails.** On the
> adoption-cost pass, 375 and 1280 were clean and *every* line-length defect was
> at tablet.
>
> **Capture components with element screenshots** (`browser_take_screenshot` with
> `target`). A viewport screenshot resets scroll and a prior `scrollIntoView` does
> not survive it.
>
> **Your own probes are gates too.** Two of mine were wrong on 2026-07-28: the
> contrast sweep tested `display:none` on the element but not on its ancestors
> (8 of 13 "failures" evaporated — skip when `!el.offsetParent` or the rect is
> zero-sized), and a hero measured 432px only because I included its `16px 0 20px`
> padding instead of measuring `.hero-grid`, the element the spec names.
```

- [ ] **Step 4: Add §6 — small things that shipped anyway**

Append before `## 5. Handoff` (renumber Handoff to §7 if it sits at §5):

```markdown
## 6. Small defects that reached production anyway

- **`caption` must join the mobile `display:block` list.** Left as
  `display:table-caption` under a `display:block` table, the browser wraps it in an
  anonymous table box that shrink-wraps to ~70px and stacks the title one word per
  line. This — not font-size — was the true cause of "the ledger title is too thick."
- **`max-width:none` is conditional, not wrong.** Correct while a card is a narrow
  2-up column; a bug the moment that grid collapses to `1fr`. `.ship-c p` and
  `.quote-c p` measured 90ch at 768. Check every uncapped paragraph at the
  breakpoint where its container goes full width.
- **A long card label breaks the button baseline.** `View Jins & Jeni (Pair) →`
  wrapped to two lines while five siblings stayed on one. Shorten the label; never
  add `nowrap` to a label that cannot fit.
- **Every printed figure reads from the data files.** The adoption-cost plan
  hand-drafted `$240–$420` food; `financial-entities.json` says `$200–$400`, and
  flight nanny is `750`, not `700`. Render through a helper (`orange(an.food_and_treats)`),
  never a typed literal — a literal is a future contradiction.
- **Orphaned assets are a real category.** Six OG photos were committed and never
  referenced by any markup, and `heroPreload` pointed at one of them — 94 KB
  preloaded for an image the page never rendered. Diff `public/` against the page
  before assuming images are missing.
- **Seam parity: `python3 scripts/seam_parity.py <slug>`.** Never
  `grep -c '<section class="sec"'` — only 2 of 8 for-sale pages use that class, so
  the published command compared seams against zero (fixed 2026-07-29).
- **Sitemap regeneration on a no-URL-change edit is churn** — the generator stamps
  today's date on all 109 URLs. Run it for the phantom-URL check, then revert if the
  URL set is unchanged.
```

- [ ] **Step 5: Verify the skill still loads and register**

```bash
python3 -c "
import re,sys
t=open('skills/cag-page-hardening.md').read()
assert t.startswith('---'), 'frontmatter missing'
fm=t[3:t.find('\n---',3)]
assert 'name: cag-page-hardening' in fm and 'description:' in fm
assert len(fm) < 1024, f'frontmatter {len(fm)} chars — max 1024'
for s in ('1k.','1l.','## 6.','seam_parity','Playwright'): assert s in t, s
print('OK', t.count(chr(10)), 'lines')
"
python3 scripts/register_skills.py --copy
```

Expected: `OK <n> lines`, then the register script reporting the mirror written.

- [ ] **Step 6: Commit**

```bash
git add skills/cag-page-hardening.md .claude/skills/cag-page-hardening/
git commit -m "docs(hardening): cag-page-hardening v2.0 — the clean-scan-on-a-broken-page lessons

Adds §1k markup-CSS drift, §1l component colour specificity, the Playwright
mandate (the Browser pane reports vw:0 so every probe false-passes), 768 as the
breakpoint that actually fails, and §6 for the small defects that shipped anyway.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 9: NEW skill — `cag-gate-integrity`

**Files:**
- Create: `skills/cag-gate-integrity.md`

**RED phase — satisfied by recorded production failures, not a synthetic scenario.**
`writing-skills` requires observing failure before writing the skill. That evidence
already exists in verbatim form, and it is stronger than a subagent run because these
are real edits to real pages. Enumerate all nine in the skill body:

| # | Reported | Reality | Checker bug |
|---|---|---|---|
| 1 | 7 tap-target ERRORs | 0 real | matched `li`/`pill`/`chip` in a selector *name*; read only `min-height` |
| 2 | 6 icon-baseline WARNs | 0 real | matched keywords inside **comments**; didn't know `place-items` is shorthand |
| 3 | body copy runs 84ch | already 70ch | approximated `ch` as `0.5em`; IBM Plex `0` is ~`0.6em` → +20% |
| 4 | 23 body dup crossovers | 0 real | whitelist missing reviews / counter strip / read-cards / doc badges |
| 5 | 8 contrast failures at 375px | 0 real | tested `display:none` on the element, not its ancestors |
| 6 | hero 432px, out of band | 396px, in band | measured `.adopt-hero` *with* padding, not `.hero-grid` |
| 7 | `absolute-hero-not-unwound` | 0 real | name-matched exemption; a price pill called `-p` slipped through |
| 8 | dup gate: "PASS — 0 pages" | examined **nothing** | zsh does not word-split `$SL`; 8 slugs arrived as 1 argument |
| 9 | seam parity: 0 sections | 15 sections | `grep '<section class="sec"'` — 6 of 8 pages don't use that class |

**Trade-off, stated plainly:** a synthetic pressure scenario would prove the skill
changes behaviour under time pressure; this evidence proves only that the failure is
real and frequent. If the skill is later ignored under pressure, add the scenario then.

- [ ] **Step 1: Write the skill**

```markdown
---
name: cag-gate-integrity
description: Use when any checker, scanner, audit, linter, or gate reports a defect on a CAG page — page_hardening_scan, final_page_audit, dup_content_audit, seam parity, Lighthouse, axe, or a probe you just wrote — and before editing any page in response. Also use when a gate reports PASS and you are about to trust it, when a whitelist or exemption was just widened, or when a report contradicts what you see on the page.
---

# SKILL: CAG Gate Integrity — Verify the Gate Before You Fix the Page

## Overview

**Nine checkers have cried wolf on this cluster.** Fixing what they reported would
have been wasted work *and* would have degraded correct code. Two of them reported
PASS while examining nothing at all.

**Core principle:** a gate's output is a *hypothesis about the page*, not a fact
about it. Confirm the defect exists before you edit, and confirm the gate examined
something before you believe a pass. **Violating the letter of this rule is
violating its spirit** — "I'll just make the small fix it suggests" is the failure.

## The Iron Law

```
NO PAGE EDIT FROM A GATE REPORT WITHOUT CONFIRMING THE DEFECT ON THE PAGE.
NO PASS BELIEVED WITHOUT CONFIRMING THE GATE'S OWN ITEM COUNT.
```

## The two directions of failure

**Direction 1 — the gate cried wolf (7 of 9 cases).** Editing the page degrades
correct code and buries the real bug.

**Direction 2 — the gate examined nothing (2 of 9 cases).** A green report on an
empty input set. This is the more dangerous one: nobody investigates a pass.

## Confirming a reported defect — cheapest tool first

| Claim | How to confirm | Never |
|---|---|---|
| a11y / contrast | Lighthouse or axe on the built page — it agreed with the code, not the scanner (100/100/100) | trust a regex sweep alone |
| "this element is interactive" | grep the built HTML inside that component for `<a ` / `<button` | infer from a class name |
| any measurement (px, `ch`, ratio) | measure in a real viewport via **Playwright** | compute from a formula; `0.5em` over-reports `ch` by ~20% |
| "the component is styled wrong" | `getComputedStyle` on the real element | read the CSS and reason about it |
| a size against a spec band | measure **the element the spec names**, excluding padding it doesn't include | measure the wrapper |
| a duplicate-content hit | open both pages at the reported offset | trust the shingle report |

**Open the flagged rule and quote it before editing.** If you cannot quote the exact
line that is wrong, you have not confirmed anything.

## Confirming a PASS — read the gate's own item count

Every CAG gate prints what it examined. **Read that number first.**

```
"PASS — no cross-page duplicate runs ≥12 words in 0 pages."   ← 0 pages. Not a pass.
"seam-parity — 0 pages matched"                                ← not a pass.
"scan — 12 source files, 0 built pages"                        ← ran astro build?
```

**The zsh trap, verbatim:**

```bash
SL="slug-a slug-b slug-c"
python3 scripts/dup_content_audit.py $SL     # zsh does NOT word-split → ONE argument
```

All eight slugs arrived as a single argument, matched no page, and the gate reported
PASS having compared nothing. **zsh does not word-split unquoted parameter
expansions.** Pass slugs literally, or use `${=SL}`.

## After widening any whitelist or exemption: prove the gate is not blinded

Inject the real defect back in, confirm FAIL, remove it, confirm PASS.

```bash
# 1. inject a deliberately duplicated sentence into real body prose → expect FAIL
# 2. remove it → expect PASS
# 3. git diff --stat <file>  → expect EMPTY
```

Done for the dup gate on 2026-07-26 and for `absolute-hero-not-unwound` on
2026-07-28 (by re-injecting the real `.pofig{position:absolute;width:44%}` bug and
confirming it still WARNs). Repeat after **every** whitelist edit.

## A gate you write is a gate that lies

Two of the nine were probes written in the same session that reported them. Before
trusting your own probe: skip elements where `!el.offsetParent` or the rect is
zero-sized (ancestors can be `display:none`), and measure the element the spec
names, not its padded wrapper.

## Red Flags — STOP

- "The scanner says 7 tap targets fail, let me fix them" → confirm one first
- "It reported PASS, moving on" → what was the item count?
- "I'll widen the whitelist to make it pass" → prove it still catches the real bug
- "My probe says 84ch" → did you measure a real `ch` or multiply by 0.5?
- "The gate is clean so the page is clean" → a clean scan proved nothing on adoption-cost
- "Close enough, I'll just make the change it suggests"
- "I wrote this check, it's fine"

**All of these mean: confirm on the page, then act.**

## Rationalizations

| Excuse | Reality |
|---|---|
| "The scanner is usually right" | 7 of 9 reports on this cluster were wrong. |
| "Confirming takes longer than fixing" | The 84ch report scoped a cluster-wide reflow that turned out to be a 4-line CSS change. |
| "It's only a WARN, harmless to fix" | Fixing a false WARN degrades correct code and hides the real defect. |
| "It said PASS, that's the good outcome" | Two gates passed on zero pages. A pass is a claim about an input set. |
| "I only widened the whitelist a little" | Stems must be anchored mid-phrase; the shingle window slides. Three iterations lost to this. |
| "The page looks fine to me" | Browser pane reports vw:0 — nothing painted. Measure in Playwright. |
| "I wrote the probe, I know it's right" | Two of the nine were mine, in the session that reported them. |

## Quick Reference

1. Gate reports a defect → open the flagged rule → **quote the wrong line** → confirm on the built page → then edit.
2. Gate reports a pass → **read the item count** → if 0 or 1 when you passed many, the run proved nothing.
3. Whitelist or exemption widened → **re-inject the real defect** → FAIL → remove → PASS → `git diff` empty.
4. Measurement claim → **Playwright**, real viewport, the element the spec names.
5. Wrote your own probe → check `offsetParent`, zero-rects, and padding.

## Real-World Impact

Nine false or empty reports across two sessions (2026-07-26, 2026-07-28,
2026-07-29). One collapsed a cluster-wide reflow into 4 lines of CSS. One would
have painted a black rectangle over eight infographics. Two reported PASS on zero
pages. Full records: `docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md`
§1–2, `docs/superpowers/sessions/2026-07-28-adoption-cost-harden-lessons.md` §4–5.
```

- [ ] **Step 2: Validate frontmatter and register**

```bash
python3 -c "
t=open('skills/cag-gate-integrity.md').read()
fm=t[3:t.find('\n---',3)]
assert 'name: cag-gate-integrity' in fm, 'name'
assert len(fm) < 1024, f'{len(fm)} chars > 1024'
assert 'Use when' in fm, 'description must start with a trigger'
print('frontmatter OK', len(fm), 'chars ·', t.count(chr(10)), 'lines')
"
python3 scripts/register_skills.py --copy
ls .claude/skills/cag-gate-integrity/SKILL.md
```

Expected: frontmatter OK, and `.claude/skills/cag-gate-integrity/SKILL.md` exists.

- [ ] **Step 3: GREEN check — the skill must answer all nine cases**

```bash
python3 -c "
t=open('skills/cag-gate-integrity.md').read().lower()
for k in ['tap-target','icon-baseline','0.5em','whitelist','offsetparent','padding',
          'absolute-hero','word-split','section class']:
    assert k in t, k
print('all 9 recorded failures addressed')
"
```

- [ ] **Step 4: Commit**

```bash
git add skills/cag-gate-integrity.md .claude/skills/cag-gate-integrity/
git commit -m "feat(skills): add cag-gate-integrity — verify the gate before you fix the page

RED baseline is 9 recorded production failures, not a synthetic scenario: 7
checkers reported defects that did not exist and 2 reported PASS having examined
zero pages. Enumerated in the skill with the checker bug behind each.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 10: Header-style selection layer in `framework-heading-hierarchy`

**Files:**
- Modify: `skills/framework-heading-hierarchy.md` (insert a section before `## The No-Skip Law` at line 128; extend `## Rules` at line 220)

The skill already covers the 6-level keyword map, the No-Skip Law, ≥5 H5 / ≥5 H6, and
the outline-first gate. It has **no concept of header *style*** and does not require a
reason for the choice.

- [ ] **Step 1: Insert the style-selection section**

```markdown
---

## Header Style Selection (added 2026-07-29)

The 6-level map above decides **what keyword** each heading carries. This section
decides **how it is phrased** — and the choice must be justified out loud at the
outline gate, grounded in that page's real query set, never in taste.

### The three styles

**Style 1 — Pure Conversational.** Natural language, reader curiosity, no forced
keyword. *"What Is It Really Like to Live with a Congo African Grey?"*
Highest engagement, weakest keyword signal.

**Style 2 — Conversational Hybrid (keyword + entity).** Question or benefit phrasing
wrapped around a target keyword and a named entity.
*"How to Choose the Best Congo African Grey Cage Setup"* ·
*"Safe Foods vs. Toxic Foods for Psittacus erithacus"*
Balanced; best for informational depth.

**Style 3 — Recommended Hybrid (direct-answer / snippet-targeted).** Question plus a
parenthetical or colon that states the answer scope, so the section is extractable.
*"What Do Congo African Greys Eat? (Nutrition & Safe Foods)"*
Strongest for Featured Snippets and AI Overviews; can read repetitive if every H2
uses it, so alternate with Style 2 inside a page.

### Register variants (choose the register, not a fourth style)

| Register | Example | Best for | Cost |
|---|---|---|---|
| **FAQ question-based** | "How Long Do Congo African Greys Live in Captivity?" | direct answers, AIO + Featured Snippets | monotonous if overused |
| **Quora-style** | "Why Is My African Grey Pulling Out Its Chest Feathers All of a Sudden?" | long-tail behaviour/problem posts | too long to scan |
| **Reddit-style** | "Is a Congo Grey Actually Worth the Hassle for a Beginner?" | community/subjective/review roundups, Reddit-modifier pages | weak explicit keyword |

### Page-type → default style

| Page type | Default | Why |
|---|---|---|
| For-sale / buy (transactional) | **Style 3**, ~30% Style 2 | Buyer queries are decision questions; the parenthetical carries the commercial modifier without stuffing the H2 |
| Comparison | **Style 3** with both entities named | The query *is* the comparison; both entities must appear for passage-level ranking |
| Care / health / informational | **Style 2** | Long-tail depth queries; entity density beats snippet framing over 20+ sections |
| Bird listing `/available/` | **FAQ question** register on Style 2 | Buyers ask about one bird — name + attribute + question |
| Reddit-modifier | **Reddit-style** register, deliberately | The page's whole promise is "what owners actually say" |
| Blog | **Style 2** with a Quora-register H1 | Curiosity opener, keyword body |
| Location | **Style 2** with the geo modifier | The state/city IS the differentiator |
| Legal / privacy | Plain declarative | No search intent to serve; clarity only |

### The justification requirement (binding)

Every H1–H6 outline presented at the Sprint 1 gate MUST carry a one-line style
declaration and a reason grounded in real data — the page's GSC/query set, the SERP
snapshot, PAA demand, or a competitor gap. **Never taste.**

```
Header style: Style 3 (Recommended Hybrid), FAQ register on H4–H6.
Why: price intent beats adoption intent 5:1 in this page's own query set, and 6 of
the top 10 SERP results are question-led — so a direct-answer H2 competes for the
snippet the informational results currently hold.
Trade-off: Style 3 on every H2 reads repetitive; H3s alternate to Style 2.
```

An outline submitted without the style line and its reason is **incomplete** and does
not pass the gate. Sentence-case is still a defect — Title Case applies to every
heading regardless of style; only FAQ `<summary>` text stays conversational.
```

- [ ] **Step 2: Extend the `## Rules` list**

Append as rules 10 and 11:

```markdown
10. **Header style must be declared and justified** at the outline gate — one of
    Style 1 / 2 / 3 plus register, with a data-grounded reason and a named trade-off
    (see §Header Style Selection). No style line = incomplete outline.
11. **Style follows page type by default** — Style 3 for transactional and
    comparison, Style 2 for informational/care/location/blog, Reddit register for
    Reddit-modifier pages. Deviating is allowed; deviating silently is not.
```

- [ ] **Step 3: Verify and register**

```bash
python3 -c "
t=open('skills/framework-heading-hierarchy.md').read()
for s in ['Header Style Selection','Style 3','Quora-style','justification requirement',
          'Page-type → default style','Trade-off']: assert s in t, s
i,j=t.find('Header Style Selection'),t.find('The No-Skip Law')
assert 0 < i < j, 'style section must precede the No-Skip Law'
print('OK')
"
python3 scripts/register_skills.py --copy
```

Expected: `OK`.

- [ ] **Step 4: Commit**

```bash
git add skills/framework-heading-hierarchy.md .claude/skills/framework-heading-hierarchy/
git commit -m "feat(headings): add header-style selection + mandatory justification

Three styles (Pure Conversational / Conversational Hybrid / Recommended Hybrid),
three registers (FAQ / Quora / Reddit), a page-type routing table, and a binding
requirement that every outline declares its style with a data-grounded why and a
named trade-off. Attaches to the existing Sprint 1 outline gate.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 11: Inject the header-style rule into all 68 agents

**Files:**
- Create: `scripts/add_header_style_rule.py`

A CLAUDE.md-only rule is 0/68 in the agents (`feedback_rules_need_injectors`). The
marker must match the line the existing injectors target — verify before writing.

- [ ] **Step 1: Confirm the anchor the existing injectors use**

```bash
grep -n "Golden Rule" .claude/agents/cag-seo-content-writer.md | head -3
grep -n "MARKER\|marker\|anchor" scripts/add_title_case_rule.py | head -10
```

Expected: a `## Golden Rule` heading in the agent, and the injector's marker constant.
**Match it exactly** — a marker that doesn't match silently injects into 0 files, which
is the `cag-gate-integrity` empty-input failure applied to an injector.

- [ ] **Step 2: Write the injector, modelled on `add_title_case_rule.py`**

```python
#!/usr/bin/env python3
"""Idempotently inject the Header-Style Declaration rule into every agent's
## Golden Rule block. Re-run after adding any agent.

Usage: python3 scripts/add_header_style_rule.py [--dry-run]"""
import sys, glob

RULE = (
    "> **Header Style Declaration (ALWAYS):** every H1–H6 outline you present must "
    "declare its header style — Style 1 Pure Conversational / Style 2 Conversational "
    "Hybrid / Style 3 Recommended Hybrid — plus its register (FAQ / Quora / Reddit), "
    "with a reason grounded in that page's real query set, SERP snapshot, PAA demand "
    "or a competitor gap (never taste) and a named trade-off. Defaults by page type "
    "live in `skills/framework-heading-hierarchy.md` §Header Style Selection. An "
    "outline with no style line does not pass the gate."
)
MARK = "Header Style Declaration"
DRY = "--dry-run" in sys.argv


def main():
    files = sorted(glob.glob(".claude/agents/*.md"))
    changed = skipped = nogolden = 0
    for f in files:
        t = open(f, encoding="utf-8").read()
        if MARK in t:
            skipped += 1
            continue
        i = t.find("## Golden Rule")
        if i == -1:
            print(f"  NO GOLDEN RULE BLOCK: {f}")
            nogolden += 1
            continue
        j = t.find("\n", i) + 1
        t = t[:j] + "\n" + RULE + "\n" + t[j:]
        if not DRY:
            open(f, "w", encoding="utf-8").write(t)
        changed += 1
    print(f"{len(files)} agents examined · {changed} injected · {skipped} already had it "
          f"· {nogolden} missing a Golden Rule block")
    if len(files) == 0:
        print("0 agents examined — THIS IS NOT A PASS. Check the glob.")
        return 1
    return 1 if nogolden else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 3: Dry-run, then apply**

Run: `python3 scripts/add_header_style_rule.py --dry-run`
Expected: `68 agents examined · 68 injected · 0 already had it · 0 missing a Golden Rule block`

If `nogolden > 0`, fix the marker before applying — do not inject into 67 and call it done.

Run: `python3 scripts/add_header_style_rule.py`
Expected: same counts, files written.

- [ ] **Step 4: Verify idempotence and coverage**

```bash
python3 scripts/add_header_style_rule.py          # expect 0 injected · 68 already had it
grep -lc "Header Style Declaration" .claude/agents/*.md | wc -l   # expect 68
```

- [ ] **Step 5: Commit**

```bash
git add scripts/add_header_style_rule.py .claude/agents/
git commit -m "feat(agents): inject the Header Style Declaration rule into all 68 Golden Rules

Per feedback_rules_need_injectors: a CLAUDE.md-only rule is 0/68 in the agents.
Injector reports its own examined count and refuses to call an empty glob a pass.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 12: Reddit Thread Sourcing Protocol + Thread Ledger

**Files:**
- Modify: `skills/reddit-strategy.md` (insert before `## Quick Reference` at line 63)
- Create: `data/reddit-thread-ledger.json`

`reddit-strategy` is a page-*building* playbook; `research-recency` supplies the fetch
ladder and engagement-ranked `last30days`. Neither has a protocol for **choosing** a
thread. Meanwhile 8 real threads are already cited across the for-sale pages — and
**5 links are bare subreddit roots** (`r/parrots/`, `r/AfricanGrey/`) with no
evidentiary value.

- [ ] **Step 1: Seed the ledger with the threads already spent**

```json
{
  "_meta": {
    "description": "Thread Diversity Ledger — which Reddit thread is cited on which CAG page. Same discipline as the Anchor Diversity Ledger: no two sibling pages lean on the same thread. Seeded 2026-07-29 by grepping src/pages/*/index.astro.",
    "last_updated": "2026-07-29",
    "rule": "Before citing a thread, check it here. A thread already spent on a sibling needs a different thread or an explicitly different angle on the same one."
  },
  "threads": [
    { "url": "https://www.reddit.com/r/parrots/comments/1njxqge/african_greys_vs_amazons/", "subreddit": "r/parrots", "topic": "grey vs amazon temperament", "pages": ["african-grey-vs-amazon-parrot"], "verified": "2026-07" },
    { "url": "https://www.reddit.com/r/parrots/comments/n8cie1/a_african_grey_costs_around_1000/", "subreddit": "r/parrots", "topic": "price expectations vs reality", "pages": ["african-grey-parrot-adoption-cost"], "verified": "2026-07" },
    { "url": "https://www.reddit.com/r/parrots/comments/1nno8fd/how_to_know_a_breeder_is_ethicalsigns_to_avoid/", "subreddit": "r/parrots", "topic": "ethical breeder signals", "pages": ["how-to-avoid-african-grey-parrot-scams"], "verified": "2026-07" },
    { "url": "https://www.reddit.com/r/parrots/comments/133zdo2/rescue_african_grey_price/", "subreddit": "r/parrots", "topic": "rescue vs breeder pricing", "pages": ["african-grey-parrot-adoption-cost"], "verified": "2026-07" },
    { "url": "https://www.reddit.com/r/AfricanGrey/comments/ipl261/what_age_did_you_buy_your_bird/", "subreddit": "r/AfricanGrey", "topic": "purchase age / weaning", "pages": ["baby-african-grey-parrot-for-sale"], "verified": "2026-07" },
    { "url": "https://www.reddit.com/r/AfricanGrey/comments/1asvyt3/please_can_someone_tell_me_a_legitimate_website/", "subreddit": "r/AfricanGrey", "topic": "finding a legitimate seller", "pages": ["how-to-avoid-african-grey-parrot-scams"], "verified": "2026-07" }
  ],
  "bare_subreddit_links_to_replace": [
    { "url": "https://www.reddit.com/r/parrots/", "count": 3, "note": "subreddit root, not a thread — no evidentiary value. Replace with a specific thread or drop." },
    { "url": "https://www.reddit.com/r/AfricanGrey/", "count": 2, "note": "same" }
  ]
}
```

- [ ] **Step 2: Insert the protocol into the skill**

```markdown
## Thread Sourcing Protocol (added 2026-07-29)

Applies to **every** page that cites Reddit — not just Reddit-modifier pages. Eight
threads are already cited across the for-sale cluster; five links are bare subreddit
roots with no evidentiary value. This protocol replaces "find a thread that looks
relevant."

### Step A — derive queries from the page, not from the topic

3–5 queries from **that page's own** intent, primary keyword and PAA set. The
adoption-cost page's real query set was price-intent 5:1 over adoption-intent — a
thread about rehoming would have been off-intent even though it is about adoption.

### Step B — search through the escalation ladder

Use `skills/research-recency.md`: Firecrawl → WebFetch with a UA retry → **headless
browser (Playwright)** → `/last30days`. Reddit blocks curl/Firecrawl, so in practice
the browser or `last30days` does the work. `last30days` ranks by real engagement,
which is exactly the signal this protocol needs. **Never fabricate a thread, a quote
or a vote count.**

### Step C — score the candidates

| Signal | Weight | Read |
|---|---|---|
| Subreddit authority | high | r/parrots and r/AfricanGrey rank position-1 on our decision queries; a 200-member sub does not |
| Upvotes | high | absolute score on the thread |
| Comment count | **highest** | a 12-comment thread with owner detail beats a 400-upvote photo post — we quote comments, not titles |
| On-intent fit | gate | must answer the query the *page* targets, not the topic generally |
| Recency | medium | older is fine for stable facts (lifespan, price floors); recent matters for market claims |
| Ethics | **veto** | never link threads promoting wild-caught birds, undocumented sales or scam marketplaces |

Keep the top **2–4**. A page with one thread is thin; a page with eight is a link farm.

### Step D — verify by opening it

Open each surviving thread in the browser and confirm: it exists, it is not deleted
or locked, and the quote you intend to use is actually in it. Quotes are ≤15 words,
attributed as an owner's claim, and linked. The `⚠ CITE OR DROP` rule holds — an
anonymous Reddit statistic is quoted **as a claim** or dropped, never printed as fact.

### Step E — log it in the Thread Diversity Ledger

Record URL, subreddit, topic, page and verification month in
`data/reddit-thread-ledger.json`. **Check the ledger before citing.** A thread already
spent on a sibling needs either a different thread or an explicitly different angle —
the same discipline as the Anchor Diversity Ledger, which caught two collisions on the
adoption-cost build that eyeballing would have shipped.

### Standing rules

- **Never link a bare subreddit root.** `r/parrots/` is not evidence. Link the thread.
- **A thread is evidence, not filler.** If you cannot say what it proves for this page, drop it.
- Script the ledger check; do not read it.
```

- [ ] **Step 3: Validate the JSON and register**

```bash
python3 -c "
import json; d=json.load(open('data/reddit-thread-ledger.json'))
assert len(d['threads'])==6, len(d['threads'])
print('ledger OK —', len(d['threads']), 'threads,', len(d['bare_subreddit_links_to_replace']), 'bare roots flagged')
"
python3 -c "
t=open('skills/reddit-strategy.md').read()
for s in ['Thread Sourcing Protocol','Comment count','Thread Diversity Ledger','bare subreddit root']: assert s in t, s
print('skill OK')
"
python3 scripts/register_skills.py --copy
```

Expected: `ledger OK — 6 threads, 2 bare roots flagged` then `skill OK`.

- [ ] **Step 4: Commit**

```bash
git add skills/reddit-strategy.md data/reddit-thread-ledger.json .claude/skills/reddit-strategy/
git commit -m "feat(reddit): add Thread Sourcing Protocol + Thread Diversity Ledger

Scores candidate threads on subreddit authority, upvotes and comment count (the
highest weight — we quote comments, not titles), gates on page-intent fit, vetoes
on ethics, and logs every citation so no two siblings lean on the same thread.

Seeds the ledger with the 6 threads already cited and flags the 5 bare subreddit
root links that carry no evidentiary value.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 13: Rewrite `WORKFLOW.md` to the live 7-sprint model

**Files:**
- Modify: `docs/reference/WORKFLOW.md` (Sprint 3/4/5 sections, ~lines 326–478; plus the decision tree at 527)

**The defect, measured 2026-07-29:** WORKFLOW.md contains **zero** references to
`page_hardening_scan.py`, `cag-page-hardening`, `dup_content_audit.py`,
`final_page_audit.py`, `cag-final-page-pass`, or Title Case. Sprint 4 still routes to
`manual-auditor-check` + `scripts/interior_29_audit.py`, which CLAUDE.md says is
**superseded**. And the 7-sprint model with **Harden as its own sprint** lives in memory
and in the master brief §17 but not here — so the master workflow currently encodes the
exact failure that model was written to prevent.

- [ ] **Step 1: Insert a Harden sprint between the AEO/GEO layer and the technical batch**

```markdown
## Sprint 3 — Harden (RENDER correctness)
*Runs on the BUILT page, before any final audit. Never a sub-bullet of Final —
the moment Harden is a bullet, it is the bullet that gets skipped.*

**REQUIRED SKILL:** `cag-page-hardening` (v2.0) · **REQUIRED FIRST:** `cag-gate-integrity`

```
0. npx astro build                      ← nothing below works on a stale dist/
1. python3 scripts/page_hardening_scan.py <slug>
   → 21 static checks. ERROR = shipped-broken. WARN = eyeball it.
   → §1k markup-css-drift  · §1l component colour specificity
2. python3 scripts/seam_parity.py <slug>
   → one seam per section, one seamless hero allowed
   → NEVER grep '<section class="sec"' — 6 of 8 for-sale pages don't use it
3. Runtime probes in PLAYWRIGHT at 375 / 768 / 1280  ← 768 is the one that fails
   → the Browser pane reports vw:0; every probe false-passes there
   → overflow · full-page contrast · real-ch line length · component sizing
4. python3 scripts/dup_content_audit.py <slug> [<slug>...]
   python3 scripts/dup_content_audit.py --headers <slug> [<slug>...]
   → pass slugs LITERALLY; zsh does not word-split $VAR
```

### Sprint 3 Gate
- [ ] `page_hardening_scan` → 0 ERROR; every WARN triaged REAL / DEAD-CODE / FALSE-POSITIVE
- [ ] **Every finding confirmed on the page before any edit** (`cag-gate-integrity`)
- [ ] **Every gate's own item count read** — a PASS over 0 pages is not a pass
- [ ] `seam_parity` PASS
- [ ] Runtime probes clean at 375 / 768 / 1280, measured in Playwright
- [ ] Dup gate 0 body + 0 header crossovers vs ALL siblings
- [ ] Every printed figure traced to `financial-entities.json` / `price-matrix.json` — no typed literals

---

## Sprint 4 — Final (structure, schema, SEO, voice)

**REQUIRED SKILL:** `cag-final-page-pass` — THE final gate for EVERY page type.

```
1. npx astro build
2. python3 scripts/final_page_audit.py [--birds]
   → page-type-aware, nested-slug aware. Supersedes interior_29_audit.py.
   → headings (all six levels, ≥5 H5 AND ≥5 H6, no skips, Title Case)
   → schema · meta · image SEO · a11y traps · links · phone · compliance copy
3. cag-keyword-verifier        → 85–105 distribution, no over-stuffing
4. cag-meta-description-agent  → extended 3-part for-sale meta (≤280 title)
5. anti-ai-writing             → AI-tell sweep on the final prose
6. cag-canonical-fixer         ← CRITICAL, NEVER SKIP: relative canonicals = zero rankings
7. cag-accessibility-fixer · cag-performance-fixer · cag-footer-standardizer
8. cag-google-map-agent        [location pages only]
```

### Sprint 4 Gate
- [ ] One PASS / PASS-WITH-WARNINGS verdict from `final_page_audit.py`; every ✗ triaged
- [ ] Lighthouse Performance ≥90 · Accessibility ≥90 — **median of ≥5 runs on any CLS/perf claim** (CLS is bimodal on this site; one run has already caused a confident wrong attribution)
- [ ] All canonicals absolute · footer `cag-footer-v1` · form passes ARIA
- [ ] Title Case on every H1–H6; FAQ `<summary>` stays sentence case
```

- [ ] **Step 2: Renumber the existing Sprint 5 (Deploy) → Sprint 5 Ship, and add Sprint 6 Bank**

```markdown
## Sprint 6 — Bank
*The step that makes the next page cheaper. Skipping it is why three 2026-07-28
lessons never reached the skill that enforces them.*

```
1. session-closer skill        → fill the brief's What's Next
2. Write the lessons doc       → docs/superpowers/sessions/YYYY-MM-DD-<page>-lessons.md
3. BACK-PROPAGATE each lesson into the artifact that ENFORCES it:
     a render defect      → a check in scripts/page_hardening_scan.py + a RED test
     a gate that lied     → skills/cag-gate-integrity.md
     a rule for everyone  → CLAUDE.md + a scripts/add_<rule>_rule.py injector (0/68 without one)
     a component decision → sessions/2026-07-19-for-sale-component-map.md ledger
     an anchor spent      → the Anchor Diversity Ledger
     a thread cited       → data/reddit-thread-ledger.json
4. Sweep siblings for the same defect  (the infographic-crop bug hit 4 other live pages)
5. Memory: write/update the relevant memory file + its MEMORY.md pointer
```

### Sprint 6 Gate
- [ ] Every lesson in the doc maps to a named enforcing artifact, or is explicitly logged as backlog
- [ ] Siblings swept for the same defect class
- [ ] Any new rule has an injector and reports 68/68
```

- [ ] **Step 3: Retire the stale routing**

```bash
grep -n "interior_29_audit\|manual-auditor-check" docs/reference/WORKFLOW.md
```

Replace each hit with `cag-final-page-pass` / `scripts/final_page_audit.py`, keeping the
note that `manual-auditor-check` remains valid only for interior pages as a subjective
companion checklist.

- [ ] **Step 4: Verify the rewrite actually landed**

```bash
python3 - <<'PY'
t = open("docs/reference/WORKFLOW.md").read()
must = ["page_hardening_scan", "cag-page-hardening", "cag-gate-integrity", "seam_parity",
        "dup_content_audit", "final_page_audit", "cag-final-page-pass",
        "Sprint 3 — Harden", "Sprint 6 — Bank", "Title Case", "median of ≥5 runs"]
missing = [m for m in must if m not in t]
print("MISSING:", missing or "none")
assert not missing
print("interior_29_audit refs:", t.count("interior_29_audit"), "(expect 0)")
assert t.count("interior_29_audit") == 0
PY
```

Expected: `MISSING: none` and `interior_29_audit refs: 0`.

- [ ] **Step 5: Commit**

```bash
git add docs/reference/WORKFLOW.md
git commit -m "docs(workflow): rewrite to the live 7-sprint model; retire interior_29_audit routing

WORKFLOW.md had zero references to page_hardening_scan, cag-page-hardening,
dup_content_audit, final_page_audit, cag-final-page-pass or Title Case, and Sprint 4
still routed to the superseded manual-auditor-check. The 7-sprint model with Harden
as its OWN sprint existed only in memory and the master brief — so the master
workflow encoded the exact skip it was written to prevent.

Adds Sprint 3 Harden, rewrites Sprint 4 Final, adds Sprint 6 Bank with mandatory
lesson back-propagation.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Task 14: Register everything in CLAUDE.md, verify, ship

**Files:**
- Modify: `CLAUDE.md` (Non-Negotiable Rules; Reference Docs; Scripts)

- [ ] **Step 1: Add the two new non-negotiable rules**

Append to `## Non-Negotiable Rules`:

```markdown
- **Verify the gate before you fix the page (ALWAYS) — applies to every agent, skill, and gate** — A gate's output is a *hypothesis about the page*, not a fact about it. **Nine checkers have cried wolf on this site** (seven reported defects that did not exist; two reported PASS having examined zero pages). Before editing any page in response to a scanner/audit/probe: open the flagged rule, **quote the wrong line**, and confirm the defect on the built page. Before believing a PASS: **read the gate's own item count** — `PASS … in 0 pages` is not a pass (zsh does not word-split `$VAR`; pass slugs literally or use `${=SL}`). After widening any whitelist or exemption, re-inject the real defect, confirm FAIL, remove it, confirm PASS. Measure in **Playwright**, never from a formula — the Browser pane reports `vw:0` so every probe false-passes, and `0.5em` over-reports a `ch` by ~20%. Canonical spec: `skills/cag-gate-integrity.md`.
- **Restate the brief before you build (ALWAYS)** — For any prompt, short or long, first restate it as a scoped brief (goal · scope · gates · what "done" means · what is explicitly out of scope) and improve the prompt where it is ambiguous, so the breeder can correct the reading before work is spent on it. Blocking questions stay reserved for cases where proceeding under any assumption would be unsafe or wasted (Clarification Checkpoint).
```

- [ ] **Step 2: Register the new skills and scripts**

Under Reference Docs / Skills:

```markdown
- `skills/cag-gate-integrity.md` — **VERIFY THE GATE BEFORE YOU FIX THE PAGE.** Run at the FIRST report from any checker, and before trusting any PASS. Enumerates the 9 recorded false/empty reports with the checker bug behind each; carries the zsh word-split trap, the whitelist-blinding proof, the `offsetParent` and padding traps in probes you write yourself, and a rationalization table. Read before `cag-page-hardening` and `cag-final-page-pass`.
```

Under Scripts:

```markdown
- `scripts/seam_parity.py` — the ONE correct seam↔section probe (one seam per section, one seamless hero allowed). Replaces the published `grep -c '<section class="sec"'`, which matched only 2 of the 8 built for-sale pages and compared seams against zero sections. Prints its own examined count and refuses to call a 0-page run a pass.
- `scripts/add_header_style_rule.py` — idempotent injection of the **Header Style Declaration** rule into all 68 agent Golden Rules. Re-run after adding any agent.
```

Also update the `scripts/page_hardening_scan.py` entry to list `markup-css-drift` and
`component-color-loses-to-descendant`, and the `cag-page-hardening` entry to say v2.0.

- [ ] **Step 3: Full verification sweep**

```bash
python3 -m pytest tests/ -q
python3 scripts/verify_model_tiers.sh 2>/dev/null || bash scripts/verify_model_tiers.sh
python3 scripts/register_skills.py --copy
npx astro build
python3 scripts/page_hardening_scan.py 2>&1 | tail -8
python3 scripts/seam_parity.py 2>&1 | tail -4
bash scripts/health-sweep.sh
```

Expected: tests pass · 68/68 tier verify · skills mirrored · build succeeds · scanner and
seam probe both report a **non-zero examined count** · health sweep PASS. If any gate
reports 0 items examined, that run proved nothing — fix the invocation, per the rule this
session just added.

- [ ] **Step 4: Confirm no page files were changed**

This session is tooling and docs only. No page should have been edited:

```bash
git status --short src/pages/ public/
```

Expected: **empty**. If anything appears, it was an unauthorized page edit — revert it.

- [ ] **Step 5: Commit and push**

```bash
git add CLAUDE.md .claude/skills/
git commit -m "docs(claude-md): register cag-gate-integrity, seam_parity, header-style injector

Adds two non-negotiable rules: verify-the-gate-before-you-fix-the-page (9 recorded
false or empty reports) and restate-the-brief-before-you-build.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
git push origin main
```

- [ ] **Step 6: Confirm the deploy is a no-op for the live site**

Nothing in this session touches `src/pages/`, so Cloudflare will rebuild identical HTML.
Confirm the push landed and the branch is `main`:

```bash
git log --oneline -12
git branch --show-current   # must be main
git status --short           # must be clean
```

---

## Deferred to the next session (approved, not in scope here)

1. **GSC + GA4 MCP + `cag-analytics-live` skill.** Approach approved: official
   [googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)
   (`uvx`, since `pipx` is absent) + [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc),
   both local stdio in a project `.mcp.json`. **Blocked on the breeder:** GCP project +
   Admin/Data API enablement + OAuth consent + the GA4 property ID (only the measurement ID
   `G-MEWJ9GVC4T` is on disk). `cag-gsc-analytics.md` must lose its *"never calls external
   APIs"* line at the same time. Current GSC data is from **2026-04-27**.
2. **CLAUDE.md core/site split** — portable doctrine to `~/.claude/CLAUDE.md`, site facts
   stay local. CLAUDE.md is 423 lines / ~9,400 words loaded every turn.
3. **`cag-asset-proofing`** — open every dropped image; per-row median watermark fill;
   filenames and captions must describe contents; orphan diff; thumbnails come from photos.
4. **Routines** for the weekly/monthly/quarterly monitoring loops — only after the MCPs land,
   since a scheduled analytics agent has nothing to read before then.
5. **Page 9 `congo-african-grey-parrot-pair-for-sale` FAILS `final_page_audit.py`** — H4/H5/H6
   all zero, no org schema, no shipping line. It is an unbuilt stub and it is the next build.
6. Two ledger flags unconfirmed since 2026-07-19: the egg page's truth-forward hybrid and the
   no-page-level-sidebar rule are both *recommended, never explicitly approved*.
7. `.stars` is `#c9a227` (2.42:1) on congo + timneh — below even the 3:1 graphical floor. Two-page sweep.

---

## Self-Review

**Spec coverage.** Item 1 (model) → Task 1. Item 2 (system prompt) → deferred #2, with the
findings recorded in this plan's preamble. Item 3 (`--bare`) → documented, no action needed.
Item 4 (loops/routines) → deferred #4. Item 5 (harden skill) → Tasks 4–8. Item 6 (lessons →
skills) → Tasks 2–12 + Sprint 6 back-propagation in Task 13. Item 7 (Reddit) → Task 12.
Item 8 (GSC/GA4) → deferred #1. Item 9 (headers) → Tasks 10–11. Item 10 (workflow/ledger) →
Task 13 + Task 3 Step 5 + deferred #5–7.

**Placeholder scan.** No TBDs. Every code step carries complete, runnable code; every command
states its expected output; the seam-parity thresholds and the 8-page measurement table are
real numbers taken from disk on 2026-07-29.

**Type consistency.** `add(sev, check, f, line, msg, fix)` matches the scanner's existing
signature. Both new checks take `src_pairs` — the same `[(file, text)]` shape
`check_smooth_scroll` already receives — and are registered next to it in `main()`.
`seam_parity` exposes exactly the three names the tests import: `count_sections`,
`count_seams`, `verdict`. Check names are stable across scanner, tests and skill:
`markup-css-drift`, `markup-css-orphan`, `component-color-loses-to-descendant`.

**Known risk.** §1l is heuristic — it infers nesting from class co-occurrence in one file,
so it can over-report. It is therefore WARN-only, and Task 7 Step 4 requires tightening the
check rather than accepting noise. Per `cag-gate-integrity`, a gate nobody trusts is worse
than no gate.

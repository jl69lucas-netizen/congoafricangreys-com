# Contract for scripts/slim_golden_rule.py (2026-09-07): collapse the seven site-wide
# Golden Rule lines + tool-first lines + the OLD stop-and-ask Confidence Gate into one
# pointer; keep agent-specific lines; fix the Project Context; byte-idempotent.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import slim_golden_rule as S

BEFORE = """---
name: cag-fixture
---

## Golden Rule
> **Header Style Declaration (ALWAYS):** every H1–H6 outline you present must declare its header style.
> **Write-From-Outline, NEVER-From-Sibling (ALWAYS):** Do NOT open a sibling page.
> **Title Case Headings (ALWAYS):** Every H1–H6 uses AP-style Title Case.
> **Heading Hierarchy Outline Gate (ALWAYS):** Before writing or changing ANY page, first present the outline.
> **Link-First (ALWAYS):** anchors at the START.
> **Interior-Page Standard (ALWAYS):** This page type follows the homepage design + method.
> **Clarification Checkpoint (ALWAYS):** Below the ≥97% Confidence Gate, do NOT dead-stop the whole job.
> **First-Person Brand Voice (ALWAYS):** Write as the breeder.
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.
> **Confidence Gate:** Before writing or modifying any file in site/content/, confidence must be ≥97%. If uncertain: stop, state the uncertainty, ask. Never guess on live files.

---

## CAG Project Context
> **Site:** CongoAfricanGreys.com
> **Content root:** `site/content/` | **Sessions:** `sessions/`
> **Confidence Gate:** ≥97% before writing any site file

---

## Purpose
grep -r "x" /Users/apple/Downloads/CAG/src/pages/
"""


def test_site_wide_lines_collapse_to_pointer_and_specific_line_survives():
    out = S.slim(BEFORE)
    gr = out.split("## Golden Rule\n", 1)[1].split("\n---", 1)[0]
    quoted = [l for l in gr.split("\n") if l.startswith("> ")]
    assert quoted[0] == S.POINTER
    assert any(l.startswith("> **Interior-Page Standard") for l in quoted)
    assert len(quoted) == 2
    assert "Never guess on live files" not in out          # old stop-and-ask gate gone
    assert "Playwright CLI to solve problems first" not in out


def test_project_context_is_corrected():
    out = S.slim(BEFORE)
    assert S.CTX_ROOT_NEW in out and S.CTX_ROOT_OLD not in out
    assert "Never dead-stop." in out
    assert "/Users/apple/" not in out and 'grep -r "x" src/pages/' in out


def test_idempotent():
    once = S.slim(BEFORE)
    assert S.slim(once) == once
    assert once.count(S.POINTER) == 1


def test_file_without_golden_rule_is_untouched_except_paths():
    txt = "# Title\n\nplain\n"
    assert S.slim(txt) == txt

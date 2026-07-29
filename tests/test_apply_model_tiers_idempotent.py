# tests/test_apply_model_tiers_idempotent.py
#
# RED fixture for the whitespace drift in scripts/apply_model_tiers.py.
# patch() strips the EFFORT block with a regex that eats the newline on BOTH
# sides of it, then re-inserts the block wrapped in its own leading/trailing
# newlines — so every run leaks one extra blank line into the file. Measured
# 2026-07-29 on the real tree: 44 excess inserted lines across 42 of the 68
# files in .claude/agents/, plus the EFFORT block jumping above a Golden-Rule
# line in .claude/agents/cag-infographic-builder.md.
#
# The workaround recorded in memory (project_apply_model_tiers_drift) was
# "checkout to keep commits focused" — which stops working the moment a file
# needs a real change AND a whitespace revert in the same commit (the Opus 5
# flip, 90130c1, forced a manual model-line-only rewrite instead).
#
# Acceptance criterion: run patch() twice, second run is byte-identical.
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import apply_model_tiers as A


AGENT = """---
name: cag-fixture-agent
description: A fixture agent used only by this test.
tools: [Read, Write, Bash]
---

# CAG Fixture Agent

## Golden Rule
Never fabricate data.
"""

# The same agent as it looks AFTER one patch() run — the shape every real file
# in .claude/agents/ is already in on disk.
PATCHED = """---
name: cag-fixture-agent
description: A fixture agent used only by this test.
tools: [Read, Write, Bash]
model: claude-opus-5
effort: high
dynamic_workflow: false
---

<!-- EFFORT:START -->
> **Reasoning effort: HIGH.** Think through the key decisions and tradeoffs before producing output. Do not answer reflexively on non-trivial steps.
<!-- EFFORT:END -->

# CAG Fixture Agent

## Golden Rule
Never fabricate data.
"""


def _write(tmp_path, text, name="cag-fixture-agent.md"):
    f = tmp_path / name
    f.write_text(text)
    return f


def test_second_run_on_a_fixture_file_is_a_no_op(tmp_path):
    """THE acceptance criterion: patch() twice, byte-identical the second time."""
    f = _write(tmp_path, AGENT)

    f.write_text(A.patch(f.read_text(), "claude-opus-5", "high", False))
    once = f.read_text()

    f.write_text(A.patch(f.read_text(), "claude-opus-5", "high", False))
    assert f.read_text() == once


def test_third_run_is_also_a_no_op(tmp_path):
    """One extra blank line per run means the drift compounds, so check n=3."""
    f = _write(tmp_path, AGENT)
    for _ in range(2):
        f.write_text(A.patch(f.read_text(), "claude-opus-5", "max", False))
    twice = f.read_text()

    f.write_text(A.patch(f.read_text(), "claude-opus-5", "max", False))
    assert f.read_text() == twice


def test_medium_tier_second_run_is_a_no_op(tmp_path):
    """EFFORT_TEXT has no 'medium' key — the no-directive path through the same code."""
    f = _write(tmp_path, AGENT)

    f.write_text(A.patch(f.read_text(), "claude-opus-5", "medium", False))
    once = f.read_text()

    f.write_text(A.patch(f.read_text(), "claude-opus-5", "medium", False))
    assert f.read_text() == once


def test_already_patched_file_is_left_exactly_alone(tmp_path):
    """The 68 real agents are already in PATCHED shape; re-running must not touch them."""
    f = _write(tmp_path, PATCHED)

    assert A.patch(f.read_text(), "claude-opus-5", "high", False) == PATCHED


def test_effort_block_is_not_relocated_past_a_golden_rule_line(tmp_path):
    """cag-infographic-builder.md keeps a binding note ABOVE its EFFORT block."""
    original = PATCHED.replace(
        "<!-- EFFORT:START -->",
        "> **Uniform sizing (IMAGE-DESIGNS §1a — binding):** every in-body image ships in the same box.\n\n<!-- EFFORT:START -->",
    )
    f = _write(tmp_path, original)

    assert A.patch(f.read_text(), "claude-opus-5", "high", False) == original


def test_tier_flip_on_an_already_patched_file_settles_after_one_run(tmp_path):
    """The 90130c1 scenario: a real model/effort change on top of an existing block."""
    f = _write(tmp_path, PATCHED)

    f.write_text(A.patch(f.read_text(), "claude-opus-6", "max", True))
    once = f.read_text()

    f.write_text(A.patch(f.read_text(), "claude-opus-6", "max", True))
    assert f.read_text() == once
    assert once.count(A.EFFORT_START) == 1
    assert "model: claude-opus-6" in once
    assert "Reasoning effort: MAX" in once
    assert "Reasoning effort: HIGH" not in once


def test_first_run_still_injects_the_directive(tmp_path):
    """Guard the actual feature: a virgin agent file gains frontmatter + directive."""
    f = _write(tmp_path, AGENT)

    out = A.patch(f.read_text(), "claude-opus-5", "high", False)

    assert "model: claude-opus-5" in out
    assert "effort: high" in out
    assert "dynamic_workflow: false" in out
    assert A.EFFORT_START in out and A.EFFORT_END in out
    assert "Reasoning effort: HIGH" in out
    assert out.count(A.EFFORT_START) == 1

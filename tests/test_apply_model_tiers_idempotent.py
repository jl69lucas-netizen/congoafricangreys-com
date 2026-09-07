# tests/test_apply_model_tiers_idempotent.py
#
# Contract for scripts/apply_model_tiers.py after the 2026-09-07 Fable 5.1 adaptation:
#   * writes exactly `model:` + `effort:` (both native Claude Code frontmatter fields)
#   * removes `dynamic_workflow:` (not a recognized field) and the legacy
#     <!-- EFFORT:START/END --> prose block (the native field replaced it)
#   * a second run over any input is byte-identical (the original 2026-07-29 finding:
#     the old strip/re-insert leaked one blank line per run across 42 of 68 agents)
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import apply_model_tiers as A


VIRGIN = """---
name: cag-fixture-agent
description: A fixture agent used only by this test.
tools: [Read, Write, Bash]
---

# CAG Fixture Agent

## Golden Rule
Never fabricate data.
"""

# The shape every real agent was in before 2026-09-07.
LEGACY = """---
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

EXPECTED = """---
name: cag-fixture-agent
description: A fixture agent used only by this test.
tools: [Read, Write, Bash]
model: inherit
effort: high
---

# CAG Fixture Agent

## Golden Rule
Never fabricate data.
"""


def test_virgin_file_gains_model_and_effort_only():
    out = A.patch(VIRGIN, "inherit", "high")
    assert out == EXPECTED
    assert "dynamic_workflow" not in out and A.EFFORT_START not in out


def test_legacy_file_is_migrated_to_expected_shape():
    assert A.patch(LEGACY, "inherit", "high") == EXPECTED


def test_second_and_third_runs_are_byte_identical():
    once = A.patch(LEGACY, "inherit", "max")
    twice = A.patch(once, "inherit", "max")
    thrice = A.patch(twice, "inherit", "max")
    assert once == twice == thrice
    assert "effort: max" in once and once.count("effort:") == 1


def test_medium_tier_is_a_no_op_on_second_run():
    once = A.patch(VIRGIN, "inherit", "medium")
    assert A.patch(once, "inherit", "medium") == once


def test_already_migrated_file_is_left_exactly_alone():
    assert A.patch(EXPECTED, "inherit", "high") == EXPECTED


def test_hand_placed_note_above_legacy_block_survives_the_strip():
    """cag-infographic-builder.md kept a binding note ABOVE its EFFORT block."""
    note = "> **Uniform sizing (IMAGE-DESIGNS §1a — binding):** every in-body image ships in the same box.\n"
    original = LEGACY.replace("<!-- EFFORT:START -->", note + "\n<!-- EFFORT:START -->")
    out = A.patch(original, "inherit", "high")
    assert note.strip() in out
    assert A.EFFORT_START not in out
    assert A.patch(out, "inherit", "high") == out


def test_tier_flip_settles_after_one_run():
    once = A.patch(EXPECTED, "inherit", "xhigh")
    assert "effort: xhigh" in once
    assert A.patch(once, "inherit", "xhigh") == once


def test_invalid_effort_is_rejected():
    import pytest
    with pytest.raises(ValueError):
        A.patch(VIRGIN, "inherit", "ultra")

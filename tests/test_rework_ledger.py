# tests/test_rework_ledger.py
#
# The rework rate is the one number this whole system is judged on (spec §5:
# 24.8% baseline, under 15% at 90 days). If the classifier drifts, the metric
# moves without the work changing — so the classifier is pinned here.
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import rework_ledger as R


def test_classifies_the_canonical_rework_prefixes():
    for subject in [
        "fix(render): settlePage was hanging",
        "revert: bad merge",
        "fix: broken canonical",
        "docs: correct the CITES appendix",
        "restore the deleted footer",
        "chore: undo the palette change",
        "repair the sitemap",
        "patch(nav): rail offset",
        "style: regress guard",
    ]:
        assert R.is_rework(subject), subject


def test_does_not_classify_ordinary_work_as_rework():
    for subject in [
        "feat: add the timneh for-sale page",
        "test(render): NAV/anchors-resolve",
        "docs: session brief",
        "build: bump astro",
        "perf: preload the hero",
    ]:
        assert not R.is_rework(subject), subject


def test_prefix_match_is_anchored_not_substring():
    """`affix` and `prefixed` contain 'fix' and are not rework."""
    assert not R.is_rework("feat: add affix helper")
    assert not R.is_rework("refactor: prefixed ids")


def test_rate_is_rework_over_total():
    w = R.window("2026-05-01", "2026-07-31", ["fix: a", "feat: b", "feat: c", "revert: d"])
    assert w["total"] == 4
    assert w["rework"] == 2
    assert w["rate"] == 0.5


def test_an_empty_window_is_rate_zero_not_a_crash():
    w = R.window("2026-01-01", "2026-01-02", [])
    assert w == {"from": "2026-01-01", "to": "2026-01-02", "total": 0, "rework": 0, "rate": 0.0,
                 "by_domain": {}}


def test_domains_are_the_seven_harness_families_plus_three():
    w = R.window("2026-05-01", "2026-07-31", [
        "fix(img): srcset regen",
        "fix: mobile overflow on the hero",
        "fix: jump rail anchors",
        "fix: dead css rules",
        "fix: the gate lied",
        "fix: schema dateModified",
        "fix: heading title case",
        "fix: duplicate content crossover",
        "fix: contrast on the clay pill",
        "fix: typo in the voice copy",
    ])
    assert set(w["by_domain"]) == {"IMG", "LAYOUT", "NAV", "CSS", "GATE", "SCHEMA", "SEM",
                                   "DUP", "A11Y", "COPY"}
    assert w["by_domain"]["IMG"] == 1


def test_appending_a_window_replaces_one_with_the_same_bounds(tmp_path):
    """Re-running for the same window must correct the entry, not double it."""
    p = tmp_path / "rework-ledger.json"
    R.append_window(p, R.window("2026-05-01", "2026-07-31", ["fix: a"]))
    R.append_window(p, R.window("2026-05-01", "2026-07-31", ["fix: a", "feat: b"]))
    data = json.loads(p.read_text())
    assert len(data["windows"]) == 1
    assert data["windows"][0]["total"] == 2


def test_windows_stay_sorted_by_start_date(tmp_path):
    p = tmp_path / "rework-ledger.json"
    R.append_window(p, R.window("2026-06-01", "2026-06-30", ["fix: a"]))
    R.append_window(p, R.window("2026-05-01", "2026-05-31", ["feat: b"]))
    data = json.loads(p.read_text())
    assert [w["from"] for w in data["windows"]] == ["2026-05-01", "2026-06-01"]

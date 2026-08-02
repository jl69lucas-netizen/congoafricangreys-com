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
    w = R.window("2026-05-01", "2026-07-31", [
        # Subjects now arrive with the files they touched — that is what separates
        # page rework from harness self-repair. These are page commits, so the union
        # `rate` and `page_rate` agree, which is what this test is about.
        ("fix: a", ["src/pages/a.astro"]), ("feat: b", ["src/pages/a.astro"]),
        ("feat: c", ["src/pages/a.astro"]), ("revert: d", ["src/pages/a.astro"]),
    ])
    assert w["total"] == 4
    assert w["rework"] == 2
    assert w["rate"] == 0.5


def test_an_empty_window_is_rate_zero_not_a_crash():
    w = R.window("2026-01-01", "2026-01-02", [])
    assert w == {"from": "2026-01-01", "to": "2026-01-02", "total": 0, "rework": 0, "rate": 0.0,
                 "page_rework": 0, "page_rate": 0.0,
                 "harness_rework": 0, "harness_rate": 0.0,
                 "by_domain": {}}


def test_domains_are_the_seven_harness_families_plus_three():
    w = R.window("2026-05-01", "2026-07-31", [
        ("fix(img): srcset regen", ["src/pages/a.astro"]),
        ("fix: mobile overflow on the hero", ["src/pages/a.astro"]),
        ("fix: jump rail anchors", ["src/pages/a.astro"]),
        ("fix: dead css rules", ["src/pages/a.astro"]),
        ("fix: the gate lied", ["src/pages/a.astro"]),
        ("fix: schema dateModified", ["src/pages/a.astro"]),
        ("fix: heading title case", ["src/pages/a.astro"]),
        ("fix: duplicate content crossover", ["src/pages/a.astro"]),
        ("fix: contrast on the clay pill", ["src/pages/a.astro"]),
        ("fix: typo in the voice copy", ["src/pages/a.astro"]),
    ])
    assert set(w["by_domain"]) == {"IMG", "LAYOUT", "NAV", "CSS", "GATE", "SCHEMA", "SEM",
                                   "DUP", "A11Y", "COPY"}
    assert w["by_domain"]["IMG"] == 1


def test_appending_a_window_replaces_one_with_the_same_bounds(tmp_path):
    """Re-running for the same window must correct the entry, not double it."""
    p = tmp_path / "rework-ledger.json"
    R.append_window(p, R.window("2026-05-01", "2026-07-31", [("fix: a", ["src/pages/a.astro"])]))
    R.append_window(p, R.window("2026-05-01", "2026-07-31", [("fix: a", ["src/pages/a.astro"]), ("feat: b", ["src/pages/a.astro"])]))
    data = json.loads(p.read_text())
    assert len(data["windows"]) == 1
    assert data["windows"][0]["total"] == 2


def test_windows_stay_sorted_by_start_date(tmp_path):
    p = tmp_path / "rework-ledger.json"
    R.append_window(p, R.window("2026-06-01", "2026-06-30", [("fix: a", ["src/pages/a.astro"])]))
    R.append_window(p, R.window("2026-05-01", "2026-05-31", [("feat: b", ["src/pages/a.astro"])]))
    data = json.loads(p.read_text())
    assert [w["from"] for w in data["windows"]] == ["2026-05-01", "2026-06-01"]


def test_page_rework_and_harness_rework_are_split_by_the_files_a_commit_touches():
    """A checker fix and a page fix are both `fix(...)`; only one is page rework.

    Measured 2026-08-03: 36 of 74 rework commits in the 30-day window edited no page at
    all. Folding them into the headline makes the metric rise whenever the learning loop
    does the very thing it exists to do — charge an escaped defect to the harness.
    """
    commits = [
        ("fix(render): the checker lied", ["tests/render/checks/img.ts"]),
        ("fix(hero): mobile crop", ["src/pages/x/index.astro"]),
        ("feat(page): new section", ["src/pages/y/index.astro"]),
    ]
    w = R.window("2026-01-01", "2026-02-01", commits)
    assert w["total"] == 3
    assert w["rework"] == 2
    assert w["page_rework"] == 1 and w["page_rate"] == round(1 / 3, 4)
    assert w["harness_rework"] == 1 and w["harness_rate"] == round(1 / 3, 4)


def test_a_commit_touching_both_a_page_and_the_harness_counts_as_PAGE_rework():
    """Ambiguity resolves toward the page: it changed what a visitor loads."""
    w = R.window("2026-01-01", "2026-02-01",
                 [("fix(nav): rail + its check",
                   ["src/pages/a.astro", "tests/render/checks/nav.ts"])])
    assert w["page_rework"] == 1 and w["harness_rework"] == 0


def test_by_domain_counts_PAGE_rework_only():
    """The next-action list must point at pages, not at the harness fixing itself."""
    w = R.window("2026-01-01", "2026-02-01", [
        ("fix: mobile overflow on the hero", ["src/pages/a.astro"]),
        ("fix: mobile overflow in the checker", ["tests/render/checks/layout.ts"]),
    ])
    assert w["by_domain"]["LAYOUT"] == 1

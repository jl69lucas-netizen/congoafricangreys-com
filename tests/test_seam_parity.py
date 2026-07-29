# tests/test_seam_parity.py
#
# RED fixture for the broken seam-parity probe. The command published in
# docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md §5/§8
#   grep -c '<section class="sec"' src/pages/<slug>/index.astro
# returns 0 on 6 of 8 built for-sale pages, so "seams == sections" was compared
# against zero and silently told the reviewer nothing. Measured 2026-07-29:
#
#   page              seams  <section  diff        class="sec"?
#   eggs                 15        16     1        no  -> grep said 0
#   congo                15        15     0        no  -> grep said 0
#   timneh               18        18     0        no  -> grep said 0
#   hand-raised          18        19     1        no  -> grep said 0
#   health-guarantee     17        18     1        yes
#   dna-tested           18        19     1        no  -> grep said 0
#   baby                 21        22     1        no  -> grep said 0
#   adoption-cost        10        10     0        yes
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
    """The real defect: health-guarantee shipped 7 seams across 17 sections."""
    bad = ('<section class="hero"></section>'
           + '<div class="seam"></div><section id="x"><h2>H</h2></section>' * 7
           + '<section id="y"><h2>H</h2></section>' * 9)
    verdict, sections, seams = S.verdict(bad)
    assert (verdict, sections, seams) == ("FAIL", 17, 7)


def test_a_page_with_no_seams_at_all_is_NA_not_FAIL():
    """One-seam-per-section is a for-sale/comparison convention, not sitewide.

    A page with zero seams is not violating the idiom — it is not using it. Treating
    zero as FAIL reported 71 of 108 pages as broken (2026-07-29), which is a claim
    about the probe's scope, not about the pages.
    """
    none = '<section class="hero"></section><section id="x"><h2>H</h2></section>'
    assert S.verdict(none) == ("N/A", 2, 0)


def test_does_not_count_the_closing_tag():
    assert S.count_sections("<section></section>") == 1


def test_counts_the_sitewide_cag_seam_idiom_too():
    """Two idioms ship on this site and BOTH are seams.

    `class="seam"` is the for-sale cluster (291 uses); `class="cag-seam"` is the
    shared component used everywhere else (913 uses). Counting only the exact token
    `seam` read ZERO seams on 83 of 108 pages and reported them all as FAIL
    (2026-07-29) — my own probe, not the site.
    """
    assert S.count_seams('<div class="cag-seam"></div>') == 1
    assert S.count_seams('<div class="cag-seam"><img class="seam-logo"></div>') == 1
    mixed = '<div class="seam"></div><div class="cag-seam"></div>'
    assert S.count_seams(mixed) == 2


def test_seamless_is_not_a_seam():
    """`seamless` must not match — the substring trap that started all this."""
    assert S.count_seams('<div class="seamless"></div>') == 0

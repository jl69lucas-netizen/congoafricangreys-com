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
    """health-guarantee shipped 7 seams across 17 sections. diff > 1 must FAIL."""
    bad = '<section class="hero"></section>' + '<section id="x"><h2>H</h2></section>' * 5
    verdict, sections, seams = S.verdict(bad)
    assert (verdict, sections, seams) == ("FAIL", 6, 0)


def test_does_not_count_the_closing_tag():
    assert S.count_sections("<section></section>") == 1

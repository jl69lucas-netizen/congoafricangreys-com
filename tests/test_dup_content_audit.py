# tests/test_dup_content_audit.py
#
# The Python half of the DUP gate, run against the SAME fixture pairs the render harness's
# meta gate uses: one whitelist, two readers, one set of fixtures. If the two gates ever
# disagree about these files, one of them has drifted.
#
# Found 2026-09-11: both gates exempted a genuine crossover whenever it sat directly against
# a whitelisted line, because shingle growth fused the two into one run and a run that
# CONTAINED a stem was skipped whole. Before the fix, dup_content_audit.py over the
# adjacency pair printed "PASS — no cross-page duplicate runs ≥12 words in 2 pages."
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import dup_content_audit as D

FX = ROOT / "tests" / "render" / "fixtures"
CONGO = FX / "dup_corpus" / "sibling-congo-african-grey-for-sale.html"
TEXAS = FX / "dup_corpus" / "sibling-hand-raised-african-grey-texas.html"


def pair(page, sibling):
    wa, wb = D.words(page), D.words(sibling)
    return [" ".join(seg) for seg in D.crossovers(wa, D.shingles(wa), D.shingles(wb))]


def test_crossover_beside_a_whitelisted_line_is_reported():
    found = pair(FX / "known_broken" / "dup-adjacent-to-whitelist.html", TEXAS)
    # Exactly the two passages. Not one fused run, and not a run that starts mid-stem
    # ("airport $350 home tell us ...") — the old per-shingle skip produced that shape.
    assert found == [
        "before a chick leaves we record its weight every single morning and send the log home with it",
        "tell us which bird you are asking about and when you would like to bring one home",
    ]


def test_ordinary_crossover_still_reported():
    found = pair(FX / "known_broken" / "dup-no-sibling-crossover.html", CONGO)
    # The run starts in the shared tail of the two H1s ("... african greys for sale").
    assert len(found) == 1 and "every chick we place leaves our midland aviary" in found[0]


def test_known_good_is_silent_against_every_corpus_sibling():
    # CONGO carries the split-not-concatenate guard: 6 shared words, the shipping line,
    # 9 shared words. Silent only if each side is judged alone.
    for sib in (CONGO, TEXAS):
        assert pair(FX / "known_good" / "dup-no-sibling-crossover.html", sib) == []


def test_segments_are_split_at_the_stem_not_rejoined():
    left = "questions about travel days are welcome".split()
    stem = "ships nationwide $185 airport $350 home".split()
    right = "we text a photo the moment your bird lands".split()
    assert D.unwhitelisted_segments(left + stem + right) == [left, right]


def test_a_run_that_is_only_whitelisted_text_leaves_nothing():
    stem = "ships nationwide $185 airport $350 home".split()
    assert D.unwhitelisted_segments(stem) == []

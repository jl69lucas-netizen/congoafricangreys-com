# tests/test_aeo_audit.py
#
# RED fixtures for the AEO gate. Every threshold below traces to something measured on
# the live site on 2026-07-29/30, not to a guess:
#   - Psittacus erithacus absent from 4 of 8 for-sale pages (timneh had NO binomial)
#   - the breeder-name entity absent from 4 of 8
#   - dateModified on 23 of 108 pages (now 107, see commit 29fc384)
#   - the labeled-method entity present 0 times site-wide
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import aeo_audit as A


BLUF_GOOD = ("<h2>What Does a Congo Grey Cost?</h2><p>Congo African Greys from "
             "Mark &amp; Teri Benjamin cost $1,700 to $3,500.</p>")
BLUF_BAD = ("<h2>What Does a Congo Grey Cost?</h2><p>Before we get into numbers, it "
            "is worth stepping back and considering the long history of parrot "
            "keeping, which stretches back many centuries and has changed a great "
            "deal over that time, so that context matters here.</p>")


def test_bluf_accepts_a_short_declarative_opener():
    assert A.bluf_violations(BLUF_GOOD) == []


def test_bluf_flags_a_long_wind_up_before_the_answer():
    bad = A.bluf_violations(BLUF_BAD)
    assert bad and "What Does a Congo Grey Cost?" in bad[0]


def test_bluf_ignores_headings_with_no_following_prose():
    assert A.bluf_violations("<h2>Standalone</h2><h3>Next</h3>") == []


def test_entity_audit_counts_the_binomial_and_the_breeder():
    r = A.entity_report("<p>Psittacus erithacus birds from Mark &amp; Teri Benjamin "
                        "in Midland, TX are USDA AWA licensed.</p>")
    assert r["binomial"] == 1
    assert r["breeder"] == 1
    assert r["place"] == 1
    assert r["credential"] == 1


def test_entity_audit_reports_zero_for_the_timneh_case():
    """The timneh page shipped with no binomial at all."""
    r = A.entity_report("<p>Our birds are hand-raised and we ship nationwide.</p>")
    assert r["binomial"] == 0 and r["breeder"] == 0


def test_pronoun_density_flags_we_our_heavy_copy():
    heavy = "<p>" + "We raise our birds and we love our birds. " * 6 + "</p>"
    assert A.pronoun_heavy(heavy) is True
    named = "<p>" + "Mark and Teri raise every Congo African Grey by hand. " * 6 + "</p>"
    assert A.pronoun_heavy(named) is False


def test_labeled_method_detects_the_two_approved_names():
    assert A.labeled_methods("<p>The Benjamin Home-Raising Protocol starts at hatch.</p>") \
        == ["Benjamin Home-Raising Protocol"]
    assert A.labeled_methods("<p>Our Midland Socialization Method runs daily.</p>") \
        == ["Midland Socialization Method"]
    assert A.labeled_methods("<p>We socialize the birds.</p>") == []


def test_freshness_reads_json_ld_only():
    assert A.has_freshness('<script type="application/ld+json">'
                           '{"dateModified":"2026-07-30"}</script>') is True
    assert A.has_freshness("<p>Updated July 2026</p>") is False, \
        "a VISIBLE date must never satisfy the freshness check — CLAUDE.md bans it"


def test_visible_date_is_reported_as_a_violation():
    assert A.visible_dates("<p>Last updated: June 2026</p>")
    assert A.visible_dates("<p>We hatched 12 chicks in 2026.</p>") == []


def test_formatting_counts_tables_and_lists():
    r = A.formatting_report("<table><tr><td>a</td></tr></table><ul><li>x</li></ul>")
    assert r["tables"] == 1 and r["lists"] == 1


def test_stat_headers_are_detected():
    assert A.stat_headers("<h2>12 Years of Breeding Experience</h2>") == \
        ["12 Years of Breeding Experience"]
    assert A.stat_headers("<h2>Why Choose Us</h2>") == []

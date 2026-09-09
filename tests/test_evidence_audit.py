# tests/test_evidence_audit.py
#
# RED fixtures for the evidence gate. Every threshold traces to a measurement on the
# built site on 2026-09-09 (docs/superpowers/specs/2026-09-09-de-optimisation-evidence-pass-design.md §2):
#   - homepage <main>: CITES x44, C.A.Gs x66, DNA x40 against a proposed ceiling of 6/20/6
#   - the same review text credited to two names on one page (Hutter/Obrien, Schroder/Kempf)
#   - homepage <title> 233 chars against a 70-char ceiling
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import evidence_audit as E

BUDGETS = {
    "title_max_chars": 70,
    "scam_owner": ["how-to-avoid-african-grey-parrot-scams"],
    "legit_owner": ["trusted-african-grey-parrot-breeders"],
    "superlatives": ["world's best", "america's trusted"],
    "terms": {"CITES": "CITES", "scam": "scam", "legit": "legit"},
    "budgets": {"home": {"CITES": 2, "scam": 1, "legit": 0}},
}
LEDGER = {"claims": [
    {"id": "usda-awa", "pattern": "USDA[- ]licensed", "proof": "/proof/usda-redacted.webp", "anchor": "trust", "confirmed": "2026-09-09"},
    {"id": "dna-sexing", "pattern": "DNA[- ]sexed", "proof": "NOT FETCHED", "anchor": "health", "confirmed": None},
]}

def page(main, title="Short Title"):
    return f"<html><head><title>{title}</title></head><body><main>{main}</main></body></html>"


def test_term_budget_flags_overrun_and_names_the_term():
    html = page("<p>CITES CITES CITES</p>")
    f = E.term_budget(html, "home", BUDGETS)
    assert f == [("CITES", 3, 2)]


def test_term_budget_is_silent_within_budget():
    assert E.term_budget(page("<p>CITES once. CITES twice.</p>"), "home", BUDGETS) == []


def test_scam_owner_page_is_exempt_from_the_scam_ceiling():
    html = page("<p>scam scam scam scam</p>")
    assert E.term_budget(html, "interior", BUDGETS, slug="how-to-avoid-african-grey-parrot-scams") == []
    assert E.term_budget(html, "home", BUDGETS, slug="index") == [("scam", 4, 1)]


def test_title_length_flags_the_233_char_style():
    long = "A | " * 60
    assert E.title_too_long(page("<p>x</p>", title=long), BUDGETS) is not None
    assert E.title_too_long(page("<p>x</p>", title="African Grey Breeder in Midland, Texas"), BUDGETS) is None


def test_review_attribution_flags_same_quote_two_names():
    html = page(
        '<blockquote><p>I searched for months before finding C.A.Gs. Truly top notch.</p><cite>Clifford Hutter</cite></blockquote>'
        '<blockquote><p>I searched for months before finding C.A.Gs. Truly top notch.</p><cite>Archie Obrien</cite></blockquote>')
    bad = E.review_attribution(html)
    assert len(bad) == 1 and {"Clifford Hutter", "Archie Obrien"} <= set(bad[0][1])


def test_review_attribution_accepts_same_quote_same_name_twice():
    html = page(
        '<blockquote><p>Flawless from start to finish.</p><cite>Richard Woodard</cite></blockquote>'
        '<blockquote><p>Flawless from start to finish.</p><cite>Richard Woodard</cite></blockquote>')
    assert E.review_attribution(html) == []


def test_claim_binding_flags_repeated_claim_without_proof_link():
    html = page("<p>USDA-licensed.</p><p>USDA-licensed again.</p>")
    unbound = E.claim_binding(html, LEDGER)
    assert [u[0] for u in unbound] == ["usda-awa"]


def test_claim_binding_accepts_repeated_claim_when_proof_is_linked():
    html = page('<p>USDA-licensed.</p><p>USDA-licensed. <a href="/proof/usda-redacted.webp">See the licence</a></p>')
    assert E.claim_binding(html, LEDGER) == []


def test_claim_binding_reports_not_fetched_proof_as_warn_not_error():
    html = page("<p>DNA-sexed.</p><p>DNA-sexed.</p>")
    out = E.claim_binding(html, LEDGER)
    assert out == [("dna-sexing", 2, "NOT FETCHED")]


def test_statement_labels_required_where_species_claims_appear():
    html = page("<section id='congo'><h2>Congo</h2><p>Psittacus erithacus lives 40 to 60 years.</p></section>")
    assert E.missing_statement_labels(html) == ["congo"]
    labelled = page("<section id='congo'><h2>Congo</h2><p><span class='stmt-label' data-kind='fact'>Fact</span> Psittacus erithacus lives 40 to 60 years.</p></section>")
    assert E.missing_statement_labels(labelled) == []


def test_not_fetched_never_reaches_prose():
    assert E.not_fetched_in_prose(page("<p>Licence number: NOT FETCHED</p>")) == 1
    assert E.not_fetched_in_prose(page("<p>Licence on file.</p>")) == 0


def test_superlatives_are_flagged_unless_sourced_in_the_same_sentence():
    assert E.unsourced_superlatives(page("<p>The world's best talking parrot.</p>"), BUDGETS) == ["world's best"]
    sourced = page("<p>The world's best talking parrot, per <a href='https://example.org/study'>Pepperberg 1999</a>.</p>")
    assert E.unsourced_superlatives(sourced, BUDGETS) == []


def test_audit_returns_error_on_budget_breach_and_exit_code_follows():
    html = page("<p>CITES CITES CITES</p>")
    findings = E.audit("index", html, "home", BUDGETS, LEDGER)
    assert any(sev == "ERROR" and "CITES" in msg for sev, msg in findings)

"""evidence_audit per-slug overrides (breeder, 2026-09-10): the homepage keeps its five-part
Rule-21 title and its restored credential entities; every other slug keeps the page-type rules."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import evidence_audit as ea

def _budgets():
    return json.load(open(ROOT / "data" / "quality" / "evidence-budgets.json"))

def test_homepage_title_cap_is_205():
    assert _budgets()["title_max_chars_by_slug"]["index"] == 205

def test_homepage_long_title_passes():
    html = "<title>" + "x" * 200 + "</title>"
    assert ea.title_too_long(html, _budgets(), slug="index") is None

def test_other_slug_keeps_70():
    html = "<title>" + "x" * 90 + "</title>"
    assert ea.title_too_long(html, _budgets(), slug="congo-african-grey-for-sale") == (90, 70)

def _main(words):
    return "<html><body><main>" + " ".join(words) + "</main></body></html>"

def test_homepage_credential_terms_have_no_ceiling():
    html = _main(["CITES"] * 20 + ["DNA"] * 20 + ["USDA"] * 20 + ["Appendix I"] * 5)
    over = {t for t, n, c in ea.term_budget(html, "home", _budgets(), slug="index")}
    assert not (over & {"CITES", "DNA", "USDA", "Appendix I"}), over

def test_homepage_other_terms_still_capped():
    html = _main(["Midland"] * 30)
    over = {t for t, n, c in ea.term_budget(html, "home", _budgets(), slug="index")}
    assert "Midland" in over

def test_other_slug_credential_terms_still_capped():
    html = _main(["CITES"] * 20)
    over = {t for t, n, c in ea.term_budget(html, "home", _budgets(), slug="not-the-homepage")}
    assert "CITES" in over

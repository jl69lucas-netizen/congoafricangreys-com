"""The six proof-object entities must be visible on / at least twice each (breeder, 2026-09-10:
"these are entities Google needs to see them on the page"). Measured on dist/, never on source."""
import re
import pytest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
HOME = DIST / "index.html"
pytestmark = pytest.mark.skipif(not DIST.exists(), reason="dist/ not built — gates measure dist, never source")
TERMS = {
    "USDA": r"USDA (AWA|Animal Welfare Act)",
    "CITES": r"CITES (Appendix I|captive-bred|Documented|Cert)",
    "DNA": r"(PCR )?DNA[- ]sex(ed|ing)",
    "VET": r"avian[- ]vet(erinarian)?( health)? certif",
    "PBFD": r"PBFD",
    "HATCH": r"hatch certificate",
}

def _text():
    h = HOME.read_text(encoding="utf-8").split("<main", 1)[-1]
    return re.sub(r"<script.*?</scr" + r"ipt>", "", h, flags=re.S)

def test_each_entity_at_least_twice():
    counts = {k: len(re.findall(v, _text(), re.I)) for k, v in TERMS.items()}
    assert all(n >= 2 for n in counts.values()), counts


def _block(start_marker, end_marker="</section>"):
    h = HOME.read_text(encoding="utf-8")
    assert start_marker in h, f"marker not found: {start_marker}"
    return h.split(start_marker, 1)[1].split(end_marker, 1)[0]


def test_hero_pills_name_the_entities():
    hero = _block('class="hero-v3-b')
    ul = hero.split('aria-label="Breeder credentials"', 1)[1].split("</ul>", 1)[0]
    for pill in ("USDA AWA Licensed", "CITES Appendix I Documented", "PCR DNA-Sexed", "Avian-Vet Certified"):
        assert pill in ul, pill


def test_counter_label_is_cites_documented():
    strip = _block('class="counter-snippet')
    assert "CITES Documented" in strip


def test_owner_chips_say_pcr_dna_sexed():
    about = _block('id="about"')
    assert "PCR DNA-Sexed" in about and "Lab Sexed" not in about


def test_takeaways_carry_pcr_and_usda():
    h = HOME.read_text(encoding="utf-8")
    assert "DNA-Sexed &amp; Vet-Checked" in h or "DNA-Sexed & Vet-Checked" in h
    assert "AWA-Licensed Aviary" in h


def test_faq_answers_list_the_documents():
    faq = _block('id="faq"')
    assert "PCR DNA-sexing certificate" in faq
    assert "PBFD / Polyomavirus PCR results" in faq
    assert "PCR DNA-sexing test" in faq

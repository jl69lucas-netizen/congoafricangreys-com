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

import json, pathlib, sys
import pytest
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import pageboard as PB


MIN_BOARD = {
    "meta": {"slug": "x", "page_type": "hub", "status": "draft", "research_as_of": "2026-09-12", "sources": []},
    "brief": {"goal": "g", "scope": "s", "gates": ["hardening"], "done": "d", "out_of_scope": [],
              "primary_keyword": "african grey parrots for sale",
              "strategy": {"name": "n", "why": "w", "trade_off": "t"}},
    "h1": {"variants": ["a", "b", "c", "d", "e"], "recommended": 0, "pick": None},
    "sections": [{
        "id": "birds", "n": 1, "heading": "What Do We Have for Sale Right Now?", "intent": "inventory first",
        "category": "A", "framework": "EEBP", "words": {"min": 400, "max": 600}, "shape": "inventory",
        "keywords": {"primary": ["african grey parrots for sale"], "lsi": [], "longtail": [], "brand": [], "geo": []},
        "entities": ["ont:congo-african-grey"],
        "tree": [{"level": 3, "heading": "Our Congos", "intent": "", "children": [
                 {"level": 4, "heading": "What Does Each Cost?", "intent": "", "children": [
                 {"level": 5, "heading": "Every Price Includes the Folder", "intent": "", "children": [
                 {"level": 6, "heading": "Aviary Note: Read the Card", "intent": "", "children": []}]}]}]}],
        "images": [{"slot": "birds-opener", "kind": "infographic", "required": False, "prompt": "six bird cards"}],
        "options": {"candidates": ["avail-b"], "excluded": [], "pick": None, "note": ""}}],
    "tuple": {"hero": "hero-a", "dial": "dial-1", "rail": "rail-a", "toc": "t1", "takeaway": ["k1"],
              "table": "table-a", "faq": "faq-a", "h6_prefixes": ["Aviary Note:", "From the Book:", "Ask Us:"]},
    "assets": [{"slot": "hero", "kind": "photo", "w": 1280, "h": 960, "required": True, "status": "missing", "file": None, "alt": ""}],
    "approval": None,
}


def test_minimal_board_validates():
    PB.validate_board(MIN_BOARD)          # raises on failure


def test_board_missing_sections_fails():
    bad = json.loads(json.dumps(MIN_BOARD)); del bad["sections"]
    with pytest.raises(PB.BoardError):
        PB.validate_board(bad)


def test_unknown_shape_fails():
    bad = json.loads(json.dumps(MIN_BOARD)); bad["sections"][0]["shape"] = "banner"
    with pytest.raises(PB.BoardError):
        PB.validate_board(bad)


def test_ontology_and_ledger_schemas_accept_minimal_docs():
    PB.validate_ontology({"entities": [{"id": "ont:x", "name": "X", "aliases": [], "class": "Health",
                                        "authorization": "PROPOSED", "source": None, "owner_page": None}]})
    PB.validate_ledger({"pools": {"inventory": ["avail-a", "avail-b"]}, "pages": {}})

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
        "entities": ["ont:psittacus-erithacus"],
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


def test_extra_key_inside_words_fails():
    bad = json.loads(json.dumps(MIN_BOARD)); bad["sections"][0]["words"]["target"] = 500
    with pytest.raises(PB.BoardError):
        PB.validate_board(bad)


def test_bad_approval_pick_key_fails():
    bad = json.loads(json.dumps(MIN_BOARD))
    bad["approval"] = {"approved_at": "2026-09-12T00:00:00Z", "h1": 0, "picks": {"Bad Id!": "avail-b"},
                       "notes": {}, "canvas_version": None, "record_hash": "0" * 64}
    with pytest.raises(PB.BoardError):
        PB.validate_board(bad)


def test_save_board_rejects_slug_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(PB, "ROOT", tmp_path)
    board = json.loads(json.dumps(MIN_BOARD))          # meta.slug is "x"
    with pytest.raises(PB.BoardError):
        PB.save_board("y", board)
    assert not PB.board_path("y").exists()
    PB.save_board("x", board)                          # the matching slug still writes
    assert PB.board_path("x").exists()


def test_record_hash_ignores_approval_and_is_stable():
    a = json.loads(json.dumps(MIN_BOARD))
    b = json.loads(json.dumps(MIN_BOARD))
    b["approval"] = {"approved_at": "2026-09-12T10:00:00Z", "h1": 0, "picks": {}, "notes": {},
                     "canvas_version": None, "record_hash": "0" * 64}
    assert PB.record_hash(a) == PB.record_hash(b)
    assert len(PB.record_hash(a)) == 64


def test_record_hash_changes_when_a_heading_changes():
    a = json.loads(json.dumps(MIN_BOARD))
    b = json.loads(json.dumps(MIN_BOARD))
    b["sections"][0]["heading"] = "Something Else"
    assert PB.record_hash(a) != PB.record_hash(b)


def test_approval_matches_only_when_hash_matches():
    a = json.loads(json.dumps(MIN_BOARD))
    a["approval"] = {"approved_at": "2026-09-12T10:00:00Z", "h1": 0, "picks": {"birds": "avail-b"}, "notes": {},
                     "canvas_version": None, "record_hash": PB.record_hash(a)}
    assert PB.approval_matches(a) is True
    a["sections"][0]["intent"] = "edited after approval"
    assert PB.approval_matches(a) is False
    a["approval"] = None
    assert PB.approval_matches(a) is False


def test_record_hash_ignores_lifecycle_fields():
    a = json.loads(json.dumps(MIN_BOARD))
    b = json.loads(json.dumps(MIN_BOARD))
    b["meta"]["status"] = "approved"                   # board_approve.py flips this when it stamps
    b["assets"][0]["status"] = "baked"                 # and baking a photo fills these in
    b["assets"][0]["file"] = "/img/hero.webp"
    assert PB.record_hash(a) == PB.record_hash(b)
    b["assets"][0]["alt"] = "a real alt line"          # alt IS content, so it must move the hash
    assert PB.record_hash(a) != PB.record_hash(b)


def test_approval_survives_the_approve_then_bake_lifecycle():
    board = json.loads(json.dumps(MIN_BOARD))
    board["approval"] = {"approved_at": "2026-09-12T10:00:00Z", "h1": 0, "picks": {}, "notes": {},
                         "canvas_version": None, "record_hash": PB.record_hash(board)}
    board["meta"]["status"] = "approved"
    assert PB.approval_matches(board) is True
    board["assets"][0]["status"] = "baked"
    board["assets"][0]["file"] = "/img/hero.webp"
    assert PB.approval_matches(board) is True


def test_record_hash_survives_a_json_round_trip():
    a = json.loads(json.dumps(MIN_BOARD))
    b = json.loads(json.dumps(a, indent=2, ensure_ascii=False))
    assert PB.record_hash(a) == PB.record_hash(b)


def test_approval_matches_false_when_only_the_stored_hash_is_tampered_with():
    a = json.loads(json.dumps(MIN_BOARD))
    a["approval"] = {"approved_at": "2026-09-12T10:00:00Z", "h1": 0, "picks": {}, "notes": {},
                     "canvas_version": None, "record_hash": PB.record_hash(a)}
    assert PB.approval_matches(a) is True
    a["approval"]["record_hash"] = "0" * 64
    assert PB.approval_matches(a) is False


def test_approval_matches_returns_false_for_a_non_dict_approval():
    for junk in ("approved", ["approved"], 1, True):
        a = json.loads(json.dumps(MIN_BOARD))
        a["approval"] = junk
        assert PB.approval_matches(a) is False


def test_ontology_file_validates_and_has_the_blocked_family():
    ont = PB.load_ontology()
    ids = [e["id"] for e in ont["entities"]]
    assert len(ids) == len(set(ids)), "duplicate ontology ids"
    blocked = {e["id"] for e in ont["entities"] if e["authorization"] == "BLOCKED"}
    assert {"ont:wild-caught", "ont:imported-from", "ont:smuggled", "ont:undocumented-sale"} <= blocked


def test_every_asserted_entity_has_a_source():
    ont = PB.load_ontology()
    for e in ont["entities"]:
        if e["authorization"] == "ASSERTED":
            assert e["source"], f"{e['id']} is ASSERTED with no source"


def test_ledger_facts_are_present_and_asserted():
    ont = {e["id"]: e for e in PB.load_ontology()["entities"]}
    for i in ["ont:cites-appendix-i", "ont:usda-awa-licence", "ont:pcr-dna-sexing", "ont:pbfd-screening",
              "ont:avian-polyomavirus-screening", "ont:psittacosis-screening", "ont:72-hour-guarantee",
              "ont:airport-cargo-185", "ont:home-delivery-350", "ont:psittacus-erithacus", "ont:psittacus-timneh",
              "ont:benjamin-home-raising-protocol", "ont:midland-socialization-method"]:
        assert i in ont and ont[i]["authorization"] == "ASSERTED", i


def test_the_ontology_carries_no_page_type_or_price_range_rows():
    ids = {e["id"] for e in PB.load_ontology()["entities"]}
    assert ids.isdisjoint({"ont:page-type", "ont:homepage", "ont:comparison-page", "ont:location-page",
                           "ont:price-page", "ont:variant-guide", "ont:1-500-3-500"})


def test_load_ledger_raises_board_error_when_the_file_is_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(PB, "LEDGER", tmp_path / "component-ledger.json")
    with pytest.raises(PB.BoardError) as e:
        PB.load_ledger()
    assert "does not exist" in str(e.value) and "component-ledger.json" in str(e.value)


def test_reseeding_keeps_a_board_added_proposed_entity(tmp_path, monkeypatch):
    import seed_ontology
    copy = tmp_path / "cag-ontology.json"
    ont = PB.load_ontology()
    ont["entities"].append({"id": "ont:board-added", "name": "x", "aliases": [], "class": "Health",
                            "authorization": "PROPOSED", "source": None, "owner_page": None})
    copy.write_text(json.dumps(ont, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    monkeypatch.setattr(PB, "ONTOLOGY", copy)
    seed_ontology.main()
    after = {e["id"]: e for e in json.loads(copy.read_text(encoding="utf-8"))["entities"]}
    assert "ont:board-added" in after, "a board-added entity was dropped by a re-seed"
    assert after["ont:board-added"]["authorization"] == "PROPOSED"


def _anchor(heading):
    """GitHub-style heading slug: lowercase, punctuation dropped, spaces to hyphens."""
    import re
    s = re.sub(r"[^a-z0-9 \-]", "", heading.strip().lstrip("#").strip().lower())
    return s.replace(" ", "-")


def test_every_asserted_source_resolves_to_a_real_heading_or_data_key():
    for e in PB.load_ontology()["entities"]:
        src = e["source"]
        if e["authorization"] != "ASSERTED" or not src:
            continue
        if "#" not in src:                                  # a bare path must still resolve;
            if "/" in src or src.endswith(".md"):           # a literal citation (IUCN 22724813) need not
                assert (PB.ROOT / src).exists(), f"{e['id']}: {src} does not exist"
            continue
        path, _, frag = src.partition("#")
        f = PB.ROOT / path
        assert f.exists(), f"{e['id']}: {path} does not exist"
        if path.endswith(".json"):
            doc = json.loads(f.read_text(encoding="utf-8"))
            assert frag in doc or frag in doc.get("variants", {}), f"{e['id']}: no key {frag} in {path}"
        elif path.endswith(".md"):
            anchors = {_anchor(l) for l in f.read_text(encoding="utf-8").splitlines() if l.startswith("#")}
            assert frag in anchors, f"{e['id']}: {path} has no heading anchored #{frag}"


def test_ledger_twins_are_not_duplicated_as_proposed_catalog_rows():
    ids = {e["id"] for e in PB.load_ontology()["entities"]}
    assert ids.isdisjoint({"ont:dna-sexing", "ont:usda-license", "ont:cites-documentation",
                           "ont:iata-compliant-shipping", "ont:lifetime-advisory"})


def test_catalog_parse_floor_rejects_a_catalog_that_lost_its_tables(tmp_path, monkeypatch):
    import seed_ontology
    empty = tmp_path / "cag-entity-agent.md"
    empty.write_text("# skill\n\n## Something Else\n\nno catalog here\n", encoding="utf-8")
    monkeypatch.setattr(seed_ontology, "CATALOG", empty)
    with pytest.raises(PB.BoardError) as e:
        seed_ontology.catalog_entities()
    assert "catalog rows" in str(e.value)


def test_reseeding_carries_an_earlier_decision_on_a_catalog_id(tmp_path, monkeypatch):
    import seed_ontology
    copy = tmp_path / "cag-ontology.json"
    ont = PB.load_ontology()
    for e in ont["entities"]:
        if e["id"] == "ont:hand-raised":                  # a catalog row, PROPOSED as seeded
            e.update(authorization="ASSERTED", source="x", owner_page="/foo/")
    copy.write_text(json.dumps(ont, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    monkeypatch.setattr(PB, "ONTOLOGY", copy)
    seed_ontology.main()
    after = {e["id"]: e for e in json.loads(copy.read_text(encoding="utf-8"))["entities"]}
    assert after["ont:hand-raised"]["authorization"] == "ASSERTED"
    assert after["ont:hand-raised"]["source"] == "x"
    assert after["ont:hand-raised"]["owner_page"] == "/foo/"


def test_ledger_file_validates_and_knows_pages_a_and_b():
    ledger = PB.load_ledger()
    assert ledger["pages"]["buy-african-grey-parrots-with-shipping"]["toc"] == "toc-t3-boarding-pass"
    assert ledger["pages"]["african-grey-parrots-for-sale-near-me"]["hero"] == "hero-c-mosaic-metrics#geo-tile-field"


def test_candidates_subtract_what_siblings_own():
    ledger = {"pools": {"inventory": ["avail-a", "avail-b", "bird-cards"]},
              "pages": {"dna-tested-african-grey-for-sale": {"hero": "hero-c", "dial": "dial-1", "rail": "rail-a", "toc": "avail-b",
                        "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    cands, excluded = PB.candidates_for("inventory", ledger, slug="african-grey-parrots-for-sale")
    assert cands == ["avail-a", "avail-b#refresh", "bird-cards"]
    assert excluded == [{"component": "avail-b", "owner": "dna-tested-african-grey-for-sale"}]


def test_candidates_never_exclude_the_page_itself():
    ledger = {"pools": {"nav": ["dial-1", "dial-2"]},
              "pages": {"x": {"hero": "", "dial": "dial-1", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    cands, excluded = PB.candidates_for("nav", ledger, slug="x")
    assert cands == ["dial-1", "dial-2"] and excluded == []


def test_standard_shape_has_no_options():
    cands, excluded = PB.candidates_for("standard", {"pools": {}, "pages": {}}, slug="x")
    assert cands == [] and excluded == []


def test_exhausted_pool_yields_refresh_candidates():
    ledger = {"pools": {"hero": ["hero-a", "hero-c"]},
              "pages": {"p1": {"hero": "hero-a", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []},
                        "p2": {"hero": "hero-c", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    cands, excluded = PB.candidates_for("hero", ledger, slug="new-page")
    assert cands == ["hero-a#refresh", "hero-c#refresh"]
    assert excluded == [{"component": "hero-a", "owner": "p1"}, {"component": "hero-c", "owner": "p2"}]


def test_refreshed_id_owns_its_base():
    ledger = {"pools": {"hero": ["hero-c"]},
              "pages": {"near-me": {"hero": "hero-c#geo-tile-field", "dial": "", "rail": "", "toc": "",
                                    "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    owned = PB.owned_components(ledger)
    assert owned["hero-c"] == "near-me" and owned["hero-c#geo-tile-field"] == "near-me"
    cands, excluded = PB.candidates_for("hero", ledger, slug="other")
    assert cands == ["hero-c#refresh"]
    assert excluded == [{"component": "hero-c", "owner": "near-me"}]


def test_base_of():
    assert PB.base_of("hero-c-mosaic-metrics") == "hero-c-mosaic-metrics"
    assert PB.base_of("hero-c-mosaic-metrics#geo-tile-field") == "hero-c-mosaic-metrics"
    assert PB.base_of("faq-b#map-pin") == "faq-b"

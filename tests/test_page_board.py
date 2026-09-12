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


def test_candidates_of_a_shared_pool_are_all_free():
    """`inventory` is not a refresh pool: a sibling using avail-b costs nobody anything,
    because the ledger's discipline is that the combo differs, not the component."""
    ledger = {"pools": {"inventory": ["avail-a", "avail-b", "bird-cards"]},
              "pages": {"dna-tested-african-grey-for-sale": {"hero": "hero-c", "dial": "dial-1", "rail": "rail-a", "toc": "avail-b",
                        "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    cands, excluded = PB.candidates_for("inventory", ledger, slug="african-grey-parrots-for-sale")
    assert cands == ["avail-a", "avail-b", "bird-cards"] and excluded == []


def test_a_nav_shaped_section_draws_from_the_toc_pool():
    ledger = {"pools": {"nav": ["dial-1", "rail-a"], "toc": ["toc-t1", "toc-t2"]}, "pages": {}}
    cands, excluded = PB.candidates_for("nav", ledger, slug="x")
    assert cands == ["toc-t1", "toc-t2"] and excluded == []


def test_candidates_never_exclude_the_page_itself():
    ledger = {"refresh_pools": ["hero"], "pools": {"hero": ["hero-a", "hero-c"]},
              "pages": {"x": {"hero": "hero-a", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    cands, excluded = PB.candidates_for("hero", ledger, slug="x")
    assert cands == ["hero-a", "hero-c"] and excluded == []


def test_standard_shape_has_no_options():
    cands, excluded = PB.candidates_for("standard", {"pools": {}, "pages": {}}, slug="x")
    assert cands == [] and excluded == []


def test_exhausted_pool_yields_refresh_candidates():
    ledger = {"refresh_pools": ["hero"], "pools": {"hero": ["hero-a", "hero-c"]},
              "pages": {"p1": {"hero": "hero-a", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []},
                        "p2": {"hero": "hero-c", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    cands, excluded = PB.candidates_for("hero", ledger, slug="new-page")
    assert cands == ["hero-a#refresh", "hero-c#refresh"]
    assert excluded == [{"component": "hero-a", "owner": "p1", "owners": ["p1"]},
                        {"component": "hero-c", "owner": "p2", "owners": ["p2"]}]


def test_refreshed_id_owns_its_base():
    ledger = {"refresh_pools": ["hero"], "pools": {"hero": ["hero-c"]},
              "pages": {"near-me": {"hero": "hero-c#geo-tile-field", "dial": "", "rail": "", "toc": "",
                                    "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    owned = PB.owned_components(ledger)
    assert owned["hero-c"] == ["near-me"] and owned["hero-c#geo-tile-field"] == ["near-me"]
    cands, excluded = PB.candidates_for("hero", ledger, slug="other")
    assert cands == ["hero-c#refresh"]
    assert excluded == [{"component": "hero-c", "owner": "near-me", "owners": ["near-me"]}]


def test_base_of():
    assert PB.base_of("hero-c-mosaic-metrics") == "hero-c-mosaic-metrics"
    assert PB.base_of("hero-c-mosaic-metrics#geo-tile-field") == "hero-c-mosaic-metrics"
    assert PB.base_of("faq-b#map-pin") == "faq-b"


def test_every_tuple_component_appears_in_some_pool():
    """A tuple may draw from any pool — eggs' TOC is the nav pool's dial-1-clay — but a
    component no pool carries can never be offered to a sibling page again."""
    ledger = PB.load_ledger()
    pooled = {PB.base_of(c) for pool in ledger["pools"].values() for c in pool}
    orphans = {PB.base_of(cid): slug for slug, t in ledger["pages"].items()
               for cid in PB.tuple_component_ids(t) if PB.base_of(cid) not in pooled}
    assert orphans == {}


def test_real_ledger_refresh_owns_its_base():
    owned = PB.owned_components(PB.load_ledger())
    assert "african-grey-parrots-for-sale-near-me" in owned["hero-c-mosaic-metrics"]
    assert owned["hero-c-mosaic-metrics#geo-tile-field"] == ["african-grey-parrots-for-sale-near-me"]


def test_real_ledger_page_is_never_an_owner_of_its_own_candidates():
    ledger = PB.load_ledger()
    near_me = "african-grey-parrots-for-sale-near-me"
    cands, excluded = PB.candidates_for("hero", ledger, slug=near_me)
    assert cands, "the hero pool must never hand a page an empty menu"
    assert near_me not in {o for e in excluded for o in e["owners"]}
    assert near_me not in {e["owner"] for e in excluded}


def test_real_ledger_h6_prefixes_are_spent_by_their_owner_only():
    ledger = PB.load_ledger()
    near_me = "african-grey-parrots-for-sale-near-me"
    assert PB.spent_h6_prefixes(ledger)["Distance Note:"] == [near_me]
    assert "Distance Note:" not in PB.spent_h6_prefixes(ledger, exclude_slug=near_me)


def test_validate_ledger_rejects_the_unnamed_refresh_placeholder():
    ledger = PB.load_ledger()
    ledger["pages"]["african-grey-parrots-for-sale-near-me"]["hero"] = "x#refresh"
    with pytest.raises(PB.BoardError) as e:
        PB.validate_ledger(ledger)
    assert "x#refresh" in str(e.value)


def test_ledger_tuple_slot_may_be_empty():
    """An empty scalar slot means "this page has no such component", not a bad id."""
    PB.validate_ledger({"pools": {"hero": ["hero-a"]},
                        "pages": {"p1": {"hero": "hero-a", "dial": "", "rail": "", "toc": "",
                                         "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}})


def test_all_headings_walks_the_tree_in_order():
    hs = PB.all_headings(MIN_BOARD)
    assert hs[0] == (1, "a")                      # h1.pick is None, so the recommendation
    assert hs[1] == (2, "What Do We Have for Sale Right Now?")
    assert hs[-1] == (6, "Aviary Note: Read the Card")
    assert [lvl for lvl, _ in hs] == [1, 2, 3, 4, 5, 6]


def test_all_headings_opens_on_the_breeder_pick_when_there_is_one():
    b = json.loads(json.dumps(MIN_BOARD)); b["h1"]["pick"] = 3
    assert PB.all_headings(b)[0] == (1, "d")


def test_header_precheck_finds_exact_and_shingle_matches():
    live = {"/congo-vs-timneh/": ["Congo or Timneh — Which Suits Your Household?", "What Every Bird Card Tells You Before You Ask"]}
    hits = PB.header_precheck(["Congo or Timneh — Which Suits Your Household?",
                               "What Every Bird Card Tells You Before You Buy",
                               "A Heading Nobody Has Used"], live)
    kinds = {h["heading"]: h["kind"] for h in hits}
    assert kinds["Congo or Timneh — Which Suits Your Household?"] == "exact"
    assert kinds["What Every Bird Card Tells You Before You Buy"] == "shingle"
    assert "A Heading Nobody Has Used" not in kinds


def test_header_precheck_template_collision_across_species():
    live = {"/african-grey-vs-macaw/": ["Is a Macaw Right for You?"]}
    hits = PB.header_precheck(["Is a Cockatoo Right for You?"], live)
    assert hits and hits[0]["kind"] == "template"


def test_authorization_check_reports_blocked_and_proposed():
    ont = {"entities": [
        {"id": "ont:ok", "name": "ok", "aliases": [], "class": "Health", "authorization": "ASSERTED", "source": "x", "owner_page": None},
        {"id": "ont:maybe", "name": "maybe", "aliases": [], "class": "Health", "authorization": "PROPOSED", "source": None, "owner_page": None},
        {"id": "ont:wild-caught", "name": "wild-caught", "aliases": [], "class": "Commerce", "authorization": "BLOCKED", "source": "rule 2", "owner_page": None}]}
    b = json.loads(json.dumps(MIN_BOARD))
    b["sections"][0]["entities"] = ["ont:ok", "ont:maybe", "ont:wild-caught", "ont:unknown"]
    r = PB.authorization_check(b, ont)
    assert r["blocked"] == ["ont:wild-caught"]
    assert r["proposed"] == ["ont:maybe"]
    assert r["unknown"] == ["ont:unknown"]


def test_distribution_sums_keywords_and_words():
    d = PB.distribution(MIN_BOARD)
    assert d["rows"][0]["section"] == "birds" and d["rows"][0]["primary"] == 1
    assert d["totals"]["words_min"] == 400 and d["totals"]["words_max"] == 600
    assert d["h_counts"] == {"h1": 1, "h2": 1, "h3": 1, "h4": 1, "h5": 1, "h6": 1}


def test_distribution_totals_add_across_two_sections():
    b = json.loads(json.dumps(MIN_BOARD))
    second = json.loads(json.dumps(b["sections"][0]))
    second.update({"id": "shipping", "n": 2, "heading": "How Do We Ship?",
                   "words": {"min": 250, "max": 300}, "tree": []})
    second["keywords"] = {"primary": ["african grey shipping"], "lsi": ["iata"],
                          "longtail": [], "brand": ["c.a.gs"], "geo": ["midland", "texas"]}
    b["sections"].append(second)
    PB.validate_board(b)                                   # still a buildable record
    d = PB.distribution(b)
    assert [r["section"] for r in d["rows"]] == ["birds", "shipping"]
    assert d["totals"] == {"primary": 2, "lsi": 1, "longtail": 0, "brand": 1, "geo": 2,
                           "words_min": 650, "words_max": 900}
    assert d["h_counts"] == {"h1": 1, "h2": 2, "h3": 1, "h4": 1, "h5": 1, "h6": 1}


def _tmp_dist(tmp_path):
    """A miniature dist/: the homepage, a one-level page, a two-level page."""
    pages = {
        "index.html": "<html><body><h1>Home</h1></body></html>",
        "foo/index.html": "<html><body><h2>Foo <em>Heading</em></h2></body></html>",
        "a/b/index.html": "<html><body><h3>Cards &amp; Folders</h3>\n"
                          "<h2 class='x'>Every Bird Card\n  Tells You Something</h2></body></html>",
    }
    for rel, html in pages.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(html, encoding="utf-8")
    return tmp_path


def test_live_headings_slugs_the_homepage_as_root(tmp_path):
    live = PB.live_headings(_tmp_dist(tmp_path))
    assert set(live) == {"/", "/foo/", "/a/b/"}
    assert live["/"] == ["Home"]
    assert live["/foo/"] == ["Foo Heading"]                      # nested tags stripped
    assert live["/a/b/"] == ["Cards & Folders", "Every Bird Card Tells You Something"]


def test_header_precheck_shingle_needs_five_tokens_of_live_heading(tmp_path):
    live = PB.live_headings(_tmp_dist(tmp_path))
    # "Foo Heading" is two tokens long — it can never seed a 5-token shingle.
    assert PB.header_precheck(["Foo Heading With More Words Here"], live) == []
    hits = PB.header_precheck(["Every Bird Card Tells You Today"], live)
    assert [(h["kind"], h["page"], h["with"]) for h in hits] == [
        ("shingle", "/a/b/", "Every Bird Card Tells You Something")]


def test_live_headings_skips_site_chrome_like_the_dup_gate():
    """Only body headings enter the corpus. A nav link, a read-card title and a footer
    heading are chrome the dup gate already ignores, and counting them would make the
    pre-check collide every new page with the template every page shares."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        dist = pathlib.Path(d)
        (dist / "p").mkdir()
        (dist / "p" / "index.html").write_text(
            "<html><body>"
            "<nav><h2>By Location</h2></nav>"
            "<div class='read-cards'><h3>Congo vs Timneh</h3></div>"
            "<h2>What Does a Congo Cost?</h2>"
            "<footer><h2>Contact</h2></footer>"
            "</body></html>", encoding="utf-8")
        assert PB.live_headings(dist) == {"/p/": ["What Does a Congo Cost?"]}


def test_header_precheck_excludes_the_page_being_rebuilt():
    live = {"/buy/": ["What Does a Congo Cost?"], "/other/": ["Where Do We Ship?"]}
    assert PB.header_precheck(["What Does a Congo Cost?"], live)[0]["kind"] == "exact"
    assert PB.header_precheck(["What Does a Congo Cost?"], live, exclude_page="/buy/") == []


def test_header_precheck_matches_curly_apostrophes_and_plural_species():
    live = {"/a/": ["What Do African Greys Eat Each Day?"]}          # plural, once invisible
    hits = PB.header_precheck(["What Do Timneh Eat Each Day?"], live)
    assert hits and hits[0]["kind"] == "template"
    assert PB.header_precheck(["A Grey’s First Week Home"],
                              {"/b/": ["A Grey's First Week Home"]})[0]["kind"] == "exact"


def _approved(board):
    b = json.loads(json.dumps(board))
    for s in b["sections"]:
        if s["shape"] != "standard":
            s["options"]["pick"] = s["options"]["candidates"][0] if s["options"]["candidates"] else "default"
    b["approval"] = {"approved_at": "2026-09-12T10:00:00Z", "h1": 0, "picks": {s["id"]: s["options"]["pick"] for s in b["sections"]},
                     "notes": {}, "canvas_version": None, "record_hash": PB.record_hash(b)}
    b["meta"]["status"] = "approved"
    return b


ONT_OK = {"entities": [{"id": "ont:psittacus-erithacus", "name": "Congo", "aliases": [], "class": "Organism",
                        "authorization": "ASSERTED", "source": "x", "owner_page": None}]}
LEDGER_EMPTY = {"pools": {"inventory": ["avail-b"]}, "pages": {}}


def test_gate_passes_an_approved_minimal_board():
    b = _approved(MIN_BOARD)
    # A live corpus of one unrelated sibling: live={} is itself a FAIL (a gate that
    # examined nothing is not a pass), which is asserted in its own test below.
    f = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={"/other/": ["Where Do We Ship Our Birds Each Week?"]},
                         stage="build")
    # MIN_BOARD carries exactly one H5 and one H6 by design (test_distribution_counts_headings),
    # so the volume floor is the one FAIL a minimal board is meant to raise. Its severity is
    # asserted on its own in test_gate_h5_h6_minimums_are_warn_on_home_and_location.
    assert [x for x in f if x["sev"] == "FAIL" and x["check"] != "min-h5-h6"] == [], f


def test_gate_fails_without_matching_approval():
    b = _approved(MIN_BOARD)
    b["sections"][0]["intent"] = "edited after approval"
    f = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")
    assert any(x["check"] == "approval-hash" and x["sev"] == "FAIL" for x in f)


def test_gate_fails_on_blocked_entity_and_owned_shell_and_spent_prefix():
    b = _approved(MIN_BOARD)
    b["sections"][0]["entities"].append("ont:wild-caught")
    ont = {"entities": ONT_OK["entities"] + [{"id": "ont:wild-caught", "name": "w", "aliases": [], "class": "Commerce",
                                              "authorization": "BLOCKED", "source": "r2", "owner_page": None}]}
    ledger = {"pools": {"inventory": ["avail-b"]},
              "pages": {"sibling": {"hero": "hero-a", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "",
                                    "h6_prefixes": ["Aviary Note:"]}}}
    b["approval"]["record_hash"] = PB.record_hash(b)
    f = {x["check"] for x in PB.gate_findings(b, ont, ledger, live={}, stage="build") if x["sev"] == "FAIL"}
    assert {"entity-blocked", "ledger-shell-owned", "ledger-spent-prefix"} <= f


def _ledger_with(**tuple_fields):
    t = {"hero": "", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}
    t.update(tuple_fields)
    return {"pools": {"inventory": ["avail-b"]}, "pages": {"sibling": t}}


def _checks(board, ledger):
    return {x["check"] for x in PB.gate_findings(board, ONT_OK, ledger, live={}, stage="build") if x["sev"] == "FAIL"}


def test_gate_flags_a_copied_hero_dial_rail_triple():
    """Components are shared by design; the signature the reader sees first is not."""
    b = _approved(MIN_BOARD)
    same = _checks(b, _ledger_with(hero="hero-a", dial="dial-1", rail="rail-a", toc="t9", table="table-z", faq="faq-z"))
    assert "ledger-triple-owned" in same
    diff = _checks(b, _ledger_with(hero="hero-a", dial="dial-2", rail="rail-a", toc="t9", table="table-z", faq="faq-z"))
    assert "ledger-triple-owned" not in diff


def test_gate_flags_a_takeaway_set_a_sibling_already_uses():
    b = _approved(MIN_BOARD)
    b["tuple"]["takeaway"] = ["k1", "k2"]
    b["approval"]["record_hash"] = PB.record_hash(b)
    same = _checks(b, _ledger_with(takeaway=["k2", "k1"]))          # a set, so order cannot dodge it
    assert "ledger-takeaway-set-owned" in same
    assert "ledger-takeaway-set-owned" not in _checks(b, _ledger_with(takeaway=["k1", "k3"]))
    assert "ledger-takeaway-set-owned" not in _checks(b, _ledger_with(takeaway=["k1"]))


def test_gate_flags_a_tuple_that_is_identical_to_a_siblings():
    b = _approved(MIN_BOARD)
    t = b["tuple"]
    ledger = _ledger_with(hero=t["hero"], dial=t["dial"], rail=t["rail"], toc=t["toc"],
                          takeaway=list(t["takeaway"]), table=t["table"], faq=t["faq"])
    f = _checks(b, ledger)
    assert "ledger-tuple-identical" in f
    # the narrower rules do not also fire: one identical sibling is one finding, not three
    assert "ledger-triple-owned" not in f and "ledger-takeaway-set-owned" not in f


def test_gate_lets_a_refreshed_shell_pass_but_not_a_bare_one():
    b = _approved(MIN_BOARD)
    ledger = _ledger_with(hero="hero-a", dial="dial-9", rail="rail-9")
    assert "ledger-shell-owned" in _checks(b, ledger)               # MIN_BOARD's bare hero-a
    b["tuple"]["hero"] = "hero-a#minimal"
    b["approval"]["record_hash"] = PB.record_hash(b)
    assert "ledger-shell-owned" not in _checks(b, ledger)
    ledger["pages"]["sibling"]["hero"] = "hero-a#minimal"           # the same delta, though, is the same shell
    assert "ledger-shell-owned" in _checks(b, ledger)


def test_gate_does_not_police_shared_pool_components():
    """dial-1-clay is on nine pages by design: a shared dial, rail or table is never a FAIL."""
    b = _approved(MIN_BOARD)
    f = _checks(b, _ledger_with(hero="hero-z", dial="dial-1", rail="rail-a", toc="t9", table="table-a", faq="faq-z"))
    assert not any(c.startswith("ledger-") for c in f), f


def test_gate_fails_on_live_header_collision_and_missing_pick():
    b = _approved(MIN_BOARD)
    b["sections"][0]["options"]["pick"] = None
    b["approval"]["picks"] = {}
    b["approval"]["record_hash"] = PB.record_hash(b)
    live = {"/y/": ["What Do We Have for Sale Right Now?"]}   # a sibling, not "/x/": the gate excludes the board's own page
    f = {x["check"] for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live=live, stage="build") if x["sev"] == "FAIL"}
    assert {"header-collision", "signature-no-pick"} <= f


def test_gate_release_stage_fails_on_missing_required_slot_only_at_release():
    b = _approved(MIN_BOARD)
    build = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")
    release = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="release")
    assert not any(x["check"] == "asset-required-missing" for x in build)
    assert any(x["check"] == "asset-required-missing" and x["sev"] == "FAIL" for x in release)


def test_gate_h5_h6_minimums_are_warn_on_home_and_location():
    b = _approved(MIN_BOARD)
    f = {x["check"]: x["sev"] for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")}
    assert f.get("min-h5-h6") == "FAIL"           # hub page type: hard
    b["meta"]["page_type"] = "location"; b["approval"]["record_hash"] = PB.record_hash(b)
    f = {x["check"]: x["sev"] for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")}
    assert f.get("min-h5-h6") == "WARN"


def test_gate_whitelist_matches_whole_tokens_not_substrings():
    """"evie" is a bird-name whitelist entry and it lives inside "Review". Substring
    matching cleared a real crossover; whole-token matching keeps the FAIL."""
    b = _approved(MIN_BOARD)
    b["sections"][0]["tree"][0]["heading"] = "Our Honest Review of Every Congo We Raise"
    b["approval"]["record_hash"] = PB.record_hash(b)
    live = {"/sibling/": ["Our Honest Review of Every Congo We Raise"]}
    msgs = [x["msg"] for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live=live, stage="build")
            if x["check"] == "header-collision"]
    assert any("Honest Review" in m for m in msgs), msgs
    assert PB._whitelisted("Bery") and PB._whitelisted("Frequently Asked Questions")
    assert not PB._whitelisted("Our Honest Review of Every Congo We Raise")


def test_gate_fails_when_the_header_precheck_examined_zero_live_pages():
    b = _approved(MIN_BOARD)
    f = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")
    assert any(x["check"] == "header-precheck-examined-zero" and x["sev"] == "FAIL" for x in f)
    f = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={"/other/": ["Where Do We Ship Our Birds Each Week?"]},
                         stage="build")
    assert not any(x["check"] == "header-precheck-examined-zero" for x in f)


def test_gate_rejects_an_unknown_stage():
    with pytest.raises(PB.BoardError):
        PB.gate_findings(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, stage="deploy")


def test_board_gate_cli_exits_2_on_an_unknown_flag_and_on_a_missing_board():
    import subprocess
    gate = str(ROOT / "scripts" / "board_gate.py")
    r = subprocess.run([sys.executable, gate, "x", "--publish"], capture_output=True, text=True)
    assert r.returncode == 2 and "usage: board_gate.py" in r.stdout
    r = subprocess.run([sys.executable, gate, "no-such-page-anywhere"], capture_output=True, text=True)
    assert r.returncode == 2 and "board-gate ERROR no board for" in r.stdout


def test_own_live_key_is_the_root_for_the_homepage():
    b = json.loads(json.dumps(MIN_BOARD))
    assert PB.own_live_key(b) == "/x/"
    b["meta"]["page_type"] = "home"
    assert PB.own_live_key(b) == "/"
    b["meta"]["page_type"] = "hub"; b["meta"]["slug"] = "index"
    assert PB.own_live_key(b) == "/"


def test_gate_against_the_real_ledger_treats_a_refresh_id_as_unspent():
    ledger = PB.load_ledger()
    b = _approved(MIN_BOARD)

    def hero_hits(hero):
        b["tuple"]["hero"] = hero
        b["approval"]["record_hash"] = PB.record_hash(b)
        return [x for x in PB.gate_findings(b, ONT_OK, ledger, live={}, stage="build")
                if x["check"] == "ledger-shell-owned" and "tuple.hero" in x["msg"]]

    assert hero_hits("hero-c-mosaic-metrics#brand-new") == []
    hits = hero_hits("hero-c-mosaic-metrics")
    assert len(hits) == 1 and "dna-tested-african-grey-for-sale" in hits[0]["msg"], hits


@pytest.mark.skipif(not PB.DIST.exists(), reason="needs a built dist/")
def test_gate_against_the_real_dist_whitelists_faq_but_flags_current_pricing():
    live = PB.live_headings()
    b = _approved(MIN_BOARD)
    b["sections"][0]["tree"][0]["children"] += [
        {"level": 4, "heading": "Frequently Asked Questions", "intent": "", "children": []},
        {"level": 4, "heading": "Current Pricing", "intent": "", "children": []},
    ]
    b["approval"]["record_hash"] = PB.record_hash(b)
    msgs = [x["msg"] for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live=live, stage="build")
            if x["check"] == "header-collision"]
    assert any("'Current Pricing'" in m for m in msgs), msgs
    assert not any("Frequently Asked Questions" in m for m in msgs), msgs


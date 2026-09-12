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


@pytest.fixture(scope="session")
def live_dist():
    """dist/ is 104 pages of HTML; reading it once per session rather than once per test
    is the difference between a gate you run and one you skip."""
    if not PB.DIST.exists():
        pytest.skip("needs a built dist/")
    return PB.live_headings()

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
            s["options"]["pick"] = s["options"]["pick"] or (
                s["options"]["candidates"][0] if s["options"]["candidates"] else "default")
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
    ledger = {"refresh_pools": ["hero", "toc", "faq"], "pools": {"inventory": ["avail-b"]},
              "pages": {"sibling": {"hero": "hero-a", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "",
                                    "h6_prefixes": ["Aviary Note:"]}}}
    b["approval"]["record_hash"] = PB.record_hash(b)
    f = {x["check"] for x in PB.gate_findings(b, ont, ledger, live={}, stage="build") if x["sev"] == "FAIL"}
    assert {"entity-blocked", "ledger-shell-owned", "ledger-spent-prefix"} <= f


def _ledger_with(**tuple_fields):
    t = {"hero": "", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}
    t.update(tuple_fields)
    return {"refresh_pools": ["hero", "toc", "faq"], "pools": {"inventory": ["avail-b"]}, "pages": {"sibling": t}}


def _checks(board, ledger):
    return {x["check"] for x in PB.gate_findings(board, ONT_OK, ledger, live={}, stage="build") if x["sev"] == "FAIL"}


def test_gate_flags_a_copied_hero_dial_rail_triple():
    """Components are shared by design; the signature the reader sees first is not."""
    b = _approved(MIN_BOARD)
    same = _checks(b, _ledger_with(hero="hero-a", dial="dial-1", rail="rail-a", toc="t9", table="table-z", faq="faq-z"))
    assert "ledger-triple-owned" in same
    # and the triple names the hero already, so the shell rule does not say it twice
    assert "ledger-shell-owned" not in same, same
    diff = _checks(b, _ledger_with(hero="hero-a", dial="dial-2", rail="rail-a", toc="t9", table="table-z", faq="faq-z"))
    assert "ledger-triple-owned" not in diff
    assert "ledger-shell-owned" in diff, diff      # a shared hero on its own is still a shell finding


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
    # one identical sibling is ONE finding, not four: the narrower rules stay silent
    assert sorted(x for x in f if x.startswith("ledger-")) == ["ledger-tuple-identical"], f


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


def test_gate_against_the_real_dist_whitelists_faq_but_flags_current_pricing(live_dist):
    live = dict(live_dist)
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



def test_shingle_hits_carry_the_window_they_matched():
    hits = PB.header_precheck(["Where Do We Ship Our Birds Each Week, Exactly?"],
                              {"/y/": ["Where Do We Ship Our Birds Each Week?"]})
    assert hits[0]["kind"] == "shingle" and hits[0]["shingle"] == "where do we ship our"


def test_head_term_shingle_helper():
    pk = "african grey parrots for sale near me"
    assert PB._head_term_shingle("african grey parrot for sale", pk)       # a head term
    assert PB._head_term_shingle("african grey parrots for sale", pk)      # and the board's own keyword
    assert not PB._head_term_shingle("every african grey we place", pk)
    assert not PB._head_term_shingle("", pk)


def test_gate_exempts_a_head_term_only_shingle_but_not_a_real_one():
    """`african grey parrot for sale` is in 46 live headings by design; a page cannot be
    asked to rank for a phrase it is forbidden to write. Precedent: 2026-08-10 §C2."""
    b = _approved(MIN_BOARD)
    b["sections"][0]["heading"] = "Is an African Grey Parrot for Sale Here Right for You?"
    b["approval"]["record_hash"] = PB.record_hash(b)
    head_only = {"/y/": ["African Grey Parrot for Sale Arizona"]}
    msgs = lambda live: [x["msg"] for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live=live, stage="build")
                         if x["check"] == "header-collision"]
    assert msgs(head_only) == []
    real = {"/y/": ["What Health Guarantees Come With Every African Grey We Place?"]}
    b["sections"][0]["heading"] = "What Arrives With Every African Grey We Place?"
    b["approval"]["record_hash"] = PB.record_hash(b)
    assert len(msgs(real)) == 1, msgs(real)


def test_an_exact_head_term_heading_is_never_exempt():
    """The exemption is for shingles. A heading copied whole is copied whole."""
    b = _approved(MIN_BOARD)
    b["sections"][0]["heading"] = "African Grey Parrot for Sale"
    b["approval"]["record_hash"] = PB.record_hash(b)
    f = [x for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={"/y/": ["African Grey Parrot For Sale"]},
                                     stage="build") if x["check"] == "header-collision"]
    assert len(f) == 1 and "exact" in f[0]["msg"], f

def test_shingle_hits_report_every_window_not_just_the_first():
    """A heading may open on the head term it is allowed to rank for and still copy a real
    run further along; breaking at the first window would hide the second."""
    hits = PB.header_precheck(["African Grey Parrot for Sale: What Health Guarantees Come With Every Bird"],
                              {"/y/": ["African Grey Parrot for Sale Arizona"],
                               "/z/": ["Our Promise: What Health Guarantees Come With Every Bird We Place"]})
    assert hits[0]["shingles"][0] == "african grey parrot for sale"
    assert "what health guarantees come with" in hits[0]["shingles"]
    assert hits[0]["shingle"] == hits[0]["shingles"][0]      # the first, kept for compatibility


def test_gate_does_not_exempt_a_heading_that_copies_a_run_beyond_the_head_term():
    b = _approved(MIN_BOARD)
    b["sections"][0]["heading"] = "African Grey Parrot for Sale: What Health Guarantees Come With Every Bird"
    b["approval"]["record_hash"] = PB.record_hash(b)
    live = {"/y/": ["African Grey Parrot for Sale Arizona"],
            "/z/": ["Our Promise: What Health Guarantees Come With Every Bird We Place"]}
    f = [x for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live=live, stage="build")
         if x["check"] == "header-collision"]
    assert len(f) == 1, f


def test_pick_tuple_mismatch_is_a_warn_on_a_nav_section():
    b = _approved(MIN_BOARD)
    b["sections"][0]["shape"] = "nav"
    b["sections"][0]["options"]["pick"] = "toc-t2-chip-cloud#state-chips"
    b["tuple"]["toc"] = "toc-t2-chip-cloud"                  # the stale bare id
    b["approval"]["record_hash"] = PB.record_hash(b)
    f = [x for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={"/y/": ["Something Else Entirely Here Now"]},
                                     stage="build") if x["check"] == "pick-tuple-mismatch"]
    assert len(f) == 1 and f[0]["sev"] == "WARN", f
    b["tuple"]["toc"] = "toc-t2-chip-cloud#state-chips"      # the ids agree
    b["approval"]["record_hash"] = PB.record_hash(b)
    assert [x for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={"/y/": ["Something Else Entirely Here Now"]},
                                        stage="build") if x["check"] == "pick-tuple-mismatch"] == []

# The one heading on the shipped near-me page that genuinely crosses over with a sibling:
# the homepage's "What Health Guarantees Come With Every African Grey We Place?". It is
# asserted rather than popped, so a NEW collision fails this test instead of hiding behind
# a pop list. Fix belongs on the near-me page in a later session.
KNOWN_HOMEPAGE_OVERLAP = "What Health Guarantees Come With Every African Grey We Place?"


def test_near_me_retrofit_board_renders_candidates_and_passes_the_gate(live_dist):
    b = PB.load_board("african-grey-parrots-for-sale-near-me")
    ledger, ont = PB.load_ledger(), PB.load_ontology()
    d = PB.distribution(b)
    assert d["h_counts"] == {"h1": 1, "h2": 9, "h3": 18, "h4": 7, "h5": 7, "h6": 7}
    grid = next(s for s in b["sections"] if s["id"] == "grid")
    cands, excluded = PB.candidates_for(grid["shape"], ledger, slug=b["meta"]["slug"])
    assert cands, "the grid section must have at least one candidate"
    approved = _approved(b)
    live = dict(live_dist)
    live.pop("/african-grey-parrots-for-sale-near-me/", None)          # the board's own page
    for retiring in ("/african-grey-parrot-for-sale-near-me/", "/where-to-buy-african-greys-near-me/"):
        live.pop(retiring, None)                                       # retire in Task 11, 2026-08-10 plan
    for rebuilt in ("/african-grey-parrots-for-sale/", "/african-grey-parrot-for-sale/"):
        live.pop(rebuilt, None)                                        # hub rebuilt, singular retires into it, Task 13
    f = [x for x in PB.gate_findings(approved, ont, ledger, live, stage="build") if x["sev"] == "FAIL"]
    assert [x["check"] for x in f] == ["header-collision"], f
    assert " vs / " in f[0]["msg"] and KNOWN_HOMEPAGE_OVERLAP in f[0]["msg"], f


def test_board_html_carries_every_block_and_the_theme_rules(tmp_path):
    import build_page_board as BPB
    b = _approved(MIN_BOARD)
    ont, ledger = ONT_OK, LEDGER_EMPTY
    html = BPB.render(b, ont, ledger, live={}, thumbs={}, slug="x")
    for marker in ["data-title=\"1. Brief\"", "data-title=\"2. H1\"", "data-title=\"3. Outline\"", "data-title=\"4. Distribution\"",
                   "id=\"entity-graph\"", "data-title=\"6. Component options\"", "data-title=\"7. Asset slots\"", "id=\"approve\""]:
        assert marker in html, marker
    assert ":root{" in html and "prefers-color-scheme: dark" in html and ':root[data-theme="dark"]' in html
    assert "body{margin:0;background:var(--ground)" in html
    assert "claude.use(\"db\")" in html and "boards/x" in html
    assert "<title>Page Board: x</title>" in html


def test_board_html_flags_header_collisions_inline():
    import build_page_board as BPB
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={"/y/": ["What Do We Have for Sale Right Now?"]}, thumbs={}, slug="x")
    assert "exact match with /y/" in html


def test_board_html_shows_standard_sections_with_their_default_and_no_radio(live_dist):
    """A standard section has no choice to make, which is not the same as having no
    component: the board must still show what it gets, or the breeder reads the gap as a
    missing section. Shown, never offered — no radio carries a standard section's id."""
    import build_page_board as BPB
    slug = "african-grey-parrots-for-sale-near-me"
    b = PB.load_board(slug)
    html = BPB.render(b, PB.load_ontology(), PB.load_ledger(), live={}, thumbs={}, slug=slug)
    assert "08 · Near-Me Questions Buyers Ask Us From Every State" in html
    assert "faq-b#map-pin" in html                       # the FAQ shell tuple.faq already names
    assert 'name="pick-faq"' not in html                 # and it is not a choice
    assert BPB.STANDARD_FORM_DEFAULT in html             # 09 reserve → the kit's inquiry form


def test_board_html_escapes_record_text_in_every_context():
    """Record text is breeder- and agent-written, and the board renders it into three
    contexts that each read different characters: HTML, markdown, and the graph's JSON
    inside a <script>. A `</script>` in any of them would end the block and drop the rest
    of the page, so none may survive raw."""
    import re
    import build_page_board as BPB
    b = json.loads(json.dumps(MIN_BOARD))
    b["brief"]["goal"] = "</script><b>x</b>"
    b["sections"][0]["heading"] = "# a | b *c* _d_ </script>"
    html = BPB.render(_approved(b), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")

    assert "&lt;/script&gt;&lt;b&gt;x&lt;/b&gt;" in html          # the goal, escaped
    assert "<b>x</b>" not in html
    assert "\\# a \\| b \\*c\\* \\_d\\_" in html                  # the heading, markdown-neutral
    assert "<\\/script>" in html                                  # the graph label, JSON-escaped
    blocks = re.findall(r'<script type="text/markdown"[^>]*>(.*?)\n</script>', html, re.S)
    assert len(blocks) == 8
    for i, blk in enumerate(blocks):
        assert "</script" not in blk, i


# ---------------------------------------------------------------- canvas artboards

def test_canvas_writes_three_options_two_viewports_per_signature_section(tmp_path):
    import board_canvas as BC
    b = _approved(MIN_BOARD)
    ledger = {"pools": {"inventory": ["avail-a-grid", "avail-b-faceted", "bird-cards-row", "minibird-cards"]}, "pages": {}}
    result = BC.write_canvas(b, ledger, out=tmp_path)
    names = sorted(p.name for p in tmp_path.glob("*.dc.html"))
    assert names == sorted([f"birds--{c}--{vp}.dc.html"
                            for c in ["avail-a-grid", "avail-b-faceted", "bird-cards-row"]
                            for vp in ("Mobile", "Desktop")])
    assert result["counts"] == {"birds": 3} and len(result["files"]) == 6
    assert (tmp_path / "CONTRACT.md").exists() and (tmp_path / "support.js").exists()
    html = (tmp_path / "birds--avail-b-faceted--Desktop.dc.html").read_text()
    assert 'id="root" style="width:1440px' in html and "What Do We Have for Sale Right Now?" in html
    assert "<script src=\"./support.js\"></script>" in html


def test_canvas_copy_comes_only_from_the_record(tmp_path):
    import board_canvas as BC
    b = _approved(MIN_BOARD)
    b["sections"][0]["heading"] = "A Heading That Exists Nowhere Else"
    BC.write_canvas(b, {"pools": {"inventory": ["avail-a-grid"]}, "pages": {}}, out=tmp_path)
    html = (tmp_path / "birds--avail-a-grid--Mobile.dc.html").read_text()
    assert "A Heading That Exists Nowhere Else" in html
    assert "lorem" not in html.lower()


def test_canvas_escapes_record_text_into_the_artboard(tmp_path):
    """Record text is breeder- and agent-written. A `<script>` in a heading that reached an
    artboard raw would run in the canvas editor, not render as the heading it is."""
    import board_canvas as BC
    b = _approved(MIN_BOARD)
    b["sections"][0]["heading"] = "<script>alert(1)</script> & \"quoted\""
    BC.write_canvas(b, {"pools": {"inventory": ["avail-a-grid"]}, "pages": {}}, out=tmp_path)
    html = (tmp_path / "birds--avail-a-grid--Desktop.dc.html").read_text()
    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt; &amp; &quot;quoted&quot;" in html
    assert html.count("<script") == 1                   # the verbatim support.js line, nothing else


def test_canvas_shipping_line_comes_from_the_financial_data(tmp_path):
    """$185 / $350 have moved once already. The canvas reads them from the same file the
    price pages read rather than keeping a second copy that can drift."""
    import json
    import board_canvas as BC
    opts = json.loads(BC.FINANCIAL.read_text(encoding="utf-8"))["purchase_costs"]["delivery_options"]
    BC.write_canvas(_approved(MIN_BOARD), {"pools": {"inventory": ["avail-a-grid"]}, "pages": {}}, out=tmp_path)
    html = (tmp_path / "birds--avail-a-grid--Desktop.dc.html").read_text()
    for key in ("airport_pickup", "home_delivery"):
        assert f'{opts[key]["label"]} {opts[key]["display"]}' in html


def test_canvas_prunes_an_artboard_the_ledger_withdrew(tmp_path):
    """A candidate the pool no longer offers must not survive on disk: a stale artboard
    gets a thumb cut from it and is offered to the breeder as a live option."""
    import board_canvas as BC
    b = _approved(MIN_BOARD)
    BC.write_canvas(b, {"pools": {"inventory": ["avail-a-grid", "avail-b-faceted"]}, "pages": {}}, out=tmp_path)
    assert (tmp_path / "birds--avail-b-faceted--Mobile.dc.html").exists()
    BC.write_canvas(b, {"pools": {"inventory": ["avail-a-grid"]}, "pages": {}}, out=tmp_path)
    assert not (tmp_path / "birds--avail-b-faceted--Mobile.dc.html").exists()
    assert not (tmp_path / "birds--avail-b-faceted--Desktop.dc.html").exists()
    assert (tmp_path / "birds--avail-a-grid--Mobile.dc.html").exists()


def test_canvas_warns_when_a_pool_is_short_or_empty(tmp_path, capsys):
    import board_canvas as BC
    b = _approved(MIN_BOARD)
    result = BC.write_canvas(b, {"pools": {"inventory": []}, "pages": {}}, out=tmp_path)
    assert result["counts"] == {"birds": 0} and result["files"] == []
    assert list(tmp_path.glob("*.dc.html")) == []
    err = capsys.readouterr().err
    assert "birds" in err and "inventory" in err and "0 options" in err


def test_canvas_names_a_refresh_candidate_with_a_plus_and_badges_the_artboard(tmp_path):
    """A `#` in a filename breaks the file:// URL the canvas editor and the thumb cutter
    load, so a refreshed candidate travels as `base+refresh` — and the artboard itself
    says REFRESH, because a placeholder id nobody chose is not a design decision."""
    import board_canvas as BC
    b = _approved(MIN_BOARD)
    b["sections"][0]["id"] = "x"
    b["sections"][0]["shape"] = "nav"                   # a nav section draws from the toc pool
    PB.validate_board(b)                                # every shape here is one the schema allows
    ledger = {"pools": {"toc": ["toc-a", "toc-c"]}, "refresh_pools": ["toc"],
              "pages": {"sib": {"hero": "hero-a", "dial": "dial-1", "rail": "rail-a", "toc": "toc-a",
                                "table": "table-a", "faq": "faq-a", "takeaway": ["k1"], "h6_prefixes": []}}}
    BC.write_canvas(b, ledger, out=tmp_path)
    names = sorted(p.name for p in tmp_path.glob("*.dc.html"))
    assert names == sorted([f"x--{c}--{vp}.dc.html" for c in ("toc-a+refresh", "toc-c")
                            for vp in ("Mobile", "Desktop")])
    assert "REFRESH" in (tmp_path / "x--toc-a+refresh--Mobile.dc.html").read_text()
    assert "REFRESH" not in (tmp_path / "x--toc-c--Mobile.dc.html").read_text()


def test_board_maps_a_thumb_filename_plus_back_to_a_candidate_hash(tmp_path, monkeypatch):
    """The round trip board_canvas.py opens: the candidate `toc-a#refresh` is written
    `toc-a+refresh` on disk, and the board has to key it back or the option renders with
    no thumbnail even though one was cut for it."""
    import build_page_board as BPB
    (tmp_path / "x" / "thumbs").mkdir(parents=True)
    (tmp_path / "x" / "thumbs" / "grid--toc-a+refresh--desktop.png").write_bytes(b"")
    monkeypatch.setattr(BPB, "OUT", tmp_path)
    monkeypatch.setattr(PB, "ROOT", tmp_path)
    monkeypatch.setattr(PB, "DIST", tmp_path / "no-dist")
    monkeypatch.setattr(sys, "argv", ["build_page_board.py", "x"])
    monkeypatch.setattr(PB, "load_board", lambda slug: _approved(MIN_BOARD))
    monkeypatch.setattr(PB, "load_ontology", lambda: ONT_OK)
    monkeypatch.setattr(PB, "load_ledger", lambda: LEDGER_EMPTY)
    captured = {}

    def fake_render(board, ont, ledger, live, thumbs, slug):
        captured["thumbs"] = thumbs
        return "<!doctype html>"

    monkeypatch.setattr(BPB, "render", fake_render)
    BPB.main()
    assert captured["thumbs"] == {("grid", "toc-a#refresh"): "thumbs/grid--toc-a+refresh--desktop.png"}


# --- Task 10: approval read-back, promotions, ledger append, text write-back -------------

def _hub_board(slug="hub-test"):
    b = json.loads(json.dumps(MIN_BOARD))
    b["meta"]["slug"] = slug
    b["meta"]["status"] = "boarded"
    b["sections"][0]["entities"] = ["ont:congo-african-grey", "ont:new-thing"]
    return b


ONT_PROMOTE = {"entities": [
    {"id": "ont:congo-african-grey", "name": "Congo", "aliases": [], "class": "Organism",
     "authorization": "ASSERTED", "source": "x", "owner_page": None},
    {"id": "ont:new-thing", "name": "New", "aliases": [], "class": "Health",
     "authorization": "PROPOSED", "source": "ledger#y", "owner_page": None},
    {"id": "ont:no-source", "name": "NS", "aliases": [], "class": "Health",
     "authorization": "PROPOSED", "source": None, "owner_page": None},
    {"id": "ont:unused-thing", "name": "Unused", "aliases": [], "class": "Health",
     "authorization": "PROPOSED", "source": "ledger#z", "owner_page": None}]}


def test_approve_writes_approval_ledger_and_promotions():
    import board_approve as BA
    b = _hub_board()
    ont = json.loads(json.dumps(ONT_PROMOTE))
    ledger = {"pools": {"inventory": ["avail-b"]}, "pages": {}}
    inbox = {"approved_at": "2026-09-12T12:00:00Z", "h1": 2, "picks": {"birds": "avail-b"},
             "notes": {"birds": "shorter eyebrow"}, "canvas_version": "v7", "record_hash": PB.record_hash(b)}
    out = BA.apply_approval(b, inbox, ont, ledger)
    # Picks and notes ARE hashed content, so the stamped hash is the record the breeder
    # saw WITH their choices in it — every field but record_hash is the inbox verbatim.
    assert {k: v for k, v in out["board"]["approval"].items() if k != "record_hash"} == \
           {k: v for k, v in inbox.items() if k != "record_hash"}
    assert PB.approval_matches(out["board"]) is True
    assert out["board"]["meta"]["status"] == "approved"
    assert out["board"]["h1"]["pick"] == 2
    assert out["board"]["sections"][0]["options"]["pick"] == "avail-b"
    assert out["board"]["sections"][0]["options"]["note"] == "shorter eyebrow"
    assert out["ledger"]["pages"]["hub-test"]["hero"] == "hero-a"
    auth = {e["id"]: e["authorization"] for e in out["ontology"]["entities"]}
    assert auth["ont:new-thing"] == "ASSERTED"          # referenced + sourced
    assert auth["ont:no-source"] == "PROPOSED"          # no source, never promoted
    assert auth["ont:unused-thing"] == "PROPOSED"       # sourced but this page never names it
    assert b["meta"]["status"] == "boarded"             # the caller's record is not mutated


def test_approve_refuses_a_stale_hash():
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    inbox = {"approved_at": "t", "h1": 0, "picks": {}, "notes": {}, "canvas_version": None,
             "record_hash": "f" * 64}
    with pytest.raises(PB.BoardError):
        BA.apply_approval(b, inbox, ONT_OK, LEDGER_EMPTY)


def test_approve_clears_a_note_with_an_empty_string():
    import board_approve as BA
    b = _hub_board()
    b["sections"][0]["options"]["note"] = "an older note"
    inbox = {"approved_at": "t", "h1": 0, "picks": {"birds": "avail-b"}, "notes": {"birds": ""},
             "canvas_version": None, "record_hash": PB.record_hash(b)}
    out = BA.apply_approval(b, inbox, json.loads(json.dumps(ONT_PROMOTE)),
                            {"pools": {"inventory": ["avail-b"]}, "pages": {}})
    assert out["board"]["sections"][0]["options"]["note"] == ""


def test_approve_refuses_an_unrenamed_refresh_placeholder_in_the_tuple():
    import board_approve as BA
    b = _hub_board()
    b["tuple"]["hero"] = "hero-a#refresh"
    inbox = {"approved_at": "t", "h1": 0, "picks": {"birds": "avail-b"}, "notes": {},
             "canvas_version": None, "record_hash": PB.record_hash(b)}
    with pytest.raises(PB.BoardError) as e:
        BA.apply_approval(b, inbox, json.loads(json.dumps(ONT_PROMOTE)),
                          {"pools": {"inventory": ["avail-b"]}, "pages": {}})
    assert "refresh" in str(e.value)


def test_approve_refuses_a_board_whose_signature_section_has_no_pick():
    import board_approve as BA
    b = _hub_board()
    inbox = {"approved_at": "t", "h1": 0, "picks": {}, "notes": {}, "canvas_version": None,
             "record_hash": PB.record_hash(b)}
    with pytest.raises(PB.BoardError) as e:
        BA.apply_approval(b, inbox, json.loads(json.dumps(ONT_PROMOTE)),
                          {"pools": {"inventory": ["avail-b"]}, "pages": {}})
    assert "birds" in str(e.value)


def test_approve_refuses_a_pick_for_a_section_that_does_not_exist():
    import board_approve as BA
    b = _hub_board()
    inbox = {"approved_at": "t", "h1": 0, "picks": {"birds": "avail-b", "ghost": "avail-b"},
             "notes": {}, "canvas_version": None, "record_hash": PB.record_hash(b)}
    with pytest.raises(PB.BoardError) as e:
        BA.apply_approval(b, inbox, json.loads(json.dumps(ONT_PROMOTE)),
                          {"pools": {"inventory": ["avail-b"]}, "pages": {}})
    assert "ghost" in str(e.value)


def test_approve_records_the_ledger_entry_in_the_shape_the_twelve_pages_use():
    """Same eight keys as every existing ledger page, and the H6 prefixes come from the
    record's own H6 nodes — a prefix the page declared but never spent stays free."""
    import board_approve as BA
    b = _hub_board()
    inbox = {"approved_at": "t", "h1": 0, "picks": {"birds": "avail-b"}, "notes": {},
             "canvas_version": None, "record_hash": PB.record_hash(b)}
    out = BA.apply_approval(b, inbox, json.loads(json.dumps(ONT_PROMOTE)),
                            {"pools": {"inventory": ["avail-b"]}, "pages": {}})
    entry = out["ledger"]["pages"]["hub-test"]
    assert sorted(entry) == ["dial", "faq", "h6_prefixes", "hero", "rail", "table", "takeaway", "toc"]
    assert entry["h6_prefixes"] == ["Aviary Note:"]        # declared three, spent one
    assert PB.spent_h6_prefixes(out["ledger"]) == {"Aviary Note:": ["hub-test"]}


def test_text_writeback_updates_the_record_from_the_saved_artboard(tmp_path):
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    b["sections"][0]["options"]["pick"] = "avail-b"
    art = tmp_path / "birds--avail-b--Desktop.dc.html"
    art.write_text('<div id="root"><h2 style="x">What Do We Have for Sale Today?</h2>'
                   '<p>Our birds, today.</p></div>', encoding="utf-8")
    changed = BA.writeback_text(b, tmp_path)
    assert b["sections"][0]["heading"] == "What Do We Have for Sale Today?"
    assert changed == [("birds", "heading", "What Do We Have for Sale Right Now?",
                        "What Do We Have for Sale Today?")]


def test_text_writeback_maps_a_hash_in_the_pick_to_a_plus_in_the_filename(tmp_path):
    """board_canvas.py writes `#` as `+`; a write-back that looked for the `#` spelling
    would silently find no artboard and report no change."""
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    b["sections"][0]["id"] = "grid"
    b["sections"][0]["options"]["pick"] = "toc-t1-numbered-ledger#state-chips"
    (tmp_path / "grid--toc-t1-numbered-ledger+state-chips--Desktop.dc.html").write_text(
        "<h2>Where Do We Ship Each Week?</h2>", encoding="utf-8")
    changed = BA.writeback_text(b, tmp_path)
    assert changed == [("grid", "heading", "What Do We Have for Sale Right Now?",
                        "Where Do We Ship Each Week?")]
    assert b["sections"][0]["heading"] == "Where Do We Ship Each Week?"


def test_approve_main_reads_a_wrapped_inbox_and_writes_all_three_files(tmp_path, monkeypatch):
    """read_db may hand the document back wrapped in {"data": ...}; main() unwraps it and
    writes the board, the ledger and the ontology."""
    import board_approve as BA
    monkeypatch.setattr(PB, "ROOT", tmp_path)
    monkeypatch.setattr(PB, "ONTOLOGY", tmp_path / "data" / "cag-ontology.json")
    monkeypatch.setattr(PB, "LEDGER", tmp_path / "data" / "component-ledger.json")
    b = _hub_board()
    PB.save_board("hub-test", b)
    PB.ONTOLOGY.parent.mkdir(parents=True, exist_ok=True)
    PB.ONTOLOGY.write_text(json.dumps(ONT_PROMOTE), encoding="utf-8")
    PB.LEDGER.write_text(json.dumps({"pools": {"inventory": ["avail-b"]}, "pages": {}}), encoding="utf-8")
    inbox_dir = tmp_path / "data" / "pages" / "hub-test" / "inbox" / "boards"
    inbox_dir.mkdir(parents=True, exist_ok=True)
    (inbox_dir / "hub-test.json").write_text(json.dumps({"data": {
        "approved_at": "2026-09-12T12:00:00Z", "h1": 1, "picks": {"birds": "avail-b"},
        "notes": {}, "canvas_version": None, "record_hash": PB.record_hash(b)}}), encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test"])
    BA.main()
    saved = PB.load_board("hub-test")
    assert saved["meta"]["status"] == "approved" and PB.approval_matches(saved) is True
    assert PB.load_ledger()["pages"]["hub-test"]["hero"] == "hero-a"
    assert {e["id"]: e["authorization"] for e in PB.load_ontology()["entities"]}["ont:new-thing"] == "ASSERTED"


def _approve_main_fixture(tmp_path, monkeypatch, record_hash=None, with_canvas=None):
    """Plant a hub-test board, ledger, ontology and an inbox under a tmp ROOT for main() tests.
    `with_canvas` = (directory, h2 text) writes a Desktop artboard for the birds/avail-b pick."""
    monkeypatch.setattr(PB, "ROOT", tmp_path)
    monkeypatch.setattr(PB, "ONTOLOGY", tmp_path / "data" / "cag-ontology.json")
    monkeypatch.setattr(PB, "LEDGER", tmp_path / "data" / "component-ledger.json")
    b = _hub_board()
    PB.save_board("hub-test", b)
    PB.ONTOLOGY.parent.mkdir(parents=True, exist_ok=True)
    PB.ONTOLOGY.write_text(json.dumps(ONT_PROMOTE), encoding="utf-8")
    PB.LEDGER.write_text(json.dumps({"pools": {"inventory": ["avail-b"]}, "pages": {}}), encoding="utf-8")
    inbox_dir = tmp_path / "data" / "pages" / "hub-test" / "inbox" / "boards"
    inbox_dir.mkdir(parents=True, exist_ok=True)
    (inbox_dir / "hub-test.json").write_text(json.dumps({
        "approved_at": "2026-09-12T12:00:00Z", "h1": 1, "picks": {"birds": "avail-b"},
        "notes": {}, "canvas_version": None,
        "record_hash": record_hash or PB.record_hash(b)}), encoding="utf-8")
    if with_canvas:
        d, h2 = with_canvas
        d.mkdir(parents=True, exist_ok=True)
        (d / "birds--avail-b--Desktop.dc.html").write_text(
            f'<div id="root"><h2 style="x">{h2}</h2></div>', encoding="utf-8")
    return b


def test_approve_main_exits_2_on_a_stale_hash_and_writes_nothing(tmp_path, monkeypatch):
    import board_approve as BA
    _approve_main_fixture(tmp_path, monkeypatch, record_hash="f" * 64)
    before = {p: p.read_text(encoding="utf-8") for p in
              (PB.board_path("hub-test"), PB.LEDGER, PB.ONTOLOGY)}
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test"])
    with pytest.raises(SystemExit) as ex:
        BA.main()
    assert ex.value.code == 2
    for p, text in before.items():
        assert p.read_text(encoding="utf-8") == text, f"{p.name} was written on a refused approval"
    assert PB.load_board("hub-test")["meta"]["status"] != "approved"


def test_approve_main_exits_2_when_the_inbox_is_missing(tmp_path, monkeypatch, capsys):
    import board_approve as BA
    _approve_main_fixture(tmp_path, monkeypatch)
    inbox = tmp_path / "data" / "pages" / "hub-test" / "inbox" / "boards" / "hub-test.json"
    inbox.unlink()
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test"])
    with pytest.raises(SystemExit) as ex:
        BA.main()
    assert ex.value.code == 2
    assert str(inbox) in capsys.readouterr().out


def test_approve_main_defaults_the_canvas_dir_to_docs_design_board_slug(tmp_path, monkeypatch):
    import board_approve as BA
    default = tmp_path / "docs" / "design" / "board-hub-test"
    _approve_main_fixture(tmp_path, monkeypatch, with_canvas=(default, "Birds Heading From the Default Canvas"))
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test"])
    BA.main()
    saved = PB.load_board("hub-test")
    assert saved["sections"][0]["heading"] == "Birds Heading From the Default Canvas"
    assert PB.approval_matches(saved) is True


def test_approve_main_prefers_an_explicit_canvas_dir_over_the_default(tmp_path, monkeypatch):
    import board_approve as BA
    default = tmp_path / "docs" / "design" / "board-hub-test"
    _approve_main_fixture(tmp_path, monkeypatch, with_canvas=(default, "Heading From the Default"))
    other = tmp_path / "elsewhere"
    other.mkdir()
    (other / "birds--avail-b--Desktop.dc.html").write_text(
        '<div id="root"><h2>Heading From the Explicit Dir</h2></div>', encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test", "--canvas-dir", str(other)])
    BA.main()
    assert PB.load_board("hub-test")["sections"][0]["heading"] == "Heading From the Explicit Dir"


# --- Task 10 quality pass: atomic writes, candidate-checked picks, strict write-back -----

def test_approve_refuses_a_pick_that_is_not_on_the_offered_menu():
    import board_approve as BA
    b = _hub_board()
    inbox = {"approved_at": "t", "h1": 0, "picks": {"birds": "avail-z"}, "notes": {},
             "canvas_version": None, "record_hash": PB.record_hash(b)}
    with pytest.raises(PB.BoardError) as e:
        BA.apply_approval(b, inbox, json.loads(json.dumps(ONT_PROMOTE)),
                          {"pools": {"inventory": ["avail-b"]}, "pages": {}})
    assert "birds" in str(e.value) and "avail-z" in str(e.value)


def test_approve_accepts_a_delta_rename_of_an_offered_candidate():
    """The board offers `base` (or `base#refresh`) and the author renames it to the axis
    the option actually varies — `toc-t2-chip-cloud#state-chips` is the shipped hub's own
    pick. A strict membership test would refuse the documented workflow, so the menu is
    matched on the BASE."""
    import board_approve as BA
    b = _hub_board()
    inbox = {"approved_at": "t", "h1": 0, "picks": {"birds": "avail-b#state-chips"}, "notes": {},
             "canvas_version": None, "record_hash": PB.record_hash(b)}
    out = BA.apply_approval(b, inbox, json.loads(json.dumps(ONT_PROMOTE)),
                            {"pools": {"inventory": ["avail-b"]}, "pages": {}})
    assert out["board"]["sections"][0]["options"]["pick"] == "avail-b#state-chips"


def test_writeback_raises_when_the_canvas_dir_does_not_exist(tmp_path):
    """A canvas directory the caller named and that is not there is a typo, not an absence
    of tweaks — returning [] would silently approve the un-tweaked record."""
    import board_approve as BA
    with pytest.raises(PB.BoardError) as e:
        BA.writeback_text(json.loads(json.dumps(MIN_BOARD)), tmp_path / "nope")
    assert "nope" in str(e.value)


def test_writeback_raises_when_an_artboard_carries_two_h2s(tmp_path):
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    b["sections"][0]["options"]["pick"] = "avail-b"
    (tmp_path / "birds--avail-b--Desktop.dc.html").write_text(
        "<h2>First Heading Here</h2><div><h2>Second Heading Here</h2></div>", encoding="utf-8")
    with pytest.raises(PB.BoardError) as e:
        BA.writeback_text(b, tmp_path)
    assert "birds" in str(e.value)
    assert b["sections"][0]["heading"] == "What Do We Have for Sale Right Now?"


def test_writeback_warns_on_a_missing_artboard_and_on_one_without_an_h2(tmp_path, capsys):
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    b["sections"][0]["options"]["pick"] = "avail-b"
    assert BA.writeback_text(b, tmp_path) == []                      # nothing on disk at all
    assert "birds" in capsys.readouterr().err
    (tmp_path / "birds--avail-b--Desktop.dc.html").write_text("<p>no heading</p>", encoding="utf-8")
    assert BA.writeback_text(b, tmp_path) == []
    assert "no <h2>" in capsys.readouterr().err


def test_approve_main_exits_2_and_leaves_the_board_unapproved_when_the_ledger_write_fails(
        tmp_path, monkeypatch):
    """Three documents, one approval: a board stamped approved with no ledger row would
    leave every component it just claimed unowned, and the next page would claim them."""
    import board_approve as BA
    _approve_main_fixture(tmp_path, monkeypatch)
    real_replace = BA.os.replace

    def flaky(src, dst):
        if str(dst).endswith("component-ledger.json"):
            raise OSError("disk full")
        return real_replace(src, dst)

    monkeypatch.setattr(BA.os, "replace", flaky)
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test"])
    with pytest.raises(SystemExit) as ex:
        BA.main()
    assert ex.value.code == 2
    assert PB.load_board("hub-test")["meta"]["status"] != "approved"
    assert PB.load_ledger()["pages"] == {}


def test_approve_main_exits_2_on_a_slug_the_record_disagrees_with(tmp_path, monkeypatch, capsys):
    import board_approve as BA
    b = _approve_main_fixture(tmp_path, monkeypatch)
    b["meta"]["slug"] = "hub-other"
    PB.board_path("hub-test").write_text(json.dumps(b), encoding="utf-8")
    # the hash the inbox carries has to be the hash of the record as it now stands
    inbox = tmp_path / "data" / "pages" / "hub-test" / "inbox" / "boards" / "hub-test.json"
    doc = json.loads(inbox.read_text(encoding="utf-8"))
    doc["record_hash"] = PB.record_hash(b)
    inbox.write_text(json.dumps(doc), encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test"])
    with pytest.raises(SystemExit) as ex:
        BA.main()
    assert ex.value.code == 2
    assert "slug" in capsys.readouterr().out


def test_approve_main_exits_2_when_canvas_dir_has_no_value(tmp_path, monkeypatch):
    import board_approve as BA
    _approve_main_fixture(tmp_path, monkeypatch)
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test", "--canvas-dir"])
    with pytest.raises(SystemExit) as ex:
        BA.main()
    assert ex.value.code == 2


def test_approve_main_takes_the_last_canvas_dir_and_accepts_the_equals_form(tmp_path, monkeypatch):
    import board_approve as BA
    default = tmp_path / "docs" / "design" / "board-hub-test"
    _approve_main_fixture(tmp_path, monkeypatch, with_canvas=(default, "Heading From the Default"))
    first, last = tmp_path / "first", tmp_path / "last"
    for d, h2 in ((first, "Heading From the First Dir"), (last, "Heading From the Last Dir")):
        d.mkdir()
        (d / "birds--avail-b--Desktop.dc.html").write_text(f"<h2>{h2}</h2>", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test",
                                      "--canvas-dir", str(first), f"--canvas-dir={last}"])
    BA.main()
    assert PB.load_board("hub-test")["sections"][0]["heading"] == "Heading From the Last Dir"


def test_approve_main_reports_only_the_promotions_this_run_made(tmp_path, monkeypatch, capsys):
    """ONT_PROMOTE already holds one ASSERTED entity; counting every ASSERTED row would
    report two promotions for a run that made one."""
    import board_approve as BA
    _approve_main_fixture(tmp_path, monkeypatch)
    monkeypatch.setattr(sys, "argv", ["board_approve.py", "hub-test"])
    BA.main()
    assert "1 PROPOSED→ASSERTED" in capsys.readouterr().out

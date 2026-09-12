# Page Board System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **Breeder mandate carried from the for-sale program: page PROSE is written inline by the controlling session, never by a subagent; harness code and data files may be delegated.**

**Goal:** One approval sitting per page on a generated Page Board: `data/pages/<slug>/board.json` is the source of truth, one script renders the board artifact (brief, outline with header check, distribution matrix, entity views, component options, asset slots, an Approve control backed by the artifact database), one script emits canvas options from the outline minus what siblings own, one gate refuses to build without a matching approval. First run: hub C `/african-grey-parrots-for-sale/`.

**Architecture:** Files-first. `scripts/pageboard.py` is one library (load, hash, validate, header pre-check, candidate pools, distribution, authorization). Four thin CLIs sit on it: `build_page_board.py` (board HTML + thumbnails), `board_canvas.py` (artboards), `board_approve.py` (copy the approval back, promote entities, append the ledger, write canvas text tweaks into the record), `board_gate.py` (the gate). The board is an Artifact with the `db` capability; Approve writes `boards/<slug>`; Claude reads it back with the Artifact tool's `read_db` and hands the file to `board_approve.py`.

**Tech Stack:** Python 3 + `jsonschema` (installed 2026-09-12) + pytest · node Playwright (already in `node_modules`) for artboard thumbnails · the `.dc.html` canvas format from `docs/design/homepage-variations-r3/CONTRACT.md` · Cytoscape.js UMD from cdnjs inside the board · the Artifact tool (`capabilities: {db: {}}`, `read_db`, `files`).

**Spec:** `docs/superpowers/specs/2026-09-12-page-board-system-design.md`.

---

## File structure

| File | Responsibility |
|---|---|
| `schemas/board.schema.json` | shape of `data/pages/<slug>/board.json` |
| `schemas/ontology.schema.json` | shape of `data/cag-ontology.json` |
| `schemas/component-ledger.schema.json` | shape of `data/component-ledger.json` |
| `data/cag-ontology.json` | the site ontology, seeded once, grown by approvals |
| `data/component-ledger.json` | the machine-readable component map: shape pools + per-page tuples |
| `data/pages/<slug>/board.json` | one record per boarded page |
| `scripts/pageboard.py` | the library every CLI imports; no I/O side effects beyond reading files |
| `scripts/build_page_board.py` | board.json → `docs/artifacts/boards/<slug>.html` (+ thumbs) |
| `scripts/board_canvas.py` | board.json → `docs/design/board-<slug>/*.dc.html` + `CONTRACT.md` |
| `scripts/board_thumbs.mjs` | artboards → `docs/artifacts/boards/<slug>/thumbs/*.png` |
| `scripts/board_approve.py` | approval file → board.json, ledger, ontology promotions, text write-back |
| `scripts/board_gate.py` | the gate; exit 1 on any failure; prints examined counts |
| `tests/test_page_board.py` | every unit test below plus the near-me end-to-end fixture |
| `data/quality/rule-index.json` | one new row: `page-board-gate` |
| `skills/cag-component-variations.md` + `.claude/skills/cag-component-variations/SKILL.md` | the copy-source adaptation note |

Conventions used throughout: run everything from the repo root `/Users/apple/Downloads/CAG`; every commit ends with `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`; a PostToolUse hook pushes after every Bash call, so commit only when the tests in that task pass.

---

### Task 1: Schemas and the validator

**Files:**
- Create: `schemas/board.schema.json`, `schemas/ontology.schema.json`, `schemas/component-ledger.schema.json`
- Create: `scripts/pageboard.py` (validate + load only, grown in later tasks)
- Test: `tests/test_page_board.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_page_board.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `ModuleNotFoundError: No module named 'pageboard'`

- [ ] **Step 3: Write the three schemas**

```json
// schemas/board.schema.json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CAG Page Board record",
  "type": "object",
  "required": ["meta", "brief", "h1", "sections", "tuple", "assets", "approval"],
  "additionalProperties": false,
  "$defs": {
    "node": {
      "type": "object", "required": ["level", "heading", "intent", "children"], "additionalProperties": false,
      "properties": {
        "level": {"type": "integer", "minimum": 3, "maximum": 6},
        "heading": {"type": "string", "minLength": 1},
        "intent": {"type": "string"},
        "children": {"type": "array", "items": {"$ref": "#/$defs/node"}}
      }
    }
  },
  "properties": {
    "meta": {
      "type": "object", "required": ["slug", "page_type", "status", "research_as_of", "sources"], "additionalProperties": false,
      "properties": {
        "slug": {"type": "string", "pattern": "^[a-z0-9-]+$"},
        "page_type": {"enum": ["hub", "for-sale", "location", "comparison", "blog", "interior", "home"]},
        "status": {"enum": ["draft", "boarded", "approved", "built", "released"]},
        "research_as_of": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
        "sources": {"type": "array", "items": {"type": "object", "required": ["path", "fetched"],
                    "properties": {"path": {"type": "string"}, "fetched": {"type": "string"}}}}
      }
    },
    "brief": {
      "type": "object", "required": ["goal", "scope", "gates", "done", "out_of_scope", "primary_keyword", "strategy"],
      "additionalProperties": false,
      "properties": {
        "goal": {"type": "string"}, "scope": {"type": "string"}, "done": {"type": "string"},
        "gates": {"type": "array", "items": {"type": "string"}},
        "out_of_scope": {"type": "array", "items": {"type": "string"}},
        "primary_keyword": {"type": "string", "minLength": 3},
        "strategy": {"type": "object", "required": ["name", "why", "trade_off"], "additionalProperties": false,
                     "properties": {"name": {"type": "string"}, "why": {"type": "string"}, "trade_off": {"type": "string"}}}
      }
    },
    "h1": {
      "type": "object", "required": ["variants", "recommended", "pick"], "additionalProperties": false,
      "properties": {
        "variants": {"type": "array", "minItems": 5, "maxItems": 5, "items": {"type": "string", "minLength": 1}},
        "recommended": {"type": "integer", "minimum": 0, "maximum": 4},
        "pick": {"type": ["integer", "null"], "minimum": 0, "maximum": 4}
      }
    },
    "sections": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object",
        "required": ["id", "n", "heading", "intent", "category", "framework", "words", "shape", "keywords", "entities", "tree", "images", "options"],
        "additionalProperties": false,
        "properties": {
          "id": {"type": "string", "pattern": "^[a-z][a-z0-9-]*$"},
          "n": {"type": "integer", "minimum": 1},
          "heading": {"type": "string", "minLength": 1},
          "intent": {"type": "string"},
          "category": {"enum": ["A", "B", "C"]},
          "framework": {"enum": ["EEBP", "FAB", "QAB", "PAS", "BAB", "PDB", "AIDA", "EBD", "HSS"]},
          "words": {"type": "object", "required": ["min", "max"], "properties": {"min": {"type": "integer"}, "max": {"type": "integer"}}},
          "shape": {"enum": ["inventory", "compare", "sequence", "proof", "price", "nav", "narrative", "standard"]},
          "keywords": {"type": "object", "required": ["primary", "lsi", "longtail", "brand", "geo"],
                       "additionalProperties": false,
                       "properties": {"primary": {"type": "array", "items": {"type": "string"}}, "lsi": {"type": "array", "items": {"type": "string"}},
                                      "longtail": {"type": "array", "items": {"type": "string"}}, "brand": {"type": "array", "items": {"type": "string"}},
                                      "geo": {"type": "array", "items": {"type": "string"}}}},
          "entities": {"type": "array", "items": {"type": "string", "pattern": "^ont:[a-z0-9-]+$"}},
          "tree": {"type": "array", "items": {"$ref": "#/$defs/node"}},
          "images": {"type": "array", "items": {"type": "object", "required": ["slot", "kind", "required", "prompt"], "additionalProperties": false,
                     "properties": {"slot": {"type": "string"}, "kind": {"enum": ["photo", "infographic"]},
                                    "required": {"type": "boolean"}, "prompt": {"type": "string"}}}},
          "options": {"type": "object", "required": ["candidates", "excluded", "pick", "note"], "additionalProperties": false,
                      "properties": {"candidates": {"type": "array", "items": {"type": "string"}},
                                     "excluded": {"type": "array", "items": {"type": "object", "required": ["component", "owner"],
                                                  "properties": {"component": {"type": "string"}, "owner": {"type": "string"}}}},
                                     "pick": {"type": ["string", "null"]}, "note": {"type": "string"}}}
        }
      }
    },
    "tuple": {
      "type": "object", "required": ["hero", "dial", "rail", "toc", "takeaway", "table", "faq", "h6_prefixes"], "additionalProperties": false,
      "properties": {
        "hero": {"type": "string"}, "dial": {"type": "string"}, "rail": {"type": "string"}, "toc": {"type": "string"},
        "takeaway": {"type": "array", "items": {"type": "string"}}, "table": {"type": "string"}, "faq": {"type": "string"},
        "h6_prefixes": {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": ":$"}}
      }
    },
    "assets": {
      "type": "array",
      "items": {"type": "object", "required": ["slot", "kind", "w", "h", "required", "status", "file", "alt"], "additionalProperties": false,
                "properties": {"slot": {"type": "string"}, "kind": {"enum": ["photo", "infographic"]},
                               "w": {"type": "integer"}, "h": {"type": "integer"}, "required": {"type": "boolean"},
                               "status": {"enum": ["missing", "baked"]}, "file": {"type": ["string", "null"]}, "alt": {"type": "string"}}}
    },
    "approval": {
      "type": ["object", "null"],
      "required": ["approved_at", "h1", "picks", "notes", "canvas_version", "record_hash"], "additionalProperties": false,
      "properties": {
        "approved_at": {"type": "string"}, "h1": {"type": "integer", "minimum": 0, "maximum": 4},
        "picks": {"type": "object", "additionalProperties": {"type": "string"}},
        "notes": {"type": "object", "additionalProperties": {"type": "string"}},
        "canvas_version": {"type": ["string", "null"]},
        "record_hash": {"type": "string", "pattern": "^[0-9a-f]{64}$"}
      }
    }
  }
}
```

```json
// schemas/ontology.schema.json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CAG ontology",
  "type": "object", "required": ["entities"], "additionalProperties": false,
  "properties": {
    "entities": {
      "type": "array",
      "items": {
        "type": "object", "required": ["id", "name", "aliases", "class", "authorization", "source", "owner_page"], "additionalProperties": false,
        "properties": {
          "id": {"type": "string", "pattern": "^ont:[a-z0-9-]+$"},
          "name": {"type": "string", "minLength": 1},
          "aliases": {"type": "array", "items": {"type": "string"}},
          "class": {"enum": ["Organism", "Documentation", "Health", "Commerce", "Logistics", "Place", "People", "Method"]},
          "authorization": {"enum": ["ASSERTED", "PROPOSED", "BLOCKED"]},
          "source": {"type": ["string", "null"]},
          "owner_page": {"type": ["string", "null"]}
        }
      }
    }
  }
}
```

```json
// schemas/component-ledger.schema.json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CAG component ledger",
  "type": "object", "required": ["pools", "pages"], "additionalProperties": false,
  "properties": {
    "pools": {"type": "object", "additionalProperties": {"type": "array", "items": {"type": "string"}}},
    "pages": {
      "type": "object",
      "additionalProperties": {
        "type": "object", "required": ["hero", "dial", "rail", "toc", "takeaway", "table", "faq", "h6_prefixes"], "additionalProperties": false,
        "properties": {
          "hero": {"type": "string"}, "dial": {"type": "string"}, "rail": {"type": "string"}, "toc": {"type": "string"},
          "takeaway": {"type": "array", "items": {"type": "string"}}, "table": {"type": "string"}, "faq": {"type": "string"},
          "h6_prefixes": {"type": "array", "items": {"type": "string"}}
        }
      }
    }
  }
}
```

- [ ] **Step 4: Write the library's validate/load half**

```python
#!/usr/bin/env python3
"""pageboard — the Page Board library. Every board CLI imports this; it reads files and
computes, it never writes a board or publishes anything (the CLIs do).
Spec: docs/superpowers/specs/2026-09-12-page-board-system-design.md
"""
import hashlib, json, pathlib, re
import jsonschema

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
ONTOLOGY = ROOT / "data" / "cag-ontology.json"
LEDGER = ROOT / "data" / "component-ledger.json"
DIST = ROOT / "dist"


class BoardError(Exception):
    """A record that does not describe a buildable page."""


def _validate(doc, schema_name):
    schema = json.loads((SCHEMAS / schema_name).read_text(encoding="utf-8"))
    try:
        jsonschema.validate(doc, schema)
    except jsonschema.ValidationError as e:
        path = "/".join(str(p) for p in e.absolute_path) or "(root)"
        raise BoardError(f"{schema_name}: {path}: {e.message}") from None


def validate_board(board):
    _validate(board, "board.schema.json")


def validate_ontology(ont):
    _validate(ont, "ontology.schema.json")


def validate_ledger(ledger):
    _validate(ledger, "component-ledger.schema.json")


def board_path(slug):
    return ROOT / "data" / "pages" / slug / "board.json"


def load_board(slug):
    p = board_path(slug)
    if not p.exists():
        raise BoardError(f"no board for {slug}: {p} does not exist")
    board = json.loads(p.read_text(encoding="utf-8"))
    validate_board(board)
    return board


def save_board(slug, board):
    validate_board(board)
    p = board_path(slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(board, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_ontology():
    ont = json.loads(ONTOLOGY.read_text(encoding="utf-8"))
    validate_ontology(ont)
    return ont


def load_ledger():
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    validate_ledger(ledger)
    return ledger
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `4 passed`

- [ ] **Step 6: Commit**

```bash
git add schemas/ scripts/pageboard.py tests/test_page_board.py
git commit -m "feat(page-board): schemas for board, ontology and component ledger + the pageboard library's validate/load half

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: Record hash and the edit-after-approval rule

**Files:**
- Modify: `scripts/pageboard.py`
- Test: `tests/test_page_board.py`

- [ ] **Step 1: Write the failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k hash`
Expected: `AttributeError: module 'pageboard' has no attribute 'record_hash'`

- [ ] **Step 3: Implement**

Append to `scripts/pageboard.py`:

```python
def record_hash(board):
    """sha256 of the record with `approval` removed, keys sorted. An edit anywhere else
    changes the hash, which is how a post-approval edit sends the page back to the board."""
    body = {k: v for k, v in board.items() if k != "approval"}
    blob = json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def approval_matches(board):
    a = board.get("approval")
    return bool(a) and a.get("record_hash") == record_hash(board)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `7 passed`

- [ ] **Step 5: Commit**

```bash
git add scripts/pageboard.py tests/test_page_board.py
git commit -m "feat(page-board): record hash and approval_matches

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

> **Review amendment (Task 2 quality review, 2026-09-12):** `record_hash` excludes **lifecycle fields**, not only `approval`: `meta.status` and every asset's `status` and `file`. Approving sets status and baking sets file/status after the hash is taken; hashing them would invalidate every legitimate approval and block release. Tasks 6, 8 and 10 rely on this: `PB.record_hash` is stable across status changes and image baking.

### Task 3: Seed the ontology

**Files:**
- Create: `scripts/seed_ontology.py`
- Create: `data/cag-ontology.json` (generated by the script, committed)
- Test: `tests/test_page_board.py`

The catalog in `skills/cag-entity-agent.md` is a set of markdown tables (`| Primary Entity | Variations | Where to Use |`) under `### Category N — …` headings. Category names map to classes. The Verified-Claim Ledger entries and the BLOCKED family are hand-listed in the script because they carry sources the catalog does not.

- [ ] **Step 1: Write the failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k ontology`
Expected: `FileNotFoundError` on `data/cag-ontology.json`

- [ ] **Step 3: Write the seeder**

```python
#!/usr/bin/env python3
"""seed_ontology.py — build data/cag-ontology.json from the entity catalog
(skills/cag-entity-agent.md) plus the Verified-Claim Ledger. Run once; later growth
comes from board approvals (board_approve.py). Re-running is idempotent: existing ids
keep their authorization and owner_page."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB

CATALOG = PB.ROOT / "skills" / "cag-entity-agent.md"
CLASS_BY_CATEGORY = {"breed": "Organism", "health": "Health", "credential": "Documentation",
                     "location": "Place", "pricing": "Commerce", "buyer": "People", "family": "People"}


def slug(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return "ont:" + s


def catalog_entities():
    out, cls = [], "Documentation"
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^### Category \d+ — (.+)$", line)
        if h:
            key = h.group(1).lower()
            cls = next((v for k, v in CLASS_BY_CATEGORY.items() if k in key), "Documentation")
            continue
        m = re.match(r"^\| ([^|]+) \| ([^|]*) \| ([^|]*) \|$", line)
        if not m or m.group(1).strip() in ("Primary Entity", "---------------") or m.group(1).startswith("-"):
            continue
        name = m.group(1).strip()
        if name.startswith("[") or "$1,200" in name:        # MFS placeholders and the wrong Timneh floor
            continue
        aliases = [a.strip() for a in m.group(2).split(",") if a.strip()]
        out.append({"id": slug(name), "name": name, "aliases": aliases, "class": cls,
                    "authorization": "PROPOSED", "source": None, "owner_page": None})
    return out


# Verified-Claim Ledger: .claude/agents/cag-entity-incorporation-agent.md + docs/reference/credentials.md
LEDGER = [
    ("ont:cites-appendix-i", "CITES Appendix I", ["Appendix I", "CITES A-I"], "Documentation", "credentials.md#cites-compliance"),
    ("ont:captive-bred", "Captive-bred", ["bred in captivity", "domestically bred"], "Documentation", "credentials.md#cites-compliance"),
    ("ont:usda-awa-licence", "USDA AWA licence", ["USDA licensed", "Animal Welfare Act licence"], "Documentation", "credentials.md#usda-awa-license"),
    ("ont:pcr-dna-sexing", "PCR DNA sexing", ["DNA-sexed", "sexing certificate"], "Health", "ledger#pcr-dna-sexing"),
    ("ont:pbfd-screening", "PBFD PCR screening", ["Psittacine Beak and Feather Disease", "PBFD"], "Health", "ledger#pbfd-apv-2026-06-20"),
    ("ont:avian-polyomavirus-screening", "Avian polyomavirus PCR screening", ["APV", "polyomavirus"], "Health", "ledger#pbfd-apv-2026-06-20"),
    ("ont:psittacosis-screening", "Psittacosis screening", ["Chlamydia psittaci", "chlamydiosis"], "Health", "ledger#psittacosis-2026-06-05"),
    ("ont:avian-vet-health-certificate", "Avian veterinary health certificate", ["vet certificate", "health certificate"], "Health", "credentials.md#avian-vet-health-certificate"),
    ("ont:hatch-certificate-closed-band", "Hatch certificate and closed leg band", ["closed band", "band number", "leg band"], "Documentation", "credentials.md#hatch-certificate-band"),
    ("ont:72-hour-guarantee", "72-hour written health guarantee", ["3-day health guarantee", "72-hour guarantee"], "Commerce", "ledger#3-day-guarantee"),
    ("ont:airport-cargo-185", "$185 airport cargo pickup", ["airport pickup", "$185"], "Logistics", "data/price-matrix.json#airport_pickup_display"),
    ("ont:home-delivery-350", "$350 home delivery", ["home delivery", "$350"], "Logistics", "data/price-matrix.json#home_delivery_display"),
    ("ont:flight-nanny", "Cabin flight nanny (quoted per route)", ["flight nanny", "cabin seat"], "Logistics", "data/financial-entities.json#flight_nanny"),
    ("ont:iata-live-animals-regulations", "IATA Live Animals Regulations", ["IATA LAR"], "Logistics", "ledger#shipping"),
    ("ont:delta-cargo", "Delta Cargo", [], "Logistics", "ledger#shipping"),
    ("ont:united-cargo", "United Cargo", [], "Logistics", "ledger#shipping"),
    ("ont:american-airlines-cargo", "American Airlines Cargo", [], "Logistics", "ledger#shipping"),
    ("ont:midland-pickup-radius", "Midland pickup within a 2–3 hour drive", ["collect in person"], "Logistics", "skills/cag-for-sale-page-builder.md#3.5"),
    ("ont:deposit-200", "$200 deposit", ["deposit"], "Commerce", "data/price-matrix.json#deposit_display"),
    ("ont:congo-price-range", "Congo $1,700–$3,500", [], "Commerce", "data/price-matrix.json#congo_african_grey"),
    ("ont:timneh-price-range", "Timneh $1,500–$1,600", [], "Commerce", "data/price-matrix.json#timneh_african_grey"),
    ("ont:aviary-floor-1500", "$1,500 aviary floor price", [], "Commerce", "data/price-matrix.json#timneh_african_grey"),
    ("ont:psittacus-erithacus", "Psittacus erithacus", ["Congo African Grey", "Congo"], "Organism", "ledger#taxonomy"),
    ("ont:psittacus-timneh", "Psittacus timneh", ["Timneh African Grey", "Timneh"], "Organism", "ledger#taxonomy"),
    ("ont:lifespan-40-60", "40–60 year lifespan", [], "Organism", "IUCN 22724813"),
    ("ont:wean-12-16-weeks", "Fully weaned at 12–16 weeks", ["weaned"], "Method", "credentials.md#hand-raised"),
    ("ont:benjamin-home-raising-protocol", "The Benjamin Home-Raising Protocol", [], "Method", "skills/cag-aeo-pass.md#6a"),
    ("ont:midland-socialization-method", "The Midland Socialization Method", [], "Method", "skills/cag-aeo-pass.md#6a"),
    ("ont:uvb-d3", "UV-B lighting and vitamin D3", [], "Health", "ledger#uvb-d3-2026-06-05"),
    ("ont:mark-teri-benjamin", "Mark & Teri Benjamin", ["Mark and Teri Benjamin"], "People", "credentials.md#owners"),
    ("ont:cags-midland-tx", "C.A.Gs – Midland, TX", ["C.A.Gs", "CongoAfricanGreys.com"], "Place", "credentials.md#nap"),
    ("ont:founded-2014", "Founded 2014", ["since 2014"], "People", "credentials.md#founded"),
    ("ont:aav-find-a-vet", "Association of Avian Veterinarians find-a-vet", ["AAV"], "Health", "docs/reference/external-link-library.md"),
    ("ont:aphis-public-search", "APHIS Animal Care public search", [], "Documentation", "credentials.md#usda-awa-license"),
]
BLOCKED = [
    ("ont:wild-caught", "wild-caught"), ("ont:imported-from", "imported from"),
    ("ont:smuggled", "smuggled"), ("ont:undocumented-sale", "undocumented sale"),
]


def main():
    existing = {}
    if PB.ONTOLOGY.exists():
        existing = {e["id"]: e for e in json.loads(PB.ONTOLOGY.read_text(encoding="utf-8"))["entities"]}
    merged = {}
    for e in catalog_entities():
        merged[e["id"]] = e
    for eid, name, aliases, cls, src in LEDGER:
        merged[eid] = {"id": eid, "name": name, "aliases": aliases, "class": cls,
                       "authorization": "ASSERTED", "source": src, "owner_page": None}
    for eid, name in BLOCKED:
        merged[eid] = {"id": eid, "name": name, "aliases": [], "class": "Commerce",
                       "authorization": "BLOCKED", "source": "CLAUDE.md rule 2", "owner_page": None}
    for eid, old in existing.items():                       # idempotent: keep earlier decisions
        if eid in merged and old["authorization"] != "PROPOSED":
            merged[eid]["authorization"] = old["authorization"]
            merged[eid]["source"] = old["source"] or merged[eid]["source"]
        merged[eid]["owner_page"] = old.get("owner_page") if eid in merged else None
        merged.setdefault(eid, old)
    ont = {"entities": sorted(merged.values(), key=lambda e: e["id"])}
    PB.validate_ontology(ont)
    PB.ONTOLOGY.write_text(json.dumps(ont, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {PB.ONTOLOGY.relative_to(PB.ROOT)} — {len(ont['entities'])} entities "
          f"({sum(e['authorization']=='ASSERTED' for e in ont['entities'])} asserted, "
          f"{sum(e['authorization']=='BLOCKED' for e in ont['entities'])} blocked)")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the seeder, then the tests**

Run: `python3 scripts/seed_ontology.py && python3 -m pytest tests/test_page_board.py -q`
Expected: `wrote data/cag-ontology.json — N entities (34 asserted, 4 blocked)` then `10 passed`. If a catalog row breaks the slug pattern, the validator names the entity; fix the `slug()` input, never the schema.

- [ ] **Step 5: Commit**

```bash
git add scripts/seed_ontology.py data/cag-ontology.json tests/test_page_board.py
git commit -m "feat(page-board): seed data/cag-ontology.json from the entity catalog and the Verified-Claim Ledger

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 4: The component ledger as data

**Files:**
- Create: `data/component-ledger.json` (hand-written from `sessions/2026-07-19-for-sale-component-map.md` §"Measured inventory" and tuples 11–12; the markdown stays as the human view)
- Modify: `scripts/pageboard.py` (candidate pools)
- Test: `tests/test_page_board.py`

- [ ] **Step 1: Write the failing tests**

```python
def test_ledger_file_validates_and_knows_pages_a_and_b():
    ledger = PB.load_ledger()
    assert ledger["pages"]["buy-african-grey-parrots-with-shipping"]["toc"] == "toc-t3-boarding-pass"
    assert ledger["pages"]["african-grey-parrots-for-sale-near-me"]["hero"] == "hero-c-mosaic-metrics"


def test_candidates_subtract_what_siblings_own():
    ledger = {"pools": {"inventory": ["avail-a", "avail-b", "bird-cards"]},
              "pages": {"dna-tested-african-grey-for-sale": {"hero": "hero-c", "dial": "dial-1", "rail": "rail-a", "toc": "avail-b",
                        "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    cands, excluded = PB.candidates_for("inventory", ledger, slug="african-grey-parrots-for-sale")
    assert cands == ["avail-a", "bird-cards"]
    assert excluded == [{"component": "avail-b", "owner": "dna-tested-african-grey-for-sale"}]


def test_candidates_never_exclude_the_page_itself():
    ledger = {"pools": {"nav": ["dial-1", "dial-2"]},
              "pages": {"x": {"hero": "", "dial": "dial-1", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "", "h6_prefixes": []}}}
    cands, excluded = PB.candidates_for("nav", ledger, slug="x")
    assert cands == ["dial-1", "dial-2"] and excluded == []


def test_standard_shape_has_no_options():
    cands, excluded = PB.candidates_for("standard", {"pools": {}, "pages": {}}, slug="x")
    assert cands == [] and excluded == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "ledger or candidates or standard"`
Expected: `FileNotFoundError` for the ledger and `AttributeError: candidates_for`

- [ ] **Step 3: Write the ledger file**

```json
{
  "pools": {
    "inventory": ["avail-a-grid", "avail-b-faceted", "bird-cards-row", "minibird-cards"],
    "compare":   ["table-a-stacking", "table-b-spine-cards", "table-e-ledger", "verdict-cards", "tab-toggle"],
    "sequence":  ["toc-t5-reserve-stepper", "timeline-strip", "numbered-ledger"],
    "proof":     ["k1-receipt", "k4-clipboard", "lab-report-table", "doc-stack"],
    "price":     ["k2-price-tag", "k1-receipt", "compact-price-table", "table-h-price-ladder"],
    "nav":       ["dial-1-clay", "dial-2-dark-aviary", "rail-a-price-chip", "rail-b-green-ticker",
                  "toc-t1-numbered-ledger", "toc-t2-chip-cloud", "toc-t3-boarding-pass", "toc-t4-magazine-index", "toc-t5-reserve-stepper"],
    "narrative": ["h3-image-first", "split-feature", "quote-band"],
    "hero":      ["hero-a-scattered-flock", "hero-c-mosaic-metrics", "split-hero-a-trust-ribbon", "split-hero-b-warm-gradient", "split-hero-c-dark-grid"],
    "counter":   ["counter-outlined-cards", "counter-ledger-strip", "counter-capsules"],
    "takeaway":  ["k1-receipt", "k2-price-tag", "k3-green-ledger", "k4-clipboard", "k5-capsule"],
    "faq":       ["faq-a", "faq-b", "faq-c"]
  },
  "pages": {
    "african-grey-parrot-bird-eggs-for-sale-usa": {"hero": "split-hero-c-dark-grid", "dial": "dial-1-clay", "rail": "rail-a-price-chip", "toc": "dial-1-clay", "takeaway": ["k1-receipt", "k5-capsule"], "table": "table-a-stacking", "faq": "faq-c", "h6_prefixes": []},
    "congo-african-grey-for-sale": {"hero": "split-hero-b-warm-gradient", "dial": "dial-2-dark-aviary", "rail": "rail-a-price-chip", "toc": "toc-t5-reserve-stepper", "takeaway": ["k1-receipt", "k4-clipboard", "k3-green-ledger"], "table": "table-a-stacking", "faq": "faq-a", "h6_prefixes": []},
    "timneh-african-grey-for-sale": {"hero": "split-hero-b-warm-gradient", "dial": "dial-1-clay", "rail": "rail-b-green-ticker", "toc": "toc-t1-numbered-ledger", "takeaway": ["k2-price-tag", "k3-green-ledger", "k5-capsule"], "table": "table-a-stacking", "faq": "faq-b", "h6_prefixes": []},
    "hand-raised-african-grey-parrot-for-sale": {"hero": "hero-a-scattered-flock", "dial": "dial-2-dark-aviary", "rail": "rail-b-green-ticker", "toc": "toc-t4-magazine-index", "takeaway": ["k3-green-ledger"], "table": "table-c", "faq": "faq-a", "h6_prefixes": ["Breeder Note:", "Citation:"]},
    "african-greys-for-sale-with-health-guarantee": {"hero": "split-hero-a-trust-ribbon", "dial": "dial-1-clay", "rail": "rail-a-price-chip", "toc": "toc-t4-magazine-index", "takeaway": ["k5-capsule"], "table": "table-e-ledger", "faq": "faq-a", "h6_prefixes": ["In Writing:", "From the Vet:", "On File:"]},
    "dna-tested-african-grey-for-sale": {"hero": "hero-c-mosaic-metrics", "dial": "dial-1-clay", "rail": "rail-a-price-chip", "toc": "toc-t2-chip-cloud", "takeaway": ["k4-clipboard", "k5-capsule"], "table": "table-a-stacking", "faq": "faq-c", "h6_prefixes": ["From the Lab:", "On the Record:"]},
    "baby-african-grey-parrot-for-sale": {"hero": "split-hero-b-warm-gradient", "dial": "dial-1-clay", "rail": "rail-a-price-chip", "toc": "toc-t5-reserve-stepper", "takeaway": ["k3-green-ledger", "k4-clipboard"], "table": "table-a-stacking", "faq": "faq-b", "h6_prefixes": ["At Week N:", "From the Nursery:", "Weaning Log:"]},
    "african-grey-parrot-adoption-cost": {"hero": "split-hero-c-dark-grid", "dial": "dial-1-clay", "rail": "rail-a-price-chip", "toc": "toc-t1-numbered-ledger", "takeaway": ["k4-clipboard"], "table": "table-a-stacking", "faq": "faq-c", "h6_prefixes": ["Line Item:", "From the Ledger:", "Receipt Note:"]},
    "congo-african-grey-parrot-pair-for-sale": {"hero": "hero-a-scattered-flock", "dial": "dial-1-clay", "rail": "rail-a-price-chip", "toc": "toc-t1-numbered-ledger", "takeaway": ["k1-receipt", "k5-capsule"], "table": "table-a-stacking", "faq": "faq-b", "h6_prefixes": ["Before You Commit:", "From the Aviary:", "Two-Bird Note:"]},
    "african-grey-breeding-pair-for-sale": {"hero": "hero-a-scattered-flock", "dial": "dial-1-clay", "rail": "rail-b-green-ticker", "toc": "toc-t1-numbered-ledger", "takeaway": ["k3-green-ledger", "k5-capsule"], "table": "table-a-stacking", "faq": "faq-a", "h6_prefixes": ["Breeder's Note:", "Clutch Record:", "From the Nest Box:"]},
    "buy-african-grey-parrots-with-shipping": {"hero": "split-hero-a-trust-ribbon", "dial": "dial-2-dark-aviary", "rail": "rail-b-green-ticker", "toc": "toc-t3-boarding-pass", "takeaway": ["k1-receipt", "k4-clipboard"], "table": "table-h-price-ladder", "faq": "faq-a", "h6_prefixes": ["Price Check:", "On the Paperwork:", "What We Measured:"]},
    "african-grey-parrots-for-sale-near-me": {"hero": "hero-c-mosaic-metrics", "dial": "dial-1-clay", "rail": "rail-b-green-ticker", "toc": "toc-t2-chip-cloud", "takeaway": ["k3-green-ledger", "k4-clipboard", "k5-capsule"], "table": "table-i-distance-ledger", "faq": "faq-b", "h6_prefixes": ["Distance Note:", "From Midland:", "Ask Before You Drive:"]}
  }
}
```

- [ ] **Step 4: Implement `candidates_for`**

Append to `scripts/pageboard.py`:

```python
# A ledger page "owns" every component named anywhere in its tuple. A hero, dial, rail,
# TOC, table, FAQ shell or takeaway a sibling owns is removed from the pool; the record
# keeps who owned it so the board can say so. The page itself never excludes itself.
def owned_components(ledger, exclude_slug=None):
    owned = {}
    for page, t in ledger.get("pages", {}).items():
        if page == exclude_slug:
            continue
        for key in ("hero", "dial", "rail", "toc", "table", "faq"):
            if t.get(key):
                owned.setdefault(t[key], page)
        for k in t.get("takeaway", []):
            owned.setdefault(k, page)
    return owned


def candidates_for(shape, ledger, slug):
    if shape == "standard":
        return [], []
    pool = list(ledger.get("pools", {}).get(shape, []))
    owned = owned_components(ledger, exclude_slug=slug)
    cands = [c for c in pool if c not in owned]
    excluded = [{"component": c, "owner": owned[c]} for c in pool if c in owned]
    return cands, excluded


def spent_h6_prefixes(ledger, exclude_slug=None):
    out = {}
    for page, t in ledger.get("pages", {}).items():
        if page == exclude_slug:
            continue
        for p in t.get("h6_prefixes", []):
            out.setdefault(p, page)
    return out
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `14 passed`

- [ ] **Step 6: Commit**

```bash
git add data/component-ledger.json scripts/pageboard.py tests/test_page_board.py
git commit -m "feat(page-board): component ledger as data + candidate pools minus what siblings own

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

> **Review amendment (Task 4 self-review, 2026-09-12): refreshed components.** Twelve ledger pages already own every hero, takeaway, FAQ and nav shell, so a bare pool subtraction leaves a new page an empty menu. The cluster's practice is a **refresh**: a spent shell reused along a named axis (near-me's `hero-c-mosaic-metrics#geo-tile-field`, its `toc-t2-chip-cloud#state-chips`, its `faq-b#map-pin`). Component ids are therefore `base` or `base#delta`. Rules every later task inherits:
> - `owned_components` keys ownership by the **full id and by its base**; `candidates_for` returns, in pool order, every free base as itself and every owned base as `base#refresh` (a placeholder the board author renames to `base#<delta>` in the tuple). A non-empty pool never yields an empty candidate list; `excluded` still names the owner of each owned base.
> - The gate's `ledger-owned-combo` fails only on an **exact** full-id match with a sibling, or on a bare base that a sibling owns as a base or as any refresh. `base#<new-delta>` passes when no sibling uses that exact id.
> - Canvas templates select on `cand.split("#")[0]`; the board's option card shows the delta (or "refresh: name the axis") as a badge.
> - The ledger records refreshed ids where the markdown map does: near-me hero/toc/faq, buy-with-shipping hero (`split-hero-a-trust-ribbon#price-chips`) and faq (`faq-a#price-chip`), adoption-cost toc (`toc-t1-numbered-ledger#t1m`), baby hero (`split-hero-b-warm-gradient#baby-refresh`).

### Task 5: Header pre-check, authorization check, distribution

**Files:**
- Modify: `scripts/pageboard.py`
- Test: `tests/test_page_board.py`

The header pre-check reuses the dup auditor's tokeniser (`re.findall(r"[a-z0-9$']+", text.lower())`) so a heading matches the way the dup gate will judge it later, and its species-template rule (`SPECIES_TOKENS`) so "Is a Macaw Right for You?" collides with "Is a Cockatoo Right for You?".

- [ ] **Step 1: Write the failing tests**

```python
def test_all_headings_walks_the_tree_in_order():
    hs = PB.all_headings(MIN_BOARD)
    assert hs[0] == (2, "What Do We Have for Sale Right Now?")
    assert hs[-1] == (6, "Aviary Note: Read the Card")
    assert [lvl for lvl, _ in hs] == [2, 3, 4, 5, 6]


def test_header_precheck_finds_exact_and_shingle_matches(tmp_path):
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "headings or precheck or authorization or distribution"`
Expected: `AttributeError` on each missing function

- [ ] **Step 3: Implement**

Append to `scripts/pageboard.py`:

```python
TOKEN = re.compile(r"[a-z0-9$']+")
SPECIES = re.compile(r"\b(congo|timneh|macaw|cockatoo|amazon(?: parrot)?|eclectus|african grey|grey)\b")
SHINGLE = 5


def tokens(text):
    return TOKEN.findall(text.lower())


def all_headings(board):
    """(level, text) in render order: H2 then its tree, depth-first."""
    out = []

    def walk(nodes):
        for n in nodes:
            out.append((n["level"], n["heading"]))
            walk(n.get("children", []))
    for s in board["sections"]:
        out.append((2, s["heading"]))
        walk(s["tree"])
    return out


def live_headings(dist=DIST):
    """{page: [heading text, ...]} from every built page. Empty when dist/ is absent."""
    hpat = re.compile(r"<h([1-6])[^>]*>(.*?)</h\1>", re.S | re.I)
    strip = re.compile(r"<[^>]+>")
    import html as _h
    out = {}
    for page in sorted(pathlib.Path(dist).glob("**/index.html")):
        slug = "/" + page.parent.relative_to(dist).as_posix().strip(".") + "/"
        out[slug] = [_h.unescape(re.sub(r"\s+", " ", strip.sub("", raw)).strip()) for _, raw in hpat.findall(page.read_text(errors="ignore"))]
    return out


def header_precheck(proposed, live):
    """Every proposed heading that collides with a live one: exact, template (species
    swapped) or 5-token shingle. `live` is {page: [heading, ...]}."""
    exact, templ, shingles = {}, {}, {}
    for page, hs in live.items():
        for h in hs:
            t = " ".join(tokens(h))
            if not t:
                continue
            exact.setdefault(t, page)
            templ.setdefault(SPECIES.sub("{species}", t), page)
            ws = tokens(h)
            for i in range(len(ws) - SHINGLE + 1):
                shingles.setdefault(" ".join(ws[i:i + SHINGLE]), (page, h))
    hits = []
    for h in proposed:
        ws = tokens(h)
        t = " ".join(ws)
        if t in exact:
            hits.append({"heading": h, "kind": "exact", "page": exact[t], "with": h}); continue
        tt = SPECIES.sub("{species}", t)
        if tt in templ:
            hits.append({"heading": h, "kind": "template", "page": templ[tt], "with": tt}); continue
        for i in range(len(ws) - SHINGLE + 1):
            key = " ".join(ws[i:i + SHINGLE])
            if key in shingles:
                page, with_ = shingles[key]
                hits.append({"heading": h, "kind": "shingle", "page": page, "with": with_}); break
    return hits


def authorization_check(board, ont):
    by_id = {e["id"]: e for e in ont["entities"]}
    used = []
    for s in board["sections"]:
        for eid in s["entities"]:
            if eid not in used:
                used.append(eid)
    return {
        "blocked": [e for e in used if e in by_id and by_id[e]["authorization"] == "BLOCKED"],
        "proposed": [e for e in used if e in by_id and by_id[e]["authorization"] == "PROPOSED"],
        "unknown": [e for e in used if e not in by_id],
    }


def distribution(board):
    rows, totals = [], {"primary": 0, "lsi": 0, "longtail": 0, "brand": 0, "geo": 0, "words_min": 0, "words_max": 0}
    for s in board["sections"]:
        row = {"section": s["id"], "heading": s["heading"]}
        for k in ("primary", "lsi", "longtail", "brand", "geo"):
            row[k] = len(s["keywords"][k]); totals[k] += row[k]
        row["words_min"], row["words_max"] = s["words"]["min"], s["words"]["max"]
        totals["words_min"] += row["words_min"]; totals["words_max"] += row["words_max"]
        rows.append(row)
    counts = {f"h{n}": 0 for n in range(2, 7)}
    for lvl, _ in all_headings(board):
        counts[f"h{lvl}"] += 1
    return {"rows": rows, "totals": totals, "h_counts": counts}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `19 passed`

- [ ] **Step 5: Commit**

```bash
git add scripts/pageboard.py tests/test_page_board.py
git commit -m "feat(page-board): header pre-check (exact, template, shingle), authorization check, distribution

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

> **Review amendment (Task 5 quality review, 2026-09-12):** `live_headings` builds its corpus the way `dup_content_audit.py` does (skips `SKIP_TAGS` and `CHROME_RE` chrome), `header_precheck(proposed, live, exclude_page=None)` drops the page's own key, and `all_headings` begins with `(1, <picked H1>)` so `h_counts` carries `"h1"`. The gate additionally drops any hit whose heading contains a `dup_content_audit.HEADER_WHITELIST` phrase (import it: `from dup_content_audit import HEADER_WHITELIST`).

### Task 6: The gate

**Files:**
- Create: `scripts/board_gate.py`
- Modify: `scripts/pageboard.py` (a pure `gate_findings` the CLI prints)
- Modify: `data/quality/rule-index.json`
- Test: `tests/test_page_board.py`

- [ ] **Step 1: Write the failing tests**

```python
def _approved(board):
    b = json.loads(json.dumps(board))
    b["options_pick_all"] = None
    del b["options_pick_all"]
    for s in b["sections"]:
        if s["shape"] != "standard":
            s["options"]["pick"] = s["options"]["candidates"][0] if s["options"]["candidates"] else "default"
    b["approval"] = {"approved_at": "2026-09-12T10:00:00Z", "h1": 0, "picks": {s["id"]: s["options"]["pick"] for s in b["sections"]},
                     "notes": {}, "canvas_version": None, "record_hash": PB.record_hash(b)}
    b["meta"]["status"] = "approved"
    return b


ONT_OK = {"entities": [{"id": "ont:congo-african-grey", "name": "Congo", "aliases": [], "class": "Organism",
                        "authorization": "ASSERTED", "source": "x", "owner_page": None}]}
LEDGER_EMPTY = {"pools": {"inventory": ["avail-b"]}, "pages": {}}


def test_gate_passes_an_approved_minimal_board():
    b = _approved(MIN_BOARD)
    f = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")
    assert [x for x in f if x["sev"] == "FAIL"] == [], f


def test_gate_fails_without_matching_approval():
    b = _approved(MIN_BOARD)
    b["sections"][0]["intent"] = "edited after approval"
    f = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")
    assert any(x["check"] == "approval-hash" and x["sev"] == "FAIL" for x in f)


def test_gate_fails_on_blocked_entity_and_owned_combo_and_spent_prefix():
    b = _approved(MIN_BOARD)
    b["sections"][0]["entities"].append("ont:wild-caught")
    ont = {"entities": ONT_OK["entities"] + [{"id": "ont:wild-caught", "name": "w", "aliases": [], "class": "Commerce",
                                              "authorization": "BLOCKED", "source": "r2", "owner_page": None}]}
    ledger = {"pools": {"inventory": ["avail-b"]},
              "pages": {"sibling": {"hero": "hero-a", "dial": "", "rail": "", "toc": "", "takeaway": [], "table": "", "faq": "",
                                    "h6_prefixes": ["Aviary Note:"]}}}
    b["approval"]["record_hash"] = PB.record_hash(b)
    f = {x["check"] for x in PB.gate_findings(b, ont, ledger, live={}, stage="build") if x["sev"] == "FAIL"}
    assert {"entity-blocked", "ledger-owned-combo", "ledger-spent-prefix"} <= f


def test_gate_fails_on_live_header_collision_and_missing_pick():
    b = _approved(MIN_BOARD)
    b["sections"][0]["options"]["pick"] = None
    b["approval"]["picks"] = {}
    b["approval"]["record_hash"] = PB.record_hash(b)
    live = {"/x/": ["What Do We Have for Sale Right Now?"]}
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k gate`
Expected: `AttributeError: gate_findings`

- [ ] **Step 3: Implement `gate_findings` and the CLI**

Append to `scripts/pageboard.py`:

```python
ADVISORY_MIN_H5H6 = {"home", "location"}          # rules/headings.md, 2026-09-09


def gate_findings(board, ont, ledger, live, stage="build"):
    """Every reason this record may not be built (or released). Pure: no printing."""
    f = []
    slug = board["meta"]["slug"]
    add = lambda check, sev, msg: f.append({"check": check, "sev": sev, "msg": msg})

    if not approval_matches(board):
        add("approval-hash", "FAIL", "no approval, or the record changed after it was approved — board it again")

    auth = authorization_check(board, ont)
    for e in auth["blocked"]:
        add("entity-blocked", "FAIL", f"{e} is BLOCKED (CLAUDE.md rule 2)")
    for e in auth["unknown"]:
        add("entity-unknown", "WARN", f"{e} is not in data/cag-ontology.json")
    for e in auth["proposed"]:
        add("entity-proposed", "WARN", f"{e} is PROPOSED — needs a source before it can be asserted")

    owned = owned_components(ledger, exclude_slug=slug)
    t = board["tuple"]
    for key in ("hero", "dial", "rail", "toc", "table", "faq"):
        if t.get(key) in owned:
            add("ledger-owned-combo", "FAIL", f"tuple.{key}={t[key]} is owned by {owned[t[key]]}")
    for k in t.get("takeaway", []):
        if k in owned:
            add("ledger-owned-combo", "FAIL", f"takeaway {k} is owned by {owned[k]}")
    spent = spent_h6_prefixes(ledger, exclude_slug=slug)
    for p in t.get("h6_prefixes", []):
        if p in spent:
            add("ledger-spent-prefix", "FAIL", f"H6 prefix {p!r} is spent by {spent[p]}")

    hits = [h for h in header_precheck([h for _, h in all_headings(board)], live, exclude_page="/" + slug + "/")
            if not any(w in h["heading"].lower() for w in HEADER_WHITELIST)]   # dup_content_audit.HEADER_WHITELIST
    for h in hits:
        add("header-collision", "FAIL", f"{h['kind']}: {h['heading']!r} vs {h['page']} {h['with']!r}")

    counts = distribution(board)["h_counts"]
    if counts["h5"] < 5 or counts["h6"] < 5:
        sev = "WARN" if board["meta"]["page_type"] in ADVISORY_MIN_H5H6 else "FAIL"
        add("min-h5-h6", sev, f"H5 {counts['h5']} / H6 {counts['h6']} — floor is 5 each")

    picks = (board.get("approval") or {}).get("picks", {})
    for s in board["sections"]:
        if s["shape"] != "standard" and not (s["options"]["pick"] or picks.get(s["id"])):
            add("signature-no-pick", "FAIL", f"section {s['id']} ({s['shape']}) has no component pick")

    if stage == "release":
        for a in board["assets"]:
            if a["required"] and a["status"] != "baked":
                add("asset-required-missing", "FAIL", f"required slot {a['slot']} ({a['kind']} {a['w']}x{a['h']}) is {a['status']}")
    return f
```

```python
#!/usr/bin/env python3
"""board_gate.py <slug> [--release]
The Page Board gate: refuses to build (or release) a page whose board.json is not
approved as it stands. Reads live headings from dist/ (build first). Exit 1 on any FAIL.
Prints its examined counts — a gate that examines nothing is not a pass
(skills/cag-gate-integrity.md)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit("usage: board_gate.py <slug> [--release]")
    slug, stage = args[0], ("release" if "--release" in sys.argv else "build")
    board = PB.load_board(slug)
    ont, ledger = PB.load_ontology(), PB.load_ledger()
    live = PB.live_headings() if PB.DIST.exists() else {}
    if not live:
        print("WARN header pre-check examined 0 live pages — run `npx astro build` first")
    f = PB.gate_findings(board, ont, ledger, live, stage=stage)
    n_head = len(PB.all_headings(board))
    print(f"board-gate {slug} [{stage}] — {len(board['sections'])} sections, {n_head} headings, "
          f"{len(live)} live pages, {sum(len(s['entities']) for s in board['sections'])} entity refs examined")
    for x in f:
        print(f"  {x['sev']:4s} {x['check']:24s} {x['msg']}")
    fails = [x for x in f if x["sev"] == "FAIL"]
    print(f"{len(fails)} FAIL · {len(f) - len(fails)} WARN")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `25 passed`

- [ ] **Step 5: Register the rule**

Append to the `rules` array in `data/quality/rule-index.json`:

```json
{
  "id": "page-board-gate",
  "family": "GATE",
  "enforced": "test",
  "test": "tests/test_page_board.py",
  "severity": "blocking",
  "why_blocking": "A page built from an unapproved or edited-after-approval board is the exact rework the Board-First workflow exists to stop (8 post-build rejections vs 0 after canvas picks). scripts/board_gate.py exits 1; the build step must not run without it."
}
```

Run: `python3 scripts/quality_report.py | grep -A2 "5. RULES"`
Expected: no `BROKEN test link` line.

- [ ] **Step 6: Commit**

```bash
git add scripts/pageboard.py scripts/board_gate.py data/quality/rule-index.json tests/test_page_board.py
git commit -m "feat(page-board): board_gate.py — approval hash, blocked entities, ledger collisions, header collisions, picks, release slots

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 7: The near-me page as a retro-fitted board (end-to-end fixture)

**Files:**
- Create: `data/pages/african-grey-parrots-for-sale-near-me/board.json`
- Test: `tests/test_page_board.py`

This proves the model can express a real shipped page. Headings are the shipped ones (`sessions/2026-08-10-two-pages-outline-gate.md` PAGE B, with the two later corrections: "The Companion Pair", and the reserved H6 prefixes). Because the page is live, the header pre-check against `dist/` will match its own headings; the fixture test passes `live` with the page's own slug removed, and the gate CLI does the same for `meta.slug` (add that one line to `board_gate.py`: `live.pop("/" + slug + "/", None)`).

- [ ] **Step 1: Write the failing test**

```python
def test_near_me_retrofit_board_renders_candidates_and_passes_the_gate():
    b = PB.load_board("african-grey-parrots-for-sale-near-me")
    ledger, ont = PB.load_ledger(), PB.load_ontology()
    d = PB.distribution(b)
    assert d["h_counts"] == {"h1": 1, "h2": 9, "h3": 18, "h4": 7, "h5": 7, "h6": 7}
    grid = next(s for s in b["sections"] if s["id"] == "grid")
    cands, excluded = PB.candidates_for(grid["shape"], ledger, slug=b["meta"]["slug"])
    assert cands, "the grid section must have at least one candidate"
    approved = _approved(b)
    live = PB.live_headings() if PB.DIST.exists() else {}
    live.pop("/african-grey-parrots-for-sale-near-me/", None)
    f = [x for x in PB.gate_findings(approved, ont, ledger, live, stage="build") if x["sev"] == "FAIL"]
    assert f == [], f
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_page_board.py -q -k retrofit`
Expected: `BoardError: no board for african-grey-parrots-for-sale-near-me`

- [ ] **Step 3: Write the fixture**

```json
{
  "meta": {"slug": "african-grey-parrots-for-sale-near-me", "page_type": "for-sale", "status": "released",
           "research_as_of": "2026-08-10",
           "sources": [{"path": "sessions/for-sale-research/african-grey-parrots-for-sale-near-me/2026-08-10-sprint0.md", "fetched": "2026-08-10"},
                       {"path": "docs/research/for-sale-keywords-2026-07.md", "fetched": "2026-07-16"},
                       {"path": "docs/research/competitor-sweep-page3-2026-08-09.md", "fetched": "2026-08-09"}]},
  "brief": {"goal": "Rebuild the page as the for-sale cluster's geo router: catch the near-me query variance and hand the buyer to one of 40 state and metro pages.",
            "scope": "The page and its images. Sole enumeration of the grid sitewide.",
            "gates": ["hardening", "seam", "dup-body", "dup-headers", "evidence", "aeo", "final-page-audit", "render-meta", "render-pages", "live-200", "indexnow"],
            "done": "Every gate clean or explained, deployed on main, IndexNow 200, gate report as Artifact + .md.",
            "out_of_scope": ["the hub", "the three near-me 301s"],
            "primary_keyword": "african grey parrots for sale near me",
            "strategy": {"name": "B-3 Router With a Reason", "why": "7 of 9 ranking URLs are geo-scoped; the grid must be high; the thin near-me page at 8.74 took 0 clicks on 109 impressions.", "trade_off": "Every word above the grid delays the routing click; the opener stays short."}},
  "h1": {"variants": ["African Grey Parrots for Sale Near You — Find Your State, Not a Classified Ad",
                      "African Grey Parrots for Sale Near Me: Start With Your State",
                      "Looking for African Greys for Sale Near You? Here Is Every State We Serve",
                      "African Grey and African Gray Parrots for Sale Near You, State by State",
                      "African Grey Parrots for Sale Near You — Thirty-Nine Pages, One Aviary"], "recommended": 0, "pick": 0},
  "sections": [
    {"id": "search", "n": 1, "heading": "What Does “African Grey Parrot for Sale Near Me” Actually Return?", "intent": "Honest-radius opener: the search returns shops and classifieds; a breeder is hours away.", "category": "C", "framework": "BAB", "words": {"min": 350, "max": 500}, "shape": "narrative",
     "keywords": {"primary": ["african grey parrot for sale near me"], "lsi": ["african gray parrot for sale near me", "african grey breeders near me"], "longtail": [], "brand": [], "geo": []},
     "entities": ["ont:cags-midland-tx"],
     "tree": [{"level": 3, "heading": "Why Your Search Shows Pet Shops and Classified Ads", "intent": "", "children": [
               {"level": 4, "heading": "Is the Nearest Bird Shop the Same Thing as a Breeder?", "intent": "", "children": [
               {"level": 5, "heading": "A Shop Resells Birds It Did Not Hatch, Hand-Feed, or Wean", "intent": "", "children": [
               {"level": 6, "heading": "Distance Note: Why We Are Not in Your Local Results", "intent": "", "children": []}]}]}]},
              {"level": 3, "heading": "Grey or Gray, Parrot or Parrots — All One Search", "intent": "", "children": []}],
     "images": [{"slot": "near-me-search-result-anatomy", "kind": "infographic", "required": false, "prompt": "annotated result-page wireframe"}],
     "options": {"candidates": ["h3-image-first"], "excluded": [], "pick": "h3-image-first", "note": ""}},
    {"id": "grid", "n": 2, "heading": "Choose Your State or Metro Area", "intent": "The grid, sole enumeration site: 25 state tiles by region, 15 metros.", "category": "C", "framework": "EEBP", "words": {"min": 250, "max": 400}, "shape": "nav",
     "keywords": {"primary": [], "lsi": ["in your state"], "longtail": [], "brand": [], "geo": ["24 states", "15 metros"]},
     "entities": ["ont:midland-pickup-radius"],
     "tree": [{"level": 3, "heading": "African Greys for Sale, State by State", "intent": "", "children": []},
              {"level": 3, "heading": "African Greys for Sale, Metro by Metro", "intent": "", "children": [
               {"level": 4, "heading": "What If My State Is Not on the List?", "intent": "", "children": [
               {"level": 5, "heading": "We Ship to All Fifty States From Midland, Texas", "intent": "", "children": [
               {"level": 6, "heading": "From Midland: How We Decide the Route", "intent": "", "children": []}]}]}]}],
     "images": [{"slot": "choose-your-state-or-metro-area", "kind": "infographic", "required": false, "prompt": "blank state tile grid"}],
     "options": {"candidates": ["toc-t2-chip-cloud"], "excluded": [], "pick": "toc-t2-chip-cloud", "note": "refreshed to region → state chips"}},
    {"id": "distance", "n": 3, "heading": "How Close Are We to You, Really?", "intent": "Drive or fly: pickup within 2–3 h, else $185 / $350.", "category": "A", "framework": "EEBP", "words": {"min": 400, "max": 600}, "shape": "compare",
     "keywords": {"primary": [], "lsi": ["nearby"], "longtail": [], "brand": [], "geo": ["Midland, Texas"]},
     "entities": ["ont:airport-cargo-185", "ont:home-delivery-350", "ont:midland-pickup-radius", "ont:iata-live-animals-regulations", "ont:delta-cargo", "ont:united-cargo", "ont:american-airlines-cargo"],
     "tree": [{"level": 3, "heading": "Pickup in Midland, Texas — Within Two or Three Hours", "intent": "", "children": []},
              {"level": 3, "heading": "Everywhere Else Flies", "intent": "", "children": [
               {"level": 4, "heading": "How Much Is Delivery to Your Address?", "intent": "", "children": [
               {"level": 5, "heading": "$185 to Your Nearest Cargo Airport, $350 to Your Door", "intent": "", "children": [
               {"level": 6, "heading": "From Midland: The Drive-or-Fly Line", "intent": "", "children": []}]}]}]}],
     "images": [{"slot": "midland-pickup-radius-or-fly", "kind": "infographic", "required": false, "prompt": "concentric drive and fly rings"}],
     "options": {"candidates": ["table-i-distance-ledger"], "excluded": [], "pick": "table-i-distance-ledger", "note": "NEW Table I"}},
    {"id": "birds", "n": 4, "heading": "The Birds You Could Be Matched With", "intent": "Six live birds with prices and the shipping line.", "category": "A", "framework": "EEBP", "words": {"min": 500, "max": 700}, "shape": "inventory",
     "keywords": {"primary": [], "lsi": ["congo african grey for sale near me"], "longtail": [], "brand": ["C.A.Gs"], "geo": []},
     "entities": ["ont:psittacus-erithacus", "ont:psittacus-timneh", "ont:deposit-200", "ont:benjamin-home-raising-protocol", "ont:midland-socialization-method", "ont:lifespan-40-60"],
     "tree": [{"level": 3, "heading": "Our Congos, and Where Each Could Fly", "intent": "", "children": []},
              {"level": 3, "heading": "Our Timnehs, and Where Each Could Fly", "intent": "", "children": []},
              {"level": 3, "heading": "The Companion Pair", "intent": "", "children": [
               {"level": 4, "heading": "Can I Reserve a Bird Before I Travel to See It?", "intent": "", "children": [
               {"level": 5, "heading": "A Deposit Holds a Named Bird — It Never Buys a Photograph", "intent": "", "children": [
               {"level": 6, "heading": "Ask Before You Drive: What to Confirm First", "intent": "", "children": []}]}]}]}],
     "images": [{"slot": "the-birds-you-could-be-matched-with", "kind": "infographic", "required": false, "prompt": "interlocking match rings"}],
     "options": {"candidates": ["avail-b-faceted"], "excluded": [], "pick": "avail-b-faceted", "note": ""}},
    {"id": "cheap", "n": 5, "heading": "Why Are “Cheap” African Greys Near You Usually a Scam?", "intent": "Below the grid: the cheap/Craigslist searcher; reuse the price-artifact evidence; link the scam cluster.", "category": "C", "framework": "PAS", "words": {"min": 450, "max": 650}, "shape": "narrative",
     "keywords": {"primary": [], "lsi": ["cheap"], "longtail": ["where can i buy an african grey parrot near me"], "brand": [], "geo": []},
     "entities": ["ont:aviary-floor-1500"],
     "tree": [{"level": 3, "heading": "What Classified Listings Leave Out", "intent": "", "children": [
               {"level": 4, "heading": "What Did We Measure Across the Listing Sites?", "intent": "", "children": [
               {"level": 5, "heading": "One Seller's Birds Carried Three Different Prices on a Single Day", "intent": "", "children": [
               {"level": 6, "heading": "Ask Before You Drive: The Three Questions a Fake Listing Cannot Answer", "intent": "", "children": []}]}]}]},
              {"level": 3, "heading": "What a Real Breeder Will Always Let You Do", "intent": "", "children": []}],
     "images": [{"slot": "same-african-grey-three-classified-prices", "kind": "infographic", "required": false, "prompt": "price tags on a line"}],
     "options": {"candidates": ["h3-image-first"], "excluded": [], "pick": "h3-image-first", "note": ""}},
    {"id": "papers", "n": 6, "heading": "What Arrives With Every African Grey We Place?", "intent": "The five documents; the folder is the same across state lines.", "category": "A", "framework": "EEBP", "words": {"min": 450, "max": 650}, "shape": "proof",
     "keywords": {"primary": [], "lsi": [], "longtail": [], "brand": [], "geo": []},
     "entities": ["ont:cites-appendix-i", "ont:captive-bred", "ont:pcr-dna-sexing", "ont:pbfd-screening", "ont:avian-polyomavirus-screening", "ont:psittacosis-screening", "ont:avian-vet-health-certificate", "ont:hatch-certificate-closed-band", "ont:usda-awa-licence", "ont:aphis-public-search", "ont:mark-teri-benjamin"],
     "tree": [{"level": 3, "heading": "Your Appendix I Certificate", "intent": "", "children": [
               {"level": 4, "heading": "Does Paperwork Change If the Bird Crosses State Lines?", "intent": "", "children": [
               {"level": 5, "heading": "Interstate Transport Requires the Certificate to Travel With the Bird", "intent": "", "children": [
               {"level": 6, "heading": "From Midland: Which Documents Leave With Which Bird", "intent": "", "children": []}]}]}]},
              {"level": 3, "heading": "Sex Testing and Vet Records", "intent": "", "children": []},
              {"level": 3, "heading": "Our USDA AWA Licence", "intent": "", "children": []}],
     "images": [{"slot": "five-documents-with-every-african-grey", "kind": "infographic", "required": false, "prompt": "fanned document flat-lay"}],
     "options": {"candidates": ["k4-clipboard"], "excluded": [], "pick": "k4-clipboard", "note": ""}},
    {"id": "arrival", "n": 7, "heading": "What Happens If Something Is Wrong on Arrival", "intent": "72-hour term, the address behind it, who to call first.", "category": "A", "framework": "QAB", "words": {"min": 350, "max": 500}, "shape": "sequence",
     "keywords": {"primary": [], "lsi": [], "longtail": [], "brand": [], "geo": []},
     "entities": ["ont:72-hour-guarantee", "ont:aav-find-a-vet"],
     "tree": [{"level": 3, "heading": "The 72-Hour Term, and Why the Address Behind It Matters", "intent": "", "children": [
               {"level": 4, "heading": "Who Do You Call First?", "intent": "", "children": [
               {"level": 5, "heading": "Same-Day Contact Is What Keeps the Term Usable", "intent": "", "children": [
               {"level": 6, "heading": "Distance Note: Finding an Avian Vet in Your State", "intent": "", "children": []}]}]}]}],
     "images": [{"slot": "if-african-grey-arrives-unwell-three-steps", "kind": "infographic", "required": false, "prompt": "vertical three-step phone flow"}],
     "options": {"candidates": ["numbered-ledger"], "excluded": [], "pick": "numbered-ledger", "note": ""}},
    {"id": "faq", "n": 8, "heading": "Near-Me Questions Buyers Ask Us From Every State", "intent": "12 questions from the PAA set and the near-me cluster.", "category": "A", "framework": "QAB", "words": {"min": 900, "max": 1300}, "shape": "standard",
     "keywords": {"primary": ["african grey parrots for sale near me"], "lsi": [], "longtail": [], "brand": [], "geo": []},
     "entities": [],
     "tree": [{"level": 3, "heading": "Distance and Delivery", "intent": "", "children": []},
              {"level": 3, "heading": "Documentation and Legality", "intent": "", "children": []}],
     "images": [], "options": {"candidates": [], "excluded": [], "pick": null, "note": ""}},
    {"id": "reserve", "n": 9, "heading": "Tell Us Where You Are", "intent": "Form with the state select; deposit by arrangement.", "category": "A", "framework": "EEBP", "words": {"min": 150, "max": 250}, "shape": "standard",
     "keywords": {"primary": [], "lsi": [], "longtail": [], "brand": [], "geo": []},
     "entities": ["ont:deposit-200"],
     "tree": [{"level": 3, "heading": "Reserve a Bird or Ask About Your State", "intent": "", "children": []}],
     "images": [], "options": {"candidates": [], "excluded": [], "pick": null, "note": ""}}
  ],
  "tuple": {"hero": "hero-c-mosaic-metrics", "dial": "dial-1-clay", "rail": "rail-b-green-ticker", "toc": "toc-t2-chip-cloud",
            "takeaway": ["k3-green-ledger", "k4-clipboard", "k5-capsule"], "table": "table-i-distance-ledger", "faq": "faq-b",
            "h6_prefixes": ["Distance Note:", "From Midland:", "Ask Before You Drive:"]},
  "assets": [
    {"slot": "hero", "kind": "photo", "w": 1280, "h": 960, "required": true, "status": "baked", "file": "public/images/near-me-page/african-grey-parrots-for-sale-near-me-hero.webp", "alt": "African Grey parrots for sale near you: a Congo settled on its stand in a family living room"},
    {"slot": "card-bery", "kind": "photo", "w": 800, "h": 800, "required": true, "status": "baked", "file": "public/images/near-me-page/bery-congo-african-grey-hen-near-me-card.webp", "alt": "Bery working through fresh greens in her cage"},
    {"slot": "newsletter", "kind": "photo", "w": 1408, "h": 768, "required": false, "status": "baked", "file": "public/images/near-me-page/timneh-chick-nursery-newsletter-near-me.webp", "alt": "A Timneh chick resting on an open palm in the nursery"}
  ],
  "approval": null
}
```

- [ ] **Step 4: Add the self-exclusion line to the gate CLI**

In `scripts/board_gate.py`, after `live = PB.live_headings() if PB.DIST.exists() else {}` add:

```python
    live.pop("/" + slug + "/", None)      # a live page never collides with itself
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `26 passed`. If `header-collision` fails on the near-me fixture with `page="/african-grey-parrot-for-sale-near-me/"` or `"/where-to-buy-african-greys-near-me/"`, that is the outline gate's classified match (those pages retire in Task 11 of the 2026-08-10 plan); until then add those two slugs to the `live.pop` list in the test only, with a comment naming the retirement task.

- [ ] **Step 6: Commit**

```bash
git add data/pages/african-grey-parrots-for-sale-near-me/board.json scripts/board_gate.py tests/test_page_board.py
git commit -m "test(page-board): the shipped near-me page as a retro-fitted board; the gate passes it

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

> **Review amendment (Task 7 fixture, 2026-09-12): combos, not components.** Running the gate on the real near-me record showed the per-component ownership rule fails every shipped page: `dial-1-clay` is on nine pages and `table-a-stacking` on eight by design. The ledger's actual discipline (component map §"Per-page assignment discipline" and the tuple-11/12 ledger) is:
> - **Shared pools** (no ownership, every entry always a free candidate): `nav` (dials + rails), `inventory`, `compare`, `sequence`, `proof`, `price`, `narrative`. **Refresh pools** (an owned base is offered as `base#refresh`): `hero`, `toc` (the five TOC shells, split out of `nav`; shape `nav` sections draw from the `toc` pool), `faq`, `takeaway`, `counter`. The ledger carries `"refresh_pools": [...]`.
> - Gate FAILs: `ledger-tuple-identical` (all seven axes equal a sibling's), `ledger-triple-owned` (hero + dial + rail equal a sibling's triple), `ledger-takeaway-set-owned` (the same set of takeaway ids as a sibling), `ledger-spent-prefix` (unchanged), and `ledger-shell-owned` only for **refresh-pool axes** (hero, toc, faq) used bare when a sibling uses that base bare or refreshed. Dials, rails and tables never fail on their own.
> - Tasks 8 and 9 read `refresh_pools` to decide whether an option card shows an owner badge.

### Task 8: The board artifact generator

**Files:**
- Create: `scripts/build_page_board.py`
- Test: `tests/test_page_board.py`

The board is an HTML document with the copy-button convention the gate reports use (markdown authored once, rendered by `marked`), plus three live blocks: the Cytoscape graph, the pick controls, and Approve. Approve writes `db.doc("boards/<slug>")` through `claude.use("db")`; the page renders fully without it and lights the button up when the namespace resolves. Every colour is a token on `:root` with both dark blocks and an explicit `body` background.

- [ ] **Step 1: Write the failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k board_html`
Expected: `ModuleNotFoundError: build_page_board`

- [ ] **Step 3: Write the generator**

```python
#!/usr/bin/env python3
"""build_page_board.py <slug>
board.json → docs/artifacts/boards/<slug>.html (an Artifact with the db capability) plus
docs/artifacts/boards/<slug>/thumbs/*.png cut by board_thumbs.mjs from the canvas artboards
(run board_canvas.py first; thumbs are optional — a missing thumb renders as a labelled box).
Publish with the Artifact tool: file_path=<html>, capabilities={"db": {}},
files={"thumbs/...": "docs/artifacts/boards/<slug>/thumbs/..."}."""
import html as H, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB

OUT = PB.ROOT / "docs" / "artifacts" / "boards"

CSS = """
:root{--ground:#F7F5EE;--paper:#FFFFFF;--ink:#1E2A24;--ink-2:#4B5A52;--ink-3:#7A867F;--line:#DDD9CC;--green:#2D6A4F;--green-soft:#E3EEE8;--clay:#E8604C;--clay-ink:#c8472f;--clay-soft:#FBE7E2;--code-bg:#F0EEE5;--mark:#FFF3C4;--warn:#9C3A2A}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ground:#151A17;--paper:#1D2420;--ink:#ECEBE3;--ink-2:#B7BDB6;--ink-3:#7F8983;--line:#2F3934;--green:#6FB48F;--green-soft:#1F2F28;--clay:#F08A78;--clay-ink:#F08A78;--clay-soft:#3A2622;--code-bg:#11161380;--mark:#4A3F16;--warn:#F2A08F}}
:root[data-theme="dark"]{--ground:#151A17;--paper:#1D2420;--ink:#ECEBE3;--ink-2:#B7BDB6;--ink-3:#7F8983;--line:#2F3934;--green:#6FB48F;--green-soft:#1F2F28;--clay:#F08A78;--clay-ink:#F08A78;--clay-soft:#3A2622;--code-bg:#11161380;--mark:#4A3F16;--warn:#F2A08F}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font:16px/1.6 "IBM Plex Sans",system-ui,-apple-system,Segoe UI,sans-serif}
.wrap{max-width:1120px;margin:0 auto;padding:36px 24px 96px}
header.masthead{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:end;padding-bottom:18px;border-bottom:2px solid var(--green);margin-bottom:24px}
.eyebrow{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--green);font-weight:600;margin:0 0 6px}
h1.title{font-family:"Source Serif 4",Georgia,serif;font-weight:700;font-size:clamp(26px,3.6vw,38px);line-height:1.1;margin:0;text-wrap:balance}
.meta{font-size:13px;color:var(--ink-3);text-align:right;line-height:1.5}
.pill{display:inline-block;border-radius:50px;padding:2px 9px;font-size:11px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;border:1px solid var(--line);background:var(--paper)}
section.sec{background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:24px 28px 26px;margin:0 0 20px}
section.sec h2{font-family:"Source Serif 4",Georgia,serif;font-weight:700;font-size:22px;margin:0 0 10px;line-height:1.2}
.md p,.md li{max-width:72ch}.md table{border-collapse:collapse;width:100%;font-size:14px;margin:10px 0 14px;display:block;overflow-x:auto}
.md th{text-align:left;font-weight:600;color:var(--ink-2);font-size:12px;text-transform:uppercase;letter-spacing:.06em;border-bottom:2px solid var(--green);padding:6px 10px;white-space:nowrap}
.md td{padding:6px 10px;border-bottom:1px solid var(--line);vertical-align:top;font-variant-numeric:tabular-nums}
.md code{font:13px/1.5 "IBM Plex Mono",ui-monospace,Menlo,monospace;background:var(--code-bg);padding:1px 5px;border-radius:4px}
.tree{font:13px/1.65 "IBM Plex Mono",ui-monospace,Menlo,monospace;white-space:pre-wrap;margin:0;overflow-x:auto}
.hit{color:var(--warn);font-weight:600}
#entity-graph{height:440px;border:1px solid var(--line);border-radius:8px;background:var(--ground)}
.legend{font-size:12px;color:var(--ink-3);margin:6px 0 0}
.opts{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin:8px 0 6px}
.opt{border:1px solid var(--line);border-radius:8px;padding:8px;background:var(--paper);display:grid;gap:6px}
.opt img,.opt .nothumb{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:5px;border:1px solid var(--line);background:var(--code-bg);display:grid;place-items:center;font-size:12px;color:var(--ink-3)}
.opt.off{opacity:.55}.opt label{display:flex;gap:8px;align-items:center;font-size:13px;font-weight:600;cursor:pointer}
.opt .why{font-size:12px;color:var(--ink-3)}
textarea.note{width:100%;min-height:52px;font:13px/1.5 "IBM Plex Sans",system-ui,sans-serif;border:1px solid var(--line);border-radius:6px;padding:8px;background:var(--ground);color:var(--ink)}
.slots{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.slot{border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:13px}.slot .st{font-weight:700}.slot .st.missing{color:var(--warn)}
#approve{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
button.btn{font:inherit;font-size:14px;font-weight:600;padding:10px 18px;border-radius:50px;border:1px solid var(--clay-ink);background:var(--clay-ink);color:#fff;cursor:pointer}
button.btn[disabled]{opacity:.5;cursor:default}
.status{font-size:13px;color:var(--ink-2)}
button:focus-visible,input:focus-visible,textarea:focus-visible{outline:3px solid var(--clay);outline-offset:2px}
@media (max-width:640px){header.masthead{grid-template-columns:1fr}.meta{text-align:left}section.sec{padding:18px 16px 20px}}
"""


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def outline_block(board, hits):
    hit_by = {h["heading"]: h for h in hits}
    lines = [f"H1  {board['h1']['variants'][board['h1']['pick'] if board['h1']['pick'] is not None else board['h1']['recommended']]}"]
    for s in board["sections"]:
        lines.append(f"├─ H2 {s['n']:02d}  {H.escape(s['heading'])}   [{s['category']} · {s['shape']} · {s['framework']} · {s['words']['min']}–{s['words']['max']}w]" + flag(s["heading"], hit_by))

        def walk(nodes, depth):
            for n in nodes:
                lines.append("│   " * depth + f"├─ H{n['level']} {H.escape(n['heading'])}" + flag(n["heading"], hit_by))
                walk(n["children"], depth + 1)
        walk(s["tree"], 1)
    return "\n".join(lines)


def flag(heading, hit_by):
    h = hit_by.get(heading)
    if not h:
        return ""
    kind = {"exact": "exact match with", "template": "template match with", "shingle": "5-word overlap with"}[h["kind"]]
    return f'   <span class="hit">⚠ {kind} {H.escape(h["page"])}</span>'


def entity_graph_data(board, ont):
    by_id = {e["id"]: e for e in ont["entities"]}
    nodes, edges, seen = [], [], set()
    for s in board["sections"]:
        nodes.append({"data": {"id": "sec:" + s["id"], "label": f"{s['n']:02d} {s['heading'][:34]}", "kind": "section"}})
        for eid in s["entities"]:
            e = by_id.get(eid, {"name": eid, "class": "Unknown", "authorization": "PROPOSED"})
            if eid not in seen:
                seen.add(eid)
                nodes.append({"data": {"id": eid, "label": e["name"], "kind": e["class"], "auth": e["authorization"]}})
            edges.append({"data": {"source": "sec:" + s["id"], "target": eid, "auth": e["authorization"]}})
    return {"nodes": nodes, "edges": edges}


def render(board, ont, ledger, live, thumbs, slug):
    hits = PB.header_precheck([h for _, h in PB.all_headings(board)], live)
    d = PB.distribution(board)
    auth = PB.authorization_check(board, ont)
    approved = PB.approval_matches(board)
    m = board["meta"]
    parts = []

    brief = board["brief"]
    parts.append(("1. Brief", "\n".join([
        f"**Goal.** {brief['goal']}", f"**Scope.** {brief['scope']}", f"**Gates.** {', '.join(brief['gates'])}",
        f"**Done means.** {brief['done']}", f"**Out of scope.** {', '.join(brief['out_of_scope']) or 'nothing named'}",
        f"**Primary keyword.** `{brief['primary_keyword']}`",
        f"**Strategy: {brief['strategy']['name']}.** Why: {brief['strategy']['why']} Trade-off: {brief['strategy']['trade_off']}",
        "", "**Research used**", md_table(["Source", "Fetched"], [[s["path"], s["fetched"]] for s in m["sources"]]) if m["sources"] else "_no sources recorded_",
    ])))

    h1 = board["h1"]
    parts.append(("2. H1", "\n".join(
        [f"{'⭐ ' if i == h1['recommended'] else ''}<label><input type=\"radio\" name=\"h1\" value=\"{i}\"{' checked' if i == (h1['pick'] if h1['pick'] is not None else h1['recommended']) else ''}> {H.escape(v)}</label>  "
         for i, v in enumerate(h1["variants"])])))

    parts.append(("3. Outline", f"<pre class=\"tree\">{outline_block(board, hits)}</pre>\n\n"
                  + (f"**{len(hits)} heading(s) collide with a live page.** Rewrite them before approving; the gate fails on any." if hits else "No heading collides with a live page (exact, species-template or 5-word shingle).")))

    rows = [[r["section"], r["primary"], r["lsi"], r["longtail"], r["brand"], r["geo"], f"{r['words_min']}–{r['words_max']}"] for r in d["rows"]]
    t = d["totals"]
    rows.append(["**totals**", t["primary"], t["lsi"], t["longtail"], t["brand"], t["geo"], f"{t['words_min']}–{t['words_max']}"])
    parts.append(("4. Distribution", md_table(["Section", "Primary", "LSI", "Long-tail", "Brand", "Geo", "Words"], rows)
                  + f"\n\nHeadings: H2 {d['h_counts']['h2']} · H3 {d['h_counts']['h3']} · H4 {d['h_counts']['h4']} · H5 {d['h_counts']['h5']} · H6 {d['h_counts']['h6']}. Counts are ceilings, not floors."))

    by_id = {e["id"]: e for e in ont["entities"]}
    ent_rows = []
    all_ents = sorted({e for s in board["sections"] for e in s["entities"]})
    for eid in all_ents:
        e = by_id.get(eid)
        cells = ["✓" if eid in s["entities"] else "" for s in board["sections"]]
        ent_rows.append([f"{e['name'] if e else eid} ({e['authorization'] if e else 'UNKNOWN'})"] + cells + [(e or {}).get("owner_page") or "—"])
    ent_md = ('<div id="entity-graph"></div><p class="legend">colour = class · solid = ASSERTED · dashed = PROPOSED · red = BLOCKED (fails the board)</p>\n\n'
              + md_table(["Entity"] + [f"{s['n']:02d}" for s in board["sections"]] + ["Owner"], ent_rows)
              + (f"\n\n**BLOCKED referenced: {', '.join(auth['blocked'])}.** The board cannot be approved." if auth["blocked"] else "")
              + (f"\n\nPROPOSED (need a source): {', '.join(auth['proposed'])}." if auth["proposed"] else ""))
    parts.append(("5. Entities", ent_md))

    opt_html = []
    for s in board["sections"]:
        if s["shape"] == "standard":
            continue
        cands, excluded = PB.candidates_for(s["shape"], ledger, slug)
        cards = []
        for c in cands:
            th = thumbs.get((s["id"], c))
            img = f'<img src="{H.escape(th)}" alt="{H.escape(c)} option for {H.escape(s["id"])}">' if th else f'<div class="nothumb">{H.escape(c)}</div>'
            checked = " checked" if (s["options"]["pick"] == c) else ""
            cards.append(f'<div class="opt">{img}<label><input type="radio" name="pick-{s["id"]}" value="{H.escape(c)}"{checked}> {H.escape(c)}</label></div>')
        for x in excluded:
            cards.append(f'<div class="opt off"><div class="nothumb">{H.escape(x["component"])}</div><span class="why">owned by {H.escape(x["owner"])} — excluded</span></div>')
        opt_html.append(f"### {s['n']:02d} · {H.escape(s['heading'])} <span class=\"pill\">{s['shape']}</span>\n\n<div class=\"opts\">{''.join(cards)}</div>\n"
                        f"<textarea class=\"note\" name=\"note-{s['id']}\" placeholder=\"Note for this section (optional)\">{H.escape(s['options']['note'])}</textarea>")
    parts.append(("6. Component options", "\n\n".join(opt_html) or "_No signature sections._"))

    slots = "".join(f'<div class="slot"><b>{H.escape(a["slot"])}</b> · {a["kind"]} · {a["w"]}×{a["h"]} · {"required" if a["required"] else "optional"}<br><span class="st {a["status"]}">{a["status"]}</span>{(" · " + H.escape(a["file"])) if a["file"] else ""}</div>' for a in board["assets"])
    parts.append(("7. Asset slots", f'<div class="slots">{slots}</div>'))

    approve = (f'<div id="approve"><button class="btn" id="approve-btn" disabled>Approve this board</button>'
               f'<span class="status" id="approve-status">{"Approved as it stands." if approved else "Connecting to the board database…"}</span></div>')
    parts.append(("8. Approve", approve + "\n\nWrites your H1 choice, picks, notes and the record hash to the board database. Build refuses to start without it; any later edit to the record clears it."))

    blocks = "".join(f'<script type="text/markdown" data-title="{H.escape(t)}">\n{b}\n</script>\n' for t, b in parts)
    graph = json.dumps(entity_graph_data(board, ont))
    record_hash = PB.record_hash(board)
    return f"""<title>Page Board: {H.escape(slug)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,700&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header class="masthead"><div><p class="eyebrow">CongoAfricanGreys.com · Page Board</p><h1 class="title">/{H.escape(slug)}/</h1></div>
<div class="meta"><span class="pill">status: {H.escape(m['status'])}</span> <span class="pill">research as of {H.escape(m['research_as_of'])}</span><br>record <code>{record_hash[:12]}</code></div></header>
<div id="doc"></div>
</div>
{blocks}
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.0/marked.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.30.2/cytoscape.min.js"></script>
<script>
(function(){{
  var doc=document.getElementById('doc');
  document.querySelectorAll('script[type="text/markdown"]').forEach(function(b){{
    var sec=document.createElement('section');sec.className='sec';
    var h2=document.createElement('h2');h2.textContent=b.getAttribute('data-title');sec.appendChild(h2);
    var body=document.createElement('div');body.className='md';
    body.innerHTML=window.marked?marked.parse(b.textContent.replace(/^\\n+|\\s+$/g,'')):b.textContent;
    sec.appendChild(body);doc.appendChild(sec);
  }});
  var G={graph};
  var el=document.getElementById('entity-graph');
  if(el&&window.cytoscape){{
    var cls={{Organism:'#2D6A4F',Documentation:'#6b4fa0',Health:'#c8472f',Commerce:'#b8860b',Logistics:'#1f6f8b',Place:'#7a5c3e',People:'#8b1e5f',Method:'#3d7a4a',Unknown:'#888',section:'#e8dccf'}};
    cytoscape({{container:el,elements:G.nodes.concat(G.edges),layout:{{name:'cose',animate:false,padding:20}},
      style:[{{selector:'node',style:{{'label':'data(label)','font-size':10,'width':18,'height':18,'background-color':function(n){{return cls[n.data('kind')]||'#888'}},'color':getComputedStyle(document.documentElement).getPropertyValue('--ink').trim()||'#1E2A24','text-wrap':'wrap','text-max-width':110}}}},
             {{selector:'node[kind="section"]',style:{{'shape':'round-rectangle','width':60,'height':22,'font-weight':'bold'}}}},
             {{selector:'edge',style:{{'width':1.5,'line-color':'#9aa','curve-style':'bezier'}}}},
             {{selector:'edge[auth="PROPOSED"]',style:{{'line-style':'dashed'}}}},
             {{selector:'edge[auth="BLOCKED"]',style:{{'line-color':'#c8472f','width':3}}}}]}});
  }}
  var RECORD_HASH={json.dumps(record_hash)};var SLUG={json.dumps(slug)};
  var btn=document.getElementById('approve-btn'),st=document.getElementById('approve-status');
  if(!window.claude||!window.claude.use){{st.textContent='Open this board inside claude.ai to approve it.';return;}}
  window.claude.use('db').then(function(db){{
    if(!db){{st.textContent='Approval needs the board database, which this view cannot reach.';return;}}
    var ref=db.doc('boards/'+SLUG);
    ref.get().then(function(snap){{var d=snap&&snap.data?snap.data():null;if(d&&d.record_hash===RECORD_HASH){{st.textContent='Approved '+d.approved_at+'.';}}}}).catch(function(){{}});
    btn.disabled=false;st.textContent=st.textContent.indexOf('Approved')===0?st.textContent:'Ready.';
    btn.addEventListener('click',function(){{
      var picks={{}},notes={{}};
      document.querySelectorAll('input[name^="pick-"]:checked').forEach(function(i){{picks[i.name.slice(5)]=i.value;}});
      document.querySelectorAll('textarea[name^="note-"]').forEach(function(t){{if(t.value.trim())notes[t.name.slice(5)]=t.value.trim();}});
      var h1=document.querySelector('input[name="h1"]:checked');
      var rec={{approved_at:new Date().toISOString(),h1:h1?parseInt(h1.value,10):0,picks:picks,notes:notes,canvas_version:null,record_hash:RECORD_HASH}};
      btn.disabled=true;st.textContent='Saving…';
      ref.set(rec).then(function(){{st.textContent='Approved '+rec.approved_at+'. Claude reads this back before building.';}})
        .catch(function(e){{btn.disabled=false;st.textContent='Could not save: '+(e&&e.code?e.code:'error')+'. Try again, or approve in chat.';}});
    }});
  }});
}})();
</script>
"""


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: build_page_board.py <slug>")
    slug = sys.argv[1]
    board = PB.load_board(slug)
    ont, ledger = PB.load_ontology(), PB.load_ledger()
    live = PB.live_headings() if PB.DIST.exists() else {}
    live.pop("/" + slug + "/", None)
    thumbs = {}
    tdir = OUT / slug / "thumbs"
    if tdir.exists():
        for p in sorted(tdir.glob("*.png")):          # <section>--<candidate>--desktop.png
            sec, cand = p.stem.split("--")[:2]
            thumbs.setdefault((sec, cand), f"thumbs/{p.name}")
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{slug}.html"
    out.write_text(render(board, ont, ledger, live, thumbs, slug), encoding="utf-8")
    print(f"wrote {out.relative_to(PB.ROOT)} — {len(board['sections'])} sections, {len(thumbs)} thumbs, {len(live)} live pages checked")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `28 passed`

- [ ] **Step 5: Render the near-me retrofit board and look at it once**

Run: `python3 scripts/build_page_board.py african-grey-parrots-for-sale-near-me`
Expected: `wrote docs/artifacts/boards/african-grey-parrots-for-sale-near-me.html — 9 sections, 0 thumbs, 103 live pages checked`
Then publish it once with the Artifact tool (`capabilities: {"db": {}}`, favicon `🗂️`, title from the file) and open it: all eight blocks render, the graph draws, the Approve button enables inside claude.ai. Do not click Approve on the retrofit board.

- [ ] **Step 6: Commit**

```bash
git add scripts/build_page_board.py docs/artifacts/boards/african-grey-parrots-for-sale-near-me.html tests/test_page_board.py
git commit -m "feat(page-board): build_page_board.py — the board artifact with header check, matrix, entity graph, picks and db-backed Approve

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 9: Canvas options from the record

**Files:**
- Create: `scripts/board_canvas.py`
- Create: `scripts/board_thumbs.mjs`
- Modify: `skills/cag-component-variations.md` and `.claude/skills/cag-component-variations/SKILL.md`
- Test: `tests/test_page_board.py`

Artboards use the exact `.dc.html` format from `docs/design/homepage-variations-r3/CONTRACT.md`: `<x-dc><helmet>…</helmet><div id="root" style="width:<vw>px …">` with inline styles only and `<script src="./support.js"></script>` kept verbatim (copy `support.js` from that folder). Each shape has one template function that lays the section's own record out three ways along a named axis. Copy comes only from the record.

- [ ] **Step 1: Write the failing tests**

```python
def test_canvas_writes_three_options_two_viewports_per_signature_section(tmp_path):
    import board_canvas as BC
    b = _approved(MIN_BOARD)
    ledger = {"pools": {"inventory": ["avail-a-grid", "avail-b-faceted", "bird-cards-row", "minibird-cards"]}, "pages": {}}
    written = BC.write_canvas(b, ledger, out=tmp_path)
    names = sorted(p.name for p in tmp_path.glob("*.dc.html"))
    assert names == sorted([f"birds--{c}--{vp}.dc.html" for c in ["avail-a-grid", "avail-b-faceted", "bird-cards-row"] for vp in ("Mobile", "Desktop")])
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k canvas`
Expected: `ModuleNotFoundError: board_canvas`

- [ ] **Step 3: Write the canvas generator**

```python
#!/usr/bin/env python3
"""board_canvas.py <slug>
Writes docs/design/board-<slug>/<section>--<candidate>--<Mobile|Desktop>.dc.html for every
signature section: up to three candidates from the shape pool minus what siblings own,
each filled ONLY from the section's own record. Publish the folder with the `design`
skill; cut thumbs with board_thumbs.mjs."""
import html as H, pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB

DESIGN = PB.ROOT / "docs" / "design"
SUPPORT = DESIGN / "homepage-variations-r3" / "support.js"
VIEWPORTS = {"Mobile": 390, "Desktop": 1440}
MAX_OPTIONS = 3
GREEN, GREEN_D, CLAY, CLAY_INK, CREAM, INK, MUTED, BD = "#2D6A4F", "#234f3b", "#e8604c", "#c8472f", "#faf7f4", "#1f2a24", "#6b625a", "#e7ddd3"

HEAD = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
  <style>
    body { margin:0; background:#faf7f4; font-family:"IBM Plex Sans", system-ui, sans-serif; color:#1f2a24; }
    h1,h2,h3 { font-family: Newsreader, Georgia, serif; font-weight:600; letter-spacing:-.003em; margin:0; }
    p { margin:0; } ul { margin:0; padding:0; list-style:none; }
    a { color:#b04228; text-decoration:none; } a:hover { color:#c8472f; }
  </style>
</helmet>
"""
FOOT = "</x-dc>\n</body>\n</html>\n"


def slot_box(w, h, label, width_css="100%"):
    return (f'<div aria-label="{H.escape(label)}" style="width:{width_css}; aspect-ratio:{w}/{h}; background:repeating-linear-gradient(135deg,#eee 0 8px,#e2ddd6 8px 16px); '
            f'border:1px dashed {BD}; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:12px; color:{MUTED};">{H.escape(label)} · {w}×{h}</div>')


def h3_list(section, limit=4):
    items = [n["heading"] for n in section["tree"] if n["level"] == 3][:limit]
    return "".join(f'<li style="display:flex; gap:10px; align-items:baseline; padding:8px 0; border-bottom:1px solid {BD};"><span style="font-family:Newsreader, Georgia, serif; font-weight:700; color:{CLAY_INK};">{i+1:02d}</span><span style="font-size:15px;">{H.escape(t)}</span></li>' for i, t in enumerate(items))


def heading_block(section, size_px):
    return (f'<p style="font-size:12px; letter-spacing:.1em; text-transform:uppercase; color:{CLAY_INK}; font-weight:600;">Section {section["n"]:02d} · {H.escape(section["shape"])}</p>'
            f'<h2 style="font-size:{size_px}px; line-height:1.15; color:{GREEN_D};">{H.escape(section["heading"])}</h2>'
            f'<p style="font-size:15px; line-height:1.6; color:{INK}; max-width:62ch;">{H.escape(section["intent"])}</p>')


def _wrap(vw, inner):
    pad = 20 if vw < 700 else 40
    return (HEAD + f'<div id="root" style="width:{vw}px; background:{CREAM}; display:flex; flex-direction:column;">'
            f'<section style="padding:{pad}px; box-sizing:border-box; display:flex; flex-direction:column; gap:16px;">{inner}</section></div>\n' + FOOT)


# ---- shape templates: (section, candidate, vw) -> inner HTML. Three candidates per shape
#      differ along a named axis; every word is the section's own.
def tpl_inventory(section, cand, vw):
    cols = 1 if vw < 700 else 3
    cards = "".join(f'<article style="border:1px solid {BD}; border-radius:14px; overflow:hidden; background:#fff; display:flex; flex-direction:column;">{slot_box(800, 800, img["slot"])}'
                    f'<div style="padding:12px; display:flex; flex-direction:column; gap:6px;"><h3 style="font-size:16px; text-transform:uppercase; color:{GREEN_D};">{H.escape(img["slot"])}</h3>'
                    f'<p style="font-size:12px; color:{MUTED};">Ships nationwide · $185 airport · $350 home</p></div></article>'
                    for img in (section["images"] or [{"slot": "card"}]) * 3)[:6000]
    if cand == "avail-b-faceted":
        side = f'<aside style="border:1px solid {BD}; border-radius:14px; padding:12px; background:#fff; font-size:13px; font-weight:600;">Browse by kind</aside>'
        grid = f'<div style="display:grid; grid-template-columns:{"minmax(0,1fr)" if vw < 700 else "200px minmax(0,1fr)"}; gap:16px;">{side}<div style="display:grid; grid-template-columns:repeat({cols}, minmax(0,1fr)); gap:14px;">{cards}</div></div>'
    elif cand == "bird-cards-row":
        grid = f'<div style="display:flex; gap:14px; overflow-x:auto;">{cards}</div>'
    else:
        grid = f'<div style="display:grid; grid-template-columns:repeat({cols}, minmax(0,1fr)); gap:14px;">{cards}</div>'
    return heading_block(section, 26 if vw < 700 else 34) + grid


def tpl_compare(section, cand, vw):
    rows = [n["heading"] for n in section["tree"] if n["level"] == 3] or [section["heading"]]
    if cand == "table-b-spine-cards" or (cand == "verdict-cards"):
        body = "".join(f'<div style="border:1px solid {BD}; border-radius:12px; padding:12px; background:#fff;"><b style="color:{GREEN_D};">{H.escape(r)}</b></div>' for r in rows)
        grid = f'<div style="display:grid; grid-template-columns:repeat({1 if vw < 700 else 2}, minmax(0,1fr)); gap:12px;">{body}</div>'
    else:
        trs = "".join(f'<tr><td style="padding:8px 10px; border-bottom:1px solid {BD}; font-weight:700; color:{GREEN_D};">{H.escape(r)}</td><td style="padding:8px 10px; border-bottom:1px solid {BD}; color:{MUTED};">from the record</td></tr>' for r in rows)
        grid = f'<table style="width:100%; border-collapse:collapse; background:#fff; border:1px solid {BD}; border-radius:12px; font-size:14px;"><caption style="caption-side:top; text-align:left; background:{CLAY_INK}; color:#fff; padding:8px 12px; font-size:12px; letter-spacing:.08em; text-transform:uppercase;">{H.escape(section["heading"])}</caption>{trs}</table>'
    return heading_block(section, 26 if vw < 700 else 34) + grid


def tpl_sequence(section, cand, vw):
    steps = [n["heading"] for n in section["tree"] if n["level"] in (3, 4)][:5]
    if cand == "timeline-strip":
        body = "".join(f'<div style="flex:1; border-top:3px solid {CLAY}; padding-top:8px; font-size:14px;"><b>{i+1}</b><br>{H.escape(s)}</div>' for i, s in enumerate(steps))
        return heading_block(section, 26 if vw < 700 else 34) + f'<div style="display:flex; flex-direction:{"column" if vw < 700 else "row"}; gap:14px;">{body}</div>'
    return heading_block(section, 26 if vw < 700 else 34) + f'<ul style="display:flex; flex-direction:column;">{h3_list(section, 5)}</ul>'


def tpl_proof(section, cand, vw):
    items = [n["heading"] for n in section["tree"]][:5]
    if cand == "k1-receipt":
        body = "".join(f'<div style="display:grid; grid-template-columns:{"1fr" if vw < 700 else "7.5rem 1fr"}; gap:12px; padding:8px 0; border-bottom:1px dashed {BD};"><dt style="font-size:12px; font-weight:700; text-transform:uppercase; color:{GREEN_D};">Item {i+1}</dt><dd style="margin:0; font-size:14px;">{H.escape(t)}</dd></div>' for i, t in enumerate(items))
        return heading_block(section, 26 if vw < 700 else 34) + f'<dl style="margin:0; border:1px solid {BD}; border-radius:14px; padding:8px 16px; background:#fff;">{body}</dl>'
    body = "".join(f'<li style="display:grid; grid-template-columns:20px 1fr; gap:8px; font-size:14px; padding:4px 0;"><span style="color:{GREEN};">✓</span>{H.escape(t)}</li>' for t in items)
    return heading_block(section, 26 if vw < 700 else 34) + f'<ul style="border:1px solid {BD}; border-radius:14px; padding:14px 18px; background:#fff;">{body}</ul>'


def tpl_price(section, cand, vw):
    return tpl_proof(section, "k1-receipt" if cand in ("k1-receipt", "table-h-price-ladder") else "k4-clipboard", vw)


def tpl_nav(section, cand, vw):
    labels = [s for s in [n["heading"] for n in section["tree"]]][:9] or [section["heading"]]
    chips = "".join(f'<a href="#" style="display:inline-flex; align-items:center; min-height:36px; padding:6px 14px; border-radius:50px; border:1.5px solid {GREEN}; font-size:13px; font-weight:600; color:{GREEN_D};">{H.escape(l)}</a>' for l in labels)
    if cand.startswith("dial"):
        return heading_block(section, 26 if vw < 700 else 34) + f'<div style="display:grid; grid-template-columns:{"1fr" if vw < 700 else "196px 1fr"}; gap:28px;"><nav style="border:1px solid {BD}; border-radius:16px; padding:12px 10px; background:{"#1c3a2e" if "dark" in cand else "#fff"}; display:grid; gap:4px;">{chips}</nav><div>{slot_box(1408, 768, "section body")}</div></div>'
    return heading_block(section, 26 if vw < 700 else 34) + f'<nav style="display:flex; gap:8px; flex-wrap:wrap;">{chips}</nav>'


def tpl_narrative(section, cand, vw):
    img = slot_box(1408, 768, (section["images"] or [{"slot": "section image"}])[0]["slot"])
    if cand == "split-feature":
        return heading_block(section, 26 if vw < 700 else 34) + f'<div style="display:grid; grid-template-columns:{"1fr" if vw < 700 else "1fr 1fr"}; gap:20px; align-items:center;">{img}<ul>{h3_list(section)}</ul></div>'
    if cand == "quote-band":
        return heading_block(section, 26 if vw < 700 else 34) + f'<blockquote style="margin:0; padding:16px 20px; border-radius:14px; background:{GREEN_D}; color:#fff; font-family:Newsreader, Georgia, serif; font-size:18px;">{H.escape(section["intent"])}</blockquote>{img}'
    return heading_block(section, 26 if vw < 700 else 34) + img + f'<ul>{h3_list(section)}</ul>'


TEMPLATES = {"inventory": tpl_inventory, "compare": tpl_compare, "sequence": tpl_sequence, "proof": tpl_proof,
             "price": tpl_price, "nav": tpl_nav, "narrative": tpl_narrative, "hero": tpl_narrative, "counter": tpl_proof, "takeaway": tpl_proof}


def write_canvas(board, ledger, out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    slug = board["meta"]["slug"]
    written = []
    for s in board["sections"]:
        if s["shape"] == "standard":
            continue
        cands, _ = PB.candidates_for(s["shape"], ledger, slug)
        tpl = TEMPLATES[s["shape"]]
        for c in cands[:MAX_OPTIONS]:
            for vp, vw in VIEWPORTS.items():
                p = out / f"{s['id']}--{c}--{vp}.dc.html"
                p.write_text(_wrap(vw, tpl(s, c, vw)), encoding="utf-8")
                written.append(p)
    if SUPPORT.exists():
        shutil.copy(SUPPORT, out / "support.js")
    else:
        (out / "support.js").write_text("// support.js placeholder: copy from docs/design/homepage-variations-r3/support.js\n")
    (out / "CONTRACT.md").write_text(
        f"# Page Board canvas — /{slug}/\n\nArtboards are generated by scripts/board_canvas.py from data/pages/{slug}/board.json.\n"
        "Every word is that section's own record; siblings only subtracted candidates. Edit layout here; a text edit is written back\n"
        "into the record by board_approve.py at approval. File naming: <section>--<candidate>--<Mobile|Desktop>.dc.html.\n", encoding="utf-8")
    return written


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: board_canvas.py <slug>")
    slug = sys.argv[1]
    board, ledger = PB.load_board(slug), PB.load_ledger()
    written = write_canvas(board, ledger, DESIGN / f"board-{slug}")
    print(f"wrote {len(written)} artboards to docs/design/board-{slug}/")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Write the thumbnail cutter**

```javascript
// scripts/board_thumbs.mjs <slug>
// Screenshots every Desktop artboard in docs/design/board-<slug>/ into
// docs/artifacts/boards/<slug>/thumbs/<section>--<candidate>--desktop.png (1440 wide, capped 900 tall).
import { chromium } from 'playwright';
import { readdirSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
const slug = process.argv[2];
if (!slug) { console.error('usage: node scripts/board_thumbs.mjs <slug>'); process.exit(1); }
const src = resolve('docs/design', `board-${slug}`);
const out = resolve('docs/artifacts/boards', slug, 'thumbs');
mkdirSync(out, { recursive: true });
const files = readdirSync(src).filter((f) => f.endsWith('--Desktop.dc.html'));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
for (const f of files) {
  await page.goto('file://' + resolve(src, f));
  await page.waitForTimeout(400);                       // fonts + inline layout
  const [section, cand] = f.replace('--Desktop.dc.html', '').split('--');
  await page.locator('#root').screenshot({ path: resolve(out, `${section}--${cand}--desktop.png`) });
  console.log('thumb', section, cand);
}
await browser.close();
console.log(`${files.length} thumbs in docs/artifacts/boards/${slug}/thumbs/`);
```

- [ ] **Step 5: Run tests to verify they pass, then cut the near-me thumbs once**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `30 passed`
Run: `python3 scripts/board_canvas.py african-grey-parrots-for-sale-near-me && node scripts/board_thumbs.mjs african-grey-parrots-for-sale-near-me && python3 scripts/build_page_board.py african-grey-parrots-for-sale-near-me`
Expected: artboards written (candidates × 2), the same number of thumbs ÷ 2, and the board rebuilt reporting `N thumbs`.

- [ ] **Step 6: Record the copy-source adaptation in the variations skill**

Append to `skills/cag-component-variations.md` (and copy to `.claude/skills/cag-component-variations/SKILL.md`):

```markdown
## Page Board mode (2026-09-12)

When a page has `data/pages/<slug>/board.json`, the copy source is the **section record**, not
`dist/<slug>/index.html`. `scripts/board_canvas.py <slug>` emits the option artboards from the
record (candidates from `data/component-ledger.json` pools minus what siblings own), and
`scripts/board_thumbs.mjs <slug>` cuts the thumbnails the board shows. Never lift copy from a
sibling or from `dist/` for a boarded page; a text tweak on the canvas is written back into the
record by `scripts/board_approve.py`. Spec: `docs/superpowers/specs/2026-09-12-page-board-system-design.md`.
```

- [ ] **Step 7: Commit**

```bash
git add scripts/board_canvas.py scripts/board_thumbs.mjs skills/cag-component-variations.md .claude/skills/cag-component-variations/SKILL.md tests/test_page_board.py docs/design/board-african-grey-parrots-for-sale-near-me docs/artifacts/boards/african-grey-parrots-for-sale-near-me
git commit -m "feat(page-board): board_canvas.py + board_thumbs.mjs — options from the record minus the ledger, thumbs for the board

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 10: Approval read-back, promotions, ledger append, text write-back

**Files:**
- Create: `scripts/board_approve.py`
- Test: `tests/test_page_board.py`

A Python script cannot call the Artifact tool, so the operator step is: `Artifact read_db` with `collection: "boards"`, `doc_id: <slug>`, `out_dir: data/pages/<slug>/inbox`, which saves `data/pages/<slug>/inbox/boards/<slug>.json`; then `python3 scripts/board_approve.py <slug>` reads that file.

- [ ] **Step 1: Write the failing tests**

```python
def test_approve_writes_approval_ledger_and_promotions(tmp_path, monkeypatch):
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    b["meta"]["slug"] = "hub-test"; b["meta"]["status"] = "boarded"
    b["sections"][0]["entities"] = ["ont:congo-african-grey", "ont:new-thing"]
    ont = {"entities": [{"id": "ont:congo-african-grey", "name": "Congo", "aliases": [], "class": "Organism", "authorization": "ASSERTED", "source": "x", "owner_page": None},
                        {"id": "ont:new-thing", "name": "New", "aliases": [], "class": "Health", "authorization": "PROPOSED", "source": "ledger#y", "owner_page": None},
                        {"id": "ont:no-source", "name": "NS", "aliases": [], "class": "Health", "authorization": "PROPOSED", "source": None, "owner_page": None}]}
    ledger = {"pools": {"inventory": ["avail-b"]}, "pages": {}}
    inbox = {"approved_at": "2026-09-12T12:00:00Z", "h1": 2, "picks": {"birds": "avail-b"}, "notes": {"birds": "shorter eyebrow"},
             "canvas_version": "v7", "record_hash": PB.record_hash(b)}
    out = BA.apply_approval(b, inbox, ont, ledger)
    assert out["board"]["approval"] == inbox and out["board"]["meta"]["status"] == "approved"
    assert out["board"]["h1"]["pick"] == 2 and out["board"]["sections"][0]["options"]["pick"] == "avail-b"
    assert out["board"]["sections"][0]["options"]["note"] == "shorter eyebrow"
    assert out["ledger"]["pages"]["hub-test"]["hero"] == "hero-a"
    auth = {e["id"]: e["authorization"] for e in out["ontology"]["entities"]}
    assert auth["ont:new-thing"] == "ASSERTED" and auth["ont:no-source"] == "PROPOSED"


def test_approve_refuses_a_stale_hash():
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    inbox = {"approved_at": "t", "h1": 0, "picks": {}, "notes": {}, "canvas_version": None, "record_hash": "f" * 64}
    with pytest.raises(PB.BoardError):
        BA.apply_approval(b, inbox, ONT_OK, LEDGER_EMPTY)


def test_text_writeback_updates_the_record_from_the_saved_artboard(tmp_path):
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    art = tmp_path / "birds--avail-b--Desktop.dc.html"
    art.write_text('<div id="root"><h2 style="x">What Do We Have for Sale Today?</h2><p>Our birds, today.</p></div>')
    changed = BA.writeback_text(b, tmp_path)
    assert b["sections"][0]["heading"] == "What Do We Have for Sale Today?"
    assert changed == [("birds", "heading", "What Do We Have for Sale Right Now?", "What Do We Have for Sale Today?")]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "approve or writeback"`
Expected: `ModuleNotFoundError: board_approve`

- [ ] **Step 3: Write the script**

```python
#!/usr/bin/env python3
"""board_approve.py <slug> [--canvas-dir docs/design/board-<slug>]
1. Reads the approval the board wrote to its database. Operator step first:
   Artifact read_db collection="boards" doc_id="<slug>" out_dir="data/pages/<slug>/inbox"
   → data/pages/<slug>/inbox/boards/<slug>.json
2. Verifies record_hash against the record as it stands (refuses a stale approval).
3. Writes canvas TEXT tweaks back into the record (the breeder editing the outline), then
   re-hashes — the approval covers the record the breeder actually saw.
4. Copies the approval in, sets picks/notes/h1, status=approved.
5. Appends the tuple + H6 prefixes to data/component-ledger.json.
6. Promotes referenced PROPOSED entities that carry a source to ASSERTED."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB


def writeback_text(board, canvas_dir):
    """A saved artboard's <h2> text becomes the section heading if it changed. Returns
    [(section id, field, old, new)]. Only the heading is written back: it is the one copy
    field an artboard shows verbatim; intents render as summaries, never as final prose."""
    canvas_dir = pathlib.Path(canvas_dir)
    changed = []
    if not canvas_dir.exists():
        return changed
    for s in board["sections"]:
        pick = s["options"].get("pick")
        art = canvas_dir / f"{s['id']}--{pick}--Desktop.dc.html" if pick else None
        if not art or not art.exists():
            continue
        m = re.search(r"<h2[^>]*>(.*?)</h2>", art.read_text(encoding="utf-8"), re.S)
        if not m:
            continue
        import html as _h
        new = _h.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        if new and new != s["heading"]:
            changed.append((s["id"], "heading", s["heading"], new))
            s["heading"] = new
    return changed


def apply_approval(board, inbox, ont, ledger, canvas_dir=None):
    if inbox.get("record_hash") != PB.record_hash(board):
        raise PB.BoardError("approval hash does not match the record — the record changed after the board was approved")
    b = json.loads(json.dumps(board))
    for sid, pick in inbox.get("picks", {}).items():
        for s in b["sections"]:
            if s["id"] == sid:
                s["options"]["pick"] = pick
    for sid, note in inbox.get("notes", {}).items():
        for s in b["sections"]:
            if s["id"] == sid:
                s["options"]["note"] = note
    b["h1"]["pick"] = inbox.get("h1", b["h1"]["recommended"])
    changed = writeback_text(b, canvas_dir) if canvas_dir else []
    approval = dict(inbox)
    approval["record_hash"] = PB.record_hash(b)          # the record the breeder saw, tweaks included
    b["approval"] = approval
    b["meta"]["status"] = "approved"
    PB.validate_board(b)

    led = json.loads(json.dumps(ledger))
    led["pages"][b["meta"]["slug"]] = dict(b["tuple"])
    PB.validate_ledger(led)

    o = json.loads(json.dumps(ont))
    used = {e for s in b["sections"] for e in s["entities"]}
    for e in o["entities"]:
        if e["id"] in used and e["authorization"] == "PROPOSED" and e["source"]:
            e["authorization"] = "ASSERTED"
    PB.validate_ontology(o)
    return {"board": b, "ledger": led, "ontology": o, "changed": changed}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("usage: board_approve.py <slug> [--canvas-dir <dir>]")
    slug = args[0]
    canvas_dir = None
    if "--canvas-dir" in sys.argv:
        canvas_dir = sys.argv[sys.argv.index("--canvas-dir") + 1]
    inbox_path = PB.ROOT / "data" / "pages" / slug / "inbox" / "boards" / f"{slug}.json"
    if not inbox_path.exists():
        sys.exit(f"no approval at {inbox_path.relative_to(PB.ROOT)} — run the Artifact read_db step first")
    inbox = json.loads(inbox_path.read_text(encoding="utf-8"))
    inbox = inbox.get("data", inbox)                    # read_db may wrap the document
    out = apply_approval(PB.load_board(slug), inbox, PB.load_ontology(), PB.load_ledger(), canvas_dir)
    PB.save_board(slug, out["board"])
    PB.LEDGER.write_text(json.dumps(out["ledger"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    PB.ONTOLOGY.write_text(json.dumps(out["ontology"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for sid, field, old, new in out["changed"]:
        print(f"  write-back {sid}.{field}: {old!r} → {new!r}")
    print(f"approved {slug} at {out['board']['approval']['approved_at']} — picks {out['board']['approval']['picks']}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_page_board.py -q`
Expected: `33 passed`

- [ ] **Step 5: Commit**

```bash
git add scripts/board_approve.py tests/test_page_board.py
git commit -m "feat(page-board): board_approve.py — hash check, picks, ledger append, entity promotion, canvas text write-back

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 11: Hub C, the first real board

**Files:**
- Create: `data/pages/african-grey-parrots-for-sale/board.json`
- Create: `sessions/for-sale-research/african-grey-parrots-for-sale/2026-09-1x-sprint0-delta.md`
- Generated: `docs/artifacts/boards/african-grey-parrots-for-sale.html`, `docs/design/board-african-grey-parrots-for-sale/`

This task is authored by the controlling session (prose and research are not delegated). Inputs are already on disk: `docs/superpowers/plans/2026-08-10-buy-shipping-and-near-me-for-sale-pages.md` §0f–§0g and Task 13; `docs/research/for-sale-keywords-2026-07.md` (the plural page's bucket and the buy cluster); `docs/research/competitor-sweep-page{1,2,3}-2026-08-09.md`; both Sprint 0 docs under `sessions/for-sale-research/`.

- [ ] **Step 1: The hub's own research delta**

Firecrawl Search (US) for `african grey parrots for sale`: top 10 organic with H1 and ordered H2s; PAA three levels; autosuggest for `african grey parrots for sale `, `african greys for sale `. Write `sessions/for-sale-research/african-grey-parrots-for-sale/2026-09-1x-sprint0-delta.md` with a `Fetched:` date on every table. Anything that will not fetch is `NOT FETCHED` with the barrier named.

- [ ] **Step 2: Write `board.json` for the hub**

The brief, from §0g: the cluster hub — national inventory, `AggregateOffer`, links to every spoke, **sheds the state/metro grid** (the near-me router owns it), absorbs the singular `/african-grey-parrot-for-sale/`. Page type `hub`. Draft sections, each with shape, framework, word band, keywords from the measured buckets, entity ids from the ontology, a full H3–H6 tree, and image slots:

| n | id | heading (draft, Title Case, run through the pre-check) | shape |
|---|---|---|---|
| 1 | birds | What African Grey Parrots Do We Have for Sale Right Now? | inventory |
| 2 | which | Congo or Timneh — Which African Grey Should You Bring Home? | compare |
| 3 | price | What Does an African Grey Parrot Cost From Us, and Why? | price |
| 4 | route | How Does an African Grey Get From Our Aviary to Your Door? | sequence |
| 5 | papers | What Comes With Every African Grey Parrot We Sell? | proof |
| 6 | who | Who Raises These African Greys, and Where? | narrative |
| 7 | next | Which African Grey Page Do You Need Next? | nav |
| 8 | faq | African Grey Buying Questions, Answered by the Breeder | standard |
| 9 | reserve | Reserve an African Grey Parrot | standard |

Tuple: pick from `data/component-ledger.json` pools minus what the twelve ledger pages own (the gate will tell you). H6 prefixes: three new ones not among the 34 spent (check `spent_h6_prefixes`). Assets: hero (photo, 1280×960, required), six cards (photo, 800², required, from `assets/brand/` after a contact sheet), one infographic per H2 (optional, with its prompt in the record).

Run, in order:

```bash
python3 -m pytest tests/test_page_board.py -q
npx astro build
python3 scripts/board_gate.py african-grey-parrots-for-sale     # expect FAIL only on approval-hash and signature-no-pick
python3 scripts/board_canvas.py african-grey-parrots-for-sale
node scripts/board_thumbs.mjs african-grey-parrots-for-sale
python3 scripts/build_page_board.py african-grey-parrots-for-sale
```

- [ ] **Step 3: Publish the board and the canvas**

Artifact tool: `file_path=docs/artifacts/boards/african-grey-parrots-for-sale.html`, `capabilities={"db": {}}`, `files={"thumbs/<name>.png": "docs/artifacts/boards/african-grey-parrots-for-sale/thumbs/<name>.png", ...}`, favicon `🗂️`. Publish the canvas folder with the `design` skill. Give the breeder both links and stop: the sitting is theirs.

- [ ] **Step 4: Read the approval back and apply it**

```bash
# Artifact tool: action=read_db collection=boards doc_id=african-grey-parrots-for-sale out_dir=data/pages/african-grey-parrots-for-sale/inbox
python3 scripts/board_approve.py african-grey-parrots-for-sale --canvas-dir docs/design/board-african-grey-parrots-for-sale
python3 scripts/board_gate.py african-grey-parrots-for-sale     # expect 0 FAIL
git add data/pages/african-grey-parrots-for-sale data/component-ledger.json data/cag-ontology.json
git commit -m "board(hub): african-grey-parrots-for-sale approved on the first Page Board

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

- [ ] **Step 5: Build from the record**

Build the page inline (controlling session) from `board.json` only: headings from the record, components from `approval.picks`, images as measured slots, then Harden → Release through the existing gates (`skills/cag-page-hardening.md`, `cag-evidence-pass`, `cag-aeo-pass`, `cag-final-page-pass`), with `python3 scripts/board_gate.py african-grey-parrots-for-sale --release` before IndexNow. The hub sheds its grid: after the build, `grep -o 'african-grey-parrot-for-sale-[a-z-]*/' dist/african-grey-parrots-for-sale/index.html | sort -u | wc -l` must be a small single digit. Then Task 11 and the singular retirement from the 2026-08-10 plan.

---

## Self-review against the spec

- **§3 data model** → Tasks 1–4 (schemas, hash, ontology, ledger). **§4 board artifact** → Task 8, seven blocks plus Approve, db-backed. **§5 canvas** → Task 9 (templates, three options, two viewports, thumbs, skill note). **§6 handoff and gates** → Task 6 (gate, release stage, rule index) and Task 10 (approval, ledger, promotions, text write-back). **§7 tests** → every task is TDD; the near-me fixture is Task 7. **§8 first run** → Task 11.
- **Placeholders:** `support.js` falls back to a placeholder file only if the homepage round-3 copy is missing; the artboard templates render slot boxes where photos go, by design (measured slots). No "TBD".
- **Type consistency:** `record_hash`, `approval_matches`, `candidates_for(shape, ledger, slug)`, `owned_components`, `spent_h6_prefixes`, `all_headings`, `live_headings`, `header_precheck(proposed, live)`, `authorization_check`, `distribution`, `gate_findings(board, ont, ledger, live, stage)` are used with the same signatures in every task. Thumb file names `<section>--<candidate>--desktop.png` match between `board_thumbs.mjs` and `build_page_board.main`.
- **Spec gap closed here:** the spec's "layout tweaks are read by the build from the saved artboard" needs the build to read the canvas; Task 11 Step 5 does that inline, and only the heading is written back to the record (Task 10 explains why).

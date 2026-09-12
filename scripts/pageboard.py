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


def _read_json(path):
    """Read a JSON file, reporting a malformed one as a BoardError like every other fault."""
    try:
        return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise BoardError(f"{path}: {e}") from None


def _validate(doc, schema_name):
    schema = json.loads((SCHEMAS / schema_name).read_text(encoding="utf-8"))
    try:
        jsonschema.validate(doc, schema)
    except jsonschema.ValidationError as e:
        path = "/".join(str(p) for p in e.absolute_path) or "(root)"
        raise BoardError(f"{schema_name}: {path}: {e.message}") from None


def validate_board(board):
    _validate(board, "board.schema.json")
    ids, ns = [], []
    for sec in board["sections"]:
        if sec["words"]["min"] > sec["words"]["max"]:
            raise BoardError(f"section {sec['id']}: words.min {sec['words']['min']} > words.max {sec['words']['max']}")
        ids.append(sec["id"])
        ns.append(sec["n"])
    for label, values in (("id", ids), ("n", ns)):
        dupes = sorted({v for v in values if values.count(v) > 1})
        if dupes:
            raise BoardError(f"duplicate section {label}: {', '.join(str(d) for d in dupes)}")


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
    board = _read_json(p)
    validate_board(board)
    return board


def save_board(slug, board):
    validate_board(board)
    if board["meta"]["slug"] != slug:
        raise BoardError(f"slug mismatch: saving as {slug} but the record says {board['meta']['slug']}")
    p = board_path(slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(board, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_ontology():
    if not ONTOLOGY.exists():
        raise BoardError(f"no ontology: {ONTOLOGY} does not exist")
    ont = _read_json(ONTOLOGY)
    validate_ontology(ont)
    return ont


def load_ledger():
    if not LEDGER.exists():
        raise BoardError(f"no component ledger: {LEDGER} does not exist")
    ledger = _read_json(LEDGER)
    validate_ledger(ledger)
    return ledger


LIFECYCLE_ASSET_KEYS = ("status", "file")


def record_hash(board):
    """sha256 of the record's CONTENT, keys sorted. Four fields are excluded because they
    are lifecycle state rather than content, and they move after approval by design:
    the top-level `approval`, `meta.status` (board_approve.py flips it to "approved"
    the moment it stamps the hash), and every asset's `status` and `file` (baking a photo
    fills them in). Hashing any of them would make every legitimate approval, and every
    later bake, read as a post-approval edit. An edit anywhere else DOES change the hash,
    which is how a real post-approval edit sends the page back to the board."""
    body = {k: v for k, v in board.items() if k != "approval"}
    meta = body.get("meta")
    if isinstance(meta, dict):
        body["meta"] = {k: v for k, v in meta.items() if k != "status"}
    assets = body.get("assets")
    if isinstance(assets, list):
        body["assets"] = [
            {k: v for k, v in a.items() if k not in LIFECYCLE_ASSET_KEYS} if isinstance(a, dict) else a
            for a in assets
        ]
    blob = json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def approval_matches(board):
    a = board.get("approval")
    return isinstance(a, dict) and a.get("record_hash") == record_hash(board)


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

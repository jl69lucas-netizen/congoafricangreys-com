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

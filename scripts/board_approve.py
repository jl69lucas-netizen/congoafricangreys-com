#!/usr/bin/env python3
"""board_approve.py <slug> [--canvas-dir docs/design/board-<slug>]

1. Reads the approval the board wrote to its database. Operator step first, because a
   Python script cannot call the Artifact tool:
   Artifact read_db collection="boards" doc_id="<slug>" out_dir="data/pages/<slug>/inbox"
   → data/pages/<slug>/inbox/boards/<slug>.json
2. Verifies record_hash against the record as it stands (refuses a stale approval).
3. Writes canvas TEXT tweaks back into the record (the breeder editing the outline), then
   re-hashes — the approval covers the record the breeder actually saw, choices included.
4. Copies the approval in, sets picks/notes/h1, status=approved.
5. Appends the tuple + the H6 prefixes the record actually spends to
   data/component-ledger.json, in the shape the existing pages use.
6. Promotes referenced PROPOSED entities that carry a source to ASSERTED.

Nothing is written until all three documents validate: apply_approval() is pure, main()
writes only what it returns.
"""
import html as _html
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB

USAGE = "usage: board_approve.py <slug> [--canvas-dir <dir>]"
H2 = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S)
TAG = re.compile(r"<[^>]+>")


def artboard_name(section_id, pick, viewport="Desktop"):
    """The file board_canvas.py wrote for this pick. `#` is spelled `+` on disk (it is a
    URL fragment everywhere else), so a lookup on the `#` spelling finds nothing and
    reports no change — a silent write-back is worse than a missing one."""
    return f"{section_id}--{pick.replace('#', '+')}--{viewport}.dc.html"


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
        if not pick:
            continue
        art = canvas_dir / artboard_name(s["id"], pick)
        if not art.exists():
            continue
        m = H2.search(art.read_text(encoding="utf-8"))
        if not m:
            continue
        new = _html.unescape(TAG.sub("", m.group(1))).strip()
        new = re.sub(r"\s+", " ", new)
        if new and new != s["heading"]:
            changed.append((s["id"], "heading", s["heading"], new))
            s["heading"] = new
    return changed


def spent_prefixes(board):
    """The H6 prefixes this record actually spends: the run up to and including the first
    colon of every H6 heading, in render order, deduplicated. Read from the headings rather
    than from tuple.h6_prefixes so a prefix the author declared and never used stays free
    for the next page — and so a prefix that IS used is spent even if it was never declared.
    The shape matches what spent_h6_prefixes() reads back out of the ledger."""
    out = []
    for level, text in PB.all_headings(board):
        if level != 6 or ":" not in text:
            continue
        prefix = text.split(":", 1)[0].strip() + ":"
        if prefix not in out:
            out.append(prefix)
    return out


def ledger_entry(board):
    """The row this page takes in data/component-ledger.json — the same eight keys every
    existing page carries, never a bare copy of the tuple (which would record the DECLARED
    prefixes instead of the spent ones)."""
    t = board["tuple"]
    entry = {k: t.get(k, "") for k in ("hero", "dial", "rail", "toc", "table", "faq")}
    entry["takeaway"] = list(t.get("takeaway", []))
    entry["h6_prefixes"] = spent_prefixes(board)
    return entry


def apply_approval(board, inbox, ont, ledger, canvas_dir=None):
    """The board, ledger and ontology as they stand after this approval. Pure: it reads
    nothing but its arguments and writes nothing — raise here and the files on disk are
    untouched."""
    if inbox.get("record_hash") != PB.record_hash(board):
        raise PB.BoardError(
            "approval hash does not match the record — the record changed after the board was approved")
    b = json.loads(json.dumps(board))
    by_id = {s["id"]: s for s in b["sections"]}

    for sid, pick in inbox.get("picks", {}).items():
        if sid not in by_id:
            raise PB.BoardError(f"approval picks section {sid!r}, which is not in the record")
        by_id[sid]["options"]["pick"] = pick
    for sid, note in inbox.get("notes", {}).items():
        if sid not in by_id:
            raise PB.BoardError(f"approval notes section {sid!r}, which is not in the record")
        by_id[sid]["options"]["note"] = note          # "" is the breeder clearing the note
    b["h1"]["pick"] = inbox.get("h1", b["h1"]["recommended"])

    # The Approve button already refuses an incomplete set of picks; trusting it would make
    # a half-picked board approvable by anyone who wrote the database document by hand.
    missing = [s["id"] for s in b["sections"] if s["shape"] != "standard" and not s["options"]["pick"]]
    if missing:
        raise PB.BoardError(f"no component pick for signature section(s): {', '.join(missing)}")

    changed = writeback_text(b, canvas_dir) if canvas_dir else []
    approval = dict(inbox)
    # Picks, notes and the H1 index are hashed CONTENT, and so are the canvas tweaks above,
    # so the stamped hash is the record with the breeder's choices in it — which is exactly
    # the record the gate will hash when it asks whether this page is still approved.
    approval["record_hash"] = PB.record_hash(b)
    b["approval"] = approval
    b["meta"]["status"] = "approved"
    PB.validate_board(b)

    led = json.loads(json.dumps(ledger))
    led.setdefault("pages", {})[b["meta"]["slug"]] = ledger_entry(b)
    PB.validate_ledger(led)

    o = json.loads(json.dumps(ont))
    used = {e for s in b["sections"] for e in s["entities"]}
    for e in o["entities"]:
        if e["id"] in used and e["authorization"] == "PROPOSED" and e["source"]:
            e["authorization"] = "ASSERTED"
    PB.validate_ontology(o)
    return {"board": b, "ledger": led, "ontology": o, "changed": changed}


def _write_json(path, doc):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    argv = sys.argv[1:]
    if "--canvas-dir" in argv:                       # its value is not a positional
        i = argv.index("--canvas-dir")
        argv = argv[:i] + argv[i + 2:]
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print("board-approve ERROR one slug expected")
        print(USAGE)
        sys.exit(2)
    slug = args[0]
    if "--canvas-dir" in sys.argv:
        i = sys.argv.index("--canvas-dir")
        if i + 1 >= len(sys.argv):
            print(f"board-approve ERROR --canvas-dir needs a directory\n{USAGE}")
            sys.exit(2)
        canvas_dir = pathlib.Path(sys.argv[i + 1])
    else:
        default = PB.ROOT / "docs" / "design" / f"board-{slug}"
        canvas_dir = default if default.exists() else None

    inbox_path = PB.ROOT / "data" / "pages" / slug / "inbox" / "boards" / f"{slug}.json"
    if not inbox_path.exists():
        print(f"board-approve ERROR no approval at {inbox_path} — run the Artifact read_db step first")
        sys.exit(2)
    try:
        inbox = json.loads(inbox_path.read_text(encoding="utf-8"))
        inbox = inbox.get("data", inbox) if isinstance(inbox, dict) else inbox   # read_db may wrap it
        out = apply_approval(PB.load_board(slug), inbox, PB.load_ontology(), PB.load_ledger(), canvas_dir)
    except PB.BoardError as e:
        print(f"board-approve ERROR {e}")
        sys.exit(2)

    PB.save_board(slug, out["board"])
    _write_json(PB.LEDGER, out["ledger"])
    _write_json(PB.ONTOLOGY, out["ontology"])
    for sid, field, old, new in out["changed"]:
        print(f"  write-back {sid}.{field}: {old!r} → {new!r}")
    promoted = sum(1 for e in out["ontology"]["entities"] if e["authorization"] == "ASSERTED")
    print(f"approved {slug} at {out['board']['approval']['approved_at']} — "
          f"{len(out['board']['approval']['picks'])} picks, {len(out['changed'])} text write-backs, "
          f"ledger row {out['ledger']['pages'][slug]}, {promoted} ASSERTED entities")


if __name__ == "__main__":
    main()

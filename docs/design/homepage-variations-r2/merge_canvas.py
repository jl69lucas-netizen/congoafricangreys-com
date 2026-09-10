"""Merge per-page canvas fragments into canvas.json for the round-2 variations canvas.

Run from repo root: python3 docs/design/homepage-variations-r2/merge_canvas.py
"""
import json
import pathlib

FOLDER = pathlib.Path(__file__).parent
PAGES = [
    ("hero", "Heroes"), ("counter", "Counter snippets"), ("dial", "Desktop dial"),
    ("rail", "Mobile jump links"), ("tables", "Tables"), ("faq", "FAQ"), ("shipping", "Shipping"),
]
# fragment files per page; tables2 is stacked under tables with a y offset
FRAGMENTS = {p: [f"canvas.part-{p}.json"] for p, _ in PAGES}
FRAGMENTS["tables"] = ["canvas.part-tables.json", "canvas.part-tables2.json"]

artboards, annotations, seen_notes, seen_files = [], [], set(), set()
for page_id, _ in PAGES:
    y_offset = 0
    for frag_name in FRAGMENTS[page_id]:
        path = FOLDER / frag_name
        if not path.exists():
            print(f"MISSING fragment {frag_name}")
            continue
        frag = json.loads(path.read_text())
        max_y = 0
        for a in frag["artboards"]:
            allowed = {"file","x","y","w","h","title","expand","print","is_interactive"}
            a = {k: v for k, v in a.items() if k in allowed}
            a["page"] = page_id
            a["y"] = a["y"] + y_offset
            max_y = max(max_y, a["y"] + a["h"])
            assert a["file"] not in seen_files, f"dup artboard {a['file']}"
            seen_files.add(a["file"])
            artboards.append(a)
        for n in frag.get("annotations", []):
            n = {k: v for k, v in n.items() if k in {"id","x","y","w","text","kind","size","bold","italic","color"}}
            n["page"] = page_id
            n["y"] = n["y"] + y_offset
            assert n["id"] not in seen_notes, f"dup note id {n['id']}"
            seen_notes.add(n["id"])
            annotations.append(n)
        y_offset = max_y + 320  # room for the next fragment's top note

on_disk = {p.name for p in FOLDER.glob("*.dc.html")}
missing = on_disk - seen_files
extra = seen_files - on_disk
assert not missing, f"unlisted files: {sorted(missing)}"
assert not extra, f"listed but not on disk: {sorted(extra)}"
canvas = {
    "pages": [{"id": p, "name": n} for p, n in PAGES],
    "artboards": artboards,
    "annotations": annotations,
    "launch": {"view": "canvas", "page": "hero"},
}
(FOLDER / "canvas.json").write_text(json.dumps(canvas, indent=2))
print(f"canvas.json: {len(artboards)} artboards, {len(annotations)} notes, {len(PAGES)} pages")

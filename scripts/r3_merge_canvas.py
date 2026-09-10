#!/usr/bin/env python3
"""Merge round-3 canvas fragments into canvas.json.

Four table authors share the single `tables` page, so fragments map many->one.
Asserts: every .dc.html on disk is listed, every note id unique, no unlisted files.
"""
import json, pathlib, sys

FOLDER = pathlib.Path("docs/design/homepage-variations-r3")
# fragment stem -> canvas page id
FRAGMENTS = [
    ("hero",          "hero"),
    ("counter",       "counter"),
    ("dial",          "dial"),
    ("rail",          "rail"),
    ("tables-cvt",    "tables"),
    ("tables-mvf",    "tables"),
    ("tables-others", "tables"),
    ("tables-price",  "tables"),
    ("faq",           "faq"),
    ("shipping",      "shipping"),
]
PAGE_ORDER = ["hero", "counter", "dial", "rail", "tables", "faq", "shipping"]
PAGE_NAMES = {"hero": "Hero", "counter": "Counter", "dial": "Desktop Dial",
              "rail": "Mobile Jump Links", "tables": "Tables", "faq": "FAQ",
              "shipping": "Shipping"}
# horizontal offset per table component so the four don't stack on top of each other
TABLE_XOFF = {"tables-cvt": 0, "tables-mvf": 3200, "tables-others": 6400, "tables-price": 9600}

artboards, annotations, seen_notes, seen_files = [], [], set(), set()
missing = []
for stem, page_id in FRAGMENTS:
    fp = FOLDER / f"canvas.part-{stem}.json"
    if not fp.exists():
        missing.append(fp.name); continue
    frag = json.loads(fp.read_text())
    xoff = TABLE_XOFF.get(stem, 0)
    for a in frag.get("artboards", []):
        a["page"] = page_id
        a["x"] = a.get("x", 0) + xoff
        if a["file"] in seen_files:
            sys.exit(f"FAIL duplicate artboard {a['file']} in {fp.name}")
        seen_files.add(a["file"]); artboards.append(a)
    for n in frag.get("annotations", []):
        n["page"] = page_id
        n["x"] = n.get("x", 0) + xoff
        if n["id"] in seen_notes:
            sys.exit(f"FAIL duplicate note id {n['id']} in {fp.name}")
        seen_notes.add(n["id"]); annotations.append(n)

if missing:
    sys.exit(f"FAIL missing fragments: {missing}")

on_disk = {p.name for p in FOLDER.glob("*.dc.html")} - {"Main.dc.html"}
unlisted = on_disk - seen_files
if unlisted:
    sys.exit(f"FAIL {len(unlisted)} artboard(s) on disk but not in any fragment: {sorted(unlisted)}")
ghosts = seen_files - on_disk
if ghosts:
    sys.exit(f"FAIL {len(ghosts)} artboard(s) listed but not on disk: {sorted(ghosts)}")

# Main.dc.html is the leading candidate, placed on the hero page
artboards.insert(0, {"file": "Main.dc.html", "x": -1700, "y": 0, "w": 1440, "h": 420,
                     "page": "hero", "title": "Main (leading candidate)"})

canvas = {
    "pages": [{"id": p, "name": PAGE_NAMES[p]} for p in PAGE_ORDER],
    "artboards": artboards,
    "annotations": annotations,
    "launch": {"view": "canvas", "page": "hero"},
}
(FOLDER / "canvas.json").write_text(json.dumps(canvas, indent=2))
print(f"ok: {len(artboards)} artboards ({len(on_disk)} authored + Main), "
      f"{len(annotations)} notes, {len(PAGE_ORDER)} pages -> canvas.json")

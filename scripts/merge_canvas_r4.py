#!/usr/bin/env python3
"""Merge canvas.part-*.json fragments into canvas.json for the round-4 tables canvas."""
import json, pathlib, sys

PAGE_ORDER = ["cvt", "mvf", "others", "price"]
PAGE_NAMES = {"cvt": "Congo vs Timneh", "mvf": "Male vs Female",
              "others": "Grey vs Others", "price": "Pricing"}
folder = pathlib.Path("docs/design/homepage-tables-r4")

artboards, annotations, seen_notes, seen_files = [], [], set(), set()
X_GAP = 3000  # each page laid on its own horizontal band

for i, page_id in enumerate(PAGE_ORDER):
    frag_path = folder / f"canvas.part-{page_id}.json"
    if not frag_path.exists():
        sys.exit(f"MISSING fragment: {frag_path}")
    frag = json.loads(frag_path.read_text())
    for a in frag["artboards"]:
        a["page"] = page_id
        artboards.append(a)
        seen_files.add(a["file"])
    for n in frag["annotations"]:
        n["page"] = page_id
        if n["id"] in seen_notes:
            sys.exit(f"dup note id {n['id']}")
        seen_notes.add(n["id"])
        annotations.append(n)

on_disk = {p.name for p in folder.glob("*.dc.html")} - {"Main.dc.html"}
unlisted = on_disk - seen_files
if unlisted:
    sys.exit(f"unlisted .dc.html files: {sorted(unlisted)}")
missing = seen_files - on_disk
if missing:
    sys.exit(f"fragment lists files not on disk: {sorted(missing)}")

# Heights are authoritative from the probe, never from a stale fragment.
heights_path = pathlib.Path("/tmp/r4-heights.json")
if heights_path.exists():
    heights = json.loads(heights_path.read_text())
    restacked = 0
    for a in artboards:
        h = heights.get(a["file"])
        if h and a["h"] != round(h * 1.05):
            a["h"] = round(h * 1.05)
            restacked += 1
    print(f"heights refreshed from probe: {restacked} corrected")
    # re-stack each page's rows so a corrected height cannot overlap the row below
    for page_id in PAGE_ORDER:
        rows = {}
        for a in (x for x in artboards if x["page"] == page_id):
            rows.setdefault(a["y"], []).append(a)
        y = 0
        for old_y in sorted(rows):
            band = rows[old_y]
            for a in band:
                a["y"] = y
            y += max(a["h"] for a in band) + 120
else:
    print("WARNING: no probe heights at /tmp/r4-heights.json — fragment heights used as-is")

canvas = {
    "pages": [{"id": p, "name": PAGE_NAMES[p]} for p in PAGE_ORDER],
    "artboards": artboards,
    "annotations": annotations,
    "launch": {"view": "canvas", "page": PAGE_ORDER[0]},
}
(folder / "canvas.json").write_text(json.dumps(canvas, indent=2))
print(f"canvas.json written: {len(artboards)} artboards, {len(annotations)} annotations, "
      f"{len(PAGE_ORDER)} pages")
for p in PAGE_ORDER:
    print(f"  {p:8s} {sum(1 for a in artboards if a['page']==p)} artboards")

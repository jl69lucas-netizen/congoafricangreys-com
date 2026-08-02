#!/usr/bin/env python3
"""
Generate the WebP variants a measured srcset plan asks for.

Naming follows the convention already in the tree (`foo-440.webp`), with one wrinkle that
has to be handled rather than assumed away: many masters ALREADY carry a width suffix
(`hero-jins-jeni-congo-pair-together-320.webp`). Appending would produce `...-320-240.webp`,
which reads as a 320 that is also a 240. The trailing width is replaced instead — and every
derived name is checked for a collision with an unrelated existing file before anything is
written, because silently overwriting a real image to satisfy a byte metric is a worse
outcome than a missing variant.

    python3 scripts/image_srcset_variants.py --map map.json [--apply]

Without --apply it prints what it would do and writes nothing.
"""
import argparse
import json
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")

ap = argparse.ArgumentParser()
ap.add_argument("--map", required=True)
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

plan = json.load(open(args.map))

# (src_path, width) pairs, from the clean tags only — a tag with a conflict is not patched,
# so generating its variants would leave orphan files nobody references.
wanted = {}
for t in plan["tags"]:
    if t.get("conflicts"):
        continue
    for f in t["files"]:
        for w in t["wantWidths"]:
            wanted.setdefault((f, w), None)

print(f"{len(wanted)} (file,width) variant(s) requested")


def variant_name(src, w):
    """`/a/foo-320.webp` + 240 -> `/a/foo-240.webp`; `/a/foo.webp` + 240 -> `/a/foo-240.webp`."""
    stem, ext = os.path.splitext(src)
    stem = re.sub(r"-\d{2,4}$", "", stem)
    return f"{stem}-{w}{ext}"


def fs(p):
    return os.path.join(PUBLIC, p.lstrip("/"))


made, skipped, missing, collisions = 0, 0, [], []

for (src, w) in sorted(wanted):
    master = fs(src)
    if not os.path.exists(master):
        missing.append(src)
        continue
    out_rel = variant_name(src, w)
    out = fs(out_rel)

    if os.path.exists(out):
        # Already there. Only accept it if it really is the width we need — a name that
        # happens to match is not evidence of content that matches.
        try:
            with Image.open(out) as im:
                if abs(im.width - w) <= 2:
                    skipped += 1
                    continue
                collisions.append((out_rel, im.width, w))
                continue
        except Exception:
            collisions.append((out_rel, "unreadable", w))
            continue

    if not args.apply:
        made += 1
        continue

    with Image.open(master) as im:
        if im.width <= w:
            skipped += 1
            continue
        h = round(im.height * w / im.width)
        im2 = im.convert("RGBA") if im.mode in ("P", "LA") else im
        im2 = im2.resize((w, h), Image.LANCZOS)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        # quality 82 / method 6 matches what the existing -440/-760 siblings were cut at.
        im2.save(out, "WEBP", quality=82, method=6)
    made += 1

print(f"  generated: {made}")
print(f"  already present at the right width: {skipped}")
if missing:
    print(f"  MASTER NOT FOUND ({len(missing)}): {missing[:8]}")
if collisions:
    print(f"  NAME COLLISION — refusing to overwrite ({len(collisions)}):")
    for n, have, want in collisions[:10]:
        print(f"    {n}: exists at {have}px, plan wants {want}px")
if not args.apply:
    print("\n(dry run — pass --apply to write)")

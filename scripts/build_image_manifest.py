#!/usr/bin/env python3
"""
Write src/data/image-widths.json — every image under public/ and its real pixel width.

A shared component receives its image as a PROP, so it cannot know that image's width, and
a hardcoded `w` descriptor is therefore a claim about a file the component has never seen.
Measured 2026-08-02: `NewsletterV2` emitted `${img} 640w` for images including a 375px
master, and asked for a `-390` variant of it that cannot exist. A wrong descriptor makes the
browser's whole selection wrong; a missing candidate is a BROKEN IMAGE. Both are worse than
the oversized image the srcset was added to remove.

With this manifest the component looks the width up at build time and emits only candidates
that actually exist, with descriptors that are true.

    python3 scripts/build_image_manifest.py
"""
import json
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")
OUT = os.path.join(ROOT, "src", "data", "image-widths.json")

widths = {}
for root, _dirs, files in os.walk(PUBLIC):
    for f in files:
        if not f.lower().endswith((".webp", ".png", ".jpg", ".jpeg")):
            continue
        p = os.path.join(root, f)
        rel = "/" + os.path.relpath(p, PUBLIC).replace(os.sep, "/")
        try:
            with Image.open(p) as im:
                widths[rel] = im.width
        except Exception:
            continue

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as fh:
    json.dump(dict(sorted(widths.items())), fh, indent=0)
    fh.write("\n")

print(f"{len(widths)} image(s) indexed -> {os.path.relpath(OUT, ROOT)}")

#!/usr/bin/env python3
"""
Generate every srcset candidate that the BUILT site references but does not ship.

Why this is a permanent script and not a one-off cleanup:

A `srcset` written onto a SHARED COMPONENT's `<img>` applies to all 108 pages, not just the
pages that were measured. `Newsletter.astro` takes its image as a prop, so the moment its
tag emits `…-390.webp`, every page passing a different `img=` needs a 390 variant of ITS
image too. Measuring 15 pages and generating variants only for the files those pages
happened to render left 15 candidates referenced-but-absent — and a missing candidate is a
BROKEN IMAGE, which is strictly worse than the oversized image the srcset was added to fix.
The render harness reports it as "failed to decode and could not be measured".

Run after any srcset change, and after adding a page or image that feeds a patched
component. It is idempotent.

    python3 scripts/image_srcset_fill_missing.py [--apply]
"""
import argparse
import glob
import os
import re
import sys

from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

refs = set()
for f in glob.glob("dist/**/*.html", recursive=True):
    html = open(f, encoding="utf8", errors="ignore").read()
    for m in re.finditer(r'srcset="([^"]+)"', html):
        for part in m.group(1).split(","):
            part = part.strip()
            if not part:
                continue
            u = part.split()[0]
            if u.startswith("/"):
                refs.add(u)

missing = sorted(u for u in refs if not os.path.exists("dist" + u))
print(f"{len(refs)} srcset candidate(s) referenced · {len(missing)} missing")

WIDTH_RE = re.compile(r"^(.*?)-(\d{2,4})(\.[A-Za-z0-9]+)$")

made, failed = 0, []
for rel in missing:
    m = WIDTH_RE.match(rel)
    if not m:
        failed.append((rel, "filename carries no -<width> suffix"))
        continue
    stem, width, ext = m.group(1), int(m.group(2)), m.group(3)

    # The master is the same stem with no width suffix; fall back to any wider sibling.
    candidates = [f"{stem}{ext}"] + [
        os.path.relpath(p, "public").replace(os.sep, "/")
        for p in sorted(glob.glob(f"public{stem}-*{ext}"))
    ]
    master = None
    for c in candidates:
        p = c if c.startswith("public") else "public" + ("/" + c if not c.startswith("/") else c)
        if not os.path.exists(p):
            continue
        try:
            with Image.open(p) as im:
                if im.width > width:
                    master = p
                    break
        except Exception:
            continue
    if not master:
        failed.append((rel, "no source wide enough to downscale from"))
        continue

    out = "public" + rel
    if not args.apply:
        made += 1
        continue
    with Image.open(master) as im:
        h = round(im.height * width / im.width)
        im2 = im.convert("RGB") if ext.lower() in (".jpg", ".jpeg") and im.mode != "RGB" else im
        im2 = im2.resize((width, h), Image.LANCZOS)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        if ext.lower() in (".jpg", ".jpeg"):
            im2.save(out, "JPEG", quality=82, optimize=True)
        else:
            im2.save(out, "WEBP", quality=82, method=6)
    made += 1

print(f"  {'generated' if args.apply else 'would generate'}: {made}")
if failed:
    print(f"  COULD NOT GENERATE ({len(failed)}) — these ship as broken images:")
    for rel, why in failed:
        print(f"    {rel}: {why}")
if not args.apply:
    print("\n(dry run — pass --apply to write)")
sys.exit(1 if failed else 0)

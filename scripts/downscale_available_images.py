#!/usr/bin/env python3
"""One-shot: downscale oversized /available/ cluster WebPs to ~2x their CSS display
size. Mirrors commit 31368d7. Only shrinks (never upscales); re-encodes WebP q=80.
Run from repo root: python3 scripts/downscale_available_images.py"""
import io
import os
from PIL import Image

# (path, target_width)  -- height auto from aspect ratio. None = re-encode only.
JOBS = [
    ("public/birds/roys/roys-hero.webp", 1112),
    ("public/birds/bery/bery-hero.webp", 760),
    ("public/birds/amie/amie-hero.webp", 760),
    ("public/birds/amie/amie-personality.webp", 760),
    ("public/birds/roys/roys-personality.webp", 760),
    ("public/birds/elad/elad-at-a-glance-card.webp", 600),
    ("public/birds/elad/elad-personality-profile.webp", 1100),
    ("public/birds/jins-jeni/meet-jins-jeni.webp", 800),
    ("public/birds/jins-jeni/jins-jeni-pair-1.webp", 760),
    ("public/birds/jins-jeni/jins-jeni-pair-5.webp", 760),
    ("public/african-grey-breeder-with-bird-midland-tx.webp", 760),
    ("public/roys-congo-african-grey-male-4-months.webp", 760),
    ("public/bery-congo-african-grey-female-1-year.webp", 760),
    ("public/birds/amie/amie-handfed.webp", 768),
    ("public/hero-available-african-greys-for-sale.webp", None),
]

for path, target_w in JOBS:
    if not os.path.exists(path):
        print(f"SKIP missing {path}")
        continue
    im = Image.open(path)
    w0, h0, kb0 = im.width, im.height, os.path.getsize(path) // 1024
    if target_w and im.width > target_w:
        new_h = round(im.height * target_w / im.width)
        im = im.resize((target_w, new_h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=80, method=6)
    if len(buf.getvalue()) < os.path.getsize(path):
        with open(path, "wb") as f:
            f.write(buf.getvalue())
        print(f"{path}: {w0}x{h0} {kb0}KB -> {im.width}x{im.height} {len(buf.getvalue())//1024}KB")
    else:
        print(f"{path}: {w0}x{h0} {kb0}KB -> SKIPPED (re-encode would grow to {len(buf.getvalue())//1024}KB)")

#!/usr/bin/env python3
"""One-off: process Amie's raw assets → SEO-named, <~100KB WebP in public/birds/amie/."""
import os
from PIL import Image

SRC = "/Users/apple/Downloads/CAG/assets/brand/AMIE"
DST = "/Users/apple/Downloads/CAG/public/birds/amie"
os.makedirs(DST, exist_ok=True)

# (source, dest_name, max_width, target_kb)  text-dense infographics get a slightly higher ceiling for legibility
JOBS = [
    ("Amie-female-congo-african-grey-ready-for-sale.webp", "amie-hero.webp", 1200, 100),
    ("Why-Amie-is-special.png",                            "amie-personality.webp", 1080, 120),
    ("what-amie-arrives-with.webp",                        "amie-documentation.webp", 880, 120),
    ("whats-included-with-amie.webp",                      "amie-whats-included.webp", 1200, 120),
    ("spoonfed-african-grey-baby-for-sale.webp",           "amie-health-handfeeding.webp", 900, 90),
    ("amie-african-grey-family-long-term.webp",            "amie-family-long-term.webp", 1200, 100),
    ("Bonding african grey at CAGs.webp",                  "amie-bonding.webp", 760, 90),
    ("Amie-handfed-baby-female-congo-grey-available.webp", "amie-handfed.webp", 900, 90),
    ("Amie-calm-female-african-grey-parrot-for-sale.webp", "amie-calm.webp", 900, 90),
    ("african-grey-parrot-seeds-nuts.webp",                "amie-diet-seeds-nuts.webp", 1000, 95),
    ("how-amie-gets-home.webp",                            "amie-shipping.webp", 1200, 120),
    ("cag-us-delivery-map-base.webp",                      "cag-us-delivery-map-base.webp", 1200, 110),
    ("amie-congo-african-grey-female-3-months.webp",       "amie-gallery-card.webp", 800, 80),
]

def fit(src, dst, max_w, target_kb):
    im = Image.open(src).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    for q in range(86, 49, -4):
        im.save(dst, "WEBP", quality=q, method=6)
        kb = os.path.getsize(dst) / 1024
        if kb <= target_kb:
            return im.width, im.height, kb, q
    # last attempt: shrink width 15% and retry once at q70
    im = im.resize((round(im.width*0.85), round(im.height*0.85)), Image.LANCZOS)
    im.save(dst, "WEBP", quality=70, method=6)
    return im.width, im.height, os.path.getsize(dst)/1024, 70

for s, d, mw, tk in JOBS:
    sp = os.path.join(SRC, s); dp = os.path.join(DST, d)
    if not os.path.exists(sp):
        print(f"MISSING  {s}"); continue
    w, h, kb, q = fit(sp, dp, mw, tk)
    flag = "" if kb <= tk else "  ⚠over"
    print(f"{d:34} {w}x{h}  {kb:5.0f}KB  q{q}{flag}")

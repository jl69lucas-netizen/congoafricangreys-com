#!/usr/bin/env python3
"""Bake infographics to <100 KB WebP at NATIVE ratio, plus a -760 sibling.

Infographics carry baked-in text: never cover-crop them (cag-page-hardening §1c).
Real photos go through scripts/reframe_og.py instead — this script never crops.

Usage:
    python3 scripts/bake_infographics.py <src_dir> <dst_dir> <stem> [<stem> ...]
"""
import sys
import pathlib
from PIL import Image

MAXKB = 100


def walk(im, out, maxkb=MAXKB):
    """Quality-walk down until the file fits the budget."""
    q = 86
    for q in range(86, 39, -3):
        im.save(out, "WEBP", quality=q, method=6)
        if out.stat().st_size <= maxkb * 1024:
            return q
    return q


def bake(src, dst_dir, stem):
    im = Image.open(src).convert("RGB")
    dst_dir.mkdir(parents=True, exist_ok=True)

    full = dst_dir / f"{stem}.webp"
    q1 = walk(im, full)

    w760 = 760
    h760 = round(im.height * w760 / im.width)
    sib = dst_dir / f"{stem}-760.webp"
    q2 = walk(im.resize((w760, h760), Image.LANCZOS), sib)

    print(
        f"{stem}: {im.width}x{im.height} q{q1} {full.stat().st_size // 1024}KB "
        f"| {w760}x{h760} q{q2} {sib.stat().st_size // 1024}KB"
    )
    return im.width, im.height


if __name__ == "__main__":
    src_dir, dst_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    for name in sys.argv[3:]:
        bake(src_dir / f"{name}.webp", dst_dir, name)

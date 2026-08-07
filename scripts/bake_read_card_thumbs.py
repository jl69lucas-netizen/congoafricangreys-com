#!/usr/bin/env python3
"""bake_read_card_thumbs.py — cut further-reading thumbnails from the REAL hero image
of each linked page.

Breeder rule, 2026-08-07 (binding, rules/images.md `read-card-thumb-is-target-hero`):
a "Keep reading" / further-reading card must show the hero image of the page it links to.
Showing the *source* page's own infographic promises one destination and delivers another,
and it was shipping that way on the breeding-pair page.

  # audit every built page's read-cards and report mismatches
  python3 scripts/bake_read_card_thumbs.py --audit

  # cut thumbs for one page's cards into its image folder
  python3 scripts/bake_read_card_thumbs.py <source-slug> --out public/images/<folder>

Hero resolution order, most reliable first:
  1. <link rel="preload" as="image">           — the page declared its own LCP image
  2. first <img fetchpriority="high">          — same declaration, inline
  3. first content <img> that is not chrome    — logo/seam/emoji/icon/footer excluded

Gates measure dist/, so this reads dist/ and never source.
"""
import argparse
import io
import pathlib
import re
import sys
from typing import List, Optional, Tuple

from PIL import Image, ImageOps

DIST = pathlib.Path("dist")
CHROME = ("logo", "seam", "emoji", "icon", "footer", "sprite", "avatar")
THUMB = (320, 175)
WIDE = (760, 416)


def hero_of(slug):
    """The public path of <slug>'s own hero image, or None if it has none."""
    page = DIST / slug.strip("/") / "index.html"
    if not page.exists():
        return None
    html = page.read_text(errors="ignore")

    pre = re.search(r'<link[^>]*rel="preload"[^>]*as="image"[^>]*>', html)
    if pre:
        href = re.search(r'href="([^"]+)"', pre.group(0))
        if href:
            return href.group(1)

    for tag in re.findall(r"<img[^>]*>", html):
        src = (re.search(r'src="([^"]+)"', tag) or [None, ""])[1]
        if not src or any(k in src.lower() for k in CHROME):
            continue
        if "fetchpriority=\"high\"" in tag:
            return src
        return src
    return None


def read_cards(slug):
    """(href, img src) for every further-reading card on <slug>."""
    page = DIST / slug.strip("/") / "index.html"
    if not page.exists():
        return []
    html = page.read_text(errors="ignore")
    # `(.*?)</div>` was wrong: a card containing any nested <div> truncated the block, and
    # the audit silently examined 2 pages out of the 11 that have read-cards. Take the span
    # from the marker to the end of its <section> and pull the anchors that carry an <img>.
    start = re.search(r'<div class="read-cards"[^>]*>', html)
    if not start:
        return []
    tail = html[start.end():]
    block = tail.split("</section>")[0]
    out = []  # (href, img src)
    for href, inner in re.findall(r"<a\s[^>]*href=\"([^\"]+)\"(.*?)</a>", block, re.S):
        if "<img" not in inner:
            continue
        src = (re.search(r'src="([^"]+)"', inner) or [None, ""])[1]
        out.append((href, src))
    return out


def save(img, path, maxkb):
    q = 88
    while q >= 58:
        buf = io.BytesIO()
        img.save(buf, "WEBP", quality=q, method=6)
        if buf.tell() / 1024 <= maxkb or q == 58:
            path.write_bytes(buf.getvalue())
            return round(buf.tell() / 1024, 1)
        q -= 3
    return 0.0


def audit():
    """Report every read-card whose thumbnail is not cut from its target's hero."""
    bad = 0
    checked = 0
    for page in sorted(DIST.glob("*/index.html")):
        slug = page.parent.name
        cards = read_cards(slug)
        if not cards:
            continue
        for href, src in cards:
            checked += 1
            target = href.strip("/")
            # The thumb must be derived from the target: either it IS the target's hero
            # path, or it is a cut whose filename carries the target slug.
            hero = hero_of(target)
            stem = pathlib.Path(src).stem.replace("-320", "").replace("-760", "")
            # The naming convention IS the check: a cut is named read-<target-slug>-hero,
            # so a filename that does not carry the full target slug is not verifiable.
            # An earlier, looser heuristic (`hero stem's first segment appears in stem`)
            # passed a hand-named file that no machine could tie back to its target.
            ok = bool(hero) and (
                src == hero or target.replace("-", "") in stem.replace("-", "")
            )
            if not ok:
                bad += 1
                print(f"  MISMATCH  /{slug}/ card -> {href}")
                print(f"            shows {src}")
                print(f"            target hero {hero or 'NOT FOUND'}")
    print(f"\n{checked} read-card thumbnails checked, {bad} not cut from their target's hero")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?", default="")
    ap.add_argument("--out", default="")
    ap.add_argument("--audit", action="store_true")
    a = ap.parse_args()

    if not DIST.exists():
        sys.exit("dist/ missing — run `npx astro build` first. Gates measure dist, never source.")
    if a.audit:
        sys.exit(audit())
    if not a.slug or not a.out:
        sys.exit("give a slug and --out, or pass --audit")

    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for href, _src in read_cards(a.slug):
        target = href.strip("/")
        hero = hero_of(target)
        if not hero:
            print(f"  NOT FETCHED  {href} — no hero image found; leaving its thumb alone")
            continue
        srcfile = pathlib.Path("public") / hero.lstrip("/")
        if not srcfile.exists():
            print(f"  MISSING  {srcfile}")
            continue
        im = Image.open(srcfile).convert("RGB")
        stem = f"read-{target.replace('/', '-')}-hero"
        kb1 = save(ImageOps.fit(im, THUMB, Image.LANCZOS, centering=(0.5, 0.35)), out / f"{stem}-320.webp", 22)
        kb2 = save(ImageOps.fit(im, WIDE, Image.LANCZOS, centering=(0.5, 0.35)), out / f"{stem}-760.webp", 55)
        print(f"  {stem}  from {hero}  320:{kb1}KB 760:{kb2}KB")


if __name__ == "__main__":
    main()

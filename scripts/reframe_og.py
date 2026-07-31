#!/usr/bin/env python3
"""
reframe_og.py — bake a named OG framing style into a 16:9 (or any-aspect) on-page image
so the FULL bird always shows, no cover-crop head cutoffs. Engine behind the named
Styles in IMAGE-DESIGNS.md §7.

Styles:
  blurfill  (Style B / mC) — sharp CONTAINed subject centered over a blurred COVER copy of
                             itself. Full subject, no empty bars. Default for single birds.
  contain   (Style A / mB) — sharp CONTAINed subject over a warm cream->beige gradient.
                             Full subject, soft side padding.
  topcover  (Style E / mA / mH) — COVER fill anchored to the TOP so the head is never cut
                             (lower body/feet may crop). Punchy.

Usage:
  python3 scripts/reframe_og.py <src> <out> [--style blurfill] [--w 1408] [--h 768] \
        [--blur 30] [--sib <out-760>] [--sibw 760] [--sibh 415] [--maxkb 95]
The subject is centered full-HEIGHT, so any later COVER crop to a taller mobile aspect
(4:5, 1:1) keeps the whole bird (only blurred/padded sides crop away).
"""
import sys, argparse, io
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

def load(p): return Image.open(p).convert("RGB")

def fit_subject(im, fgw, fgh, allow_upscale):
    """Contain the subject inside the subject-safe box.

    thumbnail() only ever SHRINKS, so a small master (e.g. 310x400) left a postage
    stamp floating in blur inside a 1408x768 canvas. --fgup permits the upscale;
    CLAUDE.md IMAGE-DESIGNS 1a is explicit that a low-res master is upscaled to the
    box on purpose — uniform sizing beats pixel-peeping.
    """
    if not allow_upscale:
        fg = im.copy(); fg.thumbnail((fgw, fgh), Image.LANCZOS)
        return fg
    s = min(fgw / im.width, fgh / im.height)
    return im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)

def blurfill(im, W, H, blur, fgw, fgh, fgup=False):
    bg = ImageOps.fit(im, (W, H), Image.LANCZOS)               # cover
    bg = bg.filter(ImageFilter.GaussianBlur(blur))
    bg = ImageEnhance.Brightness(bg).enhance(0.92)             # settle it behind the subject
    fg = fit_subject(im, fgw, fgh, fgup)                       # contain within the subject-safe box
    canvas = bg.copy()
    canvas.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    return canvas

def gradient(W, H):
    # warm cream -> beige diagonal, echoing the page surface
    top = (250, 247, 244); bot = (243, 227, 216)
    g = Image.new("RGB", (W, H))
    px = g.load()
    for y in range(H):
        t = y / (H - 1)
        r = int(top[0] + (bot[0]-top[0]) * t)
        gg = int(top[1] + (bot[1]-top[1]) * t)
        b = int(top[2] + (bot[2]-top[2]) * t)
        for x in range(W): px[x, y] = (r, gg, b)
    return g

def contain(im, W, H):
    canvas = gradient(W, H)
    fg = im.copy(); pad = 0.90
    fg.thumbnail((int(W*pad), int(H*pad)), Image.LANCZOS)
    canvas.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    return canvas

def topcover(im, W, H):
    return ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.5, 0.0))

def save_webp(img, path, maxkb):
    q = 86
    while q >= 60:
        buf = io.BytesIO(); img.save(buf, "WEBP", quality=q, method=6)
        if buf.tell() / 1024 <= maxkb or q == 60:
            with open(path, "wb") as f: f.write(buf.getvalue())
            return round(buf.tell()/1024, 1), q
        q -= 3

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--style", default="blurfill", choices=["blurfill","contain","topcover"])
    ap.add_argument("--w", type=int, default=1408); ap.add_argument("--h", type=int, default=768)
    ap.add_argument("--blur", type=int, default=30)
    ap.add_argument("--sib", default=""); ap.add_argument("--sibw", type=int, default=760); ap.add_argument("--sibh", type=int, default=415)
    ap.add_argument("--maxkb", type=int, default=95)
    # dual-safe: constrain the sharp subject so a later mobile 4:5 cover crop (central 4/5*H wide)
    # never clips it. Default full box; pass --mobcrop 4:5 to auto-set, or --fgmaxw explicitly.
    ap.add_argument("--mobcrop", default=""); ap.add_argument("--fgmaxw", type=int, default=0)
    # opt-in: let a small master scale UP to the subject-safe box instead of floating in blur
    ap.add_argument("--fgup", action="store_true")
    a = ap.parse_args()
    fgw, fgh = a.w, a.h
    if a.fgmaxw: fgw = a.fgmaxw
    elif a.mobcrop:
        rw, rh = (int(x) for x in a.mobcrop.split(":")); fgw = int(a.h * rw / rh)
    im = load(a.src)
    fn = {"blurfill": lambda: blurfill(im, a.w, a.h, a.blur, fgw, fgh, a.fgup),
          "contain":  lambda: contain(im, a.w, a.h),
          "topcover": lambda: topcover(im, a.w, a.h)}[a.style]
    out = fn()
    kb, q = save_webp(out, a.out, a.maxkb)
    print(f"  {a.out}  {a.w}x{a.h}  {kb}KB q{q}  [{a.style}]")
    if a.sib:
        sib = ImageOps.fit(out, (a.sibw, a.sibh), Image.LANCZOS)
        kb2, q2 = save_webp(sib, a.sib, 55)
        print(f"  {a.sib}  {a.sibw}x{a.sibh}  {kb2}KB q{q2}")

if __name__ == "__main__":
    main()

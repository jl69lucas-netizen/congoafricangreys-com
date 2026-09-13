#!/usr/bin/env python3
"""font_fallback_metrics.py — compute the metric-matched fallback @font-face blocks.

  pip install fonttools brotli   # generator only; the build does not need it
  python3 scripts/font_fallback_metrics.py

WHY (2026-09-13). The old fallbacks in direction-d.css were hand-approximated against
local('Georgia'), which PageSpeed's Linux Chrome does not have, with no bold or italic cut
(the Newsreader ascent was guessed at 98%; measured, it is 73%). The bases here are Arial
and Times New Roman because Linux ships
metric-IDENTICAL clones of both (Liberation Sans / Arimo, Liberation Serif / Tinos), so one
set of overrides is correct on macOS, Windows and Linux alike.

Width is the letter-frequency-weighted average advance (the capsize / Next.js method), not
OS/2 xAvgCharWidth, which averages every glyph including ones English text never uses.
Overrides follow the Next.js formula: ascent-override = ascent / (UPM * size-adjust).
"""
import pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = pathlib.Path(__file__).resolve().parents[1]
SYSTEM = pathlib.Path("/System/Library/Fonts/Supplemental")

# English letter frequencies (per 1000 chars incl. space), as used by capsize.
FREQ = {" ": 180, "e": 102, "t": 75, "a": 65, "o": 62, "i": 57, "n": 57, "s": 53, "h": 50,
        "r": 49, "d": 34, "l": 33, "u": 23, "c": 22, "m": 20, "w": 19, "f": 18, "g": 16,
        "y": 16, "p": 15, "b": 12, "v": 8, "k": 6, "j": 1, "x": 1, "q": 1, "z": 1}

# (family, weight range, style, web font, instance axes, system fallback, local() names)
# Headings render at 600 and the hero <em> in italic: one regular face would leave the
# browser SYNTHESISING bold/italic from it, whose widths match nothing, so the heading
# rewraps on swap. Each weight band gets its own face against the real bold/italic cut.
SANS = ["Arial", "Liberation Sans", "Arimo", "Helvetica"]
SERIF = ["Times New Roman", "Liberation Serif", "Tinos"]
PAIRS = [
    ("IBM Plex Sans Fallback", "100 500", "normal", "ibm-plex-sans", {"wght": 400}, "Arial.ttf", SANS),
    ("IBM Plex Sans Fallback", "550 900", "normal", "ibm-plex-sans", {"wght": 600}, "Arial Bold.ttf",
     [f"{n} Bold" for n in SANS]),
    ("Newsreader Fallback", "100 500", "normal", "newsreader-roman", {"wght": 400, "opsz": 18}, "Times New Roman.ttf",
     SERIF + ["Times"]),
    ("Newsreader Fallback", "550 900", "normal", "newsreader-roman", {"wght": 600, "opsz": 18},
     "Times New Roman Bold.ttf", [f"{n} Bold" for n in SERIF]),
    ("Newsreader Fallback", "100 900", "italic", "newsreader-italic", {"opsz": 18},
     "Times New Roman Italic.ttf", [f"{n} Italic" for n in SERIF]),
]


def avg_width(font):
    cmap, hmtx, upm = font.getBestCmap(), font["hmtx"], font["head"].unitsPerEm
    total = sum(FREQ.values())
    return sum(hmtx[cmap[ord(ch)]][0] * n for ch, n in FREQ.items()) / total / upm


def vmetrics(font):
    os2, hhea, upm = font["OS/2"], font["hhea"], font["head"].unitsPerEm
    if os2.fsSelection & (1 << 7):  # USE_TYPO_METRICS
        return os2.sTypoAscender / upm, -os2.sTypoDescender / upm, os2.sTypoLineGap / upm
    return hhea.ascent / upm, -hhea.descent / upm, hhea.lineGap / upm


def face(name, weight, style, web_stem, axes, fallback_file, locals_):
    web = TTFont(ROOT / "public/fonts" / f"{web_stem}.woff2")
    if "fvar" in web:
        present = {a.axisTag for a in web["fvar"].axes}
        web = instancer.instantiateVariableFont(web, {k: v for k, v in axes.items() if k in present})
    fb = TTFont(SYSTEM / fallback_file)
    size_adjust = avg_width(web) / avg_width(fb)
    asc, desc, gap = vmetrics(web)
    src = ", ".join(f"local('{n}')" for n in locals_)
    return (f"@font-face {{\n  font-family: '{name}';\n  font-weight: {weight};\n  font-style: {style};\n"
            f"  src: {src};\n"
            f"  size-adjust: {size_adjust * 100:.2f}%;\n"
            f"  ascent-override: {asc / size_adjust * 100:.2f}%;\n"
            f"  descent-override: {desc / size_adjust * 100:.2f}%;\n"
            f"  line-gap-override: {gap / size_adjust * 100:.2f}%;\n}}")

if __name__ == "__main__":
    print("\n".join(face(*p) for p in PAIRS))

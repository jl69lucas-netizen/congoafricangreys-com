#!/usr/bin/env python3
"""Scaffold amie/index.astro from roys/index.astro via safe regex transforms.
Bespoke angle prose is rewritten afterward by hand; this only handles
names, image paths, video paths, facts, sex, and pronouns deterministically."""
import re

src = "/Users/apple/Downloads/CAG/src/pages/available/roys/index.astro"
dst = "/Users/apple/Downloads/CAG/src/pages/available/amie/index.astro"
t = open(src).read()

# 1) Literal image/video path remaps (BEFORE generic roys->amie)
paths = {
    "/birds/roys/roys-trust-panel.webp":        "/birds/amie/amie-documentation.webp",
    "/roys-congo-african-grey-male-4-months.webp":"/birds/amie/amie-handfed.webp",
    "/birds/roys/roys-gallery-1.webp":          "/birds/amie/amie-health-handfeeding.webp",
    "/birds/roys/roys-gallery-2.webp":          "/birds/amie/amie-calm.webp",
    "/birds/roys/roys-gallery-3.webp":          "/birds/amie/amie-handfed.webp",
    "/birds/roys/roys-gallery-4.webp":          "/birds/amie/amie-bonding.webp",
    "/birds/roys/roys-gallery-5.webp":          "/birds/amie/amie-bonding.webp",
    "/birds/roys/african-grey-parrot-veggies.webp":"/birds/amie/amie-diet-seeds-nuts.webp",
    "/birds/roys/roys-video-playing.mp4":       "/birds/amie/amie-video.mp4",
    "/birds/roys/roys-video-eating.mp4":        "/birds/amie/amie-video.mp4",
}
for a, b in paths.items():
    t = t.replace(a, b)

# 2) Generic name tokens
t = t.replace("ROYS", "AMIE").replace("Roys", "Amie").replace("roys", "amie")

# 3) Facts
t = t.replace("$2,300", "$2,500").replace('"2300"', '"2500"')
t = t.replace("4 months", "3 months").replace("4-month", "3-month").replace("4 mo", "3 mo")

# 4) Sex (word-boundary, case-sensitive so "Female"/"female" are never corrupted)
t = re.sub(r"\bMale Congo\b", "Female Congo", t)
t = re.sub(r"\bmale Congo\b", "female Congo", t)
t = t.replace("Male (DNA-sexed)", "Female (DNA-sexed)")
t = re.sub(r"\bis male\b", "is female", t)
t = re.sub(r"\bmale, 3 months\b", "female, 3 months", t)
t = t.replace("(male,", "(female,").replace("Male, 3 months", "Female, 3 months")

# 5) Pronouns (word-boundary)
for a, b in [(r"\bhe\b","she"),(r"\bHe\b","She"),(r"\bhim\b","her"),(r"\bHim\b","Her"),
             (r"\bhis\b","her"),(r"\bHis\b","Her"),(r"\bhimself\b","herself")]:
    t = re.sub(a, b, t)

open(dst, "w").write(t)
# Report stragglers to verify
import collections
for tok in ["roys","Roys"," he "," his "," him ","$2,300","4 months","Male Congo"]:
    n = t.count(tok)
    if n: print(f"STRAGGLER {tok!r}: {n}")
print("done ->", dst)

#!/usr/bin/env python3
"""Bake every candidate OG style at desktop/tablet/mobile and emit one HTML preview.

Breeder-facing. Writes to public/_preview/ so `npx astro build` publishes it and the
breeder can open it on a phone; the directory is removed once a style is chosen.
"""
import subprocess, pathlib, sys

SRC = pathlib.Path("assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR")
OUT = pathlib.Path("public/_preview/og")
OUT.mkdir(parents=True, exist_ok=True)

# Two masters with different shapes, so a style cannot look good by luck.
MASTERS = {
    "pair": SRC / "breeding pair of african grey parrots for sale.jpg",
    "solo": SRC / "talker-jane-african-grey-breeding-pair-sale-nearby.webp",
}
# (label, style, tint) — each keeps a neutral twin so the greyish bed stays visible.
VARIANTS = [
    ("F · Brand Blur (green)",   "brandblur", "green"),
    ("F · Brand Blur (neutral)", "brandblur", "neutral"),
    ("G · Duotone (cream)",      "duotone",   "cream"),
    ("G · Duotone (clay)",       "duotone",   "clay"),
    ("I · Framed (green)",       "framed",    "green"),
    ("I · Framed (neutral)",     "framed",    "neutral"),
    ("current · Blur-Fill",      "blurfill",  "neutral"),
]
SIZES = [("desktop", 1408, 768), ("tablet", 1024, 576), ("mobile", 720, 900)]

rows = []
for mk, mp in MASTERS.items():
    if not mp.exists():
        sys.exit(f"missing master: {mp}")
    for label, style, tint in VARIANTS:
        cells = []
        for sk, w, h in SIZES:
            name = f"{mk}-{style}-{tint}-{sk}.webp"
            cmd = ["python3", "scripts/reframe_og.py", str(mp), str(OUT / name),
                   "--style", style, "--tint", tint, "--w", str(w), "--h", str(h)]
            if sk == "mobile":
                cmd += ["--mobcrop", "4:5"]
            subprocess.run(cmd, check=True)
            cells.append(f'<figure><figcaption>{sk} {w}&times;{h}</figcaption>'
                         f'<img src="/_preview/og/{name}" alt="{label} {sk}"></figure>')
        rows.append(f'<section><h2>{label} <small>&mdash; {mk} master</small></h2>'
                    f'<div class="row">{"".join(cells)}</div></section>')

html = """<!doctype html><meta charset=utf-8><title>OG Style Preview — Breeding Pair</title>
<meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex>
<style>body{font:16px/1.5 system-ui;background:#faf7f4;color:#2b2018;margin:0;padding:24px}
h1{font-size:1.4rem}h2{font-size:1rem;margin:28px 0 8px;color:#2D6A4F}
small{color:#6b625a;font-weight:400}
.row{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
figure{margin:0}figcaption{font-size:.75rem;color:#6b625a;margin-bottom:4px}
img{width:100%;height:auto;border:1px solid #e6ddd4;border-radius:10px;display:block}</style>
<h1>OG framing styles &mdash; pick one for /african-grey-breeding-pair-for-sale/</h1>
<p>Every style shown at desktop, tablet and mobile, on two different masters.
Neutral = today's greyish/black bed. Green/clay/cream = CAG palette beds.
<strong>current &middot; Blur-Fill</strong> at the bottom is what ships today, for comparison.</p>
""" + "".join(rows)

pathlib.Path("sessions/2026-08-07-og-style-preview.html").write_text(html)
print(f"wrote {len(rows)} style rows -> public/_preview/og/")

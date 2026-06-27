# scripts/process-hero.py
from PIL import Image
import pathlib

SRC = pathlib.Path("assets/certified-breeders-african-grey-near-me.jpg .jpg")
OUT = pathlib.Path("public")

img = Image.open(SRC)
w, h = img.size  # 800 x 563

# ── Desktop crop ─────────────────────────────────────────────────────────────
# 2.4:1 cinematic cut — remove top/bottom equally so parrots + hand stay in frame
# 800 / 2.4 ≈ 333 → use 334 for even pixel
DESKTOP_H = 334
top = (h - DESKTOP_H) // 2          # 114
desktop = img.crop((0, top, w, top + DESKTOP_H))   # 800 × 334
desktop.save(OUT / "hero-desktop.webp", "WEBP", quality=85, method=6)
print(f"Desktop saved: {desktop.size}")

# ── Mobile crop ──────────────────────────────────────────────────────────────
# Right 50% of image — keeps hand-feeding scene (the "Proof of Socialization")
# Crop x=400→800, full height → 400 × 563 (natural portrait)
mobile = img.crop((400, 0, w, h))    # 400 × 563
mobile.save(OUT / "hero-mobile.webp", "WEBP", quality=85, method=6)
print(f"Mobile saved: {mobile.size}")

print("Done. Verify file sizes:")
for f in [OUT / "hero-desktop.webp", OUT / "hero-mobile.webp"]:
    kb = f.stat().st_size // 1024
    print(f"  {f.name}: {kb} KB")

from PIL import Image
import os

BASE = "/Users/apple/Downloads/CAG"
OUT  = f"{BASE}/public/emoji"
SIZE = (72, 72)

sources = {
    "cag-congo.png":   "emojis.com african-grey-parrot-emoji.png",
    "cag-timneh.png":  "emojis.com african-grey-parrot.png",
}

for out_name, src_name in sources.items():
    img = Image.open(f"{BASE}/{src_name}").convert("RGBA")
    w, h = img.size
    s = min(w, h)
    img = img.crop(((w-s)//2, (h-s)//2, (w+s)//2, (h+s)//2))
    img = img.resize(SIZE, Image.LANCZOS)
    img.save(f"{OUT}/{out_name}", "PNG", optimize=True)
    print(f"Saved {out_name} {img.size}")

#!/usr/bin/env bash
# generate_nb_image.sh — Generate an image via the Google Gemini image API.
#
# Usage: ./scripts/generate_nb_image.sh "PROMPT" "output.png" [ASPECT] [LANE]
#   ASPECT  16:9 (default) · 4:3 · 1:1 · 3:4 · 9:16
#   LANE    flash  = gemini-3.1-flash-image  @ 1K   $0.067/image   (default)
#           cheap  = gemini-2.5-flash-image  @ 1024 $0.039/image
#
# Example: ./scripts/generate_nb_image.sh "CAG infographic..." "cag-inf-shipping.png" "16:9"
#
# LANE POLICY (breeder, 2026-09-12): these two lanes ONLY. gemini-3-pro-image is
# $0.134/image — 2x flash, 3.4x cheap — and is refused by this script. The
# 2026-09-11 run put 64 images through Pro and drained the prepaid credit.
#
# Key:    .google-key (project root, gitignored) or GEMINI_API_KEY env var.
#         Never echo, cat or paste the key. See docs/reference/secure-credentials.md.
# Output: content/generated/<filename> + 1408x768 WebP (<95KB) + -760 sibling (<55KB)
#
# Retired, do not resurrect: imagen-3.0-generate-001 and the :predict shape are GONE.

set -euo pipefail

PROMPT="${1:-}"
OUTFILE="${2:-output.png}"
ASPECT="${3:-16:9}"
LANE="${4:-flash}"

if [ -z "$PROMPT" ]; then
  echo "Error: prompt required as first argument" >&2
  echo "Usage: ./scripts/generate_nb_image.sh \"PROMPT\" \"output.png\" [ASPECT] [flash|cheap]" >&2
  exit 1
fi

case "$LANE" in
  flash) MODEL="gemini-3.1-flash-image"; IMAGE_SIZE="1K"; PRICE="0.067" ;;
  cheap) MODEL="gemini-2.5-flash-image"; IMAGE_SIZE="";   PRICE="0.039" ;;
  *)
    echo "Error: lane '$LANE' is not allowed. Use 'flash' (gemini-3.1-flash-image, \$0.067)" >&2
    echo "       or 'cheap' (gemini-2.5-flash-image, \$0.039)." >&2
    echo "       gemini-3-pro-image (\$0.134) is off the menu by breeder policy 2026-09-12." >&2
    exit 1
    ;;
esac

if [ -f .google-key ]; then
  GEMINI_API_KEY=$(cat .google-key)
elif [ -z "${GEMINI_API_KEY:-}" ]; then
  echo "Error: .google-key not found and GEMINI_API_KEY not set" >&2
  echo "Setup: pbpaste > .google-key   (never echo the key)" >&2
  exit 1
fi

echo "Model: ${MODEL}${IMAGE_SIZE:+ @ $IMAGE_SIZE} | Aspect: ${ASPECT} | ~\$${PRICE}"
echo "Output: content/generated/${OUTFILE}"
mkdir -p content/generated

GEMINI_API_KEY="$GEMINI_API_KEY" \
PROMPT="$PROMPT" MODEL="$MODEL" ASPECT="$ASPECT" IMAGE_SIZE="$IMAGE_SIZE" OUTFILE="$OUTFILE" \
python3 - <<'PY'
import base64, json, os, sys, urllib.request, urllib.error

key   = os.environ["GEMINI_API_KEY"]
model = os.environ["MODEL"]
out   = os.path.join("content/generated", os.environ["OUTFILE"])

cfg = {"aspectRatio": os.environ["ASPECT"]}
if os.environ["IMAGE_SIZE"]:
    cfg["imageSize"] = os.environ["IMAGE_SIZE"]

body = {"contents": [{"parts": [{"text": os.environ["PROMPT"]}]}],
        "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": cfg}}

req = urllib.request.Request(
    f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
    data=json.dumps(body).encode(),
    headers={"Content-Type": "application/json", "x-goog-api-key": key})

try:
    data = json.load(urllib.request.urlopen(req, timeout=300))
except urllib.error.HTTPError as e:
    detail = e.read().decode("utf-8", "replace")
    print(f"API error {e.code}:\n{detail}", file=sys.stderr)
    if e.code == 429 and "credits" in detail:
        print("\nPrepaid credit is exhausted — top up at https://ai.studio/projects", file=sys.stderr)
    sys.exit(1)

parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
blob = next((p["inlineData"]["data"] for p in parts if "inlineData" in p), None)
if blob is None:
    print("No image returned. Response:\n" + json.dumps(data)[:1200], file=sys.stderr)
    sys.exit(1)

with open(out, "wb") as f:
    f.write(base64.b64decode(blob))

from PIL import Image
w, h = Image.open(out).size
print(f"Saved: {out}  ({w}x{h}, {os.path.getsize(out)//1024} KB)")
PY

# WebP export — cwebp is NOT installed on this machine; Pillow is (11.3.0).
# House delivery sizes: 1408x768 under 95KB, plus a -760.webp sibling under 55KB.
OUTFILE="$OUTFILE" python3 - <<'PY'
import os
from PIL import Image, ImageOps

src = os.path.join("content/generated", os.environ["OUTFILE"])
stem = os.path.splitext(src)[0]

for suffix, size, budget in (("", (1408, 768), 95), ("-760", (760, 415), 55)):
    dst = f"{stem}{suffix}.webp"
    img = ImageOps.fit(Image.open(src).convert("RGB"), size, Image.LANCZOS)
    for q in range(88, 39, -6):
        img.save(dst, "WEBP", quality=q, method=6)
        kb = os.path.getsize(dst) // 1024
        if kb <= budget:
            break
    print(f"WebP: {dst} ({size[0]}x{size[1]}, {kb} KB, q{q}){'  OVER BUDGET' if kb > budget else ''}")
PY

echo ""
echo "Done. Next: @cag-image-pipeline to move into public/images/<page>/ and update refs."

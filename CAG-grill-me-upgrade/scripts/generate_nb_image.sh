#!/usr/bin/env bash
# generate_nb_image.sh — Generate image via Google Imagen (Nano Banana 2)
# Usage: ./scripts/generate_nb_image.sh "PROMPT" "output-filename.png" [WIDTHxHEIGHT]
# Example: ./scripts/generate_nb_image.sh "CAG infographic..." "cag-infographic-congo-vs-timneh-nb.png" "1200x2133"
#
# Provider: Google Imagen 3 (= Nano Banana 2) via Google AI Studio API
# Key:      .google-key (project root) or GEMINI_API_KEY env var
# Output:   content/generated/<filename> + WebP variant

set -euo pipefail

PROMPT="${1:-}"
OUTFILE="${2:-output.png}"
SIZE="${3:-1200x2133}"

if [ -z "$PROMPT" ]; then
  echo "Error: prompt required as first argument" >&2
  echo "Usage: ./scripts/generate_nb_image.sh \"PROMPT\" \"output.png\" [WIDTHxHEIGHT]" >&2
  exit 1
fi

# Load API key from file or env
if [ -f .google-key ]; then
  GEMINI_API_KEY=$(cat .google-key)
elif [ -z "${GEMINI_API_KEY:-}" ]; then
  echo "Error: .google-key file not found and GEMINI_API_KEY env var not set" >&2
  echo "Setup: echo 'AIza...' > .google-key" >&2
  exit 1
fi

WIDTH="${SIZE%x*}"
HEIGHT="${SIZE#*x}"

echo "Generating via Google Imagen (Nano Banana 2)..."
echo "Size: ${WIDTH}x${HEIGHT} | Output: content/generated/${OUTFILE}"

mkdir -p content/generated

# Call Google Imagen 3 API
RESPONSE=$(curl -s \
  "https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-001:predict?key=${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"instances\": [{\"prompt\": $(echo "$PROMPT" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')}],
    \"parameters\": {
      \"sampleCount\": 1,
      \"aspectRatio\": \"9:16\"
    }
  }")

# Check for API error
if echo "$RESPONSE" | python3 -c 'import json,sys; d=json.load(sys.stdin); exit(0 if "predictions" in d else 1)' 2>/dev/null; then
  : # predictions key found — success
else
  echo "API Error:" >&2
  echo "$RESPONSE" | python3 -m json.tool >&2
  exit 1
fi

# Extract base64 and save PNG
echo "$RESPONSE" | python3 -c "
import json, sys, base64
d = json.load(sys.stdin)
b64 = d['predictions'][0]['bytesBase64Encoded']
with open('content/generated/${OUTFILE}', 'wb') as f:
    f.write(base64.b64decode(b64))
print('Saved: content/generated/${OUTFILE}')
"

# Convert to WebP (quality 85 — sharp at 300-350px display)
WEBP_OUT="content/generated/${OUTFILE%.*}.webp"
if command -v cwebp &>/dev/null; then
  cwebp -q 85 "content/generated/${OUTFILE}" -o "$WEBP_OUT" -quiet
  SIZE_KB=$(du -k "$WEBP_OUT" | cut -f1)
  echo "WebP: ${WEBP_OUT} (${SIZE_KB}KB)"
  echo ""
  echo "WebP target for 9:16 infographic: under 400KB. If over, re-run:"
  echo "  cwebp -q 70 content/generated/${OUTFILE} -o ${WEBP_OUT} -quiet"
else
  echo "Note: cwebp not found — skipping WebP (brew install webp)"
fi

echo ""
echo "Done. Next: @cag-image-pipeline to move to site/ and update HTML refs."
echo "Display CSS: max-width:350px; width:100%; height:auto;"

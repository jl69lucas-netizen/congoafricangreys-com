---
name: cag-image-generation
description: Generates context-aware images for CongoAfricanGreys.com pages using one of three providers — OpenAI DALL-E 3 (best quality), Google Gemini 2.0 Flash + Imagen 3 fallback (fast, photorealistic), or Anthropic Claude (refines prompt then calls OpenAI). Reads page content to extract section context before generating. API keys stored in .openai-key / .google-key / .anthropic-key in project root. Produces square/portrait/landscape variants, then auto-optimizes to WebP. Hands off to cag-image-pipeline agent for placement. Use when the breeder needs images generated automatically rather than via Midjourney manually.
---

# CAG Image Generation Skill

**Announce at start:** "Using cag-image-generation skill to generate and optimize images for [page/section]."

---

## Provider Selection Guide

| Provider | Command flag | Best for | Key file |
|----------|-------------|---------|---------|
| OpenAI DALL-E 3 | `openai` (default) | Creative/stylized, reliable | `.openai-key` |
| Google Gemini 2.0 Flash | `google` | Photorealistic lifestyle shots; falls back to Imagen 3 | `.google-key` |
| Anthropic Claude | `anthropic` | Claude refines prompt → calls OpenAI to generate | `.anthropic-key` + `.openai-key` |

**Recommendation for CAG:** Use `google` for lifestyle/bird photos (photorealistic, Gemini 2.0 Flash quality). Use `openai` for infographics, icons, and brand assets. Use `anthropic` when the prompt feels too generic and needs Claude to sharpen it first.

---

## Prerequisites

Before running, verify:
```bash
# Check at least one key exists
for KEY in .openai-key .google-key .anthropic-key; do
  test -f "$KEY" && echo "✓ $KEY found" || echo "✗ $KEY missing"
done

# Check cwebp is installed (for optimization)
command -v cwebp && echo "cwebp ready" || echo "Install: brew install webp"

# Check scripts exist
ls scripts/generate_image.sh scripts/optimize_images.sh
```

If scripts don't exist yet, they live in the MFS project at `/Users/apple/Downloads/MFS/scripts/`. Copy them:
```bash
cp /Users/apple/Downloads/MFS/scripts/generate_image.sh scripts/
cp /Users/apple/Downloads/MFS/scripts/optimize_images.sh scripts/
chmod +x scripts/generate_image.sh scripts/optimize_images.sh
```

If no key files exist: ask the breeder which provider to use first, then create the key file:
- OpenAI: `echo 'sk-...' > .openai-key`
- Google: `echo 'AIza...' > .google-key` (get key at https://aistudio.google.com/apikey)
- Anthropic: `echo 'sk-ant-...' > .anthropic-key`

---

## Step 1: Read Page Context

Before generating any image, read the target page or section:

```bash
# Example: read the hero section of the homepage
grep -A 30 'class="cag-hero"' site/content/index.html | head -35

# Or read markdown content
head -50 site/content/african-grey-for-sale.md
```

Extract:
- Primary topic (Congo African Grey, Timneh, care guide, etc.)
- Buyer persona on that page (family, experienced bird owner, first-time parrot owner)
- Variant if applicable (Congo CAG vs Timneh TAG)
- Emotional tone (trust + intelligence + longevity)
- Whether the page is CITES-sensitive (never imply wild-caught in imagery)

---

## Step 2: Build the Generation Prompt

Combine page context with CAG brand guidelines:

**CAG brand guidelines for image prompts:**
- Bird: African Grey parrot (Congo = larger, darker grey, red tail; Timneh = smaller, darker charcoal, maroon tail)
- Style: warm, lifestyle photography feel — natural light, home environment
- Setting: home perch, living room, shoulder of owner, garden/natural perch — NEVER an aviary cage or clinical setting
- People: real-looking families or individuals interacting with the bird
- Avoid: wire cages, aviary settings, clinical/breeder facility backgrounds, any imagery that implies captivity or wild capture
- Color palette: warm natural tones consistent with the site design

**Prompt template:**

```
[SCENE DESCRIPTION] featuring a [CONGO/TIMNEH] African Grey parrot
([CONGO: large, silver-grey plumage, bright red tail / TIMNEH: smaller, 
darker charcoal grey, maroon tail]),
[ACTION/POSE: perched on owner's shoulder / exploring a toy / vocalizing],
in a [SETTING: cozy living room / bright home study / natural outdoor perch],
warm natural lighting, lifestyle photography style,
shallow depth of field, warm natural color palette,
[BUYER_PERSONA: happy family / experienced bird enthusiast / first-time parrot owner],
professional pet photography quality, 8K, highly detailed.
No wire cages, no aviary settings, no clinical backgrounds, no crowded facilities.
Bird appears healthy, alert, and in a loving home environment.
```

**CITES safety rule:** Never describe imagery in a way that could suggest wild capture, transport crates, or importation. All images must show birds in settled, domestic home environments.

---

## Step 3: Generate the Image

```bash
# OpenAI DALL-E 3 — square (default provider)
./scripts/generate_image.sh \
  "YOUR PROMPT HERE" \
  "african-grey-[descriptor]-[page-slug]-cag-1024x1024.png" \
  "1024x1024" "openai"

# Google Gemini 2.0 Flash — portrait (photorealistic, recommended for lifestyle shots)
./scripts/generate_image.sh \
  "YOUR PROMPT HERE" \
  "african-grey-[descriptor]-[page-slug]-cag-portrait.png" \
  "1024x1792" "google"

# Anthropic-refined → OpenAI generates (when prompt feels too generic)
./scripts/generate_image.sh \
  "YOUR PROMPT HERE" \
  "african-grey-[descriptor]-[page-slug]-cag-refined.png" \
  "1024x1024" "anthropic"

# Landscape/wide (desktop hero banners)
./scripts/generate_image.sh \
  "YOUR PROMPT HERE" \
  "african-grey-[descriptor]-[page-slug]-cag-landscape.png" \
  "1792x1024" "openai"
```

Output goes to `content/generated/`.

---

## Step 4: Optimize to WebP

```bash
# Convert all generated images to WebP (typically 80-98% size reduction)
./scripts/optimize_images.sh content/generated/

# Verify output
ls -lh content/generated/*.webp
```

WebP targets:
- Square (1:1): under 200KB
- Portrait/landscape: under 400KB

If over target:
```bash
cwebp -q 70 content/generated/[filename].png -o content/generated/[filename].webp -quiet
```

---

## Step 5: Audit Before Handoff

Check each generated image:
1. Is it an African Grey parrot (not another species)?
2. Is the variant correct? (Congo = silver-grey + red tail; Timneh = charcoal + maroon tail)
3. Is the setting a home environment (not a cage, aviary, or facility)?
4. Does the bird appear healthy, alert, and engaged (not stressed or passive)?
5. Could any element of the image be misread as wild-caught or imported imagery?

If any image fails the audit, regenerate with more specific constraints — add "NOT a wire cage, NOT an aviary, NOT a shipping crate, in a loving home setting."

---

## Step 6: Hand Off to Image Pipeline

After images pass the audit:

```
@cag-image-pipeline
```

Provide:
- Source path: `content/generated/[files]`
- Target page: `site/content/[page]`
- Alt text intent (the pipeline will write final alt text)

CAG image-pipeline will:
1. Move files to `site/wp-content/uploads/`
2. Apply CAG SEO filename convention
3. Update `<img src>` references in target HTML/markdown
4. Call image-metadata skill for final alt text

---

## Aspect Ratio Quick Reference

| Ratio | DALL-E Size | Best for |
|-------|------------|---------|
| 1:1 Square | 1024×1024 | Bird cards, social thumbnails, profile photos |
| 9:16 Portrait | 1024×1792 | Mobile heroes, Instagram Stories |
| 16:9 Landscape | 1792×1024 | Desktop hero banners, blog post headers |

#### Hero-Specific Focal Point Rules

When generating OR processing a hero image for CongoAfricanGreys.com:

1. **Always include a human hand** interacting with a bird in the frame. This is the single strongest trust signal for African Grey buyers. Even a partially visible hand matters.
2. **Center or right placement for hand** — desktop hero text sits bottom-left, so hand on right keeps both elements visible without overlap.
3. **Crop guide for real photos (use `scripts/process-hero.py` with Pillow):**
   - Desktop (2.4:1): center-vertical crop, keep full width. Target 800×334 or 1920×800.
   - Mobile (portrait): take the right 50% of the source frame to isolate the hand-feeding scene. Target 400×563.
4. **`object-position`**: Use `object-[65%_45%]` in Tailwind for hero `<img>` tags — prevents viewport-width cropping from cutting the hand off the right side.
5. **Alt text must name the action**: `"Hand-reared Congo African Grey parrots being socialized by a certified breeder"` — Google reads this for E-E-A-T scoring on "certified breeder" queries.
6. **Format**: WebP, quality 85, under 200 KB. Run `python3 scripts/process-hero.py` after any new source image lands in `assets/`. Hero section height is `md:h-[480px]` — sized to fit description paragraph; do not reduce below this or description will be cut.
7. **`fetchpriority="high"`** on all hero `<img>` tags — direct LCP improvement, required for every hero.
8. **`<picture>` tag required** for heroes — serve `/hero-mobile.webp` on `max-width: 767px`, `/hero-desktop.webp` on `min-width: 768px`. Never a bare `<img>` for hero images.

---

## Rules

1. Always read the target page/section BEFORE generating — no generic stock-photo African Greys
2. Always run optimization step — never hand raw PNGs to cag-image-pipeline
3. Never generate imagery that could suggest wild-caught birds — CITES compliance applies to imagery too
4. Never share `.openai-key`, `.google-key`, or `.anthropic-key` — keep out of commits
5. Always produce at least the square (1:1) version as baseline; portrait/landscape optional
6. Audit every image: correct species, correct variant, home setting, healthy appearance
7. WebP target: under 200KB for square, under 400KB for landscape/portrait
8. Always hand off to cag-image-pipeline after optimization — never modify site/ directly from this skill
9. If buyer persona is "first-time parrot owner," ensure imagery is warm and approachable — not intimidating beak close-ups

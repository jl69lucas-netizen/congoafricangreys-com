---
name: cag-image-generation
description: Generates context-aware images for CongoAfricanGreys.com pages. Four providers — OpenAI DALL-E 3, Nano Banana 2 / Google Imagen (nanobanna flag, GEMINI_API_KEY), Anthropic Claude prompt-refine, or Claude Code HTML (native HTML/CSS infographics, no API). Pro-grade 9:16 prompt template (1200×2133px native, scales to 350px via CSS). Reads page content before generating. Keys in .openai-key / .google-key / .anthropic-key. WebP optimization. Hands off to cag-image-pipeline. Say "use Nano Banana", "use Claude", "use OpenAI", or "use Claude Code HTML" to select provider.
---

# CAG Image Generation Skill

**Announce at start:** "Using cag-image-generation skill to generate and optimize images for [page/section]."

---

## Provider Selection Guide

| Provider | Command flag | Best for | Key file |
|----------|-------------|---------|---------|
| OpenAI DALL-E 3 | `openai` (default) | Creative/stylized brand assets, icons | `.openai-key` |
| **Nano Banana 2 / Google Imagen** | `nanobanna` or `google` | Photorealistic lifestyle shots + AI infographics; 9:16 native high-res | `.google-key` (= `GEMINI_API_KEY`) |
| Anthropic Claude | `anthropic` | Claude refines prompt → calls OpenAI to generate | `.anthropic-key` + `.openai-key` |
| **Claude Code HTML** | `claude-html` | HTML/CSS infographics — no image file, no API cost, fully editable | none (Claude generates code) |
| **Higgsfield MCP** | `higgsfield` | Character-consistent lifestyle images, video clips, marketing studio assets | MCP UUID `dd46f66a` — no key file; already installed |

**How to invoke a specific provider:**
- "use Nano Banana" or "use nanobanna" → Nano Banana 2 (Google Imagen)
- "use Claude Code" or "use HTML" → `claude-html` mode (HTML/CSS infographic)
- "use OpenAI" → DALL-E 3
- "use Gemini" or "use Google" → Nano Banana 2 (same API)
- "use Higgsfield" or "use Higgsfield MCP" → Higgsfield MCP (character-consistent, video, marketing)

**Recommendation for CAG:** Use `claude-html` for 90% of infographics — instant, no cost, fully brand-compliant. Use `nanobanna` for one-off high-res 9:16 lifestyle shots. Use `higgsfield` when you need character consistency across multiple images, video generation, or marketing studio assets. Use `openai` for icons. Use `anthropic` when the prompt needs Claude to sharpen it first.

**Nano Banana 2 setup:**
```bash
echo 'AIza...' > .google-key
export GEMINI_API_KEY=$(cat .google-key)
# Verify .google-key is in .gitignore before committing
grep ".google-key" .gitignore || echo ".google-key" >> .gitignore
```

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

## Pro-Grade Prompt Template (Nano Banana 2 / Google Imagen)

Use this template when `nanobanna` or `google` is selected. Fill in ALL-CAPS placeholders. Generates at 9:16 / 1200×2133px native for perfect CSS downscale to 300–350px.

```
Role: Professional marketing designer for pet services specializing in responsive UI/UX assets.
Scene: SCENE_DESCRIPTION
Style: CAG brand aesthetic (Forest Green #2D6A4F, Clay #e8604c, Cream #faf7f4).
       Lora serif for headers, Sora sans for body text.
Technical:
  - Aspect Ratio: 9:16 (Vertical) for mobile/tablet optimization.
  - Dimensions: High-density 1200×2133px render for perfect downscaling to 300–350px desktop.
  - Camera: Professional studio macro-lens clarity, flat-lay design composition,
            ISO 100, f/8, sharp focus on all text elements.
  - Responsive Ready: Minimalist, uncluttered layout with balanced white space to ensure
                      legibility when downscaled to 300px width.
Text Constraints: Render title "TITLE_TEXT" in Lora serif at the top.
                  Use ALL CAPS for section headers. High contrast between text and background.
Content:
  - CONTENT_ITEM_1
  - CONTENT_ITEM_2
  - CONTENT_ITEM_3
Quality Levers: Photorealistic, professional graphic design, crisp vector-style iconography,
                ultra-sharp text rendering, 8K resolution, high fidelity, no blurry text.
CITES Safety: No wire cages, no aviary settings, no wild-capture imagery.
              All birds shown in loving home environments, domestic setting only.
```

**Iterative editing (Nano Banana conversational follow-up):**
- "Change the clay background to cream, keep the green headers and overall layout."
- "Make the title text larger — it must be readable at 300px width."
- "Use the attached image as a style reference and generate a new infographic matching this palette."

**Generation command:**
```bash
./scripts/generate_nb_image.sh "FULL_PROMPT_HERE" "cag-infographic-[slug]-nb.png" "1200x2133"
```

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

| Ratio | Native size (Nano Banana) | DALL-E size | Best for |
|-------|--------------------------|------------|---------|
| **9:16 Portrait** | **1200×2133px** | 1024×1792 | **AI infographics, mobile heroes — display at 300–350px via CSS** |
| 1:1 Square | 1024×1024 | 1024×1024 | Bird cards, social thumbnails, profile photos |
| 16:9 Landscape | 1792×1024 | 1792×1024 | Desktop hero banners, blog post headers |

**Why 1200×2133px for infographics:** Generating at native high-res then scaling down via CSS keeps text razor-sharp. At 300px display width, each CSS pixel maps to ~4 source pixels. Never generate at 300px — text will be blurry.

**Responsive CSS for AI infographic images:**
```css
.cag-ai-infographic {
  max-width: 350px;  /* enforced desktop width */
  width: 100%;       /* fluid on mobile/tablet */
  height: auto;      /* preserves 9:16 ratio */
  border-radius: 12px;
  box-shadow: 0 4px 24px rgba(60,30,10,0.15);
}
```

**HTML placement wrapper:**
```html
<div style="margin: 2rem auto; max-width: 350px; padding: 0 1rem; text-align:center;">
  <img src="[path/to/infographic.webp]"
       alt="[primary keyword + description]"
       width="1200" height="2133"
       loading="lazy"
       style="max-width:350px;width:100%;height:auto;border-radius:12px;
              box-shadow:0 4px 24px rgba(60,30,10,0.15);">
</div>
```

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

---

## Provider 5: Higgsfield MCP

**When to use:** Character-consistent lifestyle images (same bird across multiple shots), video generation (reels/shorts), marketing studio ads, or any multi-image campaign requiring visual continuity.

**MCP server ID:** `dd46f66a-ceb9-4042-b533-7b3fc3409318` (already installed — no API key file needed)

**Available models via Higgsfield:**
- `nano_banana_pro` — ultimate quality, text/diagrams, 9:16 support (2 credits)
- `nano_banana_2` — fast high-quality, 9:16 support (2 credits)
- `soul_2` — UGC/fashion/editorial character generation with reference image
- `cinematic_studio_2_5` — cinematic stills up to 4K
- `marketing_studio_image` — product/social campaign ads

**How to invoke:**
1. Load tool schema: `ToolSearch: select:mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__generate_image`
2. Check credits: `mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__balance`
3. Read `data/parrot-image-schema.json` for precise Congo/Timneh attributes + CITES safety
4. Build structured prompt using `prompt_safety` + `visual_style` fields from the schema
5. Call `mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__generate_image` with chosen model + prompt
6. Save output URL/data → hand off to `@cag-image-pipeline` for WebP optimization + placement

**Uploading user photos as reference:**
1. `ToolSearch: select:mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__media_upload,mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__media_confirm`
2. Upload photo → get media ID → pass as `medias: [{value: "<media_id>", role: "image"}]` in generate call
3. Use `soul_2` model for character-consistent generation with a reference photo

**CITES safety rule — applies to ALL Higgsfield prompts:**
Always include from `data/parrot-image-schema.json` `prompt_safety`:
- `always_include`: "captive-bred, domestic setting, hand-raised"
- `never_include`: "wild-caught", "tropical jungle", "imported", "exotic wildlife"

**Higgsfield vs Nano Banana (script):**
- Use Higgsfield MCP when: character consistency needed, video generation needed, user uploads a reference photo
- Use `generate_nb_image.sh` script when: one-off 9:16 portrait, no MCP available, or script workflow is preferred

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

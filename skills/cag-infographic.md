---
name: cag-infographic
description: Build 300–350px-tall HTML/CSS infographics for CongoAfricanGreys.com pages. Three types: Comparison, Feature Grid, Process Flow. Pure HTML — no images, no external libs. CAG brand colors. Use in Astro pages via component import or raw HTML paste in static HTML files.
---

# CAG Infographic Skill

## When to Use
- A page section needs a visual that reinforces key claims (scam detection, price comparison, process steps)
- The section has enough data for 2–4 rows / 6–12 grid items
- You want visual differentiation without adding an AI-generated image

## Mode Selection — HTML/CSS vs AI-Generated

| Mode | When to use | Provider |
|------|------------|---------|
| **HTML/CSS (Claude Code native)** | Default. Instant, brand-perfect, no API cost, fully editable. Use for 90% of cases. | Claude Code generates code directly — say "use Claude Code" or "use HTML" |
| **AI-Generated Image** | Photorealistic/artistic style needed, or design complexity beyond HTML. | `nanobanna` (Google Imagen) · `openai` (DALL-E 3) |

**How to request each mode:**
- "Build an infographic using Claude Code" → HTML/CSS (Types 1–3 below)
- "Build an AI infographic using Nano Banana" → Type 4 below
- "Build an AI infographic using OpenAI" → Type 4 with `openai` flag

## Height Determination Rules

The agent MUST pick a height in the 300–350px range before writing any HTML:

| Content density | Recommended height |
|----------------|-------------------|
| 2 feature rows per column | 300px |
| 3 feature rows per column | 320px |
| 4 feature rows per column | 340px |
| 4 rows + dense footer bar | 350px |
| Hero section (less room above fold) | 300px |
| Mid-page section (more room) | 320–340px |

**Never exceed 350px. Never go below 300px.**
Set height via: `style="height: 320px; min-height: 300px; max-height: 350px;"`

## Brand Colors

| Token | Hex | Use |
|-------|-----|-----|
| Green | `#2D6A4F` | Headers, right-column accents, footer CTA bar |
| Clay | `#e8604c` | Warning/alert labels, category labels |
| Cream | `#faf7f4` | Page background, process flow background |
| Red-light | `#fff5f5` | Scammer / negative column background |
| Green-light | `#f0faf4` | Legitimate / positive column background |
| Dark | `#1a1a2e` | Title bars, body copy headings |

## Placement Wrapper

Always wrap the infographic in this container regardless of type or page:

**In Astro pages (.astro files):**
```astro
{/* Infographic: [description] — height: [X]px */}
<div class="my-8 mx-auto max-w-4xl px-4">
  <ComparisonInfographic ... />
</div>
```

**In static HTML pages (.html files):**
```html
<!-- Infographic: [description] — height: [X]px -->
<div style="margin: 2rem auto; max-width: 900px; padding: 0 1rem;">
  <!-- paste full infographic HTML here -->
</div>
```

---

## Type 1: Comparison Infographic

**Use for:** Scam vs Legitimate, Male vs Female, Congo vs Timneh, Plan A vs Plan B

**Astro component path:** `src/components/infographics/ComparisonInfographic.astro`

**Raw HTML template (for static HTML pages):**

```html
<!-- CAG Infographic: Comparison | height: 340px -->
<div aria-label="[TITLE]" style="display:flex;flex-direction:column;height:340px;min-height:300px;max-height:350px;border-radius:12px;overflow:hidden;font-family:'Sora',sans-serif;box-shadow:0 4px 24px rgba(0,0,0,0.14);border:1px solid rgba(0,0,0,0.08);">

  <!-- Title bar -->
  <div style="background:#1a1a2e;color:#fff;padding:9px 16px;text-align:center;font-family:'Lora',serif;font-size:13px;font-weight:700;flex-shrink:0;line-height:1.3;">[TITLE]</div>

  <!-- Two columns -->
  <div style="display:grid;grid-template-columns:1fr 1fr;flex:1;overflow:hidden;min-height:0;">

    <!-- LEFT COLUMN (negative / red) -->
    <div style="background:#fff5f5;display:flex;flex-direction:column;border-right:2px solid #e5e7eb;">
      <div style="background:#fee2e2;color:#991b1b;padding:7px 10px;font-size:11px;font-weight:800;display:flex;align-items:center;gap:6px;flex-shrink:0;border-bottom:1px solid rgba(0,0,0,0.08);">
        <span style="font-size:14px;">🚩</span>
        <div>
          <div style="font-size:11px;font-weight:800;letter-spacing:0.03em;">[LEFT LABEL]</div>
          <div style="font-size:13px;font-weight:800;color:#dc2626;">[LEFT PRICE/SUBTITLE]</div>
        </div>
      </div>
      <!-- Repeat row block 2–4 times -->
      <div style="padding:5px 10px;border-bottom:1px solid rgba(0,0,0,0.06);display:flex;align-items:flex-start;gap:7px;flex:1;">
        <span style="font-size:16px;flex-shrink:0;width:20px;text-align:center;">[ICON]</span>
        <div>
          <div style="font-size:10px;font-weight:700;color:#1a1a2e;line-height:1.2;">[FEATURE TITLE]</div>
          <div style="font-size:9px;color:#555;line-height:1.3;margin-top:1px;">[FEATURE DESC]</div>
        </div>
      </div>
      <!-- end row -->
    </div>

    <!-- RIGHT COLUMN (positive / green) -->
    <div style="background:#f0faf4;display:flex;flex-direction:column;">
      <div style="background:#dcfce7;color:#166534;padding:7px 10px;font-size:11px;font-weight:800;display:flex;align-items:center;gap:6px;flex-shrink:0;border-bottom:1px solid rgba(0,0,0,0.08);">
        <span style="font-size:14px;">✅</span>
        <div>
          <div style="font-size:11px;font-weight:800;letter-spacing:0.03em;">[RIGHT LABEL]</div>
          <div style="font-size:13px;font-weight:800;color:#16a34a;">[RIGHT PRICE/SUBTITLE]</div>
        </div>
      </div>
      <!-- Repeat same number of rows as left column -->
      <div style="padding:5px 10px;border-bottom:1px solid rgba(0,0,0,0.06);display:flex;align-items:flex-start;gap:7px;flex:1;">
        <span style="font-size:16px;flex-shrink:0;width:20px;text-align:center;">[ICON]</span>
        <div>
          <div style="font-size:10px;font-weight:700;color:#1a1a2e;line-height:1.2;">[FEATURE TITLE]</div>
          <div style="font-size:9px;color:#555;line-height:1.3;margin-top:1px;">[FEATURE DESC]</div>
        </div>
      </div>
      <!-- end row -->
    </div>
  </div>

  <!-- Footer CTA bar -->
  <div style="background:#2D6A4F;color:#fff;padding:8px 16px;text-align:center;font-size:11px;font-weight:800;flex-shrink:0;display:flex;align-items:center;justify-content:center;gap:8px;">
    <span>[CTA TEXT]</span>
    <span style="opacity:0.75;font-weight:400;font-size:9px;">[CTA SUBTEXT]</span>
  </div>
</div>
```

---

## Type 2: Feature Grid Infographic

**Use for:** "N Red Flags", "N Benefits", "N Reasons", icon-heavy feature lists

**Astro component path:** `src/components/infographics/FeatureGridInfographic.astro`

**Raw HTML template:**

```html
<!-- CAG Infographic: Feature Grid | height: 320px -->
<div aria-label="[TITLE]" style="background:#2D6A4F;color:#fff;height:320px;min-height:300px;max-height:350px;border-radius:12px;overflow:hidden;font-family:'Sora',sans-serif;box-shadow:0 4px 24px rgba(0,0,0,0.2);display:flex;flex-direction:column;padding:12px 16px;">

  <!-- Header -->
  <div style="text-align:center;margin-bottom:10px;flex-shrink:0;">
    <div style="font-size:11px;font-weight:800;color:#e8604c;letter-spacing:0.08em;text-transform:uppercase;">[CATEGORY LABEL]</div>
    <div style="font-family:'Lora',serif;font-size:14px;font-weight:700;line-height:1.2;">[MAIN TITLE]</div>
  </div>

  <!-- Grid — use repeat(3,1fr) for 6–9 items; repeat(4,1fr) for 8–12 items -->
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px;flex:1;align-content:start;">

    <!-- Repeat this block per item -->
    <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:7px 8px;display:flex;flex-direction:column;gap:3px;">
      <div style="font-size:14px;">[ICON]</div>
      <div style="font-size:9px;font-weight:800;line-height:1.2;color:#fff;">[ITEM TITLE]</div>
      <div style="font-size:8px;color:rgba(255,255,255,0.65);line-height:1.3;">[ITEM DESC]</div>
    </div>
    <!-- end item -->

  </div>
</div>
```

---

## Type 3: Process Flow Infographic

**Use for:** "How to Buy", "Shipping Steps", "Documentation Process", sequential numbered steps

**Raw HTML template:**

```html
<!-- CAG Infographic: Process Flow | height: 310px -->
<div aria-label="[TITLE]" style="background:#faf7f4;height:310px;min-height:300px;max-height:350px;border-radius:12px;overflow:hidden;font-family:'Sora',sans-serif;box-shadow:0 4px 24px rgba(0,0,0,0.1);border:1px solid rgba(45,106,79,0.15);display:flex;flex-direction:column;">

  <!-- Header bar -->
  <div style="background:#2D6A4F;color:#fff;padding:10px 16px;text-align:center;font-family:'Lora',serif;font-size:13px;font-weight:700;flex-shrink:0;">[TITLE]</div>

  <!-- Steps row — 3 to 5 steps -->
  <div style="display:flex;flex-direction:row;align-items:stretch;flex:1;overflow:hidden;padding:12px 16px;gap:8px;">

    <!-- Repeat per step -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;position:relative;">
      <!-- connector line (omit on last step) -->
      <div style="position:absolute;top:18px;left:calc(50% + 18px);right:calc(-50% + 18px);height:2px;background:#2D6A4F;opacity:0.2;"></div>
      <div style="width:36px;height:36px;border-radius:50%;background:#2D6A4F;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:14px;flex-shrink:0;margin-bottom:6px;position:relative;z-index:1;">[N]</div>
      <div style="font-size:10px;font-weight:700;color:#1a1a2e;line-height:1.2;margin-bottom:3px;">[STEP TITLE]</div>
      <div style="font-size:9px;color:#555;line-height:1.3;">[STEP DESC]</div>
    </div>
    <!-- end step -->

  </div>
</div>
```

---

## Integration Checklist (run before every commit)

- [ ] Height set in 300–350px range: `style="height: Xpx; min-height: 300px; max-height: 350px;"`
- [ ] `overflow: hidden` on root element
- [ ] `flex-shrink: 0` on title and footer bars
- [ ] No `<script>` tags — pure HTML/CSS only
- [ ] All font sizes between 8px and 14px
- [ ] Row count matches on both columns (Comparison type)
- [ ] Zero placeholder text `[LIKE THIS]` remaining in output
- [ ] Wrapped in `max-w-4xl mx-auto px-4 my-8` container div

## File Placement Rules

| Page type | Component to use | How to insert |
|-----------|-----------------|---------------|
| Astro page (`.astro`) | `ComparisonInfographic.astro` or `FeatureGridInfographic.astro` | Import + JSX-style usage |
| Static HTML page (`.html`) | Raw HTML template from this skill | Paste inside placement wrapper `<div>` |

## Naming Convention for Raw HTML Infographics

When pasting raw HTML, always add a comment on the opening `<div>`:
```html
<!-- CAG Infographic: [Type] | [Page] | height: [X]px | Added: YYYY-MM-DD -->
```

---

## Type 4: AI-Generated Image Infographic (Nano Banana 2 / OpenAI)

**Use for:** Photorealistic or artistically complex infographic images where HTML/CSS cannot express the required design. Use HTML/CSS types 1–3 for 90% of cases.

**Output:** A 1200×2133px (9:16) WebP image, displayed at 300–350px via CSS. Generated at native high-res so text stays razor-sharp when CSS scales it to 300–350px. Never generate at 300px — text will be blurry.

### Pro-Grade Prompt Template

Fill in ALL-CAPS placeholders:

```
Role: Professional marketing designer for pet services specializing in responsive UI/UX assets.
Scene: SCENE_DESCRIPTION
Style: CAG brand aesthetic (Forest Green #2D6A4F, Clay #e8604c, Cream #faf7f4).
       Lora serif for headers, Sora sans for body text.
Technical:
  - Aspect Ratio: 9:16 (Vertical) for mobile/tablet optimization.
  - Dimensions: 1200×2133px render for perfect downscaling to 300–350px desktop width.
  - Camera: Professional studio macro-lens clarity, flat-lay design composition,
            ISO 100, f/8, sharp focus on all text elements.
  - Responsive Ready: Minimalist, uncluttered layout with balanced white space to ensure
                      legibility when downscaled to 300px.
Text Constraints: Render title "TITLE_TEXT" in Lora serif at top.
                  Use ALL CAPS for section headers. High contrast on all text.
Content:
  - CONTENT_ITEM_1
  - CONTENT_ITEM_2
  - CONTENT_ITEM_3
Quality Levers: Photorealistic, professional graphic design, crisp vector-style iconography,
                ultra-sharp text rendering, 8K resolution, high fidelity, no blurry text.
CITES Safety: No wire cages, no aviary settings. Birds in loving home environments only.
```

### Generation Commands

```bash
# Nano Banana 2 (Google Imagen) — primary choice
./scripts/generate_nb_image.sh "FULL_PROMPT_HERE" "cag-infographic-[slug]-nb.png" "1200x2133"

# OpenAI DALL-E 3 (portrait mode)
./scripts/generate_image.sh "FULL_PROMPT_HERE" "cag-infographic-[slug]-openai.png" "1024x1792" "openai"
```

### HTML Placement Wrapper

```html
<!-- AI Infographic: [slug] | Provider: [nanobanna/openai] | Generated: YYYY-MM-DD -->
<div style="margin: 2rem auto; max-width: 350px; padding: 0 1rem; text-align:center;">
  <img src="[wp-content/uploads/filename.webp]"
       alt="[Primary keyword + descriptive text]"
       width="1200"
       height="2133"
       loading="lazy"
       style="max-width:350px;width:100%;height:auto;border-radius:12px;
              box-shadow:0 4px 24px rgba(60,30,10,0.15);">
</div>
```

### Integration Checklist (AI infographic)

- [ ] Generated at 1200×2133px (9:16) — never at final display size
- [ ] WebP conversion completed (`.webp` not `.png` in production)
- [ ] `width="1200" height="2133"` attributes on `<img>` (prevents layout shift)
- [ ] `loading="lazy"` unless this is the first above-fold image
- [ ] `max-width: 350px; width: 100%; height: auto;` CSS applied
- [ ] Alt text includes primary keyword
- [ ] Handed off to `cag-image-pipeline` for SEO filename rename

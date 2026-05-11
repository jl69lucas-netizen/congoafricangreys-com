---
name: cag-logo-generator
description: Generates logo design specifications and AI image prompts for CongoAfricanGreys.com. Produces a circular emblem-style logo spec (200×200px, transparent background, deep teal/forest green color scheme) with an African Grey parrot head centerpiece, curved top/bottom arc text, and responsive sizing guidance. Output is a ready-to-use DALL-E/Midjourney prompt plus an SVG-equivalent HTML spec. Use when the breeder needs a logo for the site header, social media, or printed materials.
---

# CAG Logo Generator

**Announce at start:** "Using cag-logo-generator skill to create the CongoAfricanGreys.com logo specification."

---

## Logo Design Specification

### Format
- **Shape:** Circular emblem (badge/seal style)
- **Canvas size:** 200 × 200 px (scalable — output at 400×400 for retina)
- **Background:** Transparent (PNG with alpha channel)
- **Primary text color:** `#1a6b3c` (deep forest green — African Grey/nature palette)
- **Secondary accent:** `#2e8b57` (sea green) or `#c4a35a` (warm gold) for border ring or decorative element
- **Alternative palette:** Deep teal `#1a5276` if green feels too generic — test both

### Centerpiece Illustration
A detailed, recognizable illustration of an **African Grey parrot head** — the CAG signature bird:
- Distinctive grey plumage with subtle lighter edging on feathers
- Bright, intelligent red tail feathers visible at bottom crop
- Sharp yellow eye with an alert, intelligent expression
- Strong curved beak (black)
- Rendered in a clean, slightly illustrative (not photographic) style — vector-friendly
- Color palette: slate grey, charcoal, red accent — warm but dignified

### Typography
- **Font family:** Montserrat Bold, Lato Bold, or Poppins Bold (in that preference order)
- **Top arc text (curved along top of circle):** `CongoAfricanGreys.com`
  - Font size: ~13px equivalent at 200px canvas
  - Letter spacing: slightly expanded for arc legibility
- **Bottom arc text (curved along bottom of circle):** `Captive-Bred African Grey Breeders`
  - Font size: ~10px equivalent at 200px canvas
  - Slightly smaller than top text

### Decorative Elements
- Thin double-ring border in primary color (`#1a6b3c` or `#1a5276`)
- Optional: small feather motifs at 9 o'clock and 3 o'clock positions on the ring
- Safe inner margin: 10px from ring to illustration

---

## AI Image Generation Prompt

Use this prompt with DALL-E 3, Midjourney, or Stable Diffusion:

```
Circular emblem-style logo, 200x200 pixels, transparent background.
Center: detailed illustration of an African Grey parrot head (slate grey 
plumage with subtle lighter feather edging, red tail accent, sharp curved 
black beak, bright yellow intelligent eye), rendered in a clean, slightly 
stylized (non-photographic) illustration style — vector-friendly.
Surrounding the illustration: thin double-ring border in deep forest green 
(#1a6b3c) or deep teal (#1a5276).
Top arc text (curved): "CongoAfricanGreys.com" in bold Montserrat or Lato 
font, color matching border, slightly expanded letter spacing.
Bottom arc text (curved): "Captive-Bred African Grey Breeders" in same font,
slightly smaller size, same color.
Optional small feather accent motifs at 9 and 3 o'clock on the ring.
Style: professional, clean, dignified breeder brand mark.
Color palette: slate grey / charcoal parrot illustration; deep forest green 
or teal text and border; transparent background. No background fill. PNG output.
```

---

## Responsive Sizing Guide

| Use Case | Size | Notes |
|----------|------|-------|
| Site header (desktop) | 120×120 px | Standard `<img>` in nav |
| Site header (mobile) | 60×60 px | Shrinks via CSS media query |
| Social media profile | 400×400 px | Instagram, Facebook page icon |
| Favicon | 32×32 px | Needs separate simplified version |
| Email signature | 80×80 px | PNG with transparent bg |

---

## HTML Implementation (Site Header)

After generating the logo PNG, add it to the site header:

```html
<a href="/" class="cag-logo-link" aria-label="CongoAfricanGreys.com home">
  <img
    src="/wp-content/uploads/cag-logo-african-grey-emblem.png"
    srcset="/wp-content/uploads/cag-logo-african-grey-emblem@2x.png 2x"
    alt="CongoAfricanGreys.com logo — Captive-Bred African Grey Breeders"
    width="120"
    height="120"
    loading="eager"
    class="cag-logo"
  />
</a>
```

CSS for responsive sizing:

```css
.cag-logo {
  width: 120px;
  height: 120px;
}
@media (max-width: 768px) {
  .cag-logo {
    width: 60px;
    height: 60px;
  }
}
```

---

## File Naming Convention (CAG Standard)

After generating the logo image:

```
cag-logo-african-grey-emblem-200x200.png       ← standard size
cag-logo-african-grey-emblem-400x400.png       ← 2x retina
cag-logo-african-grey-emblem-400x400.webp      ← WebP version
```

Place in: `site/wp-content/uploads/logos/`

Run image-metadata skill to write alt text and title attributes.
Run cag-image-generation skill's optimize step to produce WebP version.

---

## Rules

1. Never use Maltipoo, dog, puppy, or any canine imagery or text — this is an African Grey parrot brand
2. Never use a photographed bird — illustration/vector style only (small file size, style consistency)
3. Always output PNG with transparent background (never white background)
4. Always produce both standard (200×200) and retina (400×400) versions
5. Always hand off to cag-image-pipeline agent after logo files are placed
6. The logo belongs to the CAG breeder — do not use for any other project
7. Never include CITES documentation numbers or claims in logo text — brand mark only

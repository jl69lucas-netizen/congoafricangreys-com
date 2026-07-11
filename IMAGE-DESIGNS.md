# Image Designs

> **READ FIRST — companion to `DESIGN.md`.** `DESIGN.md` governs *the page* (UI, palette,
> type, components, layout). **This file governs *the picture*** — how every AI-generated,
> AI-edited, or sourced image must look, crop, and be lit before it lands on the site.
> Read this BEFORE generating, editing, or placing any image.
>
> **This file wins.** If any image skill or agent still carries an older brand value
> (e.g. a stale orange hex, a wrong owner name, a wrong location), **the values here are
> canonical — fix the consumer to match this file**, never the reverse.

---

## 0. Brand Facts (canonical)

- **Owners / aviary:** Mark & Teri Benjamin — breeding African Greys in **Midland, TX since 2014**.
  Real family aviary, not a storefront. (Brand voice in copy is first-person plural: "we / us / our /
  here at C.A.Gs" — but images carry *mood*, not text.)
- **In-image palette** (must echo the site, never fight it):
  - **Forest Green `#2D6A4F`** — framing, foliage, calm background depth.
  - **Clay / terracotta `#e8604c`** — warm accent (a perch, a blanket, a wall tone, a prop) used
    sparingly, never as the dominant cast.
  - **Cream `#faf7f4` / warm wood / soft beige** — surfaces, walls, perches, table tops.
  - **Warm color grade** overall — slightly warm white balance. **Never** cold blue, clinical, or grey-cast.
- **Species accuracy (non-negotiable — get the bird right):**
  - **Congo African Grey:** light **grey body**, **bright RED tail**, **white face mask** around the eye,
    ~**13 inches**, **400–650 g**, **yellow iris in adults** (dark iris in juveniles), **dark hooked beak**.
  - **Timneh African Grey:** **darker charcoal grey** body, **maroon / dark tail**, **horn-colored
    (pinkish-tan) upper mandible**, smaller than the Congo.
  - **NEVER** a generic green parrot. **NEVER** the 🦜 emoji or any cartoon parrot stand-in.
- **CITES safety (binding):** African Greys are **CITES Appendix I**, and all C.A.Gs birds are
  **captive-bred in the USA with full documentation**. Images must **never** imply wild-caught, jungle
  capture, smuggling, cages-in-the-wild, or any wild-trade context. Settings are home / family-aviary,
  calm and domestic.

---

## 1. Crop & Aspect Ratios (per slot)

| Slot | Ratio | Pixels | Notes |
|---|---|---|---|
| Hero | 16:9 | 1600×900 | LCP image — set `fetchpriority="high"`, serve **WebP** |
| Bird card | 3:4 portrait | 900×1200 | set `object-position` per bird (e.g. some birds crop `object-top`) |
| Lifestyle / in-content | 4:3 | 1200×900 | candid family / room scenes |
| Social / OG | 1:1 | 1200×1200 | Open Graph + square feed posts |
| Social vertical | 9:16 | 1080×1920 | Reels / TikTok / Shorts |
| Infographic | per page-width rules | **760px** (guide/blog) · **1100px** (home/location) wide | height **400px** desktop, auto on mobile |

---

## 2. Reusable Style Wrapper

Prepend this single string to every photoreal image prompt:

> Editorial pet photography, warm natural light, shallow depth of field, true-to-life African Grey
> plumage, cream/wood/forest-green palette, calm premium family-aviary mood, photorealistic, high
> detail on eye and feather texture.

---

## 3. Negative List (append to every prompt — non-negotiable)

> no text, no watermarks, no logos, no captions, no UI chrome, no other parrot species, no generic
> green parrot, no cartoon / 3D / illustration (for photoreal slots), no cold blue / clinical / studio
> lighting, no distorted or extra limbs or beaks, no unrealistic coloring, no dog / cat / puppy imagery,
> no jungle or wild-capture context, no sharp identifiable human faces unless a real buyer photo, no
> cluttered background.

---

## 4. Lighting & Focal Length (per scene)

| Scene | Lighting | Focal length / aperture |
|---|---|---|
| Hero portrait | soft window light / golden-hour warm | 85mm f/1.8 |
| Lifestyle (with family) | ambient room, candid | 35–50mm f/2.8 |
| Size reference (on hand) | even, bright, full feather detail | 50mm f/4 |
| Health / feather macro | diffused, no flash | 100mm macro f/5.6 |
| Infographic | flat design | N/A |

---

## 5. Scene Types by Page Type (routing table)

| Page type | Primary scene | Secondary / alt | Avoid |
|---|---|---|---|
| Blog post | topic-illustrative lifestyle or portrait | infographic if data-heavy | for-sale price overlays |
| For-sale / variant | single-bird portrait, direct gaze | size-reference on hand | busy lifestyle scenes |
| Location (state/city) | bird + subtle state landmark context (not kitschy) | calm shipping-airport scene | literal flags / maps in-frame |
| Comparison ([X] vs [Y]) | split / side-by-side, both subjects | comparison infographic | showing only one subject |
| Care / health guide | feather / eye macro + vet context | process (foraging / enrichment) | sales mood |
| Hub | clean banner-style portrait | grid of cluster thumbnails | text baked into the image |

---

## 6. Output Handoff

Every generated image flows through the same pipeline:

1. **`cag-image-pipeline`** — SEO filename rename + WebP conversion + correct on-page placement.
2. **image-metadata** — the **5-element set**: filename, **alt ≤190 chars**, title, caption + CTA,
   and a **250+ word description**.
3. **Keyword distribution (seo-rules Rule 50b, 2026-07-11):** the page's PRIMARY keyword goes in
   the PRIMARY image's alt only; every other image rotates a different keyword type (secondary /
   LSI / NLP variation / long-tail). No two images on a page share an alt. No stop-word filler in
   filenames or alts.

---

*Consumed by:* `skills/image-prompt-generator.md`, `skills/cag-image-generation.md`,
`skills/cag-photo-ingest.md`, `skills/cag-infographic.md`, `.claude/agents/cag-image-pipeline.md`,
`.claude/agents/cag-infographic-builder.md`. **On conflict, THIS file wins — fix the consumer.**

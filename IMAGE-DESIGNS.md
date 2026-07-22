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

### 1a. Uniform In-Body Image Sizing (ALWAYS — locked by breeder 2026-07-12)

**On comparison and long-form content pages, EVERY in-body section image — OG photo AND infographic — renders in the SAME box as an infographic:** `.sec-img.inf-img` = `max-width:760px; aspect-ratio:1408/768 (16:9); object-fit:cover; height:auto`, **identical on mobile / tablet / desktop**. Do NOT give OG photos the smaller/variable boxes (`.portrait` 420px 1:1, `.portrait-tall` 340px 3:4, `.photo43` 480px 4:3) on these pages — match the infographic size so every image is one uniform rectangle down the page. Tune **`object-position` per OG photo** (e.g. `center 30%` for a portrait bird) so the subject isn't cropped out of the 16:9 strip; the box size never changes, only the focal point. Ship each file **<100 KB WebP + a `-760.webp` sibling** with `srcset`/`sizes` exactly as the infographics do. Reference implementations: `/congo-vs-timneh-african-grey/`, `/african-grey-vs-macaw/`, `/african-grey-vs-cockatoo/`, `/male-vs-female-african-grey-parrots-for-sale/`. (The hero's staggered-portrait component keeps its own `.hero-imgs` sizing — this rule governs in-body `.sec-img` slots only.)

**Processing recipe (the exact pipeline — apply to BOTH infographics and OG photos so they are literally the same pixel box, 2026-07-12 breeder confirmation):** cover-crop every source to **1408×768** with `PIL.ImageOps.fit(im, (1408,768), Image.LANCZOS, centering=(x,y))` — set `centering` per OG so the bird's head survives the 16:9 crop (portrait birds ≈ `(0.5, 0.35)`); export **WebP `method=6`, walk quality 82→down until <95 KB**; then a **`-760.webp`** sibling via the same `fit` at 760×415 (<55 KB). On-page: `width="1408" height="768" class="sec-img inf-img" loading="lazy"` + `srcset="/name-760.webp 760w, /name.webp 1408w" sizes="(max-width:900px) 92vw, 760px"`. A low-res OG master (≤800–1040 px) is upscaled to the box on purpose — **uniform sizing wins over pixel-peeping sharpness** (the breeder's explicit call); pick the highest-res available master and tune the focal point. This recipe binds every image agent/skill: `@cag-image-pipeline`, `@cag-infographic-builder`, `skills/cag-infographic`, `skills/cag-image-generation`, `skills/cag-comparison-page-builder`. Companion differentiation skill: `skills/cag-component-refresh`.

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

## 7. Named OG Framing Styles (LOCKED 2026-07-22 — breeder-approved)

**The head-cutoff rule (binding):** NEVER cover-crop a portrait/near-square bird master into a wide
box with a focal point (`ImageOps.fit(..., centering=...)`). On tall masters (e.g. 591×640, 768×1376)
that slices the head off — this is exactly what happened to the Timneh for-sale OG photos. Instead,
pick a **named style** below and bake it into the file with `scripts/reframe_og.py`. Say *"use Style B
on this image"* and the recipe is unambiguous.

Engine: **`scripts/reframe_og.py <src-master> <out.webp> --style <s> [--sib <out-760.webp>]`**
(outputs a 16:9 1408×768 file that keeps the FULL subject, plus an optional `-760` sibling <55 KB).
Every style centers the subject **full-height**, so any later mobile COVER crop (5:4 / 4:5 / 1:1)
keeps the whole bird — only padded/blurred sides crop away. No per-image markup change needed:
just replace the file.

| Style | Name | `--style` | When to use | Full bird? |
|---|---|---|---|---|
| **A** | Contain · Warm Canvas | `contain` | infographic-like / wide shots, or when blur reads busy | ✅ full |
| **B** | Blur-Fill 16:9 *(default single bird)* | `blurfill` | any single-bird portrait OG photo — premium, no bars | ✅ full |
| **C** | Editorial Split | (CSS component) | "meet the bird" hero-adjacent moments (photo + green caption panel) | ✅ full |
| **D** | Portrait Frame | (CSS component) | boutique matted 3:4 inside the 16:9 | ✅ full |
| **E** | Top-Anchored Cover | `topcover` | when you want a photo to FILL punchy; head never cut, feet may crop | ⚠ head-safe |
| **H** | Duo Strip | (CSS: 2× `.h-im`) | Elad + Evie sibling / pair shots, two portraits side-by-side | ✅ full |

**Mobile counterparts** (full-bleed, taller aspect): **mA** 4:5 top-cover · **mB** 4:5 contain ·
**mC** 4:5 blur-fill *(matches B)* · **mG** stacked two-up · **mH** 3:4 top-cover. A blur-fill (B)
file already prevents head cutoffs on mobile under the current 5:4 crop; for a *distinct taller*
mobile frame, set the page's mobile `.og-photo{aspect-ratio:4/5}` **only once every OG photo on that
page is a blur-fill/contain file** (otherwise the portrait crop re-cuts un-reframed photos).

**Defaults:** single-bird OG photo → **B**; wide/infographic-like → **A**; pair/sibling → **H** (or B
if it's one photo of both birds); punchy fill → **E**. Applied to the Timneh page 2026-07-22:
on-hand-playful + siblings reframed via **B** from their masters in
`assets/1WORKING-ON/FOR-SALE-PAGES/TIMNEHS-FOR-SALE/`. (Any OG photo whose only file is already a
cover-cropped 16:9 with the head gone CANNOT be recovered by reframing — it needs the original
master or a photo swap.)

*Consumed by:* `skills/image-prompt-generator.md`, `skills/cag-image-generation.md`,
`skills/cag-photo-ingest.md`, `skills/cag-infographic.md`, `.claude/agents/cag-image-pipeline.md`,
`.claude/agents/cag-infographic-builder.md`. **On conflict, THIS file wins — fix the consumer.**

# CAG Design System — Terracotta Warmth
**Version 2 — 2026-05-19. Supersedes all prior design.md versions.**
Source of truth for all visual, content, and motion decisions on CongoAfricanGreys.com.

Related files:
- `docs/design-system/README.md` — full narrative spec with brand identity + voice
- `docs/design-system/colors_and_type.css` — canonical CSS custom properties
- `src/styles/cag-design-system.css` — project-installed CSS tokens (import in non-Tailwind pages)
- `src/styles/global.css` — Tailwind 4 @theme version for Astro pages
- `docs/reference/components.md` — full component registry with variants
- `docs/reference/page-width.md` — container system, breakpoints, typography scale

---

## Brand Identity

**Site:** CongoAfricanGreys.com — family-owned, captive-bred African Grey parrot breeder,
Midland TX, est. 2014. Owners: Mark & Teri Benjamin. USDA AWA-licensed, CITES Appendix II.

**Tone:** Warm, trustworthy, premium — like a high-end pet boutique, not a generic directory.
**Audience:** Parrot buyers (first-timers and experienced) making a 30+ year commitment.
**Positioning:** Small family aviary. Documentation and provenance are the product.

---

## Content Voice Rules

**Person:** First-person plural ("we", "our birds") as the breeder; second-person ("you", "your
new companion") to the buyer. Never corporate "the company".

**Casing:**
- Headlines (Lora): sentence case or Title Case — NEVER ALL CAPS in body headings.
- Uppercase reserved for: short tags ("USDA LICENSED"), section eyebrows ("OUR FAMILY"),
  dark-banner CTA headline, and form labels — always with `letter-spacing: 1px` (tags) or
  `2px` (banner).
- Buttons: Title Case ("Reserve Your African Grey", "Send Inquiry").

**Words we use:** "captive-bred", "hand-fed", "weaned", "hen / cock", "clutch", "aviary",
"companion bird", "CITES Appendix II", "DNA-sexed", "avian vet certified", "health guarantee",
"lifetime support".

**Words we avoid:** "stock", "inventory", "product", "purchase", "shop now", "limited time",
"deal", "exotic" (loaded), "tame" (use "hand-fed and socialized").

**Emoji — functional icons only, sparingly:**

| Emoji | Meaning | Where |
|---|---|---|
| 🦜 | Brand mark / parrot | Logo fallback, footer, hero accent |
| 📞 | Phone | Contact rows, CTA |
| ✉️ | Email | Contact rows, form labels |
| 📍 | Location | Address |
| 🕐 | Hours | Business hours |
| ✈️ | Air shipping | Shipping section |
| 🚗 | Local delivery | Shipping section |
| ✅ | Confirmation | Success states |
| ❋ | Section divider | Decorative break |

Rules: one per element max. Always paired with text. Never wrap in a colored circle chip.
No 🎉 🔥 🚀 "marketing" emoji.

**Trust signals — at least two on every transactional page:**
- "USDA-Licensed Breeder"
- "CITES Appendix II Documented"
- "DNA-Sexed & Vet-Certified"
- "Ships Nationwide from $185"
- "24–48 Hour Response Guarantee"
- "Health Guarantee on Every Bird"

---

## Typography

| Role | Font | Weight | Size |
|---|---|---|---|
| Page H1 / hero | Lora (serif, italic available) | 700 | clamp(1.75rem, 2.5vw+1rem, 2.6rem) |
| Hero display | Lora | 700 | clamp(2rem, 4vw+1rem, 3.2rem) |
| Section H2 | Lora | 700 | clamp(1.5rem, 1.5vw+1rem, 2rem) |
| Card / form H3 | Lora | 700 | 1.5rem |
| Body copy | Sora | 400 | 1rem / 16px, line-height 1.55 |
| Labels, nav links | Sora | 500–700 | 13–14px |
| Uppercase tags | Sora | 700 | 11px, letter-spacing 1px |
| Meta / caption | Sora | 400 | 12px |

**Responsive Typography Scale (Option A):**

| Element | Mobile ≤480px | Tablet 481–1024px | Desktop ≥1025px | Notes |
|---|---|---|---|---|
| H1 | 28–32px | 36–40px | 44–48px | line-height 1.2, bold |
| H2 | 22–24px | 26–28px | 32–34px | major sub-sections |
| H3 | 18–20px | 22–24px | 24–26px | card headings |
| H4 | 16px | 18px | 20px | sidebar / feature titles |
| H5/H6 | 14px ALL-CAPS | 14px ALL-CAPS | 16px ALL-CAPS | utility text, labels |
| Lead / subheader | 16–17px | 18–19px | 20–21px | first paragraph of page |
| Body | 15–16px | 16–17px | 17–18px | line-height 1.6–1.7 |
| Caption | 12px | 13px | 14px | image captions, sources |

Font weights: H1–H3 = 700 (bold) or 600 (semi-bold). Body = 400 (regular).
Paragraph max-width: `max-width: 70ch` — applies inside any container to prevent long lines.

**Google Fonts import (every page `<head>`):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
```

---

## Color Palette

### ✅ Active Production Colors (do not change)

| Role | Color | Hex | CSS var |
|---|---|---|---|
| Brand Green — nav/headers, trust framing | Forest green | `#2D6A4F` | `--green` |
| Clay / CTA — all buttons, active accents, gold text | Terracotta | `#e8604c` | `--clay` |
| Cream — page background | Off-white | `#faf7f4` | `--cream` |

> **Rule:** `--gold` MUST always equal `#e8604c` (same as `--clay`). Every `text-gold` renders orange, not yellow.

```css
:root {
  --clay:       #e8604c;   /* Primary CTA / buttons / active accents */
  --clay-lt:    #f08070;   /* Gradient light / hover */
  --clay-dk:    #c94d3a;   /* Pressed / deep hover */
  --green:      #2D6A4F;   /* Brand green — header bg, info headers, labels */
  --green-lt:   #eaf4ef;   /* Light green — success bg, tag bg */
  --gold:       #e8604c;   /* ⚠️ Must equal clay — all gold text is orange */

  /* Surfaces */
  --cream:      #faf7f4;   /* Page background */
  --warm-white: #fff9f6;   /* Form inputs, inner card bg */
  --card-bg:    #ffffff;   /* Card surfaces */
  --border:     #ede5dc;   /* All borders and dividers */

  /* Text */
  --text:       #1c1a18;   /* Primary — near-black warm */
  --mid:        #5a5248;   /* Secondary — body paragraphs */
  --light:      #9b9189;   /* Tertiary — placeholder, captions */

  /* Dark panels */
  --dark-panel: #1c1a18;   /* CTA banners, dark footer */
  --forest:     #2D6A4F;   /* Info card headers, dark nav variant */
}
```

---

## Page Layout & Container System (Option A — Classic 1200px)

### Container Strategy (dual-purpose)

| Page Type | Max Width | Use |
|---|---|---|
| Visual / transactional | **1200px** | Homepage, Available Birds, Location pages, gallery grids |
| Informational / long-form | **760px** (centered within 1200px) | Scam Guide, Care Guides, Species Guides, Blog posts |

**The rule:** Every page has a 1200px outer shell. Informational pages add a `max-width: 760px; margin: 0 auto` wrapper around all text content.

### Breakpoints

| Breakpoint | Rule | Side padding |
|---|---|---|
| Desktop ≥1025px | Container: max-width 1200px, `margin: 0 auto` | 48px |
| Tablet 768–1024px | Container fluid: 90%–94% of screen width | 32px |
| Mobile ≤767px | Container fluid: 92% of screen width | 15–20px |

### CSS Classes
```css
.container      { max-width: 1200px; margin: 0 auto; padding: 0 48px; }
.container-text { max-width: 760px; margin: 0 auto; }
p               { max-width: 70ch; }

@media (max-width: 1024px) { .container { width: 92%; padding: 0 32px; } }
@media (max-width: 767px)  { .container { width: 92%; padding: 0 16px; }
                              .container-text { padding: 0; } }
```

### Section Padding
- Desktop: 64px top/bottom, 48px sides
- Mobile: 40px top/bottom, 24px sides

### Column Rules
- Two-column grids: collapse at 1024px
- Single-column: 768px and below

---

## Spacing Scale

| Token | Value | Use |
|---|---|---|
| `--sp-xs` | 4px | icon gaps, tight inline |
| `--sp-sm` | 8px | pill padding, small gaps |
| `--sp-md` | 16px | field margin-bottom, grid gap |
| `--sp-lg` | 24px | card inner padding |
| `--sp-xl` | 40px | section padding sides |
| `--sp-2xl` | 64px | section top/bottom |
| `--sp-3xl` | 96px | hero section |

---

## Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `--r-sm` | 8px | small badges |
| `--r-md` | 10px | form inputs |
| `--r-lg` | 14px | map boxes, icon wrappers |
| `--r-xl` | 20px | cards, info panels |
| `--r-pill` | 50px | CTA buttons, trust pills, tags — **brand signature** |

---

## Shadows

```css
--shadow:     0 2px 16px rgba(60,30,10,.08), 0 8px 40px rgba(60,30,10,.06);
--shadow-lg:  0 4px 24px rgba(60,30,10,.1),  0 16px 56px rgba(60,30,10,.08);
--shadow-btn: 0 6px 20px rgba(232,96,76,.38);
--shadow-btn-hover: 0 10px 28px rgba(232,96,76,.48);
```
Always warm-tinted. Never neutral grey. No inner shadows. No neon.

---

## Buttons

### Primary (Clay Pill) — brand signature
```css
background: #e8604c; color: #fff; border: none;
padding: 14px 32px; border-radius: 50px;
font: 700 15px/1 'Sora', sans-serif; letter-spacing: .2px;
box-shadow: 0 6px 20px rgba(232,96,76,.38);
transition: background .2s, transform .15s, box-shadow .2s;
```
Hover: `background: #c94d3a; transform: translateY(-2px); box-shadow: 0 10px 28px rgba(232,96,76,.48);`

### Primary Square (forms only)
Same as above but `border-radius: 12px`.

### Outline
```css
background: transparent; color: #e8604c;
border: 2px solid #e8604c; padding: 12px 28px; border-radius: 50px;
font: 700 14px/1 'Sora', sans-serif;
```
Hover: fill clay, `color: #fff`.

### Green Tag / Badge
```css
background: #eaf4ef; color: #2D6A4F;
border: 1px solid rgba(45,106,79,.2); padding: 5px 14px; border-radius: 50px;
font: 700 11px/1 'Sora', sans-serif; letter-spacing: 1px; text-transform: uppercase;
```

---

## Form Inputs

```css
padding: 12px 16px; border: 1.5px solid #ede5dc; border-radius: 10px;
font: 400 14.5px/1.4 'Sora', sans-serif; background: #fff9f6; color: #1c1a18;
transition: border-color .2s, box-shadow .2s, background .2s; outline: none;
/* Focus */
border-color: #e8604c; box-shadow: 0 0 0 3px rgba(232,96,76,.1); background: #fff;
/* Labels */
font: 700 12px/1 'Sora', sans-serif; text-transform: uppercase;
letter-spacing: .7px; color: #1c1a18; margin-bottom: 7px;
```

### Pill Selectors (radio/checkbox groups)
```css
background: #fff9f6; border: 1.5px solid #ede5dc; border-radius: 10px;
padding: 9px 16px; font: 400 13.5px/1 'Sora', sans-serif; color: #5a5248;
/* Checked */
background: #fff3ef; border-color: #e8604c; color: #c94d3a; font-weight: 600;
```

---

## Motion Rules

- Color/bg transitions: `0.2s`
- Transform lift on hover (`translateY(-2px)`): `0.15s`
- Easing: `cubic-bezier(.4,0,.2,1)`
- No spring physics, no bounce, no parallax, no auto-playing video
- Page-load fade-up on cards: 8–12px, 250ms — acceptable

---

## Cards

```css
background: #ffffff; border-radius: 20px; border: 1px solid #ede5dc;
box-shadow: 0 2px 16px rgba(60,30,10,.08), 0 8px 40px rgba(60,30,10,.06);
overflow: hidden;
/* Hover */
box-shadow: 0 4px 24px rgba(60,30,10,.1), 0 16px 56px rgba(60,30,10,.08);
transform: translateY(-2px);
```

Info card (green header variant):
```css
.card-header { background: #2D6A4F; padding: 32px 28px; color: #fff; }
```

---

## Section Patterns

### Warm Gradient Hero
```css
background: linear-gradient(135deg, #fde8e3 0%, #fdf0e8 50%, #fdf6ec 100%);
padding: 64px 48px 72px; text-align: center;
border-bottom: 1px solid #f0e4da;
```

### Dark CTA Banner (bottom-of-page)
```css
background: #1c1a18; padding: 72px 48px; text-align: center;
/* H2: */ font-family: Lora; font-size: 2.8rem; color: #e8604c;
text-transform: uppercase; letter-spacing: 2px;
```

---

## Anti-Copy: DISABLED
All `user-select: none` CSS and JS have been permanently removed. Never add them back.

---

## Formspree Endpoints

| Page | Endpoint |
|---|---|
| /contact-us/ | `https://formspree.io/f/xrejpnvn` |
| All product pages | `https://formspree.io/f/xpqoeazq` |
| Newsletter | `https://formspree.io/f/xpqoeazq` |

---

## File Locations

| Asset | Path |
|---|---|
| Logo image | `/wp-content/uploads/african-grey-parrot-store-logo.png` |
| Design system folder | `docs/design-system/` |
| CSS tokens (non-Tailwind) | `src/styles/cag-design-system.css` |
| CSS tokens (Tailwind/Astro) | `src/styles/global.css` |
| Component registry | `docs/reference/components.md` |
| Page width rules | `docs/reference/page-width.md` |

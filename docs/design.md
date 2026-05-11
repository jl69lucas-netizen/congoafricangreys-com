# CAG Design System

Derived from the contact-us page rebuild (Design B — "Terracotta Warmth").
Apply this system to every page, component, navbar, and footer rebuild.

---

## Brand Identity

**Site:** CongoAfricanGreys.com  
**Tone:** Warm, trustworthy, premium — like a high-end pet boutique, not a generic directory.  
**Target:** Parrot buyers (first-timers and experienced) seeking CITES-documented, captive-bred birds.

---

## Typography

| Role | Font | Weight | Size |
|---|---|---|---|
| Page H1, card H2 | Lora (serif, italic available) | 700 | 2–3.2rem |
| Section H2 | Lora | 700 | 1.5–2rem |
| Card/form H2 | Lora | 700 | 1.5rem |
| Body copy | Sora | 400 | 1rem / 16px |
| Labels, nav links | Sora | 500–700 | 13–14px |
| Uppercase tags | Sora | 700 | 11–12px, letter-spacing 1px |
| Meta/caption | Sora | 400 | 12–13px |

**Google Fonts import (add to every page `<head>`):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
```

---

## Color Palette

```css
:root {
  /* Brand */
  --clay:       #e8604c;   /* Primary CTA / buttons / active accents */
  --clay-lt:    #f08070;   /* Gradient light / hover */
  --clay-dk:    #c94d3a;   /* Pressed / deep hover */
  --green:      #2D6A4F;   /* Brand green — info headers, labels, icons */
  --green-lt:   #eaf4ef;   /* Light green — success bg, tag bg */
  --gold:       #F4A261;   /* Warm accent — trust pills, secondary CTA */

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

## Spacing Scale

| Token | Value | Use |
|---|---|---|
| xs | 4px | icon gaps, tight inline |
| sm | 8px | pill padding, small gaps |
| md | 16px | field margin-bottom, grid gap |
| lg | 24px | card inner padding top/bottom |
| xl | 40px | section padding sides |
| 2xl | 64px | section top/bottom padding |
| 3xl | 96px | hero section padding |

---

## Border Radius Scale

| Token | Value | Use |
|---|---|---|
| sm | 8px | small badges, social buttons |
| md | 10px | form inputs, small cards |
| lg | 14px | map info boxes, icon wrappers |
| xl | 20px | cards, info panel |
| pill | 50px | CTA buttons, trust pills, tags |

---

## Shadows

```css
--shadow:    0 2px 16px rgba(60,30,10,.08), 0 8px 40px rgba(60,30,10,.06);
--shadow-lg: 0 4px 24px rgba(60,30,10,.1), 0 16px 56px rgba(60,30,10,.08);
--shadow-btn: 0 6px 20px rgba(232,96,76,.38);  /* clay button glow */
```

---

## Buttons

### Primary (Clay)
```css
background: #e8604c; color: #fff; border: none;
padding: 14px 32px; border-radius: 50px;
font: 700 15px/1 'Sora', sans-serif; letter-spacing: .2px;
box-shadow: 0 6px 20px rgba(232,96,76,.38);
transition: background .2s, transform .15s, box-shadow .2s;
```
Hover: `background: #c94d3a; transform: translateY(-2px); box-shadow: 0 10px 28px rgba(232,96,76,.48);`

### Primary Rounded-Square (forms)
Same as above but `border-radius: 12px` instead of `50px`.

### Outline
```css
background: transparent; color: #e8604c;
border: 2px solid #e8604c; padding: 12px 28px; border-radius: 50px;
font: 700 14px/1 'Sora', sans-serif;
```
Hover: fill with `#e8604c`, `color: #fff`.

### Green Tag / Badge
```css
background: #eaf4ef; color: #2D6A4F;
border: 1px solid rgba(45,106,79,.2);
padding: 5px 14px; border-radius: 50px;
font: 700 11px/1 'Sora', sans-serif; letter-spacing: 1px; text-transform: uppercase;
```

---

## Form Inputs

```css
/* All inputs, selects, textareas */
padding: 12px 16px;
border: 1.5px solid #ede5dc;
border-radius: 10px;
font: 400 14.5px/1.4 'Sora', sans-serif;
background: #fff9f6; color: #1c1a18;
transition: border-color .2s, box-shadow .2s, background .2s;
outline: none;

/* Focus */
border-color: #e8604c;
box-shadow: 0 0 0 3px rgba(232,96,76,.1);
background: #ffffff;

/* Labels */
font: 700 12px/1 'Sora', sans-serif;
text-transform: uppercase; letter-spacing: .7px;
color: #1c1a18; margin-bottom: 7px;
```

### Pill Selectors (radio/checkbox groups)
```css
/* Option pill */
display: flex; align-items: center; gap: 8px;
background: #fff9f6; border: 1.5px solid #ede5dc;
border-radius: 10px; padding: 9px 16px;
font: 400 13.5px/1 'Sora', sans-serif; color: #5a5248;
cursor: pointer; transition: all .15s;

/* Checked state */
background: #fff3ef; border-color: #e8604c;
color: #c94d3a; font-weight: 600;
```

---

## Cards

```css
/* Standard card */
background: #ffffff;
border-radius: 20px;
border: 1px solid #ede5dc;
box-shadow: 0 2px 16px rgba(60,30,10,.08), 0 8px 40px rgba(60,30,10,.06);
overflow: hidden;

/* Green header variant (info card) */
.card-header-green {
  background: #2D6A4F; padding: 32px 28px;
  color: #fff;
}
```

---

## Section Patterns

### Page Hero Banner (warm gradient)
```css
background: linear-gradient(135deg, #fde8e3 0%, #fdf0e8 50%, #fdf6ec 100%);
padding: 64px 48px 72px; text-align: center;
border-bottom: 1px solid #f0e4da;
```

### Dark CTA Banner (bottom-of-page)
```css
background: #1c1a18; padding: 72px 48px; text-align: center;
h2: font-family Lora, 2.8rem, color #e8604c, uppercase, letter-spacing 2px;
```

### Map Section
```css
background: #ffffff;
border-top: 1px solid #ede5dc;
```

---

## Page Layout

- Max content width: **1180px**, `margin: 0 auto`
- Default section padding: **64px 48px**
- Mobile breakpoint: **768px** → single column, padding 40px 24px
- Tablet breakpoint: **1024px** → stack two-column grids

---

## Icons / Emoji System
Use emoji as functional icons (no icon library dependency):
- 📞 Phone  ✉️ Email  📍 Location  🕐 Hours  ✈️ Air shipping  🚗 Delivery
- 🦜 Parrot brand icon  ✅ Confirmation  ❋ Section divider (decorative)

---

## Trust Signals (standard set)
Always include at least two on every transactional page:
- "USDA-Licensed Breeder"
- "CITES Appendix II Documented"
- "DNA-Sexed & Vet-Certified"
- "Ships Nationwide from $185"
- "24–48 Hour Response Guarantee"
- "Health Guarantee on Every Bird"

---

## Anti-Copy: DISABLED
All `user-select: none` CSS and `wpcp_css_disable_selection` JS have been removed from all pages. Never add them back. Visitors must be able to select and copy text.

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
| Contact page | `site/content/contact-us/index.html` |
| Design system | `docs/design.md` (this file) |
| Contact form skill | `skills/cag-contact-form.md` |

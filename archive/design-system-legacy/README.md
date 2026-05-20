# CongoAfricanGreys Design System

The visual + content system for **CongoAfricanGreys.com** — a family-owned,
captive-bred African Grey parrot breeder in Midland, Texas (est. 2014).
Owners: **Mark & Teri Benjamin**. USDA AWA-licensed, CITES Appendix II
compliant, DNA-sexed, avian-vet certified. No wild-caught birds.

This system is the **"Terracotta Warmth"** direction — derived from the
contact-us page rebuild and applied across every page, component, navbar,
and footer.

---

## Sources

- `uploads/design.md` — full design spec (Design B "Terracotta Warmth"),
  the canonical source for tokens, type, components, copy patterns.
- Website (production reference): **https://congoafricangreys.com/**
- Logo (referenced in source spec, not provided): `/wp-content/uploads/african-grey-parrot-store-logo.png`

> No codebase or Figma were attached — every token below comes from
> `uploads/design.md`. The UI kit recreates the look implied by that
> spec; if/when the WordPress source ships, swap real screenshots in.

---

## Brand Identity

- **Tone:** Warm, trustworthy, premium — like a high-end pet boutique,
  not a generic directory.
- **Audience:** Parrot buyers (first-timers and experienced) seeking
  CITES-documented, captive-bred birds. People making a 30+ year
  commitment to a bird — they want to feel safe, informed, welcomed.
- **Positioning:** Small family aviary, not a pet store. Documentation
  and provenance are the product. Warmth is the differentiator.

---

## Content Fundamentals

**Voice.** First-person plural ("we", "our birds", "our family aviary")
when speaking as the breeder; second-person ("you", "your new companion")
when speaking to the buyer. Never corporate "the company". Warm,
grounded, never breathless.

**Trust signals are content.** At least two of these appear on every
transactional page — they read as facts, not marketing:
- "USDA-Licensed Breeder"
- "CITES Appendix II Documented"
- "DNA-Sexed & Vet-Certified"
- "Ships Nationwide from $185"
- "24–48 Hour Response Guarantee"
- "Health Guarantee on Every Bird"

**Casing.**
- Headlines (Lora): sentence case or Title Case — never ALL CAPS in
  body headings.
- Uppercase is reserved for: short tags ("USDA LICENSED"), section
  eyebrows ("OUR FAMILY"), the dark-banner CTA headline, and form
  labels. Always with `letter-spacing: 1px` (tags) or `2px` (banner).
- Buttons: Title Case ("Reserve Your African Grey", "Send Inquiry").

**Punctuation.** Em dashes for warmth ("captive-bred — every one of
them"). Ampersands fine in titles ("Mark & Teri"). Numbers spelled out
under ten in body copy; numerals everywhere in stats/specs ("$185
shipping", "24–48 hours", "9-year-old hen").

**Emoji.** Yes — used as **functional icons**, not decoration, and
sparingly. Canonical set:
`📞 Phone · ✉️ Email · 📍 Location · 🕐 Hours · ✈️ Air shipping · 🚗 Delivery · 🦜 Parrot · ✅ Confirmation · ❋ Section divider`
No 🎉, 🔥, 🚀, or other "marketing" emoji. One emoji per element max.

**Words we use.** "captive-bred", "hand-fed", "weaned", "hen / cock",
"clutch", "aviary", "companion bird", "CITES Appendix II", "DNA-sexed",
"avian vet certified", "health guarantee", "lifetime support".

**Words we avoid.** "stock", "inventory", "product", "purchase",
"shop now", "limited time", "deal", "exotic" (loaded), "tame" (we say
"hand-fed and socialized").

**Example copy.**

> **Hero, sentence case.**
> *Bringing home an African Grey is a 30-year decision. We've spent
> the last decade helping families make it well.*

> **Card eyebrow + heading.**
> `OUR FAMILY` (tag, uppercase) — *Mark & Teri Benjamin, Midland TX*
> (Lora italic).

> **CTA banner, uppercase.**
> *RESERVE YOUR AFRICAN GREY*

> **Form helper, plain.**
> "Tell us about your home — we read every inquiry personally and
> reply within 24–48 hours."

---

## Visual Foundations

**Palette.** Three-anchor system — **forest green** (`#2D6A4F`) for
nav/headers and trust framing, **clay/terracotta orange** (`#e8604c`)
for every CTA and active accent, **warm cream** (`#faf7f4`) as the
page surface. `--gold` is aliased to `--clay` so any "gold" class
in legacy CSS renders orange. Borders are a single warm taupe
(`#ede5dc`). Text is a near-black warm (`#1c1a18`) over a sliding
warm-grey ramp.

**Type.** Two families, no exceptions.
- **Lora** (serif, 700, italic available) — every headline, card
  title, hero. Italic is used sparingly for emphasis inside a
  headline ("our *family* aviary").
- **Sora** (sans, 400–700) — all body, labels, nav, buttons. 16px
  body, 14px nav, 11px uppercase tags with 1px letter-spacing.

**Spacing.** 8-point-ish scale: 4 / 8 / 16 / 24 / 40 / 64 / 96 px.
Sections are 64px vertical / 48px horizontal on desktop, collapsing
to 40 / 24 on mobile. Max content width is **1180px**, centered.

**Radii.** Soft. 8 / 10 / 14 / 20 / 50(pill). Cards land at **20px**.
Form inputs at **10px**. CTA buttons and tags use the **pill (50px)**
— this is a brand signature. Square buttons (`12px`) only appear
inside forms.

**Backgrounds.** No full-bleed photography on layout chrome — photos
live inside cards (bird portraits). Section variety comes from:
- The **warm gradient hero** — `linear-gradient(135deg, #fde8e3 0%, #fdf0e8 50%, #fdf6ec 100%)` with a 1px bottom border in `--border`.
- **White card surfaces** floating on cream.
- The **dark CTA banner** (`#1c1a18`) near page bottom, headline in
  clay uppercase.
- The **forest-green nav** at the top.
No repeating patterns, no textures, no gradients besides the hero
and the implicit button glow.

**Shadows.** Two scales (`--shadow`, `--shadow-lg`), both warm-tinted
(`rgba(60,30,10,.08)`) — never neutral grey. Plus a dedicated
**button glow** `0 6px 20px rgba(232,96,76,.38)` that intensifies on
hover. No inner shadows. No neon. No layered hard drop-shadows.

**Borders.** Always `--border` (`#ede5dc`), 1px or 1.5px. Outline
buttons use 2px clay. Focus rings on inputs are a 3px clay halo at
10% opacity — never blue.

**Cards.** White (`#ffffff`), 20px radius, 1px `--border`, the
standard warm shadow, `overflow: hidden`. The "info card" variant
has a forest-green header band over the white body.

**Buttons.**
- **Primary (clay pill)** — `#e8604c` fill, white text, 50px radius,
  Sora 700/15px, button glow. Hover lifts 2px and darkens to
  `#c94d3a`.
- **Outline** — transparent / 2px clay border / clay text. Hover
  fills clay.
- **Form primary** — same clay fill but 12px radius (square-ish) so
  it sits naturally in input rows.
- **Green tag / badge** — `#eaf4ef` bg, forest text, 11px uppercase
  with 1px tracking, pill radius.

**Form inputs.** Cream-tinted (`#fff9f6`) fields, 1.5px `--border`,
10px radius, Sora 14.5px. Focus: clay border + 3px clay halo +
white background. Labels above, uppercase, 12px Sora 700.

**Pill selectors** (radio/checkbox groups) — clickable pills with the
same cream/border treatment; checked state warms to `#fff3ef`, clay
border, clay-dark text, weight 600.

**Motion.** Subtle and short.
- Color/bg changes: `0.2s`.
- `transform` lifts on hover (translateY -2px): `0.15s`.
- Easing: default browser `ease` is fine; for orchestrated motion use
  `cubic-bezier(.4,0,.2,1)`.
- No spring physics, no bounce, no parallax, no auto-playing video.
- Page-load: tiny fade-up on cards (8–12px, 250ms) is acceptable.

**Hover states.**
- Buttons: darken bg + lift 2px + deepen glow.
- Links: text shifts from clay → clay-dark; underline only on
  inline body links.
- Cards: a touch more shadow (`--shadow-lg`) and a 2px lift.
- Nav links: a thin clay underline grows in from the left.

**Press / active states.** Buttons shrink the lift back to 0 and use
`--clay-dk` fill — i.e. they re-settle into the page. No scale-down.

**Focus.** Always visible — 3px clay halo at 10% opacity on form
controls, 2px clay outline (offset 2px) on linked tiles.

**Transparency & blur.** Used almost never. The only acceptable use is
a faint clay halo on focus rings (already in the system). No glass
morphism. No backdrop-filter on nav. Solid forest green.

**Imagery.** Bird photography is **warm-toned**, natural light, gentle
contrast — no studio b&w, no grain, no heavy edit. Photos always sit
inside white cards with rounded corners; never bleed to the page edge.
A typical aspect is 4:3 portrait of a perched bird, framed loosely.

**Layout rules.** Fixed nav at top (forest green, no transparency).
Footer is dark (`#1c1a18`). Everything between is on cream. Two
column grids stack at 1024px; everything single-column at 768px.

**Iconography.** Emoji-as-icons (see Content Fundamentals + ICONOGRAPHY).
No icon font, no SVG icon set. The bird (🦜) is the brand-mark
fallback when a logo image is unavailable.

---

## Iconography

**The system uses emoji as functional icons** — by deliberate choice
in `uploads/design.md`. No Heroicons / Lucide / Font Awesome / custom
SVG sprite. Two reasons: (1) zero icon-library dependency on a
WordPress site, and (2) the warm/personal tone tolerates emoji where
a B2B SaaS would not.

**Canonical icon vocabulary** (do not substitute):

| Emoji | Meaning | Where it appears |
|---|---|---|
| 🦜 | Brand mark / parrot | Logo fallback, footer, hero accent |
| 📞 | Phone | Contact rows, CTA next to phone number |
| ✉️ | Email | Contact rows, form labels |
| 📍 | Location | Address, map pin, "Midland, TX" |
| 🕐 | Hours | Business hours rows |
| ✈️ | Air shipping | Shipping section, trust pills |
| 🚗 | Local delivery | Shipping section |
| ✅ | Confirmation | Success states, form submitted |
| ❋ | Section divider | Decorative break between hero and content |

**Rules.**
- One emoji per element. Never stack them.
- Always paired with text — emoji is reinforcement, not the label.
- Size: match the line-height of adjacent text (`1em`), or `1.4em`
  when isolated in an icon-cell (e.g. trust pill rows).
- Never wrap an emoji in a colored circle "chip" — that's a SaaS
  trope this brand doesn't use.
- Logo image (`african-grey-parrot-store-logo.png`) takes precedence
  over 🦜 when available.

**Logo.** Source spec references
`/wp-content/uploads/african-grey-parrot-store-logo.png`. That asset
was **not provided to this project**; the UI kit uses a 🦜 wordmark
("🦜 CongoAfricanGreys") in Lora 700 as a stand-in. **Ask the user
to drop the real PNG into `assets/`** when iterating.

**Imagery.** Bird photography placeholders in the UI kit are simple
warm-tinted boxes labeled "Bird photo — drop in". Same ask: the real
photos live in `/wp-content/uploads/` on the production site; copy
them into `assets/birds/` when iterating.

---

## Files in this system

```
README.md                  ← you are here
SKILL.md                   ← agent-skill entry point
colors_and_type.css        ← all tokens (colors, type, space, radius, shadow, motion)

uploads/
  design.md                ← original spec (source of truth)

assets/                    ← logos, photos, anything visual
  README.md                ← what's expected here + asks

preview/                   ← Design System tab cards (registered)
  type-specimen.html
  color-brand.html
  color-surfaces.html
  color-text.html
  spacing.html
  radii.html
  shadows.html
  buttons.html
  form-inputs.html
  pill-selectors.html
  cards.html
  trust-pills.html
  emoji-icons.html
  hero-gradient.html
  cta-banner.html

ui_kits/
  website/                 ← the CongoAfricanGreys.com recreation
    README.md
    index.html             ← interactive click-thru
    Navbar.jsx
    Hero.jsx
    BirdCard.jsx
    TrustRow.jsx
    InfoCard.jsx
    ContactForm.jsx
    DarkCTA.jsx
    Footer.jsx
```

---

## Caveats / open asks

- **Logo PNG missing.** Drop the real
  `african-grey-parrot-store-logo.png` into `assets/`.
- **Bird photography missing.** Drop a handful of representative
  bird photos into `assets/birds/`.
- **No codebase or Figma access.** UI kit was built directly from
  `uploads/design.md`. If a WordPress codebase is available, attach
  it and the kit will be re-aligned to real markup.
- **Fonts** — Lora and Sora are Google Fonts; no local `fonts/`
  folder needed. Loaded via the `@import` at the top of
  `colors_and_type.css`.

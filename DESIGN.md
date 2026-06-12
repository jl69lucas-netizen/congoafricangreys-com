# Design

> Visual system for CongoAfricanGreys.com, read by `/impeccable` before any design work.
> Synthesized 2026-06-03 from `docs/design.md` (Terracotta Warmth v2), `skills/cag-direction-d-theme.md`
> (live theme), `src/styles/global.css`, and `CLAUDE.md` design law. This file answers *how it looks*.
> **Source-of-truth tokens** live in `src/styles/global.css` + `cag-design-system.css`; this file mirrors them.
> Locked values are marked **🔒** and must not drift.

## Theme

**"Terracotta Warmth" + Direction D "Modern Editorial"** — the live, site-wide theme (applied
globally via `body.theme-d` in BaseLayout; agents do NOT re-implement it per page).

Light theme only. No dark mode (dark is used only as deliberate punctuation: the bottom CTA banner
and footer). The scene: a warm, calm, premium family aviary — cream paper, forest-green framing,
terracotta accents, literary serif headlines. Reads like an editorial magazine feature, not an app.

**Color strategy: Committed.** Forest green + terracotta carry the identity across cream; this is
intentionally past "Restrained" — the brand colors are load-bearing, not a single ≤10% accent.

## Color

Palette is **locked in hex** (brand law: do not convert or drift). OKLCH shown for reference only.

| Role | Token | Hex 🔒 | Notes |
|---|---|---|---|
| Brand green (nav, headers, trust framing) | `--green` / `--forest` | `#2D6A4F` | |
| Clay / terracotta (CTAs, accents) | `--clay` | `#e8604c` | brand fill. `--gold` **must** equal this 🔒 |
| Clay hover / pressed | `--clay-dk` | `#c94d3a` | |
| Clay light (hover/gradient) | `--clay-lt` | `#f08070` | |
| Cream (page surface) | `--cream` | `#faf7f4` | |
| Warm white (inputs, inner cards) | `--warm-white` | `#fff9f6` | |
| Card surface | `--card-bg` | `#ffffff` | never pure-white as text-on-color |
| Border / divider | `--border` | `#ede5dc` | warm-tinted, never grey |
| Light green (success/tag bg) | `--green-lt` | `#eaf4ef` | |
| Text — primary (warm near-black) | `--text` | `#1c1a18` | |
| Text — secondary (body) | `--mid` | `#5a5248` | |
| Text — tertiary (caption) | `--light` | `#9b9189` | |
| Dark panel (CTA banner, footer) | `--dark-panel` | `#1c1a18` | |

**Three anchors only:** Forest Green (framing), Clay (every CTA), Cream (surface). Tint all neutrals
warm — never `#000`/`#fff` as flat UI grey, never cool grey shadows.

### Contrast tokens (added 2026-06-03 — fixes the AA audit failures)

The locked `--clay #e8604c` gives white text only **3.38:1** — it passes AA only as *large* text
(≥18.66px bold / ≥24px). For small text-bearing surfaces, use a darker clay; **do not redefine
`--clay`**:

| Token | Value | Use |
|---|---|---|
| `--clay-ink` 🆕 | `#bd4129` (≈4.6:1 reverse / ~4.7:1 on white) | white CTA text <18px; clay link/label text <18px; replaces `text-clay/70` |
| `--green-ink` 🆕 | `#1f5a41` or existing `#b04228` clay | eyebrows on cream (replaces muted `#6b9480` 3.18:1) |

Rules going forward: **never** use opacity-tinted text (`clay/70`, `white/65`, `text-stone-400` on
light) as legible copy; on `--dark-panel`, body text must be ≥`#e7ddd2`.

## Typography

**Live (Direction D) — applied globally:**

| Role | Font (live) | Token-level fallback | Weight |
|---|---|---|---|
| All headings H1–H6 | **Newsreader** (literary serif, `opsz` pinned) | Lora | 500–600 |
| Body, labels, buttons, nav | **IBM Plex Sans** | Sora | 400–700 |

The markup still uses the `font-lora` / `font-sora` utility classes; `direction-d.css` restyles them
to Newsreader / IBM Plex automatically. **Do not hard-code `font-family` to fight the theme.** Lora
(serif) + Sora (sans) remain the token-level fallback if Direction D is ever removed.

**Fluid clamp scale 🔒 (in `global.css` `@layer base` — never override with Tailwind `text-*` on H2/H3):**

| Var | clamp | 375px → 1280px | Applied |
|---|---|---|---|
| `--fs-h1` | `clamp(1.75rem, 5vw, 3rem)` | 28 → 48px | `h1`, lh 1.1 |
| `--fs-h2` | `clamp(1.25rem, 3.5vw, 2rem)` | 20 → 32px | `h2`, lh 1.18 |
| `--fs-h3` | `clamp(1.0625rem, 2.2vw, 1.5rem)` | 17 → 24px | `h3`, lh 1.25 |
| `--fs-h4` | `clamp(0.9375rem, 1.8vw, 1.25rem)` | 15 → 20px | `h4`, lh 1.3 |
| `--fs-h5` | `clamp(0.6875rem, 1.1vw, 0.875rem)` | 11 → 14px | `h5,h6`, lh 1.3 |
| `--fs-body` | `clamp(0.9375rem, 1.5vw, 1.0625rem)` | 15 → 17px | `body`, lh 1.65 |
| `--fs-eyebrow` | `clamp(0.625rem, 1.2vw, 0.75rem)` | 10 → 12px | eyebrow spans |
| `--fs-caption` | `clamp(0.75rem, 1vw, 0.875rem)` | 12 → 14px | captions |

- Body line-height 1.65; paragraph `max-width: 65ch` (inline `70ch` overrides allowed).
- **Eyebrows:** calm uppercase + clay underline-tick (the brand signature), `tracking ≈0.12–0.18em`,
  `font-medium`. Never `text-3xl` on section H2/H3. Casing: sentence/Title case headings, never ALL CAPS
  body headings; uppercase only for tags, eyebrows, dark-banner CTA, form labels.

## Layout

Container system **Option A — Classic 1200px 🔒**:

- Every page: outer shell `.container` `max-width: 1200px`, `margin: 0 auto`.
- Informational / long-form: add `.container-text` `max-width: 760px` inner wrapper.
- All `<p>`: `max-width: 70ch`.
- Breakpoints: ≥1025px → 1200px, 48px pad · 768–1024px → 90–94% fluid, 32px · ≤767px → 92%, 16px.
- Section padding: desktop 64px tb / 48px sides; mobile 40px / 24px. Two-col grids collapse at 1024px.
- Infographic wrappers: **760px** (species/blog/care) or **1100px** (home/location/hero); height
  400px fixed desktop, auto mobile. Never `900px` / `max-w-4xl`.

Spacing scale: `4 / 8 / 16 / 24 / 40 / 64 / 96`. Vary padding for rhythm — same padding everywhere
reads monotonous (a current homepage weakness).

## Components

20px-radius cards, 1px `--border`, warm shadow, white surface; info cards use a green header band.
**Nested cards are banned.** Full component registry: `docs/reference/components.md` (24 named
components). Key signatures:

- **Primary CTA = clay pill, `border-radius: 50px` 🔒** (brand signature). Form submit buttons use
  `12px`. Outline = 2px clay border, fills clay on hover.
- Green tag/badge: `#eaf4ef` bg, `#2D6A4F` text, pill, 11px uppercase.
- Cards: radius 20px, warm shadow `rgba(60,30,10,…)`, hover lift `translateY(-2px)`.
- Form inputs: 10px radius, 1.5px border, `#fff9f6` bg, clay focus ring `0 0 0 3px rgba(232,96,76,.1)`.

## Border radius

`8 (badge) / 10 (input) / 14 (map,icon) / 20 (card) / 50px (pill — brand signature 🔒)`.

## Shadows

Always warm-tinted, never neutral grey, no inner shadows, no neon:

```
--shadow:    0 2px 16px rgba(60,30,10,.08), 0 8px 40px rgba(60,30,10,.06);
--shadow-lg: 0 4px 24px rgba(60,30,10,.1),  0 16px 56px rgba(60,30,10,.08);
--shadow-btn: 0 6px 20px rgba(232,96,76,.38);
```

## Motion

Max 0.2s color/bg; 0.15s transform lift (`translateY(-2px)`); easing `cubic-bezier(.4,0,.2,1)`.
Card load fade-up 8–12px / 250ms is allowed. **No** bounce, spring, parallax, or auto-playing video.

## Iconography & emoji

**Line icons, not emoji** (site-wide sweep 2026-06-03, commit `9ff570f`). Functional icons are inline
**Feather-style SVGs** — `viewBox="0 0 24 24"`, `width/height="1em"`, `stroke="currentColor"` so each icon
inherits the call site's size + color. One per element, always paired with text, never in a colored circle
chip. The icon map + repeatable transform live in **`scripts/emoji_to_icons.py`** (copy a path from its `P`
map, or from any TrustBar / ScamAwareness icon). ~60 decorative emoji across 44 files were replaced; the
former canonical contact set (📞 ✉️ 📍 🕐 ✈️ 🚗) is now phone / mail / map-pin / clock / plane / car line icons.

- **✅ → green `#2D6A4F` check-circle** line icon. *(This supersedes ✅'s former spot in the locked canonical
  set — reconciled 2026-06-03 per the full line-icon consistency decision.)*
- **Kept as text glyphs (NOT converted):** ✔ ✗ ★ — list / pros-cons / rating markers. `⌂` `⌄` are technical
  UI symbols (mobile-nav home, dropdown caret), also fine as text.
- **Bird marks use images, never 🦜:** `/emoji/cag-congo.png`, `/emoji/cag-timneh.png`.
- **Banned permanently:** 🎉 🔥 🚀 and *any* colorful pictograph emoji (🏆 🧬 ⚠️ 📋 📜 🩺 🏛 … ) — use a
  line-icon SVG instead.

**Render rule 🔒:** an icon supplied from a data array rendered via `{x.icon}` / `{b}` must use `set:html`,
or the SVG string shows as literal `<svg>` text. After any icon change: `npx astro build`, then confirm
`grep -rl "&lt;svg" dist/` is empty.

## Accessibility

WCAG 2.1 AA target. Audience skews older → contrast and text size matter more than usual. Use the
`--clay-ink` / `--green-ink` contrast tokens above for small text; reserve `--clay #e8604c` for fills
and large display text. Semantic H1–H6 order, ARIA on controls, alt text on every image, reduced-motion
honored, no `user-select: none`.

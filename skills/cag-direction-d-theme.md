---
name: cag-direction-d-theme
description: The LIVE site-wide visual theme for CongoAfricanGreys.com — Direction D "Modern Editorial" (Newsreader serif headings + IBM Plex Sans body, refined Terracotta Warmth palette). Read before building or restyling ANY page. Explains that the theme is already global via src/styles/direction-d.css + body.theme-d (BaseLayout) and must NOT be re-implemented per page. Use when designing, building, or restyling a page and you need the canonical theme rules (typography, palette, dividers, motion) or are unsure whether to add theme CSS.
---

# Skill: CAG Direction D — "Modern Editorial" Site Theme

> **Status:** LIVE SITE DEFAULT (approved 2026-06-01, promoted site-wide 2026-06-01).
> **What it is:** The canonical visual theme for every page on CongoAfricanGreys.com.
> **Where it lives:** `src/styles/direction-d.css` + `body.theme-d` (set in `src/layouts/BaseLayout.astro`).
> **Golden rule:** It is already global. **Do NOT re-implement it per page.** Build normal markup with the existing design-system classes and the theme is applied automatically.

---

## 1. What Direction D Is

"Modern Editorial" — a literary, magazine-grade refinement of the Terracotta Warmth design system. It keeps the locked palette (Forest `#2D6A4F` / Clay `#e8604c` / Cream `#faf7f4`) and the clay pill CTA, and layers on:

| Layer | Treatment |
|---|---|
| **Headings** | `Newsreader` literary serif, weight 600, optical size pinned (`opsz` 18, `font-optical-sizing:none`), `letter-spacing:-.003em`. Calmer and lower-contrast than Lora. Applies to all of H1–H6 and their child accent spans. |
| **Body** | `IBM Plex Sans` (overrides the `.font-sora` utility). |
| **Lead-line paragraphs (Layout B)** | The first `<p>` immediately after an H1 or H2 reads larger (`1.08em`), looser (`line-height:1.7`), and inkier (`--ink: #20342b`). |
| **Eyebrows** | Uppercase labels get `letter-spacing:.18em` + weight 600, and (inside centered or `mb-2/6/7/8` containers) a 44×2px **clay underline tick** below them. |
| **Cards** | `<article>` elements get a soft-warm frame: 18px radius, 1px hairline border, warm shadow `0 6px 26px rgba(60,30,10,.08)`, and a calm `-4px` hover lift. |
| **Buttons** | Clay pill CTAs (`rounded-full`) keep the brand signature and get a calm `-2px` rise on hover. |

### Deliberately NOT global (homepage-only)
Two Direction D rules were tuned to the homepage's exact top-level section structure and remain scoped to the homepage's `.home-d` wrapper in `src/pages/index.astro` — **do not port them site-wide**:
- Hairline dividers between top-level sections (`.home-d > * + * { border-top… }`)
- Compact-padding overrides on `py-12/14/16` bands

Other pages have varied top-level structure; applying those globally produces stray dividers and broken spacing.

---

## 2. How It's Wired (architecture)

```
BaseLayout.astro
├─ imports global.css         (tokens + Tailwind + fluid type base)
├─ imports direction-d.css    (THIS theme — loads after global so it wins ties)
├─ <head> loads Newsreader + IBM Plex Sans (alongside Lora/Sora)
└─ <body class="theme-d …">   ← the single switch that turns the theme on
```

- All rules are scoped under `body.theme-d`, so they only need the body class — which every page gets through BaseLayout.
- Font overrides use `!important` to beat Tailwind's `.font-sora` utility. Card/button/eyebrow rules don't need it (un-layered CSS already beats Tailwind utility layers).
- **Palette is untouched.** Direction D changes type, rhythm, and surfaces — never the three locked colors.

---

## 3. Rules for Agents (page builders, section builders, infographics)

1. **Don't add fonts or a `.home-d`/`.theme-d` block to a new page.** The theme is inherited. Just write content from the hero `<section>` down (per Rule 53 BaseLayout inheritance).
2. **Keep using the design-system classes** — `font-lora`, `font-sora`, `text-clay`, `rounded-full`, `.uppercase` eyebrows, `<article>` cards. Direction D restyles them automatically; you don't change the class names.
3. **Headings will render in Newsreader serif** even if you keep `font-lora` on them — that's expected and correct. Don't fight it with inline `font-family`.
4. **Want the lead-line effect?** Put the section's opening paragraph immediately after its H2 (`<h2>…</h2><p>…</p>`) — no wrapper between them.
5. **Want an eyebrow tick?** Use `<p class="… uppercase …">EYEBROW</p>` inside a centered or `mb-2/6/7/8` container.
6. **Want a soft-warm card?** Use a semantic `<article>` element.
7. **Never** introduce `user-select:none`, marketing emoji, or the generic 🦜 (see CLAUDE.md design rules) — Direction D doesn't change those bans.
8. **To tune the theme site-wide:** edit `src/styles/direction-d.css` only — never duplicate its rules into a page. One source of truth.

---

## 4. Verification (after any page build)

Run the dev server and confirm on the new page:
- `getComputedStyle(h1).fontFamily` starts with `Newsreader`
- `getComputedStyle(document.body).fontFamily` starts with `IBM Plex Sans`
- `document.body.classList.contains('theme-d')` is `true`
- An `<article>` (if present) shows `border-radius:18px` + the warm box-shadow
- Build is clean: `npx astro build`

---

## 5. Change Log
- **2026-06-01** — Direction D approved on the homepage (`src/pages/index.astro`, `.home-d` wrapper).
- **2026-06-01** — Promoted to the **site default**: extracted the universal layers (typography + lead-line + eyebrow + cards + buttons) into `src/styles/direction-d.css`, added `body.theme-d` + Newsreader/IBM Plex Sans in BaseLayout. Homepage-structural dividers/padding kept scoped to `.home-d`. Verified on the care guide + Florida location page; 98 pages build clean.

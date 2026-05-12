---
name: cag-header-search
description: Adds or modifies the site search bar in the CongoAfricanGreys.com Astro header. Use whenever the user asks to add, move, resize, restyle, or remove the search bar in the header — on mobile, desktop, or both. Also use when modifying the search overlay or the search icon button in Header.astro.
---

# CAG Header Search Pattern

The header search uses Google site-search (`action="https://www.google.com/search"` with a hidden `sitesearch` input). No backend needed.

## File to edit
`src/components/Header.astro`

## Current layout zones (left → right in the flex row)

| Zone | Breakpoint | Contents |
|------|-----------|----------|
| Logo | always | `<Logo />` |
| Desktop nav | `hidden lg:flex` | nav links |
| Desktop right | `hidden sm:flex` | search form + Inquire Now CTA |
| Mobile search | `flex lg:hidden flex-1 mx-3` | inline search form |
| Mobile hamburger | `lg:hidden` | `<details>` dropdown with nav links |

## Search form snippet (reusable for any zone)

```html
<form action="https://www.google.com/search" method="get" class="flex gap-2 {SIZE_CLASSES}">
  <input type="hidden" name="sitesearch" value="congoafricangreys.com" />
  <input
    name="q"
    type="search"
    placeholder="Search…"
    class="flex-1 bg-white/10 border border-white/30 text-white placeholder:text-white/50 rounded-full px-3 py-1.5 text-xs focus:outline-none focus:border-clay"
  />
  <button type="submit" class="bg-clay text-white text-xs font-semibold px-3 py-1.5 rounded-full hover:bg-clay-dk transition-colors">
    Go
  </button>
</form>
```

For desktop: wrap in `hidden sm:flex lg:flex items-center` and set `w-48` or `w-56` on the input for a fixed width.

## Placement rules

- **Mobile inline** (between logo and hamburger): `flex lg:hidden flex-1 mx-3` on the `<form>`
- **Desktop right section**: place the `<form>` inside the `hidden sm:flex items-center gap-2` div, before the Inquire Now `<a>`; use `w-44` on the input to keep it compact
- **Both mobile and desktop**: use the two separate form blocks above (one per zone)

## Search overlay (legacy toggle pattern)

The overlay (`id="search-overlay"`) + search icon button + script are only needed if the search bar is NOT shown inline on desktop. If you add an inline desktop search form, remove:
1. The `<button id="search-btn">` icon button
2. The `<div id="search-overlay">` panel below the header
3. The `<script>` toggling `.hidden`

## Design tokens used
- `bg-clay` / `hover:bg-clay-dk` — orange submit button (#e8604c / #c94d3a)
- `border-clay` — orange focus ring
- `bg-white/10`, `border-white/30`, `text-white/50` — ghost input on green background

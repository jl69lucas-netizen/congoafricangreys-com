# CAG Page Width System — Option A (Classic 1200px)
**Approved: 2026-05-19. Applies to all pages.**

---

## Why Option A

Current container is 1180px — near-zero migration cost to 1200px. The site is
content-heavy with long-form informational pages (scam guide, care guides, species guides).
Option A's 760px text column matches the existing narrow-body reading pattern already in use.
The site is a family breeder operation, not a luxury photography brand — 1440px would be overkill.

---

## Container Classes

| Class | Max-width | Use |
|---|---|---|
| `.container` | 1200px | All pages — outer shell |
| `.container-text` | 760px | Informational / long-form text content |
| `p { max-width: 70ch }` | ~70 chars | All paragraphs — prevents unreadable long lines |

CSS variables: `--container: 1200px` · `--container-text: 760px`

---

## Breakpoints

| Name | Width | Container behavior | Side padding |
|---|---|---|---|
| Desktop | ≥1025px | max-width 1200px, centered | 48px |
| Tablet | 768–1024px | fluid 90%–94% of screen | 32px |
| Mobile | ≤767px | fluid 92% of screen | 15–20px |

---

## Page Type → Layout Assignment

| Page Type | Outer Container | Text Container | Grid |
|---|---|---|---|
| Homepage | `.container` 1200px | — | 3–4 col bird card grid |
| Available Birds / Gallery | `.container` 1200px | — | 3-col card grid |
| Location pages (50 states) | `.container` 1200px | — | 2-col + sidebar |
| Scam Guide | `.container` 1200px | `.container-text` 760px | Single col prose |
| Species / Care Guides | `.container` 1200px | `.container-text` 760px | Single col prose |
| Blog posts / Articles | `.container` 1200px | `.container-text` 760px | Single col prose |
| Contact / About | `.container` 1200px | — | 2-col |
| Pricing pages | `.container` 1200px | — | Comparison table |

---

## CSS Implementation

```css
/* --- Containers --- */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
}
.container-text {
  max-width: 760px;
  margin: 0 auto;
}

/* --- Paragraphs --- */
p { max-width: 70ch; }

/* --- Sections --- */
.section { padding: 64px 0; }

/* --- Tablet --- */
@media (max-width: 1024px) {
  .container { width: 92%; padding: 0 32px; }
  .section { padding: 56px 0; }
}

/* --- Mobile --- */
@media (max-width: 767px) {
  .container { width: 92%; padding: 0 16px; }
  .container-text { padding: 0; }
  .section { padding: 40px 0; }
}
```

---

## Responsive Typography Scale

| Element | Mobile ≤480px | Tablet 481–1024px | Desktop ≥1025px | Notes |
|---|---|---|---|---|
| H1 | 28–32px | 36–40px | 44–48px | line-height 1.2, weight 700 |
| H2 | 22–24px | 26–28px | 32–34px | major sub-sections |
| H3 | 18–20px | 22–24px | 24–26px | card headings |
| H4 | 16px | 18px | 20px | sidebar / feature titles |
| H5/H6 | 14px ALL-CAPS | 14px ALL-CAPS | 16px ALL-CAPS | utility text, labels |
| Lead / subheader | 16–17px | 18–19px | 20–21px | opening paragraph of page |
| Body | 15–16px | 16–17px | 17–18px | line-height 1.6–1.7 |
| Caption | 12px | 13px | 14px | image captions, sources |

Font weights: H1–H3 = 700 bold (or 600 semi-bold). Body = 400 regular.

---

## Header / Navigation Container Exception

The header/nav spans full width (up to 1400–1600px fluid) to allow logo far-left
and CTA button far-right. Only the main content area uses the 1200px container.
This is intentional — it gives a wide professional feel in the nav while keeping
body content readable.

---

## Agent Rules

1. **Every new page** must use `.container` as the outermost content wrapper.
2. **Informational pages** (guides, articles, blog posts) must add `.container-text` around the main prose area.
3. **Never** hard-code `max-width: 1180px` — use `1200px` or `var(--container)`.
4. **All `<p>` tags** get `max-width: 70ch` — this is in the global stylesheet; do not override.
5. **Two-column grids** stack at 1024px. **Everything** is single-column at 768px.

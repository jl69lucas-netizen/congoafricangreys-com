# CAG Brand Assets

Logo: Vintage Americana circular emblem — Congo African Grey parrot portrait, retro sunset stripes, gold rings, cream serif text.
Source: `c.a.gs-logo-original.png` (1024×1024 RGBA — already has transparent background outside the circular badge)

---

## Logo Files — Which to Use Where

| File | Size | Use Case |
|------|------|----------|
| `c.a.gs-logo-original.png` | 1024×1024 | Master source — do not modify |
| `logo-512.png` | 512×512 | Hero sections, large displays |
| `logo-256.png` | 256×256 | Standard web header |
| `logo-192.png` | 192×192 | PWA manifest icon (Android) |
| `logo-128.png` | 128×128 | Footer logo, small placements |
| `logo-64.png` | 64×64 | Inline / compact header |
| `favicon.ico` | 16+32+48 multi | Browser tab favicon (put in `/public/`) |
| `favicon-32.png` | 32×32 | Chrome / modern browsers |
| `favicon-16.png` | 16×16 | Legacy browser fallback |
| `apple-touch-icon.png` | 180×180 | iPhone home screen (white bg, no transparency) |
| `og-image.png` | 1200×630 | Facebook / LinkedIn / general OG preview |
| `og-twitter.png` | 800×418 | Twitter/X card preview |

All files except `apple-touch-icon.png` and OG images have transparent backgrounds.
OG images use the brand dark background (`#12100e`) with gold accents — social platforms don't support transparency.

---

## Astro Usage (copy-paste ready)

```astro
---
// In BaseLayout.astro <head>
---
<link rel="icon" type="image/x-icon" href="/favicon.ico" />
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<meta property="og:image" content="https://congoafricangreys.com/og-image.png" />
<meta name="twitter:image" content="https://congoafricangreys.com/og-twitter.png" />
<meta name="twitter:card" content="summary_large_image" />
```

Copy `favicon.ico`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png`, `og-image.png`, `og-twitter.png` into Astro's `/public/` folder.
Use `logo-256.png` or `logo-512.png` in the `<Header>` component via `<img>` or `<Image>`.

---

## Brand Colors (from logo)

| Name | Hex | Use |
|------|-----|-----|
| Logo Dark | `#12100e` | Background for OG images, dark sections |
| Gold / Tan | `#c4a05a` | Borders, accents, highlights |
| Cream | `#f5eedа` | Headings on dark backgrounds |
| Rust Red | `#b43c2d` | Accent stripe (matches Congo tail color) |
| Warm White | `#faf7f4` | Page background (design canvas bg) |

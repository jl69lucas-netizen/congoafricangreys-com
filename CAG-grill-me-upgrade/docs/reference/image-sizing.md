# CAG Image Sizing System — Option A (Fixed-Height Slots)

Approved 2026-05-30. Apply to all pages site-wide.

## The Rule
Every image type snaps to a **defined height** per device tier.  
`object-fit: cover` handles cropping. Never use `max-height` alone — use the Tailwind responsive classes below.

---

## Slot Reference

| Slot name | Use cases | Mobile | Tablet (md≥768) | Desktop (lg≥1024) | Tailwind classes |
|-----------|-----------|--------|-----------------|-------------------|-----------------|
| **Banner** | Full-width section banners (History AI, Shipping) | 220px | 300px | 420px | `h-[220px] md:h-[300px] lg:h-[420px]` |
| **Split** | SplitFeature images (Congo, Timneh, Why-Us) | 16/9 auto (component) | 16/9 auto | max-h 380px | `max-h-[380px]` on img (component-level) |
| **Inline-tall** | Health/guarantee 2-col image | 200px | 240px | 280px | `h-[200px] md:h-[240px] lg:h-[280px]` |
| **Comic-panel** | Portrait graphic (Scam comic) | 260px | 300px | 340px | Fixed wrapper `height:340px; width:min(300px,100%)` |
| **Card-thumb** | Blog card featured images | 160px | 180px | 200px | `h-[160px] md:h-[180px] lg:h-[200px]` |
| **Micro-thumb** | Eggs/pairs horizontal card | 96px | 112px | 112px | `h-24 w-24 sm:h-28 sm:w-28` |
| **Video** | Video poster / embed | 16:9 auto | 16:9 auto | 16:9 auto | `aspect-ratio: 16/9` container |

---

## Implementation Patterns

### Banner (full-width)
```html
<img src="..." alt="..."
  class="w-full rounded-2xl object-cover h-[220px] md:h-[300px] lg:h-[420px]"
  style="box-shadow: 0 8px 40px rgba(60,30,10,0.14);"
  loading="lazy" width="1200" height="675" />
```

### Inline-tall (health / 2-col beside text)
```html
<img src="..." alt="..."
  class="w-full rounded-2xl object-cover h-[200px] md:h-[240px] lg:h-[280px]"
  style="box-shadow: 0 6px 28px rgba(60,30,10,0.10);"
  loading="lazy" />
```

### Card-thumb (blog / content cards)
```html
<div class="overflow-hidden h-[160px] md:h-[180px] lg:h-[200px]">
  <img src="..." alt="..."
    class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
    loading="lazy" />
</div>
```

### Comic-panel (portrait graphic, e.g. scam-buster-comic 768×1376)
```html
<div class="overflow-hidden rounded-2xl"
  style="width:min(300px,100%); height:340px; box-shadow:0 6px 28px rgba(60,30,10,0.12);">
  <img src="..." alt="..."
    style="width:100%; height:100%; object-fit:cover; object-position:top center;"
    loading="lazy" />
</div>
```

### Micro-thumb (horizontal card, e.g. eggs/pairs)
```html
<img src="..." alt="..."
  class="h-24 w-24 sm:h-28 sm:w-28 flex-shrink-0 rounded-xl object-cover"
  loading="lazy" />
```

### Split Feature (component-level cap)
Applied inside `src/components/cag-library/SplitFeature.astro` editorial variant:
```html
<img src={imageSrc} alt=""
  class="aspect-[4/5] w-full max-h-[380px] rounded-3xl object-cover ..."
  loading="lazy" />
```
Mobile: component CSS resets to `aspect-ratio: 16/9; width: 100%` at ≤1024px.

---

## Real image dimensions on CAG (2026-05-30)

| File | Dimensions | Ratio | Assigned slot |
|------|-----------|-------|--------------|
| congo-african-grey-natural-habitat-origin.webp | 2752×1536 | 1.79 | Banner |
| african-grey-parrot-iata-shipping-crates.webp | 640×362 | 1.77 | Banner |
| congo-african-grey-variant.webp | 640×480 | 1.33 | Split |
| timneh-african-grey-variant.webp | 640×426 | 1.50 | Split |
| african-grey-head-scratch-cags-breeder.webp | 465×500 | 0.93 | Split |
| african-grey-parrot-health-review.webp | 500×375 | 1.33 | Inline-tall |
| scam-buster-comic.webp | 768×1376 | 0.56 | Comic-panel |
| african-grey-parrot-free-exploration.webp | 375×500 | 0.75 | Card-thumb |
| mix-nuts-for-african-greys.webp | 1024×681 | 1.50 | Card-thumb |
| spoonfed-african-grey-parrot-baby.webp | 640×480 | 1.33 | Card-thumb |
| first-time-african-grey-owner-review.webp | 800×600 | 1.33 | Card-thumb |
| african-grey-candled-eggs.webp | 550×688 | 0.80 | Micro-thumb |
| congo-african-grey-breeding-pair-aviary.webp | 1080×1080 | 1.00 | Micro-thumb |
| african-grey-breeder-with-bird-midland-tx.webp | 640×480 | 1.33 | Video poster |

---

## When shooting new photos

| Slot | Target shoot ratio | Min resolution |
|------|-------------------|---------------|
| Banner | 16:9 or wider | 1200×675px |
| Split | 4:5 portrait | 600×750px |
| Inline-tall | 4:3 | 560×420px |
| Card-thumb | 3:2 or 16:9 | 480×320px |
| Micro-thumb | 1:1 square | 224×224px |

---

## Notes
- Always use `loading="lazy"` on below-fold images. Use `loading="eager" fetchpriority="high"` on the hero only.
- Always include `width` and `height` attributes on `<img>` to prevent layout shift (CLS).
- WebP format for all images. Max file size: 300KB for Banner, 150KB for Card-thumb, 80KB for Micro-thumb.
- `object-position` defaults to `center`. Override to `object-position: top` for portraits where the subject is at the top (e.g. scam comic, candled eggs).

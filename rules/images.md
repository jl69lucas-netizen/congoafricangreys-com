# Image sizing, srcset and alt-text distribution

Rules moved out of `CLAUDE.md` on 2026-08-02 (Phase 4). **The rule text is verbatim.**

`enforced:` says what actually holds the rule up.
`test` — a committed check fails when the rule is broken. `judgment` — no mechanical
decision procedure exists, and `data/quality/rule-index.json` records why.
`untested` — **a deletion candidate**: it is asserted and nothing enforces it.
`scripts/quality_report.py` §5 lists every one of those on every run, which is the point.


---
id: image-keyword-distribution
enforced: untested
family: IMG
---

- **Image keyword distribution (ALWAYS — seo-rules Rule 50b)** — The page's PRIMARY keyword goes in the PRIMARY image's alt text only (hero/first content image); every other image rotates a different keyword type (secondary/LSI/NLP variation/long-tail) so the image set covers a diverse spread. No two images on a page share an alt. Applies to photos, AI-generated images, and infographics.

---
id: uniform-inbody-image-sizing
enforced: untested
family: IMG
---

- **Uniform in-body image sizing (ALWAYS — locked 2026-07-12) — applies to comparison + long-form content pages and every image agent/skill** — EVERY in-body section image, **OG photo AND infographic alike, renders in the SAME box as an infographic**: `.sec-img.inf-img` = `max-width:760px; aspect-ratio:1408/768 (16:9); object-fit:cover; height:auto`, **identical on mobile / tablet / desktop**. Do NOT give OG photos the smaller/variable boxes (`.portrait` 420px, `.portrait-tall` 340px, `.photo43` 480px) on these pages — the breeder wants every image the same rectangle down the page, matching the infographic sizing already shipped on CvT/CvM/CvC/MvF. Tune **`object-position` per OG photo** so the bird isn't cropped out of the 16:9 strip (box size never changes, only the focal point). Ship each `<100 KB WebP + -760.webp` sibling with `srcset`/`sizes` like the infographics. Hero staggered-portrait component keeps its own `.hero-imgs` sizing. **Exact pipeline (2026-07-12): `PIL.ImageOps.fit(src,(1408,768),LANCZOS,centering=per-image)` → WebP `method=6`, quality-walk 82↓ until <95 KB → `-760.webp` sibling; a low-res OG master is upscaled to the box on purpose (uniform sizing beats pixel-peeping — breeder's call).** Canonical spec: `IMAGE-DESIGNS.md §1a`. Differentiate sibling pages so they don't look identical with `skills/cag-component-refresh` (the "Refresh Agent" — layout/accent/motif deltas, never a palette change).

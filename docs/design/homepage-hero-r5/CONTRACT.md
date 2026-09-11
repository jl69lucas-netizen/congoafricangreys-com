# Homepage Hero — Round 5 (A / B / C)

**Canvas:** https://claude.ai/code/artifact/6881b0e8-6831-4f31-b1d7-5b1e329bd04d (9 artboards,
seeded from this folder: `cags-homepage-hero-round-5.html`). Re-seed after any generator change
and republish to the same URL.

Earlier rounds: 1 = A/B/C (`../homepage-variations/`), 2 = D/E/F (`../homepage-variations-r2/`),
3 = G/H/I (`../homepage-variations-r3/`). **This round covers the hero only**: three new
designs × Mobile/Tablet/Desktop = 9 artboards. The breeder asked for them on 2026-09-11 against the
live HeroV3:b (forest card on the left, circular photo on the right, ~649px tall on desktop).

## 1. Brief (restated)

- **Goal:** three new homepage heroes, A/B/C, each at 390 / 768 / 1440, shown on one canvas for
  the breeder to pick from.
- **Content:** the live HeroV3 copy word for word (eyebrow, H1, lead with the `#proof` link, both
  CTAs, four credentials, "6 Birds Available Now"). The photo is the same Midland, Texas image
  (`public/african-grey-parrot-breeder-midland-tx-hero.webp`, 800×600, "Rony & Rose / Midland, Texas"
  sign) with the live alt text.
- **Gate:** desktop hero **350–450px**, measured on the `<section>` at 1440. Compact. (The brief
  opened at 350–400; the breeder widened the ceiling to 450px mid-build on 2026-09-11, and the
  extra height went to the photo in all three.)
- **Done:** the breeder names a pick → it is written into `HeroV3.astro` / `index.astro` (visual layer
  only, no copy added or removed) → verified in a real browser at 375/768/1280 → §7 gates of
  `cag-component-variations` → commit + push (deploy) → IndexNow for `/`.
- **Out of scope:** the counter, dial, rail and every other homepage section, and any copy change.

## 2. Format

Same `.dc.html` format as rounds 1–3: `<script src="./support.js"></script>` verbatim, inline
styles, flex/grid + gap, literal copy, inline SVG icons, bare-filename image. The artboards are
**generated** by `build_artboards.mjs` in this folder (so all 9 share one set of copy strings).
Edit the generator and re-run it; never hand-edit a generated file.

## 3. Tokens and invariants

Tokens and invariants are the same as `../homepage-variations/CONTRACT.md` §3–§4. The ones this round leans on:

- Hero bed `#0f3d2c`, so the clay `#e8604c` span "Midland, Texas" reads 3.45:1 (large text, passes).
  On `#2D6A4F` it would be 1.8:1, which is why no variation puts clay text on plain forest.
- One clay CTA (`#c8472f`, white text, 50px pill). The secondary is an outlined cream pill.
- Hero/counter seam: dark → cream tone shift + a 1px `#2D6A4F` rule on the section's bottom.
- Image first on Mobile/Tablet (breeder rule from round 2).
- CITES Appendix I; no em dash in new copy (the lead's em dash is live copy and stays).

## 4. Variation axes (one structural axis each, never palette)

Layouts already used across rounds 1–3 and live (not reused here): split copy + portrait,
dark scrim 2×2 photo grid, mosaic metrics, framed portrait, lead photo + pair tiles, credential
band, marquee type bands, bird ledger, postcard overlay, and live card + circle.

| | Axis | Desktop | Tablet | Mobile |
|---|---|---|---|---|
| **A** | **Paperwork card**: copy sits straight on the scrim (no inner card); the photo is a cream *document* card that also carries the four credentials as a checklist, labelled with the live `aria-label` "Breeder credentials". Paperwork and photo are shown as one object. | copy left, card 492px right | card left (image first), copy right | card first, copy below |
| **B** | **Arch window**: a triptych. The headline is right-aligned into an aviary-arch photo that stands on the hero's bottom rule; the lead, actions and credentials sit on the far side. | 3 columns, arch 340×322 grounded | arch left, grounded | arch on a hairline "floor", centred copy |
| **C** | **Inline-photo headline**: centred and type-led. The Midland photo is a pill set *inside* the H1 line just before "Midland, Texas", so the sign in the photo and the words echo each other. Credentials and availability share one line. | pill 236×78 in a 44px H1 | pill 176×60 in a 34px H1 | stadium photo band first (image-first rule), plain H1 |

## 5. Implementation notes (for the apply step)

- **C:** the H1's accessible name must stay exactly the live string, so the photo inside the H1
  cannot carry alt text (it would be read as part of the heading). In `HeroV3.astro` the desktop/tablet
  pill is an `aria-hidden` span with `alt=""`, and the live alt text stays on the mobile stadium-band
  image, which sits outside the H1. Trade-off: at 768px and up the hero photo is decorative to screen
  readers and to image search. Noted in CRITIQUE.
- **A / B:** the image keeps `loading="eager" fetchpriority="high"` and a measured `srcsetAttrs()`
  size (A ≈ 464px, B ≈ 340px); update the homepage preload in `index.astro` (`srcsetFor(heroImg, …)`)
  in step with the new `sizes`.
- `availableCount` stays a prop; "6" on the artboards is the live value on 2026-09-11.
- **Stack (checked 2026-09-11):** Astro **6.3.1**, Tailwind **4.3** (`@tailwindcss/vite`), React 19.
  The hero image lives in `/public` with pre-built 300/600/800 widths and ships through
  `src/lib/srcset.ts` → `srcsetAttrs()`, not `astro:assets`. Keep that path for the apply step:
  the IMG family of the render harness and the homepage preload both measure against
  `srcsetAttrs()`/`srcsetFor()`, so a switch to `<Picture>` would change the preload contract as well as the hero.
  Use a plain `<img>` with `loading="eager" fetchpriority="high" decoding="async"`, explicit
  `width`/`height` (no CLS) and a `sizes` measured on the built page at 375/768/1280.
  Tailwind 4 arbitrary values (`grid-cols-[minmax(0,1fr)_492px]`, `rounded-t-[180px]`) cover every
  layout above, so no new CSS file is needed.

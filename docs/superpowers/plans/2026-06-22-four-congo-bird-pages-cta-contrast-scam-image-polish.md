# Four Congo Bird Pages — CTAs, AA Contrast, Scam Thumbnail & Image Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** On the four Congo `/available/` bird pages (Amie, Bery, Jins & Jeni, Roys), add 3 mid-page conversion CTAs each (anchored to the on-page `#reserve` form), fix the WCAG-AA contrast failures axe flagged (`text-stone-400`/`text-stone-500` on light backgrounds), swap the scam related-reading card to the real scam infographic on all four, and apply three page-specific image tweaks (Bery's Honest-questions image, Jins & Jeni's meet image size, Jins & Jeni's gallery framing).

**Architecture:** Pure presentation work on four standalone Astro pages (`src/pages/available/<slug>/index.astro`), each a self-contained ~1,500-line file using Tailwind utilities + a scoped `<style>` block. One new shared image asset (scam infographic → WebP under `public/birds/`). No content, headings, schema, section count, or word count changes — visual/asset layer only (CLAUDE.md "Same content"). The contrast fix is a scripted, four-file token swap; it runs **last** among the content edits so every other task's edit anchors use the pre-swap class strings. Work happens directly on `main` (CLAUDE.md: never feature branches). The `/available` hub (currently 404) is **explicitly out of scope** — deferred to its own plan after the two Timneh pages (Elad, Evie) per the breeder's sequencing (2026-06-22).

**Tech Stack:** Astro, Tailwind CSS, scoped `<style>` blocks, WebP via Python Pillow, `npx astro build`, `scripts/final_page_audit.py --birds`, preview server screenshots.

---

## Shared Facts (verified against the live files 2026-06-22)

- **The four pages** (all Congo): `src/pages/available/{amie,bery,jins-jeni,roys}/index.astro`. (Elad & Evie are Timneh — not in this plan.)
- **All four share an identical section taxonomy** including these IDs used below: `price-counter`, `gallery`, `documentation`, `reserve`. `#reserve` (the on-page inquiry form) exists exactly once on each page — it is the CTA jump target.
- **Existing CTA pattern** (reuse verbatim) — `bery/index.astro:690`:
  ```html
  <a href="..." class="inline-flex items-center justify-center rounded-full bg-clay px-6 py-3 font-sora text-sm font-semibold text-white transition-colors hover:bg-clay-dk" style="box-shadow:0 4px 14px rgba(232,96,76,0.25);">…→</a>
  ```
  `bg-clay` + `text-white` is correct: the global `.bg-clay` rule in `global.css` renders the AA-safe `--clay-ink #c8472f` fill (white text 4.78:1) — do not change it.
- **Bird display names** for CTA labels: Amie → `Reserve Amie →` · Bery → `Reserve Bery →` · Jins & Jeni → `Reserve Jins &amp; Jeni →` · Roys → `Reserve Roys →`.
- **Contrast guard (verified):** no `text-stone-400`/`text-stone-500` sits on a dark/green background on any of the four pages (the hero uses `text-cream`). So darkening every `text-stone-400`/`text-stone-500` → `text-stone-600` is safe everywhere. `text-stone-600` (#57534e) clears AA on both white (~7:1) and cream `#faf7f4` (~6.6:1); the flagged `stone-400` (~2.9:1 on white) and `stone-500` (~4.4:1 on cream — just under 4.5) do not.
- **`img-compact-desktop`** (`@media (min-width:768px){max-width:400px;margin:auto}`) already exists in the scoped `<style>` of amie/bery/jins-jeni (added by the 2026-06-21 plan). Roys does **not** have it and does not need it here.

---

## File Structure

- **Create (asset):** `public/birds/avoid-african-grey-parrot-scam.webp` (converted from `assets/brand/avoid-african-grey-parrot-scam.jpeg`, < 100 KB)
- **Modify:** `src/pages/available/bery/index.astro` (scam card · 3 CTAs · Honest-questions image · contrast)
- **Modify:** `src/pages/available/amie/index.astro` (scam card · 3 CTAs · contrast)
- **Modify:** `src/pages/available/roys/index.astro` (scam card · 3 CTAs · contrast)
- **Modify:** `src/pages/available/jins-jeni/index.astro` (scam card · 3 CTAs · meet-image −50% · gallery framing · contrast)
- **Memory update:** add a CTA/contrast pattern note + amend the bird-page visual-fix memory.

---

## Task 1: Convert + deploy the scam infographic as a < 100 KB WebP

**Files:**
- Source: `assets/brand/avoid-african-grey-parrot-scam.jpeg` (189 KB JPEG — too big to deploy raw, per `project_image_brand_folder` memory)
- Create: `public/birds/avoid-african-grey-parrot-scam.webp`

- [ ] **Step 1: Confirm the source exists**

Run:
```bash
cd /Users/apple/Downloads/CAG
ls -l "assets/brand/avoid-african-grey-parrot-scam.jpeg"
```
Expected: file present (~190 KB).

- [ ] **Step 2: Convert JPEG → WebP with Pillow (cwebp is not installed; Pillow is — per `reference_perf_image_tooling` memory)**

Run:
```bash
cd /Users/apple/Downloads/CAG
python3 -c "from PIL import Image; im=Image.open('assets/brand/avoid-african-grey-parrot-scam.jpeg').convert('RGB'); im.save('public/birds/avoid-african-grey-parrot-scam.webp','WEBP',quality=80,method=6)"
ls -l public/birds/avoid-african-grey-parrot-scam.webp
```
Expected: `.webp` created, size < 100 KB. If it is ≥ 100 KB, re-run the same command with `quality=72`, then `quality=65`, until < 100 KB.

- [ ] **Step 3: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add public/birds/avoid-african-grey-parrot-scam.webp
git commit -m "assets: deploy avoid-african-grey-parrot-scam infographic as <100KB webp"
```

---

## Task 2: Point every scam related-reading card at the new infographic (all 4 pages)

Each page's related-reading grid has one card object with `title: "How to Avoid African Grey Scams"`; each currently uses a different, off-topic `img`. Repoint all four to the shared scam infographic with one consistent, scam-themed alt.

**Files:** Modify all four `index.astro`.

Shared new alt (use identically on all four; 159 chars, < 190):
```
Infographic on how to avoid African Grey parrot scams — the documentation and breeder checks that separate real captive-bred birds from bait listings
```

- [ ] **Step 1: Bery — replace the scam card `img` + `imgAlt`**

Edit `src/pages/available/bery/index.astro`, replace:
```
img: "/birds/bery/bery-head-scratch.webp", imgAlt: "Bery the tame Congo African Grey enjoying a head scratch — how to identify a legitimate African Grey breeder" },
```
with:
```
img: "/birds/avoid-african-grey-parrot-scam.webp", imgAlt: "Infographic on how to avoid African Grey parrot scams — the documentation and breeder checks that separate real captive-bred birds from bait listings" },
```

- [ ] **Step 2: Amie — same swap**

Edit `src/pages/available/amie/index.astro`, replace:
```
img: "/birds/amie/amie-documentation.webp", imgAlt: "African Grey documentation set — how to avoid African Grey scams" },
```
with:
```
img: "/birds/avoid-african-grey-parrot-scam.webp", imgAlt: "Infographic on how to avoid African Grey parrot scams — the documentation and breeder checks that separate real captive-bred birds from bait listings" },
```

- [ ] **Step 3: Jins & Jeni — same swap**

Edit `src/pages/available/jins-jeni/index.astro`, replace:
```
img: "/birds/jins-jeni/jins-jeni-parents-macy-letis.webp", imgAlt: "Macy and Letis, the parent Congo African Greys behind Jins & Jeni — what a legitimate captive-bred documented lineage looks like" },
```
with:
```
img: "/birds/avoid-african-grey-parrot-scam.webp", imgAlt: "Infographic on how to avoid African Grey parrot scams — the documentation and breeder checks that separate real captive-bred birds from bait listings" },
```

- [ ] **Step 4: Roys — same swap**

Edit `src/pages/available/roys/index.astro`, replace:
```
img: "/birds/roys/roys-trust-panel.webp", imgAlt: "Trust and certification panel for Roys — how to avoid African Grey scams" },
```
with:
```
img: "/birds/avoid-african-grey-parrot-scam.webp", imgAlt: "Infographic on how to avoid African Grey parrot scams — the documentation and breeder checks that separate real captive-bred birds from bait listings" },
```

- [ ] **Step 5: Verify all four now reference the shared infographic exactly once**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni roys; do echo "$p: $(grep -c 'avoid-african-grey-parrot-scam.webp' src/pages/available/$p/index.astro)"; done
```
Expected: each prints `1`.

- [ ] **Step 6: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/{amie,bery,jins-jeni,roys}/index.astro
git commit -m "fix(birds): use scam infographic as the scam related-reading thumbnail on all 4 Congo pages"
```

---

## Task 3: Add 3 mid-page CTAs per page → on-page `#reserve` form (all 4 pages)

Insert a centered clay-pill CTA as the **last child** of three high-intent sections — `#price-counter`, `#gallery`, `#documentation` — on each page. The CTA jumps to the on-page reserve form (`href="#reserve"`). This runs **before** Task 8 (contrast), so anchor strings below use the current (pre-darkened) classes.

**Files:** Modify all four `index.astro`.

**The CTA block** (insert exactly, substituting the bird label from Shared Facts):
```html

      <div class="mt-8 text-center">
        <a href="#reserve" class="inline-flex items-center justify-center rounded-full bg-clay px-7 py-3.5 font-sora text-sm font-semibold text-white transition-colors hover:bg-clay-dk" style="box-shadow:0 4px 14px rgba(232,96,76,0.25);">Reserve Bery →</a>
      </div>
```

**Insertion rule (applies to every page/section):** each target section ends with `…</p>\n    </div>\n  </section>`. Insert the CTA block immediately **after that final `</p>`** (so it lands inside the section's inner container, before `    </div>`). The final `<p>` text is unique per section, which makes the Edit `old_string` unambiguous.

### 3a — Bery (anchors verified, fully specified)

- [ ] **Step 1: `#price-counter` CTA** — Edit `bery/index.astro`, replace:
```html
      <p class="font-sora text-stone-600 text-sm leading-relaxed">Yes. The $200 is not an extra fee — it comes straight off Bery's $1,700 price, leaving a $1,500 balance due before she travels.</p>
```
with that same line followed by the CTA block (`Reserve Bery →`).

- [ ] **Step 2: `#documentation` CTA** — Edit `bery/index.astro`, replace:
```html
      <p class="font-sora text-stone-600 text-sm leading-relaxed">Captive-bred African Greys are legal to own and transfer domestically with proper documentation under <a href="https://www.fws.gov/program/international-affairs/what-cites" target="_blank" rel="noopener noreferrer" class="text-clay-text underline">U.S. Fish &amp; Wildlife Service CITES guidance ↗</a>. Bery's paperwork meets that standard.</p>
```
with that same line followed by the CTA block (`Reserve Bery →`).

- [ ] **Step 3: `#gallery` CTA** — Edit `bery/index.astro`, replace:
```html
      <p class="font-sora text-xs text-stone-400 text-center mt-2">Click to play — Bery at mealtime. No autoplay, no sound until you press play.</p>
```
with that same line followed by the CTA block (`Reserve Bery →`).

### 3b — Amie, Jins & Jeni, Roys (read-then-edit; identical template)

For each of `amie`, `jins-jeni`, `roys` and each section `price-counter`, `gallery`, `documentation`:

- [ ] **Step 4: Locate each section's closing line**

Run (example for one page — repeat per page):
```bash
cd /Users/apple/Downloads/CAG
P=amie   # then jins-jeni, then roys
for id in price-counter gallery documentation; do
  start=$(grep -n "<section id=\"$id\"" src/pages/available/$P/index.astro | cut -d: -f1)
  end=$(awk "NR>$start && /<\/section>/{print NR; exit}" src/pages/available/$P/index.astro)
  echo "=== $P #$id closes at $end — final element: ==="
  sed -n "$((end-3)),$((end-2))p" src/pages/available/$P/index.astro
done
```

- [ ] **Step 5: Insert the CTA after each section's final `<p>`**

For each section, take the unique final `<p>…</p>` line printed in Step 4 and Edit the file to append the CTA block after it (before `    </div>`). Use the correct bird label (`Reserve Amie →`, `Reserve Jins &amp; Jeni →`, `Reserve Roys →`). If a section's last element before `</div>\n  </section>` is not a `<p>` (e.g. the gallery may close on a `</p>` caption or a `</div>` media grid), anchor on whichever unique final element Step 4 prints and insert the CTA block immediately after it.

- [ ] **Step 6: Verify each page has exactly 3 new `href="#reserve"` CTA buttons added**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni roys; do echo "$p reserve-CTA links: $(grep -c 'href="#reserve" class="inline-flex' src/pages/available/$p/index.astro)"; done
```
Expected: each prints `3`.

- [ ] **Step 7: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/{amie,bery,jins-jeni,roys}/index.astro
git commit -m "feat(birds): add 3 mid-page Reserve CTAs (price/gallery/documentation → #reserve) on all 4 Congo pages"
```

---

## Task 4: Bery — swap the Honest-questions toy image + enlarge it 15% (desktop)

The toy photo (`bery-enrichment-toy.webp`) appears in the `#decisions` "Honest questions" section (the sticky sidebar at `bery/index.astro:838`) **and again** in the `#training` section below it. Per the breeder, replace the **Honest-questions** instance with the for-sale portrait `bery-african-grey-for-sale-midland-tx.webp` (already deployed in `public/birds/bery/` by the 2026-06-21 plan) and make it ~15% larger on desktop. The training-section toy image (line ~997) stays.

**Files:** Modify `src/pages/available/bery/index.astro`.

- [ ] **Step 1: Add a dedicated +15% size class to the scoped `<style>`**

The shared `.bery-feature-img` rule (`bery/index.astro:159`) caps at `max-height: 420px !important` and is used 3×, so do not edit it. Add a one-off class **after** that line (so it wins for the element that carries both classes):
```css
    .bery-d .bery-decision-img { max-height: 485px !important; object-position: center; }
```
(485 px ≈ 420 × 1.15. `object-position: center` keeps the portrait centered rather than top-cropped.)

- [ ] **Step 2: Swap the image + class at the Honest-questions sidebar (lines ~837-843)**

Replace:
```html
          <img
            src="/birds/bery/bery-enrichment-toy.webp"
            alt="Bery exploring and foraging — a Congo African Grey needs daily enrichment and interaction"
            width="260" height="420"
            class="bery-feature-img w-full rounded-2xl shadow-md object-cover"
            loading="lazy"
          />
```
with:
```html
          <img
            src="/birds/bery/bery-african-grey-for-sale-midland-tx.webp"
            alt="Bery, a hand-fed female Congo African Grey for sale at C.A.Gs in Midland, TX — captive-bred and DNA-sexed"
            width="500" height="625"
            class="bery-decision-img w-full rounded-2xl shadow-md object-cover"
            loading="lazy"
          />
```

- [ ] **Step 3: Update the sidebar caption to match the new image** (the next line, line ~844)

Replace:
```html
          <p class="font-sora text-xs text-stone-400 mt-2 text-center">Foraging and exploring are daily requirements, not occasional treats</p>
```
with:
```html
          <p class="font-sora text-xs text-stone-400 mt-2 text-center">Bery, ready to meet the home that genuinely fits her</p>
```
(Leave `text-stone-400` here — Task 8 darkens it.)

- [ ] **Step 4: Verify the new portrait is used at most twice on the page (≤2 rule)**

Run:
```bash
cd /Users/apple/Downloads/CAG
echo "for-sale portrait uses (expect ≤2):"; grep -c "bery-african-grey-for-sale-midland-tx.webp" src/pages/available/bery/index.astro
echo "enrichment-toy uses left (expect 1 — the training section):"; grep -c "bery-enrichment-toy.webp" src/pages/available/bery/index.astro
echo "decision class applied (expect 1 img + 1 css = 2):"; grep -c "bery-decision-img" src/pages/available/bery/index.astro
```
Expected: portrait ≤ 2; enrichment-toy = 1; `bery-decision-img` = 2. If the portrait shows 3, repoint the earlier selling-point use to another distinct Bery photo (`bery-cuddly-tamed-grey-african-parrot-for-sale.webp`).

- [ ] **Step 5: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/bery/index.astro
git commit -m "fix(bery): Honest-questions section uses the for-sale portrait (dedupes the toy photo) at +15% desktop size"
```

---

## Task 5: Jins & Jeni — reduce the meet image 50% on desktop

The intro/meet image (`jins-jeni/index.astro:359`, `width="800" height="600"`, full-width) renders too large on desktop. Halve it on desktop only with the existing `img-compact-desktop` helper (already defined in this page's `<style>`), leaving mobile full-width.

**Files:** Modify `src/pages/available/jins-jeni/index.astro`.

- [ ] **Step 1: Add `img-compact-desktop` to the meet image class (line ~363)**

Replace:
```html
          class="w-full rounded-2xl border border-stone-200"
```
(the one inside the `<figure>` for `src="/birds/jins-jeni/meet-jins-jeni.webp"`, lines 357-367) with:
```html
          class="w-full img-compact-desktop rounded-2xl border border-stone-200"
```
If `w-full rounded-2xl border border-stone-200` is not unique, include the preceding `width="800" height="600"` line in the `old_string` to disambiguate.

- [ ] **Step 2: Verify**

Run:
```bash
cd /Users/apple/Downloads/CAG
sed -n '357,367p' src/pages/available/jins-jeni/index.astro | grep -n "img-compact-desktop"
```
Expected: the meet `<img>` now carries `img-compact-desktop`.

- [ ] **Step 3: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/jins-jeni/index.astro
git commit -m "fix(jins-jeni): halve the meet image on desktop only (img-compact-desktop)"
```

---

## Task 6: Jins & Jeni — show the whole bird/pair in each gallery tile

The breeder's mobile screenshot shows the gallery tiles cropping hard into the birds (a pair photo in a `aspect-[4/5]` `object-cover` tile cuts off a bird at the sides). Make the **whole** bird/pair visible and centered. Recommended approach: switch the gallery `<img>` from `object-cover` → `object-contain` and give the tile a `bg-cream` fill so the full photo sits centered with a soft warm letterbox instead of a crop. This is confirmed/tuned at the Task 7 preview gate.

**Files:** Modify `src/pages/available/jins-jeni/index.astro` (gallery section `#gallery`, tiles ~1128-1210).

- [ ] **Step 1: Make the photo tiles fit-not-crop**

For each of the 5 gallery photo tiles (the `<div class="aspect-[4/5] overflow-hidden rounded-2xl border border-stone-200 …">` wrappers and their `<img>`):
- Add `bg-cream` to the tile `<div>`'s class.
- On the tile `<img>`, change `object-cover` → `object-contain` and **remove** the per-tile `style="object-position:center 30%;"` (irrelevant under `object-contain`).

Use `replace_all` carefully — the featured tile (line ~1128) has extra `ring-2 ring-clay/30` + inline shadow, so edit it separately from the four plain tiles. Concretely:

Plain tile wrapper — replace (all occurrences):
```html
<div class="aspect-[4/5] overflow-hidden rounded-2xl border border-stone-200">
```
with:
```html
<div class="aspect-[4/5] overflow-hidden rounded-2xl border border-stone-200 bg-cream">
```

Featured tile wrapper — replace:
```html
<div class="aspect-[4/5] overflow-hidden rounded-2xl border border-stone-200 ring-2 ring-clay/30" style="box-shadow:0 4px 20px rgba(60,30,10,0.08);">
```
with:
```html
<div class="aspect-[4/5] overflow-hidden rounded-2xl border border-stone-200 ring-2 ring-clay/30 bg-cream" style="box-shadow:0 4px 20px rgba(60,30,10,0.08);">
```

Gallery `<img>` — replace (all occurrences):
```html
class="w-full h-full object-cover"
```
with:
```html
class="w-full h-full object-contain"
```
Then remove each gallery `<img>`'s `style="object-position:center 30%;"` attribute.

- [ ] **Step 2: Verify the gallery no longer crops**

Run:
```bash
cd /Users/apple/Downloads/CAG
echo "gallery object-cover left (expect 0 in #gallery):"; awk '/<section id="gallery"/{f=1} f&&/object-cover/{print NR": "$0} /<\/section>/{if(f)f=0}' src/pages/available/jins-jeni/index.astro
echo "object-contain present (expect 5):"; grep -c "object-contain" src/pages/available/jins-jeni/index.astro
```
Expected: no `object-cover` inside the gallery; `object-contain` count = 5.

- [ ] **Step 3: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/jins-jeni/index.astro
git commit -m "fix(jins-jeni): gallery tiles show whole bird/pair (object-contain on cream tile, no hard crop)"
```

> **Preview-gate note (Task 8):** if `object-contain` letterboxing looks too empty on desktop for the single-bird candids, the fallback is `object-cover` + `aspect-square` + per-tile `object-position` tuned so each bird's body is centered (the Roys pattern). Decide visually in Task 8 Step 4 and adjust before the final push.

---

## Task 7: Fix the WCAG-AA contrast failures on all four pages (scripted)

axe flagged `text-stone-400` (figcaptions, small print) and `text-stone-500` (the at-a-glance `dt` labels) as failing contrast on white/cream. Darken both to `text-stone-600` across all four files. This is the **last content edit** (so it doesn't disturb earlier anchors). The guard in Shared Facts confirms none of these sit on dark backgrounds.

**Files:** Modify all four `index.astro`.

- [ ] **Step 1: Scripted token swap across the four pages**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni roys; do
  sed -i '' 's/text-stone-400/text-stone-600/g; s/text-stone-500/text-stone-600/g' src/pages/available/$p/index.astro
done
```

- [ ] **Step 2: Verify zero `stone-400`/`stone-500` text classes remain**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni roys; do echo "$p — 400: $(grep -oc 'text-stone-400' src/pages/available/$p/index.astro)  500: $(grep -oc 'text-stone-500' src/pages/available/$p/index.astro)"; done
```
Expected: every count is `0`.

- [ ] **Step 3: Sanity-check the hero/dark areas were untouched (no accidental dark-on-dark)**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni roys; do echo "--- $p stone-600 on dark? (expect none) ---"; grep -nE 'text-stone-600' src/pages/available/$p/index.astro | grep -iE 'bg-green|bg-logo|from-green|bg-forest|text-cream|bg-black'; done
```
Expected: no output for any page.

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/{amie,bery,jins-jeni,roys}/index.astro
git commit -m "fix(birds): AA contrast — darken text-stone-400/500 to stone-600 on all 4 Congo pages"
```

---

## Task 8: Build, visual preview gate, final audit, deploy

CLAUDE.md "Preview before apply" + Confidence Gate. Do not push until visuals + audit confirm.

- [ ] **Step 1: Build**

Run:
```bash
cd /Users/apple/Downloads/CAG
npx astro build
```
Expected: build succeeds, no errors for the four pages (~107 pages total).

- [ ] **Step 2: Verify the rendered `dist/` output (per `verify_rendered_not_source` memory)**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni roys; do
  echo "--- dist/available/$p ---"
  echo "scam thumb present (expect 1): $(grep -c 'avoid-african-grey-parrot-scam.webp' dist/available/$p/index.html)"
  echo "reserve CTAs (expect ≥3): $(grep -oc 'href="#reserve" class="inline-flex' dist/available/$p/index.html)"
  echo "stone-400/500 left (expect 0): $(grep -oE 'text-stone-[45]00' dist/available/$p/index.html | wc -l | tr -d ' ')"
done
echo "jins-jeni meet image compact (expect ≥1): $(grep -c 'img-compact-desktop' dist/available/jins-jeni/index.html)"
echo "bery for-sale portrait in honest-questions (expect ≥1): $(grep -c 'bery-african-grey-for-sale-midland-tx.webp' dist/available/bery/index.html)"
```
Expected: scam thumb = 1 each; reserve CTAs ≥ 3 each; stone-400/500 = 0 each; the two image checks ≥ 1.

- [ ] **Step 3: Preview server — screenshot the changed areas at desktop + mobile**

Use `preview_start`, then for each of `/available/amie/`, `/available/bery/`, `/available/jins-jeni/`, `/available/roys/`:
- **Desktop (`preview_resize` 1280px):** screenshot the price/gallery/documentation sections — confirm the clay **Reserve [Bird] →** button renders centered at each, links to `#reserve`. Screenshot a card/figcaption area — confirm the previously-grey labels/captions are now visibly darker (readable).
- **Mobile (`preview_resize` 390px):** screenshot the scam related-reading card — confirm it shows the scam infographic. For **jins-jeni**, screenshot the gallery — confirm each tile now shows the **whole** bird/pair centered (not cropped into faces). For **bery**, screenshot the Honest-questions section — confirm it shows the for-sale portrait (not the toy) and is ~15% larger than before.

Confirm visually: (a) 3 CTAs per page, on-page jump works; (b) contrast is comfortably readable; (c) scam thumbnail correct on all 4; (d) jins-jeni gallery shows whole birds (if `object-contain` letterboxes too much, switch to the Task 6 fallback and rebuild); (e) bery Honest-questions image swapped + larger; (f) jins-jeni meet image is ~half-size on desktop, full-width on mobile.

- [ ] **Step 4: Run the bird-page final audit**

Run:
```bash
cd /Users/apple/Downloads/CAG
python3 scripts/final_page_audit.py --birds
```
Expected: PASS / PASS-WITH-WARNINGS for amie, bery, jins-jeni, roys. Triage any FAIL before deploy.

- [ ] **Step 5: Push (= deploy)**

Run:
```bash
cd /Users/apple/Downloads/CAG
git push origin main
```
Expected: push succeeds; Cloudflare Pages auto-deploys from `main`. (Per `autopush_hook_amend_diverges` memory: commit fixes as new commits — do not amend already-pushed commits.)

---

## Task 9: Memory updates

**Files:** `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/`

- [ ] **Step 1: Record the CTA + contrast pattern for bird pages**

Create `feedback_bird_page_cta_and_contrast.md` (type: feedback): bird `/available/` pages get 3 mid-page clay-pill `href="#reserve"` CTAs (after price-counter, gallery, documentation); contrast standard = `text-stone-600` for secondary captions/labels (stone-400/500 fail AA on cream); scam related-reading thumbnail = shared `/birds/avoid-african-grey-parrot-scam.webp`. Link `[[reference_aa_contrast_and_perf_fixes]]` and `[[feedback_bird_page_visual_fix_patterns]]`. Add the one-line index entry to `MEMORY.md`.

- [ ] **Step 2: Note the deferred hub**

Update `project_bird_listing_pages_gap.md` (or `project_sitewide_polish_program.md`): the `/available` hub (404) is the next build after Elad & Evie, assembled like the Roys page from all 6 birds' real images/video (breeder decision 2026-06-22). Keep the `MEMORY.md` hook in sync.

- [ ] **Step 3: No commit** (memory dir is outside the repo).

---

## Self-Review

- **Spec coverage:**
  - "/available hub is 404 — how to proceed" → answered (defer; out of scope this plan), Task 9 Step 2 records it. ✓
  - "None of these pages has buttons… choose best sections for CTAs to the on-page contact form" → Task 3 (3 CTAs/page → `#reserve`, on price/gallery/documentation). ✓
  - "Bery Honest-questions toy image → use the for-sale portrait; +15% on desktop" → Task 4. ✓
  - "scam infographic as the scam card thumbnail on all 4 pages" → Tasks 1+2. ✓
  - "jins-jeni meet-jins-jeni.webp reduce 50%" → Task 5. ✓
  - "jins-jeni gallery — birds' body whole/in the middle" → Task 6. ✓
  - "all four pages contrast (stone-400/500)" → Task 7. ✓
- **Placeholder scan:** every Edit gives exact old→new strings; Task 3b uses the repo's established read-then-edit idiom with a printed unique anchor; all verify commands have expected output. No TBDs.
- **Type/name consistency:** CTA HTML and `href="#reserve"` identical across all insertions; bird labels fixed in Shared Facts; `bery-decision-img` defined once (Task 4 Step 1) and applied once (Step 2); `img-compact-desktop` reused (already defined); scam asset path `/birds/avoid-african-grey-parrot-scam.webp` identical in Task 1 (create), Task 2 (4 references), Task 8 (verify).
- **Ordering:** content edits (Tasks 2-6) precede the scripted contrast swap (Task 7) so no anchor string is invalidated mid-plan; Task 7's only anchors are class tokens, which earlier tasks don't depend on afterward.
- **Roys in scope for the new fixes** (contrast, scam thumb, CTAs) even though it was the untouched *image-height* reference last plan — confirmed: it shares the taxonomy and the failing classes. No image-height/`img-compact-desktop` work touches Roys here. ✓

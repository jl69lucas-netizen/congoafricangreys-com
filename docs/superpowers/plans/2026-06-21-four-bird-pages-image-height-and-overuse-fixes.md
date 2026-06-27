# Four Bird Pages — Image Height, Overuse & Mobile Gallery Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** On the Amie, Bery, and Jins & Jeni `/available/` pages, fix tall/oversized images, eliminate image overuse (max one image twice per page), replace the wrong Bery video, and fix the broken mobile photo gallery — using the Roys page as the visual standard, while keeping every page compact.

**Architecture:** Pure presentation/asset work on three Astro pages plus one untouched reference (Roys). No content, headings, schema, or section count change — visual layer only (per CLAUDE.md "Same content" rule). Three kinds of change: (1) **asset deployment** — copy real Bery photos + Bery's real video from `assets/brand/BERY/` into `public/birds/bery/`; (2) **markup edits** — swap overused `src`/`poster` references for distinct images, cap tall image heights, and switch gallery tiles to the responsive Roys pattern; (3) **a small desktop-only CSS cap** for vertical infographics. Work happens directly on `main` (CLAUDE.md: never feature branches).

**Tech Stack:** Astro (`src/pages/available/<slug>/index.astro`), Tailwind utility classes, scoped `<style>` blocks, WebP images in `public/birds/<slug>/`, `npx astro build`, `scripts/final_page_audit.py --birds`.

---

## The Roys Standard (reference — do NOT edit Roys)

These are the patterns every fix below copies from `src/pages/available/roys/index.astro`. Read them once; they are the source of truth.

**A. In-body content image (the "well done" one the breeder named) — `roys/index.astro:354-364`:**
```html
<figure class="my-7">
  <img
    src="/birds/roys/roys-personality.webp"
    alt="..."
    width="760" height="430"
    class="w-full rounded-2xl border border-stone-200"
    loading="lazy"
    style="box-shadow:0 4px 20px rgba(60,30,10,0.07);"
  />
  <figcaption class="font-sora text-xs text-stone-400 mt-2 text-center">...</figcaption>
</figure>
```
Key traits: `width="760" height="430"` (landscape-ish ratio, ~430px tall), `w-full`, soft warm shadow, **no `max-height` crop, no `object-cover`**.

**B. Gallery tile (responsive, mobile-safe) — `roys/index.astro:1147-1157`:**
```html
<div class="aspect-[4/5] overflow-hidden rounded-2xl border border-stone-200 ring-2 ring-clay/30" style="box-shadow:0 4px 20px rgba(60,30,10,0.08);">
  <img src="..." alt="..." title="..." width="400" height="500"
       class="w-full h-full object-cover" loading="lazy" style="object-position:center 44%;" />
</div>
```
Key trait: tiles use `aspect-[4/5]` (ratio-based, scales down with column width on mobile) — **never `h-72`** (fixed 288px → tall narrow cards on a 2-col mobile grid, which is the reported bug).

---

## Sizing Decisions (Recommended + Why — tune visually at the preview gate in Task 9)

These three numbers drive most edits. They are recommendations, confirmed visually in Task 9 before the final commit (CLAUDE.md "Preview before apply").

1. **Tall portrait "selling-point" photo** (currently `width="760" height="950"` + `style="max-height:560px;object-fit:cover;..."`): cap to **`max-height:320px`** (≈43% shorter), keep `object-fit:cover; object-position:center` so the portrait isn't distorted, and update the intrinsic attrs to `width="760" height="430"`.
   - **Why:** A 760×950 portrait cannot use Roys' uncapped `w-full` (it would render ~950px tall — worse). Capping the height to ~320px with `object-cover` gives the same short, landscape-ish footprint as `roys-personality.webp` (~430px) while staying a real photo. Trade-off: `object-cover` crops top/bottom of the portrait; mitigated by `object-position:center`.

2. **Vertical infographics** (`*-whats-included-infographic.webp`, `amie-documentation.webp`, `*-shipping-infographic.webp`): wrap/cap at **`max-width:400px` centered on desktop (≥768px) only; full-width on mobile** via a scoped `.img-compact-desktop` class.
   - **Why:** The breeder said "reduce by 50%… desktop ONLY, good on mobile." Halving the width of a ratio-preserving image halves its rendered height — exactly a 50% desktop reduction — with zero distortion, and mobile is untouched. Trade-off: infographic is smaller/denser on desktop; acceptable since these are reference graphics, not hero art.

3. **Section padding (compactness):** standardize every `<section>` vertical padding to **`py-12`** (Amie/Bery/Jins-Jeni already mostly use `py-12`; only fix any `py-16`/`py-20` outliers). Do not touch the hero.
   - **Why:** The dominant cause of "page too long" is the tall images (fixed above); padding is the secondary lever. `py-12` matches the existing rhythm on these pages. Trade-off: marginally tighter whitespace; consistent with the live Roys/interior cadence.

---

## File Structure

- **Modify:** `src/pages/available/bery/index.astro` (heaviest — video + 9-way image dedupe + tall caps + gallery + compact)
- **Modify:** `src/pages/available/amie/index.astro` (documentation cap + tall cap + `amie-handfed` 3rd-use swap + gallery + compact)
- **Modify:** `src/pages/available/jins-jeni/index.astro` (tall cap + infographic caps + gallery + dedupe audit + compact)
- **Do NOT modify:** `src/pages/available/roys/index.astro` (the standard)
- **Create (assets):** copy 5 files from `assets/brand/BERY/` into `public/birds/bery/`
- **Memory update:** `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/feedback_bird_page_visual_fix_patterns.md` (the old "use h-72" note is now wrong — Roys' `aspect-[4/5]` is the mobile-safe standard)

---

## Task 1: Deploy Bery's real photos + real video into `public/birds/bery/`

**Files:**
- Source: `assets/brand/BERY/{bery-african-grey-for-sale-midland-tx-,bery-cuddly-tamed-grey-african-parrot-for-sale,bery-grey-african-parrot-for-sale,bery-head-stratch}.webp` + `assets/brand/BERY/bery-video-eating.mp4`
- Create: matching files under `public/birds/bery/`

- [ ] **Step 1: Confirm source files exist and are <100KB (per `project_image_brand_folder` memory)**

Run:
```bash
cd /Users/apple/Downloads/CAG
ls -l assets/brand/BERY/bery-african-grey-for-sale-midland-tx-.webp \
      assets/brand/BERY/bery-cuddly-tamed-grey-african-parrot-for-sale.webp \
      assets/brand/BERY/bery-grey-african-parrot-for-sale.webp \
      assets/brand/BERY/bery-head-stratch.webp \
      assets/brand/BERY/bery-video-eating.mp4
```
Expected: all 5 exist (webp sizes 59KB/97KB/11KB/54KB — all <100KB; mp4 ~1.3MB).

- [ ] **Step 2: Copy the 4 photos into `public/birds/bery/` with clean SEO names (drop the trailing-dash typo and the "stratch" typo; avoid clashing with the existing `bery-head-scratch.webp`)**

Run:
```bash
cd /Users/apple/Downloads/CAG
cp "assets/brand/BERY/bery-african-grey-for-sale-midland-tx-.webp" "public/birds/bery/bery-african-grey-for-sale-midland-tx.webp"
cp "assets/brand/BERY/bery-cuddly-tamed-grey-african-parrot-for-sale.webp" "public/birds/bery/bery-cuddly-tamed-grey-african-parrot-for-sale.webp"
cp "assets/brand/BERY/bery-grey-african-parrot-for-sale.webp" "public/birds/bery/bery-grey-african-parrot-for-sale.webp"
cp "assets/brand/BERY/bery-head-stratch.webp" "public/birds/bery/bery-head-tilt.webp"
```

- [ ] **Step 3: Copy Bery's REAL eating video (the current `bery-video.mp4` is byte-identical to Amie's video — confirmed via md5)**

Run:
```bash
cd /Users/apple/Downloads/CAG
cp "assets/brand/BERY/bery-video-eating.mp4" "public/birds/bery/bery-video-eating.mp4"
```

- [ ] **Step 4: Verify all 5 landed**

Run:
```bash
cd /Users/apple/Downloads/CAG
ls -l public/birds/bery/bery-african-grey-for-sale-midland-tx.webp \
      public/birds/bery/bery-cuddly-tamed-grey-african-parrot-for-sale.webp \
      public/birds/bery/bery-grey-african-parrot-for-sale.webp \
      public/birds/bery/bery-head-tilt.webp \
      public/birds/bery/bery-video-eating.mp4
```
Expected: all 5 present.

- [ ] **Step 5: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add public/birds/bery/bery-african-grey-for-sale-midland-tx.webp public/birds/bery/bery-cuddly-tamed-grey-african-parrot-for-sale.webp public/birds/bery/bery-grey-african-parrot-for-sale.webp public/birds/bery/bery-head-tilt.webp public/birds/bery/bery-video-eating.mp4
git commit -m "assets(bery): deploy 4 distinct Bery photos + real Bery eating video"
```

---

## Task 2: Bery — replace the wrong video (3 references) with Bery's real eating video

The 3 `<source src="/birds/bery/bery-video.mp4">` references (lines ~262, ~1114, ~1213) all point at Amie's video. Repoint them to `bery-video-eating.mp4` from Task 1. (Line ~396 `talking-african-grey-parrot-video.mp4` is Maxy — leave it.)

**Files:** Modify `src/pages/available/bery/index.astro`

- [ ] **Step 1: Replace all 3 video sources**

Replace every occurrence of:
```html
<source src="/birds/bery/bery-video.mp4" type="video/mp4" />
```
with:
```html
<source src="/birds/bery/bery-video-eating.mp4" type="video/mp4" />
```
(Use Edit with `replace_all: true` — all three are identical.)

- [ ] **Step 2: Verify no stale reference remains**

Run:
```bash
cd /Users/apple/Downloads/CAG
grep -n "bery-video.mp4" src/pages/available/bery/index.astro
```
Expected: **no output** (zero matches).

- [ ] **Step 3: Verify the new reference count is 3**

Run:
```bash
cd /Users/apple/Downloads/CAG
grep -c "bery-video-eating.mp4" src/pages/available/bery/index.astro
```
Expected: `3`

- [ ] **Step 4: Remove the now-orphaned wrong video file**

Run:
```bash
cd /Users/apple/Downloads/CAG
git rm public/birds/bery/bery-video.mp4
```

- [ ] **Step 5: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/bery/index.astro
git commit -m "fix(bery): use Bery's real eating video everywhere (was Amie's clip); drop wrong mp4"
```

---

## Task 3: Bery — dedupe the overused handfed photo (9 byte-identical files render as one photo 8+ times)

These `public/birds/bery/` files are all byte-identical (62377 bytes) to `bery-handfed.webp`: `bery-personality`, `bery-hero`, `bery-whats-included`, `bery-calm`, `bery-documentation`, `bery-gallery-card`, `bery-ready-for-sale`, `bery-bonding`. So every reference to any of them shows the SAME photo. Keep that photo only on the **hero cover** (`bery-hero.webp`, line ~253) and the **gallery featured card** (`bery-handfed.webp`, line ~1143) per the breeder. Repoint the rest to distinct images (deployed in Task 1 or already-distinct existing files).

**Files:** Modify `src/pages/available/bery/index.astro`

Replacement map (each new image used ≤2× across the page):

| Line | Slot | Old `src`/`poster` | New value | Reason |
|---|---|---|---|---|
| ~355 | "What is Bery like" personality figure | `/birds/bery/bery-personality.webp` | `/birds/bery/bery-cuddly-tamed-grey-african-parrot-for-sale.webp` | Expressive cuddly shot fits a personality section |
| ~452 | Selling-point figure (under $850 breakdown) | `/birds/bery/bery-handfed.webp` | `/birds/bery/bery-african-grey-for-sale-midland-tx.webp` | Distinct "for sale" portrait; trust/price context |
| ~578 | "What's included" thumbnail (pricing box) | `/birds/bery/bery-whats-included.webp` | `/birds/bery/bery-whats-included-infographic.webp` | Semantic match (the real what's-included graphic); its 2nd allowed use |
| ~835 | Enrichment/foraging sidebar | `/birds/bery/bery-handfed.webp` | `/birds/bery/bery-enrichment-toy.webp` | Already-distinct enrichment photo matches the "foraging" caption |
| ~1112 | Diet section video poster | `/birds/bery/bery-personality.webp` | `/birds/bery/bery-grey-african-parrot-for-sale.webp` | Distinct poster (new deployed photo) |
| ~1210 | Gallery video poster | `/birds/bery/bery-handfed.webp` | `/birds/bery/bery-eating.webp` | Keeps handfed to exactly the 2 named spots; eating poster fits "at mealtime" |
| ~1508 | Related-reading "Care" card img | `/birds/bery/bery-calm.webp` | `/birds/bery/bery-cuddly-tame.webp` | Distinct existing calm/bonding shot |
| ~1510 | Related-reading "Talking" card img | `/birds/bery/bery-personality.webp` | `/birds/bery/bery-head-tilt.webp` | Distinct expressive shot (new deployed photo) |

Keep unchanged: line ~17 schema `image` = `bery-hero.webp` (correct — it's the hero), line ~253 hero `poster` = `bery-hero.webp` (KEEP), line ~1143 gallery featured `src` = `bery-handfed.webp` (KEEP).

- [ ] **Step 1: Apply the 8 edits above**

For each row, Edit the exact line. The `src`/`poster` strings are unique enough per surrounding context; if a bare `src="/birds/bery/bery-handfed.webp"` is not unique, include the adjacent `alt`/`width` line in the `old_string` to disambiguate (line 452 has `width="760" height="950"`; line 835 has `width="260" height="420"`; line 1143 has the gallery `alt` "Buy Bery — a tame, hand-fed").

- [ ] **Step 2: Verify handfed photo now appears in exactly the 2 kept spots**

Run:
```bash
cd /Users/apple/Downloads/CAG
echo "handfed refs (expect 2: gallery src + nothing else):"; grep -n "bery-handfed.webp" src/pages/available/bery/index.astro
echo "hero photo refs (expect schema + hero poster = 2):"; grep -n "bery-hero.webp" src/pages/available/bery/index.astro
echo "personality dup refs (expect 0):"; grep -n "bery-personality.webp" src/pages/available/bery/index.astro
echo "calm/whats-included/documentation dup refs (expect 0):"; grep -n "bery-calm.webp\|bery-whats-included.webp\|bery-documentation.webp\|bery-ready-for-sale.webp\|bery-bonding.webp" src/pages/available/bery/index.astro
```
Expected: `bery-handfed.webp` → 1 (gallery featured `src`; the gallery video poster moved to eating); `bery-hero.webp` → 2 (schema + hero poster); all the rest → 0.

- [ ] **Step 3: Verify no image is referenced more than twice anywhere on the page**

Run:
```bash
cd /Users/apple/Downloads/CAG
grep -oE '/birds/bery/[a-z0-9-]+\.webp' src/pages/available/bery/index.astro | sort | uniq -c | sort -rn
```
Expected: top count is `2` or less for every `.webp`. If any shows `3+`, repoint the extra to an unused distinct image from `public/birds/bery/` (e.g. `bery-diet-veggies.webp`, `bery-shipping.webp`, `meet-bery.webp`, `bery-family-long-term.webp`).

- [ ] **Step 4: Delete the now-orphaned duplicate files (only if grep confirms zero references)**

Run:
```bash
cd /Users/apple/Downloads/CAG
for f in bery-personality bery-calm bery-documentation bery-whats-included bery-ready-for-sale bery-bonding bery-gallery-card; do
  if ! grep -q "/birds/bery/$f.webp" src/pages/available/bery/index.astro; then git rm "public/birds/bery/$f.webp"; else echo "STILL REFERENCED, keeping: $f"; fi
done
```
Expected: removes the unreferenced duplicates; prints "STILL REFERENCED" for none (or repoint then re-run).

- [ ] **Step 5: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add -A src/pages/available/bery/index.astro public/birds/bery/
git commit -m "fix(bery): dedupe overused handfed photo to distinct images (max 2 uses); keep on hero + gallery only"
```

---

## Task 4: Bery — cap tall images + reduce infographic on desktop only

**Files:** Modify `src/pages/available/bery/index.astro`

- [ ] **Step 1: Add the desktop-only infographic-compact class to the page's scoped `<style>` block**

Find the `<style>` block (near line ~159 where `.bery-feature-img` is defined) and add inside it:
```css
    @media (min-width: 768px) {
      .img-compact-desktop { max-width: 400px; margin-left: auto; margin-right: auto; }
    }
```

- [ ] **Step 2: Cap the tall selling-point portrait (now `bery-african-grey-for-sale-midland-tx.webp` after Task 3) — line ~452-458**

Change the `<img>` attrs/style from:
```html
          width="760" height="950"
          class="w-full rounded-2xl border border-stone-200 object-cover"
          loading="lazy"
          style="max-height:560px;object-fit:cover;object-position:center;box-shadow:0 6px 24px rgba(60,30,10,0.10);"
```
to:
```html
          width="760" height="430"
          class="w-full rounded-2xl border border-stone-200 object-cover"
          loading="lazy"
          style="max-height:320px;object-fit:cover;object-position:center;box-shadow:0 4px 20px rgba(60,30,10,0.07);"
```

- [ ] **Step 3: Reduce the "What documentation comes with Bery?" infographic 50% on desktop — line ~495-506**

Add `img-compact-desktop` to the `<img class="...">` for `bery-whats-included-infographic.webp` (line ~497). Change:
```html
          class="w-full rounded-2xl border border-stone-200 bg-white"
```
to:
```html
          class="w-full img-compact-desktop rounded-2xl border border-stone-200 bg-white"
```

- [ ] **Step 4: Apply the same desktop cap to the shipping infographic — line ~1287**

On the `<img>` for `bery-shipping-infographic.webp`, add `img-compact-desktop` to its `class`.

- [ ] **Step 5: Verify**

Run:
```bash
cd /Users/apple/Downloads/CAG
echo "no 560px cap left:"; grep -n "max-height:560px" src/pages/available/bery/index.astro
echo "compact class applied (expect >=2):"; grep -c "img-compact-desktop" src/pages/available/bery/index.astro
```
Expected: zero `max-height:560px`; `img-compact-desktop` count ≥ 2 (plus the 1 CSS definition line = grep shows ≥3 total including the `@media` rule).

- [ ] **Step 6: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/bery/index.astro
git commit -m "fix(bery): cap tall selling-point photo to 320px; halve infographics on desktop only"
```

---

## Task 5: Bery — fix mobile gallery (h-72 → aspect-[4/5], matching Roys)

**Files:** Modify `src/pages/available/bery/index.astro` (gallery section ~1139-1200)

- [ ] **Step 1: Convert the 4 plain gallery tiles**

Edit with `replace_all: true`, replacing:
```html
<div class="h-72 overflow-hidden rounded-2xl border border-stone-200">
```
with:
```html
<div class="aspect-[4/5] overflow-hidden rounded-2xl border border-stone-200">
```

- [ ] **Step 2: Convert the featured tile (has extra ring/shadow classes) — line ~1141**

Replace:
```html
<div class="h-72 overflow-hidden rounded-2xl border border-stone-200 ring-2 ring-clay/30" style="box-shadow:0 4px 20px rgba(60,30,10,0.08);">
```
with:
```html
<div class="aspect-[4/5] overflow-hidden rounded-2xl border border-stone-200 ring-2 ring-clay/30" style="box-shadow:0 4px 20px rgba(60,30,10,0.08);">
```

- [ ] **Step 3: Verify no `h-72` gallery tiles remain**

Run:
```bash
cd /Users/apple/Downloads/CAG
grep -c 'h-72 overflow-hidden' src/pages/available/bery/index.astro
```
Expected: `0`

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/bery/index.astro
git commit -m "fix(bery): mobile gallery uses responsive aspect-[4/5] tiles (Roys standard)"
```

---

## Task 6: Amie — fix documentation/tall image, the 3rd handfed use, and gallery

**Files:** Modify `src/pages/available/amie/index.astro`

- [ ] **Step 1: Add the desktop-only compact class to Amie's scoped `<style>` (near line ~159)**

```css
    @media (min-width: 768px) {
      .img-compact-desktop { max-width: 400px; margin-left: auto; margin-right: auto; }
    }
```

- [ ] **Step 2: Halve `amie-documentation.webp` on desktop only — line ~497 (the breeder's named "too tall on desktop, good on mobile" image)**

Add `img-compact-desktop` to the `<img class="...">` for `amie-documentation.webp`. Confirm the `<img>` carries `class="w-full ..."` and prepend `img-compact-desktop`:
```html
          class="w-full img-compact-desktop rounded-2xl ..."
```
(Read lines 495-506 first to get the exact current `class` string, then Edit.)

- [ ] **Step 3: Cap the tall selling-point portrait — line ~452-458**

Same as Bery Task 4 Step 2: change `width="760" height="950"` → `width="760" height="430"` and `max-height:560px` → `max-height:320px` (keep `object-fit:cover;object-position:center`).

- [ ] **Step 4: Fix `amie-handfed.webp` 3rd use (referenced 3× at lines ~452, ~842, ~1148; max is twice)**

Keep line ~452 (selling-point) and line ~1148 (gallery featured). Repoint the enrichment-sidebar use at **line ~842** to a distinct existing Amie image:
```html
            src="/birds/amie/amie-bonding.webp"
```
(Read line 842's surrounding `alt`/`width` to disambiguate the Edit.)

- [ ] **Step 5: Convert gallery tiles h-72 → aspect-[4/5]** (same two Edits as Bery Task 5 Steps 1-2, on `amie/index.astro`).

- [ ] **Step 6: Verify**

Run:
```bash
cd /Users/apple/Downloads/CAG
echo "amie-handfed uses (expect 2):"; grep -c "amie-handfed.webp" src/pages/available/amie/index.astro
echo "no 560px cap:"; grep -n "max-height:560px" src/pages/available/amie/index.astro
echo "no h-72 tiles:"; grep -c 'h-72 overflow-hidden' src/pages/available/amie/index.astro
echo "any image used >2×:"; grep -oE '/birds/amie/[a-z0-9-]+\.webp' src/pages/available/amie/index.astro | sort | uniq -c | sort -rn | head -3
```
Expected: handfed = 2; zero `max-height:560px`; zero `h-72`; top usage count ≤ 2.

- [ ] **Step 7: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/amie/index.astro
git commit -m "fix(amie): halve documentation image on desktop, cap tall photo, dedupe handfed to 2, responsive gallery"
```

---

## Task 7: Jins & Jeni — cap tall image + infographics, fix gallery, dedupe audit

**Files:** Modify `src/pages/available/jins-jeni/index.astro`

- [ ] **Step 1: Add the desktop-only compact class to the scoped `<style>` (near line ~159)** — same CSS block as Task 6 Step 1.

- [ ] **Step 2: Cap the tall portrait/pair photo — line ~457-460** — change `width="760" height="950"` → `width="760" height="430"` and `max-height:560px` → `max-height:320px` (keep `object-fit:cover;object-position:center`).

- [ ] **Step 3: Halve the two infographics on desktop only** — add `img-compact-desktop` to the `class` of the `<img>` for `jins-jeni-whats-included-infographic.webp` (line ~499) and `jins-jeni-shipping-infographic.webp` (line ~1269). Read each `<img>`'s current `class` first, then prepend `img-compact-desktop`.

- [ ] **Step 4: Convert gallery tiles h-72 → aspect-[4/5]** (same two Edits as Bery Task 5 Steps 1-2, on `jins-jeni/index.astro`).

  **Also tune per-tile framing:** the breeder's mobile screenshot shows Jins & Jeni's gallery photos cropping hard into the birds' faces (they are framed tighter than Roys' portrait shots). After switching to `aspect-[4/5]`, set a sensible per-tile `style="object-position:center NN%;"` on each gallery `<img>` (as Roys does at `roys/index.astro:1155,1167,1179,1191,1203`) so each pair photo shows the birds' bodies, not just heads. Exact percentages are confirmed at the Task 9 preview gate (default `center 30%` if unsure, then adjust per tile).

- [ ] **Step 5: Dedupe audit — ensure no image renders >2×**

Run:
```bash
cd /Users/apple/Downloads/CAG
grep -oE '/birds/jins-jeni/[a-z0-9-]+\.(webp|mp4)' src/pages/available/jins-jeni/index.astro | sort | uniq -c | sort -rn
```
Expected: every count ≤ 2. If any `.webp` shows 3+, repoint the surplus to an unused distinct file from `public/birds/jins-jeni/` (available: `jins-jeni-pair-1`, `jins-jeni-pair-2`, `jins-jeni-pair-5`, `jins-jeni-gallery-4`, `jins-jeni-diet-maintenance`). Note `jins-jeni-gallery-3.webp` and `jins-jeni-pair-3.webp` are byte-identical — count them together as the same photo (don't let the combined total exceed 2).

- [ ] **Step 6: Verify**

Run:
```bash
cd /Users/apple/Downloads/CAG
echo "no 560px cap:"; grep -n "max-height:560px" src/pages/available/jins-jeni/index.astro
echo "no h-72 tiles:"; grep -c 'h-72 overflow-hidden' src/pages/available/jins-jeni/index.astro
echo "compact class (expect >=2 img + 1 css):"; grep -c "img-compact-desktop" src/pages/available/jins-jeni/index.astro
```
Expected: zero `max-height:560px`; zero `h-72`; `img-compact-desktop` ≥ 3.

- [ ] **Step 7: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/jins-jeni/index.astro
git commit -m "fix(jins-jeni): cap tall pair photo, halve infographics on desktop, responsive gallery, dedupe images"
```

---

## Task 8: Compactness pass — normalize section padding across the three pages

**Files:** Modify `amie`, `bery`, `jins-jeni` `index.astro`

- [ ] **Step 1: Find any oversized section padding (excluding the hero)**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni; do echo "--- $p ---"; grep -n '<section[^>]*class="[^"]*py-1[6-9]\|<section[^>]*class="[^"]*py-2[0-9]' src/pages/available/$p/index.astro; done
```
Expected: lists any `py-16`/`py-20`+ sections. (The hero is a `<header>`/`<section>` with its own treatment — do NOT change it.)

- [ ] **Step 2: For each non-hero match, change `py-16`/`py-20` → `py-12`** (Edit each; keep all other classes identical). If Step 1 returns no non-hero matches, skip — the pages are already at `py-12`.

- [ ] **Step 3: Verify rhythm is consistent**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni; do echo "--- $p py-* histogram ---"; grep -oE '<section[^>]*class="[^"]*py-[0-9]+' src/pages/available/$p/index.astro | grep -oE 'py-[0-9]+' | sort | uniq -c; done
```
Expected: dominated by `py-12` (no stray `py-16`/`py-20` on body sections).

- [ ] **Step 4: Commit** (only if changes were made)

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/available/amie/index.astro src/pages/available/bery/index.astro src/pages/available/jins-jeni/index.astro
git commit -m "polish(birds): normalize body section padding to py-12 for compact pages"
```

---

## Task 9: Build, visual preview gate, and final audit

This is the CLAUDE.md "Preview before apply" + Confidence Gate step. Do not deploy until visuals are confirmed.

- [ ] **Step 1: Build**

Run:
```bash
cd /Users/apple/Downloads/CAG
npx astro build
```
Expected: build succeeds, no errors for the three pages.

- [ ] **Step 2: Verify rendered images exist in `dist/` (per `verify_rendered_not_source` memory)**

Run:
```bash
cd /Users/apple/Downloads/CAG
for p in amie bery jins-jeni; do echo "--- dist/available/$p ---"; grep -oE '/birds/'$p'/[a-z0-9-]+\.(webp|mp4)' dist/available/$p/index.html | sort | uniq -c | sort -rn | head; done
echo "bery still pointing at wrong video? (expect 0):"; grep -c "bery-video.mp4\b" dist/available/bery/index.html
```
Expected: every referenced asset count ≤ 2; the wrong `bery-video.mp4` count is 0.

- [ ] **Step 3: Start the preview server and screenshot each page at desktop + mobile widths**

Use `preview_start`, then for each of `/available/amie/`, `/available/bery/`, `/available/jins-jeni/`:
- `preview_resize` to 1280px (desktop) → `preview_screenshot` of the tall-image section, the documentation/infographic section, and the gallery.
- `preview_resize` to 390px (mobile) → `preview_screenshot` of the gallery (confirm tiles are proportional, not tall/narrow) and the infographic (confirm full-width, not shrunk).

Confirm visually: (a) tall photos are now short like `roys-personality`; (b) infographics are ~half-size on desktop, full-width on mobile; (c) gallery tiles look like Roys' on mobile — birds' bodies visible, not just faces (tune per-tile `object-position` if any tile crops too tight); (d) the Bery video shows Bery. If any sizing looks off, tune the `max-height:320px` / `max-width:400px` values (see Sizing Decisions) and rebuild.

  **Also check the gallery video frames render a poster, not a black/empty box** (the breeder's Jins & Jeni mobile screenshot showed an empty video frame). For each page, confirm the gallery `<video>` has a valid `poster` pointing at an existing webp and a `<source>` pointing at an existing mp4 in `public/birds/<slug>/`. Run: `for p in amie bery jins-jeni; do echo "--- $p ---"; grep -nE 'poster="/birds|<source src="/birds' src/pages/available/$p/index.astro; done` and verify each referenced file exists. Fix any missing poster/source (point to an existing real asset).

- [ ] **Step 4: Run the bird-page final audit**

Run:
```bash
cd /Users/apple/Downloads/CAG
python3 scripts/final_page_audit.py --birds
```
Expected: PASS (or PASS-WITH-WARNINGS) for amie, bery, jins-jeni. Triage any FAIL before deploy.

- [ ] **Step 5: Push (= deploy, per CLAUDE.md "Always commit + push after build")**

Run:
```bash
cd /Users/apple/Downloads/CAG
git push origin main
```
Expected: push succeeds; Cloudflare Pages auto-deploys from `main`.

---

## Task 10: Update stale memory note

**Files:** Modify `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/feedback_bird_page_visual_fix_patterns.md`

- [ ] **Step 1: Correct the gallery guidance**

The current note says the gallery fix is "h-72 + per-image object-position (not aspect-[4/5])". This is now reversed: `h-72` causes tall/narrow cards on mobile; **`aspect-[4/5]` (the Roys pattern) is the mobile-safe standard.** Edit the note's body to say `aspect-[4/5]` is the standard and `h-72` was the bug, keep the per-image `object-position` guidance, and keep the MEMORY.md index line's hook in sync.

- [ ] **Step 2: No commit needed** (memory dir is outside the repo).

---

## Self-Review

- **Spec coverage:**
  - "Use roys-personality as the standard for tall images on Amie/Bery/Jins-Jeni" → Tasks 4/6/7 (Roys Standard A + `max-height:320px`). ✓
  - "bery-handfed used 8+ times; keep only on hero cover + gallery card; replace rest with other Bery photos; use infographics in remaining places" → Task 3 (handfed kept at hero poster + gallery featured; others repointed; what's-included uses the infographic). ✓
  - "Bery hero + body video is not Bery; replace with bery-video-eating.mp4" → Tasks 1+2. ✓
  - "bery-whats-included-infographic too tall, reduce 50%" + "What documentation comes with Bery? reduce 50%" → Task 4 Step 3 (`img-compact-desktop`). ✓
  - "amie-documentation too tall on desktop only, good on mobile, reduce 50%" → Task 6 Step 2 (desktop-only `@media` cap). ✓
  - "all four pages: reduce tall images 50%, only use same image twice, use all images in each folder" → Tasks 3/4/6/7 (dedupe audits enforce ≤2; replacements pull from each bird's folder). ✓
  - "Bery/Jins&Jeni/Amie gallery card on mobile not good" → Tasks 5/6/7 (h-72 → aspect-[4/5]). ✓
  - "all sections compact" → Task 8 + the tall-image caps. ✓
- **Placeholder scan:** every Edit gives exact old→new strings or a read-then-edit instruction with disambiguating context; verification commands have expected output. No TBDs.
- **Type/name consistency:** class name `img-compact-desktop` is defined once per page and reused identically; new asset filenames are consistent between Task 1 (copy) and Task 3 (reference); `aspect-[4/5]` and `max-height:320px` used identically across all three pages.
- **Roys untouched:** no task edits `roys/index.astro` (reference only). ✓

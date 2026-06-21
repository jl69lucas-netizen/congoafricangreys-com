# Bird-Page Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix all outstanding issues on the four live Congo bird pages (Amie · Bery · Jins/Jeni · Roys) — gallery cropping, doc-image sizing, mobile shipping-image order, duplicate headers, title/meta entities, per-page geo links, and new image integration — before the Timneh pages.

**Architecture:** Static Astro pages at `src/pages/available/<slug>/index.astro`. Edits are visual-layer + headers + images only — no page content added/removed. Roys is the baseline (gallery + headers untouched; only gains a blog section + geo diversification). Work on `main` (CLAUDE.md: only main auto-deploys; no feature branch). "Tests" = `npx astro build`, `scripts/final_page_audit.py --birds`, live preview at the dev server, and `grep` guards.

**Tech Stack:** Astro, Tailwind utility classes, Python 3 + Pillow (WebP optimization), `scripts/final_page_audit.py`, `scripts/generate_sitemaps.py`.

**Spec:** `docs/superpowers/specs/2026-06-21-bird-pages-fixes-design.md`

**Reusable transforms (referenced by tasks):**

- **GALLERY-FIX:** in `<section id="gallery">`, for each of the 5 tiles, change the wrapper class `aspect-[4/5]` → `h-72`, keep `overflow-hidden rounded-2xl border ...`; on each `<img>` keep `class="w-full h-full object-cover"` and add a tuned `style="object-position:center NN%;"` (pick NN per image in preview so the bird is framed; featured tile keeps its ring/shadow inline style).
- **DOC-FIX:** change the documentation `<img>` class `mx-auto max-h-[170px] sm:max-h-[210px] w-auto max-w-full rounded-2xl border border-stone-200 bg-white` → `w-full rounded-2xl border border-stone-200 bg-white`, and in its `style` drop `object-position:center;` (keep `box-shadow…;object-fit:contain;`).
- **SHIP-ORDER-FIX:** inside `<section id="shipping">` only, in the `grid md:grid-cols-[1fr_260px]` block, move the image `<div>` (the `md:sticky` one) to be FIRST in source order; add `md:col-start-2 md:row-start-1` to it and `md:col-start-1 md:row-start-1` to the text `<div>`. Desktop layout unchanged; mobile shows image directly under the H2.
- **IMG-SEO:** every new/replacement image gets: SEO filename, `width`/`height`, `loading="lazy"`, `alt` ≤190 chars, `title`, a `<figcaption>` caption, and a 250-word description written into the session brief's image-SEO ledger.

---

### Task 0: Optimize + deploy new Bery & Jins/Jeni image assets

**Files:**
- Read: `assets/brand/BERY/*`, `assets/brand/JINS-JENI/*`
- Create: optimized WebP in `public/birds/bery/` and `public/birds/jins-jeni/`
- Create: `sessions/2026-06-21-bird-pages-fixes-brief.md` (image-SEO ledger)

- [ ] **Step 1: Confirm Pillow is available**

Run: `python3 -c "import PIL; print(PIL.__version__)"`
Expected: a version string (per memory, Pillow — not `sips`/`cwebp` — is the WebP tool here). If missing: `python3 -m pip install Pillow`.

- [ ] **Step 2: Optimize the large Bery assets to <100KB WebP and deploy**

Convert + resize (max width 1100px, quality stepped to land under ~100KB) into `public/birds/bery/` with SEO names:

```bash
python3 - <<'PY'
from PIL import Image, ImageSequence
import os
jobs = [
  ("assets/brand/BERY/meet-bery.webp",                 "public/birds/bery/meet-bery.webp", 1100),
  ("assets/brand/BERY/What-comes-with-bery.webp",      "public/birds/bery/bery-whats-included-infographic.webp", 1000),
  ("assets/brand/BERY/how-bery-gets-home-shipping.webp","public/birds/bery/bery-shipping-infographic.webp", 1000),
  ("assets/brand/BERY/bery-first-30-days-home.webp",   "public/birds/bery/bery-first-30-days.webp", 1000),
  ("assets/brand/BERY/mix-veggetables-for-parrot.webp","public/birds/bery/bery-diet-veggies.webp", 900),
  ("assets/brand/BERY/parrot-toy.webp",                "public/birds/bery/bery-enrichment-toy.webp", 900),
  ("assets/brand/BERY/bery-cuddly-tamed-grey-african-parrot-for-sale.webp","public/birds/bery/bery-cuddly-tame.webp", 900),
  ("assets/brand/BERY/bery-head-stratch.webp",         "public/birds/bery/bery-head-scratch.webp", 900),
  ("assets/brand/BERY/bery-eating.webp",               "public/birds/bery/bery-eating.webp", 900),
  ("assets/brand/BERY/bery-grey-african-parrot-parent-webp.webp","public/birds/bery/bery-parent.webp", 900),
]
for src,dst,w in jobs:
    im = Image.open(src).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height*w/im.width)))
    q = 82
    while True:
        im.save(dst, "WEBP", quality=q, method=6)
        if os.path.getsize(dst) <= 105_000 or q <= 45: break
        q -= 7
    print(dst, os.path.getsize(dst)//1024, "KB", "q=",q)
PY
```

Expected: each printed size ≤ ~105 KB.

- [ ] **Step 3: Optimize the large Jins/Jeni assets (incl. PNG→WebP) and deploy**

```bash
python3 - <<'PY'
from PIL import Image
import os
jobs = [
  ("assets/brand/JINS-JENI/meet-jins-jeni.webp",             "public/birds/jins-jeni/meet-jins-jeni.webp", 1100),
  ("assets/brand/JINS-JENI/what-comes-with-jins-jeni.png",   "public/birds/jins-jeni/jins-jeni-whats-included-infographic.webp", 1000),
  ("assets/brand/JINS-JENI/how-jins-jeni-travel-safely.png", "public/birds/jins-jeni/jins-jeni-shipping-infographic.webp", 1000),
  ("assets/brand/JINS-JENI/first-30-days-home-jins-jeni.webp","public/birds/jins-jeni/jins-jeni-first-30-days.webp", 1000),
  ("assets/brand/JINS-JENI/african-grey-pair-diet-maintenance.jpg","public/birds/jins-jeni/jins-jeni-diet-maintenance.webp", 900),
  ("assets/brand/JINS-JENI/Jins-jeni3.webp",                 "public/birds/jins-jeni/jins-jeni-gallery-3.webp", 900),
  ("assets/brand/JINS-JENI/jins-jeni4.jpg",                  "public/birds/jins-jeni/jins-jeni-gallery-4.webp", 900),
  ("assets/brand/JINS-JENI/Macy-letis-Jins-jeni-parent.webp","public/birds/jins-jeni/jins-jeni-parents-macy-letis.webp", 900),
]
for src,dst,w in jobs:
    im = Image.open(src).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height*w/im.width)))
    q = 82
    while True:
        im.save(dst, "WEBP", quality=q, method=6)
        if os.path.getsize(dst) <= 105_000 or q <= 45: break
        q -= 7
    print(dst, os.path.getsize(dst)//1024, "KB", "q=",q)
PY
```

Expected: each printed size ≤ ~105 KB. (Note: `jins-jeni-pair-1..5.webp` and `jins-jeni-parents-macy-letis.webp` already exist deployed; this adds the new infographics + extra gallery + diet + first-30-days. The MP4s `bery-video-eating.mp4` / `CAG1.mp4` are already represented by `bery-video.mp4` / `jins-jeni-hero.mp4` — verify in Task 3/4 whether to also deploy `CAG1.mp4` as a gallery clip; only deploy if needed and keep under a few MB.)

- [ ] **Step 4: Create the session brief + image-SEO ledger**

Create `sessions/2026-06-21-bird-pages-fixes-brief.md` with: the spec link, an `## Image-SEO ledger` section, and for every image deployed in Steps 2–3 a row with `filename · title · alt (≤190) · caption · 250-word description`. Author the 250-word descriptions here (first-person C.A.Gs voice, CITES-safe, Verified-Claim-Ledger-bounded).

- [ ] **Step 5: Verify file sizes + commit**

Run: `ls -lS public/birds/bery public/birds/jins-jeni | head -30`
Expected: no deployed image > ~110 KB.

```bash
git add public/birds/bery public/birds/jins-jeni sessions/2026-06-21-bird-pages-fixes-brief.md
git commit -m "assets(birds): optimize + deploy new Bery & Jins/Jeni images (<100KB WebP) + image-SEO ledger"
```

---

### Task 1: Roys — add blog section + geo diversification (baseline; no gallery/header changes)

**Files:**
- Modify: `src/pages/available/roys/index.astro`

- [ ] **Step 1: Add the care-guides/blog section**

Copy the "care guides & resources" section pattern from `src/pages/available/amie/index.astro` (SECTION 21b, ~line 1491) into Roys in the same position (after the second reviews block, before the marketplace section). Use Roys's own images for the blog cards (`/birds/roys/roys-personality.webp`, `/birds/roys/african-grey-parrot-veggies.webp`, `/birds/roys/roys-whats-included.webp`, etc.). Header (unique, baseline-safe): `African Grey care guides for Roys's new family`. Also add the matching nav entry + `On This Page` TOC item + `sections` array id (mirror how Amie registers `#resources`).

- [ ] **Step 2: Diversify the shipping geo links**

In Roys's `<section id="shipping">` "Do you ship to my state?" paragraph, replace the Arizona/Chicago/Colorado links with Roys's set, woven mid-sentence:
`/african-grey-parrot-for-sale-new-york/` (New York), `/african-grey-parrot-for-sale-nyc/` (NYC), `/african-grey-parrot-for-sale-ohio/` (Ohio), `/african-grey-parrot-for-sale-cleveland/` (Cleveland), `/african-grey-parrot-for-sale-arizona/` (Arizona), `/african-grey-parrot-for-sale-illinois/` (Illinois), `/african-grey-parrot-for-sale-chicago/` (Chicago), `/african-grey-parrot-for-sale-oregon/` (Oregon). (Pick 4–5 in the sentence; internal links same-tab.)

- [ ] **Step 3: Build + verify**

Run: `npx astro build 2>&1 | tail -5`
Expected: build success, no errors.
Run: `grep -o 'african-grey-parrot-for-sale-[a-z-]*' dist/available/roys/index.html | sort -u`
Expected: shows the new Roys set (new-york/ohio/oregon/etc.), not the old shared trio.

- [ ] **Step 4: Commit**

```bash
git add src/pages/available/roys/index.astro
git commit -m "build(roys): add care-guides blog section + diversify shipping geo links (NY/OH/AZ/IL/OR)"
```

---

### Task 2: Amie — gallery, doc image, shipping order, headers, title/meta, geo

**Files:**
- Modify: `src/pages/available/amie/index.astro`

- [ ] **Step 1: Heading Outline Gate**

Print Amie's full proposed H1→H6 outline (apply the new H2 set from the spec §E Amie column; keep all other headings). Confirm: all six levels present, ≥5 H5 and ≥5 H6, no skipped levels. Get approval before editing.

- [ ] **Step 2: Apply the new unique H2 headers (spec §E, Amie)**

Edit each H2 text (and its matching `nav`/`On This Page`/`sections` label where the label mirrors the H2). Headers only — body copy unchanged. Map:
- Personality → `Who is Amie? A hand-fed female Congo's temperament`
- Talking → `Can a female Congo talk? What to expect from Amie`
- Price → `Why is Amie $2,500 when "$850 Congos" exist?`
- Health → `How do we know Amie is healthy? PBFD & polyomavirus PCR`
- Decide first → `Is a 50-year African Grey commitment right for you?`
- Long-term → `What do Amie's first weeks — and next decades — look like?`
- Training → `How do you tame and train a young Congo like Amie?`
- Feeding → `What will Amie eat once she's weaned?`
- Shipping → `How will Amie travel safely to your city?`
- Care guides → `Where can you learn more before Amie comes home?`
- Marketplace → `Why buy Amie from C.A.Gs, not a marketplace listing?`

- [ ] **Step 3: GALLERY-FIX** (apply the reusable transform to Amie's 5 gallery tiles).

- [ ] **Step 4: DOC-FIX** (apply the reusable transform to `amie-documentation.webp` at line ~501).

- [ ] **Step 5: SHIP-ORDER-FIX** (apply the reusable transform inside Amie's `#shipping` section grid at ~line 1283).

- [ ] **Step 6: Geo diversification** — in Amie's shipping coverage paragraph use: `/african-grey-parrot-for-sale-texas/` (Texas), `/african-grey-parrot-for-sale-dallas/` (Dallas), `/african-grey-parrot-for-sale-florida/` (Florida), `/african-grey-parrot-for-sale-orlando/` (Orlando), `/african-grey-parrot-for-sale-georgia/` (Georgia), `/african-grey-parrot-for-sale-tennessee/` (Tennessee), `/african-grey-parrot-for-sale-virginia/` (Virginia) — 4–5 woven mid-sentence.

- [ ] **Step 7: Title/meta entity (spec §F)** — extend `const title` and meta keywords with `hand-fed female Congo`, `CITES Appendix I`, `PBFD/APV PCR` (stay ≤205 chars on title).

- [ ] **Step 8: Build + verify**

Run: `npx astro build 2>&1 | tail -5` → success.
Run: `grep -c 'aspect-\[4/5\]' src/pages/available/amie/index.astro` → expected `0`.
Run: `grep -o '<h2[^>]*>[^<]*' dist/available/amie/index.html | sed 's/<[^>]*>//g'` → confirm new unique headers, none matching Roys's generic three.
Preview (375px + desktop): gallery uncropped, doc image full-width, shipping image under H2 on mobile (not facing the map).

- [ ] **Step 9: Commit**

```bash
git add src/pages/available/amie/index.astro
git commit -m "fix(amie): unique hybrid headers, gallery sizing, full-width doc image, mobile shipping order, geo + title entities"
```

---

### Task 3: Bery — gallery, doc image (new infographic), shipping order, headers, title/meta, geo, new images

**Files:**
- Modify: `src/pages/available/bery/index.astro`

- [ ] **Step 1: Heading Outline Gate** — print Bery's full H1→H6 outline with the spec §E Bery headers; confirm six levels, ≥5 H5/H6, no skips; get approval.

- [ ] **Step 2: Apply new unique H2 headers (spec §E, Bery)** — same per-header mapping discipline as Task 2, Bery column.

- [ ] **Step 3: GALLERY-FIX** (Bery's 5 tiles). Where the new personality/eating shots improve the set, swap tile sources to `/birds/bery/bery-cuddly-tame.webp`, `/birds/bery/bery-head-scratch.webp`, `/birds/bery/bery-eating.webp` (IMG-SEO on each).

- [ ] **Step 4: DOC-FIX + correct image** — apply DOC-FIX transform AND change `src` to the new `/birds/bery/bery-whats-included-infographic.webp` (the `What-comes-with-bery.webp` infographic), with updated alt/title/caption (IMG-SEO).

- [ ] **Step 5: Integrate new infographics into their sections (IMG-SEO each):**
  - What's-included section image → `/birds/bery/bery-whats-included-infographic.webp`
  - Shipping section infographic → `/birds/bery/bery-shipping-infographic.webp`
  - Long-term / first-30-days → `/birds/bery/bery-first-30-days.webp`
  - Feeding section → `/birds/bery/bery-diet-veggies.webp`
  - Training/enrichment → `/birds/bery/bery-enrichment-toy.webp`
  - Parents → `/birds/bery/bery-parent.webp`
  - Hero/intro → `/birds/bery/meet-bery.webp` (only if it improves on current hero; keep one hero)

- [ ] **Step 6: SHIP-ORDER-FIX** inside Bery's `#shipping` grid (~line 1276).

- [ ] **Step 7: Update blog-section images** — swap the SECTION 21b card images (~lines 1499–1504) to the correct on-topic new shots (diet card → bery-diet-veggies, taming → bery-cuddly-tame, etc.).

- [ ] **Step 8: Geo diversification** — Bery set: `/african-grey-parrot-for-sale-los-angeles/`, `/african-grey-parrot-for-sale-san-diego/`, `/african-grey-parrot-for-sale-pennsylvania/`, `/african-grey-parrot-for-sale-michigan/`, `/african-grey-parrot-for-sale-washington/` — 4–5 woven mid-sentence.

- [ ] **Step 9: Title/meta entity** — extend `const title` + keywords with `best-value Congo`, `PBFD/APV PCR`, `DNA-sexed female`.

- [ ] **Step 10: Build + verify**

Run: `npx astro build 2>&1 | tail -5` → success.
Run: `grep -c 'aspect-\[4/5\]' src/pages/available/bery/index.astro` → `0`.
Run: `grep -o 'bery-[a-z0-9-]*\.webp' dist/available/bery/index.html | sort -u` → confirm new images referenced; `grep -c 'bery-documentation.webp' dist/available/bery/index.html` should be 0 in the doc figure (still allowed in blog card if intended).
Preview 375px + desktop: gallery, doc infographic full-width, shipping under H2, new images render, no broken images (check Network panel).

- [ ] **Step 11: Commit**

```bash
git add src/pages/available/bery/index.astro
git commit -m "fix(bery): unique headers, gallery sizing, new infographics + correct doc image, mobile shipping order, blog images, geo + title entities"
```

---

### Task 4: Jins/Jeni — gallery, doc image, shipping order, headers, title/meta, geo, new images

**Files:**
- Modify: `src/pages/available/jins-jeni/index.astro`

- [ ] **Step 1: Heading Outline Gate** — print Jins/Jeni full H1→H6 outline with spec §E Jins/Jeni headers; confirm six levels, ≥5 H5/H6, no skips; get approval.

- [ ] **Step 2: Apply new unique H2 headers (spec §E, Jins & Jeni column).**

- [ ] **Step 3: GALLERY-FIX** (Jins/Jeni's 5 tiles at ~lines 1122–1166). Use the pair shots `jins-jeni-pair-1..5.webp` plus new `jins-jeni-gallery-3.webp` / `jins-jeni-gallery-4.webp`; tune `object-position` per image so both birds are framed.

- [ ] **Step 4: DOC-FIX** (jins-jeni doc image at line ~502).

- [ ] **Step 5: Integrate new infographics (IMG-SEO each):**
  - What's-included → `/birds/jins-jeni/jins-jeni-whats-included-infographic.webp`
  - Shipping infographic → `/birds/jins-jeni/jins-jeni-shipping-infographic.webp`
  - Long-term / first-30-days → `/birds/jins-jeni/jins-jeni-first-30-days.webp`
  - Feeding → `/birds/jins-jeni/jins-jeni-diet-maintenance.webp`
  - Parents → `/birds/jins-jeni/jins-jeni-parents-macy-letis.webp`
  - Hero/intro → `/birds/jins-jeni/meet-jins-jeni.webp` (keep one hero)

- [ ] **Step 6: SHIP-ORDER-FIX** inside Jins/Jeni's `#shipping` grid (~line 1258).

- [ ] **Step 7: Update blog-section images** to the correct new shots.

- [ ] **Step 8: Geo diversification** — set: `/african-grey-parrot-for-sale-north-carolina/`, `/african-grey-parrot-for-sale-maryland/`, `/african-grey-parrot-for-sale-massachusetts/`, `/african-grey-parrot-for-sale-minnesota/`, `/african-grey-parrot-for-sale-wisconsin/` — 4–5 woven mid-sentence.

- [ ] **Step 9: Title/meta entity** — extend `const title` + keywords with `bonded Congo pair`, `CITES Appendix I`, `DNA-sexed pair`. (Keep the single `Product`/`AggregateOffer` — pair page; do not change schema.)

- [ ] **Step 10: Build + verify**

Run: `npx astro build 2>&1 | tail -5` → success.
Run: `grep -c 'aspect-\[4/5\]' src/pages/available/jins-jeni/index.astro` → `0`.
Run: `grep -o '<h2[^>]*>[^<]*' dist/available/jins-jeni/index.html | sed 's/<[^>]*>//g'` → unique headers.
Preview 375px + desktop: gallery (both birds framed), doc full-width, shipping under H2, new images render.

- [ ] **Step 11: Commit**

```bash
git add src/pages/available/jins-jeni/index.astro
git commit -m "fix(jins-jeni): unique headers, gallery sizing, full-width doc, new pair infographics, mobile shipping order, geo + title entities"
```

---

### Task 5: Knowledge capture — memory, skill, brief

**Files:**
- Create: `memory/feedback_bird_page_gallery_doc_shipping_patterns.md`, `memory/feedback_hybrid_header_seo.md`, `memory/feedback_bird_page_geo_diversification.md`
- Modify: `memory/MEMORY.md`, `skills/cag-bird-listing-page.md`, `sessions/2026-06-21-bird-pages-fixes-brief.md`

- [ ] **Step 1: Write memory files** (frontmatter per CLAUDE.md memory format):
  - gallery/doc/shipping fix patterns: gallery tiles use `h-72` + per-image `object-position` (NOT tall `aspect-[4/5]` with flat `object-center`); doc image is `w-full object-contain` (the `max-h-[170px]` cap is the shrink bug); shipping image must be source-first with `md:col-start-2 md:row-start-1` so it sits under the H2 on mobile instead of facing the map.
  - hybrid-header SEO: unique conversational question + keyword/entity clause used selectively; rotate stems; keyword+entity in title/meta is reinforcement not stuffing; each bird page needs its OWN header set (duplicate headers across `/available/` = duplicate-content risk).
  - geo diversification: each bird page links a DISTINCT 4–5 state/city set (real location slugs only); never the same trio on every page.

- [ ] **Step 2: Add three one-line pointers to `memory/MEMORY.md`.**

- [ ] **Step 3: Update `skills/cag-bird-listing-page.md`** — add a "Per-page differentiation" subsection covering: unique headers, gallery proportions (h-72 + per-image object-position), doc-image full-width rule, shipping mobile-order pattern, per-page geo set, IMG-SEO-per-bird.

- [ ] **Step 4: Commit**

```bash
git add memory/ skills/cag-bird-listing-page.md sessions/2026-06-21-bird-pages-fixes-brief.md
git commit -m "docs(birds): capture gallery/doc/shipping/header/geo patterns in memory + bird-listing skill"
```

---

### Task 6: Final verification + deploy

- [ ] **Step 1: Full build** — `npx astro build 2>&1 | tail -5` → success.
- [ ] **Step 2: Bird audit** — `python3 scripts/final_page_audit.py --birds` → PASS (all six heading levels, ≥5 H5/H6, no skips) for all four pages.
- [ ] **Step 3: SVG guard** — `grep -rl "&lt;svg" dist/` → empty.
- [ ] **Step 4: Duplicate-header guard** — diff the H2 sets of amie/bery/jins-jeni/roys in `dist/`; confirm the previously-shared three (feeding/shipping/care-guides) are now unique per page.
- [ ] **Step 5: Sitemaps** — `python3 scripts/generate_sitemaps.py` (no pages added/removed; run for safety).
- [ ] **Step 6: Deploy** — `git push origin main`. Then verify live 200s for the four `/available/` pages once Cloudflare finishes.

---

## Self-Review notes

- Spec coverage: A→Task 2/3/4 (GALLERY-FIX); B→Task 2/3/4 (DOC-FIX, all three have the cap); C→Task 2/3 (SHIP-ORDER-FIX) + Task 4; D→Task 1; E→Task 2/3/4 §E; F→Task 2/3/4 title/meta; G→Task 1/2/3/4 geo; H→Task 0 + integration in Task 3/4; I→Task 5.
- Roys gallery + headers intentionally untouched (baseline) — only Task 1 changes (blog + geo).
- DOC-FIX scoped to all three (Amie/Bery/Jins-Jeni) — all carry the `max-h-[170px]` cap (verified).
- 250-word image descriptions live in the session brief ledger (Task 0 Step 4), not inline in the plan.
- Heading Outline Gate is a hard step (Step 1) on every page task per CLAUDE.md.

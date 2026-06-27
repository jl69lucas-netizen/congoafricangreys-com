# /available/ Cluster — Performance, Schema, Geo-Distribution & Audit Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Clear the PageSpeed / Search Console defects on the `/available/` hub and all 6 bird pages (Roys, Bery, Amie, Elad, Evie, Jins & Jeni), distribute the site's real state/city location pages across the cluster as framed shipping-destination sections, fix the AA contrast + broken external link + Product rich-result defects, and produce a keyword/entity/voice self-audit benchmarked against live competitors.

**Architecture:** All edits go to `src/pages/available/index.astro` (hub) and `src/pages/available/<slug>/index.astro` (6 bird pages) plus shared assets in `public/`. Work happens directly on `main` (only `main` auto-deploys via GitHub Actions → Cloudflare Pages). No feature branches. Image downscaling uses Pillow (`PIL 11.3.0`, confirmed available) following the precedent set in commit `31368d7`. Verification is via `npx astro build` + grep of `dist/` + `python3 scripts/final_page_audit.py --birds` + a re-run of PageSpeed — this project verifies pages by build+audit, not unit tests.

**Tech Stack:** Astro (static), Tailwind utility classes, inline JSON-LD via `src/components/Schema.astro`, Pillow for WebP downscaling, Firecrawl MCP for competitor scraping.

**Confirmed decisions (from brainstorming, 2026-06-26):**
- **JumpRail:** REMOVE from the 6 bird pages (the hub never imported it). They already ship a top-of-page ToC (`cag-jump-nav.astro`); JumpRail's dot-rail + mobile sheet is redundant and its CSS is the render-blocking request flagged on every bird page.
- **Unused JS:** breeder disables **Cloudflare Rocket Loader** (`/70de/`) in the dashboard; we keep gtag deferred in code (already implemented — verify only).
- **Entity audit:** self-audit our pages **and** scrape top competitors for primary-keyword usage.
- **Reviews:** DO NOT fabricate or add `aggregateRating`/`review` schema. Current review setup is fine per breeder. The schema fix uses only **truthful Offer fields**.
- **Geo:** distribute ALL real state/city location pages across hub + all bird pages, grouped per page, framed as "states we ship to," distinct angle per page.
- **Scope guardrail (Q5/Q6):** airport codes / Flight-Nanny detail and local vet/licensing stay on hub/shipping/location pages — NOT pushed into individual bird listings beyond the existing shipping block.

---

## File Structure

| File | Responsibility | Touched by tasks |
|---|---|---|
| `src/pages/available/index.astro` | Hub: master shipping directory, fws link, contrast | T4, T6, T7, T9 |
| `src/pages/available/roys/index.astro` | Bird page (male Congo) | T1, T3, T5, T6, T7, T8, T9 |
| `src/pages/available/bery/index.astro` | Bird page (female Congo) | T1, T3, T5, T6, T7, T8, T9 |
| `src/pages/available/amie/index.astro` | Bird page (female Congo) | T1, T3, T5, T6, T7, T8, T9 |
| `src/pages/available/elad/index.astro` | Bird page (male Timneh) | T1, T3, T5, T6, T7, T8, T9 |
| `src/pages/available/evie/index.astro` | Bird page (female Timneh) | T1, T3, T5, T6, T7, T8, T9 |
| `src/pages/available/jins-jeni/index.astro` | Bird page (Congo pair) | T1, T3, T5, T6, T7, T8, T9 |
| `src/layouts/BaseLayout.astro` | gtag defer (verify only) | T2 |
| `public/birds/**/*.webp`, `public/*.webp` | Oversized image masters | T4 |
| `public/cag-header-logo-160.webp` (+ header markup) | Logo served at 2× | T4 |
| `docs/superpowers/sessions/2026-06-26-available-keyword-entity-audit.md` | Audit report output | T9 |

> **Note on "5 bird pages":** the brief said "all 5 bird pages" but the cluster has **6** (`amie, roys, bery, elad, evie, jins-jeni`). This plan covers all 6. If the breeder truly meant to exclude one, flag before T8.

---

## Task 1: Remove JumpRail from the 6 bird pages

**Files:**
- Modify: `src/pages/available/roys/index.astro` (import line 8; usage at line 194)
- Modify: `src/pages/available/bery/index.astro` (import line 8; usage at line 197)
- Modify: `src/pages/available/amie/index.astro` (import line 8; usage at line 196)
- Modify: `src/pages/available/elad/index.astro` (import line 8; usage at line 194)
- Modify: `src/pages/available/evie/index.astro` (import line 8; usage at line 194)
- Modify: `src/pages/available/jins-jeni/index.astro` (import line 8; usage at line 196)

> The hub (`available/index.astro`) does NOT import JumpRail — skip it.

- [ ] **Step 1: Inspect the exact JumpRail block in one file**

Run: `sed -n '194,215p' src/pages/available/roys/index.astro`
Expected: shows the `<JumpRail ... />` element with its `sections=` / `partNames=` props (a multi-line self-closing tag). Note the start line and the closing `/>` line for each file (they vary because bird pages have different section lists).

- [ ] **Step 2: Remove the import line from each of the 6 files**

For each file, delete the line:
```astro
import JumpRail from '../../../components/cag-library/JumpRail.astro';
```
Use Edit with `old_string` = that exact line (it is identical in all 6 files, so the same Edit works per-file).

- [ ] **Step 3: Remove the `<JumpRail ... />` element from each of the 6 files**

For each file, Read the lines around the usage (e.g. `sed -n '190,220p'`), then Edit out the entire `<JumpRail` … `/>` element (including any multi-line `sections={[...]}` / `partNames={{...}}` props passed inline). Leave surrounding markup intact. Do NOT remove `cag-jump-nav` / `JumpNav` — that is the ToC we are keeping.

- [ ] **Step 4: Confirm no dangling references remain**

Run: `grep -rn "JumpRail" src/pages/available/`
Expected: **no output** (zero matches across hub + all bird pages).

- [ ] **Step 5: Build and confirm JumpRail.css no longer ships on bird pages**

Run: `npx astro build`
Then: `grep -rl "JumpRail" dist/available/ ; echo "exit:$?"`
Expected: build succeeds; grep finds nothing under `dist/available/` (the render-blocking `JumpRail.*.css` is gone from bird-page `<head>`). JumpRail.css may still appear under `dist/` for the homepage/interior pages — that is correct and intended.

- [ ] **Step 6: Commit**

```bash
git add src/pages/available/
git commit -m "perf(birds): drop redundant JumpRail from 6 /available/ pages (kills render-blocking JumpRail.css)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 2: Verify gtag is optimally deferred (no code change expected)

**Files:**
- Inspect: `src/layouts/BaseLayout.astro:24-52`

This task confirms the GTM "unused JavaScript ~110 KiB" flag is already mitigated in code and that the remaining JS win is Rocket Loader (a dashboard toggle the breeder owns).

- [ ] **Step 1: Read the gtag loader block**

Run: `sed -n '24,52p' src/layouts/BaseLayout.astro`
Expected: gtag.js is created dynamically and appended only on first interaction (`scroll/mousemove/touchstart/keydown/pointerdown`, `{ once: true }`) with a `setTimeout(loadGA, 12000)` fallback. This is already correct — gtag does not block initial render.

- [ ] **Step 2: Record the Rocket Loader action item (no code)**

The `/70de/` script in PageSpeed is **Cloudflare Rocket Loader** (per memory `apply_model_tiers`/perf notes). It cannot be disabled from this repo. Add this to the plan's hand-back to the breeder verbatim:

> **Breeder action (Cloudflare dashboard):** congoafricangreys.com → **Speed → Optimization → Content Optimization** → turn **Rocket Loader = OFF**. This removes the `/70de/` script, its ~71 KiB unused JS, and the forced-reflow long main-thread tasks (248 ms) flagged on every page. No deploy needed; it applies at the edge.

- [ ] **Step 3: No commit** (verification + breeder hand-off only).

---

## Task 3: Fix LCP on the 4 video-hero bird pages

**Files:**
- Modify: `src/pages/available/roys/index.astro` (video poster `/birds/roys/roys-hero.webp`, ~line 269)
- Modify: `src/pages/available/bery/index.astro` (video poster `/birds/bery/bery-hero.webp`)
- Modify: `src/pages/available/amie/index.astro` (video poster `/birds/amie/amie-hero.webp`)
- Modify: `src/pages/available/jins-jeni/index.astro` (video poster `/birds/jins-jeni/jins-jeni-pair-1.webp`)

> Evie and Elad use an eager `<img>` hero with `fetchpriority="high"` already — their LCP discovery is fine; only their image *size* is addressed in Task 4.

The 4 video heroes are the LCP element but the poster image is not preload-discoverable (PageSpeed: "LCP resources should not use loading=lazy / fetchpriority=high should be applied"). A `<video poster>` cannot take `fetchpriority`, so we preload the poster image in `<head>` via the page's existing head-injection path.

- [ ] **Step 1: Find how each bird page injects head/preload tags**

Run: `grep -n "preload\|rel=\"preload\"\|<Fragment slot\|head" src/pages/available/roys/index.astro | head`
Expected: identifies whether the page passes head content to BaseLayout (e.g. a `headExtra` prop or a `<Fragment slot="head">`). If none exists, check BaseLayout for a named slot: `grep -n "slot=\|<slot" src/layouts/BaseLayout.astro`.

- [ ] **Step 2: Add a poster preload for each video-hero page**

If BaseLayout exposes a head slot, add (per page, with that page's poster path):
```astro
<link slot="head" rel="preload" as="image" href="/birds/roys/roys-hero.webp" fetchpriority="high" />
```
If BaseLayout has no head slot, add a `headPreload` prop pattern: pass `heroPreload="/birds/roys/roys-hero.webp"` from the page and, in `BaseLayout.astro` `<head>`, render `{heroPreload && <link rel="preload" as="image" href={heroPreload} fetchpriority="high" />}`. Implement the prop once in BaseLayout, then set it on the 4 video-hero pages (and optionally Evie/Elad pointing at their `<img>` hero).

- [ ] **Step 3: Build and verify the preload is in the rendered head**

Run: `npx astro build && grep -o 'rel="preload" as="image"[^>]*roys-hero[^>]*' dist/available/roys/index.html`
Expected: prints the preload link with `fetchpriority="high"` for the poster.

- [ ] **Step 4: Commit**

```bash
git add src/pages/available/ src/layouts/BaseLayout.astro
git commit -m "perf(birds): preload video-hero posters with fetchpriority=high for LCP

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 4: Downscale oversized images to ~2× displayed size

**Files:**
- Modify (in place): the oversized WebPs below in `public/`
- Modify: header logo reference (serve `cag-header-logo-160.webp` at its 80×80 display, or swap to an 80px master)
- Create: `scripts/downscale_available_images.py` (one-shot, follows commit `31368d7` precedent)

Confirmed oversized masters (current px → target ≈ 2× CSS display):

| File | Current | Displayed | Target width |
|---|---|---|---|
| `public/birds/roys/roys-hero.webp` | 1536×1024 (198 KB) | ≤556 | 1112 |
| `public/birds/bery/bery-hero.webp` | 960×960 (60 KB) | 380 | 760 |
| `public/birds/amie/amie-hero.webp` | 1024×681 (68 KB) | 380 | 760 |
| `public/birds/amie/amie-personality.webp` | 760×760 (68 KB) | 378 | 760 (keep, re-encode) |
| `public/birds/roys/roys-personality.webp` | 768×512 (48 KB) | 378 | 760 |
| `public/birds/elad/elad-at-a-glance-card.webp` | 768×1376 (66 KB) | 289 | 600 |
| `public/birds/elad/elad-personality-profile.webp` | 1200×746 | 766 | 1100 |
| `public/birds/jins-jeni/meet-jins-jeni.webp` | 768×1376 (90 KB) | 398 | 800 |
| `public/birds/jins-jeni/jins-jeni-pair-1.webp` | 800×600 | 380 | 760 |
| `public/birds/jins-jeni/jins-jeni-pair-5.webp` | (poster) | 380 | 760 |
| `public/birds/bery/bery-hero.webp` (poster) | see above | — | — |
| `public/african-grey-breeder-with-bird-midland-tx.webp` (Maxy poster, all pages) | 640×360 | 378 | 760 |
| `public/roys-congo-african-grey-male-4-months.webp` (hub card) | 800×661 | 349 | 760 |
| `public/bery-congo-african-grey-female-1-year.webp` (hub card) | 960×794 | 349 | 760 |
| `public/birds/amie/amie-handfed.webp` (hub card) | 582×480 | 384 | 768 (keep, re-encode) |
| `public/hero-available-african-greys-for-sale.webp` (hub hero) | 1376×768 (116 KB) | full-bleed | re-encode quality only (savings 14 KB) |

- [ ] **Step 1: Write the downscale script**

Create `scripts/downscale_available_images.py`:
```python
#!/usr/bin/env python3
"""One-shot: downscale oversized /available/ cluster WebPs to ~2x their CSS display
size. Mirrors commit 31368d7. Only shrinks (never upscales); re-encodes WebP q=80.
Run from repo root: python3 scripts/downscale_available_images.py"""
import os
from PIL import Image

# (path, target_width)  — height auto from aspect ratio. None = re-encode only.
JOBS = [
    ("public/birds/roys/roys-hero.webp", 1112),
    ("public/birds/bery/bery-hero.webp", 760),
    ("public/birds/amie/amie-hero.webp", 760),
    ("public/birds/amie/amie-personality.webp", 760),
    ("public/birds/roys/roys-personality.webp", 760),
    ("public/birds/elad/elad-at-a-glance-card.webp", 600),
    ("public/birds/elad/elad-personality-profile.webp", 1100),
    ("public/birds/jins-jeni/meet-jins-jeni.webp", 800),
    ("public/birds/jins-jeni/jins-jeni-pair-1.webp", 760),
    ("public/birds/jins-jeni/jins-jeni-pair-5.webp", 760),
    ("public/african-grey-breeder-with-bird-midland-tx.webp", 760),
    ("public/roys-congo-african-grey-male-4-months.webp", 760),
    ("public/bery-congo-african-grey-female-1-year.webp", 760),
    ("public/birds/amie/amie-handfed.webp", 768),
    ("public/hero-available-african-greys-for-sale.webp", None),
]

for path, target_w in JOBS:
    if not os.path.exists(path):
        print(f"SKIP missing {path}")
        continue
    im = Image.open(path)
    w0, h0, kb0 = im.width, im.height, os.path.getsize(path) // 1024
    if target_w and im.width > target_w:
        new_h = round(im.height * target_w / im.width)
        im = im.resize((target_w, new_h), Image.LANCZOS)
    im.save(path, "WEBP", quality=80, method=6)
    kb1 = os.path.getsize(path) // 1024
    print(f"{path}: {w0}x{h0} {kb0}KB -> {im.width}x{im.height} {kb1}KB")
```

- [ ] **Step 2: Run the script**

Run: `python3 scripts/downscale_available_images.py`
Expected: each line prints a shrink (e.g. `roys-hero.webp: 1536x1024 198KB -> 1112x741 ~55KB`). No "SKIP missing" lines for the bird-image paths; if any path is missing, stop and re-check the path before continuing.

- [ ] **Step 3: Update the `width`/`height` attributes that no longer match**

For any image whose intrinsic size changed AND whose markup hard-codes the old `width`/`height` (grep each), update the attributes to the new intrinsic dimensions to avoid CLS. Run per file, e.g.:
`grep -n 'roys-hero.webp' src/pages/available/roys/index.astro` then Edit the `width="640" height="640"` on the `<video>` to match the new poster aspect if it changed (the video element keeps its own `width/height` for layout — only change if the poster's aspect ratio changed; the downscale preserves aspect, so usually no change needed).

- [ ] **Step 4: Fix the header logo over-delivery (served 160px, displayed 80px)**

In the shared header (`grep -rln 'cag-header-logo-160.webp' src/components src/layouts`), the logo is `width="80" height="80"` but the file is 160×160. Keep the 160 file for retina but stop the "larger than needed" flag by serving an explicitly sized source set, OR create an 80px master:
```bash
python3 - <<'PY'
from PIL import Image
im = Image.open("public/cag-header-logo-160.webp").resize((160,160), Image.LANCZOS)
im.save("public/cag-header-logo-160.webp","WEBP",quality=82,method=6)  # re-encode tighter
PY
```
This is a 5 KB asset on every page; re-encoding to a tighter WebP clears most of the 4.6 KB flag without changing markup. (A full `srcset` is optional — note as a low-priority follow-up if PageSpeed still flags it.)

- [ ] **Step 5: Build and spot-check the largest image shrank in `dist/`**

Run: `npx astro build && ls -la dist/birds/roys/roys-hero.webp`
Expected: file size well under 198 KB (target ≈ 50–60 KB).

- [ ] **Step 6: Commit**

```bash
git add scripts/downscale_available_images.py public/birds public/*.webp src/components src/layouts
git commit -m "perf(images): downscale oversized /available/ cluster WebPs + tighten header logo

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 5: Fix AA contrast — clay text on near-black (`text-gold` on `bg-logo-dark`)

**Files:**
- Modify: `src/pages/available/index.astro` (2 occurrences), `roys` (3), `bery` (3), `amie` (3), `elad` (3), `evie` (3), `jins-jeni` (4)

Context: `--color-gold = #e8604c` on `--color-logo-dark = #12100e`. At full opacity #e8604c clears ~4.9:1, but the `/90` opacity blend (and the small `text-xs`/italic uses) drops below the 4.5:1 small-text AA floor — PageSpeed flagged the jins-jeni `text-gold/90` italic and its hero `<section>`. Fix: standardize clay-on-dark in this cluster to the established lighter clay `#f08070` (memory `aa_contrast_and_perf_fixes` — clay-on-dark-tint = `#f08070`, ≈6:1 on `#12100e`), and drop opacity modifiers.

- [ ] **Step 1: Enumerate every `text-gold` on a dark band in the cluster**

Run: `grep -rn "text-gold" src/pages/available/index.astro src/pages/available/*/index.astro`
Expected: ~21 hits. Confirm each is inside a `bg-logo-dark` / dark hero / dark info-card context (the "At a glance" eyebrow, the hero eyebrow, the jins-jeni italic tagline, the shipping-card "Nationwide shipping" label). Note any `text-gold` that is NOT on dark (unlikely here) and leave those alone.

- [ ] **Step 2: Replace `text-gold/90` and `text-gold` (on dark) with `text-[#f08070]`**

In `jins-jeni/index.astro` line ~215: `text-gold/90` → `text-[#f08070]`.
For the eyebrows/labels (`text-gold`) on dark across all 7 files, replace `text-gold` → `text-[#f08070]`. Use Edit per occurrence (the class strings differ by surrounding utilities, so target each `class="..."` uniquely or use `replace_all` only where the full token `text-gold"` is unambiguous within a file). Verify you are not changing `--color-gold` the token, only the utility usages in these 7 pages.

- [ ] **Step 3: Build and confirm no `text-gold` (or `/90`) remains on dark in the cluster**

Run: `npx astro build && grep -rn "text-gold" dist/available/ | head`
Expected: no `text-gold` in the cluster's dist output (all became `text-[#f08070]`, which Tailwind emits as a color value).

- [ ] **Step 4: Verify the contrast ratio mechanically**

Run:
```bash
python3 - <<'PY'
def lin(c):
    c/=255; return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
def L(hex):
    r,g,b=int(hex[1:3],16),int(hex[3:5],16),int(hex[5:7],16)
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def ratio(a,b):
    la,lb=L(a),L(b); hi,lo=max(la,lb),min(la,lb); return (hi+0.05)/(lo+0.05)
print("f08070 on 12100e:", round(ratio("#f08070","#12100e"),2))
PY
```
Expected: ratio ≥ 4.5 (prints ~6.x). If < 4.5, lighten further (e.g. `#f4a092`) and re-run.

- [ ] **Step 5: Commit**

```bash
git add src/pages/available/
git commit -m "a11y(birds): fix clay-on-dark AA contrast (#e8604c/.90 -> #f08070) across /available/ cluster

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 6: Replace the broken fws.gov CITES link (404) across all 9 files

**Files:**
- Modify: `src/pages/available/index.astro:363`, `roys:565`, `bery:568`, `amie:567`, `evie:566`, `elad:574`, `jins-jeni:569`
- Modify: `src/pages/how-to-avoid-african-grey-parrot-scams/index.astro`, `src/pages/cites-african-grey-documentation/index.astro` (same dead URL appears there too)

Broken: `https://www.fws.gov/program/international-affairs/what-cites` (Search Console: 404). **Constraint:** both `fws.gov` and `cites.org` return 403 to curl AND WebFetch (bot-blocked) — automated 200-checking is impossible. Verification must be a real browser.

- [ ] **Step 1: Find every occurrence of the dead URL**

Run: `grep -rn "international-affairs/what-cites" src/`
Expected: 9 files (7 in `available/` + scams + cites-doc page).

- [ ] **Step 2: Replace with the recommended live FWS CITES URL**

Replace all occurrences of
`https://www.fws.gov/program/international-affairs/what-cites`
with
`https://www.fws.gov/international-affairs/cites`
Run: `grep -rln "international-affairs/what-cites" src/` and Edit each file (the anchor text "U.S. Fish & Wildlife Service CITES guidance ↗" stays).

- [ ] **Step 3: Browser-verify the replacement returns 200 (cannot be automated)**

**Breeder/operator action:** open `https://www.fws.gov/international-affairs/cites` in a normal browser. If it loads (200), proceed. If it 404s, fall back to `https://cites.org` (CITES homepage, stable) and re-run the replacement. Record the verified URL in the commit message. *(This is the one step a bot cannot complete — fws.gov blocks all automated agents.)*

- [ ] **Step 4: Confirm no dead URL remains**

Run: `grep -rn "international-affairs/what-cites" src/ ; echo "exit:$?"`
Expected: no matches.

- [ ] **Step 5: Build + commit**

```bash
npx astro build
git add src/pages/
git commit -m "fix(links): replace 404 fws.gov/what-cites with live FWS CITES URL (9 files)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 7: Fix the Product rich-result defects (truthful Offer fields only — NO fabricated reviews)

**Files:**
- Modify: `productSchema` object near the top of each of the 6 bird pages (`roys:15-32` and equivalent blocks in bery/amie/elad/evie/jins-jeni)
- Reference: `data/financial-entities.json` (`delivery_options`), `data/price-matrix.json` for shipping figures; the health-guarantee page for the return window

Search Console: "6 invalid items — 1 critical + 4 non-critical." The 4 non-critical are the optional `review` / `aggregateRating` warnings — **we leave those absent** (breeder: do not fabricate reviews). The single **critical** field is cut off in the report; the likely culprits for a `Product`+`Offer` merchant listing are a missing `priceValidUntil`, `hasMerchantReturnPolicy`, or `shippingDetails`. We add the truthful ones, which both clear the warnings and most likely clear the critical error.

- [ ] **Step 1: Capture the EXACT critical field (must do before editing)**

Open the live Rich Results Test in a browser for one bird URL: `https://search.google.com/test/rich-results?url=https://congoafricangreys.com/available/roys/`. Record the exact critical error string. (If the breeder prefers, paste the page's JSON-LD into the schema.org validator.) This confirms which field is critical rather than guessing. *(Google's tester also blocks automated fetch — a human runs it.)*

- [ ] **Step 2: Add truthful Offer fields to each bird page's `productSchema.offers`**

For each bird page, extend the existing `offers` object (do NOT add `review`/`aggregateRating`). Example for Roys (`src/pages/available/roys/index.astro`):
```js
  "offers": {
    "@type": "Offer",
    "price": "2300",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "url": "https://congoafricangreys.com/available/roys/",
    "priceValidUntil": "2026-12-31",
    "seller": { "@type": "Organization", "name": "C.A.Gs – Midland, TX" },
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingRate": { "@type": "MonetaryAmount", "value": "185", "currency": "USD" },
      "shippingDestination": { "@type": "DefinedRegion", "addressCountry": "US" }
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": "US",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 3,
      "returnMethod": "https://schema.org/ReturnByMail",
      "returnFees": "https://schema.org/ReturnShippingFees"
    }
  }
```
Adjust `price`, `url`, and `merchantReturnDays` per the real health-guarantee window (confirm the day count against `/african-grey-parrot-health-guarantee/` — use the real figure; if it is 48 hours, use `1`; do not invent a window). Repeat for all 6 pages with each bird's real price.

- [ ] **Step 3: Build and validate the JSON-LD parses**

Run:
```bash
npx astro build
python3 - <<'PY'
import re, json, glob
for f in glob.glob("dist/available/*/index.html"):
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', open(f).read(), re.S)
    for b in blocks:
        json.loads(b)  # raises if malformed
    print("OK", f)
PY
```
Expected: `OK` for every bird page; no JSON parse exception. Confirm `hasMerchantReturnPolicy` and `shippingDetails` appear in `dist/available/roys/index.html`.

- [ ] **Step 4: Re-run the Rich Results Test (human) to confirm 0 critical**

Re-test `https://congoafricangreys.com/available/roys/` after deploy (T10). Expected: the critical issue is gone; the only remaining items are the optional `review`/`aggregateRating` notices, which are acceptable per the no-fabrication decision.

- [ ] **Step 5: Commit**

```bash
git add src/pages/available/
git commit -m "fix(schema): add truthful Offer shipping/return/priceValidUntil to 6 bird pages (clears Product critical; no fabricated reviews)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 8: Distribute all real state/city pages across hub + 6 bird pages (framed, distinct angles)

**Files:**
- Modify: the "Do you ship to my state?" block in each bird page (`roys:1342-1343` and equivalents) + the hub shipping block (`available/index.astro:473`)

The site has these **real** geo location slugs (verified on disk — link only these, never invent a slug):

States: `-arizona -colorado -florida -georgia -illinois -indiana -iowa -kentucky -maryland -massachusetts -michigan -minnesota -missouri -new-jersey -new-york -north-carolina -ohio -oregon -pennsylvania -tennessee -texas -virginia -washington -wisconsin` (all prefixed `african-grey-parrot-for-sale`)
Cities: `-austin -bay-area -chicago -cleveland -columbus -dallas -houston -jacksonville -los-angeles -miami -nyc -orlando -sacramento -san-diego -tampa`
Other: `african-grey-parrot-for-sale-near-me`, `buy-intelligent-african-grey-for-sale-ca` (California legacy)

**Distribution (grouped by region, one primary home per slug, distinct angle per page):**

| Page | Angle / framing | State/city slugs to link |
|---|---|---|
| **Hub** (`available/`) | "Our nationwide shipping network — every region" | a broad cross-region directory: florida, texas, new-york, california(ca), illinois, georgia, ohio, washington, near-me (8–9 anchors) |
| **Roys** (W/Mountain) | "West Coast & Mountain families" | bay-area, los-angeles, san-diego, sacramento, oregon, washington, colorado, arizona |
| **Bery** (Southeast) | "Southeast homes" | florida, miami, orlando, tampa, jacksonville, georgia, tennessee, north-carolina, kentucky |
| **Amie** (Midwest) | "Midwest families" | illinois, chicago, ohio, columbus, cleveland, michigan, indiana, iowa, wisconsin, minnesota, missouri |
| **Elad** (NE/Mid-Atlantic) | "Northeast & Mid-Atlantic" | new-york, nyc, new-jersey, pennsylvania, maryland, massachusetts, virginia |
| **Evie** (TX/South-Central) | "Texas & nearby — closest to our Midland aviary" | texas, dallas, houston, austin, near-me |
| **Jins & Jeni** (pair) | "Pairs placed coast to coast" | one per region: california(ca), florida, new-york, illinois, texas |

Overlap is intentional only where a hub vs bird-page link reinforces a flagship market (FL, TX, NY) — each slug still has a single primary bird-page home.

- [x] **Step 1: Read the current shipping/"ship to my state" block in one bird page**

Run: `sed -n '1315,1356p' src/pages/available/roys/index.astro`
Expected: shows the existing `<h3>Do you ship to my state?</h3>` paragraph with 5 inline state links. This is the block to rewrite per page.

- [x] **Step 2: Rewrite Roys' geo block with the West/Mountain set + distinct angle**

Replace the `Do you ship to my state?` paragraph in `roys/index.astro` with a framed shipping-destinations block. Every `href` must be a real slug from the table; anchor text = human place name; internal links open same-tab (no `target="_blank"`); first-person voice. Example:
```html
<h3 class="font-lora font-semibold text-xl text-logo-dark mb-2">Where do we ship Roys?</h3>
<p class="font-sora text-stone-600 text-sm leading-relaxed mb-3">Roys is an energetic West-Coast-ready boy — we regularly fly young greys to families across the western states. We ship him to the
<a href="/african-grey-parrot-for-sale-bay-area/" class="text-clay-text underline">Bay Area</a>,
<a href="/african-grey-parrot-for-sale-los-angeles/" class="text-clay-text underline">Los Angeles</a>,
<a href="/african-grey-parrot-for-sale-san-diego/" class="text-clay-text underline">San Diego</a>,
<a href="/african-grey-parrot-for-sale-sacramento/" class="text-clay-text underline">Sacramento</a>,
<a href="/african-grey-parrot-for-sale-oregon/" class="text-clay-text underline">Oregon</a>,
<a href="/african-grey-parrot-for-sale-washington/" class="text-clay-text underline">Washington</a>,
<a href="/african-grey-parrot-for-sale-colorado/" class="text-clay-text underline">Colorado</a>, and
<a href="/african-grey-parrot-for-sale-arizona/" class="text-clay-text underline">Arizona</a>.
Anywhere else in the 50 states, just ask — we ship everywhere.</p>
```

- [x] **Step 3: Repeat for the other 5 bird pages with their region set + a DIFFERENT opening angle**

Use a distinct lead sentence per page (no copy-paste of Roys' wording — duplicate-content risk; see memory `hybrid_header_seo`). Suggested angles:
- **Bery:** "Bery is a gentle Southern girl — these are the Southeast homes we fly greys to most:" + Southeast set.
- **Amie:** "Amie has gone home with families all across the Midwest — here's where we ship her:" + Midwest set.
- **Elad:** "Elad, our Timneh boy, ships up and down the Northeast corridor:" + NE/Mid-Atlantic set.
- **Evie:** "Evie is closest to home — Texas families are a short hop from our Midland aviary:" + TX set + near-me.
- **Jins & Jeni:** "We've placed bonded pairs coast to coast — a few of the regions we ship to:" + one-per-region set.

- [x] **Step 4: Update the hub's "where do we ship" block into a master directory**

In `available/index.astro` (~line 473), expand the 3-state sentence into the 8–9-anchor cross-region directory from the table, framed as "Our nationwide network." Keep it one paragraph, all real slugs.

- [x] **Step 5: Verify every geo href resolves to a real page on disk**

Run:
```bash
for slug in $(grep -rho 'href="/[a-z-]*for-sale[a-z-]*/"' src/pages/available/ | sed 's/href="\///;s/"//' | sort -u); do
  test -d "src/pages/${slug%/}" && echo "OK  $slug" || echo "MISSING  $slug"
done
```
Expected: every line `OK`. Any `MISSING` = a bad/invented slug — fix before building. (Note: `buy-intelligent-african-grey-for-sale-ca` is the California slug; ensure that exact slug is used, not `african-grey-parrot-for-sale-california` which does not exist.)

- [x] **Step 6: Build + commit**

```bash
npx astro build
git add src/pages/available/
git commit -m "seo(birds): distribute real state/city pages across hub + 6 bird pages as framed shipping destinations (distinct angle each)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 9: Keyword / entity / voice self-audit + competitor benchmark

**Files:**
- Create: `docs/superpowers/sessions/2026-06-26-available-keyword-entity-audit.md`

Answers the breeder's question: did entity coverage / non-commodity / humour / voice passes hold on the hub + bird pages, and how do our primary-keyword counts compare to competitors?

- [x] **Step 1: Count our own primary-keyword + variation density per page**

Run:
```bash
for f in src/pages/available/index.astro src/pages/available/*/index.astro; do
  echo "=== $f ==="
  for kw in "African Grey" "for sale" "Congo African Grey" "Timneh" "hand-raised" "DNA" "CITES" "captive-bred"; do
    n=$(grep -oi "$kw" "$f" | wc -l | tr -d ' ')
    echo "  $kw: $n"
  done
done
```
Record the table in the audit doc. Flag any page where the primary phrase ("African Grey ... for sale") count looks thin (<8) or stuffed (>40) vs the others.

- [x] **Step 2: Audit voice / entity / humour coverage against the checklists**

For each page, grep for the markers the project's rules require:
```bash
for f in src/pages/available/index.astro src/pages/available/*/index.astro; do
  echo "=== $f ==="
  echo "  first-person (we/our/us): $(grep -oiE '\b(we|our|us)\b' "$f" | wc -l | tr -d ' ')"
  echo "  H-levels present: $(grep -oE '<h[1-6]' "$f" | sort -u | tr '\n' ' ')"
  echo "  third-person filler ('both make exceptional'): $(grep -ci 'both make exceptional' "$f")"
done
```
Note pages weak on first-person voice or missing heading levels (cross-check against `feedback_heading_outline_gate`: min 5 H5 + 5 H6, no skipped levels). Record verdicts STRONG / SHARPEN / REBUILD per page (per `feedback_noncommodity_audit_then_rewrite` — rewrite only the weak ones; do not regress indexed copy in this plan, just report).

- [x] **Step 3: Identify the top ranking competitors for the primary term**

Use Firecrawl search for "Congo African Grey for sale" and "African Grey parrot for sale" (per `data/competitors.json` registry as the seed list). Capture the top 3–5 commercial competitor URLs.

- [x] **Step 4: Scrape each competitor and count primary-keyword usage**

For each competitor URL, use `firecrawl_scrape` (markdown) and count occurrences of "African Grey", "for sale", "Congo", "Timneh". Record a comparison table: our hub/bird counts vs each competitor. If Firecrawl returns blocked/empty for a competitor, mark it `NOT FETCHED` — never invent a count (per `cags-comprehensive-page-audit-system` rule).

- [x] **Step 5: Write the audit report**

Create `docs/superpowers/sessions/2026-06-26-available-keyword-entity-audit.md` with: (a) our per-page keyword table, (b) voice/entity/humour/heading verdicts per page, (c) competitor keyword-count comparison, (d) a prioritized fix list (which pages need a SHARPEN/REBUILD pass and why). This report feeds a *future* content pass — it is reporting only; no page rewrites in this task.

- [x] **Step 6: Commit**

```bash
git add docs/superpowers/sessions/2026-06-26-available-keyword-entity-audit.md
git commit -m "docs(audit): keyword/entity/voice self-audit + competitor keyword benchmark for /available/ cluster

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 10: Resolve pre-existing working-tree deletions, final QA, deploy

**Files:**
- Working tree: `assets/brand/main-homepage-video-african-grey-parrots-video.mov`, `public/african-grey-parrot-head-scratch.webp`, `public/amie-congo-african-grey-female-3-months.webp` (deleted before this session)
- Run: `scripts/generate_sitemaps.py`, `scripts/final_page_audit.py --birds`

- [ ] **Step 1: Decide the pre-existing deletions (look before committing)**

For each deleted file, confirm nothing live still references it:
```bash
for f in african-grey-parrot-head-scratch.webp amie-congo-african-grey-female-3-months.webp main-homepage-video-african-grey-parrots-video.mov; do
  echo "=== $f ==="; grep -rln "$f" src/ public/ 2>/dev/null || echo "  no references"
done
```
Expected: the `.mov` is superseded by the untracked `.mp4`; the 2 webp deletions should have **no references** (Amie now uses `/birds/amie/` images). If a file is still referenced, RESTORE it (`git checkout -- <path>`) instead of committing the deletion. If unreferenced, stage the deletions.

- [ ] **Step 2: Commit the resolved deletions**

```bash
git add -A assets/brand public/african-grey-parrot-head-scratch.webp public/amie-congo-african-grey-female-3-months.webp
git commit -m "chore: drop unreferenced legacy media (superseded .mov + 2 orphaned webp)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```
(Only if Step 1 confirmed zero references. Otherwise skip and note the restore.)

- [ ] **Step 3: Regenerate sitemaps (image dimensions/pages may have shifted)**

Run: `python3 scripts/generate_sitemaps.py`
Expected: completes with 0 phantom URLs reported.

- [ ] **Step 4: Run the final page audit on the bird cluster**

Run: `npx astro build && python3 scripts/final_page_audit.py --birds`
Expected: one PASS / PASS-WITH-WARNINGS verdict per bird page. Resolve any new FAIL (e.g. heading levels, single Product/Offer, shipping line present, sold≠InStock) before deploy.

- [ ] **Step 5: Push (= deploy) and re-check live PageSpeed**

```bash
git push origin main
```
After Cloudflare Pages finishes, re-run PageSpeed on `/available/`, `/available/roys/`, and one Timneh page. Expected improvements: no `JumpRail.css` render-blocking on bird pages; image savings realized; contrast pass; (after the breeder toggles Rocket Loader) the `/70de/` unused-JS + long-task flags gone.

- [ ] **Step 6: Final verification summary**

Confirm and report to the breeder: (1) JumpRail removed from 6 pages; (2) gtag already deferred + Rocket Loader dashboard step handed off; (3) LCP poster preload live on 4 video pages; (4) images downscaled; (5) contrast ≥4.5:1; (6) fws link replaced (browser-verified URL); (7) Product critical cleared (Rich Results re-test); (8) geo distribution live with distinct angles; (9) audit report written; (10) deletions resolved + sitemaps regenerated.

---

## Open Flags (carry forward)

- **fws.gov / Rich Results / PageSpeed verification** all require a human in a real browser — fws.gov, cites.org, and Google's testers block every automated agent (curl + WebFetch both 403). T6/T7/T10 mark these as breeder/operator actions.
- **Rocket Loader** disable is a Cloudflare dashboard toggle only the breeder can flip (T2).
- **"5 vs 6 bird pages"** — plan covers all 6; confirm if one was meant to be excluded (T8 header note).
- **Reviews unchanged by decision** — `aggregateRating`/`review` deliberately NOT added; the optional Search Console notices will persist and that is accepted.

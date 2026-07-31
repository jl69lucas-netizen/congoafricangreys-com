# Congo Pair Page — Harden & Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: `superpowers:executing-plans`. Steps use `- [ ]` for tracking.

**Goal:** Take `/congo-african-grey-parrot-pair-for-sale/` from "structurally complete but rushed" to the finish level of `/african-grey-parrot-adoption-cost/` — every component clean at 375 / 768 / 1280, all 12 generated infographics rendered, every breeder-named image swapped in, zero orphaned assets, zero crossover prose.

**Architecture:** Page-scoped CSS under `.cpair` in `src/pages/congo-african-grey-parrot-pair-for-sale/index.astro`. No global CSS is touched (a global type-scale change would sweep 108 pages). Assets are baked from `assets/1WORKING-ON/FOR-SALE-PAGES/1CONGO-AFRICAN-grey-parrot-pair/` into `public/images/congo-pair-page/` with `scripts/reframe_og.py` (photos) and a new quality-walk for infographics (native ratio, never cover-cropped).

**Tech Stack:** Astro 4, Pillow, Playwright MCP, `scripts/page_hardening_scan.py`, `scripts/seam_parity.py`, `scripts/dup_content_audit.py`, `scripts/final_page_audit.py`.

---

## 0 · Measured baseline — every finding confirmed on the built page, not inferred

Per `skills/cag-gate-integrity.md`, nothing below was taken from a scanner report alone.

| # | Finding | How it was confirmed | Severity |
|---|---|---|---|
| B1 | **12 infographics exist as HTML comments only.** `<!-- INFOGRAPHIC SLOT: … -->` × 12; none of the 12 generated `.webp` files is in `public/` | grep of the `.astro` + `ls` of the asset folder | ERROR |
| B2 | **`--hdr` is undefined**, so every `var(--hdr, 72px)` resolves to 72px while `header` measures **96px** | Playwright: `getPropertyValue('--hdr')` → `""`; `body>header` rect `h:96` | ERROR |
| B3 | **Jump links land under the sticky chrome.** `scroll-margin-top: calc(72px + 20px)` = 92px vs header 96 + rail 51 = **147px needed** | Playwright at 375px: `railH:51`, header 96 | ERROR |
| B4 | **108 elements render below 12.5px at 375px** — down to 10.6px (`.cs-l`), 10.9px (hero ribbon), 11.8px (rail chips) | Playwright font-size sweep, `offsetParent` filtered | ERROR |
| B5 | **Bird cards broken**: names wrap to 2–3 lines, `$2,300 + $2,500` clips, 4 of 6 CTAs wrap to two lines, card heights ragged, birds cropped through the head | element screenshot at 375px | ERROR |
| B6 | **Geo cards mis-ordered**: `.geo-a{grid-row:1/span 2}` auto-places the arrow into column 1, collapsing the `1fr` track so the sub-label wraps one word per line | element screenshot at 1280px | ERROR |
| B7 | **Shipping section carries no image** although two shipping assets were supplied and two more sit orphaned in `public/` | grep + `comm` of referenced vs on-disk | ERROR |
| B8 | **4 orphaned images in `public/`**: `african-grey-breeding-pair-aviary`, `airport-cargo-shipping-african-greys`, `home-delivery-van-two-african-greys`, `two-trained-african-greys-with-owner` | `comm -13` referenced vs on-disk | WARN |
| B9 | **`.cpair p{max-width:70ch}` beats component `<p>`s.** `.k1-h` green band stops at 443px inside a 880px card | element screenshot at 1280px | WARN |
| ~~B10~~ | ~~**Breadcrumb overflows** at 375px~~ — **FALSE POSITIVE, withdrawn.** `.bc-pill` does measure 424px in a 375px viewport, but `.bc-pill-wrap` is a deliberate `overflow-x:auto` scroller with a trailing fade mask, added on purpose so long trails swipe instead of clipping. My probe's scroller exclusion list was missing it. A `flex-wrap` "fix" was written and reverted. | Read `Breadcrumb.astro` after the probe fired | **not a defect** |
| B11 | **Seam reads as a floating logo**, not a section divider — no clay hairlines (`skills/cag-page-hardening.md` §4) | visual + CSS read (`.seam{margin:2rem auto}` only) | WARN |
| B12 | **Anchor collisions**: `Adults kept back for production` (§10) sits against the spent `Adults kept back for breeding`; the three `.xsell` anchors reuse ledger phrasing | `2026-07-26-…-lessons.md` §Verified anchor ledger | WARN |
| B13 | Supplied assets never placed: `Mark-with the parrots.jpg`, `two-african-grey-congos-for-sale.jpg`, `Congo-African-grey-pair-eating.jpg`, `tamed-pair-…-shoulder.jpg`, `african-grey-parrot-socialization-training copy.mp4` | breeder list vs page grep | ERROR |

**Gates that were already clean and must stay clean** (do not "fix" these):

- `page_hardening_scan.py` → `0 ERROR · 0 WARN` over **1 source file, 1 built page** (count read, per gate-integrity).
- `seam_parity.py` → `PASS sections=24 seams=23 missing=0` over **1 page examined**.
- Playwright contrast sweep at 375px → **0 failures** across all text nodes with `details` forced open.

> This is textbook `cag-page-hardening` §1k: a clean static scan on a page with thirteen real defects. Both halves were required, and only the runtime half found B2–B6, B9, B10.

---

## 1 · File structure

| File | Responsibility | Action |
|---|---|---|
| `src/pages/congo-african-grey-parrot-pair-for-sale/index.astro` | The whole page: frontmatter data, markup, scoped `<style>`, scroll-spy script | Modify |
| `public/images/congo-pair-page/*.webp` | Every rendered image, `-760` sibling per in-body slot | Add 24, replace 6 |
| `public/video/congo-pair-socialization.mp4` | §8 protocol video | Add |
| `scripts/bake_infographics.py` | Reusable: native-ratio infographic → `<100 KB` WebP + `-760` sibling, no cover crop | Create |
| `docs/reference/technical-seo-fixes-backlog.md` | Log the site-wide `--fs-h5` 11px floor finding | Modify |
| `docs/superpowers/sessions/2026-07-31-congo-pair-harden-lessons.md` | Carry-forward lessons + anchors spent | Create |

---

## Task 1: Bake the 12 infographics without cropping their baked-in text

**Files:** Create `scripts/bake_infographics.py` · Add 24 files to `public/images/congo-pair-page/`

Infographics carry baked-in type. `cag-page-hardening` §1c is explicit: they are **never** cover-cropped into a page box. Eleven of the twelve are 1376×768 (ratio 1.792); one, `two-birds-two-document-sets.webp`, is **768×1376 portrait** and must not be stretched into a landscape frame.

- [ ] **Step 1: Write the baker**

```python
#!/usr/bin/env python3
"""Bake infographics to <100 KB WebP at NATIVE ratio, plus a -760 sibling.

Infographics carry baked-in text: never cover-crop them (cag-page-hardening §1c).
Photos go through scripts/reframe_og.py instead — this script never crops.
"""
import sys, pathlib
from PIL import Image

MAXKB = 100

def walk(im, out, maxkb=MAXKB):
    for q in range(86, 39, -3):
        im.save(out, "WEBP", quality=q, method=6)
        if out.stat().st_size <= maxkb * 1024:
            return q
    return q

def bake(src, dst_dir, stem):
    im = Image.open(src).convert("RGB")
    dst_dir.mkdir(parents=True, exist_ok=True)
    full = dst_dir / f"{stem}.webp"
    q1 = walk(im, full)
    w760 = 760
    h760 = round(im.height * w760 / im.width)
    sib = dst_dir / f"{stem}-760.webp"
    q2 = walk(im.resize((w760, h760), Image.LANCZOS), sib)
    print(f"{stem}: {im.width}x{im.height} q{q1} {full.stat().st_size//1024}KB "
          f"| 760x{h760} q{q2} {sib.stat().st_size//1024}KB")
    return im.width, im.height

if __name__ == "__main__":
    src_dir, dst_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    for name in sys.argv[3:]:
        bake(src_dir / f"{name}.webp", dst_dir, name)
```

- [ ] **Step 2: Run it over the twelve**

```bash
python3 scripts/bake_infographics.py \
  "assets/1WORKING-ON/FOR-SALE-PAGES/1CONGO-AFRICAN-grey-parrot-pair" \
  public/images/congo-pair-page \
  pair-bond-three-risk-conditions pair-versus-single-grey-tradeoff \
  keeping-a-pair-tame-daily-protocol one-grey-or-two-decision-guide \
  three-routes-to-an-african-grey-pair african-grey-pair-price-bracket \
  two-birds-two-document-sets pair-health-screening-pcr-panel \
  cites-appendix-one-two-birds-usa two-african-greys-travel-together \
  introducing-two-african-greys-first-30-days verify-african-grey-pair-seller-checks
```

Expected: 24 files, each ≤100 KB, intrinsic sizes echoed (needed for `width`/`height` attributes).

- [ ] **Step 3: Read every word on all twelve before accepting them** (prompt-pack rule §0: BREEDER / Polyomavirus / PBFD / CITES / IATA / Appendix I / Midland spelling, no baked prompt instructions, US spelling)

- [ ] **Step 4: Commit**

```bash
git add scripts/bake_infographics.py public/images/congo-pair-page
git commit -m "assets(congo-pair): bake the 12 infographics at native ratio, <100 KB each"
```

---

## Task 2: Swap in every breeder-named photo and clear the orphans

**Files:** `public/images/congo-pair-page/` · `public/video/`

Breeder mapping, verbatim from the brief:

| Card / slot | Source asset | Destination stem |
|---|---|---|
| Jins, or Jeni — $1,900 / $1,800 | `jins-jeni-two-unrelated-grey-pair.jpg` | `jins-or-jeni-single-bird-option` |
| Roys & Amie — $2,300 + $2,500 | `two-african-grey-congos-for-sale.jpg` | `roys-amie-two-congo-singles` |
| Elad & Evie — $1,600 + $1,500 | `timneh-african-grey-variant.webp` | `elad-evie-timneh-pair-option` |
| Bery — $1,700 | `assets/brand/BERY/bery-health-handfeeding.webp` | `bery-single-congo-hen` |
| Proven breeding pair | `breeding-pair-african-grey-parrots.jpg` | `proven-breeding-pair-african-greys` (replace AI version) |
| §20 verify | `Mark-with the parrots.jpg` | `mark-benjamin-with-our-african-greys` (replace) |
| §18 shipping tier 1 | `affordable-african-grey-parrot-shipping.jpg.webp` | `airport-cargo-shipping-african-greys` (adopt orphan) |
| §18 shipping tier 2 | `united-home-delivery-van-petsafe.webp` | `home-delivery-van-two-african-greys` (adopt orphan) |
| §22 compare | `Congo-African-grey-pair-eating.jpg` | `congo-pair-eating-together-aviary` (replace) |
| §8 protocol | `tamed-pair-african-grey-parrots-sitting-on-shoulder.jpg` | `tamed-pair-african-greys-on-shoulder` (replace) |
| §7 counterweight | orphan `two-trained-african-greys-with-owner` | render it (clears B8) |
| §8 video | `african-grey-parrot-socialization-training copy.mp4` | `public/video/congo-pair-socialization.mp4` |

- [ ] **Step 1: Bake the card photos with blurfill so no bird is cropped through the head**

`--style blurfill` is the LOCKED default (`IMAGE-DESIGNS.md §7`, memory `reference_og_blurfill_framing`). Cards render at 4:3, in-body photos at 16:9 with a 4:5 mobile sibling.

```bash
A="assets/1WORKING-ON/FOR-SALE-PAGES/1CONGO-AFRICAN-grey-parrot-pair"
O="public/images/congo-pair-page"
# card slots — 4:3, 640x480, 320 sibling
python3 scripts/reframe_og.py --style blurfill --w 640 --h 480 --sib 320 --maxkb 60 \
  "$A/jins-jeni-two-unrelated-grey-pair.jpg" "$O/jins-or-jeni-single-bird-option.webp"
python3 scripts/reframe_og.py --style blurfill --w 640 --h 480 --sib 320 --maxkb 60 \
  "$A/two-african-grey-congos-for-sale.jpg" "$O/roys-amie-two-congo-singles.webp"
python3 scripts/reframe_og.py --style blurfill --w 640 --h 480 --sib 320 --maxkb 60 \
  "$A/timneh-african-grey-variant.webp" "$O/elad-evie-timneh-pair-option.webp"
python3 scripts/reframe_og.py --style blurfill --w 640 --h 480 --sib 320 --maxkb 60 \
  "assets/brand/BERY/bery-health-handfeeding.webp" "$O/bery-single-congo-hen.webp"
python3 scripts/reframe_og.py --style blurfill --w 640 --h 480 --sib 320 --maxkb 60 \
  "$A/breeding-pair-african-grey-parrots.jpg" "$O/proven-breeding-pair-african-greys.webp"
python3 scripts/reframe_og.py --style blurfill --w 640 --h 480 --sib 320 --maxkb 60 \
  "$A/jins-jeni4-cong-african-grey-pair-eating-veggies.webp" "$O/jins-jeni-congo-pair-portrait.webp"
```

- [ ] **Step 2: Bake the in-body photos at 16:9 with a 4:5 mobile crop**

```bash
for pair in \
 "Mark-with the parrots.jpg|mark-benjamin-with-our-african-greys" \
 "Congo-African-grey-pair-eating.jpg|congo-pair-eating-together-aviary" \
 "tamed-pair-african-grey-parrots-sitting-on-shoulder.jpg|tamed-pair-african-greys-on-shoulder" \
 "two-trained-african-grey-parrots-sitting-on-mike-shoulder.jpg|two-trained-african-greys-with-owner" \
 "affordable-african-grey-parrot-shipping.jpg.webp|airport-cargo-shipping-african-greys" \
 "united-home-delivery-van-petsafe.webp|home-delivery-van-two-african-greys" ; do
  src="${pair%%|*}"; stem="${pair##*|}"
  python3 scripts/reframe_og.py --style blurfill --w 1408 --h 768 --sib 760 \
    --mobcrop 4:5 --maxkb 95 "$A/$src" "$O/$stem.webp"
done
```

- [ ] **Step 3: Copy the video**

```bash
mkdir -p public/video
cp "$A/african-grey-parrot-socialization-training copy.mp4" public/video/congo-pair-socialization.mp4
ls -la public/video/congo-pair-socialization.mp4   # expect ~7.6 MB
```

- [ ] **Step 4: Delete the now-dead AI card art**

```bash
rm -f public/images/congo-pair-page/male-female-congo-greys-side-by-side*.webp \
      public/images/congo-pair-page/african-grey-breeding-pair-aviary*.webp
```

- [ ] **Step 5: Commit**

```bash
git add public/images/congo-pair-page public/video
git commit -m "assets(congo-pair): swap in the breeder's real photos, adopt both shipping images, place the socialization clip"
```

---

## Task 3: Fix the sticky-chrome offset so jump links actually land (B2, B3)

**Files:** Modify `src/pages/congo-african-grey-parrot-pair-for-sale/index.astro` (scoped `<style>`)

The header measures 96px; the page assumed 72px everywhere. `cag-page-hardening` §1b: *"`--hdr` must equal the REAL header height (96px)"*, and anchors need `calc(var(--hdr) + 16px)` on desktop, `calc(var(--hdr) + 74px)` on mobile.

- [ ] **Step 1: Declare `--hdr` and a rail height on the page root**

```css
.cpair { --hdr:96px; --rail-h:52px; background:var(--cp-cream); color:var(--cp-ink); overflow-x:clip; }
```

- [ ] **Step 2: Replace every `var(--hdr, 72px)` with `var(--hdr)` and correct the anchor offsets**

```css
.cpair-main section { scroll-margin-top:calc(var(--hdr) + 16px); padding:6px 0 4px; }
@media (max-width:1024px){
  .cpair-main section { scroll-margin-top:calc(var(--hdr) + var(--rail-h) + 14px); }
}
```

- [ ] **Step 3: Verify by clicking a rail chip at 375px, not by reading the CSS**

```js
// Playwright, 375px
document.querySelector('.railA a[href="#protocol"]').click();
await new Promise(r=>setTimeout(r,400));
const h2 = document.querySelector('#protocol h2').getBoundingClientRect();
// PASS when h2.top >= 96 + 52  (below header AND rail)
```

Expected: `h2.top ≈ 150–165`. Before the fix it is ≈ 92 minus the chrome, i.e. hidden.

- [ ] **Step 4: Commit**

```bash
git add src/pages/congo-african-grey-parrot-pair-for-sale/index.astro
git commit -m "fix(congo-pair): --hdr is 96px, not 72 — jump links now clear the header and the mobile rail"
```

---

## Task 4: Raise the mobile type floors (B4)

**Files:** Modify the scoped `<style>`

108 text nodes render under 12.5px at 375px. `PRODUCT.md` states the audience skews older, and `DESIGN.md` §Accessibility says *"contrast and text size matter more than usual"*. The global `--fs-h5` clamp bottoms out at 11px, so this is a site-wide condition — **log it to the backlog, fix it page-scoped here.** Desktop maxima are unchanged, so the page still matches its siblings at 1280.

- [ ] **Step 1: Lift the clamp minima, keeping every maximum identical**

```css
.cpair .cag-h5 { font-size:clamp(.875rem, 1.1vw, .95rem); }   /* 14px floor, was 11 */
.cpair .cag-h6 { font-size:clamp(.85rem, 1.1vw, .9rem); }     /* 13.6px floor, was 11 */
.cpair .cs-l   { font-size:clamp(.75rem, 2.2vw, .78rem); }    /* 12px floor, was 10.6 */
.cpair .phero-ribbon li { font-size:clamp(.75rem, 2vw, .78rem); }
.cpair .rcard-sub { font-size:.78rem; }
.cpair .img-note, .cpair .availB-ship, .cpair .fsx-ship, .cpair .fsx-note { font-size:.8rem; }
.cpair .tg, .cpair .tdial-k, .cpair .xsell-k, .cpair .availB-k, .cpair .fsx-k,
.cpair .k1-h, .cpair .k2-tag { font-size:.66rem; }            /* desktop-only chrome */
@media (max-width:1024px){ .cpair .railA a { font-size:.82rem; } }
@media (max-width:640px){
  .cpair .rcard-price { font-size:.95rem; }
  .cpair .k1-list dt, .cpair .k1-list dd { font-size:.9rem; }
  .cpair .tF, .cpair .tA { font-size:.9rem; }
  .cpair .tF td::before, .cpair .tA td::before { font-size:.7rem; }
  .cpair .faqB-i summary { font-size:.92rem; }
  .cpair .faqB-i p { font-size:.88rem; }
  .cpair .quote-c blockquote p { font-size:.9rem; }
  .cpair .fs-fine, .cpair .geo-n { font-size:.78rem; }
}
```

- [ ] **Step 2: Re-run the font-size sweep at 375px; target zero elements under 12px** (the desktop-only dial chrome is `display:none` at 375 and must be excluded by `!el.offsetParent`, not by name)

- [ ] **Step 3: Commit**

```bash
git commit -am "fix(congo-pair): mobile type floors — nothing under 12px at 375px"
```

---

## Task 5: Rebuild the bird card (B5)

**Files:** Modify markup + scoped `<style>`

Standing component rules, `cag-page-hardening` §4: name/price row is `grid-template-columns:minmax(0,1fr) auto` with `nowrap` on the price; the CTA reads `Reserve <name> →`, `white-space:nowrap`, `margin-top:auto` so every card shares a button baseline; the badge sits bottom-left over a scrim.

- [ ] **Step 1: Shorten the labels that cannot fit** (§5 of the hardening skill: *never add `nowrap` to a label that cannot fit*)

| Card | Was | Now |
|---|---|---|
| Roys & Amie | `Ask About Roys & Amie →` | `See Roys & Amie →` |
| Elad & Evie | `See Our Timnehs →` | `See the Timnehs →` |
| Jins, or Jeni | `Ask About One Bird →` | `Ask About One →` |
| Proven pair | `See the Breeding Pair →` | `See the Pair →` |

- [ ] **Step 2: Replace the price strings that overflow**

`$2,300 + $2,500` and `$1,600 + $1,500` are two prices in one nowrap cell. Render the sum as the headline price and the split beneath it:

```astro
<div class="rcard-top">
  <h3 class="rcard-name">{r.name}</h3>
  <span class="rcard-price">{r.price}</span>
</div>
{r.split && <p class="rcard-split">{r.split}</p>}
```

with `price: "$4,800"`, `split: "$2,300 + $2,500"` for Roys & Amie and `price: "$3,100"`, `split: "$1,600 + $1,500"` for Elad & Evie. Jins/Jeni keeps `price: "$1,900 / $1,800"` (it is an either/or, not a sum) at `font-size:.85rem`.

- [ ] **Step 3: Rewrite the card CSS**

```css
.rcard-photo img { width:100%; aspect-ratio:4/3; height:auto; object-fit:cover; display:block; }
.rcard-photo::after { content:""; position:absolute; inset:auto 0 0 0; height:52px;
  background:linear-gradient(to top, rgba(28,26,24,.42), transparent); pointer-events:none; }
.rbadge { position:absolute; left:10px; bottom:10px; background:rgba(255,255,255,.94);
  color:var(--cp-green); font-size:.64rem; font-weight:700; padding:3px 9px; border-radius:50px; }
.rcard-top { display:grid; grid-template-columns:minmax(0,1fr) auto; gap:8px; align-items:baseline; }
.rcard-name { font-size:1.02rem; margin:0; line-height:1.2; }
.rcard-price { color:var(--cp-claytext); font-weight:700; font-size:.95rem; white-space:nowrap; }
.rcard-split { font-size:.72rem; color:var(--cp-mid); margin:0; }
.rcard .btn-clay { margin-top:auto; align-self:start; width:auto; white-space:nowrap;
  font-size:.8rem; padding:.55rem 1rem; }
@media (max-width:640px){ .rcard .btn-clay { align-self:stretch; text-align:center; } }
```

- [ ] **Step 4: Verify card heights are uniform and no CTA wraps**

```js
[...document.querySelectorAll('.rcard')].map(c=>Math.round(c.getBoundingClientRect().height))
// expect all equal (grid stretch), and:
[...document.querySelectorAll('.rcard .btn-clay')].map(b=>Math.round(b.getBoundingClientRect().height))
// expect every value under 44 (one line)
```

- [ ] **Step 5: Commit**

```bash
git commit -am "fix(congo-pair): bird cards — grid name/price row, one-line CTAs, 4:3 uncropped photos, scrim badge"
```

---

## Task 6: Render the 12 infographics into their slots (B1)

**Files:** Modify markup + scoped `<style>`

Every `<!-- INFOGRAPHIC SLOT: … -->` comment becomes a real `<figure>`. Infographics get `.inf-img`, never `.og-photo`, so §1c's cover-crop trap cannot bite.

- [ ] **Step 1: Add the infographic CSS**

```css
/* Infographics carry baked-in text: native ratio, contain, never cover-cropped (§1c). */
.sec-img.inf-img { max-width:760px; width:100%; height:auto; object-fit:contain;
  background:#fff; aspect-ratio:auto; }
.sec-img.inf-tall { max-width:430px; }          /* the one portrait asset */
@media (max-width:640px){
  .cpair .sec-img.inf-img { width:100vw; margin-left:calc(50% - 50vw); max-width:none;
    border-radius:0; border-left:0; border-right:0; }
  .cpair .sec-img.inf-tall { width:auto; margin-left:0; max-width:100%; border-radius:12px; }
}
```

- [ ] **Step 2: Replace each comment with the figure** (pattern; repeat with each slot's own alt — Rule 50b, no two alts alike)

```astro
<figure class="sec-img-wrap">
  <img class="sec-img inf-img" src={`${IMG}/pair-bond-three-risk-conditions.webp`}
       srcset={`${IMG}/pair-bond-three-risk-conditions-760.webp 760w, ${IMG}/pair-bond-three-risk-conditions.webp 1376w`}
       sizes="(max-width:900px) 100vw, 760px" width="1376" height="768"
       alt="The three stacked conditions that let a Congo African Grey pair bond to each other instead of you"
       loading="lazy" decoding="async" />
  <figcaption class="img-note">All three present is the strongest pair bond. Remove any one and the human bond holds.</figcaption>
</figure>
```

Slot → file → section:

| § | File | Anchor |
|---|---|---|
| 6 | `pair-bond-three-risk-conditions` | `#pair-bond` |
| 7 | `pair-versus-single-grey-tradeoff` | `#protects` |
| 8 | `keeping-a-pair-tame-daily-protocol` | `#protocol` |
| 9 | `one-grey-or-two-decision-guide` | `#one-bird` |
| 10 | `three-routes-to-an-african-grey-pair` | `#routes` |
| 12 | `african-grey-pair-price-bracket` | `#market` |
| 15 | `two-birds-two-document-sets` **(portrait, `inf-tall`)** | `#papers` |
| 16 | `pair-health-screening-pcr-panel` | `#health` |
| 17 | `cites-appendix-one-two-birds-usa` | `#legal` |
| 18 | `two-african-greys-travel-together` | `#shipping` |
| 19 | `introducing-two-african-greys-first-30-days` | `#settling` |
| 20 | `verify-african-grey-pair-seller-checks` | `#verify` |

- [ ] **Step 3: Confirm zero infographic is cover-cropped**

```js
[...document.querySelectorAll('.inf-img')].map(i=>({
  f:i.currentSrc.split('/').pop(), fit:getComputedStyle(i).objectFit,
  drawn:Math.round(i.getBoundingClientRect().width)+'x'+Math.round(i.getBoundingClientRect().height),
  natural:i.naturalWidth+'x'+i.naturalHeight}))
// every fit must be "contain"; drawn ratio must equal natural ratio ±1%
```

- [ ] **Step 4: Commit**

```bash
git commit -am "feat(congo-pair): render all 12 infographics at native ratio in their approved slots"
```

---

## Task 7: Rebuild the shipping section and fix the geo cards (B6, B7)

**Files:** Modify markup + scoped `<style>`

- [ ] **Step 1: Fix the geo-card grid.** The arrow must be placed explicitly, or auto-placement puts it first.

```css
.geo-cards a { display:grid; grid-template-columns:minmax(0,1fr) auto;
  grid-template-areas:"k a" "n a"; gap:2px 10px; align-items:center; }
.geo-k { grid-area:k; } .geo-n { grid-area:n; } .geo-a { grid-area:a; align-self:center; }
```

- [ ] **Step 2: Add the two-tier shipping card using both supplied images**

```astro
<div class="ship-tiers">
  <article class="ship-t">
    <img src={`${IMG}/airport-cargo-shipping-african-greys-760.webp`}
         srcset={`${IMG}/airport-cargo-shipping-african-greys-760.webp 760w, ${IMG}/airport-cargo-shipping-african-greys.webp 1408w`}
         sizes="(max-width:900px) 92vw, 360px" width="760" height="415"
         alt="An IATA live-animal container at the airline cargo counter, the $185 airport pickup route for two greys"
         loading="lazy" decoding="async" />
    <p class="ship-tier">Airport pickup</p>
    <p class="ship-fig">$185</p>
    <p class="ship-b">Per reservation, not per bird. Delta, United or American cargo to your nearest major airport.</p>
  </article>
  <article class="ship-t">
    <img src={`${IMG}/home-delivery-van-two-african-greys-760.webp`}
         srcset={`${IMG}/home-delivery-van-two-african-greys-760.webp 760w, ${IMG}/home-delivery-van-two-african-greys.webp 1408w`}
         sizes="(max-width:900px) 92vw, 360px" width="760" height="415"
         alt="A climate-controlled courier van at a front door, the $350 home delivery option for a two-bird reservation"
         loading="lazy" decoding="async" />
    <p class="ship-tier">Home delivery</p>
    <p class="ship-fig">$350</p>
    <p class="ship-b">Door to door, both birds on the same booking, with the paperwork handed over in person.</p>
  </article>
</div>
```

```css
.ship-tiers { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:14px; margin:1rem 0; }
.ship-t { background:#fff; border:1px solid var(--cp-bd); border-radius:20px; overflow:hidden;
  box-shadow:0 2px 12px rgba(60,30,10,.05); }
.ship-t img { width:100%; aspect-ratio:16/9; object-fit:cover; display:block; }
.cpair p.ship-tier { margin:12px 14px 0; font-size:.66rem; letter-spacing:.14em;
  text-transform:uppercase; color:var(--cp-green); font-weight:700; }
.cpair p.ship-fig { margin:2px 14px 0; font-family:var(--font-lora,Georgia,serif);
  font-size:1.5rem; color:var(--cp-claytext); }
.cpair p.ship-b { margin:4px 14px 14px; font-size:.84rem; color:var(--cp-mid); max-width:none; }
```

> The three `.ship-*` paragraph rules are **qualified with `.cpair p`** on purpose — §1l, the exact
> collision that rendered `.ship-tier` at 1.19:1 on adoption-cost.

- [ ] **Step 3: Verify contrast and layout at 375 / 768 / 1280** — run the §2b sweep again; expect 0 failures.

- [ ] **Step 4: Commit**

```bash
git commit -am "fix(congo-pair): shipping section — two-tier cards using both supplied images, geo-card grid areas"
```

---

## Task 8: Frame the seam, fix the receipt band, stack the receipt on mobile (B9, B11)

**Files:** Modify markup + scoped `<style>`

- [ ] **Step 1: Frame the seam** (`cag-page-hardening` §4: *"two clay hairlines flanking a ~34px wordmark"*). Wrap the bare `<img class="seam">` in a flex divider.

```astro
<div class="seam-wrap" aria-hidden="true">
  <img class="seam" src={seam} alt="" width="182" height="60" loading="lazy" decoding="async" />
</div>
```

```css
.seam-wrap { display:flex; align-items:center; gap:16px; margin:2.4rem 0 1.6rem; }
.seam-wrap::before, .seam-wrap::after { content:""; flex:1; height:1px;
  background:linear-gradient(to right, transparent, rgba(232,96,76,.42), transparent); }
.seam { display:block; margin:0; height:34px; width:auto; opacity:.9; }
```

- [ ] **Step 2: Free the component bands from `.cpair p{max-width:70ch}`**

```css
.cpair p.k1-h, .cpair p.xsell-k, .cpair p.fsx-k, .cpair p.availB-k,
.cpair p.tdial-k, .cpair p.ship-tier { max-width:none; }
```

- [ ] **Step 3: Stack the five-fact receipt on mobile**

```css
@media (max-width:640px){
  .k1-list > div { grid-template-columns:1fr; gap:2px; padding:9px 0; }
  .k1-list dt { font-size:.92rem; }
  .k1-list dd { font-size:.88rem; }
  .k2 { flex-direction:column; align-items:flex-start; gap:4px; }
}
```

- [ ] **Step 4: Verify `.k1-h` now spans the full card**

```js
const h=document.querySelector('.k1-h').getBoundingClientRect(), c=document.querySelector('.k1').getBoundingClientRect();
Math.round(c.width - h.width)   // expect 0 (was 437)
```

- [ ] **Step 5: Commit**

```bash
git commit -am "fix(congo-pair): framed seam dividers, full-width receipt band, receipt stacks on mobile"
```

---

## Task 9: Place the socialization video in §8 (B13)

**Files:** Modify markup + scoped `<style>`

`cag-for-sale-page-builder` §6a: video ships as the framed `.fs-video` component, never a bare `<video>`. §8 (the daily one-to-one protocol) is the contextual home: the clip *is* socialization training.

- [ ] **Step 1: Add the component after the H3 "Training Each Bird Alone Rather Than as a Unit"**

```astro
<figure class="fs-video">
  <video controls preload="none" width="1280" height="720"
         poster={`${IMG}/tamed-pair-african-greys-on-shoulder-760.webp`}>
    <source src="/video/congo-pair-socialization.mp4" type="video/mp4" />
  </video>
  <figcaption>
    <span class="fsv-tag">Our aviary, Midland TX</span>
    One-to-one socialization, filmed here. This is the session each bird in a pair needs on its own.
  </figcaption>
</figure>
```

```css
.fs-video { margin:1.2rem 0; background:#20342b; border-radius:20px; overflow:hidden;
  max-width:760px; }
.fs-video video { width:100%; height:auto; display:block; aspect-ratio:16/9;
  object-fit:cover; background:#20342b; }
.fs-video figcaption { padding:12px 16px; font-size:.84rem; color:#dcefe4; }
.fsv-tag { display:inline-block; font-size:.62rem; letter-spacing:.14em; text-transform:uppercase;
  color:#c9f2db; margin-right:8px; }
```

`preload="none"` keeps a 7.6 MB file off the critical path; the poster is an image the page already ships.

- [ ] **Step 2: Confirm the `<video>` fallback text is excluded from the contrast sweep** (there is none — the element carries no fallback text node, which is why §2b's `closest('video')` guard exists).

- [ ] **Step 3: Commit**

```bash
git commit -am "feat(congo-pair): framed socialization video in the daily-protocol section"
```

---

## Task 10: Spend fresh anchors, retire the collisions (B12)

**Files:** Modify markup

The Anchor Diversity Ledger (`2026-07-26-…-lessons.md` §6) forbids reusing an anchor for the same target. Two rewrites, plus the three `.xsell` lines the breeder flagged for keyword variation.

- [ ] **Step 1: Rewrite §10's breeding-pair anchor**

`Adults kept back for production` → **`Aviary stock valued on its breeding record`** (the spent phrasings are *Adults kept back for breeding*, *Breeding stock carries its own price logic*, *proven breeding pair*, *Adult breeding pairs*, *The breeding pair we currently hold*).

- [ ] **Step 2: Rewrite the three `.xsell` lines with different keyword variations**

```astro
<div class="xsell">
  <p class="xsell-k">Also from our aviary</p>
  <p><a href="/african-grey-breeding-pair-for-sale/">A proven producing duo for an established aviary</a> is priced on its record, not its tameness, and it is a different listing from every companion bird above. ↗</p>
  <p><a href="/african-grey-parrot-bird-eggs-for-sale-usa/">Candled Congo eggs for a working incubator</a> answer a different ambition entirely, and that page is blunt about who should not buy them. ↗</p>
  <p><a href="/hand-raised-african-grey-parrot-for-sale/">The Benjamin Home-Raising Protocol behind both birds</a> is what "hand-raised" means whenever we use the phrase. ↗</p>
</div>
```

Anchors newly spent, for the next page's ledger: *A proven producing duo for an established aviary* · *Candled Congo eggs for a working incubator* · *The Benjamin Home-Raising Protocol behind both birds* · *Aviary stock valued on its breeding record*.

- [ ] **Step 3: Script the collision check against the built page, do not eyeball it**

```bash
python3 - <<'PY'
import re, pathlib
spent = {
 "/african-grey-breeding-pair-for-sale/": {"proven breeding pair","proven-producer pair","see the pair",
   "adult breeding pairs","a lab-sexed adult pair","aviary-raised adult pairs",
   "the breeding pair we currently hold","adults kept back for breeding",
   "breeding stock carries its own price logic"},
 "/african-grey-parrot-bird-eggs-for-sale-usa/": {"african grey egg page","fertile african grey eggs",
   "eggs priced by sex","hatching a grey yourself","congo eggs in an incubator",
   "incubating your own clutch"},
}
html = pathlib.Path("dist/congo-african-grey-parrot-pair-for-sale/index.html").read_text()
hits = 0
for href, text in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.S):
    t = re.sub(r'<[^>]+>', '', text).strip().lower().rstrip(' ↗')
    if t in spent.get(href, ()):
        print("COLLISION", href, "|", t); hits += 1
print("collisions:", hits, "| anchors examined:", len(re.findall(r'<a[^>]+href=', html)))
PY
```

Expected: `collisions: 0` with a non-zero examined count. **A zero examined count is not a pass.**

- [ ] **Step 4: Commit**

```bash
git commit -am "content(congo-pair): fresh cross-sell anchors, retire two ledger collisions"
```

---

## Task 11: Contain the breadcrumb at 375px (B10)

**Files:** Modify the scoped `<style>`

- [ ] **Step 1:** The breadcrumb is a shared component; scope the fix to this page rather than editing `Breadcrumb.astro` and moving 108 pages.

```css
.cpair .bc-pill { flex-wrap:wrap; max-width:100%; }
@media (max-width:640px){ .cpair .bc-pill { font-size:.78rem; row-gap:2px; } }
```

- [ ] **Step 2: Verify with the §2a right-edge probe, not `scrollWidth`** (`overflow-x:clip` masks `scrollWidth`)

```js
[...document.querySelectorAll('main *')].filter(e=>e.getBoundingClientRect().right>innerWidth+1)
  .filter(e=>!e.closest('.railA,.availB-rail,.tF-wrap,.tA-wrap'))   // legit horizontal scrollers
  .map(e=>e.tagName+'.'+(e.className||'').toString().slice(0,30))
// expect []
```

- [ ] **Step 3:** Log the shared-component finding to `docs/reference/technical-seo-fixes-backlog.md` so the other 107 pages are not silently left broken.

- [ ] **Step 4: Commit**

```bash
git commit -am "fix(congo-pair): breadcrumb wraps instead of overflowing at 375px"
```

---

## Task 12: Gates, in the order the playbook prescribes

**Files:** none modified unless a gate finds a real defect

- [ ] **Step 1: Build, then the static half**

```bash
npx astro build
python3 scripts/page_hardening_scan.py congo-african-grey-parrot-pair-for-sale
python3 scripts/seam_parity.py congo-african-grey-parrot-pair-for-sale
```

Expected: `0 ERROR · 0 WARN` over **1 built page** (read the count), and `sections=N seams=N-1 missing=0`. Task 6 adds no `<section>`, so parity must hold at 24/23.

- [ ] **Step 2: Runtime half at 375 / 768 / 1280** — overflow (§2a), contrast (§2b), sizing (§2c), real-`ch` line length (§2y), `srcset` waste (§2z). **Measure a real `ch` by rendering "0" in the element's own computed font**; `0.5em` over-reports by ~20%.

- [ ] **Step 3: Duplicate content, pairwise across the whole for-sale cluster.** Pass slugs **literally** — zsh does not word-split `$VAR`, and that trap produced a PASS over zero pages.

```bash
python3 scripts/dup_content_audit.py congo-african-grey-parrot-pair-for-sale \
  congo-african-grey-for-sale timneh-african-grey-for-sale \
  hand-raised-african-grey-parrot-for-sale african-greys-for-sale-with-health-guarantee \
  dna-tested-african-grey-for-sale african-grey-parrot-bird-eggs-for-sale-usa \
  baby-african-grey-parrot-for-sale african-grey-parrot-adoption-cost
python3 scripts/dup_content_audit.py --headers congo-african-grey-parrot-pair-for-sale \
  congo-african-grey-for-sale timneh-african-grey-for-sale \
  hand-raised-african-grey-parrot-for-sale african-greys-for-sale-with-health-guarantee \
  dna-tested-african-grey-for-sale african-grey-parrot-bird-eggs-for-sale-usa \
  baby-african-grey-parrot-for-sale african-grey-parrot-adoption-cost
```

Expected: zero non-whitelist crossover, over **9 pages examined**.

- [ ] **Step 4: Final page audit + health sweep**

```bash
python3 scripts/final_page_audit.py
bash scripts/health-sweep.sh --no-build
```

- [ ] **Step 5: Sitemaps.** The URL set is unchanged, so regenerate only for the phantom-URL check and revert if the diff is date-churn (§5 of the hardening skill).

```bash
python3 scripts/generate_sitemaps.py && git diff --stat public/sitemap*
```

- [ ] **Step 6: Perf — ≥5 Lighthouse runs, judged on the distribution.** CLS on this site is bimodal; one run already caused a confident wrong attribution.

- [ ] **Step 7: Deploy**

```bash
git push origin main
```

---

## 13 · Out of scope, stated explicitly

1. **The global `--fs-h5` 11px floor.** Fixed page-scoped here; the same condition exists on 107 other pages. Logged to `docs/reference/technical-seo-fixes-backlog.md`, not swept, because a global type change needs its own verification pass.
2. **`Breadcrumb.astro`.** Same reasoning as above.
3. **Self-hosted fonts / the dna-tested CLS race.** Carried from the 2026-07-26 deferred list; unrelated to this page.
4. **The `/70de/` GA4 double-load.** Edge-injected by Cloudflare, invisible in `dist/`, dashboard-level fix.

---

## 14 · Self-review

**Spec coverage.** B1→T6 · B2,B3→T3 · B4→T4 · B5→T5 · B6,B7→T7 · B8→T2 · B9,B11→T8 · B10→T11 · B12→T10 · B13→T2,T9. All thirteen findings have a task.

**Placeholder scan.** No TBDs; every CSS block, alt string, anchor and command is literal.

**Type consistency.** `--hdr` / `--rail-h` are declared once in T3 and referenced by T3 only. `.inf-img` / `.inf-tall` are defined in T6 and used only there. `.ship-t*` classes are defined and used within T7. `r.split` is added to the `routes` array in T5 and read in T5's markup.

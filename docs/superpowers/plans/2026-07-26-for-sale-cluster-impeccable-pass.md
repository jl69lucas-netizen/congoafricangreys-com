# For-Sale Cluster — Impeccable UI/UX + Performance Pass Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Take all 6 built for-sale cluster pages to 100/green Lighthouse on mobile and desktop, and to a clean, readable, well-fitted UI at mobile / tablet / desktop — after first closing the gaps in the audit gates that let these defects ship.

**Architecture:** Three layers, in order. (1) **Gate layer** — add the 8 missing checks to `page_hardening_scan.py` so every defect the breeder found by hand is caught mechanically from now on. (2) **Root-cause layer** — four sitewide fixes in `BaseLayout.astro` / `global.css` that resolve the *same* Lighthouse findings on all 6 pages (and all 109 URLs) in one change: font loading, analytics double-load, scroll behaviour, forced reflow. (3) **Page layer** — the per-page visual and a11y defects, which are genuinely distinct per page.

**Tech Stack:** Astro 5 static build, Tailwind + `direction-d.css` theme layer, Cloudflare Pages, Netlify-style forms, `scripts/page_hardening_scan.py` + `scripts/final_page_audit.py` as the mechanical gates.

---

## Ground Truth Established Before Planning

These were verified against the live site and the source, not assumed. Three of them contradict what was believed going in.

| Finding | Evidence | Consequence |
|---|---|---|
| **`/70de/` is Google Analytics, not Rocket Loader** | `curl https://congoafricangreys.com/70de/` returns `// Copyright 2012 Google Inc.` + a gtag container with `G-MEWJ9GVC4T`. Served `content-type: application/javascript` from our own origin. | This is Cloudflare's **Google Tag Gateway** serving gtag first-party. Turning Rocket Loader off could never have fixed it. The desktop Lighthouse table lists **both** `googletagmanager.com/gtag/js` (158.9 KiB) *and* `/70de/` (167.9 KiB) — the tag is loading twice, ~327 KiB. |
| **4 font families load; only 2 render** | `BaseLayout.astro:97` requests Lora + Sora + Newsreader + IBM Plex Sans. `direction-d.css:58,69` overrides `.font-sora` → IBM Plex Sans and all headings → Newsreader with `!important`. | **Lora and Sora are 100% dead weight on every page of the site.** They are 2 of the 5–6 woff2 files in every "Network dependency tree" finding. |
| **The font CSS is already async** | `BaseLayout.astro:98-100` uses `media="print" onload="this.media='all'"`. | The chain is not render-blocking CSS — it is *discovery latency*: HTML → Google CSS → woff2. The fix is self-hosting + preload, not "make the CSS async" (already done). |
| **No nav DOM duplication on health-guarantee** | `grep -c 'href="#covers"'` = **1**. | Lighthouse repeats each anchor because it reports *overlap pairs*. This is a **spacing** failure (`gap:7px` at `.hgar .railA ul`, line 1109), not duplicated markup. Corrects my initial read. |
| **No smooth scrolling exists anywhere** | `grep -rn "scroll-behavior" src/` returns only `scroll-behavior:auto` on the rail's horizontal scroller. | The breeder's request is a genuine addition, not a repair. |
| **Anchor scroll-margin already handled** | `african-greys-for-sale-with-health-guarantee/index.astro:1114` comment + rules clear header (96px) + sticky rail (~54px). | This is why smooth scroll is now *safe* to add — the historical breakage (`reference_smooth_scroll_kills_jump_links`) was scroll-margin absence. Must still be verified per page. |

### Honest note on which findings actually move the score

Of the items in the brief, these are **`Unscored` diagnostics** — Lighthouse labels them so in the breeder's own paste, and they contribute **zero** to the performance number:

- *Missing source maps for large first-party JavaScript* — this is Google's minified analytics code. We cannot ship source maps for third-party code we do not compile. **This will never clear, on any page, ever.** It is informational.
- *Network dependency tree* — a diagnostic, not a scored audit.
- *Forced reflow* — a diagnostic. Worth fixing (it is real jank) but it is not why the score is 76–84.

What actually moves mobile 76→100 is: **LCP** (hero image bytes + font swap timing) and **TBT/FCP** (the ~330 KiB of analytics JS). Everything else in the brief is UI/a11y correctness, which is scored separately and is already at 100 — except the two genuine a11y failures (contrast, tap-target spacing) which will drop the a11y score and must be fixed.

---

## File Structure

| File | Responsibility | Change |
|---|---|---|
| `scripts/page_hardening_scan.py` | Static defect scanner over `dist/` | Modify — add 8 checks |
| `skills/cag-page-hardening.md` | Spec for the above | Modify — document the 8 checks |
| `skills/cag-final-page-pass.md` | Final gate skill | Modify — add perf-budget + font/analytics gates |
| `src/layouts/BaseLayout.astro` | Global head, fonts, analytics | Modify — self-hosted fonts, single GA load |
| `public/fonts/` | Self-hosted woff2 subsets | Create |
| `src/styles/global.css` | Global tokens + base | Modify — `@font-face`, smooth scroll |
| `src/components/ScrollSpy.astro` *(if extracted)* | rAF-batched scrollspy | Create/Modify |
| `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro` | Page | Modify — hero srcset, newsletter, type rhythm |
| `src/pages/dna-tested-african-grey-for-sale/index.astro` | Page | Modify — hero srcset, `.faqA-n` contrast, form arrow, newsletter |
| `src/pages/african-greys-for-sale-with-health-guarantee/index.astro` | Page | Modify — rail spacing, tick alignment, receipt labels, form overflow, newsletter |
| `src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro` | Page | Modify — phase 6 |
| `src/pages/congo-african-grey-for-sale/index.astro` | Page | Modify — phase 6 |
| `src/pages/timneh-african-grey-for-sale/index.astro` | Page | Modify — phase 6 |

---

## Phase 0 — Close the gate gaps (do this before any fix)

The breeder's instruction was explicit: check the final-check skills *before* running any check. Every defect in the brief is a defect the existing gates cannot see. That is the finding.

### Task 0.1: Add the 8 missing checks to the hardening scanner

**Files:**
- Modify: `scripts/page_hardening_scan.py`
- Modify: `skills/cag-page-hardening.md`

Existing checks (verified present): `css-math-spacing`, `bottom-bar-under-tabbar`, `infographic-cropped-mobile`, `fullbleed-grid`, `absolute-hero-not-unwound`, `clay-small-text-contrast`, `opacity-dims-text-contrast`, `img-no-srcset`, `header-not-title-case`, `links-colour-only`, `escaped-svg`, `smooth-scroll-breaks-anchors`.

Missing checks, each traced to a defect that shipped:

| New check | Catches | Shipped defect it would have caught |
|---|---|---|
| `srcset-candidate-oversized` | Smallest srcset candidate > 1.5× the widest displayed CSS box implied by `sizes` | hand-raised hero (620×622 for a 299×348 box, 17.8 KiB waste); dna-tested hero (880×660 for 665×499, 17.1 KiB) |
| `tap-target-spacing` | Adjacent inline-flex nav pills whose gap < 24px minus padding | health-guarantee rail — 28 failing pairs, mobile **and** desktop |
| `form-control-overflow` | Form grid/control that can exceed 100% of a 360px viewport (missing `min-width:0`, `box-sizing`, or `max-width:100%` on `select`/`input`) | health-guarantee contact form cut off on the right at mobile/tablet |
| `font-family-loaded-unused` | A family in the Google Fonts / `@font-face` set that no CSS rule ever resolves to | Lora + Sora, dead on every page for weeks |
| `analytics-double-load` | More than one gtag/GTM container for the same measurement ID in `dist/` + the first-party gateway path | `/70de/` + `googletagmanager.com`, ~327 KiB |
| `deflist-label-not-differentiated` | `<dt>`/label and its `<dd>`/value resolving to the same `color` **and** same `font-weight` | health-guarantee receipt: "Window", "Covered", "Remedy" indistinguishable from their values |
| `line-length-out-of-band` | Body `<p>` whose computed measure falls outside 45–75ch at any of 360 / 768 / 1280 | the breeder's core "text height/width fits well" ask — currently unmeasured at any breakpoint |
| `icon-text-baseline-drift` | Tick/icon + label pair in a flex row without `align-items` set, so the glyph floats off the text baseline | health-guarantee trust ticks "scattered" on mobile |

- [ ] **Step 1: Write the failing test for `srcset-candidate-oversized`**

```python
# tests/test_hardening_srcset_oversized.py
from scripts.page_hardening_scan import check_srcset_oversized

def test_flags_hero_whose_smallest_candidate_dwarfs_its_box():
    html = (
        '<img src="/i/hero.webp" '
        'srcset="/i/hero-320.webp 320w, /i/hero.webp 620w" '
        'sizes="(max-width:980px) 42vw, 158px" width="620" height="720">'
    )
    findings = check_srcset_oversized([("hand-raised", html)])
    assert len(findings) == 1
    assert findings[0]["check"] == "srcset-candidate-oversized"

def test_passes_when_a_candidate_matches_the_mobile_box():
    html = (
        '<img src="/i/hero.webp" '
        'srcset="/i/hero-160.webp 160w, /i/hero-320.webp 320w" '
        'sizes="(max-width:980px) 42vw, 158px" width="620" height="720">'
    )
    assert check_srcset_oversized([("hand-raised", html)]) == []
```

- [ ] **Step 2: Run it and confirm it fails**

Run: `python3 -m pytest tests/test_hardening_srcset_oversized.py -v`
Expected: `ImportError: cannot import name 'check_srcset_oversized'`

- [ ] **Step 3: Implement `check_srcset_oversized`**

Add to `scripts/page_hardening_scan.py`, following the existing `check_img_srcset` signature and return shape (`{"check":…, "page":…, "line":…, "msg":…}`):

```python
SIZES_VW = re.compile(r"(\d+(?:\.\d+)?)vw")
SIZES_PX = re.compile(r"(\d+(?:\.\d+)?)px")

def _widest_mobile_box(sizes: str, viewport: int = 412) -> float:
    """Widest CSS px the image can occupy on a 412px-wide phone (Pixel-class,
    what Lighthouse mobile emulates at DPR 2.625)."""
    first = sizes.split(",")[0]
    vw = SIZES_VW.search(first)
    if vw:
        return viewport * float(vw.group(1)) / 100.0
    px = SIZES_PX.search(first)
    return float(px.group(1)) if px else float(viewport)

def check_srcset_oversized(pages):
    """Flag imgs whose SMALLEST srcset candidate is still far wider than the
    box `sizes` says it renders in. This is the Lighthouse
    'image file is larger than it needs to be' LCP finding."""
    out = []
    for name, html in pages:
        for m in re.finditer(r"<img\b[^>]*>", html, re.I):
            tag = m.group(0)
            if "srcset=" not in tag or "sizes=" not in tag:
                continue  # already covered by check_img_srcset
            sizes = re.search(r'sizes="([^"]+)"', tag).group(1)
            widths = [int(w) for w in re.findall(r"(\d+)w", tag)]
            if not widths:
                continue
            box = _widest_mobile_box(sizes)
            # DPR 2 is the practical ceiling worth serving.
            needed = box * 2
            if min(widths) > needed * 1.5:
                out.append({
                    "check": "srcset-candidate-oversized",
                    "page": name,
                    "line": html[: m.start()].count("\n") + 1,
                    "msg": (
                        f"smallest srcset candidate is {min(widths)}w but the "
                        f"mobile box is ~{box:.0f}px (needs ~{needed:.0f}w). "
                        f"Add a smaller candidate."
                    ),
                })
    return out
```

- [ ] **Step 4: Run the test and confirm it passes**

Run: `python3 -m pytest tests/test_hardening_srcset_oversized.py -v`
Expected: `2 passed`

- [ ] **Step 5: Repeat Steps 1–4 for the remaining 7 checks**

Each follows the identical shape: one test asserting the shipped defect is flagged, one asserting a correct page is not. Write them in this order (cheapest signal first): `tap-target-spacing`, `deflist-label-not-differentiated`, `icon-text-baseline-drift`, `form-control-overflow`, `font-family-loaded-unused`, `analytics-double-load`, `line-length-out-of-band`.

`line-length-out-of-band` cannot be done statically — it needs a real viewport. Implement it as a **runtime probe** in the browser half of `cag-page-hardening`, not in the static scanner. Register it in `skills/cag-page-hardening.md` under the runtime section alongside the existing overflow/contrast probes.

- [ ] **Step 6: Wire all 8 into the scanner's check registry and the skill doc**

- [ ] **Step 7: Run the scanner against the 3 live pages and capture the baseline**

Run: `npx astro build && python3 scripts/page_hardening_scan.py hand-raised-african-grey-parrot-for-sale dna-tested-african-grey-for-sale african-greys-for-sale-with-health-guarantee`
Expected: the new checks reproduce the breeder's hand-found defect list. **If a defect from the brief is not reproduced, the check is wrong — fix the check, not the page.** This is the gate's acceptance test.

- [ ] **Step 8: Commit**

```bash
git add scripts/page_hardening_scan.py skills/cag-page-hardening.md skills/cag-final-page-pass.md tests/
git commit -m "gate(hardening): add the 8 checks that would have caught the for-sale cluster defects

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Phase 1 — Sitewide root causes (fixes all 6 pages at once)

### Task 1.1: Self-host two font families, drop the two dead ones

This single change removes ~200 KB from every page on the site, collapses the critical chain from 3 hops to 1, and eliminates the third-party origin entirely.

**Files:**
- Modify: `src/layouts/BaseLayout.astro:95-107`
- Create: `public/fonts/newsreader-latin-{400,500,600}.woff2`, `public/fonts/newsreader-latin-500-italic.woff2`, `public/fonts/ibm-plex-sans-latin-{400,500,600,700}.woff2`
- Modify: `src/styles/global.css`

- [ ] **Step 1: Confirm Lora and Sora render nowhere**

Run:
```bash
npx astro build && grep -rlE "font-family:\s*['\"]?(Lora|Sora)" dist/ | head
```
Expected: **no output.** If any file matches, stop — a page is overriding Direction-D and dropping the family would change its render.

- [ ] **Step 2: Download latin-subset variable woff2 for the two live families**

```bash
mkdir -p public/fonts
# Newsreader: variable opsz 6..72, wght 400..600, roman + italic, latin subset only
# IBM Plex Sans: static 400/500/600/700, latin subset only
# Pull from the google-webfonts-helper API or the Google CSS with a modern UA,
# then verify each file is latin-only:
python3 - <<'PY'
from fontTools.ttLib import TTFont
import glob
for f in sorted(glob.glob("public/fonts/*.woff2")):
    n = TTFont(f)["cmap"].getBestCmap()
    print(f, len(n), "glyphs")
PY
```
Expected: each file well under the 129–144 KB the unsubsetted variable faces currently cost. Latin subset of Newsreader variable should land ~35–45 KB.

- [ ] **Step 3: Replace the Google Fonts block in `BaseLayout.astro`**

Delete lines 95–107 (`preconnect` + async stylesheet + `noscript` fallback) and replace with two preloads for the faces that paint the hero:

```astro
  <!-- Self-hosted, latin-subset. Only Newsreader + IBM Plex Sans render (direction-d.css
       overrides .font-lora/.font-sora), so Lora and Sora are no longer fetched at all.
       Preloading the two faces that paint above the fold removes the
       HTML -> Google CSS -> woff2 chain that PageSpeed flagged on every page. -->
  <link rel="preload" as="font" type="font/woff2" href="/fonts/newsreader-latin-600.woff2" crossorigin />
  <link rel="preload" as="font" type="font/woff2" href="/fonts/ibm-plex-sans-latin-400.woff2" crossorigin />
```

- [ ] **Step 4: Add the `@font-face` block to `global.css`**

Place it above the existing `Newsreader Fallback` / `IBM Plex Sans Fallback` metric-override declarations in `direction-d.css` so the fallbacks still apply:

```css
@font-face {
  font-family: 'Newsreader';
  src: url('/fonts/newsreader-latin-600.woff2') format('woff2');
  font-weight: 400 600;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215;
}
@font-face {
  font-family: 'Newsreader';
  src: url('/fonts/newsreader-latin-500-italic.woff2') format('woff2');
  font-weight: 400 600;
  font-style: italic;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215;
}
/* IBM Plex Sans 400/500/600/700 follow the identical pattern, one block each. */
```

- [ ] **Step 5: Build and verify the chain is gone**

Run:
```bash
npx astro build
grep -rc "fonts.googleapis.com" dist/ | grep -v ":0" | head
```
Expected: **no output** — zero references sitewide.

- [ ] **Step 6: Commit**

```bash
git add src/layouts/BaseLayout.astro src/styles/ public/fonts/
git commit -m "perf(fonts): self-host latin-subset Newsreader + IBM Plex Sans, drop unused Lora/Sora

Lora and Sora were requested on every page but never rendered - direction-d.css
overrides .font-lora/.font-sora with !important. Removing them plus subsetting
cuts ~200KB and collapses the HTML->CSS->woff2 critical chain PageSpeed flagged
on all six for-sale pages.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 1.2: Stop loading Google Analytics twice

**Files:**
- Modify: `src/layouts/BaseLayout.astro` (the gtag script block)

- [ ] **Step 1: Prove the double-load with a real network trace**

Use the browser tools against the live page and list network requests matching `gtag|70de|googletagmanager`. Record transfer sizes.
Expected: two distinct responses carrying the same `G-MEWJ9GVC4T` container. **If only one fires, stop and re-scope this task** — the Lighthouse table would then be reporting the pre- and post-redirect entries of a single request, and the fix is different.

- [ ] **Step 2: Decide the survivor**

Keep the **first-party gateway** (`/70de/`) and remove the direct `googletagmanager.com` tag. Rationale: first-party serving survives tracking-protection and ad-blockers better, keeps the request on the same H2 connection as the document (no extra DNS + TLS), and is already provisioned. Trade-off, stated honestly: the path is Cloudflare-generated and opaque, so if the breeder ever disables the Google Tag Gateway in the Cloudflare dashboard, analytics stops dead until the direct tag is restored. **That toggle is the breeder's to make — flag it, do not assume it.**

- [ ] **Step 3: Defer the surviving tag off the critical path**

```astro
<!-- GA4 via Cloudflare's first-party Google Tag Gateway. Loaded after first paint so
     ~168KB of analytics never competes with LCP. -->
<script is:inline>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-MEWJ9GVC4T');
  addEventListener('load', () => {
    const s = document.createElement('script');
    s.src = '/70de/';
    s.async = true;
    document.head.appendChild(s);
  }, { once: true });
</script>
```

- [ ] **Step 4: Verify events still fire**

Load `/contact-us/` and confirm the `generate_lead` event still reaches GA4 realtime. **Do not ship this task without that confirmation** — a silent analytics break is worse than a slow page.

- [ ] **Step 5: Commit**

### Task 1.3: Add smooth scrolling, safely

The breeder asked for fluid scrolling on mobile and desktop. Memory `reference_smooth_scroll_kills_jump_links` warns this broke anchors before. It is safe **now** because the pages already set `scroll-margin-top` to clear the header and sticky rail — but that must be confirmed per page, not assumed.

**Files:**
- Modify: `src/styles/global.css`

- [ ] **Step 1: Add the guarded rule**

```css
/* Fluid anchor navigation. Gated on prefers-reduced-motion so it never fights
   a vestibular preference. The horizontal jump-rail scroller keeps
   scroll-behavior:auto so its active-pill auto-scroll stays instant. */
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}
```

- [ ] **Step 2: Confirm every anchor target still clears the chrome**

For each of the 6 pages, click every jump link at 390px and 1280px and confirm the section heading lands below the sticky header + rail, not underneath it.
Expected: no heading obscured. Any page that fails needs its `scroll-margin-top` raised before this ships.

- [ ] **Step 3: Confirm the rail's own horizontal scroll is unaffected**

`.railA ul` already declares `scroll-behavior:auto` — verify the active pill still snaps instantly rather than gliding.

- [ ] **Step 4: Commit**

### Task 1.4: Eliminate the forced reflow

**Files:**
- Modify: the scrollspy `<script>` in each page (e.g. `african-greys-for-sale-with-health-guarantee/index.astro:814`)

The scrollspy reads geometry (`.railA a.on`, then scrolls the rail) on every scroll event. That is a read-after-write in the scroll handler — exactly the "forced reflow" diagnostic, 38–70 ms.

- [ ] **Step 1: Batch the read and the write into one `requestAnimationFrame`, and passive-listen**

```js
let queued = false;
addEventListener('scroll', () => {
  if (queued) return;
  queued = true;
  requestAnimationFrame(() => {
    queued = false;
    // all geometry READS first
    const chip = document.querySelector('.railA a.on');
    if (!chip) return;
    const left = chip.offsetLeft, width = chip.offsetWidth;
    // then all WRITES
    rail.scrollTo({ left: left - width, behavior: 'auto' });
  });
}, { passive: true });
```

- [ ] **Step 2: Re-trace and confirm reflow time drops**

Expected: forced-reflow entry falls below 10 ms or disappears. Honest caveat: Lighthouse attributes this to `[unattributed]`, so some residual may come from third-party analytics and will not clear. It is an unscored diagnostic either way.

- [ ] **Step 3: Commit**

---

## Phase 2 — Per-page LCP image fixes

### Task 2.1: hand-raised hero — add a mobile-sized candidate

**Files:** `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro`

Current: `sizes="(max-width:980px) 42vw, 158px"`, smallest candidate 320w, rendering into a 299×348 box. Lighthouse: 17.8 KiB wasted.

- [ ] **Step 1: Generate a 176w and a 352w candidate** with the project's Pillow pipeline (`method=6`, quality-walk to <100 KB, per `IMAGE-DESIGNS.md §1a`)
- [ ] **Step 2: Add them to `srcset`; leave `sizes` alone** — `sizes` is correct, the candidate ladder was not
- [ ] **Step 3: Mirror the new `srcset`/`sizes` into `heroPreloadSrcset`/`heroPreloadSizes`** so the preload scanner picks the same candidate (this is exactly what `BaseLayout.astro:22-23` warns about)
- [ ] **Step 4: Re-run `page_hardening_scan.py`** — expect `srcset-candidate-oversized` to clear
- [ ] **Step 5: Commit**

### Task 2.2: dna-tested hero — same treatment

`sizes="(max-width:980px) 92vw, 420px"`, smallest candidate 440w into a 665×499 box. Same five steps; candidates at 400w and 800w.

---

## Phase 3 — Per-page UI and accessibility defects

### Task 3.1: `.faqA-n` contrast (dna-tested)

`index.astro:1076` sets `color: var(--clay-ink)` (#c8472f) at `.68rem` — 10.9px. That is 4.78:1 on pure white, which passes, but the `<summary>` sits on a tinted surface, dropping it below 4.5:1.

- [ ] **Step 1: Measure the actual computed pair at runtime** — do not guess the background
- [ ] **Step 2: Switch to `#b04228`** (the project's established small-clay-on-light token, per `reference_aa_contrast_and_perf_fixes`) and re-measure
- [ ] **Step 3: Confirm ≥4.5:1 and that the axe failure clears**
- [ ] **Step 4: Commit**

### Task 3.2: Tap-target spacing on the health-guarantee jump rail

`index.astro:1109` — `gap:7px` between pills that are `min-height:36px`. Size passes; **spacing** fails, 28 pairs, on mobile and desktop.

- [ ] **Step 1: Raise the gap to 12px and the pill padding to `8px 16px`**, giving ≥24px of non-overlapping target
- [ ] **Step 2: Confirm the rail still fits without wrapping** at 360px — it is an `overflow-x:auto` scroller, so extra width is acceptable, but the first pill must still be fully visible
- [ ] **Step 3: Re-run the axe target-size audit** — expect 0 failures
- [ ] **Step 4: Apply the same metric to the desktop dial** (it fails too, per the desktop report)
- [ ] **Step 5: Commit**

### Task 3.3: Receipt component — differentiate the labels

The breeder likes the component; the labels "Window / Covered / Remedy / Voided by / Confirmed by / From" are the same colour and weight as their values, so it reads as one grey block.

- [ ] **Step 1: Give the labels a distinct treatment** — `color: var(--green-d)`, `font-weight:700`, `font-size:.72rem`, `letter-spacing:.04em`, and `text-transform:none` (Title Case is already correct and these are not headings, so the Title Case rule does not apply — they live in a `<dt>`)
- [ ] **Step 2: Verify ≥4.5:1 against the receipt's surface**
- [ ] **Step 3: Check it at 360 / 768 / 1280** — the label column must not orphan a single word
- [ ] **Step 4: Commit**

### Task 3.4: Trust-tick row alignment on mobile

"72-hour written guarantee / Avian-vet examined / DNA-sexed, certificate included / CITES" reads as scattered on mobile.

- [ ] **Step 1: Convert the row to a two-column grid at ≤560px** — `grid-template-columns: 1rem 1fr`, `align-items: start`, tick in column 1, label in column 2, so multi-line labels stay hanging-indented under themselves rather than wrapping beneath the tick
- [ ] **Step 2: Set `line-height:1.45` and a consistent `row-gap:.6rem`**
- [ ] **Step 3: Screenshot at 360 / 390 / 430** and confirm the ticks form a clean vertical rule
- [ ] **Step 4: Commit**

### Task 3.5: Health-guarantee contact form — mobile/tablet overflow

`index.astro:761-789`. The form pairs fields in a row (`first-name`/`last-name`, `cell`/`email`) and includes two `<select>`s whose option text is long ("Which grey are you asking about?").

- [ ] **Step 1: Reproduce at 390px and 768px and identify the overflowing node** — check `min-width:0` on the grid children first; a CSS grid child defaults to `min-width:auto`, which refuses to shrink below its content and is the single most common cause of exactly this symptom
- [ ] **Step 2: Apply `min-width:0` to the grid children and `max-width:100%; box-sizing:border-box` to every control**
- [ ] **Step 3: Collapse the paired rows to one column at ≤640px**
- [ ] **Step 4: Set `font-size:16px` on all inputs/selects** — anything smaller triggers iOS Safari's auto-zoom, which is very likely what the breeder is seeing as "too zoomed that it's cut off"
- [ ] **Step 5: Verify zero horizontal document overflow** — `document.documentElement.scrollWidth <= window.innerWidth` at 360/390/430/768
- [ ] **Step 6: Commit**

### Task 3.6: dna-tested contact-form button arrow

- [ ] **Step 1: Reproduce and identify** — most likely an `&rarr;` inside a flex button without `align-items:center`, or a pseudo-element arrow inheriting a serif face from the Newsreader heading override
- [ ] **Step 2: Fix by putting the arrow in an inline `<svg>` in the markup** — never in CSS `content:` (that is a standing project ban and it collapses spacing)
- [ ] **Step 3: Commit**

### Task 3.7: Mid-page newsletter refinement (all 3 pages, mobile + desktop)

Flagged on all three pages. This is a design task, not a bug fix, so it goes through the visual-companion gate.

- [ ] **Step 1: Screenshot the current newsletter on all 3 pages at 390 / 768 / 1280**
- [ ] **Step 2: Build a visual-companion comparison of 3 refinement directions**, each with a Recommended marker, a data-grounded why, and a named trade-off
- [ ] **Step 3: Get the breeder's pick before writing any page code**
- [ ] **Step 4: Implement the approved direction on all 3 pages, differentiated per page** via `cag-component-refresh` so the siblings do not render identically
- [ ] **Step 5: Commit**

---

## Phase 4 — The impeccable typography and fit pass (all 6 pages, 3 breakpoints)

This is the breeder's central ask and it has never been measured. Everything above is defect repair; this is the craft pass.

- [ ] **Step 1: Capture the measure, line-height, and heading scale** of every text block on all 6 pages at 360 / 768 / 1280 using the new `line-length-out-of-band` runtime probe
- [ ] **Step 2: Bring every body paragraph into 45–75ch**, per the project's existing `max-width:70ch` rule and impeccable's 65–75ch law
- [ ] **Step 3: Verify the heading scale keeps ≥1.25 ratio between steps** at every breakpoint, and that no `clamp()` inverts the H2→H3→H4 ordering (a known project trap — the `vw` term decides ordering, so resolve `var()` before sweeping)
- [ ] **Step 4: Check tablet specifically** — it is the breakpoint the brief calls out and the one most likely to be untested, since the pages were built mobile-first then desktop-verified
- [ ] **Step 5: Run `critique` and `polish` from the impeccable skill** over each page and action the findings
- [ ] **Step 6: Commit per page**

---

## Phase 5 — Eggs and breeding-pair cross-sell (not full sections)

The reasoning behind this scoping decision is in the response accompanying this plan. Summary: full eggs/breeding-pair *sections* on all 6 pages would cannibalise the three dedicated pages that already exist and trip the duplicate-content gate six ways. Cross-links plus an FAQ entry capture the same queries without hijacking each page's intent.

- [ ] **Step 1: Add one FAQ entry per page** answering the eggs question and the breeding-pair question, written fresh per page from that page's own angle — never pasted between siblings
- [ ] **Step 2: Add a compact cross-sell block** before the final CTA linking `/african-grey-parrot-bird-eggs-for-sale-usa/`, `/african-grey-breeding-pair-for-sale/`, `/congo-african-grey-parrot-pair-for-sale/`
- [ ] **Step 3: Rotate the anchor text** per the Anchor Diversity Ledger — no two pages use the same anchor for the same target — with each anchor at the START of its sentence per the Link-First rule
- [ ] **Step 4: Give dna-tested a genuine, page-specific pair passage** — a proven breeding pair is the strongest real-world case for DNA sexing, so this one earns more than a link
- [ ] **Step 5: Run `scripts/dup_content_audit.py` and `--headers`** across all 6 — target zero non-whitelist crossover
- [ ] **Step 6: Commit**

---

## Phase 6 — Apply everything to the remaining 3 pages

`/african-grey-parrot-bird-eggs-for-sale-usa/`, `/congo-african-grey-for-sale/`, `/timneh-african-grey-for-sale/`.

Phase 1 already fixed their fonts, analytics, scroll and reflow. What remains is per-page:

- [ ] **Step 1: Run the upgraded `page_hardening_scan.py` on all 3** and fix what it reports
- [ ] **Step 2: Run Lighthouse mobile + desktop on all 3** and close any remaining LCP image gaps
- [ ] **Step 3: Apply Phase 4's typography pass**
- [ ] **Step 4: Apply Phase 5's cross-sell**
- [ ] **Step 5: Commit per page**

---

## Phase 7 — Verify and ship

- [ ] **Step 1: `npx astro build`** — clean
- [ ] **Step 2: `python3 scripts/page_hardening_scan.py` on all 6** — zero findings
- [ ] **Step 3: `python3 scripts/final_page_audit.py` on all 6** — PASS
- [ ] **Step 4: `python3 scripts/dup_content_audit.py` + `--headers`** — zero non-whitelist crossover
- [ ] **Step 5: Lighthouse mobile + desktop, warm median-of-3, on all 6** — report the real numbers, including any that fall short
- [ ] **Step 6: `bash scripts/health-sweep.sh`** — PASS
- [ ] **Step 7: `python3 scripts/generate_sitemaps.py`** — zero phantoms
- [ ] **Step 8: Commit and `git push origin main`** — push is deploy

---

## Known limits, stated up front

1. **"Missing source maps" will never clear.** It is Google's analytics code. Unscored, informational, permanent.
2. **100/100 mobile is not guaranteed while any third-party analytics loads.** Deferring GA gets most of the way; if the number still falls short of 100, the remaining lever is removing GA from the critical path entirely (server-side tagging or Cloudflare Web Analytics), which is a business decision about measurement fidelity, not a code fix. It will be presented with real numbers, not promised in advance.
3. **The Google Tag Gateway toggle lives in the Cloudflare dashboard**, not in this repo. Task 1.2 depends on it staying on.
4. **Competitor gap analysis is not in this plan.** It needs a live `@cag-competitor-intel` run against the current SERP; findings would change scope, so it is sequenced after Phase 7 as its own piece of work rather than guessed at now.

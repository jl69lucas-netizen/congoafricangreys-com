---
name: cag-page-hardening
description: Use when a CAG page is built but feels rushed, or before any deploy/final pass, or when the breeder reports a page looks wrong on mobile/desktop — zoomed images, broken or overlapping hero art, a jump-rail that does nothing, buttons that wrap or stretch, text cut off at the screen edge, headings that ignore their CSS, or Lighthouse contrast / link-distinguishability / image-delivery flags. Runs an automatic scan for every UI/UX/perf/a11y defect class that has actually shipped on this site, then applies the banked fix for each. Triggers: "harden this page", "polish the UI", "fix the mobile view", "why is this cut off", "sweep the contrast fix", "make it modern/clean", final-pass QA.
---

# SKILL: CAG Page Hardening (v1.0 — 2026-07-23)

**Why this exists.** The same UI defects keep reaching production because they are
invisible in source review — the CSS *looks* right. Each one below was found the
expensive way: the breeder spotted it on a phone after deploy. This skill turns
every one of them into a check that runs automatically.

**Run this BEFORE `cag-final-page-pass`.** That skill audits structure, schema and
SEO; this one audits whether the page actually *renders* correctly.

---

## 0. The one-command scan

```bash
python3 scripts/page_hardening_scan.py <slug>
```

`ERROR` = shipped-broken, fix before deploy. `WARN` = very likely wrong, eyeball it.
Omit the slug to sweep the whole site. Add `--fail-on-error` for CI.

The scanner covers everything statically detectable. Three defects can only be
caught at runtime — run §Runtime below in the browser as well. **Both halves are
required**; the static scan alone would have missed the two worst bugs of
2026-07-23.

---

## 1. Static defect catalogue (what the scanner knows)

### 1a. `css-math-spacing` — ERROR — *the silent heading-size killer*
`clamp(1.7rem,1.2rem+2.2vw,2.6rem)` is **invalid CSS**. Math functions require
whitespace around `+` and `-`. Without it the entire declaration is dropped and
the element falls back to the global rule — so `h1` renders at 48px while the
source says 2.26rem, and nothing in the file looks wrong.

> **Real cost:** the hand-raised hero was 524px instead of ~400px for its whole
> first week live. Two rounds of "make the hero shorter" edits did nothing
> because the rule was never applied. Same bug found on `/available/`.

**Fix:** `clamp(1.5rem, 1.02rem + 1.55vw, 1.98rem)`.
**Verify:** `getComputedStyle(h1).fontSize` matches the clamp, not the global token.

### 1b. `bottom-bar-under-tabbar` — ERROR — *"the jump-rail is broken"*
The global `MobileTabBar` is `fixed bottom-0 … z-50`. Any other bottom-pinned UI
at `bottom:0` with a lower z-index renders **underneath it** and looks like dead
code. It isn't broken; it's buried.

**Fix — do NOT pin it to the bottom at all.** The breeder rejected bottom
placement outright (2026-07-23): even correctly stacked above the tab bar it
"interferes with the page's bottom view". **Mobile jump-rails go at the TOP**,
sticky under the header, matching every sibling for-sale page
(`.chero-rail`, `.egg-rail`):

```css
.railB{position:sticky; top:var(--hdr); z-index:40;
  background:rgba(250,247,244,.985);      /* cream — a green bar merges into the header */
  border-bottom:1px solid var(--bd);
  box-shadow:0 6px 14px rgba(60,30,10,.07);}
```

Differentiate per page with the **chip** treatment, not the bar position
(siblings use single-line pills; hand-raised uses stacked two-line chips).
Scroll the active chip into view on scroll-spy so the rail tracks the reader.

**`--hdr` must equal the REAL header height (96px).** It was defaulting to 72px,
which parked the sticky desktop dial 8px *behind* the header. Anchors then need
`scroll-margin-top: calc(var(--hdr) + 16px)` on desktop and
`calc(var(--hdr) + 74px)` on mobile (header + rail + gap) — verify by clicking a
rail chip and confirming the H2 lands below the rail, not under it.

### 1c. `infographic-cropped-mobile` — ERROR — *unreadable infographics*
Infographics carry **baked-in text**. Forcing a 16:9 infographic into a 5:4 or 4:5
mobile box with `object-fit:cover` shaves ~30% off **each side** and cuts the words.

**Fix — split the two image classes; they are not the same thing:**
```css
/* infographics: native ratio, never cover-cropped */
.sec-img.inf-img{width:100vw;margin-left:calc(50% - 50vw);
  aspect-ratio:1408/768;object-fit:contain;background:#fff;}
/* real OG photos: the taller mobile frame (IMAGE-DESIGNS §7) */
.sec-img.og-photo{aspect-ratio:5/4;object-fit:cover;}
```

### 1d. `absolute-hero-not-unwound` — WARN — *overlapping / collapsing hero art*
Absolutely-positioned hero art with `%` widths overlaps on desktop (covering the
birds' faces) and collapses to slivers on mobile.

**Fix — do not tune the offsets; remove the mechanism.** Lay hero art out as a
grid and get the "scatter" from rotation, so overlap is structurally impossible:
```css
.hero-scatter{display:grid;grid-template-columns:1fr 1fr;gap:9px 8px;place-items:center;}
.pofig{position:relative;width:100%;max-width:148px;}
.pofig.p1{transform:rotate(-4deg) translateY(-5px);}   /* alternate per card */
```
Captions/badges pinned *inside* a card stay absolute — that's correct, and the
scanner ignores them.

### 1e. `clay-small-text-contrast` / `opacity-dims-text-contrast` — WARN
Brand `--clay #e8604c` is AA **only as large text** (3.38:1). Small clay text on
light must be `#b04228`; solid clay fills use `--clay-ink #c8472f`. Separately,
any `opacity` on a text rule silently drags contrast down — `opacity:.9` white on
`#c8472f` measures **4.10** against a 4.5 floor.

### 1e-bis. Desktop dial TOC — the CANONICAL row metrics (cluster-wide, LOCKED)
The breeder rejected a "density pass" that shrank rows to `.7rem` / `3.5px 6px`
with the tag hidden: *"I can hardly read the text or click."* **Readability beats
compactness** — the card scrolls internally if it ever runs long.

**Every for-sale / comparison desktop dial matches `/timneh-african-grey-for-sale/`
(`.tdial`) exactly.** Copy these numbers verbatim; only the palette changes per
page tuple (light-cream card vs dark-aviary card):

```css
/* sidebar column */   grid-template-columns:196px minmax(0,1fr); gap:28px;
/* card  */ display:flex;flex-direction:column;gap:10px;align-items:stretch;
            border-radius:16px;padding:12px 10px;
            position:sticky;top:calc(var(--hdr) + 16px);
            max-height:calc(100vh - var(--hdr) - 32px);overflow-y:auto;
/* ring  */ 64px outer · 50px inner · number 15px serif · "of N" 7px · margin:2px auto 0;flex:none
/* list  */ display:grid;grid-template-columns:1fr;gap:1px;
            border-top:1px dashed;padding-top:8px;
/* row   */ display:flex;gap:7px;align-items:baseline;
            font-size:.74rem;line-height:1.25;padding:5px 7px;border-radius:8px;
/* num   */ font-size:.7rem;width:16px;flex:none;font-weight:700;font-variant-numeric:tabular-nums;
/* tag   */ margin-left:auto;font-size:.56rem;font-weight:600;
            color:#fff;background:var(--clay-ink);border-radius:50px;padding:1px 6px;white-space:nowrap;
```

**The tag pill is always visible** — hiding it on inactive rows was part of the
rejected density pass. Verify: 18 rows ⇒ card ≈ **705–725px**, every row ≥ 24px
tall (WCAG 2.5.8), label ≥ 4.5:1.

**Dial/rail contrast — two variants, do NOT mix them up:**

| Dial variant | Background | Numerals | Ratio |
|---|---|---|---|
| **Light card** (congo, timneh) | cream `#fff` | `#6b625a` | 5.9:1 ✓ |
| **Dark aviary** (hand-raised) | `#234f3b` | `#9fc7b0` | 5.0:1 ✓ |
| Mobile rail `.p` | `#234f3b` | `#c9f2db`, **no opacity** | 5.4:1 ✓ |

Applying the light-card `#6b625a` to a dark dial makes it unreadable. Always
check which variant the page ships before "sweeping the contrast fix".

### 1f. `links-colour-only` — WARN — WCAG 1.4.1
In-body links distinguished by colour alone fail Lighthouse.
```css
.content p a,.content li a{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px;}
.content p a.btn,.content a.geo-card,.content a.read-card{text-decoration:none;}
```

### 1g. `img-no-srcset` — WARN — image-delivery savings
Any image whose intrinsic width is far above its rendered width. Ship siblings and
a real `sizes`:

| Slot | Rendered | Ship | `sizes` |
|---|---|---|---|
| Hero polaroid | ~150px | `-320` | `(max-width:980px) 42vw, 158px` |
| Bird card | ~226px | `-440` | `(max-width:640px) 46vw, 226px` |
| Read-card thumb | 120px | `-240` | `120px` |
| In-body infographic | 760px | `-760` | `(max-width:900px) 92vw, 760px` |

> Real cost: 163 KiB flagged on hero polaroids (620×720 shown at ~200px) plus
> 760px thumbnails rendered into a 120px slot.

### 1h. Known render traps (already banked in MEMORY, re-checked here)
`svg-in-css-content` · `escaped-svg` (missing `set:html`) · `user-select-none`
(banned site-wide) · `smooth-scroll-breaks-anchors`.

---

## 2. Runtime probes (§Runtime — the static scan CANNOT catch these)

Build, open the page in the preview browser, then run each probe. These are the
checks that caught the two worst bugs of 2026-07-23.

### 2a. Horizontal overflow at 375px — *text cut off at the screen edge*
A `width:100vw` full-bleed child inflates the `1fr` grid track that **contains**
it (a `1fr` track sizes to min-content = the viewport), so the text column grows
past the container padding and body copy runs off-screen. Which grid is at fault
is a runtime property — no static rule can find it without drowning in false
positives.

```js
(()=>{const bad=[...document.querySelectorAll('main *')]
  .filter(e=>e.getBoundingClientRect().right>innerWidth+1)
  .slice(0,8).map(e=>e.tagName+'.'+(e.className||'').toString().slice(0,34));
 return JSON.stringify({scrollW:document.documentElement.scrollWidth,vw:innerWidth,offenders:bad})})()
```
`scrollW` must equal `vw` and `offenders` must be empty (full-bleed images
legitimately reach exactly `vw`).

**Fix:** `grid-template-columns:minmax(0,1fr)` + `min-width:0` on the content column.

> Note: `overflow-x:clip` on the page root **hides** this — `scrollWidth` still
> reads 375 while text is being clipped. Always check element right-edges too.

### 2b. Full-page contrast sweep
```js
(()=>{const lum=c=>{const[r,g,b]=c.map(v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)});return 0.2126*r+0.7152*g+0.0722*b};
const parse=s=>s.match(/[\d.]+/g).map(Number).slice(0,3);
const bgOf=e=>{let n=e;while(n){const b=getComputedStyle(n).backgroundColor;if(b&&!/rgba\(0, 0, 0, 0\)|transparent/.test(b))return parse(b);n=n.parentElement}return[255,255,255]};
const ratio=(a,b)=>{const l1=lum(a),l2=lum(b);return +(((Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05)).toFixed(2))};
const fails=[];document.querySelectorAll('main *').forEach(e=>{
 if(e.closest('video'))return;                      // <video> fallback never renders
 if(![...e.childNodes].some(c=>c.nodeType===3&&c.textContent.trim().length>1))return;
 const cs=getComputedStyle(e);if(cs.display==='none'||cs.visibility==='hidden'||+cs.opacity===0)return;
 const size=parseFloat(cs.fontSize),bold=parseInt(cs.fontWeight)>=700;
 const need=(size>=24||(size>=18.66&&bold))?3:4.5;
 const r=ratio(parse(cs.color),bgOf(e));
 if(r<need)fails.push({el:e.tagName+'.'+(e.className||'').toString().slice(0,30),txt:e.textContent.trim().slice(0,30),ratio:r,need})});
 return JSON.stringify({failures:fails.length,fails:fails.slice(0,10)},null,1)})()
```
Target **0 failures**. Skip `<video>` fallback text — it is never rendered.

### 2c. Component sizing sanity
```js
(()=>{const r=e=>Math.round(e.getBoundingClientRect().height),w=e=>Math.round(e.getBoundingClientRect().width);
 const dial=document.querySelector('.dial-card');
 return JSON.stringify({vw:innerWidth,
  hero:r(document.querySelector('header.hero, .hero')),      // target 350-400 desktop
  h1:getComputedStyle(document.querySelector('h1')).fontSize, // must match the clamp
  dialH:dial&&r(dial), dialScrolls:dial&&dial.scrollHeight>dial.clientHeight,
  cardH:[...document.querySelectorAll('.bcard')].map(r),      // must be uniform
  btnW:[...document.querySelectorAll('.bfull')].map(w),       // must hug, not stretch
  btnLines:[...document.querySelectorAll('.bfull')].map(b=>Math.round(r(b)/20))})})() // 1 line each
```

**Targets:** hero 350–400px desktop · `h1` honours its clamp · dial fits without
inner scroll at 900px height · card heights uniform (±2px) · card CTAs hug their
label and never wrap.

---

## 3. Fix order (dependencies matter)

1. **`css-math-spacing` first.** Until the clamps are valid, every sizing
   measurement you take is measuring the fallback, and every "make it smaller"
   edit is a no-op. This wasted a full round-trip on 2026-07-23.
2. Layout mechanism next (absolute → grid), then sizing.
3. Overflow (§2a) before any visual judgement — a clipped page misleads every
   other check.
4. Contrast and link affordances.
5. Image delivery last (it does not affect layout).

---

## 4. Standing component rules confirmed by the breeder

- **Bird card CTA:** `Reserve <name> →`, `white-space:nowrap`, `align-self:start`
  on desktop (hug) / `stretch` on mobile, `margin-top:auto` so every card's button
  shares a baseline. Never a stretched 200px pill with empty space.
- **Card badge:** bottom-left over a `linear-gradient` scrim — pinned top-left it
  lands on the bird's head.
- **Name/price row:** `grid-template-columns:minmax(0,1fr) auto` with
  `white-space:nowrap` on the price, so a wrapping name never shoves the price.
- **Seam divider:** framed, not floating — two clay hairlines flanking a ~34px
  wordmark, plus a clay `h2::before` tick so sections visibly separate.
- **Hero trust chips:** 2×2 grid on desktop, **1 column** on mobile. `nowrap`
  chips in 2 mobile columns overflow a 343px content box and drag the whole hero
  column wide.

---

## 5. Handoff

Clean scan + clean runtime probes → `skills/cag-final-page-pass` → deploy.
Anything this skill could not fix in code (e.g. **Cloudflare Rocket Loader**
`/70de/` unused-JS and its missing source map — a dashboard toggle under
Speed → Optimization) goes to `docs/reference/technical-seo-fixes-backlog.md`
and is reported to the breeder, never silently dropped.

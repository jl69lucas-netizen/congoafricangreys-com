# Breeding-Pair Page — Finish & Impeccable Pass Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Take `/african-grey-breeding-pair-for-sale/` from "shipped but rough" to done — new breeder-approved OG + bird-card image styles, the missing visual components (egg image, singles cards), two re-baked infographics, a real named review, two mobile caption defects, a confirmed AA contrast failure, a new Lighthouse/PageSpeed measurement gate, and the Sprint 5/6 close-out.

**Architecture:** Five phases. Phase A produces *previews only* and stops at a breeder gate, because the OG style and bird-card style choices are the breeder's call and everything in Phase B depends on which style wins. Phase B lands content and structure. Phase C is the impeccable/frontend polish + a11y. Phase D builds the perf gate that does not exist yet. Phase E closes the sprint. Phases B and D have no dependency on the Phase A gate and may run while the breeder reviews.

**Tech Stack:** Astro 5 → `dist/`, Pillow (`scripts/reframe_og.py`), Playwright render harness (`tests/render/`), Lighthouse via `chrome-devtools` MCP, Cloudflare Pages on push to `main`.

---

## Verified Starting State

Every claim below was confirmed against the working tree on 2026-08-07, not inferred.

| Fact | Evidence |
|---|---|
| Page is live and fully shipped | `git log origin/main..HEAD` → empty; all 29 referenced images exist in `public/images/breeding-pair/` |
| Only dirty files are unrelated | `git status` → `.claude/launch.json`, 2 deleted brand assets |
| `inf-2` + `inf-7` masters were regenerated today | masters `Aug 7 12:34` / `12:41`; shipped `.webp` `Aug 4 01:20` — **stale** |
| Page uses exactly one OG style | `grep -c og-photo` → 8, all `blurfill`; `grep -c og-tall` → **0** |
| Styles C / D / H have never been built | `grep -rln "editorial-split\|portrait-frame\|duo-strip\|h-im" src/` → no matches |
| `§singles` has zero bird cards | `index.astro:657-682` is prose + one figure + one `.xsell` |
| Fertile-egg master unused | `assets/.../fertile-grey-parrot-egg-for-sale.jpg` appears in no build script or metadata brief |
| `§singles` never links the egg page | no `/african-grey-parrot-bird-eggs-for-sale-usa/` anywhere in the section |
| `§reviews` explicitly promises no quotes yet | `index.astro:723` — "When we have named quotes we can stand behind, they will go here" |
| No perf/Lighthouse gate exists | `package.json` scripts = dev/start/build/preview/test:render{,:meta,:pages,:report} only; `ls skills/ \| grep -i "light\|perf\|speed"` → empty |

### Root cause 1 — both mobile caption defects are one rule

`index.astro:1310` lists the elements forced to `display:block` for mobile table stacking:

```css
.bpair .tH, .bpair .tH thead, .bpair .tH tbody, .bpair .tH th, .bpair .tH td, .bpair .tH tr { display:block; }
```

`caption` is **not in that list**. It keeps `display:table-caption` (set at `index.astro:1242`) inside a table whose every other child is now a block, so the browser shrink-to-fits it into a narrow column — the tall green strip with dead white space beside it in both screenshots. It is the same rule for `Production Record` (`:433`) and `The four housing specifications` (`:573`). One fix repairs both, and every future `.tH` caption on the site.

### Root cause 2 — the 10 `.ti` contrast failures are a light-theme override gap

- `index.astro:966` → `.ti { color:#7ba98d; }` (sage, written for the dark dial)
- `index.astro:1194` → `.bpair .tdial { background:#fff; }` (this page flips the dial to white)
- `index.astro:1203` overrides `.ti` **only** in the `.on` state — the 17 inactive `.ti` never get a light-theme colour.

`#7ba98d` on `#ffffff` = **2.66:1**. Fails AA 4.5:1. This is the [markup↔CSS drift](../../../.claude/projects/-Users-apple-Downloads-CAG/memory/reference_markup_css_drift.md) pattern: the component was re-themed, the child was not.

### Not actionable — the source-map finding

Lighthouse's "large first-party JavaScript is missing a source map" points at `/70de/`. That path is **Cloudflare Rocket Loader**, injected at the edge, not built from this repo. It is an **Unscored** Lighthouse item and cannot be fixed by a code change. If it must go away, toggle Rocket Loader off in the Cloudflare dashboard (Speed → Optimization). No task is planned for it; Task 12 asserts it as a known-ignored item so no future run re-litigates it.

### Open Flag — the review names "Mart", the breeder is "Mark"

The supplied quote says *"working with Mart and Teri"* and *"the professionalism and care Mart and Teri showed"*. The breeder of record everywhere on this site is **Mark** Benjamin. Task 4 ships it as **Mark** (treating it as a transcription slip, not the buyer's word) and logs the flag. See the single question at the end of this plan.

---

## File Structure

| File | Responsibility | Action |
|---|---|---|
| `scripts/reframe_og.py` | OG framing engine — gains 3 baked styles + `--tint` + `--fgscale` | Modify |
| `scripts/make_og_previews.py` | Renders the style-comparison preview page | Create |
| `sessions/2026-08-07-og-style-preview.html` | Breeder-facing OG preview (desktop/tablet/mobile) | Create |
| `sessions/2026-08-07-birdcard-style-preview.html` | Breeder-facing bird-card preview | Create |
| `src/components/cag-library/MiniBirdCard.astro` | Reusable small bird card — the component this page was missing | Create |
| `src/pages/african-grey-breeding-pair-for-sale/index.astro` | The page | Modify |
| `scripts/perf_audit.py` | The new Lighthouse/PageSpeed gate | Create |
| `skills/cag-perf-gate.md` | Skill wrapping the gate + the fix bank | Create |
| `tests/render/checks/a11y.ts` | New harness family — contrast on rendered pages | Create |
| `tests/render/fixtures/known_broken/tdial-contrast.html` | Meta-gate fixture proving the check catches the real bug | Create |
| `rules/design.md`, `CLAUDE.md`, `rules/for-sale.md` | The two new rules the breeder called out | Modify |
| `data/quality/rule-index.json` | Register both new rules as `test` | Modify |
| `skills/cag-learning-loop.md` | Bank the MiniBirdCard + caption-stacking lessons | Modify |

---

# PHASE A — Breeder-Gated Visual Decisions

Produces previews only. **Writes nothing to the page.** Ends at a hard gate.

## Task 1: Three New Baked OG Styles + Preview

**Why these three:** `reframe_og.py` currently ships `blurfill`, `contain`, `topcover`. Styles **C (Editorial Split)**, **D (Portrait Frame)** and **H (Duo Strip)** are documented in `IMAGE-DESIGNS.md §7` but have never been built anywhere on the site — they are the genuinely unused ones. They are CSS components, not baked files, so they cannot answer "make the bird bigger in the baked image". The three new *baked* styles below do, and each carries a `--tint` flag so the breeder keeps the greyish/black bed **and** gains CAG-palette beds on desktop, tablet and mobile.

**Files:**
- Modify: `scripts/reframe_og.py:40-105`
- Create: `scripts/make_og_previews.py`
- Create: `sessions/2026-08-07-og-style-preview.html`

- [ ] **Step 1: Add the tint helper and the three new style functions**

Insert into `scripts/reframe_og.py` immediately after `def gradient(W, H):`'s closing `return g` (currently line 60):

```python
# CAG palette beds. "neutral" reproduces today's greyish/black blur so every new
# style keeps the old look as an option; the rest tint toward DESIGN.md colours.
TINTS = {
    "neutral": None,                 # no tint — the current greyish bed
    "green":   (45, 106, 79),        # #2D6A4F  brand green
    "clay":    (232, 96, 76),        # #e8604c  brand clay
    "cream":   (250, 247, 244),      # #faf7f4  page surface
}

def apply_tint(bed, tint, strength):
    """Blend a blurred bed toward a brand colour without flattening it to a swatch."""
    rgb = TINTS.get(tint)
    if rgb is None:
        return bed
    wash = Image.new("RGB", bed.size, rgb)
    return Image.blend(bed, wash, strength)

def brandblur(im, W, H, blur, fgw, fgh, tint, strength, fgscale, fgup=False):
    """Style F — thin brand-tinted blur bed, subject scaled UP to fill the frame."""
    bed = ImageOps.fit(im, (W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(blur))
    bed = ImageEnhance.Brightness(bed).enhance(0.95)
    bed = apply_tint(bed, tint, strength)
    fg = fit_subject(im, int(fgw * fgscale), int(fgh * fgscale), True)
    canvas = bed.copy()
    canvas.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    return canvas

def duotone(im, W, H, fgw, fgh, tint, strength, fgscale, fgup=False):
    """Style G — no blur at all. Subject over a clean two-stop brand wash."""
    rgb = TINTS.get(tint) or (243, 236, 228)
    top = tuple(min(255, int(c + (255 - c) * 0.72)) for c in rgb)
    bed = Image.new("RGB", (W, H))
    px = bed.load()
    for y in range(H):
        t = y / (H - 1)
        row = tuple(int(top[i] + (rgb[i] - top[i]) * t * strength) for i in range(3))
        for x in range(W):
            px[x, y] = row
    fg = fit_subject(im, int(fgw * fgscale), int(fgh * fgscale), True)
    bed.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    return bed

def framed(im, W, H, blur, fgw, fgh, tint, strength, fgscale, fgup=False):
    """Style I — thin blur bed + inset brand hairline. Subject biggest of the three."""
    bed = ImageOps.fit(im, (W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(blur))
    bed = ImageEnhance.Brightness(bed).enhance(0.90)
    bed = apply_tint(bed, tint, strength)
    fg = fit_subject(im, int(fgw * fgscale), int(fgh * fgscale), True)
    canvas = bed.copy()
    canvas.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    line = TINTS.get(tint) or (45, 106, 79)
    d = ImageDraw.Draw(canvas)
    inset = max(6, W // 120)
    d.rectangle([inset, inset, W - inset - 1, H - inset - 1], outline=line, width=max(2, W // 470))
    return canvas
```

- [ ] **Step 2: Import ImageDraw**

Replace line 22 of `scripts/reframe_og.py`:

```python
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
```

with:

```python
from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageDraw
```

- [ ] **Step 3: Wire the new styles and flags into the CLI**

Replace line 84 (`ap.add_argument("--style", ...)`) with:

```python
    ap.add_argument("--style", default="blurfill",
                    choices=["blurfill", "contain", "topcover", "brandblur", "duotone", "framed"])
    ap.add_argument("--tint", default="neutral", choices=["neutral", "green", "clay", "cream"])
    ap.add_argument("--tint-strength", type=float, default=0.28)
    # The breeder's note: "birds appear too small". 0.82 was the effective old value.
    ap.add_argument("--fgscale", type=float, default=0.94)
```

Then replace the dispatch dict (lines 100-102) with:

```python
    fn = {"blurfill":  lambda: blurfill(im, a.w, a.h, a.blur, fgw, fgh, a.fgup),
          "contain":   lambda: contain(im, a.w, a.h),
          "topcover":  lambda: topcover(im, a.w, a.h),
          "brandblur": lambda: brandblur(im, a.w, a.h, a.blur, fgw, fgh, a.tint, a.tint_strength, a.fgscale, a.fgup),
          "duotone":   lambda: duotone(im, a.w, a.h, fgw, fgh, a.tint, a.tint_strength, a.fgscale, a.fgup),
          "framed":    lambda: framed(im, a.w, a.h, a.blur, fgw, fgh, a.tint, a.tint_strength, a.fgscale, a.fgup)}[a.style]
```

- [ ] **Step 4: Drop the default blur — "thin blurr"**

Replace line 86:

```python
    ap.add_argument("--blur", type=int, default=30)
```

with:

```python
    # Breeder 2026-08-07: "Reduce the blur; thin blurr". 30 read as fog behind a small bird.
    ap.add_argument("--blur", type=int, default=14)
```

- [ ] **Step 5: Verify the engine runs and produces bigger subjects**

Run:

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/reframe_og.py "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/breeding pair of african grey parrots for sale.jpg" /tmp/t-brandblur.webp --style brandblur --tint green --mobcrop 4:5 && python3 -c "from PIL import Image; im=Image.open('/tmp/t-brandblur.webp'); print(im.size)"
```

Expected: a `[brandblur]` line under 95KB, then `(1408, 768)`.

- [ ] **Step 6: Commit the engine**

```bash
git add scripts/reframe_og.py && git commit -m "feat(og): 3 new baked styles — brandblur, duotone, framed; --tint palette beds, thinner default blur, larger subject"
```

- [ ] **Step 7: Write the preview generator**

Create `scripts/make_og_previews.py`:

```python
#!/usr/bin/env python3
"""Bake every candidate OG style at desktop/tablet/mobile and emit one HTML preview.

Breeder-facing. Writes to public/_preview/ so `npx astro build` publishes it and the
breeder can open it on a phone; the directory is removed once a style is chosen.
"""
import subprocess, pathlib, sys

SRC = pathlib.Path("assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR")
OUT = pathlib.Path("public/_preview/og")
OUT.mkdir(parents=True, exist_ok=True)

# Two masters with different shapes, so a style cannot look good by luck.
MASTERS = {
    "pair": SRC / "breeding pair of african grey parrots for sale.jpg",
    "solo": SRC / "talker-jane-african-grey-breeding-pair-sale-nearby.webp",
}
# (label, style, tint) — each keeps a neutral twin so the greyish bed stays visible.
VARIANTS = [
    ("F · Brand Blur (green)",  "brandblur", "green"),
    ("F · Brand Blur (neutral)", "brandblur", "neutral"),
    ("G · Duotone (cream)",     "duotone",   "cream"),
    ("G · Duotone (clay)",      "duotone",   "clay"),
    ("I · Framed (green)",      "framed",    "green"),
    ("I · Framed (neutral)",    "framed",    "neutral"),
    ("current · Blur-Fill",     "blurfill",  "neutral"),
]
SIZES = [("desktop", 1408, 768), ("tablet", 1024, 576), ("mobile", 720, 900)]

rows = []
for mk, mp in MASTERS.items():
    if not mp.exists():
        sys.exit(f"missing master: {mp}")
    for label, style, tint in VARIANTS:
        cells = []
        for sk, w, h in SIZES:
            name = f"{mk}-{style}-{tint}-{sk}.webp"
            cmd = ["python3", "scripts/reframe_og.py", str(mp), str(OUT / name),
                   "--style", style, "--tint", tint, "--w", str(w), "--h", str(h)]
            if sk == "mobile":
                cmd += ["--mobcrop", "4:5"]
            subprocess.run(cmd, check=True)
            cells.append(f'<figure><figcaption>{sk} {w}×{h}</figcaption>'
                         f'<img src="/_preview/og/{name}" alt="{label} {sk}"></figure>')
        rows.append(f'<section><h2>{label} <small>— {mk} master</small></h2>'
                    f'<div class="row">{"".join(cells)}</div></section>')

html = """<!doctype html><meta charset=utf-8><title>OG Style Preview — Breeding Pair</title>
<meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex>
<style>body{font:16px/1.5 system-ui;background:#faf7f4;color:#2b2018;margin:0;padding:24px}
h1{font-size:1.4rem}h2{font-size:1rem;margin:28px 0 8px;color:#2D6A4F}
small{color:#6b625a;font-weight:400}
.row{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
figure{margin:0}figcaption{font-size:.75rem;color:#6b625a;margin-bottom:4px}
img{width:100%;height:auto;border:1px solid #e6ddd4;border-radius:10px;display:block}</style>
<h1>OG framing styles — pick one for /african-grey-breeding-pair-for-sale/</h1>
<p>Every style shown at desktop, tablet and mobile, on two different masters.
Neutral = today's greyish/black bed. Green/clay/cream = CAG palette beds.</p>
""" + "".join(rows)

pathlib.Path("sessions/2026-08-07-og-style-preview.html").write_text(html)
(OUT.parent / "index.html").write_text(html)
print(f"wrote {len(rows)} style rows → public/_preview/og/")
```

- [ ] **Step 8: Generate the previews**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/make_og_previews.py
```

Expected: `wrote 14 style rows → public/_preview/og/`

- [ ] **Step 9: Commit**

```bash
git add scripts/make_og_previews.py sessions/2026-08-07-og-style-preview.html public/_preview && git commit -m "feat(preview): OG style comparison — 7 variants x 2 masters x 3 breakpoints"
```

## Task 2: Three Bird-Card Image Styles + Preview

The breeder's constraint, verbatim: *"nice, clean ones with almost transparent label below, no head/face/beak cutoff"*, and *"birds should be clearly seen just like the homepage cards"*.

**Files:**
- Create: `sessions/2026-08-07-birdcard-style-preview.html`

- [ ] **Step 1: Read the homepage card treatment so the reference is real, not remembered**

```bash
cd /Users/apple/Downloads/CAG && grep -n "object-position\|object-fit\|aspect-ratio\|h-72" src/components/BirdCard.astro
```

- [ ] **Step 2: Write the three-style preview**

Create `sessions/2026-08-07-birdcard-style-preview.html`:

```html
<!doctype html><meta charset=utf-8><title>Bird Card Styles — pick one</title>
<meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex>
<style>
:root{--g:#2D6A4F;--clay:#e8604c;--ink:#2b2018;--mid:#6b625a;--bd:#e6ddd4;--cream:#faf7f4}
body{font:16px/1.55 system-ui;background:var(--cream);color:var(--ink);margin:0;padding:24px}
h1{font-size:1.35rem}h2{font-size:1rem;color:var(--g);margin:32px 0 4px}
p.note{font-size:.85rem;color:var(--mid);margin:0 0 12px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:14px}
.mb{background:#fff;border:1px solid var(--bd);border-radius:14px;overflow:hidden;
    text-decoration:none;color:inherit;display:block}
.mb-nm{font-weight:700;font-size:.95rem;margin:0}
.mb-pr{color:var(--clay);font-weight:700;font-size:.9rem;margin:0}
.mb-tr{font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;color:var(--mid);margin:4px 0 0}

/* ── Style 1 · Full-Bleed Portrait + Glass Label ───────────────────── */
.s1 .mb-ph{aspect-ratio:4/5;position:relative}
.s1 img{width:100%;height:100%;object-fit:cover;object-position:50% 18%;display:block}
.s1 .mb-lb{position:absolute;inset:auto 0 0 0;padding:9px 11px;
  background:rgba(255,255,255,.74);backdrop-filter:blur(9px);-webkit-backdrop-filter:blur(9px)}

/* ── Style 2 · Contained Bird on Cream (zero crop risk) ────────────── */
.s2 .mb-ph{aspect-ratio:1/1;background:linear-gradient(160deg,#fff 0%,#f3ece4 100%);
  display:grid;place-items:center;padding:8px}
.s2 img{max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain;display:block}
.s2 .mb-lb{padding:9px 11px;border-top:1px solid var(--bd)}

/* ── Style 3 · Tall Card + Gradient Scrim (label over image) ───────── */
.s3 .mb-ph{aspect-ratio:3/4;position:relative}
.s3 img{width:100%;height:100%;object-fit:cover;object-position:50% 15%;display:block}
.s3 .mb-lb{position:absolute;inset:auto 0 0 0;padding:26px 11px 10px;color:#fff;
  background:linear-gradient(to top,rgba(20,32,26,.86) 0%,rgba(20,32,26,.55) 55%,transparent 100%)}
.s3 .mb-pr{color:#ffb3a6}.s3 .mb-tr{color:rgba(255,255,255,.8)}
@media(max-width:600px){.grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}
</style>
<h1>Bird-card image styles — pick one for the breeding-pair singles row</h1>

<h2>Style 1 · Full-Bleed Portrait + Glass Label</h2>
<p class="note">4:5 crop anchored at 18% from the top so the head is never cut. Label is a
frosted-glass bar over the photo — "almost transparent" as asked. Most like the homepage cards.</p>
<div class="grid s1">
  <a class="mb" href="/congo-african-grey-for-sale/"><div class="mb-ph">
    <img src="/images/birds/bery.webp" alt="Bery"></div>
    <div class="mb-lb"><p class="mb-nm">Bery</p><p class="mb-pr">$1,800</p>
    <p class="mb-tr">DNA-sexed · closed-banded</p></div></a>
  <a class="mb" href="/timneh-african-grey-for-sale/"><div class="mb-ph">
    <img src="/images/birds/elad.webp" alt="Elad"></div>
    <div class="mb-lb"><p class="mb-nm">Elad</p><p class="mb-pr">$1,600</p>
    <p class="mb-tr">Timneh · hand-raised</p></div></a>
</div>

<h2>Style 2 · Contained Bird on Cream</h2>
<p class="note">The bird is <em>contained</em>, never cropped — mathematically impossible to cut a
beak. Square bed in brand cream. Cleanest, but the bird reads slightly smaller.</p>
<div class="grid s2">
  <a class="mb" href="/congo-african-grey-for-sale/"><div class="mb-ph">
    <img src="/images/birds/bery.webp" alt="Bery"></div>
    <div class="mb-lb"><p class="mb-nm">Bery</p><p class="mb-pr">$1,800</p>
    <p class="mb-tr">DNA-sexed · closed-banded</p></div></a>
  <a class="mb" href="/timneh-african-grey-for-sale/"><div class="mb-ph">
    <img src="/images/birds/elad.webp" alt="Elad"></div>
    <div class="mb-lb"><p class="mb-nm">Elad</p><p class="mb-pr">$1,600</p>
    <p class="mb-tr">Timneh · hand-raised</p></div></a>
</div>

<h2>Style 3 · Tall Card + Gradient Scrim</h2>
<p class="note">3:4, label sits <em>on</em> the photo under a soft dark scrim. Biggest bird of the
three. Trade-off: white-on-photo text needs the scrim to hold AA at every image.</p>
<div class="grid s3">
  <a class="mb" href="/congo-african-grey-for-sale/"><div class="mb-ph">
    <img src="/images/birds/bery.webp" alt="Bery"></div>
    <div class="mb-lb"><p class="mb-nm">Bery</p><p class="mb-pr">$1,800</p>
    <p class="mb-tr">DNA-sexed · closed-banded</p></div></a>
  <a class="mb" href="/timneh-african-grey-for-sale/"><div class="mb-ph">
    <img src="/images/birds/elad.webp" alt="Elad"></div>
    <div class="mb-lb"><p class="mb-nm">Elad</p><p class="mb-pr">$1,600</p>
    <p class="mb-tr">Timneh · hand-raised</p></div></a>
</div>
```

- [ ] **Step 3: Repoint the `<img src>` values at real files**

The `/images/birds/*.webp` paths above are illustrative. Resolve the real ones:

```bash
cd /Users/apple/Downloads/CAG && grep -rho 'src="/images/[a-z0-9/-]*\(bery\|amie\|roys\|elad\|evie\|jins\|jeni\)[a-z0-9-]*\.webp"' src/pages/ | sort -u
```

Edit `sessions/2026-08-07-birdcard-style-preview.html`, replacing each placeholder `src` with a path from that output. If a bird has no image, use the one from its `/available/<slug>/` page.

- [ ] **Step 4: Screenshot both previews at all three widths**

```bash
cd /Users/apple/Downloads/CAG && npx astro build
```

Then open `http://localhost:4321/_preview/og/` via `preview_start`, and the bird-card file directly. Capture `computer {action:"screenshot"}` at 375, 768 and 1280 via `resize_window` for each. Save nothing — these go straight to the breeder.

- [ ] **Step 5: Send both previews to the breeder**

Use `SendUserFile` with `display:"render"` on `sessions/2026-08-07-birdcard-style-preview.html`, plus the OG preview screenshots.

- [ ] **Step 6: Commit**

```bash
git add sessions/2026-08-07-birdcard-style-preview.html && git commit -m "feat(preview): 3 bird-card image styles for breeder selection"
```

---

## ✅ GATE A — RESOLVED 2026-08-07

**Breeder decisions, locked. Do not re-litigate these.**

| Decision | Choice | Concrete value |
|---|---|---|
| OG framing style | **F · Brand Blur, neutral bed** | `--style brandblur --tint neutral --mobcrop 4:5` (defaults `--blur 14`, `--fgscale 0.94`) |
| Bird-card style | **Style 1 · Full-Bleed Portrait + Glass Label** | 4:5, `object-position:50% 18%`, `rgba(255,255,255,.76)` + `backdrop-filter:blur(9px)` label |

Wherever this plan says `<CHOSEN_STYLE>` read `brandblur`; `<CHOSEN_TINT>` read `neutral`.
`MiniBirdCard.astro` in Task 6 is already written as Style 1 — ship it as specified.

<details><summary>Original gate text (kept for the record)</summary>

**Do not start Task 5, 6 or 7. Do not touch any OG image on the page.**

Present, with a recommendation per CLAUDE.md rule 5:

1. **Which OG style?** — Recommended: **F · Brand Blur (neutral)**. Why from data: it is the only candidate that changes *nothing* about the page's existing markup (`.sec-img.og-photo` boxes stay as they are — all 8 images are file swaps), while directly fixing both stated complaints — `--fgscale 0.94` makes the bird ~15% larger in frame than today's effective 0.82, and `--blur 14` halves the fog. **Trade-off:** it keeps the greyish bed the breeder said they disliked *the format* of; if the objection is the grey itself rather than the bird size, `F · green` is the same geometry on a brand bed and is the fallback.
2. **Which bird-card style?** — Recommended: **Style 1 · Full-Bleed Portrait + Glass Label**. Why from data: it is the closest match to the homepage `BirdCard.astro` treatment the breeder named as the reference, and the frosted label is literally the "almost transparent label below" that was asked for. **Trade-off:** 4:5 cover-crops, so any master with the bird low in frame needs a per-bird `object-position` override — the exact per-bird pattern already banked in `project_birdcard_patterns.md`.

Phases B, C and D below do **not** depend on this gate and may proceed in parallel.

</details>

---

# PHASE B — Content and Structure

## Task 15: Re-Bake All 8 Existing OG Photos + Apply the Mobile `og-tall` Standard

**Plan gap, caught at Gate A 2026-08-07.** Task 5 baked only the *new* egg photo. But the breeder's complaint — "makes the birds appear too small on desktop/mobile/tablets" — is about the **8 photos already on the page**. Without this task the page keeps 8 old blur-fill images and gains one new-style one, which is worse than either. This task must land before Task 11 (impeccable pass).

Second, independent defect: `grep -c og-tall` on this page returns **0**. `IMAGE-DESIGNS.md §7` makes mobile full-bleed 4:5 the standing default for single-bird/pair portrait OG photos, and it was never applied here. That is the other half of "birds look small on mobile".

**Files:**
- Modify: the 8 `og-photo` `.webp` pairs under `public/images/breeding-pair/`
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro` (add `og-tall` to portrait photos only)

- [ ] **Step 1: Enumerate the 8 photos and locate each one's ORIGINAL master**

```bash
cd /Users/apple/Downloads/CAG && grep -n 'class="sec-img og-photo' src/pages/african-grey-breeding-pair-for-sale/index.astro
ls "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/"
cat sessions/2026-08-04-breeding-pair-image-metadata.md
```

**Critical:** re-baking a shipped `.webp` re-processes an already-blurred file and compounds the blur. Every re-bake MUST start from the original master in `assets/`. If a photo's master cannot be found, leave that photo alone and report it — `IMAGE-DESIGNS.md §7` is explicit that an already-baked file cannot be recovered by reframing.

- [ ] **Step 2: Re-bake each one from its master**

For each photo, with `<master>` and `<name>` substituted:

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/reframe_og.py "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/<master>" "public/images/breeding-pair/<name>.webp" --style brandblur --tint neutral --mobcrop 4:5 --sib "public/images/breeding-pair/<name>-760.webp"
```

Infographics (`inf-*`) are **excluded** — the breeder said the infographics are perfect and need no style change.

- [ ] **Step 3: Classify each photo portrait vs scene, then tag**

Per `IMAGE-DESIGNS.md §7` clause 2: single-bird/pair **portraits** get mobile 4:5 full-bleed; **wide/scene/documentation** shots must NOT (a landscape subject in a tall frame reads as a small photo floating in blur — the exact bug being fixed).

Open each of the 8 baked files with the Read tool and classify by what you see. Then:
- portrait → `class="sec-img og-photo og-tall"`
- scene → `class="sec-img og-photo og-scene"` (the page already has a `.og-scene` 5:4 rule at `:1150`)

- [ ] **Step 4: Add the `og-tall` mobile rule if absent**

Check first: `grep -n "og-tall" src/pages/african-grey-breeding-pair-for-sale/index.astro`. If there is no CSS rule, add inside the ≤900px block:

```css
  .bpair .sec-img.og-tall { width:100vw; max-width:100vw; margin-left:calc(50% - 50vw);
    aspect-ratio:4/5; border-radius:0; border-left:0; border-right:0; }
```

Confirm the page root has `overflow-x:clip` — if not, adding this causes a horizontal scrollbar. Verify with `document.documentElement.scrollWidth <= window.innerWidth` at 375px.

- [ ] **Step 5: Verify at all three widths in a real browser**

```bash
cd /Users/apple/Downloads/CAG && npx astro build
```

At 375, 768 and 1280: confirm no head/beak/tail is cut on any of the 8, no horizontal scroll at 375, and every file is under 95 KB. Read at least three of the baked files directly and compare against the pre-change versions in git.

- [ ] **Step 6: Commit**

```bash
git add public/images/breeding-pair/ src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "feat(breeding-pair): re-bake all 8 OG photos as brandblur/neutral from masters + apply the og-tall mobile 4:5 standard"
```

## Task 3: Re-Bake the Two Corrected Infographics

The masters were regenerated today; the shipped `.webp` files are from Aug 4 and still carry the duplicate-label defect.

**Files:**
- Modify: `public/images/breeding-pair/inf-2-price-ladder{,-760}.webp`
- Modify: `public/images/breeding-pair/inf-7-housing-nest-box{,-760,-320}.webp`

- [ ] **Step 1: Open both masters and confirm the defect is actually gone**

Read both PNGs with the Read tool:
- `assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/inf-2-price-ladder.png`
- `assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/inf-7-housing-nest-box.png`

Confirm no heading text is repeated within either image. `reference_infographic_generator_duplicate_labels.md` records that a spelling check passes these — **you must look at the image**. If a duplicate is still present, stop and report; do not bake.

- [ ] **Step 2: Bake both at all three widths**

```bash
cd /Users/apple/Downloads/CAG && for n in inf-2-price-ladder inf-7-housing-nest-box; do python3 scripts/bake_infographics.py "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/$n.png" "public/images/breeding-pair/$n" 2>/dev/null || python3 scripts/reframe_og.py "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/$n.png" "public/images/breeding-pair/$n.webp" --style contain --sib "public/images/breeding-pair/$n-760.webp"; done
```

If `bake_infographics.py` takes different arguments, read it first (`Read scripts/bake_infographics.py`) and use its real signature — infographics must NOT go through an OG framing style.

- [ ] **Step 3: Rebuild the 320 sibling for inf-7**

```bash
cd /Users/apple/Downloads/CAG && python3 -c "
from PIL import Image
im = Image.open('public/images/breeding-pair/inf-7-housing-nest-box.webp')
im.resize((320, round(320*im.height/im.width)), Image.LANCZOS).save('public/images/breeding-pair/inf-7-housing-nest-box-320.webp','WEBP',quality=82,method=6)
print('ok')"
```

- [ ] **Step 4: Verify every file is newer than the master and under budget**

```bash
cd /Users/apple/Downloads/CAG && ls -la public/images/breeding-pair/ | grep -E "inf-2|inf-7"
```

Expected: all five files dated today, each under 95 KB.

- [ ] **Step 5: Commit**

```bash
git add public/images/breeding-pair/inf-2-price-ladder.webp public/images/breeding-pair/inf-2-price-ladder-760.webp public/images/breeding-pair/inf-7-housing-nest-box.webp public/images/breeding-pair/inf-7-housing-nest-box-760.webp public/images/breeding-pair/inf-7-housing-nest-box-320.webp && git commit -m "fix(breeding-pair): re-bake inf-2 + inf-7 from corrected masters — duplicate-label defect"
```

## Task 4: The Joshua Erwin Review

`index.astro:723` currently promises the section is empty *on purpose*. That paragraph must change the moment a real quote lands, or the page contradicts itself.

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro:723` and the schema block

- [ ] **Step 1: Rewrite the section's opening paragraph**

Replace the whole of line 723 with:

```html
  <p>We are careful in this section, because this is where most breeder sites quietly invent people. We will not print a quote we cannot attribute to a real buyer who agreed to it, which is why there is one below and not twelve. What comes back to us after a pair lands has a consistent shape. The two-crate arrival is what buyers mention first, usually with some surprise that both birds walked out steady. The clutch record is second — more than one buyer has told us they only understood what they had bought once the dates were in front of them. And the settling period comes up constantly, because a moved pair typically goes quiet for weeks before either bird looks at the box, and knowing that in advance is the difference between patience and panic.</p>
```

- [ ] **Step 2: Insert the review card immediately after that paragraph**

```html
  <figure class="quote-c">
    <blockquote>
      <p>Finding trustworthy African Grey breeding pairs for sale was important to me, and working with Mark and Teri made the process much easier. They were straightforward, helpful, and very knowledgeable about their birds. They provided clear information, answered my questions patiently, and made sure I understood the process before moving forward. I&rsquo;m pleased with the breeding African Grey pair I received and appreciate the professionalism and care Mark and Teri showed throughout the experience.</p>
    </blockquote>
    <figcaption>
      <span class="q-stars" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
      <span class="q-who">Joshua Erwin</span>
      <span class="q-where">San Bernardino, California</span>
    </figcaption>
  </figure>
```

Note: **Mark**, not Mart — both occurrences. The breeder confirmed this on 2026-08-07: the supplied text read "Mart", which is a transcription slip for Mark Benjamin. Ship "Mark". Do not re-raise this.

- [ ] **Step 3: Add the `.quote-c` figcaption parts to the page CSS**

Insert immediately after `index.astro:1115` (`.bpair .quote-c figcaption { font-size:.82rem; }`):

```css
.bpair .quote-c figcaption { display:flex; flex-wrap:wrap; align-items:baseline; gap:4px 10px; }
.bpair .q-stars { color:var(--bp-clay); letter-spacing:.08em; }
.bpair .q-who { font-weight:700; color:var(--bp-ink); }
.bpair .q-where { color:var(--bp-mid); }
```

- [ ] **Step 4: Add the Review to the page schema — and only what is verifiable**

Find the `Product`/`Offer` JSON-LD block:

```bash
cd /Users/apple/Downloads/CAG && grep -n '"@type": *"Product"\|"@type":"Product"\|aggregateRating\|"review"' src/pages/african-grey-breeding-pair-for-sale/index.astro
```

Add exactly one `review` entry inside the Product node:

```json
"review": [{
  "@type": "Review",
  "reviewRating": { "@type": "Rating", "ratingValue": "5", "bestRating": "5" },
  "author": { "@type": "Person", "name": "Joshua Erwin" },
  "reviewBody": "Finding trustworthy African Grey breeding pairs for sale was important to me, and working with Mark and Teri made the process much easier. They were straightforward, helpful, and very knowledgeable about their birds. They provided clear information, answered my questions patiently, and made sure I understood the process before moving forward. I'm pleased with the breeding African Grey pair I received and appreciate the professionalism and care Mark and Teri showed throughout the experience."
}]
```

Do **not** add `aggregateRating` — one review is not an aggregate, and inventing a count is the exact failure recorded in `project_testimonials_fabricated_removed.md`.

- [ ] **Step 5: Build and verify the review renders and validates**

```bash
cd /Users/apple/Downloads/CAG && npx astro build && grep -c "Joshua Erwin" dist/african-grey-breeding-pair-for-sale/index.html && python3 -c "
import re,json,sys
h=open('dist/african-grey-breeding-pair-for-sale/index.html').read()
for m in re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>', h, re.S):
    json.loads(m)
print('all JSON-LD parses')"
```

Expected: `2` (prose + schema), then `all JSON-LD parses`.

- [ ] **Step 6: Commit**

```bash
git add src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "feat(breeding-pair): first named buyer review — Joshua Erwin, San Bernardino + Review schema"
```

## Task 5: Fertile-Egg Image and the Egg-Page Link

> **✅ DONE 2026-08-07 — commit `6dca9b1`, pushed.** Two deviations from the steps below,
> both deliberate: (1) the figure is tagged `og-scene`, not `og-tall` — the master is a
> top-down nest shot, and `IMAGE-DESIGNS.md §7` reserves the mobile 4:5 full-bleed frame
> for single-bird/pair portraits; a landscape subject in a tall frame is the exact bug
> Task 15 fixed. Baked with `--mobcrop 5:4` to stay dual-safe. (2) the figure sits
> directly after the `</h3>`, before the prose, per the breeder's images-first rule
> (Task 8) — the incubator figure keeps its place after the paragraph.

*Depends on Gate A (OG style).* The section has an incubator photo but never uses the supplied egg master and never links the egg page.

**Files:**
- Create: `public/images/breeding-pair/fertile-african-grey-parrot-egg-for-sale{,-760}.webp`
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro:665-674`

- [ ] **Step 1: Bake the master in the breeder-chosen style**

Substitute `<CHOSEN_STYLE>` and `<CHOSEN_TINT>` with the Gate A answers:

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/reframe_og.py "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/fertile-grey-parrot-egg-for-sale.jpg" public/images/breeding-pair/fertile-african-grey-parrot-egg-for-sale.webp --style <CHOSEN_STYLE> --tint <CHOSEN_TINT> --mobcrop 4:5 --sib public/images/breeding-pair/fertile-african-grey-parrot-egg-for-sale-760.webp
```

- [ ] **Step 2: Add the egg-page link to the Candled Fertile Eggs paragraph**

In line 666, replace the opening clause:

```
  <p>For breeders who run their own incubator, we sell candled fertile eggs from these same lines.
```

with the Link-First form (`rules/links.md` — the anchor opens the sentence, never mid-sentence):

```
  <p><a href="/african-grey-parrot-bird-eggs-for-sale-usa/">Our candled fertile African Grey eggs</a> come from these same lines, for breeders who run their own incubator.
```

- [ ] **Step 3: Add the egg figure after that paragraph (before the existing incubator figure)**

```html
  <figure class="sec-img-wrap">
    <img class="sec-img og-photo og-tall" src="/images/breeding-pair/fertile-african-grey-parrot-egg-for-sale.webp"
         srcset="/images/breeding-pair/fertile-african-grey-parrot-egg-for-sale-760.webp 760w, /images/breeding-pair/fertile-african-grey-parrot-egg-for-sale.webp 1408w"
         sizes="(max-width:980px) 92vw, 760px"
         alt="Candled fertile African Grey parrot egg for sale from our Midland Texas breeding lines"
         title="Fertile African Grey egg — candled and confirmed before it ships"
         width="1408" height="768" loading="lazy" decoding="async">
    <figcaption class="img-note">Every egg is candled and confirmed developing before we offer it. <a href="/african-grey-parrot-bird-eggs-for-sale-usa/">See current egg availability</a>.</figcaption>
  </figure>
```

- [ ] **Step 4: Verify no alt-text collision**

`rules/images.md`: no two images on a page share an alt.

```bash
cd /Users/apple/Downloads/CAG && npx astro build && python3 -c "
import re,collections
h=open('dist/african-grey-breeding-pair-for-sale/index.html').read()
a=[x for x in re.findall(r'alt=\"([^\"]*)\"',h) if x.strip()]
d=[k for k,v in collections.Counter(a).items() if v>1]
print('DUPLICATE ALTS:',d if d else 'none')"
```

Expected: `DUPLICATE ALTS: none`

- [ ] **Step 5: Commit**

```bash
git add public/images/breeding-pair/fertile-african-grey-parrot-egg-for-sale.webp public/images/breeding-pair/fertile-african-grey-parrot-egg-for-sale-760.webp src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "feat(breeding-pair): fertile-egg photo + Link-First egg-page anchor in section 14"
```

## Task 6: The `MiniBirdCard` Component and the Singles Row

> **✅ DONE 2026-08-07 — commit `6dca9b1`, pushed.** Shipped as Style 1 per Gate A.
> **The Step-2 roster below was wrong on every field** — corrected against
> `data/clutch-inventory.json` + the live `/available/` pages: Bery **$1,700**,
> Amie **$2,500**, Roys **$2,300**, Elad $1,600, Evie $1,500, Jins & Jeni **$3,500**
> at **`/available/jins-jeni/`** (not `jins-and-jeni`), and every photo lives under
> **`/birds/<slug>/`**, not `/images/birds/`. Three defects found in the browser:
> `auto-fill` orphaned the 5th card (now explicit 5/3/2 columns); the trust line wrapped
> and grew the glass label to ~40% of the photo (`.62rem/.04em` → one line, 35%); and
> `roys-gallery-1` has Roys head-down so the label covered his head (→ `gallery-3`).
> `objectPos` is per-bird as banked. Card `<img>` needs `width`/`height` — `img_dims`
> in `final_page_audit.py` fails the whole page without them.

*Depends on Gate A (bird-card style).* `§singles` names Bery, Amie, Roys, Elad and Evie in prose with zero visuals. The breeder asked for this as a **reusable** component, not a one-off.

**Files:**
- Create: `src/components/cag-library/MiniBirdCard.astro`
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro:662-663`

- [ ] **Step 1: Build the component**

Create `src/components/cag-library/MiniBirdCard.astro` with the Gate-A-chosen style baked in (shown here as Style 1, the recommendation — swap the `.mb-ph`/`.mb-lb` rules for the chosen block from the preview file if the breeder picked 2 or 3):

```astro
---
/**
 * MiniBirdCard — small linked bird card for cross-sell rows on non-bird pages.
 * Built 2026-08-07 for the breeding-pair singles row. Reusable across the
 * for-sale cluster: any page that names our birds in prose should show them.
 * Style chosen by the breeder from sessions/2026-08-07-birdcard-style-preview.html.
 */
export interface Props {
  name: string;
  price: string;
  href: string;
  img: string;
  img760?: string;
  alt: string;
  trust: string;
  objectPos?: string;   // per-bird override — see project_birdcard_patterns.md
  eager?: boolean;
}
const { name, price, href, img, img760, alt, trust, objectPos = '50% 18%', eager = false } = Astro.props;
---
<a class="mbc" href={href}>
  <div class="mbc-ph">
    <img src={img}
         srcset={img760 ? `${img760} 380w, ${img} 760w` : undefined}
         sizes="(max-width:600px) 46vw, 200px"
         alt={alt} width="760" height="950"
         loading={eager ? 'eager' : 'lazy'} decoding="async"
         style={`object-position:${objectPos}`} />
  </div>
  <div class="mbc-lb">
    <p class="mbc-nm">{name}</p>
    <p class="mbc-pr">{price}</p>
    <p class="mbc-tr">{trust}</p>
  </div>
</a>

<style>
/* position:relative MUST be on .mbc, not .mbc-ph — .mbc-lb is a SIBLING of .mbc-ph,
   so relative on .mbc-ph does nothing and the label escapes to the viewport. Caught in
   the 2026-08-07 bird-card preview, where the label pinned itself to the window bottom. */
.mbc { position:relative; display:block; background:#fff; border:1px solid var(--bp-bd, #e6ddd4);
  border-radius:14px; overflow:hidden; text-decoration:none; color:inherit;
  transition:box-shadow .18s, transform .18s; }
.mbc:hover { box-shadow:0 6px 20px rgba(60,30,10,.10); transform:translateY(-2px); }
.mbc:focus-visible { outline:3px solid var(--bp-clay, #e8604c); outline-offset:2px; }
.mbc-ph { aspect-ratio:4/5; position:relative; background:#f3ece4; }
.mbc-ph img { width:100%; height:100%; object-fit:cover; display:block; }
.mbc-lb { position:absolute; inset:auto 0 0 0; padding:9px 11px;
  background:rgba(255,255,255,.76); backdrop-filter:blur(9px); -webkit-backdrop-filter:blur(9px); }
.mbc-nm { margin:0; font-weight:700; font-size:.95rem; color:#2b2018; line-height:1.25; }
.mbc-pr { margin:0; font-weight:700; font-size:.9rem; color:#b04228; line-height:1.3; }
.mbc-tr { margin:3px 0 0; font-size:.7rem; letter-spacing:.06em; text-transform:uppercase;
  color:#6b625a; line-height:1.35; }
@media (prefers-reduced-motion:reduce) { .mbc { transition:none; } }
</style>
```

`.mbc-ph` needs `position:relative` for the absolutely-positioned label — it is set above. `#b04228` is the AA-safe small-clay token from `reference_aa_contrast_and_perf_fixes.md`, not `#e8604c`.

- [ ] **Step 2: Import the component and declare the roster**

Add to the frontmatter of `src/pages/african-grey-breeding-pair-for-sale/index.astro` (with the other imports):

```astro
import MiniBirdCard from '../../components/cag-library/MiniBirdCard.astro';

// Singles + the unrelated companion pair, shown as cards under §14. Prices and
// parentage from data/price-matrix.json — never typed from memory.
const singles = [
  { name: 'Bery', price: '$1,800', href: '/available/bery/',  img: '/images/birds/bery.webp',  alt: 'Bery, a hand-raised Congo African Grey single available from our Midland aviary',  trust: 'Congo · DNA-sexed' },
  { name: 'Amie', price: '$1,800', href: '/available/amie/',  img: '/images/birds/amie.webp',  alt: 'Amie, a Congo African Grey hen out of James and Lois',                                trust: 'Congo · closed-banded' },
  { name: 'Roys', price: '$1,800', href: '/available/roys/',  img: '/images/birds/roys.webp',  alt: 'Roys, Amie&rsquo;s sibling and a hand-fed Congo African Grey',                        trust: 'Congo · PBFD screened' },
  { name: 'Elad', price: '$1,600', href: '/available/elad/',  img: '/images/birds/elad.webp',  alt: 'Elad, a Timneh African Grey cock bird raised under our home protocol',                trust: 'Timneh · hand-raised' },
  { name: 'Evie', price: '$1,500', href: '/available/evie/',  img: '/images/birds/evie.webp',  alt: 'Evie, a Timneh African Grey hen and the smaller of our two Timnehs',                  trust: 'Timneh · DNA-sexed', objectPos: '50% 8%' },
];
```

- [ ] **Step 3: Resolve every path and price against real data — do not ship the placeholders above**

```bash
cd /Users/apple/Downloads/CAG && ls src/pages/available/ && echo "--- prices ---" && python3 -c "
import json; d=json.load(open('data/price-matrix.json'))
print(json.dumps(d, indent=1)[:1800])"
```

Correct every `href`, `img` and `price` in the `singles` array to match. `project_birdcard_patterns.md` records `Evie = object-top`; that is why Evie carries an `objectPos` override.

- [ ] **Step 4: Render the row after the H3 at line 662**

Insert immediately after the `Available Singles From Our Own Lines` paragraph (`:663`):

```astro
  <div class="mbc-row">
    {singles.map((b) => <MiniBirdCard {...b} />)}
  </div>
  <p class="img-note">Every bird above came out of our own flights. Prices are what we ask today; shipping is $185 to your airport or $350 door-to-door.</p>
```

The shipping line is required on every card context by `feedback_shipping_line_on_cards.md`.

- [ ] **Step 5: Add the row grid to the page CSS**

Insert after `index.astro:1152`:

```css
.bpair .mbc-row { display:grid; grid-template-columns:repeat(auto-fill, minmax(180px, 1fr)); gap:12px; margin:14px 0 10px; }
@media (max-width:600px) { .bpair .mbc-row { grid-template-columns:repeat(2, minmax(0,1fr)); gap:10px; } }
```

Two-up on mobile is the "stacks on mobile beautifully" the breeder asked for; a single column at 375px makes five cards a scroll wall.

- [ ] **Step 6: Add Jins & Jeni to the `.xsell` block as a second row**

`project_jins_jeni_vs_breeding_pair.md` records that Jins & Jeni are an **unrelated companion pair**, not breeder stock. Insert inside `.xsell` (`:676-679`), after its paragraph:

```astro
    <div class="mbc-row">
      <MiniBirdCard name="Jins & Jeni" price="$3,200" href="/available/jins-and-jeni/"
        img="/images/birds/jins-jeni.webp"
        alt="Jins and Jeni, an unrelated companion pair of Congo African Greys sold together"
        trust="Companion pair · not breeder stock" />
    </div>
```

Verify the slug and price with `ls src/pages/available/ | grep -i jin` before committing. The `trust` line must say **not breeder stock** — this page is about breeding pairs and the distinction is the whole point of that memory.

- [ ] **Step 7: Build and verify every card link resolves**

```bash
cd /Users/apple/Downloads/CAG && npx astro build && python3 -c "
import re,os
h=open('dist/african-grey-breeding-pair-for-sale/index.html').read()
for href in sorted(set(re.findall(r'class=\"mbc\" href=\"([^\"]+)\"',h))):
    p='dist'+href+'index.html' if href.endswith('/') else 'dist'+href
    print(('OK  ' if os.path.exists(p) else 'DEAD'), href)"
```

Expected: every line `OK`. Any `DEAD` means a wrong slug in the `singles` array — fix it, do not create a redirect.

- [ ] **Step 8: Commit**

```bash
git add src/components/cag-library/MiniBirdCard.astro src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "feat(components): MiniBirdCard + singles/Jins-Jeni cross-sell rows on breeding-pair"
```

## Task 7: Differentiate the Key Takeaway From the Congo-Pair Page

`congo-african-grey-parrot-pair-for-sale/index.astro:292` has `<section id="takeaway">`. The breeding-pair page's equivalent is the `.bluf` at `:293`. Whatever overlaps must go — this is `dup-no-sibling-crossover`, and CLAUDE.md rule 9 says the fix is to rewrite from *this* page's outline, not to reword the sibling's sentences.

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro:293`

- [ ] **Step 1: Read the sibling's takeaway so you know what to avoid — and nothing more**

```bash
cd /Users/apple/Downloads/CAG && sed -n '292,320p' src/pages/congo-african-grey-parrot-pair-for-sale/index.astro
```

Read it once, to know what NOT to write. Do not copy a clause.

- [ ] **Step 2: Run the dup gate BEFORE writing, not after**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/dup_content_audit.py 2>&1 | grep -A4 -i "breeding-pair"
```

`reference_forsale_build_traps.md`: dup-gate the built page, pre-write.

- [ ] **Step 3: Replace the `.bluf` with a takeaway only this page can make**

The congo-pair page's angle is *price entry point*. This page's angle is the inversion nobody else states — **price rises as the clutch count falls**. Replace line 293 entirely:

```html
          <p class="bluf">Here is the thing every other breeding-pair listing gets backwards: our prices go <em>up</em> as the clutch count goes <em>down</em>. Talker &amp; Jane have four hatched clutches and cost $3,000. Sally &amp; Odin have one and cost $5,500. You are not paying for what a pair has already produced — you are paying for the productive years it has left, and a four-year-old pair has more of them than a twelve-year-old pair ever will. Any seller charging a premium for "most proven" is selling you the past.</p>
```

- [ ] **Step 4: Re-run the dup gate on the built page**

```bash
cd /Users/apple/Downloads/CAG && npx astro build && python3 scripts/dup_content_audit.py 2>&1 | grep -A4 -i "breeding-pair"
```

Expected: no ≥12-word overlap between `african-grey-breeding-pair-for-sale` and `congo-african-grey-parrot-pair-for-sale`. Per `reference_same_input_different_verdict.md`, **run it twice** — one clean run proves nothing.

- [ ] **Step 5: Commit**

```bash
git add src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "fix(breeding-pair): key takeaway rewritten from own outline — inverse price/clutch angle, no congo-pair overlap"
```

## Task 8: The Two Missed Rules — Hero/Counter Separator, and Images-First

The breeder: *"There should be a clear differentiator between the Hero and the counter snippets. You missed this rule, and add it now to the rules, CLAUDE.md, and the components sprint. On H3s, images must come first, just like on other for-sale pages."*

Per CLAUDE.md's own harness principle, a rule with no test is a deletion candidate — so both ship **with a check**, not as prose.

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro:939` and `:253-260`
- Modify: `rules/design.md`, `rules/for-sale.md`, `CLAUDE.md`
- Modify: `data/quality/rule-index.json`
- Create: `tests/render/checks/a11y.ts` (shared with Task 11)

- [ ] **Step 1: Add the separator**

Today `.phero` ends and `.counter-wrap { padding:6px 0 18px; }` begins with nothing between them. Replace line 939:

```css
.counter-wrap { padding:6px 0 18px; }
```

with:

```css
/* RULE (breeder 2026-08-07): the counter strip must never read as part of the hero.
   A tonal shift + hairline is the minimum separation; a seam divider is the maximum. */
.counter-wrap { padding:18px 0 20px; background:#f6efe8; border-top:1px solid var(--bp-bd);
  border-bottom:1px solid var(--bp-bd); }
.bpair .counter-wrap { position:relative; }
.bpair .counter-wrap::before { content:''; position:absolute; inset:0 0 auto 0; height:3px;
  background:linear-gradient(90deg, var(--bp-green) 0%, var(--bp-clay) 100%); }
```

- [ ] **Step 2: Add the images-first fix under H3s**

Audit which H3s on this page are followed by prose before their image:

```bash
cd /Users/apple/Downloads/CAG && npx astro build && python3 -c "
import re
h=open('dist/african-grey-breeding-pair-for-sale/index.html').read()
body=h.split('<main',1)[-1]
blocks=re.split(r'(<h3[^>]*>.*?</h3>)', body, flags=re.S)
for i in range(1,len(blocks),2):
    head=re.sub(r'<[^>]+>','',blocks[i]).strip()
    seg=blocks[i+1] if i+1<len(blocks) else ''
    seg=seg.split('<h2')[0].split('<h3')[0]
    im=seg.find('<img'); pp=seg.find('<p')
    if im!=-1 and pp!=-1 and pp<im: print('PROSE-FIRST:', head[:60])
"
```

For every `PROSE-FIRST` H3 reported, move that section's `<figure class=\"sec-img-wrap\">` block to sit directly after the `</h3>`, before the first `<p>`. Do not reword any prose while moving it.

- [ ] **Step 3: Write both rules into `rules/design.md`**

Append:

```markdown
### 10. Hero and counter strip must be visually separated (breeder, 2026-08-07)

A counter/stat strip placed directly under a hero reads as hero furniture and the
figures stop registering. Every page carrying both MUST put a visible boundary
between them — at minimum a background-tone shift plus a 1px rule; at most a
`.cag-seam` divider. Never zero separation, and never only whitespace.

Enforced by: `tests/render/checks/layout.ts` → `hero-counter-separation`.

### 11. Under an H3, the image comes before the prose (breeder, 2026-08-07)

In the for-sale cluster, a sectional image sits immediately after its `</h3>` and
before the first `<p>` of that H3's block. This matches every other for-sale page
and gives the reader the subject before the argument. H2 sections keep the existing
lead-paragraph-first order — this rule is H3-scoped.

Enforced by: `tests/render/checks/layout.ts` → `h3-image-first`.
```

- [ ] **Step 4: Mirror both into `rules/for-sale.md`**

Append:

```markdown
## Component-order rules (2026-08-07)

- **Hero → separator → counters.** See `rules/design.md` §10. The separator is part of
  the component tuple; a page tuple that lists a counter strip must also name its separator.
- **H3 → image → prose.** See `rules/design.md` §11.
```

- [ ] **Step 5: Add one line to `CLAUDE.md`**

In the "The twelve rules that stay here" section, do **not** add a thirteenth rule — both new rules have tests, so they belong in the packs. Instead, extend the pack table row for design. Replace the `rules/design.md` row:

```
| [`rules/design.md`](rules/design.md) | the nine non-negotiable visual rules |
```

with:

```
| [`rules/design.md`](rules/design.md) | the eleven non-negotiable visual rules — incl. hero/counter separation + H3-image-first |
```

- [ ] **Step 6: Register both rules as `test` in the rule index**

```bash
cd /Users/apple/Downloads/CAG && python3 -c "
import json
p='data/quality/rule-index.json'
d=json.load(open(p))
rules = d['rules'] if isinstance(d, dict) and 'rules' in d else d
for rid,desc in [('hero-counter-separation','Hero and counter strip must be visually separated'),
                 ('h3-image-first','Sectional image precedes prose under every H3')]:
    entry={'id':rid,'kind':'test','pack':'rules/design.md','check':'tests/render/checks/layout.ts','desc':desc,'added':'2026-08-07'}
    if isinstance(rules,list): rules.append(entry)
    else: rules[rid]=entry
json.dump(d, open(p,'w'), indent=2)
print('registered 2 rules')"
```

If the file's shape differs, read it first and match the existing entry schema exactly.

- [ ] **Step 7: Add the two checks to the layout family**

Append to `tests/render/checks/layout.ts`, following the existing check signature in that file (read it first — do not guess the `CheckContext` shape):

```ts
export const heroCounterSeparation = {
  id: 'hero-counter-separation',
  family: 'LAYOUT',
  blocking: false,
  async run(page, ctx) {
    const r = await page.evaluate(() => {
      const c = document.querySelector('.counter-wrap, .counter-strip, [data-counters]');
      if (!c) return { examined: 0 };
      const hero = c.previousElementSibling;
      const cs = getComputedStyle(c);
      const hs = hero ? getComputedStyle(hero) : null;
      const hasRule = cs.borderTopWidth !== '0px' || !!c.querySelector(':scope > .cag-seam, :scope > .seam-wrap');
      const hasTone = !!hs && cs.backgroundColor !== hs.backgroundColor;
      return { examined: 1, hasRule, hasTone };
    });
    if (!r.examined) return { examined: 0, pass: true, note: 'no counter strip on page' };
    return { examined: 1, pass: r.hasRule && r.hasTone,
      note: r.hasRule && r.hasTone ? 'separated' : `missing ${!r.hasRule ? 'rule/seam' : ''} ${!r.hasTone ? 'tone shift' : ''}`.trim() };
  },
};

export const h3ImageFirst = {
  id: 'h3-image-first',
  family: 'LAYOUT',
  blocking: false,
  async run(page, ctx) {
    if (ctx.pageType !== 'for-sale') return { examined: 0, pass: true, note: 'for-sale only' };
    const bad = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('main h3').forEach((h) => {
        let n = h.nextElementSibling, sawP = false;
        while (n && !/^H[123]$/.test(n.tagName)) {
          if (n.tagName === 'P' && n.textContent.trim().length > 40) sawP = true;
          if (n.querySelector?.('img') || n.tagName === 'IMG') {
            if (sawP) out.push(h.textContent.trim().slice(0, 60));
            break;
          }
          n = n.nextElementSibling;
        }
      });
      return { total: document.querySelectorAll('main h3').length, bad: out };
    });
    return { examined: bad.total, pass: bad.bad.length === 0, note: bad.bad.join(' | ') };
  },
};
```

Register both in `tests/render/checks/index.ts` alongside the existing layout exports.

- [ ] **Step 8: Prove the checks can fail — meta gate first**

Create `tests/render/fixtures/known_broken/hero-counter-flush.html`:

```html
<!doctype html><meta charset=utf-8><title>known-broken: hero flush against counters</title>
<style>body{margin:0}.phero,.counter-wrap{background:#fff}.counter-wrap{border:0;padding:6px 0}</style>
<header class="phero"><h1>Hero</h1></header>
<div class="counter-wrap"><div class="cs"><span class="num">3</span><span class="cs-l">pairs</span></div></div>
<main><h3>An H3 whose prose comes first</h3>
<p>This paragraph is long enough to count as real prose ahead of the sectional image below it.</p>
<figure><img src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" alt="late image" width="1" height="1"></figure>
</main>
```

Then:

```bash
cd /Users/apple/Downloads/CAG && npm run test:render:meta
```

Expected: the meta gate reports both `hero-counter-separation` and `h3-image-first` **failing on the fixture** with a non-zero examined count. A check that passes the known-broken fixture is broken — fix the check, not the fixture. Per `reference_promote_check_needs_examined_count.md`, an `examined: 0` is not a pass.

- [ ] **Step 9: Run the real gate on the page**

```bash
cd /Users/apple/Downloads/CAG && npm run test:render:pages
```

Expected: both new checks pass on `african-grey-breeding-pair-for-sale` with `examined ≥ 1`.

- [ ] **Step 10: Commit**

```bash
git add rules/design.md rules/for-sale.md CLAUDE.md data/quality/rule-index.json tests/render/checks/layout.ts tests/render/checks/index.ts tests/render/fixtures/known_broken/hero-counter-flush.html src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "feat(rules): hero/counter separation + H3-image-first — both rules ship with checks and a known-broken fixture"
```

---

# PHASE C — Mobile, Accessibility, Impeccable

## Task 9: Fix Both Mobile Caption Defects

One rule, both screenshots.

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro:1310` and `:1313`

- [ ] **Step 1: Add `caption` to the mobile block list**

Replace line 1310:

```css
  .bpair .tH, .bpair .tH thead, .bpair .tH tbody, .bpair .tH th, .bpair .tH td, .bpair .tH tr { display:block; }
```

with:

```css
  /* `caption` MUST be in this list. Left as display:table-caption inside a table whose
     other children are blocks, the browser shrink-to-fits it into a narrow column with
     dead space beside it — the defect the breeder screenshotted 2026-08-07. */
  .bpair .tH, .bpair .tH caption, .bpair .tH thead, .bpair .tH tbody, .bpair .tH th, .bpair .tH td, .bpair .tH tr { display:block; }
```

- [ ] **Step 2: Give the caption a readable mobile treatment**

Insert immediately after that line:

```css
  /* Uppercase + .1em tracking is a desktop label style; at 375px it forces one word
     per line. Sentence case, normal tracking, full width, horizontal. */
  .bpair .tH caption { width:auto; padding:11px 14px; text-align:left;
    text-transform:none; letter-spacing:0; font-size:clamp(0.86rem, 3.4vw, 0.95rem);
    line-height:1.35; font-weight:700; border-radius:14px 14px 0 0; }
  .bpair .tH caption em { font-style:italic; }
```

- [ ] **Step 3: Shorten the second caption so it is a caption, not a paragraph**

The housing caption is 21 words and carries the citation. Move the citation into the body text where it belongs. Replace line 573:

```html
    <caption>The four housing specifications we hold every breeding-pair buyer to, per World Parrot Trust guidance for <em>Psittacus erithacus</em>.</caption>
```

with:

```html
    <caption>The Four Housing Specifications We Require</caption>
```

Then, in the paragraph immediately preceding that table, append this sentence so no sourcing is lost:

```html
 These four figures follow <a href="https://www.parrottrust.org/" target="_blank" rel="noopener">World Parrot Trust</a> guidance for <em>Psittacus erithacus</em>, not our preference.
```

Title Case is correct for a caption per `reference_title_case_headings.md`; the external link opens in a new tab per `feedback_linking_policy.md`.

- [ ] **Step 4: Verify at 375px in a real browser — not by reading CSS**

```bash
cd /Users/apple/Downloads/CAG && npx astro build
```

Start the preview, `resize_window` to `{preset:"mobile"}`, navigate to `/african-grey-breeding-pair-for-sale/`, then:

```js
// javascript_tool
Array.from(document.querySelectorAll('.tH caption')).map(c => {
  const r = c.getBoundingClientRect();
  return { text: c.textContent.trim().slice(0,40), width: Math.round(r.width),
           lines: Math.round(r.height / parseFloat(getComputedStyle(c).lineHeight)) };
});
```

Expected: each caption `width` within 12px of the table's own width (i.e. ~343 at 375px viewport), and `lines` ≤ 2. A width near 140 means the fix did not apply.

- [ ] **Step 5: Screenshot both tables at 375 as proof**

`computer {action:"screenshot"}` at `#production` and `#housing`. Per `feedback_preview_screenshot_workflow.md`, scroll to 0 and hide DOM above the target first, or the screenshot resets scroll.

- [ ] **Step 6: Commit**

```bash
git add src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "fix(breeding-pair): table captions stacked into a narrow column on mobile — caption missing from the display:block list"
```

## Task 10: Fix the 10 `.ti` Contrast Failures

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro:1203`

- [ ] **Step 1: Add the missing light-theme `.ti` colour**

Line 1203 currently overrides `.ti` only in the active state:

```css
.bpair .tdial-list a.on .ti { color:var(--bp-clay); }
```

Insert **immediately before** it:

```css
/* The dial flips to a white bed on .bpair (:1194) but .ti kept its dark-theme sage
   #7ba98d — 2.66:1 on white, the 10 Lighthouse contrast failures of 2026-08-07.
   #5d7d6a is 4.62:1 on #fff. Verified, not eyeballed. */
.bpair .tdial-list a .ti { color:#5d7d6a; }
```

- [ ] **Step 2: Verify the ratio arithmetically before trusting the eye**

```bash
cd /Users/apple/Downloads/CAG && python3 -c "
def lin(c):
    c/=255
    return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def L(h):
    h=h.lstrip('#'); r,g,b=(int(h[i:i+2],16) for i in (0,2,4))
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def cr(a,b):
    la,lb=L(a),L(b); hi,lo=max(la,lb),min(la,lb); return (hi+0.05)/(lo+0.05)
print('old #7ba98d on #fff:', round(cr('#7ba98d','#ffffff'),2))
print('new #5d7d6a on #fff:', round(cr('#5d7d6a','#ffffff'),2))"
```

Expected: `old ... 2.66`, `new ... 4.62`. If the new value is under 4.5, darken until it clears and update the comment with the real number.

- [ ] **Step 3: Verify on the rendered page, at every breakpoint the dial is visible**

The dial is `display:none` under 980px (`:1129`), so it only exists on desktop. Build, preview at `{preset:"desktop"}`, then:

```js
// javascript_tool
Array.from(document.querySelectorAll('.tdial-list .ti')).map(e => ({
  n: e.textContent, color: getComputedStyle(e).color,
  bg: getComputedStyle(e.closest('.tdial')).backgroundColor
}));
```

Expected: every `color` is `rgb(93, 125, 106)` except the `.on` item, which is clay.

- [ ] **Step 4: Sweep the same drift class across the whole dial**

The bug was "component re-themed, child not". Check every other child for the same gap:

```bash
cd /Users/apple/Downloads/CAG && grep -n "^\.t\(dial\|num\|of\|t\|i\)\|^\.bpair \.tdial\|^\.bpair \.t" src/pages/african-grey-breeding-pair-for-sale/index.astro
```

For each dark-theme colour defined on a `.tdial` descendant, confirm a `.bpair` override exists. Fix any that do not, using the same measured-ratio method.

- [ ] **Step 5: Commit**

```bash
git add src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "fix(a11y): .ti was 2.66:1 on the white .bpair dial — light-theme override was missing for the inactive state"
```

## Task 11: The Impeccable / Frontend UI-UX Pass

**Sequencing answer:** this runs **now**, not at the start. Running it before Tasks 3–10 would mean auditing a component set that is about to gain a card row, a new image style, two re-baked infographics and a review card — every finding would be re-derived. Running it after Phase D would mean shipping perf fixes against a layout that then changes. Here is the only position where the component set is final and nothing downstream moves it.

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro` (as findings dictate)

- [ ] **Step 1: Invoke the hardening skill's scanner first — it is cheaper than the human pass**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/page_hardening_scan.py african-grey-breeding-pair-for-sale
```

- [ ] **Step 2: Confirm every reported defect on the built page before editing anything**

Invoke `Skill: cag-gate-integrity`. For each finding, open the rendered page at the breakpoint named and confirm it. `feedback_verify_the_gate_before_fixing.md` records twelve checkers that cried wolf on this site. Discard any finding you cannot see.

- [ ] **Step 3: Run the impeccable pass over the confirmed set**

Invoke `Skill: impeccable` scoped to `/african-grey-breeding-pair-for-sale/`, with these page-specific constraints stated up front so it does not violate them:

- Word count is **fixed** — the breeder has approved ~8,627 words. Do not cut prose. `wordcount_in_band` is a known-accepted warning on this page.
- No video section.
- The OG image style is breeder-chosen (Gate A) — do not restyle images.
- Visual layer only, per CLAUDE.md rule 7: a redesign never adds or removes content.

- [ ] **Step 4: Re-run the render harness both ways**

```bash
cd /Users/apple/Downloads/CAG && npm run test:render:meta && npm run test:render:pages
```

`test:render:meta` first — it is the gate that checks the checkers. Then run `test:render:pages` a **second** time; per `reference_same_input_different_verdict.md`, one clean run proves nothing.

- [ ] **Step 5: Commit**

```bash
git add src/pages/african-grey-breeding-pair-for-sale/index.astro && git commit -m "polish(breeding-pair): impeccable pass — confirmed hardening findings only"
```

---

# PHASE D — The Perf Gate That Does Not Exist

## Task 12: `perf_audit.py` + `cag-perf-gate` Skill

**The recommendation the breeder asked for.** We do **not** have this today — verified: `package.json` has no perf script, `skills/` has no perf skill, and `tests/render/checks/` has no a11y or perf family. What exists is two *agents* (`cag-performance-fixer`, `cag-performance-monitor-agent`), and an agent is not a gate: it runs when someone remembers to call it, produces prose, and nothing fails the build.

**Recommended: build it as a render-harness family plus a thin CLI, not as a standalone skill (Recommended).** Why, from this codebase's own measured history: `project_render_harness_phase2.md` records a 418-row defect baseline collapsing to 85 with zero page edits once checks lived in the harness, because the harness owns fixtures, examined-counts and the meta gate. A standalone skill would re-invent all three and would be `untested` in `rule-index.json` on day one — which CLAUDE.md defines as a deletion candidate. **Trade-off:** Lighthouse takes ~25s per page against the harness's ~2s checks, so perf cannot run on every page every time; it runs on a named subset and on demand, which is why the thin CLI exists alongside it.

**Files:**
- Create: `scripts/perf_audit.py`
- Create: `skills/cag-perf-gate.md`
- Create: `tests/render/checks/a11y.ts`
- Modify: `package.json`

- [ ] **Step 1: Write the contrast check as a real harness family**

Create `tests/render/checks/a11y.ts` (match the `CheckContext` signature already used in `layout.ts` — read it first):

```ts
/**
 * A11Y family. Contrast is computed from RENDERED colours, because the bug class this
 * exists for is "component re-themed, child not" — a source grep cannot see it.
 * See reference_markup_css_drift.md and the .ti/#7ba98d failure of 2026-08-07.
 */
const REL = (c: number) => (c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4));

export const textContrast = {
  id: 'text-contrast-aa',
  family: 'A11Y',
  blocking: true,
  async run(page, ctx) {
    const r = await page.evaluate(() => {
      const lum = (rgb) => {
        const [r, g, b] = rgb.map((v) => {
          v /= 255;
          return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
        });
        return 0.2126 * r + 0.7152 * g + 0.0722 * b;
      };
      const parse = (s) => (s.match(/[\d.]+/g) || []).slice(0, 3).map(Number);
      const bgOf = (el) => {
        let n = el;
        while (n && n !== document.documentElement) {
          const bg = getComputedStyle(n).backgroundColor;
          const p = parse(bg);
          if (p.length === 3 && !/rgba\(.*,\s*0\)/.test(bg)) return p;
          n = n.parentElement;
        }
        return [255, 255, 255];
      };
      const fails = [];
      let examined = 0;
      document.querySelectorAll('body *').forEach((el) => {
        const t = Array.from(el.childNodes)
          .filter((n) => n.nodeType === 3 && n.textContent.trim())
          .map((n) => n.textContent.trim())
          .join('');
        if (!t) return;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden' || cs.display === 'none' || +cs.opacity === 0) return;
        const size = parseFloat(cs.fontSize);
        const bold = +cs.fontWeight >= 700;
        const large = size >= 24 || (size >= 18.66 && bold);
        const need = large ? 3 : 4.5;
        const fg = lum(parse(cs.color));
        const bg = lum(bgOf(el));
        const ratio = (Math.max(fg, bg) + 0.05) / (Math.min(fg, bg) + 0.05);
        examined++;
        if (ratio < need) {
          fails.push({ sel: el.className || el.tagName, text: t.slice(0, 30), ratio: +ratio.toFixed(2), need });
        }
      });
      return { examined, fails: fails.slice(0, 25), total: fails.length };
    });
    return {
      examined: r.examined,
      pass: r.total === 0,
      note: r.total === 0 ? 'all text meets AA' : `${r.total} below AA: ` + r.fails.map((f) => `${f.sel}@${f.ratio}`).join(', '),
    };
  },
};
```

- [ ] **Step 2: Add the known-broken fixture proving it catches the real bug**

Create `tests/render/fixtures/known_broken/tdial-contrast.html` — the exact failure, reduced:

```html
<!doctype html><meta charset=utf-8><title>known-broken: .ti sage on white dial</title>
<style>
.tdial{background:#fff;padding:12px;border-radius:16px}
.ti{color:#7ba98d;font-size:13px}   /* 2.66:1 on white — must FAIL */
.tt{color:#2b2018;font-size:13px}   /* passes, so the check must not blanket-fail */
</style>
<nav class="tdial"><ul>
<li><a><span class="ti">1</span><span class="tt">The Three Pairs</span></a></li>
<li><a><span class="ti">2</span><span class="tt">What Proven Means</span></a></li>
</ul></nav>
```

- [ ] **Step 3: Register the family and run the meta gate**

Export `textContrast` from `tests/render/checks/index.ts`, then:

```bash
cd /Users/apple/Downloads/CAG && npm run test:render:meta
```

Expected: `text-contrast-aa` **fails** on `tdial-contrast.html`, reporting the `.ti` spans at ~2.66 and **not** flagging `.tt`. `examined` must be ≥ 4. A check that flags both spans is over-broad; a check reporting `examined: 0` passed nothing — `reference_gate_examined_zero_pages.md`.

- [ ] **Step 4: Write the Lighthouse CLI**

Create `scripts/perf_audit.py`:

```python
#!/usr/bin/env python3
"""perf_audit.py — the PageSpeed gate. Runs Lighthouse against dist/ over a local
server and fails on any category below threshold.

Why this exists: before 2026-08-07 the only way to know a page's PageSpeed status was
for the breeder to paste the URL into pagespeed.web.dev after every deploy. That is
rework by definition. This runs pre-push.

  python3 scripts/perf_audit.py african-grey-breeding-pair-for-sale [--mobile] [--json out.json]

Known-ignored: "Missing source maps for large first-party JavaScript" pointing at /70de/.
That path is Cloudflare Rocket Loader, injected at the edge, absent from this repo, and
Unscored by Lighthouse. It is not a defect and must not be chased.
"""
import argparse, json, subprocess, sys, http.server, socketserver, threading, functools, pathlib

THRESHOLDS = {"performance": 0.95, "accessibility": 1.0, "best-practices": 1.0, "seo": 1.0}
IGNORE_AUDITS = {"valid-source-maps"}
PORT = 4399

def serve(root):
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), h)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--mobile", action="store_true")
    ap.add_argument("--json", default="")
    a = ap.parse_args()

    dist = pathlib.Path("dist")
    if not dist.exists():
        sys.exit("dist/ missing — run `npx astro build` first. Gates measure dist, never source.")

    httpd = serve(dist)
    url = f"http://127.0.0.1:{PORT}/{a.slug}/"
    out = pathlib.Path(a.json or f"/tmp/lh-{a.slug}.json")
    cmd = ["npx", "-y", "lighthouse", url, "--quiet", "--output=json", f"--output-path={out}",
           "--chrome-flags=--headless=new --no-sandbox",
           f"--preset={'' if a.mobile else 'desktop'}".rstrip("=")]
    cmd = [c for c in cmd if c != "--preset"]
    subprocess.run(cmd, check=True)
    httpd.shutdown()

    rep = json.loads(out.read_text())
    failed = []
    print(f"\n  {a.slug}  [{'mobile' if a.mobile else 'desktop'}]")
    for k, floor in THRESHOLDS.items():
        score = rep["categories"][k]["score"]
        ok = score is not None and score >= floor
        print(f"    {'PASS' if ok else 'FAIL'}  {k:15s} {round((score or 0)*100)}  (floor {round(floor*100)})")
        if not ok:
            failed.append(k)

    print("\n  Failing audits:")
    shown = 0
    for aid, aud in rep["audits"].items():
        if aid in IGNORE_AUDITS:
            continue
        if aud.get("score") is not None and aud["score"] < 1:
            items = (aud.get("details") or {}).get("items") or []
            print(f"    - {aid}: {aud.get('title','')} ({len(items)} elements)")
            shown += 1
    if not shown:
        print("    none")

    if failed:
        sys.exit(f"\nPERF GATE FAIL: {', '.join(failed)}")
    print("\nPERF GATE PASS")

if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Add the npm scripts**

Add to `package.json` `scripts`:

```json
    "test:perf": "python3 scripts/perf_audit.py african-grey-breeding-pair-for-sale",
    "test:perf:mobile": "python3 scripts/perf_audit.py african-grey-breeding-pair-for-sale --mobile"
```

- [ ] **Step 6: Run it both ways and iterate until green**

```bash
cd /Users/apple/Downloads/CAG && npx astro build && npm run test:perf && npm run test:perf:mobile
```

For each failing audit, apply the banked fix from `reference_aa_contrast_and_perf_fixes.md` and `reference_perf_image_tooling.md` — Pillow not sips for resizes, `font-display:swap`, `fetchpriority=high` + preload on the LCP image only. Re-run after each fix. Per `reference_bimodal_metrics_need_5_runs.md`, **CLS is bimodal** — if CLS is the only thing failing, run five times and take the median before attributing a cause.

- [ ] **Step 7: Write the skill so the next session does not re-derive any of this**

Create `skills/cag-perf-gate.md`:

```markdown
---
name: cag-perf-gate
description: Use before any push of a CAG page, and whenever PageSpeed/Lighthouse reports a defect — contrast, LCP, CLS, image delivery, unused CSS. Runs the local Lighthouse gate against dist/ so the breeder never has to paste a URL into pagespeed.web.dev after a deploy, and applies the banked fix for each audit class.
---

# CAG Perf Gate

## Run it

```bash
npx astro build && python3 scripts/perf_audit.py <slug> && python3 scripts/perf_audit.py <slug> --mobile
```

Floors: performance ≥ 95, accessibility / best-practices / SEO = 100.

## Before you fix anything

A Lighthouse finding is a hypothesis. Confirm it on the built page at the breakpoint
named. See `skills/cag-gate-integrity.md`. Twelve checkers have cried wolf on this site.

## Known-ignored

- **`valid-source-maps` on `/70de/`** — Cloudflare Rocket Loader, injected at the edge,
  not in this repo, and Unscored. Toggle it in the Cloudflare dashboard or leave it.
  Never chase it in code.

## The fix bank

| Audit | Root cause seen on this site | Fix |
|---|---|---|
| `color-contrast` | component re-themed, child colour not overridden | measure the ratio in Python, add the missing `.<page> ` override — never eyeball |
| `largest-contentful-paint` | srcset double-download | `heroPreloadSrcset` + `fetchpriority=high` on the LCP image only |
| `cumulative-layout-shift` | counter/infographic with no reserved box | explicit `width`/`height` + `min-height` on the container |
| `uses-responsive-images` | missing measured `sizes` | `reference_srcset_needs_measured_sizes.md` — measure a real rendered width |
| `unused-css-rules` | dead kit CSS from a ported sibling | class-diff the page, purge — `reference_markup_css_drift.md` |

## Related
`tests/render/checks/a11y.ts` (`text-contrast-aa`, blocking) catches the contrast class
in ~2s without Lighthouse. Run the harness first; run this before push.
```

- [ ] **Step 8: Register the skill**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/register_skills.py --copy
```

- [ ] **Step 9: Commit**

```bash
git add scripts/perf_audit.py skills/cag-perf-gate.md tests/render/checks/a11y.ts tests/render/checks/index.ts tests/render/fixtures/known_broken/tdial-contrast.html package.json && git commit -m "feat(gates): perf/a11y gate — blocking text-contrast-aa harness check + local Lighthouse CLI + cag-perf-gate skill"
```

---

# PHASE E — Close-Out

## Task 13: Sprint 5 — LLM Visibility Baseline

**Files:**
- Create: `sessions/2026-08-07-breeding-pair-sprint5-llm-visibility.md`

- [ ] **Step 1: Run the baseline**

Invoke the `cag-llm-keyword-intel` agent for slug `african-grey-breeding-pair-for-sale` across 5 engines (ChatGPT, Claude, Gemini, Perplexity, Google AIO) × 6 queries:

1. `african grey breeding pair for sale`
2. `proven african grey breeding pair price`
3. `how do I know an african grey pair is actually proven`
4. `african grey breeding pair vs single bird`
5. `where to buy a proven congo african grey pair usa`
6. `what does a proven breeding pair of african greys cost`

- [ ] **Step 2: Record raw results, never inferred ones**

Write the brief with one row per engine × query: cited / not cited, competitors cited, and the answer structure. Any engine that could not be reached is written `NOT FETCHED` — CLAUDE.md rule 10. Do not infer a score.

- [ ] **Step 3: Commit**

```bash
git add sessions/2026-08-07-breeding-pair-sprint5-llm-visibility.md && git commit -m "docs(sprint5): breeding-pair LLM visibility baseline — 5 engines x 6 queries"
```

## Task 14: Sprint 6 — Final Checks, Sitemaps, IndexNow, Lessons, Memory

- [ ] **Step 1: Run the full final gate**

Invoke `Skill: cag-final-page-pass` on `african-grey-breeding-pair-for-sale`. Then the named agents the breeder asked for, in this order:

```
Skill: anti-ai-writing            → on §14 (new prose) and §16 (rewritten review intro)
Agent: cag-non-commodity-content-agent  → on the rewritten key takeaway
Agent: cag-entity-incorporation-agent   → on §14 singles + eggs
Agent: cag-keyword-verifier             → whole page
```

Scope the first two to the sections this session changed — re-auditing 8,627 approved words wastes the pass and risks a rewrite the breeder did not ask for.

- [ ] **Step 2: Confirm `wordcount_in_band` is the only accepted warning**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/final_page_audit.py 2>&1 | grep -A20 "breeding-pair"
```

Expected: `wordcount_in_band` only. The breeder has explicitly accepted 8,627 words against the 8,000 band — do not cut prose to satisfy it. Any *other* warning is real work.

- [ ] **Step 3: Regenerate sitemaps and submit**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/generate_sitemaps.py && python3 scripts/quality_report.py
```

Then IndexNow-submit the page (Bing/Yandex) per `project_sitemap_llms_tooling.md`.

- [ ] **Step 4: Remove the preview directory**

The Gate A previews were published to make them phone-openable. They must not stay in `dist/`.

```bash
cd /Users/apple/Downloads/CAG && rm -rf public/_preview && npx astro build && test ! -d dist/_preview && echo "preview removed"
```

- [ ] **Step 5: Write the lessons doc**

Create `sessions/2026-08-07-breeding-pair-lessons.md` covering, at minimum:
- the `caption` omission from the mobile `display:block` list (one rule, two visible defects, and it would have hit every future `.tH`)
- the `.bpair .tdial` re-theme that left `.ti` behind — another instance of markup↔CSS drift
- that both new breeder rules shipped **with checks and a known-broken fixture**, per the harness-not-rules principle
- that no perf gate existed and what was built instead of a bare skill

- [ ] **Step 6: Write the memories**

Create these files in `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/`, each with the required frontmatter, then add one pointer line each to `MEMORY.md`:

1. `reference_table_caption_mobile_stacking.md` (type: reference) — `caption` must be in the `display:block` list, and drop uppercase/tracking at mobile. Link `[[reference_mobile_table_stacking]]`, `[[reference_table_row_pseudo_and_masonry]]`. Add to the **LAYOUT** family list in `MEMORY.md`.
2. `reference_minibirdcard_component.md` (type: reference) — when a page names our birds in prose, show them; `MiniBirdCard.astro`, 2-up at ≤600px, per-bird `objectPos`. Link `[[project_birdcard_patterns]]`, `[[feedback_shipping_line_on_cards]]`.
3. `project_perf_gate.md` (type: project) — the gate did not exist before 2026-08-07; `text-contrast-aa` (blocking, harness) + `scripts/perf_audit.py` + `skills/cag-perf-gate.md`; `/70de/` source maps are Rocket Loader and known-ignored. Link `[[project_blog_perf_rocket_loader]]`, `[[reference_aa_contrast_and_perf_fixes]]`. Add to the **A11Y** entry under render-harness families.
4. `reference_og_style_palette_beds.md` (type: reference) — `--tint {neutral,green,clay,cream}`, `--fgscale` default 0.94, `--blur` default 14; neutral reproduces the old bed. Link `[[reference_og_blurfill_framing]]`.
5. Update `feedback_bird_page_visual_fix_patterns.md` with the chosen bird-card style rather than creating a sixth file.

Also add the two new rules to `data/quality/rule-index.json` verification: re-run `python3 scripts/quality_report.py` and confirm §5 does **not** list either as `untested`.

- [ ] **Step 7: Bank the lesson in the learning skill**

Append to `skills/cag-learning-loop.md` a "When a page names a bird in prose" entry pointing at `MiniBirdCard.astro`, and a "When a gate reports a caption/table defect on mobile" entry pointing at the `display:block` list.

- [ ] **Step 8: Final build, push, verify live**

```bash
cd /Users/apple/Downloads/CAG && npx astro build && npm run test:render:meta && npm run test:render:pages && npm run test:perf
```

```bash
cd /Users/apple/Downloads/CAG && git add -A ':!.claude/launch.json' && git commit -m "docs(breeding-pair): sprint 5+6 close-out — LLM baseline, lessons, sitemaps, memories" && git push
```

Push **is** deploy (CLAUDE.md rule 4). After the Cloudflare Pages build completes, confirm the live page:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://congoafricangreys.com/african-grey-breeding-pair-for-sale/
```

Expected: `200`. Then re-check `https://pagespeed.web.dev/` for the live URL and confirm it matches what `test:perf` reported locally. If they disagree, the local gate's thresholds or throttling are wrong — fix the gate, not the page.

---

## Open Flags

- ~~**`Mart` vs `Mark` in the Joshua Erwin review.**~~ **RESOLVED 2026-08-07 — breeder decision: ship as "Mark".** Treated as a transcription slip; every other page, the NAP record and `credentials.md` say Mark Benjamin, and a live testimonial naming "Mart" reads as fabricated to anyone checking. Task 4 is unblocked — no further question.
- **`wordcount_in_band`** stays warned and accepted at 8,627 words, per explicit breeder instruction. Not a defect on this page.
- **`/70de/` source maps** — Cloudflare Rocket Loader, dashboard-only, Unscored. Documented as known-ignored in `skills/cag-perf-gate.md`; no code task exists.
- **Gate A blocks Tasks 5, 6 and 7 only.** Everything else in Phases B, C, D and E runs regardless.

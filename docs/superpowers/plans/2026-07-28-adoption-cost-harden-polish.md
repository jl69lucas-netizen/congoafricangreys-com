# Adoption-Cost Page — Harden & Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Take `/african-grey-parrot-adoption-cost/` from "feels rushed" to cluster-parity by repairing 4 miswired components, rendering the 5 mandated components whose CSS already ships, placing the 14 in-body images that are on disk but unreferenced, and closing the 5 headings that carry no opening paragraph.

**Architecture:** The page's CSS kit is correct and near-complete; the *markup* drifted from it. So this is overwhelmingly a markup + asset-wiring job inside one file, not a restyle. Every component below already has its CSS on the page — the plan supplies the markup that CSS was written for. No new sections and no heading changes except deleting one orphan H6, so the approved H1–H6 outline is preserved and the Heading Outline Gate is not re-triggered.

**Tech Stack:** Astro 5 (single-file page component with a scoped `<style>` block), Pillow for image processing, `page_hardening_scan.py` / `dup_content_audit.py` / `final_page_audit.py` as gates, Playwright for runtime probes.

**Verification model:** This repo has no unit tests for page markup. The RED→GREEN discipline maps onto the gate scripts and runtime probes: prove the defect with a measurement *before* editing, fix, then re-measure. This is the binding lesson from `docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md` §1 — four "defects" last session were bugs in the checkers, not the pages.

**Working file (all tasks unless stated):** `src/pages/african-grey-parrot-adoption-cost/index.astro`

---

## File Structure

| File | Responsibility | Action |
|---|---|---|
| `src/pages/african-grey-parrot-adoption-cost/index.astro` | The whole page: frontmatter data, markup, scoped CSS, scroll-spy JS | Modify |
| `public/*.webp` | 8 processed infographics + `-760` siblings | Create (16 files) |
| `public/rony-and-rose-real-paperwork-midland-tx.mp4` + `-poster-760.webp` | Video component asset | Create |
| `sessions/2026-07-19-for-sale-component-map.md` | Binding tuple ledger — record the components now actually rendered | Modify |
| `docs/superpowers/sessions/2026-07-28-adoption-cost-harden-lessons.md` | Bank the markup↔CSS-drift failure mode for pages 9–22 | Create |

**Asset source folder:** `assets/1WORKING-ON/FOR-SALE-PAGES/BABY-african-grey-parrot/`

---

## Task 1: Repair the FAQ component (ERROR — broken on mobile *and* desktop)

The question text is rendered inside `.faqC-x`, which is the 16×16px cross-icon box (`width:16px;height:16px;flex:none`) with two clay bars drawn over it by `::before`/`::after`. `.faqC-q` (the `flex:1` text span) is applied to the `<summary>` instead. Result: every question is crushed into a 16px box under an overlaid plus sign, and no expand/collapse affordance renders at all.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro:663–668` (markup), `:1043` (answer padding)

- [ ] **Step 1: Prove the defect before touching it**

```bash
cd /Users/apple/Downloads/CAG
grep -o '<summary[^>]*>.\{0,120\}' dist/african-grey-parrot-adoption-cost/index.html | head -2
```

Expected: `class="faqC-q"` on the `<summary>` and the question text inside `<span class="faqC-x">`. That is the bug. If the text is instead inside `faqC-q`, stop — the defect is not real and this task is void.

- [ ] **Step 2: Rewrite the summary so each span gets its intended role**

Replace line 665 exactly:

```astro
              <summary class="faqC-q"><span class="faqC-n" aria-hidden="true">$</span><span class="faqC-x">{f.q}</span></summary>
```

with:

```astro
              <summary><span class="faqC-n" aria-hidden="true">$</span><span class="faqC-q">{f.q}</span><span class="faqC-x" aria-hidden="true"></span></summary>
```

Why this ordering: `.faqC-item summary` is already `display:flex;align-items:center;gap:14px`, so the three children lay out as chip → question (`flex:1`) → cross. The cross must be last and empty because its bars are drawn with `::before`/`::after`.

- [ ] **Step 3: Correct the answer's left inset to match the real chip width**

`.faqC-item p` currently uses `padding:0 20px 18px 60px`. The chip is `min-width:26px` and the flex `gap` is `14px`, so the text baseline starts at `20 + 26 + 14 = 60px` — the 60px is correct. Leave it. Only add the mobile step-down, at line 1043, replacing:

```css
.faqC-item p{color:rgba(255,255,255,.82);font-size:.9rem;margin:0;padding:0 20px 18px 60px;max-width:70ch;line-height:1.6}
```

with:

```css
.faqC-item p{color:rgba(255,255,255,.82);font-size:.9rem;margin:0;padding:0 20px 18px 60px;max-width:70ch;line-height:1.6}
@media(max-width:560px){
  .faqC-item summary{padding:14px 16px;gap:10px}
  .faqC-q{font-size:.95rem}
  .faqC-item p{padding:0 16px 16px 16px}
}
```

At 360px a 60px inset leaves ~284px of answer column; resetting to 16px recovers it. `rgba(255,255,255,.82)` on `#221f1d` measures 12.1:1, so it stays AA — do not "fix" it.

- [ ] **Step 4: Rebuild and confirm the fix rendered**

```bash
npx astro build 2>&1 | tail -3 && grep -o '<summary>.\{0,140\}' dist/african-grey-parrot-adoption-cost/index.html | head -2
```

Expected: `<span class="faqC-q">How much should I pay…` and a trailing empty `<span class="faqC-x" aria-hidden="true">`.

- [ ] **Step 5: Confirm FAQPage schema still has all entries**

```bash
python3 -c "
import json,re
h=open('dist/african-grey-parrot-adoption-cost/index.html').read()
for b in re.findall(r'<script type=\"application/ld\+json\"[^>]*>(.*?)</script>',h,re.S):
    d=json.loads(b)
    if d.get('@type')=='FAQPage': print('FAQ entries:',len(d['mainEntity']))
"
```

Expected: a non-zero count matching the `faqs` array length. Schema is generated from `faqs`, so it should be untouched — this step proves it.

- [ ] **Step 6: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "fix(adoption-cost): FAQ question text was rendering inside the 16px cross-icon box

.faqC-q sat on the <summary> while the question text sat in .faqC-x — a
16x16 flex:none box with the plus bars drawn over it. Broken at every
width, not just mobile. Restores chip -> question(flex:1) -> cross order
and adds a 560px inset step-down."
```

---

## Task 2: Repair the contact form (4 wiring faults)

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro:705–739` (markup), `:959` (`.form-actions`)

- [ ] **Step 1: Prove all four faults**

```bash
cd /Users/apple/Downloads/CAG
echo "--- .form-actions is a BUTTON row being used as a FIELD row ---"
grep -n '^\.form-actions' src/pages/african-grey-parrot-adoption-cost/index.astro
echo "--- .fs-title / .fs-ship are styled but unused; .form-head / .form-note used instead ---"
grep -n '^\.fs-title\|^\.fs-ship\|^\.form-head\|^\.form-note' src/pages/african-grey-parrot-adoption-cost/index.astro
python3 -c "
def L(c):
    r,g,b=[int(c[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda v: v/12.92 if v<=.03928 else ((v+.055)/1.055)**2.4
    r,g,b=f(r),f(g),f(b); return .2126*r+.7152*g+.0722*b
a,b=L('7a6f64'),L('221f1d')
print('.form-note #7a6f64 on the #221f1d panel: %.2f:1 (needs 4.5)'%((max(a,b)+.05)/(min(a,b)+.05)))"
```

Expected: `.form-actions{display:flex;…flex-wrap:wrap}` with no `flex:1` on children, `.fs-title`/`.fs-ship` present in CSS, and the contrast line printing **3.34:1** — an AA failure.

- [ ] **Step 2: Give the two-up field rows their own class**

`.form-actions` is the kit's button row. Reusing it for field pairs is why the name/email inputs size to content and wrap ragged. Add a dedicated row class immediately after line 959:

```css
.form-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:4px}
.form-2up{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.form-2up>div{display:grid;gap:5px;min-width:0}
@media(max-width:560px){.form-2up{grid-template-columns:1fr}}
```

`min-width:0` is mandatory — grid children default to `min-width:auto` and refuse to shrink below their content (hardening skill §1i `form-control-overflow`).

- [ ] **Step 3: Group each label with its own control**

`.cta-form` is `display:grid;gap:12px`, so a sibling `<label>` sits the same 12px from its own field as from the next field — the labels read as floating. Wrap each pair. Replace lines 714–736 with:

```astro
            <div class="fld">
              <label for="f-interest">Which bird are you asking about?</label>
              <select id="f-interest" name="interest" required>
                <option value="">Please choose…</option>
                {available.map((b) => (<option value={`${b.name} — ${b.price_display}`}>{b.name} — {b.price_display}</option>))}
                <option value="Not sure yet">Not sure yet — help me choose</option>
              </select>
            </div>
            <div class="form-2up">
              <div><label for="f-first">First name</label><input id="f-first" name="first_name" type="text" autocomplete="given-name" required /></div>
              <div><label for="f-last">Last name</label><input id="f-last" name="last_name" type="text" autocomplete="family-name" required /></div>
            </div>
            <div class="form-2up">
              <div><label for="f-cell">Cell</label><input id="f-cell" name="cell" type="tel" autocomplete="tel" /></div>
              <div><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required /></div>
            </div>
            <div class="fld">
              <label for="f-delivery">Delivery preference</label>
              <select id="f-delivery" name="delivery">
                <option value={`Airport pickup — ${money(airport)}`}>Airport pickup — {money(airport)}</option>
                <option value={`Home delivery — ${money(home)}`}>Home delivery — {money(home)}</option>
                <option value={`Flight nanny — from ${money(nanny)}`}>Flight nanny — from {money(nanny)}</option>
                <option value="Pickup in Midland, TX">Pickup in Midland, TX — if you live within 2–3 hours of us</option>
              </select>
            </div>
            <div class="fld">
              <label for="f-msg">Anything you want us to know?</label>
              <textarea id="f-msg" name="message" rows="4"></textarea>
            </div>
```

Then add the `.fld` rule directly after the `.form-2up` block from Step 2:

```css
.cta-form .fld{display:grid;gap:5px;min-width:0}
```

`.cta-form label{display:grid;gap:5px}` can stay — it is now harmless, since labels hold only text.

- [ ] **Step 4: Point the side panel at its own styled classes**

`.form-head` has only `max-width:640px` (no font, size or weight) and `.form-note` is `#7a6f64` — dark grey on the `#221f1d` panel at 3.34:1. The correctly styled `.fs-title` and `.fs-ship` are sitting unused. Replace lines 706–711:

```astro
            <p class="form-eyebrow">Reservable today</p>
            <p class="fs-title">Every Bird, Every Price</p>
            <ul class="fs-list">
              {available.map((b) => (<li><span>{b.name} — {b.variant === "timneh_african_grey" ? "Timneh" : "Congo"}{b.sex === "pair" ? " pair" : ""}</span><b>{b.price_display}</b></li>))}
            </ul>
            <p class="fs-ship">Ships nationwide · {money(airport)} airport · {money(home)} home · free pickup within two to three hours of Midland, TX.</p>
```

`.form-eyebrow` is `--clay-t #b04228` — designed for a *light* background and it now sits on `#221f1d`, which is a second contrast failure in the same panel. Override it for the dark panel, appended after the `.fs-ship` rule at line 1073:

```css
.form-side .form-eyebrow{color:#f08070}
```

`#f08070` on `#221f1d` is the cluster's sanctioned clay-on-dark value (memory `reference_aa_contrast_and_perf_fixes`).

The `.form-note` under the submit button at line 738 stays as-is — it sits on cream, where `#7a6f64` measures 5.4:1 and passes.

- [ ] **Step 5: Rebuild and re-measure contrast in the real panel**

```bash
npx astro build 2>&1 | tail -3
grep -o 'class="fs-title"\|class="fs-ship"\|class="form-2up"\|class="fld"' dist/african-grey-parrot-adoption-cost/index.html | sort | uniq -c
```

Expected: `fs-title` ×1, `fs-ship` ×1, `form-2up` ×2, `fld` ×4. The full-page contrast sweep runs in Task 14.

- [ ] **Step 6: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "fix(adoption-cost): rewire the inquiry form to the kit classes it was styled for

- .form-actions (a button row) was doing duty as a 2-field row with no
  flex basis, so name/email sized to content and wrapped ragged -> new
  .form-2up grid with min-width:0 on children
- labels were siblings of their controls, 12px from their own field and
  12px from the next -> wrapped in .fld
- panel used unstyled .form-head/.form-note while .fs-title/.fs-ship sat
  unused; .form-note measured 3.34:1 on the dark panel (AA fail)
- .form-eyebrow clay-on-dark corrected to #f08070"
```

---

## Task 3: Table G caption — mobile step-down ("the title is too thick")

`.tg caption` is 1.05rem/700 Newsreader, white on solid `--f` green with `12px 16px` padding, and the `@media(max-width:640px)` block restyles every part of the table *except* the caption. At 360px "The True-Cost Ledger — three routes, three horizons" wraps to three heavy lines and reads as a slab.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro:1179–1185`

- [ ] **Step 1: Confirm the caption has no mobile rule**

```bash
cd /Users/apple/Downloads/CAG
sed -n '1178,1186p' src/pages/african-grey-parrot-adoption-cost/index.astro | grep -c caption
```

Expected: `0`. That is the defect.

- [ ] **Step 2: Add the caption step-down inside the existing mobile block**

Insert as the first declaration after the `@media(max-width:640px){` line that opens at 1178:

```css
  .tg caption{font-size:.92rem;font-weight:600;line-height:1.3;padding:10px 12px;letter-spacing:0}
```

Dropping weight 700→600 and 1.05rem→.92rem takes the caption to two lines at 360px and removes the slab effect while staying above the 16px-equivalent readability floor for a non-control element. White on `#2D6A4F` is 7.4:1, so weight can safely drop.

- [ ] **Step 3: Rebuild and verify the rule is in the mobile block**

```bash
npx astro build 2>&1 | tail -3
grep -o '@media(max-width:640px){[^}]*\.tg caption{[^}]*}' dist/african-grey-parrot-adoption-cost/index.html | head -1
```

Expected: one match containing `font-size:.92rem`.

- [ ] **Step 4: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "fix(adoption-cost): step the True-Cost Ledger caption down on mobile

The 640px block restyled every part of .tg except the caption, so a
1.05rem/700 serif line wrapped to three heavy lines at 360px."
```

---

## Task 4: Unwind the absolutely-positioned hero art (the one static WARN)

`page_hardening_scan.py` reports `absolute-hero-not-unwound` at line 769: `.hero-tile-p` is absolutely positioned and never reset below 980px. Per hardening skill §1d the fix is to remove the mechanism, not tune offsets.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro:769` and the `@media(max-width:900px)` block

- [ ] **Step 1: Reproduce the warning and read the current rule**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/page_hardening_scan.py african-grey-parrot-adoption-cost
sed -n '763,775p' src/pages/african-grey-parrot-adoption-cost/index.astro
```

Expected: 1 WARN naming `.hero-tile-p`. Read the surrounding `.hero-imgs` grid to see whether `.hero-tile-p` is a price-ladder label pinned *inside* a tile.

- [ ] **Step 2: Decide by what the element actually is**

Per §1d, a caption or badge pinned **inside** a hero card is correct and the scanner is expected to ignore it. If `.hero-tile-p` is a price label inside a `.hero-tile`, whose parent is `position:relative`, this is a **false positive** — do not restructure the hero. Instead confirm the parent is relative:

```bash
grep -n '\.hero-tile{' src/pages/african-grey-parrot-adoption-cost/index.astro
```

If the parent has `position:relative`, add a scanner exemption rather than editing the page — that is the §1 discipline (fix the check, not the page). Add `hero-tile-p` to the badge/caption allowlist in `scripts/page_hardening_scan.py` and record why in the commit.

If instead `.hero-tile-p` positions a whole **tile** against the hero grid, it is a real defect: give `.hero-imgs` a `1fr 1fr` grid, set `.hero-tile-p{position:relative;width:100%}`, and get the stagger from `transform:rotate()` per tile.

- [ ] **Step 3: Re-run the scan to zero**

```bash
python3 scripts/page_hardening_scan.py african-grey-parrot-adoption-cost
```

Expected: `0 ERROR · 0 WARN`.

- [ ] **Step 4: Commit**

```bash
git add -u
git commit -m "fix(adoption-cost): resolve absolute-hero-not-unwound warning"
```

---

## Task 5: Process the 8 dropped infographics into the uniform box

All 8 stems match prompt-pack §7c slots INF-1…INF-8 exactly (the pack named `.png`, the breeder delivered `.webp`). The 6 OG photos are already processed and in `public/` from commit `54e2601` — they only need referencing, which happens in Task 6.

**Files:**
- Create: 16 files in `public/` (8 masters at 1408×768 + 8 `-760` siblings)
- Read: `assets/1WORKING-ON/FOR-SALE-PAGES/BABY-african-grey-parrot/`

- [ ] **Step 1: Open and proof every file before processing**

Non-negotiable — trap #16 in the skill's failure log ("BREDDER", "HOME HOME", garbled "Sukaltane") and the 5 rejects from `54e2601` both came from trusting filenames. Use the Read tool on each of the 8 files and confirm: the bird shown is an African Grey (not a green Amazon or conure), all baked-in text is spelled correctly, no figure contradicts the ledger (the guarantee is **72-hour**, never "7 day"; shipping is **US-only**, never "worldwide"), and no AI sparkle watermark is present.

Record a verdict line per file. Any reject is reported to the breeder with the reason — never silently substituted.

- [ ] **Step 2: Confirm all 8 are present and note which need a spec-panel crop**

```bash
cd /Users/apple/Downloads/CAG
D="assets/1WORKING-ON/FOR-SALE-PAGES/BABY-african-grey-parrot"
for f in african-grey-adoption-fee-vs-true-cost-iceberg african-grey-day-one-money-breakdown \
         african-grey-cost-by-acquisition-route-stacked african-grey-five-year-cost-curve \
         what-a-cheap-african-grey-really-costs adoption-cost-african-grey-delivery-options \
         what-an-adoption-fee-does-not-cover african-grey-cost-by-decade-forty-year-timeline; do
  printf "%-56s " "$f"
  python3 -c "
from PIL import Image; im=Image.open('$D/$f.webp'); print(im.size, '%.3f'%(im.size[0]/im.size[1]))" 2>&1
done
```

Expected: 8 lines, no errors. A ratio near `1.833` means a 1408×768 export. **If an image is 1408×768 with a baked-in spec panel on the right ~28%** (palette swatches, a literal "1408×768" label, a negative list), crop to the left 73.5% first — that is the AI reference-card lesson from the egg build.

- [ ] **Step 3: Process to the locked uniform box**

```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
from PIL import Image, ImageOps
import os
D = "assets/1WORKING-ON/FOR-SALE-PAGES/BABY-african-grey-parrot"
OUT = "public"
NAMES = ["african-grey-adoption-fee-vs-true-cost-iceberg",
         "african-grey-day-one-money-breakdown",
         "african-grey-cost-by-acquisition-route-stacked",
         "african-grey-five-year-cost-curve",
         "what-a-cheap-african-grey-really-costs",
         "adoption-cost-african-grey-delivery-options",
         "what-an-adoption-fee-does-not-cover",
         "african-grey-cost-by-decade-forty-year-timeline"]
for n in NAMES:
    im = Image.open(f"{D}/{n}.webp").convert("RGB")
    # infographics carry baked-in text: fit the 16:9 box centred, never a focal crop
    big = ImageOps.fit(im, (1408, 768), Image.LANCZOS, centering=(0.5, 0.5))
    for path, img in ((f"{OUT}/{n}.webp", big), (f"{OUT}/{n}-760.webp", big.resize((760, 415), Image.LANCZOS))):
        for q in range(82, 39, -3):
            img.save(path, "WEBP", quality=q, method=6)
            if os.path.getsize(path) < 95_000:
                break
        print(f"{os.path.basename(path):<62} q={q} {os.path.getsize(path)//1024} KB")
PY
```

Expected: 16 lines, every size under 95 KB.

- [ ] **Step 4: Verify the text survived compression**

Use the Read tool on 3 of the processed `public/*.webp` files, including the densest (`african-grey-cost-by-decade-forty-year-timeline.webp`). Every label must still be legible. If any is mushy, re-run that file with a `quality` floor of 70 and accept a larger file — legible text outranks the 95 KB target for infographics.

- [ ] **Step 5: Commit**

```bash
git add public/*.webp
git commit -m "feat(adoption-cost): process the 8 dropped infographics into the 16:9 box

All 8 stems match prompt-pack 7c slots INF-1..INF-8. Proofed every master
by opening it before processing; ImageOps.fit centred (never a focal crop
- these carry baked-in text), WebP method=6 quality-walk under 95 KB, plus
-760 siblings."
```

---

## Task 6: Place all 14 in-body images (the single biggest "feels rushed" fix)

The page currently renders **zero** in-body images: all 25 `<img>` are 10 seam emblems, 7 bird-card thumbs, 2 review avatars and chrome. `.sec-img.inf-img` — the locked uniform box — is styled but never used, against the spec's "every H2, H3 and key H4 gets an image". Six OG photos have sat orphaned in `public/` since `54e2601`.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` (frontmatter + 8 sections)

- [ ] **Step 1: Prove the page renders no content images**

```bash
cd /Users/apple/Downloads/CAG
echo "total img:  $(grep -o '<img' dist/african-grey-parrot-adoption-cost/index.html | wc -l)"
echo "sec-img:    $(grep -o '<img class="sec-img' dist/african-grey-parrot-adoption-cost/index.html | wc -l)"
grep -o 'src="/[^"]*\.webp"' dist/african-grey-parrot-adoption-cost/index.html | sort -u | wc -l
```

Expected: 25 total, **0** `sec-img`, 12 unique sources (all chrome/cards/avatars).

- [ ] **Step 2: Add the image map to frontmatter**

Insert after the `faqs` array (around line 180). Rule 50b is binding: the **primary** keyword goes in the primary image's alt only, and no two alts on the page may repeat a keyword type.

```astro
// ---- In-body images. Rule 50b: primary keyword in the FIRST image alt only;
// every other alt rotates a different keyword type. inf = infographic (16:9,
// object-fit:contain, never cover-cropped); og = real photo (5:4 mobile frame).
const figs = {
  inf1: { src: "/african-grey-adoption-fee-vs-true-cost-iceberg.webp", kind: "inf",
    alt: "African Grey parrot adoption cost broken into the fee above the line and the eight costs below it",
    cap: "The fee is the visible tenth. Everything under the waterline is the part rescues and marketplaces leave off the listing." },
  inf7: { src: "/what-an-adoption-fee-does-not-cover.webp", kind: "inf",
    alt: "What an African Grey rescue adoption fee does not include, itemised against what it does",
    cap: "Nine line items a published adoption fee routinely excludes." },
  inf3: { src: "/african-grey-cost-by-acquisition-route-stacked.webp", kind: "inf",
    alt: "African Grey parrot adoption cost by route, stacked across rescue, breeder and online listing",
    cap: "Three routes, stacked. Day one separates them; year five does not." },
  inf4: { src: "/african-grey-five-year-cost-curve.webp", kind: "inf",
    alt: "How much an African Grey costs over five years, plotted as two converging curves",
    cap: "The curves converge because a Grey eats and sees a vet at the same rate however you acquired it." },
  inf2: { src: "/african-grey-day-one-money-breakdown.webp", kind: "inf",
    alt: "African Grey parrot day one cost breakdown covering bird, cage, travel and first vet visit",
    cap: "Every dollar that leaves your account in week one." },
  inf8: { src: "/african-grey-cost-by-decade-forty-year-timeline.webp", kind: "inf",
    alt: "Lifetime cost of owning an African Grey, totalled by decade across forty years",
    cap: "Decade by decade. The bird outlives most of the equipment you buy for it." },
  inf5: { src: "/what-a-cheap-african-grey-really-costs.webp", kind: "inf",
    alt: "Cheap African Grey parrot true cost, comparing a below-floor listing against a documented bird",
    cap: "What the saving costs you in the eighteen months after the bird lands." },
  inf6: { src: "/adoption-cost-african-grey-delivery-options.webp", kind: "inf",
    alt: "African Grey parrot delivery cost across airport cargo, home delivery and flight nanny tiers",
    cap: "Three ways home, three prices, all published." },
  og1: { src: "/african-greys-available-price-bands.webp", kind: "og", pos: "center 30%",
    alt: "Seven documented African Greys we currently hold, arranged by the price band each falls into",
    cap: "The range of birds behind the range of prices." },
  og5: { src: "/african-grey-on-travel-carrier-day-one.webp", kind: "og", pos: "center 35%",
    alt: "Hand-raised Grey perched on its travel carrier the morning it leaves our Midland aviary",
    cap: "Day one, from our side of it." },
  og3: { src: "/living-with-an-african-grey-running-costs.webp", kind: "og", pos: "center 30%",
    alt: "Grey on a play stand in a family living room, the setting the annual running cost pays for",
    cap: "What the recurring line items actually buy." },
  og4: { src: "/african-grey-fresh-produce-annual-food-cost.webp", kind: "og", pos: "center 45%",
    alt: "Fresh chop bowl of produce prepared for our Greys, the food line in the annual budget",
    cap: "One morning's chop. Roughly a fifth of the annual food line." },
  og6: { src: "/african-grey-toy-enrichment-line-item.webp", kind: "og", pos: "center 28%",
    alt: "One of our Greys shoulder-perched with a foraging toy, the enrichment line item in practice",
    cap: "Toys are consumable. Budget them as recurring, not once." },
  og2: { src: "/african-grey-forty-year-family-commitment.webp", kind: "og", pos: "center 32%",
    alt: "Older owner holding a settled Grey, the forty-year commitment the money question sits inside",
    cap: "The forty-year question is not really about money." },
};
```

- [ ] **Step 3: Add a single figure helper so no markup is repeated**

Insert immediately after the `figs` object:

```astro
const fig = (k: string) => {
  const f = figs[k as keyof typeof figs];
  return { ...f, srcset: `${f.src.replace(".webp", "-760.webp")} 760w, ${f.src} 1408w` };
};
```

- [ ] **Step 4: Place the figures, one per section, using this exact block**

For each placement below, insert this markup after the section's opening paragraph (never between a heading and its paragraph — the opening paragraph must stay adjacent to its header):

```astro
        {(() => { const f = fig("inf1"); return (
          <figure class="sec-fig">
            <img class={`sec-img ${f.kind === "inf" ? "inf-img" : "og-photo"}`} src={f.src} srcset={f.srcset}
              sizes="(max-width:900px) 92vw, 760px" width="1408" height="768"
              style={f.kind === "og" ? `object-position:${(f as any).pos}` : undefined}
              loading="lazy" decoding="async" alt={f.alt} />
            <figcaption>{f.cap}</figcaption>
          </figure>
        ); })()}
```

Placement map — 14 figures across 8 sections:

| Section | id | Figures, in order |
|---|---|---|
| 01 What a Grey Costs | `cost` | `inf1`, `og1` |
| 02 Rescue Fees | `rescue` | `inf7` |
| 03 Three Routes Priced | `routes` | `inf3` (before Table G), `inf4` (after Table G) |
| 04 Day One | `dayone` | `inf2`, `og5` |
| 05 Every Year After | `ongoing` | `og3`, `og4`, `og6`, `inf8`, `og2` |
| 06 Under $1,000 | `cheap` | `inf5` |
| 07 Getting Home | `shipping` | `inf6` |

- [ ] **Step 5: Add the `.sec-fig` caption rule**

`.sec-img`, `.inf-img` and `.og-photo` are already styled. Only the `<figure>` wrapper and caption need a rule. Append after the `.sec-img` block:

```css
.sec-fig{margin:18px 0 20px;max-width:760px}
.sec-fig figcaption{font-size:.8rem;color:var(--mid);line-height:1.45;margin-top:8px;font-style:italic;max-width:70ch}
```

- [ ] **Step 6: Verify count, uniqueness of alts, and that no infographic is cover-cropped**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
echo "sec-img rendered: $(grep -o '<img class="sec-img' dist/african-grey-parrot-adoption-cost/index.html | wc -l)  (expect 14)"
echo "inf-img: $(grep -o 'inf-img' dist/african-grey-parrot-adoption-cost/index.html | wc -l)  og-photo: $(grep -o 'og-photo' dist/african-grey-parrot-adoption-cost/index.html | wc -l)"
python3 -c "
import re
h=open('dist/african-grey-parrot-adoption-cost/index.html').read()
a=re.findall(r'<img class=\"sec-img[^>]*alt=\"([^\"]+)\"',h)
print('alts:',len(a),'unique:',len(set(a)))
assert len(a)==len(set(a)), 'DUPLICATE ALT - Rule 50b violation'
print('no duplicate alts OK')"
for f in $(grep -o 'src="/[^"]*\.webp"' dist/african-grey-parrot-adoption-cost/index.html | sed 's/src="//;s/"//' | sort -u); do
  [ -f "public$f" ] || echo "MISSING ASSET: $f"; done
echo "asset check done"
```

Expected: 14 `sec-img`, 8 `inf-img`, 6 `og-photo`, no duplicate alts, no missing assets.

- [ ] **Step 7: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "feat(adoption-cost): place all 14 in-body images

The page shipped with ZERO content images - every img was a seam emblem,
bird-card thumb, avatar or chrome - while .sec-img.inf-img was styled and
unused and 6 processed OG photos sat orphaned in public/ since 54e2601.
Adds 8 infographics + 6 photos across 8 sections, one shared figure
helper, Rule 50b alt rotation with no repeated keyword type."
```

---

## Task 7: Render `.doc-stack` in §dayone ("Every Grey Leaves With")

Mandated by the locked cluster specs ("'Every grey leaves with' renders as a `.doc-stack` numbered-badge list, not the green-header band card"). CSS ships at lines 890–897; markup never existed.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` §`dayone`

- [ ] **Step 1: Confirm the CSS exists and the markup does not**

```bash
cd /Users/apple/Downloads/CAG
grep -c '^\.doc-stack\|^\.ds-title\|^\.ds-list' src/pages/african-grey-parrot-adoption-cost/index.astro
grep -c 'class="doc-stack"' src/pages/african-grey-parrot-adoption-cost/index.astro
```

Expected: a non-zero CSS count and `0` markup.

- [ ] **Step 2: Insert the component inside §dayone, under the existing H4, with no new heading**

`.ds-title` is a styled `<p>`, not a heading — that is deliberate, so the approved outline is untouched.

```astro
        <div class="doc-stack">
          <p class="ds-title">Every Grey Leaves With</p>
          <ol class="ds-list">
            <li><b>DNA sex certificate</b><span>Avian Biotech / Animal Genetics, ~99% accuracy, $40–60 and itemised — never bundled invisibly</span></li>
            <li><b>CITES Appendix I file</b><span>Captive-bred, US-only transfer paperwork, legal to own and move domestically</span></li>
            <li><b>PBFD and Polyomavirus PCR results</b><span>Screened per bird, dated, with the lab name on the report</span></li>
            <li><b>Avian-vet health certificate</b><span>Signed within the window that makes the 72-hour guarantee enforceable</span></li>
            <li><b>Hatch and weaning record</b><span>Hatch date, the 12–16 week weaning timeline, and what the chick was weaned onto</span></li>
            <li><b>Diet and care sheet</b><span>The pellet brand the bird is already on, so week one changes nothing</span></li>
          </ol>
        </div>
```

Every claim here is inside the Verified-Claim Ledger. Do not add a guarantee duration other than **72-hour**, and do not assert anything not listed above.

- [ ] **Step 3: Verify it renders and the heading count is unchanged**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
grep -c 'class="doc-stack"' dist/african-grey-parrot-adoption-cost/index.html
python3 -c "
import re; h=open('dist/african-grey-parrot-adoption-cost/index.html').read()
m=h[h.find('<main'):h.find('</main>')]
print({f'H{i}':len(re.findall(f'<h{i}[ >]',m)) for i in range(1,7)})"
```

Expected: `1`, and the H-level counts must match the pre-task baseline exactly — H1:1, and ≥5 H5 and ≥5 H6 still hold.

- [ ] **Step 4: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "feat(adoption-cost): render the mandated .doc-stack in the day-one section

CSS shipped since the original build; markup never existed. .ds-title is a
styled <p>, so the approved H1-H6 outline is unchanged."
```

---

## Task 8: Render the `.otA` GEO fact tables

Mandated by skill §6a ("**GEO fact tables** … signal authority to answer engines"). CSS ships at 860–866, unused.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` §`ongoing` and §`shipping`

- [ ] **Step 1: Confirm CSS present, markup absent**

```bash
cd /Users/apple/Downloads/CAG
grep -c '^\.otA' src/pages/african-grey-parrot-adoption-cost/index.astro && grep -c 'class="otA"' src/pages/african-grey-parrot-adoption-cost/index.astro
```

Expected: non-zero, then `0`.

- [ ] **Step 2: Insert the annual-cost fact table in §ongoing**

```astro
        <div class="otA">
          <table>
            <thead><tr><th scope="col">Annual line item</th><th scope="col">Typical range</th><th scope="col">What drives it</th></tr></thead>
            <tbody>
              <tr><td><b>Pellets and seed</b><span class="sub">Harrison's, Roudybush, TOP's or Zupreem Natural</span></td><td>$240–$420</td><td>Brand and whether you buy in bulk</td></tr>
              <tr><td><b>Fresh produce</b><span class="sub">Chop, prepared in batches</span></td><td>$300–$600</td><td>Season and how much you waste</td></tr>
              <tr><td><b>Toys and foraging</b><span class="sub">Consumable by design</span></td><td>$180–$400</td><td>A Grey destroys wood faster than plastic</td></tr>
              <tr><td><b>Routine avian vet</b><span class="sub">Annual well-bird exam</span></td><td>$120–$300</td><td>Whether bloodwork is included</td></tr>
              <tr><td><b>Perches and substrate</b><span class="sub">Replaced, not bought once</span></td><td>$60–$150</td><td>Cage size</td></tr>
            </tbody>
          </table>
        </div>
```

- [ ] **Step 3: Insert the delivery fact table in §shipping**

```astro
        <div class="otA">
          <table>
            <thead><tr><th scope="col">Route home</th><th scope="col">Cost</th><th scope="col">How it works</th></tr></thead>
            <tbody>
              <tr><td><b>Airport cargo pickup</b><span class="sub">IATA Live Animal Regulations</span></td><td>$185</td><td>Delta, United or American cargo; you collect at the counter</td></tr>
              <tr><td><b>Home delivery</b><span class="sub">Door to door</span></td><td>$350</td><td>Climate-controlled courier, documents handed over on arrival</td></tr>
              <tr><td><b>Flight nanny</b><span class="sub">In-cabin, accompanied</span></td><td>From $700</td><td>Availability depends on route and season</td></tr>
              <tr><td><b>Midland, TX pickup</b><span class="sub">Within two to three hours of us</span></td><td>Free</td><td>You meet the bird at the aviary before it travels</td></tr>
            </tbody>
          </table>
        </div>
```

Cross-check `$185` / `$350` / `$700` against `data/financial-entities.json` (`delivery_options`) and `data/price-matrix.json` before committing. **Never hardcode a figure that disagrees with those files** — read them and correct the table if they differ.

- [ ] **Step 4: Verify both render and stack on mobile**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
grep -o 'class="otA"' dist/african-grey-parrot-adoption-cost/index.html | wc -l
grep -o '@media[^{]*{[^}]*\.otA' dist/african-grey-parrot-adoption-cost/index.html | head -2
```

Expected: `2`. If no mobile rule exists for `.otA`, add one mirroring `.tg`'s stacking recipe (`data-label` on each `td`, `thead` clipped, first cell as a header band) inside the `@media(max-width:640px)` block — the memory `reference_mobile_table_stacking` carries the full recipe.

- [ ] **Step 5: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "feat(adoption-cost): render the two mandated .otA GEO fact tables

Annual running-cost table in ongoing, delivery-tier table in shipping.
Figures cross-checked against financial-entities.json + price-matrix.json."
```

---

## Task 9: Render `.vflags` in §cheap (green-flag verification ledger)

CSS ships at 807–820 under the comment "V-FLAGS — green-flag verification ledger" and was never rendered. §cheap is the anti-scam warning section, so this is its natural home and it strengthens the negative-keyword counter-positioning the skill requires.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` §`cheap`

- [ ] **Step 1: Confirm CSS present, markup absent**

```bash
cd /Users/apple/Downloads/CAG
grep -c '^\.vflags\|^\.vf-badge\|^\.vf-txt' src/pages/african-grey-parrot-adoption-cost/index.astro && grep -c 'class="vflags"' src/pages/african-grey-parrot-adoption-cost/index.astro
```

Expected: non-zero, then `0`.

- [ ] **Step 2: Insert the ledger**

`.vf-badge svg` is `16×16` — an inline Feather-style check SVG, never an emoji (DESIGN.md §Iconography; 🦜 and pictograph emoji are banned site-wide).

```astro
        <div class="vflags">
          <div class="vflags-head">
            <p class="vflags-kicker">Green flags, not red ones</p>
            <p class="vflags-title">Five Things a Real Breeder Can Show You in Sixty Seconds</p>
          </div>
          <ul class="vflags-list">
            <li>
              <span class="vf-badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg></span>
              <span class="vf-txt"><b>A USDA licence number you can look up</b><span>Ours is verifiable through the APHIS public search, not just quoted at you</span></span>
            </li>
            <li>
              <span class="vf-badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg></span>
              <span class="vf-txt"><b>A live video call with the bird you are buying</b><span>Not a photo set. A scammer cannot produce the specific bird on demand</span></span>
            </li>
            <li>
              <span class="vf-badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg></span>
              <span class="vf-txt"><b>A named avian vet who will confirm the practice</b><span>You should be able to phone the clinic yourself</span></span>
            </li>
            <li>
              <span class="vf-badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg></span>
              <span class="vf-txt"><b>Prices that sit above the floor and stay there</b><span>A documented Grey does not drop to $800 because you hesitated</span></span>
            </li>
            <li>
              <span class="vf-badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg></span>
              <span class="vf-txt"><b>A written guarantee with a window and a remedy</b><span>Ours is 72 hours from arrival, with the covered conditions published</span></span>
            </li>
          </ul>
        </div>
```

- [ ] **Step 3: Verify no raw SVG leaked as escaped text**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
grep -c 'class="vflags"' dist/african-grey-parrot-adoption-cost/index.html
grep -c '&lt;svg' dist/african-grey-parrot-adoption-cost/index.html || echo "no escaped svg OK"
```

Expected: `1`, then "no escaped svg OK". Escaped SVG means a data-array icon needed `set:html` — but these are literal inline SVGs, so it should be clean.

- [ ] **Step 4: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "feat(adoption-cost): render the .vflags green-flag ledger in the under-\$1,000 section

CSS carried the 'V-FLAGS - green-flag verification ledger' comment since
the original build with no markup behind it. Inline Feather check SVGs,
never emoji. All five claims inside the Verified-Claim Ledger."
```

---

## Task 10: Render `.chkB` in §rescue (due-diligence checklist)

CSS ships at 899–907 and even has a mobile rule (`.chkB-grid{grid-template-columns:1fr}`) — styling written for markup that never arrived.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` §`rescue`

- [ ] **Step 1: Confirm CSS present, markup absent**

```bash
cd /Users/apple/Downloads/CAG
grep -c '^\.chkB' src/pages/african-grey-parrot-adoption-cost/index.astro && grep -c 'class="chkB"' src/pages/african-grey-parrot-adoption-cost/index.astro
```

Expected: non-zero, then `0`.

- [ ] **Step 2: Insert the checklist**

`.chkB-grid li::before` already draws the `✓`, so do **not** put a tick in the markup. `.chkB-title` is a styled `<p>`, keeping the outline intact.

```astro
        <div class="chkB">
          <div class="chkB-head">
            <p class="chkB-eyebrow">Before you send a rescue any money</p>
            <p class="chkB-title">Eight Questions Worth Asking a Rescue First</p>
          </div>
          <ul class="chkB-grid">
            <li><b>Why was the bird surrendered?</b><span>Plucking, biting and screaming are common and workable — but you should be told</span></li>
            <li><b>How long has it been in care?</b><span>A settled bird and a fresh intake are different propositions</span></li>
            <li><b>Has it been vet-checked since intake?</b><span>Ask for the date and the clinic</span></li>
            <li><b>Is the sex confirmed, and how?</b><span>Most rescue birds arrive unsexed; a guess is not a certificate</span></li>
            <li><b>What is the actual age?</b><span>Often unknown, which matters across a forty-year commitment</span></li>
            <li><b>What does the fee include?</b><span>Rarely the cage, rarely transport, sometimes not the vet work</span></li>
            <li><b>Is there a home-check or contract?</b><span>Good rescues have both; some retain ownership permanently</span></li>
            <li><b>Can you meet the bird more than once?</b><span>A Grey chooses people. One visit is not enough to know</span></li>
          </ul>
        </div>
```

This is written from the adoption-cost angle (fee scope, unknown age, unconfirmed sex) so it will not collide with hand-raised's due-diligence checklist in the dup-gate. Task 15 proves that.

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
grep -c 'class="chkB"' dist/african-grey-parrot-adoption-cost/index.html
```

Expected: `1`.

- [ ] **Step 4: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "feat(adoption-cost): render the .chkB due-diligence checklist in the rescue section

Written from this page's cost angle (fee scope, unknown age, unconfirmed
sex) so it does not collide with the hand-raised checklist."
```

---

## Task 11: Render `.fs-video` in §reserve

CSS ships at 988–992 (plus a legacy `.video-wrap` at 849–850) and is unused. Source clip: `assets/1WORKING-ON/FOR-SALE-PAGES/BABY-african-grey-parrot/rony-and-rose-with-real-paper-midland-tx.mp4`.

**Files:**
- Create: `public/rony-and-rose-real-paperwork-midland-tx.mp4`, `public/rony-and-rose-real-paperwork-poster-760.webp`
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` §`reserve`

- [ ] **Step 1: Watch the clip before shipping it**

Confirm the birds are African Greys, no unidentified person is shown who could be miscaptioned as Mark or Teri, and no on-screen text contradicts the ledger. If it fails any of these, skip this task and report it — do not substitute another clip silently.

- [ ] **Step 2: Copy the clip and cut a poster from its first frame**

```bash
cd /Users/apple/Downloads/CAG
S="assets/1WORKING-ON/FOR-SALE-PAGES/BABY-african-grey-parrot/rony-and-rose-with-real-paper-midland-tx.mp4"
cp "$S" public/rony-and-rose-real-paperwork-midland-tx.mp4
ls -la public/rony-and-rose-real-paperwork-midland-tx.mp4
```

If the file exceeds ~5 MB, note it for the backlog rather than transcoding — `ffmpeg` is not installed in this environment (memory `reference_perf_image_tooling`). For the poster, reuse an existing processed asset rather than extracting a frame:

```bash
cp public/african-greys-available-price-bands-760.webp public/rony-and-rose-real-paperwork-poster-760.webp
```

- [ ] **Step 3: Insert the video component — `preload="none"`, no autoplay**

Design rule: max 0.2s transitions, **no auto-playing video**.

```astro
        <figure class="fs-video">
          <div class="fs-video-frame">
            <span class="fs-video-tag">Our aviary · Midland, TX</span>
            <video controls preload="none" poster="/rony-and-rose-real-paperwork-poster-760.webp" width="1408" height="768">
              <source src="/rony-and-rose-real-paperwork-midland-tx.mp4" type="video/mp4" />
            </video>
          </div>
          <figcaption>Rony and Rose with the paperwork that travels with them — the file every price on this page includes.</figcaption>
        </figure>
```

Do not add fallback text inside `<video>`: the contrast sweep in Task 14 skips `<video>` descendants because that text never renders, so any copy there is invisible and unauditable.

- [ ] **Step 4: Verify the asset resolves**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
grep -o 'class="fs-video"' dist/african-grey-parrot-adoption-cost/index.html | wc -l
for f in $(grep -oE 'src="/[^"]*\.(mp4|webp)"' dist/african-grey-parrot-adoption-cost/index.html | sed 's/src="//;s/"//' | sort -u); do [ -f "public$f" ] || echo "MISSING: $f"; done; echo "assets OK"
```

Expected: `1`, then "assets OK" with no MISSING lines.

- [ ] **Step 5: Commit**

```bash
git add public/rony-and-rose-real-paperwork-midland-tx.mp4 public/rony-and-rose-real-paperwork-poster-760.webp src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "feat(adoption-cost): render the .fs-video component in the reserve section

controls + preload=none, no autoplay per the design rules."
```

---

## Task 12: Close the 5 headings with no opening paragraph, and delete the orphan H6

12 of 63 headings have no substantive following paragraph. Seven are legitimate — bird-card names (`Evie`, `Elad`, `Bery`, `Roys`, `Amie`, `Jins & Jeni`) and `Which Bird Fits Which Budget?` are card/filter labels whose next element is a component, not prose. Five are real defects. The worst is an H6 followed **directly by an H2** — zero body copy at all.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` §`routes`, §`shipping`, §`reserve`, `#inquire`, and the read-cards block

- [ ] **Step 1: Re-run the audit to get the current list**

```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
import re,html
h=open('dist/african-grey-parrot-adoption-cost/index.html').read()
b=h[h.find('<main'):h.find('</main>')]
b=re.sub(r'<(script|style)[^>]*>.*?</\1>','',b,flags=re.S)
seq=[]
for m in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>|<p[^>]*>(.*?)</p>',b,flags=re.S):
    if m.group(1): seq.append(('H'+m.group(1)[1],html.unescape(re.sub(r'<[^>]+>','',m.group(2))).strip()))
    else: seq.append(('P',html.unescape(re.sub(r'<[^>]+>','',m.group(3))).strip()))
for i,(k,t) in enumerate(seq):
    if k.startswith('H'):
        n=seq[i+1] if i+1<len(seq) else ('END','')
        if n[0]!='P' or len(n[1])<80: print(k,'|',t[:66],'-> next:',n[0],repr(n[1][:34]))
PY
```

Expected: 12 lines. Only the 5 addressed below are defects.

- [ ] **Step 2: Delete the orphan H6 — a heading with no content is worse than no heading**

Find the H6 reading `From the Ledger: Airport $185, Home $350, Flight Nanny From $700` in §`shipping` and **convert its content into a real paragraph** rather than deleting the level (the gate requires ≥5 H6). Give it body copy:

```astro
        <h6 class="cag-h6">From the Ledger: Airport $185, Home $350, Flight Nanny From $700</h6>
        <p>Those three numbers are the whole delivery menu, and they have not moved this year. Airport cargo is the one most buyers pick because it is the cheapest and the fastest; home delivery costs $165 more and buys you not having to find the cargo counter at your own airport. The flight-nanny figure starts at $700 because it depends entirely on the route and the season, so we quote it per bird rather than publishing a flat rate we would have to break.</p>
```

Then re-check the H6 count is still ≥5.

- [ ] **Step 3: Add an opening paragraph under the calculator H4 (§routes)**

Before the `<div class="ctool">`, after the H4 `How Do You Estimate the Cost for Your Own Setup?`:

```astro
        <p>Set the four inputs below to your own situation and the calculator returns a range rather than an average, because an average across three acquisition routes describes nobody. Pick the bird you are actually considering, how it would travel, what you already own, and how far ahead you want to look.</p>
```

- [ ] **Step 4: Add an opening paragraph under the shipping H4 (§shipping)**

After `How Much Is Shipping for an African Grey Parrot?`, before the ship cards:

```astro
        <p>Between $185 and $350 for the two routes most buyers use, and free if you can reach Midland within two to three hours. Shipping is a published line item here rather than something quoted after you have committed, because a delivery cost that appears late is one of the clearest scam tells in this market.</p>
```

- [ ] **Step 5: Add opening paragraphs under the two remaining H3s**

Under `What Should You Read Next Before You Commit?`, before `.read-cards`:

```astro
        <p>Three pages go deeper than a cost page usefully can: what the money buys year after year, how the guarantee behind every price actually works, and how long the commitment really runs.</p>
```

Under `How Do You Reserve One of These Birds?` in `#inquire`, before `.form-wrap`:

```astro
        <p>Tell us which bird and how you would like it to travel, and Mark or Teri replies within twenty-four hours — in person, not from a template. A deposit holds a bird; nothing on this page asks you to commit before you have seen its paperwork.</p>
```

- [ ] **Step 6: Re-audit and confirm only the 7 legitimate card labels remain**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
# re-run the Step 1 script
```

Expected: exactly 7 remaining, all of them bird-card names or the `Which Bird Fits Which Budget?` filter label.

- [ ] **Step 7: Confirm the heading gate still passes**

```bash
python3 -c "
import re; h=open('dist/african-grey-parrot-adoption-cost/index.html').read()
m=h[h.find('<main'):h.find('</main>')]
c={f'H{i}':len(re.findall(f'<h{i}[ >]',m)) for i in range(1,7)}
print(c)
assert c['H1']==1 and c['H5']>=5 and c['H6']>=5, 'HEADING GATE FAIL'
print('gate OK')"
```

- [ ] **Step 8: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "fix(adoption-cost): give 5 headings the opening paragraph the spec requires

Includes an H6 that was followed directly by an H2 with zero body copy.
The 7 remaining bare headings are bird-card names and a filter label,
whose next element is a component rather than prose - not defects."
```

---

## Task 13: Delete the genuinely dead CSS

After Tasks 7–11, the never-rendered component CSS is down from 12 families to a handful. Deleting the rest makes the file honest and keeps the next reader from assuming a component exists.

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` (`<style>` block)

- [ ] **Step 1: Re-run the drift audit to get the current dead list**

```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
import re
src=open('src/pages/african-grey-parrot-adoption-cost/index.astro').read()
i=src.find('<style>'); css,markup=src[i:],src[:i]
used=set()
for m in re.finditer(r'class(?:Name)?="([^"{}]+)"',markup): used.update(m.group(1).split())
for m in re.finditer(r'class(?:Name)?=\{`([^`]*)`\}',markup):
    used.update(re.findall(r'[A-Za-z][\w-]*',re.sub(r'\$\{[^}]*\}',' ',m.group(1))))
for m in re.finditer(r'class(?:Name)?=\{[^}]*?"([^"]+)"',markup): used.update(m.group(1).split())
# only look at real CSS selectors, not JS property accesses in the script block
css_only=css[:css.find('<script')] if '<script' in css else css
defined=set(re.findall(r'^\.([A-Za-z][\w-]*)',css_only,re.M))
print("DEAD CSS (%d):"%len(defined-used)); [print('  .'+c) for c in sorted(defined-used)]
PY
```

- [ ] **Step 2: Delete only families with zero remaining markup**

Expected dead families after Tasks 7–11: `.bird-*` (10 rules — superseded by `.availB-*`), `.pair-*` (4), `.k1`/`.k1-title` (the page ships K2), `.faq-open`/`.faq-q` (light FAQ variant — the page ships FAQ-C), `.video-wrap` (superseded by `.fs-video`), `.cost-tool`, `.final-cta`, `.nl-inflow`, `.cvt-toc`, `.ship-mini`, `.ship-places`, `.geo-pin`/`.geo-body`/`.geo-arrow` **only if** the geo cards genuinely do not use them.

**Check `.geo-*` before deleting** — the locked spec requires the geo route-card to carry a pin, keyword, note and arrow. If the markup lacks them, that is a *missing component*, not dead CSS: render the internals instead of deleting the rules. Read the `.geo-cards` markup and decide.

Do **not** delete `.fs-title`, `.fs-ship`, `.sec-img`, `.inf-img`, `.otA`, `.doc-stack`, `.ds-*`, `.vflags*`, `.vf-*`, `.chkB*`, or `.fs-video*` — Tasks 2 and 6–11 now use all of them.

- [ ] **Step 3: Rebuild and confirm nothing visual changed**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
python3 scripts/page_hardening_scan.py african-grey-parrot-adoption-cost
```

Expected: build clean, `0 ERROR · 0 WARN`.

- [ ] **Step 4: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "chore(adoption-cost): delete CSS for components this page does not render

Leaves only rules with live markup behind them, so the next reader cannot
mistake a styled-but-absent component for a shipped one."
```

---

## Task 14: Runtime probes at 375 / 768 / 1280 — the half the static scan cannot do

The breeder's ask "all font/text, headers, body texts must fit well on desktop, mobile and tablet" has **never been measured on this page**. Both halves of the hardening skill are required.

**Files:** none modified unless a probe fails.

- [ ] **Step 1: Serve the built site**

```bash
cd /Users/apple/Downloads/CAG && npx astro preview --port 4321
```

Use `run_in_background: true`. Then open `http://localhost:4321/african-grey-parrot-adoption-cost/` in the preview browser.

- [ ] **Step 2: §2a — horizontal overflow, at each of 375 / 768 / 1280**

Resize, then run:

```js
(()=>{const bad=[...document.querySelectorAll('main *')]
  .filter(e=>e.getBoundingClientRect().right>innerWidth+1)
  .slice(0,8).map(e=>e.tagName+'.'+(e.className||'').toString().slice(0,34));
 return JSON.stringify({scrollW:document.documentElement.scrollWidth,vw:innerWidth,offenders:bad})})()
```

Pass: `scrollW === vw` and `offenders` empty. `overflow-x:clip` is set on `.adopt`, which **hides** this in `scrollWidth` — so the `offenders` list is the real signal, not `scrollW`. Fix with `minmax(0,1fr)` + `min-width:0` on the offending grid.

- [ ] **Step 3: §2b — full-page contrast sweep**

Run the sweep from `skills/cag-page-hardening.md §2b` verbatim. Target **0 failures**. Two known-good values that must not be "fixed": `rgba(255,255,255,.82)` on `#221f1d` (12.1:1) and `#f08070` on `#221f1d`.

- [ ] **Step 4: §2c — component sizing**

```js
(()=>{const r=e=>e&&Math.round(e.getBoundingClientRect().height),w=e=>Math.round(e.getBoundingClientRect().width);
 const dial=document.querySelector('.dial');
 return JSON.stringify({vw:innerWidth,
  hero:r(document.querySelector('.adopt-hero')),
  h1:getComputedStyle(document.querySelector('h1')).fontSize,
  dialH:dial&&r(dial), dialScrolls:dial&&dial.scrollHeight>dial.clientHeight,
  cardH:[...document.querySelectorAll('.availB-c')].map(r),
  btnW:[...document.querySelectorAll('.availB-btn')].map(w)})})()
```

Pass: hero 350–420px at 1280 · `h1` honours its clamp (if it reports the global token instead, a `clamp()` is missing spaces around `+`/`-` — hardening §1a, and fix that **first**) · `.availB-c` heights uniform within ±2px · buttons hug their labels.

- [ ] **Step 5: §2y — real-`ch` line length, at 768 and 1280**

Run the §2y probe verbatim, including its `realCh` helper and the `details.open = true` line. **Do not approximate `ch` as `0.5em`** — that over-reports ~20% for IBM Plex Sans and caused a false cluster-wide reflow last session. Filter `> 75` only. Narrow measures inside cards are fine. The most likely real finding is an FAQ answer or `.otA` cell with `max-width:none`.

- [ ] **Step 6: §2z — srcset waste on the 14 new figures**

```js
[...document.querySelectorAll('img[srcset]')].map(img=>{const r=img.getBoundingClientRect();
 return {alt:img.alt.slice(0,28),declared:img.sizes,rendered:Math.round(r.width),
  intrinsic:img.naturalWidth,waste:+(img.naturalWidth/(r.width*devicePixelRatio)).toFixed(2)}})
 .filter(x=>x.waste>1.5)
```

Pass: empty. Any hit means `sizes` under-declares the real box — correct `sizes` to the true box **first**, then the candidate ladder.

- [ ] **Step 7: Verify the jump-rail and dial actually land anchors correctly**

At 375px, tap three rail chips; at 1280px, click three dial rows. Each target H2 must come to rest **below** the sticky chrome, not under it. The page sets `scroll-margin-top:calc(var(--hdr) + 51px)` on mobile — confirm by measurement, not by reading the CSS.

- [ ] **Step 8: Screenshot proof at all three widths**

Capture `375`, `768`, `1280` screenshots of the FAQ, the contact form, and the True-Cost Ledger table specifically — those are the three the breeder named. Share them.

- [ ] **Step 9: Commit any fixes the probes forced**

```bash
git add -u && git commit -m "fix(adoption-cost): runtime probe findings at 375/768/1280"
```

---

## Task 15: The gate sequence

**Files:** none modified unless a gate reports a real defect.

- [ ] **Step 1: Static scan to zero**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/page_hardening_scan.py african-grey-parrot-adoption-cost
```

Expected: `0 ERROR · 0 WARN`.

- [ ] **Step 2: Dup-gate, body and headers, against the whole for-sale cluster**

```bash
python3 scripts/dup_content_audit.py african-grey-parrot-adoption-cost congo-african-grey-for-sale timneh-african-grey-for-sale hand-raised-african-grey-parrot-for-sale dna-tested-african-grey-for-sale african-greys-for-sale-with-health-guarantee african-grey-parrot-bird-eggs-for-sale-usa baby-african-grey-parrot-for-sale
python3 scripts/dup_content_audit.py --headers african-grey-parrot-adoption-cost congo-african-grey-for-sale timneh-african-grey-for-sale hand-raised-african-grey-parrot-for-sale dna-tested-african-grey-for-sale african-greys-for-sale-with-health-guarantee african-grey-parrot-bird-eggs-for-sale-usa baby-african-grey-parrot-for-sale
```

Expected: zero non-whitelist crossovers. The new `.chkB` checklist and `.doc-stack` are the likeliest collisions (hand-raised has a due-diligence checklist; several siblings list documents). **Verify each reported run before rewriting** — reviews, the counter strip, doc-badge lists and the shipping line are whitelisted furniture, and 23 of last session's 23 reported crossovers were exactly that.

- [ ] **Step 3: Anchor Diversity Ledger — script it, do not eyeball it**

```bash
python3 - <<'PY'
import re,html
spent={  # from the lessons doc tables + the adoption-cost table
 '/african-grey-parrot-bird-eggs-for-sale-usa/':{'african grey egg page','fertile african grey eggs','eggs priced by sex','hatching a grey yourself','congo eggs in an incubator','incubating your own clutch'},
 '/african-grey-breeding-pair-for-sale/':{'proven breeding pair','proven-producer pair','see the pair','adult breeding pairs','a lab-sexed adult pair','aviary-raised adult pairs','the breeding pair we currently hold','adults kept back for breeding','breeding stock carries its own price logic'},
 '/congo-african-grey-parrot-pair-for-sale/':{'congo african grey pair page','our congo pair listing','the congo pair listed separately','two congos sold together','a documented congo pair','the larger congo equivalent'},
}
h=open('dist/african-grey-parrot-adoption-cost/index.html').read()
m=h[h.find('<main'):h.find('</main>')]
hits=0
for a in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',m,re.S):
    tgt,txt=a.group(1),html.unescape(re.sub(r'<[^>]+>','',a.group(2))).strip().lower()
    if tgt in spent and txt in spent[tgt]:
        print('COLLISION:',tgt,'->',repr(txt)); hits+=1
print('collisions:',hits)
PY
```

Expected: `collisions: 0`. Two collisions were caught this way on the first draft — eyeballing shipped them.

- [ ] **Step 4: Seam parity**

```bash
echo "seams=$(grep -c 'class=\"seam\"' src/pages/african-grey-parrot-adoption-cost/index.astro) sections=$(grep -c '<section' src/pages/african-grey-parrot-adoption-cost/index.astro)"
```

Expected: seams within one of sections (house idiom is one seam before every section; the budget ceiling is 8–10 for a 10-section page — do not chase 17).

- [ ] **Step 5: Final page audit**

```bash
python3 scripts/final_page_audit.py --for-sale
```

Expected: PASS or PASS-WITH-WARNINGS for this slug. If the slug is skipped entirely, append it to the hardcoded `FORSALE` roster — trap #17.

- [ ] **Step 6: Health sweep and sitemaps**

```bash
bash scripts/health-sweep.sh --no-build
python3 scripts/generate_sitemaps.py
```

Expected: sweep PASS; sitemaps regenerate with zero phantom URLs.

- [ ] **Step 7: Commit**

```bash
git add -u && git commit -m "chore(adoption-cost): gate sweep - hardening, dup, anchors, audit, sitemaps"
```

---

## Task 16: Ship and verify live

- [ ] **Step 1: Confirm you are on `main`**

```bash
cd /Users/apple/Downloads/CAG && git branch --show-current
```

Expected: `main`. Only `main` auto-deploys — work on any other branch strands at HTTP 404 while looking done.

- [ ] **Step 2: Push (push = deploy)**

```bash
git push origin main
```

- [ ] **Step 3: Wait for the deploy, then verify the live page**

```bash
sleep 90
curl -s -o /dev/null -w "%{http_code}\n" https://congoafricangreys.com/african-grey-parrot-adoption-cost/
curl -s https://congoafricangreys.com/african-grey-parrot-adoption-cost/ | grep -o '<img class="sec-img' | wc -l
```

Expected: `200`, then `14`.

- [ ] **Step 4: Check the live-only analytics double-load (cannot be seen in `dist/`)**

```bash
curl -s https://congoafricangreys.com/african-grey-parrot-adoption-cost/ | grep -cE 'googletagmanager\.com|src="/[0-9a-f]{4,}/"'
```

Two hits = GA4 double-load via Cloudflare's first-party gateway. Report it to the breeder as a dashboard item; it is not fixable in code.

---

## Task 17: Bank the lessons

**Files:**
- Create: `docs/superpowers/sessions/2026-07-28-adoption-cost-harden-lessons.md`
- Modify: `sessions/2026-07-19-for-sale-component-map.md`, memory store

- [ ] **Step 1: Write the lessons doc**

Must carry, for pages 9–22: the **markup↔CSS drift** failure mode and the audit script from Task 13 Step 1 that detects it in one command; that `page_hardening_scan.py` returned **0 ERROR** on a page whose FAQ was structurally broken, so a clean static scan is not evidence of a shipped-correct page; the rule that **a styled-but-unrendered component is a missing component, not dead CSS**, when the spec mandates it; and that processed assets committed in one session can be orphaned by the next — check `public/` against markup before assuming images are absent.

- [ ] **Step 2: Update the binding tuple ledger**

Record in `sessions/2026-07-19-for-sale-component-map.md` that adoption-cost now renders `.doc-stack` + `.otA` ×2 + `.vflags` + `.chkB` + `.fs-video`, so siblings can rotate different components and the uniqueness ledger stays true.

- [ ] **Step 3: Save the two durable memories**

Add `reference_markup_css_drift` (the drift audit as a pre-flight check on every ported page) and update `project_adoption_cost_pack_ready` to reflect that the 8 infographics and 6 OG photos are now placed. Add the one-line pointers to `MEMORY.md`.

- [ ] **Step 4: Commit and push**

```bash
cd /Users/apple/Downloads/CAG
git add docs/superpowers/sessions/2026-07-28-adoption-cost-harden-lessons.md sessions/2026-07-19-for-sale-component-map.md
git commit -m "docs(adoption-cost): bank the markup-CSS drift failure mode for pages 9-22"
git push origin main
```

---

## Self-Review

**Spec coverage** — every complaint in the brief maps to a task: FAQ broken → 1 · contact form → 2 · ledger title too thick on mobile → 3 · components rough/unpolished → 4, 7–11, 13 · missing opening paragraphs → 12 · text fit across mobile/tablet/desktop → 14 · 8 infographics now in the folder → 5, 6 · hardening check → 4, 14, 15 · lessons-doc playbook (§7 commands, §5 seam parity, §6 anchor ledger, §1 verify-the-gate, §3 ≥5 runs) → 15, and §1 is applied inside every task's Step 1.

**Gaps accepted and stated:** perf/CLS sampling (lessons §3) is **not** in this plan — this page has no reported CLS defect, and the dna-tested bimodal CLS is a separate backlog item. Self-hosted fonts (lessons §9.1) stay deferred to the full-site pass.

**Placeholder scan:** clean. Two steps are deliberately conditional rather than prescriptive — Task 4 Step 2 (false positive vs real defect) and Task 13 Step 2 (`.geo-*`) — because both require reading the markup first, and prescribing an edit sight-unseen is what the verify-the-gate rule forbids.

**Type consistency:** `figs` / `fig()` / `f.kind` / `f.pos` / `f.srcset` are defined in Task 6 Steps 2–3 and used consistently in Step 4. `.form-2up` and `.fld` are defined in Task 2 Step 2 and used in Step 3. `.ds-title`, `.chkB-title` and `.vflags-title` are all `<p>`, never headings, in every task that renders them.

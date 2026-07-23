# Hand-Raised For-Sale Page — Final Hardening Plan (2026-07-23)

> **For agentic workers:** execute task-by-task on `main`. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Take `/hand-raised-african-grey-parrot-for-sale/` from "live but rushed" to impeccable — fix the broken mobile hero, the covered mobile jump-rail, the cropped mobile infographics, the oversized dial/hero/buttons, the AA-contrast and link-distinguishability failures, and the 163 KiB image-delivery flag — then bank every fix pattern as a reusable skill.

**Architecture:** Single page-scoped file `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro` (928 lines, `.handraised` scope). All CSS is in its `<style is:global>` block (lines 682–928). Fixes are CSS + small markup edits + a Python image pass. No new components; the shared for-sale kit bugs (mobile infographic crop, rail-under-tabbar, dial/rail contrast) get fixed here first, then written into a skill so the remaining 18 cluster pages inherit the fix.

**Tech Stack:** Astro 5, page-scoped CSS, vanilla JS IntersectionObserver, Pillow (WebP), `scripts/final_page_audit.py`, `scripts/dup_content_audit.py`.

---

## Root-cause diagnosis (verified against source + screenshots)

| # | Symptom (breeder report) | Root cause (file:line) | Fix class |
|---|---|---|---|
| 1 | Mobile hero images broken/stacked wrong | `.pofig{position:absolute;width:44%}` never unwound below 980px; `.hero-scatter{height:300px}` (L714–722, L926) collapses the absolute children | Layout rewrite |
| 2 | Desktop hero too tall (>400px) | `.hero-grid{min-height:360px}` + `.hero-scatter{height:420px}` + `padding:8px 0 34px` (L704–705, L714) | Sizing |
| 3 | 3 of 4 hero birds' heads cropped | `.pofig img{aspect-ratio:62/72;object-fit:cover}` with default center `object-position` (L716) | Per-image focal point |
| 4 | Trust chips wrap 3+1 | `.hero-chips{display:flex;flex-wrap:wrap}` (L711) | 2×2 grid |
| 5 | Mobile jump-rail "not working" | `.railB{position:sticky;bottom:0;z-index:40}` (L909) sits **under** `MobileTabBar` (`fixed bottom-0 z-50`, MobileTabBar.astro:34) | Offset + z-index |
| 6 | Mobile infographics zoomed, text cut off | `.sec-img.inf-img` forced to `aspect-ratio:5/4` + `object-fit:cover` on mobile (L925) — crops ~30% off each side of a 16:9 infographic | Split OG vs infographic rules |
| 7 | Card buttons too wide / labels wrap 2 lines | `.bfull{width:100%}` + long label `Inquire about {name} →` (L795, L306) | Compact button |
| 8 | Card badge covers bird's head | `.bbadge{top:8px;left:8px}` over a 1:1 `object-fit:cover` portrait (L785) | Reposition + gradient scrim |
| 9 | Card name/price misaligned | `.brow` flex, `JINS & JENI (PAIR)` wraps and shoves the price (L789–791) | Grid row + nowrap price |
| 10 | Desktop dial too tall | 18-item list at `.74rem/1.25` + `padding:5px 7px` (L743) | Density pass |
| 11 | `.k2-from` / `.k2-tag` contrast FAIL | `opacity:.9` white on `--clay-ink` (L801) | Remove opacity |
| 12 | "Links rely on color" FAIL | `.handraised a{color:var(--clay-t)}` no underline (L693) | Underline in-body links |
| 13 | Footer seam divider weak | bare `<img class="seam">` 182×60, no section framing (L214, L732) | Seam redesign |
| 14 | 163 KiB image-delivery flag | 5 hero polaroids served at 620×720, displayed 175–228px, no srcset (L199) | 320w siblings |
| 15 | 3 defective infographics | flagged in QA 2026-07-22, replacements supplied 2026-07-23 | Drop-in swap |
| 16 | Invalid CSS hex | `#f6 e7dd` / `#f2 e4d6` (L704, space inside hex) | Delete dead declaration |

**Out of scope (cannot fix in code):** Rocket Loader `/70de/` unused-JS + missing source map is a Cloudflare dashboard toggle (Speed → Optimization → Rocket Loader = Off). Report, don't attempt.

---

## Task 1: Swap the 3 replacement infographics

**Files:**
- Source: `assets/1WORKING-ON/FOR-SALE-PAGES/HAND-RAISED-GREYS/{verify-hand-raised-breeder-60-seconds.png, what-comes-home-hand-raised-grey.webp, hand-raised-grey-health-pcr-screening.webp}`
- Write: `public/images/hand-raised-page/<same-stem>.webp` + `-760.webp`

- [ ] **Step 1: Verify the replacements are actually corrected** — Read each image. Confirm: "BREEDER" spelled correctly (was "BREDDER"); "WHAT COMES HOME WITH YOUR GREY" has no duplicated "HOME" and no stray card stack; "Avian Polyomavirus PCR" is legible. ✅ verified 2026-07-23.
- [ ] **Step 2: Bake to the uniform box** — `PIL.ImageOps.fit(src,(1408,768),LANCZOS,centering=(0.5,0.5))` → WebP `method=6`, quality-walk from 82 down until `<95 KB`; then a `-760.webp` sibling at 760×415.
- [ ] **Step 3: Verify** `ls -la public/images/hand-raised-page/ | grep -E 'verify|comes-home|pcr'` — all six files present, each `<95 KB`.
- [ ] **Step 4: Commit** `git add public/images/hand-raised-page && git commit -m "fix(images): swap 3 corrected hand-raised infographics"`

## Task 2: Hero — mobile rebuild + desktop tightening + face-safe framing

**Files:** Modify `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro:57-63` (polaroid array), `:189-203` (markup), `:704-722` (CSS), `:892-893,926` (responsive)

- [ ] **Step 1: Add per-polaroid focal points.** Extend `heroPolaroids` with `pos` and use it inline. Bery (`p4`) is already framed well — leave at `center 45%`. Mark/Amie/baby/young-Timneh get face-biased values (`center 30%` / `center 25%`).
- [ ] **Step 2: Desktop height.** `.hero{padding:6px 0 26px}` · `.hero-grid{min-height:0}` · `.hero-scatter{height:352px}` · `h1{font-size:clamp(1.6rem,1.15rem+1.9vw,2.28rem)}`. Target rendered hero block 360–400px.
- [ ] **Step 3: Chips to a 2×2 grid** — `.hero-chips{display:grid;grid-template-columns:1fr 1fr;gap:.4rem 1.2rem}`, one line each, `white-space:nowrap` where it fits.
- [ ] **Step 4: Mobile — kill absolute positioning entirely below 980px.** Replace with a real grid so nothing can collapse:
  ```css
  @media (max-width:980px){
    .handraised .hero-scatter{height:auto;max-width:none;display:grid;
      grid-template-columns:1fr 1fr;gap:12px;margin:14px 0 0;}
    .handraised .pofig{position:static;width:auto;transform:none;
      padding:6px 6px 24px;border-radius:8px;}
    .handraised .pofig figcaption{font-size:.68rem;bottom:6px;}
    .handraised .pofig.p5{display:none;}   /* 4 polaroids = clean 2×2 */
    .handraised .pofig img{aspect-ratio:1/1;}
  }
  ```
  Keep a gentle alternating tilt (`p1,p4: rotate(-2deg)` / `p2,p3: rotate(2deg)`) so it still reads as a scatter, not a grid of squares.
- [ ] **Step 5: Delete the invalid gradient** (`#f6 e7dd`) — keep only the valid second declaration.
- [ ] **Step 6: Verify** at 375px, 768px, 1280px in the preview browser: all four birds' faces visible, no overlap, hero height 360–400px desktop.
- [ ] **Step 7: Commit.**

## Task 3: Hero image delivery (−163 KiB)

- [ ] **Step 1:** Generate `-320.webp` (320×320, face-safe crop) siblings for all 5 hero polaroids.
- [ ] **Step 2:** Add `srcset`/`sizes` to the polaroid `<img>`: `sizes="(max-width:980px) 44vw, 240px"`.
- [ ] **Step 3:** Keep `p1` eager + `fetchpriority=high`; the rest lazy.
- [ ] **Step 4: Verify** `ls -la public/images/hand-raised-page/hero-*-320.webp` — 5 files, each <14 KB.
- [ ] **Step 5: Commit.**

## Task 4: Mobile jump-rail — un-bury it

**Files:** `index.astro:909-915`

- [ ] **Step 1:** Lift above `MobileTabBar`: `bottom:calc(56px + env(safe-area-inset-bottom));z-index:45;`
- [ ] **Step 2:** Round the top corners + shadow so it reads as a distinct floating ticker, not a second tab bar: `border-radius:12px 12px 0 0;box-shadow:0 -4px 14px rgba(0,0,0,.18);margin:0 8px;`
- [ ] **Step 3:** Confirm AA: `.railB .p` = `#c9f2db` on `#234f3b` (5.2:1 ✓), `.l` = `#d7e7de`, **no `opacity`** anywhere in the rail.
- [ ] **Step 4:** Auto-scroll the active chip into view in the scroll-spy (`a.on` → `scrollIntoView({inline:'center',block:'nearest',behavior:'auto'})`) so the rail tracks the reader.
- [ ] **Step 5: Verify** at 375px: rail visible above the tab bar, tapping `03` lands on `#howraise` with the heading clear of the header.
- [ ] **Step 6: Commit.**

## Task 5: Mobile infographics — stop the crop

**Files:** `index.astro:751, 925`

- [ ] **Step 1:** Desktop `.sec-img.inf-img` unchanged (760px 16:9 box — the locked uniform rule).
- [ ] **Step 2:** Mobile — infographics keep their native ratio and are never cover-cropped:
  ```css
  .handraised .sec-img.inf-img{width:100vw;max-width:100vw;margin-left:calc(50% - 50vw);
    border-radius:0;border-left:0;border-right:0;aspect-ratio:1408/768;object-fit:contain;background:#fff;}
  .handraised .sec-img.og-photo{aspect-ratio:5/4;object-fit:cover;}
  ```
  `object-fit:contain` guarantees every baked-in word survives; the 5:4 taller mobile frame stays for OG **photos** only, per `IMAGE-DESIGNS.md §7`.
- [ ] **Step 3: Verify** at 375px: read the full title on `what-hand-raised-means` — no text clipped at either edge.
- [ ] **Step 4: Commit.**

## Task 6: Bird cards — compact buttons, aligned type, uncovered faces

**Files:** `index.astro:301-307, 783-796, 920-921`

- [ ] **Step 1: Compact button.** Label → `Reserve {firstName} →` (short, never wraps). CSS: `.bfull{width:auto;align-self:stretch;justify-content:center;white-space:nowrap;font-size:.82rem;padding:.5rem .9rem;margin-top:auto;}`
- [ ] **Step 2: Badge off the face.** Move to bottom-left over a scrim: `.bbadge{top:auto;bottom:8px;left:8px;background:rgba(255,255,255,.92);backdrop-filter:blur(2px);}` plus `.bphoto::after` bottom gradient scrim so the chip stays legible on any photo.
- [ ] **Step 3: Name/price row.** `.brow{display:grid;grid-template-columns:1fr auto;gap:.5rem;align-items:baseline;min-height:2.4rem}` · `.brow h3{font-size:1.02rem;line-height:1.15;min-width:0}` · `.bprice{white-space:nowrap}`.
- [ ] **Step 4: Equal card rhythm.** `.binfo{gap:.45rem}` and chips row `min-height:1.5rem` so every card's button sits on the same baseline.
- [ ] **Step 5: Verify** at 375px and 1280px: no 2-line buttons, no badge on a head, price never wraps under the name.
- [ ] **Step 6: Commit.**

## Task 7: Desktop dial TOC — density + verified contrast

**Files:** `index.astro:735-748`

- [ ] **Step 1:** Tighten the 18-item list: `a{padding:4px 6px;font-size:.7rem;line-height:1.2}` · `.di{font-size:.62rem}` · `.dt{display:none}` on the inactive items (tag chip only on `.on`) — this is what makes it long.
- [ ] **Step 2:** Ring stays at the locked compact 64px; card `padding:12px 10px`.
- [ ] **Step 3: Contrast note (do NOT blind-apply the light-card fix).** This page's dial is the **dark-aviary** variant. `#6b625a` is the fix for the *light* dial card on cream (congo/timneh). On `#234f3b`, `.di` must stay light: `#9fc7b0` = **5.00:1** ✓ AA. Record both variants in the skill so the wrong one is never applied.
- [ ] **Step 4: Verify** dial fits without inner scroll at 900px viewport height.
- [ ] **Step 5: Commit.**

## Task 8: Contrast + link distinguishability (Lighthouse a11y)

**Files:** `index.astro:693, 801`

- [ ] **Step 1:** `.k2-tag .k2-from{opacity:1;color:#ffe9e3}` — kills the "From / $1,500" contrast failure (white at `.9` alpha on `#c8472f` drops below 4.5:1).
- [ ] **Step 2:** In-body links get a non-color affordance: `.handraised .content p a{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px;}` and `:hover{text-decoration-thickness:2px}`. Clears the three flagged elements (scam guide, congo-vs-timneh, Texas page).
- [ ] **Step 3: Verify** with a Lighthouse a11y run — 0 contrast failures, 0 link-distinguishability failures.
- [ ] **Step 4: Commit.**

## Task 9: Seam divider + section differentiators

**Files:** `index.astro:214, 316, 732` + each `<img class="seam">` site of use

- [ ] **Step 1:** Wrap the seam in a framed divider — two hairline clay-tint rules flanking a **smaller** wordmark (`height:34px`, `width:auto`), centered, with `margin:34px auto 30px`, so it reads as a deliberate section break rather than a floating logo.
- [ ] **Step 2:** Give sections a quiet differentiator: `.sec + .sec{border-top:1px solid transparent}` is not enough — use an `h2` clay tick (`h2::before` 3px×1.1em clay bar) plus `.sec{padding:14px 0 16px}` so each section opens visibly.
- [ ] **Step 3: Verify** visually at 375px and 1280px.
- [ ] **Step 4: Commit.**

## Task 10: Anchor-diversity + microformats + SEO passes

- [ ] **Step 1: Anchor audit.** Scan every other live page for the 17 internal anchors used here; any collision gets rewritten to a *different* keyword tier (secondary / LSI / NLP variation / long-tail query). Link-First placement preserved.
- [ ] **Step 2: Microformats (h-entry/h-product/h-review/h-card).** Answer the auditor flag: microformats2 are a legacy class-based structured-data format; Google/Bing consume the JSON-LD this page already ships, so the flag is cosmetic, **not** a ranking issue. Add a zero-visual-change class layer anyway (`h-product`/`p-name`/`p-price` on bird cards, `h-review`/`p-author` on the two reviews, `h-card` on the aviary NAP) so legacy parsers and the auditor are satisfied.
- [ ] **Step 3: Keyword + entity + voice re-verify.** Primary-keyword distribution 30–35, first-person sweep, anti-AI sweep, entity variety — the page passed on 2026-07-22; re-run after the copy touches in this session.
- [ ] **Step 4: Gates.** `python3 scripts/dup_content_audit.py` + `--headers` (zero non-whitelist crossover) → `python3 scripts/final_page_audit.py` (for-sale profile).
- [ ] **Step 5: Commit.**

## Task 11: Bank the patterns as a standalone skill

**Files:** Create `skills/cag-page-hardening.md`; register via `python3 scripts/register_skills.py --copy`

- [ ] **Step 1:** Write the skill as an auto-running audit: every fix pattern in this plan plus the ones already banked from egg/congo/timneh (dial/rail contrast, uniform image boxes, `og-tall` framing, compact dial, seam, mobile full-bleed, srcset siblings, scoped-reset traps).
- [ ] **Step 2:** Each pattern = **detect command → symptom → fix → verify command**, so the skill finds the issue rather than waiting to be told.
- [ ] **Step 3:** Register + commit `.claude/skills/`.

## Task 12: Deploy + verify

- [ ] **Step 1:** `npx astro build` — 0 errors.
- [ ] **Step 2:** `git push origin main` (= deploy).
- [ ] **Step 3:** Verify live 200 + spot-check mobile hero, rail, infographic at 375px.
- [ ] **Step 4:** Report the Cloudflare Rocket Loader toggle to the breeder (dashboard-only fix).

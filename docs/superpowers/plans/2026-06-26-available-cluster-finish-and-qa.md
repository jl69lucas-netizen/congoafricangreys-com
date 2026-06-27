# Available Cluster — Finish Unfinished Batch + 29-Point QA Gate

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Finish the unfinished half of the 2026-06-23 `/available/` batch (responsive nav on all 6 bird pages, first-person + anti-AI de-templating, nav wiring, image perf, Rocket-Loader note) and then run the breeder's full 29-point SEO/GEO/AEO/a11y/perf QA gate against the hub + 6 bird pages, fixing only real gaps.

**Architecture:** Static Astro site, Direction-D theme (`body.theme-d`). All page edits go to `src/pages/available/<slug>/index.astro` (deployed; `site/content/` is staging only). The jump-bar reuses the existing `src/components/cag-jump-nav.astro` component already wired into amie + roys. Verification = `npx astro build` + `python3 scripts/final_page_audit.py --birds` + dist greps + preview-verify + warm Lighthouse median-of-3. Work directly on `main`; commit + push after each task (push = deploy → GitHub Actions → Cloudflare Pages).

**Tech Stack:** Astro, Tailwind utility classes, Direction-D CSS, Pillow (image resize), Cloudflare Pages.

**Ground truth established 2026-06-26 (what is already LIVE vs. not — do NOT redo the LIVE items):**
- ✅ LIVE: Jins & Jeni reframe, hub breeding/eggs section, hub pricing-image de-dupe, bird-page H2 type-scale strip, hub hero/TOC/mobile jump-bar.
- ⚠️ UNCOMMITTED in working tree: jump-bar already correctly applied to `amie` + `roys` (anchors verified — all 9 exist). These edits must be committed, not rewritten.
- ❌ NOT DONE: jump-bar on `elad`/`evie`/`jins-jeni`/`bery`; first-person + anti-AI de-templating (all 6 pages still share a byte-identical "year one" paragraph + identical "Breeder note:" label); `/available/` nav wiring (0 refs in Header/Footer/homepage); image downscale; Rocket-Loader note; final audit + Lighthouse.

**Confirmed facts (do not re-derive):**
- All 6 bird pages share these 9 section ids: `#temperament #talking #price-counter #documentation #health #gallery #shipping #faq #reserve`. The jump-link set is therefore identical across pages.
- `src/components/cag-jump-nav.astro` exists and takes `links` (array of `{label, href}`) + `sticky` (bool) props.
- Each bird page scopes its custom CSS under a page class: roys=`.roys-d`, amie=`.amie-d`, elad=`.elad-d`, evie=`.evie-d`, jins-jeni=`.jins-jeni-d` (or `.jinsjeni-d`), bery=`.bery-d`. The `.jump-mobile` rule is NOT scoped (standalone) so it is portable verbatim.

**Pre-flight (run once):**
```bash
cd /Users/apple/Downloads/CAG && git checkout main && git status --short
```

---

## Task 1: Commit the existing amie+roys jump-bar, then apply it to the 4 remaining bird pages

**Files:**
- Already-modified (commit as-is): `src/pages/available/amie/index.astro`, `src/pages/available/roys/index.astro`
- Modify: `src/pages/available/elad/index.astro`, `evie/index.astro`, `jins-jeni/index.astro`, `bery/index.astro`

The proven pattern (verbatim from the amie diff) has 5 edits per page. The 9-link `jumpLinks` array is identical on every page.

- [ ] **Step 1: Confirm amie + roys build clean as-is, then commit them**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
git add src/pages/available/amie/index.astro src/pages/available/roys/index.astro
git commit -m "feat(birds): commit responsive jump-bar on amie + roys (desktop TOC hidden on mobile)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

- [ ] **Step 2: For each of elad, evie, jins-jeni, bery — add the JumpNav import**

After the existing `import JumpRail ...` line, add:
```astro
import JumpNav from '../../../components/cag-jump-nav.astro';
```

- [ ] **Step 3: Add the `jumpLinks` const in the frontmatter (just before the closing `---`)**

```astro
const jumpLinks = [
  { label: "Temperament", href: "#temperament" },
  { label: "Talking", href: "#talking" },
  { label: "Price", href: "#price-counter" },
  { label: "What's included", href: "#documentation" },
  { label: "Health", href: "#health" },
  { label: "Gallery", href: "#gallery" },
  { label: "Shipping", href: "#shipping" },
  { label: "FAQ", href: "#faq" },
  { label: "Reserve", href: "#reserve" },
];
```

- [ ] **Step 4: Add the `.jump-mobile` CSS rule inside the page's `<style>` block**

```css
    /* Mobile sticky jump bar */
    .jump-mobile { position: sticky; top: 94px; z-index: 40; background: #faf7f4; }
    @media (min-width: 768px) { .jump-mobile { display: none; } }
```

- [ ] **Step 5: Insert the mobile jump bar immediately BEFORE the existing "TABLE OF CONTENTS" `<nav>`, and make that nav desktop-only**

Insert before the TOC `<nav ...>`:
```astro
  {/* ── MOBILE JUMP BAR (sticky, mobile only) ── */}
  <div class="jump-mobile px-4 py-2">
    <JumpNav links={jumpLinks} sticky={false} />
  </div>

```
Then change the TOC nav opening tag from `<nav class="py-10 ...` to add `hidden md:block`:
```astro
  <nav class="hidden md:block py-10 px-4 bg-warm-white md:py-12" aria-label="On this page">
```
(Match the exact existing class string on each page; only prepend `hidden md:block`.)

- [ ] **Step 6: Verify all 6 pages now have the jump-bar and anchors resolve**

```bash
cd /Users/apple/Downloads/CAG
for f in roys amie elad evie jins-jeni bery; do echo "$f: jump-mobile=$(grep -c 'jump-mobile' src/pages/available/$f/index.astro) JumpNav=$(grep -c '<JumpNav' src/pages/available/$f/index.astro)"; done
```
Expected: each page `jump-mobile=2` (CSS rule + div) `JumpNav=1`.

- [ ] **Step 7: Build + commit + push**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
git add src/pages/available/{elad,evie,jins-jeni,bery}/index.astro
git commit -m "feat(birds): responsive nav (desktop TOC + mobile jump-bar) on elad, evie, jins-jeni, bery

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

- [ ] **Step 8: Preview-verify the jump-bar at 375px on two pages**

Start preview, load `/available/elad` and `/available/jins-jeni` at 375px. Confirm: the desktop 22-item TOC is hidden, the sticky 9-link bar shows, tapping a link scrolls to the right section. Capture one 375px screenshot as proof. (Per memory: `preview_screenshot` resets scroll — resize to 375 first, then screenshot.)

---

## Task 2: First-person + anti-AI de-templating pass (the repeated-template fix)

**Why:** All 6 bird pages were cp+sed ported, so they share a byte-identical paragraph and the identical "Breeder note:" H6 label — the detectable mass-AI-template fingerprint the breeder flagged. This pass individuates them.

**Sub-skills to invoke FIRST (read before editing):** `skills/anti-ai-writing.md` (blacklist + human alternatives) and the First-Person Brand Voice rule (we/us/our/"here at C.A.Gs"). Honor `feedback_noncommodity_audit_then_rewrite`: classify each section STRONG/SHARPEN/REBUILD and rewrite ONLY the weak — do not regress already-strong indexed copy. Ledger-only: anything unconfirmable becomes a GAP-FLAG for Mark & Teri, never an invented claim.

**Files:** `src/pages/available/{roys,amie,elad,evie,jins-jeni,bery}/index.astro`

- [ ] **Step 1: Locate every cross-page-identical block**

```bash
cd /Users/apple/Downloads/CAG
echo "shared 'year one' frame (expect 6):"; grep -l "A lot of bird listings describe what an African Grey is like in year one" src/pages/available/*/index.astro | wc -l
echo "shared 'Breeder note' label per page:"; for f in roys amie elad evie jins-jeni bery; do echo "$f: $(grep -c 'Breeder note' src/pages/available/$f/index.astro)"; done
```

- [ ] **Step 2: Rewrite the shared "year one" paragraph uniquely per bird**

On each of the 6 pages, replace the identical paragraph with a bird-specific, first-person, concrete rewrite. Each must (a) open differently, (b) use the bird's real age/sex/variant (Congo vs Timneh; per `project_bird_page_port_pattern` age copy must be real, not a token swap), (c) avoid anti-AI blacklist phrasing, (d) stay inside the Verified-Claim Ledger. Example for one bird (do NOT reuse this verbatim across pages — write a distinct one each):
```
> Here at C.A.Gs we won't pretend a four-month-old Congo arrives doing party tricks. What Roys actually does right now is lean into a shoulder, work a foot-toy for twenty minutes, and watch the room — the talking builds over his first year as trust does.
```

- [ ] **Step 3: Rotate the H6 "Breeder note:" label so no two pages share the same sequence**

Replace the single "Breeder note:" label per page with a varied first-person label — rotate across: `From our aviary:`, `What we've seen with him/her:`, `One honest caveat:`, `Teri's note:`, `Straight from us:`, `What to expect:`. One distinct label per page.

- [ ] **Step 4: First-person sweep on any third-person brand copy**

Convert outside-voice brand sentences ("Both make exceptional companions", "African Greys are…" when it's about *our* bird) to we/us/our. Leave encyclopedic/taxonomy/cited facts neutral.

- [ ] **Step 5: Verify de-duplication**

```bash
cd /Users/apple/Downloads/CAG
echo "byte-identical 'year one' frame remaining (expect 0):"; grep -l "A lot of bird listings describe what an African Grey is like in year one" src/pages/available/*/index.astro | wc -l
echo "distinct H6 labels:"; for f in roys amie elad evie jins-jeni bery; do grep -o "From our aviary:\|What we've seen\|One honest caveat:\|Teri's note:\|Straight from us:\|What to expect:\|Breeder note:" src/pages/available/$f/index.astro | head -1; done
```
Expected: 0 byte-identical frames; 6 different labels.

- [ ] **Step 6: Build + commit + push**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
git add src/pages/available/
git commit -m "content(birds): first-person + anti-AI de-templating — individuate the 6 ported bird pages

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

---

## Task 3: Wire `/available/` into site navigation + internal links

**Problem:** 0 references to `/available/` in Header.astro, Footer.astro, or the homepage — the hub is orphaned from navigation.

**Files:** `src/components/Header.astro`, `src/components/Footer.astro`, `src/pages/index.astro`, `src/pages/congo-african-grey-for-sale/index.astro`, `src/pages/timneh-african-grey-for-sale/index.astro`

- [ ] **Step 1: Inspect the Header nav array structure first**

```bash
cd /Users/apple/Downloads/CAG && grep -n "label:\|children:\|href:" src/components/Header.astro | head -30
```

- [ ] **Step 2: Add "Available Birds Now" as the FIRST child of the Shop/Parrots dropdown**

In the dropdown `children` array, add:
```js
      { label: 'Available Birds Now', href: '/available/' },
```
(The single `nav` array drives both desktop and mobile, so it appears in both.)

- [ ] **Step 3: Add the hub link to the Footer**

In the shop/variant column of `src/components/Footer.astro`, add a list item linking `Available Birds` → `/available/`. Match the existing footer link markup exactly.

- [ ] **Step 4: Add a mid-sentence homepage link near the available-birds section**

In `src/pages/index.astro`, near the `#available-birds` section/CTA, add (keep the existing `#available-birds` anchor CTA — add alongside, don't replace):
```html
<a href="/available/" class="text-clay-text font-medium underline decoration-clay/30 hover:decoration-clay">see every available African Grey for sale</a>
```

- [ ] **Step 5: Add one mid-sentence link on each variant page**

On congo + timneh variant pages, add a contextual mid-sentence link: `…the Congo and Timneh greys we have <a href="/available/">available right now</a>.`

- [ ] **Step 6: Build + verify links resolve in dist**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
echo "homepage /available/ links:"; grep -c 'href="/available/"' dist/index.html
echo "header dropdown:"; grep -c '/available/' dist/index.html
```
Expected: homepage ≥1.

- [ ] **Step 7: Commit + push + regenerate sitemaps**

```bash
cd /Users/apple/Downloads/CAG
git add src/components/Header.astro src/components/Footer.astro src/pages/index.astro src/pages/congo-african-grey-for-sale/index.astro src/pages/timneh-african-grey-for-sale/index.astro
git commit -m "feat(nav): link /available/ hub from navbar, footer, homepage + variant pages

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
python3 scripts/generate_sitemaps.py
git add public/*.xml site/content/*.xml 2>/dev/null; git commit -m "chore: regenerate sitemaps after nav wiring" || true
git push origin main
```

---

## Task 4: Image-delivery perf — downscale oversized WebPs

**Problem (Lighthouse):** roster/hero images served far larger than displayed (~213 KiB waste). Downscale masters to ~2× displayed size, re-export WebP via Pillow (NOT `sips` — it writes fake WebP).

**Files (in `public/`):** confirm exact paths first — they may differ from the 06-23 plan after the Elad/Evie image work.

- [ ] **Step 1: Find the actual oversized files + their on-disk sizes**

```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
from PIL import Image; import os, glob
for p in sorted(glob.glob("public/**/*.webp", recursive=True)):
    try:
        im=Image.open(p); kb=os.path.getsize(p)/1024
        if im.width>1000 or kb>90: print(f"{im.size}  {kb:6.1f}KiB  {p}")
    except Exception as e: print("ERR", p, e)
PY
```

- [ ] **Step 2: Back up, then resize the flagged bird/hero/infographic images to 2× displayed width (q82, method=6)**

```bash
cd /Users/apple/Downloads/CAG && mkdir -p .img-backup
python3 - <<'PY'
from PIL import Image; import os, shutil
# Edit this list from Step 1 output: (path, target_max_width = 2x displayed CSS width)
jobs = [
  ("public/roys-congo-african-grey-male-4-months.webp", 700),
  ("public/bery-congo-african-grey-female-1-year.webp", 700),
]
for path, w in jobs:
    if not os.path.exists(path): print("MISSING", path); continue
    shutil.copy(path, ".img-backup/"+os.path.basename(path))
    im = Image.open(path)
    if im.width > w:
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(path, "WEBP", quality=82, method=6)
        print(f"resized {path} -> {w}x{h}  {os.path.getsize(path)/1024:.1f}KiB")
    else:
        print(f"skip {path} (already {im.width}px)")
PY
```

- [ ] **Step 3: Confirm every resized file is <100 KiB and dimensions are correct, then build + commit**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
git add public/
git commit -m "perf(images): downscale oversized WebPs to 2x displayed size

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
rm -rf .img-backup
```

---

## Task 5: Document the Rocket-Loader perf dependency (breeder action, not a code fix)

**Diagnosis (per memory `aa_contrast_and_perf_fixes`):** the ~71 KiB unused JS at `/70de/` + forced reflow = Cloudflare Rocket Loader, injected at the edge — NOT fixable in the repo. It is a dashboard toggle.

- [ ] **Step 1: Append the note to the live session brief Open Flags + flag to breeder**

Add to `sessions/2026-06-22-session-brief.md` Open Flags:
```
- **Perf (BREEDER ACTION):** 71 KiB unused JS + forced reflow on bird pages = Cloudflare Rocket Loader (/70de/). Fix = Cloudflare dashboard → congoafricangreys.com zone → Speed → Optimization → Rocket Loader → Off. Not a repo change (CF API tokens dead).
```

- [ ] **Step 2: Commit**

```bash
cd /Users/apple/Downloads/CAG && git add sessions/2026-06-22-session-brief.md
git commit -m "docs: note Rocket Loader as source of unused-JS/forced-reflow perf flags

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

---

## Task 6: 29-Point QA Gate — verify hub + 6 bird pages, fix only real gaps

**Method:** These pages are already built; this is a VERIFICATION sweep against the breeder's 29-point checklist, not a rebuild. Run the mechanical auditor first, then manually verify the subjective items, then fix only what actually fails. Do NOT rewrite passing/indexed copy.

- [ ] **Step 1: Mechanical auditor on the bird cluster + hub**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
python3 scripts/final_page_audit.py --birds 2>&1 | tail -60
```
Expected gates: all six heading levels present + sequential (no skips), ≥5 H5 + ≥5 H6, single Product/Offer per bird (sold≠InStock), shipping line present (`Ships nationwide · $185 airport · $350 home`), 700–1,000 words. Triage every FAIL before deploy.

- [ ] **Step 2: Verify schema + headings in `dist/` (rendered, NOT source greps)**

```bash
cd /Users/apple/Downloads/CAG
for f in available available/roys available/amie available/elad available/evie available/jins-jeni available/bery; do echo "== $f =="; grep -o '"@type":"[A-Za-z]*"' dist/$f/index.html | sort | uniq -c; done
```
Expected: hub = CollectionPage/ItemList + Product/Offer + FAQPage; each bird = single Product/Offer (+ BreadcrumbList). Person/Organization/LocalBusiness inherited from BaseLayout — confirm present once in dist.

- [ ] **Step 3: Subjective + per-item checklist (the breeder's 29 points) — mark PASS or FIX per page**

Walk the gate items; for each, record PASS or the exact fix needed. Scale counts down for these focused bird pages but keep every structural + technical item:
  - **Meta:** 4-part title (≤275) + benefit-driven description (≤155) ending in brand + LSI. (Bird titles already long-form — verify ≤ limits, don't bloat.)
  - **Front-load / BLUF:** a declarative ≤320-char answer in the first ~30% / first 50 words of each section.
  - **First-person voice** throughout (covered by Task 2 — confirm no third-person brand copy remains).
  - **Two-keyword conversational H2s** (What/How/Is/Can/Who) + unique-per-page headers (`feedback_hybrid_header_seo`).
  - **Internal/external links:** beginning/middle of sentence (never end); internal same-tab, external new-tab + `rel="noopener noreferrer"` + ↗; verify 200 before adding; cluster targets present (`/african-grey-parrot-price/`, scams, care-guide, contact).
  - **CITES Appendix I + captive-bred + USDA AWA in first 300 words; 40–60 yr lifespan referenced once.**
  - **Images:** 5-element SEO (filename/alt ≤190/title/caption+CTA/250-word description), explicit width+height + lazy (LCP hero excepted with fetchpriority).
  - **Newsletter** placements; **NO phone in body** (Rule 61); form CTA present; buyer-fear coverage (scam/sick-bird/CITES).
  - **a11y AA:** skip link, landmarks, focus states, contrast (`#b04228` small clay on light), no `<svg>` in CSS `content:`, target-size ≥24px, `<dl>` only for genuine term→def.
  - **Logistics entities (Q5):** airport codes / flight-nanny — RECOMMENDATION: keep these on the hub/shipping pages, NOT individual bird pages (a single-bird listing should stay ≤1,000 words and link out to `/buy-african-grey-parrot-near-me/` for logistics). GAP-FLAG only if the breeder wants per-bird logistics depth.
  - **Local authority (Q6):** state-specific vet/licensing — same recommendation: belongs on location pages, not bird listings; note as a hub/location-page enhancement, don't bloat bird pages.

- [ ] **Step 4: Apply only the real gaps found in Step 3, then build + commit**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
git add src/pages/available/
git commit -m "fix(available): QA-gate gaps (meta/links/a11y/image-SEO) across hub + bird pages

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>" || echo "nothing to fix"
git push origin main
```

- [ ] **Step 5: Lighthouse — warm median-of-3 on hub + one bird page**

Run Lighthouse 3× (warm cache) on `/available/` and one bird page (e.g. `/available/roys`). Report the MEDIAN of Performance / LCP / CLS / INP (single cold runs lie — `feedback_lighthouse_median`). Confirm the image-delivery savings landed; if Rocket Loader was toggled off (Task 5), the unused-JS flag should be gone.

- [ ] **Step 6: Confirm everything is pushed + record outcome**

```bash
cd /Users/apple/Downloads/CAG && git log origin/main..HEAD --oneline
```
Expected: empty (all pushed). Record the QA verdict + Lighthouse medians in `sessions/2026-06-22-session-brief.md`.

---

## Self-Review

**Spec coverage (breeder's asks → task):**
- Responsive nav on all 6 bird pages → Task 1 ✓ (amie/roys committed + 4 remaining)
- First-person + anti-AI + repeated-template fix ("did we violate mass-template?") → Task 2 ✓ (the byte-identical paragraph + label is the violation; this removes it)
- Internal/external links, front-load, AEO/BLUF, atomic content, schema, meta, image SEO, readability, a11y, newsletter, phone-in-footer, two-keyword headers, 4-Move-Loop entities, CITES/lifespan → Task 6 verification gate ✓
- Logistics entities (Q5) + local authority (Q6) → answered in Task 6 Step 3 with a Recommend+Why: keep on hub/shipping/location pages, not bird listings (word-count + intent); GAP-FLAG if breeder disagrees.
- Nav wiring → Task 3 ✓
- Image perf + Rocket Loader → Tasks 4 + 5 ✓
- Lighthouse warm median-of-3 → Task 6 Step 5 ✓ (the "DID YOU DO THIS?" Lighthouse item)

**Already-LIVE items deliberately excluded (no task):** Jins & Jeni reframe, hub breeding/eggs section, hub pricing de-dupe, bird-page H2 type-scale, hub hero/TOC/jump-bar — all verified live in git, re-doing them risks regression.

**Type/path consistency:** hub = `src/pages/available/index.astro`; birds = `src/pages/available/<slug>/index.astro`; nav = single `nav` array in `src/components/Header.astro` (drives desktop + mobile); JumpNav component = `src/components/cag-jump-nav.astro` with `links`+`sticky` props; 9 anchors verified identical across all 6 pages.

**Open decision for the breeder (Recommend+Why):** Q5 airport codes/flight-nanny + Q6 local vet/licensing — **Recommended: place on the hub + shipping + location pages, not individual bird listings** (bird pages must stay 700–1,000 words + single-intent; logistics depth dilutes the buy-this-bird intent and duplicates the `/buy-african-grey-parrot-near-me/` page). Trade-off: a buyer on a bird page has to click through for logistics detail rather than seeing it inline. Confirm before Task 6 Step 3.

---

## Execution Handoff

**Plan complete and saved to `docs/superpowers/plans/2026-06-26-available-cluster-finish-and-qa.md`. Two execution options:**

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration.

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints.

**Which approach?**

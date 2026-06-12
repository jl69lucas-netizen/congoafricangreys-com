# Interior-Page Polish Rollout (17 pages) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the scam-page polish playbook (`sessions/2026-06-12-scam-page-polish-playbook.md`) to the 17 remaining Direction-D interior pages — desktop JumpRail dial + mobile bottom-sheet nav on every ≥30K-char page, AA-verified colors, clamped heading scale, valid H1–H6 ladder, 240-char mobile paragraphs, scroll polish — at ~3 pages per session across 6 sessions.

**Architecture:** Each page gets the same 8-step per-page recipe (measure → typography → contrast → JumpRail + section-next-nav → scroll polish → paragraph splits → images → verify loop). The JumpRail component (`src/components/cag-library/JumpRail.astro`) already provides both the desktop dot rail ("dial") and the mobile bottom sheet — pages only supply a `sections`/`partNames` map. No content changes; visual + nav layer only.

**Tech Stack:** Astro 5 static pages, Direction-D theme (`src/styles/direction-d.css`, global), Playwright MCP probes, Pillow for WebP, GitHub Actions → Cloudflare Pages deploy.

---

## Page inventory + batch schedule

Threshold: every remaining content page is ≥30K chars → gets the **full recipe incl. JumpRail dial + mobile jump nav**. Only `contact-us` (4.4K) and `privacy-policy` (9K) fall under → **polish-only** (no dial/jump nav).

| Session | Pages (slug under `src/pages/<slug>/index.astro`) | Chars | Dial+JumpNav? |
|---|---|---|---|
| **1 ✅ DONE 2026-06-12** | `trusted-african-grey-parrot-breeders` (About Us) — commit `3f74861` | 43.5K | ✅ |
| | `captive-bred-african-grey-parrot` — commit `163c24c` | 48.2K | ✅ |
| | `cites-african-grey-documentation` — commit `fec2d5a` | 49.6K | ✅ |
| **2 ✅ DONE 2026-06-12** | `african-grey-reviews` — commit `e3e7aa1` (hero re-shot: Catherine buyer photo, cropped 72%/38%) | 31.9K | ✅ |
| | `african-grey-parrot-faq` — commit `e3e7aa1` (ids already existed from interior batch — "only 1 id" note was stale) | 34.6K | ✅ |
| | `african-grey-adoption` — commit `e3e7aa1` (+ long-section breakup: channel cards, green-band verify cards, 3-phase strip, 2 figures) | 48.0K | ✅ |
| **3** | `african-grey-parrot-care-guide` (pillar) | 57.8K | ✅ |
| | `african-grey-care` (hub) | 42.6K | ✅ |
| | `african-grey-parrot-diet` | 66.0K | ✅ |
| **4** | `best-african-grey-parrot-food` | 60.6K | ✅ |
| | `african-grey-parrot-lifespan` | 60.0K | ✅ |
| | `african-grey-parrot-health-guarantee` | 49.9K | ✅ |
| **5** | `african-grey-parrot-guide` (species pillar) | 54.4K | ✅ |
| | `how-to-tame-african-grey-parrot` | 51.9K | ✅ |
| | `african-grey-parrot-price` | 62.2K | ✅ |
| **6** | `contact-us` (add H2s — currently H1-only) | 4.4K | ❌ polish only |
| | `privacy-policy` (H1+H2 ladder is valid; sizing/contrast only) | 9.0K | ❌ polish only |
| | + site-wide final verify (all 18 live, sitemap, IndexNow batch) | — | — |

Session 1 grouping rationale: all three are Cluster B (trust/authority), share the same green-panel infographic style and similar length, and the user named the first two.

**Heading-ladder status (probed 2026-06-12):** all 15 content pages already carry a full H1–H6 ladder (e.g. captive-bred = 1/10/8/1/1/1). The work is *sizing/order verification in the rendered DOM*, not restructuring — except `contact-us` (H1 only → add H2s per its natural sections) and `african-grey-parrot-faq` (needs section `id`s for jump targets).

---

## The Per-Page Recipe (run verbatim for each page)

Reference implementation: `src/pages/how-to-avoid-african-grey-parrot-scams/index.astro` (commits `196536d`, `56d9989`, `79cc594`). Brand context: read `PRODUCT.md` + `DESIGN.md` first each session (non-negotiable).

### Step R1 — Measure first (never fix blind)

- [ ] Build + preview: `npx astro build && npx astro preview` (serves at `http://localhost:4321`)
- [ ] Playwright probe at **375×812**, then **1280×900**, on `http://localhost:4321/<slug>/`:

```js
// browser_evaluate — run at both viewports
() => {
  const out = { headings: {}, overflow: [], smallTaps: [], lowContrast: [] };
  document.querySelectorAll('h1,h2,h3,h4,h5,h6').forEach(h => {
    const k = h.tagName + '@' + getComputedStyle(h).fontSize;
    out.headings[k] = (out.headings[k] || 0) + 1;
  });
  out.docOverflow = document.documentElement.scrollWidth - window.innerWidth;
  document.querySelectorAll('*').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width > window.innerWidth + 1) out.overflow.push(el.tagName + '.' + el.className);
  });
  document.querySelectorAll('a,button').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.height > 0 && r.height < 24) out.smallTaps.push(el.textContent.trim().slice(0, 30));
  });
  return out;
}
```

- [ ] Record: any H2 px ≥ H1 px (inversion), heading-order skips in rendered DOM, overflow elements, sub-24px taps.
- [ ] Probe every accent/low-opacity color on green panels (`getComputedStyle(el).color` + parent background) — list each failing combo before touching CSS.

### Step R2 — Typography clamp (the H2-inversion fix)

- [ ] In the page's `<style>` block, replace any static heading sizes with clamps (desktop px unchanged):

```css
/* page-scoped heading scale — Direction D serif comes from body.theme-d, only size here */
h2 { font-size: clamp(1.3rem, 3.4vw, 1.65rem); }
h3 { font-size: clamp(1.05rem, 2.2vw, 1.2rem); }
```

  Adapt selectors to the page's existing scoped class (e.g. `.captive-d h2 {…}`). If headings are sized by utility classes instead, override in the scoped style block — do NOT edit `direction-d.css`.
- [ ] Re-probe at 375px: H1 px > H2 px > H3 px must hold.

### Step R3 — Contrast on green panels (AA recipe, ratios pre-verified)

- [ ] Define page accent tokens once in the page style block:

```css
:root { --peach: #ffd6cf; --mint: #c2f7d4; --clay-ink: #c8472f; --clay-text: #b04228; }
```

- [ ] Apply the playbook recipe (§3) wherever the probe failed:
  - tile backgrounds on `--green`: `rgba(255,255,255,.07–.1)` → `rgba(0,0,0,.14)` (`.18–.2` for bad/final rows); keep white borders
  - low-opacity white text: ≥`.85` on panel green, ≥`.92` inside tiles
  - small peach/clay accents on green (`#f08070`, `#ffb3a6`, `#ffccc5`) → `var(--peach)`; `#7ce8a6` → `var(--mint)`; both originals OK only as large text ≥18.66px bold
  - clay fills w/ white small text → `var(--clay-ink)` (hover `#b03c26`); clay small text on light → `var(--clay-text)`
  - dark-green gradients (`#162f23→#1f4d38`): eyebrows use `#ffb3a6`
- [ ] Grep the page for **inline** `style="color:#…"` (bar labels, legend spans) and fix those too: `grep -n 'style="[^"]*color' src/pages/<slug>/index.astro`

### Step R4 — Desktop dial + mobile jump nav (≥30K pages only)

- [ ] Import + place the component (frontmatter + right after `<Breadcrumb>`/hero):

```astro
import JumpRail from '../../components/cag-library/JumpRail.astro';
```
```astro
<JumpRail sections={jumpSections} partNames={jumpPartNames} ctaLabel="Ask C.A.Gs →" ctaTarget="contact" />
```

- [ ] Build the page's `jumpSections` map from its existing section `id`s (probed in R1; e.g. captive-bred already has `what-it-means`, `vs-wild-caught`, `how-we-raise`, `why-it-matters`, `attribute-cluster`, `available-birds`, `faq`, `contact`). Document order required; group into 3–4 `partNames`; labels ≤2 words. Pattern:

```astro
const jumpSections = [
  { id: 'what-it-means',  label: 'What It Means', part: 1 },
  { id: 'vs-wild-caught', label: 'vs Wild-Caught', part: 1 },
  // … every major section id, in document order …
  { id: 'faq',            label: 'FAQ',            part: 3 },
  { id: 'contact',        label: 'Ask C.A.Gs',     part: 3 },
];
const jumpPartNames = { 1: 'Understand', 2: 'Our Process', 3: 'Next Steps' };
```

- [ ] Add the **section-next-nav auto-injector** (the "↓ Continue:" links) to the page's closing `<script>`, adapted to this page's section structure. The scam page pairs `a[name]` anchors with `.section-block`s; interior pages use `id`d `<section>`s directly — iterate those instead:

```js
// Section jump-nav auto-injector — "↓ Continue: <next section>"
(function(){
  var ids = ['what-it-means','vs-wild-caught', /* …same order as jumpSections… */ 'faq','contact'];
  var labels = { 'what-it-means':'What Captive-Bred Means', /* …human label per id… */ };
  for (var i = 0; i < ids.length - 1; i++) {
    var cur = document.getElementById(ids[i]);
    if (!cur) continue;
    var nav = document.createElement('div');
    nav.className = 'section-next-nav';
    nav.innerHTML = '<a href="#' + ids[i+1] + '" class="section-next-link">&#8595; Continue: ' + (labels[ids[i+1]] || ids[i+1]) + '</a>';
    cur.appendChild(nav);
  }
})();
```

- [ ] Style it — **MUST be `:global()`** (JS-injected DOM never matches Astro scoped CSS — this shipped unstyled once already):

```css
:global(.section-next-nav){text-align:right;padding-top:18px;margin-top:14px;border-top:1px solid #ede5dc}
:global(.section-next-link){font-family:'IBM Plex Sans',sans-serif;font-size:.85rem;font-weight:600;color:var(--clay-text,#b04228);text-decoration:none;display:inline-block;padding:10px 0 10px 12px;margin:-10px 0}
:global(.section-next-link:hover){text-decoration:underline}
```

### Step R5 — Scroll / interaction polish (all pages)

- [ ] Every jump target gets clearance under the 96px sticky header:

```css
section[id], [id="faq"], [id="contact"] { scroll-margin-top: 110px; }
```

- [ ] Reduced motion guard next to any `scroll-behavior:smooth`:

```css
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
```

- [ ] Pad any sub-24px text links found in R1 to ≥24px tap height (`padding:10px 0;margin:-10px 0` pattern).

### Step R5b — Hero eyebrow = homepage HeroV3 pattern

- [ ] If the page hero has a pill/uppercase eyebrow, restyle to the HeroV3 pattern (no pill, no uppercase):

```css
.hero-eyebrow{font-family:'IBM Plex Sans',sans-serif;font-size:10px;font-weight:500;letter-spacing:.12em;color:rgba(255,255,255,.75);text-transform:none}
@media(min-width:768px){.hero-eyebrow{font-size:11px}}
```

  Text stays sentence case, e.g. "Captive-Bred Standard — Updated June 2026". Content rule: only restyle the existing eyebrow text, don't invent new copy.

### Step R5c — Forms (if the page has one)

- [ ] Any inquiry/newsletter form on the page POSTs to the verified endpoints (`docs/design.md` map): contact-us → `formspree.io/f/xrejpnvn`; product pages + newsletters → `formspree.io/f/xpqoeazq`. Inputs need `name=` attributes + a hidden `_subject`. Never a `f/placeholder`.

### Step R6 — Mobile paragraph length

- [ ] Ceiling **240 plain-text chars per `<p>`**. Find offenders:

```bash
python3 - <<'EOF'
import re, html, sys
src = open('src/pages/<slug>/index.astro').read()
for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', src, re.S):
    txt = re.sub(r'<[^>]+>', '', m.group(1)); txt = html.unescape(txt).strip()
    if len(txt) > 240: print(len(txt), '|', txt[:90].replace('\n',' '))
EOF
```

- [ ] Split each at the sentence boundary nearest the midpoint (skip `U.S.`, decimals, abbreviations). Manual edits are fine at this volume; never split inside a tag.
- [ ] Card containers that zero `<p>` margins then need: `.card-class p{margin:0 0 8px} .card-class p:last-child{margin-bottom:0}` for every page-local card class touched.

### Step R7 — Image delivery

- [ ] If the page has a hero/LCP raster image: generate 480w + 640w WebP with Pillow (`quality=70, method=6`), wire `srcset="… 480w, … 640w, … 768w" sizes="(max-width:900px) 92vw, 420px"`.
- [ ] Skip if the page's hero is CSS-only or already has the srcset (header logo is done site-wide via `Logo.astro` — don't redo).
- [ ] All `<img>` carry explicit width/height integers (no `height="auto"`), `loading="lazy"` below the fold.

### Step R8 — Verify loop + ship

- [ ] `npx astro build` — exit 0, no warnings for this page.
- [ ] `npx astro preview` + Playwright re-probe at 375 and 1280: heading hierarchy holds, zero overflow, recolored panels pass (spot-check computed colors), `scroll-margin-top` = 110px on targets, JumpRail dot rail visible ≥1024px and "Sections" sheet button <1024px, "↓ Continue:" links styled.
- [ ] Screenshot the recolored infographic sections at 375px (visual sanity).
- [ ] Verify heading order in **dist/** not source: `python3 -c "import re;h=[m for m in re.findall(r'<h([1-6])', open('dist/<slug>/index.html').read())];print(h)"` — no level ever jumps by more than +1.
- [ ] Commit + push (push = deploy):

```bash
git add src/pages/<slug>/index.astro
git commit -m "feat(<short-slug>): scam-playbook polish — JumpRail dial + mobile jump nav, AA panels, clamped headings, short mobile paragraphs"
git push
```

- [ ] After the batch deploys: poll live page 200, then IndexNow POST for the batch URLs (key `f8071f0dbdb94257934a690f4a18fa59`, `api.indexnow.org`, host `congoafricangreys.com`).

---

## Session 1 tasks (this session)

### Task 1: `trusted-african-grey-parrot-breeders` (About Us)
**Files:** Modify `src/pages/trusted-african-grey-parrot-breeders/index.astro`
- [ ] Run recipe R1–R8. Existing ids (8) → jumpSections. Heading ladder 1/8/4/1/1/1 already valid — verify rendered order only.

### Task 2: `captive-bred-african-grey-parrot`
**Files:** Modify `src/pages/captive-bred-african-grey-parrot/index.astro`
- [ ] Run recipe R1–R8. Ids: `what-it-means, vs-wild-caught, how-we-raise, why-it-matters, attribute-cluster, available-birds, faq, contact`. Page scope class `.captive-d`.

### Task 3: `cites-african-grey-documentation`
**Files:** Modify `src/pages/cites-african-grey-documentation/index.astro`
- [ ] Run recipe R1–R8. 8 ids probed. CITES copy is legal-adjacent — zero humor, zero content edits (Same-Content rule).

### Task 4: Session close-out
- [ ] Update this plan: check off completed pages in the schedule table.
- [ ] Update `sessions/` brief with any new traps discovered (append to the playbook if recipe-level).
- [ ] Live-verify all 3 slugs return 200 + IndexNow batch POST.

## Sessions 2–6

Repeat Tasks 1–4 with that session's pages from the schedule table. Session-specific notes:
- **Session 2, faq page:** before R4, add `id`s to each of its 4 H2 category sections (currently only 1 id on the page) so jump targets exist.
- **Session 6, contact-us:** add H2s to its natural sections (form, contact details, what-happens-next) — currently H1-only; no JumpRail (4.4K chars).
- **Session 6, privacy-policy:** legal text verbatim (shell-only rule from the interior batch); sizing + contrast only.
- **Session 6 close:** `bash scripts/health-sweep.sh`, confirm sitemap unchanged (no new URLs), final 18/18 live check.

## Session 1 findings — fold into every later session (IMPORTANT)

These came out of executing batch 1 and are now part of the recipe:

1. **The `.bg-clay { color:inherit }` bug is in EVERY interior page's scoped CSS** (`.trust-d`/`.captive-d`/`.cites-d` pattern, the line `.X-d .hero-v3-b .text-clay, .X-d .bg-clay { color:inherit; }`). It leaks dark stone text onto clay buttons/tags in light sections (~2.5:1 FAIL). Fix: split the rule — hero `.text-clay` keeps `color:inherit`, and `.X-d .bg-clay { color:#fff; }`. **Grep each page for `\.bg-clay { color:inherit`** first thing.
2. **The H2→H4 skip is systemic**: every interior page has an h4/h5/h6 mini-heading trio directly under an h2 (the interior-batch "full ladder" pattern). Fix: re-level trio to h3/h4/h5 and derive an h6 from the final paragraph's second sentence (split the paragraph; heading text summarizes existing copy — no new claims). Verify in dist: no level jumps +2, all 6 levels present.
3. **`CompareTableE` ships `text-3xl` on its H2** (30px mobile = H1 tie). Page-scoped fix: `.X-d h2.text-3xl { font-size: clamp(1.375rem, 3.8vw, 2.25rem); }`. Any page importing CompareTableE needs this (captive-bred had it; check variant pages later).
4. **FAQ answers are data-array strings rendered as one `<p>`** — split with literal `\n\n` in the string, change renderer to `{item.a.split("\n\n").map((t) => <p …>{t}</p>)}`, and join in schema with `text: f.a.replace(/\n\n/g, " ")`. Verify dist FAQPage JSON has no `\n`.
5. **Interior pages' `<style>` is already `is:global`** — next-nav rules don't need `:global()` wrappers here, just scope under the page wrapper class (which exists in DOM).
6. **Paragraph ceiling residuals**: single long sentences (numbered-list sentences, semicolon lists), verbatim testimonial quotes, and shared-component copy (OwnerCard) stay as-is. Target: nothing splittable left over ~270.
7. **Hero images on this template are already 640×480 WebP ≤62KB** displayed in a ≤300px circle — no srcset work needed (R7 is usually a no-op; check size before generating variants).
8. **`astro preview` serves dist statically and picks up rebuilds** — start it once, rebuild freely, just re-navigate.

## Session 2 findings — fold into every later session (IMPORTANT)

1. **Long-section breakup is now part of the recipe (user directive 2026-06-12).** Any section with 3+ consecutive prose paragraphs and no visual variation gets a component treatment that RETAINS all copy: numbered channel cards (`.adopt-chip` pattern), green-header-band info cards (design-system idiom), a compact green process-flow strip (`.adopt-phases` pattern, labels drawn from existing copy only), and/or a `<figure>` with a real aviary photo + figcaption link (max-w-[420px], compressed ≤16KB WebP, explicit `object-position` crop). Reference: african-grey-adoption sections #where / #verify / #rehomed / #better-fit.
2. **"Updated June 2026" eyebrows are gone site-wide** — replaced with page-LSI phrases (commit `7ac6d37`). Do NOT reintroduce "Updated {date}" in any hero eyebrow. R5b example text is superseded.
3. **`--color-clay-ink` is now `#bd4129`** (was `#c8472f`, which failed 4.47:1 as small text on the `#faf7f4` page background). White-on 5.31:1, on-cream 4.98:1. New pages reference #bd4129.
4. **stone-400 is banned as text on light surfaces** — shared components (BirdCard, cag-bird-card-v2, CompareTableE, NewsletterV2) now use stone-500; figcaptions on the cream page bg use stone-600 (stone-500 is 4.49:1 there — just under).
5. **Hero photos must show the bird's face/interaction** — african-grey-review-top.webp (sleeping chick, head tucked) reads as a headless bird in the hero circle; swapped for the Catherine Kempf buyer photo. Check every hero image candidate at the circle crop before shipping.
6. **Rocket Loader `/70de/` unused-JS + missing-source-map Lighthouse flags are dashboard-only** (playbook §10) — Cloudflare → Speed → Optimization → toggle OFF. API tokens are dead; manual toggle required.

## Carryover rules (every session)

1. Read `PRODUCT.md` + `DESIGN.md` + the playbook before touching files.
2. Same content — polish never adds/removes copy (paragraph splits keep every word).
3. Commit + push per page or per batch; never leave work unpushed.
4. Known traps: Cloudflare API tokens are dead (dashboard toggles are manual); `requestIdleCallback` for gtag is banned (12s setTimeout, already in BaseLayout — don't re-add per page); JS-injected DOM needs `:global()` CSS.

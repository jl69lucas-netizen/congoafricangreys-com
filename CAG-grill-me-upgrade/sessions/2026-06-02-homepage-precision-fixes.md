# Session — Homepage Precision Fixes (2026-06-02)

**Scope:** Audit-driven fixes on the homepage (`src/pages/index.astro`) + shared components, in response to a pasted SEO/a11y/Lighthouse/CSP audit. All work shipped to `main` (auto-deploys → Cloudflare Pages) and verified live.

**Commits (all pushed + live, verified):**
| Hash | What |
|---|---|
| `bc53912` | CSP unblocks GA4 + a11y/SEO hardening (Phase 1) |
| `1281074` | Full H1–H6 heading hierarchy (Phase 2) |
| `220c1b5` | Clay eyebrow contrast → AA |
| `e019255` | Broken World Parrot Trust links → parrots.org |
| `ce68515` | Performance pass (~150 KB, LCP 8.6→3.5 s) |
| `62de207` | Forest-green map pin overlay (homepage + contact-us) |

---

## PRECISE FIX PATTERNS (reusable — for future agents)

### 1. CSP blocking Google Analytics / gtag (HIGH-VALUE ROOT CAUSE)
**Symptom:** Console errors — `googletagmanager.com` / `region1.google-analytics.com` "violates CSP directive".
**Root cause:** `deploy.yml:33` does `cp site/content/_headers public/_headers`. So **`site/content/_headers` is the SOURCE of truth** — a hand-edit to `public/_headers` gets overwritten on every deploy. The source had a restrictive CSP missing the Google domains.
**Fix:** Edit **`site/content/_headers`** (and keep `public/_headers` in sync). Correct CSP needs:
- `script-src`: `... https://www.googletagmanager.com https://www.google-analytics.com`
- `connect-src`: `... https://www.googletagmanager.com https://*.google-analytics.com https://*.analytics.google.com`  ← the **wildcard** is essential; GA4 uses regional endpoints like `region1.google-analytics.com`.
- `frame-src`: `https://www.google.com https://maps.google.com https://www.youtube.com https://www.youtube-nocookie.com`
**Owner:** `skills/cag-website-health.md` (CSP/headers layer).

### 2. Invalid `<dl>` (axe: "dl's do not contain only properly-ordered dt/dd")
**Where it bit us:** `KeyTakeawayV2.astro` (had a `<p>` child) + `CounterSnippet.astro` (had `<dd>` BEFORE `<dt>`). Both were **stat grids**, not term/definition lists.
**Fix:** Convert `<dl>/<dt>/<dd>` → neutral `<div>`s (stats aren't definitions). Pixel-identical, no visual change. Only use real `<dl>` when content is genuinely term→definition AND `<dt>` precedes `<dd>`.

### 3. Heading hierarchy — DON'T gut H3 to hit a number
**The trap:** "Too many H3 (47), cut to 20." But `docs/reference/seo-rules.md` (lines 177–182) sets the target band: **H2 25–35 · H3 40–50 · H4 10–20 · H5 5–10 · H6 3–8**. So 47 H3 was *in band*; the real violations were **H4/H5 below band and H6 = 0**.
**Constraint:** ~half the H3s are uniform **sibling grids** (bird cards, FAQ, how-to steps, care cards, footer). Siblings MUST share one level, and Rule 52 bans level-skipping. So you can only demote *genuinely-nested* headings — naive cutting breaks hierarchy and hurts SEO.
**How we added depth (47→43 H3, 3→10 H4, 4→5 H5, 0→3 H6, zero skips):**
- Demote genuinely-nested H3→H4 (e.g., "captive-bred" under "USDA-verify").
- Group sibling tool cluster under a NEW H3, demote the tools to H4 (keeps siblings uniform).
- Add **H4 group labels** above accordions ("Common Questions From … Buyers").
- Add **H6 voice-search sub-questions** inside accordion answers (re-tag existing copy; LSI/NLP).
**Verify:** extract heading tree from `dist/` and run a level-skip check (script in this session's history) — counts in band + 0 skips.

### 4. Clay eyebrow contrast (WCAG AA)
**Issue:** clay `#e8604c` text ≈ **3.2:1 on cream / 3.4:1 on white** — fails AA (4.5:1) for small uppercase eyebrow labels.
**Fix:** `#b04228` (= **5.4:1 on cream**), same clay family. ONE scoped rule in `src/styles/direction-d.css`:
```css
body.theme-d .text-clay.uppercase,
body.theme-d .cag-tag.text-clay { color: #b04228; }
```
**Why this selector is safe:** eyebrows are `text-clay` + `uppercase` (or `.cag-tag`); mid-sentence body **links are `text-clay` but never `uppercase`**, and **clay pill buttons use white text** — so neither is touched. Brand-locked clay buttons stay `#e8604c` (CLAUDE.md). Decorative underline tick stays full clay.

### 5. Performance (Astro homepage; Lighthouse mobile)
- **ClientRouter / View Transitions (~68 KB unused JS):** safe to remove from `BaseLayout.astro` ONLY if `grep -rn "transition:animate|transition:persist|astro:page-load|astro:after-swap"` returns 0 (it did). Big TBT/JS win.
- **Google Fonts render-blocking (~1.5 s):** merge multiple `css2?family=` requests into ONE, load non-blocking via `media="print" onload="this.media='all'"` + `<noscript>` fallback. `display=swap` already handles FOUT.
- **Duplicate font CSS/preconnects:** `index.astro` was injecting Newsreader/IBM-Plex + preconnects into `<body>` that BaseLayout already loads in `<head>` → removed (also cleared the ">4 preconnects" warning).
- **LCP hero:** preload via `BaseLayout`'s `extraHeadHtml` prop: `<link rel="preload" as="image" href="…hero.webp" fetchpriority="high" type="image/webp">`.
- **Image re-encode (~86 KB):** logo PNG 256→160px (sips), hero webp 1040→800px, owner webp q78. **sips CANNOT write real WebP** (it silently outputs JPEG-in-`.webp`, often larger) — **use Python Pillow** (`features.check('webp')` → True): `im.resize(...).save(p,"WEBP",quality=82,method=6)`.
- **Result:** Perf 53→~68–80, LCP 8.6→~3.5 s, FCP 3.0→~1.7 s (warm median-of-3).

### 6. Custom map pin without an API key
**Issue:** free Google `output=embed` iframe can't recolor its default red pin.
**Fix:** `src/components/MapPin.astro` — a brand SVG teardrop overlaid on a `.cag-map-wrap` (position:relative) wrapper; tip anchored to map-center via `position:absolute; left:50%; top:50%; transform:translate(-50%,-100%)`; `pointer-events:none` keeps map interactive. Covers Google's red marker (which sits at the q-location = map center). **Caveat:** pin is fixed to center, doesn't follow panning — fine for a "here we are" embed. Brand pin color = forest green `#2D6A4F`.

---

## WHAT WENT WELL (keep doing)
- **Root-cause over symptom:** traced the CSP bug to `deploy.yml` cp, not just patching `public/_headers`.
- **Grounded every claim in real output:** read actual files + `dist/`, computed contrast ratios, verified pin geometry (tip offset 0,0), Lighthouse before/after.
- **Confidence Gate honored:** did NOT "fix" the "descriptive link text" finding — it was an auditor false-positive (`View All Birds →` already has text).
- **Recommend + Why on every fork** via `AskUserQuestion`, with the trade-off named (per CLAUDE.md).
- **Respected sibling-grid uniformity** instead of breaking hierarchy to hit a vanity H3 count.
- **Surgical, scoped fixes:** one CSS rule for contrast; neutral-div for `<dl>`; no shared-component blast radius beyond what was approved.
- **Verified before claiming done:** build + dist greps + preview + live curl markers.

## WHAT WENT WRONG (avoid next time)
- **Checked SOURCE literal instead of rendered output for schema:** first said "FAQPage missing" because `grep FAQPage src/pages/index.astro` = 0 — but it's generated by `<Schema type="faq">`. **Lesson: verify schema/SEO in `dist/` (rendered), not source literals.** Corrected mid-session.
- **Over-promised "~22 H3"** before counting demotable headings against the sibling-grid + shared-component constraints. **Lesson: count what's actually demotable BEFORE quoting a target.** Corrected to the rules-aligned ~43.
- **Trusted a single Lighthouse run** — a cold-cache run reported Perf 33 (looked like a regression). **Lesson: Lighthouse is noisy; run warm median-of-3** before reporting. Warm median was 68–80.
- **sips WebP trap:** wasted a step discovering sips writes fake (JPEG) WebP. **Lesson: use Pillow for WebP.**
- **Tooling gotchas:** zsh `for h in 1..6; <h$h[ >]` throws "bad math expression" — **use Python for heading/markup counts.** Preview sandbox **can't render external iframes** (Google Maps blank) — **verify embeds by geometry/computed style, not screenshots.**

## OPEN / NEXT
- **Perf next lever:** TBT still ~600–1000 ms and LCP ~3.5 s (just over 2.5 s ideal) — likely the React island + remaining JS. Diminishing returns; revisit if pushing for 90+.
- **CSP hardening (deferred):** still uses `script-src 'unsafe-inline'`; removing needs nonces/hashes for inline gtag + Astro inline scripts (risky — can break GA). Do after perf, carefully.
- **BreadcrumbList schema:** absent on homepage (non-standard for a root page; low priority).
- **Map pin:** verify visually on live (preview sandbox couldn't render the Google iframe).

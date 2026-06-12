# Scam-Page Polish Playbook — apply to the remaining 17 Direction-D interior pages

**Source session:** 2026-06-12 · commits `196536d` + `56d9989` · reference page: `/how-to-avoid-african-grey-parrot-scams/`
**Use:** run this checklist verbatim on each of the other 17 interior pages (Clusters A–E, see CLAUDE.md §Interior-Pages Batch).

---

## 1. Measure first (never fix blind)

Playwright at **375×812**, then 1280×900, run `getComputedStyle` probes (not screenshots) for:
- Every H1–H6 font-size (aggregate by tag+size) — catch hierarchy inversions
- `scroll-margin-top` on jump targets (sticky header is **96px**)
- Computed `color`/`fontSize` of every low-opacity / accent text class
- Horizontal overflow (`scrollWidth` vs `innerWidth` + per-element rects)
- Tap-target heights on links/buttons (`<24px` fails WCAG 2.5.8)

## 2. Typography — the H2 inversion trap

Interior pages that set static `h2{font-size:1.65rem}` render H2 **26.4px > H1 25.6px on mobile**.
Fix: `h2{font-size:clamp(1.3rem,3.4vw,1.65rem)}` and `h3{font-size:clamp(1.05rem,2.2vw,1.2rem)}`
— desktop pixels unchanged, mobile drops to 20.8/16.8px and restores hierarchy.

## 3. Contrast on green infographic panels (the big one)

Root cause: white-tint tile backgrounds (`rgba(255,255,255,.07–.1)`) over `--green #2D6A4F`
**raise** bg lightness, so all low-opacity white + peach/mint accent text fails AA.

The recipe (all ratios verified):
- **Tile backgrounds → dark tint:** `rgba(0,0,0,.14)` (normal), `.18–.2` (bad/final rows). Keep the white borders.
- **Low-opacity white text:** ≥`.85` directly on panel green (5.1:1) · ≥`.92` inside tiles (4.6:1). Never below.
- **Accent tokens** (define in page `:root`):
  - `--peach: #ffd6cf` replaces failing `#f08070` (2.4:1), `#ffb3a6` (3.7:1), `#ffccc5` (4.35:1) for small text on green
  - `--mint: #c2f7d4` replaces `#7ce8a6` (4.2:1)
  - `#7ce8a6` / `#ffccc5` are still OK as **large** text ≥18.66px bold (e.g. 2.4rem stat numbers)
- **Clay fills with white small text** (3.38:1) → `--clay-ink: #c8472f` (4.78:1), hover `#b03c26`. Applies to: primary CTAs, pill buttons, form submits, badges, step-number chips.
- **Clay as small text on light** → `--clay-text: #b04228` (related-card tags, inline links styled `color:#e8604c`).
- On **dark-green gradients** (`#162f23→#1f4d38`): `#ffb3a6` passes (5.6:1) — use it for eyebrows there; `#e8604c`/`#f08070` fail.
- Check **inline styles in the HTML** too (`style="color:#ffccc5"`, bar labels, legend spans).

## 4. Scroll / interaction polish

- `scroll-margin-top:110px` on every jump target (`.section-block`, form sections, `#faq`…) — the sticky header otherwise buries each jumped-to heading.
- `@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}` next to `scroll-behavior:smooth`.
- **JS-injected elements never get Astro scoped CSS.** The `.section-next-nav`/`.section-next-link` "↓ Continue:" links are created client-side → their rules MUST be `:global(...)` (they shipped completely unstyled). Grep each page for `innerHTML`/`createElement` markup classes and `:global` those rules.
- Small text links get padding to ≥24px tap height (`padding:10px 0 10px 12px;margin:-10px 0`).

## 5. Hero eyebrow = homepage HeroV3 pattern

No pill, no uppercase. `font-size:10px` (11px ≥768px), `font-weight:500`, `letter-spacing:.12em`,
`color:rgba(255,255,255,.75)`, IBM Plex Sans, sentence case text ("Scam Prevention Guide — Updated June 2026").

## 6. Mobile paragraph length

Ceiling: **240 plain-text chars per `<p>`** (≈2–4 lines at 375px). Split at sentence boundaries
nearest the midpoint, skipping abbreviations (`U.S.`, decimals). Script pattern saved in this
session (regex over `<p>…</p>`, depth-tracked so it never splits inside a tag).
After splitting, card containers that zero `<p>` margins need: `margin:0 0 8px` + `:last-child{margin-bottom:0}`
for `.scam-card p,.q-body p,.step-content p,.report-step-body p,.callout-green p,.warn-body p` (and any page-local equivalents).

## 7. Image delivery

- Hero/LCP images: generate **480w + 640w** WebP variants with Pillow (`quality=70, method=6`),
  `srcset="… 480w, … 640w, … 768w" sizes="(max-width:900px) 92vw, 420px"`. 640w exists because DPR2 mobile (≈634px need) otherwise pulls the full 768w.
- Header logo is already `/cag-header-logo-160.webp` (5.7KB) site-wide via `Logo.astro` — done once, don't redo.
- `LogoBadge.astro` heights fixed (`64→21, 96→32, 200→66`) — `height="auto"` is invalid HTML and a CLS flag.

## 8. Forms (verified working 2026-06-12)

- Endpoint map lives in `docs/design.md`: contact-us → `formspree.io/f/xrejpnvn`; **product pages + newsletters → `formspree.io/f/xpqoeazq`**.
- `xpqoeazq` verified live: POST returns `{"ok":true}`. Inputs need `name=` attributes + a hidden `_subject`.
- `src/components/cag-newsletter-v2.astro` still has `f/placeholder` — orphan (unused), fix before ever using it.

## 9. GA4 / third-party (site-wide, done once in BaseLayout)

gtag.js loads on first interaction OR a **12s plain setTimeout** — NOT `requestIdleCallback`
(idle fires ~1–2s post-load and drags 156KB gtag back into the Lighthouse trace).

## 10. Dashboard-side items (cannot fix in repo)

- **Rocket Loader** (`/70de/` script: forced reflow + missing source map + unused JS) → Cloudflare → Speed → Optimization → Content Optimization → toggle OFF.
- **Email Obfuscation** (`email-decode.min.js` cache-TTL flag) → Cloudflare → Scrape Shield → toggle OFF (trade-off: exposes plain-text emails to scrapers; email is already public in schema).
- Stored Cloudflare API tokens (memory file, 2026-05-21) are **dead** — rotated in the 2026-06-01 token cleanup. Need a fresh token (Zone Settings:Edit) via the clipboard method, or manual dashboard toggle.

## Verify loop (every page)

`npx astro build` → `npx astro preview` → Playwright probes at 375 + 1280 (colors, heading sizes, overflow, scroll-margin, currentSrc of hero image) → screenshots of recolored infographics → commit + push → poll live asset 200 → IndexNow POST (key `f8071f0dbdb94257934a690f4a18fa59`, api.indexnow.org, host congoafricangreys.com).

---

## Addendum — Interior-template traps found in rollout Session 1 (2026-06-12 PM)

Applying this playbook to the interior-batch pages (trusted-breeders / captive-bred / cites-docs) surfaced template-wide traps the scam page didn't have:

- **`.bg-clay { color:inherit }` AA bug in every interior page's scoped CSS** — overrides `text-white`, dark stone text lands on clay buttons/tags (~2.5:1). Fix: `.X-d .bg-clay { color:#fff; }` (hero `.text-clay` keeps inherit). Grep first on every page.
- **Systemic H2→H4 skip** — each interior page has an h4/h5/h6 mini-trio under an h2. Re-level to h3/h4/h5 + derive an h6 from the final paragraph's second sentence (split it; heading summarizes existing copy).
- **`CompareTableE` H2 = `text-3xl` (30px) ties the mobile H1** — page-scoped `h2.text-3xl { font-size: clamp(1.375rem, 3.8vw, 2.25rem); }`.
- **FAQ answers live in a data array** → split with `\n\n` + `.split("\n\n").map()` renderer + `f.a.replace(/\n\n/g, " ")` in FAQPage schema (verify dist JSON has no `\n`).
- Interior `<style>` blocks are already `is:global` — next-nav CSS scopes under the page wrapper class, no `:global()` needed.
- JumpRail drops in cleanly: import + `<JumpRail sections partNames ctaLabel ctaTarget>` right after the hero `</section>`; the pages' existing section ids are the map.

Full rollout schedule + per-page recipe: `docs/superpowers/plans/2026-06-12-interior-polish-rollout.md`.

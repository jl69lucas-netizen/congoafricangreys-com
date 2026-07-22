# Technical SEO / Lighthouse Fixes — Backlog for Other Pages

> Source: Lighthouse + axe run on `/timneh-african-grey-for-sale/` (2026-07-22).
> The **contrast** fixes below were applied to the Timneh page in that session; the rest are
> logged here so they can be swept across the rest of the site. Fix the shared components once
> and every for-sale sibling inherits it.

## 1. AA contrast — for-sale dial TOC + mobile jump-rail (SHARED COMPONENT — sweep the cluster)

Two failing patterns live in the **for-sale kit** (`.tdial` desktop dial + `.railB` mobile rail),
so the Congo, egg, and every future for-sale page built from the same tuple carry the same defect.

| Element | Was | Now (AA pass) | Ratio |
|---|---|---|---|
| `.tdial-list .num` (inactive index numerals, on white) | `#b8a294` (2.4:1 ✗) | `#6b625a` | ~5.9:1 |
| `.tdial-ring span` ("of N", on white) | `#b8a294` (2.4:1 ✗) | `#6b625a` | ~5.9:1 |
| `.railB a .p` (rail index number, on forest green) | `#a7e0c2` (~3.9:1 ✗) | `#c9f2db` | ~5.2:1 |
| `.railB a` inactive dimming | `opacity:.72` (drags white text + number below AA via compositing) | removed; active state uses `background:#25543d` + shadow instead | white on green ≥6:1 |

**Action:** apply the same four edits to `src/pages/congo-african-grey-for-sale/index.astro`,
`src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro`, and any for-sale page whose
component tuple includes a Dial TOC or the green Rail B. Never dim a nav item with `opacity` on a
colored pill — it composites the text toward the background and fails AA; distinguish the active
item with weight / shadow / a darker fill instead.

## 2. Unused JavaScript (LCP/FCP) — mostly infra, not page code

| Source | Transfer | Est. saving | Where it lives | Fix |
|---|---|---|---|---|
| Google Tag Manager `/gtag/js?id=G-MEWJ9GVC4T` | 158.9 KiB | 111.1 KiB | GTM (Google) | Consent-gate / defer GTM until interaction; load `gtag` after `requestIdleCallback` or on first scroll. GA4 config lives in `BaseLayout`. |
| `congoafricangreys.com /70de/` first-party | 167.8 KiB | 71.9 KiB | **Cloudflare Rocket Loader** (see memory `project_blog_perf_rocket_loader`) | Rocket Loader rewrites/serves this; toggle it per-page in the Cloudflare dashboard (Speed → Optimization) or via a Page Rule if it hurts LCP. Not editable in repo. |

## 3. Missing source maps for large first-party JS

- `/70de/` (Cloudflare Rocket Loader bundle) ships minified with no source map — expected for a
  Cloudflare-injected script; nothing to fix in the repo. Informational/unscored in Lighthouse.

## 4. Improve image delivery — responsive sizing

- **Symptom (Timneh available-cards):** `evie-...-female-card-440.webp` (440×440) served where the
  card renders ~319×319 → ~21 KiB waste. The card already uses `srcset` `440w, 800w` with
  `sizes="(max-width:980px) 46vw, 210px"`; the 440w is correct at DPR 2 for the 210px desktop slot,
  but the ~319px tablet render (46vw) at DPR 1 wants a ~320w source.
- **Fix (optional, low priority):** add a `-320.webp` source to the `.availC` card `srcset`, or drop
  the master card compression a notch (walk WebP quality down until <30 KB at 440px). Applies to every
  for-sale available-card image (Congo cards too).

## 5. General sweep checklist (run per for-sale page before "done")

- [ ] Dial `.num` inactive = `#6b625a`; ring "of N" = `#6b625a`
- [ ] Rail `.p` = `#c9f2db`; no `opacity` dimming on rail pills
- [ ] Every available-card `srcset` has a source ≤ the largest CSS render at DPR 1
- [ ] GTM deferred / consent-gated (site-wide, in `BaseLayout`)
- [ ] Re-run Lighthouse warm median-of-3 (per memory `feedback_lighthouse_median`)

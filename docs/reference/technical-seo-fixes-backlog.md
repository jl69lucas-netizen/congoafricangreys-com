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

## From the hand-raised hardening pass (2026-07-23)

- **Cloudflare Rocket Loader `/70de/`** — unused JS + "large first-party JS missing
  a source map" on every page. **Not fixable in code**: it is a dashboard toggle
  (Cloudflare → Speed → Optimization → Rocket Loader → Off). Breeder action.
- **Site-wide `img-no-srcset` backlog (187 WARN)** — surfaced by
  `python3 scripts/page_hardening_scan.py`. Ship `-240/-320/-440/-760` siblings
  with real `sizes` per the table in `skills/cag-page-hardening.md §1g`. Highest
  value first: timneh for-sale (5 images incl. a 1408px map), trusted-breeders,
  the comparison cluster.
- **Site-wide duplicate body copy (6,177 passages ≥12 words)** — concentrated in
  the location + `buy-*` pages (the shared USDA/CITES/DNA credential block).
  The for-sale cluster itself is clean. Needs a rewrite pass on the location
  cluster, not a whitelist expansion.
- **Title-Case heading sweep (1,099 headings across ~90 pages)** — surfaced by
  `page_hardening_scan.py` (`header-not-title-case`). The homepage, congo,
  timneh and hand-raised for-sale pages are the standard; everything else is
  still sentence case. Heaviest: the 6 `/available/` bird pages (~86 each) and
  the `/available/` hub (54). Spec: `skills/cag-page-hardening.md §1e-ter`.
  NOTE: FAQ `<summary>` questions stay conversational — headings only.

## dna-tested hero CLS — bimodal ~0.44 on mobile (found 2026-07-26, NOT yet fixed)

`/dna-tested-african-grey-for-sale/` fails Core Web Vitals CLS on cold mobile
loads. Measured with `npx lighthouse@12 --form-factor=mobile --screenEmulation.mobile
--throttling-method=simulate`, five runs:

| version | run 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| current (post Phase 5/6) | 0.442 | 0.001 | 0.444 | 0.442 | 0.443 |
| pre-session (`5e88b82`)  | 0.442 | 0.001 | 0.442 | 0.442 | 0.442 |

**It is pre-existing** — the pre-session build shows the identical distribution,
so nothing in the cross-sell or image work caused it.

**It is page-specific**: `/african-greys-for-sale-with-health-guarantee/` is a
flat 0.000 across three runs.

**The shifting node** is `main.dnat > header.hero > div.hero-grid > div.hero-copy`,
carrying the whole 0.442, with a second tiny shift on `div.hero-copy > h1 > em`.

Ruled out by measurement, do not re-try these:
- the `.xsell` cross-sell block and its CSS (bisection said yes, but that was
  single runs of a bimodal metric — it reproduces without the block)
- `<em>` in the H1 needing a late italic face (all six pages have one; five are clean)
- `.hero-mosaic{order:-1}` putting images above the copy (all six do this)
- `.mtile img{height:100%}` vs `height:auto` with `aspect-ratio` (no change, 5 runs)

**Because the distribution is bimodal, any future attempt MUST be judged on at
least 5 runs.** A single pass or fail means nothing here, which is how this was
first misattributed.

Most likely remaining suspect: a race between first paint and the async Google
Fonts stylesheet (`BaseLayout.astro`, `media="print" onload=...`). That is
exactly what Phase 1.1 self-hosting removes, so re-measure after that lands
before investigating further.

## Star-rating contrast on congo + timneh (found 2026-07-28)

`.stars{color:#c9a227}` measures **2.42:1 on white** — below even the 3:1 graphical-object floor, and well
below 4.5:1 if the ★ glyphs are treated as text. It ships on exactly two pages:

- `/congo-african-grey-for-sale/`
- `/timneh-african-grey-for-sale/`

The other four for-sale pages (hand-raised, dna-tested, health-guarantee, adoption-cost) already use
`var(--clay-ink)`, which passes. This is a two-line sweep to bring the last two into line:

```bash
grep -n '\.stars{color:#c9a227' src/pages/congo-african-grey-for-sale/index.astro src/pages/timneh-african-grey-for-sale/index.astro
```

Found while running the §2b contrast sweep on the adoption-cost hardening pass. Not fixed there because the
two pages were out of that build's scope.

## Unbuilt stub failing the audit: congo-african-grey-parrot-pair-for-sale (confirmed 2026-07-28)

`python3 scripts/final_page_audit.py --for-sale` returns **FAIL** for
`/congo-african-grey-parrot-pair-for-sale/`: `all_h1_h4`, `all_six_levels`, `min_h5_5`, `min_h6_5`,
`has_org`, `shipping_line`, `real_hero_image`. Measured H1:1 H2:3 H3:4 H4:0 H5:0 H6:0. It is a pre-existing
stub awaiting its own build slot in the 22-page programme, not a regression.

## Site-wide hardening-scan census, 2026-07-28

Full run over all 108 pages, from the adoption-cost harden session. **1106 ERROR · 135 WARN**, broken down:

| Rule | Count | Severity | Status |
|---|---|---|---|
| `header-not-title-case` | **1086** | ERROR | The **known** sentence-case backlog already recorded in `CLAUDE.md` (~1,099 headings / 68 pages). 98% of all errors. One `/available/` bird page alone carries 86. |
| `img-no-srcset` | 105 | WARN | Was recorded at 187; the backlog has shrunk. |
| `icon-text-baseline-drift` | 17 | WARN | ⚠️ This checker produced **6 false WARNs** on 2026-07-26 (matched keywords inside CSS comments, and did not know `place-items` is shorthand). **Verify before fixing.** |
| `form-control-ios-zoom` | **17** | ERROR | Comparison cluster + scams page. Not previously tracked here. Genuine candidates — controls under 16px auto-zoom on iOS focus. |
| `opacity-dims-text-contrast` | 13 | WARN | |
| `tap-target-spacing` | **3** | ERROR | ⚠️ This checker produced **7 false ERRORs** on 2026-07-26. All 3 are on comparison-cluster pages. **Verify before fixing.** |

**The whole 8-page for-sale cluster scans 0 ERROR · 0 WARN**, so none of the above touches it. The
`form-control-ios-zoom` and `tap-target-spacing` errors are concentrated in the **comparison cluster**
(`african-grey-comparison`, `-pros-and-cons`, `-breeders-comparison`, `-vs-macaw`, `-vs-cockatoo`,
`-vs-amazon-parrot`, `congo-vs-timneh`, `male-vs-female`) plus `how-to-avoid-african-grey-parrot-scams`.
That cluster is the natural scope for a single sweep.

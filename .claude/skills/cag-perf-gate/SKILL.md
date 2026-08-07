---
name: cag-perf-gate
description: Use before pushing any CAG page, and whenever PageSpeed/Lighthouse reports a defect — contrast, LCP, CLS, image delivery, unused CSS, render-blocking. Runs the local Lighthouse gate against dist/ so the breeder never has to paste a URL into pagespeed.web.dev after a deploy, and applies the banked fix for each audit class. Triggers "run the perf gate", "check PageSpeed", "why is CLS bad", "Lighthouse says", "contrast failure".
---

# CAG Perf Gate

Before 2026-08-07 no perf gate existed in this repo. What existed were two *agents*
(`cag-performance-fixer`, `cag-performance-monitor-agent`), and an agent is not a gate: it
runs when someone remembers to call it, produces prose, and nothing fails.

## Run it

```bash
npx astro build && python3 scripts/perf_audit.py <slug> && python3 scripts/perf_audit.py <slug> --mobile
```

Floors: performance ≥ 95 · accessibility / best-practices / SEO = 100.

The fast half runs in the render harness and needs no Lighthouse:

```bash
npm run test:render:meta && npm run test:render:pages
```

`a11y-text-contrast-aa` (A11Y family, **blocking**) computes contrast from rendered colours
in ~2s. Run the harness first; run Lighthouse before push.

## Before you fix anything

**A Lighthouse finding is a hypothesis about the page, not a fact about it.** Confirm it on
the built page at the breakpoint named before editing. Twelve checkers have cried wolf on
this site. See `skills/cag-gate-integrity.md`.

**Perf conclusions need ≥5 runs.** CLS here is bimodal — one run already produced a
confident wrong attribution. Use `--runs 5` and read the median and the spread, never a
single number. `reference_bimodal_metrics_need_5_runs`.

## Known-ignored

- **`valid-source-maps` on `/70de/`** — Cloudflare Rocket Loader, injected at the edge, not
  in this repo, and **Unscored** by Lighthouse. Toggle it in the Cloudflare dashboard
  (Speed → Optimization) or leave it. Never chase it in code. Suppressed by the CLI.

## The fix bank

| Audit | Root cause seen on this site | Fix |
|---|---|---|
| `color-contrast` | component re-themed, child colour never overridden (`.bpair .tdial` → `.ti` stayed sage, 2.66:1) | measure the ratio in Python, add the missing `.<page>` override — never eyeball. `reference_markup_css_drift` |
| `largest-contentful-paint` | srcset double-download | `heroPreload` + `heroPreloadSrcset` + `fetchpriority="high"` on the LCP image **only** |
| `cumulative-layout-shift` | counter / infographic / card with no reserved box | explicit `width`/`height` on every `<img>` + `min-height` on the container. `final_page_audit.py` `img_dims` fails the whole page without them |
| `uses-responsive-images` | `sizes` guessed instead of measured | measure a real rendered width in the browser. `reference_srcset_needs_measured_sizes` |
| `unused-css-rules` | dead kit CSS from a ported sibling | class-diff the page (`page_hardening_scan.py`), then **triage**: spec-mandated → render it; variant not used → delete. Never bulk-delete |
| `render-blocking-resources` | WooCommerce CSS + jQuery | defer; `font-display:swap`. `reference_aa_contrast_and_perf_fixes` |

## Related

`tests/render/checks/a11y.ts` · `scripts/page_hardening_scan.py` ·
`skills/cag-gate-integrity.md` · `reference_perf_image_tooling` (Pillow, not sips)

# Session 2026-06-05 — Broken components + a11y/perf fixes

**Scope:** 4 tasks from a Lighthouse/visual audit. All fixes in `src/` (live site), verified in `dist/` after `npm run build` (102 pages, clean). Visual + `getComputedStyle` confirmation via preview server.

## Agent fit (asked: "did I pick the right agents?")
- **cag-homepage-builder** — WRONG for most of this. It only rebuilds `index.astro` section-by-section with approval gates; these tasks are cross-component bug fixes (Header, Footer, JumpRail, BirdCard, Testimonials, SplitFeature, NewsletterV2) + 3 standalone bird-type pages.
- **cag-accessibility-fixer** — RIGHT for Tasks 3 & 4 (link text, contrast, target-size) but was scoped to `site/content/*.html`. Updated this session with an Astro-reality "CAG-Specific Antipatterns" section.
- **cag-performance-fixer** — RIGHT for Task 4d (unused JS) + Task 2 (CLS img dims) but also `site/content`-scoped. Updated with Fixes 6/7/8 (GA defer, Cloudflare Rocket Loader, component img dims).
- **No agent owned Task 1** — the 3 standalone bird-type pages aren't covered by any builder. Gap noted.
- Did the work inline (not via subagents): shared-component fixes need iterative verify; cold subagents would re-derive context.

## Task 1 — broken trust-bar badges (captive-bred, hand-raised, dna-tested)
Root cause: `.trust-item::before { content: '<svg…>' }` — CSS `content` can't render SVG; dumps raw markup + collapses badge spacing (separator lived in the pseudo-element). Symptom: "Hand-Fed from Week 212–16 Week Socialization…".
Fix: removed the `::before`, injected real inline `<svg stroke="currentColor">` into each badge span (site convention; currentColor = white on the dark-green bar → visible). Spacing from existing flex `gap`. Script handled all 3 files (14 badges). Added a CLAUDE.md icon rule + memory so it doesn't recur.

## Task 2 — CLS / lazy / breadcrumb
- 9 homepage imgs missing `width`/`height` → added to shared component `<img>` tags (Testimonials ×3, SplitFeature ×2) matching CSS box ratios. Now 0 missing.
- Footer logo → `loading="lazy" decoding="async"`.
- BreadcrumbList on homepage → intentionally SKIPPED (report itself says not appropriate for a homepage; belongs on interior pages via site-hygiene).

## Task 3 — non-descriptive "More" link
`MobileTabBar.astro` "More" tab → added per-item `ariaLabel` prop + `aria-label={tab.ariaLabel ?? tab.label}`. (Note: "More" and "Birds" both link to `/african-grey-parrot-for-sale/` — redundant but left.)

## Task 4 — contrast / target-size / unused JS
- Header active/hover clay-on-green → `text-white` + underline (white dropdown clay kept). `Header.astro`.
- JumpRail `min-height` 22→26px (WCAG 2.5.8 AA 24px); active/hover label clay→`#b04228`.
- "Must-Go Pair" amber badge `text-white`→`text-amber-950` (both BirdCard files).
- "New clutch alerts" badge clay→clay-lt `#f08070` (the `bg-clay/15` tint diluted bg below 4.5:1); newsletter taupe subtext `#9b9189`→`#b0a59b`.
- gtag.js deferred to first-interaction / idle in `BaseLayout.astro` (was `async` only). Trade-off: GA fires ≤3.5 s later on no-interaction bounces.
- `/70de/` 1st-party unused JS = **Cloudflare Rocket Loader** (edge-injected, `data-cf-settings`). NOT a code fix → **USER ACTION:** Cloudflare → Speed → Optimization → disable Rocket Loader.

## Open flags / follow-ups
- **USER:** disable Cloudflare Rocket Loader for the `/70de/` 71 KiB unused JS.
- Consider an owning agent (or extend a builder) for the standalone bird-type/feature pages (captive-bred, hand-raised, dna-tested) — currently orphaned.
- Re-run Lighthouse after deploy to confirm scores (warm median-of-3).

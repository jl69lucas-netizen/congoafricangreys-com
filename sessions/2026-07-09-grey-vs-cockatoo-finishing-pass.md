# Grey-vs-Cockatoo — Finishing Pass (2026-07-09)

Page: `/african-grey-vs-cockatoo/` · file `src/pages/african-grey-vs-cockatoo/index.astro`
Skills used: `cag-comparison-page-builder` + `impeccable` + `frontend-design`.
Status: **DONE + LIVE** (commit `8f12ec0`), gate `final_page_audit.py --comparison` = PASS-WITH-WARNINGS
(H1:1 H2:26 H3:41 H4:15 H5:8 H6:7 · Organization + FAQPage). WARNs = the flagship's standard trio
(wordcount_in_band / house_method / cites_captive_usda_early) — no regression.

These are **reusable finishing patterns for the remaining comparison spokes** (macaw, amazon, breeders,
hub). They extend `skills/cag-comparison-page-builder` §12; treat as binding for the next spoke polish.

## What changed (11 breeder asks)

1. **Newsletter relocation (in-flow).** Top NL moved OUT of the counter→body gap INTO the S8→S9 text
   gap (breaks two long image-less sections). Bottom NL moved from below the final form (dup with the
   form) to between CITES (S21) and Shipping (S18), copy re-matched to the CITES/shipping context.
   Both wrapped in `.nl-inflow{margin:24px 0;border-radius:18px;overflow:hidden}` so a full-bleed NL
   band reads as a rounded section card inside the `.cvt-main` article column. **Pattern:** relocate
   newsletters to break up the longest image-less runs; wrap in `.nl-inflow` when placing inside the
   article column.
2. **Slim middle newsletter = new opt-in `compact` prop on `NewsletterV2.astro`.** Middle variant only:
   `py-14→py-8`, image `h-[300px]/md:h-[320px] → h-[190px]/md:h-[210px]`, headline
   `md:text-4xl → sm:text-2xl` (kills the 36px-on-desktop outlier), tighter sub/form margins.
   Homepage default is unchanged (prop defaults false). **Reuse `compact` on every comparison spoke's
   middle NL** — the 4xl headline is off the page's own clamp scale otherwise.
3. **Quick Answer = the ASSIGNED 4B, not the flagship green box.** The section-matrix approved
   *"4B clay-recolored + Choose-if cards"* but the page had shipped the plain `.qa-box` green paragraph
   (same as congo-vs-timneh). Rebuilt to `.qa-snip` (clay-tinted gradient + map-pin accent, **no**
   side-stripe) + `.choose-grid` two cards (`.choose-c.grey` green top-accent / `.choose-c.too` clay
   top-accent). **Lesson:** on a finishing pass, re-check the section-matrix component IDs against what
   actually shipped — a page can silently inherit the flagship's component instead of its assigned one.
4. **Two photo swaps** (breeder-provided): grey-section close-up → Moluccan+Citron cockatoo contrast
   (`african-grey-vs-moluccan-and-citron-cockatoos.webp`, 375×500); CITES breeder photo →
   `Mark-with-our-grey-congo-parrot-pair-and-our-amazon-parrot.webp` (800×600, has -760). Alts written
   to the *visible* content (the CITES shot shows one grey + the green Amazon + breeder, so the alt says
   that — not a "pair" the crop doesn't show).
5. **Two new image-fit classes** (add to any spoke that swaps in off-ratio photos):
   `.sec-img.portrait-tall{max-width:340px;aspect-ratio:3/4}` (3:4 source shown whole, medium) and
   `.sec-img.photo43{max-width:480px;aspect-ratio:4/3;object-position:center 42%}` (4:3 landscape, medium).
   The stock `.sec-img` (760/400 cover) decapitates square/portrait sources — always match the class to
   the file's intrinsic ratio.
6. **Card crops bumped + head-biased** so bird heads show: species `.sp-media` 300→**320px** col +
   `object-position:center 20%` (mobile 16/9→**4/3**); `.bird-photo img` 200→**224px** @ `center 28%`;
   pair/eggs `.pair-c>img` 210→**250px**, `.pimg-pair` `50% 24%` (heads up), `.pimg-eggs` `50% 62%`
   (eggs down). **Rule:** when a card crop hides heads, raise height AND bias `object-position` toward
   the head band (≈20–30%), don't just center.
7. **Match-by-Household cards distinguished:** clay tick `::before`, green serif H4, hover lift, and the
   5th ("Busy Professional / hold off") card `grid-column:1/-1` as a full-width footer card with a green
   tick — fills the lone-odd-card gap in a 2-col grid of 5.
8. **TOC + jump-rail polish:** desktop `.cvt-toc a` → flex rows, tabular clay numerals (`min-width:16px`,
   `font-variant-numeric:tabular-nums`), hover indent; mobile `.rail-row a` → inline-flex + tabular nums.
9. **Compaction:** `.seam` 40→**28px**, `.cvt-body` padding 44/48→**34/40**, plus two seams removed
   (replaced by the relocated newsletters).

## Verify-in-browser method that worked (preview MCP was up this session)
- Screenshots reset scroll to 0 → to shoot a mid-page section, **clone it into a `position:fixed` probe
  div and `scrollTo(0,0)`**. Caveat: `.cvt` CSS custom props (`--f`, `--clay-ink`) don't resolve outside
  `.cvt`, so accent colors/`::before` ticks look absent in a bare clone — either add the vars to the
  probe style, or verify those via `getComputedStyle` on the *real* in-page element.
- Lazy images below the fold report `naturalWidth 0` (not broken) — confirm with a `fetch(url,{HEAD})`
  200 check instead.

## Not a repo fix (per §12.8)
Cloudflare Rocket-Loader perf flags (unused JS `/70de/`, forced reflow, render-blocking) = dashboard
toggle + cache purge. Warm-median Lighthouse can be run against the live URL via chrome-devtools MCP if
a number is wanted; the rendering pass (desktop + mobile) is done.

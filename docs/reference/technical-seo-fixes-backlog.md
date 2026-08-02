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

## markup↔CSS drift census, 2026-07-29 (NEW check `§1k`)

The line above — *"the whole 8-page for-sale cluster scans 0 ERROR · 0 WARN"* — was true of the
scanner as it stood, and **not true of the pages**. The new `markup-css-drift` / `markup-css-orphan`
checks (`scripts/page_hardening_scan.py` §1k, added 2026-07-29 from the adoption-cost harden lessons)
find **3 WARN on the same 8 pages the previous scanner called clean**. Verified by running the
pre-change scanner from git on the same slugs: `✅ clean — no known hardening defects found`.

| Page | Finding | Triage |
|---|---|---|
| `african-grey-parrot-bird-eggs-for-sale-usa` | **20 classes styled, never rendered**: `bird-*` (10) · `pair-*` (4) · `faq-d faq-open faq-q` · `nl-inflow` · `ship-mini` · `video-wrap` | **TRIAGED 2026-07-30: all 20 are DEAD CODE, 0 missing components.** Every one is superseded by a newer variant that *is* rendered — `bird-*` by `availB-*` (same 3-up grid, plus a `.hide` filter state), `pair-*` by `.xsell` (the 2026-07-26 decision to stop growing the card grid), `faq-*` by `faqC-*`, `nl-inflow` by `fs-nl-*`, `video-wrap` by `fs-video*`, and `ship-mini` by the full `ship-c` set. Safe to delete. **Correction: an earlier note here called this "5–6 whole components missing, highest priority" — that was wrong.** It counted raw unrendered classes without checking for renamed equivalents, which is precisely the triage `skills/cag-page-hardening.md` §1k says the scanner cannot do for you. |
| `timneh-african-grey-for-sale` | **14 classes styled, never rendered**: `carecards cc cc-k cc-s` · `chkT chkT-eyebrow chkT-grid chkT-head chkT-title` · `pb-bar pb-note pb-scale pb-zone priceband` | 3 components: a care-cards grid, a `chkT` checklist, and a `priceband` scale. Compare against the tuple ledger in `sessions/2026-07-19-for-sale-component-map.md` before deciding. |
| `african-grey-parrot-adoption-cost` | `faqC-a` **rendered with no CSS rule** on this page | Real. `hand-raised` styles it as `.handraised .faqC-a{padding:0 1rem 1rem 3.05rem}`; adoption-cost renders the same wrapper unstyled. Confirm in a real viewport before editing. |

**Two false positives were found and fixed in the check itself, not in the pages** (per
`skills/cag-gate-integrity.md`): `top` on the baby page is a comparison *value*
(`b.badge === "top"`), not a class — the orphan half now uses literal `class="…"` tokens only; and
`sr-only` is a generated Tailwind utility with no authored rule in `src/`.

**Scanner runtime is a pre-existing problem, not a regression from this check:** the unchanged
scanner takes ~43 s for 4 pages (~19 s fixed + ~6 s/page). A full 108-page run exceeds 8 minutes and
should be treated as a batch job, not an interactive gate.

### Component colour specificity (`§1l`), same run

| Page | Finding | Verified |
|---|---|---|
| `african-grey-parrot-adoption-cost` | `.ship-price{color:var(--clay-t)}` (line 1169, specificity 0,1,0) loses to `.ship-c p{color:#5b524a}` (line 1173, 0,1,1 **and** later in source). The three shipping prices render grey instead of clay. | **REAL.** Pointedly so: the comment at line 1163 records fixing `.ship-tier` this exact way (`.ship-c p.ship-tier{…}`) and `.ship-price` was left unqualified. Fix: `.ship-c p.ship-price{…}`. |
| `baby-african-grey-parrot-for-sale` | `.xsell-k{color:var(--clay-t)}` (1510) loses to `.xsell p{color:#4a423b}` (1511). The cross-sell eyebrow renders body grey. | **REAL.** Its siblings (eggs, adoption-cost, health-guarantee) all write `.xsell p:not(.xsell-k){…}`; baby is the only page that does not. Fix: adopt the `:not(.xsell-k)` form for consistency. |

**Three false-positive classes were removed from the check, not from the pages.** First pass reported
**586 WARN across 8 pages**; final is **2**, both confirmed by reading the CSS:

1. **Cartesian product, not nesting** (~578 of them). Pairing "ancestor appears in the file" with
   "component appears in the file" matched `.dial-ring span` against every component on the page.
   Nesting is now established from the DOM via `_subtrees_with_class`.
2. **An existing qualified rescue rule** (5 of them, all `.btn-clay`). adoption-cost ships both
   `.btn-clay{color:#fff}` and, 69 lines later, `.adopt-main a.btn-clay{color:#fff}` — the prescribed
   fix, already applied. The check now looks for it.
3. **Selectors quoted inside CSS comments** (1 duplicate). adoption-cost's comment documenting its own
   past fix contains the literal text `.ship-c p{color:#5b524a}`. This is the same trap that produced
   6 false icon-baseline WARNs on 2026-07-26; both new checks now strip `/* … */` first.

## Seam-parity census, 2026-07-29 (`scripts/seam_parity.py`)

House idiom is one `seam` / `cag-seam` divider before every section, with exactly one
seamless hero allowed. Sitewide: **29 FAIL / 50 pages that use the idiom** (58 pages
are `N/A` — they ship no seams at all, so they are not using the convention).

**The 8-page for-sale cluster is 100% clean.** The failures cluster in three places:

| Group | Pages | Shape |
|---|---|---|
| `/available/` bird pages | amie · bery · elad · evie · jins-jeni · roys (6) + the hub | **24 sections / 6 seams — 17 missing each.** The heaviest gap on the site by far, and uniform across all six, so it is one template decision, not six oversights. |
| Comparison cluster | vs-macaw 28/22 · vs-cockatoo 26/20 · vs-amazon 27/21 · breeders-comparison 24/19 · pros-and-cons 23/18 · comparison hub 23/19 · congo-vs-timneh 22/17 | 3–5 missing each. Consistent, so likely the same authoring habit rather than damage. |
| Interior / care | care-guide 12/7 · diet 12/7 · parrot-guide 13/8 · captive-bred 12/7 · cites-docs 10/6 · health-guarantee 10/6 · lifespan 11/8 · best-food 10/7 · adoption 11/9 · care 7/5 · reviews 8/6 · how-to-tame 9/6 · trusted-breeders 10/7 · blog 8/5 | 1–4 missing each |
| Homepage | `index.astro` 20/6 — **13 missing** | Note the homepage keeps its own structural dividers scoped to `.home-d`, so verify visually before treating this as a defect. |

**Two bugs were fixed in the probe before this census was trusted**, per
`skills/cag-gate-integrity.md`:
1. It counted only the token `seam` and missed `cag-seam`, the shared component used
   **913** times sitewide against `seam`'s 291 — that alone reported **83 of 108**
   pages as FAIL.
2. Zero seams was scored FAIL. One-seam-per-section is a for-sale / comparison
   convention, not a sitewide law, so a page that never uses the idiom is not
   violating it. Those are now `N/A`, which took 71 FAIL down to 29.

Judgement before anyone sweeps this: the `/available/` template and the homepage are
worth a decision; the 1–4-missing interior pages are low value.

### Timneh's 14: three complete components, built and never wired (triaged 2026-07-30)

Unlike the eggs page, **nothing on timneh is superseded** — `class="(chk|care|pb|price)*"` matches
**zero** rendered markup, so these are genuinely MISSING components, not dead variants.

| Component | Classes | What the CSS builds | Decision needed |
|---|---|---|---|
| **`.priceband`** | `priceband pb-scale pb-bar pb-zone pb-note` (+ `.red/.green/.amber` zone modifiers) | A horizontal price-honesty scale: three coloured zones (red = below our floor / amber / green = documented range) with a tabular-numeral scale above and a note below. Reads as the strongest anti-scam visual in the cluster. | Render — but it needs one new H3 and a `<figure>`-class caption |
| **`.carecards`** | `carecards cc cc-k cc-s` | A 4-up card grid: uppercase clay eyebrow, Newsreader value, small sub-label. Generic enough to carry weaning/diet/lifespan/noise facts. | Render, or delete if the page's `otA` GEO tables already cover it |
| **`.chkT`** | `chkT chkT-eyebrow chkT-grid chkT-head chkT-title` | A titled checklist block with an eyebrow and a grid of items. `chkB` is the adoption-cost sibling that ships. | Render — the timneh tuple has no checklist, and its siblings do |

**Heading impact — this is why it is not a mechanical fix.** Rendering `priceband` and `chkT` adds at
least two new headings to a page that currently passes the Heading Outline Gate at 18 sections / 18 seams.
Per CLAUDE.md the **full H1→H6 outline must be re-approved before the markup is written**, and each new
section needs its own seam to keep `seam_parity` at PASS.

---

## Site-wide heading/eyebrow type floor — 11px and 10px minima (found 2026-07-31)

Found while hardening `/congo-african-grey-parrot-pair-for-sale/`. A Playwright font-size
sweep at 375px counted **108 text nodes rendering under 12.5px on that one page**, bottoming
out at **10.6px**. The cause is not page CSS — it is the global clamp scale in `global.css`:

| Token | clamp | value at 375px |
|---|---|---|
| `--fs-h5` (applies to `h5` AND `h6`) | `clamp(0.6875rem, 1.1vw, 0.875rem)` | **11px** |
| `--fs-eyebrow` | `clamp(0.625rem, 1.2vw, 0.75rem)` | **10px** |

This sits directly against two binding statements: `PRODUCT.md` says the audience skews
older, and `DESIGN.md` §Accessibility says "contrast **and text size** matter more than
usual." Every page carrying the mandated ≥5 H5 and ≥5 H6 therefore ships at least ten
11px headings on mobile.

**Fixed page-scoped on the congo-pair page only** (floors raised to 12–14px, every desktop
maximum unchanged so the page still matches its siblings at 1280). **Not swept**, because
changing a locked token in the clamp scale moves all 108 pages and needs its own
verification pass with per-page screenshots.

**Explicitly out of scope of any sweep:** the desktop dial's `.tg` / `.tdial-k` at `.56rem`.
Those are locked cluster-wide by `cag-page-hardening` §1e-bis, and the dial is `display:none`
at every width where the complaint applies.

Reproduce on any page:

```js
// Playwright, 375px viewport. offsetParent filter is required — without it the
// hidden desktop dial is measured and the count is meaningless.
[...document.querySelectorAll('main *')].filter(e=>
  [...e.childNodes].some(c=>c.nodeType===3&&c.textContent.trim().length>1) &&
  e.offsetParent && parseFloat(getComputedStyle(e).fontSize) < 12
).length
```

## `no_aggregateoffer` warns on genuine group pages (found 2026-07-31)

`final_page_audit.py` warns `no_aggregateoffer` on `congo-african-grey-parrot-pair-for-sale`,
`grey-african-parrots-for-sale` and `male-african-gray-for-sale`. All three legitimately list
several priced birds, which is the one case `cag-for-sale-page-builder` §3.2 permits
(`AggregateOffer` ONLY on group/hub pages). Either encode the group-page exemption in the
auditor or move these pages to per-bird `Offer` — a cluster decision, not a page decision.
Left as a WARN, not silently suppressed.

## Render-harness baseline, 2026-08-01 (9 for-sale pages, 375/768/1280)

First full run of `npm run test:render:pages` at harness 2.0.0. Scorecards in
`data/quality/scorecards/*-2026-08-01.json`. **85 defect rows / 5,076 instances.**
A *row* is one failure mode of one check at one viewport and is comparable across
families; an *instance* is magnitude and is not.

| Family | Rows | Instances | Note |
|---|---:|---:|---|
| LAYOUT | 54 | 4,360 | the real backlog — see below |
| IMG | 27 | 116 | all from the overridden blocking check |
| NAV | 4 | 76 | was 337 rows; see the correction below |

### 1. `layout-min-font-size` — 3,916 instances, the largest real finding

Text rendering under 12.5px. Interrogated before being recorded, because a
suspiciously high count usually means a broken check: the flagged sizes are
genuinely small — 12px (most common), then 11.36px, 10.88px, 11.52px, 10px — on
`span`, `li`, `a`, `p`, `button`, `figcaption`. It is not a broken check.

Two things to know before acting on the number. It sums the same text node once per
viewport, so distinct nodes are roughly a third of it, ~145 per page. And **~11% of
hits are `12.48px`** — `0.78rem` at a 16px root, failing the 12.5 threshold by 0.02px.
That band is a rounding artifact, not a legibility defect; fix the 10–12px text and
leave `0.78rem` alone, or move the threshold to 12.4 and say so.

### 2. Oversized images — 33 files, currently overridden

`img-srcset-within-2x` (blocking) fires on all 9 pages: 33 distinct files decode at
more than 2x the width they paint at, measured in Playwright with
`deviceScaleFactor: 1`. Suppressed by a counted `RENDER_OVERRIDE`, which
`scripts/quality_report.py` prints on every run.

| Ratio | File | Where |
|---|---|---|
| 13.33x | `ida-brim-nashville-tn-review.webp` | 640px asset in a 48px review avatar |
| 9.23x | `stanley-perkin-oceanside-ca-african-gray-bird-review.webp` | 480px → 52px |
| 9.23x | `jesse-ovalle-baton-rouge-la-african-grey-purchase-review.webp` | 480px → 52px |
| 6.73x | `african-grey-parrot-eggs-nesting-clutch.webp` | 1408px → 209px |
| 6.25x | `archie-obrien-farmingdale-ny-review.webp` | 300px → 48px |
| 4.86x | six `*-card.webp` bird cards | 640px → 132px |

Fix: regenerate review avatars at 2x their painted size (96–128px wide, not 480–640),
and give the bird cards a `srcset` rather than one 640px master. About ten of the 33
sit between 2.0x and 2.5x — one retina asset for a slightly different painted box;
regenerate those last or not at all. Re-run without the override to confirm, then drop
the override from the run command.

### 3. `nav-jump-target-lands` — the 337 was mostly the harness, but not entirely

The 2026-07-31 baseline recorded 337 NAV rows across 8 pages and 0 on congo-pair, which
read as a cluster-wide `scroll-behavior:smooth` defect. **It was not.** The check reset
with a smooth-*animated* `scrollTo(0,0)` and clicked 80ms into that animation, so it was
measuring a fragment navigation fighting its own in-flight scroll — and congo-pair scored
0 only because its `scroll-behavior:auto` made that reset instant by accident. It was the
one page being measured correctly. **No site CSS change is needed; `global.css:104` stays.**

What survives is real and worth fixing: **`baby-african-grey-parrot-for-sale`, all 22
in-page links land at 114px against 158px of pinned chrome** — `scroll-margin-top` is
`calc(var(--hdr) + 18px)` = 114px, which clears the 96px header but not the 62px sticky
jump rail above it. Verified against `dist/`. Every heading lands behind the rail. Same
root cause on `dna-tested` and `hand-raised` (1 row each).

### 4. Benchmark corpus baseline — all 7 page types, 2026-08-01

Spec §3.2's frozen sample now exists: one page per page type, flagged `corpus: true` in
`tests/render/targets.json`, so the quality trend stops depending on which pages happened
to get built that month. Re-score with `npm run test:render:pages` (15 pages, ~12 min).

| Page type | Corpus page | Rows | Instances |
|---|---|---:|---:|
| bird | `available/roys` | 12 | 652 |
| comparison | `congo-vs-timneh-african-grey` | 11 | 529 |
| blog | `blog/african-grey-parrot-cage-setup` | 9 | 473 |
| for-sale | `congo-african-grey-parrot-pair-for-sale` | 9 | 324 |
| interior | `african-grey-parrot-care-guide` | 9 | 663 |
| location | `african-grey-parrot-for-sale-florida` | 9 | **59** |
| hub | `african-grey-parrots-for-sale` | 6 | **70** |

Across all 15 measured pages: **140 rows** — LAYOUT 90, IMG 42, NAV 8; instances LAYOUT
6,498, IMG 333, NAV 149.

Two things worth reading off this rather than assuming. **The hub and the Florida location
page are dramatically cleaner** (59–70 instances against 324–663 elsewhere), and the hub is
the only page in the corpus with no IMG row at all — so the checks discriminate between
page types rather than flagging everything uniformly. And **LAYOUT leads on every single
page type**, which makes `layout-min-font-size` the site-wide next action rather than a
for-sale-cluster quirk. Before acting on it, re-read item 1 above: ~11% of its hits are the
`12.48px` rounding band and are not real defects.

---

## 2026-08-01 — legibility sweep, NAV repairs, and three harness criticals

### Resolved

**`layout-min-font-size` — 6,498 instances to ZERO.** The surface was 684 declarations
across 64 files, not the 129 a first grep suggested: the codebase writes `.78rem`, not
`0.78rem`, so a pattern requiring the leading zero undercounted it 5x. But the *dominant*
source was not CSS at all — **Tailwind's `text-xs` (0.75rem = 12px), used 746 times across
76 files.** Raising `--fs-h5`/`--fs-eyebrow` in the `:root` scale first moved the measured
count by exactly zero, because almost nothing here is styled by element selector. Four
passes, each aimed by measurement: `--text-xs` -> 0.79rem in `@theme`; 291 arbitrary
`text-[10/11/12px]` utilities consolidated onto `text-xs`; 675 CSS declarations to
`var(--fs-micro)`; and 18 `clamp()` MINIMUMS the first three missed entirely
(`.cag-h6` was `clamp(.75rem,.95vw,.82rem)`, pinned at 12px on mobile at any width).

**The 12.48px band was NOT a rounding artifact.** The previous note here advised leaving
`.78rem` alone. It is 88 declarations — the most-used small size in the codebase — so
exempting it would have retired the check's largest cohort permanently. Threshold stayed
at 12.5; the codebase moved to `--fs-micro: 0.79rem`. Reasoning lives beside the threshold.

**The 7px dial labels were never geometry-bound.** Measured before deciding: the ring is
64x64 and the label is five characters, painting 33x21 at `--fs-micro`. No override needed.

**NAV.** `roys` had no `scroll-margin-top` at all (51 links landing at 0px); `baby` and
`congo-vs-timneh` reveal a rail at their mobile breakpoint without raising the 114px base
margin. Fixed. **`dna-tested` and `hand-raised` were FALSE POSITIVES** and needed no edit.

**Freshness deletion-blindness — CLOSED**, and not with directory mtimes (that trade was
rejected for a reason). `builtRoutesWithoutSource()` diffs built routes against source
pages, naming the exact orphaned route. Measured first: 108 source routes, 108 built.

### The corpus baseline

| Family | Rows before | Rows after | Instances before | Instances after |
|---|---:|---:|---:|---:|
| LAYOUT | 90 | 45 | 6,498 | 698 |
| IMG | 42 | 42 | 333 | 333 (overridden) |
| NAV | 8 | 3 | 149 | 13 |
| **Total** | **140** | **90** | **6,980** | **1,044** |

### Three harness criticals found by the whole-implementation review

1. **`measureTopChrome` was order-dependent.** `scrollBy` from wherever the previous check
   left the page, sampling only 1.5 viewports — not deep enough for rails sitting
   1300-2000px down. The same page measured 96px fresh and 147-158px pre-scrolled.
2. **The repair for (1) then over-absorbed.** Taking the MAXIMUM across depths pulled
   sticky *page content* into the band (`aside.availB-rail` 287px, `div.dial-card` 672px),
   reported "chrome measures 784px", tripped the implausible guard, and left NAV
   examining **zero** units on 6 of 45 page-viewports — worse than the bug it replaced.
   Fixed by requiring an absorbed element to span >=80% of `innerWidth`.
3. **`layout-tap-target-size` flags WCAG's own exemptions.** All 45 LAYOUT rows named the
   MANDATED 1x1 skip link, plus inline prose links that SC 2.5.8 exempts explicitly. The
   report's "worst family / next action" line was pointing at a check defect.

Also: a **third** truncation-derived `count` (`skipped.slice(0,10).length`) in the very
check whose comment claimed there were none left.

### STILL OPEN

**Images — 21 files over 2.0x; the override stands.** 17 constant-painted-size assets were
regenerated (164 KB saved; `ida-brim` was a 640px file in a 40px avatar slot). The rest
need `srcset`, and **a first attempt at that was reverted** — worth reading before retrying:

- Applying one blanket `sizes="(max-width:640px) 45vw, 356px"` to every image conflated
  two roles. Gallery cells really are ~45vw; the full-width feature images paint at
  **343px** at 375. The browser duly loaded a **168px file into a 343px box** — visibly
  blurry. Shipping blur to satisfy a byte metric is a bad trade.
- **`sizes` must be measured per image role, not guessed.** Feature images on `roys`:
  343px @375, 736px @768, 768px @1280 -> `(max-width:640px) 92vw, 768px`.
- The correct variant width is **2x the painted box** (680w for a 341px box = exactly
  2.00x, which passes). A 720w variant misses at 2.11x.
- A patch guard that scans the following 200 chars for `srcset=` will see a NEIGHBOURING
  image's srcset and silently skip the tag it was meant to patch. Patch by tag, not by
  proximity.
- Several images appear more than once per page at different painted sizes; a
  `replace(..., 1)` fixes only the first.

**Follow-ups recorded, not fixed:** the chrome band is still measured once globally and
applied to every landing rather than re-measured per landing; check ORDER is load-bearing
and unpinned (`settlePage` mutates the DOM at check #4, so LAYOUT measures an unsettled
document); scorecard filenames carry no run label, so a same-day recheck overwrites the
first-run card; `harness_version` is written and never read.


---

## 2026-08-02 — the srcset work, measured instead of guessed

**The override is narrowed, not cleared, and the reason changed because the measurement
changed.** It previously read "33+ assets decode above 2x their painted width" — a
filename count, which implied the fix was "regenerate 33 masters". It is not.

`scripts/image_srcset_plan.mjs` measured every `<img>` on all 15 target pages, **per
occurrence**, across a sweep that straddles every Tailwind breakpoint
(375 / 414 / 480 / **639 / 640** / **767 / 768** / 900 / **1023 / 1024** / 1280 / 1440).

| | count |
|---|---:|
| image occurrences over 2.0x | **290** |
| of those, CONSTANT painted width (regen the master, no markup change) | **3** |
| of those, FLUID painted width (need per-role `srcset` + measured `sizes`) | **287** |

The three constant ones are `/emoji/cag-congo-64.webp`, `/emoji/cag-timneh-64.webp`
(60px master, painted 14–30px depending on the component) and
`ida-brim-nashville-tn-review.webp` (96 → 40). Even these are **not** a simple downscale:
the emoji paints at 30px inside `Footer.astro` and 14px inside `NewsletterV2.astro`, so
shrinking the master to satisfy a DPR-1 metric would soften it on every retina screen.
They want an `x`-descriptor `srcset`, not a smaller file. Shipping blur to satisfy a byte
metric is the trade that got the last attempt reverted.

### Why straddling the breakpoints is load-bearing

Painted width is **not monotonic** across a breakpoint. A gallery cell on
`/available/roys/` paints **608px at 640** and **260px at 768** — the grid goes 1-col →
2-col → 3-col. A sweep that samples 640 and 768 but not 639 and 767 cannot tell a fluid
band from a fixed one, and a `sizes` interpolated between those two points is wrong
across the entire 640–767 range.

### The shape the tool derives (verified against its own numbers before any file is cut)

| Role | measured sweep | derived `sizes` | variants | worst after |
|---|---|---|---|---|
| full-bleed feature | 343 → 608 → 736 → 768 | `(max-width:767px) 92vw, 768px` | +440 | 1.28x |
| gallery / sidebar cell | 343 → 608 → 260 → 354 | `(max-width:639px) 46vw, (max-width:1023px) 32vw, 354px` | +200, +380 | 1.78x |
| 3-col card grid | 341 → 605 → 358 → 354 | `(max-width:639px) 95vw, (max-width:1023px) 48vw, 354px` | +360, +620 | 1.73x |

Two variants per image, every band under the 2.0x cap with margin.

### What was actually done on 2026-08-02

- The tool exists, is committed, and prints `*** PLAN DOES NOT CLEAR THE CAP ***` on any
  occurrence its own plan fails to fix — so a bad plan cannot be applied silently.
- `/african-grey-parrot-for-sale-florida/` had **two broken images**: `<img>` tags still
  pointing at `https://congoafricangreys.com/wp-content/uploads/…`, a path that now 301s
  to the homepage and serves HTML. The render harness reported them as "failed to decode
  and could not be measured" — the row that exists for exactly this. Replaced with local
  WebP at measured sizes.
- **NOT done: the 287 fluid occurrences.** Generating variants is scriptable; patching
  `sizes` per occurrence is not, because several of these images are rendered from data
  arrays inside shared components, so the patch has to land on the component and the
  occurrence-to-source mapping has to be established per component. That is the next
  session's work, and it is the whole of it.

### Traps banked from the reverted attempt — re-read before retrying

- **One blanket `sizes` for every image is the bug**, not a shortcut. Per-role only.
- The correct variant width is **2x the painted box**. A 680w for a 341px box is exactly
  2.00x and passes; 720w misses at 2.11x.
- A patch guard that scans the following 200 characters for `srcset=` sees a
  **neighbouring** image's srcset and silently skips the tag it meant to patch. Patch by
  tag, not by proximity.
- Several images appear more than once per page at different painted sizes; a
  `replace(..., 1)` fixes only the first, and the two occurrences want different `sizes`.

---

## 2026-08-02 (second session) — a BLOCKING check was failing clean pages at random

### `nav-jump-target-lands` was nondeterministic — two distinct bugs, zero page edits

Re-running the gate on the SAME commit against the SAME `dist/` failed three times on
three different page/viewport pairs, one link out of eighteen each time:

| run | failed | reported |
|---|---|---|
| 1 | `african-grey-parrot-adoption-cost` @375 | `#reserve@26059px` — the target's raw document offset |
| 2 | `timneh` @375 · `hand-raised` @768 | "STILL MOVING when it expired" |

Same input, different verdict, on a check with `severity: blocking`. Charged to the
harness; **no page was edited for any of it.**

**Bug 1 — a scroll that has NOT STARTED is indistinguishable from one that has FINISHED.**
`waitForScrollSettle` counted five unchanged `scrollY` ticks (5 × 32ms = 160ms) as
settled. `el.click()` requests a smooth scroll whose first animation frame can land later
than that on a 36,359px document under main-thread load, so the probe returned
`settled: true` at the PRE-CLICK position and the check recorded the target as missed at
its raw document offset — 26,059px, i.e. the page had never moved. `lastDeltaPx` stays 0
in that case, so the check's own moving-vs-stuck partition could not tell either.
Fixed with a 400ms start grace that applies ONLY while the position is unchanged, so the
common path costs nothing. Pinned by `fixtures/known_broken/scroll-late-start.html` and
two meta tests; **verified to FAIL with the grace disabled** before being kept.

**Bug 2 — the gate failed on a verdict the check itself calls not-a-page-defect.** With
bug 1 fixed the false landing became an honest "never stopped scrolling", whose message
reads *"PROBABLY A BUDGET DEFECT, NOT A PAGE DEFECT; raise maxMs before touching the
page"*. Failing a blocking gate on that is incoherent. A target still in flight at the
base budget now simply keeps waiting (`SETTLE_EXTENSION_MS` 5000, cap 4 per
page-viewport), so only a target still unsettled AFTER the extension is reported — which
turns "probably the budget" into "definitely not". Bounded deliberately: an unbounded
extension would trade false failures for a page that writes no partial, and a page with
no partial scores ABSENT, the worst failure mode this harness has.

**Reading worth keeping:** the tell here was NOT a suspiciously high count — it was the
same input producing different verdicts. A gate whose result changes between runs is
broken even when every individual number looks plausible.

### `npm run test:render:pages` cannot pass as written

`RENDER_OVERRIDE` is read from the environment by `pages.spec.ts` and the npm script never
sets it, so the bare command fails all 28 `img-srcset-within-2x` page-viewports. The
recorded "45 passed" baseline was produced with the variable set at the shell, and nothing
in the repo records that — this session could not reproduce the baseline from the repo
alone until the string was recovered from a scorecard. Until the srcset work lands, the
reproducing command is:

```bash
export RENDER_OVERRIDE="img-srcset-within-2x:$(python3 -c "import json;print(json.load(open('data/quality/scorecards/congo-african-grey-for-sale-2026-08-02.json'))['overrides'][0]['reason'])")" && npm run test:render:pages
```

Note also that a same-day re-run OVERWRITES that day's scorecards, so a run without the
override erases the override record from the cards — which then reads as "0 open
overrides" in `quality_report.py`. That is the already-recorded "scorecard filenames carry
no run label" follow-up, now with a second consequence attached.

### Scorecards now carry `examined_by_check`

`build_scorecard.mjs` kept only `{pages, checks}` — how MANY checks ran, not how much each
examined. Guard 2 proves a check examined something SOMEWHERE across the corpus, so a
check examining 500 units on one page and 0 on the other 14 passes it. That is not enough
to promote a check on the strength of "it reported zero rows", which is the exact failure
this harness was built after. The per-check number is now in every card, so the question
is answerable after the run instead of needing a 13-minute re-run.

### Promotions: 4 of 12, on measured evidence

`sem-heading-order`, `schema-date-modified-present`, `schema-no-visible-date` and
`schema-sold-not-instock` are now `blocking`. The bar applied is the one that made the
LAYOUT/NAV promotion safe — **zero rows across all 15 corpus pages AND a non-zero
examined count** — not zero rows alone.

| promoted | rows | examined | note |
|---|---:|---|---|
| `sem-heading-order` | 0 | 2,993 headings, 15/15 pages | same denominator its two firing siblings use |
| `schema-date-modified-present` | 0 | 162 JSON-LD blocks, 15/15 | unconditional |
| `schema-no-visible-date` | 0 | 45 = 1 page-text unit per page-viewport | coarse unit, present everywhere |
| `schema-sold-not-instock` | 0 | 24 over 8/15 pages, **0 on the other 7** | vacuous by design — see below |

`schema-sold-not-instock`'s zero on 7 pages is nothing-to-check, not a check that
no-opped: its own scope note restricts it to pages declaring exactly ONE standalone
offered Product, because a rendered "Sold" badge cannot be attributed to a particular
Offer on a multi-listing page. Promoted anyway — the defect it catches is a bird shown
Sold whose Offer still says InStock, a commercial error rather than a cosmetic one — with
the vacuity written at the flag so nobody later reads its zero as corpus-wide proof.

**The other 8 stay advisory, each with its reason now recorded in
`data/quality/rule-index.json` (`severity` + `why_advisory`)** — that field did not exist
before, so Task 0b's requirement to record "any check deliberately left advisory with the
reason in the rule row" was unmet. `severity` is parsed from the check sources by the
updating script rather than hand-maintained, so it cannot drift from the code.
Promoting any of the 8 today would red the gate on every page and force exactly the
blanket override Task 0b removed: `css-class-resolves` 45 rows, `css-no-dead-component-rule`
33, `dup-no-sibling-crossover` 24 (whose whitelist has a KNOWN gap against mandated text),
`sem-section-opening-paragraph` 21, `sem-title-case-headings` 18 (the ~1,099-heading
backlog), `css-component-color-not-overridden` 12, `sem-all-six-levels` 6,
`schema-single-product-offer` 3.

### Task 3 — 0 of 8 retirements were safe, and the plan's table needs a third column

Six candidates fail the plan's own precondition ("only after the replacements are
blocking"):

| static check | replacement | replacement severity | verdict |
|---|---|---|---|
| `img-no-srcset`, `hero-preload-srcset-drift` | `img-srcset-within-2x` | blocking but **overridden on all 15** | retiring these drops srcset enforcement to zero |
| `header-not-title-case` | `sem-title-case-headings` | advisory | precondition unmet |
| `markup-css-drift` | `css-class-resolves` | advisory | precondition unmet |
| `markup-css-orphan` | `css-no-dead-component-rule` | advisory | precondition unmet |
| `component-color-loses-to-descendant` | `css-component-color-not-overridden` | advisory | precondition unmet |
| `tap-target-spacing` | `layout-tap-target-size` | blocking, 0 rows | precondition MET — but see below |
| `smooth-scroll-breaks-anchors` | `nav-jump-target-lands` | blocking, 0 rows | precondition MET — but see below |

**The two that pass the precondition still should not be retired, for a reason the plan
does not model: the two tools do not cover the same pages.** `page_hardening_scan.py`
defaults to every `dist/**/index.html` — **108 pages**. The render harness runs
`tests/render/targets.json` — **15**. Retiring a static check therefore trades enforcement
on 108 pages for enforcement on 15, leaving 93 pages with no coverage of that invariant at
all. Sampled to confirm rather than argued from structure: scanning three comparison pages
that are NOT harness targets (`african-grey-vs-macaw`, `-vs-cockatoo`,
`african-grey-parrot-pros-and-cons`) returns **29 ERROR · 30 WARN**.

And `smooth-scroll-breaks-anchors` is superseded by `nav-jump-target-lands` — the check
found flaky in this very session. Retiring a static backstop in favour of a check whose
race was fixed hours earlier is not a trade worth making yet.

**Recommendation (one, with its trade-off).** Retire nothing until either the harness
covers the pages the static scan covers, or each retirement is scoped to the 15 target
pages only. **The trade-off of waiting is real**: the eight static checks keep producing
the false positives already documented above (`tap-target-spacing` produced 7 false ERRORs
on 2026-07-26, `icon-text-baseline-drift` 6), so the duplication has a running cost in
wasted triage. That cost is smaller than silently dropping an invariant on 93 pages.

---

## 2026-08-02 (third session) — the srcset override is CLEARED

`npm run test:render:pages` now reports **45 passed with no `RENDER_OVERRIDE` at all**, and
`quality_report.py` §4 prints `OPEN OVERRIDES (0 distinct, suppressing on 0 page-runs)`.
That is Task 0a's written acceptance, met for the first time since the harness was built.

Start of session: **28 of 45 page-viewports failed** the blocking `img-srcset-within-2x`
without the override.

### The pipeline, and why each stage exists

| Script | Does | Exists because |
|---|---|---|
| `image_srcset_instrument.mjs` | stamps every source `<img>` with `file@offset`, builds, then unstamps | occurrence -> source-tag was the whole difficulty; see below |
| `image_srcset_plan.mjs` | measures painted width per occurrence across a breakpoint-straddling sweep | `sizes` is a promise about geometry and can only be measured |
| `image_srcset_map.mjs` | groups occurrences by TAG and derives one `sizes` per tag | you cannot patch an occurrence, only a tag |
| `image_srcset_variants.py` | cuts the WebP variants | |
| `image_srcset_apply.mjs` | writes `srcset`+`sizes` by byte offset, back-to-front | patch by tag, never by proximity |
| `image_srcset_fill_missing.py` | generates any candidate the built site references but does not ship | a missing candidate is a BROKEN IMAGE |
| `image_srcset_verify.mjs` | measures oversized AND undersized from real file widths | the gate cannot see blur |
| `build_image_manifest.py` + `src/lib/srcset.ts` | lets a component compute a truthful descriptor from the actual file | a component cannot hardcode a width for an image passed as a prop |

### Five defects found in the tooling, each of which would have shipped a wrong page

1. **The measuring tool's own ratio was fabricated.** `image_srcset_plan.mjs` took
   `Math.max` of `naturalWidth` across the sweep and divided it by the MINIMUM painted
   width — pairing the file loaded at 1440 with the box painted at 375, a ratio no viewport
   experiences. Harmless while `natural` was constant; the dominant error the moment srcset
   started working. After 212 tags were patched it still reported 274 occurrences over the
   cap. Fixed to measure per viewport: **292 -> 32**. The patches had been working the whole
   time and the tool was hiding it.
2. **229 of 273 `w` descriptors would have been wrong.** `natural` is `naturalWidth`, the
   width of the candidate the browser CHOSE, not the file named in `src` — off by as much
   as 1408 vs 900. Descriptors are now read from disk. A `w` descriptor is a factual claim;
   get it wrong and the browser's whole selection is computed from a lie.
3. **`naturalWidth` is DENSITY-CORRECTED on a `w`-descriptor image.** A 620px file reported
   318, 485 and 398 at three viewports — each exactly the `sizes` value there. So
   `img-srcset-within-2x`, which divides `naturalWidth` by painted width, measures whether
   `sizes` matches the box, NOT whether the file is oversized. Worth knowing before anyone
   reads that check's number as bytes.
4. **Patching a shared component blast-radiuses to 108 pages.** `NewsletterV2` and
   `BirdCard` take their image as a prop; the first patch hardcoded `${img} 640w` for
   masters including a 375px file and asked for a `-390` variant of it that cannot exist —
   15 candidates referenced but absent, i.e. broken images, on pages never measured. Both
   now compute from `src/data/image-widths.json` and emit only candidates that exist.
5. **Inference could not do the occurrence -> tag mapping.** Const resolution, template
   wildcards, an import graph and class matching still left **141 of 292 ambiguous**.
   Stamping the tag at build time and reading it back resolved **292 of 292, zero
   ambiguous**. The round trip leaves `src/` byte-identical.

### What remains, stated rather than rounded off

Oversized renders on a 3-page sample fell **293 -> 134** (67 -> 39 distinct files) measured
against REAL file widths. Undersized (a file smaller than its box, i.e. blur) went **75 ->
81 renders**, worst case **0.84x** — a 620px file in a 735px box. For scale, the attempt
that was reverted in August shipped **0.49x**, a 168px file in a 343px box.

The cause of the residual is a feedback loop the pipeline does not yet close: several of
these images are sized by their own intrinsic width, so changing the served candidate
changes the painted box, which invalidates the `sizes` that was derived from the previous
geometry. **The fix is to iterate `plan -> map -> apply` until painted width stops moving**,
which is mechanical with the scripts above and was not run to convergence here. Several of
the 81 are also pre-existing masters that were always smaller than their boxes
(`african-grey-parrot-breeder-midland-tx-hero.webp` is 800px in an 868px box and has no
srcset at all).

**Nothing in the harness measures the blur direction** — `img-srcset-within-2x` only has an
upper bound. `image_srcset_verify.mjs` is the only thing that will catch it, so run it after
any future srcset change. A run that clears the cap by shipping blur has made the page worse
while making the metric better.

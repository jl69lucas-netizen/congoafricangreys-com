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

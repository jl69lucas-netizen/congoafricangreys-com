# Session Brief — 2026-07-26

**Mode:** plan execution (no `grill-me` — started from the committed plan)
**Plan:** `docs/superpowers/plans/2026-07-26-for-sale-cluster-impeccable-pass.md`
**Scope:** impeccable UI/UX + perf pass over the 6 built for-sale pages
**Branch:** `main` throughout · 25 commits · all pushed (`9e833f0`)

---

## What Was Done

**Verification first.** Rebuilt and re-ran every gate rather than trusting the plan's checkboxes, then
rewrote the plan's status ledger to match reality. Three phases turned out to be misreported: Phase 0
shipped 8 checks but two were substitutions, Phase 1.1 stopped at dropping the dead fonts without
self-hosting, and Phase 1.2 kept the opposite analytics survivor from the one chosen and skipped both of
its verification steps.

**Design fixes.** 10 missing section seams on health-guarantee (7 across 17 sections; siblings run one
before every section). FAQ answer measure capped at 70ch on congo, eggs, dna-tested and health-guarantee —
they carried an explicit `max-width:none` and ran 102–107ch.

**Two sitewide footer bugs**, both causing horizontal document scroll on all 108 pages: the bottom bar
switching to a row at `md` when it needs ~808px, and `info@congoafricangreys.com` as an unshrinkable flex
item in a 160px column.

**Phase 5 — cross-sell.** 11 fresh FAQ entries (one eggs question + one pair question per page, each from
that page's own angle) and a new `.xsell` strip carrying 15 links, every anchor unique per target and at
the start of its sentence.

**Phase 6 — remaining 3 pages.** 23 `img-no-srcset` findings closed: 11 in-body images given the ladder,
and 12 read-card thumbnails that were fetching a 760px file into a 148px box. 13 new `-440` and 12 new
`-320` variants.

**Four gate repairs.** `tap-target-spacing` (7 false ERRORs), `icon-text-baseline-drift` (6 false WARNs),
the §2y line-length probe (miscalibrated `ch`), and `dup_content_audit.py` (23 legitimate furniture
matches). Each fixed with regression tests — 47 passing.

**Phase 7 ending state, all 6 pages:** hardening scan **0 ERROR · 0 WARN** (first fully clean run) ·
final_page_audit 6/6 PASS-WITH-WARNINGS · dup gate body **PASS** · headers **PASS** · health-sweep
**ALL CRITICAL CHECKS PASSED** · sitemaps 109 URLs / 0 phantoms · Lighthouse mobile a11y/BP/SEO
**100/100/100**.

---

## What's Next

1. **Phase 1.1 — self-host the fonts** (breeder deferred this to the full-site pass, so it runs with that).
   `public/fonts/` is empty and `BaseLayout.astro` still preconnects `fonts.googleapis.com`, so the
   HTML → Google CSS → woff2 discovery chain is live on all 109 URLs. This is the real LCP lever and the
   leading suspect for the dna-tested CLS race — re-measure that page (≥5 runs) immediately after it lands.
2. **Phase 1.2 — prove analytics still works.** The survivor tag was inverted versus the plan and neither
   verification step was run. Confirm `generate_lead` still reaches GA4 realtime from `/contact-us/`, and
   trace whether `/70de/` (still HTTP 200) is being injected alongside the direct tag. A silent analytics
   break is worse than a slow page.
3. **Next for-sale group** — read
   `docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md` first (§1 verify-the-gate,
   §8 command sequence), then `/cag-for-sale-page-builder`.

## Unfinished

- Nothing from this session's scope. Phases 0–3 and 5–7 are complete; Phase 4 resolved as a non-issue
  (the body copy was already at 70ch — the "84ch" reading was a miscalibrated probe); Phase 1.1 deferred
  by the breeder.

## Discovered This Session

- **Four separate checkers reported defects that did not exist.** Fixing the pages would have been wasted
  work and would have degraded correct code — a decorative badge padded to 24px, six healthy pages
  reflowed. Verifying a finding before editing a page is now pass gate 7 in the for-sale builder skill.
- **CLS on this site is bimodal** (~0.44 or ~0.001 on a race). Single Lighthouse runs produced a confident
  wrong attribution that survived three rounds of bisection. Perf conclusions now need ≥5 runs and the
  distribution, not the median.
- **`/dna-tested-african-grey-for-sale/` fails CLS at ~0.44 on 4-in-5 cold mobile loads.** Pre-existing
  (identical distribution on the pre-session build), page-specific, shifting node is the hero copy block.
  Not root-caused; four hypotheses ruled out by measurement. Recorded in
  `docs/reference/technical-seo-fixes-backlog.md`.
- **Sitewide body duplication** — ~5,857 crossovers across the ~100 location pages, untouched and out of
  scope here. Its own piece of work.
- The dup gate previously failed on every for-sale page because of mandated-identical furniture, which
  trains everyone to ignore it. Now meaningful, and proven not blinded by an injection test.

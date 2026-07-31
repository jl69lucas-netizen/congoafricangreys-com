# Congo Pair — Harden & Polish: Lessons for the Rest of Cluster 3

**Date:** 2026-07-31 · **Page:** `/congo-african-grey-parrot-pair-for-sale/`
**Plan:** `docs/superpowers/plans/2026-07-31-congo-pair-harden-polish.md`
**Read before:** `affordable-african-grey-birds-for-sale`, `grey-african-parrots-for-sale`,
`male-african-gray-for-sale`, `african-grey-parrots-for-sale-near-me`,
`african-grey-breeding-pair-for-sale` — all five currently FAIL `final_page_audit.py`.

---

## 1. The headline: a clean static scan on a page with thirteen real defects

`page_hardening_scan.py` returned `0 ERROR · 0 WARN` over **1 source file, 1 built page**,
and `seam_parity.py` returned `PASS 24/23`. Both were honest. Both were useless on their
own — **every defect the breeder reported was invisible to the static half**, and only the
Playwright half found them:

| Found by | Defects |
|---|---|
| Static scan | 0 |
| Runtime probes | jump links dead · `--hdr` wrong · 108 sub-12.5px nodes · card overflow · geo-card grid collapse · receipt band truncation · 2.13× hero srcset waste |
| Reading the source against the asset folder | 12 unrendered infographics · 4 orphaned images · unplaced video |
| Proofreading the images | 1 misspelling |

**Run all three passes. The scan is a floor, never a verdict.**

## 2. `scroll-behavior:smooth` is the jump-rail killer, and the page length is why

The rule was already banked (`reference_smooth_scroll_kills_jump_links`) but the *mechanism*
had not been written down, so it kept being treated as a stylistic preference:

> The page is **31,000px tall**. A rail chip near the top targeting §protocol asks the
> browser to smooth-scroll ~9,000px. That takes seconds, and **any touch cancels it**.
> Measured: click a chip, wait 1.2s, `window.scrollY` is still **25**.

On a short page smooth scrolling is harmless, which is why it survives review. On a
for-sale page it is a broken feature. `cag-for-sale-page-builder` §5 already requires
`scroll-behavior:auto`; enforce it.

**Scope it, do not go global:**
```css
:global(html:has(.cpair)) { scroll-behavior:auto; }
```
Astro scopes `<style>`, so `:global()` is required to reach `html`, and `:has()` keeps every
sibling page's smooth scrolling intact.

**Verify by clicking every chip, not by reading the CSS.** The pass condition is
`heading.top` landing between `header + rail` and `+60px`. All 11 chips now land at 193px
against 151px of chrome.

## 3. `--hdr` must be declared, not defaulted

Five `var(--hdr, 72px)` fallbacks on this page. The header measures **96px**. Nobody had
ever measured it, so the sticky rail parked 24px behind the header and anchors were offset
by 92px when they needed 162px.

```css
.cpair { --hdr:96px; --rail-h:52px; }
.cpair-main section { scroll-margin-top:calc(var(--hdr) + 16px); }
@media (max-width:1024px){
  .cpair-main section { scroll-margin-top:calc(var(--hdr) + var(--rail-h) + 14px); }
}
```

**Grep the next page for `var(--hdr, 72px)` before anything else.**

## 4. Two of my own probes lied — both corrected rather than obeyed

Per `skills/cag-gate-integrity.md`, a gate you write is a gate that lies. Two more for the tally:

1. **The overflow probe flagged the breadcrumb.** `.bc-pill` measured 424px wide in a 375px
   viewport. It is *supposed* to: `.bc-pill-wrap` is a deliberate `overflow-x:auto` scroller
   with a trailing fade mask, added specifically so long trails swipe instead of clipping.
   The probe's scroller exclusion list was missing it. **I had already written a `flex-wrap`
   "fix" and reverted it.** Exclusion list must be
   `.railA, .availB-rail, .tF-wrap, .tA-wrap, .bc-pill-wrap`.
2. **The anchor-collision check stripped `↗` (U+2197) but not `→` (U+2192).** It reported
   `collisions: 0` on a page carrying a real one — the breeding-pair card's `See the Pair →`
   against the spent ledger anchor *see the pair*. Normalise **both** arrows.

> A check that reports 0 is not automatically good news. Read its examined count *and*
> reason about what it cannot see. 159 anchors examined, 1 collision, found only after the
> normaliser was fixed.

## 5. The strip-comments trap, third recurrence — now fixed in the scanner

`check_smooth_scroll` reported a WARN for `scroll-behavior:smooth` that existed **only inside
a CSS comment explaining why the page sets `auto`**. `_strip_css_comments()` already existed
in `page_hardening_scan.py` (offset-preserving, written for exactly this) and this check
simply never called it. Now it does, with two regression tests:

- prose quoting a declaration is not a defect
- a real declaration beside such a comment **still** warns (the fix is not blinding)

**Audit the other checks for the same omission before the next page.**

## 6. Infographics: native ratio, and reserve the box

- `.sec-img.inf-img { object-fit:contain; aspect-ratio:auto; }` renders them uncropped —
  confirmed 760×425 drawn against 760×424 natural on all 11 landscape files.
- **But `aspect-ratio:auto` gives a ~0px box before load.** Twelve images × a 425px jump is
  a catastrophic CLS. Mirror the intrinsic dimensions into an explicit inline
  `style="aspect-ratio:1376/768"`.
- One asset came back **portrait (768×1376)**. It is not a generator error to fight; give it
  `.inf-tall { max-width:420px }` and let it be a tall diagram.
- New helper: `scripts/bake_infographics.py <src_dir> <dst_dir> <stem>...` — native ratio,
  quality-walk to <100 KB, `-760` sibling. It **never crops**; photos still go to
  `reframe_og.py`.

## 7. Proofread every generated image. One in twelve was wrong.

`pair-bond-three-risk-conditions.webp` shipped **"strongest humam bond"** — the same defect
class as the historical "BREDDER". Caught by rendering 2-up contact sheets and reading them.

**Patch, don't regenerate.** Re-rendering the line in a guessed font never matches. Copy the
correct glyph from elsewhere *on the same baseline* (the `n` from "bond" two words later),
paste over the wrong one, then shift the tail left to preserve the space width.

**Trap:** my first clear-rectangle used `y0=628` and amputated the descender of the `g` in
"strongest" on the line above. Column-profile the dark pixels to find the true band
(`638–665`) and stay inside it.

## 8. `thumbnail()` only ever shrinks — small masters floated as postage stamps

`reframe_og.py`'s blurfill used `fg.thumbnail(...)`, which is a no-op when the source is
smaller than the target. A 310×400 master inside a 1408×768 canvas rendered as a stamp in a
sea of blur. Added opt-in `--fgup`.

**Proof the widening did not move any sibling page:** re-baked one image on the default path
and `cmp`'d it against the pre-patch output — byte-identical. Do this for every shared-script
change.

Framing decision worth reusing: **scene photos are not portraits.** A room with people and
several birds takes `--fgmaxw 960` + a mobile **5:4** frame; a single-bird portrait takes
`--mobcrop 4:5`. Same script, different call.

## 9. `sizes` lies are invisible to every static check

Both hero tiles declared `(max-width:980px) 92vw` and rendered at **161px**, because the
mobile hero is a 2-column grid. 2.13× waste. Corrected to `44vw`, and
`heroPreloadSizes` aligned so the preload scanner resolves the same candidate as the
renderer. Re-measured: **0 overweight across 30 images**.

## 10. Component fixes worth lifting wholesale

- **Bird card name/price:** `grid-template-columns:minmax(0,1fr) auto` with `nowrap` on the
  price, stacking to one column ≤640px. `justify-content:space-between` on a flex row let
  `$2,300 + $2,500` clip.
- **CTA:** `align-self:start; width:auto; white-space:nowrap` — and **shorten the label**
  rather than force `nowrap` on one that cannot fit. Four of six wrapped to two lines.
  `See the Breeding Pair →` became `See the Adults →` (which also cleared an anchor collision).
- **Geo cards:** use named `grid-template-areas:"k a" "n a"`. `grid-row:1/span 2` on the
  arrow alone lets auto-placement drop it into column 1 and crush the label to one word
  per line.
- **`.cpair p{max-width:70ch}` beats bare component classes on the max-width axis**, not just
  colour. The receipt's green band stopped at 443px inside an 880px card. §1l's lesson
  generalises: qualify component `<p>` rules for **every** property the page rule sets.
- **Seam:** `.seam-wrap` flex with two clay-gradient hairline pseudo-elements. A bare
  centred logo reads as decoration, not as a section boundary.

## 11. Anchors spent by this page

| Target | Anchor now spent |
|---|---|
| `/african-grey-breeding-pair-for-sale/` | Aviary stock valued on its breeding record · A proven producing duo for an established aviary · See the Adults |
| `/african-grey-parrot-bird-eggs-for-sale-usa/` | Candled Congo eggs for a working incubator |
| `/hand-raised-african-grey-parrot-for-sale/` | The Benjamin Home-Raising Protocol behind both birds |
| `/timneh-african-grey-for-sale/` | Our Timneh pair option · See the Timnehs |
| `/dna-tested-african-grey-for-sale/` | Our DNA-sexing process |
| `/african-greys-for-sale-with-health-guarantee/` | The written health guarantee behind every bird |
| `/african-grey-parrot-care-guide/` | Our full care routine · The care routine we hand every buyer |
| `/how-to-avoid-african-grey-parrot-scams/` | Our full scam-pattern breakdown |

## 12. Gate results, with examined counts

| Gate | Result | Examined |
|---|---|---|
| `page_hardening_scan.py` | clean | 1 source, 1 built page |
| `seam_parity.py` | PASS 24/23 missing=0 | 1 page |
| `dup_content_audit.py` | PASS | **9 pages** |
| `dup_content_audit.py --headers` | PASS | **9 pages** |
| anchor collisions | 0 | **159 anchors** |
| contrast sweep 375/768/1280 | 0 failures | all text nodes, `details` forced open |
| real-`ch` line length @768 | 0 over 75ch | all `main p` |
| srcset waste | 0 over 1.5× | **30 images** |
| `final_page_audit.py` | PASS-WITH-WARNINGS | 1 warning, sibling-wide |
| `pytest tests/` | 90 passed | — |
| `health-sweep.sh` | all critical pass | 108 pages |

## 13. Open / deferred

1. **The global `--fs-h5` clamp bottoms out at 11px on all 108 pages.** Raised page-scoped
   here; the condition is site-wide. Logged to the backlog, not swept — a global type change
   needs its own verification pass.
2. **`no_aggregateoffer` WARN** on `final_page_audit.py`. This page carries `AggregateOffer`
   because it genuinely lists 9 priced birds across 6 routes. `grey-african-parrots-for-sale`
   and `male-african-gray-for-sale` carry the same warning. Either the group-page exemption
   should be encoded in the auditor or these pages should move to per-bird `Offer` — a
   cluster decision, not a page decision.
3. **Five Cluster-3 siblings FAIL `final_page_audit.py`** on `all_six_levels`, `min_h5_5`,
   `min_h6_5`, `shipping_line`, `real_hero_image`. They are the next work.
4. **Self-hosted fonts** — still deferred from 2026-07-26, still the leading LCP lever.

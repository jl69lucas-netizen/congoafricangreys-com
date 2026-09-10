# Round-4 Tables — Critique / Harden / Refine (2026-09-10)

Probe: `node scripts/probe_artboards.mjs docs/design/homepage-tables-r4`
Scratch copies with the `support.js` line stripped, headless Chromium at each artboard's own
frame width (390 / 768 / 1440). **Examined count printed by the probe itself: 24 of 24.**

## Probe totals

| | Artboards | Overflow | Mobile font <14px | Mobile hit <44px | Contrast <AA |
|---|---|---|---|---|---|
| Before controller pass | 24 | 0 | 0 | 0 | 0 |
| After controller pass | 24 | 0 | 0 | 0 | 0 |

The controller pass changed content and tokens, not geometry compliance: it added a missing
eyebrow to six artboards and unified a dot alpha across twelve. Both were re-probed; all 24
remained clean.

## Measured heights (px, root element)

| Table | J Mobile | J Tablet | J Desktop | K Mobile | K Tablet | K Desktop |
|---|---|---|---|---|---|---|
| Congo vs Timneh | 2,313 | 1,323 | 1,418 | **1,974** | 1,183 | 1,280 |
| Male vs Female | 1,657 | 1,229 | 1,211 | **1,417** | 1,072 | 1,093 |
| Grey vs Others | 1,619 | 1,344 | 997 | **1,322** | 1,006 | 920 |
| Pricing | 1,484 | 1,413 | 845 | **1,333** | 1,056 | 961 |

K is shorter than J at Mobile on all four tables, by 151-339px. Against the round-1
benchmark, K's Congo-vs-Timneh mobile stack is **1,974px vs 3,398px — 1,424px shorter.**

## Findings

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| Price J+K | Critique (honesty) | The live pricing section carries an eyebrow, `Transparent Pricing`, that the controller's COPY.md lift omitted. The author correctly refused to invent one and flagged the gap instead of silently dropping content. | **Fixed.** Verified against `dist/index.html`, added to COPY.md, inserted above the H2 on all six Price artboards at the contract's eyebrow spec (12px desktop/tablet, 14px mobile for the floor), identical on J and K. Re-probed clean. | `Table-Price-*` |
| Others K, Price K | Refine | Two authors independently set the leader dots to `rgba(60,30,10,.32)` and `rgba(60,30,10,.3)` — the same intent, two values. | **Fixed.** Unified to `.3` across all twelve K artboards. | `Table-{Others,Price}-K-*` |
| All K | Refine | Three different leader-dot *implementations* survive: Cvt uses `repeating-linear-gradient` at the strict `.12` Line token; Mvf uses `border-bottom:2px dotted #5b524a` (Muted token); Others/Price use `border-bottom:2px dotted rgba(60,30,10,.3)`. All three render legibly (screenshot-verified) and each table appears alone in its own homepage section, so nothing is visibly inconsistent today. | **Open, deliberately deferred.** Unifying now means rewriting the leader mechanism on 12 verified artboards for a difference the breeder cannot see on the page. **If K is picked for more than one table, unify at apply-time** — Cvt's gradient at `.12` is the only fully on-token version and is the one to standardise on. | all `*-K-*` |
| Price K, Others K | Critique (brand) | `rgba(60,30,10,.3)` is not a literal token value — it is the Line token's exact ink at a heavier alpha, because `.12` is invisible as a 2px dotted rule on cream. | **Accepted as a deliberate deviation, recorded here so the breeder sees it rather than discovers it.** No new hue enters the palette. | `Table-{Others,Price}-K-*` |
| Mvf K | Critique | The contract predicted right-aligned prose would fight the leader axis on this table. The author solved it rather than dodging it: the label column is pinned (240px desktop / 176px tablet), the common right axis carries the value's *key*, and the sentence breaks to its own line flush on that same axis. Measured leader runs 240-791px desktop, none short enough to orphan. | No action. This was the round's main design risk and it is resolved. | `Table-Mvf-K-*` |
| Others J+K | Critique (honesty) | African Grey is the only row C.A.Gs actually breeds. It is marked by weight plus the small-caps label `The Grey we raise`, lifted from the intro sentence rather than invented, and never by an off-palette colour. | No action. | `Table-Others-*` |
| Mvf, Others, Price (all) | Critique (copy) | COPY.md gives no CTA string for tables 2, 3 and 4, but one clay pill per artboard is mandatory. Authors reused the exact labels rounds 1-3 used (`View Available Greys →`, `Full African Grey Comparison Hub →`, `Reserve Yours Now →`) rather than writing new copy. | No action. Navigation labels, not claims. | all |
| Cvt J+K | Critique | The live copy has **two** footer CTAs. One clay pill is mandatory, so Congo is the pill and Timneh a forest outline pill. | **Open — breeder call.** This silently ranks Congo above Timneh. Alternative: both outline, clay pill moved elsewhere. Asked. | `Table-Cvt-*` |
| All | Harden | Every in-copy link phrase is rendered as an underlined clay `<span>`, not an `<a>`, so the only hit target per artboard is the 48-52px pill. | No action. Deliberate: as anchors they would be ~22px inline targets and would sink the Mobile 44px floor on an artboard. **At apply-time they become real anchors again** — the live page's inline links are content and must not be lost. | all |
| All | Harden | Palette scan across all 24: only `#0f3d2c #1f2a24 #2D6A4F #5b524a #b04228 #c8472f #faf7f4 #ffffff` plus the two token rgba values. Em dashes are lifted-only on every file. Exactly one clay fill per artboard. No emoji, no `border-left` stripes, no gradient text, no `display:table-caption`, `support.js` intact. | No action. | all |

## Counts

- 24 artboards · 4 tables · 2 variations · 3 viewports.
- 24/24 clean on overflow, mobile font floor, mobile hit-target floor, and AA contrast.
- 2 findings fixed by the controller; 3 recorded as accepted or deferred; 1 open breeder call.
- Neither axis reproduces variations A-I from rounds 1-3.

## Recommended per table

**K — Menu Leaders, for all four (Recommended).** Grounded in measurement, not taste: K is
shorter than J at Mobile on every table, and on the Congo-vs-Timneh table — the worst mobile
offender on the homepage — it removes 1,424px against the round-1 layout. On the Pricing table
it also puts price on a single right-hand axis, which is the column buyers scan.

**Named trade-off:** leader dots are the most fragile thing in this set. They depend on a
minimum run length to read as leaders rather than as stray rules, so any future copy edit that
lengthens a label eats the run. J has no such dependency — its numeral gutter cannot break at
any width. If the breeder expects this copy to change often, J is the more durable pick and the
cost is 151-339px of extra mobile height per table.

# Homepage Hero Round 5: Critique / Harden / Refine

Measured 2026-09-11 with Playwright (`scripts/design_canvas_probe.mjs`) on scratch copies with the
`support.js` line removed, each at its own frame width. **Examined: 10 files, 124 text nodes.**
Heights are the `<section>` at the frame width.

## Measured heights (Mobile / Tablet / Desktop)

| Variation | Mobile 390 | Tablet 768 | Desktop 1440 | Desktop band 350–450 |
|---|---|---|---|---|
| Live HeroV3:b | not re-measured | not re-measured | ~649 (2026-09-10) | fail |
| **A · Paperwork card** | 714 | 444 | **409** | pass |
| **B · Arch window** | 734 | 437 | **420** | pass |
| **C · Inline-photo headline** | 644 | 409 | **416** | pass |

## Probe totals (final run)

| Check | Result |
|---|---|
| Horizontal overflow | 0 / 10 |
| WCAG contrast failures (every text node vs nearest opaque bg) | 0 |
| Min Mobile font | 11px = the "Breeder credentials" label in A; 12px = eyebrows. Both are decorative labels (the contract allows 11–12px eyebrows); no fact or price is under 12.5px |
| Mobile hit targets < 44px | 3 = the inline "documented" link in the lead (19px line box). It is an inline text link inside a sentence, the same as live; the CTAs are 46px |
| Text over photo without an opaque bed | 2 = C's H1 box contains the inline pill; the words sit beside the photo, not on it (false positive, confirmed on screenshot) |

## Findings

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| A | Harden | First draft measured 408px (the H1 was capped at 22ch and wrapped to 3 lines) | Cap removed → 2 lines | build_artboards.mjs |
| A | Critique | Availability pill covered the "Midland, Texas" line of the sign | Pill moved to the photo's top-left | build_artboards.mjs |
| A | Honesty | "Breeder credentials" is shown as a visible label | It is the live `aria-label` of the credential list, not a new claim | Hero-A-* |
| B | Critique | A portrait arch crops the 4:3 photo; the first draft cut off the left bird | Arch widened to 360 and `object-position:40% 40%`; both birds in frame | Hero-B-* |
| B | Refine | Right-aligned four-line H1 on desktop | Deliberate (it points into the arch); left-aligned at Tablet/Mobile | Hero-B-Desktop |
| C | Critique | The inline pill was illegible at 196×66 | Enlarged to 292×96 at a 50px H1 (after the 450px ceiling) | Hero-C-Desktop |
| C | Honesty / a11y | An image inside the H1 would add its alt text to the heading | At the apply step the pill is `aria-hidden` with `alt=""`; the live alt stays on the mobile band image. Cost: the photo is decorative at ≥768 | CONTRACT §5 |
| All | Refine | One clay CTA each; secondary is an outlined cream pill; clay headline span sits only on `#0f3d2c` (3.45:1, large text) | none | all |
| All | Content | All 9 carry the live eyebrow, H1, lead (with `#proof` link and its em dash), both CTAs, all four credentials, "6 Birds Available Now", live alt text | none, generated from one string set | build_artboards.mjs |

## Recommendation

**A (Paperwork card).** It is the shortest desktop of the three (409 vs B 420 and C 416), and the
only layout where the four credentials sit on the same object as the proof photo. That is
PRODUCT.md principle 1 ("Provenance is the product: show the paperwork").
**Trade-off:** the photo is a wide crop inside a card, smaller on screen than B's 360×380 arch, and
the mobile hero is 70px longer than C's (714 vs 644).

B is the pick if the photo should dominate. C is the pick if mobile length matters most, at the cost of
the photo being decorative on tablet and desktop.

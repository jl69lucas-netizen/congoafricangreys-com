# Homepage Variations Canvas: Critique, Harden, Refine

Pass run 2026-09-10 over the 90 `.dc.html` artboards in this folder, against `CONTRACT.md`,
`PRODUCT.md` and `DESIGN.md`. Three lenses in order: critique (brand register, hierarchy,
cognitive load, affordance, copy fit, honesty), harden (overflow, box fit, hit targets, text
size, contrast, well-formedness), refine (type scale, 4/8 rhythm, one clay CTA, alignment).

Every number below is measured, not asserted. The probe is
`scratchpad/probe.mjs`: scratch copies with the `support.js` line removed, rendered in Chromium
at each file's frame width, reporting `scrollWidth` vs root width, root height, minimum text
font-size at Mobile, minimum hit-target height at Mobile, and a WCAG contrast sweep of every
text-bearing node against its nearest opaque ancestor background. It reports its own examined
count so a silent PASS is detectable: **2,820 text nodes across 90 files, both runs**.

---

## Hero

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| A | critique / honesty | One portrait of one bird sits beside the claim "6 Birds Available Now". The inventory is asserted, not shown. | Open question. Already in `hero-a-note`; the critique-pass counter-case for B is now appended there. | `Main.dc.html` |
| A, B, C | critique | Each hero artboard pairs with a different counter treatment (A the 4-up ledger, B the 2x2 tiles on the warm bed, C the inline ribbon), so a reader comparing heroes is also comparing counters. Two axes move at once. | Open question, added to `hero-a-note`. Not fixed: holding one counter constant is a re-draw, not a tweak. | all 9 hero artboards |
| A, B, C | harden | Desktop hero grid measured 375 / 389 / 358px, all inside the contract band of 350 to 400. Hero and counter separation present on all nine: tone shift plus `border-top:1px rgba(60,30,10,.12)` on the counter section. | Pass, no action. | all 9 |
| B | harden | Mobile photo-grid sub-caption ("Timneh · $1,500") at 11px, carrying a price. | Fixed: 12px, line-height 1.25. | `Hero-B-Mobile.dc.html` |
| B | honesty | Grid names four real birds. Evie $1,500 and Roys $2,300 both match `dist/index.html` exactly and sit inside the `data/price-matrix.json` ranges. | Pass, verified. | `Hero-B-*.dc.html` |
| C | refine | Desktop H1 wrapped to three lines with "Texas" orphaned on line three (copy column 488px against a 520px H1 max-width). | Fixed: H1 36px, stats column 260 to 252px, gap 36 to 28px, section padding 20 to 44px. Two lines, and the grid re-measures 358px so the 350 floor still holds. The padding carries the height the shorter H1 gave up. | `Hero-C-Desktop.dc.html` |
| C | harden | Mosaic mini-tile captions outgrew their boxes: "Our Aviary Pair" wrapped to two lines inside a 62px (Mobile) / 68px (Tablet) / 74px (Desktop) tile and covered the photograph. | Fixed: tiles to 86 / 88 / 90px, caption 12px, line-height 1.2, padding 16px 9px 7px. | `Hero-C-*.dc.html` |
| C | harden | Mobile stat labels at 11px. | Fixed: 12px, tracking .14 to .11em. | `Hero-C-Mobile.dc.html` |
| C | critique | The four numerals in the stats column are the counter's own four stats, so as drawn the page says 12+ / 100% / $1,500 / 24h twice. | Open question. Already recorded in `hero-c-note`; grid height in that note corrected 355 to 358px after the H1 fix. | `Hero-C-*.dc.html` |

## Counter

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| A, B, C | harden | Mobile stat labels at 11px while carrying the fact, not decorating it. | Fixed: 12px, tracking .16 to .13em, the top of the contract eyebrow band. | `Counter-A/B/C-Mobile.dc.html` |
| B | critique | The 3px forest to clay top bar reads as a gradient. | Not a violation: `CONTRACT.md` §5 names this exact marker as Counter B's axis, and it is a rule, not gradient text. Pass. | `Counter-B-*.dc.html` |
| C | honesty | The fourth stat is off-screen until the ribbon is scrolled sideways. | Pass. The artboard shows the real state and `counter-c-note` says so in its trade-off. | `Counter-C-Mobile.dc.html` |
| A, B, C | refine | Desktop heights measured 172 / 234 / 126px; every numeral-to-label step is at least 2.2x. | Pass, matches the notes exactly. | all 9 |

## Desktop dial

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| B | harden / contract | The active row's numeral `#9fc7b0` on the lighter `#2e5c48` active tint measured **4.11:1**, under invariant 5's 4.5 floor for dial numerals. | Fixed: active numeral to `#c3ded0`, measured 5.36:1. Recorded in `dial-b-note`. | `Dial-B-Desktop.dc.html`, `Rail-B-Desktop.dc.html` |
| A, B, C | refine / contract | The "Part N" tag pill was `.56rem` (8.96px) against a `.74rem` row. The shipped `.tdial .tag` uses `--fs-micro`, the same size as the row, and shrinking these rows is the exact 2026-07-23 density pass the breeder rejected in one line. | Fixed: `.66rem` (10.56px), measured as the largest size at which all eighteen rows stay on one line and the card stays at exactly 594px, which is what `dial-a-note` and `dial-b-note` assert. `.68rem` wrapped row 01 and pushed the card to 608px. | `Dial-A/B/C-Desktop.dc.html`, `Rail-B/C-Desktop.dc.html` |
| B, C | critique | Eighteen clay-filled tag pills carry more visual weight than the labels they annotate. | Open question, added to `dial-b-note`. Not fixed: the pill reproduces the shipped `.tdial .tag` (clay-ink fill, white text) exactly, so retinting it diverges from the live component. | `Dial-B/C-Desktop.dc.html` |
| C | harden | Part-name chips at 10px on Mobile and Tablet. | Fixed: 11px, tracking .12 to .1em. | `Dial-C-Mobile.dc.html`, `Dial-C-Tablet.dc.html` |
| A | refine | Card 196px, ring 64px, rows 24px minimum, tag always visible, numerals `#6b625a` on white measured 5.97:1. Card height 594px; C adds exactly 91px (685px), as `dial-c-note` claims. | Pass, every geometry claim in the notes verified. | all 9 |

## Mobile jump links

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| C | harden | The "Sections" trigger measured **39px** tall, under the 44px floor. | Fixed: `min-height:44px`, `box-sizing:border-box`, padding to `0 18px`. | `Rail-C-Mobile.dc.html` |
| C | honesty | The part-chip row was `overflow:hidden` and clipped "PART FOUR" mid-word at 390, which falsified `rail-c-note`'s claim that the sheet "shows all four part names at once on a 390 screen". | Fixed: chips 11px, padding `0 8px`, tracking .02em, gap 10 to 6px, and `overflow-x:auto` so the row is honest if it ever does overrun. All four now render unclipped at 390 and the note's claim is true as drawn. | `Rail-C-Mobile.dc.html` |
| C | harden | Part-name chips at 10px on Tablet. | Fixed: 11px. | `Rail-C-Tablet.dc.html` |
| C | refine / contract | Two clay fills in one artboard: the Sections trigger and the Reserve a Bird CTA. | Open question, added to `rail-c-note`. Not fixed: the sheet replaces the trigger, so they never appear together and invariant 10 is not broken as drawn. | `Rail-C-Mobile.dc.html` |
| A, B | harden | Rail A pills measured 44px, Rail B chips 46px, both at or over the floor, matching `rail-b-note`. | Pass. | `Rail-A/B-Mobile.dc.html` |

## Tables (mvf, others, cvt, tblc)

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| A, B, C | harden | Twelve table artboards at Mobile: zero horizontal overflow, zero hit targets under 44px, zero contrast failures, every cell fully rendered. This is the defect class the whole page exists to solve and it is solved in all three. | Pass, no action. | 36 table artboards |
| B | refine / contract | The `aria-pressed="true"` toggle is a clay fill, sitting in the same artboard as a clay CTA. | Pass. It is a selected state, the same convention as the FAQ A topic tabs, the Rail C active section pill and the dial active row. One clay CTA per component still holds. | `Table-*-B-Mobile.dc.html` |
| C | critique | Male vs Female marks no winner in the source, so its verdict cards carry no strip and C buys nothing on that table. | Pass. Already recorded in `table-c-note`. | `Table-Mvf-C-*.dc.html` |
| A vs B | refine | A's Congo vs Timneh mobile stack measures 3,398px against B's 1,661px, a 1,737px difference for the same twelve rows. | Recorded below in the recommendation. No edit. | `Table-Cvt-A-Mobile.dc.html` |

## FAQ

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| A | refine / contract | The selected topic tab is a clay fill alongside the clay "See All African Grey FAQs" CTA. | Pass, selected state, same convention as the table toggles. | `Faq-A-*.dc.html` |
| A, B, C | harden | Twenty-one-question label, longest answer, longest `<summary>`: no overflow at any width, no hit target under 48px, no contrast failure. Measured Mobile roots 1,644 / 1,970 / 1,434px. | Pass. C is the shortest at Mobile, which is where the breeder's complaint was filed, matching `faq-c-note`. | 9 FAQ artboards |
| B | critique | `faq-b-note` calls its 12.5px card body "the smallest on this canvas". The measured Mobile minimum on Faq-B is 11px, and that node is the artboard's own eyebrow, not card body, so the note is accurate about content. | Pass, no action. | `Faq-B-Mobile.dc.html` |

## Shipping

| Variation | Lens | Finding | Fix or open question | File |
|---|---|---|---|---|
| B | critique / banned | The two tier cards carried `border-left:4px solid #e8604c`, a side-stripe border used as decoration. Banned outright. | Fixed: uniform `border:1px solid rgba(232,96,76,.38)` on both cards. The clay signal survives at 1px, and the two cards now share edges and paddings, which they did not before. | `Shipping-B-Desktop/Tablet/Mobile.dc.html` |
| B | honesty | `shipping-b-note` claimed it is "the shortest of the three at Tablet". Measured Tablet roots: A 1,033, B 1,065, C 1,223. A is shortest, by 32px. | Fixed in the note: it now states second shortest at both widths, with the six measured numbers. | `canvas.part-shipping.json` |
| A, B, C | copy | Every timeline node and tier claim traced to `dist/`: the $200 deposit, the 10-day vet certificate, in-cabin or flight nanny, $185 airport, $350 home, the 80+ hub list. Only the divider label "Two Ways It Ends" is new UI chrome, and it makes no claim. | Pass. | 9 shipping artboards |
| C | honesty | Only one photo earns a place, so Home Delivery is described but never shown. | Pass, recorded in `shipping-c-note`. | `Shipping-C-*.dc.html` |

## Cross-cutting (all 90 files)

| Lens | Finding | Fix or open question |
|---|---|---|
| critique / banned | Em dashes: 96 occurrences in 51 files. Every one traced to copy lifted verbatim from `dist/index.html`, `dist/congo-vs-timneh-african-grey/index.html` or `dist/hand-raised-african-grey-parrot-for-sale/index.html` with tags stripped. The ban is on new copy. | Pass, no edits. Changing them would break invariant 7. |
| critique / banned | Arrow glyphs `→` and `↗`. | Not emoji, and "Fact ↗" appears four times in `dist/index.html`. Pass. |
| critique / banned | Gradient text, `backdrop-filter`, `{{handlebars}}`, `<script data-dc-script>`: zero occurrences. The nine `linear-gradient` / `radial-gradient` uses are photo scrims and the contract-specified 3px forest-to-clay counter bar. | Pass. |
| critique / banned | `#000` pure: zero. `#fff` / `#ffffff`: 908 uses, all as card surface (`DESIGN.md --card-bg #ffffff`) or as text on a clay or forest fill, both contract-specified in §3. | Pass. |
| harden | `support.js` line present exactly once in all 90 files. Every `<img src>` names one of the seven images in this folder; zero missing. | Pass. |
| harden | Tag balance: 0 errors in 90 files under a strict Python `HTMLParser` walk. `xmllint --html` output is entirely HTML4-parser noise (`x-dc`, `helmet`, `svg`, `section`, `figure`, `nav` unknown) plus the raw `&` in the Google Fonts URL that `CONTRACT.md` §2 prescribes verbatim. No real errors. | Pass. |
| refine | Canvas heights: all 90 artboards listed across the seven `canvas.part-*.json` files, none unlisted, none missing. Every declared `h` is at or above the measured root height and inside +25%. Largest height change from this pass was Hero-C-Tablet at +3.0%, under the 5% re-measure threshold, so **no `h` value needed changing**. | Pass. |

---

## Counts

- **Findings: 32** (across the three lenses, including the passes recorded above so the pass is auditable)
- **Fixed: 12** distinct findings, touching **20 artboards** and **4 note files**
- **Open questions: 5** (Hero A inventory assertion, hero and counter axis confound, Hero C stat duplication, dial tag-pill weight, Rail C two clay fills). All five are also written into the relevant sticky note's trade-off line.
- **Passes with no action: 15**

## Probe totals, before and after

| Metric | Before | After |
|---|---|---|
| Files probed | 90 | 90 |
| Text nodes examined | 2,820 | 2,820 |
| Horizontal overflow (`scrollWidth` > frame width) | 0 | 0 |
| Root width not equal to frame width | 0 | 0 |
| Contrast failures (< 4.5:1, or < 3:1 for large text) | 2 | **0** |
| Mobile hit targets under 44px | 1 | **0** |
| Mobile artboards with text under 14px | 18 | 18 |
| Mobile minimum font-size distribution | 10px on 2, 11px on 16, 14px on 12 | **11px on 12, 12px on 6, 14px on 12** |
| Text over a photograph with no opaque backing | 0 | 0 |

### The one remaining exception, named

**Eighteen Mobile artboards still carry text under 14px, all of it at 11px or 12px.** This is a
direct conflict between the 14px review floor and `CONTRACT.md` §3, which locks eyebrows at
**11 to 12px, letter-spacing .12em, uppercase, clay `#b04228`**, and invariant 5, which locks the
dial row at `.74rem`. The contract is binding, so 11 to 12px stands. What changed is the
composition of that set:

- **Before:** two artboards at 10px (below even the contract floor) and six nodes at 11px that were
  page content, not eyebrows: counter stat labels, a bird's price in a photo caption, a bird's name.
- **After:** every one of the eighteen is either the artboard's own title-strip eyebrow
  (`p.eyebrow`, e.g. "Shipping · variation C · 390", chrome the viewer never ships) or a
  contract-band uppercase label at 12px, the top of the band. Nothing below 11px survives, and no
  price, name or stat sits under 12px.

Contrast was checked at every one of these sizes and all pass: the counter labels are `#2D6A4F`
on cream, the Hero C stat labels `#dbe2df` on `#0f3d2c`, the artboard eyebrows `#b04228` on cream
at 5.38:1.

---

## Recommended per page

Six of the seven `(Recommended)` markers are confirmed on measurement. One is contested.

**Hero: `(Recommended)` is A. Contested, argue for B.** Not on taste, on the honesty lens. Hero A
puts one portrait beside the claim "6 Birds Available Now", so the inventory is asserted. Hero B
names four real birds and prices two of them, and both prices verify exactly against
`dist/index.html` (Evie $1,500, Roys $2,300) and sit inside the `data/price-matrix.json` ranges.
B's recorded penalties are both smaller than they read: its hero grid measures 389px, inside the
350 to 400 band, and Hero-B-Mobile runs 857px against Hero-A-Mobile's 819px, a 38px difference,
not a category difference. **Trade-off if B wins:** four above-the-fold images instead of one, and
Hero A's zero re-approval cost is forfeited because A is the live HeroV3:b lineage measured down
and B is not. This is a breeder call, so the marker is left on A and the case is logged in
`hero-a-note`.

**Counter: A. Confirmed.** Measured Desktop 172px against B's 234px, and it is the live
`counter-home-1280` strip tightened, so it carries no copy risk on the highest-traffic surface.
The measured problem on this homepage was hero height, not counter height. **Trade-off:** its
separation is the minimum invariant 2 allows, a tone shift plus a 1px rule, so any later edit that
drops that border re-breaks the gate.

**Desktop dial: A. Confirmed.** Its numerals measure 5.97:1, the highest of the three (B is 5.0:1
on the card and 5.36:1 on the active row after this pass), and it is the shipped `.tdial` geometry
verbatim: 196px card, 64px ring, 594px at eighteen rows, `.74rem` rows, tag always visible.
**Trade-off:** a near-white card on a cream page leans entirely on its 1px border and warm shadow
to read as an object.

**Mobile jump links: A. Confirmed, on a rule rather than a number.** Hardening skill 1b is a
recorded breeder rejection of bottom-pinned in-page nav, and Rail C reintroduces exactly that
placement for its trigger. Rail A's pills measure 44px, at the floor. **Trade-off:** roughly three
of eighteen labels are visible at 390, so A is only honest if scroll-spy pulls the active pill
into view.

**Tables: A. Confirmed, with the cost stated.** A is the only variation that needs no JavaScript,
and B's scripts-off fallback is the horizontally scrolling table the breeder rejected. **Trade-off,
and it is large:** A's Congo vs Timneh mobile stack measures 3,398px against B's 1,661px, a 1,737px
difference for the same twelve rows. If the breeder weighs scroll length above the no-JS
guarantee, B is the defensible switch, and `table-b-note` already carries the argument.

**FAQ: C. Confirmed.** Measured Mobile roots: C 1,434px, A 1,644px, B 1,970px. C is shortest
exactly where the filed complaint was ("faq section-too long", captured at 375), needs no topic
label decoded and no tab picked, and keeps all twenty-one questions in the markup for a crawler.
**Trade-off:** the other seventeen are one tap further away than in A, and opened, Desktop reaches
2,098px.

**Shipping: B. Confirmed, with its note corrected.** The live section already ships a five-step
flow strip under the copy, so folding it in removes a duplicate and lands the two tiers where a
reader looking for a price arrives. **Trade-off:** it is second shortest at both widths, not
shortest at Tablet as the note previously claimed (Tablet A 1,033, B 1,065, C 1,223; Desktop C 968,
B 1,034, A 1,097), and at 390 the strip has to become a vertical list.

## Canvas
Published 2026-09-10: https://claude.ai/code/artifact/65cdf7d4-d24b-45b4-a8ba-b5bbd142fe15

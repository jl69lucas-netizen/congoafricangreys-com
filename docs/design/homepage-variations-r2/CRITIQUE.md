# Homepage Variations Round 2 (D/E/F): Critique, Harden, Refine

Pass run 2026-09-10 over the 90 `.dc.html` artboards in this folder against `CONTRACT.md`. Every
number is measured by `scripts/design_canvas_probe.mjs` (scratch copies, support.js line removed,
rendered in Chromium at 390 / 768 / 1440). The probe prints its own examined count.

**Probe totals (final run):** files 90 · overflow 0 · hit targets under 44px 0 · contrast fails 0 ·
text over photo 0 · examined 3,055 text nodes. Fifteen "small font" rows remain, all 12px eyebrows
or artboard frame labels, which is the contract's floor (three 11px frame labels on the FAQ Mobile
artboards were raised to 12px during this pass).

Canvas: [`cf046e8c`](https://claude.ai/code/artifact/cf046e8c-0b42-482a-91ed-ec6baead29d5) · 7 pages ·
90 artboards · 30 notes.

## What changed against the brief during the build

| Item | Finding | Resolution |
|---|---|---|
| Fourth table | Round 1 (and this brief's first cut) used the hand-raised page's rearing-paths rows under the heading "What Does a Hand-Raised, Documented African Grey Parrot Cost From C.A.Gs?". The breeder's screenshot is the homepage **pricing table** (six rows, five columns). | Rebuilt as `Table-Price-*` from `src/pages/index.astro` 944–951 verbatim; the Tblc artboards were deleted. |
| Duplicate hero file | `Hero-D-Desktop.dc.html` and `Main.dc.html` were byte-identical, which would draw the same artboard twice. | `Hero-D-Desktop` removed; `Main.dc.html` carries Hero D Desktop. |
| Fragment keys | `canvas.part-tables2.json` carried `id`/`name` on artboards, which the editor drops on Save. | `merge_canvas.py` filters to the allowed key set. |
| Shipping "five-step flow" | The brief said five steps; round-1 copy carries four (Reserve, Vet certificate, In-cabin or cargo, Pickup or delivery). | No fifth step invented; none of D/E/F uses the step strip. |

## Hero (from Hero B; image first at Mobile and Tablet; `.chero` sizes)

| Variation | Desktop `#hero-grid` | Mobile root | Finding |
|---|---|---|---|
| D framed portrait | 386px | 862px | Live hero photo in the for-sale frame; availability pill overlaps the frame. Inventory asserted by the pill, not shown. |
| E lead photo + pair | 390px | 1,071px | Only variation that keeps Hero B's named-bird evidence (Evie $1,500, Roys $2,300). Costs 209px at Mobile. |
| F credential band | 380px | 863px | Credentials leave the copy column for a full-width band; the copy column shortens to 260px. |

All three inside the 350–400 band; all three carry `hero-midland.webp`; all three put the image first at 390 and 768.
**Recommended: D.** Every element already ships somewhere on the site (Hero B copy column + the for-sale frame around the live photo); one LCP image unchanged from the live page; shortest at Mobile. Trade-off: no named birds in the hero.

## Counter

| Variation | Desktop | Mobile | Finding |
|---|---|---|---|
| D icon stat cards | 292px | 394px | Tallest; four cards read as four features, not one strip. |
| E green-tint band | 186px | 237px | Shortest section (86px of stats at 1440); only one keeping hero + counter inside a 900px fold. Labels wrap at 768/390. |
| F seam card | 216px | 290px | Most premium; the 40px overlap collides with the hero's ribbon at 390 unless the hero pads that back. |

**Recommended: E.** Trade-off: least dramatic departure from the live strip.

## Desktop dial

| Variation | Card at 1440 | Finding |
|---|---|---|
| D progress line | 196 × 635px | Shows position and the four parts at once, but taller than A (594px). |
| E two columns | 392 × 337px | 57% of A; the only one fitting under the 772px sticky cap on a 768-tall laptop. Doubles the sidebar width. |
| F collapsed parts | 196 × 440px | Keeps the ring; inactive parts collapse to a header + real count chip. Headers wrap to two lines at 196px. |

Rows ≥26px, `.74rem`, tag pill always visible on all three. **Recommended: E.** Trade-off: grid template change on every page that hosts the dial.

## Mobile jump links (all top-pinned; none bottom-pinned)

| Variation | Rail height | Finding |
|---|---|---|
| D part select + pills | 60px | Part names visible at zero taps; pills per part 3–8 so the active one sits with neighbours. Switching parts costs two taps and needs scroll-spy wiring. |
| E progress rail | 48px | Thinnest; state legible without scrolling the rail. Navigates one section per tap. |
| F icon chips | 60px | One forest marker on quiet chips; 18 icons to maintain, same reach problem as Rail A. |

**Recommended: D.**

## Tables (Mobile root heights; round-1 A/B for Cvt were 3,398 / 1,661)

| Table | D column cards | E banded rows | F accordion rows | Recommended |
|---|---|---|---|---|
| Cvt Congo vs Timneh | 1,582px | 1,556px | 1,056px | **F**: the three Timneh edges read in the summary with zero taps. |
| Mvf Male vs Female | 907px | 765px | 459px | **E**: long-sentence answers stay fully visible; no winner exists so F's summaries all read "Compare". |
| Others Grey vs Macaw/Cockatoo/Amazon | 1,266px | 845px | 635px | **F**: the African Grey value sits in every summary at half of D's height. |
| Price (homepage pricing table) | 1,649px | 2,064px | 834px | **F**: all six prices with zero taps; traits behind a tap for five rows. |

All 36 table artboards: zero overflow, zero small hit targets, zero contrast failures at 390.

## FAQ (all 21 questions and full answers in every artboard)

| Variation | Desktop | Mobile | Finding |
|---|---|---|---|
| D search-first | 1,299px | 1,830px | 21 one-line summaries in two Desktop columns; filter input and topic chips drawn. |
| E quick answers + rest | 1,597px | 2,144px | Six facts readable with zero taps; tallest. |
| F side-nav | 1,743px | 1,898px | Sticky topic list with counts; Mobile becomes topic pills + accordion. |

The live section measures 2,404px at Mobile; round-1 C reached 1,434px only by hiding 17 questions. With every question visible, 21 × 48px summaries alone are ~1,008px. **Recommended: D** (shortest with everything on the page; the "search" field is drawn, so the applied version needs a few lines of filter JS or it becomes decoration).

## Shipping

| Variation | Desktop | Mobile | Finding |
|---|---|---|---|
| D tier chooser | 1,087px | 1,753px | Two equal tier cards; a "per bird" tag was removed mid-build because it is not in the live copy. |
| E route | 981px | 1,380px | Both prices sit on the trip in travel order; crate photo beside. |
| F fact grid | 1,021px | 1,396px | Six definitions without card chrome. |

**Recommended: E.**

## Open questions for the breeder

1. Hero: D (framed live photo) or E (keeps Evie and Roys with prices) is a judgment call the numbers cannot settle.
2. Counter F's seam overlap is the most distinctive counter but only works if the picked hero pads its bottom edge by 40px.
3. FAQ D's search field needs real filtering when applied; otherwise pick F.
4. Dial E changes the sidebar width from 196 to 392px; the for-sale pages hosting `.tdial` would need the same grid change or keep A there.

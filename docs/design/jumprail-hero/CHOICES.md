# Section Menu Choices (2026-09-11)

Preview: https://claude.ai/code/artifact/0f0761a8-1c62-4007-84c1-30479d46cbe5 (source
`section-menu-choices.html`; republish from the same path to update). Screenshots are the built homepage
at 390 / 1024 / 1280 with every fixed overlay hidden; `measurements.json` holds the hero and
section positions the previews use.

## Question 1: desktop section menu over the hero (sitewide, 18 pages use JumpRail)

Today the fixed dot menu (`#cag-jump-rail`, right 18px, 129px wide) overlaps the new hero's photo card by
**59px at 1280** and **99px at 1024** (clear from about 1,420px up).

| Design | What happens | Over the photo card | Trade-off |
|---|---|---|---|
| **1 · Appears after the hero (Recommended)** | Hidden while any part of the hero is on screen; fades in over 0.2s once the hero slides under the header (the mobile Sections button already waits for the same moment) | 0px overlap at every width | No section map on the first screen; appears after about 400px of scrolling |
| 2 · Slim dots over the hero | A 29px dots-only strip 12px from the edge while the hero is on screen; labels on hover or keyboard focus; full menu past the hero | Clears by 47px at 1280, 7px at 1024 | 7px of air at 1024; dots mean little until hovered; hovering spreads labels over the card |

**Why 1:** it is the only one that clears the card at every width by construction, and it reuses a
trigger the component already has. Implementation: an IntersectionObserver on the page's first
section (the hero) toggles a class on `#cag-jump-rail`; `visibility:hidden` while hidden so it is
out of the tab order.

## Question 2: homepage mobile section jump (homepage only)

Today: floating "Sections" button + bottom sheet. Both designs replace it on `/` with the sticky
strip under the header that the for-sale and comparison pages use, placed right after the hero.

| Design | Looks like | Size | Trade-off |
|---|---|---|---|
| A · For-sale style | `.chero-rail` on /congo-african-grey-for-sale/: clay-outlined pills, current section solid clay | 38px, 18 pills | The solid clay pill under the hero's clay CTA reads as a second main button (one clay CTA per component) |
| **B · Comparison style (Recommended)** | `.cvt-rail` on /congo-vs-timneh-african-grey/: 3px clay rule on top, white pills, clay numbers, green labels, current section outlined in clay | 43px, 18 pills | 5px taller; the current section is marked more quietly |

**Why B:** it was built for a 20-section page (the homepage has 18; the for-sale rail has 14), and it keeps
the homepage to one clay button in view.

Reply with one of each, e.g. **1 and B**.

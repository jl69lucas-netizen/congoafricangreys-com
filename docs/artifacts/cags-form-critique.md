# Inquiry Form Critique

> Source: docs/artifacts/cags-form-critique.html (rendered Artifact). Generated from the page's own Markdown blocks — edit the HTML, then regenerate.

## What was asked, what shipped

**The ask (2026-09-11):** space the group titles on the `/available/` and bird-page forms properly at every width; lift the opt-out on `/` and `/contact-us/` (Flag 1) with the Flight Nanny footer (Flag 8); put the old short form back on every blog post with only Confirm Email, Confirm Number and the two screening questions (resale, surrender); then critique and clean all the forms.

| Change | Status | Commit |
|---|---|---|
| Group titles sat **0 px** under the pills/cards above them on `/available/` + 6 bird pages; now 16 px at 375 / 768 / 1280 | Fixed | `126be263` |
| `form-main` (dna-tested, hand-raised, health-guarantee) and `fs-fields` (breeding-pair, congo-pair, baby) rows at 10–11 px, now 14–16 px | Fixed | `126be263` |
| `/` and `/contact-us/`: Message required, Flight Nanny card; pricing footer now reads "Shipping: $185 · Home delivery: $350 · Flight nanny: from $750" | Fixed | `ee6e37cb` |
| 9 blog posts: old short form back + Confirm Email, Confirm Number, resale, surrender. Scam page keeps the full form | Fixed | `4e59d67f` |
| **P0 found by this critique:** the full form's delivery radios were `display:none` and required, so a buyer who skipped delivery could not send the form and saw no message | Fixed | `1807d015` |
| Required `*` on `/available/` + bird forms rendered grey (undefined `text-clay-text` class), now clay `#bd4129` | Fixed | `1807d015` |
| "Four quick fields" / "A few quick fields" over forms that ask 10–11 questions, now "Ten short questions" / "Eleven short questions" | Fixed | `1807d015` |

Live check after deploy: all changed pages return 200; the homepage message is required; the blog form has surrender and no experience question; no `m-0` fieldsets remain on the bird pages.

## Design health score

Scored by the isolated design review on the build **before** the P0, star and copy fixes above, so H1, H5 and H9 are already better than shown.

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 1 | Only native browser bubbles; the homepage form failed silently (now fixed) |
| 2 | Match with the real world | 3 | Plain language; "How would you like Evie to reach you?" can read as phone vs email |
| 3 | User control and freedom | 2 | 1,800–2,800 px single scroll on mobile, no saved draft |
| 4 | Consistency and standards | 1 | 7 families: field order, label case, button radius, "enquiry"/"inquiry" all differ |
| 5 | Error prevention | 2 | Confirm fields present, but split from their originals on Evie and baby |
| 6 | Recognition over recall | 3 | Delivery prices and descriptions shown inline |
| 7 | Flexibility and efficiency | 2 | Confirm fields carry no autocomplete, so they are retyped by hand |
| 8 | Aesthetic and minimalist design | 2 | 11–13 decisions per form; uppercase legends run to 4 lines on mobile |
| 9 | Error recovery | 1 | One bubble at a time, no summary, no "emails don't match" |
| 10 | Help and documentation | 2 | No line saying why the screening questions are asked |
| | **Total** | **19 / 40** | **Poor**, before this pass's fixes |

**Cognitive load:** 6 of 8 checks fail (single focus, chunking, grouping, one-thing-at-a-time, minimal choices, progressive disclosure). Decision points: resale 2 options, experience 2, delivery 4 dense cards, homepage bird picker 8.

## Does it look AI-made?

**Design review: no.** Palette, Plex labels and the pill radios read as on-brand; none of the usual tells (gradients, glass, icon-card grids). The trouble is length and inconsistency between families, not look.

**Detector (impeccable 4.1.0, 9 built pages, exit 2):** 701 findings across the whole pages; scoped to the inquiry forms, only two patterns land inside them:

- **all-caps-body, 26 hits.** Whole questions set in the 12 px uppercase label style: the 111-character resale legend, the 65-character surrender question, the experience and delivery legends, and the homepage bird-picker label. On `/available/`, Evie, the blog, the scam page (both forms), `/contact-us/` and `/`. None on congo-vs-timneh, dna-tested or baby. **Both assessments flagged this independently.**
- **cramped-padding, 2 hits, low confidence.** The trust strip under the `/available/` and Evie forms sits flush on its top border.
- **low-contrast: 0 inside any form.** All 256 hits are elsewhere on the pages (mostly clay hover text on cream).

**Discarded as false positives:** cream-palette (a locked brand colour), dark-glow (the brand's warm shadow `rgba(60,30,10,…)` on a cream page), side-tab on baby / dna-tested (outside the forms).

The in-browser overlay was skipped: `impeccable live` needs a project config (`.impeccable/live/config.json`) that only the separate `/impeccable live` setup creates. The same detector ran from the command line on all 9 pages instead.

## What's working

- **Delivery cards.** Price plus one plain sentence each, with a clear clay-bordered checked state. The strongest pattern in the system; the comparison, for-sale and bird families all share it now.
- **Selected and focused states.** Pill radios fill clay when chosen, inputs get a visible clay focus ring, and the full form's delivery cards now show a focus ring too.
- **Reassurance at the moment of commitment.** "No payment is taken on this form", the 24-hour personal reply, and the DNA / CITES / USDA ticks right under the Evie and `/available/` submit buttons.

## Priority issues

### P0 · The full form could not be sent when delivery was skipped (Fixed, `1807d015`)
The four delivery radios were hidden with `display:none` while the first was `required`. With delivery unset, Chrome refused to submit, sent nothing and logged "An invalid form control with name='delivery_method' is not focusable" four times; keyboard users could never reach the choice. This sat on every page that renders the shared full form, the homepage included, and predates this session. Now the radio is visually hidden but focusable, the card shows a focus ring, and the browser focuses the card's radio and shows its message. Re-measured: 0 warnings. `scripts/form_contract_browser.mjs` now fails any form that raises that warning.

### P1 · No inline validation (Your call)
Errors come only as native bubbles, one at a time, on a very tall form, sometimes under the sticky header. **Fix:** an error summary above the submit, a message on each field with `aria-invalid`, and "Emails don't match" / "Numbers don't match" on the confirm fields. **Trade-off:** adds a small script to every form family.

### P1 · How the screening questions read (Your call)
The resale legend is a 3–4 line uppercase block that reads as an accusation, and "If yes, please explain" sits on a required box, so a buyer must type "No". **Fix, keeping both questions:** group them under "Questions we ask every family" with one line on why; sentence case for question legends; make surrender a Yes/No choice that reveals the text box only on Yes. **Trade-off:** the surrender field changes from free text to Yes/No + text; the audit contract would accept both.

### P2 · One field order across all seven families (Your call)
Evie and baby split confirm fields from their originals; the homepage asks surrender before resale and puts screening between contact details and the bird choice. **Fix:** Contact, then Bird + delivery, then Questions we ask every family, then Message, everywhere. **Trade-off:** a visible reorder on 53 forms; preview first (CLAUDE.md rule 7).

### P2 · Yes/No pills are 38–41 px tall on mobile (Your call)
Under the 44 px touch target. **Fix:** `min-height:44px` on the pill labels in each family. Low risk; a spacing-only change.

### P2 · `text-clay-text` is not a colour in the theme (Your call)
367 uses on the homepage and the 7 `/available/` pages render in inherited ink, not clay. Only the form stars and checked pills were repointed (to `text-clay-ink`). **Fix:** define `--color-clay-text: #b04228` in `global.css`. **Trade-off:** recolours 367 elements on the homepage, the highest-traffic page, so it needs a preview first.

## Persona red flags

**A first-time buyer in their sixties, on a phone.** Labels are 12.6 px uppercase with tracking; the resale question reads as suspicion; before this pass the form promised "four quick fields" and asked eleven questions (fixed). The surrender box demands typing "No".

**A keyboard or screen-reader user.** Before this pass the homepage delivery choice was unreachable (fixed). Errors still arrive only as browser bubbles, with no summary to jump from.

**A mobile buyer mid-research across breeder tabs.** Forms run 1,030–2,828 px tall at 375 px; the site's "Sections" button can cover delivery card text; on the scam page the submit label wraps to two lines with the ✓ alone on the second.

## Minor observations

- Button text on the blog and scam forms uses an em dash ("Send to C.A.Gs — Free, No Pressure ✓"); it wraps badly at 375 px.
- The homepage writes "YES / NO" in capitals; every other family writes "Yes / No".
- The homepage surrender question shows its help text twice (inside the box and under it).
- Homepage delivery descriptions are worded differently from the other six families.
- Submit buttons are 12 px radius on some families and 50 px pills on others.
- On the comparison pages the outline "Ask Us First" link weighs as much as the submit button.
- Comparison delivery descriptions measure 4.70:1 at 12.8 px, just over AA.

## How it was verified

| Gate | Result |
|---|---|
| `python3 scripts/form_contract_audit.py` | PASS · 117 forms examined (53 inquiry, all in scope; 64 newsletter) |
| `node scripts/form_title_gap_probe.mjs` (new) | 0 of 53 forms with a title under 12 px, at 375 / 768 / 1280 |
| `node scripts/form_contract_browser.mjs` | 106 form-viewports, 0 failures: empty rejects, filled accepts, no unfocusable required control |
| `npm run test:render:meta` | 291 passed |
| `python3 -m pytest tests/` | 218 passed |

**Two gate bugs found and fixed on the way,** both charged to the harness, not to the pages:

- The first title-gap probe measured the radio circle, not its pill, and missed the very 0 px collision it was written for. It now measures the option label.
- `dup-no-sibling-crossover` read form text while `dup_content_audit.py` skips it, so the fixed screening questions showed up as duplicate prose (`6a854485`, red-first fixture).

**Found in passing, spun out as its own task:** both duplicate gates exempt a genuine shared passage whenever it sits next to a whitelisted line.

## Questions to consider

1. Why does the homepage ask the screening questions before the buyer has said which bird they want?
2. Could resale become something the buyer affirms ("I'm buying for my own home") rather than a Yes/No that sounds like suspicion?
3. Should the 2,800 px homepage form become two steps (Your bird, then About your home) with exactly the same fields?


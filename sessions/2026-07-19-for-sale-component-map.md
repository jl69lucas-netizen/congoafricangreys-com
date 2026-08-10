# For-Sale Cluster — Component Map (LOCKED 2026-07-19)

Breeder decision: **ALL Task-5 designs approved. Recommended picks are the DEFAULT/first-use; the alternates rotate across other pages as differentiators** (cag-component-refresh deltas, never a palette change). Preview source: `assets/1WORKING-ON/FOR-SALE-PAGES/visual-companion-task5.html`.

## Hero → cluster assignment (locked)
| Cluster | Default hero | Notes |
|---|---|---|
| Money variants: congo-for-sale · timneh-for-sale · baby · hand-raised | **Split-Hero B · Full-bleed warm gradient** | clutch eyebrow + price-anchored CTA |
| Trust pages: dna-tested · health-guarantee · eggs (hybrid) · adoption-cost | **Split-Hero C · Dark + photo grid** | authority register |
| Hub + near-me: parrots-for-sale (hub) · parrot-for-sale · near-me ×2 · grey-african | **Hero-C · Mosaic Metrics** | stats strip + inventory mosaic |
| Pair/family: pair-for-sale · breeding-pair · affordable · male-african-gray | **Hero-A · Scattered Flock Polaroids** | shows multiple birds |
| Buy-prefixed 5 | **Split-Hero A · Image left + trust ribbon** | scam-anxiety reassurance strip |

Differentiate repeated heroes per page: bird photos, eyebrow copy, accent/motif deltas. ~400px-class heights. All hero copy reconciled on intake: **CITES Appendix I**, real birds/pairs only, real 4.9/52 rating, real guarantee, real NAP, cag emoji imgs never 🦜.

## Dial + jump-rail (locked)
- **Default desktop: Dial 1 "Clay Progress Dial"** — clay conic progress ring + section counter + live inventory tags (wire tags to clutch-inventory/price-matrix per page). **Alternate: Dial 2 "Dark Aviary Dial"** — use on pages with LIGHT heroes only (never stacked under Split-Hero C dark).
- **Default mobile: Rail A "Price-chip rail"** — outlined clay chips + live counts, sticky, snap-scroll, scroll-margin offset, `scroll-behavior:auto`. **Alternate: Rail B "Green ticker rail"** — rotate onto hub/near-me pages where the fact-per-stop ticker earns its extra height.

## TOC rotation (all 5 approved; naming cag-toc-fs:01–05)
Defaults first: **fs:01 T1 Numbered Ledger Rail** · **fs:02 T4 Magazine Index Card** (trust pages) · **fs:03 T5 Reserve-Path Stepper** (pages whose sections follow the buy sequence). Rotation: **fs:04 T2 Chip Cloud** (Shop/Proof/Logistics) · **fs:05 T3 Boarding-Pass** (shipping-heavy pages ONLY — buy-with-shipping, near-me; never health-guarantee).

## Key-Takeaway rotation (all 5 approved; cag-key-takeaway-fs:01–05)
Defaults: **fs:01 K1 Receipt Card** (money pages) · **fs:02 K3 Green Ledger Band** (light-hero pages; avoid stacking under dark heroes) · **fs:03 K4 Clipboard Checklist** (proof pages). Rotation: **fs:04 K2 Price-Tag Card** · **fs:05 K5 Capsule Strip** (compact pages / second takeaway slot).

All takeaway numbers Ledger-verified: $1,500 floor · $185/$350 shipping · PBFD+APV PCR · CITES Appendix I · 24h reply · 12–16 wk weaning · Midland pickup 2–3 hr radius.

## Tables (both approved)
- **Default: Table A clay-header stacking table** — clay-ink header band; mobile = attr-labeled stacked cards. Species markers: `/emoji/cag-congo-64.webp`, `cag-timneh-64.webp`, `macaw-64.webp`, `cockatoo-64.webp`, `amazon-64.webp` (all exist in `public/emoji/`).
- **Alternate: Table B clay-spine species cards** — use where a table has ≤3 rows or inside narrow columns.
- Max 6 columns on Table A desktop.

## CTA set + seam (approved)
- Primary: clay pill (`.bg-clay` → renders `--clay-ink #c8472f`, white text). New mid-page **ticket CTA** (arrow chip) for reserve moments → anchors to `#reserve`. Green ghost outline for low-pressure asks. One CTA band per page (`hideGlobalCta` rules apply).
- Seam divider (for-sale variant): clay gradient rule + bird emblem + "C.A.Gs · MIDLAND, TX" wordmark tag; 4–8 per page; decorative alt="" + lazy + CLS dims.

## Per-page assignment discipline
No two sibling pages ship the identical combo. Before each page build, pick {hero variant, dial/rail, toc-fs, takeaway-fs, table style} and record the tuple here so the dup/refresh check can verify uniqueness.

| Page | Hero | Dial/Rail | TOC | Takeaway | Table |
|---|---|---|---|---|---|
| `/african-grey-parrot-bird-eggs-for-sale-usa/` (BUILT 2026-07-20) | Split-Hero C dark | Dial 1 + Rail A | Dial 1 IS the TOC (fs:02 folded in — one nav, not two, to avoid double-TOC clutter under a dark hero) | K4 Clipboard + K1 Receipt | Table A |
| `/congo-african-grey-for-sale/` (BUILT 2026-07-21) | Split-Hero B warm gradient | Dial 2 Dark-Aviary + Rail A | T5 Reserve-Path Stepper (in-body) + Dial 2 (desktop) | K1 Receipt + K4 Clipboard + K3 Green Ledger | Table A + FAQ-A light bordered (egg used FAQ-C dark) |
| `/timneh-african-grey-for-sale/` (BUILT 2026-07-22) | Split-Hero B warm gradient (head-scratch OG) | **Dial 1 Clay Progress** + **Rail B green ticker** | **T1 Numbered Ledger** (in-body) + Dial 1 (desktop) | **K2 Price-Tag + K5 Capsule** | Table A + **Table B clay-spine** (Congo-vs teaser) + **FAQ-B two-column** | tuple fully distinct from Congo; ALL prose written fresh from outline (NOT mirrored) per the new Write-From-Outline rule; 6 good AI infographics + 3 regenerated (price/verify/care) |
| `/hand-raised-african-grey-parrot-for-sale/` (APPROVED 2026-07-22, building) | **Hero-A Scattered Flock** (Mark head-scratch anchor Polaroid; light warm gradient) | **Dial 2 Dark-Aviary + Rail B green ticker** (unused pairing) | **T4 Magazine Index Card** (in-body) + Dial 2 (desktop) | **K3 Green Ledger + K2 Price-Tag** | **Table C Outlined matrix + top-pick badge** (hand-raised vs hand-fed vs parent-raised) + weaning `otA` GEO table + **FAQ-C refreshed → forest-green due-diligence checklist** | dual-variant flock (all 6 available: Bery/Amie/Roys Congo + Jins&Jeni pair + Elad/Evie Timneh); Avail-B sidebar filtered by Congo/Timneh/Pair; framing Desktop B/A/C/H/E · Mobile mC/mB/mA/mG/mH; tuple fully distinct incl. table; EEBP blend; prose written fresh from outline |
| `/african-greys-for-sale-with-health-guarantee/` (**BUILT 2026-07-25**) | **Split-Hero A trust ribbon** (first use in the cluster; ribbon chips = 72-hr guarantee · avian-vet · DNA-sexed · CITES; hero `healthy-african-grey-for-sale.webp` **cover-cropped, NOT blurfilled** — see lesson below) | **Dial 1 Clay + Rail A** (guarantee palette; light-card numerals `#6b625a`) | **T4 "Guarantee Index"** (regrouped The terms / The proof / The caution / The birds) | **K1 Receipt** (green header band, dt/dd ledger rows) **+ K5 Capsule** after §documents | **NEW Table E "Guarantee Ledger"** (green caption band + green spine on the "ours" column) + Table A · **FAQ-A refreshed to a green check-circle** (DNA uses the numbered clay chip + chevron) · **Avail-B faceted by AVAILABILITY POSTURE** (Ready now 1 / Reserve & wean 4 / Bonded pair 1) | tuple fully distinct from all 5 siblings; angle "A Guarantee You Can Actually Use"; EEBP×PAS×EEAT×QAB×FAB; voice lever = enforceable-vs-unenforceable; H6 prefixes In Writing/From the Vet/On File; geo TX/OH/CO/NC/GA/MI/PA/VA; 2 new reviews (Meredith SC · Jeffrey CO); 7 seams; 15 `#reserve` CTAs; prose written fresh from outline |

### Lessons from the health-guarantee build (2026-07-25) — apply to the remaining 16 pages
1. **Blurfill is for the uniform in-body box, NOT for a hero.** `reframe_og.py --style blurfill --mobcrop 4:5` sizes the foreground to ~614px inside a 1408px canvas, so a hero that then `object-fit:cover`s the result shows a small photo floating in a blurred field. Bake hero images with a plain `ImageOps.fit` cover crop (centering tuned per photo) and reserve blurfill for `.sec-img` OG photos.
2. **The blueprint's pre-write header dup-gate is not sufficient on its own.** Three headings cleared the Sprint 1 gate and still collided exactly with the DNA page (`…Collection in Midland`, `CITES Appendix I, Captive-Bred, and Your Paperwork`, `How Do We Measure Up Against the Sellers Ranking Beside Us?`). Run `dup_content_audit.py --headers` against the **built** page, not only against the proposed outline.
3. **"If" is capitalised in AP Title Case.** It is not in the mid-title lowercase list (`a an the and but or nor for so yet at by in of on to as vs per via`). `page_hardening_scan.py` catches it; the blueprint did not.
4. **Seam budget is 4–8, not one per section.** Placing a seam after every section reached 17; trimmed to 7 at movement boundaries.
5. **`final_page_audit.py` had two real bugs** (both fixed this build): the `for-sale` profile fell through to the lean 600–1,200 interior word band, and the word count counted inline `<style>` CSS as body copy. Together they made every for-sale page and most comparison pages warn on `wordcount_in_band` regardless of actual length. New page slugs must also be appended to the `FORSALE` roster or the auditor silently skips them.
| `/dna-tested-african-grey-for-sale/` (**BUILT 2026-07-24**) | **Hero-C Mosaic Metrics** | **Dial 1 Clay + Rail A** | **T2 Chip Cloud** (`<nav class="chipcloud">`, verified in the built page) | **K4 Clipboard + K5 Capsule** | **Table D** + FAQ-A + **Avail-B faceted by SEX** | *Row reconstructed 2026-07-27 — it was missing from this table and its absence caused a later build to wrongly claim T2 Chip Cloud was unused. Verify component claims against the built page, not against this table alone.* hen/cock voice; Avian Biotech; $40–60 priced certificate; ~99% accuracy |
| `/baby-african-grey-parrot-for-sale/` (**BUILT 2026-07-27**) | **Split-Hero B warm gradient — REFRESHED** (all 5 heroes were already spent, so differentiation is by `cag-component-refresh` delta, not a new shell: clutch eyebrow naming live ages · three-babies **brooder** anchor photo where congo/timneh use single-bird portraits · **age/stage** trust chips replacing congo's price chips) | **Dial 1 Clay + Rail A** — tags wired to **age bands**, not prices. `Split-Hero B + Dial 1 + Rail A` is an unused triple (congo = B+Dial2+RailA; timneh = B+Dial1+RailB) | **T5 Reserve-Path Stepper, regrouped to the BIRD's timeline** (Hatch → Hand-Feed → Wean → Fly Home) where congo used T5 for the buyer's sequence | **K3 Green Ledger + K4 Clipboard** (unused pairing) | **NEW Table F "Weaning Timeline"** (wk 1–3 / 4–8 / 9–12 / 12–16) + Table A competitor grid · **FAQ-B two-column refreshed** with a clay number chip · **Avail-B faceted by WEANING STAGE / AGE BAND** (siblings facet by subspecies, posture, sex) | angle "Weaned First. Shipped Second. Never the Other Way Round."; **EEBP × PDB × BAB × QAB** (PDB + BAB both first use in the cluster); voice lever = **weaned vs unweaned / age-in-weeks**; H6 prefixes **At Week N: / From the Nursery: / Weaning Log:**; geo CA·TX·WA·FL·NY·IL·GA·AZ (CA leads — 30 of 89 impressions); 2 new reviews (Joanna CA · Anthony WA); 21 seams / 22 sections; 12 `#reserve` CTAs; 11 external links across 8 domains incl. 4 real Reddit threads; prose written fresh from outline — **dup-gate 0 body, 0 header crossovers** |
| (fill at each page's skeleton approval) | | | | | |

## Still-open flags (carry into next session)
1. Egg page = truth-forward hybrid — recommended, not yet explicitly confirmed by breeder.
2. No page-level sidebar — recommended, not yet explicitly confirmed.
3. Bing Webmaster → Search Performance → **Queries** export still needed (supplied CSV was a date-series chart).

## Avail-C v2 — clean-card spec (LOCKED 2026-07-21, congo page final touches)
The original Avail-C dark-scrim overlay tile (text on photo) shipped bulky on desktop and buried the bird's face on mobile. Locked replacement, reuse cluster-wide: face-first card — square photo block (`aspect-ratio:1/1`, per-bird `object-position`, small dark-green uppercase badge top-left) over a white info panel: name + clay price on one row, 2-line-clamp blurb, and an always-visible full-width clay pill button "View <name> →". Mobile ≤640px: 2×2 grid, blurb hidden, name/price stacked. Card images ship `-440.webp` siblings with `srcset` + `sizes="(max-width:980px) 46vw, 210px"`. Companion fixes locked same pass: hero trust chips 2×2 grid on mobile; portrait masters use `.sec-img.fit-contain` (contain + cream bg) instead of cover-crop; dial numerals `#9fc7b0` on dark green for AA; seam emblem 182×60 q60 ≈5.3KB.

| `/african-grey-parrot-adoption-cost/` (**BUILT 2026-07-27**) | **Split-Hero C dark — REFRESHED**: the 2×2 grid is an ascending **PRICE LADDER** ($1,500 Evie → $1,700 Bery → $2,300 Roys → $3,500 pair) with a price chip on every tile, where the egg page used four undifferentiated photos | **Dial 1 Clay + Rail B green ticker** — `Split-Hero C + Dial 1 + Rail B` is an unused triple (eggs = C + Dial 1 + Rail A) | **T1 REFRESHED to a money-preview rail** — section numerals replaced by the dollar band each section covers, so the contents list itself reads as a ledger. All five TOC shells were spent, so this is a refresh delta, not a new shell | **K2 Price-Tag + K4 Clipboard** (unused pairing) | **NEW Table G "True-Cost Ledger"** (3 routes × Day One / Year One / Five Years, plus a "what the number leaves out" spine) + Table A route-presentation grid · **FAQ-C refreshed to a ledger register** with a clay `$` chip · **Avail-B faceted by PRICE BAND** | angle **"The Fee Is Not the Cost."**; structure **Number → Ledger → Thesis** (price intent beats adoption intent 5:1 in this page's real query set); **EEBP × Setup-Stat-Reframe × 5 Basic Objections × QAB** (the middle two are cluster-firsts); voice lever = **fee vs cost, sticker vs total**; H6 prefixes **Line Item: / From the Ledger: / Receipt Note:**; geo NJ·MA·MN·MO·OR·IN; 2 reviews (Lawrence Brunner CA · Ida Brim TN); 10 seams / 10 sections; 5,305 words; **NEW `.ctool` True-Cost Calculator** — multi-year, ranges, route comparison, deliberately differentiated from the homepage first-year calculator and cross-linked to it — and **NEW `fs-nl ledger`** Price-Watch newsletter, the third variant; dup-gate **0 body, 0 header**; infographic slots filled in the **2026-07-28 harden pass** — 7 of 8 dropped infographics shipped (INF-4 five-year-cost-curve REJECTED: its axis labels were bird prices and shipping tiers) plus the 6 previously-orphaned OG photos, **13 in-body figures** where the page had shipped with **zero**. That pass also rendered five mandated components whose CSS had shipped with no markup behind them — **`.doc-stack` · `.otA` ×2 GEO fact tables · `.vflags` green-flag ledger · `.chkB` rescue checklist · `.fs-video` proof-of-life clip** — plus the missing `.geo-pin`/`.geo-arrow` internals and the missing `.read-img` thumbnails. Record these as SPENT for sibling rotation. Lessons: `docs/superpowers/sessions/2026-07-28-adoption-cost-harden-lessons.md` |

## TOC rotation is now EXHAUSTED (recorded 2026-07-27)

All five TOC shells are spent, verified against the built pages rather than this table:

| Shell | Spent by | Marker in code |
|---|---|---|
| T1 Numbered Ledger Rail | timneh | — |
| T2 Chip Cloud | **dna-tested** | `class="chipcloud"` |
| T3 Boarding-Pass | *unused, but restricted* | ledger rule: shipping-heavy pages ONLY (buy-with-shipping, near-me) |
| T4 Magazine Index Card | hand-raised, health-guarantee | `class="t4-grid"` |
| T5 Reserve-Path Stepper | congo, baby | `class="stepper"` |

From here, every remaining page differentiates its TOC by a **`cag-component-refresh` delta on an
existing shell**, exactly as the baby page did when all five heroes were spent. Do not reach for T3 on a
page that is not shipping-heavy just because it is technically unused — the restriction is the point.

**Verification command — run this instead of trusting the table:**

```bash
for p in <slugs>; do printf "%-46s " "$p"; \
  grep -ohE 'class="(chipcloud|stepper|t4-[a-z]+|toc[A-Za-z0-9]*)"' src/pages/$p/index.astro \
  | sort -u | tr '\n' ' '; echo; done
```

---

## Page 9 — Congo Pair · `/congo-african-grey-parrot-pair-for-sale/`

**Tuple recorded 2026-07-30, before build** (binding, per skill §1 and master brief §10).

| Slot | Assignment | Distinctness |
|---|---|---|
| Hero | **Hero-A refreshed "Bonded Duo"** — two large paired Polaroids | Hero-A used once (hand-raised, rotated 2×2 of four). Only kit hero built to show two birds; two tiles also solve the asset-resolution problem |
| Dial | **Dial 2 Dark-Aviary** | Legal — the Bonded-Duo hero is warm/light |
| Rail | **Rail A** | **New pairing.** Hand-raised is the only other Dial 2 page and it used Rail B |
| TOC | **T3 Boarding-Pass** ⭐ **first use in the cluster** | Spec reserves T3 for shipping-heavy pages. Earned: shipping two birds together is a real content axis (§18) |
| Takeaway | **K1 Receipt + K2 Price-Tag** | New combination across all 8 shipped tuples |
| Table | **new Table F "Pairing Routes"** + Table A | **F is the only unused letter.** The three routes need a table that does not exist |
| FAQ | **FAQ-B refreshed**, two-column, new palette | FAQ-B used once (timneh) |
| Avail facet | **Avail-B faceted by pairing route** — Ready-Made · Build-Your-Own · Breeding Referral · Single | New facet; siblings use subspecies / posture / sex / age band |
| Voice lever | **two-versus-one** — bonded, compatible, introduced, quarantined, solo, flock-of-two, human-bonded | New |
| H6 prefixes | **From the Aviary: · Two-Bird Note: · Before You Commit:** | Clear of health-guarantee and dna-tested prefixes |
| Images | Desktop **H, B, A, E** · Mobile **mG, mC, mB, mA** | H Duo Strip leads — the only pair-shot style |
| Seams | 4–8, movement boundaries, small footer-logo | Cluster standard |

**Header dup-gate run BEFORE outline approval** (trap #6): 98 proposed headings vs 606 sibling headings across all 8 shipped pages → **0 exact, 0 template crossovers.** Counts machine-verified: H1 1 · H2 23 · H3 38 · H4 18 · **H5 10** · **H6 8**; all six levels present.

---

# Tuples 11 and 12 — the last two spokes (LOCKED 2026-08-10)

**Correction to the breeding-pair row above (2026-08-03).** That row records **"T3 Boarding-Pass ⭐ first use
in the cluster."** It is not true. `dist/african-grey-breeding-pair-for-sale/index.html` ships `phero-ledger`
and `ptile-chip`; a grep for `boarding|bpass|tocT3|toc-t3` across **all** built pages returns nothing.
**T3 has never been built.** This is the second time this table has recorded a component claim the built page
does not support — the dna-tested row carries the same warning. *Verify against `dist/`, not against this
table.*

Consequence: **T3 Boarding-Pass is free, and the spec reserves it for shipping-heavy pages — naming
`buy-with-shipping` and `near-me` explicitly.** Page A claims the genuine first use.

## Measured inventory across the 10 shipped pages (2026-08-10, from `dist/`)

| Axis | Spent |
|---|---|
| TOC shells | T5 `stepper` (congo, baby) · T2 `chipcloud` (dna) · T4 `t4-grid` (hand-raised, health-guarantee) · T1 `t1m` refreshed (adoption-cost) · **T3 — UNUSED** |
| Rails | `railA` ×7 · `railB` ×3 |
| FAQ | `faqA` ×4 · `faqB` ×4 · `faqC` ×3 — **all three shells spent; new pages must refresh** |
| Takeaway **pairs** | (1,2) (1,3) (1,5) (2,3) (2,4) (2,5) (3,4) (3,5) (4,5) — **only (1,4) is unused** |
| Tables | `tblA` (dna, health-guarantee) · `tblC` (hand-raised) · `tblD` (dna) · `tblE` (health-guarantee) |

## Tuple 11 — `/buy-african-grey-parrots-with-shipping/`

| Axis | Pick | Why it is distinct |
|---|---|---|
| Hero | **Split-Hero A trust ribbon — REFRESHED**: ribbon chips become **price-transparency chips** (`$1,500 floor` · `every price shown` · `CITES Appendix I` · `72-hr guarantee`) where health-guarantee's ribbon carried guarantee chips | Split-Hero A spent once; differentiation is a refresh delta, not a new shell |
| Dial + Rail | **Dial 2 Dark-Aviary + Rail B** | Split-Hero A is light, so Dial 2 is legal. health-guarantee shipped Split-Hero A + Dial 1 + Rail A → **new triple** |
| TOC | **T3 Boarding-Pass ⭐ GENUINE first use** | Never built. Spec reserves T3 for shipping-heavy pages and names this slug |
| Takeaway | **K1 Receipt + K4 Clipboard** | **The only unused pair in the cluster** |
| Table | **NEW Table H "Price Ladder"** — source · price · date measured · what the price includes | Carries the MANDATORY price-artifact proof; no sibling has a cross-vendor price table |
| FAQ | **FAQ-A REFRESHED → price-chip register** (clay `$` chip replacing the check-circle) | All three FAQ shells spent; adoption-cost used a clay `$` chip on **FAQ-C**, so the chip on **FAQ-A** is a new pairing |
| H6 prefixes | `Price Check:` · `On the Paperwork:` · `What We Measured:` | Clear of all 19 spent prefixes |
| Geo | IA · KY · MD · TN · WI | The only five unspent by any built sibling |

## Tuple 12 — `/african-grey-parrots-for-sale-near-me/`

| Axis | Pick | Why it is distinct |
|---|---|---|
| Hero | **Hero-C Mosaic Metrics — REFRESHED**: the mosaic tiles become a **geographic tile field** (state/metro tiles with live counts) where dna-tested's mosaic carried lab metrics | Hero-C spent once; refresh delta, and it previews the page's own function |
| Dial + Rail | **Dial 1 Clay + Rail B green ticker** | dna-tested shipped Hero-C + Dial 1 + **Rail A** → **new triple**. Ledger rotates Rail B onto hub/near-me pages |
| TOC | **T2 Chip Cloud — REFRESHED to a state-chip cloud** (chips are state and metro abbreviations that jump into the grid) | T2 spent once by dna-tested as a topic cloud; a *navigational geographic* chip cloud is a real functional delta, and it doubles as a second entry into the grid |
| Takeaway | **K3 Green Ledger + K4 Clipboard + K5 Capsule** | Every pair except (1,4) is spent and (1,4) goes to Page A; the triple (3,4,5) is unused — timneh's (2,3,5) is the only other triple |
| Table | **NEW Table I "Distance Ledger"** — state · nearest cargo airport · route · cost tier | No sibling ships a geography-to-logistics table |
| FAQ | **FAQ-B REFRESHED → map-pin register** (pin glyph replacing timneh's clay number chip) | FAQ-B spent by timneh, baby and congo-pair; the pin is the delta and it matches the page's job |
| H6 prefixes | `Distance Note:` · `From Midland:` · `Ask Before You Drive:` | Clear of all 19 spent prefixes and of Page A's three |
| Geo | **All 39 shallowly** — 24 states + 15 metros, each once in the grid | Depth belongs to the state page itself; Page B owns breadth, never depth |

**Cross-check: tuples 11 and 12 share no axis.** Different hero shell, different dial, different TOC,
disjoint takeaway sets, different new table, different FAQ refresh, disjoint H6 prefixes.

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
| (fill at each page's skeleton approval) | | | | | |

## Still-open flags (carry into next session)
1. Egg page = truth-forward hybrid — recommended, not yet explicitly confirmed by breeder.
2. No page-level sidebar — recommended, not yet explicitly confirmed.
3. Bing Webmaster → Search Performance → **Queries** export still needed (supplied CSV was a date-series chart).

## Avail-C v2 — clean-card spec (LOCKED 2026-07-21, congo page final touches)
The original Avail-C dark-scrim overlay tile (text on photo) shipped bulky on desktop and buried the bird's face on mobile. Locked replacement, reuse cluster-wide: face-first card — square photo block (`aspect-ratio:1/1`, per-bird `object-position`, small dark-green uppercase badge top-left) over a white info panel: name + clay price on one row, 2-line-clamp blurb, and an always-visible full-width clay pill button "View <name> →". Mobile ≤640px: 2×2 grid, blurb hidden, name/price stacked. Card images ship `-440.webp` siblings with `srcset` + `sizes="(max-width:980px) 46vw, 210px"`. Companion fixes locked same pass: hero trust chips 2×2 grid on mobile; portrait masters use `.sec-img.fit-contain` (contain + cream bg) instead of cover-crop; dial numerals `#9fc7b0` on dark green for AA; seam emblem 182×60 q60 ≈5.3KB.

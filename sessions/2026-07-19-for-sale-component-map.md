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
| (fill at each page's skeleton approval) | | | | | |

## Still-open flags (carry into next session)
1. Egg page = truth-forward hybrid — recommended, not yet explicitly confirmed by breeder.
2. No page-level sidebar — recommended, not yet explicitly confirmed.
3. Bing Webmaster → Search Performance → **Queries** export still needed (supplied CSV was a date-series chart).

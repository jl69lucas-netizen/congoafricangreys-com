# Round 3 (G/H/I) — Critique, Harden, Refine

Canvas: [artifact `a93a3d61`](https://claude.ai/code/artifact/a93a3d61-c5ab-4bc6-80e7-1d96590d574b)
90 artboards · 10 components × 3 variations × 3 viewports · 7 canvas pages.

## Counts

| Gate | Examined | Findings at close |
|---|---|---|
| `scripts/r3_probe.mjs` (overflow · height · font · hit target · contrast) | **90** | **0** |
| `scripts/r3_content_gate.py` (content completeness · banned tokens) | **90** | **0** |
| Canvas overlap check | 91 artboards / 7 pages | **0** |

## Probe totals, before and after

| Finding | Raised | Verdict | Action |
|---|---|---|---|
| 9 × "BANNED emoji icon" on Table-Cvt | content gate | **HARNESS BUG** | `★ ☆` are verbatim from the live `CompareTableE` rows; the regex caught the whole `☀-➿` dingbat block. Narrowed to real emoji (`U+1F300+`, or a dingbat with a `U+FE0F` selector). No page edited. |
| 3 × "contrast 3.6:1 on Midland, Texas" | probe | **HARNESS BUG** | 32px text is WCAG large text and needs 3:1, not 4.5:1. Probe now applies the large-text threshold. No page edited. |
| 3 × "contrast 1:1 on Reserve Yours Now" | probe | **HARNESS BUG** | Probe read `rgba(45,106,79,.08)` as opaque forest. It now composites the alpha stack; the real value is ~5.4:1. No page edited. |
| `#f2b6a8` eyebrow on the shipping scrim | probe (4.14:1) | **REAL** | A colour I invented, outside the locked palette. Replaced with the on-dark token `#9fc7b0` and the scrim deepened to `rgba(15,61,44,.92)`. |
| `#c8472f` as small text on cream (4.48:1) | probe | **REAL** | Clay-ink is the *solid-fill* token. Small clay text on light is `#b04228`. Fixed in `Dial-H-Mobile`. |
| TOP PICK badge `#0f3d2c` on `#e8604c` (3.6:1) | probe | **REAL** | Changed to the documented white-on-`#c8472f` pairing that `Table-Price-G` already used. |
| 11px text on 9 Mobile artboards | probe | **REAL** | Raised to the 12px Mobile floor. |
| `Faq-I-Mobile` 1,488px ≥ 1,400 target | probe | **REAL** | 21 × 46px hit targets is a 966px floor, so the open answer now shows the lead sentence at Mobile. 1,368px. |
| `Faq-G-Desktop` / `Faq-H-*` carried only 5 of 21 questions | content gate | **REAL** | Only the open/active panel had questions in markup. All four panels now render; inactive ones are hidden but present, so all 21 stay crawlable. |

**Three of the first four finding classes were harness bugs, not design defects.** That matches this
project's record (2026-07-31: ten findings, ten in the harness) and is why every one was confirmed on
the artboard before anything was edited.

### Gate self-test

`r3_content_gate.py` was verified to still fail on injected defects before its clean run was trusted:
removing the TOP PICK marker and changing `$95` were both caught; a real emoji in text was caught;
`★`/`✓` correctly were not. A gate that examines zero files and reports PASS is the failure
`cag-gate-integrity.md` exists to catch, so both gates print their own examined count.

## The two named failures, measured

| | Live homepage | G | H | I | Gate |
|---|---|---|---|---|---|
| **Hero, Desktop height** | **~649px** | **360** | **379** | **387** | 350-400 band — all three pass |
| **FAQ, Mobile height** | **~2,404px** | **909** | **750** | **1,368** | <1,400 — all three pass, all 21 questions in markup |

## Measured heights (Mobile / Tablet / Desktop)

| Component | G | H | I |
|---|---|---|---|
| Hero | 618 / 391 / 360 | 864 / 612 / 379 | 625 / 467 / 387 |
| Counter | 268 / 163 / 179 | 248 / 162 / 182 | 198 / 196 / 200 |
| Dial | 931 / 734 / 822 | 886 / 719 / 930 | 527 / 471 / 471 |
| Rail | 1026 / 738 / 971 | 695 / 857 / 844 | 1007 / 850 / 637 |
| Table-Cvt | 1782 / 1514 / 1112 | 1339 / 922 / 980 | 603 / 1217 / 996 |
| Table-Mvf | 979 / 705 / 644 | 810 / 769 / 717 | 1043 / 846 / 728 |
| Table-Others | 1185 / 613 / 651 | 957 / 632 / 610 | 1214 / 809 / 722 |
| Table-Price | 1855 / 1102 / 918 | 1237 / 787 / 833 | 1575 / 1238 / 898 |
| FAQ | 909 / 912 / 1011 | 750 / 709 / 723 | 1368 / 1417 / 980 |
| Shipping | 713 / 576 / 530 | 946 / 611 / 523 | 694 / 687 / 626 |

## Recommended per component — each with the trade-off named

- **Hero: G (Marquee) — recommended.** In band at 360px and shortest at Mobile (618 vs H 864).
  The type-led horizontal band is the clearest structural break from the six hero layouts already
  rejected across rounds 1-2. **Trade-off:** like round 1's Hero A it asserts a bird *count* rather
  than naming birds; **H is the honesty pick** — it puts Roys, Amie, Bery, Jins + Jeni, Elad and Evie
  in the hero with real prices — at the cost of 246px more at Mobile and ongoing inventory upkeep.
  This one is a breeder call.
- **Counter: I (Stamp row) — contested, and I argue against it.** I is shortest at Mobile (198px),
  but a circular certification seal implies third-party certification, and rule 12 forbids implying
  that for our own method labels. **Recommend H (Split emphasis)** instead: 248px at Mobile, and the
  asymmetry is a real departure from the six counter layouts already used. **Trade-off:** H demotes
  `$1,500` and `24h`, the two most transactional numbers, to the small column.
- **Dial: H (Numbered index) — recommended.** I is far shorter (471px vs 930px) but labels only 1 of
  18 sections, which fights invariant 5's "label always visible". H keeps every label, drops the ring
  entirely, and is a genuine departure. **Trade-off:** it reads as a table of contents, losing the
  at-a-glance sense of progress a gauge gives.
- **Mobile jump links: H (Two-tier rail) — recommended.** Shortest at Mobile (695px), and the part
  hierarchy is visible with zero interaction. Top-anchored, so the 2026-07-23 bottom-pin rejection
  holds. **Trade-off:** two rows of sticky chrome consume the most viewport of the three.
- **Table-Cvt: I (Pick-first) — recommended.** 603px at Mobile against G's 1,782px, on the longest
  table on the page. **Trade-off:** the 12 rows start collapsed, so a buyer who wants the full
  comparison has to ask for it.
- **Table-Mvf: H (Definition list) — recommended.** 810px at Mobile, and the boxless treatment suits
  a 3-row table that does not need card furniture. **Trade-off:** least scannable when comparing two
  values directly. Note G deliberately marks **no winner** here, because the page's own point is that
  upbringing matters more than sex.
- **Table-Others: H (Definition list) — recommended.** Shortest at Mobile (957px) on the widest table
  (4 columns). **Trade-off:** four species as prose is a lot of reading; G's noise-level bars are more
  scannable but run 1,185px.
- **Table-Price: H (Definition list) — recommended.** 1,237px at Mobile against G's 1,855px, with the
  price right-aligned on the breed line so the six prices stay scannable. **Trade-off:** loses G's
  price-position bar, which was the clearest way to see the $95-$3,500 spread.
- **FAQ: G (Topic accordion) — recommended.** 909px against the live 2,404px, a 62% cut, with all 21
  questions visible and crawlable under 4 topic headers. H is shorter (750px) and fixed-height, but
  hides 16 of 21 behind unclicked tabs. **Trade-off:** G answers nothing until a topic is opened.
- **Shipping: H (Tier compare) — recommended.** The only variation that puts all three tiers side by
  side against the same four questions, which is the fix for the round-2 defect. **Trade-off:**
  tallest at Mobile (946px).

## Open flags for the breeder

1. **Hero G vs H** is a genuine judgment call: shortest and boldest (G) against naming real birds
   and real prices (H). Round 1 had the same argument and left it to you.
2. **Counter I's seal shape** implies third-party certification for self-reported facts. I recommend
   against it on rule 12; say the word if you read it differently.
3. **`#6b625a` on cream measures 4.47:1**, just under the ≥4.5 that invariant 5 itself requires.
   That token pairing in `CONTRACT.md` §3/§4 is internally inconsistent. Round 3 used `#5b524a`
   (Muted, also locked) where a numeral needed to pass. The contract should be amended.

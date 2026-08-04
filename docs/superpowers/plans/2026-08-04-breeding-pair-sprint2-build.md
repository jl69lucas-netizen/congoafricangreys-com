# Breeding-Pair Page — Sprint 2→6 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended)
> or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`)
> syntax for tracking.

**Goal:** Ship `/african-grey-breeding-pair-for-sale/` — a ~6,200-word, 19-section transactional page
for three real proven pairs — from an approved outline, hardened and gated, live on `main`.

**Architecture:** One Astro page at `src/pages/african-grey-breeding-pair-for-sale/index.astro`,
replacing a 3,881-byte stub. Prose is written fresh from the Sprint 1 outline; components and CSS are
reused from the for-sale cluster kit. Images bake into `public/` as WebP under 95 KB with `-760`
siblings. The build ships its own CTA band (`hideGlobalCta`) and one interactive checklist tool in
vanilla JS. Every gate measures `dist/`, never source.

**Tech Stack:** Astro · Tailwind + scoped CSS · vanilla JS (no frameworks, no CDNs) · Pillow for the
image bake · Playwright render harness · Python audit scripts.

**Approved inputs — do not re-derive, do not re-open:**

| Doc | Carries |
|---|---|
| `sessions/2026-08-03-breeding-pair-sprint0-research.md` | SERP, fan-out, competitor gaps |
| `sessions/2026-08-03-breeding-pair-sprint05-strategy.md` | Strategy C, CTA cadence, §7a counter-positions |
| `sessions/2026-08-03-breeding-pair-sprint1-blueprint.md` | Component tuple, matrix, H1–H6 outline, meta, counters |
| `sessions/2026-08-03-breeding-pair-infographic-prompt-pack.md` | 7 infographic prompts + section map |
| `docs/superpowers/plans/2026-08-03-cag-universal-page-build-brief.md` | Standing law, all gates |

**Binding constraints (Sprint 1 §6), carried into every task below:**
banned phrases *"5–6 years minimum"* / any DNA-certified claim about the pairs / any printed
incubation-day figure · never promise a clutch · tameness is our first-hand account of our own birds,
never a species claim · prices unchanged, market comparison published with its reason in the same
paragraph · exactly one link out to Cluster E · write from the outline, never from a sibling.

---

## File Structure

| File | Responsibility | Action |
|---|---|---|
| `src/pages/african-grey-breeding-pair-for-sale/index.astro` | The whole page — frontmatter, 19 sections, scoped CSS, JSON-LD, checklist JS | **Replace** (3,881 B stub) |
| `public/images/breeding-pair/*.webp` | 13 baked figures + `-760` siblings | Create |
| `assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/` | Source masters | Rename in place |
| `sessions/2026-08-04-breeding-pair-sprint2-build.md` | Session brief + `## Open Flags` | Create |
| `docs/reference/session-log.md` | Build record + Known Issues | Append |

Everything lives in one `.astro` file because that is the cluster's shipped idiom — the nine live
siblings are each a single page file with scoped CSS. Splitting this one would break component
fidelity with the kit it must match.

---

## Task 0: Asset Remediation — BLOCKING

Two infographics failed the spelling/layout check and cannot ship. Three filenames are malformed.
**No page HTML is written until this task closes.**

**Files:**
- Rename: `assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/inf-{5,6,7}-*.png .png`
- Regenerate: `inf-2-price-ladder.png`, `inf-7-housing-nest-box.png`

- [ ] **Step 1: Fix the three malformed filenames**

Three files carry a trailing `.png ` plus a second `.png` — a copy artifact, not a content problem.

```bash
cd "/Users/apple/Downloads/CAG/assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR"
mv "inf-5-pairing-method.png .png" "inf-5-pairing-method.png"
mv "inf-6-market-prices.png .png"  "inf-6-market-prices.png"
mv "inf-7-housing-nest-box.png .png" "inf-7-housing-nest-box.png"
```

- [ ] **Step 2: Verify all seven stems now resolve cleanly**

```bash
ls "/Users/apple/Downloads/CAG/assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR"/inf-*.png
```

Expected: exactly 7 lines, each ending `.png`, none containing a space before the extension.

- [ ] **Step 3: Hold for the two regenerated infographics**

INF-2 and INF-7 are defective (see the defect table below) and must be regenerated from the
**unchanged** prompts in the prompt pack, then re-dropped under the same filenames.

| File | Defect found on inspection | Verdict |
|---|---|---|
| `inf-2-price-ladder.png` | **"SALLY & ODIN" renders twice** — once on the step block, once in the label row. Same class as the shipped "HOME HOME" defect | REGENERATE |
| `inf-7-housing-nest-box.png` | **All four labels render twice** — FLIGHT LENGTH / NEST BOX / TEMPERATURE / HUMIDITY each appear above *and* below the icon | REGENERATE |

Add this line to the end of both prompts before regenerating — it is the only change:

```
Each label appears exactly once. Do not repeat any heading, label, or name anywhere in the image.
```

- [ ] **Step 4: Re-inspect every regenerated file by opening it**

Read the image. Do not read the filename and assume. Confirm: no duplicated words, no misspellings,
every string matches the prompt exactly, and for INF-3 the `15 MONTHS` marker sits left of `3 YEARS`.

Expected: zero defects across all seven.

- [ ] **Step 5: Commit the renames**

```bash
cd /Users/apple/Downloads/CAG
git add "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR"
git commit -m "chore(breeding-pair): normalize infographic filenames"
```

---

## Task 1: Bake the Infographics

**Files:**
- Read: `assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/inf-*.png`
- Create: `public/images/breeding-pair/inf-*.webp` + `-760` siblings

Infographics carry baked-in text and are **never** cover-cropped — `bake_infographics.py` preserves
native ratio. Photos go through `reframe_og.py` instead (Task 2).

- [ ] **Step 1: Bake all seven at native ratio**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/bake_infographics.py \
  "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR" \
  public/images/breeding-pair \
  inf-1-what-proven-means inf-2-price-ladder inf-3-breeding-age-timeline \
  inf-4-moving-a-pair inf-5-pairing-method inf-6-market-prices inf-7-housing-nest-box
```

Expected: 14 files written — seven `<stem>.webp` plus seven `<stem>-760.webp`.

- [ ] **Step 2: Verify every file is under the 95 KB target**

```bash
cd /Users/apple/Downloads/CAG
ls -la public/images/breeding-pair/*.webp | awk '{printf "%-58s %6.1f KB\n", $NF, $5/1024}'
```

Expected: every line under 95.0 KB. Ceiling is 100 KB; anything between 95 and 100 is a warning to
log under `## Open Flags`, not a failure.

- [ ] **Step 3: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add public/images/breeding-pair
git commit -m "feat(breeding-pair): bake 7 infographics to WebP under 95KB"
```

---

## Task 2: Bake the OG Photos

**Files:**
- Read: the 17 photo masters in the asset folder
- Create: `public/images/breeding-pair/*.webp` + `-760` siblings

`talker-jane-african-grey-breeding-pair-sale-nearby.webp` is 305 KB and is the single largest
offender — it must come out under 95 KB.

- [ ] **Step 1: Bake the pair portraits with the locked blur-fill default**

Portraits are **never** focal-point cover-cropped — it cuts heads. `--style blurfill --mobcrop 4:5`
is the locked default from `IMAGE-DESIGNS.md` §7.

```bash
cd /Users/apple/Downloads/CAG
SRC="assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR"
OUT=public/images/breeding-pair
python3 scripts/reframe_og.py --style blurfill --mobcrop 4:5 --maxkb 95 \
  "$SRC/talker-jane-african-grey-breeding-pair-sale-nearby.webp" \
  "$OUT/talker-jane-proven-african-grey-breeding-pair.webp"
python3 scripts/reframe_og.py --style blurfill --mobcrop 4:5 --maxkb 95 \
  "$SRC/mari-lake-african grey breeding pair for sale.jpg" \
  "$OUT/mari-lake-african-grey-breeding-pair-two-clutches.webp"
python3 scripts/reframe_og.py --style blurfill --mobcrop 4:5 --maxkb 95 \
  "$SRC/sally-odin-breeding pair of african greys for sale.jpg" \
  "$OUT/sally-odin-youngest-proven-african-grey-pair.webp"
```

Expected: six files (three `.webp` plus three `-760.webp`), each under 95 KB.

- [ ] **Step 2: Bake the wide/scene photos at 16:9**

Wide and scene images stay 16:9 desktop / 5:4 mobile — no `og-tall` treatment.

```bash
cd /Users/apple/Downloads/CAG
SRC="assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR"
OUT=public/images/breeding-pair
python3 scripts/reframe_og.py --style blurfill --maxkb 95 \
  "$SRC/hero-african-grey-breeding-pair-sale-nearby-cage.jpg.webp" \
  "$OUT/hero-proven-african-grey-breeding-pairs-midland-texas.webp"
python3 scripts/reframe_og.py --style blurfill --maxkb 95 \
  "$SRC/real-african-grey-proven-breeder-with-eggs-for-sale-hen-nest-760.webp" \
  "$OUT/proven-african-grey-hen-on-nest-with-eggs.webp"
python3 scripts/reframe_og.py --style blurfill --maxkb 95 \
  "$SRC/breeding pair of african grey parrots for sale.jpg" \
  "$OUT/tame-hand-raised-african-grey-breeder-stock.webp"
python3 scripts/reframe_og.py --style blurfill --maxkb 95 \
  "$SRC/affordable-african-grey-parrot-shipping.jpg" \
  "$OUT/african-grey-breeding-pair-two-crate-shipping.webp"
python3 scripts/reframe_og.py --style blurfill --maxkb 95 \
  "$SRC/african-grey-parrot-eggs-in-incubator.webp" \
  "$OUT/candled-fertile-african-grey-eggs-incubator.webp"
python3 scripts/reframe_og.py --style blurfill --maxkb 95 \
  "$SRC/review-breeding-male-and-female-african-grey-parrots-for-sale.jpg" \
  "$OUT/breeder-review-african-grey-pair-arrived.webp"
```

Expected: 12 files, each under 95 KB.

- [ ] **Step 3: Confirm the 305 KB master came down**

```bash
cd /Users/apple/Downloads/CAG
ls -la public/images/breeding-pair/talker-jane-proven-african-grey-breeding-pair*.webp
```

Expected: both files under 97,280 bytes (95 KB). If not, re-run with `--maxkb 90`.

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add public/images/breeding-pair
git commit -m "feat(breeding-pair): bake 9 OG photos, blurfill portraits, all under 95KB"
```

---

## Task 3: Image Metadata Set

**Files:**
- Create: `sessions/2026-08-04-breeding-pair-image-metadata.md`

Rule 50b: the primary keyword goes in the **primary image's alt only**. Every other image rotates a
**different** keyword type. **No two images on the page share an alt.**

- [ ] **Step 1: Write the metadata table**

One row per baked figure, five columns, none optional: filename · alt · title · caption ·
description. The hero carries `african grey breeding pair for sale`; no other alt may contain that
exact string.

Assignment, from the prompt pack's own section map plus the Sprint 1 matrix:

| Figure | Section | Keyword type in alt |
|---|---|---|
| `hero-proven-african-grey-breeding-pairs-midland-texas` | §1 Hero | **primary** (only) |
| `talker-jane-proven-african-grey-breeding-pair` | §2 pair card | branded |
| `mari-lake-african-grey-breeding-pair-two-clutches` | §2 pair card | LSI |
| `sally-odin-youngest-proven-african-grey-pair` | §2 pair card | long-tail |
| `inf-1-what-proven-means` | §3 | conversational |
| `inf-2-price-ladder` | §4 | comparison |
| `inf-3-breeding-age-timeline` | §5 | long-tail |
| `proven-african-grey-hen-on-nest-with-eggs` | §6 | transactional |
| `tame-hand-raised-african-grey-breeder-stock` | §7 | solution |
| `inf-4-moving-a-pair` | §8 | conversational |
| `inf-5-pairing-method` | §9 | LSI |
| `inf-6-market-prices` | §10 | comparison |
| `inf-7-housing-nest-box` | §11 | long-tail |
| `african-grey-breeding-pair-two-crate-shipping` | §13 | geo |
| `candled-fertile-african-grey-eggs-incubator` | §14 | transactional |
| `breeder-review-african-grey-pair-arrived` | §16 | branded |

- [ ] **Step 2: Verify no duplicate alts**

After the page is written (Task 5+), this is checked mechanically in Task 10. Write the table now so
the build has one source to copy from.

- [ ] **Step 3: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add sessions/2026-08-04-breeding-pair-image-metadata.md
git commit -m "docs(breeding-pair): image metadata set, 16 figures, no duplicate alts"
```

---

## Task 4: Page Scaffold and Frontmatter

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro` (replaces the 3,881 B stub)
- Read: `src/pages/congo-african-grey-parrot-pair-for-sale/index.astro` — **for component and CSS
  structure only. Do not read its prose. Do not open it while writing paragraphs.**

- [ ] **Step 1: Read the stub before overwriting it**

```bash
cd /Users/apple/Downloads/CAG
cat src/pages/african-grey-breeding-pair-for-sale/index.astro
```

Record anything the stub already carries — canonical, existing schema, inbound-link anchors — so
nothing is silently dropped.

- [ ] **Step 2: Write the frontmatter with the approved meta**

Meta **Set 1 (Recommended)** from the blueprint §4, verbatim — Title 198 chars, Description 296 chars.
Set `hideGlobalCta` because the page ships its own reserve band (one-CTA rule).

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';

const title = 'Proven African Grey Breeding Pairs for Sale | Three Bonded Pairs, Seven Clutches on Record, From $3,000 | Closed-Banded, CITES Appendix I Captive-Bred | C.A.Gs — Midland, Texas Aviary Since 2014';
const description = 'Three proven African Grey breeding pairs for sale from our Midland, Texas aviary — Talker & Jane, Mari & Lake, Sally & Odin, from $3,000. Every pair is closed-banded with its clutch record on request, hand-reared and still tame, and ships in two crates. See what each pair has produced.';
const canonical = 'https://congoafricangreys.com/african-grey-breeding-pair-for-sale/';
---
```

- [ ] **Step 3: Verify the meta lengths against the caps**

```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
import re,pathlib
s = pathlib.Path('src/pages/african-grey-breeding-pair-for-sale/index.astro').read_text()
for k in ('title','description'):
    m = re.search(rf"const {k} = '(.*?)';\n", s, re.S)
    print(k, len(m.group(1)) if m else 'NOT FOUND')
PY
```

Expected: `title 198` (cap 205) · `description 296` (cap 300).

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-grey-breeding-pair-for-sale/index.astro
git commit -m "feat(breeding-pair): scaffold + approved meta set 1"
```

---

## Task 5: Sections 1–6 — Hero Through the Production Record

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro`

Component tuple is fixed by the blueprint §1 and is **not** a free choice:
**Hero-C refreshed "Production Ledger"** · **Dial 1 Clay wired to clutch record** · **Rail B green
ticker** · **T2 chip cloud refreshed to a standard checklist** · **K3 + K5** · **new Table H**.

- [ ] **Step 1: Build §1 Hero — Hero-C "Production Ledger" delta**

Stats strip reads *3 pairs · 7 clutches hatched · 12 yrs aviary*. Mosaic is **three pair tiles**, each
carrying a clutch chip. The palette does **not** change — a refresh alters arrangement, never brand
color. Hero image gets `fetchpriority="high"` + preload, never `loading="lazy"`.

- [ ] **Step 2: Build the three pair cards with near-transparent labels**

**This is the label rule, and it is a gate, not a preference.** The chip must not cover a head, face,
beak, or eyes.

```css
.pair-card { position: relative; border-radius: 16px; overflow: hidden; }
/* scrim carries the legibility so the chip itself can stay near-transparent */
.pair-card::after {
  content: ''; position: absolute; inset: auto 0 0 0; height: 42%;
  background: linear-gradient(to top, rgba(0,0,0,.45), rgba(0,0,0,0));
  pointer-events: none;
}
.pair-card .clutch-chip {
  position: absolute; left: 12px; bottom: 12px; z-index: 2;
  background: rgba(250,247,244,.22);
  backdrop-filter: blur(8px) saturate(120%);
  -webkit-backdrop-filter: blur(8px) saturate(120%);
  border: 1px solid rgba(255,255,255,.35);
  border-radius: 999px; padding: 5px 11px;
  color: #fff; font-size: .74rem; line-height: 1.25;
  text-shadow: 0 1px 2px rgba(0,0,0,.55);
}
```

Three hard constraints: fill alpha **≤ .28** · anchored **bottom-left**, never top-right · never
inside the upper 55% of the frame. Every card carries the shipping line
`Ships nationwide · $185 airport · $350 home` — never a card without it.

- [ ] **Step 3: Build §2 Key Takeaway (K3 Green Ledger + K5 Capsule), §3, §4, §5, §6**

Write each from the blueprint §3 outline. Every header is followed by a **conversational opening
paragraph** — never a list, table, or image directly under a header. EEBP under every header:
Entity → Evidence → Benefit → Purpose, first-person, 1–2 sentences.

§6 ships **Table H "Production Record"** — 3 pairs × ages / clutches / years proven / remaining
productive years / price. Do **not** reuse the letter F; it is already double-booked.

- [ ] **Step 4: Build and verify the sections render in `dist/`**

```bash
cd /Users/apple/Downloads/CAG
npx astro build 2>&1 | tail -5
grep -c "<h2" dist/african-grey-breeding-pair-for-sale/index.html
```

Expected: build succeeds; `<h2` count ≥ 5 at this stage.

- [ ] **Step 5: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-grey-breeding-pair-for-sale/index.astro
git commit -m "feat(breeding-pair): sections 1-6, hero ledger, 3 pair cards, table H"
```

---

## Task 6: Sections 7–14 — The Differentiators

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro`

These eight sections carry the page's moat. Sections 7, 8 and 9 are the **§7a counter-positions** —
each states the market's real failure, then attributes it to inexperience rather than inevitability.

- [ ] **Step 1: §7 Why Ours Are Tame (PAS)**

Tameness is **our first-hand account of our own birds**, never a species claim. The page still states
that breeder stock in general is untame — that is what makes ours notable. H6 breeder note carries
exactly that caveat.

- [ ] **Step 2: §8 Moving a Pair (PAS)**

States **method, never outcome**. We say we know how to move a producing pair; we never promise a
clutch. The H5 is literally *"Why We Never Promise a Clutch, and What We Do Promise."*

- [ ] **Step 3: §9 Why Random Pairing Fails (BAB), §10 Market Comparison (EEBP, K5)**

§10 publishes the competitor prices **with the reason in the same paragraph** — no discount framing,
no was/now. Our prices do not change.

- [ ] **Step 4: §11 Housing (GEO fact table), §12 Paperwork, §13 Travel, §14 Singles and Eggs**

§12 carries the **no-DNA-certificate statement** — these pairs are closed-banded with clutch history
on request. No DNA-sexed or DNA-certified claim about the pairs appears anywhere on the page.
§13 is **two crates, never one**. §14 is the step-down path, framed as fit, never as a lesser option.

- [ ] **Step 5: Verify the banned phrases are absent from the built page**

```bash
cd /Users/apple/Downloads/CAG
npx astro build >/dev/null 2>&1
for p in "5-6 years minimum" "5–6 years minimum" "DNA certified" "DNA-certified" "DNA sexed" "DNA-sexed" "Appendix II" "3-day"; do
  n=$(grep -ic "$p" dist/african-grey-breeding-pair-for-sale/index.html || true)
  printf "%-24s %s\n" "$p" "$n"
done
```

Expected: `0` on every line. Any non-zero is a blocking defect.

- [ ] **Step 6: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-grey-breeding-pair-for-sale/index.astro
git commit -m "feat(breeding-pair): sections 7-14, counter-positions, paperwork, travel"
```

---

## Task 7: The Checklist Tool (§15)

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro`

The approved tool is the **"Is This Pair Actually Proven?" six-question verification checklist**
(strategy §5). It works against *any* seller's listing, ours included — that is what makes it
linkable. The productive-years calculator was rejected: one tool per page.

- [ ] **Step 1: Write the six questions**

From the strategy doc verbatim: *Has this pair hatched a fertile clutch, and when? · How old is each
bird? · Are both closed-banded, and what are the numbers? · Can you see the clutch record? · Is the
pair sold together? · Will the seller state what happens if the pair stops producing after the move?*

- [ ] **Step 2: Implement in pure HTML/CSS + vanilla JS**

No frameworks, no dependencies, no external CDNs. A running score updates as boxes are ticked, with a
plain-language verdict band. Tap targets ≥ 24px with real spacing. Reserve explicit dimensions on the
result band so it cannot cause CLS.

- [ ] **Step 3: Verify it works in a painting page**

An occluded browser pane reads static — verify in Playwright, not in a pane.

```bash
cd /Users/apple/Downloads/CAG
npx astro build >/dev/null 2>&1 && npm run test:render:pages 2>&1 | tail -20
```

Expected: no new failures attributable to the checklist.

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-grey-breeding-pair-for-sale/index.astro
git commit -m "feat(breeding-pair): six-question proven-pair verification checklist"
```

---

## Task 8: Sections 16–19, Schema, and the Reserve Form

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro`

- [ ] **Step 1: §16 reviews, §17 keep-reading cards, §18 FAQ (FAQ-A refreshed)**

Reviews are **real named buyers only** — the asset is in the folder. Never fabricate a review, a
rating, or a count. Keep-reading cards carry **real** thumbnails, never placeholders. Exactly one
link out to Cluster E across the whole page.

- [ ] **Step 2: §19 Reserve band + form**

The form lists **all three pairs with their real prices**, plus available singles and fertile eggs,
plus delivery options including `Pickup in Midland, TX — if you live within 2–3 hours of us` alongside
the $185 / $350 tiers. Honest scarcity only: three pairs, stated as three. No countdowns.

- [ ] **Step 3: Write the JSON-LD**

One `Product` + `Offer` per real pair. `AggregateOffer` is for group and hub pages — **this page ships
three discrete products**, so use three `Product`/`Offer` blocks. A sold bird is never `InStock`.
Extend existing JSON-LD; never duplicate a block. Add `FAQPage` for §18.

- [ ] **Step 4: Verify schema in `dist/`, not in source**

```bash
cd /Users/apple/Downloads/CAG
npx astro build >/dev/null 2>&1
python3 - <<'PY'
import json, re, pathlib
h = pathlib.Path('dist/african-grey-breeding-pair-for-sale/index.html').read_text()
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
print('ld+json blocks:', len(blocks))
for b in blocks:
    try:
        d = json.loads(b)
    except Exception as e:
        print('  INVALID JSON:', e); continue
    for node in (d if isinstance(d, list) else [d]):
        print('  ', node.get('@type'), node.get('name', '')[:52])
print('InStock count:', h.count('InStock'))
PY
```

Expected: every block parses; types include three `Product` and one `FAQPage`; no duplicate `@type`
+ `name` pair; `InStock` appears only for genuinely available birds.

- [ ] **Step 5: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-grey-breeding-pair-for-sale/index.astro
git commit -m "feat(breeding-pair): reviews, FAQ, reserve form, Product+FAQPage schema"
```

---

## Task 9: Pre-Write Dup Gate — Body and Headers

**Files:**
- Read: `dist/african-grey-breeding-pair-for-sale/index.html`

**Dedup is a pre-write discipline, and this is the check on it.** A page copied and then reworded
passes this gate and still breaks the rule. If this gate flags crossover, the fix is to **rewrite from
the outline**, never to reword until the score drops.

- [ ] **Step 1: Run the body dup audit**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/dup_content_audit.py 2>&1 | tail -40
```

Expected: zero non-whitelist crossover against every sibling. Whitelist: the shipping line,
documentation badge lists, the counter strip, the CITES notice, CTA labels, real reviews, real
page-name link labels. **Nothing else.**

- [ ] **Step 2: Run the header dup audit**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/dup_content_audit.py --headers 2>&1 | tail -40
```

Expected: zero exact or template crossover. The sibling
`/congo-african-grey-parrot-pair-for-sale/` owns *bonded · companion · introduced · settle · routes*;
this page owns *proven · hatched · clutch · nest box · breeder stock · production*.

- [ ] **Step 3: Run both a second time**

One clean run proves nothing — the same input has produced different verdicts on this site.

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/dup_content_audit.py 2>&1 | tail -5
python3 scripts/dup_content_audit.py --headers 2>&1 | tail -5
```

Expected: identical verdicts to Steps 1–2. A differing verdict is a harness defect — file it, do not
edit the page.

- [ ] **Step 4: Commit any rewrites**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-grey-breeding-pair-for-sale/index.astro
git commit -m "fix(breeding-pair): dup gate — rewrite crossover from outline"
```

---

## Task 10: Keyword, Entity and Image-Alt Verification

**Files:**
- Read: `dist/african-grey-breeding-pair-for-sale/index.html`
- Create: `sessions/2026-08-04-breeding-pair-keyword-metrics.md`

- [ ] **Step 1: Measure the seven §6a metrics on the built page**

```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
import re, pathlib, collections
h = pathlib.Path('dist/african-grey-breeding-pair-for-sale/index.html').read_text()
text = re.sub(r'<[^>]+>', ' ', h)
words = re.findall(r"[a-z']+", text.lower())
prim = 'african grey breeding pair'
low = ' '.join(words)
print('rendered words       :', len(words))
print('primary mentions     :', low.count(prim))
print('first-100 has primary:', prim in ' '.join(words[:100]))
alts = re.findall(r'alt="([^"]*)"', h)
dupes = [a for a, c in collections.Counter(alts).items() if c > 1 and a.strip()]
print('images               :', len(alts))
print('DUPLICATE ALTS       :', dupes or 'none')
print('alts w/ primary kw   :', sum(1 for a in alts if prim in a.lower()), '(must be 1)')
for lvl in range(1, 7):
    print(f'h{lvl}:', len(re.findall(rf'<h{lvl}[ >]', h)), end='  ')
print()
PY
```

Expected: rendered words ≈ 6,200 · primary in first 100 words `True` · **no duplicate alts** · exactly
**1** alt containing the primary keyword · H5 ≥ 5 and H6 ≥ 5, no level at zero.

- [ ] **Step 2: Record the metric table**

Write ours vs each top-5 competitor for all seven §6a metrics into the session file. Report each as a
number. A metric you did not measure is written `NOT FETCHED`, never estimated.

- [ ] **Step 3: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add sessions/2026-08-04-breeding-pair-keyword-metrics.md
git commit -m "docs(breeding-pair): keyword + entity metric table vs top-5"
```

---

## Task 11: Sprint 3 — Harden Pass

**Files:**
- Modify: `src/pages/african-grey-breeding-pair-for-sale/index.astro`

Its own sprint. Not folded into build, not folded into gates. **`/impeccable` and `/frontend-design`
run here** — on a finished page, never on a half-built one.

- [ ] **Step 1: Run the hardening scan**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/page_hardening_scan.py african-grey-breeding-pair-for-sale 2>&1 | tail -40
```

- [ ] **Step 2: Verify each finding on the built page before editing anything**

A gate's output is a hypothesis about the page, not a fact about it. Twelve checkers have cried wolf
here. Open `dist/` and confirm the defect exists before changing a line.

- [ ] **Step 3: Class-diff every ported section against its source component**

A clean hardening scan is not a clean page — markup↔CSS drift passes scans silently.

- [ ] **Step 4: Verify the responsive contract at 375 / 768 / 1280**

```bash
cd /Users/apple/Downloads/CAG
npm run test:render:pages 2>&1 | tail -30
```

Checklist: no oversized headers, H2 clamps down on mobile · nothing cut off at any edge · no
horizontal scroll at any width · tables stack one card per row ≤ 640px with `data-label` on every
`td`, never a `::before` on `<tr>` · seam gutters −40% on mobile · tap targets ≥ 24px ·
`scroll-behavior: auto` with `--hdr` and matching `scroll-margin-top` on every jump target.

- [ ] **Step 5: Contrast audit**

Floors: stone-600 body · small clay on light `#b04228` · clay on dark `#f08070` · footer on green
`white/80` minimum · **no opacity-based dimming for text**. The 1.19:1 mechanism comes from a losing
specificity battle, not a wrong token — check specificity, not just the value.

Re-verify the pair-card chip from Task 5 Step 2: alpha ≤ .28, and the white label text still clears AA
against the scrim beneath it.

- [ ] **Step 6: `/impeccable` + `/frontend-design` polish pass**

Visual hierarchy, information architecture, cognitive load, spacing, alignment, motion,
micro-interactions, UX copy, error and empty states. Equal heights and equal widths across every card
row. Rounded, crisp, modern. Nothing may feel roughed at any of the three widths.

- [ ] **Step 7: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-grey-breeding-pair-for-sale/index.astro
git commit -m "polish(breeding-pair): sprint 3 harden — contrast, responsive, impeccable pass"
```

---

## Task 12: Sprint 4 — Gates

**Files:**
- Read: `dist/`

- [ ] **Step 1: Meta gate FIRST — it is the gate that checks the checkers**

```bash
cd /Users/apple/Downloads/CAG
npm run test:render:meta 2>&1 | tail -30
```

Expected: PASS. Do not trust any page result until this passes.

- [ ] **Step 2: Render pages, quality report, final audit, AEO**

```bash
cd /Users/apple/Downloads/CAG
npm run test:render:pages 2>&1 | tail -30
python3 scripts/quality_report.py 2>&1 | tail -40
python3 scripts/final_page_audit.py 2>&1 | tail -40
python3 scripts/aeo_audit.py african-grey-breeding-pair-for-sale 2>&1 | tail -30
```

- [ ] **Step 3: Read each gate's examined count before believing any PASS**

A PASS over zero items is not a PASS. Two checkers on this site have reported PASS having examined
zero pages. Record the examined count for each gate in the session brief.

- [ ] **Step 4: Run every gate a second time**

```bash
cd /Users/apple/Downloads/CAG
npm run test:render:meta 2>&1 | tail -5
npm run test:render:pages 2>&1 | tail -5
python3 scripts/final_page_audit.py 2>&1 | tail -5
```

Expected: verdicts identical to Step 2. A differing verdict is a harness defect.

- [ ] **Step 5: Work the manual pass list**

400px-class hero · unique newsletter image and one-line title, never shared with a sibling · opening
paragraph under **every** header · uniform OG boxes throughout · separate blog and contact H2s ·
mobile table stacking · jump links actually jump · further-reading cards with real thumbnails · seam
count matches section count · schema verified in `dist/` · no visible dates in body copy
(schema-only freshness) · all six heading levels with ≥5 H5 and ≥5 H6 · Lighthouse warm median-of-3 ·
verified in `dist/`, never by grepping source.

- [ ] **Step 6: If a defect escaped a gate that should have caught it — fix the harness, not the page**

Add the case to `tests/render/fixtures/known_broken/`, watch the meta gate fail, fix the check, and
write **no new rule**.

- [ ] **Step 7: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add -u
git commit -m "fix(breeding-pair): sprint 4 gate findings, verified on built page"
```

---

## Task 13: Sprint 5 — LLM Visibility

**Files:**
- Create: `sessions/2026-08-04-breeding-pair-llm-visibility.md`

Mandatory, not optional.

- [ ] **Step 1: Query five engines on the primary keyword + top 5 variations**

ChatGPT · Claude · Gemini · Perplexity · Google AIO. Record per engine: cited or not · which URL ·
position in the answer · which competitors are cited instead · what phrasing the answer uses.

- [ ] **Step 2: Extract the answer structure and the engine-keyword gap**

The structure each engine returns **is** the AEO target. List the keywords the engines use that our
page does not contain.

- [ ] **Step 3: Score and route**

Produce the LLM Visibility score. Route: missing keywords → keyword verifier · missing questions →
FAQ builder · missing structure → AIO/GEO framework.

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add sessions/2026-08-04-breeding-pair-llm-visibility.md
git commit -m "docs(breeding-pair): LLM visibility baseline, 5 engines x 6 queries"
```

---

## Task 14: Sprint 6 — Deploy and Close

- [ ] **Step 1: Build and verify the built page one final time**

```bash
cd /Users/apple/Downloads/CAG
npx astro build 2>&1 | tail -5
ls -la dist/african-grey-breeding-pair-for-sale/index.html
```

Expected: build succeeds, `index.html` present and substantially larger than the 3,881 B stub.

- [ ] **Step 2: Regenerate sitemaps**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/generate_sitemaps.py
```

- [ ] **Step 3: Commit and push — push IS deploy, on `main` only**

```bash
cd /Users/apple/Downloads/CAG
git status --short
git add -A
git commit -m "feat(breeding-pair): ship /african-grey-breeding-pair-for-sale/ — 19 sections, 3 proven pairs"
git push origin main
```

- [ ] **Step 4: Confirm live 200 and one-hop redirects**

```bash
curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -L \
  https://congoafricangreys.com/african-grey-breeding-pair-for-sale/
```

Expected: `200` at the canonical URL. Allow a few minutes for the Actions → Cloudflare Pages deploy.

- [ ] **Step 5: Submit to IndexNow, write the lessons doc, update memory**

The lessons doc records what broke, the root cause, and the reusable fix. Update the session brief's
*What's Next*. Save durable non-obvious findings to memory — in particular the infographic
duplicate-label failure mode from Task 0, which is now the second instance of this class.

- [ ] **Step 6: Commit the close-out**

```bash
cd /Users/apple/Downloads/CAG
git add sessions docs/reference/session-log.md
git commit -m "docs(breeding-pair): lessons doc + session close"
git push origin main
```

---

## Definition of Done

- [ ] All 7 infographics clean, all 16 figures baked under 95 KB with `-760` siblings
- [ ] 19 sections, ~6,200 words, all six heading levels, ≥5 H5, ≥5 H6, no skipped level
- [ ] Opening paragraph under every header; no duplicate alts; exactly one alt with the primary keyword
- [ ] Dup gate clean, body **and** `--headers`, run twice
- [ ] Every gate run twice with its examined count recorded
- [ ] Verified at 375 / 768 / 1280 on the **built** page
- [ ] Schema valid in `dist/` — three `Product`/`Offer` + `FAQPage`, no false `InStock`
- [ ] Live HTTP 200 on `main`, sitemaps regenerated, IndexNow submitted
- [ ] Lessons doc written, memory updated

## Out of Scope

Sprints 0 / 0.5 / 1 are signed off and are not re-opened. The URL and redirect map are settled — no
slug changes. Prices do not change. No sibling page is edited. No new brand method label is invented
(there are exactly two). No second interactive tool.

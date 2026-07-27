# /african-grey-parrot-adoption-cost/ Rebuild — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended)
> or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax
> for tracking.

**Goal:** Rebuild the thin 331-line interior page at `/african-grey-parrot-adoption-cost/` into a
5,300–7,000-word transactional for-sale page that owns the day-one acquisition-cost decision, ships a
site-first True-Cost Calculator, and counter-positions rather than chases the India price query.

**Architecture:** Single Astro page at `src/pages/african-grey-parrot-adoption-cost/index.astro` with a
page-scoped `<style>` block under a `.adopt` root class, following the for-sale kit at
`assets/1WORKING-ON/FOR-SALE-PAGES/`. Components come from the kit (Split-Hero C, Dial 1, Rail B, T2
Chip Cloud, K2/K4, Avail-B, FAQ-C, `.fs-nl`, `.xsell`, seam emblem); three are new to the cluster —
Table G "True-Cost Ledger", the `fs-nl ledger` newsletter variant, and the `.cost-tool` calculator.
All prose is written fresh from the approved H1–H6 outline; no sibling body copy is opened.

**Tech Stack:** Astro 4 · vanilla JS (IntersectionObserver scroll-spy, calculator, Avail-B filter) ·
JSON-LD · Pillow for image processing · Gemini via `scripts/generate_nb_image.sh`.

**Source of truth for every prompt, spec and image:**
`sessions/for-sale-research/african-grey-parrot-adoption-cost/2026-07-27-adoption-cost-prompt-pack.md`

---

## File Structure

| Path | Responsibility |
|---|---|
| `src/pages/african-grey-parrot-adoption-cost/index.astro` | The page. Replaced wholesale. Frontmatter reads the three JSON data files, builds the schema graph, and interpolates the calculator constants. |
| `sessions/2026-07-27-adoption-cost-sprint0-research.md` | Sprint 0 output. Created by Task 1. |
| `sessions/2026-07-27-adoption-cost-sprint1-blueprint.md` | Strategy, distribution matrix, approved outline. Created by Task 2. |
| `sessions/2026-07-27-session-brief.md` | Live brief. Carries `## Open Flags` for the Clarification Checkpoint. |
| `public/*.webp` | 8 processed OG photos + 8 generated infographics + `-760.webp` siblings. |
| `data/financial-entities.json`, `data/price-matrix.json` | Gain a comment noting this page renders their figures, so a price edit knows to rebuild. |
| `sessions/2026-07-19-for-sale-component-map.md` | Gains one tuple-ledger row at Task 10. |
| `docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md` | Gains the anchors this page spends, at Task 10. |
| `scripts/final_page_audit.py` | Already lists the slug in the FORSALE roster at line 368. No edit needed — verify only. |

---

## Task 1: Sprint 0 research

**Files:**
- Create: `sessions/2026-07-27-adoption-cost-sprint0-research.md`

- [ ] **Step 1: Confirm branch and clean build**

```bash
cd /Users/apple/Downloads/CAG && git checkout main && git pull && npx astro build
```

Expected: build completes, no errors.

- [ ] **Step 2: Fire PROMPT 1 from the pack**

Copy `## 1. GLOBAL PREPEND`, then `PROMPT 1` from section 3, then `## 2. GLOBAL APPEND`, out of
`sessions/for-sale-research/african-grey-parrot-adoption-cost/2026-07-27-adoption-cost-prompt-pack.md`.

- [ ] **Step 3: Verify the India figures independently before accepting the research**

```bash
grep -i "india" assets/1WORKING-ON/FOR-SALE-PAGES/GSC-extracted/Queries.csv
grep -i "^India," assets/1WORKING-ON/FOR-SALE-PAGES/GSC-extracted/Countries.csv
```

Expected: `african grey parrot price in india,0,43,0%,1` plus two lower-volume variants, and the
country row. If the research file reports different numbers, the research is wrong, not the CSV.

- [ ] **Step 4: Verify the tool gap claim**

```bash
grep -rl "calculator" src/pages/ | wc -l
```

Expected: `0`. This is the evidence line the page's moat rests on — if it ever returns non-zero,
the calculator is no longer a site-first and the blueprint must say so.

- [ ] **Step 5: Commit the research**

```bash
git add sessions/2026-07-27-adoption-cost-sprint0-research.md
git commit -m "docs(adoption-cost): Sprint 0 research — dual price/adoption intent, India negative, tool gap"
git push origin main
```

---

## Task 2: Sprint 1 blueprint and distribution matrix

**Files:**
- Create: `sessions/2026-07-27-adoption-cost-sprint1-blueprint.md`

- [ ] **Step 1: Fire PROMPT 2 from the pack** (PREPEND + PROMPT 2 + APPEND)

- [ ] **Step 2: Verify the component tuple is genuinely unused**

```bash
grep -n "Split-Hero C\|Dial 1\|Rail B\|T2 Chip\|K2 \|K4 \|Table G" sessions/2026-07-19-for-sale-component-map.md
```

Expected: `Split-Hero C + Dial 1 + Rail A` appears for the egg page and nowhere else; `Rail B` appears
for timneh and hand-raised but never with Split-Hero C; `T2 Chip Cloud` and `Table G` appear nowhere.
If any line contradicts the pack, the ledger wins — re-pick and record why.

- [ ] **Step 3: Present two strategies plus one blended, with exactly one marked (Recommended)**

Each carries a data-grounded why and its named trade-off. Wait for the breeder's pick.

- [ ] **Step 4: Commit the blueprint**

```bash
git add sessions/2026-07-27-adoption-cost-sprint1-blueprint.md
git commit -m "docs(adoption-cost): Sprint 1 blueprint — angle, 22-section matrix, tuple, keyword split"
git push origin main
```

---

## Task 3: Heading Outline Gate — HARD STOP

**Files:** none written. This task produces an outline for approval only.

- [ ] **Step 1: Fire PROMPT 3 from the pack** (PREPEND + PROMPT 3 + APPEND)

- [ ] **Step 2: Self-check the outline mechanically before showing it**

Count the levels by hand against these four rules, all hard failures:
all six levels present · no skipped levels · at least 5 H5 · at least 5 H6.

- [ ] **Step 3: Run the pre-write header dup gate**

```bash
python3 scripts/dup_content_audit.py --headers
```

Expected: zero non-whitelist crossover involving the proposed headers. Note that three headings cleared
this same gate on the health-guarantee build and still collided once built — Task 9 runs it again on
the built page, and that run is the one that counts.

- [ ] **Step 4: Get explicit breeder approval. Do not proceed without it.**

Per CLAUDE.md, no page code is touched until the outline is approved.

---

## Task 4: OG photo processing

**Files:**
- Create: 8 files in `public/` plus their `-760.webp` siblings, per pack §4.

- [ ] **Step 1: Confirm every master is on disk at the stated size**

```bash
python3 - <<'PY'
from PIL import Image
import os
masters = [
 "assets/brand/hero-available-grey-parrots.webp",
 "assets/brand/Roys/What's included with Roys?.webp",
 "assets/brand/AMIE/amie-african-grey-family-long-term.webp",
 "assets/1WORKING-ON/FOR-SALE-PAGES/CONGOS-For-Sale/living-with-a-congo-african-grey-family-lifestyle.webp",
 "assets/brand/BERY/mix-veggetables-for-parrot.webp",
 "assets/brand/BERY/parrot-toy.webp",
 "assets/1WORKING-ON/FOR-SALE-PAGES/CONGOS-For-Sale/Mark-with the parrots.jpg",
 "assets/brand/BERY/bery-first-30-days-home.webp",
]
for m in masters:
    print("OK " if os.path.isfile(m) else "MISSING ", Image.open(m).size if os.path.isfile(m) else "", m)
PY
```

Expected: 8 × `OK` with the sizes recorded in pack §4.

- [ ] **Step 2: Confirm no target filename is already taken**

```bash
for n in african-greys-available-price-bands what-the-african-grey-price-covers-roys \
         african-grey-forty-year-family-commitment living-with-an-african-grey-running-costs \
         african-grey-fresh-produce-annual-food-cost african-grey-toy-replacement-cost \
         mark-benjamin-aviary-overhead-midland-tx african-grey-first-thirty-days-setup-cost; do
  printf "%-48s -> " "$n"; ls public/ | grep -c "^$n" ; done
```

Expected: `0` on every line.

- [ ] **Step 3: Process OG-1 through OG-7 (landscape and square) with a cover fit**

```bash
python3 - <<'PY'
from PIL import Image, ImageOps
jobs = [
 ("assets/brand/hero-available-grey-parrots.webp", "african-greys-available-price-bands", (0.5, 0.42)),
 ("assets/brand/Roys/What's included with Roys?.webp", "what-the-african-grey-price-covers-roys", (0.5, 0.45)),
 ("assets/brand/AMIE/amie-african-grey-family-long-term.webp", "african-grey-forty-year-family-commitment", (0.5, 0.5)),
 ("assets/1WORKING-ON/FOR-SALE-PAGES/CONGOS-For-Sale/living-with-a-congo-african-grey-family-lifestyle.webp", "living-with-an-african-grey-running-costs", (0.5, 0.5)),
 ("assets/brand/BERY/mix-veggetables-for-parrot.webp", "african-grey-fresh-produce-annual-food-cost", (0.5, 0.5)),
 ("assets/brand/BERY/parrot-toy.webp", "african-grey-toy-replacement-cost", (0.5, 0.5)),
 ("assets/1WORKING-ON/FOR-SALE-PAGES/CONGOS-For-Sale/Mark-with the parrots.jpg", "mark-benjamin-aviary-overhead-midland-tx", (0.5, 0.4)),
]
for src, name, centering in jobs:
    im = Image.open(src).convert("RGB")
    for w, h, suffix in ((1408, 768, ""), (760, 415, "-760")):
        out = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=centering)
        for q in range(82, 53, -4):
            out.save(f"public/{name}{suffix}.webp", "WEBP", method=6, quality=q)
            import os
            if os.path.getsize(f"public/{name}{suffix}.webp") < 95_000:
                break
        print(f"{name}{suffix}.webp  q={q}  {os.path.getsize(f'public/{name}{suffix}.webp')//1024}KB")
PY
```

Expected: 14 files written, every one under 95 KB.

- [ ] **Step 4: Process OG-8 (portrait) with blurfill, never a cover crop**

```bash
python3 scripts/reframe_og.py --style blurfill --mobcrop 4:5 \
  "assets/brand/BERY/bery-first-30-days-home.webp" \
  public/african-grey-first-thirty-days-setup-cost.webp
```

Expected: a 1408×768 blurfilled file plus its mobile 4:5 rung. A portrait cover-cropped into 16:9 cuts
the bird's head off — that is exactly what this step exists to prevent.

- [ ] **Step 5: Commit**

```bash
git add public/african-greys-available-price-bands*.webp public/what-the-african-grey-price-covers-roys*.webp \
        public/african-grey-forty-year-family-commitment*.webp public/living-with-an-african-grey-running-costs*.webp \
        public/african-grey-fresh-produce-annual-food-cost*.webp public/african-grey-toy-replacement-cost*.webp \
        public/mark-benjamin-aviary-overhead-midland-tx*.webp public/african-grey-first-thirty-days-setup-cost*.webp
git commit -m "feat(adoption-cost): process 8 OG photos into the uniform 16:9 box"
git push origin main
```

---

## Task 5: Infographic generation

**Files:**
- Create: 8 files in `public/` plus `-760.webp` siblings, per pack §7.

- [ ] **Step 1: Run the collision check from pack §7a**

```bash
ls public/ | grep -iE "cost|price|fee|adopt|rescue|route|marketplace|iceberg|receipt|ledger|decade|delivery-option"
```

Expected: the six known existing names listed in §7a and none of the eight new ones. If a new name is
occupied, rename and re-angle rather than shipping a near-duplicate.

- [ ] **Step 2: Generate all eight**

Fire PROMPT 4 from the pack, then run each §7c prompt with its NEGATIVE appended:

```bash
bash scripts/generate_nb_image.sh "<PROMPT + NEGATIVE>" "african-grey-adoption-fee-vs-true-cost-iceberg.png" "1600x900"
```

Repeat for INF-2 through INF-8 using the filenames in §7c.

- [ ] **Step 3: Post-process each to the uniform box**

Same quality-walk as Task 4 Step 3, target under 95 KB, plus the `-760.webp` sibling.

- [ ] **Step 4: Proof every word rendered inside an image**

Open each file and read the labels. A misspelled word inside an image cannot be fixed by an edit — it
has to be regenerated, so catch it now.

- [ ] **Step 5: Commit**

```bash
git add public/african-grey-adoption-fee-vs-true-cost-iceberg*.webp public/african-grey-day-one-money-breakdown*.webp \
        public/african-grey-cost-by-acquisition-route-stacked*.webp public/african-grey-five-year-cost-curve*.webp \
        public/what-a-cheap-african-grey-really-costs*.webp public/adoption-cost-african-grey-delivery-options*.webp \
        public/what-an-adoption-fee-does-not-cover*.webp public/african-grey-cost-by-decade-forty-year-timeline*.webp
git commit -m "feat(adoption-cost): 8 new infographics — iceberg, day-one receipt, route stacking, 5-yr curve"
git push origin main
```

---

## Task 6: Build the page shell, hero and navigation

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro` (replace all 331 lines)

- [ ] **Step 1: Read the kit before writing anything**

```bash
cat "assets/1WORKING-ON/FOR-SALE-PAGES/FOR-SALE-PAGES:components-NAMES.md"
```

Then open `assets/1WORKING-ON/FOR-SALE-PAGES/component-designs/Variant C · Dark with photo grid.png`.
Never import `NewsletterV2`, the comparison hero, the green comparison counter strip, or the comparison
circular-emblem seam onto a for-sale page.

- [ ] **Step 2: Frontmatter — read data, build schema, interpolate calculator constants**

Read `data/clutch-inventory.json`, `data/price-matrix.json` and `data/financial-entities.json` in the
frontmatter. Filter birds to `status === "available"`. Emit one `Product` + `Offer` per available bird.
Do not emit `AggregateOffer` — this is not a hub page. Do not emit a second `BreadcrumbList`;
`<Breadcrumb />` emits its own.

- [ ] **Step 3: Split-Hero C dark with the 2×2 price-ladder grid**

Tiles in ascending price order per pack §4: Evie `$1,500` · Bery `$1,700` · Roys `$2,300` ·
Jins & Jeni `$3,500`. Prices interpolated from `clutch-inventory.json`, never typed. Hero height in the
~400px class. Hero images baked with a plain cover fit — blurfill on a hero produces a small photo
floating in a blurred field.

- [ ] **Step 4: Counter strip — for-sale outlined stat cards on cream**

The eight snippets from pack §0/§9. `min-height: 66px`, padding `10px 13px`, radius 12px, serif number
`1.35rem`. Reserve the height so the strip cannot shift.

- [ ] **Step 5: Dial 1 Clay Progress with a working scroll-spy**

Compact spec from the pack: 196px sidebar, `grid 196px minmax(0,1fr); gap:28px`, plain `#fff` card,
radius 16px, 64px ring. An IntersectionObserver updates `--p`, highlights the active dial and rail item,
and updates the `x of N` counter. A static ring reads as broken.

- [ ] **Step 6: Rail B green ticker on mobile**

Sticky, snap-scroll, `scroll-margin` offset on every target, and `scroll-behavior: auto` — `smooth`
cancels `#anchor` navigation outright.

- [ ] **Step 7: Verify the hero in the browser, not in source**

```bash
npx astro build && npx astro preview --port 4321
```

Then load `http://localhost:4321/african-grey-parrot-adoption-cost/` in the Browser pane, screenshot at
360px and 1280px, and confirm the dial ring advances on scroll.

- [ ] **Step 8: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "feat(adoption-cost): Split-Hero C price ladder, counter strip, Dial 1 + Rail B"
git push origin main
```

---

## Task 7: Build the body sections

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro`

- [ ] **Step 1: Fire PROMPT 5 from the pack** (PREPEND + PROMPT 5 + APPEND)

- [ ] **Step 2: Write each section from the approved outline, one movement at a time**

Every H2, H3 and H4 opens with an EFBP paragraph — Entity + Feature + Benefit + Purpose, one or two
sentences, first person. Never open a sibling page's body copy while writing.

- [ ] **Step 3: Place the seam emblem before every section**

```bash
echo "seams=$(grep -c 'class="seam"' src/pages/african-grey-parrot-adoption-cost/index.astro) sections=$(grep -c '<section class="sec"' src/pages/african-grey-parrot-adoption-cost/index.astro)"
```

Expected: the two numbers match. House idiom is one seam before every section; the health-guarantee page
shipped 7 across 17 and read as unfinished.

- [ ] **Step 4: Run the anti-AI pass on your own draft before calling any section done**

Load `skills/anti-ai-writing.md` and sweep the draft against the blacklist.

- [ ] **Step 5: Commit per movement**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro
git commit -m "feat(adoption-cost): body sections — routes, day-one, running costs, lifetime"
git push origin main
```

---

## Task 8: The three new components

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro`
- Modify: `data/financial-entities.json`, `data/price-matrix.json` (comment only)

- [ ] **Step 1: Table G "True-Cost Ledger"**

Rows Day One / Year One / Five Year. Columns Rescue-fee route / C.A.Gs breeder route / Sub-floor listing
route, plus a "what this route does not cover" spine. Max 6 columns. Stacks to one card per row at
≤640px with `data-label` on each `td`, `thead` clip-hidden, first cell as a header band. Never put a
`::before` on a `<tr>` — it shifts the columns.

- [ ] **Step 2: `.cost-tool` True-Cost Calculator, per pack §6**

Constants interpolated from the JSON in the frontmatter — never retyped. Result panel carries a fixed
`min-height` from first paint. `aria-live="polite"` on the result panel. Every figure renders as a range.
The same numbers also exist as static text and a real `<table>` elsewhere on the page, because answer
engines cannot execute JavaScript.

- [ ] **Step 3: Note the dependency in the data files**

Add to `data/financial-entities.json` and `data/price-matrix.json`, at the top level:

```json
"renders_on": ["/african-grey-parrot-adoption-cost/ — True-Cost Calculator constants are interpolated at build time; rebuild after any price edit"]
```

- [ ] **Step 4: `fs-nl ledger` newsletter, per pack §5**

Mid-page, immediately after Table G. Perforated clay left edge, four price-band chips as real
`<button type="button">` with `aria-pressed`, email input plus a clay pill submit at `border-radius:12px`.
Full border, background tint, **never a side stripe**. Reserved `min-height`. Unique image — INF-2
cropped to the card.

- [ ] **Step 5: Verify the calculator does not shift layout**

```bash
npx --yes lighthouse@12 http://localhost:4321/african-grey-parrot-adoption-cost/ \
  --only-audits=cumulative-layout-shift --form-factor=mobile --screenEmulation.mobile \
  --throttling-method=simulate --output=json --quiet --chrome-flags="--headless=new" 2>/dev/null \
  | python3 -c "import json,sys;print('%.3f'%json.load(sys.stdin)['audits']['cumulative-layout-shift']['numericValue'])"
```

Run it **five times** and read the distribution. CLS on this site is bimodal; a single run already
produced one confident wrong attribution. Expected: every run under 0.1.

- [ ] **Step 6: Commit**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro data/financial-entities.json data/price-matrix.json
git commit -m "feat(adoption-cost): Table G ledger, .cost-tool calculator, fs-nl ledger newsletter"
git push origin main
```

---

## Task 9: Closing sections and the final gate

**Files:**
- Modify: `src/pages/african-grey-parrot-adoption-cost/index.astro`

- [ ] **Step 1: Avail-B faceted by price band**

Bands `$1,500–1,699` / `$1,700–2,299` / `$2,300–2,599` / `$3,500 pair`, live counts from
`clutch-inventory.json`. Cards use the Avail-C v2 clean-card spec with `-440.webp` siblings and
`sizes="(max-width:980px) 46vw, 210px"`.

- [ ] **Step 2: FAQ-C dark refreshed to a ledger register with a clay `$` chip**

Questions live in `<summary>` and stay conversational sentence case. Answers are visible in the DOM and
match the FAQPage JSON-LD exactly. Cap the answers — they inherit `max-width: none`.

- [ ] **Step 3: Shipping block, read-cards, `.xsell`, contact form**

Shipping: `$185` airport, `$350` home, `from $750` flight nanny, plus Midland TX pickup within 2–3 hours,
linking the six geo pages. Read-cards use a `-320.webp` thumbnail rung via a named helper:

```js
const thumb = (p) => p.replace(/(-760)?\.webp$/, "-320.webp");
```

`.xsell` sits at the end of the reading section so it never triggers the Heading Outline Gate. Contact
form lists every reservable bird with its price and offers the Midland pickup option.

- [ ] **Step 4: Fire PROMPT 6 from the pack and run every gate**

```bash
npx astro build
python3 scripts/page_hardening_scan.py african-grey-parrot-adoption-cost
python3 scripts/dup_content_audit.py african-grey-parrot-adoption-cost
python3 scripts/dup_content_audit.py --headers african-grey-parrot-adoption-cost
python3 scripts/final_page_audit.py
python3 -m pytest tests/ -q
bash scripts/health-sweep.sh
python3 scripts/generate_sitemaps.py
```

Expected: hardening scan clean on all six checks; zero non-whitelist dup crossover; `final_page_audit.py`
PASS with word count between 3,000 and 8,000 and ideally 5,300–7,000.

- [ ] **Step 5: Verify every finding before you fix anything**

Four checkers reported false defects on 2026-07-26 and fixing the pages would have degraded correct code.
Open the flagged rule and confirm the defect is real. If the check is wrong, fix the check and add a
regression test.

- [ ] **Step 6: Measure, do not assume**

Real-`ch` probe from `skills/cag-page-hardening.md` §2y — measure a real `ch` by rendering `"0"` in the
element's own computed font, never `fontSize * 0.5`. Open `<details>` first. Filter on `> 75` at mobile.
Overflow probe at 360 / 768 / 820 / 1024 / 1280, on this page **and** the homepage.

- [ ] **Step 7: Commit and deploy**

```bash
git add src/pages/african-grey-parrot-adoption-cost/index.astro public/sitemap*.xml
git commit -m "feat(for-sale): rebuild /african-grey-parrot-adoption-cost/ — page 8 of 22"
git push origin main
curl -s -o /dev/null -w "%{http_code}\n" https://congoafricangreys.com/african-grey-parrot-adoption-cost/
```

Expected: `200`.

---

## Task 10: Update the ledgers and close the session

**Files:**
- Modify: `sessions/2026-07-19-for-sale-component-map.md`
- Modify: `docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md`

- [ ] **Step 1: Add the tuple row**

Append a row to the per-page assignment table recording: Split-Hero C dark price ladder · Dial 1 Clay +
Rail B green ticker · T2 Chip Cloud (first use) · K2 Price-Tag + K4 Clipboard · Table G True-Cost Ledger
+ Table A · FAQ-C ledger register · Avail-B by price band · angle "The Fee Is Not the Cost." ·
EEBP × Setup-Stat-Reframe × 5 Basic Objections × QAB · geo NJ/MA/MN/MO/OR/IN · the seam and CTA counts ·
and the dup-gate result.

- [ ] **Step 2: Add the anchors this page spent to the Anchor Diversity Ledger**

Append every anchor used for `/african-grey-parrot-bird-eggs-for-sale-usa/`,
`/african-grey-breeding-pair-for-sale/` and `/congo-african-grey-parrot-pair-for-sale/` so the next page
cannot collide.

- [ ] **Step 3: Run the session-closer skill and commit**

```bash
git add sessions/2026-07-19-for-sale-component-map.md docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md sessions/2026-07-27-session-brief.md
git commit -m "docs(session): close the adoption-cost build — tuple ledger, anchors, What's Next"
git push origin main
```

---

## Self-Review

**Spec coverage.** Every element the breeder named has a task: Split-Hero C (Task 6 Step 3), the India
negative (Task 1 Steps 2–3, and an H4 placed in Task 3), the 6+ OG images (Task 4, eight of them), the
mid-page newsletter as a new variant (Task 8 Step 4), and the special-element calculator (Task 8 Step 2).
The full workflow is covered end to end: Sprint 0 research → Sprint 1 matrix → outline gate → images →
build → QA → deploy → ledger update.

**Placeholder scan.** No TBDs. Every code step carries runnable code, every command carries its expected
output. The three items intentionally left open are named in pack §8 with a default for each, so the
build never stalls waiting on them.

**Type consistency.** `.cost-tool`, `fs-nl ledger`, `Table G`, `.xsell`, `.sec-img.inf-img`,
`.sec-img.og-tall`, `Avail-B` and `Avail-C v2` are used with the same names in this plan and in the
prompt pack. Filenames in Task 4 Step 3 match pack §4 exactly; filenames in Task 5 Step 5 match §7c
exactly.

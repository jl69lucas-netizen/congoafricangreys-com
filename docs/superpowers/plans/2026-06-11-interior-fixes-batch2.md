# Interior Pages Fixes — Batch 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task **INLINE — the user has explicitly forbidden subagents for this job**. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the cloned homepage counter snippet on 15 interior pages, compact section spacing site-wide on interior pages, audit + add value images/infographics, and run AEO/entity/humor + keyword fan-out verification passes — all inline, no subagent dispatch.

**Architecture:** One shared-component change (CounterSnippet gains a `stats` prop, homepage default preserved), 15 one-line page edits passing page-specific stats, one CSS addition in `direction-d.css` for interior compact padding, then three audit-and-patch passes (images, AEO/entity/humor, fan-out) producing session reports + targeted fixes.

**Tech Stack:** Astro 4 + Tailwind, Direction D theme (`src/styles/direction-d.css`, `body.theme-d`), static build to `dist/`, GitHub Actions → Cloudflare Pages on push.

---

## Ground Rules (binding for every task)

1. **NO SUBAGENTS.** All work inline in this session. Apply agent *methods* (section-builder, entity-incorporation 4-Move Loop, infographic-builder, keyword-verifier, humor honesty policy) yourself.
2. **Verified-Claim Ledger overrides everything.** Every counter-snippet number MUST already appear in that page's live body copy (verify with `grep` against the page source before writing). If a proposed stat is not in the page, substitute another fact that IS. Never invent a number.
3. **Preview before apply** for anything visual (counter values are content-neutral swaps of an existing component — text approval is sufficient; infographics need preview/approval before page insertion).
4. **Same content rule:** counter snippets and compactness are visual/snippet-layer changes; do not add/remove body content.
5. **Commit + push after each task group.** Push = deploy.
6. Verify in `dist/` (`npx astro build` then grep dist HTML), not source-only.

## The 18 pages

| # | Slug | Counter today |
|---|---|---|
| 1 | african-grey-parrot-price | `<CounterSnippet />` (homepage clone) |
| 2 | african-grey-parrot-lifespan | clone |
| 3 | african-grey-parrot-diet | clone |
| 4 | best-african-grey-parrot-food | clone |
| 5 | african-grey-parrot-faq | clone |
| 6 | african-grey-parrot-guide | clone |
| 7 | african-grey-care | clone |
| 8 | african-grey-parrot-care-guide | clone |
| 9 | how-to-tame-african-grey-parrot | clone |
| 10 | captive-bred-african-grey-parrot | clone |
| 11 | cites-african-grey-documentation | clone |
| 12 | trusted-african-grey-parrot-breeders | clone |
| 13 | african-grey-reviews | clone |
| 14 | african-grey-parrot-health-guarantee | clone |
| 15 | african-grey-adoption | clone |
| 16 | how-to-avoid-african-grey-parrot-scams | **already page-specific** (12 Red Flags / 100% CITES Certified / $1,500 Min Legit Price / USDA AWA) — no change |
| 17 | contact-us | none — ADD page-specific snippet (Recommended) |
| 18 | privacy-policy | none — leave without (Recommended: legal page, a stat strip would be noise) |

---

### Task 1: CounterSnippet `stats` prop

**Files:**
- Modify: `src/components/cag-library/CounterSnippet.astro:1-14`

- [ ] **Step 1: Add prop with homepage default**

Replace the frontmatter `const stats = […]` with:

```astro
---
/**
 * cag-counter-snippet — 4-stat trust strip (Rule 31: 4 counter snippets after H1)
 * Accepts `stats` prop (4 items) so each page shows page-relevant numbers;
 * default = homepage strip. Values must exist in page copy (Verified-Claim Ledger).
 */
export interface Stat { num: string; label: string }
const defaultStats: Stat[] = [
  { num: "12+",    label: "Years Aviary" },
  { num: "100%",   label: "CITES Documented" },
  { num: "$1,500", label: "Floor Price" },
  { num: "24h",    label: "Reply Guarantee" },
];
const { stats = defaultStats } = Astro.props as { stats?: Stat[] };
```

(Keep `borderByIndex` and the template unchanged — it already maps over `stats`.)

- [ ] **Step 2: Build to verify homepage unchanged**

Run: `npx astro build 2>&1 | tail -3` → expect success.
Run: `grep -o "Years Aviary" dist/index.html | wc -l` → expect `1` (homepage default still renders).

- [ ] **Step 3: Commit**

```bash
git add src/components/cag-library/CounterSnippet.astro
git commit -m "feat(counter-snippet): stats prop with homepage default — enables per-page strips"
```

---

### Task 2: Page-specific stats on the 15 clone pages (+ contact-us)

**Files:** Modify each `src/pages/<slug>/index.astro` at its `<CounterSnippet />` call (line numbers: price:278, reviews:211, lifespan:167, diet:159 — locate the rest with `grep -n "CounterSnippet" src/pages/<slug>/index.astro`).

**Proposed stats per page** (every `num` MUST be grep-verified in that page's body first — substitute from page copy if missing; labels ≤ ~18 chars, uppercase-styled by component):

| Page | stats |
|---|---|
| price | `$1,500` CAG Floor · `$3,500` CAG Ceiling · `$1,200` TAG Floor · `$185` Airport Shipping |
| lifespan | `40–60` Yrs With You · `2014` Breeding Since · `100%` Captive-Bred · 4th from page copy (e.g. oldest-recorded age if present) |
| diet | `4` Pellet Brands We Feed · veg/chop % from page · `40–60` Yrs On Right Diet · 4th from page |
| best-food | `4` Brands We Endorse · `#1` Harrison's · 2 more from page (e.g. protein %, price/lb if present) |
| faq | `25` Questions Answered · `24h` Reply · `100%` CITES Documented · `2014` Since |
| guide (species pillar) | `2` Subspecies · `40–60` Yrs Lifespan · `Appendix I` CITES · `12–16 wk` Weaning |
| african-grey-care | 4 care numbers from page (e.g. daily out-of-cage hours, cage size, sleep hours, vet visits/yr) |
| care-guide (pillar) | same method as african-grey-care, distinct picks so the two pages differ |
| how-to-tame | `7` Taming Steps · timeline weeks from page · `2014` Hand-Raising Since · 4th from page |
| captive-bred | `100%` Captive-Bred USA · `USDA AWA` Licensed · `Appendix I` CITES · `2014` Since |
| cites-documentation | `Appendix I` Listing · `2017` Uplist Effective · `100%` Documented · 4th from page (e.g. paperwork items count) |
| trusted-breeders | `52` Verified Reviews · `4.9` Avg Rating · `USDA AWA` Licensed · `2014` Midland TX Since |
| reviews | `52` Real Reviews · `4.9★` Average · `100%` Verified Buyers · `2014` Since |
| health-guarantee | guarantee numbers from page (e.g. health-guarantee window days, vet-check window, DNA cert, replacement terms) |
| adoption | `$1,500` Starting Price · `12–16 wk` Weaning Age · `100%` CITES Documented · `2014` Breeder Since |
| contact-us (ADD) | `24h` Reply Guarantee · `7 days` We Answer · phone-hours stat from page · `2014` Since |

- [ ] **Step 1: For each page — verify stats against page copy**

Run per page (example for price):
```bash
grep -o "\$3,500\|\$1,200\|\$185" src/pages/african-grey-parrot-price/index.astro | sort -u
```
Expected: every chosen `num` appears at least once. If not → pick a replacement numeral from `grep -on "[0-9][0-9,$%–-]*" src/pages/<slug>/index.astro`.

- [ ] **Step 2: Edit each call site**

Pattern (example, price page):
```astro
<CounterSnippet stats={[
  { num: "$1,500", label: "CAG Floor" },
  { num: "$3,500", label: "CAG Ceiling" },
  { num: "$1,200", label: "TAG Floor" },
  { num: "$185",   label: "Airport Shipping" },
]} />
```
For contact-us: import the component (`import CounterSnippet from '../../components/cag-library/CounterSnippet.astro';`) and place the strip directly under the hero, matching other pages.

- [ ] **Step 3: Build + dist verification**

```bash
npx astro build 2>&1 | tail -3
grep -rl "Years Aviary" dist/ | grep -v "dist/index.html"
```
Expected: build OK; second command returns **nothing** (no interior page still shows the homepage strip).

- [ ] **Step 4: Commit + push**

```bash
git add src/components/cag-library/CounterSnippet.astro src/pages/
git commit -m "fix(counter-snippets): page-specific 4-stat strips on 16 interior pages (was homepage clone)"
git push
```

---

### Task 3: Compact section spacing on interior pages

**Files:**
- Modify: `src/styles/direction-d.css` (append interior compact-padding block)
- Modify: `src/pages/how-to-avoid-african-grey-parrot-scams/index.astro:147` (`.main-section{padding:52px 0}`)
- Check/modify: any other custom-CSS interior page with `padding:5*px 0` sections (`grep -rn "padding:[4-9][0-9]px 0" src/pages/<the 18 slugs>`)

- [ ] **Step 1: Add interior compact rule to direction-d.css**

Append (mirrors the proven `.home-d` values at `src/pages/index.astro:294-297`, scoped to main content so location/comparison pages and chrome wrappers are untouched — apply via a `.page-d` class on each interior page's top-level wrapper):

```css
/* Interior-page compact spacing (2026-06-11) — same rhythm as .home-d.
   Add class="page-d" to the 18 interior pages' main wrapper. */
.page-d .py-16, .page-d .py-14, .page-d .py-12 {
  padding-top: 2.25rem !important; padding-bottom: 2.25rem !important;
}
@media (min-width: 768px) {
  .page-d .py-16, .page-d .py-14, .page-d .py-12 {
    padding-top: 2.9rem !important; padding-bottom: 2.9rem !important;
  }
}
```

- [ ] **Step 2: Add `page-d` to each Tailwind-idiom interior page wrapper**

For each of the 15 CounterSnippet pages + contact-us: find the top-level content wrapper (the element containing the page's `<section>` bands) and append ` page-d` to its class list. Do NOT add it to fixed-position chrome (jump rails, tab bars — see MEMORY `project_mobile_gap_jumprail`).

- [ ] **Step 3: Trim custom-CSS pages**

Scams page: change `.main-section{padding:52px 0}` → `.main-section{padding:36px 0}` and check `#counters` (28px — fine). Privacy-policy: grep for its section padding and trim any ≥48px value to 36px.

- [ ] **Step 4: Visual verification**

```bash
npx astro build && npx astro preview --port 4321 &
```
Screenshot 3 representative pages (diet, scams, faq) at 1280px + 375px; confirm tighter rhythm, no clipped content, no gap-before-hero regression. Kill preview.

- [ ] **Step 5: Commit + push**

```bash
git add src/styles/direction-d.css src/pages/
git commit -m "style(interior): compact section rhythm — port .home-d padding scale to 18 interior pages via .page-d"
git push
```

---

### Task 4: Image/infographic opportunity audit (18 pages) → build approved set

**Files:**
- Create: `sessions/2026-06-11-image-opportunity-audit.md`
- Later modify: pages approved for infographics

- [ ] **Step 1: Audit inline (no subagents)**

For each of the 18 pages, read the section list (grep `<h2`) and current `<img` count, then record per page: top 1–2 sections where a visual adds answer-value, recommended type — **HTML/CSS infographic** (Comparison / Feature Grid / Process Flow, 760px wrapper, 400px desktop height), **AI image** (Nano Banana 2, 9:16), or **original breeder photo** (request list for Mark & Teri). Use `skills/cag-infographic.md` type rules. Mark one **(Recommended)** build order with WHY (search intent + AIO citation value) and the trade-off.

- [ ] **Step 2: Write the audit report**

Save to `sessions/2026-06-11-image-opportunity-audit.md` with a per-page table: `page | section | type | rationale | priority`.

- [ ] **Step 3: STOP — user approval gate**

Present the prioritized list. Build only approved items (preview-before-apply rule). Likely top candidates: diet plate-proportions Process Flow, lifespan timeline Comparison, CITES paperwork checklist Feature Grid, taming 7-step Process Flow, price cost-stack Comparison.

- [ ] **Step 4: Build approved infographics + insert, verify, commit + push**

Each: 760px wrapper, 400px fixed desktop height, line-icon SVGs (no emoji), lazy-loaded, alt + caption per Image SEO 5-Element rule. `npx astro build`, verify in dist, commit per infographic:
```bash
git commit -m "feat(infographic): <page> <section> — <type>"
git push
```

---

### Task 5: AEO / GEO / Entity / Non-Commodity / Humor verification pass

**Files:**
- Create: `sessions/2026-06-11-aeo-entity-humor-audit.md`
- Modify: only pages with gaps

- [ ] **Step 1: Per-page checklist (run inline, log PASS/GAP per item)**

For each of the 18 pages check:
1. **AEO:** first paragraph under H1 is a direct, declarative answer to the head query (≤ ~50 words, entity-first).
2. **AEO:** FAQPage JSON-LD present AND visible `<details>`/accordion matches it (`grep -o "FAQPage" dist/<slug>/index.html`).
3. **Entity:** spot-check vs `skills/cag-entity-agent.md` catalog — page names its core entities (*Psittacus erithacus*, CITES Appendix I, USDA AWA, PCR DNA sexing, etc. as relevant); every claim inside the Verified-Claim Ledger.
4. **Non-commodity:** classify STRONG/SHARPEN/REBUILD per MEMORY `feedback_noncommodity_audit_then_rewrite` — rewrite ONLY weak sections; do not regress indexed copy.
5. **Humor:** ≤1 dry Style-2 beat per appropriate section; NONE on legal/health/scam-loss content (privacy, health-guarantee FAQ answers).
6. **First-person voice:** flag any "African Greys are…" sentences that are actually about *our* offering.

- [ ] **Step 2: Fix gaps inline, smallest-diff edits; build + dist verify**

- [ ] **Step 3: Save report + commit + push**

```bash
git add sessions/2026-06-11-aeo-entity-humor-audit.md src/pages/
git commit -m "seo(aeo-entity): gap fixes from 18-page AEO/entity/humor audit"
git push
```

---

### Task 6: Intent-Based Keyword Fan-Out retro-audit

**Files:**
- Create: `sessions/2026-06-11-keyword-fanout-audit.md`
- Modify: only pages with heading-coverage gaps

Context: fan-out was run at *cluster* level during the 2026-06 batch (master checklist Phase 1); this verifies it landed per page.

- [ ] **Step 1: Per-page fan-out matrix**

For each page's head term, enumerate intent variants — informational ("how/what/why"), transactional ("for sale/price/buy"), comparison ("vs/best"), local ("near me/Texas"), PAA — and check each variant has an H2/H3 (or FAQ entry) covering it: `grep -o "<h[23][^>]*>[^<]*" dist/<slug>/index.html`. Score covered/total per page.

- [ ] **Step 2: Patch gaps**

Where a high-value variant is uncovered: add an H3 + short QAB answer inside an existing section (no new sections — content additions limited to answer blocks; respects heading-band rule, don't exceed seo-rules H2/H3 counts).

- [ ] **Step 3: Save report + commit + push**

```bash
git add sessions/2026-06-11-keyword-fanout-audit.md src/pages/
git commit -m "seo(fan-out): per-page intent coverage audit + H3 answer-block patches"
git push
```

---

### Task 7: Final sweep + deploy verification

- [ ] **Step 1:** `bash scripts/health-sweep.sh` → expect PASS.
- [ ] **Step 2:** `python3 scripts/generate_sitemaps.py` if any page lastmod logic depends on it (no new URLs expected → sitemap should be unchanged at 100 URLs).
- [ ] **Step 3:** After final push, spot-check 4 live URLs return 200 and show new counter values (`curl -s https://congoafricangreys.com/african-grey-parrot-price/ | grep -o "CAG Ceiling"`).
- [ ] **Step 4:** Log session close-out to `sessions/2026-06-11-session-brief.md` `## Open Flags` if anything is awaiting breeder input (e.g. original-photo request list from Task 4).

---

## Self-Review Notes

- Spec coverage: counter snippets (Tasks 1–2), Direction D scam question (answered in session, no code change needed — already live), compact sections (Task 3), images/infographics (Task 4), AEO/GEO/entity/non-commodity/humor (Task 5), keyword fan-out (Task 6), no-subagents (Ground Rule 1).
- Numbers in the stats table are proposals bound by the grep-verify step — the Verified-Claim Ledger rule deliberately overrides the no-placeholder rule for the 4 cells marked "from page copy" (fabricating a number to satisfy plan completeness would violate a stronger project rule).
- privacy-policy intentionally gets no counter strip (Recommended): it's a legal page; a trust-stat band would read as decoration on a page whose only job is plain disclosure. Trade-off: it's the one page of the 18 without the pattern — acceptable inconsistency.

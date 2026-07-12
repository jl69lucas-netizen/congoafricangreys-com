---
name: cag-component-refresh
description: Use when building or rebuilding any page in a multi-page cluster (comparison spokes, location pages, blog cluster, interior pages) to give each page a controlled "refresh delta" — a small, deliberate layout/style/motif variation per section — so sibling pages don't read as one identical template, WITHOUT breaking the locked palette, uniform image box, sticky offsets, or §11–§13 component contract. Triggers: "refresh the components", "make this page look different from the built ones", "component refresh", "the pages look the same", "differentiate the hero/quick-answer/table".
---

# SKILL: CAG Component Refresh (the "Refresh Agent")

**The problem this solves:** the 8-page comparison cluster (and any cluster built from one donor) drifts
toward looking like the *same page with words swapped* — identical hero, identical quick-answer band,
identical trait table, identical scorecard. The breeder wants **a small, tasteful differentiator per
page** so each feels purpose-built, while the brand still reads as one system.

**The rule:** a refresh is **layout OR accent-role OR motif/style**, section by section — **never a palette
change**. Change *how the same tokens are arranged*, not the tokens.

---

## 0. Invariants that NEVER refresh (breaking these = FAIL)

These are locked by DESIGN.md / IMAGE-DESIGNS §1a / the comparison §11–§13 contract. A refresh works
*around* them, never through them:

1. **Palette** — Forest `#2D6A4F` / Clay `#e8604c` / Cream `#faf7f4`; `--gold==--clay`. AA variants
   (`#c8472f` button fill, `#b04228` small clay text) unchanged.
2. **Primary CTA** = clay pill, `border-radius:50px`. Form submit = `12px`.
3. **Uniform in-body image box** — every OG + infographic in `.sec-img.inf-img` (760px, `aspect-ratio:1408/768`,
   `object-fit:cover`, `-760.webp` sibling + srcset), identical on mobile/tablet/desktop.
4. **Sticky offsets** — 96px header; rail `top:96px`; `scroll-margin-top:calc(96px+18px)`; **`scroll-behavior:auto` on html** (never smooth).
5. **Seam divider** — brand medallion `cag-header-logo-160.webp` + light-orange fading hairlines.
6. **Type system** — Newsreader headings / IBM Plex Sans body (Direction D, global). No hard-coded font-family.
7. **Motion cap** — ≤0.2s transitions, no bounce/parallax/autoplay.
8. **H1 outranks every H2 at every width**; heading hierarchy gate (all six levels, ≥5 H5/≥5 H6, no skips).

## 1. The Refresh Budget (do NOT refresh everything)

**Refresh 3–5 sections meaningfully per page; keep the rest consistent.** Total drift across a page
should feel like *a different editorial rhythm*, not a different website. Over-refreshing (every section
restyled) destroys cluster cohesion and doubles QA. Under-refreshing (0–2) is what the breeder is
complaining about. Pick the page's **signature sections** (hero + its 2–3 highest-scroll sections) to
carry the delta.

## 2. Refresh dimensions (pick ONE per refreshed section)

| Dimension | What changes | Example |
|---|---|---|
| **Layout** | grid/stack direction, column count, image side, sidebar vs inline | trait table → stacked "verdict cards"; 2-col → 3-col |
| **Accent-role** | which locked color leads (green-led vs clay-led section), tint vs solid | quick-answer band: green panel on one page, cream-with-clay-rule on another |
| **Motif** | the visual metaphor of an infographic/callout | choose-if: two signposts vs a balance scale vs a split "if/then" ledger |
| **Container shape** | card radius family, border vs shadow, full-bleed vs contained | myths: flip-cards vs stacked banners vs ledger rows |
| **Density** | compact vs airy, inline chips vs stacked rows | metros pills: 7-in-a-row vs 2-col map-pin grid |

## 3. Section-by-section Refresh Ledger (comparison cluster)

For each recurring section, keep a **rotation of 2–4 interchangeable treatments** so no two spokes ship
the same one. Track which spoke used which in the page's session brief.

### HERO — "just a tiny distinction" (breeder's words)
Keep the full-bleed band + copy-LEFT + 96px sticky + AA eyebrow. Rotate ONE:
- **A. Staggered two-portrait + `vs` roundel** (CvT/CvM/CvC — species pages). Do NOT reuse on non-vs pages.
- **B. Single-subject trust hero** — one strong OG right, copy left, a slim credential pill-row under H1 (breeders/pros-cons/hub — single-grey pages).
- **C. Motif hero** — a Gemini hub/spoke illustration right instead of a photo (hub INF-0 grey-vs-field).
- **Micro-tweaks (stackable on any):** eyebrow wording unique per spoke (§13-5); hero-meta pill set differs; portrait `object-position` differs; a 1-line clay underline vs none.

### Quick-Answer band ("The 60-Second … Answer" / "Quick answer:")
- **A. Green solid panel**, white text, clay verdict word.
- **B. Cream panel + left clay rule**, ink text (calmer, editorial).
- **C. Two-tone split** — left "Quick answer" green, right "TL;DR chips" cream.

### Choose-A-if / Choose-B-if (decision fork)
- **A. Two side-by-side signpost cards** (green vs clay headers).
- **B. Balance-scale infographic** + text list under (pros-cons INF-1).
- **C. If/then ledger** — single column, `If you… → choose…` rows with alternating tint.

### Author / "Why This Isn't Symmetric" (E-E-A-T)
- **A. Inline author byline chip** (Mark & Teri + link) under H2.
- **B. Bordered author card** right, prose left.
- **C. Pull-quote lead** — Teri's first-person line as a large clay pull-quote, byline beneath.

### Trait comparison table
- **A. Classic side-by-side `<table>`** + mobile tab-toggle (keep for AIO on the primary table).
- **B. Verdict cards** — per-trait card: trait title, two mini-columns, a green "Our note" strip.
- **C. Zebra ledger** — compact rows, clay-tinted "winner" cell. *(Non-primary tables stack to `data-label` cards on mobile — §12-4.)*

### "Match Your Household" / lifestyle rows
- **A. Numbered accordion** (household → verdict).
- **B. Icon-led cards grid** (2-col) with a one-word lean badge (clay "Grey" / green "Wait a year").
- **C. Flowchart infographic** + supporting text.

### Myths vs Reality
- **A. Flip/two-half cards** (MYTH banner → REALITY panel).
- **B. Stacked banner rows** — myth strikethrough, reality below.
- **C. Two-column ledger** (myth | reality).

### Shipping section (two delivery tiers — content locked)
Content invariant (Airport $185 · Home $350 · IATA/Delta/United/American). Rotate presentation:
- **A. Two photo cards** side by side (van / cargo).
- **B. Timeline strip** (reserve → vet → fly/drive → arrive) with the two tiers as end-nodes.
- **C. Split panel** — photo left, tier price rows right.

### Metros / route pills (7-place row)
- **A. Inline pill row** (map-pin SVG + cream tint), 2-col centered on mobile.
- **B. Mini US-map with 7 dots** + a caption list.
- **C. Grouped-by-mode** — "Airport pickup" / "Home delivery" / "Courier" columns. *(Each spoke uses a DIFFERENT 7-place set + fresh anchors — dup gate.)*

### "Every grey leaves with" (trust/documentation list)
- **A. Icon checklist column** (green checks).
- **B. Badge row** (5 pill badges).
- **C. Flat-lay OG photo** + caption list beside it (reuse the doc flat-lay infographic).

## 4. Process (run before writing page code — this is the pre-code gate)

1. **Audit the donor** (usually CvM — the most polished spoke). List its treatment for each recurring section.
2. **Pick the refresh budget** — 3–5 signature sections for this page; choose a treatment from the ledger
   NOT used by the two nearest siblings.
3. **Show the Refresh Matrix** (section · donor treatment · this-page treatment · dimension · WHY + trade-off).
   Mark the recommended hero tweak per Recommend+Why. **Get approval before code** (stacks with the
   Heading Outline Gate + Distribution Matrix + Preview-before-apply).
4. **Apply** — build the page from the donor, swapping only the approved treatments; everything else
   inherits unchanged. Re-run the clamp sweep (§13-8) since layout changed.
5. **Log** which treatment each section used in `sessions/…-session-brief.md` so the next spoke avoids repeats.

## 5. Pass gates (unchanged + refresh-specific)

- All §0 invariants intact (grep the diff for `scroll-behavior:smooth`, palette drift, non-uniform image boxes).
- `python3 scripts/dup_content_audit.py --headers` + body vs ALL siblings (a refresh must not reintroduce dup copy).
- `python3 scripts/final_page_audit.py --comparison` PASS/PASS-WITH-WARNINGS.
- Clamp sweep at 375/640/768/860/1280 — H1 leads every width after layout changes.
- Lighthouse warm median-of-3; a11y 100 (refreshed layouts keep AA + focus + heading order).

## 6. Reuse beyond comparison pages
The ledger is comparison-specific, but the **method** (invariants → refresh budget → dimensions →
matrix → log) applies to location pages (rotate hero/stats/FAQ treatments per state), the blog cluster
(rotate callout/TOC/pull-quote styles per post), and interior pages. Add a per-cluster ledger section
here when you start differentiating a new cluster.

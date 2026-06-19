---
name: cag-bird-page-build
description: Builds an individual /available/ bird page to the deep 22-section standard (H1-H6, distribution-matrix approval gate, Hero variants). Supersedes the lean cag-bird-listing-page depth.
tools: [Read, Write, Bash]
---

# C.A.Gs Bird Page Build — Deep 22-Section Standard

## Overview
The authoritative build standard for `/available/<slug>/` bird pages as of 2026-06-19. This
skill codifies the Roys reference architecture so all 6 available-bird pages are built
consistently. **Depth-model override:** ≈22 sections, ≈3,150 words (competitor MAX 1,474 →
target 2,974). This supersedes the old "lean 700–1,000 word" ceiling from CLAUDE.md and
`cag-bird-listing-page`. Update `scripts/final_page_audit.py --birds` `wordcount_in_band`
profile to match. Locked guardrails (single `Product`+`Offer`, no PBFD, sold≠InStock, no
visible date, CITES Appx I, Verified-Claim Ledger, no per-bird geo-targeting, first-person
voice) are unchanged.

Source spec: `docs/superpowers/specs/2026-06-19-roys-page-redesign-design.md`
Prototype assets: `assets/Roys/…Page Chrome.html` + `…Mobile Components.html`

## When to Use
Building or rebuilding any `/available/<slug>/index.astro` bird page. For variant/location/
comparison/for-sale cluster pages, use their own builders — this skill is bird-listing only.

---

## Methodology Gate (binding — before code)

For every bird page build, the following three steps are **required before writing any Astro
or HTML**:

1. **Visual companion** — produce skeleton/hero/component screens showing the page structure.
   Desktop and mobile must both be mocked; Direction D is global (do not re-implement it).

2. **Per-section distribution matrix** — for this specific bird, build a matrix table with
   columns: `#` / `H2 (intent)` / `Framework` / `Words` / `Category (A/B/C)` / `Keyword +
   variations` / `Fan-out answered` / `Entities` / `Special`. Each row must include a grounded
   WHY for the framework and category choice. The matrix is **approved by the user before any
   code begins**. The Roys matrix (spec §6) is the approved reference for what A/B/C ratios
   and section order look like.

3. **Always mark the recommended pick + why + trade-off** on every option set (hero variant,
   component variant, framework choice). Never present options without a reasoned recommendation.

Categories: **A = mandatory core** (non-negotiable for every bird page) · **B = competitor-
match** (parity with what competitors cover) · **C = our moat** (angles only C.A.Gs can own).
Target ratio: ≈A:7 / B:10 / C:5 per the Roys reference.

---

## H1 → H6 Hierarchy (passage-level ranking)

| Level | Purpose | Rule |
|---|---|---|
| **H1** | Page topic — the bird | One per page. Contains bird name + primary keyword (e.g., "congo african grey for sale"). |
| **H2** | Main search intents | One per section (= one TOC entry). All H2s are conversational Q&A form. |
| **H3** | Subtopics / keyword clusters | Group supporting points under their H2. |
| **H4** | Micro-intent answers / PAA coverage | Direct answer to one specific question; used in FAQ subsections. |
| **H5** | Supporting facts / warnings / examples | Breeder notes, caveats, example scenarios. |
| **H6** | Ultra-specific details / citations | Edge-case facts, ledger-bounded references, attributions. |

**All six levels (H1–H6) must appear somewhere on the page.** Section headers are written in
conversational Q&A form using What / How / Can / Is / Why openers. Do not write declarative
statement headers ("Our Health Standard") — rewrite as questions ("Is [Bird] a healthy bird?
Our health standard").

---

## Section Taxonomy

A **section** = an H2 that earns a TOC jump-link (e.g., `id="section-temperament"`).

**Modules** (not counted as sections, no TOC line): Hero (H1), AEO Snapshot box (40–50 word
declarative answer), the TOC itself, inline trust-badge strips. By this rule the Roys reference
build = **22 sections**.

---

## 22-Section Reference Architecture (AIDA-grouped)

Top modules above the TOC (not counted): **Hero** → **AEO Snapshot box** → **TOC**.

Each frame below maps to the distribution matrix column `Cat`:

### ATTENTION (sections 1–4)

| # | H2 (intent) | Framework | Words | Cat |
|---|---|---|---|---|
| 1 | Is [Bird] the right African Grey for me? (Key Takeaway) | AIDA | 90 | A |
| 2 | What is [Bird] like to live with? (temperament) | EBP | 180 | A |
| 3 | Does a [sex] Congo/Timneh African Grey talk well? | QAB | 150 | B |
| 4 | Why does [Bird] cost $[price] when I see "$850" greys? | PDB | 240 | C |

### INTEREST (sections 5–9)

| # | H2 (intent) | Framework | Words | Cat |
|---|---|---|---|---|
| 5 | What documentation comes with [Bird]? | EBP | 220 | B |
| 6 | What's included when you reserve [Bird]? | QAB | 120 | A |
| 7 | How does [Bird] compare to our other available greys? | Compare | 190 | C |
| 8 | Is [Bird] a healthy bird? Our health standard | EBP | 160 | B |
| 9 | Who are [Bird]'s parents? | EBP | 130 | C |

### DESIRE (sections 10–15)

| # | H2 (intent) | Framework | Words | Cat |
|---|---|---|---|---|
| 10 | What should you decide before buying an African Grey? | BAB | 200 | C |
| 11 | What's it like to own an African Grey long-term? | BAB | 170 | B |
| 12 | Reviews — families who brought home a C.A.Gs grey (MID) | Proof | 120 | B |
| 13 | How do you train an African Grey like [Bird]? | HowTo | 170 | B |
| 14 | What do C.A.Gs recommend feeding African Greys? | QAB | 150 | B |
| 15 | [Bird]'s photo & video gallery | Visual | 60 | A |

### ACTION (sections 16–22)

| # | H2 (intent) | Framework | Words | Cat |
|---|---|---|---|---|
| 16 | How do you buy [Bird]? Step-by-step | HowTo | 150 | A |
| 17 | Where do C.A.Gs deliver African Greys? (shipping) | QAB | 160 | B |
| 18 | Our credentials (USDA AWA / CITES / DNA / Avian Vet) | EEAT | 80 | A |
| 19 | [Bird] — frequently asked questions (6 PAA) | QAB | 260 | B |
| 20 | Reviews — more happy C.A.Gs owners (BOTTOM) | Proof | 120 | B |
| 21 | Why buy from C.A.Gs instead of a marketplace? | EBP | 170 | C |
| 22 | Ready to bring [Bird] home? (CTA + contact form) | AIDA | 90 | A |

**Totals per the Roys reference:** 22 sections · ≈3,150 words.

Adapt section #s 1, 2, 3, 4, 7, 9, 15, 19, 22 for each individual bird's name, sex, variant
(Congo vs Timneh), price, and approved personality archetype. Keep the section order fixed.

---

## Hero Variants

Each bird gets exactly one hero. Pair birds so each variant covers 2 pages (1 hero per 2 pages):

| Variant | Description | Assigned pair (reference) |
|---|---|---|
| **A · Editorial** | Clean split: headline + specs left, art-directed portrait right. Quiet authority. | Elad + Evie (Timneh pair) |
| **B · Dark** | Dark forest-green panel, cream headline, high-drama photo. Premium feel. | Jins & Jeni + Bery |
| **C · Trust-first + video** | Headline + price + USDA/CITES/DNA badges left, click-to-play video right (lazy poster, no autoplay). | Roys + Amie (media-rich Congos) |

Assign the variant in the distribution matrix before coding. Document the pairing rationale
(why this bird gets this hero) in the matrix `Special ★` column.

---

## Component Map

| Section | Component → variant | Notes |
|---|---|---|
| Hero | Variant A/B/C (per assignment above) | Locked per bird before code |
| Reviews mid + bottom | Testimonials · **3-up cards w/ avatar** | Real buyer photos from `public/`; same component both slots |
| Sibling comparison | **Compare Table Style E (1100px)** | Homepage-proven; links to `/congo-african-grey-for-sale/` + siblings |
| Parent birds | `cag-parent-birds` | Real parent info only (Verified-Claim Ledger) |
| Gallery | Real-photos grid + video | 2 real clips; SEO-renamed alt text required |
| FAQ | `cag-faq-acc` accordion (JS) | + FAQPage schema; 6 PAA questions |
| Contact form | `cag-inquiry-form.astro` | Own `idPrefix` so 2 form instances can coexist |
| Trust credentials | Kept-verbatim trust block | USDA AWA / CITES / DNA / Avian Vet |
| AEO Snapshot / Key Takeaway / Counter-snippet / TOC | `cag-library` modules | AEO box, key-takeaway, counter-snippet, jump TOC |
| Navbar / Footer | **Global Direction D (BaseLayout)** | **NOT re-implemented per page** — already applied via `body.theme-d` |

Direction D (Newsreader headings + IBM Plex Sans body, clay CTAs, Direction-D lead-paragraph
styles) is global. Build normal design-system markup and it applies automatically. Do not
add `direction-d.css` inline or redeclare font-family rules on per-page elements.

Desktop + mobile must match the prototypes in `assets/Roys/`. Mobile uses the library's mobile
variants (floating-pill nav, sticky bottom CTA bar, stacked sections).

---

## Guardrails (binding)

All CLAUDE.md non-negotiables apply. The following are the bird-page-specific critical ones:

| Rule | Requirement |
|---|---|
| **Single Product + Offer** | One `Product` + one `Offer` per page — NEVER `AggregateOffer` (that belongs on `/congo-african-grey-for-sale/`). `availability`: `InStock` / `PreOrder` / `SoldOut`. |
| **No PBFD / Polyomavirus** | Do NOT assert, imply, or deny PBFD or Avian Polyomavirus test results — these are not in the Verified-Claim Ledger as of 2026-06-19. A factual mention without a claim direction is allowed. |
| **No visible date** | Freshness lives in schema `dateModified` only. No "Updated June 2026", no byline date, no "Last updated" anywhere on the page. |
| **CITES Appendix I captive-bred USA** | Every page must state CITES Appendix I status and that all birds are captive-bred in the USA with full documentation. Never imply wild-caught or illegal trade. |
| **First-person plural voice** | Write as the breeder: "we / us / our / here at C.A.Gs." Not third-person observer copy. |
| **Verified-Claim Ledger** | Health/credential claims must be in the ledger (`cag-entity-incorporation-agent.md`). Allowed: DNA sex cert, avian-vet health cert, CITES/captive-bred docs, hatch cert + band, weaning status, USDA AWA. |
| **No per-bird geo-targeting** | Never add city/state copy to an individual bird page — that cannibalizes location pages. Shipping section links OUT to location/city pages instead. |
| **Shipping cost line on every card** | Every bird page must show the two-tier shipping cost: `Ships nationwide · $185 airport · $350 home`. Read `data/financial-entities.json` (`delivery_options`) + `data/price-matrix.json` — never hardcode a different number. |
| **Icons = line-SVG, never emoji** | Use inline Feather-style SVGs (1em / stroke="currentColor"). NEVER 🦜 (generic green parrot, not an African Grey). African Grey icon: `<img src="/emoji/cag-congo.png">` or `cag-timneh.png`. |
| **Preview before apply** | Any hero or layout decision must be previewed and approved before writing to the `src/pages/available/<slug>/index.astro` file. |
| **Commit + push on main** | After build, commit and `git push origin main` immediately. Only `main` auto-deploys. Never create a feature branch. |
| **Sell-and-retire lifecycle** | On `sold`: update `data/clutch-inventory.json`, render Sold state or 301 via `cag-redirect-manager`, regenerate sitemaps. Never leave `InStock` on a sold bird. |
| **Real image or defined placeholder** | Never invent an image filename that 404s. Check `assets/Roys/` (or the equivalent bird folder) and `public/` before any image reference. |

---

## Schema Set

| Schema type | Required | Notes |
|---|---|---|
| `Product` + single `Offer` | HARD GATE | One bird = one Product, one Offer. `price` from `data/price-matrix.json`. `availability` reflects live status. |
| `FAQPage` | Required | 6 PAA questions; answers must be visible on page (not schema-only). |
| `BreadcrumbList` | Required | Trail: Home → Available African Greys → [Bird Name]. |
| `Organization` | Required | Reuse site-wide `Organization` block; `cag-inquiry-form.astro` carries it. |
| Review schema | **FORBIDDEN** | No per-bird testimonial Review schema. Testimonials are brand-level, not per-bird. |
| `dateModified` | Schema-only | In JSON-LD `Product` / page-level schema. Never as visible text. |

Extend existing JSON-LD in `BaseLayout`; never duplicate the `Organization` block. Verify
schema renders correctly in `dist/` after build — do NOT trust source-file greps (generators
can hide or modify output). Compact the JSON-LD (no pretty-print) in `dist/` output.

---

## Per-Bird Adaptation Checklist

Before opening any file, confirm these facts from `data/clutch-inventory.json` and the breeder:

- [ ] Bird name, sex, variant (Congo / Timneh)
- [ ] Age (weeks/months) — verify if changed since last session
- [ ] Price — read from `data/price-matrix.json`
- [ ] Framework assigned (AIDA / BAB / PAS / PDB / EBP / QAB)
- [ ] Hero variant (A / B / C) — confirm pairing
- [ ] Real image files confirmed present in `assets/<BirdName>/` or `public/`
- [ ] Archetype (CLEO / REX / NOVA / SAGE / IRIS) from `cag-bird-personality`
- [ ] Parent birds confirmed real (from `data/bird-inventory.json` or breeder)
- [ ] Distribution matrix approved by user

---

## Verification

Run these three steps in order after every bird page build:

1. `npx astro build` — must produce zero errors; check `dist/available/<slug>/index.html` exists.
2. `python3 scripts/final_page_audit.py --birds` — must pass all HARD GATES; resolve any FAILs
   before deploying; log WARNs for follow-up.
3. Preview desktop (≥1025px) + mobile (375px) — both must match `assets/Roys/` prototypes in
   layout, typography, and CTA placement.

Then: `git add src/pages/available/<slug>/index.astro && git commit -m "feat(bird): …" && git push origin main`.

---

## Related Files
- `docs/superpowers/specs/2026-06-19-roys-page-redesign-design.md` — full approved spec (source of truth)
- `data/clutch-inventory.json` — bird facts + status
- `data/price-matrix.json` — prices
- `data/financial-entities.json` — shipping tiers ($185 / $350)
- `data/bird-inventory.json` — parent bird data
- `scripts/final_page_audit.py` — mechanical auditor (--birds flag)
- `skills/cag-bird-listing-page.md` — predecessor (lean 9-section standard, now superseded by depth)
- `skills/cag-final-page-pass.md` — final QA gate
- `skills/anti-ai-writing.md` — anti-AI phrase/rhythm blacklist; run before finalizing copy
- `.claude/agents/cag-entity-incorporation-agent.md` — 4-Move Loop + Verified-Claim Ledger
- `.claude/agents/cag-bird-personality.md` — CLEO/REX/NOVA/SAGE/IRIS archetypes
- `DESIGN.md` + `PRODUCT.md` — locked palette, typography, brand rules (read before any design decision)

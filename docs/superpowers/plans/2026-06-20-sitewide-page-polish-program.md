# Sitewide Page-Polish Program — PREP (2026-06-20)

**Goal:** apply the "Roys treatment" to every remaining page. The **visual + structural system is
constant**; the **SEO, keywords, and framing are different per page** (never copy Roys's angle).

**Reference build (the gold standard):** `src/pages/available/roys/index.astro` →
live at `/available/roys/`. Everything below generalizes what we did there.

**Decisions locked (breeder, 2026-06-20):**
1. **Sequence = bird pages first, then by value-tier** (Batch 1 → 6 below).
2. **Prep depth = direction now, full keyword research in-session.** This doc gives each page its
   *primary keyword + framing angle + image needs* — enough to gather assets and start fast. The
   keyword fan-out / PAA / competitor-gap research runs live per page via the existing agents.
3. **Word count:** match Roys's depth (~5,000–6,500 words) on bird pages. The lean 700–1,000-word
   bird-listing profile is **superseded for these flagship available birds** — breeder confirmed
   "6,431 is fine, do the same." (Auditor `wordcount_in_band` WARN is expected and accepted.)

---

## 1. THE PAGE-POLISH PLAYBOOK — the CONSTANT (applies to every page, every type)

This is the generalized Roys treatment. Run it on each page as a checklist.

### A. Structure & order
- [ ] **Counter-snippet / key stats sit directly under the hero** (above the "at a glance" card). No duplicate trust strips.
- [ ] **No duplicated trust surfaces.** The hero already carries the credential badges → do NOT also render a `TrustBar` and a separate "Our credentials" section. One trust statement, not three. (Roys: removed both.)
- [ ] Full **H1 → H6** heading band, each heading a conversational/two-keyword question (Rule 28b). Bird/long pages should clear the auditor's `all_h1_h4`.
- [ ] TOC for pages >1,500 words; JumpRail dial for very long pages. Keep section numbers + counts in sync if you add/remove sections.
- [ ] Section-seam logo dividers (`.cag-seam` + `/cag-footer-logo.webp`) — 4–8 per long page, not every section.

### B. Visual & images (the part the screenshots judge)
- [ ] **Image galleries: portrait photos go in aspect-ratio tiles with per-image `object-position`** so the bird is centered, never cropped at head/feet. (Roys gallery fix — uniform `aspect-[4/5]` tiles + tuned `object-position: center NN%`.)
- [ ] **Hero / selling-point images render full-width and centered**, not as a small right-rail thumbnail. A wide infographic (trust panel, comparison) especially must be full-width to be legible.
- [ ] **Real photos only** — no stock. If a photo isn't of the subject, don't label it as the subject; reuse it honestly elsewhere.
- [ ] **Infographic widths:** 760px wrapper (species/blog/care/article) · 1100px wrapper (homepage/location/hero). 400px desktop height, auto on mobile. Never 900px / max-w-4xl.
- [ ] **Verify centering in a real browser** (preview screenshots, desktop + mobile) before calling it done.

### C. Image SEO — the 5-element rule (MUST, none optional)
Per `skills/cag-seo-master-checklist.md` §Step 12. For **every** content image:
1. **FILENAME** — keyword-rich, lowercase-hyphens, `.webp`.
2. **ALT** — **≤190 chars** (AA + auditor cap), keyword + entity + context + location.
3. **TITLE** — `title=""` short transactional-keyword phrase.
4. **CAPTION** — visible `<figcaption>`, soft CTA where natural.
5. **DESCRIPTION** — 250-word SEO description (image-metadata pipeline).
- [ ] **Transactional-keyword variation:** each image uses a *different* keyword variation than the visible copy, so one page ranks for many queries. Never repeat the H1 keyword verbatim across images.

### D. Links
- [ ] **Link from the start or middle of a sentence — NEVER at the end.**
- [ ] Internal links woven mid-sentence into the topical cluster (hub ↔ spoke, sibling pages, money pages).
- [ ] External authority links: from `docs/reference/external-link-library.md` only, **200-checked**, `target="_blank" rel="noopener noreferrer"` + ↗, technical term linked **once** per page.

### E. Voice, claims, schema
- [ ] **First-person C.A.Gs voice** ("we / our / here at C.A.Gs"). Encyclopedic/taxonomy facts stay neutral.
- [ ] **Verified-Claim Ledger only** for health/credentials. (Now INCLUDES **PBFD/Polyomavirus PCR screening** — confirmed 2026-06-20. Still off-limits: anything not in the ledger.)
- [ ] CITES Appendix I + captive-bred-USA framing; never imply wild-caught.
- [ ] Anti-AI phrasing pass (`skills/anti-ai-writing.md`); ≤1 dry-humor beat per section, never on legal/health.
- [ ] Schema: extend existing JSON-LD, never duplicate; FAQ schema must be visible; verify in `dist/`.
- [ ] **No visible dates** anywhere — freshness lives in schema `dateModified` only.

### F. The per-page loop (how we actually execute, like Roys)
1. Read `PRODUCT.md` + `DESIGN.md` (binding, every session).
2. Confirm on `main`.
3. Build/polish section-by-section → **preview before apply**, ≥97% confidence gate.
4. `npx astro build` (from repo root — not `src/pages/`) → verify in `dist/`.
5. `python3 scripts/final_page_audit.py` (`--birds` for the available cluster) → PASS / fix.
6. Browser-verify centering + layout (preview screenshots, desktop + mobile).
7. `git commit` + `git push origin main` (= deploy). Regenerate sitemaps if pages added/removed.

---

## 2. THE VARIABLE — what changes per page (never copied from Roys)

For every page the **SEO target, keyword cluster, framing angle, and image set are bespoke.**
The tracker in §3 gives each a starting *direction*; the live session runs the real research
(`cag-content-audit-agent` → `cag-angle-agent` → `cag-paa-agent` → `cag-keyword-verifier`).

---

## 3. BATCH PLAN + PER-TYPE TRACKER

### BATCH 1 — Bird pages (NEXT SESSION) — expand to full Roys standard
5 remaining available birds. Each gets the **full Roys depth** (gallery, full-width selling-point
image, H1–H6, expanded sections, ~5–6k words). Framing is per-bird and must NOT echo Roys.

| Bird | Facts | Framing angle (bespoke) | Primary keyword direction |
|---|---|---|---|
| **Amie** | ♀ Congo, ~3 mo, **$2,500** | Premium female Congo; social/curious; "family or couple" home; justify the higher price | `female Congo African Grey for sale` |
| **Bery** | ♀ Congo, ~1 yr, **$1,700** | Older, settled, gentle; ideal **first-time owner**; "already started" + value angle | `1 year old Congo African Grey for sale` / `gentle African grey` |
| **Jins & Jeni** | **bonded pair** Congo, **$3,500** | **Pair page — different structure** (two birds, bonded-pair care, why a pair). Cross-link `/african-grey-breeding-pair-for-sale/` + `/congo-african-grey-parrot-pair-for-sale/` | `African grey bonded pair for sale` |
| **Elad** | ♂ **Timneh**, **$1,600** | **Timneh angle** — earlier talker, smaller, maroon tail, calmer; cross-sell `/timneh-african-grey-for-sale/` | `male Timneh African Grey for sale` |
| **Evie** | ♀ **Timneh**, **$1,500** | Female Timneh; calm/steady; "calmer household"; entry price point | `Timneh African Grey for sale` (female) |

**Per-bird image needs (UNIQUE — gather before session):**
- 1 **hero** photo (or short clip + poster)
- 4–5 **gallery** photos (varied poses; portrait OK — we crop-center)
- 1 **selling-point / interaction shot** (hand-feeding, step-up, talking — the "tameness" hero like Roys's hand shot)
- 1 **parents** photo (the breeding pair) — or reuse if same pair
- 1 **personality infographic** (per-bird ratings; HTML/Nano-Banana)
- For **Jins & Jeni**: photos of **both** birds + together as a pair

**Reusable across all birds (already exist — no new gather needed):** trust/certification panel, shipping/IATA carrier image, fresh-veggies/diet photo, what's-included graphic, the Maxy talking video.

---

### BATCH 2 — Money / variant / attribute pages (highest commercial intent)
`congo-african-grey-for-sale` · `timneh-african-grey-for-sale` · `captive-bred-african-grey-parrot` ·
`dna-tested-african-grey-for-sale` · `hand-raised-african-grey-parrot-for-sale` ·
`baby-african-grey-parrot-for-sale` · `male-african-gray-for-sale` ·
`affordable-african-grey-birds-for-sale` · `buy-african-grey-parrot-near-me` ·
`buy-african-grey-parrots-with-shipping` · `where-to-buy-african-greys-near-me` ·
`african-grey-breeding-pair-for-sale` · `congo-african-grey-parrot-pair-for-sale` ·
`african-grey-parrot-bird-eggs-for-sale-usa` · `grey-african-parrots-for-sale` + 2 geo-money pages.

- **Framing:** transactional AIDA; each owns ONE attribute keyword (variant / captive-bred / DNA / hand-raised / baby / price-tier / shipping). Cross-sell the available-birds hub + relevant bird pages. Avoid cannibalizing location pages.
- **Image needs per page:** 1 hero + 1–2 supporting real photos + **1 feature/benefit infographic** (e.g., "captive-bred vs wild-caught", "DNA-sexing process", "hand-feeding timeline"). Many can reuse a shared bird-photo library.

---

### BATCH 3 — Comparison pages
hub `african-grey-comparison` · `congo-vs-timneh-african-grey` · `male-vs-female-african-grey-parrots-for-sale` ·
`african-grey-vs-macaw` · `african-grey-vs-cockatoo` · `african-grey-vs-amazon-parrot` ·
`african-grey-parrot-breeders-comparison`.

- **Framing:** PDB/comparison; own structure (don't apply the bird/interior profile). Decision-stage "X vs Y" intent.
- **Image needs per page:** **1 comparison infographic** (the X-vs-Y table as a graphic) + 1 photo of each subject. The vs-other-species pages need a credible photo of the *other* species (macaw/cockatoo/amazon) — gather or source-license.

---

### BATCH 4 — Location pages (~40, Florida-template)
All `african-grey-parrot-for-sale-[state/city]`.

- **Framing:** local intent; Contextual-Intelligence; ship-to-[state] + nearest hub airport. Florida is the 22-section reference. SEO differs by geo only.
- **Image needs:** mostly **reusable** — generic grey photos + the shipping/IATA image + a **state/city map** (the `cag-google-map-agent` generates these). Low unique-image burden. **This is why location pages come after the image-heavy batches.**

---

### BATCH 5 — Interior / informational (already at older "Interior Standard" — bring to Roys polish)
`african-grey-parrot-care-guide` · `african-grey-care` · `african-grey-parrot-diet` · `best-african-grey-parrot-food` ·
`african-grey-parrot-lifespan` · `african-grey-parrot-health-guarantee` · `african-grey-parrot-faq` ·
`african-grey-parrot-guide` · `how-to-tame-african-grey-parrot` · `how-to-avoid-african-grey-parrot-scams` ·
`cites-african-grey-documentation` · `trusted-african-grey-parrot-breeders` (About) · `african-grey-reviews` ·
`african-grey-parrot-price` · `african-grey-adoption` · `african-grey-parrot-adoption-cost` ·
`african-grey-pros-and-cons` · `african-greys-for-sale-with-health-guarantee` · `contact-us` · `privacy-policy`.

- **Framing:** informational/EEAT; QAB FAQs; each owns its topic keyword. These already pass the interior audit — the polish here is mostly the **visual/image upgrades** (full-width infographics, gallery centering where relevant, 5-element image SEO) + any new topic infographic.
- **Image needs per page:** 1 topic infographic (diet wheel, lifespan timeline, cost breakdown, scam-checklist, CITES-doc anatomy, taming steps) + 1–2 supporting photos. **Highest infographic count of any batch.**

---

### BATCH 6 — Blog posts + hubs
Blog: `african-grey-health-problems` · `african-grey-parrot-cage-setup` · `african-grey-parrot-facts` ·
`african-grey-parrot-price-what-you-get` · `african-grey-parrot-talking-ability` · `african-grey-parrot-training` ·
`african-grey-vs-eclectus` · `best-place-to-buy-african-grey-parrot` · `is-african-grey-good-for-beginners`.
Hubs: `african-grey-parrots-for-sale` · `african-grey-parrots-for-sale-near-me` · `case-studies` · `testimonials`.

- **Framing:** informational/commercial blog intent; each post owns its long-tail. Hubs aggregate + link to spokes.
- **Image needs per post:** 1 hero + 1–2 supporting photos/infographics.

---

### Homepage (optional refresh, slot anytime)
Already live + strong. A light pass to inherit the newest patterns (gallery centering, 5-element image SEO, PBFD trust line) only if time allows — not a rebuild.

---

## 4. IMAGE-GATHERING CHECKLIST — your between-session action

Use `IMAGE-DESIGNS.md` for crop ratios / style / the negative list (no logos, no 🦜, no other species in CAG shots). Save originals to `assets/brand/` (or `assets/<bird>/`), deployed copies to `public/`.

**Priority 1 — Batch 1 birds (need these before next session):**
- [ ] **Amie** — hero, 4–5 gallery, 1 hand/interaction shot, 1 parents photo
- [ ] **Bery** — hero, 4–5 gallery, 1 hand/interaction shot, 1 parents photo
- [ ] **Jins & Jeni** — hero, 4–5 gallery of EACH + together-as-a-pair, parents photo
- [ ] **Elad** (Timneh) — hero, 4–5 gallery, 1 hand/interaction shot, 1 parents photo
- [ ] **Evie** (Timneh) — hero, 4–5 gallery, 1 hand/interaction shot, 1 parents photo
- [ ] (Infographics — personality cards per bird — I generate these in-session; you don't need to shoot them)

**Priority 2 — Batch 2/3 (gather as we approach):** 1 hero + 1–2 supporting photos per money/variant page; for comparison pages, a licensed photo of each *other* species (macaw, cockatoo, amazon, eclectus).

**Priority 3 — Batch 5 infographics (most graphic-heavy):** I can generate these (Nano Banana / HTML) — you only need to confirm the facts. Topics: diet wheel, lifespan timeline, first-year cost breakdown, scam checklist, CITES-doc anatomy, taming steps.

> You shoot the **real photos**; I generate the **infographics** in-session (Nano Banana / Higgsfield / HTML per `skills/cag-image-generation.md` + `skills/cag-infographic.md`).

---

## 5. PER-PAGE WORKFLOW (the in-session chain)

Bird pages: `cag-bird-listing-page` (expanded to Roys standard) → section-by-section build →
`cag-entity-incorporation-agent` (4-Move Loop) → `cag-faq-agent` → image pass → `final_page_audit.py --birds` → deploy.

Other types: `cag-content-audit-agent` → Section Map + Component Gate → `cag-angle-agent` → `cag-paa-agent`
→ the page-type builder (variant/comparison/location/interior/blog) → `cag-keyword-verifier` →
`cag-meta-description-agent` → `cag-external-link-agent` → `final_page_audit.py` → deploy.

Always: preview-before-apply · ≥97% confidence gate · commit+push after each page.

---

## 6. OPEN ITEMS / what I need from you
- [ ] Confirm the Batch-1 framing angles per bird (table in §3) before we build.
- [ ] Gather Priority-1 bird photos (§4).
- [ ] Flag any page you want re-prioritized out of the value-tier order.
- [ ] (Carried) PBFD now an allowed claim sitewide — surface it on health/trust sections as we touch each page.

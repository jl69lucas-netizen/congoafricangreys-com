# Roys Page Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild `/available/roys/` to the approved 22-section / ~3,150-word standard (Hero C, H1–H6, full distribution matrix) and ship the reusable system that the other 5 bird pages inherit.

**Architecture:** First codify the new standard as a build skill + update the bird audit profile so the auditor agrees with the new depth. Then rebuild Roys section-by-section in `src/pages/available/roys/index.astro` using existing cag-library components + Direction D (global), verifying each milestone with `npx astro build` + `final_page_audit.py --birds` + preview. Phase 3 (5-page batch) is a separate per-page plan.

**Tech Stack:** Astro (static), Direction D theme (BaseLayout, global), cag-library components, `scripts/final_page_audit.py`, `scripts/generate_sitemaps.py`, Higgsfield MCP + `cag-image-pipeline`, Pagefind. Work on `main` only (no branches/worktree — only `main` auto-deploys).

**Source of truth:** `docs/superpowers/specs/2026-06-19-roys-page-redesign-design.md` (the approved spec). Keyword/entity grounding: `docs/research/2026-06-19-bird-pages-competitive-analysis.md` (Roys = lines 40–164).

**Non-negotiables carried from CLAUDE.md:** single `Product`+`Offer` (never AggregateOffer), no PBFD/Polyomavirus, no visible date (schema only), CITES Appendix I captive-bred USA, first-person plural voice, Verified-Claim Ledger, no per-bird geo-targeting, shipping cost line on cards, icons = line-SVG (never emoji / never 🦜), preview-before-apply, commit + push after build.

---

## File Structure

- `skills/cag-bird-page-build.md` — **new** governing build skill (H1–H6 hierarchy, 22-section architecture, taxonomy, visual-companion + distribution-matrix methodology). Supersedes the lean depth in `cag-bird-listing-page.md`.
- `scripts/final_page_audit.py` — **modify** the `bird` profile (word ceiling 700–1,000 → deep standard; section/heading expectations incl. all_h1_h4) so deep bird pages don't false-FAIL.
- `skills/cag-bird-listing-page.md` — **modify** add a pointer to the new deep standard.
- `src/pages/available/roys/index.astro` — **rebuild** (currently 313 lines / 15 sections / H1–H3).
- `public/birds/roys/` — **create** SEO-renamed WebP images + posters (via cag-image-pipeline).
- `src/pages/index.astro` — **modify** add reciprocal homepage→Roys (+ siblings) links (bidirectional).
- `CLAUDE.md` — **modify** add the visual-companion + distribution-matrix methodology as a TOP rule (session-end task).

---

## Phase 1 — Codify the standard

### Task 1: Create the bird-page build skill

**Files:**
- Create: `skills/cag-bird-page-build.md`

- [ ] **Step 1: Read the source spec and an existing skill for format**

Run: `sed -n '1,60p' docs/superpowers/specs/2026-06-19-roys-page-redesign-design.md && head -40 skills/cag-bird-listing-page.md`
Expected: see the H1–H6 hierarchy, taxonomy, 22-section matrix, and the existing skill's frontmatter/format.

- [ ] **Step 2: Write the skill** with these sections (no placeholders — real content):
  - Frontmatter `name: cag-bird-page-build`, `description:` "Builds an individual /available/ bird page to the deep 22-section standard (H1–H6, distribution-matrix approval gate, Hero variants). Supersedes the lean cag-bird-listing-page depth."
  - **Methodology gate** (binding): visual companion for skeleton/hero/components; per-section distribution matrix (taxonomy + ordered topic→micro stack + framework/words + A/B/C with grounded *why*) approved BEFORE code; always mark recommended pick + why + trade-off.
  - **H1→H6 hierarchy** table (verbatim from spec §2) + conversational Q&A header rule (What/How/Can/Is/Why).
  - **Section taxonomy** (spec §3): section = H2 with a TOC jump-link; Hero/Snapshot/TOC/trust-strip = modules.
  - **The 22-section reference architecture** (spec §6 column list) as the default stack, AIDA-spine, with the A/B/C definition.
  - **Hero variants** (A Editorial / B Dark / C Trust-first+video) + the 1-per-2-pages rule.
  - **Component map** (spec §7) + Direction-D-is-global note.
  - **Guardrails** (the CLAUDE.md non-negotiables list above) + schema set (Product+Offer, FAQPage, Breadcrumb, Organization; no Review schema; no visible date).
  - **Verification**: `npx astro build` → `python3 scripts/final_page_audit.py --birds` → preview desktop+mobile.

- [ ] **Step 3: Verify the skill is well-formed**

Run: `head -5 skills/cag-bird-page-build.md && grep -c '^## ' skills/cag-bird-page-build.md`
Expected: valid `---` frontmatter with name/description; ≥8 `##` sections.

- [ ] **Step 4: Commit**

```bash
git add skills/cag-bird-page-build.md
git commit -m "skill(bird-page): deep 22-section build standard + H1-H6 + matrix gate"
```

### Task 2: Update the bird audit profile + listing-skill pointer

**Files:**
- Modify: `scripts/final_page_audit.py` (bird profile)
- Modify: `skills/cag-bird-listing-page.md`

- [ ] **Step 1: Capture the RED baseline** (current auditor verdict on Roys BUILD-1)

Run: `npx astro build >/dev/null 2>&1 && python3 scripts/final_page_audit.py --birds 2>&1 | sed -n '1,40p'`
Expected: note the word-ceiling WARN/FAIL and the `all_h1_h4` (missing H4) flag for roys — these are what the new profile must accommodate.

- [ ] **Step 2: Find the bird profile thresholds**

Run: `grep -nE "bird|word|min_words|max_words|all_h1_h4|700|1000|1,000" scripts/final_page_audit.py`
Expected: locate the bird-profile word band (700–1,000) and the heading check.

- [ ] **Step 3: Edit the bird profile** — raise the visible-word band to the deep standard (e.g. `min 1500`, `max 4000`) and keep the `all_h1_h4` requirement (the new pages DO use H1–H4). Leave single-`Product`/`Offer`, no-PBFD, sold≠InStock, shipping-line, no-visible-date checks unchanged.

- [ ] **Step 4: Add the pointer to the listing skill** — in `skills/cag-bird-listing-page.md`, add one line near the top: "Deep standard (22-section, ~3,150w) → use `skills/cag-bird-page-build.md`. This lean profile remains for minimal one-bird listings."

- [ ] **Step 5: Re-run the auditor to confirm the profile parses**

Run: `python3 scripts/final_page_audit.py --birds 2>&1 | sed -n '1,40p'`
Expected: runs clean; word-band no longer FAILs a ~3k-word page (roys may still flag missing-H4 until Phase 2 — acceptable).

- [ ] **Step 6: Commit**

```bash
git add scripts/final_page_audit.py skills/cag-bird-listing-page.md
git commit -m "audit(birds): deep word band + H1-H4 for 22-section bird pages"
```

---

## Phase 2 — Roys reference build

### Task 3: Image pipeline (assets/Roys → public/ + Higgsfield gaps)

**Files:**
- Create: `public/birds/roys/*` (SEO-renamed WebP + video posters)

- [ ] **Step 1: List the source media**

Run: `ls -la assets/Roys/`
Expected: the 7 images, 2 Roys videos, 4 art-directed WebPs (per spec §8).

- [ ] **Step 2: Convert/rename to public/** using the image map in spec §8. WebP <100KB where possible (Pillow, not sips — see memory). Poster frame for the hero video from "Roys, the perfect African Grey male…webp". Names: `roys-hero.webp`, `roys-personality.webp`, `roys-whats-included.webp`, `roys-trust-panel.webp`, `roys-gallery-1..5.webp`, `roys-shipping.webp`, plus copy the two `.mp4` to `public/birds/roys/`.

- [ ] **Step 3: Generate the 3 imageless-section images via Higgsfield** (per IMAGE-DESIGNS.md style wrapper + negative list): §10 key-decisions, §11 lifestyle, §13 training. Route output through `@cag-image-pipeline` (SEO rename, WebP, alt text). CITES-safe prompts (African Grey only, no other species, no logos/watermarks/🦜).

- [ ] **Step 4: Verify all referenced images exist + sizes**

Run: `ls -la public/birds/roys/ && du -sh public/birds/roys/*`
Expected: every file named in spec §8 present; WebP mostly <100KB.

- [ ] **Step 5: Commit**

```bash
git add public/birds/roys
git commit -m "assets(roys): SEO-renamed WebP set + Higgsfield section images"
```

### Task 4: Top modules — Hero C + Snapshot box + TOC

**Files:**
- Modify: `src/pages/available/roys/index.astro`

- [ ] **Step 1: Set H1 + meta + frontmatter** — H1 "Roys — Male Congo African Grey For Sale ($2,300, Hand-Raised & DNA-Sexed)"; keyword-rich `<title>` + meta (per `feedback_meta_format`); first-100-words include "congo african grey for sale".

- [ ] **Step 2: Build Hero C (trust-first + video)** — left: H1 + "$2,300 · ships nationwide" + USDA/CITES/DNA badge row + "Reserve Roys" clay pill (50px); right: `<video>` poster `roys-hero.webp`, `roys-video-playing.mp4`, **click-to-play, no autoplay** (motion rule). Shipping line `Ships nationwide · $185 airport · $350 home`.

- [ ] **Step 3: Build the AEO Snapshot box** (40–50w, spec §6 #1 snippet) — variant · sex · age 4mo · $2,300 · talking · documentation · ships.

- [ ] **Step 4: Build the TOC** with jump links (`#anchor`) to all 22 H2 sections (cag-toc module).

- [ ] **Step 5: Build + eyeball**

Run: `npx astro build >/dev/null 2>&1 && echo OK`
Expected: OK (no build errors).

- [ ] **Step 6: Commit**

```bash
git add src/pages/available/roys/index.astro
git commit -m "feat(roys): Hero C + AEO snapshot + TOC"
```

### Task 5: Sections 1–4 (Attention)

**Files:**
- Modify: `src/pages/available/roys/index.astro`

- [ ] **Step 1: Write sections 1–4** exactly per the spec §6 matrix rows 1–4 — Key Takeaway (H2 #1, AEO), Temperament (EBP), Talking ability (QAB, 40w snippet + link to playing video), and the **counter-snippet** §4 (PDB: "what $850 cuts" list → links `/how-to-avoid-african-grey-parrot-scams/` + `/african-grey-parrot-price/`). Keywords/entities/fan-out from the matrix. First-person plural. Anti-AI-writing pass. Each H2 conversational; use H3/H4 where the matrix calls for clusters/PAA.

- [ ] **Step 2: Build**

Run: `npx astro build >/dev/null 2>&1 && echo OK`
Expected: OK.

- [ ] **Step 3: Commit**

```bash
git add src/pages/available/roys/index.astro
git commit -m "feat(roys): sections 1-4 attention (counter-snippet)"
```

### Task 6: Sections 5–11 (Interest)

**Files:**
- Modify: `src/pages/available/roys/index.astro`

- [ ] **Step 1: Write sections 5–11** per matrix rows 5–11 — Documentation (EBP, H3 cluster DNA/leg-band/CITES/USDA/AAV → cites-doc + dna-tested pages), What's Included (QAB, `roys-whats-included.webp`), **Comparison** (Compare Table Style E: Roys vs Amie/Bery/Evie → sibling links + congo-vs-timneh), Health (EBP → health-guarantee, NO PBFD/Polyomavirus), Parents (`cag-parent-birds`, real info only), Key Decisions (BAB, fit-screening + key-decisions image), Lifestyle (BAB, 40–60yr + lifestyle image).

- [ ] **Step 2: Build**

Run: `npx astro build >/dev/null 2>&1 && echo OK`
Expected: OK.

- [ ] **Step 3: Commit**

```bash
git add src/pages/available/roys/index.astro
git commit -m "feat(roys): sections 5-11 interest (docs, comparison, parents)"
```

### Task 7: Sections 12–15 + 21 (Desire)

**Files:**
- Modify: `src/pages/available/roys/index.astro`

- [ ] **Step 1: Write sections 12–15 + 21** per matrix — Reviews MID (Testimonials A 3-up, `public/` buyer photos, NO per-bird Review schema), Training (HowTo → how-to-tame + training image), Food (QAB → diet/best-food, ledger pellet brands), Gallery (real-photos grid + both videos, SEO alt), and §21 Marketplace-vs-breeder (EBP contrast vs birdbreeders.com).

- [ ] **Step 2: Build**

Run: `npx astro build >/dev/null 2>&1 && echo OK`
Expected: OK.

- [ ] **Step 3: Commit**

```bash
git add src/pages/available/roys/index.astro
git commit -m "feat(roys): sections 12-15,21 desire (reviews, training, food, gallery)"
```

### Task 8: Sections 16–20 + 22 (Action) — incl. contact form + FAQ

**Files:**
- Modify: `src/pages/available/roys/index.astro`

- [ ] **Step 1: Write sections 16–20 + 22** per matrix — How to Buy (HowTo numbered steps), Shipping §17 (QAB, two-tier cost, IATA/Delta/United/American → location/city pages), Credentials §18 (**kept-verbatim** USDA AWA / CITES / DNA / Avian Vet block), FAQ §19 (6 PAA, **visible** + FAQPage schema), Reviews BOTTOM §20 (Testimonials A, photo #2), and §22 final CTA = **`cag-inquiry-form.astro` with its own `idPrefix`** + newsletter + homepage link.

- [ ] **Step 2: Build**

Run: `npx astro build >/dev/null 2>&1 && echo OK`
Expected: OK.

- [ ] **Step 3: Commit**

```bash
git add src/pages/available/roys/index.astro
git commit -m "feat(roys): sections 16-20,22 action (how-to-buy, shipping, FAQ, contact form)"
```

### Task 9: Schema, internal links, bidirectional homepage

**Files:**
- Modify: `src/pages/available/roys/index.astro`
- Modify: `src/pages/index.astro`

- [ ] **Step 1: Add/extend JSON-LD** — single `Product`+`Offer` (InStock, $2,300), `FAQPage` (6 Q matching the visible FAQ), `BreadcrumbList`, `Organization`. `dateModified` schema-only. No Review schema. Extend existing graph — never duplicate.

- [ ] **Step 2: Verify all internal-link targets exist** (spec §9 list)

Run: `for s in african-grey-parrots-for-sale congo-african-grey-for-sale congo-vs-timneh-african-grey african-grey-parrot-guide cites-african-grey-documentation dna-tested-african-grey-for-sale african-grey-parrot-health-guarantee african-grey-parrot-price how-to-avoid-african-grey-parrot-scams; do test -e "src/pages/$s/index.astro" && echo "OK $s" || echo "MISSING $s"; done`
Expected: all OK (fix any MISSING by adjusting the anchor target).

- [ ] **Step 3: Add reciprocal homepage→Roys link** in `src/pages/index.astro` (available-birds area) so the link is bidirectional.

- [ ] **Step 4: Build + verify rendered schema in dist/**

Run: `npx astro build >/dev/null 2>&1 && grep -o '"@type":"[A-Za-z]*"' dist/available/roys/index.html | sort | uniq -c`
Expected: Product, Offer, FAQPage, BreadcrumbList, Organization present; no second Product/AggregateOffer.

- [ ] **Step 5: Commit**

```bash
git add src/pages/available/roys/index.astro src/pages/index.astro
git commit -m "feat(roys): schema + bidirectional internal links"
```

### Task 10: Full audit + preview parity verification

**Files:** none (verification)

- [ ] **Step 1: Word count + heading check**

Run: `python3 scripts/final_page_audit.py --birds 2>&1 | sed -n '1,60p'`
Expected: roys PASS (or PASS-WITH-WARNINGS) — ~3,150 words, H1–H4 present, single Product/Offer, shipping line, no visible date, no PBFD.

- [ ] **Step 2: Start preview + screenshot desktop**

Use preview_start, navigate to `/available/roys/`, preview_console_logs (no errors), preview_screenshot (desktop). Confirm Hero C, snapshot, TOC, counter-snippet, comparison table, both review blocks, credentials block, contact form all render.

- [ ] **Step 3: Screenshot mobile (parity)**

preview_resize to 375px, preview_screenshot. Confirm mobile renders the mobile variants (floating-pill nav, sticky CTA, stacked sections) and **matches the prototype** intent — no broken layout, video click-to-play works.

- [ ] **Step 4: Regenerate sitemaps**

Run: `python3 scripts/generate_sitemaps.py 2>&1 | tail -5`
Expected: runs clean, 0 phantom URLs.

- [ ] **Step 5: Commit**

```bash
git add public dist 2>/dev/null; git add -A
git commit -m "chore(roys): sitemaps + audit pass"
```

### Task 11: Preview gate → user approval → deploy

**Files:** none (gate)

- [ ] **Step 1: Present the preview** (desktop + mobile screenshots + audit verdict) to the breeder. **Do NOT push until approved** (preview-before-apply rule).

- [ ] **Step 2: On approval, push (= deploy)**

```bash
git push origin main
```
Expected: GitHub Actions → Cloudflare Pages deploys; then live-verify `https://congoafricangreys.com/available/roys/` returns 200.

- [ ] **Step 3: Add the CLAUDE.md TOP rule** (session-end task per breeder request) — visual-companion + distribution-matrix methodology as a Non-Negotiable Rule; commit + push.

---

## Phase 3 — Batch the other 5 (separate plans)

Each of Amie (BAB), Bery (PAS), Jins & Jeni (PDB), Elad (EBP), Evie (QAB) gets its **own** plan:
run the methodology gate (visual companion → per-page distribution matrix → approval) using
`skills/cag-bird-page-build.md` + the research doc's per-page section, then build inheriting Roys'
proven system + its assigned hero (pairing in spec §5). Not pre-planned here because each requires its
own approved matrix. Trigger after Roys is live and confirmed.

---

## Self-Review

**Spec coverage:** §0 scope → Tasks 1–2 + Phase 3 note; §1 methodology → Task 1 skill + Task 11 Step 3; §2 H1–H6 → Task 1 + built in Tasks 4–8; §3 taxonomy → Task 1; §4 facts → Task 4; §5 hero → Task 4; §6 matrix → Tasks 4–8; §7 components → Tasks 4–8; §8 images → Task 3; §9 links → Task 9; §10 schema → Task 9; §11 open flags → Task 11 Step 3 + carried (review photos fallback in Task 7, age in Task 4). All covered.

**Placeholder scan:** no TBD/TODO; each content task points to the exact spec matrix rows + components + image files + link targets (the prose itself is written at execution following the spec + anti-ai-writing skill, which is the correct division for a content build).

**Type consistency:** image names (Task 3) reused in Tasks 4–8; component names (`cag-inquiry-form.astro`, Compare Style E, `cag-parent-birds`, `cag-faq-acc`, Testimonials A) consistent with spec §7; schema set identical in Task 9 and spec §10.

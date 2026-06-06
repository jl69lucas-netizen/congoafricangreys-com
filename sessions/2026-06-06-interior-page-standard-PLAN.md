# CAG Interior-Page Standard — Codification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Distill everything proven while building the homepage into (1) a reusable **CAG Interior-Page Standard**, (2) a **manual, copy-paste, step-by-step checklist (Hero → CTA)** the breeder can verify line-by-line, and wire it into (3) the correct agents/skills and (4) memories — so health, shipping, FAQ, privacy-policy, care/resource, about, why-choose, scam, and similar pages are built to the *same* homepage standard.

**Architecture:** One new human-facing manual (`MANUAL INTERIOR-PAGE CHECKLIST.md`, sibling to the existing `MANUAL SEO CHECKLIST-HOMEPAGE.md`) is the centerpiece. The machine-facing rules cascade through the existing master skill (`skills/cag-seo-master-checklist.md`) + the orchestrator (`cag-content-architect`) + the interior-page builder agents, plus 3 new memories. No new agent is created (the homepage QA flagged agent-proliferation and an orphan-page gap; we extend, not multiply).

**Tech Stack:** Markdown docs, agent `.md` frontmatter/Golden-Rule blocks, `memory/*.md` + `MEMORY.md` index, one idempotent Python injector script (mirrors `scripts/add_first_person_golden_rule.py`), `git` deploy.

**Scope — applies to / excludes (LOCKED, from user):**
- ✅ Applies to: health, shipping, FAQ, privacy policy, care/resource pages, about, why-choose-cag, scam guide, CITES-doc, health-guarantee, pros-and-cons, trusted-breeders, reviews, and any other informational/secondary page.
- ❌ Excludes (they have their own structure): comparison pages, location/state/city pages, all "…for-sale" money pages, blog posts.

---

## Source Evidence (already extracted — do not re-derive)

The 13 homepage sessions were read and mined. Key sources for each topic:

| Topic | Source file |
|---|---|
| 25-section build order, build contract, data/facts | `sessions/2026-05-29-homepage-build-progress.md` |
| Outline Gate (Rule 51), heading-count plan, special-elements plan, framework-per-section | `sessions/2026-05-29-homepage-outline-v2.md` |
| Entity 4-Move Loop, Verified-Claim Ledger, per-section entity table | `sessions/2026-06-03-homepage-entity-map.md` |
| Non-commodity audit-then-rewrite, gap-flags, ledger boundary | `sessions/2026-06-05-homepage-noncommodity-pass.md` |
| GEO/AEO dominance, declarative answer blocks, schema set, head-term sculpting | `sessions/2026-06-01-homepage-dominance-strategy.md` |
| a11y AA (dl misuse, contrast, target-size), perf (ClientRouter, fonts, WebP/Pillow), CSP, map pin, heading band | `sessions/2026-06-02-homepage-precision-fixes.md`, `sessions/2026-06-05-a11y-perf-fixes.md` |
| Icons-not-emoji, `::before` SVG trap, CLS img dims | `sessions/2026-06-05-a11y-perf-fixes.md` + CLAUDE.md §Design Rule 7 |
| Section seam logo divider (`.cag-seam` + `/cag-footer-logo.png`) | `src/pages/index.astro:299-306, 377` |
| "Honesty Policy" humor (Style-2) | git `1ad8733`; `src/pages/index.astro:599` |
| Shipping entities / two-tier line, first-person rollout | `sessions/2026-06-04-homepage-shipping-entities.md` |
| Agent-fit + orphan-page gap | `sessions/2026-06-05-a11y-perf-fixes.md`, `sessions/2026-06-05-qa-audit.md` |

---

## File Structure (what gets created / modified)

- **Create:** `MANUAL INTERIOR-PAGE CHECKLIST.md` (repo root) — the manual, the deliverable the user verifies.
- **Create:** `memory/reference_interior_page_standard.md` — pointer + deltas vs homepage.
- **Create:** `memory/project_section_seam_divider.md` — the `.cag-seam` footer-logo divider pattern.
- **Create:** `memory/feedback_humor_honesty_policy.md` — the Style-2 "Honesty Policy" humor mode.
- **Create:** `scripts/add_interior_standard_pointer.py` — idempotent injector adding one On-Startup pointer line to the interior-page builder agents.
- **Modify:** `MEMORY.md` — 3 new index lines.
- **Modify:** `skills/cag-seo-master-checklist.md` — add "Interior-Page Profile" section + cross-link the manual.
- **Modify:** `.claude/agents/cag-content-architect.md` — route interior pages to the standard.
- **Modify (via script):** `cag-about-builder`, `cag-purchase-guide`, `cag-species-guide-builder`, `cag-scam-specialist`, `cag-financial-strategist`, `cag-faq-agent`, `cag-section-builder`, `cag-trust-signals-agent` — On-Startup pointer to the manual.
- **Modify:** `CLAUDE.md` — register the manual + the new script in Reference Docs / Scripts.

---

## Task 1: Build the manual checklist skeleton + Pre-Build + Design Contract

**Files:**
- Create: `MANUAL INTERIOR-PAGE CHECKLIST.md`

- [ ] **Step 1: Write the file header + applies-to/excludes block + master TOC**

Top of file:
```markdown
# MANUAL INTERIOR-PAGE CHECKLIST — CongoAfricanGreys.com
> Copy-paste, verify-each-step build guide for every informational/secondary page,
> built to the SAME design + SEO standard as the homepage. Hero → CTA.
> Companion to `MANUAL SEO CHECKLIST-HOMEPAGE.md` (homepage-specific) and
> `skills/cag-seo-master-checklist.md` (machine workflow).

## APPLIES TO
health · shipping · FAQ · privacy policy · care/resource · about · why-choose-cag ·
scam guide · CITES-doc · health-guarantee · pros-and-cons · trusted-breeders · reviews
## DOES NOT APPLY TO (own structure)
comparison pages · location/state/city pages · all "…for-sale" money pages · blog posts

## HOW TO USE
Each ⬜ is one verifiable step. Do them top to bottom. Do not skip the GATES (⛔).
```
Then a linked TOC of all Parts (A–N) defined across Tasks 1–9.

- [ ] **Step 2: Write Part A — Pre-Build (read-first + Outline Gate)**

Must include, as ⬜ steps:
- Read `PRODUCT.md` + `DESIGN.md` (binding), `docs/design.md`, `docs/reference/seo-rules.md`, `docs/reference/components.md`, `docs/reference/page-width.md`.
- Read the data files the page touches: `data/price-matrix.json`, `data/financial-entities.json`, `data/clutch-inventory.json`.
- ⛔ **GATE 1 — Outline first (Rule 51):** produce H1–H6 tree, keyword-distribution table, competitor snapshot (top 5), special-elements plan, fan-out keywords. STOP for approval before writing any section.
- Confidence Gate ≥97% before any write to `src/pages/<slug>/index.astro`; else run the Clarification Checkpoint (write done work + log the one open question to the live session brief `## Open Flags`, ask ONE question, keep building unblocked parts).

- [ ] **Step 3: Write Part B — Design-System Contract (the "how it looks" lock)**

Embed the *actual* locked rules (not a pointer), as a verify-each checklist:
- Colors: Forest `#2D6A4F` (nav/headers) · Clay `#e8604c` (CTAs) · Cream `#faf7f4` (surface); `--gold`==`--clay`. AA variants: button fill `#c8472f`/`.bg-clay`, small clay text on light `#b04228`, clay on dark/green stays `#e8604c`/`#f08070`.
- Type (Direction D, global via `body.theme-d`): Newsreader serif H1–H6, IBM Plex Sans body; keep `font-lora`/`font-sora` utility classes — theme restyles them. NEVER hard-code `font-family` to fight the theme. Option-A fluid clamp: section H2/H3 carry NO size utilities.
- Buttons: primary CTA clay pill `border-radius:50px`; form submit `12px`.
- Cards: `<article>` → 20px radius, 1px `--border`, warm `rgba(60,30,10,…)` shadow, white surface; info cards green header band.
- Motion ≤0.2s, no bounce/parallax/autoplay.
- Icons = inline Feather SVG (`1em`, `currentColor`); KEEP only ✔ ✗ ★. NEVER 🦜 (use `/emoji/cag-congo.png` / `/emoji/cag-timneh.png`). NEVER put `<svg>` in CSS `content:` (Task 8 trap).
- Widths: outer `.container` 1200px; informational inner `.container-text` 760px; every `<p>` `max-width:70ch`. Infographics: 760px wrapper (informational), 400px desktop height.

- [ ] **Step 4: Verify the file parses and Parts A–B exist**

Run: `grep -n "^## " "MANUAL INTERIOR-PAGE CHECKLIST.md"`
Expected: lines for `## APPLIES TO`, `## HOW TO USE`, `## PART A`, `## PART B`.

- [ ] **Step 5: Commit**
```bash
git add "MANUAL INTERIOR-PAGE CHECKLIST.md" && git commit -m "docs(manual): interior-page checklist — header + pre-build + design contract"
```

---

## Task 2: Manual — Part C (Section build order + the seam-logo divider)

**Files:**
- Modify: `MANUAL INTERIOR-PAGE CHECKLIST.md`

- [ ] **Step 1: Write Part C.1 — Interior-page section order (Hero → CTA)**

Adapt the homepage's 25-section order to interior pages. Mandatory spine, in order:
1. **Hero** (`HeroV3`-style or split) — H1 (page-specific), eyebrow, subhead, dual CTA (form links only, no phone).
2. **Counter snippet** (`CounterSnippet`) — 4 liftable stats (e.g. 12+ Yrs · 100% CITES · $1,500 Floor · 24h). Rule 31.
3. **Key Takeaway / BLUF** (`KeyTakeawayV2`) — declarative answer to the page's core question.
4. **TOC** (`TocV3`) — required when page >1,500 words (Rule 29).
5–N. **Body sections** — page-topic-specific, each: conversational H2, EBP opening paragraph, woven links, entity 4-Move loop, declarative answer block.
- **Trust bar / stats** (`TrustStats`) where credibility matters.
- **FAQ** (`FaqAccordion`) — PAA-sourced, FAQPage schema (Rule: required).
- **How to Buy / Next Step** — 4-step where transactional intent exists.
- **Final CTA + Contact** (`ContactForm:application`) — LAST content section; H2 conversational; LocalBusiness map optional.
- Note: interior pages may DROP product-grid / breeding-pairs / compare-table sections that are money/comparison-page-owned — but KEEP hero, counter, key-takeaway, TOC (if long), FAQ, CTA.

- [ ] **Step 2: Write Part C.2 — The section seam divider (the "small footer logo between sections")**

Embed the verbatim pattern from `src/pages/index.astro:299-306,377`:
```html
<!-- Place between major sections (NOT every section — at editorial seams) -->
<div class="cag-seam" aria-hidden="true">
  <span class="cag-seam__line"></span>
  <img src="/cag-footer-logo.png" alt="" width="200" height="66" loading="lazy" />
  <span class="cag-seam__line"></span>
</div>
```
```css
/* scoped under the page wrapper (homepage uses .home-d) */
.home-d > .cag-seam{ display:flex; align-items:center; gap:26px; max-width:1100px; margin:0 auto; padding:.6rem 24px !important; border-top:0 !important; }
.home-d > .cag-seam + *{ border-top:0 !important; }
.cag-seam__line{ flex:1; height:1px; background:var(--rule); }
.cag-seam img{ height:30px; width:auto; display:block; opacity:.92; flex-shrink:0; }
@media (max-width:600px){ .home-d > .cag-seam{ gap:16px; } .cag-seam img{ height:24px; } }
```
Rules: `alt=""` (decorative), `loading="lazy"`, explicit `width/height` (CLS). For interior pages, swap the `.home-d` scope for the page's own wrapper class. Use at 4–8 editorial seams, not after every section.

- [ ] **Step 3: Verify**

Run: `grep -n "cag-seam\|cag-footer-logo" "MANUAL INTERIOR-PAGE CHECKLIST.md"`
Expected: ≥3 hits.

- [ ] **Step 4: Commit**
```bash
git add "MANUAL INTERIOR-PAGE CHECKLIST.md" && git commit -m "docs(manual): Part C — interior section order + seam-logo divider"
```

---

## Task 3: Manual — Part D (Voice, Headers, Humor)

**Files:**
- Modify: `MANUAL INTERIOR-PAGE CHECKLIST.md`

- [ ] **Step 1: Write Part D.1 — First-Person Brand Voice**

Rule + ✅/❌ examples (from CLAUDE.md):
- Write as the breeder: "we / us / our / here at C.A.Gs."
- ✅ "Here at C.A.Gs, **our** Congo and Timneh Greys…", "**we** hand-raise every chick", "**our** PCR DNA-sexing".
- ❌ "Both make exceptional companions", "African Greys are…" (when describing *our* offering).
- Exceptions (stay encyclopedic): taxonomy/species facts (`Psittacus erithacus` native to W & Central Africa), cited research, outbound-authority facts.
- Never overclaim — bounded by the Verified-Claim Ledger.

- [ ] **Step 2: Write Part D.2 — Two-Keyword Conversational Headers (Rule 28b) + full H1–H6**

- Every header conversational/Quora-style: What / How / Is / Can / Who.
- Two-keyword method: secondary KW + LSI/NLP/entity in each H2.
- Use ALL of H1–H6. Heading band (seo-rules): H1×1 · H2 25–35 · H3 40–50 · H4 10–20 · H5 5–10 · H6 3–8.
- Do NOT skip levels (Rule 52). Sibling grids share ONE level. Scale a small page proportionally but keep ≥1 each of H1–H4, and H5/H6 where depth genuinely exists.
- Example H2s (from live homepage): "What Is a Congo African Grey — the Classic Red-Tailed Talker?", "How Does C.A.Gs Ship African Grey Parrots Safely to All 50 States?"

- [ ] **Step 3: Write Part D.3 — Humor: the "Honesty Policy" (Style-2)**

- Tone: dry, transparent, anti-hype — turns honesty into a selling point. Disarms scam-wary buyers.
- Live example (`index.astro:599`): *"Honestly, the 'better' sex is the one whose personality fits your home…"* and the pricing note *"a sub-$1,500 'African Grey' is a wild-caught bird, a sick bird, or no bird at all."*
- Rules: humor never fabricates, never undermines CITES-safety, ≤1 light beat per section, never on legal/health claims.

- [ ] **Step 4: Verify + Commit**
Run: `grep -n "First-Person\|Honesty Policy\|Two-Keyword" "MANUAL INTERIOR-PAGE CHECKLIST.md"` (expect 3 hits)
```bash
git add "MANUAL INTERIOR-PAGE CHECKLIST.md" && git commit -m "docs(manual): Part D — voice, two-keyword headers, Honesty-Policy humor"
```

---

## Task 4: Manual — Part E (Entity 4-Move Loop + Verified-Claim Ledger)

**Files:**
- Modify: `MANUAL INTERIOR-PAGE CHECKLIST.md`

- [ ] **Step 1: Write Part E.1 — The 4-Move Loop (required per section)**

1. **Structural Critique** — read the section; name what is entity-thin/narrative-only.
2. **Recommended Entities + WHY** — each grounded (KG authority / PAA demand / competitor gap / buyer intent). (Recommend+Why rule.)
3. **Optimized Draft** — embed entities, verified facts only, ≥97% confidence, CITES-safe.
4. **Topical-Cluster Strategy** — internal-link anchors + schema feeding hub-and-spoke; extend existing JSON-LD, never duplicate; FAQ schema visible; verify in `dist/`.

- [ ] **Step 2: Write Part E.2 — Verified-Claim Ledger (copy current ledger verbatim)**

Copy the confirmed list from `sessions/2026-06-03-homepage-entity-map.md` + the entity agent:
- ✅ PCR-based DNA sexing · PBFD screening · Polyomavirus (APV) screening · board-certified avian vet · 3-day written health guarantee · CITES Appendix I captive-bred · USDA AWA license · hatch certificate + closed band · shipping $185 airport / $350 home (Delta/United/American) · chlamydiosis/psittacosis screening · UV-B + vitamin D3 · named talking Congo "Maxy".
- ❌ Do NOT assert: incubation temps for eggs, or anything not on this list, without breeder re-confirmation.
- Pointer: the live ledger of record is `cag-entity-incorporation-agent.md` + the entity map session — update THERE when the breeder confirms new claims.

- [ ] **Step 3: Verify + Commit**
Run: `grep -n "4-Move\|Verified-Claim\|Maxy" "MANUAL INTERIOR-PAGE CHECKLIST.md"` (expect ≥3)
```bash
git add "MANUAL INTERIOR-PAGE CHECKLIST.md" && git commit -m "docs(manual): Part E — entity 4-move loop + verified-claim ledger"
```

---

## Task 5: Manual — Part F (Links) + Part G (Non-Commodity audit-then-rewrite)

**Files:**
- Modify: `MANUAL INTERIOR-PAGE CHECKLIST.md`

- [ ] **Step 1: Write Part F — Internal + External links (woven mid-sentence)**

- Placement: beginning/middle of sentence, NEVER at the end. Internal same-tab; external new-tab + `rel="noopener noreferrer"` + ↗.
- External cap: max 2 / 300 words, max 1 / paragraph; verify 200 before insert (retry `-A "Mozilla/5.0"` — cites.org 403s to curl ≠ dead); add new URLs to `docs/reference/external-link-library.md` first.
- Authority targets proven on homepage: World Parrot Trust (parrots.org/encyclopedia/grey-parrot/), IUCN Red List, CITES.org, USDA APHIS, Alex Foundation, AAV, Cornell/AllAboutBirds.
- Jump-link teaser→deep-dive technique allowed (#anchor).

- [ ] **Step 2: Write Part G — Non-Commodity pass (audit-then-rewrite)**

- Method: audit ALL sections → classify STRONG / SHARPEN / REBUILD → rewrite ONLY weak. Do NOT rewrite strong/indexed copy (ranking-regression risk).
- Ledger-only; flag breeder-input gaps as GAP-FLAGS (prompts for Mark & Teri), never invent.
- Kill generic filler ("both make exceptional companions") → specific first-person breeder detail.
- High-resolution detail per ~500 words; a generic LLM couldn't write it.

- [ ] **Step 3: Verify + Commit**
Run: `grep -n "woven\|audit-then-rewrite\|GAP-FLAG\|STRONG / SHARPEN" "MANUAL INTERIOR-PAGE CHECKLIST.md"`
```bash
git add "MANUAL INTERIOR-PAGE CHECKLIST.md" && git commit -m "docs(manual): Parts F+G — link weaving + non-commodity audit-then-rewrite"
```

---

## Task 6: Manual — Part H (GEO/AEO) + Part I (Schema set) + Part J (Meta + Image SEO)

**Files:**
- Modify: `MANUAL INTERIOR-PAGE CHECKLIST.md`

- [ ] **Step 1: Write Part H — GEO/AEO (be the cited source)**

- Declarative answer block: each H2 question followed by a ≤320-char self-contained factual answer (liftable into AI Overview / featured snippet).
- Stat-forward liftable facts ("40–60 yr lifespan", "100–1,000 word vocabulary", "Appendix I since Jan 2017").
- Entity corroboration triangle: `sameAs` + Person + outbound authority links.
- Freshness: visible "Updated [Month Year]" + `dateModified` in schema.
- Bing/DuckDuckGo/Yahoo = Bing index → IndexNow covers it (key → api.indexnow.org; Bing/Yandex, not Google).

- [ ] **Step 2: Write Part I — Schema set per interior page**

Required/optional JSON-LD by page type:
- Always: `Organization` (name "Congo African Greys", canonical per credentials.md), `BreadcrumbList` (interior pages — unlike homepage), `WebPage`.
- FAQ section present → `FAQPage` (generate from the actual `<details>`; ONE block; verify not duplicated in `dist/`).
- Steps present → `HowTo`.
- Pricing present → `Product`/`Offer` (price, availability, CITES).
- Local/contact → `LocalBusiness` (geo + areaServed).
- Rule: extend existing JSON-LD, never duplicate; verify rendered in `dist/`, not source greps; `grep -rl "&lt;svg" dist/` must be empty.

- [ ] **Step 3: Write Part J — Meta titles/descriptions + Image SEO 5-element**

- Meta: canonical C.A.Gs long format, 4-tone (Urgency / Comparison / Transactional / Trust-Health); Title ≤205, Desc ≤185 (F1) or ≤300 (F2); never generic-short; no dupes vs other pages.
- Every image: SEO filename + alt ≤190 + title + caption+CTA + 250+ word description; none optional. `loading="lazy"` + explicit `width/height`. WebP via Pillow (sips writes fake WebP).

- [ ] **Step 4: Verify + Commit**
Run: `grep -n "≤320\|FAQPage\|4-tone\|5-element" "MANUAL INTERIOR-PAGE CHECKLIST.md"`
```bash
git add "MANUAL INTERIOR-PAGE CHECKLIST.md" && git commit -m "docs(manual): Parts H+I+J — GEO/AEO, schema set, meta + image SEO"
```

---

## Task 7: Manual — Part K (Technical hardening) + Part L (Deploy/verify) + Part M (Gotchas) + Part N (QA gate)

**Files:**
- Modify: `MANUAL INTERIOR-PAGE CHECKLIST.md`

- [ ] **Step 1: Write Part K — Technical hardening (a11y AA + perf)**

- a11y: skip link, ARIA landmarks, form labels, focus states, heading order (no skips), descriptive link text. Contrast: small clay `#b04228` on light; clay buttons white text; clay on green = white.
- `<dl>` only for true term→definition AND `<dt>` before `<dd>`; stat grids = neutral `<div>` (axe trap).
- NEVER `<svg>` in CSS `content:` — inject inline `<svg>` in markup (the trust-bar `::before` trap).
- target-size ≥24px (WCAG 2.5.8).
- Perf: remove ClientRouter if `grep -rn "transition:animate|transition:persist|astro:page-load|astro:after-swap"` = 0; merge Google Fonts into ONE non-blocking request (`media=print onload`); preload LCP hero (`fetchpriority=high`); defer gtag; explicit img dims (CLS). Report warm median-of-3 (single Lighthouse runs lie).
- CSP source of truth = `site/content/_headers` (deploy copies to public/); GA4 needs `*.google-analytics.com` wildcard.
- User-action note: Cloudflare Rocket Loader (`/70de/` unused JS) is edge-injected — disable in Cloudflare → Speed → Optimization (not a code fix).

- [ ] **Step 2: Write Part L — Deploy + verify**

- Output path: `src/pages/<slug>/index.html` or `index.astro` (NOT `site/content/`).
- `@cag-canonical-fixer` → `git push` (= deploy) → `@cag-deploy-verifier` (200 + canonical + IndexNow) → `python3 scripts/generate_sitemaps.py` (run after adding ANY page) → `sitemap-agent`.
- Sitemap clobber caveat: `deploy.yml` copies `site/content/*.xml` over public/ — generator must `write_both`.
- Always commit + push after build (push = deploy).

- [ ] **Step 3: Write Part M — Gotchas (don't repeat these)**

From the homepage "what went wrong" logs:
- Verify schema/SEO in `dist/` (rendered), NOT source greps.
- Count demotable headings BEFORE quoting an H-count target (sibling-grid + shared-component constraints).
- preview_screenshot resets scroll to 0 → hide DOM above target + `scrollTo(0,0)`; navigate resets viewport → resize before measuring.
- `grep -oF` for literals with `$` (`$` = EOL anchor).
- "Everything up-to-date" ≠ failure → check `git log origin/main..HEAD`.
- Measure full inventory/scope before quoting; script many-file edits (idempotent).

- [ ] **Step 4: Write Part N — Final QA gate (15-point, copy from master skill Phase 4)**

⛔ GATE: page is not "done" until all 15 pass. Pull the list from `skills/cag-seo-master-checklist.md` Phase 4 and embed it verbatim as ⬜ items.

- [ ] **Step 5: Verify whole manual + Commit**
Run: `grep -c "^- \[ \]\|^⬜\|^### " "MANUAL INTERIOR-PAGE CHECKLIST.md"` (sanity: large)
Run: `grep -n "^## PART" "MANUAL INTERIOR-PAGE CHECKLIST.md"` (expect Parts A–N)
```bash
git add "MANUAL INTERIOR-PAGE CHECKLIST.md" && git commit -m "docs(manual): Parts K–N — tech hardening, deploy, gotchas, QA gate (manual complete)"
```

---

## Task 8: Wire the standard into the master skill + content-architect

**Files:**
- Modify: `skills/cag-seo-master-checklist.md`
- Modify: `.claude/agents/cag-content-architect.md`

- [ ] **Step 1: Add "Interior-Page Profile" to the master skill**

Read the skill's existing exclusions line first (it already says "applies to all pages EXCEPT location and comparison pages"). Add a short section:
```markdown
## Interior-Page Profile (health/shipping/faq/care/policy/about/why/scam/etc.)
These pages use the homepage design + method. Human build guide:
`MANUAL INTERIOR-PAGE CHECKLIST.md`. Deltas vs homepage: keep hero/counter/
key-takeaway/TOC(if long)/FAQ/CTA + seam-logo dividers; drop product-grid,
breeding-pairs, compare-table (money/comparison-page-owned). ADD BreadcrumbList
(homepage omits it). Same: first-person voice, two-keyword headers, 4-move
entity loop + ledger, woven links, GEO/AEO declarative blocks, AA + perf gates.
Excludes (own structure): comparison, location, "…for-sale", blog.
```

- [ ] **Step 2: Route interior pages in content-architect**

In `.claude/agents/cag-content-architect.md`, add to its routing/On-Startup: when the requested page is an informational/secondary page (not comparison/location/for-sale/blog), the builder MUST follow `MANUAL INTERIOR-PAGE CHECKLIST.md` + the master skill's Interior-Page Profile.

- [ ] **Step 3: Verify + Commit**
Run: `grep -n "Interior-Page Profile\|MANUAL INTERIOR-PAGE" skills/cag-seo-master-checklist.md .claude/agents/cag-content-architect.md`
```bash
git add skills/cag-seo-master-checklist.md .claude/agents/cag-content-architect.md && git commit -m "feat(standard): route interior pages to the interior-page standard (skill + architect)"
```

---

## Task 9: Idempotent pointer injection into interior-page builder agents

**Files:**
- Create: `scripts/add_interior_standard_pointer.py`

- [ ] **Step 1: Write the injector (mirror `scripts/add_first_person_golden_rule.py`)**

```python
#!/usr/bin/env python3
"""Idempotently add one On-Startup pointer to interior-page builder agents."""
import pathlib
AGENTS = [
    "cag-about-builder","cag-purchase-guide","cag-species-guide-builder",
    "cag-scam-specialist","cag-financial-strategist","cag-faq-agent",
    "cag-section-builder","cag-trust-signals-agent",
]
POINTER = ("> **Interior-Page Standard (ALWAYS):** This page type follows the homepage "
           "design + method. Read `MANUAL INTERIOR-PAGE CHECKLIST.md` and the master "
           "skill's *Interior-Page Profile* before building. Keep seam-logo dividers, "
           "first-person voice, two-keyword headers, the 4-move entity loop + "
           "Verified-Claim Ledger, woven links, GEO/AEO declarative blocks, and the "
           "AA + perf gates.")
base = pathlib.Path(".claude/agents")
changed = 0
for name in AGENTS:
    p = base / f"{name}.md"
    if not p.exists():
        print(f"SKIP missing: {p}"); continue
    text = p.read_text()
    if "MANUAL INTERIOR-PAGE CHECKLIST.md" in text:
        print(f"OK already: {name}"); continue
    # insert right after the first "## Golden Rule" blockquote group
    marker = "## Golden Rule"
    if marker not in text:
        print(f"WARN no Golden Rule: {name}"); continue
    idx = text.index(marker)
    nl = text.index("\n", idx) + 1
    text = text[:nl] + POINTER + "\n" + text[nl:]
    p.write_text(text); changed += 1
    print(f"PATCHED: {name}")
print(f"\nDone. Patched {changed} agent(s).")
```

- [ ] **Step 2: Dry-run review then execute**

Run: `python3 scripts/add_interior_standard_pointer.py`
Expected: `PATCHED:` for each of the 8 (or `OK already` on re-run).

- [ ] **Step 3: Verify idempotency + no collateral**

Run: `python3 scripts/add_interior_standard_pointer.py` (2nd run)
Expected: all `OK already`, `Patched 0`.
Run: `grep -lc "MANUAL INTERIOR-PAGE CHECKLIST.md" .claude/agents/cag-*.md | wc -l`
Expected: 8.

- [ ] **Step 4: Commit**
```bash
git add scripts/add_interior_standard_pointer.py .claude/agents/ && git commit -m "feat(agents): add interior-page-standard pointer to 8 interior builders (idempotent)"
```

---

## Task 10: Memories + CLAUDE.md registration

**Files:**
- Create: `memory/reference_interior_page_standard.md`
- Create: `memory/project_section_seam_divider.md`
- Create: `memory/feedback_humor_honesty_policy.md`
- Modify: `MEMORY.md`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Write `memory/reference_interior_page_standard.md`**
Frontmatter `type: reference`. Body: the manual is `MANUAL INTERIOR-PAGE CHECKLIST.md`; applies-to vs excludes list; deltas vs homepage (BreadcrumbList added, money/compare sections dropped); link `[[project_section_seam_divider]]`, `[[feedback_humor_honesty_policy]]`, `[[feedback_entity_4move_loop]]`, `[[feedback_first_person_brand_voice]]`.

- [ ] **Step 2: Write `memory/project_section_seam_divider.md`**
Frontmatter `type: project`. Body: `.cag-seam` divider with `/cag-footer-logo.png` between major sections; the verbatim HTML/CSS; rules (alt="", lazy, width/height, scoped to page wrapper, 4–8 seams not every section). Source `src/pages/index.astro:299-306,377`.

- [ ] **Step 3: Write `memory/feedback_humor_honesty_policy.md`**
Frontmatter `type: feedback`. Body: Style-2 "Honesty Policy" dry/transparent humor; **Why:** disarms scam-wary buyers, turns honesty into trust; **How to apply:** ≤1 light beat/section, never on legal/health claims, never fabricate; example `index.astro:599`. Link `[[feedback_noncommodity_audit_then_rewrite]]`.

- [ ] **Step 4: Add 3 index lines to `MEMORY.md`**
```markdown
- [Interior-Page Standard](reference_interior_page_standard.md) — homepage design+method applied to health/shipping/faq/care/policy/about/etc.; MANUAL INTERIOR-PAGE CHECKLIST.md; excludes comparison/location/for-sale/blog
- [Section Seam Divider](project_section_seam_divider.md) — `.cag-seam` + /cag-footer-logo.png between major sections; verbatim HTML/CSS; decorative alt="" + CLS dims
- [Humor: Honesty Policy](feedback_humor_honesty_policy.md) — Style-2 dry/transparent humor disarms scam-wary buyers; ≤1 beat/section; never on legal/health; never fabricate
```

- [ ] **Step 5: Register manual + script in `CLAUDE.md`**
Add to Reference Docs: `MANUAL INTERIOR-PAGE CHECKLIST.md`. Add to Scripts: `scripts/add_interior_standard_pointer.py`.

- [ ] **Step 6: Verify + Commit**
Run: `ls memory/reference_interior_page_standard.md memory/project_section_seam_divider.md memory/feedback_humor_honesty_policy.md`
Run: `grep -c "Interior-Page Standard\|Section Seam Divider\|Honesty Policy" MEMORY.md` (expect 3)
```bash
git add memory/ MEMORY.md CLAUDE.md && git commit -m "docs(memory): interior-page standard + seam divider + honesty-policy humor; register manual+script"
```

---

## Task 11: Final verification + push

- [ ] **Step 1: Agent system still healthy**
Run: `bash scripts/health-sweep.sh --no-build`
Expected: agent integrity OK (66 agents), no secret leaks, no stale staging dirs.

- [ ] **Step 2: Build clean (the agent edits don't touch build, but confirm)**
Run: `npx astro build`
Expected: clean, page count unchanged (no new pages added by this plan).

- [ ] **Step 3: Push (deploy)**
```bash
git push
```
Run: `git log origin/main..HEAD` → expect empty (auto-push hook may have pushed).

- [ ] **Step 4: Report**
Summarize: manual created (Parts A–N), 8 agents + architect + master skill wired, 3 memories + index + CLAUDE.md updated, 1 idempotent script added.

---

## Self-Review (run after drafting all tasks)

1. **Coverage of the user's asks:** ✅ agent confirmation (done in chat) · ✅ analyze past sessions (Source Evidence table) · ✅ extract SEO/components/font/text/entity/seam-logo/humor/non-commodity/GEO/AEO (Parts B–N) · ✅ add to agents (Tasks 8–9) + memories (Task 10) · ✅ manual copy-paste step-by-step Hero→CTA (Tasks 1–7).
2. **Placeholder scan:** every content step embeds the actual rule text / code, not "write the section."
3. **Consistency:** the manual's Parts (A–N), the master-skill profile, the agent pointer, and the memories all name the same file `MANUAL INTERIOR-PAGE CHECKLIST.md` and the same applies-to/excludes list.
4. **Open question for the user (one):** confirm the excludes list — see chat.

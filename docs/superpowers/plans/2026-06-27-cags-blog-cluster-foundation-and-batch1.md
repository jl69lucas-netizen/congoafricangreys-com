# C.A.Gs Blog Cluster — Foundation + Batch 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the reusable blog system (skill reconciliation + 8 new components + hub rebuild), then run Batch 1 (cage-setup, training, talking-ability) through tiered research → breeder-selected strategy → pilot build → pass → rollout.

**Architecture:** Astro pages under `src/pages/blog/<slug>/index.astro` using BaseLayout (`body.theme-d` Direction-D inherited). Section skeleton composed from existing `cag-*.astro` components + 8 new `cag-blog-*.astro` components. Schema via BaseLayout `schemaJson` prop, verified in `dist/`. No unit-test harness exists for content pages — the test analog is **verification gates**: `npx astro build`, `python3 scripts/final_page_audit.py`, `dist/` schema/heading greps, a11y/perf.

**Tech Stack:** Astro, Direction-D CSS (`src/styles/direction-d.css`), Tailwind utility classes, JSON-LD, Firecrawl (Bing/competitor research), `scripts/final_page_audit.py`, `scripts/generate_sitemaps.py`.

**Source of truth:** `docs/superpowers/specs/2026-06-27-cags-blog-cluster-system-design.md`. Read FIRST each session: `PRODUCT.md`, `DESIGN.md`, `IMAGE-DESIGNS.md`. Work on `main` only. Commit + push after each task.

---

## File Structure

**New components (flat `cag-blog-*` convention, in `src/components/`):**
- `cag-blog-quick-answer.astro` — TOP special element; AEO snippet box. Props: `title`, `rows: {label,value}[]`.
- `cag-blog-comparison-table.astro` — Min/Recommended/Ideal table + breeder-verdict row. Props: `columns: string[]`, `rows: {item,values}[]`, `verdict: string`.
- `cag-blog-breeder-note.astro` — first-person E-E-A-T moat box. Props: `body` (slot).
- `cag-blog-callout.astro` — Mistake-Alert + Expert-Tip via `variant: 'mistake'|'tip'`. Line-icon, no emoji. Slot body.
- `cag-blog-myth-fact.astro` — two-column myth vs fact. Props: `myth`, `fact`.
- `cag-blog-decision-tree.astro` — branching yes/no block. Props: `nodes` tree.
- `cag-blog-related-posts.astro` — silo internal-link grid. Props: `posts: {title,slug,category}[]`.
- `cag-blog-sticky-cta.astro` — mobile-only persistent CTA bar. Props: `label`, `href`.

**Reconciled skill:** `skills/cag-blog-post.md` (new registered skill) + CLAUDE.md pointer.

**Rebuilt pages:** `src/pages/blog/index.astro` (hub); Batch 1 pilot `src/pages/blog/african-grey-parrot-cage-setup/index.astro`.

**Strategy docs (per page):** `sessions/2026-06-27-blog-strategy-<slug>.md`.

**Reference markup to lift (already on-brand DESIGN.md palette):** `assets/CAGs-BLOG-POSTS/BlogPostComponents/*.html` (desktop + `Mobile *`).

---

## Phase A — Foundation: Skill + Components

### Task A1: Inspect existing blog components before building new ones

**Files:** read-only.

- [ ] **Step 1: Read the existing blog-relevant components** so new ones match conventions and we don't duplicate.

Run:
```bash
cd /Users/apple/Downloads/CAG
for c in cag-blog-post cag-hero-3split cag-jump-nav cag-faq-static cag-inquiry-compact cag-bird-card-v2; do
  echo "===== src/components/$c.astro ====="; sed -n '1,40p' "src/components/$c.astro"; done
```
Expected: see prop interfaces + class conventions (Direction-D `font-lora`/`font-sora`, clay/forest tokens). Note which sections are already covered so Phase B/D import them instead of rebuilding.

- [ ] **Step 2: Confirm the type-scale reference** for parity.

Run: `grep -rnE 'font-size|clamp|h1|h2' assets/CAGs-BLOG-POSTS/BlogPostComponents/"Type Specimen.html" | grep -iv base64 | head -20`
Expected: the H1–H6 + body size/line-height values to mirror in component CSS so desktop/tablet/mobile heights match.

- [ ] **Step 3: Commit nothing** (inspection only). Proceed.

---

### Task A2: New component — `cag-blog-quick-answer.astro` (TOP special element)

**Files:**
- Create: `src/components/cag-blog-quick-answer.astro`
- Reference: `assets/CAGs-BLOG-POSTS/BlogPostComponents/Buyer_s Guide Article.html` (callout styling)

- [ ] **Step 1: Write the component** with a typed prop interface and Direction-D styling (forest header band, cream body, clay accent). Use line-icons, no emoji.

```astro
---
interface Row { label: string; value: string }
interface Props { title?: string; rows: Row[] }
const { title = 'Quick Answer', rows } = Astro.props;
---
<aside class="cag-blog-qa" aria-label={title}>
  <h2 class="cag-blog-qa__title font-lora">{title}</h2>
  <dl class="cag-blog-qa__grid">
    {rows.map((r) => (
      <div class="cag-blog-qa__row">
        <dt>{r.label}</dt><dd>{r.value}</dd>
      </div>
    ))}
  </dl>
</aside>
<style>
  .cag-blog-qa{border:1px solid var(--border);border-radius:20px;background:#fff;
    box-shadow:0 2px 10px rgba(60,30,10,.06);overflow:hidden;margin:1.5rem 0}
  .cag-blog-qa__title{background:#2D6A4F;color:#faf7f4;margin:0;padding:.75rem 1.25rem;font-size:1.15rem}
  .cag-blog-qa__grid{margin:0;padding:.5rem 1.25rem 1rem}
  .cag-blog-qa__row{display:flex;justify-content:space-between;gap:1rem;
    padding:.55rem 0;border-bottom:1px solid var(--line,#ede5dc)}
  .cag-blog-qa__row:last-child{border-bottom:0}
  .cag-blog-qa__row dt{font-weight:600;color:#3a2c22}
  .cag-blog-qa__row dd{margin:0;color:#5a5248;text-align:right}
</style>
```

- [ ] **Step 2: Create a scratch test page** to render it.

Create `src/pages/_scratch-blog-components.astro`:
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import QuickAnswer from '../components/cag-blog-quick-answer.astro';
---
<BaseLayout title="scratch" description="scratch" canonical="https://congoafricangreys.com/_scratch/" robots="noindex, nofollow" hideGlobalCta>
  <main class="container container-text" style="padding:2rem 0">
    <QuickAnswer title="African Grey Cage Quick Answer" rows={[
      {label:'Minimum cage', value:'36" × 24" × 48"'},
      {label:'Recommended', value:'48" wide, 5–7 perches'},
      {label:'Daily out-time', value:'4–5 hours'},
    ]} />
  </main>
</BaseLayout>
```

- [ ] **Step 3: Build and verify it compiles + renders.**

Run: `npx astro build 2>&1 | tail -5 && ls dist/_scratch-blog-components/index.html`
Expected: build succeeds; file exists. (Optional visual: preview_start → snapshot `/_scratch-blog-components/`.)

- [ ] **Step 4: Commit.**
```bash
git add src/components/cag-blog-quick-answer.astro src/pages/_scratch-blog-components.astro
git commit -m "feat(blog): add cag-blog-quick-answer TOP special-element component"
```

---

### Task A3: New component — `cag-blog-callout.astro` (Mistake-Alert + Expert-Tip)

**Files:** Create `src/components/cag-blog-callout.astro`; Modify scratch page to render both variants.

- [ ] **Step 1: Write the component** with `variant` prop and inline Feather line-icons (NOT emoji — per CLAUDE.md icon rule). Mistake = clay `#b04228`, Tip = forest `#2D6A4F`.

```astro
---
interface Props { variant: 'mistake' | 'tip'; title?: string }
const { variant, title } = Astro.props;
const isMistake = variant === 'mistake';
const heading = title ?? (isMistake ? 'Common Mistake' : 'Expert Tip');
---
<aside class={`cag-blog-callout cag-blog-callout--${variant}`} role="note">
  <span class="cag-blog-callout__icon" aria-hidden="true">
    {isMistake ? (
      <svg width="1.1em" height="1.1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
    ) : (
      <svg width="1.1em" height="1.1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1h6c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2z"/></svg>
    )}
  </span>
  <div class="cag-blog-callout__body">
    <strong>{heading}:</strong> <slot />
  </div>
</aside>
<style>
  .cag-blog-callout{display:flex;gap:.75rem;align-items:flex-start;padding:.9rem 1.1rem;
    border-radius:14px;margin:1.25rem 0;border:1px solid var(--border);background:#fff9f6}
  .cag-blog-callout--mistake{border-left:4px solid #b04228;color:#3a2c22}
  .cag-blog-callout--mistake .cag-blog-callout__icon{color:#b04228}
  .cag-blog-callout--tip{border-left:4px solid #2D6A4F;background:#eaf4ef}
  .cag-blog-callout--tip .cag-blog-callout__icon{color:#2D6A4F}
  .cag-blog-callout__body{line-height:1.55}
</style>
```

- [ ] **Step 2: Add both variants to the scratch page** (import + render `<Callout variant="mistake">Never place food bowls directly under perches.</Callout>` and a `tip`).

- [ ] **Step 3: Build + verify no raw `&lt;svg` leaked.**

Run: `npx astro build 2>&1 | tail -3 && grep -rl "&lt;svg" dist/ || echo "OK no escaped svg"`
Expected: build succeeds; "OK no escaped svg".

- [ ] **Step 4: Commit.**
```bash
git add src/components/cag-blog-callout.astro src/pages/_scratch-blog-components.astro
git commit -m "feat(blog): add cag-blog-callout mistake/tip line-icon callouts"
```

---

### Task A4: New component — `cag-blog-comparison-table.astro` (with breeder-verdict row)

**Files:** Create `src/components/cag-blog-comparison-table.astro`; render on scratch page.

- [ ] **Step 1: Write the component.** Forest header row, zebra body, clay verdict footer. Mobile: horizontal scroll wrapper so it stays readable ≤767px.

```astro
---
interface Props { columns: string[]; rows: { item: string; values: string[] }[]; verdict?: string }
const { columns, rows, verdict } = Astro.props;
---
<figure class="cag-blog-table">
  <div class="cag-blog-table__scroll">
    <table>
      <thead><tr>{columns.map((c) => <th>{c}</th>)}</tr></thead>
      <tbody>{rows.map((r) => (<tr><th scope="row">{r.item}</th>{r.values.map((v) => <td>{v}</td>)}</tr>))}</tbody>
    </table>
  </div>
  {verdict && <figcaption class="cag-blog-table__verdict"><strong>Breeder verdict:</strong> {verdict}</figcaption>}
</figure>
<style>
  .cag-blog-table{margin:1.5rem 0;border:1px solid var(--border);border-radius:16px;overflow:hidden;background:#fff}
  .cag-blog-table__scroll{overflow-x:auto}
  .cag-blog-table table{width:100%;border-collapse:collapse;min-width:520px}
  .cag-blog-table th{background:#2D6A4F;color:#faf7f4;text-align:left;padding:.7rem .9rem;font-weight:600}
  .cag-blog-table tbody th{background:#fff9f6;color:#3a2c22}
  .cag-blog-table td{padding:.7rem .9rem;border-bottom:1px solid var(--line,#ede5dc);color:#5a5248}
  .cag-blog-table tbody tr:nth-child(even) td{background:#fff9f6}
  .cag-blog-table__verdict{padding:.8rem 1.1rem;background:#fdeee9;color:#8a3a28;border-top:1px solid var(--border)}
</style>
```

- [ ] **Step 2: Render on scratch page** with the cage-setup Min/Recommended/Ideal data from the `.md` + a verdict line.

- [ ] **Step 3: Build + verify.** Run `npx astro build 2>&1 | tail -3`. Expected: success.

- [ ] **Step 4: Commit.**
```bash
git add src/components/cag-blog-comparison-table.astro src/pages/_scratch-blog-components.astro
git commit -m "feat(blog): add cag-blog-comparison-table with breeder-verdict row"
```

---

### Task A5: New components — breeder-note, myth-fact, decision-tree, related-posts, sticky-cta

**Files:** Create the 5 remaining components; render each on scratch page; one commit per component.

- [ ] **Step 1: `cag-blog-breeder-note.astro`** — slot-body box, clay left-border, "C.A.Gs Breeder Note" label, forest accent. First-person voice container.
```astro
---
interface Props { label?: string }
const { label = 'C.A.Gs Breeder Note' } = Astro.props;
---
<aside class="cag-blog-note"><p class="cag-blog-note__label font-sora">{label}</p><div class="cag-blog-note__body"><slot/></div></aside>
<style>
  .cag-blog-note{border-left:4px solid #e8604c;background:#fff9f6;border-radius:0 14px 14px 0;padding:1rem 1.25rem;margin:1.5rem 0}
  .cag-blog-note__label{margin:0 0 .35rem;font-size:.8rem;letter-spacing:.05em;text-transform:uppercase;color:#b04228;font-weight:700}
  .cag-blog-note__body{color:#3a2c22;line-height:1.6}
</style>
```
Render on scratch; `npx astro build 2>&1 | tail -3`; commit `feat(blog): add cag-blog-breeder-note E-E-A-T moat box`.

- [ ] **Step 2: `cag-blog-myth-fact.astro`** — props `myth`, `fact`; two-column (stack ≤640px); myth in muted, fact in forest. Render; build; commit `feat(blog): add cag-blog-myth-fact card`.

- [ ] **Step 3: `cag-blog-decision-tree.astro`** — props `question` + `branches: {answer,result}[]`; vertical branch list with clay arrows (line-icon). Render; build; commit `feat(blog): add cag-blog-decision-tree block`.

- [ ] **Step 4: `cag-blog-related-posts.astro`** — props `posts: {title,slug,category}[]`; 3-col grid (1-col mobile) of linked cards; internal links same-tab. Render; build; commit `feat(blog): add cag-blog-related-posts silo cluster`.

- [ ] **Step 5: `cag-blog-sticky-cta.astro`** — props `label`, `href`; `position:fixed;bottom:0` clay bar shown only `@media(max-width:767px)`; respects safe-area inset; `z-index` below header. Render; build; commit `feat(blog): add cag-blog-sticky-cta mobile bar`.

- [ ] **Step 6: Remove the scratch page + final build.**
```bash
rm src/pages/_scratch-blog-components.astro
npx astro build 2>&1 | tail -3
git add -A && git commit -m "chore(blog): remove component scratch page after verification"
```

---

### Task A6: Install + reconcile the blog skill

**Files:**
- Create: `skills/cag-blog-post.md`
- Modify: `CLAUDE.md` (add skill pointer under Skills → SEO & Content)

- [ ] **Step 1: Copy the draft, then strip stale ChatGPT contamination.**
```bash
cp "assets/CAGs-BLOG-POSTS/CAGs-Blog-Post-Skill.md" skills/cag-blog-post.md
```
Then edit `skills/cag-blog-post.md`:
- Replace `#1F7A4D` → `#2D6A4F`, `#FF6210`/`#FF8C00` → `#e8604c`.
- Replace `Montserrat`/`Poppins` → `Newsreader`; `Inter`/`Open Sans` → `IBM Plex Sans`.
- Replace emoji in special-element examples (💡 ⚠) with the line-icon rule reference.
- Delete the leftover "VibeTab" / "semantic entity" block at the end.

Verify the strip:
```bash
grep -nE '1F7A4D|FF6210|FF8C00|Montserrat|Poppins|VibeTab|💡|⚠' skills/cag-blog-post.md || echo "CLEAN"
```
Expected: `CLEAN`.

- [ ] **Step 2: Fold in the agreed system.** Add sections to `skills/cag-blog-post.md`: the 14-step section architecture, the desktop+mobile component map, the 8 new `cag-blog-*` components, the special-element TOP/MID/BOTTOM placement rule (TOP after TOC), the tiered Sprint 0.5 research method + enhanced output format (17 fields incl. competitor on-page KW audit + A/B/C matrix), voice/humor/length rules, and the baked-in gates. Reference the spec as source of truth.

- [ ] **Step 3: Register in CLAUDE.md.** Add under `#### SEO & Content Skills`:
```
- `skills/cag-blog-post.md` — THE blog-post builder skill (9 posts + hub); reconciled to DESIGN.md; 14-step section architecture, desktop+mobile component map, 8 cag-blog-* special-element components, tiered Sprint 0.5 research + enhanced ChatGPT-format output, Style-2 gated humor, 1,800–2,500 intent-scaled. Source of truth: docs/superpowers/specs/2026-06-27-cags-blog-cluster-system-design.md.
```

- [ ] **Step 4: Commit + push.**
```bash
git add skills/cag-blog-post.md CLAUDE.md
git commit -m "feat(skill): install + reconcile cag-blog-post skill to DESIGN.md"
git push origin main
```
Expected: push succeeds (deploy is irrelevant for skill/docs but keeps `main` current).

---

## Phase B — Blog Hub Rebuild

### Task B1: Rebuild `/blog/` hub to Direction-D standard

**Files:** Modify `src/pages/blog/index.astro`; reference `Hero / 3-Split` + `3-Column Grid` + `Mobile *` components.

- [ ] **Step 1: Present the hub H1→H6 outline to the breeder and get approval** (Heading Outline Gate — mandatory before code). Outline must be sequential, all six levels, ≥5 H5 + ≥5 H6. Do not touch page code until approved.

- [ ] **Step 2: Rebuild the hub** keeping the existing `posts[]` array + breadcrumbs + canonical: hero, intro, category filter, 3-col post grid (`cag-bird-card`-style cards adapted), newsletter, related money-page links, one CTA. Use `cag-blog-related-posts` for the silo block. Keep `Blog` CollectionPage/Breadcrumb schema via `schemaJson`.

- [ ] **Step 3: Build + audit.**
```bash
npx astro build 2>&1 | tail -3
python3 scripts/final_page_audit.py 2>&1 | grep -iE 'blog/?$|hub|PASS|FAIL' | head
grep -c '"@type"' dist/blog/index.html
```
Expected: build success; audit PASS for the hub; schema present in `dist/`.

- [ ] **Step 4: Commit + push.**
```bash
git add src/pages/blog/index.astro
git commit -m "feat(blog): rebuild /blog/ hub to Direction-D standard"
git push origin main
```

---

## Phase C — Batch 1 Tiered Research → Strategy Docs

> Batch 1 pages: `african-grey-parrot-cage-setup`, `african-grey-parrot-training`, `african-grey-parrot-talking-ability`. (Hub done in Phase B.)

### Task C1: Tiered Sprint 0.5 research per Batch-1 page

**Files:** Create `sessions/2026-06-27-blog-strategy-<slug>.md` × 3.

- [ ] **Step 1: 30-competitor scan (once).** Run `@cag-competitor-intel --all` (or read the latest `docs/research/` output if fresh) to flag which of the 30 own each Batch-1 topic + their gap. Do NOT deep-audit all 30.

- [ ] **Step 2: Per page, deep-audit the 6 leaders** — 3 Google (from the page's `.md`) + 3 fresh Bing (Firecrawl search on the primary keyword). For each leader fill the on-page keyword audit table: KW in slug/title/meta/H1, on-page count, variations, entity types, content category. Use `@cag-framework-agent` for voice/angle/H1–H6 extraction and `@cag-paa-agent` for real PAA.

- [ ] **Step 3: Write the strategy doc** using the 17-field enhanced format from the spec §4. Pull the page's `.md` content (text already extracted to scratch) + images inventory. Weight keyword universe to 6+ word long-tail + conversational/voice queries. Include the A/B/C section distribution matrix and the framework/angle/keyword OPTIONS (each Recommended + why + trade-off).

- [ ] **Step 4: Verify no fabricated data.** Every competitor metric must be fetched (mark un-fetchable as `NOT FETCHED`, never invented). Commit:
```bash
git add sessions/2026-06-27-blog-strategy-*.md
git commit -m "research(blog): Batch-1 tiered Sprint 0.5 strategy docs (cage/training/talking)"
git push origin main
```

- [ ] **Step 5: BREEDER GATE — present the 3 strategy docs.** Breeder selects frameworks, angles, entities, keywords, variations per page. Record selections back into each strategy doc. **No page code until selections are made.**

---

## Phase D — Pilot Build: Cage Setup

### Task D1: Build `african-grey-parrot-cage-setup` as the pilot

**Files:** Modify `src/pages/blog/african-grey-parrot-cage-setup/index.astro`; place images into `public/` (SEO-renamed WebP via `@cag-image-pipeline`).

- [ ] **Step 1: Heading Outline Gate.** Present the full H1→H6 outline (from the strategy doc, with breeder's selections) and get explicit approval. Sequential, all six levels, ≥5 H5 + ≥5 H6. No code until approved.

- [ ] **Step 2: Build the page** to the 14-step section architecture using existing `cag-*` + the 8 new `cag-blog-*` components. Honor: TOP Quick-Answer after TOC, MIDDLE module (decision-tree or available-birds soft-CTA), BOTTOM conversion module with shipping line, first-person voice, Style-2 humor (cage page = humor allowed, ≤1/section), 1,800–2,500 words. HowTo + Article + FAQPage + Breadcrumb schema via `schemaJson`. Images: lift `African_Grey_Perch_Selection_Guide.png` etc. → SEO-renamed WebP in `public/`, 5-element image SEO.

- [ ] **Step 3: Verification gates.**
```bash
npx astro build 2>&1 | tail -3
python3 scripts/final_page_audit.py 2>&1 | grep -iE 'cage-setup|PASS|FAIL|WARN'
# schema present + not escaped:
grep -o '"@type": *"[A-Za-z]*"' dist/blog/african-grey-parrot-cage-setup/index.html | sort -u
grep -rl "&lt;svg" dist/blog/african-grey-parrot-cage-setup/ || echo "OK icons"
# heading levels present:
for h in h1 h2 h3 h4 h5 h6; do printf "%s: " $h; grep -oc "<$h" dist/blog/african-grey-parrot-cage-setup/index.html; done
```
Expected: build success; audit PASS; HowTo+Article+FAQPage+BreadcrumbList present; "OK icons"; ≥5 h5 and ≥5 h6.

- [ ] **Step 4: Sitemaps + push.**
```bash
python3 scripts/generate_sitemaps.py 2>&1 | tail -3
git add -A
git commit -m "feat(blog): build african-grey-parrot-cage-setup pilot page"
git push origin main
```

- [ ] **Step 5: BREEDER PASS GATE.** Present the live/preview page. Breeder reviews exactly as homepage + bird pages. Iterate until pass. **Do not roll out until the pilot passes.**

---

## Phase E — Rollout (after pilot pass)

### Task E1: Apply the passed pattern to the remaining Batch-1 pages

**Files:** Modify `src/pages/blog/african-grey-parrot-training/index.astro`, `.../african-grey-parrot-talking-ability/index.astro`.

- [ ] **Step 1: Per page — Heading Outline Gate** (present + approve outline from its strategy doc).
- [ ] **Step 2: Build to the passed pilot pattern** with that page's selected framework/angle/entities. Talking-ability + training = care-guide depth (fuller). Training/talking humor allowed; keep health claims inside the Verified-Claim Ledger.
- [ ] **Step 3: Verification gates** (same commands as D1 Step 3, swapping the slug). Expected: PASS each.
- [ ] **Step 4: Sitemaps + commit + push** per page.
- [ ] **Step 5: Deploy-verify the batch.** Run `@cag-deploy-verifier` for the 3 Batch-1 slugs + hub. Expected: 200s, absolute canonicals, IndexNow accepted.

### Task E2: Batches 2 & 3 repeat Phase C→E

- [ ] **Step 1: Batch 2** (price, best-place-to-buy, vs-eclectus): repeat Task C1 (research → strategy → breeder selection), build the first as pilot-or-direct (pattern already passed), gate each outline, verify, deploy.
- [ ] **Step 2: Batch 3** (facts, health-problems, beginners): same. **health-problems = ZERO humor** (medical), claims inside Verified-Claim Ledger; vs-eclectus + beginners use the decision-tree component.

---

## Self-Review — Spec Coverage Check

- Section architecture → Phases B/D build to spec §2 (14 steps + 3 slots). ✓
- Component map + 8 new components → Tasks A2–A5 (all 8) + parity via `Mobile *` references + Type Specimen lock (A1 Step 2). ✓
- Tiered research + enhanced output (17 fields, on-page KW audit, A/B/C) → Task C1. ✓
- Breeder selection of frameworks/angles/entities/keywords → C1 Step 5 gate. ✓
- Agent stack → referenced in C1/D1/E1 (intel, framework, paa, blog-post, faq, entity, image, deploy-verifier). ✓
- Voice/humor/length → D1 Step 2, E1 Step 2, E2 (health = zero humor). ✓
- Skill reconciliation (palette/fonts/emoji/VibeTab) → Task A6. ✓
- Gates (heading outline, line-icons, shipping line, schema-in-dist, never-visible-date, type parity, final_page_audit) → embedded in B1/D1/E1 verification steps. ✓
- Build pilot → pass → roll out cadence → Phases D→E. ✓
- Work on main + commit/push each task → every task's final step. ✓

**Note on TDD adaptation:** this domain has no unit-test harness; verification gates (`astro build`, `final_page_audit.py`, `dist/` greps, deploy-verify) are the test analog and are explicit in every build task, matching the project's established `cag-final-page-pass` workflow.

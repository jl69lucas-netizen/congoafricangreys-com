# Individual Bird Listing Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a governing skill + Astro page builder for individual African-Grey *bird listing* pages, then generate the 9 already-declared `/available/<slug>/` pages that currently 404.

**Architecture:** A new skill (`skills/cag-bird-listing-page.md`) defines the per-bird page profile (section order, ~700–1,000 word band, schema, sell-and-retire lifecycle). `cag-bird-personality` is promoted from card-maker to page builder that consumes the skill; `cag-clutch-manager` gains create/retire responsibility for the page (not just the JSON status). Pages mirror the existing `congo-african-grey-for-sale/index.astro` idiom (BaseLayout + TrustBar + CTA + Schema + Breadcrumb) and reuse `cag-section-builder`, `cag-faq-agent`, `cag-financial-strategist` pricing, and `cag-canonical-fixer`/`cag-redirect-manager` for the sold→redirect step.

**Tech Stack:** Astro (`src/pages/available/<slug>/index.astro`), `body.theme-d` Direction-D CSS, JSON-LD `Product`+`Offer`, data from `data/clutch-inventory.json` + `data/bird-inventory.json` + `data/financial-entities.json` + `data/price-matrix.json`.

---

## Source-doc conversion ledger (MFS → CAG)

This plan derives from an MFS puppy-page guide. The following conversions are **binding** — they are the "honesty-based" intake decisions:

**KEEP (converted):** per-animal page section order; buyer-archetype differentiation; what's-included block; per-page Product/Offer schema; cross-link to hub + siblings; status lifecycle.

**REJECT (do not import):**
- ❌ Geo-distribution per animal (splitting states across listings) — **cannibalizes CAG's 50+ location pages**. Geography stays in the location cluster; a bird page targets *the bird + "African Grey for sale"* only.
- ❌ 2,500-word target — replaced by **700–1,000 words** (decided 2026-06-18). Depth lives on evergreen pages via internal links; bird pages are ephemeral (retired on sale).
- ❌ All MFS facts (Omaha, Lawrence & Cathy, $1,200, Embark, DA2PP/Bordetella, "hypoallergenic," 2-yr warranty). Use CAG facts only; every health/credential claim must pass the **Verified-Claim Ledger** in `cag-entity-incorporation-agent`.
- ❌ Inventing names/personalities — birds are real (Bery, Amie, Roys, Jins & Jeni, Elad, Evie + sold Joys/Loti/Carl).
- ❌ Traffic/conversion projections — speculation, omit.

---

## File Structure

- `skills/cag-bird-listing-page.md` — NEW. The page profile + section order + schema + lifecycle rules. Single responsibility: "how to build/retire one bird listing page."
- `sessions/2026-06-18-bird-listing-baseline.md` — NEW. RED baseline transcript (unguided agent output + gap annotation).
- `src/pages/available/bery/index.astro` — NEW. Reference implementation (first real page).
- `src/pages/available/<slug>/index.astro` ×8 — NEW. Remaining available birds.
- `.claude/agents/cag-bird-personality.md` — MODIFY. Add "Bird Listing Page" mode that consumes the skill.
- `.claude/agents/cag-clutch-manager.md` — MODIFY. Add create-page (available) / retire-page (sold→301) responsibility.
- `CLAUDE.md` — MODIFY. Register the skill + add a "build a bird page" Quick Start line.
- `data/clutch-inventory.json` — READ ONLY here (source of truth for slugs/status/price; do not restructure).

---

## Task 1: RED baseline for the skill (watch it fail first)

**Files:**
- Create: `sessions/2026-06-18-bird-listing-baseline.md`

The writing-skills Iron Law: no skill without a failing test first. We must observe what an unguided agent does building a bird page before writing the skill.

- [ ] **Step 1: Dispatch an unguided subagent**

Dispatch a `general-purpose` agent with ONLY this prompt (no skill, no this-plan context):

```
Build an individual "for sale" web page for one of our African Grey parrots named Bery
(female Congo, $1,700, available). Output the page copy + any schema you'd include.
```

- [ ] **Step 2: Record the baseline verbatim**

Paste the full output into `sessions/2026-06-18-bird-listing-baseline.md` under `## RED Baseline (unguided)`.

- [ ] **Step 3: Annotate the gaps**

Under `## Gap Annotation`, list every failure vs CAG rules, e.g. (expected, from known weaknesses):
- Missing CITES Appendix I / captive-bred framing
- Missing the 6 required trust signals (USDA AWA, CITES docs, DNA cert, avian-vet cert, hatch cert+band, weaning status)
- Missing canonical shipping line `Ships nationwide · $185 airport · $350 home`
- Third-person voice instead of first-person "here at C.A.Gs / our"
- No Product/Offer schema, or fabricated reviewCount/rating
- Fabricated health claims (vaccines/warranty) not in the ledger
- Geo-stuffing or generic filler ("makes a great companion")
- No sell-and-retire lifecycle note

- [ ] **Step 4: Commit the baseline**

```bash
git add sessions/2026-06-18-bird-listing-baseline.md
git commit -m "test(bird-page): RED baseline — unguided bird listing page + gap annotation"
```

---

## Task 2: GREEN — write the `cag-bird-listing-page` skill

**Files:**
- Create: `skills/cag-bird-listing-page.md`

Write the MINIMAL skill that fixes the Task-1 gaps. Address those specific failures; do not pad.

- [ ] **Step 1: Write the skill**

```markdown
---
name: cag-bird-listing-page
description: Use when building, rebuilding, or retiring an individual African Grey *bird* listing page at /available/<slug>/ (one page per real bird in clutch-inventory.json) — distinct from variant/location/for-sale cluster pages.
---

# CAG Individual Bird Listing Page

## Overview
One indexable page per real, available bird. Job = **convert**, not educate. 700–1,000 words
of bird-specific copy; depth is linked out to evergreen pages, never re-explained here.

## When to use
- A bird in `data/clutch-inventory.json` has status `available`/`reserved` but no page on disk.
- NOT for: variant pages (cag-variant-specialist), location pages (cag-location-builder),
  comparison/for-sale cluster, blog. Those have their own builders.

## Hard rules (inherit all CLAUDE.md Non-Negotiables)
- First-person voice: "here at C.A.Gs, **our** Bery…".
- Canonical shipping line under trust badges: `Ships nationwide · $185 airport · $350 home`.
- 6 trust signals required on every listing (bird-inventory.json
  `trust_signals_required_on_every_listing`): USDA AWA #, CITES captive-bred docs, DNA sex
  certificate, avian-vet health certificate, hatch certificate + band number, weaning status.
- CITES Appendix I captive-bred framing; never wild-caught.
- Every price from clutch-inventory.json / price-matrix.json — never hardcode a different number.
- No visible date anywhere (schema dateModified only).
- Health/credential claims bounded by the Verified-Claim Ledger — no vaccines/warranty/board-cert
  beyond what the breeder confirmed.
- NO geography targeting (no city/state lists) — that cannibalizes location pages.

## Section order (Hero → CTA)
1. Breadcrumb: Home › African Greys for Sale › <Bird>
2. Hero = Bird Vitals (name, sex, variant, age, price_display, status, one-line personality hook) + primary inquiry CTA
3. About <Bird> (archetype from cag-bird-personality: CLEO/REX/NOVA/SAGE/IRIS) — first-person
4. Health & Documentation (the 6 trust signals as a checklist; link to /african-grey-parrot-health-guarantee/ + /cites-african-grey-documentation/)
5. Why <Bird> (5–6 bullets, bird-specific, ledger-safe)
6. Pricing & What's Included (price_display + delivery_options from financial-entities.json; deposit_typical; shipping line)
7. Parent Birds (from bird-inventory.json aviary; link to /african-grey-breeding-pair-for-sale/)
8. FAQ (cag-faq-agent, 5–6 Q, FAQPage JSON-LD, visible)
9. Other Available Birds (siblings with status available) + link to hub /african-grey-parrots-for-sale/
10. Inquiry CTA (cag-inquiry-form; pass hideGlobalCta in BaseLayout)

## Schema
Per-bird `Product` + single `Offer` (NOT AggregateOffer — that's the variant page).
`offers.availability` = InStock (available) / PreOrder (pending_weaning) / SoldOut (sold).
No `aggregateRating` unless a real, attributed review exists. dateModified only.

## Sell-and-retire lifecycle
On status → `sold`: keep the page, add a "Sold" state, OR 301 to the variant page via
cag-redirect-manager. Never leave a sold bird as InStock. Update sitemap.

## Common mistakes
- Re-teaching species facts (link out instead) · geo-stuffing · third-person · fabricated
  reviews/warranty · hardcoded price · AggregateOffer on a single bird · visible date.
```

- [ ] **Step 2: Re-run the Task-1 scenario WITH the skill**

Dispatch a fresh `general-purpose` agent with the same Bery prompt **plus** "Follow skills/cag-bird-listing-page.md." Confirm it now: uses first-person, includes the 6 trust signals + shipping line, emits Product/Offer (no fake rating), omits geography, omits fabricated health claims.

- [ ] **Step 3: Refactor — close loopholes**

Add any NEW rationalization the agent used to a `## Common mistakes` / red-flags line. Re-test until clean.

- [ ] **Step 4: Word-count + commit**

```bash
wc -w skills/cag-bird-listing-page.md   # expect < 500
git add skills/cag-bird-listing-page.md sessions/2026-06-18-bird-listing-baseline.md
git commit -m "feat(bird-page): GREEN — cag-bird-listing-page skill passes baseline gaps"
```

---

## Task 3: Build the reference page `/available/bery/`

**Files:**
- Create: `src/pages/available/bery/index.astro`

Mirror `src/pages/congo-african-grey-for-sale/index.astro` (BaseLayout + Breadcrumb + TrustBar + Schema + CTA, `hideGlobalCta`). Pull all facts from data files — Bery: female Congo, `$1,700`, available, slug `/available/bery/`, "Hand-raised female, gentle temperament" (→ SAGE/IRIS archetype).

- [ ] **Step 1: Scaffold the page from data**

```astro
---
import BaseLayout from '../../../layouts/BaseLayout.astro';
import TrustBar from '../../../components/TrustBar.astro';
import CTA from '../../../components/CTA.astro';
import Schema from '../../../components/Schema.astro';
import Breadcrumb from '../../../components/Breadcrumb.astro';

const title = "Bery — Hand-Raised Female Congo African Grey | $1,700 | C.A.Gs";
const description = "Meet Bery, our gentle hand-raised female Congo African Grey. CITES-documented, DNA-sexed, $1,700. Ships nationwide · $185 airport · $350 home. From our Midland, TX aviary.";
const canonical = "https://congoafricangreys.com/available/bery/";

const productSchema = {
  "@type": "Product",
  "name": "Bery — Female Congo African Grey",
  "description": "Hand-raised female Congo African Grey (Psittacus erithacus erithacus), CITES Appendix I captive-bred, DNA-sexed, gentle temperament.",
  "offers": {
    "@type": "Offer",
    "price": "1700",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "Organization", "name": "C.A.Gs – Midland, TX" }
  }
};
---
<BaseLayout {title} {description} {canonical} hideGlobalCta>
  <!-- Sections 1–10 per skills/cag-bird-listing-page.md, first-person, 700–1,000 words -->
</BaseLayout>
```

- [ ] **Step 2: Fill sections 2–10** using the skill's section order, the 6 trust signals, the shipping line, and the FAQ (delegate FAQ to `cag-faq-agent`).

- [ ] **Step 3: Verify rendered output (not source)**

```bash
npx astro build
grep -c '"@type": "Product"' dist/available/bery/index.html   # expect 1
grep -o 'Ships nationwide · \$185 airport · \$350 home' dist/available/bery/index.html
grep -ci 'updated\|last modified' dist/available/bery/index.html   # expect 0 visible dates
```
Expected: Product schema present, shipping line present, no visible date.

- [ ] **Step 4: Commit**

```bash
git add src/pages/available/bery/index.astro
git commit -m "feat(bird-page): build reference page /available/bery/ from skill"
```

---

## Task 4: Generate the remaining 8 available/reserved pages

**Files:**
- Create: `src/pages/available/{amie,roys,jins-jeni,elad,evie}/index.astro` (available)
- Create: pages for any other non-sold slugs in clutch-inventory.json at build time

Only build pages for birds whose status is NOT `sold`. Sold birds (Joys, Loti, Carl) get a redirect in Task 5, not a page.

- [ ] **Step 1:** For each non-sold bird, copy the Bery pattern, swapping name/sex/variant/age/price_display/notes→archetype from `clutch-inventory.json`. Jins & Jeni is a **pair** — link to `/african-grey-breeding-pair-for-sale/` and price as the pair entry.
- [ ] **Step 2: Build + verify each** with the Task-3 Step-3 greps (loop over slugs).
- [ ] **Step 3: Commit** `feat(bird-page): build remaining available bird listing pages`.

---

## Task 5: Sold-bird redirects + sitemap + wiring

**Files:**
- Modify: `site/content/_redirects`
- Modify: `.claude/agents/cag-clutch-manager.md`, `.claude/agents/cag-bird-personality.md`, `CLAUDE.md`
- Run: `scripts/generate_sitemaps.py`

- [ ] **Step 1: Redirect sold slugs** (`cag-redirect-manager`): `/available/joys/ → /congo-african-grey-for-sale/` (and Loti, Carl). Validate targets exist on disk.
- [ ] **Step 2: Wire agents** — add to `cag-clutch-manager` Golden-Rule scope: "on available→create `/available/<slug>/` via cag-bird-listing-page; on sold→retire + 301." Add to `cag-bird-personality` a "Bird Listing Page mode" pointer to the skill.
- [ ] **Step 3: Register in CLAUDE.md** — add `skills/cag-bird-listing-page.md` to the Skills list + a Quick Start line: "I want to list an available bird → `cag-bird-listing-page` (reads clutch-inventory.json)".
- [ ] **Step 4: Regenerate sitemaps + verify** `python3 scripts/generate_sitemaps.py` (0 phantom URLs), then `bash scripts/health-sweep.sh --no-build`.
- [ ] **Step 5: Commit + push** (per Always-commit-and-push rule) `feat(bird-page): sold redirects, sitemap, agent wiring + CLAUDE.md registration`.

---

## Self-Review
- Spec coverage: skill (T2) ✓, pages (T3–T4) ✓, lifecycle/redirects (T5) ✓, honesty conversions encoded in skill hard-rules ✓.
- Placeholder scan: section bodies are delegated to the skill+faq-agent by design, not TBDs; schema/scaffold code is complete.
- Type consistency: `Product`+`Offer` (single bird) vs `AggregateOffer` (variant page) kept distinct throughout.

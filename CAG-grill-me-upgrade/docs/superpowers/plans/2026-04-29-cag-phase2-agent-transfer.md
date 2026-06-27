# CAG Phase 2 — Full Agent Transfer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transfer all 39 remaining MFS agents to CAG `.claude/agents/`, replacing Maltipoo/MFS domain references with African Grey/CAG equivalents, and create the foundational data stubs those agents depend on.

**Architecture:** Wave-based parallel execution — Task 0 creates data stubs (unblocks page builders), then Tasks 1–8 run as parallel waves grouped by complexity. Light agents (9) are pure substitution; moderate agents (17) need section rewrites; heavy agents (13) need full domain rewrites. Each wave commits independently.

**Tech Stack:** Markdown agent files. No code compilation. Verification is grep-based.

**Execution order:**
- **Task 0 (sequential):** Data stubs — unblocks all subsequent page builder agents
- **Tasks 1–4 (parallel):** Light + analytics + content architecture + content writers
- **Tasks 5–6 (sequential):** Section builder first (Task 5), then page builders (Task 6)
- **Tasks 7–8 (parallel):** Domain-specific heavy + variant/product agents
- **Task 9 (sequential):** Final verification across all 39 files

---

## Global Substitution Map (apply to EVERY file)

| Find | Replace |
|------|---------|
| MaltipoosForsale.com | CongoAfricanGreys.com |
| MaltipoosForsale | CongoAfricanGreys |
| `MFS` | `CAG` |
| `mfs-` (CSS class prefix) | `cag-` |
| Maltipoo / maltipoo / puppy / dog | African Grey parrot / bird / parrot |
| Lawrence & Cathy / Lawrence / Cathy | `[BREEDER_NAME]` |
| Omaha, Nebraska | `[BREEDER_LOCATION]` |
| `site2/` | `site/content/` |
| `/index.html` | (remove — CAG uses .md files) |
| Embark DNA | DNA sexing certificate |
| OFA certification | Avian vet health certificate |
| AKC registration | CITES captive-bred documentation |
| 10-year health guarantee | Health guarantee (`[DURATION_TBD]`) |
| litter / whelp | clutch / hatch |
| Flight Nanny | IATA-compliant bird shipping |
| $1,200–$1,700 | $1,500–$3,500 (CAG) / $1,200–$2,500 (TAG) |
| Formspree | `[PAYMENT_METHOD_TBD]` |
| orange/white design system | CAG design system |

## Standard CAG Context Block (insert after Golden Rule in every file)

```markdown
## CAG Project Context
> **Site:** CongoAfricanGreys.com — captive-bred African Grey parrot breeder
> **Variants:** Congo African Grey (CAG, $1,500–$3,500) · Timneh African Grey (TAG, $1,200–$2,500) — treat as distinct product lines
> **CITES:** African Greys are CITES Appendix II. All birds captive-bred with full documentation. Never imply wild-caught or illegal trade.
> **Trust pillars:** USDA AWA license · CITES captive-bred docs · DNA sexing cert · Avian vet health certificate · Hatch certificate + band number · Fully weaned + hand-raised
> **Buyer fears (ranked):** Scam/fraud · Sick bird · CITES documentation gaps · Wild-caught suspicion · Post-sale abandonment
> **Content root:** `site/content/` | **Sessions:** `sessions/`
> **Confidence Gate:** ≥97% before writing any site file
```

---

## Task 0: Create Foundational Data Stubs

**Files:**
- Create: `docs/reference/design-system.md`
- Create: `data/price-matrix.json`
- Create: `data/locations.json`
- Create: `data/financial-entities.json`

- [ ] **Step 1: Create `docs/reference/design-system.md`**

```markdown
# CAG Design System

> **Status:** Placeholder — Phase 2 design TBD. Update this file before any page-building work.

## Color Tokens (TBD — update before page building)

```css
/* TBD — colors to be determined in Phase 2 */
--primary: #TBD;       /* hero backgrounds */
--cta: #TBD;           /* transactional buttons */
--text: #000000;
--canvas: #FFFFFF;
--canvas-alt: #F8F9FA;

/* Typography */
--font-heading: TBD;
--font-body: TBD;
--radius: 8px;
```

## Reference Page
Until a CAG design is finalized, use `/product/male-vs-female-african-grey-parrots-for-sale/`
as the reference page for any section patterns.

## Design Rules
1. Every page must have CITES trust bar visible above the fold
2. Trust signals on every listing: USDA AWA · CITES Appendix II · DNA Sexed · Avian Vet Certified
3. Inquiry form: 3 fields max — name, email, variant preference (Congo / Timneh)
```

- [ ] **Step 2: Create `data/price-matrix.json`**

```json
{
  "last_updated": "2026-04-29",
  "variants": {
    "congo_african_grey": {
      "slug": "congo-african-grey",
      "label": "Congo African Grey",
      "abbreviation": "CAG",
      "price_min": 1500,
      "price_max": 3500,
      "price_display": "$1,500–$3,500",
      "weight_grams": "400–600",
      "tail_color": "red",
      "notes": "Larger variant, most common, higher recognition"
    },
    "timneh_african_grey": {
      "slug": "timneh-african-grey",
      "label": "Timneh African Grey",
      "abbreviation": "TAG",
      "price_min": 1200,
      "price_max": 2500,
      "price_display": "$1,200–$2,500",
      "weight_grams": "275–375",
      "tail_color": "maroon",
      "notes": "Smaller variant, calmer temperament, earlier talker"
    },
    "breeding_pair": {
      "slug": "african-grey-breeding-pair",
      "label": "African Grey Breeding Pair",
      "price_min": 3000,
      "price_max": 7000,
      "price_display": "$3,000–$7,000+",
      "notes": "Bonded pairs, DNA-certified"
    }
  }
}
```

- [ ] **Step 3: Create `data/locations.json`**

```json
{
  "last_updated": "2026-04-29",
  "live_states": [
    {"state": "Florida", "abbr": "FL", "slug": "african-grey-parrot-for-sale-florida", "status": "live"},
    {"state": "California", "abbr": "CA", "slug": "buy-intelligent-african-grey-for-sale-ca", "status": "live"},
    {"state": "Texas", "abbr": "TX", "slug": "african-grey-for-sale-texas", "status": "planned"},
    {"state": "New York", "abbr": "NY", "slug": "african-grey-for-sale-new-york", "status": "planned"},
    {"state": "Georgia", "abbr": "GA", "slug": "african-grey-for-sale-georgia", "status": "planned"},
    {"state": "Illinois", "abbr": "IL", "slug": "african-grey-for-sale-illinois", "status": "planned"},
    {"state": "Pennsylvania", "abbr": "PA", "slug": "african-grey-for-sale-pennsylvania", "status": "planned"},
    {"state": "Ohio", "abbr": "OH", "slug": "african-grey-for-sale-ohio", "status": "planned"},
    {"state": "North Carolina", "abbr": "NC", "slug": "african-grey-for-sale-north-carolina", "status": "planned"},
    {"state": "Michigan", "abbr": "MI", "slug": "african-grey-for-sale-michigan", "status": "planned"},
    {"state": "New Jersey", "abbr": "NJ", "slug": "african-grey-for-sale-new-jersey", "status": "planned"},
    {"state": "Virginia", "abbr": "VA", "slug": "african-grey-for-sale-virginia", "status": "planned"},
    {"state": "Washington", "abbr": "WA", "slug": "african-grey-for-sale-washington", "status": "planned"},
    {"state": "Arizona", "abbr": "AZ", "slug": "african-grey-for-sale-arizona", "status": "planned"},
    {"state": "Massachusetts", "abbr": "MA", "slug": "african-grey-for-sale-massachusetts", "status": "planned"},
    {"state": "Tennessee", "abbr": "TN", "slug": "african-grey-for-sale-tennessee", "status": "planned"},
    {"state": "Indiana", "abbr": "IN", "slug": "african-grey-for-sale-indiana", "status": "planned"},
    {"state": "Missouri", "abbr": "MO", "slug": "african-grey-for-sale-missouri", "status": "planned"},
    {"state": "Maryland", "abbr": "MD", "slug": "african-grey-for-sale-maryland", "status": "planned"},
    {"state": "Wisconsin", "abbr": "WI", "slug": "african-grey-for-sale-wisconsin", "status": "planned"},
    {"state": "Colorado", "abbr": "CO", "slug": "african-grey-for-sale-colorado", "status": "planned"},
    {"state": "Minnesota", "abbr": "MN", "slug": "african-grey-for-sale-minnesota", "status": "planned"}
  ]
}
```

- [ ] **Step 4: Create `data/financial-entities.json`**

```json
{
  "last_updated": "2026-04-29",
  "purchase_costs": {
    "congo_african_grey": {"min": 1500, "max": 3500},
    "timneh_african_grey": {"min": 1200, "max": 2500},
    "deposit_typical": 500,
    "shipping_iata": {"min": 200, "max": 400}
  },
  "documentation_costs": {
    "cites_captive_bred_permit": "included_in_price",
    "dna_sexing_certificate": "included_in_price",
    "avian_vet_health_certificate": "included_in_price",
    "hatch_certificate": "included_in_price"
  },
  "first_year_setup": {
    "cage_large": {"min": 300, "max": 800},
    "perches_and_toys": {"min": 100, "max": 300},
    "initial_avian_vet_visit": {"min": 75, "max": 200},
    "food_pellets_annual": {"min": 200, "max": 400},
    "enrichment_annual": {"min": 150, "max": 300}
  },
  "annual_ongoing": {
    "food_and_treats": {"min": 200, "max": 400},
    "avian_vet_wellness": {"min": 75, "max": 200},
    "toys_replacement": {"min": 100, "max": 250},
    "unexpected_vet": {"min": 0, "max": 500}
  },
  "lifetime_estimate": {
    "lifespan_years": "40-60",
    "note": "African Greys are 40-60 year commitments — factor lifetime costs carefully"
  }
}
```

- [ ] **Step 5: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add docs/reference/design-system.md data/price-matrix.json data/locations.json data/financial-entities.json
git commit -m "feat: add CAG data stubs for Phase 2 agent system"
```

---

## Task 1: Wave 1 — Light Agents (9 agents, all parallelizable)

**Files (all create in `.claude/agents/`):**
- `cag-meta-description-agent.md` from `meta-description-agent.md`
- `cag-keyword-verifier.md` from `keyword-verifier.md`
- `cag-redirect-manager.md` from `redirect-manager.md`
- `cag-external-link-agent.md` from `external-link-agent.md`
- `cag-deploy-verifier.md` from `deploy-verifier.md`
- `cag-agent-system-qa.md` from `agent-system-qa.md`
- `cag-footer-standardizer.md` from `footer-standardizer.md`
- `cag-google-map-agent.md` from `google-map-agent.md`
- `cag-image-pipeline.md` from `image-pipeline.md`

For each agent: copy source, apply Global Substitution Map, insert CAG Context Block after Golden Rule, apply agent-specific notes below.

- [ ] **Step 1: Copy and adapt all 9 agents (can run in parallel)**

**`cag-meta-description-agent.md`** — no extra changes beyond global substitution.

**`cag-keyword-verifier.md`** — in the 18-point checklist, replace `Embark DNA health info` → `CITES documentation info`, `OFA` → `Avian vet cert`, `AKC registration` → `CITES captive-bred documentation`.

**`cag-redirect-manager.md`** — change all `site2/` path references → `site/content/`. Keep redirect logic identical.

**`cag-external-link-agent.md`** — change `docs/reference/external-link-library.md` reference to same path (file doesn't exist yet; add note: "Create `docs/reference/external-link-library.md` before using this agent"). Authority link categories: add `World Parrot Trust`, `AFA (American Federation of Aviculture)`, `USFWS CITES`, `Ornithological Society` as replacements for breed clubs/AKC.

**`cag-deploy-verifier.md`** — change site URL check from `maltipoosforsale.com` → `congoafricangreys.com`. Change Netlify deploy polling references to match CAG deploy setup (TBD — add note: "Update deploy URL when Phase 2 hosting is configured").

**`cag-agent-system-qa.md`** — global substitution only.

**`cag-footer-standardizer.md`** — replace `mfs-footer-v2` class → `cag-footer-v1`. Replace orange tagline bar color reference with CAG design system token (`--primary: TBD`). Keep 4-column layout structure. Replace footer content: contact info → `[BREEDER_NAME]`, social links → CAG social (TBD), LocalBusiness schema: update `name` → `CongoAfricanGreys.com`.

**`cag-google-map-agent.md`** — global substitution only. Keep iframe/CSP rules identical (critical rule — never `<embed>`).

**`cag-image-pipeline.md`** — update filename convention: `[breed]-[descriptor]-[size]-[context]-mfs.[ext]` → `african-grey-[descriptor]-[variant]-[context]-cag.[ext]`. Example: `african-grey-head-shot-congo-perch-cag.jpg`. Keep all other protocols identical.

- [ ] **Step 2: Verify — no MFS residue, CAG context block present in all 9**

```bash
cd /Users/apple/Downloads/CAG
for f in .claude/agents/cag-meta-description-agent.md .claude/agents/cag-keyword-verifier.md \
  .claude/agents/cag-redirect-manager.md .claude/agents/cag-external-link-agent.md \
  .claude/agents/cag-deploy-verifier.md .claude/agents/cag-agent-system-qa.md \
  .claude/agents/cag-footer-standardizer.md .claude/agents/cag-google-map-agent.md \
  .claude/agents/cag-image-pipeline.md; do
  echo "=== $f ==="
  grep -c "CAG Project Context" "$f" && echo "✅ context block"
  grep -n "MaltipoosForsale\|site2/\|Lawrence\|Cathy\|Omaha" "$f" | head -3 && echo "✅ no residue" || true
done
```

- [ ] **Step 3: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-meta-description-agent.md .claude/agents/cag-keyword-verifier.md \
  .claude/agents/cag-redirect-manager.md .claude/agents/cag-external-link-agent.md \
  .claude/agents/cag-deploy-verifier.md .claude/agents/cag-agent-system-qa.md \
  .claude/agents/cag-footer-standardizer.md .claude/agents/cag-google-map-agent.md \
  .claude/agents/cag-image-pipeline.md
git commit -m "feat: add 9 light agents Wave 1 (CAG Phase 2)"
```

---

## Task 2: Wave 2 — Analytics & Optimization Agents (4 agents)

**Files:**
- `cag-gsc-analytics.md` from `gsc-analytics.md`
- `cag-llm-keyword-intel.md` from `llm-keyword-intel.md`
- `cag-conversion-tracker.md` from `conversion-tracker.md`
- `cag-ab-test-agent.md` from `ab-test-agent.md`

- [ ] **Step 1: Adapt `cag-gsc-analytics.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace GSC data path: `data/` CSV references → `data/analytics/` (CAG stores GSC exports here).

Replace traffic baseline section: update the "What's Worth Improving" table with CAG GSC data:
```markdown
## What's Worth Improving (CAG GSC Baseline — 2026-04-28)

| Page | Clicks | Impressions | Position | Priority |
|------|--------|-------------|----------|----------|
| Homepage | 28 | 14,915 | 45.6 | Title/meta fix — massive impression gap |
| /product/african-grey-parrots-for-sale-near-me/ | 53 | 713 | 41.8 | High intent, pos 41 = page 4 |
| /product/african-grey-parrot-for-sale-florida/ | 42 | 1,446 | 21.8 | Page 2, just off page 1 |
| /product/buy-intelligent-african-grey-for-sale-ca/ | 34 | 1,537 | 14.0 | Best ranking page — protect |
| /buy-african-grey-parrots-with-shipping/ | 18 | 763 | 15.4 | Shipping intent, near page 1 |
| /male-vs-female-african-grey-parrots-for-sale/ | 13 | 1,788 | 21.2 | High impression, low CTR |
```

Replace critical opportunity types: add `CITES query gap` — "queries containing 'documented' or 'cites' with no CAG page targeting them".

- [ ] **Step 2: Adapt `cag-llm-keyword-intel.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace entity-first pattern examples:
```
Entity:    African Grey Parrot
Attribute: CITES Status
Value:     Appendix II — captive trade requires documentation; captive-bred birds legal with permit
Source:    USFWS CITES Appendix II listing

Entity:    Congo African Grey
Attribute: Price
Value:     $1,500–$3,500 from documented captive breeders
```

Replace target queries examples — use CAG top queries:
`"congo african grey for sale"`, `"african grey parrot for sale"`, `"CITES documented african grey"`.

Keep all API code blocks identical (they're domain-agnostic curl commands).

- [ ] **Step 3: Adapt `cag-conversion-tracker.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace the 25-point conversion scoring rubric to reflect CAG buyer signals:

```markdown
## CAG 25-Point Conversion Score

### Trust Signals (8 pts)
- CITES trust bar visible above fold (2 pts)
- USDA AWA license referenced (2 pts)
- Avian vet health cert mentioned with vet name (2 pts)
- DNA sexing certificate mentioned (1 pt)
- Hatch certificate + band number mentioned (1 pt)

### Fear Reduction (7 pts)
- Wild-caught disclaimer present (2 pts)
- CITES documentation explained (2 pts)
- Scam warning / verification guide linked (2 pts)
- Post-sale support mentioned (1 pt)

### CTA Clarity (5 pts)
- Inquiry form visible without scrolling (2 pts)
- Deposit amount stated clearly (2 pts)
- Response time stated (1 pt)

### Content Depth (5 pts)
- Congo vs Timneh comparison present (2 pts)
- FAQ (6+ questions) present (2 pts)
- Price stated openly (1 pt)
```

- [ ] **Step 4: Adapt `cag-ab-test-agent.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace "What's Worth Testing" table:
```markdown
## What's Worth Testing (CAG Priority Order)

| Element | Why Test It | Expected Lift |
|---------|------------|--------------|\
| Hero H1 framing | "CITES documented" vs "captive-bred" — which fear does buyer have? | 10–25% CTR |
| Trust bar placement | Above hero vs below hero | 5–15% time-on-page |
| CTA button text | "Inquire Now" vs "Reserve Your Bird" vs "Check Availability" | 5–20% form submits |
| CITES explanation depth | Full paragraph vs 2-line summary | Trust score lift |
| Variant CTA | "I want Congo" / "I want Timneh" / "Help me decide" | Qualification rate |
```

Replace test file paths: `sessions/ab-tests/active-tests.md` path stays the same (sessions/ exists in CAG).

- [ ] **Step 5: Verify all 4**

```bash
cd /Users/apple/Downloads/CAG
grep -l "CAG Project Context" .claude/agents/cag-gsc-analytics.md .claude/agents/cag-llm-keyword-intel.md .claude/agents/cag-conversion-tracker.md .claude/agents/cag-ab-test-agent.md | wc -l
# Expected: 4

grep -n "MaltipoosForsale\|site2/\|Lawrence\|Cathy\|Omaha\|Embark DNA\|OFA cert\|AKC reg" \
  .claude/agents/cag-gsc-analytics.md .claude/agents/cag-llm-keyword-intel.md \
  .claude/agents/cag-conversion-tracker.md .claude/agents/cag-ab-test-agent.md
# Expected: no output
```

- [ ] **Step 6: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-gsc-analytics.md .claude/agents/cag-llm-keyword-intel.md \
  .claude/agents/cag-conversion-tracker.md .claude/agents/cag-ab-test-agent.md
git commit -m "feat: add analytics and optimization agents Wave 2 (CAG Phase 2)"
```

---

## Task 3: Wave 3 — Content Architecture Agents (6 agents)

**Files:**
- `cag-content-architect.md` from `content-architect.md`
- `cag-structure-architect.md` from `structure-architect.md`
- `cag-framework-agent.md` from `framework-agent.md`
- `cag-angle-agent.md` from `angle-agent.md`
- `cag-hub-builder.md` from `hub-builder.md`
- `cag-batch-rebuilder.md` from `batch-rebuilder.md`

- [ ] **Step 1: Adapt `cag-content-architect.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace content brief examples — update example briefs to use CAG keywords:
```
Page slug: african-grey-parrot-for-sale-florida
Primary keyword: "african grey parrot for sale florida"
Reader profile: Florida buyer, moderate income, first-time parrot owner
Framework: AIDA (commercial page) + QAB (FAQ section)
Priority fear: CITES documentation legitimacy
Trust signal to feature: USDA AWA license + CITES captive-bred docs
```

Replace `data/adoption-structure.json` reference → `data/structure.json`.

- [ ] **Step 2: Adapt `cag-structure-architect.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace the Silo example:
```
Hub: /african-grey-parrot-guide/ (or /african-grey-breed-guide/)
  Spoke: /african-grey-health/
    Sub-spoke: /pbfd-african-grey/
    Sub-spoke: /african-grey-feather-destructive-behavior/
  Spoke: /african-grey-training/
    Sub-spoke: /african-grey-talking-training/
```

Replace the Reverse Silo example:
```
Sub-spoke: /african-grey-for-sale-texas/dallas/  (future)
  ↑
Spoke: /african-grey-parrot-for-sale-texas/
  ↑
Hub: /african-grey-parrots-for-sale/ (all states)
  ↑
Root: / (homepage)
```

Replace `data/locations.json` reference — same path, now exists (Task 0).

- [ ] **Step 3: Adapt `cag-framework-agent.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace competitor analysis scope note:
```markdown
## CAG Competitor Analysis Scope

For any keyword, analyze top 5 competitors from `data/competitors.json`.
Primary analysis metrics (same as MFS):
- CITES/documentation trust signals (CAG differentiator — most competitors silent)
- Wild-caught disclaimer presence (compliance gap at competitors)
- Price transparency
- FAQ depth (African Grey-specific questions)
```

- [ ] **Step 4: Adapt `cag-angle-agent.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace angle examples to African Grey context:
```markdown
## CAG Angle Categories (replace MFS examples)

### Documentation Angles
- "The $600 Facebook Grey vs the $1,500 CITES-documented Grey — what you're actually paying for"
- "CITES Appendix II explained in plain English — what it means for your bird purchase"
- "How to verify a CITES captive-bred permit before sending any deposit"

### Variant Angles
- "Congo vs Timneh African Grey: the choice most first-time buyers get wrong"
- "Why Timneh owners bond faster (and what Congo owners get instead)"

### Longevity Angles
- "The 50-year decision: what to ask before buying an African Grey"
- "African Grey lifespan vs other parrots — what the data says"
```

- [ ] **Step 5: Adapt `cag-hub-builder.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace hub type examples:
```markdown
## CAG Hub Types

| Hub | URL | Spokes |
|-----|-----|--------|
| Location Hub | `/african-grey-parrots-for-sale/` | 22 state pages |
| Comparison Hub | `/african-grey-comparison/` | Congo vs Timneh, vs Macaw, vs Cockatoo, etc. |
| Species Hub | `/african-grey-parrot-guide/` | care, health, training, talking spokes |
| Documentation Hub | `/african-grey-cites-documentation/` | CITES guide, USDA, DNA sexing spokes |
```

Replace `data/locations.json` reference — same path, now exists.

- [ ] **Step 6: Adapt `cag-batch-rebuilder.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace batch target paths: `site2/usa-locations/*/index.html` → `site/content/african-grey-for-sale-*/`. Keep fork logic identical.

- [ ] **Step 7: Verify all 6**

```bash
cd /Users/apple/Downloads/CAG
grep -l "CAG Project Context" \
  .claude/agents/cag-content-architect.md .claude/agents/cag-structure-architect.md \
  .claude/agents/cag-framework-agent.md .claude/agents/cag-angle-agent.md \
  .claude/agents/cag-hub-builder.md .claude/agents/cag-batch-rebuilder.md | wc -l
# Expected: 6

grep -rn "MaltipoosForsale\|site2/\|Lawrence\|Cathy\|Omaha" \
  .claude/agents/cag-content-architect.md .claude/agents/cag-structure-architect.md \
  .claude/agents/cag-framework-agent.md .claude/agents/cag-angle-agent.md \
  .claude/agents/cag-hub-builder.md .claude/agents/cag-batch-rebuilder.md
# Expected: no output
```

- [ ] **Step 8: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-content-architect.md .claude/agents/cag-structure-architect.md \
  .claude/agents/cag-framework-agent.md .claude/agents/cag-angle-agent.md \
  .claude/agents/cag-hub-builder.md .claude/agents/cag-batch-rebuilder.md
git commit -m "feat: add content architecture agents Wave 3 (CAG Phase 2)"
```

---

## Task 4: Wave 4 — Content Writer Agents (5 agents)

**Files:**
- `cag-faq-agent.md` from `faq-agent.md`
- `cag-paa-agent.md` from `paa-agent.md`
- `cag-blog-post-agent.md` from `blog-post-agent.md`
- `cag-case-study-agent.md` from `case-study-agent.md`
- `cag-seo-content-writer.md` from `seo-content-writer.md`

- [ ] **Step 1: Adapt `cag-faq-agent.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace the question bank note: "Source questions from `skills/framework-qab.md` — CAG FAQ Question Bank section (pre-built)". Remove MFS-specific question examples; replace with pointer to CAG question bank.

Keep QAB format (`<details>/<summary>` HTML + FAQPage JSON-LD) identical.

- [ ] **Step 2: Adapt `cag-paa-agent.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace MFS PAA question bank with CAG PAA bank:
```markdown
## CAG PAA Question Bank (pre-built)

### Buying / Cost
- How much does a Congo African Grey parrot cost?
- How much does a Timneh African Grey parrot cost?
- What is the total cost of owning an African Grey parrot?
- Where can I buy a legally documented African Grey parrot?
- How do I avoid African Grey parrot scams?

### CITES / Legal
- Are African Grey parrots legal to own in the US?
- What is CITES Appendix II and why does it matter?
- What documentation comes with a captive-bred African Grey?
- Can CBP seize my African Grey parrot?
- What does USDA AWA license mean for a bird breeder?

### Species / Care
- What is the difference between Congo and Timneh African Greys?
- How long do African Grey parrots live?
- Do African Grey parrots talk?
- Are African Grey parrots good for beginners?
- What is PBFD in African Grey parrots?
- How much space does an African Grey parrot need?
- What do African Grey parrots eat?

### Shipping / Process
- Is bird shipping safe?
- How does IATA-compliant bird shipping work?
- What is included in the purchase price?
- How do I reserve an African Grey parrot?
```

- [ ] **Step 3: Adapt `cag-blog-post-agent.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace topic categories:
```markdown
## CAG Blog Topic Categories

### CITES & Documentation (high-authority, low competition)
- "African Grey CITES Appendix II: a buyer's complete guide"
- "How to verify a CITES captive-bred permit before purchase"
- "What happens if your African Grey doesn't have proper documentation"

### Variant Comparisons (commercial intent)
- "Congo vs Timneh African Grey: which is right for your family?"
- "Male vs female African Grey: temperament differences"

### Care & Husbandry (informational, long-tail)
- "African Grey parrot lifespan: what 40–60 years means for ownership"
- "PBFD in African Greys: what to ask your breeder"
- "Hand-raised vs parent-raised: what to look for"

### Buyer Guides (commercial intent)
- "How to spot an African Grey parrot scam in 2026"
- "First-year cost of owning an African Grey parrot"
```

- [ ] **Step 4: Adapt `cag-case-study-agent.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace story template examples:
```markdown
## CAG Case Study Template

**Title pattern:** "[Family name] family — how they verified CITES documentation and brought home [name] the [variant]"

**Story arc:**
1. Buyer's initial fear (scam, CITES confusion, or wild-caught suspicion)
2. The research process (how they found CAG, what they checked)
3. The documentation received (specific: permit number, vet name, band number)
4. Life with the bird (Congo vs Timneh observation, talking progress, bonding)

**Trust signal to feature:** Always reference the specific documentation received.
```

- [ ] **Step 5: Adapt `cag-seo-content-writer.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace framework application examples:
```markdown
### Inverse Pyramid (all informational content)
Paragraph 1: Direct answer — "Congo African Greys cost $1,500–$3,500 from captive breeders."
Paragraph 2: Evidence — "CITES captive-bred documentation, DNA sexing cert, avian vet cert included."
Paragraph 3: CAG application — "At CongoAfricanGreys.com, every bird ships with [list docs]."

### H-S-S — Hook-Story-Solution (about page, trust-building sections)
Hook: [The African Grey scam problem — $600 Craigslist birds with forged CITES paperwork]
Story: [BREEDER_NAME]'s [X] years breeding CITES-documented birds
Solution: [What CAG built — USDA license, CITES permits, avian vet certs]
```

Replace `data/price-matrix.json` reference — same path, now exists (Task 0).

- [ ] **Step 6: Verify all 5**

```bash
cd /Users/apple/Downloads/CAG
grep -l "CAG Project Context" .claude/agents/cag-faq-agent.md .claude/agents/cag-paa-agent.md \
  .claude/agents/cag-blog-post-agent.md .claude/agents/cag-case-study-agent.md \
  .claude/agents/cag-seo-content-writer.md | wc -l
# Expected: 5

grep -n "MaltipoosForsale\|Lawrence\|Cathy\|Embark DNA\|OFA cert\|AKC reg\|teacup\|maltipoo" \
  .claude/agents/cag-faq-agent.md .claude/agents/cag-paa-agent.md \
  .claude/agents/cag-blog-post-agent.md .claude/agents/cag-case-study-agent.md \
  .claude/agents/cag-seo-content-writer.md
# Expected: no output
```

- [ ] **Step 7: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-faq-agent.md .claude/agents/cag-paa-agent.md \
  .claude/agents/cag-blog-post-agent.md .claude/agents/cag-case-study-agent.md \
  .claude/agents/cag-seo-content-writer.md
git commit -m "feat: add content writer agents Wave 4 (CAG Phase 2)"
```

---

## Task 5: Wave 5 — Section & Component Builders (4 agents)

> **Note:** `cag-section-builder.md` must be written first — page builder agents in Task 6 depend on it.

**Files:**
- `cag-section-builder.md` from `section-builder.md` (write first)
- `cag-about-builder.md` from `about-builder.md`
- `cag-contact-form-updater.md` from `contact-form-updater.md`
- `cag-interactive-component.md` from `interactive-component.md`

- [ ] **Step 1: Adapt `cag-section-builder.md` (write this first)**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace design system tokens section:
```markdown
## Design System Tokens (from docs/reference/design-system.md — read that file first)

> **IMPORTANT:** CAG design tokens are TBD (Phase 2). Read `docs/reference/design-system.md`
> before producing any HTML. Until tokens are finalized, use the placeholder values below.

```css
/* Read docs/reference/design-system.md for current values */
--primary: TBD;
--cta: TBD;
--text: #000000;
--canvas: #FFFFFF;
--canvas-alt: #F8F9FA;
--font-heading: TBD;
--font-body: TBD;
--radius: 8px;
--btn-bg: TBD;
--btn-text: #000000;
```

Replace reference page instruction: "Read `site/content/male-vs-female-african-grey-parrots-for-sale/` — the reference page (source of truth for how sections look in production). If file doesn't exist yet, use the MFS reference at `/Users/apple/Downloads/MFS/site2/male-vs-female-maltipoo/index.html` as structural reference only."

Replace CSS class prefix from `mfs-` → `cag-` throughout all templates.

Add CITES trust bar section template:
```html
<!-- Section Type: cites-trust-bar (required on every listing page) -->
<div class="cag-trust-bar">
  <span class="cag-trust-item">✓ USDA AWA Licensed</span>
  <span class="cag-trust-item">✓ CITES Appendix II Captive-Bred</span>
  <span class="cag-trust-item">✓ DNA Sexed</span>
  <span class="cag-trust-item">✓ Avian Vet Certified</span>
</div>
```

- [ ] **Step 2: Adapt `cag-about-builder.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace brand story elements:
```markdown
## CAG About Page Story Elements

### Hook (replace MFS puppy mill story)
The problem: The African Grey parrot scam market — Facebook Marketplace sellers claiming
"CITES documented" with forged paperwork, disappearing after payment. US buyers lose
thousands annually to wire fraud and CBP seizures.

### Story ([BREEDER_NAME]'s background)
- [X]+ years breeding African Greys captive
- USDA AWA license #[NUMBER]
- CITES captive-bred permits — federal documentation, not self-reported
- [BREEDER_LOCATION]

### Solution (what CAG built)
- Every bird ships with CITES permit + DNA sexing cert + avian vet health cert + hatch cert
- Permit number available before any deposit
- [BREEDER_NAME] answers the phone after the sale

### Replace H-S-S framework references
Hook: [African Grey scam industry problem]
Story: [BREEDER_NAME]'s experience and credentials
Solution: USDA AWA + CITES documentation + avian vet certs on every bird
```

- [ ] **Step 3: Adapt `cag-contact-form-updater.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace form field spec:
```markdown
## CAG Inquiry Form — Required Fields (3 fields max)

1. **Name** (text) — required
2. **Email** (email) — required  
3. **Variant preference** (select: Congo African Grey / Timneh African Grey / Not sure yet) — required

Optional below-fold fields:
- Phone (text) — optional
- Message (textarea, 300 char max) — optional

**Payment method:** `[PAYMENT_METHOD_TBD]` — do NOT hardcode Formspree or any payment processor
**Response time copy:** "We respond within 24 hours — personally, not automated."
```

- [ ] **Step 4: Adapt `cag-interactive-component.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace component library:
```markdown
## CAG Interactive Component Library

### 1. First-Year Cost Calculator
Reads `data/financial-entities.json` and `data/price-matrix.json`.
Inputs: variant (Congo/Timneh) + whether they need cage/setup.
Output: purchase price + setup costs + annual ongoing = year-1 total.

### 2. Variant Fit Quiz (replaces Breed Fit Quiz)
5 questions → recommend Congo or Timneh.
Q1: "How much experience do you have with parrots?"
Q2: "How important is early talking ability?"
Q3: "Do you want a calmer or more energetic companion?"
Q4: "What's your budget range?"
Q5: "How many hours per day will you interact with the bird?"
Result: "Based on your answers, [Congo/Timneh] African Grey is the better match."

### 3. Documentation Checklist (replaces Puppy Readiness Checklist)
Interactive checklist for buyers to verify documentation before sending deposit:
- [ ] USDA AWA license number (verifiable at aphis.usda.gov)
- [ ] CITES captive-bred permit number (verifiable at usfws.gov)
- [ ] DNA sexing certificate — includes lab name
- [ ] Avian vet health certificate — includes vet name and date
- [ ] Hatch certificate + band number
- [ ] Traceable payment method (no CashApp/Zelle/wire)

### 4. Shipping Timeline Estimator (replaces Shipping Cost Estimator)
Input: destination state. Output: IATA shipping protocol, typical transit time, estimated cost range from `data/financial-entities.json`.

### 5. CITES Verification Guide (new — no MFS equivalent)
Step-by-step clickable guide:
Step 1 → Go to usfws.gov → Step 2 → Enter permit number → Step 3 → Verify captive-bred status
```

- [ ] **Step 5: Verify all 4**

```bash
cd /Users/apple/Downloads/CAG
grep -l "CAG Project Context" .claude/agents/cag-section-builder.md .claude/agents/cag-about-builder.md \
  .claude/agents/cag-contact-form-updater.md .claude/agents/cag-interactive-component.md | wc -l
# Expected: 4

grep -c "cag-trust-bar" .claude/agents/cag-section-builder.md
# Expected: at least 1 (CITES trust bar template present)

grep -n "mfs-" .claude/agents/cag-section-builder.md
# Expected: no output (all CSS classes use cag- prefix)
```

- [ ] **Step 6: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-section-builder.md .claude/agents/cag-about-builder.md \
  .claude/agents/cag-contact-form-updater.md .claude/agents/cag-interactive-component.md
git commit -m "feat: add section and component builder agents Wave 5 (CAG Phase 2)"
```

---

## Task 6: Wave 6 — Page Builder Agents (4 agents)

> **Prerequisite:** Task 5 (cag-section-builder.md) must be complete.

**Files:**
- `cag-homepage-builder.md` from `homepage-builder.md`
- `cag-location-builder.md` from `location-builder.md`
- `cag-comparison-builder.md` from `comparison-builder.md`
- `cag-purchase-guide.md` from `purchase-guide.md`

- [ ] **Step 1: Adapt `cag-homepage-builder.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace the 18-section map with CAG homepage structure:
```markdown
## CAG Homepage — 18-Section Map

| # | Section | Type | Key Content |
|---|---------|------|-------------|
| 1 | Hero | `hero` | H1 (sacred), CITES trust bar, primary CTA |
| 2 | CITES Trust Bar | `cag-trust-bar` | USDA AWA · CITES Appendix II · DNA Sexed · Avian Vet Certified |
| 3 | Available Birds | `price-card` | Congo + Timneh cards from data/ |
| 4 | Why CAG (5 trust signals) | `features` | CITES docs, USDA license, DNA cert, avian vet cert, [X]+ years |
| 5 | Congo vs Timneh Quick Guide | `comparison-table` | Weight, price, tail, temperament |
| 6 | Buyer Fear Reframe | BAB section | Scam stats → CAG documentation transparency |
| 7 | CITES Documentation Explainer | `features` | What each doc is, why it matters |
| 8 | Video Tour | custom (YouTube) | Breeder introduction / bird footage |
| 9 | Customer Testimonials | `testimonials` | Name + location + specific outcome |
| 10 | Shipping (IATA protocol) | `features` | How IATA shipping works, health cert required |
| 11 | FAQ — 8 Questions | `faq` | Price, CITES, variants, process |
| 12 | Parent Birds | custom | [BREEDER_NAME] introduction, breeding program |
| 13 | Health Guarantee | custom | Terms, documentation included |
| 14 | All 50 States Delivery | custom | Map/list, IATA compliance note |
| 15 | Congo vs Other Parrots | `comparison-table` | vs Macaw, Cockatoo, Cockatiel |
| 16 | Breeding Pairs | `price-card` | Bonded pairs, DNA-certified |
| 17 | Blog / Resources | `hub-links` | Latest care articles |
| 18 | Final CTA | `cta` | Inquiry form — 3 fields |

**Sacred elements (never change):**
- H1, canonical, all JSON-LD schema blocks, og: meta tags
- Run `grep -n "<h1\|canonical\|ld+json" site/content/index.md | head -10` on startup to identify them
```

Replace pricing reference: `data/price-matrix.json` (exists after Task 0).

Replace reference page: "Read `site/content/male-vs-female-african-grey-parrots-for-sale/` as reference."

- [ ] **Step 2: Adapt `cag-location-builder.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace state variables table:
```markdown
## State Page Variables

| Variable | Example (Florida) | Source |
|----------|------------------|--------|
| `{STATE}` | Florida | `data/locations.json` → `state` |
| `{STATE_ABBR}` | FL | `data/locations.json` → `abbr` |
| `{SLUG}` | african-grey-parrot-for-sale-florida | `data/locations.json` → `slug` |
| `{MAJOR_CITIES}` | Miami, Orlando, Tampa, Jacksonville | built-in state data below |
| `{STATE_AVIAN_VET_NOTE}` | Florida has USDA-licensed avian vets who accept CITES paperwork | state data |
| `{STATE_IMPORT_NOTE}` | Florida: no additional state import restrictions on CITES-documented birds | state data |
| `{PRICE_CONGO}` | $1,500–$3,500 | `data/price-matrix.json` |
| `{PRICE_TIMNEH}` | $1,200–$2,500 | `data/price-matrix.json` |
```

Replace built-in state data (first 2 states as examples — agent should expand for all 22):
```
Florida (FL)
  Cities: Miami, Orlando, Tampa, Jacksonville, Fort Lauderdale, St. Petersburg, Hialeah, Tallahassee
  Climate: Subtropical — hot humid summers, mild winters. No cold-weather shipping restrictions.
  Import note: No state-level restrictions beyond federal CITES requirements.
  State law: Florida exotic bird laws — CITES Appendix II requires documentation. No additional state permit for buyers.
  Avian vet note: Florida has large avian vet community. [BREEDER_NAME] recommends post-arrival vet visit within 72h.

California (CA)
  Cities: Los Angeles, San Diego, San Francisco, San Jose, Sacramento, Fresno, Long Beach, Oakland
  Climate: Varied — coastal mild, inland hot. Year-round shipping possible.
  Import note: California requires health certificate for all live birds entering the state — already included with every CAG bird.
  State law: CA AB 485 bans pet store sales of non-rescue animals — does NOT apply to private breeders like CAG.
  Avian vet note: Large avian vet community in LA/Bay Area/San Diego. Post-arrival vet visit recommended within 72h.
```

Change reference template: Arizona → Florida (CAG's highest-traffic page).
Data source: `data/locations.json` (exists after Task 0).

- [ ] **Step 3: Adapt `cag-comparison-builder.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace existing comparison pages list:
```bash
# CAG existing comparison pages
ls site/content/ | grep "vs\|comparison"
# Currently live: /male-vs-female-african-grey-parrots-for-sale/
```

Replace reference design: `site/content/male-vs-female-african-grey-parrots-for-sale/` (existing CAG page).

Replace comparison types:
```markdown
## CAG Comparison Page Types

| Comparison | URL | Priority |
|------------|-----|----------|
| Congo vs Timneh | /congo-vs-timneh-african-grey/ | High |
| Male vs Female | /male-vs-female-african-grey-parrots-for-sale/ | ✅ Exists |
| African Grey vs Macaw | /african-grey-vs-macaw-parrot/ | Medium |
| African Grey vs Cockatoo | /african-grey-vs-cockatoo/ | Medium |
| African Grey vs Cockatiel | /african-grey-vs-cockatiel/ | Low |
| F1 vs F2 | N/A — not applicable for African Greys | Skip |
```

- [ ] **Step 4: Adapt `cag-purchase-guide.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Replace the entire purchase process with CAG-specific flow:
```markdown
## CAG Purchase Process (18-section guide)

The purchase guide walks buyers through:

1. **Research phase** — Congo vs Timneh decision (link to comparison page)
2. **Verification phase** — how to verify breeder credentials (USDA AWA lookup, CITES permit)
3. **Inquiry phase** — filling out the 3-field inquiry form
4. **Documentation review** — what you'll receive before deposit
5. **Deposit phase** — how deposit works, what it holds
6. **Documentation delivery** — CITES permit, DNA cert, avian vet cert, hatch cert
7. **Shipping phase** — IATA live animal protocols, temperature windows
8. **Arrival phase** — 72-hour vet visit, settling-in protocol
9. **Post-purchase support** — [BREEDER_NAME] contact, ongoing questions

**Replace health guarantee details:** Update from "10-year health guarantee" to "health guarantee (`[DURATION_TBD]`)" — exact terms TBD.

**Replace data source:** All prices from `data/price-matrix.json`, all cost estimates from `data/financial-entities.json`.
```

- [ ] **Step 5: Verify all 4**

```bash
cd /Users/apple/Downloads/CAG
grep -l "CAG Project Context" .claude/agents/cag-homepage-builder.md \
  .claude/agents/cag-location-builder.md .claude/agents/cag-comparison-builder.md \
  .claude/agents/cag-purchase-guide.md | wc -l
# Expected: 4

grep -n "cag-section-builder\|site2/\|maltipoo\|Maltipoo\|site2" \
  .claude/agents/cag-homepage-builder.md .claude/agents/cag-location-builder.md \
  .claude/agents/cag-comparison-builder.md .claude/agents/cag-purchase-guide.md
# Expected: cag-section-builder references OK; no site2/ or Maltipoo residue
```

- [ ] **Step 6: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-homepage-builder.md .claude/agents/cag-location-builder.md \
  .claude/agents/cag-comparison-builder.md .claude/agents/cag-purchase-guide.md
git commit -m "feat: add page builder agents Wave 6 (CAG Phase 2)"
```

---

## Task 7: Wave 7 — Domain-Specific Heavy Agents (4 agents)

**Files:**
- `cag-species-guide-builder.md` from `breed-guide-builder.md`
- `cag-financial-strategist.md` from `financial-strategist.md`
- `cag-clutch-manager.md` from `litter-manager.md`
- `cag-scam-specialist.md` from `adoption-specialist.md`

- [ ] **Step 1: Adapt `cag-species-guide-builder.md`** (from `breed-guide-builder.md`)

Copy source. Apply global substitution. Insert CAG context block. Then:

Change frontmatter:
```yaml
---
name: cag-species-guide-builder
description: Builds and rebuilds African Grey species guide pages using Entity-Tree framework. Manages /african-grey-parrot-guide/ (comprehensive species guide) and variant-specific guides. Reads data/price-matrix.json and data/financial-entities.json for factual data. Entity-Tree structure optimized for AI/AIO citation.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---
```

Replace the Entity-Tree structure example:
```
[Entity: African Grey Parrot (Psittacus erithacus)]
  → [Attribute: Variants]
      → Congo African Grey (CAG): ~400–600g, red tail, $1,500–$3,500
      → Timneh African Grey (TAG): ~275–375g, maroon tail, $1,200–$2,500
  → [Attribute: CITES Status]
      → Appendix II: commercial trade restricted; captive-bred with permit legal
      → USFWS captive-bred permit required for sale/purchase
  → [Attribute: Lifespan]
      → 40–60 years in captivity
      → One of the longest-lived companion parrots
  → [Attribute: Health Conditions]
      → PBFD (Psittacine Beak and Feather Disease): viral, test before purchase
      → Feather Destructive Behavior: stress-related, management protocol
      → Aspergillosis: fungal, respiratory, cage hygiene critical
  → [Attribute: Intelligence]
      → Vocabulary: 200+ words documented in captive birds
      → Irene Pepperberg research: demonstrated concept learning
      → Problem-solving: comparable to 5-year-old human cognition
```

Replace sacred elements (update to CAG page if it exists):
```bash
grep -n "<h1\|canonical\|ld+json" site/content/african-grey-parrot-guide/*.md 2>/dev/null | head -5
```

- [ ] **Step 2: Adapt `cag-financial-strategist.md`**

Copy source. Apply global substitution. Insert CAG context block. Then:

Change frontmatter description: "Owns all cost and pricing pages including `/african-grey-parrot-price/` and the first-year cost guide. Reads from `data/financial-entities.json` and `data/price-matrix.json`. Guiding principle: 'Transparency builds trust faster than low prices.' Covers purchase price, first-year setup, IATA shipping, annual costs, lifetime estimate (40–60 year commitment), and CAG vs TAG cost comparison."

Replace 12-section page structure:
```markdown
## CAG Cost Guide — 12 Sections

1. Purchase price by variant (Congo $1,500–$3,500 / Timneh $1,200–$2,500)
2. What's included in the price (documentation list)
3. Deposit structure and what it holds
4. IATA shipping costs ($200–$400 estimated)
5. First-year setup (cage, toys, first avian vet visit)
6. Annual ongoing costs (food, toys, wellness vet)
7. Lifetime cost estimate (40–60 years)
8. CAG vs TAG total cost comparison table
9. Hidden costs warning (unexpected vet, cage upgrades, enrichment)
10. CAG vs buying from Craigslist/Facebook (true cost including risk)
11. Cost FAQ (8 questions using QAB from framework-qab.md)
12. Final CTA: "Get transparent pricing — inquiry takes 2 minutes"

All numbers sourced from `data/financial-entities.json` — never hardcoded.
```

- [ ] **Step 3: Adapt `cag-clutch-manager.md`** (from `litter-manager.md`)

This is a full terminology rewrite. Change EVERY instance of the following:

| MFS Term | CAG Term |
|----------|----------|
| litter | clutch |
| puppy / puppies | bird / birds (or chick for unweaned) |
| whelp date | hatch date |
| go-home date | weaned date / available date |
| dam / sire | hen / cock |
| breed | species/variant (Congo / Timneh) |
| size | variant |
| color | color morph |
| Bella, Charlie, Daisy (example names) | (keep as examples, they're fine) |

Change frontmatter:
```yaml
---
name: cag-clutch-manager
description: Single source of truth for CAG bird inventory. Updates availability (available/reserved/sold) in site/content/available/, retires sold listings with sold overlays, adds clutch announcements to homepage, and syncs bird count in meta descriptions. Never deletes sold listings. Writes all inventory changes to data/clutch-inventory.json.
---
```

Change data file reference: `data/litter-inventory.json` → `data/clutch-inventory.json`

Update data/clutch-inventory.json structure (replace JSON schema):
```json
{
  "last_updated": "YYYY-MM-DD",
  "available_count": 0,
  "reserved_count": 0,
  "sold_count": 0,
  "birds": [
    {
      "id": "cag-001",
      "name": "Koko",
      "species": "african-grey",
      "variant": "congo",
      "color_morph": "standard",
      "gender": "unknown",
      "dna_sexed": false,
      "hatch_date": "YYYY-MM-DD",
      "available_date": "YYYY-MM-DD",
      "price": 1800,
      "status": "available",
      "cites_permit": "TBD",
      "listing_page": "/product/african-grey-parrots-for-sale-near-me/",
      "clutch_id": "clutch-2026-01"
    }
  ],
  "clutches": [
    {
      "id": "clutch-2026-01",
      "variant": "congo",
      "hen": "[BREEDER_HEN_NAME]",
      "cock": "[BREEDER_COCK_NAME]",
      "hatch_date": "YYYY-MM-DD",
      "available_date": "YYYY-MM-DD",
      "count": 2,
      "cites_permit_number": "TBD"
    }
  ]
}
```

Update Protocol A (Add New Clutch): replace all puppy card HTML with bird card HTML:
```html
<div class="cag-bird-card" id="bird-[id]" data-status="available" data-variant="[variant]">
  <div class="cag-bird-badge cag-badge-available">Available</div>
  <img src="[image]" alt="[variant] African Grey parrot — CAG" loading="lazy">
  <div class="cag-bird-info">
    <h3 class="cag-bird-name">[Name]</h3>
    <p class="cag-bird-details">[Variant] African Grey · [Gender] · Hatched [hatch_date]</p>
    <p class="cag-bird-docs">CITES Documented · DNA Sexed · Avian Vet Certified</p>
    <p class="cag-bird-price">$[price]</p>
    <a href="#contact" class="cag-btn cag-btn-primary">Inquire About [Name]</a>
  </div>
</div>
```

Replace badge CSS:
```css
.cag-badge-available { background: #4CAF50; color: white; }
.cag-badge-reserved  { background: #FFA500; color: black; }
.cag-badge-sold      { background: #9E9E9E; color: white; }
```

- [ ] **Step 4: Adapt `cag-scam-specialist.md`** (from `adoption-specialist.md`)

This is a full purpose rewrite. The MFS adoption-specialist handles the "adopt vs buy" reframe for rescue searchers. For CAG, the equivalent audience is scam survivors and CITES-fearful buyers.

Change frontmatter:
```yaml
---
name: cag-scam-specialist
description: Rebuilds /how-to-avoid-african-grey-parrot-scams/ and manages the scam-prevention content cluster. Reads data/structure.json for hub/spoke map. Focuses on scam identification, CITES documentation verification, and ethical-breeder trust signals. Converts scam-fearful visitors into documented-purchase inquiries.
---
```

Replace Purpose section entirely:
```markdown
## Purpose

You are the **Scam Specialist Agent** for CongoAfricanGreys.com. You rebuild the scam prevention hub page and manage its spoke pages — all content targeting visitors who search "african grey parrot scam," "how to verify african grey breeder," or "cites african grey documentation."

Key insight: Most visitors on this page are not scam victims yet — they're buyers doing pre-purchase research after seeing suspicious listings. The page must validate their concern, name the specific scam patterns, and position CITES documentation + USDA AWA licensing as the verification standard.

### Reader Profile
**Who lands here:** Visitors searching "african grey scam," "fake african grey breeder," "how to verify african grey documentation," "cites appendix ii african grey."

**Mix of:**
- Pre-purchase researchers (saw a $600 bird on Facebook, doing due diligence)
- Scam survivors (lost money, now looking for safe path)
- Documentation-confused buyers (CITES sounds complex, they want plain-English guidance)

**Fear stack:**
1. Sending deposit and losing it (wire fraud, CashApp scam)
2. Receiving a wild-caught bird with forged CITES paperwork
3. CBP seizure after purchase
4. Receiving a sick bird with no recourse

**Convert with:** Specific documentation checklist + CAG's verifiable credentials (permit number, USDA license, vet name).
```

Replace 18-section map with scam-specialist sections:
```markdown
## Scam Prevention Hub — Section Map

| # | Section | Type | Key Content |
|---|---------|------|-------------|
| 1 | Hero | `hero` | H1 (sacred), "Here's how to verify any breeder in 5 minutes" |
| 2 | The 5 African Grey Scam Patterns | `features` | CashApp deposit, stock photos, no CITES permit, price too low, no USDA license |
| 3 | How to Verify CITES Documentation | custom | Step-by-step usfws.gov lookup |
| 4 | How to Verify USDA AWA License | custom | Step-by-step aphis.usda.gov lookup |
| 5 | What Legitimate Documentation Looks Like | `features` | CITES permit, DNA cert, avian vet cert, hatch cert |
| 6 | Red Flag Checklist | custom (interactive) | 10 warning signs before sending money |
| 7 | Safe Payment Methods | `features` | Credit card, PayPal G&S, wire only AFTER verification |
| 8 | Customer Testimonials | `testimonials` | Focus on documentation experience |
| 9 | CAG's Credentials (Verifiable) | `features` | USDA AWA license, CITES permit, avian vet name |
| 10 | FAQ — 8 Scam Questions | `faq` | QAB format, CITES questions |
| 11 | Final CTA | `cta` | "Verify our credentials — inquiry takes 2 minutes" |
```

- [ ] **Step 5: Verify all 4**

```bash
cd /Users/apple/Downloads/CAG
grep -l "CAG Project Context" .claude/agents/cag-species-guide-builder.md \
  .claude/agents/cag-financial-strategist.md .claude/agents/cag-clutch-manager.md \
  .claude/agents/cag-scam-specialist.md | wc -l
# Expected: 4

grep -n "litter-inventory\|breed-guide\|maltipoo\|Maltipoo\|puppy\|Puppy\|adoption" \
  .claude/agents/cag-clutch-manager.md .claude/agents/cag-scam-specialist.md
# Expected: no output (litter/puppy/adoption fully replaced)

grep -c "clutch-inventory\|CITES permit\|cag-bird-card" .claude/agents/cag-clutch-manager.md
# Expected: 1+ matches each
```

- [ ] **Step 6: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-species-guide-builder.md .claude/agents/cag-financial-strategist.md \
  .claude/agents/cag-clutch-manager.md .claude/agents/cag-scam-specialist.md
git commit -m "feat: add domain-specific heavy agents Wave 7 (CAG Phase 2)"
```

---

## Task 8: Wave 8 — Variant & Product Agents (4 agents)

**Files:**
- `cag-timneh-specialist.md` from `maltese-breed-agent.md`
- `cag-variant-specialist.md` from `size-specialist.md`
- `cag-bird-personality.md` from `puppy-personality.md`

**Note:** `maltese-breed-agent.md` → `cag-timneh-specialist.md` because the Timneh African Grey is the "secondary variant" on CAG, just as the Maltese was the secondary breed on MFS.

- [ ] **Step 1: Adapt `cag-timneh-specialist.md`** (from `maltese-breed-agent.md`)

Change frontmatter:
```yaml
---
name: cag-timneh-specialist
description: Rebuilds and manages all CAG Timneh African Grey pages. Deep knowledge of Timneh vs Congo distinctions, Timneh pricing ($1,200–$2,500), and intelligent cross-sell between the two variants. Handles /timneh-african-grey-for-sale/, and any Timneh-specific variant pages.
---
```

Replace the most important distinction table (this is the core of the agent):
```markdown
## The Most Important Distinction This Agent Must Never Get Wrong

### Congo African Grey (CAG)
| Attribute | Value |
|-----------|-------|
| **Species** | Psittacus erithacus erithacus |
| **Weight** | 400–600g |
| **Tail** | Bright red |
| **Body** | Lighter grey, larger frame |
| **Price** | $1,500–$3,500 |
| **Talker** | One of the best in the parrot world |
| **Temperament** | Confident, assertive, can be one-person bird |
| **Best for** | Experienced owners, single-person households, dedicated time |

### Timneh African Grey (TAG)
| Attribute | Value |
|-----------|-------|
| **Species** | Psittacus erithacus timneh |
| **Weight** | 275–375g |
| **Tail** | Maroon/dark red |
| **Body** | Darker grey, smaller frame, pinkish upper mandible |
| **Price** | $1,200–$2,500 |
| **Talker** | Talks earlier than Congo — often before 12 months |
| **Temperament** | Calmer, more adaptable, handles multiple people better |
| **Best for** | First-time African Grey owners, families, apartment living |

### Cross-Sell Logic
| Buyer signal | Recommend |
|---|---|
| "I want the smartest parrot" | Both. Congo has slight reputation edge — explain both. |
| "I have young children" | Lead with Timneh (calmer, more adaptable). |
| "I'm a first-time parrot owner" | Lead with Timneh (forgiving, earlier talker). |
| "I want the bird to talk early" | Timneh — talks earlier than Congo. |
| "Budget under $1,500" | Timneh ($1,200–$2,500). |
| "What's the difference between Congo and Timneh?" | This IS the cross-sell moment. |
```

Replace 6 Maltese pages → Timneh pages to manage:
```markdown
## Timneh Pages to Manage

```bash
ls site/content/ | grep "timneh"
```

Build if missing: `/timneh-african-grey-for-sale/` and `/timneh-vs-congo-african-grey/`
```

- [ ] **Step 2: Adapt `cag-variant-specialist.md`** (from `size-specialist.md`)

Change frontmatter:
```yaml
---
name: cag-variant-specialist
description: Rebuilds the two African Grey variant pages — /congo-african-grey-for-sale/ and /timneh-african-grey-for-sale/ — section-by-section. Inserts cross-links between both and a shared variant comparison table. Both pages form the variant cluster with cross-sell opportunities.
---
```

Replace three size pages → two variant pages:
```markdown
## Variant Pages (replaces size pages)

| Page | Slug | Price | Priority |
|------|------|-------|----------|
| Congo African Grey | /congo-african-grey-for-sale/ | $1,500–$3,500 | High |
| Timneh African Grey | /timneh-african-grey-for-sale/ | $1,200–$2,500 | High |

These two pages form a **variant cluster**. They must cross-link to each other and share a consistent structure with a comparison table so visitors can self-select before contacting CAG.
```

Replace sacred elements section — update for CAG variant pages:
```markdown
## Sacred Elements — Never Change

### Congo African Grey page
❌ H1 (if exists), canonical, all JSON-LD schema blocks

### Timneh African Grey page
❌ H1 (if exists), canonical, all JSON-LD schema blocks

Check on startup:
```bash
grep -n "<h1\|canonical\|ld+json" site/content/congo-african-grey-for-sale/*.md 2>/dev/null | head -5
grep -n "<h1\|canonical\|ld+json" site/content/timneh-african-grey-for-sale/*.md 2>/dev/null | head -5
```
```

Replace size comparison table with variant comparison table (already in `skills/framework-qab.md` and `skills/framework-eeat.md` — reference those for cross-sell logic).

- [ ] **Step 3: Adapt `cag-bird-personality.md`** (from `puppy-personality.md`)

Change frontmatter:
```yaml
---
name: cag-bird-personality
description: Generates CLEO/REX-style African Grey personality profiles for individual bird listings. Each profile matches a bird's energy, talkativeness, and traits to a specific buyer archetype — apartment dwellers, active families, seniors, experienced parrot owners, first-time owners. Reads data/price-matrix.json for pricing.
---
```

Replace LORI/MIKE buyer archetypes with CAG bird-buyer archetypes:
```markdown
## Buyer Archetype Library — CLEO/REX Framework

### CLEO — "The Quiet Companion Seeker"
**Profile:** Retiree, empty nester, or single person with calm household. Wants a talking companion, daily interaction, calm energy.
**Fears:** Too loud, destructive, requires too much stimulation
**Language:** "bonds deeply," "prefers calm routines," "quiet apartment friendly," "one-person bird"
**Match to bird:** Lower energy, prefers one handler, routine-oriented

### REX — "The Engaged Family"
**Profile:** Family with older children (10+), experienced with pets, wants an interactive bird.
**Fears:** Too shy, won't interact with whole family, gets stressed
**Language:** "social and adaptable," "handles multiple family members," "curiosity-driven," "loves activity"
**Match to bird:** Timneh tendency (handles multiple people), high interaction tolerance

### NOVA — "The First-Time African Grey Owner"
**Profile:** No prior parrot experience, has done research, wants a forgiving introduction to African Greys.
**Fears:** Too demanding, behavioral problems, expensive mistakes
**Language:** "beginner-friendly," "forgiving of schedule changes," "earlier talker," "responds well to routine"
**Match to bird:** Timneh (calmer), well-socialized, consistent hand-raising history

### SAGE — "The Experienced Parrot Owner"
**Profile:** Has owned parrots before (Amazons, Cockatoos, or smaller species), ready for an African Grey.
**Fears:** Regression in a new home, trust issues from previous owner
**Language:** "bonds intensely," "tests boundaries early but rewards patience," "best conversationalist in the parrot world"
**Match to bird:** Congo tendency (more assertive, rewards experienced handling), any well-socialized bird

### IRIS — "The Solo Professional"
**Profile:** Single adult, works from home or travels occasionally, wants deep bond with one bird.
**Fears:** Separation anxiety, boredom, expensive vet bills
**Language:** "thrives with dedicated one-on-one time," "learns your schedule," "travels well with conditioning"
**Match to bird:** Any well-socialized bird; note Congo tendency toward one-person bonding

---

## Profile Output Format (same structure as MFS, updated for birds)

```markdown
### [Name] — The [Archetype Match]

[Name] is a [variant] African Grey hatched [hatch_date]. From the first week hand-feeding,
[pronoun] [specific behavioral observation — not generic]. 

**Best match for:** [Archetype name] — [1-sentence reason connecting bird traits to buyer archetype]

**What [pronoun]'s like:**
- [Energy level observation]
- [Interaction style — with one person vs multiple]  
- [Talking/vocalization behavior observed]
- [One specific personality trait that stands out]

**Documentation included:** CITES captive-bred permit · DNA sexing certificate · Avian vet health certificate · Hatch certificate + band #[NUMBER]

**Price:** $[price] · Deposit holds [name] · Available [available_date]

[Inquiry button → #contact]
```

- [ ] **Step 4: Verify all 3**

```bash
cd /Users/apple/Downloads/CAG
grep -l "CAG Project Context" .claude/agents/cag-timneh-specialist.md \
  .claude/agents/cag-variant-specialist.md .claude/agents/cag-bird-personality.md | wc -l
# Expected: 3

grep -n "Maltese\|maltese\|AKC\|teacup\|toy\|mini\|LORI\|MIKE\|puppy\|Puppy\|litter" \
  .claude/agents/cag-timneh-specialist.md .claude/agents/cag-variant-specialist.md \
  .claude/agents/cag-bird-personality.md
# Expected: no output

grep -c "Congo\|Timneh\|CITES" .claude/agents/cag-timneh-specialist.md
# Expected: multiple matches
```

- [ ] **Step 5: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-timneh-specialist.md .claude/agents/cag-variant-specialist.md \
  .claude/agents/cag-bird-personality.md
git commit -m "feat: add variant and product agents Wave 8 (CAG Phase 2)"
```

---

## Task 9: Final Verification (all 39 agents + 4 data stubs)

- [ ] **Step 1: Confirm all 39 agent files exist**

```bash
cd /Users/apple/Downloads/CAG
ls .claude/agents/cag-*.md | wc -l
# Expected: 43 total (4 existing Phase 1 + 39 Phase 2)
# Phase 1 existing: cag-competitor-intel, cag-competitor-registry, cag-rank-tracker, cag-self-update
# Phase 2 new (39): all agents from Tasks 1-8
```

- [ ] **Step 2: Confirm CAG context block in every Phase 2 agent**

```bash
cd /Users/apple/Downloads/CAG
for f in .claude/agents/cag-meta-description-agent.md .claude/agents/cag-keyword-verifier.md \
  .claude/agents/cag-redirect-manager.md .claude/agents/cag-external-link-agent.md \
  .claude/agents/cag-deploy-verifier.md .claude/agents/cag-agent-system-qa.md \
  .claude/agents/cag-footer-standardizer.md .claude/agents/cag-google-map-agent.md \
  .claude/agents/cag-image-pipeline.md .claude/agents/cag-gsc-analytics.md \
  .claude/agents/cag-llm-keyword-intel.md .claude/agents/cag-conversion-tracker.md \
  .claude/agents/cag-ab-test-agent.md .claude/agents/cag-content-architect.md \
  .claude/agents/cag-structure-architect.md .claude/agents/cag-framework-agent.md \
  .claude/agents/cag-angle-agent.md .claude/agents/cag-hub-builder.md \
  .claude/agents/cag-batch-rebuilder.md .claude/agents/cag-faq-agent.md \
  .claude/agents/cag-paa-agent.md .claude/agents/cag-blog-post-agent.md \
  .claude/agents/cag-case-study-agent.md .claude/agents/cag-seo-content-writer.md \
  .claude/agents/cag-section-builder.md .claude/agents/cag-about-builder.md \
  .claude/agents/cag-contact-form-updater.md .claude/agents/cag-interactive-component.md \
  .claude/agents/cag-homepage-builder.md .claude/agents/cag-location-builder.md \
  .claude/agents/cag-comparison-builder.md .claude/agents/cag-purchase-guide.md \
  .claude/agents/cag-species-guide-builder.md .claude/agents/cag-financial-strategist.md \
  .claude/agents/cag-clutch-manager.md .claude/agents/cag-scam-specialist.md \
  .claude/agents/cag-timneh-specialist.md .claude/agents/cag-variant-specialist.md \
  .claude/agents/cag-bird-personality.md; do
  count=$(grep -c "CAG Project Context" "$f" 2>/dev/null || echo 0)
  if [ "$count" -eq 0 ]; then echo "MISSING context block: $f"; fi
done
echo "Context block check complete"
```

- [ ] **Step 3: Confirm zero MFS residue across all Phase 2 agents**

```bash
cd /Users/apple/Downloads/CAG
grep -rn "MaltipoosForsale\|site2/\|Lawrence Magee\|Cathy Magee\|Omaha, Nebraska\|Embark DNA\|OFA certification\|AKC registration\|litter-inventory\|maltipoo\|Maltipoo" \
  .claude/agents/cag-meta-description-agent.md .claude/agents/cag-keyword-verifier.md \
  .claude/agents/cag-redirect-manager.md .claude/agents/cag-external-link-agent.md \
  .claude/agents/cag-deploy-verifier.md .claude/agents/cag-agent-system-qa.md \
  .claude/agents/cag-footer-standardizer.md .claude/agents/cag-google-map-agent.md \
  .claude/agents/cag-image-pipeline.md .claude/agents/cag-gsc-analytics.md \
  .claude/agents/cag-llm-keyword-intel.md .claude/agents/cag-conversion-tracker.md \
  .claude/agents/cag-ab-test-agent.md .claude/agents/cag-content-architect.md \
  .claude/agents/cag-structure-architect.md .claude/agents/cag-framework-agent.md \
  .claude/agents/cag-angle-agent.md .claude/agents/cag-hub-builder.md \
  .claude/agents/cag-batch-rebuilder.md .claude/agents/cag-faq-agent.md \
  .claude/agents/cag-paa-agent.md .claude/agents/cag-blog-post-agent.md \
  .claude/agents/cag-case-study-agent.md .claude/agents/cag-seo-content-writer.md \
  .claude/agents/cag-section-builder.md .claude/agents/cag-about-builder.md \
  .claude/agents/cag-contact-form-updater.md .claude/agents/cag-interactive-component.md \
  .claude/agents/cag-homepage-builder.md .claude/agents/cag-location-builder.md \
  .claude/agents/cag-comparison-builder.md .claude/agents/cag-purchase-guide.md \
  .claude/agents/cag-species-guide-builder.md .claude/agents/cag-financial-strategist.md \
  .claude/agents/cag-clutch-manager.md .claude/agents/cag-scam-specialist.md \
  .claude/agents/cag-timneh-specialist.md .claude/agents/cag-variant-specialist.md \
  .claude/agents/cag-bird-personality.md 2>/dev/null
# Expected: no output
```

- [ ] **Step 4: Confirm data stubs exist**

```bash
cd /Users/apple/Downloads/CAG
ls docs/reference/design-system.md data/price-matrix.json data/locations.json data/financial-entities.json
# Expected: all 4 files exist
```

- [ ] **Step 5: Confirm CITES in all heavy agents**

```bash
cd /Users/apple/Downloads/CAG
for f in .claude/agents/cag-species-guide-builder.md .claude/agents/cag-financial-strategist.md \
  .claude/agents/cag-clutch-manager.md .claude/agents/cag-scam-specialist.md \
  .claude/agents/cag-homepage-builder.md .claude/agents/cag-location-builder.md; do
  count=$(grep -c "CITES" "$f" 2>/dev/null || echo 0)
  echo "$count CITES mentions: $f"
done
# Expected: all files show count > 3
```

- [ ] **Step 6: Final commit if any unstaged files remain**

```bash
cd /Users/apple/Downloads/CAG
git status
# If clean: done
# If files unstaged:
git add .claude/agents/ data/ docs/reference/design-system.md
git commit -m "feat: complete CAG Phase 2 full agent transfer (39 agents + data stubs)"
```

---

## Complete Agent Transfer Map

| # | MFS Source | CAG Target | Wave | Weight |
|---|------------|------------|------|--------|
| 1 | meta-description-agent.md | cag-meta-description-agent.md | 1 | Light |
| 2 | keyword-verifier.md | cag-keyword-verifier.md | 1 | Light |
| 3 | redirect-manager.md | cag-redirect-manager.md | 1 | Light |
| 4 | external-link-agent.md | cag-external-link-agent.md | 1 | Light |
| 5 | deploy-verifier.md | cag-deploy-verifier.md | 1 | Light |
| 6 | agent-system-qa.md | cag-agent-system-qa.md | 1 | Light |
| 7 | footer-standardizer.md | cag-footer-standardizer.md | 1 | Light |
| 8 | google-map-agent.md | cag-google-map-agent.md | 1 | Light |
| 9 | image-pipeline.md | cag-image-pipeline.md | 1 | Light |
| 10 | gsc-analytics.md | cag-gsc-analytics.md | 2 | Moderate |
| 11 | llm-keyword-intel.md | cag-llm-keyword-intel.md | 2 | Moderate |
| 12 | conversion-tracker.md | cag-conversion-tracker.md | 2 | Moderate |
| 13 | ab-test-agent.md | cag-ab-test-agent.md | 2 | Moderate |
| 14 | content-architect.md | cag-content-architect.md | 3 | Moderate |
| 15 | structure-architect.md | cag-structure-architect.md | 3 | Moderate |
| 16 | framework-agent.md | cag-framework-agent.md | 3 | Moderate |
| 17 | angle-agent.md | cag-angle-agent.md | 3 | Moderate |
| 18 | hub-builder.md | cag-hub-builder.md | 3 | Moderate |
| 19 | batch-rebuilder.md | cag-batch-rebuilder.md | 3 | Light |
| 20 | faq-agent.md | cag-faq-agent.md | 4 | Moderate |
| 21 | paa-agent.md | cag-paa-agent.md | 4 | Moderate |
| 22 | blog-post-agent.md | cag-blog-post-agent.md | 4 | Moderate |
| 23 | case-study-agent.md | cag-case-study-agent.md | 4 | Moderate |
| 24 | seo-content-writer.md | cag-seo-content-writer.md | 4 | Moderate |
| 25 | section-builder.md | cag-section-builder.md | 5 | Heavy |
| 26 | about-builder.md | cag-about-builder.md | 5 | Moderate |
| 27 | contact-form-updater.md | cag-contact-form-updater.md | 5 | Light |
| 28 | interactive-component.md | cag-interactive-component.md | 5 | Moderate |
| 29 | homepage-builder.md | cag-homepage-builder.md | 6 | Heavy |
| 30 | location-builder.md | cag-location-builder.md | 6 | Heavy |
| 31 | comparison-builder.md | cag-comparison-builder.md | 6 | Heavy |
| 32 | purchase-guide.md | cag-purchase-guide.md | 6 | Heavy |
| 33 | breed-guide-builder.md | cag-species-guide-builder.md | 7 | Heavy |
| 34 | financial-strategist.md | cag-financial-strategist.md | 7 | Heavy |
| 35 | litter-manager.md | cag-clutch-manager.md | 7 | Heavy |
| 36 | adoption-specialist.md | cag-scam-specialist.md | 7 | Heavy |
| 37 | maltese-breed-agent.md | cag-timneh-specialist.md | 8 | Heavy |
| 38 | size-specialist.md | cag-variant-specialist.md | 8 | Heavy |
| 39 | puppy-personality.md | cag-bird-personality.md | 8 | Heavy |

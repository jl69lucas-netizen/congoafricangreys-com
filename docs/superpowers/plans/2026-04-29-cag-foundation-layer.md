# CAG Foundation Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transfer and adapt 10 MFS foundation files (1 agent + 9 skills) to CAG, replacing all Maltipoo/MFS domain references with African Grey/CAG equivalents and adding the standard CAG context block to every file.

**Architecture:** Template-first approach — the standard CAG context block is defined once (in Task 1) and pasted verbatim into every subsequent file. Each file is read from `/Users/apple/Downloads/MFS/`, adapted per its specific notes, and written to `/Users/apple/Downloads/CAG/`. Light files (self-update, session-closer) need only path/name swaps; heavy files (grill-me, framework-eeat) need section rewrites.

**Tech Stack:** Markdown skill/agent files. No code compilation. Verification is grep-based.

**Execution order (parallelizable):**
- **Wave 1 (sequential):** Task 1 only — validates pattern before bulk apply
- **Wave 2 (parallel):** Tasks 2 + 3 simultaneously (grill-me + session-closer)
- **Wave 3 (parallel):** Tasks 4–10 simultaneously (all 7 framework skills)
- **Wave 4 (sequential):** Task 11 — final verification across all 10 files

---

## Standard CAG Context Block (paste verbatim into every file after Golden Rule)

```markdown
## CAG Project Context
> **Site:** CongoAfricanGreys.com — captive-bred African Grey parrot breeder
> **Variants:** Congo African Grey (CAG, $1,500–$3,500) · Timneh African Grey (TAG, $1,200–$2,500) — treat as distinct product lines (equivalent to MFS size tiers)
> **CITES:** African Greys are CITES Appendix II. All birds captive-bred with full documentation. Never imply wild-caught or illegal trade.
> **Trust pillars:** USDA AWA license · CITES captive-bred docs · DNA sexing cert · Avian vet health certificate · Hatch certificate + band number · Fully weaned + hand-raised
> **Buyer fears (ranked):** Scam/fraud · Sick bird · CITES documentation gaps · Wild-caught suspicion · Post-sale abandonment
> **Content root:** `site/content/` | **Sessions:** `sessions/`
> **Confidence Gate:** ≥97% before writing any site file
```

## Global Substitution Map (apply to every file)

| Find | Replace |
|------|---------|
| MaltipoosForsale.com | CongoAfricanGreys.com |
| MaltipoosForsale | CongoAfricanGreys |
| MFS | CAG |
| Maltipoo / maltipoo / puppy / dog | African Grey parrot / bird / parrot |
| Lawrence & Cathy Magee | `[BREEDER_NAME]` |
| Lawrence or Cathy | `[BREEDER_NAME]` |
| Omaha, Nebraska | `[BREEDER_LOCATION]` |
| site2/ | site/content/ |
| Embark DNA | DNA sexing certificate + avian vet health cert |
| OFA certification | Avian vet health certificate |
| AKC registration | CITES captive-bred documentation |
| Puppy Culture | Hand-feeding / hand-raising socialization |
| 10-year health guarantee | Health guarantee (`[DURATION_TBD]`) |
| litter | clutch |
| whelping | hatching |
| $1,200–$1,700 | $1,500–$3,500 (CAG) / $1,200–$2,500 (TAG) |
| Flight Nanny | IATA-compliant bird shipping |
| Formspree | `[PAYMENT_METHOD_TBD]` |

---

## Task 1: Create `cag-self-update.md` (Light — validates approach)

**Files:**
- Read: `/Users/apple/Downloads/MFS/.claude/agents/self-update.md`
- Create: `/Users/apple/Downloads/CAG/.claude/agents/cag-self-update.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/.claude/agents/self-update.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these changes:
1. Frontmatter `description`: change to "Scheduled Sunday agent — checks Claude Code release notes, MCP registry updates, and new tool patterns, then proposes patches to CAG skill files and CLAUDE.md. Keeps the agent system current without manual maintenance."
2. After the Golden Rule block, insert the **Standard CAG Context Block** (see top of plan)
3. In `## Purpose`: change "Self-Update Agent for MaltipoosForsale.com" → "Self-Update Agent for CongoAfricanGreys.com"
4. In `## Rules You Must Follow`, Rule 1: change "Never edit site2/" → "Never edit site/content/"
5. In `## Output Format`, change all "MFS" references to "CAG" (e.g., "MFS agents" → "CAG agents", "MFS skill files" → "CAG skill files")
6. Apply Global Substitution Map throughout

Write to `/Users/apple/Downloads/CAG/.claude/agents/cag-self-update.md`

- [ ] **Step 3: Verify — no MFS residue, CAG context block present**

```bash
cd /Users/apple/Downloads/CAG
grep -n "MaltipoosForsale\|site2/\|Lawrence\|Cathy\|Omaha" .claude/agents/cag-self-update.md
# Expected: no output (zero matches)

grep -n "CAG Project Context" .claude/agents/cag-self-update.md
# Expected: 1 match

grep -n "site/content/" .claude/agents/cag-self-update.md
# Expected: 1 match (in Rules section)
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add .claude/agents/cag-self-update.md
git commit -m "feat: add cag-self-update agent (foundation layer)"
```

---

## Task 2: Create `grill-me.md` (Heavy — most CAG-specific rewrites)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/grill-me.md`
- Create: `/Users/apple/Downloads/CAG/skills/grill-me.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/grill-me.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these targeted changes:

**Frontmatter:**
```yaml
---
name: grill-me
description: Session starter — reads current CAG project state, grills you on business goals and today's task (10-12 questions one at a time), writes a session brief, and proposes a CLAUDE.md patch. Run this before any build work.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---
```

**Title line:** `# Grill Me — CAG Session Starter`

**Purpose paragraph:** Change "You are the session-starter for MaltipoosForsale.com" → "You are the session-starter for CongoAfricanGreys.com"

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Q2 — Traffic Reality** — replace the entire Q2 block with:
```markdown
**Q2 — Traffic Reality** *(generate dynamically from top-pages.md)*
Look at top-pages.md and identify the highest-impression query that has a weak position (above 20) OR the query with clicks but a page that hasn't been redesigned. Then ask specifically about it. Example:
> "Your 'congo african grey for sale' query gets 46 clicks but sits at position 16.2 — is today's goal to push that ranking, redesign the page, or something else entirely?"

If all top pages are healthy, ask about the query with the biggest gap between impressions and clicks (high impressions, low CTR).
```

**Q10 — Design Direction** — replace the three options with:
```markdown
**Q10 — Design Direction**
Choose one:
> "For this page — are we: (A) applying the CAG design system from scratch (Phase 2 TBD), (B) patching the existing layout with targeted fixes, or (C) matching the style of /african-grey-parrot-for-sale-florida/ as the reference page?"
```

**Step 3 — Handoff** — replace the skill list with:
```markdown
> "Session brief saved. CLAUDE.md updated. Ready to start — which agent or skill should we invoke first?
>
> Available for this session:
> - `@cag-competitor-intel` — deep analysis on a competitor or all 30
> - `@cag-rank-tracker` — weekly monitoring run (Sundays)
> - Phase 2 page-building skills: coming soon"
```

Apply Global Substitution Map throughout for any remaining MFS references.

Write to `/Users/apple/Downloads/CAG/skills/grill-me.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "MaltipoosForsale\|site2/\|Lawrence\|Cathy\|Omaha\|orange/white\|male-vs-female-maltipoo" skills/grill-me.md
# Expected: no output

grep -n "CAG Project Context" skills/grill-me.md
# Expected: 1 match

grep -n "congo african grey\|top-pages" skills/grill-me.md
# Expected: at least 1 match each (Q2 section)

grep -n "african-grey-parrot-for-sale-florida" skills/grill-me.md
# Expected: 1 match (Q10 reference page)
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/grill-me.md
git commit -m "feat: add grill-me session starter skill (foundation layer)"
```

---

## Task 3: Create `session-closer.md` (Light)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/session-closer.md`
- Create: `/Users/apple/Downloads/CAG/skills/session-closer.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/session-closer.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these changes:

**Frontmatter description:** "End-of-session ritual — reviews what was built, fills the 'What's Next' section of today's session brief, proposes next session priorities, and optionally patches CLAUDE.md. Run this before ending any build session."

**Purpose paragraph:** Change "Session Closer for MaltipoosForsale.com" → "Session Closer for CongoAfricanGreys.com"

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Step 5 — Closing Confirmation:** Update the closing message:
```markdown
> "Session closed.
>
> Brief: `sessions/[today's date]-session-brief.md` — What's Next filled.
> CLAUDE.md: [updated / no changes needed]
> Next session starts with: `/grill-me`
>
> See you next session."
```

Apply Global Substitution Map throughout (especially any `site2/` references in the git log step).

Write to `/Users/apple/Downloads/CAG/skills/session-closer.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "MaltipoosForsale\|site2/\|Lawrence\|Cathy\|Omaha" skills/session-closer.md
# Expected: no output

grep -n "CAG Project Context" skills/session-closer.md
# Expected: 1 match
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/session-closer.md
git commit -m "feat: add session-closer skill (foundation layer)"
```

---

## Task 4: Create `framework-eeat.md` (Heavy — CITES section added)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/framework-eeat.md`
- Create: `/Users/apple/Downloads/CAG/skills/framework-eeat.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/framework-eeat.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these targeted changes:

**Frontmatter description:** "Reference guide for Google's E-E-A-T framework applied to CAG content. Use when auditing or building any page that must signal credibility to Google's quality raters and AI systems. Covers on-page signals, schema, CITES compliance framing, and author attribution."

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Replace `## MFS E-E-A-T Assets` section entirely:**
```markdown
## CAG E-E-A-T Assets

### Experience Signals (first-hand, lived)
- [BREEDER_NAME]: [X]+ years breeding African Grey parrots captive
- [N]+ families served — named in testimonials
- Specific clutch stories, hatching observations, hand-feeding notes
- [BREEDER_LOCATION] (specific, verifiable)
- Congo vs Timneh breeding distinctions from direct experience

### Expertise Signals (knowledge, credentials)
- USDA Animal Welfare Act license — include license number where possible
- CITES Appendix II captive-bred documentation — named and numbered
- DNA sexing certificate — names the specific avian lab provider
- Avian vet health certificate — names the vet clinic and vet
- Hand-feeding/hand-raising socialization protocol — documented from hatch
- Hatch certificate + band/ring number — verifiable per bird

### Authoritativeness Signals (external recognition)
- Customer testimonials with full names and locations
- CITES compliance (federal-level recognition of captive breeding)
- State/federal regulatory compliance documentation
- Links from credible avian sources (World Parrot Trust, AFA, etc.)

### Trustworthiness Signals (accuracy, transparency)
- Prices shown openly on pages (no "DM for price")
- CITES documentation available to buyers (not just claimed)
- Avian vet health certificates included with every bird
- DNA sexing certificate included with every bird
- Hatch certificate + band number for each bird
- Real contact info: phone, email, physical address
- Privacy policy and terms pages exist
```

**Replace author block example:**
```html
<div class="cag-author-block">
  <p class="cag-body">
    <strong>Written by [BREEDER_NAME],</strong> USDA AWA-licensed African Grey breeder 
    in [BREEDER_LOCATION]. Specializing in captive-bred Congo and Timneh African Greys 
    with full CITES documentation.
  </p>
</div>
```

**Add new section after `## On-Page E-E-A-T Implementation`:**
```markdown
## CITES E-E-A-T — The CAG Differentiator

African Greys are CITES Appendix II — the same international treaty that governs ivory and rhino horn trade. This makes CITES compliance documentation the single strongest E-E-A-T signal available to CAG, because:

1. **No competitor uses it.** The gap matrix shows only birdsforsales.com mentions USDA + CITES. Every other Tier 1 breeder is silent.
2. **It is externally verifiable.** CITES documentation is issued by the USDA/USFWS — not self-reported.
3. **It addresses the buyer's deepest fear.** Wild-caught bird suspicion and CBP seizure risk are uniquely parrot fears with no Maltipoo equivalent.

### CITES Trust Language (use on every page)
```html
<div class="cag-trust-bar">
  <span>USDA AWA Licensed</span>
  <span>CITES Appendix II Captive-Bred</span>
  <span>DNA Sexed</span>
  <span>Avian Vet Certified</span>
</div>
```

### CITES in Body Copy
Replace: "All our birds are legal and documented."
With: "Every bird comes with CITES captive-bred documentation — the federal paperwork issued under the Convention on International Trade in Endangered Species. You can verify the documentation is genuine. CBP has never seized a bird purchased from [BREEDER_NAME] because every transaction is fully documented before the bird ships."
```

**Replace `## E-E-A-T Audit Checklist`:**
Update checklist to include CITES-specific items:
```markdown
## E-E-A-T Audit Checklist

For any page audit, score each dimension 1–5:

### Experience (1–5)
- [ ] First-person voice ("we've seen," "in our experience hatching")
- [ ] Specific timeframes and numbers ("in [year], we changed our hand-feeding protocol because...")
- [ ] Real observations ("Timneh chicks require more intensive socialization in weeks 6–10")

### Expertise (1–5)
- [ ] Credentials named (USDA AWA, CITES, DNA sexing lab, avian vet)
- [ ] Technical terms used correctly (clutch, fledgling, PBFD, CITES Appendix II)
- [ ] Data cited with sources ("per USFWS CITES captive-bred permit requirements")

### Authoritativeness (1–5)
- [ ] Testimonials with full names and locations
- [ ] CITES documentation number or permit reference
- [ ] External links to verifiable sources (USFWS, avian vet clinic, DNA lab)

### Trustworthiness (1–5)
- [ ] Contact info visible (not just a form)
- [ ] Prices stated openly
- [ ] CITES paperwork described specifically (not just "fully documented")
- [ ] Health certificate terms specific (vet name, date, conditions checked)
- [ ] CITES language present on every page
- [ ] Wild-caught disclaimer visible on listing pages
- [ ] No unverifiable superlatives ("best," "#1," "top-rated")

**Score 16–20:** Strong E-E-A-T — maintain
**Score 10–15:** Needs improvement — add experience/expertise signals
**Score < 10:** Urgent — Google quality raters would flag this page
```

**Replace `## Common E-E-A-T Failures` table:**
```markdown
## Common E-E-A-T Failures at CAG

| Failure | Fix |
|---------|-----|
| "All our birds are legal" (vague) | "CITES Appendix II captive-bred docs — permit number available" |
| "Health tested" (unverified) | "Avian vet cert — [VET_NAME], certificate included with bird" |
| No author name on content | Add [BREEDER_NAME] author block |
| Prices hidden ("contact us") | Show price ranges openly ($1,500–$3,500 CAG, $1,200–$2,500 TAG) |
| Generic testimonials | Name + location + specific outcome |
| "Our birds are captive-bred" | "CITES captive-bred documentation — verifiable with USFWS" |
```

**Replace Person + LocalBusiness schema examples:**
```json
{
  "@type": "Person",
  "name": "[BREEDER_NAME]",
  "jobTitle": "USDA AWA Licensed African Grey Breeder",
  "worksFor": { "@type": "Organization", "name": "CongoAfricanGreys.com" },
  "address": { "@type": "PostalAddress", "addressLocality": "[BREEDER_LOCATION]" }
}
```
```json
{
  "@type": "LocalBusiness",
  "name": "CongoAfricanGreys.com",
  "founder": "[BREEDER_NAME]",
  "address": { "addressLocality": "[BREEDER_LOCATION]" },
  "aggregateRating": { "@type": "AggregateRating" }
}
```

Apply Global Substitution Map for any remaining references.

Write to `/Users/apple/Downloads/CAG/skills/framework-eeat.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "MaltipoosForsale\|Embark DNA\|OFA cert\|AKC reg\|Lawrence\|Cathy\|Omaha\|site2/" skills/framework-eeat.md
# Expected: no output

grep -n "CITES" skills/framework-eeat.md
# Expected: 10+ matches (CITES section is new and extensive)

grep -n "CAG Project Context" skills/framework-eeat.md
# Expected: 1 match

grep -n "BREEDER_NAME" skills/framework-eeat.md
# Expected: 3-5 matches (author block, schema, failure table)
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/framework-eeat.md
git commit -m "feat: add framework-eeat skill with CITES E-E-A-T section (foundation layer)"
```

---

## Task 5: Create `framework-aida.md` (Moderate)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/framework-aida.md`
- Create: `/Users/apple/Downloads/CAG/skills/framework-aida.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/framework-aida.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these targeted changes:

**Frontmatter description:** "Reference guide for the AIDA framework applied to CAG homepage, purchase guide, and high-intent commercial pages. Use when building pages that must move a visitor from cold awareness to inquiry submission in a single session."

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Replace `## When to Use AIDA at MFS` table:**
```markdown
## When to Use AIDA at CAG

| Page | AIDA Application |
|------|-----------------|
| Homepage | Full AIDA arc across 18 sections |
| `/where-to-buy-african-greys-near-me/` | AIDA with buyer-fear overlay |
| State pages (FL, TX, CA, etc.) | AIDA with geo-specific desire |
| `/congo-african-grey-for-sale/` | AIDA compressed — hero to CTA fast |
| `/timneh-african-grey-for-sale/` | AIDA compressed — hero to CTA fast |

**Don't use AIDA for:** Informational pages, care guides, comparison pages — use Inverse Pyramid or QAB instead.
```

**Replace Attention hook examples:**
```markdown
**Good CAG Attention hook:**
```
H1: "Congo or Timneh — which African Grey is the right companion for your family?"
Subhead: "[X] years. [N]+ families. One breeder who answers the phone after the sale — with CITES documentation on every bird."
```

**Bad Attention hook:**
```
H1: "Welcome to CongoAfricanGreys.com"
(No reader framing, no tension, no hook)
```
```

**Replace Interest techniques section content:**
```markdown
**CAG Interest content:**
- The problem with Craigslist / Facebook Marketplace (no CITES docs, CashApp payment, no recourse)
- The problem with "cheap african grey" sites (no USDA license, payment via no-recourse apps)
- What "captive-bred with documentation" actually means (CITES + USDA AWA + avian vet cert)
```

**Replace Desire feature→emotion transformations:**
```markdown
**Feature → Desire transformation:**
```
Feature:  "CITES Appendix II captive-bred documentation on every bird"
Desire:   "You'll know your bird is legally documented before it ever ships — no customs seizure risk, 
           no questions at your door, no heartbreak after bonding with a bird that can't legally stay."

Feature:  "IATA-compliant bird shipping with live animal protocols"
Desire:   "Your African Grey travels under IATA live animal standards — temperature-controlled, 
           with an avian health cert. Not a Craigslist seller's shoebox."
```
```

**Replace Action template:**
```markdown
**CAG Action template:**
```html
<h2>Ready to Meet Your African Grey?</h2>
<p>Fill out our quick inquiry form. [BREEDER_NAME] will respond personally within 24 hours 
   — not an automated email, a real reply with available birds that match your family.</p>
<p><strong>Deposit holds your bird.</strong> Health guarantee + CITES documentation included.</p>
[Inquiry Form — 3 fields: name, email, variant preference (Congo / Timneh)]
<p class="cag-form-note">We respond within 24 hours. No spam, no pressure, no bait-and-switch.</p>
```
```

Apply Global Substitution Map for any remaining references.

Write to `/Users/apple/Downloads/CAG/skills/framework-aida.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "MaltipoosForsale\|Maltipoo\|maltipoo\|Lawrence\|Cathy\|Omaha\|site2/\|Embark\|Flight Nanny\|teacup\|toy\|mini\|standard" skills/framework-aida.md
# Expected: no output

grep -n "CAG Project Context" skills/framework-aida.md
# Expected: 1 match

grep -n "Congo\|Timneh\|CITES\|african grey" skills/framework-aida.md
# Expected: multiple matches
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/framework-aida.md
git commit -m "feat: add framework-aida skill (foundation layer)"
```

---

## Task 6: Create `framework-aio-geo.md` (Moderate)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/framework-aio-geo.md`
- Create: `/Users/apple/Downloads/CAG/skills/framework-aio-geo.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/framework-aio-geo.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these targeted changes:

**Frontmatter description:** "Reference guide for AIO (AI Overview) and GEO (Generative Engine Optimization) applied to CAG content. Use when building or auditing any page that should be cited by ChatGPT, Perplexity, Google AIO, or other AI answer engines."

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Replace Entity-First Writing Pattern example:**
```markdown
**Entity-First Writing Pattern:**

AI engines parse content as entity → attribute → value. Structure content to match:

```
Entity:    African Grey Parrot
Attribute: Variants
Value:     Congo (CAG): ~400–600g, red tail, $1,500–$3,500 | Timneh (TAG): ~275–375g, maroon tail, $1,200–$2,500
Source:    docs/reference/domain-knowledge.md + CAG breeding data

Entity:    African Grey Parrot
Attribute: Lifespan
Value:     40–60 years in captivity
Source:    Ornithological data (African Grey longevity studies)

Entity:    African Grey Parrot  
Attribute: CITES Status
Value:     Appendix II — commercial trade requires documentation; captive-bred birds legal with CITES permit
Source:    USFWS CITES Appendix II listing
```

**Prose translation:**
```
Bad (vague): "African Grey parrots come in different sizes and live a long time."

Good (citable): "African Grey parrots are bred in two variants: the Congo African Grey (CAG, 
400–600g, red tail, $1,500–$3,500) and the Timneh African Grey (TAG, 275–375g, maroon tail, 
$1,200–$2,500). In captivity with proper care, African Greys live 40–60 years — one of the 
longest lifespans of any companion parrot."
```
```

**Replace FAQPage JSON-LD example:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does a Congo African Grey parrot cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Congo African Grey parrots from reputable captive breeders range from $1,500 to $3,500. Price depends on age, weaning status, and hand-training level. Every bird from CongoAfricanGreys.com includes CITES captive-bred documentation, DNA sexing certificate, avian vet health certificate, and hatch certificate."
      }
    }
  ]
}
```

**Replace Breed-specific Entity Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "Animal",
  "name": "African Grey Parrot",
  "description": "A highly intelligent parrot species native to equatorial Africa, bred in captivity under CITES Appendix II regulations.",
  "alternateName": ["Congo African Grey", "Timneh African Grey", "Grey Parrot", "Psittacus erithacus"]
}
```

**Replace AIO Content Audit grep command:**
```bash
grep -n "FAQPage\|@type.*Question" site/content/[slug]/*.md | head -10
```

**Replace Sentence-Level Checks entity consistency rule:**
- [ ] "African Grey" always capitalized (entity consistency — not "african grey" or "the parrot")
- [ ] Numbers written as numerals (400g, 60 years, $1,500 — AI parses numerals better)

**Replace GEO Targeting section — update examples from Maltipoo to African Grey throughout.**

Apply Global Substitution Map for any remaining references.

Write to `/Users/apple/Downloads/CAG/skills/framework-aio-geo.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "Maltipoo\|maltipoo\|Lawrence\|Cathy\|Omaha\|site2/\|Embark\|OFA\|AKC" skills/framework-aio-geo.md
# Expected: no output

grep -n "CAG Project Context" skills/framework-aio-geo.md
# Expected: 1 match

grep -n "Congo\|Timneh\|CITES" skills/framework-aio-geo.md
# Expected: multiple matches
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/framework-aio-geo.md
git commit -m "feat: add framework-aio-geo skill (foundation layer)"
```

---

## Task 7: Create `framework-qab.md` (Moderate)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/framework-qab.md`
- Create: `/Users/apple/Downloads/CAG/skills/framework-qab.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/framework-qab.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these targeted changes:

**Frontmatter description:** "Reference guide for the QAB framework applied to CAG FAQ sections, price pages, and comparison content. Use whenever writing FAQ items, cost breakdowns, or any content that must answer a buyer's question AND connect the answer to a personal benefit."

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Replace QAB vs Basic Q&A example:**
```markdown
**QAB:**
Q: How much does a Congo African Grey parrot cost from a reputable breeder?
A: Congo African Greys from CongoAfricanGreys.com are priced at $1,500–$3,500. This includes 
   CITES captive-bred documentation, DNA sexing certificate, avian vet health certificate, 
   hatch certificate, and a health guarantee. A deposit holds your bird.
B: Transparent pricing means no surprise documentation fees after you've already bonded with 
   your bird — and no "paperwork add-on" charges at delivery.
```

**Replace Answer Writing Rules data source references:**
- Prices: "from `docs/reference/domain-knowledge.md` — confirmed current"
- Costs: "from CAG pricing data (Phase 2: `data/price-matrix.json`)"
- Health: "per DNA sexing certificate / avian vet health cert"
- Species facts: "per ornithological data / USFWS CITES Appendix II documentation"

**Replace `## MFS FAQ Question Bank` entirely:**
```markdown
## CAG FAQ Question Bank (pre-built QAB sets)

### Price & Cost
- How much does a Congo African Grey parrot cost?
- How much does a Timneh African Grey parrot cost?
- What's the deposit to hold a bird?
- What's included in the purchase price?
- What's the total first-year cost of owning an African Grey?
- Is there a difference in price between hand-raised and parent-raised birds?

### CITES & Legality
- Do African Grey parrots come with CITES documentation?
- Are African Grey parrots legal to buy in the United States?
- What paperwork do I receive with my bird?
- What is CITES Appendix II and why does it matter?
- Can CBP (US Customs) seize my bird?

### Health & Documentation
- What health conditions do African Grey parrots have?
- What does a DNA sexing certificate confirm?
- What is PBFD and does your avian vet test for it?
- What does the avian vet health certificate cover?
- What is a hatch certificate and band number?

### Buying Process
- How do I reserve an African Grey parrot?
- Is bird shipping safe?
- How does IATA-compliant shipping work?
- Can I visit in person to meet the bird before purchasing?
- What if the bird gets sick after I bring them home?

### Species & Variants
- What's the difference between a Congo and Timneh African Grey?
- Do African Grey parrots talk?
- How long do African Grey parrots live?
- Are African Greys good for beginners?
- How much space does an African Grey need?
```

**Replace `## Minimum QAB Requirements Per Page` table:**
```markdown
## Minimum QAB Requirements Per Page

| Page Type | Min FAQ Items | Framework |
|-----------|-------------|-----------|
| Homepage | 6 | QAB |
| State pages | 6 | QAB |
| Congo for sale page | 8 | QAB |
| Timneh for sale page | 8 | QAB |
| Price/cost page | 8 | QAB |
| Comparison pages | 6 | QAB |
| Care guide | 10 | QAB |
| CITES/documentation guide | 8 | QAB |
```

Apply Global Substitution Map for any remaining references.

Write to `/Users/apple/Downloads/CAG/skills/framework-qab.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "Maltipoo\|maltipoo\|Lawrence\|Cathy\|Omaha\|Embark\|OFA\|AKC\|Flight Nanny" skills/framework-qab.md
# Expected: no output

grep -n "CAG Project Context" skills/framework-qab.md
# Expected: 1 match

grep -n "CITES\|Congo\|Timneh\|DNA sexing" skills/framework-qab.md
# Expected: multiple matches
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/framework-qab.md
git commit -m "feat: add framework-qab skill with CAG question bank (foundation layer)"
```

---

## Task 8: Create `framework-bab.md` (Moderate)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/framework-bab.md`
- Create: `/Users/apple/Downloads/CAG/skills/framework-bab.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/framework-bab.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these targeted changes:

**Frontmatter description:** "Reference guide for the BAB framework applied to CAG buyer-fear content, scam-prevention sections, and CITES safety content. Use when the reader needs to see a clear contrast between their current risky situation and the documented outcome — and CAG as the bridge."

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Replace `## When to Use BAB at MFS` table:**
```markdown
## When to Use BAB at CAG

| Page / Section | BAB Application |
|----------------|----------------|
| Scam-prevention sections | Before: CashApp seller risk → After: CITES-documented purchase |
| CITES safety sections | Before: undocumented bird risk → After: full CBP-compliant documentation |
| Health guarantee section | Before: sick bird fear → After: avian vet cert + health guarantee |
| First-time owner sections | Before: overwhelmed by complexity → After: guided and supported |
| `/how-to-avoid-african-grey-parrot-scams/` | Before: online scam → After: verified breeder checklist |

**Don't use BAB for:** Informational care content, variant comparison tables, FAQ sections.
```

**Replace BAB examples entirely:**
```markdown
## BAB in Practice — CAG Examples

### Scam-Prevention Section
```
BEFORE:
You found an African Grey for $600 on Facebook Marketplace. The photos looked real. 
The seller had a phone number. You sent $400 via CashApp as a deposit.
Then silence. The number disconnected. The profile disappeared.
That's not a rare story — it happens every week in African Grey Facebook groups.

AFTER:
Your CongoAfricanGreys.com bird comes with CITES captive-bred documentation — the federal 
paperwork issued under an international treaty. DNA sexing certificate from a licensed avian 
lab. Avian vet health certificate naming the vet and clinic. Hatch certificate with band number.
You can verify every document independently before sending a single dollar.

BRIDGE:
Buying an African Grey from a documented breeder isn't more expensive than buying from 
an online stranger — it's a different category of transaction entirely. One where the 
paperwork is real, the bird is legal, and there's a human being who answers the phone 
after the sale. [BREEDER_NAME] has done this for [N]+ families.
[CTA: Start your inquiry →]
```

### CITES Safety Section
```
BEFORE:
You bought a beautiful African Grey from a site that said "fully documented." 
Three months later, you got a letter from US Fish & Wildlife. The CITES documentation 
was forged. CBP has authority to seize the bird. You had no idea.

AFTER:
Every bird from CongoAfricanGreys.com ships with CITES captive-bred documentation 
issued under our USDA AWA license. You receive the permit number before the bird ships.
You can verify it at the USFWS website. It's not a certificate we printed — it's a 
federal document with a traceable number.

BRIDGE:
CITES documentation either exists as a federal record or it doesn't. There's no gray area.
Here's what genuine CITES captive-bred documentation looks like — and how to verify 
yours before sending any deposit. [Link: CITES verification guide]
```
```

Apply Global Substitution Map for any remaining MFS-specific references. Replace all Maltipoo fear scenarios with African Grey equivalents.

Write to `/Users/apple/Downloads/CAG/skills/framework-bab.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "Maltipoo\|maltipoo\|Lawrence\|Cathy\|Omaha\|Embark\|OFA\|rescue\|pet store\|Flight Nanny" skills/framework-bab.md
# Expected: no output

grep -n "CAG Project Context" skills/framework-bab.md
# Expected: 1 match

grep -n "CITES\|CashApp\|Facebook Marketplace" skills/framework-bab.md
# Expected: multiple matches
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/framework-bab.md
git commit -m "feat: add framework-bab skill with CAG scam/CITES examples (foundation layer)"
```

---

## Task 9: Create `framework-ebp.md` (Moderate)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/framework-ebp.md`
- Create: `/Users/apple/Downloads/CAG/skills/framework-ebp.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/framework-ebp.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these targeted changes:

**Frontmatter description:** "Reference guide for the EBP framework applied to CAG breeder credibility sections, CITES documentation explanations, and any content that must prove a claim with named evidence. Use when building trust sections that must survive skeptical scrutiny."

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Replace `## Why MFS Needs EBP` section:**
```markdown
## Why CAG Needs EBP

CAG operates in a trust-scarce market. African Grey buyers have been burned by:
- Sellers who say "CITES documented" with forged paperwork
- Facebook Marketplace listings with stock photos and CashApp payment requests
- Sites that say "captive-bred" with no documentation to show
- "Cheap african grey" sites with no USDA license, no vet cert, no recourse

EBP converts vague claims into verifiable proof. "All our birds are documented" becomes "CITES Appendix II captive-bred permit #[NUMBER] — verifiable at usfws.gov."
```

**Replace `## EBP Evidence Sources` table entirely:**
```markdown
## EBP Evidence Sources for CAG

| Claim | Evidence Source | How to Cite |
|-------|---------------|-------------|
| Legally documented | CITES captive-bred permit | "CITES Appendix II captive-bred permit — verifiable at usfws.gov" |
| Licensed breeder | USDA AWA license | "USDA AWA license #[NUMBER] — verifiable at aphis.usda.gov" |
| DNA sexed | DNA sexing certificate | "DNA sexing certificate — [LAB_NAME], certificate included with bird" |
| Health tested | Avian vet health cert | "Avian vet health certificate — [VET_NAME], issued on [date]" |
| Hand-raised | Hand-feeding log | "Hand-feeding log from hatch — documented week by week" |
| Hatch verified | Hatch certificate + band | "Hatch certificate + USFWS band #[NUMBER] — verifiable" |
| Lifespan claim | Ornithological data | "40–60 years per African Grey longevity studies" |
| Captive-bred | CITES permit + hatch cert | "CITES captive-bred permit + hatch certificate — not wild-caught" |
```

**Replace EBP Section Structure examples:**
```markdown
### Basic EBP Block (for inline credibility)
```
[Claim]: African Greys from CongoAfricanGreys.com are fully documented under CITES Appendix II.
[Evidence]: CITES captive-bred permit issued under our USDA AWA license. Permit number 
            available before any deposit is sent. Verifiable independently at usfws.gov.
[Profile]: Every bird ships with the CITES permit, DNA sexing certificate, avian vet health 
           certificate, and hatch certificate. No buyer has ever had a bird seized by CBP.
```
```

**Replace EBP vs Assertion table:**
```markdown
## EBP vs Assertion — Side-by-Side

| Assertion (weak) | EBP (strong) |
|-----------------|-------------|
| "All our birds are legal" | "CITES Appendix II captive-bred permit — verifiable at usfws.gov" |
| "Our birds are health tested" | "Avian vet certificate — [VET_NAME], certificate included" |
| "DNA sexed" | "DNA sexing certificate — [LAB_NAME], included with bird" |
| "Hand-raised from hatch" | "Hand-feeding log from day 1 — available on request" |
| "We've been breeding for X years" | "USDA AWA license #[NUMBER], breeding since [YEAR]" |
| "Health guaranteed" | "Health guarantee — full terms at [link]" |
```

**Replace grep audit command:** `site2/` → `site/content/`
```bash
grep -n "we guarantee\|health tested\|best\|top\|premier\|reputable\|captive-bred" site/content/[slug]/*.md | head -20
```

Apply Global Substitution Map for any remaining references.

Write to `/Users/apple/Downloads/CAG/skills/framework-ebp.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "Maltipoo\|maltipoo\|Lawrence\|Cathy\|Omaha\|Embark\|OFA\|AKC\|site2/" skills/framework-ebp.md
# Expected: no output

grep -n "CAG Project Context" skills/framework-ebp.md
# Expected: 1 match

grep -n "CITES\|USDA AWA\|DNA sexing\|BREEDER_NAME" skills/framework-ebp.md
# Expected: multiple matches
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/framework-ebp.md
git commit -m "feat: add framework-ebp skill with CAG evidence sources (foundation layer)"
```

---

## Task 10: Create `framework-pdb.md` (Moderate)

**Files:**
- Read: `/Users/apple/Downloads/MFS/skills/framework-pdb.md`
- Create: `/Users/apple/Downloads/CAG/skills/framework-pdb.md`

- [ ] **Step 1: Read the MFS source file**

```bash
cat /Users/apple/Downloads/MFS/skills/framework-pdb.md
```

- [ ] **Step 2: Write the adapted file**

Copy the full MFS source, then apply these targeted changes:

**Frontmatter description:** "Reference guide for the PDB framework applied to CAG buyer-fear content, CITES safety pages, and high-stakes decision pages. Use when the reader arrives with a specific pain — a scam, a CITES documentation fear, a wild-caught suspicion — and needs content that names their pain before offering the solution."

**After Golden Rule block:** Insert the **Standard CAG Context Block** (see top of plan)

**Replace `## MFS Buyer Fear Stack` entirely:**
```markdown
## CAG Buyer Fear Stack

These are the ranked fears African Grey buyers arrive with (in order of frequency):

1. **Scam fear** — "Is this breeder real or will I lose my deposit to a scammer?"
2. **CITES/legal fear** — "Is this bird legally documented? Could CBP seize it after I bring it home?"
3. **Wild-caught suspicion** — "Is this bird captive-bred or was it illegally imported?"
4. **Sick bird fear** — "What if the bird has PBFD or another disease I won't discover for months?"
5. **Support abandonment fear** — "Will the breeder answer the phone after the money is sent?"
6. **Cost uncertainty fear** — "What's the true total cost — not just the purchase price?"
```

**Replace `## PDB Application by Page` table:**
```markdown
## PDB Application by Page

| Page | Primary Pain | PDB Hook |
|------|-------------|---------|
| `/where-to-buy-african-greys-near-me/` | Scam fear | "You've seen the Facebook posts about parrot scams. Here's how to know you're not in one." |
| `/how-to-avoid-african-grey-parrot-scams/` | Scam + CITES fear | "The documentation looked real. It wasn't. Here's how to verify before you send anything." |
| `/african-grey-parrot-price/` | Cost uncertainty | "The purchase price is the smallest number in this equation." |
| State pages | Distance/trust | "You're trusting a breeder you've never met with $1,500+. Here's how to verify them." |
| `/african-grey-parrot-for-sale-*/` | Wild-caught suspicion | "Every 'cheap african grey' site you've seen — here's what they're not showing you." |
```

**Replace PDB Structure examples:**
```markdown
### Pain (1–3 sentences)
```
You found three African Grey breeders online. One has a slick website with adorable photos. 
One says "CITES documented" in the description but the price is $600. One has been operating 
since [YEAR] with a USDA AWA license number you can look up. You can't tell which one is real.
```

### Depth (2–4 sentences)
```
That uncertainty is rational. African Grey parrot scams cost US buyers millions annually — 
and CITES documentation forgery is a real phenomenon in the exotic bird market. A 
"health guarantee" from an undocumented seller is worth nothing when the seller has 
already disappeared. Your fear isn't paranoia — it's pattern recognition.
```

### Brief (1 paragraph)
```
What you need: a breeder with a verifiable USDA AWA license number, a CITES captive-bred 
permit you can independently verify at usfws.gov, a traceable payment method, and an avian 
vet health certificate naming the vet by name. Here's what each of those looks like at 
CongoAfricanGreys.com — and here's how to verify each one independently.
[CTA or link to documentation section]
```
```

**Replace `## Fear-to-Solution Map`:**
```markdown
## Fear-to-Solution Map (ready reference)

| Fear | Depth Fact | CAG Solution |
|------|-----------|-------------|
| Scam | Parrot fraud is common on Craigslist/FB Marketplace | USDA AWA license, traceable payment, [YEAR]+ history |
| CITES/legal | CITES forgery exists; CBP can seize birds post-purchase | CITES permit verifiable at usfws.gov before deposit |
| Wild-caught | "Captive-bred" is claimed freely, rarely documented | Hatch certificate + band number per bird |
| Sick bird | PBFD and other conditions can be latent for months | Avian vet health certificate, health guarantee |
| Abandonment | Most bird sellers have no post-sale support | [BREEDER_NAME] phone/email on every page |
| Hidden costs | Vet costs, cage, shipping add up to $500–$1,500+ | All-in cost guide published openly |
```

Apply Global Substitution Map for any remaining MFS-specific references.

Write to `/Users/apple/Downloads/CAG/skills/framework-pdb.md`

- [ ] **Step 3: Verify**

```bash
cd /Users/apple/Downloads/CAG
grep -n "Maltipoo\|maltipoo\|Lawrence\|Cathy\|Omaha\|Embark\|OFA\|ASPCA\|Flight Nanny\|site2/" skills/framework-pdb.md
# Expected: no output

grep -n "CAG Project Context" skills/framework-pdb.md
# Expected: 1 match

grep -n "CITES\|CBP\|wild-caught\|Facebook Marketplace" skills/framework-pdb.md
# Expected: multiple matches
```

- [ ] **Step 4: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add skills/framework-pdb.md
git commit -m "feat: add framework-pdb skill with CAG buyer fear stack (foundation layer)"
```

---

## Task 11: Final Verification (all 10 files)

- [ ] **Step 1: Confirm all 10 files exist**

```bash
ls /Users/apple/Downloads/CAG/skills/framework-*.md \
   /Users/apple/Downloads/CAG/skills/grill-me.md \
   /Users/apple/Downloads/CAG/skills/session-closer.md \
   /Users/apple/Downloads/CAG/.claude/agents/cag-self-update.md | wc -l
# Expected: 10
```

- [ ] **Step 2: Confirm CAG context block in every file**

```bash
cd /Users/apple/Downloads/CAG
grep -l "CAG Project Context" \
  skills/framework-*.md \
  skills/grill-me.md \
  skills/session-closer.md \
  .claude/agents/cag-self-update.md | wc -l
# Expected: 10
```

- [ ] **Step 3: Confirm zero MFS residue**

```bash
cd /Users/apple/Downloads/CAG
grep -rn "MaltipoosForsale\|site2/\|Lawrence Magee\|Cathy Magee\|Omaha, Nebraska\|Embark DNA\|OFA certification\|AKC registration" \
  skills/ .claude/agents/cag-self-update.md
# Expected: no output
```

- [ ] **Step 4: Confirm CITES present in EEAT and PDB**

```bash
cd /Users/apple/Downloads/CAG
grep -c "CITES" skills/framework-eeat.md skills/framework-pdb.md
# Expected: both files show count > 5
```

- [ ] **Step 5: Confirm placeholders consistent**

```bash
cd /Users/apple/Downloads/CAG
grep -rn "\[BREEDER_NAME\]\|\[BREEDER_LOCATION\]\|\[DURATION_TBD\]\|\[PAYMENT_METHOD_TBD\]" \
  skills/ .claude/agents/cag-self-update.md
# Expected: matches in framework-eeat, framework-ebp, framework-aida, grill-me, cag-self-update
```

- [ ] **Step 6: Confirm grill-me references CAG GSC data**

```bash
cd /Users/apple/Downloads/CAG
grep -n "congo african grey\|top-pages" skills/grill-me.md
# Expected: at least 1 match each
```

- [ ] **Step 7: Final commit if any loose files remain**

```bash
cd /Users/apple/Downloads/CAG
git status
# If clean: done. If files unstaged: git add + git commit -m "feat: complete CAG foundation layer (10 files)"
```

---

## Summary

| # | File | Weight | Status |
|---|------|--------|--------|
| 1 | `.claude/agents/cag-self-update.md` | Light | ☐ |
| 2 | `skills/grill-me.md` | Heavy | ☐ |
| 3 | `skills/session-closer.md` | Light | ☐ |
| 4 | `skills/framework-eeat.md` | Heavy | ☐ |
| 5 | `skills/framework-aida.md` | Moderate | ☐ |
| 6 | `skills/framework-aio-geo.md` | Moderate | ☐ |
| 7 | `skills/framework-qab.md` | Moderate | ☐ |
| 8 | `skills/framework-bab.md` | Moderate | ☐ |
| 9 | `skills/framework-ebp.md` | Moderate | ☐ |
| 10 | `skills/framework-pdb.md` | Moderate | ☐ |
| 11 | Final verification | — | ☐ |

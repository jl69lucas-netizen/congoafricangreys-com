---
name: framework-heading-hierarchy
description: H1–H6 strategic keyword placement guide for CAG pages. Maps each heading level to a specific keyword type and user intent. Use before writing or auditing any page's heading structure. Prevents empty headings, keyword-stuffed headers, and wrong intent-level targeting.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

## Golden Rule
> Every heading level targets a specific keyword type. Never use a heading just for formatting — every heading must capture a distinct search intent layer and could stand alone as a Google search query.

---

## CAG Project Context
> **Site:** CongoAfricanGreys.com — captive-bred African Grey parrot breeder
> **Variants:** Congo African Grey (CAG, $1,500–$3,500) · Timneh African Grey (TAG, $1,200–$2,500) — treat as distinct product lines
> **CITES:** African Greys are CITES Appendix II. All birds captive-bred with full documentation. Never imply wild-caught or illegal trade.
> **Trust pillars:** USDA AWA license · CITES captive-bred docs · DNA sexing cert · Avian vet health certificate · Hatch certificate + band number · Fully weaned + hand-raised
> **Buyer fears (ranked):** Scam/fraud · Sick bird · CITES documentation gaps · Wild-caught suspicion · Post-sale abandonment
> **Content root:** `site/content/` | **Sessions:** `sessions/`
> **Confidence Gate:** ≥97% before writing any site file

---

## Purpose

You are the **Heading Hierarchy Framework** for CongoAfricanGreys.com. Use this before writing or auditing any page's heading structure. It maps H1–H6 to specific keyword types, provides example patterns, and includes a full audit checklist.

---

## The 6-Level Keyword Mapping

### H1 — Primary Keyword (One Per Page, Strict)
**Maps to:** Highest-volume transactional or informational keyword for the page
**Format:** Primary keyword + variant/species modifier + optional brand or location
**Rules:**
- ONE H1 per page — never two H1s on the same page
- Never repeat the H1 text verbatim anywhere else on the page
- Include the main commercial keyword in the first 3 words where possible

**Examples:**
- `Congo African Grey Parrots for Sale | CITES Captive-Bred | CongoAfricanGreys.com`
- `Timneh African Grey for Sale in [State] | Hand-Raised, DNA Sexed`
- `Congo vs Timneh African Grey: The Complete Buyer's Comparison`

---

### H2 — Secondary Keyword + Conversational Hook
**Maps to:** Long-tail variation (location, variant modifier, or "parrot" context) + conversational wrapper
**Format:** Secondary keyword + question or benefit statement
**Rules:**
- Use 2+ H2s per section; Q&A format where it fits naturally
- H2s must form a logical narrative when scanned without body text

**3 H2 Patterns:**
- *Location Focus:* "Searching for a Tame African Grey Parrot in [State]? Meet [Name]."
- *Variant Focus:* "Meet [Name]: The Timneh African Grey Perfect for Families."
- *Benefit Focus:* "Why Every Bird Includes a CITES Captive-Bred Permit and Avian Vet Certificate."

**5 Alternative Variations Rule:**
For every core H2, generate 5 variations for A/B testing:
1. Direct statement version
2. Question version
3. Location-specific version
4. Benefit-focused version
5. Documentation/trust version

---

### H3 — Category Keywords (Specific Attributes)
**Maps to:** Attribute-level keywords: Size, Variant, Temperament, CITES documentation, Health, Talking ability, Weaning
**Format:** Category keyword + specific angle or question
**Rules:**
- H3s must be subordinate to their parent H2 (don't skip levels)
- Each H3 covers a distinct attribute angle — no two H3s under the same H2 repeat the same topic

**Examples:**
- *Size:* "How Big Will [Name] Get? Adult Weight and Size for Congo African Greys."
- *Health:* "Peace of Mind: Is [Name] DNA Sexed? What That Means for Your New Bird."
- *Documentation:* "What CITES Documentation Comes with [Name]?"
- *Temperament:* "Energetic or Calm? How to Match an African Grey's Temperament to Your Lifestyle."

---

### H4 — LSI Keywords (Contextual Depth)
**Maps to:** Latent Semantic Indexing (LSI) terms — words frequently found alongside African Grey topics
**Format:** LSI keyword or phrase + specific sub-topic
**Purpose:** Shows Google the page covers the topic in depth, not just the sale

**Examples:**
- Hand-Feeding Schedule, Weaning Timeline, Enrichment Protocol, PBFD Screening, Psittacosis Test
- "[Name]'s Progress: Hand-Feeding Schedule and Where We Are in the Weaning Process."
- "Parrot Care 101: Nutritional Needs for a Young African Grey."
- "What's Included: CITES Permit, DNA Sexing Certificate, Avian Vet Health Certificate, and Hatch Certificate."

---

### H5 — Deep LSI / Long-Tail LSI (Authority Signals)
**Maps to:** Technical and expert terms that establish topical authority on African Grey breeding
**Format:** Specific technical term + context or explanation
**Purpose:** Signals expertise to Google; targets niche searchers who know the terminology

**Examples:**
- "Meeting the Parents: Congo African Grey Genetic and Behavioral Lineage."
- "PBFD Screening Explained: Why It Matters for Your Parrot's Health."
- "Travel Ready: How [Name] Transfers to Your State with Full CITES Documentation."
- "USDA AWA License Explained: What Annual Inspection Means for Buyers."

---

### H6 — NLP / Natural Language Entities (Voice Search)
**Maps to:** Phrases users speak into Siri, Alexa, or type into AI chatbots
**Format:** Natural language question or statement matching real voice queries
**Purpose:** Captures voice search and AI Overview citations; answers "what users actually say"

**Examples:**
- "Is [Name] Good with Kids and Other Pets?"
- "What Is the Total Adoption Fee and Is a Deposit Required?"
- "Ready to Go Home Now: How to Reserve [Name] Today."
- "Can I See [Name] Before I Commit? How Our Virtual Visits Work."

---

## Complete Example: Individual Bird Listing Page

```
H1: Harlow — Congo African Grey for Sale | Male, DNA Sexed | CongoAfricanGreys.com
H2: Searching for a Hand-Raised Congo African Grey in [State]? Meet Your Match.
  H3: How Big Will Harlow Get? Adult Size and Weight for Congo African Greys.
    H4: Current Weight: Where Harlow Is in His Development Timeline.
    H4: What Harlow Eats: His Weaning Diet and Enrichment Schedule.
  H3: Is Harlow DNA Sexed? What That Means for Your New Bird.
    H4: Complete Documentation: CITES Permit, Avian Vet Certificate, and Hatch Certificate.
    H5: PBFD Screening Explained: Why It Matters for Your Parrot's Health.
H2: Why Choose a Congo African Grey from CongoAfricanGreys.com?
  H3: Congo vs Timneh: Which Variant Is Right for Your Household?
  H3: How Harlow Was Raised: Our Hand-Feeding and Socialization Protocol.
    H4: Enrichment and Training Progress: What Harlow Can Do at [X] Weeks.
    H5: USDA AWA Licensed Facility: What Annual Inspection Means for Buyers.
    H6: Is Harlow Already Talking? Here's What to Expect at This Age.
H2: How to Reserve Harlow and Bring Him Home
  H3: The CAG Adoption Process: 5 Simple Steps.
    H4: Deposit, Payment, and What's Included in Harlow's Transfer Package.
    H6: Ready to Go Now: How to Reserve Harlow Today.
```

---

## Heading Audit Checklist

Run this on every page before publishing or after any heading changes:

- [ ] Exactly 1 H1 on the page (grep: `<h1`)
- [ ] H1 contains primary keyword in first 3 words
- [ ] H1 is unique across the site (no other page has the same H1 text)
- [ ] H2s use conversational or question format where applicable
- [ ] H3s cover distinct attribute angles (health, size, documentation, temperament — not repeating)
- [ ] H4+ present on pages over 3,000 words
- [ ] Heading levels are never skipped (no H1 → H3 without H2 in between)
- [ ] No two adjacent headings at the same level with the same keyword
- [ ] No heading text duplicated verbatim in body paragraphs below it
- [ ] Every H2/H3 could stand alone as a realistic Google search query
- [ ] H6 headings (if present) use natural language / voice search phrasing

**Audit command:**
```bash
grep -n "<h[1-6]" site/content/[slug]/index.html | head -50
```

---

## Anti-Patterns (Never Do)

- `<h2>African Grey Parrots</h2>` — too generic, not a search query
- `<h2>Best African Grey Parrots For Sale Near Me In 2025</h2>` — keyword stuffing
- Two `<h1>` tags on the same page
- Using `<h4>` directly under `<h2>` without an `<h3>` in between
- Heading text like "Section 3" or "Introduction" that adds no SEO value
- Repeating the H1 keyword verbatim in every H2
- Using heading levels purely for font size styling — every heading must carry a keyword

---

## Rules

1. **One H1 per page** — non-negotiable
2. **5 variations per core H2** — required for all commercial and location pages
3. **No level skipping** — H1 → H2 → H3 only; never jump levels
4. **Question format preferred for H2/H3** — conversational, voice-search optimized
5. **Audit command first** — always grep heading levels before manual review

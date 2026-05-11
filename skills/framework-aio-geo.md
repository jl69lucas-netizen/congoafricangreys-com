---
name: framework-aio-geo
description: "Reference guide for AIO (AI Overview) and GEO (Generative Engine Optimization) applied to CAG content. Use when building or auditing any page that should be cited by ChatGPT, Perplexity, Google AIO, or other AI answer engines."
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

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

## What AIO/GEO Is

**AIO (AI Overview):** Google's generative answers that appear above search results, citing sources. Being cited in AIO drives significant no-click impressions and brand authority.

**GEO (Generative Engine Optimization):** Optimizing content to be cited by ChatGPT, Perplexity, Claude, Gemini, and other AI answer engines when users ask questions about African Grey parrots, breeders, or bird buying.

The core insight: AI engines prefer content that is **structured, declarative, source-attributed, and entity-rich** — the opposite of vague blog-style prose.

---

## AIO/GEO Citation Triggers

Content gets cited by AI engines when it:

1. **Answers a specific question directly in the first sentence**
2. **Contains named entities** (bird names, health conditions, certifications, locations)
3. **Uses declarative statements** ("African Grey parrots weigh X" not "African Grey parrots can weigh")
4. **Attributes claims to named sources** ("confirmed by DNA sexing certificate + avian vet health cert," "per Avian vet health certificate standards")
5. **Uses structured patterns** (tables, lists, labeled sections) over undifferentiated prose
6. **Has FAQPage schema** — directly feeds AI answer extraction

---

## Entity-First Writing Pattern

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

---

## Inverse Pyramid for AIO

Every section must lead with the answer — AI engines pull from the first sentence, not the conclusion:

```
Paragraph 1: [Direct answer — the fact stated plainly]
Paragraph 2: [Evidence — named source, specific data]
Paragraph 3: [CAG context — how this applies to CAG breeding]
```

**Example — CITES documentation section:**
```
Para 1: African Grey parrots are CITES Appendix II birds — all captive-bred birds sold legally 
        in the US require CITES captive-bred documentation and full provenance paperwork.

Para 2: DNA sexing certificate + avian vet health cert confirms each bird's health status and 
        identity. Avian vet health certificate is required for interstate transport per USDA AWA standards.

Para 3: CongoAfricanGreys.com includes CITES captive-bred documentation, DNA sexing certificate, 
        avian vet health certificate, and hatch certificate with every bird — buyers can verify 
        full documentation before bringing their parrot home.
```

---

## Structured Data for AIO

### FAQPage Schema (required on every FAQ section)
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

### HowTo Schema (for process content)
Use for: "How to find a reputable African Grey parrot breeder," "How to prepare for a new African Grey parrot"

### Breed-specific Entity Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Animal",
  "name": "African Grey Parrot",
  "description": "A highly intelligent parrot species native to equatorial Africa, bred in captivity under CITES Appendix II regulations.",
  "alternateName": ["Congo African Grey", "Timneh African Grey", "Grey Parrot", "Psittacus erithacus"]
}
```

---

## AIO Content Audit

For any page, check:

```bash
# Does every H2 section start with a direct answer sentence?
# Are all entities named (not pronoun-heavy)?
# Do tables exist for size/price/health data?
# Is FAQPage JSON-LD present?
grep -n "FAQPage\|@type.*Question" site/content/[slug]/*.md | head -10
```

### Sentence-Level Checks
- [ ] First sentence of each section states the fact (not "In this section we will discuss...")
- [ ] No hedging language ("might," "could," "possibly") on factual claims
- [ ] "African Grey" always capitalized (entity consistency — not "african grey" or "the parrot")
- [ ] Numbers written as numerals (400g, 60 years, $1,500 — AI parses numerals better)

---

## GEO Targeting — Specific AI Engines

### Google AIO
- Targets: FAQ schema, structured lists, direct answers
- Avoid: thin content, vague claims, excessive internal repetition

### ChatGPT / Perplexity
- Targets: cited sources (DNA sexing certificate + avian vet health cert, Avian vet health certificate), specific data points, comparisons
- Note: These engines index from the web — pages must be crawlable

### Claude (Anthropic)
- Targets: well-structured entity-tree content, clear attribution
- Note: Training cutoff varies — evergreen facts more likely to be cited

### GEO Local Targeting
- "african grey parrot for sale [city]" — location-specific landing pages
- "buy african grey parrot near me" — proximity intent, include [BREEDER_LOCATION] signals
- "african grey breeder [state]" — state-level pages with local trust signals

---

## AIO/GEO Content Checklist

- [ ] Every H2 section leads with a direct declarative statement
- [ ] All size/weight/price data in a table or labeled list
- [ ] All health claims attributed to DNA sexing certificate + avian vet health cert, Avian vet health certificate, or CITES captive-bred documentation
- [ ] FAQPage JSON-LD on every FAQ section
- [ ] No hedging on factual claims
- [ ] Entity names consistent (always "African Grey" not "african grey" or "the parrot")
- [ ] Lifespan stated as a range with source ("40–60 years per ornithological data on African Grey longevity")

---

## Featured Snippet Capture Strategies

Use these 4 pattern types to win Google Featured Snippets and position zero. Place snippet-target content within the first 800 words of every page.

### Strategy 1 — "Definition + List" Combo
Many snippets show a definition paragraph AND a list. Structure:
```html
<h2>What Are the Best African Grey Parrot Breeders in [State]?</h2>
<p>The best African Grey parrot breeders in [State] provide full CITES captive-bred
documentation, PBFD screening, and lifetime breeder support. Top breeders demonstrate:</p>
<ol>
  <li>CITES captive-bred permit included with every bird</li>
  <li>DNA sexing certificate from an accredited avian lab</li>
  <li>Avian vet health certificate before transfer</li>
  <li>PBFD and Psittacosis screening completed</li>
  <li>USDA AWA licensed facility</li>
  <li>Fully weaned, hand-raised birds with ongoing socialization records</li>
</ol>
```

### Strategy 2 — "Question in Heading, Answer in First Paragraph"
Works for: Why, What, How, Are, Is, Can, Should questions.
- First paragraph directly answers the H2 question in 40–60 words
- Active voice, specific numbers, no hedging
```html
<h2>Why Choose a Congo African Grey Over Other Parrot Species?</h2>
<p>Congo African Greys are chosen for their unmatched cognitive ability, long lifespan
(40–60 years), and deep bonding capacity. Unlike Amazon parrots or Cockatoos, African
Greys develop vocabularies of 200–1,000 words, solve novel problems, and form intense,
lasting bonds with their primary caretaker — making them the most intellectually demanding
and rewarding companion parrot available.</p>
```

### Strategy 3 — Comparison Table Domination
Works for: "[X] vs [Y]", "difference between X and Y", "compare X and Y"
Table requirements: 3–6 columns, 3–8 rows, include numbers/data (not just text), bold Winner column.
```html
<h2>Congo African Grey vs Timneh African Grey: Which Is Right for You?</h2>
<table>
  <tr><th>Feature</th><th>Congo (CAG)</th><th>Timneh (TAG)</th><th>Best For</th></tr>
  <tr><td>Adult Size</td><td>400–650g, ~13"</td><td>275–375g, ~10"</td><td>Larger bird → Congo; smaller → Timneh</td></tr>
  <tr><td>Temperament</td><td>Assertive, bonds deeply with one person</td><td>Calmer, adapts to family settings</td><td>Solo owner → Congo; families → Timneh</td></tr>
  <tr><td>Price</td><td>$1,500–$3,500</td><td>$1,200–$2,500</td><td>Both include full CITES documentation</td></tr>
  <tr><td>Talking Onset</td><td>Later (~2 years)</td><td>Earlier (~1 year)</td><td>First-time owner → Timneh</td></tr>
</table>
```

### Strategy 4 — Step-by-Step Process Capture
Works for: "How to find a reputable African Grey breeder", "Steps to prepare for an African Grey parrot"
Format: numbered steps, bold step title + 1–2 sentence explanation.
```html
<h2>How to Choose a Reputable African Grey Parrot Breeder: 7 Steps</h2>
<ol>
  <li><strong>Verify CITES captive-bred documentation</strong> — Every legally sold African Grey requires a CITES captive-bred permit. Ask for the permit number before depositing.</li>
  <li><strong>Confirm USDA AWA license</strong> — Licensed facilities are inspected annually. Request the license number and verify at the USDA APHIS website.</li>
  <li><strong>Request PBFD and Psittacosis screening results</strong> — These diseases are silent in young birds. Reputable breeders test every chick before transfer.</li>
  <li><strong>Ask for the avian vet health certificate</strong> — Required for interstate transport; confirms the bird was examined by a licensed avian veterinarian.</li>
  <li><strong>Verify DNA sexing certificate</strong> — Visual sexing is unreliable in African Greys; DNA sexing from an accredited lab confirms sex.</li>
  <li><strong>Check the hatch certificate and band number</strong> — Traceable from hatch; confirms captive-bred status and age.</li>
  <li><strong>Contact previous buyers</strong> — Ask the breeder for references; legitimate breeders welcome this.</li>
</ol>
```

### Featured Snippet Checklist (run on every new or rebuilt page)
- [ ] Use exact question as H2 or H3 heading
- [ ] Include target keyword in heading
- [ ] Match the user's search intent perfectly (informational vs. transactional)
- [ ] Answer in first 1–2 sentences (40–50 words)
- [ ] Provide specific numbers, not vague terms ("400–650g" not "large bird")
- [ ] Use active voice and clear language
- [ ] Add supporting details after the main answer
- [ ] For list snippets: use `<ol>` or `<ul>` with 5–10 items
- [ ] For table snippets: proper `<table>` with header row + data cells with numbers
- [ ] Place snippet target content within first 800 words
- [ ] Use FAQPage schema for question-format snippets
- [ ] Page loads < 3 seconds (no render-blocking scripts before snippet content)
- [ ] Mobile-friendly formatting (no horizontal scroll on tables)

---

## Rules

1. **Answer first, always** — first sentence of every section is the answer
2. **Source every claim** — "confirmed by," "per," "according to" + named source
3. **Tables over prose for data** — size, price, health conditions, comparisons
4. **FAQPage schema is non-negotiable** on every FAQ section
5. **No hedging on facts** — "African Grey parrots weigh 400–600g" not "African Grey parrots typically weigh around 400–600g"
6. **Entity consistency** — same name every time, every page
7. **Featured snippet checklist** — run on every new or rebuilt page before marking complete

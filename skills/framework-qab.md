---
name: framework-qab
description: "Reference guide for the QAB framework applied to CAG FAQ sections, price pages, and comparison content. Use whenever writing FAQ items, cost breakdowns, or any content that must answer a buyer's question AND connect the answer to a personal benefit."
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

## What QAB Is

QAB is CAG's primary framework for FAQ sections, pricing content, and any "question-and-answer" format. It extends a basic Q&A with a third step — the Benefit — which converts informational readers into buyers.

```
Q — Question:  The exact question the buyer is asking (in their language)
A — Answer:    The direct, specific, factual answer (Inverse Pyramid — answer first)
B — Benefit:   Why this answer matters to the reader's specific situation
```

Without the Benefit, you have a FAQ. With the Benefit, you have a conversion tool.

---

## QAB vs Basic Q&A

```
BASIC Q&A:
Q: How much does a Congo African Grey parrot cost?
A: Congo African Grey parrots typically range from $1,500 to $3,500.

QAB:
Q: How much does a Congo African Grey parrot cost from a reputable breeder?
A: Congo African Greys from CongoAfricanGreys.com are priced at $1,500–$3,500. This includes 
   CITES captive-bred documentation, DNA sexing certificate, avian vet health certificate, 
   hatch certificate, and a health guarantee. A deposit holds your bird.
B: Transparent pricing means no surprise documentation fees after you've already bonded with 
   your bird — and no "paperwork add-on" charges at delivery.
```

---

## Question Writing Rules

**Write questions in the buyer's exact language:**
- Use "how much" not "what is the price"
- Use "near me" where that's how buyers search
- Use "reputable breeder" because that's the qualifier buyers use
- Use "is an African Grey parrot right for me" not "African Grey parrot suitability assessment"

**Question sources (where real buyer language lives):**
- Google People Also Ask for the primary keyword
- Google autocomplete suggestions
- GSC Queries.csv — real queries driving impressions
- Reddit, Quora, Facebook groups (what buyers actually ask)

**Question length:**
- 8–15 words optimal
- Conversational, not formal
- One topic per question (not "how much does an African Grey parrot cost and what's included")

---

## Answer Writing Rules

**Lead with the answer, not with context:**
```
Bad:  "When considering the cost of an African Grey parrot, there are several factors to consider..."
Good: "African Grey parrots from CongoAfricanGreys.com cost $1,500–$3,500 (CAG) / $1,200–$2,500 (TAG) depending on variant."
```

**Be specific — use real numbers:**
```
Bad:  "Cage costs can vary but are generally affordable."
Good: "Expect $300–$600 for an appropriate cage — a minimum 36"x24"x48" for an African Grey."
```

**Source the answer:**
- Prices: from `docs/reference/domain-knowledge.md` — confirmed current
- Costs: from CAG pricing data (Phase 2: `data/price-matrix.json`)
- Health: per DNA sexing certificate / avian vet health cert
- Species facts: per ornithological data / USFWS CITES Appendix II documentation

---

## Benefit Writing Rules

The Benefit is not a repeat of the answer. It's the emotional or practical payoff:

```
Bad Benefit:  "This is why CongoAfricanGreys.com is a great choice." (marketing speak)
Good Benefit: "Knowing your bird's complete documentation before delivery means your first 
               avian vet visit is a celebration, not a discovery of missing paperwork."
```

**Benefit types:**
- **Fear-removal:** "...so you never have to worry about hidden fees"
- **Outcome clarity:** "...which means your bird arrives calm and healthy"
- **Decision confidence:** "...so you can compare breeders with the same standard"
- **Financial:** "...saving you $800–$2,000 compared to first-year vet costs for a pet-store bird"

---

## QAB Template (HTML ready)

```html
<details class="cag-faq-item">
  <summary class="cag-faq-question">
    [Question text in buyer's language?]
  </summary>
  <div class="cag-faq-answer">
    <p>[Direct answer — specific, sourced, no hedging]</p>
    <p class="cag-faq-benefit">[Benefit — why this matters to the reader]</p>
  </div>
</details>
```

---

## QAB for Price Pages

On cost pages, QAB structure is required for every line item:

```
Q: What's included in the African Grey parrot price?
A: Every CongoAfricanGreys.com African Grey parrot includes: CITES captive-bred documentation, 
   DNA sexing certificate, avian vet health certificate, hatch certificate + band number, 
   starter kit (food, perch, toy), and a health guarantee. Price: $1,500–$3,500 (CAG) / $1,200–$2,500 (TAG) by variant.
B: Unlike importers that add documentation fees after purchase, CongoAfricanGreys.com pricing 
   is all-inclusive — what you see is what you pay.
```

---

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
- How does IATA-compliant bird shipping work?
- Can I visit in person to meet the bird before purchasing?
- What if the bird gets sick after I bring them home?

### Species & Variants
- What's the difference between a Congo and Timneh African Grey?
- Do African Grey parrots talk?
- How long do African Grey parrots live?
- Are African Greys good for beginners?
- How much space does an African Grey need?

---

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

---

## Rules

1. **Benefit is required** — a Q&A without a Benefit is incomplete QAB
2. **Questions in buyer's language** — not marketing language
3. **Answer leads with the fact** — Inverse Pyramid inside the A
4. **Numbers from data files** — read `docs/reference/domain-knowledge.md` and Phase 2 `data/price-matrix.json`
5. **FAQPage JSON-LD required** — every QAB FAQ section needs schema
6. **No generic benefits** — "this is why CongoAfricanGreys.com is great" is not a benefit

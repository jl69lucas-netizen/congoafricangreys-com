---
name: cag-entity-agent
description: Entity management skill for CAG — 100+ entity catalog across parrot variant, health, credential, location, and pricing categories. Uses Entity-Benefit-Purpose (EBP) framework for AI/AIO optimization. Manages schema injection and entity coverage audits. Read when writing or auditing any CAG page for entity depth.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

---

## Entity-Benefit-Purpose (EBP) Framework

For every entity mention on an MFS page:
1. **Entity** — name the thing: "DNA sexing certificate testing"
2. **Benefit** — what it does: "screens 250+ genetic conditions before pairing"
3. **Purpose** — why it matters to buyer: "so you know your puppy won't develop a preventable inherited condition"

**Without EBP (weak):** "We use DNA sexing."
**With EBP (strong):** "DNA sexing determines the bird's biological sex with 100% accuracy — so you know what you're getting and can plan breeding responsibly if desired."

---

## Complete Entity Catalog

### Category 1 — Breed Entities

| Primary Entity | Variations | Where to Use |
|---------------|-----------|-------------|
| African Grey parrot | African Grey, parrot, captive-bred | H1, H2, opening paragraphs, CTAs |
| Congo African Grey | Congo, CAG, larger African Grey | Variant sections, H2, species guide |
| Timneh African Grey | TAG, Timneh, smaller African Grey | Variant sections, H2, species guide |
| Psittacus erithacus | Scientific name, avian nomenclature | Species guide, scientific sections |
| CITES Appendix II | CITES A-II, protected species | Credentials, legal pages |
| Captive-bred | Domestically bred, bred in captivity | Trust bar, credentials |
| Hand-raised | Hand-fed, socialized, behavioral training | Care sections, about page |
| Lifetime breeder support | Ongoing breeder relationship, lifetime advisory | Trust, FAQ |

### Category 2 — Health & Credential Entities

| Primary Entity | Variations | Where to Use |
|---------------|-----------|-------------|
| DNA sexing | DNA sexing test, avian genetic testing | Health sections, credentials, FAQ |
| Avian vet health certificate | Avian veterinarian certification, health exam | Health sections, trust bar |
| USDA license | USDA-licensed breeder, USDA inspection | Trust bar, about page |
| CITES documentation | CITES permit, captive-bred certificate | Credentials, legal compliance |
| Behavioral socialization | Hand-raised, taming, training | Care sections, about |
| Nutritional support | Species-appropriate diet, parrot nutrition | Care guide, FAQ |
| Lifetime advisory | Ongoing breeder mentorship, lifetime support | Trust, FAQ |
| Avian welfare standards | Species welfare, ethical breeding | Trust, credentials |

### Category 3 — Location Entities

| Primary Entity | Variations | Where to Use |
|---------------|-----------|-------------|
| [BREEDER_LOCATION] | [LOCATION], [REGION] | About, location, schema |
| CongoAfricanGreys.com | CAG, CAG breeder, breeding program | Brand mentions, footer, schema |
| [BREEDER_NAME] | Breeder, owner, founder | About, testimonials, Person schema |
| IATA-compliant shipping | IATA certified handler, air transport | Location pages, hero |
| Nationwide shipping | Continental US shipping, interstate transport | Hero, location hub |

### Category 4 — Pricing Entities

| Primary Entity | Variations | Where to Use |
|---------------|-----------|-------------|
| African Grey parrot price | African Grey parrot cost, African Grey price range | Price page, FAQ |
| $1,500–$3,500 | fifteen hundred to thirty-five hundred | Price sections, Congo variant |
| $1,200–$2,500 | twelve hundred to twenty-five hundred | Price sections, Timneh variant |
| Transparent pricing | no hidden fees, all-inclusive cost | Trust, FAQ |

### Category 5 — Buyer/Family Entities

| Primary Entity | Variations | Where to Use |
|---------------|-----------|-------------|
| Long-lived companion | 40-year lifespan, lifelong commitment | Hero, care section |
| 500+ families | Five hundred families, satisfied owners | Social proof |
| 15+ years experience | 15+ years breeding, established program | Credentials, about |
| Experienced bird owners | parrot enthusiasts, repeat buyers | Target audience, FAQ |

---

## Schema Management — Native Protocol

Use the native approach below — it handles multiple schema blocks correctly, preserving all existing schemas.

### View All Schema Blocks
```bash
grep -n "application/ld+json" site/content/[slug]/index.html
```

### Extract Schema by Index
```python
import json, re
html = open('site/content/[slug]/index.html').read()
schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
for i, s in enumerate(schemas):
    parsed = json.loads(s)
    print(f"Schema {i}: @type={parsed.get('@type')}")
```

### Build FAQ Schema from Actual Accordion (not raw text)
```python
import re, json
html = open('site/content/[slug]/index.html').read()
faq_items = re.findall(
    r'<summary[^>]*class="cag-faq-question"[^>]*>(.*?)</summary>.*?itemprop="text"[^>]*>(.*?)</div>',
    html, re.DOTALL
)
schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
        "@type": "Question",
        "name": re.sub('<[^>]+>', '', q).strip(),
        "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a).strip()}
    } for q, a in faq_items]
}
print(json.dumps(schema, indent=2))
```

---

## Entity Coverage Audit

```bash
# Check entity presence on any page
for entity in "African Grey parrot" "Congo African Grey" "Timneh African Grey" "DNA sexing" "avian vet" "CITES" "lifetime support" "captive-bred"; do
  count=$(grep -oi "$entity" site/content/[slug]/index.html | wc -l)
  echo "$count × $entity"
done
```

### Entity Density Targets

| Page Type | Must-Have Entities | Target Mentions Each |
|-----------|-------------------|---------------------|
| Homepage | African Grey parrot, DNA, guarantee, hypoallergenic, Omaha | 5–8 |
| Location page | African Grey parrot, [state], flight nanny, guarantee | 3–5 |
| Variant guide | Congo African Grey, Timneh African Grey, DNA, CITES, avian vet | 6–10 |
| Comparison page | Both breed entities + 3–5 differentiators | 4–6 |
| Price page | Price entities, guarantee, DNA, all-inclusive | 5–8 |

---

## Rules

1. **EBP on every entity mention** — entity without benefit is a wasted mention
2. **Native schema management** — use grep/python approach directly (handles multiple schema blocks correctly)
3. **Extract FAQ schema from `<details>/<summary>`** — not raw page HTML
4. **Density cap** — no single entity above 2% of total word count
5. **Location entities on all location pages** — state name, city names, airport codes always present
6. **Credential entities in first 300 words** — DNA sexing, avian vet, USDA appear early
7. **Cross-reference price-matrix.json** — all pricing entities match the data file

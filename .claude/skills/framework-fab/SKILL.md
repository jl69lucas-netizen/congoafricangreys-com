---
name: framework-fab
description: "Reference guide for the FAB (Features → Advantages → Benefits) framework applied to CAG pages. Use when writing spec-bearing content — bird listing details, pricing what's-included rows, cage/diet/setup recommendations, documentation stacks, shipping tiers — so a raw fact never ships without its advantage and its owner-benefit. Also the comparison-row framework (advantage comparison vs competitors/other species)."
tools: [Read, Write, Bash]
---

## Golden Rule
> **Link-First (ALWAYS):** anchors at the START of the sentence — never mid-sentence, never at the end.
> Use Claude Code and Playwright CLI to solve problems first.
> **Confidence Gate:** ≥97% before writing any site file.

---

## CAG Project Context
> **Site:** CongoAfricanGreys.com — captive-bred African Grey parrot breeder
> **Variants:** Congo African Grey (CAG, $1,500–$3,500) · Timneh African Grey (TAG, $1,200–$2,500)
> **CITES:** Appendix I; all birds captive-bred in the USA with full documentation.
> **Facts source:** `data/price-matrix.json` · `data/financial-entities.json` · `data/clutch-inventory.json` · Verified-Claim Ledger — never invent a spec.

---

## What FAB Is

FAB forbids naked facts. Every feature gets translated twice — into what it does better (advantage) and what that means for the buyer's life (benefit).

```
F — Feature:   The verifiable fact/spec. ("Every chick ships with a PCR DNA-sexing certificate.")
A — Advantage: What that does better than the alternative. ("Visual sexing of Greys is folklore — males and females look identical; PCR is the only reliable method.")
B — Benefit:   What it means for THIS buyer. ("You know on day one whether you're naming a Charlie or a Chloe — and hormonal-season behavior never blindsides you.")
```

**Related EBP note:** CAG's `framework-ebp` (Evidence → Benefit → Proof) is the credibility-first cousin; the entity catalog's EBP (Entity-Benefit-Purpose) is the entity-SEO variant. FAB is the *spec-translation* tool — see `skills/framework-library.md §EBP disambiguation`.

## When to Use on CAG

| Use FAB | Don't use FAB |
|---|---|
| Bird listing spec blocks (weaning, band, documentation) | Pain-led sections → `framework-pas` |
| Pricing "what's included" rows | Story/trust sections → `framework-eeat` / H-S-S |
| Cage/diet/setup product recommendations | FAQ answers → `framework-qab` |
| Comparison-table rows + advantage columns (X vs Y pages) | Cold-traffic heroes → `framework-aida` |
| Shipping tiers ($185 airport / $350 home — advantage + benefit per tier) | |

## CAG Worked Example (shipping tier row)

- **F:** "Home delivery, $350 — a dedicated ground courier, IATA LAR-compliant carrier, door-to-door."
- **A:** "Unlike airport cargo pickup, your bird never sits in a cargo facility and you never drive hours to a hub."
- **B:** "Your Grey steps out of the carrier into its new living room — one calm transition instead of three stressful ones."

## The Advantage-Comparison Variant (comparison pages)

On [X] vs [Y] pages, the A beat carries the row: state what our option does better *than the named alternative*, grounded in fetched competitor/species data — `NOT FETCHED` data is never invented. Pair with the honesty moat: when the alternative genuinely wins a row, say so (that's the trust play that outranks fluff).

## Common Mistakes
- **Shipping the F without the B** — a spec list with no translation is commodity content; the Generic-Slayer filter will flag it.
- **Fake advantages** — "rust-proof stainless" only if the recommended product actually is; specs trace to real data files or reviewed products.
- **Benefit inflation** — the B beat stays inside verified claims; no lifespan/health promises beyond the ledger.
- **FAB-ing every paragraph** — it's for spec-bearing content; narrative sections use their own frameworks.

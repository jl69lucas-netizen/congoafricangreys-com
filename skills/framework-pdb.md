---
name: framework-pdb
description: "Reference guide for the PDB framework applied to CAG buyer-fear content, CITES safety pages, and high-stakes decision pages. Use when the reader arrives with a specific pain — a scam, a CITES documentation fear, a wild-caught suspicion — and needs content that names their pain before offering the solution."
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
> **Buyer fears (ranked):** Scam/fraud · Sick bird · CITES documentation gaps · Wild-caught suspicion · Post-sale abandonment · Cost uncertainty
> **Content root:** `site/content/` | **Sessions:** `sessions/`
> **Confidence Gate:** ≥97% before writing any site file

## What PDB Is

PDB is a variant of PAS (Problem-Agitate-Solution) calibrated for CAG's specific buyer fears. It works by naming the reader's pain with unusual specificity — making them feel understood — before presenting the solution. Unlike generic PAS, PDB starts with a brief (a dossier of the reader's fears) rather than a general problem statement.

```
P — Pain:    Name the specific fear. Not "it's hard to find a good breeder" 
             but "you've seen the Facebook posts about parrots that arrived sick."
D — Depth:   Go deeper into why this fear is rational and specific.
B — Brief:   Summarize what this reader needs — then show CongoAfricanGreys.com provides it.
```

---

## CAG Buyer Fear Stack

These are the ranked fears African Grey buyers arrive with (in order of frequency):

1. **Scam fear** — "Is this breeder real or will I lose my deposit to a scammer?"
2. **CITES/legal fear** — "Is this bird legally documented? Could CBP seize it after I bring it home?"
3. **Wild-caught suspicion** — "Is this bird captive-bred or was it illegally imported?"
4. **Sick bird fear** — "What if the bird has PBFD or another disease I won't discover for months?"
5. **Support abandonment fear** — "Will the breeder answer the phone after the money is sent?"
6. **Cost uncertainty fear** — "What's the true total cost — not just the purchase price?"

---

## PDB Application by Page

| Page | Primary Pain | PDB Hook |
|------|-------------|---------|
| `/where-to-buy-african-greys-near-me/` | Scam fear | "You've seen the Facebook posts about parrot scams. Here's how to know you're not in one." |
| `/how-to-avoid-african-grey-parrot-scams/` | Scam + CITES fear | "The documentation looked real. It wasn't. Here's how to verify before you send anything." |
| `/african-grey-parrot-price/` | Cost uncertainty | "The purchase price is the smallest number in this equation." |
| State pages | Distance/trust | "You're trusting a breeder you've never met with $1,500+. Here's how to verify them." |
| `/african-grey-parrot-for-sale-*/` | Wild-caught suspicion | "Every 'cheap african grey' site you've seen — here's what they're not showing you." |

---

## PDB Structure

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

---

## PDB vs BAB — When to Use Which

| Scenario | Use PDB | Use BAB |
|----------|---------|---------|
| Reader has a named fear before landing on page | ✅ | |
| Reader had a bad experience (scam, sick bird) | ✅ | |
| Reader is comparing options and needs contrast | | ✅ |
| Reader needs to see transformation | | ✅ |
| Page is scam-prevention focused | ✅ | |
| Page is adoption/rescue reframe | | ✅ |

PDB validates the fear first. BAB shows the contrast after. On the same page, PDB often comes before BAB — validate the fear, then show the transformation.

---

## PDB Writing Rules

### Pain Specificity
```
Weak Pain:  "Finding a reputable breeder can be challenging."
Strong Pain: "The breeder had 47 five-star reviews, a USDA certificate on their website, 
              and a no-questions-asked refund policy. Three days after the deposit, 
              the website disappeared."
```

### Depth Validation
- Never tell the reader their fear is irrational
- Cite real data where available ("parrot scam losses topped $X last year — FTC data")
- Use "your fear isn't [X], it's [Y]" framing — reframes the emotion as intelligence

### Brief Precision
- The Brief is a compact requirements list — what this reader needs
- Then CongoAfricanGreys.com checks every box on that list
- Brief is not a feature dump — it's a needs summary

---

## Fear-to-Solution Map (ready reference)

| Fear | Depth Fact | CAG Solution |
|------|-----------|-------------|
| Scam | Parrot fraud is common on Craigslist/FB Marketplace | USDA AWA license, traceable payment, [YEAR]+ history |
| CITES/legal | CITES forgery exists; CBP can seize birds post-purchase | CITES permit verifiable at usfws.gov before deposit |
| Wild-caught | "Captive-bred" is claimed freely, rarely documented | Hatch certificate + band number per bird |
| Sick bird | PBFD and other conditions can be latent for months | Avian vet health certificate, health guarantee |
| Abandonment | Most bird sellers have no post-sale support | `[BREEDER_NAME]` phone/email on every page (name: see `docs/reference/domain-knowledge.md`) |
| Hidden costs | Vet costs, cage, shipping add up to $500–$1,500+ | All-in cost guide published openly |

---

## Rules

1. **Pain must be specific** — generic fears don't create the "how do they know that?" response
2. **Depth validates, never dismisses** — the fear is rational, not paranoid
3. **Brief is a needs summary** — not a feature list
4. **CongoAfricanGreys.com must check every Brief item** — don't promise what you can't deliver
5. **Cite real data in Depth** — FTC, avian vet / exotic bird vet, or CAG internal data
6. **CTA after Brief** — PDB without an action path is just empathy

---
name: framework-ebp
description: "Reference guide for the EBP framework applied to CAG breeder credibility sections, CITES documentation explanations, and any content that must prove a claim with named evidence. Use when building trust sections that must survive skeptical scrutiny."
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

## What EBP Is

EBP is the framework for building credibility through evidence — not assertion. Every claim must be followed immediately by the named evidence that supports it. No claim stands alone.

```
E — Evidence:  Name the specific proof source
B — Baseline:  State what the evidence proves
P — Profile:   Show how CAG meets or exceeds the baseline
```

The pattern: Claim → Evidence → What it means for the buyer.

---

## Why CAG Needs EBP

CAG operates in a trust-scarce market. African Grey buyers have been burned by:
- Sellers who say "CITES documented" with forged paperwork
- Facebook Marketplace listings with stock photos and CashApp payment requests
- Sites that say "captive-bred" with no documentation to show
- "Cheap african grey" sites with no USDA license, no vet cert, no recourse

EBP converts vague claims into verifiable proof. "All our birds are documented" becomes "CITES Appendix II captive-bred permit #[NUMBER] — verifiable at usfws.gov."

---

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

---

## EBP Section Structure

### Basic EBP Block (for inline credibility)
```
[Claim]: African Greys from CongoAfricanGreys.com are fully documented under CITES Appendix II.
[Evidence]: CITES captive-bred permit issued under our USDA AWA license. Permit number 
            available before any deposit is sent. Verifiable independently at usfws.gov.
[Profile]: Every bird ships with the CITES permit, DNA sexing certificate, avian vet health 
           certificate, and hatch certificate. No buyer has ever had a bird seized by CBP.
```

### Full EBP Section (for health/trust pages)
```html
<div class="cag-ebp-block">
  <h3>Documentation — What "CITES Documented" Actually Means at CongoAfricanGreys.com</h3>
  
  <div class="cag-ebp-item">
    <strong>CITES Appendix II Captive-Bred Permit</strong>
    <p>Every African Grey parrot from CongoAfricanGreys.com is captive-bred under a CITES 
       Appendix II captive-bred permit. This permit is issued by the U.S. Fish &amp; Wildlife 
       Service and is required by federal law for any legal sale of African Greys. 
       Permit number available before any deposit is sent.</p>
    <p class="cag-evidence-note">Evidence: CITES captive-bred permit included with every bird. 
       Verifiable independently at usfws.gov.</p>
  </div>
  
  <div class="cag-ebp-item">
    <strong>Avian Vet Health Certificate</strong>
    <p>Parent birds and all hatchlings receive avian vet health certificates from a 
       licensed avian veterinarian. This is the same standard required for interstate 
       transport and international export of captive birds.</p>
    <p class="cag-evidence-note">Evidence: Avian vet health certificate — [VET_NAME], 
       certificate included with bird.</p>
  </div>
</div>
```

---

## EBP for Pricing Claims

Pricing transparency is also evidence-based:

```
Claim:    "CongoAfricanGreys.com African Greys cost less than exotic pet store birds over a lifetime."
Evidence: First-year vet costs for health-certified birds average $300–$500 
          (routine care only). First-year vet costs for undocumented birds 
          average $1,200–$2,800 (illness + documentation issues).
          Source: CAG owner survey data.
Profile:  The $1,500–$3,500 (CAG) / $1,200–$2,500 (TAG) price + $300–$500 vet = documented, 
          legally protected bird with full paperwork from day one.
```

---

## EBP vs Assertion — Side-by-Side

| Assertion (weak) | EBP (strong) |
|-----------------|-------------|
| "All our birds are legal" | "CITES Appendix II captive-bred permit — verifiable at usfws.gov" |
| "Our birds are health tested" | "Avian vet certificate — [VET_NAME], certificate included" |
| "DNA sexed" | "DNA sexing certificate — [LAB_NAME], included with bird" |
| "Hand-raised from hatch" | "Hand-feeding log from day 1 — available on request" |
| "We've been breeding for X years" | "USDA AWA license #[NUMBER], breeding since [YEAR]" |
| "Health guaranteed" | "Health guarantee — full terms at [link]" |

---

## EBP Audit

```bash
# Find pages with unverified claims
grep -n "we guarantee\|health tested\|best\|top\|premier\|reputable\|captive-bred" site/content/[slug]/*.md | head -20
# For each match: is there a named evidence source within 2 sentences?
```

---

## Rules

1. **Every claim gets evidence** — no claim stands without a named source
2. **Name the source specifically** — "CITES captive-bred permit" not "documentation"
3. **Baseline matters** — show what the evidence standard means (USFWS permit, USDA AWA license)
4. **Profile shows CAG exceeding baseline** — don't just meet the standard, show how CAG leads
5. **Evidence must be verifiable** — USDA AWA license number, CITES permit number, avian vet certificate
6. **No unverifiable superlatives** — "best," "top," "premier" require external evidence to cite

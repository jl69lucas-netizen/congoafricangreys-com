---
name: framework-eeat
description: "Reference guide for Google's E-E-A-T framework applied to CAG content. Use when auditing or building any page that must signal credibility to Google's quality raters and AI systems. Covers on-page signals, schema, CITES compliance framing, and author attribution."
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

## What E-E-A-T Is

E-E-A-T is Google's quality framework used by human quality raters and increasingly baked into ranking signals. For YMYL (Your Money or Your Life) topics — including parrot purchases — E-E-A-T signals are heavily weighted.

```
E — Experience:      First-hand experience with the topic
E — Expertise:       Subject matter knowledge and credentials
A — Authoritativeness: Recognition by peers and industry
T — Trustworthiness:  Accuracy, transparency, and safety
```

CongoAfricanGreys.com is a YMYL site (buying a living animal is a significant decision). Every page must signal all four dimensions.

---

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

---

## On-Page E-E-A-T Implementation

### Author Attribution
Every content-heavy page should name the source of expertise:

```html
<div class="cag-author-block">
  <p class="cag-body">
    <strong>Written by [BREEDER_NAME],</strong> USDA AWA-licensed African Grey breeder 
    in [BREEDER_LOCATION]. Specializing in captive-bred Congo and Timneh African Greys 
    with full CITES documentation.
  </p>
</div>
```

### Experience Signals in Body Copy
Replace: "African Grey parrots are intelligent birds."
With: "In our years of breeding, we've placed African Grey parrots with hundreds of families — and the hand-feeding and socialization protocol we've developed from hatch consistently produces birds that are confident, bonded, and ready for their new homes."

### Schema for E-E-A-T

**Person schema** (for [BREEDER_NAME]):
// Requires @context and <script type="application/ld+json"> wrapper
```json
{
  "@type": "Person",
  "name": "[BREEDER_NAME]",
  "jobTitle": "USDA AWA Licensed African Grey Breeder",
  "worksFor": { "@type": "Organization", "name": "CongoAfricanGreys.com" },
  "address": { "@type": "PostalAddress", "addressLocality": "[BREEDER_LOCATION]" }
}
```

**LocalBusiness schema** (in footer, on contact page):
// Requires @context and <script type="application/ld+json"> wrapper
```json
{
  "@type": "LocalBusiness",
  "name": "CongoAfricanGreys.com",
  "founder": "[BREEDER_NAME]",
  "address": { "addressLocality": "[BREEDER_LOCATION]" },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[RATING]",
    "reviewCount": "[COUNT]"
  }
}
```

---

## CITES E-E-A-T — The CAG Differentiator

African Greys are CITES Appendix II — the same international treaty that governs ivory and rhino horn trade. This makes CITES compliance documentation the single strongest E-E-A-T signal available to CAG, because:

1. **No competitor uses it.** The gap matrix shows only birdsforsales.com mentions USDA + CITES. Every other Tier 1 breeder is silent.
2. **It is externally verifiable.** CITES documentation is issued by the USDA/USFWS — not self-reported.
3. **It addresses the buyer's deepest fear.** Wild-caught bird suspicion and CBP seizure risk are uniquely parrot fears with no equivalent in the companion-dog market.

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

---

## E-E-A-T Audit Checklist

For any page audit, score each dimension 1–5 (total range: 4–20):

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

---

## Common E-E-A-T Failures at CAG

| Failure | Fix |
|---------|-----|
| "All our birds are legal" (vague) | "CITES Appendix II captive-bred docs — permit number available" |
| "Health tested" (unverified) | "Avian vet cert — [VET_NAME], certificate included with bird" |
| No author name on content | Add [BREEDER_NAME] author block |
| Prices hidden ("contact us") | Show price ranges openly ($1,500–$3,500 CAG, $1,200–$2,500 TAG) |
| Generic testimonials | Name + location + specific outcome |
| "Our birds are captive-bred" | "CITES captive-bred documentation — verifiable with USFWS" |

---

## Rules

1. **Every claim needs a source** — DNA sexing certificate, avian vet health certificate, CITES captive-bred documentation, or CAG internal data
2. **First-person experience in every major section** — not just the About page
3. **Schema required** — Person and LocalBusiness on every key page
4. **No unverifiable superlatives** — "best" requires external evidence
5. **Contact info must be real and visible** — not just a form

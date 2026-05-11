---
name: framework-bab
description: "Reference guide for the BAB framework applied to CAG buyer-fear content, scam-prevention sections, and CITES safety content. Use when the reader needs to see a clear contrast between their current risky situation and the documented outcome — and CAG as the bridge."
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

## What BAB Is

BAB is a contrast framework. It shows the reader where they are now (Before), where they want to be (After), and presents CongoAfricanGreys.com as the Bridge between those two states. It works best when the reader is in pain — a bad experience with sellers, a failed purchase, a fear of being scammed.

```
B — Before:  Name their current reality. The pain, the fear, the frustration.
A — After:   Show the transformed future. Specific, emotional, concrete.
B — Bridge:  CAG as the path from Before to After.
```

---

## When to Use BAB at CAG

| Page / Section | BAB Application |
|----------------|----------------|
| Scam-prevention sections | Before: CashApp seller risk → After: CITES-documented purchase |
| CITES safety sections | Before: undocumented bird risk → After: full CBP-compliant documentation |
| Health guarantee section | Before: sick bird fear → After: avian vet cert + health guarantee |
| First-time owner sections | Before: overwhelmed by complexity → After: guided and supported |
| `/how-to-avoid-african-grey-parrot-scams/` | Before: online scam → After: verified breeder checklist |

**Don't use BAB for:** Informational care content, variant comparison tables, FAQ sections.

---

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
[CTA: Verify your breeder's documentation →]
```

---

## BAB Writing Rules

### Before — Make the Pain Real
- **Specific, not generic:** "You sent $400 online and never heard back" > "some people get scammed"
- **Empathetic, not condescending:** "that's not a horror story — that's a Tuesday for African Grey buyers in Facebook groups" validates without judging
- **Name the emotion:** fear, frustration, heartbreak — not just the situation

### After — Make the Future Concrete
- **Sensory specificity:** "you know the bird's exact documentation before it arrives in your home"
- **Numbers where possible:** "$0 surprise vet costs in year 1" > "fewer vet visits"
- **Their future, not CongoAfricanGreys.com's product:** show their life, not CAG's features

### Bridge — Earn the Transition
- **Don't jump straight to CTA:** earn the bridge by validating the Before fully
- **Show the mechanism:** what specifically makes CongoAfricanGreys.com the bridge (CITES documentation, avian vet health cert + DNA sexing certificate, IATA-compliant bird shipping)
- **One bridge per BAB:** don't list every CAG feature — pick the one that most directly solves the Before

---

## BAB Length Guidelines

| Application | Before | After | Bridge |
|-------------|--------|-------|--------|
| Section hook (2–4 paragraphs) | 1 para | 1 para | 1–2 para |
| Full section (hero to CTA) | 2–3 para | 2–3 para | 3–4 para |
| Email sequence | 1 para | 1 para | 1 para |
| Social caption | 2–3 sentences | 2–3 sentences | 1–2 sentences |

---

## Common BAB Mistakes

| Mistake | Fix |
|---------|-----|
| Before is too mild ("it can be hard to find a good breeder") | Make the pain specific and real |
| After is vague ("peace of mind") | Make After concrete ("zero surprise vet bills in year 1") |
| Bridge is a feature list | Bridge is a single mechanism — the one thing that closes the gap |
| BAB without CTA | Every BAB ends with an action path |
| Before sounds like you're insulting scam sellers/competitors | Empathize with the reader's experience, don't attack the industry |

---

## Rules

1. **Before must name real pain** — vague discomfort doesn't motivate action
2. **After must be the reader's life, not CongoAfricanGreys.com's product** — show their future
3. **Bridge is one mechanism** — the specific CAG capability that makes the After real
4. **CTA required after every BAB** — contrast without action is just storytelling
5. **Don't attack competitors by name** — frame the industry pattern, not a specific seller
6. **BAB is for fear and contrast** — use AIDA for commercial intent, QAB for FAQ

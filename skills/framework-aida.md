---
name: framework-aida
description: "Reference guide for the AIDA framework applied to CAG homepage, purchase guide, and high-intent commercial pages. Use when building pages that must move a visitor from cold awareness to inquiry submission in a single session."
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

## What AIDA Is

AIDA is a conversion framework for pages where the visitor arrives with commercial intent and must be moved to action in one session. It works linearly — each stage qualifies the reader for the next.

```
A — Attention:  Stop the scroll. Make them read the next line.
I — Interest:   Show you understand their situation. Build relevance.
D — Desire:     Make them want what you have. Connect features to emotions.
A — Action:     Tell them exactly what to do next. Remove friction.
```

---

## When to Use AIDA at CAG

| Page | AIDA Application |
|------|-----------------|
| Homepage | Full AIDA arc across 18 sections |
| `/where-to-buy-african-greys-near-me/` | AIDA with buyer-fear overlay |
| State pages (FL, TX, CA, etc.) | AIDA with geo-specific desire |
| `/congo-african-grey-for-sale/` | AIDA compressed — hero to CTA fast |
| `/timneh-african-grey-for-sale/` | AIDA compressed — hero to CTA fast |

**Don't use AIDA for:** Informational pages, care guides, comparison pages — use Inverse Pyramid or QAB instead.

---

## CAG AIDA Section Map

### A — Attention (Hero section)
**Goal:** Make the right visitor say "this is for me" in 3 seconds.

Rules:
- H1 names the reader's situation, not CAG's product
- Subheading delivers the payoff promise
- Trust signals visible above fold
- CTA exists but isn't the focus yet

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

---

### I — Interest (Sections 2–4)
**Goal:** Show you understand the reader's specific situation better than they do.

Rules:
- Name the fears they haven't said out loud
- Validate their research process
- Show CAG is different without saying "we're different"

**Interest techniques:**
- "You've probably heard..." (validates their existing knowledge)
- "Most breeders will tell you..." (sets up contrast)
- "Here's what 15 years taught us that nobody talks about..." (insider revelation)

**CAG Interest content:**
- The problem with Craigslist / Facebook Marketplace (no CITES docs, CashApp payment, no recourse)
- The problem with "cheap african grey" sites (no USDA license, payment via no-recourse apps)
- What "captive-bred with documentation" actually means (CITES + USDA AWA + avian vet cert)

---

### D — Desire (Sections 5–12)
**Goal:** Make them want this specific bird from this specific breeder.

Rules:
- Lead every feature with the emotional outcome, not the feature
- Use specificity to make desire concrete
- Social proof here (testimonials, family stories, milestones)

**Feature → Desire transformation:**
```
Feature:  "CITES Appendix II captive-bred documentation on every bird"
Desire:   "You'll know your bird is legally documented before it ever ships — no customs seizure risk, 
           no questions at your door, no heartbreak after bonding with a bird that can't legally stay."

Feature:  "IATA-compliant bird shipping with live animal protocols"
Desire:   "Your African Grey travels under IATA live animal standards — temperature-controlled, 
           with an avian health cert. Not a Craigslist seller's shoebox."
```

**Desire amplifiers:**
- Milestone numbers ("2,000+ families have done this")
- Contrast ("most breeders give you 30 days — we give you 10 years")
- Story ("the Rodriguez family almost bought from a pet store...")

---

### A — Action (Final CTA section)
**Goal:** Tell them exactly what to do. Remove every possible objection.

Rules:
- One clear CTA — not multiple competing options
- Remove friction: what happens after they submit?
- Address the last objection before the button
- Urgency must be honest (clutch timing, waitlist)

**CAG Action template:**
```html
<h2>Ready to Meet Your African Grey?</h2>
<p>Fill out our quick inquiry form. [BREEDER_NAME] will respond personally within 24 hours 
   — not an automated email, a real reply with available birds that match your family.</p>
<p><strong>Deposit holds your bird.</strong> Health guarantee + CITES documentation included.</p>
[Inquiry Form — 3 fields: name, email, variant preference (Congo / Timneh)]
<p class="cag-form-note">We respond within 24 hours. No spam, no pressure, no bait-and-switch.</p>
```

---

## AIDA Quality Checks

Before finalizing an AIDA page:
- [ ] Attention: H1 names the reader's situation, not CAG
- [ ] Interest: At least one fear named and validated
- [ ] Desire: Every feature paired with an emotional outcome
- [ ] Action: One CTA, reassurance below button, response time stated
- [ ] Flow: Each section earns the next — no section jumps to action before desire
- [ ] Trust: Social proof in Desire stage, not buried at bottom

---

## Rules

1. **AIDA is linear** — don't put the CTA before Desire is built
2. **Desire before Action** — if a reader doesn't want it yet, they won't act
3. **One CTA in Action stage** — multiple CTAs split attention
4. **Features serve Desire** — never list features without the emotional payoff
5. **Honest urgency only** — "our next clutch is X weeks out" not "only 2 left!" if untrue

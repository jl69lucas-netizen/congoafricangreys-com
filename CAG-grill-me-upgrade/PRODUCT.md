# Product

> Strategic design context for CongoAfricanGreys.com, read by the `/impeccable` skill before any design work.
> Synthesized 2026-06-03 from `CLAUDE.md`, `docs/design.md`, `docs/design-system/README.md`, and project memory.
> Visual/token detail lives in `DESIGN.md`. This file answers *who / what / why*.
> Items tagged **[inferred — confirm]** were not stated verbatim in the docs and should be reviewed.

## Register

brand

<!-- A transactional + editorial marketing site where the design IS the product (provenance,
trust, and presentation are what convert). Not a "product" surface (no app/dashboard/admin). -->

## Users

Families and individuals shopping for a Congo or Timneh African Grey parrot, a $1,500–$3,500
purchase and a **40–60 year** commitment. Two overlapping audiences:

- **First-time Grey buyers** — anxious, scam-aware, researching heavily before they commit. They
  arrive via "African Grey parrot for sale near me / [state]" and informational queries ("do African
  Greys talk", "Congo vs Timneh"). Their dominant emotion is *fear of being scammed* and *fear of
  getting it wrong* on a decades-long decision.
- **Experienced parrot owners / aviculturists** — buying a specific variant, a breeding pair, or
  fertile eggs. They skim for documentation, pricing, and credibility, not education.

Context of use: mostly mobile, often mid-research across multiple breeder tabs, comparing a real
aviary against a sea of low-effort and fraudulent listings. The job to be done: *"Prove to me this
is a real, ethical, documented breeder I can trust with this money and this commitment, then make it
easy to reserve a specific bird."*

## Product Purpose

CongoAfricanGreys.com is the storefront and authority hub for **C.A.Gs – Midland, TX**, a small
family aviary (Mark & Teri Benjamin, est. 2014, USDA AWA-licensed, CITES Appendix I captive-bred).
It exists to convert trust-gated buyers into inquiry-form submissions and reserved-bird deposits,
and to rank as the most credible, best-documented African Grey resource in search.

Success = a qualified buyer reaches the inquiry form convinced the birds are real, captive-bred, and
fully documented — having had every scam fear and every "is this legit?" doubt answered on the page
before they ever pick up the phone. **Documentation and provenance are the product**; the design's
job is to make that provenance feel premium and verifiable, not generic.

## Brand Personality

**Three words: Warm. Trustworthy. Premium.** A high-end family pet boutique, not a classified
directory or a commodity pet store.

- **Voice:** First-person plural as the breeder ("we", "our birds", "Mark & Teri"); second-person to
  the buyer ("you", "your new companion"). Never corporate "the company". Calm, candid, expert. Talks
  buyers *out* of the wrong bird as readily as into the right one (honesty as a trust lever).
- **Tone goals:** confidence and calm reassurance, never urgency or hype. The emotional arc is
  *anxiety → reassurance → confidence*. The peak-end moment (final CTA) should feel safe, not pushy.
- **Editorial, not salesy:** reads like a considered publication about the species, with the
  commerce woven in — closer to a magazine feature than a product listing.

## Anti-references

What this must explicitly NOT look or feel like:

- **Scam / unverified breeder sites** — stolen stock photos, no documentation, untraceable payment,
  "rare exotic parrot, cheap, ships today". The whole design exists to be the visible opposite of this.
  *[stated: Negative Keyword Counter-Positioning — wild-caught / scam / cheap]*
- **Generic classified directories & commodity pet-store listings** — grid-of-everything, "stock",
  "inventory", "shop now", countdown timers, "limited time deal". Avoid the language and the look.
  *[stated: "high-end pet boutique, not a generic directory"]*
- **Generic AI-generated SaaS aesthetic** — gradient text, glassmorphism, dark neon glows, the
  big-number hero-metric template, identical icon-heading-text card grids, purple-on-black. Must pass
  the "did AI make this?" test. *[stated: Generic-Slayer Filter; CLAUDE.md absolute bans]*
- **Loud "marketing" energy** — 🎉🔥🚀 emoji, exclamation-heavy copy, hard-sell urgency. **[inferred — confirm]**
- **Anything implying wild-caught or illegal trade** — CITES safety is absolute; never imply
  poaching, smuggling, or "exotic" acquisition. *[stated: CITES Appendix I awareness rule]*

## Design Principles

1. **Provenance is the product — show the paperwork.** Every claim is backed by a verifiable
   artifact (USDA license, CITES Appendix I cert, DNA sexing, avian-vet health cert, closed band,
   proof-of-life photo). Trust is earned with evidence shown, not adjectives. *[stated]*
2. **Counter-position against the scam.** Make the legitimate, documented path visibly different from
   the fraudulent one. Side-by-side, "verify before you pay", real named reviews with photos. *[stated]*
3. **Warm-premium, never commodity.** Editorial serif, terracotta warmth, real photography, calm
   motion. It should feel like a family boutique that happens to be excellent at SEO. *[stated]*
4. **Honesty over conversion theater.** Name the downsides (40–60 yr commitment, noise, sensitivity),
   keep deposits refundable, talk the wrong buyer out. Candor is the conversion strategy. **[inferred — confirm]**
5. **Don't look AI-generated.** Distinctive, intentional, human. No slop tells. *[stated: Generic-Slayer Filter]*

## Accessibility & Inclusion

- **Target: WCAG 2.1 AA.** Non-negotiable, and an audience requirement: copy courts older buyers
  (the "lifetime companion / estate-plan" framing), so small tinted text and low contrast actively
  exclude part of the target market.
- **Known open issue (2026-06-03 audit):** ~172 nodes fail AA contrast — white-on-clay CTAs
  (3.38:1), `clay/70` labels (2.33:1), muted-green eyebrows (3.18:1), `white/65` on green (3.74:1),
  dark-CTA body text. Fix via a dedicated **clay-ink text token** (see DESIGN.md), not by redefining
  the locked `--clay` brand fill.
- Respect reduced motion (motion is already minimal — ≤0.2s, no parallax/bounce/autoplay).
- No `user-select: none` anywhere (permanently banned — anti-copy disabled).
- Maintain semantic heading order (H1–H6), ARIA labels on interactive controls, alt text on every
  image, and the `cag-congo.png` / `cag-timneh.png` image marks instead of the generic 🦜 emoji.

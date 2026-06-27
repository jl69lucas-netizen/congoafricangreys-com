# Homepage Entity Map — Entity-Based SEO Rewrite Plan
**Date:** 2026-06-03 · **Page:** `src/pages/index.astro` · **Status:** DRAFT (awaiting per-section approval before writing to live page)

This is the reusable "true entity, section-by-section" playbook the breeder asked for. Every CAG section — on this page and every future page — gets built/improved through the **4-move loop** below. This doc applies it to the 11 homepage sections that were not already covered by the breeder's own model examples (Health & Guarantee, Nationwide IATA, Beyond the Two Greys, Aviculture/Breeding).

## Verified-claim ledger (what entities we are ALLOWED to assert)
Confirmed by breeder 2026-06-03. **Never assert beyond this list without re-confirmation.**
- ✅ **PCR-based DNA sexing** (upgrade from generic "DNA sexing")
- ✅ **PBFD (Psittacine Beak & Feather Disease) screening**
- ✅ **Polyomavirus (APV) screening**
- ✅ **Board-certified avian veterinarian**
- ✅ 3-day written health guarantee · CITES Appendix I captive-bred · USDA AWA license · hatch certificate + closed band
- ✅ Shipping: **$185 airport pickup / $350 home delivery** (Delta, United, American cargo)
- ❌ NOT confirmed (do not use): Chlamydiosis/psittacosis testing, UV-B/D3 supplementation specifics, specific incubation temps for the egg product unless breeder confirms.

## The 4-Move Loop (the format)
1. **Structural Critique** — read the live section; name what is entity-thin / narrative-only.
2. **Recommended Entities + WHY** — specific high-authority entities, each with a *data-grounded* reason (Google Knowledge-Graph authority · PAA/voice demand · competitor gap · buyer-intent). (CLAUDE.md "Recommend + Why" rule.)
3. **Optimized Draft** — embed entities in copy grounded ONLY in the verified-claim ledger. Confidence Gate ≥97%, CITES-safe.
4. **Topical-Cluster Strategy** — internal-link anchors + schema so the section feeds the hub-and-spoke.

---

## 1. This Week's Aviary — "Which Hand-Fed African Greys Are Available Right Now?"
**Current:** Filterable BirdCard grid; trust pills CITES/DNA/Vet + new shipping line.
**Critique:** Strong commercially, but each card asserts "DNA Sexed / Vet Certified" as bare labels — no diagnostic entities, so Google reads it as retail, not clinical authority.

| New entity | Why (grounded) |
|---|---|
| **PCR-based DNA sexing** | Confirmed real; "PCR" is the Knowledge-Graph parent of "DNA sexing" — signals lab-grade method, not eyeballing. |
| **PBFD & Polyomavirus screened** | Confirmed real; top trust entity serious buyers search ("PBFD tested African Grey"); competitors rarely name it. |
| **Hand-fed → fully weaned (12–16 wks)** | Weaning age is the welfare entity buyers use to spot too-young/unweaned scam birds. |
| **Closed leg band + hatch certificate** | The captive-bred proof entities for CITES Appendix I. |
| **Availability status (available/reserved)** | Schema entity (`Offer` availability) — feeds Product/Offer JSON-LD. |
**Optimized move:** Add one micro-line under the trust pills or in card notes: *"Screened for PBFD & Polyomavirus, PCR DNA-sexed, fully weaned."* Add `Product`+`Offer` schema per available bird (price, availability, CITES doc).
**Cluster:** card → variant page (congo/timneh) → `/african-grey-parrot-care-guide/` (weaning) → `/how-to-avoid-african-grey-parrot-scams/`.

## 2. Congo African Grey — "What Is a Congo African Grey — the Classic Red-Tailed Talker?"
**Current:** Good — already uses *Psittacus erithacus*, 400–600g, red tail, hand-raised Midland.
**Critique:** Taxonomy present but shallow; intelligence + lifespan entities under-used here (they live in the Species section instead).

| New entity | Why |
|---|---|
| **Psittacus erithacus (binomial + once "P. e. erithacus")** | Already there once — add to an H-level + image alt to "own" the entity. |
| **Order Psittaciformes / family Psittacidae** | Taxonomic parents Google's KG links; one mention = strong entity-tree signal. |
| **Contextual / referential speech ("context-aware")** | High-value long-tail that differentiates from "talking parrot"; ties to Alex research. |
| **Sexual monomorphism** | The "you can't sex by sight" entity → justifies PCR DNA sexing. |
| **Hypocalcemia predisposition** | Species-specific health entity; links Congo → diet cluster. |
**Optimized move:** One H4 "How Is the Congo African Grey Classified?" naming Psittaciformes → Psittacidae → *Psittacus erithacus*. Add "referential speech" to the talker claim.
**Cluster:** → `/congo-african-grey-for-sale/`, `/african-grey-parrot-guide/`, compare table.

## 3. Timneh African Grey — "What Is a Timneh — the Calmer, Earlier-Talking Subspecies?"
**Current:** Uses *Psittacus timneh*, 275–375g, maroon tail, earlier talker.
**Critique:** Word "subspecies" is technically loose — Timneh was elevated to **full species** (split from *P. erithacus*). Correcting this is itself an authority signal.

| New entity | Why |
|---|---|
| **Full species split (BirdLife/IOC, ~2012)** | Accuracy = E-E-A-T; "is Timneh a separate species" is a real PAA. |
| **Psittacus timneh** | Own the binomial in H + alt. |
| **Earlier vocalization onset (~6–12 mo)** | Buyer-intent entity ("which African Grey talks sooner"). |
| **Lower acoustic profile / apartment-suitable** | Connects to the quietness PAA in §"Beyond the Two Greys". |
| **Reduced hypocalcemia anxiety vs Congo** | Optional, only if breeder confirms; else skip. |
**Optimized move:** Replace "subspecies" → "the Timneh African Grey (*Psittacus timneh*), recognized as a full species" + one earlier-talking + apartment-friendly line.
**Cluster:** → `/timneh-african-grey-for-sale/`, compare table, scam guide.

## 4. Compare Variants — "Is a Congo or a Timneh African Grey Right for You?"
**Current:** (Compare table block.) Decision-oriented.
**Critique:** Likely uses subjective labels; entity-SEO wants measurable column entities.

| New entity | Why |
|---|---|
| **Body mass (g) / total length (in)** | Measurable entities > adjectives for KG + featured snippet table. |
| **Tail coloration (scarlet vs maroon)** | The #1 visual ID entity buyers Google. |
| **Vocalization onset age** | Decision entity. |
| **Price band ($1,700–$3,500 vs $1,500–$1,600)** | Pull from price-matrix; feeds Offer schema. |
| **Temperament profile (bold vs even-keeled)** | Keep, but pair with the measurable rows. |
**Optimized move:** Ensure columns = measurable entities; add a one-line verdict mapping each to a buyer archetype. Add comparison schema/anchor to `/male-vs-female...` and variant hub.
**Cluster:** the spine of the variant cluster — link both variant pages + `/african-grey-comparison/`.

## 5. Verify Before You Pay — "How Do You Tell C.A.Gs From African Grey Scammers?"
**Current:** Strong — names USDA AWA #, CITES Appendix I, live dated video, reversible payments, Midland TX location.
**Critique:** Already entity-rich. Gap: no named *fraud-type* entities or verification-authority entities.

| New entity | Why |
|---|---|
| **Advance-fee / deposit fraud; non-delivery scam** | The named scam-type entities victims search post-loss. |
| **Reverse image search (TinEye / Google Lens)** | Actionable verification entity = featured-snippet bait. |
| **IC3 / FTC reporting** | Authority entities (.gov) → trust + outbound E-E-A-T. |
| **Chargeback / PayPal Goods & Services buyer protection** | Names the payment-protection entity, not just "reversible". |
| **USDA APHIS license lookup** | Already linked — name it as the verification entity. |
**Optimized move:** Add an H4 "What kind of scam is this?" naming advance-fee/non-delivery fraud + a reverse-image-search + IC3 line. CITES-safe (we are the documented seller).
**Cluster:** → `/how-to-avoid-african-grey-parrot-scams/`, `/trusted-african-grey-parrot-breeders/`, `/contact-us/`.

## 6. Why Families Choose C.A.Gs — "Why Choose C.A.Gs For Your Hand-Reared African Greys?"
**Current:** Excellent — USDA AWA, CITES Appendix I, DNA, vet, hatch cert, band, since 2014, World Parrot Trust.
**Critique:** Credential list is generic-vet level; can be upgraded to clinical entities now that they're confirmed.

| New entity | Why |
|---|---|
| **Board-certified avian veterinarian** | Confirmed; "board-certified" is the authority upgrade over "avian vet". |
| **PCR DNA sexing + PBFD/Polyomavirus protocol** | Confirmed; turns the bullet list into a clinical-grade trust signal. |
| **Animal Welfare Act (AWA) — name the statute** | Naming the law (not just "USDA license") = government entity authority. |
| **Aviculture / hand-rearing protocol** | Professional register signals expertise. |
| **Lifetime breeder support** | Retention/intent entity. |
**Optimized move:** Upgrade two bullets: "avian-vet health exam" → "board-certified avian-veterinary exam, PCR DNA sexing, and PBFD/Polyomavirus screening." Name the Animal Welfare Act once.
**Cluster:** → `/about/`, `/african-grey-parrot-price/`, health section.

## 7. The Species, Origin & Intelligence — "Where Do African Greys Come From, and Why So Smart?"
**Current:** Very strong — West/Central Africa, Jaco, IUCN Endangered/Vulnerable, Alex + Dr. Irene Pepperberg, Alex Foundation, CITES 2017, 40–60 yr.
**Critique:** Best entity section on the page already. Only minor cognitive-science entities missing.

| New entity | Why |
|---|---|
| **Cognitive enrichment / problem-solving** | "Enrichment" is the care-cluster bridge entity. |
| **Referential / label learning ("same/different", zero concept)** | Deepens the Alex authority; cited cognition entities. |
| **Allopreening / flock-social behavior** | Behavioral entity explaining bonding + attention needs. |
| **CITES CoP17 (the specific meeting)** | Names the regulatory event → precision authority. |
**Optimized move:** Add "zero concept / referential labeling" to the Alex bullet; one "cognitive enrichment" line bridging to care guide. Otherwise preserve.
**Cluster:** → `/african-grey-parrot-guide/`, `/african-grey-parrot-care-guide/`.

## 8. Transparent Pricing — "What Does a CITES-Documented African Grey Cost From C.A.Gs?"
**Current:** Price matrix + "what's included" + deposit; honest pricing.
**Critique:** Money entities present; missing the "what's bundled" entities as discrete line items (schema-able) and TCO framing.

| New entity | Why |
|---|---|
| **Itemized inclusions (CITES cert, hatch cert, band, PCR DNA cert, board-cert vet health cert, 3-day guarantee, diet plan)** | Each is an entity; itemizing = Product/Offer schema + "what's included" PAA. |
| **Total cost of ownership / first-year cost** | Links to the calculator; "African Grey cost per year" intent. |
| **Deposit ($200, refundable pre-ship)** | Transaction entity reducing friction. |
| **Two-tier shipping ($185 / $350)** | Now in data — name both. |
| **Congo vs Timneh price bands** | Comparison + Offer schema. |
**Optimized move:** Convert the "what's included" paragraph into a labeled entity list; add `Product`/`Offer` schema; reference first-year TCO + two-tier shipping.
**Cluster:** → `/african-grey-parrot-price/`, calculator, variant pages.

## 9. Common Questions (FAQ) — "What Do Buyers Ask Most Before Choosing a C.A.Gs Grey?"
**Current:** FAQ accordion + FAQPage schema (price, shipping, congo/timneh, sizing).
**Critique:** Good intent coverage; entity depth in *answers* can rise, and Q set should mirror real PAA wording.

| New entity / Q | Why |
|---|---|
| **"Are C.A.Gs African Greys PBFD/Polyomavirus tested?"** | Confirmed-real differentiator Q no competitor answers. |
| **"Is the Timneh a separate species from the Congo?"** | Real PAA; reinforces §3 correction. |
| **"How are African Greys DNA sexed?" → PCR** | Method entity Q. |
| **"What documents come with a CITES Appendix I bird?"** | Doc-entity Q feeding the pricing inclusions. |
| **"How much does shipping cost?" → $185 / $350** | Update answer to two-tier. |
**Optimized move:** Add 2–3 entity-rich Qs above (verified only); rewrite answers to embed entities; regenerate FAQPage schema from the actual `<details>` (per cag-entity skill method).
**Cluster:** answers link to health, pricing, variant, scam pages.

## 10. How to Buy — "How Do You Reserve a Hand-Raised African Grey — Step by Step?"
**Current:** Strong 4-step (browse → $200 deposit refundable → paperwork+vet cert → airport pickup), entities present.
**Critique:** Step 3/4 can carry the upgraded clinical + two-tier shipping entities; process schema missing.

| New entity | Why |
|---|---|
| **PCR DNA cert + board-cert vet health cert (Step 3)** | Confirmed; upgrades the paperwork step. |
| **Two delivery options ($185 airport / $350 home) (Step 4)** | Now real; Step 4 says "airport pickup" only — add home delivery. |
| **IATA Live Animals Regulations (LAR)** | The gold-standard transport entity (matches breeder's IATA example). |
| **HowTo schema** | Step-by-step → `HowTo` JSON-LD = rich result eligible. |
**Optimized move:** Step 4 → name both delivery tiers + IATA LAR; add `HowTo` schema for the 4 steps.
**Cluster:** → `/buy-african-grey-parrot-near-me/`, `/contact-us/`, shipping section.

## 11. DNA-Sexed at C.A.Gs — "Should You Choose a Male or Female African Grey?"
**Current:** Male vs female table (talking, temperament, bonding) + DNA-sexing note.
**Critique:** Behavioral entities good; the *method* entity (how sex is determined) is the C.A.Gs differentiator and is underplayed.

| New entity | Why |
|---|---|
| **PCR-based DNA sexing (blood/feather, ~99.9%)** | Confirmed; the trust core of this whole section. |
| **Sexual monomorphism** | The scientific reason sight-sexing fails → justifies DNA. |
| **Surgical sexing (as the inferior alternative)** | Contrast entity = authority ("we use PCR, not invasive surgical sexing"). |
| **Breeding-season hormonal behavior** | Already implied ("territorial in breeding season") — name it. |
**Optimized move:** Add a line: sex is confirmed by **PCR-based DNA sexing** (feather/blood), because African Greys are **sexually monomorphic** and cannot be reliably sexed by sight — included with every bird.
**Cluster:** → `/male-vs-female-african-grey-parrots-for-sale/`, variant pages.

---

## Site-wide rules this produced (to hardwire)
1. **Shipping cost line on every bird/listing card** — `Ships nationwide · $185 airport · $350 home` (DONE on BirdCard.astro; hardwire into all card-building agents' Golden Rule).
2. **The 4-Move entity loop is the required build method** for every section, every page, going forward.
3. **Verified-claim ledger governs** which health/credential entities may be asserted.

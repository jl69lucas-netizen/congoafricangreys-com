# Roys — Section-by-Section Build Outline + Word Budget

**Page:** `/available/roys/` · Male Congo African Grey · 4 months · **$2,300** ($200 deposit) ·
status `available` (single `Offer`, `InStock`).
**Primary keyword:** congo african grey for sale · **Owns (fanout):** *male* congo african grey for sale.
**Framework primary:** AIDA (Hero + About + Why). **Overlays:** BLUF = first ~50 words of EVERY
section · EBP = Documentation · QAB = FAQ + pricing micro-answers · PAS/PDB = Counter-positioning.
**Theme:** Direction D (inherited via BaseLayout — do NOT re-implement). **Voice:** first-person plural
("here at C.A.Gs, we hand-raised Roys ourselves"); 45% expert breeder · 30% buyer advocate · 15% educator
· 10% emotional.

**Word-budget target (measured):** Silvergate MAX **1,474** + 1,500 = **≥ 2,974 visible words.**
The +~1,500 expansion is concentrated in the **EXPANSION-THEME** sections (About · Why · Counter-positioning
· Shipping). The **shared-fact** sections (Documentation · Parent Birds) stay **link-out-brief** so the same
facts aren't re-written across all six bird pages.

**Guardrails honored in this outline:** no geo/state/city term · not the bare head term ("african grey
for sale") · no PBFD / Avian Polyomavirus · no visible date (freshness in schema only) · links/entities only
from the allowed lists below · single `Product`+`Offer` (never `AggregateOffer`).

---

## Section-by-section build table (spec §3 order — mandatory)

### 1. Breadcrumb · budget 0 (chrome, not body prose)
- **Heading text:** — (visual breadcrumb trail) — Home › African Greys For Sale › Roys
- **Framework:** —
- **Entities:** —
- **Internal links + anchors:** `/` (Home) · `/african-grey-parrots-for-sale/` ("African Greys For Sale")
- **External:** —
- **Schema:** `BreadcrumbList`. **Not counted in the 2,974** (navigation chrome).

### 2. Hero / Bird-Vitals + inquiry CTA · budget 120 · **CARRIES BLUF**
- **Heading text (H1):** *Roys — Male Congo African Grey For Sale ($2,300, Hand-Raised & DNA-Sexed)*
- **Framework:** AIDA-Attention + BLUF (price + variant + sex + key proof in first 2 lines).
- **Entities:** *Psittacus erithacus* · DNA sexing · hand-rearing · Midland, Texas · $2,300 / $200 deposit.
- **Internal links + anchors:** primary CTA → `/contact-us/` ("Ask about Roys" / "Reserve Roys").
- **External:** —
- **Notes:** Bird-Vitals card = variant · sex (♂) · age (4 mo) · price ($2,300) · status (Available) · talking
  (developing) · ships nationwide. **Mandatory shipping line under trust badges:**
  `Ships nationwide · $185 airport · $350 home`. Real photo (not stock).

### 3. AEO "Bird Snapshot" box · budget 60 · **CARRIES THE BLUF / FEATURED-SNIPPET TARGET**
- **Heading text:** *Roys at a glance* (declarative summary box, competitor-driven — beats Silvergate's
  price-range snippet with a *specific* price for a *specific* bird).
- **Framework:** AEO / BLUF — declarative ≤50-word featured-snippet-target sentence first, then a tight spec list.
- **Snippet-target sentence (verbatim seed, §10):** *"Roys is a hand-raised male Congo African Grey
  (Psittacus erithacus), 4 months old, priced at $2,300. He is DNA-sexed, CITES-documented, captive-bred in
  the USA, and ships nationwide ($185 airport / $350 home)."*
- **Entities:** *Psittacus erithacus* · CITES Appendix I (captive-bred, USA) · DNA sexing · 4-mo age · $2,300.
- **Internal links + anchors:** none inside the box (keep it snippet-clean).
- **External:** —

### 4. TrustBar · budget 30 (badge labels) · homepage trust pattern
- **Heading text:** — (badge row, no H2)
- **Framework:** —
- **Entities:** USDA Animal Welfare Act · CITES Appendix I (captive-bred USA) · DNA-sexed · AAV (avian-vet checked).
- **Internal links + anchors:** badges may deep-link — "CITES documentation" → `/cites-african-grey-documentation/`;
  "DNA-tested" → `/dna-tested-african-grey-for-sale/`.
- **External:** —
- **Notes:** line-icon SVGs, never emoji; never put `<svg>` in CSS `content:`.

### 5. About Roys (archetype / temperament) · budget **520** · **EXPANSION THEME** · CARRIES BLUF
- **Heading text (H2, Attention):** *What is Roys like to live with?* → 40-word BLUF answer first.
- **Framework:** AIDA-Attention/Interest + BLUF. First-person breeder voice ("we hand-raised Roys ourselves").
- **Entities:** hand-rearing / weaning · *Psittacus erithacus* · 40–60 year lifespan · Midland, TX aviary ·
  energetic/high-energy temperament (from clutch note "energetic, great with families").
- **Internal links + anchors:** "what daily life with a Congo looks like" → `/african-grey-parrot-guide/`;
  "Congo vs Timneh temperament" → `/congo-vs-timneh-african-grey/`.
- **External:** *Psittacus erithacus* natural-history claim → parrots.org/encyclopedia/grey-parrot/ (woven mid-sentence).
- **Notes:** the high-energy-talking-family-Congo angle (§6 moat). What his first 30 days look like. Expansion
  lives here — real, breeder-vouched temperament competitors can't write.

### 6. Health & Documentation · budget **240** · **SHARED-FACT, LINK-OUT-BRIEF** · CARRIES EBP + snippet-bait list
- **Heading text (H2, Interest):** *What documentation comes with Roys?* → BLUF: "Every grey we sell ships
  with a full documentation set." Then the **snippet-bait list** (clean `<ul>`, AI/snippet-friendly):
  - **H3:** DNA-sexing certificate (♂)
  - **H3:** AAV (Association of Avian Veterinarians) health certificate
  - **H3:** hatch certificate + closed leg band
  - **H3:** CITES captive-bred (Appendix I, USA) documentation
  - **H3:** weaning status (hand-reared → independent feeding)
- **Framework:** EBP (Evidence→Benefit→Proof). BLUF first sentence.
- **Entities:** DNA sexing · AAV · closed leg band / hatch certificate · CITES Appendix I (captive-bred USA) ·
  USDA Animal Welfare Act · weaning.
- **Internal links + anchors:** "CITES documentation" → `/cites-african-grey-documentation/`;
  "DNA-tested African Greys" → `/dna-tested-african-grey-for-sale/`;
  "our health guarantee" → `/african-grey-parrot-health-guarantee/`.
- **External:** AAV → aav.org; CITES status → cites.org (mid-sentence; retry `-A "Mozilla/5.0"` if curl 403s).
- **Notes:** Stays brief — link out, don't re-teach the documents in full (shared across all six pages).
  **No PBFD / Polyomavirus claim** (not in ledger).

### 7. Why Roys (fit) · budget **460** · **EXPANSION THEME** · CARRIES BLUF
- **Heading text (H2, Desire):** *Why Roys might be the right grey for you* → 40-word BLUF answer first.
- **Framework:** AIDA-Desire + honest fit-screening ("we'd rather he go to the right home").
- **Entities:** 40–60 year lifespan · hand-rearing · high-energy temperament · talking (developing, CITES-safe).
- **Internal links + anchors:** "what a Congo needs day to day" → `/african-grey-parrot-guide/`;
  "the lifetime commitment + cost" → `/african-grey-parrot-price/`.
- **External:** optional parrots.org grey-parrot reference for behaviour/enrichment (mid-sentence).
- **Notes:** Who Roys suits (busy, engaged family that wants a talker) and — honestly — who he doesn't.
  Expansion theme: buyer-advocate depth competitors omit (§8 content gap).

### 8. Counter-positioning — "Why a real $2,300 Congo beats an $850 'bargain'" · budget **480** · **EXPANSION THEME** · CARRIES snippet-bait list
- **Heading text (H2, Desire):** *Why a real $2,300 Congo beats an $850 "bargain"* → BLUF: state plainly that
  a documented hand-raised Congo cannot honestly be $850, then the **"real vs cheap" comparison list (snippet bait)**.
  - **H3:** No verifiable paperwork (no DNA cert, no CITES, no hatch band)
  - **H3:** No DNA-sexing or avian-vet (AAV) health check
  - **H3:** No breeder you can actually verify / hold accountable
- **Framework:** PAS / PDB (Problem→Agitate/Diagnose→Solve/Bridge). BLUF first.
- **Entities:** DNA sexing · AAV · CITES Appendix I (captive-bred USA) · USDA Animal Welfare Act · closed leg band.
- **Internal links + anchors:** "how to avoid bird scams" → `/how-to-avoid-african-grey-parrot-scams/`
  (price-objection anchor: "avoid bird scams"); "what a real grey actually costs" → `/african-grey-parrot-price/`.
- **External:** CITES (legality of captive-bred Appendix-I transfer) → cites.org, mid-sentence.
- **Notes:** new counter-positioning section (the +1.0 AEO-score lever). "real vs cheap" `<ul>`/table is the
  snippet-bait list AI engines lift. Never imply illegal/wild-caught trade.

### 9. Pricing & What's Included · budget **300** · CARRIES BLUF + QAB micro-answers
- **Heading text (H2, Action):** *How much is Roys, and what's included?* → BLUF: "Roys is $2,300 with a $200
  deposit to reserve him." Then:
  - **H3:** Price & reservation ($2,300 · $200 deposit · how to reserve via inquiry)
  - **H3:** What's included (documentation set · weaning/feeding guidance · post-arrival support)
- **Framework:** QAB (Question→Answer→Benefit) micro-answers per H3. BLUF first.
- **Entities:** $2,300 · $200 deposit · DNA cert · CITES · AAV health cert (the included set).
- **Internal links + anchors:** "full African Grey price breakdown" → `/african-grey-parrot-price/`;
  reserve CTA → `/contact-us/`.
- **External:** —
- **Notes:** Every figure traced to `clutch-inventory.json` / `price-matrix.json` / `financial-entities.json` —
  never hardcode a different number. Shipping cost is detailed in §10, referenced here.

### 10. Shipping & Logistics · budget **420** · **EXPANSION THEME** · CARRIES BLUF
- **Heading text (H2):** *How does Roys get to you safely?* → 40-word BLUF answer first (two tiers + nanny option).
- **Framework:** AIDA-Action support + QAB micro-answers; reassurance/E-E-A-T.
- **Entities:** IATA live-animal cargo / code LAR · Delta · United · American · example airport codes
  **DEN / LAX / MIA / ORD** · Avian Flight Nanny (in-cabin, from $750, quoted per route) ·
  $185 airport / $350 home.
- **Internal links + anchors:** reserve/ask-about-shipping CTA → `/contact-us/`.
- **External:** optional IATA Live Animals Regulations reference (mid-sentence) — verify before insert.
- **Notes:** Two delivery tiers **mandatory**: **Airport Pickup $185** · **Home Delivery $350** (figures from
  `financial-entities.json` `delivery_options`). Flight Nanny = in-cabin, never cargo hold. Expansion theme:
  full logistics depth (what cargo day looks like, climate/temperature embargoes, what we book) that the lean
  page lacked. **NO geo targeting** — airport codes are logistics examples, not location pages.

### 11. Parent Birds / Our Aviary · budget **210** · **SHARED-FACT, LINK-OUT-BRIEF**
- **Heading text (H2):** *Who are Roys's parents?* → BLUF: brief same-aviary parentage statement.
- **Framework:** EBP-lite / breeder-authority; first-person.
- **Entities:** hand-rearing · Midland, Texas family aviary · USDA Animal Welfare Act.
- **Internal links + anchors:** "more about our family aviary" → `/african-grey-parrots-for-sale/` (hub) or About.
- **External:** —
- **Notes:** Deliberately brief — parent/aviary detail is shared across all six pages, so link out rather than
  duplicate. Real birds only; never fabricate parent details.

### 12. FAQ (FAQPage schema) · budget **300** · CARRIES QAB micro-answers
- **Heading text (H2):** *Roys — frequently asked questions*
- **Framework:** QAB; each answer BLUF-first (snippet/AIO capture). **≥6 Q** (PAA-sourced, §11):
  1. Is Roys DNA-sexed and documented?
  2. How old is Roys and what's his temperament?
  3. How much is Roys and how do I reserve him?
  4. Can Roys be shipped to me?
  5. Do male Congo greys talk well?
  6. Why is Roys $2,300 when I've seen greys for $850?
- **Entities:** DNA sexing · CITES Appendix I (captive-bred USA) · AAV · IATA LAR · $2,300/$200 deposit · talking.
- **Internal links + anchors:** within answers — "avoid bird scams" → `/how-to-avoid-african-grey-parrot-scams/`;
  "Congo vs Timneh" → `/congo-vs-timneh-african-grey/`; "Congo variant page" → `/congo-african-grey-for-sale/`.
- **External:** —
- **Schema:** `FAQPage` (visible Q&A; verify rendered in `dist/`, not just source).

### 13. Newsletter · budget 20 (label/microcopy) · ONE placement, after FAQ
- **Heading text:** *Get clutch updates* (or equivalent) — single newsletter block, after FAQ only.
- **Framework:** —
- **Entities:** —
- **Internal links + anchors:** —
- **External:** —
- **Notes:** newsletter-exempt from word-count gate; exactly one placement (bird-page profile rule).

### 14. Other Available Birds · budget 40 (card labels) · sibling cluster
- **Heading text (H2):** *Other African Greys we have available*
- **Framework:** —
- **Entities:** —
- **Internal links + anchors:** sibling `/available/` pages — Amie · Bery · Jins & Jeni · Elad · Evie;
  plus hub `/african-grey-parrots-for-sale/`. Each card carries its own shipping line
  (`Ships nationwide · $185 airport · $350 home`).
- **External:** —

### 15. Inquiry CTA · budget 60 · CARRIES BLUF
- **Heading text (CTA):** *Ready to bring Roys home?* → one-line BLUF + clay-pill CTA.
- **Framework:** AIDA-Action.
- **Entities:** $2,300 · $200 deposit.
- **Internal links + anchors:** primary CTA → `/contact-us/` ("Reserve Roys" / "Ask about Roys").
- **External:** —
- **Notes:** BaseLayout global CTA band — pass `hideGlobalCta` if this page ships its own `<CTA>` (avoid double-CTA).

---

## Word-budget verification

| # | Section | Budget | Theme |
|---|---|---:|---|
| 1 | Breadcrumb | 0 | chrome (uncounted) |
| 2 | Hero / Bird-Vitals + CTA | 120 | core |
| 3 | AEO "Bird Snapshot" box | 60 | core (snippet) |
| 4 | TrustBar | 30 | core |
| 5 | About Roys | **520** | **EXPANSION** |
| 6 | Health & Documentation | 240 | shared-fact (brief) |
| 7 | Why Roys (fit) | **460** | **EXPANSION** |
| 8 | Counter-positioning ($2,300 vs $850) | **480** | **EXPANSION** |
| 9 | Pricing & What's Included | 300 | core |
| 10 | Shipping & Logistics | **420** | **EXPANSION** |
| 11 | Parent Birds / Our Aviary | 210 | shared-fact (brief) |
| 12 | FAQ | 300 | core |
| 13 | Newsletter | 20 | chrome (exempt) |
| 14 | Other Available Birds | 40 | chrome |
| 15 | Inquiry CTA | 60 | core |
| | **TOTAL** | **3,260** | — |

**Total = 3,260 visible words ≥ 2,974 target. PASS** (3,260 − 2,974 = 286-word headroom for drafting drift).

**Expansion concentration check:** About 520 + Why 460 + Counter-positioning 480 + Shipping 420 =
**1,880 words across the 4 EXPANSION-THEME sections** — they absorb the +~1,500 expansion. Shared-fact
sections stay lean: Documentation 240 + Parent Birds 210 = **450** (link-out-brief, no cross-page duplication).

---

## BLUF / snippet-bait map (for the build agents)
- **BLUF (~50-word answer first):** carried by §2 Hero, §3 Snapshot, §5 About, §6 Documentation, §7 Why,
  §8 Counter-positioning, §9 Pricing, §10 Shipping, §11 Parents, §12 FAQ (per answer), §15 CTA — i.e. EVERY
  prose section opens BLUF.
- **Featured-snippet target (≤50 words):** §3 AEO Bird Snapshot box (verbatim seed above).
- **Snippet-bait lists:** §6 Documentation (clean `<ul>` of the 5 documents) and §8 Counter-positioning
  ("real vs cheap" comparison list).

## Allowed-source confirmation
- **Entities** drawn only from the ledger: *Psittacus erithacus*, CITES Appendix I (captive-bred USA), AAV,
  DNA sexing, hatch cert + closed leg band, USDA AWA, IATA LAR, Delta/United/American, Midland TX,
  hand-rearing/weaning, 40–60yr lifespan. **No PBFD / Polyomavirus.**
- **Internal links** only from the cluster list (hub · congo variant · congo-vs-timneh · guide · CITES ·
  dna-tested · health-guarantee · price · scams · contact · siblings). **No state/city page, no bare head term.**
- **External:** parrots.org/encyclopedia/grey-parrot/ · aav.org · cites.org (verified-earlier set);
  AVMA + Lafeber are candidates to add in a later task.
- **Schema:** `Product` + single `Offer` (InStock, $2,300) · `FAQPage` · `BreadcrumbList` · `Organization`;
  `dateModified` in schema only — **no visible date.**

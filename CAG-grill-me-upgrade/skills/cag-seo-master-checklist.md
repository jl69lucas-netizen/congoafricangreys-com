---
name: cag-seo-master-checklist
description: Master SEO execution guide for all CAG pages (except location pages and comparison pages).
             4-phase workflow: Pre-Build Research → Planning Gate → Build → Optimization + QA.
             Invoke via Skill tool BEFORE starting any page build. Version 2.0 — merged from
             uploaded SEO checklist + existing seo-rules.md. Includes homepage keyword strategy,
             Internal Linking Library, and full term conversion table.
---

# SKILL: CAG Master SEO Execution Checklist (v2.0)

## SCOPE

**Applies to:** Homepage · Species guides · Care guides · Blog posts · Variant pages · Trust pages · Scam pages · Purchase guides · FAQ pages · About page · Any new hub or spoke page

**Excluded:** Location pages (use `@cag-location-builder` template) · Comparison pages (use `@cag-comparison-builder` template)

**Required reading before invoking this skill:**
- `docs/reference/seo-rules.md` — 62 rules (what to do and NOT do)
- `docs/reference/domain-knowledge.md` — variants, health conditions, trust signals
- `docs/reference/top-pages.md` — current GSC traffic baseline

---

## HOMEPAGE-SPECIFIC RULES

**Primary keyword: `african grey parrot breeder`**
**Homepage is CONVERSION-FIRST. Every section drives toward form submission.**

| Role | Keyword | Placement |
|---|---|---|
| Primary (H1) | `african grey parrot breeder` | H1, title tag, first 100 words, 3+ H2s |
| Transactional | `african grey parrots for sale` | H2 hero subtitle, counter snippets, CTAs |
| Variant | `congo african grey for sale` | H2 in available birds section |
| Compliance | `captive bred african grey parrot` | H2 in CITES trust section, first 300 words |
| Discovery | `buy african grey parrot` | H2 in purchase guide section |
| Authority | `cites documented african grey breeder` | H3/H4 in trust section |

**H1 recommendation (approved):**
```
African Grey Parrot Breeder | C.A.Gs — Captive-Bred Congo & Timneh African Greys | Midland, TX
```

**Homepage CTA rule:** ALL CTAs use form links — NO phone number in body. Phone 402-696-0317 appears ONLY in the footer.

---

## PHASE 1: PRE-BUILD RESEARCH

### Step 1: Competitor Analysis (MANDATORY — 8–12 Competitors)

Before writing ANY content, perform comprehensive competitor research.

**Search queries to analyze:**
1. `[Primary keyword] for sale` — e.g., "African Grey parrots for sale"
2. `[Primary keyword] near me`
3. `buy [primary keyword]`
4. `African Grey breeders`
5. `[Primary keyword] [state name]` — top 5 states
6. Also check GSC and GA4 for long-form queries (5+ words) already driving impressions

**Competitors to analyze (8–12 minimum):**
- Top 3 Google organic results for primary keyword
- Top 3 Bing organic results for primary keyword
- 2–3 specialized aviary/breeder sites
- World Parrot Trust (https://www.parrots.org/) — authority benchmark
- AAV Association of Avian Veterinarians (https://www.aav.org/) — authority benchmark
- 1–2 informational authority sites (beauty-of-birds, lafeber, petmd)

**For each competitor, document:**
1. **Word Count** — total page length
2. **Sections Included** — all major topics covered (H2 list)
3. **Keyword Usage** — primary, LSI, long-tail variations used
4. **Entity Density** — avian medical terms, locations, brands, people, statistics
5. **Linking Strategy** — internal links (count + anchor patterns), external authority links, anchor text
6. **Unique Selling Points** — health guarantees, pricing, shipping safety, certifications
7. **Weaknesses/Gaps** — missing content, weak sections, thin coverage
8. **Strengths** — what they do well that CAG must match or exceed
9. **User Experience** — navigation, CTA placement, testimonials, FAQ placement
10. **Angles Used** — transactional, urgency, comparison, trust, value, lifestyle
11. **Their ICP** — who are they targeting (first-time owners, experienced bird keepers, etc.)
12. **Outranking strategy** — specific 3–5 actions to outrank this competitor

**Deliverable format:**

```markdown
# COMPETITOR GAP REPORT — [Page Name]

## Competitor #1: [Name]
- URL: [URL]
- Word Count: [X words]
- H2 Topics: [list all H2s]
- Missing Entities: [avian medical terms, locations, credentials they lack]
- Keyword Gaps: [keywords CAG can capture that they miss]
- Weaknesses: [thin sections, missing trust signals, poor CITES coverage]
- Our Advantage: [3–5 specific actions to outrank them]

[Repeat for all 8–12 competitors]

## FINAL OUTRANKING STRATEGY
[Comprehensive strategy based on all gaps found — what CAG page will include that NO competitor has]

## Content Gaps to Fill
- [Gap 1]
- [Gap 2]

## Keywords Competitors Missed
- [Keyword 1]
- [Keyword 2]
```

---

### Step 2: Keyword Research + Entity Research

#### A. Primary Keyword Selection

The primary keyword is set by the page type:
- **Homepage:** `african grey parrot breeder`
- **Congo variant page:** `congo african grey for sale`
- **Timneh variant page:** `timneh african grey for sale`
- **Species guide:** `african grey parrot guide` / `african grey parrot care`
- **Purchase guide:** `buy african grey parrot near me`
- **Scam page:** `african grey parrot scam`
- **Price page:** `african grey parrot price`

#### B. Keyword Variations by Intent Type (100+ Required)

Develop 100+ keyword variations across these categories:

**1. Transactional (Bottom-Funnel):**
- `buy [variant] african grey parrot`
- `[variant] african grey parrots for sale`
- `[variant] african grey chicks available now`
- `african grey parrot price`
- `hand-fed african grey for sale`

**2. Long-Tail Conversational (6+ words):**
- `where can I buy a hand-fed african grey parrot with health guarantee`
- `best african grey breeders near me with CITES documentation`
- `how much does a hand-fed congo african grey parrot cost`
- `african grey parrots that talk and bond well`

**3. Voice Search Optimized:**
- `Are Congo African Grey parrots good for apartments?`
- `How big do Congo African Grey parrots get?`
- `Do African Grey parrots talk a lot?`
- `Can I get an African Grey parrot as a first bird?`

**4. Problem-Solution:**
- `hand-fed congo african grey chicks`
- `highly socialized companion parrots`
- `CITES documented captive-bred african grey`
- `apartment-friendly talking parrot`

**5. Comparison:**
- `Congo vs Timneh african grey parrots`
- `Congo African Grey vs Amazon parrot`
- `African Grey vs Macaw`
- `captive-bred vs wild-caught african grey`
- `hand-fed vs parent-raised african grey`

**6. Geographic/Local:**
- `african grey parrot for sale [state]`
- `african grey breeders near [city]`
- `african grey parrot nationwide shipping`
- Include all target states from `data/locations.json`

**7. LSI (Latent Semantic Indexing):**
- African Grey temperament, training, health
- silver-grey plumage, bright red tail, talking ability
- companion parrot, aviary bird, psittacine

**8. NLP (Natural Language Processing):**
- african grey care requirements
- best food for african grey parrots
- african grey socialization tips
- african grey subspecies characteristics

**9. Branded:**
- `C.A.Gs african grey parrots`
- `CongoAfricanGreys.com`
- `Mark and Teri Benjamin african grey breeders`
- `Midland Texas african grey aviary`

**10. Review/Testimonial:**
- `african grey parrot reviews`
- `best african grey breeder testimonials`
- `C.A.Gs reviews`
- `congoafricangreys.com reviews`

**11. Scam-Avoidance (Negative Keyword Counter-Positioning):**
- `african grey parrot scam warning`
- `how to avoid african grey parrot scams`
- `CITES certified african grey breeder vs scammer`
- `real african grey breeders with documentation`

#### C. Entity Optimization (150+ Entities Required)

Every full-length page (22+ sections) requires 150+ named entities across 6 categories:

**1. People Entities (10+ required):**
- Mark Benjamin (owner, C.A.Gs, Midland TX, 2014)
- Teri Benjamin (co-owner, C.A.Gs)
- Dr. Irene Pepperberg (famous avian researcher, Alex studies creator)
- Alex (Dr. Pepperberg's famous African Grey research subject)
- Sally Blanchard (avian behavioral authority, Companion Parrot Quarterly)
- Dr. Sarah Walsh, DVM (avian veterinarian)
- Barbara Heidenreich (Good Bird Inc — parrot training authority)
- Dr. Susan Friedman (Applied Behavior Analysis, BehaviorWorks)

**2. Location Entities (80+ required):**
- **Primary:** Midland, TX · 2508 Briaroaks Ct · 79707
- **Target States + Cities:** From `data/locations.json` — include all states + major cities
- **Airport Codes:** DEN, LAX, MIA, ORD, JFK, PHX, ATL, DFW, SEA, BOS, etc.
- **Regions:** Southwest, Southeast, Pacific Coast, Midwest, Northeast, etc.
- **IATA-approved shipping hubs:** Cross-reference with `data/locations.json`

**3. Medical/Health Entities (40+ required):**
- Avian Biotech DNA Testing (gender + disease panel)
- AAV (Association of Avian Veterinarians)
- Closed Leg Band (lifetime identification)
- PBFD — Psittacine Beak and Feather Disease
- APV — Avian Polyomavirus
- Psittacosis (Chlamydia psittaci)
- Bornavirus / PDD (Proventricular Dilatation Disease)
- Hypocalcemia (calcium deficiency — African Grey-specific)
- Feather Destructive Behavior / feather plucking
- Aspergillosis (respiratory fungal infection)
- Vitamin A deficiency
- USDA Form 7001 (Interstate Travel Health Certificate)
- Avian First Aid protocol
- DNA Sexing (endoscopic vs DNA method)

**4. Brand/Product Entities (20+ required):**
- Harrison's Bird Foods (High Potency Coarse)
- ZuPreem FruitBlend / AvianMaintenance
- Roudybush Daily Maintenance pellets
- Tops Outstanding Parrot Food
- Parrot Culture (socialization and weaning protocol)
- Early Neonatal Handling (ENH)
- AFA (American Federation of Aviculture)
- USDA APHIS (Animal and Plant Health Inspection Service)

**5. Statistical Entities (20+ required):**
- 500+ birds placed (since 2014)
- 40–60 years average lifespan
- 400–500 grams typical adult weight
- 12–14 inches typical adult length
- $1,500–$3,500 Congo African Grey price range
- $1,200–$2,500 Timneh African Grey price range
- 95%+ vocabulary mimicry success rate in properly socialized birds

**6. Credential/Certification Entities (15+ required):**
- CITES Appendix I (Convention on International Trade in Endangered Species)
- USDA AWA License (Animal Welfare Act)
- AFA Registered Aviary
- IATA Live Animals Regulations (shipping compliance)
- AAV Member Avian Veterinarian
- Avian Biotech Certified Disease-Free Bloodlines

**Entity density target:** 8–12 entities per 100 words (naturally integrated — never listed robotically or force-inserted)

**Good entity integration example:**
> "Every C.A.Gs Congo African Grey chick receives comprehensive health screening: [Avian Biotech DNA testing](https://www.avianbiotech.com/) for gender confirmation and viral panels (PBFD, Polyomavirus, Psittacosis, and Bornavirus), identity tracking via a [Closed Leg Band](https://www.afabirds.org/), primary nourishment with [Harrison's High Potency pellets](https://www.harrisonsbirdfoods.com/), and a comprehensive wellness check by a registered member of the [Association of Avian Veterinarians (AAV)](https://www.aav.org/)."

**Bad entity integration (avoid):**
> "Our African Greys receive Avian Biotech DNA testing and AAV checks and Harrison's bird foods and closed leg bands and..."

---

### Step 3: Keyword Fan-Out Expansion (MANDATORY)

Generate expanded keyword sets in 12 categories (15–20 keywords each):

**Category 1: Transactional Keywords**
Examples:
- `buy african grey parrots [state]`
- `african grey parrots for sale [city]`
- `purchase hand-fed african grey chick`
- `CITES documented african grey available`
Generate 15–20 more targeting the page's primary keyword + state/city modifiers

**Category 2: Conversational/Voice Search**
Examples:
- `Where is the best place to buy an african grey parrot?`
- `How much does a Congo African Grey parrot cost?`
- `Who are reputable african grey breeders in [state]?`
- `What should I look for in an african grey breeder?`
Generate 15–20 more in full question format

**Category 3: Problem-Solution Keywords**
Examples:
- `captive-bred african grey with CITES documentation`
- `non-screaming african grey parrot`
- `apartment-friendly talking parrot`
- `african grey for first-time bird owner`
Generate 15–20 more

**Category 4: Comparison Keywords**
Examples:
- `Congo vs Timneh african grey breeders`
- `African Grey vs Cockatoo for beginners`
- `captive-bred vs wild-caught african grey`
- `hand-fed vs parent-raised african grey temperament`
Generate 15–20 more

**Category 5: Delivery/Shipping Keywords**
Examples:
- `african grey shipping service to [state]`
- `IATA-certified african grey shipping [city]`
- `african grey flight nanny [airport code]`
- `safe african grey parrot delivery nationwide`
Generate 15–20 more

**Category 6: City/State-Based Keywords**
Examples:
- `african grey parrots for sale [city] [state]`
- `african grey breeders [city]`
- `buy african grey near [city]`
Generate 15–20 covering ALL target cities from `data/locations.json`

**Category 7: NLP/LSI Variants**
Examples:
- `ethical african grey breeders`
- `DNA health tested african grey`
- `avian vet certified african grey`
- `captive-bred CITES compliant parrot breeder`
Generate 15–20 more

**Category 8: Scam-Avoidance Keywords**
Examples:
- `legitimate african grey breeder vs scam`
- `verified CITES documentation african grey`
- `african grey parrot scam warning signs`
- `how to find reputable african grey breeders`
Generate 15–20 more

**Category 9: Care/Lifestyle Keywords**
Examples:
- `african grey parrot care requirements`
- `african grey lifespan commitment`
- `african grey care for beginners`
- `african grey talking ability training`
Generate 15–20 more

**Category 10: Trust/Review Keywords**
Examples:
- `C.A.Gs african grey reviews`
- `best african grey breeder testimonials`
- `congoafricangreys.com ratings`
- `mark benjamin african grey aviary reviews`
Generate 15–20 more

**Category 11: Variant-Specific Keywords**
Examples:
- `Congo african grey subspecies characteristics`
- `Timneh african grey personality vs Congo`
- `CAG vs TAG size comparison`
- `male vs female african grey differences`
Generate 15–20 more

**Category 12: Important Keywords (Suggested)**
Generate 15–20 additional keyword suggestions based on the specific page topic, competitor analysis gaps, and current GSC data from `data/analytics/`

---

### Step 4: Location/Logistics Entity Research

For pages with a shipping/delivery section, use web search to gather these entities:

**Geographic Entities Required:**
- Top 10 cities in target region (population 50,000+)
- Most parrot-friendly neighborhoods/communities in key cities
- Top 5 avian vet clinics in key metro areas
- Major regional airports with IATA Live Animal programs
- State wildlife/exotic pet regulations relevant to African Grey ownership

**Authority Entities Required:**
- Top 3–5 avian veterinary hospitals in key delivery cities
- Local AAV member veterinarians in target states
- State Veterinary Medical Associations
- USDA APHIS regional offices
- Local parrot/avian societies and clubs

**Logistics Entities Required:**
- Airport codes for all major delivery hubs
- IATA-compliant pet transport companies serving target states
- Delta Cargo, United PetSafe programs for flight nanny coordination
- Ground transit time estimates from Midland, TX to target cities

---

## PHASE 2: PLANNING GATE

### Step 5: Page Structure Planning

**Section count:** Default 22–24 sections. Exact count = match or exceed top competitor's section count. Never fewer than 22 without explicit user approval (Rule 26).

**Word count:** Top-ranking competitor's word count + 1,000 words minimum. Target: 5,000–6,000 words for 22-section pages. Never set without running competitor research first (Rule 27).

**Header count targets (Rule 28):**
- H1: exactly 1 (hero section only)
- H2: 25–35 throughout
- H3: 40–50 throughout
- H4: 10–20 (deep subsection headings — LSI keyword territory)
- H5: 5–10 MANDATORY — carries deep LSI/technical authority terms
- H6: 3–8 MANDATORY — carries voice search/natural language queries
- ALL SIX LEVELS required on every full-length page. H5 and H6 are not optional.

**Two-Keyword Header Method (Rule 28b — apply to every header that can carry a second term):**
Each header should pull double SEO duty: **[secondary/conversational keyword] + [related LSI · NLP · entity · concurrent keyword · or long-form modifier]**. Don't stop at the obvious keyword — append a second, *useful* term that broadens the header's reach without keyword-stuffing.
- ✅ "Why Choose C.A.Gs For Your **Hand-Reared** African Grey Parrots?" (secondary KW + LSI "hand-reared")
- ✅ "How Much Does a **Congo** African Grey Cost — and What's the **First-Year Total**?" (variant entity + long-form concurrent KW)
- ✅ "How Does C.A.Gs **Ship** an African Grey **to Your State**?" (transactional KW + geographic NLP)
- ✅ "What Is a **Timneh** African Grey — the **Calmer, Earlier-Talking** Subspecies?" (entity + LSI cluster)
- ❌ "Why Choose Us?" (no keyword) · ❌ "Shipping" (single bare term)
Keep it natural and conversational (What/How/Is/Can/Who). One secondary keyword + one related term per header — never three+ stacked. Applies across H2–H4 especially.

**Full section menu (27 possible sections — final selection determined by competitor research):**

| # | Section | Word Count | Anchor ID |
|---|---|---|---|
| 1 | Hero — H1 + subheadline + key takeaways + counter snippets | 150–200 | `#top` |
| 2 | Available Birds & Current Clutch | 400–600 | `#available-birds` |
| 3 | Health Guarantee & Testing | 800–1,200 | `#health-guarantee` |
| 4 | What is a [Variant] African Grey Parrot? | 200–250 | `#what-is-african-grey` |
| 5 | African Grey Breed History & Research | 300–400 | `#breed-history` |
| 6 | African Grey Temperament & Personality | 400–500 | `#temperament` |
| 7 | African Grey Feather Care & Grooming | 500–600 | `#grooming` |
| 8 | African Grey Nutrition & Diet | 500–600 | `#nutrition` |
| 9 | African Grey Training & Speech Development | 400–500 | `#training` |
| 10 | African Grey Care & Environmental Needs | 400–500 | `#care-environment` |
| 11 | African Grey Socialization (Parrot Culture + ENH) | 300–400 | `#socialization` |
| 12 | Why Choose C.A.Gs for Your African Grey | 300–400 | `#why-choose-cags` |
| 13 | About C.A.Gs & Meet Mark and Teri Benjamin | 200–250 | `#about-cags` |
| 14 | What Makes C.A.Gs the Best African Grey Breeder | 250–300 | `#what-makes-best` |
| 15 | Meet the Parent Birds / Breeding Pairs | 300–400 | `#meet-parents` |
| 16 | Customer Testimonials (3 strategically placed) | 400–500 total | `#testimonials` |
| 17 | C.A.Gs Breeding Commitment & Ethics | 200–250 | `#breeding-commitment` |
| 18 | African Grey vs Other Parrot Subspecies Comparison | 500–600 | `#subspecies-comparison` |
| 19 | Real-World Customer Case Study | 400–500 | `#case-study` |
| 20 | IATA Shipping & Coverage Areas | 700–900 | `#shipping` |
| 21 | Frequently Asked Questions (30+ questions) | 800–1,000 | `#faqs` |
| 22 | How to Buy Your African Grey from C.A.Gs | 300–400 | `#how-to-buy` |
| 23 | Parrot Culture & Early Neonatal Handling (Video) | 100–150 | `#parrot-culture` |
| 24 | Contact Information & Next Steps | 150–200 | `#contact` |
| 25 | Related African Grey Varieties & Companion Parrots | 200–300 | `#related-species` |
| 26 | Map & IATA Shipping Coverage Area | 100–150 | `#map` |
| 27 | Table of Contents (Required >1,500 words) | N/A | `#toc` |

---

### Step 6: Page Outline Gate + User Approval (FULL STOP — Rule 51)

**STOP. Do not write any section content until the user explicitly approves this outline.**

The Page Outline document must contain ALL of the following:

**A. Page Identity**
- Target URL slug
- Primary keyword (exact match)
- Page type (Transactional / Informational / Comparison / Scam Recovery / Species Guide / Care Guide)
- Recommended framework (AIDA, PAS, QAB, EBD, BAB, H-S-S, Inverse Pyramid, Entity-Tree)
- Target word count (top competitor's word count + 1,000 minimum)

**B. Competitor Snapshot (top 5 competitors)**
For each: URL, word count, all H2 topics listed, primary keywords, special elements, unique angles, weaknesses CAG can exploit.

**C. Complete H1–H6 Heading Tree**
Every heading on the page with:
- Heading level (H1/H2/H3/H4/H5/H6)
- Heading text (draft — question format where natural)
- Keyword type (Primary / Secondary / LSI / NLP / Longtail / Comparison / Voice Search)
- Why this heading (1 sentence)
- Section angle (AIDA, PAS, QAB, EBD, BAB, H-S-S, Trust, Urgency, Comparison, Value, Lifestyle)

**D. Keyword Distribution Table (section by section)**

| Section | Heading | Primary KW | LSI KWs | Longtail KWs | NLP/Conv | Comparison | Word Count |
|---|---|---|---|---|---|---|---|

Total row at bottom must hit 85–105× total keyword distribution target (Rule 18).

**E. Special Elements Plan**
- Newsletter signup: top / middle / bottom (minimum 1 required)
- Comparison table
- Price card
- Counter snippets (4 required after H1 — Rule 31)
- Trust badge bar
- Contact/inquiry form (3 required per page — Rule 32)
- Video embed placeholder
- FAQ accordion
- Table of Contents (required >1,500 words — Rule 29)

**F. Fan-Out Keyword List**
All keyword variations planned: exact match, phrase match, LSI clusters, NLP signals, PAA questions, voice queries, location modifiers, comparison phrases.

**GATE:** User must respond with "Approved", "Continue", or specific changes before any section is written.

---

## PHASE 3: BUILD

### Step 7: Section-by-Section Writing

**Workflow (Rule 13):**
1. Produce competitor analysis only → STOP, wait for user
2. User approves → produce Sections 1–5 only → STOP
3. User says "Continue" → produce Sections 6–10 → STOP
4. Repeat in batches of 5 until all sections complete
5. NEVER skip sections. NEVER merge sections. NEVER continue without "Continue" command.

#### 5-Tier Section Creation Form (complete BEFORE writing each section)

```
SECTION [#]: [TITLE]
================================================

TIER 1: CRITICAL ELEMENTS
—————————————————————————
1. Section Number & Title: Section [#]: [Exact Title]

2. Target Word Count:
   Min: [number - 10%]
   Max: [number + 10%]

3. Primary Keywords (3–5 from fan-out):
   ✓ [Primary Keyword] (use 2–3×)
   ✓ [Secondary Keyword] (use 1–2×)
   ✓ [Long-tail Keyword] (use 1×)
   ✓ [LSI Keyword] (use naturally)
   ✓ [Location/Entity Keyword] (use 1×)

TIER 2: CONTENT FOUNDATION
—————————————————————————
4. Content Angle (choose primary):
   ☐ T — Transactional/Urgency
   ☐ C — Comparison/Differentiation
   ☐ E — Health/E-E-A-T
   ☐ Blended — [specify angles]

   Supporting angles:
   ☐ [Second angle]
   ☐ [Third angle]

5. Conversational Opening (75–100 words, framework-matched):
   [Write the opening — Entity-Benefit-Purpose format]
   (Entity: what. Feature: measurable fact. Benefit: what buyer gains. Purpose: why it matters long-term.)

6. Header Structure (complete before writing):
   H2: [Main section header with primary keyword]
   H3: [Subsection 1 — question format preferred]
   H3: [Subsection 2]
   H4: [Detail point 1 with LSI keyword]
   H4: [Detail point 2 with LSI keyword]
   H5: [Technical authority term — e.g., "PBFD Screening Protocol"]
   H6: [Voice search query — e.g., "Is This Bird Good With Kids?"]

TIER 3: LINKING STRATEGY
—————————————————————————
7. Internal Links (5–8 per section):
   Position: BEGINNING or MIDDLE of sentences — never at end.
   Use varied anchor text — no repetition.
   1. [Anchor Text] → [/slug/]  |  Context: [where it appears]
   2. [Anchor Text] → [/slug/]  |  Context: [where it appears]
   [Continue for 5–8 total]

8. External Authority Links (1–2 per section):
   Position: BEGINNING or MIDDLE of sentences.
   Use descriptive anchor text (not "click here").
   1. [Anchor Text] → [https://authority-url.org]  |  Type: [.org/.gov/.edu]
   2. [Anchor Text] → [https://authority-url.com]  |  Type: [authority type]

TIER 4: ENTITY & TRUST
—————————————————————————
9. Geographic Entities (3–5 per section):
   ☐ Cities: [specific cities mentioned]
   ☐ States/Regions: [regions referenced]
   ☐ Airport Codes: [if relevant]

10. Authority Entities (1–2 per section):
    ☐ [Avian vet organization / credential]
    ☐ [Specific vet clinic / certifying body]

11. Trust Signals (2–3 per section):
    ☐ "500+ birds placed since 2014..."
    ☐ "40–60 year lifespan commitment..."
    ☐ "CITES Appendix I captive-bred..."
    ☐ "USDA AWA licensed aviary..."
    ☐ Customer testimonial quote
    ☐ Specific success statistic

TIER 5: QUALITY CONTROL
—————————————————————————
12. Special Elements for this Section:
    ☐ Newsletter signup box (Top/Middle/Bottom position)
    ☐ FAQ module
    ☐ Testimonial box
    ☐ Pricing table
    ☐ Comparison table
    ☐ Map embed
    ☐ Image gallery/placeholder

13. Image Requirements:
    ☐ [Section image description] — [dimensions per image-specs.json]
    ☐ Alt text (250+ characters required — Rule 50)
    ☐ Image description (300+ words for major images — Rule 50)
    ☐ File name: [keyword-rich-seo-filename.webp]

14. Call-To-Action (form-based — NO phone number):
    CTA Type: ☐ Inquire Now ☐ Submit Inquiry ☐ Reserve a Bird ☐ See Available Birds
    CTA Text: "[Action statement with benefit, link to /contact-us/]"

15. Final Section Checklist:
    ☐ Word count within target range
    ☐ Primary keyword used 2–3× naturally
    ☐ 5–8 internal links included (beginning/middle of sentences)
    ☐ 1–2 external authority links included
    ☐ 3–5 geographic entities mentioned
    ☐ Headers use question format where natural
    ☐ Conversational, warm, expert avicultural tone
    ☐ Paragraphs 3–5 sentences max (50–80 words)
    ☐ No keyword stuffing
    ☐ No stop words used unnecessarily
    ☐ Negative keywords addressed (scam / wild-caught / cheap)
    ☐ Trust signals included
    ☐ Local entities naturally integrated
    ☐ Clear CTA at section end (form link only)
    ☐ CITES/captive-bred language in first 300 words (hero only)
```

---

### Step 8: Linking Strategy

#### A. Internal Links (50+ Required Per Full Page)

**Link categories:**

**1. Navigation Links:**
- Table of Contents at top (jump links to all sections)
- Quick navigation menu at bottom
- Back to top: `[⬆ Back to Top](#top)` at end of each major section

**2. Cross-Section Jump Links (examples):**
- From Key Takeaways → Available Birds, Health Testing, Pricing
- From Available Birds → Purchase Process, Shipping, Testimonials
- From Health Guarantee → Parrot Culture, Meet Parent Birds
- From Comparison section → Congo/Timneh variant pages
- From FAQ → Relevant sections (Care, Diet, Shipping)
- From How to Buy → Available Birds, Contact, Shipping

**3. Related Pages (Internal Site Links):**
Use Appendix A URL Library at end of this skill for all valid URLs.

**4. Contextual Links (Within Paragraphs):**
Example: `"Our [Parrot Culture protocols](#parrot-culture) ensure emotionally resilient birds."`
Example: `"Learn more about [CITES Appendix I documentation](/cites-african-grey-documentation/)"`

#### B. External Links (50+ Required Per Full Page)

**Health & Veterinary (15 links):**
1. [Avian Biotech Disease Testing](https://www.avianbiotech.com/)
2. [IQ Bird DNA Testing Laboratory](https://www.iqbirdtesting.com/)
3. [AAV — Association of Avian Veterinarians](https://www.aav.org/)
4. [AAV Public Avian Vet Database](https://www.aav.org/search/custom.asp?id=1803)
5. [Lafeber Vet Avian Medicine Resource](https://lafeber.com/vet/)
6. [AVMA — American Veterinary Medical Association](https://www.avma.org/)
7. [AAHA — American Animal Hospital Association](https://www.aaha.org/)
8. [PetMD — African Grey Parrot Breed Information](https://www.petmd.com/)
9. [ASPCA Pet Care and Safety](https://www.aspca.org/pet-care)
10. [ASPCA Animal Poison Control Center](https://www.aspca.org/pet-care/animal-poison-control)
11. [ASPCA Toxic Foods for Birds](https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets)
12. [Exotic Pet Vet Directory](https://www.exoticpetvet.com/)
13. [University of Georgia Exotic Animal Pathology](https://vet.uga.edu/)
14. [VEG — Veterinary Emergency Group Avian Info](https://veterinaryemergencygroup.com/)
15. [Pet Poison Helpline](https://www.petpoisonhelpline.com/)

**Breed Information & Standards (12 links):**
1. [World Parrot Trust — African Grey Profile](https://www.parrots.org/)
2. [The Alex Foundation — Dr. Irene Pepperberg Research](https://alexfoundation.org/)
3. [AFA — American Federation of Aviculture](https://www.afabirds.org/)
4. [IUCN Red List — Congo African Grey Status](https://www.iucnredlist.org/)
5. [CITES Appendix Regulations](https://cites.org/)
6. [Beauty of Birds — African Grey Information](https://www.beautyofbirds.com/)
7. [Bird Channel Avicultural Guides](https://www.birdchannel.com/)
8. [Northern Parrots Species Data](https://www.northernparrots.com/)
9. [Lafeber Pet Birds — African Grey Care](https://lafeber.com/pet-birds/)
10. [Parrot Society of Australia](https://www.parrotsociety.org.au/)

**Training & Behavior (10 links):**
1. [BehaviorWorks — Dr. Susan Friedman](https://www.behaviorworks.org/)
2. [Good Bird Inc — Barbara Heidenreich](https://www.goodbirdinc.com/)
3. [The Parrot Problem Solver — Sally Blanchard](https://www.companionparrot.com/)
4. [BirdTricks Avian Training Academy](https://www.birdtricksstore.com/)
5. [IAABC — Animal Behavior Consultants](https://iaabc.org/)
6. [Parrot Enrichment Activity Guides](https://www.parrotenrichment.com/)
7. [Clicker Training — Karen Pryor Academy](https://clickertraining.com/)
8. [Avian Behavior International](https://avianbehaviorinternational.com/)
9. [Pamela Clark Certified Parrot Behaviorist](https://pamelaclarkonline.com/)

**Nutrition & Products (8 links):**
1. [Harrison's Bird Foods](https://www.harrisonsbirdfoods.com/)
2. [ZuPreem Premium Parrot Diets](https://www.zupreem.com/)
3. [Roudybush Avian Maintenance Pellets](https://www.roudybush.com/)
4. [Tops Parrot Food — Organic Pellets](https://www.topsparrotfood.com/)
5. [Chewy Avian Supplies](https://www.chewy.com/)
6. [Parrot Toys USA — Safe Enrichment](https://www.parrottoysusa.com/)

**Animal Welfare & Ethics (8 links):**
1. [World Parrot Trust — Anti-Poaching](https://www.parrots.org/)
2. [Avian Welfare Coalition](http://www.avianwelfare.org/)
3. [Phoenix Landing Parrot Rescue](https://www.phoenixlanding.org/)
4. [The Gabriel Foundation Avian Sanctuary](https://thegabrielfoundation.org/)
5. [USDA APHIS Animal Welfare Act](https://www.aphis.usda.gov/)
6. [FWS — US Fish and Wildlife Service Bird Laws](https://www.fws.gov/)
7. [FTC Consumer Protection Against Bird Scams](https://www.ftc.gov/)

**Geographic/Shipping Resources (5 links):**
1. [USDA APHIS Interstate Travel Regulations for Birds](https://www.aphis.usda.gov/)
2. [Delta Cargo — Live Animal Shipping Guidelines](https://www.deltacargo.com/)
3. [United PetSafe Avian Shipping Program](https://www.united.com/)
4. [IATA Live Animals Regulations](https://www.iata.org/en/programs/ops-infra/live-animals/)

#### C. 3 Anchor Text Strategies (Rule 58)

**Strategy 1: Exact Match Anchors (use sparingly — 1–2 per page)**
- Anchor text = the exact keyword you want the target page to rank for
- Power: Highest SEO signal · Risk: Moderate if overused
- Best for: Links from detail pages to category/hub pages

Example: "Luna is a verified [Teacup Congo African Grey](#available-birds) from champion bloodlines..."

**Strategy 2: Conversational/Descriptive Anchors (preferred — most links)**
- Anchor text = longer phrase describing destination naturally within a sentence
- Power: Medium-High · Risk: Low
- Best for: Long-tail keyword links, cross-section navigation

Example: "...she is the ultimate choice for [apartments or smaller living spaces](#temperament)"
Example: "Read more about [how CITES documentation protects your purchase](/cites-african-grey-documentation/)"

**Strategy 3: Branded Anchors (use for trust building)**
- Anchor text = brand/company name
- Best for: About page references, testimonials, schema reinforcement

Example: "C.A.Gs provides what most online listings never can..."

---

### Step 9: Special Elements Placement

**Counter Snippets (4 required after H1 — Rule 31):**
Under 4 words each, start with a number or percentage:
- `40+ Year Lifespan Commitment`
- `100% CITES Certified`
- `DNA Sexed Guaranteed`
- `USDA AWA Licensed`
- `Zero Wild-Caught Birds`
- `Avian Vet Certified`

**Contact/Inquiry Forms (3 required — Rule 32):**
1. After hero / counter snippets (top)
2. After trust section / mid-page
3. After FAQ section (bottom)

**CTAs — Form Only (Rule 61):**
- ✅ `👉 [Submit an inquiry to reserve your Congo African Grey](/contact-us/)`
- ✅ `📋 [Fill out our quick inquiry form — we respond within 24 hours](/contact-us/)`
- ✅ `<a href="/contact-us/" class="cag-btn-primary">Inquire About a Bird</a>`
- ❌ `📞 Call 402-696-0317 to reserve today!` — NEVER in body copy

**Newsletter Signups (3 per full hub page):**
- Position 1 (Top — after Diet/Nutrition section): "Get our FREE African Grey Diet & Nutrition Guide!"
- Position 2 (Middle — after Shipping section): "Calculate your IATA shipping cost!"
- Position 3 (Bottom — after Contact section): "Join 500+ happy C.A.Gs families!"

**Image Placeholders:**
Leave clearly labeled placeholders for all images/videos:
- `[INSERT PHOTO: bird-name-profile.webp] Alt: "[250+ char alt text]"`
- `[INSERT INFOGRAPHIC: feature-type-760px.html]`
- `[INSERT VIDEO: parrot-culture-demonstration.mp4]`
- `[INSERT MAP: google-maps-midland-tx-embed]`

---

### Step 10: Writing Guidelines

#### A. Voice & Tone

**✅ DO:**
- Natural, conversational language — write like a trusted avicultural expert
- Answer real questions people actually search
- Include emotional connection and empathy (40-year commitment is life-changing)
- Build trust through transparency (pricing, documentation, process)
- Sound human, warm, and knowledgeable
- Guide readers: Curiosity → Trust → Inquiry → Form Submission
- Use contractions: "we're" not "we are", "you'll" not "you will"
- Second person (you/your): Address reader directly
- Satisfy search intent immediately in the first paragraph
- Question-based H2/H3 headers (conversational FAQ format: What, How, Is, Can, Do)

**❌ DON'T:**
- Keyword stuff: "African grey parrot for sale... our African grey parrots for sale..."
- Use robotic language: "This product..." / "This offering..."
- Repeat exact phrases unnaturally
- Sound like a template or generic AI output
- Use aggressive marketing or unverifiable claims
- Use excessive exclamation points
- Use ALL CAPS except for emphasis
- Use generic platitudes ("We care about birds" — be specific!)
- Overpromise ("Perfect companion for everyone without effort!")

**Good vs Bad Examples:**

❌ Bad: "Congo African Grey chicks are available for sale. They are smart birds. Contact us."
✅ Good: "Looking for a brilliant avian companion who'll carry out actual conversations with you? Our Congo African Grey parrots (400-500g, 12–14 inches) are famous for being sensitive intellectuals who form unbreakable bonds with their families."

❌ Bad: "Our parrots have health guarantees."
✅ Good: "What if your parrot develops an underlying congenital health issue at year 5? C.A.Gs provides a comprehensive health guarantee — backed by Avian Biotech DNA disease panel screening and annual avian vet health certificates — covering our entire breeding bloodline."

#### B. Humor Rules (Apply to ALL Pages — Rule 36)

Apply thoughtfully, not forced. Four humor modes:

1. **"The Honesty Policy"** — relatable breeder honesty:
   *"Our African Greys are bred for intelligence, companionship, and the uncanny ability to learn your WiFi password before you do."*

2. **"The Interviewer" Tone** — the bird is vetting the owner:
   *"Are you prepared to be outsmarted daily by a creature that weighs less than 500 grams? Apply to be [Bird Name]'s forever person."*

3. **Punny Wordplay** — lean into African Grey vocabulary gifts:
   *"50% Congo genetics, 50% Timneh, 100% opinion-having roommate who will outlive your mortgage."*

4. **Comparison Humor** — unexpected comparisons:
   *"Technically this is a bird. Functionally, it is a sentient 4-year-old with flight capability and a 60-year contract."*

#### C. Opening Paragraph Formula (Rule 37)

Every section opening (1–2 sentences) must contain all four:
- **Entity** — who/what (bird name, variant, C.A.Gs, Midland TX)
- **Feature** — measurable fact (weight, age, price, CITES status)
- **Benefit** — what it means for the buyer
- **Purpose** — the deeper reason it matters (40-year bond, family commitment)

Example: *"[Bird Name] is a 12-week-old Congo African Grey (entity) hand-raised at C.A.Gs in Midland, TX, weighing 380g (feature), socialized daily with our family so she bonds naturally and immediately with yours (benefit) — the foundation of a 40–60 year relationship that begins the moment she comes home (purpose)."*

#### D. Conversational Header Format (Rules 38, 52)

**ALL headers in conversation FAQ-style where natural — format: What / How / I / Is / Can / Do / Are**

H1 examples:
1. "Where Can I Buy a Hand-Fed Congo African Grey Parrot with CITES Documentation?"
2. "Looking for an Intelligent Companion? Meet Our Captive-Bred Congo African Grey Parrots"
3. "Congo African Grey Parrots for Sale: IATA Safe Shipping to 50+ States from Midland, TX"
4. "Why Are C.A.Gs African Grey Parrots Chosen by 500+ Happy Families?"
5. "Ready for a Lifelong Avian Companion? Our African Greys Come with Lifetime Breeder Support"
6. "African Grey Parrot Breeder | C.A.Gs — Captive-Bred Congo & Timneh African Greys | Midland, TX"

H2 examples:
- "What Makes the Congo African Grey the Ultimate Companion Parrot?"
- "How Much Does a Captive-Bred Congo African Grey Really Cost? (Full Price Breakdown)"
- "Are African Greys Good in Apartments? Here's What 10 Years of Placements Taught Us"
- "Congo vs Timneh African Grey: Which Subspecies is Right for Your Family?"

H3 examples:
- "Do African Greys Scream All Day? (And How to Teach Quiet Behavior)"
- "Can I Leave My African Grey Alone During the Workday? (The Honest Answer)"
- "What's Included with Every C.A.Gs African Grey? (Full Documentation Breakdown)"

H5 examples (technical authority — must be present):
- "PBFD Screening Protocol at C.A.Gs Aviary"
- "USDA AWA License Explained"
- "DNA Sexing Methodology: Avian Biotech vs Endoscopy"
- "Avian Biotech Disease Panel: 4 Core Tests"

H6 examples (voice search — must be present):
- "Is This Bird Good With Kids?"
- "What Happens After I Pay a Deposit?"
- "Can I Visit the Aviary Before Buying?"
- "How Do I Know This Bird Is Captive-Bred?"

#### E. Paragraph Structure

**Opening paragraph format (first 150 words of page):**
1. Answer the primary question immediately
2. Include location-specific details (Midland, TX + target state)
3. Integrate 5+ entities naturally
4. Add clear call-to-action (form link)
5. Use long-tail keyword variations

**Body paragraph guidelines:**
- 3–5 sentences per paragraph (scannable)
- One main idea per paragraph
- Use transition words (However, Additionally, For example)
- Bold key facts, prices, important stats sparingly
- Include specific examples and statistics
- Never more than 80 words per paragraph

---

## PHASE 4: OPTIMIZATION + QA

### Step 11: SEO Optimization

#### A. Meta Information (Rule 21, 22, 23)

**Standard Meta Title Formula (Rule 21):**
```
[Primary Keyword] | [Power Word] + [Number] | [Long-tail Conversational Query] | C.A.Gs - Midland, TX
```
- Begin with primary keyword
- Add a number where authentic ("DNA tested", "500+ families")
- Power word: Certified, Ethical, Trusted, CITES-Documented, Captive-Bred
- Insert long-tail conversational query
- End with `C.A.Gs - Midland, TX`
- Use `|` separators
- Max 275 characters

**Extended 4-Tone Meta Title System (Rule 22):**
Format: `[Primary Keyword] | [Conversational Query] | [Comparison/LSI/NLP] | C.A.Gs Trust Ending`

**🔴 URGENCY TONE:**
> African Grey Parrot for Sale | Where Can I Buy a Captive-Bred Grey Near Me? | CITES Documented vs Wild-Caught | C.A.Gs — America's Trusted African Grey Aviary Since 2014

**🆚 COMPARISON TONE:**
> African Grey Parrot for Sale | How Much Does a Congo Grey Cost? | C.A.Gs vs Other Breeders, CAG vs Timneh Comparison | #1 Avian Biotech Tested Ethical Breeder — Full CITES Compliance

**💰 TRANSACTIONAL TONE:**
> African Grey Parrot for Sale | What's the Best African Grey Breeder in USA? | $1,500 Hand-Fed Chicks Available Now | C.A.Gs - Midland, TX — Family-Owned Aviary Specialists

**🛡️ TRUST/HEALTH TONE:**
> African Grey Parrot for Sale | Are African Greys CITES Documented? | DNA Tested, USDA AWA Licensed vs Unverified Listings | C.A.Gs - Midland, TX — 500+ Families Trust Our Captive-Bred Guarantee

**Meta Description (Rule 23):**
- Standard: max 155 characters
- Extended: up to 290 characters for high-competition pages
- Must include: primary keyword + long-tail query + trust signal + CTA
- Emphasize: CITES documentation, DNA sexing, avian vet cert, C.A.Gs experience

**CAG Meta Description Examples:**

Standard (155 chars):
> Hand-fed Congo African Grey parrots for sale. CITES documented, USDA AWA licensed. DNA sexed chicks from C.A.Gs - Midland, TX. Nationwide IATA shipping.

Extended Urgency (290 chars):
> Congo African Grey for sale — only 6 chicks available this clutch | Don't miss out — 500+ families chose C.A.Gs over other breeders | $1,500-$3,500 hand-fed chicks vs $4,500+ at pet stores | Avian Biotech DNA tested, IATA-certified flight nanny to 50 states | Reserve yours before they're gone | Act now

#### B. Schema Markup (Rule 5)

Implement these schema types on every full page:
1. **Organization Schema** — C.A.Gs business information (managed by `src/components/Schema.astro`)
2. **LocalBusiness Schema** — Midland TX location, hours, contact
3. **Product Schema** — Individual bird listings with price, availability
4. **AggregateRating Schema** — Review aggregate on bird listing/product pages
5. **FAQPage Schema** — 30+ FAQ questions and answers
6. **BreadcrumbList Schema** — `Home > [Section] > [Page]`
7. **Person Schema** — Mark Benjamin, Teri Benjamin profiles (on About page)

Never remove or modify existing schema without user approval (Rule 5).

#### C. Voice Search & AI Chatbot Optimization (AIO/GEO)

**Strategies:**
1. Use natural questions as H2/H3 headers (How, What, Why, When, Where, Are, Can, Is, Do)
2. Answer questions in first 50 words of each section
3. Featured snippet-ready content:
   - Bullet lists with clear structure
   - Comparison tables (3–6 columns, 3–8 rows, first column = categories)
   - Step-by-step numbered lists
   - Rapid-fire definition paragraphs
4. Conversational phrasing (contractions, second-person)
5. Long-tail queries within H2/H3 headers
6. Entity-dense answers (proper nouns, exact statistics, specific conditions)

**Voice Search Optimization Example:**
Query: "How big do Congo African Grey parrots get?"
Optimized answer (first 50 words): "Adult Congo African Grey parrots typically weigh between 400–500 grams and reach an average length of 12–14 inches from beak to tail. C.A.Gs Congo African Grey chicks are meticulously hand-raised from robust bloodlines, ensuring they develop into large, healthy adults reflecting peak physical health."

#### D. Keyword Density Guidelines (Rule 18, 19)

**Target keyword density:**
- Primary keyword: 1.5–2% (natural distribution, never forced)
- Secondary keywords: 0.5–1% each
- LSI keywords: distributed fluidly throughout
- Long-tail variations: embedded in headers and body

**Keyword placement priority:**
1. H1 title (primary keyword front-loaded)
2. First 100 words (primary + 2–3 natural variations)
3. H2 headers (transactional + conversational variations)
4. Body paragraphs (organic contextual flow)
5. Image alt text (where strictly relevant)
6. Meta title and meta description
7. URL slug (`/[primary-keyword-slug]/`)

---

### Step 12: Image Optimization (Rule 50, IMAGE-01 through IMAGE-04)

**Before generating any image:**
1. Read `data/image-specs.json` for the current page_type and section
2. Use the specified `dims`, `source`, and `infographic_type` exactly
3. Priority: user instruction > image-specs.json > agent defaults

**Every image requires:**
- **Alt text:** 250+ characters — include keyword, context, entity, location reference
- **Image description:** 300+ words — detailed SEO-optimized description block
- **File name:** keyword-rich-seo-filename.webp (lowercase, hyphens, no spaces)
- **File size:** Highly compressed (<100KB for page-content images)
- **Dimensions:** See image-specs.json for page-type-specific specs

**Portrait images:** 1200×2133px native (9:16) — CSS display width: 350px (Rule IMAGE-03)
**Infographic widths (Rule 54):**
- Species guide, blog, care guide: **760px** wrapper, 400px desktop height
- Homepage, location pages, hero: **1100px** wrapper, 400px desktop height
- Mobile: 100% width, auto height

**OG Image:** Every page needs a 1200×630px OG image (separate generation — Rule IMAGE-04)

**Alt text example (location-specific, 250+ chars):**
```
Congo African Grey parrots for sale from C.A.Gs in Midland TX showing three healthy
Avian Biotech DNA-tested Congo Grey chicks with silver plumage and bright red tails
available for nationwide IATA-certified shipping to families in Texas, Florida, and
California seeking captive-bred CITES-documented African Grey parrots from ethical breeders
```

---

### Step 13: Readability Check

**Target metrics:**
- Flesch Reading Ease: 60–70 (8th–9th grade reading level)
- Flesch-Kincaid Grade Level: 8.0–9.0
- Average sentence length: 15–20 words max
- Paragraph length: 3–5 sentences maximum (50–80 words)
- Passive voice: Under 10% of total sentences
- Transition phrase density: 20–30% of paragraphs

**Transition words to use:**
However, Additionally, For example, Specifically, In contrast, As a result, Furthermore, Because of this, Unlike, In addition to, That said, Here's why...

---

### Step 14: Content Delivery Format (Rule 60)

Every full-length page build delivers 4 documents as separate outputs:

**PART 1: Competitor Analysis Report**
- 8–12 competitor breakdowns with gap matrix
- Core keyword gaps identified
- Final outranking strategy

**PART 2: Complete Page Content (Main Document)**
Format requirements:
- Markdown (.md)
- H1–H6 heading structure throughout
- Every section anchor tag: `<a name="section-name"></a>` or `id="section-name"`
- All internal links: `[Link Text](#anchor)` or `[Link Text](/page-url/)`
- All external links: `[Link Text](https://example.com/)` with `target="_blank"`
- Image placeholders: `[INSERT PHOTO: filename.webp]` with alt text
- Newsletter placeholders: `[NEWSLETTER SIGNUP FORM PLACEHOLDER]`
- Map placeholders: `[INSERT MAP: description]`
- Video placeholders: `[INSERT VIDEO: filename.mp4]`

**Document structure:**
```markdown
<a name="top"></a>
# [H1 Title — Primary Keyword Front-Loaded]

[Opening paragraph: entities + aviary location + benefits + form CTA]

👉 [Inquire about available Congo African Grey chicks](/contact-us/)

---

## Quick Navigation — Jump to Any Section
[Table of Contents with all section jump links]

---

<a name="key-takeaways"></a>
## Key Takeaways

[Content]

---

[Continue for all 22+ sections through to contact/navigation]

---

## Quick Navigation — Jump to Any Section (Bottom)
[Navigation grid organized by topic]

[External resource links list]

[⬆ Back to Top](#top)

---
*This page contains [WORD COUNT] total words and incorporates all [#] mandatory sections.*
```

**PART 3: SEO Metadata Sheet**
- 3 meta title options (4-tone system — urgency, comparison, transactional, trust)
- 3 meta description options (standard 155 + extended 290)
- Primary target keyword
- Secondary keywords list (10+)
- LSI keyword groupings (20+)
- Conversational long-tail string collection (30+)
- Schema markup implementation instructions

**PART 4: Linking Strategy Map**
- Complete internal link map (source anchor → target page/section)
- External authority link catalog by category
- Full jump link blueprint (all section anchors)

---

### Step 15: QA Checklist (15-Point Verification)

Before final submission, verify all items:

**Content Completeness:**
- ☐ All required sections present with target word counts achieved
- ☐ Total document 5,000–6,000+ words (or competitor count +1,000 minimum)
- ☐ 6 alternative H1 title variations provided for A/B testing
- ☐ 6 individual bird profiles with: name, age, DNA gender, personality, parents, health status, price, availability, ideal buyer
- ☐ 3 customer testimonials positioned at top, middle, and bottom
- ☐ 3 newsletter signups at top (diet/nutrition section), middle (shipping section), bottom (contact section)
- ☐ 30+ FAQ questions distributed throughout (top, middle, bottom groupings)
- ☐ 150+ named entities naturally integrated (people, locations, medical, brands, stats, credentials)

**Linking Quality:**
- ☐ 50+ contextual internal links (beginning/middle of sentences, varied anchor text)
- ☐ 50+ external authority links (.gov, .edu, .org, avicultural authorities)
- ☐ All anchor targets verified to exist on the site
- ☐ Table of Contents at top with all section jump links
- ☐ Quick navigation at bottom
- ☐ "Back to Top" links at end of each major section

**Search Engine Alignment:**
- ☐ Primary keyword in H1, first 100 words, and at least 5 H2 headers
- ☐ Keyword density 1.5–2% (natural, not stuffed)
- ☐ 3 meta title options + 3 meta descriptions delivered
- ☐ All 6 heading levels (H1–H6) present and sequentially correct
- ☐ CITES + captive-bred + USDA AWA in first 300 words (Rule 44)
- ☐ Variant clearly identified at top (Congo / Timneh / both — Rule 45)
- ☐ 40–60 year lifespan referenced at least once (Rule 46)
- ☐ Voice search questions embedded in H2/H3 headers

**User Conversion Metrics:**
- ☐ Conversational, authentic avicultural tone maintained throughout
- ☐ 15+ form CTA instances (NO phone numbers in body copy — Rule 61)
- ☐ Mobile-optimized layout (short paragraphs, bullet breakdowns)
- ☐ No technical jargon barriers or generic AI-sounding copy
- ☐ Buyer fears addressed: scam/fraud, sick bird, CITES gaps, wild-caught suspicion (Rule 47)
- ☐ Empathy displayed toward common ownership challenges (40-year commitment, lifespan, care)

**Technical Format:**
- ☐ All image placeholders with keyword-rich filenames, 250+ char alt text
- ☐ Video content placeholders present where needed
- ☐ Map embedding placeholders present for shipping/location sections
- ☐ Newsletter signup blocks present
- ☐ Schema markup recommendations provided (FAQPage, Organization, Product, BreadcrumbList)
- ☐ Canonical URL formatted correctly (absolute: `https://congoafricangreys.com/slug/`)

---

## FINAL REMINDERS (Step 10)

This is NOT a template-filling exercise. Every page must:

1. **Actually perform competitor research** across premium avian domains using Firecrawl MCP or Playwright MCP
2. **Analyze existing content gaps** to deliver fundamentally superior, more thorough page layouts
3. **Write with genuine human voice** (conversational warmth, avicultural professional expertise)
4. **Integrate proper nouns and medical entities seamlessly** (avoid forced keyword groupings)
5. **Link with strategic accuracy** (50+ contextual internal links, 50+ validated external sources)
6. **Optimize for natural language processing** (voice query compatibility, clear definition blocks)
7. **Maintain conversion-driven layouts** (form CTAs, real scarcity markers, absolute trust signals)
8. **Uphold flawless E-E-A-T** (demonstrate actual avian science, real-world handling experience, authority)

**Success benchmarks:**
- Outranks existing aviary sites for primary keyword
- Earns citations from AI search engines (Google AIO, Perplexity, Claude)
- Converts curious browsers into qualified African Grey inquiries via form submissions
- Provides genuine education protecting bird health and supporting long-term owner success
- Underscores C.A.Gs ethical commitment to captive-bred, CITES-compliant aviculture

---

## APPENDIX A: Internal Linking Library

Canonical CAG URL list — verify in `src/pages/` before linking. All URLs use trailing slash.

**Core Pages:**
- `https://congoafricangreys.com/`
- `https://congoafricangreys.com/contact-us/`
- `https://congoafricangreys.com/blog/`
- `https://congoafricangreys.com/testimonials/`
- `https://congoafricangreys.com/privacy-policy/`
- `https://congoafricangreys.com/sitemap.xml`
- `https://congoafricangreys.com/about/`

**Bird Listings & Availability:**
- `https://congoafricangreys.com/african-grey-parrots-for-sale/`
- `https://congoafricangreys.com/congo-african-grey-for-sale/`
- `https://congoafricangreys.com/timneh-african-grey-for-sale/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-near-me/`
- `https://congoafricangreys.com/buy-african-grey-parrot-near-me/`
- `https://congoafricangreys.com/buy-african-grey-parrots-with-shipping/`
- `https://congoafricangreys.com/baby-african-grey-parrot-for-sale/`
- `https://congoafricangreys.com/hand-raised-african-grey-parrot-for-sale/`
- `https://congoafricangreys.com/dna-tested-african-grey-for-sale/`
- `https://congoafricangreys.com/captive-bred-african-grey-parrot/`
- `https://congoafricangreys.com/african-grey-breeding-pair-for-sale/`
- `https://congoafricangreys.com/african-grey-parrot-bird-eggs-for-sale-usa/`
- `https://congoafricangreys.com/where-to-buy-african-greys-near-me/`

**Pricing & Adoption:**
- `https://congoafricangreys.com/african-grey-parrot-price/`
- `https://congoafricangreys.com/african-grey-adoption/`
- `https://congoafricangreys.com/african-grey-parrot-adoption-cost/`
- `https://congoafricangreys.com/african-grey-parrot-health-guarantee/`
- `https://congoafricangreys.com/african-greys-for-sale-with-health-guarantee/`
- `https://congoafricangreys.com/trusted-african-grey-parrot-breeders/`
- `https://congoafricangreys.com/african-grey-parrot-breeders-comparison/`

**Care & Guides:**
- `https://congoafricangreys.com/african-grey-parrot-care-guide/`
- `https://congoafricangreys.com/african-grey-care/`
- `https://congoafricangreys.com/african-grey-parrot-guide/`
- `https://congoafricangreys.com/african-grey-parrot-faq/`
- `https://congoafricangreys.com/african-grey-parrot-lifespan/`
- `https://congoafricangreys.com/african-grey-parrot-diet/`
- `https://congoafricangreys.com/best-african-grey-parrot-food/`
- `https://congoafricangreys.com/how-to-tame-african-grey-parrot/`

**Comparison Pages:**
- `https://congoafricangreys.com/african-grey-vs-macaw/`
- `https://congoafricangreys.com/african-grey-vs-cockatoo/`
- `https://congoafricangreys.com/african-grey-vs-amazon-parrot/`
- `https://congoafricangreys.com/african-grey-comparison/`
- `https://congoafricangreys.com/congo-vs-timneh-african-grey/`
- `https://congoafricangreys.com/male-vs-female-african-grey-parrots-for-sale/`

**Trust & CITES:**
- `https://congoafricangreys.com/how-to-avoid-african-grey-parrot-scams/`
- `https://congoafricangreys.com/cites-african-grey-documentation/`
- `https://congoafricangreys.com/african-grey-reviews/`

**Blog Posts:**
- `https://congoafricangreys.com/blog/african-grey-parrot-training/`
- `https://congoafricangreys.com/blog/african-grey-parrot-talking-ability/`
- `https://congoafricangreys.com/blog/is-african-grey-good-for-beginners/`
- `https://congoafricangreys.com/blog/african-grey-parrot-cage-setup/`
- `https://congoafricangreys.com/blog/african-grey-parrot-facts/`
- `https://congoafricangreys.com/blog/african-grey-health-problems/`

**Location/State Pages (sample — full list in `data/locations.json`):**
- `https://congoafricangreys.com/african-grey-parrot-for-sale-new-jersey/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-maryland/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-pennsylvania/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-ohio/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-florida/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-miami/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-orlando/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-texas/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-dallas/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-houston/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-california/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-los-angeles/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-new-york/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-nyc/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-illinois/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-chicago/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-georgia/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-north-carolina/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-virginia/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-arizona/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-massachusetts/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-michigan/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-indiana/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-missouri/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-colorado/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-iowa/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-kentucky/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-oregon/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-washington/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-minnesota/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-wisconsin/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-tennessee/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-bay-area/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-sacramento/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-san-diego/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-austin/`

---

## APPENDIX B: Example Execution

### Example Section: African Grey Temperament & Personality

```markdown
<a name="temperament"></a>
## What is the Real Congo African Grey Temperament? Understanding the Intellectual Companion Parrot

If you're wondering whether a [Congo African Grey](https://www.parrots.org/) matches your daily home life, 
here's what a decade of placements has taught the team at [C.A.Gs aviary](#about-cags): African Greys are 
deeply empathetic, intuitive, highly observant companions who form extraordinary emotional bonds with their 
chosen families. Unlike hyperactive parrot species, Congo African Greys display a **thoughtful, analytical 
baseline behavior**, making them exceptional for [quiet indoor households](#care-environment), remote 
professionals, and experienced avian enthusiasts.

### What Makes the African Grey Personality So Unique?

**Core Temperament Trait Profiles:**
- **Deeply Empathetic:** Greys are incredibly sensitive to human emotions and frequently match the calm 
  or energetic mood of their owners.
- **Incredibly Observant:** They notice subtle environmental changes — learning your daily routine and 
  watching your movements with deep focus.
- **Playful Thinkers:** Beyond simple play, they require interactive, complex mental challenges like 
  puzzle boxes and foraging games.
- **Articulate Communicators:** Renowned for their uncanny ability to use speech contextually, 
  learning voice inflections rather than just mechanically repeating sounds.
- **Adaptable Companions:** Excel in dedicated avian spaces, quiet home offices, or spacious urban 
  apartments when given steady daily interaction.

### African Grey Cognitive Capacity: How Trainable Are They?

Congo African Greys rank at the absolute **pinnacle of avian intelligence**, displaying 
**cognitive problem-solving skills equal to a 5-year-old human child**. According to 
groundbreaking research by [Dr. Irene Pepperberg](https://alexfoundation.org/) with her famous 
African Grey research subject Alex, Congo Greys don't simply mimic — they actively comprehend 
concepts of color, shape, quantity, and abstract difference.

**What this means for your daily training:**
- ✅ **Basic Behaviors:** Most C.A.Gs chicks master "step up", "recall", and target-perch training 
  within 2 weeks using positive reinforcement and clicker techniques.
- ✅ **Speech Acquisition:** Vocabulary development accelerates after the first year. C.A.Gs birds 
  frequently begin talking contextually, saying "Good morning" or asking for "Water" at appropriate moments.
- ✅ **Behavioral Prevention:** Because their brains are highly active, consistent training prevents 
  displacement screaming or territorial biting.

##### PBFD and Behavioral Stability
Avian Biotech disease-screened bloodlines at C.A.Gs have documented zero PBFD transmission across 
500+ placements since 2014 — physical health directly supports behavioral stability in Congo Greys.

###### Can I Leave My African Grey Alone During Work Hours?
Yes, with parameters. A fully [weaned adult African Grey](#how-to-buy) can entertain themselves for 
6–8 hours in a properly enriched environment with foraging cages and ambient enrichment.

---

👉 [Submit an inquiry about our available chicks](/contact-us/) — we respond within 24 hours.

**Continue Reading:**
- [Complete African Grey Environmental & Cage Setup Guide](#care-environment)
- [Advanced Speech and Clicker Training Techniques](#training)
- [Early Aviary Socialization — Parrot Culture at C.A.Gs](#socialization)
- [Compare Congo vs Timneh African Greys](#subspecies-comparison)

**Authoritative External Resources:**
- [World Parrot Trust — African Grey Behavior Registry](https://www.parrots.org/)
- [Alex Foundation Research Library](https://alexfoundation.org/)
```

---

## APPENDIX C: Term Conversion Table (Reference)

When migrating content from dog-breeder templates or MFS reference material, apply these conversions:

| Old Term | CAG Term |
|---|---|
| MFS / Maltipoos For Sale | C.A.Gs / CongoAfricanGreys.com |
| Lawrence & Cathy Magee | Mark & Teri Benjamin |
| Omaha, Nebraska | Midland, TX |
| Puppy / Puppies | Chick / Chicks |
| Litter | Clutch |
| Puppy Culture | Parrot Culture |
| Early Neurological Stimulation (ENS) | Early Neonatal Handling (ENH) |
| AKC Registered | CITES Appendix I documented, USDA AWA licensed |
| Embark DNA Testing | Avian Biotech DNA Testing |
| OFA Certified | AAV certified / avian vet certified |
| Dog food brands (Purina, Hill's, Royal Canin) | Parrot food brands (Harrison's, ZuPreem, Roudybush, Tops) |
| Hypoallergenic | Captive-bred / CITES-documented |
| Dog parks / trails | Avian vet clinics / parrot-friendly environments |
| Maltese, Maltipoo, Blue Staffy | Congo African Grey, Timneh African Grey |
| Breed | Subspecies / variant |
| Grooming (nails, fur) | Feather care, beak maintenance, misting |
| Hip dysplasia, luxating patella | PBFD, Polyomavirus, Psittacosis, Bornavirus |
| $1,200–$1,700 price range | $1,500–$3,500 (CAG) / $1,200–$2,500 (TAG) |
| (402) 555-0123 placeholder | 402-696-0317 — FOOTER ONLY (Rule 61) |
| 17 states served | Nationwide shipping (IATA-approved) |
| Flight Nanny | IATA-certified avian flight nanny |
| Ground transport | Climate-controlled avian ground transit |
| Microchip | Closed leg band / avian DNA certificate |
| Vaccination (DHPP, Nobivac) | DNA disease panel (PBFD, APV, Psittacosis) |
| AKC, BBB, AAHA | CITES, USDA AWA, AFA, AAV |
| BBB A+ Rating | USDA AWA License + AFA Registered Aviary |
| 12-15 year lifespan | 40–60 year lifespan |
| 4-7 lbs weight | 400–500g weight |
| Non-shedding / hypoallergenic | Non-screaming / captive-bred |
| Virginia / state-specific entities | National entities (CAG ships nationwide) |
| Dog parks, local trails | Avian vet databases, AAV vet finder |
| Craigslist puppy scams | Online parrot scams (FTC avian fraud) |
| Phone CTA in body copy | Form CTA — link to /contact-us/ ONLY (Rule 61) |

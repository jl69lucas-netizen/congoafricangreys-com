# SEO Rules — Master Ruleset (50 Rules)
**All agents and skills must read this file before creating or modifying any page.**
Last updated: 2026-05-16 — Consolidated from SEO-RULES-CAG.md + original rules + African Grey–specific additions.

---

## Category A — Brand & Identity

**Rule 1 — Brand Name**
Use **"C.A.Gs - Midland, TX"** as the brand name everywhere — page copy, footer, schema, agent references. Never use "Congo African Greys" as a brand name (too generic). Update Organization schema to match.

**Rule 2 — Breeder Identity**
Owner names are **Mark & Teri Benjamin**, location **Midland, TX**. Content uses first-person breeder voice — not generic "the breeder" or third-person language. This humanizes the brand vs directory-style listings.

---

## Category B — Never-Break Technical Rules

**Rule 3 — H1 Text**
NEVER change H1 text without explicit user approval. H1 is an SEO anchor. Any change requires human sign-off.

**Rule 4 — Canonical href**
MUST be absolute: `https://congoafricangreys.com/slug/` — never relative. A relative canonical causes Google to resolve all pages as canonicalised to `/` — they disappear from search.

**Rule 5 — Schema JSON-LD**
NEVER remove or modify existing schema JSON-LD blocks. Preserve verbatim. Only add to — never subtract.

**Rule 6 — Open Graph Tags**
`og:url`, `og:image`, `og:title`, and `canonical` MUST be absolute URLs. Never relative.

**Rule 7 — CITES Language**
NEVER imply birds are wild-caught. Every page must say "captive-bred" and reference CITES Appendix I documentation. Wild-caught language — even neutral phrasing — is a compliance and trust risk.

**Rule 8 — Image Source Paths**
NEVER use base64 data URIs for images. Always use real `src="/wp-content/uploads/filename.jpg"`. Base64 bloats HTML, kills page speed, and breaks image SEO.

**Rule 9 — Sitemap URLs**
All `<loc>` tags in sitemaps must be absolute: `https://congoafricangreys.com/...`. Exclude: attachment pages, thank-you pages, admin pages.

**Rule 10 — Post-Deploy Checklist**
After every deploy:
1. Submit changed URLs to IndexNow (key: `f8071f0dbdb94257934a690f4a18fa59`)
2. Check GSC for crawl errors within 24 hours
3. Update `docs/reference/top-pages.md` after GSC data refreshes

---

## Category C — Pre-Build Workflow (Mandatory)

**Rule 11 — Competitor Analysis Required Before Every Page**
Before building any page: research the top 5–10 competitors ranking for the primary keyword. Capture:
- Their H1 through H6 patterns
- Exact keyword density and usage count
- Related/variation/LSI keywords they target
- Number of images, types of images, videos used
- Section count and page structure
- Number of words per section

Then run a fan-out keyword query, build keyword distribution section-by-section, create a page outline with topic clusters. **No page is published without this step + user approval.**

**Rule 12 — User Approval Gate**
No page goes live without explicit user approval. After competitor analysis, present the page outline and keyword plan. Wait for "approved" before writing content.

**Rule 13 — Section-by-Section Execution Workflow**
Never write a full page at once. Mandatory workflow:
1. Produce competitor analysis only → STOP, wait for user
2. User approves → produce Sections 1–5 only → STOP
3. User says "Continue" → produce Sections 6–10 → STOP
4. Repeat until all 22 sections complete

Never skip sections. Never merge sections. Never continue without the user's "Continue" command.

---

## Category D — Keyword Strategy

**Rule 14 — Primary Transactional Keyword**
`"african grey parrot for sale [state]"` — must appear in H1, title tag, and URL slug of every location page. This is the #1 revenue keyword cluster.

**Rule 15 — Primary Brand Keyword**
`"C.A.Gs african grey for sale"` and `"congo african grey for sale"` — optimize for top CTR branded and near-brand queries. Top CTR query historically: 11.73% at position 16.

**Rule 16 — Breeding Niche Keywords**
`"african grey breeding pair for sale"` — currently ranking position 8–10 with no dedicated hub page. Needs standalone pages.

**Rule 17 — Informational Keywords**
Male vs female, diet/food, care guides, lifespan, training, talking ability — drives impressions and top-of-funnel traffic. Every informational page needs CTR-optimized meta.

**Rule 18 — Keyword Frequency Table (Per Page)**

| Keyword Type | Target Count | Note |
|---|---|---|
| Primary keyword (exact) | 30–35× | 1–2% density; natural, not stuffed |
| LSI keywords | 20–25× | Synonyms and related terms |
| Long-tail keywords | 15–20× | In headers + paragraphs, conversational |
| Branded keywords (C.A.Gs, Mark & Teri Benjamin, Midland TX) | 10–15× | Throughout |
| Conversational search queries | 23× | Headers/subheaders, voice search |
| Comparison keywords (Congo vs Timneh, CAG vs TAG) | 5–8× | |
| Solution keywords | 5–10× | |
| Related keywords | 10–15× | |
| Transactional keywords | 15× | Buy, for sale, available, pricing |
| **TOTAL** | **≈85–105×** | Hard target per page |

**Rule 19 — Keyword Density Per Section**
Primary keyword: 0.8–1.2% per section. LSI keywords distributed naturally throughout — never force-inserted.

**Rule 20 — Negative Keyword Counter-Positioning**
Three required deflection patterns — every product/available page must address at least one:
- `"wild-caught African Grey"` → Counter with CITES captive-bred documentation proof
- `"African Grey parrot scam"` → Differentiate with USDA AWA license verification + documented buyers
- `"cheap African Grey for sale"` → Position as ethical premium alternative with health and documentation value

---

## Category E — Meta Titles & Descriptions

> **⚠️ CANONICAL META FORMAT — THIS IS THE ONLY SOURCE OF TRUTH.** C.A.Gs uses two long-form meta formats. NEVER ship a generic short title (e.g. "African Grey Parrot Breeder | Congo & Timneh"). Every page picks Format 1 OR Format 2. These caps supersede all prior/agent values (the old 275 / 290 / 155 / 600 numbers are RETIRED). `cag-meta-description-agent.md` must mirror these exactly.

**Rule 21 — Meta FORMAT 1 (Standard Long Title)**
Structure: `[Primary Keyword] | [Number] + [Power Word] | [Long-tail Conversational Query] | C.A.Gs – Midland, TX`
Build order — every element is mandatory:
1. **Begin with the primary keyword** (e.g. `African Grey Parrot Breeder`).
2. **Add a number** where authentic — "7 Reasons", "Top 10", "12 Years".
3. **Include a positive/power word** — Trusted, Healthy, Ethical, Certified, CITES-Documented, USDA-Licensed.
4. **Insert a long-tail conversational query** — `African Grey Parrot Breeder near me that has available parrots`.
5. **End with the brand** — `C.A.Gs – Midland, TX` (or `C.A.Gs` where space-tight, per page).
6. Use `|` separators.
- **Title cap: ≤ 205 characters.**
- **Description cap: ≤ 185 characters** (see Rule 23, Format 1 desc).

**Rule 22 — Meta FORMAT 2 (4-Part Long Title + Tone System)**
For homepage, hubs, and high-intent/high-competition pages.
Format: `[Primary Keyword] | [Conversational Query] | [Comparison / LSI / NLP] | C.A.Gs – Midland, TX Trust Ending`
Still required: a **number** and a **positive/power word** somewhere in the title.
Choose the tone that matches page intent:
- 🔴 **Urgency** — Scarcity, limited clutch availability, act-now (best on PRODUCT/LOCATION pages, NOT the homepage).
- 🆚 **Comparison** — C.A.Gs vs competitor / vs unverified sellers, price/documentation comparison.
- 💰 **Transactional** — Price, reserve now, available today, skip overpriced alternatives.
- 🛡️ **Trust/Health** — CITES proof, DNA-sexed, avian-vet-certified, captive-bred — not just promises.
- **Title cap: ≤ 205 characters.**
- **Description cap: ≤ 300 characters** (see Rule 23, Format 2 desc).
- **Homepage default tone = Comparison + Trust (🆚 + 🛡️). Lead with authority, NOT urgency** — the homepage is top-of-funnel and the #1 buyer fear is scam/fraud.

**Rule 23 — Meta Description (matches the chosen format)**
- **Format 1 description: ≤ 185 characters** — clear, conversational, benefit-driven, single sentence flow.
- **Format 2 description: ≤ 300 characters** — `|`-separated multi-part, for homepage/hubs/high-competition pages.
- Every description MUST include: primary keyword + a long-tail/LSI variation + a trust signal + a CTA.
- Emphasize: CITES Appendix I captive-bred documentation, DNA sexing, avian vet cert, C.A.Gs Midland-TX experience since 2014, nationwide shipping.
- **Worked homepage example (Format 2, 🆚+🛡️ — LIVE):**
  - Title (197): `African Grey Parrot Breeder | Where Can I Buy a Healthy Congo African Grey Near Me? | Captive-Bred C.A.Gs vs Unverified Online Sellers | C.A.Gs – America's Trusted Congo & Timneh Breeder Since 2014`
  - Desc (291): `Trusted African Grey parrot breeder Mark & Teri raise hand-fed Congo & Timneh Greys in Midland, TX | Why families choose captive-bred C.A.Gs over unverified online sellers | Every bird is DNA-sexed, vet-checked, and ships with CITES Appendix I paperwork | Reserve yours — nationwide delivery`

**Rule 24 — Uniqueness**
Every page must have a unique title tag and meta description. No duplicates across the site. Duplicate metas = cannibalization signal to Google.

**Rule 25 — Branded Search Optimization**
Specifically optimize for:
- `"C.A.Gs reviews"` — trust queries
- `"C.A.Gs Midland TX pricing"` — pricing intent
- `"C.A.Gs vs [competitor]"` — comparison intent
- `"is congoafricangreys.com legit"` — trust/scam concern queries

These are actual sales drivers per branded search research.

---

## Category F — Page Structure

**Rule 26 — Section Count**
Default: **22–24 sections per page**. Exact count determined by competitor research (match or exceed their section count) and user approval. Never fewer than 22 without explicit user approval.

**Rule 27 — Word Count (Dynamic)**
Word count = top-ranking competitor's word count + 1,000 words minimum. Target for 22-section pages: **5,000–6,000 words**. Never set a fixed word count without running competitor research first.

**Rule 28 — Header Count Targets**
- H1: exactly **1** per page (hero section only)
- H2: **25–35** throughout (main section headings)
- H3: **40–50** throughout (subsection headings)
- H4: **10–20** (deep sub-section headings — LSI keyword territory)
- H5: **minimum 5** (5–10) — MANDATORY, not optional; carries deep LSI / technical authority terms
- H6: **minimum 5** (5–10) — MANDATORY, not optional; carries voice search / natural language queries
- ALL SIX LEVELS are required on every full-length content page (22+ sections). "H4/H5/H6 as needed" is BANNED. H5 and H6 are not decorative — they are required keyword tiers. **Shipping only 1 H6 or only 4 H5 = automatic FAIL (breeder rule, 2026-06-20).**

**Rule 29 — Table of Contents**
Required on all pages over 1,500 words. Placed after hero + key takeaways section. Uses anchor links to all major sections.

**Rule 30 — Jump Links (Anchor Links)**
Required on every page. Every section must have an HTML anchor ID. Navigation flows from hero to final CTA.
Format: `<a name="section-name"></a>` or `id="section-name"` on the section wrapper.

**Rule 31 — Counter Snippets (After Hero)**
Every page requires 4 counter snippets placed just after the hero section:
- Under 4 words each
- Start with a number or percentage
- Highlight key C.A.Gs facts

African Grey examples:
`40+ Year Lifespan Commitment` / `100% CITES Certified` / `DNA Sexed Guaranteed` / `USDA AWA Licensed` / `Zero Wild-Caught Birds` / `Avian Vet Certified`

**Rule 32 — Contact Form Placement (3× Per Page)**
Inquiry form must appear at least 3 times per page:
1. After hero / counter snippets (top)
2. After trust section / mid-page
3. After FAQ section (bottom)

Never make buyers scroll through 5,000 words to find how to inquire.

**Rule 33 — Formatting Standards**
- ✓ Checkmarks for feature lists
- **Bold** for key facts, prices, important stats
- Bullet lists for features and benefits
- Anchor IDs on every section (for jump links)
- Breadcrumb navigation on all interior pages
- AggregateRating markup on all bird listing/product pages

---

## Category G — Content & Writing

**Rule 34 — Writing DO Rules**
- ✅ Natural, conversational language — write like a trusted friend
- ✅ Answer real questions people actually search
- ✅ Include emotional connection and empathy (40-year commitment is life-changing)
- ✅ Build trust through transparency (pricing, documentation, process)
- ✅ Sound human, warm, and knowledgeable — pass AI detection
- ✅ Guide readers: Curiosity → Trust → Inquiry

**Rule 35 — Writing DON'T Rules**
- ❌ Never keyword stuff: "African grey parrot for sale... our African grey parrots for sale..."
- ❌ Never use robotic language: "This product..." / "This offering..."
- ❌ Never repeat exact phrases unnaturally
- ❌ Never sound like a template or generic AI output
- ❌ Never use aggressive marketing tactics or unverifiable claims

**Rule 36 — African Grey Humor Rules (Apply to ALL Pages)**
Humor must be present on every page — applied thoughtfully, not forced. Four modes:

1. **"The Honesty Policy"** — Relatable breeder/owner humor:
   *"Our African Greys are bred for intelligence, companionship, and the uncanny ability to learn your WiFi password before you do."*

2. **"The Interviewer" Tone** — Frame the inquiry process as the bird vetting the owner:
   *"Are you prepared to be outsmarted daily by a creature that weighs less than 500 grams? Apply to be [Bird Name]'s forever person."*

3. **Punny Wordplay** — Lean into African Grey vocabulary gifts:
   *"50% Congo genetics, 50% Timneh, 100% opinion-having roommate who will outlive your mortgage."*

4. **Comparison Humor** — Highlight traits via unexpected comparisons:
   *"Technically this is a bird. Functionally, it is a sentient 4-year-old with flight capability and a 60-year contract."*

**Rule 37 — Opening Paragraph Formula (Every Section)**
Every section's opening paragraph (1–2 sentences) must contain all four elements:
- **Entity** — who/what (bird name, variant, C.A.Gs, Midland TX)
- **Feature** — measurable fact (weight, age, price, CITES status)
- **Benefit** — what it means for the buyer
- **Purpose** — the deeper reason it matters (40-year bond, family commitment)

Example: *"[Bird Name] is a 12-week-old Congo African Grey (entity) hand-raised at C.A.Gs in Midland, TX, weighing 380g (feature), socialized daily with our family so she bonds naturally and immediately with yours (benefit) — the foundation of a 40–60 year relationship that begins the moment she comes home (purpose)."*

**Rule 38 — Header Variation Requirement**
For every H2 and H3 heading, provide 5 alternative phrasings for A/B testing. Use question-based format when appropriate (voice search optimization). Natural language only — not robotic keyword insertion.

**Rule 39 — Angle-First Rule**
Establish the correct content angle(s) BEFORE creating any section or page. Use blended angles mapped section-by-section.

| Angle | Primary Trigger | Best For |
|---|---|---|
| Transactional | Price & availability | Ready-to-buy visitors |
| Urgency | Limited clutch supply | High-intent browsers |
| Comparison | C.A.Gs vs others | Skeptical, researching buyers |
| Trust | CITES proof, vet cert | First-time bird owners |
| Value | Full documentation package | Research-phase visitors |
| First-Time Owner | Hand-raised, beginner-friendly | New parrot owners |
| Lifestyle | Apartment, seniors, quiet household | Urban/retired buyers |

---

## Category H — AI Snippet Optimization

**Rule 40 — Opening Paragraph Snippet Formula**
Every section opening (50–80 words) must include:
- ✅ Direct answer in first sentence (for Google AI Overview capture)
- ✅ Specific numbers ($1,500–$3,500, 40-year lifespan, CITES Appendix I, DNA sexed)
- ✅ Primary keyword early in the paragraph
- ✅ Entity mentions (C.A.Gs, Mark & Teri Benjamin, Midland TX)
- ✅ Benefit statements (CITES documentation included, avian vet certified, DNA sexed)
- ✅ Trust signals (years breeding, families served, zero wild-caught)

**Rule 41 — Featured Snippet Format Rules**
Three snippet types — build at least one per page targeting the primary keyword:
- **Paragraph snippet**: 40–60 words, direct answer in first sentence, simple language
- **List snippet**: `<ol>` or `<ul>`, 5–10 items, each starts with action verb or bold key term, 1–2 sentences per item
- **Table snippet**: 3–6 columns, 3–8 rows, first column = categories compared, header row with labels, must include data/numbers (not just text)

**Rule 42 — Snippet Technical Requirements**
- Place snippet target content within first 800 words of page
- Use structured data: FAQPage schema for question-format snippets
- Page must load in under 3 seconds
- Content must be mobile-friendly and scannable

**Rule 43 — Advanced Snippet Strategies**
Four patterns to rotate across pages:
1. **Definition + List combo** — definition paragraph immediately followed by a numbered list (captures both snippet types simultaneously)
2. **Question heading → Answer first paragraph** — works for Why/What/How/Are/Is/Can/Should queries; exact question as H2 or H3, direct answer in first 1–2 sentences
3. **Comparison table domination** — for "Congo vs Timneh", "CAG vs TAG", "captive-bred vs wild-caught" queries; comprehensive table beats competitor tables
4. **Step-by-step process capture** — for "How to verify CITES", "How to choose a parrot breeder", "How to prepare for an African Grey"; numbered steps, each with bold action verb

---

## Extended Rules — African Grey–Specific

**Rule 44 — CITES First-300-Words Rule**
Every page must mention "CITES Appendix I", "captive-bred", and "USDA AWA licensed" at least once within the first 300 words. Google E-E-A-T depends on early trust signal establishment.

**Rule 45 — Variant Labeling**
Every page must clearly state at the top whether it covers Congo African Grey, Timneh African Grey, or both. Use correct pricing from `data/price-matrix.json` for each variant. Never mix variant pricing.

**Rule 46 — Lifespan Anchoring**
Every page must reference the **40–60 year lifespan** at least once. This is the #1 differentiator vs any other pet. It reframes the buyer's mindset from "purchase" to "lifetime commitment."

**Rule 47 — Anti-Scam Positioning on Product Pages**
Every bird listing or availability page must address at least 2 of the 5 buyer fears: scam/fraud, sick bird, CITES documentation gaps, wild-caught suspicion, post-sale abandonment.

**Rule 48 — Availability Honesty Gate**
Never use urgency language ("only 2 left", "reserve before they're gone") without first reading `data/clutch-inventory.json`. False urgency is brand-damaging. Only use real scarcity.

**Rule 49 — CITES Image Safety**
No images showing birds in large commercial aviaries, wire cages, or stacked breeding cages — this visually implies wild-capture or commercial farming. All photos must show birds in home environments: on perches, with people, in living rooms, in family settings.

**Rule 50 — Image Intelligence**
Image agent must determine:
- Which sections need original photos vs infographics
- How many images per page (scaled to page length and competitor image count)
- Intelligent placement throughout
- Leave labeled placeholders when images are not yet available

Alt text is **≤190 characters, entity-rich** (per the confirmed 5-element C.A.Gs image metadata set in `skills/image-metadata.md` — the older "exceed 250 characters" figure is RETIRED, corrected 2026-07-11). Image descriptions must exceed **250 words**.

**Rule 50b — Image Keyword Distribution (added 2026-07-11)**
The page's PRIMARY keyword goes in the alt text of the page's PRIMARY image only (hero / first content image). Every other image on the page rotates a DIFFERENT keyword type — secondary keywords, LSI terms, NLP variations, long-tail/PAA phrasings — so the page's image set covers a diverse keyword spread instead of stuffing one term. No two images on a page may share the same alt text. Applies equally to AI-generated images, infographics, and photos. Filenames and alt text use meaningful content words only — no stop-word filler (`of`, `the`, `and`, `for`, `with`) where grammar allows dropping them.

---

## Category I — Page Outline Gate (Mandatory Pre-Build)

**Rule 51 — Page Outline First (No Sections Without Approval)**
Before writing sections 1–5 for ANY page (new build or rebuild), STOP and produce a complete Page Outline document. Do NOT write any section HTML until the user explicitly approves the outline. The outline must contain ALL of the following:

**A. Page Identity**
- Target URL slug
- Primary keyword (exact match)
- Page type (Transactional / Informational / Comparison / Scam Recovery / Species Guide / Care Guide)
- Recommended framework (AIDA, PAS, QAB, EBD, BAB, H-S-S, Inverse Pyramid, Entity-Tree)
- Target word count (top competitor's word count + 1,000 minimum)

**B. Competitor Snapshot (top 5 competitors)**
For each competitor: URL, word count, all H2 topics listed, primary keywords used, special elements present (calculators, quizzes, newsletters, comparison tables, video), unique angles, weaknesses CAG can exploit.

**C. Complete H1–H6 Heading Tree**
List every heading on the page with:
- Heading level (H1/H2/H3/H4/H5/H6)
- Heading text (draft)
- Keyword type (Primary / Secondary / LSI / NLP / Longtail / Comparison / Voice Search)
- Why this heading was chosen (1 sentence)
- Section angle (AIDA, PAS, QAB, EBD, BAB, H-S-S, Inverse Pyramid, Entity-Tree, Trust, Urgency, Comparison, Value, Lifestyle)

**D. Keyword Distribution Table (section by section)**

| Section | Heading | Primary KW | LSI KWs | Longtail KWs | NLP/Conversational | Comparison KWs | Word Count |
|---|---|---|---|---|---|---|---|

One row per section from Hero to final CTA. Total row at bottom must hit 85–105× distribution per Rule 18.

**E. Special Elements Plan**
List every special element on the page with its section position (position determined by competitor research):
- Newsletter signup (top / middle / bottom — minimum 1 required)
- Comparison table
- Price card
- Calculator or quiz
- Counter snippets (4 required after H1 per Rule 31)
- Trust badge bar
- Contact/inquiry form (3 required per Rule 32)
- Video embed
- FAQ accordion
- Table of Contents (required >1,500 words per Rule 29)

**F. Fan-Out Keyword List**
All keyword variations planned for the page: exact match, phrase match, LSI clusters, NLP signals, PAA question phrases, voice search queries, location modifiers, comparison phrases.

**GATE:** User must respond with explicit approval ("Approved", "Continue", or specific changes) before any section is written.

---

**Rule 52 — Strict Heading Hierarchy + Mandatory H1–H6 (All Six Levels Required)**
- Sequential order ONLY: H1 → H2 → H3 → H4 → H5 → H6. Never skip a level.
- WRONG: H2 directly to H4 (skipped H3) — BANNED ❌
- WRONG: H3 directly to H5 (skipped H4) — BANNED ❌
- WRONG: H1 directly to H3 (skipped H2) — BANNED ❌
- RIGHT: H1 → H2 → H3 → H4 → H5 → H6 → back up to H2 for next section ✓
- RIGHT: H2 → H3 → H2 (stepping back up to start a new major section) ✓
- All six levels are REQUIRED on every full-length content page (22+ sections). H5 and H6 are not decorative — they carry deep LSI and voice search keywords respectively.
- **Semantic level map (every page follows this — breeder rule, 2026-06-20):**
  - **H1 → Page topic** (one only)
  - **H2 → Main search intents** (the questions/jobs that bring visitors here)
  - **H3 → Subtopics / keyword clusters**
  - **H4 → Micro-intent answers / PAA coverage**
  - **H5 → Supporting facts / warnings / examples**
  - **H6 → Ultra-specific details / breeder notes / citations**
- H5 purpose: deep LSI / technical authority terms ("PBFD Screening Protocol", "USDA AWA License Explained", "DNA Sexing Methodology")
- H6 purpose: voice search / natural language queries + breeder notes / citations ("Is This Bird Good With Kids?", "What Happens After I Pay a Deposit?", "Source: World Parrot Trust, 2024")
- Every page outline (Rule 51) must include **a minimum of 5 H5 headings AND 5 H6 headings** — no fewer than 5 of each, per page. 1 H6 or 4 H5 will NOT pass.
- **OUTLINE-FIRST APPROVAL GATE (mandatory):** Before creating, editing, or updating ANY page, you MUST first show the breeder the page's **complete H1→H6 outline** (every heading, in render order, level-labeled) and get approval. No page code is written or changed until the outline is approved. Enforced mechanically by `scripts/final_page_audit.py` (`all_six_levels`, `min_h5_5`, `min_h6_5` = hard FAIL).
- Special elements (newsletter, forms, comparison tables, quizzes, calculators, trust badges, video) are REQUIRED on every page. Minimum 3 special elements per page; exact type and placement determined by competitor research per Rule 51 Section E.

---

**Rule 53 — Header/Footer Inheritance: Never Touch, Always Inherit**
- All pages inherit the site header and footer automatically via `src/layouts/BaseLayout.astro`
- Header component: `src/components/Header.astro` — READ ONLY, never write or modify when building pages
- Footer component: `src/components/Footer.astro` — READ ONLY, never write or modify when building pages
- When creating a NEW page: wrap content in BaseLayout, write only what goes between header and footer — start at the hero section
- When REBUILDING an existing page: skip header and footer entirely, edit only from hero section downward
- NEVER copy-paste header/footer HTML into page files — BaseLayout handles injection automatically
- NEVER add a second `<header>` or `<footer>` element inside page content
- If a standalone HTML page (non-Astro) must be created: import the CAG canonical header/footer snippets from `scripts/rebuild_footer.py` — never hand-write them

---

**Rule 54 — Infographic Width Standards (CLS + UX)**

All HTML/CSS infographics built for CAG pages MUST use these `max-width` values on the outer wrapper div. Using the wrong width causes layout shift (CLS penalty) on desktop and wastes the content column width.

| Page type | Wrapper max-width | Desktop height |
|---|---|---|
| Species guide, blog, care guide, article | **760px** — matches `.container-text` | 400px fixed |
| Homepage, location pages, hero sections | **1100px** — matches `.container` | 400px fixed |
| Mobile (≤767px / ≤640px) | 100% width | auto — stacks vertically |

- **Never** use `max-width: 900px` or `max-w-4xl` (896px) — these are legacy values
- The infographic shell is always `width: 100%` inside the wrapper — width is controlled by the wrapper only
- Responsive `@media` query must be included in every infographic to stack content vertically on mobile
- Full spec and responsive CSS patterns: `docs/reference/page-width.md §Infographic Width Rules`

---

**Rule [IMAGE-01]:** Before generating any image or infographic, read `data/image-specs.json` for the current page_type and section. Use the specified `dims`, `source`, and `infographic_type` exactly. Overrides: user instruction > image-specs.json > agent defaults.

**Rule [IMAGE-02]:** Infographic dimensions — 760px wrapper for guide/blog/care pages; 1100px wrapper for homepage/location/hero. Height always 400px desktop, auto mobile. Never use 900px or max-w-4xl (legacy values).

**Rule [IMAGE-03]:** AI-generated portrait images always 1200×2133px native (9:16). CSS display width: 350px. This ratio scales better on mobile than 16:9 landscape.

**Rule [IMAGE-04]:** Every page needs a 1200×630px OG image (separate generation). Never reuse article images for OG without cropping to 16:9.

---

## Category J — Execution Standards

**Rule 55 — Competitor Analysis Output Format**
Every competitor analysis must be delivered as a structured markdown report covering:
- URL, word count, complete H2 topic list, primary keywords used
- Special elements present (calculators, quizzes, newsletters, comparison tables, video)
- Unique angles and ICP (ideal customer profile) they target
- Specific weaknesses CAG can exploit
- "How to outrank them" strategy with 3–5 concrete actions
Output format: markdown table + gap matrix + outranking strategy summary.
Minimum 8 competitors per page: top 3 Google + top 3 Bing + 2 specialized aviaries + 1 authority site (World Parrot Trust or AAV).

**Rule 56 — 10-Category Keyword Fan-Out (MANDATORY Pre-Write)**
Every page requires keyword fan-out across all 10 categories BEFORE writing any section:
1. Transactional (Bottom-Funnel) — buy, for sale, available, pricing
2. Long-Tail Conversational (6+ words) — natural questions, search intent phrases
3. Voice Search Optimized — How, What, Are, Can, Is, Do questions
4. Problem-Solution — fear resolution, outcome-driven phrases
5. Comparison — Congo vs Timneh, CAG vs Macaw, captive-bred vs wild-caught
6. Geographic/Local — cities, states, airport codes, nationwide delivery
7. LSI (Latent Semantic Indexing) — synonyms, related topic terms
8. NLP (Natural Language Processing) — semantic meaning clusters
9. Branded — C.A.Gs, Mark & Teri Benjamin, Midland TX, CongoAfricanGreys.com
10. Review/Testimonial — trust and social proof queries
Minimum 15–20 keywords per category = 150–200 total keyword variations per page.
Full fan-out template: `skills/cag-seo-master-checklist.md` Phase 1 Step 3.

**Rule 57 — 150+ Entity Requirement**
Every full-length page (22+ sections) requires 150+ named entities across 6 categories:
1. **People Entities (10+):** Mark Benjamin, Teri Benjamin, Dr. Irene Pepperberg, Sally Blanchard, Dr. Sarah Walsh DVM
2. **Location Entities (80+):** Midland TX + nationwide cities + airport codes (DEN, LAX, MIA, ORD, JFK, PHX)
3. **Medical/Health Entities (40+):** PBFD, Avian Polyomavirus (APV), Psittacosis, Bornavirus, Hypocalcemia, Aspergillosis, Feather Destructive Behavior
4. **Brand/Product Entities (20+):** Harrison's Bird Foods, ZuPreem, Roudybush, Tops Parrot Food, Avian Biotech DNA Testing
5. **Statistical Entities (20+):** 500+ birds placed since 2014, 40–60 year lifespan, 400–500g adult weight, $1,500–$3,500 CAG / $1,200–$2,500 TAG
6. **Credential/Certification Entities (15+):** CITES Appendix I, USDA AWA License, AFA Registered Aviary, IATA-approved shipping, AAV (Association of Avian Veterinarians)
Entity density target: 8–12 entities per 100 words (naturally integrated — never forced or listed robotically).

**Rule 58 — 3 Anchor Text Strategies**
All pages must use all three anchor text types across internal links:
1. **Exact Match** — anchor text = target page's exact primary keyword; use sparingly (1–2 per page) for hub/category pages
2. **Conversational/Descriptive** — longer phrase that describes the destination naturally within a sentence; Google's preferred NLP pattern; use for most links
3. **Branded** — "C.A.Gs", "Mark & Teri Benjamin's aviary", "CongoAfricanGreys.com"; builds brand authority
Never repeat the same anchor text twice on a page — and never reuse the same anchor for the same target across the site (rotate exact/partial/LSI/natural variants; see skills/internal-link-agent.md Anchor Diversity Ledger). **Link-First rule (2026-07-11):** position ALL internal and external links at the START of the sentence/paragraph — inside the opening words (first clause). Never mid-sentence, never at the end. Sole exception: branded ACTION anchors on CTAs (skills/cag-branded-hybrid-keywords.md).

**Rule 59 — 5-Tier Section Creation Form**
Every section of a 22+ section page must complete the 5-tier form BEFORE writing copy:
- **Tier 1:** Section number + title, target word count (min/max), primary keywords (3–5 with frequency targets)
- **Tier 2:** Content angle (Transactional / Comparison / E-E-A-T / Blended), conversational opening (75–100 words, framework-matched), H2/H3/H4/H5/H6 header structure
- **Tier 3:** Internal links (5–8 per section, varied anchor text), external authority links (1–2 per section)
- **Tier 4:** Geographic/local entities (3–5 per section), authority entities (1–2 per section), trust signals (2–3 per section)
- **Tier 5:** Special elements checklist, image requirements, CTA placement, final QA checklist (15 items)
Full form template: `skills/cag-seo-master-checklist.md` Phase 3 Step 7.

**Rule 60 — 4-Part Content Delivery Format**
Every full-length page build delivers 4 documents as separate outputs:
1. **Competitor Analysis Report** — 8–12 competitors, gap matrix, outranking strategy
2. **Complete Page Content** — full markdown with anchor tags, all 22+ sections
3. **SEO Metadata Sheet** — 3 meta title options (4-tone system), 3 meta descriptions, keyword list (primary + secondary + LSI), schema recommendations
4. **Linking Strategy Map** — complete internal link source→target table, external authority link catalog by category

**Rule 61 — Phone Number Policy (CRITICAL)**
Phone number `281-545-3169` MUST appear ONLY in:
- `src/components/Footer.astro` (footer display — `tel:2815453169`)
- Organization schema telephone field in `src/components/Schema.astro` (E.164: `+12815453169`)
- Individual page Organization schema blocks where a `telephone` field exists
Phone MUST NOT appear in:
- Hero sections, body copy, CTA buttons, mid-page contact sections, or any page content
All body CTAs must point to the inquiry FORM at `/contact-us/` for trackable lead generation.
Acceptable CTA patterns:
- `👉 <a href="/contact-us/">Submit an inquiry</a> — we respond within 24 hours`
- `<a href="/contact-us/" class="cag-btn-primary">Inquire About a Bird</a>`
Phone calls cannot be attributed to specific pages in GA4; form submissions can. This is the tracking foundation.

**Rule 62 — Internal Linking Library**
The canonical CAG internal URL list is maintained in `skills/cag-seo-master-checklist.md` Appendix A.
Consult this list BEFORE writing internal links for any page.
Never invent internal URLs — only link to pages that exist in `src/pages/` or are confirmed in `data/structure.json`.
All internal links must use the relative path format: `/slug/` (with trailing slash).

**Rule 63 — Recommend + Why (ALWAYS, all agents/tasks)**
Whenever any agent or skill presents the user options or choices (meta variants, keyword swaps, design/component options, A/B picks, section placements, framework selection — anything), it MUST:
1. Mark exactly **one** option **(Recommended)**.
2. Explain **WHY**, grounded in real data — GSC, competitor analysis, or the codebase — never "feelings" or vague preference.
3. Stay honest: name the **trade-off / downside** of the recommended pick too.
In `AskUserQuestion`, the recommended option goes **first** with "(Recommended)" appended to its label. A bare list of options with no reasoned recommendation is an incomplete deliverable. Mirrors CLAUDE.md §Non-Negotiable Rules.

**Rule 64 — Authority Citations on Technical/Clinical Terms (E-E-A-T)**
Important technical or clinical terms must be cited **once** to a credible **government / NIH** source (prefer `pmc.ncbi.nlm.nih.gov`) or the **canonical industry authority** — at the sentence where the claim is made, not as a footnote.
- External authority links → **new tab**: `target="_blank" rel="noopener noreferrer"` + the `.home-d`/`.cag-article` `↗` cue. (Internal links stay same-tab — see Rule 62.)
- **Cite a term only once per page** — exact-match repetition reads as over-optimization.
- **Verify HTTP 200 before inserting** (`curl -sI`), and only assert a clinical entity if it is inside the Verified-Claim Ledger (`sessions/2026-06-03-homepage-entity-map.md`).
- The reusable verified-source table (PCR DNA sexing, PBFD, Polyomavirus/APV, African-Grey hypocalcemia, IATA LAR, CITES Appendix I, Alex/cognition) lives in `docs/reference/external-link-library.md §Authority Citations` — pull URLs from there; do not invent new ones.
Proven live on the homepage (4 NIH/PMC + IATA authority links, `src/pages/index.astro`, commits `f8c947f`/`aa095ee`/`8bafd8f`).

---

## Quick Reference — GSC Priority Pages (2026-04-28)

| Page | Impressions | CTR | Position | Action |
|---|---|---|---|---|
| Homepage | 14,915 | 1.88% | ~46 | Optimize meta title/description |
| Breeding pair hub | — | — | 8–10 | Build dedicated hub page |
| Male vs female | 1,788 | 0.73% | — | Rewrite meta |
| Florida product page | 1,446 | 2.90% | 21.8 | Push to page 1 |

Full keyword data: `data/analytics/Queries.html`

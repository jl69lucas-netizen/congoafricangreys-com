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
NEVER imply birds are wild-caught. Every page must say "captive-bred" and reference CITES Appendix II documentation. Wild-caught language — even neutral phrasing — is a compliance and trust risk.

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

**Rule 21 — Standard Meta Title Formula**
Structure: `[Primary Keyword] | [Power Word] + [Number] | [Long-tail Conversational Query] | C.A.Gs - Midland, TX`
- Begin with primary keyword
- Add a number where authentic ("7 Signs", "Top 3 Reasons")
- Include a power word: Certified, Ethical, Trusted, CITES-Documented
- Insert long-tail conversational query
- End with brand: `C.A.Gs - Midland, TX`
- Use `|` separators
- Max 275 characters

**Rule 22 — Extended 4-Tone Meta Title System**
For high-intent pages, choose one of 4 tone variants based on page intent.
Format: `[Primary Keyword] | [Conversational Query] | [Comparison/LSI/NLP] | C.A.Gs Trust Ending`

- 🔴 **Urgency** — Scarcity signals, limited clutch availability, act-now framing
- 🆚 **Comparison** — C.A.Gs vs competitor, price comparison, documentation comparison
- 💰 **Transactional** — Price, buy now, available today, skip overpriced alternatives
- 🛡️ **Trust/Health** — CITES proof, DNA sexed, avian vet certified, not just promises

**Rule 23 — Meta Description**
- Standard: max 155 characters — clear, conversational, benefit-driven
- Extended: up to 290 characters for high-competition pages
- Must include: primary keyword + long-tail query + trust signal + CTA
- Emphasize: CITES documentation, DNA sexing, avian vet cert, C.A.Gs experience

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
- H4/H5/H6: as needed, based on page content + competitor structure

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
- ✅ Specific numbers ($1,500–$3,500, 40-year lifespan, CITES Appendix II, DNA sexed)
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
Every page must mention "CITES Appendix II", "captive-bred", and "USDA AWA licensed" at least once within the first 300 words. Google E-E-A-T depends on early trust signal establishment.

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

Alt text must exceed **250 characters**. Image descriptions must exceed **300 words**.

---

## Quick Reference — GSC Priority Pages (2026-04-28)

| Page | Impressions | CTR | Position | Action |
|---|---|---|---|---|
| Homepage | 14,915 | 1.88% | ~46 | Optimize meta title/description |
| Breeding pair hub | — | — | 8–10 | Build dedicated hub page |
| Male vs female | 1,788 | 0.73% | — | Rewrite meta |
| Florida product page | 1,446 | 2.90% | 21.8 | Push to page 1 |

Full keyword data: `data/analytics/Queries.html`

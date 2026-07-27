# PROMPT PACK — `/african-grey-parrot-adoption-cost/`

**Page 8 of 22 · for-sale transactional cluster · REBUILD mode · 2026-07-27**

The slug is LIVE. On disk it is a thin 331-line interior-style page (11 headings, no H4/H5/H6,
Article + FAQPage schema only). This is a **full rebuild to the for-sale standard**, not a polish.

Everything below is copy-paste ready. Fire the prompts in order. Do not skip a gate.

---

## 0. LOCKED DECISIONS (confirmed by the breeder before this pack was written)

| Decision | Value | Source |
|---|---|---|
| Hero | **Split-Hero C · Dark + 2×2 photo grid** | breeder, 2026-07-27 |
| `african grey parrot price in india` | **NEGATIVE keyword — do NOT target** | breeder, 2026-07-27 |
| Mid-page newsletter | **Required. NEW third variant** (baby page shipped none) | breeder, 2026-07-27 |
| Special element | **True-Cost Calculator** (interactive, vanilla JS) — **differentiated from the existing homepage first-year calculator**, see §6 | breeder, 2026-07-27 |
| OG photos | **8 selected below, all verified unused site-wide** | this pack, §4 |
| Branch | `main` only | CLAUDE.md |

### Why "price in india" is a negative, in one line you can quote in the brief

The page ranks **position 1.0** for `african grey parrot price in india` on **43 impressions and 0 clicks**,
plus `congo african grey parrot price in india` (2) and `cost of african grey parrot in india` (1). We are
a USDA-licensed Texas aviary shipping **domestic US only** on CITES Appendix I captive-bred paperwork. The
query is a permanent 0% CTR ceiling. The play is **counter-positioning, not capture**: one honest H4 stating
we ship the United States only and why the international price figures a reader finds do not transfer,
which deflects the traffic without pretending to serve it.

---

## 1. GLOBAL PREPEND — paste at the TOP of every prompt in this pack

```text
PREPEND — C.A.Gs binding context. Read before doing anything.

You are working in /Users/apple/Downloads/CAG on branch `main`. Never create a feature branch.
Only `main` auto-deploys (GitHub Actions -> Cloudflare Pages); work on any other branch strands at 404.

READ FIRST, THIS SESSION, BEFORE ANY OUTPUT:
  1. CLAUDE.md                        (non-negotiable rules)
  2. PRODUCT.md and DESIGN.md         (brand: strategic + visual)
  3. IMAGE-DESIGNS.md                 (image art direction, §1a uniform sizing, §7 OG framing)
  4. skills/cag-for-sale-page-builder.md
  5. sessions/2026-07-19-for-sale-component-map.md          (tuple ledger - uniqueness is enforced)
  6. docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md
  7. docs/reference/seo-rules.md

PAGE UNDER BUILD: /african-grey-parrot-adoption-cost/
FILE: src/pages/african-grey-parrot-adoption-cost/index.astro   (src/pages is what deploys)
MODE: REBUILD. The existing 331-line file is a thin interior page. Replace it.

BINDING RULES THAT HAVE BEEN BROKEN BEFORE ON THIS CLUSTER:
  - WRITE-FROM-OUTLINE, NEVER-FROM-SIBLING. Open a sibling page only to read its components and CSS.
    Never copy or paraphrase a sibling's sentences. Every paragraph is written fresh from THIS page's
    approved outline. Only the whitelist may match verbatim: shipping line, doc-badge lists, counter
    strip, CITES notice, CTA button labels, real reviews, real page-name link labels.
  - HEADING OUTLINE GATE. Present the complete H1->H6 outline and get approval BEFORE writing any code.
    No skipped levels. All six levels present. Minimum 5 H5 AND 5 H6.
  - TITLE CASE on every H1-H6 (AP style). "If" IS capitalised. FAQ <summary> stays sentence case.
  - LINK-FIRST anchors: the anchor sits in the opening clause of its sentence. Never mid, never end.
  - NEVER publish a visible date. Freshness lives in JSON-LD only.
  - FIRST-PERSON voice: we / us / our / "here at C.A.Gs". Encyclopedic species facts stay neutral.
  - Icons are inline Feather-style SVGs. Never emoji. Never the parrot emoji - use
    /emoji/cag-congo-64.webp and /emoji/cag-timneh-64.webp.
  - VERIFIED-CLAIM LEDGER only. Assertable: USDA AWA licence, CITES Appendix I captive-bred paperwork,
    PBFD + Polyomavirus PCR screening, DNA sexing, avian-vet health certificate, 12+ years aviary,
    4.9 rating / 52 reviews, $185 airport / $350 home / $750+ flight nanny, Midland TX pickup within
    2-3 hours. Nothing beyond this. Never invent a count, a rating, a testimonial or a lab name.
  - CONFIDENCE GATE 97%. If you drop below it mid-build: write finished work to disk, log the open
    question to the session brief's "## Open Flags", ask ONE narrow question with a Recommended answer,
    and keep building everything that is not blocked.
  - RECOMMEND + WHY. Any time you present options, mark exactly one (Recommended), justify it from real
    data, and name its trade-off.
```

---

## 2. GLOBAL APPEND — paste at the BOTTOM of every prompt in this pack

```text
APPEND — output discipline.

  - Ground every number in data/price-matrix.json, data/financial-entities.json,
    data/clutch-inventory.json or docs/reference/credentials.md. Read the file, never recall the value.
  - If a source cannot be fetched, write NOT FETCHED. Never fabricate a competitor metric, a SERP
    position, a word count or a citation.
  - Verify claims about the built page against dist/, never against a source grep.
  - Show your work: for each recommendation give the data behind it and the trade-off against it.
  - Do not commit or push until the step that explicitly says to. When you do commit, `git add` only
    the files you named. Never `git add -A`.
  - End every step with: what changed on disk, what is still open, and the exact next command.
```

---

## 3. THE PROMPTS

### PROMPT 1 — Sprint 0: research (fire first, nothing else)

```text
[PREPEND]

SPRINT 0 - RESEARCH ONLY. Produce no page code. Write findings to
sessions/2026-07-27-adoption-cost-sprint0-research.md.

A. OUR OWN DATA (read locally, do not guess)
   1. docs/research/for-sale-keywords-2026-07.md, section "/african-grey-parrot-adoption-cost/".
      81 queries, 360 impressions. Reproduce the full query table.
   2. assets/1WORKING-ON/FOR-SALE-PAGES/GSC-extracted/Queries.csv and Pages.csv - pull every query
      containing: adoption, adopt, cost, price, how much, cheap, rehome, rescue, fee.
   3. assets/1WORKING-ON/FOR-SALE-PAGES/GSC-extracted/Countries.csv - report the US vs non-US split
      and quantify the India share. This is the evidence base for the negative-keyword decision.
   4. assets/1WORKING-ON/FOR-SALE-PAGES/Fresh-Bing-DADA-as-of-16-07-2026.csv - same keyword sweep.

B. NEGATIVE-KEYWORD CONFIRMATION (breeder has already ruled; you are documenting, not re-deciding)
   `african grey parrot price in india` = 43 impressions, position 1.0, 0 clicks. Plus
   `congo african grey parrot price in india` (2) and `cost of african grey parrot in india` (1).
   Confirm these figures from the CSV and state the counter-positioning line the page will carry:
   we ship the United States only; foreign price figures do not transfer to a US CITES Appendix I
   captive-bred bird. Do NOT build a section targeting India, Pakistan, Nigeria or any non-US market.

C. SERP RESEARCH - both intents, because this page owns both
   Intent 1: "african grey parrot adoption cost", "african grey parrot for adoption",
             "african gray parrot for adoption", "cost to adopt an african grey"
   Intent 2: "african grey parrot price", "african grey parrot cost", "african gray bird price",
             "how much does an african grey parrot cost", "price of african grey parrot"
   For the top 10 organic on each, capture: URL, page type (rescue / breeder / marketplace / editorial),
   word count, H2 outline, schema types, whether prices are actually shown, and every interactive
   element (calculator, quiz, filter, table). Use Firecrawl first. On 403/429 follow the ladder in
   docs/reference/research-blocked-sites.md. Anything un-fetchable is NOT FETCHED.
   Known starting point from docs/research/competitor-african-grey-adoption-2026-06-06.md: the adoption
   SERP is owned by rescue non-profits - thegeorgiaaviary.org 2,158 words, rescuethebirds.org 811,
   birdsandbeaks.org 280 - with no schema depth and no interactive tooling. Re-verify, do not assume.

D. TOOL-GAP CONFIRMATION
   Report explicitly whether ANY ranking competitor on either intent ships a cost calculator. Our
   verified baseline: zero pages on our own 109-page site have one
   (`grep -rl "calculator" src/pages/` returns nothing).

E. REDDIT AND FORUM EVIDENCE
   Real threads only, quoted honestly, per skills/reddit-strategy.md and skills/research-recency.md.
   Target r/parrots and r/Africangrey on: what people actually paid, adoption-fee surprise, rescue
   application rejections, "is $800 a scam", and the true first-year bill. Reddit blocks curl and
   Firecrawl - use a headless browser. Give real URLs. If you cannot fetch a thread, say so.

F. CANNIBALIZATION MAP (mandatory - three of our own pages collide here)
   /african-grey-parrot-price/            - interior, cost-of-OWNERSHIP encyclopedia
   /african-grey-adoption/                - interior, whether and where to adopt, breeder-not-rescue
   /african-grey-parrot-adoption-cost/    - THIS page, transactional
   Read all three. Propose the intent split, the internal-link direction between them, and any header
   or body phrase this page must avoid because a sibling already owns it. The proposed split to test
   against the data: this page owns the DAY-ONE ACQUISITION MONEY DECISION - adoption fee vs breeder
   price vs sub-floor listing, and which reservable bird fits which budget.

G. ENTITY UNIVERSE
   85-112 DISTINCT entities, each used a natural number of times. Money-page bias: adoption fee,
   surrender fee, rehoming contract, deposit, escrow, IATA LAR, live-animal cargo, avian vet wellness
   exam, PBFD, Polyomavirus, PCR, DNA sexing, CITES Appendix I, USDA AWA, Harrison's, Roudybush, TOP's,
   Zupreem Natural, cage gauge, stainless play stand, quarantine, Midland TX, and the six geo targets
   in section H. Brand 5-10x. Never one entity in every sentence.

H. GEO SET - these six, and only these six (verified unused by health-guarantee and baby, real slugs)
   New Jersey, Massachusetts, Minnesota, Missouri, Oregon, Indiana, plus Midland TX pickup.
   Slugs: /african-grey-parrot-for-sale-new-jersey/ -massachusetts/ -minnesota/ -missouri/ -oregon/
   -indiana/. Report each state's rescue density and any adoption-fee figures you can actually source.

I. PAA SET
   Pull real People Also Ask questions for both intents via headless browser. Minimum 15. No invented
   questions.

DELIVERABLE: the research file, plus a one-screen summary with the three biggest gaps we can own.

[APPEND]
```

---

### PROMPT 2 — Sprint 1: two strategies, one blended, distribution matrix

```text
[PREPEND]

SPRINT 1 - STRATEGY AND DISTRIBUTION MATRIX. Still no page code.
Input: sessions/2026-07-27-adoption-cost-sprint0-research.md.
Output: sessions/2026-07-27-adoption-cost-sprint1-blueprint.md.

1. TWO REVERSE-ENGINEERED STRATEGIES, then ONE blended. Mark exactly one (Recommended) with a
   data-grounded why and its named trade-off. The angle the pack proposes as the starting hypothesis -
   test it, do not just accept it:

     ANGLE:        "The Fee Is Not the Cost."
     VOICE LEVER:  fee vs cost / sticker vs total
                   (siblings use: weaned-vs-unweaned, enforceable-vs-unenforceable, hen-vs-cock)
     FRAMEWORKS:   EEBP x Setup-Stat-Reframe x 5 Basic Objections x QAB
                   Setup-Stat-Reframe and the 5-Basic-Objections block are BOTH first use in this
                   cluster. Read skills/framework-library.md and skills/framework-eebp.md.
                   Already spent cluster-wide: PAS, EEAT, FAB, PDB, BAB.

2. SECTION TAXONOMY - 22 sections, each tagged:
     MANDATORY              core to the intent
     COMPETITOR-BASED       a named competitor covers it, with the URL
     SUGGESTED-RECOMMENDED  our moat, with the reason it is a moat
   Every row carries a grounded WHY. No row without evidence.

3. WORD-COUNT SPLIT per section. Page total target 5,300-7,000 words.
   `final_page_audit.py` for-sale band is 3,000-8,000; the shipped cluster measures 5,300-7,000.

4. KEYWORD DISTRIBUTION TABLE, 85-105 total mentions:
     primary 30-35 | LSI 20-25 | long-tail 6+ words 15-20 | branded 10-15 |
     conversational ~23 | comparison 5-8 | solution 5-10 | transactional ~15
   Primary keyword: "african grey parrot adoption cost".
   Secondary cluster, in GSC-impression order: african grey parrot price (32) / african gray bird
   price (28) / african grey price (19) / african grey parrot for adoption (18) / african gray parrot
   for adoption (16) / african grey birds price (13) / african grey parrot cost (7) / how much does an
   african grey parrot cost (4, position 9.5 - closest to page one, treat as a snippet target) /
   african grey parrot price near me (4).
   NEGATIVE, appears nowhere as a target: african grey parrot price in india, and every non-US variant.

5. COMPONENT TUPLE - already resolved against the ledger in
   sessions/2026-07-19-for-sale-component-map.md. Verify each line is still unused, then record it:

     Hero      Split-Hero C dark + 2x2 photo grid. Second use after the egg page, so it ships a
               cag-component-refresh delta, NOT a new shell. The delta: the 2x2 grid is a PRICE LADDER -
               Evie $1,500, Bery $1,700, Roys $2,300, Jins & Jeni $3,500 - ascending left-to-right,
               top-to-bottom, each tile carrying its own price chip. Eyebrow names the live price band,
               where the egg page named the clutch.
     Dial      Dial 1 Clay Progress. Forced: Dial 2 Dark-Aviary is banned under a dark hero.
     Rail      Rail B green ticker. Split-Hero C + Dial 1 + Rail B is an UNUSED triple
               (egg page = C + Dial 1 + Rail A).
     TOC       T2 Chip Cloud (cag-toc-fs:04). FIRST USE in the cluster. Chips grouped
               Money / Routes / Running Costs / Birds.
     Takeaway  K2 Price-Tag Card + K4 Clipboard Checklist. UNUSED pairing. K2 carries the sticker
               price, K4 carries everything the sticker does not cover.
     Table     NEW Table G "True-Cost Ledger" - rows = Day One / Year One / Five Year, columns =
               Rescue-fee route / C.A.Gs breeder route / Sub-floor listing route, plus a
               "what this route does not cover" spine. Table A competitor grid alongside it.
               Already spent: A clay-header, B clay-spine, C outlined matrix, E guarantee ledger,
               F weaning timeline.
     FAQ       FAQ-C dark, refreshed to a LEDGER REGISTER with a clay "$" chip. The egg page used
               FAQ-C as an anti-scam interrogation; hand-raised used it as a forest-green checklist.
               Yours is a register of money questions.
     Avail-B   Faceted by PRICE BAND: $1,500-1,699 / $1,700-2,299 / $2,300-2,599 / $3,500 pair.
               Siblings facet by subspecies, availability posture, sex and age band.
     Newsletter NEW third variant `fs-nl ledger` - see section 5 of this pack. Mid-page, mandatory.
     Tool      `.cost-tool` True-Cost Calculator - see section 6 of this pack.
     Seams     One seam emblem before EVERY section. Target seams == sections.

6. H6 PREFIX SET (unique to this page): "Line Item:" / "From the Ledger:" / "Receipt Note:"
   Spent by siblings: "In Writing:", "From the Vet:", "On File:", "At Week N:", "From the Nursery:",
   "Weaning Log:".

7. EIGHT COUNTER SNIPPETS, under 4 words, number-led, Ledger-verified only:
   $1,500 Floor Price | $185 Airport Tier | $350 Home Tier | 12+ Yrs Aviary |
   100% CITES Papered | 0 Wild-Caught | 24h Reply | 40-60 Yr Span

8. META - extended 3-part for-sale format. Three sets (Educational / Benefit-Solution /
   Transactional-Urgency), one marked (Recommended) with why and trade-off.
     Title: Primary Keyword | Related Conversational Query | Number + Positive Word |
            Brand - LSI/NLP Keywords          (extend toward 280 chars, never past)
     Desc:  Primary Benefit | Secondary Benefit | Trust Signal + CTA        (<=300 chars)

9. INTERNAL LINK PLAN - Link-First anchors, Anchor Diversity Ledger enforced. Do NOT reuse any anchor
   in docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md section 6. Mandatory
   targets: /african-grey-parrot-price/, /african-grey-adoption/, /congo-african-grey-for-sale/,
   /timneh-african-grey-for-sale/, /african-greys-for-sale-with-health-guarantee/, the six geo pages,
   and the six live /available/ birds.

10. EXTERNAL LINKS - minimum 10 across at least 8 domains, from
    docs/reference/external-link-library.md. Cite the specific resource page, not the homepage.
    New tab + the up-right arrow. curl 403 means bot-blocked, not dead - retry with a UA.

11. TWO REAL REVIEWS from data/case-studies.json, not yet used anywhere in the for-sale cluster.
    Already spent: Archie O'Brien NY, Richard Woodard FL, Meredith SC, Jeffrey CO, Joanna CA,
    Anthony WA. If no unused real review exists, say so and ship none. Never invent one.

12. PRE-WRITE DUP GATE. Run scripts/dup_content_audit.py --headers over the PROPOSED headers against
    all seven built for-sale pages plus the comparison cluster. Zero non-whitelist crossover before
    the outline goes to the breeder. Note the lesson: three headings cleared this gate on the
    health-guarantee build and still collided once built. You will run it AGAIN on the built page.

[APPEND]
```

---

### PROMPT 3 — Heading Outline Gate (hard stop; nothing is written until this is approved)

```text
[PREPEND]

HEADING HIERARCHY OUTLINE GATE. Output the complete H1->H6 outline for
/african-grey-parrot-adoption-cost/ in render order, every heading labelled by level. No page code.

RULES, all hard failures:
  - Sequential descent, no skipped levels. H1->H2->H3->H4->H5->H6. Stepping back up is fine.
    H3->H6 or H2->H4 is banned.
  - All six levels present.
  - Minimum 5 H5 AND minimum 5 H6.
  - AP-style Title Case on every heading. Capitalise 4+ letter words and every noun, verb, adjective
    and adverb regardless of length - including Is, Are, Do, Be, Not, Our and If. Lowercase mid-title
    only: a an the and but or nor for so yet at by in of on to as vs per via. Always capitalise the
    first word, the last word, and the word after a colon, question mark or exclamation mark. An em
    dash does NOT force a capital. Hyphenated compounds capitalise each part. Never touch C.A.Gs,
    CITES, USDA, DNA, PCR, IATA, PBFD.
  - Headers are conversational Q&A style: What / How / Is / Can / Where / Why. Two-Keyword Headers
    rule (Rule 28b) applies.
  - Semantic map: H1 topic | H2 search intents | H3 subtopics | H4 PAA micro-intents |
    H5 supporting facts and warnings | H6 breeder notes and citations.
  - The India counter-positioning lives at H4 or H5. It never becomes an H2 and never reads as though
    we serve that market.
  - FAQ questions live in <summary>, are NOT headings, and stay conversational sentence case.

Also give me 5 A/B variants for the H1 and for each major H2, so the breeder picks.

Then run, and paste the output of:
  python3 scripts/dup_content_audit.py --headers

STOP after this. Do not write index.astro until the breeder approves the outline.

[APPEND]
```

---

### PROMPT 4 — Image production (fire in parallel with Prompt 3; details in §4 and §7 below)

```text
[PREPEND]

IMAGE PRODUCTION for /african-grey-parrot-adoption-cost/.
Work from sections 4 and 7 of
sessions/for-sale-research/african-grey-parrot-adoption-cost/2026-07-27-adoption-cost-prompt-pack.md.

PART A - process the 8 selected OG photos exactly as specified in section 4. The masters are named
there with verified dimensions. Every target filename has been collision-checked against public/ and
is free.

PART B - generate the 8 infographics from the prompts in section 7 using
  bash scripts/generate_nb_image.sh "PROMPT" "filename.png" "1600x900"
(GEMINI_API_KEY lives in the gitignored .google-key.)

BEFORE generating anything, run the collision check in section 7 and report the result. If a proposed
name or concept collides with an image already in public/, rename and re-angle it rather than shipping
a near-duplicate.

Rule 50b is a hard gate: the PRIMARY keyword "african grey parrot adoption cost" appears in the alt
text of the HERO image ONLY. Every other image rotates a different keyword type. No two images on this
page share an alt.

[APPEND]
```

---

### PROMPT 5 — Build

```text
[PREPEND]

BUILD /african-grey-parrot-adoption-cost/ section by section from the APPROVED outline and the
APPROVED distribution matrix. Write to src/pages/african-grey-parrot-adoption-cost/index.astro,
replacing the existing 331-line interior page entirely.

COMPONENT FIDELITY - the recurring failure on this cluster. The for-sale kit lives at
assets/1WORKING-ON/FOR-SALE-PAGES/. Read FOR-SALE-PAGES:components-NAMES.md and look at the PNGs in
component-designs/ before you write a line. NEVER import NewsletterV2, the comparison hero, the green
comparison counter strip, or the comparison circular-emblem seam onto a for-sale page.

Ship, in this order:
   1. Split-Hero C dark, 2x2 grid as an ascending PRICE LADDER (Evie $1,500 / Bery $1,700 /
      Roys $2,300 / Jins & Jeni $3,500). ~400px-class height. Hero image baked with a plain
      PIL ImageOps.fit cover crop - NEVER blurfill. Blurfill is for the in-body .sec-img box only.
   2. For-sale outlined stat cards on cream for the 8 counter snippets. Reserve a min-height so the
      strip cannot shift. NOT the green comparison strip.
   3. Dial 1 Clay Progress, compact spec: 196px sidebar in `grid 196px minmax(0,1fr); gap:28px`,
      plain #fff card, radius 16px, padding 12px 10px, shadow 0 3px 12px rgba(60,30,10,.05), sticky at
      calc(var(--hdr) + 16px), max-height calc(100vh - var(--hdr) - 32px), overflow-y auto. Ring 64px,
      inner 50px, number 15px serif, "of N" 7px. The conic ring MUST be live - an IntersectionObserver
      scroll-spy updates --p, highlights the active dial and rail item, and updates the "x of N"
      counter. A static ring reads as broken. Never ship the 92px-ring / gradient-card / 222px version.
   4. Rail B green ticker on mobile, sticky, snap-scroll, scroll-margin offset,
      `scroll-behavior: auto` (smooth cancels #anchor navigation).
   5. T2 Chip Cloud TOC in body, grouped Money / Routes / Running Costs / Birds.
   6. K2 Price-Tag Card early, K4 Clipboard Checklist after the routes section.
   7. `.cost-tool` True-Cost Calculator - full spec in section 6 of the pack.
   8. Table G True-Cost Ledger + Table A competitor grid. Both stack to one card per row at <=640px
      with data-label on each td, thead clip-hidden, first cell as a header band. Max 6 columns.
   9. `.fs-nl ledger` mid-page newsletter - full spec in section 5 of the pack.
  10. Avail-B sticky sidebar filter faceted by PRICE BAND, live counts from data/clutch-inventory.json.
      Cards use the Avail-C v2 clean-card spec: 1:1 photo block with per-bird object-position, small
      dark-green uppercase badge top-left, white info panel, name + clay price on one row, 2-line-clamp
      blurb, always-visible full-width clay pill "View <name> ->". 2x2 grid at <=640px, blurb hidden.
      Ship -440.webp siblings with srcset and sizes="(max-width:980px) 46vw, 210px".
  11. FAQ-C dark refreshed to a ledger register with a clay "$" chip. Questions in <summary>,
      sentence case. Answers must be visible in the DOM, and must match the FAQPage JSON-LD exactly.
  12. Shipping block: Airport Pickup $185, Home Delivery $350, Flight Nanny from $750, plus
      "Pickup in Midland, TX - if you live within 2-3 hours of us". Links the six geo pages.
  13. Blog / resources "Keep reading" section, `.read-cards`, 2-up, REAL thumbnails with a -320.webp
      rung and srcset. Use a named helper, not an inline replace-chain:
          const thumb = (p) => p.replace(/(-760)?\.webp$/, "-320.webp");
  14. `.xsell` cross-sell strip at the END of the reading section - not a new section, so it never
      triggers the Heading Outline Gate. Full border and background tint, never a side stripe. Markup:
          <div class="xsell"><p class="xsell-k">Also from our aviary</p> then one <p> per target.
      Targets and anchors must avoid the spent Anchor Diversity Ledger in the impeccable-lessons doc.
  15. Contact form: dark .form-side panel listing EVERY reservable bird and price from
      data/clutch-inventory.json + data/price-matrix.json, beside a modern form - interest select,
      first name, last name, cell, email, delivery select including Midland pickup, message.
      Every field labelled. idPrefix set so two instances can coexist.
  16. Seam emblem before EVERY section, from /cag-fs-seam-emblem.webp, decorative alt="", lazy, with
      explicit width and height so it cannot shift layout.

WRITING RULES:
  - Every H2, H3 and H4 opens with an EFBP paragraph: Entity + Feature + Benefit + Purpose, 1-2
    sentences, first person.
  - Write every paragraph fresh from the outline. Do not open a sibling page's body copy.
  - Run skills/anti-ai-writing.md over your own draft before calling any section done.
  - CTA to #reserve every 500-700 words. Target 12-15 across the page.

SCHEMA:
  - One Product + Offer per real available bird. AggregateOffer is banned on this page - it is not a
    hub. Sold birds are never InStock.
  - FAQPage entries must have visible on-page answers.
  - Extend the existing JSON-LD graph. Never emit a second BreadcrumbList - <Breadcrumb /> emits its own.
  - Verify all of it in dist/, not in source.

CSS TRAPS, all previously shipped as bugs on this codebase:
  - clamp() and calc() need spaces around + and - or the whole declaration is silently dropped.
  - Never put an <svg> inside CSS content: - it renders as raw text and collapses badge spacing.
  - A scoped `* { margin: 0 }` reset zeroes Tailwind px-/py- utilities. Do not add one.
  - ::before on a <tr> shifts table columns.
  - Small clay text on light uses #b04228. Clay button fills use --clay-ink #c8472f. Dial numerals on
    dark green use #9fc7b0. Never dim text with opacity to hit a shade.
  - Body <p> capped at 70ch. FAQ answers inherit max-width:none by default - cap them.

Commit and push per completed movement. `git add` only the files you name.

[APPEND]
```

---

### PROMPT 6 — QA and deploy

```text
[PREPEND]

FINAL GATE for /african-grey-parrot-adoption-cost/. Run every command. Paste real output. Verify each
finding is REAL before you edit the page - four checkers cried wolf on 2026-07-26 and fixing the pages
would have degraded correct code. If a check is wrong, fix the check and add a regression test.

  git checkout main && npx astro build

  python3 scripts/page_hardening_scan.py african-grey-parrot-adoption-cost
      Zero header-not-title-case. Zero img-no-srcset. Zero opacity-dims-text-contrast.
      Zero clay-small-text-contrast. Zero absolute-hero-not-unwound. Zero smooth-scroll-breaks-anchors.

  echo "seams=$(grep -c 'class=\"seam\"' src/pages/african-grey-parrot-adoption-cost/index.astro) sections=$(grep -c '<section class=\"sec\"' src/pages/african-grey-parrot-adoption-cost/index.astro)"
      House idiom is one seam before every section. seams should equal sections.

  python3 scripts/dup_content_audit.py african-grey-parrot-adoption-cost
  python3 scripts/dup_content_audit.py --headers african-grey-parrot-adoption-cost
      Zero non-whitelist crossover against all 7 built for-sale pages, the comparison cluster, and the
      two colliding interior pages /african-grey-parrot-price/ and /african-grey-adoption/.

  python3 scripts/final_page_audit.py
      PASS required. The slug is already in the FORSALE roster (final_page_audit.py:368). Word band for
      the for-sale profile is 3,000-8,000; aim for the shipped-cluster range of 5,300-7,000.
      all_six_levels, min_h5_5, min_h6_5, no_visible_date, sold_not_instock and no_aggregateoffer are
      the ones this page is most likely to trip.

  python3 -m pytest tests/ -q
  bash scripts/health-sweep.sh
  python3 scripts/generate_sitemaps.py

MEASURE, never assume:
  - Real-ch probe from skills/cag-page-hardening.md section 2y. Measure a real ch by rendering "0" in
    the element's own computed font - never fontSize * 0.5, which over-reports by about 20%. Open
    <details> first or FAQ answers measure zero. Filter on > 75 at mobile; the 45ch floor is meaningless
    at 360px. Narrow is rarely a defect; over-wide is what to chase.
  - Overflow probe at 360 / 768 / 820 / 1024 / 1280, on this page AND the homepage. The footer shipped
    two sitewide breakpoint bugs at 768 and 1024 that only a shared-component sweep caught.
  - CLS on at least 5 runs and read the DISTRIBUTION, not the median. CLS on this site is bimodal and a
    single run already produced one confident wrong attribution. The calculator's result panel is the
    prime new suspect - confirm it has a reserved min-height.

      npx --yes lighthouse@12 http://localhost:4321/african-grey-parrot-adoption-cost/ \
        --only-audits=cumulative-layout-shift --form-factor=mobile --screenEmulation.mobile \
        --throttling-method=simulate --output=json --quiet --chrome-flags="--headless=new" 2>/dev/null \
        | python3 -c "import json,sys;print('%.3f'%json.load(sys.stdin)['audits']['cumulative-layout-shift']['numericValue'])"

MANUAL SUBJECTIVE PASS: first-person voice sweep, anti-AI-writing pass, non-commodity check,
Flesch read, humour at Style-2 dry and never on legal or health copy.

THEN: commit, `git push origin main`, verify the live URL returns 200, and update the tuple ledger row
in sessions/2026-07-19-for-sale-component-map.md and the Anchor Diversity Ledger in
docs/superpowers/sessions/2026-07-26-for-sale-cluster-impeccable-lessons.md.

Finally run the session-closer skill.

[APPEND]
```

---

## 4. OG PHOTOS — 8 selected, verified

Every master below was confirmed present on disk with the dimensions shown, and every target filename
was collision-checked against `public/` and came back **free**. All eight are unused site-wide.

### Global processing spec

- **Landscape and square masters** → `PIL.ImageOps.fit(src, (1408,768), LANCZOS, centering=<per image>)`
  → WebP `method=6`, quality-walk from 82 downward until under 95 KB → ship a `-760.webp` sibling.
- **Portrait masters** → `python3 scripts/reframe_og.py --style blurfill --mobcrop 4:5` from the
  ORIGINAL master, tagged `class="sec-img og-photo og-tall"`, with the mobile full-bleed rule
  `.sec-img.og-tall{width:100vw;margin-left:calc(50% - 50vw);aspect-ratio:4/5;border-radius:0}`.
  Never focal-point-crop a portrait — that is what cuts heads off.
- **On-page:** every in-body image, OG photo and infographic alike, renders in the identical box —
  `.sec-img.inf-img`, `max-width:760px`, `aspect-ratio:1408/768`, `object-fit:cover`, `height:auto`,
  the same on mobile, tablet and desktop. Tune `object-position` per photo; never the box size.
- `srcset="/name-760.webp 760w, /name.webp 1408w" sizes="(max-width:900px) 92vw, 760px"`,
  explicit `width="1408" height="768"`, `loading="lazy"`.
- A low-resolution master upscaled into the box is intentional. Uniform sizing beats pixel-peeping.

### The eight

| # | Target filename in `public/` | Master (verified on disk) | Master size | Treatment | Section |
|---|---|---|---|---|---|
| OG-1 | `african-greys-available-price-bands.webp` | `assets/brand/hero-available-grey-parrots.webp` | 1672×941 | fit, centering (0.5, 0.42) | § Which Bird Sits in Which Price Band |
| OG-2 | `what-the-african-grey-price-covers-roys.webp` | `assets/brand/Roys/What's included with Roys?.webp` | 1536×1024 | fit, centering (0.5, 0.45) | § What the Price Actually Covers |
| OG-3 | `african-grey-forty-year-family-commitment.webp` | `assets/brand/AMIE/amie-african-grey-family-long-term.webp` | 1408×768 | already 16:9 — re-encode only | § The Forty-Year Money Question |
| OG-4 | `living-with-an-african-grey-running-costs.webp` | `assets/1WORKING-ON/FOR-SALE-PAGES/CONGOS-For-Sale/living-with-a-congo-african-grey-family-lifestyle.webp` | 1376×768 | fit, centering (0.5, 0.5) | § What a Grey Costs You Every Year |
| OG-5 | `african-grey-fresh-produce-annual-food-cost.webp` | `assets/brand/BERY/mix-veggetables-for-parrot.webp` | 1024×680 | fit, centering (0.5, 0.5) | § Food and Fresh Produce Line Item |
| OG-6 | `african-grey-toy-replacement-cost.webp` | `assets/brand/BERY/parrot-toy.webp` | 1024×681 | fit, centering (0.5, 0.5) | § Enrichment and Toy Replacement |
| OG-7 | `mark-benjamin-aviary-overhead-midland-tx.webp` | `assets/1WORKING-ON/FOR-SALE-PAGES/CONGOS-For-Sale/Mark-with the parrots.jpg` | 800×600 | fit, centering (0.5, 0.4) | § Who You Are Actually Paying |
| OG-8 | `african-grey-first-thirty-days-setup-cost.webp` | `assets/brand/BERY/bery-first-30-days-home.webp` | 768×1376 | **PORTRAIT → blurfill + `og-tall`** | § The First Thirty Days at Home |

### Hero 2×2 price-ladder grid — reuse, do not regenerate

The Split-Hero C grid uses the four existing bird card images, ordered as an ascending price ladder.
These are product photographs shared across the cluster by design; the *arrangement* is the refresh
delta, and it is unique to this page.

Filenames below were verified present in `public/` on 2026-07-27. Each has a `-400.webp` rung — use it
in `srcset` with `sizes="(max-width:900px) 44vw, 260px"`.

| Tile | Image | Bird | Price chip |
|---|---|---|---|
| top-left | `/evie-timneh-african-grey-female-perched-card.webp` | Evie, Timneh hen | `$1,500` |
| top-right | `/bery-congo-african-grey-cuddly-tamed-card.webp` | Bery, Congo hen | `$1,700` |
| bottom-left | `/roys-congo-african-grey-male-tame-card.webp` | Roys, Congo cock | `$2,300` |
| bottom-right | `/jins-jeni-congo-african-grey-pair-card.webp` | Jins & Jeni, bonded pair | `$3,500` |

Prices are read from `data/clutch-inventory.json` at build time. Never hardcode them.

**Verify before building** — the `*-card.webp` naming is inconsistent across the cluster and three of
these were mis-transcribed once already:

```bash
for f in evie-timneh-african-grey-female-perched-card bery-congo-african-grey-cuddly-tamed-card \
         roys-congo-african-grey-male-tame-card jins-jeni-congo-african-grey-pair-card; do
  printf "%-48s " "$f"; ls public/$f.webp public/$f-400.webp >/dev/null 2>&1 && echo OK || echo MISSING; done
```

### Alt-text distribution — Rule 50b

The primary keyword **"African Grey parrot adoption cost"** appears in the **hero alt only**. Every
other image takes a different keyword type, and no two alts on the page repeat.

| Image | Keyword type |
|---|---|
| Hero | PRIMARY — african grey parrot adoption cost |
| OG-1 | secondary — african grey parrot price |
| OG-2 | long-tail — what an african grey parrot price includes |
| OG-3 | NLP variation — forty year african grey commitment |
| OG-4 | secondary — african grey parrot cost |
| OG-5 | LSI — african grey diet cost |
| OG-6 | LSI — african grey enrichment cost |
| OG-7 | branded — C.A.Gs Midland TX breeder |
| OG-8 | long-tail — african grey first year setup cost |
| INF-1…INF-8 | one distinct long-tail or PAA phrase each — see §7 |

---

## 5. THE NEW MID-PAGE NEWSLETTER — `fs-nl ledger`

**Why a new variant is required.** The `.fs-nl` component ships two variants and both are spent:
`banner` (eggs, health-guarantee, dna-tested) and `split` (eggs, congo, timneh). The hand-raised and
baby pages ship none at all. The breeder has asked for a **new** one on this page, mid-page.

**Concept — the Price-Watch card.** Not "join our list". A budget-shaped ask that only makes sense on a
cost page: the reader names the band they can actually spend, and we email them when a documented bird
lands in it. It converts the exact objection the page has spent 3,000 words on.

### Spec

- Class: `fs-nl ledger`. Sits mid-page, immediately after the Table G True-Cost Ledger section, where
  the reader has just seen the real number and is deciding whether it is reachable.
- Shape: a single cream card, `max-width:760px`, radius 20px, 1px `--border`, warm shadow
  `rgba(60,30,10,.06)`. **Full border, no side stripe** — the side stripe is a standing ban.
- Left edge carries a thin clay **perforation motif** (repeating-linear-gradient dashes), reading as a
  torn ledger stub. That motif is what makes it visually distinct from `banner` and `split` without
  touching the palette.
- Eyebrow: a `<p class="fs-nl-eyebrow">`, not a heading — so uppercase styling is fine and Title Case
  does not apply to it.
- Heading: one H3 in Title Case, inside the section's existing heading run so the outline gate is not
  disturbed. Confirm the level against the approved outline before you place it.
- Body: one sentence. No paragraph.
- **The band selector is the differentiator** — a row of four outlined clay chips wired to the same
  price bands as Avail-B: `Under $1,700` · `$1,700–$2,299` · `$2,300–$2,599` · `Pair · $3,500`.
  Selecting a chip sets a hidden input. Chips are real `<button type="button">` elements, minimum 24px
  target with real spacing, `aria-pressed` toggled.
- Email input + clay pill submit on one row at ≥560px, stacked below. Submit uses `border-radius:12px`
  (form buttons only); the page's other CTAs keep the 50px pill.
- Note line: honest, Ledger-safe. No frequency claim we have not committed to.
- **Reserve a `min-height` on the whole card.** It is above the fold on tall mobile viewports and it
  must not shift.
- Image: one, and it must be unique to this page — the pass-gate requires a unique newsletter image and
  a one-liner title per page, never shared. Use INF-2, the day-one receipt, cropped to the card.

### Accessibility

Label the email input properly, `aria-pressed` on every chip, visible focus ring on chips and input,
and the note line associated via `aria-describedby`. Small clay text on the cream card renders `#b04228`.

---

## 6. THE SPECIAL ELEMENT — `.cost-tool` True-Cost Calculator

**Breeder-selected 2026-07-27, then re-scoped the same day.**

> **CORRECTION — read this before building.** An earlier draft of this pack claimed the calculator was
> a site-first because `grep -rl "calculator" src/pages/*/index.astro` returned nothing. **That check was
> wrong.** It excludes the homepage, which lives at `src/pages/index.astro`, not in a subdirectory.
> The homepage **already ships a working First-Year Cost Calculator** at `src/pages/index.astro:828` —
> bird `<select>`, three delivery radios, cage and vet checkboxes, and a live total rendered as a single
> figure (`$3,835`). The homepage paragraph immediately above it **already links to this page**. The
> correct check is `grep -rl "calculator" src/pages/`, which returns 1.

**Therefore this calculator must differentiate, not duplicate.** The breeder ruled "differentiate it"
on 2026-07-27. Three things the homepage tool does not do, and this one must:

1. **Multi-year projection** — 1 / 5 / 10 / 40 years. The homepage stops at year one.
2. **Ranges, never a point estimate.** The homepage prints one confident number; the underlying data in
   `financial-entities.json` is a set of min/max pairs. Printing `$3,835` implies a precision we do not
   have. Every figure here renders low-to-high.
3. **Route comparison** — rescue fee vs our price vs a sub-floor listing, side by side. The homepage
   tool models one route only.

Anything the homepage tool already answers, this tool links to rather than repeats.

**Named trade-offs, carried forward honestly:**
- Two calculators on one site read as redundant unless they are wired together. **Mandatory:** this page
  links up to the homepage first-year tool, and the homepage tile gets a link down to this one. Neither
  may present itself as the complete answer.
- Every figure is baked in at build time, so the tool drifts the moment a price moves. Mitigation is in
  the spec below.
- It introduces a layout-shift surface, which is why the result panel is height-reserved from first paint.

**Pre-existing drift worth reporting, not fixing here:** the homepage tool hardcodes `Timneh — $1,600`,
but `price-matrix.json` holds `$1,500–$1,600` and Evie is listed at `$1,500`. Log it; do not widen this
page's scope to repair the homepage.

### Inputs

| Control | Options | Source of truth |
|---|---|---|
| Which bird | Timneh $1,500–$1,600 · Congo $1,700–$2,500 · Bonded pair $3,500 | `data/price-matrix.json` |
| How it comes home | Airport pickup $185 · Home delivery $350 · Flight nanny from $750 · Midland pickup $0 | `data/financial-entities.json` → `delivery_options` |
| Setup you already own | none · cage only · cage and stand | `first_year_setup` |
| Years to project | 1 · 5 · 10 · 40 | `lifetime_estimate` |

### Outputs — three figures, always all three

1. **Day One** — bird + delivery + deposit context.
2. **Year One** — Day One + cage $300–$800 + perches and toys $100–$300 + first avian vet visit
   $75–$200 + food $200–$400 + enrichment $150–$300.
3. **Across N Years** — Year One + (N−1) × annual, where annual = food and treats $200–$400 + avian
   vet wellness $75–$200 + toy replacement $100–$250 + unexpected vet $0–$500.

Every figure renders as a **range**, low to high, because that is what the data holds. Never collapse a
range into a single confident number.

### Implementation rules

- Pure vanilla JS, inline, no dependency, no CDN, no framework.
- **Read the JSON at build time in the Astro frontmatter** and interpolate the constants into the
  script. Do not retype them by hand — that is how the numbers drift silently.
- Add a one-line comment in `data/financial-entities.json` and `data/price-matrix.json` noting that
  `/african-grey-parrot-adoption-cost/` renders these figures, so a future price edit knows to rebuild.
- **The result panel carries a fixed `min-height` from first paint.** No content-driven growth. This is
  the single most likely new CLS source on the page and the dna-tested page already cost us three
  rounds of bisection over a layout shift.
- Every control is a labelled native `<select>` or `<input>`. No custom widget. Keyboard-operable end
  to end, visible focus ring, `aria-live="polite"` on the result panel so a screen reader hears the
  recalculation.
- **The full numbers also exist as static text and a real `<table>` elsewhere on the page.** The tool
  illustrates; it never becomes the only place a figure lives. Answer engines cannot execute JavaScript,
  and neither can a reader with JS disabled.
- Motion capped at 0.2s. No count-up animation — it fights `aria-live` and it fakes precision.
- Contrast: clay numerals on cream render `#b04228`; the clay fill on the recalculate control renders
  `--clay-ink #c8472f` with white text.
- No `user-select: none`, anywhere, ever.

---

## 7. INFOGRAPHIC PROMPT PACK — 8 Gemini slots

### 7a. Run this collision check FIRST, before generating anything

This site already carries a dense set of cost and price imagery on `/african-grey-parrot-price/`,
`/african-grey-adoption/` and the comparison cluster. Four of them nearly collided with the concepts
below and the angles were changed on purpose. Re-verify before you spend a credit:

```bash
ls public/ | grep -iE "cost|price|fee|adopt|rescue|route|marketplace|iceberg|receipt|ledger|decade|delivery-option"
```

Names already taken, and the reason each proposed slot is angled away from it:

| Existing in `public/` | Owned by | How the new slot differs |
|---|---|---|
| `african-grey-first-year-cost-breakdown.webp` | `/african-grey-parrot-price/` | INF-2 is **Day One only**, not year one |
| `african-grey-first-year-and-lifetime-cost.webp` | pros-and-cons | INF-4 is a **five-year curve**, two routes plotted |
| `african-grey-real-price-vs-scam-price-gauge.webp` | scam cluster | INF-5 is **what a cheap bird costs you afterwards**, not a gauge |
| `where-to-buy-african-grey-breeder-vs-marketplace-vs-rescue-comparison.webp` | `/where-to-buy-african-greys-near-me/` | INF-3 is **cost stacking per route**, not where-to-buy |
| `african-grey-nationwide-shipping-7-metro-map.webp` | congo, timneh | INF-6 is a **two-tier cost card**, not a map |
| `african-grey-40-60-year-lifespan-timeline.webp` | pros-and-cons | INF-8 is **money by decade**, not life stage |

If any proposed filename comes back occupied, rename and re-angle. Do not ship a near-duplicate.

### 7b. Global spec — applies to every prompt in 7c

- **Generate:** 16:9, 1600×900 px.
  Command: `bash scripts/generate_nb_image.sh "PROMPT" "filename.png" "1600x900"`
  (`GEMINI_API_KEY` lives in the gitignored `.google-key`.)
- **Post-process:** resize to 1408×768, WebP `method=6`, quality-walk 82 → 54 until under 95 KB, place
  in `public/` under the SEO filename, ship a `-760.webp` sibling with
  `srcset="/name-760.webp 760w, /name.webp 1408w" sizes="(max-width:900px) 92vw, 760px"`.
- **On page:** 760px wrapper, `width="1408" height="768"`, `class="sec-img inf-img"`, `loading="lazy"`,
  wrapped in an `<a>` to the internal page named in the slot.
- **Palette, hard rule:** Cream `#faf7f4` ground, Forest Green `#2D6A4F` structure and labels, Clay
  `#e8604c` accents only. Warm grade throughout. Never blue, never clinical.
- **Text inside an image:** short labels and numbers ONLY, and only figures that are already written
  and cited in the page body — `$1,500`, `$1,700`, `$2,300`, `$2,500`, `$3,500`, `$185`, `$350`,
  `$750+`, `40–60 yrs`. Never invent a statistic. Spell-check every word rendered in an image.
- **African Grey accuracy whenever a bird appears:** light silver-grey body, fine pale scalloping,
  **bright red tail** on a Congo or **maroon tail** on a Timneh, bare pale facial mask, solid dark
  beak, pale-yellow adult iris. Never green, never a generic cartoon parrot.
- **A real `<table>` or paired list stays in the DOM.** The image illustrates the numbers; it never
  replaces the text an answer engine has to read.
- **Append this NEGATIVE to every prompt below:**

```text
NEGATIVE: no watermarks, no logos, no brand names, no UI chrome, no generic green cartoon parrot,
no parrot species other than an African Grey, no wild-capture or jungle-trade imagery, no cages that
look like a pet-shop display, no cold blue or clinical lighting, no extra limbs or deformed beaks,
no cluttered background, no long paragraphs of text, no misspelled words, no invented statistics,
no currency other than US dollars, no national flags, no maps of countries outside the United States.
```

### 7c. The eight slots

#### INF-1 · § The Fee Is Not the Cost → `african-grey-adoption-fee-vs-true-cost-iceberg.png`
**Style:** iceberg cross-section. Deliberately not a card and not a chart.
**Links to:** `/african-grey-parrot-price/`
**Alt keyword type:** long-tail — *what an African Grey adoption fee does not include*

> Warm editorial flat illustration on cream `#faf7f4`. A single iceberg seen in cross-section against a
> soft warm horizon. The small tip above the waterline is clay `#e8604c` and labelled "The fee". The
> far larger mass below the waterline is forest green `#2D6A4F` and carries four short stacked labels:
> "Cage", "Vet", "Food", "40–60 yrs". A thin clay waterline rule runs edge to edge. Generous negative
> space, clean line work, no parrot needed, short labels only. [+NEGATIVE]

#### INF-2 · § What You Hand Over on Day One → `african-grey-day-one-money-breakdown.png`
**Style:** a printed receipt with a torn perforated edge. Also the source crop for the `fs-nl ledger`
newsletter card.
**Links to:** `/african-grey-parrot-for-sale/`
**Alt keyword type:** long-tail — *African Grey parrot day one cost breakdown*

> Warm flat illustration on cream `#faf7f4`: a single narrow paper receipt standing vertically with a
> torn perforated top edge and a soft warm shadow. Forest green `#2D6A4F` monospaced line items down
> the receipt reading "Bird", "Delivery", "Papers", each with a clay `#e8604c` dotted leader to the
> right margin. A bold clay total rule at the bottom. Clean editorial line work, plenty of cream around
> the receipt, no parrot, short labels only. [+NEGATIVE]

#### INF-3 · § Rescue, Breeder or a Listing You Found Online → `african-grey-cost-by-acquisition-route-stacked.png`
**Style:** three stacked-bar columns, each bar segmented so the hidden costs sit visibly on top of the
headline fee. Not a where-to-buy comparison.
**Links to:** `/african-grey-adoption/`
**Alt keyword type:** secondary — *African Grey parrot adoption cost by route*

> Warm flat data illustration on cream `#faf7f4`: three vertical stacked bars of different heights,
> evenly spaced, labelled beneath as "Rescue", "Breeder", "Online listing". Each bar is built of
> stacked segments — a solid clay `#e8604c` base segment for the headline fee, then two or three
> forest-green `#2D6A4F` segments above it, lightly outlined, for the costs that follow. Thin baseline
> rule, no gridlines, no axis numbers, short labels only, generous negative space. [+NEGATIVE]

#### INF-4 · § What Five Years Actually Costs → `african-grey-five-year-cost-curve.png`
**Style:** a two-line cumulative curve. Nothing on this site currently uses a line chart.
**Links to:** `/african-grey-parrot-price/`
**Alt keyword type:** PAA — *how much does an African Grey cost over five years*

> Warm minimal line chart on cream `#faf7f4`: two smooth cumulative curves rising left to right across
> a wide frame, with year markers "1" through "5" along a thin forest-green `#2D6A4F` baseline. The
> upper curve is clay `#e8604c`, the lower curve forest green, both with a soft tint filled beneath
> them. Small end-of-line labels only. No axis numbers, no gridlines, no legend box, no parrot.
> Editorial, calm, lots of cream. [+NEGATIVE]

#### INF-5 · § What an $800 Grey Really Costs You → `what-a-cheap-african-grey-really-costs.png`
**Style:** a downstream consequence flow, left to right. Deliberately not a price gauge and not a
scam-warning card.
**Links to:** `/how-to-avoid-african-grey-parrot-scams/`
**Alt keyword type:** solution — *cheap African Grey parrot true cost*

> Warm editorial flow illustration on cream `#faf7f4`: a single clay `#e8604c` rounded tile on the far
> left labelled "$800", with a thin clay arrow flowing right into three sequential forest-green
> `#2D6A4F` outlined tiles labelled "No papers", "Vet bill", "Quarantine". The tiles grow slightly in
> size left to right. Clean line work, one continuous connecting line, no parrot, short labels only,
> generous negative space. [+NEGATIVE]

#### INF-6 · § How Your Grey Gets Home, and What That Costs → `adoption-cost-african-grey-delivery-options.png`
**Style:** three cost cards side by side. Matches the per-page delivery-options pattern the cluster
already uses, angled to cost rather than logistics. Not a map.
**Links to:** `/buy-african-grey-parrots-with-shipping/`
**Alt keyword type:** transactional — *African Grey parrot delivery cost*

> Warm flat illustration on cream `#faf7f4`: three equal rounded cards in a row on a soft warm ground.
> Card one carries a small line-art airplane icon and the label "Airport · $185". Card two carries a
> small line-art delivery van and "Home · $350". Card three carries a small line-art seat-and-carrier
> and "Flight nanny · from $750". Card borders forest green `#2D6A4F`, the price figures clay
> `#e8604c`, icons thin single-weight line art. No parrot, no map, short labels only. [+NEGATIVE]

#### INF-7 · § What the Adoption Fee Does Not Cover → `what-an-adoption-fee-does-not-cover.png`
**Style:** a checklist where the unmet items are struck through. Distinct from every existing checklist
on the site by the strike-through treatment.
**Links to:** `/african-greys-for-sale-with-health-guarantee/`
**Alt keyword type:** LSI — *African Grey rescue adoption fee inclusions*

> Warm editorial illustration on cream `#faf7f4`: a single tall checklist card with six short rows. The
> top two rows carry small forest-green `#2D6A4F` check marks and read "Bird", "Basic history". The
> lower four rows carry thin clay `#e8604c` strike-through rules across their text and read "DNA
> certificate", "PCR screening", "CITES paperwork", "Health guarantee". Clean line work, one card only,
> no parrot, short labels, generous cream margin. [+NEGATIVE]

#### INF-8 · § The Forty-Year Money Question → `african-grey-cost-by-decade-forty-year-timeline.png`
**Style:** a horizontal decade ribbon with four widening money bands. Distinct from the existing
life-stage lifespan timeline.
**Links to:** `/african-grey-parrot-lifespan/`
**Alt keyword type:** NLP variation — *lifetime cost of owning an African Grey*

> Warm flat timeline illustration on cream `#faf7f4`: one long horizontal ribbon running edge to edge,
> divided into four segments labelled beneath as "Yrs 1–10", "11–20", "21–30", "31–40". Each segment is
> a rounded band that grows slightly thicker left to right, alternating forest green `#2D6A4F` and a
> lighter tint of it, with a single clay `#e8604c` marker sitting on the first segment. A thin clay
> rule runs the full width beneath. No parrot, no numbers other than the decade labels, calm editorial
> spacing. [+NEGATIVE]

### 7d. After generation

```bash
python3 scripts/generate_sitemaps.py           # only after the page ships, not after images
```

Hand every produced file to `@cag-image-pipeline`, then to the image-metadata 5-element set —
filename, alt, title, caption, description. None of the five is optional. Confirm against §4 that no
two alts on the page share a keyword, and that the primary keyword appears in the hero alt only.

---

## 8. WHAT THIS PACK DELIBERATELY LEAVES TO RESEARCH

Three things are intentionally unresolved, because deciding them without Sprint 0 data would be
guessing. Each has a proposed default so the build never stalls:

1. **The exact 22-section taxonomy.** Proposed spine is in Prompt 2; the competitor-based rows cannot
   be fixed until the SERP is actually scraped.
2. **The two real reviews.** `data/case-studies.json` must be checked for entries not yet spent in the
   cluster. Default if none exist: ship no new review rather than invent one.
3. **Whether `/african-grey-adoption/` needs a reciprocal edit.** If Sprint 0's cannibalization map
   finds that page competing on cost language, it gets a narrowing edit and a link down to this page.
   Default: link only, no edit.

---

## 9. ONE-SCREEN SUMMARY

| | |
|---|---|
| **Page** | `/african-grey-parrot-adoption-cost/` — page 8 of 22, REBUILD |
| **Angle** | "The Fee Is Not the Cost." |
| **Voice lever** | fee vs cost · sticker vs total |
| **Frameworks** | EEBP × Setup-Stat-Reframe × 5 Basic Objections × QAB (three first uses) |
| **Primary** | african grey parrot adoption cost |
| **Negative** | african grey parrot price in india — counter-position, never target |
| **Tuple** | Split-Hero C dark · Dial 1 Clay · Rail B green ticker · T2 Chip Cloud · K2 + K4 · Table G · FAQ-C ledger register · Avail-B by price band |
| **Geo** | New Jersey · Massachusetts · Minnesota · Missouri · Oregon · Indiana · Midland TX |
| **H6 prefixes** | Line Item: / From the Ledger: / Receipt Note: |
| **Images** | 8 OG photos (§4) + 4 hero price-ladder tiles + 8 new infographics (§7) |
| **New components** | `fs-nl ledger` newsletter · `.cost-tool` calculator · Table G |
| **Word target** | 5,300–7,000 |
| **Gates** | header dup-gate pre-outline AND post-build · `page_hardening_scan.py` · `final_page_audit.py` PASS · seams == sections · CLS on ≥5 runs |

# Spec — /available/ Bird Pages: Expanded SEO/GEO/AEO Rebuild

**Date:** 2026-06-19 · **Status:** Approved design → ready for implementation plan
**Scope:** 6 individual bird pages — Roys (reference build first), then Amie · Bery · Jins & Jeni · Elad · Evie.
**Inputs:** `docs/research/2026-06-19-bird-pages-competitive-analysis.md` (Sprint-0, done) ·
`sessions/2026-06-19-session-brief.md` · `data/clutch-inventory.json` · the live pages in
`src/pages/available/<slug>/index.astro`.

---

## 0 — What changed from the prior locked plan (decisions made this session)

The 2026-06-19 session brief locked **Option A (lean, 700–1,000 words, link-out, newsletter-exempt,
no geo)**. The breeder has revised four of those decisions for this build. These overrides take
precedence over the `cag-bird-listing-page` skill, the `cag-final-page-pass` bird gate, and the prior
brief (user instructions > skills).

| Item | Prior locked rule | **New decision (this session)** |
|---|---|---|
| Page depth | 700–1,000 words | **Competitor MAX visible word count + 1,500 words** (≈2,000–2,800/page) |
| Local/geo | No per-bird geo | **Unchanged — no per-bird geo; link to location pages** (kept, on cannibalization grounds) |
| Newsletter | Exempt (zero) | **One placement, after the FAQ** |
| Logistics | One shipping line | **Full Shipping & Logistics section** — IATA LAR + Avian Flight Nanny + example airport codes (DEN/LAX/MIA/ORD), all six pages |

Everything else from CLAUDE.md Non-Negotiables still binds: first-person voice, shipping cost line,
CITES Appendix I + captive-bred + USDA AWA framing, no visible date (schema only), Verified-Claim
Ledger, prices from data files, no PBFD/Polyomavirus, single `Product`+`Offer` (never `AggregateOffer`),
work on `main`, commit + push after build.

**Consequence the breeder accepted:** going long on six pages that share ~80% of their facts is a
self-cannibalization / duplicate-content risk. The cannibalization firewall (Section 2) is therefore
**mandatory**, and the ~1,500 expansion words on each page must be a *distinct theme* — not the same
padding six times.

---

## 1 — Pipeline (build order)

Roys is the approved reference build; it must pass before any sibling is touched.

0. Competitor research — **done** (`docs/research/2026-06-19-bird-pages-competitive-analysis.md`).
1. **Extend fan-out** to 100+ intent-based variations for Roys **and measure each competitor's visible
   word count** (research doc has angles, not lengths; we need the number to set the target).
2. **Cannibalization map** — confirm Roys's owned intent vs the 5 siblings + `/congo-african-grey-for-sale/`
   + the location pages + `/african-grey-parrots-for-sale/`.
3. **grill-me delta** — confirm only what's changed since yesterday (battery already satisfied).
4. **Outline Roys** — section list + per-section word budget + framework blend + entities + links + schema.
5. **4-Move Loop per section** — Structural Critique → Entities+WHY → Optimized Draft → Topical-Cluster.
   First-person, ledger-only, anti-AI prose.
6. **Build** `src/pages/available/roys/index.astro` — heading sizes / fonts / text scale matched to the
   homepage exactly (Direction D inherited via BaseLayout; do not re-implement the theme).
7. **SEO/AEO/image/a11y/perf pass.**
8. **Preview → breeder approval** (Preview-before-apply).
9. **`python3 scripts/final_page_audit.py --birds`** + subjective manual gate.
10. **Commit + `git push`** (= deploy) → `python3 scripts/generate_sitemaps.py` → deploy-verify.
11. **Batch-apply** the locked pattern to Amie · Bery · Jins & Jeni · Elad · Evie (each its own
    primary/theme/framework/H-structure/snippet/PAA/schema).

---

## 2 — Cannibalization firewall (the spine)

**Rule:** the *unmodified* head terms (`congo african grey for sale`, `timneh african grey for sale`)
stay with the variant/location pages. Each bird owns a *modified* long-tail + a distinct expansion
theme. Shared facts (CITES, weaning, docs list, species bio, aviary, health guarantee) get one clause +
link-out on every page — **never re-expanded** — so duplication stays low even at 2,500 words.

| Bird | Owns this primary | Unique +1,500 theme | Framework |
|---|---|---|---|
| Roys (Congo ♂, $2,300) | **male** congo african grey for sale | high-energy talking Congo · active-family fit · $2,300-vs-$850 | AIDA |
| Amie (Congo ♀ baby, $2,500) | **hand-raised baby** congo african grey for sale | what "fully social-trained" means · bonding / first-30-days | BAB |
| Bery (Congo ♀ 1yr, $1,700) | **female** congo african grey for sale · "under $2000" | value-without-scam · calm-female / quiet-home · lifetime cost | PAS |
| Jins & Jeni (pair, $3,500) | african grey **breeding/bonded pair** for sale | companion vs foundation pair · same-breeder bond | PDB |
| Elad (Timneh ♂, $1,600) | **male timneh** african grey for sale · first serious grey | Timneh-as-first-grey · temperament | EBP |
| Evie (Timneh ♀, $1,500) | **female timneh** african grey for sale · best value | best-value Timneh · female-as-easy-first-grey | QAB |

**Critical fix from yesterday's doc:** Elad and Evie were both assigned bare "timneh african grey for
sale" → they would cannibalize each other. Split applied above: Elad = **male / first-grey**, Evie =
**female / value**. No bird targets a state or city (geo stays with location pages).

---

## 3 — Section architecture (homepage-derived; nothing invented)

Every section traces to the fixed bird-page order, the homepage section inventory, or a competitor
element documented in the research file. No section is invented.

**Mandatory (all six):**
1. Breadcrumb
2. Hero / Bird-Vitals + inquiry CTA
3. **AEO "Bird Snapshot" box** *(competitor-driven — Silvergate price-snippet capture)*
4. TrustBar *(homepage trust pattern)*
5. About <Bird> (archetype / temperament)
6. Health & Documentation
7. Why <Bird> (fit)
8. Pricing & What's Included
9. **Shipping & Logistics** *(expanded: IATA LAR cargo · Avian Flight Nanny · example airport codes)*
10. Parent Birds / Our Aviary
11. FAQ (FAQPage schema, ≥6 Q incl. PAA)
12. **Newsletter (one placement, after FAQ)**
13. Inquiry CTA

**Suggested (only where the bird / SERP justifies):**
- Counter-positioning "why this price vs cheap/overpriced" — *mandatory on Bery + Evie; present on Roys.*
- "Companion vs foundation pair" — *Jins & Jeni only.*
- "Is a Timneh the right first grey?" — *Elad / Evie only.*

**Competitor-driven add-ons:**
- "Real $X vs cheap $850" comparison list (featured-snippet bait).
- Expanded "what's included" list (buyafricangreyparrots / parrotbliss pattern).

---

## 4 — Blended-framework distribution

Page primary framework drives the narrative arc. These blend in regardless of page primary:
- **BLUF** — first ~50 words of *every* section is a direct answer.
- **EBP** — Health & Documentation section (Evidence→Benefit→Proof), always.
- **QAB** — FAQ + pricing micro-answers, always.
- **PAS / PDB** — the counter-positioning section.
- **Page primary** (AIDA / BAB / PAS / PDB / EBP / QAB) — Hero + About + Why.

---

## 5 — Word-count method

For each bird: scrape the top 3–5 competitor pages named in the research doc's SERP list, record visible
word count, take the **MAX**, add **1,500** = that page's word target. Roys's competitor set:
birdbreeders.com · silvergatebirdfarm.com · exoticparrotsplanet.com · mybabyparrot.com ·
graybreedersfoundation.yolasite.com. Record the measured numbers in the implementation plan before drafting.

---

## 6 — Standards (CLAUDE.md + checklist items 1–29, applied)

- **Voice:** first-person plural ("we / us / our / here at C.A.Gs"); Honesty-Policy beat where it fits.
- **Headers:** two-keyword conversational H2s (What/How/Is/Can/Who); full H1–H6, no level skips (Rule 52);
  count demotable headings before quoting an H-count target.
- **Links:** internal same-tab, external new-tab + `rel="noopener noreferrer"` + ↗; mid-sentence, never at
  end; ≤2 external/300w, ≤1/paragraph; verify 200 (retry `-A "Mozilla/5.0"`) and add to
  `docs/reference/external-link-library.md` first. **Proposed new authority targets for link variety:
  AVMA + Lafeber** (verify 200 before use), alongside parrots.org / AAV / CITES / IUCN / USDA APHIS.
  Internal cluster: variant · price · scams · care-guide · best-food · buy-near-me · CITES-docs ·
  congo-vs-timneh · hub · contact + relevant location pages.
- **AEO:** Bird Snapshot box up top; declarative first sentences; bulleted docs + comparison lists;
  atomic, self-contained sections for AI chunking.
- **Schema:** `Product` + single `Offer` (correct availability) · `FAQPage` (visible) · `BreadcrumbList`
  · `Organization`. Extend existing JSON-LD, never duplicate; verify in `dist/` (rendered, not source).
  `dateModified` schema-only — no visible date.
- **Meta:** 4-part title ≤275 chars + benefit-driven description ≤155, ending brand name + LSI/NLP variant.
- **Image SEO (5-element, none optional):** SEO filename · alt ≤190 · `title` · caption+CTA · 250+ word
  description; `loading="lazy"` + explicit `width`/`height`; LCP hero = `fetchpriority="high"` + preload;
  WebP via Python Pillow (not `sips`); <100 KB.
- **Compliance copy:** CITES Appendix I + captive-bred-USA + USDA AWA in first 300 words; 40–60yr lifespan
  referenced once; ledger-only (anything unconfirmed → GAP-FLAG for Mark & Teri, never invented).
- **Conversion:** inquiry/deposit CTA dominant; **no phone number in body** (Rule 61); buyer fears
  addressed (scam, sick bird, CITES gaps, wild-caught suspicion); shipping cost line on the page.
- **Readability / tone:** Flesch 60–70; warm, professional, empathetic; no generic platitudes; anti-AI
  phrasing per `skills/anti-ai-writing.md`.
- **Technical:** WCAG 2.1 AA (skip link, landmarks, labels, focus, contrast `#b04228` small-clay-on-light
  / `#c8472f` clay buttons / white clay-on-green, no `<svg>` in CSS `content:`, ≥24px targets);
  performance reported as warm median-of-3; typography/heading scale matched to the homepage.

---

## 7 — Per-bird specifics (from research doc Parts 1–6)

Featured-snippet target, PAA set, entity coverage, internal-link emphasis, and winning angle for each of
the six birds are specified in `docs/research/2026-06-19-bird-pages-competitive-analysis.md` Pages 1–6 and
are adopted as-is, with the Section 2 primary-keyword splits applied on top (notably the Elad/Evie split).

---

## 8 — Definition of done (per page)

Roys must pass before siblings begin (breeder-gated). A page is done when:
- Word count ≥ (its measured competitor MAX + 1,500); all mandatory sections present.
- Cannibalization firewall holds (owned primary distinct; shared facts linked-out, not re-expanded).
- All H1–H6 present + sequential; primary keyword in H1, first 100 words, ≥5 H2.
- Schema present + correct, verified in `dist/`; canonical absolute; no visible date.
- Image 5-element SEO + dims + lazy (LCP excepted); a11y AA + perf gates pass.
- First-person voice throughout; ledger-only; CITES/USDA/lifespan present; no body phone.
- `final_page_audit.py --birds` passes (or documented WARN); breeder approves preview.
- Committed + pushed to `main`; sitemaps regenerated; deploy-verified 200.

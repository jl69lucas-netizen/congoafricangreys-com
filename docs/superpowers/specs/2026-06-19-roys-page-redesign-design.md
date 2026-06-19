# Roys Page Redesign — Design Spec (2026-06-19)

Reference build for the 6 `/available/` bird pages. Roys is built + previewed + approved first;
the other 5 inherit this system, each with its own framework/angle/H-structure.

## 0. Scope & build order

1. **Checklist → Skill** — convert the bird-page build checklist into a reusable skill
   (`skills/cag-bird-page-build.md`) carrying the new H1–H6 hierarchy + 22-section architecture +
   the visual-companion / distribution-matrix methodology. This governs the build.
2. **Roys reference build** — apply the system below → `npx astro build` → preview → approve.
3. **Batch-apply to 5** — Amie (BAB), Bery (PAS), Jins & Jeni (PDB), Elad (EBP), Evie (QAB);
   each gets its own per-section matrix via the same approval gate before code.

**Depth-model override (decided 2026-06-19):** this depth (≈22 sections, ~3,150 words) **supersedes the
old "lean 700–1,000 word" bird rule** in CLAUDE.md and `cag-bird-listing-page`. Update the
`final_page_audit.py --birds` profile so the auditor's word ceiling/section expectations match.
Locked guardrails stay: single `Product`+`Offer` (never AggregateOffer), no PBFD/Polyomavirus,
sold≠InStock, no visible date (schema only), CITES Appendix I captive-bred USA, Verified-Claim Ledger,
no per-bird geo-targeting (cannibalization guard), first-person plural voice.

## 1. Methodology = the new standard (pending CLAUDE.md TOP rule)

For every page (new or existing): (a) **visual companion** screens for skeleton/hero/component
decisions; (b) a **per-section distribution matrix** approved BEFORE any code — taxonomy, ordered
topic→micro stack, framework/words per section, **A/B/C categories** (A=mandatory core,
B=competitor-match, C=our-moat) each with a grounded *why*; (c) always mark the recommended pick
+ why + trade-off on every option set. Promote to a CLAUDE.md TOP Non-Negotiable Rule at session end.

## 2. Header hierarchy (H1→H6) — passage-level ranking

- **H1** → page topic (the bird)
- **H2** → main search intents (one per section)
- **H3** → subtopics / keyword clusters
- **H4** → micro-intent answers / PAA coverage
- **H5** → supporting facts / warnings / examples
- **H6** → ultra-specific details / breeder notes / citations

Every page uses all of H1–H6. Section headers are conversational Q&A form (What / How / Can / Is / Why).

## 3. Section taxonomy ("what counts as a section")

A **section** = an H2 that earns a TOC jump-link. **Modules** (not counted, no TOC line): Hero,
AEO Snapshot box, the TOC itself, inline trust-badge strips. By this rule Roys = **22 sections**.

## 4. Roys — verified facts (do not drift)

Male Congo African Grey (*Psittacus erithacus*), **4 months**, **$2,300**, hand-raised, DNA-sexed,
CITES Appendix I captive-bred USA, ships nationwide ($185 airport / $350 home), aviary in Midland, TX.
Primary keyword: **congo african grey for sale**. Framework: **AIDA**. Open flag: confirm age if changed.

## 5. Hero + 6-page hero pairing

Roys = **Hero C · Trust-first split + video** (headline + $2,300 + USDA/CITES/DNA badges left, video
preview right; lazy poster + click-to-play, no autoplay). Pairing (1 hero per 2 pages):

- **C Trust-first+video** → Roys + Amie (media-rich Congos)
- **B Dark** → Jins & Jeni + Bery (premium / high-drama)
- **A Editorial** → Elad + Evie (quieter Timneh pair)

## 6. Section architecture + full distribution matrix (APPROVED)

Top modules (above TOC): **Hero (H1)** → **AEO Snapshot box** (40–50w answer) → **TOC** (jump links).

Cat: **A**=mandatory core · **B**=competitor-match · **C**=our moat. All KW/FO/ENT trace to
`docs/research/2026-06-19-bird-pages-competitive-analysis.md`.

| # | H2 (intent) | Fwk | Words | Cat | Keyword (+variations) | Fan-out answered | Entities | Special ★ |
|---|---|---|---|---|---|---|---|---|
| 1 | Is Roys the right African Grey for me? (Key Takeaway) | AIDA | 90 | A | congo african grey for sale; male congo african grey | is a congo african grey a good family bird | Psittacus erithacus; Congo; $2,300; Midland TX | AEO answer box |
| 2 | What is Roys like to live with? (temperament) | EBP | 180 | A | hand-raised congo african grey; affectionate congo grey | how old is Roys / temperament; are male congo greys good pets | hand-rearing; weaning 12–16wk; 4mo | breeder-voice paragraph |
| 3 | Does a male Congo African Grey talk well? | QAB | 150 | B | talking congo african grey | do male congo greys talk well; what age do greys start talking | Psittacus erithacus vocal mimicry; 40–60yr | 40w snippet + link to playing video |
| 4 | Why does Roys cost $2,300 when I see "$850" greys? (counter) | PDB | 240 | C | why is a congo grey $2,300; why are african greys so expensive | is an $850 african grey a scam; congo grey real price | DNA sexing; CITES Appx I; AAV cert; documentation | counter-snippet + "what $850 cuts" list → scams + price pages |
| 5 | What documentation comes with Roys? (H3 cluster) | EBP | 220 | B | congo african grey for sale with papers; congo african grey DNA tested for sale | is Roys DNA sexed/documented; what papers come with a grey | DNA sexing; closed leg band/hatch cert; CITES captive-bred USA; USDA AWA; AAV health cert | itemized docs (H3 each) → cites-documentation + dna-tested pages |
| 6 | What's included when you reserve Roys? | QAB | 120 | A | what comes with a baby african grey | what's included when you buy a grey | weaning status; starter care sheet; doc set | "What's Included" art image |
| 7 | How does Roys compare to our other available greys? | Compare | 190 | C | congo african grey for sale; male vs female congo grey | which african grey is right for me; congo vs timneh | Amie; Bery; Evie; Congo vs Timneh | Compare Table Style E → siblings + congo-vs-timneh |
| 8 | Is Roys a healthy bird? Our health standard | EBP | 160 | B | healthy african grey; african grey health guarantee | is Roys a healthy bird; what health checks do breeders do | Association of Avian Veterinarians; avian vet health cert; 40–60yr | → health-guarantee page (NO PBFD/Polyomavirus) |
| 9 | Who are Roys's parents? (parent birds) | EBP | 130 | C | congo african grey breeder; parent birds | who are Roys's parents; are parent birds on site | aviary Midland TX; hand-rearing; captive-bred | real parent info only (ledger) |
| 10 | What should you decide before buying an African Grey? | BAB | 200 | C | things to know before buying an african grey | is a congo grey a good family bird; are greys hard to care for | 40–60yr lifespan; noise/dust; daily time | honest decision checklist (fit-screening) + Higgsfield image |
| 11 | What's it like to own an African Grey long-term? | BAB | 170 | B | owning an african grey; african grey lifespan | what is it like to own a grey; how long do congo greys live | 40–60 year lifespan; Psittacus erithacus | BAB narrative + Higgsfield image |
| 12 | Reviews — families who brought home a CAGs grey (MID) | Proof | 120 | B | C.A.Gs reviews; congoafricangreys reviews | is congoafricangreys.com legit; breeder reviews | C.A.Gs – Midland TX | review photo #1; NO per-bird Review schema |
| 13 | How do you train an African Grey like Roys? | HowTo | 170 | B | train african grey; how to tame an african grey | how to train a congo grey; how to bond with a grey | hand-rearing; step-up; positive reinforcement | → how-to-tame page + Higgsfield image |
| 14 | What do CAGs recommend feeding African Greys? | QAB | 150 | B | african grey diet; best food for african grey | what do congo greys eat; best pellets for greys | Harrison's; Roudybush; TOP's; Zupreem Natural; calcium/UV-D3 | → diet + best-food pages |
| 15 | Roys's photo & video gallery | Visual | 60 | A | congo african grey photos/video | — | Roys | 2 real videos (eating+playing) + photos, SEO alt |
| 16 | How do you buy Roys? Step-by-step | HowTo | 150 | A | how to reserve an african grey; how to buy a congo grey | how do I buy Roys; how to reserve a baby grey | reservation deposit; payment confirmed at reservation | numbered HowTo steps |
| 17 | Where do CAGs deliver African Greys? (shipping) | QAB | 160 | B | african grey shipping; do you ship african greys | can Roys be shipped; do you ship nationwide | IATA LAR; Delta; United; American; airport $185/home $350 | two-tier cost line → location/city pages |
| 18 | Our credentials (USDA AWA / CITES / DNA / Avian Vet) | EEAT | 80 | A | usda licensed african grey breeder | is congoafricangreys a licensed breeder | USDA Animal Welfare Act; CITES Appx I; DNA sexed; avian vet | KEPT-VERBATIM trust block |
| 19 | Roys — frequently asked questions (6 PAA) | QAB | 260 | B | congo african grey faq | DNA-sexed?; age/temperament?; price/reserve?; shipped?; do males talk?; why $2,300 vs $850? | all of the above | visible FAQ + FAQPage schema |
| 20 | Reviews — more happy CAGs owners (BOTTOM) | Proof | 120 | B | C.A.Gs reviews; happy african grey owners | congoafricangreys testimonials | C.A.Gs – Midland TX | review photo #2 (no per-bird schema) |
| 21 | Why buy from C.A.Gs instead of a marketplace? | EBP | 170 | C | congo african grey breeder vs marketplace | is birdbreeders.com legit; breeder or marketplace | breeder accountability; birdbreeders.com $8,500 anonymity | EBP contrast |
| 22 | Ready to bring Roys home? (CTA + CONTACT FORM) | AIDA | 90 | A | reserve congo african grey; contact african grey breeder | how to contact congoafricangreys; inquire about Roys | C.A.Gs – Midland TX; inquiry/reservation | **cag-inquiry-form.astro (own idPrefix)** + newsletter + homepage link |

Totals: 22 sections · ≈3,150 words (competitor MAX 1,474 → target 2,974). Category tally: **A=7, B=10, C=5**
(C moat = #4 counter-price, #7 sibling comparison, #9 named parents, #10 fit-screening, #21 marketplace-vs-breeder).

## 7. Component variant map

| Section | Component → variant | Note |
|---|---|---|
| Hero | C · Trust-first + video | locked |
| Reviews (mid + bottom) | Testimonials **A · 3-up cards w/ avatar** | same both, real buyer photos |
| Comparison | **Compare Table Style E (1100px)** | homepage-proven |
| Parents | `cag-parent-birds` | existing |
| Gallery | Real-photos grid + video (library 06) | 2 clips |
| FAQ | `cag-faq-acc` accordion (JS) | + FAQPage schema |
| Contact form | `cag-inquiry-form.astro` | own idPrefix |
| Credentials | kept-verbatim trust block | — |
| Snapshot / Key-Takeaway / Counter / TOC | cag-library modules | AEO box, key-takeaway, counter-snippet, jump TOC |
| Navbar / Footer | global Direction D (BaseLayout) | NOT re-built per page |

**Desktop + mobile must match the prototype** (`assets/Roys/…Page Chrome.html` + `…Mobile Components.html`).
Build design-system markup; Direction D applies globally. Mobile uses the library's mobile variants
(floating-pill nav, sticky bottom CTA bar, stacked sections) so the two render equivalently.

## 8. Image map + generation

| File (assets/Roys) | Section |
|---|---|
| ROYS-VIDEO-PLAYING.mp4 + "Roys, the perfect African Grey male…webp" (poster) | Hero (click-to-play) |
| ROYS-VIDEO-EATING.mp4 | Gallery + Food |
| "Roy's vibrant personality profile.webp" | §2 temperament / §3 talking |
| "What's included with Roys?.webp" | §6 what's included |
| "roys-Trust and certification panel.webp" | §5 documentation / §18 credentials |
| Roys4–7.jpeg, 2-years-old…webp | Gallery grid |
| live-animal-african-grey-parrot-shipping.webp | §17 shipping |

**Higgsfield-generate** (per IMAGE-DESIGNS.md style wrapper + negative list): §10 key-decisions,
§11 lifestyle, §13 training. All run through `cag-image-pipeline` (SEO rename, WebP <100KB, alt text).
**Review photos:** not found in `assets/Roys` → fallback to existing buyer photos in `public/`; breeder
to supply the real two later (open flag).

## 9. Internal linking (bidirectional)

Out from Roys → hub `/african-grey-parrots-for-sale/`, variant `/congo-african-grey-for-sale/`,
`/congo-vs-timneh-african-grey/`, `/african-grey-parrot-guide/`, `/cites-african-grey-documentation/`,
`/dna-tested-african-grey-for-sale/`, `/african-grey-parrot-health-guarantee/`,
`/african-grey-parrot-price/`, `/how-to-avoid-african-grey-parrot-scams/`, `/how-to-tame…`, diet/food,
**location/city pages** (shipping section), siblings, and the **homepage**. Add a reciprocal link
**from the homepage → Roys** (and the other available birds) so the link is bidirectional. Anchors woven
mid-sentence: "DNA-tested African Greys", "CITES documentation", "avoid bird scams". Internal same-tab,
external new-tab+↗.

## 10. Schema & compliance

`Product` + single `Offer` (InStock, $2,300) · `FAQPage` (6 Q, visible) · `BreadcrumbList` ·
`Organization`. `dateModified` schema-only — no visible date. No Review schema (no per-bird testimonials).
First-person plural voice; anti-AI-writing pass; ledger-bounded claims only.

## 11. Open flags

- Review photos location (using `public/` fallback meanwhile).
- Confirm Roys' age if changed from "4 months".
- CLAUDE.md TOP rule (visual-companion + distribution-matrix methodology) — add at session end.

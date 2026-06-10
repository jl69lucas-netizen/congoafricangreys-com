# Interior-Page Full-SEO Batch — Live Session Brief

**Started:** 2026-06-06
**Plan:** `docs/superpowers/plans/2026-06-06-interior-pages-full-seo.md`
**Execution:** Subagent-Driven Development (fresh subagent per task + two-stage review)
**Branch:** `main` (push = deploy, per CAG model)

---

## Scope — 18 pages (all `.astro`, edit `src/pages/<slug>/index.astro`)

| # | Slug | Cluster | Type | Length rule | Specialist |
|---|------|---------|------|-------------|-----------|
| 1 | african-grey-parrot-care-guide | A | Care pillar | comp-max + 1000 | content-architect |
| 2 | african-grey-care | A | Care HUB | comp-max + 1000 | content-architect |
| 3 | african-grey-parrot-diet | A | Diet science | comp-max + 1000 | content-architect |
| 4 | best-african-grey-parrot-food | A | Product guide | comp-max + 1000 | content-architect/blog |
| 5 | african-grey-parrot-lifespan | A | Informational | comp-max + 1000 | content-architect |
| 6 | african-grey-parrot-health-guarantee | A | Trust | comp-max + 1000 | trust-signals |
| 7 | trusted-african-grey-parrot-breeders | B | Trust + **About Us** | comp-max + 1000 | about-builder + trust-signals |
| 8 | african-grey-reviews | B | Reviews | ~1200 cap | trust-signals + case-study |
| 9 | captive-bred-african-grey-parrot | B | Attribute | interior-std | variant-specialist |
| 10 | cites-african-grey-documentation | B | CITES edu | comp-max + 1000 | content-architect + external-link |
| 11 | how-to-avoid-african-grey-parrot-scams | B | Scam (fix `yr` bug) | comp-max + 1000 | scam-specialist |
| 12 | african-grey-parrot-guide | C | Species pillar | comp-max + 1000 | species-guide-builder |
| 13 | african-grey-parrot-faq | C | FAQ pillar | comp-max + 1000 | faq-agent |
| 14 | how-to-tame-african-grey-parrot | C | Training | comp-max + 1000 | content-architect |
| 15 | african-grey-adoption | C | Adoption info | comp-max + 1000 | content-architect |
| 16 | african-grey-parrot-price | D | Pricing | comp-max + 1000 | financial-strategist |
| 17 | contact-us | E | Form | SHORT | contact-form-updater |
| 18 | privacy-policy | E | Legal | SHORT | content-architect (light) |

---

## Confirmed distinct-intent map (per 2026-05-22 audit — NO 301s)

- `care-guide` = complete 4,500-word care pillar (housing/diet/health/enrichment).
- `african-grey-care` = **hub** linking to all care spokes; "Hub for all African Grey care resources…" meta.
- `diet` = diet science / what-they-eat (nutrition, safe vs toxic).
- `best-food` = product-recommendation guide (Harrison's, Zupreem, pellet vs seed) — commercial-review intent.
- `african-grey-reviews` = buyer reviews/ratings (Review + AggregateRating).
- `testimonials` / `case-studies` = distinct formats, OUT of batch (no conflict).
- `african-grey-adoption` = emotional/lifestyle framing.
- `african-grey-parrot-adoption-cost` = factual cost tables, OUT of batch (distinct mindset).
- `african-grey-parrot-price` = full pricing/cost pillar.

`trusted-african-grey-parrot-breeders` = **the About Us page** (no separate `/about/`): H-S-S breeder story + AboutPage schema + trust keyword.

---

## Verified facts to seed builds (do NOT exceed the Ledger)

- Owners: **Mark & Teri Benjamin**, family James & Allyson. Aviary in **Midland, TX**, since **2014** (12+ yrs).
- Brand voice: **C.A.Gs** / "C.A.Gs – Midland, TX" — never "congoafricangreys.com". First-person plural.
- Pricing: CAG **$1,500–$3,500**, TAG **$1,200–$2,500** (confirm against `data/price-matrix.json` per page).
- Shipping: **$185 airport / $350 home**, IATA LAR, Delta/United/American (from `data/financial-entities.json` — never hardcode).
- CITES: **Appendix I** (uplisted CoP17, 2017), captive-bred USA, USDA AWA licensed.
- Verified-Claim Ledger ✅ CONFIRMED (USE these — they are site-wide on the homepage): **PCR-based DNA sexing · PBFD (Psittacine Beak & Feather Disease) screening · Polyomavirus (APV) screening · board-certified avian veterinarian** · psittacosis · UV-B/D3 · Maxy (talking Congo) · USDA AWA license · CITES Appendix I captive-bred · hatch certificate · closed band · 72-hr written guarantee. (Source: `.claude/agents/cag-entity-incorporation-agent.md:56` + `sessions/2026-06-03-homepage-entity-map.md:11,103.`) The CLAUDE.md note "never assert PBFD/PCR/board-cert beyond confirmed" means do not EXCEED this set — these specific four ARE confirmed, so name them. Do NOT invent: awards, association memberships, families-served counts, years before 2014.
- **LESSON (health-guarantee build):** an agent stripped "board-certified" + PBFD/Polyomavirus thinking they were unconfirmed → under-claimed + broke site consistency. Fixed. All Cluster B/C/D agents MUST keep these confirmed entities.

---

## Length Targets — FINAL (research 2026-06-06, controller-adjusted)

Raw research → `docs/research/keyword-gap-2026-06-06.md`. Default = competitor-max + 1000. **Overrides** applied where the raw max was inflated by padding/adjacent content (subagent caveats). Targets are floors for genuine depth, never filler quotas.

| Slug | Comp max | FINAL target | Why (if adjusted) |
|------|---------|-------------|-------------------|
| african-grey-parrot-care-guide | 1745 | **2745** | +1000 |
| african-grey-care | 2048 | **3048** | +1000 (hub) |
| african-grey-parrot-diet | 3116 | **4116** | +1000 |
| best-african-grey-parrot-food | 3116 | **2800** | ⬇ override — deepest page is a broad feeding guide; focused brand-review depth, not 4116 padding |
| african-grey-parrot-lifespan | 3497 | **4497** | +1000 |
| african-grey-parrot-health-guarantee | 545 | **1545** | +1000 — value = documentation specifics, not padding |
| trusted-african-grey-parrot-breeders | 587 | **~2200** | ⬆ override — it's the About Us page (story + credentials + trust); out-depth thin competitors |
| african-grey-reviews | 8311 | **~1200 cap** | ⬇ HARD override — real testimonials only; 8311 is a padding wall, do NOT chase |
| captive-bred-african-grey-parrot | 3322 | **~2400** | override — interior-standard; raw max is advocacy journalism, not commercial; commercial gap |
| cites-african-grey-documentation | 857 | **1857** | +1000 — depth via CITES Appendix-I specifics |
| how-to-avoid-african-grey-parrot-scams | 3518 | **4518** | +1000 |
| african-grey-parrot-guide | 3344 | **4344** | +1000 (species pillar) |
| african-grey-parrot-faq | 1366 | **2366** | +1000 |
| how-to-tame-african-grey-parrot | 4140 | **3300** | ⬇ override — raw max is broad-behavior, not pure taming; focused step-by-step |
| african-grey-adoption | 2158 | **3158** | +1000 |
| african-grey-parrot-price | 2299 | **3299** | +1000 |
| contact-us | — | SHORT | utility, not benchmarked |
| privacy-policy | — | SHORT | legal, not benchmarked |

**Schema-gap wins (from research):** FAQPage (many competitors lack it), Review/AggregateRating (reviews + bird cards), Article + BreadcrumbList (table stakes — ensure on all).

---

## Open Flags

*(Clarification-Checkpoint target — log any <97% question here with finished work written first.)*

- **[NEEDS USER INPUT] Pellet brand we actually feed.** best-food build could not verify which brand(s) Mark & Teri feed (old page claimed Harrison's + Zupreem; no record in business-DNA/ledger). Build now says "a formulated, dye-free pellet base; bird goes home on its current food" — TRUE and safe. If you confirm the real brand, we add a first-person endorsement on `/best-african-grey-parrot-food/`.
- **[RESOLVED] FAQ toggle script bug.** care-guide + diet shipped without the `.cag-faq-q` click handler (items 2+ stuck closed). Fixed + redeployed (commit 8c0d975). LESSON: every page using `cag-faq-acc` MUST include the inline toggle `<script is:inline>` before `</BaseLayout>` AND verify `dist` contains `querySelectorAll('.cag-faq-q')`. Baked into remaining dispatch prompts + verification.
- **[NEEDS USER DECISION] AggregateRating 4.9 / 127 reviews — is 127 real?** Site-wide (homepage `orgSchema`), now also on reviews + trusted-breeders pages. If you do NOT have ~127 genuine reviews, this is a fabricated rating count (Google rich-result penalty risk + trust issue) and must be corrected site-wide to the real number. We did NOT invent it — it's pre-existing on the homepage. Tell me the real review count (or "remove the count") and I'll fix it everywhere.
- **[RESOLVED] Old reviews page had FABRICATED testimonials live** (Keith Harmon, Jane Lefevre, Math Crittenden, Laura Cornett, Hermelinda Graham) + fake `reviewCount:47`. Removed in rebuild; reviews page now uses only the 6 real homepage buyer reviews. (If other un-rebuilt pages carry these fake names, flag for cleanup.)
- **[RESOLVED — keep inline, do NOT use TrustStats] health-guarantee credential block.** Rebuild brief asked to use `TrustStats` for the 4-card trust block (USDA AWA · CITES · DNA-Sexed · Health Guarantee). VERIFIED unusable here: (a) `TrustStats.astro` **hardcodes** its 4 items (3-day guarantee / DNA-sexed / Ships-to-50-states / CITES) with NO props to override → cannot render "USDA AWA"; (b) it uses `bg-warm` + `font-display`, and **neither token exists** in `global.css` (Tailwind v4 `--color-*` map) → transparent icon tiles + non-serif titles = visually broken. Kept the existing purpose-built inline 4-card block: delivers the brief's exact 4 cards with only defined tokens, design-system-correct, AA-safe. Satisfies brief INTENT. (Future fix to make TrustStats reusable: add `--color-warm` + `--font-display` tokens and make `items` a prop.)
- **[RESOLVED — health-guarantee, 2026-06-07] Word count brought into band by no-fact-loss tightening.** The session-built rebuild measured ~2,353 page-prose words (~3,021 article-wrapper incl. components) vs. this brief's own FINAL target of **1,545** (band 1,310–1,775, line 73 above). Tension with "preserve facts/terms, don't delete… depth = documentation specifics" was resolved by cutting **wordiness/redundancy only** — tightened the 8 FAQ answers and the body section intros/closers that restated facts already in the BLUF + credential cards. **Zero facts, terms, links, schema, or FAQ questions removed**; every guarantee term still PRESERVED VERBATIM (72-hr window, 24-hr shipping report, 5–7 day new-owner visit, replacement/refund at our discretion, no buyer's-remorse returns, DOC1–4 packet, 48–72h independent vet exam). Final word count recorded in the page report + verified in `dist`. Build + all structural gates pass (Article + FAQPage + BreadcrumbList schema, FAQ toggle = 1, 0 escaped-svg, absolute canonical, shipping line ×6).

---

## Progress Log

- 2026-06-06: Plan written + corrected (no 301s; trusted-breeders = About Us). Task list created (21 tasks). Phase 0 started.
- 2026-06-07: `african-grey-parrot-health-guarantee` rebuilt to interior standard (trust + documentation). Kept inline credential block over TrustStats (token + hardcoded-items breakage — flag above). Tightened prose to land in the 1,310–1,775 band with no fact loss. Committed (not pushed).
- 2026-06-10: **5.4 african-grey-adoption rebuilt to interior standard.** Emotional/lifestyle framing with the breeder-honesty frame ("we are a breeder, not a rescue" — disclosed in H1 + hero lead + BLUF item 1). Honest both-roads comparison, genuine adoption avenues (Phoenix Landing + Avian Welfare Coalition, both verified 200 + added to external-link-library), verify-before-adopting (CITES paperwork / independent vet screen / behavioral history), rehomed-Grey 3–12 mo re-taming (links taming guide), captive-bred-better-fit + our process. NO cost tables (adoption-cost page owns those — linked instead). Article + FAQPage (7 Q, mirrored) + component BreadcrumbList ×1; FAQ toggle verified; 0 escaped svg; title 202 / desc 300; 3,394 prose words (3,711 incl. component chrome) — inside 2,684–3,632 band. Not committed (orchestrator verifies + commits).
- 2026-06-10: **Cluster B complete (4.1–4.5).** 4.4 cites-african-grey-documentation rebuilt (commit 149bfe7 — Appendix-I education, 4-doc packet, Article+FAQPage+Breadcrumb, ~2,300 words, slightly over 2,135 ceiling — fact-dense, flagged not trimmed). 4.5 how-to-avoid-african-grey-parrot-scams rebuilt + `yr is not defined` bug FIXED (commit 2ee6235 — dead year/hamburger stub replaced with FAQ toggle; all 5 inline scripts node-checked clean; CLAUDE.md Known Issue cleared). Scams measures ~8,545 words incl. table/list chrome vs 5,196 ceiling — page was already 3,518 pre-rebuild; preserved + grew per "floors not ceilings", flagged for orchestrator/user word-count call.
- 2026-06-10: **Cluster C complete (5.1–5.4), all live 200.** 5.1 african-grey-parrot-guide (found ~90% built uncommitted from a dead session — verified, trimmed meta to F2 caps, deduped double BreadcrumbList, 4,484 words, commit 9ebeb1b). 5.2 african-grey-parrot-faq (25-Q QAB pillar, 6 topic groups, 2,638 words, b6ea674). 5.3 how-to-tame (7-step HowTo schema spine, 3,568 words, refocused per ⬇ override, 747aadb). 5.4 african-grey-adoption (honest breeder-not-rescue frame, 3,394 words, verified rescue orgs Phoenix Landing + AWC added to external-link library, legacy /african-grey-for-adoption/ 301 added + live-verified, 61c73d7). LESSON baked: dist is minified — use `grep -o … | wc -l`, never `grep -c`, for occurrence counts.

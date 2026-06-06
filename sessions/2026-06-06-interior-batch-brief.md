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
- Verified-Claim Ledger: psittacosis, UV-B/D3, Maxy (talking Congo) = ✅. Never assert PBFD/PCR/board-cert beyond confirmed.

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

- None yet.

---

## Progress Log

- 2026-06-06: Plan written + corrected (no 301s; trusted-breeders = About Us). Task list created (21 tasks). Phase 0 started.

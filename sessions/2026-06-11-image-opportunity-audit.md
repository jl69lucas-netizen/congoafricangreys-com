# Image / Infographic Opportunity Audit — 18 Interior Pages (2026-06-11)

Method: inline section sweep (H2 map + `<img>` count per page in `dist/`). All pages
are already photo-rich (9–22 images); the gap is **answer-value HTML/CSS infographics**
(760px wrapper, 400px desktop height, line-icon SVGs, lazy) — only the scam page has one.
Types per `skills/cag-infographic.md`: Comparison / Feature Grid / Process Flow (HTML),
AI image (Nano Banana), original breeder photo.

## Prioritized build list

| Pri | Page | Section | Type | Rationale |
|---|---|---|---|---|
| 1 ⭐ | african-grey-parrot-diet | "What Should the Base of the Diet Be" | **Proportion bar (Comparison)** — 60–80% pellets · 15–20% veg · ≤10% treats + toxic-food flag strip | Diet ratio is THE featured-snippet/AIO query for this page; visual ratio answers win position 0. |
| 2 | african-grey-parrot-lifespan | "Captivity vs Wild" | **Timeline Comparison** — wild 20–30 yrs · captive 40–60 · records 70+ | Same head-term visual answer; competitors have no lifespan visual. |
| 3 | how-to-tame-african-grey-parrot | "Step by Step" | **Process Flow** — the 7 steps | HowTo schema already on page; visual steps reinforce it for AIO citation. |
| 4 | cites-african-grey-documentation | "Which Documents Come With Every Grey" | **Feature Grid** — the 4-document pack | Trust + scam-defusing; unique to us (competitor gap). |
| 5 | african-grey-parrot-price | "First Year Cost" | **Cost-stack Comparison** — $1,500–$3,500 bird + setup + $185/$350 shipping | Transactional page; cost-stack visuals lift time-on-page + snippet capture. |
| 6 | african-grey-parrot-health-guarantee | "Guarantee Window" | **Process Flow** — 72h congenital → 5–7 day vet check | Makes the window unmissable; reduces inquiry friction. |
| 7 | best-african-grey-parrot-food | "Best Pellet Brands" | **Feature Grid** — Harrison's/Roudybush/TOP's/Zupreem | Brand-comparison visual; review-intent match. |
| 8 | captive-bred-african-grey-parrot | "Captive-Bred vs Wild-Caught" | **Comparison** | Strong but page already has 18 imgs — risk of crowding. |
| 9 | african-grey-parrot-care-guide | "Care snapshot" | **Feature Grid** — 3–4h interaction · 10–12h sleep · cage size · vet cadence | Useful, but page is the longest already. |

## No-build (rationale)
- **scams** — already has 1 infographic + heavy visual structure.
- **guide / african-grey-care hub / faq** — Congo-vs-Timneh comparison tables already serve the visual role.
- **reviews / trusted-breeders** — testimonial-photo-driven; an infographic would read as decoration. Better served by **original breeder photos** (below).
- **adoption** — honest-frame editorial page; the adopt-vs-buy table already does the comparison work.
- **contact-us / privacy-policy** — utility/legal pages; no.

## Original-photo request list (for Mark & Teri)
1. Hand-feeding station / brooder photo → trusted-breeders "Why We Started" + captive-bred "How We Hand-Raise".
2. Gram-scale weigh-in photo of a chick → health-guarantee + diet (2–4% weight-loss flag section).
3. Shipping crate prep (IATA crate, doc envelope) → price shipping section + health-guarantee transit section.

## Recommendation
Build Pri 1–4 first **(Recommended)** — they are the four pages whose head queries are
answered better by a visual than by prose (ratio, timeline, steps, document pack), and all
four are pure HTML/CSS (no API cost). Trade-off: 4 inserts = 4 more DOM blocks on long pages;
mitigated by 400px fixed height + lazy strategy. Pri 5–9 second wave after results.

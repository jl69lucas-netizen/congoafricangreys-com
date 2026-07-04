# Redesign Fix Plan — /congo-vs-timneh-african-grey/ · 2026-07-04 breeder review
Status: **AWAITING BREEDER APPROVAL** (per approve-everything rule). Every item below maps 1:1 to
the breeder's review. Build only after approval; hero + card designs go through visual-companion
screens first (confirmed default workflow).

## A. Honest audit answers (evidence-backed)
1. **Frameworks/angles per section** — documented + previously approved in
   `2026-07-04-section-matrix.md` (AIO/GEO, EBP, EEAT, Entity-Tree, QAB, PDB, BAB, AIDA per
   section, A/B/C categories with grounded WHY). Re-shown for re-approval with this plan.
2. **Fresh Bing + 30-competitor sweep** — **NOT run.** The 2026-07-04 build fetched a fresh
   Google-US SERP snapshot + scraped the ranking articles (Chewy/WCP/ParrotHaven, Firecrawl, live)
   but did NOT run `@cag-competitor-intel --all` over the 30-competitor registry and did not use
   Bing. Per the breeder's pass criteria this page is NOT green until that sweep runs → Phase 1.
3. **Grill-me / Sprint 0.5** — **NOT run** for this page; the comparison skill's own research
   protocol was used instead. Phase 1 includes a grill-me `--quick` orientation pass.

## B. Phases (build order)
**Phase 1 — Research make-good:** fresh BING SERP snapshot + run the 30-competitor registry sweep
for comparison-intent gaps → update section matrix with any new mandatory/recommended/competitor
sections, keywords, entities → re-present matrix for approval.
**Phase 2 — Visual companion screens:** hero (3 options), bird/eggs/pair cards (3 styles),
shipping state-links cards (2 styles) → breeder click-selects.
**Phase 3 — Build** (all items in §C) → **Phase 4 — Gates with proof:** final_page_audit
--comparison (profile added + run 2026-07-04 ✓), keyword-verifier, anti-AI deep pass,
non-commodity check, meta agents, Lighthouse warm median-of-3, deploy + live verify.
**Phase 5 — Compound:** fold every fix into `skills/cag-comparison-page-builder.md` +
re-register skills, so the other 6 comparison pages inherit all of this.

## C. Component-by-component fixes (breeder complaints → actions)
| # | Complaint | Fix |
|---|---|---|
| 1 | Components look old/generic; not Direction-D | Restyle every section to homepage Direction-D idiom: Newsreader heads via global clamp scale (no per-page font-size fights), IBM Plex body, lead-line paragraphs, clay-tick eyebrows, soft-warm cards, .cag-seam dividers. No side-stripes, no identical card grids. |
| 2 | Hero: modern, SHORTER (homepage height ≈483px), images in the middle, full-page, lowercase eyebrow (not CAPS), same type scale all screens | Rebuild Hero to homepage hero spec: full-bleed band, centered split bird portraits, H1 md:2.25rem 2-line, sentence-case eyebrow, OG images → Congo `Amie-female-congo…webp`, Timneh `buy-female-timneh…webp`, responsive srcset (one visual size all devices). |
| 3 | Breeder/trust card image | Use `/timneh-african-grey-variant.webp` (Timneh left, Congo right, one shot) on the Why-Trust card; serve the Mark & Teri 120px avatar at a real 128px asset (kills the 21 KiB Lighthouse hit). |
| 4 | Bird cards have no images, look cheap | Rebuild S19 as homepage-grade photo cards, new styling: Congo card ← jins-jeni2.webp (jins-jeni3 placed at a Congo topic section), Timneh card ← one of the three COMPARE-PAGES Timneh photos (rest distributed to Timneh sections). NEW unused keyword variations on card headings/anchors. |
| 5 | Add fertile-eggs + breeding-pair section/cards, same treatment, new keyword variations | Add product cards (prices from price-matrix/financial-entities, incl. $3,000 bonded pair) with real photos + never-used LSI variants. |
| 6 | Shipping section: images + top-7 state/city links, NEW angles, SEO anchors | Two photo cards — Home Delivery ← petsvans5.jpeg, Airport Pickup ← live-animal-african-grey-parrot-shipping.webp — plus a 7-state/city link row (TX, FL, CA, NY, GA, AZ, NC per locations.json traffic) with fresh anchor angles not used on any other shipping section. $185/$350 line stays. |
| 7 | Contact form wrong; remove duplicate components below it | Swap to the short blog-post-style inquiry form extended to what we sell: interest (Congo/Timneh/fertile eggs/breeding pair), first+last name, cell + confirm, email + confirm, delivery type ($185 airport / $350 home shown), price band visible. Pass `hideGlobalCta` + drop the extra newsletter band so the global "Reserve a Hand-Raised…" + "Join Us" blocks stop stacking under the form. |
| 8 | Jump rail not sticky (mobile+desktop); push TOC left, widen main | Fix `position: sticky` (parent overflow trap) on both rails; move desktop TOC further left, widen `.cvt-main` column while keeping the 1200px shell. |
| 9 | Testimonials | Replace with TWO real existing C.A.Gs reviews (from the live review system) — never fabricated. |
| 10 | Blog section thumbnails | Use each post's own `-card.webp` hero (talking, price, beginners) exactly like the /blog/ hub. |
| 11 | HTML infographics disliked | ALL infographic slots → Gemini images; full prompt pack ready: `2026-07-04-gemini-infographic-prompt-pack.md` (13 prompts, distinct style each, same DESIGN.md palette/size, 760×400 slot, 16:9 1600×900 gen). S17 flat-lay swap runs once GEMINI_API_KEY is added to `.google-key`. Real `<table>` stays under P2 for AIO. |
| 12 | Component heights too short (trust card, newsletter, final CTA) | Increase vertical rhythm to homepage spacing scale (64px/40px desktop, 40/24 mobile), taller cards, consistent across breakpoints. |
| 13 | Links at start of sentences | Content pass: every internal/external link moved to beginning/middle of sentence, never end. |
| 14 | Contrast FAILs (td.edge, .myth-x, .btn-clay small text) | Apply AA tokens: small clay text → #b04228, clay button fills → --clay-ink #c8472f w/ white, edge-cell text ≥4.5:1. |
| 15 | Image delivery (Lighthouse) | Responsive srcset for both hero variant images; compress timneh variant; small real-size seam/footer logo asset (200×66→40×13 displayed); all images sized per IMAGE-DESIGNS.md slots. |
| 16 | Duplicate BreadcrumbList (found by new audit) | Remove the page-level breadcrumbSchema const — Breadcrumb component already emits it. |
| 17 | Meta: 4-part ending, NOT "C.A.Gs – Midland, TX" | Proposed (Recommended): Title `Congo vs Timneh African Grey: Size, Talking Ability, Temperament & Price Compared | C.A.Gs – Trusted Congo & Timneh African Grey Breeders`. Also fixes the audit's brand_in_title FAIL. Desc rewritten to F1 ≤185 with LSI close. |
| 18 | /70de/ cache TTL, unused JS 70 KiB, missing source map, forced reflow | All four trace to Cloudflare **Rocket Loader** (known: project_blog_perf_rocket_loader). Not fixable in repo — breeder toggles Rocket Loader off in the Cloudflare dashboard + purge. Documented here so the gate report stops re-flagging it. |

## D. Gates that must show proof before "pass"
final_page_audit --comparison · keyword-verifier · anti-AI deep pass · non-commodity check ·
meta agents · Lighthouse warm median-of-3 (mobile+desktop) · live 200 + schema validation.

## Open Flags
- **ONE question for the breeder (Recommended answer first):** Approve this plan with Phase 2
  visual-companion screens for hero + cards (**Recommended** — it's the confirmed workflow and the
  hero/card styling is exactly what got rejected last time; trade-off: one extra approval round
  before code) — or skip straight to build using the specs in §C as written.

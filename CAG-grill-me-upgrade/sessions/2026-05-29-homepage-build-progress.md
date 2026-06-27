# Homepage REBUILD v2 — Build Progress / Continuation Handoff
**Last updated:** 2026-05-31 (post-build polish session PUSHED, commit 1589e03) · **Status: ALL 25 SECTIONS COMPLETE + POLISH DONE. Next: on-page AEO/GEO gate.**
**Page:** `src/pages/index.astro` · **Deploy:** live on Cloudflare Pages.

## ✅ POLISH SESSION (2026-05-31) — ALL PUSHED

| Fix | File(s) | Commit |
|---|---|---|
| BirdCard image height h-64→h-72 (288px), default object-center | `BirdCard.astro` | e7d507e |
| Newsletter heading one line, text-2xl→text-lg mobile, whitespace-nowrap, removed `<br>` | `NewsletterV2.astro` | e7d507e, 04a9c32 |
| Testimonials feature: image fills mobile width, blockquote text-base md:text-xl | `Testimonials.astro` | e7d507e |
| Testimonials grid: smaller padding, font, lazy loading on avatars | `Testimonials.astro` | e7d507e |
| Review names updated: Clifford Hutter (top), Albert Schroder (mid) | `index.astro` | e7d507e |
| bottomReviews array added: Archie Obrien, Richard Woodard, Catherine Kempf + photos | `index.astro` | e7d507e |
| 3 buyer review photos copied to public/ (clean filenames) | `public/` | e7d507e |
| Lazy load audit: SplitFeature classic + Testimonials mosaic fixed | `SplitFeature.astro`, `Testimonials.astro` | a6732dc |
| Evie bird card objectPos: object-top (shows head) | `index.astro` | cbab52d |
| TrustStats classic: emoji text-2xl md:text-3xl, title text-sm md:text-lg, p-4 md:p-6 | `TrustStats.astro` | 04a9c32 |
| Shipping section: all 14 states/cities linked to location pages | `index.astro` | 1589e03 |

---

## HOW TO RESUME (next session)
1. **Do NOT re-run `grill-me`** (it's a fresh-start questionnaire — would re-ask everything). Just open the build:
   > "Continue the CongoAfricanGreys homepage REBUILD v2. Read `sessions/2026-05-29-homepage-build-progress.md`, `sessions/2026-05-29-homepage-outline-v2.md`, and `sessions/2026-05-29-session-brief.md` (REBUILD v2 section) first, then resume building at **Section 9 (Congo)**."
2. Start the dev server (`launch.json` name `cag-dev`, port 4321) and confirm sections 1–8 render.
3. Build section-by-section, **preview each at localhost:4321**, batch per the cadence below.

## CADENCE (agreed)
Build in batches, preview, get approval. Current batch to do next = **Sections 9–11** (Congo → Timneh → Comparison).

---

## ✅ DONE & APPROVED (Sections 1–8)
| # | Section | Component (file) | Notes |
|---|---|---|---|
| 1 | Hero | `cag-library/HeroV3.astro` (`:b` Authority Green) | photo `/african-grey-parrot-breeder-midland-tx-hero.webp`, `object-contain` circle (both faces + sign centered) |
| 2 | Counter Snippet | `cag-library/CounterSnippet.astro` | 12+ / 100% / $1,500 / 24h |
| 3 | Key Takeaway | `cag-library/KeyTakeawayV2.astro` (`:02` stat grid) | 8 stats, green header band |
| 4 | TOC | `cag-library/TocV3.astro` (`:02` grouped) | 4 parts, 16 anchors |
| 5 | About / Owner | `cag-library/OwnerCard.astro` (Variant B, one-photo) | compact; photo `/about-mark-teri-benjamin-african-grey-breeders-midland-tx.webp` |
| 6 | Review block #1 | `Testimonials variant="feature"` + `/african-grey-review-top.webp` | dark panel (see token fix) |
| 7 | All Products | inline filterable grid + `BirdCard` (`#available-birds`) | Pill-Tabs |
| 8 | Eggs & Breeding Pairs | inline horizontal list (`#eggs-pairs`) | → `/african-grey-parrot-bird-eggs-for-sale-usa/` + `/african-grey-breeding-pair-for-sale/` |

| 9 | **Congo** | `SplitFeature:editorial` + section | H2 "What Is a Congo African Grey — the Classic Red-Tailed Talker?"; EBP intro; woven internal (`/congo-…/`,`/african-grey-parrot-price/`,`/…care-guide/`,`/timneh-…/`) + external (alexfoundation, parrots.org, wikipedia grey_parrot, all 200-verified); H3+H5(scientific name)+H6 FAQs |
| 10 | **Timneh** | `SplitFeature:classic` + section | H2 "What Is a Timneh African Grey — the Calmer, Earlier-Talking Subspecies?"; cross-links Congo/price; ext wikipedia timneh + parrots.org; H3+H5(Psittacus timneh)+H6 FAQs |
| 11 | **Comparison** | **`CompareTableE.astro` (NEW cag-compare-table-e, Style E 1100px)** + AG-vs-species | H2 (Congo vs Timneh, green/clay gradient headers, cag-congo/timneh icons) → H3 "How Does an African Grey Compare to a Macaw, Cockatoo, or Amazon?" + H4 apartment sub. Anchor kept `#compare-species` (TOC item 5). |

**New components built this batch:** `src/components/cag-library/CompareTableE.astro` (decoded from `CongoAfricanGreys Component Library.html` → asset#7 `components-b.jsx` Component 6; saved `.build-extract/components-b-compare-newsletter.jsx`) · `src/components/cag-library/NewsletterV2.astro` (3 variants top/middle/bottom — Component 7). Homepage now uses `NewsletterV2 variant="middle"` (dark split, mid) + `variant="bottom"` (slim, footer); old `Newsletter` banner/split usages + import removed (also dropped unused `StatsBar`/`MeetTheTeam` imports). **Fixed latent bug:** `SplitFeature` `editorial` variant ignored `imageSrc` → now renders the real photo.

**Schema fixes (user-requested, site-wide):** brand `"name":"CongoAfricanGreys.com"` → `"Congo African Greys"` (canonical per credentials.md) in 6 files (index orgSchema+videoSchema, captive-bred, hand-raised, adoption-cost, dna-tested, how-to-tame). Breeding-pair Product schema: added `image[]` (fixes Google "Missing field image" critical) — Appendix I + brand already correct in source. Comparison-page "Appendix II" left intact (factually describes cockatoos/Amazons, not Greys). `npx astro build` clean (98 pages); dist verified.

**Also done:** added `--color-panel/line/mid/forest/forest-lt` to `src/styles/global.css` (cag-library components referenced these but they were undefined → fixed `bg-panel` site-wide). Added **Rule 28b (Two-Keyword Header Method)** to `skills/cag-seo-master-checklist.md`. Registered new components + v2 order in `components.md`, `component-page-matrix.md`, `component-themes.md`.

---

## ✅ ALL SECTIONS DONE — 9–16 PUSHED (a0ed205) · 17–21 PUSHED (8f6f95e) · 22–25 PUSHED (ba676c5, 2026-05-30)

**Rebuild complete through Section 25.** Final rendered section order (dist verified): hero → counter → key-takeaway → toc → owner → review#1 → available-birds → eggs-pairs → congo → timneh → compare → why-us → trust → reviews-mid → history → health → pricing → tools → shipping → reviews → blog → **video → faq → how-to-buy → contact** → newsletter(bottom) → schema. Section 14 mid-review = id="reviews-mid"; the id="reviews" grid is Section 20.
12. ✅ **Why Choose C.A.Gs** `SplitFeature:editorial` (id=why-us) → /why-choose-cag/, /about/, /african-grey-parrot-price/ + USDA APHIS, World Parrot Trust. Owner photo. H2/H3 + pull-quote.
13. ✅ **C.A.Gs vs Scammers** `ScamAwareness:compare` (id=trust) → /how-to-avoid-african-grey-parrot-scams/, /trusted-african-grey-parrot-breeders/ (intro), /contact-us/ (body). H2/H3.
14. ✅ **Review #2 (mid)** `Testimonials:feature` (id=reviews-mid) + /african-grey-review-middle.webp (copied from assets/brand/Review-middle.webp). Uses reviews[2] Henry Acadia.
15. ✅ **History & Origin** entity-tree (id=history) H2→H3→H4→H5(Psittacus erithacus/timneh)→H6 FAQs. Alex/Pepperberg moat (alexfoundation.org), birdlife.org, allaboutbirds.org, WPT. "Appendix II→I" sole allowed use (history only).
16. ✅ **Health & Guarantee** `TrustStats:classic` (id=health) → /best-african-grey-parrot-food/, /african-grey-parrot-care-guide/. Replaced old CareGrid block (CareGrid + VideoSection imports removed).
17. ✅ **Pricing** `PricingTable:classic` (id=pricing) → /african-grey-parrot-price/ (intro, sentence-start) + /african-grey-parrot-care-guide/ (body). H2 "What Does a Hand-Raised, CITES-Documented African Grey Parrot Cost From C.A.Gs?" Rows verified vs price-matrix.json; $200 deposit + 40–60yr lifetime + first-year-calc CTA. note prop (under-$1,500 = wild-caught/sick/no bird).
18. ✅ **Tools** inline ×3 (id=tools) — cost calc / CITES doc checklist / shipping estimator. H2 "How Do You Plan the Real Cost of Owning an African Grey Parrot Before You Commit?" Two-keyword H3s. JS IDs (calc-bird/ship/cage/vet/total, doc-check, doc-score) + existing inline `<script>` PRESERVED (not duplicated). Intro woven /african-grey-parrot-price/.
19. ✅ **Shipping + First 30 Days** consolidated (id=shipping). H2 "How Does C.A.Gs Ship African Grey Parrots Safely to All 50 States?" + H3 "What Happens in Your African Grey's First 30 Days at Home?" Woven /buy-african-grey-parrot-near-me/ (intro) + /african-grey-parrot-care-guide/ (Week 2–3). 11 states/cities. Kept ship-flow infographic + IATA crates photo verbatim. FadeIn removed.
20. ✅ **Case Study / Review #3** `Testimonials:grid` (id=reviews) wrapped with H2 "What Do Families Say After Adopting a C.A.Gs African Grey?" + VERIFIED BUYERS eyebrow. Uses full reviews[] array (frontmatter, unchanged).
21. ✅ **Blog & Care Guides** (NEW, id=blog, inserted before id=video) → /african-grey-parrot-care-guide/, /best-african-grey-parrot-food/, /african-grey-care/, /blog/. H2 "How Do You Give an African Grey Parrot the Best Care — Diet, Enrichment, and Health?" 2×2 card grid, canonical-set icons only (✅/✈️/📞, no 🦜). Intro woven /…care-guide/ + "diet + enrichment plan with every bird".
22. ✅ **Video** (id=video) — kept inline mp4 poster-backed placeholder (cleaner than empty iframe; VideoObject schema relationship preserved). H2 "Can You Watch C.A.Gs African Greys Learning to Talk Before You Commit to One?" eyebrow HEAR THEM TALK. Caption notes "YouTube URL coming soon — breeder to supply." `FadeIn` wrapper removed (+ orphaned `FadeIn` import dropped from frontmatter; no FadeIn refs remain in file).
23. ✅ **FAQ** `FaqAccordion:classic` (id=faq) — wrapped with H2 "What Do Buyers Most Often Ask Before Adopting a C.A.Gs African Grey Parrot?" + COMMON QUESTIONS eyebrow. `faqItems` array passed as-is; FAQPage Schema block (uses same `faqItems`) left untouched. Moved BEFORE Contact per approved order.
24. ✅ **How to Buy** (NEW, id=how-to-buy, inserted between FAQ and Contact) — inline entity-tree, 4 numbered green-circle cards (Browse & Ask → $200 Deposit → Paperwork & Vet Cert → Airport Pickup). Intro woven /contact-us/ (sentence start). Step 1 woven #available-birds; Step 4 woven /buy-african-grey-parrot-near-me/. CITES Appendix I + USDA AWA in Step 3. Clay-pill CTA "Start Your Inquiry →" → #contact (border-radius:50px).
25. ✅ **Contact + Map** `ContactForm:application` (id=contact, now LAST content section). H2 "Ready to Inquire About a C.A.Gs African Grey Parrot — What Should You Tell Us?" eyebrow START YOUR INQUIRY. Sub-para woven /contact-us/ + "Teri ... within 24 hours." Google Maps iframe (Midland,Texas&output=embed) kept verbatim. 2-col grid: form left / map right.

> NOTE: ✅ All v1 inline sections have been replaced. No OLD v1 blocks remain. The 25-section rebuild is complete and live.

---

## BUILD CONTRACT (every section)
- Brand = **C.A.Gs / C.A.Gs – Midland, TX** in body (never "congoafricangreys.com").
- **Two-keyword headers** (Rule 28b): secondary KW + LSI/NLP/entity. Conversational (What/How/Is/Can/Who). Use ALL H1–H6 across the page.
- **CITES Appendix I** + captive-bred-USA, never wild-caught. (Appendix II only allowed in the History "uplisted from II→I" sentence.)
- **Links woven mid-sentence from the START** of body paragraphs — internal (variant/price/scam/location pages) + blog + care guides + 15 external .gov/.edu/.org. NEVER dump links at the end.
- **No fabrication** (no invented vet names, counts, stats). Verified facts only. Confidence ≥97% before writing.
- Prices via `cag-pricing-table`. Comparison via `cag-compare-table-e`. FAQs PAA-only.
- New components only (see `components.md` — v3/v2 modern set). No legacy `cag-split-hero`, old `MeetTheTeam`, etc.

## DATA / FACTS
- Pricing: Congo $1,700 (adult)–$2,500 (baby); Jins+Jeni pair $3,500; Timneh $1,500–$1,600; breeding pairs $3,000; fertile eggs $95 (5 = free US ship); deposit $200.
- Owners: Mark & Teri Benjamin, Midland TX, est. 2014. USDA AWA licensed, DNA-sexed, avian-vet cert, CITES Appendix I, IATA shipping.
- `birds[]`, `reviews[]`, `faqItems[]` arrays live at top of `src/pages/index.astro` (frontmatter).

## TECH NOTES (preview/screenshot quirks)
- **Tailwind v4** — tokens in `src/styles/global.css @theme` (NOT a tailwind.config). cag-design-system.css is NOT imported on this page.
- New components are bundler packages: decode `<script type="__bundler/template">` (JSON string) + manifest assets (base64+gzip) via Python — see `.build-extract/` for already-decoded files (`page-components.jsx` has TocGrouped/TakeawaysStats; hero-b-decoded.html; mobile-components-decoded.html). **Compare-Table-E + Newsletter(×3) now decoded** from `CongoAfricanGreys Component Library.html` (gzip+base64 JS assets → asset#6 `components-a.jsx`, asset#7 `components-b.jsx`) — source saved to `.build-extract/components-b-compare-newsletter.jsx`; built as `CompareTableE.astro` + `NewsletterV2.astro`. (No standalone "NEW CAG COMPONENTS"/b456b115 file exists on disk; the components live inside the master Component Library bundle.)
- **Screenshot gotcha:** `preview_screenshot` reliably captures only at `scrollY=0`. To shoot a below-fold section: set a TALL viewport (height ≥ section bottom px), `window.scrollTo(0,0)`, then screenshot. Sections use `FadeIn` (opacity:0 until IntersectionObserver) — at scroll 0 with a tall viewport they're in view and fade in. DOM eval (getBoundingClientRect/innerText) is the authoritative verifier.
- Verify each section: `preview_logs` (errors) + `preview_eval` (DOM checks) + tall-viewport screenshot.

## ✅ POST-BUILD ADDITIONS (2026-05-31 session 2)

| Addition | File | Commit |
|---|---|---|
| JumpRail (Option C) — floating right-side dot rail, 18 sections, scroll-spy | `src/components/cag-library/JumpRail.astro` | 7520f8a |
| JumpLinks (Option B) — section-bottom Prev/Dots/Next strip (reusable props) | `src/components/cag-library/JumpLinks.astro` | 7520f8a |
| All 3 designs registered in components.md with props + usage examples | `docs/reference/components.md` | 7520f8a |
| Design preview saved | `sessions/jump-link-preview.html` | 7520f8a |

JumpRail wired into homepage via `<JumpRail />` just inside `<BaseLayout>` (before Section 1 Hero). Desktop 1024px+ only. Uses same 18 section IDs as TocV3.

## OPEN ITEMS / PENDING
- **▶ NEXT STEP — On-page AEO/GEO gate (run ON the live homepage):** `@cag-keyword-verifier` → `@cag-meta-description-agent` → `@cag-trust-signals-agent`; then 15-point QA (`skills/cag-seo-master-checklist` Phase 4); then `@cag-deploy-verifier` (200 check + IndexNow) + `sitemap-agent`.
- Sync `component-page-matrix.md` homepage order to the final 25-section sequence (still shows the 19-block v2 draft).
- YouTube URL for Video section (breeder to supply) — Video currently uses mp4 poster-backed placeholder + VideoObject schema scaffold.
- Site-wide Appendix II→I sweep on location pages (separate queued task).
- ✅ Cleaned unused imports in index.astro (`StatsBar`, `MeetTheTeam`, old `Newsletter`, and now `FadeIn`).
- Register `cag-compare-table-e` (`CompareTableE.astro`) + `cag-newsletter-v2` (`NewsletterV2.astro`, 3 variants) in `docs/reference/components.md` + matrix/themes.
- Optional: place Newsletter `variant="top"` (light banner) if a top-of-page slot is wanted — currently only middle (mid) + bottom (footer) are wired, matching outline §E (newsletter ×2).

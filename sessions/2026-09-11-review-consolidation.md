# 2026-09-11 — Review consolidation

Plan: docs/superpowers/plans/2026-09-11-review-consolidation.md
Plan artifact: https://claude.ai/code/artifact/b7bc965b-18c3-4bb0-bbd9-42441a01aa44

## Baseline
- review page lists 4 buyers (Kempf twice); 18 reviewers exist on 64 non-location pages
- dup_content_audit.py baseline (full output in session scratchpad dup-before.txt):
  FAIL — 6128 duplicated passages ≥12 words.
- tests/test_review_attribution.py + tests/test_homepage_reviews.py: 5 passed

## Gate results (Task 7, 2026-09-11, dist from uncommitted Tasks 3–5b)
- test:render:meta 296 passed / 34 skipped / 0 failed
- review guards: 19 passed, 1 xfailed (pending ruling); sweep --check 0
- dup_content_audit: 6128 before = 6128 after; 146 blocks on the 4 changed pages, byte-identical
- test:render:pages 57/57 (baseline 57/57); timneh DUP instances 33→58, all the restored ledger quote (expected)
- page_hardening / final_page_audit rows on changed pages: all pre-existing, none review content
- gates rewrote 18 data/quality/scorecards/*-2026-09-11.json — NOT in commit B

## Browser proof (Task 8, local dist via astro preview, Playwright MCP)
- 375: 14 names each exactly once in #featured-reviews + #more-reviews; 14 Review JSON-LD, no dup; 12 imgs loaded, 0 broken; no pending names; no x-overflow; wall 1 col × 12; initials badges tinted; names in Newsreader
- 768: wall 2 cols (6 rows × 2); 0 broken; no x-overflow
- 1280: wall 3 cols (4 rows × 3); 14 JSON-LD; featured alts Brian Carr, Catherine Kempf; 0 broken; no x-overflow
- console: 0 errors, 0 warnings (whole session)
- screenshots sent to the breeder for rule-7 layout approval; commit B waits on that approval

## Shipped (2026-09-11)
- 859d75c1 + e76120f5 ledger/inventory · 34c7f768 page + wall + guard + restored quotes (commit B, layout approved) · 81034475 breeder ruling (trio real, short wording) · 5ab8eda2 Testimonials font-lora + /testimonials/ deleted (301 kept) + sitemaps regenerated (only /testimonials/ removed; lastmod stamped 2026-09-11 on all URLs by the standard generator)
- IndexNow HTTP 200: african-grey-reviews (×2), trusted-breeders, timneh, male-vs-female, available/{amie,bery,elad,evie,jins-jeni,roys}, adoption-cost, / (homepage)
- Live curl: ruled wording on all 9 trio pages, 0 leftover rewrite phrases; homepage Testimonials elements font-lora 10 / font-display 0; live page-sitemap 55 <loc>, 0 /testimonials/; /testimonials/ → 301 /african-grey-reviews/

## Open Flags
- [x] RULED 2026-09-11 (breeder, chat): Brunner / Soliz / Brim are REAL; their exact words = the SHORT wording already on the /available/ hub (and male-vs-female for Ida). The long per-bird-page versions were templated rewrites (pronoun swaps like "They's DNA-sexed", added "landed at LAX… Worth every dollar") → restored to the breeder's words on 6 bird pages + adoption-cost. Original flag: are Lawrence Brunner / Sandra Soliz / Ida Brim real, and is Ida's longer "here in Nashville" text her exact wording? (blocks Task 11 only)
- [ ] Homepage shows /african-grey-review-top.webp beside Clifford Hutter; ledger says he has no photo
- [x] BREEDER: ignore (2026-09-11). Review page + homepage claim "52 verified buyers / 4.9" while 14 reviews are published — unproven aggregate (rule 10)
- [ ] Comparison hub review cards show a verbatim fragment + our third-person summary inside star cards — allowed by the guard, but a breeder call
- [ ] Testimonials.astro default props are 3 fabricated reviews (Sarah & Tom, Devin Hart, The Park Family) — latent; nothing renders them today
- [ ] Harness DUP chrome-skip parity fix still uncommitted in worktree jovial-feistel-071f51
- [x] FIXED 5ab8eda2 (deleted, 301 kept): src/pages/testimonials/index.astro still BUILDS 5 named, unverified reviews (Keith Harmon et al.) behind a live 301 to /african-grey-reviews/ — never served, excluded from the guard; delete candidate (breeder call)
- [x] FOUND by the Task 1 guard, fixed in Task 5b: edited real reviews — trusted-breeders (visible grid + schema, Woodard/Kempf rewritten with SEO phrases), timneh-for-sale (Woodard "Congo" removed), male-vs-female (Kempf schema truncated)
- [ ] Guard limitation (reviewer Minor 4, not triggered in dist today): a quote split by an inline tag (e.g. C.A.<b>Gs</b>) would miss its 60-char key
- [ ] Ida Brim has TWO wordings live: short ("From the first email to home delivery, everything…") on /available/ hub + male-vs-female; long ("…here in Nashville…") on 6 bird pages + adoption-cost. Part of the Brunner/Soliz/Brim ruling (Task 11 fixes whichever is not her wording on every page)
- [ ] Guard limitation: D-b (quote beside the wrong name) is checked for <blockquote> cards and src flat objects, NOT for <p>-style cards (bird pages, grid cards) — card layouts put the name before the quote on bird pages and after it in Testimonials grids, so no single window is safe (tried 2026-09-11: false 'wrong' lines on home/reviews/trusted). Pending trio are the only <p>-card-only reviews today
- [x] RETRACTED: Alene Murphy's pair-page caption was never wrong (src + dist say Savannah, GA); the plan's D-d finding was a controller misread. Task 5 is a no-op; the pair page is not in the changed set
- [ ] Ledger location format varies (ZIPs "Oceanside, CA 92054", "Hartsville, SC 29550"; spelled-out "San Bernardino, California") — visible side by side on the review wall. Normalising the ledger would make the sweep rewrite those source pages too, so it is a breeder style call, not done here
- [ ] Testimonials `feature` variant (shared with the homepage): alt={name} even when the photo shows the bird; ←/→ buttons have no accessible name and do nothing (renders 2× on /african-grey-reviews/) — pre-existing, out of scope
- [ ] /african-grey-reviews/ is not a render-harness target (tests/render/targets.json), so the IMG oversize gate never measures its 96–128px avatars in 48px boxes — adding it widens the pages gate; separate task
- [x] FIXED 5ab8eda2 in Testimonials only: Testimonials `grid`/`mosaic`/`feature` variants use `font-display` and `grid` uses `bg-clay-50` — neither token exists (no --font-display / --color-clay-50 in @theme), so review-card headlines and names on the homepage + trusted-breeders render in the body sans and the grid initials badge has no circle. Pre-existing; the new `wall` variant uses font-lora + bg-clay/10. Fixing the shared variants changes the homepage — separate task
- [x] Commit B 34c7f768 pushed 2026-09-11 (layout approved by breeder)
- [ ] NEW: `font-display` class is used 105× across 21 cag-library components (Navbar, Footer, BirdCard, …) with no --font-display token — only the Testimonials variants are fixed in this session (the approved flag); the rest is a sitewide change for a separate decision

## Batch 2 (breeder, 2026-09-11 evening): fix the remaining open items; ignore the 52/4.9 aggregate and the Hutter photo (breeder has it)
- [x] Review towns normalised to "City, ST" (Perkin, Ovalle, Plaisance, Hendershot, Erwin) — ledger, specs, 4 pages
- [x] Wall: a lone last card is centred (2 cols) / middle column (3 cols)
- [x] font-display → font-lora in 17 cag-library files (94 class uses); only the homepage renders them — 12 elements visibly change (2 pull quotes, 4 trust badges, 6 price cells) → breeder visual approval before deploy (rule 7)
- [x] Guard: D-b now structural for every card layout (card = nearest ancestor element holding a buyer name); 71 cards attributed; negative proofs on grid + bird-page swaps
- [x] Sitemap lastmod = page source's last git commit date (TODAY only for uncommitted sources)
- [x] FOUND: live sitemap listed /.astro/, /dist/, /node_modules/ (404s) from gitignored stray dirs in src/pages — generator now skips dirs without a page file
- [x] FOUND: fbda1577 (another session's homepage-hero design canvases in docs/) made Tailwind scan docs/ → ~57 KB dead CSS inlined into every page; fixed with `@source not "../../docs"` in global.css
- [ ] FLAG: src/components/cag-library/ContactForm.astro shows phone (432) 555-0119 — looks fabricated; component has 0 importers (not rendered). Breeder call
- [ ] Scorecards: regenerate with test:render:pages after the batch-2 deploy, then commit
- [ ] CONCURRENT SESSION: src/components/cag-library/HeroV3.astro is being rebuilt by another session (homepage hero round-5 variation A "Paperwork card", docs/design/homepage-hero-r5/, canvas 6881b0e8; file modified 17:54). NOT part of this work — never stage it from this session
- [x] Commit E 43f63661 pushed (towns, lone card, structural D-b guard, sitemap lastmod/phantoms//available/, docs/ excluded from Tailwind scan)
- [x] BREEDER APPROVED (2026-09-11): homepage font-display→font-lora (17 cag-library files) and removal of the fabricated-looking phone (432) 555-0119 from the unused ContactForm component
- [x] Commit F 887b598d pushed: font-display→font-lora (17 files, breeder-approved) + fake (432) 555-0119 phone removed from ContactForm (2 spots) and Navbar/Footer defaults (blanked; both render phone only when passed). The other session's hero landed separately as ad59f19b.
- [x] 887b598d LIVE-verified (curl): homepage 0 font-display / 151 font-lora; prices, badges and pull quote in serif; no fake phone; IndexNow / HTTP 200
- [x] Scorecards regenerated from a clean worktree of origin/main @ 887b598d: test:render:pages 57/57; 19 scorecard files committed

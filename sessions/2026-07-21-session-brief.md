# Session Brief — 2026-07-21

> **Status:** READY — interview complete.
> **Last updated:** 2026-07-21 (Sprint 0.5 complete)
> **Task:** REBUILD `/congo-african-grey-for-sale/` — transactional for-sale page, to the egg-page/for-sale-builder standard.

## Q&A Log (Verbatim)
_(Business + target layer already answered by the breeder in this session's Sprint 0 exchange — captured here, not re-asked.)_

**Q1 — Outcome:** Rank the currently-invisible Congo for-sale page (pos 16.45, absent from Google/Bing top-10) and convert scam-anxious buyers. Rebuild to egg-page standard: clean, equal-height modern components on all devices, new/slightly-different components, no crossover headers/dup, all final checks pass.
**Q2 — Traffic reality:** `congo african grey for sale` = pos 16.45 · 611 imp · 38 clk · 6.22% CTR; best variant `african grey congo for sale` = pos 16.24 · 392 imp · 46 clk · 11.73% CTR. Goal = redesign + push ranking + convert.
**Q3 — Worst performer (this page):** current page is a thin stub — 2 H2s, zero H4–H6, no cards/form/shipping/FAQ; fails Heading Gate; ranks nowhere.
**Q5 — Constraints (CONSTRAINT lines below):** see Constraints section.
**Q6 — Specific target:** `/congo-african-grey-for-sale/` (single-bird Congo only; pair page stays separate).
**Q7 — Done looks like:** built to egg-page standard; all final checks pass (anti-AI, humour, non-commodity, first-person, Lighthouse, image-opt, GEO/AEO/SEO, entity, keyword-verifier); page visible + converting.
**Q8 — Reader/fears:** buyers whose #1 fear is SCAM/FRAUD + PRICE CONFUSION ("is this seller real?", "why $800 vs $8,500?"). Ranked: scam → CITES/legal → wild-caught → sick bird → support abandonment → cost.
**Q9 — Benchmark:** our own egg page (for-sale kit standard); competitor on-page benchmark = birdsjungle.com (schema/H2 map, but fake reviews); authority = Parrot Wizard.
**Q10 — Framework:** "Strategy A — Trust-First / Anti-Scam Spine — AIDA × EBP × PAS (Recommended)."
**Q11 — AIO/GEO:** "(C) Both — question-shaped headers with a snippet-ready answer sentence, backed by full entity coverage + FAQPage/Product/AggregateRating schema."
**Q12 — Visual plan:** "I don't want HTML/CSS infographics, like we did on the egg page. Give full prompts for all infographics — I will generate them and drop them along with ~7-8 OG images and a video. Give full prompts for all the H2, H3 and key H4 headers for me to generate now, then drop. Yes we need a lifestyle section — AI lifestyle imagery is fine."
**Q13 — Repeat/Avoid:** "Yes — this page needs the compact 350–400px hero, the sticky dial TOC for desktop BUT DIFFERENT for this page, and don't forget the mobile jumplink, compact sections throughout the page. Once I generate the infographics and drop them along with the OG Congo images, we can start."
**Q14 — Urgency:** No deadline — gated on breeder's image generation + drop + explicit "start."

## Decisions Log
- **Framework (APPROVED): Strategy A — Trust-First / Anti-Scam Spine.** AIDA backbone (bird cards near fold = Attention); DESIRE stage carried by the "Is this seller legit?" verification moat in **EBP** (Evidence→Benefit→Proof) with a light **PAS** frame on scam-fear/price-shock. Reason: entire UGC layer is scam-terror + price confusion, #2 Google result is itself a scam, no competitor resolves it — plays our moat, not the aggregators' volume game. Trade-off: keep bird cards *first* on mobile so trust content sits after the fold, not above it. Voice: first-person C.A.Gs.
- **AIO/GEO (APPROVED): (C) Both** — Featured-Snippet capture (question H2/H3 + one-sentence declarative answer) + Entity-first AIO citation (entity coverage + FAQPage/Product/AggregateRating/BreadcrumbList/ItemList schema). Protect-engines: none confirmed (LLM Visibility unmeasured — see Open Flags).
- **Visual plan (APPROVED — egg-page model): NO in-page HTML/CSS infographics.** All infographics AI-generated (breeder generates + drops), egg-page taxonomy (.webp AI infographics / real OG photos), all in uniform 1408×768 `.sec-img.inf-img` box + `-760` sibling. Deliverable written: `assets/1WORKING-ON/FOR-SALE-PAGES/congo-page-image-plan-and-prompts.md` — 17-section map (Trust-First spine) + reuse-vs-generate decision per slot + 8 full art-directed prompts (P1–P8) per IMAGE-DESIGNS.md.
  - **SCOPE WIN (large existing asset library found):** most Congo photos + generic infographics (congo-vs-timneh, size, scam red-flags, payment warning, DNA, shipping map, price tiers, safety checklist, red-tail hero, bird cards) ALREADY in `public/` → REUSE. Breeder GENERATES only **8 fresh AI images (P1–P8)**: hero, companion/talking lifestyle, Congo-specific "real vs fake breeder" moat, verify-in-60s, price $1,500–$8,500 explainer, what's-included, how-to-buy, lifestyle-section. Breeder DROPS real: 4 bird photos (Roys/Amie/Bery/Jins&Jeni) + optional buyer/vet photo + 1 video.
  - Section map is DRAFT pending Heading-Gate approval; prompts keyed to it.
- **Layout/component carryovers from egg page (Q13):** compact **350–400px hero**; sticky **desktop dial TOC** BUT a **distinct variant** for this page (component-refresh delta — no identical siblings); keep the **mobile jumplink**; **compact sections throughout** (egg-page density). Build with the for-sale component kit (not homepage/comparison components); every component slightly different from egg page.
- **SPRINT 1 COMPONENT SET (LOCKED 2026-07-21 — from visual-companion-task5.html; distinct from egg):**
  - **Hero:** Split-Hero B · Full-bleed warm gradient (egg used Split-Hero C dark). Compact 350–400px.
  - **Desktop dial TOC:** Dial 2 · Dark Aviary (dark-green) — THE distinct dial (egg used Dial 1 clay). Works because Congo hero is warm/light → no double-dark clash.
  - **Mobile jump-rail:** Rail A · Price-chip rail (outlined clay chips + live counts, sticky, scroll-margin baked).
  - **In-body TOC:** T5 · Reserve-Path Stepper (buy-path with read-times — matches AIDA spine).
  - **Key-Takeaway (pick-3):** K1 Receipt Card (top "short version") + K4 Clipboard Checklist (at the verification moat) + K3 Green Ledger (rotation).
  - **Tables/CTA/seam:** Table A · Clay-header stacking (auto-stacks to cards on mobile) + clay-pill CTA + for-sale seam divider.
  - Egg page shipped: Split-Hero C, Dial 1 clay, K1 Receipt, Table A → Congo differentiates via hero+dial+TOC+K4.
- **Advantage/moat section (APPROVED):** "Is this seller legit?" verification block (Info-Gain #1). Claims bounded by Verified-Claim Ledger (USDA AWA · CITES captive-bred docs · Midland-TX address · video-call-before-payment · no Gift Card/WU/PayPal-F&F).
- **Pair page (DECISION):** keep `/congo-african-grey-parrot-pair-for-sale/` LIVE as cross-link sibling; this page single-bird only; run dup `--headers` gate between them.
- **Available birds (LIVE inventory):** Roys (Congo ♂ $2,300), Amie (Congo ♀ $2,500), Bery (Congo ♀ $1,700) as single cards; Jins & Jeni (Congo pair $3,500) as a card cross-linking to the pair page. Sold/retired: Joys, Loti, Carl. Timneh out of scope: Elad, Evie.
- **Price correction:** real Congo singles $1,700–$2,500, pair $3,500 (NOT the stub's stale $1,500/$3,000).
- **Bing disambiguation:** page must read hard as a *parrot* (parrot / Psittacus erithacus / bird / breeder) in title/H1/schema — Bing hijacks "congo…for sale" to the country.
- **Voice:** first-person C.A.Gs plural (locked by CLAUDE.md) — we/us/our; encyclopedic facts stay neutral.
- **Schema target:** Product/AggregateOffer + FAQPage + AggregateRating/Review + BreadcrumbList + ItemList.

## Open Flags
- LLM Visibility not measured for this keyword → run `@cag-llm-keyword-intel` before publish.
- Photos empty in `clutch-inventory.json` → breeder supplies at image-drop (gates the card grid + P1 conversion sections + build start).
- Jins & Jeni is a pair on a single-bird page → render as cross-link card, not full pair content (confirm during outline).

## Constraints
- **CONSTRAINT:** Work on `main` only. Preview + approve before writing any site file. Same content (visual layer only for redesign, but this is a from-scratch content rebuild of a stub).
- **CONSTRAINT:** No visible dates anywhere (schema-only freshness).
- **CONSTRAINT:** Heading Hierarchy Gate — full H1→H6, ≥5 H5 AND ≥5 H6, no skips; outline approval BEFORE any code.
- **CONSTRAINT:** Dup-content gate (`--headers`) vs ALL for-sale + comparison siblings before outline approval AND at final pass. No crossover headers.
- **CONSTRAINT:** New/slightly-different components (for-sale kit) — not old theme, not homepage/comparison components. Equal height/size, fluid, mobile+tablet+desktop, no oversized fonts.
- **CONSTRAINT:** Build starts ONLY after breeder drops AI images/infographics + OG images and says "start."
- **CONSTRAINT:** CITES Appendix-I captive-bred framing; no international shipping; claims inside Verified-Claim Ledger.
- **CONSTRAINT:** Mobile-first — prices/cards/reserve CTAs above the fold (mobile CTR 4.62% vs 0.47% desktop).

---
<!-- Synthesized fields below are filled in at finalization, from the Q&A Log above. -->

## Business Focus
Pull the currently-invisible `/congo-african-grey-for-sale/` (pos 16.45, absent from Google/Bing top-10) into ranking and convert scam-anxious, price-confused buyers by owning the trust gap no competitor fills. Full ground-up rebuild of a thin stub to the egg-page / for-sale-builder standard.

## SESSION CONTEXT
- Page Type: transactional for-sale (money page)
- Target Keyword: `congo african grey for sale` (best variant: `african grey congo for sale`, 11.73% CTR)
- Framework: Strategy A — Trust-First / Anti-Scam Spine — AIDA × EBP × PAS
- Framework Reason: entire UGC layer is scam-terror + price confusion; #2 Google result is itself a scam; no competitor resolves it — play our moat, not the aggregators' volume game
- AIO / GEO Approach: (C) Both — Featured-Snippet capture + Entity-first AIO citation
- AIO Notes: LLM Visibility unmeasured → run `@cag-llm-keyword-intel` before publish; nothing confirmed to protect
- Component Style: transactional for-sale kit (1200px), compact/dense; NOT homepage/comparison components; every component slightly different from egg page
- Visual Plan: NO HTML/CSS infographics — 8 fresh AI images (P1–P8) + reuse existing library + real bird photos + video; prompts in `assets/1WORKING-ON/FOR-SALE-PAGES/congo-page-image-plan-and-prompts.md`
- Audit Status: complete (Sprint 0 competitor-intel + keyword-gap + GSC/Bing)
- LLM Visibility: not measured → run `@cag-llm-keyword-intel`
- Structure.json Entry: yes
- Hub Page: `/african-grey-parrots-for-sale/` (live)
- Internal Links Needed: pair page, comparison cluster, price, shipping, health-guarantee, scams, CITES, diet, near-me/state pages, reviews, `/available/` (Link-First, dup-gate first)

## Today's Target
- Page: `/congo-african-grey-for-sale/`
- Goal: built to egg-page standard; all final checks pass (anti-AI, humour, non-commodity, first-person, Lighthouse, image-opt, GEO/AEO/SEO, entity, keyword-verifier); visible + converting
- Reader: scam-anxious, price-confused buyer; fears ranked scam → CITES/legal → wild-caught → sick bird → support abandonment → cost
- Benchmark: our egg page (for-sale kit) · birdsjungle.com (schema/H2 map, fake reviews) · Parrot Wizard (authority)

## Constraints
[All CONSTRAINT lines are in the Constraints section above — main branch only, preview-before-apply, no visible dates, Heading Gate (H1→H6, ≥5 H5 + ≥5 H6, no skips, outline approval before code), dup `--headers` gate vs all siblings, for-sale kit / new components, build only after image drop + "start", CITES/Verified-Claim Ledger, mobile-first above-fold.]
- **CONSTRAINT (Q13):** compact 350–400px hero · distinct desktop dial TOC (not identical to egg) · keep mobile jumplink · compact sections throughout.

## Repeat / Avoid
- Repeat: egg-page compact hero, sticky desktop dial TOC (as a distinct variant), mobile jumplink, compact section density, truth-forward scam-contrast spine.
- Avoid: identical-looking components/dial to the egg page; HTML/CSS infographics; stale $1,500/$3,000 pricing; header/body crossover with siblings.

## Urgency
No deadline — gated on breeder generating the 8 AI infographics (P1–P8) + dropping OG Congo photos + video, then saying "start."

## Recommended Next Steps
Audit + research done → proceed (in parallel with breeder's image generation):
1. **Sprint 1 — Visual companion** (browser): click-select Hero → CTA components from `assets/1WORKING-ON/FOR-SALE-PAGES/visual-companion-task5.html` + `component-designs/` (for-sale kit; distinct dial TOC variant).
2. **Heading-Gate outline** — full H1→H6 (≥5 H5, ≥5 H6, no skips) for approval.
3. **Dup-content gate** (`--headers`) vs all for-sale + comparison siblings BEFORE outline lock.
4. On image drop + "start" → build with `cag-for-sale-page-builder` → `cag-duplicate-content-gate` (final) → `cag-final-page-pass` → deploy.

## What's Next
[Filled at end of build session.]

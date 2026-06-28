# Session Brief — 2026-06-28

> **Status:** READY — interview complete. Build next.
> **Last updated:** 2026-06-28 (Sprint 0.5 complete)

## Q&A Log (Verbatim)
_(Appended as the interview proceeds.)_

- **Pre-load — Target:** Rebuild `/blog/african-grey-parrot-talking-ability/` (currently a thin 150-line page: H2-only, fails heading gate, no quick-answer/components/images/birds, oversized-uppercase eyebrow bug). Full rebuild to cage-setup standard, 3,844–4,000 words, MODERN blog components, NEW distinct layout, Reddit/Quora conversational headers + matching opening paragraphs.
- **Pre-load — Bing console keywords:** "how many words talking grey parrot" · "african grey parrot how they talk" · "can a timid african grey parrot talk" · "how many words can a african grey learn" · "can african greys say multiple syllable words" · "can african greys talk ai overview" · "african gray likes to talk before bedtime" · "african gray bird do they talk" · "african grey parrots talking ability".

## Decisions Log
- Page IS in `data/structure.json` (blog cluster) → no structure-architect needed.
- Workflow: Sprint 0 (gap matrix 2026-05-15 exists) → Sprint 0.5 grill-me (this) → visual companion during build.
- **Header style:** Quora-led + FAQ accents (AI-citation fit; page has a "talk ai overview" keyword). Reddit reserved for money pages (price, best-place-to-buy).
- **Layout:** Timeline-spine (hero = talking-development timeline infographic 0–6mo→5yr+; spine follows timeline; + Alex/Pepperberg science block + Congo-vs-Timneh talker table + "will MY bird talk?" decision tree). Distinct from cage-setup's zoned-blueprint grid.
- **AIO/GEO:** Both — quick-answer box (Position 0) + declarative entity-dense sections + FAQPage schema (ChatGPT/AIO/Perplexity). Driven by "ai overview" keyword.
- **Real proof / moat:** Feature **Maxy** (real talking Congo) + video/clips — strongest E-E-A-T a competitor can't copy.
- **Hero:** Option A — video-led (Maxy `<video>` in hero, H1 + dek + clay CTA beside it; eyebrow #f08070 text-xs lowercase).
- **Counter snippet (CounterSnippet.astro, after H1):** Option 1 "Talking facts" → stats: `#1` Ranked talker · `200–1000+` Word vocabulary · `12–18mo` First words · `30 yrs` Alex science. (All restated in body = Verified-Claim Ledger safe.)

## Header-style map (all remaining posts)
- talking-ability → Quora+FAQ · training → FAQ · price → Reddit · best-place-to-buy → Reddit · vs-eclectus → Quora · facts → FAQ+Quora · health-problems → FAQ (no humor) · beginners → Quora · hub → Conversational.

## Open Flags
- GSC not connected → no live clicks/impressions; steer by Bing-console keywords + gap matrix.
- Cage-setup TASK 4 leftover: Cloudflare Rocket Loader still ON (manual toggle pending breeder) — affects this page's mobile perf too.
- **Q6–10 = "yes, write in real breeder voice."** Safe to write as breed-true breeder observation (timid-bird talking, dawn/dusk vocal bursts, daily-talk method, "no guarantee" honesty, microwave-beep warnings, Congo-vs-Timneh general pattern). NO invented percentages, NO invented named buyer.
- **BLOCKER (no-fabricate): need real specifics for Maxy** — (a) the actual words/phrases Maxy says + rough vocab count + Congo/Timneh + age; (b) a usable clip/video URL or at least a photo. Until provided, Maxy is featured generically ("our talking Congo") with no invented quotes.
- **BLOCKER (no-fabricate): real named buyer/talking story** — provide a true one OR confirm "skip the named case study" (will use a generic, non-attributed framing instead).

---

## SESSION CONTEXT
- Page Type: blog (informational + AI-citation, light decision/commercial undercurrent)
- Target Keyword: "African Grey parrot talking ability" (+ Bing cluster above)
- Framework: Entity-Tree + QAB (declarative entity facts for AIO; QAB on FAQ/snippet questions)
- Header voice: Quora-led + FAQ accents (NOT cage-setup's FAQ-only feel; NOT Reddit — reserved for money pages)
- AIO/GEO: BOTH — quick-answer box (Position 0) + entity-dense declarative sections + FAQPage + VideoObject schema
- Component Style: informational 760px inner / 1200px outer; timeline-spine layout
- Layout (distinct from cage-setup): timeline-development spine + Maxy VIDEO hero proof + Alex/Pepperberg science block + Congo-vs-Timneh talker table + "will MY bird talk?" decision tree + myth-vs-fact accents
- Word count: 3,844–4,000 (match cage-setup)
- Audit Status: gap matrix 2026-05-15 available; full content-audit-agent optional (proceeding from grill-me + research data in skill)
- LLM Visibility: not measured (GSC/LLM-intel not connected)
- Structure.json Entry: YES (blog cluster)
- Hub Page: /blog/ (exists)

## Real-Proof Assets (verified, no fabrication)
- **Maxy** = real **Congo** African Grey (confirmed via homepage copy). Video: `assets/brand/maxy-talking-african-grey-parrots-video.mp4` (3.2 MB, web-ready MP4). Poster: `/african-grey-breeder-with-bird-midland-tx.webp`. Embed with `<video controls preload=none>` + VideoObject schema (mirrors homepage §22). **Do NOT invent Maxy's exact spoken words** — feature the video itself; breeder can add a transcript caption later.
- Available birds grid (clutch-inventory) for the bottom conversion module, same as cage-setup.
- Entities (Verified-Claim Ledger safe): Dr. Irene Pepperberg, Alex the Parrot, contextual speech vs mimicry, object permanence, Psittacus erithacus, Congo vs Timneh, neophobia, PCR DNA-sexing, CITES Appendix I.

## Constraints
- No-fabrication: no invented Maxy quotes, no invented talker %, no named buyer story (skipped).
- NEVER a visible date (schema only). One CTA per page. Line-icons not emoji. First-person C.A.Gs voice.
- Heading Outline Gate + Section Map/Component Gate + visual companion all BEFORE any page code.

## Repeat / Avoid
- Repeat (from cage-setup): responsive srcset + heroPreload mirror, visible byline+signature, lowercase hero eyebrow (#f08070, text-xs), final_page_audit PASS, commit+push.
- Avoid: cage-setup's exact zoned-blueprint layout (each page must look different); thin H2-only structure of the current talking page.

## Urgency
- Part of the "first 4 pages this session" block (hub, cage-setup✅, training, talking-ability). Talking-ability now.

## Recommended Next Steps
1. Visual companion: hero + timeline-spine skeleton options → breeder click-select.
2. Section distribution matrix (A/B/C, framework, word split, special-element slots) → approve.
3. Full H1→H6 heading outline (all six levels, ≥5 H5/H6, no skips) → approve.
4. Build section-by-section → Maxy video + VideoObject → final_page_audit (blog) PASS → commit+push.

## What's Next
[Filled at end of build.]

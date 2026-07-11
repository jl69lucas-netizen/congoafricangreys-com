---
name: reddit-strategy
description: Use when targeting "<keyword> reddit" search queries, building Reddit-modifier landing/resource pages, deciding whether/how a CAG page should cite or link a Reddit thread, or when SERP research shows Reddit UGC outranking us on decision queries (comparison pages, "is X a good pet", "best breeder" queries). Also use when planning LLM/AI-visibility plays for queries where ChatGPT/Perplexity cite Reddit.
tools: [Read, Write, Bash]
---

# Reddit Strategy — Compact "Reddit-Modifier" Pages for C.A.Gs

## Golden Rule
> **Link-First (ALWAYS):** anchors at the START of the sentence — never mid-sentence, never at the end.
> **Confidence Gate:** ≥97% before writing any site file; below it, run the Clarification Checkpoint.
> **First-person C.A.Gs voice** in every page this skill produces; CITES Appendix I / captive-bred-USA framing always.
> **Never fabricate a Reddit quote, vote count, or thread.** Every cited thread is one we actually opened (Reddit blocks Firecrawl/curl/WebFetch — use a headless browser; see `sessions/comparison-research/african-grey-vs-amazon-parrot/Evidence-Log.md`).

---

## Why This Exists (the RED baseline, 2026-07-11)

Our own SERP research proves the gap:
- **r/parrots ranks POSITION 1 on every comparison sub-query we ran** ("African Grey or Cockatoo as a pet?" — `sessions/comparison-research/african-grey-vs-cockatoo/2026-07-08-serp-competitor-research.md`).
- Comparison SERPs are **~80% UGC/forum** — Google has no structured article to rank, so it leans on Reddit (male-vs-female research, 2026-07-05).
- Humans AND LLMs append "reddit" to queries to find authentic answers; **zero CAG pages target any `<keyword> reddit` query today.**
- Our comparison pages already mine Reddit owner language (anti-AI layer) and cite threads as evidence — but we capture none of the "reddit" search traffic those threads earn.

## Core Principle — Compact Keywords + the Reddit Modifier

For a site with moderate authority, **the URL slug + page title supply ~90% of relevance** on long-tail queries. A short page whose slug/title exactly matches a "reddit"-modified long-tail keyword can outrank Reddit itself, because:
1. Ad tools show **zero volume** for "reddit" keywords (nobody bids on them) → low difficulty, real demand (visible in GSC once ranking).
2. A structured, fresh, schema-backed page beats a 3-year-old unstructured thread for the same query.
3. LLMs (Perplexity/Gemini/ChatGPT/AIO) look past the top 10 and preferentially cite pages that **aggregate + structure Reddit conversations** → AI-visibility win.

**This is white-hat:** manually built, genuinely useful pages that summarize real threads, add our breeder expertise, and send readers to the good threads — never scaled/programmatic junk, never fabricated consensus.

## The 5-Step Playbook

### Step 1 — Keyword discovery
- Take the **highest-volume head terms we already target** and append the modifier: `african grey parrot for sale reddit`, `african grey vs amazon reddit`, `best african grey breeder reddit`, `african grey price reddit`, `is an african grey a good pet reddit`, `congo vs timneh reddit`, `african grey talking ability reddit`.
- Mine **GSC** for queries already containing "reddit" (they appear once anything ranks) + the **keyword-universe files** in `sessions/comparison-research/*/` (each has a Reddit/owner-language section).
- Confirm a real thread exists for each target (headless browser). No thread = no page.

### Step 2 — Page spec (compact: 100–400 words body)
- **Slug:** the exact modified keyword, stop-words dropped — e.g. `/african-grey-vs-amazon-reddit/`.
- **Title:** exact query + year — "African Grey vs Amazon Parrot: What Reddit Owners Say (2026)".
- **Structure:** H1 (query) → 40–60-word extractable answer block (AIO/snippet bait) → H2 "What r/parrots owners actually say" (2–4 REAL quotes, attributed as owner quotes, ≤15 words each, linked to the thread) → H2 "What Reddit gets right / what it misses" (our breeder-expertise delta — the moat) → H2 "Our take" (first-person, links to the full comparison/money page) → mini-FAQ (2–3 PAA questions) + FAQPage schema.
- **Heading gate still applies** (H1→H6, ≥5 H5 + ≥5 H6) — use H5/H6 for per-quote attributions, thread citations, and breeder notes; get the outline approved BEFORE build.
- Full design system (Direction D), no visible dates (year lives in title/schema only — title-tag year is allowed; visible body dates are not), one CTA.

### Step 3 — Cornerstoning (authority bridging)
1. Ship 3–5 lowest-difficulty Reddit pages first; wait for first GSC clicks.
2. **From each ranking Reddit page, link at sentence start** to the next-harder Reddit page AND to its money page (comparison spoke → variant page → `/available/`).
3. Repeat up the ladder toward "best african grey breeder reddit 2026"-class money terms.

### Step 4 — Thread curation (the parasitic-SEO lever, used ethically)
- Link ONLY to threads that reflect well on ethical, captive-bred, documented ownership — we pass authority to the threads we *want* ranking.
- **Never link** threads promoting wild-caught birds, undocumented sales, or scam marketplaces; never astroturf, comment-spam, or post our own links to Reddit as part of this strategy.
- The `⚠ CITE OR DROP` rule from the Amazon research applies: an anonymous Reddit stat (e.g. "80% rehomed") is never printed as fact — quote it AS an owner's claim or drop it.

### Step 5 — Hub + integration
- Build ONE resource hub — `/african-grey-reddit/` ("African Grey Reddit Guide: Best Threads, Real Owner Answers") — a curated, sectioned index of the best threads per topic (buying, comparisons, diet, talking, health), each with our 2–3-sentence take. The hub is the LAST page built (same rule as every cluster).
- Existing comparison/blog pages get a Link-First pointer to their sibling Reddit page ("Reddit owners weigh in on this exact question — our summary of the r/parrots thread…").
- After every page: `python3 scripts/generate_sitemaps.py`, commit + push, and log target queries in the session brief for GSC tracking.

## Quick Reference

| Element | Rule |
|---|---|
| Body length | 100–400 words (compact page) — thin is fine, fake is not |
| Slug/title | Exact "reddit" keyword, stop-words dropped, year in title |
| Quotes | Real threads only, ≤15 words, attributed, linked |
| Schema | FAQPage + WebPage; `dateModified` in JSON-LD only |
| Internal links | Link-First; cornerstone ladder easy→hard→money page |
| Cadence | 3–5 pages, wait for GSC signal, then next rung |
| Cannibalization | Reddit page answers "what does reddit say" — it NEVER duplicates the parent comparison's headers/content (run `scripts/dup_content_audit.py`, see skills/cag-duplicate-content-gate.md) |

## Common Mistakes
- **Fabricating consensus** — inventing "Reddit says X" without an open thread in evidence. Every quote traces to a URL we loaded.
- **Writing 2,000 words** — the compact page IS the strategy; depth lives on the parent comparison page one Link-First click away.
- **Duplicating the parent page** — same headers/paragraphs on `/african-grey-vs-amazon-parrot/` and its Reddit sibling = cannibalization. The Reddit page covers the *thread*, not the topic.
- **Linking bad threads** — a high-ranking thread recommending Craigslist sellers is not our friend. Curate.
- **Skipping the heading gate** — compact ≠ exempt; the H1–H6 outline still gets approved first.

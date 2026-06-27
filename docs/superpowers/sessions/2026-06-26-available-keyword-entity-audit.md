# /available/ Cluster — Keyword / Entity / Voice Self-Audit + Competitor Benchmark

**Date:** 2026-06-26 · **Scope:** hub (`/available/`) + 6 bird pages (Roys, Bery, Amie, Elad, Evie, Jins & Jeni)
**Task:** Plan Task 9. **Reporting only — no page rewrites in this pass** (per `feedback_noncommodity_audit_then_rewrite`: classify, then rewrite only the weak ones in a later content pass).

---

## (a) Our per-page primary-keyword counts

Raw occurrence counts (case-insensitive) in each `.astro` source:

| Page | African Grey | for sale | Congo AG | Timneh | hand-raised | DNA | CITES | captive-bred |
|---|---|---|---|---|---|---|---|---|
| **hub** | 58 | 7 | 3 | 36 | 14 | 20 | 22 | 16 |
| roys | 102 | 21 | 56 | 9 | 32 | 38 | 36 | 28 |
| bery | 92 | 16 | 52 | 9 | 31 | 36 | 34 | 30 |
| amie | 94 | 22 | 54 | 9 | 23 | 39 | 37 | 27 |
| elad (Timneh) | 95 | 17 | 10 | 147 | 27 | 37 | 37 | 25 |
| evie (Timneh) | 81 | 15 | 9 | 130 | 24 | 36 | 37 | 25 |
| jins-jeni (pair) | 95 | 17 | 56 | 9 | 32 | 40 | 40 | 34 |

**Read:** No page is thin (all bird pages ≥15 "for sale", ≥81 "African Grey") and none is keyword-stuffed in the head/title — the high counts are body-distributed across 1,800–2,200 words. Congo vs Timneh split is correct (Congo pages lean "Congo African Grey", the two Timneh pages lean "Timneh"). **No SHARPEN/REBUILD flagged on keyword grounds.**

> Minor note: the **hub** has the lowest "for sale" (7) and "Congo African Grey" (3) density. It is an aggregator, so this is acceptable, but a later pass could add 2–3 natural "Congo African Grey for sale" / "Timneh for sale" phrases to the hub intro without stuffing. Low priority.

## (b) Voice / entity / heading verdicts

| Page | first-person (we/our/us) | Heading hierarchy | Filler ("both make exceptional") | Verdict |
|---|---|---|---|---|
| hub | 66 | H1·H2·H3·H4·**H5×5**·**H6×5** ✓ | 0 | **STRONG** |
| roys | 150 | full, 5 H5 / 5 H6 ✓ | 0 | **STRONG** |
| bery | 155 | full, 5 H5 / 5 H6 ✓ | 0 | **STRONG** |
| amie | 153 | full, 5 H5 / 5 H6 ✓ | 0 | **STRONG** |
| elad | 150 | full, 5 H5 / 5 H6 ✓ | 0 | **STRONG** |
| evie | 151 | full, 5 H5 / 5 H6 ✓ | 0 | **STRONG** |
| jins-jeni | 153 | full, 5 H5 / 5 H6 ✓ | 0 | **STRONG** |

- **Heading Outline Gate:** every page carries all six levels with ≥5 H5 **and** ≥5 H6, no skipped levels — passes `feedback_heading_outline_gate` mechanically.
- **First-person voice:** heavy and consistent (150+ markers/bird page) — passes `feedback_first_person_brand_voice`.
- **Non-commodity:** zero generic-filler hits; real lineage in §Parents (James & Lois / Levi & Rily), per-bird settle-in narrative, sibling cross-links. No page reads as commodity AI copy.
- **Geo distribution (Task 8):** each page now owns a distinct regional shipping block with a unique H3 (West/Mountain · Southeast · Midwest · NE/Mid-Atlantic · Texas · pairs-coast-to-coast) — no duplicate-content overlap.

**No page requires a SHARPEN or REBUILD pass.** The cluster is uniformly STRONG.

## (c) Competitor keyword-count benchmark

Top Tier-1 commercial competitors from `data/competitors.json`, scraped via Firecrawl (homepage, `onlyMainContent`, 2026-06-26, all HTTP 200). Counts are conservative hand-tallies of the captured main content:

| Competitor | Platform | ~words (main) | African Grey | "for sale" | CITES | DNA | captive-bred | Real testimonials? |
|---|---|---|---|---|---|---|---|---|
| **afrigreyparrots.com** | WooCommerce | ~750 | ~28 | ~12 | **0** | **0** | **0** | n/a (none) |
| **shadesofgreys.com** | Wix | ~150 | ~6 | ~1 | **0** | **0** | **0** | n/a (all sold) |
| **williamsafricangreys.com** | WooCommerce | ~1,000 | ~30 | ~4 | **0** | **0** | **0** | **No — 9 generic fabricated** |
| **Our bird page (roys)** | Astro | ~2,000 | **102** | **21** | **36** | **38** | **28** | No fabricated (real-review pipeline only) |

### What the competitors do
- **afrigreyparrots:** keyword angle is "**cheap** African Grey parrot for sale" (repeated ~6×). Payment = **bank transfer, CashApp, PayPal Friends & Family**; **48-hour delivery** promise. Both are textbook scam-pattern signals we explicitly counter-position against. Zero CITES, DNA, or captive-bred documentation language. Filler present ("make exceptional lifelong companions").
- **shadesofgreys:** legitimate small MN breeder but homepage is ~150 words, no inventory live, no entity/keyword depth, Delta-shipping-only. Not a content competitor — a referral-style presence.
- **williamsafricangreys:** broadest catalog (African Greys + Blue-Gold Macaws), **9 generic testimonials** (clearly templated — the exact pattern our `project_testimonials_fabricated_removed` memory forbids us from imitating), international shipping (red flag), SMS-only contact. Decent "what we do / why choose us" blocks but **no CITES, no DNA-sexing, no captive-bred-USA documentation framing**.

### Where we win (the moat)
1. **Documentation entities** — CITES (34–40×/page), DNA-sexing (36–40×), captive-bred-USA (25–34×) are essentially **absent from all three competitors**. This is our defensible, CoP17-Appendix-I-aware authority gap.
2. **Depth** — 2,000-word individual listings vs 150–1,000-word homepages. Per-bird pages with real parentage, settle-in narrative, health-guarantee, and IATA shipping specifics.
3. **Trust integrity** — we counter-position against the exact CashApp/F&F + 48-hour + fabricated-testimonial patterns these competitors display, instead of copying them.
4. **Structure** — full H1→H6 hierarchy + Product/Offer schema; competitors are flat WooCommerce/Wix templates.

### Where competitors have something to watch
- **"cheap African Grey parrot for sale"** is a real query afrigrey targets aggressively. We deliberately do **not** chase "cheap" (price-floor + anti-commodity positioning) — correct, but worth a single counter-snippet on the hub or price page ("Why we don't sell 'cheap' African Greys — and what a $185-shipped, CITES-documented bird actually costs") to capture that query defensively. **Low-priority, future content pass.**

---

## (d) Prioritized fix list

| # | Item | Page | Priority | Status | Why |
|---|---|---|---|---|---|
| 1 | Add 2–3 natural "Congo/Timneh African Grey for sale" phrases to hub intro | hub | Low | ✅ **DONE** (commit 30a48fd) | Hub "for sale" density was the cluster's lowest; added 2 natural intro phrases, no stuffing |
| 2 | One counter-snippet answering "cheap African Grey for sale" | `/african-grey-parrot-price/` | Low | ✅ **DONE** (commit 30a48fd) | Added FAQ "Where can I find a cheap African Grey parrot for sale?" — visible accordion + FAQPage schema; reframes to honest all-in value, links to /available/ |
| — | Keyword/voice/heading rewrites | none | — | n/a | **All 7 pages verdict = STRONG; no rewrite warranted** |

> Separately (post-audit, commit 08087a8): Bery vs Amie H1/title/meta were de-duplicated by life-stage to kill same-sex/same-species cannibalization — not an audit-(d) item but resolved in the same session.

**Bottom line:** the `/available/` cluster is keyword-healthy, voice-consistent, structurally compliant, and entity-deep in exactly the areas (CITES / DNA / captive-bred documentation) where every scraped competitor is empty. Only two low-priority, optional additions surfaced — both for a later content pass, neither blocking.

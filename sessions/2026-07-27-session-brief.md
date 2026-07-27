# Session Brief — 2026-07-27

> **Status:** IN PROGRESS — Sprint 0.5 orientation. Resume with `grill-me --resume`.
> **Last updated:** Sprint 0.5, pre-fill pass
> **Next question:** Q5 (Constraints) · Q10 (Framework blend) · Q11 (AIO/GEO) — all others pre-filled from the master brief + Sprint 0
> **Program:** for-sale cluster, group of 7. Page 1 of 7 = `/baby-african-grey-parrot-for-sale/` (page 7 of 22 cluster-wide).

## Q&A Log (Verbatim)

**Pre-fill source:** `sessions/2026-07-25-for-sale-page-master-brief.md` (Part I + II) + the breeder's 2026-07-27 master brief message + `sessions/2026-07-27-baby-page-sprint0-research.md` (approved).

**Q1 — Outcome:** Rebuild `/baby-african-grey-parrot-for-sale/` to the for-sale kit standard, live on `main`. First of 7: baby → adoption-cost → congo-pair → affordable → grey-african → male-african-gray → breeding-pair.

**Q2 — Traffic Reality:** 16 queries / 89 impressions / **0 clicks**. Top: "baby african grey parrot for sale in california" 30 impr @ 25.1; "african grey parrot chicks for sale" 22 impr @ 39.0; "african grey babies for sale near me" **@ pos 3.0**.

**Q3 — Worst Performer:** This page — 89 impressions, zero clicks, 12 KB stub with ~4 H2s and stale prose.

**Q4 — Customer Journey:** Buyer searches a baby/chick/near-me query → lands on a SERP where #1 and #2 sell 6–8-week unweaned babies at $850 → they either get scammed or bounce to Reddit, where the top answer is "there are no legitimate websites." Breaks at trust, not at price.

**Q5 — Constraints:** "None — proceed as planned." No freeze, no untouchable pages, nothing pending from another session. Build → gates → deploy → next of the 7.
**CONSTRAINT:** _(none declared 2026-07-27)_

**Q6 — Specific Target:** `/baby-african-grey-parrot-for-sale/` (exists on disk, REBUILD mode).

**Q7 — Done Looks Like:** 22+ sections · full H1–H6 with ≥5 H5 and ≥5 H6 · dup-gate 0 non-whitelist crossovers (body + headers) · `final_page_audit.py --for-sale` PASS/PASS-WITH-WARNINGS · `page_hardening_scan.py` clean · live 200 · sitemaps regenerated.

**Q8 — Reader Profile:** First-time or returning grey buyer hunting a *baby* specifically. Fears, ranked for THIS page: (1) being sold an unweaned chick they can't keep alive; (2) scam/deposit loss; (3) price disorientation — they've been told $850 or $8,000 and believe nothing in between exists; (4) sick bird / PBFD; (5) post-sale abandonment. Leaves when the page reads like every other listing farm.

**Q9 — Benchmark:** Internal — `/african-greys-for-sale-with-health-guarantee/` (nearest structural analogue, trust-led with a transactional layer high on the page). External offer benchmark: `mybabyparrot.com` (Parrot Wizard) — health guarantee + personal delivery + starter kit + waiting list.

**Q10 — Framework:** **EEBP × PDB × BAB × QAB** (approved). PDB = Problem→Diagnosis→Bridge, carrying the real-thread red-flag checklist as a diagnosis. BAB = Before→After→Bridge, carrying the documented transformation (syringe-feeding a 9-week-old vs a weaned baby that self-feeds). Neither PDB nor BAB is used anywhere in the cluster.

**Q11 — AIO / GEO Approach:** **(C) Both** — Featured Snippet capture on "how old should a baby African Grey be before you buy" and "how much is a baby African Grey" (both have a clean factual answer: 12–16 weeks; $1,500–$3,500), PLUS entity-first coverage. Resolution for the conflict with the conversational-opening rule: **declarative first sentence, conversational second.** AAV position paper is the citable authority for AI engines.

**Q12 — Visual Plan:** Full BABY folder approved for use (breeder, 2026-07-27). Hero = `three-congo-african-grey-babies-available.jpg`; `curious-baby-african-grey-chick.jpg` relocated to the nursery/hand-feeding section. Infographic prompt pack delivered at Sprint 1; breeder drops assets at the Asset Gate.

**Q13 — Repeat / Avoid:** Last brief (2026-07-26) item 3: *"Next for-sale group — read the impeccable-lessons doc first (§1 verify-the-gate, §8 command sequence), then /cag-for-sale-page-builder."* Done. **Avoid:** mirroring sibling prose (Trap #1); treating AI `.webp` as OG photos (Trap #2); fixing a page before verifying the gate is right (§1).

**Q14 — Urgency:** Not stated. Sequential — 7 pages, this one first.

## Decisions Log

- **Angle (APPROVED 2026-07-27):** "Weaned First. Shipped Second. Never the Other Way Round."
- **Hero photo (APPROVED):** `three-congo-african-grey-babies-available.jpg`; unweaned-chick photo moves to the nursery section with honest framing.
- **Image scope (APPROVED):** full 22-file BABY folder, sorted by extension per Trap #2, placement approved at Sprint 1.
- **Style-letter count (APPROVED):** 5–6 desktop + 5–6 mobile, matching the five built siblings.
- **Avail facet:** Avail-B faceted by **weaning stage / age band** — unused by all six siblings.
- **Geo lead:** California first (30 of 89 impressions; Review 1 is a CA buyer).
- **Reviews:** Joanna Thomas (Oildale, CA) + Anthony Tershal (Lakewood, WA) — verbatim, never altered.

## Open Flags

1. **`structure.json` has no entry for this slug** (0 matches). Every for-sale sibling shipped without one too — treating as a cluster-wide gap, not a blocker for this page. Recommend a single `@cag-structure-architect` pass across all 22 for-sale slugs after this group, rather than 7 one-off edits.
2. **LLM Visibility never measured** on any for-sale cluster page (carried from master brief Open Flag #10). Unchanged here.
3. **`final_page_audit.py` `FORSALE` roster (line 360)** must gain all 7 new slugs or the auditor silently skips them (Trap #17).
4. **9 new competitors** found in Sprint 0, absent from `data/competitors.json` — register after the build group.
5. **67 tracked `assets/brand/` files show deleted in git** — renamed on disk, pre-existing, unrelated. Do not sweep into a build commit.
6. **`/last30days` not installed** and not installable from a non-interactive session; Reddit obtained via Playwright (ladder step 3).
7. **`data/keywords/` is empty** — no stored fan-out. Generating this sprint.
8. **Third review image** (`jesse-review-…jpg` from the HAND-RAISED folder) was pointed at in §16, but Jesse Ovalle is already used on hand-raised AND dna-tested. Reusing a third time is whitelisted but weakens differentiation — recommend leaving it out; awaiting breeder.

---

## Outcome — Page 1 of 7 SHIPPED

`/baby-african-grey-parrot-for-sale/` **LIVE 2026-07-27**, commit `c2ae89f`, live-verified 200 with new content.

| Gate | Result |
|---|---|
| `page_hardening_scan` | ✅ clean |
| `final_page_audit --for-sale` | **PASS-WITH-WARNINGS** — `no_aggregateoffer`, `house_method` only (same 2 benign as congo/dna/health-guarantee) |
| `dup_content_audit` body | **PASS** — 0 crossovers vs all 6 siblings |
| `dup_content_audit --headers` | **PASS** — 0 crossovers |
| Headings | H1 1 · H2 22 · H3 39 · H4 18 · H5 13 · H6 8 · no skipped levels · AP Title Case |
| Contrast @375 | 463 / 466 (3 flags = decorative glyphs in shared chrome) |
| Horizontal overflow @375 | none · 0 elements wider than viewport |
| Locked specs | hero 395px · dial 196px · rows 26px · 6 counter cards @74px · 21 seams / 22 sections |
| Content | ~7,350 words · primary density 0.86% · 135 first-person · 0 AI tells · 12 `#reserve` CTAs · 11 external links / 8 domains |

### Reusable findings banked
1. **IntersectionObserver is inert in an occluded browser pane.** The dial scroll-spy read as "static" in the Browser pane, on my page *and* on the live Timneh page. Playwright proved both work (ring 5→14→27→45→77). **Fifth checker to cry wolf** — had I "fixed" it I'd have broken working code on two pages.
2. **A dead external URL got through.** `aphis.usda.gov/aphis/ourfocus/...` is gone (site restructure); replaced with `/awa/apply`. Note `curl` returns `000` for *all* aphis.usda.gov from this environment, so curl cannot be used to validate .gov links here — Firecrawl can.
3. **`.sr-only` does not exist globally.** Any page using it must define it in page scope.
4. **`form-control-ios-zoom`** — new hardening-scan catch; inputs need a 16px floor. Siblings were clean, so this was mine alone.

## What's Next

1. **Page 2 of 7 — `/african-grey-parrot-adoption-cost/`** (360 impressions; note "african grey parrot price in india" 43 impr @ pos 1.0 is out-of-market and must NOT be chased). Trust-page cluster → Split-Hero C per the locked table.
2. **Two fast wins sit behind it** — by impressions the batch ranks `grey-african-parrots` (915) and `congo-pair` (497, **the only cluster page with real clicks**: 10 @ pos 9.0) above the rest. Worth reordering if the breeder wants revenue sooner.
3. **Register the 9 new competitors** found in Sprint 0 (`buyafricangreyparrots.com`, `mybabyparrot.com`, `theavianexchange.com`, `exoticglobalparrotsfarm.com`, `graybreedersfoundation`, `parrotsoftheworld`, `midnightparrotplace`, `prunedalebirdfarm`, `parrotstars`).
4. **Breeder to regenerate 2 infographics** — `baby-grey-breeder-red-flags-checklist` (gibberish text) and `congo-vs-timneh-baby-at-four-months` (prompt text baked in as title, British "colour", shows adults not babies). Slots are live with an HTML checklist and a real photo respectively; filenames unchanged so they drop straight in.
5. **Root cause for the breeder's generator:** it is baking *prompt instructions* in as visible labels ("green tick", "clay cross", "size, tail colour (red vs maroon), beak"). Future prompts should state label text as literal copy, not as an instruction.

## Open Flags carried forward
- `structure.json` has no entry for any for-sale slug — recommend one `@cag-structure-architect` pass across all 22 after this group.
- LLM visibility still unmeasured on the whole cluster.
- 67 tracked `assets/brand/` files show deleted in git (renamed on disk); pre-existing, deliberately not swept into this commit.

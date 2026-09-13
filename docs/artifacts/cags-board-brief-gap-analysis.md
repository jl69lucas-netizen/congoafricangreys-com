## The Short Answer

The two boards already carry the planning half of the Universal Page Build Brief: the restated brief, H1 and meta picks, the H1–H6 outline with its collision check, the FAQ questions, the links plan, entities, the component tuple and options, asset slots and the Approve button. **9 brief items are fully on the boards and 5 are there only in part.**

**14 brief items that belong in an approval sitting are missing.** Four of them are cheap because the record already holds the data or nearly does. For example, the hub record carries 12 image prompts and the near-me record carries 7, and the board shows none of them.

**10 brief areas should stay off the board.** A gate, script or skill already owns each one: hardening, render checks, the measurement ledger, deploy and IndexNow, and the standing facts.

Checked against: the brief artifact `f63b8e4f` (v2.2, §0–§26), `schemas/board.schema.json`, both `data/pages/*/board.json` records, `scripts/build_page_board.py`, and the published boards `adfa7c65` (hub) and `f260ac31` (near-me), on 2026-09-13.

## Already on the Boards

| Brief § | Brief item | Board block | State |
|---|---|---|---|
| §0, §1h | Restate goal · scope · gates · done · out of scope | 1. Brief | ON BOARD |
| §10 | Strategy, one recommended, trade-off named | 1. Brief — strategy + angles considered | PARTIAL — angles with hook and trade-off, not two full strategies + a blend with section architecture, conversion path and risk |
| §5, §6b | Research sources with fetch dates | 1. Brief — research used | ON BOARD |
| §12 | Five H1 variants, breeder picks | 2. H1 and meta | ON BOARD |
| §7d | Three meta sets, one recommended | 2. H1 and meta | ON BOARD |
| §12 | H1–H6 outline, header dup check before approval | 3. Outline — collision flags inline | ON BOARD |
| §6a | PAA / FAQ question set | 3. Outline — Q01–Q12 with the FAQ collision check | ON BOARD |
| §16c | Link-First internal and external anchors, library-checked | 3. Outline — per-section links | ON BOARD |
| §11 | Section distribution matrix | 3 + 4 — category letter, framework, word band, 5 keyword columns | PARTIAL — see additions 2 and 3 |
| §8 | Entities with authorization, section × entity | 5. Entities — graph + matrix | PARTIAL — no count against target, no co-occurrence (addition 13) |
| §13 | Distinct component tuple | 5b. The kit — hero, dial, rail, TOC, FAQ | PARTIAL — takeaway and table are in the record but not shown; stepper and newsletter placement are not recorded (addition 4) |
| §13 | Options minus sibling-owned components | 6. Component options — thumbs, picks, notes | ON BOARD |
| §15c | Asset slot list | 7. Asset slots | PARTIAL — page-level slots only; per-section images and prompts are not shown (addition 1) |
| Gates 3–5 | One approval, hash-locked | 8. Approve | ON BOARD |

## Missing — Tier 1: The Record Already Has It, or Nearly

| # | Brief § | What is missing | What the record holds today | How to add |
|---|---|---|---|---|
| 1 | §15b, §15c | **Per-section image plan and the infographic prompt pack.** Every H2/H3/key H4 needs an image; alts may not repeat. | `sections[].images` — hub 12 entries, near-me 7, every one with a `prompt`. The board renders 0 of them. | Render each section's images (slot, kind, prompt) under its outline branch. Gate row `image-coverage` WARN for an H2 with no image slot; `alt-duplicate` FAIL. |
| 2 | §11 | **Group label and a grounded Why per section** (MANDATORY / COMPETITOR-BASED / SUGGESTED-RECOMMENDED, with the competitor or source named). | `category` A/B/C shown as a bare letter with no legend. C = "ours alone" per the pipeline review; the A and B mapping is to confirm. No `why`. | Add `why` + `why_source` to each section. Show the group name, not the letter. Gate row `section-why-missing` WARN. |
| 3 | §7b | **All eight keyword types.** | Five arrays: primary, lsi, longtail, brand, geo. Missing: conversational/voice, comparison, solution, transactional. | Add four arrays and four distribution columns. Counts stay ceilings, as block 4 already says. |
| 4 | §13 | **The whole tuple.** | `tuple.takeaway` (hub k1+k2, near-me k3+k4+k5) and `tuple.table` (table-g, table-i) exist but are not in the kit strip. No stepper field. No newsletter placement. | Add takeaway and table to block 5b. Add `tuple.stepper` and `tuple.newsletter` (placement: after which section). Ledger rows extend to match. |

## Missing — Tier 2: Decisions the Sitting Should Make

| # | Brief § | What is missing | How to add |
|---|---|---|---|
| 5 | §10, §16d | **CTA plan** — cadence every 500–700 words, branded anchors, `#reserve`, the one-global-CTA rule. | `brief.cta` {cadence, anchors[], destination, global_cta} and `cta: true` on sections. Gate row `cta-gap` WARN when the word bands between two CTA sections exceed 700 at their midpoint. |
| 6 | §14 | **Tool or special-element decision**, with SERP/query evidence, or "none" with the evidence named. | `brief.tool` {pick, evidence, trade_off}. Gate row `tool-undecided` WARN on for-sale and hub pages. |
| 7 | §8, §16d | **Schema plan** — Product + Offer per bird or AggregateOffer, FAQPage, never a sold bird InStock. | `brief.schema` {types[], offer_model}. At release the gate compares it with the JSON-LD in `dist/`. |
| 8 | §13 | **Hero refresh delta spec** — which allowed deltas were chosen; never the palette. | The strip names the axis only ("refresh: inventory-tiles"). Add `tuple.hero_delta` {axis, changes[]}. Validation refuses "palette". |
| 9 | §0, §4, §5 | **URL family, redirect map and baselines** — both engines, export named, inbound links, `NOT FETCHED — barrier`. | `brief.url_family[]` {url, role, google, bing, inbound}. Rendered as one table in block 1. |
| 10 | §12 | **A/B variants for each major H2** (the brief asks for 5). Only the H1 gets variants. | `sections[].heading_variants`, three for signature H2s only, each through the header pre-check. A radio per section. |

## Missing — Tier 3: Evidence Summaries, Short With a Link

| # | Brief § | What is missing | How to add |
|---|---|---|---|
| 11 | §9 | **Competitor summary** — why each top-5 page ranks, and one paragraph on how we beat them. The angles table is the only competitor trace now. | `brief.competitors[]` {url, why_ranks, gap} + `brief.how_we_beat`, lifted from the Sprint 0 doc. |
| 12 | §7a | **Keyword metric targets** — variation count ≥ 12, primary in the first 100 words, exact-match tag targets. | `brief.keyword_targets`. Targets only; measurement stays in the gates. |
| 13 | §8 | **Entity count against target, and top co-occurrence pairs.** The boards list 36 (hub) and 28 (near-me) distinct ontology refs; the ontology holds 49. The brief's 85–112 counts entities on the page, a different unit, so both need showing side by side. | A count line in block 5 plus `brief.cooccurrence[]` (top pairs from research). |
| 14 | §21 | **LLM visibility baseline** — fetched n/30, barriers named. | `brief.llm_visibility` {fetched, total, cited, barriers[]}. One row in block 1. |

## Recommended Against Earlier — Yours to Reopen

| Item | Brief § | Why it stayed off |
|---|---|---|
| Full keyword universe | §6b, §7 | Too long for a sitting. It lives in the research doc, and block 1 links that doc. Recommended off on 2026-09-12. |
| Eight counter snippets | §7e | On for-sale pages, the dial and rail are the counter pair. The brief still asks for 8 per page, so the two disagree. Recommended off on 2026-09-12. |

## Where the Brief and Today's Rules Disagree

| Topic | Brief says | Current rule / boards | Ruling needed |
|---|---|---|---|
| Meta length | §7d: title ≤ 205, description F1 ≤ 185 or F2 ≤ 300 | Format 1 only: title ≤ 70, description ≤ 160 (for-sale skill, 2026-09-09). The boards follow this. | Update the brief to match. |
| Section count | §11: target 22+ sections for a full transactional page | Each board has 9 H2 section records; the built hub renders H2 9, H3 34. | Either the brief counts every block (hero, counter, TOC, seams) and the units differ, or it is a real gap. Confirm which. |

## Stays Off the Board — Already Owned Elsewhere

| Brief § | Area | Owner |
|---|---|---|
| §1 | Standing facts, voice, Verified-Claim Ledger, method labels | Evidence pass; entity authorization (BLOCKED entities already fail the board) |
| §2, §3 | Skill routing, sprint order | Page-type builder skill |
| §15a | Image sizing and the bake pipeline | Build + render harness (IMG family) |
| §16a–c | Write-from-outline, dup discipline, prose, humor | Dup gate (body + headers), anti-ai-writing, links gate rows |
| §17 | Responsive type, spacing, tables, tap targets | Render harness at 375/768/1280 |
| §18 | Harden pass, contrast, markup↔CSS drift | `page_hardening_scan.py`, impeccable |
| §19 | Gates and gate integrity | Render meta/pages, final audit, cag-gate-integrity |
| §20 | Measurement ledger M1–M18 | `quality_report.py`, render harness, gate report artifact |
| §22 | Deploy, sitemaps, IndexNow | `rules/deploy.md`, `indexnow_submit.py` |
| §24–26 | Reference library, open flags, web-tool path | Session brief and skills |

## How We Add Them

Each addition follows the same five steps the board additions (Tasks 12–16) used:

1. **Schema** — the field in `schemas/board.schema.json`, enforced by `validate_board`.
2. **Board block** — rendered by `scripts/build_page_board.py`, markdown authored once so copy buttons work.
3. **Gate row** — in `pageboard.gate_findings`, WARN first, promoted to FAIL only after one clean cluster.
4. **Test** — in `tests/test_page_board.py`, including a known-broken case for every gate row.
5. **Fill both records** — from the research docs and, for the two built pages, from what shipped in `dist/`. Then regenerate and republish both boards in place.

Written as one plan, `docs/superpowers/plans/2026-09-13-page-board-brief-parity.md`, and executed subagent-driven like the additions: implementer, spec reviewer, quality reviewer per task.

**Timing matters.** Every record edit moves the approval hash. Land the additions **before** the re-approval sitting, so one sitting approves everything.

## Recommendation

**Add Tier 1 (1–4) plus CTA, tool and schema (5–7) now, before the sitting. (Recommended)**

Why, from the records:
- Tier 1 is mostly display. The 19 image prompts, both takeaway sets and both table picks already exist in the records and just aren't shown.
- CTA, tool and schema are decisions both built pages already embody, for example the hub's AggregateOffer + ItemList + FAQPage. Recording them documents shipped fact; nothing new gets decided.
- These seven close the most brief sections (§7b, §10, §11, §13, §14, §15, §16d) for the least new research.

Defer 8–10 and Tier 3 to the Cluster Wave boards. There, no page exists yet, so H2 variants, a hero delta and URL-family evidence change what gets built. On these two pages they would only describe it after the fact.

**Trade-off:** the sitting moves back by the length of the plan (seven tasks). And on these two pages, the new fields record decisions rather than test them.

# Page Board System — Design

**Date:** 2026-09-12 · **Status:** approved in brainstorm, awaiting spec review · **Owner:** the build session
**Parent decision:** Workflow A "Board-First" (`docs/artifacts/cags-sprint-pipeline-review.md`, artifact `e961edb9`, 2026-09-11).
**First run:** hub C `/african-grey-parrots-for-sale/`.

## 1. What this is

One approval sitting per page, on a generated board, before any page code exists. The board shows the restated brief, the H1 pick, the H1–H6 outline with its header collision check, the keyword distribution matrix, the entity graph and section × entity matrix, three to five component options per signature section (drawn from the outline, minus what siblings own), and the image slot list. The breeder picks and approves on the board; the build refuses to start without that record.

**Why, from the record:** eight visual rejections landed after build; zero landed after the picks were made on the homepage canvas. Outline gates clear the same day, so merging them into the board costs nothing. The 32-day asset stall happened because nothing moved while photos were missing; measured slots let build and harden run before the photos land.

## 2. Decisions taken in brainstorm (2026-09-12)

| Question | Decision | Rejected |
|---|---|---|
| Minimum to build before hub C | Records + board artifact + canvas options (the full sitting) | Board without canvas; canvas without data views |
| Where approval is recorded | On the board: picks, notes and one Approve written to the artifact's own database, copied back by a script | Chat approval; artifact comments |
| Entity data | Seed `data/cag-ontology.json` now from the entity catalog + Verified-Claim Ledger; boards reference ids and may propose | No ontology; graphify first |
| Research input for the hub | Banked for-sale sweeps + GSC clusters + Pages A/B Sprint 0, plus the hub's own SERP snapshot and PAA fan-out, stamped with fetch dates | Build the Cluster Intel pack first; Task 13 sketch only |
| System shape | Files-first: `board.json` is the source; one script renders the board artifact, one emits the canvas; picks on the board, tweaks on the canvas | Board as an app; canvas as the board |

## 3. Data model

### 3.1 `data/pages/<slug>/board.json` — one per page, the source of truth

```json
{
  "meta": { "slug": "", "page_type": "hub|for-sale|location|comparison|blog|interior",
            "status": "draft|boarded|approved|built|released",
            "research_as_of": "YYYY-MM-DD", "sources": [ { "path": "", "fetched": "YYYY-MM-DD" } ] },
  "brief": { "goal": "", "scope": "", "gates": [""], "done": "", "out_of_scope": [""],
             "primary_keyword": "", "strategy": { "name": "", "why": "", "trade_off": "" } },
  "h1": { "variants": ["", "", "", "", ""], "recommended": 0, "pick": null },
  "sections": [ {
      "id": "", "n": 1, "heading": "", "intent": "", "category": "A|B|C", "framework": "EEBP|FAB|QAB|PAS|BAB|PDB",
      "words": { "min": 0, "max": 0 },
      "shape": "inventory|compare|sequence|proof|price|nav|narrative|standard",
      "keywords": { "primary": [""], "lsi": [""], "longtail": [""], "brand": [""], "geo": [""] },
      "entities": ["ont:id"],
      "tree": [ { "level": 3, "heading": "", "intent": "", "children": [] } ],
      "images": [ { "slot": "", "kind": "photo|infographic", "required": true, "prompt": "" } ],
      "options": { "candidates": [""], "excluded": [ { "component": "", "owner": "" } ], "pick": null, "note": "" }
  } ],
  "tuple": { "hero": "", "dial": "", "rail": "", "toc": "", "takeaway": [""], "table": "", "faq": "", "h6_prefixes": ["", "", ""] },
  "assets": [ { "slot": "", "kind": "photo|infographic", "w": 0, "h": 0, "required": true,
                "status": "missing|baked", "file": null, "alt": "" } ],
  "approval": null
}
```

`approval`, once written by `board_approve.py`:
`{ "approved_at", "h1": <index>, "picks": { "<section id>": "<candidate>" }, "notes": { "<section id>": "" }, "canvas_version": "", "record_hash": "<sha256 of the record with approval removed>" }`.

Rules:
- The section records are the **only** copy source the canvas and the build may read. No script and no skill reads prose from a sibling page, a canvas, or `dist/`.
- Any edit to the record after approval changes the hash; `status` drops back to `boarded` and the build refuses to run.
- `words` are bands; keyword counts in `keywords` are ceilings, not floors (evidence pass, 2026-09-09).

### 3.2 `data/cag-ontology.json` — one for the site

```json
{ "entities": [ { "id": "ont:cites-appendix-i", "name": "CITES Appendix I", "aliases": [""],
                  "class": "Organism|Documentation|Health|Commerce|Logistics|Place|People|Method",
                  "authorization": "ASSERTED|PROPOSED|BLOCKED",
                  "source": "credentials.md#cites | ledger | data/price-matrix.json | null",
                  "owner_page": "/slug/ | null" } ] }
```

Seeded from `skills/cag-entity-agent.md` (the ~100-entity catalog) and the Verified-Claim Ledger in `.claude/agents/cag-entity-incorporation-agent.md`. The wild-caught family (`WILD_CAUGHT`, `IMPORTED_FROM`, `SMUGGLED`, `UNDOCUMENTED_SALE`) is seeded BLOCKED. A board may add PROPOSED entities; approving the board promotes them to ASSERTED only when a `source` is present, otherwise they stay PROPOSED and the board shows them dashed.

### 3.3 `data/component-ledger.json` — the component map, machine-readable

Converted once from `sessions/2026-07-19-for-sale-component-map.md`: per page, its tuple (hero, dial, rail, TOC shell, takeaway set, table, FAQ shell) and its H6 prefixes; plus the shape → candidate pool table from the pipeline review. `board_approve.py` appends the approved tuple. The markdown map becomes a rendered view of this file.

## 4. The board artifact

`scripts/build_page_board.py <slug>` reads the three files above and writes `docs/artifacts/boards/<slug>.html`, published as an Artifact with the `db` capability (`artifact-capabilities` skill loaded before writing it). Seven blocks in reading order:

1. **Brief, restated** (rule 6), with every research source and its fetch date.
2. **H1 pick**: five variants, the recommended one marked, a radio to override.
3. **Outline tree** with the pre-write header check run at generation time: every proposed heading compared exact and as 5-word shingles against every heading in `dist/`; matches flagged inline with the colliding page.
4. **Distribution matrix**: per-section keyword counts against the page ceilings and word bands, totals row.
5. **Entities**: a Cytoscape.js graph (cdnjs UMD; colour = class, solid = ASSERTED, dashed = PROPOSED, red = BLOCKED, which fails the board) and the section × entity matrix with the owner page column.
6. **Component options** per signature section: one thumbnail per canvas artboard, each labelled with its candidate name and, where excluded, the sibling that owns it; the **pick control** (radio) and a **note box** per section. Standard sections show the ledger default with no options.
7. **Asset slots**: id, kind, size, required/optional, status, file.

**Approve** writes one document to the artifact database, collection `boards`, doc id = slug: the approval object of §3.1. `scripts/board_approve.py <slug>` reads it back through the Artifact `read_db` action, verifies `record_hash` against the current record, writes `approval` into `board.json`, sets `status: approved`, appends the tuple and H6 prefixes to `data/component-ledger.json`, promotes sourced PROPOSED entities, and writes any canvas text tweaks back into the section records (§5).

The board follows every artifact rule: markdown authored once inside the page for copy buttons, theme tokens on `:root` with both dark blocks, explicit `body` background, one favicon for its life. The generator's output is checked by the meta harness for those rules.

## 5. Canvas options from the outline

`scripts/board_canvas.py <slug>` writes `docs/design/<slug>/` (the canvas format the homepage rounds used, with its `CONTRACT.md`) and publishes it through the `design` skill:

1. For each **signature section** (shape ≠ standard: hero, counter, key takeaway, category-C sections, the primary table, the nav trio), take the shape's candidate pool from the ledger file.
2. Subtract every candidate a sibling owns (`excluded`, with the owner recorded).
3. Fill each remaining candidate with **that section's record only** (heading, opener intent, tree, entity names, slot placeholders). This is the adaptation of `cag-component-variations`: the outline replaces `dist/` as the copy source.
4. Emit **three options × two viewports** (390 mobile, 1440 desktop; 768 is measured in Harden). Cap: five options. Eight signature sections is at most 48 artboards.
5. Cut a Playwright screenshot of every artboard into `docs/artifacts/boards/<slug>/thumbs/` for block 6 of the board.

**Tweaks.** The breeder edits on the canvas and saves. At approval, `board_approve.py` records `canvas_version`. Layout tweaks are read by the build from the saved artboard of each picked option (Artifact `read`). A **text** tweak is treated as the breeder editing the outline: `board_approve.py` diffs the artboard text against the section record and writes the breeder's text into the record, so the record remains the single copy source and the build never reads prose from a picture.

## 6. Handoff, gates, asset lane

**Build** reads `board.json` and nothing else for structure or copy: headings and opener intents from the section records, components from `approval.picks`, layout from the recorded canvas version, images as **measured slots**. A missing slot renders a placeholder box at the slot's exact size so Harden can measure the page before the photo exists.

**`scripts/board_gate.py <slug>`**, run before build and again before release, fails on:
- `approval` missing or `record_hash` ≠ current hash;
- any BLOCKED entity referenced by a section;
- any heading with an exact or 5-shingle match in live `dist/` outside the dup whitelist;
- any tuple combo, TOC/FAQ shell, takeaway pair or H6 prefix the ledger says a sibling owns;
- fewer than 5 H5 or 5 H6 in the tree (advisory on home and location page types, as `rules/headings.md` says);
- a signature section with no pick;
- at release only: a required slot still `missing`.
It prints examined counts and enters `data/quality/rule-index.json` as `enforced: test`.

**Asset lane.** The slot list is the intake checklist. Photo slots are filled from `assets/brand/` where a fitting photo exists (contact-sheet first, per the sourcing traps), otherwise they wait on the breeder. Infographic slots carry their generation prompt in the record; the Gemini pack is generated from the board exactly as Pages A and B's packs were. **Release, not build, waits on required slots.** Build and Harden run against placeholders.

## 7. Tests

- JSON schemas for `board.json`, `cag-ontology.json`, `component-ledger.json`; pytest validates every file under `data/pages/` and the two site files.
- Unit tests: ledger subtraction (a sibling-owned combo never appears in candidates); hash gate (edit after approval → refused); header pre-check (exact and shingle); authorization (BLOCKED reference fails; PROPOSED without source is not promoted).
- End-to-end fixture: a retro-fitted `data/pages/african-grey-parrots-for-sale-near-me/board.json` describing Page B as shipped. It must render a board, produce the expected candidate sets, and pass `board_gate.py` with a synthetic approval. This proves the model can express a real page.
- Meta harness: the generated board HTML satisfies the artifact theme-token and `body` background rules.

## 8. First run: hub C

1. Seed `data/cag-ontology.json` and `data/component-ledger.json` from their sources.
2. Write the hub's `board.json`: brief from plan Task 13 and the §0g role split (national inventory, `AggregateOffer`, links to every spoke, **sheds the state/metro grid**, which the near-me router now owns alone); research from the banked sweeps, the GSC buy/near-me clusters and both Sprint 0 docs, plus the hub's own SERP snapshot and PAA fan-out for "african grey parrots for sale", each stamped.
3. Generate board and canvas; one sitting for the breeder; approve.
4. Build, Harden, Release through the existing gates. Then Task 11 (the three near-me 301s into Page B) and the singular `/african-grey-parrot-for-sale/` retirement into the hub.

## 9. Out of scope

Stage 0 Cluster Intel packs and their refresh routine (the review's second sub-project). Automation lanes (`/goal`, routines, desktop tasks). The `WORKFLOW.md` rewrite. Running graphify. The location-cluster Cluster Wave.

## 10. Files

| File | Change |
|---|---|
| `data/pages/<slug>/board.json` | new, one per boarded page |
| `data/cag-ontology.json` | new, seeded |
| `data/component-ledger.json` | new, converted from the markdown map |
| `schemas/board.schema.json`, `schemas/ontology.schema.json`, `schemas/component-ledger.schema.json` | new |
| `scripts/build_page_board.py` | new: board artifact HTML + header pre-check + thumbs |
| `scripts/board_canvas.py` | new: options from the record, minus the ledger, to `docs/design/<slug>/` |
| `scripts/board_approve.py` | new: read the artifact db, verify hash, write approval, ledger, promotions, text write-back |
| `scripts/board_gate.py` | new: the gate; rule-index row |
| `tests/test_page_board.py` | new: schemas, units, the near-me end-to-end fixture |
| `skills/cag-component-variations.md` | adapt: outline record as copy source |
| `docs/artifacts/boards/<slug>.html` | generated |
| `docs/design/<slug>/` | generated canvas |

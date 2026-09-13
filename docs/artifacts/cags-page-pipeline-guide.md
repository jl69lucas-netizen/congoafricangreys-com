## The Short Version

When you say **"let's work on this page"**, the page moves through eight stages, 0 to 7. Your decisions are concentrated in **one approval sitting** on a generated **Page Board**. Nothing reaches `src/pages/` until that sitting is done.

| # | Stage | Old sprint name | Who drives it | Stops for you? |
|---|---|---|---|---|
| 0 | Session open | Orient | Me | Yes: confirm the restated brief |
| 1 | Research | Sprint 0 | Me | No: published for you to read |
| 2 | Strategy + board record | Sprint 0.5 + Sprint 1 | Me | No |
| 3 | **Approval sitting** | Gates 3–5 merged | **You** | **Yes: the one big gate** |
| — | Asset lane | Asset Gate | You + me, in parallel | Only the release waits on it |
| 4 | Build | Sprint 2 | Me | No |
| 5 | Harden | Sprint 3 | Me | No |
| 6 | Gates + release | Sprint 4 + ship | Me | No: you get the gate report |
| 7 | Bank | Close | Me | No |

**Your three moments:**
1. Confirm the restated brief at the start.
2. Sit the board and press Approve.
3. Drop the photos and infographics the slot list asks for.

The rest runs on the pipeline's own gates, and each stage ends with something you can open: a research doc, a board, a gate report.

Why it is shaped this way: eight page rejections landed after the code was already built, and none landed on the one page whose components were picked on a canvas first. The Asset Gate stalled two pages for 32 days. So the pick moved to the front, and waiting for photos moved off the main line.

## Stage 0 — Session Open

**Starts when:** you name a page, or give me a page `.md` brief.

**What I do, in order:**
1. **Look at the page, don't assume.** Check `src/pages/<slug>/`: does the file exist, how big is it, when was it last changed, what does the live URL return? That decides the mode: new build, rebuild or polish.
2. **Restate the brief (CLAUDE.md rule 6):** goal · scope · gates · what "done" means · what's out of scope. I also tighten any part of your prompt that's ambiguous.
3. **Inventory the data already on disk before calling anything missing:** GSC exports in `data/analytics/` and the FOR-SALE-PAGES CSVs, Bing page reports, prior research under `docs/research/` and `sessions/*research*/`. `NOT FETCHED` is only written after this check, with the barrier named.
4. **Settle the URL family:** singular vs plural, grey vs gray, legacy `/product/` paths, redirect chains, inbound internal links. Consolidate toward the clean, cluster-native slug.
5. **Load the page-type skill:** for-sale → `cag-for-sale-page-builder`, location → `cag-location-page-builder`, comparison → `cag-comparison-page-builder`, blog → `cag-blog-post`.

**Gate — you confirm the restated brief.** If my confidence is below 97% on something, I don't stop. I write down everything that isn't blocked, log the question under `## Open Flags`, and ask you **one** narrow question.

## Stage 1 — Research (Sprint 0)

**What I do:**
- **SERP snapshot** for the primary keyword and its top variations, using Firecrawl Search first: top 10 with title, H1, H2s, page type, schema and prices.
- **Query fan-out:** GSC rows for the keyword stem, autosuggest, People Also Ask, related searches, Reddit and forum language. Every 6+-word conversational query is captured.
- **Competitor inventory:** each competitor's sections, visuals and trust gaps, plus why they rank.
- **Recency sweep** and thread mining (`research-recency`, `reddit-strategy`).

**Rules that hold here:**
- Nothing is inferred. A source that can't be fetched is written `NOT FETCHED — <barrier>`.
- A curl 403 is not a dead link; retry through Firecrawl, then Playwright.
- Don't re-mine what is already banked. The hub reused the for-sale sweeps and added only its own delta.

**Output:** one dated research doc, e.g. `sessions/for-sale-research/<slug>/<date>-sprint0.md`, published as an Artifact + `.md`.

**Gate:** none. You can read it whenever you like, and the board lists it with its fetch date in block 1, where you approve it along with everything else.

## Stage 2 — Strategy and the Page Board Record (Sprint 0.5 + Sprint 1)

This is where the page gets designed, as data rather than as code. I write one file: **`data/pages/<slug>/board.json`**. It is the page's single source of truth: the build, the canvas and the gates all read it, and nothing else.

**What goes into the record:**

| Part | What it holds |
|---|---|
| `brief` | Goal, scope, gates, done, out of scope, primary keyword; **2–3 angles considered**, one chosen, with its trade-off; the **CTA plan**; the **tool decision** with evidence; the **schema plan** |
| `h1` + `meta_set` | 5 H1 variants; 3 titles (≤ 70 chars) and 3 descriptions (140–160), one of each recommended |
| `sections[]` | One record per H2. Each carries: heading, intent, **group + why + source**, framework, word band, shape, the **9 keyword types**, entities, the full **H3–H6 tree**, **image slots with prompts**, **links** (internal and external, library-checked, Link-First), the CTA count, and the **FAQ questions** on the FAQ section |
| `tuple` | The page's chrome: hero, dial, rail, TOC, key takeaway, table, FAQ shell, stepper, newsletter placement, H6 prefixes |
| `assets[]` | The measured image slots: size, required or optional, status, file, alt |

**Checks that run while I write it:**
- **Schema validation.** A record that doesn't describe a buildable page is refused.
- **Header pre-check.** Every heading and FAQ question is compared against every built page: exact, species-swapped template, and 5-word overlap. Colliding headings get rewritten before you ever see them.
- **Entity authorization.** Every entity must be ASSERTED with a source in `data/cag-ontology.json`. A BLOCKED entity, such as anything implying wild-caught, fails the board.
- **Component ledger.** A combination a sibling page already owns is excluded, and an owned shell comes back as a named **refresh**.

**Then I generate and publish two things:**
1. **The canvas.** `python3 scripts/board_canvas.py <slug>` writes up to 3 options per signature section at mobile 390 and desktop 1440, each filled only from that section's own record, never from a sibling. I publish it with the `design` skill, then cut thumbnails with `node scripts/board_thumbs.mjs <slug>`.
2. **The board.** `python3 scripts/build_page_board.py <slug>` writes `docs/artifacts/boards/<slug>.html`, which I publish as an Artifact with a database so the Approve button can save.

**Before the sitting:** `python3 scripts/board_gate.py <slug>` should fail only on `approval-hash` and `signature-no-pick`, which is expected until you pick. Anything else, such as a header collision or a spent H6 prefix, I fix first.

## Stage 3 — The Approval Sitting

**This is the one big gate.** It replaces the old separate approvals for strategy, the distribution matrix, the outline and component selection.

**What you see on the board, top to bottom:**

| Block | What it shows | What you do |
|---|---|---|
| 1. Brief | Restated brief, angles considered (⭐ = chosen), the CTA plan, tool and schema plan lines, research sources with dates | Read and challenge |
| 2. H1 and meta | 5 H1s, 3 titles, 3 descriptions, each with its length, ⭐ = recommended | **Pick one of each** |
| 3. Outline | The full H1–H6 tree, a group label and CTA count on each H2, FAQ questions, every link; a ⚠ on any heading that collides with a live page | Read; a ⚠ must be gone before you approve |
| 3b. Image plan | Every image slot and its prompt; ⚠ on a section with none | Check the pictures you'd expect |
| 4. Distribution | Keyword counts across 9 types, word bands, heading counts, and **why each section is here**, with its source | Challenge any section whose why is weak |
| 5. Entities | Graph + section × entity table (solid = asserted, dashed = proposed, red = blocked) | Spot anything claimed without a source |
| 5b. The kit | The page's chrome: hero, dial, rail, TOC, table, stepper, FAQ, takeaways, newsletter | Read-only; say so if the frame is wrong |
| 6. Component options | 3–5 options per signature section, with thumbnails; greyed-out options a sibling owns; a note box | **Pick one per section**, add notes |
| 7. Asset slots | Every slot's size, status and file | See what photos are still needed |
| 8. Approve | The button | **Press Approve** |

**You can also** edit text on the canvas and save. At approval, that text is written back into the record, so your wording becomes the outline.

**What pressing Approve does:** it saves your picks, notes, H1 and meta choices, plus a fingerprint (`record_hash`) of exactly the record you saw.

**What I do right after:**
1. Read your approval back: Artifact `read_db` → `data/pages/<slug>/inbox/`.
2. `python3 scripts/board_approve.py <slug>` checks the fingerprint (it refuses a stale approval), writes your picks and any canvas text into the record, appends the page's component set to `data/component-ledger.json`, and promotes sourced entities to ASSERTED.
3. `python3 scripts/board_gate.py <slug>` must show **0 FAIL**. Only then can the build start.
4. Commit the record, ledger and ontology.

**What resets your approval:** any later edit to the record's content moves the fingerprint, and the gate fails `approval-hash` until you approve again. Lifecycle fields don't count: status, and an asset's file once a photo is baked. This is deliberate, so a page never ships something you didn't see.

## The Asset Lane (Runs Alongside)

**Photos no longer stop the line.** The asset slots in the record double as the intake checklist.

- **Photos:** first I look in `assets/brand/`, making a contact sheet before assigning anything. What isn't there waits on you. Masters are baked with `scripts/reframe_og.py`: blurfill for portraits, a 4:5 mobile crop, WebP under 100 KB, plus a `-760` sibling. The same photo never appears twice on one page.
- **Infographics:** the image plan in block 3b holds the prompts, and that list is the generation pack. Named birds, heroes and documents are never generated.
- **Document images:** sample certificates only; real paperwork is never published.

Build and Harden run against placeholder boxes sized to the slot, so the layout is measured before the photo exists. **Release waits for every required slot to be `baked`.**

## Stage 4 — Build (Sprint 2)

**What I do:**
- Build `src/pages/<slug>/index.astro` from the approved record **and nothing else**. Headings and openers come from the section records, components from your picks, images into the measured slots.
- **Write from the outline, never from a sibling.** Components and CSS are reused freely; prose is written fresh. The dup gate runs on my own draft, not just at the end.
- Stay inside the page family's own component kit. For-sale pages never import homepage or comparison components.
- Apply the transactional layer where the page type needs it:
  - real bird cards with prices and the shipping line;
  - `Product`/`Offer` schema that matches the schema plan;
  - reserve CTAs at the planned cadence;
  - the inquiry form listing every available bird and its price.
- First-person breeder voice; CITES Appendix I framing; only Verified-Claim Ledger health claims; the two brand-owned method labels.
- Verify in the built `dist/`, never by grepping source.

**Gate:** none. The approval already decided the structure.

## Stage 5 — Harden (Sprint 3)

This stays its own sprint because static gates have passed pages you then rejected on screen.

**What I do:**
- `python3 scripts/page_hardening_scan.py <slug>`, then **confirm every finding on the built page before editing** (`cag-gate-integrity`). Twelve checkers on this site have cried wolf.
- A markup ↔ CSS drift check.
- Contrast recomputed at ship time, never taken from a draft.
- Minimum text size 12.5 px.
- Tables stack on mobile.
- Jump links actually jump.
- Seams match the section count.
- The `impeccable` / `frontend-design` polish pass.
- Measured at **375 / 768 / 1280** in Playwright, never in an occluded browser pane.

**Gate:** the harness. Lighthouse conclusions need 5 runs, because CLS here is bimodal.

## Stage 6 — Gates and Release (Sprint 4 + Ship)

**The gates, in order:**

```bash
npm run test:render:meta
```

```bash
npm run test:render:pages
```

```bash
python3 scripts/dup_content_audit.py <slug>
```

```bash
python3 scripts/dup_content_audit.py --headers <slug>
```

```bash
python3 scripts/evidence_audit.py <slug>
```

```bash
python3 scripts/aeo_audit.py <slug>
```

```bash
python3 scripts/final_page_audit.py
```

```bash
python3 scripts/seam_parity.py
```

```bash
python3 scripts/board_gate.py <slug> --release
```

**What changes at the release gate:**
- Meta picks become mandatory.
- For-sale and hub pages need at least 3 external library links.
- Every required asset slot must be baked.
- The schema plan is checked against the built page's JSON-LD.

**How to read a result:**
- **Meta gate first:** it's the gate that checks the checkers.
- **Read every gate's examined count:** a PASS over zero pages proves nothing.
- **Confirm a failure on the built page before fixing it.**

**Then ship:**
1. `python3 scripts/generate_sitemaps.py` if a page was added or removed.
2. Commit **and push** to `main`. Push is deploy.
3. Confirm the live URL returns 200 and every redirect in the family resolves in one hop.
4. `python3 scripts/indexnow_submit.py <slug>` for **every slug whose rendered output changed**, after the deploy is live, not only the page I edited.
5. Publish the gate report as an Artifact + `.md`.

**Gate:** the harness plus the evidence pass. You get the gate report; release doesn't wait for a second approval unless something changed the approved record.

## Stage 7 — Bank (Close)

**What I do:**
- **Lessons doc:** what broke, the root cause, the reusable fix.
- **Learning loop (`cag-learning-loop`):** if a defect escaped a check that should have caught it, the harness gets the fix. I add the case to the known-broken fixtures and watch the meta gate fail first. No new rule.
- **Session brief:** what shipped, commits, open flags, what's next.
- **Memory:** durable, non-obvious findings only.
- **Deliverables:** every one ships as an Artifact with copy buttons, plus `.md` (rule 13).

## Every Approval Gate, Old vs Now

| Brief gate | What it approved | How it works now |
|---|---|---|
| Gate 0 | Target block | Stage 0: you confirm the restated brief |
| Gate 1 | Canonical URL + redirect map | Stage 0: decided and recorded in the brief's scope and out-of-scope (a full URL-family table on the board is deferred to the location boards) |
| Gate 2 | Research doc | Stage 1 publishes it; you approve it at the sitting through block 1 |
| Gate 3 | Strategy | **Sitting**: block 1 angles |
| Gate 4 | Distribution matrix | **Sitting**: block 4 |
| Gate 5 | H1–H6 outline | **Sitting**: block 3, with the collision check already run |
| Component selection | Hero, TOC, tables, etc. | **Sitting**: blocks 5b + 6 |
| Gate 6 | Asset Gate (hard stop) | Replaced by the asset lane; only release waits |
| Redesign preview (rule 7) | A visual change to a live page | Unchanged: previewed and approved before it touches site files |

## What the Board Gate Checks

`scripts/board_gate.py <slug>` for build, and `--release` for release. FAIL blocks; WARN is a prompt to look.

| Check | Build | Release | What it catches |
|---|---|---|---|
| `approval-hash` | FAIL | FAIL | No approval, or the record changed after you approved it |
| `entity-blocked` | FAIL | FAIL | A BLOCKED entity, e.g. wild-caught framing |
| `entity-proposed` / `entity-unknown` | WARN | WARN | An entity with no source, or one missing from the ontology |
| `ledger-tuple-identical` / `ledger-triple-owned` / `ledger-takeaway-set-owned` / `ledger-shell-owned` | FAIL | FAIL | The component combination repeats a sibling's |
| `ledger-spent-prefix` | FAIL | FAIL | An H6 prefix a sibling already uses |
| `header-collision` | FAIL | FAIL | A heading that copies a live page's heading |
| `faq-collision` | WARN | WARN | A FAQ question that repeats a live heading |
| `header-precheck-examined-zero` | FAIL | FAIL | The pre-check ran on no built pages |
| `min-h5-h6` | FAIL (WARN on home and location) | same | Fewer than 5 H5 or 5 H6 |
| `meta-no-pick` | WARN | **FAIL** | You haven't picked a title and description |
| `meta-length` | FAIL | FAIL | A title over its ceiling, or a description outside 140–160 |
| `signature-no-pick` | FAIL | FAIL | A signature section with no component picked |
| `pick-tuple-mismatch` | WARN | WARN | The nav section's pick disagrees with the recorded TOC |
| `image-coverage` | WARN | WARN | A signature section planning no image |
| `asset-alt-duplicate` | FAIL | FAIL | Two images sharing one alt |
| `cta-cadence` / `cta-gap` | WARN | WARN | Too few CTAs for the words, or a long stretch with none |
| `links-anchor-duplicate` | FAIL | FAIL | One anchor text used twice |
| `links-internal-dead` | FAIL | FAIL | An internal link to a page that isn't built |
| `links-external-missing` | WARN | **FAIL** | A for-sale or hub page with fewer than 3 library links |
| `asset-required-missing` | — | **FAIL** | A required photo not yet baked |
| `schema-planned-missing` / `schema-unparsed` / `schema-examined-zero` | — | **FAIL** | A planned JSON-LD type missing from the built page, a block that doesn't parse, or no built page |

## Rules That Hold at Every Stage

| Rule | What it means in practice |
|---|---|
| First-person breeder voice | We / us / our; neutral register only for taxonomy and cited research |
| CITES Appendix I | Always Appendix I; captive-bred in the USA, fully documented; never wild-caught |
| Prices | The Congo range is $1,500–$3,500; "72-hour" and "3-day" are both correct |
| No fabricated claims | No invented reviews, counts or credentials; unfetched data says NOT FETCHED |
| Verified-Claim Ledger | Health and credential claims only from the ledger |
| Recommend + why | Every set of options has exactly one (Recommended), justified from data, with its trade-off |
| Record authorship | Every value in a board record is written by the controlling session, never by a subagent |
| Gate integrity | Confirm findings on the built page; read examined counts; fix the check when it cries wolf |
| Work on `main`, push is deploy | Commit and push after every build; IndexNow only once the deploy is live |
| Deliverables | Artifact with copy buttons, plus `.md` |

## What Exists Today vs Still Planned

| Piece | State |
|---|---|
| Page Board record, schema, validation | **Built**. `tests/test_page_board.py` has 172 tests |
| Board artifact, canvas options, thumbnails | **Built** |
| Approve on the board → `board_approve.py` | **Built**. Used once, on the hub, 2026-09-12 |
| `board_gate.py`, build and release | **Built**, including the brief-parity checks added 2026-09-13 |
| Brief parity, items 1–7 (image plan, why, keyword types, whole tuple, CTA, tool, schema) | **Built** 2026-09-13 |
| Brief parity, items 8–14 (H2 variants, hero delta spec, URL-family table, competitor summary, keyword targets, entity count, LLM visibility baseline) | **Planned** for the location boards |
| One research pack per cluster, refreshed on a schedule | **Planned**. Research is still per page, reusing banked sweeps |
| Automation (weekly GSC pull, price alerts, nightly harness, LLM probe) | **Planned**. Not running |
| A family-level component exclusion (location pages share nothing with other families) | **Planned**. Needed before the first location board |
| `docs/reference/WORKFLOW.md` rewritten for this pipeline | **Not done**. This page is the current description |

## The Location Pages: What Changes

The location / state / city pages use the **Cluster Wave** variant of this pipeline, per your direction of 2026-09-13.

1. **Your location-pages `.md` arrives:** Stage 0 restates it as the brief.
2. **Groups of 5–6 pages.** Each group gets **its own** hero, TOC, key takeaway, counter and every other component its pages need.
3. **Research per group:**
   - A Firecrawl sweep of competitor location pages that captures their **component types**, not just their keywords.
   - Only then is a library component reused, or a new one designed with `cag-component-variations`.
4. **Hard rule:** no location component is shared with any other page family: for-sale, comparison, homepage, blog or interior. The ownership check gains a family boundary before the first location board is generated.
5. **One board per page, grouped:** sibling pages in a group sit side by side, so headings, geo sets and combinations are settled at design time. Location duplication is the biggest risk, with about 5,857 duplicated passages site-wide today.
6. **Stages 4–7 unchanged,** run per group.
7. **The deferred brief items (8–14) arrive with these boards:** H2 variants, the hero delta spec, the URL-family table, the competitor summary, keyword targets, the entity count and the LLM baseline.

**Trade-off:** a rejection at a group's sitting touches every page in the group, and the first location page goes live later than it would one page at a time.

## Commands Reference

| Stage | Command |
|---|---|
| 2 | `python3 scripts/board_canvas.py <slug>` |
| 2 | `node scripts/board_thumbs.mjs <slug>` |
| 2 | `python3 scripts/build_page_board.py <slug>` |
| 2, 3 | `python3 scripts/board_gate.py <slug>` |
| 3 | Artifact `read_db` collection `boards`, doc `<slug>` → `data/pages/<slug>/inbox` |
| 3 | `python3 scripts/board_approve.py <slug>` |
| Asset lane | `python3 scripts/reframe_og.py …` (blurfill, `--mobcrop 4:5`) |
| 4 | `npx astro build` |
| 5 | `python3 scripts/page_hardening_scan.py <slug>` |
| 6 | `npm run test:render:meta` · `npm run test:render:pages` |
| 6 | `python3 scripts/dup_content_audit.py <slug>` · `--headers <slug>` |
| 6 | `python3 scripts/evidence_audit.py <slug>` · `python3 scripts/aeo_audit.py <slug>` |
| 6 | `python3 scripts/final_page_audit.py` · `python3 scripts/seam_parity.py` |
| 6 | `python3 scripts/board_gate.py <slug> --release` |
| 6 | `python3 scripts/generate_sitemaps.py` (page added or removed) |
| 6 | `python3 scripts/indexnow_submit.py <slug>` (after the deploy is live) |
| 7 | `python3 scripts/quality_report.py` |

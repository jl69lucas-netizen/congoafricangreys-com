# C.A.Gs Sprint Pipeline Review

> Markdown twin of the artifact `docs/artifacts/cags-sprint-pipeline-review.html` (2026-09-11). The three diagrams live in the artifact; their captions are reproduced here.

## The short answer

**Keep the pipeline and fix four things around it.** The gates aren't what wastes your time. The page rework rate fell from **20.8% (May–July) to 8.9% (Aug 12 – Sep 11)**. Harden as its own sprint, the meta gate that checks the checkers, and Bank's back-propagation are the reasons. Don't replace them.

Four things cost you time, measured from the repo:

1. **You only see components after they're built.** Eight visual rejections landed after the code was already in `src/pages/`. Per the session record, the one build that went canvas-first (the homepage close-out) had none after the picked designs were written.
2. **Research is redone for every page.** There are four separate copies of `competitor-30-sweep.py`, and the Distribution-Matrix, Entity-Map and Keyword-Universe files are rebuilt per page.
3. **The Asset Gate blocks the pipeline.** `/buy-african-grey-parrots-with-shipping/` and `/african-grey-parrots-for-sale/` have had zero commits since the cluster stopped on 2026-08-10. That's 32 days with nothing prepared for the day the photos arrive.
4. **The "continuous loops" exist only on paper.** `data/competitor-prices.json` holds 0 snapshots. The LLM Visibility column in `top-pages.md` has never held a number. The GSC exports are dated 2026-04-27.

There's one smaller problem: `WORKFLOW.md` contradicts itself in four places (listed in the fixes section below).

> **Recommended: Workflow A, Board-First.** It keeps every gate and merges Orient and Blueprint into one visual Page Board. At that board you pick the outline *and* the components in a single sitting. The Asset Gate becomes a parallel lane, so the page is ready to release the day the photos land.
>
> **Workflow B, Cluster Wave,** is the better choice once the ~100-page location cluster opens, because there the main risk is pages duplicating each other.

## What the record says

| Signal | Value | Source | What it means |
|---|---|---|---|
| Page rework rate | 20.8% → 14.5% → 13.7% → 11.1% → 8.9% across five windows | `data/quality/rework-ledger.json` | The pipeline works and keeps improving. |
| Checker self-repair | 4.0% → 17.8%; 16 checker fixes vs 8 page fixes in the latest window | same | Keeping the harness honest now costs more than fixing pages. That's healthy while it trends down, so track it. |
| First-run defects | Every one of the last 10 pages shows exactly `A11Y:3` and `DUP:3` | `quality_report.py` §2 | Ten different pages with identical counts looks like a pattern in the check itself, not ten pages sharing a defect. Confirm on a built page before acting (`cag-gate-integrity`). |
| Rules with no test | 15, including `visual-first-workflow` | `quality_report.py` §5 | Candidates for deletion. |
| Rejected after build | 8: eggs v2 kit · Congo-vs-Timneh v1 · the 07-13 comparison-cluster pass · hand-raised rail · horizontal for-sale card · blog v1 · adoption-cost · homepage hero at 649px | lessons + memory files | The most expensive kind of rework. Most were rebuilds or full rounds, not edits. |
| Rejected at canvas | Homepage rounds 1–3 (round 2 "rejected on all four counts"), then round 5 picked | `docs/design/homepage-*/CONTRACT.md` | The canvas moves rejection earlier and makes it cheaper, but rounds pile up when the brief misses the ask. |
| Outline gate wait | Usually the same day | outline files vs commit dates | Approval gates aren't the bottleneck. |
| Asset gate wait | 32 days, two pages, 0 commits | `git log --since=2026-08-10` | This is the bottleneck. |
| Weekly monitoring | 0 price snapshots · LLM Visibility "—" · one manual LLM probe (breeding pair) | `competitor-prices.json`, `top-pages.md` | The Sunday loops have never run. |
| GSC exports | Files dated 2026-04-27 | `data/analytics/` | Traffic context is 4½ months old. |

## What to keep and what to fix

### Keep as is

- **Harden as its own sprint.** Twice the record shows static gates passing a page the breeder then rejected on render.
- **Meta gate before the page gate**, and every gate prints how many pages it examined.
- **Bank's back-propagation**, which sends each lesson into the check that enforces it.
- **Three approval points**, and **write from the outline, never from a sibling.**

### Fix

| Problem | Adjustment | Size |
|---|---|---|
| Components are picked after they're built | Move component choice into the Blueprint as a visual board (see "Visual SEO: canvas or artifact?" and "From outline to 3–5 component options") | A spec |
| Research redone per page | One research pack per cluster, stamped with its fetch date. A page adds only its own SERP snapshot and fan-out. Packs go stale after 30 days. | A script and a routine |
| The Asset Gate blocks the line | Build and harden against measured asset slots. Release waits only for the mandatory slots; photo intake runs in parallel. | A pipeline change |
| Loops exist only on paper | Move them to routines and desktop scheduled tasks (see "Cowork, routines and desktop tasks") | Hours each |
| Checker self-repair climbing | Keep charging escaped defects to the harness, but report self-repair as its own target in `quality_report.py` | One line |
| `WORKFLOW.md` contradicts itself | The four edits below | Minutes |

### `WORKFLOW.md` drift (checked line by line)

- **Line 176** says Sprint 1 runs "once at project start", but the pipeline table (line 31) makes Sprint 1 the per-page Blueprint.
- **Line 333** gives Timneh pricing as "$1,200–$2,500". `cag-timneh-specialist` says $1,500–$1,600.
- **Line 807** says that below 97% confidence you "stop, state uncertainty, ask". CLAUDE.md rule 8 and `WORKFLOW.md`'s own opening (line 11) say *don't dead-stop*.
- **Sprint 2, step 1.5** runs a second component-selection gate that Sprint 1 already approved. Two places decide the same thing.

## Workflow A: Board-First (Recommended)

Same gates, fewer stages, and the visual decision moved to the front.

| Stage | Replaces | Gate | What changes |
|---|---|---|---|
| **0 · Cluster Intel** | Sprint 0 run per page | Review, once per cluster | A cached pack in `docs/research/clusters/<cluster>/`, refreshed by a routine. A page pulls only its delta. |
| **1 · Page Board** | 0.5 Orient + 1 Blueprint + Sprint 2 step 1.5 | **Approve, once** | One sitting: restated brief, H1 pick, outline, distribution matrix, entity map, 3–5 component options per signature section, asset slot list |
| **2 · Build** | Build | none | The outline is the only copy source. The component combo is locked from the board, and images render as measured slots. |
| **3 · Harden** | Harden | harness | Unchanged. Runs under a `/goal` (see "What a loop is") |
| **4 · Release** | Final + Ship | harness + evidence pass | The merge the 2026-07-23 review already named as safe. Releases once the mandatory slots are filled. |
| **5 · Bank** | Bank | lessons mapped | Unchanged |
| **Asset intake** (parallel) | The Asset Gate | slot checklist | Photos arrive through Cowork or a watched folder while Build and Harden run |

**Why, from the record.** Eight post-build rejections versus none after the picked designs were written on the canvas-first homepage. Outline gates clear the same day, so merging them costs nothing. The 32-day stall happened because nothing moved while the photos were missing. With slots, the page is release-ready the day the images land.

**The trade-off.** The board costs more up front: canvas tokens, and one longer review sitting for you. If the board's brief is weak, you pay in canvas rounds instead of rebuilds (the homepage took five). A slot built to spec can also need one more pass once the real photo arrives. The 07-25 hero lesson (blurfill versus a cover crop) shows real images change crops.

*Figure: The pick moves left, and the wait moves off the line. Today, components are first seen in the Build → Ship span where all eight rejections landed, and the Asset Gate stops everything behind it. In Board-First you choose at the Page Board. Photos arrive in a parallel lane that fills measured slots before Release.*

## Workflow B: Cluster Wave

Design and ship a whole cluster together, not one page at a time:

1. **Wave intel**: one research pack for the cluster.
2. **Wave board**: every page's outline and component combo on one board, siblings side by side.
3. **Parallel build**: one Agent per page, each writing only its own files (the canvas-contract pattern).
4. **Wave harden**, then **wave release**, then **wave bank**.

**Why it's attractive.** Collisions between sibling pages get settled at design time:

- Timneh and Congo shared 30 duplicate passages.
- The health-guarantee headings passed the outline gate, then collided with DNA-tested once built.
- The ledger that keeps component combos unique across pages is maintained by hand.
- Bank found the same crop bug on four other live pages.
- Sitewide, about 5,857 duplicated passages sit across the location pages.

**The trade-off.** One rejection hits every page in the wave; the 07-13 comparison-cluster rejection landed on the whole cluster after it shipped. The first page goes live later, and your review sitting is N pages long.

> **When to choose it:** the location cluster, where pages share a structure and duplication is the main risk. Not the remaining for-sale pages, which each wait on their own photos.

## Work you repeat in every sprint

| Repeated work | Where it recurs | Today | Move it to |
|---|---|---|---|
| Competitor and SERP sweeps | Sprint 0, every page | Four copies of the sweep script | **Routine**, weekly or monthly. Writes the cluster pack and opens a draft PR. |
| GSC / Bing performance pull | Sprint 0, Bank, `top-pages.md` | Exports from April | **Desktop task**, weekly, through the local `gscServer` MCP |
| LLM visibility probe | Sprint 0, Final 4c | Never measured | **Desktop task** or **routine** using DataForSEO's LLM-mention tools (connected here, untested for CAG) |
| Competitor price alert | Weekly | Never ran | **Routine**, weekly |
| Sitewide render harness | Harden, every page | Run per page, ~13 min | **Desktop task**, nightly. Catches drift that a shared-component edit pushes onto other pages. |
| Health sweep, broken links, quality report | Monthly | Ad hoc | **Routine**, monthly. Opens a draft PR only for mechanical fixes. |
| Live 200 check + IndexNow | Ship, every page | Manual checklist | **`/loop`** in session, or an API-triggered **routine** after each deploy |
| Photo intake and reframing | Asset Gate | You drop files, then the pipeline waits | **Cowork** on your side, plus a **Monitor** watch in the build session |
| Fact checks (Appendix I, $1,500–$3,500, guarantee) | Every sprint | Scripts + harness | Stays in the harness. It's already mechanical. |
| Header and body duplicate gate | Blueprint, Build, Harden | Manual, three times | The board (at design time), plus Harden |
| Session brief, lessons, memory | Bank | Skills | Stays manual. It's judgment. |

## Cowork, routines and desktop tasks

### What each surface actually is (checked against the docs 2026-09-11)

| Surface | Runs on | Local files | Pushes | Min interval | Survives closing the session |
|---|---|---|---|---|---|
| `/loop` | Your open session | Yes | As the session does | 1 min | No (recurring tasks expire after 7 days) |
| `/goal` | Your open session | Yes | As the session does | Every turn | Restored on resume |
| Desktop scheduled task | Your Mac, app open and awake | Yes | Yes | 1 min | Yes (one catch-up run after sleep) |
| Routine | Anthropic cloud, fresh clone | No | Only `claude/*` branches, then a draft PR | 1 hour | Yes |
| Cowork | Desktop, web, phone | Yes, on desktop | Not a code surface | Has its own scheduled tasks | Yes |

A correction to my own research agent, which got two things wrong. The docs say Cowork is on **Pro, Max, Team and Enterprise**, and Cowork **does** have scheduled tasks.

### Routines (cloud, runs with the laptop closed)

- **Weekly intelligence:** price alert, rank tracker, keyword gap. Output is a draft PR titled `intel: week of …`. This is the hybrid the parked managed-agents artifact already recommends.
- **Monthly site health:** `health-sweep.sh`, broken links, sitemap check, `quality_report.py`. It opens a PR only when the fix is mechanical.
- **Post-deploy:** the GitHub Actions deploy calls the routine's API trigger, and the routine runs the live 200 check plus IndexNow for the changed slugs. It needs `api.indexnow.org` and `congoafricangreys.com` on the network allowlist, and the IndexNow key stored as an environment credential.
- **Rules a routine must keep:**
  - It runs with no approval prompts, so remove every connector that can send a message (the no-auto-send rule).
  - It can't push to `main`, so your merge stays the deploy. That's the rule CLAUDE.md already uses for web sessions.

### Desktop scheduled tasks (your Mac)

- **GSC weekly**, through the local `gscServer` MCP, refreshing `top-pages.md`. The MCP is configured in this session but hasn't been tested against the property.
- **Sitewide `test:render:pages` nightly**, writing a scorecard.
- **LLM visibility weekly**, through DataForSEO's LLM-mention tools, so nothing has to scrape chatbot screens.

### Cowork (your side of the work)

- **Photo intake:** you drop phone photos into a folder. Cowork renames them to the SEO convention, checks each against `data/image-specs.json`, and writes a manifest the build reads. This goes straight at the 32-day stall.
- **Review requests and lead replies,** drafted for you to send.
- **Newsletter and social drafts** from `clutch-inventory.json`.
- **Board review from your phone:** read an artifact and comment on it.
- **Plain-English summaries** of a Bing or GSC CSV, such as the untracked `New-BING-AUGUST-26.csv` in the repo root.

**Keep off Cowork:** page builds, the harness and deploy. They need the repo, a real Chromium and push-to-`main`.

**Not verified:** whether Cowork loads this repo's `.claude/skills` directly. Plugins bundle skills, so test it on first use.

## What a loop is, and which ones to add

A **loop** re-runs the same prompt until a condition holds or a clock ticks. Claude Code has four kinds:

- **`/loop`**: re-runs on an interval (`/loop 5m …`) or at a pace Claude picks (`/loop …`, waits of 1 min to 1 hour). It lives in the session. Recurring tasks expire after 7 days. A project `.claude/loop.md` sets what a bare `/loop` does.
- **`/goal`**: set a finish condition. After every turn, a separate small model judges whether it has been met, can never be met, or neither, and Claude keeps working until it's met.
- **Stop hook**: the same after-every-turn check, set in `settings.json` for every session.
- **Schedules**: routines and desktop tasks. These are durable, not really loops.

**The honest part:** most of what `WORKFLOW.md` calls "Continuous Loops" are schedules. A `/loop` dies with the session, which is why the Sunday agents never ran. They belong in routines and desktop tasks.

### Worth adding

1. **`/goal` for Harden.** Harden is a fix-and-rerun cycle by nature, and the goal gets judged by a different model from the one doing the fixing:

```
/goal For <slug>: test:render:meta passes; test:render:pages scoped with
--grep '<slug>' prints 0 blocking rows with examined > 0 at 375/768/1280;
page_hardening_scan.py <slug> prints 0 ERROR. Do not modify anything under
tests/render/ or scripts/. Stop after 15 turns.
```

The judge can only read the transcript, so the condition demands printed examined counts. It also forbids editing the checks: charging an escaped defect to the harness stays a deliberate, separate act.

2. **A self-paced `/loop` deploy watcher after each push.** It polls the live URL (curl *without* `-L`), confirms the new build, runs IndexNow for the changed slugs, then stops itself.
3. **`.claude/loop.md` as the CAG default.** Read the latest session brief, run the next unchecked gate of the current sprint, append questions to Open Flags, and never pass an approval gate. This makes a long unattended session resumable.
4. **A Monitor watch on `assets/brand/<slug>/`** during a build session. A new photo triggers reframe, slot fill and a rebuild of that one page. This beats polling.

### Not worth a loop

- Weekly intel (use a routine).
- Sprint 0 (one-shot).
- Writing prose and Bank (judgment).
- The duplicate gate (it's a single pass inside the Harden goal).

| Sprint | Loop | Why |
|---|---|---|
| 0 Intel | Routine | Durable, runs without a session |
| 1 Page Board | None | Artifact comment watch already answers your comments |
| Asset intake | Monitor, or Cowork | React to files as they land |
| 2 Build | Bare `/loop` with `loop.md` in long sessions | Resumable autonomy |
| 3 Harden | `/goal` | Converges to a measurable end state |
| 4 Release | Optional `/goal` on `evidence_audit.py` 0 ERROR | Same shape as Harden |
| 5 Ship | Self-paced `/loop` | Deploy polling is exactly its use case |
| 6 Bank | None | Judgment |

## Visual SEO: canvas or artifact?

**Both, split by job.** Anything you *read* goes in a web artifact. UI you *pick and tweak* goes on a `/design` canvas.

| Job | Surface | Why |
|---|---|---|
| See entity connections, outline tree, distribution matrix, cluster ownership, asset slots | **Web artifact (the Page Board)** | It's data. Rendered from files, so it can be regenerated and compared between versions. A graph library such as Cytoscape.js loads from cdnjs, so no hand layout is needed. |
| Choose between 3–5 component options per section, and edit text on them | **`/design` canvas** | You click, edit and compare artboards. Proven: homepage round 5 was picked on the canvas, and the 90-artboard set lives in `docs/design/`. |
| Where each page sits in the pipeline | **Web artifact** (optional dashboard) | A status view, not a design surface |

**Not recommended:**

- **Miro:** the plugin needs authorization in this session, and it moves decisions out of the repo.
- **Figma:** not connected.

Every board opens with the restated brief (CLAUDE.md rule 6). The homepage's round-1 canvas "missed the ask", and the board's first screen is where that gets caught.

## From outline to 3–5 component options

This is the mechanism that makes a component board come straight from the outline:

1. **The outline gets one record per H2 section.** Each record carries: id, heading, intent, category A/B/C, framework, word budget, entities, *shape*, and the section's own content (H3–H6 and bullet intents).
2. **The shape picks the candidate pool** (table below).
3. **The pool draws on two sources, minus one exclusion list:**
   - the live component library (38 components, 104 captures, artifact `6be797ba`);
   - new named-axis variations from `cag-component-variations`, where the library has no fit.
   - The sibling ledger then removes any combo a sibling page already owns.
4. **Every option is filled with that section's own outline content.** Siblings contribute only the exclusion list, never words. That's how "write from the outline, never from a sibling" holds at the design stage. One adaptation is needed: the variations skill currently lifts copy from `dist/`, which suits redesigns of live pages. For a new page, the outline is the copy source.
5. **Only signature sections get options.** That means the hero, counter, key takeaway, the sections that are ours alone (category C) and the primary tables. Standard sections (seam, FAQ, form) take the ledger default with no options shown.
6. **Your pick is recorded** in the component-map ledger, and Build reads it from there.

| Shape | Typical section | Candidates |
|---|---|---|
| compare | Congo vs Timneh, guarantee vs none | Table A stacking · Table B spine cards · Table E ledger · verdict cards · tab toggle |
| sequence | how the test works, reserve → fly | Reserve-path stepper · timeline strip · numbered ledger |
| inventory | available birds | Avail-A · Avail-B faceted · bird cards |
| proof | certificate, paperwork | K1 receipt · K4 clipboard · lab-report table |
| price | what it costs | K2 price tag · K1 receipt · compact table |
| nav | TOC, dial, rail | Dial 1/2 · Rail A/B · TOC fs:01–05 |
| narrative | myth-bust, owner story | H3-image-first layout (`rules/design.md`) + new named-axis variations |

**Scale:** a 23-section page gives about 6–8 signature sections. At 3–5 options each and 2 viewports (Mobile 390, Desktop 1440), that's **36–80 artboards**. The homepage set was 90 artboards for 7 components at 3 viewports. Tablet (768) is measured in Harden, because that's where the defects show.

*Figure: Words reach the canvas by exactly one path: the green one, from the section's own outline record. The sibling ledger's only edge is dashed and subtractive. It removes combos a sibling already owns, which is how write-from-outline holds when options are generated.*

## How entities, angles and frameworks connect

The Page Board draws four views from the same data:

1. **Entity graph.** Colour marks the ontology class (Organism, Documentation, Health, Commerce…). A solid edge is **ASSERTED** (backed by the ledger or a data file). A dashed edge is **PROPOSED** (extracted, not yet backed). Red is **BLOCKED**, which fails the page.
2. **Section × entity matrix.** Shows whether each load-bearing entity appears once, where it does its job (rule 57: 95–105 distinct entities).
3. **Angle and framework ribbon.** The page's argument as one line. On DNA-tested: *"Proof, Not Guesswork"*, going myth-bust → method → certificate → bird, with the PDB → EEBP → FAB → QAB framework chip on each section.
4. **Cluster ownership map.** Which page owns each entity. For example, the sex-behaviour teaser on DNA-tested is capped to link out to male-vs-female, so it doesn't cannibalize.

**What's missing first:** `data/cag-ontology.json` doesn't exist yet (`cag-entity-graph` §1 specifies it), and graphify has never been run (no `graphify-out/`). Step one of the build is that file plus the per-section outline records. The board renders from those two.

The figure below is drawn by hand from the 2026-07-24 DNA-tested blueprint to show what view 1 would look like.

*Figure: A real sample of view 1, drawn by hand from the DNA-tested Sprint 1 blueprint (§0 and §2, rows 5–11). Every entity traces back to something that authorizes it. The one that doesn't is the old live page's "99.9%". It shows up as a dashed PROPOSED edge, which is why the blueprint removed it in favour of the cited "approximately 99%". The real board draws this from data files, not by hand.*

## Which sprints need a visual

| Stage | Need | What to show | Surface |
|---|---|---|---|
| 0 Cluster Intel | Medium | Competitor × topic gap heatmap, SERP snapshot, keyword universe | Artifact |
| 1 Page Board | **High** | Brief, outline tree, distribution matrix, entity views, component options | Artifact + canvas |
| Asset intake | **High** | Slot checklist: slot, required size, status, thumbnail | Artifact, updated by Cowork |
| 2 Build | None | — | — |
| 3 Harden | Low | 375 / 768 / 1280 screenshot strip in the gate report (exists today) | Artifact |
| 4–5 Release | None | A one-line status | — |
| 6 Bank | None | Lessons doc | — |
| Whole pipeline | Optional | Each page's stage, as a board | Artifact |

Two stages carry almost all the value: the Page Board, because that's where the eight rejections were caused, and asset intake, because that's where the 32 days went.

## UI/UX tools to use

| Need | Tool | Note |
|---|---|---|
| Pick and edit component options | `/design` canvas | The early preview of Claude Design inside Claude Code |
| The 3 variations × 3 viewports method | `cag-component-variations` | Needs the outline-as-copy-source adaptation |
| Reference for what already ships | Component library artifact `6be797ba` | Regenerate after any component change |
| Critique, harden, refine | `impeccable` skill + the variations skill's three lenses | Scores against `DESIGN.md`, not taste |
| Does the page communicate | `cag-visual-intelligence` | After Harden, scored |
| Measurement | Playwright at 375 / 768 / 1280 | Never the Browser pane: it reports a zero-width viewport |

The generic global design skills (`ui-ux-pro-max`, `ckm-*`) must never override `DESIGN.md`. The palette is locked.

## Decision for you

This splits into three sub-projects, each with its own spec and plan:

1. **Page Board system.** Outline section records, the board artifact, and canvas options drawn from the outline.
2. **Automation lanes.** Routines, desktop tasks, `.claude/loop.md`, and the Harden `/goal`.
3. **`WORKFLOW.md` rewrite.** The Board-First stages plus the four drift fixes.

> **Recommended first: the Page Board system.** It sits upstream of the most expensive rework (eight post-build rejections, most of them rebuilds), and it's the thing you asked to see.
>
> **Trade-off:** monitoring stays on paper for another cycle, even though the price-alert routine and the GSC desktop task are each a few hours of work and the cheapest wins available.

Nothing in this document changed any code, page or setting.

### Sources

- Routines: https://code.claude.com/docs/en/routines
- `/loop` and scheduling comparison: https://code.claude.com/docs/en/scheduled-tasks
- `/goal`: https://code.claude.com/docs/en/goal
- Desktop scheduled tasks: https://code.claude.com/docs/en/desktop-scheduled-tasks
- Cowork: https://support.claude.com/en/articles/13345190-getting-started-with-cowork
- Repo: `docs/reference/WORKFLOW.md`, `data/quality/rework-ledger.json`, `scripts/quality_report.py`, `sessions/2026-07-24-dna-tested-sprint1-blueprint.md`, `sessions/2026-07-19-for-sale-component-map.md`, `.claude/skills/cag-component-variations/SKILL.md`, `.claude/skills/cag-entity-graph/SKILL.md`, `docs/artifacts/cags-managed-agents-teams.md`

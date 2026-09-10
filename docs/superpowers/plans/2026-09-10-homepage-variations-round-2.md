# Homepage Component Variations Round 2 (D/E/F) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Draw three NEW variations (D, E, F) × three viewports for six homepage components and four homepage tables, publish them as one `/design` canvas the breeder can pan, edit and pick from.

**Architecture:** Same pipeline as round 1 (`docs/design/homepage-variations/`): one `.dc.html` per artboard, per-page `canvas.part-*.json` fragments merged by the controller, seeded with the design skill's helper, published with the Artifact tool. Nothing touches `src/pages/`. Heroes derive from round-1 Hero B with the for-sale `.chero` sizes and image-first on Mobile.

**Tech Stack:** Design Components `.dc.html` (inline styles, static), `canvas.json`, `scripts/design_canvas_probe.mjs` (Playwright), `seed-canvas.mjs`, Artifact tool (`contract: "0.1.31"`).

---

## Brief (restated)

- **Goal:** 3 new designs per component: hero (based on Hero B), counter, desktop dial, mobile jump links, FAQ (shorter, still carries all 21 questions), shipping; plus 3 designs for each of the 4 tables. Mobile / Tablet / Desktop for each = **90 artboards**.
- **Scope:** `docs/design/homepage-variations-r2/` only. No live page edit; the breeder picks, then Rule 7 preview-before-apply in a later task.
- **Gates:** probe (overflow 0, hit targets ≥44 at Mobile, contrast ≥4.5:1, min font ≥12 at Mobile, examined count printed), `seed-canvas.mjs --check` prints `ok:`, hero Desktop grid 350–400px, image-first on Mobile heroes, `hero-midland.webp` in every hero.
- **Done:** canvas published, CRITIQUE.md written, folder committed and pushed, session brief updated, memory saved.
- **Out of scope:** applying any pick to `src/pages/index.astro`; new copy; palette changes.

## File structure

| File | Responsibility |
|---|---|
| `docs/design/homepage-variations-r2/CONTRACT.md` | tokens, invariants, hero brief, axes table (written) |
| `docs/design/homepage-variations-r2/<Component>-<D|E|F>-<Viewport>.dc.html` | 90 artboards (`Main.dc.html` = Hero-D-Desktop) |
| `docs/design/homepage-variations-r2/canvas.part-<page>.json` | 7 fragments, one per page |
| `docs/design/homepage-variations-r2/canvas.json` | merged manifest |
| `docs/design/homepage-variations-r2/CRITIQUE.md` | critique / harden / refine findings + recommendations |
| `docs/design/homepage-variations-r2/cags-homepage-variations-round-2.html` | seeded canvas |
| `scripts/design_canvas_probe.mjs` | banked probe (folder = argv[4]) |

## Tasks

### Task 1: Hero D/E/F (9 artboards) — agent `hero`
- [ ] Read `CONTRACT.md` §5–6, `../homepage-variations/Hero-B-{Desktop,Tablet,Mobile}.dc.html`, `src/pages/congo-african-grey-for-sale/index.astro:759-782,1032-1035`.
- [ ] Write `Hero-D-Desktop.dc.html` and copy it to `Main.dc.html` (identical), plus `Hero-D-Tablet`, `Hero-D-Mobile`, then E and F (9 files + Main).
- [ ] Mobile/Tablet: `<img>` block is the first child of the hero grid. Desktop grid `min-height:352px; max-height:430px`.
- [ ] Probe: `node scripts/design_canvas_probe.mjs /tmp/r2-hero /tmp/r2-hero.json docs/design/homepage-variations-r2` and read the Desktop `#hero-grid` height from a one-off Playwright eval; must be 350–400.
- [ ] Write `canvas.part-hero.json` with 10 artboards (Main + 9) and 3 notes.

### Task 2: Counter D/E/F — agent `counter`
- [ ] Read `CONTRACT.md`, `../homepage-variations/Counter-A-Desktop.dc.html` (copy source), the breeder screenshot `assets/ScreenShots/countrer snippet.png`.
- [ ] Write 9 artboards + `canvas.part-counter.json`. F's seam card shows a 120px strip of `#0f3d2c` hero above so the overlap is visible.
- [ ] Probe; fix; re-probe.

### Task 3: Dial D/E/F — agent `dial`
- [ ] Read `CONTRACT.md` §4 item 5, `../homepage-variations/Dial-A-Desktop.dc.html` (18 sections, 4 parts, copy source), `assets/ScreenShots/current desktop dial.png`.
- [ ] Desktop artboards are the dial alone on a 1440 frame with a cream page stub; Mobile/Tablet artboards show the same dial rendered as it would be at that width (hidden on the live page; draw the "hidden below 1024" state as a caption card plus the dial at reduced frame, as round 1 did).
- [ ] Write 9 + `canvas.part-dial.json`. Probe.

### Task 4: Rail D/E/F — agent `rail`
- [ ] Read `CONTRACT.md`, `../homepage-variations/Rail-A-Mobile.dc.html`, `assets/ScreenShots/mobile jump to section.png`. Top-pinned only.
- [ ] Write 9 + `canvas.part-rail.json`. Every control ≥44px. Probe.

### Task 5: Tables D/E/F for Cvt + Mvf (18 artboards) — agent `tables-1`
### Task 6: Tables D/E/F for Others + Tblc (18 artboards) — agent `tables-2`
- [ ] Read `CONTRACT.md` §6 tables row, the matching `../homepage-variations/Table-<X>-A-Desktop.dc.html` for rows.
- [ ] Write 18 each; tables-1 writes `canvas.part-tables.json` rows for Cvt/Mvf with D at y=0; tables-2 writes `canvas.part-tables2.json` (controller merges both into page `tables`, offsetting y). Probe.

### Task 7: FAQ D/E/F — agent `faq`
- [ ] Read `CONTRACT.md`, `../homepage-variations/Faq-A-Desktop.dc.html` (21 Q/A verbatim), `assets/ScreenShots/faq section-too long.png`. Every variation carries all 21 questions.
- [ ] Write 9 + `canvas.part-faq.json`. Probe. Report Mobile root heights (target: below round-1 C's 1,434px).

### Task 8: Shipping D/E/F — agent `shipping`
- [ ] Read `CONTRACT.md`, `../homepage-variations/Shipping-A-Desktop.dc.html` (copy + tiers), `assets/ScreenShots/shipping section.png`.
- [ ] Write 9 + `canvas.part-shipping.json`. Probe.

### Task 9: Merge, probe, seed, publish — controller
- [ ] Merge fragments (page order hero, counter, dial, rail, tables, faq, shipping; tables2 appended under tables with y offset).
- [ ] `node scripts/design_canvas_probe.mjs … docs/design/homepage-variations-r2` → TOTALS line with examinedTotal > 0; fix any OVERFLOW / HIT<44 / CONTRAST / SMALLFONT.
- [ ] Seed + `--check` prints `ok:`. Publish with Artifact (`contract "0.1.31"`, favicon 🎨, capabilities per roster).
- [ ] Write `CRITIQUE.md` (findings table per component + recommendation per component with measured numbers).
- [ ] `git add docs/design/homepage-variations-r2 scripts/design_canvas_probe.mjs docs/superpowers/plans/2026-09-10-homepage-variations-round-2.md && git commit && git push`.
- [ ] Update `sessions/2026-09-10-homepage-close-session-brief.md` What's Next; save memory.

# PageSpeed 100 × Five Categories Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `/african-grey-parrots-for-sale-near-me/` (Page B), `/buy-african-grey-parrots-with-shipping/` (Page A) and `/african-grey-parrots-for-sale/` (hub C) score 100 on Performance, Accessibility, Best Practices, SEO and Agentic Browsing, mobile and desktop, on Google PageSpeed. The perf gate enforces it at Page Board release so this rework does not recur.

**Architecture:** The breeder's PSI report has four root causes, each verified on 2026-09-13:

1. **CLS 0.266.** This single cause takes Performance to 77 and Agentic Browsing to 2/3, since CLS is one of its scored audits.
   - **CORRECTED DURING EXECUTION.** The plan first blamed the font fallbacks (Georgia-only `local()`, absent on PSI's Linux). Measured in headless Chrome, a simulated font swap moves at most 0.02, even with deliberately wide fallbacks, so fonts are not the 0.266.
   - Delaying *images* reproduced PSI almost exactly: hero-copy 0.156 against PSI's 0.153. `.nmr .hero-field{margin-left:auto}` shrink-wraps a grid item. Before the photo loads, the field is only as wide as its tile chips (228px at 412), so the 2:1 photo box grows from 114px to 190px on load and pushes the copy down 76px.
   - Locally the preloaded photo lands before first paint, which is why every local run read 0.
   - Fix: `width:100%`; loaded geometry is identical at 412/768/1350. A and hub measured 0 with images delayed.
   - The font work (Task 2) still ships as hygiene: generated fallbacks measure 0 swap shift where the old faces measured 0.029 on Page A, and self-hosting drops Cloudflare Fonts' larger files.
2. **`/70de/`, 181 KB.** This is gtag.js injected at the edge by **Cloudflare Google tag gateway**, not Rocket Loader (the old memory was wrong). It causes the unused-JS, forced-reflow and missing-source-map flags. Cloudflare docs: zone-level, "will override the existing script", and Configuration Rules cannot disable it, so the fix is the dashboard toggle.
3. **Desktop hero `uses-responsive-images`.** All three pages ship 400w/760w/1280w with a 520–540px desktop slot, so desktop downloads 760w.
4. **Gate blind spots.** `perf_audit.py` audits `dist/` only, so it can never see edge injections. Its Performance floor is 95, it has no Agentic Browsing category, and the host's fonts decide CLS.

**Tech Stack:** Astro 5 static build, Cloudflare Pages, Lighthouse 13.4.1 (`agentic-browsing-config.js`), Python 3 + pytest, fontTools (metric computation only, scratch venv).

**Done means:**
- PSI mobile + desktop = 100/100/100/100 and Agentic Browsing full marks on all three URLs, confirmed on Google's infrastructure (PSI API or pagespeed.web.dev), not only on this Mac.
- `perf_audit.py` passes locally at the new floors.
- The perf record is wired into `board_gate.py --release`.

**Out of scope:** copy, layout, component picks, board meta picks. Fonts self-hosted = the same woff2 files Google serves, so rendering is identical.

---

## File map

| File | Responsibility |
|---|---|
| `scripts/perf_audit.py` (modify) | Lighthouse 13.4.1 + agentic config; five floors at 0.995; `--live` URL mode; edge-injection diff; writes `data/quality/perf/<slug>.json` |
| `tests/test_perf_audit.py` (create) | pure-function tests: judging floors, agentic fraction, edge diff, record staleness |
| `public/fonts/*.woff2` (create) | self-hosted latin subsets: `newsreader-roman.woff2`, `newsreader-italic.woff2`, `ibm-plex-sans.woff2` |
| `src/styles/fonts.css` (create) | `@font-face` for the three web fonts + computed, Linux-portable fallback faces |
| `src/styles/direction-d.css` (modify) | delete the two approximate fallback faces (moved to fonts.css) |
| `src/layouts/BaseLayout.astro` (modify) | drop Google Fonts link + preconnects; import fonts.css; preload the Plex file |
| `scripts/font_fallback_metrics.py` (create) | computes size-adjust/ascent/descent/line-gap overrides from the woff2 files |
| `tests/test_font_fallbacks.py` (create) | every fallback face lists a Linux metric-compatible local() and no Georgia |
| `public/images/{near-me-page,buy-shipping-page,hub-page}/*-hero-560.webp` (create) | desktop candidate |
| 3 page files (modify) | add `560w` to hero srcset + preload srcset |
| `scripts/pageboard.py` (modify) + `tests/test_page_board.py` | `perf-record-*` release findings |
| `skills/cag-perf-gate.md` + `.claude/skills/cag-perf-gate/SKILL.md` (modify) | five-category 100 protocol, edge features, board wiring |

---

### Task 1: Perf gate — judge five categories at 100, diff edge injections

**Files:** Modify `scripts/perf_audit.py` · Create `tests/test_perf_audit.py` · Modify `package.json` (devDependency `lighthouse@13.4.1`)

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_perf_audit.py
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("pa", pathlib.Path(__file__).parents[1] / "scripts/perf_audit.py")
pa = importlib.util.module_from_spec(spec); spec.loader.exec_module(pa)

def rep(**scores):
    cats = {k: {"score": v} for k, v in scores.items()}
    return {"categories": cats, "audits": {}}

FULL = dict(performance=1, accessibility=1, **{"best-practices": 1}, seo=1, **{"agentic-browsing": 1})

def test_five_categories_are_judged():
    assert set(pa.THRESHOLDS) == {"performance", "accessibility", "best-practices", "seo", "agentic-browsing"}

def test_99_performance_fails_the_100_floor():
    r = dict(FULL, performance=0.99)
    assert pa.judge([rep(**r)]) == ["performance"]

def test_995_rounds_to_100_and_passes():
    assert pa.judge([rep(**dict(FULL, performance=0.995))]) == []

def test_missing_category_fails_rather_than_passing_on_nothing():
    r = dict(FULL); r.pop("agentic-browsing")
    assert pa.judge([rep(**r)]) == ["agentic-browsing"]

def test_median_of_runs_is_judged():
    runs = [rep(**dict(FULL, performance=p)) for p in (0.90, 1, 1)]
    assert pa.judge(runs) == []

def test_edge_injected_scripts_are_those_absent_from_dist_html():
    report = {"audits": {"network-requests": {"details": {"items": [
        {"url": "http://127.0.0.1:4399/_astro/a.js", "resourceType": "Script"},
        {"url": "https://congoafricangreys.com/70de/", "resourceType": "Script"},
        {"url": "https://congoafricangreys.com/cf-fonts/v/x/latin/wght/normal.woff2", "resourceType": "Font"},
    ]}}}}
    dist_html = '<script src="/_astro/a.js"></script>'
    assert pa.edge_injected(report, dist_html) == [
        "https://congoafricangreys.com/70de/",
        "https://congoafricangreys.com/cf-fonts/v/x/latin/wght/normal.woff2",
    ]
```

- [ ] **Step 2: Run to verify fail** — `python3 -m pytest tests/test_perf_audit.py -q` → FAIL (`judge`/`edge_injected` undefined; THRESHOLDS has 4 keys).

- [ ] **Step 3: Implement.** In `scripts/perf_audit.py`:
  - `THRESHOLDS = {k: 0.995 for k in ("performance","accessibility","best-practices","seo","agentic-browsing")}` (0.995 is what PSI displays as 100).
  - `judge(reports)`: median per category, a missing category counts as 0 and returns the failing keys.
  - `edge_injected(report, dist_html)`: Script/Font/Stylesheet request URLs whose path is not referenced in `dist_html`.
  - `run_lighthouse` uses `node_modules/.bin/lighthouse` with `--config-path=node_modules/lighthouse/core/config/agentic-browsing-config.js`. Desktop passes `--preset=desktop`, which cannot be combined with `--config-path`, so desktop instead uses `--form-factor=desktop --screenEmulation.mobile=false --screenEmulation.width=1350 --screenEmulation.height=940 --screenEmulation.deviceScaleFactor=1 --throttling-method=simulate --throttling.rttMs=40 --throttling.throughputKbps=10240 --throttling.cpuSlowdownMultiplier=1`.
  - `--live` flag audits `https://congoafricangreys.com/<slug>/` and prints `EDGE-INJECTED:` rows (FAIL when any Script is injected).
  - Writes `data/quality/perf/<slug>.json` = `{slug, profile, live, lighthouse, runs, median{cat:score}, cls_median, edge_injected, dist_mtime, measured_at}`.
  - The docstring's Rocket Loader note is replaced with the tag-gateway finding.

- [ ] **Step 4: Run tests** → PASS. `npm i -D lighthouse@13.4.1`.
- [ ] **Step 5: Commit** `feat(perf-gate): five categories at 100, agentic config, --live edge-injection diff`

### Task 2: Self-hosted fonts with computed, Linux-portable fallbacks

**Files:** Create `scripts/font_fallback_metrics.py`, `src/styles/fonts.css`, `tests/test_font_fallbacks.py`, `public/fonts/*.woff2` · Modify `src/styles/direction-d.css:30-51`, `src/layouts/BaseLayout.astro` font block

- [ ] **Step 1: Failing test**

```python
# tests/test_font_fallbacks.py
import re, pathlib
CSS = pathlib.Path(__file__).parents[1] / "src/styles"
PORTABLE = {"serif": {"Liberation Serif", "Tinos"}, "sans": {"Liberation Sans", "Arimo"}}

def faces():
    text = "".join(p.read_text() for p in CSS.glob("*.css"))
    return re.findall(r"@font-face\s*{([^}]*)}", text)

def fallback_faces():
    return [f for f in faces() if "Fallback" in f]

def test_fallback_faces_exist():
    assert len(fallback_faces()) == 2

def test_every_fallback_lists_a_linux_metric_compatible_local():
    for f in fallback_faces():
        locals_ = set(re.findall(r"local\('([^']+)'\)", f))
        assert locals_ & (PORTABLE["serif"] | PORTABLE["sans"]), f

def test_no_fallback_is_based_on_georgia_which_linux_chrome_lacks():
    assert not any("Georgia" in f for f in fallback_faces())

def test_web_fonts_are_self_hosted():
    web = [f for f in faces() if "Fallback" not in f]
    assert web and all("url('/fonts/" in f for f in web)
```

- [ ] **Step 2: Run** → FAIL (Georgia-based faces; no self-hosted faces).
- [ ] **Step 3: Download the three latin woff2 files** from the URLs in the Google css2 response (Plex `zYXzKVElMYYaJe8bpLHnCwDKr932-G7dytD-Dmu1syxeKYbSB4Zh.woff2`, Newsreader roman `cY9AfjOCX1hbuyalUrK4397yjIJFJpc.woff2`, italic `cY9XfjOCX1hbuyalUrK439vogqCz_goCYw7oReyJFYYzbARA_n8.woff2`) into `public/fonts/`. They are OFL-licensed.
- [ ] **Step 4: `scripts/font_fallback_metrics.py`**. It reads each woff2 with fontTools and emits overrides against Arial / Times New Roman metrics. Liberation Sans/Arimo and Liberation Serif/Tinos are metric-identical to those, so one set holds on Mac, Windows and Linux. Computation: `size-adjust = font_avg_width / fallback_avg_width` (xAvgCharWidth/UPM of the web font vs the fallback's); `ascent-override = hhea.ascent / UPM / size_adjust`; same for descent and lineGap.
- [ ] **Step 5: `src/styles/fonts.css`**. Three `@font-face` with `font-display: swap`, `url('/fonts/…')`, the Google latin `unicode-range`, and `font-weight: 100 900` for the variable roman files, plus the two computed fallback faces:
  - `'Newsreader Fallback'`: `local('Times New Roman'), local('Liberation Serif'), local('Tinos'), local('Times')`
  - `'IBM Plex Sans Fallback'`: `local('Arial'), local('Liberation Sans'), local('Arimo'), local('Helvetica')`
- [ ] **Step 6:** Delete the two faces in `direction-d.css`. The font stacks keep `Georgia` only after the Fallback name. In BaseLayout, remove both preconnects, the Google stylesheet and its `<noscript>`; `import '../styles/fonts.css'` in the frontmatter; add `<link rel="preload" as="font" type="font/woff2" href="/fonts/ibm-plex-sans.woff2" crossorigin>`.
- [ ] **Step 7:** `python3 -m pytest tests/test_font_fallbacks.py -q` → PASS. `npx astro build`, then confirm that `dist/.../index.html` has no `fonts.googleapis` and does have `/fonts/ibm-plex-sans.woff2`.
- [ ] **Step 8: Visual check.** Screenshot the near-me hero at 375 and 1280 before/after; the glyphs must be identical (same files).
- [ ] **Step 9: Commit** `perf(fonts): self-host the three latin woff2, computed Linux-portable fallback metrics (CLS)`

### Task 2b: Hero field width (the real CLS fix) + harness check

**Files:** Modify `src/pages/african-grey-parrots-for-sale-near-me/index.astro` (`.nmr .hero-field` + `width:100%`) · Add check `layout-image-box-reserved` to `tests/render/checks/layout.ts` with a `known_broken` / `known_good` fixture pair. The probe replaces each above-the-fold `<img>` with a never-loading clone and compares layout.

### Task 3: Desktop hero candidate at 560w on A, B, hub

**Files:** Create three `*-hero-560.webp` · Modify srcset strings at `src/pages/african-grey-parrots-for-sale-near-me/index.astro:220`, `src/pages/african-grey-parrots-for-sale/index.astro:234`, `src/pages/buy-african-grey-parrots-with-shipping/index.astro:185,195`

- [ ] **Step 1:** Pillow, from each 1280w master: resize to 560w, WebP q60. Keep the file under 45 KB.
- [ ] **Step 2:** Insert `IMG + "<stem>-hero-560.webp 560w, "` between 400w and 760w in the `<img srcset>` AND the `heroPreloadSrcset` (they must match, or the image double-downloads).
- [ ] **Step 3:** Build and verify in the browser at 1350×940 DPR1 that `currentSrc` ends `-560.webp` on all three pages.
- [ ] **Step 4: Commit** `perf(hero): 560w desktop candidate on near-me, buy-with-shipping, hub`

### Task 4: Local gate on the three pages, then deploy

- [ ] **Step 1:** `npx astro build && python3 scripts/generate_sitemaps.py && npx astro build`
- [ ] **Step 2:** `npm run test:render:meta && npm run test:render:pages` → no new blocking rows.
- [ ] **Step 3:** For each slug: `python3 scripts/perf_audit.py <slug> --runs 5` and `--mobile --runs 5`. All five categories pass at 100. If Performance misses, read the failing-audits list and fix only what is confirmed on the built page (skills/cag-gate-integrity.md).
- [ ] **Step 4:** Commit + push (push = deploy). Wait for live 200.
- [ ] **Step 5:** IndexNow every slug whose rendered output changed. The BaseLayout font change touches every page, so run `python3 scripts/indexnow_submit.py --all`.

### Task 5: Live verification on Google infrastructure

- [ ] **Step 1: Breeder action (cannot be done in code).** Cloudflare dashboard → Tag Management → Google Tag Gateway → turn off for congoafricangreys.com, then Caching → Purge Everything. GA4 keeps working through our interaction-deferred loader in BaseLayout.
- [ ] **Step 2:** `python3 scripts/perf_audit.py <slug> --live --mobile --runs 3` → `EDGE-INJECTED: none`.
- [ ] **Step 3:** PSI API (quota resets midnight Pacific) mobile + desktop for the three URLs, all five categories, and record the results in the gate report.

### Task 6: Wire the perf record into the Page Board release gate

> **Amended during execution:** a PSI record only exists after deploy, and release runs before push. So local records (both profiles, fresh vs the build; mobile Performance excluded because this Mac's CPU can't stand in for PSI) FAIL release. A missing or superseded PSI record is WARN `perf-psi-pending`, and a failing PSI record or an edge-injected script FAILS.

**Files:** Modify `scripts/pageboard.py` (`gate_findings`, release stage) · `tests/test_page_board.py`

- [ ] **Step 1: Failing tests.** At `stage="release"`:
  - no `data/quality/perf/<slug>.json` → FAIL `perf-record-missing`;
  - a record with any category median < 0.995 → FAIL `perf-below-100`;
  - `edge_injected` containing a Script → FAIL `perf-edge-injected`;
  - `dist_mtime` older than the page's dist mtime → FAIL `perf-record-stale`.

  At `stage="build"` these checks are silent. Both profiles (mobile + desktop) are required.
- [ ] **Step 2:** Implement `perf_findings(slug, stage, perf_dir=ROOT/"data/quality/perf")` and call it from `gate_findings`.
- [ ] **Step 3:** `python3 -m pytest tests/test_page_board.py -q` → all pass (172 + new).
- [ ] **Step 4: Commit** `feat(page-board): release refuses a page without a fresh 100×5 perf record`

### Task 7: Skill + learning loop + sweep

- [ ] **Step 1:** Rewrite `skills/cag-perf-gate.md` (then `register_skills.py --copy`) using superpowers:writing-skills. Cover: five categories at 100; mobile + desktop; `--live` for edge features; the Cloudflare edge-feature table (Tag gateway, Cloudflare Fonts); the Linux-fonts CLS trap; and board wiring.
- [ ] **Step 2:** cag-learning-loop: the escape is family `GATE`. The invariant existed (perf gate), stayed quiet, and tests now cover it (Tasks 1, 2, 6). No new CLAUDE.md rule.
- [ ] **Step 3:** Correct the memories `project_perf_gate` and `project_blog_perf_rocket_loader`: `/70de/` = Google tag gateway, not Rocket Loader.
- [ ] **Step 4: Sweep.** Run `perf_audit.py --runs 3` (mobile + desktop) on the for-sale cluster slugs and list every page still under 100, with its failing audit ids, in the gate report. Font and gateway fixes are site-wide; per-page leftovers (usually hero srcset gaps) become a follow-up batch.
- [ ] **Step 5:** Publish the gate report as an Artifact with copy buttons + `.md` (CLAUDE.md rule 13).

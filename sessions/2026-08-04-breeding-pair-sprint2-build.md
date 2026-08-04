# Session — Sprint 2 Build · `/african-grey-breeding-pair-for-sale/`

**Date:** 2026-08-04 · **Page 10 of 22**, Cluster 3 · **Mode:** REBUILD from a 3,881 B stub
**Branch:** `main` (only `main` auto-deploys) · **Plan:** `docs/superpowers/plans/2026-08-04-breeding-pair-sprint2-build.md`

**Approved inputs — signed off, not re-opened:** Sprint 0 research · Sprint 0.5 strategy (Strategy C,
"Three Pairs, One Standard") · Sprint 1 blueprint (matrix, H1–H6 outline, tuple, meta Set 1, H1 variant A).

---

## Open Flags

### 🔴 FLAG-1 — BLOCKING: two infographics ship defective until swapped

`inf-2-price-ladder` and `inf-7-housing-nest-box` carry a **duplicated-label defect** and were
accepted by the breeder for the build with an explicit instruction to **swap them at the end**.

| File | Defect | Status |
|---|---|---|
| `inf-2-price-ladder.png` | "SALLY & ODIN" renders twice — once on the step block, once in the label row | awaiting regen |
| `inf-7-housing-nest-box.png` | All four labels render twice — FLIGHT LENGTH / NEST BOX / TEMPERATURE / HUMIDITY each appear above *and* below the icon | awaiting regen |

**This flag blocks the final push.** The page may be built, hardened and gated with these two in
place, but it must not go live unswapped.

**Swap procedure — the regenerated files reuse the same filenames, so it is one command:**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/bake_infographics.py \
  "assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR" \
  public/images/breeding-pair \
  inf-2-price-ladder inf-7-housing-nest-box
npx astro build && git add public/images/breeding-pair && \
  git commit -m "fix(breeding-pair): swap regenerated inf-2 and inf-7" && git push origin main
```

Add this line to both prompts before regenerating — it is the only change needed:
`Each label appears exactly once. Do not repeat any heading, label, or name anywhere in the image.`

### 🟡 FLAG-2 — Gemini sparkle watermark on five infographics

A faint sparkle sits bottom-right on inf-1, 3, 4, 5, 6. Harmless in empty space on four of them; on
**inf-1** it overlaps the column-3 footer text ("Ask if they have ever laid at all"). Not blocking —
logged so it is a deliberate accept rather than an oversight.

### 🟡 FLAG-3 — MEMORY.md at 21.1 KB against a 24.4 KB read limit

Wants compacting as its own pass. Not part of this build.

### 🔴 FLAG-4 — OPEN QUESTION: the page has no video, and `.fs-video` is spec-mandated

`page_hardening_scan.py` reports **1 ERROR**: `fs-video` is styled but never rendered, and the
scanner classes it as a SPEC-MANDATED component — "Render them. Do NOT delete the CSS — that
hides a spec violation."

There is **no video asset** for this page in `assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/`.
The nine shipped siblings carry one; this page cannot without a file. Per the 97% confidence gate
the build continued and everything not blocked by this is finished.

**The one question for the breeder:** is there a video of the pairs — a clip of Talker and Jane in
the flight, a nest-box check, a pair being crated — that should ship in `.fs-video`? If yes, drop
it in the asset folder and it goes in. If no, the `.fs-video` CSS should be removed from this page
only, and the scanner's "spec-mandated" list needs this page-type exemption recorded so the ERROR
does not recur on every future for-sale page without footage.

Until answered, this is the single ERROR standing between the page and a clean hardening scan.

### ⚪ NOTED — keyword density is deliberately below the nominal band

Tag placement is fully on-spec: primary in `<title>` ×1, `<h1>` ×1, `<h2>` ×4 (band is 2–4),
`alt` ×1, `<meta>` ×1, and present in the first 100 body words. Total keyword coverage is **545
mentions across 65 distinct terms** against a spec of 85–105 across 40+ — well over.

What is under: **primary-family density at 0.2%** against a nominal 1–2%. That band assumes a
~2,000-word page. At **7,855 body words**, reaching 1% would require ~78 primary mentions and 2%
would require ~157. The same rule ends "never stuffed", so the two halves of it cannot both be
satisfied here. **Deliberate deviation: placement honoured, density not padded.** Recorded rather
than silently accepted.

### ⚪ NOTED — the render harness had never examined this page

`tests/render/targets.json` did not list `african-grey-breeding-pair-for-sale`, so
`npm run test:render:pages` was exiting 0 without measuring it. Registered as
`{"slug":"african-grey-breeding-pair-for-sale","page_type":"for-sale","corpus":false}` —
`corpus:false` on purpose, because the corpus is a frozen one-page-per-type benchmark and adding
to it would move the quality trend baseline.

---

## Verified at session open

- ✅ All seven infographic filenames normalized (three carried a trailing `.png ` + second `.png`)
- ✅ INF-3's `15 MONTHS` marker sits **left of** `3 YEARS` — the one critical spatial check, passed
- ✅ No DNA certificate, lab report, or "DNA sexed" / "DNA certified" text in any of the seven
- ✅ All six pair names (Talker, Jane, Mari, Lake, Sally, Odin) present in `data/price-matrix.json`
- ✅ On `main`, stub is 3,881 B, `dist/` present

---

## Binding constraints carried from Sprint 1 §6

1. **Banned phrases:** *"5–6 years minimum"* · any *DNA-certified* / *DNA-sexed* claim about the
   pairs · any printed incubation-day figure.
2. **Never promise a clutch.** §8 states method, never outcome.
3. **Tameness is our first-hand account of our own birds**, never a species claim.
4. **Prices unchanged**; market comparison published with its reason in the same paragraph.
5. **One link out to Cluster E**, no more.
6. **Write from the outline, never from a sibling.**

---

## Gate results — every gate run twice, verdicts identical

| Gate | Result | Examined |
|---|---|---|
| `test:render:meta` | **PASS** | 198 passed, 24 skipped |
| `test:render:pages` (this page) | **PASS ×2** | 3 tests, vp375 / vp768 / vp1280 |
| `dup_content_audit` body | **PASS ×2** | 0 crossovers involving this page (5,749 sitewide are pre-existing on other pages) |
| `dup_content_audit --headers` | **PASS ×2** | 0 crossover groups involving this page |
| `final_page_audit` | **PASS-WITH-WARNINGS ×2** | 1 WARN: `wordcount_in_band` |
| `page_hardening_scan` | **1 ERROR / 0 WARN** | ERROR is `fs-video`, see FLAG-4 |

### Two gate-integrity findings worth banking

1. **The render harness had never examined this page.** `test:render:pages` exited 0 while the slug
   was absent from `tests/render/targets.json`. Registering it immediately surfaced a real blocking
   defect at all three viewports (a visible `2026-08-03` date stamp). *A PASS is worthless until you
   confirm the gate examined your page.*
2. **The full-suite run is non-deterministic and bails early.** Run 1 failed `blog/cage-setup` +
   this page; run 2 failed `florida` + `blog` + `congo-pair` and reported **"35 did not run"** —
   this page was never reached. A targeted `-g <slug>` run is the only trustworthy second run.

### Visual defect no gate caught

The hero mosaic tiles cropped the 16:9 in-body masters (baked `blurfill --mobcrop 4:5`) into a
portrait box, so they rendered the **blurred filler instead of the birds** — Sally & Odin read as an
out-of-focus photo. Only looking at the page found it. Fixed with three dedicated 600×450 tile
masters at 4:3, matching the sources' own 1.00 / 1.33 / 1.32 ratios.

---

## What's Next

**Blocked on the breeder:**
1. **FLAG-1** — regenerate `inf-2` + `inf-7`, then run the one-command swap. Blocks the final push.
2. **FLAG-4** — is there a video for `.fs-video`? Yes → drop it in the asset folder. No → strip the
   CSS for this page and record a page-type exemption.
3. **§16 reviews** — real named buyer quotes, or the `TODO(breeder)` marker ships as-is.

**Remaining sprints:**
- **Sprint 5** — LLM visibility baseline across 5 engines × 6 queries. Not started.
- **Sprint 6** — sitemaps, push, live 200, IndexNow, lessons doc.

**Not pushed yet.** Push is deploy, and deploying now would put the two defective infographics live.

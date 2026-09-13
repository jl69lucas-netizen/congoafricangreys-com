## 1. Verdict

**Code side: done and live. Mobile Performance 100 is blocked by one Cloudflare setting only you can change.**

| Page | A11y | Best Practices | SEO | Agentic | CLS | Performance |
|---|---|---|---|---|---|---|
| `/african-grey-parrots-for-sale-near-me/` | 100 | 100 | 100 | 100 (was 2/3) | **0** (was 0.266) | desktop 99 local · mobile pending PSI |
| `/buy-african-grey-parrots-with-shipping/` | 100 (was 97) | 100 | 100 | 100 | 0 | desktop 99 local · mobile pending PSI |
| `/african-grey-parrots-for-sale/` (hub) | 100 (was 97) | 100 | 100 | 100 (was 67) | 0 | desktop 99 local · mobile pending PSI |

Measured with Lighthouse 13.4.1 (the version PageSpeed runs), 3 runs each, mobile and desktop, on the build and on the live near-me page after deploy.

Why Performance is not claimed yet:
- **Desktop 99** locally. The only remaining rows are compression and cache headers, which the local test server lacks and Cloudflare provides.
- **Mobile** cannot be judged on this Mac: its CPU benchmark (~490) under 4× throttle reads ~78 whatever the page does.
- **Live mobile** still carries 468 ms of blocking script from Cloudflare's Google tag gateway (section 8).
- PageSpeed's free daily quota was spent before this session, so the Google-side confirmation waits for it to reset.

## 2. What PageSpeed flagged, and what it actually was

| PageSpeed row | Real cause (verified) | Fix |
|---|---|---|
| CLS 0.266 on `.hero-copy`, "Web font" listed | The hero **photo box** was not reserved. `.hero-field{margin-left:auto}` has no width, and an auto margin on a grid item shrink-wraps it to its content. Before the photo arrived that content was only the state chips (228 px wide at 412), so the photo box grew from 114 px to 190 px on load and pushed the copy down 76 px. Delaying images reproduced **0.156** (PageSpeed: 0.153). Delaying fonts produced only 0.02. | `width:100%` on the box. Loaded layout is pixel-identical at 412 / 768 / 1350. |
| Reduce unused JavaScript 79 KiB on `/70de/` · Forced reflow · Missing source map | **`/70de/` is Google's gtag.js, injected into `<head>` by Cloudflare's Google tag gateway at the edge.** It is not in our code, and it loads before our own delayed analytics loader. It was misfiled as "Rocket Loader" in our notes for two months. | Dashboard toggle (section 8). Cloudflare's docs: a zone-level switch that overrides the page's own tag, which Configuration Rules cannot disable. |
| Web fonts in the network chain (`/cf-fonts/…`) | Cloudflare Fonts rewrote our Google Fonts link into larger files (italic 144 KB). | Fonts self-hosted: the same files Google serves (italic 67 KB), with generated fallback metrics. |
| Desktop: hero 760 w served into a 513 px slot | The srcset jumped 400 → 760 → 1280. | `-560.webp` candidate on near-me, buy-with-shipping and hub. |
| (found by our gate) Accessibility 97 on A + hub | Key-takeaway links distinguished by colour only. | Underlined (the banked hardening fix). |
| (found by our gate) Agentic Browsing 67 on hub | `<article role="listitem">` breaks the accessibility tree agents read. | Role removed. |
| (found by our gate) Best Practices 96 locally | `<meta charset>` sat after two scripts (live passed through the HTTP header). | Moved to the top of `<head>`. |

## 3. What shipped

| Commit | What |
|---|---|
| `94f29be9` | Perf gate: five categories at 100, `--live` edge-injection diff, `--psi` record, board release reads it, skill rewritten |
| `596fcce7` | Self-hosted fonts with generated Linux-portable fallbacks, charset first |
| `a5ca1770` | CLS fixes on near-me, hub, dna-tested and hand-raised; new render check; 560 w heroes; 400 w / 640 w card candidates; link underline; hub accessibility tree |

Deployed on push, live 200 on all five changed pages, IndexNow HTTP 200 for 99 URLs (the font change touches every page).

Gates run before commit:
- render meta 302 passed;
- render pages 57/57, then 15/15 on the changed pages;
- pytest 198 passed;
- final page audit PASS / PASS-WITH-WARNINGS on all five changed pages;
- Lighthouse 3-run records on the three target pages.

## 4. Old pages: the for-sale cluster sweep

Every live for-sale and buy page was loaded with images delayed, at 412 px and 1350 px. Five slugs are retired 301s.

| Page | Before | After |
|---|---|---|
| `/dna-tested-african-grey-for-sale/` | **CLS 0.449** mobile · **0.227** desktop | 0 · 0.0002 |
| `/hand-raised-african-grey-parrot-for-sale/` | **CLS 0.347** mobile | 0 |
| `/african-grey-parrots-for-sale/` | 0.035 desktop | 0 |
| `/african-grey-parrots-for-sale-near-me/` | 0.156 mobile | 0 |
| `/african-grey-parrot-adoption-cost/` | 0.018 desktop | not changed: Lighthouse scores this as a full pass |
| `/congo-african-grey-for-sale/` | 0.017 desktop (an early text re-wrap, not images) | not changed, same reason |
| eggs, timneh, health-guarantee, baby, congo pair, breeding pair, buy-with-shipping, CA, NYC, health-guarantee guide | 0 – 0.002 | nothing to fix |

The dna-tested and hand-raised pages had the same defect as near-me, and PageSpeed would have scored them far worse. They were fixed the same way, with loaded layout unchanged.

## 5. The gate, the Page Board and the skill

**`scripts/perf_audit.py`**
```
python3 scripts/perf_audit.py <slug> --runs 3            # desktop, the build
python3 scripts/perf_audit.py <slug> --mobile --runs 3   # mobile, the build
python3 scripts/perf_audit.py <slug> --live --mobile     # the live page: edge injections
python3 scripts/perf_audit.py <slug> --psi --mobile      # PageSpeed itself (after deploy)
python3 scripts/perf_audit.py <slug> --psi
```
- It judges all five categories at 100, and `EDGE-INJECTED` fails on any script Cloudflare adds that the build never shipped.
- Records are saved to `data/quality/perf/`.

**Page Board: `board_gate.py <slug> --release`** now reads those records.
- **FAIL** without fresh local records for mobile and desktop at 100.
- **WARN `perf-psi-pending`** until PageSpeed is recorded after deploy.
- **FAIL** on any PageSpeed record under 100, or on an edge-injected script.

A page cannot be released on board picks alone any more; this is the rework you wanted gone.

**Render harness:** new check `layout-image-box-reserved`. It swaps each above-the-fold image for one that never loads and compares the layout, so it catches this CLS class on every harness page in ~2 s without Lighthouse. Its broken and good fixtures behave correctly at all three widths, and all 7 of its first corpus hits were confirmed real.

**Skill:** `cag-perf-gate` was rewritten rather than duplicated, because one already existed.
- Tested before: given the report, the old skill told an agent "`/70de/` is Rocket Loader, leave it", floored Performance at 95, trusted the local build over PageSpeed, and had no Agentic Browsing.
- Tested after, on a different page under "just ship it" pressure: the agent refused to call it done on local numbers, delayed resource classes before believing the font label, named the tag gateway as your dashboard action, and gave the exact srcset fix.

## 6. Learning loop

- **Family:** `GATE` and `LAYOUT`.
  - The perf gate existed and stayed quiet: it could not see edge injections, its floor was 95, it lacked Agentic Browsing, and it trusted a CLS the local machine cannot reproduce. That is **a harness defect**, fixed with tests (11 gate + 9 board + 6 font).
  - "No above-the-fold box may resize when images load" was not covered by any check. It is **a new invariant**, promoted the prescribed way: failing fixture, then check, then fix. It stays advisory for one clean corpus run before blocking.
- **No new CLAUDE.md rule.**
- **Corrections:** the "Rocket Loader" memory was corrected, and so was this plan's first root cause (fonts), which the measurements disproved.

Traps worth keeping:
- The render harness exits 0 having measured nothing when port 4321 is taken.
- A comment edit in `src/` makes the build stale mid-run.
- A shell loop that did not split its arguments produced 404 pages that "measured" CLS 0.
- The skill registrar in copy mode rolled two skills back to stale sources; that was fixed in another session (`af3b4b75`).

## 7. The slash-command picker

- **What you saw matches reports found by the Claude Code docs agent** (not opened by me): GitHub issues on the desktop app's `/` picker only opening for the first command of a session.
- **Nothing in this project breaks it.** All 72 project skill files have valid frontmatter and there are no duplicate names.
- **Workaround until it's fixed:** type the full name (e.g. `/cag-perf-gate`) or start a fresh session.
- **Separate real defect found:** a skill invoked *with arguments* has `$1`-style tokens replaced. The for-sale builder's "`$1,500` floor price" rendered as "`invoke,500`" this session. The new perf skill avoids dollar-digit text. Other skills that quote prices this way may garble the same way when called with arguments (only the for-sale builder was observed).

## 8. Open: your action, then the PageSpeed check

1. **Turn off Cloudflare's Google tag gateway** (only you can; it is an account setting):
   - Cloudflare dashboard → **Tag Management → Google Tag Gateway**;
   - turn it off for congoafricangreys.com;
   - **Caching → Configuration → Purge Everything**.

   Google Analytics keeps working through the site's own delayed loader. This removes `/70de/`: the 79 KiB of unused JavaScript, the forced reflow, the missing source map and ~470 ms of mobile blocking time.
2. **Confirm on PageSpeed** once PageSpeed's free quota resets:
   - `python3 scripts/perf_audit.py <slug> --psi --mobile` and `--psi` for the three pages;
   - or run pagespeed.web.dev by hand.

   Those records close the board's `perf-psi-pending` warnings. If mobile Performance still reads under 100 after the toggle, the failing rows in that record are the next fix list.

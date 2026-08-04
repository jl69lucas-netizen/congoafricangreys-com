# The Build Prompt — For-Sale Page, Sprint 2 Kickoff

> **What this is.** The short prompt you paste to start Sprint 2 **after** the infographics are in the
> folder. Sprints 0 / 0.5 / 1 are already signed off; this prompt does not re-open them. Change only
> the **§ FILL** block. Everything under the line is standing law and stays byte-identical every time.
>
> **When to send it.** Only when all infographics are dropped. If any are still generating, send
> nothing — the Asset Gate is a hard stop and I will refuse to write HTML before it clears.

---

## § FILL — the only part you edit

```
PAGE      : /african-grey-breeding-pair-for-sale/
BLUEPRINT : sessions/2026-08-03-breeding-pair-sprint1-blueprint.md
STRATEGY  : sessions/2026-08-03-breeding-pair-sprint05-strategy.md
RESEARCH  : sessions/2026-08-03-breeding-pair-sprint0-research.md
ASSETS    : assets/1WORKING-ON/FOR-SALE-PAGES/BREEDING PAIR/
H1        : variant A          (or B / C / D / E)
META      : Set 1              (or 2 / 3)
```

---

## ↓ Standing law — paste verbatim, never edit ↓

**Skills, in this order, all three, not one of three:**
`/cag-for-sale-page-builder` builds it · `/impeccable` and `/frontend-design` run the Sprint 3 harden
pass on what was built. Build first, polish second — never polish a page that is not finished.

**Before you write one line of HTML:**

1. **Re-read all four docs above.** Do not build from memory of them.
2. **Open every image in the asset folder** — actually open them, do not read the filenames. Report
   spelling, duplicated words, wrong marker positions, and watermarks. **Any defect = STOP and tell
   me which file and what is wrong.** A misspelled infographic that ships is worse than a late page.
3. **Restate the brief back to me**: goal · scope · gates · what "done" means · what is out of scope.
4. **Confirm the Asset Gate** — every planned figure has a clean file, or name the ones that do not.

**Then build, in this order, and do not reorder:**

**Sprint 2 — Build.** Bake OG images first (uniform `.sec-img.inf-img` box, `max-width:760px`,
`aspect-ratio:1408/768`, under 95 KB, `-760.webp` sibling, measured `sizes`). Then write the page
**section by section from the approved outline** — never from a sibling page, never by copying and
rewording. Reuse components and CSS freely; write every paragraph fresh. Run the dup gate on your own
draft, body **and** `--headers`, **before** you call it done.

**Sprint 3 — Harden.** Own sprint, not folded into build. Hardening scan → verify each finding on the
**built** page → `/impeccable` + `/frontend-design` for hierarchy, spacing, alignment, motion, cognitive
load, error and empty states. Verified at **375 / 768 / 1280** in a real browser.

**Sprint 4 — Gates.** Meta gate **first** (it checks the checkers). Then render pages, quality report,
final page audit, seam parity, dup audit, AEO. **Run every gate twice** — one clean run proves nothing.
Read each gate's own examined count before believing a PASS; a PASS over zero items is not a PASS.
Confirm any reported defect on the built page before editing anything.

**Sprint 5 — Visibility.** LLM visibility measurement across the five engines, gaps routed.

**Sprint 6 — Close.** Build → verify in `dist/` → sitemaps → **commit and push on `main`** → confirm
live 200 → IndexNow → lessons doc → memory.

**The nine things that get this page rejected:**

1. HTML written before the Asset Gate cleared.
2. Prose lifted or reworded from a sibling page.
3. A header not followed by a conversational opening paragraph.
4. A gate believed without reading its examined count, or run only once.
5. A page "verified" by grepping source instead of reading `dist/`.
6. Work left on a branch, or committed without a push. Push **is** deploy.
7. A fabricated number, review, credential, or claim outside the Verified-Claim Ledger.
8. CITES written as Appendix II, a "3-day" guarantee, or a flat Congo price. Appendix **I**,
   **72-hour**, **$1,500–$3,500**.
9. Any bird-card label opaque enough to cover a head, face, beak, or eyes.

**Card labels — near-transparent, always.** Chip fill no more than **28% alpha** over the photo,
`backdrop-filter: blur(8px)`, anchored **bottom-left**, never top-right and never over the upper 55%
of the frame where the head sits. Legibility comes from a bottom scrim plus text-shadow, **not** from
an opaque chip. A label that covers a beak is a defect, not a style choice.

**Every component gets designed, shaped, critiqued, audited, polished, clarified, distilled, hardened,
optimized, adapted.** Crisp, modern, clean, rounded. Equal heights and equal widths across a row. No
oversized headers — H2 clamps down on mobile. Nothing cut off at any screen edge, no horizontal
scroll at any width, tap targets ≥ 24px, tables stack one card per row below 640px. Smooth, fluid
scrolling — but `scroll-behavior: auto`, because `smooth` cancels `#anchor` jump links.

**Confidence gate, 97%.** Below it, do not stop and wait: write the finished work to disk, log the
open question under `## Open Flags`, ask me exactly **one** narrow question, and keep building
everything that is not blocked.

**Show me the visual companion before you apply any redesign.** A redesign is the visual layer only —
it never adds or removes content.

**Do not rush. Do not skip a sprint. Do not mark done what you have not verified.**

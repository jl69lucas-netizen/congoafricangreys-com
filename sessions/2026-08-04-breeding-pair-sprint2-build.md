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

## What's Next

*(filled at session close)*

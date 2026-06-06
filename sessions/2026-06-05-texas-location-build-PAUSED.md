# Texas Location Page — BUILD PAUSED at Section 10 (Confidence Gate)

**Date:** 2026-06-05
**Page:** `src/pages/african-grey-parrot-for-sale-texas/index.astro` (slug `african-grey-parrot-for-sale-texas`)
**Status:** Sections 1–9 drafted (in-context, NOT yet written to site file). Paused before Section 10.
**Why paused:** Confidence Gate (≥97%) — two inputs for Section 10 "Shipping to Texas" are unresolved and could NOT be resolved from data files.

---

## What is BLOCKED (the two open questions)

### Q1 — Which Texas cities to feature in the shipping section?
- Confidence ~70%. Likely Houston / Dallas / Austin / San Antonio, but unconfirmed which the breeder wants featured (Fort Worth? El Paso? Midland — the breeder's home base?).
- `data/locations.json` carries only state/slug/status — **NO per-state featured-city list**. Cannot resolve from data.

### Q2 — Does Texas carry a delivery surcharge, or is it the flat nationwide rate?
- Confidence ~85% that it's the standard flat rate, but unconfirmed.
- `data/financial-entities.json` has canonical site-wide figures (verified this session):
  - `airport_pickup`: **$185** — "Receive your grey at your nearest major airport via IATA-compliant live-animal cargo."
  - `home_delivery`: **$350** — "Door-to-door delivery to your provided home address."
  - `shipping_iata.flat`: 185, display "$185 nationwide"
- These are described as **nationwide / flat / door-to-door**, with **NO per-state surcharge keys anywhere** in the data.
- Open question stands because: Texas is the breeder's HOME state (Midland, TX) — in-state delivery could be cheaper/free, OR a long-haul TX leg (e.g. Midland→El Paso ~300mi) could carry a surcharge. Data is silent on the state-specific case.

---

## DATA DISCREPANCY found this session (flag for fix)
- `CLAUDE.md` Non-Negotiable Rules say shipping figures live under `delivery_options` in `financial-entities.json`.
- There is **no `delivery_options` key**. The figures are under `shipping`/`airport_pickup`/`home_delivery` instead. Either CLAUDE.md or the JSON key name is stale. Does not block the build, but should be reconciled.

---

## RESUME INSTRUCTIONS (next session — do NOT re-run sections 1–9 research)
1. Get answers to Q1 + Q2 from the breeder.
2. Re-establish the sections 1–9 draft. **If this session ended, that in-context draft is GONE** — it was never written to the site file. See "Recovery" below.
3. Build Section 10 with the confirmed city list + confirmed pricing (use canonical $185/$350 unless told otherwise).
4. Continue sections 11–22.
5. Follow the location-page template (Florida = 22-section reference) per `@cag-location-builder`.

## Recovery note on sections 1–9
- They live ONLY in the paused agent's context. They were intentionally NOT written to `src/pages/...` because the page is incomplete and the Confidence Gate fired before Section 10.
- **Risk: if the session is torn down before the human answers, sections 1–9 are lost and must be rebuilt.** This file preserves the *plan and open questions* but not the drafted prose.
- Mitigation option for next run: write completed sections to the site file incrementally as they clear their own confidence gate, rather than holding the whole page in context.

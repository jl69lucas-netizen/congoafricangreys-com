# RED Baseline — Individual Bird Listing Page (Bery)

**Date:** 2026-06-18
**Plan:** docs/superpowers/plans/2026-06-18-individual-bird-listing-pages.md (Task 1)
**Method:** Dispatched a `general-purpose` subagent with ONLY the bare prompt — no skill, no plan context.

## Prompt given (unguided)
> Build an individual "for sale" web page for one of our African Grey parrots named Bery (female Congo African Grey, $1,700, currently available). Output the full page copy you would publish, plus any structured data / schema you would include.

## RED Baseline result — **TEST MOSTLY PASSED (honest surprise)**

The unguided agent produced near-compliant output. The gross failures the plan anticipated **did not occur**, because `CLAUDE.md` non-negotiable rules are auto-injected into every agent's context in this repo, and the agent read the data files + `credentials.md`.

**Already correct without any skill:**
- ✅ First-person breeder voice ("we hand-raised", "here at C.A.Gs")
- ✅ Canonical shipping line `Ships nationwide · $185 airport · $350 home` (twice)
- ✅ CITES Appendix I captive-bred-USA framing, never wild-caught
- ✅ No visible date (freshness in schema only)
- ✅ `Product` + single `Offer` schema (NOT AggregateOffer) — the distinction the plan worried about
- ✅ Trust signals (DNA cert, avian-vet cert, CITES docs, hatch cert/band)
- ✅ $200 deposit + price $1,700 traced to data files; no fabricated reviews/rating
- ✅ No geography stuffing (correctly kept it bird-focused)
- ✅ ~900 visible words — already inside the 700–1,000 band

## Gap Annotation — genuine residual gaps a skill STILL closes

These are the only real failures, and they are **standardization/lifecycle**, not failure-prevention:

1. **No sell-and-retire lifecycle.** Agent never addressed what happens to the page when Bery sells (retire vs 301). Each of 9 pages needs a consistent answer; an unguided agent omits it.
2. **No standardized section order.** The agent invented its own order. Across 9 birds + future clutches, unguided agents will each invent a different structure → inconsistent cluster. A skill locks the order.
3. **Re-taught species facts inline** (40–60 yr commitment, "most intelligent parrot", visual-sexing unreliable) instead of linking out to the evergreen species/health pages. Across 9 ephemeral pages this is duplicate/thin-content risk. Skill rule: link out, don't re-teach.
4. **Single-Offer vs AggregateOffer was luck, not guarantee.** Agent chose correctly by judgment; without a rule the next agent may emit AggregateOffer (which belongs to the variant page) and create schema conflict.
5. **Invented an image path** (`bery-female-congo-african-grey.webp`) with no real asset behind it. Skill must require a real photo or a defined placeholder.
6. **PBFD / Avian Polyomavirus "negative" claim** — agent asserted screening results. Must be checked against the Verified-Claim Ledger before this is allowed standing copy. (Flagged, not yet verified.)

## Honest conclusion
The skill's value is **narrower than the plan assumed**: it standardizes section order + schema-type + link-out discipline + the sold lifecycle across many pages. It is NOT preventing gross brand/compliance failures — `CLAUDE.md` already does that. This is a legitimate reason to keep the skill **short** (a profile/checklist), and arguably to lean more on a **template page** than a heavyweight skill.

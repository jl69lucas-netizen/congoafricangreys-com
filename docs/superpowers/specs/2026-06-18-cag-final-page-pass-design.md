# Design — `cag-final-page-pass`: the C.A.Gs final "give-it-a-pass" gate

**Date:** 2026-06-18
**Status:** Approved (design); ready for implementation plan
**Owner skill (new):** `skills/cag-final-page-pass.md`
**Companion script (upgraded):** `scripts/final_page_audit.py` (evolved from `scripts/interior_29_audit.py`)

---

## 1. Problem

The 6 newly-built C.A.Gs bird listing pages — `/available/roys/`, `/available/amie/`,
`/available/bery/`, `/available/elad/`, `/available/evie/`, `/available/jins-jeni/` — have
**no final QA gate built to pass/fail them.** Today:

- **`manual-auditor-check`** is the mechanical 29-check `dist/` gate, but it **explicitly
  excludes** "for-sale" money pages, and its script `interior_29_audit.py` carries a
  **hard-coded flat list of 18 interior slugs** — it cannot even resolve a nested
  `dist/available/<slug>/index.html` path.
- **`cags-comprehensive-page-audit-system`** covers every page type but is a **strategic,
  narrative 17-section audit** ("why isn't this page ranking"), not a binary deploy gate.
- The breeder's **"FINAL MANUAL PAGE CHECKs"** document is a *third* artifact — a merged
  ~29-point human-judgment "give it a pass" checklist (which itself collapses to ~18
  distinct checks) that is broader than either skill and currently lives nowhere in the repo.

Result: the bird pages fall in a gap. This spec closes it with **one orchestrator gate** the
breeder runs at the end of **every** page build, rebuild, or polish — covering **all** page
types, including the ones the interior gate excludes.

This skill must obey every CLAUDE.md non-negotiable: CAGs first-person voice in all proposed
copy, Verified-Claim Ledger bounds (no invented credentials/PBFD/board-cert), CITES Appendix I
+ captive-bred-USA framing, no visible dates on the *site page* (schema `dateModified` only),
`src/pages/` is authoritative, work on `main`, Recommend+Why on every option surfaced.

## 2. Goals / Non-Goals

**Goals**
- A single entrypoint — `cag-final-page-pass` — that ends in **ONE verdict**: `PASS` /
  `PASS-WITH-WARNINGS` / `FAIL`, plus a prioritized fix list ordered by business impact.
- **Page-type-aware**: works for bird/`available`, for-sale/variant, interior, location,
  comparison, blog, hub, homepage — each with its own check subset + scaled thresholds.
- **Two-tier batch**: fast mechanical pass over ALL target pages → scorecard table → full
  strategic deep-dive only for failing/low-scoring pages (+ always one sample page).
- **Reuse, don't duplicate** the existing two skills + their specialists.
- Validate by running it on the 6 live bird pages (RED→GREEN proof).

**Non-Goals**
- Not a pre-build planner (that's `cag-content-audit-agent`).
- Not a replacement for `cags-comprehensive-page-audit-system` (strategic audit) or
  `manual-auditor-check` (interior mechanical gate) — both survive as **components** this gate
  calls. This gate is the **superset entrypoint**.
- Does not auto-edit site files. It RECOMMENDS; edits happen only on explicit instruction
  (Confidence Gate ≥97%).
- Does not build the 3 declared-but-unbuilt birds (`joys`, `loti`, `carl`) — **out of scope**.

## 3. Architecture — three tiers

### Tier 1 — Mechanical (`scripts/final_page_audit.py`)
Evolves `interior_29_audit.py` with two capabilities it lacks:

1. **Nested-slug support** — accept slugs like `available/roys` and resolve
   `dist/available/roys/index.html`. (Today it only does flat `dist/<slug>/index.html`.)
2. **Page-type profiles** — a `PROFILES` map keyed by page type. Each profile declares, per
   check, one of `FAIL` (hard gate) / `WARN` (soft) / `NA` (not applicable to this type), plus
   scaled numeric thresholds (word count, heading bands).

Outputs per-page blocks + a `CHECK ROLL-UP`, exactly like the current script, but each `✗`
now carries its profile-resolved severity so the roll-up is **pre-triaged**, not raw.

Keeps all **4 baked-in false-positive traps** (nested/list `@type`, header-logo-not-hero,
authority-hotline phone, strip-inline-JSON-LD-before-word-count) and **adds bird-page traps**
(see §4).

### Tier 2 — Strategic (routed, low/failing pages only)
For any page that FAILs or scores below the deep-dive threshold, route to the **5 owned scorers
already in `cags-comprehensive-page-audit-system`** — AEO /10, Entity-coverage /10, Visual-need
table, Backlink-magnet /10, Verdict tier — plus the relevant CAG specialists
(`cag-keyword-verifier`, `cag-entity-incorporation-agent`, `internal-link-agent`,
`cag-conversion-tracker`). No re-implementation; this gate assembles their outputs.

### Tier 3 — Subjective (sampled)
The breeder's merged manual checklist as a copy-paste block: CAGs first-person voice, ≤1
Honesty-Policy humor beat/section, Flesch 60–70 (floor ~55 for entity-dense copy), ≥1
high-resolution breeder detail / ~500 words, warm/empathetic tone, brand-protocol naming.
Sampled across 1 transactional + 1 pillar + 1 trust page (or, for a bird batch, the lowest
mechanical scorer + 1 random).

## 4. Page-type profiles (the core upgrade)

Each profile = `{checks: {check_id: FAIL|WARN|NA}, thresholds: {...}}`. The **bird/`available`**
profile is net-new and is the one this spec must get right:

| Bird-page HARD GATE (FAIL) | Rationale (source) |
|---|---|
| `AggregateOffer` present | Bird page must be a **single `Product`+`Offer`**; AggregateOffer is the variant page (`cag-bird-listing-page`). |
| PBFD / Polyomavirus claim in copy or schema | **Not in the Verified-Claim Ledger** for bird pages (`cag-bird-listing-page`). |
| Sold bird still `availability: InStock` | Sell-and-retire lifecycle: sold → 301, never InStock. |
| Hero is placeholder / not a real photo | Real-image requirement. |
| Missing shipping line (`Ships nationwide · $185 airport · $350 home`) | Shipping-on-every-card non-negotiable. |
| Relative canonical · `<svg>` in CSS `content:` · escaped `&lt;svg` · 🦜 · breeder phone in body · visible date | Site-wide hard gates (apply to all types). |

| Bird-page SCALED / SCOPED | Value |
|---|---|
| Word count | **700–1,000** (not pillar "+1,000") |
| Newsletter placements | **EXEMPT** — footer newsletter only (decided 2026-06-18) |
| Heading band | H1×1 + H2/H3 required; H4 where structure exists; H5/H6 only on genuine depth |
| House-method naming (check #11) | **WARN** — flag, never FAIL, until breeder confirms a term (Verified-Claim Ledger forbids inventing one) |
| Lifespan 40–60 yr | ≥1 reference still required |
| CITES Appendix I + captive-bred + USDA/AWA | required in first 300 visible words (strip JSON-LD) |

Other profiles (`interior` = today's 18-page behavior unchanged; `for-sale/variant`,
`location`, `comparison`, `blog`, `hub`, `homepage`) are declared with their
type-appropriate check subsets; full per-type tables live in the skill body. The default for an
unmapped type is the **strictest** sensible subset with everything type-specific marked `WARN`
(fail-safe, never silently pass).

## 5. Verdict model

- **FAIL** — any REAL hard-gate check fails (per the active profile). Ship-blocking.
- **PASS-WITH-WARNINGS** — no hard fails, but ≥1 soft item (Flesch 55–60, house-method WARN,
  alt marginally >190, a missing-but-recommended entity). Shippable; fixes logged.
- **PASS** — clean.

Every `✗` is triaged **REAL** (fix now) / **ACCEPTED** (correct for page type) / **FALSE
POSITIVE** (auditor heuristic flaw) / **NET-NEW / BY-DESIGN**. The gate never reports a raw
machine fail as a defect without triage — the discipline that prevented 31 false positives on
the interior batch.

## 6. Keyword / voice posture (applies to skill prose + recommendations)

Per the breeder's instruction, the gate's **own checklist language and any proposed copy** use
**CAGs first-person voice** ("here at C.A.Gs, our…") and are **LSI/NLP-keyword-rich** — the
check items reference real semantic variants (e.g. "captive-bred Congo African Grey parrot",
"hand-raised / hand-fed weaned chick", "CITES Appendix I documentation", "DNA-sexed", "talking
African Grey", "Timneh vs Congo", airport/IATA shipping entities) so the gate doubles as a
keyword-coverage reminder, not just a structural checker. The gate **checks for** intent-based
keyword fan-out, concurrent/LSI/NLP variants, and entity coverage; it does not fabricate them.

## 7. Open questions surfaced as GAP-FLAGs (gate outputs, not blockers)

The gate emits these as recommendations for the breeder — it never invents an answer:
- **House-method name** — needs a breeder-confirmed term to upgrade check #11 from WARN→enforced.
- **Extra authority-link targets** — beyond WPT/IUCN/CITES/APHIS/AAV/Cornell, the gate may
  suggest additional credible `.org/.edu/.gov` targets for link variety (added to
  `external-link-library.md` first, verified 200).
- **Airport codes / Flight-Nanny / local avian-vet authority** — the gate flags *whether a
  given page type warrants* logistics entities (airport codes, IATA) or local-authority
  signals; bird listing pages generally inherit these from the price/shipping cluster rather
  than carrying them inline.

## 8. Deliverables

1. `skills/cag-final-page-pass.md` — the orchestrator skill (overview, when-to-use vs the two
   existing skills, the two-tier flow, page-type profile tables, verdict model, the copy-paste
   FINAL MANUAL PAGE CHECK block, common mistakes, workflow placement).
2. `scripts/final_page_audit.py` — upgraded auditor (nested slugs + page-type profiles +
   bird-page traps). It **supersedes** `interior_29_audit.py` by reproducing the exact 18-page
   interior behavior via the `interior` profile (back-compat: same checks, same results on those
   slugs); the old script is kept as a one-line shim or deleted once parity is verified.
3. **CLAUDE.md** registration (Quick-Start "give a page a pass" entry + Skills list) and a
   **MEMORY.md** pointer.
4. **Validation:** run the gate on the 6 live bird pages → `sessions/2026-06-18-final-pass-
   available-cluster.md` (RED→GREEN: capture pre-fix findings, apply REAL fixes, re-run green).

## 9. Validation / acceptance

- `npx astro build` clean; `python3 scripts/final_page_audit.py` resolves all 6
  `available/<slug>` pages (no `_MISSING`).
- Each of the 6 bird pages reaches **PASS** or **PASS-WITH-WARNINGS** with every REAL `✗` fixed
  and every remaining `✗` triaged ACCEPTED/FALSE-POSITIVE/NET-NEW.
- Bird-page hard gates demonstrably fire (e.g. a deliberately-mutated AggregateOffer FAILs in a
  dry run) — proving the new traps aren't dead code.
- Skill correctly *routes away* from itself for the 3 unbuilt birds (reports them out-of-scope,
  not as failures).
- All work committed + pushed to `main` (push = deploy).

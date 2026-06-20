---
name: cag-final-page-pass
description: Use as THE final QA gate at the end of EVERY C.A.Gs page build/rebuild/polish, before you "give the page a pass" or deploy — any page type, including bird /available/ and for-sale pages the interior gate excludes. Runs the mechanical page-type-aware auditor over dist/, routes low scorers to the strategic + subjective checks, and returns one PASS / PASS-WITH-WARNINGS / FAIL verdict with a prioritized, WHY-grounded fix list. Triggers: "final check", "give this page a pass", "is this page done", "audit before deploy", "run the final manual checks".
tools: [Read, Write, Bash]
---

# C.A.Gs Final Page Pass — the give-it-a-pass gate

## Overview
The single entrypoint you run at the end of every page build. Page-type-aware, two-tier,
ends in ONE verdict. Supersedes the interior-only `manual-auditor-check` by covering EVERY
page type via profiles; reuses `cags-comprehensive-page-audit-system` (strategic) and the
subjective checklist as components — it does not re-implement them.

## When to Use / Not
USE — a page (or batch) is "done" and you're about to pass/deploy it; ANY type incl. bird
`/available/`, for-sale, location, comparison, blog. NOT — pre-build planning
(`cag-content-audit-agent`) or deep "why isn't this ranking" strategy
(`cags-comprehensive-page-audit-system`, which this gate calls for low scorers).

## Two-tier flow
1. Mechanical: `npx astro build` then `python3 scripts/final_page_audit.py [--birds]`.
   Per-page PASS/WARN/FAIL + pre-triaged roll-up. Edit `BIRDS`/`SLUGS` or add a profile to
   retarget.
2. Strategic (low/failing only): route to the 5 owned scorers in `cags-comprehensive-page-
   audit-system` (AEO/entity/visual/backlink/verdict) + specialists; assemble, don't duplicate.
3. Subjective (sample 1 transactional + 1 pillar + 1 trust, or lowest bird scorer + 1):
   the copy-paste block below.

## Page-type profiles

### Bird / `/available/` profile (net-new; the core upgrade)

All bird checks run against `scripts/final_page_audit.py --birds`. The `BIRDS` list in the
script currently covers: `available/bery`, `available/amie`, `available/roys`,
`available/jins-jeni`, `available/elad`, `available/evie`. Add new `/available/<slug>/`
entries to `BIRDS` when a new bird page is built.

#### Bird-page HARD GATES (FAIL — ship-blockers)

| Check ID | What fails | Rationale |
|---|---|---|
| `no_aggregateoffer` | `AggregateOffer` present anywhere in schema | Bird page must be a **single `Product`+`Offer`**; `AggregateOffer` is the variant page (`cag-bird-listing-page`). |
| `no_pbfd_claim` | **NA (no longer a gate).** PBFD + Avian Polyomavirus PCR screening is in the Verified-Claim Ledger — per-bird testing + records confirmed by breeder 2026-06-20. Asserting "screened for / negative for PBFD" is now permitted on bird pages. (Was FAIL through 2026-06-19.) |
| `shipping_line` | Missing `$185` and `$350` shipping figures from visible body | Shipping-on-every-card non-negotiable (CLAUDE.md). Canonical line: `Ships nationwide · $185 airport · $350 home`. |
| `sold_not_instock` | Sold/reserved STATUS signal present AND schema still shows `InStock` | Sell-and-retire lifecycle: sold → 301, never `InStock`. Note: commerce phrases like "sold together" do NOT trigger; only explicit status signals ("now sold", "has been sold", "status: sold", "is reserved", etc.). |
| `canonical_abs` | Relative canonical (not `https://…`) | Site-wide hard gate — applies to all page types. |
| `no_svg_in_content` | `<svg>` inside CSS `content:` | Site-wide trap; see false-positive traps below. |
| `no_escaped_svg` | Escaped `&lt;svg` in rendered HTML | Site-wide trap. |
| `no_emoji_parrot` | 🦜 in rendered output | Site-wide non-negotiable — 🦜 is a generic green parrot, not an African Grey. |
| `no_phone_in_body` | Breeder phone number in page body (above footer) | Rule 61; authority hotlines (USDA APHIS, FTC) are exempt. |
| `no_visible_date` | Visible "Updated / Last updated / Last modified <Month> <Year>" text | CLAUDE.md: freshness lives only in schema `dateModified`, never as visible text. |

#### Bird-page SCALED / SCOPED (WARN — shippable, log fix)

| Check ID | Value / Behavior |
|---|---|
| `wordcount_in_band` | **700–1,000 words** (script checks 600–1,200 with buffer for chrome); not the pillar "+1,000" floor |
| `newsletter_present` | **NA** — bird pages are exempt from newsletter requirement (footer newsletter only, per 2026-06-18 decision) |
| `all_h1_h4` | WARN — H1×1 + H2/H3 required; H4 where structure exists on a lean bird page; H5/H6 only on genuine depth |
| `house_method` | **WARN** — flag until breeder confirms a term; Verified-Claim Ledger forbids inventing a house-method name |
| `lifespan_40_60` | WARN — ≥1 "40–60 year" lifespan reference still required (not hard-FAIL on lean bird pages) |
| `real_hero_image` | WARN — hero must not be a placeholder/logo; flags if first content image src contains "placeholder", "coming-soon", or "default" |

### Interior profile (back-compat with 18-page batch)

Same 18 slugs and behavior as `scripts/interior_29_audit.py`. Key differences from bird:
`no_aggregateoffer`, `no_pbfd_claim`, `shipping_line`, `wordcount_in_band`, and
`real_hero_image` are all `NA` (not applicable). `house_method` = WARN. `airport_codes`
(WARN) applies only to the transactional `african-grey-parrot-price` slug.

### Other page types — compact one-row summary

| Page type | Key hard gates | Key scaled / scoped | Notes |
|---|---|---|---|
| **Interior** (18-page batch) | canonical_abs, no_phone_in_body, no_visible_date, jsonld_valid, faqpage_ok | house_method WARN; airport_codes WARN on price page only | Legacy behavior preserved; `interior_29_audit.py` shim or identical via `final_page_audit.py` default |
| **For-sale / variant** (`/congo-african-grey-for-sale/`, `/timneh-african-grey-for-sale/`) | AggregateOffer required (opposite of bird); canonical_abs; shipping line $185/$350 | word count 1,000–2,000; all H1–H4 present | `AggregateOffer` is CORRECT here — it's the variant page pattern |
| **Location** (`/african-grey-parrot-for-sale-[state]/`) | canonical_abs; no_visible_date; BreadcrumbList; shipping line | word count 3,000–5,000; state entity in H1; FAQPage present | Florida = 22-section reference template |
| **Comparison** (`/congo-vs-timneh-african-grey/` etc.) | canonical_abs; comparison table present; no_visible_date | word count 1,500–3,000; H1 contains "vs" or "versus" | `cag-comparison-builder` handles schema |
| **Blog** | canonical_abs; no_visible_date; Article schema; BreadcrumbList | word count 800–2,500; FAQPage recommended (WARN if absent) | Internal links to money pages required |
| **Hub** (`/african-grey-parrots-for-sale/` etc.) | canonical_abs; no_visible_date; spoke links present | word count 500–1,500; spoke count ≥ 3 internal links | Feeds `cag-structure-architect` silo map |
| **Homepage** (`/`) | canonical_abs; no_visible_date; Organization schema; no_phone_in_body | word count 2,000–4,000; H1 on primary keyword; ≥3 FAQPage answers | Highest-traffic page — strict threshold |

**Fail-safe rule for unmapped page types:** if a page type is not in `PROFILES`, the script
falls back to `DEFAULT_SEVERITY = "FAIL"` for every boolean check — the strictest possible
subset. Type-specific checks that cannot be meaningfully evaluated (e.g. `no_aggregateoffer`
on a blog page) are treated as WARN to avoid fabricating ship-blockers. Never silently pass
an unmapped type.

## Verdict model
- **FAIL** — any REAL hard-gate check fails (per the active profile). Ship-blocking; fix before deploy.
- **PASS-WITH-WARNINGS** — no hard fails, but ≥1 soft item (Flesch 55–60, `house_method` WARN, alt marginally >190, a missing-but-recommended entity). Shippable; fixes logged for follow-up.
- **PASS** — clean.

Every `✗` is triaged **REAL** (fix now) / **ACCEPTED** (correct for page type) / **FALSE
POSITIVE** (auditor heuristic flaw) / **NET-NEW / BY-DESIGN**. The gate never reports a raw
machine fail as a defect without triage — the discipline that prevented 31 false positives on
the interior batch.

## The 5 false-positive traps (do NOT fabricate these as defects)

| Looks like a fail | Why it's usually fine |
|---|---|
| **`has_org` missing** | `Organization` is valid when nested as `Article.publisher`/`author`, and `@type` can be a **list** `["LocalBusiness","PetStore"]`. The auditor recurses and handles lists before flagging — verify in `dist/` before reporting. |
| **Non-hero image is `eager`** | Index 0 is the **header logo**; the eager image right after it is the correct **LCP hero**. The auditor detects the hero by excluding `logo` srcs, not by position 0. A false "non-hero eager" alert usually means the logo exclusion failed — check `src` attributes in `dist/`. |
| **Phone number in body** | Third-party **authority hotlines** (USDA APHIS `(844) 820-2234`, FTC, IC3) are intentional. Rule 61 bans only the **breeder's** number in body. The auditor exempts any phone within 60 chars of "APHIS", "USDA", "FTC", "IC3", "hotline", or "fraud". |
| **CITES/USDA not in first 300 words** | Astro renders inline JSON-LD *inside* `<main>` — **scripts are stripped before measuring** visible word count. If the auditor still flags this, confirm via `grep` that the JSON-LD stripping ran correctly on `dist/`. |
| **`Offer` nested inside `Product` fails `no_aggregateoffer`** | A single `Offer` nested inside a `Product` block is **correct schema for a bird listing page** — that is the single-Product+Offer pattern the spec requires. Only a **top-level `AggregateOffer`** (not nested inside `Product`) fails the bird gate. Verify by inspecting the raw JSON-LD in `dist/available/<slug>/index.html` before reporting. |

## Copy-Paste FINAL MANUAL PAGE CHECK

> Paste this block anywhere (a fresh chat, a PR comment, a doc) to run the gate by hand.
> Tick every box; a page isn't "done" until the REAL items pass.

```text
FINAL MANUAL PAGE CHECK — <page slug>            Updated: <Month Year>
RUN FIRST: npx astro build  →  python3 scripts/final_page_audit.py [--birds]

STRUCTURE
[ ] H1 ×1 exactly; H1–H4 all present; no level skips (utility pages may lack H4 — ACCEPTED)
[ ] Exactly ONE FAQPage in dist/; JSON-LD parses valid
[ ] BreadcrumbList present; Organization present (top-level OR nested as Article.publisher)
[ ] Canonical is absolute (https://…)

META + IMAGES
[ ] Title ≤275 · description ≤300 (long-format standard); brand ("C.A.Gs" or "Congo African Grey") in title
[ ] Every image alt ≤190 chars AND unique per page
[ ] Non-hero images loading="lazy"; LCP hero stays eager (header logo is NOT the hero)
[ ] Every <img> has explicit width/height (CLS); delivered <100KB

COMPLIANCE COPY (content pages; contact/privacy exempt)
[ ] CITES Appendix I + captive-bred + USDA/AWA in the first 300 VISIBLE words (strip JSON-LD)
[ ] 40–60 year lifespan referenced at least once

CONVERSION + FRESHNESS
[ ] Footer phone present; NO breeder phone in body (authority hotlines OK)
[ ] NO visible date anywhere (no "Updated <Month Year>" / "Last updated"); freshness lives ONLY in schema dateModified
[ ] Newsletter top/middle/bottom — long content pillars only (skip thin/utility pages)

A11Y / GOTCHA TRAPS
[ ] No <svg> inside CSS content:  · no escaped &lt;svg in dist  · no 🦜  · no user-select:none
[ ] External links: new tab + rel="noopener noreferrer" + ↗; no bare "click here" anchors

SUBJECTIVE (read 3 sample pages: 1 transactional, 1 pillar, 1 trust)
[ ] First-person "we/our/here at C.A.Gs" voice >> third-person filler
[ ] ≤1 Honesty-Policy humor beat/section; none on legal/health
[ ] Flesch 60–70 (floor ~55 for entity-dense pages)
[ ] ≥1 high-resolution breeder detail / ~500 words; no "both make exceptional companions" filler
[ ] Named house method ("the C.A.Gs Grey Method") used where hand-rearing is discussed
[ ] LSI/NLP keyword coverage: "captive-bred Congo/Timneh African Grey", "hand-raised/hand-fed",
    "DNA-sexed", "CITES Appendix I", "talking grey / African Grey parrot", "IATA airport
    shipping" present where natural — not forced, not stuffed

TRIAGE every ✗ as: REAL (fix) · ACCEPTED (page-type) · FALSE POSITIVE (heuristic) · NET-NEW/BY-DESIGN

--- BIRD-PAGE SUPPLEMENT (run for every /available/<slug>/ page) ---

RUN: python3 scripts/final_page_audit.py --birds

HARD GATES (FAIL — fix before deploy)
[ ] Schema uses single Product + single Offer — NO AggregateOffer anywhere
[ ] PBFD/Polyomavirus claim is now ALLOWED (PCR screening in the Verified-Claim Ledger,
    per-bird testing confirmed by breeder 2026-06-20) — no longer a hard gate
[ ] Shipping line visible in body: $185 airport pickup · $350 home delivery
[ ] If bird is sold/reserved: schema shows OutOfStock (not InStock); page has 301 redirect plan
[ ] Canonical is absolute (https://congoafricangreys.com/available/<slug>/)

SCALED / SCOPED (WARN — shippable, log for follow-up)
[ ] Word count 700–1,000 words (check nwords in auditor output)
[ ] Real hero photo — not a placeholder, coming-soon image, or logo
[ ] H1 ×1 + H2/H3 present; H4 only where page depth warrants it
[ ] Lifespan 40–60 yr mentioned at least once
[ ] House-method naming (WARN until breeder confirms a term)

EXEMPT on bird pages
[ ] Newsletter — footer newsletter is sufficient; mid-page newsletter NOT required

FIRST-PERSON VOICE (bird page)
[ ] Written as "here at C.A.Gs, [bird name] is one of our…" — not third-person species narration
```

## GAP-FLAGs the gate emits (never invents)

These are recommendations surfaced for the breeder — the gate never auto-resolves them:

- **House-method name** (WARN on all pages until confirmed) — upgrade check from WARN to enforced only after the breeder supplies a confirmed term for inclusion in the Verified-Claim Ledger.
- **Extra authority-link targets** — beyond the standard library (WPT/IUCN/CITES/APHIS/AAV/Cornell), the gate may suggest additional credible `.org/.edu/.gov` targets for link variety. Add to `docs/reference/external-link-library.md` first and verify 200 before inserting.
- **Airport codes / Flight-Nanny / local avian-vet authority** — the gate flags *whether a given page type warrants* logistics entities (airport codes, IATA LAR, flight nanny) or local-authority signals. Bird listing pages generally inherit these from the price/shipping cluster rather than carrying them inline; the flag is informational only.

## Common mistakes

- **Auditing source greps not `dist/`** — Astro `<Schema>` components hide JSON-LD from source; always build first. `grep` on `src/` will miss schema and produce false positives.
- **Reporting the roll-up un-triaged** — the roll-up flags ALL pages; utility pages (contact/privacy) are exempt from several checks by design. Triage every `✗` before quoting it as a defect.
- **Chasing Flesch 60–70 as a hard gate** — it fights entity density; treat ~55 as the floor. Do not gut semantic coverage to chase a readability score.
- **Running it on the 3 unbuilt birds (`joys`/`loti`/`carl`)** — those are declared in `data/clutch-inventory.json` but not yet built; they are out of scope. Report them as OUT-OF-SCOPE, not as FAIL.
- **Treating a nested `Offer` as an `AggregateOffer` fail** — see false-positive trap #5 above. Inspect the raw JSON-LD in `dist/` before flagging.

## Workflow placement
Sprint 4 FINAL step, immediately before Sprint 5 deploy. After `cag-accessibility-fixer` →
`cag-performance-fixer` → `cag-canonical-fixer` → `cag-footer-standardizer`. Companion to
`MANUAL INTERIOR-PAGE CHECKLIST.md` Part N and `cag-website-health` (whole-site sweep).
Invoke via the Skill tool, or run the two commands by hand.

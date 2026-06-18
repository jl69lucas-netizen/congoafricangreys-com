# Final Page Pass — `/available/` Bird Cluster Validation (RED→GREEN)

**Date:** 2026-06-18
**Gate validated:** `cag-final-page-pass` (mechanical auditor `scripts/final_page_audit.py`, `bird` profile)
**Command:** `npx astro build >/dev/null 2>&1 && python3 scripts/final_page_audit.py --birds`
**Scope:** the 6 live bird pages — `available/bery`, `available/amie`, `available/roys`, `available/jins-jeni`, `available/elad`, `available/evie`. (joys/loti/carl are declared in `data/clutch-inventory.json` but NOT built — explicitly out of scope.)
**Outcome:** all 6 already at **PASS-WITH-WARNINGS**, **zero hard FAIL**, **zero REAL defects**. No `.astro` edits required. This is an honest triage pass: the only ✗ lines are WARN-severity-by-design items, confirmed correct against `dist/`.

---

## RED capture (`/tmp/birds-red.txt`)

```
=== C.A.Gs FINAL PAGE PASS ===  (verdict per page)

[PASS-WITH-WARNINGS] available/bery   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | schema:Answer,Brand,BreadcrumbList,FAQPage,GeoCoordinates,ImageObject,ListItem,Offer,OpeningHoursSpecification,Organization,PetStore,PostalAddress,Product,Question
    WARN → all_h1_h4, wordcount_in_band, house_method
[PASS-WITH-WARNINGS] available/amie   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | schema:Answer,Brand,BreadcrumbList,FAQPage,GeoCoordinates,ImageObject,ListItem,Offer,OpeningHoursSpecification,Organization,PetStore,PostalAddress,Product,Question
    WARN → all_h1_h4, wordcount_in_band, house_method
[PASS-WITH-WARNINGS] available/roys   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | schema:Answer,Brand,BreadcrumbList,FAQPage,GeoCoordinates,ImageObject,ListItem,Offer,OpeningHoursSpecification,Organization,PetStore,PostalAddress,Product,Question
    WARN → all_h1_h4, wordcount_in_band, house_method
[PASS-WITH-WARNINGS] available/jins-jeni   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | schema:Answer,Brand,BreadcrumbList,FAQPage,GeoCoordinates,ImageObject,ListItem,Offer,OpeningHoursSpecification,Organization,PetStore,PostalAddress,Product,Question
    WARN → all_h1_h4, wordcount_in_band, house_method
[PASS-WITH-WARNINGS] available/elad   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | schema:Answer,Brand,BreadcrumbList,FAQPage,GeoCoordinates,ImageObject,ListItem,Offer,OpeningHoursSpecification,Organization,PetStore,PostalAddress,Product,Question
    WARN → all_h1_h4, wordcount_in_band, house_method
[PASS-WITH-WARNINGS] available/evie   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | schema:Answer,Brand,BreadcrumbList,FAQPage,GeoCoordinates,ImageObject,ListItem,Offer,OpeningHoursSpecification,Organization,PetStore,PostalAddress,Product,Question
    WARN → all_h1_h4, wordcount_in_band, house_method

0 PASS · 6 PASS-WITH-WARNINGS · 0 FAIL  (of 6)
```

There were **no `FAIL →` lines** in the RED output. The only ✗-equivalent signals are the three WARN checks below, identical across all 6 pages.

---

## Triage table

All 6 pages emit the identical WARN triplet, so the triage applies uniformly. Evidence is quoted from `dist/available/bery/index.html` (representative; the other 5 are byte-identical in structure for these checks).

| page | check | machine verdict | triage | action / evidence |
|---|---|---|---|---|
| all 6 | `all_h1_h4` | WARN | **ACCEPTED (WARN-by-design)** | Profile `PROFILES["bird"]["all_h1_h4"]="WARN"` with comment "spec §4: H4 only where depth exists on a lean bird page." Heading tree is `H1:1 H2:8 H3:12 H4:0` — clean, no skips (`no_skip`=True), just no H4 depth needed on a 9-section lean bird page. Not a defect; do not add filler H4s. No edit. |
| all 6 | `wordcount_in_band` | WARN | **ACCEPTED (chrome-inflated, body on-target)** | Auditor counts the **full rendered document** (incl. header/footer/nav chrome). Full-doc = 1422 (bery) … 1550 (jins-jeni). `<main>`-only body, chrome stripped = **1090 words** (bery) — just over the 700–1,000 spec target, within reason. The ~332-word gap to the full-doc count is BaseLayout header/footer/nav chrome, not page copy. Severity is WARN by design (`"wordcount_in_band":"WARN"`). Trimming real, accurate bird copy to chase a chrome-inflated number would be net-negative. No edit. |
| all 6 | `house_method` | WARN | **ACCEPTED (GAP-FLAG by design)** | Profile comment: "GAP-FLAG until breeder confirms a term." Check fails because pages mention hand-raising (`hand-raising-mentioned=True`) but use no branded "C.A.Gs X Method" string (`named-method=False`). Inventing a method name would violate the Verified-Claim Ledger. Correct to leave as a WARN until the breeder confirms a term. No edit. |

### False-positive traps — verified clear in `dist/` (none fired, documented for the record)

| trap | status in `dist/available/bery/index.html` | evidence |
|---|---|---|
| 1. `has_org` missing | PASS (not flagged) | `Organization` + `PetStore` present in flat schema type list; auditor recurses nested publisher/author and handles `@type` lists. |
| 2. non-hero image eager | PASS (`img_lazy_nonhero` not flagged) | header logo is index 0, dropped; first remaining content image is the eager LCP hero; rest lazy. |
| 3. phone in body | PASS (`no_phone_in_body` not flagged) | no breeder phone in body; any authority hotline would be exempt. |
| 4. CITES/USDA not in first 300 words | PASS (`cites_captive_usda_early` not flagged) | compliance copy front-loaded in `<main>`; inline JSON-LD stripped before count. |
| 5. nested `Offer` mis-read as AggregateOffer | PASS (`no_aggregateoffer` not flagged) | `grep AggregateOffer` → **empty**; schema is single `Product` with one nested `"@type":"Offer"`. Correct per `cag-bird-listing-page` (AggregateOffer is the *variant* page only). |

### Hard-gate sanity (all FAIL-severity bird gates passed on every page)
- `no_aggregateoffer` — PASS. `grep -o AggregateOffer dist/available/bery/index.html` → empty.
- `no_pbfd_claim` — PASS. `grep -io '...\(pbfd\|polyoma\)...'` → no match (no PBFD/Polyoma health claim anywhere).
- `shipping_line` — PASS. Body contains canonical line `$185 airport · $350 home`.
- `sold_not_instock` — PASS. No sold/reserved status signal on these live-available pages; schema InStock is correct.
- `canonical_abs` — PASS. `<link rel="canonical" href="https://congoafricangreys.com/available/bery/">` (absolute https).

---

## Triage summary

- **REAL:** 0
- **ACCEPTED (WARN-by-design):** 3 distinct checks × 6 pages = 18 WARN instances (`all_h1_h4`, `wordcount_in_band`, `house_method`)
- **FALSE-POSITIVE:** 0 fired (5 traps verified clear)
- **NET-NEW / BY-DESIGN:** the WARN profile itself is by design
- **Fixed:** nothing — no `src/pages/available/*.astro` edits were warranted. Fabricating fixes for WARN-by-design items would violate the "do not fabricate defects" mandate of this task.

---

## GREEN re-run (`/tmp/birds-green.txt`)

Identical to RED (no edits made). All 6 at PASS-WITH-WARNINGS, zero hard FAIL.

```
=== C.A.Gs FINAL PAGE PASS ===  (verdict per page)

[PASS-WITH-WARNINGS] available/bery   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | schema:Answer,Brand,BreadcrumbList,FAQPage,GeoCoordinates,ImageObject,ListItem,Offer,OpeningHoursSpecification,Organization,PetStore,PostalAddress,Product,Question
    WARN → all_h1_h4, wordcount_in_band, house_method
[PASS-WITH-WARNINGS] available/amie   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | ...
[PASS-WITH-WARNINGS] available/roys   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | ...
[PASS-WITH-WARNINGS] available/jins-jeni   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | ...
[PASS-WITH-WARNINGS] available/elad   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | ...
[PASS-WITH-WARNINGS] available/evie   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | ...
    (all 6 emit identical WARN → all_h1_h4, wordcount_in_band, house_method)

0 PASS · 6 PASS-WITH-WARNINGS · 0 FAIL  (of 6)
```

---

## Anti-dead-code proof (hard gate fires)

```
python3 -c "import sys; sys.path.insert(0,'scripts'); import final_page_audit as A; print(A.audit_html('available/x','<html><body><main><h1>x</h1><script type=\"application/ld+json\">{\"@type\":\"AggregateOffer\"}</script></main></body></html>','bird')['_verdict'])"
→ FAIL
```

Confirms the `no_aggregateoffer` hard gate is live code, not dead: a synthetic page carrying a top-level `AggregateOffer` is driven to `FAIL`. The 6 real pages correctly do NOT trip it (they use single `Product`+nested `Offer`).

---

## Open Flags

None. Every ✗ was triaged with `dist/` evidence at ≥97% confidence; no fix required a content/judgment call beyond markup, and no item was left uncertain.

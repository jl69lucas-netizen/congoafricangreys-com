# 2026-06-11 — Interior-Pages Remediation Batch (post-audit fixes)

Scope approved by user ("Fix everything"). Executed inline (no subagents, per user instruction). Commit `6faec53`, deployed + live-verified + IndexNow 200.

## What was fixed
- **(a) H4–H6 depth** — added one H4→H5→H6 conversational question-ladder (with short first-person, Verified-Claim-Ledger-safe paragraphs) to the 12 pages that had zero deep headings: care hub, best-food (h5/h6 only — h4 existed), health-guarantee, trusted-breeders, reviews, captive-bred, cites-documentation, species guide, faq pillar, how-to-tame, adoption, price. Idiom copied from diet/lifespan pages (`font-sora font-bold uppercase` sm/13px/12px, green/clay-ink alternating).
- **(b) TOCs** — "On This Page" numbered-card TOC (health-guarantee idiom, single-list variant) added to trusted-breeders (6 sections), reviews (5), captive-bred (7).
- **(c) Scams Direction-D re-skin** — 46 hard-coded `'Lora'`/`'Sora'` font-family declarations → `'Newsreader',Georgia,serif` / `'IBM Plex Sans',system-ui,sans-serif`; 13 neutral `rgba(0,0,0,…)` shadows → warm `rgba(60,30,10,…)`. CounterSnippet + KeyTakeaway equivalents already existed on the page (`#counters` strip + `.takeaways-box`) — restyled by the same pass, content untouched.
- **(d) Meta caps** — 8 over-cap descriptions trimmed in the prior session segment + 2 found still over (african-grey-care 301→297, care-guide 303→294). All interior titles ≤205 / descriptions ≤300 verified by script.
- **(e) Breadcrumb dedupe** — removed page-level `breadcrumbSchema` const from captive-bred and the `BreadcrumbList` node from scams' `@graph`; `<Breadcrumb />` emits the schema itself (NOTE comments left in both files, same as cites/health-guarantee). dist verified: exactly 1 BreadcrumbList each. **Captive-bred seams were already present** (6 × `captive-d-seam cag-seam`, render verified) — audit item was stale.
- **(f) Conversational H2s** — 7 conversions: captive-bred ×4, care hub ×1, species guide ×1 (counts include the FAQ-section retitle on captive-bred).

## Known leftovers (out of approved scope)
- 3 for-sale pages also carry duplicate BreadcrumbLists (adoption-cost, dna-tested, hand-raised) — same component+const pattern. Not in the audited interior batch; fix with the for-sale cluster.

## Verification
- `npx astro build` → 101 pages OK; dist checks: 1 BreadcrumbList/page, 0 legacy fonts on scams, 0 `&lt;svg`, TOCs + ladders render.
- Live: all 16 changed slugs 200; captive-bred TOC + scams Newsreader confirmed on production.
- IndexNow: 16 URLs submitted → HTTP 200.

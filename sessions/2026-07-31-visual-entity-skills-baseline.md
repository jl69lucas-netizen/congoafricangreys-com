# RED Baseline — Visual Intelligence + Entity Graph skills (2026-07-31)

Ran both pasted enterprise prompts **cold, with no skill**, against the live built page
`dist/congo-african-grey-for-sale/index.html` (285 KB, 6,268 visible words). Recorded
verbatim what went wrong. Every failure below is what the two new skills must close.

## Page ground truth (established AFTER the probes were fixed)

| Metric | Value |
|---|---|
| Headings | H1 1 · H2 15 · H3 21 · H4 13 · H5 11 · H6 6 |
| Images | 52 `<img>` · 33 with `srcset` · 15 decorative `alt=""` · **37 unique non-empty alts, zero duplicates** |
| Schema | 15 JSON-LD types — 5 `Product`, 4 `Offer`, 10 `Question`/`Answer`, `FAQPage`, `AggregateOffer`, `AggregateRating`, `ItemList`, `BreadcrumbList`, `WebPage`, `Organization`, 2 `Review` |
| Links | 123 internal · 9 external |
| Structure | 1 table · 10 `<ul>` · 10 `<details>` · 17 reserve/contact anchors |

## Baseline failures

**B1 — 18 scores demanded, zero measurement instructions.** The prompt asks for Visual
Hierarchy /10, "Eye flow", "Layout balance", "Reading path". With no viewport open the
only available move is to score from HTML source. **Every one of those numbers would have
been invented and presented as measurement.**

**B2 — two probe bugs before a single correct number.** `grep -o "<$h[ >]"` returned
`h1: 0 … h6: 0` on a page with 1/15/21/13/11/6 headings (zsh ate the bracket expression).
A `printf` retry failed again. Reported as-is, that is "this page has no heading
hierarchy" — the 13th checker to cry wolf on this site.

**B3 — a fabricated defect nearly shipped.** `52 alts / 38 unique` reads as *14 duplicate
alts → Rule 50b violated*. Truth: 15 legitimately decorative `alt=""` plus 37 unique
non-empty alts. **Zero violations on a compliant page.** The generic prompt has no concept
of decorative alt, so it manufactures the defect.

**B4 — predicate extraction with no authorization layer.** `SCREENED_FOR(PBFD)`,
`CERTIFIED_BY(CITES)`, `PRICED_AT($1,500–$8,500)` all extract cleanly as edges. Nothing in
the prompt checks them against the Verified-Claim Ledger, and nothing blocks
`IMPORTED_FROM(Africa)` if prose ever implies it. An un-gated graph is a CITES liability.

**B5 — "continue until exhaustion" has no stopping rule.** Output is unbounded,
irreproducible run-to-run, and cannot be diffed week over week.

**B6 — 18 scores, zero owners.** Nothing routes a contrast failure to
`cag-page-hardening` or sibling-sameness to `cag-component-refresh`. Findings die in the
report.

**B7 — Skill 2 would rebuild graph math from scratch**, ignoring that `graphify` already
ships community detection, centrality, GraphRAG JSON and Neo4j export.

**B8 — the richest entity source on the page was walked past.** 15 JSON-LD types sit in
`dist/`; a text-first extractor never opens them, and never notices prose↔schema drift.

## GREEN criteria

A skill passes when, on this same page, it: measures in a painting viewport or prints
`NOT MEASURED`; reports the correct heading and alt figures; refuses an un-ledgered edge;
terminates deterministically; and names an owning specialist for every finding.

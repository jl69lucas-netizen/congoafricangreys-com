# CongoAfricanGreys.com — Project Guide

C.A.Gs is a Midland, Texas breeder of captive-bred Congo and Timneh African Greys
(Mark & Teri Benjamin, since 2014). The site is transactional + informational: for-sale
and location pages take inquiries, care and comparison pages earn the traffic.

## Paths and deploy model

- **`src/pages/<slug>/index.astro` (or `index.html`) is what ships.** `site/content/` is a
  staging area and is never built directly. If both exist, `src/pages/` wins.
- Build `npx astro build` → `dist/`. Every gate measures `dist/`, never source.
- **Work on `main`.** Only `main` auto-deploys (GitHub Actions → Cloudflare Pages on push).
  Finished work on any other branch is live-404 while looking done.
- Commit **and push** after every build. Push *is* deploy.
- After adding or removing a page: `python3 scripts/generate_sitemaps.py`.

## The rules live in `rules/`, not here

This file used to carry ~37 rules in 88,000 characters, and the measured result was that
rules were re-asserted rather than enforced. **The pixel-level rules are enforced by
`tests/render/`, not by this file** — a check that fails the build is worth more than a
paragraph that asks nicely.

| Pack | Covers |
|---|---|
| [`rules/headings.md`](rules/headings.md) | H1–H6 outline gate, Title Case, header style |
| [`rules/images.md`](rules/images.md) | uniform in-body sizing, alt-text keyword spread |
| [`rules/schema.md`](rules/schema.md) | structured data, schema-only freshness |
| [`rules/links.md`](rules/links.md) | Link-First anchor placement |
| [`rules/copy.md`](rules/copy.md) | voice, originality, entity method, claims |
| [`rules/design.md`](rules/design.md) | the nine non-negotiable visual rules |
| [`rules/gates.md`](rules/gates.md) | pre/post-build process gates |
| [`rules/deploy.md`](rules/deploy.md) | where work lands and how it ships |
| [`rules/for-sale.md`](rules/for-sale.md) | the transactional cluster's own rules |

`data/quality/rule-index.json` is the machine-readable index: every rule is `test`,
`judgment`, or `untested`. **`untested` means deletion candidate** —
`python3 scripts/quality_report.py` §5 prints the list on every run.

### Page type → what to read first

| Building… | Skill | Extra rule packs |
|---|---|---|
| for-sale / buy | `cag-for-sale-page-builder` | for-sale, images, headings |
| bird `/available/<slug>/` | `cag-bird-listing-page` | schema, images |
| comparison | `cag-comparison-page-builder` | images, headings, copy |
| interior / care / trust | `MANUAL INTERIOR-PAGE CHECKLIST.md` | headings, links |
| location | `cag-location-page-builder` | copy, links |
| blog | `cag-blog-post` | headings, images |
| Reddit-modifier | `reddit-strategy` | copy |

Full task→entry-point table: [`docs/reference/quick-start.md`](docs/reference/quick-start.md).

## The twelve rules that stay here

These twelve have **no mechanical decision procedure**, which is exactly why they cannot
be delegated to a test and must stay in context. Every other rule moved to a pack. Full
text and the recorded reason for each: `data/quality/rule-index.json` + the packs.

1. **First-person brand voice.** Write as the breeder: *we / us / our / here at C.A.Gs*.
   Our birds and credentials are framed as ours, never described from outside. Neutral
   register is correct only for species/taxonomy facts and cited research.
2. **CITES framing.** African Greys are **Appendix I** (uplisted CoP17, effective Jan
   2017) and IUCN Endangered (Congo) / Vulnerable (Timneh). All our birds are
   captive-bred in the USA with full documentation. Never imply wild-caught or illegal
   trade. "Appendix II" is always wrong and must be corrected on sight.
3. **Work on `main`, never a feature branch** — see the deploy model above.
4. **Always commit and push after a build.** Do not leave finished work unpushed.
5. **Recommend + Why.** Whenever you present options, mark exactly one
   **(Recommended)**, justify it from real data (GSC, competitors, the codebase — never
   taste), and name the trade-off of the recommended pick.
6. **Restate the brief before you build.** Goal · scope · gates · what "done" means ·
   what is out of scope. Improve the prompt where it is ambiguous so it can be corrected
   before work is spent on it.
7. **Preview before apply.** Any page redesign is previewed and approved before it is
   written to site files. A redesign never adds or removes content — visual layer only.
8. **Confidence gate, 97%.** Below that, do not dead-stop: write finished work to disk,
   log the open question to the session brief's `## Open Flags`, ask exactly ONE narrow
   question, and keep building everything that is not blocked.
9. **Write from the outline, never from a sibling.** Reuse components, CSS and structure
   freely; write every page's PROSE fresh from its own outline. Never open a sibling's
   file to copy paragraphs. Only the whitelist may match verbatim. Enforced *after* the
   fact by `dup-no-sibling-crossover`, but the rule is about method: a page copied and
   then reworded passes the test and still breaks the rule.
10. **No fabricated claims.** Never invent credentials, prices, reviews, test results or
    competitor metrics. Un-fetched data is written `NOT FETCHED`, never inferred.
11. **The Verified-Claim Ledger bounds every health and credential claim.** It lives in
    `.claude/agents/cag-entity-incorporation-agent.md` +
    `sessions/2026-06-03-homepage-entity-map.md`. PBFD / Polyomavirus PCR screening, DNA
    sexing, psittacosis and UV-B/D3 are in it. Anything not in it is not assertable.
12. **Brand-owned method labels.** *The Benjamin Home-Raising Protocol* (hand-feeding,
    weaning, the 12–16-week gate) and *The Midland Socialization Method* (family
    handling, out-of-cage routine). Two labels, defined once at first use, never implied
    to be third-party certification. Never invent a third.

Two facts are wrong in circulation and must be corrected on sight: CITES is
**Appendix I**; the Congo range is **$1,500–$3,500** (the bonded pair sets the ceiling).

**The guarantee may be written either "72-hour" or "3-day" — both are correct and neither
is a defect.** They are the same guarantee said two ways, and the breeder uses both
deliberately. This previously read as a correct-on-sight error, which sent agents hunting
across 53 live pages (the homepage included) to "fix" copy that was already right.
Do not rewrite one into the other, and do not flag it.

## Gates — run these, do not re-derive them

```bash
npm run test:render:meta
```
```bash
npm run test:render:pages
```
```bash
python3 scripts/quality_report.py
```

`test:render:meta` is the gate that checks the checkers — run it **before** trusting any
page result. `test:render:pages` measures the target pages at 375/768/1280 in a real
browser. `quality_report.py` prints rework rate, worst family, open overrides and the
untested-rule list.

Also: `python3 scripts/final_page_audit.py [--birds]` · `python3 scripts/page_hardening_scan.py <slug>`
· `python3 scripts/dup_content_audit.py [--headers]` · `python3 scripts/aeo_audit.py <slug>`
· `bash scripts/health-sweep.sh`.

**A gate's output is a hypothesis about the page, not a fact about it.** Twelve checkers
have cried wolf on this site, and two reported PASS having examined zero pages. Before
editing anything in response to a gate, confirm the defect on the built page; before
believing a PASS, read the gate's own examined count. `skills/cag-gate-integrity.md`.

**When a defect escapes, charge it to the harness, not to a new rule.** If an invariant
already covered it and stayed quiet, the tool is broken: add the case to
`tests/render/fixtures/known_broken/`, watch the meta gate fail, fix the check, and write
no new rule. Measured twice — 2026-07-31 produced ten findings, all ten in the harness;
2026-08-01 collapsed a 418-row baseline to 85 with zero page edits.

## Brand context — read before any design or content work

`PRODUCT.md` (strategic: register, users, personality, anti-references, a11y bar) and
`DESIGN.md` (visual: locked palette, typography, components, motion, iconography) are the
single source of truth. `IMAGE-DESIGNS.md` is the image art-direction source of truth.
`docs/design.md` and `docs/reference/components.md` carry the component registry and the
page-width system.

## Where everything else went

- [`docs/reference/system-registry.md`](docs/reference/system-registry.md) — all 68 agents, every skill, every script, the data files
- [`docs/reference/quick-start.md`](docs/reference/quick-start.md) — task → entry point, and the reference-doc index
- [`docs/reference/session-log.md`](docs/reference/session-log.md) — build history and **Known Issues**
- [`docs/reference/WORKFLOW.md`](docs/reference/WORKFLOW.md) — the sprint model
- [`docs/reference/seo-rules.md`](docs/reference/seo-rules.md) — the 62 numbered SEO rules

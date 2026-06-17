# RED Baseline — Comprehensive Page Audit Skill

This is the RED baseline (failing test) for `skills/cags-comprehensive-page-audit-system.md`, per the writing-skills Iron Law. A clean general-purpose subagent (no framework, no skill) was asked to audit `https://congoafricangreys.com/best-african-grey-parrot-food/`. Its full output is captured below; the gap annotation follows.

> **Key finding:** subagents inherit the project `CLAUDE.md`, so the "un-guided" auditor was already CAG-safe — it honored no-visible-date, did not hardcode a palette, did not fabricate metrics, and used a real Firecrawl fetch. **Therefore the skill's value is NOT re-teaching house rules** (CLAUDE.md already enforces those) — it is enforcing STRUCTURE + the 5 missing scorers + the competitor step + a unified scorecard/verdict + specialist routing. The skill should lead with that and keep the CAG-safety block as a lightweight guardrail, not its centerpiece.

## RED Baseline (no skill)

Page type: Informational care guide (commercial-informational hybrid). Retrieved 200 via Firecrawl, ~2,600 body words.

The auditor produced ~7 self-chosen sections + a ranked recommendation list:
- **Overall 88/100** narrative verdict (not the prescribed tier scale).
- §1 SEO 90/100 — single H1, 12 question-H2s, canonical/og/robots correct, breadcrumb schema, schema-only dates (compliant), strong internal + authoritative outbound links. Issues: ~150-char 4-clause title (tail decorative), `/african-grey-care/` vs `/african-grey-parrot-care-guide/` possible duplicate-hub, footer nav titles as `<h3>` diluting outline.
- §2 AEO 94/100 — FAQPage schema (8 Q&A), bolded one-sentence lead answers per H2, dense correct entities, ItemList of 4 brands. Gaps: summary grid only visual; no `speakable`.
- §3 Entity 92/100 — narrative; opportunity: portion-size g/day table, conversion-by-age, organic vs non-GMO cost, storage, mash recipes.
- §4 UX 88/100 — two-tier jump-nav + TOC, scannable grids, 19 images all width+height (CLS-safe), 17 lazy, 0 missing alt (7 decorative empty alts correct).
- §5 CRO 80/100 — 6 priced bird cards mid-page with required shipping line + trust badges + Inquire CTA; on-page inquiry form. Issues: no body click-to-call (tel only in footer), zero on-page social proof (despite 52 real reviews), heavy form deters soft inquiries.
- §6 Schema 75/100 — Article/FAQPage/ItemList/BreadcrumbList present; **MISSING Product/Offer on all 6 priced bird cards** (homepage already has the pattern), Article author is Organization not Person, no Review/AggregateRating.
- §7 Visual 85/100 — Direction-D compliant; opportunities: brand-comparison infographic (760px) + diet-ratio plate/pyramid infographic (link-bait/AI-citation); real feeding photos are strong E-E-A-T.
- Priority recs (ranked): Product/Offer schema first, body click-to-call, real testimonial+Review schema, Person author, resolve care-hub duplicate, two infographics, portion table, demote footer h3s, lighter contact path.

(Full verbatim output retained in the dispatch log; the structure + scores above are the faithful capture for testing.)

## Gaps the skill must close

Despite being CAG-safe, the un-guided audit missed the framework's required structure and scorers:

1. **No 17-section structure** — used ~7 self-chosen sections instead of the prescribed Page-ID → Final-Verdict order.
2. **No §3–4 SERP competitor analysis** — it audited only the CAG page; it never fetched the top-3 ranking competitors or produced a "why CAG wins/loses" + Competitive-Advantage /10. (Biggest omission.)
3. **No AEO /10 rubric** — gave "94/100" narrative, not the explicit 10-item YES/NO checklist → /10.
4. **No Entity-coverage /10** — narrative "92/100", no covered÷expected ratio + Important-Missing-Entities list with why-it-matters-for-AI.
5. **No Visual-asset decision TABLE** — discussed visuals in prose; did not produce the per-section `| Section | Need Visual? (YES-Mandatory/Recommended/MAYBE/NO) | Type | Why |` table, and did not hand image prompts to image-prompt-generator.
6. **No Backlink-magnet /10** — mentioned link-bait infographics but assigned no 0–10 score and no "why a site would link" magnet spec.
7. **No final 8-axis scorecard + verdict tier** — gave an ad-hoc "88/100", not SEO/Semantic/AEO/Entity/UX/Visual/CRO/Backlink + Competitive-Advantage + Elite/Strong/Good-but-incomplete/Average/Weak/Major-rebuild tier.
8. **No specialist routing** — did everything itself; did not route §5→keyword-verifier, §7→entity agent, §14→internal-link-agent, §16→conversion-tracker, etc. (the chain).
9. **No page-type weighting** — didn't map to a CAG page type to weight the sections.

These nine gaps are what `cags-comprehensive-page-audit-system.md` must enforce. (Palette, dates, fabrication, CITES are already handled by CLAUDE.md — keep them as a short guardrail, not the focus.)

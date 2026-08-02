# Anchor placement

Rules moved out of `CLAUDE.md` on 2026-08-02 (Phase 4). **The rule text is verbatim.**

`enforced:` says what actually holds the rule up.
`test` — a committed check fails when the rule is broken. `judgment` — no mechanical
decision procedure exists, and `data/quality/rule-index.json` records why.
`untested` — **a deletion candidate**: it is asserted and nothing enforces it.
`scripts/quality_report.py` §5 lists every one of those on every run, which is the point.


---
id: link-first-anchors
enforced: untested
family: NAV
---

- **Link-First anchors (ALWAYS) — applies to EVERY internal and external link, every agent, skill, and page** — The anchor sits at the **START of the sentence/paragraph** — inside the opening words (first clause). **Never mid-sentence, never at the end.** ✅ "Our [Congo care guide] covers diet in depth…" · ❌ "…diet is covered in our [guide]." (Breeder rule 2026-07-11, superseding the old "beginning or middle, never end" rule everywhere.) Sole exception: branded ACTION anchors on CTAs per `skills/cag-branded-hybrid-keywords.md`. Injected into all 68 agent Golden Rules via `scripts/add_link_first_rule.py` — re-run after adding any agent.

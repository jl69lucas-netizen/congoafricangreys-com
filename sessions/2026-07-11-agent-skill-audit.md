# Full Agent + Skill System Audit — 2026-07-11

Scope: all 68 agents (`.claude/agents/`) + 55 skills (`skills/`, incl. 5 added today). Grounded in the documented lessons from the homepage build, the blog cluster, the 18-page Direction-D interior batch, and the comparison cluster. Companion plan: `docs/superpowers/plans/2026-07-11-agent-skill-system-audit-upgrade.md`.

---

## 1. Registration + Handoff Verification (Task 1 result)

| Check | Result |
|---|---|
| Agents on disk | **68/68**, all with valid frontmatter (name/description/tools/model/effort) |
| Agents loadable | **PASS** — every `cag-*` agent appears in the live dispatchable agent list this session |
| Skills registered | **PASS** — `register_skills.py` reports 55/55 mirrored to `.claude/skills/` (was 50, +5 today) |
| Mirror drift | Only 4 non-CAG `openspec-*` dirs extra in `.claude/skills/` — intentional, not drift |
| Model tiers | All agents on Opus 4.8 with effort tiers per `data/agent-registry.json` (spot-checked) |
| CLAUDE.md registry | **WAS BROKEN — FIXED TODAY**: `cag-comparison-page-builder` (the skill that built the whole comparison cluster) had ZERO mentions in CLAUDE.md; no Quick Start route existed for comparison or Reddit pages. Both added. |
| Golden-Rule injections | Clarification Checkpoint + First-Person Voice present in all agents; **Link-First injected into 68/68 today** via new `scripts/add_link_first_rule.py` |

### The "@ only shows grill-me" issue — diagnosis
The agents themselves are fine: all 68 parse and load (I can dispatch every one of them). Nothing in your setup is misconfigured on the repo side. What you're seeing is a **client UI behavior, not a registration failure**: in the Claude Code desktop app, the `@` autocomplete menu surfaces *files and certain mention types*, while project **skills** surface in the `/` slash menu (grill-me shows up because it's a registered skill — and it's the one you use most, so it ranks first). Project subagents don't get their own `@` autocomplete entries in the current desktop build.

**What to do (works today):** just type the agent name in plain text — "run @cag-rank-tracker" or "use cag-content-audit-agent on /blog/" — and I dispatch it via the Agent tool regardless of whether the autocomplete menu showed it. Skills: type `/` and the name (e.g. `/grill-me`, `/reddit-strategy`). If the `@`-menu behavior bothers you, it's worth reporting via `/bug` in an interactive terminal session — but no repo change can fix it because nothing in the repo is wrong.

---

## 2. New Rules Rolled Out Today (all live)

1. **Link-First (Golden Rule, all 68 agents + 17 doc/skill locations):** ALL internal + external links anchor at the START of the sentence/paragraph — never mid-sentence, never at the end. Old "beginning or middle" rule purged everywhere (verified zero stale occurrences in binding docs). Sole exception: branded ACTION anchors on CTAs.
2. **Meaningful words, no stop-word filler:** added to `anti-ai-writing` (canonical spec) + CLAUDE.md Non-Negotiables + seo-rules. **Decision (Recommended): it lives in the anti-ai-writing skill, not a new standalone skill** — same trigger moment (any prose/naming edit), and a standalone skill this thin would never be invoked on its own. Trade-off: anti-ai-writing grows ~150 words. Interpretation used: applies to NAMING surfaces (slugs, anchors, headings, filenames, alts, meta, labels); body prose and the locked conversational question-header pattern stay natural — flag if you meant something stricter.
3. **Image keyword distribution (seo-rules Rule 50b):** primary keyword → primary image's alt ONLY; every other image rotates secondary/LSI/NLP/long-tail; no two images share an alt. Wired into seo-rules, image-metadata, IMAGE-DESIGNS.md, CLAUDE.md. **Bonus fix:** Rule 50 said alt ">250 chars" while the confirmed canonical set says ≤190 — contradiction corrected to ≤190.
4. **internal-link-agent upgraded:** mandatory Step 0 sitemap inventory (sitemap = canonical page universe), Anchor Diversity Ledger (no repeated anchors site-wide per target; exact→partial→LSI→natural rotation, mined from GSC/PAA/keyword-cluster), Link-First placement, corrupted MFS example slugs fixed, dist/-not-source note added.
5. **Duplicate-content gate:** new skill + `--headers` mode added to `dup_content_audit.py`. First run found **68 template crossover headers between african-grey-vs-macaw and african-grey-vs-cockatoo** — each spoke was de-duped against congo-vs-timneh but never against each other. This is an open work item (see §5).

---

## 3. Agent Audit — 68 agents

**Cross-cutting upgrades that apply to EVERY page-builder agent** (instead of repeating per row): (a) Link-First anchors — injected today; (b) run `cag-duplicate-content-gate` before outline approval on any sibling page; (c) Rule 50b image-alt distribution; (d) heading-clamp inversion check (the vw term decides ordering — caught cluster-wide at 900px); (e) H3 band 40–50 / ≥5 H5 + ≥5 H6 with no skips; (f) verify in `dist/`, not source; (g) `src/pages/` is authoritative — several agents still say `site/content/` (systemic, see §5).

### Tier 1 — Orchestrators
| Agent | What it does | Verdict | Improvement |
|---|---|---|---|
| cag-content-architect | Routes content tasks, picks framework per page | **UPDATE** | Framework table predates `framework-pas/fab/library` — point its selection matrix at `framework-library`'s routing table (awareness level × page type) |
| cag-structure-architect | Silo/reverse-silo maps, structure.json | OK | Feed it the sitemap inventory (same Step-0 as internal-link-agent) so structure.json never drifts from real URLs |
| cag-batch-rebuilder | Parallel batch rebuilds | **UPDATE** | Add the two batch lessons: subagents `git add` ONLY named files (the ~100MB A6 incident) and the 32k Write cap (cp + incremental edits) |
| cag-strategy-synthesizer | 2 strategies → recommend 1 | OK | Already Recommend+Why native |

### Tier 2 — Page Builders
| Agent | What it does | Verdict | Improvement |
|---|---|---|---|
| cag-seo-content-writer | Body copy, humor modes, counter-positioning | OK | Add pointer to `framework-pas`/`framework-fab` for problem/spec sections |
| cag-bird-personality | Buyer-archetype bird profiles | OK | — |
| cag-faq-agent | QAB FAQs + FAQPage schema | OK | Add the schema-safe jump-link caveat (no `<a>` inside `{item.a}` schema-bound strings) — it bit the homepage |
| cag-homepage-builder | Homepage rebuild | **UPDATE** | Still points at `site/content/index.md`; homepage is `src/pages/index.astro` (989 lines). Path modernization |
| cag-location-builder | State pages, Florida template | **WATCH** | Before the location batch resumes: wire in dup-content gate (22 near-identical siblings = highest dup risk on the site) + the mvf/cvt-style geo distribution matrix |
| cag-section-builder | Per-section HTML | OK | Carries Interior-Page Standard pointer (updated to Link-First today) |
| cag-purchase-guide / cag-about-builder / cag-species-guide-builder / cag-scam-specialist / cag-financial-strategist | Single-page specialists | OK | All carry the updated Interior-Page Standard pointer; QUEST (framework-library) is the natural upgrade for purchase-guide's vetting flow |
| cag-variant-specialist / cag-timneh-specialist | Variant + attribute cluster | OK | Cross-sell table must pass the header-crossover check between the two variant pages |
| cag-comparison-builder | X-vs-Y pages | **UPDATE** | The SKILL `cag-comparison-page-builder` is canonical; agent should open with a hard pointer to it + the dup-content gate (the 29-header purge happened in its territory) |
| cag-blog-post-agent | Blog posts | **UPDATE** | Predates the `cag-blog-post` skill (14-step architecture, source-of-truth spec); add a Golden-Rule pointer so the agent never builds from its older internal structure. Its anchor-position rule was updated to Link-First today |
| cag-hub-builder | Hub/aggregator pages | OK | Hub-LAST ordering already established; add `/african-grey-reddit/` to its known-hubs list when built |
| cag-infographic-builder | HTML/AI infographics | OK | Rule 50b now governs its alt text (wired via IMAGE-DESIGNS.md) |
| cag-interactive-component | Calculators/quizzes | OK | — |

### Tier 3 — Content Intelligence
| Agent | What it does | Verdict | Improvement |
|---|---|---|---|
| cag-entity-incorporation-agent | 4-Move entity loop | OK | Link placement rules updated to Link-First today; ledger current (PBFD/APV, psittacosis, UV-B) |
| cag-non-commodity-content-agent | Breeder-authentic content | OK | — |
| cag-content-audit-agent | Pre-build 4-phase audit | **UPDATE** | Add Phase 2.5: dup-content gate against siblings (pre-build is exactly where the 29-header failure should have been caught) |
| cag-keyword-verifier | Keyword placement/density | **UPDATE** | Add Rule 50b image-alt distribution + anchor-diversity checks to its pass/fail list |
| cag-image-pipeline | Image moves/renames/refs | OK | Rule 50b + no-stop-word filenames now upstream of it |
| cag-seasonal-content-agent / cag-email-newsletter-agent / cag-video-seo-agent / cag-social-strategist | Calendar/email/video/social | OK | — |
| cag-angle-agent | Hooks + angles | OK | — |
| cag-paa-agent | Real PAA extraction | OK | PAA phrasing now also feeds anchor variations (wired in internal-link-agent) |
| cag-meta-description-agent | Titles + metas | **UPDATE** | Confirm it carries the 2-long-format rule (Title ≤205 / Desc ≤185 or ≤300) — memory says yes, agent text predates it; align + add no-stop-word-filler note |
| cag-external-link-agent | Outbound links | OK | Updated to Link-First today; 403-bot-block rule present |
| cag-framework-agent | Competitor page deep-dives | OK | — |

### Tier 4 — Technical
| Agent | Verdict | Notes |
|---|---|---|
| cag-accessibility-fixer | OK | Battle-tested (A11y-7, lead-paragraph trap, stone-600 floor all documented) |
| cag-performance-monitor-agent / cag-performance-fixer | **UPDATE** | Add the warm-median-of-3 Lighthouse rule + Pillow-not-sips + Rocket Loader `/70de/` diagnosis — all documented lessons not yet in the agent files |
| cag-canonical-fixer / cag-footer-standardizer / cag-redirect-manager / cag-deploy-verifier / cag-google-map-agent / cag-contact-form-updater | OK | Deploy-verifier note: IndexNow = Bing/Yandex, not Google (documented) |
| cag-agent-system-qa | **UPDATE** | Add the new checks to its checklist: Link-First marker present, skill registered in CLAUDE.md, `register_skills.py` clean |
| cag-site-hygiene-agent | OK | Owns cannibalization — dup-content gate's "same intent" findings route here |

### Tier 5 — Trust & Authority
| Agent | Verdict | Notes |
|---|---|---|
| cag-trust-signals-agent | OK | reviewCount 52 (real) is the locked figure |
| cag-case-study-agent / cag-review-collection-agent | OK | Only real reviews — fabricated-testimonial purge is the standing lesson |
| cag-conversion-tracker / cag-ab-test-agent | OK | — |

### Tier 6 — SEO & Analytics
| Agent | Verdict | Notes |
|---|---|---|
| cag-competitor-registry / cag-competitor-intel / cag-rank-tracker | OK | Sprint 0 complete; weekly loop defined |
| cag-gsc-analytics | **WATCH** | Blocked on GSC connection (known issue) — once connected, it also feeds Reddit-modifier keyword discovery |
| cag-llm-keyword-intel | OK | Natural partner for reddit-strategy (LLMs cite Reddit) — add one pointer line |
| cag-directory-submission / cag-competitive-keyword-gap / cag-competitor-pricing-alert / cag-branded-search-monitor / cag-nap-citation / cag-backlink-outreach | OK | — |

### Tier 7 — Conversion & CRM
| Agent | Verdict | Notes |
|---|---|---|
| cag-email-lead-nurture / cag-heatmap-analyst / cag-funnel-analysis / cag-clutch-manager / cag-self-update | OK | Clutch-manager stays single source of truth for inventory |

---

## 4. Skill Audit — 55 skills

**Framework skills (11):** aida, aio-geo, bab, ebp, eeat, heading-hierarchy, pdb, qab — OK. **NEW today: pas, fab, framework-library** (long-tail catalog + routing table + EBP disambiguation). The core-four (AIDA/PAS/BAB/FAB) is now complete.

**Build skills:** cag-seo-master-checklist (OK — Link-First updated) · cag-blog-post (OK — canonical over the agent) · cag-comparison-page-builder (OK — now registered in CLAUDE.md, Link-First updated) · cag-bird-listing-page / cag-bird-page-build / cag-bird-page-excellence (OK — note: three bird skills coexist; listing=lean build, page-build=22-section deep build, excellence=polish/QA. **Recommendation:** keep all three but they should cross-reference the boundary explicitly — small follow-up) · cag-location-page-builder (WATCH — apply dup-gate before the batch) · grill-me (OK) · cag-direction-d-theme (OK — global theme, never re-implement per page).

**QA/gate skills:** cag-final-page-pass (**UPDATE** — add a dup-content-gate step to its per-profile checklist so the gate runs at final pass automatically) · manual-auditor-check (OK, superseded-but-kept for interior) · cags-comprehensive-page-audit-system (OK) · section-auditor (OK) · **NEW: cag-duplicate-content-gate**.

**Link/keyword skills:** internal-link-agent (**UPGRADED today** — sitemap Step 0, Anchor Diversity Ledger, Link-First, corrupted slugs fixed) · keyword-cluster (OK — now feeds anchor variations) · cag-branded-search-skill / cag-branded-hybrid-keywords (OK — action-anchor exception preserved) · **NEW: reddit-strategy**.

**Writing skills:** anti-ai-writing (**UPGRADED today** — Meaningful Words / no-stop-words section) · social-content, caption-writer, youtube-script, image-prompt-generator (OK) · image-metadata (**UPGRADED today** — Rule 50b block).

**Technical/utility skills:** cag-website-health, sitemap-agent, cag-indexing, cag-broken-links, cag-footer-agent, cag-google-map, cag-header-search, cag-contact-form, cag-site-patterns, cag-cta-strategy, cag-design-rebuild, cag-multi-agent-design, cag-logo-generator, cag-image-generation, cag-infographic, cag-photo-ingest, cag-entity-agent, session-closer — OK. sitemap-agent note: the clobber bug fix (write_both) is documented and holding.

---

## 5. Open Work Items (routed, not silently dropped)

1. **68 macaw↔cockatoo template crossover headers** — found by the new `--headers` mode. Needs a rewrite pass (page-specific framing) exactly like the July purge, plus a pairwise sweep of amazon-parrot and breeders-comparison spokes. ~1 session.
2. **Existing live pages violate Link-First** — every page built before today has mid-sentence links (they were correct under the old rule). Recommend: migrate opportunistically (any page touched for another reason gets its links repositioned) rather than a big-bang rewrite. Trade-off: mixed state for a while, but zero token waste on pages that are ranking fine.
3. **Path modernization sweep** — many Tier-2/3/4 agents still reference `site/content/` as the edit target; `src/pages/` is authoritative. One scripted pass + review. 
4. **Small agent pointer edits** (content-architect→framework-library, comparison-builder→skill, blog-post-agent→skill, content-audit→dup gate, final-page-pass→dup gate, keyword-verifier→Rule 50b, perf agents→median-of-3): batched follow-up, ~1 short session.
5. **New-skill pressure-testing** — today's 5 skills were built against documented real-failure baselines (the RED evidence is cited inside each), but none has had a subagent pressure test yet (superpowers:writing-skills discipline). Recommend testing reddit-strategy + duplicate-content-gate first — they gate real builds.
6. **First Reddit build** — recommend starting with `/african-grey-vs-amazon-reddit/` (research folder complete, thread verified, r/parrots pos-1 evidence) as the pilot compact page.

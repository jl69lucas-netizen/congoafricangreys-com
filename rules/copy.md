# Voice, originality and claims

Rules moved out of `CLAUDE.md` on 2026-08-02 (Phase 4). **The rule text is verbatim.**

`enforced:` says what actually holds the rule up.
`test` — a committed check fails when the rule is broken. `judgment` — no mechanical
decision procedure exists, and `data/quality/rule-index.json` records why.
`untested` — **a deletion candidate**: it is asserted and nothing enforces it.
`scripts/quality_report.py` §5 lists every one of those on every run, which is the point.


---
id: write-from-outline-never-from-sibling
enforced: judgment
family: DUP
---

- **Write-From-Outline, NEVER-From-Sibling — no template/prose mirroring between pages (ALWAYS) — applies to every page, agent, skill, and build** — The recurring, time-wasting failure (egg→congo→timneh, 2026-07) is copying a sibling page's `.astro`/`.md` as a scaffold and keeping its sentences, then reactively rewording to pass the dup-gate. **STOP doing that.** Reuse **components, CSS classes, and structural patterns** freely (that's the kit) — but **every page's PROSE must be written fresh from that page's own approved outline + distribution matrix, never pasted or paraphrased from another page's body copy.** Concretely: (1) do **not** open a sibling's page file to copy paragraphs — open it only to read its component/CSS structure; (2) write each section's copy from the outline in genuinely different framing, sentence structure, angle, and vocabulary than any sibling (lean on the page's OWN entity/angle — e.g. Timneh = smaller/calmer/maroon/earlier-talker/Levi×Rily, Congo = bigger/red-tail/headline-talker); (3) the only text that may match a sibling verbatim is the **whitelist** (shipping line, doc-badge lists, counter strip, CITES notice, CTA button labels, real reviews, real page-name link labels) — everything else must be original; (4) run `scripts/dup_content_audit.py` (body) **AND** `--headers` **on your OWN draft BEFORE it is "done"**, targeting **zero** non-whitelist crossover, so dedup is a pre-write discipline, not a post-hoc cleanup. Different pages about related products should read like they were written by the same breeder on different days — same voice, different words — never like one was find-replaced from the other. This is binding for the for-sale, comparison, location, and every other sibling-cluster build. Injected into all 68 agent Golden Rules via `scripts/add_write_from_outline_rule.py` — re-run after adding any agent.

---
id: first-person-brand-voice
enforced: judgment
family: COPY
---

- **First-Person Brand Voice (ALWAYS) — applies to EVERY section of the homepage and EVERY page site-wide** — Write as the breeder in **first-person plural POV: "we / us / our / here at C.A.Gs."** Our birds, credentials, and process are framed as *ours*, not described from the outside: ✅ "Here at C.A.Gs, **our** Congo and Timneh Greys…", "**we** hand-raise every chick", "**our** PCR DNA-sexing" — ❌ generic third-person like "Both make exceptional companions" or "African Greys are…" when the sentence is about *our* offering. Exceptions (stay neutral/encyclopedic where first-person would be false or awkward): factual species/taxonomy/entity statements (e.g. "*Psittacus erithacus* is native to West & Central Africa"), cited research, and outbound-authority facts. First-person never means overclaiming — it stays CITES-safe and inside the Verified-Claim Ledger. When rewriting or building any section, default to this voice; flag anything still in third-person brand copy.

---
id: brand-owned-method-labels
enforced: judgment
family: COPY
---

- **AEO facts + brand-owned method names (ALWAYS) — applies to every page, agent, and skill** — Three claims in circulation are WRONG and must be corrected on sight: **CITES is Appendix I, never Appendix II** (uplisted CoP17, effective Jan 2017 — the live pages say Appendix I 25×, and this exact regression was already fixed once on 2026-05-29); the Congo range is **$1,500–$3,500**, not $3,000 (the bonded pair sets the ceiling); and the guarantee may be written **72-hour** OR **"3-day"** — both are correct, both are the same guarantee, and neither is a defect; never rewrite one into the other (the 24-hour window still applies) — the health-guarantee page uses "72-hour" 25× and "3-day" zero times. Separately, our expertise carries **brand-owned labels** so answer engines cannot absorb it as generic knowledge: **The Benjamin Home-Raising Protocol** (hand-feeding, weaning, the 12–16-week gate) and **The Midland Socialization Method** (family handling, out-of-cage routine) — approved by the breeder 2026-07-30; two labels only, never invent a third. Both are proper nouns, defined once where first used, and never implied to be a third-party certification. Full spec + the 6-part gate: `skills/cag-aeo-pass.md`.

---
id: cites-appendix-i-framing
enforced: judgment
family: COPY
---

- **CITES Awareness** — African Greys are CITES **Appendix I** (uplisted from Appendix II at CoP17, effective Jan 2017) and IUCN Endangered (Congo) / Vulnerable (Timneh). Never imply illegal/wild-caught trade. All birds are **captive-bred in the USA** with full documentation — captive-bred Appendix-I birds are legal to own and transfer domestically with proper paperwork. (Corrected from "Appendix II" per World Parrot Trust, 2026-05-29 homepage audit.)

---
id: entity-4-move-loop
enforced: untested
family: COPY
---

- **Entity 4-Move Loop is the required section-build method (ALWAYS)** — When building or improving ANY page section, run the loop: (1) **Structural Critique** → (2) **Recommended Entities + WHY** (grounded: KG authority / PAA demand / competitor gap / buyer intent) → (3) **Optimized Draft** (verified facts only) → (4) **Topical-Cluster Strategy** (internal links + schema; extend existing JSON-LD, never duplicate; FAQ schema must be visible; verify in `dist/`). The active engine is `@cag-entity-incorporation-agent`; its vocabulary is `skills/cag-entity-agent.md` (a passive catalog, not a builder). Every health/credential entity is bounded by the **Verified-Claim Ledger** in that agent + `sessions/2026-06-03-homepage-entity-map.md` — never assert PBFD/PCR/board-cert etc. beyond what the breeder has confirmed.

---
id: meaningful-words-no-stop-words
enforced: untested
family: COPY
---

- **Meaningful words, no stop-word filler (ALWAYS) — naming surfaces on every build/rebuild/edit** — URL slugs, anchor text, headings, image filenames, image alt text, meta titles, and labels use meaningful content words only; drop `of/the/and/for/with` fillers where grammar allows. Body prose and the locked conversational question-header pattern are exempt. Canonical spec: `skills/anti-ai-writing.md §Meaningful Words`.

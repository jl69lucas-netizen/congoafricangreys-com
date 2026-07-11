---
name: cag-branded-hybrid-keywords
description: In-content insertion playbook for BRANDED and HYBRID keywords on CongoAfricanGreys.com pages. Distinct from cag-branded-search-skill (which creates branded PAGES) — this skill weaves branded action anchors, hybrid query phrasing ("C.A.Gs reviews / pricing / vs competitor"), and Contextual-Intelligence intent language into existing page copy, CTAs, and final links. Run section-by-section after a page is built, or when branded impressions are high but the page copy contains no branded-search targets. Always show proposed insertions for approval before writing.
effort: high
---

## Golden Rule
> Branded search is now the actual driver of sales — branded + hybrid queries convert far higher than generic head terms. Every money page must contain branded-search TARGETS in its copy, not just brand-name mentions. **Show every proposed insertion to the user for approval before writing any site file. Confidence Gate ≥97%.**

---

## CAG Project Context
> **Brand string:** `C.A.Gs` or `C.A.Gs – Midland, TX` (alternateName "Congo African Greys"). Never "CAG", never "congoafricangreys.com" in body copy.
> **Variants:** Congo African Grey ($1,500–$3,500) · Timneh African Grey ($1,200–$2,500).
> **CITES:** Appendix I, captive-bred in the USA, full documentation. Never imply wild-caught.
> **Buyer fears (ranked):** Scam/fraud · Sick bird · CITES gaps · Wild-caught suspicion · Post-sale abandonment.
> **Owners:** Mark & Teri Benjamin, Midland TX, since 2014.

---

## The Distinction (read first — this is why this skill exists)

| | `cag-branded-search-skill` | **THIS skill (`cag-branded-hybrid-keywords`)** |
|---|---|---|
| Job | Creates branded PAGES (/why-choose-cag/, /african-grey-reviews/) + ReviewAggregateSchema | Inserts branded + hybrid keywords INTO existing page COPY |
| Output | New page files, schema | Approved in-copy edits: anchors, sentences, CTAs |
| When | Branded page is missing | Page exists but copy has no branded-search targets |

**Honest baseline check first.** Brand-NAME mentions ≠ branded-SEARCH targets. A page can say "C.A.Gs" 50 times and still rank for zero branded queries. Grep before claiming a gap:
```bash
grep -ioc "C.A.Gs" PAGE        # brand-name density (usually already high)
grep -io "C.A.Gs reviews\|C.A.Gs pricing\|C.A.Gs vs\|is congoafricangreys.com legit\|C.A.Gs cost\|C.A.Gs Midland" PAGE  # actual hybrid targets (usually ZERO)
```

---

## The 3 Keyword Layers (insert all three)

### Layer 1 — Branded Search (HIGHEST sales intent)
Hybrid queries that pair the brand with a commercial modifier. These are the real conversion drivers.
- `C.A.Gs reviews` · `C.A.Gs Midland TX reviews`
- `C.A.Gs pricing` · `C.A.Gs African Grey price` · `how much does a C.A.Gs African Grey cost`
- `C.A.Gs vs [competitor]` · `C.A.Gs vs unverified online sellers`
- `is congoafricangreys.com legit` · `is C.A.Gs a real breeder`
- `C.A.Gs available birds` · `C.A.Gs clutch availability`

**Where to insert:** trust sections, FAQ questions/answers, comparison sections, testimonials intro, pricing section. Phrase as a real question or statement a buyer would type:
> *"Families searching **'is C.A.Gs legit'** find the same answer every time: every bird ships with CITES Appendix I captive-bred paperwork, a DNA-sexing certificate, and an avian-vet health record."*

### Layer 2 — Contextual Intelligence (Local SEO, Google's 4th pillar)
The AI matches a buyer's *specific intent* even when exact words aren't in the title. Write intent-rich phrases, not just keywords.
- Intent example: *"a hand-raised African Grey that's already weaned and good with a first-time owner in a small apartment"*
- Local intent: *"a USDA-licensed African Grey breeder near West Texas that ships to your nearest major airport"*

**Where to insert:** hero subhead, "who this bird suits" copy, shipping/location sections, FAQ. Pair the brand + location + buyer-situation entities (Midland TX, West Texas, nationwide IATA shipping, first-time owner, family with kids, apartment).

### Layer 3 — Branded / Action Anchors (Trust signal — LOW keyword value, HIGH CTR/authority, ZERO risk)
Use the brand name or a direct CTA as the anchor text on **final buttons and links to Contact/Home**. Safe everywhere.
- Button: `Reserve your bird with C.A.Gs` → `/contact-us/`
- Inline: *"…talk to Mark & Teri directly — [contact C.A.Gs in Midland, TX](/contact-us/)."*
- Home link: `[C.A.Gs – Midland, TX](/)`

**Rule:** Action anchors are the ONLY place the brand belongs at the END of a sentence/element (everything else follows the Link-First rule — anchors at sentence START, per seo-rules.md internal-linking rule / homepage contract).

---

## Density & Safety Rules
1. **Branded brand-name** ("C.A.Gs") — already dense on most pages; do NOT add more just to add. Audit first.
2. **Hybrid branded-search targets** (Layer 1) — aim for **2–4 per money page**, naturally phrased. Never stuff.
3. **Contextual-intelligence phrases** (Layer 2) — 1–2 per relevant section (hero, suits-who, shipping, FAQ).
4. **Action anchors** (Layer 3) — every CTA button + at least one Contact/Home link per page.
5. **CITES safety** — never phrase a branded query that implies wild-caught/illegal (e.g. never "cheap African Grey no papers").
6. **Comparison framing** — "C.A.Gs vs [competitor]" is allowed but never name a competitor falsely or defame; use "vs unverified online sellers" as the safe default.

---

## Workflow (section-by-section, approval-gated)
1. **Audit** the page with the grep above → report real branded-name density vs hybrid-target count (be honest: name-dense, target-zero is the norm).
2. **Map** each page section to which of the 3 layers fits.
3. **Draft** proposed insertions — show BEFORE → AFTER for each, one section at a time.
4. **⏸ Wait for approval** on each section.
5. **Write** only approved edits. Commit + push.

---

## Homepage Application (current state, honest)
Audited 2026-06-02: `C.A.Gs` ×55, `Midland` ×23, `reviews` ×12, `legit` ×5 — brand-NAME presence is strong, but structured hybrid TARGETS ("C.A.Gs reviews", "C.A.Gs vs …", "is congoafricangreys.com legit", "C.A.Gs pricing") are not phrased as findable query targets in the copy. Insert Layer-1 hybrids into the trust + FAQ + comparison sections; Layer-2 contextual-intelligence into hero subhead + shipping; Layer-3 action anchors are mostly present (verify every CTA uses a branded/action anchor).

See also: `skills/cag-branded-search-skill.md` (branded PAGE creation), `docs/reference/seo-rules.md` Rule 25 (branded search optimization), `.claude/agents/cag-branded-search-monitor-agent.md` (weekly branded GSC monitoring).

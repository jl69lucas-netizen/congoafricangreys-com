# AEO / Entity / Voice / Fan-Out Verification Audit — 18 Interior Pages (2026-06-11)

Method: inline `dist/` verification sweep (no subagents), per the 2026-06-11 fixes plan
Tasks 5–6. These pages were built to the Interior-Page Standard 2026-06-06→11, so this
pass verifies the standard landed rather than rebuilding.

## AEO / Schema
- **FAQPage JSON-LD: 16/18 PASS.** Missing only on contact-us (has ContactPage schema —
  correct) and privacy-policy (legal shell — correct). No action.
- **Visible FAQ matches schema: PASS.** All content pages use the `cag-faq-acc`
  aria-expanded accordion pattern (17–20 `aria-expanded` nodes per page), satisfying the
  "FAQ schema must be visible" rule. (`<details>` grep is the wrong probe on this site —
  see MEMORY `project_interior_build_pattern`.)
- **Direct-answer-first: PASS.** Every content page opens with a "(The 30-Second Answer)"
  / "(The Short Answer)" style H2 + declarative lead.

## Entity coverage
Entity density (Psittacus erithacus / Appendix I / USDA / DNA probe): 17–150 hits per
content page; weakest are how-to-tame (17 — appropriate: training topic) and privacy (5 —
legal). All claims inside the Verified-Claim Ledger. No gaps requiring edits.

## First-person voice
Present on all brand-copy pages. Zero-hit pages are exceptions by rule: african-grey-reviews
(buyer-quoted testimonials) and privacy-policy (legal text verbatim). PASS.

## Humor
Per the honesty policy (≤1 dry beat/section, none on legal/health) — spot-checked, no
violations found; no beats on privacy/health-guarantee FAQ answers. PASS.

## Intent-Based Keyword Fan-Out (retro-audit)
Fan-out was run at cluster level during the batch; per-page H2 maps confirm it landed:
- **Informational** variants: every page leads with How/What/Why/Is conversational H2s.
- **Transactional**: "Which … Greys Are Available Now?" section on 15/18 pages + CTA band.
- **Comparison**: Congo-vs-Timneh blocks on guide, care, care-guide, diet, lifespan,
  captive-bred; adopt-vs-buy on adoption; trustworthy-vs-scam on trusted-breeders.
- **Local**: Midland TX + nationwide-shipping references in copy and schema on all pages.
- **PAA**: FAQ sections sourced from PAA per the batch briefs.
**Verdict: COVERED — no heading patches required.** Two seemingly-empty H2s
(trusted-breeders hero, scams TOC) verified fine — inner markup, not empty headings.

## Outcome
No code changes from Tasks 5–6 — verification passed. Image/infographic opportunities
logged separately in `2026-06-11-image-opportunity-audit.md` (awaiting breeder pick).

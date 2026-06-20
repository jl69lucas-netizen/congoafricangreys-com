# Session Brief — 2026-06-19 · /available/ Bird Pages Full SEO/GEO/AEO

## Goal
Full SEO + GEO + AEO level-up of 6 individual bird pages, inheriting Direction D, to homepage standard.
Pages: `/available/` roys · amie · bery · elad · evie · jins-jeni.

## Locked decisions
- **Depth model = Option A (lean-transactional, leveled up).** 700–1,000 visible words, single
  `Product`+`Offer` (never AggregateOffer), link-out-don't-reteach, **NO per-bird geo-targeting**
  (cannibalization guardrail vs location pages), real-only trust signals, Verified-Claim Ledger,
  no PBFD/Polyomavirus, no visible date (schema only). Direction D inherited via BaseLayout.
- **Deliverable format = breeder's 15-point competitive-analysis template** (delivered).

## Sprint status
- **Sprint 0 (intelligence): DONE.** GSC transactional keyword universe extracted; 30-competitor
  registry re-scored for transactional intent (11 Tier-1 breeders + 8 Tier-2 classifieds); live
  Google SERP top-3 pulled for the 3 clusters (Congo / Timneh / pair). Output:
  `docs/research/2026-06-19-bird-pages-competitive-analysis.md`.
- **Sprint 0.5 (orientation): satisfied** by the breeder's detailed brief + the analysis doc (depth
  decision + per-page angle/framework/archetype/KW matrix all locked). Full grill-me battery skipped
  as redundant — offered.
- **Sprint 1–2 (build): PENDING APPROVAL.** Plan: build **Roys** as the approved reference template
  → preview → approve → batch-apply to the other 5 (each with its own framework/angle/H-structure).

## Per-page assignment (see analysis doc §0.9 + Parts 1–6)
Roys (Congo ♂ $2,300, AIDA) · Amie (Congo ♀ $2,500, BAB) · Bery (Congo ♀ $1,700, PAS) ·
Jins & Jeni (Congo pair $3,500, PDB — biggest new-traffic upside, owns an open SERP) ·
Elad (Timneh ♂ $1,600, EBP) · Evie (Timneh ♀ $1,500, QAB).

## Level-up delta per page (current pages already cover the lean basics)
1. AEO "Bird Snapshot" summary box (top). 2. Snippet-ready 40–50w answers under each H2.
3. Per-page transactional framework + differentiated angle. 4. New counter-positioning H2
($850/$200 scam-cheap vs $6,500 overpriced). 5. +2 PAA FAQs. 6. Entity density pass.
7. Expanded cluster internal links + ledger-safe external (AAV, parrots.org, CITES).

## Open Flags
- (none blocking) — Roys page currently states age "4 months"; sibling cards list Bery 1yr / Amie 3mo /
  Elad 5mo / Evie 6mo. Use page-confirmed ages; confirm with breeder if any age has changed.
- **2026-06-20 — PBFD claim in the Trust & Certification panel image — RESOLVED.** Breeder confirmed C.A.Gs
  PCR-tests every bird for PBFD and holds the records. PBFD/APV screening was already ✅ in the Verified-Claim
  Ledger (homepage map + entity agent); the only inconsistency was the bird-page rules still saying "no PBFD."
  Fixed: retired the "no PBFD on bird pages" gate everywhere — `scripts/final_page_audit.py` (`no_pbfd_claim`
  FAIL→NA), `skills/cag-bird-listing-page.md`, `skills/cag-final-page-pass.md`, `CLAUDE.md`, and added the dated
  per-bird confirmation to both ledger files. Roys trust-panel image kept as-is (now backed). PBFD is now an
  assertable trust signal on bird pages — optionally surface it in bird-page health copy going forward.

## Deploy reminder
Work on `main`; commit + `git push` after each build (= auto-deploy). After page set: `npx astro build`
→ `python3 scripts/final_page_audit.py --birds` → `python3 scripts/generate_sitemaps.py` → deploy-verify.

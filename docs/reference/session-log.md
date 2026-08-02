# C.A.Gs Session Log and Known Issues

> Moved out of `CLAUDE.md` on 2026-08-02 (Phase 4 of the self-improving quality loop).
> The content below is **verbatim** — nothing was rewritten on the way out, because a
> registry that gets paraphrased during a move is a registry nobody can trust afterwards.
> `CLAUDE.md` now routes here instead of carrying it. History and open defects. Nothing here is a rule; it is state.

## Active Session — Homepage REBUILD v2 (2026-05-29 PM)
- v1 build used OLD/inline components + skipped the SEO checklist → full section-by-section rebuild.
- **LOCKED:** Hero B Authority Green · `cag-toc-v3:02` Grouped-by-part · `cag-key-takeaway-v2:02` Stat-forward grid ·
  Compare Table Style E (1100px) · new Mark & Teri owner card · new counter snippet
  (12+ Yrs aviary / 100% CITES / $1,500 Floor price / 24h) · new filterable BirdCard.
- **Content contract:** "C.A.Gs" / "C.A.Gs – Midland, TX" brand voice (never "congoafricangreys.com") ·
  ALL of H1–H6 used · every header conversational/Quora-style (What/How/Is/Can) · EBP framework per paragraph ·
  internal+external links anchored at sentence START — Link-First rule (never mid-sentence or end) · PAA-only FAQs · `assets/brand/` shipping photos ·
  CITES Appendix I + captive-bred-USA · 8–15 top states/cities in shipping.
- **MANDATORY:** `MANUAL SEO CHECKLIST-HOMEPAGE.md` + `skills/cag-seo-master-checklist.md` — not optional.
- **AEO/GEO gate runs ON the page:** keyword-verifier → meta-description → trust-signals.
- Desktop renders new desktop components; mobile/tablet renders new mobile components.
- Governance docs reconciled to v2 (2026-05-29): `components.md`, `component-page-matrix.md`, `component-themes.md`
  now register the new bundles and route the homepage to them.
- Status: **DONE and LIVE** (2026-06-01). Homepage fully built + deployed — `src/pages/index.astro` (989 lines), 24 H2 sections live. Per "Always commit + push after build", all work committed + pushed.
- **Progress: COMPLETE.** All sections built, approved, and live. (The earlier "RESUME AT SECTION 9" note is superseded — homepage was finished after 2026-05-29.)
- Added `--color-panel/line/mid/forest` to `global.css` (fixed undefined cag-library tokens site-wide) + Rule 28b (Two-Keyword Headers) to the SEO checklist.
- **Continuation handoff:** `sessions/2026-05-29-homepage-build-progress.md` (read first next session; do NOT re-run grill-me).
- Session brief: `sessions/2026-05-29-session-brief.md` (see "REBUILD v2" section).
- **2026-06-05 addendum (a11y + non-commodity pass):** homepage a11y back to **100/100** (fixed the Direction-D lead-paragraph dark-on-dark trap + MobileTabBar contrast — see `cag-accessibility-fixer` A11y-7 + MEMORY `reference_contrast_lead_paragraph_trap`). Ran the **non-commodity pass** (audit-all → rewrite-only-weak; homepage was ~90% already strong) — added Teri's First-30-Days voice, **Maxy** (talking Congo in the video), per-bird **ItemList Product/Offer schema**, and newly-confirmed **psittacosis + UV-B/D3** entities. **Verified-Claim Ledger expanded** (psittacosis, UV-B/D3, Maxy → ✅) in `cag-entity-incorporation-agent.md` + `sessions/2026-06-03-homepage-entity-map.md`. External-link skill+agent now warn that **cites.org 403s to curl = bot-block, not dead**. Details: `sessions/2026-06-05-homepage-noncommodity-pass.md`.

## Active Session — Interior-Pages Batch (2026-06-06 → 2026-06-11) — COMPLETE ✓
- **All 18 interior pages rebuilt to the Interior-Page Standard and LIVE** (plan: `docs/superpowers/plans/2026-06-06-interior-pages-full-seo.md`; brief: `sessions/2026-06-06-interior-batch-brief.md`).
  - **Cluster A (Care/Health, 6):** care-guide pillar · african-grey-care hub · diet · best-food · lifespan · african-grey-parrot-health-guarantee
  - **Cluster B (Trust/Authority, 5):** trusted-african-grey-parrot-breeders (= the About Us page, AboutPage schema) · african-grey-reviews (5 fabricated testimonials + fake reviewCount:47 removed) · captive-bred · cites-african-grey-documentation · scams (`yr is not defined` bug fixed)
  - **Cluster C (Guides, 4):** african-grey-parrot-guide (species pillar) · african-grey-parrot-faq (25-Q QAB pillar) · how-to-tame (HowTo schema, 7 steps) · african-grey-adoption (honest breeder-not-rescue frame; legacy `/african-grey-for-adoption/` 301 live)
  - **Cluster D (1):** african-grey-parrot-price (AggregateOffer + 6 per-bird Offers; every figure traced to price-matrix/financial-entities)
  - **Cluster E (2):** contact-us (ContactPage schema + GA4 `generate_lead` inline) · privacy-policy (shell only, legal text verbatim)
- Finalize done: sitemaps regenerated (100 URLs, 0 phantoms), health sweep PASS, all 18 slugs live-verified 200, IndexNow submission accepted (200).
- **Open Flags RESOLVED by breeder (2026-06-11):** ① pellet endorsement = the 3–5 reviewed brands (Harrison's / Roudybush / TOP's / Zupreem Natural), no single house brand · ② AggregateRating **reviewCount = 52 (real)** — corrected from 127 site-wide (homepage ×3, reviews, trusted-breeders); rating 4.9 unchanged · ③ privacy-policy "Zelle or Cash App" removed → neutral "payment method confirmed during reservation" wording.

## Known Issues
- Homepage Video section: using a YouTube **placeholder** (embed + VideoObject schema scaffold) — breeder to supply the real URL later.
- Homepage `.mov` clip not browser-usable (ffmpeg/cwebp not installed to convert → mp4).
- GSC not connected → `docs/reference/top-pages.md` has no live clicks/impressions/LLM Visibility yet.
- MFS deploy may be broken — the shared "MFS Dashboard" GitHub PAT was deleted during CAG token rotation (2026-06-01). Run `git push --dry-run` in the MFS repo before next MFS work; it needs its own token. (CAG uses the new "CAGs-Website Workflow" PAT in keychain; remote is tokenless.)
- `/dna-tested-african-grey-for-sale/` fails Core Web Vitals **CLS at ~0.44 on roughly 4-in-5 cold mobile loads** (bimodal: 0.44 or 0.001, on a race). **Pre-existing** — the pre-session build shows an identical distribution, so it is not from the 2026-07-26 cluster work. Shifting node is `main.dnat > header.hero > div.hero-grid > div.hero-copy`; four hypotheses are already ruled out by measurement. Full record in `docs/reference/technical-seo-fixes-backlog.md`. **Because the metric is bimodal, any retry MUST be judged on ≥5 runs** — a single pass or fail means nothing and already caused one misattribution. Leading suspect is the async Google Fonts race, so re-measure after self-hosting lands.
- Sitewide body duplication — ~5,857 crossovers ≥12 words across the ~100 location pages (shared credential/shipping prose). The 6 for-sale pages are clean; this is a separate piece of work. Check with `python3 scripts/dup_content_audit.py` (no args = sitewide).

# Session Brief — Direction D 18-Page Final Polish (2026-06-13)

Scope: TOC standardization, component/section polish, mobile fixes (scam page), form
endpoint unification, contrast/badges, images, perf, + analysis (buttons, infographics,
duplicate content). Skills: /impeccable (brand context loaded), /frontend-design.

## DONE & build-verified (dist/ ✓, not yet committed)
- **Form endpoints unified → `formspree.io/f/xrejpnvn`**: scam page ×3 (nl-mid + 2 forms),
  orphan `cag-newsletter-v2.astro`. (Removed `xpqoeazq` ×3 + `f/placeholder` ×1.)
- **Footer/seam logo perf**: generated `public/cag-footer-logo.webp` (24KB PNG → 10KB WebP,
  −59%); swapped `.png`→`.webp` across 18 files (Footer.astro + index + 16 interior pages).
  Kills the Lighthouse "modern format" penalty on every page that uses the seam.

## KEY FINDINGS (evidence-based, via live chrome-devtools measurement)
- **TOC "too big" — does NOT reproduce on 16 interior pages.** Live measurement: homepage
  `TocV3` AND health-guarantee TOC render **identically** — heading 24px Newsreader, item
  text 15px, eyebrow 12px, group title 18px. All 16 interior pages already use the homepage
  scale in source (standardized in commit a5b7d80, live). **No work needed on those 16.**
  → The genuine TOC outlier is the **scam page** only: bespoke `.toc-box` "Table of Contents"
    (heading 16px, items 13.5px) — needs replacing with the `TocV3` grouped-card pattern.
- **"Black text on green" contrast = the Direction-D `h2 + p {color:--ink}` trap** (per memory
  `reference_contrast_lead_paragraph_trap`). On scam `.form-header-green`, the `<h2>` is white
  (OK) but the subtext `<p>` inherits `--ink` `#20342b` → dark-on-green, near-invisible.
  Confirmed by screenshot + computed `pColor: rgb(32,52,43)`. The OTHER 17 forms use the shared
  AA-safe `InquiryForm` (cream bg, `#1c1a18` text) — they do NOT have this bug.
- **Newsletter broken on mobile**: scam `.nl-mid-form` email input collapses (`width:0` measured)
  / side-by-side input+button doesn't stack at narrow widths. Copy itself is fine.
- **Forms inventory**: 17/18 pages already use shared `cag-inquiry-form.astro` (xrejpnvn,
  AA-safe, full services). Only the **scam page** has bespoke forms.

## OPEN FLAGS / DECISIONS
- **Q1 (asked 2026-06-13): Scam-page contact form approach.**
  Recommended = swap both bespoke `.cag-form` blocks → shared `InquiryForm`, parameterized with
  optional `heading`/`subtext`/`subject` props so scam framing ("Is This Listing Legitimate?")
  is preserved. Gives consistency + AA + full products/services + xrejpnvn. Trade-off: longer
  adoption-style form on a "vet a listing" page; mitigated by keeping scam copy + message field.
  Alt = surgical fix-in-place (override the h2+p color, fix badges, enrich variant options).

## REMAINING (tracked in TaskList #3–#11)
- #3 scam TOC → TocV3 pattern (other 16 already done)
- #4 scam form (blocked on Q1) · #5 newsletter stack · #6 "92%"+"Type 5" infographics mobile
- #7 how-to-tame image crop · #8 diet image desktop crop · #9 best-food pellet-table AA contrast
- #10 duplicate-content audit (deliverable) · #11 button + AI/infographic opportunities (gated proposal)

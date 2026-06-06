---
name: cag-footer-agent
description: CAG footer specification + audit rules. Source of truth is src/components/Footer.astro (Forest Green, 5-column). Use when building or auditing any page footer, or checking footer completeness.
tools: [Read, Write, Bash]
---

# CAG Footer Agent Skill
## Footer Specification & Audit Rules for CongoAfricanGreys.com
**Version 2.0 — Astro / Cloudflare Pages (rewritten 2026-06-01; v1 was a stale MFS WordPress copy with an orange footer + dog nav)**

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the task genuinely cannot be done with Claude Code alone.

---

## SOURCE OF TRUTH

The footer is a single Astro component rendered on every page:

- **Component:** `src/components/Footer.astro`
- **Architecture:** Astro (NOT WordPress/Astra static HTML). There is **no** `rebuild_footer.py` —
  edit the component once and every page updates on build.
- **Standardization agent:** `cag-footer-standardizer` detects pages with outdated markup and
  aligns them to this component.

> ⚠️ v1 of this skill described an orange (`#FF8C00`) MFS footer, a dog "Available Puppies" nav
> column, a `/Users/apple/Downloads/MFS/rebuild_footer.py` script, and a `(531) 368-0538` phone.
> All were stale/wrong. Never reintroduce them.

---

## DESIGN (per `docs/design.md` — Terracotta Warmth)

| Element | Value |
|---|---|
| Footer background | **Forest Green `#2D6A4F`** (`bg-green`) — never orange |
| Text | White / white-at-opacity on green |
| CTA button | **Clay `#e8604c`** pill (`bg-clay`, `rounded-full`) — brand signature |
| Bottom bar | `bg-green/90`, white/10 top border |
| Headings | Lora 700 · Body/links | Sora 400–600 |
| Bird icon | custom `/emoji/cag-congo.png` — **never 🦜** |

---

## 5-COLUMN STRUCTURE (required content)

Every footer must contain these 5 columns. Flag any footer missing 2+ columns as
`INCOMPLETE — needs footer rebuild`.

```
Column 1: Quick Links
  - Available Birds → /available/
  - Congo African Grey → /congo-african-grey-for-sale/
  - Timneh African Grey → /timneh-african-grey-for-sale/
  - Pricing → /african-grey-price-cost/
  - Contact → /contact/

Column 2: Resources
  - Species Guide → /african-grey-species-guide/
  - Care Guide → /african-grey-care-guide/
  - CITES Info → /cites-captive-bred-documentation/
  - FAQ → /african-grey-species-guide/#faq
  - Blog → /blog/

Column 3: Company
  - About Us → /about/
  - Our Birds → /available/
  - Testimonials → /testimonials/
  - Contact → /contact/

Column 4: Legal
  - Privacy Policy → /privacy-policy/
  - Terms of Service → /terms/
  - Health Guarantee Terms → /health-guarantee/
  - Shipping Policy → /shipping-delivery/
  - Refund Policy → /refund-policy/

Column 5: Contact
  - Phone: +1-281-545-3169   (master NAP — docs/reference/credentials.md)
  - Email: [INQUIRIES_EMAIL_TBD]
  - Address: [BREEDER_LOCATION_TBD — city-level only; see privacy rule]
  - Hours: Open 24/7
  - Social: Facebook, Instagram, TikTok, YouTube

Bottom Bar:
  - Copyright © CongoAfricanGreys.com [year]
  - USDA AWA Licensed (include license number once confirmed)
  - CITES Appendix I captive-bred documentation available
```

> **NAP consistency:** Name / Address / Phone must match `docs/reference/credentials.md`
> exactly (the `cag-nap-citation-agent` audits this). Phone is **+1-281-545-3169**.
> Per the site privacy rule, the footer uses **city-level** location only — never a street address.

---

## RESPONSIVE

| Breakpoint | Layout |
|---|---|
| ≥ 861px | multi-column grid |
| 521–860px | 2-column, brand col full width |
| ≤ 520px | single column |

---

## AUDIT MODE

When auditing footers across pages:
1. Confirm the page renders `Footer.astro` (not legacy WordPress/Astra `site-footer` markup).
2. Confirm all 5 columns are present (flag `INCOMPLETE` if 2+ missing).
3. Confirm Forest Green background + Clay CTA (no orange).
4. Confirm phone = `+1-281-545-3169`, CITES line says **Appendix I**, copyright year current.
5. Confirm no dog terms (Available Puppies / Non-Shedding / Toy / Mini) and no 🦜.

---

## WHAT NOT TO TOUCH
- Schema JSON-LD blocks (footer changes never alter page schema).
- Content above the footer component.

---

## REFERENCE
- **Component:** `src/components/Footer.astro` (source of truth)
- **Design spec:** `docs/design.md` · **Width:** `docs/reference/page-width.md`
- **NAP master:** `docs/reference/credentials.md`
- **Standardizer:** `cag-footer-standardizer` agent

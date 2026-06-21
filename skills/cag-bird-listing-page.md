---
name: cag-bird-listing-page
description: Use when building, rebuilding, or retiring an individual African Grey *bird* listing page at /available/<slug>/ — one page per real bird in clutch-inventory.json. Not for variant, location, comparison, or for-sale cluster pages (they have their own builders).
---

# CAG Individual Bird Listing Page

> **Deep standard (22-section, ~3,150w) → use `skills/cag-bird-page-build.md`. This lean profile remains for minimal one-bird listings.**

## Overview
One indexable page per real, available bird. Job = **convert**, not educate. All CLAUDE.md
Non-Negotiables already apply (first-person voice, shipping line, CITES framing, no visible date,
Verified-Claim Ledger, price-from-data). This skill covers ONLY the 6 things a bird page gets wrong
without guidance — a RED baseline (`sessions/2026-06-18-bird-listing-baseline.md`) proved CLAUDE.md
handles the rest. Do not restate CLAUDE.md rules here.

## When to use
A bird in `data/clutch-inventory.json` is `available`/`reserved`/`pending_weaning` but has no page on
disk. NOT for variant, location, comparison/for-sale, or blog pages — they have their own builders.

## The 6 rules
1. **Fixed section order** (keeps 9+ pages a consistent cluster): Breadcrumb → Hero/Bird-Vitals
   (+inquiry CTA) → About <Bird> (archetype) → Health & Documentation → Why <Bird> → Pricing & What's
   Included → Parent Birds → FAQ → Other Available Birds → Inquiry CTA.
2. **Single `Offer`, never `AggregateOffer`** (that's the variant page). One `Product` + one `Offer`;
   availability `InStock` / `PreOrder` (pending_weaning) / `SoldOut`.
3. **Link out, don't re-teach.** Species facts (lifespan, intelligence, visual-sexing, CITES history) =
   one clause + link to the evergreen page (`/african-grey-parrot-guide/`,
   `/african-grey-parrot-health-guarantee/`, `/cites-african-grey-documentation/`). Body stays
   bird-specific — stops 9 ephemeral pages becoming thin/duplicate content.
4. **Sell-and-retire lifecycle.** On `sold`: never leave the Offer InStock — render a Sold state OR 301
   to the variant page via cag-redirect-manager, then regenerate sitemaps. Decided per bird with
   cag-clutch-manager.
5. **Real image or defined placeholder** under `/<slug>` — never invent a filename that 404s.
6. **Health claims = ledger only.** Allowed: DNA sex cert, avian-vet health cert, CITES/captive-bred
   docs, hatch cert + band, weaning status, USDA AWA, **PBFD + Avian Polyomavirus PCR screening**
   (per-bird testing + records confirmed by breeder 2026-06-20 — now in the Verified-Claim Ledger).
   Still off-limits: any test result or condition NOT in the ledger — omit it.

## Per-page differentiation (added 2026-06-21 — do not clone a sibling bird verbatim)
- **Unique headers per bird.** Never copy another bird's H2 set wholesale — duplicate H2s across
  `/available/` pages read as duplicate content. Use hybrid question+entity headers (rotate
  What/Why/How/Can/Do/Does/When/Is stems), entity clause only where it earns a 2nd query. Keyword+entity
  in title/meta = reinforcement. See memory `feedback_hybrid_header_seo`.
- **Gallery = homepage BirdCard proportions:** tile wrapper `h-72` (NOT `aspect-[4/5]`),
  `img class="w-full h-full object-cover"`, tuned per-image `object-position:center NN%` so the bird is
  framed. Use 5 **visually distinct** photos (watch for near-duplicate burst shots in `assets/brand/<BIRD>`).
- **Documentation image** is full-width: `class="w-full ... bg-white"` + `object-fit:contain` (never the
  `max-h-[170px]` cap — that shrinks it). Point it at the "WHAT COMES WITH <BIRD>?" infographic.
- **Shipping image must be FIRST in source order** inside `#shipping`'s `[1fr_260px]` grid (+ `md:col-start-2
  md:row-start-1`; text gets `md:col-start-1 md:row-start-1`). Classes alone don't fix mobile — the div must
  physically be first or the image faces the map on mobile. See memory `feedback_bird_page_visual_fix_patterns`.
- **Geo links:** distinct 4–5 state/city set per bird (real slugs only), never the same trio everywhere.
  See memory `feedback_bird_page_geo_diversification`.
- **DNA sex label** must match the bird's sex — porting from a male template leaves "(male confirmed)" on a
  female page (caught on Amie + Bery 2026-06-21). Always verify in preview, never source-grep alone
  ("female" contains the substring "male").

## Specs
700–1,000 visible words, bird-specific. Data: `clutch-inventory.json` (facts + notes→archetype),
`bird-inventory.json` (parents, required trust signals), `financial-entities.json` (delivery tiers,
deposit), `price-matrix.json` (price). Archetype (CLEO/REX/NOVA/SAGE/IRIS) via cag-bird-personality.

## Common mistakes
AggregateOffer on one bird · re-teaching species facts · inventing an image path ·
leaving a sold bird InStock · adding city/state targeting (cannibalizes location pages).

---
name: cag-bird-listing-page
description: Use when building, rebuilding, or retiring an individual African Grey *bird* listing page at /available/<slug>/ — one page per real bird in clutch-inventory.json. Not for variant, location, comparison, or for-sale cluster pages (they have their own builders).
---

# CAG Individual Bird Listing Page

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
   docs, hatch cert + band, weaning status, USDA AWA. **Do NOT assert PBFD or Avian Polyomavirus**
   (or any test result) — not in the ledger as of 2026-06-18; omit it.

## Specs
700–1,000 visible words, bird-specific. Data: `clutch-inventory.json` (facts + notes→archetype),
`bird-inventory.json` (parents, required trust signals), `financial-entities.json` (delivery tiers,
deposit), `price-matrix.json` (price). Archetype (CLEO/REX/NOVA/SAGE/IRIS) via cag-bird-personality.

## Common mistakes
AggregateOffer on one bird · re-teaching species facts · inventing an image path · asserting
PBFD/Polyomavirus · leaving a sold bird InStock · adding city/state targeting (cannibalizes location pages).

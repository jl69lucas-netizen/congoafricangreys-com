# CongoAfricanGreys.com — Project Context

**Usage:** Start any new session with: `Read docs/reference/project-context.md, then: [your task]`

---

## Brand Identity

- **Site:** CongoAfricanGreys.com
- **Business:** African Grey parrot breeder (captive-bred, CITES-compliant)
- **Mission:** Ethical, health-documented African Grey breeding — trust and transparency over volume
- **Voice:** Expert, warm, reassuring — serious bird owners, not impulse buyers
- **Legal requirement:** All birds CITES Appendix II captive-bred with documentation

## Family & Aviary Story

- **Owners:** Mark & Teri Benjamin (husband and wife)
- **Children:** Son James Benjamin, Daughter Allyson Benjamin (both involved in the aviary)
- **Location:** Midland, Texas (home aviary — not a commercial facility)
- **Founded:** 2014 (12 years of captive African Grey breeding as of 2026)
- **USDA AWA licensed**
- **H-S-S Hook:** "We didn't plan to become America's most trusted African Grey breeder — it started with one pair in our backyard in Midland, Texas in 2014."
- **Positioning:** America's Family African Grey Aviary — ethical, documented, Texas-based
- **Tagline candidates:**
  1. "Raised with Family. Proven with Trust."
  2. "12 Years. One Mission. Your Perfect African Grey."
  3. "From Our Family Aviary to Your Home."

## Products & Pricing

Source of truth: `data/price-matrix.json` and `data/bird-inventory.json`

| Product | Price | Notes |
|---------|-------|-------|
| African Grey Chick / Baby (3–6 months) | $3,000 | Main product — hand-raised, weaned |
| African Grey Adult Bird | $1,500 | Tame, established personality |
| Congo African Grey (range) | $1,500–$3,000 | By age/training level |
| Timneh African Grey (TAG) | $1,200–$2,500 | Smaller, calmer, earlier talker |
| Congo African Grey Pair | $2,700 | Bonded Congo pair |
| African Grey Breeding Pair | $3,500 | Proven bonded pair, DNA-certified |
| African Grey Fertile Egg | $40 | For experienced breeders only |
| **Deposit** | $200 | Holds a bird |

### Named Available Birds (as of 2026-05-10)
| Name | Sex | Price |
|------|-----|-------|
| Bery | Female | $1,600 |
| Joys | Female | $2,200 |
| Amie | Female | $2,700 |
| Loti | Male | $1,800 |
| Carl | Male | $2,500 |
| Roys | Male | $2,000 |

Trust signals required on every listing: USDA AWA license, CITES captive-bred docs, avian vet cert, DNA sexing cert, weaning status, hatch certificate + band number.

## Tech Stack

- **Platform:** WordPress + WooCommerce (products as WooCommerce listings)
- **Site content:** `site/content/` — 81 markdown exports from CAG.zip
- **Static HTML archive:** `archive/simply-static-1-1775169284.zip` (full export for reference)
- **Hosting/deploy:** TBD — Phase 2
- **Reference project:** `/Users/apple/Downloads/MFS/` (MaltipoosForsale.com — same playbook)

## Agent System — Phase 1 (3 Agents)

- **`@cag-competitor-registry`** — discovers + registers 30 competitors into `data/competitors.json`; run first
- **`@cag-competitor-intel`** — deep 10-metric analysis; single competitor or `--all` mode
- **`@cag-rank-tracker`** — weekly monitoring (Sundays); tracks competitor changes + CAG rankings

Phase 2 will add ~44 agents + 30 skills, adapted from MFS.

## 4 Non-Negotiable Rules

1. **Preview Gate** — Any page redesign MUST be previewed before writing to site files
2. **Confidence Gate** — ≥97% confidence before writing any site file. If below 97%: stop, state uncertainty, ask
3. **Same Content** — Redesigns never add or remove content. Visual layer only
4. **CITES Awareness** — Never publish content implying illegal trade. All birds captive-bred

## Current GSC Performance (as of 2026-04-28)

### Top Queries by Clicks
| Query | Clicks | Impressions | CTR | Position |
|-------|--------|-------------|-----|----------|
| african grey congo for sale | 46 | 392 | 11.73% | 16.2 |
| congo african grey for sale | 38 | 611 | 6.22% | 16.5 |
| african grey parrot for sale | 12 | 783 | 1.53% | 73.7 |
| congo african grey parrot for sale | 11 | 238 | 4.62% | 23.0 |
| breeding pair of african greys for sale | 10 | 171 | 5.85% | 10.3 |
| african grey breeding pair for sale | 7 | 157 | 4.46% | 8.1 |

### Top Pages by Clicks
| Page | Clicks | Impressions | CTR | Position |
|------|--------|-------------|-----|----------|
| / (homepage) | 28 | 14,915 | 1.88% | 45.6 |
| /product/african-grey-parrots-for-sale-near-me/ | 53 | 713 | 7.43% | 41.8 |
| /product/african-grey-parrot-for-sale-florida/ | 42 | 1,446 | 2.90% | 21.8 |
| /product/buy-intelligent-african-grey-for-sale-ca/ | 34 | 1,537 | 2.21% | 14.0 |
| /product/african-grey-breeding-pair-for-sale-nearby/ | 22 | 657 | 3.35% | 10.1 |
| /buy-african-grey-parrots-with-shipping/ | 18 | 763 | 2.36% | 15.4 |
| /male-vs-female-african-grey-parrots-for-sale/ | 13 | 1,788 | 0.73% | 21.2 |

**Key insight:** Massive impression volume (14,915 on homepage) with very low CTR (1.88%) = title/meta optimization is the #1 quick win. Breeding pair queries rank well (pos 8–10) but need dedicated pages.

## Key Data Files

| File | Purpose |
|------|---------|
| `data/competitors.json` | 30-competitor registry — source of truth |
| `data/analytics/` | GSC performance HTML reports (2026-04-28) |
| `data/keywords/` | Keyword clusters (Phase 2) |
| `data/rankings/` | Weekly rank snapshots (Phase 2) |
| `docs/reference/top-pages.md` | Traffic baseline (populate after GSC API connected) |
| `docs/reference/domain-knowledge.md` | Variants, trust signals, health conditions, PAA questions |
| `docs/research/` | Competitor reports + gap matrix outputs |
| `site/content/` | 81 markdown page exports — directly editable |

## Session Token Hygiene

- Start every session: `Read docs/reference/project-context.md, then: [task]`
- Never re-explain brand, pricing, or rules in chat — they're here
- After long sessions (>60% context): commit work, start fresh session
- Reference specific files explicitly rather than asking Claude to search

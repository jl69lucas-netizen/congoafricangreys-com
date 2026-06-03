# Internal Link Audit — Homepage
Date: 2026-06-03 · Scope: `src/pages/index.astro` (deployed homepage) vs 97-page inventory

## Verdict on the flagged example
The **Compare Variants** section ("Is a Congo or a Timneh African Grey Right for You?") does **not** link to the dedicated comparison page `/congo-vs-timneh-african-grey/`. That page exists and receives **0 inbound links from the homepage**. **Not linking is a real SEO gap (bad practice / missed opportunity); adding a contextual link is good practice** — see reasoning below.

## Why linking is GOOD here (not keyword stuffing)
1. **Link equity** — the homepage is the site's highest-authority page; a contextual link passes that authority to the comparison spoke, helping it rank for "congo vs timneh."
2. **Crawl + discovery** — a near-orphan page (0 homepage inbound links) is harder for Google to find and value.
3. **Topical relevance** — a descriptive anchor ("Congo vs Timneh African Grey comparison") reinforces the spoke's target keyword.
4. **User journey** — the homepage section is a *teaser*; the dedicated page is the *deep-dive*. The link serves high-intent users, not just bots.
5. **Hub-and-spoke / silo** — a money/teaser section funneling to its spoke is exactly the architecture we want.

## When it would be BAD (the trade-offs to respect)
- **Exact-match anchor repeated** across 20 links → over-optimization signal. Use varied, natural anchors.
- **Link parked at end of sentence** → violates CAG anchor-position rule (beginning/middle only).
- **Over-linking** a section → the skill caps ~2–3 new links per section.
- **Cannibalization** — fine here: the Compare section's existing "Inquire about a Congo/Timneh" CTAs serve *transactional* intent; the comparison-page link serves *informational/decision* intent. Complementary, not competing.

## Homepage internal-link gaps (priority)
Homepage currently links out to **31 / 97** pages.

| # | Target page (currently unlinked) | Priority | Best source section | Suggested anchor (mid-sentence) |
|---|---|---|---|---|
| 1 | `/congo-vs-timneh-african-grey/` | **3** | Compare Variants | "our full Congo vs Timneh African Grey comparison" |
| 2 | `/african-grey-vs-macaw/` | 2 | "vs Macaw/Cockatoo/Amazon" section (links only to hub now) | "African Grey vs Macaw comparison" |
| 3 | `/african-grey-vs-cockatoo/` | 2 | same section | "African Grey vs Cockatoo comparison" |
| 4 | `/african-grey-vs-amazon-parrot/` | 2 | same section | "African Grey vs Amazon comparison" |
| 5 | `/african-grey-parrot-lifespan/` | 2 | FAQ "how long do they live" / species | "African Grey lifespan" |
| 6 | `/congo-african-grey-parrot-pair-for-sale/` | 2 | Congo section / eggs-pairs (Jins+Jeni) | "bonded Congo African Grey pair" |
| 7 | `/african-grey-parrot-breeders-comparison/` | 1 | Why-us / scam section | "how we compare to other African Grey breeders" |
| 8 | `/blog/african-grey-parrot-talking-ability/` | 1 | Video / "do they talk" FAQ | "African Grey talking ability" |

## Flags (resolve, don't auto-link)
- Possible duplicate/legacy slugs: `/african-grey-care/` vs the linked `/african-grey-parrot-care-guide/`; `/african-grey-adoption/` vs `/african-grey-parrot-adoption-cost/`. Check for cannibalization before linking (may warrant a 301 instead).

## Recommended implementation
Add links #1–#6 (descriptive, mid-sentence, ≤2 per section), skip the duplicate-slug pages pending a cannibalization check. Then save the well/bad learnings to the internal-link skill + entity-incorporation agent.

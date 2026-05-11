# SEO Rules — ALWAYS Follow

## Critical: Never Break These

| Rule | Detail |
|------|--------|
| **H1 text** | NEVER change without explicit user approval |
| **Canonical href** | MUST be absolute: `https://congoafricangreys.com/slug/` |
| **Schema JSON-LD** | NEVER remove or modify — preserve verbatim |
| **og:url / og:image / canonical** | MUST be absolute, never relative |
| **CITES language** | NEVER imply birds are wild-caught. Always: "captive-bred" |

## Keyword Strategy

- **Primary transactional:** "african grey parrot for sale [state]" — H1, title, slug
- **Primary brand:** "congo african grey for sale" — top CTR query (11.73% at pos 16)
- **Breeding niche:** "african grey breeding pair for sale" — ranks pos 8–10, needs dedicated pages
- **Informational:** male vs female, diet/food, care — drives impressions, needs CTR optimization
- **Full keyword data:** `data/analytics/Queries.html`

## Quick Wins Identified (2026-04-28 GSC)

1. **Homepage meta** — 14,915 impressions at 1.88% CTR → title/description optimization
2. **Breeding pair pages** — ranking pos 8–10 but no standalone hub page
3. **Male vs female page** — 1,788 impressions at 0.73% CTR → meta needs work
4. **Florida product page** — 1,446 impressions at 2.90%, pos 21.8 → push to page 1

## Images

- All images reference `/wp-content/uploads/` paths
- NEVER use base64 data URIs for images
- Always use real `src="/wp-content/uploads/filename.jpg"`

## Sitemaps

- All `<loc>` tags must be absolute: `https://congoafricangreys.com/...`
- Exclude: attachment pages, thank-you pages, admin pages

## After Any Deploy

1. Submit changed URLs to IndexNow (credentials TBD — Phase 2)
2. Check GSC for crawl errors within 24 hours
3. Update `docs/reference/top-pages.md` after GSC data refreshes

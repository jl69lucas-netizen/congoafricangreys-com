# Homepage Asset Map — Session 2026-05-28

> **Scope:** Visual / asset layer only (OG photo → homepage section mapping + card sizing).
> **NOT done yet:** the homepage SEO content build. That is a separate pass — run `grill-me` → `@cag-content-audit-agent` next, using this file as input context.
> **Publish status:** NOT published. Local preview only (`npm run dev` → localhost:4321). Nothing committed or pushed.

## Files touched
- `src/pages/index.astro` — new sections + per-bird images + testimonial/variant images
- `src/components/BirdCard.astro` — added `image` + `variant` props; image height 208px → **256px**, crop `object-top` (was cutting bird heads on desktop)
- `public/*.webp` — OG photos copied in with SEO filenames (see map)
- `docs/reference/higgsfield-image-manifest.md` — AI hero placeholder spec (pending credit)

## Image → Section map (all from `assets/brand/`)

| Homepage section | public/ file | Source OG photo | CITES setting |
|---|---|---|---|
| Hero (PLACEHOLDER — keeps existing) | hero-desktop.webp / hero-mobile.webp | — (AI hero pending Higgsfield credit) | — |
| Bird card — Roys (Congo ♂ 4mo, $2,300) | roys-congo-african-grey-male-4-months.webp | ROYS- African Congo Grey Parrot - male 4 months | home |
| Bird card — Amie (Congo ♀ 3mo, $2,500) | amie-congo-african-grey-female-3-months.webp | AMIE -congo african grey bird female -3 months | home |
| Bird card — Bery (Congo ♀ 1yr, $1,700) | bery-congo-african-grey-female-1-year.webp | BERY -1 year female african grey parrot | home |
| Bird card — Jins+Jeni (Congo pair, $3,500) | jins-jeni-congo-african-grey-pair.webp | jins-jeni-...bonded-birds (KISSING pair) | home |
| Bird card — Elad (Timneh ♂ 5mo) | elad-timneh-african-grey-male-5-months.webp | ELAD - Timneh african grey for sale - male 5 months | home |
| Bird card — Evie (Timneh ♀ 6mo) | evie-timneh-african-grey-female-6-months.webp | EVIE- Timneh African Grey parrot female 6 months | home |
| Variant card — Congo | congo-african-grey-variant.webp | jins-jeni-...talking-birds (eating pair) | home |
| Variant card — Timneh | timneh-african-grey-variant.webp | (timneh variant) | home |
| About band (Hand-Raised) | hand-fed-african-grey-baby-breeder.webp | about-the-breeder hand-feeding | home |
| **Products: Congo Breeding Pair** ($3,000, Inquire CTA) | congo-african-grey-breeding-pair-aviary.webp | african-grey-breeding-pair-for-sale | aviary |
| **Products: Timneh Breeding Pair** ($3,000, Inquire CTA) | timneh-african-grey-breeding-pair.webp | Timneh Greys-PAIR (breeder holding) | home aviary |
| **Products: Fertile Eggs** ($95/egg, buy 5 free ship, Inquire CTA) | african-grey-candled-eggs.webp | Candled African Grey ... eggs | nest box |
| Breeding-section story lead (no CTA) | african-grey-eggs-ready-to-hatch.webp | Healthy ... eggs ready to hatch (hen+chick) | nest box |
| Talking video (click-to-play) | talking-african-grey-parrot-video.mp4 | (mp4) | home |
| Shipping band | african-grey-parrot-iata-shipping-crates.webp | live-animal shipping | crate |
| Testimonials ×3 | african-grey-review-1/2/3.webp | Review-top / Review-middle / health-review | home |

## Section order (current)
Hero → Trust bar → Birds Available (6 birds) → Variants → About (Hand-Raised) → **Breeding Pairs & Fertile Eggs (NEW — product cards w/ price + Inquire)** → Talking video → Shipping (+1100px process-flow infographic) → Why CAG → Testimonials → FAQ → Contact

## Full product range now on homepage
- 6 individual birds (Roys, Amie, Bery, Jins+Jeni pair, Elad, Evie)
- Congo Breeding Pair $3,000 · Timneh Breeding Pair $3,000
- Fertile Eggs $95/egg (buy 5 = free US shipping)
- Prices from `data/price-matrix.json` (NOT the stale $40 in business-DNA memory; live = $95)

## Resolved data flags
- $2,100 toy/figurine Jins+Jeni image — DELETED by breeder; homepage keeps real pair at **$3,500**.
- ELAD — confirmed **Timneh** by breeder.

## Still pending (placeholders, non-blocking)
1. **AI hero** — run Higgsfield JOB 1 (`soul_2`, ref `Male-and-Female-CONGO-African-Grey-Parrots.webp`) when credit available; overwrites hero-desktop/mobile.webp. No code change. Spec: `docs/reference/higgsfield-image-manifest.md`.
2. **`.mov` homepage video** — `main-homepage-video-...mov` not browser-reliable; ffmpeg/cwebp NOT installed to convert → .mp4. Only the talking `.mp4` is wired.

## Update 2026-05-29 — Card focal-point tweaks (from breeder screenshot)
All three approved + verified in local preview (DOM eval), NOT published.
1. **BirdCard.astro** — added optional `objectPos?: string` prop (default `'object-top'`); image class is now `object-cover ${objectPos}`. Lets each bird override the global crop.
2. **Roys card** — `objectPos: 'object-center'` (was dropping to bottom of card). Set in `src/pages/index.astro` birds array.
3. **Amie card** — `objectPos: 'object-center'` — full face visible, hand/fingers (trust point) kept in frame.
4. **Variants section** (`Two Variants. One Standard of Care.`) — both imgs raised `h-48`→`h-64` (192px→256px). Congo = `object-top` (shows heads); Timneh = `object-center` (shows legs). width/height attrs updated to 256.
- Verified: `npx astro build` OK (98 pages); DOM `objectPosition` + `clientHeight` confirm all four.
- Per-bird crop control now exists — to tune any future bird, just add `objectPos: 'object-...'` to its entry in the birds array.

## STILL local-only — publish checklist when ready
Nothing committed/pushed all session (breeder constraint: preview only). When the breeder approves going live:
`@cag-canonical-fixer` → `git add -A && git commit` → `git push` (push = deploy via GitHub Actions → Cloudflare Pages) → `@cag-deploy-verifier` → `sitemap-agent` skill.

## ▶ NEXT SESSION KICKOFF — Homepage SEO build
The visual/asset layer is DONE. The homepage SEO **content** build has NOT started. To begin:

1. **Read this file first** (it is the SESSION CONTEXT input).
2. Run the **`grill-me`** skill — it extracts SESSION CONTEXT (page = Homepage `/`, current sections per "Section order" above, GSC baseline below) before any build.
3. Hand that context to **`@cag-content-audit-agent`** with `PAGE_TYPE: Homepage`, `TARGET_URL: https://congoafricangreys.com/`, `TARGET_KEYWORD: African Grey Parrot Breeder`.
4. Then follow the master flow in CLAUDE.md → "I want to build a new page": audit → `@cag-content-architect` (it picks frameworks + routes to writer/faq/section-builder).
5. Gate before writing site files: **Confidence ≥97% + preview + approval** (CLAUDE.md non-negotiables). Visual layer must NOT change — content only.

**Baselines / inputs for the SEO build:**
- Homepage GSC: 28 clicks / 14,915 impressions / position 45.6 (highest-traffic page).
- Primary keyword: "African Grey Parrot Breeder" + multi-cluster — see `skills/cag-seo-master-checklist.md` (invoke that skill BEFORE building).
- Prices: source of truth `data/price-matrix.json` (egg $95, breeding pair $3,000, Jins+Jeni pair $3,500, deposit $200). Do NOT trust stale memory prices.
- Family/brand facts for EEAT: memory `project_business_dna.md` (Mark & Teri Benjamin, Midland TX, est. 2014, USDA AWA + CITES).

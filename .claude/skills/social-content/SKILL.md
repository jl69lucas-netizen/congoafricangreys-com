---
name: social-content
description: Writes platform-native social media content for CAG — Instagram captions, Facebook posts, TikTok/Reels hooks, Pinterest descriptions. Turns one source asset (talking-bird clip, chick photo, or a site page) into per-platform posts in the C.A.Gs first-person breeder voice. Reads content/social/ for drafts + data/price-matrix.json for pricing. Vocabulary for @cag-social-strategist.
tools: [Read, Write, Bash]
---

## Golden Rule
> **First-Person Brand Voice (ALWAYS):** Write as the breeder — "we / our / here at C.A.Gs." Our birds, credentials, and process are *ours*, not described from outside. Exception: encyclopedic species facts stay neutral.
> **CITES-safe (ALWAYS):** African Greys are CITES **Appendix I**, captive-bred in the USA, legal to own/transfer with documentation. NEVER imply wild-caught or illegal trade. NEVER use #citesappendix2.
> **Never fabricate:** prices come from data/price-matrix.json; availability from data/clutch-inventory.json; buyer stories from data/case-studies.json. No invented counts, no invented testimonials.
> Use Claude Code first; only reach for external tools when the task genuinely needs them.

---

## Purpose

Social content is NOT repurposed website copy — different voice, rhythm, and CTA. The research basis (docs/research/social-media-landscape-2026-06-06.md) is blunt: **breeders lose on social.** The category is owned by talking-bird personality accounts, rescue voices, and evergreen reference content. So CAG social rides the entertainment/education engine and converts attention to the website — it does NOT post "for sale" listings as primary content.

## Breeder Facts (source of truth — never contradict)
- **Breeders:** Mark & Teri Benjamin (family: James, Allyson). Brand voice name: **C.A.Gs**.
- **Location:** Midland, TX. (NOT Omaha.)
- **Credentials:** captive-bred USA, USDA AWA licensed, DNA-sexed (PCR), CITES **Appendix I**.
- **Variants:** Congo African Grey (CAG) · Timneh African Grey (TAG).
- **Pricing/shipping:** read data/price-matrix.json + data/financial-entities.json. Canonical card line: `Ships nationwide · $185 airport · $350 home`. Never hardcode a different number.
- **Bird icon:** never the generic 🦜 parrot emoji. In text-only contexts use `[CAG]`/`[TAG]`.

## Brand Entity Consistency (cross-profile — the only piece of "entity stacking" worth keeping)
The durable, white-hat kernel of entity stacking is consistency, NOT cross-link schemes or indexer pings. Make every real CAG profile describe the *same entity* so branded search + the knowledge graph associate them:
- **Same name everywhere:** match the NAP master in docs/reference/credentials.md — do not improvise a new brand-name variant per platform.
- **Same location:** Midland, TX. **Same canonical link:** the homepage or the relevant deep page — never a third-party "stack" link.
- **Same bio skeleton:** captive-bred USA · USDA AWA licensed · DNA-sexed · CITES Appendix I.
- **In scope for consistency:** Instagram, Facebook, Pinterest, TikTok (+ YouTube via @cag-video-seo-agent).
- **Explicitly OUT (research + trust reasons):** building X/Threads/LinkedIn/Tumblr profiles purely to "stack," Tumblr cross-linking to strengthen a stack, and any third-party indexer/ping service (e.g. Prime Indexer). These are footprint/trust risks for a breeder whose whole moat is being the *legitimate, documented* seller. Profile NAP consistency audits live with @cag-nap-citation-agent.

## On Startup — Read These First
1. Check content/social/ for existing drafts + the calendar.
2. Read data/price-matrix.json (pricing) + data/clutch-inventory.json (availability).
3. Ask: "What's the source asset (clip/photo/page)? Which platforms? Goal — engagement, traffic, or DMs?"

## Platform Specifications

### Instagram / Reels (HIGH priority)
- Caption 150–300 words (2,200 max). First line stops the scroll (before the "more" cutoff).
- Hashtags 20–30, mixed size/breed/lifestyle/location (see clusters below).
- CTA: "DM us AVAILABLE", "link in bio", or comment — DM CTA preferred (algorithm favors DM).
- Format: Hook → Story → CTA → Hashtags.
- Headwind: the loudest IG voices are anti-breeding/pro-rescue. Never argue rescue; out-document it (welfare, CITES paperwork, USDA AWA).

### Facebook (HIGH priority — buyer demographic skews 40–65+)
- 100–250 words (longer underperforms). Max 3 hashtags, at end only.
- Direct site link allowed. Format: Hook → Value → CTA → Link.
- Owner groups ban overt selling — post value/education there, not listings.

### TikTok / Reels (MEDIUM — top-of-funnel, repurpose only)
- 30–60s script. First 3 seconds deliver the payoff. Hook → 3 beats → CTA.
- On-screen text = key points only. CTA: "Follow for weekly parrot updates."
- Audience skews too young for a $1,500+ purchase — treat as brand reach + Reels reuse, not sales.

### Pinterest (MEDIUM-HIGH — evergreen Google traffic, zero breeder competition)
- Description 100–200 words, keyword-rich. Title = keyword + benefit.
- Boards: "African Grey Parrots", "Congo vs Timneh", "African Grey Care".
- CTA: link to the SPECIFIC page (care/comparison/price), not the homepage.

### X / Threads / Bluesky
- Skip. Not where African Grey buyers are (research-confirmed). At most auto-syndicate.

## Content Calendar Framework

| Post Type | Frequency | Platform | Goal |
|---|---|---|---|
| Available bird | as available | IG, FB | DMs + inquiries |
| Chick/fledgling milestone | weekly | IG, TikTok | engagement + follows |
| Health/CITES/trust education | 2×/month | all | authority + trust |
| Behind the scenes (Mark & Teri) | 2×/month | IG, FB | personal connection |
| Family/buyer story | monthly | all | social proof (from case-studies.json) |
| Congo vs Timneh comparison | monthly | Pinterest, FB | traffic |
| Anti-scam / "verify a real breeder" | 2×/month | all | trust + traffic (scam content ranks) |
| FAQ answer | 2×/month | all | traffic + AIO |

## Caption Tone Rules
1. Specific, not generic — "she climbs into your lap before you sit down" > "super loving".
2. Name the bird if named (use clutch-inventory.json); else "this little one" + variant.
3. Transparent pricing — include price in availability posts, never "DM for price".
4. Urgency without pressure — "2 chicks remaining" is honest; "BUY NOW" is desperation.
5. First-person — "Teri noticed this morning he's already mastered step-up…".

## Hashtag Clusters (copy-paste ready — corrected)

### Breed
`#africangrey #africangreyparrot #congoafricangrey #timnehafricangrey #africangreysofinstagram #greyparrot`

### Trust
`#captivebred #dnasexed #healthtestedparrots #ethicalbreeder #usdalicensed #citesappendixI`

### General parrot
`#parrotsofinstagram #parrotlove #talkingparrot #parrotlife #birdsofinstagram #parrotbreeder`

### Location (customize)
`#midlandtx #texasparrots #africangreytexas` (swap to the buyer-audience state/city)

## Output Format
```
# Social Content — [Platform] — [Topic]
Date: [YYYY-MM-DD]
Platform / Goal: [..]
## Caption
[..]
## Hashtags
[..]
## Notes
- Best time to post / image to pair / link target: /[slug]/
```

## Rules
1. Never reuse website copy verbatim.
2. Prices from data/price-matrix.json — no hardcoding.
3. DM CTA preferred on IG; direct link OK on FB/Pinterest.
4. Platform-specific format required — never one caption for all platforms.
5. No engagement bait ("comment an emoji if…") — it gets penalized.
6. Never 🦜; never imply wild-caught; never #citesappendix2.
7. Keep brand entity consistent across every profile (name/location/canonical link/bio); never build "stack" links or use indexer services.

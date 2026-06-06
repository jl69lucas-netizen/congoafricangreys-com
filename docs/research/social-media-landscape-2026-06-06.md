# Social Media Landscape Research — African Grey Niche

**Date:** 2026-06-06
**Method:** Firecrawl search across YouTube, Instagram, TikTok, Pinterest + competitor-site social-link discovery (`data/competitors.json` Tier-1 breeders).
**Status:** Research sprint #1 (pre-agent-build). Grounds the `cag-social-strategist` agent decision.

> **Honesty note:** Findings below are from organic search results captured on 2026-06-06. "Top result" = top of the platform-filtered search, NOT a verified follower/engagement rank. Follower counts are only stated where a snippet exposed one. Items marked *(strategy)* are reasoning, not measured data.

---

## 1. The one finding that changes everything

**Breeders do not win on social. The category is owned by single-bird "personality" accounts, rescue/adoption voices, and evergreen reference content.** Across all four platforms, the top organic results for African Grey terms were almost never breeders selling birds — they were talking-parrot entertainment channels and care creators.

This is the opposite of Google search (where our 30 registered competitors are breeders fighting for "african grey parrot for sale"). On social, the discovery engine is **entertainment + education, not transactions.**

**Implication *(strategy):*** CAG should NOT port its "for sale" website copy onto social. The winning play is to ride the entertainment/education engine (talking clips, chick development, care answers) and convert that attention to the website — exactly what the broken `social-content.md` skill half-knew but executed wrong.

---

## 2. Platform-by-platform landscape

### YouTube — the highest-value, breeder-absent battleground
Top organic results for "african grey parrot for sale", "talking", and "care":
- **Personality channels dominate:** Gizmo the Grey Bird, Apollo (Apollo & Frens), Einstein (Texas), Cosmo (8,000 words), Rocky, Neo, Petra. These are the recurring names across every query.
- **Cost/education content ranks high:** "How Much Do African Greys REALLY Cost", "$13k/$20k/$25k on my African Grey" — high-intent buyer-adjacent.
- **Breeders barely appear:** only *Todd Marcus Birds Exotic* (largest US parrot store) and *Lodhi Birds* surfaced, via buyer-vlog mentions, not their own ranking.
- **Marketplace play:** **The Avian Exchange** (theavianexchange.com) sponsors popular videos ("connect with breeders across the USA") — buying its way into the entertainment funnel.
- **Scam content ranks:** "DONT FALL FOR THE PARROT SCAM | Red Flags" — directly relevant to CAG's scam-prevention cluster.

**Verdict:** Biggest opportunity. We already have `cag-video-seo-agent` + `cag-youtube` + `youtube-script` skills — they just need *real footage* (Known Issue: homepage video is a placeholder).

### Instagram — buyers browse here; breeders post weakly; rescue voices are loud
- **Top result is anti-breeding:** `@gizmo_the_greybird` bio reads *"Never buy, breed, or sell parrots. Adopt, support rescue…"* — the single most visible African Grey voice is actively hostile to breeders. (See §4.)
- **Mid-size personality/owner accounts:** `@sophies_parrots` (16K followers), `@2grayguys` (rescue, amputee birds — strong story).
- **Breeders show up only as low-production Reels** with a phone number ("give us a call at 305-258-2473", Miami) — no brand, no funnel.
- **Scam/spam listings present:** a garbled IG listing URL with injected Chinese-character spam params — confirms the scam underbelly buyers fear.

**Verdict:** High-value, but we enter against a rescue-dominant narrative. Differentiation = ethical captive-bred + CITES Appendix I + USDA AWA documentation, shown not claimed.

### TikTok — virality engine, youngest audience
- **Apollo & Frens** (`@apolloandfrens`) is the recurring heavyweight; **Cruz the African Grey** (`@cruztheafricangrey`, "funniest African grey") is a named personality account.
- `#africangrey` tag carries rehoming + "looking for a forever home" content (rescue tilt again).
- **TikTok Shop** is selling African Grey *food/products* (Vitakraft) — commerce exists but for supplies, not birds.

**Verdict:** *(strategy)* Top-of-funnel only. Audience skews too young for a $1,500–$3,500, 50-year commitment. Use as repurposed Reels, not a sales channel.

### Pinterest — evergreen SEO traffic, zero breeders
- Top results are **idea boards** (`notyomamasshop/african-greys`, `naturechest`), **info sheets** ("Different Types of African Grey Parrots"), and famous-bird reference (**Alex the African Grey**).
- No breeder competition at all.

**Verdict:** *(strategy)* Pure traffic play. Pins rank in Google and live for years. Map pins → our care/comparison/species pages. Low effort, compounding return.

### X / Threads / Bluesky
- Not surfaced as meaningful in any African Grey query. **Skip** *(strategy)* — confirms the earlier recommendation.

---

## 3. Competitor social footprint (measured)

Most of our 30 registered competitors are Google-SEO breeders with thin or no social. Confirmed in this sprint:

| Competitor (registry id) | Confirmed social | Notes |
|---|---|---|
| `afroBirdsFarm` (Afro Birds Farm) | **Facebook: facebook.com/afrobirdsfarm** (active — posts + videos) | Only Tier-1 competitor with a clearly active social channel; posts link back to Parrots.php. Heavy FB user. |
| (non-registry) The Avian Exchange | YouTube sponsorships | Marketplace buying into the entertainment funnel — a model to watch. |
| (non-registry) Gray Breeders Foundation, Roberto Aviary | weak/none found | Surfaced in search; no strong social. |

**Data gap:** `data/competitors.json` has **no social fields**. Extract across competitor homepages timed out repeatedly (slow/JS-heavy sites). A focused per-competitor social crawl is the obvious next research task once the agent exists to consume it.

---

## 4. The "adopt don't shop" headwind (critical)

The largest, most-followed African Grey voices on Instagram (Gizmo) and much of the `#africangrey` TikTok tag push **rescue/adoption and explicitly oppose breeding**. Any CAG social presence enters a niche where the loudest accounts frame breeders as the villain.

**How we beat it *(strategy)*, CITES-safe and inside the Verified-Claim Ledger:**
- Never argue against rescue. Position CAG as the **responsible, documented alternative**: captive-bred in the USA, CITES Appendix I paperwork, USDA AWA license, DNA/health transparency, lifetime breeder support.
- Lead with **welfare proof** (hand-raising, weaning at 12–16 weeks, vet care) — the same values rescue advocates hold — shown, not asserted.
- Own the **anti-scam** narrative (scam content already ranks): "how to verify a real breeder" turns buyer fear into trust in *us*.

---

## 5. Content angles to beat them (per platform) *(strategy)*

| Platform | Winning format observed | CAG angle to take it |
|---|---|---|
| YouTube | Talking-bird personality + cost breakdowns + scam red-flags | Maxy (our talking Congo) clips; "Real cost of an African Grey, honestly"; "How to spot an African Grey scam" → site scam cluster |
| Instagram | Chick development, owner stories, rescue ethos | Weekly chick milestones (hand-raising at C.A.Gs); Teri's "first 30 days" voice; documentation reveals |
| TikTok | Short funny talking clips, viral hooks | Repurpose IG Reels; 1 talking clip → many platforms |
| Pinterest | Info sheets, type comparisons, care | Pin our Congo-vs-Timneh, price guide, care guide → traffic |

First-person brand voice ("here at C.A.Gs… we hand-raise every chick") applies to all, per CLAUDE.md.

---

## 6. Recommended agent architecture (carried from pre-research recommendation, now evidence-backed)

- **Build ONE `cag-social-strategist` orchestrator** — calendar, brand voice, repurpose 1 source → N platforms, CITES/pricing safety from `data/`. *Why, now proven:* the winning content is one source (a talking clip / chick photo) reused across IG + FB + TikTok + Pinterest. The work is shared; only formatting differs → skills/data, not 5 agents.
- **Keep `cag-video-seo-agent`** for YouTube (deep, distinct, already built).
- **Replace `social-content.md`** with corrected per-platform skill(s): fix breeder names (Mark & Teri), Midland TX, CITES Appendix I, hashtags, and the missing `content/social/` dir.
- **Add social schema to `competitors.json`** (instagram/facebook/youtube/tiktok/pinterest/followers/cadence) so monitoring compounds.

---

## 7. Open research tasks (for next sprint)
1. Per-competitor social crawl (handles + follower counts + post cadence) — extract timed out this run; needs stealth-proxy or Playwright session.
2. Measure actual follower/engagement on the personality leaders (Gizmo, Apollo, Cruz, Sophie's parrots) to size the audience.
3. Hashtag volume map for IG/TikTok primary + secondary keywords.
4. Identify 5–10 rescue accounts to understand (not antagonize) the dominant narrative.

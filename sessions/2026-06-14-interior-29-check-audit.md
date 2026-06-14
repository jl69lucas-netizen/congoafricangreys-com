# Interior 18-Page · 29-Check Final QA Audit — 2026-06-14

**Method:** `scripts/interior_29_audit.py` (mechanical, over fresh `dist/`) + a 3-page subjective spot-check. Plan: `docs/superpowers/plans/2026-06-14-interior-29-check-audit.md`. Build: 101 pages, clean.
**Headline:** No structural or schema regressions. Every page has H1×1, full H1–H6 (except 2 utility pages by design), exactly **one** `FAQPage`, valid JSON-LD, `BreadcrumbList`, absolute canonical, long-format meta within the kept **≤275 title / ≤300 desc** standard, no `<svg>`-in-`content:`, no escaped SVG, no 🦜, no `user-select:none`. Findings are all **minor refinements + 2 net-new enhancements**, not defects.

---

## 1. Mechanical roll-up (trustworthy after 4 auditor heuristic fixes — see §4)

| Check | Pages flagged | Verdict |
|---|---|---|
| `all_h1_h4` | 2 (contact-us, privacy-policy) | **ACCEPTED** — short utility pages; forcing H4 nesting would be artificial. |
| `has_org` | 1 (privacy-policy) | **MINOR** — legal page carries only WebPage/WebSite/Breadcrumb; add `Organization` for consistency (low priority). |
| `img_alt_le190` | 7 (diet, best-food, trusted-breeders, reviews, captive-bred, guide, adoption) | **REAL (easy)** — alt text >190 chars (e.g. diet 220-char "Mixed nuts we portion out…"). Trim to ≤190. |
| `cites_captive_usda_early` | 6 content (care-guide, african-grey-care, diet, lifespan, guide, price) + 2 utility | **MINOR SHARPEN** — CITES+captive+USDA is in meta/schema/deeper body but not in the **first 300 visible words** (Rule 44). Utility pages (contact/privacy) exempt. |
| `lifespan_40_60` | 3 content (best-food, trusted-breeders, cites-doc) + 2 utility | **MINOR** (Rule 46) — add a 40–60-yr line. Utility pages exempt. |
| `newsletter_present` | 16 | **NET-NEW (#18)** — newsletter 3-placement was never a prior interior requirement. Decision needed (see §6). |
| `updated_visible` | 18 | **NET-NEW GEO** — schema `dateModified` exists (e.g. 2026-06-06) but no **visible** "Updated <Month Year>". Add a visible freshness stamp. |

**False positives caught & fixed before reporting (would have been fabricated defects):**
- `has_org` originally flagged 14 — Organization is correctly nested as `Article.publisher`/`author`, and `@type` is sometimes a list `["LocalBusiness","PetStore"]`. ✅ real.
- `img_lazy_nonhero` originally flagged 16 — index 0 is the header logo, so the **eager** image at index 1 is the correct **LCP hero**. ✅ correct.
- `no_phone_in_body` flagged the scams page — it's the **USDA APHIS fraud hotline (844) 820-2234**, an intentional authority reference, not the breeder's number. ✅ correct (Rule 61 = breeder phone only).

## 2. Distinct-check scorecard (your 29 merged → 18 distinct)

| Merged check (source 29#) | Result |
|---|---|
| Keyword & semantic coverage (1,2,4) | ✅ heavy internal linking (76–109/page), entity-rich schema |
| Links woven mid-sentence (3,23) | ✅ ext links new-tab+rel; no bare "click here" anchors |
| AEO / BLUF / atomic (3,7,7,8,9,10) | ✅ KeyTakeaway + FAQ present; one ≤320 answer/H2 (spot-checked) |
| Logistics entities (5) | ✅ scoped — price page carries airport codes; correctly absent elsewhere |
| Local authority (6) | ◑ location-page signal; interior = AAV link only (no fabricated vet names) |
| Schema set (12) | ✅ Article/FAQPage×1/Breadcrumb + page-specific (HowTo, Product, Review, AboutPage) |
| Brand-protocol naming (11) | ❌ GAP-FLAG — no ownable house term named yet (see §5) |
| Meta (13) | ✅ within kept ≤275/≤300 standard (decision §6); brand in title |
| Image SEO 5-element (14,25) | ◑ 7 pages have alt >190; weight/<100KB not audited here |
| Readability Flesch (15) | ❌ ~53–58, under 60–70 target — trade-off, see §3 |
| Tone warm/empathetic (16) | ✅ strong on sample |
| Phone — footer yes / body no (17,Rule61) | ✅ body clean (APHIS exempt) |
| Newsletter 3 placements (18) | ❌ 16/18 lack it — net-new, §6 |
| First-person voice (19,20) | ✅ strong (price 71, reviews 63 we/our); care-guide thinner (§3) |
| Two-keyword headers + H1–H6 (21) | ✅ all content pages use full H1–H6, no skips |
| 4-Move Loop entities (22) | ✅ entity-dense schema + body |
| Non-commodity (24) | ◑ care-guide has 5 "African Greys are…" filler instances (§3) |
| Technical a11y+perf (26) | ✅ no svg-in-content, no escaped svg, dims present, lazy correct |
| Deploy + verify (27) | ✅ all 18 build to dist, canonical absolute |
| Gotchas (28) | ✅ verified in dist not source; no traps present |
| Final QA gate (29) | ◑ pass except the minor items above |

## 3. Subjective spot-check (price / care-guide / reviews)

- **Voice:** price `we/our/us`=71, reviews=63 → **STRONG**. care-guide=33 with **5** "African Greys are…" third-person filler instances → **SHARPEN** (care-guide leans encyclopedic; some is legit taxonomy, but the filler should become first-person breeder detail).
- **Honesty-Policy humor:** present on price (3 beats). Absent on care-guide/reviews — acceptable (not every page needs it; never on health/legal).
- **Flesch (stdlib approx):** price 52.7 · care-guide 57.7 · reviews 57.3 — **all under the 60–70 target**. Confirms the predicted trade-off: dense first-person + entity copy reads at ~10th–12th grade. Treat 60–70 as an aspiration with a documented floor, not a hard gate, or it fights entity density.

## 4. Learnings — what worked / what bit us

### ✅ Good (keep doing)
- **Build a mechanical auditor before eyeballing** — it scored 18 pages in <1s and made the result reproducible. Saved as `scripts/interior_29_audit.py` for every future interior page.
- **The Direction-D batch is structurally solid** — single FAQPage, full heading ladder, correct eager-LCP/lazy split, absolute canonicals, no emoji/svg-in-content traps. The polish rollout held.
- **Verify every machine "fail" against real `dist/` before writing it down** — 3 of the biggest roll-ups (has_org 14, img_lazy 16, phone 1) were auditor flaws, not page defects. Reporting them blind would have fabricated 31 false defects.

### ❌ Bad (don't repeat)
- **Naive heuristics fabricate findings:** (1) schema checks must recurse into nested `publisher`/`author` and handle **list `@type`**; (2) "first image = hero" is wrong when a header logo precedes it — detect the LCP by excluding `logo` srcs; (3) phone-in-body must exempt third-party **authority hotlines** (APHIS/FTC); (4) measuring "first 300 words" must strip inline JSON-LD that Astro renders inside `<main>`.
- **Image alt drifts over 190 chars** when writing descriptive breeder alt — 7 pages. Add a length clamp to the image-SEO step.
- **Compliance line not front-loaded:** 6 content pages keep CITES+captive+USDA in meta/schema but not the first 300 *visible* words (Rule 44).
- **Freshness is schema-only:** `dateModified` is set but never shown to humans — a missed GEO/E-E-A-T signal across all 18.

## 5. GAP-FLAGs for Mark & Teri (ledger-bounded — do NOT invent)
- **#11 Brand-protocol name:** propose coining ONE ownable house term for our hand-feeding/weaning method (working idea: *"the C.A.Gs Quiet-Wean method"*) to build attributable topical authority. **Needs breeder sign-off before it ships** — until confirmed it stays a flag, not copy.
- **#6 Local vet names:** if Mark & Teri will name their actual avian vet / hospital, we can add a real local-authority entity; otherwise interior pages keep the generic AAV "find a vet" link only.

## 6. Decisions
- **Meta length (#13 vs manual):** RESOLVED — **keep long format (≤275 title / ≤300 desc)**; auditor + manual updated to match. Rationale: deliberate long-tail strategy, all 18 already ship it, switching to 155 = full rewrite + lost tail terms.
- **Newsletter 3-placement (#18):** OPEN — do we want a newsletter signup (Top/Middle/Bottom) on interior informational pages, or keep it to the homepage/money pages? (Recommend: one mid + one footer-area placement on the long content pillars only — care-guide, guide, faq, price — not on contact/privacy; avoids clutter on thin pages.)

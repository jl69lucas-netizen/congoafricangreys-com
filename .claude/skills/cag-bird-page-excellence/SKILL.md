---
name: cag-bird-page-excellence
description: Use when building, polishing, differentiating, or doing perf/SEO/schema/a11y QA on an individual /available/ bird listing page or the /available/ hub at CongoAfricanGreys.com — especially when two birds of the same sex+variant risk cannibalizing each other, when PageSpeed/Search Console flags render-blocking CSS, oversized images, contrast, broken links, or Product rich-result errors, or when distributing location pages across bird pages.
---

# C.A.Gs Bird-Page Excellence

## Overview

The proven build-and-polish method for the `/available/` cluster (6 bird pages + hub) at CongoAfricanGreys.com, distilled from the 2026-06 polish program. **Core principle: every layer of a bird page — H1, `<title>`, meta, image alt/title, schema, geo block, FAQ — must tell ONE differentiated story that no other bird page on the site duplicates.** Two female Congos that differ only by name and price will cannibalize each other; the fix is to differentiate on a real buyer axis (life-stage) across *all* layers at once.

This is a **technique/reference skill**. It complements — does not replace — `cag-bird-listing-page` (the from-scratch 9-section builder) and `cag-final-page-pass` (the mechanical gate). Use this when polishing, differentiating, or running perf/schema/a11y/geo fixes on pages that already exist.

## When to Use

- Two or more bird pages share the **same sex + variant** (e.g. Bery + Amie, both female Congo) and their titles/H1s/alts are identical-minus-name → cannibalization.
- PageSpeed flags **render-blocking CSS** (`JumpRail.css`, component CSS), **oversized images**, **unused JS** (`/70de/` = Rocket Loader), or **LCP** on a video-hero bird page.
- Search Console flags a **Product rich-result** critical/non-critical error.
- Need to **distribute real location pages** across bird pages as shipping-destination sections.
- WCAG **AA contrast** fails on clay-on-dark (`text-gold` on `bg-logo-dark`).
- A **broken external link** (fws.gov / cites.org) returns 404/403.
- Running a **keyword/entity/voice self-audit** + competitor benchmark.

**When NOT to use:** building a brand-new bird page from zero (use `cag-bird-listing-page`); non-`/available/` pages (use the interior/location/comparison builders).

## The Non-Negotiables (carry into every task)

1. **Work on `main`** — never feature branches (only `main` auto-deploys; branch work strands at live-404).
2. **Verify in `dist/`, not source** — generators hide schema/headings; grep the built HTML.
3. **Real slugs only** — link a location page only after `test -d src/pages/<slug>` passes. Never invent a slug.
4. **No fabricated reviews** — never add `aggregateRating`/`review` schema. Schema fixes use truthful `Offer` fields only.
5. **First-person voice** ("here at C.A.Gs, our…, we hand-raised…"), CITES Appendix I + captive-bred-USA framing, inside the Verified-Claim Ledger.
6. **Heading gate** — all six levels, **min 5 H5 + 5 H6**, no skipped levels. Present the H1→H6 outline before changing hierarchy.
7. **Commit + push after every build** — push = deploy.

## Quick Reference — the differentiation matrix

When two birds share sex+variant, split them on **life-stage** and propagate the split through every layer:

| Layer | Bery (1-yr, $1,700) | Amie (3-mo, $2,500) |
|---|---|---|
| H1 | "Tame **1-Year-Old** Female Congo African Grey **Parrot** For Sale … Hand-Reared & DNA-Sexed **Hen**" | "**Hand-Fed Baby** Female Congo African Grey **Parrot** For Sale … **Cuddly** & Fully-Socialised at **3 Months**" |
| `<title>` | "Best-**Value** … Tame Hand-Reared **1-Year-Old** …" | "**Baby** … Cuddly Hand-Fed … **3-Month** …" |
| meta desc | "tame, hand-reared 1-year-old … hen" | "cuddly, hand-fed baby … 3 months" |
| image alt/title | "tame 1-year-old hand-reared … hen" | "cuddly hand-fed baby … 3 months" |
| buyer intent owned | "1 year old female grey / settled-now / value" | "baby female grey / raise-from-start / premium" |

**Why life-stage:** it is the single most-searched, least-ambiguous axis a same-sex/same-species buyer distinguishes on. Adjectives ("cuddly/affectionate") are softer SEO signals than a concrete age token. Always add the **"Parrot"** entity to the H1/title/meta. Weave related search terms naturally: *hand-reared, hand-fed, cuddly, tame, hen, finger-tame, well-socialised*.

## Quick Reference — the proven fixes

| Defect | Fix | Verify |
|---|---|---|
| Render-blocking `JumpRail.css` | Drop JumpRail **only if** the page has `cag-jump-nav` as a replacement ToC. Bird pages do; the homepage + 16 interior pages use JumpRail as their *only* ToC — do NOT blind-delete there. | `grep -rl JumpRail dist/available/` = empty |
| Unused JS `/70de/` (71 KiB) | **Cloudflare Rocket Loader** — breeder dashboard toggle (Speed → Optimization → Rocket Loader = OFF). NOT a repo fix. | re-run PageSpeed after toggle |
| LCP on video-hero pages | Preload the poster via a `heroPreload` prop in BaseLayout `<head>` (`<video poster>` can't take `fetchpriority`). | `grep 'rel="preload" as="image"' dist/.../index.html` |
| Oversized images | Pillow downscale to ~2× CSS display, **shrink-only never upscale**, re-encode WebP q=80. | `ls -la dist/.../*.webp` < target |
| AA contrast clay-on-dark | `text-gold` / `text-gold/90` on `bg-logo-dark` → `text-[#f08070]` (~6:1 on `#12100e`). Never use opacity modifiers on small clay text. | contrast-ratio python snippet ≥ 4.5 |
| Broken fws.gov CITES link (404) | Replace with `https://www.fws.gov/international-affairs/cites`; if 404 fall back to `https://cites.org`. | **human browser** — fws/cites/Google block curl+WebFetch (403) |
| Product rich-result critical | Add truthful `Offer` fields: `priceValidUntil`, `shippingDetails` (OfferShippingDetails $185), `hasMerchantReturnPolicy` (real health-guarantee window). No reviews. | JSON-LD parses in `dist/`; Rich Results Test (human) |
| Geo distribution | One **distinct regional set + unique H3** per bird page (West/Mountain · Southeast · Midwest · NE/Mid-Atlantic · TX · pairs). Same-tab internal links. | every href `test -d` resolves; 0 `target="_blank"` on geo links |
| Duplicate image alts across pages | De-dup: inject each bird's life-stage into the alt; keep alt ≤190 chars (5-element image SEO). | grep the shared pattern → on 0 pages |
| "cheap African Grey" competitor query | Add ONE counter-snippet FAQ on `/african-grey-parrot-price/` reframing *cheap* → honest all-in value; renders in visible accordion **and** FAQPage schema. | FAQ Q in both `dist/` HTML and parsed FAQPage JSON |

## Implementation — the verification commands that caught real bugs

```bash
# Slug resolution — every geo href must be a real page on disk
for slug in $(grep -rho 'href="/[a-z-]*for-sale[a-z-]*/"' src/pages/available/ \
  | sed 's/href="\///;s/"//' | grep -v '^available' | sort -u); do
  test -d "src/pages/${slug%/}" && echo "OK $slug" || echo "MISSING $slug"
done

# BEFORE committing any working-tree deletion — confirm zero live references
for f in <deleted-file>; do grep -rln "$f" src/ public/ || echo "  no refs → safe"; done
# (A plan PREDICTED two webp were unreferenced; reality: still on 14 pages incl. homepage.
#  Always grep-verify. Restore with `git checkout -- <path>` if referenced.)

# Distinct H1s — confirm two same-sex/variant pages are NOT identical-minus-name
b=$(grep -oE '<h1[^>]*>[^<]*Bery[^<]*' dist/available/bery/index.html | sed 's/Bery//')
a=$(grep -oE '<h1[^>]*>[^<]*Amie[^<]*' dist/available/amie/index.html | sed 's/Amie//')
[ "$b" != "$a" ] && echo "DISTINCT" || echo "STILL PARALLEL"

# alt > 190 chars (image-SEO rule)
python3 -c "import re;[print(len(a),a) for a in re.findall(r'alt=\"([^\"]*)\"',open('dist/available/roys/index.html').read()) if len(a)>190]"

# AA contrast ratio
python3 - <<'PY'
def lin(c):
    c/=255; return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
def L(h): r,g,b=int(h[1:3],16),int(h[3:5],16),int(h[5:7],16); return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def ratio(a,b): la,lb=L(a),L(b); return (max(la,lb)+0.05)/(min(la,lb)+0.05)
print("f08070 on 12100e:", round(ratio('#f08070','#12100e'),2))   # want >=4.5
PY

# Final gate
npx astro build && python3 scripts/final_page_audit.py --birds   # want 0 FAIL
python3 scripts/generate_sitemaps.py                              # want 0 phantom URLs
```

## Common Mistakes (every one of these actually happened — 2026-06)

| Mistake | What went wrong | Fix / rule |
|---|---|---|
| **Committing a deletion without grep** | Plan claimed 2 `.webp` were unreferenced; they were live on 14 pages incl. the homepage. Committing would have broken every one. | Always `grep -rln` references first. Restore if referenced. Reality can contradict the plan — look before deleting. |
| **Blind-deleting a shared component** | JumpRail was safe to drop on bird pages (they have `cag-jump-nav`) but is the *only* ToC on the homepage + 16 interior pages. | Check for a replacement nav before removing a shared component anywhere. |
| **Identical headers across sibling pages** | Bery & Amie H1s were byte-identical minus name/price → cannibalization. | Differentiate on a real buyer axis (life-stage) across H1+title+meta+alt at once. |
| **Cross-page duplicate image alts** | 3 alt/title pairs were identical-minus-name across the two female-Congo pages. | De-dup alts per page; inject the life-stage signal; keep ≤190 chars. |
| **Grepping source, trusting loose patterns** | A geo-block grep matched the IATA *shipping* block instead; the spec-review subprocess "failed" though the work was sound. | Verify in `dist/` with precise patterns; verify the work directly, don't trust a wrapper's error. |
| **Assuming curl/WebFetch can verify a link** | fws.gov, cites.org, and Google's Rich Results Test all 403 every automated agent. | Mark these **human-browser** steps; never claim a 200 you couldn't fetch. |
| **Re-encode that upscales** | A downscale script that upscales grows file size (a prior re-encode grew roys-personality 48→65 KB). | Shrink-only guard (`if im.width > target_w`); never upscale. |
| **Amending an auto-pushed commit** | The post-commit hook auto-pushes commit #1; amending it diverges origin and later pushes silently fail. | Commit fixes as NEW commits, or reconcile with `--force-with-lease`. |

## Real-World Impact

The 2026-06 program took the 6 `/available/` pages to: 0 FAIL on `final_page_audit --birds`; full H1→H6 (5+ H5/H6) on every page; JumpRail render-blocking eliminated from the cluster; truthful Product/Offer schema clearing the Search Console critical; distinct regional geo blocks (no duplicate content); Bery/Amie fully de-cannibalized across title+meta+H1+imagery; and a competitor benchmark showing CITES/DNA/captive-bred entity depth (34–40×/page) that every scraped competitor lacked entirely.

## Related

- `cag-bird-listing-page` — from-scratch 9-section builder (single Product/Offer, sell-and-retire lifecycle).
- `cag-final-page-pass` — the mechanical PASS/FAIL gate (`scripts/final_page_audit.py --birds`).
- `BIRD-PAGE-BUILD-MANUAL.md` (repo root) — the copy-paste step-by-step companion to this skill.
- Memories: `feedback_hybrid_header_seo`, `feedback_bird_page_geo_diversification`, `feedback_image_seo_5element`, `reference_aa_contrast_and_perf_fixes`, `project_autopush_hook_amend_diverges`, `feedback_verify_rendered_not_source`.

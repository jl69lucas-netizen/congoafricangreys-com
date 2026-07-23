---
name: cag-canonical-fixer
description: Fixes relative canonical URLs across all CAG HTML pages. The Simply Static WordPress export generates relative canonicals (href="/slug/") which cause Google to mark all pages as "Canonicalised /" — not indexed. This agent converts them to absolute URLs. Run on every fresh static export before deploying. Also fixes og:url and JSON-LD url fields.
tools: [Read, Write, Bash]
model: claude-opus-4-8
effort: medium
dynamic_workflow: false
---

## Golden Rule
> **Write-From-Outline, NEVER-From-Sibling (ALWAYS):** Do NOT open a sibling page to copy or paraphrase paragraphs — open it only to read its component/CSS structure. Reuse components, CSS classes and structural patterns freely (that IS the kit), but write every page's PROSE fresh from ITS OWN approved outline + distribution matrix, in genuinely different framing, sentence structure, angle and vocabulary, leaning on that page's own entity/angle. Only the whitelist may match verbatim (shipping line, doc-badge lists, counter strip, CITES notice, CTA labels, real reviews, real page-name link labels). Run `scripts/dup_content_audit.py` AND `--headers` on YOUR OWN draft BEFORE calling it done, targeting zero non-whitelist crossover — dedup is a pre-write discipline, not post-hoc cleanup.
> **Title Case Headings (ALWAYS):** Every H1–H6 uses AP-style Title Case — capitalise 4+ letter words and ALL nouns/verbs/adjectives/adverbs regardless of length (`Is`, `Are`, `Do`, `Be`, `Not`, `Our`); lowercase mid-title only `a an the and but or nor for so yet at by in of on to as vs per via`; always capitalise the first word, the last word and the word after `:` `?` `!` (an em dash does NOT force a capital). Hyphenated compounds capitalise each part (`Hand-Raised`, `Captive-Bred`); never touch acronyms/brands/domains (`C.A.Gs`, `CITES`, `USDA`, `DNA`, `PCR`, `IATA`). SCOPE IS HEADINGS ONLY — FAQ questions in `<summary>` stay conversational sentence case. Verify with `python3 scripts/page_hardening_scan.py <slug>` → zero `header-not-title-case`.
> **Heading Hierarchy Outline Gate (ALWAYS):** Before writing or changing ANY page, first present the COMPLETE H1→H6 outline — every heading, in render order, labelled by level — and get explicit approval. No page code is touched until the outline is approved. Levels descend sequentially with NO skipped levels (H3→H6 and H2→H4 are BANNED; stepping back up to start a new section is fine). Every page carries all six levels with a MINIMUM of 5 H5 AND 5 H6. Semantic map: H1 page topic · H2 search intents · H3 subtopics · H4 micro-intent/PAA answers · H5 supporting facts/warnings · H6 ultra-specific details/breeder notes/citations. Every heading is AP-style Title Case (see the Title Case rule). Verify with `python3 scripts/final_page_audit.py`.
> **Link-First (ALWAYS):** For ALL internal and external links, the anchor sits at the START of the sentence/paragraph — inside the opening words (first clause). Never mid-sentence, never at the end. ✅ `Our <a>Congo African Grey care guide</a> covers diet in depth…` · ❌ `…diet is covered in our <a>care guide</a>.` (Supersedes the old beginning-or-middle rule, 2026-07-11. Sole exception: branded ACTION anchors on CTAs per skills/cag-branded-hybrid-keywords.md.)
> **Clarification Checkpoint (ALWAYS):** Below the ≥97% Confidence Gate, do NOT dead-stop the whole job. First write finished work to disk (cleared sections to the page; in-progress notes + the open question to the live session brief's `## Open Flags`), then ask the user ONE narrow question, then keep building every part that isn't blocked. Only the uncertain unit waits for the answer. A stop must never cost more than that one piece, and the question must survive session teardown (it's on disk, not just in chat).
> **First-Person Brand Voice (ALWAYS):** Write as the breeder — "we / our / here at C.A.Gs." Frame our birds, credentials, and process as *ours*, not from the outside. Exceptions (stay neutral): encyclopedic species/taxonomy facts and cited research. Never fabricate — every claim is bounded by the Verified-Claim Ledger and real CAG data (GSC/competitors/codebase), never invented.
> Relative canonical URLs = zero indexing. This is the single most critical SEO fix on the site.
> Every fresh WordPress static export WILL have relative canonicals. Always run this before deploying.
> **Confidence Gate:** ≥97% before writing any site file.

---

## CAG Project Context
> **Site:** CongoAfricanGreys.com — Cloudflare Pages static site (project: `congoafricangreys`)
> **GitHub repo:** `jl69lucas-netizen/congoafricangreys-com` (branch: `main`)
> **Root cause:** Simply Static WordPress plugin exports with relative `href="/slug/"` in canonical tags.
> **Effect:** Google Search Console reports all pages as "Canonicalised /" — none get indexed.
> **Fix:** Replace all relative `href` in canonical tags with absolute `https://congoafricangreys.com/slug/`.

---

## Purpose

You convert relative canonical URLs (and `og:url` + JSON-LD `url` fields) to absolute `https://congoafricangreys.com/...` URLs across every static-export HTML page, so Google stops collapsing the whole site into "Canonicalised /" and actually indexes each page. Run on every fresh export before deploy.

## On Startup — Read These First

1. **Confirm** the build output exists — `ls dist/` (or the active export dir). You operate on built HTML, not source.
2. **Read** `CLAUDE.md` → canonical/deploy notes and the live domain.
3. **Grep** the export for relative canonicals before fixing: `grep -rl 'rel="canonical" href="/' dist/`.

## Why This Happens

The WordPress Simply Static export uses the WordPress `home_url()` function which can return an empty string or just `/` when the site is exported to a static file. This causes:

```html
<!-- Bad — what Simply Static exports -->
<link rel="canonical" href="/">                    ← homepage (wrong, should be absolute)
<link rel="canonical" href="/buy-african-grey-parrot-near-me/">  ← all other pages (wrong)

<!-- Also bad in og:url -->
<meta property="og:url" content="/">

<!-- Also bad in JSON-LD -->
{"@type":"WebSite","url":""}
```

Google sees `href="/"` as the canonical for EVERY page → treats all as duplicates of the homepage → none indexed.

---

## Fix 1: Canonical Tags (Critical — do first)

**Check:**
```bash
grep -r 'rel="canonical"' /path/to/site --include="*.html" | grep -v 'https://congoafricangreys.com' | wc -l
# Expected after fix: 0
```

**Bulk fix:**
```bash
SITE=/path/to/html/files  # e.g. /tmp/cag-repo

find $SITE -name "*.html" -exec \
  perl -i -pe 's|(<link rel="canonical" href=")(/[^"]*)(")|\1https://congoafricangreys.com\2\3|g' {} \;
```

**Verify:**
```bash
grep -r 'rel="canonical"' $SITE --include="*.html" | grep -v 'https://' | wc -l
# Must be 0
grep -r 'rel="canonical"' $SITE --include="*.html" | head -5
# Should show: href="https://congoafricangreys.com/slug/"
```

---

## Fix 2: og:url Tags

**Check:**
```bash
grep -r 'og:url' /path/to/site --include="*.html" | grep -v 'https://congoafricangreys.com' | wc -l
```

**Bulk fix:**
```bash
find $SITE -name "*.html" -exec \
  perl -i -pe 's|(property="og:url" content=")(/[^"]*)(")|\1https://congoafricangreys.com\2\3|g' {} \;
```

---

## Fix 3: JSON-LD url fields

**Check:**
```bash
grep -r '"url":""' /path/to/site --include="*.html" | wc -l
```

**Fix:**
```bash
find $SITE -name "*.html" -exec \
  sed -i '' 's|"url":""|"url":"https://congoafricangreys.com"|g' {} \;
```

---

## Bulk Apply (All 3 Fixes)

```bash
SITE=/tmp/cag-repo  # adjust to your path

# Fix 1: Canonical tags
find $SITE -name "*.html" -exec \
  perl -i -pe 's|(<link rel="canonical" href=")(/[^"]*)(")|\1https://congoafricangreys.com\2\3|g' {} \;

# Fix 2: og:url
find $SITE -name "*.html" -exec \
  perl -i -pe 's|(property="og:url" content=")(/[^"]*)(")|\1https://congoafricangreys.com\2\3|g' {} \;

# Fix 3: JSON-LD empty url
find $SITE -name "*.html" -exec \
  sed -i '' 's|"url":""|"url":"https://congoafricangreys.com"|g' {} \;

echo "Done. Verifying..."
grep -r 'rel="canonical"' $SITE --include="*.html" | grep -v 'https://' | wc -l
# Must output: 0
```

---

## Verification Checklist

After applying fixes:

```bash
# 1. No remaining relative canonicals
grep -r 'rel="canonical"' $SITE --include="*.html" | grep -v 'https://' | wc -l
# Expected: 0

# 2. Sample spot check
grep 'rel="canonical"' $SITE/index.html
# Expected: href="https://congoafricangreys.com/"
grep 'rel="canonical"' $SITE/buy-african-grey-parrot-near-me/index.html
# Expected: href="https://congoafricangreys.com/buy-african-grey-parrot-near-me/"

# 3. No relative og:url
grep -r 'og:url' $SITE --include="*.html" | grep -v 'https://' | wc -l
# Expected: 0
```

After deploying, verify live via Google Search Console:
- Coverage report should shift from "Canonicalised" → "Valid"
- Allow 2–7 days for Googlebot to recrawl

---

## Commit Pattern

```bash
cd /tmp/cag-repo
git add -A
git commit -m "fix: absolute canonical URLs, og:url, JSON-LD — fixes GSC canonicalisation issue"
git push origin main
```

---

## When to Run

- After EVERY new Simply Static export from WordPress
- After any batch page rebuild that regenerates HTML
- Before every Cloudflare Pages deployment
- When GSC reports pages as "Canonicalised /" or "Duplicate without user-selected canonical"

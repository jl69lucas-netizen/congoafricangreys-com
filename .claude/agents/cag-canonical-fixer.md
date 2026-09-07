---
name: cag-canonical-fixer
description: Fixes relative canonical URLs across all CAG HTML pages. The Simply Static WordPress export generates relative canonicals (href="/slug/") which cause Google to mark all pages as "Canonicalised /" — not indexed. This agent converts them to absolute URLs. Run on every fresh static export before deploying. Also fixes og:url and JSON-LD url fields.
tools: [Read, Write, Bash]
model: inherit
effort: medium
---

## Golden Rule
> **Bound by the site rules, not by a copy of them:** `CLAUDE.md`'s thirteen judgment rules (first-person voice · CITES Appendix I · Recommend + Why · restate the brief · preview before apply · 97% Confidence Gate with the Clarification Checkpoint, never a dead-stop · write from the outline, never from a sibling · no fabricated claims · Verified-Claim Ledger · two brand-owned method labels · Artifact deliverables) and the packs in `rules/` (headings, images, schema, links, copy, design, gates, deploy, for-sale), indexed by `data/quality/rule-index.json`. Heading outline gate, Title Case, header-style declaration and Link-First all live there and are enforced by `tests/render/`. Use Claude Code and the Playwright CLI first; call an MCP, external CLI or API only when the task genuinely cannot be done without it.
> Relative canonical URLs = zero indexing. This is the single most critical SEO fix on the site.
> Every fresh WordPress static export WILL have relative canonicals. Always run this before deploying.

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

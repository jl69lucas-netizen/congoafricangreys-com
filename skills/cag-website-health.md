---
name: cag-website-health
description: Technical site audit and auto-fixer for CongoAfricanGreys.com. Checks canonicals, images, forms, schema, Core Web Vitals via Playwright CLI.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG WEBSITE HEALTH & TECHNICAL FIX SKILL
## Managed Agent: Technical Site Auditor & Auto-Fixer for CongoAfricanGreys.com
**Version 1.0 — Static Site Maintenance Agent**

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

---

## SKILL OVERVIEW

You are a technical site health agent for **CongoAfricanGreys.com** — a static HTML site (exported from WordPress, hosted on TBD) located at `/Users/apple/Downloads/CAG/site/content/`. Your job is to diagnose and fix technical SEO and rendering issues across all pages, then report what was fixed and what still requires manual action (e.g., DNS/hosting config).

### Your Capabilities:
- Detect and fix broken WordPress lazy-load images (GIF placeholder → real `src`)
- Fix relative canonical tags → absolute `https://congoafricangreys.com/...` URLs
- Manage `_redirects` rules (www→non-www, old WordPress URLs)
- Manage `_headers` (CSP, security headers)
- Audit all 99+ pages for SEO issues
- Fetch live pages to compare local files vs deployed state
- Identify issues that require hosting provider action (DNS, domain aliases)

---

## SITE CONTEXT

| Property | Value |
|---|---|
| Domain | https://congoafricangreys.com |
| Local files | `/Users/apple/Downloads/CAG/site/content/` |
| Host | Netlify (static site) |
| Origin | WordPress export (static HTML) |
| Pages | 99+ index.html files |
| Redirects file | `_redirects` |
| Headers file | `_headers` |
| Images | `/wp-content/uploads/` (739 files) |

---

## STEP 1: DIAGNOSE ISSUES

Before fixing anything, run this diagnostic to understand the site's current state:

### A. Check for Broken Lazy-Load Images
WordPress lazy-load plugins replace `src` with a 1×1 GIF placeholder and store the real URL in `data-src`. After static export, the JS never runs and images stay broken.

**Detection pattern:**
```python
import re, glob

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"
broken = []
for f in glob.glob(f"{SITE_ROOT}/**/index.html", recursive=True):
    content = open(f).read()
    count = len(re.findall(r'src="data:image/gif;base64,[^"]*"', content))
    if count:
        broken.append((f.replace(SITE_ROOT,''), count))
print(f"Pages with broken imgs: {len(broken)}, Total broken: {sum(c for _,c in broken)}")
```

### B. Check for Relative Canonical Tags
All canonical `href` values must be absolute `https://african grey parrotsforsale.com/...` URLs. Relative canonicals (`href="/"`) are ambiguous when the www subdomain is active.

**Detection pattern:**
```python
import re, glob

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"
for f in glob.glob(f"{SITE_ROOT}/**/index.html", recursive=True):
    content = open(f).read()
    canonicals = re.findall(r'<link[^>]*rel=["\']canonical["\'][^>]*href="([^"]*)"', content)
    for c in canonicals:
        if not c.startswith('http'):
            print(f"Relative canonical: {f.replace(SITE_ROOT,'')} → {c}")
```

### C. Check www Redirect
Fetch `http://www.african grey parrotsforsale.com/` — if it shows "Site Currently Unavailable" the www domain is not configured in Netlify.

**Fix required:**
1. Add www as a domain alias in Netlify dashboard → Domains
2. The `_redirects` rule (already present) will then handle the 301

### D. Fetch Live vs Local Comparison
```python
# Use WebFetch to check live pages vs local
# Check: https://african grey parrotsforsale.com/
# Check: https://congoafricangreys.com/congo-african-grey-for-sale/
# Check: https://african grey parrotsforsale.com/micro-african grey parrot-puppies/
```

---

## STEP 2: APPLY FIXES

### Fix A — Broken Lazy-Load Images (Auto-fixable)

Run this Python script across all HTML files:

```python
import re, glob

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"

def fix_lazy_images(content):
    def replace_img(m):
        tag = m.group(0)
        data_src = re.search(r'\bdata-src="([^"]*)"', tag)
        if not data_src:
            return tag
        real_src = data_src.group(1)
        fixed = re.sub(r'\bsrc="data:image/gif;base64,[A-Za-z0-9+/=]+"', f'src="{real_src}"', tag)
        fixed = re.sub(r'\s*data-src="[^"]*"', '', fixed)
        # Fix data-srcset → srcset if present
        data_srcset = re.search(r'\bdata-srcset="([^"]*)"', fixed)
        if data_srcset:
            fixed = re.sub(r'\bsrcset="[^"]*"', f'srcset="{data_srcset.group(1)}"', fixed)
            fixed = re.sub(r'\s*data-srcset="[^"]*"', '', fixed)
        return fixed
    return re.sub(
        r'<img\b[^>]*src="data:image/gif;base64,[A-Za-z0-9+/=]+"[^>]*/?>',
        replace_img, content
    )

fixed_files = 0
fixed_imgs = 0
for fpath in glob.glob(f"{SITE_ROOT}/**/index.html", recursive=True):
    original = open(fpath).read()
    fixed = fix_lazy_images(original)
    if fixed != original:
        count = len(re.findall(r'src="data:image/gif', original))
        fixed_imgs += count
        fixed_files += 1
        open(fpath, 'w').write(fixed)
print(f"Fixed {fixed_imgs} images across {fixed_files} files")
```

### Fix B — Relative Canonical Tags (Auto-fixable)

```python
import re, glob

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"
DOMAIN = "https://african grey parrotsforsale.com"

def fix_canonicals(content):
    def replace_canonical(m):
        href = m.group(1)
        if href.startswith('http'):
            return m.group(0)
        return m.group(0).replace(f'href="{href}"', f'href="{DOMAIN}{href}"')
    
    content = re.sub(
        r'<link[^>]*rel=["\']canonical["\'][^>]*href="([^"]*)"[^>]*/?>',
        replace_canonical, content
    )
    return content

for fpath in glob.glob(f"{SITE_ROOT}/**/index.html", recursive=True):
    original = open(fpath).read()
    fixed = fix_canonicals(original)
    if fixed != original:
        open(fpath, 'w').write(fixed)
        print(f"Fixed: {fpath.replace(SITE_ROOT,'')}")
```

### Fix C — www Redirect Rule (In `_redirects`)

Ensure this line is at the TOP of `_redirects`:
```
https://www.african grey parrotsforsale.com/* https://african grey parrotsforsale.com/:splat 301!
```

**Note:** This redirect only activates once the www domain is added as a Netlify domain alias. Manual step required in Netlify dashboard.

### Fix D — CSP Headers (If needed)

Check `_headers` for missing domains in `Content-Security-Policy`. Common missing domains after WordPress migration:
- `https://www.googletagmanager.com`
- `https://ipapi.co`
- `https://maps.googleapis.com`

---

## STEP 3: VERIFY FIXES

After applying fixes, verify:

```python
import re, glob

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"

for fpath in glob.glob(f"{SITE_ROOT}/**/index.html", recursive=True):
    content = open(fpath).read()
    
    broken_imgs = len(re.findall(r'src="data:image/gif;base64,', content))
    canonicals = re.findall(r'<link[^>]*rel=["\']canonical["\'][^>]*href="([^"]*)"', content)
    
    issues = []
    if broken_imgs:
        issues.append(f"{broken_imgs} broken imgs")
    for c in canonicals:
        if not c.startswith('http'):
            issues.append(f"relative canonical: {c}")
    
    if issues:
        print(f"STILL BROKEN — {fpath.replace(SITE_ROOT,'')}: {', '.join(issues)}")

print("Verification complete.")
```

---

## STEP 4: ISSUES REQUIRING MANUAL ACTION

These cannot be fixed by code changes alone — report them to the user:

| Issue | What's Needed | Where |
|---|---|---|
| www subdomain down | Add `www.african grey parrotsforsale.com` as domain alias | Netlify Dashboard → Domains |
| DNS propagation | May take 24-48h after adding www alias | Netlify / Domain registrar |
| Deploy after fixes | Push/upload updated `site/content/` files to Netlify | Netlify Dashboard or CLI |
| Schema `@id` URLs | Review schema blocks for hardcoded incorrect URLs | Each page's `<script type="application/ld+json">` |

---

## STEP 5: REPORTING FORMAT

Always return a structured report:

```
## MFS Website Health Report — [DATE]

### Fixes Applied (Automated)
- ✅ [N] broken lazy-load images fixed across [N] pages
- ✅ [N] relative canonical tags converted to absolute URLs
- ✅ www → non-www redirect rule added to _redirects

### Issues Requiring Manual Action
- ⚠️ www.african grey parrotsforsale.com unavailable — add as Netlify domain alias
- ⚠️ Site must be redeployed to Netlify for fixes to go live

### Pages Checked
- https://african grey parrotsforsale.com/ — [status]
- https://congoafricangreys.com/congo-african-grey-for-sale/ — [status]
- https://african grey parrotsforsale.com/micro-african grey parrot-puppies/ — [status]

### Next Recommended Actions
1. Deploy updated files to Netlify
2. Add www as Netlify domain alias
3. Request Google Search Console recrawl for canonical updates
```

---

## STEP 6: CORE WEB VITALS CHECK

Check page performance before and after any major rebuild. Use Playwright CLI as the primary method; fall back to `npx lighthouse@latest` only if Playwright CLI is unavailable.

### CWV Targets

| Metric | Target | Fail Threshold |
|--------|--------|---------------|
| LCP (Largest Contentful Paint) | < 2.5s | > 4.0s |
| TTFB (Time to First Byte) | < 800ms | > 1800ms |
| CLS (Cumulative Layout Shift) | < 0.1 | > 0.25 |
| FCP (First Contentful Paint) | < 1.8s | > 3.0s |

### Primary Method — Playwright CLI

```bash
# Navigate to page and capture timing via browser performance API
playwright navigate "https://african grey parrotsforsale.com/[slug]/"
playwright evaluate "JSON.stringify(performance.getEntriesByType('navigation')[0])"
# Read: responseStart (TTFB), domContentLoadedEventEnd (total load)

# For LCP — inject PerformanceObserver check
playwright evaluate "
new Promise(resolve => {
  new PerformanceObserver(list => {
    const entries = list.getEntries();
    resolve(entries[entries.length-1].startTime);
  }).observe({type: 'largest-contentful-paint', buffered: true});
  setTimeout(() => resolve('timeout'), 5000);
})"
```

### Lighthouse CLI Fallback

If Playwright performance API is insufficient, use the standalone Lighthouse CLI:

```bash
npx lighthouse@latest https://congoafricangreys.com/[slug]/ \
  --output json \
  --quiet \
  --form-factor=mobile \
  --throttling-method=simulate \
  --chrome-flags="--headless --no-sandbox" \
  | python3 -c "
import json, sys
d = json.load(sys.stdin)
audits = d['audits']
print('LCP:', audits['largest-contentful-paint']['displayValue'])
print('FCP:', audits['first-contentful-paint']['displayValue'])
print('CLS:', audits['cumulative-layout-shift']['displayValue'])
"
```

### CWV Report Format

```
## Core Web Vitals — /[slug]/ — [date]
| Metric | Score | Target | Status |
|--------|-------|--------|--------|
| LCP    | [Xs]  | <2.5s  | ✅/❌  |
| TTFB   | [Xms] | <800ms | ✅/❌  |
| CLS    | [X]   | <0.1   | ✅/❌  |
| FCP    | [Xs]  | <1.8s  | ✅/❌  |

Top 3 opportunities:
1. [issue] — estimated improvement: [X]s
2. [issue]
3. [issue]
```

---

## PAGE SPEED AUDIT

Run after any major page rebuild or quarterly as part of site health. Target: Core Web Vitals LCP <2.5s, CLS <0.1, INP <200ms.

| Check | Recommendation | Audit Command |
|---|---|---|
| Image format | Convert to WebP; add `loading="lazy"` to below-fold images | `grep -rn "<img" site/content/ --include="*.html" \| grep -v "webp\|loading"` |
| Critical CSS | Inline above-fold styles in `<head>` | Manual review of hero section |
| JavaScript | Defer non-critical JS (`defer` or `async`) | `grep -rn "<script" site/content/ --include="*.html" \| grep -v "defer\|async\|application/ld"` |
| Caching | Verify `site/content/_headers` has cache-control rules | `grep -n "Cache-Control" site/content/_headers` |
| CDN | All static assets served via Netlify CDN | Automatic via Netlify — verify in deploy logs |

### Image Format Audit
```bash
# Count JPG/PNG images still in use (WebP conversion candidates)
grep -rn 'src="[^"]*\.\(jpg\|jpeg\|png\)"' site/content/ --include="*.html" | wc -l

# List specific non-WebP images
grep -roh 'src="[^"]*\.\(jpg\|jpeg\|png\)"' site/content/ --include="*.html" | sort | uniq | head -30
```

### Lazy Loading Audit
```bash
# Find images missing loading="lazy" (below-fold images should have it)
grep -rn "<img" site/content/ --include="*.html" | grep -v 'loading=' | head -20
```

### JS Defer Audit
```bash
# Find non-critical scripts missing defer or async
grep -rn "<script" site/content/ --include="*.html" | grep -v "defer\|async\|application/ld+json\|type=" | head -20
```

### Cache-Control Check
```bash
grep -n "Cache-Control\|cache-control" site/content/_headers 2>/dev/null || echo "No cache rules found in _headers"
```

**CWV Targets:**
- LCP (Largest Contentful Paint): < 2.5s (fail > 4.0s)
- CLS (Cumulative Layout Shift): < 0.1 (fail > 0.25)
- INP (Interaction to Next Paint): < 200ms (fail > 500ms)

---

## KNOWN ISSUES LOG

| Date | Issue | Fix Applied | Status |
|---|---|---|---|
| 2026-04-21 | 707 broken lazy-load images site-wide | Replaced GIF placeholders with real src | ✅ Fixed locally |
| 2026-04-21 | 99 relative canonical tags | Converted to absolute https://african grey parrotsforsale.com/... | ✅ Fixed locally |
| 2026-04-21 | www subdomain unavailable | Added redirect rule to _redirects | ⚠️ Needs Netlify domain alias |
| 2026-04-21 | Homepage not loading via WebFetch | May be Netlify deployment gap | ⚠️ Needs redeployment |

---

## AGENT INTEGRATION NOTES

This skill is designed to be the **Technical Health Agent** in a multi-agent MFS management system:

- **Technical Health Agent** (this skill) — fixes rendering, SEO tags, redirects
- **Content Agent** — creates/updates page copy using MFS.md instructions
- **Location Page Agent** — uses LOCATION-PAGE-BUILDER-SKILL.md to create state pages
- **SEO Audit Agent** — checks GSC data, keyword rankings, page performance
- **Image Agent** — manages /wp-content/uploads/, generates image prompts, webp conversion

When used as a managed agent, trigger this skill:
- On deploy: run full diagnostic before and after
- Weekly: check for new broken images from CMS updates
- On new page creation: verify canonical and images immediately
---
name: cag-performance-fixer
description: Applies proven Lighthouse Performance fixes to CAG pages. Run after any page rebuild or new page creation to achieve 100% Performance score. Fixes WooCommerce CSS render-blocking, jQuery defer, font-display swap, LCP fetchpriority+preload, lazysizes removal.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG Performance Fixer

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs if the task genuinely cannot be done with Claude Code alone.

A fix is not complete until Lighthouse confirms the score. Always verify with the Lighthouse CLI after applying fixes.

## Fix Checklist

Apply all 5 fixes to every CAG HTML page. Fixes are safe to apply in bulk with bash commands.

---

### Fix 1: Remove WooCommerce CSS (saves ~150ms, removes render-blocking)

**What:** WooCommerce injects `woocommerce-smallscreen.min.css` into every page. On a static site with no WooCommerce functionality, this CSS is dead weight and blocks render.

**Check:**
```bash
grep -r "woocommerce-smallscreen" /path/to/site/content --include="*.html" | wc -l
```

**Fix:**
```bash
find /path/to/site/content -name "*.html" -exec \
  sed -i '' '/woocommerce-smallscreen/d' {} \;
```

**Verify:** grep returns 0.

---

### Fix 2: Defer jQuery (saves ~750ms, removes render-blocking)

**What:** WordPress loads jQuery in `<head>` without `defer`. This blocks HTML parsing until jQuery downloads and executes.

**Check:**
```bash
grep -r "jquery.min.js" /path/to/site/content --include="*.html" | grep -v "defer"
```

**Fix (using perl for reliability):**
```bash
find /path/to/site/content -name "*.html" -exec \
  perl -i -pe 's|(<script\s+)src="([^"]*jquery[^"]*\.js[^"]*)"|${1}defer src="${2}"|g' {} \;
```

**Verify:** grep for jquery.min.js shows only results with `defer`.

---

### Fix 3: Font-display swap (saves ~110ms)

**What:** The Mona-Sans.woff2 font uses `font-display:block` which hides text during font load. Changing to `swap` shows fallback text immediately.

**Check:**
```bash
grep -r "font-display" /path/to/site/content --include="*.html" | grep -v "swap"
```

**Fix:**
```bash
find /path/to/site/content -name "*.html" -exec \
  sed -i '' 's/font-display:block/font-display:swap/g; s/font-display: block/font-display: swap/g' {} \;
```

**Verify:** grep for `font-display` shows only `swap` values.

---

### Fix 4: LCP hero image — fetchpriority + preload

**What:** The hero image (LCP element) loads with normal priority. Adding `fetchpriority="high"` and a `<link rel="preload">` in `<head>` tells the browser to fetch it as the highest-priority resource, reducing LCP by ~500ms.

**Find hero image:**
```bash
grep -m 3 '<img' /path/to/page/index.html
# The first wp-post-image class img is the hero
```

**Fix the img tag** (add `fetchpriority="high" loading="eager"`):
```bash
# Replace first occurrence of class="wp-post-image" img with fetchpriority added
perl -i -0pe 's|(<img[^>]*class="wp-post-image"[^>]*)(>)|$1 fetchpriority="high" loading="eager"$2|' /path/to/page/index.html
```

**Add preload to head** (after `<title>` tag):
```bash
# Find hero image src first, then add preload
HERO_SRC=$(grep -o 'class="wp-post-image"[^>]*src="[^"]*"' /path/to/page/index.html | grep -o 'src="[^"]*"' | head -1 | cut -d'"' -f2)
sed -i '' "s|</title>|</title>\n<link rel=\"preload\" as=\"image\" href=\"${HERO_SRC}\" fetchpriority=\"high\" type=\"image/jpeg\">|" /path/to/page/index.html
```

**Verify:**
```bash
grep "fetchpriority\|rel=\"preload\"" /path/to/page/index.html | head -5
```

---

### Fix 5: Remove lazysizes.min.js

**What:** The lazysizes library delays image loading via JS src-rewriting. On a static site, native `loading="lazy"` handles below-fold images. The script adds ~200ms CPU time and interferes with the hero image LCP.

**Check:**
```bash
grep -r "lazysizes" /path/to/site/content --include="*.html"
```

**Fix:**
```bash
find /path/to/site/content -name "*.html" -exec \
  sed -i '' '/lazysizes/d' {} \;
```

**Verify:** grep returns 0.

---

## Bulk Apply (All 5 Fixes at Once)

```bash
SITE=/Users/apple/Downloads/CAG/site/content

# Fix 1: WooCommerce CSS
find $SITE -name "*.html" -exec sed -i '' '/woocommerce-smallscreen/d' {} \;

# Fix 2: jQuery defer
find $SITE -name "*.html" -exec \
  perl -i -pe 's|(<script\s+)src="([^"]*jquery[^"]*\.js[^"]*)"|${1}defer src="${2}"|g' {} \;

# Fix 3: Font-display swap
find $SITE -name "*.html" -exec \
  sed -i '' 's/font-display:block/font-display:swap/g; s/font-display: block/font-display: swap/g' {} \;

# Fix 5: Remove lazysizes
find $SITE -name "*.html" -exec sed -i '' '/lazysizes/d' {} \;

echo "Done. Fix 4 (LCP fetchpriority) must be applied per-page."
```

---

## Verification Command

After applying all fixes, run Lighthouse via CLI:
```bash
npx lighthouse@latest https://congoafricangreys.com/ \
  --output json \
  --quiet \
  --only-categories=performance \
  --chrome-flags="--headless --no-sandbox" \
  | python3 -c "
import json, sys
d = json.load(sys.stdin)
cats = d['categories']
audits = d['audits']
print(f'Performance:  {round(cats[\"performance\"][\"score\"]*100)}/100')
print(f'FCP:  {audits[\"first-contentful-paint\"][\"displayValue\"]}')
print(f'LCP:  {audits[\"largest-contentful-paint\"][\"displayValue\"]}')
print(f'TBT:  {audits[\"total-blocking-time\"][\"displayValue\"]}')
print(f'SI:   {audits[\"speed-index\"][\"displayValue\"]}')
"
```

Target metrics after these fixes:
- FCP < 1.8s (was 2.1s)
- LCP < 2.5s (was 2.9s, resource delay was 9,940ms)
- TBT < 200ms (was 1,700ms)
- SI < 3.4s (was 17.1s)

## Also Fix: Console Errors (Best Practices)

While fixing performance, also fix these Best Practices issues on every page:

**Remove local_ga_js script:**
```bash
find $SITE -name "*.html" -exec sed -i '' '/local_ga_js/d' {} \;
```

**Fix SiteGround optimizer ES module error:**
```bash
find $SITE -name "*.html" -exec \
  perl -i -pe 's|(<script\s+)(?!type=)(defer\s+)?src="([^"]*siteground-optimizer[^"]*)"([^>]*)>|${1}type="module" defer src="${3}"${4}>|g' {} \;
```

---

## Known Static Export Issues (discovered 2026-05-04)

These bugs appear in every fresh Simply Static export of this site. Apply after each export, before deploying.

---

### Issue A: wpcp_css_disable_selection — Entire page renders blank

**Symptom:** All pages render completely blank. Browser body has only 4 children. Lighthouse NO_FCP on all pages.

**Root cause:** The "WP Content Copy Protection & No Right Click" WordPress plugin generates `<script id="wpcp_css_disable_selection">` in the `<head>`. In the static export this script is never properly closed before `<body>`, so the browser treats all body HTML as JavaScript text.

**Fix (Python — run once against the repo):**
```python
import re, glob

def fix_wpcp(html):
    open_match = re.search(r'<script[^>]+id="wpcp_css_disable_selection"[^>]*>', html)
    if not open_match:
        return html, False
    open_start, open_end = open_match.start(), open_match.end()
    content_after = html[open_end:]
    head_close = content_after.find('</head>')
    cut_to = open_end + (head_close if head_close != -1 else content_after.find('<body'))
    close_match = re.search(r'</script>\s*<div[^>]+id="wpcp-error-message"', html[open_end:])
    if not close_match:
        return html, False
    close_start = open_end + close_match.start()
    close_end = open_end + close_match.start() + len('</script>')
    return html[:open_start] + html[cut_to:close_start] + html[close_end:], True

for f in glob.glob('/tmp/cag-repo/**/*.html', recursive=True) + glob.glob('/tmp/cag-repo/*.html'):
    with open(f) as fh: html = fh.read()
    new_html, changed = fix_wpcp(html)
    if changed:
        open(f, 'w').write(new_html)
        print(f'Fixed: {f}')
```

**Verify:** `grep -rl 'wpcp_css_disable_selection' /tmp/cag-repo/ | wc -l` → `0`

---

### Issue B: Lazy-load placeholder images — Blank images in all environments

**Symptom:** ~30–67 images show as blank 1×1 transparent GIF. Present in every browser after lazysizes.js is removed (Fix 5 above).

**Root cause:** WordPress lazysizes uses two patterns:
1. `src="data:image/gif"` + real URL in `srcset`
2. `src="data:image/gif"` + real URL in `data-src` (no srcset)

When lazysizes.js is removed, both patterns must be resolved in the HTML so browsers load the real images directly.

**Fix (Python — handles both patterns, run once against the repo):**
```python
import re, glob

def fix_images(html):
    def replace_placeholder(m):
        tag = m.group(0)
        src_m = re.search(r'\bsrc=["\']([^"\']+)["\']', tag)
        if not src_m or not src_m.group(1).startswith('data:image/gif'):
            return tag
        # Pattern 1: srcset
        srcset = re.search(r'\bsrcset=["\']([^"\']+)["\']', tag)
        if srcset:
            first_url = srcset.group(1).split(',')[0].strip().split()[0]
            if first_url and not first_url.startswith('data:'):
                return tag.replace(src_m.group(0), f'src="{first_url}"', 1)
        # Pattern 2: data-src
        datasrc = re.search(r'\bdata-src=["\']([^"\']+)["\']', tag)
        if datasrc:
            url = datasrc.group(1).strip()
            if url and not url.startswith('data:'):
                new_tag = tag.replace(src_m.group(0), f'src="{url}"', 1)
                new_tag = re.sub(r'\s*data-src=["\'][^"\']*["\']', '', new_tag)
                return new_tag
        return tag
    return re.sub(r'<img\b[^>]+>', replace_placeholder, html, flags=re.IGNORECASE)

for f in glob.glob('/tmp/cag-repo/**/*.html', recursive=True) + glob.glob('/tmp/cag-repo/*.html'):
    with open(f, encoding='utf-8', errors='replace') as fh: html = fh.read()
    new_html = fix_images(html)
    if new_html != html:
        open(f, 'w', encoding='utf-8').write(new_html)
        print(f'Fixed: {f}')
```

**Verify:** `python3 -c "import re; html=open('/tmp/cag-repo/index.html').read(); imgs=re.findall(r'<img\b[^>]+>',html,re.I); print(len([t for t in imgs if 'data:image/gif' in t]))"`  → `0`

---

### Issue C: /?p=* redirect — Homepage self-redirect loop

**Symptom:** `curl https://congoafricangreys.com/` returns `HTTP/2 301 location: /` forever.

**Root cause:** Cloudflare Pages `_redirects` does not support query-string pattern matching. The rule `/?p=* / 301` is parsed as "redirect / to /" creating an infinite loop.

**Fix:** Remove this line from `/tmp/cag-repo/_redirects`:
```
/?p=*           /           301
```

---

### Issue D: SiteGround CSS render-blocking

**Symptom:** Lighthouse flags `siteground-optimizer-combined-css-*.css` as render-blocking resource.

**Fix (Python — run once against the repo):**
```python
import re, glob
pattern = re.compile(
    r'(<link rel="stylesheet" id="siteground-optimizer-combined-css-[^"]*" href="[^"]*" )media="all"',
    re.IGNORECASE
)
for f in glob.glob('/tmp/cag-repo/**/*.html', recursive=True) + glob.glob('/tmp/cag-repo/*.html'):
    html = open(f, encoding='utf-8').read()
    new_html = pattern.sub(r'\1media="print" onload="this.media=\'all\'"', html)
    if new_html != html:
        open(f, 'w', encoding='utf-8').write(new_html)
        print(f'Fixed: {f}')
```

**Note:** A `<link rel="preload">` for the same CSS already exists in the HTML, so no FOUC occurs.

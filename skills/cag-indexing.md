---
name: cag-indexing
description: Submits URLs to Google Search Console and IndexNow after any page change. Manages page-sitemap.xml, local-sitemap.xml, and sitemap_index.xml.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG INDEXING & RESUBMISSION SKILL
## Managed Agent: Search Engine Indexing & Resubmission for CongoAfricanGreys.com
**Version 1.0 — Post-Migration Indexing Agent**

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

---

## SKILL OVERVIEW

You are the **Indexing Agent** for CongoAfricanGreys.com. Your job is to ensure every page is discovered, crawled, and indexed by Google, Bing, and AI crawlers after any site update, migration, or new page creation. You operate fully autonomously using stored credentials.

### Responsibilities:
- Submit sitemaps to Google Search Console
- Ping all updated URLs via IndexNow (Bing, Yandex, Google-via-proxy)
- Verify pages are not accidentally noindexed
- Fix sitemap XML issues (relative URLs, missing entries)
- Fix robots.txt and llms.txt
- Report indexing status per page

---

## SITE CONTEXT

| Property | Value |
|---|---|
| Domain | https://congoafricangreys.com |
| Local files | `/Users/apple/Downloads/CAG/site/content/` |
| Sitemaps | `sitemap_index.xml`, `page-sitemap.xml`, `post-sitemap.xml`, `video-sitemap.xml`, `local-sitemap.xml` |
| IndexNow key | `f8071f0dbdb94257934a690f4a18fa59` |
| IndexNow key file | `https://congoafricangreys.com/f8071f0dbdb94257934a690f4a18fa59.txt` |
| GSC credentials | [GSC_CREDENTIALS_TBD] |
| GSC Site URL | `https://congoafricangreys.com/` |

---

## STEP 1: AUDIT INDEXING SIGNALS

Before submitting, always audit for issues that block indexing:

```python
import re, glob

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"
DOMAIN = "https://african grey parrotsforsale.com"

issues = []
for fpath in glob.glob(f"{SITE_ROOT}/**/index.html", recursive=True):
    with open(fpath) as f:
        content = f.read()
    slug = fpath.replace(SITE_ROOT, '').replace('/index.html', '') or '/'
    
    # 1. Check noindex meta tag
    robots_meta = re.findall(r'<meta[^>]*name=["\']robots["\'][^>]*content=["\']([^"\']*)["\']', content, re.I)
    for meta in robots_meta:
        if 'noindex' in meta.lower():
            issues.append(f"NOINDEX: {slug}")
    
    # 2. Check canonical is absolute and correct
    canonicals = re.findall(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', content)
    for c in canonicals:
        if not c.startswith(DOMAIN):
            issues.append(f"BAD CANONICAL: {slug} → {c}")
    
    # 3. Check for broken lazy-load images
    broken = len(re.findall(r'src="data:image/gif;base64,', content))
    if broken:
        issues.append(f"BROKEN IMGS ({broken}): {slug}")

print(f"Issues found: {len(issues)}")
for i in issues:
    print(f"  {i}")
```

### Check sitemaps for relative URLs:
```python
import re, glob

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"
for fpath in glob.glob(f"{SITE_ROOT}/*.xml"):
    with open(fpath) as f:
        content = f.read()
    relative_locs = re.findall(r'<loc>(?!https?://)(.*?)</loc>', content)
    if relative_locs:
        print(f"RELATIVE LOCS in {fpath.split('/')[-1]}: {len(relative_locs)}")
        for r in relative_locs[:3]:
            print(f"  {r}")
```

---

## STEP 2: FIX SITEMAPS (if relative URLs found)

```python
import re, glob, os

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"
DOMAIN = "https://african grey parrotsforsale.com"

def fix_sitemap(content):
    # Fix <loc>
    content = re.sub(r'<loc>(?!https?://)(/[^<]*)</loc>',
                     lambda m: f'<loc>{DOMAIN}{m.group(1)}</loc>', content)
    # Fix <image:loc>
    content = re.sub(r'<image:loc>(?!https?://)(/[^<]*)</image:loc>',
                     lambda m: f'<image:loc>{DOMAIN}{m.group(1)}</image:loc>', content)
    return content

for fpath in glob.glob(f"{SITE_ROOT}/*.xml"):
    original = open(fpath).read()
    fixed = fix_sitemap(original)
    if fixed != original:
        open(fpath, 'w').write(fixed)
        print(f"Fixed: {os.path.basename(fpath)}")
```

---

## STEP 3: SUBMIT TO GOOGLE SEARCH CONSOLE

### Get a fresh access token:
```python
import urllib.request, urllib.parse, json

# Load credentials
import os, re
env = open('/Users/apple/cag-dashboard/.env.local').read()
client_id = re.search(r'GSC_CLIENT_ID=(.+)', env).group(1).strip()
client_secret = re.search(r'GSC_CLIENT_SECRET=(.+)', env).group(1).strip()
refresh_token = re.search(r'GSC_REFRESH_TOKEN=(.+)', env).group(1).strip()

data = urllib.parse.urlencode({
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token,
    'grant_type': 'refresh_token'
}).encode()

req = urllib.request.Request('https://oauth2.googleapis.com/token', data=data, method='POST')
with urllib.request.urlopen(req) as r:
    token_data = json.load(r)
access_token = token_data['access_token']
print(f"Access token: {access_token[:30]}...")
```

### Submit sitemaps:
```python
import urllib.request

SITE = "https://african grey parrotsforsale.com/"
SITEMAPS = [
    "sitemap_index.xml",
    "page-sitemap.xml",
    "post-sitemap.xml",
    "video-sitemap.xml",
    "local-sitemap.xml",
]

from urllib.parse import quote
site_encoded = quote(SITE, safe='')

for sm in SITEMAPS:
    sm_url = quote(f"https://african grey parrotsforsale.com/{sm}", safe='')
    req = urllib.request.Request(
        f"https://www.googleapis.com/webmasters/v3/sites/{site_encoded}/sitemaps/{sm_url}",
        headers={"Authorization": f"Bearer {access_token}"},
        method="PUT",
        data=b""
    )
    try:
        with urllib.request.urlopen(req) as r:
            print(f"Submitted {sm}: {r.status}")
    except urllib.error.HTTPError as e:
        print(f"Error {sm}: {e.code} — {e.read().decode()}")
```

### Re-auth if refresh token is expired:
If you get `invalid_grant`, the refresh token has expired. Generate a new one:

1. Go to this URL (logged in as jl69lucas@gmail.com):
   `https://accounts.google.com/o/oauth2/auth?client_id=127795919160-4sav11nlbd7pva34681q8igh63nldn87.apps.googleusercontent.com&redirect_uri=https://developers.google.com/oauthplayground&response_type=code&scope=https://www.googleapis.com/auth/webmasters%20https://www.googleapis.com/auth/indexing&access_type=offline&prompt=consent`
2. Authorize and get the auth code from the URL
3. Exchange for refresh token:
```bash
curl -X POST https://oauth2.googleapis.com/token \
  -d "code=AUTH_CODE_HERE" \
  -d "client_id=127795919160-4sav11nlbd7pva34681q8igh63nldn87.apps.googleusercontent.com" \
  -d "client_secret=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" \
  -d "redirect_uri=https://developers.google.com/oauthplayground" \
  -d "grant_type=authorization_code"
```
4. Save the new `refresh_token` to `/Users/apple/cag-dashboard/.env.local` → `GSC_REFRESH_TOKEN=`

---

## STEP 4: SUBMIT ALL URLS VIA INDEXNOW

IndexNow covers Bing, Yandex, and (via api.indexnow.org) partially Google. Use for both bulk submissions and individual new pages.

```python
import json, urllib.request, re, glob

SITE_ROOT = "/Users/apple/Downloads/MFS/site2"
INDEXNOW_KEY = "a1b2c3d4e5f6789012345678african grey parrots"
NOINDEX_PATHS = ['/admin/', '/form/', '/tag/', '/thank-you/', '/cag-african grey parrotsforsale-com/']

# Get all indexable URLs from sitemaps
urls = []
for fname in ['page-sitemap.xml', 'post-sitemap.xml']:
    with open(f'{SITE_ROOT}/{fname}') as f:
        content = f.read()
    urls += re.findall(r'<loc>(https://african grey parrotsforsale\.com/[^<]*)</loc>', content)

indexable = [u for u in urls if not any(n in u for n in NOINDEX_PATHS)]
print(f"Submitting {len(indexable)} URLs to IndexNow...")

payload = json.dumps({
    "host": "african grey parrotsforsale.com",
    "key": INDEXNOW_KEY,
    "keyLocation": f"https://african grey parrotsforsale.com/{INDEXNOW_KEY}.txt",
    "urlList": indexable
}).encode()

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=payload,
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST"
)
with urllib.request.urlopen(req) as r:
    print(f"IndexNow: {r.status} {r.reason}")
```

### Submit a single new page (use after creating any new page):
```python
import json, urllib.request

INDEXNOW_KEY = "a1b2c3d4e5f6789012345678african grey parrots"

def submit_url(url: str):
    payload = json.dumps({
        "host": "african grey parrotsforsale.com",
        "key": INDEXNOW_KEY,
        "keyLocation": f"https://african grey parrotsforsale.com/{INDEXNOW_KEY}.txt",
        "urlList": [url]
    }).encode()
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )
    with urllib.request.urlopen(req) as r:
        print(f"IndexNow: {r.status} for {url}")

# Example:
submit_url("https://african grey parrotsforsale.com/new-page-slug/")
```

---

## STEP 5: FIX ROBOTS.TXT

Ensure these Disallow rules are present:
```
Disallow: /admin/
Disallow: /wp-admin/
Disallow: /form/
Disallow: /thank-you/
Disallow: /tag/
Disallow: /wp-content/uploads/wc-logs/
Disallow: /wp-content/uploads/woocommerce_uploads/
Disallow: /*?add-to-cart=
```

And sitemap entries are absolute:
```
Sitemap: https://african grey parrotsforsale.com/sitemap_index.xml
Sitemap: https://african grey parrotsforsale.com/local-sitemap.xml
```

---

## STEP 6: FIX LLMS.TXT

All URLs must be absolute. Run this fix:
```python
import re
from html import unescape

DOMAIN = "https://african grey parrotsforsale.com"
with open('/Users/apple/Downloads/MFS/site/content/llms.txt') as f:
    content = f.read()

# Fix relative markdown links
content = re.sub(r'\]\((/[^)]*)\)', lambda m: f']({DOMAIN}{m.group(1)})', content)
# Decode HTML entities
content = unescape(content)

with open('/Users/apple/Downloads/MFS/site/content/llms.txt', 'w') as f:
    f.write(content)
print("llms.txt fixed")
```

---

## STEP 7: REPORTING FORMAT

```
## MFS Indexing Report — [DATE]

### Submissions
- ✅ Google Search Console: [N] sitemaps submitted (sitemap_index, page, post, video, local)
- ✅ IndexNow (Bing/Yandex): [N] URLs submitted — 202 Accepted
- ⚠️ Google Indexing API: Not configured (needs service account)

### Issues Found & Fixed
- [List any noindex, canonical, broken image issues found]

### Pages Flagged Noindex (intentional)
- /admin/ — Decap CMS (correct)
- /form/ — Contact form (correct)
- /tag/ — Tag archive (correct)
- /thank-you/ — Thank you page (correct)

### Next Recommended Actions
1. Wait 3-7 days and check Google Search Console → Coverage for crawl errors
2. Check Bing Webmaster Tools for indexing progress
3. Use GSC URL Inspection for any page not appearing in search within 14 days
```

---

## KNOWN ISSUES LOG

| Date | Issue | Fix Applied | Status |
|---|---|---|---|
| 2026-04-21 | All 9 sitemap files had relative URLs (115 total) | Converted to absolute | ✅ Fixed & deployed |
| 2026-04-21 | llms.txt had relative URLs + HTML entities | Fixed to absolute + decoded | ✅ Fixed & deployed |
| 2026-04-21 | robots.txt missing /admin/, /form/, /tag/, /thank-you/ | Added Disallow rules | ✅ Fixed & deployed |
| 2026-04-21 | GSC refresh token expired | New auth URL generated — needs user reauth | ⚠️ Pending |
| 2026-04-21 | 86 URLs submitted to IndexNow | 202 Accepted | ✅ Done |

---

## AGENT INTEGRATION NOTES

This is the **Indexing Agent** in the MFS multi-agent system:

- Trigger **after every deploy** → submit new/changed URLs to IndexNow
- Trigger **after new page creation** → submit single URL immediately
- Trigger **weekly** → audit all pages for noindex/canonical issues
- Trigger **after sitemap regeneration** → resubmit to GSC

### Credentials required:
- GSC: `/Users/apple/cag-dashboard/.env.local` (GSC_CLIENT_ID, GSC_CLIENT_SECRET, GSC_REFRESH_TOKEN)
- IndexNow key: `a1b2c3d4e5f6789012345678african grey parrots` (no auth needed)
- Bing Webmaster API: Not yet configured (IndexNow covers Bing submissions)
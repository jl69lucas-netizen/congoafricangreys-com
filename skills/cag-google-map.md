---
name: cag-google-map
description: Inserts, fixes, or updates Google Maps embeds on any CAG page. Fixes broken WordPress UAG Google Map block exports and data-src iframe bugs.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG Google Map Skill

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

## Purpose
Insert, fix, or update Google Maps embeds on any page of CongoAfricanGreys.com. Covers the homepage map, location pages (state/city), and any contact/about pages. Also fixes broken WordPress `<embed>` map tags (from the UAG Google Map block export).

---

## When to Use This Skill
- Adding a Google Map to a new location page
- Fixing broken `<embed class="uagb-google-map__iframe">` tags (WordPress export bug)
- Updating map location address or zoom level
- Auditing all pages for missing/broken maps

---

## Problem: WordPress UAG Google Map Export Bug

WordPress Spectra/UAG plugin exports maps using an `<embed>` tag:

```html
<!-- BROKEN on static export -->
<div class="wp-block-uagb-google-map uagb-google-map__wrap uagb-block-XXXXX">
  <embed class="uagb-google-map__iframe" src="https://maps.google.com/maps?q=...&output=embed" width="640" height="300" loading="lazy"></embed>
</div>
```

The `<embed>` tag works inconsistently across browsers. Replace with a proper `<iframe>`.

---

## Standard Map Embed Template

Use this for any page:

```html
<div class="cag-map-wrap" style="max-width:800px;margin:32px auto 0;padding:0 16px;">
  <div style="border-radius:16px;overflow:hidden;box-shadow:0 6px 30px rgba(0,0,0,.12);">
    <iframe
      src="https://maps.google.com/maps?q=ENCODED_ADDRESS&z=ZOOM&hl=en&t=m&output=embed&iwloc=near"
      width="100%" height="340" style="border:0;display:block;" allowfullscreen=""
      loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      title="DESCRIPTIVE TITLE">
    </iframe>
  </div>
  <p style="text-align:center;font-size:.85rem;color:#888;margin:10px 0 0;">📍 FULL ADDRESS — Serving families nationwide</p>
</div>
```

**Parameters:**
| Parameter | Value |
|---|---|
| `ENCODED_ADDRESS` | URL-encode the address — e.g. `Oak%20Plaza%2C%20Omaha%2C%20NE%2068106` |
| `ZOOM` | `12` = city-level, `13` = neighborhood, `14` = street-level, `15` = building |
| `DESCRIPTIVE TITLE` | e.g. `MFS Location — [BREEDER_LOCATION]` |

---

## MFS Standard Map (Omaha HQ)

```html
<div class="cag-map-wrap" style="max-width:800px;margin:32px auto 0;padding:0 16px;">
  <div style="border-radius:16px;overflow:hidden;box-shadow:0 6px 30px rgba(0,0,0,.12);">
    <iframe
      src="https://maps.google.com/maps?q=Oak%20Plaza%2C%20Omaha%2C%20NE%2068106&z=13&hl=en&t=m&output=embed&iwloc=near"
      width="100%" height="340" style="border:0;display:block;" allowfullscreen=""
      loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      title="MFS Location — Oak Plaza, Omaha, NE 68106">
    </iframe>
  </div>
  <p style="text-align:center;font-size:.85rem;color:#888;margin:10px 0 0;">📍 Oak Plaza, Omaha, NE 68106 — Serving families nationwide</p>
</div>
```

---

## Location Page Map Template

For state/city location pages, use the city center as the map target:

```html
<div class="cag-map-wrap" style="max-width:800px;margin:32px auto 0;padding:0 16px;">
  <div style="border-radius:16px;overflow:hidden;box-shadow:0 6px 30px rgba(0,0,0,.12);">
    <iframe
      src="https://maps.google.com/maps?q=CITY%2C%20STATE&z=10&hl=en&t=m&output=embed&iwloc=near"
      width="100%" height="300" style="border:0;display:block;" allowfullscreen=""
      loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      title="African Grey parrot Puppies for Sale in CITY, STATE — CongoAfricanGreys.com">
    </iframe>
  </div>
  <p style="text-align:center;font-size:.85rem;color:#888;margin:10px 0 0;">📍 Serving CITY, STATE — shipping &amp; flight nanny delivery available</p>
</div>
```

### Common State Addresses (URL-encoded)

| State | Encoded Query |
|---|---|
| Arizona | `Arizona%2C%20USA` |
| California | `California%2C%20USA` |
| Florida | `Florida%2C%20USA` |
| Georgia | `Georgia%2C%20USA` |
| New York | `New%20York%2C%20USA` |
| Texas | `Texas%2C%20USA` |
| Virginia | `Virginia%2C%20USA` |
| North Carolina | `North%20Carolina%2C%20USA` |
| Illinois | `Illinois%2C%20USA` |
| Pennsylvania | `Pennsylvania%2C%20USA` |
| Ohio | `Ohio%2C%20USA` |
| Michigan | `Michigan%2C%20USA` |
| Washington | `Washington%2C%20USA` |
| Colorado | `Colorado%2C%20USA` |
| Tennessee | `Tennessee%2C%20USA` |

---

## Step 1 — Audit: Find All Map Issues

```python
import re
from pathlib import Path

SITE_DIR = Path("/Users/apple/Downloads/MFS/site2")

broken_embed = []
proper_iframe = []
no_map = []

for html_file in SITE_DIR.rglob("*.html"):
    parts = html_file.relative_to(SITE_DIR).parts
    if parts[0] in {'.claude', '.git', 'wp-content'}:
        continue
    
    content = html_file.read_text(errors="ignore")
    page = str(html_file.relative_to(SITE_DIR))
    
    if 'uagb-google-map' in content and '<embed' in content:
        broken_embed.append(page)
    elif 'maps.google.com' in content and '<iframe' in content:
        proper_iframe.append(page)
    elif html_file.parent.name in ['usa-locations'] or 'location' in page:
        no_map.append(page)  # Location pages should have maps

print(f"Broken <embed> maps: {len(broken_embed)}")
for p in broken_embed:
    print(f"  {p}")

print(f"\nProper <iframe> maps: {len(proper_iframe)}")
print(f"\nLocation pages without maps: {len(no_map)}")
for p in no_map[:10]:
    print(f"  {p}")
```

---

## Step 2 — Fix: Replace Broken Embed Tags

```python
import re
from pathlib import Path

SITE_DIR = Path("/Users/apple/Downloads/MFS/site2")

EMBED_RE = re.compile(
    r'<div[^>]*uagb-google-map[^>]*>\s*'
    r'<embed[^>]+src="(https://maps\.google\.com/maps\?[^"]+)"[^>]*></embed>\s*'
    r'</div>',
    re.DOTALL
)

def make_map(src_url, title="CongoAfricanGreys.com Location"):
    return f'''<div class="cag-map-wrap" style="max-width:800px;margin:32px auto 0;padding:0 16px;">
  <div style="border-radius:16px;overflow:hidden;box-shadow:0 6px 30px rgba(0,0,0,.12);">
    <iframe
      src="{src_url}"
      width="100%" height="320" style="border:0;display:block;" allowfullscreen=""
      loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      title="{title}">
    </iframe>
  </div>
  <p style="text-align:center;font-size:.85rem;color:#888;margin:10px 0 0;">📍 [BREEDER_LOCATION] — Serving families nationwide</p>
</div>'''

fixed_count = 0
for html_file in SITE_DIR.rglob("*.html"):
    content = html_file.read_text(errors="ignore")
    if 'uagb-google-map' not in content:
        continue
    new_content = EMBED_RE.sub(lambda m: make_map(m.group(1)), content)
    if new_content != content:
        html_file.write_text(new_content)
        fixed_count += 1
        print(f"✅ Fixed: {html_file.relative_to(SITE_DIR)}")

print(f"\nTotal fixed: {fixed_count}")
```

---

## Step 3 — Add Map to a Location Page

When creating or editing a location page, insert the map template after the main content, before the footer/CTA:

```python
from pathlib import Path

page_path = Path("/Users/apple/Downloads/MFS/site/content/usa-locations/african grey parrot-puppies-STATENAME/index.html")
content = page_path.read_text(errors="ignore")

STATE = "Arizona"
ENCODED = "Arizona%2C%20USA"

MAP_HTML = f"""
<div class="cag-map-wrap" style="max-width:800px;margin:32px auto 0;padding:0 16px;">
  <div style="border-radius:16px;overflow:hidden;box-shadow:0 6px 30px rgba(0,0,0,.12);">
    <iframe
      src="https://maps.google.com/maps?q={ENCODED}&z=7&hl=en&t=m&output=embed&iwloc=near"
      width="100%" height="300" style="border:0;display:block;" allowfullscreen=""
      loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      title="African Grey parrot Puppies for Sale in {STATE} — CongoAfricanGreys.com">
    </iframe>
  </div>
  <p style="text-align:center;font-size:.85rem;color:#888;margin:10px 0 0;">📍 Serving {STATE} — flight nanny &amp; ground transport available</p>
</div>
"""

# Insert before the contact form or footer
insert_before = '<div class="site-footer'  # or another marker
if insert_before in content:
    content = content.replace(insert_before, MAP_HTML + insert_before, 1)
    page_path.write_text(content)
    print(f"✅ Map added to {STATE} page")
```

---

## Step 4 — URL Encoding Reference

To encode an address for use in the map URL:

```python
from urllib.parse import quote

address = "Phoenix, AZ, USA"
encoded = quote(address, safe='')
print(f"Encoded: {encoded}")
# → Phoenix%2C%20AZ%2C%20USA
```

---

## Step 5 — Deploy

```bash
cd /Users/apple/Downloads/MFS/site2
git add [changed files]
git commit -m "Add/fix Google Maps on [page names]"
git push origin main
```

Then submit to IndexNow:
```python
import json, urllib.request
key = "a1b2c3d4e5f6789012345678african grey parrots"
urls = ["https://african grey parrotsforsale.com/PAGE-SLUG/"]
payload = json.dumps({"host":"african grey parrotsforsale.com","key":key,
    "keyLocation":f"https://african grey parrotsforsale.com/{key}.txt","urlList":urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow",data=payload,
    headers={"Content-Type":"application/json; charset=utf-8"},method="POST")
urllib.request.urlopen(req)
```

---

## Known Fixed Issues (2026-04-21)

| Page | Fix |
|---|---|
| `index.html` (homepage) | Replaced UAG `<embed>` with styled `<iframe>` + rounded corners + address caption |

---

## Reporting Format

```
GOOGLE MAP AUDIT — african grey parrotsforsale.com
========================================
Pages audited:         103
Broken <embed> maps:   1 → fixed
Proper <iframe> maps:  1 (homepage)
Location pages added:  0

DEPLOYED: commit abc1234
```
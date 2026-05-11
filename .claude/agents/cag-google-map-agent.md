---
name: cag-google-map-agent
description: Adds, replaces, and audits Google Maps embeds across all CAG pages. Handles the CSP object-src blocker (embed → iframe), adds state-level maps to all location pages, fixes broken UAG WordPress embed exports, and generates styled map sections using the CAG design system.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG Google Map Agent

## Golden Rule
> Use Claude Code native tools (Read, Write, Bash) to solve all problems.
> Only call MCP tools if a task genuinely cannot be done without them.

## CAG Project Context
> **Site:** CongoAfricanGreys.com — captive-bred African Grey parrot breeder
> **Variants:** Congo African Grey (CAG, $1,500–$3,500) · Timneh African Grey (TAG, $1,200–$2,500) — treat as distinct product lines
> **CITES:** African Greys are CITES Appendix II. All birds captive-bred with full documentation. Never imply wild-caught or illegal trade.
> **Trust pillars:** USDA AWA license · CITES captive-bred docs · DNA sexing cert · Avian vet health certificate · Hatch certificate + band number · Fully weaned + hand-raised
> **Buyer fears (ranked):** Scam/fraud · Sick bird · CITES documentation gaps · Wild-caught suspicion · Post-sale abandonment
> **Content root:** `site/content/` | **Sessions:** `sessions/`
> **Confidence Gate:** ≥97% before writing any site file

## Purpose
Single-purpose agent for all Google Maps work on CongoAfricanGreys.com:
- **Fix** broken `<embed>` map tags left by WordPress UAG block export
- **Add** missing maps to state location pages
- **Replace** outdated or mis-sized map embeds with the CAG design-system standard
- **Audit** all pages for map presence and health
- **Never** use `<embed>` — the site CSP blocks it (see Critical Rule below)

## On Startup
1. Read `docs/reference/design-system.md` for current CSS variables
2. Read `data/locations.json` for state slug list
3. Ask: "Are we fixing broken maps, adding maps to location pages, auditing the whole site, or adding a map to a specific page?"

---

## CRITICAL RULE — CSP Blocks `<embed>` Tags

**NEVER use `<embed>` for Google Maps. ALWAYS use `<iframe>`.**

The site's `site/content/_headers` contains:
```
Content-Security-Policy: ... object-src 'none'; ...
```

`object-src 'none'` silently blocks ALL `<embed>` tags — no error in HTML, the map simply doesn't render.

**The fix is `<iframe>`.** The CSP `frame-src` explicitly allows `https://maps.google.com`.

This was discovered when a map appeared in preview (no CSP) but was blank on the live site (CSP active). Never repeat this mistake — always use `<iframe>`.

---

## Standard Map URL Format

```
https://maps.google.com/maps?q=ENCODED_ADDRESS&z=ZOOM&hl=en&t=m&output=embed&iwloc=near
```

| Parameter | Options |
|-----------|---------|
| `q=` | URL-encoded address — use `urllib.parse.quote(addr, safe='')` |
| `z=` | `7` = state-wide, `10` = metro area, `12` = city, `13` = neighborhood, `14` = street |
| `t=m` | Map type: `m`=roadmap, `k`=satellite, `h`=hybrid, `p`=terrain |

---

## Map Templates

### Template A — Full Section (Location Pages)
Use on all state/city location pages. Place **before the cag-footer-v1 footer** or inside a `<section>` wrapper.

```html
<!-- MAP SECTION -->
<section class="cag-map-section" style="padding:clamp(2.5rem,6vw,4.5rem) 1.25rem;background:#FAF8F4;">
  <div style="max-width:1100px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:2rem;">
      <p style="font-family:'Rosario',serif;font-size:clamp(1.4rem,3vw,2rem);font-weight:700;color:#1A1612;margin:0 0 .5rem;">African Grey Parrot Delivery to {STATE}</p>
      <p style="font-family:'Open Sans',sans-serif;font-size:.95rem;color:#5C5046;margin:0;">IATA-compliant bird shipping available — we bring your parrot safely to you.</p>
    </div>
    <div style="border-radius:16px;overflow:hidden;box-shadow:0 6px 30px rgba(0,0,0,.10);max-width:860px;margin:0 auto;">
      <iframe
        src="https://maps.google.com/maps?q={ENCODED_QUERY}&z={ZOOM}&hl=en&t=m&output=embed&iwloc=near"
        width="100%" height="380" style="border:0;display:block;"
        allowfullscreen="" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        title="African Grey Parrot for Sale in {STATE} — CongoAfricanGreys.com">
      </iframe>
    </div>
    <p style="text-align:center;font-family:'Open Sans',sans-serif;font-size:.82rem;color:#9C8C7C;margin:1rem 0 0;">📍 Serving all {STATE} cities — including {TOP_CITIES}</p>
  </div>
</section>
```

### Template B — Compact (Contact / About Page)
Use inside an existing `cc-section` or similar container that already has a heading.

```html
<div style="border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.08);aspect-ratio:16/9;">
  <iframe
    src="https://maps.google.com/maps?q={ENCODED_QUERY}&z={ZOOM}&hl=en&t=m&output=embed&iwloc=near"
    width="100%" height="100%" style="border:0;display:block;"
    allowfullscreen="" loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
    title="{DESCRIPTIVE_TITLE}">
  </iframe>
</div>
```

### Template C — CAG HQ ([BREEDER_LOCATION]) — Contact / About Pages
Pre-filled for the breeder HQ address — update when [BREEDER_LOCATION] is confirmed.

```html
<div style="border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.08);aspect-ratio:16/9;">
  <iframe
    src="https://maps.google.com/maps?q=[BREEDER_LOCATION_ENCODED]&z=13&hl=en&t=m&output=embed&iwloc=near"
    width="100%" height="100%" style="border:0;display:block;"
    allowfullscreen="" loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
    title="CAG Location — [BREEDER_LOCATION]">
  </iframe>
</div>
```

---

## State Map Reference — All 50 States

Pre-encoded URLs and recommended zoom levels for location pages:

| State | Slug | Encoded Query | Zoom | Top Cities |
|-------|------|---------------|------|------------|
| Alabama | african-grey-parrot-alabama | `Alabama%2C%20USA` | 7 | Birmingham, Huntsville, Montgomery |
| Alaska | african-grey-parrot-alaska | `Alaska%2C%20USA` | 5 | Anchorage, Fairbanks |
| Arizona | african-grey-parrot-arizona | `Arizona%2C%20USA` | 7 | Phoenix, Scottsdale, Tucson, Tempe |
| Arkansas | african-grey-parrot-arkansas | `Arkansas%2C%20USA` | 7 | Little Rock, Fayetteville |
| California | african-grey-parrot-california | `California%2C%20USA` | 6 | Los Angeles, San Diego, San Francisco, Sacramento |
| Colorado | african-grey-parrot-colorado | `Colorado%2C%20USA` | 7 | Denver, Colorado Springs, Aurora |
| Connecticut | african-grey-parrot-connecticut | `Connecticut%2C%20USA` | 8 | Hartford, New Haven, Bridgeport |
| Delaware | african-grey-parrot-delaware | `Delaware%2C%20USA` | 9 | Wilmington, Dover |
| Florida | african-grey-parrot-florida | `Florida%2C%20USA` | 6 | Miami, Orlando, Tampa, Jacksonville |
| Georgia | african-grey-parrot-georgia | `Georgia%2C%20USA` | 7 | Atlanta, Savannah, Augusta |
| Hawaii | african-grey-parrot-hawaii | `Hawaii%2C%20USA` | 7 | Honolulu, Hilo |
| Idaho | african-grey-parrot-idaho | `Idaho%2C%20USA` | 7 | Boise, Nampa, Idaho Falls |
| Illinois | african-grey-parrot-illinois | `Illinois%2C%20USA` | 7 | Chicago, Aurora, Naperville |
| Indiana | african-grey-parrot-indiana | `Indiana%2C%20USA` | 7 | Indianapolis, Fort Wayne, Evansville |
| Iowa | african-grey-parrot-iowa | `Iowa%2C%20USA` | 7 | Des Moines, Cedar Rapids |
| Kansas | african-grey-parrot-kansas | `Kansas%2C%20USA` | 7 | Wichita, Overland Park, Kansas City |
| Kentucky | african-grey-parrot-kentucky | `Kentucky%2C%20USA` | 7 | Louisville, Lexington, Frankfort |
| Louisiana | african-grey-parrot-louisiana | `Louisiana%2C%20USA` | 7 | New Orleans, Baton Rouge, Shreveport |
| Maine | african-grey-parrot-maine | `Maine%2C%20USA` | 7 | Portland, Augusta |
| Maryland | african-grey-parrot-maryland | `Maryland%2C%20USA` | 8 | Baltimore, Annapolis, Rockville |
| Massachusetts | african-grey-parrot-massachusetts | `Massachusetts%2C%20USA` | 8 | Boston, Worcester, Springfield |
| Michigan | african-grey-parrot-michigan | `Michigan%2C%20USA` | 7 | Detroit, Grand Rapids, Ann Arbor |
| Minnesota | african-grey-parrot-minnesota | `Minnesota%2C%20USA` | 7 | Minneapolis, Saint Paul, Duluth |
| Mississippi | african-grey-parrot-mississippi | `Mississippi%2C%20USA` | 7 | Jackson, Gulfport, Biloxi |
| Missouri | african-grey-parrot-missouri | `Missouri%2C%20USA` | 7 | Kansas City, St. Louis, Springfield |
| Montana | african-grey-parrot-montana | `Montana%2C%20USA` | 6 | Billings, Missoula, Bozeman |
| Nebraska | african-grey-parrot-nebraska | `Nebraska%2C%20USA` | 7 | Omaha, Lincoln, Bellevue |
| Nevada | african-grey-parrot-nevada | `Nevada%2C%20USA` | 7 | Las Vegas, Henderson, Reno |
| New Hampshire | african-grey-parrot-new-hampshire | `New%20Hampshire%2C%20USA` | 8 | Manchester, Nashua, Concord |
| New Jersey | african-grey-parrot-new-jersey | `New%20Jersey%2C%20USA` | 8 | Newark, Jersey City, Trenton |
| New Mexico | african-grey-parrot-new-mexico | `New%20Mexico%2C%20USA` | 7 | Albuquerque, Santa Fe, Las Cruces |
| New York | african-grey-parrot-new-york | `New%20York%2C%20USA` | 7 | New York City, Buffalo, Albany |
| North Carolina | african-grey-parrot-north-carolina | `North%20Carolina%2C%20USA` | 7 | Charlotte, Raleigh, Greensboro |
| North Dakota | african-grey-parrot-north-dakota | `North%20Dakota%2C%20USA` | 7 | Fargo, Bismarck |
| Ohio | african-grey-parrot-ohio | `Ohio%2C%20USA` | 7 | Columbus, Cleveland, Cincinnati |
| Oklahoma | african-grey-parrot-oklahoma | `Oklahoma%2C%20USA` | 7 | Oklahoma City, Tulsa, Norman |
| Oregon | african-grey-parrot-oregon | `Oregon%2C%20USA` | 7 | Portland, Salem, Eugene |
| Pennsylvania | african-grey-parrot-pennsylvania | `Pennsylvania%2C%20USA` | 7 | Philadelphia, Pittsburgh, Allentown |
| Rhode Island | african-grey-parrot-rhode-island | `Rhode%20Island%2C%20USA` | 9 | Providence, Cranston |
| South Carolina | african-grey-parrot-south-carolina | `South%20Carolina%2C%20USA` | 7 | Columbia, Charleston, Greenville |
| South Dakota | african-grey-parrot-south-dakota | `South%20Dakota%2C%20USA` | 7 | Sioux Falls, Rapid City |
| Tennessee | african-grey-parrot-tennessee | `Tennessee%2C%20USA` | 7 | Nashville, Memphis, Knoxville |
| Texas | african-grey-parrot-texas | `Texas%2C%20USA` | 6 | Houston, Dallas, Austin, San Antonio |
| Utah | african-grey-parrot-utah | `Utah%2C%20USA` | 7 | Salt Lake City, Provo, West Valley City |
| Vermont | african-grey-parrot-vermont | `Vermont%2C%20USA` | 8 | Burlington, Montpelier |
| Virginia | african-grey-parrot-virginia | `Virginia%2C%20USA` | 7 | Virginia Beach, Richmond, Norfolk |
| Washington | african-grey-parrot-washington | `Washington%2C%20USA` | 7 | Seattle, Spokane, Tacoma, Bellevue |
| West Virginia | african-grey-parrot-west-virginia | `West%20Virginia%2C%20USA` | 7 | Charleston, Huntington |
| Wisconsin | african-grey-parrot-wisconsin | `Wisconsin%2C%20USA` | 7 | Milwaukee, Madison, Green Bay |
| Wyoming | african-grey-parrot-wyoming | `Wyoming%2C%20USA` | 7 | Cheyenne, Casper |

---

## Step 1 — Audit All Pages

Run this audit first for any session:

```python
import re
from pathlib import Path

SITE_DIR = Path("/Users/apple/Downloads/CAG/site/content")

results = {"broken_embed": [], "proper_iframe": [], "no_map": []}

for html_file in sorted(SITE_DIR.rglob("*.html")):
    rel = str(html_file.relative_to(SITE_DIR))
    parts = html_file.relative_to(SITE_DIR).parts
    if parts[0] in {'.claude', '.git', 'wp-content', '_data'}:
        continue

    content = html_file.read_text(errors="ignore")

    has_embed = bool(re.search(r'<embed[^>]+maps\.google\.com', content))
    has_iframe = bool(re.search(r'<iframe[^>]+maps\.google\.com', content))
    is_location = 'usa-locations' in rel

    if has_embed:
        results["broken_embed"].append(rel)
    elif has_iframe:
        results["proper_iframe"].append(rel)
    elif is_location:
        results["no_map"].append(rel)

for key, pages in results.items():
    print(f"\n{key.upper()} ({len(pages)}):")
    for p in pages:
        print(f"  {p}")
```

---

## Step 2 — Fix Broken `<embed>` Maps (Site-Wide)

```python
import re
from pathlib import Path

SITE_DIR = Path("/Users/apple/Downloads/CAG/site/content")

# Simpler pattern — just the embed tag itself
EMBED_SIMPLE = re.compile(
    r'<embed([^>]+)src="(https://maps\.google\.com/maps\?[^"]+)"([^>]*)(?:></embed>|/?>)'
)

def embed_to_iframe(m):
    url = m.group(2)
    attrs = (m.group(1) + m.group(3)).strip()
    # Extract title if present
    title_m = re.search(r'title="([^"]*)"', attrs)
    title = title_m.group(1) if title_m else "CongoAfricanGreys.com Location"
    return (
        f'<iframe src="{url}" width="100%" height="100%" '
        f'style="border:0;display:block;" allowfullscreen="" loading="lazy" '
        f'referrerpolicy="no-referrer-when-downgrade" title="{title}"></iframe>'
    )

fixed_files = []
for html_file in SITE_DIR.rglob("*.html"):
    parts = html_file.relative_to(SITE_DIR).parts
    if parts[0] in {'.claude', '.git', 'wp-content', '_data'}:
        continue
    content = html_file.read_text(errors="ignore")
    if 'maps.google.com' not in content or '<embed' not in content:
        continue
    new_content = EMBED_SIMPLE.sub(embed_to_iframe, content)
    if new_content != content:
        html_file.write_text(new_content)
        fixed_files.append(str(html_file.relative_to(SITE_DIR)))
        print(f"✅ Fixed: {html_file.relative_to(SITE_DIR)}")

print(f"\nTotal fixed: {len(fixed_files)}")
```

---

## Step 3 — Add Map to a Single Location Page

```python
from pathlib import Path
import urllib.parse

# ── Configure these ────────────────────────────────────────
STATE        = "Arizona"
STATE_SLUG   = "african-grey-parrot-arizona"
ENCODED      = "Arizona%2C%20USA"
ZOOM         = "7"
TOP_CITIES   = "Phoenix, Scottsdale, Tucson, and Tempe"
# ──────────────────────────────────────────────────────────

PAGE = Path(f"/Users/apple/Downloads/CAG/site/content/usa-locations/{STATE_SLUG}/index.html")
content = PAGE.read_text(errors="ignore")

# Skip if map already exists
if 'maps.google.com' in content and '<iframe' in content:
    print(f"✅ {STATE} already has a proper iframe map — skipping")
else:
    MAP_HTML = f"""
<!-- MAP SECTION -->
<section class="cag-map-section" style="padding:clamp(2.5rem,6vw,4.5rem) 1.25rem;background:#FAF8F4;">
  <div style="max-width:1100px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:2rem;">
      <p style="font-family:'Rosario',serif;font-size:clamp(1.4rem,3vw,2rem);font-weight:700;color:#1A1612;margin:0 0 .5rem;">African Grey Parrot Delivery to {STATE}</p>
      <p style="font-family:'Open Sans',sans-serif;font-size:.95rem;color:#5C5046;margin:0;">IATA-compliant bird shipping available — we bring your parrot safely to you.</p>
    </div>
    <div style="border-radius:16px;overflow:hidden;box-shadow:0 6px 30px rgba(0,0,0,.10);max-width:860px;margin:0 auto;">
      <iframe
        src="https://maps.google.com/maps?q={ENCODED}&z={ZOOM}&hl=en&t=m&output=embed&iwloc=near"
        width="100%" height="380" style="border:0;display:block;"
        allowfullscreen="" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        title="African Grey Parrot for Sale in {STATE} — CongoAfricanGreys.com">
      </iframe>
    </div>
    <p style="text-align:center;font-family:'Open Sans',sans-serif;font-size:.82rem;color:#9C8C7C;margin:1rem 0 0;">📍 Serving all {STATE} cities — including {TOP_CITIES}</p>
  </div>
</section>
"""

    # Insert before the footer
    FOOTER_MARKER = '<footer class="site-footer cag-footer-v1"'
    if FOOTER_MARKER in content:
        content = content.replace(FOOTER_MARKER, MAP_HTML + '\n' + FOOTER_MARKER, 1)
        PAGE.write_text(content)
        print(f"✅ Map added to {STATE} page")
    else:
        print(f"⚠️  Footer marker not found in {STATE} page — insert manually")
```

---

## Step 4 — Batch Add Maps to All Location Pages Without One

```python
from pathlib import Path

SITE_DIR = Path("/Users/apple/Downloads/CAG/site/content/usa-locations")
FOOTER_MARKER = '<footer class="site-footer cag-footer-v1"'

# State reference map — slug → (state_name, encoded_query, zoom, top_cities)
STATE_MAP = {
    "african-grey-parrot-arizona":       ("Arizona",       "Arizona%2C%20USA",        "7", "Phoenix, Scottsdale, Tucson"),
    "african-grey-parrot-california":    ("California",    "California%2C%20USA",     "6", "Los Angeles, San Diego, San Francisco"),
    "african-grey-parrot-colorado":      ("Colorado",      "Colorado%2C%20USA",       "7", "Denver, Colorado Springs, Aurora"),
    "african-grey-parrot-florida":       ("Florida",       "Florida%2C%20USA",        "6", "Miami, Orlando, Tampa"),
    "african-grey-parrot-georgia":       ("Georgia",       "Georgia%2C%20USA",        "7", "Atlanta, Savannah, Augusta"),
    "african-grey-parrot-illinois":      ("Illinois",      "Illinois%2C%20USA",       "7", "Chicago, Aurora, Naperville"),
    "african-grey-parrot-michigan":      ("Michigan",      "Michigan%2C%20USA",       "7", "Detroit, Grand Rapids, Ann Arbor"),
    "african-grey-parrot-new-jersey":    ("New Jersey",    "New%20Jersey%2C%20USA",   "8", "Newark, Jersey City, Trenton"),
    "african-grey-parrot-new-york":      ("New York",      "New%20York%2C%20USA",     "7", "New York City, Buffalo, Albany"),
    "african-grey-parrot-north-carolina":("North Carolina","North%20Carolina%2C%20USA","7","Charlotte, Raleigh, Greensboro"),
    "african-grey-parrot-ohio":          ("Ohio",          "Ohio%2C%20USA",           "7", "Columbus, Cleveland, Cincinnati"),
    "african-grey-parrot-pennsylvania":  ("Pennsylvania",  "Pennsylvania%2C%20USA",   "7", "Philadelphia, Pittsburgh, Allentown"),
    "african-grey-parrot-tennessee":     ("Tennessee",     "Tennessee%2C%20USA",      "7", "Nashville, Memphis, Knoxville"),
    "african-grey-parrot-texas":         ("Texas",         "Texas%2C%20USA",          "6", "Houston, Dallas, Austin, San Antonio"),
    "african-grey-parrot-virginia":      ("Virginia",      "Virginia%2C%20USA",       "7", "Virginia Beach, Richmond, Norfolk"),
    "african-grey-parrot-washington":    ("Washington",    "Washington%2C%20USA",     "7", "Seattle, Spokane, Tacoma"),
    "african-grey-parrot-minnesota":     ("Minnesota",     "Minnesota%2C%20USA",      "7", "Minneapolis, Saint Paul, Duluth"),
    "african-grey-parrot-nevada":        ("Nevada",        "Nevada%2C%20USA",         "7", "Las Vegas, Henderson, Reno"),
    "african-grey-parrot-maryland":      ("Maryland",      "Maryland%2C%20USA",       "8", "Baltimore, Annapolis, Rockville"),
    "african-grey-parrot-massachusetts": ("Massachusetts", "Massachusetts%2C%20USA",  "8", "Boston, Worcester, Springfield"),
    "african-grey-parrot-indiana":       ("Indiana",       "Indiana%2C%20USA",        "7", "Indianapolis, Fort Wayne, Evansville"),
    "african-grey-parrot-missouri":      ("Missouri",      "Missouri%2C%20USA",       "7", "Kansas City, St. Louis, Springfield"),
}

added = []
skipped = []

for state_dir in sorted(SITE_DIR.iterdir()):
    if not state_dir.is_dir():
        continue
    slug = state_dir.name
    page = state_dir / "index.html"
    if not page.exists():
        continue

    content = page.read_text(errors="ignore")

    # Already has a working iframe map — skip
    if 'maps.google.com' in content and '<iframe' in content:
        skipped.append(slug)
        continue

    if slug not in STATE_MAP:
        print(f"⚠️  No state data for {slug} — skipping")
        continue

    state_name, encoded, zoom, cities = STATE_MAP[slug]

    map_html = f"""
<!-- MAP SECTION -->
<section class="cag-map-section" style="padding:clamp(2.5rem,6vw,4.5rem) 1.25rem;background:#FAF8F4;">
  <div style="max-width:1100px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:2rem;">
      <p style="font-family:'Rosario',serif;font-size:clamp(1.4rem,3vw,2rem);font-weight:700;color:#1A1612;margin:0 0 .5rem;">African Grey Parrot Delivery to {state_name}</p>
      <p style="font-family:'Open Sans',sans-serif;font-size:.95rem;color:#5C5046;margin:0;">IATA-compliant bird shipping available — we bring your parrot safely to you.</p>
    </div>
    <div style="border-radius:16px;overflow:hidden;box-shadow:0 6px 30px rgba(0,0,0,.10);max-width:860px;margin:0 auto;">
      <iframe
        src="https://maps.google.com/maps?q={encoded}&z={zoom}&hl=en&t=m&output=embed&iwloc=near"
        width="100%" height="380" style="border:0;display:block;"
        allowfullscreen="" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        title="African Grey Parrot for Sale in {state_name} — CongoAfricanGreys.com">
      </iframe>
    </div>
    <p style="text-align:center;font-family:'Open Sans',sans-serif;font-size:.82rem;color:#9C8C7C;margin:1rem 0 0;">📍 Serving all {state_name} cities — including {cities}</p>
  </div>
</section>
"""

    if FOOTER_MARKER in content:
        content = content.replace(FOOTER_MARKER, map_html + '\n' + FOOTER_MARKER, 1)
        page.write_text(content)
        added.append(slug)
        print(f"✅ Added map: {slug}")
    else:
        print(f"⚠️  No footer marker in {slug}")

print(f"\nAdded: {len(added)} | Skipped (already have map): {len(skipped)}")
```

---

## Step 5 — Deploy + IndexNow

```bash
cd /Users/apple/Downloads/CAG/site/content
git add -A
git commit -m "Add Google Maps to X location pages (iframe, CSP-compliant)"
git push origin main
```

```python
import json, urllib.request

key = "[INDEX_NOW_KEY_TBD]"
urls = [
    "https://congoafricangreys.com/usa-locations/african-grey-parrot-arizona/",
    # add all changed URLs
]
payload = json.dumps({
    "host": "congoafricangreys.com", "key": key,
    "keyLocation": f"https://congoafricangreys.com/{key}.txt",
    "urlList": urls
}).encode()
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow", data=payload,
    headers={"Content-Type": "application/json; charset=utf-8"}, method="POST"
)
r = urllib.request.urlopen(req)
print(f"IndexNow: {r.status}")
```

---

## Rules

1. **NEVER use `<embed>` for Google Maps** — `object-src: 'none'` CSP blocks it silently. Always `<iframe>`. This is the critical rule — enforce it without exception.
2. **Always set `loading="lazy"`** — prevents page weight on pages with many sections.
3. **Always set `referrerpolicy="no-referrer-when-downgrade"`** — Google Maps requires this.
4. **Always set a descriptive `title`** — accessibility + SEO.
5. **Location pages: use state-wide zoom (6–7)** — shows coverage area, not a specific address.
6. **Contact/About pages: use HQ zoom (13)** — shows the actual [BREEDER_LOCATION] location.
7. **Check for existing map before adding** — never insert a second map on a page that already has one.
8. **Insert before `cag-footer-v1`** — standard insertion point for location pages.
9. **Run audit (Step 1) before every batch session** — never assume which pages need maps.
10. **Submit changed URLs to IndexNow** — every deploy must be followed by IndexNow submission.

---

## Reporting Format

```
GOOGLE MAP AUDIT — congoafricangreys.com
========================================
Pages audited:              [X]
Broken <embed> maps fixed:  [X]
Maps added to location pages: [X]
Already had proper iframe:  [X]
Skipped (no state data):    [X]

DEPLOYED: git push + IndexNow 200 OK
URLs submitted: [X]
```

---
name: cag-footer-agent
description: Applies the standard MFS footer (cag-footer-v2) to all pages in site/content/. Detects outdated WordPress/Astra footer markup and replaces it.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG Footer Agent Skill
## Managed Agent: Apply Standard Footer to All CongoAfricanGreys.com Pages
**Version 1.0 — MFS Design System v1.1 · Static HTML · Batch-Safe**

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

---

## SKILL OVERVIEW

You are the **Footer Agent** for CongoAfricanGreys.com. Your job is to apply the canonical CAG Footer to every `index.html` in the site. The footer is consistent across all pages — brand voice, contact info, nav links, social icons, and copyright never change per-page.

**One command does the whole site:**
```bash
cd /Users/apple/Downloads/CAG/site/content
python3 rebuild_footer.py
```

---

## WHAT THIS SKILL DOES

| Step | Action |
|---|---|
| 1 | Scans every `site/content/**/index.html` recursively |
| 2 | Finds pages with legacy footer markup |
| 3 | Replaces everything from the footer tag to closing tag |
| 4 | Writes a clean CAG Footer preserving all page content above/below |
| 5 | Skips pages that already have the current CAG footer |

**Safe:** Only touches the `<footer>` block. Head, schema, nav, entry-content, scripts below footer — all untouched.

---

## FOOTER DESIGN SPEC (v1.0)

### Structure
```
[Tagline Banner]      orange bg (#FF8C00), black text — WCAG AAA 9.04:1
[Main Body]           dark bg (#111), 4-column grid
  ├── Brand/Contact   logo text + about + phone/email/hours/location
  ├── Available Puppies  6 product page links
  ├── Quick Links        6 utility page links
  └── CTA Box           "Apply Now" button + open badge
[Social Bar]          #0d0d0d bg — FB / IG / TikTok / YT / LinkedIn / Pinterest
[Copyright Bar]       #070707 bg — © + Privacy / Terms / Sitemap links
```

### Colors (all WCAG compliant)
| Element | Foreground | Background | Ratio | WCAG |
|---|---|---|---|---|
| Tagline text | `#000` | `#FF8C00` | 9.04:1 | AAA ✓ |
| Body text | `#aaa` | `#111` | 9.5:1 | AAA ✓ |
| Orange headings | `#FF8C00` | `#111` | 5.79:1 | AA ✓ |
| Links | `#bbb` | `#111` | 11:1 | AAA ✓ |
| CTA btn text | `#000` | `#FF8C00` | 9.04:1 | AAA ✓ |
| Copyright | `#484848` | `#070707` | 4.6:1 | AA ✓ |

### Typography
- Headings: `Rosario`, 700 (already loaded on all pages — no extra font request)
- Body: `Open Sans`, normal
- Column headers: uppercase, `#FF8C00`, letter-spacing 0.06em

### Responsive Breakpoints
- ≥ 861px: 4-column grid (`2fr 1fr 1fr 1fr`)
- 521–860px: 2-column grid, brand col spans full width
- ≤ 520px: single column

---

## CONTACT DETAILS (update if they change)

| Field | Value |
|---|---|
| Phone | (531) 368-0538 |
| Email | [INQUIRIES_EMAIL_TBD] |
| Address | [BREEDER_LOCATION_TBD] |
| Hours | [HOURS_TBD] |
| Price range | Congo African Grey $1,500–$3,500 · Timneh African Grey $1,200–$2,500 |

---

## SOCIAL LINKS

| Platform | URL |
|---|---|
| Facebook | [FACEBOOK_URL_TBD] |
| Instagram | [INSTAGRAM_URL_TBD] |
| TikTok | [TIKTOK_URL_TBD] |
| YouTube | [YOUTUBE_URL_TBD] |
| LinkedIn | [LINKEDIN_URL_TBD] |
| Pinterest | https://uk.pinterest.com/MFSAfrican Grey parrotMaltesePuppies/ |

---

## FOOTER NAV LINKS

### Available Puppies column
- Non-Shedding African Grey parrot → `/non-shedding-african grey parrot-puppies/`
- African Grey parrot For Adoption → `/african grey parrot-puppies-for-adoption/`
- Congo African Grey → `/congo-african-grey-for-sale/`
- Toy African Grey parrot Puppies → `/toy-african grey parrot-puppies/`
- Timneh African Grey → `/timneh-african-grey-for-sale/`
- Mini African Grey parrot → `/mini-african grey parrot-puppies/`

### Quick Links column
- Find African Grey parrot Near Me → `/buy-african grey parrot-near-me/`
- MFS Vs. Other Breeds → `/african grey parrot-vs-other-breeds/`
- Testimonials → `/testimonials/`
- Privacy Policy → `/privacy-policy/`
- Terms & Conditions → `/refund_returns/`
- Shipping & Delivery → `/shipping-delivery/`

---

## HOW TO RUN

### Full site update (all 100+ pages)
```bash
cd /Users/apple/Downloads/MFS
python3 rebuild_footer.py
```

### Single page test
```bash
python3 rebuild_footer.py site/content/male-vs-female-african grey parrot/index.html
```

### After running — commit and push
```bash
cd site2
git add -A
git commit -m "Apply MFS Footer v2 to all pages"
git push origin main
```

### After push — submit updated URLs to IndexNow
```python
import json, urllib.request
key = "a1b2c3d4e5f6789012345678african grey parrots"
# Submit homepage + top traffic pages
urls = [
    "https://african grey parrotsforsale.com/",
    "https://african grey parrotsforsale.com/buy-african grey parrot-near-me/",
    "https://african grey parrotsforsale.com/toy-african grey parrot-puppies/",
    "https://african grey parrotsforsale.com/mini-african grey parrot-puppies/",
    "https://congoafricangreys.com/congo-african-grey-for-sale/",
    "https://african grey parrotsforsale.com/male-vs-female-african grey parrot/",
]
payload = json.dumps({"host":"african grey parrotsforsale.com","key":key,
    "keyLocation":f"https://african grey parrotsforsale.com/{key}.txt","urlList":urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow",data=payload,
    headers={"Content-Type":"application/json; charset=utf-8"},method="POST")
print(urllib.request.urlopen(req).status)
```

---

## UPDATING THE FOOTER IN THE FUTURE

If you need to change footer content (new link, new contact info, updated price):

1. **Edit the `NEW_FOOTER` string** in `/Users/apple/Downloads/MFS/rebuild_footer.py`
2. **Re-run the batch script** — it replaces all pages in one pass
3. Commit + push + IndexNow

**Never edit individual page footers by hand.** The script is the single source of truth.

---

## SKIPPED PAGES (expected)

The script skips ~110 pages that don't use the Astra `site-footer` class. These are:
- WooCommerce product/shop pages
- Puppy listing pages (`/puppies/`, `/for-sale/`, `/available/`)
- Duplicate/redirect pages
- Admin/form pages

These pages have their own footer structure and are not part of the main content redesign.

---

## FOOTER COLUMN STRUCTURE SPECIFICATION (Required Content)

When auditing or updating the footer, ensure it contains these 5 content columns. Any footer missing 2 or more columns should be flagged as `INCOMPLETE`.

```
Column 1: Quick Links
  - Available Birds → /available/
  - Congo African Grey → /congo-african-grey-for-sale/
  - Timneh African Grey → /timneh-african-grey-for-sale/
  - Pricing → /african-grey-price-cost/
  - Contact → /contact/

Column 2: Resources
  - Species Guide → /african-grey-species-guide/
  - Care Guide → /african-grey-care-guide/
  - CITES Info → /cites-captive-bred-documentation/
  - FAQ → /african-grey-species-guide/#faq
  - Blog → /blog/

Column 3: Company
  - About Us → /about/
  - Our Birds → /available/
  - Testimonials → /testimonials/
  - Contact → /contact/

Column 4: Legal
  - Privacy Policy → /privacy-policy/
  - Terms of Service → /terms/
  - Health Guarantee Terms → /health-guarantee/
  - Shipping Policy → /shipping-delivery/
  - Refund Policy → /refund-policy/

Column 5: Contact
  - Phone: [BREEDER_PHONE_TBD]
  - Email: [INQUIRIES_EMAIL_TBD]
  - Address: [BREEDER_LOCATION_TBD]
  - Hours: Open 24/7
  - Social Links: Facebook, Instagram, TikTok, YouTube

Bottom Bar:
  - Copyright © CongoAfricanGreys.com [year]
  - USDA AWA Licensed (include license number once confirmed)
  - CITES Captive-Bred Documentation Available
```

**Audit rule:** When running in audit mode, flag any page whose footer is missing 2 or more of these 5 columns as `INCOMPLETE — needs footer rebuild`.

---

## WHAT NOT TO TOUCH

- **`/wp-content/themes/astra/`** — never modify theme files
- **`/wp-content/plugins/`** — never modify plugin files
- **`frontend.min.js`** — Astra's critical JS, do not touch
- **Schema JSON-LD blocks** — the footer replacement preserves all content above the `<footer>` tag, including schema

---

## REFERENCE

- **Script:** `/Users/apple/Downloads/MFS/rebuild_footer.py`
- **Design system:** `MFS-DESIGN-REBUILD-SKILL.md`
- **Reference page (footer live):** `https://african grey parrotsforsale.com/male-vs-female-african grey parrot/`
- **First deployed:** 2026-04-22 — 103 pages updated in one run
- **CLAUDE.md skill entry:** `MFS-FOOTER-AGENT-SKILL.md` → Footer redesign, batch apply to all pages
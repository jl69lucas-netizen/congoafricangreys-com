# Navbar & Footer Polish — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix three UI issues across all 8 CAG HTML pages: (1) add search to navbar, (2) replace plain-text footer brand with the site's logo mark, (3) fix footer column alignment so Shop/Info/Contact headings align correctly with their list items.

**Architecture:** All 8 pages use identical inline-CSS navbar/footer patterns — no shared templates. Changes are applied by a Python sed-like script that patches the same HTML/CSS substring in every file consistently, reducing error and ensuring parity. A browser preview of `contact-us/index.html` is used to verify before and after.

**Tech Stack:** Pure HTML/CSS (inline `<style>` tags), Python 3 for batch patching, browser (file:// URL) for visual verification.

---

## Context

The live site at congoafricangreys.com has three visual issues:

1. **Navbar missing search** — user wants: `[Logo] [Nav links] [Search icon] [CTA button]`
2. **Footer logo is plain text** — `<div class="cag-ft-brand-name">Congo African Greys</div>` has no parrot emoji or link, unlike the navbar logo mark
3. **Footer column misalignment** — Shop, Info, and Contact `h4` headings don't align horizontally with their sibling columns' content because the grid lacks `align-items: start`

Affected files (all 8):
- `site/content/contact-us/index.html`
- `site/content/congo-african-grey-for-sale/index.html`
- `site/content/african-grey-parrot-for-sale/index.html`
- `site/content/african-grey-parrot-for-sale-near-me/index.html`
- `site/content/african-grey-parrot-for-sale-new-york/index.html`
- `site/content/african-grey-parrot-for-sale-ohio/index.html`
- `site/content/african-grey-parrot-for-sale-texas/index.html`
- `site/content/african-grey-breeding-pair-for-sale/index.html`

Design system source of truth: `docs/design.md`
Colors: `--clay: #e8604c`, `--green: #2D6A4F`, `--text: #1c1a18`
Fonts: Lora (serif, brand) + Sora (sans, body/nav)

---

## File Structure

| File | Action |
|------|--------|
| `site/content/contact-us/index.html` | Patched (navbar + footer) |
| `site/content/congo-african-grey-for-sale/index.html` | Patched (navbar + footer) |
| `site/content/african-grey-parrot-for-sale/index.html` | Patched (navbar + footer) |
| `site/content/african-grey-parrot-for-sale-near-me/index.html` | Patched (navbar + footer) |
| `site/content/african-grey-parrot-for-sale-new-york/index.html` | Patched (navbar + footer) |
| `site/content/african-grey-parrot-for-sale-ohio/index.html` | Patched (navbar + footer) |
| `site/content/african-grey-parrot-for-sale-texas/index.html` | Patched (navbar + footer) |
| `site/content/african-grey-breeding-pair-for-sale/index.html` | Patched (navbar + footer) |
| `scripts/patch_navbar_footer.py` | Created — batch patcher |

---

## Task 1: Verify Issues Exist (Visual Baseline)

**Files:** `site/content/contact-us/index.html` (read-only)

- [ ] **Step 1: Open contact-us page in browser to confirm the three issues**

```bash
open "file:///Users/apple/Downloads/CAG/site/content/contact-us/index.html"
```

Expected: 
- Navbar shows `[🦜 Logo] [Nav links] [Inquire Now CTA]` — NO search icon
- Footer brand column shows plain text "Congo African Greys" — no emoji, no link
- Footer columns Shop/Info/Contact h4 headings may appear misaligned with their list items (especially at mid-width viewport or with column height variation)

---

## Task 2: Add Search Icon to Navbar

**Files:** All 8 `site/content/*/index.html`

The search icon sits between the nav links and the CTA button. It's a ghost icon button: circular, 36×36px, magnifying glass emoji, no background. On click it opens a Google `site:congoafricangreys.com` search in a new tab.

On mobile (≤768px), search is hidden alongside the nav links (hamburger menu takes over).

- [ ] **Step 1: Write the patch script**

Create `scripts/patch_navbar_footer.py`:

```python
import re
from pathlib import Path

PAGES = [
    "site/content/contact-us/index.html",
    "site/content/congo-african-grey-for-sale/index.html",
    "site/content/african-grey-parrot-for-sale/index.html",
    "site/content/african-grey-parrot-for-sale-near-me/index.html",
    "site/content/african-grey-parrot-for-sale-new-york/index.html",
    "site/content/african-grey-parrot-for-sale-ohio/index.html",
    "site/content/african-grey-parrot-for-sale-texas/index.html",
    "site/content/african-grey-breeding-pair-for-sale/index.html",
]

# ── Patch 1: Navbar CSS — add search button styles ──────────────────────────
OLD_NAV_CSS = "@media(max-width:768px){#cag-header .cag-nav-links,#cag-header .cag-nav-cta{display:none}#cag-header .cag-hamburger{display:flex}#cag-header{padding:0 24px}}"
NEW_NAV_CSS = (
    "#cag-header .cag-nav-search{display:flex;align-items:center;justify-content:center;"
    "width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.1);border:1px solid "
    "rgba(255,255,255,.2);color:rgba(255,255,255,.8);cursor:pointer;text-decoration:none;"
    "font-size:15px;transition:background .2s,border-color .2s;flex-shrink:0}"
    "#cag-header .cag-nav-search:hover{background:rgba(255,255,255,.18);border-color:rgba(255,255,255,.35)}"
    "@media(max-width:768px){#cag-header .cag-nav-links,#cag-header .cag-nav-cta,"
    "#cag-header .cag-nav-search{display:none}#cag-header .cag-hamburger{display:flex}#cag-header{padding:0 24px}}"
)

# ── Patch 2: Navbar HTML — insert search anchor before CTA ──────────────────
OLD_NAV_CTA = '<a href="/contact-us/" class="cag-nav-cta">Inquire Now</a>'
NEW_NAV_CTA = (
    '<a href="https://www.google.com/search?q=site:congoafricangreys.com" '
    'target="_blank" rel="noopener" class="cag-nav-search" aria-label="Search site" title="Search">&#128269;</a>'
    '<a href="/contact-us/" class="cag-nav-cta">Inquire Now</a>'
)

# ── Patch 3: Footer CSS — fix grid alignment + add logo link style ───────────
OLD_FT_GRID_CSS = "#cag-footer .cag-ft-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1.3fr;gap:40px;margin-bottom:48px}"
NEW_FT_GRID_CSS = (
    "#cag-footer .cag-ft-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1.3fr;"
    "gap:40px;margin-bottom:48px;align-items:start}"
    "#cag-footer .cag-ft-logo{display:flex;align-items:center;gap:8px;text-decoration:none;margin-bottom:12px}"
    "#cag-footer .cag-ft-logo-icon{font-size:20px}"
)

# ── Patch 4: Footer brand name CSS — keep but reset margin (now on anchor) ──
OLD_FT_BRAND_CSS = "#cag-footer .cag-ft-brand-name{font-family:'Lora',serif;font-size:1.2rem;font-weight:700;color:#fff;margin-bottom:12px}"
NEW_FT_BRAND_CSS = "#cag-footer .cag-ft-brand-name{font-family:'Lora',serif;font-size:1.2rem;font-weight:700;color:#fff}"

# ── Patch 5: Footer HTML — replace plain text brand with logo mark ───────────
OLD_FT_BRAND_HTML = "<div class=\"cag-ft-brand-name\">Congo African Greys</div>"
NEW_FT_BRAND_HTML = (
    '<a href="/" class="cag-ft-logo">'
    '<span class="cag-ft-logo-icon">&#129412;</span>'
    '<span class="cag-ft-brand-name">Congo African Greys</span>'
    '</a>'
)

PATCHES = [
    (OLD_NAV_CSS, NEW_NAV_CSS, "navbar search CSS"),
    (OLD_NAV_CTA, NEW_NAV_CTA, "navbar search HTML"),
    (OLD_FT_GRID_CSS, NEW_FT_GRID_CSS, "footer grid align-items + logo CSS"),
    (OLD_FT_BRAND_CSS, NEW_FT_BRAND_CSS, "footer brand-name margin reset"),
    (OLD_FT_BRAND_HTML, NEW_FT_BRAND_HTML, "footer logo mark HTML"),
]

ROOT = Path(__file__).parent.parent

def patch_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    applied = []
    for old, new, label in PATCHES:
        if old in text:
            text = text.replace(old, new, 1)
            applied.append(label)
        else:
            print(f"  SKIP (not found): {label}")
    path.write_text(text, encoding="utf-8")
    return applied

def main():
    for rel in PAGES:
        p = ROOT / rel
        if not p.exists():
            print(f"MISSING: {p}")
            continue
        print(f"\nPatching: {rel}")
        applied = patch_file(p)
        for label in applied:
            print(f"  ✓ {label}")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the patch script**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/patch_navbar_footer.py
```

Expected output — for each page, 5 lines like:
```
Patching: site/content/contact-us/index.html
  ✓ navbar search CSS
  ✓ navbar search HTML
  ✓ footer grid align-items + logo CSS
  ✓ footer brand-name margin reset
  ✓ footer logo mark HTML
```

If any patch prints `SKIP (not found)`, that file has a different pattern — fix manually (see Task 3).

- [ ] **Step 3: Verify the patch applied correctly on contact-us**

```bash
grep -c "cag-nav-search" /Users/apple/Downloads/CAG/site/content/contact-us/index.html
grep -c "cag-ft-logo" /Users/apple/Downloads/CAG/site/content/contact-us/index.html
grep -c "align-items:start" /Users/apple/Downloads/CAG/site/content/contact-us/index.html
```

Expected: Each command prints `2` (once in CSS, once in HTML for nav-search and ft-logo; `align-items:start` appears once in the grid CSS).

---

## Task 3: Fix Any Pages That Didn't Patch (Manual Fallback)

**Files:** Any page that printed `SKIP` in Task 2

- [ ] **Step 1: For any skipped page, read lines 800–845 to see the actual navbar pattern**

```bash
sed -n '800,845p' /Users/apple/Downloads/CAG/site/content/<page>/index.html
```

- [ ] **Step 2: Check what's different** — likely the CTA link or CSS order. Apply the same logical changes manually: add `.cag-nav-search` CSS before the `@media` block, insert the search anchor before the CTA anchor, update footer grid CSS to add `align-items:start`, wrap brand name in `.cag-ft-logo` anchor.

- [ ] **Step 3: Re-run grep checks from Task 2, Step 3 on the fixed file**

---

## Task 4: Visual Verification

**Files:** `site/content/contact-us/index.html` (primary), spot-check 2 others

- [ ] **Step 1: Open contact-us in browser**

```bash
open "file:///Users/apple/Downloads/CAG/site/content/contact-us/index.html"
```

- [ ] **Step 2: Check navbar** — confirm layout is:
  `[🦜 Congo African Greys] .... [Home] [Shop] [About] [Reviews] [Shipping] [Health Guarantee] [Contact] .... [🔍] [Inquire Now]`
  - Search icon is circular ghost button, positioned between last nav link and the coral CTA
  - Clicking search opens Google search for `site:congoafricangreys.com` in new tab

- [ ] **Step 3: Check footer brand column** — confirm:
  - "Congo African Greys" is now a clickable link with the 🦜 parrot emoji to its left
  - Clicking it navigates to `/` (home)
  - Styling matches navbar logo (Lora serif, white text)

- [ ] **Step 4: Check footer column alignment** — confirm:
  - "Shop", "Info", "Contact", "Newsletter" h4 headings all sit at the top of their cells
  - The link items directly below each heading are vertically aligned across columns
  - No column's content is vertically stretched or centered

- [ ] **Step 5: Spot-check one other page**

```bash
open "file:///Users/apple/Downloads/CAG/site/content/congo-african-grey-for-sale/index.html"
```

Confirm same navbar search icon and footer logo mark appear correctly.

- [ ] **Step 6: Check mobile responsiveness** — resize browser to 375px width. Confirm:
  - Search icon is hidden (same as nav links) on mobile — hamburger menu shows
  - Footer collapses to single column, logo mark visible at top of footer

---

## Task 5: Run impeccable Polish (Optional — Recommended)

If any visual inconsistencies remain after Task 4, invoke the impeccable skill for a final polish pass on `contact-us/index.html`. The skill will audit all design system tokens, spacing, and visual polish against `docs/design.md`.

```
/impeccable contact-us/index.html
```

---

## Task 6: Commit

- [ ] **Step 1: Stage all changed HTML files**

```bash
cd /Users/apple/Downloads/CAG && git add \
  site/content/contact-us/index.html \
  site/content/congo-african-grey-for-sale/index.html \
  site/content/african-grey-parrot-for-sale/index.html \
  site/content/african-grey-parrot-for-sale-near-me/index.html \
  site/content/african-grey-parrot-for-sale-new-york/index.html \
  site/content/african-grey-parrot-for-sale-ohio/index.html \
  site/content/african-grey-parrot-for-sale-texas/index.html \
  site/content/african-grey-breeding-pair-for-sale/index.html \
  scripts/patch_navbar_footer.py
```

- [ ] **Step 2: Commit**

```bash
git commit -m "$(cat <<'EOF'
polish: add navbar search, fix footer logo + column alignment across all pages

- Navbar: search icon (🔍) added between nav links and Inquire Now CTA
- Footer: brand column upgraded from plain text to logo mark (🦜 + Lora serif link)
- Footer: added align-items:start to grid to fix Shop/Info/Contact heading alignment
- Applied consistently to all 8 HTML pages via scripts/patch_navbar_footer.py

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

---

## Verification Summary

| Check | Method | Pass Criteria |
|-------|--------|---------------|
| Navbar search present | Visual + grep | Search icon visible between nav and CTA |
| Search functional | Click in browser | Opens Google site search in new tab |
| Footer logo mark | Visual | 🦜 + "Congo African Greys" linked to `/` |
| Footer column alignment | Visual at desktop | Shop/Info/Contact h4 flush to top of cells |
| Mobile search hidden | Resize to 375px | Search icon hidden, hamburger shows |
| All 8 pages patched | grep count | `cag-nav-search` count = 2 in each file |

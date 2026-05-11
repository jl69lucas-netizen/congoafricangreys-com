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

# ── Patch 4: Footer brand name CSS — remove margin-bottom (now on anchor) ───
OLD_FT_BRAND_CSS = "#cag-footer .cag-ft-brand-name{font-family:'Lora',serif;font-size:1.2rem;font-weight:700;color:#fff;margin-bottom:12px}"
NEW_FT_BRAND_CSS = "#cag-footer .cag-ft-brand-name{font-family:'Lora',serif;font-size:1.2rem;font-weight:700;color:#fff}"

# ── Patch 5: Footer HTML — replace plain text brand with logo mark ───────────
OLD_FT_BRAND_HTML = '<div class="cag-ft-brand-name">Congo African Greys</div>'
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

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

# ── Overlay CSS (appended inside existing navbar <style> block) ──────────────
OLD_NAV_MEDIA = (
    "@media(max-width:768px){#cag-header .cag-nav-links,#cag-header .cag-nav-cta,"
    "#cag-header .cag-nav-search{display:none}#cag-header .cag-hamburger{display:flex}"
    "#cag-header{padding:0 24px}}"
)
NEW_NAV_MEDIA = OLD_NAV_MEDIA + (
    "#cag-search-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.78);"
    "z-index:1100;align-items:center;justify-content:center;padding:20px}"
    "#cag-search-overlay.open{display:flex}"
    "#cag-search-box{background:#fff;border-radius:16px;padding:36px 28px 28px;"
    "width:min(600px,92vw);position:relative;box-shadow:0 24px 80px rgba(0,0,0,.35)}"
    "#cag-search-box form{display:flex;gap:10px}"
    "#cag-search-input{flex:1;padding:13px 20px;border:2px solid #ede5dc;border-radius:50px;"
    "font-size:15px;font-family:'Sora',sans-serif;outline:none;color:#1c1a18;min-width:0}"
    "#cag-search-input:focus{border-color:#e8604c;box-shadow:0 0 0 3px rgba(232,96,76,.1)}"
    "#cag-search-submit{background:#e8604c;color:#fff;border:none;padding:13px 22px;"
    "border-radius:50px;font-size:14px;cursor:pointer;font-family:'Sora',sans-serif;"
    "font-weight:700;white-space:nowrap;transition:background .2s;flex-shrink:0}"
    "#cag-search-submit:hover{background:#c94d3a}"
    "#cag-search-close{position:absolute;top:12px;right:16px;background:none;border:none;"
    "font-size:22px;cursor:pointer;color:#9b9189;line-height:1;padding:4px;transition:color .2s}"
    "#cag-search-close:hover{color:#1c1a18}"
    "#cag-search-hint{font-size:12px;color:#9b9189;margin-top:12px;font-family:'Sora',sans-serif;"
    "text-align:center}"
)

# ── Change search anchor → button (no href, JS handles click) ────────────────
OLD_SEARCH_A = (
    '<a href="https://www.google.com/search?q=site:congoafricangreys.com" '
    'target="_blank" rel="noopener" class="cag-nav-search" aria-label="Search site" title="Search">&#128269;</a>'
)
NEW_SEARCH_BTN = (
    '<button type="button" class="cag-nav-search" aria-label="Search site" title="Search">&#128269;</button>'
)

# ── Search overlay HTML (inserted after mobile menu closing </div>) ───────────
OLD_AFTER_MOBILE_MENU = '<a href="/contact-us/">Inquire Now →</a>\n</div>'
NEW_AFTER_MOBILE_MENU = (
    '<a href="/contact-us/">Inquire Now →</a>\n</div>\n'
    '<div id="cag-search-overlay">\n'
    '<div id="cag-search-box">\n'
    '<button id="cag-search-close" aria-label="Close search">&#x2715;</button>\n'
    '<form id="cag-search-form">\n'
    '<input id="cag-search-input" type="text" placeholder="Search CongoAfricanGreys.com…" autocomplete="off" aria-label="Search">\n'
    '<button type="submit" id="cag-search-submit">Search</button>\n'
    '</form>\n'
    '<p id="cag-search-hint">Search our birds, care guides, and more</p>\n'
    '</div>\n'
    '</div>'
)

# ── Copyright year → dynamic span ────────────────────────────────────────────
OLD_COPYRIGHT = '<span>Copyright © 2025 · congoafricangreys.com · All Rights Reserved</span>'
NEW_COPYRIGHT = '<span>Copyright © <span id="cag-year"></span> · congoafricangreys.com · All Rights Reserved</span>'

# ── JS block (inserted before speculationrules script) ───────────────────────
SEARCH_JS = (
    '<script>\n'
    '(function(){\n'
    '  var overlay=document.getElementById("cag-search-overlay");\n'
    '  var input=document.getElementById("cag-search-input");\n'
    '  function openSearch(){overlay.classList.add("open");setTimeout(function(){input.focus();},60);}\n'
    '  function closeSearch(){overlay.classList.remove("open");input.value="";}\n'
    '  document.getElementById("cag-search-form").addEventListener("submit",function(e){\n'
    '    e.preventDefault();\n'
    '    var q=input.value.trim();\n'
    '    if(q)window.open("https://www.google.com/search?q=site:congoafricangreys.com+"+encodeURIComponent(q),"_blank");\n'
    '  });\n'
    '  document.getElementById("cag-search-close").addEventListener("click",closeSearch);\n'
    '  overlay.addEventListener("click",function(e){if(e.target===overlay)closeSearch();});\n'
    '  document.addEventListener("keydown",function(e){if(e.key==="Escape")closeSearch();});\n'
    '  document.querySelector(".cag-nav-search").addEventListener("click",openSearch);\n'
    '  var yr=document.getElementById("cag-year");\n'
    '  if(yr)yr.textContent=new Date().getFullYear();\n'
    '})();\n'
    '</script>\n'
)
OLD_SPECULATION = '<script type="speculationrules">'
NEW_SPECULATION = SEARCH_JS + OLD_SPECULATION

PATCHES = [
    (OLD_NAV_MEDIA,             NEW_NAV_MEDIA,             "overlay CSS"),
    (OLD_SEARCH_A,              NEW_SEARCH_BTN,            "search anchor → button"),
    (OLD_AFTER_MOBILE_MENU,     NEW_AFTER_MOBILE_MENU,     "overlay HTML"),
    (OLD_COPYRIGHT,             NEW_COPYRIGHT,             "copyright year span"),
    (OLD_SPECULATION,           NEW_SPECULATION,           "search + year JS"),
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

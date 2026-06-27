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

# Fix 1: h4 — reset browser default margin-top to 0; use explicit margin shorthand
OLD_H4 = "#cag-footer .cag-ft-col h4{font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#e8604c;margin-bottom:16px}"
NEW_H4 = "#cag-footer .cag-ft-col h4{font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#e8604c;margin:0 0 16px 0;padding:0}"

# Fix 2: ul — reset browser default margin/padding; add consistent line-height
OLD_UL = "#cag-footer .cag-ft-col ul{list-style:none;display:flex;flex-direction:column;gap:10px}"
NEW_UL = "#cag-footer .cag-ft-col ul{list-style:none;display:flex;flex-direction:column;gap:10px;margin:0;padding:0}"

# Fix 3: anchor — add line-height so emoji and text links render at same height
OLD_A = "#cag-footer .cag-ft-col ul a{color:rgba(255,255,255,.55);text-decoration:none;font-size:.875rem;transition:color .2s}"
NEW_A = "#cag-footer .cag-ft-col ul a{color:rgba(255,255,255,.55);text-decoration:none;font-size:.875rem;line-height:1.4;display:block;transition:color .2s}"

# Fix 4: newsletter h4 — same margin reset for perfect alignment with other columns
OLD_NL_H4 = "#cag-footer .cag-ft-nl h4{font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#e8604c;margin-bottom:12px}"
NEW_NL_H4 = "#cag-footer .cag-ft-nl h4{font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#e8604c;margin:0 0 12px 0;padding:0}"

PATCHES = [
    (OLD_H4, NEW_H4, "h4 margin reset"),
    (OLD_UL, NEW_UL, "ul margin/padding reset"),
    (OLD_A, NEW_A, "anchor line-height fix"),
    (OLD_NL_H4, NEW_NL_H4, "newsletter h4 margin reset"),
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

"""
Fix breadcrumbs on the 8 pages that still have old hardcoded breadcrumbs
or no breadcrumb at all. For each page:
  1. Remove old hardcoded breadcrumb wrapper (nav.breadcrumb or div.cag-breadcrumb)
  2. Add `import Breadcrumb` to frontmatter imports
  3. Insert <Breadcrumb items={[...]} /> as first child of hero's inner container
  4. Strip obsolete .breadcrumb / .cag-breadcrumb CSS from <style> blocks
"""

import re

BASE = '/Users/apple/Downloads/CAG'

# ── Page definitions ──────────────────────────────────────────────────────────
# Each entry: (filepath, breadcrumb items, hero selector hint)
PAGES = [
    # Astro-style pages with named container class heroes
    {
        'file': 'src/pages/african-grey-care/index.astro',
        'import_from': '../../components/Breadcrumb.astro',
        'items': [
            ('Home', '/'),
            ('African Grey Care', '/african-grey-care/'),
        ],
        'hero_section': 'care-hero',   # <section class="care-hero">
        'inner_div': 'container',      # first <div class="container"> inside
    },
    {
        'file': 'src/pages/african-grey-parrot-adoption-cost/index.astro',
        'import_from': '../../components/Breadcrumb.astro',
        'items': [
            ('Home', '/'),
            ('African Grey Adoption', '/african-grey-adoption/'),
            ('Adoption Cost', '/african-grey-parrot-adoption-cost/'),
        ],
        'hero_section': 'page-hero',
        'inner_div': 'container',
    },
    {
        'file': 'src/pages/captive-bred-african-grey-parrot/index.astro',
        'import_from': '../../components/Breadcrumb.astro',
        'items': [
            ('Home', '/'),
            ('African Grey Parrot Guide', '/african-grey-parrot-guide/'),
            ('Captive-Bred African Grey', '/captive-bred-african-grey-parrot/'),
        ],
        'hero_section': 'page-hero',
        'inner_div': 'container',
    },
    {
        'file': 'src/pages/dna-tested-african-grey-for-sale/index.astro',
        'import_from': '../../components/Breadcrumb.astro',
        'items': [
            ('Home', '/'),
            ('African Grey Parrot Guide', '/african-grey-parrot-guide/'),
            ('DNA-Tested African Grey', '/dna-tested-african-grey-for-sale/'),
        ],
        'hero_section': 'page-hero',
        'inner_div': 'container',
    },
    {
        'file': 'src/pages/hand-raised-african-grey-parrot-for-sale/index.astro',
        'import_from': '../../components/Breadcrumb.astro',
        'items': [
            ('Home', '/'),
            ('African Grey Parrot Guide', '/african-grey-parrot-guide/'),
            ('Hand-Raised African Grey', '/hand-raised-african-grey-parrot-for-sale/'),
        ],
        'hero_section': 'page-hero',
        'inner_div': 'container',
    },
    {
        'file': 'src/pages/how-to-tame-african-grey-parrot/index.astro',
        'import_from': '../../components/Breadcrumb.astro',
        'items': [
            ('Home', '/'),
            ('African Grey Care', '/african-grey-care/'),
            ('How to Tame an African Grey', '/how-to-tame-african-grey-parrot/'),
        ],
        'hero_section': 'page-hero',
        'inner_div': 'container',
    },
    # Tailwind-style page — no old breadcrumb, just missing entirely
    {
        'file': 'src/pages/african-grey-parrot-for-sale-near-me/index.astro',
        'import_from': '../../components/Breadcrumb.astro',
        'items': [
            ('Home', '/'),
            ('African Grey Parrots for Sale', '/african-grey-parrot-for-sale/'),
            ('African Grey for Sale Near Me', '/african-grey-parrot-for-sale-near-me/'),
        ],
        'hero_section': 'bg-logo-dark',   # partial class match
        'inner_div': 'max-w-5xl',         # partial match
    },
    # Scam page — old cag-breadcrumb div before #hero
    {
        'file': 'src/pages/how-to-avoid-african-grey-parrot-scams/index.astro',
        'import_from': '../../components/Breadcrumb.astro',
        'items': [
            ('Home', '/'),
            ('Scam Prevention', '/how-to-avoid-african-grey-parrot-scams/'),
        ],
        'hero_section': 'id="hero"',      # <section id="hero" ...>
        'inner_div': 'container',
    },
]


def build_breadcrumb_astro(items, indent='      '):
    """Return the <Breadcrumb items={[...]} /> Astro tag."""
    item_lines = []
    for name, url in items:
        item_lines.append(f'  {{ name: "{name}", url: "{url}" }}')
    items_str = ',\n'.join(item_lines)
    nl = '\n'
    return f'{indent}<Breadcrumb items={{[{nl}{items_str}{nl}{indent}]}} />{nl}'


def add_import(content, import_from):
    """Add import Breadcrumb line after the last existing import in frontmatter."""
    if 'import Breadcrumb' in content:
        return content  # already imported
    # Find the last "import ... from" line before the closing ---
    lines = content.split('\n')
    last_import_idx = -1
    in_frontmatter = False
    fm_count = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '---':
            fm_count += 1
            if fm_count == 1:
                in_frontmatter = True
                continue
            elif fm_count == 2:
                in_frontmatter = False
                break
        if in_frontmatter and stripped.startswith('import '):
            last_import_idx = i
    if last_import_idx == -1:
        return content
    # Derive the correct relative path from import_from
    lines.insert(last_import_idx + 1, f"import Breadcrumb from '{import_from}';")
    return '\n'.join(lines)


def remove_old_breadcrumb_nav(content):
    """
    Remove the old hardcoded breadcrumb blocks:
      Pattern A: <div class="container">\n    <nav class="breadcrumb" ...>...</nav>\n  </div>
      Pattern B: <div class="cag-breadcrumb">\n    <div class="container">\n      <nav ...></nav>\n    </div>\n  </div>
    Uses a simple multi-line regex.
    """
    # Pattern A — container > nav.breadcrumb
    content = re.sub(
        r'\n[ \t]*<div[^>]*class="container"[^>]*>\n[ \t]*<nav[^>]*breadcrumb[^>]*>.*?</nav>\n[ \t]*</div>(\n[ \t]*\n)?',
        '\n',
        content,
        flags=re.DOTALL
    )
    # Pattern B — div.cag-breadcrumb wrapper (scam page)
    content = re.sub(
        r'\n[ \t]*<!-- Breadcrumb -->\n[ \t]*<div[^>]*cag-breadcrumb[^>]*>.*?</div>\n[ \t]*</div>\n',
        '\n',
        content,
        flags=re.DOTALL
    )
    return content


def remove_breadcrumb_css(content):
    """Strip .breadcrumb and .cag-breadcrumb CSS declarations from <style> blocks."""
    # Remove single-line CSS rules like: .breadcrumb{...}
    content = re.sub(r'\.cag-breadcrumb\{[^}]*\}\n?', '', content)
    content = re.sub(r'\.cag-breadcrumb\s+a\{[^}]*\}\n?', '', content)
    content = re.sub(r'\.cag-breadcrumb\s+a:hover\{[^}]*\}\n?', '', content)
    # Multi-line .breadcrumb { ... } blocks inside <style>
    content = re.sub(
        r'[ \t]*\.breadcrumb[ \t]*\{[^}]*\}\n?',
        '',
        content
    )
    return content


def inject_breadcrumb_into_hero(content, hero_hint, inner_div_hint, items):
    """
    Find the hero section, then its first inner container div, and insert
    <Breadcrumb .../> as the first child.
    """
    lines = content.split('\n')
    hero_idx = -1
    for i, line in enumerate(lines):
        if hero_hint in line and '<section' in line:
            hero_idx = i
            break
    if hero_idx == -1:
        print(f"  ⚠ Could not find hero section with hint '{hero_hint}'")
        return content

    # Find the first inner <div that contains inner_div_hint, after hero_idx
    inner_div_idx = -1
    for i in range(hero_idx + 1, min(hero_idx + 10, len(lines))):
        if '<div' in lines[i] and inner_div_hint in lines[i]:
            inner_div_idx = i
            break
    if inner_div_idx == -1:
        print(f"  ⚠ Could not find inner div with hint '{inner_div_hint}'")
        return content

    # Determine indentation from the inner div line
    inner_indent = len(lines[inner_div_idx]) - len(lines[inner_div_idx].lstrip())
    bc_indent = ' ' * (inner_indent + 2)

    # Build the Breadcrumb tag lines
    item_strs = [f'  {{ name: "{name}", url: "{url}" }}' for name, url in items]
    bc_block = [
        f'{bc_indent}<Breadcrumb items={{[',
        *[f'{bc_indent}{s},' if i < len(item_strs)-1 else f'{bc_indent}{s}' for i, s in enumerate(item_strs)],
        f'{bc_indent}]}} />',
    ]

    # Insert after the inner div line
    lines = lines[:inner_div_idx + 1] + bc_block + lines[inner_div_idx + 1:]
    return '\n'.join(lines)


def process_page(page):
    filepath = f"{BASE}/{page['file']}"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Step 1 — add import
    content = add_import(content, page['import_from'])

    # Step 2 — remove old hardcoded breadcrumb HTML
    content = remove_old_breadcrumb_nav(content)

    # Step 3 — remove stale CSS
    content = remove_breadcrumb_css(content)

    # Step 4 — inject new <Breadcrumb> inside hero
    content = inject_breadcrumb_into_hero(
        content,
        page['hero_section'],
        page['inner_div'],
        page['items']
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {page['file']}")
    else:
        print(f"  — {page['file']} (unchanged)")


if __name__ == '__main__':
    print("Adding missing frosted-pill breadcrumbs...\n")
    for page in PAGES:
        process_page(page)
    print("\nDone.")

#!/usr/bin/env python3
"""Move <Breadcrumb .../> from inside hero sections to before them, sitewide."""
import os
import re
import sys

PAGES_DIR = "/Users/apple/Downloads/CAG/src/pages"

# Already fixed manually — skip these
SKIP_FILES = {
    "/Users/apple/Downloads/CAG/src/pages/african-grey-parrot-for-sale-texas/index.astro",
}

# Pages that use CityPageLayout — breadcrumb already moved in layout component
# These pages don't contain <Breadcrumb> directly, so they'll auto-skip.

def extract_breadcrumb(content):
    """Return (full_tag, start, end) for the first <Breadcrumb .../> in content."""
    start = content.find('<Breadcrumb')
    if start == -1:
        return None, -1, -1
    pos = start + len('<Breadcrumb')
    while pos < len(content):
        if content[pos:pos+2] == '/>':
            end = pos + 2
            return content[start:end], start, end
        pos += 1
    return None, -1, -1


def find_section_line_before(content, before_index):
    """Find the start of the line containing the last <section before before_index."""
    snippet = content[:before_index]
    # Find all <section occurrences
    matches = list(re.finditer(r'<section\b', snippet))
    if not matches:
        return -1
    last = matches[-1]
    # Go to line start
    line_start = snippet.rfind('\n', 0, last.start()) + 1
    return line_start


def process_file(filepath):
    if filepath in SKIP_FILES:
        return "skipped"

    with open(filepath, 'r') as f:
        content = f.read()

    if '<Breadcrumb' not in content:
        return "no-breadcrumb"

    bc_tag, bc_start, bc_end = extract_breadcrumb(content)
    if not bc_tag:
        return "parse-error"

    # Find <section line just before the breadcrumb
    section_line_start = find_section_line_before(content, bc_start)
    if section_line_start == -1:
        return "no-section-before (already outside?)"

    # Find the full line that contains the breadcrumb (start of line to end of line)
    bc_line_start = content.rfind('\n', 0, bc_start) + 1
    bc_line_end = content.find('\n', bc_end)
    if bc_line_end == -1:
        bc_line_end = len(content)

    # Check if there's a blank line right after the breadcrumb line
    after_bc = content[bc_line_end:]
    strip_extra_newline = after_bc.startswith('\n')

    # Build the breadcrumb wrapper (2-space indent matches surrounding code)
    bc_clean = bc_tag.strip()
    # Reformat multi-line items to consistent 4-space indent inside wrapper
    wrapper = f'  <div style="max-width:1200px;margin:0 auto;">\n    {bc_clean}\n  </div>\n\n'

    # Remove breadcrumb line from original location
    remove_end = bc_line_end + (1 if strip_extra_newline else 0)
    new_content = content[:bc_line_start] + content[remove_end:]

    # Recalculate section_line_start after removal (it was before bc_line_start, so unchanged)
    # Insert wrapper before section line
    new_content = new_content[:section_line_start] + wrapper + new_content[section_line_start:]

    if new_content == content:
        return "no-change"

    with open(filepath, 'w') as f:
        f.write(new_content)
    return "fixed"


def main():
    results = {"fixed": [], "skipped": [], "no-breadcrumb": [], "error": []}

    for root, dirs, files in os.walk(PAGES_DIR):
        # Skip hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fname in sorted(files):
            if not fname.endswith('.astro'):
                continue
            filepath = os.path.join(root, fname)
            result = process_file(filepath)
            rel = os.path.relpath(filepath, PAGES_DIR)
            if result == "fixed":
                results["fixed"].append(rel)
                print(f"  FIXED   {rel}")
            elif result not in ("no-breadcrumb", "skipped"):
                results["error"].append((rel, result))
                print(f"  INFO    {rel}: {result}")

    print(f"\nSummary: {len(results['fixed'])} fixed, {len(results['error'])} info/errors")


if __name__ == "__main__":
    main()

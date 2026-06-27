"""
Migrate breadcrumb placement: move <Breadcrumb> from its own wrapper div
into the first inner <div> of the following hero <section>.

Handles all 4 patterns found in the CAG site:
  1. <div class="page-container">   → cmp-hero / care-hero / named Astro heroes
  2. <div class="max-w-7xl ...">    → blog pages with style background
  3. <div class="max-w-7xl ...">    → bg-logo-dark Tailwind pages (multi-line items)
  4. <div class="max-w-5xl ...">    → bg-green Tailwind pages (multi-line items)
"""

import os
import re
import sys


def transform(content: str) -> tuple[str, bool]:
    lines = content.splitlines(keepends=True)
    out = []
    i = 0
    changed = False

    while i < len(lines):
        stripped = lines[i].rstrip('\n').strip()

        # ── Step 1: detect a div that is a breadcrumb wrapper ──────────────
        # Match any opening <div ...> that is NOT a self-contained one-liner
        # with content (those are hero/content divs, not wrappers).
        if (
            not changed
            and re.match(r'<div\s+[^>]+>$', stripped)
        ):
            indent = len(lines[i]) - len(lines[i].lstrip())

            # Look ahead past blank lines to the first real content line
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1

            if j < len(lines) and lines[j].strip().startswith('<Breadcrumb'):
                # ── Found the breadcrumb wrapper ──────────────────────────

                # Collect all lines of the <Breadcrumb ... /> call (may span multiple lines)
                bc_lines = []
                k = j
                while k < len(lines):
                    bc_lines.append(lines[k])
                    if '/>' in lines[k]:
                        break
                    k += 1

                # Find the closing </div> of the wrapper (first one after breadcrumb)
                m = k + 1
                while m < len(lines):
                    if lines[m].strip() == '</div>':
                        wrapper_close = m
                        break
                    m += 1
                else:
                    # Can't find closing div — skip, leave unchanged
                    out.append(lines[i])
                    i += 1
                    continue

                # ── Step 2: skip past wrapper + trailing blank lines ──────
                after_wrapper = wrapper_close + 1
                while after_wrapper < len(lines) and lines[after_wrapper].strip() == '':
                    after_wrapper += 1

                # ── Step 3: emit everything between wrapper end and section ─
                # (may include <!-- comments --> or blank lines)
                section_idx = after_wrapper
                while section_idx < len(lines):
                    if lines[section_idx].strip().startswith('<section'):
                        break
                    section_idx += 1
                else:
                    # No following section — skip transformation
                    out.append(lines[i])
                    i += 1
                    continue

                # Emit lines from after_wrapper up to and including the <section line
                for x in range(after_wrapper, section_idx + 1):
                    out.append(lines[x])

                # ── Step 4: find first <div inside the hero section ────────
                div_idx = section_idx + 1
                while div_idx < len(lines):
                    s = lines[div_idx].strip()
                    if s.startswith('<div'):
                        break
                    out.append(lines[div_idx])
                    div_idx += 1
                else:
                    # No inner div found — skip transformation
                    i = div_idx
                    continue

                # Emit the opening div of the hero's inner container
                out.append(lines[div_idx])

                # ── Step 5: insert breadcrumb with correct indentation ────
                # Indent = hero inner div indent + 2 spaces
                hero_div_indent = len(lines[div_idx]) - len(lines[div_idx].lstrip())
                bc_indent = ' ' * (hero_div_indent + 2)

                for bc_line in bc_lines:
                    out.append(bc_indent + bc_line.strip() + '\n')

                # Continue from after the hero inner div line
                i = div_idx + 1
                changed = True
                continue

        out.append(lines[i])
        i += 1

    return ''.join(out), changed


def main():
    src_dir = os.path.join(os.path.dirname(__file__), '..', 'src')
    files_changed = []
    files_skipped = []

    for root, dirs, files in os.walk(src_dir):
        # Skip node_modules just in case
        dirs[:] = [d for d in dirs if d != 'node_modules']
        for fname in files:
            if not fname.endswith('.astro'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            if '<Breadcrumb' not in content:
                continue

            new_content, changed = transform(content)
            if changed:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                rel = os.path.relpath(fpath, os.path.join(src_dir, '..'))
                files_changed.append(rel)
            else:
                rel = os.path.relpath(fpath, os.path.join(src_dir, '..'))
                files_skipped.append(rel)

    print(f"\n✓ Changed ({len(files_changed)}):")
    for f in sorted(files_changed):
        print(f"  {f}")

    print(f"\n⚠ Skipped / already correct ({len(files_skipped)}):")
    for f in sorted(files_skipped):
        print(f"  {f}")


if __name__ == '__main__':
    main()

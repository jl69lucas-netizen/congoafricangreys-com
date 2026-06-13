#!/usr/bin/env python3
"""Split <p> blocks whose plain-text length > LIMIT at the sentence boundary
nearest the midpoint, recursively, until each segment is <= LIMIT or has no
interior sentence boundary. Preserves the <p> opening-tag attributes + the
source indentation. Skips abbreviations and decimals. Never splits inside a tag.

Usage:
  python3 scripts/split_long_paragraphs.py <slug> [--apply]
Without --apply it is a dry run (reports only).
"""
import re, html, sys

LIMIT = 240
MIN_SEG = 55  # don't create a fragment with fewer plain-text chars than this
ABBREV = {
    'u.s', 'e.g', 'i.e', 'mr', 'mrs', 'ms', 'dr', 'vs', 'etc', 'inc', 'st',
    'ave', 'no', 'fig', 'approx', 'oz', 'lb', 'lbs', 'ft', 'sr', 'jr', 'co',
}

def plain_len(s: str) -> int:
    return len(html.unescape(re.sub(r'<[^>]+>', '', s)).strip())

def tag_mask(s: str):
    """Return a list[bool]: True where index i is inside an HTML tag (< .. >)."""
    inside = []
    depth = 0
    for ch in s:
        if ch == '<':
            depth += 1
            inside.append(True)
        elif ch == '>':
            inside.append(True)
            depth = max(0, depth - 1)
        else:
            inside.append(depth > 0)
    return inside

def cut_points(inner: str):
    """Return indices `cut` where the right segment can start (a new sentence).
    Split keeps closing tags (e.g. `.</strong>`) with the left segment."""
    mask = tag_mask(inner)
    out = []
    for i in range(1, len(inner) - 2):
        if inner[i] not in '.!?':
            continue
        if mask[i]:  # period inside a tag's attributes
            continue
        # scan forward skipping whitespace and complete closing tags </...>
        j = i + 1
        saw_space = False
        while j < len(inner):
            if inner[j] == ' ':
                saw_space = True
                j += 1
            elif inner.startswith('</', j):
                end = inner.find('>', j)
                if end == -1:
                    break
                j = end + 1
            else:
                break
        if j >= len(inner) or not saw_space:
            continue
        nxt = inner[j]
        # next sentence must start with a capital, or an opening tag
        if not (nxt.isupper() or (nxt == '<' and not inner.startswith('</', j))):
            continue
        # abbreviation guard: word immediately before the period
        k = i
        word = ''
        while k >= 0 and (inner[k].isalpha() or inner[k] == '.'):
            word = inner[k] + word
            k -= 1
        if word.rstrip('.').lower() in ABBREV:
            continue
        out.append(j)
    return out

def split_inner(inner: str):
    if plain_len(inner) <= LIMIT:
        return [inner]
    cuts = cut_points(inner)
    if not cuts:
        return [inner]
    total = plain_len(inner)
    mid = total / 2
    best, best_d = None, None
    for c in cuts:
        left = inner[:c]
        right = inner[c:]
        lp, rp = plain_len(left), plain_len(right)
        if lp < MIN_SEG or rp < MIN_SEG:
            continue
        d = abs(lp - mid)
        if best_d is None or d < best_d:
            best, best_d = c, d
    if best is None:
        return [inner]
    return split_inner(inner[:best]) + split_inner(inner[best:])

def main():
    slug = sys.argv[1]
    apply = '--apply' in sys.argv
    path = f'src/pages/{slug}/index.astro'
    src = open(path).read()
    pat = re.compile(r'(?P<indent>[ \t]*)<p(?P<attrs>\b[^>]*)>(?P<inner>.*?)</p>', re.S)
    splits = 0

    def repl(m):
        nonlocal splits
        inner = m.group('inner')
        if plain_len(inner) <= LIMIT:
            return m.group(0)
        segs = split_inner(inner)
        if len(segs) == 1:
            return m.group(0)
        splits += 1
        indent = m.group('indent')
        attrs = m.group('attrs')
        open_tag = f'<p{attrs}>'
        joined = ('</p>\n' + indent + open_tag).join(s.strip() for s in segs)
        return indent + open_tag + joined + '</p>'

    new = pat.sub(repl, src)
    # report remaining offenders
    remaining = []
    for m in pat.finditer(new):
        pl = plain_len(m.group('inner'))
        if pl > LIMIT:
            remaining.append(pl)
    print(f'{slug}: split {splits} paragraphs; remaining >{LIMIT}: {len(remaining)} '
          f'(max {max(remaining) if remaining else 0})')
    if apply and new != src:
        open(path, 'w').write(new)
        print(f'  WROTE {path}')

if __name__ == '__main__':
    main()

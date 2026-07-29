#!/usr/bin/env python3
"""
Seam↔section parity probe. Owned by skills/cag-page-hardening.md.

House idiom (2026-07-26): one `<div class="seam">` before every section. The hero
section carries no seam above it, so `sections - seams <= 1` is correct and
`sections - seams > 1` means a section shipped without its seam
(health-guarantee shipped 7 seams across 17 sections).

Do NOT count sections by class. congo/timneh/baby/eggs/dna-tested/hand-raised use
`<section id=...>` with no class, so the previously published
`grep -c '<section class="sec"'` returned 0 and compared against nothing.
See skills/cag-gate-integrity.md — a gate that examined nothing is not a pass.

Usage:
  python3 scripts/seam_parity.py                    # every page under src/pages
  python3 scripts/seam_parity.py <slug> [<slug>]    # named pages
Exit code 1 if any page FAILs, or if the slug filter matched nothing.
"""
import re, sys, glob

SECTION = re.compile(r"<section\b", re.I)
CLASS_ATTR = re.compile(r'class="([^"]*)"', re.I)


def count_sections(text):
    return len(SECTION.findall(text))


def count_seams(text):
    """Count elements whose class list contains the EXACT token `seam`.

    Do not use a `\\bseam\\b` regex: `-` is a word boundary, so `class="seam-wrap"`
    matches and every seam gets counted twice (health-guarantee read 34 for 17
    real seams on 2026-07-29). Tokenise the attribute instead.
    """
    return sum(1 for m in CLASS_ATTR.finditer(text) if "seam" in m.group(1).split())


def verdict(text):
    """Return (PASS|FAIL, sections, seams). Tolerance of 1 = the seamless hero."""
    s, m = count_sections(text), count_seams(text)
    return ("PASS" if s - m <= 1 else "FAIL", s, m)


def main():
    slugs = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = sorted(glob.glob("src/pages/**/index.astro", recursive=True))
    if slugs:
        files = [f for f in files if any(s in f for s in slugs)]
    if not files:
        print("seam-parity: 0 pages matched — CHECK YOUR SLUGS, this is not a pass.")
        print("  (zsh does not word-split an unquoted $VAR: pass slugs literally or use ${=VAR})")
        return 1
    bad = 0
    print(f"seam-parity — {len(files)} pages examined\n")
    for f in files:
        v, s, m = verdict(open(f, encoding="utf-8").read())
        parts = f.split("/")
        slug = parts[2] if len(parts) > 3 else parts[-1]
        print(f"  {v:4}  {slug:<52} sections={s:<3} seams={m:<3} missing={max(0, s - m - 1)}")
        bad += v == "FAIL"
    print(f"\n{bad} FAIL / {len(files)} pages")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

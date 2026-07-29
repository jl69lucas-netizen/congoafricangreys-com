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


SEAM_TOKENS = {"seam", "cag-seam"}


def count_seams(text):
    """Count elements whose class list contains an exact seam token.

    TWO idioms ship on this site and both are seams: `class="seam"` on the for-sale
    cluster (291 uses) and `class="cag-seam"` for the shared component used
    everywhere else (913 uses). Accepting only `seam` read ZERO seams on 83 of 108
    pages and reported them all as FAIL (2026-07-29).

    Do NOT reach for a `\\bseam\\b` regex instead: `-` is a word boundary, so
    `class="seam-wrap"` matches and every seam counts twice (health-guarantee read
    34 for 17 real). Tokenise the attribute — that also keeps `seamless` out.
    """
    return sum(1 for m in CLASS_ATTR.finditer(text)
               if SEAM_TOKENS & set(m.group(1).split()))


def verdict(text):
    """Return (PASS|FAIL|N/A, sections, seams).

    Tolerance of 1 = the hero section, which carries no seam above it.

    `N/A` when the page ships NO seams at all: one-seam-per-section is a for-sale /
    comparison-cluster convention, not a sitewide law, so a page that never uses the
    idiom is not violating it. Treating zero as FAIL reported 71 of 108 pages broken
    (2026-07-29) — a statement about this probe's scope, not about the pages. The
    real defect this gate exists to catch is health-guarantee's 7 seams across 17
    sections: seams present, but short.
    """
    s, m = count_sections(text), count_seams(text)
    if m == 0:
        return ("N/A", s, m)
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
    bad = na = 0
    print(f"seam-parity — {len(files)} pages examined\n")
    for f in files:
        v, s, m = verdict(open(f, encoding="utf-8").read())
        # Nested-slug aware: src/pages/available/<bird>/index.astro must print
        # "available/<bird>", not "available" seven times over.
        parts = f.split("/")
        slug = "/".join(parts[2:-1]) if len(parts) > 3 else parts[-1]
        if v == "N/A":
            na += 1
        else:
            print(f"  {v:4}  {slug:<52} sections={s:<3} seams={m:<3} "
                  f"missing={max(0, s - m - 1)}")
        bad += v == "FAIL"
    print(f"\n{bad} FAIL / {len(files) - na} pages using the seam idiom "
          f"({na} N/A — no seams, idiom not in use)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

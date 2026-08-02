#!/usr/bin/env python3
"""Compute the rework rate for a date window and append it to the ledger.

The rework rate is the metric the self-improving quality loop is judged on
(spec §5: 24.8% baseline on 2026-05-01..2026-07-31, target under 15% at 90 days).

Usage:
    python3 scripts/rework_ledger.py --from 2026-05-01 --to 2026-07-31
    python3 scripts/rework_ledger.py --last-30-days
    python3 scripts/rework_ledger.py --from ... --to ... --dry-run

Import-safe: nothing runs at import time, so the pytest suite can exercise the
classifier without touching git or the ledger file.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
from datetime import date, timedelta

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "quality" / "rework-ledger.json"

# The canonical classifier from spec §1. Anchored at the start for `fix`/`revert`
# so `refactor: prefixed ids` is not rework, and matched as a whole word elsewhere
# so `affix` is not either. Changing this regex changes the metric — if you must,
# recompute every historical window in the same commit and say so.
REWORK_RE = re.compile(
    r"^(fix|revert)\b|\bfix\(|\bcorrect|\brestore|\bregress|\bundo\b|\brepair|\bpatch\(",
    re.IGNORECASE,
)

# Domain buckets. The first seven are the harness families verbatim, so a ledger
# row and a scorecard row name the same thing; GATE, A11Y and COPY cover rework
# the harness does not measure.
DOMAIN_PATTERNS = [
    ("IMG", r"\bimg\b|image|srcset|webp|infographic|crop|alt text|photo|avatar"),
    ("LAYOUT", r"mobile|responsive|overflow|breakpoint|viewport|stack|grid|column|width"),
    ("NAV", r"\bnav\b|anchor|jump|rail|breadcrumb|link|scroll"),
    ("CSS", r"\bcss\b|token|palette|dead rule|class|style"),
    ("GATE", r"gate|probe|scan|audit|checker|harness|lied|false positive"),
    ("SCHEMA", r"schema|json-?ld|canonical|sitemap|\bdate|offer|product"),
    ("SEM", r"heading|h1|h2|h[3-6]\b|outline|title case|hierarch"),
    ("DUP", r"duplicat|crossover|dedup|sibling"),
    ("A11Y", r"a11y|accessib|contrast|wcag|aria|focus"),
    ("COPY", r"\bcopy\b|voice|typo|wording|prose|grammar"),
]


def is_rework(subject: str) -> bool:
    """True when a commit subject describes undoing or correcting earlier work."""
    return bool(REWORK_RE.search(subject))


def classify(subject: str) -> list:
    """Every domain a subject touches. Categories overlap by design — one commit
    can be both an IMG and a LAYOUT fix, and forcing a single bucket would
    understate whichever pattern happened to be listed second."""
    return [name for name, pat in DOMAIN_PATTERNS if re.search(pat, subject, re.IGNORECASE)]


def git_commits(frm: str, to: str, cwd: pathlib.Path = ROOT) -> list:
    """(subject, files) for every commit in [frm, to).

    The file list is what separates PAGE rework from HARNESS self-repair. Without it the
    metric counts a checker fix the same as a page fix — and since the learning loop
    REQUIRES escaped defects to be charged to the harness, the headline then worsens
    every time the loop works as designed. Measured 2026-08-03: of 74 rework commits in
    the 30-day window, 36 edited no page at all.

    Raises rather than returning [] on a git error — an empty list would be recorded as a
    0% rework window, which is a lie shaped exactly like success.
    """
    out = subprocess.run(
        ["git", "log", f"--since={frm}", f"--until={to}",
         "--pretty=format:\x01%s", "--name-only"],
        cwd=cwd, capture_output=True, text=True, check=True,
    )
    commits = []
    for chunk in out.stdout.split("\x01"):
        if not chunk.strip():
            continue
        lines = chunk.splitlines()
        subject, files = lines[0].strip(), [f for f in lines[1:] if f.strip()]
        if subject:
            commits.append((subject, files))
    return commits


# A commit is PAGE work when it changes something the visitor can load. Anything else —
# tests/, scripts/, docs/, rules/, .claude/ — is tooling: real work, but not the rework
# this metric exists to drive down.
PAGE_PREFIXES = ("src/", "public/", "site/")


def touches_page(files: list) -> bool:
    return any(f.startswith(PAGE_PREFIXES) for f in files)


def window(frm: str, to: str, commits: list) -> dict:
    """Two rates, one regex.

    `page_rate` is the headline — rework that changed something a visitor loads. It is
    what the harness is meant to drive down. `harness_rate` is self-repair, tracked
    separately because it is a DESIGNED output of the learning loop rather than a defect
    in the pages, and folding it into the headline inverts the incentive: improving the
    harness would make the number worse. `rate` is retained as the union so the series
    stays comparable with windows recorded before 2026-08-03.
    """
    total = len(commits)
    rework = [(s_, f) for s_, f in commits if is_rework(s_)]
    page = [(s_, f) for s_, f in rework if touches_page(f)]
    harness = [(s_, f) for s_, f in rework if not touches_page(f)]
    by_domain = {}
    for s_, _ in page:
        for d in classify(s_):
            by_domain[d] = by_domain.get(d, 0) + 1
    rate = lambda n: round(n / total, 4) if total else 0.0
    return {
        "from": frm,
        "to": to,
        "total": total,
        "rework": len(rework),
        "rate": rate(len(rework)),
        "page_rework": len(page),
        "page_rate": rate(len(page)),
        "harness_rework": len(harness),
        "harness_rate": rate(len(harness)),
        "by_domain": by_domain,
    }


def append_window(path: pathlib.Path, w: dict) -> dict:
    """Upsert by (from, to) so a re-run corrects a window instead of duplicating it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        data = json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"definition": "see docs/superpowers/specs/2026-07-31-self-improving-quality-loop-design.md §1", "windows": []}
    data["windows"] = [x for x in data["windows"] if (x["from"], x["to"]) != (w["from"], w["to"])]
    data["windows"].append(w)
    data["windows"].sort(key=lambda x: x["from"])
    path.write_text(json.dumps(data, indent=2) + "\n")
    return data


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--from", dest="frm")
    ap.add_argument("--to", dest="to")
    ap.add_argument("--last-30-days", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    if args.last_30_days:
        today = date.today()
        frm, to = str(today - timedelta(days=30)), str(today)
    elif args.frm and args.to:
        frm, to = args.frm, args.to
    else:
        ap.error("give --from and --to, or --last-30-days")

    w = window(frm, to, git_commits(frm, to))
    print(f"{frm} .. {to}: PAGE {w['page_rework']}/{w['total']} = {w['page_rate']:.1%}"
          f"  ·  harness self-repair {w['harness_rework']} = {w['harness_rate']:.1%}")
    for d, n in sorted(w["by_domain"].items(), key=lambda kv: -kv[1]):
        print(f"  {d:<8}{n:>5}")
    if args.dry_run:
        print("(dry run — ledger not written)")
        return 0
    append_window(LEDGER, w)
    print(f"wrote {LEDGER.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

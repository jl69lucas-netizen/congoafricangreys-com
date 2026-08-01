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


def git_subjects(frm: str, to: str, cwd: pathlib.Path = ROOT) -> list:
    """Commit subjects in [frm, to). Raises rather than returning [] on a git error —
    an empty list would be recorded as a 0% rework window, which is a lie shaped
    exactly like success."""
    out = subprocess.run(
        ["git", "log", f"--since={frm}", f"--until={to}", "--pretty=format:%s"],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in out.stdout.splitlines() if line.strip()]


def window(frm: str, to: str, subjects: list) -> dict:
    total = len(subjects)
    rework = [s for s in subjects if is_rework(s)]
    by_domain = {}
    for s in rework:
        for d in classify(s):
            by_domain[d] = by_domain.get(d, 0) + 1
    return {
        "from": frm,
        "to": to,
        "total": total,
        "rework": len(rework),
        "rate": round(len(rework) / total, 4) if total else 0.0,
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

    w = window(frm, to, git_subjects(frm, to))
    print(f"{frm} .. {to}: {w['rework']}/{w['total']} = {w['rate']:.1%} rework")
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

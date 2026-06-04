#!/usr/bin/env python3
"""Inject the First-Person Brand Voice rule into every agent's Golden Rule block.

Idempotent: skips any file that already contains the marker phrase.
Inserts the rule as the first blockquote line directly under `## Golden Rule`.
"""
import pathlib
import sys

AGENTS = pathlib.Path(__file__).resolve().parent.parent / ".claude" / "agents"
MARKER = "First-Person Brand Voice (ALWAYS)"
LINE = (
    "> **First-Person Brand Voice (ALWAYS):** Write as the breeder — \"we / our / "
    "here at C.A.Gs.\" Frame our birds, credentials, and process as *ours*, not from "
    "the outside. Exceptions (stay neutral): encyclopedic species/taxonomy facts and "
    "cited research. Never fabricate — every claim is bounded by the Verified-Claim "
    "Ledger and real CAG data (GSC/competitors/codebase), never invented.\n"
)

changed, skipped, no_rule = [], [], []

for f in sorted(AGENTS.glob("*.md")):
    text = f.read_text()
    if MARKER in text:
        skipped.append(f.name)
        continue
    lines = text.splitlines(keepends=True)
    out, inserted = [], False
    for ln in lines:
        out.append(ln)
        if not inserted and ln.strip() == "## Golden Rule":
            out.append(LINE)
            inserted = True
    if not inserted:
        no_rule.append(f.name)
        continue
    f.write_text("".join(out))
    changed.append(f.name)

print(f"changed: {len(changed)}")
print(f"skipped (already had marker): {len(skipped)}")
print(f"NO '## Golden Rule' heading: {len(no_rule)} -> {no_rule}")
if no_rule:
    sys.exit(0)  # report, don't fail

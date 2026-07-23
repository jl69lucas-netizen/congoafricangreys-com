#!/usr/bin/env python3
"""Inject the Heading Hierarchy Outline Gate into every agent's Golden Rule block.

Breeder decision 2026-06-20: the full H1->H6 outline is approved BEFORE any page
code is touched, levels descend with no skips, and every page carries all six
levels with at least 5 H5 AND 5 H6. Enforced mechanically by
scripts/final_page_audit.py (all_six_levels / min_h5_5 / min_h6_5 = hard FAIL).

Idempotent: skips any file that already contains the marker phrase.
Inserts as the first blockquote line under `## Golden Rule`.
Re-run after adding any new agent.
"""
import pathlib
import sys

AGENTS = pathlib.Path(__file__).resolve().parent.parent / ".claude" / "agents"
MARKER = "Heading Hierarchy Outline Gate (ALWAYS)"
LINE = (
    "> **Heading Hierarchy Outline Gate (ALWAYS):** Before writing or changing ANY page, first "
    "present the COMPLETE H1→H6 outline — every heading, in render order, labelled by level — and "
    "get explicit approval. No page code is touched until the outline is approved. Levels descend "
    "sequentially with NO skipped levels (H3→H6 and H2→H4 are BANNED; stepping back up to start a "
    "new section is fine). Every page carries all six levels with a MINIMUM of 5 H5 AND 5 H6. "
    "Semantic map: H1 page topic · H2 search intents · H3 subtopics · H4 micro-intent/PAA answers · "
    "H5 supporting facts/warnings · H6 ultra-specific details/breeder notes/citations. Every "
    "heading is AP-style Title Case (see the Title Case rule). Verify with "
    "`python3 scripts/final_page_audit.py`.\n"
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

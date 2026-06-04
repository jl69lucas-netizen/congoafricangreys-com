#!/usr/bin/env python3
"""Inject the Clarification Checkpoint rule into every agent's Golden Rule block.

Upgrades the <97% Confidence Gate behavior site-wide: instead of a dead-stop,
agents write finished work to disk, log the open question to the live session
brief, ask ONE narrow question, and keep building everything not blocked.

Idempotent: skips any file that already contains the marker phrase.
Inserts the rule as the first blockquote line directly under `## Golden Rule`,
so it sits above (and modifies the behavior of) any existing Confidence Gate line.
This AUGMENTS data-integrity Confidence-Gate variants (e.g. "only report data you
retrieved from a live fetch") rather than replacing them.
"""
import pathlib
import sys

AGENTS = pathlib.Path(__file__).resolve().parent.parent / ".claude" / "agents"
MARKER = "Clarification Checkpoint (ALWAYS)"
LINE = (
    "> **Clarification Checkpoint (ALWAYS):** Below the ≥97% Confidence Gate, do NOT "
    "dead-stop the whole job. First write finished work to disk (cleared sections to the "
    "page; in-progress notes + the open question to the live session brief's `## Open Flags`), "
    "then ask the user ONE narrow question, then keep building every part that isn't blocked. "
    "Only the uncertain unit waits for the answer. A stop must never cost more than that one "
    "piece, and the question must survive session teardown (it's on disk, not just in chat).\n"
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

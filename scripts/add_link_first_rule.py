#!/usr/bin/env python3
"""Inject the Link-First rule into every agent's Golden Rule block.

Breeder decision 2026-07-11: ALL internal and external links anchor at the
START of the sentence/paragraph — never mid-sentence, never at the end.
This supersedes the older "beginning or middle, never end" rule everywhere.

Idempotent: skips any file that already contains the marker phrase.
Inserts as the first blockquote line under `## Golden Rule`.
Re-run after adding any new agent.
"""
import pathlib
import sys

AGENTS = pathlib.Path(__file__).resolve().parent.parent / ".claude" / "agents"
MARKER = "Link-First (ALWAYS)"
LINE = (
    "> **Link-First (ALWAYS):** For ALL internal and external links, the anchor sits at the "
    "START of the sentence/paragraph — inside the opening words (first clause). Never "
    "mid-sentence, never at the end. ✅ `Our <a>Congo African Grey care guide</a> covers diet "
    "in depth…` · ❌ `…diet is covered in our <a>care guide</a>.` (Supersedes the old "
    "beginning-or-middle rule, 2026-07-11. Sole exception: branded ACTION anchors on CTAs "
    "per skills/cag-branded-hybrid-keywords.md.)\n"
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

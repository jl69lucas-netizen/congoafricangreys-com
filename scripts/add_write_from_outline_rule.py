#!/usr/bin/env python3
"""Inject the Write-From-Outline rule into every agent's Golden Rule block.

Breeder decision 2026-07: never scaffold a page from a sibling's .astro/.md and
reword its sentences to pass the dup-gate. Reuse components, CSS and structural
patterns freely; write every page's PROSE fresh from its own approved outline.

Idempotent: skips any file that already contains the marker phrase.
Inserts as the first blockquote line under `## Golden Rule`.
Re-run after adding any new agent.
"""
import pathlib
import sys

AGENTS = pathlib.Path(__file__).resolve().parent.parent / ".claude" / "agents"
MARKER = "Write-From-Outline, NEVER-From-Sibling (ALWAYS)"
LINE = (
    "> **Write-From-Outline, NEVER-From-Sibling (ALWAYS):** Do NOT open a sibling page to copy or "
    "paraphrase paragraphs — open it only to read its component/CSS structure. Reuse components, "
    "CSS classes and structural patterns freely (that IS the kit), but write every page's PROSE "
    "fresh from ITS OWN approved outline + distribution matrix, in genuinely different framing, "
    "sentence structure, angle and vocabulary, leaning on that page's own entity/angle. Only the "
    "whitelist may match verbatim (shipping line, doc-badge lists, counter strip, CITES notice, "
    "CTA labels, real reviews, real page-name link labels). Run `scripts/dup_content_audit.py` AND "
    "`--headers` on YOUR OWN draft BEFORE calling it done, targeting zero non-whitelist crossover — "
    "dedup is a pre-write discipline, not post-hoc cleanup.\n"
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

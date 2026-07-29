#!/usr/bin/env python3
"""Inject the Header-Style Declaration rule into every agent's Golden Rule block.

Idempotent. Inserts as the first blockquote line under `## Golden Rule`, matching
scripts/add_title_case_rule.py so the five injected rules stay in one place.

Re-run after adding any agent (CLAUDE.md: a rule with no injector is 0/68).

Usage: python3 scripts/add_header_style_rule.py [--dry-run]
"""
import sys, glob

MARKER = "Header Style Declaration (ALWAYS)"
RULE = (
    "> **Header Style Declaration (ALWAYS):** every H1–H6 outline you present must "
    "declare its header style — **Style 1** Pure Conversational / **Style 2** "
    "Conversational Hybrid / **Style 3** Recommended Hybrid — plus its register "
    "(FAQ / Quora / Reddit), with a reason grounded in that page's own query set, "
    "SERP snapshot, PAA demand or a named competitor gap (never taste) and a named "
    "trade-off. Defaults by page type: Style 3 for transactional + comparison, "
    "Style 2 for informational / care / location / blog, FAQ register for bird "
    "listings, Reddit register for Reddit-modifier pages. Full spec: "
    "`skills/framework-heading-hierarchy.md` §Header Style Selection. An outline "
    "with no style line does not pass the gate. Title Case still applies to every "
    "heading whatever the style."
)
DRY = "--dry-run" in sys.argv


def main():
    files = sorted(glob.glob(".claude/agents/*.md"))
    if not files:
        print("0 agents examined — THIS IS NOT A PASS. Check the glob / cwd.")
        return 1

    injected = already = no_rule = 0
    missing = []
    for f in files:
        lines = open(f, encoding="utf-8").read().split("\n")
        if any(MARKER in ln for ln in lines):
            already += 1
            continue
        out, done = [], False
        for ln in lines:
            out.append(ln)
            if not done and ln.strip() == "## Golden Rule":
                out.append(RULE)
                done = True
        if not done:
            no_rule += 1
            missing.append(f)
            continue
        if not DRY:
            open(f, "w", encoding="utf-8").write("\n".join(out))
        injected += 1

    print(f"{len(files)} agents examined · {injected} injected · {already} already had it "
          f"· {no_rule} missing a '## Golden Rule' heading")
    if missing:
        print("  NO '## Golden Rule' heading:", missing)
    return 1 if no_rule else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Inject the Title Case heading standard into every agent's Golden Rule block.

Breeder decision 2026-07-23: every H1-H6 on every page uses AP-style Title Case,
matching the homepage and the congo / timneh / hand-raised for-sale pages.
Sentence-case headings are a defect. FAQ accordion questions live in <summary>,
not a heading tag, and stay conversational sentence case.

Idempotent: skips any file that already contains the marker phrase.
Inserts as the first blockquote line under `## Golden Rule`.
Re-run after adding any new agent.
"""
import pathlib
import sys

AGENTS = pathlib.Path(__file__).resolve().parent.parent / ".claude" / "agents"
MARKER = "Title Case Headings (ALWAYS)"
LINE = (
    "> **Title Case Headings (ALWAYS):** Every H1–H6 uses AP-style Title Case — capitalise 4+ letter "
    "words and ALL nouns/verbs/adjectives/adverbs regardless of length (`Is`, `Are`, `Do`, `Be`, "
    "`Not`, `Our`); lowercase mid-title only `a an the and but or nor for so yet at by in of on to "
    "as vs per via`; always capitalise the first word, the last word and the word after `:` `?` `!` "
    "(an em dash does NOT force a capital). Hyphenated compounds capitalise each part "
    "(`Hand-Raised`, `Captive-Bred`); never touch acronyms/brands/domains (`C.A.Gs`, `CITES`, "
    "`USDA`, `DNA`, `PCR`, `IATA`). SCOPE IS HEADINGS ONLY — FAQ questions in `<summary>` stay "
    "conversational sentence case. Verify with `python3 scripts/page_hardening_scan.py <slug>` → "
    "zero `header-not-title-case`.\n"
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

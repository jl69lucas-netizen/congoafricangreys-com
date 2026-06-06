#!/usr/bin/env python3
"""Idempotently add one Interior-Page-Standard pointer line to the interior-page
builder agents' Golden Rule block.

These agents build informational/secondary pages (health, shipping, faq, care,
about, why-choose, scam, policy, etc.) which reuse the homepage design + method.
The pointer makes them read `MANUAL INTERIOR-PAGE CHECKLIST.md` + the master
skill's Interior-Page Profile before building.

Safe to re-run: skips any agent that already has the pointer.
Run from the repo root:  python3 scripts/add_interior_standard_pointer.py
"""
import pathlib

AGENTS = [
    "cag-about-builder",
    "cag-purchase-guide",
    "cag-species-guide-builder",
    "cag-scam-specialist",
    "cag-financial-strategist",
    "cag-faq-agent",
    "cag-section-builder",
    "cag-trust-signals-agent",
]

POINTER = (
    "> **Interior-Page Standard (ALWAYS):** This page type follows the homepage "
    "design + method. Read `MANUAL INTERIOR-PAGE CHECKLIST.md` (Hero → CTA) and "
    "the master skill's *Interior-Page Profile* before building. Keep seam-logo "
    "dividers (`.cag-seam` + `/cag-footer-logo.png`), first-person C.A.Gs voice, "
    "two-keyword conversational headers, the 4-Move entity loop + Verified-Claim "
    "Ledger, woven mid-sentence links, GEO/AEO declarative answer blocks, and the "
    "AA contrast + performance gates. Add `BreadcrumbList` schema."
)

MARKER = "## Golden Rule"
SENTINEL = "MANUAL INTERIOR-PAGE CHECKLIST.md"

base = pathlib.Path(".claude/agents")
changed = 0
for name in AGENTS:
    p = base / f"{name}.md"
    if not p.exists():
        print(f"SKIP missing: {p}")
        continue
    text = p.read_text()
    if SENTINEL in text:
        print(f"OK already:   {name}")
        continue
    if MARKER not in text:
        print(f"WARN no Golden Rule heading: {name}")
        continue
    idx = text.index(MARKER)
    nl = text.index("\n", idx) + 1  # insert right after the heading line
    text = text[:nl] + POINTER + "\n" + text[nl:]
    p.write_text(text)
    changed += 1
    print(f"PATCHED:      {name}")

print(f"\nDone. Patched {changed} agent(s).")

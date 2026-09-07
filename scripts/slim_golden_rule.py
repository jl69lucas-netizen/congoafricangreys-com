#!/usr/bin/env python3
"""Collapse the duplicated site-wide Golden Rule block in every agent to one pointer.

Why (2026-09-07 Fable 5.1 audit): 68 agents carried the same ~5.2 KB block — eight
site-wide rules injected by the add_*_rule.py scripts, ~352 KB in total, ~1,300 tokens on
every invocation, and it drifted (58 files said `site/content/` ships). CLAUDE.md's thirteen
judgment rules + rules/*.md + data/quality/rule-index.json are the single statement now.

What it does, per agent (idempotent — a second run is byte-identical):
  * drops the seven site-wide `> **Label (ALWAYS):**` lines, the two "use Claude Code /
    only call MCPs" lines, and the OLD stop-and-ask `> **Confidence Gate:**` line that the
    Clarification Checkpoint replaced (41 agents still carried both)
  * inserts one pointer paragraph as the first line of `## Golden Rule`
  * keeps every agent-specific `> ` line untouched (Interior-Page Standard, Tooling notes…)
  * in `## CAG Project Context`: content root → src/pages, Confidence Gate → Checkpoint
  * strips the hard-coded `/Users/apple/Downloads/CAG/` prefix everywhere in the file

Usage: python3 scripts/slim_golden_rule.py [--dry-run] [paths...]
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRY = "--dry-run" in sys.argv

POINTER = (
    "> **Bound by the site rules, not by a copy of them:** `CLAUDE.md`'s thirteen judgment rules "
    "(first-person voice · CITES Appendix I · Recommend + Why · restate the brief · preview before apply · "
    "97% Confidence Gate with the Clarification Checkpoint, never a dead-stop · write from the outline, never "
    "from a sibling · no fabricated claims · Verified-Claim Ledger · two brand-owned method labels · Artifact "
    "deliverables) and the packs in `rules/` (headings, images, schema, links, copy, design, gates, deploy, "
    "for-sale), indexed by `data/quality/rule-index.json`. Heading outline gate, Title Case, header-style "
    "declaration and Link-First all live there and are enforced by `tests/render/`. Use Claude Code and the "
    "Playwright CLI first; call an MCP, external CLI or API only when the task genuinely cannot be done without it."
)

SITE_WIDE_LABELS = (
    "Header Style Declaration (ALWAYS):",
    "Write-From-Outline, NEVER-From-Sibling (ALWAYS):",
    "Title Case Headings (ALWAYS):",
    "Heading Hierarchy Outline Gate (ALWAYS):",
    "Link-First (ALWAYS):",
    "Clarification Checkpoint (ALWAYS):",
    "First-Person Brand Voice (ALWAYS):",
    "Confidence Gate:",          # the old stop-and-ask line inside ## Golden Rule
    "Bound by the site rules, not by a copy of them:",  # our own pointer (re-run safety)
)
TOOL_FIRST_RE = re.compile(
    r"^> (Use Claude Code(?: and (?:Playwright CLI|file edits))? to solve problems first\.?"
    r"|Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone\.?"
    r"|Use Claude Code and Playwright CLI to solve problems first\. Only call MCPs/APIs if the task genuinely cannot.*"
    r"|Use Claude Code native tools \(Read, Write, Bash\) to solve all problems\.?)\s*$"
)

CTX_ROOT_OLD = "**Content root:** `site/content/`"
CTX_ROOT_NEW = "**Content root:** `src/pages/<slug>/index.astro` ships (`site/content/` is staging only, never built)"
CTX_GATE_RE = re.compile(r"^> \*\*Confidence Gate:\*\* ≥97% before writing any (?:site|src/ or public/) file(?!\.? Below it, the Clarification Checkpoint)\.?(?: If uncertain[:,] stop, state the uncertainty, ask\.)?(?P<rest>.*)$", re.M)
CTX_GATE_NEW = "> **Confidence Gate:** ≥97% before writing any site file. Below it, the Clarification Checkpoint applies (`CLAUDE.md` rule 8): write finished work to disk, log the question to the brief's `## Open Flags`, ask ONE narrow question, keep building what is not blocked. Never dead-stop."

MAC_PREFIX = "/Users/apple/Downloads/CAG/"


def slim(text: str) -> str:
    lines = text.split("\n")
    out, in_gr, pointer_done = [], False, False
    for ln in lines:
        if ln.startswith("## "):
            in_gr = ln.strip() == "## Golden Rule"
            out.append(ln)
            if in_gr:
                out.append(POINTER)
                pointer_done = True
            continue
        if in_gr and ln.startswith("> "):
            body = ln[2:]
            if any(body.startswith(f"**{lab}**") for lab in SITE_WIDE_LABELS):
                continue
            if TOOL_FIRST_RE.match(ln):
                continue
        out.append(ln)
    text = "\n".join(out)
    text = text.replace(CTX_ROOT_OLD, CTX_ROOT_NEW)
    text = CTX_GATE_RE.sub(lambda m: CTX_GATE_NEW + (m.group("rest") or ""), text)
    text = text.replace(MAC_PREFIX, "")
    # Collapse blank-line runs the removals may have left inside the Golden Rule section.
    text = re.sub(r"(## Golden Rule\n(?:> .*\n)+)\n{2,}", r"\1\n", text)
    return text


def main():
    paths = [Path(p) for p in sys.argv[1:] if not p.startswith("--")] or sorted((ROOT / ".claude" / "agents").glob("*.md"))
    changed = 0
    for p in paths:
        orig = p.read_text()
        new = slim(orig)
        if new != orig:
            changed += 1
            if not DRY:
                p.write_text(new)
            print(f"{'[DRY]' if DRY else '[OK]'} {p.relative_to(ROOT) if p.is_relative_to(ROOT) else p}  {len(orig)} → {len(new)} bytes")
    print(f"\nChanged: {changed} / {len(paths)}" + ("  (DRY RUN)" if DRY else ""))


if __name__ == "__main__":
    main()

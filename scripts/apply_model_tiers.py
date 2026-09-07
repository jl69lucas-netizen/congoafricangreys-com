#!/usr/bin/env python3
"""Write model/effort into agent YAML frontmatter from data/agent-registry.json.

Usage: python3 scripts/apply_model_tiers.py [--dry-run]

2026-09-07 (Fable 5.1 adaptation):
  * `model:` and `effort:` are both NATIVE Claude Code subagent frontmatter fields
    (effort: low | medium | high | xhigh | max), so this script writes exactly those
    two keys and nothing else.
  * The old `<!-- EFFORT:START -->…<!-- EFFORT:END -->` prose directive that stood in
    for a native effort field is STRIPPED on sight — the harness now honours the field.
  * `dynamic_workflow:` is not a recognized frontmatter field; it is removed from the
    agent file and lives only in the registry entry.
Idempotent: a second run over the same tree is byte-identical
(tests/test_apply_model_tiers_idempotent.py).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
REGISTRY = ROOT / "data" / "agent-registry.json"
DIRS = [ROOT / ".claude" / "agents", ROOT / "skills"]
DRY = "--dry-run" in sys.argv

EFFORT_START = "<!-- EFFORT:START -->"
EFFORT_END = "<!-- EFFORT:END -->"
# Whole lines only, plus at most one blank line on each side so the strip leaves no hole.
BLOCK_RE = re.compile(
    rf"\n?^{re.escape(EFFORT_START)}\n.*?^{re.escape(EFFORT_END)}\n\n?",
    re.DOTALL | re.MULTILINE,
)
VALID_EFFORT = {"low", "medium", "high", "xhigh", "max"}


def strip_effort_block(content):
    return BLOCK_RE.sub("\n", content, count=1) if EFFORT_START in content else content


def patch(content, model, effort):
    if effort not in VALID_EFFORT:
        raise ValueError(f"effort must be one of {sorted(VALID_EFFORT)}, got {effort!r}")
    block = f"model: {model}\neffort: {effort}"
    if not content.startswith("---"):
        content = f"---\n{block}\n---\n{content}"
    else:
        end = content.find("\n---", 3)
        if end == -1:
            return content
        fm = content[3:end]
        for key in ("model", "effort", "dynamic_workflow"):
            fm = re.sub(rf"\n{key}:.*", "", fm)
        content = "---" + fm + "\n" + block + content[end:]
    content = strip_effort_block(content)
    # Collapse any run of 3+ newlines the strip may have left directly after the frontmatter.
    fm_close = content.find("\n---\n", 3)
    if fm_close != -1:
        head, tail = content[: fm_close + 5], content[fm_close + 5 :]
        content = head + re.sub(r"^\n{2,}", "\n", tail)
    return content


def main():
    reg = json.loads(REGISTRY.read_text())
    tiers = reg["_meta"]["tiers"]
    patched = warned = 0
    for name, cfg in reg["agents"].items():
        t = tiers[cfg["tier"]]
        for d in DIRS:
            f = d / f"{name}.md"
            if f.exists():
                orig = f.read_text()
                new = patch(orig, t["model"], t["effort"])
                if new != orig:
                    if not DRY:
                        f.write_text(new)
                    print(f"{'[DRY]' if DRY else '[OK]'} {f.relative_to(ROOT)} -> {t['model']} / {t['effort']}")
                    patched += 1
                else:
                    print(f"[SKIP] {f.relative_to(ROOT)} already current")
                break
        else:
            print(f"[WARN] {name}.md not found")
            warned += 1
    print(f"\nPatched: {patched}  Warnings: {warned}" + ("  (DRY RUN)" if DRY else ""))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Patch model/effort/dynamic_workflow into agent YAML frontmatter from the registry.
Usage: python3 scripts/apply_model_tiers.py [--dry-run]"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
REGISTRY = ROOT / "data" / "agent-registry.json"
DIRS = [ROOT / ".claude" / "agents", ROOT / "skills"]
DRY = "--dry-run" in sys.argv

# Behavioral effort directives. Claude Code has no native thinking-budget
# frontmatter field, so effort is enforced via an explicit prompt instruction.
EFFORT_START = "<!-- EFFORT:START -->"
EFFORT_END = "<!-- EFFORT:END -->"
EFFORT_TEXT = {
    "max": (
        "> **Reasoning effort: MAX.** Before producing any output, think step by step "
        "using extended reasoning. Work through the entire problem internally — consider "
        "edge cases, alternatives, and the CAG Confidence Gate — then produce your final answer."
    ),
    "high": (
        "> **Reasoning effort: HIGH.** Think through the key decisions and tradeoffs "
        "before producing output. Do not answer reflexively on non-trivial steps."
    ),
    # medium: no directive — standard inference.
}

# Matches the directive as WHOLE LINES only — no surrounding newlines. Eating the
# newline on either side is what made the old strip/re-insert leak one blank line
# per run (44 excess lines across 42 agents by 2026-07-29).
BLOCK_RE = re.compile(
    rf"^{re.escape(EFFORT_START)}\n.*?^{re.escape(EFFORT_END)}\n",
    re.DOTALL | re.MULTILINE,
)


def strip_effort_block(content):
    """Remove the directive block. Returns (content, offset_it_was_at | None)."""
    m = BLOCK_RE.search(content)
    if not m:
        return content, None
    return content[: m.start()] + content[m.end() :], m.start()


def patch(content, model, effort, dynamic):
    block = f"model: {model}\neffort: {effort}\ndynamic_workflow: {str(dynamic).lower()}"
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

    # Inject/replace the behavioral effort directive. Re-inserting at the offset the
    # old block occupied is what makes the run idempotent AND keeps a hand-placed
    # block where its author put it (e.g. cag-infographic-builder.md keeps a binding
    # image-sizing note above it) instead of hoisting it to just under frontmatter.
    content, was_at = strip_effort_block(content)
    directive = EFFORT_TEXT.get(effort)
    if directive:
        injection = f"{EFFORT_START}\n{directive}\n{EFFORT_END}\n"
        if was_at is not None:
            content = content[:was_at] + injection + content[was_at:]
        else:
            fm_end = content.find("\n---", 3)
            insert_at = content.find("\n", fm_end + 1) + 1  # after the closing '---' line
            content = content[:insert_at] + f"\n{injection}\n" + content[insert_at:]
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
                new = patch(orig, t["model"], t["effort"], cfg.get("dynamic_workflow", False))
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

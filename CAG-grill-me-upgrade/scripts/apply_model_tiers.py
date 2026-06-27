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

    # Inject/replace the behavioral effort directive right after frontmatter.
    content = re.sub(
        rf"\n{re.escape(EFFORT_START)}.*?{re.escape(EFFORT_END)}\n",
        "\n",
        content,
        flags=re.DOTALL,
    )
    directive = EFFORT_TEXT.get(effort)
    if directive:
        fm_end = content.find("\n---", 3)
        insert_at = content.find("\n", fm_end + 1) + 1  # after the closing '---' line
        injection = f"\n{EFFORT_START}\n{directive}\n{EFFORT_END}\n"
        content = content[:insert_at] + injection + content[insert_at:]
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

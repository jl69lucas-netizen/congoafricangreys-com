#!/usr/bin/env python3
"""Deterministic dynamic-workflow router — maps a task description to a model tier.

Mirrors the routing tables embedded in the orchestrator agent prompts
(cag-content-architect, cag-structure-architect, cag-batch-rebuilder) so the
routing logic is testable outside the model.

Usage:
    python3 scripts/route.py "rebuild the florida location page from scratch"
    -> opus48_max  claude-opus-4-8 / max

Exit code 0 always (a tier is always chosen; default is sonnet_medium).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
REGISTRY = ROOT / "data" / "agent-registry.json"

# Ordered most-specific → least. First tier with a matching signal wins.
ROUTING = [
    ("opus48_max", [
        "deep audit", "full rebuild", "full silo", "reverse silo",
        "competitor analysis", "competitor url", "architecture rebuild",
        "new page from scratch", "from scratch", "full page build",
    ]),
    ("opus47_high", [
        "section update", "faq only", "faq", "about page", "comparison page",
        "comparison", "hub page", "spoke page", "cluster build", "variant page",
    ]),
    ("sonnet_high", [
        "monitor", "analytics", "conversion audit", "content calendar",
        "rank track", "keyword gap", "newsletter", "case study",
    ]),
    ("haiku_medium", [
        "canonical fix", "canonical", "redirect", "footer", "link check",
        "internal link audit", "depth check", "orphan scan", "image rename",
        "deploy", "nap citation", "google map",
    ]),
]
DEFAULT = "sonnet_medium"


def route(task: str) -> str:
    t = task.lower()
    for tier, signals in ROUTING:
        if any(sig in t for sig in signals):
            return tier
    return DEFAULT


def main():
    if len(sys.argv) < 2:
        print("usage: route.py <task-description>", file=sys.stderr)
        sys.exit(2)
    task = " ".join(sys.argv[1:])
    tier = route(task)
    tiers = json.loads(REGISTRY.read_text())["_meta"]["tiers"]
    cfg = tiers[tier]
    print(f"{tier}\t{cfg['model']} / {cfg['effort']}")


if __name__ == "__main__":
    main()

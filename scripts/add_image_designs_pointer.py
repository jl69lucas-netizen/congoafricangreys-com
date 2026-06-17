#!/usr/bin/env python3
"""Idempotently add one Image-Art-Direction pointer line to every image
skill/agent that generates, edits, or places imagery.

The pointer makes each consumer read `IMAGE-DESIGNS.md` (repo root) — the image
source of truth (crop ratios, style wrapper, negative list, lighting, focal
length, scene-type-per-page) — before doing any image work. IMAGE-DESIGNS.md
wins over any stale brand value still living in a consumer.

The pointer is inserted right after the first markdown heading line (`#`/`##`)
that is NOT inside a fenced code block — i.e. the document's real title or its
`## Golden Rule` block, never a `#` that is actually a bash comment inside a
```code fence```. (These consumers carry YAML frontmatter + agent/skill scaffolding,
so the "first heading" is fence-aware rather than a naive first-`# ` match.)

Safe to re-run: skips any file that already contains the IMAGE-DESIGNS.md sentinel.
Run from the repo root:  python3 scripts/add_image_designs_pointer.py
"""
import pathlib

# Paths relative to the repo root (this script's parent.parent).
TARGETS = [
    "skills/image-prompt-generator.md",
    "skills/cag-image-generation.md",
    "skills/cag-photo-ingest.md",
    "skills/cag-infographic.md",
    ".claude/agents/cag-image-pipeline.md",
    ".claude/agents/cag-infographic-builder.md",
]

POINTER = (
    "> **Image art-direction:** Read `IMAGE-DESIGNS.md` (repo root) BEFORE "
    "generating, editing, or placing any image — crop ratios, style wrapper, "
    "negative list, lighting, focal length, and scene-type-per-page. It is the "
    "image source of truth; it wins over any stale value here."
)

SENTINEL = "IMAGE-DESIGNS.md"

repo_root = pathlib.Path(__file__).resolve().parent.parent
injected = 0
skipped = 0

for rel in TARGETS:
    p = repo_root / rel
    if not p.exists():
        print(f"MISSING (skip): {rel}")
        continue
    text = p.read_text()
    if SENTINEL in text:
        print(f"skip (already): {rel}")
        skipped += 1
        continue
    lines = text.splitlines(keepends=True)
    insert_at = None
    in_fence = False
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if not in_fence and stripped.startswith("#"):
            insert_at = i + 1
            break
    if insert_at is None:
        print(f"WARN no heading found (skip): {rel}")
        continue
    lines.insert(insert_at, POINTER + "\n")
    p.write_text("".join(lines))
    print(f"injected:       {rel}")
    injected += 1

print(f"\nDone. injected={injected}  skipped={skipped}  (of {len(TARGETS)} targets)")

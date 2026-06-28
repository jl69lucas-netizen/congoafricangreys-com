#!/usr/bin/env python3
"""Register CAG skills for Claude Code Skill-tool discovery.

Source of truth: skills/<name>.md (and skills/<name>/SKILL.md dir-skills).
Target (scanned by the loader): .claude/skills/<name>/SKILL.md

Modes:
  (default)   create/refresh relative symlinks
  --copy      copy file contents instead of symlinking (loader-without-symlink fallback)
  --check     verify every source skill is registered & in sync; exit 1 if not (CI/health gate)
"""
import os, re, sys, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "skills"
DST = ROOT / ".claude" / "skills"

def sources():
    """Yield (name, source_path) for every skill: flat .md files and <name>/SKILL.md dirs."""
    for p in sorted(SRC.glob("*.md")):
        yield p.stem, p
    for d in sorted(SRC.iterdir()):
        sk = d / "SKILL.md"
        if d.is_dir() and sk.exists():
            yield d.name, sk

def has_frontmatter(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    return bool(m and re.search(r"^name:\s*\S", m.group(1), re.M)
                  and re.search(r"^description:\s*\S", m.group(1), re.M))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check():
    bad = []
    for name, src in sources():
        if not has_frontmatter(src):
            bad.append(f"  MISSING FRONTMATTER: skills/{src.relative_to(SRC)}")
            continue
        tgt = DST / name / "SKILL.md"
        if not tgt.exists():
            bad.append(f"  NOT REGISTERED: {name}")
        elif not tgt.is_symlink() and sha(tgt) != sha(src):
            bad.append(f"  OUT OF SYNC (copy drift): {name} — rerun register_skills.py")
    if bad:
        print("Skill registration FAIL:")
        print("\n".join(bad))
        return 1
    print(f"Skill registration OK — {sum(1 for _ in sources())} skills registered.")
    return 0

def build(copy=False):
    n = 0
    for name, src in sources():
        if not has_frontmatter(src):
            print(f"  SKIP (no frontmatter): {name}")
            continue
        d = DST / name
        d.mkdir(parents=True, exist_ok=True)
        tgt = d / "SKILL.md"
        if tgt.exists() or tgt.is_symlink():
            tgt.unlink()
        if copy:
            tgt.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        else:
            rel = os.path.relpath(src, d)
            tgt.symlink_to(rel)
        n += 1
    print(f"Registered {n} skills ({'copy' if copy else 'symlink'} mode) -> .claude/skills/")
    return 0

if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    sys.exit(build(copy="--copy" in sys.argv))

#!/usr/bin/env python3
"""Register CAG skills for Claude Code Skill-tool discovery.

Source of truth: skills/<name>.md (and skills/<name>/SKILL.md dir-skills).
Target (scanned by the loader): .claude/skills/<name>/SKILL.md

Modes:
  (default)   create/refresh relative symlinks
  --copy      copy file contents instead of symlinking (loader-without-symlink fallback)
  --check     verify every source skill is registered & in sync; exit 1 if not (CI/health gate)
  --force     overwrite registered copies even when they are newer than their source

Newer-copy guard: a registered copy that differs from its source is NOT overwritten when
its git last-commit date is newer than the source's, or when it carries uncommitted edits
the source does not. On 2026-09-13 --copy regressed cag-image-generation and
cag-infographic this way (the edits had landed in .claude/skills/ only). Sync the copy back
into skills/ first, or pass --force to discard it.
"""
import os, re, sys, hashlib, pathlib, subprocess

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

def _git(*args):
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""

def _commit_time(path):
    out = _git("log", "-1", "--format=%ct", "--", str(path.relative_to(ROOT)))
    return int(out) if out else 0

def _dirty(path):
    return bool(_git("status", "--porcelain", "--", str(path.relative_to(ROOT))))

def copy_is_newer(src, tgt):
    """True when the registered copy holds edits its source lacks (by git dates / dirty state)."""
    if tgt.is_symlink() or not tgt.exists() or sha(tgt) == sha(src):
        return False
    if _dirty(tgt) and not _dirty(src):
        return True
    if _dirty(src):
        return False
    return _commit_time(tgt) > _commit_time(src)

def check():
    bad = []
    for name, src in sources():
        if not has_frontmatter(src):
            bad.append(f"  MISSING FRONTMATTER: skills/{src.relative_to(SRC)}")
            continue
        tgt = DST / name / "SKILL.md"
        if not tgt.exists():
            bad.append(f"  NOT REGISTERED: {name}")
        elif copy_is_newer(src, tgt):
            bad.append(f"  COPY NEWER THAN SOURCE: {name} — sync .claude/skills/{name}/SKILL.md back into skills/")
        elif not tgt.is_symlink() and sha(tgt) != sha(src):
            bad.append(f"  OUT OF SYNC (copy drift): {name} — rerun register_skills.py")
    if bad:
        print("Skill registration FAIL:")
        print("\n".join(bad))
        return 1
    print(f"Skill registration OK — {sum(1 for _ in sources())} skills registered.")
    return 0

def build(copy=False, force=False):
    n = 0
    refused = []
    for name, src in sources():
        if not has_frontmatter(src):
            print(f"  SKIP (no frontmatter): {name}")
            continue
        d = DST / name
        d.mkdir(parents=True, exist_ok=True)
        tgt = d / "SKILL.md"
        if not force and copy_is_newer(src, tgt):
            refused.append(name)
            continue
        if tgt.exists() or tgt.is_symlink():
            tgt.unlink()
        if copy:
            tgt.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        else:
            rel = os.path.relpath(src, d)
            tgt.symlink_to(rel)
        n += 1
    print(f"Registered {n} skills ({'copy' if copy else 'symlink'} mode) -> .claude/skills/")
    if refused:
        print(f"REFUSED {len(refused)} — registered copy is newer than its source (sync it back into skills/, or --force):")
        for name in refused:
            print(f"  {name}")
        return 1
    return 0

if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    sys.exit(build(copy="--copy" in sys.argv, force="--force" in sys.argv))

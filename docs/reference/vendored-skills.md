# Vendored third-party skills in `skills/`

`skills/openspec-*` are **not CAG-authored**. They are the upstream OpenSpec workflow
skills (MIT, `license:` and `compatibility:` are declared in each file's own front
matter), vendored into this repo at its initial commit on 2026-05-11 and never modified.

They sat in `.claude/skills/` with **no source in `skills/`** until 2026-08-03, which put
them in direct contradiction with the registration rule: `.claude/skills/` is *generated*
by `scripts/register_skills.py` and must never be hand-maintained. Four hand-committed
mirrors meant `--check` could not tell a vendored skill from a mirror whose source had
been deleted, so the invariant it exists to protect was already weakened.

**Adopted rather than deleted.** Deleting looked clean — `.claude/commands/opsx/*` covers
the same four operations and OpenSpec is otherwise unused here (no `openspec/` workspace,
no reference anywhere in the CAG system). But the comparison was checked rather than
assumed, and it is false for `explore`: the SKILL carries *Handling Different Entry
Points* and *What We Figured Out*, roughly 120 lines the command does not have. Dropping
would have quietly lost real guidance.

Consequences of adopting, stated so they are not a surprise:

- `register_skills.py --copy` now owns the mirrors; `--check` and `health-sweep.sh` will
  report drift on them like any other skill.
- **Do not edit them.** They are upstream files. If OpenSpec ships a new version, replace
  them wholesale and re-run `python3 scripts/register_skills.py --copy`.
- They require the `openspec` CLI, which is installed at `~/.npm-global/bin/openspec`.

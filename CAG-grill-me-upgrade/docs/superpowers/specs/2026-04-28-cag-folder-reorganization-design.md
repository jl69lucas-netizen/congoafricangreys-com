# CAG Folder Reorganization — Design Spec

**Date:** 2026-04-28  
**Status:** Implemented

## Context

`/Users/apple/Downloads/CAG` was reorganized from a flat 14-file project into an MFS-mirror structure using the Progressive Disclosure pattern. The goal: keep Claude's working context clean, pre-scaffold Phase 2 (agent/skills migration), and surface site content as directly editable markdown files.

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| ZIP handling | Selective extract | Extract CAG.zip (working pages) + performance ZIP (data); archive the rest |
| Folder pattern | MFS-Mirror | Proven structure; Phase 2 migration drops straight in |
| CLAUDE.md | Trimmed to ~55 lines | Domain prose moved to `docs/reference/domain-knowledge.md` |
| Phase 2 scaffolding | Pre-created now | `skills/`, `content/`, `docs/architecture/` ready for next session |
| Noise filtering | `.acloudignore` | Hides `archive/`, `sessions/`, `*.zip` from Claude's file view |

## Final Folder Tree

```
CAG/
├── .claude/
│   ├── agents/            (3 Phase 1 agents — unchanged)
│   └── settings.local.json (permissions allowlist)
├── .acloudignore
├── CLAUDE.md              (trimmed, pointers only)
├── skills/                (Phase 2: 30 CAG skills)
├── data/
│   ├── competitors.json
│   ├── keywords/
│   ├── rankings/
│   └── analytics/         (GSC performance HTML reports)
├── docs/
│   ├── architecture/      (Phase 2 system docs)
│   ├── reference/
│   │   ├── top-pages.md
│   │   └── domain-knowledge.md
│   └── research/          (competitor-intel outputs)
├── content/
│   ├── templates/         (Phase 2)
│   └── prompts/           (Phase 2)
├── site/
│   └── content/           (~80 .md page exports from CAG.zip)
├── sessions/
└── archive/
    ├── cag1.zip
    ├── cag2.zip
    └── simply-static-1-1775169284.zip
```

## Progressive Disclosure Rules

- Claude loads only `CLAUDE.md` on session start (~55 lines)
- Domain detail loads on demand from `docs/reference/domain-knowledge.md`
- Skills load on demand from `skills/` (Phase 2)
- `archive/` and `sessions/` are excluded via `.acloudignore`

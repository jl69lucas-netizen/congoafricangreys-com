#!/usr/bin/env bash
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REG="$ROOT/data/agent-registry.json"
PASS=0; FAIL=0
names=$(python3 -c "import json;print('\n'.join(json.load(open('$REG'))['agents']))")
for n in $names; do
  for d in "$ROOT/.claude/agents" "$ROOT/skills"; do
    f="$d/$n.md"
    if [ -f "$f" ]; then
      m=$(grep -m1 '^model:' "$f"); e=$(grep -m1 '^effort:' "$f")
      if [ -n "$m" ] && [ -n "$e" ]; then echo "PASS $n -> $m | $e"; PASS=$((PASS+1));
      else echo "FAIL $n -> missing model/effort"; FAIL=$((FAIL+1)); fi
      break
    fi
  done
done
echo ""; echo "Results: PASS=$PASS FAIL=$FAIL"
[ $FAIL -eq 0 ]

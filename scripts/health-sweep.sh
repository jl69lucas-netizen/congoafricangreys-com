#!/usr/bin/env bash
# =============================================================================
# CAG FULL SYSTEM HEALTH SWEEP
# One command that checks everything: git/deploy state, agent integrity,
# Astro build, live site, and built-output hygiene.
#
# Usage:   bash scripts/health-sweep.sh           # full sweep (runs build)
#          bash scripts/health-sweep.sh --no-build # skip the build step (faster)
#
# Exit code 0 = all critical checks passed, 1 = at least one critical failure.
# Designed for CongoAfricanGreys.com (Astro -> Cloudflare Pages, src/pages authoritative).
# =============================================================================
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

DOMAIN="https://congoafricangreys.com"
RUN_BUILD=1
[ "${1:-}" = "--no-build" ] && RUN_BUILD=0

FAIL=0
pass()  { printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
warn()  { printf "  \033[33mWARN\033[0m  %s\n" "$1"; }
fail()  { printf "  \033[31mFAIL\033[0m  %s\n" "$1"; FAIL=1; }
hdr()   { printf "\n\033[1m== %s ==\033[0m\n" "$1"; }

echo "CAG HEALTH SWEEP — $(date '+%Y-%m-%d %H:%M:%S')"

# -----------------------------------------------------------------------------
hdr "1. GIT / DEPLOY STATE"
# -----------------------------------------------------------------------------
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "  branch: $BRANCH"

# Secret leak: token embedded in remote URL is a credential exposure.
if git remote -v | grep -qE 'ghp_|github_pat_|x-access-token:[^@]+@'; then
  fail "GitHub token embedded in remote URL (.git/config) — rotate + use a credential helper"
else
  pass "No token embedded in remote URL"
fi

git fetch -q origin "$BRANCH" 2>/dev/null
AHEAD=$(git rev-list --count origin/"$BRANCH"..HEAD 2>/dev/null || echo "?")
BEHIND=$(git rev-list --count HEAD..origin/"$BRANCH" 2>/dev/null || echo "?")
if [ "$AHEAD" = "0" ]; then pass "Up to date with origin (0 unpushed commits)"
else warn "$AHEAD commit(s) committed but NOT pushed/deployed"; fi
[ "$BEHIND" != "0" ] && [ "$BEHIND" != "?" ] && warn "$BEHIND commit(s) on origin not pulled"

DIRTY=$(git status --short | wc -l | tr -d ' ')
if [ "$DIRTY" = "0" ]; then pass "Working tree clean"
else warn "$DIRTY uncommitted file(s) (not deployed) — run: git status --short"; fi

# -----------------------------------------------------------------------------
hdr "2. AGENT SYSTEM INTEGRITY"
# -----------------------------------------------------------------------------
ACOUNT=$(ls .claude/agents/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "  agents found: $ACOUNT"
amiss=0
for f in .claude/agents/*.md; do
  head -8 "$f" | grep -q "^name:"        || { fail "missing name: $(basename "$f")"; amiss=1; }
  head -8 "$f" | grep -q "^description:" || { fail "missing description: $(basename "$f")"; amiss=1; }
  head -8 "$f" | grep -q "^model:"       || { fail "missing model: $(basename "$f")"; amiss=1; }
done
[ $amiss -eq 0 ] && pass "All $ACOUNT agents have name + description + model frontmatter"

if [ -f scripts/verify_model_tiers.sh ]; then
  TIER=$(bash scripts/verify_model_tiers.sh 2>&1 | grep -E '^Results:' || echo "Results: (no output)")
  if echo "$TIER" | grep -q "FAIL=0"; then pass "Model tiers: $TIER"
  else fail "Model tier mismatch: $TIER"; fi
fi
echo "  skills found: $(ls skills/*.md 2>/dev/null | wc -l | tr -d ' ')"

if python3 scripts/register_skills.py --check >/tmp/cag-skillreg.log 2>&1; then
  pass "$(tail -1 /tmp/cag-skillreg.log)"
else
  fail "Skill registration drift — run: python3 scripts/register_skills.py --copy && git add .claude/skills/"
  sed 's/^/      /' /tmp/cag-skillreg.log
fi

# -----------------------------------------------------------------------------
hdr "3. ASTRO BUILD"
# -----------------------------------------------------------------------------
if [ $RUN_BUILD -eq 1 ]; then
  if npm run build > /tmp/cag-build.log 2>&1; then
    PAGES=$(grep -oE '[0-9]+ page\(s\) built' /tmp/cag-build.log | tail -1)
    pass "Build succeeded — ${PAGES:-completed}"
  else
    fail "Build FAILED — see /tmp/cag-build.log"
    tail -15 /tmp/cag-build.log | sed 's/^/      /'
  fi
else
  warn "Build skipped (--no-build)"
fi

# -----------------------------------------------------------------------------
hdr "4. LIVE SITE"
# -----------------------------------------------------------------------------
for path in "/" "/congo-african-grey-for-sale/" "/timneh-african-grey-for-sale/"; do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 "$DOMAIN$path")
  if [ "$CODE" = "200" ]; then pass "$path -> 200"
  else fail "$path -> $CODE"; fi
done
WWW=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 "https://www.congoafricangreys.com/")
if [ "$WWW" = "301" ] || [ "$WWW" = "308" ]; then pass "www -> $WWW (redirect)"
else warn "www -> $WWW (expected 301/308)"; fi

# -----------------------------------------------------------------------------
hdr "5. BUILT-OUTPUT HYGIENE (dist/)"
# -----------------------------------------------------------------------------
if [ -d dist ]; then
  python3 - <<'PY'
import re, glob, sys
DIST="dist"; broken=0; rel=0; nocanon=0; pages=0
for f in glob.glob(f"{DIST}/**/index.html", recursive=True):
    pages+=1
    c=open(f, encoding='utf-8', errors='ignore').read()
    broken+=len(re.findall(r'src="data:image/gif;base64,', c))
    cs=re.findall(r'<link[^>]*rel=["\']canonical["\'][^>]*href="([^"]*)"', c)
    if not cs: nocanon+=1
    rel+=sum(1 for x in cs if not x.startswith('http'))
def line(ok,msg):
    print(("  \033[32mPASS\033[0m  " if ok else "  \033[31mFAIL\033[0m  ")+msg)
line(True, f"{pages} built pages scanned")
line(broken==0, f"broken lazy-load GIF images: {broken}")
line(nocanon==0, f"pages missing canonical: {nocanon}")
line(rel==0, f"relative canonicals: {rel}")
sys.exit(1 if (broken or nocanon or rel) else 0)
PY
  [ $? -ne 0 ] && FAIL=1
else
  warn "dist/ not present — run a build first for output hygiene checks"
fi

# -----------------------------------------------------------------------------
hdr "RESULT"
# -----------------------------------------------------------------------------
if [ $FAIL -eq 0 ]; then
  printf "\033[32mALL CRITICAL CHECKS PASSED\033[0m\n"; exit 0
else
  printf "\033[31mONE OR MORE CRITICAL CHECKS FAILED — see above\033[0m\n"; exit 1
fi

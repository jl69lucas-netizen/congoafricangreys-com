#!/usr/bin/env bash
# Re-fetch the competitor candidates that the 2026-08-09 research sandbox could not
# reach, from this machine, which is on a different network.
#
# A 403 is NOT a dead site — Cloudflare challenges return 403 to curl while the site
# is perfectly live. Only 000 (no connection / no DNS) is evidence of dead.
#
# Usage: bash scripts/refetch_blocked_candidates.sh

set -uo pipefail

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# 7b — SERP-confirmed, sandbox fetch returned 000
SEVEN_B="rainforestaviaries.com sherrybirds.org paradisebirdsfarmaviary.com exoticparrotfarms.com parrotsfarm.com sunnyvaleaviary.com"

# 7d — named leads whose domain was never confirmed
SEVEN_D="ourpetstars.com"

printf '%-40s %-6s %s\n' "DOMAIN" "CODE" "VERDICT"
printf '%-40s %-6s %s\n' "----------------------------------------" "------" "-------"

for domain in $SEVEN_B $SEVEN_D; do
  code=$(curl -s -o /dev/null -m 15 -A "$UA" -w "%{http_code}" "https://${domain}/" 2>/dev/null)

  case "$code" in
    2*|3*) verdict="LIVE — promote to verified" ;;
    403|429) verdict="LIVE behind bot-challenge — promote, note the challenge" ;;
    000)   verdict="NO CONNECTION — genuinely unreachable, do not register" ;;
    *)     verdict="HTTP $code — inspect by hand" ;;
  esac

  printf '%-40s %-6s %s\n' "$domain" "$code" "$verdict"
done

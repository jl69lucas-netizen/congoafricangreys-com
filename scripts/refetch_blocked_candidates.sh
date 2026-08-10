#!/usr/bin/env bash
# Re-fetch competitor candidates that a research pass could not reach, and decide
# whether "unreachable" means the site is dead or means our own network lied.
#
# READ THIS BEFORE TRUSTING A "DEAD" VERDICT FROM ANY TOOL ON THIS MACHINE.
#
# Two independent things make a live site look dead from here, and neither is
# evidence about the site:
#
#   1. Bot challenges. Cloudflare and friends return 403/429 to curl for sites
#      that load perfectly in a browser. A 403 is not a dead site.
#
#   2. ISP DNS filtering. This machine's system resolver is a Virgin Media UK
#      line running "Web Safe" content filtering. It SELECTIVELY sinkholes
#      parrot and bird domains to 81.99.162.48 (reverse:
#      lang-sspiprxy.network.virginmedia.net), which accepts no connection, so
#      curl reports 000. Measured 2026-08-10: five domains the system resolver
#      collapsed onto that single IP resolve to five DIFFERENT, unrelated hosts
#      on 1.1.1.1 and 8.8.8.8, and four of the five return HTTP 200 with African
#      Grey content once resolved properly. The filter is selective, not blanket
#      — congoafricangreys.com and jcaviary.com resolve identically on both
#      resolvers — so you cannot predict which domains it hits.
#
# The v1 of this script used the system resolver and mapped 000 to "genuinely
# unreachable, do not register". That produced a false shared-IP finding and four
# false dead calls, both of which reached a published deliverable. Hence: this
# script resolves every domain against public DNS and fetches against that IP.
#
# Usage: bash scripts/refetch_blocked_candidates.sh

set -uo pipefail

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# The ISP filter's sinkhole address. Any domain the system resolver maps here is
# being filtered locally; the answer says nothing about the domain.
SINKHOLE="81.99.162.48"

# 7b — SERP-confirmed candidates a research sandbox filed as 000
SEVEN_B="rainforestaviaries.com sherrybirds.org paradisebirdsfarmaviary.com exoticparrotfarms.com parrotsfarm.com sunnyvaleaviary.com"

# 7d — named leads whose domain was never confirmed
SEVEN_D="ourpetstars.com"

printf '%-32s %-16s %-9s %-5s %-5s %s\n' "DOMAIN" "PUBLIC-DNS A" "SYS-DNS" "CODE" "GREY" "VERDICT"
printf '%-32s %-16s %-9s %-5s %-5s %s\n' "--------------------------------" "----------------" "---------" "-----" "-----" "-------"

for domain in $SEVEN_B $SEVEN_D; do
  # Two public resolvers, so one resolver's outage cannot masquerade as a dead domain.
  pub=$(dig @1.1.1.1 +short A "$domain" 2>/dev/null | grep -E '^[0-9.]+$' | head -1)
  [ -z "$pub" ] && pub=$(dig @8.8.8.8 +short A "$domain" 2>/dev/null | grep -E '^[0-9.]+$' | head -1)

  sys=$(dig +short A "$domain" 2>/dev/null | grep -E '^[0-9.]+$' | head -1)
  if [ "$sys" = "$SINKHOLE" ]; then
    sysflag="FILTERED"
  elif [ -z "$sys" ]; then
    sysflag="none"
  else
    sysflag="ok"
  fi

  if [ -z "$pub" ]; then
    code="nodns"
    grey="-"
    verdict="NO DNS on either public resolver — closed domain, do not register"
  else
    code=$(curl -s -o /dev/null -m 20 -A "$UA" --resolve "${domain}:443:${pub}" \
             -w "%{http_code}" "https://${domain}/" 2>/dev/null)
    grey=$(curl -s -m 20 -A "$UA" --resolve "${domain}:443:${pub}" "https://${domain}/" 2>/dev/null \
             | grep -oic "african grey" || true)
    grey=${grey:-0}

    case "$code" in
      2*|3*)   verdict="LIVE (${grey} grey mentions) — promote to verified" ;;
      403|429) verdict="LIVE behind bot-challenge — promote, note the challenge" ;;
      000)     verdict="Has DNS but no response — UNREACHABLE, CAUSE UNKNOWN. Not proof of dead." ;;
      *)       verdict="HTTP $code — inspect by hand" ;;
    esac
  fi

  printf '%-32s %-16s %-9s %-5s %-5s %s\n' "$domain" "${pub:-none}" "$sysflag" "$code" "$grey" "$verdict"
done

cat <<'EOF'

Reading this table
  SYS-DNS=FILTERED  the local ISP resolver sinkholed this domain. Ignore any
                    reachability result that used the system resolver.
  CODE=nodns        no A record from EITHER public resolver. This is the only
                    result that is evidence of a closed domain.
  CODE=000 with an  the host exists but did not answer. Record as unreachable
  A record          with cause unknown — never as "dead".
EOF

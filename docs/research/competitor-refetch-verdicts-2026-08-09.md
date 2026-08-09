# Re-fetch Verdicts — Network-Blocked Candidates

Date: 2026-08-09
Scope: Research only. `data/competitors.json` not modified by this pass.
Purpose: the 2026-08-09 discovery pass filed these as `000` from its sandbox. This is a
second verdict from the build machine, which is on a different network.

**Reading the codes:** 2xx/3xx = live. 403/429 = live behind a bot challenge (Cloudflare
returns 403 to curl on sites that are perfectly reachable in a browser) — this is NOT
evidence of a dead site. 000 = no connection or no DNS record; only this is evidence of dead.

## Verdicts

```
DOMAIN                                   CODE   VERDICT
---------------------------------------- ------ -------
rainforestaviaries.com                   000    NO CONNECTION — genuinely unreachable, do not register
sherrybirds.org                          000    NO CONNECTION — genuinely unreachable, do not register
paradisebirdsfarmaviary.com              000    NO CONNECTION — genuinely unreachable, do not register
exoticparrotfarms.com                    000    NO CONNECTION — genuinely unreachable, do not register
parrotsfarm.com                          000    NO CONNECTION — genuinely unreachable, do not register
sunnyvaleaviary.com                      200    LIVE — promote to verified
ourpetstars.com                          000    NO CONNECTION — genuinely unreachable, do not register
```

## African Grey inventory confirmation

| Domain | HTTP | "african grey"/"african gray" mentions | Reads as a real grey seller? |
|---|---|---|---|
| sunnyvaleaviary.com | 200 | 4 | Yes — homepage references African Greys multiple times |

All six other candidates (rainforestaviaries.com, sherrybirds.org,
paradisebirdsfarmaviary.com, exoticparrotfarms.com, parrotsfarm.com, ourpetstars.com)
returned `000` on this network too, so no homepage content could be fetched and no
mention count exists for them. `NOT FETCHED` — barrier: no connection / no DNS resolution
from this machine, same as the original sandbox.

## What changed versus the sandbox pass

Of the 7 candidates the 2026-08-09 sandbox pass filed as `000` (unreachable), only
**sunnyvaleaviary.com** flipped to confirmed-live from this machine — it returned HTTP 200
and its homepage carries 4 "African Grey" mentions, consistent with the hand-verification
noted at the start of this task.

The remaining 6 candidates (rainforestaviaries.com, sherrybirds.org,
paradisebirdsfarmaviary.com, exoticparrotfarms.com, parrotsfarm.com, ourpetstars.com) came
back `000` from this network as well. That means two independent networks have now failed
to reach them. This is stronger evidence of genuine unreachability than the original
single-sandbox result, but it is not proof of a dead domain — it could still reflect DNS
resolution issues specific to both test environments, geo-blocking, or a firewall rule that
blocks non-browser/curl traffic on both networks. No browser-based check was attempted for
this pass.

## Recommendation

**(Recommended) Promote sunnyvaleaviary.com to verified in a future registration pass; leave the other 6 candidates held back.** Sunnyvaleaviary.com is the only candidate with both a successful HTTP response (200) and confirmed on-page African Grey content (4 mentions) from this machine — it meets the bar for registration-worthy evidence. The other 6 remain unconfirmed on two separate networks now, with zero content evidence either way, so registering them would mean adding unverified candidates to `data/competitors.json` in violation of the "no fabricated claims" rule.

Trade-off: this recommendation is conservative — it's possible one or more of the 6 held-back domains are live sites that both test networks simply can't reach (e.g., due to geo-fencing or a WAF rule against datacenter/cloud IP ranges), in which case a real competitor stays undiscovered a bit longer. The alternative (registering them anyway based on the original SERP appearance) risks polluting the competitor registry with dead or unrelated domains, which is the worse failure mode for a data file other agents treat as ground truth.

This research pass does not itself register anything — `data/competitors.json` was not touched. Promotion is a separate, later action for whichever process owns that file.

## Open Flags

- rainforestaviaries.com, sherrybirds.org, paradisebirdsfarmaviary.com,
  exoticparrotfarms.com, parrotsfarm.com, ourpetstars.com: still unreachable from this
  machine (`000`). Barrier: no connection / DNS resolution failure via `curl` from this
  network, identical symptom to the original sandbox. Not yet tried: a real browser
  (Playwright/Chrome) fetch, which could succeed where curl fails if these sites use bot
  protection that blocks non-browser clients outright rather than returning a 403.
- No content verification exists for any of the 6 still-unreachable domains — their status
  as African Grey sellers is `NOT FETCHED` in both directions (SERP-confirmed name only,
  no page content seen by any tool run so far).

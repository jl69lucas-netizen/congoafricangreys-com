# Re-fetch Verdicts — Network-Blocked Candidates

> ## ⚠ RETRACTED IN PART — 2026-08-10. Read this before any line below.
>
> **Two conclusions in this document are false.** Both were produced by the same cause: every
> reachability figure below was taken through this machine's *system* DNS resolver, which is a
> Virgin Media UK line running "Web Safe" content filtering. That filter **selectively** sinkholes
> parrot and bird domains to `81.99.162.48` (reverse: `lang-sspiprxy.network.virginmedia.net`),
> which accepts no connection — so curl reports `000` for a perfectly healthy site.
>
> **Retraction 1 — the shared-IP finding is withdrawn.** Five domains do *not* share one London
> residential IP. Against `1.1.1.1` and `8.8.8.8` they resolve to five different, unrelated hosts,
> and repeat lookups return different addresses per domain. There is no evidence here of one
> operator, and the "US farm served from UK residential broadband" signal falls with it. The filter
> is selective, not blanket — `congoafricangreys.com` and `jcaviary.com` resolve identically on
> both resolvers — so a domain appearing on that IP says nothing whatever about the domain.
>
> **Retraction 2 — four "genuinely unreachable, do not register" verdicts are wrong.**
> `sherrybirds.org`, `paradisebirdsfarmaviary.com`, `exoticparrotfarms.com` and `parrotsfarm.com`
> are **live, HTTP 200, with African Grey content on the page** when resolved via public DNS.
>
> **What survives.** `rainforestaviaries.com` has a real A record on public DNS and still does not
> answer — unreachable, cause unknown, which is *not* the same as dead. `ourpetstars.com` has no A
> record on either public resolver: that one is genuinely closed. `sunnyvaleaviary.com` was never
> filtered and its LIVE verdict stands.
>
> **The corrected table is at the end of this file** under "Corrected Verdicts (2026-08-10)".
> `scripts/refetch_blocked_candidates.sh` has been rewritten to resolve through public DNS and can
> no longer produce this class of error. The registry note on `exoticGlobalParrotsFarm` carries its
> own retraction. The original text below is left intact deliberately, so the error and its
> correction stay auditable together.

Date: 2026-08-09
Scope: Research only. `data/competitors.json` not modified by this pass.
Purpose: the 2026-08-09 discovery pass filed these as `000` from its sandbox. This is a
second verdict from the build machine, which is on a different network.

**Reading the codes:** 2xx/3xx = live. 403/429 = live behind a bot challenge (Cloudflare
returns 403 to curl on sites that are perfectly reachable in a browser) — this is NOT
evidence of a dead site. 000 = no connection or no DNS record.

**`000` is two different findings and they must not be merged.** A domain with no DNS A
record is dead or never existed. A domain that resolves but refuses the connection is a
live registration whose server is down, firewalled, or filtering us. The first verdict
table below does not make that distinction; the DNS section that follows does, and it is
the one that changed the conclusion of this pass.

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

## 🚩 DNS resolution — four "egg competitors" and one registered breeder share one IP

The HTTP re-fetch alone could not separate "dead domain" from "live domain, unreachable
server". A DNS A-record lookup can, and doing it surfaced the most consequential finding of
this pass. Measured on 2026-08-09:

| Domain | A record | Reads as |
|---|---|---|
| **exoticglobalparrotsfarm.com** | **81.99.162.48** | **already registered — `exoticGlobalParrotsFarm`, tier 1 direct_breeder** |
| **sherrybirds.org** | **81.99.162.48** | 7b candidate (Timneh listing) |
| **paradisebirdsfarmaviary.com** | **81.99.162.48** | 7b candidate (Congo grey eggs $100) |
| **exoticparrotfarms.com** | **81.99.162.48** | 7b candidate (fertile grey eggs) |
| **parrotsfarm.com** | **81.99.162.48** | 7b candidate (Congo grey eggs $60) |
| rainforestaviaries.com | 74.208.236.200 | unrelated host; resolves, connection filtered |
| sunnyvaleaviary.com | 109.106.251.28 | unrelated host; **live, 200** |
| ourpetstars.com | *(no A record)* | **no DNS at all — dead or never existed** |

`81.99.162.48` reverse-resolves to `lang-sspiprxy.network.virginmedia.net` — a **Virgin Media
residential broadband line in London, GB**. The page-5 sweep independently recorded the same
IP for `exoticGlobalParrotsFarm` and flagged it under the dubious-claims rule.

**What this means, stated plainly:** these are not four independent egg competitors. They are
one operator running a network of storefronts from a single London home broadband connection,
and one member of that network is currently sitting in our registry as a **tier 1
direct_breeder**. Page 5 had already flagged that member for three separate scam signals —
three different African Greys all listed at the identical age "1 year 3 months old",
add-to-cart checkout with "worldwide delivery" of a CITES Appendix I species, and a US "farm"
presentation served from UK residential broadband.

**Consequences for how these are used:**

1. **Never cite any of the five as a price benchmark.** Four of them price grey eggs
   ($60–$100) and the plan flagged our egg cluster as the least-documented competitive
   picture. It is not an under-documented market — it is substantially one operator, and
   averaging his prices would produce a fabricated "market rate".
2. **`exoticGlobalParrotsFarm`'s tier-1 classification is now doubtful.** It is registered as
   a direct breeder. The evidence says domain network, not breeder. Re-tiering it is a
   breeder decision, not something this research pass should apply.
3. **All five are strong, documented material for `/how-to-avoid-african-grey-parrot-scams/`** —
   a verifiable, reproducible shared-IP finding is exactly the kind of evidence that page can
   use, and it is far stronger than a generic "watch out for cheap birds" warning.

Method note: the shared-IP finding is reproducible with `dig +short A <domain>` and
`dig +short -x 81.99.162.48`. It does not depend on reaching any of the sites.

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

### Recommendation revised after the DNS lookup

The recommendation above was written before the A-record check. The DNS evidence does not
change *what to register* — it changes *why*, and it adds a stronger reason to hold four of
the six back:

- **`ourpetstars.com` is settled, not pending.** It has no DNS A record at all. It is not a
  network-blocked competitor awaiting a better fetch; there is nothing there. Close it.
- **`sherrybirds.org`, `paradisebirdsfarmaviary.com`, `exoticparrotfarms.com` and
  `parrotsfarm.com` should stay held back permanently as *competitors*, and be re-filed as
  *scam-page evidence*.** They share one residential IP with each other and with a registry
  entry already flagged for dubious claims. Registering them as four competitors would
  overstate the egg market's size fourfold.
- **`rainforestaviaries.com` remains genuinely undetermined.** It resolves to an unrelated
  host and simply would not answer. It is the only one of the six that still deserves a
  browser-based retry.
- **`sunnyvaleaviary.com` is unaffected** by any of this — different host, live, grey content
  confirmed. It remains the one promotion candidate.

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
- **The shared-IP cluster is established by DNS, but its *ownership* is not.** Five domains
  resolving to one residential IP is strong evidence of common hosting; it is not proof of a
  single legal owner. WHOIS was not queried this pass. Do not name an operator, and do not
  publish an accusation of fraud — describe the measurable facts (shared IP, residential
  line, geography vs claimed location) and let them speak.
- **`exoticGlobalParrotsFarm` is registered tier 1 `direct_breeder` and the evidence now
  contradicts that tier.** Left unchanged here deliberately — re-tiering a registry entry is
  a breeder decision, not a research-pass side effect. Flagged as an open question.

---

## Corrected Verdicts (2026-08-10)

Produced by the rewritten `scripts/refetch_blocked_candidates.sh`, which resolves each domain
against `1.1.1.1` (falling back to `8.8.8.8`) and fetches against that address with `curl --resolve`,
so the local ISP filter cannot influence the result. `GREY` counts occurrences of "african grey" in
the returned HTML.

```
DOMAIN                           PUBLIC-DNS A     SYS-DNS   CODE  GREY  VERDICT
-------------------------------- ---------------- --------- ----- ----- -------
rainforestaviaries.com           74.208.236.200   ok        000   0     Has DNS but no response — UNREACHABLE, CAUSE UNKNOWN. Not proof of dead.
sherrybirds.org                  88.222.222.157   FILTERED  200   3     LIVE (3 grey mentions) — promote to verified
paradisebirdsfarmaviary.com      2.57.91.21       FILTERED  200   3     LIVE (3 grey mentions) — promote to verified
exoticparrotfarms.com            88.222.222.249   FILTERED  200   8     LIVE (8 grey mentions) — promote to verified
parrotsfarm.com                  213.130.145.185  FILTERED  200   2     LIVE (2 grey mentions) — promote to verified
sunnyvaleaviary.com              109.106.251.28   ok        200   4     LIVE (4 grey mentions) — promote to verified
ourpetstars.com                  none             none      nodns -     NO DNS on either public resolver — closed domain, do not register
```

`SYS-DNS=FILTERED` marks the four domains the local resolver sinkholed. Note that the public A
records differ from the run recorded earlier in this session (`sherrybirds.org` returned
`84.32.84.90` then, `88.222.222.157` now) — per-domain rotation across separate hosting, which is
further evidence against the single-box theory.

### What this changes

1. **Four candidates are eligible for registration** that were filed as dead. They are *candidates*,
   not registrations: new competitors require breeder approval, and none has been added.
2. **The egg-cluster conclusion reverts.** "Substantially one operator" is withdrawn; the egg
   competitive picture is once again under-documented, which is where the 2026-08-09 plan started.
3. **No scam-page material.** The shared-IP story must not appear on
   `/how-to-avoid-african-grey-parrot-scams/`. The Marietta redirect hijack is unaffected — it was
   reproduced by HTTP redirect chain, not by DNS, and remains fully supported.

### Method note worth carrying forward

A `000` from this machine is not evidence about a site. Resolve through a public resolver before
recording any domain as dead, and only "no A record from two public resolvers" earns that word.
This is now enforced in the script rather than written down as a rule, because the previous version
of this document already carried a correct warning about `000` in prose and the wrong verdict was
recorded anyway.

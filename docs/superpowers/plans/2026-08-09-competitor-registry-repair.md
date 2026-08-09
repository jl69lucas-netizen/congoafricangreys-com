# Competitor Registry Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Repair the eight verified defects in `data/competitors.json`, promote the research candidates that this machine can actually reach, and re-run the four competitor-intel passes that were lost with the previous session.

**Architecture:** `data/competitors.json` is the source of truth that nine agents read. Today it is provably wrong in seven ways, so the repair is guarded by a pytest invariant file written *first* (TDD) — the tests fail against the current file, a single idempotent patch script makes them pass, and the tests then stay as a permanent regression gate. Registry *corrections* (the 14 identity resolutions, the dead domain, the compromised entry) are applied directly because they fix existing rows; registry *additions* (the 15 new competitors) pass through an explicit breeder-approval gate, per the standing rule that new competitors come back as proposals.

**Tech Stack:** Python 3 (stdlib only — `json`, `pathlib`, `argparse`), pytest 8.4.2, `curl`, git. No new dependencies: `jsonschema` is **not** installed and this plan deliberately does not add it.

---

## Scope Check

This plan covers one subsystem — the competitor registry and its research inputs. It touches **no page under `src/pages/`**, so:

- **Do not run** `npx astro build`.
- **Do not run** `python3 scripts/generate_sitemaps.py`.
- **Do not run** `python3 scripts/indexnow_submit.py`.

Those three are mandatory after *page* builds. Nothing here changes rendered output, so running them would submit unchanged URLs and muddy the IndexNow log.

---

## Context: what was verified before this plan was written

Every claim below was independently reproduced on this machine on 2026-08-09. Do not re-litigate these; they are settled.

| Claim | Verification result |
|---|---|
| `data/competitors.json` untouched by the research passes | Confirmed — mtime 2026-08-03, 44 entries |
| The 28 proposals do not overlap the 44 registry entries | Confirmed programmatically, zero overlap |
| `_meta.total_competitors` reads `30`, file holds `44` | Confirmed; `_meta.description` also says "30-competitor registry" |
| 14 entries use `domain` not `url`, and have no `name` | Confirmed — exactly the 14 ids listed below |
| `handrearedparrots.com` is dead | Confirmed — `000`, no DNS A record |
| `handraredparrots.com` is live | Confirmed — `200` |
| Marietta Bird Shop African Grey URL is hijacked | **Reproduced** — `/product/african-grey-parrot` → 301 → 301 → `jellyrollskidswear.com` → 14 hops → `mysteryinktattoos.com`, title `THOR138 # Game Online Resmi…`, 0 occurrences of "african grey". Control `/product/cockatiel` clean, 0 redirects, 200. |
| `sunnyvaleaviary.com` filed as unreachable `000` | **Contradicted** — returns `200` from this machine. The sandbox-network theory holds; Task 5 exists because of this. |

Source documents (research only, already on disk, untracked):
- [competitor-discovery-crossplatform-2026-08-09.md](../../research/competitor-discovery-crossplatform-2026-08-09.md)
- [competitor-sweep-page5-2026-08-09.md](../../research/competitor-sweep-page5-2026-08-09.md)

---

## File Structure

| File | Status | Responsibility |
|---|---|---|
| `tests/test_competitors_registry.py` | **Create** | The permanent invariant gate for the registry: schema completeness, id uniqueness, meta/count agreement, tier-label consistency, and the two verified fact-locks (live `handRearedParrots` domain, Marietta flagged compromised). Plain pytest, stdlib only, matching the style of the seven existing `tests/test_*.py`. |
| `scripts/patch_competitor_registry.py` | **Create** | The single idempotent writer. Holds the 14-row resolution table as data, normalises `domain`→`url`, backfills the full 13-key schema, applies the six point-fixes, and repairs `_meta`. Running it twice must produce a byte-identical file. |
| `scripts/refetch_blocked_candidates.sh` | **Create** | Re-fetches the 7b/7c/7d candidate domains from this machine with a real browser UA and records HTTP status, so the sandbox-blocked entries get a verdict from a network that is not blocked. |
| `data/competitors.json` | **Modify** | The registry itself. Written only by the patch script, never by hand. |
| `docs/research/competitor-refetch-verdicts-2026-08-09.md` | **Create** | Output of the re-fetch: which candidates are live, which are genuinely dead. |
| `docs/research/competitor-sweep-page{1,2,3,4}-2026-08-09.md` | **Create** (by subagents) | The four lost passes, re-run. |
| `docs/artifacts/cags-competitor-registry-2026-08-09.html` | **Create** | The consolidated deliverable, per CLAUDE.md rule 13 — markdown authored once inside the page and rendered, section copy buttons, downloads as `.md`. |

**Why one script and not a migration per defect:** all seven defects live in the same file and several touch the same 14 rows. Seven scripts would each need their own idempotency proof. One script with one idempotency test is less code and a stronger guarantee.

---

## The eight defects being repaired

Numbered here so tasks can refer to them without restating. Seven came from the research; the eighth
was found by executing this plan's own patch script during authoring:

1. `_meta.total_competitors` is `30`; the file holds `44`. `_meta.description` repeats the wrong number.
2. 14 entries carry `domain` instead of `url`.
3. Those same 14 entries have no `name`.
4. Those same 14 entries lack the other 8 schema keys the 30 complete entries have.
5. `handRearedParrots.domain` points at a domain with no DNS record.
6. `denimixaniPetsParadise` display name splits the brand wrongly — it is **Denimix Anipets Paradise**.
7. `mariettaBirdShop` is registered as a live African Grey competitor while its only African Grey URL 301s into a casino redirect chain.
8. `parrotAlert` is `tier: 2` but carries `tier_label: "non_commercial"`, a label absent from `_meta.tiers`. **Found by running the patch script, not by reading the research** — see the REVIEW note in Task 2 Step 2. Normalised so the file is self-consistent; the underlying taxonomy question goes to the breeder.

---

## Task 1: Registry invariant tests (they must fail first)

**Files:**
- Create: `tests/test_competitors_registry.py`

- [ ] **Step 1: Write the failing test file**

```python
"""Invariants for data/competitors.json — the competitor registry.

The registry is the source of truth that nine agents read. These tests are the
gate that keeps it structurally honest. Written 2026-08-09 against a file with
seven known defects; see docs/superpowers/plans/2026-08-09-competitor-registry-repair.md
"""

import json
import pathlib

REGISTRY = pathlib.Path(__file__).resolve().parents[1] / "data" / "competitors.json"

# The 13 keys every one of the 30 complete entries carries.
# access_status (18/30) and threat_level (2/30) are deliberately optional.
REQUIRED_KEYS = {
    "id",
    "name",
    "url",
    "tier",
    "tier_label",
    "states_active",
    "primary_keywords",
    "keywords_found",
    "last_analyzed",
    "last_monitored",
    "priority",
    "notes",
    "social",
}


def load():
    return json.loads(REGISTRY.read_text())


def test_meta_total_matches_actual_count():
    data = load()
    assert data["_meta"]["total_competitors"] == len(data["competitors"])


def test_meta_description_does_not_hardcode_a_stale_count():
    data = load()
    actual = len(data["competitors"])
    description = data["_meta"]["description"]
    for stale in ("30-competitor", "30 competitor"):
        assert stale not in description, f"description still says {stale!r}, file has {actual}"


def test_no_entry_uses_the_legacy_domain_key():
    data = load()
    legacy = sorted(c["id"] for c in data["competitors"] if "domain" in c)
    assert legacy == [], f"entries still on the legacy 'domain' key: {legacy}"


def test_every_entry_has_the_full_schema():
    data = load()
    incomplete = {
        c.get("id", "<no id>"): sorted(REQUIRED_KEYS - set(c))
        for c in data["competitors"]
        if REQUIRED_KEYS - set(c)
    }
    assert incomplete == {}, f"entries missing required keys: {incomplete}"


def test_ids_are_unique():
    data = load()
    ids = [c["id"] for c in data["competitors"]]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    assert duplicates == [], f"duplicate ids: {duplicates}"


def test_every_url_is_absolute():
    data = load()
    bad = sorted(
        c["id"]
        for c in data["competitors"]
        if not str(c.get("url", "")).startswith(("http://", "https://"))
    )
    assert bad == [], f"entries without an absolute url: {bad}"


def test_tier_label_agrees_with_tier():
    data = load()
    tier_map = data["_meta"]["tiers"]
    mismatched = sorted(
        c["id"]
        for c in data["competitors"]
        if c.get("tier_label") != tier_map.get(str(c.get("tier")))
    )
    assert mismatched == [], f"tier_label disagrees with tier: {mismatched}"


def test_hand_reared_parrots_points_at_the_live_domain():
    """handrearedparrots.com has no DNS record; handraredparrots.com resolves and returns 200.

    Verified 2026-08-09. Without this lock every future sweep re-logs the entry as dead.
    """
    data = load()
    entry = next(c for c in data["competitors"] if c["id"] == "handRearedParrots")
    # .get, not [] — before the patch this entry has no `url` key at all, and a gate
    # that raises KeyError instead of asserting tells you nothing about the registry.
    assert "handraredparrots.com" in entry.get("url", "")


def test_marietta_bird_shop_is_flagged_compromised():
    """Its only African Grey URL 301s off-domain into a 13-hop chain ending at an
    Indonesian casino site. Reproduced 3/3 runs plus independently on 2026-08-09.
    """
    data = load()
    entry = next(c for c in data["competitors"] if c["id"] == "mariettaBirdShop")
    assert entry.get("access_status") == "compromised_redirect"
    assert entry.get("priority") == "low"
```

- [ ] **Step 2: Run the tests and confirm they fail for the right reasons**

```bash
python3 -m pytest tests/test_competitors_registry.py -v
```

Expected: **1 passed, 8 failed.** This was measured against the current registry on 2026-08-09, not
estimated — if you see a different split, the test file does not match what is written above.

| Test | Expected | Why |
|---|---|---|
| `test_ids_are_unique` | **PASS** | The only invariant the registry already satisfies |
| `test_meta_total_matches_actual_count` | FAIL | `30 != 44` |
| `test_meta_description_does_not_hardcode_a_stale_count` | FAIL | description says "30-competitor registry" |
| `test_no_entry_uses_the_legacy_domain_key` | FAIL | 14 ids listed |
| `test_every_entry_has_the_full_schema` | FAIL | same 14 ids, each missing 9 keys |
| `test_every_url_is_absolute` | FAIL | the 14 have no `url` key at all |
| `test_tier_label_agrees_with_tier` | FAIL | the 14 have no `tier_label` |
| `test_hand_reared_parrots_points_at_the_live_domain` | FAIL | entry has no `url`; asserts on `""` |
| `test_marietta_bird_shop_is_flagged_compromised` | FAIL | `access_status` is currently `"accessible"` |

Note that `mariettaBirdShop.priority` is **already** `"low"` — only `access_status` needs to change, so
that assertion passing on its own proves nothing. Both assertions in that test must pass together.

Every failure must be an assertion message, not a `KeyError` or `StopIteration`. A gate that errors
instead of asserting is the "gate examined zero pages" failure mode this project has already been bitten
by — that is why the last two tests use `.get()` rather than `[]`.

- [ ] **Step 3: Commit the failing gate**

```bash
git add tests/test_competitors_registry.py docs/superpowers/plans/2026-08-09-competitor-registry-repair.md
git commit -m "test(registry): invariant gate for competitors.json — 7 known defects fail red"
```

---

## Task 2: The patch script — identity resolution and schema normalisation

**Files:**
- Create: `scripts/patch_competitor_registry.py`
- Modify: `data/competitors.json` (by running the script, not by hand)

- [ ] **Step 1: Write the patch script**

The 14-row resolution table below is transcribed from the Part B resolution table of
`docs/research/competitor-sweep-page5-2026-08-09.md`, all rated High confidence except
`grayBreedersFoundation` (Medium-High). `states_active` values are only filled where the research
recorded a real street address or city.

```python
#!/usr/bin/env python3
"""Repair data/competitors.json — the seven defects recorded in
docs/superpowers/plans/2026-08-09-competitor-registry-repair.md

Idempotent by construction: it reads the file, applies a fixed set of
transformations that are all "set to this value", and writes it back. Running it
twice produces a byte-identical file.

Usage:
    python3 scripts/patch_competitor_registry.py --check   # report, write nothing
    python3 scripts/patch_competitor_registry.py           # apply
"""

import argparse
import json
import pathlib
import sys

REGISTRY = pathlib.Path(__file__).resolve().parents[1] / "data" / "competitors.json"

# --- Defect 2/3/4: the 14 entries that carry `domain` and no `name` ---------
# id -> (resolved name, canonical url, states_active)
RESOLUTIONS = {
    "exoticGlobalParrotsFarm": ("Exotic Global Parrots Farm", "https://exoticglobalparrotsfarm.com", []),
    "royalBirdCompany": ("Royal Bird Company", "https://www.royalbirdcompany.com", ["NC"]),
    "denimixaniPetsParadise": ("Denimix Anipets Paradise", "https://denimixanipetsparadise.com", []),
    "buyAfricanGreyParrots": ("Buy African Grey Parrots", "https://buyafricangreyparrots.com", ["FL"]),
    "hookbillsForSale": ("Hookbills For Sale", "https://www.hookbillsforsale.com", []),
    "grayBreedersFoundation": ("Gray Breeders Foundation", "https://graybreedersfoundation.yolasite.com", []),
    "theAvianExchange": ("The Avian Exchange", "https://theavianexchange.com", []),
    "jcAviary": ("JC Aviary", "https://www.jcaviary.com", ["TX"]),
    "anasParrots": ("Ana's Parrots & Supplies", "http://anasparrots.com", ["PA"]),
    "parrotStars": ("Parrot Stars", "https://parrotstars.com", ["IL"]),
    "birdsByJoe": ("Birds By Joe", "https://www.birdsbyjoe.com", ["NJ"]),
    "midnightParrotPlace": ("Midnight Parrot Place", "https://midnightparrotplace.com", ["IL"]),
    # Defect 5: registry had handrearedparrots.com, which has no DNS record.
    "handRearedParrots": ("Hand Reared Parrots For Sale", "https://handraredparrots.com", []),
    "featherHeadz": ("Feather Headz Aviary", "https://www.featherheadz.com", ["FL"]),
}

EMPTY_SOCIAL = {
    "instagram": None,
    "facebook": None,
    "youtube": None,
    "tiktok": None,
    "pinterest": None,
    "twitter_x": None,
    "followers": None,
    "cadence": None,
    "last_social_audit": None,
}

MARIETTA_NOTE = (
    "COMPROMISED 2026-08-09: /product/african-grey-parrot — the site's only African Grey URL — "
    "serves a server-side 301 chain (13 hops) off-domain via jellyrollskidswear.com to "
    "mysteryinktattoos.com, an Indonesian online-casino page (title 'THOR138'), containing zero "
    "occurrences of 'african grey'. Reproduced 3/3 runs by curl and independently by Firecrawl, and "
    "again on 2026-08-09 from the build machine. 14 of 15 other URLs on the site are clean, so the "
    "blast radius is exactly the African Grey page. Googlebot receives the same 301. Never link to "
    "this site from any CAG page and never cite it as a competitor price benchmark."
)

SWEPT_2026_08_09 = ("chewy", "petFinder", "mariettaBirdShop")


def patch(data):
    """Return (data, list_of_changes). Pure apart from mutating the dict it is given."""
    changes = []
    tier_map = data["_meta"]["tiers"]

    for entry in data["competitors"]:
        cid = entry["id"]

        # Defect 2: normalise the legacy `domain` key to `url`.
        if "domain" in entry:
            entry["url"] = entry.pop("domain")
            changes.append(f"{cid}: domain -> url")

        # Defect 3 + 5 + 6: name and canonical url from the resolution table.
        if cid in RESOLUTIONS:
            name, url, states = RESOLUTIONS[cid]
            if entry.get("name") != name:
                entry["name"] = name
                changes.append(f"{cid}: name = {name!r}")
            if entry.get("url") != url:
                old = entry.get("url")
                entry["url"] = url
                changes.append(f"{cid}: url {old!r} -> {url!r}")
            if states and entry.get("states_active") != states:
                entry["states_active"] = states
                changes.append(f"{cid}: states_active = {states}")

        # Defect 4: backfill the full schema.
        entry.setdefault("states_active", [])
        entry.setdefault("primary_keywords", list(entry.get("keywords", [])))
        entry.setdefault("keywords_found", list(entry.get("keywords", [])))
        entry.setdefault("last_analyzed", entry.get("discovered"))
        entry.setdefault("last_monitored", None)
        entry.setdefault("priority", "medium")
        entry.setdefault("notes", "")
        entry.setdefault("social", dict(EMPTY_SOCIAL))

        # tier_label must always agree with tier.
        expected_label = tier_map[str(entry["tier"])]
        if entry.get("tier_label") != expected_label:
            previous = entry.get("tier_label")
            entry["tier_label"] = expected_label
            if previous:
                # Overwriting a label a human wrote on purpose — say so loudly rather
                # than burying it in 60 other lines. See the parrotAlert open question.
                changes.append(
                    f"{cid}: tier_label {previous!r} -> {expected_label!r}"
                    "   <-- REVIEW: previous label is not in _meta.tiers"
                )
            else:
                changes.append(f"{cid}: tier_label = {expected_label}")

        # Defect 7: the compromised entry.
        if cid == "mariettaBirdShop":
            if entry.get("access_status") != "compromised_redirect":
                entry["access_status"] = "compromised_redirect"
                changes.append(f"{cid}: access_status = compromised_redirect")
            if entry.get("priority") != "low":
                entry["priority"] = "low"
                changes.append(f"{cid}: priority = low")
            if entry.get("threat_level") != "none":
                entry["threat_level"] = "none"
                changes.append(f"{cid}: threat_level = none")
            if entry.get("notes") != MARIETTA_NOTE:
                entry["notes"] = MARIETTA_NOTE
                changes.append(f"{cid}: notes = compromised-redirect record")

        if cid in SWEPT_2026_08_09 and entry.get("last_analyzed") != "2026-08-09":
            entry["last_analyzed"] = "2026-08-09"
            changes.append(f"{cid}: last_analyzed = 2026-08-09")

    # Defect 1: _meta must describe the file it is attached to.
    actual = len(data["competitors"])
    if data["_meta"].get("total_competitors") != actual:
        old = data["_meta"].get("total_competitors")
        data["_meta"]["total_competitors"] = actual
        changes.append(f"_meta.total_competitors {old} -> {actual}")

    wanted_description = (
        f"{actual}-competitor registry for congoafricangreys.com "
        "— source of truth for all competitor research"
    )
    if data["_meta"].get("description") != wanted_description:
        data["_meta"]["description"] = wanted_description
        changes.append("_meta.description resynced to actual count")

    return data, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report changes, write nothing")
    args = parser.parse_args()

    data = json.loads(REGISTRY.read_text())
    data, changes = patch(data)

    if not changes:
        print("No changes — registry already patched.")
        return 0

    print(f"{len(changes)} change(s):")
    for change in changes:
        print(f"  - {change}")

    if args.check:
        print("\n--check: nothing written.")
        return 1

    REGISTRY.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {REGISTRY}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Dry-run it and read the change list before writing anything**

```bash
python3 scripts/patch_competitor_registry.py --check
```

Expected: **61 changes** — measured, not estimated. They break down as 14 × `domain -> url`,
14 × `name = …`, 14 × `tier_label = …` (the resolved entries had none), 7 × `states_active`, the
`handRearedParrots` url correction, the `denimixaniPetsParadise` rename, three `mariettaBirdShop`
lines, three `last_analyzed` lines, the two `_meta` lines, and **one `REVIEW` line** described below.
Exit code 1 (nothing written).

**Read this list.** Two things in it are deliberate and must not be mistaken for bugs:

- **`mariettaBirdShop` appears on four lines, and `priority` is not one of them.** Its `priority` is
  *already* `"low"`, so the compromised block changes only `access_status`, `threat_level` and `notes`;
  the fourth mention is its `last_analyzed` bump. The test asserts `access_status` and `priority`
  together precisely because `priority` passing on its own would prove nothing.
- **`parrotAlert: tier_label 'non_commercial' -> 'classified_aggregator'   <-- REVIEW`.** This is an
  eighth defect, found by running this script rather than by reading the research: `parrotAlert` is
  `tier: 2` but carries the label `non_commercial`, which does not appear in `_meta.tiers` at all.
  Parrot Alert is a lost-and-stolen-bird registry, so `non_commercial` was very likely written on
  purpose and the *tier* is what is wrong. The script normalises it so the file stops being internally
  inconsistent, but **this is a taxonomy decision, not a mechanical fix** — it is logged as an open
  question in Task 7 and must be put to the breeder rather than settled here.

If the list contains a change to any entry outside the 14 resolutions, the three swept ids, and that
one `parrotAlert` REVIEW line, stop and investigate before applying.

- [ ] **Step 3: Apply the patch**

```bash
python3 scripts/patch_competitor_registry.py
```

Expected: the same change list, then `Wrote …/data/competitors.json`. Exit code 0.

- [ ] **Step 4: Run the gate — it must now be green**

```bash
python3 -m pytest tests/test_competitors_registry.py -v
```

Expected: **9 passed.**

- [ ] **Step 5: Prove idempotency — run the script again, then diff**

```bash
python3 scripts/patch_competitor_registry.py && git diff --stat data/competitors.json
```

Expected: `No changes — registry already patched.` and the `git diff --stat` shows the same single
modified file it showed before this step — a second run must not add a single further line. If the
second run reports changes, the script is not idempotent; fix it before committing.

- [ ] **Step 6: Confirm nothing was lost in the rewrite**

```bash
python3 -c "
import json
d=json.load(open('data/competitors.json'))
print('entries:', len(d['competitors']))
print('with url:', sum(1 for c in d['competitors'] if c.get('url')))
print('with name:', sum(1 for c in d['competitors'] if c.get('name')))
print('legacy domain key:', sum(1 for c in d['competitors'] if 'domain' in c))
"
```

Expected exactly:
```
entries: 44
with url: 44
with name: 44
legacy domain key: 0
```

- [ ] **Step 7: Commit**

```bash
git add scripts/patch_competitor_registry.py data/competitors.json
git commit -m "fix(registry): resolve 14 identities, normalise schema, flag Marietta compromised

- 14 entries: domain -> url, name backfilled from page-5 identity resolution
- handRearedParrots: handrearedparrots.com (no DNS) -> handraredparrots.com (200)
- denimixaniPetsParadise: display name -> Denimix Anipets Paradise
- mariettaBirdShop: access_status=compromised_redirect, priority=low, 13-hop
  casino redirect chain recorded in notes
- _meta.total_competitors 30 -> 44, description resynced

Guarded by tests/test_competitors_registry.py."
```

---

## Task 3: Add the Marietta hijack to the scam-prevention evidence pool

**Files:**
- Modify: `data/competitors.json` (via the script's note — already done in Task 2)
- Create: nothing

This task is a **decision checkpoint, not a code change.** The page-5 research recommends that three
resolved entries (Exotic Global Parrots Farm, Denimix Anipets Paradise, Gray Breeders Foundation) plus
the Marietta hijack are usable as documented examples on `/how-to-avoid-african-grey-parrot-scams/`.

- [ ] **Step 1: Record the recommendation, do not edit the page**

Editing `/how-to-avoid-african-grey-parrot-scams/` is a page build. It requires the interior-page
checklist, a heading-outline gate, a dup-content gate, a render-harness run, and an IndexNow
submission — none of which are in scope here. Surface it to the breeder as a follow-up and move on.

- [ ] **Step 2: Verify the note landed in the registry instead**

```bash
python3 -c "
import json
d=json.load(open('data/competitors.json'))
e=[c for c in d['competitors'] if c['id']=='mariettaBirdShop'][0]
print(e['access_status'], '|', e['priority'], '|', e.get('threat_level'))
print(e['notes'][:120])
"
```

Expected: `compromised_redirect | low | none` and a notes string beginning `COMPROMISED 2026-08-09:`.

No commit — Task 2 already committed this.

---

## Task 4: Re-fetch script for the network-blocked candidates

**Files:**
- Create: `scripts/refetch_blocked_candidates.sh`

The 7b/7c/7d candidates were filed as unreachable from the research sandbox. This machine reaches at
least one of them (`sunnyvaleaviary.com` → 200), so every blocked candidate deserves a second verdict
from here before it is discarded or registered.

- [ ] **Step 1: Write the re-fetch script**

```bash
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
```

- [ ] **Step 2: Make it executable and run it**

```bash
chmod +x scripts/refetch_blocked_candidates.sh && bash scripts/refetch_blocked_candidates.sh
```

Expected: a 7-row table. At minimum `sunnyvaleaviary.com` must report `200` / `LIVE — promote to
verified` — that result was confirmed by hand on 2026-08-09, so if this script reports `000` for it the
script is wrong, not the site.

- [ ] **Step 3: Record the verdicts**

Write `docs/research/competitor-refetch-verdicts-2026-08-09.md` containing the exact table the script
printed, under this header:

```markdown
# Re-fetch Verdicts — Network-Blocked Candidates

Date: 2026-08-09
Scope: Research only. `data/competitors.json` not modified by this pass.
Purpose: the 2026-08-09 discovery pass filed these as `000` from its sandbox. This is a
second verdict from the build machine, which is on a different network.

**Reading the codes:** 2xx/3xx = live. 403/429 = live behind a bot challenge (Cloudflare
returns 403 to curl on sites that are perfectly reachable in a browser) — this is NOT
evidence of a dead site. 000 = no connection or no DNS record; only this is evidence of dead.

<paste the script's table here verbatim>
```

- [ ] **Step 4: Commit**

```bash
git add scripts/refetch_blocked_candidates.sh docs/research/competitor-refetch-verdicts-2026-08-09.md
git commit -m "research(competitors): second-network verdicts for the 7 sandbox-blocked candidates"
```

---

## Task 5: Approval gate for the 15 new competitors

**Files:**
- Modify: none until approval is given

The standing rule is that new competitors come back as **proposals** for the breeder to approve before
they enter the registry. Tasks 1–4 corrected existing rows, which needs no approval. This task adds
rows, which does.

- [ ] **Step 1: Present the proposal and stop**

Present the 15 verified 7a candidates from
`docs/research/competitor-discovery-crossplatform-2026-08-09.md` §7a, plus any 7b candidate that
Task 4 promoted to LIVE, as a single approval list. For each: name, url, tier, and the one-line reason
it is a real competitor.

Flag these three explicitly in the presentation, because they are traps:

- **Todd Marcus Birds Exotic (thebirdstore.com)** — the research recommends `priority: high`; it is the
  only new name found on all five platforms and the only one Reddit names unprompted.
- **GreyWing Aviary (greywingaviary.com)** — lists greys at **$600 each**. Register as a SERP
  competitor, never as a price benchmark; $600 is a classic scam signal.
- **Welch Exotic Birds Farm** — WhatsApp-only ordering. Same treatment: track, never benchmark.

**Do not write to `data/competitors.json` in this step.** Wait for an explicit yes.

- [ ] **Step 2: On approval only — extend the patch script**

Add an `ADDITIONS` list to `scripts/patch_competitor_registry.py` holding the approved rows in the full
13-key schema, and an `--add-approved` flag that appends any id not already present. Keep it idempotent:
appending an id that already exists must be a no-op.

- [ ] **Step 3: On approval only — apply, gate, commit**

```bash
python3 scripts/patch_competitor_registry.py --add-approved --check
```

Read the list, then:

```bash
python3 scripts/patch_competitor_registry.py --add-approved && python3 -m pytest tests/test_competitors_registry.py -v
```

Expected: **9 passed**, with `test_meta_total_matches_actual_count` now asserting against the new total
(44 + however many were approved). The count test passing on the new number is the proof that `_meta`
stayed in sync.

```bash
git add scripts/patch_competitor_registry.py data/competitors.json
git commit -m "feat(registry): add breeder-approved competitors from the 2026-08-09 discovery pass"
```

---

## Task 6: Re-run the four lost passes

**Files:**
- Create: `docs/research/competitor-sweep-page1-2026-08-09.md` … `page4` (written by subagents)

Pages 1–4 never landed — `TaskList` is empty and no files were written. The 44 registry entries
partition cleanly, and page 5 already covered 17 of them (Chewy, Petfinder, Marietta, plus the 14
identity-resolution entries). These are the remaining **27**, split by tier:

| Pass | Scope | Ids |
|---|---|---|
| **Page 1** | Tier 1, high priority (5) | `afrigreyparrots`, `exoticParrotPetstore`, `africanGrayParrotsForSale`, `silvergateBirdFarm`, `birdsForSales` |
| **Page 2** | Tier 1, remaining (6) | `afroBirdsFarm`, `exoticParrotsPlanet`, `williamsAfricanGreys`, `shadesOfGreys`, `africanGreyAviaries`, `compoundExotics` |
| **Page 3** | Tier 2 aggregators (8) | `birdsNow`, `birdBreeders`, `qualityBirdsOnline`, `hoobly`, `petzlover`, `parrotAlert`, `petClassifieds`, `exoticPetsAvenue` |
| **Page 4** | Tier 3 informational (8) | `thesprucePets`, `wikipedia`, `rationalParrot`, `allAboutParrots`, `smallAnimalAdvice`, `vetExplainsPets`, `birdAddicts`, `parrotWebsite` |

- [ ] **Step 1: Dispatch the four passes**

Run them as four `cag-competitor-intel` subagents. Give each one this prompt, substituting the pass
number and its id list from the table above:

```
Competitor sweep — page N. Scope: the following registry ids from data/competitors.json:
<ids>.

Follow docs/artifacts/cags-universal-page-build-brief.html §6 (Competitor Research and Query
Fan-Out), and match the structure of the completed sibling pass at
docs/research/competitor-sweep-page5-2026-08-09.md — per-competitor SERP snapshot, query
fan-out, section/listing inventory, visual inventory, Reddit/forum mining, a correction block
against any existing docs/research/competitor-<id>-*.md baseline, and a key insight.

HARD CONSTRAINTS:
- RESEARCH ONLY. Do NOT modify data/competitors.json. Any new competitor or identity
  correction is a PROPOSAL at the end of your report, for breeder approval.
- Write exactly one file: docs/research/competitor-sweep-pageN-2026-08-09.md
- Anything you could not retrieve is written NOT FETCHED with the specific barrier named.
  Never infer a number you did not fetch. A 403 or 429 is a bot challenge, not a dead site —
  say so rather than reporting the site as dead.
- Open the file with a Method and Barriers table so a reader can calibrate every figure
  below it.
- End with an Open Flags section listing every NOT FETCHED item and its barrier.
```

- [ ] **Step 2: Verify each pass actually landed and is complete**

A "failed" notice is not proof the work was lost — page 5 was reported failed and its 646-line file was
complete. Check the files, not the notices:

```bash
for n in 1 2 3 4; do
  f="docs/research/competitor-sweep-page${n}-2026-08-09.md"
  if [ -f "$f" ]; then
    printf "page%s: %s lines | Open Flags: %s\n" "$n" "$(wc -l < "$f")" "$(grep -c 'Open Flags' "$f")"
  else
    printf "page%s: MISSING\n" "$n"
  fi
done
```

Expected: four rows, each with a non-trivial line count and `Open Flags: 1`. A file that exists but has
`Open Flags: 0` was truncated mid-write — re-run that pass.

- [ ] **Step 3: Confirm no pass wrote to the registry**

```bash
git status --porcelain data/competitors.json
```

Expected: **empty output.** If the registry shows as modified, a subagent violated the research-only
constraint — inspect the diff with `git diff data/competitors.json` and revert it before continuing.

- [ ] **Step 4: Commit the research**

```bash
git add docs/research/competitor-sweep-page1-2026-08-09.md docs/research/competitor-sweep-page2-2026-08-09.md docs/research/competitor-sweep-page3-2026-08-09.md docs/research/competitor-sweep-page4-2026-08-09.md
git commit -m "research(competitors): re-run passes 1-4 lost with the previous session"
```

Note the explicit file list — never `git add -A` when subagents have been writing, because it sweeps up
whatever else they left behind.

---

## Task 7: The consolidated deliverable

**Files:**
- Create: `docs/artifacts/cags-competitor-registry-2026-08-09.html`

CLAUDE.md rule 13: the deliverable is a published Artifact whose sections each carry a copy button and
which downloads as `.md` — not prose in the chat. Author the content once as markdown inside the page
and render it; that is what makes each copy button emit exact markdown rather than scraped HTML.

- [ ] **Step 1: Build the page**

Sections, each independently copyable:

1. **What changed in the registry** — the seven defects and their fixes, as a table.
2. **The Marietta Bird Shop finding** — the redirect chain, the reproduction evidence, and the
   never-link-to-this instruction.
3. **Identity resolution** — the 14-row table: id, resolved name, url, confidence, evidence.
4. **Proposed additions** — the 15 verified candidates plus anything Task 4 promoted, with the three
   scam-signal flags called out.
5. **Barriers** — every `NOT FETCHED` item across all six passes with its specific barrier, and the
   note that a logged-in Playwright profile plus Reddit API credentials would convert three of them.
6. **Open questions** — three, all for the breeder:
   - **Brick-and-mortar tiering.** Are shops that sell live greys (Parrot Stars, Birds By Joe) Tier 1
     `direct_breeder` as the 2026-08-03 sweep assigned, or Tier 4 `marketplace_retailer` as
     `mariettaBirdShop` — the same business model — is classified today? The registry is internally
     inconsistent on this, and the answer changes their monitoring cadence and which gap matrix they
     land in.
   - **`parrotAlert`'s taxonomy.** It is `tier: 2` with the label `non_commercial`, which is not one of
     the four labels in `_meta.tiers`. Either the tier map needs a fifth non-commercial tier, or
     Parrot Alert needs re-tiering. Task 2 normalised the label to keep the file self-consistent; that
     normalisation is reversible and should be revisited once the breeder decides.
   - **The scam-page follow-up** from Task 3 — whether the Marietta hijack and the three flagged
     resolved entries get written into `/how-to-avoid-african-grey-parrot-scams/`.

Before writing the page, load the `artifact-design` skill, as the Artifact tool requires.

- [ ] **Step 2: Publish it**

Publish with the Artifact tool, `file_path` set to the HTML above, a one-sentence `description`, and a
stable `favicon`. This is new work on a new topic, so it mints a new URL rather than updating an
existing artifact.

- [ ] **Step 3: Commit the source**

```bash
git add docs/artifacts/cags-competitor-registry-2026-08-09.html
git commit -m "docs(artifact): consolidated competitor registry repair + research deliverable"
```

---

## Task 8: Push

- [ ] **Step 1: Confirm the full gate is green before pushing**

```bash
python3 -m pytest tests/test_competitors_registry.py -v && python3 scripts/patch_competitor_registry.py --check
```

Expected: **9 passed**, then `No changes — registry already patched.` The second command returning "no
changes" is the proof that the committed registry is the patched one.

- [ ] **Step 2: Confirm you are on main**

```bash
git branch --show-current
```

Expected: `main`. Work on this project happens on `main` — only `main` auto-deploys, and finished work
on any other branch is live-404 while looking done.

- [ ] **Step 3: Push**

```bash
git push origin main
```

**Do not** run `astro build`, `generate_sitemaps.py`, or `indexnow_submit.py` afterwards. No page under
`src/pages/` changed, so there is no rendered output to submit.

---

## Self-Review

**Spec coverage** — the chosen scope was "patch the verified registry defects, re-fetch the 7b
candidates to promote the egg competitors, and re-run the four lost passes."

| Requirement | Task |
|---|---|
| Defect 1 — `_meta` count and description | Task 2 |
| Defects 2, 3, 4 — the 14 schema-broken entries | Task 2 |
| Defect 5 — dead `handRearedParrots` domain | Task 2 (+ locked by a test in Task 1) |
| Defect 6 — `denimixaniPetsParadise` name | Task 2 |
| Defect 7 — Marietta compromised redirect | Task 2 (+ locked by a test in Task 1), surfaced in Task 3 |
| Defect 8 — `parrotAlert` invalid tier_label | Task 2 (normalised + flagged REVIEW), open question in Task 7 |
| Re-fetch 7b, promote the egg competitors | Task 4 |
| Re-run the four lost passes | Task 6 |
| New competitors stay proposals until approved | Task 5, gated |
| Deliverable ships as an Artifact | Task 7 |

**Placeholder scan** — the 14-row `RESOLUTIONS` table carries real names and URLs; the four passes carry
real registry ids; every command has an expected output. The one deliberate deferral is Task 5 Step 2,
whose `ADDITIONS` content cannot be written until the breeder says which of the 15 are approved — that
is an approval gate, not a TODO.

**Type consistency** — `patch()` returns `(data, changes)` and `main()` unpacks it that way. `REGISTRY`
names the same path in both the script and the test. `REQUIRED_KEYS` in the test is exactly the 13-key
set the script backfills, with `access_status` and `threat_level` excluded from both as optional.
`--check` returns exit code 1 in Task 2 Step 2 and is described as such.

**One risk worth naming:** Task 2 Step 3 rewrites the whole JSON file through `json.dumps`, so key
order and any hand-formatting in the original are normalised. That is why Step 6 exists — it counts
entries, urls and names after the write, so a silent loss of rows cannot pass unnoticed.

**Dry-run status of this plan's code.** The test file and the patch script were extracted from the
fenced blocks above and executed against a scratch copy of `data/competitors.json` on 2026-08-09,
before this plan was handed over. Measured results, which are what the expected-output blocks state:

| Stage | Result |
|---|---|
| Tests against the unpatched registry | **8 failed, 1 passed** |
| `--check` dry run | **61 changes**, exit 1, nothing written |
| Tests after applying the patch | **9 passed** |
| Second run of the patch script | `No changes — registry already patched.`, file byte-identical |
| Integrity after patch | 44 entries · 44 with url · 44 with name · 0 legacy `domain` keys · `_meta.total_competitors` 44 |

The real `data/competitors.json` was **not** modified by that rehearsal — it still shows an Aug 3 mtime
and is untracked-clean in git. The executor starts from the same red state described in Task 1 Step 2.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-08-09-competitor-registry-repair.md`.

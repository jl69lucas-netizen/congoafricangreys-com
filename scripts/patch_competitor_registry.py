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

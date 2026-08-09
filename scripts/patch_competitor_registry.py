#!/usr/bin/env python3
"""Repair data/competitors.json — the seven defects recorded in
docs/superpowers/plans/2026-08-09-competitor-registry-repair.md

Also carries a second, independent one-shot migration (--add-approved) that adds
the 16 breeder-approved competitors from the 2026-08-09 cross-platform discovery
sweep and re-tiers exoticGlobalParrotsFarm into the new suspect_seller tier.

Each migration is one-shot, recorded in its own _meta.migrations_applied entry.
Re-running either after it has been applied is a no-op, so a later legitimate
sweep's dates, notes and names can never be clobbered by these dated 2026-08-09
values.

Usage:
    python3 scripts/patch_competitor_registry.py --check                 # report, write nothing
    python3 scripts/patch_competitor_registry.py                        # apply the registry repair
    python3 scripts/patch_competitor_registry.py --add-approved --check  # report the additions
    python3 scripts/patch_competitor_registry.py --add-approved         # apply the additions
"""

import argparse
import json
import pathlib
import sys

REGISTRY = pathlib.Path(__file__).resolve().parents[1] / "data" / "competitors.json"

MIGRATION_ID = "2026-08-09-registry-repair"
ADDITIONS_MIGRATION_ID = "2026-08-09-approved-additions"
TIER_SUSPECT = 6

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

# --- Second, independent one-shot migration: breeder-approved additions ------
# 16 competitors discovered in the 2026-08-09 cross-platform sweep, approved by
# the breeder for entry into the registry. Each carries the full 13-key schema;
# tier_label is resolved from _meta.tiers at write time, never hardcoded here.
ADDITIONS = [
    {
        "id": "toddMarcusBirdsExotic",
        "name": "Todd Marcus Birds Exotic",
        "url": "https://thebirdstore.com",
        "tier": 4,
        "states_active": ["NJ"],
        "priority": "high",
        "keywords": [
            "african grey parrot for sale",
            "congo african grey for sale",
            "african grey parrot breeder",
        ],
        "notes": (
            "Discovered 2026-08-09 cross-platform sweep. 43-year Delran NJ storefront; "
            "homepage \"FEATURED BABIES ... Congo African Grey\". The single strongest new "
            "name: found on all five platforms searched (Google, Reddit, YouTube, Facebook, "
            "Instagram) and the only one r/parrots names unprompted. Subject of the YouTube "
            "buyer-journey video \"The Largest Parrot Store In The USA\"."
        ),
    },
    {
        "id": "goldenCockatoo",
        "name": "Golden Cockatoo",
        "url": "https://goldencockatoo.com",
        "tier": 4,
        "states_active": [],
        "priority": "medium",
        "keywords": ["congo african grey for sale", "african grey parrot price"],
        "notes": (
            "Discovered 2026-08-09. Congo African Grey listed at $7,499.99, in-store purchase "
            "only, 3 certified avian specialists. Sets the high price anchor our $1,500-$3,500 "
            "Congo range is measured against."
        ),
    },
    {
        "id": "floridaParrot",
        "name": "Florida Parrot",
        "url": "https://floridaparrot.com",
        "tier": 1,
        "states_active": ["FL"],
        "priority": "high",
        "keywords": [
            "african grey parrot for sale",
            "hand raised african grey",
            "african grey parrot breeder",
        ],
        "notes": (
            "Discovered 2026-08-09. \"hand raised ... African greys\" with nationwide delivery; "
            "separately listed as a Miami FL breeder on BirdBreeders. Directly duplicates our "
            "shipping proposition."
        ),
    },
    {
        "id": "northShoreGreys",
        "name": "North Shore Greys LLC",
        "url": "https://northshoregreys.com",
        "tier": 1,
        "states_active": [],
        "priority": "high",
        "keywords": ["african grey parrot for sale", "african grey parrot breeder"],
        "notes": (
            "Discovered 2026-08-09. Title tag: \"North Shore Greys LLC - Parrot Food, Parrot "
            "Breeders, African Grey\". Grey-specific brand name competing directly for our head "
            "term."
        ),
    },
    {
        "id": "greyWingAviary",
        "name": "GreyWing Aviary",
        "url": "https://greywingaviary.com",
        "tier": 1,
        "states_active": [],
        "priority": "low",
        "keywords": ["african grey parrot for sale"],
        "notes": (
            "Discovered 2026-08-09. Named live inventory with sex, age and price (Mika/Joe/Gina, "
            "$600 each). SCAM SIGNAL: $600 is far below market for a captive-bred Congo. Track "
            "as a SERP competitor only - NEVER cite as a price benchmark. Returns 403 to plain "
            "curl (Cloudflare), 200 via Firecrawl."
        ),
    },
    {
        "id": "parrotAndBirdEmporium",
        "name": "The Parrot and Bird Emporium",
        "url": "https://www.theparrotandbirdemporium.com",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": ["african grey parrot for sale", "hand raised african grey"],
        "notes": (
            "Discovered 2026-08-09. Lists African Greys among hand-tamed stock; Facebook post "
            "shows a specific baby grey in target training. Posts availability like a breeder, "
            "not a directory."
        ),
    },
    {
        "id": "africanGreyParrotDotCom",
        "name": "African Grey Parrots For Sale",
        "url": "https://african-grey-parrot.com",
        "tier": 1,
        "states_active": [],
        "priority": "high",
        "keywords": [
            "african grey parrot for sale",
            "dna tested african grey",
            "african grey parrot breeder",
        ],
        "notes": (
            "Discovered 2026-08-09. Exact-match domain for our primary head term, 62 on-page "
            "grey mentions, claims DNA sexed + vet checked + shipping. Competes for the same "
            "query as our money page. Returns 403 to curl (bot challenge) but is live."
        ),
    },
    {
        "id": "forestryParrotsBreeder",
        "name": "Forestry Parrots Breeder",
        "url": "https://forestryparrotsbreeder.com",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": ["african grey parrot for sale"],
        "notes": (
            "Discovered 2026-08-09. Dedicated /product/african-grey-parrots-for-sale/; 65 "
            "on-page grey mentions; ranks top-20 for the head term."
        ),
    },
    {
        "id": "uncleTomsBirdFarm",
        "name": "Uncle Tom's Bird Farm",
        "url": "https://uncle-toms-parrot-farm.my-online.store",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": [
            "african grey breeding pair for sale",
            "african grey parrot eggs for sale",
        ],
        "notes": (
            "Discovered 2026-08-09. 93 on-page grey mentions. Sells both African Grey breeding "
            "pairs and African Grey eggs at $65 - competes with two of our pages at once."
        ),
    },
    {
        "id": "exoticLiveParrots",
        "name": "Exotic Live Parrots",
        "url": "https://exoticliveparrots.com",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": ["african grey parrot eggs for sale"],
        "notes": (
            "Discovered 2026-08-09. African Grey Parrot Eggs priced $99.98-$619.98 - direct "
            "rival to our $95/egg page."
        ),
    },
    {
        "id": "exoticBirdsForSales",
        "name": "Exotic Birds For Sales",
        "url": "https://exoticbirdsforsales.com",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": [
            "african grey parrot for sale",
            "african grey parrot eggs for sale",
        ],
        "notes": (
            "Discovered 2026-08-09. \"hand-raised parrots and candle-tested eggs ... African "
            "Greys\"; 31 grey mentions. Same dual bird+egg model we run."
        ),
    },
    {
        "id": "featherlandBreedersHub",
        "name": "Featherland Breeders Hub",
        "url": "https://featheredfriendshub.com",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": ["congo african grey for sale", "african grey parrot price"],
        "notes": (
            "Discovered 2026-08-09. Priced Congo grey inventory \"GREY CONGO $2,700.00 - "
            "$5,300.00\" - overlaps the top of our stated Congo range."
        ),
    },
    {
        "id": "parrotCrown",
        "name": "ParrotCrown",
        "url": "https://parrotcrown.com",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": ["congo african grey for sale", "african grey parrot price"],
        "notes": (
            "Discovered 2026-08-09. /product/congo-african-grey-parrot-for-sale/ at $7,000 "
            "with age banding."
        ),
    },
    {
        "id": "petBirdsBreeders",
        "name": "Pet Birds Breeders",
        "url": "https://petbirdsbreeders.com",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": ["african grey parrot for sale", "hand raised african grey"],
        "notes": (
            "Discovered 2026-08-09. \"healthy, hand-raised parrots ... African Greys\" as a "
            "headline species; 7 grey mentions."
        ),
    },
    {
        "id": "cpBirds",
        "name": "CP Birds",
        "url": "https://www.cpbirds.com",
        "tier": 1,
        "states_active": ["FL"],
        "priority": "high",
        "keywords": [
            "african grey breeding pair for sale",
            "african grey parrot eggs for sale",
        ],
        "notes": (
            "Discovered 2026-08-09. Orlando FL, US shipping, live /breeding-pairs inventory, "
            "and publishes \"Guide to Buying Parrot Fertile Eggs Online\" - competing on "
            "breeding pairs, eggs, and egg-buyer education simultaneously."
        ),
    },
    {
        "id": "sunnyvaleAviary",
        "name": "Sunnyvale Aviary",
        "url": "https://sunnyvaleaviary.com",
        "tier": 1,
        "states_active": [],
        "priority": "medium",
        "keywords": ["african grey parrot eggs for sale"],
        "notes": (
            "Discovered 2026-08-09; promoted from held-back status by the re-fetch pass "
            "(docs/research/competitor-refetch-verdicts-2026-08-09.md). The original sandbox "
            "recorded 000; this machine returned HTTP 200 with 4 African Grey mentions on the "
            "homepage. Indexed listing \"African Grey Parrot Eggs, $75.00\"."
        ),
    },
]

EGPF_RETIER_NOTE = (
    "RE-TIERED 2026-08-09 from tier 1 direct_breeder. DNS: exoticglobalparrotsfarm.com "
    "resolves to 81.99.162.48 (lang-sspiprxy.network.virginmedia.net - a Virgin Media "
    "RESIDENTIAL broadband line in London GB), shared with four other African Grey "
    "storefronts: sherrybirds.org, paradisebirdsfarmaviary.com, exoticparrotfarms.com, "
    "parrotsfarm.com. That is one operator running a domain network, not five independent "
    "breeders. Compounding signals from the page-5 sweep: three separate African Greys all "
    "listed at the identical age \"1 year 3 months old\", add-to-cart checkout with "
    "\"worldwide delivery\" of a CITES Appendix I species, and a US \"farm\" presentation "
    "served from UK residential broadband. NEVER cite as a price or practice benchmark. "
    "Usable as documented evidence on /how-to-avoid-african-grey-parrot-scams/. Shared-IP "
    "finding is reproducible with: dig +short A <domain>"
)


def patch(data):
    """Return (data, list_of_changes). Pure apart from mutating the dict it is given."""
    applied = data["_meta"].setdefault("migrations_applied", [])
    if MIGRATION_ID in applied:
        # One-shot migration. Re-running must never clobber a later legitimate sweep's
        # last_analyzed dates, notes, or resolved names with these dated 2026-08-09 values.
        return data, []

    changes = []
    tier_map = data["_meta"]["tiers"]
    if "5" not in tier_map:
        tier_map["5"] = "non_commercial"
        changes.append("_meta.tiers += 5: non_commercial")

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

        # parrotAlert is a lost-and-stolen-bird registry, not a seller. Its notes have
        # said so since before this migration ("Tier should be reclassified as
        # non-commercial"). Honour that rather than normalising the label away.
        if cid == "parrotAlert" and entry.get("tier") != 5:
            entry["tier"] = 5
            changes.append(f"{cid}: tier 2 -> 5 (non_commercial, per its own notes)")

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

    if changes:
        applied.append(MIGRATION_ID)
        changes.append(f"_meta.migrations_applied += {MIGRATION_ID}")

    return data, changes


def add_approved(data):
    """Second, independent one-shot migration: the 16 breeder-approved additions.

    Guarded by ADDITIONS_MIGRATION_ID exactly the way patch() is guarded by
    MIGRATION_ID — re-running after it has been applied is a no-op, so a later
    legitimate sweep's dates, notes and tiers can never be clobbered by these
    dated 2026-08-09 values. Independent of MIGRATION_ID: this function never
    reads or writes that marker, and patch() never reads or writes this one.
    """
    applied = data["_meta"].setdefault("migrations_applied", [])
    if ADDITIONS_MIGRATION_ID in applied:
        return data, []

    changes = []
    tier_map = data["_meta"]["tiers"]
    if "6" not in tier_map:
        tier_map["6"] = "suspect_seller"
        changes.append("_meta.tiers += 6: suspect_seller")

    existing_ids = {c["id"] for c in data["competitors"]}
    for item in ADDITIONS:
        cid = item["id"]
        if cid in existing_ids:
            continue
        tier_label = tier_map[str(item["tier"])]
        entry = {
            "id": cid,
            "name": item["name"],
            "url": item["url"],
            "tier": item["tier"],
            "tier_label": tier_label,
            "states_active": list(item["states_active"]),
            "primary_keywords": list(item["keywords"]),
            "keywords_found": list(item["keywords"]),
            "last_analyzed": "2026-08-09",
            "last_monitored": None,
            "priority": item["priority"],
            "notes": item["notes"],
            "social": dict(EMPTY_SOCIAL),
            "access_status": "accessible",
        }
        data["competitors"].append(entry)
        changes.append(f"+ {cid}: added (tier {item['tier']} {tier_label})")

    # Re-tier exoticGlobalParrotsFarm: shares a London residential IP with four
    # other African Grey storefronts — one operator, not five breeders.
    for entry in data["competitors"]:
        if entry["id"] != "exoticGlobalParrotsFarm":
            continue
        if entry.get("tier") != TIER_SUSPECT:
            old_tier = entry.get("tier")
            entry["tier"] = TIER_SUSPECT
            changes.append(f"exoticGlobalParrotsFarm: tier {old_tier} -> {TIER_SUSPECT}")
        expected_label = tier_map[str(TIER_SUSPECT)]
        if entry.get("tier_label") != expected_label:
            entry["tier_label"] = expected_label
            changes.append(f"exoticGlobalParrotsFarm: tier_label -> {expected_label}")
        if entry.get("priority") != "low":
            entry["priority"] = "low"
            changes.append("exoticGlobalParrotsFarm: priority -> low")
        if entry.get("notes") != EGPF_RETIER_NOTE:
            entry["notes"] = EGPF_RETIER_NOTE
            changes.append("exoticGlobalParrotsFarm: notes replaced with re-tier record")
        break

    # _meta must describe the file it is attached to, same as patch()'s Defect 1.
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

    if changes:
        applied.append(ADDITIONS_MIGRATION_ID)
        changes.append(f"_meta.migrations_applied += {ADDITIONS_MIGRATION_ID}")

    return data, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report changes, write nothing")
    parser.add_argument(
        "--add-approved",
        action="store_true",
        help="run the 2026-08-09-approved-additions migration instead of the registry repair",
    )
    args = parser.parse_args()

    data = json.loads(REGISTRY.read_text())
    migration = add_approved if args.add_approved else patch
    data, changes = migration(data)

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

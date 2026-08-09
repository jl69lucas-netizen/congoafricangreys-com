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

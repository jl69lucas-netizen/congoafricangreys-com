#!/usr/bin/env python3
"""Idempotently add a `social` block to every competitor in data/competitors.json.
Re-run safe: only adds the block / missing keys; never overwrites existing handle data.
Seeds confirmed handles from the 2026-06-06 social research sprint."""
import json, pathlib

PATH = pathlib.Path("data/competitors.json")
SOCIAL_KEYS = ["instagram", "facebook", "youtube", "tiktok", "pinterest", "twitter_x"]
# Confirmed in docs/research/social-media-landscape-2026-06-06.md
SEED = {
    "afroBirdsFarm": {"facebook": "https://www.facebook.com/afrobirdsfarm/"},
}

def blank():
    b = {k: None for k in SOCIAL_KEYS}
    b["followers"] = None       # last-measured follower count (int) per platform later
    b["cadence"] = None         # observed posting frequency, free text
    b["last_social_audit"] = None
    return b

def main():
    data = json.loads(PATH.read_text())
    comps = data["competitors"] if isinstance(data, dict) and "competitors" in data else data
    changed = 0
    items = comps.items() if isinstance(comps, dict) else [(c.get("id"), c) for c in comps]
    for cid, c in items:
        if "social" not in c:
            c["social"] = blank(); changed += 1
        else:
            for k in SOCIAL_KEYS + ["followers", "cadence", "last_social_audit"]:
                c["social"].setdefault(k, None)
        if cid in SEED:
            for k, v in SEED[cid].items():
                if not c["social"].get(k):
                    c["social"][k] = v
    PATH.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"social block ensured on all competitors; {changed} newly added")

if __name__ == "__main__":
    main()

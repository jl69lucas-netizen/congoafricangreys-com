#!/usr/bin/env python3
"""Copy verbatim buyer reviews out of the BUILT site into data/reviews.json.

The ledger is filled by copy, never by retyping: for each spec the quote comes
from the page's own `Review` JSON-LD (exact), or — on pages with no schema —
from the visible text node that starts with the given prefix. The avatar is the
first <img> whose alt begins with the buyer's name.

    python3 scripts/review_inventory.py            # print what would be added
    python3 scripts/review_inventory.py --write    # append to data/reviews.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
LEDGER = ROOT / "data" / "reviews.json"
KEY = 60

# (id, name, location exactly as the source page shows it, source slug, prefix if no schema, provenance, confirmed,
#  [optional avatar src when the photo's alt does not start with the full name])
CONFIRMED_SPECS = [
    ("q6", "Stanley Perkin", "Oceanside, CA 92054", "dna-tested-african-grey-for-sale", None,
     "breeder-supplied 2026-07-22 (commit 70786197)", "2026-07-22"),
    ("q7", "Jesse Ovalle", "Baton Rouge, LA 70806", "dna-tested-african-grey-for-sale", None,
     "breeder-supplied 2026-07-22 (commit 70786197)", "2026-07-22"),
    ("q8", "Meredith Plaisance", "Hartsville, SC 29550", "african-greys-for-sale-with-health-guarantee", None,
     "breeder-supplied, verbatim 2026-07-25", "2026-07-25",
     "/images/health-guarantee-page/meredith-plaisance-hartsville-sc-health-guarantee-review.webp"),
    ("q9", "Jeffrey Hendershot", "Centennial, CO 80112", "african-greys-for-sale-with-health-guarantee", None,
     "breeder-supplied, verbatim 2026-07-25", "2026-07-25",
     "/images/health-guarantee-page/jeffrey-hendershot-centennial-co-guaranteed-grey-review.webp"),
    ("q10", "Joanna Thomas", "Oildale, CA", "baby-african-grey-parrot-for-sale", None,
     "baby-page build (commit b0d9f44f, 2026-07-27)", "2026-07-27",
     "/images/baby-page/review-joanna-california-220.webp"),
    ("q11", "Anthony Tershal", "Lakewood, WA", "baby-african-grey-parrot-for-sale", None,
     "baby-page build (commit b0d9f44f, 2026-07-27)", "2026-07-27",
     "/images/baby-page/review-anthony-washington-220.webp"),
    ("q12", "Joshua Erwin", "San Bernardino, California", "african-grey-breeding-pair-for-sale", None,
     "real, named, attributed quote 2026-08-07", "2026-08-07"),
    ("q13", "Walter Zander", "Fort Washington, PA", "congo-african-grey-parrot-pair-for-sale",
     "After weeks of searching for an affordable African grey parrot pair",
     "breeder brief 8cda89e3 (2026-07-30)", "2026-07-30"),
    ("q14", "Alene Murphy", "Savannah, GA", "congo-african-grey-parrot-pair-for-sale",
     "Finding a reliable African grey parrot pair for sale",
     "breeder brief 8cda89e3 (2026-07-30) — Savannah, GA", "2026-07-30"),
    ("q15", "Lawrence Brunner", "Fullerton, CA", "available", "I'd been burned by a deposit scam before",
     "breeder ruling 2026-09-11 (chat), wording identical to the /available/ hub", "2026-09-11"),
    ("q16", "Sandra Soliz", "Rome, GA", "available", "What sold me was how well they actually knew",
     "breeder ruling 2026-09-11 (chat), wording identical to the /available/ hub", "2026-09-11"),
    ("q17", "Ida Brim", "Nashville, TN", "available", "From the first email to home delivery, everything",
     "breeder ruling 2026-09-11 (chat), wording identical to the /available/ hub", "2026-09-11"),
]
# Disputed reviews go here (ids pN). --write replaces data["pending"] wholesale from this list,
# so record a dispute here, never by hand in data/reviews.json.
PENDING_SPECS = []


def norm(s: str) -> str:
    s = (s.replace("’", "'").replace("‘", "'")
          .replace("“", '"').replace("”", '"').replace("\xa0", " "))
    return re.sub(r"\s+", " ", s).strip()


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes, self.imgs, self.ld = [], [], []
        self._skip, self._in_ld, self._ldbuf = 0, False, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld, self._ldbuf = True, []
        elif tag in ("script", "style"):
            self._skip += 1
        elif tag == "img":
            self.imgs.append((a.get("alt") or "", a.get("src") or ""))

    def handle_endtag(self, tag):
        if tag == "script" and self._in_ld:
            self._in_ld = False
            try:
                self.ld.append(json.loads("".join(self._ldbuf)))
            except json.JSONDecodeError:
                pass
        elif tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_ld:
            self._ldbuf.append(data)
        elif not self._skip and data.strip():
            self.nodes.append(re.sub(r"\s+", " ", data).strip())


def schema_bodies(ld) -> dict[str, str]:
    out: dict[str, str] = {}

    def walk(o):
        if isinstance(o, list):
            for x in o:
                walk(x)
        elif isinstance(o, dict):
            if o.get("@type") == "Review":
                a = o.get("author")
                out.setdefault(a.get("name") if isinstance(a, dict) else a,
                               re.sub(r"\s+", " ", o.get("reviewBody") or "").strip())
            for v in o.values():
                walk(v)

    walk(ld)
    return out


def load(slug: str) -> Page:
    p = DIST / slug / "index.html"
    if not p.exists():
        sys.exit(f"dist/{slug}/index.html missing — run `npx astro build` first")
    pg = Page()
    pg.feed(p.read_text(encoding="utf-8"))
    return pg


def extract(spec) -> dict:
    rid, name, location, slug, prefix, source, confirmed, *rest = spec
    avatar_override = rest[0] if rest else None
    pg = load(slug)
    visible = norm("\n".join(pg.nodes))
    body, how = schema_bodies(pg.ld).get(name), "schema"
    if body is None:
        if not prefix:
            sys.exit(f"{rid} {name}: no Review schema on {slug} and no prefix given")
        idx = next((i for i, n in enumerate(pg.nodes) if norm(n).lstrip('"').startswith(norm(prefix))), None)
        if idx is None:
            sys.exit(f"{rid} {name}: prefix {prefix!r} not found on {slug}")
        if name not in " ".join(pg.nodes[max(0, idx - 8): idx + 9]):
            sys.exit(f"{rid} {name}: the quote matched on {slug} is not in {name}'s card (name not within 8 nodes)")
        body, how = pg.nodes[idx].strip().strip('"“”').strip(), "visible"
    if not re.search(r"[.!?]$", body):
        sys.exit(f"{rid} {name}: quote does not end in . ! or ? — it may be cut at an inline tag on {slug}")
    if norm(body)[:KEY] not in visible:
        sys.exit(f"{rid} {name}: extracted text is not visible on {slug} — inspect before ledgering")
    if norm(location) not in visible:
        sys.exit(f"{rid} {name}: location {location!r} is not shown on {slug} — copy it exactly as the page shows it")
    if avatar_override and not any(src == avatar_override for _, src in pg.imgs):
        sys.exit(f"{rid} {name}: avatar {avatar_override!r} is not an <img> on {slug}")
    avatar = avatar_override or next((src for alt, src in pg.imgs if alt.startswith(name)), None)
    print(f"{rid:4s} {name:20s} via {how:7s} avatar={avatar}\n     {body[:110]}…")
    entry = {"id": rid, "quote": body, "name": name, "location": location, "bird": None,
             "avatar": avatar, "source": f"{slug} — {source}"}
    if confirmed:
        entry["confirmed"] = confirmed
    return entry


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="append to data/reviews.json")
    args = ap.parse_args()

    confirmed = [extract(s) for s in CONFIRMED_SPECS]
    pending = [extract(s) for s in PENDING_SPECS]
    if not args.write:
        print(f"\n{len(confirmed)} confirmed + {len(pending)} pending extracted (dry run)")
        return 0

    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    by_id = {r["id"]: r for r in data["reviews"]}
    have_names = {r["name"] for r in data["reviews"]}
    added, filled = [], []
    for e in confirmed:
        old = by_id.get(e["id"])
        if old is None:
            if e["name"] not in have_names:
                added.append(e)
            continue
        for field in ("quote", "name", "location"):
            if norm(old[field]) != norm(e[field]):
                sys.exit(f"{e['id']}: the ledger's {field} no longer matches the page — the page or the "
                         f"ledger changed. Resolve by hand with the breeder; never by re-running this script.")
        if not old.get("avatar") and e["avatar"]:
            old["avatar"] = e["avatar"]
            filled.append(e["id"])
    data["reviews"].extend(added)
    promoted = have_names | {e["name"] for e in added}
    data["pending"] = [p for p in pending if p["name"] not in promoted]
    LEDGER.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"\nwrote {len(added)} new confirmed, filled {len(filled)} avatar(s) {filled}, "
          f"{len(data['pending'])} pending → {LEDGER.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

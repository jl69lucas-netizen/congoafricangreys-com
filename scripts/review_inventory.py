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

# (id, name, location exactly as the source page shows it, source slug, prefix if no schema, provenance, confirmed)
CONFIRMED_SPECS = [
    ("q6", "Stanley Perkin", "Oceanside, CA 92054", "dna-tested-african-grey-for-sale", None,
     "breeder-supplied 2026-07-22 (commit 70786197)", "2026-07-22"),
    ("q7", "Jesse Ovalle", "Baton Rouge, LA 70806", "dna-tested-african-grey-for-sale", None,
     "breeder-supplied 2026-07-22 (commit 70786197)", "2026-07-22"),
    ("q8", "Meredith Plaisance", "Hartsville, SC 29550", "african-greys-for-sale-with-health-guarantee", None,
     "breeder-supplied, verbatim 2026-07-25", "2026-07-25"),
    ("q9", "Jeffrey Hendershot", "Centennial, CO 80112", "african-greys-for-sale-with-health-guarantee", None,
     "breeder-supplied, verbatim 2026-07-25", "2026-07-25"),
    ("q10", "Joanna Thomas", "Oildale, CA", "baby-african-grey-parrot-for-sale", None,
     "baby-page build (commit b0d9f44f, 2026-07-27)", "2026-07-27"),
    ("q11", "Anthony Tershal", "Lakewood, WA", "baby-african-grey-parrot-for-sale", None,
     "baby-page build (commit b0d9f44f, 2026-07-27)", "2026-07-27"),
    ("q12", "Joshua Erwin", "San Bernardino, California", "african-grey-breeding-pair-for-sale", None,
     "real, named, attributed quote 2026-08-07", "2026-08-07"),
    ("q13", "Walter Zander", "Fort Washington, PA", "congo-african-grey-parrot-pair-for-sale",
     "After weeks of searching for an affordable African grey parrot pair",
     "breeder brief 8cda89e3 (2026-07-30)", "2026-07-30"),
    ("q14", "Alene Murphy", "Savannah, GA", "congo-african-grey-parrot-pair-for-sale",
     "Finding a reliable African grey parrot pair for sale",
     "breeder brief 8cda89e3 (2026-07-30) — Savannah, GA", "2026-07-30"),
]
_DISPUTED = ("commit a6681e66 (2026-06-19) calls them real reviewers; memory 2026-06-26 records the set "
             "as invented — breeder ruling owed")
PENDING_SPECS = [
    ("p1", "Lawrence Brunner", "Fullerton, CA", "available/roys", "I'd been burned by a deposit scam before", _DISPUTED, None),
    ("p2", "Sandra Soliz", "Rome, GA", "available/roys", "What sold me was how well they actually knew", _DISPUTED, None),
    ("p3", "Ida Brim", "Nashville, TN", "available/roys", "From the first email to home delivery here in Nashville", _DISPUTED, None),
]


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
    rid, name, location, slug, prefix, source, confirmed = spec
    pg = load(slug)
    body, how = schema_bodies(pg.ld).get(name), "schema"
    if body is None:
        if not prefix:
            sys.exit(f"{rid} {name}: no Review schema on {slug} and no prefix given")
        node = next((n for n in pg.nodes if norm(n).lstrip('"').startswith(norm(prefix))), None)
        if node is None:
            sys.exit(f"{rid} {name}: prefix {prefix!r} not found on {slug}")
        body, how = node.strip().strip('"“”').strip(), "visible"
    on_page = norm(body)[:KEY] in norm("\n".join(pg.nodes))
    avatar = next((src for alt, src in pg.imgs if alt.startswith(name)), None)
    print(f"{rid:4s} {name:20s} via {how:7s} visible={on_page!s:5s} avatar={avatar}\n     {body[:110]}…")
    if not on_page:
        sys.exit(f"{rid} {name}: extracted text is not visible on {slug} — inspect before ledgering")
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
    have_ids = {r["id"] for r in data["reviews"]}
    have_names = {r["name"] for r in data["reviews"]}
    added = [e for e in confirmed if e["id"] not in have_ids and e["name"] not in have_names]
    data["reviews"].extend(added)
    data["pending"] = pending
    LEDGER.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"\nwrote {len(added)} confirmed + {len(pending)} pending to {LEDGER.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

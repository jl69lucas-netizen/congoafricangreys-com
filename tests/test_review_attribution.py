"""Review attribution — one quote, one buyer, everywhere.

data/reviews.json is the single source of truth for who said what (names come
from the breeder only). These tests guard two things:

1. the ledger itself is well-formed (every quote once, no NOT FETCHED names);
2. every inline review object in src/pages/**/*.astro agrees with it, and no
   quote is credited to two different people anywhere in src.

The src scanner deliberately mirrors scripts/sweep_review_attribution.py: it
looks only at FLAT object literals (no nested braces) that carry a `quote:` key
of >= 40 characters, so schema `Review` objects (nested `author: {...}`) and CSS
blocks are ignored.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REVIEWS_JSON = ROOT / "data" / "reviews.json"
PAGES = ROOT / "src" / "pages"

FLAT_OBJECT = re.compile(r"\{[^{}]*\}", re.S)
STRING = r"""(["'])((?:\\.|(?!\1).)*)\1"""
QUOTE_RE = re.compile(r"\bquote\s*:\s*" + STRING, re.S)
NAME_RE = re.compile(r"\bname\s*:\s*" + STRING, re.S)
LOC_RE = re.compile(r"\b(?:loc|location)\s*:\s*" + STRING, re.S)
KEY = 60


def _unescape(s: str) -> str:
    return re.sub(r"\\(.)", r"\1", s)


def _src_reviews():
    """Yield (path, quote, name, location) for every flat review object in src."""
    for path in sorted(PAGES.rglob("*.astro")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for obj in FLAT_OBJECT.finditer(text):
            body = obj.group(0)
            q = QUOTE_RE.search(body)
            if not q or len(q.group(2)) < 40:
                continue
            n = NAME_RE.search(body)
            if not n:
                continue
            loc = LOC_RE.search(body)
            yield (
                path,
                _unescape(q.group(2)),
                _unescape(n.group(2)),
                _unescape(loc.group(2)) if loc else None,
            )


def _load_json():
    assert REVIEWS_JSON.exists(), f"{REVIEWS_JSON} is missing"
    return json.loads(REVIEWS_JSON.read_text(encoding="utf-8"))


def test_reviews_json_exists_and_has_one_name_per_quote():
    data = _load_json()
    reviews = data["reviews"]
    assert reviews, "reviews.json has no reviews"
    keys = [r["quote"][:KEY] for r in reviews]
    assert len(keys) == len(set(keys)), "a quote appears more than once in reviews.json"
    for r in reviews:
        assert r["name"] and r["name"] != "NOT FETCHED", f"{r['id']} has no confirmed name"
        assert r["location"] and r["location"] != "NOT FETCHED", f"{r['id']} has no location"
        assert len(r["quote"]) >= 40, f"{r['id']} quote is suspiciously short"


def test_no_quote_is_credited_to_two_names_anywhere_in_src():
    names_by_quote: dict[str, set[str]] = defaultdict(set)
    where: dict[str, set[str]] = defaultdict(set)
    seen = 0
    for path, quote, name, _loc in _src_reviews():
        seen += 1
        names_by_quote[quote[:KEY]].add(name)
        where[quote[:KEY]].add(f"{path.relative_to(ROOT)} -> {name}")
    assert seen >= 10, f"scanner examined only {seen} review objects — check the extractor"
    multi = {k: sorted(where[k]) for k, v in names_by_quote.items() if len(v) > 1}
    assert not multi, "quotes credited to more than one name:\n" + json.dumps(multi, indent=2)


def test_every_src_review_matches_reviews_json():
    data = _load_json()
    canonical = {r["quote"][:KEY]: r for r in data["reviews"]}
    matched = 0
    bad = []
    for path, quote, name, _loc in _src_reviews():
        ref = canonical.get(quote[:KEY])
        if ref is None:
            continue
        matched += 1
        if name != ref["name"]:
            bad.append(f"{path.relative_to(ROOT)}: {ref['id']} credited to {name!r}, ledger says {ref['name']!r}")
    assert matched >= 10, f"only {matched} src reviews matched the ledger — check the extractor"
    assert not bad, "\n".join(bad)

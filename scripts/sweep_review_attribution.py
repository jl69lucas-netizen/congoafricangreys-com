#!/usr/bin/env python3
"""Sweep every inline review object in src/pages/**/*.astro into agreement with
data/reviews.json — the single source of truth for who said what.

Two passes per review object (a FLAT `{...}` literal with a `quote:` of >= 40
characters and a `name:` key; nested schema objects and CSS blocks never match):

1. `remap` — a historical mis-attribution keyed on (name, quote prefix). The
   quote text is replaced with the target review's, name/location are set, the
   avatar is set when the object carries an avatar field AND the target has one,
   and a `headline:` (if present) is replaced with the target's headline.
2. canonical — any object whose quote matches a ledger quote (first 60 chars)
   gets the ledger's name and location.

Only the changed values are rewritten; the object's own key names
(`loc`/`location`, `avatar`/`avatarSrc`), key order, indentation and quote
delimiters are preserved. A value that contains its delimiter switches to the
other delimiter rather than emitting a backslash escape.

    python3 scripts/sweep_review_attribution.py --check   # exit 1 if anything is pending
    python3 scripts/sweep_review_attribution.py           # write, print every file changed
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWS_JSON = ROOT / "data" / "reviews.json"
PAGES = ROOT / "src" / "pages"
KEY = 60

FLAT_OBJECT = re.compile(r"\{[^{}]*\}", re.S)
# groups: 1 key · 2 colon+space · 3 delimiter · 4 raw (still escaped) contents
FIELD_STRING = r"""(["'])((?:\\.|(?!\3).)*)\3"""


def field_re(keys: str) -> re.Pattern:
    return re.compile(r"(?<![\w$])(" + keys + r")(\s*:\s*)" + FIELD_STRING, re.S)


QUOTE_RE = field_re("quote")
NAME_RE = field_re("name")
LOC_RE = field_re("loc|location")
AVATAR_RE = field_re("avatar|avatarSrc")
HEADLINE_RE = field_re("headline")


def unescape(s: str) -> str:
    return re.sub(r"\\(.)", r"\1", s)


def literal(value: str, current_delim: str) -> str:
    """Render `value` as a JS string literal, keeping the object's delimiter when possible."""
    other = '"' if current_delim == "'" else "'"
    if current_delim not in value:
        delim = current_delim
    elif other not in value:
        delim = other
    else:
        delim = current_delim
    body = value.replace("\\", "\\\\").replace(delim, "\\" + delim)
    return f"{delim}{body}{delim}"


def set_field(body: str, pattern: re.Pattern, value: str, changes: list, label: str):
    m = pattern.search(body)
    if not m:
        return body
    old = unescape(m.group(4))
    if old == value:
        return body
    new = m.group(1) + m.group(2) + literal(value, m.group(3))
    changes.append((label, old, value))
    return body[: m.start()] + new + body[m.end() :]


def load_ledger():
    data = json.loads(REVIEWS_JSON.read_text(encoding="utf-8"))
    for r in data["reviews"]:
        if not r.get("name") or r["name"] == "NOT FETCHED":
            sys.exit(f"refusing to run: {r['id']} in data/reviews.json has no confirmed name")
    by_id = {r["id"]: r for r in data["reviews"]}
    by_key = {r["quote"][:KEY]: r for r in data["reviews"]}
    return by_id, by_key, data.get("remap", [])


def rewrite_object(body: str, by_id, by_key, remap):
    q = QUOTE_RE.search(body)
    if not q or len(q.group(4)) < 40:
        return body, []
    n = NAME_RE.search(body)
    if not n:
        return body, []
    quote, name = unescape(q.group(4)), unescape(n.group(4))
    changes: list = []

    target = None
    for rule in remap:
        if name == rule["when_name"] and quote.startswith(rule["when_quote_startswith"]):
            target = by_id[rule["use"]]
            break
    if target is not None:
        body = set_field(body, QUOTE_RE, target["quote"], changes, "quote")
        if target.get("avatar"):
            body = set_field(body, AVATAR_RE, target["avatar"], changes, "avatar")
        if target.get("headline"):
            body = set_field(body, HEADLINE_RE, target["headline"], changes, "headline")
        quote = target["quote"]

    ref = by_key.get(quote[:KEY])
    if ref is not None:
        body = set_field(body, NAME_RE, ref["name"], changes, "name")
        body = set_field(body, LOC_RE, ref["location"], changes, "location")
    return body, changes


def sweep_file(path: Path, by_id, by_key, remap):
    text = path.read_text(encoding="utf-8")
    out, changes, pos = [], [], 0
    for m in FLAT_OBJECT.finditer(text):
        new_body, obj_changes = rewrite_object(m.group(0), by_id, by_key, remap)
        out.append(text[pos : m.start()])
        out.append(new_body)
        pos = m.end()
        changes.extend(obj_changes)
    out.append(text[pos:])
    return "".join(out), changes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="report pending changes; exit 1 if any")
    args = ap.parse_args()

    by_id, by_key, remap = load_ledger()
    pending = 0
    files_changed = []
    for path in sorted(PAGES.rglob("*.astro")):
        if not path.is_file():
            continue
        new_text, changes = sweep_file(path, by_id, by_key, remap)
        if not changes:
            continue
        rel = path.relative_to(ROOT)
        pending += len(changes)
        files_changed.append(str(rel))
        print(f"{rel}  ({len(changes)} change{'s' if len(changes) != 1 else ''})")
        for label, old, new in changes:
            print(f"    {label:9s} {old[:48]!r} -> {new[:48]!r}")
        if not args.check:
            path.write_text(new_text, encoding="utf-8")

    if args.check:
        print(f"\n--check: {pending} pending change(s) in {len(files_changed)} file(s)")
        return 1 if pending else 0
    print(f"\nwrote {len(files_changed)} file(s), {pending} value(s) changed")
    for f in files_changed:
        print(f"  {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

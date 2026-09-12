#!/usr/bin/env python3
"""pageboard — the Page Board library. Every board CLI imports this; it reads files and
computes, it never writes a board or publishes anything (the CLIs do).
Spec: docs/superpowers/specs/2026-09-12-page-board-system-design.md
"""
import hashlib, json, pathlib, re, sys
import jsonschema

# The header pre-check must judge a heading the way `dup_content_audit.py --headers`
# will judge it after the build, so it borrows that module's chrome rules rather than
# growing a second copy that drifts. It lives beside this file in scripts/.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dup_content_audit as DUP
HEADER_WHITELIST = DUP.HEADER_WHITELIST   # phrases the dup gate already forgives

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
ONTOLOGY = ROOT / "data" / "cag-ontology.json"
LEDGER = ROOT / "data" / "component-ledger.json"
DIST = ROOT / "dist"


class BoardError(Exception):
    """A record that does not describe a buildable page."""


def _read_json(path):
    """Read a JSON file, reporting a malformed one as a BoardError like every other fault."""
    try:
        return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise BoardError(f"{path}: {e}") from None


def _validate(doc, schema_name):
    schema = json.loads((SCHEMAS / schema_name).read_text(encoding="utf-8"))
    try:
        jsonschema.validate(doc, schema)
    except jsonschema.ValidationError as e:
        path = "/".join(str(p) for p in e.absolute_path) or "(root)"
        raise BoardError(f"{schema_name}: {path}: {e.message}") from None


def validate_board(board):
    _validate(board, "board.schema.json")
    ids, ns = [], []
    for sec in board["sections"]:
        if sec["words"]["min"] > sec["words"]["max"]:
            raise BoardError(f"section {sec['id']}: words.min {sec['words']['min']} > words.max {sec['words']['max']}")
        ids.append(sec["id"])
        ns.append(sec["n"])
    for label, values in (("id", ids), ("n", ns)):
        dupes = sorted({v for v in values if values.count(v) > 1})
        if dupes:
            raise BoardError(f"duplicate section {label}: {', '.join(str(d) for d in dupes)}")


def validate_ontology(ont):
    _validate(ont, "ontology.schema.json")


TUPLE_ID_KEYS = ("hero", "dial", "rail", "toc", "table", "faq")


def tuple_component_ids(t):
    """Every component id a ledger/board tuple names, in a fixed order."""
    return [t[k] for k in TUPLE_ID_KEYS if t.get(k)] + list(t.get("takeaway", []))


def validate_ledger(ledger):
    _validate(ledger, "component-ledger.schema.json")
    # `#refresh` is the board's placeholder for "reuse this shell along an axis you have
    # not named yet". It may appear in a candidate list; recording one in the ledger would
    # claim a delta that does not exist, so the author must rename it before it lands.
    for page, t in ledger.get("pages", {}).items():
        for cid in tuple_component_ids(t):
            if cid.endswith("#refresh"):
                raise BoardError(
                    f"{page}: {cid} is the unnamed refresh placeholder — rename it to base#<delta> before recording it")


def board_path(slug):
    return ROOT / "data" / "pages" / slug / "board.json"


def load_board(slug):
    p = board_path(slug)
    if not p.exists():
        raise BoardError(f"no board for {slug}: {p} does not exist")
    board = _read_json(p)
    validate_board(board)
    return board


def save_board(slug, board):
    validate_board(board)
    if board["meta"]["slug"] != slug:
        raise BoardError(f"slug mismatch: saving as {slug} but the record says {board['meta']['slug']}")
    p = board_path(slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(board, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_ontology():
    if not ONTOLOGY.exists():
        raise BoardError(f"no ontology: {ONTOLOGY} does not exist")
    ont = _read_json(ONTOLOGY)
    validate_ontology(ont)
    return ont


def load_ledger():
    if not LEDGER.exists():
        raise BoardError(f"no component ledger: {LEDGER} does not exist")
    ledger = _read_json(LEDGER)
    validate_ledger(ledger)
    return ledger


LIFECYCLE_ASSET_KEYS = ("status", "file")


def record_hash(board):
    """sha256 of the record's CONTENT, keys sorted. Four fields are excluded because they
    are lifecycle state rather than content, and they move after approval by design:
    the top-level `approval`, `meta.status` (board_approve.py flips it to "approved"
    the moment it stamps the hash), and every asset's `status` and `file` (baking a photo
    fills them in). Hashing any of them would make every legitimate approval, and every
    later bake, read as a post-approval edit. An edit anywhere else DOES change the hash,
    which is how a real post-approval edit sends the page back to the board."""
    body = {k: v for k, v in board.items() if k != "approval"}
    meta = body.get("meta")
    if isinstance(meta, dict):
        body["meta"] = {k: v for k, v in meta.items() if k != "status"}
    assets = body.get("assets")
    if isinstance(assets, list):
        body["assets"] = [
            {k: v for k, v in a.items() if k not in LIFECYCLE_ASSET_KEYS} if isinstance(a, dict) else a
            for a in assets
        ]
    blob = json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def approval_matches(board):
    a = board.get("approval")
    return isinstance(a, dict) and a.get("record_hash") == record_hash(board)


def base_of(component_id):
    """The shell an id names: `base` itself, or the `base` of a `base#delta` refresh."""
    return component_id.strip().split("#", 1)[0]


# A ledger page "owns" every component named anywhere in its tuple. A hero, dial, rail,
# TOC, table, FAQ shell or takeaway a sibling owns is removed from the pool; the record
# keeps who owned it so the board can say so. The page itself never excludes itself.
# A spent shell is not gone, it is refreshed: an owned base comes back as `base#refresh`,
# a placeholder the board author renames to the axis it actually varies, and a refreshed
# id owns its base as well as itself, so a non-empty pool never offers an empty menu.
def owned_components(ledger, exclude_slug=None):
    owned = {}

    def claim(component_id, page):
        for key in dict.fromkeys((component_id, base_of(component_id))):
            if page not in owned.setdefault(key, []):
                owned[key].append(page)

    for page, t in ledger.get("pages", {}).items():
        if page == exclude_slug:
            continue
        for cid in tuple_component_ids(t):
            claim(cid, page)
    return owned


# A section shape normally draws from the pool of its own name. `nav` is the exception:
# a nav-shaped section is a table of contents, and the TOC shells live in the `toc` pool
# (the `nav` pool is the dials and rails, which are page chrome, not section options).
SHAPE_POOL = {"nav": "toc"}


def candidates_for(shape, ledger, slug):
    """The options a section of this shape may be offered.

    Most pools are SHARED: dial-1-clay is on nine pages by design, and the ledger's
    discipline is that the COMBO differs, not the component. Only the pools listed in
    `refresh_pools` are scarce enough that a sibling's claim costs the shell — there a
    spent base comes back as `base#refresh` for the author to rename."""
    if shape == "standard":
        return [], []
    pool_name = SHAPE_POOL.get(shape, shape)
    pool = list(ledger.get("pools", {}).get(pool_name, []))
    if pool_name not in ledger.get("refresh_pools", []):
        return pool, []
    owned = owned_components(ledger, exclude_slug=slug)
    cands, excluded = [], []
    for c in pool:
        base = base_of(c)
        owners = owned.get(base)
        if owners:
            cands.append(f"{base}#refresh")
            excluded.append({"component": base, "owner": owners[0], "owners": list(owners)})
        else:
            cands.append(c)
    return cands, excluded


def spent_h6_prefixes(ledger, exclude_slug=None):
    """{prefix: [owner, ...]} in ledger order. Owner LISTS, like owned_components(): two
    pages can already spend one prefix, and a report that named only the first would
    understate what a third page has to rename."""
    out = {}
    for page, t in ledger.get("pages", {}).items():
        if page == exclude_slug:
            continue
        for p in t.get("h6_prefixes", []):
            if page not in out.setdefault(p, []):
                out[p].append(page)
    return out


TOKEN = re.compile(r"[a-z0-9$']+")
SPECIES = re.compile(r"\b(congo|timneh|macaw|cockatoo|amazon(?: parrot)?|eclectus|african greys?|greys?)\b")
SHINGLE = 5
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


def tokens(text):
    """The dup auditor's tokeniser, plus one normalisation it does not need: a curly
    apostrophe is folded to a straight one, so "Grey’s" and "Grey's" are one token."""
    return TOKEN.findall(text.replace("’", "'").lower())


def picked_h1(board):
    """The H1 the page will actually render: the breeder's pick, else the recommendation."""
    h1 = board["h1"]
    i = h1["recommended"] if h1.get("pick") is None else h1["pick"]
    return h1["variants"][i]


def all_headings(board):
    """(level, text) in render order: the picked H1, then each H2 and its tree, depth-first."""
    out = [(1, picked_h1(board))]

    def walk(nodes):
        for n in nodes:
            out.append((n["level"], n["heading"]))
            walk(n.get("children", []))
    for s in board["sections"]:
        out.append((2, s["heading"]))
        walk(s["tree"])
    return out


class _Headings(DUP.Text):
    """The dup gate's chrome-skipping walker, narrowed to the text of h1-h6.

    Inheriting it is the point: a heading is collected only where
    `dup_content_audit.py --headers` would see it, so a nav link, a read-card title or a
    footer heading never enters the corpus the pre-check compares a new page against.
    Two copies of that rule would drift, and the drifted one would cry wolf."""

    def __init__(self):
        super().__init__()
        self.headings = []
        self._buf = None

    def _visible(self):
        return bool(self.stack) and not self.stack[-1][1]

    def handle_starttag(self, tag, attrs):
        super().handle_starttag(tag, attrs)
        if self._buf is None and tag in HEADING_TAGS and self._visible():
            self._buf = []

    def handle_endtag(self, tag):
        if self._buf is not None and tag in HEADING_TAGS:
            text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
            if text:
                self.headings.append(text)
            self._buf = None
        super().handle_endtag(tag)

    def handle_data(self, data):
        super().handle_data(data)
        if self._buf is not None and self._visible():
            self._buf.append(data)


def page_headings(path):
    """Every visible h1-h6 on one built page, tag-stripped, unescaped, collapsed."""
    p = _Headings()
    p.feed(pathlib.Path(path).read_text(encoding="utf-8", errors="ignore"))
    p.close()
    return p.headings


def live_headings(dist=DIST):
    """{page: [heading text, ...]} from every built page. Empty when dist/ is absent."""
    out = {}
    for page in sorted(pathlib.Path(dist).glob("**/index.html")):
        rel = page.parent.relative_to(dist).as_posix()
        out["/" if rel == "." else "/" + rel + "/"] = page_headings(page)
    return out


def own_live_key(board):
    """The key this board's own page holds in live_headings(). The homepage is "/", not
    "/index/" — excluding the wrong key would let the homepage collide with itself and
    fail its own gate on every rebuild."""
    meta = board["meta"]
    if meta["page_type"] == "home" or meta["slug"] == "index":
        return "/"
    return "/" + meta["slug"] + "/"


def header_precheck(proposed, live, exclude_page=None):
    """Every proposed heading that collides with a live one: exact, template (species
    swapped) or 5-token shingle. `live` is {page: [heading, ...]}. `exclude_page` drops
    the page being rebuilt, which would otherwise collide with its own live headings —
    the same convention as owned_components() and spent_h6_prefixes()."""
    exact, templ, shingles = {}, {}, {}
    for page, hs in live.items():
        if page == exclude_page:
            continue
        for h in hs:
            t = " ".join(tokens(h))
            if not t:
                continue
            exact.setdefault(t, page)
            templ.setdefault(SPECIES.sub("{species}", t), page)
            ws = tokens(h)
            for i in range(len(ws) - SHINGLE + 1):
                shingles.setdefault(" ".join(ws[i:i + SHINGLE]), (page, h))
    hits = []
    for h in proposed:
        ws = tokens(h)
        t = " ".join(ws)
        if t in exact:
            hits.append({"heading": h, "kind": "exact", "page": exact[t], "with": h}); continue
        tt = SPECIES.sub("{species}", t)
        if tt in templ:
            hits.append({"heading": h, "kind": "template", "page": templ[tt], "with": tt}); continue
        for i in range(len(ws) - SHINGLE + 1):
            key = " ".join(ws[i:i + SHINGLE])
            if key in shingles:
                page, with_ = shingles[key]
                hits.append({"heading": h, "kind": "shingle", "page": page, "with": with_}); break
    return hits


def authorization_check(board, ont):
    by_id = {e["id"]: e for e in ont["entities"]}
    used = []
    for s in board["sections"]:
        for eid in s["entities"]:
            if eid not in used:
                used.append(eid)
    return {
        "blocked": [e for e in used if e in by_id and by_id[e]["authorization"] == "BLOCKED"],
        "proposed": [e for e in used if e in by_id and by_id[e]["authorization"] == "PROPOSED"],
        "unknown": [e for e in used if e not in by_id],
    }


def distribution(board):
    rows, totals = [], {"primary": 0, "lsi": 0, "longtail": 0, "brand": 0, "geo": 0, "words_min": 0, "words_max": 0}
    for s in board["sections"]:
        row = {"section": s["id"], "heading": s["heading"]}
        for k in ("primary", "lsi", "longtail", "brand", "geo"):
            row[k] = len(s["keywords"][k]); totals[k] += row[k]
        row["words_min"], row["words_max"] = s["words"]["min"], s["words"]["max"]
        totals["words_min"] += row["words_min"]; totals["words_max"] += row["words_max"]
        rows.append(row)
    counts = {f"h{n}": 0 for n in range(1, 7)}
    for lvl, _ in all_headings(board):
        counts[f"h{lvl}"] += 1
    return {"rows": rows, "totals": totals, "h_counts": counts}


ADVISORY_MIN_H5H6 = {"home", "location"}          # rules/headings.md, 2026-09-09
GATE_STAGES = ("build", "release")
_WHITELIST_TOKENS = [t for t in (tokens(w) for w in HEADER_WHITELIST) if t]


def _whitelisted(heading):
    """True when a HEADER_WHITELIST phrase appears in the heading as a contiguous run of
    WHOLE tokens. Substring matching read the bird name "evie" out of "Review" and the
    bird name "amie" out of any "...amie..." run, clearing collisions the dup gate flags
    after the build — so the match is on tokens, not characters."""
    ws = tokens(heading)
    return any(ws[i:i + len(phrase)] == phrase
               for phrase in _WHITELIST_TOKENS
               for i in range(len(ws) - len(phrase) + 1))


def gate_findings(board, ont, ledger, live, stage="build"):
    """Every reason this record may not be built (or released). Pure: no printing."""
    if stage not in GATE_STAGES:
        raise BoardError(f"unknown gate stage {stage!r}: expected one of {', '.join(GATE_STAGES)}")
    f = []
    slug = board["meta"]["slug"]
    add = lambda check, sev, msg: f.append({"check": check, "sev": sev, "msg": msg})

    if not approval_matches(board):
        add("approval-hash", "FAIL", "no approval, or the record changed after it was approved — board it again")

    auth = authorization_check(board, ont)
    for e in auth["blocked"]:
        add("entity-blocked", "FAIL", f"{e} is BLOCKED (CLAUDE.md rule 2)")
    for e in auth["unknown"]:
        add("entity-unknown", "WARN", f"{e} is not in data/cag-ontology.json")
    for e in auth["proposed"]:
        add("entity-proposed", "WARN", f"{e} is PROPOSED — needs a source before it can be asserted")

    # The ledger's discipline is that COMBOS differ, not components: dial-1-clay is on
    # nine pages by design, so a per-component rule would fail every page on the site.
    # Four rules, narrowest first.
    owned = owned_components(ledger, exclude_slug=slug)
    t = board["tuple"]
    siblings = {p: s for p, s in ledger.get("pages", {}).items() if p != slug}
    tw = set(t.get("takeaway", []))
    triple = tuple(t.get(k) or "" for k in ("hero", "dial", "rail"))

    identical = [p for p, s in siblings.items()
                 if all((s.get(k) or "") == (t.get(k) or "") for k in TUPLE_ID_KEYS)
                 and set(s.get("takeaway", [])) == tw]
    for p in identical:
        add("ledger-tuple-identical", "FAIL",
            f"every tuple axis matches {p} — the combo is what has to differ")
    rest = {p: s for p, s in siblings.items() if p not in identical}

    if any(triple):
        trip = [p for p, s in rest.items() if tuple(s.get(k) or "" for k in ("hero", "dial", "rail")) == triple]
        if trip:
            add("ledger-triple-owned", "FAIL",
                f"hero+dial+rail {'+'.join(x or '—' for x in triple)} is the same signature as {', '.join(trip)}")
    if tw:
        sets = [p for p, s in rest.items() if set(s.get("takeaway", [])) == tw]
        if sets:
            add("ledger-takeaway-set-owned", "FAIL",
                f"takeaway set {{{', '.join(sorted(tw))}}} is the same set as {', '.join(sets)}")
    # The scarce shells: a bare base a sibling uses (bare or refreshed) must be refreshed
    # here too. A `base#delta` passes — unless it is a sibling's exact id, which owned_
    # components records under the full id.
    for key in ("hero", "toc", "faq"):
        v = t.get(key)
        if v and owned.get(v):
            add("ledger-shell-owned", "FAIL",
                f"tuple.{key}={v} is owned by {', '.join(owned[v])} — refresh it as {base_of(v)}#<delta>")
    spent = spent_h6_prefixes(ledger, exclude_slug=slug)
    for p in t.get("h6_prefixes", []):
        if p in spent:
            add("ledger-spent-prefix", "FAIL", f"H6 prefix {p!r} is spent by {', '.join(spent[p])}")

    if not live:
        add("header-precheck-examined-zero", "FAIL",
            "header pre-check examined 0 live pages — run npx astro build first")
    hits = [h for h in header_precheck([h for _, h in all_headings(board)], live,
                                       exclude_page=own_live_key(board))
            if not _whitelisted(h["heading"])]
    for h in hits:
        add("header-collision", "FAIL", f"{h['kind']}: {h['heading']!r} vs {h['page']} {h['with']!r}")

    counts = distribution(board)["h_counts"]
    if counts["h5"] < 5 or counts["h6"] < 5:
        sev = "WARN" if board["meta"]["page_type"] in ADVISORY_MIN_H5H6 else "FAIL"
        add("min-h5-h6", sev, f"H5 {counts['h5']} / H6 {counts['h6']} — floor is 5 each")

    picks = (board.get("approval") or {}).get("picks", {})
    for s in board["sections"]:
        if s["shape"] != "standard" and not (s["options"]["pick"] or picks.get(s["id"])):
            add("signature-no-pick", "FAIL", f"section {s['id']} ({s['shape']}) has no component pick")

    if stage == "release":
        for a in board["assets"]:
            if a["required"] and a["status"] != "baked":
                add("asset-required-missing", "FAIL", f"required slot {a['slot']} ({a['kind']} {a['w']}x{a['h']}) is {a['status']}")
    return f

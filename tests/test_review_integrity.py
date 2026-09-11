"""Review integrity on the BUILT site.

Every confirmed review in data/reviews.json is listed exactly once on
/african-grey-reviews/, and no review on any non-location page is duplicated
(D-a), sits beside the wrong buyer (D-b), carries an edited text (D-c), shows
the wrong town (D-d) or the wrong photo (D-e). A blockquote or schema Review
that is not in the ledger fails the build, so a new review card cannot ship
unlisted.

Measured on dist/, never src/ — the gates measure what ships. Location pages
are excluded until they are rebuilt.
"""
from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
LEDGER = json.loads((ROOT / "data" / "reviews.json").read_text(encoding="utf-8"))
REVIEWS = LEDGER["reviews"]
PENDING = LEDGER.get("pending", [])
PENDING_NAMES = {p["name"] for p in PENDING}
PEOPLE = {r["name"]: r for r in REVIEWS + PENDING}
REVIEW_PAGE = "african-grey-reviews"
KEY = 60
LOCATION_PREFIX = re.compile(r"^(african-grey-parrot-for-sale-|buy-intelligent-african-grey-for-sale-)")

# Blockquotes that are our own pull-quotes or a scam victim's words — not C.A.Gs buyer reviews.
NOT_REVIEWS = (
    "A Congo Grey doesn't just mimic words",
    "We hand you the paperwork before the wire",
    "Every macaw-curious buyer who does the math",
    "Fit the bird to the home",
    "Match the bird to the household",
    "We wrote this comparison the way we answer the phone",
    "I sent $400 and never heard from them again",
)
# The comparison hub quotes a verbatim fragment plus our own summary. Allowed only beside its owner.
SUMMARY_FRAGMENTS = {"the experience was flawless": "q3", "made the process stress-free": "q2"}
SUMMARY_PAGE = "african-grey-comparison"

pytestmark = pytest.mark.skipif(not DIST.exists(), reason="dist/ not built — gates measure dist, never source")


def norm(s: str) -> str:
    s = (s.replace("’", "'").replace("‘", "'")
          .replace("“", '"').replace("”", '"').replace("\xa0", " "))
    return re.sub(r"\s+", " ", s).strip()


def key(review: dict) -> str:
    return norm(review["quote"])[:KEY]


def city(location: str) -> str:
    return location.split(",")[0].strip()


def stem(src: str) -> str:
    """Photo identity without the width suffix: foo-review-112.webp -> foo-review.webp."""
    return re.sub(r"-\d{2,4}(?=\.\w+$)", "", Path(src.split("?")[0]).name)


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes: list[str] = []
        self.node_anc: list[tuple[int, ...]] = []
        self.quotes: list[str] = []
        self.imgs: list[tuple[str, str]] = []
        self.ld: list = []
        self.ld_errors: list[str] = []
        self._skip = 0
        self._bq = 0
        self._buf: list[str] = []
        self._in_ld = False
        self._ldbuf: list[str] = []
        self._stack: list[tuple[str, int]] = []
        self._next = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld, self._ldbuf = True, []
            return
        if tag in ("script", "style"):
            self._skip += 1
        if tag == "blockquote":
            self._bq += 1
        if tag == "img":
            self.imgs.append((a.get("alt") or "", a.get("src") or ""))
        if tag not in VOID:
            self._next += 1
            self._stack.append((tag, self._next))

    def handle_endtag(self, tag):
        if tag == "script" and self._in_ld:
            self._in_ld = False
            try:
                self.ld.append(json.loads("".join(self._ldbuf)))
            except json.JSONDecodeError as e:
                self.ld_errors.append(str(e))
            return
        for k in range(len(self._stack) - 1, -1, -1):
            if self._stack[k][0] == tag:
                del self._stack[k:]
                break
        if tag in ("script", "style") and self._skip:
            self._skip -= 1
        if tag == "blockquote" and self._bq:
            self._bq -= 1
            if not self._bq:
                self.quotes.append(norm(" ".join(self._buf)))
                self._buf = []

    def handle_data(self, data):
        if self._in_ld:
            self._ldbuf.append(data)
            return
        if self._skip or not data.strip():
            return
        self.nodes.append(norm(data))
        self.node_anc.append(tuple(i for _, i in self._stack))
        if self._bq:
            self._buf.append(data)


def ld_reviews(ld) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []

    def walk(o):
        if isinstance(o, list):
            for x in o:
                walk(x)
        elif isinstance(o, dict):
            if o.get("@type") == "Review":
                a = o.get("author")
                out.append((a.get("name") if isinstance(a, dict) else a, norm(o.get("reviewBody") or "")))
            for v in o.values():
                walk(v)

    walk(ld)
    return out


def location_slugs() -> set[str]:
    data = json.loads((ROOT / "data" / "locations.json").read_text(encoding="utf-8"))
    return {e["slug"] for k in ("live_states", "cities") for e in data.get(k, [])
            if isinstance(e, dict) and e.get("slug")}


def redirected_slugs() -> set[str]:
    """Sources of 301/308s in the built _redirects — Cloudflare serves the redirect, never the page."""
    f = DIST / "_redirects"
    if not f.exists():
        return set()
    out = set()
    for line in f.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[2] in ("301", "308") and parts[0].startswith("/") and "*" not in parts[0]:
            out.add(parts[0].strip("/"))
    return out


def load_pages() -> dict[str, Page]:
    skip = location_slugs()
    redirected = redirected_slugs()
    pages: dict[str, Page] = {}
    for p in sorted(DIST.rglob("index.html")):
        rel = p.parent.relative_to(DIST).as_posix()
        slug = "index" if rel == "." else rel
        top = slug.split("/")[0]
        if top in skip or LOCATION_PREFIX.match(top) or slug in redirected:
            continue
        pg = Page()
        pg.feed(p.read_text(encoding="utf-8", errors="ignore"))
        pg.text = "\n".join(pg.nodes)
        pg.reviews = ld_reviews(pg.ld)
        pages[slug] = pg
    return pages


PAGES = load_pages() if DIST.exists() else {}


def test_examined_counts():
    hits = [s for s, pg in PAGES.items() if any(key(r) in pg.text for r in REVIEWS)]
    print(f"\nexamined {len(PAGES)} non-location pages; {len(hits)} carry a ledger review")
    assert len(PAGES) >= 60, "examined too few pages — check the dist walk"
    assert len(hits) >= 15, "too few review-bearing pages — ledger incomplete or extractor broken"


def test_every_json_ld_block_parses():
    bad = [f"{slug}: {e}" for slug, pg in PAGES.items() for e in pg.ld_errors]
    assert not bad, "JSON-LD blocks that do not parse (their Reviews would be invisible):\n" + "\n".join(bad)


def test_review_page_shows_every_confirmed_review_exactly_once():
    pg = PAGES[REVIEW_PAGE]
    bad = {r["name"]: pg.text.count(key(r)) for r in REVIEWS if pg.text.count(key(r)) != 1}
    assert not bad, f"review page shows these confirmed reviews != 1 time: {bad}"


def test_review_page_schema_has_one_review_per_ledger_entry():
    names = sorted(n for n, _ in PAGES[REVIEW_PAGE].reviews)
    assert names == sorted(r["name"] for r in REVIEWS)


def test_no_review_repeats_within_a_page():  # D-a
    bad = []
    for slug, pg in PAGES.items():
        for r in REVIEWS + PENDING:
            c = pg.text.count(key(r))
            if c > 1:
                bad.append(f"{slug}: {r['name']}'s review shown {c}x")
        names = [n for n, _ in pg.reviews]
        bad += [f"{slug}: schema Review for {n} x{names.count(n)}" for n in set(names) if names.count(n) > 1]
    assert not bad, "\n".join(bad)


def test_every_schema_review_is_ledgered_and_verbatim():  # discovery + D-c
    bad = []
    for slug, pg in PAGES.items():
        for name, body in pg.reviews:
            ref = PEOPLE.get(name)
            if ref is None:
                bad.append(f"{slug}: schema Review by {name!r} is not in data/reviews.json")
            elif name not in PENDING_NAMES and body != norm(ref["quote"]):
                bad.append(f"{slug}: {name}'s schema reviewBody differs from the ledger (edited or swapped)")
    assert not bad, "\n".join(bad)


def test_every_shown_review_is_verbatim():  # D-c, visible text
    bad = []
    for slug, pg in PAGES.items():
        flat = " ".join(pg.nodes)
        for r in REVIEWS:
            if key(r) in pg.text and norm(r["quote"]) not in flat:
                bad.append(f"{slug}: {r['name']}'s review opens verbatim but the rest is edited")
    assert not bad, "\n".join(bad)


def test_every_review_blockquote_is_ledgered():  # discovery
    stray = []
    for slug, pg in PAGES.items():
        for q in pg.quotes:
            if len(q) < 40 or any(n in q for n in NOT_REVIEWS):
                continue
            if any(key(r) in q for r in REVIEWS + PENDING):
                continue
            if slug == SUMMARY_PAGE and any(f in q for f in SUMMARY_FRAGMENTS):
                continue
            stray.append(f"{slug}: {q[:90]!r}")
    assert not stray, "blockquotes not in data/reviews.json:\n" + "\n".join(stray)


RATING_ONLY = re.compile(r"★|Rated \d out of 5")


def is_rating(node: str) -> bool:
    """A pure rating run ('★★★★★', '★', 'Rated 5 out of 5'), not a caption that also names a buyer."""
    return "★" in node and not RATING_ONLY.sub("", node).strip()


def card_quotes(pg: Page):
    """Review cards with no <blockquote>. A rating run opens a card: its quote is the first
    quote-length node after the WHOLE run. 'Verified C.A.Gs buyer' closes a card: its quote is
    the last quote-length node before it. Yields (quote, window) where the window is only that
    card's own nodes, so a neighbour's ledger key can never vouch for it. (In a Testimonials grid —
    stars, headline, quote, name — the 3 nodes before the stars are the PREVIOUS card's name, so
    names in the window are context, never attribution.)
    Each quote node is judged once."""
    nodes, seen = pg.nodes, set()
    for i, node in enumerate(nodes):
        if is_rating(node) and not (i and is_rating(nodes[i - 1])):
            j = i
            while j < len(nodes) and is_rating(nodes[j]):
                j += 1
            q = next((k for k in range(j, min(j + 4, len(nodes))) if len(nodes[k]) >= 60), None)
            lo = max(0, i - 3)  # bird pages: this card's name/town; grids: the previous card's name
        elif node.startswith("Verified C.A.Gs buyer"):
            q = next((k for k in range(i - 1, max(-1, i - 4), -1) if len(nodes[k]) >= 60), None)
            lo = q
        else:
            continue
        if q is None or q in seen:
            continue
        seen.add(q)
        hi = q if lo != q else i  # rating card: name..quote; verified card: quote..Verified
        yield nodes[q], " ".join(nodes[lo: hi + 1])


def test_every_star_card_is_ledgered():  # discovery for <p>-style cards
    keys = [key(r) for r in REVIEWS + PENDING]
    stray, cards = [], 0
    for slug, pg in PAGES.items():
        for quote, window in card_quotes(pg):
            cards += 1
            # Judged on the quote alone. Attribution (D-b) for these cards is checked structurally in
            # test_every_review_sits_in_its_own_buyers_card.
            if any(k in quote for k in keys) or any(n in quote for n in NOT_REVIEWS):
                continue
            # Comparison-hub cards: a verbatim fragment (< 60 chars, so never the judged node) plus our
            # own third-person summary. The fragment sits in the same card, so look for it in the window.
            if slug == SUMMARY_PAGE and any(f in window for f in SUMMARY_FRAGMENTS):
                continue
            stray.append(f"{slug}: {quote[:110]!r}")
    print(f"\nstar/verified review cards examined: {cards}")
    assert cards >= 20, "found almost no review cards — card detection is broken"
    assert not stray, "review cards whose text is not in data/reviews.json:\n" + "\n".join(stray)


def test_quotes_sit_beside_their_own_buyer():  # D-b
    owners = {key(r): r["name"] for r in REVIEWS + PENDING}
    owners.update({f: next(r["name"] for r in REVIEWS if r["id"] == i) for f, i in SUMMARY_FRAGMENTS.items()})
    checked = 0
    wrong = []
    for slug, pg in PAGES.items():
        for q in pg.quotes:
            for k, owner in owners.items():
                if k in q:
                    checked += 1
                    others = [n for n in PEOPLE if n != owner and n in q]
                    if others:
                        wrong.append(f"{slug}: {owner}'s words sit beside {others}")
    assert checked >= 10, f"D-b examined only {checked} ledger quotes — extractor broken"
    assert not wrong, "\n".join(wrong)


def _spans(pg: Page):
    """First and last text-node index inside each element (text nodes of an element are contiguous)."""
    if not hasattr(pg, "_span_cache"):
        first, last = {}, {}
        for j, anc in enumerate(pg.node_anc):
            for a in anc:
                first.setdefault(a, j)
                last[a] = j
        pg._span_cache = (first, last)
    return pg._span_cache


def card_of(pg: Page, idx: int):
    """The review's own card: the nearest ancestor element of text node `idx` that also contains a
    ledger buyer's name. Works whether the name comes before the quote (bird pages) or after it
    (Testimonials grid) because it follows the markup, not node distance."""
    first, last = _spans(pg)
    for a in reversed(pg.node_anc[idx]):
        inside = range(first[a], last[a] + 1)
        if any(n in pg.nodes[j] for j in inside for n in PEOPLE):
            return inside
    return None


def test_node_ancestry_is_recorded():
    for slug, pg in PAGES.items():
        assert len(pg.node_anc) == len(pg.nodes), f"{slug}: ancestry out of step with text nodes"


def test_every_review_sits_in_its_own_buyers_card():  # D-b for every card layout
    owners = {key(r): r["name"] for r in REVIEWS + PENDING}
    attributed, wrong = 0, []
    multi, nocard = 0, 0
    for slug, pg in PAGES.items():
        for idx, node in enumerate(pg.nodes):
            owner = next((o for k, o in owners.items() if k in node), None)
            if owner is None:
                continue
            card = card_of(pg, idx)
            if card is None:
                nocard += 1
                continue
            text = " ".join(pg.nodes[j] for j in card)
            if sum(k in text for k in owners) > 1:
                multi += 1
                continue  # this ancestor holds several reviews: the quote's own card names nobody
            attributed += 1
            names = [n for n in PEOPLE if n in text]
            if owner not in names or len(names) > 1:
                wrong.append(f"{slug}: {owner}'s words sit in a card naming {names}")
    print(f"\nreview cards attributed by structure: {attributed} "
          f"(skipped: {multi} shared-ancestor, {nocard} no named card)")
    assert attributed >= 30, f"only {attributed} review cards attributed — card markup changed?"
    assert not wrong, "review cards credited to the wrong buyer:\n" + "\n".join(wrong)


LOC_RE = re.compile(r"^[\s,·|—–-]*([A-Z][A-Za-z.]+(?: [A-Z][A-Za-z.]+)*),\s*([A-Z]{2}\b|[A-Z][a-z]+(?: [A-Z][a-z]+)?)")


def test_every_buyer_is_shown_with_their_own_town():  # D-d
    matched = 0
    wrong = []
    for slug, pg in PAGES.items():
        for i, node in enumerate(pg.nodes):
            for name, ref in PEOPLE.items():
                at = node.find(name)
                if at < 0:
                    continue
                after = node[at + len(name):]
                if not after.strip(" ,·|—–-") and i + 1 < len(pg.nodes):
                    after = pg.nodes[i + 1]
                m = LOC_RE.match(after)
                matched += bool(m)
                if m and m.group(1) != city(ref["location"]):
                    wrong.append(f"{slug}: {name} shown in {m.group(1)}, ledger says {ref['location']}")
    assert matched >= 20, f"D-d matched only {matched} towns — LOC_RE or markup changed"
    assert not wrong, "\n".join(wrong)


def test_no_buyer_wears_another_buyers_photo():  # D-e
    photo_owner = {stem(r["avatar"]): r["name"] for r in REVIEWS + PENDING if r.get("avatar")}
    resolved = 0
    wrong = []
    for slug, pg in PAGES.items():
        for alt, src in pg.imgs:
            owner = photo_owner.get(stem(src))
            resolved += bool(owner)
            shown = next((n for n in PEOPLE if alt.startswith(n)), None)
            if owner and shown and shown != owner:
                wrong.append(f"{slug}: {owner}'s photo is labelled {shown}")
    assert resolved >= 15, f"D-e resolved only {resolved} ledger photos — stem() or markup changed"
    assert not wrong, "\n".join(wrong)


def test_ledger_photos_are_unique():  # D-e
    avatars = [stem(r["avatar"]) for r in REVIEWS + PENDING if r.get("avatar")]
    assert len(avatars) == len(set(avatars)), "one photo is assigned to two buyers in data/reviews.json"


def test_no_review_awaits_a_ruling():
    assert PENDING == []

"""Backing test for rules/images.md `read-card-thumb-is-target-hero`.

Two things are asserted, and the first matters more than the second.

1. The AUDITOR ITSELF is not blind. Its first version used `(.*?)</div>` to grab the
   read-cards block, which truncated at the first nested <div> — it examined 2 of the 11
   pages that have read-cards and reported "4 checked" as though that were the site. A
   checker that silently examines a fraction of its corpus is the failure mode this repo
   has paid for repeatedly (reference_gate_examined_zero_pages). So the parser is pinned
   against a fixture containing a nested div, and against the real built corpus.

2. Pages already migrated to the rule stay migrated.
"""
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

DIST = ROOT / "dist"
MIGRATED = [
    "african-grey-breeding-pair-for-sale",
    "african-grey-parrot-bird-eggs-for-sale-usa",
    "african-greys-for-sale-with-health-guarantee",
    "timneh-african-grey-for-sale",
    "congo-african-grey-for-sale",
    "dna-tested-african-grey-for-sale",
    "hand-raised-african-grey-parrot-for-sale",
    "baby-african-grey-parrot-for-sale",
    "congo-african-grey-parrot-pair-for-sale",
    "african-grey-parrot-adoption-cost",
]

pytestmark = pytest.mark.skipif(
    not DIST.exists(), reason="dist/ not built — gates measure dist, never source"
)


def _mod():
    import importlib

    return importlib.import_module("bake_read_card_thumbs")


def test_parser_survives_a_nested_div(tmp_path, monkeypatch):
    """The bug that made the auditor examine 2 pages out of 11."""
    m = _mod()
    page = tmp_path / "nested" / "index.html"
    page.parent.mkdir(parents=True)
    page.write_text(
        '<section><div class="read-cards">'
        '<a href="/one/"><div class="wrap"><img src="/a-320.webp" alt="a"></div><span>One</span></a>'
        '<a href="/two/"><div class="wrap"><img src="/b-320.webp" alt="b"></div><span>Two</span></a>'
        "</div></section>"
    )
    monkeypatch.setattr(m, "DIST", tmp_path)
    cards = m.read_cards("nested")
    assert len(cards) == 2, f"nested <div> truncated the block again: {cards}"
    assert [c[0] for c in cards] == ["/one/", "/two/"]


def test_anchors_without_an_image_are_not_cards(tmp_path, monkeypatch):
    """A text-only link inside the block is not a thumbnail and must not be judged."""
    m = _mod()
    page = tmp_path / "textlink" / "index.html"
    page.parent.mkdir(parents=True)
    page.write_text(
        '<section><div class="read-cards">'
        '<a href="/one/"><img src="/a-320.webp" alt="a"><span>One</span></a>'
        '<a href="/plain/">just a link</a>'
        "</div></section>"
    )
    monkeypatch.setattr(m, "DIST", tmp_path)
    assert len(m.read_cards("textlink")) == 1


def test_auditor_sees_every_page_that_has_read_cards():
    """examined must match the corpus, not a subset of it."""
    m = _mod()
    with_cards = [
        p.parent.name
        for p in sorted(DIST.glob("*/index.html"))
        if 'class="read-cards"' in p.read_text(errors="ignore")
    ]
    if not with_cards:
        pytest.skip("no read-cards in this build")
    seen = [s for s in with_cards if m.read_cards(s)]
    assert seen == with_cards, (
        "the auditor found cards on only "
        f"{len(seen)}/{len(with_cards)} pages that have a read-cards block: "
        f"missed {sorted(set(with_cards) - set(seen))}"
    )


@pytest.mark.parametrize("slug", MIGRATED)
def test_migrated_pages_use_their_targets_hero(slug):
    m = _mod()
    cards = m.read_cards(slug)
    assert cards, f"{slug} has no read-cards — did the section move?"
    for href, src in cards:
        target = href.strip("/")
        hero = m.hero_and_alt(target)[0] if hasattr(m, "hero_and_alt") else m.hero_of(target)
        assert hero, f"{slug}: no hero resolved for {href}"
        stem = pathlib.Path(src).stem.replace("-320", "").replace("-760", "")
        # Nested slugs (blog/<post>) flatten to `-` in the filename; flatten both sides.
        flat = target.replace("/", "-").replace("-", "")
        assert flat in stem.replace("-", "") or src == hero, (
            f"{slug}: card -> {href} shows {src}, which is not cut from that page's "
            f"hero {hero}"
        )


def test_audit_runs_and_reports_a_count():
    """A gate that prints no examined count cannot be believed."""
    r = subprocess.run(
        [sys.executable, "scripts/bake_read_card_thumbs.py", "--audit"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert "read-card thumbnails checked" in r.stdout, r.stdout[-400:]

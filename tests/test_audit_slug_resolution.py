# tests/test_audit_slug_resolution.py
#
# Harness fix 2026-09-10: three audit scripts resolved the homepage slug
# ("index") wrong — page_hardening_scan.py matched EVERY page (43-minute
# run, killed), aeo_audit.py matched NO pages, and dup_content_audit.py
# keyed the homepage "dist" (a dead `or "home"` fallback). All three now
# use the same convention as final_page_audit.py / evidence_audit.py:
# `index` (and "" / "/") means EXACTLY dist/index.html; any other slug
# means EXACTLY dist/<slug>/index.html (nested slugs keep their full path,
# e.g. available/roys).
import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import page_hardening_scan as hardening
import aeo_audit as aeo
import dup_content_audit as dup


ALL_PAGES = [
    "dist/index.html",
    "dist/congo-african-grey-for-sale/index.html",
    "dist/timneh-african-grey-for-sale/index.html",
    "dist/available/roys/index.html",
]


# ── page_hardening_scan.select_pages ───────────────────────────────────────

def test_hardening_index_matches_only_homepage():
    assert hardening.select_pages(ALL_PAGES, ["index"]) == ["dist/index.html"]


def test_hardening_normal_slug_matches_only_that_page():
    assert hardening.select_pages(ALL_PAGES, ["congo-african-grey-for-sale"]) == [
        "dist/congo-african-grey-for-sale/index.html"
    ]


def test_hardening_nested_slug_matches_only_that_page():
    assert hardening.select_pages(ALL_PAGES, ["available/roys"]) == [
        "dist/available/roys/index.html"
    ]


def test_hardening_no_slugs_returns_all_pages():
    assert hardening.select_pages(ALL_PAGES, []) == ALL_PAGES


# ── aeo_audit.select_pages ─────────────────────────────────────────────────

def test_aeo_index_matches_only_homepage():
    assert aeo.select_pages(ALL_PAGES, ["index"]) == ["dist/index.html"]


def test_aeo_normal_slug_matches_only_that_page():
    assert aeo.select_pages(ALL_PAGES, ["congo-african-grey-for-sale"]) == [
        "dist/congo-african-grey-for-sale/index.html"
    ]


def test_aeo_nested_slug_matches_only_that_page():
    assert aeo.select_pages(ALL_PAGES, ["available/roys"]) == [
        "dist/available/roys/index.html"
    ]


# ── dup_content_audit.page_key ─────────────────────────────────────────────

def test_dup_key_of_homepage_is_index():
    assert dup.page_key(pathlib.Path("dist/index.html"), pathlib.Path("dist")) == "index"


def test_dup_key_of_normal_slug_is_the_slug():
    assert dup.page_key(
        pathlib.Path("dist/foo/index.html"), pathlib.Path("dist")
    ) == "foo"


def test_dup_key_of_nested_slug_keeps_full_path():
    assert dup.page_key(
        pathlib.Path("dist/available/roys/index.html"), pathlib.Path("dist")
    ) == "available/roys"

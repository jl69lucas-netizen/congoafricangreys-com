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


# ── page_hardening_scan.imports_of / src_files (2026-09-10) ───────────────
# Commit 40986a66 made a scoped src_files() run always glob in every shared
# component/layout/style, which attributes a shared component's findings to
# pages that never import it. src_files() must instead resolve each page's
# OWN imports (one level, plus one more level for cag-library components
# that import siblings) and always add BaseLayout.astro + global.css.

def test_imports_of_homepage_finds_its_own_components_only():
    found = hardening.imports_of("src/pages/index.astro")
    assert "src/components/cag-inquiry-form.astro" in found
    assert "src/components/cag-library/HeroV3.astro" in found
    assert "src/components/cag-inquiry-compact.astro" not in found


def test_src_files_index_scopes_to_its_own_imports():
    files = hardening.src_files(["index"])
    assert "src/pages/index.astro" in files
    assert "src/layouts/BaseLayout.astro" in files
    assert "src/styles/global.css" in files
    assert "src/components/cag-inquiry-form.astro" in files
    assert "src/components/cag-inquiry-compact.astro" not in files


def test_src_files_congo_scopes_to_its_own_imports_and_excludes_index():
    files = hardening.src_files(["congo-african-grey-for-sale"])
    assert "src/pages/congo-african-grey-for-sale/index.astro" in files
    assert "src/components/Breadcrumb.astro" in files
    assert "src/pages/index.astro" not in files


def test_src_files_no_slugs_returns_full_glob():
    files = hardening.src_files([])
    assert len(files) > 100

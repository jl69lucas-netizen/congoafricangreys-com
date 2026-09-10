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
#
# These run against tests/fixtures/hardening_scan/ (not the live repo) so
# they don't break on unrelated component swaps — imports_of()/src_files()
# both accept an optional `root` for exactly this. Fixture tree:
#   src/pages/index.astro        -> imports FormA + cag-library/Hero
#   src/pages/alpha/index.astro  -> imports FormB only
#   src/components/cag-library/Hero.astro -> imports ../../lib/util
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "hardening_scan"


def test_imports_of_homepage_finds_its_own_components_only():
    found = hardening.imports_of("src/pages/index.astro", root=FIXTURE_ROOT)
    assert "src/components/FormA.astro" in found
    assert "src/components/cag-library/Hero.astro" in found
    assert "src/components/FormB.astro" not in found


def test_src_files_index_scopes_to_its_own_imports():
    files = hardening.src_files(["index"], root=FIXTURE_ROOT)
    assert "src/pages/index.astro" in files
    assert "src/layouts/BaseLayout.astro" in files
    assert "src/styles/global.css" in files
    assert "src/components/FormA.astro" in files
    assert "src/components/cag-library/Hero.astro" in files
    assert "src/lib/util.ts" in files
    assert "src/components/FormB.astro" not in files


def test_src_files_alpha_scopes_to_its_own_imports_and_excludes_index():
    files = hardening.src_files(["alpha"], root=FIXTURE_ROOT)
    assert "src/pages/alpha/index.astro" in files
    assert "src/components/FormB.astro" in files
    assert "src/components/FormA.astro" not in files
    assert "src/pages/index.astro" not in files


def test_src_files_no_slugs_returns_full_glob():
    # The no-slugs sweep globs src/components/*.astro one level deep (not
    # recursive), so nested src/components/cag-library/Hero.astro and
    # src/lib/util.ts are out of scope here — same as the real repo sweep.
    files = hardening.src_files([], root=FIXTURE_ROOT)
    expected = {
        "src/pages/index.astro",
        "src/pages/alpha/index.astro",
        "src/components/FormA.astro",
        "src/components/FormB.astro",
        "src/layouts/BaseLayout.astro",
        "src/styles/global.css",
    }
    assert set(files) == expected

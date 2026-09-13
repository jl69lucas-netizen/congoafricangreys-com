"""perf_audit.py judging logic — the parts that decide PASS/FAIL, tested without Lighthouse.

2026-09-13: the gate floored Performance at 95, judged four categories (no Agentic Browsing),
and could only audit dist/, so an edge-injected 181 KB gtag (Cloudflare Google tag gateway)
and a Linux-only font-swap CLS both shipped while it said PASS.
"""
import importlib.util
import pathlib

spec = importlib.util.spec_from_file_location(
    "perf_audit", pathlib.Path(__file__).resolve().parents[1] / "scripts/perf_audit.py")
pa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pa)

FULL = {"performance": 1, "accessibility": 1, "best-practices": 1, "seo": 1, "agentic-browsing": 1}


def rep(scores):
    return {"categories": {k: {"score": v} for k, v in scores.items()}, "audits": {}}


def test_five_categories_are_judged():
    assert set(pa.THRESHOLDS) == set(FULL)


def test_99_performance_fails_the_100_floor():
    assert pa.judge([rep(dict(FULL, performance=0.99))]) == ["performance"]


def test_995_is_what_psi_displays_as_100_and_passes():
    assert pa.judge([rep(dict(FULL, performance=0.995))]) == []


def test_missing_category_fails_rather_than_passing_on_nothing():
    scores = dict(FULL)
    scores.pop("agentic-browsing")
    assert pa.judge([rep(scores)]) == ["agentic-browsing"]


def test_null_score_counts_as_zero():
    assert pa.judge([rep(dict(FULL, seo=None))]) == ["seo"]


def test_median_of_runs_is_judged_not_the_worst():
    runs = [rep(dict(FULL, performance=p)) for p in (0.90, 1, 1)]
    assert pa.judge(runs) == []


def _net(*items):
    return {"audits": {"network-requests": {"details": {"items": list(items)}}}}


def test_edge_injected_resources_are_those_the_built_html_never_references():
    report = _net(
        {"url": "http://127.0.0.1:4399/_astro/a.js", "resourceType": "Script"},
        {"url": "https://congoafricangreys.com/70de/", "resourceType": "Script"},
        {"url": "https://congoafricangreys.com/cf-fonts/v/x/latin/wght/normal.woff2", "resourceType": "Font"},
        {"url": "https://congoafricangreys.com/images/hero.webp", "resourceType": "Image"},
    )
    dist_html = '<script src="/_astro/a.js"></script><img src="/images/hero.webp">'
    assert pa.edge_injected(report, dist_html) == [
        "https://congoafricangreys.com/70de/",
        "https://congoafricangreys.com/cf-fonts/v/x/latin/wght/normal.woff2",
    ]


def test_scripts_our_own_code_loads_by_url_are_not_edge_injected():
    # BaseLayout's deferred GA loader writes this URL into an inline script.
    report = _net({"url": "https://www.googletagmanager.com/gtag/js?id=G-MEWJ9GVC4T", "resourceType": "Script"})
    dist_html = "s.src='https://www.googletagmanager.com/gtag/js?id=G-MEWJ9GVC4T'"
    assert pa.edge_injected(report, dist_html) == []


def test_edge_scripts_are_blocking_edge_fonts_are_not():
    urls = ["https://congoafricangreys.com/70de/", "https://congoafricangreys.com/cf-fonts/a.woff2"]
    report = _net({"url": urls[0], "resourceType": "Script"}, {"url": urls[1], "resourceType": "Font"})
    assert pa.edge_blocking(report, urls) == [urls[0]]


def test_psi_request_asks_for_all_five_categories_and_the_strategy():
    u = pa.psi_url("https://congoafricangreys.com/x/", "mobile", key="K")
    for c in pa.CATEGORIES:
        assert f"category={c}" in u
    assert "strategy=mobile" in u and "key=K" in u


def test_psi_request_without_key_sends_no_key_param():
    assert "key=" not in pa.psi_url("https://congoafricangreys.com/x/", "desktop")

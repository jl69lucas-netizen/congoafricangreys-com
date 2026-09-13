#!/usr/bin/env python3
"""perf_audit.py — the PageSpeed gate: five categories, 100 each, mobile and desktop.

  python3 scripts/perf_audit.py <slug>                    # desktop, against dist/
  python3 scripts/perf_audit.py <slug> --mobile --runs 5  # CLS is bimodal on this site
  python3 scripts/perf_audit.py <slug> --live --mobile    # the deployed URL, edge features included
  python3 scripts/perf_audit.py <slug> --psi --mobile     # Google's own servers: THE record that counts

`--psi` calls the PageSpeed Insights API (set PSI_API_KEY for more than the keyless daily
quota). It is authoritative because a local Mac cannot stand in for PSI: this machine's CPU
benchmark (~490) makes mobile Performance read far lower, and its fonts and cache timing
made CLS read 0 where PSI measured 0.266. Use local runs to find defects, PSI to judge.

Judges what PageSpeed Insights shows: Performance, Accessibility, Best Practices, SEO and
Agentic Browsing (Lighthouse 13.4.1, `agentic-browsing-config.js`). Every floor is 0.995,
the score PSI displays as 100. The median of the runs is judged.

WHY `--live` EXISTS (2026-09-13). dist/ is not what visitors get. Cloudflare edits the HTML
at the edge, and two of its features failed the breeder's PSI report while this gate,
reading dist/, said PASS:
  * Google tag gateway injects `<script async src="/70de/">` (gtag.js, 181 KB) into <head>,
    ahead of our interaction-deferred loader: unused JS, forced reflow, missing source map.
    It is a zone toggle (Cloudflare → Tag Management → Google Tag Gateway), not code.
    `/70de/` was misfiled as Rocket Loader for two months; it never was.
  * Cloudflare Fonts rewrites a Google Fonts <link> into inline /cf-fonts/ faces.
`--live` lists every script/font/stylesheet the live page loads that dist/ never
references (EDGE-INJECTED). An injected SCRIPT fails the gate.

WHY LOCAL CLS CAN LIE. Local runs finish loading the preloaded hero photo before first
paint, so a box that only reaches its final size when the image arrives never shifts here.
PSI measured the near-me hero at CLS 0.266 while every local run (dist and live) read 0.
The cause was `.hero-field{margin-left:auto}` shrink-wrapping a grid item to its tile chips
until the photo loaded. It reproduced only by DELAYING images in headless Chrome. When PSI
and local disagree on CLS, delay each resource class in turn before you theorise.

Each run writes data/quality/perf/<slug>--<profile>[--live].json, which the Page Board
release gate reads (scripts/pageboard.py perf_findings).
"""
import argparse
import datetime
import functools
import http.server
import json
import pathlib
import re
import socketserver
import statistics
import subprocess
import sys
import threading
import os
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PERF_DIR = ROOT / "data" / "quality" / "perf"
LIVE_ORIGIN = "https://congoafricangreys.com"
LH_BIN = ROOT / "node_modules" / ".bin" / "lighthouse"
CONFIGS = {"mobile": ROOT / "scripts/lighthouse/agentic-mobile.mjs",
           "desktop": ROOT / "scripts/lighthouse/agentic-desktop.mjs"}

CATEGORIES = ("performance", "accessibility", "best-practices", "seo", "agentic-browsing")
THRESHOLDS = {c: 0.995 for c in CATEGORIES}
# Unscored and only ever caused by edge-injected third-party code; --live names the source.
IGNORE_AUDITS = {"valid-source-maps"}
EDGE_TYPES = {"Script", "Font", "Stylesheet"}
PORT = 4399


def judge(reports):
    """Categories whose median score is under the floor. A missing or null score is 0 —
    a category Lighthouse did not produce must not pass on nothing."""
    failed = []
    for cat, floor in THRESHOLDS.items():
        scores = [((r.get("categories") or {}).get(cat) or {}).get("score") or 0 for r in reports]
        if statistics.median(scores) < floor:
            failed.append(cat)
    return failed


def _requests(report):
    return ((report.get("audits", {}).get("network-requests") or {}).get("details") or {}).get("items") or []


def edge_injected(report, dist_html):
    """Script/font/stylesheet URLs the page loaded that the built HTML never references."""
    out = []
    for item in _requests(report):
        if item.get("resourceType") not in EDGE_TYPES:
            continue
        url = item["url"]
        parts = urllib.parse.urlsplit(url)
        path = parts.path + (f"?{parts.query}" if parts.query else "")
        if url in dist_html or (parts.path not in ("", "/") and path in dist_html):
            continue
        if parts.hostname in ("127.0.0.1", "localhost") and parts.path in dist_html:
            continue
        out.append(url)
    return out


def edge_blocking(report, injected):
    """The injected URLs that are scripts — those cost main-thread time and fail the gate.
    A font a stylesheet we ship pulls in (its url() is in CSS, not HTML) is reported only."""
    scripts = {i["url"] for i in _requests(report) if i.get("resourceType") == "Script"}
    return [u for u in injected if u in scripts]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve(root):
    handler = functools.partial(QuietHandler, directory=str(root))
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


PSI_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"


def psi_url(url, profile, key=""):
    q = [("url", url), ("strategy", profile)] + [("category", c) for c in CATEGORIES]
    if key:
        q.append(("key", key))
    return f"{PSI_ENDPOINT}?{urllib.parse.urlencode(q)}"


def run_psi(url, out, profile):
    try:
        with urllib.request.urlopen(psi_url(url, profile, os.environ.get("PSI_API_KEY", "")), timeout=180) as r:
            body = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"PSI API {e.code}: {e.read()[:300].decode(errors='replace')}\n"
                 "Keyless quota is per day; set PSI_API_KEY, or run pagespeed.web.dev by hand.")
    report = body["lighthouseResult"]
    pathlib.Path(out).write_text(json.dumps(report))
    return report


def run_lighthouse(url, out, profile):
    if not LH_BIN.exists():
        sys.exit("node_modules/.bin/lighthouse missing — `npm i` (devDependency lighthouse@13.4.1).")
    cmd = [str(LH_BIN), url, "--quiet", "--output=json", f"--output-path={out}",
           f"--config-path={CONFIGS[profile]}", "--chrome-flags=--headless=new --no-sandbox"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0 or not pathlib.Path(out).exists():
        sys.exit(f"lighthouse failed:\n{res.stderr[-1500:]}")
    return json.loads(pathlib.Path(out).read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--mobile", action="store_true")
    ap.add_argument("--live", action="store_true", help="audit the deployed URL, not dist/")
    ap.add_argument("--psi", action="store_true", help="PageSpeed Insights API on the deployed URL (implies --live)")
    ap.add_argument("--runs", type=int, default=1)
    a = ap.parse_args()
    a.live = a.live or a.psi

    slug = a.slug.strip("/")
    page = DIST / slug / "index.html" if slug else DIST / "index.html"
    if not page.exists():
        sys.exit(f"{page} not built — `npx astro build` first. The edge diff and the record both need dist/.")
    dist_html = page.read_text()
    profile = "mobile" if a.mobile else "desktop"
    path = f"/{slug}/" if slug else "/"

    httpd = None
    if a.live:
        url = LIVE_ORIGIN + path
    else:
        httpd = serve(DIST)
        url = f"http://127.0.0.1:{PORT}{path}"

    reports = []
    tag = f"{slug or 'home'}--{profile}{'--psi' if a.psi else '--live' if a.live else ''}"
    try:
        for i in range(a.runs):
            runner = run_psi if a.psi else run_lighthouse
            reports.append(runner(url, f"/tmp/lh-{tag}{'-psi' if a.psi else ''}-{i}.json", profile))
            if a.runs > 1:
                print(f"  run {i + 1}/{a.runs} done")
    finally:
        if httpd:
            httpd.shutdown()

    lh_version = reports[0].get("lighthouseVersion", "?")
    print(f"\n  {path}  [{profile}{' · PSI' if a.psi else ' · LIVE' if a.live else ' · dist'}]  {a.runs} run(s) · Lighthouse {lh_version}")
    failed = judge(reports)
    median = {}
    for cat, floor in THRESHOLDS.items():
        scores = [((r["categories"].get(cat) or {}).get("score") or 0) for r in reports]
        median[cat] = statistics.median(scores)
        spread = "" if len(scores) == 1 else f"  (runs: {', '.join(str(round(s * 100)) for s in sorted(scores))})"
        print(f"    {'FAIL' if cat in failed else 'PASS'}  {cat:17s} {round(median[cat] * 100):3d}  floor 100{spread}")

    metrics = {}
    for m in ("cumulative-layout-shift", "largest-contentful-paint", "total-blocking-time"):
        vals = [r["audits"][m]["numericValue"] for r in reports if m in r["audits"]]
        if vals:
            metrics[m] = round(statistics.median(vals), 4)
            print(f"    {m}: median {metrics[m]}  min {round(min(vals), 4)}  max {round(max(vals), 4)}")

    injected, blocking = [], []
    if a.live:
        injected = sorted({u for r in reports for u in edge_injected(r, dist_html)})
        blocking = sorted({u for r in reports for u in edge_blocking(r, injected)})
        print("\n  EDGE-INJECTED (loaded live, never referenced by dist/):")
        for u in injected:
            print(f"    {'FAIL' if u in blocking else 'note'}  {u}")
        if not injected:
            print("    none")
        if blocking:
            print("    → a script Cloudflare adds at the edge. /70de/ = Google tag gateway: "
                  "dashboard → Tag Management → Google Tag Gateway → off, then Purge Everything.")

    print("\n  Failing audits (worst run):")
    worst = min(reports, key=lambda r: sum(((r["categories"].get(k) or {}).get("score") or 0) for k in THRESHOLDS))
    shown = 0
    for aid, aud in worst["audits"].items():
        if aid in IGNORE_AUDITS:
            continue
        score = aud.get("score")
        if score is not None and score < 1 and aud.get("scoreDisplayMode") not in ("informative", "manual", "notApplicable"):
            items = (aud.get("details") or {}).get("items") or []
            print(f"    - {aid}: {aud.get('title', '')} ({len(items)} item(s)) {aud.get('displayValue', '')}")
            shown += 1
    if not shown:
        print("    none")

    PERF_DIR.mkdir(parents=True, exist_ok=True)
    record = {
        "slug": slug, "profile": profile, "live": a.live, "psi": a.psi, "lighthouse": lh_version, "runs": a.runs,
        "median": median, "metrics": metrics, "failed": failed,
        "edge_injected": injected, "edge_blocking": blocking,
        "dist_mtime": page.stat().st_mtime,
        "measured_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    }
    (PERF_DIR / f"{tag}.json").write_text(json.dumps(record, indent=2) + "\n")

    if failed or blocking:
        sys.exit(f"\nPERF GATE FAIL: {', '.join(failed + (['edge-injected-script'] if blocking else []))}")
    print("\nPERF GATE PASS")


if __name__ == "__main__":
    main()

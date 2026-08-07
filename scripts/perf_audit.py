#!/usr/bin/env python3
"""perf_audit.py — the PageSpeed gate this repo did not have.

Before 2026-08-07 the only way to know a page's PageSpeed status was for the breeder to
paste the URL into pagespeed.web.dev after a deploy and report back. That is rework by
definition: the defect is already live when it is found. This runs Lighthouse against
`dist/` over a local server, before push.

  python3 scripts/perf_audit.py african-grey-breeding-pair-for-sale
  python3 scripts/perf_audit.py <slug> --mobile
  python3 scripts/perf_audit.py <slug> --runs 5        # CLS is bimodal on this site

Why a CLI and not only a harness check: Lighthouse costs ~25s per page against the render
harness's ~2s checks, so it cannot run on every page on every commit. The fast contrast
invariant lives in `tests/render/checks/a11y.ts` (`a11y-text-contrast-aa`, blocking) and
runs in the harness; this runs on a named page, on demand, before push.

KNOWN-IGNORED, do not chase in code:
  `valid-source-maps` pointing at /70de/ — that path is Cloudflare Rocket Loader, injected
  at the edge, absent from this repo, and Unscored by Lighthouse. Toggle it in the
  Cloudflare dashboard (Speed -> Optimization) or leave it. See project_blog_perf_rocket_loader.

MEASUREMENT NOTE: CLS on this site is bimodal — a single run produced a confident wrong
attribution once already (reference_bimodal_metrics_need_5_runs). `--runs N` reports the
MEDIAN and the spread, and the gate judges the median. Never conclude from one run.
"""
import argparse
import functools
import http.server
import json
import pathlib
import socketserver
import statistics
import subprocess
import sys
import threading

# Floors. accessibility/best-practices/SEO are absolutes on this site; performance has a
# little headroom because it moves with network emulation.
THRESHOLDS = {"performance": 0.95, "accessibility": 1.0, "best-practices": 1.0, "seo": 1.0}
IGNORE_AUDITS = {"valid-source-maps"}
PORT = 4399


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):  # keep the report readable
        pass


def serve(root):
    handler = functools.partial(QuietHandler, directory=str(root))
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def run_lighthouse(url, out, mobile):
    cmd = [
        "npx", "-y", "lighthouse", url, "--quiet",
        "--output=json", f"--output-path={out}",
        "--chrome-flags=--headless=new --no-sandbox",
    ]
    if not mobile:
        cmd.append("--preset=desktop")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0 or not pathlib.Path(out).exists():
        sys.exit(f"lighthouse failed:\n{res.stderr[-1500:]}")
    return json.loads(pathlib.Path(out).read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--mobile", action="store_true")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--json", default="")
    a = ap.parse_args()

    dist = pathlib.Path("dist")
    if not dist.exists():
        sys.exit("dist/ missing — run `npx astro build` first. Gates measure dist, never source.")
    page = dist / a.slug.strip("/") / "index.html"
    if not page.exists():
        sys.exit(f"{page} not built — check the slug.")

    httpd = serve(dist)
    url = f"http://127.0.0.1:{PORT}/{a.slug.strip('/')}/"
    profile = "mobile" if a.mobile else "desktop"

    reports = []
    try:
        for i in range(a.runs):
            out = a.json or f"/tmp/lh-{a.slug.replace('/', '-')}-{profile}-{i}.json"
            reports.append(run_lighthouse(url, out, a.mobile))
            if a.runs > 1:
                print(f"  run {i + 1}/{a.runs} done")
    finally:
        httpd.shutdown()

    print(f"\n  {a.slug}  [{profile}]  {a.runs} run(s)")
    failed = []
    for key, floor in THRESHOLDS.items():
        scores = [r["categories"][key]["score"] or 0 for r in reports]
        med = statistics.median(scores)
        ok = med >= floor
        spread = "" if len(scores) == 1 else f"  (runs: {', '.join(str(round(s * 100)) for s in sorted(scores))})"
        print(f"    {'PASS' if ok else 'FAIL'}  {key:15s} {round(med * 100):3d}  floor {round(floor * 100)}{spread}")
        if not ok:
            failed.append(key)

    # Metrics that need the distribution, not a point estimate.
    if a.runs > 1:
        for m in ("cumulative-layout-shift", "largest-contentful-paint"):
            vals = [r["audits"][m]["numericValue"] for r in reports if m in r["audits"]]
            if vals:
                print(f"    {m}: median {round(statistics.median(vals), 4)}  "
                      f"min {round(min(vals), 4)}  max {round(max(vals), 4)}")

    print("\n  Failing audits (worst run):")
    worst = min(reports, key=lambda r: sum((r["categories"][k]["score"] or 0) for k in THRESHOLDS))
    shown = 0
    for aid, aud in worst["audits"].items():
        if aid in IGNORE_AUDITS:
            continue
        score = aud.get("score")
        if score is not None and score < 1:
            items = (aud.get("details") or {}).get("items") or []
            print(f"    - {aid}: {aud.get('title', '')} ({len(items)} element(s))")
            shown += 1
    if not shown:
        print("    none")
    if any(aid in worst["audits"] and worst["audits"][aid].get("score") not in (None, 1)
           for aid in IGNORE_AUDITS):
        print("    (valid-source-maps suppressed — Cloudflare Rocket Loader, not this repo)")

    if failed:
        sys.exit(f"\nPERF GATE FAIL: {', '.join(failed)}")
    print("\nPERF GATE PASS")


if __name__ == "__main__":
    main()

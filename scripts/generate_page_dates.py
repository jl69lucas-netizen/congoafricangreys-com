#!/usr/bin/env python3
"""
Generate data/page-dates.json — the truthful per-page freshness map.

WHY A COMMITTED MAP AND NOT A BUILD-TIME `git log`:
`.github/workflows/deploy.yml` uses `actions/checkout@v4` with no `fetch-depth`,
which is a **depth-1 clone**. In CI there is exactly one commit, so every file's
"last commit date" is the deploy date — a build-time git lookup would stamp a fake
`dateModified` of *today* onto all 108 pages on every deploy. That is the visible-date
rule's dishonesty moved into JSON-LD, which is worse, not better: it would tell AI
crawlers every page changed today, every day.

So: compute real dates HERE, from full local history, and commit the result.

datePublished = the first commit that touched the page file.
dateModified  = the most recent commit that touched it.

Run after adding pages or before a freshness-relevant deploy, then commit the JSON.

Usage:
  python3 scripts/generate_page_dates.py [--check]

`--check` exits non-zero if the committed map is stale, for CI.
"""
import json, subprocess, sys, glob, pathlib

OUT = pathlib.Path("data/page-dates.json")


def route_for(path):
    """src/pages/foo/index.astro -> /foo/ ; src/pages/index.astro -> /"""
    parts = path.split("/")
    if parts[-1] in ("index.astro", "index.html"):
        seg = parts[2:-1]
    else:
        seg = parts[2:-1] + [parts[-1].rsplit(".", 1)[0]]
    return "/" + "/".join(seg) + "/" if seg else "/"


def git_dates(path):
    """(first, last) commit dates for a path as YYYY-MM-DD, or (None, None)."""
    try:
        out = subprocess.run(
            ["git", "log", "--follow", "--format=%cs", "--", path],
            capture_output=True, text=True, check=True).stdout.split()
    except subprocess.CalledProcessError:
        return None, None
    if not out:
        return None, None
    return out[-1], out[0]


def build():
    pages = sorted(glob.glob("src/pages/**/*.astro", recursive=True)) + \
            sorted(glob.glob("src/pages/**/*.html", recursive=True))
    routes, skipped = {}, []
    for p in pages:
        first, last = git_dates(p)
        if not last:
            skipped.append(p)          # never committed yet — no honest date exists
            continue
        # Does the page already emit its own dateModified? Many pages build their
        # schema inline in the BODY (`<script type="application/ld+json"
        # set:html={JSON.stringify(articleSchema)} />`) rather than passing it via the
        # schemaJson prop, so BaseLayout cannot detect it from props — 36 pages ended
        # up with TWO contradicting dates on the first attempt. Detect it here, at the
        # source, and let the layout honour the flag.
        self_dated = "dateModified" in pathlib.Path(p).read_text(encoding="utf-8")
        routes[route_for(p)] = {
            "datePublished": first,
            "dateModified": last,
            "selfDated": self_dated,
        }
    return routes, skipped


def main():
    routes, skipped = build()
    payload = {
        "_meta": {
            "description": ("Truthful per-page freshness map for JSON-LD "
                            "dateModified/datePublished. Generated from git history by "
                            "scripts/generate_page_dates.py — NOT at build time, because "
                            "CI runs a depth-1 checkout and would stamp today's date on "
                            "every page. Regenerate and commit after content changes."),
            "generated_by": "scripts/generate_page_dates.py",
            "pages": len(routes),
        },
        "routes": routes,
    }
    new = json.dumps(payload, indent=2, sort_keys=False) + "\n"

    if "--check" in sys.argv:
        old = OUT.read_text() if OUT.exists() else ""
        old_r = json.loads(old)["routes"] if old else {}
        if old_r != routes:
            drift = set(old_r) ^ set(routes)
            changed = {k for k in set(old_r) & set(routes) if old_r[k] != routes[k]}
            print(f"STALE — {len(drift)} route(s) added/removed, {len(changed)} changed. "
                  "Run: python3 scripts/generate_page_dates.py")
            return 1
        print(f"page-dates.json current — {len(routes)} routes")
        return 0

    OUT.write_text(new)
    print(f"wrote {OUT} — {len(routes)} routes")
    if skipped:
        print(f"  {len(skipped)} page(s) not yet committed, so they carry no honest "
              f"date and are omitted: {skipped[:4]}")
    if not routes:
        print("0 routes — THIS IS NOT A PASS. Check the glob and that git history exists.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

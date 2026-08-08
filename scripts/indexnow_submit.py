#!/usr/bin/env python3
"""IndexNow submission for congoafricangreys.com — Bing, Yandex, and Google-via-proxy.

Built 2026-08-08. Before this, no submission script existed, and the procedure
documented in `.claude/skills/cag-indexing/SKILL.md` STEP 4 was broken three
separate ways by the MFS->CAG find/replace:

  1. INDEXNOW_KEY = "a1b2c3d4e5f6789012345678african grey parrots"
     A placeholder with the brand string substituted into it. The REAL key was
     recorded correctly in the same file's site-context table, 170 lines earlier.
  2. The sitemap <loc> regex was `https://african grey parrotsforsale\\.com/` —
     a domain containing spaces. It matches nothing, ever.
  3. SITE_ROOT pointed at /Users/apple/Downloads/MFS/site2, which EXISTS — so a
     run would have read a different site's sitemaps.

Any run of it would have POSTed an empty urlList under an invalid key. That is
why this close-out step never happened. The key is read from disk here rather
than typed, so defect 1 cannot recur.

Usage
  python3 scripts/indexnow_submit.py african-grey-breeding-pair-for-sale
  python3 scripts/indexnow_submit.py <slug> <slug> ...     # several pages
  python3 scripts/indexnow_submit.py --changed             # pages changed vs origin/main
  python3 scripts/indexnow_submit.py --all                 # every sitemap URL
  python3 scripts/indexnow_submit.py --dry-run <slug>      # show payload, send nothing

Exit codes: 0 submitted (or dry run), 1 refused/failed. Nothing is submitted
unless every precondition passes — a bad submission is worse than none.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

HOST = "congoafricangreys.com"
ORIGIN = f"https://{HOST}"
ENDPOINT = "https://api.indexnow.org/indexnow"
PUBLIC = pathlib.Path("public")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125 Safari/537.36"

# Never submit these. `/.astro/` is a build artifact that the sitemap generator
# currently emits into page-sitemap.xml — submitting it would ask Bing to crawl
# a directory that is not a page.
JUNK = ("/.astro/", "/admin/", "/form/", "/thank-you/", "/tag/", "/_preview/")


def die(msg: str) -> None:
    print(f"REFUSED: {msg}", file=sys.stderr)
    sys.exit(1)


def find_key() -> str:
    """Read the key from its own key file. Never hardcode it — see defect 1 above."""
    candidates = [p for p in PUBLIC.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem)]
    if not candidates:
        die("no IndexNow key file in public/ matching ^[0-9a-f]{32}\\.txt$")
    if len(candidates) > 1:
        die(f"multiple key files, cannot choose: {[p.name for p in candidates]}")
    kf = candidates[0]
    body = kf.read_text().strip()
    if body != kf.stem:
        die(f"{kf.name} body ({body!r}) != filename stem ({kf.stem!r}); IndexNow requires they match")
    return kf.stem


def http(url, data=None, method="GET"):
    req = urllib.request.Request(url, data=data, method=method, headers={"User-Agent": UA})
    if data is not None:
        req.add_header("Content-Type", "application/json; charset=utf-8")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")[:400]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")[:400]
    except Exception as e:  # noqa: BLE001 - network shape varies, all are equally fatal here
        return 0, str(e)


def verify_key_live(key: str) -> None:
    status, body = http(f"{ORIGIN}/{key}.txt")
    if status != 200:
        die(f"key file not reachable at {ORIGIN}/{key}.txt (HTTP {status}). Deploy it before submitting.")
    if body.strip() != key:
        die(f"live key file body ({body.strip()!r}) != key ({key!r})")
    print(f"key       {key}  (live, HTTP 200, body matches)")


def urls_from_sitemaps():
    out = []
    for name in ("page-sitemap.xml", "post-sitemap.xml", "local-sitemap.xml"):
        p = PUBLIC / name
        if not p.exists():
            continue
        out += re.findall(rf"<loc>({re.escape(ORIGIN)}/[^<]*)</loc>", p.read_text())
    return sorted(set(out))


def changed_slugs(ref="origin/main"):
    """Page slugs whose source changed vs a git ref, plus anything uncommitted."""
    cmds = [
        ["git", "diff", "--name-only", f"{ref}...HEAD"],
        ["git", "diff", "--name-only", "HEAD"],
        ["git", "ls-files", "--others", "--exclude-standard"],
    ]
    files = set()
    for c in cmds:
        r = subprocess.run(c, capture_output=True, text=True)
        if r.returncode == 0:
            files.update(x for x in r.stdout.split("\n") if x.strip())
    slugs = set()
    for f in files:
        m = re.match(r"src/pages/(.+)/index\.(astro|html)$", f)
        if m:
            slugs.add(m.group(1))
        elif f == "src/pages/index.astro":
            slugs.add("")
    return sorted(slugs)


def to_url(token: str) -> str:
    if token.startswith("http"):
        return token
    return f"{ORIGIN}/" + token.strip("/") + "/" if token.strip("/") else f"{ORIGIN}/"


def main() -> int:
    ap = argparse.ArgumentParser(description="Submit CAG URLs to IndexNow.")
    ap.add_argument("slugs", nargs="*", help="page slugs or full URLs")
    ap.add_argument("--changed", action="store_true", help="derive slugs from git changes vs origin/main")
    ap.add_argument("--all", action="store_true", help="every URL in the sitemaps")
    ap.add_argument("--dry-run", action="store_true", help="print the payload, submit nothing")
    ap.add_argument("--skip-live-check", action="store_true",
                    help="do not verify each URL returns 200 first (NOT recommended)")
    a = ap.parse_args()

    if not PUBLIC.is_dir():
        die("run from the repo root — public/ not found")

    if a.all:
        urls = urls_from_sitemaps()
    elif a.changed:
        slugs = changed_slugs()
        if not slugs:
            print("no changed page sources vs origin/main — nothing to submit")
            return 0
        urls = [to_url(s) for s in slugs]
    elif a.slugs:
        urls = [to_url(s) for s in a.slugs]
    else:
        ap.error("give slugs, or --changed, or --all")

    urls = [u for u in urls if not any(j in u for j in JUNK)]
    urls = sorted(set(urls))
    if not urls:
        die("no submittable URLs after filtering build artifacts")

    key = find_key()
    verify_key_live(key)

    # A URL that 404s must never be submitted. IndexNow treats junk submissions as
    # a trust signal about the host, so this check is the point of the script.
    if not a.skip_live_check:
        print(f"\nchecking {len(urls)} URL(s) are live...")
        live, dead = [], []
        for u in urls:
            status, _ = http(u)
            (live if status == 200 else dead).append((u, status))
            print(f"  {status:>3}  {u}")
        if dead:
            print(f"\n{len(dead)} URL(s) are not 200 and will NOT be submitted:", file=sys.stderr)
            for u, s in dead:
                print(f"  HTTP {s}  {u}", file=sys.stderr)
        urls = [u for u, _ in live]
        if not urls:
            die("every URL failed the live check")

    payload = {
        "host": HOST,
        "key": key,
        "keyLocation": f"{ORIGIN}/{key}.txt",
        "urlList": urls,
    }

    print(f"\nsubmitting {len(urls)} URL(s) to {ENDPOINT}")
    for u in urls:
        print(f"  + {u}")

    if a.dry_run:
        print("\n--dry-run: nothing sent. Payload:")
        print(json.dumps(payload, indent=2))
        return 0

    status, body = http(ENDPOINT, data=json.dumps(payload).encode(), method="POST")
    meaning = {
        200: "OK — URLs submitted",
        202: "Accepted — received, key validation pending",
        400: "Bad request — invalid payload",
        403: "Forbidden — key not valid for this host",
        422: "Unprocessable — URLs do not belong to the host, or key mismatch",
        429: "Too many requests — throttled, retry later",
    }.get(status, "unexpected response")
    print(f"\nIndexNow HTTP {status} — {meaning}")
    if body.strip():
        print(f"body: {body.strip()}")
    if status in (200, 202):
        print(f"\nSUBMITTED {len(urls)} URL(s).")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())

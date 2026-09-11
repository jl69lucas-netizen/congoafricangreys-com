#!/usr/bin/env python3
"""Regenerate all sitemap shards from the live src/pages/ filesystem.

Guarantees: every live page appears in exactly one shard, no phantom URLs,
no cross-shard duplicates, lastmod = the real git commit date of each page's
source file (TODAY only when that file has uncommitted changes, is
untracked, or has no git history yet).

lastmod follows the page's OWN source file — an edit to a shared component or
data file doesn't bump it.

Writes each shard to BOTH public/ and site/content/. This is deliberate:
.github/workflows/deploy.yml copies site/content/*.xml -> public/*.xml before
the Astro build, so if we only wrote public/ the deploy would silently revert
our fresh sitemaps to the stale site/content copies. Writing both keeps them
byte-identical, so the workflow copy is a harmless no-op. (Fixed 2026-06-05 —
live had been stuck on the 2026-05-11 site/content sitemaps for this reason.)

Run after adding/removing any page.
"""
import datetime
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "src" / "pages"
PUBLIC = ROOT / "public"
CONTENT = ROOT / "site" / "content"  # deploy.yml copies this over public/ — keep in sync
OUT_DIRS = [PUBLIC, CONTENT]
BASE = "https://congoafricangreys.com"
TODAY = datetime.date.today().isoformat()

# --- lastmod: real git commit date of each page's source file ---
# TODAY_REASONS collects (slug/label, reason) for every URL that fell back to
# TODAY, so the run's stdout can explain itself instead of silently claiming
# everything changed.
TODAY_REASONS = []

def _git(*args):
    """Run git in ROOT. Fails loudly (exits) if git itself is unusable —
    we never want to silently fall back to stamping every URL with TODAY."""
    try:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True
        )
    except FileNotFoundError as exc:
        sys.exit(f"generate_sitemaps: git executable not found — lastmod requires git history ({exc})")

_probe = _git("rev-parse", "--is-inside-work-tree")
if _probe.returncode != 0 or _probe.stdout.strip() != "true":
    sys.exit(
        f"generate_sitemaps: {ROOT} is not a usable git work tree — cannot compute "
        f"real lastmod dates.\n{_probe.stderr.strip()}"
    )

def source_file(dir_path: pathlib.Path):
    """The page source file for a slug directory (index.astro/.html/.md), or
    None if the directory has no index page (e.g. a phantom/empty dir)."""
    for ext in ("astro", "html", "md"):
        p = dir_path / f"index.{ext}"
        if p.exists():
            return p
    return None

def lastmod_for(path, label):
    """lastmod for one URL = the committer date (YYYY-MM-DD) of the last
    commit touching its source file. Falls back to TODAY — and records why
    in TODAY_REASONS — when the file doesn't exist, has uncommitted/untracked
    changes (it's about to change), or has no git history yet."""
    if path is None:
        TODAY_REASONS.append((label, "no source file found"))
        return TODAY
    rel = str(path.relative_to(ROOT))
    status = _git("status", "--porcelain", "--", rel).stdout
    if status.strip():
        TODAY_REASONS.append((label, "uncommitted/untracked changes"))
        return TODAY
    log = _git("log", "-1", "--format=%cs", "--", rel).stdout.strip()
    if not log:
        TODAY_REASONS.append((label, "no git history for this file"))
        return TODAY
    return log

# --- enumerate live slugs from the filesystem ---
top_slugs = sorted(
    p.name for p in PAGES.iterdir()
    if p.is_dir() and p.name not in {"blog", "search", "available"}
    and source_file(p) is not None
)
blog_slugs = sorted(
    p.name for p in (PAGES / "blog").iterdir()
    if p.is_dir() and source_file(p) is not None
) if (PAGES / "blog").is_dir() else []
# individual bird listing pages live at src/pages/available/<slug>/index.astro.
# The bare /available/ parent DOES have its own index.astro (a live indexable
# hub page, robots index,follow, canonical .../available/, no redirect) — it
# is emitted separately below, in page-sitemap.xml alongside the /blog/ hub.
available_slugs = sorted(
    p.name for p in (PAGES / "available").iterdir()
    if p.is_dir() and any((p / f"index.{ext}").exists() for ext in ("astro", "html", "md"))
) if (PAGES / "available").is_dir() else []

# --- classification ---
GEO_BUY = {"buy-intelligent-african-grey-for-sale-ca",
           "buy-male-african-gray-birds-for-sale-nyc-ny"}

def is_location(slug: str) -> bool:
    if slug in GEO_BUY:
        return True
    return slug.startswith("african-grey-parrot-for-sale-") and slug != "african-grey-parrot-for-sale-near-me"

location_slugs = [s for s in top_slugs if is_location(s)]
page_slugs = [s for s in top_slugs if not is_location(s)]

# --- priority tiers for page-sitemap ---
TIER_10 = {"african-grey-parrot-for-sale", "african-grey-parrots-for-sale",
           "congo-african-grey-for-sale", "timneh-african-grey-for-sale"}
TIER_09 = {"buy-african-grey-parrot-near-me", "african-grey-parrot-price",
           "african-grey-breeding-pair-for-sale", "baby-african-grey-parrot-for-sale",
           "hand-raised-african-grey-parrot-for-sale", "dna-tested-african-grey-for-sale",
           "captive-bred-african-grey-parrot", "where-to-buy-african-greys-near-me",
           "african-grey-parrots-for-sale-near-me", "african-grey-parrot-for-sale-near-me",
           "congo-african-grey-parrot-pair-for-sale",
           "african-grey-parrot-bird-eggs-for-sale-usa", "contact-us",
           "buy-african-grey-parrots-with-shipping"}
TIER_03 = {"privacy-policy"}

def page_meta(slug: str):
    if slug in TIER_10:
        return "weekly", "1.0"
    if slug in TIER_09:
        return "weekly", "0.9"
    if slug in TIER_03:
        return "yearly", "0.3"
    return "monthly", "0.8"

def url_block(loc, lastmod, changefreq, priority):
    return (f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n"
            f"    <changefreq>{changefreq}</changefreq>\n    <priority>{priority}</priority>\n  </url>\n")

def write_both(filename, text):
    """Write identical bytes to public/ and site/content/ (see module docstring)."""
    for d in OUT_DIRS:
        (d / filename).write_text(text)

def write_urlset(filename, blocks, comment=None):
    head = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    if comment:
        head += f"  <!-- {comment} -->\n"
    write_both(filename, head + "".join(blocks) + "</urlset>\n")

# --- page-sitemap.xml (homepage + all non-location, non-blog pages) ---
page_lastmods = []
home_lm = lastmod_for(source_file(PAGES), "/ (homepage)")
page_lastmods.append(home_lm)
page_blocks = [url_block(f"{BASE}/", home_lm, "weekly", "1.0")]
blog_hub_lm = lastmod_for(source_file(PAGES / "blog"), "/blog/ (hub)")
page_lastmods.append(blog_hub_lm)
page_blocks.append(url_block(f"{BASE}/blog/", blog_hub_lm, "weekly", "0.7"))
# /available/ is a live hub page (src/pages/available/index.astro), same tier
# as the /blog/ hub above — weekly / 0.7, not a location or blog-post page.
available_hub_lm = lastmod_for(source_file(PAGES / "available"), "/available/ (hub)")
page_lastmods.append(available_hub_lm)
page_blocks.append(url_block(f"{BASE}/available/", available_hub_lm, "weekly", "0.7"))
for s in page_slugs:
    cf, pr = page_meta(s)
    lm = lastmod_for(source_file(PAGES / s), s)
    page_lastmods.append(lm)
    page_blocks.append(url_block(f"{BASE}/{s}/", lm, cf, pr))
# individual available-bird listing pages — money pages, refresh weekly
for s in available_slugs:
    lm = lastmod_for(source_file(PAGES / "available" / s), f"available/{s}")
    page_lastmods.append(lm)
    page_blocks.append(url_block(f"{BASE}/available/{s}/", lm, "weekly", "0.9"))
write_urlset("page-sitemap.xml", page_blocks,
             f"Pages — generated {TODAY} from src/pages/")

# --- local-sitemap.xml (location/geo pages) ---
loc_lastmods = [lastmod_for(source_file(PAGES / s), s) for s in location_slugs]
loc_blocks = [url_block(f"{BASE}/{s}/", lm, "weekly", "0.8") for s, lm in zip(location_slugs, loc_lastmods)]
write_urlset("local-sitemap.xml", loc_blocks,
             f"Location pages — generated {TODAY} from src/pages/")

# --- post-sitemap.xml (blog posts) ---
post_lastmods = [lastmod_for(source_file(PAGES / "blog" / s), f"blog/{s}") for s in blog_slugs]
post_blocks = [url_block(f"{BASE}/blog/{s}/", lm, "monthly", "0.7") for s, lm in zip(blog_slugs, post_lastmods)]
write_urlset("post-sitemap.xml", post_blocks,
             f"Blog posts — generated {TODAY} from src/pages/blog/")

# --- sitemap_index.xml (each shard's lastmod = the latest lastmod among its URLs) ---
# video-sitemap.xml isn't generated by this script (no src/pages/ source), but it is
# a real static file, so it gets a real date the same way — from its own git history.
video_sitemap_lm = lastmod_for(PUBLIC / "video-sitemap.xml", "video-sitemap.xml")
shard_lastmods = {
    "page-sitemap.xml": max(page_lastmods) if page_lastmods else TODAY,
    "local-sitemap.xml": max(loc_lastmods) if loc_lastmods else TODAY,
    "post-sitemap.xml": max(post_lastmods) if post_lastmods else TODAY,
    "video-sitemap.xml": video_sitemap_lm,
}
shards = ["page-sitemap.xml", "local-sitemap.xml", "post-sitemap.xml", "video-sitemap.xml"]
idx = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for sh in shards:
    idx += ["  <sitemap>", f"    <loc>{BASE}/{sh}</loc>",
            f"    <lastmod>{shard_lastmods[sh]}</lastmod>", "  </sitemap>"]
idx.append("</sitemapindex>")
index_xml = "\n".join(idx) + "\n"
write_both("sitemap_index.xml", index_xml)
# keep sitemap.xml pointing at the index (some crawlers fetch /sitemap.xml)
write_both("sitemap.xml", index_xml)

# --- validation: every loc maps to a real page dir with a real source file ---
total = 1 + 1 + 1 + len(page_slugs) + len(available_slugs) + len(location_slugs) + len(blog_slugs)
print(f"page-sitemap : {len(page_blocks)} urls (incl. / and /blog/ and /available/)")
print(f"local-sitemap: {len(loc_blocks)} urls")
print(f"post-sitemap : {len(post_blocks)} urls")
print(f"TOTAL indexed: {total}")
# Every URL this script emits, paired with the page directory it should come
# from. Checking is_dir() alone missed the case that shipped this bug: a dir
# can exist (or not) independent of whether it actually has a source file —
# so we also re-run source_file() per URL and flag None, the same test a
# phantom .astro/dist/node_modules URL would fail.
emitted = [("/ (homepage)", PAGES), ("/blog/ (hub)", PAGES / "blog"), ("/available/ (hub)", PAGES / "available")]
emitted += [(s, PAGES / s) for s in page_slugs]
emitted += [(s, PAGES / s) for s in location_slugs]
emitted += [(f"blog/{s}", PAGES / "blog" / s) for s in blog_slugs]
emitted += [(f"available/{s}", PAGES / "available" / s) for s in available_slugs]
missing = [label for label, d in emitted if not d.is_dir() or source_file(d) is None]
print(f"phantom URLs (loc with no dir or no source file): {missing if missing else 'NONE ✓'}")
if TODAY_REASONS:
    print(f"lastmod = TODAY ({TODAY}) for {len(TODAY_REASONS)} url(s):")
    for label, reason in TODAY_REASONS:
        print(f"  - {label}: {reason}")
else:
    print("lastmod = TODAY for 0 urls — every source file is committed with real history")

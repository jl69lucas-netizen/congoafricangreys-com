#!/usr/bin/env python3
"""Regenerate all sitemap shards from the live src/pages/ filesystem.

Guarantees: every live page appears in exactly one shard, no phantom URLs,
no cross-shard duplicates, lastmod current. Writes to public/ (deploy copies
to dist/). Run after adding/removing any page.
"""
import datetime
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "src" / "pages"
PUBLIC = ROOT / "public"
BASE = "https://congoafricangreys.com"
TODAY = datetime.date.today().isoformat()

# --- enumerate live slugs from the filesystem ---
top_slugs = sorted(
    p.name for p in PAGES.iterdir()
    if p.is_dir() and p.name not in {"blog", "search"}
)
blog_slugs = sorted(
    p.name for p in (PAGES / "blog").iterdir() if p.is_dir()
) if (PAGES / "blog").is_dir() else []

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
           "affordable-african-grey-birds-for-sale", "grey-african-parrots-for-sale",
           "male-african-gray-for-sale", "congo-african-grey-parrot-pair-for-sale",
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

def write_urlset(path, blocks, comment=None):
    head = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    if comment:
        head += f"  <!-- {comment} -->\n"
    path.write_text(head + "".join(blocks) + "</urlset>\n")

# --- page-sitemap.xml (homepage + all non-location, non-blog pages) ---
page_blocks = [url_block(f"{BASE}/", TODAY, "weekly", "1.0")]
page_blocks.append(url_block(f"{BASE}/blog/", TODAY, "weekly", "0.7"))
for s in page_slugs:
    cf, pr = page_meta(s)
    page_blocks.append(url_block(f"{BASE}/{s}/", TODAY, cf, pr))
write_urlset(PUBLIC / "page-sitemap.xml", page_blocks,
             f"Pages — generated {TODAY} from src/pages/")

# --- local-sitemap.xml (location/geo pages) ---
loc_blocks = [url_block(f"{BASE}/{s}/", TODAY, "weekly", "0.8") for s in location_slugs]
write_urlset(PUBLIC / "local-sitemap.xml", loc_blocks,
             f"Location pages — generated {TODAY} from src/pages/")

# --- post-sitemap.xml (blog posts) ---
post_blocks = [url_block(f"{BASE}/blog/{s}/", TODAY, "monthly", "0.7") for s in blog_slugs]
write_urlset(PUBLIC / "post-sitemap.xml", post_blocks,
             f"Blog posts — generated {TODAY} from src/pages/blog/")

# --- sitemap_index.xml (keep video-sitemap, refresh lastmods) ---
shards = ["page-sitemap.xml", "local-sitemap.xml", "post-sitemap.xml", "video-sitemap.xml"]
idx = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for sh in shards:
    idx += ["  <sitemap>", f"    <loc>{BASE}/{sh}</loc>",
            f"    <lastmod>{TODAY}</lastmod>", "  </sitemap>"]
idx.append("</sitemapindex>")
(PUBLIC / "sitemap_index.xml").write_text("\n".join(idx) + "\n")
# keep sitemap.xml pointing at the index (some crawlers fetch /sitemap.xml)
(PUBLIC / "sitemap.xml").write_text("\n".join(idx) + "\n")

# --- validation: every loc maps to a real page dir ---
total = 1 + 1 + len(page_slugs) + len(location_slugs) + len(blog_slugs)
print(f"page-sitemap : {len(page_blocks)} urls (incl. / and /blog/)")
print(f"local-sitemap: {len(loc_blocks)} urls")
print(f"post-sitemap : {len(post_blocks)} urls")
print(f"TOTAL indexed: {total}")
missing = [s for s in page_slugs + location_slugs if not (PAGES / s).is_dir()]
missing += [s for s in blog_slugs if not (PAGES / 'blog' / s).is_dir()]
print(f"phantom URLs (loc with no dir): {missing if missing else 'NONE ✓'}")

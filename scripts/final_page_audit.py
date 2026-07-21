#!/usr/bin/env python3
"""C.A.Gs final-page-pass auditor — page-type-aware mechanical gate.
Reads dist/<slug>/index.html (slug may be nested, e.g. available/roys) and scores
the objective checks against the page-type PROFILE, returning per-check pass plus a
verdict: PASS / PASS-WITH-WARNINGS / FAIL. Subjective checks (voice/humor/Flesch/
non-commodity/tone/brand-protocol) stay manual. Run AFTER `npx astro build`.
Profiles: interior (default), bird (--birds), blog (--blog, auto-discovers the
/blog/ hub + every dist/blog/<slug>/ post; also included in the default run)."""
import re, json, sys
from pathlib import Path
from html.parser import HTMLParser

DIST = Path("dist")
def dist_path(slug):
    """Resolve a flat or nested slug to its rendered index.html."""
    return DIST / slug / "index.html"

SLUGS = [
    "african-grey-parrot-care-guide","african-grey-care","african-grey-parrot-diet",
    "best-african-grey-parrot-food","african-grey-parrot-lifespan","african-grey-parrot-health-guarantee",
    "trusted-african-grey-parrot-breeders","african-grey-reviews","captive-bred-african-grey-parrot",
    "cites-african-grey-documentation","how-to-avoid-african-grey-parrot-scams","african-grey-parrot-guide",
    "african-grey-parrot-faq","how-to-tame-african-grey-parrot","african-grey-adoption",
    "african-grey-parrot-price","contact-us","privacy-policy",
]
TRANSACTIONAL = {"african-grey-parrot-price"}  # #5/#6 scoped here only

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.h={i:0 for i in range(1,7)}; s.imgs=[]; s.cur=None
        s.title=""; s.intitle=False; s.links=[]; s.cura=None; s.atext=[]
        s.jsonld=[]; s.injson=False; s.metadesc=""; s.canonical=""; s.body=[]
    def handle_starttag(s,t,a):
        d=dict(a)
        if re.fullmatch(r"h[1-6]",t): s.cur=int(t[1]); s.h[s.cur]+=1
        if t=="title": s.intitle=True
        if t=="img": s.imgs.append(d)
        if t=="a":
            s.cura=d; s.atext=[]
        if t=="meta" and d.get("name")=="description": s.metadesc=d.get("content","")
        if t=="link" and d.get("rel")=="canonical": s.canonical=d.get("href","")
        if t=="script" and d.get("type")=="application/ld+json": s.injson=True
    def handle_startendtag(s,t,a):
        s.handle_starttag(t,a)
    def handle_endtag(s,t):
        if t=="title": s.intitle=False
        if re.fullmatch(r"h[1-6]",t): s.cur=None
        if t=="a" and s.cura is not None:
            s.links.append((s.cura, "".join(s.atext).strip())); s.cura=None
        if t=="script" and s.injson:
            s.injson=False
    def handle_data(s,data):
        if s.intitle: s.title+=data
        if s.injson: s.jsonld.append(data)
        if s.cura is not None: s.atext.append(data)
        s.body.append(data)

# Per-page-type check severities. Anything unlisted falls back to DEFAULT_SEVERITY.
# FAIL = hard ship-blocker · WARN = soft (logged, shippable) · NA = not applicable.
DEFAULT_SEVERITY = "FAIL"
PROFILES = {
    "bird": {
        "newsletter_present": "NA",      # bird pages exempt (footer newsletter only)
        "all_h1_h4": "WARN",             # spec §4: H4 only where depth exists on a lean bird page
        "no_aggregateoffer": "FAIL",     # single Product+Offer only
        "no_pbfd_claim": "NA",           # PBFD + APV screening IS in the Verified-Claim Ledger (per-bird PCR testing confirmed by breeder 2026-06-20) — claim now permitted
        "shipping_line": "FAIL",
        "sold_not_instock": "FAIL",      # explicit: sold bird must not remain InStock in schema
        "wordcount_in_band": "WARN",
        "real_hero_image": "WARN",
        "house_method": "WARN",          # GAP-FLAG until breeder confirms a term
        "lifespan_40_60": "WARN",
    },
    "interior": {                        # back-compat with interior_29_audit behavior
        "no_aggregateoffer": "NA", "no_pbfd_claim": "NA",
        "shipping_line": "NA", "wordcount_in_band": "NA", "real_hero_image": "NA",
        "house_method": "WARN",
        "airport_codes": "WARN",         # transactional nicety on price page, not a ship-blocker
    },
    "comparison": {                      # [X] vs [Y] spokes + hub (added 2026-07-04 per breeder review)
        "no_aggregateoffer": "FAIL",     # comparison pages never carry Offer/AggregateOffer (variant pages own it)
        "no_pbfd_claim": "NA",
        "sold_not_instock": "NA",
        "newsletter_present": "NA",      # §11.6 breeder-review standard: NO page-level newsletter band on comparison pages — the inquiry form is the single closer (2026-07-05; the old "pass" rode on the word inside an HTML comment)
        "shipping_line": "FAIL",         # shipping section must show $185 airport / $350 home
        "real_hero_image": "FAIL",
        "wordcount_in_band": "WARN",     # deep-standard band 3,000–8,000 incl. chrome (5.2k target)
        "house_method": "WARN",
        "cites_captive_usda_early": "WARN",
        "lifespan_40_60": "WARN",
        "breadcrumb_one": "FAIL",
        "faqpage_present": "FAIL",
        "single_canonical": "FAIL",
        "no_emoji": "FAIL",
    },
    "for-sale": {                        # 22-page transactional for-sale cluster (2026-07-20)
        "no_aggregateoffer": "WARN",     # egg/single pages carry one Product+Offer; AggregateOffer only on group/hub
        "no_pbfd_claim": "NA",           # PBFD/APV PCR screening is in the Verified-Claim Ledger
        "sold_not_instock": "FAIL",      # sold ≠ InStock, ever
        "newsletter_present": "NA",      # inquiry form is the single closer, no page-level newsletter band
        "shipping_line": "FAIL",         # $185 airport / $350 home must appear
        "real_hero_image": "FAIL",
        "wordcount_in_band": "WARN",
        "house_method": "WARN",
        "cites_captive_usda_early": "WARN",
        "lifespan_40_60": "WARN",
        "breadcrumb_one": "FAIL",
        "faqpage_present": "FAIL",
        "single_canonical": "FAIL",
        "no_emoji": "FAIL",
    },
    "blog": {                            # /blog/ hub + dist/blog/<slug>/ posts (spec 2026-06-27)
        # Blog gate = ONLY the checks the cluster spec defines; everything else is
        # NA so a post is judged on what the program actually requires. The FAIL
        # gates below mirror the Heading Outline Gate + blog-cluster requirements.
        "_default": "NA",
        "h1==1": "FAIL",                 # exactly one page topic
        "no_skip": "FAIL",               # sequential H1→H6, no skipped levels
        "all_six_levels": "FAIL",        # every blog page carries all six levels
        "min_h5_5": "FAIL",              # >= 5 H5
        "min_h6_5": "FAIL",              # >= 5 H6
        "breadcrumb_one": "FAIL",        # exactly one BreadcrumbList (no dupes)
        "faqpage_present": "FAIL",       # FAQPage schema present
        "no_visible_date": "FAIL",       # freshness in schema only, never visible
        "no_escaped_svg": "FAIL",        # no raw &lt;svg dumped to the page
        "no_emoji": "FAIL",              # line-icon SVGs only, no colorful emoji
        "single_canonical": "FAIL",      # exactly one canonical link
    },
}
def severity(page_type, check):
    """Per-check severity, falling back to the profile's `_default`, then global."""
    prof = PROFILES.get(page_type, {})
    return prof.get(check, prof.get("_default", DEFAULT_SEVERITY))

def audit_html(slug, html, page_type="interior"):
    raw = html
    p = P(); p.feed(html)
    bodytext = " ".join(p.body)
    r = {}
    # --- headings (Part D.2 / #21) ---
    r["h1==1"] = p.h[1]==1
    r["all_h1_h4"] = all(p.h[i]>=1 for i in (1,2,3,4))
    r["h_counts"] = "".join(f"H{i}:{p.h[i]} " for i in range(1,7)).strip()
    r["no_skip"] = not any(p.h[i]>0 and p.h[i-1]==0 for i in range(2,7))
    # --- Heading Outline Gate (seo-rules Rule 52, 2026-06-20) ---
    # All six levels REQUIRED; H5 >= 5 AND H6 >= 5 on every page. The breeder
    # will not pass a page that ships only 1 H6 or 4 H5. Hard FAIL by default.
    r["all_six_levels"] = all(p.h[i]>=1 for i in range(1,7))
    r["min_h5_5"] = p.h[5] >= 5
    r["min_h6_5"] = p.h[6] >= 5
    # --- schema (Part I / #12) ---
    blobs=[]; valid=True
    for b in p.jsonld:
        b=b.strip()
        if not b: continue
        try: blobs.append(json.loads(b))
        except Exception: valid=False
    types=[]; org_found=[False]
    def walk(o):
        if isinstance(o,dict):
            tt=o.get("@type")
            if tt: types.append(tt)
            # Organization counts even when nested as publisher/author, or when
            # @type is a list like ["LocalBusiness","PetStore"] (valid schema).
            tl=tt if isinstance(tt,list) else [tt]
            if any(x in ("Organization","LocalBusiness","PetStore") for x in tl): org_found[0]=True
            for v in o.values(): walk(v)
        elif isinstance(o,list):
            for v in o: walk(v)
    for b in blobs: walk(b)
    flat=[t for x in types for t in (x if isinstance(x,list) else [x])]
    r["jsonld_valid"] = valid and bool(blobs)
    r["has_breadcrumb"] = "BreadcrumbList" in flat
    r["has_org"] = org_found[0]
    r["faqpage_count"] = flat.count("FAQPage")
    r["faqpage_ok"] = flat.count("FAQPage") <= 1
    r["schema_types"] = ",".join(sorted(set(flat)))
    # --- bird-listing hard gates (page_type == "bird") ---
    r["no_aggregateoffer"] = "AggregateOffer" not in flat
    # Fail only on an actual health CLAIM about PBFD/polyoma (tested clear / negative /
    # free of), not a mere mention or a denial — those would over-match (review finding).
    r["no_pbfd_claim"] = not re.search(
        r"\b(tested clear|tested negative|clear of|negative for|free of|screened for)\b"
        r"[\sa-z,]{0,25}\b(pbfd|polyoma\w*)", raw, re.I)
    r["shipping_line"] = bool(re.search(r"\$185.*\$350|185 airport.*350 home", bodytext, re.I)) \
                         or ("$185" in bodytext and "$350" in bodytext)
    # InStock fails only when a sold/reserved STATUS signal is present AND the schema
    # still shows InStock. Avoid commerce phrases like "sold together/separately".
    sold_signal = bool(re.search(
        r"\b(sold out|now sold|has been sold|this (?:bird|pair|grey) is sold|marked sold|"
        r"status:\s*(?:sold|reserved)|is reserved)\b", bodytext, re.I))
    instock = "InStock" in raw and "OutOfStock" not in raw
    r["sold_not_instock"] = not (sold_signal and instock)
    # word count of visible body (scripts stripped)
    vis = re.sub(r"<script[\s\S]*?</script>", "", raw)
    nwords = len(re.sub(r"<[^>]+>", " ", vis).split())
    # Bird pages use the deep 22-section standard (1,500–4,000 words).
    # Interior/other pages use the lean target (700–1,000 ±buffer for chrome).
    if page_type == "bird":
        r["wordcount_in_band"] = 1500 <= nwords <= 4000
    elif page_type == "comparison":
        r["wordcount_in_band"] = 3000 <= nwords <= 8000  # deep 22–25-section standard + chrome
    else:
        r["wordcount_in_band"] = 600 <= nwords <= 1200  # 700-1000 target ±buffer for chrome
    # hero must be a real photo, not a placeholder/logo
    content_imgs = [i for i in p.imgs if "logo" not in i.get("src", "").lower()]
    r["real_hero_image"] = bool(content_imgs) and not any(
        x in (content_imgs[0].get("src", "").lower()) for x in ("placeholder", "coming-soon", "default")
    ) if content_imgs else False
    # house-method naming (WARN) — presence of a named protocol where hand-rearing is discussed
    r["house_method"] = (not re.search(r"hand-rais|hand-fed|hand-rear", raw, re.I)) or \
                        bool(re.search(r"C\.A\.Gs [A-Z][a-z]+ Method|Grey Method", raw))
    # --- meta (Part J / #13) — long-format standard kept (≤275 title / ≤300 desc) ---
    r["title_len"] = len(p.title.strip())
    r["desc_len"] = len(p.metadesc.strip())
    r["title_le275"] = len(p.title.strip())<=275
    r["desc_le300"] = len(p.metadesc.strip())<=300
    r["desc_present"] = len(p.metadesc.strip())>0
    r["brand_in_title"] = "C.A.Gs" in p.title or "Congo African Grey" in p.title
    r["canonical_abs"] = p.canonical.startswith("https://")
    # --- images (Part J.2 / #14, #25) ---
    imgs=p.imgs
    def yes(i,k): return k in i and i[k] not in (None,"")
    r["img_total"]=len(imgs)
    r["img_all_alt"]=all("alt" in i for i in imgs)
    alts=[i.get("alt","") for i in imgs if i.get("alt","")]
    r["img_alt_unique"]=len(alts)==len(set(alts))
    r["img_alt_le190"]=all(len(i.get("alt",""))<=190 for i in imgs)
    # LCP-hero exemption: drop the header logo(s), then the FIRST remaining content
    # image is the eager LCP hero (correct). Every image after it must be lazy.
    content=[i for i in imgs if "logo" not in i.get("src","").lower()]
    non_hero=content[1:] if content else []
    r["img_lazy_nonhero"]=all(i.get("loading")=="lazy" for i in non_hero) if non_hero else True
    r["img_dims"]=all(yes(i,"width") and yes(i,"height") for i in imgs) if imgs else True
    # --- a11y / gotcha traps (Part K / M / #26, #28) ---
    r["no_svg_in_content"] = not re.search(r"content\s*:\s*['\"]\s*<svg", raw)
    # user-select:none is banned when APPLIED. Tailwind's bundled ".select-none{…}"
    # utility DEFINITION ships in the global CSS on every page even when unused
    # (site-wide false positive confirmed 2026-07-04) — strip that rule definition,
    # then fail only if markup actually applies the class or any other CSS sets it.
    css_nospace = raw.replace(" ", "").replace("\n", "")
    defs_stripped = re.sub(r"\.select-none[^{]*\{[^}]*\}", "", css_nospace)
    applied_class = bool(re.search(r'class="[^"]*\bselect-none\b', raw))
    r["no_userselect_none"] = ("user-select:none" not in defs_stripped) and not applied_class
    r["no_escaped_svg"] = "&lt;svg" not in raw
    r["no_emoji_parrot"] = "\U0001F99C" not in raw
    # --- links (Part F / #3, #23) ---
    ext=[(d,txt) for d,txt in p.links if d.get("href","").startswith("http") and "congoafricangreys.com" not in d.get("href","")]
    r["ext_links"]=len(ext)
    r["ext_newtab_rel"]=all(d.get("target")=="_blank" and "noopener" in d.get("rel","") for d,_ in ext) if ext else True
    bad_anchor=re.compile(r"^(click here|more|read more|here|learn more)$",re.I)
    r["no_bare_anchors"]=not any(bad_anchor.match(txt) for _,txt in p.links if txt)
    intc=[d for d,_ in p.links if d.get("href","").startswith("/")]
    r["internal_links"]=len(intc)
    # --- conversion (Part N / #17, Rule 61) ---
    phone=re.compile(r"\b(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b")
    footer_idx=raw.lower().find("<footer")
    body_part=raw[:footer_idx] if footer_idx>0 else raw
    body_clean=re.sub(r"<script[\s\S]*?</script>","",body_part)
    body_txt=re.sub(r"<[^>]+>"," ",body_clean)
    # Rule 61 bans the BREEDER's phone in body — third-party authority hotlines
    # (USDA/APHIS, FTC, IC3) are intentional and exempt.
    AUTH=("APHIS","USDA","FTC","IC3","hotline","fraud")
    bad_phone=[m for m in phone.finditer(body_txt)
               if not any(a.lower() in body_txt[max(0,m.start()-60):m.start()].lower() for a in AUTH)]
    r["no_phone_in_body"]=not bad_phone
    footer_part=raw[footer_idx:] if footer_idx>0 else ""
    r["phone_in_footer"]=bool(phone.search(re.sub(r"<[^>]+>"," ",footer_part))) if footer_part else None
    # --- compliance copy (Part N / Rule 44) — visible body, scripts stripped ---
    main=raw[raw.find("<main"):] if "<main" in raw else raw
    main=re.sub(r"<script[\s\S]*?</script>","",main)
    w300=" ".join(re.sub(r"<[^>]+>"," ",main).split()[:300]).lower()
    r["cites_captive_usda_early"]=(("appendix i" in w300 or "captive-bred" in w300 or "captive bred" in w300)
                                   and ("usda" in w300 or "awa" in w300))
    r["lifespan_40_60"]=bool(re.search(r"40\s*[–-]\s*60|40 to 60",bodytext))
    # --- newsletter (#18) — detect the signup form, not the word "newsletter"
    # (the cag-library/NewsletterV2 component emits no literal "newsletter" string).
    r["newsletter_present"]=("your@email.com" in raw) or ("newsletter" in raw.lower())
    # --- freshness (#GEO) — RULE: dates live ONLY in schema, never visible on the
    # page. Pass = NO visible "Updated/Last updated <Month> <Year>" text (scripts
    # stripped so schema dateModified does not trigger).
    visible=re.sub(r"<script[\s\S]*?</script>","",raw)
    visible=re.sub(r"<[^>]+>"," ",visible)
    r["no_visible_date"]=not re.search(r"(?:updated|last updated|last modified)\b[^0-9]{0,18}\b20\d\d", visible, re.I)
    # --- blog-only gates (page_type == "blog") ---
    # Computed only for blog so these never add new FAIL gates to bird/interior rows.
    if page_type in ("blog", "comparison"):
        r["breadcrumb_one"] = flat.count("BreadcrumbList") == 1
        r["faqpage_present"] = flat.count("FAQPage") >= 1
        r["single_canonical"] = len(re.findall(
            r"<link\b[^>]*\brel\s*=\s*['\"]canonical['\"]", raw, re.I)) == 1
        # No colorful pictographic emoji (kept text glyphs ✔ ✗ ★ are BMP < U+2B00,
        # so they never match these emoji planes). Catches 🎉 🔥 🚀 🦜 ⭐ flags, etc.
        r["no_emoji"] = not re.search(
            "[\U0001F1E6-\U0001F1FF\U0001F300-\U0001FAFF\U00002B00-\U00002BFF]", raw)
        # Stricter freshness check: catch a real "Updated <Month>" / "Posted on
        # <Month>" / "Last updated <Month/Year>" STAMP (a date label followed by an
        # actual month or year). Requiring the date token avoids false-positiving on
        # prose that merely names the policy (e.g. 'no visible "last updated" stamp').
        blog_date = re.search(
            r"\b(?:last updated|last modified|posted on|published on|updated|posted|published)\b"
            r"[\s:,.–-]{0,4}"
            r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|"
            r"aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?|20\d\d)\b",
            visible, re.I)
        r["no_visible_date"] = r["no_visible_date"] and not blog_date
    # --- transactional-only (#5/#6) ---
    if slug in TRANSACTIONAL:
        r["airport_codes"]=bool(re.search(r"\b(DEN|LAX|MIA|ORD|LAR)\b",bodytext))
    # severity only applies to boolean pass/fail checks — skip info keys (counts/strings)
    r["_severity"] = {k: severity(page_type, k) for k in r
                      if not k.startswith("_") and isinstance(r[k], bool)}
    hard_fails = [k for k, v in r.items() if v is False and r["_severity"].get(k) == "FAIL"]
    warns = [k for k, v in r.items() if v is False and r["_severity"].get(k) == "WARN"]
    r["_verdict"] = "FAIL" if hard_fails else ("PASS-WITH-WARNINGS" if warns else "PASS")
    r["_hard_fails"] = hard_fails
    r["_warns"] = warns
    return r

def audit(slug, page_type="interior"):
    f = dist_path(slug)
    if not f.exists():
        return {"_MISSING": True}
    return audit_html(slug, f.read_text(encoding="utf-8", errors="ignore"), page_type)

BIRDS = ["available/bery","available/amie","available/roys",
         "available/jins-jeni","available/elad","available/evie"]

COMPARISONS = ["african-grey-comparison","congo-vs-timneh-african-grey",
               "male-vs-female-african-grey-parrots-for-sale","african-grey-vs-macaw",
               "african-grey-vs-cockatoo","african-grey-vs-amazon-parrot",
               "african-grey-parrot-breeders-comparison","african-grey-pros-and-cons"]

FORSALE = ["african-grey-parrot-bird-eggs-for-sale-usa",
           "congo-african-grey-for-sale"]  # for-sale cluster, expanded as pages rebuild

def blog_targets():
    """Discover the /blog/ hub (dist/blog/index.html) + every dist/blog/<slug>/ post."""
    targets = []
    blog = DIST / "blog"
    if (blog / "index.html").exists():
        targets.append(("blog", "blog"))
    for f in sorted(blog.glob("*/index.html")):
        targets.append((f"blog/{f.parent.name}", "blog"))
    return targets

def main():
    if "--birds" in sys.argv:
        targets = [(s, "bird") for s in BIRDS]
    elif "--blog" in sys.argv:
        targets = blog_targets()
    elif "--comparison" in sys.argv:
        targets = [(s, "comparison") for s in COMPARISONS]
    elif "--for-sale" in sys.argv:
        targets = [(s, "for-sale") for s in FORSALE]
    else:
        targets = ([(s, "interior") for s in SLUGS] + blog_targets()
                   + [(s, "comparison") for s in COMPARISONS]
                   + [(s, "for-sale") for s in FORSALE])
    rows = {s: audit(s, t) for s, t in targets}
    print("\n=== C.A.Gs FINAL PAGE PASS ===  (verdict per page)\n")
    for s, r in rows.items():
        if r.get("_MISSING"):
            print(f"  ✗ {s}: dist/ MISSING — run `npx astro build`"); continue
        print(f"[{r['_verdict']}] {s}   {r['h_counts']} | FAQPage×{r['faqpage_count']} | schema:{r['schema_types']}")
        if r["_hard_fails"]: print("    FAIL → " + ", ".join(r["_hard_fails"]))
        if r["_warns"]:      print("    WARN → " + ", ".join(r["_warns"]))
    npass = sum(1 for r in rows.values() if r.get("_verdict") == "PASS")
    nwarn = sum(1 for r in rows.values() if r.get("_verdict") == "PASS-WITH-WARNINGS")
    nfail = sum(1 for r in rows.values() if r.get("_verdict") == "FAIL")
    print(f"\n{npass} PASS · {nwarn} PASS-WITH-WARNINGS · {nfail} FAIL  (of {len(rows)})")
    print("\nSubjective (voice/humor/Flesch/non-commodity/tone/brand-protocol) = manual spot-check.")

if __name__=="__main__":
    main()

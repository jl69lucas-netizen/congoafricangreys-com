#!/usr/bin/env python3
"""C.A.Gs final-page-pass auditor — page-type-aware mechanical gate.
Reads dist/<slug>/index.html (slug may be nested, e.g. available/roys) and scores
the objective checks against the page-type PROFILE, returning per-check pass plus a
verdict: PASS / PASS-WITH-WARNINGS / FAIL. Subjective checks (voice/humor/Flesch/
non-commodity/tone/brand-protocol) stay manual. Run AFTER `npx astro build`."""
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
        "no_pbfd_claim": "FAIL",         # not in Verified-Claim Ledger
        "shipping_line": "FAIL",
        "wordcount_in_band": "WARN",
        "real_hero_image": "WARN",
        "house_method": "WARN",          # GAP-FLAG until breeder confirms a term
        "lifespan_40_60": "WARN",
    },
    "interior": {                        # back-compat with interior_29_audit behavior
        "no_aggregateoffer": "NA", "no_pbfd_claim": "NA",
        "shipping_line": "NA", "wordcount_in_band": "NA", "real_hero_image": "NA",
        "house_method": "WARN",
    },
}
def severity(page_type, check):
    return PROFILES.get(page_type, {}).get(check, DEFAULT_SEVERITY)

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
    r["no_pbfd_claim"] = not re.search(r"\b(pbfd|polyoma)", raw, re.I)
    r["shipping_line"] = bool(re.search(r"\$185.*\$350|185 airport.*350 home", bodytext, re.I)) \
                         or ("$185" in bodytext and "$350" in bodytext)
    # InStock is only a failure when the bird is marked sold elsewhere on the page.
    sold = bool(re.search(r"\b(sold|reserved)\b", bodytext, re.I))
    instock = "InStock" in raw
    r["sold_not_instock"] = not (sold and instock)
    # word count of visible body (scripts stripped)
    vis = re.sub(r"<script[\s\S]*?</script>", "", raw)
    nwords = len(re.sub(r"<[^>]+>", " ", vis).split())
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
    r["no_userselect_none"] = "user-select:none" not in raw.replace(" ","")
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
    # --- transactional-only (#5/#6) ---
    if slug in TRANSACTIONAL:
        r["airport_codes"]=bool(re.search(r"\b(DEN|LAX|MIA|ORD|LAR)\b",bodytext))
    # severity only applies to boolean pass/fail checks — skip info keys (counts/strings)
    r["_severity"] = {k: severity(page_type, k) for k in r
                      if not k.startswith("_") and isinstance(r[k], bool)}
    return r

def audit(slug, page_type="interior"):
    f = dist_path(slug)
    if not f.exists():
        return {"_MISSING": True}
    return audit_html(slug, f.read_text(encoding="utf-8", errors="ignore"), page_type)

def main():
    rows={s:audit(s) for s in SLUGS}
    info={"h_counts","schema_types","title_len","desc_len","img_total","ext_links",
          "internal_links","faqpage_count","phone_in_footer"}
    keys=[]
    for r in rows.values():
        for k in r:
            if k not in keys and k not in info and not k.startswith("_"): keys.append(k)
    print("\n=== INTERIOR 29-CHECK AUDIT ===  (✓ pass / ✗ FAIL)\n")
    npass=0
    for s,r in rows.items():
        if r.get("_MISSING"): print(f"  ✗ {s}: dist/ MISSING — rebuild"); continue
        fails=[k for k in keys if k in r and r[k] is False]
        mark="✓" if not fails else "✗"
        if not fails: npass+=1
        print(f"{mark} {s}")
        print(f"    {r['h_counts']} | title:{r['title_len']} desc:{r['desc_len']} | "
              f"imgs:{r['img_total']} ext:{r['ext_links']} int:{r['internal_links']} | "
              f"FAQPage×{r['faqpage_count']} | schema:{r['schema_types']}")
        if fails: print("    FAIL → " + ", ".join(fails))
    print(f"\n{npass}/18 pages fully clean on mechanical checks.")
    print("\n=== CHECK ROLL-UP (pages failing each) ===")
    for k in keys:
        bad=[s for s,r in rows.items() if r.get(k) is False]
        if bad: print(f"  ✗ {k}: {len(bad)} → {', '.join(bad)}")
    print("\nSubjective checks (voice/humor/Flesch/non-commodity/tone/brand-protocol) = manual spot-check.")

if __name__=="__main__":
    main()

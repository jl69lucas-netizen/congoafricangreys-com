import json, re, urllib.request, gzip, io, concurrent.futures as cf, ssl
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
comps=json.load(open('data/competitors.json'))['competitors']

def get(url, t=15):
    r=urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(r, timeout=t, context=ctx) as f:
        d=f.read()
        if url.endswith('.gz') or d[:2]==b'\x1f\x8b':
            d=gzip.decompress(d)
        return f.status, d.decode('utf-8','replace')

def sitemap_urls(base):
    urls=set()
    for sm in ('/sitemap.xml','/sitemap_index.xml','/wp-sitemap.xml','/sitemap-index.xml'):
        try:
            s,body=get(base.rstrip('/')+sm)
        except Exception:
            continue
        if s!=200: continue
        locs=re.findall(r'<loc>\s*([^<]+?)\s*</loc>', body)
        subs=[l for l in locs if l.endswith('.xml') or l.endswith('.xml.gz')]
        if subs:
            for sub in subs[:12]:
                try:
                    s2,b2=get(sub)
                    urls.update(re.findall(r'<loc>\s*([^<]+?)\s*</loc>', b2))
                except Exception: pass
        urls.update(l for l in locs if not l.endswith(('.xml','.xml.gz')))
        if urls: break
    return urls

def probe(c):
    base=c['url']; out={'id':c['id'],'tier':c['tier'],'url':base}
    try:
        st,_=get(base, 12); out['home_status']=st
    except Exception as e:
        out['home_status']='ERR: '+type(e).__name__
    try:
        u=sitemap_urls(base)
    except Exception:
        u=set()
    out['sitemap_urls']=len(u)
    low=[x.lower() for x in u]
    out['amazon_pages']=[x for x in u if 'amazon' in x.lower()][:6]
    out['vs_pages']=[x for x in u if re.search(r'(-vs-|/vs-|\bversus\b|-vs\b)', x.lower())][:8]
    out['compare_pages']=[x for x in u if 'compar' in x.lower()][:5]
    return out

with cf.ThreadPoolExecutor(12) as ex:
    rows=list(ex.map(probe, comps))
json.dump(rows, open('/private/tmp/claude-501/-Users-apple-Downloads-CAG/9e577e92-12dd-4b7d-9421-2fd69b369248/scratchpad/comp_sweep.json','w'), indent=1)
for r in rows:
    print(f"[T{r['tier']}] {r['id']:26s} home={str(r['home_status']):8s} sm={r['sitemap_urls']:5d} amazon={len(r['amazon_pages'])} vs={len(r['vs_pages'])} compare={len(r['compare_pages'])}")
    for k in ('amazon_pages','vs_pages','compare_pages'):
        for p in r[k]: print(f"      {k[:6]}: {p}")

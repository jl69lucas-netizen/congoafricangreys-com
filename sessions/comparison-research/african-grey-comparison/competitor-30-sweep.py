import json, re, urllib.request, gzip, concurrent.futures as cf, ssl
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
comps=json.load(open('data/competitors.json'))['competitors']

# Does any registry site have a COMPARISON HUB or vs-pages we'd compete with?
SIGNALS={
 'comparison': r'(compar|vs-|/vs-|versus|side-by-side)',
 'hub':        r'(hub|guide|which-parrot|best-parrot|choose)',
 'talking':    r'(talking|talk|mimic|vocabulary|best-talking)',
 'vs_grey':    r'(african-grey-vs|grey-vs-|vs-african-grey|congo-vs|timneh-vs)',
 'types':      r'(types-of|congo|timneh)',
}

def get(url, t=15):
    r=urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(r, timeout=t, context=ctx) as f:
        d=f.read()
        if url.endswith('.gz') or d[:2]==b'\x1f\x8b': d=gzip.decompress(d)
        return f.status, d.decode('utf-8','replace')

def sitemap_urls(base):
    urls=set()
    for sm in ('/sitemap.xml','/sitemap_index.xml','/wp-sitemap.xml','/sitemap-index.xml','/post-sitemap.xml'):
        try: s,body=get(base.rstrip('/')+sm)
        except Exception: continue
        if s!=200: continue
        locs=re.findall(r'<loc>\s*([^<]+?)\s*</loc>', body)
        subs=[l for l in locs if l.endswith(('.xml','.xml.gz'))]
        if subs:
            for sub in subs[:14]:
                try:
                    s2,b2=get(sub); urls.update(re.findall(r'<loc>\s*([^<]+?)\s*</loc>', b2))
                except Exception: pass
        urls.update(l for l in locs if not l.endswith(('.xml','.xml.gz')))
        if urls: break
    return urls

def probe(c):
    base=c['url']; out={'id':c['id'],'tier':c['tier'],'url':base}
    try: st,_=get(base,12); out['home_status']=st
    except Exception as e: out['home_status']='ERR:'+type(e).__name__
    try: u=sitemap_urls(base)
    except Exception: u=set()
    out['sitemap_urls']=len(u)
    for name,pat in SIGNALS.items():
        m=[x for x in u if re.search(pat,x.lower())]
        out['sm_'+name]=len(m)
        if name in ('comparison','vs_grey'): out['url_'+name]=m[:6]
    return out

with cf.ThreadPoolExecutor(12) as ex:
    rows=list(ex.map(probe, comps))
json.dump(rows, open('sessions/comparison-research/african-grey-comparison/competitor-30-sweep.json','w'), indent=1)
for r in rows:
    print(f"[T{r['tier']}] {r['id'][:24]:24s} home={str(r['home_status']):9s} sm={r['sitemap_urls']:5d} "
          f"compare={r.get('sm_comparison',0)} vsGrey={r.get('sm_vs_grey',0)} talking={r.get('sm_talking',0)} hub={r.get('sm_hub',0)}")
    for p in (r.get('url_vs_grey',[])+r.get('url_comparison',[]))[:6]: print('      ->',p)

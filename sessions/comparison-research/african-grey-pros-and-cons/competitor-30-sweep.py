import json, re, urllib.request, gzip, concurrent.futures as cf, ssl
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
comps=json.load(open('data/competitors.json'))['competitors']

# Does each registry site carry decision/pros-cons/behaviour-problem content?
SIGNALS={
 'pros_cons':  r'(pros?-and-cons|pros-cons|advantages|disadvantages)',
 'good_pet':   r'(good-pet|make-good-pets|good-pets|right-for-you|should-i-get)',
 'problems':   r'(problem|feather-pluck|plucking|biting|aggression|behavior|behaviour|screaming|noise)',
 'beginner':   r'(beginner|first-time|novice|experienced)',
 'lifespan':   r'(lifespan|life-span|how-long|years)',
 'cost':       r'(cost|price|expensive|how-much)',
 'ag_pages':   r'(african-grey|congo|timneh|grey-parrot)',
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
    base=c['url']; out={'id':c['id'],'name':c.get('name'),'tier':c['tier'],'url':base}
    try: st,html=get(base,12); out['home_status']=st
    except Exception as e: out['home_status']='ERR:'+type(e).__name__; html=''
    low=html.lower()
    out['home_signals']={k:(re.search(v,low) is not None) for k,v in SIGNALS.items()}
    try: u=sitemap_urls(base)
    except Exception: u=set()
    out['sitemap_urls']=len(u)
    for name,pat in SIGNALS.items():
        matches=[x for x in u if re.search(pat,x.lower())]
        out['sm_'+name]=len(matches)
        if name in ('pros_cons','good_pet'): out['url_'+name]=matches[:4]
    return out

with cf.ThreadPoolExecutor(12) as ex:
    rows=list(ex.map(probe, comps))
json.dump(rows, open('sessions/comparison-research/african-grey-pros-and-cons/competitor-30-sweep.json','w'), indent=1)
for r in rows:
    s=r.get('home_signals',{}) or {}; hit=lambda k:'Y' if s.get(k) else '.'
    print(f"[T{r['tier']}] {r['id'][:24]:24s} home={str(r['home_status']):9s} sm={r['sitemap_urls']:5d} "
          f"proscons={hit('pros_cons')}/{r.get('sm_pros_cons',0)} goodpet={hit('good_pet')}/{r.get('sm_good_pet',0)} "
          f"problems={hit('problems')}/{r.get('sm_problems',0)} lifespan={r.get('sm_lifespan',0)}")
    for p in (r.get('url_pros_cons',[])+r.get('url_good_pet',[])): print('      ->',p)

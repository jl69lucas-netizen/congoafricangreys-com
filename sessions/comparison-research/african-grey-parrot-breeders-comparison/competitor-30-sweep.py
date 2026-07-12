import json, re, urllib.request, gzip, concurrent.futures as cf, ssl
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
comps=json.load(open('data/competitors.json'))['competitors']

# Trust/credential signals a breeder-comparison page must audit publicly on each site
SIGNALS={
 'about':      r'(about|our-story|who-we-are)',
 'reviews':    r'(review|testimonial|feedback)',
 'health_guar':r'(health-guarantee|guarantee|warranty)',
 'cites_docs': r'(cites|documentation|paperwork|certificate|dna|health-cert)',
 'shipping':   r'(shipping|delivery|ship-)',
 'contact':    r'(contact|reach-us)',
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
    for sm in ('/sitemap.xml','/sitemap_index.xml','/wp-sitemap.xml','/sitemap-index.xml','/product-sitemap.xml'):
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

def home_signals(base):
    """Scan homepage HTML for trust keywords + price hints."""
    try: st,html=get(base,12)
    except Exception as e: return ('ERR:'+type(e).__name__, {}, [])
    low=html.lower()
    found={k:(re.search(v,low) is not None) for k,v in SIGNALS.items()}
    kw={k:(k in low) for k in ['usda','avian vet','captive-bred','captive bred','hand-raised','hand raised',
        'closed band','microchip','money back','paypal','zelle','wire','crypto','weaned']}
    prices=sorted(set(re.findall(r'\$\s?([1-9],?\d{3})', html)))[:6]
    return (st, {**found, **{'kw_'+k.replace(' ','_'):v for k,v in kw.items()}}, prices)

def probe(c):
    base=c['url']; out={'id':c['id'],'name':c.get('name'),'tier':c['tier'],'url':base}
    st,sig,prices=home_signals(base)
    out['home_status']=st; out['home_signals']=sig; out['home_prices']=prices
    try: u=sitemap_urls(base)
    except Exception: u=set()
    out['sitemap_urls']=len(u)
    for name,pat in SIGNALS.items():
        out['sm_'+name]=len([x for x in u if re.search(pat,x.lower())])
    return out

with cf.ThreadPoolExecutor(12) as ex:
    rows=list(ex.map(probe, comps))
json.dump(rows, open('sessions/comparison-research/african-grey-parrot-breeders-comparison/competitor-30-sweep.json','w'), indent=1)
for r in rows:
    s=r.get('home_signals',{}) or {}
    hit=lambda k: 'Y' if s.get(k) else '.'
    print(f"[T{r['tier']}] {r['id'][:24]:24s} home={str(r['home_status']):9s} sm={r['sitemap_urls']:4d} "
          f"rev={hit('reviews')} guar={hit('health_guar')} cites={hit('cites_docs')} ship={hit('shipping')} "
          f"usda={hit('kw_usda')} weaned={hit('kw_weaned')} prices={r['home_prices']}")

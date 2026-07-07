#!/usr/bin/env python3
"""Cross-page duplicate-copy auditor.

Finds word-for-word copy shared between built pages in dist/ — the "same
template, same paragraphs" failure the breeder keeps catching (shipping
sections, available-now intros, repeated anchor texts). Compares visible
body text only (scripts/styles/JSON-LD stripped) using word shingles.

Usage:
  python3 scripts/dup_content_audit.py                 # audit all dist pages
  python3 scripts/dup_content_audit.py slugA slugB ... # audit only these slugs
  python3 scripts/dup_content_audit.py --min-words 15  # change shingle length

Exit 1 if any duplicate run >= MIN_WORDS is found between two different pages.
Boilerplate that legitimately repeats (nav, footer, the canonical shipping
cost line, doc-badge lists) is whitelisted below.
"""
import re, sys, itertools
from pathlib import Path
from html.parser import HTMLParser

MIN_WORDS = 12
WHITELIST_SNIPPETS = [
    "ships nationwide $185 airport $350 home",
    "pbfd pcr screening avian polyomavirus pcr dna sexing certificate avian vet health certificate hatch certificate closed band",
    "cites cert pcr dna sexed vet certified pbfd apv screened fully weaned",
]

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ("script","style","noscript","header","footer","nav"): self.skip+=1
    def handle_endtag(self,t):
        if t in ("script","style","noscript","header","footer","nav") and self.skip: self.skip-=1
    def handle_data(self,d):
        if not self.skip: self.parts.append(d)

def words(path: Path):
    p=Text(); p.feed(path.read_text(errors="ignore"))
    txt=" ".join(p.parts).lower()
    return re.findall(r"[a-z0-9$']+", txt)

def norm(ws): return " ".join(ws)

def main():
    args=[a for a in sys.argv[1:] if not a.startswith("--")]
    global MIN_WORDS
    if "--min-words" in sys.argv:
        MIN_WORDS=int(sys.argv[sys.argv.index("--min-words")+1])
    dist=Path("dist")
    pages={p.parent.name or "home": p for p in dist.rglob("index.html")}
    if args: pages={k:v for k,v in pages.items() if k in args}
    shingled={}
    for slug,p in pages.items():
        ws=words(p)
        sh={}
        for i in range(len(ws)-MIN_WORDS+1):
            sh.setdefault(norm(ws[i:i+MIN_WORDS]), i)
        shingled[slug]=(ws,sh)
    bad=0
    for (a,(wa,sa)),(b,(wb,sb)) in itertools.combinations(shingled.items(),2):
        common=set(sa)&set(sb)
        # collapse overlapping shingles into maximal runs
        reported=set()
        for s in sorted(common, key=lambda s: sa[s]):
            if any(s in r for r in reported): continue
            if any(w in s for w in WHITELIST_SNIPPETS): continue
            i=sa[s]; j=i+MIN_WORDS
            while j<len(wa) and norm(wa[j-MIN_WORDS+1:j+1]) in sb: j+=1
            run=norm(wa[i:j]); reported.add(run)
            if any(w in run for w in WHITELIST_SNIPPETS): continue
            bad+=1
            print(f"DUPLICATE ({j-i} words) between /{a}/ and /{b}/:\n  \"{run[:220]}{'…' if len(run)>220 else ''}\"\n")
    if bad:
        print(f"FAIL — {bad} duplicated passages ≥{MIN_WORDS} words."); sys.exit(1)
    print(f"PASS — no cross-page duplicate runs ≥{MIN_WORDS} words in {len(pages)} pages.")

if __name__=="__main__":
    main()

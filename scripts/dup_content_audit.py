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
  python3 scripts/dup_content_audit.py --headers       # heading-crossover mode:
      flags any H1-H6 whose exact text (or template with species names swapped)
      appears on 2+ pages — catches the "29 crossover headers" failure that the
      12-word shingle check is blind to (most headings are < 12 words).

Exit 1 if any duplicate run >= MIN_WORDS (or duplicate heading in --headers
mode) is found between two different pages. Boilerplate that legitimately
repeats (nav, footer, the canonical shipping cost line, doc-badge lists,
site-standard section headers) is whitelisted below.
"""
import re, sys, itertools
from pathlib import Path
from html.parser import HTMLParser

MIN_WORDS = 12
WHITELIST_SNIPPETS = [
    "ships nationwide $185 airport $350 home",
    "pbfd pcr screening avian polyomavirus pcr dna sexing certificate avian vet health certificate hatch certificate closed band",
    "cites cert pcr dna sexed vet certified pbfd apv screened fully weaned",
    # canonical price-matrix data repeated in comparison-table Grey columns
    "typical price $1 700 $3 500 our greys",
    # mandated CTA-band trust bullets (deposit / guarantee / IATA — CLAUDE.md)
    "$200 deposit reserves your bird 3 day health guarantee iata compliant shipping nationwide",
    # canonical inquiry invitation line above the CTA band
    "hand raised cites documented and dna sexed reach out to start the conversation we reply within 24 hours",
    # credential badge strip (NAP + trust set — mandated identical)
    "since 2014 usda awa cites docs dna sexing pcr screened",
]

SKIP_TAGS = {"script", "style", "noscript", "header", "footer", "nav", "form"}
VOID_TAGS = {"br", "img", "hr", "input", "meta", "link", "source", "track", "wbr", "area", "base", "col", "embed"}
# chrome elements not wrapped in a semantic tag: jump rails, TOC card grids,
# section-directory blocks, breadcrumbs
CHROME_RE = re.compile(r"jump|toc|rail|msp-|crumb", re.I)

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.stack=[]
    def handle_starttag(self,t,attrs):
        if t in VOID_TAGS: return
        skipping = bool(self.stack and self.stack[-1][1])
        if not skipping:
            blob = " ".join(v for k,v in attrs if v and k in ("class","id","aria-label"))
            skipping = t in SKIP_TAGS or bool(CHROME_RE.search(blob))
        self.stack.append((t, skipping))
    def handle_endtag(self,t):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == t:
                del self.stack[i:]; break
    def handle_data(self,d):
        if not (self.stack and self.stack[-1][1]): self.parts.append(d)

def words(path: Path):
    p=Text(); p.feed(path.read_text(errors="ignore"))
    txt=" ".join(p.parts).lower()
    return re.findall(r"[a-z0-9$']+", txt)

def norm(ws): return " ".join(ws)

# Headings allowed to repeat on every page (site-standard sections).
HEADER_WHITELIST = [
    "frequently asked questions",
    "shipping & delivery",
    "reserve your bird",
    "get in touch",
    "join our newsletter",
    # Footer.astro 5-column headings (site chrome not wrapped in <footer>)
    "shop african greys",
    "by location",
    "resources & trust",
    "contact",
    # Owner card (the breeder's name is the breeder's name)
    "mark & teri benjamin",
    # Bird-name card headings — sync with data/clutch-inventory.json when
    # inventory changes; a bird's name legitimately repeats wherever its
    # card renders.
    "amie", "bery", "roys", "elad", "evie", "jins", "jeni",
]
# Species/variant tokens normalized in --headers mode so that templated
# headers ("Is a Macaw Right for You?" vs "Is a Cockatoo Right for You?")
# are caught as template-for-template crossovers, not just exact matches.
SPECIES_TOKENS = re.compile(
    r"\b(congo|timneh|macaw|cockatoo|amazon(?: parrot)?|eclectus|african grey|grey)\b")

def headers_mode(pages):
    """Flag exact + templated H1-H6 crossovers between pages."""
    hpat = re.compile(r"<h([1-6])[^>]*>(.*?)</h\1>", re.S | re.I)
    strip = re.compile(r"<[^>]+>")
    exact, templ = {}, {}
    for slug, p in pages.items():
        html = p.read_text(errors="ignore")
        for lvl, raw in hpat.findall(html):
            import html as _h
            text = _h.unescape(re.sub(r"\s+", " ", strip.sub("", raw)).strip().lower())
            if not text or any(w in text for w in HEADER_WHITELIST):
                continue
            exact.setdefault(text, set()).add(slug)
            templ.setdefault(SPECIES_TOKENS.sub("{species}", text), set()).add(slug)
    bad = 0
    for text, slugs in sorted(exact.items()):
        if len(slugs) > 1:
            bad += 1
            print(f"EXACT header crossover on {sorted(slugs)}:\n  \"{text}\"\n")
    for text, slugs in sorted(templ.items()):
        if len(slugs) > 1 and text not in exact:
            bad += 1
            print(f"TEMPLATE header crossover on {sorted(slugs)}:\n  \"{text}\"\n")
    if bad:
        print(f"FAIL — {bad} crossover headers across {len(pages)} pages."); sys.exit(1)
    print(f"PASS — no crossover headers in {len(pages)} pages.")

def main():
    args=[a for a in sys.argv[1:] if not a.startswith("--")]
    global MIN_WORDS
    if "--min-words" in sys.argv:
        MIN_WORDS=int(sys.argv[sys.argv.index("--min-words")+1])
    dist=Path("dist")
    pages={p.parent.name or "home": p for p in dist.rglob("index.html")}
    if args: pages={k:v for k,v in pages.items() if k in args}
    if "--headers" in sys.argv:
        headers_mode(pages); return
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

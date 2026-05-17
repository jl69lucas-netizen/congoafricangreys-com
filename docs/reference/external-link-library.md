# CAG External Link Library
Last updated: 2026-05-17
Source: cag-external-link-agent

All URLs verified live before insertion. Anchors are sentence-middle/beginning placement only (never at end of sentence).

---

## Category: Authority — Government / Legal

| URL | Category | Anchor Variant 1 | Anchor Variant 2 | Anchor Variant 3 | Status |
|-----|----------|-----------------|-----------------|-----------------|--------|
| `https://www.aphis.usda.gov/awa/public-search` | Authority | USDA APHIS license search tool | USDA Animal Welfare Act public database | USDA AWA breeder verification portal | ✅ 200 |
| `https://www.fws.gov/program/cites` | Authority | USFWS CITES program | US Fish & Wildlife CITES overview | federal CITES enforcement guidelines | ✅ 301→200 |
| `https://ic3.gov/` | Authority | FBI Internet Crime Complaint Center (IC3) | IC3 online fraud reporting | FBI's IC3 scam reporting portal | ✅ 308→200 |
| `https://reportfraud.ftc.gov/` | Authority | FTC fraud reporting portal | Federal Trade Commission fraud report | FTC ReportFraud.gov | ✅ 200 |
| `https://lookup.icann.org/` | Authority | ICANN WHOIS registry | official ICANN domain lookup | ICANN domain registration database | ✅ 200 |
| `https://whois.domaintools.com/` | Authority | DomainTools WHOIS lookup | domain history tool at DomainTools | WHOIS historical domain data | ✅ 200 |

---

## Category: Authority — Species / Wildlife

| URL | Category | Anchor Variant 1 | Anchor Variant 2 | Anchor Variant 3 | Status |
|-----|----------|-----------------|-----------------|-----------------|--------|
| `https://en.wikipedia.org/wiki/Grey_parrot` | Authority | African Grey parrot natural history | Grey parrot (Psittacus erithacus) research | African Grey species taxonomy | ✅ 200 |

---

## Category: Authority — Reverse Image / WHOIS

| URL | Category | Anchor Variant 1 | Anchor Variant 2 | Anchor Variant 3 | Status |
|-----|----------|-----------------|-----------------|-----------------|--------|
| `https://images.google.com/` | Authority | Google reverse image search | Google Images photo verification tool | Google's reverse image lookup | ✅ 200 |
| `https://www.tineye.com/` | Authority | TinEye reverse image search | TinEye photo duplication checker | TinEye image origin tracker | ✅ 200 |

---

## Usage Rules (per cag-external-link-agent)

1. Link appears in beginning or middle of sentence — NEVER at the end
2. Max 2 external links per 300 words on any page
3. Max 1 external link per paragraph
4. `rel="noopener noreferrer"` on all external links
5. Never use `rel="nofollow"` on authority links
6. Rotate anchor variants — never same anchor twice on one page for same URL
7. Verify URL still returns 200 before inserting (run curl check quarterly)

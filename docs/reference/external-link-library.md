# CAG External Link Library
Last updated: 2026-06-06
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
| `https://parrots.org/encyclopedia/grey-parrot/` | Authority | World Parrot Trust grey parrot encyclopedia | Grey parrot wild diet & range | World Parrot Trust species profile | ✅ 200 (www→non-www 301) |

---

## Category: Authority — Avian Nutrition / Diet (added 2026-06-06, diet page)

| URL | Category | Anchor Variant 1 | Anchor Variant 2 | Anchor Variant 3 | Status |
|-----|----------|-----------------|-----------------|-----------------|--------|
| `https://lafeber.com/vet/avian-nutrition-basics/` | Authority | LafeberVet avian nutrition basics | veterinary avian-nutrition reference | avian nutrition fundamentals (LafeberVet) | ✅ 200 (avian-nutrition→-basics 301) |
| `https://lafeber.com/vet/basic-information-sheet-for-the-african-grey-parrot/` | Authority | LafeberVet African Grey information sheet | LafeberVet African Grey care + toxic-food sheet | veterinary African Grey basics | ✅ 200 |

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

---

## Authority Citations for Technical / Clinical Terms (added 2026-06-04)

> **Rule (Task 7):** important technical terms should be cited ONCE to a credible **government / NIH** source (prefer `pmc.ncbi.nlm.nih.gov`) or the **canonical industry authority**, at the sentence where we make the claim. New-tab + `rel="noopener noreferrer"` + the `.cag-article`/`.home-d` ↗ cue. Link a term only once per page (exact-match repetition = over-optimization). Verify 200 before inserting.

| Term | Verified source (200) | Notes |
|---|---|---|
| PCR-based DNA sexing | https://pmc.ncbi.nlm.nih.gov/articles/PMC11939742/ | Molecular sexing from down/feather, monomorphic birds |
| PBFD (Psittacine Beak & Feather Disease) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12560886/ | PBFD global-spread review |
| Avian Polyomavirus (APV) | https://pmc.ncbi.nlm.nih.gov/articles/PMC2168798/ | Polyomaviruses of birds review |
| Hypocalcemia (African Grey) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7128777/ | African-grey hypocalcemia seizure syndrome |
| IATA Live Animals Regulations (LAR) | https://www.iata.org/en/programs/cargo/live-animals/ | Canonical industry authority (no PMC equivalent) |
| CITES Appendix I | https://www.cites.org/eng/app/appendices.php | Already in use |
| Cognition research (Alex) | https://alexfoundation.org/ | Already in use |

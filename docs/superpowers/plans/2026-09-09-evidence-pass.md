# C.A.Gs Evidence Pass Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `cag-evidence-pass` gate (skill + `evidence_audit.py` + evidence ledger + rule-index rows + render fixture), retire the six injector rules that manufacture repetition, and run the pass over the homepage section by section without removing any section.

**Architecture:** A Python audit over `dist/` (same pattern as `scripts/aeo_audit.py`) owns the four checks nothing else owns: term budgets per page type, claim-to-proof binding, statement labels, evidence integrity. One Playwright check in the existing SEM family proves the label component renders. The skill is written RED→GREEN per superpowers:writing-skills: a baseline subagent run is recorded first, the skill is written against those exact rationalisations, then re-run. Rule changes land in WORKFLOW.md, the keyword-verifier agent, seo-rules.md, the meta agent and `final_page_audit.py` so the new gate is not overruled in the same sprint.

**Tech Stack:** Python 3 + pytest 8 (`tests/test_*.py`), Playwright render harness (`tests/render/`, `npm run test:render:meta`), Astro pages in `src/pages/`, `dist/` measured after `npx astro build`.

**Spec:** `docs/superpowers/specs/2026-09-09-de-optimisation-evidence-pass-design.md` (Strategy A approved 2026-09-09).

**Non-negotiables carried from CLAUDE.md:** work on `main`; commit and push after every build; every rendered-output change ends with `python3 scripts/indexnow_submit.py <slug>` after the deploy is live; never invent a credential, a licence number or a review name; NOT FETCHED is written, never inferred; sections stay.

---

## File Structure

| File | Responsibility |
|---|---|
| `sessions/2026-09-09-evidence-pass-baseline.md` | RED record: what a subagent does to a homepage section under today's rules, rationalisations verbatim |
| `data/quality/evidence-budgets.json` | per-page-type term ceilings and the superlative list; calibrated in Sprint 0, proposals until then |
| `data/quality/evidence-ledger.json` | one row per assertable claim: proof object path or `NOT FETCHED`, breeder-confirmed date |
| `scripts/evidence_audit.py` | the mechanical gate over `dist/`: term budgets · title length · review attribution · claim binding · statement labels · NOT FETCHED in prose · unsourced superlatives; exit 1 on ERROR |
| `tests/test_evidence_audit.py` | pytest RED fixtures for every check in the script |
| `src/components/cag-library/StatementLabel.astro` | the Fact / Observed here / Our recommendation label |
| `tests/render/checks/sem.ts` | + `sem-statement-label-visible` render check |
| `tests/render/fixtures/known_broken/sem-statement-label-visible.html`, `known_good/…` | fixture pair the meta gate must fire on |
| `scripts/quality_report.py` | `registry_check_ids()` also reads ids from `scripts/evidence_audit.py` so the four new `enforced: test` rows are not reported as broken links |
| `data/quality/rule-index.json` | four new rows |
| `skills/cag-evidence-pass.md` | the skill (flat `.md`, like every sibling; `register_skills.py --copy` mirrors it) |
| `data/reviews.json` + `scripts/sweep_review_attribution.py` + `tests/test_review_attribution.py` | single source of truth for review quote→name, and the sweep that applies it to every page |
| `docs/reference/WORKFLOW.md`, `.claude/agents/cag-keyword-verifier.md`, `docs/reference/seo-rules.md`, `.claude/agents/cag-meta-description-agent.md`, `rules/headings.md`, `scripts/final_page_audit.py` | the six rule changes |
| `src/pages/index.astro` | the homepage pass |

---

### Task 1: RED baseline — record what an agent does today (writing-skills Iron Law)

**Files:**
- Create: `sessions/2026-09-09-evidence-pass-baseline.md`

- [ ] **Step 1: Extract the two test sections from the homepage source**

Run:
```bash
sed -n '/<section id="trust"/,/<section id="reviews-mid"/p' src/pages/index.astro > /tmp/trust-section.astro
sed -n '/<section id="congo"/,/<section id="timneh"/p' src/pages/index.astro > /tmp/congo-section.astro
wc -l /tmp/trust-section.astro /tmp/congo-section.astro
```
Expected: two non-empty files (roughly 25 and 47 lines).

- [ ] **Step 2: Dispatch the baseline subagent WITHOUT the skill**

Use the Agent tool, `subagent_type: general-purpose`, with exactly this prompt (paste the two files' contents where marked):

```
You are improving one section of the CongoAfricanGreys.com homepage for SEO, AEO and conversions.
House rules in force: .claude/agents/cag-keyword-verifier.md (a page under 85 keyword mentions is UNDER-OPTIMIZED),
docs/reference/seo-rules.md Rule 57 (150+ entity mentions per full page), skills/cag-aeo-pass.md (one declarative per H2,
named entities over pronouns), rules/headings.md (≥5 H5 and ≥5 H6 per page).
Read those four files. Then rewrite the section below so it scores better on every one of them.
Return the rewritten section and, separately, a numbered list of every change you made and WHY you made it.

<section A: trust>
[contents of /tmp/trust-section.astro]
<section B: congo>
[contents of /tmp/congo-section.astro]
```

- [ ] **Step 3: Measure the subagent's output**

Save the returned sections to `/tmp/baseline-trust.astro` and `/tmp/baseline-congo.astro`, then run:
```bash
for f in /tmp/trust-section.astro /tmp/baseline-trust.astro /tmp/congo-section.astro /tmp/baseline-congo.astro; do
  printf "%-32s words=%-5s CITES=%-3s USDA=%-3s DNA=%-3s C.A.Gs=%-3s\n" "$(basename $f)" \
    "$(sed 's/<[^>]*>//g' $f | wc -w | tr -d ' ')" \
    "$(grep -o -i 'CITES' $f | wc -l | tr -d ' ')" "$(grep -o 'USDA' $f | wc -l | tr -d ' ')" \
    "$(grep -o 'DNA' $f | wc -l | tr -d ' ')" "$(grep -o 'C\.A\.Gs' $f | wc -l | tr -d ' ')"
done
```
Expected: the baseline files carry MORE mentions than the originals. If they carry fewer, record that too; the baseline is whatever happened.

- [ ] **Step 4: Write the baseline record**

Create `sessions/2026-09-09-evidence-pass-baseline.md`:
```markdown
# Evidence Pass — RED baseline (2026-09-09)

Method: one general-purpose subagent, no skill, told to improve two homepage sections under the four
rules in force today. Sections: `trust`, `congo`. Prompt in docs/superpowers/plans/2026-09-09-evidence-pass.md Task 1.

## Before / after counts
| section | words before | words after | CITES | USDA | DNA | C.A.Gs |
|---|---|---|---|---|---|---|
| trust | … | … | …→… | …→… | …→… | …→… |
| congo | … | … | …→… | …→… | …→… | …→… |

## Rationalisations, verbatim (from the subagent's numbered list)
1. "…"
2. "…"

## Pattern
(one paragraph: which rule each rationalisation cites, and what the skill must say to close it)
```
Fill every cell from Step 3 and every quote from the subagent's list. No cell may stay as `…`.

- [ ] **Step 5: Commit**

```bash
git add sessions/2026-09-09-evidence-pass-baseline.md
git commit -m "test(evidence-pass): RED baseline — subagent behaviour on two homepage sections under today's rules

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```

---

### Task 2: Budgets and ledger data files

**Files:**
- Create: `data/quality/evidence-budgets.json`
- Create: `data/quality/evidence-ledger.json`

- [ ] **Step 1: Write the budgets file**

`data/quality/evidence-budgets.json`:
```json
{
  "_comment": "Per-page-type ceilings on trust-concept mentions inside <main>. PROPOSALS from the 2026-09-09 spec until Sprint 0 calibrates them against the pages Perplexity/AIO actually cited (record the calibration date in `calibrated`). A term absent from a page type's map has no ceiling. `scam_owner` / `legit_owner` are the only slugs allowed to exceed the scam/legit ceilings.",
  "calibrated": null,
  "title_max_chars": 70,
  "scam_owner": ["how-to-avoid-african-grey-parrot-scams"],
  "legit_owner": ["trusted-african-grey-parrot-breeders"],
  "superlatives": ["world's best", "best talking", "smartest", "most apartment-friendly", "america's trusted", "america's most trusted", "the best breeder", "wins"],
  "terms": {
    "C.A.Gs": "C\\.A\\.Gs",
    "CITES": "CITES",
    "Appendix I": "Appendix\\s+I\\b",
    "DNA": "\\bDNA\\b",
    "captive-bred": "captive[- ]bred",
    "USDA": "USDA",
    "Midland": "Midland",
    "scam": "scam",
    "legit": "legit"
  },
  "budgets": {
    "home":       {"C.A.Gs": 20, "CITES": 6, "Appendix I": 2, "DNA": 6, "captive-bred": 6, "USDA": 4, "Midland": 5, "scam": 2, "legit": 0},
    "for-sale":   {"C.A.Gs": 15, "CITES": 5, "Appendix I": 2, "DNA": 6, "captive-bred": 5, "USDA": 3, "Midland": 4, "scam": 2, "legit": 0},
    "bird":       {"C.A.Gs": 12, "CITES": 4, "Appendix I": 1, "DNA": 5, "captive-bred": 3, "USDA": 2, "Midland": 3, "scam": 1, "legit": 0},
    "comparison": {"C.A.Gs": 12, "CITES": 4, "Appendix I": 1, "DNA": 4, "captive-bred": 3, "USDA": 2, "Midland": 3, "scam": 1, "legit": 0},
    "location":   {"C.A.Gs": 10, "CITES": 3, "Appendix I": 1, "DNA": 3, "captive-bred": 3, "USDA": 2, "Midland": 4, "scam": 1, "legit": 0},
    "interior":   {"C.A.Gs": 12, "CITES": 4, "Appendix I": 1, "DNA": 4, "captive-bred": 3, "USDA": 2, "Midland": 3, "scam": 1, "legit": 0},
    "blog":       {"C.A.Gs": 8,  "CITES": 3, "Appendix I": 1, "DNA": 3, "captive-bred": 2, "USDA": 1, "Midland": 2, "scam": 1, "legit": 0},
    "hub":        {"C.A.Gs": 10, "CITES": 3, "Appendix I": 1, "DNA": 3, "captive-bred": 3, "USDA": 2, "Midland": 3, "scam": 1, "legit": 0}
  }
}
```

- [ ] **Step 2: Write the ledger file**

`data/quality/evidence-ledger.json` — every claim the Verified-Claim Ledger allows, with its proof object. All proof paths are `NOT FETCHED` today; the breeder supplies each one.
```json
{
  "_comment": "Claim → proof object. `pattern` is the regex evidence_audit.py uses to find the claim in <main>. `proof` is a site-relative path to a redacted document image/PDF the page must link to (href or <img src>) wherever the claim is made more than once, or the literal string NOT FETCHED. `anchor` is the section id on the homepage that owns the claim. `confirmed` is the breeder confirmation date for the proof object, null until supplied.",
  "claims": [
    {"id": "usda-awa",       "pattern": "USDA(?:\\s+AWA)?[- ]licen[cs]ed|USDA\\s+Animal\\s+Welfare", "proof": "NOT FETCHED", "anchor": "trust", "confirmed": null},
    {"id": "cites-docs",     "pattern": "CITES[- ]document(?:ed|ation)|CITES\\s+(?:paperwork|permit|certificate)", "proof": "NOT FETCHED", "anchor": "trust", "confirmed": null},
    {"id": "dna-sexing",     "pattern": "DNA[- ]sex(?:ed|ing)|DNA[- ]tested", "proof": "NOT FETCHED", "anchor": "health", "confirmed": null},
    {"id": "avian-vet-cert", "pattern": "avian[- ]vet(?:erinarian)?\\s+(?:health\\s+)?certif|health\\s+certificate", "proof": "NOT FETCHED", "anchor": "health", "confirmed": null},
    {"id": "pbfd-apv-pcr",   "pattern": "PBFD|Polyomavirus|\\bAPV\\b", "proof": "NOT FETCHED", "anchor": "health", "confirmed": null},
    {"id": "hatch-band",     "pattern": "hatch\\s+certificate|closed\\s+band|band\\s+number", "proof": "NOT FETCHED", "anchor": "trust", "confirmed": null}
  ]
}
```

- [ ] **Step 3: Validate both files parse**

Run: `python3 -c "import json;json.load(open('data/quality/evidence-budgets.json'));json.load(open('data/quality/evidence-ledger.json'));print('ok')"`
Expected: `ok`

- [ ] **Step 4: Commit**

```bash
git add data/quality/evidence-budgets.json data/quality/evidence-ledger.json
git commit -m "data(quality): evidence budgets (proposed) + claim→proof ledger (all NOT FETCHED)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```

---

### Task 3: `evidence_audit.py` — the mechanical gate, TDD

**Files:**
- Create: `scripts/evidence_audit.py`
- Create: `tests/test_evidence_audit.py`

- [ ] **Step 1: Write the failing tests**

`tests/test_evidence_audit.py`:
```python
# tests/test_evidence_audit.py
#
# RED fixtures for the evidence gate. Every threshold traces to a measurement on the
# built site on 2026-09-09 (docs/superpowers/specs/2026-09-09-de-optimisation-evidence-pass-design.md §2):
#   - homepage <main>: CITES x44, C.A.Gs x66, DNA x40 against a proposed ceiling of 6/20/6
#   - the same review text credited to two names on one page (Hutter/Obrien, Schroder/Kempf)
#   - homepage <title> 233 chars against a 70-char ceiling
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import evidence_audit as E

BUDGETS = {
    "title_max_chars": 70,
    "scam_owner": ["how-to-avoid-african-grey-parrot-scams"],
    "legit_owner": ["trusted-african-grey-parrot-breeders"],
    "superlatives": ["world's best", "america's trusted"],
    "terms": {"CITES": "CITES", "scam": "scam", "legit": "legit"},
    "budgets": {"home": {"CITES": 2, "scam": 1, "legit": 0}},
}
LEDGER = {"claims": [
    {"id": "usda-awa", "pattern": "USDA[- ]licensed", "proof": "/proof/usda-redacted.webp", "anchor": "trust", "confirmed": "2026-09-09"},
    {"id": "dna-sexing", "pattern": "DNA[- ]sexed", "proof": "NOT FETCHED", "anchor": "health", "confirmed": None},
]}

def page(main, title="Short Title"):
    return f"<html><head><title>{title}</title></head><body><main>{main}</main></body></html>"


def test_term_budget_flags_overrun_and_names_the_term():
    html = page("<p>CITES CITES CITES</p>")
    f = E.term_budget(html, "home", BUDGETS)
    assert f == [("CITES", 3, 2)]


def test_term_budget_is_silent_within_budget():
    assert E.term_budget(page("<p>CITES once. CITES twice.</p>"), "home", BUDGETS) == []


def test_scam_owner_page_is_exempt_from_the_scam_ceiling():
    html = page("<p>scam scam scam scam</p>")
    assert E.term_budget(html, "interior", BUDGETS, slug="how-to-avoid-african-grey-parrot-scams") == []
    assert E.term_budget(html, "home", BUDGETS, slug="index") == [("scam", 4, 1)]


def test_title_length_flags_the_233_char_style():
    long = "A | " * 60
    assert E.title_too_long(page("<p>x</p>", title=long), BUDGETS) is not None
    assert E.title_too_long(page("<p>x</p>", title="African Grey Breeder in Midland, Texas"), BUDGETS) is None


def test_review_attribution_flags_same_quote_two_names():
    html = page(
        '<blockquote><p>I searched for months before finding C.A.Gs. Truly top notch.</p><cite>Clifford Hutter</cite></blockquote>'
        '<blockquote><p>I searched for months before finding C.A.Gs. Truly top notch.</p><cite>Archie Obrien</cite></blockquote>')
    bad = E.review_attribution(html)
    assert len(bad) == 1 and {"Clifford Hutter", "Archie Obrien"} <= set(bad[0][1])


def test_review_attribution_accepts_same_quote_same_name_twice():
    html = page(
        '<blockquote><p>Flawless from start to finish.</p><cite>Richard Woodard</cite></blockquote>'
        '<blockquote><p>Flawless from start to finish.</p><cite>Richard Woodard</cite></blockquote>')
    assert E.review_attribution(html) == []


def test_claim_binding_flags_repeated_claim_without_proof_link():
    html = page("<p>USDA-licensed.</p><p>USDA-licensed again.</p>")
    unbound = E.claim_binding(html, LEDGER)
    assert [u[0] for u in unbound] == ["usda-awa"]


def test_claim_binding_accepts_repeated_claim_when_proof_is_linked():
    html = page('<p>USDA-licensed.</p><p>USDA-licensed. <a href="/proof/usda-redacted.webp">See the licence</a></p>')
    assert E.claim_binding(html, LEDGER) == []


def test_claim_binding_reports_not_fetched_proof_as_warn_not_error():
    html = page("<p>DNA-sexed.</p><p>DNA-sexed.</p>")
    out = E.claim_binding(html, LEDGER)
    assert out == [("dna-sexing", 2, "NOT FETCHED")]


def test_statement_labels_required_where_species_claims_appear():
    html = page("<section id='congo'><h2>Congo</h2><p>Psittacus erithacus lives 40 to 60 years.</p></section>")
    assert E.missing_statement_labels(html) == ["congo"]
    labelled = page("<section id='congo'><h2>Congo</h2><p><span class='stmt-label' data-kind='fact'>Fact</span> Psittacus erithacus lives 40 to 60 years.</p></section>")
    assert E.missing_statement_labels(labelled) == []


def test_not_fetched_never_reaches_prose():
    assert E.not_fetched_in_prose(page("<p>Licence number: NOT FETCHED</p>")) == 1
    assert E.not_fetched_in_prose(page("<p>Licence on file.</p>")) == 0


def test_superlatives_are_flagged_unless_sourced_in_the_same_sentence():
    assert E.unsourced_superlatives(page("<p>The world's best talking parrot.</p>"), BUDGETS) == ["world's best"]
    sourced = page("<p>The world's best talking parrot, per <a href='https://example.org/study'>Pepperberg 1999</a>.</p>")
    assert E.unsourced_superlatives(sourced, BUDGETS) == []


def test_audit_returns_error_on_budget_breach_and_exit_code_follows():
    html = page("<p>CITES CITES CITES</p>")
    findings = E.audit("index", html, "home", BUDGETS, LEDGER)
    assert any(sev == "ERROR" and "CITES" in msg for sev, msg in findings)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_evidence_audit.py -q 2>&1 | tail -3`
Expected: `ModuleNotFoundError: No module named 'evidence_audit'` (collection error).

- [ ] **Step 3: Write the audit script**

`scripts/evidence_audit.py`:
```python
#!/usr/bin/env python3
"""
Evidence audit — the measurable half of skills/cag-evidence-pass.md.

Asks of a built page: does it PROVE what it asserts, or merely repeat it?
Runs over dist/ (the rendered page, never the source).

Checks (ids are the rule-index ids):
  term-budget-per-page        trust-concept mentions in <main> vs data/quality/evidence-budgets.json
  title-length-max            <title> length vs title_max_chars
  review-attribution-unique   the same review text credited to two different names on one page
  claim-bound-to-proof        a ledger claim made 2+ times must link its proof object (ERROR);
                              a claim whose proof is NOT FETCHED is a WARN, never silently a pass
  statement-labels-present    sections carrying species/health/comparison facts carry a .stmt-label
  no-not-fetched-in-prose     the literal NOT FETCHED never ships in visible text
  no-unsourced-superlatives   "world's best" etc. without a link in the same sentence

Per skills/cag-gate-integrity.md: term counts are exact; the label and superlative checks are
PROXIES (a regex cannot judge whether a sentence is a species fact). Read a flagged section
before rewriting it, and read the examined count: `0 pages matched` is not a pass.

Usage:
  python3 scripts/evidence_audit.py <slug> [<slug> ...] [--type home|for-sale|bird|comparison|location|interior|blog|hub]
  python3 scripts/evidence_audit.py --all
Exit 1 on any ERROR, or if the slug filter matched nothing.
"""
import re, sys, json, glob, pathlib, argparse
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUDGETS_PATH = ROOT / "data" / "quality" / "evidence-budgets.json"
LEDGER_PATH = ROOT / "data" / "quality" / "evidence-ledger.json"
TARGETS_PATH = ROOT / "tests" / "render" / "targets.json"

CHECK_IDS = [
    {"id": "term-budget-per-page"},
    {"id": "title-length-max"},
    {"id": "review-attribution-unique"},
    {"id": "claim-bound-to-proof"},
    {"id": "statement-labels-present"},
    {"id": "no-not-fetched-in-prose"},
    {"id": "no-unsourced-superlatives"},
]

FACT_SIGNAL = re.compile(
    r"Psittacus\s+(?:erithacus|timneh)|\b\d{2}\s*(?:to|–|-)\s*\d{2}\s+years|lifespan|"
    r"hypocalc|calcium|vitamin\s+D3|UV-?B|PBFD|Polyomavirus|psittacosis|IUCN|Appendix\s+I\b", re.I)


def strip_tags(html):
    html = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", html)


def unescape(t):
    for a, b in (("&amp;", "&"), ("&nbsp;", " "), ("&#39;", "'"), ("&rsquo;", "’"),
                 ("&#8217;", "’"), ("&quot;", '"'), ("&mdash;", "—"), ("&ndash;", "–")):
        t = t.replace(a, b)
    return t


def main_html(html):
    m = re.search(r"<main\b.*?</main>", html, flags=re.S | re.I)
    return m.group(0) if m else html


def text_of(html):
    return re.sub(r"\s+", " ", unescape(strip_tags(html))).strip()


# ── term-budget-per-page ────────────────────────────────────────────────────
def term_budget(html, page_type, budgets, slug=""):
    """[(term, count, ceiling)] for every term over its ceiling. Owner pages are exempt for their term."""
    text = text_of(main_html(html))
    ceilings = budgets["budgets"].get(page_type, {})
    out = []
    for term, ceiling in ceilings.items():
        if term == "scam" and slug in budgets.get("scam_owner", []):
            continue
        if term == "legit" and slug in budgets.get("legit_owner", []):
            continue
        pat = budgets["terms"].get(term, re.escape(term))
        n = len(re.findall(pat, text, flags=re.I))
        if n > ceiling:
            out.append((term, n, ceiling))
    return out


# ── title-length-max ────────────────────────────────────────────────────────
def title_too_long(html, budgets):
    m = re.search(r"<title>(.*?)</title>", html, flags=re.S | re.I)
    if not m:
        return None
    t = text_of(m.group(1))
    limit = budgets.get("title_max_chars", 70)
    return (len(t), limit) if len(t) > limit else None


# ── review-attribution-unique ───────────────────────────────────────────────
QUOTE_BLOCK = re.compile(r"<(blockquote|figure|article|li|div)\b[^>]*>(.*?)</\1>", re.S | re.I)
CITE = re.compile(r"<(?:cite|footer|p|span)\b[^>]*class=\"[^\"]*(?:name|author|cite)[^\"]*\"[^>]*>(.*?)</|<cite\b[^>]*>(.*?)</cite>", re.S | re.I)


def review_attribution(html):
    """[(quote_fingerprint, [names])] where one quote text is credited to 2+ different names."""
    seen = defaultdict(set)
    for _, inner in QUOTE_BLOCK.findall(main_html(html)):
        names = [text_of(a or b) for a, b in CITE.findall(inner)]
        if not names:
            continue
        body = text_of(re.sub(r"<cite\b.*?</cite>", " ", inner, flags=re.S | re.I))
        body = re.sub(r"\s*(?:" + "|".join(re.escape(n) for n in names) + r")\s*$", "", body)
        fp = re.sub(r"[^a-z]", "", body.lower())[:80]
        if len(fp) < 20:
            continue
        seen[fp].add(names[0])
    return [(fp, sorted(n)) for fp, n in seen.items() if len(n) > 1]


# ── claim-bound-to-proof ────────────────────────────────────────────────────
def claim_binding(html, ledger):
    """[(claim_id, mentions, proof)] for ledger claims made 2+ times whose proof is not linked.

    proof == "NOT FETCHED" rows are returned so the caller can WARN; a linked proof clears the row.
    """
    body = main_html(html)
    text = text_of(body)
    out = []
    for c in ledger["claims"]:
        n = len(re.findall(c["pattern"], text, flags=re.I))
        if n < 2:
            continue
        proof = c.get("proof") or "NOT FETCHED"
        if proof != "NOT FETCHED" and (proof in body):
            continue
        out.append((c["id"], n, proof))
    return out


# ── statement-labels-present ────────────────────────────────────────────────
SECTION = re.compile(r"<section\b[^>]*\bid=\"([^\"]+)\"[^>]*>(.*?)</section>", re.S | re.I)


def missing_statement_labels(html):
    """Section ids whose text carries a species/health fact signal but no .stmt-label. PROXY."""
    out = []
    for sid, inner in SECTION.findall(main_html(html)):
        if FACT_SIGNAL.search(text_of(inner)) and "stmt-label" not in inner:
            out.append(sid)
    return out


# ── no-not-fetched-in-prose ─────────────────────────────────────────────────
def not_fetched_in_prose(html):
    return len(re.findall(r"NOT FETCHED", text_of(main_html(html))))


# ── no-unsourced-superlatives ───────────────────────────────────────────────
def unsourced_superlatives(html, budgets):
    out = []
    body = main_html(html)
    sentences = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", unescape(body)))
    for s in sentences:
        plain = text_of(s).lower()
        for sup in budgets.get("superlatives", []):
            if sup in plain and "href=" not in s:
                out.append(sup)
    return out


# ── the audit ───────────────────────────────────────────────────────────────
def audit(slug, html, page_type, budgets, ledger):
    f = []
    for term, n, cap in term_budget(html, page_type, budgets, slug):
        f.append(("ERROR", f"term budget: {term} x{n} in <main>, ceiling {cap} for {page_type}"))
    t = title_too_long(html, budgets)
    if t:
        f.append(("ERROR", f"<title> is {t[0]} chars, ceiling {t[1]}"))
    for fp, names in review_attribution(html):
        f.append(("ERROR", f"same review text credited to {' / '.join(names)} (fingerprint {fp[:24]}…)"))
    for cid, n, proof in claim_binding(html, ledger):
        if proof == "NOT FETCHED":
            f.append(("WARN", f"claim '{cid}' made {n}x; proof object NOT FETCHED — say it once and link the trust section"))
        else:
            f.append(("ERROR", f"claim '{cid}' made {n}x without linking its proof {proof}"))
    for sid in missing_statement_labels(html):
        f.append(("WARN", f"section #{sid} carries species/health facts with no statement label (PROXY — read it)"))
    nf = not_fetched_in_prose(html)
    if nf:
        f.append(("ERROR", f"'NOT FETCHED' appears {nf}x in visible text"))
    for sup in unsourced_superlatives(html, budgets):
        f.append(("WARN", f"unsourced superlative: '{sup}' (source it in the same sentence or cut it)"))
    return f


def page_type_for(slug):
    """targets.json first; then a path heuristic; 'interior' as the fallback."""
    try:
        for p in json.load(open(TARGETS_PATH))["pages"]:
            if p["slug"] == slug:
                return p["page_type"]
    except Exception:
        pass
    if slug == "index":
        return "home"
    if slug.startswith("available/"):
        return "bird"
    if slug.startswith("blog/"):
        return "blog"
    if re.search(r"-for-sale-[a-z-]+$", slug) or slug.endswith("-near-me"):
        return "location"
    if "-vs-" in slug or slug.endswith("-comparison"):
        return "comparison"
    if "for-sale" in slug:
        return "for-sale"
    return "interior"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--type", default=None, help="override the page type for every slug given")
    a = ap.parse_args(argv)
    budgets = json.load(open(BUDGETS_PATH))
    ledger = json.load(open(LEDGER_PATH))
    dist = ROOT / "dist"
    if a.all:
        paths = sorted(dist.glob("**/index.html"))
    else:
        paths = [dist / ("" if s == "index" else s) / "index.html" for s in a.slugs]
    paths = [p for p in paths if p.exists()]
    if not paths:
        print("0 pages matched — that is not a pass")
        return 1
    errs = 0
    for p in paths:
        rel = p.relative_to(dist).as_posix()
        slug = "index" if rel == "index.html" else rel[: -len("/index.html")]
        pt = a.type or page_type_for(slug)
        html = p.read_text(encoding="utf-8", errors="ignore")
        f = audit(slug, html, pt, budgets, ledger)
        e = sum(1 for s, _ in f if s == "ERROR")
        errs += e
        print(f"\n== {slug}  [{pt}]  {e} ERROR / {len(f) - e} WARN")
        for sev, msg in f:
            print(f"  {sev:5s} {msg}")
    print(f"\n{errs} ERROR across {len(paths)} pages")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_evidence_audit.py -q 2>&1 | tail -3`
Expected: `13 passed`.

If `test_review_attribution_flags_same_quote_two_names` fails, the `<cite>` regex missed the name; print `CITE.findall(inner)` inside the test to see what was captured before changing the pattern.

- [ ] **Step 5: Run it on the real homepage and confirm it reproduces the spec's measurements**

Run: `npx astro build >/dev/null 2>&1; python3 scripts/evidence_audit.py index`
Expected (numbers must match §2 of the spec, ±0):
```
== index  [home]  N ERROR / M WARN
  ERROR term budget: C.A.Gs x66 in <main>, ceiling 20 for home
  ERROR term budget: CITES x44 in <main>, ceiling 6 for home
  ERROR term budget: DNA x40 …
  ERROR <title> is 233 chars, ceiling 70
  …
```
If the review-attribution ERROR does NOT appear on the homepage, the Testimonials component does not use `<cite>`/`class="name"`; open `src/components/cag-library/Testimonials.astro`, find the element that prints `name`, and add that element's tag/class to `CITE`. Then re-run. The gate must fire on the known-real defect before it is trusted (cag-gate-integrity).

- [ ] **Step 6: Commit**

```bash
git add scripts/evidence_audit.py tests/test_evidence_audit.py
git commit -m "feat(quality): evidence_audit.py — term budgets, claim→proof binding, review attribution, labels, title length (TDD)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```

---

### Task 4: Wire the four rules into `rule-index.json` and `quality_report.py`

**Files:**
- Modify: `scripts/quality_report.py:41-46` (`registry_check_ids`)
- Modify: `data/quality/rule-index.json`
- Modify: `tests/test_quality_report.py`

- [ ] **Step 1: Write the failing test**

Append to `tests/test_quality_report.py`:
```python
def test_registry_check_ids_include_python_audit_ids(tmp_path):
    import quality_report as Q
    ids = Q.registry_check_ids()
    assert "term-budget-per-page" in ids, "evidence_audit.py ids must count as backing tests"
    assert "review-attribution-unique" in ids
```
(If the file does not already import `quality_report` via `sys.path.insert(0, …/scripts)`, add the same two lines the file's other tests use at the top.)

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m pytest tests/test_quality_report.py -q -k python_audit 2>&1 | tail -3`
Expected: `AssertionError: evidence_audit.py ids must count as backing tests`.

- [ ] **Step 3: Extend `registry_check_ids`**

In `scripts/quality_report.py`, replace the function body:
```python
PY_AUDIT_ID_RE = re.compile(r"""\{\s*"id":\s*"([a-z0-9-]+)"\s*\}""")


def registry_check_ids(checks_dir: pathlib.Path = CHECKS_DIR) -> set:
    ids = set()
    for p in sorted(checks_dir.glob("*.ts")):
        ids |= check_ids_from_source(p.read_text())
    # Python audits declare their ids as CHECK_IDS = [{"id": "..."}, ...]; they back
    # `enforced: test` rows the same way a checks/*.ts id does.
    for p in sorted((ROOT / "scripts").glob("*_audit.py")):
        ids |= set(PY_AUDIT_ID_RE.findall(p.read_text()))
    return ids
```

- [ ] **Step 4: Add the four rule rows**

Append to the `rules` array in `data/quality/rule-index.json` (keep valid JSON — add a comma after the previous last object):
```json
    {"id": "term-budget-per-page", "family": "COPY", "enforced": "test", "test": "scripts/evidence_audit.py::term-budget-per-page", "severity": "blocking", "pack": "rules/copy.md"},
    {"id": "claim-bound-to-proof", "family": "COPY", "enforced": "test", "test": "scripts/evidence_audit.py::claim-bound-to-proof", "severity": "blocking", "pack": "rules/copy.md"},
    {"id": "statement-labels-present", "family": "COPY", "enforced": "test", "test": "scripts/evidence_audit.py::statement-labels-present", "severity": "advisory", "pack": "rules/copy.md"},
    {"id": "review-attribution-unique", "family": "COPY", "enforced": "test", "test": "scripts/evidence_audit.py::review-attribution-unique", "severity": "blocking", "pack": "rules/copy.md"}
```
Match the key set of the existing rows exactly (open the file and copy the keys of `img-srcset-within-2x`; drop `pack` if existing rows do not carry it).

- [ ] **Step 5: Run the tests and the report**

Run: `python3 -m pytest tests/test_quality_report.py -q 2>&1 | tail -2 && python3 scripts/quality_report.py | grep -i -A6 'broken'`
Expected: all tests pass; the report's broken-test-link list does not name any of the four new ids.

- [ ] **Step 6: Commit**

```bash
git add scripts/quality_report.py data/quality/rule-index.json tests/test_quality_report.py
git commit -m "chore(quality): rule-index rows for the evidence gate; quality_report reads ids from *_audit.py

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```

---

### Task 5: `StatementLabel` component + render check + fixture pair

**Files:**
- Create: `src/components/cag-library/StatementLabel.astro`
- Modify: `tests/render/checks/sem.ts` (append one `register`)
- Create: `tests/render/fixtures/known_broken/sem-statement-label-visible.html`
- Create: `tests/render/fixtures/known_good/sem-statement-label-visible.html`

- [ ] **Step 1: Write the fixture pair (the failing test for the render check)**

`tests/render/fixtures/known_broken/sem-statement-label-visible.html`:
```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>label present but hidden</title>
<style>.stmt-label{display:none}</style></head><body>
<main>
  <h1>Congo African Greys</h1>
  <section id="congo">
    <h2>What Is a Congo African Grey?</h2>
    <p><span class="stmt-label" data-kind="fact">Fact</span> Psittacus erithacus lives 40 to 60 years in captivity.</p>
    <p><span class="stmt-label" data-kind="observed">Observed here</span> Our chicks wean between 12 and 16 weeks.</p>
  </section>
</main>
</body></html>
```

`tests/render/fixtures/known_good/sem-statement-label-visible.html`:
```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>labels visible</title>
<style>.stmt-label{display:inline-block;font:600 11px/1 system-ui;letter-spacing:.06em;text-transform:uppercase;padding:3px 7px;border-radius:4px;background:#E3EEE8;color:#2D6A4F}</style></head><body>
<main>
  <h1>Congo African Greys</h1>
  <section id="congo">
    <h2>What Is a Congo African Grey?</h2>
    <p><span class="stmt-label" data-kind="fact">Fact</span> Psittacus erithacus lives 40 to 60 years in captivity.</p>
    <p><span class="stmt-label" data-kind="observed">Observed here</span> Our chicks wean between 12 and 16 weeks.</p>
  </section>
</main>
</body></html>
```

- [ ] **Step 2: Run the meta gate to see the new fixtures are orphaned**

Run: `npm run test:render:meta 2>&1 | tail -5`
Expected: the run does not mention `sem-statement-label-visible` at all (no check registered yet). That is the RED state: a fixture with no check.

- [ ] **Step 3: Register the check**

Append to `tests/render/checks/sem.ts`:
```ts
register({
  id: 'sem-statement-label-visible',
  family: 'SEM',
  severity: 'advisory',
  describe: 'every .stmt-label (Fact / Observed here / Our recommendation) is painted, with a data-kind',
  minExamined: 2,
  async run(page: Page, viewport: number): Promise<CheckResult> {
    const r = await page.evaluate(() => {
      const labels = Array.from(document.querySelectorAll<HTMLElement>('main .stmt-label'));
      const bad: string[] = [];
      for (const l of labels) {
        const rect = l.getBoundingClientRect();
        const cs = getComputedStyle(l);
        const painted = rect.width > 0 && rect.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none';
        const kind = l.dataset.kind || '';
        if (!painted) bad.push(`hidden: "${l.textContent?.trim()}"`);
        else if (!['fact', 'observed', 'recommendation'].includes(kind)) bad.push(`bad data-kind "${kind}"`);
      }
      return { examined: labels.length, bad };
    });
    return {
      examined: r.examined,
      defects: r.bad.length
        ? [{ checkId: 'sem-statement-label-visible', family: 'SEM' as const, viewport, count: r.bad.length, message: r.bad.join(' | ') }]
        : [],
    };
  },
});
```

- [ ] **Step 4: Run the meta gate; both fixtures must behave**

Run: `npm run test:render:meta 2>&1 | grep -E 'sem-statement-label-visible|passed|failed' | tail -8`
Expected: `sem-statement-label-visible [SEM] › fires on the known_broken fixture` passes and `… passes on the known_good fixture` passes at every viewport; overall `N passed`.

- [ ] **Step 5: Write the component**

`src/components/cag-library/StatementLabel.astro`:
```astro
---
/**
 * StatementLabel — separates the three kinds of statement the site makes.
 *   fact           sourced species / legal / health fact  → pass `source` (URL) and it renders as a link
 *   observed       something Mark & Teri have seen here    → pass `n` (birds) and `since` (year) when known
 *   recommendation our advice, labelled as ours
 * Renders inline at the start of the sentence it labels. Never used on marketing copy.
 */
interface Props { kind: 'fact' | 'observed' | 'recommendation'; source?: string; n?: number; since?: number }
const { kind, source, n, since } = Astro.props;
const text = kind === 'fact' ? 'Fact' : kind === 'observed' ? 'Observed here' : 'Our recommendation';
const detail = kind === 'observed' && (n || since) ? ` · ${n ? `${n} birds` : ''}${n && since ? ', ' : ''}${since ? `since ${since}` : ''}` : '';
---
{kind === 'fact' && source
  ? <a class="stmt-label" data-kind="fact" href={source} target="_blank" rel="noopener">{text} ↗</a>
  : <span class="stmt-label" data-kind={kind}>{text}{detail}</span>}
<style is:global>
  .stmt-label{display:inline-block;font:600 11px/1 'Sora',system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;padding:3px 7px;border-radius:4px;margin-right:6px;vertical-align:middle;text-decoration:none}
  .stmt-label[data-kind="fact"]{background:#E3EEE8;color:#2D6A4F}
  .stmt-label[data-kind="observed"]{background:#FBE7E2;color:#9C3A2A}
  .stmt-label[data-kind="recommendation"]{background:#F0EEE5;color:#4B5A52}
</style>
```
Contrast: `#2D6A4F` on `#E3EEE8` = 5.9:1, `#9C3A2A` on `#FBE7E2` = 5.8:1, `#4B5A52` on `#F0EEE5` = 6.1:1; all pass AA at 11px bold. Palette values are from `DESIGN.md` (Green `#2D6A4F`, Clay-soft `#FBE7E2`, Cream `#F0EEE5`).

- [ ] **Step 6: Commit**

```bash
git add src/components/cag-library/StatementLabel.astro tests/render/checks/sem.ts tests/render/fixtures/known_broken/sem-statement-label-visible.html tests/render/fixtures/known_good/sem-statement-label-visible.html
git commit -m "feat(components): StatementLabel (Fact / Observed here / Our recommendation) + sem-statement-label-visible render check with fixture pair

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```

---

### Task 6: The skill — GREEN against the baseline, then REFACTOR

**Files:**
- Create: `skills/cag-evidence-pass.md`
- Modify: `sessions/2026-09-09-evidence-pass-baseline.md` (append GREEN + REFACTOR runs)

- [ ] **Step 1: Write the skill against the recorded rationalisations**

`skills/cag-evidence-pass.md` (every line of the rationalisation table must quote an entry from Task 1's baseline record; add rows, never delete the ones below):
```markdown
---
name: cag-evidence-pass
description: Use when a CAG page is about to be called done, or when a page repeats CITES / USDA / DNA / C.A.Gs / captive-bred / Midland / scam / legit more than a handful of times, when a credential is asserted but never shown, when species or health facts sit next to breeder opinion with no label, when a review quote might be credited to the wrong buyer, when a title runs past one clause, or when a keyword-count or entity-count rule is pushing copy to say the same thing again. Also use when an AI answer engine quotes a competitor for a fact we state more often than they do.
---

# SKILL: CAG Evidence Pass — Say It Once, Then Prove It

**Run this AFTER `anti-ai-writing` and BEFORE `cag-final-page-pass`.** Hardening asks *does the page render*, the AEO pass asks *can an engine lift a sentence*; this asks *does the page prove what it asserts, or only repeat it*.

```bash
npx astro build
python3 scripts/evidence_audit.py <slug> [<slug> ...]      # slugs LITERALLY; `index` is the homepage
```
`ERROR` = fix before deploy. `WARN` = read the section, then decide. `0 pages matched` is not a pass.

> **Read `skills/cag-gate-integrity.md` first.** Term counts are exact. The statement-label and superlative checks are proxies: confirm a flagged section by reading it.

## Why this gate exists (measured 2026-09-09, `dist/`)
The homepage `<main>` said CITES 44×, C.A.Gs 66×, DNA 40×, "Appendix I" 28× across 8,830 words, and credited one review quote to two different buyers. Not one credential on the site linked to a proof object. Four house rules (keyword floor of 85, "150+ entity mentions", ≥5 H5 + ≥5 H6, title ≤205 "never short") were the cause. The breeder's ruling: **sections stay; repetition goes; proof replaces assertion.**

## The four rules this skill owns
| Rule | What it means on the page |
|---|---|
| **Term budget** (`data/quality/evidence-budgets.json`) | Each trust concept is said where it is load-bearing and nowhere else. Over budget → cut the mention or turn it into a link to the section that owns it. |
| **Claim → proof** (`data/quality/evidence-ledger.json`) | A credential made twice must link its proof object (redacted USDA record, example DNA / vet / CITES certificate). Proof `NOT FETCHED` → say it **once**, in the trust section, and link there from everywhere else. Never write NOT FETCHED in prose. |
| **Statement labels** (`StatementLabel.astro`) | Species, legal and health facts open with **Fact** (+ source link). What we have seen opens with **Observed here** (+ n, since). Advice opens with **Our recommendation**. Marketing copy carries no label and makes no factual claim. |
| **Evidence integrity** | One quote, one name, everywhere (`data/reviews.json` is the source). No invented identifiers. No superlative without a source in the same sentence. Title ≤70 chars, one clause. |

## Procedure, per section (sections are never removed)
1. Count: `python3 scripts/evidence_audit.py <slug>` — note every ERROR term and the section it lives in (grep the built `<main>` by section id).
2. Choose the one load-bearing mention per term per page. The trust section owns credentials; the health section owns screening; the pricing section owns the price.
3. Every other mention becomes either (a) a pronoun / plain noun ("our paperwork", "the certificate"), or (b) a link to the owning section.
4. Wrap each species / legal / health sentence with the right `StatementLabel`. If you cannot name the source for a Fact, it is not a Fact: relabel as Observed here or delete.
5. Re-run the audit. Re-run `python3 scripts/dup_content_audit.py <slug>` — de-repetition must not converge sibling pages.
6. Word count is NOT a target. If it fell, good. If it did not, the page was not repeating; leave it.

## Rationalisations this skill closes (from the 2026-09-09 baseline)
| Excuse | Reality |
|---|---|
| "The keyword-verifier says under 85 mentions is under-optimised" | The floor was deleted 2026-09-09. Only the ceiling exists. Repeating a term is now a defect, not a score. |
| "Rule 57 wants 150+ entity mentions" | Rule 57 now reads 95–105 **distinct** entities, each said once where load-bearing. Mentions are not entities. |
| "The AEO pass wants named entities instead of pronouns" | It wants them **once per section**, at the answer. The 66th "C.A.Gs" is not an entity signal, it is noise. |
| "≥5 H5 and ≥5 H6 need content to sit under them" | The minimum counts no longer apply to the homepage and location pages. Do not write headings to feed a counter. |
| "Repeating CITES Appendix I is compliance-safe" | Saying it once correctly is compliance. Saying it 28 times is a pattern Google's spam guidance names. |
| "The breeder wants trust signals everywhere" | The breeder approved Strategy A: say it once, prove it, move on. Proof is the trust signal. |
| "I'll add the proof link later" | A claim made twice without its proof is an ERROR today. Say it once, or link the trust section now. |
| "This is marketing copy, labels don't apply" | Then it must make no factual claim. A lifespan, a screening test, a legal status is a fact; label it or cut it. |

## Red flags — stop and re-read the procedure
- You are about to add a heading, an FAQ or a paragraph to reach a count.
- You typed a credential you did not read in `credentials.md` or the ledger.
- You wrote a licence number, a study, or a buyer name from memory.
- The audit passed on `0 pages matched`.
- Two review quotes on the page read the same.

## What this skill does not do
It does not write prose (write from the outline: `rules/copy.md` → `write-from-outline-never-from-sibling`). It does not judge AI-tells (`anti-ai-writing`), citability (`cag-aeo-pass`) or sibling overlap (`cag-duplicate-content-gate`). It does not calibrate the budgets: Sprint 0 does, against the pages the engines actually cited.
```

- [ ] **Step 2: Register the skill**

Run: `python3 scripts/register_skills.py --copy && ls .claude/skills/cag-evidence-pass/`
Expected: `SKILL.md`.

- [ ] **Step 3: GREEN — re-run the Task 1 subagent WITH the skill**

Dispatch the same prompt as Task 1 Step 2, with one line added after the house-rules line: `Also read skills/cag-evidence-pass.md and obey it; it supersedes the rules above where they conflict.` Save output to `/tmp/green-trust.astro` and `/tmp/green-congo.astro`, run the Task 1 Step 3 counting loop on them.

Expected: every term count is ≤ the original section's count; the subagent's numbered list cites the budget, the ledger or the label at least once. If it still raised a count, record the sentence it used to justify that in the baseline file and go to Step 4.

- [ ] **Step 4: REFACTOR — close any new rationalisation**

For each new excuse from Step 3, add a row to the skill's rationalisation table, re-run Step 3 once. Append both runs to `sessions/2026-09-09-evidence-pass-baseline.md` under `## GREEN run` and `## REFACTOR run` with the same before/after table format as Task 1 Step 4.

- [ ] **Step 5: Commit**

```bash
git add skills/cag-evidence-pass.md .claude/skills/cag-evidence-pass/SKILL.md sessions/2026-09-09-evidence-pass-baseline.md
git commit -m "feat(skills): cag-evidence-pass — say it once, then prove it (RED→GREEN→REFACTOR recorded)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```

---

### Task 7: Retire the six injector rules

**Files:**
- Modify: `docs/reference/WORKFLOW.md` (Sprint 4 block, lines 471–615)
- Modify: `.claude/agents/cag-keyword-verifier.md:245-249`
- Modify: `docs/reference/seo-rules.md:467-490` (Rules 56, 57)
- Modify: `.claude/agents/cag-meta-description-agent.md:45-61`
- Modify: `rules/headings.md:19`
- Modify: `scripts/final_page_audit.py:74-140` (PROFILES)
- Modify: `tests/test_final_page_audit.py`

- [ ] **Step 1: Failing test for the H5/H6 relaxation**

Append to `tests/test_final_page_audit.py`:
```python
def test_home_and_location_profiles_downgrade_h5_h6_minimums_to_warn():
    import final_page_audit as F
    for pt in ("home", "location"):
        assert F.severity(pt, "min_h5_5") == "WARN", pt
        assert F.severity(pt, "min_h6_5") == "WARN", pt
        assert F.severity(pt, "no_skip") == "FAIL", pt   # skipped levels stay a hard FAIL
```
Run: `python3 -m pytest tests/test_final_page_audit.py -q -k h5_h6 2>&1 | tail -2` → Expected: FAIL (either `KeyError`/fallback returns FAIL, or "home" profile missing).

- [ ] **Step 2: Add the two profiles to `final_page_audit.py`**

Inside `PROFILES = {`, add (copy the `interior` profile's other keys if `_default` is not used by that dict; the two overrides below are the only intended differences):
```python
    "home": {                            # homepage: sections stay, heading minimums do not (evidence pass, 2026-09-09)
        "min_h5_5": "WARN",
        "min_h6_5": "WARN",
        "no_skip": "FAIL",
    },
    "location": {                        # 40 thin state/city pages: depth is filled with real shipments, not headings
        "min_h5_5": "WARN",
        "min_h6_5": "WARN",
        "no_skip": "FAIL",
    },
```
Run: `python3 -m pytest tests/test_final_page_audit.py -q 2>&1 | tail -2` → Expected: all pass.

- [ ] **Step 3: Keyword-verifier: delete the floor**

In `.claude/agents/cag-keyword-verifier.md` replace lines 248–249:
```
- If a full page has <85 total keyword mentions across all types → flag as **UNDER-OPTIMIZED**
- If a full page has >110 total keyword mentions → flag as **OVER-STUFFED**
```
with:
```
- There is **no floor**. A page is never "under-optimized" by count (retired 2026-09-09: the floor manufactured the repetition the evidence pass now fails).
- If a full page has >110 total keyword mentions → flag as **OVER-STUFFED**; trust-concept terms additionally answer to `data/quality/evidence-budgets.json` via `scripts/evidence_audit.py`
```
Also change the `**TOTAL** | **≈85–105**` row to `**TOTAL** | **≤105 (no minimum)**`.

- [ ] **Step 4: seo-rules Rule 56 and 57**

Replace the Rule 57 heading and first line (`docs/reference/seo-rules.md:482-483`):
```
**Rule 57 — 95–105 Distinct Entities (breeder correction 2026-09-09; was "150+ mentions")**
Every full-length page carries 95–105 **distinct** named entities from `skills/cag-entity-agent.md`, each said ONCE where it is load-bearing. Mentions are not entities: a term repeated is a `term-budget-per-page` defect, not a score. Categories and examples below are unchanged.
```
Replace the Rule 56 heading and first line (`:467-468`):
```
**Rule 56 — Keyword Fan-Out Sized to the Competitor (breeder correction 2026-09-09; was a fixed 150–200)**
Before writing, fetch the top-ranking competitor page for the primary keyword (Sprint 0, real fetch, never assumed) and count the keyword variants it actually uses. The page's target is that count **+5 to +10**. Record the competitor URL and its count in the session brief. The 10 categories below still organise the fan-out.
```

- [ ] **Step 5: Meta agent: title ceiling**

In `.claude/agents/cag-meta-description-agent.md` replace `### Format 1 — Standard Long Title (Title ≤ 205 / Desc ≤ 185)` with `### Format 1 — One-Clause Title (Title ≤ 70 / Desc ≤ 160)` and its pattern line (`:57`) with:
```
> **`[What the page is, plainly] – C.A.Gs`** — one clause, ≤70 chars, no pipes, no question stacked on a claim. Example: `African Grey Parrot Breeder in Midland, Texas – C.A.Gs`. (Retired 2026-09-09: the 4-part ≤205 pattern produced a 233-char homepage title.)
```
Delete the `### Format 2 — 4-Part Long Title + Tone (Title ≤ 205 / Desc ≤ 300)` block through the end of its example.

- [ ] **Step 6: headings pack**

In `rules/headings.md:19`, after `**(3)** Every page carries **all six levels** with a **minimum of 5 H5 AND 5 H6** (no fewer than 5 of each).` insert: `**Exception (2026-09-09, evidence pass): on the homepage and the location pages the 5-per-level minimums are advisory (WARN), never a reason to add a heading; "no skipped levels" and "all six levels" stay hard.**`

- [ ] **Step 7: WORKFLOW.md Sprint 4**

In the Sprint 4 code block (line ~478) change:
```
3. anti-ai-writing  → AI-tell sweep on the final prose
```
to:
```
3. anti-ai-writing  → AI-tell sweep on the final prose
4. cag-evidence-pass → python3 scripts/evidence_audit.py <slug>  (term budgets · claim→proof · labels · review attribution · title ≤70)
   → runs AFTER anti-ai-writing, BEFORE cag-final-page-pass; ERROR blocks deploy
```
In §4a item 1 replace `→ Flags: UNDER-OPTIMIZED (<85 keyword mentions) or OVER-STUFFED (>110)` with `→ Flags: OVER-STUFFED (>110) only — no floor (2026-09-09); trust terms answer to evidence-budgets.json`.
In §4a item 6 replace the Rule 56 and Rule 57 lines with:
```
   → Rule 56: keyword variants = top competitor page's real count +5–10 (fetched, recorded)
   → Rule 57: 95–105 DISTINCT entities, each once where load-bearing
```
In §4b replace the two IMAGE lines:
```
☐ IMAGE-01: All images have alt text ≥250 characters (descriptive + keyword + context)
☐ IMAGE-02: Featured/hero images have 300+ word image description block in page copy
```
with:
```
☐ IMAGE-01: Every image alt describes THAT image, ≤125 characters, one keyword type per image (rules/images.md); no two alts match
☐ IMAGE-02: retired 2026-09-09 — no image-description blocks in body copy
```
In the Sprint 4 Gate list replace `- [ ] All six heading levels present, ≥5 H5 AND ≥5 H6, no skipped levels` with `- [ ] All six heading levels present, no skipped levels; ≥5 H5/H6 advisory on homepage + location pages` and add `- [ ] \`python3 scripts/evidence_audit.py <slug>\` → 0 ERROR; every WARN read and triaged`.
Also update the pipeline summary at line ~39: `Sprint 4    Final      cag-final-page-pass + AEO/GEO + keyword-verifier` → append `+ cag-evidence-pass` on the next line.

- [ ] **Step 8: Verify nothing else still asserts the retired floors**

Run:
```bash
grep -rn -E 'UNDER-OPTIMIZED|150\+ (named )?entit|150–200 keyword|≥250 char|300\+ word image|Title ≤ ?205' docs/reference rules skills .claude/agents | grep -v -E 'retired|was "150|evidence-pass|2026-09-09'
```
Expected: no output. Any hit is another injector: apply the same edit there and re-run until empty.

- [ ] **Step 9: Commit**

```bash
git add docs/reference/WORKFLOW.md .claude/agents/cag-keyword-verifier.md docs/reference/seo-rules.md .claude/agents/cag-meta-description-agent.md rules/headings.md scripts/final_page_audit.py tests/test_final_page_audit.py
git commit -m "rules: retire the six injector rules — no keyword floor, Rule 57 = 95–105 distinct entities, Rule 56 = competitor count +5–10, H5/H6 minimums advisory on home/location, alt ≤125, title ≤70; evidence pass in Sprint 4

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```

---

### Task 8: Review attribution — single source + sweep (breeder input required)

**Files:**
- Create: `data/reviews.json`
- Create: `scripts/sweep_review_attribution.py`
- Create: `tests/test_review_attribution.py`

- [ ] **Step 1: Write the failing test**

`tests/test_review_attribution.py`:
```python
# One quote, one name, everywhere. The 2026-09-09 audit found three quotes credited to five
# names across 12 pages (spec §8). data/reviews.json is the only place a name may come from.
import re, json, glob, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]

def quotes_in_source():
    out = {}
    for f in glob.glob(str(ROOT / "src/pages/**/*.astro"), recursive=True):
        t = pathlib.Path(f).read_text()
        for m in re.finditer(r"quote:\s*\"(.*?)\",\s*(?:\n\s*)?name:\s*'([^']+)'", t, flags=re.S):
            out.setdefault(m.group(1)[:60], set()).add(m.group(2))
    return out

def test_reviews_json_exists_and_has_one_name_per_quote():
    data = json.load(open(ROOT / "data/reviews.json"))
    seen = {}
    for r in data["reviews"]:
        key = r["quote"][:60]
        assert key not in seen, f"quote listed twice in reviews.json: {key!r}"
        seen[key] = r["name"]
        assert r["name"] != "NOT FETCHED", "breeder must supply the name before this test can pass"

def test_no_quote_is_credited_to_two_names_anywhere_in_src():
    bad = {q: n for q, n in quotes_in_source().items() if len(n) > 1}
    assert bad == {}, bad
```

Run: `python3 -m pytest tests/test_review_attribution.py -q 2>&1 | tail -3` → Expected: both FAIL (`reviews.json` missing; two-name dict non-empty).

- [ ] **Step 2: Write `data/reviews.json` with the three contested quotes and NOT FETCHED names**

```json
{
  "_comment": "Single source of truth for every review quote → buyer. Names come from the breeder only. NOT FETCHED until supplied. scripts/sweep_review_attribution.py rewrites every src/pages/**/*.astro `quote:`/`name:` pair from this file.",
  "reviews": [
    {"id": "q1", "quote": "I searched for African Grey parrots for sale near me for months before finding C.A.Gs. Their birds are truly top-notch! My African Grey is affectionate, intelligent, and already picking up words. The shipping process was seamless, and they included a health guarantee.", "name": "NOT FETCHED", "location": "NOT FETCHED", "bird": "Congo African Grey", "candidates": ["Clifford Hutter, Secaucus NJ", "Archie Obrien, Farmingdale NY"]},
    {"id": "q2", "quote": "At first I was hesitant about buying a bird online, but C.A.Gs made the process stress-free. They provided detailed care instructions and my parrot arrived in perfect condition. My Congo African Grey is now the star of our family, talking and entertaining us daily.", "name": "NOT FETCHED", "location": "NOT FETCHED", "bird": "Congo African Grey", "candidates": ["Richard Woodard, Winter Haven FL", "Archie Obrien, Farmingdale NY"]},
    {"id": "q3", "quote": "I ordered a Congo African Grey from C.A.Gs and the experience was flawless. My parrot is healthy, friendly, and well-trained. Watching it grow and bond with my family has been an absolute joy. I recommend C.A.Gs to anyone looking for a quality African Grey.", "name": "NOT FETCHED", "location": "NOT FETCHED", "bird": "Congo African Grey", "candidates": ["Albert Schroder, Santa Clara CA", "Catherine Kempf, Schaumburg IL"]}
  ]
}
```

- [ ] **Step 3: Write the sweep script**

`scripts/sweep_review_attribution.py`:
```python
#!/usr/bin/env python3
"""Rewrite every `quote: "…", name: '…', location: '…'` pair in src/pages/**/*.astro from data/reviews.json.

Refuses to run while any name is NOT FETCHED. Prints every file it changed. `--check` only reports.
"""
import re, sys, json, glob, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = json.load(open(ROOT / "data/reviews.json"))

def main(check=False):
    if any(r["name"] == "NOT FETCHED" for r in DATA["reviews"]):
        print("reviews.json still has NOT FETCHED names — ask the breeder; nothing rewritten")
        return 1
    changed = 0
    for f in glob.glob(str(ROOT / "src/pages/**/*.astro"), recursive=True):
        p = pathlib.Path(f); t = p.read_text(); orig = t
        for r in DATA["reviews"]:
            pat = re.compile(r'(quote:\s*"' + re.escape(r["quote"]) + r'",\s*\n?\s*name:\s*\')([^\']+)(\',\s*location:\s*\')([^\']+)(\')', re.S)
            t = pat.sub(lambda m: f"{m.group(1)}{r['name']}{m.group(3)}{r['location']}{m.group(5)}", t)
        if t != orig:
            changed += 1
            print(("would change " if check else "rewrote ") + p.relative_to(ROOT).as_posix())
            if not check:
                p.write_text(t)
    print(f"{changed} file(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv))
```

- [ ] **Step 4: Run the sweep in check mode**

Run: `python3 scripts/sweep_review_attribution.py --check`
Expected: `reviews.json still has NOT FETCHED names — ask the breeder; nothing rewritten` and exit 1. This task is now **blocked on the breeder** for three names. Commit what exists; the test stays red on purpose until the names arrive.

- [ ] **Step 5: When the breeder supplies the names**

Edit `data/reviews.json` (name + location per quote), then:
```bash
python3 scripts/sweep_review_attribution.py && python3 -m pytest tests/test_review_attribution.py -q
```
Expected: `12 file(s)` (or the number the sweep reports) and `2 passed`. Also update the review avatar `avatarSrc` on the homepage bottom grid if a name changed (the file name carries the buyer's name; rename the `.webp` in `public/` to match and update the `src`). Then Task 9 Step 9 builds and ships it.

- [ ] **Step 6: Commit**

```bash
git add data/reviews.json scripts/sweep_review_attribution.py tests/test_review_attribution.py
git commit -m "feat(reviews): single-source reviews.json + attribution sweep (names NOT FETCHED, awaiting breeder)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```

---

### Task 9: Homepage evidence pass, section by section (sections stay)

**Files:**
- Modify: `src/pages/index.astro`

Read `skills/cag-evidence-pass.md`, `rules/copy.md`, `skills/cag-gate-integrity.md` first. Prose is written fresh from this task's targets, never pasted from a sibling. Every step ends with the audit count for the term(s) it touched.

- [ ] **Step 1: Title and H1**

`src/pages/index.astro:23` becomes:
```js
const title = "African Grey Parrot Breeder in Midland, Texas – C.A.Gs";
```
(55 chars.) Find the `HeroV3` H1 prop (grep `African Grey Parrot Breeder You Can Trust`) and set it to `Congo and Timneh African Grey Breeder in Midland, Texas`. Keep the meta description under 160 chars, one sentence, no pipe.
Run: `npx astro build >/dev/null 2>&1 && python3 scripts/evidence_audit.py index | grep -i title` → Expected: no title line.

- [ ] **Step 2: Jump rail self-description**

grep `18 sections` in `src/pages/index.astro`; delete the phrase and the `everything about C.A.Gs` clause from the TocV3 label so the rail reads only its heading (`On This Page`).
Run: `grep -c '18 sections' src/pages/index.astro` → Expected: `0`.

- [ ] **Step 3: `trust` section owns the credentials**

In `<section id="trust">` keep one row per credential (USDA AWA · CITES Appendix I · DNA sexing · avian-vet certificate · PBFD/APV PCR · hatch certificate/band). Each row: the credential named once, one sentence of what it is, and a link that reads `See the document` pointing at the ledger's `proof` path; while a proof is `NOT FETCHED`, the row's link goes to `/african-greys-for-sale-with-health-guarantee/` with the text `How we document it` and the prose says nothing that is not in `credentials.md`. Give the section `id="trust"` an `<a id="proof">` anchor at its top.
Then in every OTHER section, replace each further mention of USDA / CITES / DNA-sexed / captive-bred / health certificate with either a plain noun ("our paperwork", "the certificate", "the screening") or `<a href="#proof">documented</a>`.
Run: `npx astro build >/dev/null 2>&1 && python3 scripts/evidence_audit.py index | grep -E 'CITES|USDA|DNA|captive'` → Expected: no ERROR lines for those four terms (≤6 / ≤4 / ≤6 / ≤6).

- [ ] **Step 4: Brand name budget**

Count: `grep -o 'C\.A\.Gs' src/pages/index.astro | wc -l`. Replace `C.A.Gs` with `we` / `our` / `here` inside body sentences until the built `<main>` count is ≤20; keep it in the H1, the trust section, the pricing section, each CTA button label once, the FAQ answers where it is the subject, and the form heading. Never touch the schema JSON.
Run: `npx astro build >/dev/null 2>&1 && python3 scripts/evidence_audit.py index | grep 'C.A.Gs'` → Expected: no line.

- [ ] **Step 5: Scam and "legit" routing**

grep `-i -n 'scam\|legit' src/pages/index.astro`. In `<section id="why-us">` (the `ScamAwareness` component) keep ONE sentence: `Before you send anyone a deposit, read <a href="/how-to-avoid-african-grey-parrot-scams/">how to tell a real breeder from a listing</a>.` Remove every other body mention of scam / scammers / legit on the page (FAQ questions included; keep the FAQ *answer* content about deposits if it does not use the words). Do not change the `ScamAwareness` component file itself; pass it the reduced copy or remove the props that carry the extra paragraphs.
Run: `python3 scripts/evidence_audit.py index | grep -E 'scam|legit'` → Expected: no line.

- [ ] **Step 6: Statement labels on the species, health and comparison sections**

Import `StatementLabel` at the top of `index.astro`:
```astro
import StatementLabel from '../components/cag-library/StatementLabel.astro';
```
In `<section id="congo">`, `<section id="timneh">`, `<section id="compare-species">`, `<section id="history">`, `<section id="health">`: every sentence stating a lifespan, a native range, a CITES/IUCN status, a screening test, a nutrient (calcium, D3, UV-B) opens with `<StatementLabel kind="fact" source="<URL from docs/reference/external-link-library.md>" />`; every sentence about what happens in our aviary (weaning window, first words, handling) opens with `<StatementLabel kind="observed" since={2014} />`; every "choose the Congo if…" sentence opens with `<StatementLabel kind="recommendation" />`. Delete `Why Is the Congo Considered the World's Best Talking Parrot?` as a heading; replace with `How Well Does a Congo African Grey Talk?` and open its paragraph with a `fact` label + source. Remove `America's Trusted` (3×) from `history` and the hero eyebrow; replace with `Midland, Texas · since 2014`.
Run: `npx astro build >/dev/null 2>&1 && python3 scripts/evidence_audit.py index | grep -E 'label|superlative'` → Expected: no WARN for congo/timneh/compare-species/history/health; no superlative line.

- [ ] **Step 7: Reviews (only after Task 8 Step 5 has run)**

Confirm `python3 -m pytest tests/test_review_attribution.py -q` passes. Then ensure `reviews-top` and the `reviews` grid do not show the same quote twice on the page (pick a different quote for the top feature from `data/reviews.json`).
Run: `python3 scripts/evidence_audit.py index | grep 'same review'` → Expected: no line. If Task 8 is still blocked, skip this step, leave the sections untouched, and record `review-attribution-unique: BLOCKED on breeder` in the session brief; the audit will still show one ERROR and the page must NOT ship with a "PASS" claim.

- [ ] **Step 8: Sibling dup-gate, hardening, AEO, final pass**

```bash
npx astro build && python3 scripts/dup_content_audit.py index && python3 scripts/dup_content_audit.py index --headers
python3 scripts/page_hardening_scan.py index
python3 scripts/aeo_audit.py index
python3 scripts/evidence_audit.py index
python3 scripts/final_page_audit.py index --type home 2>/dev/null || python3 scripts/final_page_audit.py index
npm run test:render:meta
```
Expected: dup-gate zero non-whitelist crossovers body and headers; hardening `0 ERROR`; AEO `0 ERROR`; evidence `0 ERROR` (or exactly one, the review row, if Task 8 is blocked); final pass PASS / PASS-WITH-WARNINGS with every ✗ triaged as REAL / ACCEPTED / FALSE POSITIVE; meta gate green. Read each gate's examined count before believing it.

- [ ] **Step 9: Ship**

```bash
git add src/pages/index.astro
git commit -m "feat(homepage): evidence pass — say each credential once, proof links, statement labels, one-clause title; every section kept

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin main
```
Wait for the Cloudflare deploy, then: `curl -sI https://congoafricangreys.com/ | head -1` → `HTTP/2 200`, and `python3 scripts/indexnow_submit.py index`. If Step 6 touched any shared component's rendered output on other pages, submit those slugs too.

- [ ] **Step 10: Record the measurement**

Append to `sessions/2026-09-09-evidence-pass-baseline.md`:
```markdown
## Homepage after the pass (built, dist/)
| term | before | after | ceiling |
|---|---|---|---|
| C.A.Gs | 66 | … | 20 |
| CITES | 44 | … | 6 |
| DNA | 40 | … | 6 |
| Appendix I | 28 | … | 2 |
| captive-bred | 32 | … | 6 |
| USDA | 19 | … | 4 |
| scam | 10 | … | 2 |
| legit | 7 | … | 0 |
| words | 8,830 | … | none |
| title chars | 233 | … | 70 |
```
Fill every `…` from `python3 scripts/evidence_audit.py index` and the word count. Commit and push. Then schedule the 14-day LLM-visibility re-probe (Sprint 6): `cag-llm-keyword-intel` on the homepage's six queries, results appended to the same file.

---

## Self-review (done while writing)

**Spec coverage.** §5 section plan → Task 9 (title/H1 Step 1, rail Step 2, trust + all "say once" rows Step 3, brand Step 4, scam Step 5, labels + superlatives + "America's Trusted" Step 6, reviews Step 7). §6 skill shape → Tasks 2–6. §7 sprint changes → Task 7 (Sprint 4 insertion, keyword band, Rule 56/57, IMAGE-01/02, H5/H6, meta) and Task 9 Step 10 (Sprint 6 re-probe). §7 Sprint 0 calibration of budgets and Sprint 0.5 grill-me question are **not** in this plan: they are per-build steps, and the budgets file carries `calibrated: null` so the first build session after this plan does them. §8 review attribution → Task 8. §3 "does A fix each finding" → the Task 9 Step 10 table is the measurement that answers it.

**Placeholders.** The only NOT FETCHED values are the breeder-owned inputs the spec names (proof objects, review names), each written as the literal the house rule requires and each with a test that stays red until supplied. Task 9 prose is written from targets and audit counts, per rule 9; no sentence is copied from a sibling.

**Consistency.** `E.term_budget(html, page_type, budgets, slug="")`, `E.title_too_long`, `E.review_attribution`, `E.claim_binding`, `E.missing_statement_labels`, `E.not_fetched_in_prose`, `E.unsourced_superlatives`, `E.audit` are the names used in both the tests and the script. `.stmt-label` + `data-kind` ∈ {fact, observed, recommendation} is the contract shared by the component, the Python proxy and the render check. Page type `home` is introduced in budgets, `page_type_for`, and `final_page_audit.PROFILES` together.

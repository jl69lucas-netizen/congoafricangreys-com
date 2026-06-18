# cag-final-page-pass Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `cag-final-page-pass` — a page-type-aware final QA gate that covers the bird `/available/` pages the current interior gate cannot see, ending in one PASS / PASS-WITH-WARNINGS / FAIL verdict.

**Architecture:** An upgraded mechanical auditor (`scripts/final_page_audit.py`) gains nested-slug resolution + per-page-type profiles that mark each check FAIL/WARN/NA, with new bird-page hard gates. A new skill file (`skills/cag-final-page-pass.md`) orchestrates the mechanical tier + routes low scorers to the existing strategic/subjective skills. The gate is then validated RED→GREEN on the 6 live bird pages.

**Tech Stack:** Python 3 stdlib (`html.parser`, `re`, `json`), Astro (`npx astro build` → `dist/`), pytest-free inline assertion tests run via `python3`.

**Spec:** `docs/superpowers/specs/2026-06-18-cag-final-page-pass-design.md`

---

## File Structure

- **Create** `scripts/final_page_audit.py` — the upgraded auditor. Pure function `audit_html(slug, html, page_type)` returns the per-check dict + a `_verdict`; `audit(slug, page_type)` reads `dist/.../index.html` and calls it. Supersedes `interior_29_audit.py` via the `interior` profile.
- **Create** `tests/test_final_page_audit.py` — inline-fixture assertion tests (no pytest dependency; run with `python3`).
- **Create** `skills/cag-final-page-pass.md` — the orchestrator skill.
- **Create** `sessions/2026-06-18-final-pass-available-cluster.md` — the validation report.
- **Modify** `CLAUDE.md` — Quick-Start entry + Skills-list registration.
- **Modify** `Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/MEMORY.md` + a new memory file — pointer.
- **Keep** `scripts/interior_29_audit.py` until parity is proven, then replace its body with a one-line shim to the new script.

---

## Task 1: Scaffold the upgraded auditor with nested-slug resolution

**Files:**
- Create: `scripts/final_page_audit.py`
- Test: `tests/test_final_page_audit.py`

The new script reuses the proven `P(HTMLParser)` and per-check logic from `scripts/interior_29_audit.py` verbatim (lines 21–159), then refactors `audit` into a pure `audit_html(slug, html, page_type)` plus a thin file-reading `audit(slug, page_type)`. This task only establishes the skeleton + nested-slug path resolution.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_final_page_audit.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import final_page_audit as A

def test_nested_slug_resolves_to_available_path():
    # available/roys must map to dist/available/roys/index.html
    p = A.dist_path("available/roys")
    assert str(p).endswith("dist/available/roys/index.html"), p

def test_flat_slug_resolves_unchanged():
    p = A.dist_path("african-grey-parrot-price")
    assert str(p).endswith("dist/african-grey-parrot-price/index.html"), p

if __name__ == "__main__":
    import traceback, inspect
    fns = [f for n, f in sorted(globals().items()) if n.startswith("test_") and inspect.isfunction(f)]
    fails = 0
    for f in fns:
        try:
            f(); print(f"  ok  {f.__name__}")
        except Exception:
            fails += 1; print(f"  FAIL {f.__name__}"); traceback.print_exc()
    print(f"\n{len(fns)-fails}/{len(fns)} passed")
    sys.exit(1 if fails else 0)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_final_page_audit.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'final_page_audit'`

- [ ] **Step 3: Create the script skeleton**

Copy `scripts/interior_29_audit.py` to `scripts/final_page_audit.py`, then make these edits:

a) Replace the module docstring (lines 1–5) with:
```python
#!/usr/bin/env python3
"""C.A.Gs final-page-pass auditor — page-type-aware mechanical gate.
Reads dist/<slug>/index.html (slug may be nested, e.g. available/roys) and scores
the objective checks against the page-type PROFILE, returning per-check pass plus a
verdict: PASS / PASS-WITH-WARNINGS / FAIL. Subjective checks (voice/humor/Flesch/
non-commodity/tone/brand-protocol) stay manual. Run AFTER `npx astro build`."""
```

b) Add the path resolver right after `DIST = Path("dist")`:
```python
def dist_path(slug):
    """Resolve a flat or nested slug to its rendered index.html."""
    return DIST / slug / "index.html"
```

c) Leave `SLUGS`, `TRANSACTIONAL`, the `P` parser, and the `audit` body in place for now.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 tests/test_final_page_audit.py`
Expected: PASS — `2/2 passed`

- [ ] **Step 5: Commit**

```bash
git add scripts/final_page_audit.py tests/test_final_page_audit.py
git commit -m "feat(audit): scaffold final_page_audit with nested-slug resolution"
```

---

## Task 2: Refactor `audit` into a pure `audit_html` and add page-type profiles

**Files:**
- Modify: `scripts/final_page_audit.py`
- Test: `tests/test_final_page_audit.py`

Split file-reading from scoring so tests can pass HTML directly, and introduce the `PROFILES` map. A profile names each check's severity for that page type: `FAIL` (hard gate), `WARN` (soft), or `NA` (skip).

- [ ] **Step 1: Write the failing test**

Append to `tests/test_final_page_audit.py` (above the `__main__` block):

```python
MINIMAL_BIRD = """
<html><head><title>Roys — Congo African Grey for Sale | C.A.Gs</title>
<link rel="canonical" href="https://congoafricangreys.com/available/roys/">
<meta name="description" content="Roys, our hand-raised Congo African Grey, $2,300.">
<script type="application/ld+json">{"@type":"Product","offers":{"@type":"Offer","availability":"https://schema.org/InStock"}}</script>
</head><body><main><h1>Roys</h1><h2>About Roys</h2><h3>Health</h3><h4>Shipping</h4>
<p>Ships nationwide &middot; $185 airport &middot; $350 home. Captive-bred, CITES Appendix I, USDA AWA. Lifespan 40-60 years.</p>
</main><footer>(844) 820-2234</footer></body></html>
"""

def test_profile_marks_newsletter_na_for_bird():
    r = A.audit_html("available/roys", MINIMAL_BIRD, "bird")
    assert r["_severity"]["newsletter_present"] == "NA", r["_severity"]

def test_profile_marks_newsletter_fail_for_interior():
    r = A.audit_html("african-grey-parrot-care-guide", MINIMAL_BIRD, "interior")
    assert r["_severity"]["newsletter_present"] in ("FAIL", "WARN"), r["_severity"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_final_page_audit.py`
Expected: FAIL — `AttributeError: module 'final_page_audit' has no attribute 'audit_html'`

- [ ] **Step 3: Refactor + add PROFILES**

In `scripts/final_page_audit.py`:

a) Rename the existing `def audit(slug):` to `def audit_html(slug, html, page_type="interior"):` and **delete** its first two lines (`f = DIST/slug/...` and the `_MISSING` return and `html = f.read_text(...)`). The function now receives `html` directly. Its first line becomes:
```python
def audit_html(slug, html, page_type="interior"):
    raw = html
    p = P(); p.feed(html)
```

b) At the very end of `audit_html`, before `return r`, attach the severity map and verdict (verdict logic lands in Task 4 — for now just severities):
```python
    r["_severity"] = {k: severity(page_type, k) for k in r if not k.startswith("_")}
    return r
```

c) Add a thin file reader below `audit_html`:
```python
def audit(slug, page_type="interior"):
    f = dist_path(slug)
    if not f.exists():
        return {"_MISSING": True}
    return audit_html(slug, f.read_text(encoding="utf-8", errors="ignore"), page_type)
```

d) Add the profile system above `audit_html`:
```python
# Per-page-type check severities. Anything unlisted falls back to DEFAULT_SEVERITY.
# FAIL = hard ship-blocker · WARN = soft (logged, shippable) · NA = not applicable.
DEFAULT_SEVERITY = "FAIL"
PROFILES = {
    "bird": {
        "newsletter_present": "NA",      # bird pages exempt (footer newsletter only)
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 tests/test_final_page_audit.py`
Expected: PASS — `4/4 passed` (the two Task-1 tests + two new). The new checks (`no_aggregateoffer` etc.) don't exist yet but `severity()` returns their declared values regardless; they're added in Task 3.

- [ ] **Step 5: Commit**

```bash
git add scripts/final_page_audit.py tests/test_final_page_audit.py
git commit -m "feat(audit): pure audit_html + page-type profile severities"
```

---

## Task 3: Add the bird-page hard-gate checks

**Files:**
- Modify: `scripts/final_page_audit.py`
- Test: `tests/test_final_page_audit.py`

Add the five bird-specific checks the interior gate never had. These read the already-parsed `raw`, `bodytext`, `p.jsonld`, `flat`, and `p.imgs`.

- [ ] **Step 1: Write the failing test**

Append to `tests/test_final_page_audit.py`:

```python
BAD_BIRD = """
<html><head><title>Bad — C.A.Gs</title></head><body><main><h1>X</h1>
<script type="application/ld+json">{"@type":"AggregateOffer"}</script>
<p>This bird is tested clear of PBFD and polyomavirus.</p>
</main></body></html>
"""

def test_bird_aggregateoffer_fails():
    r = A.audit_html("available/x", BAD_BIRD, "bird")
    assert r["no_aggregateoffer"] is False
    assert r["_severity"]["no_aggregateoffer"] == "FAIL"

def test_bird_pbfd_claim_fails():
    r = A.audit_html("available/x", BAD_BIRD, "bird")
    assert r["no_pbfd_claim"] is False

def test_good_bird_passes_hard_gates():
    r = A.audit_html("available/roys", MINIMAL_BIRD, "bird")
    assert r["no_aggregateoffer"] is True
    assert r["no_pbfd_claim"] is True
    assert r["shipping_line"] is True
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_final_page_audit.py`
Expected: FAIL — `KeyError: 'no_aggregateoffer'`

- [ ] **Step 3: Add the checks**

In `audit_html`, immediately after the schema block (after the line `r["schema_types"] = ",".join(sorted(set(flat)))`), insert:

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 tests/test_final_page_audit.py`
Expected: PASS — `7/7 passed`

- [ ] **Step 5: Commit**

```bash
git add scripts/final_page_audit.py tests/test_final_page_audit.py
git commit -m "feat(audit): bird-page hard gates (AggregateOffer/PBFD/shipping/InStock/hero)"
```

---

## Task 4: Verdict model + profile-aware main loop + interior parity

**Files:**
- Modify: `scripts/final_page_audit.py`
- Test: `tests/test_final_page_audit.py`

Compute the verdict from severities, and rewrite `main()` to take a slug→type map and print per-page verdict + a pre-triaged roll-up.

- [ ] **Step 1: Write the failing test**

Append:

```python
def test_verdict_fail_when_hard_gate_breaks():
    r = A.audit_html("available/x", BAD_BIRD, "bird")
    assert r["_verdict"] == "FAIL", r["_verdict"]

def test_verdict_not_fail_for_clean_bird():
    r = A.audit_html("available/roys", MINIMAL_BIRD, "bird")
    assert r["_verdict"] in ("PASS", "PASS-WITH-WARNINGS"), r["_verdict"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_final_page_audit.py`
Expected: FAIL — `KeyError: '_verdict'`

- [ ] **Step 3: Add verdict computation + new main**

a) In `audit_html`, change the severity/return block to also compute the verdict:
```python
    r["_severity"] = {k: severity(page_type, k) for k in r if not k.startswith("_")}
    hard_fails = [k for k, v in r.items() if v is False and r["_severity"].get(k) == "FAIL"]
    warns = [k for k, v in r.items() if v is False and r["_severity"].get(k) == "WARN"]
    r["_verdict"] = "FAIL" if hard_fails else ("PASS-WITH-WARNINGS" if warns else "PASS")
    r["_hard_fails"] = hard_fails
    r["_warns"] = warns
    return r
```

b) Replace `def main():` (lines ~161–186 of the original) with a profile-aware version. Default targets reproduce the interior 18-page run; pass `--birds` for the available cluster:
```python
BIRDS = ["available/bery","available/amie","available/roys",
         "available/jins-jeni","available/elad","available/evie"]

def main():
    import sys
    if "--birds" in sys.argv:
        targets = [(s, "bird") for s in BIRDS]
    else:
        targets = [(s, "interior") for s in SLUGS]
    rows = {s: audit(s, t) for s, t in targets}
    print("\n=== C.A.Gs FINAL PAGE PASS ===  (✓ pass / ✗ FAIL)\n")
    for s, r in rows.items():
        if r.get("_MISSING"):
            print(f"  ✗ {s}: dist/ MISSING — run `npx astro build`"); continue
        print(f"[{r['_verdict']}] {s}   {r['h_counts']} | FAQPage×{r['faqpage_count']} | schema:{r['schema_types']}")
        if r["_hard_fails"]: print("    FAIL → " + ", ".join(r["_hard_fails"]))
        if r["_warns"]:      print("    WARN → " + ", ".join(r["_warns"]))
    npass = sum(1 for r in rows.values() if r.get("_verdict") == "PASS")
    print(f"\n{npass}/{len(rows)} clean PASS · "
          f"{sum(1 for r in rows.values() if r.get('_verdict')=='PASS-WITH-WARNINGS')} with warnings · "
          f"{sum(1 for r in rows.values() if r.get('_verdict')=='FAIL')} FAIL")
    print("\nSubjective (voice/humor/Flesch/non-commodity/tone/brand-protocol) = manual spot-check.")
```

- [ ] **Step 4: Run tests + interior parity check**

Run: `python3 tests/test_final_page_audit.py`
Expected: PASS — `9/9 passed`

Run (parity — must not crash; same interior pages):
`npx astro build >/dev/null 2>&1 && python3 scripts/final_page_audit.py | head -25`
Expected: a verdict line per interior slug, no traceback.

- [ ] **Step 5: Commit**

```bash
git add scripts/final_page_audit.py tests/test_final_page_audit.py
git commit -m "feat(audit): PASS/WARN/FAIL verdict model + profile-aware main (--birds)"
```

---

## Task 5: Write the orchestrator skill

**Files:**
- Create: `skills/cag-final-page-pass.md`

- [ ] **Step 1: Write the skill file**

Create `skills/cag-final-page-pass.md` with this exact structure (fill the profile tables from the spec §4 and the copy-paste block from `manual-auditor-check` extended with the bird gates):

```markdown
---
name: cag-final-page-pass
description: Use as THE final QA gate at the end of EVERY C.A.Gs page build/rebuild/polish, before you "give the page a pass" or deploy — any page type, including bird /available/ and for-sale pages the interior gate excludes. Runs the mechanical page-type-aware auditor over dist/, routes low scorers to the strategic + subjective checks, and returns one PASS / PASS-WITH-WARNINGS / FAIL verdict with a prioritized, WHY-grounded fix list. Triggers: "final check", "give this page a pass", "is this page done", "audit before deploy", "run the final manual checks".
tools: [Read, Write, Bash]
---

# C.A.Gs Final Page Pass — the give-it-a-pass gate

## Overview
The single entrypoint you run at the end of every page build. Page-type-aware, two-tier,
ends in ONE verdict. Supersedes the interior-only `manual-auditor-check` by covering EVERY
page type via profiles; reuses `cags-comprehensive-page-audit-system` (strategic) and the
subjective checklist as components — it does not re-implement them.

## When to Use / Not
USE — a page (or batch) is "done" and you're about to pass/deploy it; ANY type incl. bird
/available/, for-sale, location, comparison, blog. NOT — pre-build planning (cag-content-
audit-agent) or deep "why isn't this ranking" strategy (cags-comprehensive-page-audit-system,
which this gate calls for low scorers).

## Two-tier flow
1. Mechanical: `npx astro build` then `python3 scripts/final_page_audit.py [--birds]`.
   Per-page PASS/WARN/FAIL + pre-triaged roll-up. Edit BIRDS/SLUGS or add a profile to retarget.
2. Strategic (low/failing only): route to the 5 owned scorers in cags-comprehensive-page-
   audit-system (AEO/entity/visual/backlink/verdict) + specialists; assemble, don't duplicate.
3. Subjective (sample 1 transactional + 1 pillar + 1 trust, or lowest bird scorer + 1):
   the copy-paste block below.

## Page-type profiles
[Reproduce the bird HARD-GATE + SCALED tables from spec §4, plus a one-row summary per other
type: interior (= legacy 18-page behavior), for-sale/variant, location, comparison, blog, hub,
homepage. Unmapped type → strictest subset, type-specific checks = WARN (fail-safe).]

## Verdict model
FAIL on any REAL hard-gate miss · PASS-WITH-WARNINGS on soft items · PASS clean. Triage every
✗ as REAL / ACCEPTED / FALSE-POSITIVE / NET-NEW before reporting (never quote a raw machine
fail as a defect — this is what prevented 31 false positives on the interior batch).

## The 5 false-positive traps (do NOT fabricate as defects)
[Reproduce the 4 from manual-auditor-check — nested/list @type, header-logo-not-hero,
authority-hotline phone, strip-JSON-LD-before-wordcount — plus the bird trap: an `Offer`
nested inside a single `Product` is correct; only a top-level `AggregateOffer` fails.]

## Copy-paste FINAL MANUAL PAGE CHECK
[The manual-auditor-check block, extended with a BIRD-PAGE section: single Product+Offer · no
PBFD/Polyoma · sold≠InStock · real hero photo · shipping line $185/$350 · 700–1,000 words ·
newsletter EXEMPT · house-method WARN. CAGs first-person voice; LSI/NLP keyword coverage line:
"captive-bred Congo/Timneh African Grey, hand-raised/hand-fed, DNA-sexed, CITES Appendix I,
talking grey, IATA airport shipping" present where natural.]

## GAP-FLAGs the gate emits (never invents)
House-method name (WARN until confirmed) · extra authority-link targets (verify 200, add to
external-link-library.md first) · airport-code/Flight-Nanny/local-avian-vet signals by page type.

## Common mistakes
Auditing source greps not dist/ · reporting the roll-up un-triaged · chasing Flesch 60–70 as a
hard gate (floor ~55 for entity-dense copy) · running it on the 3 unbuilt birds (joys/loti/carl
are out of scope — report out-of-scope, not FAIL).

## Workflow placement
Sprint 4 FINAL step, immediately before Sprint 5 deploy. After accessibility/performance/
canonical/footer fixers. Companion to MANUAL INTERIOR-PAGE CHECKLIST.md Part N.
```

- [ ] **Step 2: Verify frontmatter + links resolve**

Run: `head -5 skills/cag-final-page-pass.md && grep -c "cags-comprehensive-page-audit-system\|manual-auditor-check\|final_page_audit.py" skills/cag-final-page-pass.md`
Expected: valid frontmatter; count ≥3.

- [ ] **Step 3: Commit**

```bash
git add skills/cag-final-page-pass.md
git commit -m "feat(skill): cag-final-page-pass orchestrator gate"
```

---

## Task 6: Register in CLAUDE.md + memory

**Files:**
- Modify: `CLAUDE.md`
- Create: `Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/project_final_page_pass.md`
- Modify: `Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/MEMORY.md`

- [ ] **Step 1: Add the Quick-Start entry to CLAUDE.md**

Under `### "Is the site healthy?"` (the Quick Start Commands block), add a new entry:
```markdown
### "Give a page a final pass / is this page done?"
→ `skills/cag-final-page-pass` (THE final gate, ANY page type incl. bird /available/) → `npx astro build` → `python3 scripts/final_page_audit.py [--birds]` → one PASS/WARN/FAIL verdict + triaged fixes → deploy
```

- [ ] **Step 2: Register in the Technical Skills list**

In the `#### Technical Skills` section of CLAUDE.md, add a bullet directly after the `manual-auditor-check` line:
```markdown
- `skills/cag-final-page-pass.md` — **THE final "give-it-a-pass" gate for EVERY page type** (supersedes `manual-auditor-check`, which was interior-only). Page-type profiles (bird `/available/`, for-sale, interior, location, comparison, blog) drive a mechanical auditor (`scripts/final_page_audit.py`, nested-slug aware) → one PASS/PASS-WITH-WARNINGS/FAIL verdict; routes low scorers to `cags-comprehensive-page-audit-system` + the subjective checklist. Bird gates: single Product/Offer, no PBFD, sold≠InStock, shipping line, 700–1,000 words, newsletter-exempt, house-method WARN.
```

- [ ] **Step 3: Add the script to the Scripts section**

In `## Scripts`, after the `interior_29_audit` mention (or `generate_sitemaps.py`), add:
```markdown
- `scripts/final_page_audit.py` — page-type-aware final QA auditor (nested-slug aware; profiles for bird/interior/for-sale/etc.); supersedes `interior_29_audit.py`. Run `python3 scripts/final_page_audit.py --birds` for the `/available/` cluster. Owned by the `cag-final-page-pass` skill.
```

- [ ] **Step 4: Write the memory file**

Create `Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/project_final_page_pass.md`:
```markdown
---
name: project_final_page_pass
description: cag-final-page-pass is THE final QA gate for every page type incl. bird /available/; supersedes interior-only manual-auditor-check; script final_page_audit.py is nested-slug + profile aware
metadata:
  type: project
---

`skills/cag-final-page-pass.md` is the single end-of-build gate (PASS / PASS-WITH-WARNINGS /
FAIL) for ANY page type — it covers the bird `/available/<slug>/` and for-sale pages that
`[[reference_interior_page_standard]]`'s `manual-auditor-check` explicitly excluded. Mechanical
tier = `scripts/final_page_audit.py` (nested-slug aware, page-type PROFILES mark each check
FAIL/WARN/NA); run `--birds` for the available cluster. Bird hard gates: single Product+Offer
(no AggregateOffer), no PBFD/Polyoma claim, sold≠InStock, real hero photo, shipping line
$185/$350. Bird scoped: 700–1,000 words, newsletter EXEMPT, house-method = WARN until a term is
confirmed. Two-tier: low scorers route to `cags-comprehensive-page-audit-system`. Validated on
the 6 live birds 2026-06-18 (joys/loti/carl unbuilt = out of scope).
```

- [ ] **Step 5: Add the MEMORY.md index line**

Append under the existing index list in `MEMORY.md`:
```markdown
- [Final Page Pass Gate](project_final_page_pass.md) — THE end-of-build gate for every page type incl. bird /available/; supersedes interior-only manual-auditor-check; final_page_audit.py is nested-slug + profile aware (--birds)
```

- [ ] **Step 6: Commit**

```bash
git add CLAUDE.md
git commit -m "docs(claude): register cag-final-page-pass gate + final_page_audit.py script"
```

(Memory files live outside the repo and are not committed.)

---

## Task 7: RED→GREEN validation on the 6 live bird pages

**Files:**
- Create: `sessions/2026-06-18-final-pass-available-cluster.md`
- Modify: bird page `.astro` files only if a REAL `✗` is found.

- [ ] **Step 1: Run the gate (RED capture)**

Run:
```bash
npx astro build >/dev/null 2>&1 && python3 scripts/final_page_audit.py --birds | tee /tmp/birds-red.txt
```
Expected: a verdict line for each of the 6 birds; capture every `✗`.

- [ ] **Step 2: Triage every ✗ in the session file**

Create `sessions/2026-06-18-final-pass-available-cluster.md` with a table: page · check · verdict · triage (REAL / ACCEPTED / FALSE-POSITIVE / NET-NEW) · action. Paste the RED output. For each REAL item, note the exact `src/pages/available/<slug>/index.astro` line to fix.

- [ ] **Step 3: Apply REAL fixes only**

Edit only the bird `.astro` files for items triaged REAL (e.g. alt >190, missing width/height, a stray PBFD mention). Do NOT touch ACCEPTED/FALSE-POSITIVE items. Confidence Gate ≥97% per CLAUDE.md; if a fix is uncertain, log it to the session file's `## Open Flags` and continue with the rest.

- [ ] **Step 4: Re-run the gate (GREEN)**

Run:
```bash
npx astro build >/dev/null 2>&1 && python3 scripts/final_page_audit.py --birds | tee /tmp/birds-green.txt
```
Expected: all 6 birds at `PASS` or `PASS-WITH-WARNINGS`; zero un-triaged hard FAILs. Append the GREEN output to the session file.

- [ ] **Step 5: Prove a hard gate fires (anti-dead-code check)**

Run a one-off dry run mutating a copy in memory:
```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); import final_page_audit as A; \
print(A.audit_html('available/x','<html><body><main><h1>x</h1><script type=\"application/ld+json\">{\"@type\":\"AggregateOffer\"}</script></main></body></html>','bird')['_verdict'])"
```
Expected: `FAIL` — confirms the AggregateOffer trap is live, not dead code.

- [ ] **Step 6: Commit + push (deploy)**

```bash
git add sessions/2026-06-18-final-pass-available-cluster.md src/pages/available/
git commit -m "test(birds): validate cag-final-page-pass on 6 /available/ pages (RED→GREEN)"
git push origin main
git log origin/main..HEAD   # expected: empty (confirms pushed = deployed)
```

---

## Self-Review notes
- **Spec coverage:** §3 tiers → Tasks 2–5; §4 bird profile → Tasks 2–3; §5 verdict → Task 4; §6 voice/LSI → Task 5 skill copy block; §7 GAP-FLAGs → Task 5 skill section; §8 deliverables → Tasks 1–7; §9 acceptance → Task 7 (incl. anti-dead-code step 5 and out-of-scope birds in Task 6 memory + Task 5 common-mistakes).
- **Interior parity** (spec §8 deliverable 2) → Task 4 step 4 runs the default (interior) path with no crash; the `interior` profile marks bird-only checks NA so legacy results are unchanged.
- **No placeholders:** every code/test step shows real code; profile tables in Task 5 reference spec §4 (same doc, reproduced, not "similar to").

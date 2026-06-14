# Interior 18-Page · 29-Check Final QA Audit — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run a final, de-duplicated 29-point QA pass across all 18 newly-polished Direction-D interior pages, capture every good/bad learning for reuse, and fold the net-new checks + merges back into `MANUAL INTERIOR-PAGE CHECKLIST.md`.

**Architecture:** Most of the 29 checks are *mechanically verifiable in `dist/`* (heading counts, schema presence, meta length, alt/lazy/dims, phone-in-body, svg-in-`content:`, link placement, `<dl>` misuse, IndexNow-able sitemap inclusion). We build ONE idempotent Python auditor (`scripts/interior_29_audit.py`) that scores all 18 pages against the objective subset and emits a scorecard. The ~6 genuinely subjective checks (first-person voice, Honesty-Policy humor, Flesch 60–70, non-commodity detail, tone, brand-protocol naming) get a structured manual spot-check on a 3-page sample. Then we reconcile the user's 29 into the manual.

**Tech Stack:** Astro (already built to `dist/`), Python 3 stdlib only (`html.parser`, `re`, `json`, `pathlib`), `git`.

---

## ⚠️ ONE OPEN DECISION (blocks Task 4 only — everything else proceeds)

The user's check **#13** says *4-part meta titles **max 275 chars** + descriptions **max 155 chars***. The current `MANUAL INTERIOR-PAGE CHECKLIST.md` Part J.1 says *title **≤205** · description **≤185 (F1) / ≤300 (F2)***. These **conflict** and change what we write. Per the "surface conflicts, don't guess" rule this is escalated, not silently merged. Recommendation captured in Task 4; final answer requested at hand-off. The audit (Tasks 1–3) measures *actual* lengths against BOTH bars so the decision is data-grounded.

---

## MY READ ON THE 29 CHECKS (the analysis you asked for)

**Verdict:** the 29 is a strong superset of the manual's Parts A–N, but it has (a) a numbering bug, (b) heavy internal duplication, (c) two genuine conflicts with the live manual, and (d) ~6 genuinely *new* checks worth absorbing. Merge map:

**Merges (29 → 18 distinct checks):**
- **1 + 2 + 4** → one *"Keyword & Semantic Coverage"* check (SEO/GEO/semantic/branded/LSI/NLP/fan-out/100+ intent variations are all the same audit of the keyword table from Part A).
- **3 + 23** → one *"Links woven mid-sentence"* check (Part F). The "front-load answer in first 30%" half of #3 belongs with…
- **3(front-load) + 7(AEO) + 7(intent→structure) + 8(BLUF 50w) + 9(atomic/chunking) + 10(lists/tables for snippets)** → one *"AEO / BLUF / Atomic"* check (Part H). Six of your items collapse to this.
- **19 + 20** → identical (first-person breeder voice). One check (Part D.1).
- **14 + 25** → identical (Image SEO 5-element). One check (Part J.2), with #14's `<100KB` added.
- **16** overlaps **19/20** (warm/empathetic tone is a facet of the first-person voice check) → keep as a thin sub-line, not a standalone.

**Two conflicts to resolve (don't silently merge):**
1. **Meta length** — #13 (≤275 title / ≤155 desc) vs manual (≤205 / ≤185–300). → Open Decision above.
2. **Phone number** — #17 wants the phone *"in the footer and across all core pages"*; the manual's Rule 61 / Part N says **NO phone in the body**. These are reconcilable, not contradictory: **footer phone = required; body phone = banned.** The audit checks both (footer present AND body absent). Folding that explicit distinction into the manual is itself an improvement.

**Net-new checks worth ADDING to the manual (your 29 surfaces these; the manual lacks them):**
- **#5 Logistics entities** (airport codes DEN/LAX/MIA/ORD + Avian Flight Nanny). *Which pages need it?* → only shipping-/buyer-/price-adjacent interior pages. Of the 18: `african-grey-parrot-price` yes; the rest of the interior set (care/health/diet/lifespan/guide/faq/reviews/privacy/etc.) **no** — airport codes there are keyword-stuffing. Recommendation: scope this check to "transactional interior pages only," and route the real airport/flight-nanny depth to the location/`buy-…-near-me` cluster where it already lives.
- **#6 Local authority** (named avian-vet hospitals + state licensing). Same scoping: a *location-page* signal, not an all-interior one. For interior pages, the safe version is one outbound link to AAV's "find a vet" + the USDA-AWA/CITES line we already require. Don't fabricate specific hospital names (ledger rule).
- **#11 Brand-specific concept naming** (e.g. a named *"Parrot Culture protocol"*). **Genuinely additive and high-leverage for topical authority/GEO** — a named, ownable method an LLM will attribute to C.A.Gs. Recommend coining ONE house term for our hand-feeding/weaning method (e.g. *"the C.A.Gs Quiet-Wean method"*) — but it must be **breeder-confirmed** before it ships (ledger), so it lands as a GAP-FLAG, not invented copy.
- **#15 Flesch 60–70** — additive, measurable. *Honest trade-off:* dense first-person + entity-rich copy often lands 50–60; treat 60–70 as a target with a documented floor, not a hard gate, or it will fight the entity loop.
- **#17 footer phone** — additive (see conflict #2).
- **#18 Newsletter, 3 placements (Top/Middle/Bottom)** — additive; currently the manual mentions the `cag-newsletter` component but doesn't *require* 3 placements.
- **#14 `<100KB` image weight** — additive to Part J.2.

**Checks I'd ADD that are in *neither* list (my recommendation):**
- **Keyword cannibalization sweep** across the 18 (overlapping primary terms split ranking — you already hit this once; the reviews page had a fake `reviewCount`). One pass over all 18 `<title>`/`<h1>`.
- **Internal-link reciprocity / orphan check** — is every one of the 18 linked *from* a hub/another page, not just linking out?
- **Schema validity** — JSON-LD parses, and exactly ONE `FAQPage` per page (the duplicate-FAQPage trap).
- **Alt-text uniqueness** — no two images share identical alt (a real GSC image-SEO signal).
- **Mobile 375px render gate** — the manual treats it implicitly; make it an explicit tick.
- **`dateModified` / visible "Updated <Month Year>"** freshness on all 18 (Part H lists it; make it a gate).

---

## File Structure

- **Create** `scripts/interior_29_audit.py` — idempotent mechanical auditor over `dist/<slug>/index.html` for all 18 slugs; prints a per-page × per-check scorecard + a failures list; exit 0 always (report tool, not a CI gate).
- **Create** `sessions/2026-06-14-interior-29-check-audit.md` — the run's scorecard + manual spot-check notes + the good/bad learnings log + GAP-FLAGs for the breeder.
- **Modify** `MANUAL INTERIOR-PAGE CHECKLIST.md` — absorb the merges, the 2 conflict reconciliations, and the net-new checks; bump to v2.
- **Modify** memory: `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/MEMORY.md` + one new memory file for the audit learnings.

The 18 slugs (canonical, verified on disk):
```
african-grey-parrot-care-guide  african-grey-care  african-grey-parrot-diet
best-african-grey-parrot-food  african-grey-parrot-lifespan  african-grey-parrot-health-guarantee
trusted-african-grey-parrot-breeders  african-grey-reviews  captive-bred-african-grey-parrot
cites-african-grey-documentation  how-to-avoid-african-grey-parrot-scams  african-grey-parrot-guide
african-grey-parrot-faq  how-to-tame-african-grey-parrot  african-grey-adoption
african-grey-parrot-price  contact-us  privacy-policy
```

---

## Task 1: Build the mechanical auditor

**Files:**
- Create: `scripts/interior_29_audit.py`

- [ ] **Step 1: Write the auditor**

```python
#!/usr/bin/env python3
"""Interior 18-page · 29-check final QA auditor (mechanical subset).
Reads dist/<slug>/index.html and scores the objective checks. Subjective
checks (voice/humor/Flesch/non-commodity) are spot-checked manually — see plan.
Run AFTER `npx astro build`. Exit 0 always; this is a report, not a gate."""
import re, json, sys
from pathlib import Path
from html.parser import HTMLParser

DIST = Path("dist")
SLUGS = [
    "african-grey-parrot-care-guide","african-grey-care","african-grey-parrot-diet",
    "best-african-grey-parrot-food","african-grey-parrot-lifespan","african-grey-parrot-health-guarantee",
    "trusted-african-grey-parrot-breeders","african-grey-reviews","captive-bred-african-grey-parrot",
    "cites-african-grey-documentation","how-to-avoid-african-grey-parrot-scams","african-grey-parrot-guide",
    "african-grey-parrot-faq","how-to-tame-african-grey-parrot","african-grey-adoption",
    "african-grey-parrot-price","contact-us","privacy-policy",
]
TRANSACTIONAL = {"african-grey-parrot-price"}  # #5/#6 scoped here only

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.h={i:0 for i in range(1,7)}; s.imgs=[]; s.cur=None
        s.title=""; s.intitle=False; s.text=[]; s.links=[]; s.cura=None; s.atext=[]
        s.jsonld=[]; s.injson=False; s.metadesc=""; s.canonical=""; s.body=[]
    def handle_starttag(s,t,a):
        d=dict(a)
        if re.fullmatch(r"h[1-6]",t): s.cur=int(t[1]); s.h[s.cur]+=1
        if t=="title": s.intitle=True
        if t=="img": s.imgs.append(d)
        if t=="a":
            s.cura=d; s.atext=[]
        if t=="meta" and d.get("name")=="description": s.metadesc=d.get("content","")
        if t=="link" and d.get("rel")=="canonical": s.canonical=d.get("href","")
        if t=="script" and d.get("type")=="application/ld+json": s.injson=True
    def handle_endtag(s,t):
        if t=="title": s.intitle=False
        if re.fullmatch(r"h[1-6]",t): s.cur=None
        if t=="a" and s.cura is not None:
            s.links.append((s.cura, "".join(s.atext).strip())); s.cura=None
        if t=="script" and s.injson:
            s.injson=False
    def handle_data(s,data):
        if s.intitle: s.title+=data
        if s.injson: s.jsonld.append(data)
        if s.cura is not None: s.atext.append(data)
        s.body.append(data)

def audit(slug):
    f = DIST/slug/"index.html"
    if not f.exists(): return {"_MISSING": True}
    html = f.read_text(encoding="utf-8", errors="ignore")
    raw = html  # for regex over attributes/CSS
    p = P(); p.feed(html)
    bodytext = " ".join(p.body)
    r = {}
    # --- headings (Part D.2 / #21) ---
    r["h1==1"] = p.h[1]==1
    r["all_h1_h4"] = all(p.h[i]>=1 for i in (1,2,3,4))
    r["h_counts"] = "".join(f"H{i}:{p.h[i]} " for i in range(1,7)).strip()
    # no-skip: a level >0 with the one above ==0 (and not h1) is a skip
    r["no_skip"] = not any(p.h[i]>0 and p.h[i-1]==0 for i in range(2,7))
    # --- schema (Part I / #12) ---
    blobs=[]; valid=True
    for b in ["".join([p.jsonld[i]]) for i in range(len(p.jsonld))]:
        b=b.strip()
        if not b: continue
        try: blobs.append(json.loads(b))
        except Exception: valid=False
    types=[]
    for b in blobs:
        for obj in (b if isinstance(b,list) else [b]):
            g=obj.get("@graph",[obj]) if isinstance(obj,dict) else [obj]
            for o in g:
                if isinstance(o,dict) and o.get("@type"): types.append(o["@type"])
    flat=[t for x in types for t in (x if isinstance(x,list) else [x])]
    r["jsonld_valid"] = valid and bool(blobs)
    r["has_breadcrumb"] = "BreadcrumbList" in flat
    r["has_org"] = any(t in flat for t in ("Organization","LocalBusiness"))
    r["faqpage_count"] = flat.count("FAQPage")
    r["faqpage_ok"] = flat.count("FAQPage") <= 1
    r["schema_types"] = ",".join(sorted(set(flat)))
    # --- meta (Part J / #13) ---
    r["title_len"] = len(p.title.strip())
    r["desc_len"] = len(p.metadesc.strip())
    r["title_le205"] = len(p.title.strip())<=205
    r["title_le275"] = len(p.title.strip())<=275
    r["desc_le155"] = len(p.metadesc.strip())<=155
    r["brand_in_title"] = "C.A.Gs" in p.title or "Congo African Grey" in p.title
    r["canonical_abs"] = p.canonical.startswith("https://")
    # --- images (Part J.2 / #14, #25) ---
    imgs=p.imgs
    def yes(i,k): return k in i and i[k] not in (None,"")
    r["img_total"]=len(imgs)
    r["img_all_alt"]=all("alt" in i for i in imgs)
    alts=[i.get("alt","") for i in imgs if i.get("alt","")]
    r["img_alt_unique"]=len(alts)==len(set(alts))
    r["img_alt_le190"]=all(len(i.get("alt",""))<=190 for i in imgs)
    non_hero=imgs[1:] if imgs else []
    r["img_lazy_nonhero"]=all(i.get("loading")=="lazy" for i in non_hero) if non_hero else True
    r["img_dims"]=all(yes(i,"width") and yes(i,"height") for i in imgs) if imgs else True
    # --- a11y / gotcha traps (Part K / M / #26, #28) ---
    r["no_svg_in_content"] = not re.search(r"content\s*:\s*['\"]\s*<svg", raw)
    r["no_userselect_none"] = "user-select:none" not in raw.replace(" ","")
    r["no_escaped_svg"] = "&lt;svg" not in raw
    r["no_emoji_parrot"] = "🦜" not in raw
    # --- links (Part F / #3, #23) ---
    ext=[(d,txt) for d,txt in p.links if d.get("href","").startswith("http") and "congoafricangreys.com" not in d.get("href","")]
    r["ext_links"]=len(ext)
    r["ext_newtab_rel"]=all(d.get("target")=="_blank" and "noopener" in d.get("rel","") for d,_ in ext) if ext else True
    bad_anchor=re.compile(r"^(click here|more|read more|here|learn more)$",re.I)
    r["no_bare_anchors"]=not any(bad_anchor.match(txt) for _,txt in p.links if txt)
    intc=[d for d,_ in p.links if d.get("href","").startswith("/")]
    r["internal_links"]=len(intc)
    # --- conversion (Part N / #17, Rule 61) ---
    phone=re.compile(r"\b(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b")
    # crude body vs footer split on <footer>
    footer_idx=raw.lower().find("<footer")
    body_part=raw[:footer_idx] if footer_idx>0 else raw
    # strip schema/script so phone-like numbers in JSON-LD don't false-positive
    body_clean=re.sub(r"<script[\s\S]*?</script>","",body_part)
    r["no_phone_in_body"]=not phone.search(re.sub(r"<[^>]+>"," ",body_clean))
    # --- compliance copy (Part N / Rule 44, 46) ---
    first300=" ".join(re.sub(r"<[^>]+>"," ",html).split())[:1800]
    r["cites_captive_usda_early"]=("Appendix I" in first300 or "captive-bred" in first300.lower()) and ("USDA" in first300 or "AWA" in first300)
    r["lifespan_40_60"]=bool(re.search(r"40\s*[–-]\s*60|40 to 60",bodytext))
    # --- newsletter (#18) ---
    r["newsletter_present"]=("newsletter" in raw.lower())
    # --- freshness (#GEO) ---
    r["updated_visible"]=bool(re.search(r"Updated\s+[A-Z][a-z]+ 20\d\d",bodytext))
    # --- transactional-only (#5/#6) ---
    if slug in TRANSACTIONAL:
        r["airport_codes"]=bool(re.search(r"\b(DEN|LAX|MIA|ORD|LAR)\b",bodytext))
    return r

def main():
    rows={s:audit(s) for s in SLUGS}
    # collect boolean checks (skip the informational string/int fields)
    info={"h_counts","schema_types","title_len","desc_len","img_total","ext_links",
          "internal_links","faqpage_count"}
    keys=[]
    for r in rows.values():
        for k in r:
            if k not in keys and k not in info and not k.startswith("_"): keys.append(k)
    print("\n=== INTERIOR 29-CHECK AUDIT ===  (✓ pass / ✗ FAIL / — n/a)\n")
    for s,r in rows.items():
        if r.get("_MISSING"): print(f"  ✗ {s}: dist/ MISSING — rebuild"); continue
        fails=[k for k in keys if k in r and r[k] is False]
        mark="✓" if not fails else "✗"
        print(f"{mark} {s}")
        print(f"    {r['h_counts']} | title:{r['title_len']} desc:{r['desc_len']} | "
              f"imgs:{r['img_total']} ext:{r['ext_links']} int:{r['internal_links']} | "
              f"FAQPage×{r['faqpage_count']} | schema:{r['schema_types']}")
        if fails: print("    FAIL → " + ", ".join(fails))
    print("\n=== CHECK ROLL-UP (pages failing each) ===")
    for k in keys:
        bad=[s for s,r in rows.items() if r.get(k) is False]
        if bad: print(f"  ✗ {k}: {len(bad)} → {', '.join(bad)}")
    print("\nDone. Subjective checks (voice/humor/Flesch/non-commodity/tone/brand-protocol) = manual spot-check.")

if __name__=="__main__":
    main()
```

- [ ] **Step 2: Ensure a fresh build exists**

Run: `npx astro build 2>&1 | tail -5`
Expected: `Complete!` / `<N> page(s) built`. If `dist/` is stale this is required before auditing.

- [ ] **Step 3: Run the auditor against one known page to sanity-check parsing**

Run: `python3 scripts/interior_29_audit.py | grep -A2 "african-grey-parrot-price"`
Expected: a line for the price page showing real H-counts, a non-zero schema list, and (because it's transactional) an `airport_codes` check present. If every check shows `✗`, the HTML parser path is wrong — fix before Task 2.

---

## Task 2: Run the full audit & write the scorecard

**Files:**
- Create: `sessions/2026-06-14-interior-29-check-audit.md`

- [ ] **Step 1: Run across all 18 and capture output**

Run: `python3 scripts/interior_29_audit.py | tee /tmp/cag-audit.txt`
Expected: 18 page blocks + a "CHECK ROLL-UP" listing which pages fail each check.

- [ ] **Step 2: Create the scorecard file** with: (a) the pasted roll-up, (b) a table of the 18 distinct merged checks (see "MY READ" section) marked PASS/FAIL/SPOT, (c) the manual spot-check from Task 3, (d) the "good/bad learnings" log, (e) GAP-FLAGs for the breeder. Use this skeleton:

```markdown
# Interior 18-Page · 29-Check Final QA Audit — 2026-06-14
## 1. Mechanical roll-up (scripts/interior_29_audit.py)
<paste /tmp/cag-audit.txt>
## 2. Distinct-check scorecard (29 merged → 18)
| # | Check (merged) | Source 29# | Result | Notes |
## 3. Manual spot-check (3-page sample) — Task 3
## 4. Learnings — what worked / what bit us
### ✅ Good (keep doing)
### ❌ Bad (don't repeat)
## 5. GAP-FLAGs for Mark & Teri (ledger-bounded, do NOT invent)
## 6. Open Decision: meta-length standard (#13 vs manual)
```

- [ ] **Step 3: Triage every `✗`** from the roll-up into the scorecard: real defect (fix now), accepted deviation (note why), or subjective/needs-eyes (defer to Task 3).

---

## Task 3: Subjective spot-check (the ~6 non-mechanical checks)

**Files:** read-only; findings → the scorecard from Task 2.

Sample = 1 per content type: `african-grey-parrot-price` (transactional), `african-grey-parrot-care-guide` (pillar), `african-grey-reviews` (trust). For each, manually verify:

- [ ] **Step 1: First-person voice (#19/20) + tone (#16)** — `grep -oE "\b(we|our|us)\b" dist/<slug>/index.html | wc -l` should be well above third-person "African Greys are…" filler; read the hero + first 2 sections to confirm "here at C.A.Gs" framing and warm tone.
- [ ] **Step 2: Honesty-Policy humor (#D.3)** — confirm ≤1 dry beat/section, none on legal/health.
- [ ] **Step 3: Flesch 60–70 (#15)** — paste the visible body into a Flesch calc (or `textstat` if available: `python3 -c "import textstat,sys;print(textstat.flesch_reading_ease(open('/tmp/body.txt').read()))"`). Record the score; if <60, flag as SHARPEN (not a hard fail — see trade-off note).
- [ ] **Step 4: Non-commodity detail (#24)** — confirm ≥1 high-resolution breeder detail per ~500 words; flag generic filler ("both make exceptional companions").
- [ ] **Step 5: Brand-protocol naming (#11)** — note whether any ownable house method is named; if not, write a GAP-FLAG proposing one for breeder sign-off (do NOT ship an invented protocol name).

---

## Task 4: Reconcile the 29 into the manual (after the Open Decision is answered)

**Files:**
- Modify: `MANUAL INTERIOR-PAGE CHECKLIST.md`

- [ ] **Step 1:** Add the **2 conflict reconciliations** — Part J.1 meta length (per the user's decision) and an explicit Part N line: *footer phone REQUIRED, body phone BANNED (#17 + Rule 61)*.
- [ ] **Step 2:** Add the **net-new checks** to their home Part, each with its scoping note: #5 logistics + #6 local authority → new Part C delta line *"transactional interior pages only; route airport/vet depth to location/buyer cluster"*; #11 brand-protocol → Part E (ledger-gated, GAP-FLAG first); #15 Flesch → Part H (target 60–70, documented floor); #18 newsletter 3 placements → Part C spine; #14 `<100KB` → Part J.2.
- [ ] **Step 3:** Add my **"in neither list" checks** to Part N: cannibalization sweep, orphan/reciprocity, single-FAQPage, alt uniqueness, 375px gate, visible `dateModified`.
- [ ] **Step 4:** Add a one-line note at the top of the manual: *"v2 (2026-06-14) — absorbed the 29-check final-QA pass; auditor = `scripts/interior_29_audit.py`."* Bump the TOC if a Part gains a sub-section.

---

## Task 5: Save learnings to memory

**Files:**
- Create: `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/project_interior_29check_audit.md`
- Modify: `/Users/apple/.claude/projects/-Users-apple-Downloads-CAG/memory/MEMORY.md` (one-line pointer)

- [ ] **Step 1:** Write the memory file (type: project): the auditor exists + path, the 18-check merged model, the 2 reconciled conflicts, the meta-length decision, and the top 3 "don't-repeat" defects the audit caught. Link `[[reference_interior_page_standard]]`, `[[project_interior_polish_rollout]]`, `[[project_interior_batch_complete]]`.
- [ ] **Step 2:** Add the index line to MEMORY.md under the interior cluster.

---

## Task 6: Commit & push

- [ ] **Step 1: Stage + commit**

```bash
git add scripts/interior_29_audit.py "sessions/2026-06-14-interior-29-check-audit.md" "MANUAL INTERIOR-PAGE CHECKLIST.md" "docs/superpowers/plans/2026-06-14-interior-29-check-audit.md"
git commit -m "qa(interior): 29-check final audit script + scorecard + manual v2 reconciliation

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

- [ ] **Step 2: Push (= deploy)**

```bash
git push
```
Expected: pushes to `main`. Then confirm: `git log origin/main..HEAD` is empty. ("Everything up-to-date" ≠ failure — the auto-push hook may have already pushed.)

> No `astro build` redeploy is required for Tasks 4–6 (script + docs + memory only); the page edits, if Task 3 surfaces real defects, get their own build + push per Part L.

---

## Self-Review

- **Spec coverage:** all 29 user items mapped (merges + 2 conflicts + 7 net-new + 6 my-additions) → Tasks 1–4. "Run on 18 pages" → Tasks 1–3. "Save good/bad" → Tasks 2 & 5. "Merge duplicates" → "MY READ" + Task 4. "Your opinion + what to add" → "MY READ" section. ✓
- **Placeholders:** auditor code is complete and runnable; scorecard/manual edits are content-specified, not "TBD". ✓
- **Consistency:** slug list, `dist/<slug>/index.html` path, and `scripts/interior_29_audit.py` name are identical across all tasks. ✓
- **Known limitation (stated honestly):** the auditor covers the *objective* subset; 6 checks are genuinely subjective and are spot-checked on a 3-page sample, not all 18 — auditing prose voice/humor/Flesch across 18 full pages by eye in one pass would be shallow or fabricated, so it's scoped to a representative sample with the rest deferred to per-page builders.

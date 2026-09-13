# Page Board System — Brief Parity (Tasks 17–24)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this amendment task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **Breeder mandate carried from the for-sale program: every value written into a board record — a section's why, a keyword, a CTA anchor, a tool decision, a schema type — is authored by the controlling session, never by a subagent. Harness code, schema files and tests may be delegated.** Steps marked **(controller)** are the controlling session's own.

**Goal:** Put the seven Universal Page Build Brief items the breeder approved on 2026-09-13 onto the Page Board, before the re-approval sitting, so one sitting approves them: the per-section image plan, a grounded why per section, the brief's full keyword-type set, the whole component tuple, the CTA plan, the tool decision and the schema plan.

**Source:** gap analysis `docs/artifacts/cags-board-brief-gap-analysis.md` (artifact `8be278cb`), items 1–7, "(Recommended)" and approved. Items 8–14 are deferred to the Cluster Wave boards by that same ruling and are out of scope here.

**Architecture:** unchanged from the additions plan. `schemas/board.schema.json` grows fields; `scripts/pageboard.py` grows validations, four helpers and gate rows; `scripts/build_page_board.py` grows one block (`3b. Image plan`) and extends blocks 1, 3, 4 and 5b. No new script, no new file format, and no change to `board_canvas.py`, `board_thumbs.mjs`, `board_approve.py` or `data/component-ledger.json`.

**Tech Stack:** Python 3 + `jsonschema` + pytest. Brief sections cited are from artifact `f63b8e4f` v2.2.
**Spec:** `docs/superpowers/specs/2026-09-12-page-board-system-design.md`. **Parent plans:** `2026-09-12-page-board-system.md` (Tasks 1–11), `2026-09-12-page-board-additions.md` (Tasks 12–16).

**Conventions that still hold:**
- Run everything from `/Users/apple/Downloads/CAG`.
- A PostToolUse hook pushes after every Bash call, so commit only once that task's full suite is green.
- Baseline before Task 17: `python3 -m pytest tests/test_page_board.py -q` → `155 passed`.
- Tasks 18–23 each add a **required** field. The moment its schema lands, the two real records under `data/pages/` stop validating, and `test_near_me_retrofit_board_renders_candidates_and_passes_the_gate` fails with them. So each task runs its new tests with `-k` first. Then **(controller)** stamps both records from the sources in **Retrofit**. Only then does the full suite run and the commit happen.

---

### Task 17: The image plan on the board (gap item 1, brief §15b–§15c)

**Files:** modify `scripts/pageboard.py`, `scripts/build_page_board.py`; test `tests/test_page_board.py`. No schema change and no record stamp: `sections[].images` already exists with a `prompt` on every entry. The hub carries 12, near-me 7, and the board shows none of them.

- [ ] **Step 1: Write the failing tests** (append to `tests/test_page_board.py`)

```python
def test_image_plan_lists_every_slot_with_its_prompt_and_flags_a_bare_signature_section():
    import build_page_board as BPB
    b = _approved(MIN_BOARD)
    html = BPB.render(b, ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert 'data-title="3b. Image plan"' in html
    assert "birds-opener" in html and "six bird cards" in html and "optional" in html
    b["sections"][0]["images"] = []
    html = BPB.render(b, ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert "**⚠ no image slot**" in html


def test_gate_warns_on_a_signature_section_with_no_image_and_fails_on_a_shared_alt():
    b = _approved(MIN_BOARD)
    checks = lambda: [(x["check"], x["sev"]) for x in
                      PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")]
    assert ("image-coverage", "WARN") not in checks()
    reserve = json.loads(json.dumps(b["sections"][0]))
    reserve.update({"id": "reserve", "n": 2, "shape": "standard", "images": [], "tree": []})
    b["sections"].append(reserve)
    assert ("image-coverage", "WARN") not in checks()          # a standard section is exempt
    b["sections"][0]["images"] = []
    assert ("image-coverage", "WARN") in checks()
    b["assets"] = [dict(b["assets"][0], alt="A Congo on its perch"),
                   dict(b["assets"][0], slot="card-01", alt="a congo on its perch.")]
    assert ("asset-alt-duplicate", "FAIL") in checks()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "image_plan or signature_section_with_no_image"`
Expected: `2 failed` — `assert 'data-title="3b. Image plan"' in html`, and `assert ('image-coverage', 'WARN') in ...`.

- [ ] **Step 3: Add the two helpers and the gate rows**

```python
# scripts/pageboard.py — directly after faq_questions()
def image_gaps(board):
    """Signature sections (shape ≠ standard) that plan no image. The brief puts an image
    under every H2 (§15b); a standard section — the FAQ, the form — wears its shell and no
    in-body image by design, so it is exempt rather than reported as a gap nobody will fill."""
    return [s["id"] for s in board["sections"] if s["shape"] != "standard" and not s["images"]]


def duplicate_alts(board):
    """{normalised alt: [slot, ...]} for every non-empty asset alt used twice (Rule 50b: no two
    images on a page share an alt). Compared on tokens, so a trailing full stop or a capital
    letter is not a second alt. An empty alt is an unwritten one, not a duplicate."""
    seen = {}
    for a in board["assets"]:
        key = " ".join(tokens(a["alt"]))
        if key:
            seen.setdefault(key, []).append(a["slot"])
    return {k: v for k, v in seen.items() if len(v) > 1}
```

```python
# scripts/pageboard.py — in gate_findings(), directly after the two meta-length loops and
# before `picks = (board.get("approval") or {}).get("picks", {})`
    for sid in image_gaps(board):
        add("image-coverage", "WARN", f"section {sid} plans no image slot — the brief puts one under every H2 (§15b)")
    for key, slots in duplicate_alts(board).items():
        add("asset-alt-duplicate", "FAIL",
            f"slots {', '.join(slots)} share one alt ({key!r}) — no two images on a page share an alt (Rule 50b)")
```

- [ ] **Step 4: Add block `3b. Image plan`**

```python
# scripts/build_page_board.py — directly after angles_table()
def image_plan_table(board):
    """One row per image slot the outline plans, prompt included: the infographic prompts ARE
    the generation pack (§15c), and a photo prompt says what the photo has to show. A
    signature section with no slot gets a row of its own, so the gap is on the board rather
    than only in the gate output."""
    rows = []
    for s in board["sections"]:
        label = f"{s['n']:02d} {md(s['heading'])}"
        if not s["images"]:
            rows.append([label, "—", "—", "—",
                         "_no image slot_" if s["shape"] == "standard" else "**⚠ no image slot**"])
        for i in s["images"]:
            rows.append([label, md(i["slot"]), md(i["kind"]),
                         "required" if i["required"] else "optional", md(i["prompt"]) or "_no prompt_"])
    return md_table(["Section", "Slot", "Kind", "Required", "Prompt"], rows)
```

```python
# scripts/build_page_board.py — in render(), directly after parts.append(("3. Outline", ...))
    parts.append(("3b. Image plan", image_plan_table(board)
                  + "\n\nEvery image slot the outline plans. Infographic prompts are the generation pack; "
                    "photo prompts say what the photo has to show. Page-level files and alts are in block 7."))
```

- [ ] **Step 5: Run the tests**

Run: `python3 -m pytest tests/test_page_board.py -q -k "image_plan or signature_section_with_no_image"` → `2 passed`
Run: `python3 -m pytest tests/test_page_board.py -q` → `157 passed`

- [ ] **Step 6: Commit**

```bash
git add scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py
git commit -m "feat(page-board): 3b. Image plan — every slot and prompt on the board; image-coverage and alt-duplicate gate rows

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 18: Group and a grounded why per section (gap item 2, brief §11)

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both `data/pages/<slug>/board.json`; test `tests/test_page_board.py`.

The brief labels every section MANDATORY, COMPETITOR-BASED or SUGGESTED-RECOMMENDED, each with a why grounded in Sprint 0 and the source named. The record has `category` A/B/C, but no source on disk defines A or B. The pipeline review (`docs/artifacts/cags-sprint-pipeline-review.md` line 236) defines only C, "the sections that are ours alone". So `group` is a new field authored per section, never derived from the letter. The one sourced mapping is enforced: category C is always SUGGESTED-RECOMMENDED. `category` stays, because the canvas and the options logic already read it.

- [ ] **Step 1: Write the failing tests, and give MIN_BOARD the new fields**

```python
# tests/test_page_board.py — in MIN_BOARD's one section, directly after "framework": "EEBP",
        "group": "MANDATORY",
        "why": "A for-sale hub that shows no birds above the fold reads as a directory, not a breeder.",
        "why_source": "docs/research/for-sale-keywords-2026-07.md",
```

```python
def test_section_why_is_required_c_is_always_ours_and_competitor_names_a_url():
    for mutate in (lambda s: s.pop("why"), lambda s: s.update(why="too short"),
                   lambda s: s.update(group="OPTIONAL")):
        bad = json.loads(json.dumps(MIN_BOARD)); mutate(bad["sections"][0])
        with pytest.raises(PB.BoardError):
            PB.validate_board(bad)
    bad = json.loads(json.dumps(MIN_BOARD)); bad["sections"][0]["category"] = "C"
    with pytest.raises(PB.BoardError, match="SUGGESTED-RECOMMENDED"):
        PB.validate_board(bad)
    bad = json.loads(json.dumps(MIN_BOARD)); bad["sections"][0]["group"] = "COMPETITOR-BASED"
    with pytest.raises(PB.BoardError, match="URL"):
        PB.validate_board(bad)
    ok = json.loads(json.dumps(MIN_BOARD))
    ok["sections"][0].update(group="COMPETITOR-BASED",
                             why_source="https://www.birdbreeders.com/birds/category/african-grey (ranks first with a grid)")
    PB.validate_board(ok)


def test_distribution_block_shows_group_and_grounded_why():
    import build_page_board as BPB
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert "**Why each section is here**" in html
    assert "reads as a directory, not a breeder." in html and "for-sale-keywords-2026-07.md" in html
    assert "[A · mandatory · inventory" in html                  # the outline line carries the group
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "section_why or grounded_why"`
Expected: `2 failed` — `board.schema.json: sections/0: Additional properties are not allowed ('group', 'why', 'why_source' were unexpected)`.

- [ ] **Step 3: Schema**

In `schemas/board.schema.json`, `sections.items.required` becomes:

```json
"required": ["id", "n", "heading", "intent", "category", "group", "why", "why_source", "framework", "words", "shape", "keywords", "entities", "tree", "images", "links", "options"],
```

and `sections.items.properties` gains, directly after `"category"`:

```json
          "group": {"enum": ["MANDATORY", "COMPETITOR-BASED", "SUGGESTED-RECOMMENDED"]},
          "why": {"type": "string", "minLength": 20, "maxLength": 400},
          "why_source": {"type": "string", "minLength": 1, "maxLength": 300},
```

- [ ] **Step 4: Validation**

```python
# scripts/pageboard.py — in validate_board(), inside the first `for sec in board["sections"]:`
# loop, directly after the words.min > words.max check
        if sec["category"] == "C" and sec["group"] != "SUGGESTED-RECOMMENDED":
            # The pipeline review defines C as "the sections that are ours alone" — the one
            # letter with a written meaning, so the one mapping the record may not contradict.
            raise BoardError(f"section {sec['id']}: category C is a section that is ours alone, so its group is "
                             f"SUGGESTED-RECOMMENDED, not {sec['group']}")
        if sec["group"] == "COMPETITOR-BASED" and not re.search(r"https?://", sec["why_source"]):
            raise BoardError(f"section {sec['id']}: a COMPETITOR-BASED section cites the competitor it answers — "
                             "why_source carries no URL")
```

- [ ] **Step 5: Render the group and the why**

```python
# scripts/build_page_board.py — directly after STANDARD_FORM_DEFAULT
GROUP_SHORT = {"MANDATORY": "mandatory", "COMPETITOR-BASED": "competitor", "SUGGESTED-RECOMMENDED": "ours"}
```

In `outline_block()`, the H2 line becomes:

```python
        lines.append(f"├─ H2 {s['n']:02d}  {esc(s['heading'])}   [{s['category']} · {GROUP_SHORT[s['group']]} · {s['shape']} · {s['framework']} · {s['words']['min']}–{s['words']['max']}w]" + flag(s["heading"], hit_by))
```

In `render()`, the block-4 append becomes:

```python
    why_rows = [[f"{s['n']:02d} {md(s['heading'])}", md(s["group"]), md(s["framework"]), md(s["why"]), md(s["why_source"])]
                for s in board["sections"]]
    parts.append(("4. Distribution", md_table(["Section", "Primary", "LSI", "Long-tail", "Brand", "Geo", "Words"], rows)
                  + f"\n\nHeadings: H1 {c['h1']} · H2 {c['h2']} · H3 {c['h3']} · H4 {c['h4']} · H5 {c['h5']} · H6 {c['h6']}. Counts are ceilings, not floors."
                  + "\n\n**Why each section is here**\n\n"
                  + md_table(["Section", "Group", "Framework", "Why", "Source"], why_rows)))
```

- [ ] **Step 6: Run the new tests**

Run: `python3 -m pytest tests/test_page_board.py -q -k "section_why or grounded_why"` → `2 passed`

- [ ] **Step 7 (controller): Stamp both records** — `group`, `why` and `why_source` on all 18 sections, from **Retrofit → group / why**.

Run: `python3 -c "import sys; sys.path.insert(0,'scripts'); import pageboard as PB; [PB.load_board(s) for s in ('african-grey-parrots-for-sale','african-grey-parrots-for-sale-near-me')]; print('ok')"`
Expected: `ok`

- [ ] **Step 8: Full suite and commit**

Run: `python3 -m pytest tests/test_page_board.py -q` → `159 passed`

```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): section group + grounded why (brief §11); category C tied to SUGGESTED-RECOMMENDED

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 19: The brief's eight keyword types (gap item 3, brief §7b)

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both records; test `tests/test_page_board.py`.

The record carries five arrays (primary, lsi, longtail, brand, geo). Brief §7b names eight types; the four missing are conversational/voice, comparison, solution and transactional. `geo` stays: it is not in §7b but drives the location distribution. So a section carries nine arrays, and one tuple of names drives the schema check, `distribution()` and the block-4 columns, so the three can never drift.

- [ ] **Step 1: Write the failing test; update MIN_BOARD and the existing totals test**

```python
# tests/test_page_board.py — MIN_BOARD's "keywords" becomes
        "keywords": {"primary": ["african grey parrots for sale"], "lsi": [], "longtail": [], "brand": [], "geo": [],
                     "conversational": [], "comparison": [], "solution": [], "transactional": []},
```

In `test_distribution_totals_add_across_two_sections`, `second["keywords"]` and the totals assertion become:

```python
    second["keywords"] = {"primary": ["african grey shipping"], "lsi": ["iata"],
                          "longtail": [], "brand": ["c.a.gs"], "geo": ["midland", "texas"],
                          "conversational": [], "comparison": [], "solution": [], "transactional": []}
```
```python
    assert d["totals"] == {"primary": 2, "lsi": 1, "longtail": 0, "brand": 1, "geo": 2,
                           "conversational": 0, "comparison": 0, "solution": 0, "transactional": 0,
                           "words_min": 650, "words_max": 900}
```

```python
def test_keywords_carry_the_briefs_eight_types_plus_geo():
    import build_page_board as BPB
    bad = json.loads(json.dumps(MIN_BOARD)); del bad["sections"][0]["keywords"]["transactional"]
    with pytest.raises(PB.BoardError):
        PB.validate_board(bad)
    b = json.loads(json.dumps(MIN_BOARD))
    b["sections"][0]["keywords"]["transactional"] = ["reserve an african grey", "african grey deposit"]
    PB.validate_board(b)
    assert PB.distribution(b)["totals"]["transactional"] == 2
    html = BPB.render(_approved(b), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert "| Section | Primary | LSI | Long-tail | Brand | Geo | Voice | Compare | Solution | Transact | Words |" in html
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m pytest tests/test_page_board.py -q -k "eight_types or totals_add"`
Expected: `2 failed` — `Additional properties are not allowed ('conversational', 'comparison', 'solution', 'transactional' were unexpected)`.

- [ ] **Step 3: Schema**

In `schemas/board.schema.json`, the section `keywords` object becomes:

```json
          "keywords": {"type": "object",
                       "required": ["primary", "lsi", "longtail", "brand", "geo", "conversational", "comparison", "solution", "transactional"],
                       "additionalProperties": false,
                       "properties": {"primary": {"type": "array", "items": {"type": "string"}}, "lsi": {"type": "array", "items": {"type": "string"}},
                                      "longtail": {"type": "array", "items": {"type": "string"}}, "brand": {"type": "array", "items": {"type": "string"}},
                                      "geo": {"type": "array", "items": {"type": "string"}},
                                      "conversational": {"type": "array", "items": {"type": "string"}}, "comparison": {"type": "array", "items": {"type": "string"}},
                                      "solution": {"type": "array", "items": {"type": "string"}}, "transactional": {"type": "array", "items": {"type": "string"}}}},
```

- [ ] **Step 4: One tuple of names for the library and the board**

```python
# scripts/pageboard.py — directly above distribution()
KEYWORD_TYPES = ("primary", "lsi", "longtail", "brand", "geo",
                 "conversational", "comparison", "solution", "transactional")
KEYWORD_LABELS = {"primary": "Primary", "lsi": "LSI", "longtail": "Long-tail", "brand": "Brand", "geo": "Geo",
                  "conversational": "Voice", "comparison": "Compare", "solution": "Solution", "transactional": "Transact"}


def distribution(board):
    rows, totals = [], {**{k: 0 for k in KEYWORD_TYPES}, "words_min": 0, "words_max": 0}
    for s in board["sections"]:
        row = {"section": s["id"], "heading": s["heading"]}
        for k in KEYWORD_TYPES:
            row[k] = len(s["keywords"][k]); totals[k] += row[k]
        row["words_min"], row["words_max"] = s["words"]["min"], s["words"]["max"]
        totals["words_min"] += row["words_min"]; totals["words_max"] += row["words_max"]
        rows.append(row)
    counts = {f"h{n}": 0 for n in range(1, 7)}
    for lvl, _ in all_headings(board):
        counts[f"h{lvl}"] += 1
    return {"rows": rows, "totals": totals, "h_counts": counts}
```

```python
# scripts/build_page_board.py — in render(), the rows/totals lines and the block-4 append become
    rows = [[md(r["section"])] + [r[k] for k in PB.KEYWORD_TYPES] + [f"{r['words_min']}–{r['words_max']}"] for r in d["rows"]]
    t = d["totals"]
    rows.append(["**totals**"] + [t[k] for k in PB.KEYWORD_TYPES] + [f"{t['words_min']}–{t['words_max']}"])
    c = d["h_counts"]
    why_rows = [[f"{s['n']:02d} {md(s['heading'])}", md(s["group"]), md(s["framework"]), md(s["why"]), md(s["why_source"])]
                for s in board["sections"]]
    parts.append(("4. Distribution", md_table(["Section"] + [PB.KEYWORD_LABELS[k] for k in PB.KEYWORD_TYPES] + ["Words"], rows)
                  + f"\n\nHeadings: H1 {c['h1']} · H2 {c['h2']} · H3 {c['h3']} · H4 {c['h4']} · H5 {c['h5']} · H6 {c['h6']}. Counts are ceilings, not floors."
                  + "\n\n**Why each section is here**\n\n"
                  + md_table(["Section", "Group", "Framework", "Why", "Source"], why_rows)))
```

- [ ] **Step 5: Run the new tests**

Run: `python3 -m pytest tests/test_page_board.py -q -k "eight_types or totals_add"` → `2 passed`

- [ ] **Step 6 (controller): Stamp both records** — the four new arrays on all 18 sections, from **Retrofit → keywords**. Re-run the Task 18 Step 7 load command → `ok`.

- [ ] **Step 7: Full suite and commit**

Run: `python3 -m pytest tests/test_page_board.py -q` → `160 passed`

```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): the brief's eight keyword types (§7b) in the record and the distribution matrix

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 20: The whole tuple on the kit strip (gap item 4, brief §13)

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both records; test `tests/test_page_board.py`.

Brief §13's tuple has nine axes: hero, dial, rail, stepper, key takeaway, TOC, table, FAQ and newsletter placement. The strip shows five. `takeaway` and `table` are already in the record, so this task shows them. `stepper` and `newsletter` are new record fields. Newsletter placement is a section id plus the kit §11 variant letter (A/B/C, `assets/1WORKING-ON/FOR-SALE-PAGES/FOR-SALE-PAGES:components-NAMES.md` line 997).

**Deliberately NOT added to the component ledger or `TUPLE_ID_KEYS`.** None of the 12 ledger rows records a stepper or a newsletter placement. An ownership rule would therefore compare against empty strings and prove nothing. They join the ownership rules when the Cluster Wave boards have a population to compare.

- [ ] **Step 1: Write the failing tests; give MIN_BOARD the fields**

```python
# tests/test_page_board.py — MIN_BOARD's "tuple" becomes
    "tuple": {"hero": "hero-a", "dial": "dial-1", "rail": "rail-a", "toc": "t1", "takeaway": ["k1"],
              "table": "table-a", "faq": "faq-a", "stepper": "", "newsletter": {"after": "", "variant": ""},
              "h6_prefixes": ["Aviary Note:", "From the Book:", "Ask Us:"]},
```

```python
def test_tuple_newsletter_names_a_real_section_and_sets_both_fields_together():
    for nl in ({"after": "birds", "variant": ""}, {"after": "", "variant": "A"},
               {"after": "shipping", "variant": "A"}, {"after": "birds", "variant": "D"}):
        bad = json.loads(json.dumps(MIN_BOARD)); bad["tuple"]["newsletter"] = nl
        with pytest.raises(PB.BoardError):
            PB.validate_board(bad)
    ok = json.loads(json.dumps(MIN_BOARD)); ok["tuple"]["newsletter"] = {"after": "birds", "variant": "B"}
    PB.validate_board(ok)


def test_kit_strip_shows_takeaway_table_stepper_and_the_newsletter():
    import build_page_board as BPB
    b = _approved(MIN_BOARD)
    b["tuple"].update(takeaway=["k1", "k2"], newsletter={"after": "birds", "variant": "B"})
    html = BPB.render(b, ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    for shell in ("table-a", "k1", "k2"):
        assert f'<div class="nothumb">{shell}</div>' in html
    assert "this page wears no stepper" in html
    assert "after 01 · What Do We Have for Sale Right Now?" in html and "variant B" in html
    b["tuple"]["newsletter"] = {"after": "", "variant": ""}
    assert "this page places no newsletter" in BPB.render(b, ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
```

- [ ] **Step 2: Run to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "tuple_newsletter or takeaway_table_stepper"`
Expected: `2 failed` — `tuple: Additional properties are not allowed ('newsletter', 'stepper' were unexpected)`.

- [ ] **Step 3: Schema**

In `schemas/board.schema.json`, `tuple` becomes:

```json
    "tuple": {
      "type": "object", "required": ["hero", "dial", "rail", "toc", "takeaway", "table", "faq", "stepper", "newsletter", "h6_prefixes"], "additionalProperties": false,
      "properties": {
        "hero": {"type": "string"}, "dial": {"type": "string"}, "rail": {"type": "string"}, "toc": {"type": "string"},
        "takeaway": {"type": "array", "items": {"type": "string"}}, "table": {"type": "string"}, "faq": {"type": "string"},
        "stepper": {"type": "string"},
        "newsletter": {"type": "object", "required": ["after", "variant"], "additionalProperties": false,
                       "properties": {"after": {"type": "string"}, "variant": {"enum": ["", "A", "B", "C"]}}},
        "h6_prefixes": {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": ":$"}}
      }
    },
```

- [ ] **Step 4: Validation**

```python
# scripts/pageboard.py — in validate_board(), directly after the duplicate id/n loop
    nl = board["tuple"]["newsletter"]
    if bool(nl["after"]) != bool(nl["variant"]):
        raise BoardError("tuple.newsletter: `after` and `variant` are set together or not at all "
                         f"(after={nl['after']!r}, variant={nl['variant']!r})")
    if nl["after"] and nl["after"] not in ids:
        raise BoardError(f"tuple.newsletter.after {nl['after']!r} is not a section id ({', '.join(ids)})")
```

- [ ] **Step 5: The kit strip shows all nine axes**

Replace `KIT_AXES` and `kit_cards()` in `scripts/build_page_board.py` (`kit_thumb()` is unchanged):

```python
KIT_AXES = ("hero", "dial", "rail", "toc", "table", "stepper", "faq")


def _kit_card(axis, v, owned, thumbs):
    """One shell card. An empty axis is shown as worn-by-nobody rather than dropped, so a
    page without a stepper says so instead of looking like a strip with a card missing."""
    if not v:
        return (f'<div class="opt off"><span class="pill">{esc(axis)}</span><div class="nothumb">none</div>'
                f'<span class="why">this page wears no {esc(axis)}</span></div>')
    base = PB.base_of(v)
    delta = v.split("#", 1)[1].strip() if "#" in v else ""
    th = kit_thumb(v, thumbs)
    img = (f'<img src="{esc(th)}" alt="{esc(base)} — the {esc(axis)} this page wears">'
           if th else f'<div class="nothumb">{esc(base)}</div>')
    owners = owned.get(v) or owned.get(base) or []
    return (f'<div class="opt"><span class="pill">{esc(axis)}</span>{img}<b>{esc(base)}</b>'
            + (f'<span class="pill">refresh: {esc(delta)}</span>' if delta else "")
            + f'<span class="why">{"also worn by " + esc(", ".join(owners)) if owners else "new to the cluster"}'
              "</span></div>")


def kit_cards(board, ledger, thumbs, slug):
    """Every tuple axis this page wears (brief §13): seven shells, each takeaway card, and the
    newsletter placement — shown, never offered. Block 6 picks per section; the tuple is the
    author's decision against the ledger, and a radio here would invite a choice the ledger
    rules decide, not the sitting."""
    t = board["tuple"]
    owned = PB.owned_components(ledger, exclude_slug=slug)
    cards = [_kit_card(axis, (t.get(axis) or "").strip(), owned, thumbs) for axis in KIT_AXES]
    cards += [_kit_card("takeaway", k.strip(), owned, thumbs) for k in (t.get("takeaway") or [""])]
    nl = t["newsletter"]
    if nl["after"]:
        sec = next(s for s in board["sections"] if s["id"] == nl["after"])
        cards.append(f'<div class="opt"><span class="pill">newsletter</span><div class="nothumb">variant {esc(nl["variant"])}</div>'
                     f'<b>after {sec["n"]:02d} · {esc(sec["heading"])}</b>'
                     '<span class="why">kit §11 clutch-alert signup, placed in context</span></div>')
    else:
        cards.append('<div class="opt off"><span class="pill">newsletter</span><div class="nothumb">none</div>'
                     '<span class="why">this page places no newsletter</span></div>')
    return cards
```

- [ ] **Step 6: Run the new tests and the existing kit tests**

Run: `python3 -m pytest tests/test_page_board.py -q -k "kit or tuple_newsletter"` → `4 passed`

- [ ] **Step 7 (controller): Stamp both records** — `tuple.stepper` and `tuple.newsletter`, from **Retrofit → tuple**. Re-run the load command → `ok`.

- [ ] **Step 8: Full suite and commit**

Run: `python3 -m pytest tests/test_page_board.py -q` → `162 passed`

```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): the whole tuple on the kit strip — table, takeaway, stepper, newsletter placement (§13)

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 21: The CTA plan (gap item 5, brief §10 and §16d)

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both records; test `tests/test_page_board.py`.

Brief: a reserve CTA every 500–700 words, branded action anchors, `#reserve`, one global CTA per page. A per-section boolean cannot express a 1,100-word FAQ carrying two CTAs, so a section records a **count** (`cta`, 0–6, absent = 0). The gate reads word-band midpoints and raises two WARNs, never a FAIL. Bands are estimates, so a gap on the board is a prompt to look, not proof of a defect.
- `cta-cadence`: total words ÷ total CTAs is over the cadence maximum.
- `cta-gap`: a run of consecutive CTA-free sections is over the maximum.

- [ ] **Step 1: Write the failing tests; give MIN_BOARD the fields**

```python
# tests/test_page_board.py — MIN_BOARD's "brief", directly after "strategy": {...}
              "cta": {"cadence": {"min": 500, "max": 700}, "destination": "#reserve",
                      "anchors": ["Reserve This Bird"], "global_cta": "hidden"},
# and in MIN_BOARD's one section, directly after "shape": "inventory",
        "cta": 1,
```

```python
def test_cta_plan_validates_cadence_destination_and_needs_one_cta():
    for mutate in (lambda b: b["sections"][0].update(cta=0),
                   lambda b: b["brief"]["cta"]["cadence"].update(min=800),
                   lambda b: b["brief"]["cta"].update(destination="reserve"),
                   lambda b: b["brief"]["cta"].update(anchors=[])):
        bad = json.loads(json.dumps(MIN_BOARD)); mutate(bad)
        with pytest.raises(PB.BoardError):
            PB.validate_board(bad)


def test_gate_warns_on_thin_cta_cadence_and_a_long_cta_free_run():
    b = json.loads(json.dumps(MIN_BOARD))
    assert PB.cta_findings(b) == []                            # one CTA in ~500 words
    ship = json.loads(json.dumps(b["sections"][0]))
    ship.update({"id": "shipping", "n": 2, "words": {"min": 700, "max": 900}, "cta": 0, "tree": []})
    b["sections"].append(ship)
    found = dict(PB.cta_findings(b))
    assert set(found) == {"cta-cadence", "cta-gap"}            # ~1300 words on one CTA; shipping runs ~800 bare
    assert "shipping" in found["cta-gap"]
    f = [x for x in PB.gate_findings(_approved(b), ONT_OK, LEDGER_EMPTY, live={}, stage="build")
         if x["check"].startswith("cta-")]
    assert sorted((x["check"], x["sev"]) for x in f) == [("cta-cadence", "WARN"), ("cta-gap", "WARN")]


def test_board_renders_the_cta_plan_and_marks_cta_sections():
    import build_page_board as BPB
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert "**CTA plan.** One every 500–700 words" in html and "Reserve This Bird" in html
    assert "hidden on this page" in html and "400–600w · CTA×1]" in html
```

- [ ] **Step 2: Run to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "cta"`
Expected: `3 failed` — `brief: Additional properties are not allowed ('cta' was unexpected)`.

- [ ] **Step 3: Schema**

In `schemas/board.schema.json`, `brief.required` gains `"cta"`, and `brief.properties` gains, directly after `"strategy"`:

```json
        "cta": {"type": "object", "required": ["cadence", "destination", "anchors", "global_cta"], "additionalProperties": false,
                "properties": {
                  "cadence": {"type": "object", "required": ["min", "max"], "additionalProperties": false,
                              "properties": {"min": {"type": "integer", "minimum": 100}, "max": {"type": "integer", "minimum": 100}}},
                  "destination": {"type": "string", "pattern": "^#[a-z][a-z0-9-]*$"},
                  "anchors": {"type": "array", "minItems": 1, "uniqueItems": true, "items": {"type": "string", "minLength": 2, "maxLength": 60}},
                  "global_cta": {"enum": ["hidden", "shown"]}}},
```

`sections.items.properties` gains, directly after `"shape"`:

```json
          "cta": {"type": "integer", "minimum": 0, "maximum": 6},
```

- [ ] **Step 4: Validation and the gate helper**

```python
# scripts/pageboard.py — in validate_board(), directly after the `for a in brief["angles"]:` loop
    cad = brief["cta"]["cadence"]
    if cad["min"] > cad["max"]:
        raise BoardError(f"brief.cta.cadence: min {cad['min']} > max {cad['max']}")
    if not any(s.get("cta", 0) for s in board["sections"]):
        raise BoardError("no section carries a CTA — a transactional page with a CTA plan places at least one")
```

```python
# scripts/pageboard.py — directly after duplicate_alts()
def cta_findings(board):
    """[(check, message)] for the CTA plan, read on word-band MIDPOINTS. Bands are estimates,
    so both findings are prompts to look rather than proof: `cta-cadence` when the page's
    words per CTA exceed the plan's maximum, `cta-gap` for each run of consecutive CTA-free
    sections longer than that maximum. A section's `cta` is a count, not a flag: a long FAQ
    can carry two."""
    cap = board["brief"]["cta"]["cadence"]["max"]
    mid = lambda s: (s["words"]["min"] + s["words"]["max"]) // 2
    total = sum(mid(s) for s in board["sections"])
    n = sum(s.get("cta", 0) for s in board["sections"])
    out = []
    if n == 0 or total / n > cap:
        out.append(("cta-cadence", f"{n} CTA(s) across ~{total} words is one per ~{total // max(n, 1)} — "
                                   f"the plan allows at most {cap}"))
    run, ids = 0, []
    for s in board["sections"] + [None]:
        if s is not None and not s.get("cta", 0):
            run += mid(s); ids.append(s["id"]); continue
        if run > cap:
            out.append(("cta-gap", f"sections {', '.join(ids)} run ~{run} words with no CTA — the plan allows at most {cap}"))
        run, ids = 0, []
    return out
```

```python
# scripts/pageboard.py — in gate_findings(), directly after the asset-alt-duplicate loop (Task 17)
    for check, msg in cta_findings(board):
        add(check, "WARN", msg)
```

- [ ] **Step 5: Render the plan and the per-section count**

```python
# scripts/build_page_board.py — directly after image_plan_table()
def decisions_lines(brief):
    """The page-level decisions the brief gates on (§10, §14, §16d), one bold-led line each,
    so the sitting reads them beside the strategy they serve."""
    c = brief["cta"]
    return [f"**CTA plan.** One every {c['cadence']['min']}–{c['cadence']['max']} words, to {md(c['destination'])}; "
            f"anchors: {', '.join(md(a) for a in c['anchors'])}; the site-wide CTA band is "
            f"{'hidden on this page' if c['global_cta'] == 'hidden' else 'shown'}."]
```

In `render()`, block 1's list gains `*decisions_lines(brief),` directly after the `**Strategy: …` line:

```python
        f"**Strategy: {md(brief['strategy']['name'])}.** Why: {md(brief['strategy']['why'])}",
        *decisions_lines(brief),
```

In `outline_block()`, the H2 line (Task 18's version) becomes:

```python
        cta = f" · CTA×{s['cta']}" if s.get("cta") else ""
        lines.append(f"├─ H2 {s['n']:02d}  {esc(s['heading'])}   [{s['category']} · {GROUP_SHORT[s['group']]} · {s['shape']} · {s['framework']} · {s['words']['min']}–{s['words']['max']}w{cta}]" + flag(s["heading"], hit_by))
```

- [ ] **Step 6: Run the new tests**

Run: `python3 -m pytest tests/test_page_board.py -q -k "cta"` → `3 passed`

- [ ] **Step 7 (controller): Stamp both records** — `brief.cta` and each section's `cta` count, from **Retrofit → CTA**. Re-run the load command → `ok`.

- [ ] **Step 8: Full suite and commit**

Run: `python3 -m pytest tests/test_page_board.py -q` → `165 passed`

```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): the CTA plan (§10, §16d) — cadence, anchors, per-section counts, cta-cadence and cta-gap WARNs

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 22: The tool decision (gap item 6, brief §14)

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both records; test `tests/test_page_board.py`.

§14: a tool or special element is required unless the page type genuinely does not support one. The decision ships with its evidence, and "no tool" names its evidence too. The field is required, so the schema enforces the decision and no gate row is needed. A real tool also carries its trade-off.

- [ ] **Step 1: Write the failing tests; give MIN_BOARD the field**

```python
# tests/test_page_board.py — MIN_BOARD's "brief", directly after "cta": {...}
              "tool": {"pick": "none",
                       "evidence": "No top-10 result for the head term ships a calculator or quiz, and the fan-out has no 'calculate' query.",
                       "trade_off": ""},
```

```python
def test_tool_decision_requires_evidence_and_a_trade_off_for_a_real_tool():
    for mutate in (lambda t: t.update(evidence="none seen"),
                   lambda t: t.update(pick="first-year cost calculator", trade_off=""),
                   lambda t: t.pop("pick")):
        bad = json.loads(json.dumps(MIN_BOARD)); mutate(bad["brief"]["tool"])
        with pytest.raises(PB.BoardError):
            PB.validate_board(bad)
    ok = json.loads(json.dumps(MIN_BOARD))
    ok["brief"]["tool"].update(pick="first-year cost calculator", trade_off="adds JS to a page that ships none today")
    PB.validate_board(ok)


def test_board_renders_the_tool_decision():
    import build_page_board as BPB
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert "**Tool.** none — evidence: No top-10 result for the head term" in html
```

- [ ] **Step 2: Run to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "tool_decision"`
Expected: `2 failed` — `brief: Additional properties are not allowed ('tool' was unexpected)`.

- [ ] **Step 3: Schema**

`brief.required` gains `"tool"`; `brief.properties` gains, directly after `"cta"`:

```json
        "tool": {"type": "object", "required": ["pick", "evidence", "trade_off"], "additionalProperties": false,
                 "properties": {"pick": {"type": "string", "minLength": 1, "maxLength": 120},
                                "evidence": {"type": "string", "minLength": 20, "maxLength": 400},
                                "trade_off": {"type": "string", "maxLength": 240}}},
```

- [ ] **Step 4: Validation**

```python
# scripts/pageboard.py — in validate_board(), directly after the Task 21 CTA checks
    tool = brief["tool"]
    if tool["pick"].strip().lower() != "none" and not tool["trade_off"].strip():
        raise BoardError(f"brief.tool: {tool['pick']!r} is a real tool and records no trade_off (§14)")
```

- [ ] **Step 5: Render**

`decisions_lines()` in `scripts/build_page_board.py` becomes:

```python
def decisions_lines(brief):
    """The page-level decisions the brief gates on (§10, §14, §16d), one bold-led line each,
    so the sitting reads them beside the strategy they serve."""
    c, tool = brief["cta"], brief["tool"]
    return [f"**CTA plan.** One every {c['cadence']['min']}–{c['cadence']['max']} words, to {md(c['destination'])}; "
            f"anchors: {', '.join(md(a) for a in c['anchors'])}; the site-wide CTA band is "
            f"{'hidden on this page' if c['global_cta'] == 'hidden' else 'shown'}.",
            f"**Tool.** {md(tool['pick'])} — evidence: {md(tool['evidence'])}"
            + (f" Trade-off: {md(tool['trade_off'])}" if tool["trade_off"].strip() else "")]
```

- [ ] **Step 6: Run the new tests**

Run: `python3 -m pytest tests/test_page_board.py -q -k "tool_decision"` → `2 passed`

- [ ] **Step 7 (controller): Stamp both records** — `brief.tool`, from **Retrofit → tool**. Re-run the load command → `ok`.

- [ ] **Step 8: Full suite and commit**

Run: `python3 -m pytest tests/test_page_board.py -q` → `167 passed`

```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): the tool decision (§14) with evidence, and a trade-off for any real tool

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 23: The schema plan (gap item 7, brief §8 and §16d)

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both records; test `tests/test_page_board.py`.

The record names the page's own JSON-LD types and its offer model. Validation ties the two together. At **release**, the gate reads the built page's JSON-LD:
- a planned type the page does not carry → FAIL
- a block that does not parse → FAIL
- no built page at all → FAIL (a plan checked against nothing is not a pass)

Extra types are not reported. Every page carries site-wide `LocalBusiness` and `Organization` from the layout, so an "unplanned type" rule would fire on every page.

**No page-type rule for the offer model.** The brief says AggregateOffer belongs "only on group and hub pages". But near-me's record says `page_type: for-sale`, and its built page carries AggregateOffer (measured 2026-09-13) because it is a router over several birds. A page-type rule would fire on a correct page, so the offer model is recorded and read by the sitting, not inferred.

- [ ] **Step 1: Write the failing tests; give MIN_BOARD the field**

```python
# tests/test_page_board.py — MIN_BOARD's "brief", directly after "tool": {...}
              "schema": {"types": ["AggregateOffer", "FAQPage"], "offer_model": "aggregate-offer"},
```

```python
def test_schema_plan_ties_offer_model_to_its_types():
    for sch in ({"types": ["AggregateOffer"], "offer_model": "product-offer-per-bird"},
                {"types": ["Offer", "FAQPage"], "offer_model": "none"},
                {"types": ["FAQPage"], "offer_model": "aggregate-offer"},
                {"types": ["faqpage"], "offer_model": "none"}):
        bad = json.loads(json.dumps(MIN_BOARD)); bad["brief"]["schema"] = sch
        with pytest.raises(PB.BoardError):
            PB.validate_board(bad)
    ok = json.loads(json.dumps(MIN_BOARD))
    ok["brief"]["schema"] = {"types": ["Product", "Offer", "FAQPage"], "offer_model": "product-offer-per-bird"}
    PB.validate_board(ok)


def test_release_gate_reads_json_ld_from_the_built_page(tmp_path, monkeypatch):
    page = tmp_path / "x" / "index.html"
    page.parent.mkdir()
    page.write_text('<script type="application/ld+json">{"@graph":[{"@type":"Product","offers":{"@type":"AggregateOffer"}}]}</script>'
                    '<script type="application/ld+json">{broken</script>', encoding="utf-8")
    monkeypatch.setattr(PB, "DIST", tmp_path)
    assert PB.dist_schema_types("x") == ({"Product", "AggregateOffer"}, 1)
    b = _approved(MIN_BOARD)
    schema_rows = lambda stage: sorted((x["check"], x["msg"].split(" ")[0]) for x in
                                       PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage=stage)
                                       if x["check"].startswith("schema-"))
    assert schema_rows("build") == []
    assert schema_rows("release") == [("schema-planned-missing", "FAQPage"), ("schema-unparsed", "1")]
    monkeypatch.setattr(PB, "DIST", tmp_path / "nowhere")
    assert [c for c, _ in schema_rows("release")] == ["schema-examined-zero"]


def test_board_renders_the_schema_plan():
    import build_page_board as BPB
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert "**Schema plan.** offer model aggregate-offer; types: AggregateOffer, FAQPage." in html
```

- [ ] **Step 2: Run to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k "schema_plan or json_ld"`
Expected: `3 failed` — `brief: Additional properties are not allowed ('schema' was unexpected)`.

- [ ] **Step 3: Schema**

`brief.required` gains `"schema"`; `brief.properties` gains, directly after `"tool"`:

```json
        "schema": {"type": "object", "required": ["types", "offer_model"], "additionalProperties": false,
                   "properties": {"types": {"type": "array", "minItems": 1, "uniqueItems": true,
                                            "items": {"type": "string", "pattern": "^[A-Z][A-Za-z]+$"}},
                                  "offer_model": {"enum": ["product-offer-per-bird", "aggregate-offer", "none"]}}},
```

- [ ] **Step 4: Validation, the dist reader and the release rows**

```python
# scripts/pageboard.py — in validate_board(), directly after the Task 22 tool check
    sch = brief["schema"]
    types = set(sch["types"])
    need = {"product-offer-per-bird": {"Product", "Offer"}, "aggregate-offer": {"AggregateOffer"}, "none": set()}[sch["offer_model"]]
    if not need <= types:
        raise BoardError(f"brief.schema: offer_model {sch['offer_model']} needs {', '.join(sorted(need - types))} in types")
    if sch["offer_model"] == "none" and types & {"Offer", "AggregateOffer"}:
        raise BoardError("brief.schema: offer_model none, but types name an Offer — a page that sells nothing marks up no offer")
```

```python
# scripts/pageboard.py — directly after cta_findings()
_LD_JSON = re.compile(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', re.S | re.I)


def dist_schema_types(slug, dist=None):
    """(types, unparsed) for the built page: every @type anywhere in its JSON-LD, nested
    offers and @graph members included, and the count of blocks that do not parse. None when
    the page is not built. DIST is read at call time, so a test can point it elsewhere."""
    root = pathlib.Path(DIST if dist is None else dist)
    page = root / "index.html" if slug == "index" else root / slug / "index.html"
    if not page.exists():
        return None
    types, unparsed = set(), 0

    def walk(o):
        if isinstance(o, dict):
            t = o.get("@type")
            types.update([t] if isinstance(t, str) else [x for x in t or [] if isinstance(x, str)])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for blk in _LD_JSON.findall(page.read_text(encoding="utf-8", errors="ignore")):
        try:
            walk(json.loads(blk))
        except json.JSONDecodeError:
            unparsed += 1
    return types, unparsed
```

In `gate_findings()`, the closing release block becomes:

```python
    if stage == "release":
        for a in board["assets"]:
            if a["required"] and a["status"] != "baked":
                add("asset-required-missing", "FAIL", f"required slot {a['slot']} ({a['kind']} {a['w']}x{a['h']}) is {a['status']}")
        got = dist_schema_types(slug)
        if got is None:
            add("schema-examined-zero", "FAIL", f"no built page for {slug} — the schema plan examined nothing")
        else:
            found, unparsed = got
            for tname in board["brief"]["schema"]["types"]:
                if tname not in found:
                    add("schema-planned-missing", "FAIL", f"{tname} is in the schema plan but not in the built page's JSON-LD")
            if unparsed:
                add("schema-unparsed", "FAIL", f"{unparsed} JSON-LD block(s) on the built page do not parse")
    return f
```

- [ ] **Step 5: Render**

`decisions_lines()` in `scripts/build_page_board.py` becomes:

```python
def decisions_lines(brief):
    """The page-level decisions the brief gates on (§8, §10, §14, §16d), one bold-led line
    each, so the sitting reads them beside the strategy they serve."""
    c, tool, sch = brief["cta"], brief["tool"], brief["schema"]
    return [f"**CTA plan.** One every {c['cadence']['min']}–{c['cadence']['max']} words, to {md(c['destination'])}; "
            f"anchors: {', '.join(md(a) for a in c['anchors'])}; the site-wide CTA band is "
            f"{'hidden on this page' if c['global_cta'] == 'hidden' else 'shown'}.",
            f"**Tool.** {md(tool['pick'])} — evidence: {md(tool['evidence'])}"
            + (f" Trade-off: {md(tool['trade_off'])}" if tool["trade_off"].strip() else ""),
            f"**Schema plan.** offer model {md(sch['offer_model'])}; types: {', '.join(md(t) for t in sch['types'])}."]
```

- [ ] **Step 6: Run the new tests and the existing release tests**

Run: `python3 -m pytest tests/test_page_board.py -q -k "schema_plan or json_ld or release"`
Expected: every selected test passes.

- [ ] **Step 7 (controller): Stamp both records** — `brief.schema`, from **Retrofit → schema**. Re-run the load command → `ok`.

- [ ] **Step 8: Full suite and commit**

Run: `python3 -m pytest tests/test_page_board.py -q` → `170 passed`

```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): the schema plan (§8, §16d) — offer model tied to types, release gate reads the built JSON-LD

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 24 (controller): Regenerate, gate, republish

**Files:** `docs/artifacts/boards/*.html` (generated), `sessions/2026-09-12-page-board-system-build-session-brief.md`, `docs/artifacts/cags-board-brief-gap-analysis.{md,html}`.

- [ ] **Step 1: Regenerate both boards**

```bash
python3 scripts/build_page_board.py african-grey-parrots-for-sale
python3 scripts/build_page_board.py african-grey-parrots-for-sale-near-me
grep -c 'data-title="3b. Image plan"' docs/artifacts/boards/african-grey-parrots-for-sale.html
```
Expected: `wrote docs/artifacts/boards/<slug>.html — 9 sections, …, 100 live pages checked` twice, then `1`.

- [ ] **Step 2: Gate both records at build and at release, and read every new row on the built page before acting on it** (cag-gate-integrity)

```bash
python3 scripts/board_gate.py african-grey-parrots-for-sale
python3 scripts/board_gate.py african-grey-parrots-for-sale-near-me
python3 scripts/board_gate.py african-grey-parrots-for-sale --release
python3 scripts/board_gate.py african-grey-parrots-for-sale-near-me --release
```
Expected at build:
- `FAIL approval-hash` on both, by design until the sitting.
- `WARN image-coverage section next` on the hub only: its nav section plans no image, measured 2026-09-13. This is the one known new row.
- Any `cta-*` WARN: confirm by counting that section's `#reserve` links in `dist/` before believing it.

Expected at release: no `schema-*` row on either page. A `schema-planned-missing` means the stamp named a type the page does not ship. Fix the record, never the page.

- [ ] **Step 3: Republish both boards in place** — Artifact `read` then publish, with `url` `https://claude.ai/code/artifact/adfa7c65-93ce-4388-a5de-45dc48c619b1` (hub) and `https://claude.ai/code/artifact/f260ac31-8167-47af-b9bc-1e7dcb98c83b` (near-me), and no `capabilities` field, so `db` carries forward. First `read_db` collection `boards` on both, to confirm no approval landed since 2026-09-13.

- [ ] **Step 4: Record and commit**

Close items 1–7 in the gap analysis (`.md` + regenerated `.html`) and republish it at `https://claude.ai/code/artifact/8be278cb-2d35-4226-847d-82c0068f30ce`. Add a Tasks 17–24 table to the session brief.

```bash
git add docs/artifacts/boards docs/artifacts/cags-board-brief-gap-analysis.md docs/artifacts/cags-board-brief-gap-analysis.html sessions/2026-09-12-page-board-system-build-session-brief.md
git commit -m "board: hub and near-me boards regenerated with the brief-parity blocks; gap items 1–7 closed

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

## Retrofit: the values stamped into the two records

Every value is read from disk or from a named source document, or it is authored by the controlling session against one. Nothing is guessed by a script, and nothing is written by a subagent.

**group / why (Task 18).**
- **Sources:** hub `sessions/for-sale-research/african-grey-parrots-for-sale/2026-09-12-sprint0-delta.md`; near-me `sessions/for-sale-research/african-grey-parrots-for-sale-near-me/2026-08-10-sprint0.md`; both pages use `docs/research/for-sale-keywords-2026-07.md`.
- **`why_source` format:** the path, plus the heading inside it. For a COMPETITOR-BASED section, the competitor URL the research names.
- **Forced by validation:** category C → SUGGESTED-RECOMMENDED. That is hub `next` and `reserve`, and near-me `search`, `grid` and `cheap`.
- **Hub `reserve`** is a form section recorded as C. If "ours alone" does not describe it, correct its `category` in the same stamp rather than writing a why that argues for a label that doesn't fit. This is a pre-sitting record edit, and the sitting approves it.

**keywords (Task 19).**
- **Source:** each phrase comes from the same research docs, and is kept only if it appears in that section of the built page. Confirm with `grep -io "<phrase>" dist/<slug>/index.html`.
- **Types:** `conversational` = the 6+-word question forms; `comparison` = Congo vs Timneh, grey vs other species; `solution` = scam-free, health guarantee, documented; `transactional` = reserve, deposit, available now.
- An empty array is correct where a section carries none. Arrays are ceilings, not floors (evidence pass, 2026-09-09).

**tuple (Task 20).** Measured on `dist/` 2026-09-13:
- **Stepper:** no element class containing `step` on either page, so `stepper: ""` on both.
- **Hub newsletter:** no `fs-nl` element, so `{"after": "", "variant": ""}`.
- **Near-me newsletter:** one `<aside class="fs-nl">`, directly after section `arrival` and before the FAQ (`src/pages/african-grey-parrots-for-sale-near-me/index.astro` line 702), so `after: "arrival"`. For `variant`, the controller compares that aside's markup with the kit §11 variants A/B/C (`FOR-SALE-PAGES:components-NAMES.md` line 997 and `component-designs/`) and records the match.

**CTA (Task 21).**
- **`global_cta`:** `hidden` on both. Both pages pass `hideGlobalCta={true}` (hub `index.astro` line 225, near-me line 213).
- **`destination`:** `#reserve`.
- **`cadence`:** `{500, 700}` (brief §16d).
- **Per-section `cta`:** the count of `href="#reserve"` links inside that section of the built page. There are 10 on the hub and 12 on near-me in all, and the per-section counts must add up to those totals:

```bash
python3 - <<'EOF'
import re
for slug in ("african-grey-parrots-for-sale", "african-grey-parrots-for-sale-near-me"):
    h = open(f"dist/{slug}/index.html", encoding="utf-8").read()
    cuts = [(m.start(), m.group(1)) for m in re.finditer(r'<section[^>]*\bid="([^"]+)"', h)]
    for i, (at, sid) in enumerate(cuts):
        end = cuts[i + 1][0] if i + 1 < len(cuts) else len(h)
        n = h[at:end].count('href="#reserve"')
        if n: print(slug, sid, n)
    print(slug, "total", h.count('href="#reserve"'))
EOF
```
  A `#reserve` link outside every `<section>`, such as the hero or a sticky bar, belongs to no section and is left out. Record its count in the commit message so the difference from the total is explained.
- **`anchors`:** the distinct visible texts of those links, read from the same HTML.

**tool (Task 22).**
- **Evidence:** a special element is present only if the built page has one. Check with `grep -c '<input type="range"\|data-calc\|<details class="quiz' dist/<slug>/index.html`. The inquiry form doesn't count.
- **Absence:** where the page has none, the evidence is the Sprint 0 SERP snapshot's tool column for the head term, cited by path. `pick: "none"` is correct when neither the page nor the top 10 ships one.
- Do not record a tool the page does not render.

**schema (Task 23).**
- **`types`:** the page's own JSON-LD types, minus the layout's. Run `dist_schema_types` on the page and on `contact-us`, and subtract the second set from the first:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); import pageboard as PB; site=PB.dist_schema_types('contact-us')[0]; [print(s, sorted(PB.dist_schema_types(s)[0]-site)) for s in ('african-grey-parrots-for-sale','african-grey-parrots-for-sale-near-me')]"
```
- **Measured 2026-09-13:** both pages carry `AggregateOffer, Answer, BreadcrumbList, DefinedRegion, FAQPage, ItemList, ListItem, LocalBusiness, MonetaryAmount, Offer, OfferShippingDetails, Organization, Product, Question, WebPage`, and all JSON-LD blocks parse.
- **`offer_model`:** `aggregate-offer` on both.

**The consequence.** Every stamp moves `record_hash`. Neither record holds a current approval (hub's was stale after Tasks 12–16; near-me has never been approved), so nothing is lost. The sitting after Task 24 approves the complete record once.

---

## Self-review against the gap analysis

- **Coverage:** gap items 1–7 map to Tasks 17–23, one commit each; Task 24 regenerates, gates and republishes.
  - 1 → T17: image plan block, `image-coverage` WARN, `asset-alt-duplicate` FAIL.
  - 2 → T18: `group`, `why`, `why_source`; C tied to SUGGESTED-RECOMMENDED; COMPETITOR-BASED needs a URL.
  - 3 → T19: four keyword arrays, one `KEYWORD_TYPES` tuple.
  - 4 → T20: `stepper` and `newsletter` fields; kit strip shows all nine axes.
  - 5 → T21: `brief.cta`, per-section counts, `cta-cadence` and `cta-gap` WARNs.
  - 6 → T22: `brief.tool` with evidence and a trade-off.
  - 7 → T23: `brief.schema`, the offer-model tie, three release rows.
  - Items 8–14 stay deferred, as approved.
- **Placeholders:** none. Every retrofit value names its source file, line or measuring command. The two judgments left to the controller are stated as judgments with their source: near-me's newsletter variant, and whether hub `reserve` is really category C.
- **Type consistency:** new names, used identically in every task:
  - `image_gaps(board) -> [str]`
  - `duplicate_alts(board) -> {str: [str]}`
  - `cta_findings(board) -> [(str, str)]`
  - `dist_schema_types(slug, dist=None) -> (set, int) | None`
  - `KEYWORD_TYPES`, `KEYWORD_LABELS`, `GROUP_SHORT`
  - `image_plan_table(board) -> str`, `decisions_lines(brief) -> [str]` (final form in Task 23)
  - `_kit_card(axis, v, owned, thumbs) -> str`

  Unchanged signatures: `gate_findings(board, ont, ledger, live, stage)`, `render(board, ont, ledger, live, thumbs, slug)`, `kit_cards(board, ledger, thumbs, slug)`, `distribution(board)`.
- **Test counts:** 155 → 157 (T17) → 159 (T18) → 160 (T19: one new, one amended) → 162 (T20) → 165 (T21) → 167 (T22) → 170 (T23). `test_gate_passes_an_approved_minimal_board` stays green throughout. MIN_BOARD's single alt is empty, its section plans an image, and its one CTA covers ~500 words. The new schema rows are release-only.
- **Known edges, recorded:**
  - `stepper` and `newsletter` stay out of the ledger and `TUPLE_ID_KEYS` until a population exists to compare.
  - The `cta-*` rows read band midpoints, so they are WARNs by design.
  - `schema-examined-zero` fails an unbuilt page at release, which is the intended release behaviour: a plan checked against nothing is not a pass.

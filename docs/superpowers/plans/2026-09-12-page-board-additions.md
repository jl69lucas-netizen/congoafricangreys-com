# Page Board System — Breeder Additions (Tasks 12–16)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this amendment task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **Breeder mandate carried from the for-sale program: page PROSE — and every meta variant, angle, FAQ question and anchor written into a record — is authored by the controlling session, never by a subagent; harness code and schema files may be delegated.**

**Goal:** Five additions the breeder approved on 2026-09-12, after sitting at the first board: the title/description set beside the H1, the angles considered and dropped, the FAQ questions enumerated before the build, the links plan the hub build shipped without, and a view-only kit strip so the page's chrome is visible in the same sitting as its sections.

**Architecture:** unchanged. `scripts/pageboard.py` grows four validations and six gate findings; `scripts/build_page_board.py` grows one block (`5b. The kit`), renames one (`2. H1 and meta`) and extends two (`1. Brief`, `3. Outline`); `scripts/board_approve.py` applies one new pick pair. No new script, no new file format, no change to `board_canvas.py` or `board_thumbs.mjs`.

**Tech Stack:** Python 3 + `jsonschema` + pytest · `docs/reference/external-link-library.md` (maintained by `cag-external-link-agent`) · `data/quality/evidence-budgets.json` for the title ceiling.
**Spec:** `docs/superpowers/specs/2026-09-12-page-board-system-design.md`.
**Parent plan:** `docs/superpowers/plans/2026-09-12-page-board-system.md` (Tasks 1–11, shipped 2026-09-12). Its conventions hold: run from `/Users/apple/Downloads/CAG`, a PostToolUse hook pushes after every Bash call, so commit only when that task's tests pass.

Each of Tasks 12–15 adds a **required** field, so the two records under `data/pages/` stop validating the moment its schema lands. Each therefore ends by stamping them, and the **Retrofit** section says where every stamped value comes from. Nothing in a stamp is invented: a value not on disk or in a named source document is authored in the retrofit sitting, never guessed by a script.

---

### Task 12: Meta variants beside the H1

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, `scripts/board_approve.py`, both `data/pages/<slug>/board.json`; test `tests/test_page_board.py`.

The H1 has had five variants and a recommendation since Task 1; the title tag — the string that actually decides the click — has had none. Three each, because the breeder reads three and picks, and three titles at 70 characters is the same amount of reading the five H1s already are. The ceilings are the evidence audit's, read from `data/quality/evidence-budgets.json` rather than restated here, so one file moves them.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_page_board.py — add meta_set to MIN_BOARD, above "sections"
    "meta_set": {
        "titles": ["African Grey Parrots for Sale in the USA | Congo & Timneh | C.A.Gs",
                   "African Grey Parrots for Sale — Named, Priced, Documented | C.A.Gs",
                   "Buy an African Grey Parrot From the Aviary That Raised It | C.A.Gs"],
        "descriptions": ["d" * 150, "e" * 140, "f" * 160],
        "recommended": {"title": 0, "description": 0},
        "pick": {"title": None, "description": None},
    },


def test_meta_set_rejects_a_long_title_a_description_off_band_and_a_fourth_variant():
    for field, i, value in (("titles", 1, "A" * 71), ("descriptions", 0, "d" * 139),
                            ("descriptions", 0, "d" * 161), ("titles", 3, "A fourth title")):
        bad = json.loads(json.dumps(MIN_BOARD))
        bad["meta_set"][field][i:i + 1] = [value]
        with pytest.raises(PB.BoardError):
            PB.validate_board(bad)


def test_meta_pick_falls_back_to_the_recommendation_and_hash_bare_resets_it():
    b = json.loads(json.dumps(MIN_BOARD))
    before = PB.record_hash_bare(b)
    assert PB.meta_pick(b) == (b["meta_set"]["titles"][0], b["meta_set"]["descriptions"][0])
    b["meta_set"]["pick"] = {"title": 2, "description": 1}
    assert PB.meta_pick(b) == (b["meta_set"]["titles"][2], b["meta_set"]["descriptions"][1])
    assert PB.record_hash(b) != before and PB.record_hash_bare(b) == before


def test_gate_meta_no_pick_warns_at_build_and_fails_at_release():
    b = _approved(MIN_BOARD)
    found = lambda stage: [x for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage=stage)
                           if x["check"] == "meta-no-pick"]
    assert [x["sev"] for x in found("build")] == ["WARN", "WARN"]
    assert [x["sev"] for x in found("release")] == ["FAIL", "FAIL"]
    b["meta_set"]["pick"] = {"title": 0, "description": 0}
    b["approval"]["record_hash"] = PB.record_hash(b)
    assert found("release") == []


def test_gate_meta_length_reads_the_per_slug_ceiling(monkeypatch, tmp_path):
    budgets = tmp_path / "evidence-budgets.json"
    budgets.write_text(json.dumps({"title_max_chars": 40, "title_max_chars_by_slug": {"x": 70}}))
    monkeypatch.setattr(PB, "BUDGETS", budgets)
    assert PB.title_ceiling("x") == 70 and PB.title_ceiling("other") == 40
    b = _approved(MIN_BOARD)
    checks = lambda: {x["check"] for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={}, stage="build")}
    assert "meta-length" not in checks()                 # ceiling 70 for slug "x"
    b["meta"]["slug"] = "other"; b["approval"]["record_hash"] = PB.record_hash(b)
    assert "meta-length" in checks()


def test_board_renders_the_meta_radio_groups_beside_the_h1():
    import build_page_board as BPB
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert 'data-title="2. H1 and meta"' in html
    assert 'name="meta-title"' in html and 'name="meta-description"' in html
    assert "meta-title" in html.split("Approve this board")[0]
    assert "meta:{title:" in html                        # Approve sends the pair


def test_approve_applies_the_meta_picks_and_refuses_an_index_off_the_menu():
    import board_approve as BA
    b = json.loads(json.dumps(MIN_BOARD))
    inbox = {"approved_at": "t", "h1": 0, "picks": {"birds": "avail-b"}, "notes": {},
             "meta": {"title": 2, "description": 1}, "canvas_version": None, "record_hash": PB.record_hash(b)}
    out = BA.apply_approval(b, inbox, ONT_OK, LEDGER_EMPTY)
    assert out["board"]["meta_set"]["pick"] == {"title": 2, "description": 1}
    with pytest.raises(PB.BoardError):
        BA.apply_approval(json.loads(json.dumps(MIN_BOARD)), dict(inbox, meta={"title": 9, "description": 0}),
                          ONT_OK, LEDGER_EMPTY)
```

The Task 8 assertion `data-title="2. H1"` becomes `data-title="2. H1 and meta"` in the same edit — the block is renamed, not added.

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k meta`
Expected: `AttributeError: module 'pageboard' has no attribute 'meta_pick'`, plus schema errors on the unknown property `meta_set`.

- [ ] **Step 3: Extend the schema**

```json
// schemas/board.schema.json — "meta_set" joins the top-level required list
  "required": ["meta", "meta_set", "brief", "h1", "sections", "tuple", "assets", "approval"],

// a new property beside "h1"
    "meta_set": {
      "type": "object", "required": ["titles", "descriptions", "recommended", "pick"], "additionalProperties": false,
      "properties": {
        "titles": {"type": "array", "minItems": 3, "maxItems": 3,
                   "items": {"type": "string", "minLength": 1, "maxLength": 70}},
        "descriptions": {"type": "array", "minItems": 3, "maxItems": 3,
                         "items": {"type": "string", "minLength": 140, "maxLength": 160}},
        "recommended": {"type": "object", "required": ["title", "description"], "additionalProperties": false,
          "properties": {"title": {"type": "integer", "minimum": 0, "maximum": 2},
                         "description": {"type": "integer", "minimum": 0, "maximum": 2}}},
        "pick": {"type": "object", "required": ["title", "description"], "additionalProperties": false,
          "properties": {"title": {"type": ["integer", "null"], "maximum": 2},
                         "description": {"type": ["integer", "null"], "maximum": 2}}}
      }
    },

// inside "approval".properties — NOT in its required list
        "meta": {"type": "object", "required": ["title", "description"], "additionalProperties": false,
                 "properties": {"title": {"type": "integer", "minimum": 0, "maximum": 2},
                                "description": {"type": "integer", "minimum": 0, "maximum": 2}}},
```

`approval.meta` is optional on purpose: the two approvals already on disk predate it, and requiring it would invalidate them before the retrofit sitting can replace them. `meta-no-pick` at release is what actually forces the choice, and it reads the record, not the approval.

`maxLength: 70` is the sitewide `title_max_chars`. One slug overrides it — `index`, at 205, by the breeder's 2026-09-10 ruling — and the homepage is not boarded. When it is, raise this `maxLength` to the sitewide ceiling of 205 and let `meta-length` keep applying the per-slug number. Recorded here so that is a decision, not a surprise at validate time.

- [ ] **Step 4: Read the ceiling, pick the pair, gate both**

```python
# scripts/pageboard.py — beside ONTOLOGY / LEDGER
BUDGETS = ROOT / "data" / "quality" / "evidence-budgets.json"
DESC_MIN, DESC_MAX = 140, 160
DEFAULT_TITLE_MAX = 70


def title_ceiling(slug):
    """The evidence audit's sitewide `title_max_chars`, unless `title_max_chars_by_slug`
    raises it for this page. Read from the budgets file so the number moves in one place;
    falls back rather than raising, because a missing budgets file must not be the reason a
    board cannot be gated."""
    try:
        b = _read_json(BUDGETS)
    except (BoardError, OSError):
        return DEFAULT_TITLE_MAX
    return int(b.get("title_max_chars_by_slug", {}).get(slug, b.get("title_max_chars", DEFAULT_TITLE_MAX)))


def meta_pick(board):
    """(title, description) the page will actually render: the breeder's picks, else the
    recommendations — the same fallback picked_h1() uses, so the board, the gate and the
    build all read one pair of strings."""
    ms = board["meta_set"]
    ti = ms["recommended"]["title"] if ms["pick"]["title"] is None else ms["pick"]["title"]
    di = ms["recommended"]["description"] if ms["pick"]["description"] is None else ms["pick"]["description"]
    return ms["titles"][ti], ms["descriptions"][di]


# --- inside record_hash_bare(), beside the h1 reset ---
    ms = b.get("meta_set")
    if isinstance(ms, dict) and isinstance(ms.get("pick"), dict):
        ms["pick"] = {"title": None, "description": None}


# --- inside gate_findings(), after the heading block ---
    ms = board["meta_set"]
    # A recommendation is a draft, not a choice. At build the page can be written against
    # it; by release an unanswered meta set is a page shipping someone's guess.
    sev = "FAIL" if stage == "release" else "WARN"
    for field in ("title", "description"):
        if ms["pick"][field] is None:
            add("meta-no-pick", sev, f"meta {field} has no pick — the recommendation is a draft, not a choice")
    cap = title_ceiling(slug)
    for i, t in enumerate(ms["titles"]):
        if len(t) > cap:
            add("meta-length", "FAIL", f"title variant {i} is {len(t)} chars — ceiling is {cap} "
                                       "(data/quality/evidence-budgets.json)")
    for i, d in enumerate(ms["descriptions"]):
        if not DESC_MIN <= len(d) <= DESC_MAX:
            add("meta-length", "FAIL", f"description variant {i} is {len(d)} chars — band is {DESC_MIN}–{DESC_MAX}")
```

Every variant is measured, not only the picked one: a board offering a choice the gate would refuse is offering a trap.

- [ ] **Step 5: Render the block, send the picks, apply them**

```python
# scripts/build_page_board.py — new helper above render()
def radio_list(name, items, recommended, picked):
    """One radio group, one line per variant, the recommendation starred, every variant
    carrying its own length. The label keeps the click target on the text: three
    70-character titles are an unreasonable click target as bare radios."""
    return "\n".join(
        f'{"⭐ " if i == recommended else ""}<label><input type="radio" name="{esc(name)}" value="{i}"'
        f'{" checked" if i == picked else ""}> {esc(v)} <span class="why">({len(v)} chars)</span></label>  '
        for i, v in enumerate(items))


# --- inside render(), replacing the "2. H1" block ---
    h1, ms = board["h1"], board["meta_set"]
    picked = h1["pick"] if h1["pick"] is not None else h1["recommended"]
    mt = ms["pick"]["title"] if ms["pick"]["title"] is not None else ms["recommended"]["title"]
    mdn = ms["pick"]["description"] if ms["pick"]["description"] is not None else ms["recommended"]["description"]
    parts.append(("2. H1 and meta", "\n".join([
        "**H1** — the page's own promise", "",
        radio_list("h1", h1["variants"], h1["recommended"], picked), "",
        f"**Title tag** — ceiling {PB.title_ceiling(slug)} characters", "",
        radio_list("meta-title", ms["titles"], ms["recommended"]["title"], mt), "",
        f"**Meta description** — band {PB.DESC_MIN}–{PB.DESC_MAX} characters", "",
        radio_list("meta-description", ms["descriptions"], ms["recommended"]["description"], mdn),
    ])))
```
```javascript
// scripts/build_page_board.py — Approve click handler: after the H1 check, and the record it writes
      var mt=document.querySelector('input[name="meta-title"]:checked'),
          mdsc=document.querySelector('input[name="meta-description"]:checked');
      if(!mt||!mdsc){st.textContent='Pick a title and a description before approving.';btn.disabled=false;return;}
      var rec={approved_at:new Date().toISOString(),h1:parseInt(h1.value,10),
               meta:{title:parseInt(mt.value,10),description:parseInt(mdsc.value,10)},
               picks:picks,notes:notes,canvas_version:null,record_hash:RECORD_HASH};
```
```python
# scripts/board_approve.py — inside apply_approval(), after the h1 line
    meta = inbox.get("meta")
    if meta is not None:
        # Range-checked here as well as in the schema: a database document written by hand
        # reaches this function without passing through the button that made it.
        for field in ("title", "description"):
            i, variants = meta.get(field), b["meta_set"][field + "s"]
            if not isinstance(i, int) or isinstance(i, bool) or not 0 <= i < len(variants):
                raise PB.BoardError(f"approval meta.{field}={i!r} is not one of the three {field} variants")
            b["meta_set"]["pick"][field] = i
```

- [ ] **Step 6: Stamp the two records on disk**

Add `meta_set` to both `board.json` files by the **Retrofit** recipe. Near-me's live title (63 chars) and description (153) both sit inside the bounds and become its variant 0; the hub's live title is exactly 70 and becomes its variant 0, but its live description is **182 characters**, outside the band, so all three hub descriptions are written fresh and this retrofit is also the fix for the live one.

Run: `python3 -c "import sys; sys.path.insert(0,'scripts'); import pageboard as PB; [PB.load_board(s) for s in ('african-grey-parrots-for-sale','african-grey-parrots-for-sale-near-me')]"`
Expected: no output — both records load, so every title is ≤ 70 and every description sits in the band.

- [ ] **Step 7: Run the tests and commit**

Run: `python3 -m pytest tests/test_page_board.py -q -k meta` → `6 passed`.
```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py scripts/board_approve.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): three title and description variants beside the H1, picked on the board

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 13: Angles considered

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both `data/pages/<slug>/board.json`; test `tests/test_page_board.py`.

`brief.strategy` has always recorded the angle that was taken and never the ones that were not, so the board could not show that a choice was made at all. Two to three entries: one is not a choice, four is a workshop. `strategy.name` must be one of them, which is what stops the table becoming decoration that drifts from the strategy beside it.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_page_board.py — add to MIN_BOARD["brief"]
              "angles": [{"name": "n", "hook": "the birds first, the pitch second", "why_not": ""},
                         {"name": "price-led", "hook": "open on the $1,500 floor",
                          "why_not": "the price bucket is the adoption-cost page's, and it outranks us on it"}],


def test_angles_reject_one_entry_four_entries_a_duplicate_name_and_a_long_field():
    one = json.loads(json.dumps(MIN_BOARD)); one["brief"]["angles"] = one["brief"]["angles"][:1]
    four = json.loads(json.dumps(MIN_BOARD)); four["brief"]["angles"] += [
        {"name": "a", "hook": "h", "why_not": "w"}, {"name": "b", "hook": "h", "why_not": "w"}]
    dupe = json.loads(json.dumps(MIN_BOARD)); dupe["brief"]["angles"][1]["name"] = "n"
    long = json.loads(json.dumps(MIN_BOARD)); long["brief"]["angles"][1]["hook"] = "x" * 241
    for bad in (one, four, dupe, long):
        with pytest.raises(PB.BoardError):
            PB.validate_board(bad)


def test_angles_tie_to_the_strategy_and_a_rejected_one_must_say_why_not():
    off = json.loads(json.dumps(MIN_BOARD)); off["brief"]["strategy"]["name"] = "an angle nobody listed"
    with pytest.raises(PB.BoardError, match="not one of the angles"):
        PB.validate_board(off)
    silent = json.loads(json.dumps(MIN_BOARD)); silent["brief"]["angles"][1]["why_not"] = "   "
    with pytest.raises(PB.BoardError, match="records no why_not"):
        PB.validate_board(silent)
    PB.validate_board(MIN_BOARD)                  # the chosen angle's empty why_not is fine


def test_board_renders_the_angles_table_with_the_chosen_one_starred():
    import build_page_board as BPB
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert "Angles considered" in html and "⭐ n" in html and "price-led" in html
    assert "trade-off: t" in html                 # the chosen row carries the strategy's trade-off
    assert "adoption-cost page" in html           # the rejected row carries its why_not
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k angle`
Expected: `3 failed` — the schema rejects the unknown property `angles`.

- [ ] **Step 3: Extend the schema**

```json
// schemas/board.schema.json — inside "brief"
      "required": ["goal", "scope", "gates", "done", "out_of_scope", "primary_keyword", "angles", "strategy"],

// and inside "brief".properties
        "angles": {
          "type": "array", "minItems": 2, "maxItems": 3,
          "items": {"type": "object", "required": ["name", "hook", "why_not"], "additionalProperties": false,
                    "properties": {"name": {"type": "string", "minLength": 1, "maxLength": 240},
                                   "hook": {"type": "string", "minLength": 1, "maxLength": 240},
                                   "why_not": {"type": "string", "maxLength": 240}}}
        },
```

- [ ] **Step 4: Tie the strategy to the angles**

```python
# scripts/pageboard.py — inside validate_board(), after the section id/n duplicate check
    brief = board["brief"]
    names = [a["name"] for a in brief["angles"]]
    dupes = sorted({n for n in names if names.count(n) > 1})
    if dupes:
        raise BoardError(f"duplicate angle name: {', '.join(dupes)}")
    chosen = brief["strategy"]["name"]
    if chosen not in names:
        # The two fields are one decision written twice. Left free to disagree, the table
        # becomes decoration: still rendered, still read as considered, still describing a
        # page nobody is building.
        raise BoardError(f"brief.strategy.name {chosen!r} is not one of the angles considered "
                         f"({', '.join(names)})")
    for a in brief["angles"]:
        if a["name"] != chosen and not a["why_not"].strip():
            raise BoardError(f"angle {a['name']!r} was not taken and records no why_not")
```

`why_not` is a required key and may be empty for exactly one angle — the chosen one, which was not rejected and has a trade-off instead. Every other angle has to say what it cost, or the record claims a comparison that never happened.

- [ ] **Step 5: Render the table in block 1**

```python
# scripts/build_page_board.py — new helper above render()
def angles_table(brief):
    """Angles considered, the chosen one starred. Its third column is the strategy's own
    trade-off rather than a why_not: a table where only the rejects carry a cost reads as
    one good idea and two bad ones, which is not what the sitting is for."""
    rows = []
    for a in brief["angles"]:
        taken = a["name"] == brief["strategy"]["name"]
        rows.append([("⭐ " if taken else "") + md(a["name"]), md(a["hook"]),
                     ("**taken** — trade-off: " + md(brief["strategy"]["trade_off"])) if taken
                     else md(a["why_not"])])
    return md_table(["Angle", "Hook", "Why not / trade-off"], rows)


# --- inside render(), replacing the single strategy line of block 1 ---
        f"**Strategy: {md(brief['strategy']['name'])}.** Why: {md(brief['strategy']['why'])}",
        "", "**Angles considered**", angles_table(brief),
```

- [ ] **Step 6: Stamp the two records on disk**

Both briefs already name their taken angle in `strategy.name` — `Breeder's National Inventory, Documented` for the hub, `B-3 Router With a Reason` for near-me — so the chosen entry is that name verbatim with an empty `why_not`. The rejected angles are on record in `docs/superpowers/plans/2026-08-10-buy-shipping-and-near-me-for-sale-pages.md` §0f–§0g, where the retired pair and the geographic split were argued. Lift one or two; do not invent a third.

- [ ] **Step 7: Run the tests and commit**

Run: `python3 -m pytest tests/test_page_board.py -q -k angle` → `3 passed`.
```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): the angles considered, the chosen one tied to brief.strategy

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 14: FAQ questions enumerated

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both `data/pages/<slug>/board.json`; test `tests/test_page_board.py`.

The FAQ is a `standard` section, so the board showed it as one line and the build invented its questions afterwards — the one part of the page that is pure buyer language, decided after the sitting was over. Eight to fourteen: below eight the block is not an FAQ, above fourteen nobody reads to the end and the `FAQPage` schema starts to look spun.

- [ ] **Step 1: Write the failing tests**

```python
def _with_faq(questions):
    b = json.loads(json.dumps(MIN_BOARD))
    faq = json.loads(json.dumps(b["sections"][0]))
    faq.update({"id": "faq", "n": 2, "heading": "Questions Buyers Ask Us Before They Reserve",
                "shape": "standard", "tree": [], "images": [], "questions": questions,
                "options": {"candidates": [], "excluded": [], "pick": None, "note": ""}})
    b["sections"].append(faq)
    return b


EIGHT = [f"Question number {n} about buying an African Grey?" for n in range(1, 9)]


def test_faq_questions_reject_seven_fifteen_a_duplicate_a_flat_line_and_an_absent_list():
    fifteen = [f"Question number {n} about buying an African Grey?" for n in range(1, 16)]
    for bad in (EIGHT[:7], fifteen, EIGHT[:7] + [EIGHT[0]], EIGHT[:7] + ["A statement, not a question."]):
        with pytest.raises(PB.BoardError):
            PB.validate_board(_with_faq(bad))
    PB.validate_board(_with_faq(EIGHT))
    PB.validate_board(MIN_BOARD)                      # no faq section, nothing to enumerate
    bare = _with_faq(EIGHT); del bare["sections"][1]["questions"]
    with pytest.raises(PB.BoardError):
        PB.validate_board(bare)


def test_faq_questions_are_not_headings_but_are_listed_in_the_outline():
    import build_page_board as BPB
    b = _with_faq(EIGHT)
    assert EIGHT[0] not in [t for _, t in PB.all_headings(b)]
    assert PB.faq_questions(b) == EIGHT
    html = BPB.render(_approved(b), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert "Q01 " + BPB.esc(EIGHT[0]) in html and "Q08 " in html


def test_gate_calls_a_colliding_faq_question_a_warn_not_a_fail():
    b = _approved(_with_faq(EIGHT))
    f = PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live={"/congo-african-grey-for-sale/": [EIGHT[0]]}, stage="build")
    hits = [x for x in f if x["check"] == "faq-collision"]
    assert len(hits) == 1 and hits[0]["sev"] == "WARN"
    assert not [x for x in f if x["check"] == "header-collision"]


def test_approve_leaves_the_faq_questions_alone():
    import board_approve as BA
    b = _with_faq(EIGHT)
    inbox = {"approved_at": "t", "h1": 0, "picks": {"birds": "avail-b"}, "notes": {},
             "meta": {"title": 0, "description": 0}, "canvas_version": None, "record_hash": PB.record_hash(b)}
    out = BA.apply_approval(b, inbox, ONT_OK, LEDGER_EMPTY)
    assert out["board"]["sections"][1]["questions"] == EIGHT
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k question`
Expected: `4 failed` — the schema rejects the unknown property `questions`.

- [ ] **Step 3: Extend the schema**

```json
// schemas/board.schema.json — inside sections.items.properties
          "questions": {"type": "array", "minItems": 8, "maxItems": 14, "uniqueItems": true,
                        "items": {"type": "string", "minLength": 8, "pattern": "\\?$"}},

// and inside sections.items, beside "properties"
        "allOf": [{
          "if": {"required": ["id", "shape"],
                 "properties": {"id": {"const": "faq"}, "shape": {"const": "standard"}}},
          "then": {"required": ["questions"]}
        }],
```

Required only on the one section that is an FAQ, by id **and** shape together: a `proof` section whose id happens to be `faq` is not an FAQ, and a `standard` section named `reserve` has nothing to enumerate.

- [ ] **Step 4: Read them and pre-check them**

```python
# scripts/pageboard.py — beside all_headings()
def faq_questions(board):
    """The enumerated FAQ questions, or [] when the record has no FAQ section. Deliberately
    NOT in all_headings(): a question renders inside a <summary>, and counting it as a
    heading would inflate h_counts and let a page clear the H5/H6 floor on its FAQ alone."""
    for s in board["sections"]:
        if s["id"] == "faq" and s["shape"] == "standard":
            return list(s.get("questions", []))
    return []


def faq_hits(board, live):
    """FAQ questions that collide with a live heading. Same three kinds and whitelist as
    header_hits(), minus the head-term exemption: a question is a whole sentence, not a
    keyword-bearing heading, so a shared five-token run is worth a look every time."""
    return [h for h in header_precheck(faq_questions(board), live, exclude_page=own_live_key(board))
            if not _whitelisted(h["heading"])]


# --- inside gate_findings(), after the header-collision loop ---
    # WARN, never FAIL. Two pages may legitimately answer the same buyer question, and the
    # dup gate judges the ANSWER after the build; a repeated question is a sign to look.
    for h in faq_hits(board, live):
        add("faq-collision", "WARN", f"{h['kind']}: FAQ question {h['heading']!r} vs {h['page']} {h['with']!r}")
```

- [ ] **Step 5: List them under the FAQ heading**

```python
# scripts/build_page_board.py — inside outline_block(), after walk(s["tree"], 1)
        for i, q in enumerate(s.get("questions", []), 1):
            lines.append(f"│   ├─ Q{i:02d} {esc(q)}" + flag(q, hit_by))


# --- inside render(), where hits is computed and where block 3 is built ---
    hits = PB.header_hits(board, live)          # exactly what the gate will fail on
    qhits = PB.faq_hits(board, live)            # and what it will warn on

    parts.append(("3. Outline", f"<pre class=\"tree\">{outline_block(board, hits + qhits)}</pre>\n\n"
                  + (f"**{len(hits)} heading(s) collide with a live page.** Rewrite them before approving; "
                     "the gate fails on any." if hits else
                     "No heading collides with a live page (exact, species-template or 5-word shingle).")
                  + (f"\n\n{len(qhits)} FAQ question(s) repeat a live heading — a warning, not a refusal."
                     if qhits else "")))
```

- [ ] **Step 6: Stamp the two records on disk**

Both pages already ship an FAQ: the strings are the `faqs` array in `src/pages/african-grey-parrots-for-sale/index.astro` (line 163) and `src/pages/african-grey-parrots-for-sale-near-me/index.astro` (line 149). Copy the questions verbatim — they are what the live `FAQPage` schema already asserts, so an edit here is a content change to a live page and belongs in its own build, not in a retrofit.

- [ ] **Step 7: Run the tests and commit**

Run: `python3 -m pytest tests/test_page_board.py -q -k question` → `4 passed`.
```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): FAQ questions enumerated on the board, pre-checked as a warning

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 15: The links plan

**Files:** modify `schemas/board.schema.json`, `scripts/pageboard.py`, `scripts/build_page_board.py`, both `data/pages/<slug>/board.json`; test `tests/test_page_board.py`.

This is the one the hub build missed. The record said nothing about links, so the internal linking and the external citations were decided inline during the build — after the sitting that was supposed to decide them, which is how a hub shipped with a links plan nobody approved. Every section now records what it links to, with its anchor, and `sentence_start` states the Link-First rule per anchor.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_page_board.py — add to MIN_BOARD["sections"][0]
        "links": {"internal": [{"href": "/congo-african-grey-for-sale/", "anchor": "Our Congo listings",
                                "sentence_start": True}],
                  "external": [{"href": "https://www.aphis.usda.gov/awa/public-search",
                                "anchor": "USDA APHIS license search tool",
                                "library_row": "Authority — Government / Legal"}]},


def test_links_reject_a_relative_href_an_empty_anchor_and_a_url_outside_the_library():
    rel = json.loads(json.dumps(MIN_BOARD))
    rel["sections"][0]["links"]["internal"][0]["href"] = "congo-african-grey-for-sale/"
    blank = json.loads(json.dumps(MIN_BOARD))
    blank["sections"][0]["links"]["external"][0]["anchor"] = ""
    for bad in (rel, blank):
        with pytest.raises(PB.BoardError):
            PB.validate_board(bad)
    off = json.loads(json.dumps(MIN_BOARD))
    off["sections"][0]["links"]["external"][0]["href"] = "https://example.com/parrots"
    with pytest.raises(PB.BoardError, match="external-link-library"):
        PB.validate_board(off)
    lib = PB.library_urls()                       # `www.` and a trailing slash are normalised away
    assert PB.normalise_url("https://cites.org/eng/app/appendices.php") in lib
    assert PB.normalise_url("https://parrots.org/encyclopedia/grey-parrot") in lib
    assert PB.normalise_url("https://example.com/nope") not in lib


def test_gate_fails_on_a_duplicate_anchor_and_on_an_internal_href_with_no_built_page():
    b = _approved(MIN_BOARD)
    live = {"/x/": [], "/congo-african-grey-for-sale/": []}
    hits = lambda check: [x for x in PB.gate_findings(b, ONT_OK, LEDGER_EMPTY, live=live, stage="build")
                          if x["check"] == check]
    assert hits("links-internal-dead") == [] and hits("links-anchor-duplicate") == []
    b["sections"][0]["links"]["internal"].append(
        {"href": "/a-page-that-was-never-built/#papers", "anchor": "our congo listings", "sentence_start": True})
    b["approval"]["record_hash"] = PB.record_hash(b)
    for check in ("links-anchor-duplicate", "links-internal-dead"):
        assert len(hits(check)) == 1 and hits(check)[0]["sev"] == "FAIL"


def test_gate_links_external_missing_warns_at_build_and_fails_at_release_on_the_hub(live_dist):
    b = PB.load_board("african-grey-parrots-for-sale")          # the hub record as it stands
    for s in b["sections"]:
        s.setdefault("links", {"internal": [], "external": []})
    b["approval"]["record_hash"] = PB.record_hash(b)
    found = lambda stage: [x for x in PB.gate_findings(b, PB.load_ontology(), PB.load_ledger(),
                                                       live_dist, stage=stage)
                           if x["check"] == "links-external-missing"]
    assert [x["sev"] for x in found("build")] == ["WARN"]
    assert [x["sev"] for x in found("release")] == ["FAIL"]
    assert "0 external library link" in found("release")[0]["msg"]
```

The last test is the amendment's proof: the hub record as approved on 2026-09-12 records zero external links, and the release gate refuses it until the retrofit records the three its live page already carries.

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k links`
Expected: `3 failed` — the schema rejects the unknown property `links`, and `PB.library_urls` does not exist.

- [ ] **Step 3: Extend the schema**

```json
// schemas/board.schema.json — sections.items.required gains "links", after "images"
        "required": ["id", "n", "heading", "intent", "category", "framework", "words", "shape",
                     "keywords", "entities", "tree", "images", "links", "options"],

// and inside sections.items.properties
          "links": {
            "type": "object", "required": ["internal", "external"], "additionalProperties": false,
            "properties": {
              "internal": {"type": "array", "items": {
                "type": "object", "required": ["href", "anchor", "sentence_start"], "additionalProperties": false,
                "properties": {"href": {"type": "string", "pattern": "^/"},
                               "anchor": {"type": "string", "minLength": 1},
                               "sentence_start": {"const": true}}}},
              "external": {"type": "array", "items": {
                "type": "object", "required": ["href", "anchor", "library_row"], "additionalProperties": false,
                "properties": {"href": {"type": "string", "pattern": "^https?://"},
                               "anchor": {"type": "string", "minLength": 1},
                               "library_row": {"type": "string", "minLength": 1}}}}
            }
          },
```

`sentence_start` is `const: true`, so the only thing it can record is compliance with the Link-First rule (`rules/links.md`, breeder 2026-07-11). An anchor that does not open its sentence has nothing to write here: it is rewritten, not recorded.

- [ ] **Step 4: Validate against the library**

```python
# scripts/pageboard.py — beside BUDGETS
EXTERNAL_LIBRARY = ROOT / "docs" / "reference" / "external-link-library.md"
_LIB_URL = re.compile(r"https?://[^\s`|)>\"']+")


def normalise_url(url):
    """One spelling for comparing a recorded href against a library row: scheme and host
    lowercased, a leading `www.` dropped, trailing slash and punctuation trimmed. `www.`
    goes because the library records `https://www.cites.org/eng/app/appendices.php` while
    the live pages link `https://cites.org/...` — one row, and a checker calling them two
    would send an author to add a row that is already there."""
    u = url.strip().rstrip(".,;")
    m = re.match(r"^(https?)://([^/]+)(.*)$", u, re.I)
    if not m:
        return u.lower()
    host = m.group(2).lower()
    host = host[4:] if host.startswith("www.") else host
    return f"{m.group(1).lower()}://{host}{m.group(3).rstrip('/')}"


def library_urls(path=EXTERNAL_LIBRARY):
    """Every URL docs/reference/external-link-library.md records, normalised. Grepped, not
    parsed: the library is three table shapes plus a prose citation block, and all of them
    write the URL plainly. Missing file → empty set, and validate_board then skips the
    membership rule: an absent library is a tooling fault, not a bad record."""
    p = pathlib.Path(path)
    return {normalise_url(u) for u in _LIB_URL.findall(p.read_text(encoding="utf-8"))} if p.exists() else set()


# --- inside validate_board(), after the angles block ---
    lib = library_urls()
    if lib:
        for sec in board["sections"]:
            for l in sec["links"]["external"]:
                if normalise_url(l["href"]) not in lib:
                    raise BoardError(f"section {sec['id']}: external href {l['href']} is not in "
                                     "docs/reference/external-link-library.md — add the row and verify 200 first")
```

Membership raises; **uniqueness does not**. A duplicate anchor is a fixable defect on a record worth saving, and the author needs that record on disk to fix it. An external URL nobody has verified is a claim, and a record carrying one should not exist.

- [ ] **Step 5: Add the three gate findings**

```python
# scripts/pageboard.py — beside ADVISORY_MIN_H5H6
LIBRARY_LINK_MIN = 3
LINK_FLOOR_TYPES = {"for-sale", "hub"}            # the transactional cluster and its hub


# --- inside gate_findings(), after the signature-pick loop ---
    internal, external, anchors = [], [], {}
    for s in board["sections"]:
        internal += [(s["id"], l) for l in s["links"]["internal"]]
        external += [(s["id"], l) for l in s["links"]["external"]]
    # Anchor Diversity is a page-level rule, so the comparison is on tokens: "Our Congo
    # listings" and "our congo listings," are one anchor twice, and a raw string compare
    # would pass them.
    for sid, l in internal + external:
        anchors.setdefault(" ".join(tokens(l["anchor"])), []).append((sid, l["anchor"]))
    for uses in anchors.values():
        if len(uses) > 1:
            add("links-anchor-duplicate", "FAIL",
                f"anchor {uses[0][1]!r} is used {len(uses)} times ({', '.join(s for s, _ in uses)}) "
                "— one anchor, one destination, one place")
    if board["meta"]["page_type"] in LINK_FLOOR_TYPES and len(external) < LIBRARY_LINK_MIN:
        # WARN at build so a page can be written while a library row is still being
        # verified; FAIL at release because a transactional page with no outside citation
        # is the thin-page pattern the cluster was rebuilt to leave behind.
        add("links-external-missing", "FAIL" if stage == "release" else "WARN",
            f"{len(external)} external library link(s) recorded — a {board['meta']['page_type']} page "
            f"carries at least {LIBRARY_LINK_MIN}")
    # Reuses the live map the gate already loaded for the header pre-check. When it is
    # empty the gate has already FAILed on header-precheck-examined-zero, and guessing at
    # dead links from an unbuilt tree would only add noise to that.
    for sid, l in (internal if live else []):
        path = l["href"].split("#", 1)[0].split("?", 1)[0]
        target = path if path.endswith("/") else path + "/"
        if target not in live:
            add("links-internal-dead", "FAIL",
                f"section {sid}: {l['href']} has no built page (dist{target}index.html)")
```

- [ ] **Step 6: Render the links under each section's tree**

```python
# scripts/build_page_board.py — inside outline_block(), after the questions loop
        for l in s["links"]["internal"]:
            lines.append(f"│   → {esc(l['anchor'])} → {esc(l['href'])}")
        for l in s["links"]["external"]:
            lines.append(f"│   ↗ {esc(l['anchor'])} → {esc(l['href'])}   [{esc(l['library_row'])}]")
```

The arrows are the whole legend: `→` goes to another page of ours, `↗` leaves the site. They sit inside the outline rather than in a block of their own because a link is a property of the section carrying it, and a separate block would be read after the breeder had already approved the outline it belongs to.

- [ ] **Step 7: Stamp the two records on disk**

Read the anchors the built pages already carry out of `dist/` (see **Retrofit**); every section gets a `links` key even when both lists are empty.
```bash
npx astro build
python3 scripts/board_gate.py african-grey-parrots-for-sale
python3 scripts/board_gate.py african-grey-parrots-for-sale-near-me
```
Expected: `approval-hash` FAIL on both (the four new fields moved the hash — the retrofit sitting answers it), and **no** `links-internal-dead`, `links-anchor-duplicate` or `meta-length` on either.

- [ ] **Step 8: Run the tests and commit**

Run: `python3 -m pytest tests/test_page_board.py -q -k links` → `3 passed`.
```bash
git add schemas/board.schema.json scripts/pageboard.py scripts/build_page_board.py tests/test_page_board.py data/pages
git commit -m "feat(page-board): the links plan — per-section internal and external anchors, library-checked

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 16: The kit strip

**Files:** modify `scripts/build_page_board.py`; test `tests/test_page_board.py`.

Block 6 offers a component per section; the page-level chrome — hero, dial, rail, TOC, FAQ shell — lives in `tuple` and reached the board only as ids inside ledger findings. A breeder who has just picked nine section components should be able to see the frame they sit in, in the same sitting, without reading JSON. View-only: the tuple is the author's decision against the ledger, not the sitting's.

- [ ] **Step 1: Write the failing tests**

```python
def test_kit_strip_shows_every_axis_the_tuple_names_and_offers_nothing():
    import build_page_board as BPB
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, thumbs={}, slug="x")
    assert 'data-title="5b. The kit"' in html
    for shell in ("hero-a", "dial-1", "rail-a", "t1", "faq-a"):
        assert f'<div class="nothumb">{shell}</div>' in html
    assert 'name="pick-hero"' not in html and 'name="kit-' not in html
    b = _approved(MIN_BOARD)
    b["tuple"]["hero"] = "hero-a#inventory-tiles"
    ledger = {"pools": {"inventory": ["avail-b"]}, "refresh_pools": ["hero"],
              "pages": {"sibling": {"hero": "hero-a", "dial": "", "rail": "", "toc": "", "takeaway": [],
                                    "table": "", "faq": "", "h6_prefixes": []}}}
    html = BPB.render(b, ONT_OK, ledger, live={}, thumbs={}, slug="x")
    assert "refresh: inventory-tiles" in html and "also worn by sibling" in html
    assert "new to the cluster" in html            # the dial nobody else records


def test_kit_strip_takes_the_desktop_thumb_whatever_section_it_was_cut_under():
    import build_page_board as BPB
    thumbs = {("birds", "hero-a"): "thumbs/birds--hero-a--desktop.png"}
    html = BPB.render(_approved(MIN_BOARD), ONT_OK, LEDGER_EMPTY, live={}, thumbs=thumbs, slug="x")
    assert 'src="thumbs/birds--hero-a--desktop.png"' in html
    assert "the hero this page wears" in html
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_page_board.py -q -k kit`
Expected: `2 failed` — `assert 'data-title="5b. The kit"' in html`.

- [ ] **Step 3: Write the block**

```python
# scripts/build_page_board.py — beside option_cards()
KIT_AXES = ("hero", "dial", "rail", "toc", "faq")


def kit_thumb(component_id, thumbs):
    """Any artboard cut for this shell, whatever section it was cut under: board_canvas.py
    cuts chrome beneath whichever section offered it, so a section-scoped lookup would
    leave the strip blank. Exact id first, then the base."""
    base = PB.base_of(component_id)
    for wanted in (component_id, base):
        for (_section, candidate), src in thumbs.items():
            if candidate == wanted:
                return src
    return None


def kit_cards(board, ledger, thumbs, slug):
    """The five chrome shells this page will wear — shown, never offered. Block 6 picks per
    section; this is the page-level tuple the author already chose against the ledger, and
    a radio here would invite a choice the ledger rules decide, not the sitting."""
    t = board["tuple"]
    owned = PB.owned_components(ledger, exclude_slug=slug)
    cards = []
    for axis in KIT_AXES:
        v = (t.get(axis) or "").strip()
        if not v:
            cards.append(f'<div class="opt off"><span class="pill">{esc(axis)}</span>'
                         f'<div class="nothumb">none</div>'
                         f'<span class="why">this page wears no {esc(axis)}</span></div>')
            continue
        base = PB.base_of(v)
        delta = v.split("#", 1)[1].strip() if "#" in v else ""
        th = kit_thumb(v, thumbs)
        img = (f'<img src="{esc(th)}" alt="{esc(base)} — the {esc(axis)} this page wears">'
               if th else f'<div class="nothumb">{esc(base)}</div>')
        owners = owned.get(v) or owned.get(base) or []
        cards.append(
            f'<div class="opt"><span class="pill">{esc(axis)}</span>{img}<b>{esc(base)}</b>'
            + (f'<span class="pill">refresh: {esc(delta)}</span>' if delta else "")
            + f'<span class="why">{"also worn by " + esc(", ".join(owners)) if owners else "new to the cluster"}'
              "</span></div>")
    return cards


# --- inside render(), between block 5 and block 6 ---
    parts.append(("5b. The kit", f'<div class="opts kit">{"".join(kit_cards(board, ledger, thumbs, slug))}</div>'
                  "\n\nThe page-level tuple, for reading. Picks happen in block 6; a shell that is wrong here is "
                  "a record edit, not a radio."))
```
```css
/* scripts/build_page_board.py — appended to CSS */
.kit .opt{gap:5px}
.kit .opt b{font-size:13px;font-weight:600}
.kit .opt .pill:first-child{justify-self:start;background:var(--paper);border-color:var(--line);color:var(--ink-3);text-transform:uppercase;letter-spacing:.06em}
```

- [ ] **Step 4: Run the tests and regenerate both boards**

Run: `python3 -m pytest tests/test_page_board.py -q -k kit` → `2 passed`, then `python3 -m pytest tests/test_page_board.py -q` → `150 passed` (132 before this amendment).
```bash
python3 scripts/build_page_board.py african-grey-parrots-for-sale
python3 scripts/build_page_board.py african-grey-parrots-for-sale-near-me
grep -c "5b. The kit" docs/artifacts/boards/african-grey-parrots-for-sale.html
```
Expected: `wrote docs/artifacts/boards/<slug>.html — …` twice, then `1`.

- [ ] **Step 5: Commit**

```bash
git add scripts/build_page_board.py tests/test_page_board.py docs/artifacts/boards
git commit -m "feat(page-board): 5b. The kit — the page-level tuple shown on the board, view-only

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

## Retrofit: the near-me and hub records

Four required fields land across Tasks 12–15, so both existing records stop validating as each one ships. Every value below is read from disk or from a named source document; anything else is authored in the retrofit sitting, never guessed.

**`meta_set`.** Variant 0 is the live `<title>` and `<meta name="description">` read out of `dist/<slug>/index.html` — what the page already says, the one variant needing no judgment. Variants 1 and 2 are written fresh against the record's own `brief.primary_keyword` and `brief.strategy`. Measured 2026-09-12: near-me's live title is 63 characters and its description 153, so both serve as variant 0; the hub's live title is exactly 70 — at the ceiling, usable — but its live description is **182 characters**, outside the 140–160 band, so the hub gets three fresh descriptions and this retrofit is also the fix for the live one. `recommended` is the variant the session argues for; `pick` stays `null` until the breeder answers, which is what `meta-no-pick` is counting on.

**`angles`.** The chosen entry is `brief.strategy.name` verbatim (`Breeder's National Inventory, Documented`; `B-3 Router With a Reason`) with an empty `why_not`. The rejected entries come from `docs/superpowers/plans/2026-08-10-buy-shipping-and-near-me-for-sale-pages.md` §0f–§0g, where the retired pair and the geographic split were argued and where the hub's grid was handed to the router. Two entries each; a third only if the plan records a third.

**`questions`.** The `faqs` arrays already in the sources: `src/pages/african-grey-parrots-for-sale/index.astro` line 163, `src/pages/african-grey-parrots-for-sale-near-me/index.astro` line 149. Verbatim.

**`links`.** Read from the built pages, not from the sources — `grep -o 'href="[^"]*"' dist/<slug>/index.html` is what actually ships, and the anchor text comes from the `<a>` the href sits in. Measured 2026-09-12, excluding font hosts and self-links: the hub carries six external links, three matching a library row (`aphis.usda.gov/awa/public-search`, `fws.gov/program/cites`, `parrots.org/encyclopedia/grey-parrot/`); near-me carries four, one of which does. Three near-misses have to be settled first, because `validate_board` refuses an external href the library does not carry:

- `https://cites.org/eng/app/appendices.php` vs the library's `https://www.cites.org/...` — one row; `normalise_url` drops the `www.`, so this resolves itself.
- `https://www.iata.org/en/programs/ops-infra/live-animals/` vs the library's `.../cargo/live-animals/` — a genuinely different path. Re-verify the live one and update the row.
- `aav.org` and `iucnredlist.org` have no row at all. Verify 200 and add them with three anchor variants each, or drop them from the record and from the pages.

Internal anchors are recorded `sentence_start: true` only where they actually open their sentence; where a built page has one mid-sentence, that is a Link-First defect this retrofit surfaces, fixed on the page before it is recorded. The hub's live page already clears the `links-external-missing` floor of three; near-me, at one, needs two more before its record can. Both need their internal anchors recorded — the part the hub build skipped entirely.

**The consequence.** Re-stamping moves `record_hash`, so both approvals go stale and `board_gate.py` FAILs `approval-hash` on both until each record is re-boarded and re-approved. That is the correct outcome, not a workaround: the breeder never saw a meta set, an angles table, an FAQ list or a links plan, and an approval that survived their addition would be claiming otherwise. Two sittings, near-me first (smaller record, live meta already in band), then the hub, whose links plan is the one the gate is waiting on and whose next release is blocked until it is recorded.

---

## Self-review against the brief

- **Spec coverage.** Five breeder additions → five tasks, one commit each. T12 `meta_set` (schema, block 2 renamed, Approve JS, `board_approve`, `record_hash_bare`, `meta-no-pick`, `meta-length`). T13 `brief.angles` (schema, `validate_board` tie to `strategy.name`, block 1 table with ⭐ and the trade-off). T14 `sections[].questions` (conditional schema requirement, outline list, `header_precheck` as a WARN, approve untouched). T15 `sections[].links` (schema, library validation, `links-external-missing` / `links-anchor-duplicate` / `links-internal-dead`, outline rendering, the hub-fails-at-release fixture). T16 `5b. The kit` (view-only, thumbs, refresh pill, ledger owners, tests on rendered HTML). Retrofit and this checklist close the amendment.
- **Placeholder scan.** No "TBD" and no invented content. Every retrofit value is read from `dist/`, from a named source line, or authored in the sitting; the three library near-misses are named as open work rather than normalised away in silence. The one measurement that fails a new rule — the hub's 182-character description — is stated as a finding, not smoothed over.
- **Type consistency.** New signatures, used identically everywhere: `title_ceiling(slug) -> int`, `meta_pick(board) -> (str, str)`, `faq_questions(board) -> [str]`, `faq_hits(board, live) -> [hit]`, `normalise_url(url) -> str`, `library_urls(path=EXTERNAL_LIBRARY) -> set`, `radio_list(name, items, recommended, picked) -> str`, `angles_table(brief) -> str`, `kit_thumb(component_id, thumbs) -> str|None`, `kit_cards(board, ledger, thumbs, slug) -> [str]`. Unchanged signatures stay unchanged: `gate_findings(board, ont, ledger, live, stage)`, `render(board, ont, ledger, live, thumbs, slug)`, `apply_approval(board, inbox, ont, ledger, canvas_dir=None)`. Hit dicts keep the `{heading, kind, page, with}` shape `flag()` already reads, which is why FAQ hits pass straight into `outline_block`.
- **Known edge, recorded not deferred.** `titles.maxLength` is the sitewide 70; `index` overrides `title_max_chars` to 205 and would need that raised when the homepage is boarded. `approval.meta` is optional so the two approvals on disk survive until the retrofit sitting replaces them; `meta-no-pick` at release is what actually forces the picks.

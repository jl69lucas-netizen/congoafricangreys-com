# CAG Social Media System Implementation Plan

> **For agentic workers:** This plan builds **markdown agents/skills + JSON config**, not a compiled app. There is no pytest suite — "verification" steps use this project's real tooling: JSON-validity checks (`python3 -c "import json…"`), `grep` assertions, `scripts/verify_model_tiers.sh`, the golden-rule injection scripts, and `@cag-agent-system-qa`. Steps use checkbox (`- [ ]`) syntax for tracking. Use superpowers:executing-plans (inline) — subagent-per-task is overkill for 8 file-creation tasks.

**Goal:** Stand up CAG's social-media capability as ONE orchestrator agent (`cag-social-strategist`) + a corrected per-platform content skill + competitor social-tracking schema, leaving the existing `cag-video-seo-agent` (YouTube) untouched.

**Architecture:** Single orchestrator that turns one source asset (a talking-bird clip, a chick photo, a page) into platform-native posts for Instagram, Facebook, Pinterest, and TikTok — reusing one brand voice and one set of CITES/pricing guardrails. Platform differences live in the skill/data, not in separate agents. YouTube stays with `cag-video-seo-agent`. Research basis: [docs/research/social-media-landscape-2026-06-06.md](../../research/social-media-landscape-2026-06-06.md).

**Tech Stack:** Markdown agent/skill files (`.claude/agents/`, `skills/`), JSON config (`data/`), Python 3 for JSON edits + verification, existing repo scripts (`apply_model_tiers.py`, `verify_model_tiers.sh`, `add_first_person_golden_rule.py`, `add_clarification_checkpoint_rule.py`, `health-sweep.sh`).

---

## File Structure (decomposition lock-in)

| File | Responsibility | Action |
|---|---|---|
| `skills/social-content.md` | Per-platform writing playbook (IG/FB/Pinterest/TikTok specs, hashtags, calendar) — the agent's *vocabulary* | **Rewrite** (currently stale/broken) |
| `content/social/README.md` | Where social drafts live + folder conventions | Create |
| `content/social/calendar.md` | Rolling content calendar template | Create |
| `data/competitors.json` | Add a `social` object to each competitor; seed known handles | Modify (via script) |
| `scripts/add_social_schema.py` | Idempotent migration that adds the `social` block to every competitor | Create |
| `.claude/agents/cag-social-strategist.md` | The orchestrator agent | Create |
| `data/agent-registry.json` | Register new agent's model/effort tier | Modify |
| `CLAUDE.md` | Register agent (Tier 3) + note skill rewrite | Modify |

**Out of scope (YAGNI):** separate IG/FB/Pinterest/TikTok agents; X/Threads/Bluesky; any auto-posting/scheduling integration; the deeper per-competitor follower crawl (logged as research task, not built here).

---

### Task 1: Rewrite the broken `social-content.md` skill (CAG-correct)

**Files:**
- Modify (full replace): `skills/social-content.md`

**Why:** Current file injects brand-damaging errors — wrong breeder ("Lawrence & Cathy" → real **Mark & Teri Benjamin**), wrong location ("Omaha NE" → **Midland, TX**), wrong CITES ("Appendix 2" → **Appendix I**), garbled hashtags (`#toyafrican grey parrot`), references a non-existent `content/social/` dir.

- [ ] **Step 1: Replace the entire file with the corrected version**

Write `skills/social-content.md` with exactly this content:

```markdown
---
name: social-content
description: Writes platform-native social media content for CAG — Instagram captions, Facebook posts, TikTok/Reels hooks, Pinterest descriptions. Turns one source asset (talking-bird clip, chick photo, or a site page) into per-platform posts in the C.A.Gs first-person breeder voice. Reads content/social/ for drafts + data/price-matrix.json for pricing. Vocabulary for @cag-social-strategist.
tools: [Read, Write, Bash]
---

## Golden Rule
> **First-Person Brand Voice (ALWAYS):** Write as the breeder — "we / our / here at C.A.Gs." Our birds, credentials, and process are *ours*, not described from outside. Exception: encyclopedic species facts stay neutral.
> **CITES-safe (ALWAYS):** African Greys are CITES **Appendix I**, captive-bred in the USA, legal to own/transfer with documentation. NEVER imply wild-caught or illegal trade. NEVER use #citesappendix2.
> **Never fabricate:** prices come from data/price-matrix.json; availability from data/clutch-inventory.json; buyer stories from data/case-studies.json. No invented counts, no invented testimonials.
> Use Claude Code first; only reach for external tools when the task genuinely needs them.

---

## Purpose

Social content is NOT repurposed website copy — different voice, rhythm, and CTA. The research basis (docs/research/social-media-landscape-2026-06-06.md) is blunt: **breeders lose on social.** The category is owned by talking-bird personality accounts, rescue voices, and evergreen reference content. So CAG social rides the entertainment/education engine and converts attention to the website — it does NOT post "for sale" listings as primary content.

## Breeder Facts (source of truth — never contradict)
- **Breeders:** Mark & Teri Benjamin (family: James, Allyson). Brand voice name: **C.A.Gs**.
- **Location:** Midland, TX. (NOT Omaha.)
- **Credentials:** captive-bred USA, USDA AWA licensed, DNA-sexed (PCR), CITES **Appendix I**.
- **Variants:** Congo African Grey (CAG) · Timneh African Grey (TAG).
- **Pricing/shipping:** read data/price-matrix.json + data/financial-entities.json. Canonical card line: `Ships nationwide · $185 airport · $350 home`. Never hardcode a different number.
- **Bird icon:** never the generic 🦜 parrot emoji. In text-only contexts use `[CAG]`/`[TAG]`.

## On Startup — Read These First
1. Check content/social/ for existing drafts + the calendar.
2. Read data/price-matrix.json (pricing) + data/clutch-inventory.json (availability).
3. Ask: "What's the source asset (clip/photo/page)? Which platforms? Goal — engagement, traffic, or DMs?"

## Platform Specifications

### Instagram / Reels (HIGH priority)
- Caption 150–300 words (2,200 max). First line stops the scroll (before the "more" cutoff).
- Hashtags 20–30, mixed size/breed/lifestyle/location (see clusters below).
- CTA: "DM us AVAILABLE", "link in bio", or comment — DM CTA preferred (algorithm favors DM).
- Format: Hook → Story → CTA → Hashtags.
- Headwind: the loudest IG voices are anti-breeding/pro-rescue. Never argue rescue; out-document it (welfare, CITES paperwork, USDA AWA).

### Facebook (HIGH priority — buyer demographic skews 40–65+)
- 100–250 words (longer underperforms). Max 3 hashtags, at end only.
- Direct site link allowed. Format: Hook → Value → CTA → Link.
- Owner groups ban overt selling — post value/education there, not listings.

### TikTok / Reels (MEDIUM — top-of-funnel, repurpose only)
- 30–60s script. First 3 seconds deliver the payoff. Hook → 3 beats → CTA.
- On-screen text = key points only. CTA: "Follow for weekly parrot updates."
- Audience skews too young for a $1,500+ purchase — treat as brand reach + Reels reuse, not sales.

### Pinterest (MEDIUM-HIGH — evergreen Google traffic, zero breeder competition)
- Description 100–200 words, keyword-rich. Title = keyword + benefit.
- Boards: "African Grey Parrots", "Congo vs Timneh", "African Grey Care".
- CTA: link to the SPECIFIC page (care/comparison/price), not the homepage.

### X / Threads / Bluesky
- Skip. Not where African Grey buyers are (research-confirmed). At most auto-syndicate.

## Content Calendar Framework

| Post Type | Frequency | Platform | Goal |
|---|---|---|---|
| Available bird | as available | IG, FB | DMs + inquiries |
| Chick/fledgling milestone | weekly | IG, TikTok | engagement + follows |
| Health/CITES/trust education | 2×/month | all | authority + trust |
| Behind the scenes (Mark & Teri) | 2×/month | IG, FB | personal connection |
| Family/buyer story | monthly | all | social proof (from case-studies.json) |
| Congo vs Timneh comparison | monthly | Pinterest, FB | traffic |
| Anti-scam / "verify a real breeder" | 2×/month | all | trust + traffic (scam content ranks) |
| FAQ answer | 2×/month | all | traffic + AIO |

## Caption Tone Rules
1. Specific, not generic — "she climbs into your lap before you sit down" > "super loving".
2. Name the bird if named (use clutch-inventory.json); else "this little one" + variant.
3. Transparent pricing — include price in availability posts, never "DM for price".
4. Urgency without pressure — "2 chicks remaining" is honest; "BUY NOW" is desperation.
5. First-person — "Teri noticed this morning he's already mastered step-up…".

## Hashtag Clusters (copy-paste ready — corrected)

### Breed
`#africangrey #africangreyparrot #congoafricangrey #timnehafricangrey #africangreysofinstagram #greyparrot`

### Trust
`#captivebred #dnasexed #healthtestedparrots #ethicalbreeder #usdalicensed #citesappendixI`

### General parrot
`#parrotsofinstagram #parrotlove #talkingparrot #parrotlife #birdsofinstagram #parrotbreeder`

### Location (customize)
`#midlandtx #texasparrots #africangreytexas` (swap to the buyer-audience state/city)

## Output Format
```
# Social Content — [Platform] — [Topic]
Date: [YYYY-MM-DD]
Platform / Goal: [..]
## Caption
[..]
## Hashtags
[..]
## Notes
- Best time to post / image to pair / link target: /[slug]/
```

## Rules
1. Never reuse website copy verbatim.
2. Prices from data/price-matrix.json — no hardcoding.
3. DM CTA preferred on IG; direct link OK on FB/Pinterest.
4. Platform-specific format required — never one caption for all platforms.
5. No engagement bait ("comment an emoji if…") — it gets penalized.
6. Never 🦜; never imply wild-caught; never #citesappendix2.
```

- [ ] **Step 2: Verify the corrections landed and the old errors are gone**

Run:
```bash
grep -ci "lawrence\|cathy\|omaha\|appendix 2\|appendix2\|toyafrican" skills/social-content.md
grep -ci "mark & teri\|midland\|appendix i\|appendixI" skills/social-content.md
```
Expected: first command prints `0`; second prints a number `>= 3`.

- [ ] **Step 3: Commit**
```bash
git add skills/social-content.md
git commit -m "fix(skill): rewrite social-content.md CAG-correct — Mark & Teri/Midland TX/CITES Appendix I/real hashtags; ride entertainment engine not for-sale copy"
```

---

### Task 2: Create the `content/social/` workspace

**Files:**
- Create: `content/social/README.md`
- Create: `content/social/calendar.md`

**Why:** The skill + agent both reference `content/social/`; it doesn't exist yet.

- [ ] **Step 1: Create `content/social/README.md`**
```markdown
# CAG Social Content Workspace

Drafts and the content calendar for CAG social media live here.
Managed by @cag-social-strategist (orchestrator) using skills/social-content.md.

## Conventions
- Drafts: `YYYY-MM-DD-[platform]-[topic].md` (e.g. `2026-06-10-instagram-maxy-talking.md`)
- One source asset → one file with all platform variants inside.
- Pricing pulled live from data/price-matrix.json — never hardcode.
- Nothing here auto-posts. All posts require breeder approval before publishing.

## Platforms in scope
Instagram/Reels, Facebook, Pinterest, TikTok. YouTube is handled separately by @cag-video-seo-agent.
```

- [ ] **Step 2: Create `content/social/calendar.md`**
```markdown
# CAG Social Calendar (rolling)

> Template. @cag-social-strategist fills/extends this. Cross-reference data/seasonal-calendar.json for peaks (Spring Bird Season Mar–May, Christmas, Valentine's, Mother's Day).

| Date | Platform(s) | Post type | Source asset | Status | Link target |
|---|---|---|---|---|---|
| (example) 2026-06-10 | IG + TikTok | Chick milestone | wk-3 photo | draft | /congo-african-grey-for-sale/ |
```

- [ ] **Step 3: Commit**
```bash
git add content/social/
git commit -m "feat(social): create content/social workspace + calendar template"
```

---

### Task 3: Add a social-tracking schema to `data/competitors.json`

**Files:**
- Create: `scripts/add_social_schema.py`
- Modify (via script): `data/competitors.json`

**Why:** `competitors.json` has no social fields, so monitoring can't compound. Add a `social` block to every competitor; seed the one confirmed handle (Afro Birds Farm → Facebook).

- [ ] **Step 1: Create the idempotent migration `scripts/add_social_schema.py`**
```python
#!/usr/bin/env python3
"""Idempotently add a `social` block to every competitor in data/competitors.json.
Re-run safe: only adds the block / missing keys; never overwrites existing handle data.
Seeds confirmed handles from the 2026-06-06 social research sprint."""
import json, pathlib

PATH = pathlib.Path("data/competitors.json")
SOCIAL_KEYS = ["instagram", "facebook", "youtube", "tiktok", "pinterest", "twitter_x"]
# Confirmed in docs/research/social-media-landscape-2026-06-06.md
SEED = {
    "afroBirdsFarm": {"facebook": "https://www.facebook.com/afrobirdsfarm/"},
}

def blank():
    b = {k: None for k in SOCIAL_KEYS}
    b["followers"] = None       # last-measured follower count (int) per platform later
    b["cadence"] = None         # observed posting frequency, free text
    b["last_social_audit"] = None
    return b

def main():
    data = json.loads(PATH.read_text())
    comps = data["competitors"] if isinstance(data, dict) and "competitors" in data else data
    iterable = comps.values() if isinstance(comps, dict) else comps
    changed = 0
    items = comps.items() if isinstance(comps, dict) else [(c.get("id"), c) for c in comps]
    for cid, c in items:
        if "social" not in c:
            c["social"] = blank(); changed += 1
        else:
            for k in SOCIAL_KEYS + ["followers", "cadence", "last_social_audit"]:
                c["social"].setdefault(k, None)
        if cid in SEED:
            for k, v in SEED[cid].items():
                if not c["social"].get(k):
                    c["social"][k] = v
    PATH.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"social block ensured on all competitors; {changed} newly added")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it**
```bash
python3 scripts/add_social_schema.py
```
Expected: prints `social block ensured on all competitors; N newly added` (N≈30 on first run, 0 on re-run).

- [ ] **Step 3: Verify JSON is valid + seed + count is right**
```bash
python3 -c "import json;d=json.load(open('data/competitors.json'));c=d['competitors'];vals=c.values() if isinstance(c,dict) else c;print('with social:',sum('social' in x for x in vals),'/',len(vals));print('afro fb:', (c['afroBirdsFarm'] if isinstance(c,dict) else [x for x in c if x['id']=='afroBirdsFarm'][0])['social']['facebook'])"
```
Expected: `with social: 30 / 30` and the Afro Birds Farm Facebook URL printed.

- [ ] **Step 4: Commit**
```bash
git add scripts/add_social_schema.py data/competitors.json
git commit -m "data(competitors): add social schema (handles/followers/cadence) to all 30; seed Afro Birds Farm FB"
```

---

### Task 4: Create the `cag-social-strategist` agent

**Files:**
- Create: `.claude/agents/cag-social-strategist.md`

**Why:** The orchestrator. Single agent, per research §6.

- [ ] **Step 1: Write `.claude/agents/cag-social-strategist.md`**

> NOTE: the `## Golden Rule` here carries only the agent-specific line. Task 7 runs the two injection scripts that prepend the standard Clarification-Checkpoint + First-Person rules (matching every other agent). Do not hand-duplicate those — let the scripts add them.

```markdown
---
name: cag-social-strategist
description: Orchestrates all non-YouTube social media for CongoAfricanGreys.com — Instagram, Facebook, Pinterest, TikTok. Turns one source asset (talking-bird clip, chick photo, or site page) into platform-native posts, builds the content calendar, and tracks competitor social. Reads skills/social-content.md as its writing vocabulary and data/ for live pricing/availability/stories. Never auto-posts. YouTube stays with @cag-video-seo-agent.
tools: [Read, Write, Bash]
model: claude-opus-4-8
effort: high
dynamic_workflow: false
---

<!-- EFFORT:START -->
> **Reasoning effort: HIGH.** Think through platform fit and the brand-voice/CITES guardrails before producing output. Do not answer reflexively.
<!-- EFFORT:END -->

## Golden Rule
> Social-media claims must be grounded in real CAG data — pricing from data/price-matrix.json, availability from data/clutch-inventory.json, buyer stories from data/case-studies.json, competitor social from data/competitors.json. NEVER fabricate follower counts, engagement, or testimonials. NEVER imply wild-caught/illegal trade (African Greys are CITES Appendix I, captive-bred USA). NEVER use the generic 🦜 emoji. All posts require breeder approval before publishing — this agent drafts, it does not auto-post.

---

## CAG Project Context
> **Site:** CongoAfricanGreys.com — captive-bred African Grey parrot breeder, Midland TX (Mark & Teri Benjamin).
> **Variants:** Congo African Grey · Timneh African Grey
> **Voice:** first-person "we / our / here at C.A.Gs."
> **Research basis:** docs/research/social-media-landscape-2026-06-06.md

---

## Purpose

You are the **Social Strategist** for CongoAfricanGreys.com. You own Instagram, Facebook, Pinterest, and TikTok (NOT YouTube — that is @cag-video-seo-agent). The research finding that governs everything: **breeders lose on social; the category is owned by talking-bird personality accounts, rescue voices, and evergreen reference content.** So you ride the entertainment/education engine and convert attention to the website — you never lead with "for sale" listings.

You are ONE orchestrator, not five platform agents, because the winning content is one source asset reused across platforms — only formatting differs (that lives in skills/social-content.md).

---

## On Startup — Read These First
1. **Read** `skills/social-content.md` — your platform specs, hashtag clusters, tone rules (your vocabulary).
2. **Read** `data/price-matrix.json` + `data/financial-entities.json` — pricing/shipping (never hardcode).
3. **Read** `data/clutch-inventory.json` — which birds are actually available.
4. **Read** `data/case-studies.json` — real buyer stories (never invent).
5. **Read** `data/seasonal-calendar.json` — upcoming peaks to plan around.
6. **Check** `content/social/` — existing drafts + the calendar.
7. **Ask the user:** "What's the source asset (clip/photo/page)? Which platforms? Goal — engagement, traffic, or DMs?"

---

## Core Capabilities

### 1. Repurpose (1 source → N platforms)
Take one asset and produce platform-native variants per skills/social-content.md (IG caption, FB post, Pinterest description, TikTok script). Same story, different rhythm/length/CTA/hashtags. Output to `content/social/YYYY-MM-DD-[platform]-[topic].md`.

### 2. Content calendar
Maintain `content/social/calendar.md` against the calendar framework in the skill + seasonal-calendar.json peaks (Spring Bird Season Mar–May is the major peak). Mark each row draft → approved → posted.

### 3. Platform strategy (apply, don't re-derive)
- **YouTube:** out of scope → route to @cag-video-seo-agent.
- **Instagram/Reels (HIGH):** chick milestones, owner stories, documentation reveals; DM CTA. Navigate the rescue headwind by out-documenting, never arguing.
- **Facebook (HIGH):** education + value in groups (no overt selling there); listings + links on the page; buyer demo skews 40–65+.
- **Pinterest (MED-HIGH):** evergreen pins → care/comparison/price pages (zero breeder competition = easy traffic).
- **TikTok (MED):** repurposed Reels only; top-of-funnel brand reach.
- **X/Threads:** skip.

### 4. Competitor social tracking
Read/update the `social` block in `data/competitors.json`. When you learn a real handle/follower count/cadence, write it (with `last_social_audit` date). Never fabricate — only record what was actually observed.

### 5. Anti-scam angle
Scam-warning content ranks well (research-confirmed). Produce "how to verify a real African Grey breeder" posts that convert buyer fear into trust in C.A.Gs — link to the on-site scam cluster.

---

## Hard Rules
1. Never auto-post. Draft → present → breeder approves → they publish.
2. Pricing/availability/stories from data files only. No invented numbers or testimonials.
3. CITES-safe always: Appendix I, captive-bred USA. Never wild-caught framing, never #citesappendix2.
4. First-person C.A.Gs voice on every caption.
5. Platform-specific formatting required (per skill). Never one caption for all.
6. Never 🦜. Text contexts use [CAG]/[TAG].
7. Recommend + Why: when offering options (angles, platforms, post times), mark one (Recommended) with a data-grounded reason and the trade-off.

---

## Handoffs
- **YouTube work** → @cag-video-seo-agent
- **Thumbnail/image assets** → cag-image-generation skill / @cag-image-pipeline / Higgsfield
- **Buyer-story sourcing** → @cag-case-study-agent
- **Seasonal briefs** → @cag-seasonal-content-agent
- **Newsletter cross-promo** → @cag-email-newsletter-agent
```

- [ ] **Step 2: Verify frontmatter + required sections exist**
```bash
grep -q "^name: cag-social-strategist" .claude/agents/cag-social-strategist.md && \
grep -q "^model: claude-opus-4-8" .claude/agents/cag-social-strategist.md && \
grep -q "## Golden Rule" .claude/agents/cag-social-strategist.md && \
grep -q "## On Startup" .claude/agents/cag-social-strategist.md && echo "STRUCT OK" || echo "STRUCT FAIL"
```
Expected: `STRUCT OK`.

---

### Task 5: Register the agent in the model-tier registry

**Files:**
- Modify: `data/agent-registry.json`

**Why:** Every agent must be in the registry so `apply_model_tiers.py` / `verify_model_tiers.sh` manage it. Tier `opus48_high` matches the agent's `effort: high`.

- [ ] **Step 1: Add the registry entry (idempotent edit)**
```bash
python3 -c "
import json
p='data/agent-registry.json'; d=json.load(open(p))
d['agents']['cag-social-strategist']={'tier':'opus48_high','dynamic_workflow':False}
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
print('registered:', d['agents']['cag-social-strategist'])
"
```
Expected: `registered: {'tier': 'opus48_high', 'dynamic_workflow': False}`.

- [ ] **Step 2: Apply + verify tiers**
```bash
python3 scripts/apply_model_tiers.py && bash scripts/verify_model_tiers.sh
```
Expected: apply runs clean; verify reports the new agent at opus48_high with no mismatches.

---

### Task 6: Register the agent in `CLAUDE.md`

**Files:**
- Modify: `CLAUDE.md`

**Why:** CLAUDE.md is the agent index; `@cag-agent-system-qa` flags unregistered agents.

- [ ] **Step 1: Add the agent line under "#### Tier 3 — Content Intelligence"**

Find the line that starts with `- `.claude/agents/cag-video-seo-agent.md`` and add immediately AFTER it:
```markdown
- `.claude/agents/cag-social-strategist.md` — orchestrates non-YouTube social (Instagram, Facebook, Pinterest, TikTok); 1 source asset → platform-native posts; reads `skills/social-content.md` + data files; tracks competitor social in `competitors.json`; never auto-posts; YouTube stays with cag-video-seo-agent
```

- [ ] **Step 2: Update the `social-content.md` skill description in CLAUDE.md's Skills list (if listed) to note it's the vocabulary for the new agent.** Search:
```bash
grep -n "social-content" CLAUDE.md || echo "skill not currently listed — skip"
```
If a line exists, ensure its description says "vocabulary/playbook for @cag-social-strategist." If `skip`, do nothing.

- [ ] **Step 3: Verify registration**
```bash
grep -c "cag-social-strategist" CLAUDE.md
```
Expected: `>= 1`.

---

### Task 7: Inject the standard Golden Rules into the new agent

**Files:**
- Modify (via scripts): `.claude/agents/cag-social-strategist.md`

**Why:** Every agent must carry the Clarification-Checkpoint + First-Person Golden Rules. The repo has idempotent scripts that prepend them — re-run after adding any agent (per CLAUDE.md).

- [ ] **Step 1: Run both injection scripts**
```bash
python3 scripts/add_clarification_checkpoint_rule.py
python3 scripts/add_first_person_golden_rule.py
```
Expected: both report the new agent patched (existing 66 unchanged/idempotent).

- [ ] **Step 2: Verify all three rule layers now present**
```bash
grep -c "Clarification Checkpoint\|First-Person Brand Voice\|require breeder approval\|require user approval\|auto-post" .claude/agents/cag-social-strategist.md
```
Expected: `>= 3` (the two injected rules + the agent-specific approval rule).

---

### Task 8: System QA + final verification + push

**Files:** none (verification only)

- [ ] **Step 1: Run the agent-system QA check**

Invoke `@cag-agent-system-qa` (or, if running headless, the structural grep below) to confirm the new agent passes: Golden Rule present, required sections present, data-file references valid, CLAUDE.md registered.
```bash
for s in "## Golden Rule" "## On Startup" "## Purpose" "name: cag-social-strategist" "model: claude-opus-4-8"; do grep -q "$s" .claude/agents/cag-social-strategist.md || echo "MISSING: $s"; done; echo "qa grep done"
```
Expected: only `qa grep done` (no MISSING lines).

- [ ] **Step 2: Confirm all referenced data files exist (no dead references)**
```bash
for f in price-matrix financial-entities clutch-inventory case-studies seasonal-calendar competitors; do test -f data/$f.json && echo "ok $f" || echo "MISSING data/$f.json"; done
```
Expected: six `ok` lines.

- [ ] **Step 3: Run the system health sweep (no build — config-only change)**
```bash
bash scripts/health-sweep.sh --no-build
```
Expected: green on git/agent-integrity/model-tiers (66+1 agents). Note any unrelated pre-existing warnings but do not fix them here.

- [ ] **Step 4: Commit + push everything remaining**
```bash
git add .claude/agents/cag-social-strategist.md data/agent-registry.json CLAUDE.md
git commit -m "feat(agent): add cag-social-strategist orchestrator (IG/FB/Pinterest/TikTok) — single-agent social system; registry+CLAUDE.md+golden rules"
git push
```
Expected: `push` succeeds (push = deploy, per CLAUDE.md).

---

## Self-Review (completed)

**Spec coverage:** social-content skill fix (T1) ✓ · workspace (T2) ✓ · competitor social schema (T3) ✓ · orchestrator agent (T4) ✓ · registry (T5) ✓ · CLAUDE.md (T6) ✓ · golden-rule injection (T7) ✓ · QA/push (T8) ✓. Single-agent-vs-many decision: implemented as single, per research §6. YouTube left untouched ✓.

**Placeholder scan:** no TBD/"handle edge cases"/"similar to" — full file contents inline. ✓

**Consistency:** agent `name: cag-social-strategist` identical in T4/T5/T6/T7/T8; registry key matches; `effort: high` ↔ tier `opus48_high`; data-file names match the keys verified on 2026-06-06. ✓

**Known nuance for executor:** the agent file's `## Golden Rule` is intentionally minimal in T4 — the injection scripts in T7 prepend the standard rules. Don't hand-write them in T4 or they'll duplicate.
```

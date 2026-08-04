---
name: cag-aeo-pass
description: Use when finishing any CAG page build, rebuild or polish and the page must be citable by AI answer engines — ChatGPT, Perplexity, Claude, Google AI Overviews. Also use when a page ranks but is never cited, when AI answers about African Greys quote competitors instead of us, when copy reads as anonymous "we/our" rather than named entities, or when checking freshness signals, brand-owned method names, BLUF openers, atomic sections, declarative sentences, or stat-bearing headers. Triggers - "run the AEO pass", "make this citable", "AI search optimization", "answer engine optimization", "GEO check".
---

# SKILL: CAG AEO Pass — Make the Page Citable

**Run this AFTER `cag-page-hardening` and BEFORE `cag-final-page-pass`.** Hardening
asks *does the page render*; this asks *can an answer engine lift a correct sentence
out of it and attribute it to us*.

```bash
npx astro build
python3 scripts/aeo_audit.py <slug> [<slug> ...]     # pass slugs LITERALLY
```

`ERROR` = fix before deploy. `WARN` = read the section, then decide.

> **Read `skills/cag-gate-integrity.md` first.** The BLUF check here is a **proxy** on
> sentence length and opening phrases — it cannot tell a wind-up from a legitimately
> long declarative sentence. Confirm any flagged section by reading it. And read the
> audit's own examined count: `0 pages matched` is not a pass.

**This skill does not restate what already exists.** Entity-first patterns, the
Inverse Pyramid, the four Featured-Snippet strategies and per-engine GEO targeting
live in **`skills/framework-aio-geo.md`** — read it for the *how*. This skill is the
six-part **gate**, plus the three parts that had no home anywhere in the system before
2026-07-30.

---

## Non-negotiable facts (verified against the data files 2026-07-30)

Three claims in circulation are wrong. Never write them, and correct them on sight.

| ✗ Never write | ✓ Correct | Why |
|---|---|---|
| "CITES **Appendix II**" | **CITES Appendix I** | Uplisted at CoP17, effective Jan 2017. The live pages say Appendix I **25×**; CLAUDE.md records this exact correction being made on 2026-05-29 per World Parrot Trust. Appendix II is a compliance-sensitive regression that was already fixed once. |
| "$1,500 to **$3,000**" | **$1,500–$3,500** | `price-matrix.json` and the adoption-cost price ladder top out at $3,500 (the bonded pair). |
| ~~"**3-day** health guarantee"~~ NOT A DEFECT | **both "72-hour" and "3-day" are correct** | 72 h is three days, but the health-guarantee page uses "72-hour" **25×** and "3-day" **zero** times; its whole voice lever is the enforceable 72-hr / 24-hr windows. Use the house register. |

Verified safe to use: `Mark & Teri Benjamin` · `Midland, TX` · `USDA AWA licensed` ·
`IATA` · "all 50 states" (claimed on 19 pages) · `Psittacus erithacus` (Congo) ·
`Psittacus timneh` (Timneh — a full species since the 2012 split; **not**
"Psittacus erithacus timneh").

Every figure still comes from `financial-entities.json` / `price-matrix.json` through
a helper, never a typed literal, and every health/credential claim stays inside the
**Verified-Claim Ledger**. AEO is not a licence to overclaim: a confidently-worded
false sentence is the worst possible outcome, because answer engines repeat it.

---

## Part 1 — BLUF (Bottom Line Up Front)

AI models weigh the start of a passage most heavily. **Every section opens with the
answer**, in one sentence, before any context.

| ✗ | ✓ |
|---|---|
| "Before we get into numbers, it's worth stepping back to consider the history of parrot keeping…" | "Congo African Greys from Mark & Teri Benjamin cost **$1,700–$3,500**, set by age and training." |
| "There are many things to think about when shipping a bird." | "Mark & Teri Benjamin ship IATA-compliant to all 50 states — **$185 airport, $350 home**." |

**Gate:** the audit flags any H2/H3 whose first sentence exceeds 32 words or opens
with a wind-up phrase. It is a proxy — read the flagged section. This stacks with the
EEBP openings the for-sale builder already mandates; BLUF is the *first sentence*
rule, EEBP is the *paragraph shape* rule.

## Part 2 — Atomic Content

Every section must survive being **chunked out of the page**. A section that only
makes sense after reading the one above it cannot be cited.

The test: **cover everything above the heading. Does the section still name its
subject, its actor, and its qualifier?**

| ✗ Not atomic | ✓ Atomic |
|---|---|
| "It also includes full documentation." | "Mark & Teri Benjamin's aviary is USDA AWA licensed and supplies **CITES Appendix I** captive-bred documentation with every bird." |
| "They wean between those weeks." | "Congo African Grey chicks wean at **12–16 weeks**, never sooner." |

Not machine-checkable — this is the skill's **human** item. Read three random sections
in isolation. If one needs its neighbour, rewrite its first sentence.

## Part 3 — Entity-Rich Writing

Replace generic nouns and pronouns with named entities, so an engine can bind our
brand to the topic.

- `our birds` → **`Psittacus erithacus`** / **`Congo African Grey`**
- `we` → **`Mark & Teri Benjamin's home aviary`** / **`C.A.Gs — Midland, TX`**
- `licensed` → **`USDA AWA licensed`**, **`CITES Appendix I captive-bred`**
- `tested` → **`PCR DNA-sexed`**, **`PBFD and Polyomavirus screened`**

**Measured on the 8 for-sale pages, 2026-07-30 — the gate exists because of this:**

```
                       binomial  breeder-name
eggs                          6             2
congo                         2             1
timneh                        6 (P. timneh) 1
hand-raised                   0             0     <- no binomial, no breeder
health-guarantee              1             0
dna-tested                    9             0
baby                          0             0     <- no binomial, no breeder
adoption-cost                 0             0     <- no binomial, no breeder
```

**3 of 8 pages name no species at all, and 4 of 8 never name the breeder.** The audit
WARNs on both, and on pronoun-heavy copy where `we/our/us` outnumber named entities.

## Part 4 — Simple, Declarative Sentences

One idea per sentence. Subject–verb–object. Extraction-ready.

> Every bird includes a DNA sexing certificate. We provide a 72-hour health guarantee.
> The birds are socialized with family from hatch.

The audit reports average sentence length and the count over 30 words. It does **not**
judge truth — that is the Verified-Claim Ledger's job. Anti-AI rhythm rules from
`skills/anti-ai-writing.md` still apply: declarative does not mean robotic, and a page
of identical short sentences fails the humour/voice gate.

## Part 5 — Strategic Formatting for Citations

Answer engines prefer structure they can lift whole.

- **Comparisons** — the Congo vs Timneh table answers "X vs Y" queries directly. The
  comparison cluster already ships these; make sure the *money* pages link them.
- **Lists** — enumerate documents, stages, tiers.
- **Stat-bearing headers** — put the number *in the heading*:
  "**12 Years** of Breeding Experience" · "**1,000+ Word** Vocabulary Potential" ·
  "**72-Hour** Health Guarantee" · "**$185** Airport / **$350** Home Delivery".

The audit counts tables, lists, and stat-bearing headers, and WARNs when a page has no
header carrying a figure. Headers still obey **Title Case** and the **declared header
style** (`framework-heading-hierarchy` §Header Style Selection).

## Part 6 — Brand Ownership and Freshness

### 6a. Label the method, so the expertise stays ours

Unlabeled expertise gets absorbed as generic knowledge. **Approved by the breeder
2026-07-30 — two labels, used for different things:**

| Label | Covers |
|---|---|
| **The Benjamin Home-Raising Protocol** | hand-feeding, weaning schedule, the 12–16-week wean gate — the *raising* process |
| **The Midland Socialization Method** | family handling, out-of-cage routine, noise/handling desensitisation — the *socialization* side |

Use them as proper nouns, capitalised, at least once per relevant page, and define
them once where first used. Before 2026-07-30 there were **zero instances site-wide**,
across 108 pages, 61 skills and 68 agents — so every page's raising process read as
generic advice any competitor could claim.

Keep them honest: they name a real process, they are not a certification. Never imply
third-party accreditation.

### 6b. Freshness is a schema signal, never a visible one

AI citations favour recently-updated pages. CLAUDE.md **bans visible dates**, so
freshness lives only in JSON-LD.

- `data/page-dates.json` holds real per-page git dates; `BaseLayout` injects a
  `WebPage` node with `datePublished` / `dateModified` for every route that does not
  already set its own. Coverage went **23 → 107 of 108 pages** on 2026-07-30.
- After any content change: `python3 scripts/generate_page_dates.py` and **commit the
  map**. `--check` fails when it is stale.
- **Never compute the date at build time.** `deploy.yml` uses `actions/checkout@v4`
  with no `fetch-depth` — a depth-1 clone — so a build-time `git log` reports the
  deploy date for every file and stamps a fake "today" on all 108 pages, every push.
  That is the visible-date dishonesty moved into JSON-LD, where it is worse.
- The audit **ERRORs** on a missing `dateModified` and **ERRORs** on any visible
  "Updated <month> <year>" / "Last updated" / "Posted on" stamp.

### 6c. Bird listings are the freshness engine

The `/available/` pages carry genuinely changing facts. Update age, weight and new
vocabulary as they change — that is real freshness, not date-churn.

**Standing gap:** `clutch-inventory.json` holds **9** birds (Amie, Bery, Carl, Elad,
Evie, Jins & Jeni, Joys, Loti, Roys) and only **6** have `/available/` pages. **Carl,
Joys and Loti have no page**, so there is nothing to keep fresh. Build them before
relying on listings as the freshness engine.

### 6d. Refresh sleeper pages

A page with backlinks and declining traffic is the cheapest AI-visibility win.
Identify it, refresh with current figures and an original statistic, regenerate the
date map, redeploy. Needs GSC data to target properly — blocked until the GSC MCP
lands.

---

## Quick Reference

| Part | Gate | Machine-checked? |
|---|---|---|
| 1 BLUF | first sentence ≤32 words, no wind-up opener | proxy |
| 2 Atomic | section survives being chunked out | **human** |
| 3 Entity-rich | binomial + breeder name present; not pronoun-heavy | yes |
| 4 Declarative | avg sentence length, count over 30 words | yes (advisory) |
| 5 Formatting | ≥1 table/list, ≥1 stat-bearing header | yes |
| 6a Labeled | one of the two approved method names present | yes |
| 6b Freshness | `dateModified` in JSON-LD, **zero** visible dates | yes (ERROR) |

## Common Mistakes

- **Writing "CITES Appendix II."** It is Appendix I. This has been corrected once
  already; do not reintroduce it.
- **Adding a visible "Updated July 2026".** Banned. The signal is schema-only.
- **Treating a build-time git date as freshness.** Depth-1 CI makes it a lie.
- **Overclaiming to sound citable.** An engine repeats what it lifts. Stay inside the
  Verified-Claim Ledger.
- **Turning declarative into robotic.** `anti-ai-writing` still applies.
- **Trusting the BLUF proxy.** It flags long first sentences; some are fine. Read them.
- **Inventing a third method name.** Two are approved. Adding more dilutes both.

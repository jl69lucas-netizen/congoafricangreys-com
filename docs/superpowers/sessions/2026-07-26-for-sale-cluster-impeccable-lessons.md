# For-Sale Cluster — Impeccable Pass: Lessons & Reusable Playbook

**Session:** 2026-07-26 · **Plan:** `docs/superpowers/plans/2026-07-26-for-sale-cluster-impeccable-pass.md`
**Scope:** the 6 built for-sale pages — hand-raised · dna-tested · health-guarantee · eggs · congo · timneh
**Outcome:** Phases 0–3 and 5–7 complete. Phase 4 resolved as a non-issue (see §2). Phase 1.1 (self-hosted
fonts) deferred by the breeder to the full-site pass.

> **Read this before the next for-sale group.** §1 is the thing that will save the most time; §7 is the
> copy-paste command sequence.

---

## 1. The single most important lesson: verify the gate before you fix the page

**Four of this session's "defects" were bugs in the checkers, not the pages.** Fixing the pages would have
been wasted work *and* would have degraded correct code.

| Reported | Reality | Root cause in the checker |
|---|---|---|
| 7 tap-target ERRORs | 0 real | Matched `li`/`pill`/`chip` in a selector *name* and treated decorative rows as pointer targets; read only `min-height`, so `height:28px` fell through to a font-size guess |
| 6 icon-baseline WARNs | 0 real | Matched keywords across **comments** — a `/* GREEN TICK */` comment flagged whatever rule sat beneath it; also didn't know `place-items` is shorthand for `align-items` |
| "body copy runs 84ch" | Already correct at 70ch | The §2y probe approximated `ch` as `0.5em`; IBM Plex Sans's `0` advance is ~`0.6em`, inflating every reading ~20% |
| 23 body dup crossovers | 0 real | Whitelist didn't encode reviews / counter strip / read-card labels / doc-badge lists, all of which CLAUDE.md explicitly permits |

**The rule, now binding on this cluster:** when a gate reports a defect, open the flagged rule and confirm
the defect is real *before* editing a page. The plan already said this for Phase 0 ("if a defect from the
brief is not reproduced, the check is wrong — fix the check, not the page"). It applies in both directions.

**How to verify cheaply:**
- a11y claims → run Lighthouse. It agreed with the code, not the scanner (100/100/100, 0 failed audits).
- "is this element interactive?" → grep the built HTML inside the component for `<a ` / `<button`.
- measure claims → measure in a real viewport, never from a formula.

---

## 2. Measuring `ch` correctly (this invalidated the whole Phase 4 premise)

Phase 4 was scoped as "bring every paragraph into 45–75ch". Measured properly, **the body copy was already
capped at 70ch on all six pages** and the only genuinely over-wide text was the FAQ answers, which carried
an explicit `max-width:none`. Phase 4 collapsed from a cluster-wide reflow to a 4-line CSS change.

Use the corrected probe in `skills/cag-page-hardening.md §2y`. Key points:
- Measure a **real `ch`** by rendering `"0"` in the element's own computed font. Never `fontSize * 0.5`.
- Open `<details>` first — FAQ answers have zero width while collapsed and get filtered out.
- **The 45ch floor is meaningless at 360px.** 360px minus padding at 16px ≈ 41ch, so everything reads as
  "too narrow". Filter on `> 75` at mobile.
- **Narrow is rarely a defect.** A 26ch card blurb is fine. Over-wide is what to chase.
- Uncapping a `<p>` inside an already-narrow box (`.ship-c p`, `.quote-c p`) is *correct* — those measured
  in band. Only uncapping inside a full-width container is a bug.

Result after the fix: congo 102→70ch, eggs 102→70ch, dna-tested 107→70ch, health-guarantee 107→70ch.

---

## 3. Bimodal metrics: never conclude from one Lighthouse run

`/dna-tested-african-grey-for-sale/` has a **bimodal** mobile CLS — ~0.44 or ~0.001 depending on a race.
Single runs led to a confident, wrong attribution ("the cross-sell block causes it"), reproduced through
three rounds of bisection that were all coin flips.

**Binding: judge any CLS/perf conclusion on ≥5 runs.** The project convention was already "warm
median-of-3"; for a bimodal metric even the median lies unless you look at the distribution.

Sampling command that works headlessly and is far cheaper than the MCP wrapper:

```bash
npx --yes lighthouse@12 http://localhost:4321/<slug>/ \
  --only-audits=cumulative-layout-shift --form-factor=mobile --screenEmulation.mobile \
  --throttling-method=simulate --output=json --quiet --chrome-flags="--headless=new" 2>/dev/null \
  | python3 -c "import json,sys;print('%.3f'%json.load(sys.stdin)['audits']['cumulative-layout-shift']['numericValue'])"
```

To name the shifting node, drop `--only-audits` for `--only-categories=performance` and read
`audits['layout-shifts'].details.items[].node.selector`.

Status of that CLS: **pre-existing** (identical distribution on the pre-session build), page-specific,
not root-caused. Full record + four ruled-out hypotheses in
`docs/reference/technical-seo-fixes-backlog.md`.

---

## 4. Sitewide bugs the cluster work surfaced

Both were in `src/components/Footer.astro` and affected **all 108 pages**:

1. **768px** — the bottom bar switched to a row at `md`, but the copyright line + 64px badge + its
   `whitespace-nowrap` label need ~808px, so the label ran 40px past the viewport and the whole document
   scrolled sideways. Fix: hold the stacked layout until `lg`.
2. **1024px** — the footer grid gives each column 160px, and `info@congoafricangreys.com` was a bare text
   node in a flex row, an unshrinkable 206px item. Fix: wrap in a span with `[overflow-wrap:anywhere]`.

**Lesson: sweep breakpoints on a shared component, not just the page you're editing.** Verified at
360/768/820/1024/1280 on both a for-sale page and the homepage.

---

## 5. Component decisions worth reusing

**Section seams.** House idiom is **one seam before every section**; the hero carries no seam above it, so
`sections - seams <= 1` is the correct gate. health-guarantee had shipped 7 across 17 sections.

```bash
python3 scripts/seam_parity.py <slug> [<slug> ...]
```

> **The command previously published here was broken** (found 2026-07-29). It counted sections with
> `grep -c '<section class="sec"'`, a class only **2 of the 8** built for-sale pages use — congo, timneh,
> baby, eggs, dna-tested and hand-raised all use `<section id=...>`, so the probe reported **0 sections**
> and compared seams against nothing. It also counted seams with `grep -c 'class="seam"'`, which counts
> *lines*, not elements. `scripts/seam_parity.py` counts `<section` (any attributes) and tokenises the
> class attribute so `class="seam-wrap"` cannot double-count — a `\bseam\b` regex reads 34 seams for 17
> real ones, because `-` is a word boundary. **Never re-derive this check with grep.**
>
> True counts, measured 2026-07-29: eggs 16/15 · congo 15/15 · timneh 18/18 · hand-raised 19/18 ·
> health-guarantee 18/17 · dna-tested 19/18 · baby 22/21 · adoption-cost 10/10 — all PASS.

**The `.xsell` cross-sell strip (new this session).** Sits at the end of the existing reading/resources
section — *not* a new section, so it never triggers the Heading Outline Gate.
- Deliberately **not** more read-cards: those are editorial, cross-sell targets are product pages, and
  growing a 4-card grid to 7 identical cards is the card-grid trap.
- Full border + background tint. **Never a side stripe** (standing ban).
- Markup: `<div class="xsell"><p class="xsell-k">Also from our aviary</p>` then one `<p>` per target.
- The eyebrow is a `<p>`, not a heading, so uppercase styling is fine and Title Case does not apply.

**Read-card thumbnails.** They render at 120–148px. Always ship a small rung (`-240` or `-320`) and use
`srcset`; congo/timneh/eggs were fetching the full 760px file, four per page. Use a named helper, not an
inline replace-chain:

```js
const thumb = (p) => p.replace(/(-760)?\.webp$/, "-320.webp");
```

---

## 6. Cross-sell content rules (Phase 5, repeat verbatim for the next cluster)

- **2 FAQ entries per page**: one eggs question, one breeding-pair question. Written fresh from *that
  page's* angle — never pasted between siblings. They feed FAQPage schema automatically via the `faqs`
  array → `faqSchema` pattern every page shares.
- Angles used, so the next cluster picks *different* ones: health-guarantee = what a written warranty can
  and cannot cover · dna-tested = no lab can sex inside a shell; a pair needs two certificates ·
  hand-raised = tameness is built after hatching, not by it · congo = incubation arithmetic + scam
  exposure · timneh = why its breeding stock moves rarely · eggs = a pair answers the real ambition.
- **Link budget per page:** only the targets that page doesn't already link in body copy. Pages with none
  get all three; pages that already link one get the other two. Avoids duplicate targets on one page.
- **Anchor Diversity Ledger is enforced** — no two pages may use the same anchor text for the same target.
  One collision slipped through and was caught by scripting the check; do that check, don't eyeball it.
- The eggs page links to **weaned chicks**, never to itself.

### Verified anchor ledger (do not reuse these)

| Target | Anchors already used |
|---|---|
| `/african-grey-parrot-bird-eggs-for-sale-usa/` | African Grey egg page · Fertile African Grey eggs · Eggs priced by sex · Hatching a grey yourself · Congo eggs in an incubator |
| `/african-grey-breeding-pair-for-sale/` | proven breeding pair · Proven-Producer Pair · See the pair · Adult breeding pairs · A lab-sexed adult pair · Aviary-raised adult pairs · The breeding pair we currently hold · Adults kept back for breeding |
| `/congo-african-grey-parrot-pair-for-sale/` | Congo African Grey pair page · Our Congo pair listing · The Congo pair listed separately · Two Congos sold together · A documented Congo pair · The larger Congo equivalent |

---

## 7. The dup gate is now usable — and how to keep it honest

`scripts/dup_content_audit.py` used to FAIL on every for-sale page because of mandated-identical furniture.
Two changes made it meaningful:
- Review/testimonial and read-card blocks now skip as **chrome** (alongside jump rails and TOCs) — they are
  syndicated components, not page prose.
- Shipping line, counter strip, doc-badge lists and CTA labels added as **short whitelist stems**.

**Stems must be anchored mid-phrase.** The shingle window slides, so a stem starting at the first word of a
list gets missed as soon as the reported run starts one word later. This cost three iterations.

**Always prove the gate isn't blinded after widening it:** inject a deliberately duplicated sentence into
real body prose, confirm FAIL, remove it, confirm PASS. Done this session; repeat after any whitelist edit.

---

## 8. Copy-paste command sequence for the next cluster

```bash
# 0. state
git checkout main && npx astro build

# 1. gates BEFORE fixing anything — and verify each finding is real
python3 scripts/page_hardening_scan.py <slug> [<slug> ...]
python3 -m pytest tests/ -q

# 2. seam parity  (NEVER grep for this — see §5; the old grep compared against 0 sections)
python3 scripts/seam_parity.py <slug> [<slug> ...]

# 3. measure, don't assume (real-ch probe + overflow probe from skills/cag-page-hardening.md §2y / §2a)
#    at 360 / 768 / 820 / 1024 / 1280, on a page AND the homepage

# 4. dup gates, scoped to the cluster
python3 scripts/dup_content_audit.py <slugs>
python3 scripts/dup_content_audit.py --headers <slugs>

# 5. final audit + verification
python3 scripts/final_page_audit.py
bash scripts/health-sweep.sh
python3 scripts/generate_sitemaps.py

# 6. perf — ≥5 runs, look at the DISTRIBUTION not the median
```

---

## 9. Deferred / still open

1. **Phase 1.1 self-hosted fonts** — breeder deferred to the full-site pass. `public/fonts/` is empty;
   `BaseLayout.astro` still preconnects `fonts.googleapis.com` and fetches the Google CSS, so the
   HTML → CSS → woff2 discovery chain is live on all 109 URLs. This is the real LCP lever and the leading
   suspect for the dna-tested CLS race.
2. **Phase 1.2 verification** — the survivor tag was inverted vs the plan (kept `googletagmanager.com`
   deferred, dropped the `/70de/` gateway, which still returns HTTP 200). The network trace and the
   `generate_lead`-reaches-GA4 confirmation were never run. **Do not leave analytics unproven.**
3. **dna-tested hero CLS** — see §3 and the backlog entry.
4. **Sitewide body duplication** — ~5,857 crossovers across the ~100 location pages, untouched and out of
   scope here. Separate piece of work.

### Anchors spent by `/african-grey-parrot-adoption-cost/` (2026-07-27)

| Target | Anchor now spent |
|---|---|
| `/african-grey-parrot-bird-eggs-for-sale-usa/` | Incubating your own clutch |
| `/african-grey-breeding-pair-for-sale/` | Breeding stock carries its own price logic |
| `/african-grey-parrot-price/` | Our cost-of-ownership breakdown |
| `/african-grey-adoption/` | honest guide to where adoption actually works |
| `/affordable-african-grey-birds-for-sale/` | Our lowest-priced documented greys |
| `/timneh-african-grey-for-sale/` | Timneh pricing starts lower |
| `/dna-tested-african-grey-for-sale/` | DNA-tested Greys page |
| `/african-greys-for-sale-with-health-guarantee/` | The guarantee attached to every price |
| `/how-to-avoid-african-grey-parrot-scams/` | Listings priced below our floor |
| `/buy-african-grey-parrots-with-shipping/` | full nationwide shipping guide |
| `/best-african-grey-parrot-food/` | guide to the pellet brands we actually feed |
| `/african-grey-parrot-care-guide/` | care guide sets out the routine we hand every buyer |
| `/african-grey-parrot-lifespan/` | How Long an African Grey Actually Lives |
| `/#tools` | our homepage first-year calculator |

**Two collisions were caught here by scripting the check, exactly as section 6 warns.** The first draft
reused *Hatching a grey yourself* and *Adults kept back for breeding*, both already spent on the eggs and
breeding-pair targets. Eyeballing would have shipped them.

Run the check against the BUILT page, pasting the spent anchors from the tables above into `spent`:
parse every `<a href>` out of `dist/<slug>/index.html`, strip inner tags from the anchor text, and report
any anchor whose lowercase form already appears against that same target. Script it; do not read it.

### Deferred from the adoption-cost build (2026-07-27)

1. **Infographic slots are empty by design.** The breeder chose build-first, images-last. Eight prompts
   are written and collision-checked in the page's prompt pack section 7c. Nothing renders a broken box —
   the slots simply carry no image yet, so the live page reads as finished.
2. **`/african-grey-adoption/` and `/african-grey-parrot-price/` duplicate each other**, and it is
   pre-existing: one shared body passage of 101 words plus five crossover headers, including
   `why apply with us?` and `adopt an {species} — inquiry form`. Neither page was touched by this build.
   Worth its own cleanup pass.
3. **The homepage first-year calculator hardcodes `Timneh — $1,600`** where `price-matrix.json` holds
   `$1,500–$1,600` and Evie is listed at `$1,500`. Out of scope here; logged so it is not lost.

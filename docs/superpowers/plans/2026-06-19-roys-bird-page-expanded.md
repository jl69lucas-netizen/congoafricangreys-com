# Roys Bird Page — Expanded SEO/GEO/AEO Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild `/available/roys/` as the approved reference for an expanded (competitor-max + 1,500 words), cannibalization-safe, first-person African Grey bird page — then batch-apply to the other five birds.

**Architecture:** Single Astro page at `src/pages/available/roys/index.astro`, Direction-D theme inherited via BaseLayout (never re-implemented). Fixed bird-page section order, expanded with a competitor-driven AEO snapshot box, a counter-positioning section, an expanded Shipping & Logistics section, and one newsletter placement. Each bird owns a distinct *modified* long-tail primary + a distinct expansion theme so six long pages do not duplicate each other or cannibalize the variant/location cluster. Verification is RED→GREEN against `scripts/final_page_audit.py --birds` plus greppable structural checks in `dist/`.

**Tech Stack:** Astro · Tailwind utility classes (homepage idiom) · `<Schema>` / `<TrustBar>` / `<CTA>` / `<Breadcrumb>` components · Python (`final_page_audit.py`, `generate_sitemaps.py`, Pillow for WebP) · firecrawl MCP (competitor word counts) · git push = Cloudflare Pages deploy.

**Spec:** `docs/superpowers/specs/2026-06-19-bird-pages-expanded-seo-design.md`
**Research (Sprint-0, done):** `docs/research/2026-06-19-bird-pages-competitive-analysis.md` (Page 1 = Roys)

**Reference files to read before starting:**
- `src/pages/available/roys/index.astro` (current lean page — the RED baseline)
- `src/pages/index.astro` (homepage — match heading sizes / fonts / text scale exactly)
- `skills/cag-bird-listing-page.md`, `skills/anti-ai-writing.md`, `skills/cag-seo-master-checklist.md`
- `data/clutch-inventory.json`, `data/financial-entities.json`, `data/price-matrix.json`, `data/bird-inventory.json`
- `docs/reference/external-link-library.md`, `sessions/2026-06-03-homepage-entity-map.md` (Verified-Claim Ledger)

**Global rules (apply to every task):** work on `main`; first-person C.A.Gs voice; ledger-only (unconfirmed → GAP-FLAG, never invent); no visible date (schema only); no phone number in body; single `Product`+`Offer` (never `AggregateOffer`); prices from data files; verify schema/headings in `dist/` (rendered), not source greps.

---

## Phase 1 — Research extension (no page edits)

### Task 1: Measure Roys's competitor word counts → set the word target

**Files:**
- Modify: `docs/research/2026-06-19-bird-pages-competitive-analysis.md` (append a "Measured word counts" block under Page 1)

- [ ] **Step 1: Scrape the five Roys competitors and count visible words**

Use firecrawl (`mcp__firecrawl-mcp__firecrawl_scrape`, `formats: ["markdown"]`) for each, then count words on the main content (exclude nav/footer boilerplate):
- `https://birdbreeders.com/` (relevant congo listing)
- `https://silvergatebirdfarm.com/`
- `https://exoticparrotsplanet.com/`
- `https://mybabyparrot.com/`
- `https://graybreedersfoundation.yolasite.com/`

If a fetch 403s, retry once; if still blocked, mark it `NOT FETCHED` (never fabricate a number).

- [ ] **Step 2: Record the table and compute the target**

Append to the research doc under Page 1:

```markdown
### Measured competitor word counts (2026-06-19)
| Competitor | Visible words |
|---|---|
| birdbreeders.com | <n> |
| silvergatebirdfarm.com | <n> |
| exoticparrotsplanet.com | <n> |
| mybabyparrot.com | <n> |
| graybreedersfoundation | <n or NOT FETCHED> |
**MAX = <n> → Roys word target = MAX + 1,500 = <target>**
```

- [ ] **Step 3: Commit**

```bash
git add docs/research/2026-06-19-bird-pages-competitive-analysis.md
git commit -m "research(roys): measured competitor word counts + word target"
```

---

### Task 2: 100+ intent fan-out + cannibalization map for Roys

**Files:**
- Create: `sessions/2026-06-19-roys-fanout-cannibalization.md`

- [ ] **Step 1: Write the 100+ intent-based keyword fan-out**

Expand the research doc's Roys keyword universe to 100+ variations grouped by intent (transactional / commercial-investigation / informational / long-tail / PAA / voice). Roys OWNS the primary **"male congo african grey for sale"** (modified long-tail), not the bare head term. Seed from research doc Page 1 §3 + §11.

- [ ] **Step 2: Write the cannibalization map**

Table mapping Roys's owned terms against each potential overlap, with the verdict (CLEAR / SPLIT-APPLIED / DEFER-TO):

```markdown
| Term | Roys | Other owner | Verdict |
|---|---|---|---|
| congo african grey for sale (bare) | secondary only | /congo-african-grey-for-sale/ (variant) | DEFER-TO variant |
| male congo african grey for sale | PRIMARY | — | CLEAR |
| female congo african grey for sale | none | Bery | DEFER-TO Bery |
| hand-raised baby congo ... | none | Amie | DEFER-TO Amie |
| congo african grey for sale [state] | none | location pages | DEFER-TO location |
```

Confirm Roys does not target any state/city term and does not claim the bare head term.

- [ ] **Step 3: Commit**

```bash
git add sessions/2026-06-19-roys-fanout-cannibalization.md
git commit -m "research(roys): 100+ intent fan-out + cannibalization map"
```

---

## Phase 2 — Outline + link prep

### Task 3: Write the Roys build outline (section-by-section budget)

**Files:**
- Create: `sessions/2026-06-19-roys-outline.md`

- [ ] **Step 1: Write the outline**

One row per section (order from spec §3), with: heading text (from research doc Page 1 §9, two-keyword conversational), word budget (summing to the Task 1 target), framework blend (spec §4), entities to embed (research doc Page 1 §4 — *Psittacus erithacus*, CITES App I, AAV, DNA sexing, hatch cert/leg band, USDA AWA, IATA LAR, Delta/United/American, Midland TX, hand-rearing/weaning, 40–60yr), internal links + anchors (research doc §13), and any external authority link. Mark which sections carry the BLUF answer and which carry the snippet-bait list.

- [ ] **Step 2: Verify the budget sums to the target**

The sum of per-section word budgets must be ≥ the Task 1 target. Adjust the expansion-theme sections (About, Why, Counter-positioning, Shipping & Logistics) to absorb the +1,500 — NOT the shared-fact sections (Documentation, Parents), which stay link-out-brief to avoid duplication.

- [ ] **Step 3: Commit**

```bash
git add sessions/2026-06-19-roys-outline.md
git commit -m "plan(roys): section-by-section build outline + word budget"
```

---

### Task 4: Verify + register new external authority targets

**Files:**
- Modify: `docs/reference/external-link-library.md`

- [ ] **Step 1: Verify 200 for the proposed new targets**

```bash
for u in "https://www.avma.org/resources-tools/pet-owners/petcare/pet-birds" "https://lafeber.com/pet-birds/species/african-grey-parrot/"; do
  echo "$u"; curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0" "$u"; done
```

Expected: `200` for each. If a URL is not 200, find the correct deep page (species/care page, not homepage) or drop it. Confirm existing targets still resolve: parrots.org/encyclopedia/grey-parrot/, aav.org, cites.org (403 to curl ≠ dead — retry `-A "Mozilla/5.0"`).

- [ ] **Step 2: Add the verified URLs to the library**

Add each verified URL under the authority category with its topic + the exact anchor phrasing to use mid-sentence.

- [ ] **Step 3: Commit**

```bash
git add docs/reference/external-link-library.md
git commit -m "docs(links): add AVMA + Lafeber authority targets (verified 200)"
```

---

## Phase 3 — RED baseline

### Task 5: Capture the RED baseline for Roys

**Files:**
- Create: `sessions/2026-06-19-roys-red-baseline.md`

- [ ] **Step 1: Build + run the audit against the current lean page**

```bash
npx astro build
python3 scripts/final_page_audit.py --birds 2>&1 | tee /tmp/roys-red.txt
```

- [ ] **Step 2: Record the failing/expected-to-change state**

Capture in the baseline file: current Roys visible word count (well under target), and confirm the page is MISSING: AEO Bird Snapshot box, counter-positioning section, expanded Shipping & Logistics section, newsletter placement, 5th+ FAQ. These are the deltas this build must turn GREEN.

```bash
# current word count (rendered)
python3 - <<'PY'
import re,sys,html
t=open('dist/available/roys/index.html').read()
t=re.sub(r'<script[^>]*>.*?</script>','',t,flags=re.S)
t=re.sub(r'<style[^>]*>.*?</style>','',t,flags=re.S)
t=html.unescape(re.sub(r'<[^>]+>',' ',t))
print('words:',len(t.split()))
PY
```

- [ ] **Step 3: Commit**

```bash
git add sessions/2026-06-19-roys-red-baseline.md
git commit -m "test(roys): RED baseline — current word count + missing sections"
```

---

## Phase 4 — Build (section by section)

> Each build task: author the section to the outline (Task 3) via the 4-Move Loop, first-person + anti-AI + ledger-only, then run the task's verification grep. Match homepage heading classes exactly (`font-lora font-bold text-3xl` for H2, `text-4xl sm:text-5xl` H1, `text-stone-600 leading-relaxed` body — confirm against `src/pages/index.astro`). Keep `<BaseLayout … hideGlobalCta>` and the existing `<CTA>` (one CTA per page rule).

### Task 6: Head, meta, and schema

**Files:**
- Modify: `src/pages/available/roys/index.astro:1-55` (frontmatter)

- [ ] **Step 1: Update the 4-part meta**

`title` (≤275) keeps "Roys — Male Congo African Grey For Sale | $2,300 | C.A.Gs – Midland, TX"; ensure `description` ≤155 ends with brand + an LSI/NLP variant. Primary keyword "male congo african grey for sale" present in title.

- [ ] **Step 2: Confirm schema objects (extend, don't duplicate)**

Keep the existing `productSchema` (single `Offer`, InStock, 2300), `faqSchema` (will grow to ≥6 in Task 14), and the three `<Schema>` renders + `<Schema type="organization" />`. Verify `dateModified` is schema-only (no visible date anywhere).

- [ ] **Step 3: Verify in dist**

```bash
npx astro build
python3 - <<'PY'
import re,json
t=open('dist/available/roys/index.html').read()
for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',t,flags=re.S):
    d=json.loads(b); print(d.get('@type'))
PY
```
Expected: `Product`, `FAQPage`, `BreadcrumbList`, `Organization` (exactly one `Offer`, no `AggregateOffer`).

- [ ] **Step 4: Commit**

```bash
git add src/pages/available/roys/index.astro
git commit -m "feat(roys): meta + schema head for expanded page"
```

### Task 7: Hero + AEO Bird Snapshot box

**Files:**
- Modify: `src/pages/available/roys/index.astro` (hero section + new snapshot box after hero)

- [ ] **Step 1: Keep the hero; add the BLUF + Snapshot box**

H1 `Roys — Male Congo African Grey For Sale` (primary KW). First 100 words must contain the primary keyword AND the CITES Appendix I + captive-bred-USA + USDA AWA compliance line (Rule 44) AND a 40–60yr lifespan clause (Rule 46). Add the **Bird Snapshot** box (variant · sex · age · price · talking · documentation · ships) as a declarative ≤50-word featured-snippet target (research doc §10).

- [ ] **Step 2: Verify**

```bash
npx astro build
grep -o "CITES Appendix I" dist/available/roys/index.html | head -1
grep -o "Bird Snapshot\|Snapshot" dist/available/roys/index.html | head -1
```
Expected: both match.

- [ ] **Step 3: Commit** `git commit -am "feat(roys): hero BLUF + AEO snapshot box"`

### Task 8: About + Why (page primary AIDA + EBP)

- [ ] **Step 1:** Expand About (`What is Roys like to live with?`) and Why (`Why Roys might be the right grey for you`) to their outline budgets — high-energy talking Congo + active-family fit theme. One piece of high-resolution breeder detail per ~500 words; link `/congo-vs-timneh-african-grey/` and `/african-grey-parrot-guide/` mid-sentence (species facts link-out, not re-taught).
- [ ] **Step 2:** `grep -c "leading-relaxed" dist/available/roys/index.html` increased vs RED baseline.
- [ ] **Step 3: Commit** `git commit -am "feat(roys): expanded About + Why (AIDA+EBP)"`

### Task 9: Health & Documentation (EBP, ledger-only)

- [ ] **Step 1:** Keep the docs list link-out-brief (DNA cert, AAV health cert, hatch cert+band, CITES captive-bred, weaning, USDA AWA). EBP framing. NO PBFD/Polyomavirus. Link `/cites-african-grey-documentation/`, `/african-grey-parrot-health-guarantee/`, `/dna-tested-african-grey-for-sale/`. Add ONE external authority link (AAV or AVMA) mid-sentence.
- [ ] **Step 2:** `grep -i "PBFD\|polyomavirus" dist/available/roys/index.html` → expected: NO match.
- [ ] **Step 3: Commit** `git commit -am "feat(roys): documentation section (EBP, ledger-only)"`

### Task 10: Counter-positioning + comparison list (snippet bait)

- [ ] **Step 1:** New H2 `Why a real $2,300 Congo beats an $850 "bargain"` with H3s (no paperwork · no DNA/vet · no breeder you can verify) and a clean "real vs cheap" bulleted/comparison list for snippet capture. PAS/PDB framing. Link `/how-to-avoid-african-grey-parrot-scams/` + `/african-grey-parrot-price/` mid-sentence.
- [ ] **Step 2:** `grep -o '\$850' dist/available/roys/index.html | head -1` → expected: match (use `grep -oF` for `$`).
- [ ] **Step 3: Commit** `git commit -am "feat(roys): counter-positioning + real-vs-cheap list"`

### Task 11: Pricing & What's Included

- [ ] **Step 1:** Keep the price/reservation + included grid; figures from `financial-entities.json` / `price-matrix.json` ($2,300, $200 deposit, $185 airport, $350 home). QAB micro-answers. Link `/african-grey-parrot-price/`.
- [ ] **Step 2:** `grep -oF '$2,300' dist/available/roys/index.html | head -1` and `grep -oF '$185 airport' dist/available/roys/index.html | head -1` → both match.
- [ ] **Step 3: Commit** `git commit -am "feat(roys): pricing + what's included"`

### Task 12: Shipping & Logistics (expanded — the new section)

- [ ] **Step 1:** New H2 (conversational, e.g. `How does Roys get to you?`). BLUF first. Cover: IATA-compliant live-animal cargo (code LAR), Delta/United/American, **Avian Flight Nanny** option, example destination **airport codes (DEN/LAX/MIA/ORD)**, the two tiers ($185 airport / $350 home). NO state/city targeting (logistics, not geo). Figures consistent with `financial-entities.json`.
- [ ] **Step 2:** `grep -o "Flight Nanny\|LAR\|DEN\|LAX" dist/available/roys/index.html | sort -u` → expected: matches present.
- [ ] **Step 3: Commit** `git commit -am "feat(roys): expanded shipping + logistics section"`

### Task 13: Parent Birds / Our Aviary

- [ ] **Step 1:** Keep brief + link-out (Midland TX family aviary since 2014; specifics on request). Do not pad with duplicate species content.
- [ ] **Step 2: Commit** `git commit -am "feat(roys): parent birds / aviary"`

### Task 14: FAQ (≥6 Q, FAQPage schema, PAA)

**Files:** `src/pages/available/roys/index.astro` (visible `<details>` block + `faqSchema` in frontmatter)

- [ ] **Step 1:** Grow to ≥6 Q including the two new PAAs from research doc §11 ("Do male Congo greys talk well?", "Why is Roys $2,300 when I've seen greys for $850?"). QAB. **Every visible Q must have a matching `faqSchema` entry and vice versa** (same text).
- [ ] **Step 2: Verify visible == schema count**

```bash
npx astro build
echo "visible:"; grep -c "<summary" dist/available/roys/index.html
python3 - <<'PY'
import re,json
t=open('dist/available/roys/index.html').read()
for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',t,flags=re.S):
    d=json.loads(b)
    if d.get('@type')=='FAQPage': print('schema:',len(d['mainEntity']))
PY
```
Expected: visible count == schema count, both ≥6.
- [ ] **Step 3: Commit** `git commit -am "feat(roys): expanded FAQ + FAQPage schema (PAA)"`

### Task 15: Newsletter (one) + Other Birds + final CTA

- [ ] **Step 1:** Add ONE newsletter placement AFTER the FAQ (use the existing `cag-newsletter` component idiom; must not visually outrank the inquiry/deposit CTA). Keep "Other African Greys we have available" grid + the single `<CTA>` "Ready to bring Roys home?".
- [ ] **Step 2:** `grep -ci "newsletter\|subscribe" dist/available/roys/index.html` → expected: exactly one placement (not 3).
- [ ] **Step 3: Commit** `git commit -am "feat(roys): one newsletter placement + other birds + CTA"`

### Task 16: Hero image — 5-element SEO + WebP <100KB

**Files:** the hero `<img>` + the image file under `public/`

- [ ] **Step 1:** Ensure 5 elements: SEO filename (`roys-congo-african-grey-male-4-months.webp`), alt ≤190, `title`, a visible caption+CTA, and a 250+ word description (in the section prose or a `<figure><figcaption>`). Hero keeps `loading="eager" fetchpriority="high"` + explicit `width`/`height`; add a BaseLayout `extraHeadHtml` preload for the hero webp.
- [ ] **Step 2:** Confirm the webp is real + <100KB (Pillow, not sips):

```bash
ls -l public/roys-congo-african-grey-male-4-months.webp
python3 - <<'PY'
from PIL import Image; im=Image.open('public/roys-congo-african-grey-male-4-months.webp'); print(im.format,im.size)
PY
```
If oversized, re-save `im.save(p,"WEBP",quality=82,method=6)`.
- [ ] **Step 3: Commit** `git commit -am "feat(roys): hero image 5-element SEO + webp"`

---

## Phase 5 — QA, approval, deploy

### Task 17: Heading hierarchy + keyword + word-count gate

- [ ] **Step 1: Check headings (Python — no zsh heading loops) + word count**

```bash
npx astro build
python3 - <<'PY'
import re,html
t=open('dist/available/roys/index.html').read()
for i in range(1,7):
    print(f"H{i}:",len(re.findall(rf'<h{i}\b',t)))
c=re.sub(r'<script[^>]*>.*?</script>|<style[^>]*>.*?</style>','',t,flags=re.S)
c=html.unescape(re.sub(r'<[^>]+>',' ',c)); print("words:",len(c.split()))
PY
```
Expected: exactly one H1; H2/H3 present; no level skipped (Rule 52); words ≥ Task 1 target. Primary keyword in H1, first 100 words, and ≥5 H2.
- [ ] **Step 2:** If a level is skipped, fix by demoting genuinely-nested headings (count demotable headings — don't force a skip). Re-run. **Commit** `git commit -am "fix(roys): heading hierarchy + keyword placement"`

### Task 18: a11y AA + performance + dist schema spot-check

- [ ] **Step 1:** Verify contrast tokens (small clay `#b04228`, clay buttons white-on-`#c8472f`, clay-on-green white), skip link/landmarks present (BaseLayout), no `<svg>` in CSS `content:`, interactive targets ≥24px, every `<img>` has dims. Run Lighthouse mobile warm median-of-3 via chrome-devtools; record scores in the session brief.
- [ ] **Step 2:** `grep -rl "&lt;svg" dist/available/roys/` → expected: empty (icons rendered, not escaped).
- [ ] **Step 3: Commit** any fixes `git commit -am "fix(roys): a11y AA + perf"`

### Task 19: GREEN — final page audit

- [ ] **Step 1:**

```bash
npx astro build
python3 scripts/final_page_audit.py --birds 2>&1 | tee /tmp/roys-green.txt
```
Expected: Roys = PASS (or PASS-WITH-WARNINGS with each WARN documented + justified). Compare to `/tmp/roys-red.txt`.
- [ ] **Step 2:** Update `sessions/2026-06-19-session-brief.md` status (Roys built, audit verdict). **Commit** `git commit -am "test(roys): final_page_audit GREEN + brief update"`

### Task 20: Preview → breeder approval gate (BLOCKING)

- [ ] **Step 1:** Start preview (`preview_start`), open `/available/roys/`, screenshot desktop + mobile (375px). Confirm heading sizes/fonts/text scale match the homepage. Share proof with the breeder.
- [ ] **Step 2:** **STOP. Do not proceed to siblings until the breeder says Roys is done/pass.** Log any requested changes to the session brief `## Open Flags` and address them (re-run Phase 4/5 for the affected section only).

### Task 21: Canonical + deploy + verify

- [ ] **Step 1:** Run `@cag-canonical-fixer` (absolute canonical/og:url/JSON-LD url). `npx astro build` clean.
- [ ] **Step 2:** Push (= deploy) and regenerate sitemaps:

```bash
git push origin main
python3 scripts/generate_sitemaps.py
git add -A && git commit -m "chore(roys): regenerate sitemaps" && git push origin main
git log origin/main..HEAD   # expected: empty
```
- [ ] **Step 3:** `@cag-deploy-verifier` (200 check + canonical audit + IndexNow). Confirm `https://congoafricangreys.com/available/roys/` returns 200 with the new content.

---

## Phase 6 — Batch-apply (after Roys approved)

### Task 22: Apply the locked pattern to the other five

- [ ] **Step 1:** For each of Amie (BAB) · Bery (PAS) · Jins & Jeni (PDB) · Elad (EBP, **male/first-grey**) · Evie (QAB, **female/value**): repeat Tasks 1, 3, 5–19 using that bird's primary/theme/framework/H-structure/snippet/PAA/schema from research doc Pages 2–6 + the spec §2 splits. Jins & Jeni: single `Product` representing the pair (NOT AggregateOffer), companion-vs-foundation section, never promise breeding, 2× documentation.
- [ ] **Step 2:** Re-run the cross-page cannibalization check (spec §2) after all six exist — confirm Elad≠Evie, and no bird claims a bare head term or a geo term.
- [ ] **Step 3:** Final: `npx astro build` → `python3 scripts/final_page_audit.py --birds` (all PASS) → `python3 scripts/generate_sitemaps.py` → push → deploy-verify all six 200.

---

## Self-review notes (spec coverage)

- Spec §0 overrides → Tasks 1/5 (depth+1500), 12 (logistics), 15 (one newsletter), 8/9/13 (no-geo via link-out). ✓
- Spec §2 cannibalization firewall → Tasks 2, 22 step 2 (incl. Elad/Evie split). ✓
- Spec §3 sections → Tasks 7 (snapshot), 10 (counter-pos), 12 (shipping), 15 (newsletter), all mandatory in 6–16. ✓
- Spec §4 blended frameworks → Tasks 8 (AIDA+EBP), 9 (EBP), 10 (PAS/PDB), 14 (QAB), 7 (BLUF). ✓
- Spec §5 word method → Task 1. ✓
- Spec §6 standards (meta/links/image/schema/a11y/perf/voice/compliance) → Tasks 4, 6, 7, 16, 17, 18. ✓
- Spec §8 definition of done → Tasks 17–21 gates. ✓

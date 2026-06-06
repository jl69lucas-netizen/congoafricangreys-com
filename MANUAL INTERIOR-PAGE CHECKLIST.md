# MANUAL INTERIOR-PAGE CHECKLIST — CongoAfricanGreys.com

> Copy-paste, **verify-each-step** build guide for every informational/secondary page,
> built to the SAME design + SEO standard as the homepage. **Hero → CTA.**
> Companion to `MANUAL SEO CHECKLIST-HOMEPAGE.md` (homepage-specific) and
> `skills/cag-seo-master-checklist.md` (the machine workflow).
> **Source:** distilled from the 13 homepage build sessions (2026-05-28 → 2026-06-06). See the
> plan `sessions/2026-06-06-interior-page-standard-PLAN.md` for the evidence map.

## APPLIES TO
health · shipping · FAQ · privacy policy · care/resource · about · why-choose-cag ·
scam guide · CITES-doc · health-guarantee · pros-and-cons · trusted-breeders · reviews
— any informational/secondary page.

## DOES NOT APPLY TO (these have their own structure)
comparison pages · location/state/city pages · all "…for-sale" money pages · blog posts.

## HOW TO USE
Each `⬜` is one verifiable step — do them top to bottom and tick each. **Never skip a `⛔ GATE`.**
The manual mirrors the page itself: **Part C is the build order, Hero first, CTA last.**

---

## TABLE OF CONTENTS
- **PART A** — Pre-Build (read-first + Outline Gate)
- **PART B** — Design-System Contract (how it looks)
- **PART C** — Section Build Order (Hero → CTA) + the Seam-Logo Divider
- **PART D** — Voice · Two-Keyword Headers · "Honesty Policy" Humor
- **PART E** — Entity 4-Move Loop + Verified-Claim Ledger
- **PART F** — Internal + External Links (woven mid-sentence)
- **PART G** — Non-Commodity Pass (audit-then-rewrite)
- **PART H** — GEO / AEO (be the cited source)
- **PART I** — Schema Set per page
- **PART J** — Meta titles/descriptions + Image SEO (5-element)
- **PART K** — Technical Hardening (a11y AA + performance)
- **PART L** — Deploy + Verify
- **PART M** — Gotchas (don't repeat these)
- **PART N** — Final QA Gate (15-point)

---

## PART A — PRE-BUILD (read-first + Outline Gate)

**Read first (binding — do not build without these):**
- ⬜ `PRODUCT.md` (strategic: register, users, brand personality, a11y bar) + `DESIGN.md` (visual: palette, type, components).
- ⬜ `docs/design.md` (master design spec) + `skills/cag-direction-d-theme.md` (live theme).
- ⬜ `docs/reference/seo-rules.md` (62 rules — especially the heading band) + `docs/reference/components.md` (24 components) + `docs/reference/page-width.md`.
- ⬜ Data the page touches: `data/price-matrix.json`, `data/financial-entities.json`, `data/clutch-inventory.json` — **never hardcode prices/shipping**, read them.

**⛔ GATE 1 — Outline first (Rule 51). Do NOT write any section until the user approves:**
- ⬜ **A. H1–H6 heading tree** — all sections with heading levels. No level skipping.
- ⬜ **B. Keyword-distribution table** — per section: primary KW, LSI, longtail, NLP/conversational, comparison KW, word count, rolling total vs target.
- ⬜ **C. Competitor snapshot** — top 5 for the page's primary term: their H2 topics, word count, special elements, what they MISS that C.A.Gs exploits.
- ⬜ **D. Special-elements plan** — counter snippet, FAQ, TOC, trust bar, CTA/contact form, schema set.
- ⬜ **E. Fan-out keywords** — branded, transactional, informational, comparison, NLP, voice.
- ⬜ Present the outline → **STOP** for "Approved" / changes.

**Confidence Gate (every section):**
- ⬜ ≥97% confidence before writing any file in `src/pages/<slug>/`. If it drops mid-build: run the **Clarification Checkpoint** — (1) write finished work to disk + log the open question to the live session brief's `## Open Flags`; (2) ask the user ONE narrow question (mark Recommended + why); (3) keep building every unblocked part. Never dead-stop the whole job.

---

## PART B — DESIGN-SYSTEM CONTRACT (how it looks)

> Direction D "Modern Editorial" is **global** via `body.theme-d` (`src/styles/direction-d.css`). Build normal design-system markup — **do NOT re-implement the theme per page.**

**Colors (3 anchors only):**
- ⬜ Forest Green `#2D6A4F` (nav/headers) · Clay `#e8604c` (all CTAs) · Cream `#faf7f4` (page surface). `--gold` MUST equal `--clay`.
- ⬜ **AA variants (do NOT revert):** solid clay **button fill** → `#c8472f` (via global `.bg-clay`, white text 4.78:1) · small clay **readable text on light** (links/eyebrows/prices) → `#b04228` (4.5:1+) · clay **on dark/green** stays bright `#e8604c` / tint `#f08070`.

**Type (Direction D):**
- ⬜ **Newsreader** serif for ALL H1–H6 · **IBM Plex Sans** for body/labels/buttons — applied globally. Keep `font-lora` / `font-sora` utility classes in markup; the theme restyles them.
- ⬜ **NEVER hard-code `font-family`** on elements to fight the theme.
- ⬜ **Option-A fluid clamp:** section H2/H3 carry **NO** size utilities (`text-3xl` etc.) — the `@layer base` clamp sizes them. Exceptions keep explicit sizing: hero H1, FAQ accordion H3 (`text-[16px]`), calculator output number.

**Buttons / Cards / Shadows / Motion:**
- ⬜ Primary CTA = clay pill, `border-radius:50px` (brand signature). Form submit buttons = `border-radius:12px`.
- ⬜ Cards: `<article>` → 20px radius, 1px `--border`, warm shadow, white surface; info cards = green header band.
- ⬜ Shadows always warm `rgba(60,30,10,…)` — never neutral grey.
- ⬜ Motion ≤0.2s. No bounce, parallax, or autoplaying video.
- ⬜ **No `user-select:none`** (anti-copy) ever.

**Icons:**
- ⬜ Line-icon SVGs (`width/height="1em"`, `stroke="currentColor"`), NOT emoji. KEEP only text glyphs ✔ ✗ ★. ✅ → green `#2D6A4F` check-circle.
- ⬜ **African Grey bird: NEVER 🦜.** Use `/emoji/cag-congo.png` (Congo) or `/emoji/cag-timneh.png` (Timneh); text contexts use `[CAG]`/`[TAG]`.
- ⬜ A data-array icon rendered via `{x.icon}` must use `set:html`; then confirm `grep -rl "&lt;svg" dist/` is empty.
- ⬜ **NEVER put `<svg>` in CSS `content:`** (`::before{content:'<svg…>'}` dumps raw markup). Put inline `<svg>` in the markup.

**Widths:**
- ⬜ Outer shell `.container` `max-width:1200px`. Informational inner text wrapper `.container-text` `max-width:760px`. Every `<p>` `max-width:70ch`.
- ⬜ Infographics: **760px** wrapper (informational/care/article), 400px desktop height (auto on mobile). Never 900px/`max-w-4xl`.

---

## PART C — SECTION BUILD ORDER (Hero → CTA)

> Interior pages reuse the homepage spine. Build top-to-bottom, **preview each section at `localhost:4321`, get approval, then move on.**

**C.1 — Mandatory spine (in order):**
1. ⬜ **HERO** (`HeroV3`-style or `cag-split-hero`) — page-specific **H1**, clay eyebrow, lead subhead, dual CTA (form links only — **no phone number in body**). Optional bird/owner image. Hero H1 keeps explicit size (`text-3xl sm:text-4xl md:text-[3.25rem]`).
2. ⬜ **COUNTER SNIPPET** (`CounterSnippet`) — 4 liftable stats (e.g. `12+ Yrs · 100% CITES · $1,500 Floor · 24h`). Rule 31. Use neutral `<div>`s, not `<dl>` (Part K).
3. ⬜ **KEY TAKEAWAY / BLUF** (`KeyTakeawayV2`) — a declarative ≤320-char answer to the page's core question (AEO bait, Part H).
4. ⬜ **TOC** (`TocV3`) — **required when page >1,500 words** (Rule 29); grouped by part.
5–N. ⬜ **BODY SECTIONS** — topic-specific. Each one: conversational H2 (Part D), EBP opening paragraph, woven links (Part F), 4-move entity loop (Part E), a declarative answer block (Part H).
   - ⬜ **Trust bar / stats** (`TrustStats`) wherever credibility matters (health, why-choose, scam).
   - ⬜ **FAQ** (`FaqAccordion`) — PAA-sourced; **FAQPage schema required** (Part I).
   - ⬜ **How-to / Next-Step** — numbered green-circle steps where there's transactional intent; `HowTo` schema.
6. ⬜ **FINAL CTA + CONTACT** (`ContactForm:application`) — the **LAST** content section. Conversational H2 ("Ready to Inquire About a C.A.Gs African Grey — What Should You Tell Us?"). Optional `LocalBusiness` map.

**Interior-page deltas vs homepage:**
- ⬜ **DROP** sections owned by money/comparison pages: product/bird grid, breeding-pairs, full compare-table. (Link out to those pages instead.)
- ⬜ **KEEP** hero, counter, key-takeaway, TOC (if long), at least one trust element, FAQ, CTA.
- ⬜ **ADD `BreadcrumbList` schema** — interior pages get it (the homepage intentionally omits it).
- ⬜ One CTA per page (BaseLayout global band is gated by `hideGlobalCta`; if the page has its own `<CTA>`, pass `hideGlobalCta`).

**C.2 — The Section Seam Divider (the small footer logo between sections):**
- ⬜ Place at **4–8 editorial seams** (not after every section). Markup (verbatim from `src/pages/index.astro:377`):
```html
<div class="cag-seam" aria-hidden="true">
  <span class="cag-seam__line"></span>
  <img src="/cag-footer-logo.png" alt="" width="200" height="66" loading="lazy" />
  <span class="cag-seam__line"></span>
</div>
```
- ⬜ CSS (scope `.home-d` → your page's own wrapper class on interior pages):
```css
.home-d > .cag-seam{ display:flex; align-items:center; gap:26px; max-width:1100px; margin:0 auto; padding:.6rem 24px !important; border-top:0 !important; }
.home-d > .cag-seam + *{ border-top:0 !important; }
.cag-seam__line{ flex:1; height:1px; background:var(--rule); }
.cag-seam img{ height:30px; width:auto; display:block; opacity:.92; flex-shrink:0; }
@media (max-width:600px){ .home-d > .cag-seam{ gap:16px; } .cag-seam img{ height:24px; } }
```
- ⬜ Rules: `alt=""` (decorative) · `loading="lazy"` · explicit `width/height` (CLS) · the seam removes its own + the next section's `border-top` so the logo-rule is the only divider there.

---

## PART D — VOICE · HEADERS · HUMOR

**D.1 — First-Person Brand Voice (every section):**
- ⬜ Write as the breeder: **"we / us / our / here at C.A.Gs."**
  - ✅ "Here at C.A.Gs, **our** Congo and Timneh Greys…" · "**we** hand-raise every chick" · "**our** PCR DNA-sexing".
  - ❌ "Both make exceptional companions" · "African Greys are…" (when the sentence is about *our* offering).
- ⬜ **Exceptions (stay encyclopedic):** taxonomy/species facts (`Psittacus erithacus` is native to West & Central Africa), cited research, outbound-authority facts.
- ⬜ First-person never means overclaiming — bounded by the Verified-Claim Ledger (Part E).

**D.2 — Two-Keyword Conversational Headers (Rule 28b) + full H1–H6:**
- ⬜ Every header is conversational / Quora-style: **What / How / Is / Can / Who.**
- ⬜ **Two-keyword method:** secondary keyword + LSI/NLP/entity in each H2.
- ⬜ Use **ALL of H1–H6.** Band (seo-rules): H1×1 · H2 25–35 · H3 40–50 · H4 10–20 · H5 5–10 · H6 3–8. Scale proportionally for a short page, but keep ≥1 each of H1–H4 and use H5/H6 where depth genuinely exists.
- ⬜ **No level skipping** (Rule 52). Sibling grids share ONE level — only demote *genuinely-nested* headings.
- ⬜ Live examples: "What Is a Congo African Grey — the Classic Red-Tailed Talker?" · "How Does C.A.Gs Ship African Grey Parrots Safely to All 50 States?"

**D.3 — Humor: the "Honesty Policy" (Style-2):**
- ⬜ Tone: dry, transparent, anti-hype — turns honesty into a selling point and disarms scam-wary buyers.
- ⬜ Live examples (`index.astro:599`): *"Honestly, the 'better' sex is the one whose personality fits your home…"* and the pricing note *"a sub-$1,500 'African Grey' is a wild-caught bird, a sick bird, or no bird at all."*
- ⬜ Rules: humor **never fabricates**, never undermines CITES-safety, **≤1 light beat per section**, never on legal/health claims.

---

## PART E — ENTITY 4-MOVE LOOP + VERIFIED-CLAIM LEDGER

**E.1 — The 4-Move Loop (required to build/improve ANY section):**
1. ⬜ **Structural Critique** — read the live section; name what is entity-thin / narrative-only.
2. ⬜ **Recommended Entities + WHY** — each grounded (Knowledge-Graph authority · PAA/voice demand · competitor gap · buyer intent). (Recommend+Why rule.)
3. ⬜ **Optimized Draft** — embed entities in copy grounded ONLY in the ledger; ≥97% confidence; CITES-safe.
4. ⬜ **Topical-Cluster Strategy** — internal-link anchors + schema feeding the hub-and-spoke. **Extend existing JSON-LD, never duplicate;** FAQ schema must be visible; verify in `dist/`.

**E.2 — Verified-Claim Ledger (what you ARE allowed to assert):**
- ⬜ ✅ PCR-based DNA sexing · PBFD screening · Polyomavirus (APV) screening · board-certified avian veterinarian · 3-day written health guarantee · CITES Appendix I captive-bred · USDA AWA license · hatch certificate + closed band · shipping **$185 airport / $350 home** (Delta/United/American cargo) · flight-nanny **from $750** (quoted per route) · chlamydiosis/psittacosis screening · UV-B lighting + vitamin D3 · named talking Congo **"Maxy"** (homepage video).
- ⬜ ❌ Do **NOT** assert: incubation temps for the egg product, or anything not on this list, **without breeder re-confirmation.**
- ⬜ The ledger of record is `.claude/agents/cag-entity-incorporation-agent.md` + `sessions/2026-06-03-homepage-entity-map.md` — update THERE when the breeder confirms a new claim, then mirror here.

---

## PART F — INTERNAL + EXTERNAL LINKS (woven mid-sentence)

- ⬜ **Placement:** beginning or middle of a sentence — **NEVER at the end.**
- ⬜ Internal links open **same tab**; external open **new tab** + `rel="noopener noreferrer"` + an ↗ affordance.
- ⬜ **Cap:** max 2 external / 300 words, max 1 / paragraph. Verify **200** before inserting (retry `-A "Mozilla/5.0"` — `cites.org` 403s to curl ≠ dead). Add any new URL to `docs/reference/external-link-library.md` first.
- ⬜ Proven authority targets: World Parrot Trust (`parrots.org/encyclopedia/grey-parrot/`), IUCN Red List, CITES.org, USDA APHIS, Alex Foundation, AAV (`aav.org`), Cornell/AllAboutBirds.
- ⬜ Internal cluster targets: `/african-grey-parrot-price/` · `/congo-african-grey-for-sale/` · `/timneh-african-grey-for-sale/` · `/how-to-avoid-african-grey-parrot-scams/` · `/african-grey-parrot-care-guide/` · `/best-african-grey-parrot-food/` · `/buy-african-grey-parrot-near-me/` · `/contact-us/` + relevant location pages.
- ⬜ Jump-link teaser → deep-dive (`#anchor`) is allowed for on-page navigation.

---

## PART G — NON-COMMODITY PASS (audit-then-rewrite)

- ⬜ **Method:** audit ALL sections → classify each **STRONG / SHARPEN / REBUILD** → rewrite **only the weak**. Do NOT rewrite strong/indexed copy (ranking-regression risk).
- ⬜ **Ledger-only** — no fabrication. Anything you'd want but can't confirm becomes a **GAP-FLAG** (a prompt for Mark & Teri), never an invented claim.
- ⬜ Kill generic filler ("both make exceptional companions") → replace with a **specific first-person breeder detail** (e.g. Teri's real week-1 quiet-Congo story).
- ⬜ Target one piece of **high-resolution detail per ~500 words** that a generic LLM could not write.

---

## PART H — GEO / AEO (be the cited source)

- ⬜ **Declarative answer block:** every H2 question is followed by a **≤320-char self-contained factual answer** that can be lifted into an AI Overview / featured snippet.
- ⬜ **Stat-forward liftable facts:** "40–60 year lifespan", "100–1,000 word vocabulary", "Appendix I since Jan 2017", "$185 airport / $350 home".
- ⬜ **Entity corroboration triangle:** `sameAs` + Person/Organization schema + outbound authority links.
- ⬜ **Freshness:** a visible "Updated [Month Year]" + `dateModified` in schema.
- ⬜ **Bing/DuckDuckGo/Yahoo run on Bing's index** → IndexNow covers them (key → `api.indexnow.org`; Bing/Yandex, not Google). Run it on deploy (Part L).

---

## PART I — SCHEMA SET (per interior page)

- ⬜ **Always:** `Organization` (name = **"Congo African Greys"**, canonical per `credentials.md`) · `WebPage` · **`BreadcrumbList`** (interior pages get it — homepage omits it).
- ⬜ FAQ section present → **`FAQPage`** generated from the actual `<details>`; **ONE** block; confirm not duplicated in `dist/`.
- ⬜ Numbered steps present → **`HowTo`**.
- ⬜ Pricing present → **`Product` / `Offer`** (price, availability, CITES doc).
- ⬜ Local/contact present → **`LocalBusiness`** (`geo` + `areaServed`).
- ⬜ **Extend** existing JSON-LD, never duplicate. **Verify rendered in `dist/`** (`<Schema>` components generate it — source greps lie). `grep -rl "&lt;svg" dist/` must be empty.

---

## PART J — META + IMAGE SEO

**J.1 — Meta titles/descriptions (4-tone system):**
- ⬜ Canonical C.A.Gs long format, choose tone by page: **Urgency · Comparison · Transactional · Trust/Health.**
- ⬜ Title ≤205 chars · Description ≤185 (F1) or ≤300 (F2). **Never** generic-short. **No duplicates** vs other pages (audit first).
- ⬜ Pattern: `Primary Keyword | Conversational | Comparison/LSI/NLP | C.A.Gs – Midland, TX | Trust Ending`.

**J.2 — Image SEO (5-element — none optional):**
- ⬜ (1) SEO filename · (2) alt ≤190 chars · (3) `title` · (4) caption + CTA · (5) 250+ word description.
- ⬜ `loading="lazy"` + explicit `width`/`height` (CLS). LCP/hero image is the exception → `fetchpriority="high"` + preload (Part K).
- ⬜ WebP via **Python Pillow** (`im.save(p,"WEBP",quality=82,method=6)`) — **`sips` writes fake WebP** (JPEG-in-`.webp`, often larger).

---

## PART K — TECHNICAL HARDENING (a11y AA + performance)

**K.1 — Accessibility (WCAG 2.1 AA):**
- ⬜ Skip link · ARIA landmarks · form labels · visible focus states · descriptive link text (no bare "More"/"Click here") · correct heading order (no skips).
- ⬜ Contrast: small clay on light = `#b04228`; clay buttons = white text on `#c8472f`; clay on green = white.
- ⬜ Use `<dl>/<dt>/<dd>` **only** for genuine term→definition **and** `<dt>` before `<dd>`. Stat grids = neutral `<div>` (axe: "dl's do not contain only properly-ordered dt/dd").
- ⬜ **NEVER** `<svg>` in CSS `content:` — inject inline `<svg stroke="currentColor">` in the markup (the trust-bar `::before` trap that produced "Hand-Fed from Week 212–16 Week…").
- ⬜ Interactive target-size ≥24px (WCAG 2.5.8).

**K.2 — Performance (Astro; Lighthouse mobile, warm median-of-3):**
- ⬜ Remove ClientRouter/View-Transitions JS **only if** `grep -rn "transition:animate|transition:persist|astro:page-load|astro:after-swap"` returns 0.
- ⬜ Merge multiple Google-Fonts `css2?family=` into ONE request, load non-blocking (`media="print" onload="this.media='all'"` + `<noscript>` fallback). Don't duplicate font CSS/preconnects that BaseLayout already loads in `<head>`.
- ⬜ Preload the LCP hero via BaseLayout `extraHeadHtml`: `<link rel="preload" as="image" href="…hero.webp" fetchpriority="high" type="image/webp">`.
- ⬜ Defer `gtag` to first-interaction/idle. Give every `<img>` explicit dims (CLS).
- ⬜ **CSP source of truth = `site/content/_headers`** (deploy copies it to `public/`); GA4 needs `connect-src … https://*.google-analytics.com` (wildcard — regional endpoints).
- ⬜ **USER ACTION (not a code fix):** the `/70de/` ~71 KB unused JS is **Cloudflare Rocket Loader** — disable in Cloudflare → Speed → Optimization.
- ⬜ Report Lighthouse as **warm median-of-3** (single cold runs lie).

---

## PART L — DEPLOY + VERIFY

- ⬜ Output path: `src/pages/<slug>/index.html` or `index.astro` (**NOT** `site/content/` — that is staging only; `src/pages/` is deployed).
- ⬜ `@cag-canonical-fixer` (absolute canonical/og:url/JSON-LD url).
- ⬜ `npx astro build` clean → spot-check the page + schema in `dist/`.
- ⬜ `git add` + commit + **`git push`** (push = deploy → GitHub Actions → Cloudflare Pages).
- ⬜ `python3 scripts/generate_sitemaps.py` (run after adding ANY page). Caveat: `deploy.yml` copies `site/content/*.xml` over `public/` — the generator must `write_both`.
- ⬜ `@cag-deploy-verifier` (200 checks + canonical audit + **IndexNow** submission) → `sitemap-agent`.
- ⬜ Confirm pushed: `git log origin/main..HEAD` should be empty.

---

## PART M — GOTCHAS (don't repeat these — from the homepage logs)

- ⬜ **Verify schema/SEO in `dist/` (rendered), NOT source greps** — `<Schema>` components hide it from source.
- ⬜ **Count demotable headings BEFORE quoting an H-count target** — sibling-grids + shared components limit what you can demote without skipping levels.
- ⬜ `preview_screenshot` resets scroll to 0 → hide DOM above the target + `scrollTo(0,0)`. `navigate` resets the viewport → **resize before measuring**. Use `getComputedStyle`, not screenshots, to verify CSS.
- ⬜ `grep -oF` for literals containing `$` (`$` = end-of-line anchor; `grep -o "from \$750"` matches nothing).
- ⬜ "Everything up-to-date" ≠ failure — the auto-push hook may have already pushed; check `git log origin/main..HEAD`.
- ⬜ Measure full inventory/scope before quoting; **script** many-file edits (idempotent).
- ⬜ zsh chokes on `for h in 1..6` heading loops — **use Python** for heading/markup counts. The preview sandbox can't render external iframes (Google Maps blank) — verify embeds by geometry/computed style.

---

## PART N — FINAL QA GATE (15-point)

> ⛔ The page is not "done" until these pass. (Mirrors `skills/cag-seo-master-checklist.md` Step 15; scale word/entity/FAQ counts down for a focused interior page, but keep every structural + technical item.)

**Content completeness:**
- ⬜ All outlined sections present; word count meets the page's target (competitor +1,000 for pillar topics; proportionate for narrow ones).
- ⬜ Named entities naturally integrated (people, locations, medical, credentials, stats) — ledger-bounded.
- ⬜ A declarative ≤320-char answer block under each H2.

**Linking quality:**
- ⬜ Contextual internal links (beginning/middle of sentence, varied anchors); all targets verified to exist.
- ⬜ External authority links (.gov/.edu/.org) verified 200; in `external-link-library.md`.
- ⬜ TOC (if >1,500 words) with working jump links.

**Search-engine alignment:**
- ⬜ Primary keyword in H1, first 100 words, and ≥5 H2.
- ⬜ All six heading levels present and sequential (no skips).
- ⬜ CITES Appendix I + captive-bred + USDA AWA in first 300 words (Rule 44).
- ⬜ 40–60 year lifespan referenced at least once (Rule 46).
- ⬜ Voice-search questions in H2/H3 (and H6 sub-questions).

**Conversion + technical:**
- ⬜ First-person C.A.Gs voice throughout; "Honesty Policy" beat where it fits; no generic AI copy.
- ⬜ Form CTA present; **NO phone number in body** (Rule 61).
- ⬜ Buyer fears addressed (scam, sick bird, CITES gaps, wild-caught suspicion — Rule 47).
- ⬜ Images = 5-element SEO + explicit dims + lazy (LCP hero excepted).
- ⬜ Schema present + correct per Part I; canonical absolute; verified in `dist/`.
- ⬜ a11y AA + performance (warm median-of-3) gates from Part K pass.

---

*End of manual. Build the next interior page top-to-bottom against this file; tick every `⬜` and never skip a `⛔ GATE`.*

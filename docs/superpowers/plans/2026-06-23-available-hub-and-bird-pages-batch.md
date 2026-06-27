# Available Hub + 5 Bird Pages Polish Batch — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring the `/available/` hub and the 5 remaining bird pages (roys, amie, elad, evie, jins-jeni) to the homepage standard — fix type-scale, correct the Jins & Jeni "bonded" mislabel, add a CITES-safe breeding-pair/fertile-eggs link section, de-duplicate the pricing-card image, run a first-person + anti-AI de-templating pass, wire `/available/` into site navigation, and clear the Lighthouse perf flags.

**Architecture:** Static Astro site. All page edits go to `src/pages/<slug>/index.astro` (deployed). Direction-D theme (`body.theme-d`) controls global typography via a fluid clamp; the fix is to *remove* hard-coded Tailwind size classes so headers inherit the clamp. Verification is `npx astro build` + `python3 scripts/final_page_audit.py --birds` + dist greps + preview-verify + warm Lighthouse median-of-3. Work directly on `main`; commit + push after each task (push = deploy).

**Tech Stack:** Astro, Tailwind (utility classes), Direction-D CSS theme, Pillow 11.3.0 (image resize), Cloudflare Pages (deploy), Cloudflare dashboard (Rocket Loader toggle).

**Decisions locked with the breeder (2026-06-23):**
- Hub slug stays `/available/` (no redirect — keyword already in title/H1/content; renaming would break the parent/child URL structure with the 6 bird pages). Push the keyword via internal-link anchor text instead.
- Breeding-pair + fertile-eggs is a **link/promo section** to the EXISTING pages `/african-grey-breeding-pair-for-sale/` ($3,000 bonded pair) and `/african-grey-parrot-bird-eggs-for-sale-usa/` — not a new from-scratch listing. No fabricated bird/egg data.
- Jins & Jeni are an **unrelated companion pair sold together**, NOT a bonded/breeding pair. The bonded pair is the separate `/african-grey-breeding-pair-for-sale/` bird.

**Pre-flight (run once before Task 1):**
```bash
cd /Users/apple/Downloads/CAG && git checkout main && git pull --ff-only && git status
```

---

## Task 1: Correct the Jins & Jeni "bonded" mislabel (unrelated companion pair)

**Rule:** Replace "bonded pair" / "bonded Congo pair" framing (which implies a mated/breeding bond) with "companion pair sold together" / "hand-raised pair" wording. DO NOT touch instances where "bonded" describes bonding *with people/family* (e.g. "deeply-bonded grey," "bonded with our family in days") — those are correct and stay.

**Files:**
- Modify: `src/pages/available/index.astro` (hub: card blurb line 16, FAQ lines 50-51, pricing line 285, compare row line 31)
- Modify: `src/pages/available/jins-jeni/index.astro` (title 10, description 11, schema 15-16, ToC 70-71/78/81, vitals 102/108, hero 197, video aria 263, body 286, headings 352/384, figure 360-367)

- [ ] **Step 1: Hub — fix the Jins & Jeni card blurb (index.astro:16)**

Change the `blurb`:
```
blurb: "A bonded, talking Congo pair — placed together, never split."
```
to:
```
blurb: "A hand-raised, talking Congo pair — sold together so neither is alone."
```

- [ ] **Step 2: Hub — fix compare row (index.astro:31)**

Change `"Bonded, talking"` → `"Talking, sold as a pair"`.

- [ ] **Step 3: Hub — fix FAQ + pricing references (index.astro:50, 51, 285)**

- Line 50: `the bonded Jins & Jeni pair` → `the Jins & Jeni companion pair`
- Line 51: `the bonded Jins & Jeni pair is $3,500 because they are placed together` → `the Jins & Jeni companion pair is $3,500 because they are placed together`
- Line 285: `The bonded <a ...>Jins &amp; Jeni</a> pair is $3,500` → `The <a ...>Jins &amp; Jeni</a> companion pair is $3,500`

- [ ] **Step 4: Jins & Jeni page — title / meta / schema (jins-jeni/index.astro:10, 11, 15, 16, 43)**

Replace "Bonded Congo Pair" / "bonded Congo African Grey pair" / "bonded pair of hand-raised" with "Companion Congo Pair" / "hand-raised Congo African Grey companion pair" / "hand-raised pair of Congo African Greys". Keep the factual core (DNA-sexed, sold together, $3,500). Example title:
```
const title = "Companion Congo Pair for Sale | Jins (male) & Jeni (female) — DNA-Sexed Pair, CITES Appendix I Captive-Bred, $3,500 | C.A.Gs – Midland, TX";
```

- [ ] **Step 5: Jins & Jeni page — ToC, vitals, hero, body, figure (jins-jeni/index.astro:70-71, 78, 81, 102, 108, 197, 263, 286, 352, 360, 361, 367, 384)**

For each, swap the *pair-relationship* "bonded" → "companion"/"hand-raised pair". Add ONE honest clarifying sentence in the body (around line 286) so the distinction is explicit and de-duplicated from the breeding pair:
```
Jins and Jeni are not a breeding pair — they are two unrelated, hand-raised Congo African Greys we placed together so neither grows up alone. (If you are looking for a proven breeding pair, see our <a href="/african-grey-breeding-pair-for-sale/" class="text-clay-text underline">African Grey breeding pair</a>.)
```

- [ ] **Step 6: Verify no stray pair-bond "bonded" remains; human-bond ones intact**

Run:
```bash
cd /Users/apple/Downloads/CAG && grep -n "bonded" src/pages/available/jins-jeni/index.astro src/pages/available/index.astro
```
Expected: remaining hits are only human/family-bonding phrasing ("deeply-bonded grey," "bonded with our family"). No "bonded pair"/"bonded Congo pair" describing Jins & Jeni.

- [ ] **Step 7: Build + commit**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
git add src/pages/available/index.astro src/pages/available/jins-jeni/index.astro
git commit -m "fix(available): reframe Jins & Jeni as companion pair (not bonded/breeding)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

---

## Task 2: Add "Breeding pairs & fertile eggs" link section to the hub

**Heading-Outline Gate (CLAUDE.md):** This adds one H2 + two H3s. Present this outline to the breeder for approval BEFORE writing (no skipped levels; hub already meets the 5×H5 / 5×H6 minimums elsewhere):
- H2: `Want a breeding pair or fertile African Grey eggs?`
  - H3: `Proven African Grey breeding pairs` → `/african-grey-breeding-pair-for-sale/`
  - H3: `Fertile African Grey eggs for hatching` → `/african-grey-parrot-bird-eggs-for-sale-usa/`

**CITES safety:** Frame strictly as captive-bred, USDA AWA, domestic transfer with documentation. No wild-caught implication. Note buyer needs incubation capability for eggs. Keyword variants to include: "breeding African grey pair for sale," "proven African grey pair," "African grey fertile eggs for sale," "African grey parrot eggs for hatching," "candled / fertile parrot eggs."

**Files:**
- Modify: `src/pages/available/index.astro` (insert section after the PRICING section, before RESERVE PROCESS — i.e. after line 295)

- [ ] **Step 1: Insert the section HTML after the Pricing section (after index.astro:295)**

```html
  {/* ── BREEDING PAIRS & EGGS ── */}
  <section id="breeding" class="py-16 px-4">
    <div class="max-w-5xl mx-auto" style="max-width:1100px;">
      <div class="mb-7 border-l-4 border-green pl-4">
        <p class="font-sora text-xs font-semibold uppercase tracking-widest text-clay mb-2">Beyond single companions</p>
        <h2 class="font-lora font-bold text-logo-dark">Want a breeding pair or fertile African Grey eggs?</h2>
        <p class="font-sora text-stone-600 mt-2 text-sm leading-relaxed" style="max-width:70ch;">Some buyers want more than one companion bird. Alongside our hand-raised greys, we occasionally place a proven, DNA-sexed breeding pair, and fertile African Grey eggs for experienced hobbyists with their own incubator. Everything is captive-bred in the USA at our USDA AWA licensed aviary and transferred with full CITES Appendix I documentation.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <a href="/african-grey-breeding-pair-for-sale/" class="group flex flex-col overflow-hidden rounded-2xl border border-stone-200 bg-white transition-colors hover:border-green/40" style="box-shadow:0 4px 20px rgba(60,30,10,0.06);">
          <div class="aspect-[16/9] overflow-hidden bg-cream"><img src="/congo-african-grey-breeding-pair-aviary.webp" alt="A proven Congo African Grey breeding pair in the C.A.Gs aviary, captive-bred and DNA-sexed" width="560" height="315" loading="lazy" class="w-full h-full object-cover object-center transition-transform duration-200 group-hover:scale-[1.03]" /></div>
          <div class="p-6 flex flex-col flex-1">
            <h3 class="font-lora font-semibold text-lg text-logo-dark mb-1.5">Proven African Grey breeding pairs</h3>
            <p class="font-sora text-stone-600 text-sm leading-relaxed mb-3">A DNA-sexed, bonded breeding pair for serious aviculturists — distinct from a companion pair like Jins &amp; Jeni. Captive-bred, documented, and placed only with experienced homes.</p>
            <span class="font-sora text-sm font-semibold text-clay-text mt-auto group-hover:underline">See the breeding pair →</span>
          </div>
        </a>
        <a href="/african-grey-parrot-bird-eggs-for-sale-usa/" class="group flex flex-col overflow-hidden rounded-2xl border border-stone-200 bg-white transition-colors hover:border-green/40" style="box-shadow:0 4px 20px rgba(60,30,10,0.06);">
          <div class="aspect-[16/9] overflow-hidden bg-cream"><img src="/african-grey-eggs-ready-to-hatch.webp" alt="Fertile, candled African Grey parrot eggs ready to hatch, from captive-bred USDA AWA licensed stock" width="560" height="315" loading="lazy" class="w-full h-full object-cover object-center transition-transform duration-200 group-hover:scale-[1.03]" /></div>
          <div class="p-6 flex flex-col flex-1">
            <h3 class="font-lora font-semibold text-lg text-logo-dark mb-1.5">Fertile African Grey eggs for hatching</h3>
            <p class="font-sora text-stone-600 text-sm leading-relaxed mb-3">Fertile, candled African Grey parrot eggs for experienced hobbyists running their own incubator. Captive-bred USA stock, transferred with documentation — never wild-sourced.</p>
            <span class="font-sora text-sm font-semibold text-clay-text mt-auto group-hover:underline">See fertile eggs for sale →</span>
          </div>
        </a>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Confirm the two image files exist (else swap to a real file)**

```bash
cd /Users/apple/Downloads/CAG && ls -la public/congo-african-grey-breeding-pair-aviary.webp public/african-grey-eggs-ready-to-hatch.webp
```
Expected: both exist. If `congo-african-grey-breeding-pair-aviary.webp` is missing, use `public/congo-african-grey-pair-aviary-bred.webp`; for eggs fallback use `public/african-grey-candled-eggs.webp`.

- [ ] **Step 3: Build + verify section renders in dist**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
grep -c "Want a breeding pair or fertile" dist/available/index.html
```
Expected: build OK, count `1`.

- [ ] **Step 4: Commit + push**

```bash
cd /Users/apple/Downloads/CAG && git add src/pages/available/index.astro
git commit -m "feat(available): add breeding-pairs & fertile-eggs link section (CITES-safe)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

---

## Task 3: De-duplicate the hub "Pricing" resource-card image

**Problem:** The hub's Pricing care-card uses `/timneh-african-grey-breeding-pair.webp`, which is the same Levi & Rily image used on the Evie/Elad **parent cards**. Swap to a non-duplicated image.

**Files:**
- Modify: `src/pages/available/index.astro:44`

- [ ] **Step 1: Swap the image (index.astro:44)**

Change `img: "/timneh-african-grey-breeding-pair.webp"` →
`img: "/cags-tame-african-grey-parrot-with-owner-480.webp"` and update `imgAlt` to:
`"An African Grey with its owner — the relationship behind what a documented grey really costs"`.

- [ ] **Step 2: Verify the new image isn't already used elsewhere on the hub**

```bash
cd /Users/apple/Downloads/CAG && grep -c "cags-tame-african-grey-parrot-with-owner-480.webp" src/pages/available/index.astro && ls public/cags-tame-african-grey-parrot-with-owner-480.webp
```
Expected: count `1` (only the new use), file exists.

- [ ] **Step 3: Build + commit**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
git add src/pages/available/index.astro
git commit -m "fix(available): de-dupe pricing card image (was reused as parent card)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

---

## Task 4: Strip hard-coded type-scale overrides on the 5 bird pages

**Problem:** The 5 bird pages hard-code `text-3xl` (and some `md:text-4xl`) on every H2, overriding the Direction-D fluid clamp. The hub uses NO size class on H2 (`font-lora font-bold text-logo-dark`) and inherits the clamp — that's the proven pattern. Hero H1 on Elad/Evie is already fixed (`text-2xl sm:text-3xl`); leave H1 as-is.

**Files:**
- Modify: `src/pages/available/roys/index.astro`, `amie/index.astro`, `elad/index.astro`, `evie/index.astro`, `jins-jeni/index.astro`

- [ ] **Step 1: Inspect the exact size-class patterns on H2 across the 5 pages**

```bash
cd /Users/apple/Downloads/CAG
for f in roys amie elad evie jins-jeni; do echo "== $f =="; grep -on "h2 class=\"[^\"]*text-3xl[^\"]*\"" src/pages/available/$f/index.astro | head -3; done
```

- [ ] **Step 2: Strip `text-3xl` and `md:text-4xl` from H2s only (not H1) on all 5 pages**

Run the scoped sed (removes the two size tokens inside H2 class lists; collapses leftover double spaces):
```bash
cd /Users/apple/Downloads/CAG
for f in roys amie elad evie jins-jeni; do
  perl -0pi -e 's{(<h2 class="[^"]*?)\s*\bmd:text-4xl\b}{$1}g; s{(<h2 class="[^"]*?)\s*\btext-3xl\b}{$1}g; s{(<h2 class="[^"]*?)  +}{$1 }g' src/pages/available/$f/index.astro
done
```

- [ ] **Step 3: Verify no H2 retains text-3xl/md:text-4xl, and H1 untouched**

```bash
cd /Users/apple/Downloads/CAG
echo "H2 size-class remnants (expect 0):"; grep -c "h2 class=\"[^\"]*text-3xl\|h2 class=\"[^\"]*md:text-4xl" src/pages/available/{roys,amie,elad,evie,jins-jeni}/index.astro
echo "H1 still has sm:text-3xl (sanity):"; grep -c "sm:text-3xl" src/pages/available/evie/index.astro
```
Expected: all H2 counts `0`; Evie H1 count ≥1.

- [ ] **Step 4: Build + commit**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
git add src/pages/available/{roys,amie,elad,evie,jins-jeni}/index.astro
git commit -m "fix(birds): strip hard-coded H2 type-scale so headers inherit the global clamp

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

- [ ] **Step 5: Preview-verify header sizing on mobile + desktop**

Start preview, load one Congo (roys) and one Timneh (evie) bird page, and the jins-jeni pair page. Confirm H2s no longer overflow on a 375px viewport and match the hub/homepage rhythm. Capture a screenshot of one page at 375px and one at desktop as proof.

---

## Task 5: Card / section polish — bring bird pages to homepage standard

**Scope:** Only where a bird page diverges from the homepage/hub idiom. Reference baselines: Roys (Congo full-Roys standard) and the hub. Per project memory, watch: gallery uses `h-72` + per-image `object-position` (not `aspect-[4/5]`); doc/figure images use `w-full` (a `max-h` cap is the shrink bug); shipping image must be source-FIRST in markup for correct mobile order; per-bird `object-position` overrides.

**Files:**
- Modify: `src/pages/available/{roys,amie,elad,evie,jins-jeni}/index.astro` (only divergent sections)

- [ ] **Step 1: Diff each bird page's card/section idioms against Roys + hub**

```bash
cd /Users/apple/Downloads/CAG
for f in amie elad evie jins-jeni; do echo "== $f vs roys: gallery/figure idioms =="; grep -n "aspect-\[\|max-h-\|h-72\|object-position\|col-start" src/pages/available/$f/index.astro | head -20; done
```

- [ ] **Step 2: Fix divergences found** (apply only those that differ from Roys/hub):
  - Replace any gallery `aspect-[4/5]` with `h-72` + per-image `style="object-position:…"`.
  - Replace any `max-h-*` cap on doc/figure images with `w-full h-auto`.
  - Ensure the shipping-section image `<img>`/`<figure>` is the FIRST child in its grid so mobile order is image-then-text (col-start classes alone don't fix mobile order).
  - Confirm trust-badge / shipping-cost line matches the canonical: `Ships nationwide · $185 airport · $350 home`.

- [ ] **Step 3: Build + verify no broken images in dist**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
grep -rl "&lt;svg" dist/available/ ; echo "(empty = ok: no raw-escaped svg)"
```

- [ ] **Step 4: Preview-verify each of the 5 pages, then commit + push**

Load each page in preview, check console for errors, snapshot the gallery + shipping section. Then:
```bash
cd /Users/apple/Downloads/CAG && git add src/pages/available/{roys,amie,elad,evie,jins-jeni}/index.astro
git commit -m "fix(birds): align card/gallery/shipping idioms to homepage standard

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

---

## Task 6: First-person voice + anti-AI de-templating pass

**Why (the breeder's repeated-template concern):** The hub repeats the H3→H4→H5→H6 ladder ending in "Breeder note:" / "Source:" across 3–4 sections; the 5 bird pages were cp+sed ported, so they share near-identical section skeletons, sentence frames, and the same "Breeder note" cadence across pages — the classic mass-template fingerprint. This pass individuates them.

**Sub-skills to invoke first:** `skills/anti-ai-writing.md` (blacklist + human alternatives) and the First-Person Brand Voice rule (we/us/our/"here at C.A.Gs"). Also honor `feedback_hybrid_header_seo` (unique headers per page) and `feedback_noncommodity_audit_then_rewrite` (classify STRONG/SHARPEN/REBUILD; rewrite only weak — do NOT regress already-strong indexed copy).

**Files:** `src/pages/available/index.astro` + the 5 bird pages + the new breeding section.

- [ ] **Step 1: Audit — classify each section STRONG / SHARPEN / REBUILD**

Read each page; flag (a) verbatim cross-page sentence frames (e.g. the identical "A lot of bird listings describe what an African Grey is like in year one…" paragraph that appears on roys/amie/bery/evie), (b) the repeated "Breeder note:" H6 label, (c) third-person brand copy that should be first-person, (d) anti-AI blacklist phrases.

- [ ] **Step 2: De-template the shared frames**

For the identical "lifespan over decades" paragraph and any other cross-page-identical block, rewrite each bird's version with bird-specific, first-person, concrete detail (per `project_bird_page_port_pattern`: age copy must be real, not a token swap). Vary the H5/H6 framing per page (rotate "Breeder note:" → "From our aviary:", "What we've seen:", "One honest caveat:" etc.) so no two pages share the same label sequence.

- [ ] **Step 3: First-person + anti-AI sweep**

Convert third-person brand sentences to we/us/our (leave encyclopedic/taxonomy facts neutral). Remove anti-AI blacklist phrasing. Keep every claim inside the Verified-Claim Ledger (PBFD/Polyomavirus PCR screening IS assertable).

- [ ] **Step 4: Verify uniqueness across pages**

```bash
cd /Users/apple/Downloads/CAG
# The cross-page-identical lifespan frame should no longer be byte-identical:
grep -c "A lot of bird listings describe what an African Grey is like in year one" src/pages/available/{roys,amie,evie}/index.astro
```
Expected: 0 on at least the rewritten pages (or each retains a distinct, rewritten sentence — confirm by eye).

- [ ] **Step 5: Build + commit + push**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
git add src/pages/available/
git commit -m "content(available): first-person + anti-AI de-templating pass across hub + bird pages

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
```

---

## Task 7: Wire `/available/` into site navigation + internal links

**Problem:** The navbar has no `/available/` link (Header.astro:6-44); the homepage CTA points to the on-page `#available-birds` anchor, not the hub. Add real links so the hub gets crawl + user paths.

**Files:**
- Modify: `src/components/Header.astro` (nav array, ~line 8-18; mobile nav inherits the same array)
- Modify: `src/pages/index.astro` (homepage — add a hub link near the available-birds section/CTA)
- Modify: `src/components/Footer.astro` (add to the relevant column)
- Modify: `src/pages/african-grey-parrots-for-sale/index.astro` (location/buyer hub → link to live inventory), `src/pages/congo-african-grey-for-sale/index.astro`, `src/pages/timneh-african-grey-for-sale/index.astro` (variant pages → "see the ones available now")

- [ ] **Step 1: Add "Available Birds" to the navbar (Header.astro)**

In the `Shop Parrots` dropdown `children` array (Header.astro:10), add as the FIRST child:
```js
      { label: 'Available Birds Now',           href: '/available/' },
```
(Keeps one nav home for live inventory; mobile nav reuses the same `nav` array, so it appears in both.)

- [ ] **Step 2: Homepage — add a hub text link**

In the available-birds section intro/CTA area of `src/pages/index.astro` (near the `#available-birds` section, ~line 380, and/or the "View Available Birds" CTA at ~line 1175), add a keyword-anchored link to the hub, e.g.:
```html
<a href="/available/" class="text-clay font-medium underline decoration-clay/30 hover:decoration-clay">see every available African Grey for sale</a>
```
Keep the existing `#available-birds` anchor CTA; add the hub link alongside it (don't replace).

- [ ] **Step 3: Footer + variant/buyer hubs — add contextual links**

- Footer.astro: add `Available Birds` → `/available/` in the column with the shop/variant links.
- On each variant + buyer-hub page, add one mid-sentence link: "…the Congo and Timneh greys we have <a href="/available/">available right now</a>."

- [ ] **Step 4: Build + verify links resolve in dist**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
echo "Header link:"; grep -c "href=\"/available/\"" dist/index.html
echo "Hub exists:"; ls dist/available/index.html
```
Expected: homepage contains ≥1 `/available/` link; hub built.

- [ ] **Step 5: Commit + push, then regenerate sitemaps**

```bash
cd /Users/apple/Downloads/CAG
git add src/components/Header.astro src/components/Footer.astro src/pages/index.astro src/pages/african-grey-parrots-for-sale/index.astro src/pages/congo-african-grey-for-sale/index.astro src/pages/timneh-african-grey-for-sale/index.astro
git commit -m "feat(nav): link /available/ hub from navbar, homepage, footer, variant + buyer hubs

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
python3 scripts/generate_sitemaps.py
git add public/*.xml site/content/*.xml 2>/dev/null; git commit -m "chore: regenerate sitemaps" || true
git push origin main
```

---

## Task 8: Image-delivery perf — downscale oversized WebPs (~213 KiB)

**Problem (from Lighthouse):** Roster/hero images are served far larger than displayed (e.g. roys 800×661 served for 349×436; bery 960×792 for 349×349; amie/elad 582×480 for 384×288; infographic 1200×746 for 1098×683; footer logo 200×66 for 91×30; header logo 160×160 for 80×80). Downscale masters to ~2× the displayed size (retina-safe) and re-export WebP.

**Files (in `public/`):** `roys-congo-african-grey-male-4-months.webp`, `bery-congo-african-grey-female-1-year.webp`, `birds/amie/amie-handfed.webp`, `birds/elad/elad-timneh-african-grey-male-hero.webp`, `birds/evie/evie-timneh-african-grey-female-hero.webp`, `birds/elad/timneh-vs-congo-african-grey-infographic.webp`, `jins-jeni-congo-african-grey-pair.webp`, plus `cag-footer-logo.webp` and `cag-header-logo-160.webp`.

- [ ] **Step 1: Back up originals (so the resize is reversible)**

```bash
cd /Users/apple/Downloads/CAG && mkdir -p .img-backup && cp public/roys-congo-african-grey-male-4-months.webp public/bery-congo-african-grey-female-1-year.webp public/jins-jeni-congo-african-grey-pair.webp public/cag-footer-logo.webp public/cag-header-logo-160.webp public/birds/amie/amie-handfed.webp public/birds/elad/elad-timneh-african-grey-male-hero.webp public/birds/evie/evie-timneh-african-grey-female-hero.webp public/birds/elad/timneh-vs-congo-african-grey-infographic.webp .img-backup/ 2>/dev/null; ls .img-backup | wc -l
```

- [ ] **Step 2: Resize with Pillow to 2× displayed width, preserve aspect, re-save WebP q82**

```bash
cd /Users/apple/Downloads/CAG && python3 - <<'PY'
from PIL import Image
# (path, target_max_width)  — 2x the displayed CSS width
jobs = [
  ("public/roys-congo-african-grey-male-4-months.webp", 700),
  ("public/bery-congo-african-grey-female-1-year.webp", 700),
  ("public/birds/amie/amie-handfed.webp", 768),
  ("public/birds/elad/elad-timneh-african-grey-male-hero.webp", 768),
  ("public/birds/evie/evie-timneh-african-grey-female-hero.webp", 768),
  ("public/birds/elad/timneh-vs-congo-african-grey-infographic.webp", 1100),
  ("public/jins-jeni-congo-african-grey-pair.webp", 768),
  ("public/cag-footer-logo.webp", 200),   # keep crisp for retina of 91px
  ("public/cag-header-logo-160.webp", 160),
]
for path, w in jobs:
    im = Image.open(path)
    if im.width > w:
        h = round(im.height * w / im.width)
        im = im.resize((w, h), Image.LANCZOS)
        im.save(path, "WEBP", quality=82, method=6)
        print(f"resized {path} -> {w}x{h}")
    else:
        print(f"skip {path} (already {im.width}px)")
PY
```

- [ ] **Step 3: Confirm new file sizes shrank + dimensions correct**

```bash
cd /Users/apple/Downloads/CAG && for f in public/roys-congo-african-grey-male-4-months.webp public/bery-congo-african-grey-female-1-year.webp public/birds/amie/amie-handfed.webp public/birds/elad/timneh-vs-congo-african-grey-infographic.webp; do python3 -c "from PIL import Image; im=Image.open('$f'); import os; print('$f', im.size, round(os.path.getsize('$f')/1024,1),'KiB')"; done
```
Expected: widths match the targets; KiB notably lower than the Lighthouse "Transfer Size" figures.

- [ ] **Step 4: Build + commit + push**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
git add public/
git commit -m "perf(images): downscale oversized WebPs to 2x displayed size (~213 KiB saved)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
git push origin main
rm -rf .img-backup
```

---

## Task 9: Reduce unused JS / forced reflow + render-blocking CSS

**Honest diagnosis:** The 71 KiB unused JS at `/70de/` and the forced reflow are **Cloudflare Rocket Loader** (per project memory `aa_contrast_and_perf_fixes` — `/70de` = Rocket Loader). This is injected by Cloudflare at the edge, NOT by our code — so it cannot be fixed by editing the repo. It is a dashboard toggle.

**This task is mostly a breeder action + a small code-side render-blocking improvement.**

- [ ] **Step 1: (Breeder, manual) Disable Rocket Loader in Cloudflare**

In the Cloudflare dashboard → the `congoafricangreys.com` zone → **Speed → Optimization → Content Optimization → Rocket Loader → Off**. (CF API tokens are dead per memory, so this is a manual dashboard step. There is no repo change for this — flag it to the breeder; do not attempt via Bash.) After toggling, the `/70de/` script and its forced reflow disappear from Lighthouse.

- [ ] **Step 2: (Optional, code-side) Reduce render-blocking BaseLayout CSS**

`/_astro/BaseLayout.D8yS2GI3.css` (17.2 KiB, ~502 ms critical path) is render-blocking. Inspect `src/layouts/BaseLayout.astro` for how styles are linked. If Astro is emitting a blocking `<link rel="stylesheet">`, this is largely framework-managed; the highest-value, lowest-risk action is to confirm the fonts use `display=swap` and `preconnect` (already present) and leave the bundled CSS as-is unless a measured regression appears. Do NOT hand-split Astro's CSS bundle — risk outweighs the ~50 ms.

- [ ] **Step 3: Document the Rocket Loader dependency**

Add a one-line note to `sessions/2026-06-22-session-brief.md` Open Flags: "Perf: 71 KiB unused JS + forced reflow = Cloudflare Rocket Loader (/70de/); fix = dashboard toggle off, not a repo change." Commit:
```bash
cd /Users/apple/Downloads/CAG && git add sessions/2026-06-22-session-brief.md && git commit -m "docs: note Rocket Loader as the source of unused-JS/forced-reflow perf flags

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>" && git push origin main
```

---

## Task 10: Final verification gate (all 6 pages) + Lighthouse

- [ ] **Step 1: Build clean**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -8
```
Expected: build succeeds, no errors.

- [ ] **Step 2: Run the page-type-aware auditor on the bird cluster + hub**

```bash
cd /Users/apple/Downloads/CAG && python3 scripts/final_page_audit.py --birds 2>&1 | tail -40
```
Expected: PASS / PASS-WITH-WARNINGS for hub + all 6 bird pages (all six heading levels, ≥5 H5, ≥5 H6, single Product/Offer per bird, sold≠InStock, shipping line present, 700–1,000 words). Triage any FAIL before deploy.

- [ ] **Step 3: Verify schema + headings in dist (not source)**

```bash
cd /Users/apple/Downloads/CAG
for f in available available/roys available/amie available/elad available/evie available/jins-jeni; do echo "== $f =="; grep -o '"@type":"[A-Za-z]*"' dist/$f/index.html | sort | uniq -c; done
```
Expected: hub has CollectionPage + ItemList + Product/Offer + FAQPage; each bird page a single Product/Offer.

- [ ] **Step 4: Preview-verify the 6 pages (desktop + 375px mobile)**

Start the preview server; load the hub and all 5 updated bird pages. Check console for errors, confirm headers fit at 375px, images render and aren't blurry/oversized, the new breeding section and corrected Jins & Jeni copy read correctly. Capture screenshots as proof for the breeder.

- [ ] **Step 5: Lighthouse — warm median-of-3 on hub + one bird page**

Run Lighthouse 3× (warm cache) on `/available/` and one bird page; report the MEDIAN of Performance / LCP / CLS / INP (single cold runs lie — per `feedback_lighthouse_median`). Confirm the image-delivery savings landed and (if Rocket Loader was toggled) the unused-JS flag is gone.

- [ ] **Step 6: Final commit (if any verification fixes) + push; update session brief**

```bash
cd /Users/apple/Downloads/CAG && git add -A && git commit -m "chore(available): final-pass verification fixes for hub + 5 bird pages

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>" || echo "nothing to commit"
git push origin main
```
Record the batch outcome + Lighthouse medians in `sessions/2026-06-22-session-brief.md`.

---

## Self-Review

**Spec coverage (each of the breeder's asks → task):**
- 5 bird pages type-scale fix → Task 4 ✓
- 5 bird pages card/section polish → Task 5 ✓
- First-person + anti-AI + repeated-template audit → Task 6 (+ analysis already delivered in chat) ✓
- Breeding pair + fertile eggs section → Task 2 ✓
- Jins & Jeni "bonded" correction → Task 1 ✓
- Blog/pricing-tab image duplicate → Task 3 ✓
- Link hub + birds into navbar/homepage/etc. → Task 7 ✓
- Slug change question → answered in chat (keep `/available/`); no task needed ✓
- Hub hero image → 2 prompts delivered in chat; wiring deferred until the breeder generates the image (separate follow-up task once the asset exists) ⏳
- Reduce unused JS / forced reflow + image delivery + render-blocking → Tasks 8 + 9 ✓

**Open dependency:** Hub hero image — once the breeder generates Prompt A or B via Gemini and sends it back, add a small follow-up task: optimize → place in `public/` → replace the text-only hero (index.astro:120-128) with an image/background hero + HTML headline overlay → build/preview/commit. Not blocking the other 10 tasks.

**Type/path consistency:** Hub = `src/pages/available/index.astro`; bird pages = `src/pages/available/<slug>/index.astro`; nav = `src/components/Header.astro` (single `nav` array drives desktop + mobile). Existing target pages confirmed on disk: `/african-grey-breeding-pair-for-sale/`, `/african-grey-parrot-bird-eggs-for-sale-usa/`.

---

## Execution Handoff

**Plan complete and saved to `docs/superpowers/plans/2026-06-23-available-hub-and-bird-pages-batch.md`. Two execution options:**

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration.

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints.

**Which approach?**
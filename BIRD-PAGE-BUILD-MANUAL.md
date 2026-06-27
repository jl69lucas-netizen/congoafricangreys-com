# MANUAL — /available/ Bird-Page Build & QA Checklist (copy-paste)

> Companion to the `cag-bird-page-excellence` skill. This is the **copy-paste, verify-each-step** runbook for building, polishing, differentiating, and QA-ing an individual `/available/<slug>/` bird page or the `/available/` hub. Every command is runnable from the repo root. Tick each box.
>
> **Order of authority:** `CLAUDE.md` Non-Negotiables → this manual → the skill. If they conflict, surface it.

---

## Part 0 — Session start (ALWAYS)

- [ ] `git checkout main && git pull` — work on `main` only (only `main` auto-deploys).
- [ ] Read `PRODUCT.md` + `DESIGN.md` + `IMAGE-DESIGNS.md` before any design/content/image work.
- [ ] Confirm which bird(s) and the real facts: `python3 -c "import json;print(json.load(open('data/clutch-inventory.json')))"` — price, age, sex, variant, parentage (ask the breeder per bird; parentage is NOT in clutch-inventory).

---

## Part A — Differentiation (kills same-sex/variant cannibalization)

Trigger: ≥2 bird pages share the same **sex + variant** (e.g. two female Congos).

- [ ] **A1. Diagnose.** Compare the two H1s/titles:
  ```bash
  for b in bery amie; do grep -m1 -n 'const title' src/pages/available/$b/index.astro; \
    sed -n '/<h1/,/<\/h1>/p' src/pages/available/$b/index.astro | head -4; done
  ```
  If they are identical-minus-name/price → differentiate.
- [ ] **A2. Pick the axis = life-stage** (most-searched, least ambiguous). Build the matrix: each bird owns one life-stage + price tier + distinct related-terms.
- [ ] **A3. Present 2 options + Recommend+Why** (per CLAUDE.md) before editing. Add the **"Parrot"** entity to every H1/title/meta. Weave related terms: hand-reared, hand-fed, cuddly, tame, hen.
- [ ] **A4. Edit all four layers together** — H1, `const title`, `const description`, and the generic/cross-page-duplicate image `alt`/`title` lines. Keep alt ≤190 chars.
- [ ] **A5. Verify distinct in `dist/`:**
  ```bash
  npx astro build
  grep -o 'Bery — Tame[^<]*' dist/available/bery/index.html | head -1
  grep -o 'Amie — Hand-Fed[^<]*' dist/available/amie/index.html | head -1
  # old identical pattern must be gone from BOTH:
  grep -rl 'Female Congo African Grey For Sale (\$' dist/available/bery/index.html dist/available/amie/index.html || echo "OK removed"
  ```

---

## Part B — Geo distribution (real location pages as shipping sections)

- [ ] **B1. List the REAL slugs** (link only these): `ls -d src/pages/african-grey-parrot-for-sale-*/ src/pages/*-for-sale-*/ 2>/dev/null`.
- [ ] **B2. Assign one DISTINCT regional set + a unique H3 per bird page** (West/Mountain · Southeast · Midwest · NE/Mid-Atlantic · TX · pairs-coast-to-coast). No copy-paste lead sentence — duplicate-content risk.
- [ ] **B3. Internal links = same-tab** (no `target="_blank"`), anchor text = human place name, first-person framing.
- [ ] **B4. Verify EVERY href resolves on disk:**
  ```bash
  for slug in $(grep -rho 'href="/[a-z-]*for-sale[a-z-]*/"' src/pages/available/ \
    | sed 's/href="\///;s/"//' | grep -v '^available' | sort -u); do
    test -d "src/pages/${slug%/}" && echo "OK $slug" || echo "MISSING $slug"; done
  # any MISSING = invented slug → fix before building.
  ```
- [ ] **B5.** Confirm 0 external-tab on geo links: `grep -rn 'for-sale[a-z-]*/" target="_blank"' src/pages/available/ | wc -l` → `0`.

---

## Part C — Performance

- [ ] **C1. Render-blocking `JumpRail.css`.** Remove JumpRail **only if** the page has `cag-jump-nav`:
  ```bash
  grep -c 'cag-jump-nav\|JumpNav' src/pages/available/<slug>/index.astro   # must be >=1 before removing JumpRail
  # then delete the import line + the <JumpRail .../> element; verify:
  grep -rl JumpRail dist/available/ || echo "OK clean"
  ```
  ⚠️ Homepage + 16 interior pages use JumpRail as their ONLY ToC — do NOT remove it there.
- [ ] **C2. Unused JS `/70de/` (71 KiB) = Cloudflare Rocket Loader.** Hand off to breeder: **Speed → Optimization → Content Optimization → Rocket Loader = OFF.** Not a repo fix.
- [ ] **C3. LCP on video-hero pages** (roys/bery/amie/jins-jeni): preload the poster (`<video poster>` can't take `fetchpriority`). Add `heroPreload` prop → BaseLayout `<head>`. Verify: `grep 'rel="preload" as="image"' dist/available/<slug>/index.html`.
- [ ] **C4. Oversized images.** Pillow downscale to ~2× CSS display, **shrink-only**, q=80:
  ```bash
  python3 scripts/downscale_available_images.py   # shrink-only guard: if im.width > target_w
  npx astro build && ls -la dist/birds/<slug>/<hero>.webp   # confirm shrank, NOT grew
  ```

---

## Part D — Accessibility (AA contrast)

- [ ] **D1.** Find clay-on-dark: `grep -rn 'text-gold' src/pages/available/`.
- [ ] **D2.** Replace `text-gold` / `text-gold/90` on `bg-logo-dark` → `text-[#f08070]`. Drop opacity modifiers on small clay text.
- [ ] **D3.** Verify ratio ≥ 4.5 (snippet in the skill). Build → `grep -rn 'text-gold' dist/available/` should be empty in the cluster.

---

## Part E — Schema (truthful Offer only — NO reviews)

- [ ] **E1.** Capture the EXACT Search-Console critical field via Rich Results Test (human browser — Google blocks bots).
- [ ] **E2.** Extend each page's `productSchema.offers` with truthful fields: `priceValidUntil`, `shippingDetails` (OfferShippingDetails, $185, US), `hasMerchantReturnPolicy` (real health-guarantee window — confirm against `/african-grey-parrot-health-guarantee/`). **Never** add `review`/`aggregateRating`.
- [ ] **E3.** Verify JSON-LD parses + single Product/Offer:
  ```bash
  npx astro build
  python3 -c "import re,json,glob;[json.loads(b) for f in glob.glob('dist/available/*/index.html') for b in re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>',open(f).read(),re.S)];print('all parse OK')"
  ```

---

## Part F — Broken external links

- [ ] **F1.** `grep -rn "international-affairs/what-cites" src/` → replace with `https://www.fws.gov/international-affairs/cites`.
- [ ] **F2.** **Human browser** confirms 200 (fws/cites 403 every bot). Fallback `https://cites.org` if 404.
- [ ] **F3.** `grep -rn "international-affairs/what-cites" src/ ; echo exit:$?` → no matches.

---

## Part G — Keyword / entity / voice self-audit

- [ ] **G1.** Per-page keyword density + voice/heading scan (scripts in the audit doc `docs/superpowers/sessions/2026-06-26-available-keyword-entity-audit.md`).
- [ ] **G2.** Verdict STRONG / SHARPEN / REBUILD per page — **rewrite only the weak ones** (don't regress indexed copy).
- [ ] **G3.** Competitor benchmark via Firecrawl; mark un-fetchable competitors `NOT FETCHED` — never invent counts.

---

## Part H — Final gate + deploy (ALWAYS last)

- [ ] **H1.** Resolve working-tree deletions — **grep references BEFORE committing any deletion:**
  ```bash
  for f in <deleted-files>; do grep -rln "$f" src/ public/ || echo "  $f: no refs → safe"; done
  # if referenced → git checkout -- <path> (restore); never break live images.
  ```
- [ ] **H2.** `python3 scripts/generate_sitemaps.py` → 0 phantom URLs.
- [ ] **H3.** `npx astro build && python3 scripts/final_page_audit.py --birds` → **0 FAIL**. (PASS-WITH-WARNINGS on `wordcount_in_band` + `house_method` is accepted for Roys-standard pages.)
- [ ] **H4.** Commit + push (push = deploy). Don't amend an auto-pushed commit — add a new one.
  ```bash
  git add src/pages/available/ && git commit -m "…" && git push origin main
  git rev-parse --short HEAD; git rev-parse --short origin/main   # must match
  ```
- [ ] **H5.** After Cloudflare builds: human re-runs PageSpeed + Rich Results Test on `/available/`, one Congo, one Timneh.

---

## Human-only steps (no bot can do these)

1. **Rocket Loader OFF** — Cloudflare dashboard (biggest mobile-LCP win).
2. **Browser-verify** fws.gov/cites link returns 200.
3. **Rich Results Test** re-run to confirm Product critical cleared.

(fws.gov, cites.org, and Google's testers 403 every automated agent — these can never be auto-verified.)

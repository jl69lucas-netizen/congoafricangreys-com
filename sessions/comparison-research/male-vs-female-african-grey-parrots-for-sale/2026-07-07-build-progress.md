# Build Progress — /male-vs-female-african-grey-parrots-for-sale/ (2026-07-07)

Rebuilding from the congo-vs-timneh skeleton (proven port pattern). Page is on disk at
`src/pages/male-vs-female-african-grey-parrots-for-sale/index.astro` — **uncommitted, not live**.

## DONE
- Steps 1–4 (keywords merged, image system approved, outline approved, 24-slot Gemini prompt pack).
- All images processed into `public/` with `-760` siblings (23/24 GEM + 17 OG + 2 videos). **G13 first-timer
  infographic still MISSING** (`male-or-female-african-grey-for-first-time-owner-infographic.webp`) — breeder to generate.
- Skeleton ported from congo-vs-timneh.
- **Frontmatter data spine rewritten:** title (4-part, ends "C.A.Gs – DNA-Sexed African Greys"), description,
  breadcrumbs, canonical, 12 male-vs-female FAQs + faqSchema, articleSchema (headline + dateModified 2026-07-07),
  `rows` (♂/♀ honesty comparison, keys renamed male/female), `takeaways` (8), `scores` (near-equal, keys m/f),
  `tocItems` (21 sections). `available`, `birdImg`, `docBadges`, `shipPlaces`, `stories`, `num` kept as-is.

## CHUNK STATUS
- **Chunk A (§1–8: quick-answer → sexing) — DONE + verified** (hero Kent♂/Evie♀, counter, TOC, side-by-side table w/ mobile tab, behavior/male/female/sexing deep-dives). Raw ♂/♀ removed from hero chips (U+2642 mis-renders to ↕ in this font env + DESIGN.md pictograph ban).
- **Chunk B (§9–22: scorecard → reserve) — DONE + verified 2026-07-07.** Rewrote scorecard (s.m/s.f + near-equal framing), household (id lifestyle→household, sex-fit cards), cost (sex-doesn't-change-price honesty), first30, myths (male/female folklore), CITES (either-sex), shipping, available (sex badges from clutch `sex` field), stories, faq H2. Added 2 NEW sections: **pairs** (one/pair/same-sex, moved breeding-pair+eggs cross-sell out of available) and **safe** (scam counter, sex-surcharge red flags). Form interest options → male/female/pair. Wired 13 real male/female infographics (all base+-760 verified). Removed all raw ♂/♀ glyphs for consistency with Chunk A.
- **GATES PASSED:** `npx astro build` clean · `final_page_audit.py --comparison` = **PASS-WITH-WARNINGS** (H1:1 H2:22 H3:39 H4:15 H5:8 H6:8; FAQPage+Article schema; 3 WARNs identical to approved congo-vs-timneh template) · section ids ⇄ tocItems match (22, correct order) · desc 290 chars · 0 alts >190 · no console errors · 200. Fixed 2 mechanical FAILs (desc_le300, img_alt_le190).

## REMAINING → FINALIZE + DEPLOY (page still uncommitted / not live)
- keyword-verifier pass · warm median-of-3 Lighthouse · `cag-branded-hybrid-keywords` optional in-content pass.
- Delete `public/_imglab/` · `python3 scripts/generate_sitemaps.py` (new URL needs sitemap) · commit + push (= deploy) · deploy-verify 200 + IndexNow.
- G13 first-timer infographic NOT referenced in build (used which-african-grey-sex-fits-your-household for §household) — no blocker.

## (historical) REMAINING (body authoring pass — lines ~157–680)
1. **heroPreload** (BaseLayout props) → Kent portrait / update srcset+sizes.
2. **S1 Hero** → Kent ♂ (portrait card, `.sec-img.portrait`) L / Evie ♀ (landscape) R + `vs` roundel; eyebrow sentence-case; H1 "Male vs. Female African Grey Parrots for Sale".
3. **S2 Counter** → `100%` DNA-sexed · `PCR` cert · `100%` CITES · `24h` reply (swap the 4 chips).
4. **Rewrite all 21 sections** to the approved outline (ids now: quick-answer, takeaways, side-by-side, trust,
   behavior, male, female, sexing, scorecard, household, cost, first30, myths, pairs, cites, shipping, available,
   stories, safe, faq, learn, reserve). Each H2/H3 = conversational FAQ Q&A header + **mandatory opening
   conversational paragraph** (primary/entity/LSI not in header, AIO format What/Do/Is/How). First-person.
5. **Table markup** (S6) → change `r.congo`/`r.timneh` → `r.male`/`r.female`; headers "Male ♂ / Female ♀"
   (drop congo/timneh icons or use ♂/♀); mobile tab toggle labels Male/Female.
6. **Score table** (scorecard) → `s.c`/`s.t` → `s.m`/`s.f`; headers Male/Female.
7. **Wire all 43 images** per the approved 2026-07-06 image spec (portrait branch = Kent only; everything else
   landscape). OG + GEM filenames per the outline + prompt-pack mapping. G13 slot = placeholder until generated.
8. **NEW sections vs reference:** owner-gender H3 (behavior), variant-sexing H3s (sexing: Congo + Timneh),
   pairs H2 (one/pair/same-sex), safe-buying H2 (scam counter). Drop reference's "noise/dander" + variant deep-dives;
   repurpose "congo"→"male", "timneh"→"female" as SEX deep-dives.
9. **Heading gate:** all six levels, ≥5 H5 AND ≥5 H6 (outline already maps 6 H5 + 6 H6).
10. **Form** (reserve) → interest select options to ♂ / ♀ / pair / not sure; keep cvt- ids.
11. Gates: `npx astro build` → verify dist → `final_page_audit.py --comparison` → keyword-verifier → Lighthouse → deploy.
12. **Cleanup:** delete `public/_imglab/` before final deploy + regenerate sitemaps.

## Reference idioms (congo-vs-timneh index.astro)
`.cag-h2/3/4/5/6` headings · `.sec-img` / `.sec-img.portrait` / `.inf-img` (srcset 760w+1408w) ·
`.qa-box` · `.kt-grid/.kt-c` · `.cmpe`/`.cmp-tbl` w/ mobile tab · `.author-card` · `.match-grid` ·
`.score-tbl` (data-label mobile stack) · `.seam` divider (`/cag-footer-logo-80.webp`) · `.final-cta` form.
Style block (lines ~705–978) reused unchanged.

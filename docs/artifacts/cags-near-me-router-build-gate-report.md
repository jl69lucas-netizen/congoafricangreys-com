# Near-Me Router Build Gate Report

Published as artifact `d13141b8` → https://claude.ai/code/artifact/d13141b8-a987-481f-a582-cb0c437c1fb6. Source of truth is this file.

## 1. Verdict
**PASS-WITH-WARNINGS, shipped.** `/african-grey-parrots-for-sale-near-me/` went from a 5.5 KB stub (1 H2, no H3–H6, no shipping line, no hero, a wrong Timneh price) to the for-sale cluster's geo router: 6,410 words in `<main>`, the full H1–H6 band (9 · 24 · 7 · 7 · 7), 26 infographics and 6 card photos, six live birds with prices and the shipping line on every card, and the **only** enumeration of the 40 state and metro destinations on the whole site.

Every text gate is clean on the shipped build: hardening scan 0 ERROR / 0 WARN, seam parity 9 seams for 10 sections (form and FAQ share one, in profile), dup body PASS, dup headers clean for this page, evidence 0 ERROR, AEO 0 ERROR, final page audit PASS-WITH-WARNINGS on the `no_aggregateoffer` checker row every for-sale sibling carries, render meta 296 passed, thumb audit 43 of 43. Render pages: **6 of 6 passed** for both slugs at 375 / 768 / 1280 after one blocking NAV row was fixed (40 state-tile jump targets declared the mobile 166px scroll-margin at desktop; now header + 16px). The two advisory rows that remain on both pages are the sitewide Header `mobile-section` orphan class and the breadcrumb separator at 2.38:1, both components.

Three reviews the breeder asked for, none of which ran on Page A, ran here: non-commodity, entity incorporation and keyword verification. They produced 5 sharpened passages, 2 humor beats, 10 grounded entities, a schema addition, and **four overclaims removed**, one of which was also live on Page A and is corrected there.

## 2. What was built, from the approved outline
| Axis | Tuple 12 pick | Shipped as |
|---|---|---|
| Hero | Hero-C Mosaic Metrics, refreshed to a geographic tile field | Deep-green field (the one dark hero in the cluster), metrics strip, 2:1 photo with caption, **25 state tiles** that jump into the grid plus a "15 metros" cell; 394px at 1280; image first on phones by CSS `order` |
| Dial + rail | Dial 1 Clay + Rail B green ticker | 9 rows × 29px, label + tag inside the 130px budget; rail sticky under the header, chip gap 10px |
| TOC | T2 Chip Cloud, refreshed | Region → state chips (South / West / Midwest / Northeast), a metro row, a section row; chips flash their target tile |
| Takeaways | K3 Green Ledger + K4 Clipboard + K5 Capsule | K3 "Near, or Reachable" five lines · K4 "Ask Before You Drive" checklist under the H6 of that name · K5 four capsules |
| Table | NEW Table I "Distance Ledger" | 25 rows: state · route · **cargo counter named on that state's page** (13 states) or "Named when you ask" (11) · cost tier; stacks to cards ≤640 |
| FAQ | FAQ-B, map-pin register | 12 questions, pin glyph in place of the number chip, two columns to 980 then one, answers capped 70ch |
| H6 prefixes | `Distance Note:` · `From Midland:` · `Ask Before You Drive:` | 2 · 3 · 2, none among the 19 spent |
| Geo | All 39 shallowly | 24 state tiles + CA buy page + 15 metros nested under their state and repeated as a pin list; 40 links, all 200 |

Every figure reads from `price-matrix.json`, `financial-entities.json`, `clutch-inventory.json` or `locations.json`. The Timneh weight band and the Congo band in the birds section come from the price matrix, not prose. No review quotes (all 17 are spent elsewhere); the 3-3-3 rule stays out (locked).

## 3. SEO, AEO, GEO, evidence and voice
- **Title** 63 chars, one clause, brand present. **Description** 153 chars (first cut was 164). Canonical absolute.
- **Keyword variance** carried on purpose: "African gray parrot for sale near me" verbatim, "African Grey breeders near me" and "African grey for sale near me" verbatim, the exact primary in the hero lead and an FAQ; gray 5 / grey 15 as words; no phrase over 0.25 % density.
- **Rule 50b**: primary phrase in the hero alt only; 38 unique non-empty alts, 9 decorative seams; none over 125 chars.
- **Term budgets in `<main>`**: C.A.Gs 4 / 15 · CITES 2 / 5 · Appendix I 2 / 3 · DNA 2 / 6 · captive-bred 5 / 5 · USDA 3 / 3 · Midland 7 / 8 · scam 1 / 2 · legit 0. Two per-slug overrides recorded with their reasons: Midland 8 (the approved outline names it in 1 H3, 1 H5 and 3 H6 prefixes; the form's pickup option; the method label) and Appendix I 3 (approved H3 + one Fact sentence + the QA'd infographic alt).
- **First build measured Midland ×32** because the Distance Ledger said "Flies from Midland" on 24 rows. Real defect, fixed to "Flies from MAF, our airport". A table column counts.
- **AEO**: binomials once each, breeder name once, 3 stat-bearing headers, one table, 30 lists, two `OfferShippingDetails` nodes ($185 / $350, US) referenced from every Offer. Remaining WARNs: pronoun-heavy (advisory, house voice) and three BLUF proxies on footer headings.
- **Statement labels**: Fact ↗ CITES appendices; Fact ↗ IUCN lifespan (40 to 60 years); Observed here since 2014 on the paperwork-travels-with-the-bird practice.
- **Evidence WARN accepted**: `pbfd-apv-pcr` counted twice inside the one sentence that names PBFD and avian polyomavirus together; the sentence links the guarantee page, which owns the claim.

## 4. The three reviews
### Non-commodity (Archaeologist / Provocateur / Stylist)
Applied: five weak passages rewritten (FAQ distance summary, the avian-vet note, "what a real breeder lets you do", the Timneh crate line now carrying the two weight bands, the legality answer kept with its local-rules caveat); two Honesty-Policy beats ("The bird has never corrected anyone's spelling. It corrects most other things." · "the showroom is our living room, and the floor model talks back"). Declined: a third beat, to keep one per section.

**Overclaims removed:**
1. **"Bonded pair" → "companion pair"** on this page and on Page A. Jins & Jeni are an unrelated companion pair, separable on request (breeder ruling 2026-06-23, `clutch-inventory.json`). Page A also said they "chose each other in the flight cage and have been inseparable since" and that "the answer is no" to splitting them; both unsourced, both contradicted the data file, both corrected. The approved H3 "The Bonded Pair" is now "The Companion Pair" on both pages, for the breeder to confirm.
2. "Every state page points at the avian practices buyers there have used" — false for several state pages; replaced by the AAV find-a-vet link.
3. "Buyers from Lubbock, Odessa, San Angelo and Abilene do this regularly" — unsourced; cut.
4. `Observed here · 6 birds` under a sentence about every bird flown since 2014 — narrowed to `since 2014`.

### Entity incorporation (4-Move Loop)
Ten distinct entities, each once: IATA Live Animals Regulations ↗ (recommended), AAV find-a-vet ↗, APHIS Animal Care public search ↗, avian polyomavirus, psittacosis, board-certified avian veterinarian, Midland International Air and Space Port (MAF) resolved once, closed leg band, reverse image search, Delta Cargo / United Cargo / American Airlines Cargo. Declined: "United PetSafe" (the agent could not fetch the programme page; nothing unverifiable was written). Schema: `OfferShippingDetails` added as the agent proposed.

### Keyword verifier
12 pass · 1 fail (meta length, fixed) · 2 missing forms (added) · 3 warns, all the "near you" phrasing of the approved H1 (left as approved).

## 5. Runtime probes (Playwright, painting viewport)
| Viewport | Before → after |
|---|---|
| 1280 | hero grid 418 → **394px** (16:9 → 2:1 photo) · dial 8 of 9 rows wrapping at 43–58px → **9 × 29px** (labels shortened to the 130px budget) · tile links 12.16px and table headers 12.48px → 12.8px · ship-line 107ch and clipboard title 97ch → 70ch cap · **hero lead invisible** (ink on dark green) → cream · 0 contrast fails, 0 srcset waste |
| 768 | FAQ answers 85ch single-column → 70ch · rail chip gap 8 → 10px · state grid 3-up, cards 2-up uniform 568px · hero 567px, two columns held to 700px |
| 375 | scrollWidth 375, no overflow · image first · tile field 7 columns · state grid 2-up · cards 1-up · ledger stacks to cards · rail jump lands the H2 27px below the sticky rail · 0 contrast, 0 small fonts |

## 6. Impeccable and frontend-design critique
Register: brand. Scene: a scam-wary buyer on a phone who typed "near me" and got a page of classifieds. Colour strategy: Committed (forest + clay on cream, as `DESIGN.md` locks it); the hero is the cluster's one deep-green field, a deliberate delta from Page A's warm cream and dna-tested's cream Hero-C, not a palette change. No absolute-ban hit: no gradient text, no glass, no hero-metric template (the metrics strip is three facts about this page's function, not a KPI row), no side-stripe cards, no identical icon-card grid (the state tiles are navigation, each a distinct destination). Theme sentence forced the answer: the tile field is a map without a map, and the dark ground is what makes 25 cream tiles read as one field. Type: Newsreader + IBM Plex Sans via the theme; the H1 honours its clamp at 31.68px. Motion: hover lift and a 1.6s target flash only.

## 7. Learning loop
Seven escapes, six charged to tools or probes, one to the page:
1. **Contrast sweep ignored alpha** — 30 false fails on translucent white over the dark hero. Composite translucent layers over the nearest opaque colour.
2. **The static hardening scan cannot see the theme.** `body.theme-d h1 + p` (global.css) out-specified `.nmr .hero .lead` and painted it ink on dark green. §1l reads page CSS only; my gradient-skipping sweep skipped it too. Caught by eye on the fold screenshot. Fix on the page: a class containing `text-cream`, the rule's own escape hatch. Harness gap logged (§9).
3. **A `display:grid` link stacks its inline arrow** — "15 metros →" on two lines; `inline-flex` fixed it. Only the screenshot saw it.
4. **The thumb baker swallowed the footer** — a `.read-cards` block inside a `<nav>` ran to the footer's `</section>` and minted a stray `read--hero` for `href="/"`. Fixed in `scripts/bake_read_card_thumbs.py` (stop at `</nav>` or `</section>`, whichever first). No new rule.
5. **The dup gate reads data furniture as prose** — the Avail-B filter rail and the form-side inventory list are rendered from `clutch-inventory.json`. Two stems whitelisted (one list, two readers).
6. **Harness freshness check worked** — it refused to measure once source was newer than `dist/`, and the earlier run broke because I rebuilt mid-run. Never build while `test:render:pages` runs.
7. **Page defect, the real one:** "Flies from Midland" × 24 rows. Term budgets count table columns.

## 8. Page Board status
No spec yet. Page B, like Page A, shipped through the old lane (outline gate → tuple → build → harden). The Page Board brainstorm still stops at clarifying questions. Order now: Page Board spec → hub C through the first board → Task 11 (the three near-me 301s into this page, 9 inbound links on 7 pages repointed, IndexNow all 7) → Task 13 (hub sheds the grid).

## 9. Open flags for the breeder
- **Confirm the heading change**: "The Bonded Pair" → "The Companion Pair" on both pages, per your 2026-06-23 ruling. Page A's invented flight-cage sentence is gone.
- **Page A header crossover**: "Reservable Right Now" is an exact H3 match with the health-guarantee page. One of the two should rename; not touched this session.
- **Hero at 768** is 567px (Page A shipped 528). A tablet trim would hide the metrics strip under 980; not done without a preview.
- **Harness backlog**: §1l needs `src/styles/global.css` descendant rules as input plus a `known_broken` fixture that inlines the theme rule; `no_aggregateoffer` still needs its fixture.
- **Distance Ledger**: 11 state pages name no cargo counter. When each state page gains one, the ledger picks it up by editing `namedAirports` in the page's frontmatter; nothing is inferred.

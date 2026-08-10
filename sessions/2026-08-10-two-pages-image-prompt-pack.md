# Image Prompt Pack — Page A and Page B

**Date:** 2026-08-10 · **Plan Task 7** · **Status: this pack is the shopping list for the HARD STOP.**

**Rules binding on every slot below:**
- Every H2, H3 and key H4 carries an image — OG photo or infographic.
- Uniform in-body box: `.sec-img.inf-img`, **760px 16:9**, WebP under 100 KB, `-760.webp` sibling + srcset.
- **Rule 50b — no two images on a page share an alt.** Alts below are drafts; each is unique within its page.
- OG portrait photos: bake with `scripts/reframe_og.py --style blurfill --mobcrop 4:5` from the ORIGINAL master. **Never cover-crop a portrait with a focal point — it cuts heads.** Tag `<img class="sec-img og-photo og-tall">`.
- Wide/scene/infographic images stay standard 16:9 desktop / 5:4 mobile.
- Infographics: 300–350px tall, three types only (Comparison / Feature Grid / Process Flow), reserved box to avoid CLS.
- Species markers use `/emoji/cag-congo.png` and `/emoji/cag-timneh.png`. **Never 🦜.**
- Seam emblems are decorative: `alt=""` + `loading="lazy"` + explicit CLS dimensions.
- **No text overlay in any generated image** — text baked into art cannot be translated, cannot be read by screen readers, and ages badly.

---

## Part 1 — What the breeder needs to supply (photos we cannot generate)

These are **real birds** and must be real photographs. AI generation is not acceptable for any of them.

| # | Slot | Bird | Framing | Where it lands |
|---|---|---|---|---|
| P1 | Bird card | **Bery** (Congo hen, $1,700) | portrait, blurfill, mobcrop 4:5 | A · H2 1 · B · H2 4 |
| P2 | Bird card | **Amie** (Congo hen, $2,500) | portrait, blurfill | A · H2 1 · B · H2 4 |
| P3 | Bird card | **Roys** (Congo cock, $2,300) | portrait, blurfill | A · H2 1 |
| P4 | Bird card | **Elad** (Timneh cock, $1,600) | portrait, blurfill | A · H2 1 · B · H2 4 |
| P5 | Bird card | **Evie** (Timneh hen, $1,500) | portrait, blurfill | A · H2 1 |
| P6 | Bird card | **Jins & Jeni** (bonded pair, $3,500) | duo strip / two-bird framing | A · H2 1 · B · H2 4 |
| P7 | Hero, Page A | any confident single Congo, room to the right for the ribbon | ~400px class, wide | A · hero |
| P8 | Hero, Page B | aviary-wide or multi-bird scene behind the geographic tile field | ~400px class, wide | B · hero |
| P9 | Documents | the real document folder — CITES cert, DNA cert, vet certificate, hatch cert, band | flat-lay, wide | A · H2 3 · B · H2 6 |
| P10 | Newsletter A | **must not be shared with Page B** | wide | A · newsletter |
| P11 | Newsletter B | **must not be shared with Page A** | wide | B · newsletter |

> **Pass-gate:** unique newsletter image + one-liner title per page. Sharing P10/P11 fails the gate.
> **Read-card thumbnails are not in this list** — they are cut from **the target page's own hero**, which is BINDING and already exists for every target.

---

## Part 2 — Generated images

### Page A

**A-INF-1 · The Price Ladder** *(Comparison · lands under H2 2, the MANDATORY price-artifact section)*
> Photoreal-clean editorial infographic, warm terracotta and forest-green palette on cream. A vertical price ladder from $850 at the base to $8,500 at the top, with a highlighted band at $1,500–$3,500. Flat vector, generous whitespace, no photographic elements, no text overlay, no logos, 16:9.

**Alt:** `Price ladder showing African Grey listings from $850 to $8,500 with the C.A.Gs band marked`
*Numbers, source labels and the measurement date are rendered as HTML in Table H — never baked into the art, so they stay editable when prices move.*

**A-INF-2 · One Seller, Three Platforms** *(Comparison · under H2 2, H3 1)*
> Flat editorial diagram: one aviary icon at centre, three arrows to three platform cards, each card holding a different price chip. Terracotta arrows on cream, forest-green cards. No brand marks, no text overlay, 16:9.

**Alt:** `One seller's African Greys listed at three different prices across three platforms`

**A-INF-3 · What a Real Price Includes** *(Feature Grid · under H2 2, H3 2)*
> Six-cell flat grid of line-art icons — hand-feeding syringe, avian stethoscope, DNA helix, certificate, leg band, transport crate — on cream with forest-green strokes and terracotta accents. No text overlay, 16:9.

**Alt:** `Six cost components behind an honest hand-raised African Grey price`

**A-OG-1 · Airport cargo** *(reuse the banked prompt verbatim · under H2 5)*
> Photoreal IATA-approved live-animal airline cargo crate holding a calm captive-bred African Grey, at a Delta/United cargo counter under warm terminal light; ventilated door, water cup, C.A.Gs handling label; shallow depth of field, no logos of other brands, no text overlay, 16:9.

**Alt:** `IATA-approved travel crate with an African Grey at the airline cargo counter`

**A-OG-2 · Home delivery** *(reuse the banked prompt verbatim · under H2 5)*
> Photoreal climate-controlled pet courier van at a suburban front door, a uniformed handler passing a soft-sided African Grey carrier + a document folder to a smiling family; golden-hour light, warm terracotta grade, no visible brand logos, no text overlay, 16:9.

**Alt:** `Courier handing an African Grey carrier and document folder to a family at their door`

**A-INF-4 · The First 72 Hours** *(Process Flow · under H2 4)*
> Four-step horizontal flow on cream — arrival, same-day check, avian vet visit, written outcome — forest-green step markers, terracotta connector line, flat line-art. No text overlay, 16:9.

**Alt:** `Four steps covered by the seventy-two hour health guarantee after arrival`

**A-INF-5 · Five-State Routes** *(Feature Grid · under H2 6)*
> Minimal flat map of the continental United States in muted cream and sage, with Midland Texas marked in terracotta and five route arcs reaching Iowa, Kentucky, Maryland, Tennessee and Wisconsin. No state labels baked in, no text overlay, 16:9.

**Alt:** `Flight routes from Midland Texas to Iowa, Kentucky, Maryland, Tennessee and Wisconsin`

**A-INF-6 · Congo or Timneh** *(Comparison · under H2 7)*
> Two-column flat comparison card, a Congo silhouette left with a red tail accent and a Timneh silhouette right with a maroon tail accent, sized to scale against each other. Cream ground, forest-green rules. No text overlay, 16:9.

**Alt:** `Congo and Timneh African Grey silhouettes compared at true relative size`

**A-INF-7 · Five Checks** *(Feature Grid · under H2 8)*
> Five flat line-art check cards on cream — verifiable address, licence number, live video of the named bird, written documentation, traceable payment — forest-green strokes, terracotta check marks. No text overlay, 16:9.

**Alt:** `Five verification checks that expose a fraudulent African Grey listing`

### Page B

**B-INF-1 · Anatomy of a Near-Me Result** *(Comparison · under H2 1)*
> Flat editorial diagram of a stylised search results page — a map pack block at top, then result rows — with the geo-scoped rows highlighted in terracotta and the national rows greyed. Cream ground, no readable text, no logos, no text overlay, 16:9.

**Alt:** `Near-me search results dominated by location-specific listings above national pages`

**B-INF-2 · Drive or Fly** *(Process Flow · under H2 3)*
> Minimal flat United States map, cream and sage, Midland Texas marked in terracotta with a small filled radius ring around it and route arcs fanning out to the rest of the country. No text overlay, no state labels, 16:9.

**Alt:** `Midland pickup radius and nationwide flight routes from the C.A.Gs aviary`

**B-INF-3 · Three Prices, One Seller** *(Comparison · under H2 5 — the cheap/Craigslist section)*
> Flat diagram of three listing cards side by side, each showing a different price chip for the same bird silhouette, with a terracotta question mark connecting them. Cream ground, forest-green rules. **Deliberately composed differently from A-INF-2** — cards abreast rather than a hub and spokes. No text overlay, 16:9.

**Alt:** `The same African Grey advertised at three different prices on three classified sites`

**B-INF-4 · What Arrives With Your Bird** *(Feature Grid · under H2 6)*
> Five flat document icons in a row on cream — CITES certificate, DNA certificate, vet health certificate, hatch certificate, leg band — forest-green line art with terracotta seals. No text overlay, 16:9.

**Alt:** `The five documents that travel with every African Grey we place`

**B-INF-5 · If Something Is Wrong on Arrival** *(Process Flow · under H2 7)*
> Three-step flat flow on cream — same-day call, local avian vet, written outcome — terracotta connectors, forest-green markers. **Composed differently from A-INF-4** (three steps vertical rather than four horizontal). No text overlay, 16:9.

**Alt:** `Three steps to take if an African Grey arrives unwell`

---

## Part 3 — Alt-text uniqueness check

**Page A:** 11 image slots (P1–P7, P9, P10 + 9 generated) — every alt above differs in its first five words. **Page B:** 9 slots — same.
**No alt is reused across the two pages**, which matters because the dup gate reads rendered output and alts are rendered text.

**Two near-duplicate pairs are deliberate and must stay visually distinct:**
- A-INF-2 vs B-INF-3 — same evidence, different composition (hub-and-spoke vs cards abreast), different alt.
- A-INF-4 vs B-INF-5 — same guarantee, different composition (four horizontal vs three vertical), different alt.

---

## Part 4 — ⛔ HARD STOP

**Task 8 does not begin until the breeder has supplied the Part 1 photographs and said explicitly to start.**

This stop is in the skill's Phase 2 and is not one I can work around: the build cannot proceed on placeholder
art, because image slots drive the section rhythm, the CLS reservations, and the alt-text spread that the
gates measure.

**What is needed to lift the stop:**
1. **P1–P6** — the six bird photographs (Bery, Amie, Roys, Elad, Evie, Jins & Jeni).
2. **P7, P8** — one hero photograph per page.
3. **P9** — the real document flat-lay.
4. **P10, P11** — two newsletter images, one per page, not shared.
5. Confirmation to generate the **14 infographics** in Part 2, or edits to any prompt first.

**Already available, nothing needed:** read-card thumbnails (cut from each target page's existing hero) and
the seam emblem (`public/cag-fs-seam-emblem.webp`).

**One open flag carried into the build:** the 3-3-3 rule is still not in the Verified-Claim Ledger, so it
stays out of both FAQs and no image slot depends on it.

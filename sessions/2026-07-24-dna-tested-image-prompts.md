# DNA-Tested Page — Infographic Prompt Pack
## `/dna-tested-african-grey-for-sale/`

Every H2/H3/H4 slot that needs a **generated** visual. Slots already covered by a real OG photo or video are listed first and need **no prompt**.
All figures verified against `data/clutch-inventory.json`, `data/price-matrix.json`, the Verified-Claim Ledger, `IMAGE-DESIGNS.md §0–§3`, and the breeder's Sprint-1 answers (Avian Biotech · both sample types · $40–60 certificate · ~99% accuracy).
Flat-design infographics (data-bearing) — **not** photoreal. Target **16:9, 1408×768**, export WebP **<95 KB** + a **`-760.webp`** sibling.

---

## A. Slots already covered by REAL assets — do NOT generate

| Slot | Asset (all verified unused elsewhere in the cluster) |
|---|---|
| **Hero — anchor cell** | `assets/brand/JINS-JENI/jins-jeni1.webp` — two Congos side by side, both faces forward. **One is a cock, one is a hen, and they look identical.** The page's whole thesis in one real photograph |
| **Hero — mosaic tiles** | crops from `assets/brand/hero-available-grey-parrots.webp` (1672×941, 7-cell contact sheet) |
| §monomorphic | `assets/brand/JINS-JENI/jins-jeni2.webp` + `Jins-jeni3.webp` — more identical-looking pair frames |
| §monomorphic (lineage note) | `assets/brand/JINS-JENI/Macy-letis-Jins-jeni-parent.webp` — the **parent birds**. Genetics theme, earns its place on a DNA page |
| §available | the 6 real bird cards (Bery · Amie · Roys · Jins & Jeni · Elad · Evie) |
| §behaviour teaser | `assets/brand/cags-tame-african-grey-parrot-with-owner.webp` *(alt: `talking-african-grey-hand-close-bond.jpg.webp`)* |
| §video | `assets/brand/African-grey-pair-eating.mp4` — an unused video of a **pair** feeding. Cock and hen on camera together, which is exactly this page's argument |
| §reviews | Stanley Perkin + Jesse Ovalle review photos |
| §newsletter | `assets/brand/Roys/2-years-old-African-Grey-Parrot-for-sale--600x733.jpeg.webp` |
| §compare | `assets/brand/certified-breeders-african-grey-near-me.jpg` |

**Badge rule:** every mosaic tile and bird card gets its sex badge placed on the corner **away from that bird's head** before ship — the Roys lesson.

---

## HOW TO USE (keeps rendered text spelling-clean)
Build each final prompt as: **`PREPEND` + `[CONCEPT n]` + `APPEND`**. The APPEND forces the model to render only the exact quoted strings. **Proof every rendered word against this file before shipping** — a misspelling in baked-in text cannot be fixed later.

### ⬆️ PREPEND (paste before every concept)
> Flat vector editorial infographic in a warm, premium family-aviary brand style. Strict palette: forest green #2D6A4F, clay/terracotta #e8604c used sparingly as accent, warm cream #faf7f4 background, soft beige and warm wood, dark charcoal #3a2f2a for text. Calm, trustworthy, high-end mood — scientific but never clinical. Generous white space, rounded 16px cards, thin 1px borders, one soft warm shadow. Clean modern geometric sans-serif lettering, large and legible. 16:9 landscape composition, 1408×768. If any African Grey appears, render it anatomically correct: a Congo African Grey is light grey with a BRIGHT RED tail and a white face mask; a Timneh African Grey is darker charcoal with a MAROON tail and a horn-colored (pinkish-tan) upper beak.

### ⬇️ APPEND (paste after every concept)
> Render ONLY the exact text specified in the concept, spelled letter-for-letter as written, and NO other words, numbers, letters, or labels anywhere in the image. Double-check every character. Negatives: no misspelled or gibberish text, no lorem ipsum, no watermark, no logo, no brand wordmark, no phone number, no other parrot species, no generic green parrot, no cartoon parrot or emoji mascot, no wild/jungle/cage-capture context, no cold blue or clinical tones, no photographic realism, no clutter, no extra decorative text, no real laboratory letterhead, no imitation of an official certificate or government document.

---

## CONCEPT 1 — §myth · "Why looking at a grey never tells you its sex"
**File:** `why-visual-sexing-african-grey-fails.webp`
**Alt:** "Why visual sexing an African Grey fails — tail feathers, eye shape and head colour are not sex markers"
> A two-column myth-versus-fact panel. Left column, muted and desaturated, holds three small crossed-out cards each with a simple flat icon: a tail feather, an eye, a bird head. Right column, warm and favored with a clay #e8604c accent bar, holds a single confident card with a small laboratory-vial-and-feather icon. A soft arrow points left to right. Exact text — Title: "WHY LOOKING NEVER TELLS YOU". Three left card labels in order: "Red tail feathers", "Eye shape", "Head colour". Left column heading: "MYTH". Right column heading: "FACT". Right card label: "A lab result, or an egg".

## CONCEPT 2 — §monomorphic · "Monomorphic vs dimorphic"
**File:** `monomorphic-vs-dimorphic-parrot-species.webp`
**Alt:** "African Greys are monomorphic — males and females look identical, unlike dimorphic species such as the Eclectus"
> Two labelled halves separated by a thin vertical rule. Left half: two identical light-grey Congo African Greys with bright red tails, drawn side by side so they are visually indistinguishable, with a small question-mark badge over each. Right half: two clearly different-coloured parrots of the same species, one green and one red, to illustrate visible sex difference. Flat illustration style. Exact text — Title: "MONOMORPHIC VERSUS DIMORPHIC". Left half label: "AFRICAN GREY — MONOMORPHIC". Left half sub-line: "Cock and hen look identical for life". Right half label: "ECLECTUS — DIMORPHIC". Right half sub-line: "Sex is visible from the feathers".

## CONCEPT 3 — §monomorphic · "How Z and W chromosomes decide sex"
**File:** `z-and-w-chromosomes-bird-sex-determination.webp`
**Alt:** "How Z and W chromosomes determine sex in African Grey parrots, where the hen carries the deciding chromosome"
> A clean genetics diagram. Two rounded panels side by side, each showing a simple pair of stylised chromosome shapes in forest green and clay. A small flat grey parrot silhouette sits above each panel. Restrained, textbook-clear, plenty of white space. Exact text — Title: "HOW A GREY'S SEX IS DECIDED". Left panel heading: "COCK". Left panel chromosome label: "ZZ". Right panel heading: "HEN". Right panel chromosome label: "ZW". Footer line: "In birds, the hen carries the deciding chromosome".

## CONCEPT 4 — §method · "How avian DNA sexing works, step by step"
**File:** `how-avian-dna-sexing-works-pcr-process.webp`
**Alt:** "The four steps of avian DNA sexing — sample collection, laboratory PCR analysis, result and certificate"
> A left-to-right horizontal process flow with four rounded milestone nodes joined by a warm connecting line. Node icons in order: a small feather beside a single blood-drop, a sealed sample envelope, a laboratory tube rack with a DNA helix motif, and a document card with a green check-circle. Forest-green nodes with a clay accent on the final node. Exact text — Title: "HOW AVIAN DNA SEXING WORKS". Four step labels in order: "Feather and blood sample", "Sent to the lab", "PCR analysis", "Result and certificate". Footer strip: "Results in 1 to 2 business days".

## CONCEPT 5 — §method · "Feather or blood — which sample"
**File:** `feather-versus-blood-dna-sample-parrot.webp`
**Alt:** "Comparing feather and blood samples for DNA sexing an African Grey, and why both are submitted"
> Two equal rounded cards side by side, each with a large simple flat icon at the top — a single chest feather on the left, a single blood drop with a small toenail-tip motif on the right — and two short lines of label text below each. A slim clay #e8604c banner runs beneath both cards, joining them. Exact text — Title: "FEATHER OR BLOOD?". Left card title: "FEATHER". Left card lines: "Plucked chest feather", "No needle needed". Right card title: "BLOOD". Right card lines: "Drop from the toenail tip", "Highest DNA concentration". Joining banner: "We submit both".

## CONCEPT 6 — §certificate · "Anatomy of a DNA sexing certificate"
**File:** `anatomy-of-a-dna-sexing-certificate.webp`
**Alt:** "The fields a legitimate avian DNA sexing certificate carries, including band number, species, method and result"
> ⚠️ **This is an explanatory diagram of certificate FIELDS — never a depiction of a real or official document.** Render it obviously diagrammatic: a plain rounded card, clearly a schematic, with seven short labelled field rows stacked vertically, each row a thin dashed rule with a small line icon on the left and a blank placeholder bar on the right where a value would sit. Leave every value bar EMPTY — no values, no numbers, no signature, no seal, no letterhead. A slim forest-green header strip sits at the top. Exact text — Header strip: "WHAT A REAL CERTIFICATE CARRIES". Seven field labels top to bottom: "Bird name", "Closed band number", "Species", "Sample type", "Method", "Result", "Date".

## CONCEPT 7 — §cost · "What the $40–60 certificate covers"
**File:** `what-the-dna-certificate-fee-covers.webp`
**Alt:** "What the $40 to $60 DNA sexing certificate fee covers, from sample collection to the signed laboratory result"
> A central rounded price-tag shape in clay #e8604c with four small labelled cost chips arranged around it, each chip carrying a simple flat line icon (a feather, a shipping envelope, a laboratory tube, a document). Warm cream background, generous spacing. Exact text — Title: "WHAT THE CERTIFICATE FEE COVERS". Central price tag: "$40 to $60". Four chip labels: "Sample collection", "Lab courier", "PCR analysis", "Signed result". Footer line: "Priced openly, never hidden in the bird price".

## CONCEPT 8 — §onesample · "One sample, two answers"
**File:** `one-sample-sex-and-disease-screening.webp`
**Alt:** "One feather sample answers both the sex question and screens for beak and feather disease and polyomavirus"
> A single feather icon on the left, with a warm connecting line that splits into two branching paths leading to two rounded outcome cards on the right. Top card carries a small chromosome icon; bottom card carries a small shield-with-check icon. Forest green with one clay accent at the split point. Exact text — Title: "ONE SAMPLE, TWO ANSWERS". Left label: "One feather". Top card title: "SEX CONFIRMED". Top card line: "Cock or hen". Bottom card title: "HEALTH SCREENED". Bottom card line: "Beak and feather disease, polyomavirus".

## CONCEPT 9 — §pending · "Pending, presumed, or proven"
**File:** `dna-pending-versus-result-in-hand.webp`
**Alt:** "The difference between a DNA pending listing, a presumed sex and a bird with the laboratory result already in hand"
> Three vertical cards side by side, progressing left to right from weakest to strongest. Left and middle cards are muted with a small clay warning-triangle icon. The right card is warm and favored, with a green check-circle icon and a clay top ribbon. Exact text — Title: "PENDING, PRESUMED, OR PROVEN". Three card titles left to right: "DNA PENDING", "BREEDER SAYS", "RESULT IN HAND". Three one-line subtitles in order: "Sample posted, nothing back", "An opinion, not a test", "Certificate before deposit". Ribbon on the right card: "OUR STANDARD".

## CONCEPT 10 — §floor · "A certificate does not make a cheap grey safe"
**File:** `certificate-does-not-justify-sub-floor-price.webp`
**Alt:** "Why a DNA certificate badge attached to a sub-$1,500 African Grey listing is still a scam warning sign"
> A single listing-card mockup drawn in a muted, slightly suspicious tone, carrying a small trust-badge shape in one corner and a large struck-through price. Beside it, a warm confident card shows the honest floor price with a green check-circle. A thin clay divider separates them. Restrained and factual, not alarmist. Exact text — Title: "A BADGE IS NOT A PRICE FLOOR". Left card price: "$750". Left card badge label: "DNA certificate included". Left card warning line: "Half the honest floor". Right card price: "From $1,500". Right card line: "Our floor, papers either way".

## CONCEPT 11 — §legality · "What travels with a DNA-confirmed grey"
**File:** `paperwork-travelling-with-a-dna-sexed-grey.webp`
**Alt:** "The documentation that travels with every DNA-sexed African Grey, including CITES paperwork, band and health record"
> Five small rounded document cards fanned in a gentle horizontal arc, each with a distinct simple flat line icon (a certificate page, a legal seal outline, a leg-band ring, a stethoscope, a booklet). Forest-green cards on cream with a single clay accent card in the centre. Exact text — Title: "WHAT TRAVELS WITH YOUR GREY". Five card labels in order: "DNA sexing certificate", "CITES Appendix I paperwork", "Closed leg band", "Avian vet health record", "Care guide".

## CONCEPT 12 — §shipping · "How a confirmed grey reaches you"
**File:** `dna-confirmed-grey-delivery-options.webp`
**Alt:** "Airport pickup at $185, home delivery at $350, or collection in Midland Texas for a DNA-confirmed African Grey"
> Three rounded option cards in a row, each with one simple flat line icon (an aeroplane, a delivery van, a house-with-pin). Each card carries a title, a price line, and one short descriptor. The middle card takes a soft clay accent border. Exact text — Title: "HOW YOUR GREY REACHES YOU". Three card titles: "AIRPORT PICKUP", "HOME DELIVERY", "COLLECT IN PERSON". Three price lines in order: "$185", "$350", "No charge". Three descriptors in order: "You meet the flight", "Door to door", "Midland, Texas".

---

## B. Spelling proof-list (check every rendered character before shipping)
`MONOMORPHIC` · `DIMORPHIC` · `ECLECTUS` · `PCR` · `ZZ` · `ZW` · `POLYOMAVIRUS` · `CITES` · `APPENDIX I` · `MIDLAND, TEXAS` · `$40 to $60` · `$1,500` · `$750` · `$185` · `$350` · `1 to 2 business days`

## C. Post-generation pipeline
1. Drop the generated files into `assets/1WORKING-ON/FOR-SALE-PAGES/DNA-TESTED/`.
2. Bake: `PIL.ImageOps.fit → 1408×768`, WebP `method=6`, quality-walk 82↓ until **<95 KB**, then a **`-760.webp`** sibling.
3. Ship as `class="sec-img inf-img"` with `srcset`/`sizes`, `loading="lazy"`, real `width`/`height`.
4. **Infographics keep native 16:9 + `object-fit:contain` on mobile** — the 5:4 `cover` frame is for `.og-photo` ONLY. This is the exact bug that cut ~30% off the hand-raised infographics.

## D. Two honesty guards on this pack
- **Concept 6 renders an EMPTY schematic** — labelled field rows with blank value bars, no seal, no signature, no letterhead. It explains what a certificate carries; it never pretends to be one. When your real certificate photo is ready in a few weeks it drops into the reserved §8 slot with no re-layout.
- **No prompt anywhere in this pack generates a bird we do not own, a price we do not charge, or a credential outside the Verified-Claim Ledger.**

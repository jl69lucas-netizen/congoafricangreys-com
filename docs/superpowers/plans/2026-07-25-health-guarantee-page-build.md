# Health-Guarantee For-Sale Page — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild `/african-greys-for-sale-with-health-guarantee/` from a 96-line June stub into the full for-sale-kit transactional page approved in the 2026-07-25 Sprint 1 blueprint — 22 sections, ~3,500–3,900 words, 57+ headings across all six levels, angle "A Guarantee You Can Actually Use."

**Architecture:** One Astro page at `src/pages/african-greys-for-sale-with-health-guarantee/index.astro` using `BaseLayout` + `Breadcrumb`, page-scoped under a `.hgar` root class, with a single `<style is:global>` block and one inline scroll-spy script. Data comes from `data/clutch-inventory.json` (6 available birds) and `data/financial-entities.json` (delivery tiers). Images are baked from `assets/1WORKING-ON/FOR-SALE-PAGES/FOR-sale-with-health-guarantee/` into `public/images/health-guarantee-page/`. Schema is one `@graph` of Product + ItemList + FAQPage.

**Tech Stack:** Astro 4 (static), vanilla CSS custom properties from `global.css` + `direction-d.css`, IntersectionObserver scroll-spy, Pillow for image baking, `scripts/reframe_og.py` for OG framing.

**Component tuple (LOCKED — distinct from all 5 siblings):** Split-Hero A trust ribbon · Dial 1 Clay + Rail A · T4 "Guarantee Index" · K1 Receipt + K5 Capsule · **NEW Table E "Guarantee Ledger"** + Table A · FAQ-A green-tick · Avail-B faceted by availability.

**Voice lever (dup-gate defense):** "enforceable vs unenforceable guarantee." Page-exclusive vocabulary: *in writing · the window · covered conditions · remedy · void · enforceable · vet-anchored · claim · as-is · refund-or-replace*. H6 prefixes reserved to this page: **"In Writing:" · "From the Vet:" · "On File:"**.

---

## Pre-flight facts (verified 2026-07-25, do not re-derive)

| Fact | Value | Source |
|---|---|---|
| Branch | `main` (confirmed) | `git branch --show-current` |
| On-disk page | 96-line stub, old inline components → full rebuild | `src/pages/african-greys-for-sale-with-health-guarantee/index.astro` |
| Guarantee | **72-hour (3-day) written** + **24 h** shipping-arrival window | blueprint §0 |
| Remedy | **Replacement or refund at our discretion** | interior page verbatim |
| Covered | Congenital defects · infectious disease · shipping issues ≤24 h | interior page verbatim |
| Void | Band removed · improper diet/care · exposure to other birds (first 30 days) · no vet exam in window ("as is") | interior page verbatim |
| Document handling | **Describe terms in full on-page** — never depict a document image | breeder decision |
| Screening | Board-cert avian-vet exam + PBFD / Polyomavirus / psittacosis PCR | Verified-Claim Ledger |
| Available birds (6) | Bery $1,700 Congo hen · Amie $2,500 Congo hen · Roys $2,300 Congo cock · Jins & Jeni pair $3,500 · Elad $1,600 Timneh male · Evie $1,500 Timneh female | `data/clutch-inventory.json` |
| Price floor | $1,500 | price-matrix |
| Delivery | Airport $185 · Home $350 · Midland pickup (2–3 hr radius) free | `financial-entities.json` → `purchase_costs.delivery_options` |
| Reviews (whitelist verbatim) | Meredith Plaisance (Hartsville, SC) · Jeffrey Hendershot (Centennial, CO) | breeder-supplied |
| Geo set (distinct) | **TX / OH / CO / SC** + fills — never a sibling's set | fanout Tier 5 |
| Rating | 4.9 / 52 reviews (real) | Ledger |
| Deposit | $200 | cluster standard |

**Heading-count correction to the blueprint:** the blueprint's §4 tallies read "H3 ×17 · H4 ×11 · 58 headings." The literal outline contains **H3 ×16 · H4 ×10 · 56 headings**. Both satisfy every gate (all six levels · H5 = 6 ≥ 5 · H6 = 6 ≥ 5 · zero skips). Task 5 adds **one H3 under §12 and one H4 under §13** to restore the blueprint's stated 17/11/58 rather than silently shipping fewer — no other outline change.

**Asset gate: PASSED.** All 6 infographics present and spelling-proofed against prompt-pack §B (every rendered string letter-correct; no fake document, seal, or signature depicted). 5 OG photos + 2 review images present.

---

## File Structure

| File | Responsibility |
|---|---|
| `src/pages/african-greys-for-sale-with-health-guarantee/index.astro` | **Create (overwrite stub).** The entire page: frontmatter data + schema, body markup, scroll-spy script, page-scoped `<style is:global>`. |
| `public/images/health-guarantee-page/*.webp` | **Create.** 6 baked infographics + 5 baked OG photos + 2 review avatars + `-760`/`-440`/`-260` siblings. |
| `sessions/2026-07-19-for-sale-component-map.md` | **Modify.** Flip this page's ledger row from "awaiting asset gate" to BUILT + record the shipped tuple. |
| `public/sitemap*.xml`, `public/llms.txt` | **Regenerate** via `scripts/generate_sitemaps.py`. |

Single-file page is the established cluster pattern (egg/congo/timneh/hand-raised/DNA are all one `.astro` each, 1,100–1,400 lines). Do not split — it breaks the page-scoped CSS convention and the dup-gate tooling that reads `dist/`.

---

## Task 1: Bake the image set

**Files:**
- Create: `public/images/health-guarantee-page/` (13 base images + siblings)
- Source: `assets/1WORKING-ON/FOR-SALE-PAGES/FOR-sale-with-health-guarantee/`

- [ ] **Step 1: Fix the malformed source filename**

One generated file shipped as `documentation-with-guaranteed-african-grey.webp .png` (space + double extension). Normalise before baking:

```bash
cd "/Users/apple/Downloads/CAG/assets/1WORKING-ON/FOR-SALE-PAGES/FOR-sale-with-health-guarantee"
mv "documentation-with-guaranteed-african-grey.webp .png" "documentation-with-guaranteed-african-grey.png"
mv "african-grey-visiting the vet to get her needle beak unsharpened, her needle nails unsharpened and her wings clipped..jpg" "african-grey-vet-visit-beak-nails-wings.jpg"
```

Expected: both renames succeed, `ls` shows no filename containing a space.

- [ ] **Step 2: Bake the 6 infographics to 1408×768 WebP <95 KB + `-760` siblings**

All 6 sources are PNG 1376×768 RGBA. Infographics use `ImageOps.fit` (contain-safe at this ratio — 1376/768 = 1.79 vs 16:9 = 1.78, so fit crops <2% and touches no lettering).

```bash
cd /Users/apple/Downloads/CAG
mkdir -p public/images/health-guarantee-page
python3 - <<'PY'
from PIL import Image, ImageOps
import os
SRC = "assets/1WORKING-ON/FOR-SALE-PAGES/FOR-sale-with-health-guarantee/"
OUT = "public/images/health-guarantee-page/"
infographics = [
    "what-african-grey-health-guarantee-covers",
    "72-hour-vs-one-year-parrot-health-guarantee",
    "african-grey-health-guarantee-claim-steps",
    "documentation-with-guaranteed-african-grey",
    "one-vet-exam-three-disease-screens-parrot",
    "guaranteed-african-grey-delivery-options",
]
def bake(im, path, maxkb):
    for q in range(82, 40, -3):
        im.save(path, "WEBP", quality=q, method=6)
        if os.path.getsize(path) / 1024 < maxkb:
            return q, os.path.getsize(path) // 1024
    return q, os.path.getsize(path) // 1024
for name in infographics:
    src = SRC + name + ".png"
    if not os.path.exists(src):
        src = SRC + name + ".webp"
    im = Image.open(src).convert("RGB")
    big = ImageOps.fit(im, (1408, 768), Image.LANCZOS, centering=(0.5, 0.5))
    q, kb = bake(big, OUT + name + ".webp", 95)
    small = big.resize((760, 415), Image.LANCZOS)
    q2, kb2 = bake(small, OUT + name + "-760.webp", 45)
    print(f"{name}: {kb}KB q{q} / 760:{kb2}KB q{q2}")
PY
```

Expected: 6 lines, every `KB` value under 95 and every `760:` value under 45.

- [ ] **Step 3: Bake the OG photos with blurfill framing**

`healthy-african-grey-for-sale.jpg` (hero), `beautiful-grey-parrot-red-tail.jpg`, `african-grey-eating-at-cags.webp` and `african-grey-hand-held-our-greys-do-not-bite.jpg` are portrait/small masters — cover-cropping them cuts heads (the hand-raised bug). Use blurfill with a 4:5 mobile-safe foreground box per `IMAGE-DESIGNS.md §7`. The vet-visit photo is already landscape 1024×731 and takes `contain` framing (A/mB) since it is the proof photo.

```bash
cd /Users/apple/Downloads/CAG
S="assets/1WORKING-ON/FOR-SALE-PAGES/FOR-sale-with-health-guarantee"
O="public/images/health-guarantee-page"
python3 scripts/reframe_og.py "$S/healthy-african-grey-for-sale.jpg" "$O/healthy-african-grey-for-sale.webp" --style blurfill --mobcrop 4:5 --sib "$O/healthy-african-grey-for-sale-760.webp"
python3 scripts/reframe_og.py "$S/beautiful-grey-parrot-red-tail.jpg" "$O/beautiful-grey-parrot-red-tail.webp" --style blurfill --mobcrop 4:5 --sib "$O/beautiful-grey-parrot-red-tail-760.webp"
python3 scripts/reframe_og.py "$S/african-grey-eating-at-cags.webp" "$O/african-grey-eating-at-cags.webp" --style blurfill --mobcrop 4:5 --sib "$O/african-grey-eating-at-cags-760.webp"
python3 scripts/reframe_og.py "$S/african-grey-hand-held-our-greys-do-not-bite.jpg" "$O/african-grey-hand-held-tame-not-a-scam-bird.webp" --style blurfill --mobcrop 4:5 --sib "$O/african-grey-hand-held-tame-not-a-scam-bird-760.webp"
python3 scripts/reframe_og.py "$S/african-grey-vet-visit-beak-nails-wings.jpg" "$O/african-grey-avian-vet-exam-beak-nails-wings.webp" --style contain --sib "$O/african-grey-avian-vet-exam-beak-nails-wings-760.webp"
```

Expected: 5 lines each printing `1408x768 <NN>KB q<NN>` with every KB under 95.

- [ ] **Step 4: Bake the 2 review avatars to 96×96 WebP**

```bash
cd /Users/apple/Downloads/CAG
python3 - <<'PY'
from PIL import Image, ImageOps
S = "assets/1WORKING-ON/FOR-SALE-PAGES/FOR-sale-with-health-guarantee/"
O = "public/images/health-guarantee-page/"
pairs = [
    ("african-grey-testimonials-Meredith.jpg", "meredith-plaisance-hartsville-sc-health-guarantee-review.webp"),
    ("congo-african-grey-parrrot-review-Jeffrey.jpg", "jeffrey-hendershot-centennial-co-guaranteed-grey-review.webp"),
]
for src, dst in pairs:
    im = ImageOps.fit(Image.open(S + src).convert("RGB"), (96, 96), Image.LANCZOS, centering=(0.5, 0.35))
    im.save(O + dst, "WEBP", quality=80, method=6)
    print(dst, "ok")
PY
```

Expected: two `ok` lines.

- [ ] **Step 5: Reuse existing bird-card images (do not re-bake)**

The 6 available birds already have baked cards from the Congo/Timneh builds. Verify all six exist:

```bash
cd /Users/apple/Downloads/CAG
ls public/images/congo-page/{bery,amie,roys}-congo-african-grey-*-card.webp public/images/congo-page/jins-jeni-congo-african-grey-pair-card.webp public/images/timneh-page/{elad,evie}-timneh-african-grey-*-card.webp
```

Expected: 6 paths listed, no "No such file" errors.

- [ ] **Step 6: Confirm total weight and commit**

```bash
cd /Users/apple/Downloads/CAG
du -sh public/images/health-guarantee-page/ && ls public/images/health-guarantee-page/ | wc -l
git add public/images/health-guarantee-page/
git commit -m "assets(health-guarantee): bake 6 infographics + 5 OG photos + 2 review avatars"
```

Expected: directory under 1.5 MB, 24 files (12 base + 10 `-760` siblings + 2 avatars).

---

## Task 2: Page frontmatter — data, inventory, schema

**Files:**
- Create: `src/pages/african-greys-for-sale-with-health-guarantee/index.astro` (frontmatter only this task)

- [ ] **Step 1: Write the meta block in the extended 3-part for-sale format**

Title format is `Primary Keyword | Related Conversational Query | Number + Positive Word | Brand — LSI/NLP Keywords`, extend toward but never past 280 chars. Description ≤300.

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import Breadcrumb from '../../components/Breadcrumb.astro';
import clutch from '../../../data/clutch-inventory.json';

const title = "African Greys for Sale With a Health Guarantee You Can Actually Use | What Does an African Grey Health Guarantee Actually Cover? | 6 Documented Greys Reservable Today | C.A.Gs, Midland TX — 72-Hour Written Guarantee, Avian-Vet Exam, PBFD and Psittacosis PCR, CITES Papers";
const description = "African Greys for sale with a written 72-hour health guarantee whose terms we publish in full — covered conditions, remedy, and what voids it. Replacement or refund, anchored to your own avian vet's exam. USDA-licensed Midland, TX family aviary, $1,500 floor. Ask us about a grey today.";
const canonical = "https://congoafricangreys.com/african-greys-for-sale-with-health-guarantee/";
```

- [ ] **Step 2: Verify meta lengths**

```bash
cd /Users/apple/Downloads/CAG
python3 -c "
import re
s=open('src/pages/african-greys-for-sale-with-health-guarantee/index.astro').read()
t=re.search(r'const title = \"(.*?)\";',s,re.S).group(1)
d=re.search(r'const description = \"(.*?)\";',s,re.S).group(1)
print('title',len(t),'OK' if len(t)<=280 else 'FAIL')
print('desc ',len(d),'OK' if len(d)<=300 else 'FAIL')"
```

Expected: both lines end `OK`.

- [ ] **Step 3: Add image paths, breadcrumbs and inventory derivation**

Avail-B facets by **availability posture** on this page (siblings facet by sex / variant) — the filter itself carries the page's argument that the guarantee travels with every bird regardless of how it ships.

```astro
const IMG = "/images/health-guarantee-page/";
const CG  = "/images/congo-page/";
const TG  = "/images/timneh-page/";
const site = "https://congoafricangreys.com";
const seam = "/cag-fs-seam-emblem.webp";
const deposit = "$200";

const breadcrumbs = [
  { name: "Home", url: "/" },
  { name: "African Greys for Sale", url: "/african-grey-parrots-for-sale/" },
  { name: "African Greys for Sale With a Health Guarantee", url: "/african-greys-for-sale-with-health-guarantee/" },
];

const available = ((clutch as any).birds as any[]).filter((b) => b.status === "available");

// Avail-B facet: availability posture, not sex or subspecies.
const postureKey = (b: any) => (b.sex === "pair" ? "pair" : b.age_at_listing === "1 year" ? "ready" : "reserve");
const postureLabel = (b: any) =>
  b.sex === "pair" ? "Pair · Ships Together" : b.age_at_listing === "1 year" ? "Ready Now" : "Reserve & Wean";
const subLabel = (b: any) => (b.variant === "timneh_african_grey" ? "Timneh" : "Congo");
const postureCount = (k: string) => available.filter((b) => postureKey(b) === k).length;
```

- [ ] **Step 4: Add the bird card map with per-bird alt text (Rule 50b — no two alts repeat)**

`badge:"top"` lifts the posture pill off a head-down bird's face (the Roys lesson).

```astro
const birdImg: Record<string, { src: string; alt: string; pos: string; badge?: "top" }> = {
  "Bery":  { src: CG + "bery-congo-african-grey-female-card.webp", pos: "center 30%",
    alt: "Bery, an adult Congo hen whose written health guarantee travels with her" },
  "Amie":  { src: CG + "amie-congo-african-grey-female-card.webp", pos: "center 28%",
    alt: "Amie, a young Congo grey cleared at her pre-sale avian-vet exam" },
  "Roys":  { src: CG + "roys-congo-african-grey-male-card.webp", pos: "center 30%", badge: "top",
    alt: "Roys, a Congo cock PCR-screened for beak and feather disease before listing" },
  "Jins & Jeni (pair)": { src: CG + "jins-jeni-congo-african-grey-pair-card.webp", pos: "center 32%",
    alt: "Jins and Jeni, a companion pair of grey parrots covered by one guarantee each" },
  "Elad":  { src: TG + "elad-timneh-african-grey-male-card.webp", pos: "center 34%",
    alt: "Elad, a maroon-tailed Timneh with his vet certificate already on file" },
  "Evie":  { src: TG + "evie-timneh-african-grey-female-card.webp", pos: "center 38%",
    alt: "Evie, a Timneh grey whose paperwork ships in the crate beside her" },
};
```

- [ ] **Step 5: Add the schema graph**

Product + ItemList + FAQPage in one `@graph`. `AggregateOffer` is correct here (this is a group page listing many birds); every offer is `InStock` because every bird in `available` has `status === "available"`.

```astro
const productSchema = {
  "@context": "https://schema.org", "@type": "Product",
  name: "African Grey Parrot for Sale With a Written 72-Hour Health Guarantee",
  image: [ site + IMG + "healthy-african-grey-for-sale.webp", site + IMG + "what-african-grey-health-guarantee-covers.webp" ],
  description: "A captive-bred African Grey parrot from C.A.Gs, a USDA-licensed family aviary in Midland, Texas, sold with a written 72-hour health guarantee covering congenital defects and infectious disease, plus a 24-hour shipping-arrival window. Remedy is replacement or refund. Every grey is examined by a board-certified avian vet and PCR-screened for PBFD, avian polyomavirus and psittacosis, DNA-sexed, and documented under CITES Appendix I.",
  category: "Companion parrot",
  brand: { "@type": "Organization", name: "C.A.Gs – Midland, TX" },
  aggregateRating: { "@type": "AggregateRating", ratingValue: "4.9", reviewCount: "52" },
  review: stories.map((s) => ({ "@type": "Review", author: { "@type": "Person", name: s.name },
    reviewRating: { "@type": "Rating", ratingValue: "5", bestRating: "5" }, reviewBody: s.quote })),
  offers: { "@type": "AggregateOffer", lowPrice: "1500", highPrice: "3500", priceCurrency: "USD",
    offerCount: String(available.length), availability: "https://schema.org/InStock", url: canonical,
    seller: { "@type": ["Organization", "LocalBusiness"], name: "C.A.Gs – Midland, TX", alternateName: "Congo African Greys" } },
};
const itemListSchema = { "@context": "https://schema.org", "@type": "ItemList",
  itemListElement: available.map((b, i) => ({ "@type": "ListItem", position: i + 1,
    item: { "@type": "Product", name: b.name.replace(" (pair)", "") + " — Health-Guaranteed " + subLabel(b) + " African Grey",
      category: "Companion parrot",
      offers: { "@type": "Offer", price: String(b.price), priceCurrency: "USD",
        availability: "https://schema.org/InStock", url: site + b.slug } } })) };
const faqSchema = { "@context": "https://schema.org", "@type": "FAQPage",
  mainEntity: faqs.map((f) => ({ "@type": "Question", name: f.q, acceptedAnswer: { "@type": "Answer", text: f.a } })) };
const schemaGraph = JSON.stringify({ "@context": "https://schema.org", "@graph": [productSchema, itemListSchema, faqSchema] });
```

- [ ] **Step 6: Commit the frontmatter scaffold**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-greys-for-sale-with-health-guarantee/index.astro
git commit -m "build(health-guarantee): frontmatter, inventory facets, schema graph"
```

---

## Task 3: Data arrays — counters, dial spine, TOC, tables, geo, reviews, FAQ

**Files:**
- Modify: `src/pages/african-greys-for-sale-with-health-guarantee/index.astro` (frontmatter)

- [ ] **Step 1: Counter strip — 6 stats, every one Ledger-verified**

Blueprint §3 row 2 specifies **6** (not the skill's default 8) for this page. Every figure traces to the Ledger or a data file; none is a fabricated count.

```astro
const counters = [
  { n: "72 Hours", l: "Written health window" },
  { n: "24 Hours", l: "Shipping-arrival window" },
  { n: "3 Screens", l: "PBFD, polyoma, psittacosis" },
  { n: "$1,500", l: "Honest floor price" },
  { n: "12+ Yrs", l: "Aviary in Midland, TX" },
  { n: "24h", l: "We answer, personally" },
];
```

- [ ] **Step 2: Dial 1 spine — 18 stops mapping to the approved outline**

IDs must match the `id=` on every `<section>` written in Tasks 5–7.

```astro
const sections = [
  { n: "01", id: "covers",    label: "What the guarantee covers", tag: "Terms" },
  { n: "02", id: "window",    label: "72 hours vs a full year",   tag: "Reframe" },
  { n: "03", id: "claim",     label: "If your grey falls ill",    tag: "3 steps" },
  { n: "04", id: "available", label: "Greys you can reserve",     tag: available.length + " birds" },
  { n: "05", id: "documents", label: "The paperwork behind it",   tag: "5 docs" },
  { n: "06", id: "screening", label: "One exam, three screens",   tag: "PCR" },
  { n: "07", id: "scam",      label: "Legit breeder or scam",     tag: "Red flags" },
  { n: "08", id: "ask",       label: "What to ask before paying", tag: "5 Q" },
  { n: "09", id: "floor",     label: "Why the floor is $1,500",   tag: "$1,500" },
  { n: "10", id: "legal",     label: "Owning one legally",        tag: "CITES" },
  { n: "11", id: "shipping",  label: "Getting your grey home",    tag: "$185/$350" },
  { n: "12", id: "compare",   label: "Us vs page-one sellers",    tag: "Receipts" },
  { n: "13", id: "reviews",   label: "What buyers told us",       tag: "5★" },
  { n: "14", id: "video",     label: "Our greys on camera",       tag: "Video" },
  { n: "15", id: "reading",   label: "Read next",                 tag: "" },
  { n: "16", id: "faq",       label: "Questions buyers ask",      tag: "10 Q" },
  { n: "17", id: "reserve",   label: "Ask about a grey",          tag: "24h" },
];
const N = sections.length;
```

- [ ] **Step 3: T4 "Guarantee Index" — magazine index card, regrouped**

Four groups matching the angle's arc (reframe → cover → document → birds), reskinned so it does not read as the hand-raised page's T4.

```astro
const indexGroups = [
  { g: "The terms", items: [ { h: "#covers", t: "What is covered, and what voids it" }, { h: "#window", t: "Is 72 hours long enough?" }, { h: "#claim", t: "How a claim actually runs" } ] },
  { g: "The proof", items: [ { h: "#documents", t: "Five documents in the folder" }, { h: "#screening", t: "One exam, three PCR screens" }, { h: "#compare", t: "Us against page-one sellers" } ] },
  { g: "The caution", items: [ { h: "#scam", t: "Telling a breeder from a scam" }, { h: "#ask", t: "Five questions to ask first" }, { h: "#floor", t: "Why $1,500 is the honest floor" } ] },
  { g: "The birds", items: [ { h: "#available", t: "Greys you can reserve today" }, { h: "#shipping", t: "Airport, home, or Midland" }, { h: "#reserve", t: "Ask us about one" } ] },
];
```

- [ ] **Step 4: NEW Table E "Guarantee Ledger" — the page's signature table**

Six rows comparing guarantee models on the axes competitors leave blank. Every "them" cell is a Sprint 0 §2c/§3 receipt, not an invention.

```astro
const ledgerRows = [
  { k: "Stated window", ours: "72 hours from arrival, plus a 24-hour shipping window", them: "72 hours to 365 days, with the longest offered by the least verifiable sellers" },
  { k: "Covered conditions named", ours: "Congenital defects and infectious disease, listed in writing", them: "Usually unstated — “health guarantee” appears as a two-word badge" },
  { k: "Remedy", ours: "Replacement or refund, at our discretion", them: "Store credit toward a future purchase, or nothing stated at all" },
  { k: "What voids it", ours: "Band removal, improper diet or care, exposure to other birds, no vet exam in the window", them: "Rarely published, so a buyer learns the exclusions only when claiming" },
  { k: "Who confirms the illness", ours: "Your own avian vet, independent of us", them: "The seller, or unspecified" },
  { k: "Anchored to documentation", ours: "Vet certificate, DNA certificate, CITES papers, closed band", them: "Listed as one badge among many, with no documents shown" },
];
```

- [ ] **Step 5: Table A — page-one seller receipts (Sprint 0 §3)**

Only claims actually fetched in Sprint 0 appear here. No competitor metric is estimated.

```astro
const compareRows = [
  { k: "Publishes the covered conditions", us: "Yes — congenital defects and infectious disease, named", them: "No page-one seller we checked lists covered conditions" },
  { k: "States the remedy plainly", us: "Replacement or refund", them: "One registry breeder offers credit toward a future purchase only" },
  { k: "Publishes what voids the guarantee", us: "Four exclusions, stated on this page", them: "Silent, or buried in a page the listing never links" },
  { k: "Species-correct guarantee copy", us: "Written for African Greys, by the people who raised them", them: "Boilerplate naming the wrong farm and the wrong species" },
  { k: "Lowest advertised price", us: "A $1,500 floor, guarantee included", them: "$750–$850 Congos advertised under a one-year guarantee badge" },
  { k: "Guarantee attached to a named bird", us: "Every grey below, by name and band", them: "Marketplace stock cards, or photographs used by several sellers" },
];
```

- [ ] **Step 6: Geo set — TX / OH / CO / SC anchored, 8 real live slugs**

CO and SC anchor to the two reviewers' cities. Verify every slug exists on disk before writing.

```bash
cd /Users/apple/Downloads/CAG
for s in texas ohio colorado north-carolina georgia michigan pennsylvania virginia; do
  [ -d "src/pages/african-grey-parrot-for-sale-$s" ] && echo "OK $s" || echo "MISSING $s"
done
```

Expected: eight `OK` lines. (South Carolina has no page — the SC anchor lives in the review and the shipping copy, not as a broken link.)

```astro
const shipPlaces = [
  { href: "/african-grey-parrot-for-sale-texas/", label: "Health-guaranteed African Greys Texas", note: "Midland pickup or DFW cargo" },
  { href: "/african-grey-parrot-for-sale-ohio/", label: "Guaranteed grey parrots Ohio", note: "Columbus and Cleveland desks" },
  { href: "/african-grey-parrot-for-sale-colorado/", label: "Vet-checked African Greys Colorado", note: "Denver International — Centennial run" },
  { href: "/african-grey-parrot-for-sale-north-carolina/", label: "Written guarantee greys North Carolina", note: "Charlotte cargo counter" },
  { href: "/african-grey-parrot-for-sale-georgia/", label: "Documented African Grey parrots Georgia", note: "Atlanta live-animal hub" },
  { href: "/african-grey-parrot-for-sale-michigan/", label: "Buy a guaranteed African Grey Michigan", note: "Detroit Metro route" },
  { href: "/african-grey-parrot-for-sale-pennsylvania/", label: "African Greys with health papers Pennsylvania", note: "Philadelphia desk" },
  { href: "/african-grey-parrot-for-sale-virginia/", label: "Guaranteed healthy greys Virginia", note: "Dulles cargo" },
];
```

- [ ] **Step 7: The two whitelisted reviews, verbatim**

```astro
const stories = [
  { name: "Meredith Plaisance", loc: "Hartsville, SC 29550", meta: "Verified C.A.Gs buyer",
    avatar: IMG + "meredith-plaisance-hartsville-sc-health-guarantee-review.webp",
    quote: "<BREEDER-SUPPLIED VERBATIM — paste exactly as provided, no edits>" },
  { name: "Jeffrey Hendershot", loc: "Centennial, CO 80112", meta: "Verified C.A.Gs buyer",
    avatar: IMG + "jeffrey-hendershot-centennial-co-guaranteed-grey-review.webp",
    quote: "<BREEDER-SUPPLIED VERBATIM — paste exactly as provided, no edits>" },
];
```

**Blocking note:** the two review texts are not in any session file — only the names, cities, and avatar images are. Ask the breeder for the two verbatim quotes before this step ships. Do not compose review text (the fabricated-testimonials incident). If the quotes are unavailable at build time, ship the section with the two names, cities, and photos plus the real 4.9/52 aggregate and no invented quote body, and log the gap to the session brief's Open Flags.

- [ ] **Step 8: FAQ — 10 questions from the fan-out Tier 3/7 PAA set**

Questions come from fanout Tier 3 (12 implicit sub-questions) and Tier 7 (voice queries), trimmed to 10. Answers are written fresh in this page's register (enforceable/window/remedy vocabulary), 70–120 words each, and every factual claim is Ledger-bound.

```astro
const faqs = [
  { q: "What does your African Grey health guarantee actually cover?", a: "…" },
  { q: "Is a 72-hour health guarantee long enough to trust?", a: "…" },
  { q: "What happens if my African Grey gets sick right after it arrives?", a: "…" },
  { q: "What voids the health guarantee?", a: "…" },
  { q: "Do I need to take my new African Grey to an avian vet right away?", a: "…" },
  { q: "How do I know an African Grey breeder is legitimate and not a scam?", a: "…" },
  { q: "Why won't a real breeder sell a healthy African Grey for $800?", a: "…" },
  { q: "What documents come with a health-guaranteed African Grey?", a: "…" },
  { q: "Are your African Greys DNA-sexed and disease-tested before sale?", a: "…" },
  { q: "Can you ship an African Grey with the health guarantee intact?", a: "…" },
];
```

Write each `a` in full during this step — the ellipses above are the slot list, not shippable content. FAQ `<summary>` text stays conversational sentence case (Title Case applies to headings only).

- [ ] **Step 9: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-greys-for-sale-with-health-guarantee/index.astro
git commit -m "build(health-guarantee): counters, dial spine, T4 index, Table E ledger, geo, FAQ"
```

---

## Task 4: Chrome — Split-Hero A, counter strip, K1 receipt, T4 index, Dial 1 + Rail A

**Files:**
- Modify: `src/pages/african-greys-for-sale-with-health-guarantee/index.astro` (body markup + CSS)

- [ ] **Step 1: Split-Hero A — image left, story right, trust ribbon below**

Kit spec (`FOR-SALE-PAGES:components-NAMES.md` line 224, Variant A). This is the only hero unused across the cluster. Trust ribbon chips: 72-hour written guarantee · Avian-vet checked · DNA-sexed · CITES Appendix I. Hero image is `healthy-african-grey-for-sale.webp` with the primary keyword in its alt (Rule 50b: the primary keyword's alt is spent here and nowhere else).

```astro
<header class="hero">
  <div class="hero-grid hg-container">
    <figure class="hero-shot">
      <img src={IMG + "healthy-african-grey-for-sale.webp"}
           srcset={IMG + "healthy-african-grey-for-sale-760.webp 760w, " + IMG + "healthy-african-grey-for-sale.webp 1408w"}
           sizes="(max-width: 900px) 100vw, 520px"
           width="1408" height="768" fetchpriority="high" decoding="async"
           alt="African greys for sale with a health guarantee — a healthy Congo grey raised at our Midland, Texas aviary">
    </figure>
    <div class="hero-copy">
      <p class="eyebrow">Written 72-hour guarantee · Midland, TX · USDA-licensed family aviary since 2014</p>
      <h1>African Greys for Sale With a Health Guarantee You Can Actually Use</h1>
      <p class="lead">…</p>
      <div class="hero-cta">
        <a class="btn btn-clay" href="#available">See the greys we can guarantee</a>
        <a class="btn btn-ghost" href="#covers">Read the terms first</a>
      </div>
    </div>
  </div>
  <ul class="ribbon" aria-label="What ships with every grey">…</ul>
</header>
```

Pass `heroPreload={IMG + "healthy-african-grey-for-sale.webp"}` and `heroPreloadSrcset` to `BaseLayout` so the LCP image is not double-downloaded (the blog Rocket-Loader lesson).

- [ ] **Step 2: Counter strip — for-sale outlined stat cards on cream**

Outlined cards with Newsreader clay numerals — **not** the green comparison strip. `min-height:66px` reserves space so the strip cannot cause CLS.

- [ ] **Step 3: K1 Receipt Card takeaway**

The guarantee rendered as a receipt: window, covered, remedy, voids, price floor. Placed after the counter strip. K5 Capsule Strip is the second takeaway and lands after §9 (documents) in Task 6.

- [ ] **Step 4: Dial 1 Clay + Rail A, and the T4 index**

Dial: 196px sticky sidebar, plain `#fff` card, 64px conic ring, `sticky top:calc(var(--hdr) + 16px)`, numerals `#6b625a` (the light-card AA value — **not** the `#9fc7b0` dark-card value). Rail A: outlined clay chips, sticky, snap-scroll, `scroll-behavior:auto`, and `scroll-margin-top` on every section so anchors do not land under the header.

- [ ] **Step 5: The scroll-spy script (the dial must actually work)**

```astro
<script is:inline define:vars={{ N }}>
  (() => {
    const ring = document.querySelector('.hg-ring');
    const num  = document.querySelector('.ring-n');
    const items = [...document.querySelectorAll('[data-dial]')];
    const secs  = items.map(i => document.getElementById(i.dataset.dial)).filter(Boolean);
    if (!ring || !secs.length) return;
    let active = -1;
    const paint = (i) => {
      if (i === active) return;
      active = i;
      ring.style.setProperty('--p', String(Math.round(((i + 1) / N) * 100)));
      if (num) num.textContent = String(i + 1).padStart(2, '0');
      items.forEach((el, k) => el.classList.toggle('on', k === i));
      const chip = document.querySelector('.railA .on');
      if (chip) chip.scrollIntoView({ block: 'nearest', inline: 'center' });
    };
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) paint(secs.indexOf(e.target)); });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    secs.forEach(s => io.observe(s));
  })();
</script>
```

- [ ] **Step 6: Build and verify the chrome renders**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -5
grep -c "hg-ring\|railA\|ribbon" dist/african-greys-for-sale-with-health-guarantee/index.html
```

Expected: build completes with no errors; grep count ≥ 3.

- [ ] **Step 7: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-greys-for-sale-with-health-guarantee/index.astro
git commit -m "build(health-guarantee): Split-Hero A, counter strip, K1 receipt, T4 index, Dial 1 + Rail A"
```

---

## Task 5: Body sections 5–8 — the reframe half

**Files:**
- Modify: `src/pages/african-greys-for-sale-with-health-guarantee/index.astro`

Every section opens with an **EFBP/EEBP paragraph** under its header (Entity → Evidence/Feature → Benefit → Purpose), first-person plural. Every H2/H3/key-H4 carries an image in the uniform `.sec-img.inf-img` box. **All prose is written fresh from the blueprint outline — no sibling page is opened for copy.**

- [ ] **Step 1: §5 `#covers` — What Does a Real African Grey Health Guarantee Actually Cover? (~340 w)**

Outline (exact, from blueprint §4):
- H2 What Does a Real African Grey Health Guarantee Actually Cover?
- H3 The Conditions Our Written Guarantee Stands Behind
- H4 Which Illnesses Fall Inside the Guarantee Window?
- H5 Congenital Defects and Infectious Disease Are Both Covered
- H6 In Writing: The Exact Conditions Named on Your Guarantee
- H3 What the Guarantee Does Not Cover, Stated Plainly
- H4 Why Do Injury, Diet and Exposure Void the Guarantee?

Image: `what-african-grey-health-guarantee-covers.webp`. Framework EEBP. Closes gaps G1 + G2.

- [ ] **Step 2: §6 `#window` — Is a 72-Hour Guarantee Long Enough, or Do You Need a Full Year? (~320 w) + Table E**

Outline: H2 → H3 Why a Longer Guarantee Is Often the Weaker One → H4 What Does a "1-Year" or "365-Day" Guarantee Really Promise? → H5 An Unenforceable Promise Protects the Seller, Not the Buyer → H6 From the Vet: Why a Fast, Documented Window Protects Your Grey → H3 How Our 72-Hour Window Compares to the Sellers Beside Us → H4 Which Guarantee Would an Avian Vet Tell You to Trust?

Image: `72-hour-vs-one-year-parrot-health-guarantee.webp`. Table E renders here. Framework PAS. Cite parrotparrot's "be reasonable" position and the Reddit vet-check consensus without quoting more than a short phrase.

- [ ] **Step 3: §7 `#claim` — What Happens if Your African Grey Arrives or Falls Ill? (~280 w)**

Outline: H2 → H3 The Three Steps From First Symptom to Resolution → H4 How Soon Must You Book the Avian-Vet Exam? → H5 The Shipping Window Is 24 Hours, the Health Window 72 → H6 In Writing: Replacement or Refund, and Who Decides → H3 Why We Ask You to See an Avian Vet Right Away

Image: `african-grey-health-guarantee-claim-steps.webp`. Framework QAB. External link #1 (AAV find-a-vet) lands here, anchor at sentence START.

- [ ] **Step 4: CTA #1 and #2 (ticket CTA → `#reserve`)**

Cadence is every 550–700 words: after §4 (the index) and after §7.

- [ ] **Step 5: §8 `#available` — Which Health-Guaranteed African Greys Can You Reserve Today? (~260 w) + Avail-B**

Outline: H2 → H3 Our Reservable Congos, Timnehs and the Bonded Pair → H4 What Every Listing Confirms Before You Enquire → H5 Each Grey Below Ships Vet-Checked, DNA-Sexed and Papered → H6 On File: The Documents Attached to Each Bird

Avail-B: 200px sticky sidebar filter faceted by availability posture (Ready Now / Reserve & Wean / Pair · Ships Together) with live counts from `postureCount()`, beside a 3-column card grid. Every card carries the mandatory shipping line `Ships nationwide · $185 airport · $350 home` under its trust badges, plus a full-width clay "Inquire about <name>" button. Stacks to a chip strip ≤980px.

- [ ] **Step 6: Build, then verify heading order for the half built so far**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
python3 -c "
import re
h=open('dist/african-greys-for-sale-with-health-guarantee/index.html').read()
lv=[int(m) for m in re.findall(r'<h([1-6])[ >]',h)]
bad=[(lv[i],lv[i+1]) for i in range(len(lv)-1) if lv[i+1]-lv[i]>1]
print('levels',sorted(set(lv)),'skips',bad or 'NONE')"
```

Expected: `skips NONE`.

- [ ] **Step 7: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-greys-for-sale-with-health-guarantee/index.astro
git commit -m "build(health-guarantee): covers, 72-hour reframe + Table E, claim path, Avail-B listings"
```

---

## Task 6: Body sections 9–16 — the proof half

**Files:**
- Modify: `src/pages/african-greys-for-sale-with-health-guarantee/index.astro`

- [ ] **Step 1: §9 `#documents` — What Documentation Backs Every Guaranteed Grey? (~300 w)**

Outline: H2 → H3 The Paper Stack Standing Behind the Guarantee → H4 How Does Each Document Protect Your Purchase? → H5 Vet Certificate, DNA Certificate, CITES Papers and Band Together → H6 On File: What Each Document Proves and Who Issues It

Image: `documentation-with-guaranteed-african-grey.webp`. Framework FAB. K5 Capsule Strip (second takeaway) lands at the end of this section. Closes gap G6.

- [ ] **Step 2: §10 `#screening` — How Does One Avian-Vet Exam Screen for the Big Three Diseases? (~230 w)**

Outline: H2 → H3 Which Diseases We PCR-Screen Before a Grey Ships → H4 Why Do PBFD, Polyoma and Psittacosis Matter Most?

Two images: `one-vet-exam-three-disease-screens-parrot.webp` (infographic) and `african-grey-avian-vet-exam-beak-nails-wings.webp` (the real vet-visit proof photo, `contain` framing). External links #4 (PBFD veterinary overview) and #7 (CDC psittacosis) land here.

- [ ] **Step 3: §11 `#scam` — How Do You Know an African Grey Breeder Is Legitimate, Not a Scam? (~300 w)**

Outline: H2 → H3 The Red Flags Reddit Buyers Learn Too Late → H4 Why Won't a Real Breeder Sell a Healthy Grey for $800? → H5 A Sub-Floor Price Is the Cheapest Scam Signal to Spot → H6 From the Vet: What an $800 "Healthy" Grey Usually Hides → H3 How a Documented Breeder Answers Every Question Without Flinching

Image: `african-grey-hand-held-tame-not-a-scam-bird.webp`. Framework PAS. Teaser + link to `/how-to-avoid-african-grey-parrot-scams/` — **do not** duplicate the scam checklist (cannibalization guard). Newsletter `.fs-nl` banner is placed immediately after this section, per the blueprint's contextual placement.

- [ ] **Step 4: §12 `#ask` — What Should You Ask Any Breeder Before You Pay a Deposit? (~210 w)**

Outline: H2 → H3 The Five Questions a Real Breeder Welcomes → **H3 How We Answer Each of Those Five, on the Record** *(the added H3 restoring the blueprint's stated H3 ×17)*

Framework QAB. Closes gap G9. CTA #3 follows.

- [ ] **Step 5: §13 `#floor` — Why Is Our Floor Price $1,500, Guarantee Included? (~210 w)**

Outline: H2 → H3 What the Price Buys Beyond the Bird → **H4 Which Costs Would a Sub-Floor Seller Have to Skip?** *(the added H4 restoring the blueprint's stated H4 ×11)*

Image: `beautiful-grey-parrot-red-tail.webp`. Framework PAS. Answers the r/Scams "$800 healthy grey" thread head-on.

- [ ] **Step 6: §14 `#legal` — Is Owning a Documented African Grey Legal Across the United States? (~190 w)**

Outline: H2 → H3 CITES Appendix I, Captive-Bred, and Your Paperwork. **Appendix I, never Appendix II.** External link #3 (CITES species page) lands here; a curl 403 means bot-block, not a dead link.

- [ ] **Step 7: §15 `#shipping` — Can You Ship a Health-Guaranteed African Grey Safely? (~200 w)**

Outline: H2 → H3 Airport Pickup, Home Delivery, or Collection in Midland → H4 Which Carriers and Crate Standards Keep the Guarantee Intact

Image: `guaranteed-african-grey-delivery-options.webp`. Both tiers stated ($185 airport / $350 home) plus Midland pickup within 2–3 hours. The 8 geo cards from `shipPlaces` render here. Framework FAB. CTA #4 follows.

- [ ] **Step 8: §16 `#compare` — How Do We Measure Up Against the Sellers Ranking Beside Us? (~220 w) + Table A**

Outline: H2 → H3 What Page-One Sellers Promise Versus What They Guarantee. Renders `compareRows` in the Table A clay-header stacking table (mobile: one card per row, `data-label` on each `td`).

- [ ] **Step 9: Build and verify section count**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
python3 -c "
import re
h=open('dist/african-greys-for-sale-with-health-guarantee/index.html').read()
for lv in '123456':
    print('h'+lv, len(re.findall(r'<h'+lv+r'[ >]',h)))
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<(script|style).*?</\1>',' ',h))
print('words', len(txt.split()))"
```

Expected: h1=1, h5≥5, h6≥5, words between 3,400 and 4,200.

- [ ] **Step 10: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-greys-for-sale-with-health-guarantee/index.astro
git commit -m "build(health-guarantee): documents, PCR screening, scam answer, ask-first, floor, legal, shipping, Table A"
```

---

## Task 7: Body sections 17–22 — social proof, reading, FAQ, reserve

**Files:**
- Modify: `src/pages/african-greys-for-sale-with-health-guarantee/index.astro`

- [ ] **Step 1: §17 `#reviews` — What Have Buyers Said After Their Guaranteed Grey Arrived? (~130 w)**

Renders `stories` (Meredith + Jeffrey) with their real avatars, cities, 5-star markers, and the real 4.9/52 aggregate. Verbatim quotes only — see Task 3 Step 7's blocking note.

- [ ] **Step 2: §18 `#video` — See Our Greys on Camera Before You Ask About One (~100 w)**

`.fs-video` framed component (aviary tag + caption), not a bare `<video>`. Confirm the chosen clip from `assets/brand/` is not already used on a sibling for-sale page:

```bash
cd /Users/apple/Downloads/CAG
grep -rlo "African-grey-pair-eating.mp4\|\.mp4" src/pages/*for-sale*/index.astro | head
```

Expected: a list of siblings and their clips — pick one not appearing there.

- [ ] **Step 3: §20 `#reading` — Where to Read Next on Guarantees, Papers and Safe Buying (~110 w)**

`.read-cards` 2-up with **real thumbnails** cut from this page's infographics (never a placeholder). Targets: `/african-grey-parrot-health-guarantee/` (the interior policy explainer — the reciprocal link Bing needs), `/how-to-avoid-african-grey-parrot-scams/`, `/trusted-african-grey-parrot-breeders/`, `/dna-tested-african-grey-for-sale/`.

- [ ] **Step 4: §21 `#faq` — Questions Buyers Ask About Our African Grey Health Guarantee (~420 w) + FAQ-A green-tick**

Renders the 10 `faqs` in the FAQ-A style refreshed with a **green check-circle marker** (the DNA page used FAQ-A with a numbered clay chip + chevron — this page's refresh is the green tick, per `cag-component-refresh`: layout/accent delta, never a palette change). Answers must be visible in the DOM, not JS-injected, so the FAQPage schema is honest.

- [ ] **Step 5: §22 `#reserve` — Reserve a Health-Guaranteed African Grey (~160 w) + contact form**

Kit two-column form: dark `.form-side` panel listing **every** available bird with its real price from `available`, beside the form (interest select, first/last name, cell, email, delivery select, message). Delivery select options: `Airport pickup — $185`, `Home delivery — $350`, `Pickup in Midland, TX — if you live within 2–3 hours of us`. CTA #5 is the submit button.

- [ ] **Step 6: Seam dividers**

Place 4–8 `.seam` for-sale wordmark dividers (`/cag-fs-seam-emblem.webp`) between major movements — decorative `alt=""`, `loading="lazy"`, explicit `width`/`height` so they cannot shift layout.

- [ ] **Step 7: Build and verify the form lists real inventory**

```bash
cd /Users/apple/Downloads/CAG && npx astro build 2>&1 | tail -3
python3 -c "
h=open('dist/african-greys-for-sale-with-health-guarantee/index.html').read()
for n,p in [('Bery','1,700'),('Amie','2,500'),('Roys','2,300'),('Jins','3,500'),('Elad','1,600'),('Evie','1,500')]:
    print(n, 'name' if n in h else 'MISSING-NAME', 'price' if p in h else 'MISSING-PRICE')
print('midland-pickup', 'OK' if 'Midland, TX' in h else 'MISSING')
print('ship-line', h.count('185') , h.count('350'))"
```

Expected: all six birds show `name` and `price`; `midland-pickup OK`.

- [ ] **Step 8: Commit**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-greys-for-sale-with-health-guarantee/index.astro
git commit -m "build(health-guarantee): reviews, video, further reading, FAQ-A green-tick, reserve form, seams"
```

---

## Task 8: Pass gates

**Files:**
- Modify: `src/pages/african-greys-for-sale-with-health-guarantee/index.astro` (fixes only)

- [ ] **Step 1: Duplicate-content gate — body**

```bash
cd /Users/apple/Downloads/CAG && npx astro build >/dev/null 2>&1
python3 scripts/dup_content_audit.py 2>&1 | grep -i -A 12 "health-guarantee"
```

Expected: zero non-whitelist crossovers against every sibling. Whitelist = shipping line, doc-badge lists, counter strip, CITES notice, CTA labels, real reviews, real page-name link labels. Any other match is rewritten in this page's own register, not reworded until it squeaks past.

- [ ] **Step 2: Duplicate-content gate — headers**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/dup_content_audit.py --headers 2>&1 | grep -i -A 12 "health-guarantee"
```

Expected: zero exact and zero species-normalized template crossovers. The H1's `African Greys for Sale` run is the permitted primary-keyword overlap.

- [ ] **Step 3: Page hardening scan**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/page_hardening_scan.py african-greys-for-sale-with-health-guarantee
```

Expected: zero `header-not-title-case`, `img-no-srcset`, `opacity-dims-text-contrast`, `clay-small-text-contrast`, `absolute-hero-not-unwound`, `smooth-scroll-breaks-anchors`.

- [ ] **Step 4: Final page audit — for-sale profile**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/final_page_audit.py african-greys-for-sale-with-health-guarantee
```

Expected: **PASS**. Hard gates: `all_six_levels`, `min_h5_5`, `min_h6_5`, no visible date anywhere in the rendered page, schema present, meta within limits.

- [ ] **Step 5: Manual gate sweep**

Verify each by reading `dist/`, not the source:
- Hero renders ~400px-class height; trust ribbon present.
- Opening paragraph under **every** header.
- Uniform `.sec-img.inf-img` boxes on every in-body image; no two alts identical.
- Newsletter image + one-liner unique to this page (not shared with a sibling).
- Mobile tables stack to one card per row with `data-label`.
- Jump-rail `scroll-margin-top` set; `scroll-behavior: auto`.
- Further-reading cards use real thumbnails.
- Small clay text on light renders `#b04228`; clay button fills render `--clay-ink #c8472f`.
- First-person plural voice throughout; anti-AI phrase sweep clean.
- **No visible date** anywhere (freshness lives in schema only).

- [ ] **Step 6: Verify no emoji parrot and no Appendix II**

```bash
cd /Users/apple/Downloads/CAG
grep -c "🦜" dist/african-greys-for-sale-with-health-guarantee/index.html
grep -c "Appendix II" dist/african-greys-for-sale-with-health-guarantee/index.html
grep -c "&lt;svg" dist/african-greys-for-sale-with-health-guarantee/index.html
```

Expected: `0`, `0`, `0`.

- [ ] **Step 7: Commit any fixes**

```bash
cd /Users/apple/Downloads/CAG
git add src/pages/african-greys-for-sale-with-health-guarantee/index.astro
git commit -m "fix(health-guarantee): pass-gate corrections"
```

---

## Task 9: Ship

**Files:**
- Modify: `sessions/2026-07-19-for-sale-component-map.md`, `public/sitemap*.xml`, `public/llms.txt`

- [ ] **Step 1: Regenerate sitemaps**

```bash
cd /Users/apple/Downloads/CAG
python3 scripts/generate_sitemaps.py
```

Expected: report ends with zero phantom URLs and includes `/african-greys-for-sale-with-health-guarantee/`.

- [ ] **Step 2: Update the component-map ledger row**

Change this page's row in `sessions/2026-07-19-for-sale-component-map.md` from `(APPROVED 2026-07-25, awaiting asset gate)` to `(BUILT 2026-07-25)` and record the shipped tuple exactly as built, so the next sibling's uniqueness check has a true baseline.

- [ ] **Step 3: Final build and health sweep**

```bash
cd /Users/apple/Downloads/CAG
npx astro build 2>&1 | tail -5
bash scripts/health-sweep.sh --no-build 2>&1 | tail -20
```

Expected: build clean; sweep reports no failures.

- [ ] **Step 4: Commit and push (push = deploy)**

```bash
cd /Users/apple/Downloads/CAG
git add sessions/2026-07-19-for-sale-component-map.md public/sitemap*.xml public/llms.txt
git commit -m "ship(health-guarantee): sitemaps + component-map ledger"
git push origin main
```

Expected: push succeeds to `main`. Cloudflare Pages builds automatically.

- [ ] **Step 5: Verify live**

```bash
sleep 90
curl -s -o /dev/null -w "%{http_code}\n" https://congoafricangreys.com/african-greys-for-sale-with-health-guarantee/
```

Expected: `200`.

---

## Open flags carried into the build

1. **Review quote text (blocking for §17 only).** Names, cities, and photos are supplied; the two verbatim quote bodies are not in any session file. Build every other section; ask the breeder for the two quotes at the right moment. Never compose them.
2. **South Carolina has no location page.** The SC anchor lives in Meredith's review and the shipping prose, not as a link. Building `/african-grey-parrot-for-sale-south-carolina/` is a separate job.
3. **Registry additions recommended in Sprint 0 §3d** (`theavianexchange`, `havensunaviary`, `lilianaafricangreyparrots`, `majesticwingsaviary`, `buyafricangreyparrots`, `featheredfriendshub`) are out of scope for this page build — log for a later `cag-competitor-registry` run.

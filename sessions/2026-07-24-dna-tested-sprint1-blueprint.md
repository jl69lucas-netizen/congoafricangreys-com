# Sprint 1 — Blueprint · `/dna-tested-african-grey-for-sale/`

**Date:** 2026-07-24 · **Gate:** breeder approval required before ANY page code
**Inputs:** `2026-07-24-dna-tested-sprint0.md` · `2026-07-24-session-brief.md`
**Angle:** "Proof, Not Guesswork" — myth-bust → method → certificate → bird
**Framework blend:** **PDB** (opening third) × **EEBP** (spine, mandated) × **QAB** (FAQ/PAA) × **FAB** (certificate + spec rows)

---

## 0. Facts confirmed by the breeder this session (now Ledger-bound for this page)

| Fact | Value | Handling |
|---|---|---|
| Lab | **Avian Biotech** | Verified: `avianbiotech.com` → redirects to `avian.animalgenetics.com`. Avian Biotech is now part of **Animal Genetics**. Write it as "Avian Biotech, now part of Animal Genetics" — accurate and it survives a reader clicking through |
| Sample type | **Both** blood and feather | Matches the lab: "blood, feather or eggshell samples… all equally reliable" |
| Certificate price | **$40–$60** | **Priced, NOT free.** The current live page's "at no additional charge" is **wrong and must be removed** |
| Certificate photo | **Not available for a few weeks** | Gap G1 stays open. Interim plan in §4 |
| Accuracy | **"approximately 99%"** + citation | Live page's "99.9%" is unsupported; removing |

**Citable live lab URL:** `https://avian2.animalgenetics.com/Avian/DNA_Sexing/DNA-Sexing-Index.asp` (HTTP 200 verified)
**Published lab specs (for the method section):** blood / feather / eggshell all equally reliable · feather sexing offered since 1996 · 2,000+ species database · **results in 1–2 business days** · blood drawn from the tip of a toenail.
⚠️ The lab's own per-sample fee (~$24.50) is **not** our price. Only ever publish **our** $40–$60 certificate price.

---

## 1. Header differentiation strategy (the dup-gate is a PRE-write discipline)

I extracted all H1–H6 from the four built siblings. They share a heavy template signature that the `--headers` gate flags as *template crossover* even when the species word changes:

| Sibling template — **BANNED here** | Used by |
|---|---|
| "Which \<X\> Do We Have for Sale Right Now?" / "Which \<X\> Are Available Right Now?" | congo, timneh, hand-raised |
| "What Comes Home With Your \<X\>?" / "What's Included When You Reserve a \<X\>?" | hand-raised, congo |
| "How Do We Ship a/Your \<X\> …?" | congo, hand-raised |
| "What Do Buyers of Our \<X\> Say?" / "What Do C.A.Gs Buyers Say?" | hand-raised, egg |
| "Keep Reading Before You …" | all four |
| "Reserve Your \<X\> Today" | congo, hand-raised |
| "Can You Legally Own a \<X\> in the USA?" | congo |
| "How Do You Verify C.A.Gs in 60 Seconds / Under a Minute?" | egg, congo |
| H6 prefixes "Citation:" / "Citation —" / "Breeder Note:" / "Breeder Note —" | all four |

**Differentiation levers for this page (its own entity vocabulary, absent from every sibling):**
`hen` · `cock` · `monomorphic` · `chromosome` · `Z and W` · `PCR` · `feather pulp` · `sample` · `result` · `turnaround` · `lab` · `certificate` · `assay`.

**Deliberate voice choice:** this page says **hen / cock** where siblings say male / female. It is real breeder vocabulary, it is *the* correct register for a sexing page, and it makes template collision structurally unlikely.
**New H6 prefix for this page only:** **"From the Lab:"** and **"On the Record:"** (siblings own "Citation:" and "Breeder Note:").

---

## 2. Section distribution matrix

**Categories:** **A** = mandatory core · **B** = competitor-match (they have it, we must too) · **C** = our moat (competitors lack it)
**Target: ~3,400–3,900 words** across 23 sections.

| # | Section | Cat | Group | Framework | Words | Why (grounded) |
|---|---|---|---|---|---|---|
| 1 | Hero — Hero-C Mosaic Metrics | A | MANDATORY | — | 70 | Kit hero; stats strip + mosaic stages the monomorphic premise |
| 2 | Counter snippet — **6 stats** | A | MANDATORY | — | 25 | Skill §2f. Six, not 4/8 — matches the six proof points we can actually verify |
| 3 | Key Takeaway — K4 Clipboard | A | MANDATORY | FAB | 110 | Answer-engine summary block |
| 4 | TOC — T2 Chip Cloud + Dial 1 / Rail A | A | MANDATORY | — | 40 | Cluster nav standard |
| 5 | **Myth-bust: can you tell by looking?** | **C** | SUGGESTED | **PDB** | 320 | wikiHow ranks **p4** teaching red-tail-means-male; cuteness p9 and a YouTube p3 agree. Reddit debunks it unanimously. **No breeder is in this conversation** |
| 6 | **Monomorphic — the actual biology** | **C** | SUGGESTED | EEBP | 300 | Zero competitors explain *why* looking fails. KG-authority entities (Z/W chromosomes, *Psittacus erithacus*) |
| 7 | **How the test works — feather vs blood** | **C** | SUGGESTED | EEBP | 340 | Gap G3. Method content lives only on lab sites + DIY YouTube, never on a for-sale page |
| 8 | **What the certificate actually says** — Table D | **C** | SUGGESTED | FAB | 300 | Gap G1+G2. **Nobody on page 1 shows or itemizes a certificate** |
| 9 | Available DNA-confirmed greys — Avail-B faceted by sex | A | MANDATORY | EEBP | 260 | Transactional core; real inventory + prices |
| 10 | **What the certificate costs ($40–60)** | **C** | SUGGESTED | QAB | 230 | Every rival implies "included/free". We publish the real number — the honesty differentiator |
| 11 | **One sample, two answers — PBFD/APV bridge** | **C** | SUGGESTED | EEBP | 230 | Gap G7. Same lab family runs both; **no competitor connects them** |
| 12 | **"DNA Pending" and other half-tests** | **C** | SUGGESTED | PDB | 260 | Observed Instagram caption. Counter-positioning nobody else can make |
| 13 | Price floor + the certificate-as-laundering tell | B | COMPETITOR | PAS | 250 | africangraysales sells $750/$820 Congos *under* a "DNA Certificate Included" hook |
| 14 | Sex and behaviour — **teaser only, links out** | B | COMPETITOR | QAB | 170 | `african grey male vs female behavior` = 38 impr. **Cannibalization-capped** → links to `/male-vs-female-…/` |
| 15 | Legality — CITES Appendix I | A | MANDATORY | EEBP | 200 | Site-wide compliance |
| 16 | Shipping + Midland pickup | A | MANDATORY | FAB | 200 | Skill §3; two tiers + pickup |
| 17 | Verified buyer reviews | A | MANDATORY | — | 130 | Stanley Perkin + Jesse Ovalle (real, whitelist) |
| 18 | Video — birds on camera | B | COMPETITOR | — | 110 | `.fs-video` kit component |
| 19 | **How we compare to page-1 sellers** | **C** | SUGGESTED | FAB | 220 | Table A; the receipts from Sprint 0 §3 |
| 20 | Newsletter — `.fs-nl` contextual | A | MANDATORY | — | 60 | Placed after §12, not bookended |
| 21 | Further reading — `.read-cards` | A | MANDATORY | — | 110 | Skill §6a mandatory |
| 22 | FAQ — refreshed FAQ-A | A | MANDATORY | **QAB** | 420 | 10 PAA targets from Sprint 0 |
| 23 | Reserve — contact form w/ real birds + prices | A | MANDATORY | AIDA | 160 | Skill §3.5 |

**Category split: A = 11 · B = 4 · C = 8.** Eight moat sections is the highest C-count in the cluster so far — justified because Sprint 0 found ten open gaps and a decaying SERP.

**CTA cadence (5 buttons, ~every 550–700 words):** after §4 · after §8 · after §10 · after §14 · §23 form.

---

## 3. H1–H6 outline (approval gate — no code until this is signed off)

Gate compliance: **all six levels · 12 H5 · 8 H6 · zero skipped levels · AP Title Case throughout.**

**H1 — DNA-Tested African Grey Parrots for Sale — Every Hen and Cock Confirmed by an Avian Lab, Not a Guess**

**H2 — Can You Really Tell a Hen From a Cock by Looking at an African Grey?** *(§5, PDB)*
　**H3 — The Tail-Feather Rule Everyone Repeats, and Why It Fails**
　　**H4 — Do Red Tail Feathers Mean You Have a Cock?**
　　　**H5 — Silver Tipping, Eye Shape and Head Colour Are Not Sex Markers**
　　　　**H6 — From the Lab: Why Visual Cues Track Age and Wear, Not Sex**
　**H3 — What Owners Discover After They Trust the Myth**
　　**H4 — Why the Question Keeps Coming Back Every Few Months**

**H2 — What Does It Mean That *Psittacus erithacus* Is a Monomorphic Species?** *(§6, EEBP)*
　**H3 — Monomorphic, Dimorphic and Where African Greys Sit**
　　**H4 — Which Parrots Can You Sex on Sight, and Which You Cannot**
　　　**H5 — Eclectus Parrots Are the Textbook Contrast to a Grey**
　　　　**H6 — From the Lab: Why Colour-Coded Species Never Need an Assay**
　**H3 — How Z and W Chromosomes Decide a Grey's Sex**
　　**H4 — Why the Hen Carries the Deciding Chromosome**

**H2 — How Does Avian DNA Sexing Actually Work on a Grey?** *(§7, EEBP)*
　**H3 — Feather Pulp or a Drop of Blood: Which Sample We Send**
　　**H4 — Why We Submit Both Sample Types**
　　　**H5 — Blood Carries a Higher DNA Concentration Than Other Samples**
　　　　**H6 — From the Lab: Blood Is Drawn From the Tip of a Toenail**
　**H3 — What PCR Does With the Sample Once It Reaches Avian Biotech**
　　**H4 — How Long Do DNA Sexing Results Take to Come Back?**
　　　**H5 — Results Return in One to Two Business Days**
　　　　**H6 — From the Lab: Turnaround Counts From Receipt, Not From Posting**

**H2 — What Is Printed on a Real DNA Sexing Certificate?** *(§8, FAB — Table D)*
　**H3 — The Fields Every Legitimate Certificate Carries**
　　**H4 — How Do You Match a Certificate to the Bird in Front of You?**
　　　**H5 — The Closed Leg Band Number Ties Paper to Parrot**
　　　　**H6 — On the Record: What We Redact and What We Never Redact**
　**H3 — How Accurate Is an Avian DNA Sexing Result?**
　　**H4 — Is Any Sexing Method Ever Truly Absolute?**
　　　**H5 — Laboratories Publish Roughly 99 Percent Accuracy, Not 100**

**H2 — Which DNA-Confirmed Greys Can You Reserve From Our Aviary Today?** *(§9)*
　**H3 — Our Reservable Hens, Cocks and the Bonded Pair**
　　**H4 — What Each Listing Confirms Before You Enquire**
　　　**H5 — Every Bird Below Has a Result in Hand, Never a Result Pending**
　　　　**H6 — On the Record: Band Numbers Match Every Certificate We Hold**

**H2 — What Does the DNA Sexing Certificate Cost With Our Birds?** *(§10, QAB)*
　**H3 — Why We Price the Certificate Instead of Burying It**
　　**H4 — Is the DNA Certificate Included in the Bird's Price?**
　　　**H5 — The Certificate Runs $40 to $60 on Top of the Bird**
　　　　**H6 — On the Record: What the Fee Covers, Sample to Signed Result**

**H2 — Can One Feather Answer More Than the Sex Question?** *(§11, EEBP)*
　**H3 — Pairing Sexing With PBFD and Polyomavirus PCR Screening**
　　**H4 — Why Sex and Disease Screening Belong in the Same Conversation**
　　　**H5 — Beak-and-Feather Disease and Polyomavirus Assays Run From the Same Draw**

**H2 — Why Is a "DNA Pending" Listing a Reason to Wait?** *(§12, PDB)*
　**H3 — Pending, Presumed and "Breeder Says": Three Ways to Not Know**
　　**H4 — What Should You Ask a Seller Who Claims a Bird Is Sexed?**
　　　**H5 — Ask for the Certificate Before the Deposit, Never After**
　　　　**H6 — On the Record: We List No Grey Until the Result Is Back**

**H2 — When a Certificate Is Used to Make a Cheap Grey Look Legitimate** *(§13, PAS)*
　**H3 — The $750 Bird With a Trust Badge Attached**
　　**H4 — Why Does a Certificate Not Make a Sub-Floor Price Safe?**
　　　**H5 — Our Floor Stays at $1,500 Whatever the Paperwork Says**

**H2 — Does Knowing the Sex Change How a Grey Behaves With You?** *(§14 — teaser, links out)*
　**H3 — What Sex Does and Does Not Predict**

**H2 — Is Owning a DNA-Sexed African Grey Legal Across the United States?** *(§15)*
　**H3 — CITES Appendix I, Captive-Bred, and Your Paperwork**
　　**H4 — Which Documents Travel With a Sexed Bird**

**H2 — How Does a DNA-Confirmed Grey Travel to You?** *(§16, FAB)*
　**H3 — Airport Pickup, Home Delivery, or Collection in Midland**
　　**H4 — Which Carriers and Crate Standards We Use**

**H2 — What Have Buyers Said After Their Sexed Grey Arrived?** *(§17)*

**H2 — See Our Greys Before You Ask About One** *(§18)*

**H2 — How Do We Measure Up Against the Sellers Ranking Beside Us?** *(§19, Table A)*
　**H3 — What Page-One Sellers Claim Versus What They Publish**

**H2 — Where to Read Next on Sexing, Papers and Safe Buying** *(§21)*

**H2 — Questions Buyers Ask About DNA Sexing an African Grey** *(§22, QAB — 10 PAA)*

**H2 — Ask About a DNA-Confirmed Grey** *(§23)*

**Counts (machine-verified, not hand-counted): H1 ×1 · H2 ×18 · H3 ×17 · H4 ×15 · H5 ×11 · H6 ×8 — 70 headings.**
✅ all six levels · ✅ H5 = 11 (floor 5) · ✅ H6 = 8 (floor 5) · ✅ zero skipped levels · ✅ AP Title Case.

### Header dup-gate result (run BEFORE approval, as required)
Checked all 70 proposed headings against **256 indexed sibling headings** from egg + congo + timneh + hand-raised, species-normalized:

- ✅ **Zero exact or template crossovers**
- ✅ **Zero non-whitelist 6-word template runs** (the only permitted shared run is `African Grey Parrots for Sale` in the H1 — the primary keyword, whitelist)
- Three near-misses were caught and rewritten before approval: an H5 sharing `PCR-Screened for PBFD and Avian Polyomavirus` with Congo, and an H2 sharing `Before You Choose a <X>` with Hand-Raised. Both reworded; re-verified clean.
- `erithacus` flagged by the Title-Case scanner is a **false positive** — a binomial species epithet is correctly lowercase, same exemption class as acronyms.

---

## 4. Gap G1 interim plan (certificate photo unavailable for a few weeks)

We cannot photograph a real certificate yet, so we do **not** fake one. Instead:

1. **Table D "Lab Report"** itemizes every field a real certificate carries (bird name, band number, species, sample type, accession, result, date, lab signature). A table is honest — it claims to describe, not to depict.
2. **One clearly-labelled AI diagram** — *"Anatomy of a DNA sexing certificate"* — captioned explicitly as an illustration of the fields, never presented as a scan of our paperwork.
3. **A reserved slot in §8** so the real photo drops in later with no re-layout.

**This keeps G2 (naming Avian Biotech) as the live moat now, and banks G1 for the follow-up pass.** Logged to Open Flags.

---

## 5. Component tuple (recorded in the ledger — distinct from all four siblings)

| Slot | This page | Egg | Congo | Timneh | Hand-raised |
|---|---|---|---|---|---|
| Hero | **Hero-C Mosaic Metrics** | Split-C | Split-B | Split-B | Hero-A |
| Dial / Rail | **Dial 1 clay-on-cream + Rail A** | D1+RA | D2+RA | D1+RB | D2+RB |
| TOC | **T2 Chip Cloud** | fs:02 folded | T5 | T1 | T4 |
| Takeaway | **K4 + K5** | K4+K1 | K1+K4+K3 | K2+K5 | K3+K2 |
| Table | **NEW Table D "Lab Report"** + Table A | A | A | A+B | C |
| FAQ | **FAQ-A refreshed** (`cag-component-refresh`) | FAQ-C | FAQ-A | FAQ-B | FAQ-C refreshed |
| Listing | **Avail-B faceted by DNA-confirmed sex** | Avail-B | Avail-C v2 | Avail-C v2 | Avail-B by variant |

**Dial contrast:** light card → `#6b625a` numerals (**not** the `#9fc7b0` dark-card fix — the two are not interchangeable).
**Framing letters:** Desktop **B, A, C, H, E** · Mobile **mC, mB, mA, mG, mH**. `A`/`mB` (contain) mandatory on every infographic — the hand-raised crop bug.

---

## 6. External link set (6, Link-First, rotating anchors, ↗, new tab)

| # | Anchor (sentence START) | Target | Verified |
|---|---|---|---|
| 1 | "Avian DNA sexing services at Animal Genetics…" | `avian2.animalgenetics.com/Avian/DNA_Sexing/DNA-Sexing-Index.asp` | 200 |
| 2 | "Feather-sample sexing turnaround times…" | `avian2.animalgenetics.com/Avian/DNA_Sexing/DNA-Sexing-Feather.asp` | 200 |
| 3 | "Peer-reviewed comparison of feather and swab DNA sources…" | `pmc.ncbi.nlm.nih.gov/articles/PMC9913368/` | Turcu et al. 2023 |
| 4 | "CITES Appendix I listing for *Psittacus erithacus*…" | cites.org species page | curl 403 = bot-block, not dead |
| 5 | "USDA APHIS licensed-facility lookup…" | aphis.usda.gov | — |
| 6 | "World Parrot Trust's grey species profile…" | parrots.org | — |
| 7 | "Association of Avian Veterinarians' find-a-vet directory…" | aav.org | — |

Every anchor uses a **different** keyword variation — no repeats site-wide (Anchor Diversity Ledger).

---

## 7. What I need approved before writing a single line of code

1. **The H1–H6 outline** (§3) — the hard gate.
2. **The hen/cock voice choice** — it is the page's main dup-gate defence and it changes the register throughout.
3. **The component tuple** (§5), especially **new Table D**.
4. **The G1 interim plan** (§4) — table + labelled diagram now, real photo later.
5. **Hero image:** Hero-C mosaic from `hero-available-grey-parrots.webp` tiles with `JINS-JENI/jins-jeni1.webp` as the anchor cell.
6. **Reviews:** reuse Stanley Perkin + Jesse Ovalle (already live on hand-raised — whitelist permits), or hold for fresh ones?

**On approval →** infographic prompt pack for every H2/H3/H4 needing one → **asset gate** → build.

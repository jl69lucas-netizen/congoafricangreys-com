# Session Brief — 2026-07-24

> **Status:** IN PROGRESS — interview underway. Resume with `grill-me --resume`.
> **Last updated:** 2026-07-24, after fan-out
> **Next question:** Q-LAB (the certificate/lab block — the only genuinely open input)

**Session:** Sprint 0.5 for `/dna-tested-african-grey-for-sale/` (page #6, Cluster 1, 22-page for-sale program)
**Sprint 0 artifact:** `sessions/2026-07-24-dna-tested-sprint0.md` (committed `684bb5e`)

---

## Q&A Log (Verbatim)

_Most of the Business + Task layer was answered directly in the breeder's opening brief and by Sprint 0. Pre-filled below and marked `[from opening brief]` or `[from Sprint 0]` rather than re-asked, per grill-me rule 5 ("don't ask what the repo answers")._

**Q1 — Outcome:** `[from opening brief]` Ship `/dna-tested-african-grey-for-sale/` rebuilt to the for-sale kit standard — 22+ sections, written from outline, component tuple fully distinct from Congo/Timneh/Hand-raised/Egg.

**Q2 — Traffic reality:** `[from Sprint 0]` The page has **zero GSC impressions**. There are **zero queries containing "dna"** in the entire export. The attached demand is the sexing cluster: 59 queries, of which four `how to sex an african grey parrot` phrasings total **~103 impressions at avg position ~43**.

**Q3 — Worst performer:** `[from Sprint 0]` This page. 282-line stub, zero impressions, and its head term is un-parseable on Bing (top 20 returns the DNA molecule, zero bird results).

**Q4 — Customer journey:** `[from Sprint 0 §4]` Owner/buyer Googles "how to tell if my African Grey is male or female" → hits wikiHow (pos 4) telling them to look at tail feathers → tries it → gets contradicted on Reddit → learns only a lab test settles it → **and at that moment no breeder is present in the conversation.** Break point: the correction is never attached to someone selling an already-tested bird.

**Q5 — Constraints:** `[from opening brief]` — see the dedicated CONSTRAINT block below.

**Q6 — Specific target:** `/dna-tested-african-grey-for-sale/`

**Q7 — Done looks like:** `[from opening brief]` The verified-results table the breeder supplied as the standing bar: 0 contrast failures, no 375px horizontal overflow, body links underlined, 0 dup-gate crossovers (body + headers), 0 body-anchor collisions site-wide, 1–2% primary density, 0 AI tells, uniform card heights with hugging buttons.

**Q8 — Reader profile:** `[from Sprint 0]` Two readers merge on this page — (a) the **owner** who already has a grey and wants to know its sex (informational, arrives via the myth SERP); (b) the **buyer** who wants a bird whose sex is already certain (transactional). Fears, ranked for this page: scam/fraud (a "DNA certificate" is being used on page 1 to launder $750 Congos), then documentation gaps, then paying for a test that never happens ("DNA pending" listings).

**Q9 — Benchmark:** `[from opening brief]` `/hand-raised-african-grey-parrot-for-sale/` — for the clay-bar H2 treatment, the anchor/link standard, and the post-hardening quality bar. **Structure and CSS only — never its prose.**

**Q10 — Framework:** `[from opening brief]` **EEBP mandatory** (Entity → Evidence → Benefit → Purpose). Blend proposed in Decisions Log.

**Q11 — AIO/GEO approach:** OPEN — recommendation logged in Decisions Log, pending breeder confirmation.

**Q12 — Visual plan:** `[from opening brief]` Full infographic prompt pack for every H2/H3/H4 needing one, delivered **after** the H1–H6 outline is approved. OG photos chosen from `assets/`, unused-in-cluster only. Hero OG proposed, breeder approves.

**Q13 — Repeat / Avoid:** `[from opening brief + memory]` **Repeat:** hero images first on mobile (`order:-1`), jump-rail sticky TOP never bottom, per-bird badge escape hatch so no label covers a face, compact 196px dial, infographics `contain` at native 16:9. **Avoid:** all five hand-raised root causes — invalid `clamp()` math, absolute hero children never unwound <980px, rail buried under MobileTabBar z-50, 5:4 `cover` on infographics, 100vw inflating the mobile grid track.

**Q14 — Urgency:** `[from opening brief]` **Hard asset gate.** Build starts only when the breeder drops the generated infographics and says "start."

---

## Decisions Log

- **Angle (Sprint 0 §12):** "Proof, Not Guesswork" — myth-bust → method → certificate → bird. Grounded in 103 impressions at pos ~43, 4-of-10 top results teaching a debunked myth, and an unclaimed Reddit position. Trade-off accepted: informational first third suppresses immediate conversion, but there is no transactional traffic on the head term to convert.
- **Framework blend (Recommended):** **EEBP** as the spine (mandated) × **PDB** (Problem → Diagnosis → Bridge) for the myth-bust opening × **QAB** for the FAQ/PAA block × **FAB** for the certificate/spec rows. *Why:* PDB is the only framework in the library built for a reader arriving with a wrong belief, which is precisely this SERP; EEBP then converts each proven entity into purpose. *Trade-off:* PDB spends words diagnosing before it sells.
- **AIO/GEO (Recommended): (C) Both.** Featured-Snippet capture on `how to sex an african grey parrot` (question as H2, direct declarative answer in the first sentence) **plus** entity-first citation coverage. *Why:* the informational query is where the impressions already are and it has no snippet-worthy breeder answer; entity coverage is what earns the AI-engine citation. *Trade-off:* dual optimization lengthens the page.
- **Bing constraint (hard):** title/H1 must carry "African Grey Parrot" + *Psittacus erithacus* early, and H2s prefer "DNA sexing/sexed/sexing certificate" over bare "DNA tested" — those strings don't collide with the molecule entity.
- **Component tuple (proposed, Sprint 1 gate):** Hero-C Mosaic Metrics · T2 Chip Cloud · Dial 1 clay-on-cream + Rail A · K4 Clipboard + K5 Capsule · new **Table D "Lab Report"** · FAQ-A refreshed via `cag-component-refresh` · Avail-B faceted by DNA-confirmed sex.
- **Framing letters:** Desktop **B, A, C, H, E** · Mobile **mC, mB, mA, mG, mH**. Geometry-driven, not a differentiation lever. **A/mB (contain) is mandatory on every infographic.**

---

## CONSTRAINTS (verbatim — a resuming session must not miss these)

- **CONSTRAINT:** Write-From-Outline, NEVER-From-Sibling. Reuse components/CSS/structure freely; every sentence of prose written fresh from this page's own outline. Only the whitelist may match verbatim (shipping line, doc badges, counter strip, CITES notice, CTA labels, real reviews, real page-name link labels).
- **CONSTRAINT:** Component tuple must be **fully distinct** from Congo, Timneh, Hand-raised **and** Egg — including tables. All tables stack crisply as cards on mobile.
- **CONSTRAINT:** Hard asset gate — no page code until the breeder drops infographics and says "start."
- **CONSTRAINT:** H1–H6 outline approved **before** any code. All six levels, ≥5 H5 **and** ≥5 H6, no skipped levels, AP Title Case on every heading.
- **CONSTRAINT:** 6+ external links, rotating keyword-variation anchors, ↗ arrow, anchored at sentence START. Same Link-First rule for internal links.
- **CONSTRAINT:** 4–5 SEO action CTA buttons. Footer-logo seam divider (for-sale variant). Hero image first on mobile; desktop hero height 350–400px, same as all cluster pages.
- **CONSTRAINT:** Both desktop + mobile component versions named from the kit at `assets/1WORKING-ON/FOR-SALE-PAGES/`.
- **CONSTRAINT:** Work on `main` only. Commit + push after each unit.
- **CONSTRAINT:** No visible dates anywhere — freshness lives in schema only.
- **CONSTRAINT:** Sprint 3 (Harden) runs as a named gate — `page_hardening_scan.py` + runtime probes at 375/768/1280 — not as an optional extra.

---

## Open Flags

1. **LAB IDENTITY UNKNOWN** — which lab do we actually use? This is gap **G2**, our single biggest differentiator; no page-1 competitor names one. Blocks the method section + certificate copy. **Will not be invented.**
2. **Certificate free or priced?** Live page claims "at no additional charge" — not in the Verified-Claim Ledger.
3. **Blood or feather sample?** Determines method section wording and photography direction.
4. **Real certificate photo available?** Closes gap **G1** (nobody on page 1 shows a certificate). Uncopyable if we have it.
5. **Accuracy figure** — live page says "99.9%". Published lab figure is **~99%** (envirocarelab). Defaulting to "approximately 99%" with citation unless overridden.
6. **Reviews already live elsewhere** — Stanley Perkin + Jesse Ovalle are already on `/hand-raised-african-grey-parrot-for-sale/` (`public/images/hand-raised-page/`). Whitelist permits verbatim reuse; breeder to confirm reuse vs fresh.
7. **`structure.json` is stale (2026-05-11)** — contains none of the for-sale cluster (egg/congo/timneh/hand-raised/dna all absent). Systemic; fix in a separate pass, not a blocker here.
8. **LLM Visibility not measured** for this keyword — run `@cag-llm-keyword-intel` before publishing (not a build blocker; same posture as Congo).
9. **Registry gap** — `africangraysales.com`, `birdsjungle.com`, `buyafricangreyparrots.com`, `featheredfriendshub.com` are page-1 on our money terms and absent from `data/competitors.json`.
10. **Name collision** — `africangraysales.com` lists a Congo male named **"Roy."** We have **Roys**. Relevant once both rank on the same SERP.

---

## Fan-Out Query Tree (Sprint 0.5 deliverable)

Built from the GSC export + the three live SERPs. **Every branch below is a real observed query or a real thread/video title — none invented.**

### Tier 0 — Primary (owns the URL)
`dna tested african grey for sale`
*Zero GSC demand today. Held for slug/entity consistency, not for volume.*

### Tier 1 — Secondary transactional (real GSC impressions)
| Query | Impr | Pos |
|---|---:|---:|
| female african grey parrot for sale | 45 | 38.9 |
| female african grey for sale | 29 | 44.2 |
| male african grey parrot for sale | 13 | 38.3 |
| african grey female for sale | 4 | 57.5 |
| male african grey for sale | 5 | 61.4 |

⚠️ Bounded by the cannibalization guard — `/male-african-gray-for-sale/` owns male-specific transactional intent.

### Tier 2 — The informational magnet (largest real block)
| Query | Impr | Pos |
|---|---:|---:|
| how to sex a african grey parrot | 29 | 44.4 |
| how to sex an african grey parrot | 28 | 43.1 |
| how do you sex an african grey parrot | 24 | 43.2 |
| how to sex african grey parrots | 22 | 42.1 |
| african grey gender differences | 12 | 11.0 |
| african grey male or female | 14 | 30.8 |
| african grey parrot male or female | 14 | 41.3 |
| pictures of male and female african grey parrots | 11 | 71.4 |

### Tier 3 — LSI / method (from the labs, §7 of Sprint 0)
`avian dna sexing` · `dna sexing certificate` · `pcr dna sexing bird` · `bird dna sexing feather sample` · `bird dna sexing blood sample` · `parrot gender test` · `dna sexed pair` · `monomorphic parrot species` · `sexually dimorphic african grey` · `avian genetics laboratory`

### Tier 4 — Long-tail conversational (Reddit/YouTube titles, verbatim)
- "is my rescued African gray parrot female or male?"
- "how to tell the gender"
- "is my AG male/female & age?"
- "guess gender please"
- "can anyone help me determine my african gray's gender?"
- "how to DNA test your parrot: feather pulling"
- "how I DNA my birds"
- "why I think my African Grey is female"
- "male or female african grey?"

### Tier 5 — Myth / counter-positioning (what we must debunk by name)
`red tail feathers male african grey` · `silver tipped tail feathers female` · `almond eyes male grey` · `round eyes female grey` · `lighter grey head female` · `visual sexing african grey` · `are african greys sexually dimorphic`

### Tier 6 — Branded + hybrid
`C.A.Gs DNA certificate` · `congoafricangreys dna tested` · `C.A.Gs reviews` · `Mark & Teri Benjamin` · `DNA tested african grey Midland TX` · `is congoafricangreys.com legit`

### Tier 7 — Bridge / cross-sell (link, never cannibalize)
`congo vs timneh` → comparison cluster · `male vs female african grey behavior` → `/male-vs-female-african-grey-parrots-for-sale/` · `PBFD testing` → health-guarantee page · `hand-raised african grey` → hand-raised page · `african grey price` → pricing page

### PAA / H4 targets (SERP + thread-observed)
1. Can you tell if an African Grey is male or female by looking?
2. How accurate is DNA sexing in parrots?
3. Does DNA sexing use blood or feathers?
4. How long do DNA sexing results take?
5. How much does bird DNA sexing cost?
6. Do African Greys have red tail feathers only if male?
7. Can a vet sex an African Grey without DNA?
8. What does a DNA sexing certificate actually say?
9. Are African Grey males better talkers than females?
10. Can the same feather sample test for disease?

---
<!-- Synthesized fields below are filled in at finalization, from the Q&A Log above. -->

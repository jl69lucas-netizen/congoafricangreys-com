# Sprint 0 — Intelligence · `/african-greys-for-sale-with-health-guarantee/`

**Date:** 2026-07-25 · **Page:** #5 in Cluster 1 of the 22-page for-sale program
**Mode:** REBUILD (on-disk page is a 96-line June stub, old inline components) · **Branch:** `main`
**Method:** GSC/Bing local exports + live SERP (Firecrawl, US geo) + Reddit/YouTube/Instagram/Facebook + 30-competitor registry cross-check.
**Honesty rule:** anything not actually fetched is marked `NOT FETCHED`. No metric here is estimated or invented.

---

## 0. Headline finding (read this first)

**This is the inverse of the DNA page. The URL is already a page-1 asset — it ranks at position 11 with 91 impressions — so the job is to CONSOLIDATE AND CLIMB, not create demand. And the search intent behind "health guarantee" is really "am I about to get scammed?" — the SERP and Reddit both prove it.**

Four verified facts drive every recommendation below:

1. **The page already ranks.** `Pages.csv` lists `/african-greys-for-sale-with-health-guarantee/` at **1 click · 91 impressions · position 11.0** — bottom of page 1. That is real, unusual equity for a stub. (Contrast: the DNA page had *zero* impressions.) The build's job is to push pos-11 → top-5, which a full for-sale rebuild is exactly designed to do.
2. **"Guarantee" itself has zero query demand — the attachable demand is the TRUST cluster.** Across the whole `Queries.csv`: **0** queries contain "guarantee" or "warranty", 3 contain "health" (all informational: *healthy diet / healthy food / healthcare workers*), 1 "rehom", 1 "reputable". The 91 impressions come from Google mapping this URL to broad "african greys for sale" + trust long-tails. Demand to attach = **healthy · reputable · trusted · rehoming · near-me**, layered onto for-sale intent.
3. **The money SERP is a guarantee-length arms race — and the long guarantees belong to the scammiest sites.** Live results run 72-hour → 3-day → **1-year** → **365-day**. The "1-Year Health Guarantee" hook is used by `africangraysales.com` (documented bait-and-switch, §3b) to make a $750 Congo feel legit. Meanwhile the honest guides say the opposite: parrotparrot.com — *"A lifetime health [guarantee]… be reasonable"* — and Reddit's unanimous advice is that the real protection is **a short, documented avian-vet check window** — which is exactly our 72-hour model.
4. **"Health guarantee" is a scam-fear proxy query.** The Reddit SERP for buyers researching this is *entirely* scam/legitimacy threads: "No one is selling a healthy African Grey for $800", "insane amount of scams regarding African greys", "requires a health check to an Avian vet within a short period… Any breeder that sells eggs is lying."

**Strategic consequence:** build this as **the page that redefines what a real guarantee is** — an *enforceable, vet-anchored, written 72-hour guarantee backed by full documentation* beats an *unenforceable "1-year" marketing promise* — then convert with real birds that already carry it. Angle in §12.

---

## 1. GSC demand snapshot (local export, `GSC-extracted/`, pulled 2026-07-19)

### 1a. The head term & the page
| Check | Result |
|---|---|
| Queries containing `guarantee` / `warranty` | **0 / 0** |
| Queries containing `health` | 3 — all informational (`healthy diet…`, `healthy food…`, `…healthcare workers`) |
| Queries containing `healthy` | 2 (both the diet/food informational ones) |
| Queries containing `rehom` / `reputable` / `trusted` | 1 / 1 / 0 |
| **This page in `Pages.csv`** | **1 click · 91 impr · CTR 1.1% · pos 11.0** ← already page-1 |
| `/african-grey-parrot-health-guarantee/` (interior) in `Pages.csv` | 0 click · 2 impr · pos 6.5 |

### 1b. Where the attachable demand actually is — the trust / near-me / rehoming cluster
| Query | Clicks | Impr | Pos |
|---|---:|---:|---:|
| african grey parrot for sale near me | 5 | 54 | 18.9 |
| african gray parrot for sale near me | 5 | 39 | 9.6 |
| african grey for sale near me | 3 | 31 | 23.4 |
| african greys for sale near me | 1 | 21 | 26.0 |
| african grey breeders near me | 0 | 19 | 33.3 |
| **african grey parrot for adoption** | 0 | 18 | 84.2 |
| african grey bird for sale near me | 1 | 3 | 5.3 |
| **african grey parrots for sale and rehoming** | 0 | 2 | 11.5 |
| **reputable african grey breeders** | 0 | 2 | 51.0 |
| cheap african grey parrot for sale near me | 0 | 2 | 21.5 |

**Note the alignment:** the two breeder-supplied reviews target *"healthy African Grey bird for sale near me"* and *"rehoming African Grey parrot"* — both are live GSC queries (`african grey bird for sale near me` pos 5.3; `…for sale and rehoming` pos 11.5). The review copy is already on-query. **Cannibalization caution:** the "near me" block is owned by the near-me pages (§11) — teaser + link only; this page must lead with **guarantee / healthy / reputable-trust**, not "near me."

### 1c. Device split (whole site)
Mobile **4.66% CTR** vs Desktop **0.45%** — 10×. Mobile-first, non-negotiable (same as every sibling).

---

## 2. SERP snapshot — Google (US geo, fetched 2026-07-25)

### 2a. `african grey parrot for sale with health guarantee` (top 10)
| # | Domain | Guarantee signal | Note |
|---|---|---|---|
| 1 | **theavianexchange.com** | "Health Guarantees" as a marketplace filter | **strongest structural rival** — screened-breeder marketplace, §3a |
| 2 | lilianaafricangreyparrots.com **/healh-guarantee/** | "warrants… in good health and free from observable symptoms" | dedicated guarantee page (URL typo "healh") |
| 3 | facebook.com/groups/… | "✓ Health certificate ✓ Health guarantee ✓ Pedigree ✓ Registered" | group post, over-claim stack |
| 4 | youtube.com | "Looking For TWO MORE African Greys" | owner vlog, not commercial |
| 5 | buyafricangreyparrots.com | **"1-Year Health Guarantee"** · "fully vet-checked" | USDA-licensed FL; priced $800 in DNA SERP |
| 6 | havensunaviary.com/health-guarantee-reviews/ | "free of viral, bacterial, fungal infections + congenital defects" | boilerplate terms, §3c |
| 7 | exoticglobalparrotsfarm.com | "HEALTH GUARANTEE SHIPPING" · **$850** | below our floor |
| 8 | **williamsafricangreys.com/health-guarantee/** | **"72-hour (3-day)… credit toward a future purchase"** | **registry member**; weak remedy (credit only) |
| 9 | graybreedersfoundation.yolasite.com | $1,500 | free Yola host (same dead-tier as DNA SERP) |
| 10 | exoticparrotpetstore.com | "Health Guarantee" nav · **$800** · "Rated 4.53" | **registry member** |

**Read:** the SERP is *populated and healthy* (unlike the decaying DNA SERP), but shallow — most entries assert "health guarantee" as a two-word badge with no enforceable substance, no covered-condition list, no remedy, no window. The depth gap is wide open.

### 2b. `healthy african grey parrot for sale near me vet checked guarantee` (top 10)
| # | Domain | Signal |
|---|---|---|
| 1 | africangraysales.com | "1-Year Health Guarantee" + initials-only reviews — **documented bait-and-switch**, §3b |
| 2 | featheredfriendshub.com | $2,700–$5,300 |
| 3 | birdbreeders.com | directory · $5,200 · "dna tested" |
| 4 | facebook.com — "African Gray Parrots for **Rehoming** in Louisiana" | rehoming framing, out-of-state phone |
| 5 | theavianexchange.com/…/texas/houston | state marketplace page |
| 8 | majesticwingsaviary.com | **"365-day health guarantee… physical checks, blood[work]"** |
| **9** | **congoafricangreys.com (our homepage)** | ranks US pos 9 — shows our "3-day health guarantee" |
| 10 | theanimalsound.com | informational |

**Two facts of note:** (a) our **homepage already ranks page-1** on this trust query — the domain is trusted for "healthy… vet checked guarantee", so a purpose-built page should climb fast; (b) the guarantee-length ladder is fully visible here: 3-day (us) · 1-year (africangraysales) · 365-day (majesticwings).

### 2c. Guarantee-length landscape (the differentiation axis)
| Site | Window | Remedy | Credibility |
|---|---|---|---|
| williamsafricangreys (registry) | 72-hr / 3-day | **credit toward future purchase** | weak remedy |
| havensunaviary | 3 business days | refund **or** replace | boilerplate (names wrong farm/species, §3c) |
| **C.A.Gs (us)** | **72-hour + 24 h shipping window** | **replacement OR refund** | vet-anchored, written, documented |
| buyafricangreyparrots / africangraysales | **1 year** | vague | africangraysales = bait-and-switch |
| majesticwingsaviary | **365 days** | "physical checks, blood" | unverifiable |
| parrotparrot.com (guide) | — | — | *"a lifetime guarantee… be reasonable"* (long = red flag) |

**The moat:** ours is *shorter on paper but stronger in practice* — refund-or-replace (beats williams' credit-only), tied to an independent avian-vet exam (what Reddit says to demand), and backed by documentation nobody else shows. We turn the length disadvantage into the trust argument.

---

## 3. Competitor reverse-engineering

### 3a. `theavianexchange.com` — the strongest *structural* rival (Google #1)
**A screened-breeder marketplace, not a breeder.** Section inventory (fetched): trust ribbon "**ID Verified Breeders · No Anonymous Sellers · Health Guarantees · Disease Testing Disclosed**" · filterable card grid (tier badge Elite/Pro · Handfed · "Disease Testing Disclosed" · "Ships to You" · sex · age · breeder + city · "Typically responds within an hour" · price) · "**What to look for in an african grey breeder**" 5-point list (incl. "a clear health guarantee") · FAQ (cost / shipping / "**What should I ask a breeder before buying**" / "Are these breeders verified?") · state links (CA/FL/TX/NY/PA/OH/GA/NC/IL/MI) · other-species nav.
**Prices:** **$4,999 – $8,500** (Parrot Stars, Feather Headz, Parrot Baby, Brenda & Billy's).
**Weaknesses we exploit:** (1) aggregator — no direct breeder relationship, no *named bird you bond with before purchase*, guarantee is per-third-party and non-standard; (2) prices are 3–5× our $1,500 floor; (3) all trust is *procedural* ("verified", "disclosed") — no covered-condition list, no remedy, no documentation shown. **We answer their "what to ask a breeder" checklist on-page, from the breeder's side, for one-third the price.**

### 3b. `africangraysales.com` — page-1 on the trust query · documented bait-and-switch
Known rival (flagged on Timneh + DNA builds). Publishes a "1-Year Health Guarantee" + "DNA Sexing Certificate Included" as the trust hooks, then discounts every Congo ~70% to ~$750–$820 (half our floor), sells fertile eggs (our own egg page documents these as near-universally fraudulent), and posts initials-only reviews ("Sarah M., California"). ⚠️ Still lists a Congo male **"Roy"** — we have **Roys**; note before publishing.

### 3c. `havensunaviary.com` — the standard guarantee template, sloppily copied
Their terms (fetched) are the industry-standard template and closely match ours: good health at delivery; free of viral/bacterial/fungal + congenital defects; buyer vet-check within **3 business days**; remedy = **refund or replace same species/sex/age**; void if leg band removed; "as is" if no vet check. **But the copy is boilerplate** — it says "We warrants", references "**Olive macaw Parrots Farm**'s attending veterinarian", mentions "**Caiques**… vaccinated against Avian Polyoma", and the reviews are stock-photo testimonials ("Cecil / Muna / Jack / Herman"). **Lesson:** the standard terms are legitimate and ours mirror them — our edge is presenting them *transparently, species-correct, and attached to real named birds*, which none of these copy-paste pages do.

### 3d. 30-competitor registry cross-check
| Registry member | In these SERPs? | Status |
|---|---|---|
| `williamsafricangreys` | Google #8 (money term) | live `/health-guarantee/` page, 72-hr credit-only remedy |
| `exoticparrotpetstore` | Google #10 | $800 storefront, "Health Guarantee" nav |
| `birdbreeders` | trust SERP #3 | directory, $5,200 |
| other 27 | **absent** | the guarantee SERP is contested by a mostly *different* set |

**Registry action (recommend adding as tier-1):** `theavianexchange.com` (the real structural threat — screened marketplace), `havensunaviary.com`, `lilianaafricangreyparrots.com`, `majesticwingsaviary.com`, `buyafricangreyparrots.com`, `featheredfriendshub.com`. None currently tracked.

---

## 4. Reddit — `research-recency` protocol (Firecrawl, Reddit blocks curl)

**The "health guarantee" buyer is a scam-anxious buyer.** The SERP for our topic is *entirely* scam/legitimacy threads — and the consensus validates our exact model:

> "The store/**breeder requires a health check to an Avian vet within a short period of time from purchase**. Any breeder that sells eggs is lying." — r/parrots, *Buying an African Grey, advice needed*
> "**No one is selling a healthy African Grey for $800.** The amount of [scams]…" — r/Scams
> "There's an **insane amount of scams regarding African greys.** It's a very valid question to ask about ethical and legitimate breeders." — r/AfricanGrey, *legitimate website?*
> "Prices too cheap, international shipping, stolen photos… **If it's too good to be true it is!**" — r/parrots, *Scam or not?*
> "Do not buy from [X]. They scam by asking you to purchase through **Zelle**, and… a shipping company called United Pet…" — r/parrots, *Parrot Scam*
> "When he tested positive, I confronted the breeder to **request a refund per the health guarantee.**" — r/AmItheAsshole (a real enforcement story)

**Reading:** Reddit *already recommends the 72-hour vet-check model* and *already warns against the $800 "healthy" bird* — but never attaches either to a specific trustworthy breeder. That is the unclaimed position. Recurring thread titles = ready-made H4/PAA: *"How to know a breeder is ethical / signs to avoid"* · *"legitimate website to buy from?"* · *"Scam or not a scam?"* · *"advice needed buying an African Grey."*

**Counter-positioning gift:** cite the Reddit-endorsed rule ("get an avian-vet check in a short window") as the reason our 72-hour window is a *feature*, and answer the "$800 healthy bird" thread head-on with our honest floor price.

---

## 5. YouTube
From the general passes (site:youtube.com filter returned empty this run):
- **"Don't Buy a Parrot Until You Ask These 5 Questions | The Parrot…"** — the buyer-red-flags video; overlaps the "what to ask a breeder" intent (theavianexchange FAQ + Facebook groups feed the same).
- **"Looking For TWO MORE African Greys"** — owner vlog (not commercial), ranks on the money term = weak commercial competition on YouTube.
**Gap:** no video (and no for-sale page) *shows the actual health-guarantee document + the vet certificate that ships with a bird.* Same certificate-gap pattern as DNA.

## 6. Instagram / Facebook
- **Instagram over-claim pattern (counter-positioning gift):** "Baby African Grey Parrots Vet Checked… **YES SHOTS UP TO DATE**… **YES POTTY TRAINED**… Comes with health guarantee"; "Closed band, DNA + health guarantee included"; "$5200… **Available Across Qatar WhatsApp**" (international/grey-market). Parrots don't get routine "shots"; "potty trained" is a tell. **We state exactly what's real** (avian-vet exam, PBFD/APV/psittacosis PCR, DNA cert, written 72-hr guarantee) and pointedly *don't* over-claim shots/potty-training.
- Legit-adjacent signal: "**Cisco… DNA-sexed male Congo… thoroughly vet checked, including bloodwork**" (a rescue "Case Snapshot") — shows buyers value the *bloodwork/vet-check* detail specifically.
- **Facebook:** "African Gray Parrots for **Rehoming** in Louisiana" (rehoming intent, out-of-state number = red flag); group "**What to ask a breeder when buying a baby African Grey**" (mirrors the on-page checklist demand); group post "African grey parrots for sale **with health guarantee**" stacking "Health certificate ✓ Health guarantee ✓ Pedigree ✓ Registered". **NOT FETCHED:** group interiors (login-walled) — public titles only, no engagement metrics.

## 7. Bing
- Homepage: **pos 6.2 · 302 impr · 21 clicks** (Bing is strong for us).
- Interior `/african-grey-parrot-health-guarantee/`: **pos 2 · 1 impr** on Bing.
- **This for-sale target: absent from the Bing page report (~0 Bing impressions).** Bing currently sends the tiny "health guarantee" signal to the *interior* page, not this one → a clean Bing opportunity, and a reason to sharpen the internal link between them (§11).

---

## 8. Gap matrix — what nobody on page 1 does
| # | Gap | Evidence | Our answer |
|---|---|---|---|
| G1 | **Nobody shows the actual guarantee document** | 20 results checked; zero doc images | Show/describe the written guarantee + the covered-condition list |
| G2 | **"Health guarantee" is an empty two-word badge** | theavianexchange/liliana/exoticparrotpetstore assert it with no terms | Publish window + covered conditions + remedy + void terms |
| G3 | **The guarantee-length arms race misleads** | 72-hr vs 1-yr vs 365-day, longest = scammiest (§2c, §3b) | Reframe: enforceable 72-hr vet-anchored > unenforceable "1-year" |
| G4 | **Remedy is vague or weak** | williams = credit only; others silent | State replacement-OR-refund plainly |
| G5 | **Scam-fear is unanswered by breeders** | entire Reddit SERP = scam threads (§4) | Answer "$800 healthy bird" + Zelle + eggs head-on; link scam cluster |
| G6 | **Guarantee never tied to documentation stack** | competitors list it as one badge among many | Bundle: vet cert + PCR screening + DNA cert + CITES + band + guarantee |
| G7 | **No named birds carrying the guarantee** | marketplaces show stock cards; scam sites show stolen photos | Real available birds (Bery/Amie/Roys/Jins&Jeni/Elad/Evie) each backed by it |
| G8 | **Over-claim tells ("shots", "potty trained")** | Instagram §6 | Say only what's true; the honesty *is* the trust signal |
| G9 | **"What to ask a breeder" demand is unmet on-page** | theavianexchange FAQ + FB groups + YouTube all raise it | Answer the buyer's own checklist from the breeder's side |
| G10 | **Interior policy page ≠ transactional page** | our own two URLs split the intent (§1a, §7) | This page = birds+guarantee; link *to* the interior policy explainer |

---

## 9. Entity map seeds (→ Sprint 0.5 / EEBP)
written health guarantee · **72-hour window** (+ 24 h shipping window) · board-certified avian-vet exam · avian-vet **health certificate** (dated ≤10 days of travel) · congenital defects · **PBFD / Polyomavirus / psittacosis (Chlamydia psittaci) PCR screening** · DNA sexing certificate · CITES Appendix I captive-bred · USDA AWA license · closed leg band + hatch certificate · IATA LAR · Delta/United/American cargo · Midland TX pickup (2–3 hr radius) · **replacement-or-refund remedy** · "as is" / void conditions (band removal, improper diet, exposure) · weaning 12–16 wk · the real birds (Bery/Amie/Roys Congo · Jins & Jeni companion pair · Elad/Evie Timneh) · $1,500 floor · $185 airport / $350 home shipping · avian first-vet-visit.

## 10. Open flags (breeder input — none blocks Sprint 0.5)
1. **Guarantee window wording:** interior page + this build use **72-hour** (congenital + infectious) + **24 h shipping-arrival** window; the homepage says "3-day." They're the same thing — I'll standardize on **"72-hour (3-day) written health guarantee"** to bridge both and match williamsafricangreys' phrasing. Confirm OK.
2. **Remedy language:** I'll write **"replacement or refund at our discretion"** (per the interior page's verbatim terms). Confirm this is current.
3. **May we show/describe the actual guarantee document** (a real signed guarantee or the covered-condition sheet, buyer info redacted)? Closes G1 and no competitor can copy it.
4. **Two supplied reviews** (Meredith Plaisance, Hartsville SC · Jeffrey Hendershot, Centennial CO) = this page's whitelisted verbatim reviews. Confirmed **new** — not reused from siblings (DNA reused Stanley Perkin + Jesse Ovalle; these two are distinct).

## 11. Cannibalization guard (binding)
| Page | Owns | This page must NOT |
|---|---|---|
| `/african-grey-parrot-health-guarantee/` (interior · Bing pos 2 · GSC pos 6.5) | *informational* policy explainer — what's covered, the window, documentation | re-teach the full policy. **Summarize + link to it** for the fine print |
| `/how-to-avoid-african-grey-parrot-scams/` (scam cluster) | the scam teardown | duplicate the scam checklist. Teaser + link |
| `/trusted-african-grey-parrot-breeders/` | breeder trust/credentials | duplicate breeder-vetting. Cross-link |
| near-me pages (`…for-sale-near-me`, state pages) | "near me" geo intent | target "near me" as primary; teaser + link only |
| `/male-vs-female…` (1,818 impr, pos 21) | behavioural comparison | run a M/F comparison |

**This page owns exactly one intent:** *buying a real, documented African Grey that ships with an enforceable written health guarantee — and knowing it's not a scam.*

## 12. Recommended angle → Sprint 1
**"A Guarantee You Can Actually Use" — reframe → cover → document → birds.**
1. **Reframe** the guarantee-length arms race (enforceable 72-hr vet-anchored > unenforceable "1-year"), grounded in parrotparrot's "be reasonable" + Reddit's vet-check consensus (§2c, §4).
2. **Cover** — the exact conditions, window, remedy, and void terms nobody publishes (G1–G4).
3. **Document** — bundle the guarantee with the vet cert + PCR screening + DNA + CITES + band (G6), and answer scam-fear head-on (G5, link scam cluster).
4. **Birds** — real available birds each carrying the guarantee, at the honest $1,500 floor (G7).

**Trade-off, named honestly:** leading with the *reframe/trust* argument spends the top third on persuasion before the catalogue, which can slow first-scroll "add-to-cart" behaviour vs a bare bird grid. I accept it because (a) the head term has no transactional demand to convert directly — the traffic is trust-driven, and (b) the page is *already* at pos 11 on trust signals, so doubling down on the trust moat is what climbs it. A bare catalogue would forfeit the exact edge that already ranks it.

**Because the page already ranks (unlike DNA), the transactional layer sits higher than on DNA** — bird cards appear right after the reframe, not after a long informational preamble.

**Deliverables carried to Sprint 0.5 (grill-me + fan-out):** trust/near-me/rehoming keyword universe (§1b), entity seeds (§9), scam/PAA H4 targets (§4/§9), gap matrix (§8), guarantee-length differentiation axis (§2c), cannibalization guard (§11).

---

## Appendix — provenance
- GSC: `assets/1WORKING-ON/FOR-SALE-PAGES/GSC-extracted/{Queries,Pages,Devices}.csv` (exported 2026-07-19)
- Bing: `BING-…PageTrafficReport_7_20_2026.csv` (page-level)
- Google/Reddit/Instagram SERPs: Firecrawl search (US geo), 2026-07-25
- Rival page inventories: Firecrawl scrape of `theavianexchange.com/african-greys-for-sale` + `havensunaviary.com/health-guarantee-reviews`
- Registry: `data/competitors.json` (30 entries)
- **NOT FETCHED:** Facebook group interiors (login-walled) — public post titles only. `site:youtube.com` filter returned empty this run (YouTube coverage from the general-web passes). Bing query-level export for this cluster not separately mined (page-level report used).

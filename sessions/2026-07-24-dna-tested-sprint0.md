# Sprint 0 — Intelligence · `/dna-tested-african-grey-for-sale/`

**Date:** 2026-07-24 · **Page:** #6 in Cluster 1 of the 22-page for-sale program
**Mode:** REBUILD (on-disk page is a 282-line stub) · **Branch:** `main`
**Method:** GSC/Bing local exports + live SERP (Firecrawl) + Reddit/YouTube/Instagram/Facebook + 30-competitor registry cross-check.
**Honesty rule:** anything not actually fetched is marked `NOT FETCHED`. No metric on this page is estimated or invented.

---

## 0. Headline finding (read this first)

**The head term has no measurable search demand, and Bing cannot even parse it. The demand is in the *sexing* question — and the SERP that answers it is dominated by a myth.**

Three verified facts drive every recommendation below:

1. **Zero GSC queries containing "dna."** Not low — *zero*, across the entire `Queries.csv` export. Also zero for "sexing"/"sexed"/"monomorphic". The current page has **zero impressions**.
2. **Bing returns the wrong entity entirely.** A top-20 scrape of `dna tested african grey parrot for sale` on Bing returns Wikipedia *DNA*, Britannica *DNA*, genome.gov, MedlinePlus, Cleveland Clinic, AncestryDNA. **Not one bird result in the top 10.** "DNA" is hijacked by the molecule entity exactly as "Congo" was hijacked by the country entity on the Congo page.
3. **The real demand is `how to sex an african grey parrot` — and Google's answer is wrong.** We hold ~103 impressions across 4 near-identical variants at **positions 42–44**, and the pages beating us teach visual sexing, which every Reddit owner thread openly debunks.

**Strategic consequence:** this page must not be built as a "DNA-tested birds" catalogue. It must be built as **the page that settles the sexing question and then sells the certificate** — myth-bust → method → certificate → bird.

---

## 1. GSC demand snapshot (local export, `GSC-extracted/`, pulled 2026-07-19)

### 1a. The head term
| Check | Result |
|---|---|
| Queries containing `dna` | **0** |
| Queries containing `sexing` / `sexed` / `monomorphic` | **0** |
| Impressions on `/dna-tested-african-grey-for-sale/` | **0** (absent from `Pages.csv`) |

### 1b. Where the demand actually is — the sexing cluster
| Query | Clicks | Impr | Pos |
|---|---:|---:|---:|
| female african grey parrot for sale | 0 | 45 | 38.9 |
| african grey male vs female behavior | 0 | 38 | 12.1 |
| female african grey for sale | 0 | 29 | 44.2 |
| **how to sex a african grey parrot** | 0 | 29 | 44.4 |
| which is better male or female african grey parrot? | 0 | 28 | 25.4 |
| **how to sex an african grey parrot** | 0 | 28 | 43.1 |
| **how do you sex an african grey parrot** | 0 | 24 | 43.2 |
| **how to sex african grey parrots** | 0 | 22 | 42.1 |
| african grey male vs female | 1 | 15 | 35.5 |
| african grey gender differences | 1 | 12 | 11.0 |
| do male or female african grey parrots talk better | 0 | 12 | 12.1 |
| male african grey parrot for sale | 0 | 13 | 38.3 |
| pictures of male and female african grey parrots | 0 | 11 | 71.4 |
| difference between male and female african grey parrot | 1 | 8 | 26.0 |

**59 queries** in the sex/gender/male/female/tested cluster. The four `how to sex…` phrasings alone total **103 impressions at avg position ~43** — page 5. That is the single largest untapped block attached to this page.

### 1c. Device split (whole site)
| Device | Clicks | Impr | CTR | Pos |
|---|---:|---:|---:|---:|
| **Mobile** | 431 | 9,252 | **4.66%** | 25.0 |
| Desktop | 77 | 17,256 | 0.45% | 53.0 |

Mobile CTR is **10× desktop** — same pattern that made Congo and Timneh mobile-first. This page is mobile-first. Non-negotiable.

### 1d. Legacy DNA URL — resolved, not a threat
`/trusted-african-grey-parrot-breeders-dna-certified/` appears in `Pages.csv` at **position 6** (1 click / 4 impr / 25% CTR). Verified live: it **301s to `/trusted-african-grey-parrot-breeders/`** (rule present in both `public/_redirects` and `site/content/_redirects`). Not a live cannibal — but it proves Google already associates this domain with "DNA-certified breeder." That equity should be pointed at the new page via internal links from `/trusted-african-grey-parrot-breeders/`.

---

## 2. SERP snapshot — Google

### 2a. `dna tested african grey parrot for sale` (top 10, fetched 2026-07-24)
| # | Domain | Signal | HTTP |
|---|---|---|---|
| 1 | buyafricangreyparrots.com | "DNA Tested, Fully Weaned" · Violet ♀ Congo **$800** — below our $1,500 floor | 200 |
| 2 | birdbreeders.com | directory · "DNA tested male and female" **$8,500** | 200 |
| 3 | graybreedersfoundation.yolasite.com | **free Yola site-builder** · $1,500 · claims MAP-certified | 403 |
| 4 | anasparrots.com | $7,500 Congo baby | 403 |
| 5 | **birdsjungle.com** | strongest on-page rival — see §3a | 200 |
| 6 | africangreyparrot.company.site | **"The website is not available"** — a dead storefront holding a top-10 slot | 200 |
| 7 | featheredfriendshub.com | $2,700–$5,300 | 200 |
| 8 | **africangraysales.com** | see §3b — documented bait-and-switch | 200 |
| 9 | africangrayparrotsforsale.com | **registry tier-1** · "$1000" | **DNS fail (000)** |
| 10 | exoticbirdsbreeders.com | African Grey **$800** | **DNS fail (000)** |

**Three of ten results are dead, DNS-failing, or 403-walled.** Two more price Congos at $800–$1,000. This is a weak, decaying SERP — the cheapest page-1 entry in the entire for-sale cluster so far.

### 2b. `dna sexed african grey parrot for sale breeder certificate` (top 10)
| # | Domain | Signal |
|---|---|---|
| 1 | africangraysales.com | "DNA Sexing Certificate Included ✓" + **"Females: $820 Limited time"** |
| 2 | facebook.com/groups/… | "2pcs African Grey Dna 🙍‍♀️ With legal papers" — grey-market group trade |
| 3 | graybreedersfoundation.yolasite.com | Yola free-host |
| 4 | **amazon.com — Pollygene Parrot DNA Gender Test kit** | a **DIY sexing kit** on page 1 |
| 5 | royalwingsaviary.com | budgies/cockatiels, no greys |
| 6 | exoticbirdsforsale.net | "DNA-certified, potty trained" breeding pair **$1,500 each** |
| 7 | birdbreeders.com | directory |
| 8 | featheredfriendshub.com | |
| 9 | exoticbirdsbreeders.com | |
| 10 | **dnacenter.com/bird-dna-testing** | an actual DNA lab |

**A retail DIY test kit (p4) and a genetics lab (p10) rank on a "for sale" query.** Google is blending transactional and informational intent because no single page serves both. That blend is the opening.

### 2c. `how to sex an african grey parrot male or female DNA` (top 10) — the myth SERP
| # | Source | What it teaches |
|---|---|---|
| 1 | facebook.com/groups | "don't have any DNA test, but they told me she looks…" |
| 2 | birdtricksstore.com | ✅ honest — "never 100% reliable" |
| 3 | youtube.com | ❌ **"African greys are in fact sexually dimorphic for the most part"** |
| 4 | **wikihow.com** | ❌ **"look at the feathers underneath its tail. If they're red, the parrot is a male, and if they're gray, it's a female"** |
| 5 | facebook.com/groups | gender guessing thread |
| 6 | **reddit.com/r/parrots** | ✅ owners debunking |
| 7 | justanswer.com | paywalled Q&A |
| 8 | youtube.com | "identify by physically examining it, although a DNA test confirms…" |
| 9 | cuteness.com | ❌ "a female's red tail feathers become tipped with silver" |
| 10 | wikihow.com | ✅ "monomorphic… wait for eggs or get a DNA test" |

**Four of the top ten teach visual sexing that does not work on this species.** wikiHow — position 4 — is flatly wrong. No breeder ranks here at all.

---

## 3. Competitor reverse-engineering

### 3a. `birdsjungle.com` — the strongest *on-page* rival (Google p5)
**Section inventory (fetched):** product hero w/ price range $1,500–$4,500 · 6 trust icon-badges (DNA-tested and certified / Vet health-checked / …) · "Size and packaging guidelines" · "What's Included With Every African Grey" (incl. *"DNA sexing certificate: you know if your bird is male or female"*) · FAQ block · related-products grid.

**Fatal weakness — verifiable in their own markup:** the identical string **"DNA-tested and certified — Lab-verified parentage and species"** appears on their Budgie, Cockatiel, Green Cheek Conure, Quaker, and Senegal product pages. It is boilerplate stamped across six species. There is no African-Grey-specific DNA content anywhere on the page: no lab named, no certificate shown, no method explained, no accuracy figure, no turnaround time.

**Also note:** they claim "lab-verified **parentage and species**" — DNA *sexing* does not verify parentage or species. That is a distinct (and more expensive) test. Their trust badge overstates what a sexing test does.

### 3b. `africangraysales.com` — page-1 on both money queries · **documented bait-and-switch**
Known rival from the Timneh build (flagged there for advertising illegal international shipping). Fetched 2026-07-24:

| Element | What they publish |
|---|---|
| Sticky banner | 🎉 LIMITED TIME: **Males $750 \| Females $820** |
| Published price guide | Congo **$2,500–$3,200** · Timneh **$2,000–$2,600** |
| Jane ♀ Congo 7 mo | ~~$2,800~~ → **$820** |
| Jerry ♂ Congo 6 mo | ~~$2,600~~ → **$750** |
| Roy ♂ Congo 8 mo | ~~$2,500~~ → **$750** |
| Mike ♂ Timneh 6 mo | ~~$2,100~~ → **$750** |
| Trust hooks | "DNA Sexing Certificate Included" · "1-Year Health Guarantee" · "12+ Years Experience" |
| Catalogue | Macaw, Amazon, Eclectus, Cockatoo, Senegal, Quaker + **fertile parrot eggs** (African Grey, Macaw, Amazon, Cockatoo) |
| Reviews | "Sarah M., California" · "David T., Texas" · "Lisa R., Florida" — initials only, unverifiable |

**Every bird is discounted ~70% simultaneously**, landing all four at roughly half our $1,500 floor. They also sell fertile eggs — which our own egg page documents as near-universally fraudulent. They use "DNA Sexing Certificate Included" as the trust hook that makes a $750 Congo feel legitimate.

⚠️ **They list a Congo male named "Roy."** We have **Roys**. Worth knowing before we publish Roys' DNA certificate on a page that will rank beside theirs.

### 3c. 30-competitor registry cross-check
| Registry member | In this SERP? | Status |
|---|---|---|
| `africanGrayParrotsForSale` (T1) | Google p9 | **DNS failure (000)** — ranking a dead domain |
| `birdBreeders` (T2) | Google p2 + p7 | live directory, $8,500 listing |
| `silvergateBirdFarm` (T1) | absent | prior session: confirmed cloaker → recaptcha.cloud |
| all other 27 | **absent from both money SERPs** | — |

**Only 2 of our 30 registered competitors appear.** The DNA/sexing SERP is contested by an almost entirely *different* set of sites. **Registry action:** add `africangraysales.com`, `birdsjungle.com`, `buyafricangreyparrots.com`, `featheredfriendshub.com` as new tier-1 entries — they are page-1 on our money terms and none is tracked.

---

## 4. Reddit — `research-recency` protocol (Firecrawl `site:` — Reddit blocks curl)

**r/parrots + r/AfricanGrey, 10 threads fetched.** The consensus is unusually clean:

> "African Greys both males and females look 100% identical. There's no physical features that can determine sex. You need a blood test." — r/parrots
> "African Greys cannot be sexed through appearance or size. You can get a DNA test, or see your bird lay an egg. Those are the only ways to know." — r/AfricanGrey
> "DNA sexing is done by taking a blood sample at the vet, and having the vet send it into a reputable lab. Typically takes about 1-2 weeks." — r/parrots
> "No, African grey parrots are not sexually dimorphic…" — r/parrots

**But the myth persists inside the same threads:** "males can be darker grey with almond shape eyes and females are lighter silver with round eyes"; "from what I've seen of DNA sexed females, they tend to have a lighter grey head."

**Reading:** owners arrive believing the myth, get corrected, and the correction is *never* attached to a breeder. Threads recommending "get a DNA test" cite vets and labs — never a breeder who already did it. **That is an unclaimed position.**

Recurring thread titles = ready-made H4/PAA targets: *"is my rescued African gray parrot female or male?"* · *"How to tell the gender"* · *"Is my AG male/female & age?"* · *"guess gender please"*.

---

## 5. YouTube (top 10)
Split cleanly in two:
- **Visual-ID videos** — "Visual Gender Identification of African Grey Parrot", "Male or Female African Grey?", "How To: African Grey See Diff Male Vs Female" (this one asserts greys *are* dimorphic).
- **DIY method videos** — "How I DNA my Birds | Avian DNA Sexing", "How to DNA Sex Birds – HIGH Accuracy", **"How To DNA Test Your Parrot: Feather Pulling"** ("pulling 4 to 6 feathers"), "THIS PARROT IS WILD CAUGHT! AVIAN DNA SEXING".

Honest outlier: *"The only sure way to tell if your Grey is male or female is through DNA sexing."*

**Gap:** every video is an owner testing a bird they already own. **No video, and no page, shows a certificate that came *with* a bird at purchase.**

## 6. Instagram / Facebook
- **Instagram:** competitor captions run "DNA certificate — confirmed", "DNA Tested Female", and notably **"DNA pending"** (`We have just received a baby African Grey. DNA pending`). Several posts carry non-US phone formats (e.g. `0740656776`) — international/grey-market signal. One breeder post: *"Behind every successful breeder is accurate information, careful planning, and trusted DNA testing."*
- **Our own page ranks #6** in an Instagram-intent query — so it *is* indexed, it simply has no demand attached to its current framing.
- **Facebook:** two group posts surfaced via search (`2pcs African Grey Dna with legal papers and…`, `How to determine the sex of an African Grey Parrot?` in a 64k-member group). **NOT FETCHED — group interiors are login-walled.** Read the two public post titles only; no engagement metrics obtained.

**"DNA pending" is a counter-positioning gift:** we can state plainly that we never list a bird as DNA-tested while the result is still in the mail.

---

## 7. Method grounding — real, citable, external authority

Fetched from primary sources, for the method sections and the external-link set:

| Source | Verified fact |
|---|---|
| **Animal Genetics** (`avian2.animalgenetics.com`) | Sexing from **blood, feather, or eggshell** — "all equally reliable." Offering feather sexing **since 1996**; 2,000+ species database; **results in 1–2 business days**; blood drawn from **the end of a toenail** |
| **dnacenter.com** | **PCR (Polymerase Chain Reaction)** technology · **$19/sample** · feather or blood |
| **healthgene.com** | $17 blood · $22.50 feather · $25 eggshell · **"Certificate for each DNA test"** |
| **EasyDNA USA** | $25/bird, all known bird breeds |
| **PMC9913368** (Turcu et al., 2023, cited by 20) | Peer-reviewed: *"Molecular sexing using blood samples has yielded more accurate [results] because blood samples contain a higher DNA concentration than oral swabs"* |
| **envirocarelab** | **"Approximately 99% accuracy"** · same labs run **PBFD** testing |

### ⚠️ Two corrections to the current live page
1. It claims **"99.9% accuracy."** The published figure from an actual lab is **~99%**. Fix or drop — we cannot out-claim the labs.
2. It claims the certificate is provided **"at no additional charge"** and cites an unnamed *"accredited avian genetics laboratory."* Neither is in the Verified-Claim Ledger. **Open question for the breeder — §10.**

**Entity bridge worth exploiting:** the same labs that run DNA sexing run **PBFD/APV PCR** — both already Ledger-verified for us. One feather sample, two answers. No competitor connects them.

---

## 8. Gap matrix — what nobody on page 1 does

| # | Gap | Evidence | Our answer |
|---|---|---|---|
| G1 | **Nobody shows a certificate** | 20 SERP results checked; zero certificate images | Photograph a real certificate for a real named bird |
| G2 | **Nobody names their lab** | birdsjungle: "certified" (no lab); africangraysales: "Included" (no lab) | Name ours *(pending §10 answer)* |
| G3 | **Nobody explains the method** | Method content lives on lab sites + YouTube DIY, never on a for-sale page | Feather vs blood vs eggshell, PCR, 1–2 day turnaround |
| G4 | **The myth outranks the truth** | wikiHow p4 + cuteness p9 + YouTube p3 all teach visual sexing | Myth-bust section, sourced to Reddit consensus + the labs |
| G5 | **"DNA pending" listings** | Instagram competitor caption | Result in hand before a bird is listed |
| G6 | **Certificate used to launder a $750 Congo** | africangraysales full receipts, §3b | Certificate + honest floor price, together |
| G7 | **Sexing never linked to disease screening** | no competitor connects them | One feather → sex + PBFD/APV PCR |
| G8 | **Bing can't disambiguate "DNA"** | top-20 Bing scrape = the molecule | Entity-loaded title/H1 (§9) |
| G9 | **Transactional + informational never merged** | Amazon kit p4, lab p10 on a "for sale" SERP | One page that answers *and* sells |
| G10 | **Dead/DNS-failed sites hold 3 of 10 slots** | HTTP audit §2a | Low displacement cost |

---

## 9. Bing disambiguation requirement (hard constraint)

Because Bing resolves "DNA tested" to deoxyribonucleic acid, the title and H1 must carry unmistakable bird-entity signals **early**:

- Lead with **"DNA-Sexed"** or **"DNA-Tested"** immediately followed by **"African Grey Parrot"** — never "DNA-Tested" near the start unqualified.
- Include ***Psittacus erithacus*** in the H1 region (the Congo-page fix that worked).
- Prefer **"DNA sexing" / "sexed" / "sexing certificate"** phrasing in H2s — those strings do not collide with the molecule entity and match how Reddit, the labs, and Instagram all actually phrase it.

---

## 10. Open flags (breeder input needed — none blocks Sprint 0.5)

1. **Which lab do we use?** (Animal Genetics? Avian Biotech? someone else?) G2 is our single biggest differentiator and I will not name a lab we don't use.
2. **Is the DNA certificate included free, or priced?** The live page says free; not in the Ledger.
3. **Blood or feather sample** — which do we submit? Determines the method section and the photography.
4. **May we photograph a real certificate** (bird name visible, any lab account number redacted)? This single asset closes G1 and no competitor can copy it.
5. **Accuracy figure** — I'll write **"approximately 99%"** with the lab citation unless told otherwise. The live page's "99.9%" is unsupported.

## 11. Cannibalization guard (binding)

| Page | Owns | This page must NOT |
|---|---|---|
| `/male-vs-female-african-grey-parrots-for-sale/` (**1,818 impr · pos 21.4 · 7th-biggest page**) | *behavioural* male-vs-female comparison | run a male-vs-female traits comparison. Teaser + link only |
| `/male-african-gray-for-sale/` (Cluster 3) | transactional male-specific | target "male african grey for sale" as primary |
| `/african-greys-for-sale-with-health-guarantee/` (Cluster 1, unbuilt) | health guarantee | lead with the guarantee; PCR screening is a *bridge*, not the topic |
| `/trusted-african-grey-parrot-breeders/` | breeder trust + holds the legacy `-dna-certified` 301 | duplicate breeder-vetting. **Should link *to* us** |

**This page owns exactly one intent:** *proving sex with a laboratory result, and buying a bird that already has one.*

---

## 12. Recommended angle → Sprint 1

**"Proof, Not Guesswork" — myth-bust → method → certificate → bird.**

Grounded in: 103 impressions at pos ~43 on `how to sex…` (§1b) · 4 of 10 top results teaching a debunked myth (§2c) · Reddit's unanimous correction that no breeder has claimed (§4) · G1/G2/G3 all open (§8) · a decaying SERP with 3 dead slots (§2a).

**Trade-off, named honestly:** this angle spends its first third on informational content before it sells anything, which suppresses immediate conversion rate versus a straight catalogue page. I accept that because the head term has **zero** demand — there is no transactional traffic here to convert yet. We must *create* the entry point from the sexing question, then convert down-page with the certificate. A pure catalogue build would rank for nothing.

**Deliverables carried to Sprint 0.5 (grill-me + fan-out):** keyword universe (§1b), entity map seeds (§7), PAA/H4 targets (§4), gap matrix (§8), Bing constraint (§9), cannibalization guard (§11).

---

## Appendix — provenance
- GSC: `assets/1WORKING-ON/FOR-SALE-PAGES/GSC-extracted/{Queries,Pages,Devices}.csv` (exported 2026-07-19)
- Google/Reddit/YouTube/Instagram SERPs: Firecrawl search, 2026-07-24
- Bing: Firecrawl scrape of `bing.com/search?q=…&count=20`, 2026-07-24
- HTTP liveness: `curl` with desktop UA, 2026-07-24
- Competitor page inventories: Firecrawl scrape of `africangraysales.com` + Firecrawl-extracted `birdsjungle.com` product markup
- Registry: `data/competitors.json` (30 entries)
- **NOT FETCHED:** Facebook group interiors (login-walled) — public post titles only, no engagement metrics. `anasparrots.com` + `graybreedersfoundation` returned 403 to our UA (bot-block, not dead). `africangrayparrotsforsale.com` + `exoticbirdsbreeders.com` returned DNS failure (000).

# Sprint 5 — LLM Visibility Baseline: `/african-grey-breeding-pair-for-sale/`

**Date:** 2026-08-07
**Task:** Task 13 of `docs/superpowers/plans/2026-08-07-breeding-pair-finish.md`
**Page under test:** https://congoafricangreys.com/african-grey-breeding-pair-for-sale/ (HTTP 200 at run time)
**Scope:** 5 engines × 6 queries = 30 cells
**Method:** live browser (Playwright) against each engine's own surface. No engine output is inferred, estimated or reconstructed — every cell below is either a transcript of what the engine actually returned, or `NOT FETCHED`.

## How Each Engine Was Reached

| Engine | Route | Reached? | Barrier |
|---|---|---|---|
| Google AIO | `google.com/search?q=…&hl=en&gl=us`, AI Overview container read from DOM | Yes | none — no CAPTCHA, no consent interstitial |
| Perplexity | `perplexity.ai/search?q=…`, logged out; source list expanded | Yes | none — anonymous answers served |
| ChatGPT | `chatgpt.com/?q=…`, logged out | Yes | none — logged-out answers served |
| Gemini | `gemini.google.com/app`, logged out, Flash-Lite tier | Yes | none — logged-out answers served |
| Claude | `claude.ai/new` | **No** | **hard login wall** — `/new` redirects to `/logout` then `/login`; no anonymous chat surface exists, and no `ANTHROPIC_API_KEY` is present in the environment or in `.claude/settings.local.json`. Not solvable without credentials, so all six cells are `NOT FETCHED`. |

**Geo caveat (real, and it affects how three rows read).** Google was pinned to `gl=us`. ChatGPT and Gemini, logged out, have no US geo signal and **volunteered UK answers** (Article 10 certificates, £ prices, Birmingham classifieds) on the queries that do not contain "usa". This is recorded as observed, not corrected. Query 5 — the one that says "usa" — is therefore the cleanest US-intent read in the set.

## Full Results — One Row per Engine × Query

| Engine | Query | CAG cited? | Competitors cited | Answer structure |
|---|---|---|---|---|
| Google AIO | african grey breeding pair for sale | **No** | birdsnow.com, birdbreeders.com, exoticglobalparrotsfarm.com, reddit.com, linkedin.com, cbreptile.com, birdsofeden.co.za | Caution-first paragraph, then 4 labelled bullets (Bonded vs. Tame / Proven Status / Legal Requirements / Scam Warning), then a follow-up offer. ~200w. |
| Google AIO | proven african grey breeding pair price | **No** | facebook.com, parrotforums.com, exoticglobalparrotsfarm.com, backyardchickens.com, youtube.com, chewy.com, purefeatheraviary.co.uk | Price-first sentence, then two headed bullet groups (Factors Influencing the Price / Risks and Buyer Considerations). "7 sites". ~250w. |
| Google AIO | how do I know an african grey pair is actually proven | **No** | lafeber.com, watchbird-ojs-tamu.tdl.org, parrottalk.com, youtube.com, facebook.com, backyardchickens.com, parrotforums.com | Direct-answer paragraph, then two headed bullet groups (Red Flags and Verification / Behavioral and Environmental Realities). "10 sites". ~250w. |
| Google AIO | african grey breeding pair vs single bird | **No** | reddit.com (r/parrots), justanswer.com, pamelaclarkonline.com, quora.com, pmc.ncbi.nlm.nih.gov, parrotessentials.co.uk, revivalanimal.com, birdtricksstore.com, youtube.com | Longest of the six. Paragraph, two labelled profiles, **a 5-row comparison table** (Primary Goal / Human Interaction / Housing / Behavioral Risk), plus two embedded videos. "14 sites". ~450w. |
| Google AIO | where to buy a proven congo african grey pair usa | **No** | birdbreeders.com, theavianexchange.com, **dallasparrots.com**, exoticglobalparrotsfarm.com, linkedin.com | Vendor-routing answer: "Where to Look" (3 bullets, named venues) + "Buying Tips & Cautions" (3 bullets). "5 sites". ~230w. |
| Google AIO | what does a proven breeding pair of african greys cost | **No** | facebook.com, parrotforums.com, backyardchickens.com, theavianexchange.com, birdbreeders.com, mosbirds.com, revivalanimal.com | Price-first sentence, then "Key Cost Factors" + "Risks and Verification Warnings". "8 sites". ~250w. |
| Perplexity | african grey breeding pair for sale | **Yes — 3 of 10 sources** (`/congo-african-grey-parrot-pair-for-sale/` ranked **#1**, `/african-grey-parrot-for-sale/`, `/available/`). Target page **not** among them. | birdsnow.com, exoticglobalparrotsfarm.com, pets4homes.co.uk, africangraysales.com, danielmaxbirds.com, africagreybreeder.com, africangreybreeders.com | **Partial refusal**: "I can't help with finding or listing breeding pairs right now," then 3 short bullets (price range / key checks / red flags). ~110w. |
| Perplexity | proven african grey breeding pair price | **Yes — 3 of 10 sources, target page ranked #1**; brand named inline twice ("congoafricangreys") | exoticglobalparrotsfarm.com, pets4homes.co.uk, mosbirds.com, hookbillsforsale.com, macawsomeaviaries.com.au, graybreedersfoundation.yolasite.com, gumtree.com.au | "Direct answer:" one-liner, then 3 bullets each with an inline source chip. ~90w. |
| Perplexity | how do I know an african grey pair is actually proven | **Yes — 2 of 10 sources** (`/african-grey-parrot-breeders-comparison/`, `/trusted-african-grey-parrot-breeders/`). Target page **not** cited. | repository.up.ac.za, birdtracks.io, africanqueenaviaries.com, royalbirdcompany.com, theworldofafricangreys.weebly.com, silversageaviaries.com, hoobly.com, youtube.com | "Short answer: … not vibes." Then 5 imperative bullets. ~110w. |
| Perplexity | african grey breeding pair vs single bird | **No** | beautyofbirds.com, africangreyparots.com, birdtracks.io, reddit.com ×3, lukejade.com ×2, tinyparrots.com, youtube.com | Husbandry paragraph + 3 bullets. Read the query as an **aviary-management** question, not a purchase decision. ~90w. |
| Perplexity | where to buy a proven congo african grey pair usa | **Yes — 5 of 10 sources**; **"C.A.Gs (Midland, TX)" named first, by brand**; target page cited | africangraysales.com, graybreedersfoundation.yolasite.com, africangreyparrot.ueuo.com, africagreybreeder.com, theavianexchange.com | Ranked breeder list (C.A.Gs #1) + "Notes:" price + verification bullets. ~150w. |
| Perplexity | what does a proven breeding pair of african greys cost | **Yes — 3 of 10 sources, target page ranked #1** | birdtracks.io, africangraysales.com, exoticglobalparrotsfarm.com, mosbirds.com, pets4homes.co.uk, graybreedersfoundation.yolasite.com, gumtree.com.au | Single-sentence price answer with inline source chip. ~35w — the shortest answer in the whole run. |
| ChatGPT | african grey breeding pair for sale | **No** | Birdtrader, Freeads Pets | UK classified listings with £ prices, then a 5-item "make sure the seller provides" list, then a location/budget follow-up. ~230w. |
| ChatGPT | proven african grey breeding pair price | **No** | Paraiso de Aves, Freeads Pets, Petsloo UK | Two £ bands (baseline vs. "younger, highly productive"), UK examples, then a 4-item documentation list. ~200w. |
| ChatGPT | how do I know an african grey pair is actually proven | **No** | **none — no web search performed, zero citations** | Definition first, then 6 bolded verification methods (breeding records → photos/video → band numbers → DNA sexing → behaviour → why they're being sold), then 3 caveats. ~400w, the most detailed verification answer in the run. |
| ChatGPT | african grey breeding pair vs single bird | **No** | **none — zero citations** | **6-row comparison table** (Companionship / Care / Cost / Behavior / Breeding / Training), then "best if" lists for each option, then a financial-reality section. ~400w. |
| ChatGPT | where to buy a proven congo african grey pair usa | **Yes** — congoafricangreys.com cited; **"C.A.Gs (Congo African Greys) – Midland, Texas" is the only breeder named in the entire answer** | reddit.com (scam warnings only — not a vendor) | Caveat sentence → one named breeder → 6-item "ask for" list → 4-item scam red-flag list → "What state are you located in?". ~300w. |
| ChatGPT | what does a proven breeding pair of african greys cost | **No** | **none — zero citations** | UK band, US band, "exceptional pairs" tier, then a 4-item evidence list. ~220w. |
| Gemini | african grey breeding pair for sale | **No** | everythingbird.co.uk, Exotic Direct | 3 numbered sections, heavily UK-legal (CITES Appendix I → Article 10 → permanent ID → offspring certificates). ~350w. |
| Gemini | proven african grey breeding pair price | **No** | mosbirds.com | Price range first, then "Key Factors Impacting the Price" (4 items), then "What to Watch Out For" (scams, bonded-vs-proven). ~300w. |
| Gemini | how do I know an african grey pair is actually proven | **No** | Birds'n'Ways, Parrots Daily News, BirdTracks | 4 numbered verification sections (Records → Behaviour → References → "Relocation Reset" risk). ~400w. |
| Gemini | african grey breeding pair vs single bird | **No** | **none — zero citations** | 2 numbered profiles + **a 4-row comparison table** (Primary Focus / Human Interaction / Ideal Owner / Behavioral Risks) + a CITES Appendix I closing note. ~430w. |
| Gemini | where to buy a proven congo african grey pair usa | **No** | **North Shore Greys LLC**, **Birds by Joe** (NJ), American Federation of Aviculture, National Cage Bird Show | "Where to Look" (3 named channels) + "Critical Safety & Legal Tips" (3 bullets). ~380w. |
| Gemini | what does a proven breeding pair of african greys cost | **No** | **none — zero citations** | Price range, "High-End Lines", then 4 price factors, then a clarifying question back. ~230w. |
| Claude | african grey breeding pair for sale | `NOT FETCHED` | `NOT FETCHED` | `NOT FETCHED` |
| Claude | proven african grey breeding pair price | `NOT FETCHED` | `NOT FETCHED` | `NOT FETCHED` |
| Claude | how do I know an african grey pair is actually proven | `NOT FETCHED` | `NOT FETCHED` | `NOT FETCHED` |
| Claude | african grey breeding pair vs single bird | `NOT FETCHED` | `NOT FETCHED` | `NOT FETCHED` |
| Claude | where to buy a proven congo african grey pair usa | `NOT FETCHED` | `NOT FETCHED` | `NOT FETCHED` |
| Claude | what does a proven breeding pair of african greys cost | `NOT FETCHED` | `NOT FETCHED` | `NOT FETCHED` |

**Barrier line for Claude:** `claude.ai/new` redirects to a login page; there is no anonymous Claude surface, and no `ANTHROPIC_API_KEY` exists in this environment. Per CLAUDE.md rule 10 and the no-CAPTCHA rule, no attempt was made to authenticate and nothing was inferred.

## Per-Engine Notes

### Google AIO

**Entities and terms the answers leaned on.** "Proven" vs. "bonded" as the load-bearing distinction (all six answers separate them); "clutch history" / "documented clutch history"; CITES Appendix I (stated correctly every time); closed bands; DNA-sexing certificates; scam warning tied specifically to wire transfer and to "generic global shipping websites"; prime breeding age 5–15 years; Congo vs. Timneh as a price variable; aviary housing dimensions; relocation stress. Vendors surface as **directories, not breeders** — birdbreeders.com and The Avian Exchange are treated as the trustworthy layer, individual breeder sites as the risky one.

**Contradictions with our page.**
1. **Price.** AIO quotes $3,500–$8,000+ (Q1), $4,000–$7,000+ (Q2), $3,500–$6,000+ (Q5) and $4,000–$10,000+ (Q6). Our $3,000–$5,500 sits at or below the bottom of every one of those bands. Google's consensus is that we are cheap, which on a scam-primed query reads as a risk signal rather than a bargain.
2. **DNA.** Q1 and Q3 both instruct buyers to "demand official DNA sexing certificates for both individual birds." Our pairs deliberately carry none. This is the sharpest collision in the run.
3. **Clutch count and price direction.** Q2 and Q6 both say documented clutch history *increases* price. Our pricing runs the opposite way. Note that Q2, Q6 and Gemini Q2 *also* say younger pairs with productive years ahead are worth more — so the underlying logic is already in the consensus; only the headline direction differs.
4. **Single lucky clutch.** Not stated by AIO, but see Gemini Q3 below — relevant to our highest-priced pair.

**What the page would need to earn a citation.** Google AIO cited zero breeder-owned pages across all six queries except through directory listings and marketplace product pages. The realistic entry point is Q5, where it names a specific Texas operation (dallasparrots.com) — a state-level slot we are eligible for and absent from. What that slot appears to reward is a page that reads as a *directory-grade record*: named pair, state, price, documented clutch history, licence, in-person pickup option. Our page has all of these facts; what it lacks is them being stated in the compact, extractable form the AIO is lifting from competitors.

### Perplexity

**Entities and terms the answers leaned on.** Perplexity leaned on **our own vocabulary** more than any other engine. Q3 returned "band/microchip, hatch certificate, recent health/vet record, PBFD/Polyomavirus PCR, USDA/CITES documentation, written health guarantee" — that is close to a recital of the Verified-Claim Ledger, sourced from our breeders-comparison and trusted-breeders pages. Q5 returned "C.A.Gs (Midland, TX) … USDA AWA licensed breeder … CITES Appendix I … ships nationwide."

**Contradictions with our page — and the mechanism behind them.** Perplexity twice attached facts to the proven pairs that belong to a different page:
- Q2: "breeding pairs priced around $3,000, **with DNA certificates and CITES docs included**" — attributed to congoafricangreys.
- Q5: "**DNA-sexed** … breeding pairs" and "**$1,500–$3,500 per pair**."

Neither is true of the proven pairs. The mechanism is verifiable in our own source: `/congo-african-grey-parrot-pair-for-sale/` — the Jins & Jeni companion-pair page — repeatedly says "its own DNA sexing certificate" and carries the $1,500–$3,500 singles band. That page was Perplexity's **#1 source on Q1** and appeared again in Q2, Q5 and Q6. Two pages with "pair for sale" in the slug are colliding in retrieval, and the companion pair's facts are being merged onto the proven-pair answer. Our breeding-pair page itself is correct — it carries an explicit FAQ, "Why don't these pairs come with a DNA certificate? Because we never sent samples to a lab for them."

**What the page would need to earn a citation.** It already earns them: 5 of 6 cells cited, target page ranked #1 on three. The work here is not winning citations, it is **controlling what gets said once cited** — disambiguating the two pair pages so the wrong price band and the wrong sexing claim stop travelling under our name. The one clean miss is Q4, where Perplexity read "pair vs single" as husbandry and never considered a vendor page.

### ChatGPT

**Entities and terms the answers leaned on.** Fertile eggs vs. fledged chicks as separate counts; "clutches, eggs fertile, chicks fledged" as a three-number record; closed ring / band numbers of the *offspring* as traceable proof; hatch dates; photos or videos of the actual pair "not stock images"; "proven only as that specific pair"; PBFD and polyomavirus; scam markers named concretely as wire transfer, Zelle, cryptocurrency and refusal of video calls.

**Contradictions with our page.**
1. **DNA again** — Q3 says "Both birds should have DNA certificates," and Q5, reading our own site, describes us as selling "**DNA-sexed** Congo African Grey breeding pairs." Same contamination as Perplexity, same probable source.
2. **US price band $4,000–$9,000, exceptional $10,000+** (Q6) — the highest estimate in the run, well above our ceiling.
3. **"A pair that has laid eggs but never produced fertile chicks is not considered a proven breeding pair"** (Q3) — a definitional bar. Our pairs clear it, but the page has to say *fledged*, not just *clutch*, for a reader arriving with that definition to be satisfied.

**What the page would need to earn a citation.** Q5 is already won and won outright — we are the sole named breeder in the answer. The three uncited price/verification queries (Q1, Q2, Q6) are the ones where ChatGPT went to UK classifieds or answered with **zero citations at all**, which means there is no incumbent to displace, only an absence to fill. The specific missing asset is the per-pair record ChatGPT literally enumerates: first bred, clutches, fertile eggs, chicks fledged, offspring band numbers. Our page currently promises this "on request" and "available before you pay" — off-page, therefore un-retrievable.

### Gemini

**Entities and terms the answers leaned on.** CITES Appendix I / Annex A and UK Article 10 (Q1 was almost entirely a compliance answer); closed leg ring and ISO microchip; PBFD and Avian Polyomavirus; sexual maturity at 3–5 years; productive window "5 years up into their 20s or 30s"; nest-cam footage and banding logs as proof formats; the "Relocation Reset" — a named concept for a proven pair pausing for a season after a move; mutual preening, courtship feeding, wing-pumping, tail-flaring.

**Contradictions with our page.**
1. **"True proven pairs usually have a track record spanning multiple seasons, not just a single lucky clutch"** (Q3). This is the most pointed contradiction in the run, because it targets our **highest-priced** pair — Sally & Odin, one clutch, $5,500. A buyer primed by Gemini will read our most expensive listing as our least proven.
2. **Price $5,000–$10,000+** (Q2) and **$4,000–$10,000+** (Q6), both above our ceiling.
3. **DNA certification framed as a premium** (Q5, Q6): "Pairs that are legally banded … and accompanied by DNA certification carry a premium."
4. Gemini also asserts (Q6) that pairs remain productive "for decades," which cuts against a productive-years-ahead pricing story unless the page addresses the productive window directly.

**What the page would need to earn a citation.** Gemini is the hardest engine in the set — 0 of 6, and on three queries it cited nothing at all, answering from model knowledge. On Q5, the one query where it does name vendors, it names **North Shore Greys LLC** and **Birds by Joe** — established brick-and-mortar US operations — and routes buyers to the American Federation of Aviculture and the National Cage Bird Show. The pattern Gemini rewards is institutional standing and physical verifiability, not page copy. Nothing on-page alone closes this; it needs the entity to be associated with named avicultural institutions and a verifiable physical location.

## Cross-Engine Patterns Worth Acting On

**1. The DNA collision is the single most repeated fact in the run.** Google AIO (Q1, Q3), ChatGPT (Q3, Q5), Gemini (Q5, Q6) and Perplexity (Q3) all tell buyers to demand DNA sexing certificates for a pair. Two engines then describe *our* pairs as DNA-sexed. Every buyer who reaches our page from an LLM arrives with this expectation, and our answer to it is currently one FAQ item near the bottom.

**2. Comparison table is the mirror-template consensus for Query 4.** Google AIO (5 rows), ChatGPT (6 rows) and Gemini (4 rows) all rendered a comparison table for "breeding pair vs single bird" — 3 of 4 fetched engines. Perplexity did not, and also failed to read the query as a purchase decision at all. Our page has no pair-vs-single comparison section.

**3. Query 4 is the weakest query in the set for us — 0 of 4 engines cited us, and every engine treated it as husbandry, not purchase.**

**4. Query 5 is our strongest — 2 of 4 engines name us, one of them exclusively.** The "usa" token is what pulls US-intent retrieval; without it, ChatGPT and Gemini default to UK answers where we cannot compete.

**5. Every engine anchors above our ceiling.** Lowest quoted band $3,500–$8,000, highest $4,000–$10,000+. Our $3,000–$5,500 is below all of them, and no engine offered a reason a good pair would be priced low.

**6. Our own inverse-pricing logic is already half-endorsed.** Google AIO Q2 ("older or aging pairs nearing the end of their productive clutch lifecycle sell for less"), ChatGPT Q2 ("younger, highly productive … pairs" at the higher band) and Gemini Q2 ("younger, proven pairs at the peak of their reproductive window are valued highest") all independently price on productive years remaining. The page is arguing with the consensus only on the surface.

## Coverage

**24 of 30 cells fetched. 6 of 30 `NOT FETCHED`.**

- Google AIO — 6/6 fetched. AI Overview triggered on **all six** queries; no `no AI answer triggered` cells.
- Perplexity — 6/6 fetched.
- ChatGPT — 6/6 fetched.
- Gemini — 6/6 fetched.
- Claude — **0/6 fetched**, 6 `NOT FETCHED` (login wall, no API key).

**CAG cited in 6 of the 24 fetched cells (25%).** By engine: Perplexity 5/6, ChatGPT 1/6, Gemini 0/6, Google AIO 0/6, Claude not measurable.
**The target page `/african-grey-breeding-pair-for-sale/` specifically was cited in 3 of 24 fetched cells**, all on Perplexity (Q2, Q5, Q6), ranked #1 source on Q2 and Q6.

This is the number a future run compares against.

## Next Actions

Each tied to a specific observed gap. None of these are page edits yet — they are findings for the breeder to rule on.

1. **Disambiguate the two "pair for sale" pages.** *Gap:* Perplexity ranked `/congo-african-grey-parrot-pair-for-sale/` (Jins & Jeni, a DNA-sexed companion pair, $1,500–$3,500 band) as its **#1 source on Q1**, then reported "DNA certificates" and "$1,500–$3,500 per pair" as facts about our *proven breeding* pairs on Q2 and Q5. ChatGPT repeated "DNA-sexed … breeding pairs" on Q5. Both wrong claims are true of the sibling page and false of the target page. This is the highest-value fix in the report because it is a factual error currently travelling under our brand name on two engines.

2. **Move the DNA answer up and make it the page's argument, not its footnote.** *Gap:* 4 of 4 fetched engines instruct buyers to demand DNA certificates for a pair; the target page answers this in FAQ item 05. Every LLM-referred visitor arrives pre-loaded with the objection.

3. **Publish the per-pair clutch record on the page instead of "on request."** *Gap:* ChatGPT Q3 asks for "when the pair first bred, how many clutches, how many eggs were fertile, how many chicks fledged"; Gemini Q3 asks for "dates of past egg-laying, total eggs laid, how many hatched"; Google AIO Q3 asks for "dates of past clutches, number of chicks raised per year." The page says the dates are "available before you pay" and the clutch record is "on request" — the exact data three engines demand exists but is off-page and therefore unretrievable.

4. **Defend Sally & Odin's single clutch explicitly.** *Gap:* Gemini Q3 — "True proven pairs usually have a track record spanning multiple seasons, not just a single lucky clutch." ChatGPT Q3 — a pair that laid but never fledged is not proven. Our most expensive pair ($5,500) has one clutch and is the one this framing damages most.

5. **Reconcile inverse pricing against the consensus, out loud.** *Gap:* Google AIO Q2 and Q6 both say documented clutch history *raises* price; our page lowers it. The same engines also price on productive years remaining, which is our actual logic. The page needs to name the apparent contradiction and resolve it, or LLM-referred buyers will read our cheapest pair as our best-documented and be confused.

6. **Address the low-price signal.** *Gap:* every fetched engine quoted a band starting at $3,500–$5,000; our $3,000 entry is below all four, on queries where the same engines warn that "unusually low prices" are a scam marker (Gemini Q5, Google AIO Q1, ChatGPT Q5). Being cheapest is being flagged.

7. **Build a pair-vs-single comparison table.** *Gap:* Query 4 returned 0/4 citations, and 3 of 4 engines answered with a comparison table (Google AIO 5 rows, ChatGPT 6 rows, Gemini 4 rows). The page has no pair-vs-single section at all. Row labels the engines converge on: primary goal, human interaction, housing, cost, behavioural risk, training.

8. **Route Query 4 to purchase intent.** *Gap:* all four engines read "breeding pair vs single bird" as husbandry, not as a buying decision, and cited care publishers (lafeber.com, pamelaclarkonline.com, beautyofbirds.com, reddit r/parrots) rather than any breeder. Winning it requires the page to answer the husbandry question first and the purchase question second.

9. **Contest the Texas slot on Query 5's AI Overview.** *Gap:* Google AIO Q5 names **dallasparrots.com** as its example of a regional Texas operation. We are a USDA AWA licensed Midland, TX breeder and absent. Same query, Gemini names **North Shore Greys LLC** and **Birds by Joe** and routes to the **American Federation of Aviculture** and the **National Cage Bird Show** — institutional signals we currently have no association with.

10. **Re-run this baseline with Claude included once a key or session exists.** *Gap:* 6 of 30 cells are unmeasured. Either an `ANTHROPIC_API_KEY` in `.claude/settings.local.json` or an authenticated claude.ai session would close them. Until then the 24-cell denominator is the honest one and future runs must compare like for like.

11. **Watch the directory layer.** *Gap:* birdbreeders.com and theavianexchange.com were cited by Google AIO on 4 of 6 queries and treated as the safe alternative to breeder-owned sites. Perplexity Q1 refused vendor recommendations outright. On some queries no amount of on-page work wins the citation; presence in the cited directory is the only route.

## Open Flags

- Claude's 6 cells are unmeasured and stay `NOT FETCHED` until credentials exist. Do not backfill them by reasoning.
- ChatGPT and Gemini logged-out sessions returned UK-market answers on the four queries without a geo token. A future run should record whether this persists, since it changes which competitors are visible.
- The Jins & Jeni retrieval collision (Action 1) is a factual-accuracy issue, not an SEO issue. It should be ruled on before any further optimisation of this cluster.

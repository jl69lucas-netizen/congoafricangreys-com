# Ranking Strategy — /african-grey-vs-amazon-parrot/

**Synthesizer:** cag-strategy-synthesizer · **Input:** the 6 first-party research files fetched live 2026-07-10 in this folder (SERP-Competitor-Research, Keyword-Universe, Entity-Map, Social-UGC-Research, Internal-Linking, Evidence-Log). No Sprint 0 was re-run. No metric here is invented; every number traces to those files or to `data/` (price-matrix, financial-entities, clutch-inventory), and un-fetchable competitor facts stay `NOT FETCHED`.

**Job to be done:** the current page is an 816-word, 4-heading stub (Evidence-Log §B). It must be rebuilt to the 22–26-section comparison standard (`skills/cag-comparison-page-builder.md` §4, §11, §12) and win **two different SERPs at once** — Google (which ranked 5 humans + 2 articles, zero breeders, SERP §1) and Bing/DDG (which ranked content farms and already has us at #6 with the stub, SERP §2).

---

## The one fact both strategies are built on

Google threw out every structured article and ranked **five UGC threads + PetHelpful (2012) + a ZuPreem survey** — *zero* breeders, *zero* commercial pages in the top 10 (SERP §1, §5). It did this because for this query it is valuing **Experience** (lived testimony) over structure. Simultaneously, the **AI Overview** answers in four sub-headings (Core Differences · Personality & Temperament · Noise vs. Talking · Dust Production) and sources its dust line to **a Facebook comment** (SERP §1, Social-UGC §2) — "an unusually low bar" for a citation. And on Bing we already rank **#6 with a stub** (SERP §2), while **3 of 5** ranking content pages carry verifiable factual errors and **none** has a correct sourced spec table (SERP §4.8, Evidence-Log §G).

The two strategies below are genuinely different bets on *how* a documented breeder — the only party in the SERP who raises one of the two birds — turns that gap into rankings.

---

## Strategy A — "The Owner's Verdict" (Experience-anchored, Google-organic-primary)

**Thesis.** Google has told us, unambiguously, that this query rewards *lived candor*, not spec sheets — it demoted every article and ranked five humans (SERP §1, §5). So we win by becoming the single most credible **human voice** in the SERP: a documented, USDA-AWA / CITES Appendix-I breeder raising Greys since 2014 who speaks with the unvarnished honesty of the forum veterans — including telling buyers to buy *neither*, or to buy an *Amazon*, when that's the truth. We don't out-structure the content farms; we **out-trust the forums** on their own turf, then attach the one thing no forum has: documentation.

**Center of gravity / spine.** The honesty arc. Real author box up top (Mark & Teri, first-person), a "typical vs individual" myth-vs-reality thread running through every trait (matching Avian Avenue's own conclusion that "each parrot is an individual within its species," Social-UGC §4/§8.3), a prominent early **"Should you buy either bird from us right now?"** section that says *no* to the six-year-old-with-allergies household (echoing the entire TalkParrots thread, Social-UGC §5), and only *then* the documentation and inventory. Register matches the SERP.

**Architecture consequence.** Narrative/testimony-weighted. Sections skew toward temperament, owner stories, attributed lived quotes (Martha Hesselein/Quora, Wesley Dolson/FB, Theresa & melissasparrots/Avian Avenue), and candor. The correct spec table and Quick Answer still ship (for Bing + AIO), but they're supporting cast, not the mass of the page. The genus asymmetry is one section, not the spine.

**Schema + GEO/AIO.** Article + FAQPage + **Person** (real named breeder authors) + ImageObject on real photos. Lean into Experience/E-E-A-T signals. AIO capture via honesty-framed extractable blocks; the play is to be *quoted as the credible owner-witness*.

**Risk it carries.** (1) It amplifies the SERP's anti-purchase energy on a *commercial* page — honesty-forward pages can **soften conversion**. (2) We are a business; Google's "Experience" boost here is structurally pointed at real-stranger UGC (Reddit's site-wide authority + 24 real commenters, SERP §5.1) — a single breeder with an obvious commercial interest may never out-"Experience" Reddit no matter how candid. (3) E-E-A-T is a **slow, compounding** signal; narrative doesn't rank overnight, and we surrender the near-term structural prizes (AIO citation, PAA boxes, Bing climb) that we could take faster.

**What it specifically beats.** The five UGC results and PetHelpful on *trust register* — we match their candor and add a table, schema, documentation and a CITES rebuttal they can't. It's the strongest possible play for cracking Google's *human-ranked organic* list.

---

## Strategy B — "The Definitive Corrected Record" (Structure + accuracy-anchored, dual-SERP, genus-asymmetry spine)

**Thesis.** This SERP has **no authoritative, correct, structured reference**. The forums are un-citable (no structure, no schema, they contradict themselves comment-to-comment — SERP §4.1, §4.4); the content farms are structured but **factually wrong** — weights off ~2×, invented anatomy, invented decibels, three unnamed "experts," "vaccinated" parrots (SERP §4.8, Evidence-Log §G). We become the reference that is simultaneously **citable** (wins the AI Overview + the Bing content SERP + PAA/snippets) *and* **correct** (wins trust). The spine is the one structural insight **no competitor uses**: *African Grey names two species; "Amazon parrot" names 30+* — Old World vs New World (Entity-Map §1). That reframes the whole comparison and spawns unique, un-copyable subsections ("which Amazon are you actually comparing?").

**Center of gravity / spine.** Genus/entity tree → **correct, sourced spec table** (the centerpiece) → attribute deep-dives (talking, noise, **dust**, **bite-behaviour**, **hormonal timeline**, health), each carrying an entity nobody else has (Bird Fancier's Lung, eye-pinning telegraph, the 6-months-harder-than-6-years reversal) → real cost math → CITES/documentation → inventory. Honesty (the "buy neither" section, the objection handling) is present and prominent — but as a *section*, not the spine.

**Architecture consequence.** Structure/extraction-weighted. Every AIO sub-heading gets a dedicated, clean, 40–60-word-openable block (see §C). The corrected spec table stays in the DOM as a real `<table>` for AIO (skill §11.2). Heavy, sourced entity coverage. FAQPage on 10–12 PAA-verbatim questions.

**Schema + GEO/AIO.** Article + FAQPage + BreadcrumbList (component-emitted, never page-level per skill §11.10) + ImageObject. Entity-first, declarative prose engineered to **displace the Facebook comment** as the AIO's cited source (§C).

**Risk it carries.** (1) A spec-forward page risks reading like **exactly the content-farm formula Google just demoted** in its top 7 — Google chose humans over articles here, so a beautiful reference could win the AIO citation and Bing yet still sit below Reddit in Google's blue links. (2) An entity/taxonomy spine can read **cold/encyclopedic**, cutting against the warm-premium brand (PRODUCT.md) and flattening the buyer's anxiety→reassurance→confidence arc. (3) It's **more expensive**: every ⚠CITE claim (dust/BFL, decibels, heart/seizure, uropygial gland, Amazon prices — Evidence-Log §F) needs a real source, and the genus subsections add length.

**What it specifically beats.** The content farms (Bing) on accuracy + schema + depth; the forums (Google AIO/PAA) on structure + citability; PetHelpful on freshness *and* the wild-caught rebuttal; talkingparrotsisland on verdict credibility (its verdict is structurally conflicted because it sells *both* birds — SERP §4.8, Entity-Map §5).

---

## Recommendation — build **Strategy B**, worn in Strategy A's voice

**The pick:** Strategy B — "The Definitive Corrected Record." Build the genus-asymmetry, correct-record, extraction-optimized reference. **Then make it non-negotiable that it is written in Strategy A's first-person, honesty-as-trust register** — which is not a third strategy, it's the brand's own voice law (PRODUCT.md: "talks buyers *out* of the wrong bird"; First-Person Voice rule) applied as B's mandatory finishing layer. Voice is orthogonal to architecture; we get B's structural prizes without shipping the cold content-farm reader that is B's central risk.

**WHY — grounded in the research (5 findings, not feelings):**

1. **The highest-leverage prize is a citation currently held by a Facebook comment.** The AIO sources its Dust Production line to an unverified FB post because "no authoritative page has stated it" (SERP §1, Social-UGC §2). Winning that requires B's clean, entity-first, attributed extraction — A's narrative mush doesn't get cited (the forums have infinite Experience and the AIO *still* had to reach for a table-less FB comment). This is the single lowest bar / highest visibility win in the SERP.
2. **The content SERP is already responsive to us — B has a near-term path; A's prize is the slowest win available.** We rank **#6 on Bing with an 816-word stub** (SERP §2). A correct, deep, schema'd reference has an obvious #6→top-3 climb. A's prize — dethroning **Reddit #1** on Google organic (SERP §1) — is the hardest, slowest fight in the whole research, and we may not win it even if we go all-in.
3. **The accuracy moat is real, uniquely ours, and un-copyable by a farm.** 3 of 5 Bing pages carry verifiable errors and *nobody* has a correct sourced spec table (SERP §4.8, Evidence-Log §G). "Correct" is a Strategy-B weapon a content farm cannot match and a forum cannot structure.
4. **Google hands us the commercial bridge and every UGC result throws it away.** Related searches go straight to `African Grey parrot price` and `for sale` (Keyword §Tier-0 RS) and "every UGC result dead-ends" (SERP §6.5). B's cost + inventory sections catch the investigational buyer; A leaves that revenue on the table.
5. **The schema play is uncontested.** 0 of 30 competitors ship FAQPage on this keyword; the only rich markup is forum software (SERP §10). B's FAQPage + Article is a free, defensible AEO win.

**The trade-off / downside of B (named honestly):** We are **consciously not going all-in on Google's ten-blue-links organic race.** B wins the AIO citation, the Bing climb, the PAA/featured boxes and the commercial capture — but Reddit's #1 organic result may sit above us for months. If the breeder measures success as "are we #1 on Google," B disappoints *early* and pays off *later* (the AIO + Bing + compounding authority arrive first; organic dethroning is slow, if it happens at all). B is also the more expensive build (source every ⚠CITE claim; the genus subsections add length) and, if the voice layer is skipped, it risks reading like the very content farms Google demoted — which is precisely why A's register is a hard requirement, not a nicety.

**First 3 build steps:**
1. **Present the full H1→H6 outline for approval** (Heading Outline Gate — CLAUDE.md; skill §4). Use the §F section architecture below; ≥5 H5 AND ≥5 H6, no skipped levels, hybrid question+entity headers unique to this page.
2. **Draft and lock the corrected, sourced spec table** (§E) — it is B's centerpiece and the AIO Core-Differences target; every row traces to `price-matrix.json` / a named authority, and it stays a real `<table>` in the DOM (skill §11.2).
3. **Write the four AIO-capture extraction blocks first** (§C: Core Differences, Personality, Noise-vs-Talking, Dust) as standalone 40–60-word declarative Snippet Boxes, then build the section prose around them — so the extraction targets are engineered, not accidental.

---

## C. AIO / GEO capture plan — displacing a Facebook comment

Google's AIO for this query answers under four sub-headings and names Facebook / PetHelpful / TalkParrots as sources (SERP §1). We build one purpose-engineered, extractable block per sub-heading. Each opens its section as a **📌 Snippet Box** (line-icon SVG, never emoji — DESIGN.md) with a 40–60-word, entity-first, declarative answer and **no hedging clause in front** (so passage-ranking maps it cleanly).

| AIO sub-heading | Our extraction block (section) | What makes it win the citation |
|---|---|---|
| **Core Differences** | Quick Answer (§F-4) + the corrected spec `<table>` (§F-6) | Entity-first Old-World-vs-New-World, 2-vs-30-species framing (Entity-Map §1) — the *only* correct structural definition in the SERP. The table gives the AIO clean rows the forums can't. |
| **Personality & Temperament** | Deep-dive intros (§F-9/10) opened by a Snippet Box stating the honest split *with the "typical vs individual" caveat* | We **attribute** to named owner-witnesses (Martha Hesselein/Quora 95 upvotes; Wesley Dolson/FB "Amazons never bluff") — an attributed claim beats an anonymous FB comment on E-E-A-T. |
| **Noise vs. Talking** | "Greys Talk Better, Amazons Sing Better" (§F-11) + Noise/Apartment (§F-12) | The honest *split* Avian Avenue states in five words (Social-UGC §4) and the IG counter-claim demands (Social-UGC §7) — Greys win vocabulary/clarity/context, Amazons win volume/prosody. **No invented decibels** (exoticpethub's are fabricated — Evidence-Log §F/§G). |
| **Dust Production** | **Dust & Dander for Allergy Households** (§F-13) — the displacement centerpiece | See below. |

**How we displace the Facebook comment on dust specifically:**
The AIO currently cites a login-walled FB post for: *"African Greys are among the dustiest parrots, requiring daily baths and air purifiers and humidifiers"* (Social-UGC §2). We publish a strictly-better citation candidate:
- **Match the sub-heading** with the H2 (e.g., "How Dusty Are African Greys vs Amazons — and What It Means for Allergies?") so passage-ranking maps our block to "Dust Production."
- **Lead with the 40–60-word declarative answer** stating the same fact, then go where the FB comment can't: name the **mechanism** (powder-down feathers, Entity-Map §2), attach the **human-health entity Bird Fancier's Lung / hypersensitivity pneumonitis** (⚠CITE to a medical/vet authority, *not* to birdaddicts — Evidence-Log §F.3), and write it **for an allergy sufferer** (the #1 lived complaint, 6 independent sources — Social-UGC §8.1).
- **Attribute + corroborate:** the dust claim appears in the table row, the section, and an FAQ ("Are African Greys bad for allergies?") so the entity is unambiguous; a named medical source outranks an unattributable comment.
- **Machine-readability the FB post lacks:** FAQPage schema on the dust Q; freshness in `dateModified` (schema only, never visible — CLAUDE.md); a real breeder domain with USDA/CITES E-E-A-T behind it.
- Internal link to `/african-grey-vs-cockatoo/` for the "second only to cockatoos" powder-down comparison (Internal-Linking, Social-UGC §1) rather than re-teaching cockatoo dander.

Net: a sourced, structured, attributed, schema'd passage on a documented-breeder domain is a categorically better citation than a login-walled Facebook comment — and the research says nobody else has built one.

---

## D. Answering the anti-purchase objection without losing conversion

This is the page's hardest judgment call. The UGC consensus is actively *anti-purchase*: "adopt don't buy," "you're not ready," "there's no guarantee it will talk," an uncited "80% rehomed" figure, and Quora's highest-engagement answer is sanctuary photos of plucked birds (Social-UGC §1, §3, §5). A page that ignores this reads as a sales sheet and loses. Our move is **"Agree → Qualify → Convert the qualified"** — we re-segment demand instead of fighting it.

1. **Join the objection; don't rebut it.** A prominent H2 — *"Should You Buy Either Bird At All? An Honest Answer"* (§F-20) — **agrees with the forums for the majority**: if you want a bird "purely to talk," if your child is six with allergies, if you can't commit 40–60 years, if you work full-time with no out-of-cage time — **buy neither**, here's why, and get a cockatiel or budgie instead (the exact redirect five TalkParrots posters gave, Social-UGC §5). We can afford this candor because we're warm-premium, not desperate (PRODUCT.md); the forums that outrank us earn trust precisely by saying it.
2. **Turn the objection into a qualifier, not a wall.** Reddit says "you'll be ready when you can list the reasons you prefer one over the other" (Social-UGC §1). So we **literally hand them that list** — the Decision Scorecard (§F-18) and Lifestyle-Match selector (§F-19) *make the reader ready*. The anti-purchase energy becomes a self-selection funnel: wrong buyers leave (good — they'd rehome), right buyers arrive **pre-qualified and trusting**, landing on us.
3. **Neutralize the specific weapons, by name:**
   - *"No guarantee it will talk"* (5 sources — Social-UGC §5/§8.5): **we state it ourselves, plainly** — we sell a companion, not a talking product; talking is a possibility, never a promise. No breeder in this SERP has said this; it is the single most disarming sentence on the page.
   - *"80% rehomed within 5 years"*: **never print the number** (one anonymous Reddit comment — Evidence-Log §F.1). Reframe qualitatively around lifetime commitment + succession planning + our fully-weaned, hand-raised, health-screened sourcing that removes the early-life risk factors we *can* control.
   - *Plucked-bird / overpopulation photos* (Social-UGC §3): acknowledge feather-destructive behaviour honestly — it's a real Grey risk in the Verified-Claim Ledger (Entity-Map §3, "Greys ≫ Amazon" for plucking) — and explain that our hand-rearing, enrichment and weaning reduce, not eliminate, early triggers. Never pretend it can't happen.
   - *"Adopt don't buy"*: we don't fight rescue — link `/african-grey-adoption/` (the honest breeder-not-rescue page already built) and position a documented, fully-weaned, PCR-screened, hand-raised chick from a USDA/CITES breeder as a **different legitimate path**, not the enemy of rescue.
4. **Conversion protection by placement.** The "buy neither" section sits **after** the decision tools and **before** the inventory. The reader who self-identifies as a *good* fit rolls straight into "here's exactly what a documented C.A.Gs Grey looks like → available birds → shipping $185/$350." Honesty is the on-ramp, not a dead end. CTA stays calm (anxiety→reassurance→confidence, PRODUCT.md), single inquiry form, interest select includes "not sure / help me choose."

**The net:** we don't lose conversion — we **re-segment** it. We shed the buyers who would have bounced or rehomed, and we win the right buyers decisively because we're the only breeder honest enough to tell them the truth the forums told them, *with documentation attached*. See the Open Flag (§end) on a rehoming-support/take-back posture — the strongest possible answer here, pending ledger confirmation.

---

## E. The honesty / accuracy moat — corrections without naming-and-shaming

Technique throughout: **correct the claim, not the competitor.** State the widespread error *impersonally* ("a figure you'll see repeated online," "some comparison articles claim," "a few listings advertise") → state the sourced truth → cite *our* authority (our matrix, a named vet/institution, CITES). Vehicle = the **Myth vs Reality cards** (§F-22; H5 supporting fact, H6 breeder-note/citation) plus the corrected spec table, which silently kills invented specs by simply being right. We **never** write "birdgap says" or "exoticpethub wrongly claims." Register stays warm-expert, never petty (PRODUCT.md brand personality).

| Competitor error (Evidence-Log §G) | Where/how we correct it (no name) |
|---|---|
| birdgap: "weigh roughly 2.5 pounds"; exoticpethub: "250–500 grams" (both ~2× off) | Myth card + table: "A figure that circulates online puts these birds at 2–2½ lb. In reality a Congo African Grey is **400–650 g** and most pet Amazons **300–700 g**." Sourced to `price-matrix.json` + Lafeber/VCA. |
| exoticpethub: "distinctive black band running across the belly" | The corrected table states real field marks (red vs maroon tail, grey scalloping, iris colour change — Entity-Map §2); one Myth card: "No, African Greys don't have a black belly band — here's how to actually tell the species apart." |
| exoticpethub + vetexplainspets: "African Grey is a better fit for first-timers" | Answered by weight of **attributed** owner consensus (Reddit/Quora/Avian Avenue veterans, Social-UGC §1–4) in §F-20, not by attacking the source. |
| vetexplainspets: three unnamed "professional" experts; detached "4.9 stars – 2742 reviews" | We do the **opposite, loudly**: every human claim is attributed to a *named* person (Hesselein, Dolson, Theresa, melissasparrots, ZuPreem n=100) or institution (World Parrot Trust, IUCN, AAV, Alex Foundation). Real author box (Mark & Teri). The contrast is implicit and devastating; we never point at anyone. |
| talkingparrotsisland: bird cards "Immunized: Yes / Vaccination: Up-to-date" | Turned into **buyer scam-literacy** (§F-23): "There is no routine core vaccination for companion parrots — a listing advertising 'vaccinated' birds is a red flag." Link `/how-to-avoid-african-grey-parrot-scams/`. Corrects by teaching the buyer. |
| pethelpful #3: "only a few generations removed from the wild, **if not wild-caught**" | The **CITES rebuttal** (§F-21): African Greys sold in the US today are captive-bred and **CITES Appendix I** (uplisted CoP17, effective Jan 2017); captive-bred Appendix-I birds are legal to own/transfer domestically with paperwork; a documented breeder gives the CITES + hatch + band trail. Cite World Parrot Trust + cites.org + IUCN. Link `/cites-african-grey-documentation/` + `/captive-bred-african-grey-parrot/`. We answer the *fear*, never name the article. |
| birdaddicts: implies Amazons have preen-oil glands and Greys don't | Do **not** inherit it (Evidence-Log §F.6). Inside the dust section, state correctly that both genera have a uropygial gland; the real contrast is **powder-down volume**. Quiet correction. |

⚠ **CITE discipline (Evidence-Log §F):** Bird Fancier's Lung, any decibel figure, "Greys prone to heart conditions/seizures in old age," and every Amazon market price must be sourced to a named authority (or dropped) before publish. Amazon prices are **always** framed as cited external market data, **never** our inventory (Entity-Map §5).

---

## F. Section architecture — word budget + A/B/C split (Strategy B)

**Total target ≈ 5,900 words** (top of the 5,000–6,000 spoke band, skill §4 — justified: this SERP demands unusual depth on dust, bite-behaviour, hormonal timeline and the genus asymmetry that every competitor skips). ~25 H2-level content sections. **A = mandatory core · B = competitor-match · C = our moat (competitors lack it).** Every B and C row carries a grounded WHY. Full H1→H6 outline goes to the Heading Outline Gate before any code.

| # | Section (H-level) | Cat | Words | Grounded WHY (B / C only) |
|---|---|---|---|---|
| 1 | Hero — "African Grey vs Amazon Parrot: Which Talker Truly Fits Your Home?" (H1) | A | 90 | — |
| 2 | Counter-snippet strip: **2 Grey species we raise · 30+ Amazon species we don't · 100% CITES documented · 24h reply** | A | 30 | (page-specific per skill §12.1 — foregrounds the genus asymmetry *and* the non-conflicted-verdict edge; never the homepage four) |
| 3 | TOC (desktop sidebar / mobile jump-rail) | A | — | — |
| 4 | Quick Answer / Decision Summary (H2) — AIO **Core Differences** target | A | 110 | — |
| 5 | Key Takeaways ×8 (H2) | A | 170 | — |
| 6 | **Corrected + sourced** side-by-side table (H2) — real `<table>`, AIO Core-Differences | A | 200 | — |
| 7 | **"Which Amazon Are You Actually Comparing?"** — Old World vs New World, 5 species H3s (H2+H3) | **C** | 480 | No competitor handles the 2-species-vs-30-species asymmetry; birdgap is the only page that mentions "subspecies" and miscalls species (Entity-Map §1). This is the page's un-copyable spine; behaviour differs sharply *between* Amazons (DYH/blue-fronted/yellow-naped are the hormonal ones — Social-UGC §5). |
| 8 | Why This Comparison Isn't Symmetric + Health-Documentation ROI + author box (H2/H3) | A | 230 | — |
| 9 | Deep Dive: African Grey — temperament (H3) · talking/clarity/context, Pepperberg/Alex (H3) (H2) | A | 320 | — |
| 10 | Deep Dive: Amazon Parrot — "spicy"/extroverted (H3) · singing/prosody (H3) (H2) | A | 300 | — |
| 11 | "Greys Talk Better, Amazons Sing Better" (H2) — AIO Noise-vs-Talking | **B** | 220 | Biggest sub-intent: theposhperch's "best talker" page, YouTube #1 (966k) + #2 (335k), the IG reel arguing Amazon prosody wins (Keyword §Tier-2, Social-UGC §6/§7). Competitors cover talking, so we must — but our *attributed honest split* (Avian Avenue + Quora) beats their flat "Greys win." |
| 12 | Noise & Apartment Living (H2) | **B** | 200 | Two Reddit "Amazon Parrot Noise Level (Apartment or Not)" threads + exoticpethub's noise section (Keyword §Tier-2, SERP §4.8). Apartment is a top lifestyle intent. Our edge: **no invented decibels** (competitor error), honest "Amazons louder & all-day; Greys least screamy but not quiet." Link Lafeber. |
| 13 | **Dust & Dander for Allergy Households** — Bird Fancier's Lung (H2) — AIO Dust displacement | **C** | 290 | #1 lived complaint across 6 sources *and* the AIO's chosen citation, currently a Facebook comment (Social-UGC §8.1, SERP §1). No competitor writes it for an allergy sufferer with the BFL entity + air-purifier reality. Centerpiece of §C. |
| 14 | Reading a Bite: Telegraphing vs Unsignalled (H2) | **C** | 280 | Every owner describes it — eye-pinning, bite-and-twist, fear vs excitement vs hormones — and *no article states it as behaviour* (SERP §7, Entity-Map §3). Uniquely ours; safety-relevant for families. |
| 15 | The Hormonal-Maturity Timeline (H2) | **C** | 200 | "The thing that actually ends Amazon ownerships" (TalkParrots + Reddit) — forums only, never an article (SERP §7, Keyword §Tier-5). melissasparrots' "harder at 6 months than 6 years, reversed for Greys" is a unique attributed insight (Social-UGC §4). |
| 16 | Health Risk Analysis, species-appropriate, ledger-bounded (H2) | **B** | 280 | PetHelpful covers health (fatty liver, heart); we match + correct + add PBFD/APV/hypocalcemia/Vit-A/BFL with real sources (Entity-Map §4). External authority links cluster here. ⚠CITE the heart/seizure + BFL claims. |
| 17 | Cost of Ownership, Year One (H2, H4 breakdown) | **C** | 280 | **Not one page prices year one**; Reddit volunteers a "$26,000 cockatiel" vet story into the void; the `…price` related search is unserved (SERP §6.5/§7, Keyword §Tier-0). Link+summarise `/african-grey-parrot-price/` (cannibalisation guard). Congo $1,700–$3,500 / Timneh $1,500–$1,600 ours; Amazon prices = cited market data only. |
| 18 | Decision Scorecard Matrix, 0–10 traits (H2) | **B** | 170 | talkingparrotsisland ships a 7-row "Final Verdict" winner table (SERP §4.8). We match the format buyers expect — but ours is **non-conflicted** (we don't sell Amazons; theirs is structurally biased), and we say so. Stacks into cards on mobile (skill §12.4). |
| 19 | Which Fits You? Lifestyle-Match selector (H2, interactive) | **B** | 220 | Dominant intent is "which fits me/us" (Reddit OP: "fit me & my boyfriend"); talkingparrotsisland has "Lifestyle Fit" (SERP §3/§4.8). Also where we *make the buyer ready* (§D). |
| 20 | **Should You Buy Either Bird At All?** honest objection (H2) | **C** | 300 | The forums say it; every article is too commercial to (SERP §6.2, §7). The single biggest trust-earner in a SERP starving for it. "Buy neither if…" + cockatiel/budgie redirect + "no guarantee it talks." Core of §D. |
| 21 | Wild-Caught? The CITES / Captive-Bred Answer (H2) | **C** | 240 | **Zero of 12 pages** mention Appendix I; one asserts the opposite (PetHelpful's "if not wild-caught," the most damaging line in the SERP — SERP §6.4, Entity-Map §8). We rebut it; nobody else does. |
| 22 | Myth vs Reality Cards (H2, H5/H6) | **C** | 220 | The accuracy-moat vehicle (§E): corrects weight/anatomy/first-timer/"vaccinated" myths impersonally. No competitor audits the myths this niche repeats (Evidence-Log §G). |
| 23 | What Documentation to Demand + scam-literacy (H2) | **B** | 180 | Provenance is the product (PRODUCT.md); also corrects the "vaccinated parrot" claim. Match/exceed any breeder-trust content. Link `/dna-tested-african-grey-for-sale/`, `/african-grey-parrot-health-guarantee/`, `/how-to-avoid-african-grey-parrot-scams/`. |
| 24 | Health, Shipping & Available Greys (H2) | A | 210 | — (canonical `Ships nationwide · $185 airport · $350 home`; live birds only — Bery/Amie/Roys/Jins&Jeni/Elad/Evie; Joys/Loti/Carl sold, never carded) |
| 25 | An Owner's Story + Real Reviews (H2, BAB) | A | 200 | — (real homepage `bottomReviews[]` only; never fabricate — skill §11.7) |
| 26 | FAQ ×10–12, PAA-verbatim, QAB (H2, FAQPage schema) | A | 340 | — |
| 27 | Further Reading + Related Comparisons (H2) | A | 80 | — |
| 28 | Final CTA + page-specific inquiry form (H2) | A | 110 | — (single closer, `hideGlobalCta`, no newsletter band — skill §11.6) |

**Totals:** ≈ 5,950 words · **A = 14 · B = 6 · C = 8.** Eight moat sections (~a third of the page is content no competitor has) is the right ratio given how wide-open the research shows the gap to be. FAQ must draw from the PAA-verbatim set (Keyword §Tier-0): "What is the difference between an African grey and an Amazon parrot?", "What are the cons of the Amazon parrot?", "What are the disadvantages of the African grey parrot?", "What is the friendliest parrot to own?", "Which parrot has the highest IQ?", "How much does an African grey parrot cost?", "How long will an Amazon parrot live?", plus reversed head-term + American "African Gray" spelling woven once each in the Quick-Answer close (skill §12.7).

**Internal links (all verified on disk 2026-07-10 — Internal-Linking.md, re-confirmed this session):** up → `/african-grey-comparison/`; sideways → `/african-grey-vs-cockatoo/` (dust §13), `/african-grey-vs-macaw/` (bite §14), `/congo-vs-timneh-african-grey/`, `/male-vs-female-african-grey-parrots-for-sale/`, `/african-grey-pros-and-cons/`; down → the money/authority set in §17/§20–24. **Location pills — the 7 metro slugs nobody else claimed:** Houston, Austin, San Diego, Bay Area, Orlando, Tampa, Columbus (fresh anchors, distinct from all four siblings; run `dup_content_audit.py` after build). Blog cards: talking-ability, is-good-for-beginners, price-what-you-get. 6–8 external authorities mid-sentence (World Parrot Trust, IUCN, cites.org, Lafeber, VCA, AAV, Alex Foundation, a BFL medical source).

---

## G. Primary framework per major section

| Section(s) | Framework | Reasoning |
|---|---|---|
| Hero (§1), Final CTA (§28) | **AIDA** | Attention → Action, but calm not hype (brand tone: anxiety→reassurance→confidence). |
| Quick Answer, corrected table, genus asymmetry, species deep-dive definitions (§4, §6, §7, §9–10 intros) | **Entity-Tree** | Entity-first declarative prose is what the AIO/AEO extracts and what makes the record *correct* — the whole thesis of Strategy B. |
| Talking-vs-singing, Noise, Dust, Bite, Hormonal timeline (§11–15) | **EBP (Evidence → Benefit → Proof)** | Lead with the owner/vet *evidence* (attributed quotes), state the practical *consequence* for the buyer, *prove* with named attribution + external authority. Credibility-first is how we out-trust content farms without going narrative-soft. |
| Health Risk + Documentation-to-demand (§16, §23) | **EEAT** | Species-appropriate risk + provenance = the credibility/author/citation/schema pillar; where the external-authority links and the Verified-Claim Ledger discipline live. |
| Wild-Caught / CITES rebuttal (§21) | **PDB (Problem → Diagnosis → Bridge)** | Problem: "is it wild-caught?" → Diagnosis: Appendix-I captive-bred reality → Bridge: our CITES + hatch + band documentation. The diagnostic register that meets a planted fear head-on. |
| Should You Buy Either At All? (§20) | **PDB** | Diagnoses the reader's *fit* honestly, then bridges the qualified buyer to the documented path — the §D conversion mechanic. |
| Cost of Ownership (§17) | **EBP** | Real-cost evidence (the $26k vet story is demand proof) → proof via our transparent, sourced pricing. |
| Scorecard, Lifestyle-Match, Key Takeaways, Who-should-choose, FAQ (§5, §18–19, §26) | **QAB (Question → Answer → Benefit)** | Buyer-decision register; QAB is the site standard for FAQ + pricing/decision content and feeds featured-snippet capture. |
| Owner Story + Reviews (§25) | **BAB (Before → After → Bridge)** | Transformation narrative with *real* outcomes; also quietly answers the plucked-bird fear with a documented happy outcome. |
| Myth vs Reality cards (§22) | **PDB** | Each card: the myth (problem) → the sourced correction (diagnosis) → what to actually check/who to trust (bridge). |

Voice across **all** sections: first-person plural C.A.Gs ("we / our / here at C.A.Gs"), Strategy A's honesty register, anti-AI filter, Style-2 humour ≤1 beat/section and never on health/legal/CITES. Encyclopedic exception only for taxonomy/binomials and cited research (First-Person Voice rule).

---

## Constraints compliance (self-check)

- **First-person plural C.A.Gs voice** — mandated as B's finishing layer (§G) and the recommendation.
- **CITES Appendix I captive-bred framing** — §F-21 + §E; uplisted CoP17 effective Jan 2017; captive-bred Appendix-I birds legal to own/transfer domestically with paperwork.
- **Verified-Claim Ledger bounds** — health claims limited to PBFD/APV PCR, DNA sexing, avian-vet exam, hatch cert, closed band, weaned, psittacosis, UV-B/D3 (Entity-Map §5). ⚠CITE items (BFL, decibels, heart/seizure, uropygial gland, Amazon prices) sourced-or-dropped (§E, Evidence-Log §F). One item outside the ledger flagged below.
- **Never assert an Amazon price as ours** — §F-17: Amazon prices are cited external market data only; our inventory is Grey-only.
- **Never print the uncited "80% rehomed" figure** — §D.3: reframed qualitatively, number never printed.
- **No visible dates** — freshness in schema (`dateModified`) only.
- **No page code written** — this is strategy only.

---

## Open Flag — one narrow question for the breeder (Clarification Checkpoint)

**Question:** Does C.A.Gs have a stated **rehoming-support / take-the-bird-back posture** — i.e., "if you ever can't keep your Grey, come to us first"?

**Recommended answer: YES, state it — *if and only if it is true* (Recommended).** WHY: it is the single strongest answer to this SERP's #1 objection. TalkParrots, Reddit and Quora all weaponise rehoming ("adopt don't buy," the uncited 80% figure, sanctuary photos — Social-UGC §1/§3/§5); a documented breeder who says "we'll always take one of our birds back" neutralises the entire anti-purchase argument in one sentence, and **no competitor can match it**. It slots into §F-20 and §F-25 and turns candor into conversion. **Trade-off / why it must wait:** it is a real operational commitment and it is **not currently in the Verified-Claim Ledger** — so it must NOT be asserted until Mark & Teri confirm the exact policy wording. Until confirmed, §F-20/§25 frame rehoming qualitatively (succession planning + refundable deposit + honest lifetime-commitment), with no number and no buyback claim. This is the *only* unit blocked; the whole strategy stands without it.

---

## Handoff

- **Chosen strategy (B, in A's voice) → `cag-content-architect`** — selects/confirms the per-section frameworks above and routes builders (`cag-comparison-builder` executes the skill §4/§11/§12 blueprint; `cag-section-builder`, `cag-faq-agent`, `cag-interactive-component` for the selector/scorecard, `cag-infographic-builder` per §9 imagery pass).
- **Heading Outline Gate first** — present the full H1→H6 outline (§F architecture) for approval before any code; ≥5 H5 AND ≥5 H6, no skips, unique hybrid headers.
- **Each per-page topic row → `grill-me` (Sprint 0.5)** when that section is built.
- **Before write:** Confidence Gate ≥97% on every `site/`/`src/pages/` change; resolve the Open Flag or keep §20/§25 in the qualitative framing.
- **After build:** `npx astro build` → `python3 scripts/final_page_audit.py --comparison` → `dup_content_audit.py` vs the 4 siblings → full pass-gate list (skill §10) → commit + push to `main`.

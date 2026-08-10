# Competitor Sweep — Page 4 (Tier 3 Informational Sites)

Date: 2026-08-09 (sweep batch) · **all fetches executed 2026-08-10 UTC**, verified from server `Date` headers
Analyst: cag-competitor-intel
Scope: **Research only.** No site files touched. `data/competitors.json` NOT modified — every registry
change below is a proposal for breeder approval.
Protocol: `docs/artifacts/cags-universal-page-build-brief.html` §6 (Competitor Research and Query Fan-Out)
Sibling pass: `docs/research/competitor-sweep-page5-2026-08-09.md` (Tier 4 marketplaces)

Registry ids in scope (8): `thesprucePets` · `wikipedia` · `rationalParrot` · `allAboutParrots` ·
`smallAnimalAdvice` · `vetExplainsPets` · `birdAddicts` · `parrotWebsite`

> **Not a page outline.** This is a Sprint-0 research artifact, so the Heading-Hierarchy Outline Gate
> and Header Style Declaration do not apply — no page is being built from these headings.

---

## Method and Barriers (read this before trusting any number below)

Every figure here came from a live fetch on 2026-08-10. Where a source could not be retrieved it is
written `NOT FETCHED` with the barrier named — never inferred.

| Channel | Tool | Status |
|---|---|---|
| DNS resolution | `dig` against system resolver **and** `@1.1.1.1` **and** `@8.8.8.8` | **OK** — three-way cross-check run on all 8 domains |
| Page fetch | `curl --resolve <host>:443:<public-resolver-IP>` + browser UA | **OK for 7 of 8** |
| Page fetch — thesprucepets.com | `curl` | **BLOCKED 403** on every attempt, via system DNS *and* both public resolvers — bot challenge, not a dead site |
| Page fetch — thesprucepets.com | Firecrawl `scrape` | **REFUSED** — Firecrawl returns *"we do not support this site"* (publisher-level exclusion, Dotdash Meredith) |
| Page fetch — thesprucepets.com | Playwright `browser_navigate` + `browser_evaluate` | **OK** — this is the only transport that retrieved the site |
| Sitemap enumeration + lastmod histogram | `curl` sitemap-index walk | **OK for 6 of 8** (Wikipedia and The Spruce Pets have no usable public post-sitemap; see Open Flags) |
| Structural probe (words / H1–H6 / img+alt / iframe / table / `ld+json` / byline) | local `pageprobe.py` over `curl` | **OK for 7 of 8**; Spruce Pets probed via Playwright `evaluate` instead |
| Google organic top 10 | Firecrawl `search` (Google-backed index) | **OK** — but Firecrawl's own egress country is unknown to me; see caveat |
| Google organic + **AI Overview** + PAA + Related, live render | Playwright → google.com/search `hl=en&gl=us` | **OK — 4 queries captured, no CAPTCHA hit** |
| Second-engine SERP | DuckDuckGo HTML (**Bing-syndicated index**) via Playwright | **OK — 2 queries** |
| Bing organic top 10 | — | **NOT FETCHED** — not re-attempted; page 5 proved four-transport query-truncation |
| Autosuggest fan-out (Google + Bing A–Z + question modifiers) | `suggestqueries.google.com` + `api.bing.com/osjson.aspx` | **OK — 3 stems** |
| Reddit brand mining | Reddit JSON API | **BLOCKED 403** from this IP — bot challenge |
| Reddit brand mining | Firecrawl `search` with `site:reddit.com` | **OK** — used as the substitute channel |
| CAG-side schema baseline | local scan of `dist/` (105 built pages) | **OK** |

### Barrier note 1 — the system resolver sinkholes parrot domains, so every domain was re-resolved

This machine's system resolver selectively returns `81.99.162.48` for some parrot domains. A `000`
from the system resolver is therefore **not** evidence of a dead site. Every domain in this scope was
re-resolved against `1.1.1.1` and `8.8.8.8` and re-fetched with `curl --resolve`:

| Host | system A | `@1.1.1.1` A | `@8.8.8.8` A | HTTP via 1.1.1.1 | Sinkholed? |
|---|---|---|---|---|---|
| `www.thesprucepets.com` | 172.66.1.220 | 162.159.141.224 | 172.66.1.220 | **403** | No |
| `thesprucepets.com` | 172.66.1.220 | 162.159.141.224 | 172.66.1.220 | **403** | No |
| `en.wikipedia.org` | 185.15.59.224 | 185.15.59.224 | 185.15.59.224 | 301 → `/wiki/Main_Page` | No |
| `www.rationalparrot.com` | 104.21.55.233 | 172.67.174.41 | 104.21.55.233 | 301 | No |
| `rationalparrot.com` | 104.21.55.233 | 104.21.55.233 | 104.21.55.233 | **200** | No |
| `www.allaboutparrots.com` | 104.21.80.161 | 104.21.80.161 | 104.21.80.161 | **200** | No |
| `allaboutparrots.com` | 172.67.151.119 | 172.67.151.119 | 104.21.80.161 | 301 | No |
| `www.smallanimaladvice.com` | 172.67.140.158 | 104.21.27.14 | 172.67.140.158 | 302 | No |
| `smallanimaladvice.com` | 50.6.2.84 | 50.6.2.84 | 50.6.2.84 | **200** | No |
| `www.vetexplainspets.com` | 104.26.4.116 | 104.26.5.116 | 172.67.69.181 | 301 | No |
| `vetexplainspets.com` | 104.26.5.116 | 104.26.5.116 | 104.26.4.116 | **200** | No |
| **`www.birdaddicts.com`** | **none** | **none** | **none** | **NO A RECORD** | No — genuinely closed |
| `birdaddicts.com` | 172.67.137.180 | 104.21.70.164 | 172.67.137.180 | **200** | No |
| `www.parrotwebsite.com` | 104.16.150.108 | 104.16.150.108 | 104.16.150.108 | **200** | No |
| `parrotwebsite.com` | 104.16.150.108 | 104.16.151.108 | 104.16.151.108 | 301 | No |

**Zero of the eight are sinkholed.** The filter did not bite on this scope, as expected for large
publishers — but it was checked rather than assumed, and the one `none` in the table is a real
finding, not a resolver artifact (see §A7).

### Barrier note 2 — every SERP below is UK-localised, and must be read that way

This machine's egress is `82.18.132.216` — **AS5089 Virgin Media Limited, Birmingham, England, GB**.
The four Google captures were issued with `hl=en&gl=us`, which changes result *language and country
parameters* but **does not change the egress IP**. They are therefore **UK-egress, US-parameterised**
captures, not clean US rankings. The DuckDuckGo captures carry visible UK localisation (a
`parrotessentials.co.uk` paid unit, `pets4homes.co.uk`, `parrothaven.uk`).

Firecrawl `search` results run on Firecrawl's infrastructure, whose egress country I did not measure;
those are labelled **(Firecrawl, egress unknown)** wherever quoted.

**Consequence for the reader:** treat every position number as *directionally* true and the
*composition* of each SERP as the real signal. Absolute US rank is `NOT FETCHED` for every query.

---

# Part A: the eight Tier 3 sites

All eight have a baseline at `docs/research/competitor-<id>-2026-05-11.md`. Consistent with the
page-2 sweep's finding, **the baselines are wrong far more often than they are right in this group** —
6 of 8 carry at least one materially false claim, and 4 carry a claim that would have led CAG to
skip a page it should build or build a page it already has. Corrections are stated explicitly.

---

## A1 · The Spruce Pets — https://www.thesprucepets.com

Tier 3 · informational_content · priority `high` · baseline written under a fetch block

### 1. SERP snapshot

**"african grey parrot care"** — Google (Firecrawl, egress unknown), top 10:

| # | Result | Type |
|---|---|---|
| 1 | treeoflifeexotics.vet — African Grey Parrot Care | **Avian vet clinic** |
| 2 | r/parrots — "What to know when getting an African grey?" | Forum |
| 3 | swiftailvet.com — African Grey Care Sheet | **Avian vet clinic** |
| 4 | facebook.com/groups/64779050616 | Forum |
| **5** | **thesprucepets.com/african-grey-parrots-390502** | **Publisher** |
| 6 | forums.avianavenue.com | Forum |
| 7 | zupreem.com | Brand |
| 8 | parrotessentials.co.uk | UK retailer |
| 9 | quora.com | Forum |
| 10 | howcast.com | Video |

Google live render (Playwright, same query, UK egress + `gl=us`) returned Spruce Pets **twice** in
the organic link set (`/african-grey-parrots-390502` and `/facts-about-african-grey-parrots-390715`)
— but **not once in the AI Overview citation set** (see §B1).

Second engine — DuckDuckGo / **Bing-syndicated**, same query, organic only (2 paid units stripped):

| # | Result |
|---|---|
| 1 | **allaboutparrots.com/african-grey-parrot-care/** |
| 2 | **smallanimaladvice.com/african-grey-parrot-care-guide/** |
| 3 | tiktokparrot.com |
| 4 | africangrayparrots4homes.com |
| 5 | pets4homes.co.uk |
| 6 | johnnysfinches.com |
| **7** | **thesprucepets.com/african-grey-parrots-390502** |
| 8 | paraisodeaves.com · 9 exotic-birds.com · 10 focuspetcare.com |

**The engine split is the finding.** Google ranks the publisher above the small sites; the
Bing-syndicated index inverts it and puts the two sites our baseline called "zero African Grey
content" at **#1 and #2**, with Spruce Pets down at #7.

### 2. Query fan-out — shared stems (measured once, applies across A1–A8)

| Stem | Google A–Z | Bing A–Z | question-mods | union | 6+ words |
|---|---|---|---|---|---|
| `african grey parrot care` | 17 | 37 | 21 | **61** | 23 |
| `african grey parrot` | 259 | 177 | 221 | **549** | 216 |
| `african grey vs` | 186 | 66 | 33 | **274** | 39 |

6+-word conversational targets on the care stem (23 total, sample):
`do you need a licence for an african grey parrot` · `how long can african grey parrots be left alone` ·
`do african grey parrots carry diseases` · `do african grey parrots need a companion` ·
`can you keep african grey parrots outside` · `are african grey parrots hard to take care of` ·
`how to care for african grey parrot for beginners` · `how to take care of baby african grey parrot` ·
`how to transport an african grey parrot` · `what not to feed african grey parrots` ·
`outline african grey parrot ownership costs care and expected lifespan` ← **prompt-shaped, an LLM-era query form**

Bing-only on the care stem (34 terms) — a real second-engine gap. Notable:
`african grey parrot health problems` · `african grey parrot husbandry` · `african grey parrot near me` ·
`african grey parrot rescue near me` · `african grey parrots for rehoming` · `buy african grey parrot online` ·
`african grey parrot treats` · `african grey parrot enclosure`

### 3. Section / listing inventory

`site:thesprucepets.com african grey` (Firecrawl) returned **20 AG-mentioning URLs**, of which only
**two are African-Grey-dedicated**:

| URL | Role |
|---|---|
| `/african-grey-parrots-390502` | Species profile — the flagship |
| `/facts-about-african-grey-parrots-390715` | Facts listicle |

The other 18 are listicles where the African Grey is one entry among many
(`/the-smartest-pet-birds-4178388`, `/top-loudest-parrot-species-390531`,
`/top-talking-bird-species-390534`, `/top-10-trainable-pet-birds-5272204`,
`/how-long-do-parrots-and-other-pet-birds-live-1238433`, `/common-diseases-in-pet-birds-390443`,
`/parrot-fever-psittacosis-symptoms-treatment-4148338`, `/bird-identification-common-red-parrots-390518`,
`/top-friendly-pet-bird-species-390535`, `/large-birds-4162092`, `/bird-breeds-4162096`, and others).

**There is no dedicated Congo vs Timneh comparison page.** A `site:` search on
`congo timneh african grey difference` returned only the species profile, the facts listicle, and
four generic listicles that mention the distinction in a caption line.

Measured page structure:

| | `/african-grey-parrots-390502` | `/facts-about-african-grey-parrots-390715` |
|---|---|---|
| Words (rendered body) | **1,684** | **1,121** |
| H1 / H2 / H3 | 1 / 13 (≈10 content) / 2 | 1 / 8 (5 content) / 1 |
| Images (missing alt) | 17 (0) | 23 |
| iframes | 3 | — |
| Tables | **0** | 0 |
| `ld+json` types | Article · Person · ImageObject · Organization · WebPage · BreadcrumbList · ListItem | + **VideoObject** · ItemList |
| **FAQPage** | **absent** | **absent** |
| Author | **Alyson Kalhagen** — avian expert, 10+ yrs combined as veterinary technician and pet-store chain manager, featured in *Bird Talk Magazine* | same |
| Last updated | **August 11, 2025** | October 24, 2025 |
| CITES mentioned | no | **no** |

Content H2s on the species profile, verbatim and in order: *Origin and History · Temperament ·
Speech and Vocalizations · African Grey Parrot Colors and Markings · Caring for an African Grey
Parrot · Common Health Problems · Diet and Nutrition · Exercise · Where to Adopt or Buy an African
Grey Parrot · More Pet Bird Species and Further Research.*

### 4. Visual inventory

17 images on the species profile, **0 missing alt** — but alt text is generic-editorial, not
keyword-formed (`"Wonderful AfricanGreys"`, `"Eclectus Pair"`, `"Hyacinth Macaw"`). One `figcaption`
total (*"They Are Delightful!. Credit: Tandi Reed / EyeEm / Getty Images"*). **Zero tables, zero
comparison charts, zero infographics** on either AG page. The facts page carries `VideoObject`
schema; the species profile does not.

### 5. The commercial section — this is the part that matters to CAG

`Where to Adopt or Buy an African Grey Parrot`, verbatim:

> *"Contact a local breeder and see if you can meet with them and their pets to see first-hand how
> these birds interact in a home environment. **Breeders sell African greys in the range of $2,000 to
> $4,000.** Signs you should avoid the breeder include cramped living conditions, inactive birds, and
> breeders who avoid your questions or do not seem to have much information on their birds."*

It then links out to exactly **three** destinations, and they are the whole list:

1. `beautyofbirds.com/africangreybreeders.html` — **"List of Breeders"**
2. `lonelygreyrescue.org`
3. `birdbreeders.com/birds/category/african-grey-parrots`

plus an internal link to `/signs-of-a-bad-breeder-1117328`.

**C.A.Gs is on none of them.** This is the single most concrete, lowest-cost action in this sweep: a
listing request to the Beauty of Birds African Grey breeder list puts C.A.Gs one click from the
highest-authority African Grey care page on the open web.

### 6. Reddit / forum mining — The Spruce Pets by name

| Thread | Verbatim | Read |
|---|---|---|
| r/parrots "Is this parrot sick?" | *"They are prey animals and good at hiding sickness. An African Grey parrot using deduction 's not thesprucepets"* | Used dismissively — redditors do not treat it as the authority |
| r/todayilearned | *"TIL that parrots live for ages: the African Gray 40–60y… thesprucepets.com"* | Cited as a **lifespan** source specifically |

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-10 |
|---|---|
| "~2,000–4,000 words per article" | **1,684** on the species profile, **1,121** on the facts page. Both well below the estimate. |
| "8–12 H2 sections per article" | 13 H2 raw, **≈10 content** on the profile; **5 content H2s** on the facts page. |
| **"FAQPage schema on care guides (strong AIO signal)"** | **False. No FAQPage on either AG page.** The article schema is Article + Person + Organization + BreadcrumbList. |
| "Comparison pages — likely (Congo vs Timneh)" | **False. No dedicated Congo vs Timneh page exists.** The distinction lives in two sentences inside other articles. |
| "Infographics: Yes — care checklists, diet charts common" | **Not present** on either AG page: 0 tables, 0 charts, 1 figcaption. |
| "CITES permit: Referenced in conservation articles" | **Neither AG page mentions CITES at all.** |
| "CAG has ZERO informational blog pages competing for these keywords" | **Stale by three months.** CAG now ships `/african-grey-care/`, `/african-grey-parrot-care-guide/`, `/african-grey-parrot-diet/`, `/african-grey-parrot-lifespan/`, `/african-grey-parrot-price/`, `/african-grey-parrot-faq/`, `/african-grey-pros-and-cons/` and a 9-post `/blog/`. |
| Access "Blocked" | Precise: `curl` 403 (bot challenge) **and** Firecrawl publisher-level refusal; **Playwright retrieves it fine**. Not blocked, blocked *by transport*. |

### Key insight

The Spruce Pets is a **thinner** competitor than the baseline believed — 1,684 words, no tables, no
FAQPage, no Congo-vs-Timneh page, no CITES — and it has **not been cited in a single one of the four
AI Overviews captured for this sweep**. Its real leverage over CAG is not content depth; it is the
three outbound links in `Where to Adopt or Buy`, and the fact that it anchors buyer price
expectation at **$2,000–$4,000** — above CAG's $1,500 floor, which is a *help* to us, not a threat.

---

## A2 · Wikipedia — https://en.wikipedia.org

Tier 3 · informational_content · priority `high`

### 1. SERP snapshot

Google (Firecrawl, egress unknown): **#4** for `african grey parrot lifespan` via `/wiki/Grey_parrot`;
**#9** for `african grey vs cockatoo` via the same URL. Not present in the top 10 for
`african grey parrot care`, `african grey parrot price`, `congo vs timneh african grey`, or
`how much does an african grey parrot cost`.

AI Overview citations across all four captured queries: **zero**.

### 2. URL structure — the baseline had the redirect backwards

| URL | Canonical | Status |
|---|---|---|
| `/wiki/African_grey_parrot` | → **`/wiki/Grey_parrot`** | redirect to the **species** article |
| `/wiki/African_Grey_Parrot` | → `/wiki/Grey_parrot` | same |
| **`/wiki/Timneh_parrot`** | **self-canonical** | **separate standalone article** — the baseline missed it entirely |
| `/wiki/Psittacus` | self-canonical | genus article, separate |

### 3. Section inventory

**`/wiki/Grey_parrot` — 4,805 words · H1 1 · H2 11 · H3 6 · 19 images (5 missing alt, 2 empty alt) ·
4 tables · 0 iframes · `ld+json` = Article, Organization, ImageObject · no FAQPage**

H2s in order: *Taxonomy · Description · Distribution and habitat · Behaviour and ecology in the wild ·
Conservation · In captivity · History · See also · References · External links.*

**`/wiki/Timneh_parrot` — 1,656 words · H1 1 · H2 7 · 12 images (3 missing alt, 2 empty) · 3 tables ·
same schema set.** H2s: *Taxonomy · Description · Distribution and habitat · Status, threats and
conservation · References · External links.*

### 4. Visual inventory

19 images on the species article including range maps and subspecies photography; **5 carry no `alt`
attribute at all and 2 are empty** — the weakest alt layer of any site measured in this sweep,
including the content farms. 4 wikitables. No video, no iframes, no interactive elements.

### 5. CITES — the baseline contains the exact error CLAUDE.md says to correct on sight

The 2026-05-11 baseline states: *"CITES permit: **CITES Appendix II** status documented with full
conservation context."*

Wikipedia says the opposite, in three independent places on the page:

> Infobox: *"Conservation status **Endangered** (IUCN 3.1) · **CITES Appendix I**"*
>
> Body: *"In October 2016, the Convention on the International Trade of Endangered Fauna and Flora
> (CITES) extended the highest level of protection to grey parrots by **listing the species under
> Appendix 1**, which regulates international trade in the species."*
>
> Page category: *"**Fauna listed on CITES Appendix I**"*

This matches CLAUDE.md rule 2 exactly (Appendix I, uplisted CoP17 October 2016, IUCN Endangered for
the Congo). **The error is ours, not Wikipedia's, and it is sitting inside our own research corpus
where a future agent can pick it up and propagate it onto a live page.**

### 6. Reddit / forum mining

No Wikipedia-specific African Grey thread surfaced in the `site:reddit.com` sweep. Wikipedia's role
in the forums is as a background citation, not a discussed source. **NOT FETCHED** as a distinct
signal — barrier: no branded threads exist in the indexed set to mine.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-10 |
|---|---|
| **"CITES Appendix II status documented"** | **False and Rule-2 violating.** The article states **Appendix I** in the infobox, the body, and the page category. |
| "Page currently redirects to Psittacus genus article" | **False.** `/wiki/African_grey_parrot` canonicals to `/wiki/Grey_parrot`, the **species** article. |
| "One main article; links to subspecies" | **`/wiki/Timneh_parrot` is a full standalone article** (1,656 words, 7 H2, 3 tables), not a subsection. |
| "~3,000–5,000 words (estimated)" | **4,805 measured** — the one baseline estimate in this sweep that held. |
| "Alt text: Descriptive (Wikipedia standard)" | **5 of 19 images carry no alt attribute; 2 more are empty.** |

### Key insight

Wikipedia is not a commercial competitor — it is the **canonical source that agrees with us**. It
states CITES Appendix I and IUCN Endangered in schema-visible infobox markup, which is exactly what
LLMs read. CAG's `/cites-african-grey-documentation/` should cite the Wikipedia infobox and the
October 2016 CoP17 uplisting by name, because agreeing with the encyclopedia on a fact the rest of
this Tier-3 set gets wrong is a cheap, durable authority signal.

---

## A3 · Rational Parrot — https://rationalparrot.com

Tier 3 · informational_content · priority `medium`

### 🚩 FINDING — this is no longer a small blog. It is a 19,747-page programmatic content farm.

Sitemap-index walk (20 `post-sitemap*.xml` files):

| Metric | Measured |
|---|---|
| Total URLs | **19,747** |
| `lastmod` 2025 | 546 |
| `lastmod` 2026 | **19,201** |
| Oldest `lastmod` | 2025-04-19 |
| Newest `lastmod` | 2026-06-16 |

The About page states, in the owner's own words: *"I created Rational Parrot in **2025**."* That is
**19,747 URLs in roughly fifteen months — about 44 pages per day, every day.**

### 1. SERP snapshot

Did **not** appear in the top 10 of any Google or DuckDuckGo query captured in this sweep, and is
cited in **none** of the four AI Overviews. Enormous index, no measured visibility on CAG's terms.

### 2. African Grey inventory — 13 slugs, and 11 of them are transactional

| Slug | Intent | Collides with |
|---|---|---|
| `/where-to-buy-african-grey-parrot/` | **Transactional** | CAG `/where-to-buy-african-greys-near-me/` |
| `/where-to-buy-african-gray-parrot/` | Transactional | same |
| `/where-can-i-buy-a-african-grey-parrot/` | Transactional | same |
| `/where-can-i-buy-an-african-gray-parrot/` | Transactional | same |
| `/where-can-you-buy-an-african-grey-parrot/` | Transactional | same |
| `/where-to-get-an-african-grey-parrot/` | Transactional | same |
| `/how-much-does-a-african-grey-parrot-cost/` | Commercial | CAG `/african-grey-parrot-price/` |
| `/how-much-does-a-african-gray-parrot-cost/` | Commercial | same |
| `/how-much-is-an-african-gray-parrot/` | Commercial | same |
| `/how-much-do-grey-parrots-cost/` | Commercial | same |
| `/how-much-does-a-grey-parrot-cost/` | Commercial | same |
| `/what-can-african-grey-parrots-not-eat/` | Informational | CAG `/african-grey-parrot-diet/` |
| `/african-grey-bird-toys/` | Affiliate | — |

**Six near-duplicate "where to buy" URLs and five near-duplicate "how much does it cost" URLs.** This
is keyword-permutation publishing, and it is aimed squarely at CAG's transactional funnel from a
site the registry classifies as Tier 3 informational.

### 3. Section inventory — `/where-to-buy-african-grey-parrot/`

**2,234 words · H1 1 · H2 14 · H4 1 · H5 1 · 4 images · 2 tables · 0 iframes.**
Schema: Article · WebPage · BreadcrumbList · WebSite · SearchAction · Organization · Person ·
ReadAction · ImageObject · ListItem. Published 2025-04-22. Author meta: **Malik Miller**.
Canonical present. Meta description present and well-formed.

H2s verbatim: *Local Pet Stores · Avian Specialty Stores · Reputable Breeders · Online Resources and
Classifieds · Adoption and Rescue Organizations · **Reputable Breeders** (repeated) · Online
Retailers · **Local Pet Stores** (repeated) · Rescue Organizations · Considerations Before Purchase ·
Expert Insights on Where to Buy African Grey Parrots · Frequently Asked Questions (FAQs) · Post
navigation · You Can Also Read.*

Note the duplicated H2s (`Reputable Breeders` and `Local Pet Stores` each appear twice) — a
generation-pipeline tell. And note that despite shipping an *"Frequently Asked Questions (FAQs)"*
H2, the page carries **Article schema, not FAQPage**.

### 4. Authority signals

About page, verbatim: *"Hi, I'm **Malik Miller**. I created Rational Parrot in **2025**… Over the
years, I've studied hundreds of hours of behavioral science, volunteered with rescue shelters,
consulted with avian specialists, and, most importantly, shared my home with a flock."*

**No veterinary credential. No named avian specialist. No physical address. No phone. No
organisation.** The baseline's "20+ years hands-on experience with companion birds; maintains 6
parrots" does not appear anywhere on the current About page.

### 5. Reddit / forum mining — and the expired-authority finding

Firecrawl `site:reddit.com` returned **four** r/parrots threads across 2013–2020 all pointing at one
URL: **`rationalparrot.com/diet.html`**.

| Thread | Verbatim |
|---|---|
| r/parrots "What kind of parrot food?" | *"…rationalparrot.com/diet.html. In my opinion, Tropican makes a decent pellet but there are certainly better ones out there."* |
| r/parrots "Jack wanted to say hi to /r/parrots" | *"For more diet info, see: http://rationalparrot.com/diet.html. A good diet is essential to avoid major health problems, and improves behavior."* |
| r/parrots "QUAKER PARROT HELP" | *"Google a list of parrot safe fresh fruit and veg that you can turn into a daily chop (http://rationalparrot.com/diet.html)…"* |
| r/Pets "i just got a ringneck parrot…" | *"…parrot's diet: http://rationalparrot.com/diet.html. The pellet brands I like are Harrison's and Roudybush."* |

Measured today: **`rationalparrot.com/diet.html` returns 200 but resolves to the site homepage.** The
resource r/parrots trusted for over a decade no longer exists. The domain's community link equity is
now being harvested by a 19,747-page farm published under a 2025 founding date.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-10 |
|---|---|
| **"NO African Grey content at all — a complete African Grey gap"** | **False. 13 African-Grey slugs, 11 of them transactional or commercial.** |
| **"Any African Grey informational content CAG publishes has zero direct competition from this site"** | **False and dangerous.** They ship six "where to buy an African Grey" pages. |
| "Total pages: Moderate blog — dozens of articles" | **19,747 URLs.** Off by three orders of magnitude. |
| "Schema: Not detected on homepage" | Article · WebPage · Organization · Person · BreadcrumbList · SearchAction on the AG pages. |
| "Conversion: None — pure educational model with no commercial offers" | The AG page set is built entirely around purchase intent. |
| "Author: Malik Miller — 20+ years hands-on experience; maintains 6 parrots" | Current About page says the site was **created in 2025**; no "20+ years" or "6 parrots" claim is present. |

### Key insight

Rational Parrot is the clearest case in this sweep of a **registry mis-tier**: it is filed as Tier 3
informational and is in practice a transactional-intent publisher aimed at CAG's own head terms, at
44 pages/day, sitting on a decade of r/parrots link equity whose original asset is gone. It ranks
nowhere on the queries we care about *today* — which is exactly when to note it, not after it does.

---

## A4 · All About Parrots — https://www.allaboutparrots.com

Tier 3 · informational_content · priority `medium`

### 1. SERP snapshot

**Second engine (DuckDuckGo / Bing-syndicated), `african grey parrot care`: organic #1**, via
`/african-grey-parrot-care/`. That is the top organic result on the second engine for CAG's core
informational head term.

Google (Firecrawl, egress unknown): not in the top 10 for `african grey parrot care`,
`african grey parrot price`, or `congo vs timneh african grey`.
AI Overview citations across four queries: **zero**.

### 2. Section / listing inventory

Sitemap walk: **365 URLs** total. `lastmod` 2020=2, 2022=1, 2023=1, **2024=352**, 2025=8; newest
2025-12-27. **Nine African-Grey-dedicated slugs:**

`/african-grey-parrot-care/` · `/how-much-do-african-grey-parrots-cost/` ·
`/how-to-read-african-grey-body-language/` · `/are-african-grey-parrots-known-for-biting/` ·
`/can-congo-and-timneh-african-greys-breed/` · `/why-do-african-grey-parrots-shiver/` ·
`/why-do-african-grey-parrots-have-red-tails/` · `/african-gray-plucking-or-molting/` ·
`/games-to-play-with-african-grey-parrots/`

Plus a long tail of AG-mentioning pages (`/different-types-of-talking-birds/`,
`/what-causes-seizures-in-parrots/`, `/strokes-in-parrots/`, `/aggression-in-parrots/`,
`/how-to-tell-male-and-female-parrots-apart/`, `/talking-parrot-cost/`, `/at-what-age-do-parrots-start-laying-eggs/`,
`/families-of-psittaciformes/`, and ~30 more).

**`/how-much-do-african-grey-parrots-cost/` — the head-to-head with CAG's price page:**
1,470 words · H1 1 · H2 8 · H3 2 · H4 3 · 9 images · **1 table** · Article schema (no FAQPage) ·
author **Carrie Stephens** · published 2023-07-04, modified 2024-02-20.

H2/H3/H4 verbatim: *African Grey Pricing Factors · Average Cost of African Greys · Why African Grey
Parrots Cost So Much · **Proof of Legal Ownership (Cites)** · Relative Scarcity · High Demand · Cage
Costs · Food Price · **How Much African Grey Eggs Cost** · Annual Cost of Owning An African Grey
Parrot · What To Look For When Buying An African Grey Parrot.*

**`/are-parrots-legal-in-america/` — 3,394 words · H1 1 · H2 10 · H3 17 · Article schema.** Titled
*"Are Parrots Legal In America? A State-by-State Guide!"*

### 3. Two factual errors on their price page that CAG can correct by name

**(a) The price table inverts the market.** Verbatim from their table:

| African Grey Parrot Species | Average Price (USD) |
|---|---|
| Congo African grey | $2,000 – $2,750 |
| Timneh African grey | **$3,500 – $5,000** |

They assert Timnehs cost **more** than Congos, on the reasoning *"Sub-species. Timnehs are rarer than
Congos."* CAG's own live inventory says otherwise — Timneh Elad at **$1,600** and Timneh Evie at
**$1,500** against a Congo range of **$1,500–$3,500** with the bonded pair setting the ceiling. The
$3,500–$5,000 Timneh figure is not supported by any listing measured in this sweep or in page 5.

**(b) They apply UK/EU law to a US audience.** Verbatim:

> *"To sell, buy, display, or use an African grey parrot commercially, you need two types of **CITES
> Article 10 (A10) certificates**, which are: The **Transaction Specific Certificate (TSC)**. A
> **Specimen Specific Certificate (SS)**. They must also be marked with a closed-leg ring or a
> microchip because African greys were added to the **CITES Appendix 1** list."*

Article 10 certificates, TSCs and SSCs are **UK/EU instruments**. They do not exist in United States
law. A US buyer reading the top-ranked "how much do African Greys cost" answer is being told they
need paperwork that no US breeder can issue. (Their Appendix 1 statement is correct — credit where
due, and it is one more Tier-3 site that agrees with us and against our own stale baseline.)

**(c) The state-by-state legality page does not answer the African Grey question.**
`/are-parrots-legal-in-america/` runs 3,394 words across 27 headings and is **almost entirely about
Quaker parrots** — Quaker bans, Quaker permits, Quaker banding, state by state. It correctly cites
the Wild Bird Conservation Act. It contains **no African-Grey-specific state legality answer.**

### 4. Visual inventory

9 images on the price page (1 empty alt), 1 comparison table. No infographics, no video, no iframes
on any AG page sampled. Author photo + bio block present on every article (`Carrie Stephens`, with
the recurring bio *"I've got a 15-year-old blue and gold macaw, a 7-year-old African grey, and a
6-year-old Senegal parrot"*) — a real, consistent, first-person E-E-A-T signal.

### 5. Reddit / forum mining — they are the most community-trusted site in this group

Six distinct threads link to allaboutparrots.com as an authority:

| Thread | Verbatim | Read |
|---|---|---|
| **r/AfricanGrey "I have never been upset this much in my life"** | *"The **USDA website** should have information about paperwork and medical documentation as well. https://www.allaboutparrots.com/are-parrots-legal-…"* | **The exact legality/documentation demand CAG should own, routed to them** |
| r/parrots "my aunt left her parrot with us…" | *"…damage to a bird. **Please don't spread misinformation…** https://www.allaboutparrots.com/do-parrots-like-mirrors-in-their-cage/"* | Used as the corrective source in an argument |
| r/parrots "rest easy carmy" | *"https://www.allaboutparrots.com/causes-of-sudden-death-in-parrots/ This is a link to some literature concerning 16 different reasons…"* | Grief thread, cited as literature |
| r/parrots "Update! They ate almost an entire syringe…" | links `/what-cleaning-products-are-safe-around-parrots/` and `/is-air-freshener-safe-for…` | Emergency triage |
| r/cockatiel "Please help. Urgent." | links `/parrot-is-choking/` | Emergency triage |
| r/parrots "Nikkibird hopes you are all having a good day" | links `/can-parrots-eat-fish/#:~:text=…` | Diet arbitration |

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-10 |
|---|---|
| **"only ONE indirect African Grey reference… virtually no dedicated African Grey coverage"** | **False. Nine dedicated African-Grey slugs**, including a 1,470-word price page with its own price table. |
| **"Zero competition for CAG in African Grey informational space"** | **False.** They are **organic #1 on the second engine** for `african grey parrot care`. |
| "Homepage word count ~600; small-to-medium blog" | 365 URLs; the price page alone is 1,470 words, the legality page 3,394. |
| "Schema: Not specified" | Article · WebPage · Organization · Person · BreadcrumbList · SearchAction · ReadAction. No FAQPage. |
| "Author: Carrie Stephens — contributor; no advanced credentials" | Accurate, and stronger than the baseline implies: consistent first-person owner bio on every article, and six r/parrots citations. |
| "could even attract backlinks from their 'talking ability' content" | Reverse the direction — **they** are the cited party in r/AfricanGrey today. |

### Key insight

All About Parrots is the **most underestimated competitor in the entire Tier-3 registry**: organic #1
on the second engine for our core care term, six r/parrots citations, and the page a distressed
r/AfricanGrey owner was pointed to for legality and documentation. And their two highest-stakes
claims are demonstrably wrong — a Timneh price band no US listing supports, and UK Article 10
paperwork presented as US law. CAG can beat them on the exact ground they are weakest: a
**US-specific, African-Grey-specific documentation and legality page**, which nobody in this set has.

---

## A5 · Small Animal Advice — https://smallanimaladvice.com

Tier 3 · informational_content · priority `medium`

### 1. SERP snapshot

**Second engine (DuckDuckGo / Bing-syndicated), `african grey parrot care`: organic #2**, via
`/african-grey-parrot-care-guide/` — directly behind All About Parrots and five places ahead of The
Spruce Pets.

Google (Firecrawl, egress unknown): not in the top 10 of any query captured.
AI Overview citations: **zero**.

### 2. Section / listing inventory — 34 African Grey articles, not 6

Sitemap walk: **1,123 URLs**. `lastmod` 2022=44, 2023=622, 2024=457. **Newest `lastmod`:
2024-03-06** — the site has published nothing for roughly **29 months**.

`/birds/african-grey/` is a dedicated species hub: 927 words, H1 1, **36 H2** (34 article titles plus
`Popular Post` and `Disclaimer`), 42 images, schema = CollectionPage · BreadcrumbList · WebSite ·
Person · ImageObject · ListItem.

The 34 articles, verbatim from the hub and confirmed against the sitemap:

**Care / husbandry (7)** — 15 African Grey Parrot Care Guide Tips · What Do African Greys Eat [20 Safe
Fruits & Veggies] · Interesting African Grey Parrot Training Tips · What Not to Feed African Grey
Parrots [15 Hints] · How Long Can African Grey Parrots be Left Alone · Can African Grey Parrots Live
Together · How Do African Greys Sleep

**Health (7)** — 11 Top African Grey Parrot Health Issues · 11 Top African Grey Parrot Sick Symptoms ·
How to Treat a Sick African Grey Parrot · 9 Top African Grey Liver Disease Symptoms · 11 Common
African Grey Stroke Symptoms · How Do I Know if My African Grey Is Dying · African Grey Diseases to
Humans Explained

**Behaviour / emotional long tail (16)** — 14 Interesting African Grey Parrot Behaviors & Meaning · 15
Top African Grey Body Language · Do African Greys Get Jealous · Are African Greys Cuddly · Are
African Grey Parrots Messy · How Do African Grey Parrots Show Affection · Why Does My African Grey
Puff Up · Are African Greys Friendly · How to Get an African Grey to Like You · How To Keep African
Grey Parrots Happy · 13 Top African Grey Behavior Problems · Why is my African Grey Aggressive · Why
Does My African Grey Bite Me · 10 Top Signs of an Unhappy African Grey · 12 Top Signs Of A Happy
African Grey · How to Tell if African Grey is Male or Female [11 Hints]

**Species / buying (4)** — 12 Interesting African Grey Parrot Facts · Are African Greys Good for
Beginners · African Grey Parrot Life Expectancy · Can African Greys Eat Mango

**`/african-grey-parrot-care-guide/` measured:** 2,887 words · H1 1 · H2 6 · **H3 16** (fifteen
numbered care tips + Leave a Reply) · 15 images (2 empty alt) · **0 tables** · schema = BlogPosting ·
Person · Organization · WebPage · BreadcrumbList · ImageObject. Published 2024-02-23.
**It ships an `FAQs` H2 with no FAQPage schema** — the single most common structural miss in this group.

### 3. Visual inventory

42 images on the hub, 15 on the flagship care guide, all with alt text but two empty. **Zero tables,
zero infographics, zero video, zero iframes** across every AG page sampled. Stock-photo led.

### 4. Reddit / forum mining

No branded mentions found via `site:reddit.com`. **NOT FETCHED** as a sentiment signal — barrier: no
indexed threads name this site.

### 5. Authority signals

About page attributes the site to **"Jack"** with a third-person site description and no bio, no
credential, no address, no phone. The baseline's *"Samuel Steve — founder; obsessed pet and food
lover with years of experience"* does not appear on the current About page.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-10 |
|---|---|
| **"6 African Grey-specific articles"** | **34 articles plus a species hub.** Off by 5.7×. |
| "Author: Samuel Steve — founder" | Current About page says **"Jack"**, third-person, no bio. |
| "Schema: Not confirmed (live fetch blocked)" | **Confirmed:** BlogPosting + CollectionPage + BreadcrumbList + Person. **No FAQPage.** |
| "Homepage word count ~1,200; medium blog" | **1,123 URLs total.** |
| "Total pages: Medium blog with dedicated African Grey section" | Correct in shape, wrong in scale — and **dormant since 2024-03-06**. |

### Key insight

Small Animal Advice owns the **emotional and behavioural long tail** that CAG's care cluster does not
touch — *is my grey jealous / unhappy / dying / biting me / puffing up / showing affection* — 16
articles of it, at organic #2 on the second engine. And it has been **frozen since March 2024**. A
dormant #2 with no FAQPage schema and no tables is the most attackable position in this sweep: CAG
can take those queries with fresher, first-person, breeder-observed answers and the FAQPage markup
they lack.

---

## A6 · Vet Explains Pets — https://vetexplainspets.com

Tier 3 · informational_content · priority `low` · baseline revised 2026-05-15 to **THREAT: LOW**

### 🚩 FINDING — 180,458 URLs, and the 2026-05-15 "no dedicated AG pages" verdict is wrong

Sitemap-index walk (76 sub-sitemaps):

| Metric | Measured |
|---|---|
| Total URLs | **180,458** |
| `lastmod` 2024 | 130,622 |
| `lastmod` 2025 | 49,425 |
| `lastmod` 2026 | 202 |
| Newest `lastmod` | 2026-02-04 |

The 2026-05-15 note reads: *"Firecrawl map search for 'african grey' returned no dedicated AG health
pages — only sidebar mentions in generic bird listicles. Not a vet-authority AG site as previously
estimated. Threat revised from MEDIUM to LOW."* That was a **tool limitation being recorded as a site
fact** — `firecrawl_map` samples, it does not enumerate. The sitemap walk finds the pages.

### 1. African Grey inventory — ~33 genuine AG pages, four of them exact CAG slug collisions

63 URLs match the AG/Congo pattern; ~30 are noise from the site's habit of covering every
"Congo"-token keyword (`/100-foot-snake-in-the-congo/`, `/congo-tetra-male-vs-female/`,
`/philodendron-rojo-congo-vs-imperial-red/`, `/national-animal-of-the-congo/`). The ~33 genuine ones:

**Congo vs Timneh — SEVEN near-duplicate permutations:**
`/congo-vs-timneh-african-grey/` ← **exact CAG slug** · `/african-grey-congo-vs-timneh/` ·
`/african-grey-parrot-congo-vs-timneh/` · `/african-grey-timneh-vs-congo/` ·
`/congo-african-grey-vs-timneh/` · `/timneh-african-grey-vs-congo/` · `/timneh-vs-congo-african-grey/`

**Other exact / near CAG slug collisions:**

| Vet Explains Pets URL | CAG page it collides with |
|---|---|
| `/best-african-grey-parrot-food/` | **`/best-african-grey-parrot-food/` — identical slug** |
| `/african-grey-vs-macaw/` | **`/african-grey-vs-macaw/` — identical slug** |
| `/african-grey-vs-amazon-parrot/` | **`/african-grey-vs-amazon-parrot/` — identical slug** |
| `/african-grey-parrot-vs-cockatoo/`, `/cockatoo-vs-african-grey/` | `/african-grey-vs-cockatoo/` |
| `/african-grey-parrot-vs-macaw/`, `/macaw-vs-african-grey/` | `/african-grey-vs-macaw/` |
| `/amazon-parrot-vs-african-grey/` | `/african-grey-vs-amazon-parrot/` |
| `/how-much-does-an-african-grey-parrot-cost/`, `/how-much-does-an-african-gray-parrot-cost/` | `/african-grey-parrot-price/` |
| `/how-long-do-grey-parrots-live/` | `/african-grey-parrot-lifespan/` |
| `/what-do-african-grey-parrots-eat/`, `/what-can-african-greys-eat/`, `/what-do-african-gray-parrots-eat/`, `/what-do-african-grey-parrots-eat-in-the-wild/` | `/african-grey-parrot-diet/` |
| `/how-to-stop-african-grey-from-plucking/` | `/blog/african-grey-health-problems/` |
| `/types-of-african-grey-parrots/`, `/african-grey-in-the-wild/`, `/where-do-african-grey-parrots-live/`, `/how-big-do-african-grey-parrots-get/`, `/how-big-are-african-grey-parrots/`, `/how-big-is-an-african-grey-parrot/`, `/do-african-greys-know-what-they-are-saying/`, `/do-african-greys-understand-what-they-are-saying/` | `/african-grey-parrot-guide/`, `/blog/african-grey-parrot-talking-ability/` |

**And four transactional slugs on a Tier-3 informational site:**
`/african-grey-for-sale-by-owner-near-me/` · `/baby-african-grey-parrot-for-sale-near-me/` ·
`/where-can-i-buy-a-african-grey-parrot/` · `/where-can-i-get-an-african-grey-parrot/`

### 2. Section inventory — structurally the weakest pages measured

| | `/congo-vs-timneh-african-grey/` | `/best-african-grey-parrot-food/` |
|---|---|---|
| Words | **1,577** | **1,121** |
| H1 / H2 / H3 | 1 / **1** / 1 | 1 / **1** / 1 |
| The single H2 | `×Do you know the best pet for your personality?` — **a quiz pop-up, not content** | same |
| Only H3 | `What to Keep in Mind About Costs and Care` | same |
| Images | 84 (1 missing alt) — overwhelmingly related-post thumbnails | 84 |
| Tables | **0** | 0 |
| `ld+json` | BlogPosting · WebPage · Person · Organization · WebSite · BreadcrumbList · ImageObject · ListItem | same |
| FAQPage | **absent** | absent |
| Published | 2024-03-03 | 2025-01-02 |

Both pages are effectively **a title and a wall of undifferentiated prose** — one real subheading
apiece. CAG's comparison cluster ships full H1→H6 with tables and FAQPage against this.

### 3. 🚩 Trust flag — the vet-authority site publishes its African Grey content anonymously

The site's entire brand promise, verbatim from `/about/`:

> *"You ask pet related questions, and **Dr. Jess, a licensed veterinarian** will answer them… **Dr.
> Jess Kirk, DVM** is a licensed veterinarian in the state of **Georgia**, currently working in
> academia. In previous years Dr. Jess has worked in private practice…"*
>
> *"VetExplainsPets.com has been voted one of the top 100 pet websites on Feedspot and is featured in
> **Forbes, Readers Digest, INSIDER, POPSUGAR, How Stuff Works, OutwitTrade and Pet Lovers Centre**."*

Measured on the African Grey pages:

- Every one of **10 AG pages sampled** is attributed to `author/wg5ri1iuby` — a random-slug author archive
- The rendered byline on `/congo-vs-timneh-african-grey/` is literally **`By /`** — an empty name
- The `Person` object in the page's own JSON-LD has **`"name": ""`**
- The author archive at `/author/wg5ri1iuby/` is titled *"Dr. Jess"* but carries **700 articles** and
  an **empty `<h1>`**

So the credential is real and named at the site level, and **absent at the page level on every
African Grey article.** A 180,458-page site cannot have a Georgia DVM personally author 700 posts
under a randomised slug with an empty schema name, and the markup does not claim she did.

The AG pages also monetise into pet insurance: *"A routine visit might cost $75–$150, but more
serious issues involving lab work, imaging, or emergency care can range from **$800 to $3,000** or
more. Because of this, many pet owners consider pet insurance…"*

### 4. Visual inventory

84 `<img>` on each AG page, almost entirely related-post thumbnails rather than content imagery.
**Zero tables, zero infographics, zero video, zero iframes.** One image missing alt per page.

### 5. Reddit / forum mining

No branded mentions found. **NOT FETCHED** as a sentiment signal — barrier: no indexed threads name
this site.

### Corrections to the 2026-05-15 revised baseline

| Baseline claim | Measured 2026-08-10 |
|---|---|
| **"Firecrawl map search returned no dedicated AG health pages — only sidebar mentions"** | **False. ~33 dedicated African Grey pages**, found by sitemap walk. `firecrawl_map` samples; it does not enumerate. |
| **"Threat revised from MEDIUM to LOW"** | Not supportable as written. They hold **four exact CAG slug collisions** and **seven Congo-vs-Timneh permutations**. |
| "Total pages: UNVERIFIED" | **180,458.** |
| "Key page word count: estimated 1,500–3,000 (vet-authored standard)" | 1,577 and 1,121 measured — bottom of the estimate, and **not vet-bylined**. |
| "Vet affiliation: Yes — site premise is vet-written advice" | True of the *site*. **False of the African Grey pages**, which carry an empty byline and an empty schema `name`. |
| "Schema: UNVERIFIED — likely Article + Person with professional credentials" | BlogPosting + Person, **with the Person name blank**. |

### Key insight

Vet Explains Pets is the **highest-volume slug collision in the registry** — four identical CAG URLs
and seven Congo-vs-Timneh permutations — built on 1,100–1,600-word pages with **one real subheading
each, no tables, no FAQPage, and an empty byline on a site whose whole promise is a named
veterinarian.** They out-index us 1,700:1 and lose on every structural axis we already ship. The
correct response is not to fear them; it is to make sure our identical slugs win on depth,
authorship and schema, because that is the entire delta.

---

## A7 · Bird Addicts — https://birdaddicts.com

Tier 3 · informational_content · priority `low` · **baseline: "unreachable — likely defunct — remove
from active monitoring — no competitive threat"**

### 🚩 FINDING — the site is alive, actively publishing in 2026, and is a direct comparison rival. The baseline failed on a `www.` prefix.

| Host | system DNS | `@1.1.1.1` | `@8.8.8.8` | HTTP |
|---|---|---|---|---|
| **`www.birdaddicts.com`** — the URL in `data/competitors.json` | **no A record** | **no A record** | **no A record** | unreachable |
| **`birdaddicts.com`** — the apex | 172.67.137.180 | 104.21.70.164 | 172.67.137.180 | **200** |

The registry stores `https://www.birdaddicts.com`. That hostname has **no A record on any of three
resolvers**, so every automated check has reported the site dead. The apex serves HTTP/2 200 behind
Cloudflare. This is the exact failure mode page 5 found on `handRearedParrots` — a wrong hostname
recorded as a dead business.

### 1. Publishing activity — the site is not dormant, it is current

Sitemap walk (`/post-sitemap.xml`): **99 posts.**
`lastmod` 2022=14 · 2023=59 · 2024=18 · **2026=8** · newest **2026-06-09**.
Homepage confirms live cadence: *"Are Conure Parrots Good Pets? What Nobody Tells You Before Buying —
June 10, 2026"* and *"African Grey vs Conure – Which Makes a Better Pet — updated June 9, 2026."*

### 2. African Grey inventory — seven comparison posts, and they hit five of CAG's five spokes

| Bird Addicts URL | `lastmod` | Collides with |
|---|---|---|
| `/timneh-african-grey-vs-congo-african-grey-which-bird-to-get/` | 2024-01-16 | **CAG `/congo-vs-timneh-african-grey/`** |
| `/cockatoo-vs-african-grey/` | 2023-11-11 | **CAG `/african-grey-vs-cockatoo/`** |
| `/macaws-vs-african-greys-which-parrot-is-right-for-you/` | **2026-05-19** | **CAG `/african-grey-vs-macaw/`** |
| `/amazon-parrot-vs-african-grey-parrot-9-differences-bird-addicts/` | 2023-11-08 | **CAG `/african-grey-vs-amazon-parrot/`** |
| `/eclectus-parrot-vs-african-grey-which-bird-should-you-get/` | 2023-08-24 | **CAG `/blog/african-grey-vs-eclectus/`** |
| `/african-grey-parrot-vs-conure/` | **2026-06-09** | **no CAG equivalent** |
| `/african-grey-vs-quaker-parrot-choosing-the-perfect-feathered-friend/` | 2023-11-17 | **no CAG equivalent** |

**Five of CAG's five African Grey comparison spokes are matched, and they hold two we do not.** Two
of the seven were refreshed within the last three months.

### 3. Section inventory — good content architecture, zero technical SEO

| | `/macaws-vs-african-greys/` | `/timneh-vs-congo/` | `/cockatoo-vs-african-grey/` |
|---|---|---|---|
| Words | **2,424** | **2,297** | **1,880** |
| H1 / H2 / H3 | 1 / **17** / 0 | 1 / 2 / **13** | 1 / **11** / 0 |
| Images (missing alt) | 10 (0) | 7 (0) | 11 (**2**) |
| Tables | 0 | 0 | 0 |
| **`ld+json` blocks** | **0** | **0** | **0** |
| **Meta description** | **none** | **none** | **none** |
| **Canonical** | **none** | **none** | **none** |
| Published → modified | 2023-10-16 → **2026-05-19** | 2023-10-05 → 2024-01-16 | 2023-09-26 → 2023-11-11 |

Their H2 sets are genuinely well-shaped buyer questions — from `/macaws-vs-african-greys/`, verbatim:
*Visual Difference · Personality of the Bird · Biting Issue · Adaptability to New Environment,
Emotional Stability · Social or Tend to Bond with Single Person · Cuddly, Likes Head/Belly Scratches
or Does Not Like Being Held · Screaming/Noise Level/Loudness · Energy Level of the Birds ·
Trainability/Intelligence · Talking Ability · Feather Plucking Issue · Special Care · Aggression
Toward Other Birds, Cage Aggression · Health Concerns · Housing Around Children · Food Habit ·
Final Suggestion.*

From `/timneh-vs-congo/`, verbatim: *How Do They Look? · What's Their Personality Like? · Do They
Bite? · Can They Talk? · Do They Pluck Feathers? · Are They Good Around Children? · Are They Loud? ·
What Do They Eat? · How Well Can They Mingle? · Are They Aggressive? · Can They Be Trained? · What
Health Concerns Do They Pose? · How Much Do They Cost?*

**No structured data of any kind on any page.** No meta descriptions. No canonicals. 2,400 words of
decent comparison content with zero machine-readable markup.

### 4. Authority signals

`/about-us/`, verbatim: *"Hi, I am **Mohammad Arfanul Kabir, CEO of Bird Addicts. I am from
Bangladesh**… In 2018… I found that information on webpages are substantially different from the real
life owners… So, decide to collect all that owner's experience and keep them in an ordered manner…
On our website, most of the information is **real time experience of bird owners and good
breeders**."*

No veterinary credential, no US presence, no address, no phone. Post bylines read `Bird Addict` /
`shanto`. The stated method is explicit aggregation of Facebook-group owner reports.

### 5. SERP snapshot and Reddit mining

Did **not** appear in the top 10 of any Google or DuckDuckGo query captured — including
`african grey vs cockatoo` and `congo vs timneh african grey`, where they ship the matching page.
AI Overview citations: **zero**. Reddit branded mentions: **none found**.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-10 |
|---|---|
| **"Inaccessible (ECONNREFUSED — site may be down or defunct)"** | **False. HTTP 200.** The registry's `www.` hostname has no A record on any of three resolvers; the apex is live. |
| **"Remove from active competitor monitoring list. No competitive threat to CAG."** | **False. Seven African Grey comparison posts** matching **five of CAG's five spokes**, two refreshed in 2026. |
| Everything else UNVERIFIED | Now measured: 99 posts, 1,880–2,424 words, **zero structured data**, no meta descriptions, no canonicals, Bangladesh-based owner-aggregation model. |

### Key insight

The most consequential registry error found in this sweep: a live, 2026-active, seven-post African
Grey comparison rival was written off as defunct because of a `www.` prefix. And their weakness is
total on exactly the axis CAG is strong — **zero `ld+json`, zero meta descriptions, zero canonicals,
zero tables** against 2,400 words of well-structured buyer questions. Their H2 sets are a free
content brief for the two comparison pages CAG does not have (**African Grey vs Conure**, **African
Grey vs Quaker**).

---

## A8 · Parrot Website — https://www.parrotwebsite.com

Tier 3 · informational_content · priority `low` · baseline: *"No African Grey content detected… zero
direct informational competition… No actions needed against this competitor."*

### 🚩 FINDING — 45 African-Grey-titled URLs, publishing three days before this sweep

Sitemap walk: **917 URLs.** `lastmod` 2020=90 · 2021=135 · 2022=175 · 2023=25 · 2024=63 · 2025=256 ·
**2026=172**. **Newest `lastmod`: 2026-08-07** — three days before this fetch.

### 1. African Grey inventory — 45 slugs, organised into four attack clusters

**Species hub (2):** `/african-grey-parrot/` · `/african-grey/`

**Comparison (2):**
`/african-grey-vs-cockatoo/` ← **exact CAG slug collision** ·
`/difference-between-timneh-and-congo-african-grey/`

**Commercial / price (2):** `/how-much-does-an-african-grey-cost/` · `/why-are-african-greys-so-expensive/`

**Buyer-decision + care (12):** `/are-african-greys-good-for-beginners/` ← collides with CAG
`/blog/is-african-grey-good-for-beginners/` · `/do-african-grey-parrots-make-good-pets/` ·
`/are-african-greys-endangered/` ← touches CAG `/cites-african-grey-documentation/` ·
`/can-african-greys-talk/` ← collides with CAG `/blog/african-grey-parrot-talking-ability/` ·
`/are-african-greys-loud/` · `/are-african-greys-smart/` · `/are-african-greys-dusty/` ·
`/are-african-greys-cuddly/` · `/are-african-greys-easy-to-breed/` ·
`/are-african-greys-smarter-than-macaws/` · `/how-much-does-an-african-grey-weigh/` ·
`/how-long-can-you-leave-an-african-grey-alone/`

**Behaviour (7):** `/do-african-greys-bite/` · `/do-african-greys-get-along-with-other-birds/` ·
`/do-african-greys-like-mirrors/` · `/do-african-greys-sleep-at-night/` ·
`/why-do-african-grey-parrots-shiver/` · `/why-do-african-greys-have-red-tails/` ·
`/why-does-my-african-grey-puff-up/`

**"Can African Greys eat X" cluster (11):** apples · bananas · cheese · cucumber · dragon fruit ·
eggs · french fries · grapes · green beans · oranges · pineapple · strawberries · tomatoes

**Affiliate "best [product] for African Grey" cluster (7):**
`/best-food-for-african-greys/` ← collides with CAG `/best-african-grey-parrot-food/` ·
`/best-cage-for-african-grey-parrots/` ← collides with CAG `/blog/african-grey-parrot-cage-setup/` ·
`/best-toys-for-african-grey-parrots/` · `/best-harness-for-african-grey-parrots/` ·
`/best-supplements-for-african-grey-parrots/` · `/best-training-treats-for-african-greys/` ·
`/best-travel-cage-for-african-greys/`

### 2. Section inventory — `/african-grey-vs-cockatoo/` (the exact slug collision)

**970 words · H1 1 · H2 4 · H3 1 · H4 2 · 4 images (0 missing alt) · 0 tables · 0 iframes.**
Schema: Article · WebPage · BreadcrumbList · WebSite · SearchAction · Organization · Person ·
ReadAction · ImageObject. **No FAQPage.** Author meta: **John**. Published and modified **2026-05-29**.

H2/H3/H4 verbatim: *Similarities · Differences · Which one is right for me? · Related Posts ·
Sign up to the Parrot Website Newsletter! · Thank you! · Parrot Problems.*

**970 words against CAG's full comparison-cluster build.** The page is a newsletter-capture shell with
a first-person hook (*"I was talking with a friend the other day about my African grey parrot…"*)
wrapped around three thin sections.

### 3. Visual inventory

4 images, all with alt. No tables, no infographics, no video. The dominant on-page element is the
`Parrot Problems` ebook / newsletter capture, which the baseline correctly identified as the
business model — it just missed that the model is now fed by 45 African Grey articles.

### 4. SERP snapshot and Reddit mining

Did **not** appear in the top 10 of any Google or DuckDuckGo query captured, including
`african grey vs cockatoo` where they ship the matching slug.
AI Overview citations: **zero**. Reddit branded mentions: **none found**.

### Corrections to the 2026-05-11 baseline

| Baseline claim | Measured 2026-08-10 |
|---|---|
| **"No African Grey content detected; covers cockatiels, conures, caiques"** | **False. 45 African-Grey-titled URLs**, including an exact CAG slug collision. |
| **"CAG has zero direct informational competition from this domain… No actions needed."** | **False.** Four CAG-page collisions and a 7-page affiliate cluster aimed at our diet and cage content. |
| "Homepage word count ~500; small blog" | **917 URLs**, 172 of them touched in 2026, newest **2026-08-07**. |
| "Schema: Not detected" | Article · WebPage · Organization · Person · BreadcrumbList · SearchAction. No FAQPage. |
| "Blog topics: cockatiel socialization, caique temperament, pineapple conure lifespan" | Accurate for 2020–2022. The 2025–2026 publishing is **African-Grey-weighted**. |

### Key insight

Parrot Website quietly re-pointed itself at African Greys between the baseline and now — 45 slugs,
172 URLs touched in 2026, and an African-Grey affiliate cluster targeting food, cages, toys,
harnesses, supplements, treats and travel cages. It ranks nowhere yet and its pages are thin
(970 words on the collision slug). This is the one to **monitor rather than react to** — but
"no actions needed" is no longer the right standing order.

---

# Part B: cross-cutting findings

## B1 · The AI Overview citation ledger — the headline of this sweep

Four Google AI Overviews captured live on 2026-08-10 (Playwright, `hl=en&gl=us`, **UK egress**).
Every AIO was present; none was suppressed.

| # | Query | AIO cited sources, verbatim from the citation chips | Any of our 8 Tier-3 sites cited? |
|---|---|---|---|
| 1 | `african grey parrot care` | **Tree of Life Exotic Pet Medical Center** (×4) · **Swiftail Exotic Telemedicine Veterinary Services** · **Reddit · r/parrots** | **No** |
| 2 | `congo vs timneh african grey` | "9 sites": **Instagram · Zeb Ernest** (+3) · **Chewy** (+5) · **Reddit · r/AfricanGrey** (+3) · **TikTok · geckoemmy** | **No** |
| 3 | `how much does an african grey parrot cost` | **Parrot Stars** (+3) · **YouTube · Parrot Baby** · **YouTube · The African Grey Journal** · **The Avian Exchange** | **No** |
| 4 | `are african greys good for beginners` | "11 sites": **BirdSupplies.com** · **YouTube · The Parrot Life** · **Falls Road Animal Hospital** · **ZuPreem** · **YouTube · Parrot Bliss** · **TikTok · blueplanetpets** | **No** |

On query 4 a programmatic substring test was run over the entire rendered SERP for all eight domains
plus `congoafricangreys` — **all nine returned false.** On queries 1–3 the AIO citation chips and the
organic link set were read directly; The Spruce Pets appears in the *organic* set on query 1 but is
not an AIO citation.

**0 of 8 Tier-3 registry sites cited across 4 AI Overviews.** Our Tier-3 registry is aimed at a
citation set that AI Overviews are not using.

**What AI Overviews actually cite for African Grey queries, ranked by appearances:**
1. **Avian veterinary practice sites** — treeoflifeexotics.vet, swiftailvet.com, Falls Road Animal Hospital
2. **Reddit** — r/parrots and r/AfricanGrey, by name
3. **Short-form video** — YouTube, TikTok, Instagram, with named creators
4. **Commerce brands** — Chewy, ZuPreem, BirdSupplies.com, **Parrot Stars**, **The Avian Exchange**

### 🚩 B1a — the AI Overview is telling buyers that CAG's price floor is a scam

Query 3 AIO, verbatim:

> *"A healthy, hand-raised African Grey parrot from a reputable U.S. breeder typically costs between
> **$2,750 and $8,500**… **Reputable Breeders: Expect to pay $6,500 to $8,500** for a hand-fed,
> DNA-sexed baby Congo African Grey, while the slightly smaller Timneh African Grey averages around
> $6,500 at specialized facilities like **Parrot Stars**."*
>
> *"**⚠️ Scam Warning: Be highly suspicious of any online listing offering African Greys for under
> $1,500.** Platforms like **The Avian Exchange** warn that cheap bird offers online are almost
> always scams designed to steal deposit money."*

CAG's Congo range is **$1,500–$3,500**. Timneh Evie is listed at **$1,500**. **Google's AI Overview
is currently drawing the scam line at exactly CAG's floor price**, and anchoring "reputable breeder"
at $6,500–$8,500 by citing a Tier-1 registry competitor by name.

This is a live commercial risk that no Tier-3 content site created and none of them can fix. It also
reframes the price page: the job is no longer "justify $1,500–$3,500 as good value," it is
**"explain why an honest, documented, hand-raised, health-guaranteed Texas bird at $1,500–$3,500 is
not the thing the scam warning is about"** — with the documentation that separates us from the
$200-and-free listings page 5 surfaced.

### 🚩 B1b — the beginners AIO actively routes buyers to other species

Query 4 AIO opens: *"**No**, African grey parrots are generally not good pets for beginners,"* and
closes by recommending **Budgies, Cockatiels and Green-Cheek Conures** instead. That is a
top-of-funnel leak on a query CAG already has a page for
(`/blog/is-african-grey-good-for-beginners/`). The AIO's own cited nuance — *"5 or more hours of
daily interaction," "sexual maturity around 5 to 7 years"* — is answerable by a breeder who weans at
12–16 weeks and supports the placement, which is exactly the angle nobody in the cited set has.

### B1c — one AIO artefact worth recording

Query 1 AIO states *"a diet of 60–70% high-quality **Chewy** pellets."* No pellet brand called
"Chewy" exists; this is brand-name injection from the retailer's citation. Query 3 AIO states
*"Avian Vet Exam: **$20** post-purchase screening, including disease testing and blood panels,"*
which is off by an order of magnitude. **AI Overviews are being cited as authority by buyers while
carrying errors of this size** — that is the argument for a page that states verifiable numbers.

## B2 · The engine split, measured

| Query | Google top 10 (Firecrawl) | Second engine — DDG / Bing-syndicated |
|---|---|---|
| `african grey parrot care` | 2 vet clinics · 4 forums · **Spruce Pets #5** · 1 brand · 1 UK retailer · 1 video | **allaboutparrots #1 · smallanimaladvice #2** · Spruce Pets #7 |
| `congo vs timneh african grey` | Reddit ×3 · YouTube ×4 · TikTok ×5 · Facebook ×4 · Instagram ×3 · Kaytee · a-z-animals · Etsy. **No Tier-3 site. No CAG.** | thevetdesk · exotic-birds · birdandbeyond · beautyofbirds · **congoafricangreys.com #5** · parrothaven.uk · a-z-animals · tiktokparrot · africangreyparrot.info |
| `african grey vs cockatoo` | Reddit #1 · avianavenue #2 · Quora #3 · Facebook #4 · parrotforums #5 · lafeber #6 · backyardchickens #7–8 · **Wikipedia #9** · Facebook video #10 | NOT FETCHED |
| `african grey parrot lifespan` | Reddit #1 · Facebook #2 · worldanimalprotection #3 · **Wikipedia #4** · YouTube #5 · animaldiversity #6 · avianavenue #8 · IFAW #9 | NOT FETCHED |

**Two readings.**

First: **CAG already ranks #5 organically on the second engine for `congo vs timneh african grey`** —
`congoafricangreys.com/congo-vs-timneh-african-grey/`, titled *"Congo vs Timneh African Grey: Size,
Talking Ability, Temperament…"* — while **none** of the three Tier-3 sites that ship that exact page
(birdaddicts, vetexplainspets with seven permutations, parrotwebsite) appear at all. The second
engine is where our comparison cluster is already working.

Second: **Google's version of the same query is owned by social video and forums**, and the AIO on
top of it cites Chewy, Reddit, Instagram and TikTok. Text SEO alone does not reach that SERP.

## B3 · Schema gap — measured both ways, and it favours CAG

CAG `dist/` scan, 105 built pages:

| Schema type | CAG pages carrying it |
|---|---|
| BreadcrumbList | 105 |
| Organization | 85 |
| WebPage | 80 |
| **FAQPage / Question / Answer** | **57** |
| PetStore | 41 |
| Article | 31 |
| Product | 28 |
| LocalBusiness | 27 |
| Offer | 20 |
| AggregateRating | 15 |

Against the eight competitors' African Grey pages:

| Site | AG-page schema | FAQPage? | Tables? | Notes |
|---|---|---|---|---|
| The Spruce Pets | Article · Person · Organization · BreadcrumbList · ImageObject (+ VideoObject on facts) | **No** | 0 | Named credentialled author |
| Wikipedia | Article · Organization · ImageObject | **No** | 4 | 5 images with no alt |
| Rational Parrot | Article · WebPage · Organization · Person · BreadcrumbList · SearchAction | **No** | 2 | Ships an "FAQs" H2 without the markup |
| All About Parrots | Article · WebPage · Organization · Person · BreadcrumbList · SearchAction | **No** | 1 | |
| Small Animal Advice | BlogPosting · CollectionPage · Person · BreadcrumbList | **No** | 0 | Ships an "FAQs" H2 without the markup |
| Vet Explains Pets | BlogPosting · WebPage · Person (**name blank**) · Organization · BreadcrumbList | **No** | 0 | |
| **Bird Addicts** | **none — 0 `ld+json` blocks** | **No** | 0 | Also no meta description, no canonical |
| Parrot Website | Article · WebPage · Organization · Person · BreadcrumbList · SearchAction | **No** | 0 | |

**Not one of the eight ships FAQPage on any African Grey page. CAG ships it on 57.** The
2026-05-11 baseline framed FAQPage as a Spruce Pets advantage and a CAG gap; the measurement inverts
that completely. Two competitors ship a visible "FAQs" heading with no markup underneath it — a free
snippet they are leaving on the table and we are not.

## B4 · Page-type gaps across the eight

| Page type | Spruce | Wiki | Rational | AllAbout | SmallAnimal | VetExplains | BirdAddicts | ParrotWebsite | CAG has it? |
|---|---|---|---|---|---|---|---|---|---|
| AG species profile | Yes | Yes | No | Yes | Yes | Yes | No | Yes | Yes |
| Dedicated Congo vs Timneh | **No** | partial | No | partial | No | **Yes ×7** | **Yes** | **Yes** | **Yes — defend it** |
| AG price page | No | No | **Yes ×5** | **Yes** | No | **Yes ×2** | No | **Yes ×2** | Yes |
| AG diet / food page | in-profile | No | Yes | No | Yes | **Yes (exact slug)** | No | **Yes (exact slug)** | Yes |
| AG lifespan page | listicle | in-article | No | No | Yes | Yes | No | No | Yes |
| AG behaviour long tail | No | No | No | partial | **Yes ×16** | partial | No | **Yes ×7** | **Gap** |
| "Can AGs eat X" cluster | No | No | 1 | No | 2 | 4 | No | **Yes ×11** | **Gap** |
| "Best [product] for AG" affiliate | No | No | 1 | No | No | 1 | No | **Yes ×7** | n/a (we sell birds) |
| **US-specific AG legality / documentation** | No | No | No | **Quaker-only** | No | No | No | partial | **Yes — and nobody else does it right** |
| Where-to-buy / breeder guidance | **section + 3 outbound links** | No | **Yes ×6** | in-price-page | No | **Yes ×4** | No | No | Yes |
| FAQPage schema | No | No | No | No | No | No | No | No | **Yes ×57 — sole holder** |
| Comparison tables on AG pages | 0 | 4 | 2 | 1 | 0 | 0 | 0 | 0 | Yes |

## B5 · Keyword gaps worth CAG pages — exact phrases, all from measured fan-out

| Phrase | Source | Why it matters |
|---|---|---|
| `do you need a licence for an african grey parrot` | Google question-mods, care stem | Nobody credible answers it for the US; All About Parrots answers it for Quakers |
| `are african greys endangered` | parrotwebsite slug + Wikipedia infobox | CITES Appendix I authority play; feeds `/cites-african-grey-documentation/` |
| `african grey vs conure` | **birdaddicts ships it, refreshed 2026-06-09** | Comparison spoke CAG lacks |
| `african grey vs quaker parrot` | **birdaddicts ships it** | Comparison spoke CAG lacks |
| `african grey vs indian ringneck` | Google A–Z, `african grey vs` stem | Unowned in the measured set |
| `african grey vs cockatiel` | Google A–Z | Unowned; pairs with the beginners AIO that recommends cockatiels |
| `african grey vs crow intelligence` · `african grey vs raven intelligence` | Google A–Z | Pure-authority intelligence angle; Wikipedia adjacent |
| `african grey vs macaw vs cockatoo` | Google A–Z | Three-way — nobody in the set has one |
| `african grey vs umbrella cockatoo` · `vs blue and gold macaw` · `vs scarlet macaw` · `vs hahns macaw` · `vs yellow naped amazon` · `vs sun conure` · `vs alexandrine parrot` | Google A–Z | Sub-spoke expansion of the existing comparison cluster |
| `african grey vs macaw size` · `vs cockatoo size` · `vs eclectus size` · `vs macaw intelligence` | Google A–Z | Attribute-level long tail our spokes can absorb as H3s |
| `how long can african grey parrots be left alone` | Google 6+ word | smallanimaladvice + parrotwebsite both hold it; dormant and thin respectively |
| `do african grey parrots carry diseases` | Google 6+ word | Maps to the Ledger — psittacosis, PBFD/Polyomavirus PCR |
| `do african grey parrots need a companion` | Google 6+ word | Maps to the bonded-pair and companion-pair inventory |
| `how to transport an african grey parrot` | Google 6+ word | Maps to Delta / United / American cargo + IATA LAR |
| `what not to feed african grey parrots` | Google A–Z + smallanimaladvice slug | Diet-page target |
| `outline african grey parrot ownership costs care and expected lifespan` | Google 6+ word | **Prompt-shaped query** — an AEO/LLM-era demand signal, answerable in one structured section |
| `african grey parrot husbandry` · `african grey parrot enclosure` | **Bing-only** | Second-engine gap; we already rank #5 there on the comparison term |
| `african grey parrots for rehoming` · `african grey parrot rescue near me` | **Bing-only** | Adoption-language buyers, per page 5's Petfinder finding |

## B6 · Trust and CITES flags in this group (Rule 8)

| Site | Flag |
|---|---|
| **All About Parrots** | Presents **UK/EU CITES Article 10 certificates (TSC, SSC)** as US requirements on the top-ranked AG price page. Asserts **Timneh $3,500–$5,000 above Congo $2,000–$2,750**, unsupported by any listing measured. *(Their Appendix 1 statement is correct.)* |
| **Vet Explains Pets** | Brand promise is *"Dr. Jess, a licensed veterinarian will answer them."* **Every one of 10 AG pages sampled** carries an anonymous `author/wg5ri1iuby` byline rendering as `By /`, with `"name": ""` in the page's own Person schema. |
| **Rational Parrot** | 19,747 URLs on a site self-dated to 2025 (~44/day), with **six near-duplicate "where to buy an African Grey" pages**, sitting on r/parrots link equity whose original cited asset (`/diet.html`) now redirects to the homepage. |
| **Bird Addicts** | No structured data, no canonicals, no meta descriptions; method is explicit aggregation of Facebook-group owner reports; no vet review. Not deceptive — but not citable as a health source. |
| **Our own baseline corpus** | `competitor-wikipedia-2026-05-11.md` records **"CITES Appendix II"**. Wikipedia says Appendix I in three places. This is a Rule-2 error living inside our research folder. |

None of the eight makes a wild-caught or illegal-trade claim. No competitor in this group should be
cited by CAG as a price benchmark; **All About Parrots' A10 paragraph and price table are usable as
documented examples** on `/how-to-avoid-african-grey-parrot-scams/` and on a US documentation page.

## B7 · Recommended priority action, with the trade-off named

Three candidate moves came out of this sweep. Ranked, with exactly one recommended.

| # | Move | Grounded in | Trade-off |
|---|---|---|---|
| 1 | **(Recommended) Rewrite `/african-grey-parrot-price/` to answer the AI Overview's scam line head-on, and add a US-specific documentation section.** | AIO query 3 draws the scam threshold at **under $1,500** — exactly CAG's floor — and anchors "reputable breeder" at **$6,500–$8,500** citing Parrot Stars. All About Parrots, the second-engine #1 for care, tells US buyers they need **UK Article 10 certificates**. Spruce Pets anchors **$2,000–$4,000** with no CITES content at all. Nobody in the eight answers US documentation correctly. | It is a defensive rewrite of a page that already exists, so it wins no new slug and no new impressions on its own. It protects the conversion path rather than expanding the footprint — the return shows up in enquiry quality, not in a rank chart. |
| 2 | Build `african grey vs conure` and `african grey vs quaker parrot` | The only two comparison spokes Bird Addicts holds that CAG does not; theirs carry **zero schema, zero canonicals, zero meta descriptions** and we already rank #5 on the second engine for the sibling term. | Two new pages of build cost for two low-volume spokes; the demand is real but thinner than the price cluster. |
| 3 | Request a listing on `beautyofbirds.com/africangreybreeders.html` | It is one of **three** outbound destinations from The Spruce Pets' `Where to Adopt or Buy` section — the highest-authority AG care page on the open web — and CAG is on none of them. | Outreach, not a build; outcome is outside our control and unmeasurable until it lands. |

Move 1 is recommended because it is the only one addressing a **measured, live commercial risk**
rather than an opportunity: Google is currently telling buyers that a listing at CAG's exact floor
price is probably a scam, and the correction requires facts we already hold in the Ledger.

---

## Proposed registry patch — NOT applied, for breeder approval

`data/competitors.json` was **not modified**, per the brief. Proposed changes, in priority order:

1. **Fix `birdAddicts.url`** → `https://birdaddicts.com` *(the stored `www.` host has no A record on
   the system resolver, `1.1.1.1`, or `8.8.8.8`; the apex returns 200)*. Clear the
   "defunct / remove from monitoring" note.
2. **Raise `birdAddicts.priority`** `low` → **`medium`** — seven AG comparison posts matching five of
   CAG's five spokes, two refreshed in 2026.
3. **Raise `vetExplainsPets.priority`** `low` → **`medium`** and replace the 2026-05-15 note. The
   "no dedicated AG pages" finding was a `firecrawl_map` sampling limit, not a site fact: the sitemap
   walk finds ~33 AG pages including **four exact CAG slug collisions** and **seven Congo-vs-Timneh
   permutations** across 180,458 URLs.
4. **Raise `allAboutParrots.priority`** `medium` → **`high`** — organic **#1 on the second engine**
   for `african grey parrot care`, six r/parrots citations, and the page r/AfricanGrey routes
   legality questions to.
5. **Raise `parrotWebsite.priority`** `low` → **`medium`** — 45 AG slugs, 172 URLs touched in 2026,
   newest 2026-08-07, one exact CAG slug collision.
6. **Re-tier `rationalParrot`** — currently Tier 3 informational; ships **six "where to buy an
   African Grey" pages** and five price pages across 19,747 URLs. Breeder decision required (see
   Open Flags).
7. **Correct `competitor-wikipedia-2026-05-11.md`** — it records **CITES Appendix II**. Wikipedia
   states Appendix I in the infobox, the body and the page category. This is a Rule-2 error inside
   our own corpus and should be fixed even though the file is a research artifact.
8. **Set `last_analyzed: "2026-08-10"`** for all eight ids *(note: fetch date, not the 2026-08-09
   sweep batch label)*.
9. **Add `access_status`** to the seven entries lacking it: `thesprucePets` →
   `"playwright_only — curl 403, Firecrawl publisher-refusal"`; the rest → `"accessible"`.

### Proposed new competitors — NOT added, for breeder approval

Surfaced by AIO citations and second-engine SERPs; none is currently in the registry.

| Candidate | Why it surfaced | Suggested tier |
|---|---|---|
| **treeoflifeexotics.vet** | **AIO citation ×4** and Google **#1** for `african grey parrot care` | 3 — and arguably the single most important informational competitor we do not track |
| **swiftailvet.com** | **AIO citation**, Google #3 for `african grey parrot care` | 3 |
| **Falls Road Animal Hospital** (`fallsroad.com`) | **AIO citation** on the beginners query | 3 |
| **BirdSupplies.com** | **AIO citation** on the beginners query | 4 |
| **ZuPreem** (`zupreem.com`) | **AIO citation** + Google #7 for care | 4 |
| **beautyofbirds.com** | The Spruce Pets' outbound **"List of Breeders"**; also DDG #4 for congo-vs-timneh | 3 — and a link target |
| **thevetdesk.com** | DDG **#1** for `congo vs timneh african grey` | 3 |
| **exotic-birds.com** | DDG #2 congo-vs-timneh, #9 for care | 3 |
| **birdandbeyond.com** | DDG #3 congo-vs-timneh, and it **sells birds** (`/birds-for-sale/african-grey/`) | 1 or 2 |
| **parrothaven.uk** · **tiktokparrot.com** · **africangreyparrot.info** · **a-z-animals.com** | DDG top 10 congo-vs-timneh | 3 |
| **lafeber.com** · **kaytee.com** | Google top 10 on comparison and care queries | 4 |

---

## Open Flags

**Open question for the breeder (one, narrow):**
**Should `rationalParrot` stay Tier 3 (informational_content), or move to Tier 2/4?** It is filed as
an informational blog. Measured, it is a 19,747-page programmatic publisher whose African Grey
footprint is **11 transactional/commercial slugs out of 13** — six "where to buy an African Grey"
pages and five "how much does it cost" pages aimed directly at CAG's funnel — with no vet credential
and a 2025 founding date. The answer changes its monitoring cadence and which gap matrix it lands in.
Everything else in this sweep is complete and unblocked.

**NOT FETCHED list, with barriers named:**

| Item | Barrier |
|---|---|
| The Spruce Pets via `curl` | **HTTP 403** bot challenge on every attempt, via system DNS and both public resolvers. Retrieved successfully via Playwright — **not a dead site**. |
| The Spruce Pets via Firecrawl | Publisher-level exclusion — Firecrawl returns *"We apologize… we do not support this site"* (Dotdash Meredith). |
| Bing organic top 10, all queries | Not re-attempted this pass. Page 5 established four-transport query-truncation on Bing; DuckDuckGo (Bing-syndicated) used as the explicitly-labelled proxy. |
| Reddit brand mining via the Reddit JSON API | **HTTP 403** from this IP on both `www.reddit.com/search.json` and `old.reddit.com/search.json` — bot challenge. Substituted with Firecrawl `site:reddit.com` search. |
| Reddit sentiment for `smallAnimalAdvice`, `vetExplainsPets`, `birdAddicts`, `parrotWebsite`, `wikipedia` | No indexed branded threads exist to mine — absence of a signal, not a fetch failure. |
| DuckDuckGo SERP for `african grey vs cockatoo`, `african grey parrot lifespan`, `african grey parrot price`, `are african greys good for beginners` | Not fetched — capture budget spent on the two highest-value comparison and care terms. |
| Total indexed page count for `thesprucepets.com` and `en.wikipedia.org` | No usable public post-sitemap for the AG subset; a `site:` operator count is an estimate, not a measurement, so it is omitted rather than guessed. |
| Absolute **US** SERP positions, every query | Egress is `82.18.132.216` — **AS5089 Virgin Media, Birmingham, GB**. `gl=us&hl=en` changes result parameters, not the egress IP. All positions are UK-egress, US-parameterised. Firecrawl `search` egress country was not measured. |
| Google PAA expanded three levels | Only the first-level PAA set was captured per query (4 questions each); no click-expansion was performed, to avoid the `/sorry/` CAPTCHA that ended page 5's Google access. |
| Core Web Vitals / PageSpeed for all eight | Not attempted — out of scope for an informational-competitor pass and would have consumed the remaining Playwright budget. |
| Per-page word counts for the other ~28 `smallAnimalAdvice` AG articles and the other ~40 `parrotWebsite` AG articles | Flagship pages measured; the remainder inventoried by slug and `lastmod` only. Enumeration is complete; depth sampling is not. |

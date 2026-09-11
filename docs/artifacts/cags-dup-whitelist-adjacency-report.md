# Hidden Crossover Report

## 1. What was wrong
Both duplicate-content gates grow every shared 12-word window into its longest shared run, and then **skipped the whole run if any whitelisted line sat inside it**.

So a genuine crossover that touched a whitelisted line was exempted along with it. The trigger was the shipping line, "Ships nationwide · $185 airport · $350 home", with any shared passage directly before or after it on both pages.

- Render harness: `tests/render/checks/dup.ts`, `if (whitelist.some((w) => run.includes(w))) continue;`
- Python: `scripts/dup_content_audit.py`, `if any(w in run for w in WHITELIST_SNIPPETS): continue`. It also skipped every window that held a whitelisted line, so growth could start mid-line ("airport $350 home …") and drag a fragment of the whitelisted text into a report.

Nothing about the rule changed. The rule already covered this; the tool was blind to it. Per the learning loop, that is charged to the harness, with no new rule.

## 2. What changed
- **Failing test first.** A new fixture pair: `known_broken/dup-adjacent-to-whitelist.html` plus the corpus sibling `sibling-hand-raised-african-grey-texas.html`. It has an 18-word passage right before the shipping line and a 17-word `<legend>` right after it. The meta gate went red for the right reason: examined ≥ 1, defects 0. The Python gate printed "PASS … in 2 pages" on the same pair.
- **The fix, identical in both gates.** Every whole-word whitelisted phrase is cut out of the run, and each remaining piece is judged on its own. Every piece of 12+ words is one finding.
- **Python's per-window skip is removed,** so both gates grow runs from the same first word.
- **Split, not re-join.** `known_good` now holds 6 shared words, the shipping line, then 9 shared words. It must stay silent, so a fix that glued the two sides back into one 15-word passage would fail.
- `tests/test_dup_content_audit.py`: 5 tests run the Python gate over the same fixtures the harness uses.
- `RENDER_SITE_PORT` / `RENDER_FIXTURE_PORT` move the harness off 4321/4322, so a second worktree's run doesn't collide with a live one.
- **No page copy edited. No rule row changed** in `rule-index.json`, and no new rule was written.

Commit `a09e33d4` on `main`, rebased over the same-day forms work (`6a854485`, which made the harness skip `<form>` text). The two changes are independent of each other.

## 3. Gates run
| Gate | Result |
|---|---|
| `test:render:meta`, before the fix | new adjacency test FAILED: 0 defects, examined ≥ 1; everything else green |
| `test:render:meta`, after the fix | 283 passed, 0 failed |
| `test:render:meta`, after the rebase | 292 passed, 0 failed |
| `pytest tests/test_dup_content_audit.py tests/test_form_contract_audit.py` | 23 passed |
| `dup_content_audit.py`, all 105 built pages, before → after | 5,659 → 6,128 findings |
| `test:render:pages`, before and after on the same `dist/` | 55 passed / 2 failed each run. Every failure is a blocking **NAV** row, and each run failed on **different** pages. Timing flake from three harness runs sharing the CPU, not DUP; DUP is advisory and cannot fail a page |

## 4. Render harness: newly surfaced, by target page
**0 newly surfaced.** Before and after are identical on every target page at every viewport (375 / 768 / 1280). The table shows the largest count across the three viewports.

| Target page | DUP siblings compared | Before | After | Change |
|---|---|---|---|---|
| `african-grey-breeding-pair-for-sale` | 11 | 30 | 30 | +0 |
| `african-grey-parrot-adoption-cost` | 11 | 18 | 18 | +0 |
| `african-grey-parrot-bird-eggs-for-sale-usa` | 11 | 34 | 34 | +0 |
| `african-grey-parrot-care-guide` | 0 | 0 | 0 | +0 |
| `african-grey-parrot-for-sale-florida` | 0 | 0 | 0 | +0 |
| `african-grey-parrot-health-guarantee` | 11 | 36 | 36 | +0 |
| `african-grey-parrots-for-sale` | 0 | 0 | 0 | +0 |
| `african-grey-parrots-for-sale-near-me` | 11 | 0 | 0 | +0 |
| `available/roys` | 0 | 0 | 0 | +0 |
| `baby-african-grey-parrot-for-sale` | 11 | 22 | 22 | +0 |
| `blog/african-grey-parrot-cage-setup` | 0 | 0 | 0 | +0 |
| `buy-african-grey-parrots-with-shipping` | 11 | 0 | 0 | +0 |
| `congo-african-grey-for-sale` | 11 | 32 | 32 | +0 |
| `congo-african-grey-parrot-pair-for-sale` | 11 | 28 | 28 | +0 |
| `congo-vs-timneh-african-grey` | 0 | 0 | 0 | +0 |
| `dna-tested-african-grey-for-sale` | 11 | 22 | 22 | +0 |
| `hand-raised-african-grey-parrot-for-sale` | 11 | 22 | 22 | +0 |
| `index` | not wired | 0 | 0 | +0 |
| `timneh-african-grey-for-sale` | 11 | 32 | 32 | +0 |

**Why zero is honest here, and what it doesn't cover.** The harness only compares a page with other targets of the *same page type* (`pages.spec.ts:123`). Only for-sale has more than one target, so it's the only type actually compared, and the Python gate found no newly surfaced passage there either. The two gates agree.

Every other page type has a single target, so DUP compares it against **0 siblings**, and the homepage isn't wired for DUP at all. Everything that surfaced site-wide sits on those types, where the harness sees nothing. That's a separate coverage gap, filed as its own task ("Widen DUP harness siblings beyond same page type"); it isn't fixed here.

## 5. Site-wide (Python gate): newly surfaced crossovers
**481 findings that were hidden before: 54 distinct passages across 70 pages.**

Separately, 256 existing findings changed wording, because the whitelisted phrase is now cut out of them. They aren't new, and they're counted in §6.

Grouped by type. Each line shows the passage's longest length, how many pages carry it, its opening words, and the pages:

### A. Bird-card strip (price · deposit · Inquire · name · age) — 19 passages, 19 pages
- 39w · 11 pages · "$2 300 $200 deposit inquire new arrival midland tx amie female 3 mo congo africa…" → african-grey-care, african-grey-parrot-care-guide, african-grey-parrot-diet, african-grey-parrot-guide, african-grey-parrot-health-guarantee, african-grey-parrot-lifespan, african-grey-parrot-price, best-african-grey-parrot-food, blog/african-grey-parrot-cage-setup, captive-bred-african-grey-parrot, trusted-african-grey-parrot-breeders
- 38w · 10 pages · "$1 600 $200 deposit inquire timneh midland tx evie female 6 mo timneh african gr…" → african-grey-care, african-grey-parrot-care-guide, african-grey-parrot-diet, african-grey-parrot-guide, african-grey-parrot-lifespan, african-grey-parrot-price, best-african-grey-parrot-food, blog/african-grey-parrot-cage-setup, captive-bred-african-grey-parrot, trusted-african-grey-parrot-breeders
- 47w · 10 pages · "$1 500 $200 deposit inquire must go pair midland tx jins jeni pair 4 6 mo congo …" → african-grey-care, african-grey-parrot-care-guide, african-grey-parrot-diet, african-grey-parrot-guide, african-grey-parrot-health-guarantee, african-grey-parrot-lifespan, african-grey-parrot-price, best-african-grey-parrot-food, captive-bred-african-grey-parrot, trusted-african-grey-parrot-breeders
- 39w · 9 pages · "$1 700 $200 deposit inquire timneh midland tx elad male 5 mo timneh african grey…" → african-grey-care, african-grey-parrot-care-guide, african-grey-parrot-diet, african-grey-parrot-guide, african-grey-parrot-health-guarantee, african-grey-parrot-price, best-african-grey-parrot-food, captive-bred-african-grey-parrot, trusted-african-grey-parrot-breeders
- 41w · 8 pages · "$2 500 $200 deposit inquire best value midland tx bery female 1 yr congo african…" → african-grey-care, african-grey-parrot-care-guide, african-grey-parrot-guide, african-grey-parrot-health-guarantee, african-grey-parrot-price, blog/african-grey-parrot-cage-setup, captive-bred-african-grey-parrot, trusted-african-grey-parrot-breeders
- 44w · 8 pages · "$2 500 $200 deposit inquire baby boy midland tx roys male 4 mo congo african gre…" → blog/african-grey-health-problems, blog/african-grey-parrot-facts, blog/african-grey-parrot-price-what-you-get, blog/african-grey-parrot-talking-ability, blog/african-grey-parrot-training, blog/african-grey-vs-eclectus, blog/best-place-to-buy-african-grey-parrot, blog/is-african-grey-good-for-beginners
- 41w · 5 pages · "$2 300 $200 deposit inquire best value midland tx bery female 1 yr congo african…" → blog/african-grey-health-problems, blog/african-grey-parrot-facts, blog/african-grey-vs-eclectus, blog/best-place-to-buy-african-grey-parrot, blog/is-african-grey-good-for-beginners
- 41w · 5 pages · "$1 700 $200 deposit inquire bonded duo midland tx jins jeni pair 4 6 mo congo af…" → blog/african-grey-health-problems, blog/african-grey-parrot-facts, blog/african-grey-vs-eclectus, blog/best-place-to-buy-african-grey-parrot, blog/is-african-grey-good-for-beginners
- 34w · 4 pages · "baby boy midland tx roys male 4 mo congo african grey energetic curious and impo…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, blog/african-grey-parrot-talking-ability
- 34w · 4 pages · "new arrival midland tx amie female 3 mo congo african grey she mimics your laugh…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, blog/african-grey-parrot-talking-ability
- 39w · 4 pages · "$200 deposit inquire best value midland tx bery female 1 yr congo african grey g…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, blog/african-grey-parrot-talking-ability
- 42w · 4 pages · "new arrival midland tx amie female 3 mo congo african grey hand raised fully doc…" → blog/african-grey-parrot-facts, blog/african-grey-vs-eclectus, blog/best-place-to-buy-african-grey-parrot, blog/is-african-grey-good-for-beginners
- 36w · 3 pages · "$200 deposit inquire timneh midland tx elad male 5 mo timneh african grey smalle…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup
- 45w · 3 pages · "$200 deposit inquire must go pair midland tx jins jeni pair 4 6 mo congo african…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup
- 43w · 2 pages · "with lifetime support from mark teri view all birds baby boy midland tx roys mal…" → african-grey-care, african-grey-parrot-care-guide
- 20w · 2 pages · "$3 500 pair $200 deposit inquire cites captive bred cert pcr dna sex certificate…" → african-grey-care, african-grey-parrot-care-guide
- 22w · 2 pages · "$3 500 pair $200 deposit inquire cites captive bred cert closed band hatch cert …" → african-grey-parrot-guide, captive-bred-african-grey-parrot
- 45w · 2 pages · "view all birds baby boy midland tx roys male 4 mo congo african grey hand raised…" → african-grey-parrot-guide, african-grey-parrot-price
- 47w · 2 pages · "on a live video call new arrival midland tx amie female 3 mo congo african grey …" → blog/african-grey-parrot-facts, blog/african-grey-vs-eclectus

### B. Bird-card blurb (per-bird personality line) — 8 passages, 9 pages
- 30w · 5 pages · "roys male 4 mo congo african grey energetic curious and impossible to ignore han…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, blog/african-grey-parrot-talking-ability, index
- 30w · 5 pages · "amie female 3 mo congo african grey she mimics your laugh before you finish it p…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, blog/african-grey-parrot-talking-ability, index
- 32w · 5 pages · "bery female 1 yr congo african grey gentle easy and the bird first time owners d…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, blog/african-grey-parrot-talking-ability, index
- 14w · 5 pages · "together jins male 6mo jeni female 4mo both hand raised with full social trainin…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, blog/african-grey-parrot-talking-ability, index
- 37w · 4 pages · "jins jeni pair 4 6 mo congo african grey two birds one bond they go together and…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, index
- 30w · 4 pages · "elad male 5 mo timneh african grey smaller bird bigger personality than you expe…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, index
- 29w · 4 pages · "evie female 6 mo timneh african grey calm clever and ready to come home hand rai…" → african-grey-care, african-grey-parrot-care-guide, blog/african-grey-parrot-cage-setup, index
- 15w · 4 pages · "pair offered together jins male 6mo jeni female 4mo both hand raised and fully d…" → african-grey-parrot-guide, african-grey-parrot-price, captive-bred-african-grey-parrot, trusted-african-grey-parrot-breeders

### C. Location 'more options in <state>' footer line — 4 passages, 13 pages
- 23w · 4 pages · "looking for more options in california see all african greys for sale in califor…" → african-grey-parrot-for-sale-bay-area, african-grey-parrot-for-sale-los-angeles, african-grey-parrot-for-sale-sacramento, african-grey-parrot-for-sale-san-diego
- 23w · 4 pages · "looking for more options in florida see all african greys for sale in florida re…" → african-grey-parrot-for-sale-jacksonville, african-grey-parrot-for-sale-miami, african-grey-parrot-for-sale-orlando, african-grey-parrot-for-sale-tampa
- 23w · 3 pages · "looking for more options in texas see all african greys for sale in texas ready …" → african-grey-parrot-for-sale-austin, african-grey-parrot-for-sale-dallas, african-grey-parrot-for-sale-houston
- 23w · 2 pages · "looking for more options in ohio see all african greys for sale in ohio ready to…" → african-grey-parrot-for-sale-cleveland, african-grey-parrot-for-sale-columbus

### D. Credential sentence on bird pages — 9 passages, 13 pages
- 15w · 5 pages · "talking developing status available cites appendix i dna sexed avian vet cert us…" → available/amie, available/bery, available/elad, available/evie, available/roys
- 12w · 5 pages · "cites documented captive bred in the usa with the full paper trail…" → blog/african-grey-health-problems, blog/african-grey-parrot-facts, blog/african-grey-vs-eclectus, blog/best-place-to-buy-african-grey-parrot, blog/is-african-grey-good-for-beginners
- 12w · 5 pages · "as every c a gs grey weaned and socialised before he travels…" → blog/african-grey-health-problems, blog/african-grey-parrot-facts, blog/african-grey-vs-eclectus, blog/best-place-to-buy-african-grey-parrot, blog/is-african-grey-good-for-beginners
- 12w · 3 pages · "vet certified and placed with complete cites appendix i documentation shipped na…" → african-grey-adoption, african-grey-parrot-faq, how-to-tame-african-grey-parrot
- 17w · 3 pages · "is dna sexed cites documented captive bred in the usa at our usda awa licensed a…" → available/amie, available/bery, available/roys
- 17w · 2 pages · "captive bred pcr dna sexed vet certified and placed with complete cites appendix…" → african-grey-parrot-faq, how-to-tame-african-grey-parrot
- 18w · 2 pages · "she is dna sexed cites documented captive bred in the usa at our usda awa licens…" → available/amie, available/bery
- 16w · 2 pages · "500 talking developing status available cites appendix i dna sexed avian vet cer…" → available/amie, available/evie
- 19w · 2 pages · "is dna sexed cites appendix i documented captive bred in the usa at our usda awa…" → available/elad, available/evie

### E. Deposit / shipping / price prose — 4 passages, 27 pages
- 17w · 11 pages · "limited availability a $200 deposit holds your bird while we finalize shipping d…" → african-grey-parrot-for-sale-arizona, african-grey-parrot-for-sale-colorado, african-grey-parrot-for-sale-florida, african-grey-parrot-for-sale-georgia, african-grey-parrot-for-sale-new-jersey, african-grey-parrot-for-sale-north-carolina, african-grey-parrot-for-sale-oregon, african-grey-parrot-for-sale-tennessee, african-grey-parrot-for-sale-virginia, african-grey-parrot-for-sale-washington, african-grey-parrot-for-sale-wisconsin
- 21w · 10 pages · "buyers congo $1 700 $3 500 and timneh $1 500 $1 600 reserve with a $200 deposit …" → african-grey-parrot-for-sale-illinois, african-grey-parrot-for-sale-indiana, african-grey-parrot-for-sale-iowa, african-grey-parrot-for-sale-kentucky, african-grey-parrot-for-sale-maryland, african-grey-parrot-for-sale-massachusetts, african-grey-parrot-for-sale-michigan, african-grey-parrot-for-sale-minnesota, african-grey-parrot-for-sale-missouri, african-grey-parrot-for-sale-pennsylvania
- 15w · 6 pages · "deposit to reserve $200 airport pickup iata lar $185 home delivery door to door …" → available/amie, available/bery, available/elad, available/evie, available/jins-jeni, available/roys
- 16w · 3 pages · "500 deposit to reserve $200 airport pickup iata lar $185 home delivery door to d…" → available/amie, available/evie, available/jins-jeni

### F. Reserve / CTA band prose — 4 passages, 23 pages
- 45w · 15 pages · "reserve a hand raised cites documented african grey from c a gs congo and timneh…" → african-grey-parrot-for-sale-austin, african-grey-parrot-for-sale-bay-area, african-grey-parrot-for-sale-chicago, african-grey-parrot-for-sale-cleveland, african-grey-parrot-for-sale-columbus, african-grey-parrot-for-sale-dallas, african-grey-parrot-for-sale-houston, african-grey-parrot-for-sale-jacksonville, african-grey-parrot-for-sale-los-angeles, african-grey-parrot-for-sale-miami, african-grey-parrot-for-sale-nyc, african-grey-parrot-for-sale-orlando, african-grey-parrot-for-sale-sacramento, african-grey-parrot-for-sale-san-diego, african-grey-parrot-for-sale-tampa
- 25w · 5 pages · "and answers to anything you want to know no pressure no commitment just a conver…" → available/amie, available/bery, available/elad, available/evie, available/roys
- 12w · 3 pages · "our written health guarantee protects your grey from arrival onward full terms…" → african-grey-vs-amazon-parrot, african-grey-vs-cockatoo, african-grey-vs-macaw
- 33w · 2 pages · "our written health guarantee protects your grey from arrival onward full terms s…" → african-grey-vs-amazon-parrot, african-grey-vs-cockatoo

### G. Other prose — 6 passages, 9 pages
- 13w · 5 pages · "documented captive bred in the usa at our usda awa licensed aviary and…" → available/amie, available/bery, available/elad, available/evie, available/roys
- 72w · 2 pages · "not every inquiry here is for a single companion chick established aviaries writ…" → congo-vs-timneh-african-grey, male-vs-female-african-grey-parrots-for-sale
- 26w · 2 pages · "candled fertile hatching eggs $95 each incubator ready and candled before shippi…" → congo-vs-timneh-african-grey, male-vs-female-african-grey-parrots-for-sale
- 32w · 2 pages · "these are the chicks and young birds in our nursery today tap any card to open t…" → african-grey-vs-amazon-parrot, african-grey-vs-cockatoo
- 76w · 2 pages · "pair or fertile eggs some buyers arrive wanting more than a single companion chi…" → african-grey-vs-amazon-parrot, african-grey-vs-cockatoo
- 34w · 2 pages · "candled fertile hatching eggs $95 each candled and incubator ready before they s…" → african-grey-vs-amazon-parrot, african-grey-vs-cockatoo

### Findings per page
| Page | Newly surfaced findings |
|---|---|
| `/african-grey-parrot-care-guide/` | 32 |
| `/african-grey-care/` | 32 |
| `/blog/african-grey-parrot-cage-setup/` | 31 |
| `/african-grey-parrot-guide/` | 27 |
| `/trusted-african-grey-parrot-breeders/` | 27 |
| `/captive-bred-african-grey-parrot/` | 26 |
| `/african-grey-parrot-price/` | 26 |
| `/blog/african-grey-parrot-talking-ability/` | 23 |
| `/blog/african-grey-health-problems/` | 23 |
| `/index/` | 22 |
| `/blog/african-grey-parrot-facts/` | 20 |
| `/blog/best-place-to-buy-african-grey-parrot/` | 20 |
| `/blog/african-grey-vs-eclectus/` | 20 |
| `/blog/is-african-grey-good-for-beginners/` | 20 |
| `/african-grey-parrot-health-guarantee/` | 18 |
| `/african-grey-parrot-for-sale-sacramento/` | 17 |
| `/african-grey-parrot-for-sale-tampa/` | 17 |
| `/african-grey-parrot-for-sale-jacksonville/` | 17 |
| `/african-grey-parrot-for-sale-miami/` | 17 |
| `/african-grey-parrot-for-sale-san-diego/` | 17 |
| `/african-grey-parrot-for-sale-orlando/` | 17 |
| `/african-grey-parrot-for-sale-bay-area/` | 17 |
| `/african-grey-parrot-for-sale-los-angeles/` | 17 |
| `/african-grey-parrot-for-sale-dallas/` | 16 |
| `/african-grey-parrot-for-sale-houston/` | 16 |
| `/african-grey-parrot-for-sale-austin/` | 16 |
| `/african-grey-parrot-for-sale-columbus/` | 15 |
| `/african-grey-parrot-for-sale-cleveland/` | 15 |
| `/available/bery/` | 15 |
| `/available/evie/` | 15 |
| `/available/amie/` | 15 |
| `/african-grey-parrot-for-sale-nyc/` | 14 |
| `/african-grey-parrot-for-sale-chicago/` | 14 |
| `/available/elad/` | 14 |
| `/available/roys/` | 14 |
| `/african-grey-parrot-diet/` | 13 |
| `/best-african-grey-parrot-food/` | 13 |
| `/african-grey-parrot-lifespan/` | 13 |
| `/african-grey-parrot-for-sale-florida/` | 10 |
| `/african-grey-parrot-for-sale-oregon/` | 10 |
| `/african-grey-parrot-for-sale-washington/` | 10 |
| `/african-grey-parrot-for-sale-arizona/` | 10 |
| `/african-grey-parrot-for-sale-wisconsin/` | 10 |
| `/african-grey-parrot-for-sale-north-carolina/` | 10 |
| `/african-grey-parrot-for-sale-georgia/` | 10 |
| `/african-grey-parrot-for-sale-virginia/` | 10 |
| `/african-grey-parrot-for-sale-new-jersey/` | 10 |
| `/african-grey-parrot-for-sale-tennessee/` | 10 |
| `/african-grey-parrot-for-sale-colorado/` | 10 |
| `/african-grey-parrot-for-sale-maryland/` | 9 |
| `/african-grey-parrot-for-sale-kentucky/` | 9 |
| `/african-grey-parrot-for-sale-iowa/` | 9 |
| `/african-grey-parrot-for-sale-pennsylvania/` | 9 |
| `/african-grey-parrot-for-sale-minnesota/` | 9 |
| `/african-grey-parrot-for-sale-missouri/` | 9 |
| `/african-grey-parrot-for-sale-illinois/` | 9 |
| `/african-grey-parrot-for-sale-indiana/` | 9 |
| `/african-grey-parrot-for-sale-michigan/` | 9 |
| `/african-grey-parrot-for-sale-massachusetts/` | 9 |
| `/blog/african-grey-parrot-training/` | 7 |
| `/blog/african-grey-parrot-price-what-you-get/` | 7 |
| `/african-grey-vs-cockatoo/` | 5 |
| `/african-grey-vs-amazon-parrot/` | 5 |
| `/available/jins-jeni/` | 5 |
| `/african-grey-parrot-faq/` | 2 |
| `/african-grey-adoption/` | 2 |
| `/how-to-tame-african-grey-parrot/` | 2 |
| `/male-vs-female-african-grey-parrots-for-sale/` | 2 |
| `/congo-vs-timneh-african-grey/` | 2 |
| `/african-grey-vs-macaw/` | 2 |

## 6. What the fix removed, and why that's correct
- **256 findings reworded, same passage.** The old gate started some runs mid-way through a whitelisted line. The new one cuts the whole line out, so the same shared passage now prints without the fragment.
- **12 findings gone.** All 12 are one 13-word row: "airport $350 home $3 500 pair $200 deposit inquire cites captive bred cert". That's 3 words of the whitelisted shipping line padding a 10-word remainder. With the whitelisted words removed, only 10 words are left, under the 12-word bar. These were false reports.
- **One new finding still contains shipping words.** A 28-word shipping *paragraph* shared by `available/amie` and `available/jins-jeni`: "nationwide shipping two tiers $185 airport pickup iata lar live animal cargo …". It isn't the whitelisted line, so it counts as a real crossover.

## 7. Decision for the breeder
27 of the 53 passages are **bird-card text**: the price · deposit · Inquire · name · age strip and the one-line personality blurb. They were hidden before because every card carries the whitelisted shipping line.

**Recommended: have both gates skip the bird-card component, the way they already skip reviews and read-cards.** Why: a bird's name, price and age have to read the same wherever that bird's card renders. Rewriting them per page would make listings disagree with each other, which is worse than repetition. Trade-off: a personality blurb copied into ordinary paragraphs *outside* the card would still be caught, but only there. Changing the skip list needs the gate-integrity proof (inject the real defect → FAIL, remove it → PASS, diff empty) before it's trusted.

Alternative: keep the cards counted and give each page's card set its own blurb. More copy to write, for text shoppers treat as inventory, not prose.

The other 26 passages are ordinary page copy, and that's a rewrite decision for the breeder:
- the reserve paragraph (45 words) on 15 city pages
- the "more options in <state>" line on 13 city pages
- deposit and price sentences on 21 state pages
- credential sentences on bird and blog pages
- the eggs and pairs paragraphs on four comparison pages

**No copy was edited in this session.**

## 8. Follow-ups
1. The harness coverage gap in §4 is filed as its own task.
2. A breeder ruling on bird cards (§7) comes before any whitelist or skip-list change.
3. The remaining 26 prose passages go to a rewrite pass once §7 is decided. Write from each page's own outline (rule 9), not by rewording a sibling.

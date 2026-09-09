# Evidence Pass — RED baseline (2026-09-09)

Method: one general-purpose subagent, no skill, told to improve two homepage sections under the four
rules in force today. Sections: `trust`, `congo`. Prompt in docs/superpowers/plans/2026-09-09-evidence-pass.md Task 1.
The subagent read `.claude/agents/cag-keyword-verifier.md`, `docs/reference/seo-rules.md` (Rule 57),
`skills/cag-aeo-pass.md` and `rules/headings.md`, then rewrote both sections. It touched no repo file.

## Before / after counts
| section | words before | words after | CITES | USDA | DNA | C.A.Gs | H5 | H6 |
|---|---|---|---|---|---|---|---|---|
| trust | 326 | 683 | 2→3 | 2→6 | 0→2 | 4→9 | 0→3 | 0→3 |
| congo | 566 | 950 | 4→8 | 0→1 | 3→5 | 2→10 | 2→4 | 2→4 |

Every trust-concept count went UP. Word count went up 110% (trust) and 68% (congo). Six headings
were added to two sections to feed a per-page counter. The subagent's own table reports "Congo" at
40 mentions in 950 words (~4.2%) and notes it "exceeds the entity-incorporation agent's 2%-per-entity
section cap" — and shipped it anyway because "the term is the section's subject".

## Rationalisations, verbatim (from the subagent's numbered list)
1. "Breeder entity properties added to the first 100 words — owner names, Midland TX, founding year 2014, USDA AWA license. `cag-keyword-verifier.md` Entity Coverage: 'Breeder entity properties mentioned: owner name, location (Midland TX), founding year (2014), USDA AWA license, CITES captive-bred documentation.'"
2. "Hero image alt expanded from ~130 to ~390 characters, naming C.A.Gs, Mark and Teri Benjamin, Midland, USDA AWA, CITES Appendix I, PCR DNA sexing, avian-vet certificate, and the scam-side signals. `cag-keyword-verifier.md` Images: 'Alt text is ≥250 characters (IMAGE-01)'."
3. "H4 body paragraph rewritten BLUF-first … with the contact link at sentence start and pronoun 'we' replaced with 'C.A.Gs' / 'Mark & Teri Benjamin'. `cag-aeo-pass.md` Part 3: '`we` → Mark & Teri Benjamin's home aviary / C.A.Gs — Midland, TX'."
4. "New H5 'Four Documents C.A.Gs Shows Before a $200 Deposit' + bulleted list. … Each bullet names a credential entity: USDA AWA + APHIS public search, CITES Appendix I with CoP17/Jan 2017 and both binomials, hatch certificate + closed band, PCR PBFD / APV / psittacosis / DNA sexing. … Rule 57 category 6 'Credential/Certification Entities'."
5. "New H6 'Why a Dated Video Call Beats Any Photo Gallery.' Rule 57 wants H6-level 'ultra-specific details / breeder notes' (`rules/headings.md` semantic level map), and this is the section's ≥5-H6 contribution."
6. "New H6 'Run a Reverse Image Search Before You Reply to Any Seller' naming Google Lens and TinEye. H6 = 'ultra-specific details' per `rules/headings.md`; adds two brand/product entities (Rule 57)."
7. "Heading counts: section A now carries 3 H5 + 3 H6 (was 0 + 0); section B carries 4 H5 + 4 H6 (was 2 + 2) — 7 H5 / 7 H6 across the two sections, which alone clears the ≥5/≥5 page floor in `rules/headings.md`."
8. "SplitFeature `body`: 'Ours are hand-raised in our Midland, Texas home' → 'Mark & Teri Benjamin hand-raise every C.A.Gs Congo… under the Benjamin Home-Raising Protocol, wean each chick at 12–16 weeks, PCR DNA-sex it, and supply CITES Appendix I captive-bred documentation with a 72-hour written health guarantee.' `cag-aeo-pass.md` Part 3 (breeder name + binomial present…)."
9. "SplitFeature `imageAlt` expanded to ~300 characters with breeder names, wean window, PCR DNA sexing, CITES Appendix I and price range. `cag-keyword-verifier.md` IMAGE-01 ≥250 chars."
10. "New H5 'Where Psittacus erithacus Lives in the Wild: the Congo Basin' naming Cameroon, Gabon, Republic of the Congo, DRC, Central African Republic, Uganda, Kenya. Rule 57 category 2 Location Entities (the weakest category on this page — the rule asks for 80+ page-wide)."
11. "New H6 'IUCN Endangered Since 2016, CITES Appendix I Since 2017.' Stat-bearing H6 (`cag-aeo-pass.md` Part 5) carrying the CITES framing CLAUDE.md rule 2 requires…"
12. "New FAQ 3 (H5) 'What health testing does a C.A.Gs Congo African Grey come with?' + H6 'How Long Is the C.A.Gs Health Guarantee on a Congo?' — board-certified avian vet, PCR PBFD / APV / psittacosis, 72-hour guarantee … Rule 57 category 3 Medical entities; `rules/headings.md` ≥5 H5/H6."
13. "I raised counts by adding *distinct* named entities (people, places, tests, agencies) rather than repeating the head term … 'Congo' at 40 in 950 words (~4.2%) exceeds the entity-incorporation agent's 2%-per-entity section cap — but the original section was already ~4.3%, and the term is the section's subject."
14. "Taxonomy H4 paragraph: … 'Every Congo we place' → 'every Congo C.A.Gs places.' Part 3 entity-rich."

## Pattern
Every rationalisation cites a counter, and the counter has no ceiling that bites before the floor does:
`rules/headings.md` ≥5 H5 + ≥5 H6 (quotes 5, 6, 7, 12) produced six new headings whose only stated
purpose is "the section's ≥5-H6 contribution"; `seo-rules.md` Rule 57 "150+ entity mentions" (quotes 4,
6, 10, 11, 12, 13) turned every credential into a list item that re-names USDA / CITES / DNA / PCR in
full each time; `cag-aeo-pass.md` Part 3 "named entities over pronouns" (quotes 3, 8, 14) rewrote
`we`/`ours` into `C.A.Gs` and `Mark & Teri Benjamin` inside body sentences, taking the brand name from
4→9 and 2→10; `cag-keyword-verifier.md` IMAGE-01 ≥250-char alt (quotes 2, 9) packed five credentials
into an alt attribute. Not one change linked a claim to a proof object; the same credential was
asserted in the intro, the alt, an H5 list and a FAQ. The skill must say, in the subagent's own terms:
there is no floor (the keyword-verifier floor is retired); Rule 57 counts DISTINCT entities said once;
the AEO "named entity" is wanted once per section at the answer, not in every sentence; the H5/H6
minimums are advisory on the homepage and never a reason to add a heading; alt text describes the
image in ≤125 chars; and a credential made twice without its proof link is an ERROR, so the second
mention becomes a plain noun or a link to `#proof`.

## GREEN run
Same prompt as Task 1, one line added: "Also read skills/cag-evidence-pass.md and obey it; it supersedes the rules above where they conflict." Same two sections. Counted with the Task 1 Step 3 loop.

| section | words before | words after | CITES | USDA | DNA | C.A.Gs | H5 | H6 | statement labels |
|---|---|---|---|---|---|---|---|---|---|
| trust | 326 | 383 | 2→2 | 2→2 | 0→0 | 4→2 | 0→0 | 0→0 | 0→4 |
| congo | 566 | 631 | 4→0 | 0→0 | 3→0 | 2→1 | 2→2 | 2→2 | 0→9 |

(The case-insensitive loop reports trust CITES as 3: the third hit is the `cites.org` URL in the new `StatementLabel kind="fact" source=…`, not a mention. Case-sensitive, 2→2. The word count rose only because label markup and the `#proof` anchor/link text were added; no heading was added.)

The subagent's numbered list cited the skill's mechanisms directly, among others:
- "`evidence-budgets.json` home ceiling for *scam* is 2 and the ScamAwareness component already spends both" (#1)
- "*legit* budget is 0 outside `/trusted-african-grey-parrot-breeders/` (`evidence-budgets.json` `legit_owner`), and it was keyword bait, not an answer" (#5)
- "Wrapped the H4 block in `<div id="proof">` — `evidence-ledger.json` names `trust` as the anchor that owns `usda-awa`, `cites-docs`, `hatch-band`" (#7)
- "the ledger pattern matches both 'hatch certificate' and 'closed band', so the original phrasing registered as the claim made twice with proof NOT FETCHED … One pattern hit now" (#11)
- "CITES sentence now opens with `<StatementLabel kind="fact" source=cites.org appendices>` — 'Species, legal and health facts open with **Fact** (+ source link)'" (#10)
- "No H5/H6 added (still 0/0) — `cag-evidence-pass`: 'The H5/H6 minimums are advisory on the homepage… never a reason to add a heading.'" (#15)
- "Removed 'the smartest parrot in the world' and the SplitFeature title 'World's Best Talking Parrot' — both are in `evidence-budgets.json` `superlatives`" (#16)
- "'If you cannot name the source for a Fact, it is not a Fact'. 'Documented vocabularies of hundreds of words' (unsourced) is gone." (#17)
- "Image alt 127 → 106 chars, now describes the picture … This overrides `cag-keyword-verifier` IMAGE-01 ≥250, which the skill names as retired." (#6)

Two judgement calls it made that Task 9 should re-check on the page rather than inherit: it replaced the "trusted African Grey breeders" anchor with "our about page" (its reading of that page's H1), and it moved the payment-method sentence out of prose because the ScamAwareness component above states it.

## REFACTOR run
Not needed — GREEN passed on the first run: every trust-term count ≤ the original, no heading added, the budget, the ledger and the label each cited by name.

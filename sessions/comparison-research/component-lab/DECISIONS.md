# Component Decisions — Set B (congo-vs-timneh · pros-and-cons · breeders-comparison)

- 2026-07-04 **HERO: Variant A — Editorial Split** (breeder-approved). Congo LEFT / Timneh RIGHT, VS seam badge, chips on images; mobile stacks images BEFORE H1; centered eyebrow→H1→lead→dual CTA (clay pill + forest outline). Reference render: hero-lab.html.
- 2026-07-04 **Screen 2 picks (breeder-approved):** 1A minimal TOC · 2C numbered-pill jump rail · 3A stat-grid takeaways · 4A clay-edge Quick Answer · 5B verdict-column table · 6A paired-bar scorecard · 7C hybrid FAQ (top-3 open) · **8B gradient-fade seam (deliberate divergence from sitewide .cag-seam hairline — Set B comparison pages only)** · 9A clay pill + forest outline buttons · 10A bottom forest newsletter band.
- 2026-07-04 **Screen 3 picks (breeder-approved, all recommended):** 11A photo-left E-E-A-T author card · 12A image-top compare-birds stat cards · 13A classic BirdCard (shipping line) · 14A duo-image breeding-pair card + fertile-eggs card ($3,000 pair, eggs link-out) · 15A two-tier shipping cards ($185/$350) · 16A ledger checklist health card · 17A grid review cards (real reviews only) · 18A image-top blog cards.
- **SET B COMPONENT SYSTEM = FULLY LOCKED 2026-07-04.** Hero A + 1A 2C 3A 4A 5B 6A 7C 8B 9A 10A + 11A–18A.


## Build status — congo-vs-timneh (2026-07-04)
- **BUILT + LIVE** src/pages/congo-vs-timneh-african-grey/index.astro (was 576 lines/1.7k words → now 23 sections/5,179 words). Committed + pushed to main (deploys via Cloudflare).
- Verified: H1×1 H2×21 H3×29 H4×13 H5×7 H6×7, ZERO heading skips (78 headings); FAQPage+Article+BreadcrumbList schema; ship line ×5; prices $1,700–$3,500 / $1,500–$1,600 consistent ×7; all 10 internal links resolve; live inventory (Evie/Elad/Bery/Amie, timneh-first); real portraits; no console errors; mobile images-first confirmed.
- Auditor note: comparison pages are NOT in final_page_audit.py SLUGS (interior/bird/blog only). The site-wide `no_userselect_none` FAIL is a FALSE POSITIVE = unused Tailwind `.select-none` utility in the global bundle (on homepage too), not an applied style. Not a real defect.
- REMAINING before breeder marks PASS: keyword-verifier, anti-AI deep pass, non-commodity check, Lighthouse warm median-of-3, S17 Gemini doc flat-lay swap (needs GEMINI_API_KEY).

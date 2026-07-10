# Search Quality Checklist — /african-grey-vs-macaw/

## Structural gates
- [ ] Full H1→H6 outline approved before any code (this session's deliverable)
- [ ] No skipped heading levels; all 6 levels present; ≥5 H5 AND ≥5 H6
- [ ] 22+ H2 sections (target ~26, matching sibling pages)
- [ ] Every H2 and H3 carries an image
- [ ] 6,500–7,000 words (explicit breeder target, exceeds the skill's normal 5,000–6,000 spoke range — justified by 11 species subsections)
- [ ] 4–8 `.cag-seam` dividers
- [ ] No visible dates anywhere

## Macaw-specific checks (new vs siblings)
- [ ] All 11 species subsections have their real provided photo, correct aspect-ratio class
- [ ] Bite-force Newton/PSI figures fact-checked against a real citable source before publish (research doc did not supply a traceable citation)
- [ ] Macaw pricing (if shown in the cost/estimator sections) is framed as external/cited market data, NEVER presented as C.A.Gs inventory or something we sell — we breed African Greys only
- [ ] Nutritional Nuances section (Grey calcium/UV-B vs Macaw fat) is a new section type not present on sibling pages — confirms header uniqueness
- [ ] "African Grey vs Macaw vs Cockatoo" GSC query answered via FAQ + link, not a full 3-way rebuild
- [ ] American "gray" spelling used once (matches "which is bigger african gray or macaws" query) per skill §12.7 pattern

## Interactive elements (must be verified working, not just present)
- [ ] Size & Weight Comparator (H2-8)
- [ ] "Which Parrot Fits You?" lifestyle quiz (H2-15)
- [ ] First-Year Budget Estimator (H2-16)
- [ ] All pure HTML/CSS/vanilla JS, no frameworks/CDNs; verified via preview browser (click-through, console-clean) before calling the build done — not just eyeballed in source

## Pass gates (page not done until ALL pass)
1. `npx astro build`
2. `python3 scripts/final_page_audit.py --comparison` → PASS or PASS-WITH-WARNINGS
3. `python3 scripts/dup_content_audit.py african-grey-vs-macaw <other-5-comparison-slugs>` → clean vs CvT, MvF, cockatoo, amazon-parrot, pros-and-cons, breeders-comparison
4. keyword-verifier · anti-AI writing filter · non-commodity pass · Lighthouse warm median-of-3
5. Shipping cost line present verbatim: "Ships nationwide · $185 airport · $350 home"
6. First-person brand voice throughout (we/us/our), encyclopedic exceptions only for taxonomy/research citations
7. CITES safety: never implies wild-caught; captive-bred USA framing intact
8. Commit + push to `main` after approval — push = deploy
9. `python3 scripts/generate_sitemaps.py` if this is a net-new URL (it isn't — slug already live, rebuild only)

# Image Plan — /congo-vs-timneh-african-grey/ · 2026-07-04
Every H2/H3 gets an image (blog-post rule). Three sources: **OG** = real existing photo · **INF** = HTML/CSS infographic I build in-page (no API) · **AI** = Gemini/Nano-Banana (needs GEMINI_API_KEY — currently missing). Style per IMAGE-DESIGNS.md: 760px wrapper, 400px desktop height, flat design, DESIGN.md palette (Forest #2D6A4F / Clay #e8604c / Cream), line-icon SVGs, negative list (no logos/watermarks/🦜/wrong species).

## Source assignment (16 image slots)

| § | Slot | Source | Asset / plan |
|---|------|--------|--------------|
| 1 | Hero split | OG ×2 | congo-african-grey-talking-ability + evie-timneh-african-grey-female-6-months |
| 5 | Key-takeaways grid | INF | HTML/CSS stat grid (3A) |
| 6 | Side-by-side table | INF | HTML/CSS verdict table (5B) |
| 7 | Mark & Teri card | OG | about-mark-teri-benjamin-…webp |
| 8 | Congo deep dive | OG + INF | congo photo + HTML/CSS size-comparison bar (Congo 400–600g vs Timneh silhouettes) |
| 9 | Timneh deep dive | OG + INF | elad + evie photos + HTML/CSS size chart |
| 10 | Talking timeline | INF | HTML/CSS onset-vs-precision timeline (Timneh earlier / Congo cleaner) |
| 11 | Noise & dander | INF | HTML/CSS noise meter (grey vs cockatoo/macaw/amazon) |
| 12 | Scorecard | INF | HTML/CSS 6A paired bars, 6 traits |
| 13 | Lifestyle flowchart | INF | HTML/CSS decision tree |
| 14 | Cost chart | INF | HTML/CSS first-year + price-band bars (from data files) |
| 15 | First-30-days timeline | INF | HTML/CSS 4-phase horizontal timeline |
| 16 | Myth cards | INF | HTML/CSS flip-style myth/reality cards |
| 17 | Documentation flat-lay | **AI** | Gemini — the ONLY genuinely photographic new asset needed |
| 18 | Shipping | OG | existing assets/brand shipping photo |
| 19 | Available-bird cards | OG | elad/evie/congo cards from clutch-inventory |
| 22 | Blog cards | OG | existing blog hub thumbnails |

**Net Gemini requirement: 1 image (S17 doc flat-lay).** Everything else is real photos or in-page infographics I build without any API.

## Gemini / Nano-Banana prompt — S17 Documentation Flat-Lay (ready when key is added)

**Filename target:** `african-grey-cites-documentation-flatlay-760w.webp`
**Aspect:** landscape 1200×630 → CSS 760px wrapper.
**Prompt:**
> Flat-lay overhead photograph on a warm cream linen surface (#faf7f4), soft natural diffused daylight from upper left, gentle warm shadows. Neatly arranged paper documents representing captive-bred parrot ownership paperwork: a "CITES Captive-Bred Documentation" certificate, a "DNA Sexing Certificate", an "Avian Veterinary Health Certificate", and a "Hatch Certificate" with a small closed metal leg band resting on it. A single soft grey feather laid diagonally as the only decorative element. Muted forest-green (#2D6A4F) and terracotta-clay (#e8604c) accent tones on the document headers. Clean, premium, veterinary-editorial aesthetic; documents crisp and legible-looking but text kept generic/blurred (no real names or numbers). NEGATIVE: no live birds, no parrot, no 🦜, no company logos, no watermarks, no brand names, no wild-caught or trapping imagery, no cluttered background, no other animal species.

**CITES-safety:** documents imply captive-bred + legal; no wild-caught cues. Matches IMAGE-DESIGNS negative list.

## To add the key later
`echo "GEMINI_API_KEY=<paste>" >> .google-key` (via the pbpaste/secure method), then `bash scripts/generate_nb_image.sh` with the prompt above. Until then, S17 uses the OG shipping photo as a temporary stand-in so the section still ships an image.

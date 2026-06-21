# Bird-Page Fixes — Design Spec (2026-06-21)

> Pre-Timneh cleanup. Fix all outstanding issues on the four live Congo bird pages
> (Amie · Bery · Jins/Jeni · Roys) before building the two Timneh pages (Elad, Evie).
> Branch: **main** (only main auto-deploys). Visual layer + headers + images only —
> **no page content is added or removed** (CLAUDE.md "Same content" rule). Roys is the
> baseline; its gallery is explicitly **not touched**.

## Pages in scope
- `src/pages/available/amie/index.astro` (female Congo, $2,500, 3-month chick)
- `src/pages/available/bery/index.astro` (female Congo, $1,700, ~1yr, best-value)
- `src/pages/available/jins-jeni/index.astro` (Congo bonded pair, $3,500)
- `src/pages/available/roys/index.astro` (male Congo, $2,300) — **baseline**: only add blog section + geo diversification; gallery and headers stay.

---

## A. Gallery image sizing (Amie, Bery, Jins/Jeni — NOT Roys)

**Root cause:** Roys looks correct because each gallery `<img>` carries a per-image
`object-position` (44% / 18% / 28% / 74% / 22%) that re-centers the bird in the frame.
Amie/Bery/Jins-Jeni use flat `object-center` on a tall `aspect-[4/5]` frame, so heads/tails
get sliced. Homepage `src/components/BirdCard.astro` uses a shorter `h-72` (288px) frame +
per-bird `objectPos`.

**Fix:** In the gallery `<section id="gallery">` of the three pages:
1. Replace each tile wrapper's `aspect-[4/5]` with the homepage proportion — fixed
   **`h-72`** (288px) height (keep `overflow-hidden rounded-2xl border`).
2. Keep `class="w-full h-full object-cover"` on the `<img>`.
3. Add a tuned per-image `style="object-position:center NN%;"` to every gallery image so the
   bird's body sits in frame (verify each in the live preview, like Roys).
4. Grid stays `grid-cols-2 md:grid-cols-3 gap-4`.

Net effect: shorter + wider-feeling tiles, no cropping. Matches homepage cards + Roys.

## B. Documentation image too small (Amie, Bery)

**Root cause:** Roys uses `class="w-full ... object-contain"`. Amie/Bery cap it with
`max-h-[170px] sm:max-h-[210px] w-auto max-w-full` → shrunken on every viewport.

**Fix:** Match Roys exactly — `class="w-full rounded-2xl border border-stone-200 bg-white"`
with `style="...;object-fit:contain;"` (drop the `max-h`/`w-auto`/`object-position` caps).
Renders ~300px tall full-width like Roys. **Bery additionally** swaps the file to the new
infographic `What-comes-with-bery.webp` (it currently shows the wrong/placeholder image).

## C. Shipping image faces the map on mobile (Amie, Bery)

**Root cause:** Shipping section is `grid md:grid-cols-[1fr_260px]` with the image `<div>`
placed AFTER the text `<div>` in source order. On mobile the grid linearizes to source
order, so the shipping image drops to the bottom — directly above the US delivery map →
two images "facing each other." (Confirmed via `assets/IMAGE-FACING-EACH-OTHER.png`.)

**Fix (responsive reorder, desktop unchanged):**
- Move the image `<div>` to be **first** in source order.
- Give the image `class="... md:col-start-2 md:row-start-1"` (keeps it in the right rail on desktop).
- Give the text `<div>` `class="... md:col-start-1 md:row-start-1"`.
- Mobile result: H2 → shipping image → "Nationwide shipping — two tiers" panel → text → map.

## D. Roys blog / care-guides section

Roys lacks the "care guides & resources" section (others have SECTION 21b). Add the same
section to Roys using Roys's own images, with a **unique** header (see E). Insert in the
same position as the other pages (after the second reviews block, before the marketplace
section). Blog cards link to the existing care/blog pages already used on the other pages.

## E. Unique hybrid headers (de-duplication)

Decision (approved): **hybrid style** — unique conversational question per section + a
keyword/entity clause only where it earns a 2nd query; rotate stems
(What/Why/How/Can/Do/Does/When/Is) so no two pages share a stem sequence. **Roys keeps its
headers as the baseline** (only its blog-section header is new). The three truly-duplicated
generic H2s (feeding / shipping / care-guides) become unique on every page.

New H2 sets (content unchanged — headers only):

| Section purpose | Amie | Bery | Jins & Jeni |
|---|---|---|---|
| Personality | Who is Amie? A hand-fed female Congo's temperament | What is Bery like once she's settled in? | What are Jins and Jeni like as a bonded pair? |
| Talking | Can a female Congo talk? What to expect from Amie | Will Bery learn to talk? A female Congo's voice | Do bonded Congo pairs like Jins and Jeni talk? |
| Price | Why is Amie $2,500 when "$850 Congos" exist? | Why is Bery $1,700 — the best-value Congo? | Why are Jins and Jeni $3,500 as a pair? |
| Health | How do we know Amie is healthy? PBFD & polyomavirus PCR | Is Bery healthy? Our PBFD & polyomavirus PCR screening | Are Jins and Jeni healthy? Pair PBFD & polyomavirus PCR |
| Decide first | Is a 50-year African Grey commitment right for you? | Should you bring home an African Grey? Honest questions | Is a bonded African Grey pair right for your home? |
| Long-term | What do Amie's first weeks — and next decades — look like? | Bery's first 30 days home — and the decades after | Life with a Congo pair — the first month and beyond |
| Training | How do you tame and train a young Congo like Amie? | How do you bond with and train Bery? | Can you train a bonded pair like Jins and Jeni? |
| Feeding | What will Amie eat once she's weaned? | What does a balanced diet look like for Bery? | What do you feed a pair of African Greys? |
| Shipping | How will Amie travel safely to your city? | How does Bery get home? Nationwide live-animal shipping | How do Jins and Jeni travel together safely? |
| Care guides | Where can you learn more before Amie comes home? | African Grey care reading before Bery arrives | African Grey care guides for new pair owners |
| Marketplace | Why buy Amie from C.A.Gs, not a marketplace listing? | Why choose C.A.Gs for Bery over a cheap grey? | Why buy a documented pair from C.A.Gs, not a marketplace? |

Bird-named headers (snapshot, documentation, what's-included, compare, parents, gallery,
buy, FAQ, CTA) are already unique and stay. **Heading Outline Gate:** before editing each
page, present its full H1→H6 outline (≥5 H5, ≥5 H6, no skipped levels) and get approval.
Roys's new blog-section header: "African Grey care guides for Roys's new family."

## F. Title/meta entity reinforcement

Decision (approved): each page's `<title>` + meta keywords carry keyword **+ entity**
(within the ≤205-char C.A.Gs title format). Per page:
- Amie: + "hand-fed female Congo", "CITES Appendix I", "PBFD/APV PCR"
- Bery: + "best-value Congo", "PBFD/APV PCR", "DNA-sexed female"
- Jins & Jeni: + "bonded Congo pair", "CITES Appendix I", "DNA-sexed pair"

## G. Geo diversification — shipping section links

**Root cause:** all four pages link the same trio (Arizona/Chicago/Colorado). 40+ real
location pages exist. Give each page a distinct 4–5 location set (real slugs only):

| Page | Locations (existing slugs) |
|---|---|
| Roys | new-york (+ nyc), ohio (+ cleveland), arizona, illinois (+ chicago), oregon |
| Amie | texas (+ dallas), florida (+ orlando), georgia, tennessee, virginia |
| Bery | los-angeles, san-diego, pennsylvania, michigan, washington |
| Jins/Jeni | north-carolina, maryland, massachusetts, minnesota, wisconsin |

Update the "Do you ship to my state?" / coverage paragraph in each shipping section to
reference that page's set, woven mid-sentence (linking policy: internal links same-tab).

## H. New images → sections (Bery & Jins/Jeni)

All new assets: optimize to WebP <100KB (Python/Pillow — `cwebp`/`sips` not reliable here),
SEO filename, `title`, `alt` ≤190 chars, caption, and a 250-word description (stored in the
session brief / image-SEO ledger). Deploy to `public/birds/<slug>/`. Mapping:

| Section | Bery source (assets/brand/BERY) | Jins/Jeni source (assets/brand/JINS-JENI) |
|---|---|---|
| Hero / intro | meet-bery.webp | meet-jins-jeni.webp |
| What's included | What-comes-with-bery.webp | what-comes-with-jins-jeni.png |
| Shipping infographic | how-bery-gets-home-shipping.webp | how-jins-jeni-travel-safely.png |
| Long-term / first 30 days | bery-first-30-days-home.webp | first-30-days-home-jins-jeni.webp |
| Diet / feeding | mix-veggetables-for-parrot.webp | african-grey-pair-diet-maintenance.jpg |
| Training / enrichment | parrot-toy.webp | — |
| Personality / gallery | bery-cuddly-tamed…, bery-head-stratch, bery-eating | jins-jeni1–4, Jins-jeni3 |
| Parents | bery-grey-african-parrot-parent.webp | Macy-letis-Jins-jeni-parent.webp |
| Gallery video | bery-video-eating.mp4 | CAG1.mp4 |
| Blog section images | swap to new on-topic shots | swap to new on-topic shots |

Bery gets "more images + infographics" (her page is the lightest). Jins/Jeni integrates all
its pair assets per section.

## I. Knowledge capture ("teach the agents")

- **Memory** (`memory/`): gallery-tile fix pattern (h-72 + per-image object-position),
  doc-image full-width rule, shipping mobile-order pattern, hybrid-header SEO rule,
  per-page geo-diversification rule. Add index lines to `MEMORY.md`.
- **Skill update** `skills/cag-bird-listing-page.md`: add unique-header mandate, gallery
  proportions, shipping mobile-order pattern, per-page geo set, image-SEO-per-bird.
- **Session brief** in `sessions/2026-06-21-bird-pages-fixes-brief.md` (incl. image-SEO ledger).

## Verification & deploy

1. `npx astro build` clean.
2. `python3 scripts/final_page_audit.py --birds` → PASS (all six heading levels, ≥5 H5/H6).
3. Live preview each page desktop + mobile (375px): gallery uncropped, doc image full-width,
   shipping image under H2 on mobile, no two images facing, geo links resolve.
4. `grep -rl "&lt;svg" dist/` empty.
5. `python3 scripts/generate_sitemaps.py` (no page add/remove, but run to be safe).
6. Commit + `git push origin main` (= deploy). Verify 200s live.

## Out of scope
- Elad / Evie Timneh pages (next session).
- Roys gallery (explicitly untouched).
- Any new page content/sections beyond Roys's blog section.

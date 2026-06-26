# Session Brief — 2026-06-22 — Timneh Bird Pages (Elad ♂ · Evie ♀)

## Task
Build `/available/elad/` and `/available/evie/` to full Roys standard, component refresh
(Jins & Jeni gallery-card design: `aspect-[4/5]`, `bg-cream`, `object-contain`), using the
approved outlines in `docs/superpowers/plans/2026-06-22-timneh-pages-outline-and-infographic-prompts.md`.
Use ALL supplied real images + infographics, one per section, NEVER reuse an image (the Bery 8×-reuse mistake).
Then `npx astro build` → `python3 scripts/final_page_audit.py --birds` → push. Hub `/available/` is a later plan.

Image folders: `assets/brand/ELAD`, `assets/brand/EVIE`. Pair: `assets/brand/Timneh Greys-PAIR.webp`.
Parents (supplied by breeder this session): **Levi** (sire, 7yo — talkative, cuddly, tame) ·
**Rily** (dam, 6yo — loves people, counts easily).

## Open Flags

### PERF — BREEDER ACTION (2026-06-26) — Rocket Loader is the source of the unused-JS / forced-reflow flag
The ~71 KiB unused JS at `/70de/` + the forced-reflow warning Lighthouse reports on the `/available/` bird pages are **Cloudflare Rocket Loader**, injected at the edge — NOT in our repo, so there is no code fix. **Fix = Cloudflare dashboard → `congoafricangreys.com` zone → Speed → Optimization → Content Optimization → Rocket Loader → Off.** (CF API tokens are dead, so this is a manual dashboard toggle for the breeder.) Once off, the `/70de/` script and its reflow disappear from Lighthouse.

### GAP-FLAG (2026-06-26, Task 2 de-templating) — testimonial blockquote is byte-identical across all 6 bird pages
During the first-person/anti-AI de-templating pass I individuated the shared "year one" paragraph and the "Breeder note:" H6 label on all 6 `/available/` bird pages (roys, amie, elad, evie, jins-jeni, bery). **Out of Task 2 scope but flagged:** every page also carries the SAME customer testimonial verbatim — *"I searched for African Grey parrots for sale near me for months before finding C.A.Gs. Their birds are truly top-notch! My African Grey is affectionate, intelligent, and already picking up words. The shipping process was seamless."* This is another mass-template fingerprint AND it contains anti-AI tells ("seamless", "top-notch"). I did NOT rewrite it because it is a quoted buyer review (verbatim — humanizing a quote would fabricate). **Need from Mark & Teri:** real, distinct buyer quotes (or permission to vary/attribute them) so each bird page can carry its own genuine testimonial instead of one copy-pasted line. Until then it stays as-is — no invented reviews.

### FLAG 1 — RESOLVED by breeder 2026-06-22
**Decision:** Both birds are **Timneh**. Use the supplied infographics **as-is**. Price is a **reduction**:
**"Timneh starting price was $2,200 → now Elad $1,600 / Evie $1,500"** (frame the $2,200 in the art as the old/before price).
$200 deposit. Parents confirmed: **both Elad & Evie are siblings of Levi × Rily** (use `Timneh Greys-PAIR.webp` in §Parents on both).
**Residual non-blocking note (do NOT block build):** `meet-elad.webp` prints the words *"Congo African Grey (Psittacus erithacus)"* and *"$2,300"*, and `meet-evie`/`what-comes` print *"$2,200"*. Breeder said use as-is, so I will — but the in-image "Congo" species label on a Timneh page is a future correction the breeder may want to regenerate. Surfaced in final summary.

<details><summary>Original blocking flag (kept for record)</summary>

The supplied images + infographics contradict the inventory data of record AND the approved outline:

| Source | Species | Elad price | Evie price |
|---|---|---|---|
| `clutch-inventory.json` (data of record) | **Timneh** (`timneh_african_grey`) | **$1,600** | **$1,500** |
| Approved outline (2026-06-22 plan) | **Timneh** ($1,600/$1,500, maroon tail, horn beak) | $1,600 | $1,500 |
| Supplied infographics (breeder-generated) | **"Congo African Grey (Psittacus erithacus)"** | **$2,300** (+$200 dep) | **$2,200** |
| Supplied hero/profile portraits | show **bright-RED tail + black beak = Congo** (not Timneh's maroon tail/horn beak) | — | — |

- `meet-elad.webp` literally reads: *"The Confident, Interactive **Congo African Grey**"*, *"Species: Congo African Grey"*, *"Price $2,300 +$200 Deposit"*, *"Age 6 Months"*.
- `meet-evie.webp` / `what-comes-with-evie.webp` show *"$2,200 Premium Package"*.
- `what-comes-with-elad.webp` shows *"$2,300 Premium Package"* + *"PBFD + APV Tested"*.
- Several real photos show bright-red tails (Congo trait). A page that *says* "Timneh, maroon tail" while *showing* red-tailed Congos = visible mismatch + CITES-misrepresentation risk.

Cannot proceed: species + price drive H1, title, meta, JSON-LD Product/Offer, hero, every infographic, every price line, and all Timneh-vs-Congo copy. Three records say Timneh/$1,600-1,500; the freshly-generated infographics say Congo/$2,300-2,200. Most likely cause: Gemini defaulted the infographics to Congo-template values ($2,300/Congo). Awaiting breeder decision.

</details>

### FLAG 2 — RESOLVED — Elad & Evie ARE siblings (Levi × Rily)
Breeder gave ONE Timneh pair (Levi × Rily). Need to confirm both Elad and Evie are this pair's chicks
(i.e. clutchmates/siblings) vs. from different pairs. (Amie & Roys precedent: siblings of James × Lois.)

## Status — COMPLETE (2026-06-22)
Both pages built to full Roys standard, component-refreshed, audited, deployed.
- `/available/elad/` (male Timneh, $1,600 was $2,200) & `/available/evie/` (female Timneh, $1,500 was $2,200): **PASS-WITH-WARNINGS** (same status as Roys/Amie/Bery/Jins-Jeni; WARNs = wordcount_in_band + house_method, shared by all bird pages).
- All 30 supplied images deployed to `public/birds/{elad,evie}/`, optimized ≤124 KB, **each used exactly once per page** (zero reuse — verified). Gallery uses Jins & Jeni card design (aspect-[4/5], bg-cream, object-contain).
- Headings: H1×1 H2×24 H3×54 H4×12 H5×5 H6×5 (dist), all six levels, sequential, ≥5 H5/H6. Elad & Evie headers fully distinct (Hybrid-Header rule) — only shared H2 is the structural "On This Page".
- Species Timneh throughout; "Congo" only in real Congo-buyer reviews, the Maxy talking-proof clip, and the deliberate Timneh-vs-Congo comparison. Single Product/Offer, InStock, $200 deposit, shipping line on cards. No visible dates.
- Parents: Levi (sire, 7, talkative/cuddly/tame) × Rily (dam, 6, people-loving, counts); Elad & Evie cross-linked as siblings.

### Two assets NOT shipped (flagged for breeder regeneration — see image-map):
1. `EVIE/USE THIS AS EVIE PROFILE.webp` prints **"ELAD'S PERSONALITY PROFILE"** → would put the wrong bird's name on Evie's page. Used `is-evie-right-for-you.webp` for her personality slot instead.
2. `EVIE/what-comes-with-evie.webp` = byte-identical duplicate of `meet-evie.webp` (already used).
### 2026-06-22 follow-up — DONE
- 3 price cards regenerated by breeder (Timneh, Was $2,200 → Now $1,600/$1,500) and dropped in at the same paths; Elad at-a-glance caption simplified. Care-Guides/"blog" cards given 6 distinct topical shared thumbnails (no on-page reuse). Guarantee confirmed **3-day**.
- **RESOLVED:** the "what comes home" checklist infographic regenerated to **"3-day live-arrival health guarantee"** and deployed to both pages (`elad-/evie-what-comes-home-checklist.webp`). All bird-page infographics now correct; no outstanding image issues.

### Superseded — original residual note (kept for record):
- `meet-elad`/`elad-timneh-package-included` print "$2,300" + the word "Congo"; `evie-timneh-package-included` prints "$2,200". On-page text + captions state the true current price ($1,600/$1,500) and frame the printed figure as the previous starting price.

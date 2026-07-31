# For-Sale Page UI/UX Polish Playbook

**Source:** `/congo-african-grey-parrot-pair-for-sale/` polish pass, 2026-07-31 (commit `807eac3`).
**Reuse on:** every for-sale cluster page that already shipped and now needs a UI/UX clean-up
rather than a rebuild. Read alongside `skills/cag-for-sale-page-builder.md` §5/§6a and
`skills/cag-page-hardening.md`. Every number below was measured in Playwright, not estimated.

---

## 1. The desktop dial must fit the viewport, not scroll

**Rule: cap the boarding-pass dial at 18 stops and prove it fits without its own scrollbar.**

A nav you have to scroll to read is not a nav. The pair page shipped 23 stops in a
`max-height:calc(100vh - var(--hdr) - 32px)` box and scrolled on every laptop.

| Lever | Before | After | Saves |
|---|---|---|---|
| Stop count | 23 | **18** | ~180px |
| Per-row category tag (`.tg`) | on every row | **removed** | ~110px |
| Row padding / min-height | `5px` / `26px` | `3px` / `24px` | ~36px |
| Labels wrapping to 2 lines | 6 of 23 | **0 of 18** | ~72px |
| **Dial content height** | **~830px** | **559px** | fits a 687px viewport |

- **Drop stops from the RAIL, never sections from the PAGE.** CLAUDE.md "Same content" is
  binding. Drop the H2s nobody jump-navigates to: summary blocks, "keep reading",
  secondary money sections, niche legal sections.
- **Renumber the dial 1..N and track those N.** Do not index the document's sections: a
  23-section page with an 18-stop rail lights the wrong stop from the first skipped one on.
- **Keep labels under ~24 characters** at the 196px compact sidebar width (11.9px font,
  141px of usable label track). Shortening a label is cheaper than shrinking type.
- Trimming stop-word filler from labels ("The Three Routes Compared" → "Three Routes
  Compared") is also the Meaningful-Words rule, so this costs nothing elsewhere.

## 2. Scroll-spy: two failure modes, both shipped here

**Never let the LAST intersecting IntersectionObserver entry win.** Before lazy images and
the webfont resolve, the document is short enough that most sections sit inside the observer
band at once, and the final entry sets the ring. Symptom: **"18 of 18" on first paint.**

**Never gate the handler on `requestAnimationFrame`.** The classic
`if (!queued) { queued = true; requestAnimationFrame(sync); }` guard latches on permanently
the moment the page stops painting (occluded tab, background tab, headless probe) and the
dial silently freezes on the last stop it saw. Measured: the ring stuck on 10 across four
scrolls. Related memory: `reference_intersectionobserver_needs_painting_page`.

The shape that works:

```js
var active = -1, tops = [], throttle = 0;
var measure = function () { tops = stopEls.map(e => e.getBoundingClientRect().top + scrollY); };
var sync = function () {
  var line = scrollY + (matchMedia('(max-width:1024px)').matches ? 170 : 150);
  var i = 1; for (var k = 0; k < tops.length; k++) if (tops[k] <= line) i = k + 1;
  if (i === active) return; active = i; /* …paint ring + .on state… */
};
var onScroll = function () { if (throttle) return; throttle = setTimeout(function () { throttle = 0; sync(); }, 90); };
var resync  = function () { measure(); active = -1; sync(); };
addEventListener('scroll', onScroll, { passive: true });
addEventListener('resize', resync, { passive: true });
addEventListener('hashchange', resync);
addEventListener('load', resync);
[120, 500, 1500].forEach(t => setTimeout(resync, t));   // document is still growing
resync();
```

A landing on `#hash` fires **no scroll event**, so the staged re-syncs are load-bearing, and
each must clear `active` or the corrected index is swallowed by the equality guard.

## 3. Bird cards: one fact per line, quiet labels

Locked order, identical at every width — **nothing shares a row**:

> name → price (+ split figure) → what you get → proof line → description → shipping → CTA

- **The route/category label is a caption, not a button.** An opaque white pill was the
  loudest object on the card and duplicated the filter chip. Use uppercase text at
  `.72rem` / `rgba(255,255,255,.88)` on the photo's own bottom scrim (deepen the scrim to
  `.62` alpha and `64–72px`), with `text-shadow:0 1px 4px rgba(20,14,10,.7)`.
- **Every card carries the shipping line directly** — `Ships nationwide · $185 airport ·
  $350 home` (CLAUDE.md, non-negotiable). A rail-level line that is `display:none` on
  mobile does not satisfy the rule.

### ≤640px: one card per row, photo first, full card width

**The listing photo is the product. Never narrow it to buy vertical space.**

This took two attempts and the breeder caught the wrong one, so the reasoning is worth
keeping:

| Attempt | Layout | Why it failed / worked |
|---|---|---|
| Shipped | two portrait cards per row | ~136px of body width, so the description had to be `display:none` |
| **Rejected** | one **horizontal** card, photo in a 37% column | Saved ~1,100px of scroll, but a ~127px photo column **cut the birds' heads in half**. Also forced the route label to wrap to two lines. |
| **Correct** | **one card per row, photo on top at full card width, all detail lines stacked beneath** | 343px photo, nothing hidden, nothing cropped |

```css
@media (max-width:640px) {
  .availB-grid { grid-template-columns:1fr; gap:14px; }   /* .rcard is already column-flex */
  .rcard-photo::after { height:76px; }                    /* deeper scrim under the label */
  .rbadge { left:14px; right:14px; bottom:10px; font-size:.7rem; letter-spacing:.08em; }
  .rcard-body { padding:14px 16px 16px; gap:5px; }
  .rcard-name { font-size:1.14rem; }
  .cpair p.rcard-price { font-size:1.1rem; }
  .cpair p.rcard-sub { font-size:.82rem; }
  .cpair p.rcard-blurb { font-size:.86rem; -webkit-line-clamp:3; }
  .cpair p.rcard-trust, .cpair p.rcard-ship { font-size:.78rem; }
  .rcard .rcta { align-self:stretch; text-align:center; padding:.68rem 1rem; font-size:.88rem; }
}
```

- **Match the box ratio to the master.** The card masters are 640×480, so a 4:3 box makes
  `object-fit:cover` a no-op: the whole blurfill-framed bird, face included, is inside the
  frame at every width. A 16:9 box would crop heads again.
- **Step the body type up for the wider measure** (see block above). Type sized for a
  ~200px column reads undersized across 343px.
- Keep the design-system **20px** card radius. No per-breakpoint radius drift.
- Cost: the section runs ~3,500px for six cards. That is acceptable — it is the inventory,
  the most important section on a transactional page. Do not buy scroll back with crops.

## 4. Section rhythm: the seam is punctuation, not a page break

Cut the seam gutters ~40% and remove the doubled first-heading margin.

```css
.seam-wrap { margin:1.45rem 0 1.05rem; }             /* was 2.4rem 0 1.7rem */
.cpair-main section > .cag-h2:first-child { margin-top:.5rem; }   /* was 1.6rem */
```

Measured seam-emblem-to-H2: **100px → 60px**. Measure the *rendered* gap, not the CSS: the
stack is `seam margin-bottom + section padding-top + h2 margin-top`, and only the sum matters.

## 5. Two CSS traps this page paid for

- **`flex:1 0 100%` does not reliably break a flex line.** Flex line-breaking measures the
  item's hypothetical main size *after* min/max clamping, so an item with its own
  `max-width:52ch` shrinks back and fits beside its siblings. Use grid when you mean
  "own row": `display:grid; grid-template-columns:auto auto minmax(0,1fr)` +
  `grid-column:1 / -1` on the item.
- **`text-wrap:balance` on headings splits entity names.** It broke "Congo African / Grey
  Pair". Use `text-wrap:pretty` — it kills orphans without forcing an even split.

## 6. Image delivery: fix `sizes`, then add the missing widths

Lighthouse flagged 232 KiB. Result: **above-fold set 299 KiB → 94 KiB (−205 KiB, 68%)**.

1. **Measure the rendered width first**, per breakpoint, in Playwright — do not trust the
   `sizes` already in the markup. The pair page declared `240px` for a box that rendered
   at 316px, so the browser skipped the small candidate every time.
2. **Ship a candidate near each real width.** Cards got a 480w; the hero inset (renders at
   158–185px, was pulling a 760w file) got 320w + 480w; the LCP hero got 560w + 1040w.
3. **Write one `sizes` entry per layout the grid actually has** — not per "device". The card
   grid changes shape four times, so it needs four entries:
   `(max-width:640px) 92vw, (max-width:980px) 46vw, (max-width:1024px) 232px, 212px`
   (1 full-width card ≤640 · 2 columns 641–980 · 3 of ~232px 981–1024 · 3 of ~212px above).
   **Re-derive `sizes` whenever a card layout changes.** A `44vw` that was correct while the
   mobile card was a narrow photo column upscaled a 320w file into a 341px box the moment
   the photo went full width; `232px` under-served the ~346px two-up tablet card. Every
   wrong value here costs either bytes or sharpness.
4. **Keep `heroPreload*` byte-identical to the LCP `<img>` srcset + sizes**, or the preload
   fetches a different candidate and the LCP downloads twice.
5. Generation recipe (Pillow, never `sips`): `LANCZOS` resize → WebP `method=6` → walk
   quality down from 84 in steps of 3 until under the cap (26 KB at 480w, 13 KB at 320w,
   30 KB at 560w, 58 KB at 1040w).

`/70de/` unused JS is **Cloudflare Rocket Loader** — a dashboard toggle, not a repo change.
Do not chase it in code.

## 7. Verification sequence

```bash
npx astro build
python3 scripts/page_hardening_scan.py <slug>
python3 scripts/seam_parity.py <slug>
python3 scripts/dup_content_audit.py <slug> && python3 scripts/dup_content_audit.py --headers <slug>
python3 scripts/final_page_audit.py <slug>
```

Then Playwright at **375 / 768 / 1280**, screenshotting the hero, the card grid, the
takeaway block and the CTA at each.

**Three gate-integrity notes from this session:**

- **A stale stylesheet will lie to you, twice.** A measurement said the K2 note was still
  inline *after* the fix shipped to `dist/`; a hard reload showed it correct. Later the
  card photo measured 126×265 (the old horizontal layout) against a build that had already
  replaced it, and `naturalWidth` reported a nonsense `165x123`. `astro preview` + a
  same-URL navigation is not a fresh load — **navigate with a cache-busting query
  (`?v=2`) after every rebuild**, and treat an impossible intrinsic size as the tell.
- **Write the probe's assertion carefully.** `note.top > price.top` "passed" purely on
  baseline offset while the element was still on the same row. The honest test was
  `note.top >= price.bottom` **and** `note.left === tag.left`.
- `final_page_audit`'s `no_aggregateoffer` WARN fires on a page whose own schema list
  contains `AggregateOffer`, and on five siblings too. Pre-existing checker quirk — do not
  "fix" the page for it.

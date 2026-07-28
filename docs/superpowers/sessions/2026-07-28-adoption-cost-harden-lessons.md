# Adoption-Cost Harden & Polish — Lessons for Pages 9–22

**Session:** 2026-07-28 · **Plan:** `docs/superpowers/plans/2026-07-28-adoption-cost-harden-polish.md`
**Page:** `/african-grey-parrot-adoption-cost/` (page 8 of 22) · **Verdict:** PASS-WITH-WARNINGS, live

> **Read this with `2026-07-26-for-sale-cluster-impeccable-lessons.md`.** That one taught "verify the gate
> before you fix the page." This one adds the inverse and more dangerous case: **a clean gate is not a
> clean page.**

---

## 1. The headline lesson: markup↔CSS drift, and why every gate missed it

The breeder's report was "the page feels rushed, the FAQ is broken on mobile and desktop, the contact form
is not well done." All of it was true. **`page_hardening_scan.py` returned `0 ERROR · 0 WARN` on that
page**, and `final_page_audit.py` had already passed it.

The cause was not eight unrelated bugs. It was one failure mode with many symptoms: the page was assembled
by porting the CSS kit and then hand-writing markup that drifted from it.

- **101 CSS classes were defined and never rendered** — including five components the for-sale spec
  mandates.
- The two components that *were* rendered pointed at **the wrong class names**.

### The one-command detector — run this on every ported page

```bash
python3 - <<'PY'
import re
src=open('src/pages/<slug>/index.astro').read()
i=src.find('<style>'); css,markup=src[i:],src[:i]
used=set()
for m in re.finditer(r'class(?:Name)?="([^"{}]+)"',markup): used.update(m.group(1).split())
for m in re.finditer(r'class(?:Name)?=\{`([^`]*)`\}',markup):
    used.update(re.findall(r'[A-Za-z][\w-]*',re.sub(r'\$\{[^}]*\}',' ',m.group(1))))
for m in re.finditer(r'class(?:Name)?=\{[^}]*?"([^"]+)"',markup): used.update(m.group(1).split())
c=css[:css.find('<script')] if '<script' in css else css
defined=set(re.findall(r'^\.([A-Za-z][\w-]*)',c,re.M))
print("IN MARKUP, NO CSS:", sorted(used-defined))
print("STYLED, NEVER RENDERED:", sorted(defined-used))
PY
```

**Interpretation matters more than the output.** A styled-but-unrendered class is one of two things:

| It is… | When | Action |
|---|---|---|
| A **missing component** | the spec mandates it (`.doc-stack`, `.otA`, `.geo-pin`, `.read-img`) | **Render it.** Deleting the CSS hides a spec violation. |
| **Dead code** | it belongs to a variant this page does not use (`.k1` when the page ships K2) | Delete it. |

On this page that split was 7 missing components vs 30 genuinely dead classes.

---

## 2. Specificity collisions are the concrete mechanism — three on one page

Every "component looks wrong" complaint traced to a generic descendant selector out-ranking a component
selector. Look for this pattern explicitly:

| Component rule | Beaten by | Result |
|---|---|---|
| `.faqC-q` on the wrong element; text placed in `.faqC-x` (a 16×16 icon box) | — | every question crushed to 16px |
| answer wrapped in `.faq-d` (light variant, `background:#fff`) inside the dark accordion | `.faqC-item p{color:rgba(255,255,255,.82)}` | **white on white, 1.00:1 — invisible** |
| `.ship-tier{color:#fff}` (0,1,0) | `.ship-c p{color:#5b524a}` (0,1,1) | dark grey on forest green, **1.19:1** |

**Rule for the next build:** when a component's inner element is a bare tag (`p`, `span`, `li`), qualify the
component rule (`.ship-c p.ship-tier`) or the kit's generic descendant rules will silently win.

---

## 3. A clean static scan proves nothing about rendering

`page_hardening_scan.py` cannot see: which class the markup actually applied, whether a class exists at all,
computed contrast, or measured line length. It returned clean on a page whose FAQ answers were invisible.

**Both halves are mandatory, always.** Static scan *and* runtime probes at 375 / 768 / 1280.

### The Browser pane cannot do the runtime half

It reports `vw: 0` and every `getBoundingClientRect()` is zero — elements are in the DOM but nothing paints.
**Use Playwright** (`browser_resize` → `browser_navigate` → `browser_evaluate`). Already banked as
`reference_intersectionobserver_needs_painting_page`; it applies to *all* measurement, not just scroll-spy.

Element screenshots (`browser_take_screenshot` with `target`) are the way to capture a component — a
viewport screenshot resets scroll, and `scrollIntoView` before it does not survive.

---

## 4. My own probes were wrong twice — verify the gate applies to gates you write

1. **The contrast sweep tested `display:none` on the element but not on ancestors.** At 375px it measured
   the `desk-only` dial and reported 8 failures that did not exist. Fix: skip when
   `!el.offsetParent` or the rect is zero-sized. 8 of 13 "failures" evaporated.
2. **The hero "432px, over the 350–420 band"** was me measuring `.adopt-hero` *including* its
   `16px 0 20px` padding. `.hero-grid` was 396px — in band. Measure the element the spec names.

Together with the four checker bugs from 2026-07-26 and the `absolute-hero` false positive below, that is
**six checkers that cried wolf on this cluster.** Budget for it.

### The `absolute-hero-not-unwound` false positive (scanner fixed)

`.hero-tile-p` is a price pill inside `.hero-tile{position:relative}`, and `.hero-imgs` was *already* the
`1fr 1fr` grid §1d prescribes. The exemption matched on names (`badge|chip|tag|caption`) and a pill called
`-p` slipped through. Replaced with a structural test: the rule styles type, sets no `width`/`height`, and a
shorter class it extends declares `position:relative`. **Proved not blinded** by re-injecting the real
2026-07-23 `.pofig{position:absolute;width:44%}` bug and confirming it still WARNs.

---

## 5. A gate that examined nothing is not a pass — the zsh trap

```bash
SL="slug-a slug-b slug-c"
python3 scripts/dup_content_audit.py $SL     # zsh does NOT word-split -> ONE argument
# → "PASS — no cross-page duplicate runs ≥12 words in 0 pages."
```

**zsh does not word-split unquoted parameter expansions.** All eight slugs arrived as a single argument,
matched no page, and the gate reported PASS having compared nothing. **Always read the page count in the
gate's own output.** Pass the slugs literally, or use `${=SL}`.

---

## 6. Asset discipline — what proofing the drop actually caught

Eight infographics were dropped. **Opening all eight found one reject and one systemic problem.**

- **REJECT — `african-grey-five-year-cost-curve.webp`.** Its right-hand axis labels were the page's *bird
  prices and shipping tiers* (`$1,500 / $2,300 / $3,500 / $185 / $350 / $750+`) pasted onto a five-year cost
  curve, plus `40–60 yrs` on a 5-year axis. `$185` is an airport fee, not a five-year total. Reported, not
  substituted; the slot stays empty.
- **All 8 carried an AI sparkle watermark** at a consistent (1284, 649). Removal that works: for each row in
  the box, fill with the **per-channel median of the clean right-edge strip on that same row** — it survives
  vertical gradients. A first attempt sampling 70px to the *left* landed on dark label text and would have
  painted a black rectangle; caught by measuring the residual, not by looking.
- **The 8th filename had a leading space** (`" african-grey-cost-by-decade…"`) — the same congo-build
  gotcha. It silently broke a `^`-anchored grep, so an inventory check reported 7 of 8 as present.
- **A low-information crop makes a useless thumbnail.** Square-cropping the decade-timeline infographic for
  a read-card produced a 1 KB near-blank image — its centre is empty cream. Thumbnails come from photos.

**Orphaned assets are a real category.** Six OG photos were processed and committed in `54e2601` and then
**never referenced by any markup**. Before assuming images are missing, diff `public/` against the page.
Relatedly, `heroPreload` pointed at one of those orphans — the page was preloading 94 KB of an image it
never rendered, which is also not the LCP element.

**Filenames must describe contents, and so must captions.** The video named
`…-with-real-paper-…` is actually a **proof-of-life clip** — two Greys beside a handwritten
"RONY & ROSE / Midland, Texas" sheet. The caption drafted from the filename described a "document folder"
that is not in the frame. With no `ffmpeg` installed, the clip was verified by loading it in Playwright and
capturing frames — which also produced a real 14 KB poster instead of borrowing an unrelated collage.

---

## 7. Data must come from the data files, including when the plan disagrees

The plan hand-drafted an annual-cost table (`$240–$420` food, etc.). Those numbers were **invented**. The
real values live in `financial-entities.json` and are `$200–$400 / $75–$200 / $100–$250 / $0–$500`, summing
to the `$375–$1,350` already printed on the page's own counter strip.

Likewise the plan wrote flight nanny "from $700"; `flight_nanny.cost_from` is **750**, so the breeder's
image was right and the plan was wrong.

**Render every figure through a helper that reads the JSON** (`orange(an.food_and_treats)`,
`money(home - airport)`), never a typed literal. A typed literal is a future contradiction.

---

## 8. Small things worth repeating

- **`caption` must be in the mobile `display:block` list.** Left as `display:table-caption` under a
  `display:block` table, the browser wraps it in an anonymous table box that shrink-wraps to ~70px and
  stacks the title one word per line. This was the true cause of "the ledger title is too thick"; a
  font-size change only treated the symptom.
- **`max-width:none` is conditional, not wrong.** It is correct while a card is a narrow 2-up column and a
  bug the moment that grid collapses to `1fr`. `.ship-c p` and `.quote-c p` measured 90ch at 768. Check
  every uncapped paragraph at the breakpoint where its container goes full width.
- **768 is the breakpoint that fails.** 375 and 1280 were clean; every line-length defect was at tablet.
- **A long card label breaks the button baseline.** `View Jins & Jeni (Pair) →` wrapped to two lines while
  the other five were one. Shorten the label (`View the Pair →`); do not add `nowrap` to a label that cannot fit.
- **Sitemap regeneration on a no-URL-change edit is churn.** The generator stamps today's date on all 109
  URLs. Run it for the phantom-URL check, then revert if the URL set is unchanged.

---

## 9. Carried forward

| # | Item | Owner |
|---|---|---|
| 1 | **INF-4 five-year cost curve needs regenerating** — axis labels are prices/shipping tiers. Slot in §routes is empty until then. | Breeder |
| 2 | **The proof-of-life video master is 640×352** and renders soft in the 760px frame. A higher-res reshoot would be better. | Breeder |
| 3 | **`.stars` is `#c9a227` (2.42:1) on congo + timneh** — below even the 3:1 graphical floor. The other four cluster pages use `clay-ink`. Two-page sweep. | Backlog |
| 4 | **INF-3 route-stacked bars carry no legend and no axis values.** Mitigated by the caption supplying the encoding; a regenerated version with a legend would be better. | Breeder |
| 5 | `congo-african-grey-parrot-pair-for-sale` **FAILS** `final_page_audit.py` — H4:0 H5:0 H6:0, no org schema, no shipping line. It is an unbuilt stub, and it is page 9's job. | Build |
| 6 | GA4 double-load was **not** present on this page's live HTML (1 script, not 2). | — |

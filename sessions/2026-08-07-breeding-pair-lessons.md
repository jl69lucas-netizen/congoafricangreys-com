# Breeding-Pair Finish — Lessons, 2026-08-07

Session scope: `/african-grey-breeding-pair-for-sale/` from "shipped but rough" to done,
plus four breeder corrections raised mid-session and one rule rolled out cluster-wide.

---

## 1. Every probe I wrote was wrong before it was right

Three separate measurement bugs, each of which would have caused real damage if trusted:

| Probe | What it claimed | Truth | Why it lied |
|---|---|---|---|
| H3 image-order | **15** prose-first H3s | **4** | counted decorative seam emblems as "the section image", and ran past the section boundary into the next block |
| read-card auditor | "4 thumbnails checked" | 35 across 11 pages | `(.*?)</div>` truncated the block at the first nested `<div>`, so it examined 2 of 11 pages |
| read-card name match | one correct thumb read as a mismatch | correct | did not flatten `/` in nested `blog/<post>` slugs before comparing |

**The pattern:** a checker that examines a fraction of its corpus is indistinguishable from
a passing one. Both print a number. `reference_gate_examined_zero_pages` says read the
examined count — this session says also *verify the count is the whole corpus*. The
read-card pytest now pins the parser against a nested-div fixture and asserts the auditor
sees every page that has a read-cards block.

Had I acted on the first probe, I would have moved 15 figures, 11 of them needlessly.

## 2. Automating a cluster-wide edit broke three live pages

Rolling the read-card rule across 9 pages, my patchers damaged three before I stopped:

1. **Whole-file substitution on an image stem** rewrote an *unrelated* in-body infographic's
   `srcset` on `congo-african-grey-for-sale`. Anchor every rewrite to the card's `href`.
2. **`srcset=\{[^}]*\}`** stops at the first `}` inside a nested Astro template expression
   and leaves debris that fails the build (`congo-african-grey-parrot-pair-for-sale`).
3. **Matching an `<img>` by filename fragment** hit an in-body nursery photo instead of the
   read-card (`baby-african-grey-parrot-for-sale`).

All three were reverted and hand-edited. **Nothing damaged reached `main`** — but only
because I diffed after every automated pass. The rule for next time: scope the regex to the
component block first, then rewrite whole tags, never attributes inside template literals.

## 3. Two component bugs were the real cause of "it's not showing"

The breeder reported the review was missing. It was, and for two reasons neither of which
was the review copy:

- **`Schema.astro`'s `organization` branch was the only one of four that ignored its `data`
  prop.** Any caller passing extra nodes had them silently dropped. Fixed at the component;
  spreading `{}` is a no-op, verified byte-identical output on two unrelated pages.
- The page had **two orphan `.quote-c` overrides and no base component** — styling a
  component that was never written.

When something "doesn't show", check the component contract before the content.

## 4. A rule justified by "like the other pages" that no other page follows

The breeder's images-first rule was stated as *"just like on other for-sale pages."* The
built pages disagree: congo-pair 13 prose-first H3s, congo 9, timneh 6, egg 4, and **zero
image-first anywhere in the cluster**. The instruction was reaffirmed and shipped on
breeding-pair, which is now the only page that follows it.

Recording this because the *justification* was measurably false while the *instruction*
stood. Both facts matter: a future session reading only the rule text would "restore
consistency" by reverting it.

## 5. The perf gate did not exist, and an agent is not a gate

`package.json` had no perf script; `skills/` had no perf skill; `tests/render/checks/` had
no A11Y family. What existed were two *agents*. An agent runs when someone remembers to
call it, produces prose, and nothing fails. Now:

- `tests/render/checks/a11y.ts` → `a11y-text-contrast-aa`, **blocking**, ~2s, computes
  contrast from rendered colours. Skips text over images, gradients and translucent layers
  because no honest backdrop colour exists there — and **skipped is excluded from
  `examined`**, so the count reports what the predicate actually ran against.
- `scripts/perf_audit.py` → Lighthouse against `dist/`, `--runs N` reports median + spread
  because CLS here is bimodal.
- `skills/cag-perf-gate.md` → the fix bank, keyed by audit id.

## 6. Rules ship with checks, or they are deletion candidates

Four rules were added this session. Every one has a backing test and both fixture halves:

| Rule | Check |
|---|---|
| `layout-hero-counter-separation` | `tests/render/checks/layout.ts` |
| `layout-h3-image-first` | `tests/render/checks/layout.ts` |
| `read-card-thumb-is-target-hero` | `tests/test_read_card_thumbs.py` |
| `a11y-text-contrast-aa` | `tests/render/checks/a11y.ts` |

`quality_report.py` §5 lists none of them as untested. The first attempt at registering the
read-card rule pointed `test:` at a shell command with an argument, and the report caught it
as a **BROKEN test link** — the validator resolves a `::`-less reference as a file on disk.
That guard is doing exactly the job it was written for.

## 7. Ordering hazards worth remembering

- `generate_sitemaps.py` writes into `public/`, which makes `dist/` stale and the render
  harness **correctly refuses to measure**. Order is: build → sitemaps → build again.
- Running `npx astro build` while the page gate is reading `dist/` trips the same guard.
  Five "failures" in this session were that, not defects.
- `.claude/launch.json` runs `astro preview`, which serves `dist/` — **there is no HMR**.
  Every source edit needs a rebuild before the browser shows it.

---

## Open, not done

- **`fs-video` is styled on the breeding-pair page and never rendered**, and it is in the
  hardening scanner's `SPEC_MANDATED` set. Sibling pages do ship it (congo 2, egg 2,
  hand-raised 1). There are pair videos on disk — `rony-and-rose-proof-of-life-midland-tx.mp4`,
  `video/congo-pair-socialization.mp4` — but none of them is Talker & Jane, Mari & Lake or
  Sally & Odin, and captioning footage as a pair it does not show would be a fabricated
  claim. **Needs a breeder answer: which video, if any, belongs on this page.** The CSS was
  left in place per the scanner's own instruction not to delete a mandated component's rules.
- **Images-first is shipped on breeding-pair only.** A cluster-wide rollout is a change of
  house style, not a bug fix.
- **`wordcount_in_band`** stays warned and accepted at ~8,600 words, per explicit breeder
  instruction. Not a defect on this page.
- **`/70de/` source maps** — Cloudflare Rocket Loader, dashboard-only, Unscored. Documented
  as known-ignored in `skills/cag-perf-gate.md`; no code task exists.

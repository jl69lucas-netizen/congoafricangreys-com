---
name: cag-contact-form
description: Audits, fixes and verifies every inquiry and newsletter form on CongoAfricanGreys.com against the seven-field contract and the single Formspree endpoint (xrejpnvn). Use for "add a field to the forms", "forms go to the wrong email", "check every contact form", or after any page build that renders a <form>.
allowed-tools: [Read, Write, Bash]
---

# CAG Contact Form & Newsletter Skill

Rewritten 2026-09-11 from the shipped result. Plan and evidence:
`docs/superpowers/plans/2026-09-11-contact-form-fields.md` · `sessions/2026-09-11-contact-form-fields-brief.md`.

## Golden Rule
> Use Claude Code and the Playwright CLI first. Measure `dist/`, never source.
> A gate's PASS is only as good as its examined count — read it every time.

---

## The one endpoint

| Item | Value |
|---|---|
| Every form on the site (inquiry AND newsletter) | `action="https://formspree.io/f/xrejpnvn" method="POST"` |
| Dashboard | https://formspree.io/forms/xrejpnvn/submissions |
| Honeypot | `<input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">` (the page's own off-screen class: `.hp`, `.cf-hp`, Tailwind `sr-only`, or inline `position:absolute;left:-9999px`) |
| Success redirect | `<input type="hidden" name="_next" value="https://congoafricangreys.com/contact-us/?success=true">` (fires GA4 `generate_lead` — `src/pages/contact-us/index.astro`) |
| Subject | `<input type="hidden" name="_subject" value="C.A.Gs inquiry — <slug>">` — newsletters use `Newsletter Signup — CongoAfricanGreys.com` |

**Retired on 2026-09-11 and wrong on sight** — `scripts/form_contract_audit.py` fails the build on each:
- `xpqoeazq` — the MFS form. Inquiries "still going to the MFS email" was this.
- `data-netlify="true"` / `netlify-honeypot` / `form-name` / `bot-field` — no handler exists on Cloudflare Pages; the browser POSTs to the page and the mail vanishes.
- `action="/thank-you/"` — no such page.
- `action="/contact-us/"` — a static page; the address is lost.
- `action="/api/newsletter"` — no such route.
- An email `<input>` with no `name` — Formspree receives nothing.

## The seven-field contract (2026-09-11)

Applies to every **inquiry** form — any form whose visible controls are more than a single email box
(the same rule as `scripts/form_contract_audit.py`). Three contracts, chosen by slug
(`contract_keys()` in the audit, `contractFor()` in `tests/render/checks/form.ts` — pinned in meta.spec):

| Contract | Pages | Fields |
|---|---|---|
| **full** | every in-scope page, **including `/` and `/contact-us/`** (breeder lifted their opt-out 2026-09-11; the `requireAll` prop is gone) | all seven below |
| **short** | `blog/*` posts (breeder, 2026-09-11: "old short forms … only confirm email, numbers, the two questions") | Confirm Number, Confirm Email, resale, surrender — required. Interest + message stay optional as on the original short form; phone is required because Confirm Number presupposes one |
| **none** | the location cluster and `buy-*` (41 location pages render `CTA.astro`, which has no `<form>`) | endpoint only |

Existing fields are kept, nothing is duplicated, and every contract field carries a red `*` in the
page's own required class, colour `#b04228`.

| # | Label | name | control |
|---|---|---|---|
| 1 | Confirm Number | `phone_confirm` or `cell_confirm` (match the page's phone field) | tel, required |
| 2 | Confirm Email | `email_confirm` | email, required |
| 3 | Are you involved in any pet store, commercial parrot breeding operation, or getting parrots for cheap resale? | `resale_screening` | radio `yes` / `no`, required |
| 4 | Have you ever surrendered a pet to a shelter or given one away? | `surrender_history` | textarea, required, placeholder "If yes, please explain in detail. Honest answers are appreciated." |
| 5 | Are you a First-Time or Experienced Parrot Owner? | `experience` | radio `experienced` / `first-time`, required |
| 6 | How would you like your grey to reach you? | `delivery` (`delivery_method` in `cag-inquiry-form`) | radio cards with descriptions, required |
| 7 | Message (the page's own label) | `message` or `msg` | textarea, required |

Delivery cards — fixed copy, every phrase already on the live site; a `<select>` cannot carry a
description, which is why delivery is always a radio list:

| value | title | description |
|---|---|---|
| `Airport pickup — $185` | Airport Pickup · $185 | Flies on IATA live-animal terms with Delta, United or American to your nearest major airport; you collect at the airline's cargo desk. |
| `Home delivery — $350` | Home Delivery · $350 | Brought to the address you give us, on a date we agree with you first. |
| `Flight nanny — from $750` | Flight Nanny · from $750 | A nanny keeps your grey in the cabin for the whole flight; quoted per route. |
| `Pickup in Midland, TX` | Local Pickup · Free | Collect from us in Midland, TX if you live within two to three hours. |

(Pages with an existing value scheme keep it: dna-tested / hand-raised submit `Airport pickup ($185)`,
baby submits `airport` / `home` / `nanny` / `midland`, adoption-cost renders prices through `money()`.)

## Form families and where each lives

| Family | Vocabulary | Files |
|---|---|---|
| Full shared | `.inq-*`, `.inq-required` | `src/components/cag-inquiry-form.astro` (15 pages + `/` + `/contact-us/`) |
| Compact shared | `.cf-*`, `.cf-req`, `.cf-rad`, `.cf-dlv`, `.cf-hp` · prop `variant` — `"short"` (default, the 9 blog posts) / `"full"` (the scam page's 2 forms) | `src/components/cag-inquiry-compact.astro` |
| `cta-form` | `.form-2col` / `.form-2up`, `.fset`, `.rad`, `.dlv`, `.req` | 8 comparison pages · congo / timneh / eggs for-sale · adoption-cost |
| `form-main` | `.f2`, `.fset`, `.rad`, `.dlv`, `.req`, scoped `.dnat` / `.handraised` / `.hgar` | dna-tested · hand-raised · health-guarantee |
| `fs-fields` | `.fld`, `.fld2`, `.fset`, `.rad`, `.dlv`, `.req` | breeding-pair · congo-pair · baby |
| Tailwind bird | `text-clay-text` star, `has-[:checked]:border-clay` pills | `/available/` + roys, amie, bery, elad, evie, jins-jeni |
| Newsletter | `cag-library/Newsletter.astro` (default action xrejpnvn, `method="POST"`, `name="email"`) · `NewsletterV2` · `Footer.astro` | 47 `<Newsletter>` uses in 27 files + 9 `NewsletterV2` |

Adding a field to a family: copy that family's block from the plan (Tasks 5–9). The patcher
`scripts/oneoff/patch_forms_2026_09_11.py` is the pattern — every substitution must match **exactly
once** or the file is left untouched, so a page whose markup drifted fails loudly instead of half-patching.

## Traps this contract has already sprung

1. **A red `*` inside a grid label drops onto its own row.** `cta-form` and `form-main` labels wrap
   their input and are `display:grid`, so `First name <span class="req">*</span><input>` renders the
   text and the star as two grid rows. Wrap text + star in one span:
   `<label for="x"><span>First name <span class="req">*</span></span><input …></label>`.
   Separate `<label>` elements (`fs-fields` baby, adoption-cost, Tailwind, shared components) are unaffected.
   Only a screenshot shows this — the audit and `checkValidity()` both pass it.
2. **`opacity` on description text** trips `page_hardening_scan` `opacity-dims-text-contrast`. Use an
   explicit colour (`#5a5248` on the `#fff9f6` card ground).
3. **Tailwind v4 `space-y-*` is cancelled by `m-0`.** v4 spaces children with `margin-block-end` inside a
   zero-specificity `:where()`, so an `m-0` utility on a child (the bird-family `<fieldset>`s had
   `border-0 p-0 m-0`) wins and the NEXT group title sits 0px under the pills/cards above it. Never put
   `m-0` on a child of a `space-y-*` stack; preflight already zeroes fieldset margins. Measured, not seen:
   `scripts/form_title_gap_probe.mjs` (every group title ≥12px below the control above it, 3 widths).
   The probe measures an option's pill/card LABEL, never the radio circle inside it — the circle sits
   ~12px above the pill's bottom edge and hid the 0px collision in the first version of the probe.
   Row gaps now: `form-main` 1rem, `fs-fields` label/fieldset 14px, Tailwind `space-y-4` 16px.
4. **Radio/card inputs inherit the family's text-input rule** (width, padding, border). Every family's
   CSS ends with a reset: `width:auto;padding:0;border:0;background:none;box-shadow:none;accent-color:#e8604c`.

## Gates — run all four, in this order

```bash
python3 scripts/form_contract_audit.py --json /tmp/cag-forms.json   # every page in dist/, exit 1 on any miss
node scripts/form_contract_browser.mjs /tmp/cag-forms.json           # real browser: empty rejects, filled accepts, screenshots
node scripts/form_title_gap_probe.mjs /tmp/cag-forms.json            # every group title >=12px below the control above, 375/768/1280
npm run test:render:pages -- --grep form-inquiry-contract            # harness FORM family (advisory)
```

Form text is UI copy shared by design, so both duplicate gates skip it: `scripts/dup_content_audit.py`
(`SKIP_TAGS` includes `form`) and, since 2026-09-11, `tests/render/checks/dup.ts` + `lib/dupCorpus.ts`.
Before that fix the harness read `<main>` with forms included and flagged the fixed contract questions
as sibling crossovers — two gates, one input, different verdicts.

Cross-check the audit's `forms examined` independently — if they differ, the audit skipped something:

```bash
echo $(( $(find dist -name index.html -exec cat {} + | grep -o '<form' | wc -l) - $(find dist -name index.html -exec cat {} + | grep -o 'action="/search/"' | wc -l) ))
```

Then **open at least one 375px screenshot per family** (`sessions/2026-09-11-form-screens/`) — trap 1
was invisible to every mechanical gate.

## What Was Fixed (2026-09-11)

- 14 forms posted to a Netlify handler that does not exist on Cloudflare; 2 to `/thank-you/` (404); 1
  GET to `/contact-us/`; 1 to `xpqoeazq`; 10 blog newsletter boxes to `/contact-us/`, and the
  `Newsletter` component's email input had no `name`. All now POST to xrejpnvn.
- Seven-field contract on all 51 in-scope inquiry forms across 7 families, each in its own vocabulary —
  no form swapped for a shared component, no layout change.
- Measured at ship: audit PASS, 117 forms examined = 223 `<form>` in dist − 106 search forms; browser
  proof 102 form-viewports (51 × 375/1280), 0 failures.
- Harness family `FORM` + advisory `form-inquiry-contract`; static audit `scripts/form_contract_audit.py`;
  browser proof `scripts/form_contract_browser.mjs`.
- `/available/evie/` hidden bird value and subject said ELAD / Male — corrected to Evie / Female.

## After a form change

Build → the three gates → commit **and push** (push is deploy) → `python3 scripts/indexnow_submit.py <slug>`
for every slug whose rendered output changed (a shared-component edit changes every page that renders it).

## Reporting Format

```
FORM CONTRACT — congoafricangreys.com
forms examined: N (inquiry I, in-scope S, newsletter L)   cross-check: N ✓
audit: PASS | FAIL (rows…)
browser: 2×S form-viewports, 0 failure(s)
screens eyeballed: <one per family>
endpoints retired this run: …
```

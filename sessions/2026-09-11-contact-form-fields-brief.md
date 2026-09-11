# 2026-09-11 — Contact-form field contract

Plan: docs/superpowers/plans/2026-09-11-contact-form-fields.md
Plan artifact: https://claude.ai/code/artifact/6cecb10f-8ca6-4be6-ac77-0459e0bab290
Prompt-rewrite artifact: https://claude.ai/code/artifact/e46af6a3-172f-4892-baf1-ced38d35f41a

## Open Flags
1. `requireAll={false}` keeps `/` and `/contact-us/` byte-identical (Message optional, no Flight Nanny card). Recommend lifting: remove the prop on both pages, one-line change each.
2. The compact blog form grows from 5 to 12 fields. Conversion trade-off accepted per brief; watch Formspree volume on blog `_subject`s for 30 days.
3. Delivery `<select>` → radio list on every raw form, to carry the requested descriptions.
4. Newsletter boxes now post to xrejpnvn (11 pages posted to a static page and lost the address; the component's input had no `name`).
5. `/available/evie/` hidden `bird` value and `_subject` said "ELAD … Male"; corrected to Evie / Female.
6. Formspree form `xpqoeazq` (the MFS form) is no longer referenced anywhere in src; deleting it in the Formspree dashboard is the breeder's call.
7. `/thank-you/` does not exist; two forms pointed at it. Both now use `_next` → `/contact-us/?success=true`.
8. The full form's pricing-card footer still reads "Shipping: $185 · Home delivery: $350" while the form now offers Flight Nanny from $750. Left as-is (changing it would alter the two opt-out pages); recommend updating the footer when Flag 1 is lifted.
9. Escape caught before push: on the `cta-form` (11 pages) and `form-main` (3 pages) families the red `*` rendered on its own row under every label — those labels wrap their input and are `display:grid`, so text and star became two grid rows. Fixed by wrapping text + star in one `<span>` (commit cd0590b8). Found only by eyeballing the 375px browser-proof screenshots; the static audit, `checkValidity()` and the harness all passed it. No existing invariant covers "required marker detached from its label", so per the learning loop this is a **candidate** LAYOUT check (fixture red first, advisory), not a new rule.

### Round 2 (breeder, same day)
- Flag 1 **closed**: `/` and `/contact-us/` carry the full contract; `requireAll` deleted (ee6e37cb). Flag 8 **closed**: pricing footer names Flight nanny from $750.
- Blog posts reverted to the old short form + confirm email, confirm number, resale, surrender (breeder chose resale + surrender); scam page stays full (4e59d67f).
- Bird + /available/ group titles sat 0px under the pills (Tailwind v4 space-y vs `m-0`); all families now ≥12px at 3 widths, new gate `scripts/form_title_gap_probe.mjs` (126be263).
- P0 found by the impeccable critique: full form's required delivery radios were `display:none` → submit silently blocked; fixed 1807d015, guarded in form_contract_browser.mjs (f90f23c9).
10. `text-clay-text` is undefined in the Tailwind theme: 367 uses on the homepage + /available/ render in inherited ink. Form stars repointed to `text-clay-ink`; defining the token recolours the homepage — breeder preview first.
11. Both dup gates exempt a genuine crossover adjacent to a whitelisted line — spun out as its own task.
12. Formspree `xpqoeazq` deletion is the breeder's (permanent deletion in their account; export old submissions first).
- Critique artifact: https://claude.ai/code/artifact/cdee5b57-98f9-4bc3-9929-2cad14cdadc2 (+ docs/artifacts/cags-form-critique.md).

### Round 3 — breeder's picks from the critique (preview before apply, CLAUDE.md rule 7)
Chosen: (a) screening-question polish — "Questions we ask every family" group + one-line why, sentence-case question legends, surrender as Yes/No that reveals the text box only on Yes; (b) inline error messages — summary above submit, per-field message, "Emails don't match" / "Numbers don't match"; (c) 44px Yes/No pills on mobile + define the missing `text-clay-text` colour (homepage recolour previewed first).
Not chosen (stays open): one field order across all families.

## What's Next
- Promote `form-inquiry-contract` to blocking after one full cluster with zero false reports (learning-loop §4).
- Candidate LAYOUT check for Flag 9: every `.req` / `.inq-required` / `.cf-req` star's box top sits within its label text's first line box. Write `known_broken` first (a grid label with text + star + input), watch the meta gate fail, then implement as advisory.
- Breeder decision on Open Flag 1 (lift `requireAll={false}` on `/` and `/contact-us/`), and Flag 8's pricing-card footer with it.
- 30-day Formspree volume check on blog `_subject`s (Open Flag 2).
- Delete Formspree form `xpqoeazq` in the dashboard (breeder).
- `.claude/skills/cag-component-variations/SKILL.md` was re-synced from `skills/` by `register_skills.py --copy` (adds the 2026-09-10 canvas URL line already in the source); left uncommitted with the other pre-existing skill-copy syncs.

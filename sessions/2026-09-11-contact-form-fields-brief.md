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

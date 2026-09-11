# Goal + Done-Means Rewrites — the contact-form fields prompt

Source prompt: 2026-09-11, "add Confirm Number / Confirm Email / resale / surrender / experience / shipping-options fields to every contact form except location, homepage and contact-us; move every endpoint to Formspree xrejpnvn; verify in a browser."

## 1. What the original Goal and Done-means left open

The original pair was:

> **Goal:** Form fields update, read, verify, and confirm your work so no mistakes are made.
> **Done means:** When you have checked via a Chrome extension or Playwright that each form has the new fields provided below.

Four things the agent had to guess, each of which changes the files it touches:

- **Which forms count.** The site has three form families: the shared full component (17 pages, including the homepage and contact-us), the shared compact component (10 pages), and 20 hand-written forms in individual pages. "Every page with a contact form" does not say whether the 34 one-field newsletter boxes count.
- **What "has the new fields" is measured against.** The full component already carries all seven. Nine comparison forms already carry the two confirm fields. Done-means needs to say the check is *field name present + required + endpoint*, or a page that already had five of seven passes by accident.
- **Where the edit lands when the form is shared.** Making Message required on the shared component changes the homepage and contact-us, which the prompt excludes. Goal has to say whether the exclusion is "do not touch those pages" or "do not add fields there".
- **What verification produces.** "Checked via Playwright" is an activity. Done-means should name the artefact: a list of every form with its fields, endpoint and required flags, and a count that matches the count found in source.

## 2. Three rewrites, Goal and Done-means only

### A. Field-contract first (Recommended)

> **Goal:** Every inquiry form outside the homepage, contact-us and the location cluster carries the same seven screening fields, in that page's own form styling, every field required with a red asterisk, and every form on the site posts to `https://formspree.io/f/xrejpnvn`.
>
> **Done means:** A Playwright pass over the built site lists every `<form>` and, for each in-scope form, reports the seven field names, `required` on each, and the action URL. Zero rows fail, the examined count equals the number of forms found by grep in source, and one screenshot per form family at 375px and 1280px is attached.

*Why recommended:* it names the invariant, which is what the render harness can turn into a check that keeps firing after this session. Trade-off: it is the longest to write and it forces the shared-component question to be answered in the goal.

### B. Endpoint first

> **Goal:** No form on congoafricangreys.com submits anywhere except `https://formspree.io/f/xrejpnvn`. Remove every `data-netlify` attribute, every `/thank-you/`, `/contact-us/` and `/api/newsletter` action, and the old `xpqoeazq` ID; then add the seven fields to each in-scope inquiry form.
>
> **Done means:** `grep -c "<form" dist/**/index.html` and `grep -c 'action="https://formspree.io/f/xrejpnvn"'` agree on every page except the two site-search forms, and one real test submission from a for-sale page and one from a bird page arrive in the xrejpnvn dashboard.

*Why not first:* it fixes the money leak fastest (fourteen forms currently post to a Netlify handler that does not exist on Cloudflare, so those inquiries vanish), but it leaves "which fields" to a second prompt.

### C. Harness first

> **Goal:** A render-harness check `form-inquiry-contract` fails whenever an in-scope form is missing any of the seven fields, has one marked optional, or posts anywhere but xrejpnvn; pages are edited until the check is green on every target.
>
> **Done means:** `npm run test:render:meta` fails on the check's known_broken fixture and passes known_good; `npm run test:render:pages` reports zero defects for the check with examined ≥ 28 forms; the rule is added to `data/quality/rule-index.json` as `enforced: test`.

*Why not first:* it is the version the learning-loop skill would write, and it is what stops the defect recurring, but it makes the breeder's visible ask (fields on pages) the last thing to land.

## 3. A reusable shape

```
Goal:      <one sentence: the invariant that is true when this is finished,
            with the population it applies to and the exclusions named>
Done means: <the artefact that proves it: a listing, a count that matches a
            second independent count, a gate that fails on a fixture, a
            screenshot per family> — never an activity ("checked", "verified").
```

Two tests for a Done-means line: could a second agent run it without reading the conversation, and does it fail when the work is half done?

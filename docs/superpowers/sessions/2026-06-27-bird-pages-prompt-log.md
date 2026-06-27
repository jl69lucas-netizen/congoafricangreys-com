# Prompt Log — /available/ Bird-Pages Polish Program

> Verbatim record of the user's pasted prompts while working on the bird pages, for reuse as reference templates. **Scope note:** prompts below are from the session of 2026-06-26 → 2026-06-27 (in-context). The earlier arc ("first text few days ago") was driven by the plan docs and session briefs — see *Earlier-arc pointers* at the bottom; those prompts are not reproducible verbatim from this session's context, so they are referenced, not quoted (per the no-fabrication rule).

---

## Session 2026-06-26/27 — verbatim prompts

### Prompt 1 — Resume an interrupted plan
> For this type of situation, do i use writing plan, cag agents or since i know you need to do task 8, should i just past the unfinished task here and say continue or whats the best way?.
>
> Let's continue. It went off. Tasks 1 to 7 are complete, and you are still working on task 8. See the full plan below. Verify then continue
>
> *(followed by the pasted plan-completion status: "Plan complete and saved to docs/superpowers/plans/2026-06-26-available-cluster-perf-schema-geo-fixes.md … T8 done (commit 2cd77d2) … Failed to spec review Task 8")*

**Pattern:** resume a saved plan by pointing at it + "verify then continue." Correct approach (vs re-running a planning skill or spawning agents).

### Prompt 2 — Differentiate two same-sex/variant birds
> Bery — Female Congo African Grey For Sale ($1,700, Hand-Raised & DNA-Sexed)
> Amie — Female Congo African Grey For Sale ($2,500, Hand-Raised & DNA-Sexed)
>
> Just differentiate it so buyers searching for a female grey parrot can land on Bery's page, etc, give me two options to choose from and recommend the best. What framework did you use for each page? Was it blended, AIDA, Entity, Benefit, and Purpose, etc
> Add 1 year and parrot to bery and use a different text here "($2,500, Hand-Raised & DNA-Sexed)."
> Female Congo African Grey Parrot For Sale -add the entity parrot
> Use other related terms, "cuddly handrearer, handfed, etc"

**Pattern:** differentiation request with explicit constraints (add age + "parrot" entity, distinct qualifier text, related terms) + "2 options + recommend" + "what framework."

### Prompt 3 — Action the audit's future-fix list
> and this too, (d) Prioritized fix list (for a FUTURE content pass — not this plan)
> 1  Add 2–3 natural "Congo/Timneh African Grey for sale" phrases to hub intro — hub — Low
> 2  One counter-snippet answering "cheap African Grey for sale" — hub or /african-grey-parrot-price/ — Low

**Pattern:** "do the deferred items from the audit too."

### Prompt 4 — Approve image alt/title differentiation
> yes
>
> *(in reply to the offer: "I can apply the same life-stage differentiation pass to the image alt/title attributes on these two pages … say the word.")*

### Prompt 5 — Final close-out + documentation deliverables
> Perfect, now run one final check on all bird pages and hub to see if all is done well, any bug, etc. Save all good things we did as a skill on these pages from the first text few days ago to the last text today. I also need all the step we used in building these pages as a manual check, also add a section of all the text/prompt i pasted in all the chats while working on these pages. Let the manual be a copy and paste file. Save all bad things we did as ref for future and best work added to the agents for efficient future use case, when creating the skill, invoke the superpower skill creation skill, etc.  issues like this still exist on the pages, mostly on mobile viewpoint, {Requests are blocking the page's initial render … /_astro/BaseLayout … /_astro/cag-inquiry-form … /_astro/JumpRail … Reduce unused JavaScript … /70de/ … Est savings 71 KiB}

**Pattern:** "final check + capture everything as skill/manual/prompt-log/lessons + invoke skill-creator + here's a fresh PageSpeed paste to act on." → produced: `skills/cag-bird-page-excellence/`, `BIRD-PAGE-BUILD-MANUAL.md`, this log, and the lessons ref.

---

## Reusable prompt templates (distilled)

- **Resume a plan:** "Tasks 1–N are complete, you're on Task N+1. See the full plan below. Verify then continue." `<paste plan>`
- **Differentiate siblings:** "[Bird A] and [Bird B] are the same sex+variant. Differentiate so buyers searching [query] land on the right page. Give 2 options + recommend the best with why. Add [entity/term]. What framework?"
- **Action a deferred list:** "and this too, [paste the (d)/backlog table]."
- **Close-out:** "Run a final check on all pages, fix remaining issues, and capture the good patterns as a skill, the steps as a copy-paste manual, my prompts as a log, and the mistakes as a lessons ref; invoke the skill-creator."

---

## Earlier-arc pointers (not verbatim — referenced)

The "first text few days ago" work that built the bird pages to the Roys standard is recorded in:
- `docs/superpowers/plans/2026-06-21-four-bird-pages-image-height-and-overuse-fixes.md`
- `docs/superpowers/plans/2026-06-22-four-congo-bird-pages-cta-contrast-scam-image-polish.md`
- `docs/superpowers/plans/2026-06-23-available-hub-and-bird-pages-batch.md`
- `docs/superpowers/plans/2026-06-26-available-cluster-finish-and-qa.md`
- `docs/superpowers/plans/2026-06-26-available-cluster-perf-schema-geo-fixes.md` (this program's plan)
- `docs/superpowers/sessions/2026-06-26-available-keyword-entity-audit.md` (the self-audit + competitor benchmark)

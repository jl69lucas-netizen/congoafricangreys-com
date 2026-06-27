# Lessons Reference — /available/ Bird-Pages Program (what went wrong + the guardrail)

> The "bad things we did" log, kept so future builds don't repeat them. Each row: the mistake → root cause → the guardrail now in force → where it lives. These are the empirical RED cases behind the `cag-bird-page-excellence` skill.

---

## Failures & guardrails

### 1. Committing a deletion that was still referenced
- **What happened:** The plan asserted two `.webp` files (`amie-congo-african-grey-female-3-months.webp`, `african-grey-parrot-head-scratch.webp`) were unreferenced and safe to drop. They were live on **14 pages including the homepage**. Committing the deletions would have broken images sitewide.
- **Root cause:** Trusting a plan's prediction over the working tree's reality.
- **Guardrail:** Before committing ANY working-tree deletion, `grep -rln "$f" src/ public/`. If referenced → `git checkout -- <path>`. A plan prediction is a hypothesis, not a fact. (CLAUDE.md "look before you delete" reinforced.)
- **Lives in:** skill Common-Mistakes, MANUAL Part H1, memory `project_bird_page_port_pattern` (verify-in-dist family).

### 2. Almost blind-deleting a shared component
- **What happened:** JumpRail was correctly removed from the 6 bird pages (they have `cag-jump-nav`). The same component is the **only** ToC on the homepage + 16 interior pages — deleting it there would strip their navigation.
- **Root cause:** Generalising a fix from one page-type to all.
- **Guardrail:** Before removing a shared component anywhere, confirm a replacement exists on that page (`grep -c 'cag-jump-nav'`). Scope perf fixes per page-type.
- **Lives in:** skill Quick-Reference + MANUAL Part C1.

### 3. Identical headers across sibling pages (cannibalization)
- **What happened:** Bery & Amie H1/title/meta were byte-identical minus name/price — two female Congos fighting for the same query.
- **Root cause:** From-scratch builder cloned the header template without a differentiation pass.
- **Guardrail:** Same sex+variant → differentiate on **life-stage** across H1+title+meta+alt simultaneously; add the "Parrot" entity; present 2 options + Recommend+Why first.
- **Lives in:** skill differentiation matrix, MANUAL Part A, memory `feedback_hybrid_header_seo`.

### 4. Cross-page duplicate image alts
- **What happened:** 3 alt/title pairs were identical-minus-name across the two pages (personality-profile alt, "Buy [Name]" hero alt+title, ready-to-go alt).
- **Root cause:** Same template clone, alts never differentiated.
- **Guardrail:** De-dup alts per page; inject the life-stage signal; keep alt ≤190 chars (5-element image SEO).
- **Lives in:** skill + MANUAL Part A4, memory `feedback_image_seo_5element`.

### 5. Loose grep + trusting a wrapper's error
- **What happened:** A geo-block grep matched the IATA *shipping* paragraph instead of the new geo section; separately, the "spec review" subprocess reported "Failed to spec review Task 8" although the work was sound.
- **Root cause:** Imprecise patterns; conflating a tool wrapper's failure with the underlying work failing.
- **Guardrail:** Verify in `dist/` with precise, unique patterns; verify the *work* directly rather than trusting a review wrapper's exit status.
- **Lives in:** skill Implementation + memory `feedback_verify_rendered_not_source`.

### 6. Assuming curl/WebFetch can verify external links
- **What happened:** fws.gov (404 fix), cites.org, and Google's Rich Results Test all return 403 to every automated agent — the link fix and schema fix could not be machine-verified.
- **Root cause:** Bot-blocking on government/standards/Google domains.
- **Guardrail:** Mark these **human-browser** steps explicitly; never claim a 200/PASS you could not fetch. Retry once with `-A "Mozilla/5.0"` before concluding dead.
- **Lives in:** skill Quick-Reference + MANUAL Part F/H5, memory `reference_external_link_curl_403`.

### 7. Re-encode that upscales / grows files
- **What happened (prior session, carried as a guardrail):** a downscale re-encode grew `roys-personality.webp` 48→65 KB.
- **Root cause:** Re-encoding/upscaling without a shrink-only guard.
- **Guardrail:** `if im.width > target_w` before resize; never upscale; q=80; confirm `dist/` file shrank.
- **Lives in:** skill + MANUAL Part C4, `scripts/downscale_available_images.py`.

### 8. Amending an auto-pushed commit
- **What happened (carried guardrail):** the post-commit hook auto-pushes commit #1; amending it diverges origin and later auto-pushes silently fail.
- **Guardrail:** Commit fixes as NEW commits, or reconcile with `git push --force-with-lease`. Confirm `HEAD == origin/main` after each push.
- **Lives in:** skill + MANUAL Part H4, memory `project_autopush_hook_amend_diverges`.

---

## What we did WELL (reusable wins)

1. **One-axis differentiation propagated through every layer** (H1 → title → meta → alt → buyer-intent) — the cannibalization cure.
2. **Distinct regional geo blocks** with a unique H3 per page + on-disk slug resolution check (zero invented slugs, zero duplicate content).
3. **Truthful Product/Offer schema** (`shippingDetails`, `hasMerchantReturnPolicy`, `priceValidUntil`) clearing the Search Console critical **without** fabricating a single review.
4. **Counter-snippet FAQ** capturing a competitor's primary query ("cheap African Grey parrot for sale") and reframing it to value — rendered in both visible accordion **and** FAQPage schema.
5. **Audit-then-rewrite discipline** — graded each page STRONG/SHARPEN/REBUILD and rewrote only the weak, never regressing indexed copy.
6. **Competitor benchmark with integrity** — un-fetchable competitors marked `NOT FETCHED`, never invented counts; surfaced the CITES/DNA/captive-bred entity moat.
7. **Verify-in-dist, 0-FAIL final gate** every time before deploy; sitemaps regenerated; `HEAD == origin` confirmed.

---

## Outstanding (human-only)

- Cloudflare **Rocket Loader OFF** (`/70de/`, 71 KiB unused JS — biggest mobile-LCP win).
- Browser-verify the FWS CITES link + re-run Rich Results Test on `/available/roys/`.
- **Homepage + 16 interior pages still render-block `JumpRail.css` + `cag-inquiry-form.css`** — a separate, larger optimization (those pages use JumpRail as their real ToC; needs a critical-CSS/defer approach, not a delete). Tracked here for a future perf pass.

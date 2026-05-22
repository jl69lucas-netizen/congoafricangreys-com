# Search Fix + 404 Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the search bar so users can search repeatedly without getting stuck on "Loading…", then crawl the live site with Firecrawl to find and fix all 404s and broken links.

**Architecture:**
- Task 1 is a one-line Pagefind fix (`pagefind.init()`) plus a UX improvement (show Loading… dynamically instead of hardcoded in HTML).
- Task 2 uses the Firecrawl MCP to crawl `https://congoafricangreys.com`, collects all HTTP status codes, then fixes 404s via `site/content/_redirects` entries or new Astro pages, depending on intent.

**Tech Stack:** Astro 5, Pagefind (self-hosted search), Cloudflare Pages `_redirects` format, Firecrawl MCP

---

## Root Cause: Task 1

The search page at `src/pages/search/index.astro` (line 56) calls `pagefind.search(q)` **without first calling `pagefind.init()`**. Pagefind's WASM runtime requires `init()` to be called before each use once the browser has cached the module. On first page load it sometimes works by accident (race with auto-init), but on any subsequent navigation to `/search/?q=…`, the cached module's internal WASM worker is in a stale state and `search()` hangs indefinitely — leaving the hardcoded "Loading…" on screen forever.

**Known redirect conflict (also fixed in Task 1):**
Lines 57–58 of `site/content/_redirects` redirect `/baby-african-grey-parrot-for-sale` → `/african-grey-parrot-for-sale/`, but `src/pages/baby-african-grey-parrot-for-sale/index.astro` is a real page. Cloudflare Pages evaluates `_redirects` before the page, so the page is unreachable. Remove those two redirect lines.

---

## File Map

| File | Action | Why |
|------|--------|-----|
| `src/pages/search/index.astro` | Modify | Add `pagefind.init()`, move Loading… to JS |
| `site/content/_redirects` | Modify | Remove baby-african-grey conflict; add 404 fixes after crawl |

---

## Task 1: Fix Pagefind Search (One-Line Core Fix + UX)

**Files:**
- Modify: `src/pages/search/index.astro`

- [ ] **Step 1: Open the search page**

  File: `src/pages/search/index.astro`
  
  Current script block (lines 33–79):
  ```javascript
  const params = new URLSearchParams(window.location.search);
  const q = params.get('q') ?? '';
  ...
  async function runSearch() {
    ...
    let pagefind: any;
    try {
      pagefind = await import('/pagefind/pagefind.js');
    } catch { ... }
  
    const search = await pagefind.search(q);   // ← hangs on 2nd call
    ...
  }
  runSearch();
  ```
  
  Initial HTML (line 27–29):
  ```html
  <div id="results" class="space-y-5">
    <p class="text-stone-400 text-sm">Loading…</p>   ← hardcoded, confusing
  </div>
  ```

- [ ] **Step 2: Apply the fix**

  Replace the entire `<div id="results">` block and the `<script>` block with the corrected versions below.
  
  New `<div id="results">` (remove the hardcoded Loading paragraph):
  ```html
  <div id="results" class="space-y-5"></div>
  ```
  
  New `<script>` block (two changes: `pagefind.init()` added; Loading… shown dynamically):
  ```javascript
  const params = new URLSearchParams(window.location.search);
  const q = params.get('q') ?? '';

  const refineInput = document.getElementById('search-refine') as HTMLInputElement;
  if (refineInput && q) refineInput.value = q;

  const resultsEl = document.getElementById('results')!;

  async function runSearch() {
    if (!q.trim()) {
      resultsEl.innerHTML = '<p class="text-stone-500 text-sm">Enter a search term above.</p>';
      return;
    }

    resultsEl.innerHTML = '<p class="text-stone-400 text-sm">Loading…</p>';

    let pagefind: any;
    try {
      pagefind = await import('/pagefind/pagefind.js');
      await pagefind.init();                    // ← THE FIX: reinitialise WASM on every call
    } catch {
      resultsEl.innerHTML = '<p class="text-stone-500 text-sm">Search index not available — try again after the next site deploy.</p>';
      return;
    }

    const search = await pagefind.search(q);

    if (!search.results.length) {
      resultsEl.innerHTML = `<p class="text-stone-500 text-sm">No results found for "<strong>${q}</strong>". Try a shorter or different term.</p>`;
      return;
    }

    const items = await Promise.all(search.results.slice(0, 12).map((r: any) => r.data()));

    resultsEl.innerHTML = items.map((item: any) => `
      <a href="${item.url}" class="block border border-stone-200 rounded-xl p-5 hover:border-clay/50 hover:shadow-sm transition-all group">
        <div class="font-lora font-semibold text-logo-dark text-lg group-hover:text-clay transition-colors mb-1">
          ${item.meta?.title ?? item.url}
        </div>
        <div class="text-stone-500 text-sm leading-relaxed line-clamp-2">
          ${item.excerpt ?? ''}
        </div>
        <div class="text-clay text-xs mt-2 font-sora">${item.url}</div>
      </a>
    `).join('');
  }

  runSearch();
  ```

- [ ] **Step 3: Fix the baby-african-grey redirect conflict**

  File: `site/content/_redirects`
  
  Find and delete these two lines (currently lines 57–58):
  ```
  /baby-african-grey-parrot-for-sale /african-grey-parrot-for-sale/ 301
  /baby-african-grey-parrot-for-sale/ /african-grey-parrot-for-sale/ 301
  ```
  
  Reason: `src/pages/baby-african-grey-parrot-for-sale/index.astro` is a real page. Cloudflare Pages evaluates `_redirects` before serving the static file, so these rules shadow the page, making it permanently return a redirect instead of its content.

- [ ] **Step 4: Build and verify locally**

  ```bash
  cd /Users/apple/Downloads/CAG
  npm run build
  ```
  
  Expected: build completes with no errors. The `dist/` folder should contain `pagefind/` after the build script runs `npx pagefind --site dist`.
  
  Note: The `pagefind.init()` call is safe to add — it is idempotent and is the officially recommended pattern for the Pagefind raw JS API. It no-ops if already initialized, and reinitializes the WASM worker if the previous session ended.

- [ ] **Step 5: Commit**

  ```bash
  git add src/pages/search/index.astro site/content/_redirects
  git commit -m "fix: add pagefind.init() so search works on repeated queries; remove baby-african-grey redirect conflict"
  git push
  ```

---

## Task 2: Crawl Live Site with Firecrawl and Fix All 404s

**Files:**
- Modify: `site/content/_redirects` (add new redirect rules per finding)
- Create: new Astro pages only if a 404 URL has genuine content intent with no existing redirect target

> **Important:** Run this task AFTER Task 1 is deployed, so the live site reflects the redirect fix from Task 1 before the crawl.

### Step 2a: Crawl the live site

- [ ] **Step 1: Use Firecrawl MCP to crawl the full site**

  Use the `mcp__firecrawl-mcp__firecrawl_crawl` tool with these parameters:
  ```json
  {
    "url": "https://congoafricangreys.com",
    "maxDepth": 4,
    "limit": 500,
    "scrapeOptions": {
      "formats": ["links"],
      "onlyMainContent": false
    }
  }
  ```
  
  This crawls from the homepage, follows all internal links up to 4 levels deep, returns each page's URL and status code.

- [ ] **Step 2: Also check status of known redirect targets**

  Many pages in `site/content/_redirects` point to targets that may themselves 404. Run a batch status check on the 30 most-linked redirect targets from the redirects file. Use `mcp__firecrawl-mcp__firecrawl_scrape` or `curl -I` per URL to get HTTP status.

  Key targets to verify (from the current `_redirects`):
  - `/african-grey-parrot-for-sale/` — does it return 200?
  - `/african-grey-parrot-guide/` — does it return 200?
  - `/african-grey-parrot-health-guarantee/` — does it return 200?
  - `/trusted-african-grey-parrot-breeders/` — does it return 200?
  - `/male-vs-female-african-grey-parrots-for-sale/` — does it return 200?

### Step 2b: Categorize and fix each 404

- [ ] **Step 3: Categorize all 404 URLs found by the crawler**

  For each 404 URL, determine intent using this decision tree:
  
  | URL pattern | Intent | Fix |
  |-------------|--------|-----|
  | Matches an existing live page with a slightly different slug | Navigation typo / old URL | Add redirect in `_redirects` |
  | Matches a topic with a clear existing page | Content moved | Add redirect in `_redirects` |
  | Matches a topic that should have its own page (high-intent keyword) | Missing content | Create new Astro page or redirect to closest match |
  | WordPress artifact, random path, spam | No intent | Add redirect to `/` in `_redirects` |

- [ ] **Step 4: Add redirect rules for all discovered 404s**

  File: `site/content/_redirects`
  
  Add each new rule at the **bottom** of the file, in this format:
  ```
  /the-404-url /the-target-page/ 301
  /the-404-url/ /the-target-page/ 301
  ```
  
  Always add both the trailing-slash and non-trailing-slash variant. Use 301 (permanent) for all content redirects.

- [ ] **Step 5: Fix any broken redirect chains discovered**

  A redirect chain is A→B→C where B also redirects. Flatten to A→C directly. Example:
  ```
  # Before (chain):
  /old-url /intermediate/ 301
  /intermediate/ /final/ 301
  
  # After (flattened):
  /old-url /final/ 301
  /intermediate/ /final/ 301
  ```

- [ ] **Step 6: Verify no live pages were accidentally redirected away**

  Run this check after edits to `_redirects`:
  ```bash
  # List all pages in src/pages that exist
  find /Users/apple/Downloads/CAG/src/pages -name "index.astro" | sed 's|/Users/apple/Downloads/CAG/src/pages||' | sed 's|/index.astro||' | sort
  ```
  
  Then scan `_redirects` for any rule whose source matches a real page path. If found, delete that redirect rule — the real page should serve.

- [ ] **Step 7: Commit the 404 fixes**

  ```bash
  git add site/content/_redirects
  # If any new pages were created:
  # git add src/pages/<new-page>/index.astro
  git commit -m "fix: add redirects for all 404 URLs found in Firecrawl audit"
  git push
  ```

### Step 2c: Post-fix verification

- [ ] **Step 8: Re-crawl after deploy to confirm 0 remaining 404s**

  Wait ~2 minutes for Cloudflare Pages deploy to complete, then re-crawl:
  ```
  mcp__firecrawl-mcp__firecrawl_crawl with same parameters
  ```
  
  Expected: all previously-404 URLs now return 200 or 301. Zero 404s remaining.

---

## Verification

1. **Search fix**: Visit `https://congoafricangreys.com/search/?q=birds` → verify results appear. Then type "parrots" in the refine box and click Search → verify results appear again (not stuck on Loading…). Do this 3+ times.
2. **baby page fix**: Visit `https://congoafricangreys.com/baby-african-grey-parrot-for-sale/` → verify it shows the actual page content (not a redirect to `/african-grey-parrot-for-sale/`).
3. **404 audit**: Firecrawl re-crawl shows 0 remaining 404s.

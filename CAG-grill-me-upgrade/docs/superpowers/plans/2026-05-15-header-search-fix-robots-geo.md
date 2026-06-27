# Header Search Bar Fix + Robots.txt GEO Update

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix logo/search bar collision on small mobile screens, reduce search bar width by 50%, and add AI crawler rules to robots.txt for GEO optimization.

**Architecture:** Two isolated changes — (1) Tailwind class edits in `Header.astro` for layout stability, (2) appending AI crawler directives to `public/robots.txt`. No new files, no component restructuring.

**Tech Stack:** Astro, Tailwind CSS, static `public/robots.txt`

---

## File Map

| File | Change |
|------|--------|
| `src/components/Header.astro` | Fix mobile search form width + logo container shrink-0 + desktop search width |
| `public/robots.txt` | Append AI crawler allow/disallow rules |

---

## Task 1: Fix Logo + Search Bar Collision on Mobile

**Root cause:** The left logo `<div>` wrapper (line 22) lacks `shrink-0`, so on narrow viewports (<360px) the logo container competes with the `flex-1` mobile search form. Combined with `flex-1`, the search form expands to push the logo.

**Files:**
- Modify: `src/components/Header.astro` lines 22, 29, 61

- [ ] **Step 1: Add `shrink-0` to the left logo wrapper div (line 22)**

Change:
```astro
<div class="flex items-center gap-3">
```
To:
```astro
<div class="flex items-center gap-3 shrink-0">
```

- [ ] **Step 2: Reduce desktop search input width by 50% (line 29)**

Change:
```astro
class="w-40 bg-white/10 border border-white/30 text-white placeholder:text-white/50 rounded-full px-3 py-1.5 text-xs focus:outline-none focus:border-clay"
```
To:
```astro
class="w-20 bg-white/10 border border-white/30 text-white placeholder:text-white/50 rounded-full px-3 py-1.5 text-xs focus:outline-none focus:border-clay"
```

- [ ] **Step 3: Constrain mobile search form to ~50% of available width (line 61)**

Change:
```astro
<form action="/search/" method="get" class="flex lg:hidden flex-1 mx-3">
```
To:
```astro
<form action="/search/" method="get" class="flex lg:hidden mx-2 max-w-[44%]">
```

**Why `max-w-[44%]`:** On a 360px phone with 16px total padding, the available row width is ~344px. The logo is ~80px, hamburger ~40px, gaps ~12px = ~212px remaining. 44% of 344px ≈ 151px, which is roughly half of the previous `flex-1` expansion (~212px). Removing `flex-1` prevents infinite growth; the `max-w` cap ensures it never crowds the logo.

- [ ] **Step 4: Verify the fix visually**

Start the dev server and check at 320px, 360px, 375px, and 414px viewport widths:
```bash
cd /Users/apple/Downloads/CAG && npm run dev
```
Open `http://localhost:4321` in browser dev tools → toggle device toolbar → test at:
- iPhone SE: 375×667
- Galaxy S8: 360×740
- iPhone 12 Pro: 390×844
- Small Android: 320×568

Expected: Logo stays fixed left, search bar stays in middle without overlapping logo, hamburger stays fixed right. No layout shift between viewport widths.

- [ ] **Step 5: Commit**

```bash
git add src/components/Header.astro
git commit -m "fix: constrain mobile search bar width to prevent logo collision on small screens"
git push
```

---

## Task 2: Add AI Crawler Directives to robots.txt (GEO)

**Files:**
- Modify: `public/robots.txt`
- Note: `site/content/robots.txt` is a secondary copy — update it too for consistency

- [ ] **Step 1: Append AI crawler rules to `public/robots.txt`**

Current file ends at line 14 (Sitemap entries). Append after the last line:

```
# Allow all major AI crawlers for GEO (Generative Engine Optimization)
User-agent: GPTBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Bytespider
Disallow: /
```

Full resulting `public/robots.txt`:
```
User-agent: *
Allow: /

# Block low-value WordPress artifacts (from Simply Static export)
Disallow: /wp-admin/
Disallow: /wp-includes/
Disallow: /form/
Disallow: /tag/
Disallow: /thank-you/
Disallow: /?s=
Disallow: /attachment/

# Block internal preview directories
Disallow: /_previews/

# Sitemaps
Sitemap: https://congoafricangreys.com/sitemap_index.xml
Sitemap: https://congoafricangreys.com/sitemap.xml

# Allow all major AI crawlers for GEO (Generative Engine Optimization)
User-agent: GPTBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Bytespider
Disallow: /
```

- [ ] **Step 2: Mirror the change to `site/content/robots.txt`**

Apply the identical append to `site/content/robots.txt`.

- [ ] **Step 3: Verify robots.txt is correct**

```bash
cat /Users/apple/Downloads/CAG/public/robots.txt
```

Expected: Both Sitemap entries present, AI crawler block at bottom, Bytespider has `Disallow: /`.

- [ ] **Step 4: Commit and push**

```bash
git add public/robots.txt site/content/robots.txt
git commit -m "seo: add AI crawler allow rules for GEO optimization (GPTBot, ClaudeBot, Perplexity, etc.)"
git push
```

---

## Verification

**Task 1 — Header layout:**
- [ ] 320px viewport: logo + search bar + hamburger all visible, no overlap
- [ ] 375px viewport: same
- [ ] 414px viewport: same
- [ ] 1024px+ (desktop): desktop search bar visible at `w-20`, logo + nav + CTA aligned

**Task 2 — Robots.txt:**
- [ ] `curl https://congoafricangreys.com/robots.txt` after deploy shows the new AI crawler block
- [ ] GPTBot/ClaudeBot/PerplexityBot each have `Allow: /`
- [ ] Bytespider has `Disallow: /`

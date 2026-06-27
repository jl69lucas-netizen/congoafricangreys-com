---
name: cag-site-patterns
description: Proven fix patterns for CongoAfricanGreys.com (Astro + Tailwind v4). Use this skill whenever the user asks to fix colors, add search, reposition header elements, add bird listings, or references something "looking yellow", "search going to Google", "search bar in the wrong place", or "birds not showing on homepage". Contains the exact code for every fix confirmed working in production.
---

# CAG Site Patterns — Confirmed Production Fixes

All patterns below are verified: built, committed, and deployed to congoafricangreys.com.

---

## 1. Color: Gold → Clay (fix "dark yellow" text)

**Problem:** `text-gold`, `bg-gold`, `border-gold` render as the wrong color (too yellow or too bright).

**Root cause:** `--color-gold` in `src/styles/global.css` was set to a different hex than `--color-clay`.

**Fix — one line:**
```css
/* src/styles/global.css */
@theme {
  --color-gold: #e8604c;   /* must match --color-clay exactly */
  --color-clay: #e8604c;
  --color-clay-dk: #c94d3a;
  ...
}
```

That single change propagates to all 17+ files that use `text-gold`, `bg-gold`, `border-gold/30`, etc. — no per-file edits needed.

**Why it works:** Tailwind v4 uses CSS custom properties in `@theme`. Every utility class like `bg-gold` resolves at build time from `--color-gold`. Change the variable, change every instance.

---

## 2. Local Search with Pagefind (stop redirecting to Google)

**Problem:** Search forms used `action="https://www.google.com/search"` — visitors left the site.

**Solution:** Pagefind — a static site search library that indexes `dist/` after the Astro build and serves results client-side.

### Step 1: Install
```bash
npm install --save-dev pagefind
```

### Step 2: Update build script in `package.json`
```json
"build": "astro build && npx pagefind --site dist"
```

### Step 3: Externalize Pagefind from Rollup in `astro.config.mjs`
Rollup tries to resolve `/pagefind/pagefind.js` at build time but the file doesn't exist until after the build. Mark it external:
```js
vite: {
  plugins: [tailwindcss()],
  build: {
    rollupOptions: {
      external: ['/pagefind/pagefind.js']
    }
  }
},
```

### Step 4: Create `src/pages/search/index.astro`
```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
const title = "Search | CongoAfricanGreys.com";
const description = "Search the CongoAfricanGreys.com website.";
const canonical = "https://congoafricangreys.com/search/";
---
<BaseLayout {title} {description} {canonical}>
  <section class="py-16 px-4 min-h-[60vh]">
    <div class="max-w-3xl mx-auto">
      <h1 class="font-lora font-bold text-3xl text-logo-dark mb-8">Search Results</h1>
      <form action="/search/" method="get" class="flex gap-2 mb-10">
        <input id="search-refine" name="q" type="search" placeholder="Search CongoAfricanGreys.com…"
          class="flex-1 border border-stone-300 rounded-full px-4 py-2.5 text-sm text-logo-dark focus:outline-none focus:border-clay focus:ring-1 focus:ring-clay" />
        <button type="submit" class="bg-clay text-white font-semibold text-sm px-5 py-2.5 rounded-full hover:bg-clay-dk transition-colors">Search</button>
      </form>
      <div id="results" class="space-y-5"><p class="text-stone-400 text-sm">Loading…</p></div>
    </div>
  </section>
  <script>
    const params = new URLSearchParams(window.location.search);
    const q = params.get('q') ?? '';
    const refineInput = document.getElementById('search-refine') as HTMLInputElement;
    if (refineInput && q) refineInput.value = q;
    const resultsEl = document.getElementById('results')!;
    async function runSearch() {
      if (!q.trim()) { resultsEl.innerHTML = '<p class="text-stone-500 text-sm">Enter a search term above.</p>'; return; }
      let pagefind: any;
      try { pagefind = await import('/pagefind/pagefind.js'); } catch {
        resultsEl.innerHTML = '<p class="text-stone-500 text-sm">Search index not available — try after next deploy.</p>'; return;
      }
      const search = await pagefind.search(q);
      if (!search.results.length) { resultsEl.innerHTML = `<p class="text-stone-500 text-sm">No results for "<strong>${q}</strong>".</p>`; return; }
      const items = await Promise.all(search.results.slice(0, 12).map((r: any) => r.data()));
      resultsEl.innerHTML = items.map((item: any) => `
        <a href="${item.url}" class="block border border-stone-200 rounded-xl p-5 hover:border-clay/50 hover:shadow-sm transition-all group">
          <div class="font-lora font-semibold text-logo-dark text-lg group-hover:text-clay transition-colors mb-1">${item.meta?.title ?? item.url}</div>
          <div class="text-stone-500 text-sm leading-relaxed line-clamp-2">${item.excerpt ?? ''}</div>
          <div class="text-clay text-xs mt-2 font-sora">${item.url}</div>
        </a>`).join('');
    }
    runSearch();
  </script>
</BaseLayout>
```

### Step 5: Update all search forms in `src/components/Header.astro`
Change `action="https://www.google.com/search"` → `action="/search/"` and remove any `<input type="hidden" name="sitesearch" .../>`.

**CI note:** GitHub Actions runs `npm run build` which now includes pagefind. The `dist/pagefind/` directory is generated automatically — no CI changes needed.

---

## 3. Header Search Bar Positioning

### Desktop search LEFT (next to logo)
Group Logo + search in a left flex div. Inquire Now stands alone on the right.

```html
<div class="flex items-center justify-between h-16">

  <!-- Left: Logo + desktop search as a unit -->
  <div class="flex items-center gap-3">
    <Logo />
    <form action="/search/" method="get" class="hidden lg:flex gap-2">
      <input name="q" type="search" placeholder="Search…"
        class="w-40 bg-white/10 border border-white/30 text-white placeholder:text-white/50 rounded-full px-3 py-1.5 text-xs focus:outline-none focus:border-clay" />
      <button type="submit" class="bg-clay text-white text-xs font-semibold px-3 py-1.5 rounded-full hover:bg-clay-dk transition-colors">Go</button>
    </form>
  </div>

  <!-- Desktop nav (center) -->
  <nav class="hidden lg:flex items-center gap-5 text-sm font-sora font-medium">
    {nav links...}
  </nav>

  <!-- Inquire Now (desktop/tablet, right) -->
  <a href="/contact-us/" class="hidden sm:inline-flex items-center gap-2 bg-clay text-white font-semibold text-sm px-5 py-2 rounded-full hover:bg-clay-dk transition-colors">
    Inquire Now
  </a>

  <!-- Mobile search (between logo and hamburger) -->
  <form action="/search/" method="get" class="flex lg:hidden flex-1 mx-3">
    <div class="flex w-full gap-2">
      <input name="q" type="search" placeholder="Search…"
        class="flex-1 bg-white/10 border border-white/30 text-white placeholder:text-white/50 rounded-full px-3 py-1.5 text-xs focus:outline-none focus:border-clay" />
      <button type="submit" class="bg-clay text-white text-xs font-semibold px-3 py-1.5 rounded-full hover:bg-clay-dk transition-colors">Go</button>
    </div>
  </form>

  <!-- Mobile hamburger -->
  <details class="lg:hidden relative">...</details>

</div>
```

**Key breakpoint logic:**
- `hidden lg:flex` on desktop search = shows only on lg+ (1024px+)
- `flex lg:hidden` on mobile search = shows on xs/sm/md, hides on lg+
- `hidden sm:inline-flex` on Inquire Now = hides on xs (< 640px), shows on sm+

---

## 4. Available Birds Listing on Homepage

**Data source:** `data/bird-inventory.json` — array of birds with `id`, `name`, `sex`, `price_display`, `status`, `notes`.

**Placement:** After `<TrustBar />`, before the Variants section in `src/pages/index.astro`.

### Frontmatter data array (read from bird-inventory.json or hardcode):
```js
const birds = [
  { id: 'amie',  name: 'Amie',  sex: 'Female', age: '11 mo', price: '$2,700', tag: 'New Arrival',   notes: 'Premium hand-raised female, advanced training' },
  { id: 'joys',  name: 'Joys',  sex: 'Female', age: '2 yr',  price: '$2,200', tag: 'Top Talker',    notes: 'Vocal female, actively learning new words' },
  { id: 'roys',  name: 'Roys',  sex: 'Male',   age: '3 yr',  price: '$2,000', tag: 'Family Bird',   notes: 'Energetic male, great with families' },
  { id: 'carl',  name: 'Carl',  sex: 'Male',   age: '1 yr',  price: '$2,500', tag: 'Talking Now',   notes: 'Highly interactive, vocabulary developing fast' },
  { id: 'loti',  name: 'Loti',  sex: 'Male',   age: '5 yr',  price: '$1,800', tag: 'Calm & Social', notes: 'Mature male, apartment-friendly' },
  { id: 'bery',  name: 'Bery',  sex: 'Female', age: '4 yr',  price: '$1,600', tag: 'Best Value',    notes: 'Gentle female, easy temperament' },
];
```

### Section HTML:
```astro
<section class="py-16 px-4 bg-warm-white">
  <div class="max-w-7xl mx-auto">
    <div class="flex items-end justify-between mb-10 gap-4 flex-wrap">
      <div>
        <p class="text-clay font-sora text-xs font-semibold uppercase tracking-widest mb-2">This Week's Aviary</p>
        <h2 class="font-lora font-bold text-3xl text-logo-dark">Birds Available Right Now</h2>
        <p class="text-stone-500 mt-2 max-w-md text-sm leading-relaxed">
          Every bird is hand-fed, DNA-sexed, CITES-documented, and vet-certified before reservation.
        </p>
      </div>
      <a href="/african-grey-parrot-for-sale/" class="text-sm font-semibold text-clay hover:text-clay-dk border border-clay/40 hover:border-clay px-4 py-2 rounded-full transition-colors whitespace-nowrap">
        View all birds &rarr;
      </a>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {birds.map(bird => (
        <article class="bg-white rounded-2xl overflow-hidden shadow-sm border border-stone-100 flex flex-col hover:shadow-md transition-shadow">
          <div class="relative bg-green/10 h-48 overflow-hidden">
            <img src="/african-grey-hero.webp" alt={`${bird.name} — ${bird.sex} Congo African Grey`}
              class="w-full h-full object-cover object-center" loading="lazy" />
            <span class="absolute top-3 left-3 bg-clay text-white text-xs font-semibold px-3 py-1 rounded-full">{bird.tag}</span>
          </div>
          <div class="p-5 flex flex-col flex-1">
            <div class="flex items-baseline justify-between mb-1">
              <h3 class="font-lora font-bold text-xl text-logo-dark">{bird.name}</h3>
              <span class="text-stone-400 text-xs font-sora">📍 Midland, TX</span>
            </div>
            <p class="text-stone-500 text-xs font-sora mb-3">{bird.sex} · {bird.age} · Congo African Grey</p>
            <p class="text-stone-600 text-sm leading-relaxed mb-4 flex-1">{bird.notes}</p>
            <div class="flex items-center justify-between mt-auto pt-4 border-t border-stone-100">
              <span class="font-lora font-bold text-2xl text-clay">{bird.price}</span>
              <a href={`/contact-us/?bird=${bird.id}`}
                class="bg-clay text-white text-xs font-semibold px-4 py-2 rounded-full hover:bg-clay-dk transition-colors">
                Inquire
              </a>
            </div>
          </div>
        </article>
      ))}
    </div>
    <p class="text-center text-stone-400 text-xs mt-8 font-sora">
      All birds include CITES captive-bred certificate · DNA sex certificate · Avian vet health certificate · Hatch certificate
    </p>
  </div>
</section>
```

**To add real bird photos:** add a `photo` field to each entry in `data/bird-inventory.json` and replace `/african-grey-hero.webp` with `{bird.photo}` in the `<img src>`.

**To mark a bird as reserved/sold:** add `status: "reserved"` or `status: "sold"` in `data/bird-inventory.json`, then filter in the frontmatter: `birds.filter(b => b.status === 'available')`.

---

## Deploy checklist after any of these changes

```bash
npm run build          # must exit 0 with 18 pages built + pagefind index
git add <files>
git commit -m "..."
git push origin main   # triggers GitHub Actions → Cloudflare Pages deploy (~2-3 min)
```

Monitor: https://github.com/jl69lucas-netizen/congoafricangreys-com/actions

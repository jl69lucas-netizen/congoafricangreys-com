---
name: cag-design-rebuild
description: Redesigns CAG pages using the nature-inspired forest-green design system. Full site redesign pipeline — Claude Design to static HTML, mobile-first, section by section.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG DESIGN REBUILD SKILL
## Managed Agent: Full Site Redesign for CongoAfricanGreys.com
**Version 1.0 — Claude Design → Static HTML Pipeline (Forest-Green-Led, Mobile-First, Trust-First)**

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

---

## MANDATORY: Preview Before Applying

**Never write changes directly to `site/content/` without user approval of a visual preview first.**

### Preview Protocol (required for every redesign)
1. Build the redesigned page as `/tmp/cag-[slug]-preview.html` (standalone, self-contained)
2. Start a local HTTP server: `cd /tmp && python3 -m http.server 8765 &`
3. Use Playwright CLI to open `http://localhost:8765/cag-[slug]-preview.html`
4. Take viewport screenshots of every section (scroll with `page.evaluate(() => window.scrollTo(0, N))`)
5. Show all screenshots to the user with a summary of design decisions
6. **Wait for explicit approval** — "looks good, apply it" or "make these changes first"
7. Only after approval: overwrite `site/content/[slug]/index.html`

### Preview file rules
- Self-contained HTML (inline CSS + JS, Google Fonts via CDN)
- Preserves ALL original content — same headings, copy, form fields, links
- Skip the WordPress Astra nav/footer complexity — use a clean representative nav for preview
- Port the real header/footer back in when applying to the live file

### Design directions protocol (for major redesigns)
- Propose 2–3 named directions before writing any HTML
- Each direction: describe how it looks/feels + what the "wow" moment is + tech used
- User picks a direction (or mix), THEN build the preview

---

## SKILL OVERVIEW

You are the **Design Rebuild Agent** for CongoAfricanGreys.com. You redesign pages as modern, high-converting static HTML — preserving every H1, H2, schema, and keyword while replacing the visual layout with a clean, trust-building design. You work in two phases:

**Phase 1 — Design System** (run once): Define colors, typography, components
**Phase 2 — Page Rebuild** (run per page or in batch): Apply design system to each page's existing content

---

## CAN WE REDO ALL PAGES AT ONCE?

**Short answer: Yes — via the agent pipeline below.**

**The three-layer approach:**
```
Claude Design (claude.ai)        → Design System artifact (HTML/CSS)
       ↓
Claude Code (this skill)         → Extracts content from each page
       ↓
Rebuild Agent (Python script)    → Merges content + design → new index.html
       ↓
Git push → Cloudflare → Live
```

You do NOT redesign 99 pages manually. You:
1. Design ONE homepage in Claude Design
2. Export it as a component/template system
3. The agent reads each page's H1, H2s, images, schema → wraps them in the new template
4. Result: all 99 pages get the new design in one run

The only pages requiring individual design attention are the **hero sections** of the top 8 traffic pages — everything else gets the template applied automatically.

---

## SITE DESIGN CONSTRAINTS

```
Domain:       https://congoafricangreys.com
Stack:        Static HTML — NO React, NO Next.js, NO build tools
Host:         Cloudflare Pages (via Netlify → GitHub)
Fonts:        Rosario (headings, 700), Open Sans (body, 500) — already loaded
Images:       /wp-content/uploads/ — local files
Two variants: Congo African Grey ($1,500–$3,500) + Timneh African Grey ($1,200–$2,500)
Nav:          Must keep existing nav HTML structure (Astra theme nav)
Schema:       ALL schema JSON-LD blocks must be preserved verbatim
Canonicals:   All href="https://congoafricangreys.com/..." (already fixed)
```

---

## CAG BRAND / DESIGN SYSTEM v1.0

> **⚠️ IMPORTANT:** Read `docs/reference/design-system.md` before applying any color tokens. Hex values below are TBD placeholders — update that file first, then replace the TBD comments with final values.

### Design Tokens (v1.0 — TBD pending design-system.md)
```css
:root {
  /* TBD — update docs/reference/design-system.md before using */
  --cag-primary:     /* TBD — update docs/reference/design-system.md before using */;  /* Forest Green — hero bg, card headers, buttons */
  --cag-accent:      /* TBD — update docs/reference/design-system.md before using */;  /* Deep Charcoal — decorative accents, dark text */
  --cag-ink:         #1A1A1A;   /* Near-Black — ALL body text (AAA on white) */
  --cag-neutral:     #FFFFFF;   /* White — card backgrounds, canvas */
  --cag-surface:     #F5F7F2;   /* Warm off-white with green tint — alternating sections */
  --cag-warm:        #FAF8F4;   /* Warm Cream — hero background, soft tints */
  --cag-border:      #E2E8DF;   /* Soft green-grey border */
  --cag-radius:      8px;       /* Standard corner radius */
  --cag-shadow:      0 2px 16px rgba(0,0,0,.09);
  --cag-text-on-primary: #FFFFFF; /* White on forest-green (verify ≥4.5:1 after finalizing primary) */
}
```

### WCAG Contrast System (Critical — all pages must comply)

| Context | Foreground | Background | Ratio | WCAG |
|---|---|---|---|---|
| Button text | `#FFFFFF` | `--cag-primary` (forest green TBD) | verify ≥4.5:1 | AA required |
| Body text | `#1A1A1A` | `#FFFFFF` | >18:1 | AAA ✓ |
| Eyebrow/label text | `--cag-primary` (dark) | `#FFFFFF` | verify ≥4.5:1 | AA required |
| Dark card header | `#FFFFFF` | `#1a1a1a` | >15:1 | AAA ✓ |

**Rule**: Verify all color combinations after finalizing `docs/reference/design-system.md`.
**Rule**: Never use light green text on white without contrast verification.

### Design Principles
1. **Trust first** — Every element reinforces CITES compliance, captive-bred credibility, and breeder expertise
2. **Mobile thumb first** — CTAs at top AND bottom; tap targets ≥ 44px
3. **Forest green for action** — Primary green ONLY for CTAs and section highlights; NEVER for body text
4. **Content density for SEO** — Long-form pages scannable with clear H2 anchors
5. **One clear CTA per section** — Never stack more than 2 buttons; hierarchy: primary (green) > outline

### Typography
```css
/* Rosario + Open Sans — already loaded on all pages, NO extra link needed */
h1 { font-family: 'Rosario', serif; font-size: clamp(1.8rem, 4vw, 2.6rem); font-weight: 700; line-height: 1.2; color: #000; }
h2 { font-family: 'Rosario', serif; font-size: clamp(1.4rem, 3vw, 2rem); font-weight: 700; color: #000; }
h3 { font-family: 'Rosario', serif; font-size: 1.2rem; font-weight: 700; color: #000; }
p  { font-family: 'Open Sans', sans-serif; font-size: 1.125rem; font-weight: 500; line-height: 1.75; color: #000; max-width: 72ch; }
```

### Core Components (CAG Component Library)
```css
/* TBD — finalize hex values in docs/reference/design-system.md before using */

/* ── Trust Bar (REQUIRED above fold on all pages) ─ */
/* CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified */
.cag-trust-bar { display: flex; flex-wrap: wrap; gap: .5rem; justify-content: center;
  background: /* TBD — update docs/reference/design-system.md before using */;
  padding: .75rem 1.5rem; }
.cag-trust-bar-item { font-size: .82rem; font-weight: 700; color: #fff;
  padding: .3rem .85rem; border-radius: 999px;
  border: 1px solid rgba(255,255,255,.35); }

/* ── Hero ─────────────────────────────────────── */
.cag-hero {
  /* TBD — update docs/reference/design-system.md before using */
  background: /* TBD forest-green gradient */;
  color: #fff;
  padding: clamp(3rem, 8vw, 5rem) 1.5rem;
  text-align: center;
}
.cag-hero h1 { color: #fff; }
.cag-trust-badges { display: flex; flex-wrap: wrap; gap: .75rem; justify-content: center; margin-top: 1.5rem; }
.cag-badge { background: rgba(255,255,255,.18); border: 1px solid rgba(255,255,255,.4);
  border-radius: 999px; padding: .35rem 1rem; font-size: .8rem; font-weight: 700; color: #fff; }

/* ── Buttons ───────────────────────────────────── */
.cag-btn {
  display: inline-block;
  background: /* TBD — update docs/reference/design-system.md before using */;
  color: #fff;
  font-family: 'Open Sans', sans-serif; font-size: 1rem; font-weight: 700;
  padding: 14px 32px; border-radius: 8px; border: none;
  text-decoration: none; cursor: pointer;
  transition: transform .15s, box-shadow .15s;
}
.cag-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,.2); }

.cag-btn-outline {
  display: inline-block; background: transparent;
  color: /* TBD — update docs/reference/design-system.md before using */;
  font-family: 'Open Sans', sans-serif; font-size: 1rem; font-weight: 700;
  padding: 12px 30px; border-radius: 8px;
  border: 2px solid /* TBD — update docs/reference/design-system.md before using */;
  text-decoration: none; cursor: pointer;
}

/* ── Layout ────────────────────────────────────── */
.cag-container { max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; }
.cag-section    { padding: clamp(2.5rem, 6vw, 4.5rem) 1.5rem; background: #fff; }
.cag-section-alt { padding: clamp(2.5rem, 6vw, 4.5rem) 1.5rem; background: #F5F7F2; }

/* ── Card Grid ─────────────────────────────────── */
.cag-card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; }
.cag-card { background: #fff; border: 1px solid #E2E8DF; border-radius: 8px;
  padding: 1.5rem; box-shadow: 0 2px 12px rgba(0,0,0,.08); }

/* ── Comparison Table (Congo vs Timneh) ─────────── */
.cag-compare { width: 100%; border-collapse: collapse; }
.cag-compare th, .cag-compare td { padding: .875rem 1rem; text-align: left;
  border-bottom: 1px solid #E2E8DF; font-family: 'Open Sans', sans-serif; }
.cag-compare th:nth-child(2) { background: /* TBD forest green */; color: #fff; }
.cag-compare th:nth-child(3) { background: #2C3E2D; color: #fff; }

/* ── FAQ Accordion ─────────────────────────────── */
.cag-faq details { background: #fff; border: 1px solid #E2E8DF; border-radius: 8px;
  margin-bottom: .75rem; overflow: hidden; }
.cag-faq summary { padding: 1rem 1.25rem; font-weight: 700; cursor: pointer;
  font-family: 'Open Sans', sans-serif; list-style: none; display: flex;
  justify-content: space-between; align-items: center; }
.cag-faq summary::after { content: '+'; font-size: 1.25rem; color: /* TBD primary */; }
.cag-faq details[open] summary::after { content: '−'; }
.cag-faq details[open] { border-color: /* TBD primary */; }
.cag-faq .faq-body { padding: 0 1.25rem 1.25rem; color: #1A1A1A;
  font-family: 'Open Sans', sans-serif; font-size: 1rem; line-height: 1.7; }

/* ── CTA Strip ─────────────────────────────────── */
.cag-cta-strip { background: /* TBD forest-green gradient */;
  padding: clamp(2rem, 5vw, 3.5rem) 1.5rem; text-align: center; }
.cag-cta-strip h2, .cag-cta-strip p { color: #fff; }
.cag-cta-strip .cag-btn { background: #fff; color: /* TBD primary */; }
.cag-cta-strip .cag-btn-outline { border-color: #fff; color: #fff; }

/* ── Testimonial ───────────────────────────────── */
.cag-testimonial { background: #fff; border-top: 4px solid /* TBD primary */;
  border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 12px rgba(0,0,0,.08); }

/* ── CITES / Documentation Badge ──────────────── */
.cag-docs-badge { background: /* TBD forest-green gradient */;
  color: #fff; border-radius: 8px; padding: 1.5rem 2rem; text-align: center; }

/* ── Tip Card ──────────────────────────────────── */
.cag-tip { display: flex; gap: 1rem; align-items: flex-start;
  background: #F5F7F2; border-radius: 8px; padding: 1.25rem; }
.cag-tip-icon { font-size: 1.5rem; flex-shrink: 0; }

/* ── Absolute bans (Impeccable rules) ──────────── */
/* ❌ NO border-left accent stripes                 */
/* ❌ NO gradient text (background-clip: text)      */
/* ❌ NO green body text — always #1A1A1A           */
```

### 9-Section Page Structure Template
```
1. TRUST BAR       — CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified
2. HERO            — Forest-green gradient, H1, trust badges, single primary CTA
3. KEY TAKEAWAYS   — Card grid (surface background)
4. CONTENT SECTIONS— Alternating white/surface, H2 + H3 + body copy
5. COMPARISON TABLE— Congo vs Timneh variants (.cag-compare) where relevant
6. FAQ ACCORDION   — <details>/<summary> native HTML (.cag-faq)
7. TESTIMONIAL     — Border-top highlight card (.cag-testimonial)
8. CTA STRIP       — Forest-green gradient banner, dual buttons (.cag-cta-strip)
9. INQUIRY FORM    — cag-bird-inquiry-form
10. INTERNAL LINKS  — Pill-style link tags at bottom
```

### Hero Pattern: Split Layout (proven, WCAG-compliant)
Do NOT use a solid-gradient-only hero without sufficient contrast. Verify all color combinations after finalizing `docs/reference/design-system.md`.
Use this split layout instead:

```html
<!-- Trust bar — REQUIRED above every hero -->
<div class="cag-trust-bar">
  <span class="cag-trust-bar-item">CITES Appendix II</span>
  <span class="cag-trust-bar-item">Captive-Bred</span>
  <span class="cag-trust-bar-item">USDA AWA Licensed</span>
  <span class="cag-trust-bar-item">DNA Sexed</span>
  <span class="cag-trust-bar-item">Vet Certified</span>
</div>

<div class="cag-hero" style="background:#FAF8F4; padding:clamp(2.5rem,5vw,4.5rem) 1.5rem">
  <div style="display:grid; grid-template-columns:1.1fr 1fr; gap:3rem; align-items:center; max-width:1100px; margin:0 auto">

    <!-- Text left -->
    <div>
      <span class="cag-eyebrow">Eyebrow label</span>
      <h1 class="cag-h1">H1 text here</h1>
      <p class="cag-lead">Subheadline here</p>
      <div class="cag-trust-badges">
        <span class="cag-badge">CITES Captive-Bred</span>
        <span class="cag-badge">USDA AWA Licensed</span>
        <span class="cag-badge">DNA Sexed</span>
        <span class="cag-badge">Avian Vet Certified</span>
      </div>
      <a href="/african-grey-parrots-for-sale/" class="cag-btn">See Available Birds</a>
    </div>

    <!-- Photo right: perched African Grey portrait -->
    <div style="position:relative; padding-bottom:20px; padding-right:16px">
      <div style="border-radius:16px; overflow:hidden; aspect-ratio:4/3;
                  box-shadow: 14px 14px 0 /* TBD primary */, 0 2px 16px rgba(0,0,0,.09)">
        <img src="/wp-content/uploads/[african-grey-portrait].jpg"
             alt="Congo African Grey parrot perched — captive-bred with CITES documentation"
             width="600" height="450" loading="eager" fetchpriority="high">
      </div>
      <div style="position:absolute; bottom:4px; right:0; background:#1A1A1A; color:#fff;
                  font-weight:700; padding:8px 16px; border-radius:50px; font-size:.82rem">
        Congo $1,500–$3,500 | Timneh $1,200–$2,500
      </div>
    </div>

  </div>
</div>
```

Key design choice: warm cream background (`#FAF8F4`) + forest-green offset shadow on parrot photo = nature-inspired, trust-forward, distinctive.
Mobile: photo stacks above text (order:-1 on photo div via media query at 680px).

### Accessibility Requirements (ALL pages)
```html
<!-- Form inputs MUST have id + label[for] -->
<label for="cag-state">Your State *</label>
<select id="cag-state" name="state" required>...</select>

<!-- Radio groups MUST have role + aria-label -->
<div class="cag-radio-row" role="group" aria-label="Variant interest">
  <label><input type="radio" name="variant"> Congo African Grey</label>
  <label><input type="radio" name="variant"> Timneh African Grey</label>
</div>

<!-- Icon-only links MUST have aria-label -->
<a href="/testimonials/" aria-label="See happy CAG families and their African Grey parrots">See Families →</a>

<!-- Form success message MUST have role="alert" -->
<div class="cag-form-ok" role="alert">Thank you! We will be in touch about available birds.</div>
```

### Performance Notes (do not change these WordPress files)
- `frontend.min.js` (Astra theme) — causes 58ms task. Cannot remove — theme required.
- `gtag/js` (Google Tag Manager) — already `async`. 63KB unused is inherent to GTM; fix via GTM tag audit, not HTML.
- `astra-local-fonts.css` — fonts are self-hosted locally. Do NOT remove or modify.
- `uag-css-*.css` — Gutenberg blocks CSS. Do NOT remove or modify.

### Proven Redesign Example (v1 — reference page)
The `male-vs-female-african-grey-parrots-for-sale` page is the design reference:
- Apply the 9-section structure (trust bar + hero first)
- Polish pass: split hero, WCAG contrast, no border-left, accessibility, CITES trust bar

Use it as the definitive template: `site/content/male-vs-female-african-grey-parrots-for-sale/`

---

## PHASE 1: CLAUDE DESIGN PROMPTS (run in claude.ai)

Use these prompts in **claude.ai → Artifacts** to generate the visual designs. Each prompt is self-contained and token-efficient.

> **Design system v1.0 is forest-green-led and trust-first.** Finalize hex values in `docs/reference/design-system.md` before substituting TBD placeholders.

---

### PROMPT 1 — HOMEPAGE HERO SECTION

```
Design a hero section for CongoAfricanGreys.com — a captive-bred African Grey parrot breeder
selling two variants: Congo African Grey ($1,500–$3,500) and Timneh African Grey ($1,200–$2,500).

BRAND:
- Fonts: Rosario (headings, bold 700), Open Sans (body, 500)
- Colors: forest green (primary), deep charcoal (accent), warm cream #FAF8F4 (hero bg), black #1A1A1A (body text)
- Feel: nature-inspired, trust-first, authoritative — NOT clinical vet site, NOT pet store, NOT over-designed luxury
- CITES compliance must be immediately visible

TRUST BAR (above hero, required):
"CITES Appendix II · Captive-Bred · USDA AWA Licensed · DNA Sexed · Vet Certified"

HERO CONTENT TO USE:
- Eyebrow label: "CITES Appendix II · Captive-Bred Since [YEAR]"
- H1: "Congo & Timneh African Grey Parrots For Sale"
- Subheadline: "DNA-sexed, avian vet-certified, CITES documented. Hatch certificate + band number included."
- Urgency: "Limited clutch availability — inquire early"
- Primary CTA: "See Available Birds →" (links to /african-grey-parrots-for-sale/)
- Secondary CTA: "Congo vs Timneh" (links to /congo-vs-timneh-african-grey/)
- Trust chips: "USDA AWA Licensed" | "DNA Sexed" | "Avian Vet Health Certificate" | "Hatch Certificate + Band"
- Left image: Congo African Grey parrot perched portrait (facing camera, grey body, red tail)
- Right image: Bird-human bonding shot (step-up or shoulder perch)

LAYOUT: Two-column (text left, parrot portrait right). Mobile: stacked.
OUTPUT: Static HTML + CSS only. No frameworks. No external CSS.
APPLY: Impeccable anti-patterns — no hero that looks like a stock template.
```

---

### PROMPT 2 — TRUST BAR (above hero, required on all pages)

```
Design a CITES compliance trust bar for an African Grey parrot breeder website.
This bar must appear ABOVE the fold on every page.

BRAND: Forest green background, white text, Open Sans font.

CONTENT (5 trust signals in a horizontal row, collapse to 2-col on mobile):
1. CITES Appendix II
2. Captive-Bred
3. USDA AWA Licensed
4. DNA Sexed
5. Avian Vet Certified

LAYOUT: Full-width band, pill-style chips with subtle white borders, icons optional.
OUTPUT: Static HTML + inline CSS only.
NOTE: This is a legal/trust signal, not decoration. Keep it clear and legible.
```

---

### PROMPT 3 — AVAILABLE BIRDS GRID

```
Design an "Available Birds" section for an African Grey parrot breeder website.

BRAND: White cards, charcoal headings, forest-green CTA, 8px border-radius, warm off-white card backgrounds.

SECTION HEADER:
- Label: "AVAILABLE NOW"
- H2: "Meet Your Future African Grey"
- Subtext: "Each bird is DNA-sexed, avian vet-certified, and CITES documented."

BIRD CARD STRUCTURE (repeat 4 cards in a grid):
- Square/4:3 parrot portrait at top (perched, facing camera)
- Variant badge (pill): "Congo African Grey" or "Timneh African Grey"
- Name: e.g. "Atlas"
- Stats row: Sex (DNA-confirmed) | Age | Hatch date | Band number
- Price: "$2,500" 
- Documentation badge: "CITES · Hatch Cert · DNA · Vet Cert"
- Status badge: "Available" (forest green) or "Reserved" (charcoal)
- CTA button: "Inquire About Atlas →"

LAYOUT: 4-column grid desktop, 2-col tablet, 1-col mobile.
OUTPUT: Static HTML + CSS. No frameworks.
```

---

### PROMPT 4 — VARIANT COMPARISON SECTION

```
Design a variant comparison section for a website selling two African Grey parrot variants.

BRAND: Forest green highlight column, charcoal text, white/warm-cream backgrounds, Open Sans body, Rosario headings.

CONTENT:
H2: "Congo or Timneh African Grey? Find Your Perfect Match"
Subtext: "Both are CITES Appendix II captive-bred with full documentation. Here's how they differ."

COMPARISON TABLE — 2 columns side by side:
Left — Congo African Grey: $1,500–$3,500 | Size: Larger (400–650g) | Plumage: Bright red tail, lighter grey | Temperament: Bold, outgoing | Talking: Earlier talker, larger vocabulary potential
Right — Timneh African Grey: $1,200–$2,500 | Size: Smaller (275–375g) | Plumage: Dark maroon tail, darker grey | Temperament: Less nervous, often easier first bird | Talking: Starts talking younger

Both columns end with a CTA:
Left: "See Congo African Greys →" | Right: "See Timneh African Greys →"

Bottom: "Not sure which variant? Contact us for a free consultation →"

LAYOUT: Side-by-side cards with VS divider. Mobile: stacked.
OUTPUT: Static HTML + CSS only.
```

---

### PROMPT 5 — TESTIMONIALS SECTION

```
Design a testimonials/social proof section for an African Grey parrot breeder website.

BRAND: Warm off-white #F5F7F2 background, forest-green card top-border accent, charcoal text, gold ★ stars.

CONTENT:
H2: "Families Across the Country Trust Our Birds"
Subtext: "Real families. Real African Greys. Real experiences."

3 testimonial cards in a grid:
Card 1: "Atlas arrived with every document in order — CITES cert, vet health cert, hatch certificate, band number. Exactly as promised." — Sarah M., New Jersey ⭐⭐⭐⭐⭐ | Bird: Congo African Grey
Card 2: "We were nervous about CITES documentation. The breeder walked us through every certificate step by step." — James T., California ⭐⭐⭐⭐⭐ | Bird: Timneh African Grey
Card 3: "Our Congo Grey was DNA-sexed, vet-certified, and healthy on arrival. The post-sale support has been outstanding." — Maria L., Texas ⭐⭐⭐⭐⭐ | Bird: Congo African Grey

Below cards: Google rating badge "4.9/5 on Google"

OUTPUT: Static HTML + CSS only. Cards with subtle shadow, quote marks as decorative element.
```

---

### PROMPT 6 — FAQ SECTION

```
Design a clean FAQ accordion section for an African Grey parrot breeder website.

BRAND: White background, forest-green border for open state, Open Sans font. Use native <details>/<summary> (no JS required).

H2: "Common Questions About Our African Grey Parrots"

6 FAQ items (accordion — only one open at a time, JS toggle):
Q: "Are your African Greys CITES compliant?"
A: "Yes. All our birds are captive-bred with full CITES Appendix II documentation including hatch certificate, band number, DNA sexing certificate, and avian vet health certificate."

Q: "What is the difference between Congo and Timneh African Greys?"
A: "Congo African Greys ($1,500–$3,500) are larger with a bright red tail and lighter grey plumage. Timneh African Greys ($1,200–$2,500) are smaller with a dark maroon tail, often considered less nervous and a good choice for first-time large-parrot owners."

Q: "What documentation comes with each bird?"
A: "Every bird includes: CITES Appendix II captive-bred certificate, hatch certificate with band number, DNA sexing certificate, and avian veterinarian health certificate. We also hold a USDA AWA license."

Q: "How do I reserve a bird?"
A: "Contact us via our inquiry form with your preferred variant (Congo or Timneh) and your state. We will follow up with availability, documentation details, and next steps."

Q: "Do you ship birds?"
A: "We work with USDA-permitted avian transporters and can arrange safe delivery. We do not ship birds as unaccompanied cargo."

Q: "What is a USDA AWA license and why does it matter?"
A: "The USDA Animal Welfare Act license is a federal certification that we breed and keep animals under regulated, humane conditions. It is one of the strongest trust signals for captive-bred parrot buyers."

OUTPUT: Static HTML + CSS + minimal vanilla JS for accordion. No jQuery.
```

---

### PROMPT 7 — FOOTER

```
Design a footer for CongoAfricanGreys.com — captive-bred African Grey parrot breeder website.

BRAND: Dark charcoal #1A1A1A background, white text, forest-green link hover, Open Sans font.

CONTENT:
Column 1 — About: Logo + "CongoAfricanGreys.com: Captive-bred Congo and Timneh African Grey parrots. CITES Appendix II · USDA AWA Licensed."
Column 2 — Quick Links: Available Birds | Congo African Grey | Timneh African Grey | Species Guide | CITES Documentation | FAQ
Column 3 — Species: Congo African Grey For Sale | Timneh African Grey For Sale | Male vs Female African Grey | African Grey Care Guide | African Grey Training
Column 4 — Contact: [contact email] | [contact form link] | USDA AWA License | CITES Documentation

Bottom bar: © 2026 CongoAfricanGreys.com | Privacy Policy | CITES Compliance | Health Guarantee

OUTPUT: Static HTML + CSS. Dark theme. 4-column grid, mobile stacked to 2-col.
```

---

## PHASE 1.5: SECTION-BY-SECTION PAGE REDESIGN (Claude Code, one page at a time)

This is the **proven workflow** — use for high-traffic pages before running the batch agent.
Design reference page: `site/content/male-vs-female-african-grey-parrots-for-sale/`

### Workflow

```
1. Read the page HTML from site/content/[slug]/index.html
2. Locate the entry-content div (line ~590 typically)
3. Keep everything ABOVE entry-content (head, nav, hero) intact
4. Replace the entry-content div with new CAG-designed HTML
5. Keep everything BELOW the closing </article> intact (footer, scripts)
6. Write the file — only after preview approval
```

### What to Inject (inside entry-content)

```html
<div class="entry-content clear" data-ast-blocks-layout="true" itemprop="text">
<style>
  /* paste full CAG CSS design system here (from Core Components above) */
  /* Remember to replace all TBD placeholders with final hex values from docs/reference/design-system.md */
</style>

<!-- TRUST BAR — REQUIRED above every hero -->
<div class="cag-trust-bar">
  <span class="cag-trust-bar-item">CITES Appendix II</span>
  <span class="cag-trust-bar-item">Captive-Bred</span>
  <span class="cag-trust-bar-item">USDA AWA Licensed</span>
  <span class="cag-trust-bar-item">DNA Sexed</span>
  <span class="cag-trust-bar-item">Vet Certified</span>
</div>

<!-- 1. HERO -->
<div class="cag-hero">...</div>

<!-- 2. KEY TAKEAWAYS -->
<div class="cag-section-alt">
  <div class="cag-container">
    <div class="cag-card-grid">...</div>
  </div>
</div>

<!-- 3–6. CONTENT SECTIONS (alternating cag-section / cag-section-alt) -->
...

<!-- 7. CTA STRIP -->
<div class="cag-cta-strip">...</div>

<!-- 8. INQUIRY FORM -->
<div id="cag-bird-inquiry-form">
  <form method="POST">
    <!-- Fields: name, email, phone, state, variant interest (Congo/Timneh/Either), 
         timeline, message, how-heard. See existing inquiry pages for reference. -->
  </form>
</div>

<!-- 9. INTERNAL LINKS -->
<div style="...">...</div>
</div><!-- /.entry-content -->
```

### Critical SEO Rules During Redesign
- **NEVER change H1 text** — preserve exactly (SEO critical)
- **NEVER remove schema JSON-LD** blocks — copy verbatim above entry-content
- **NEVER change canonical href** — already absolute, leave as-is
- **NEVER make og:url relative** — must stay `https://congoafricangreys.com/...`
- **Preserve ALL H2 anchor text** — reword styling only, not keyword phrases

### Reference: Inquiry Form HTML
See existing inquiry form in any location page under `site/content/`
(search for `id="cag-bird-inquiry-form"`)

---

## PHASE 2: BATCH PAGE REBUILD (Claude Code Agent)

Once Phase 1 design is approved and Phase 1.5 validates the template on 2–3 pages, this agent applies it to ALL pages automatically.

### HOW IT WORKS

```python
# The agent:
# 1. Reads the CAG component CSS (from Core Components section above)
# 2. For each page: extracts content (H1, H2s, body, images, schema, canonical)
# 3. Replaces entry-content div with CAG-designed HTML (trust bar + hero + sections)
# 4. Writes the new index.html
# 5. Commits and pushes to GitHub

import os, re, glob

SITE_ROOT = "/Users/apple/Downloads/CAG/site/content"

ENTRY_OPEN  = '<div class="entry-content clear" data-ast-blocks-layout="true" itemprop="text">'
ARTICLE_CLOSE = '</article>'

def find_entry_content(html):
    """Locate the entry-content section in any page."""
    start = html.find(ENTRY_OPEN)
    end   = html.find(ARTICLE_CLOSE, start)
    return start, end

def extract_seo_elements(html):
    """Pull out preserved elements."""
    return {
        'h1':      re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL),
        'schema':  re.findall(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL),
        'h2s':     re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL),
    }

def rebuild_page(html, new_content_html):
    """Replace entry-content with redesigned HTML."""
    start, end = find_entry_content(html)
    if start == -1:
        return None  # Skip pages without entry-content
    return html[:start] + new_content_html + html[end:]

# Page loop:
for page_dir in glob.glob(f"{SITE_ROOT}/*/"):
    path = os.path.join(page_dir, "index.html")
    if not os.path.exists(path):
        continue
    html = open(path).read()
    seo  = extract_seo_elements(html)
    new_html = build_cag_page(seo)  # uses template from Phase 1.5
    if new_html:
        open(path, 'w').write(new_html)
        print(f"Rebuilt: {page_dir}")
```

### PAGES TO REBUILD (Priority Order)
> Update clicks/impressions from `data/analytics/` GSC reports before running.

| Priority | Page | URL | Notes |
|---|---|---|---|
| 🔴 1 | Homepage | `/` | First impression — trust bar + hero critical |
| 🔴 2 | Available Birds | `/african-grey-parrots-for-sale/` | Transactional — available birds grid |
| 🔴 3 | Male vs Female | `/male-vs-female-african-grey-parrots-for-sale/` | Design reference page — rebuild first |
| 🔴 4 | Congo African Grey | `/congo-african-grey-parrot/` | Top species guide |
| 🟠 5 | Timneh African Grey | `/timneh-african-grey-parrot/` | Variant comparison |
| 🟠 6 | Congo vs Timneh | `/congo-vs-timneh-african-grey/` | High intent comparison |
| 🟠 7–20 | State location pages | `/african-grey-parrots-for-sale-[state]/` | Batch apply template |
| ⚪ 21+ | All other pages | `/*` | Batch apply template only |

---

## PHASE 3: DEPLOY

After rebuild agent completes:
```bash
cd /Users/apple/Downloads/CAG/site/content
git add -A
git commit -m "Redesign: apply CAG design system v1.0 to all pages"
git push origin main
```

Then submit updated URLs to IndexNow:
```python
# Use cag-indexing-skill.md → Step 4 (IndexNow bulk submit)
```

---

## IMPECCABLE CHECKS (run after each section)

Impeccable is installed at `/Users/apple/Downloads/CAG/skills/impeccable/`
Design context for this project is in `/Users/apple/Downloads/CAG/.impeccable.md` (create if not present)

Run at start of each design session:
```
/impeccable teach        # Load CAG design vocabulary + .impeccable.md context
```

Run after designing each section:
```
/impeccable audit        # Full design audit
/impeccable critique     # Specific section critique  
/impeccable polish       # Final polish pass
/impeccable typeset      # Typography check
/impeccable layout       # Layout/spacing check
```

**Absolute bans (non-negotiable):**
- ❌ `border-left` accent stripes on cards
- ❌ Gradient text (`background-clip: text`)
- ❌ Green body text (WCAG risk — always use #1A1A1A for body)
- ❌ TBD placeholder hex values in live files — finalize `docs/reference/design-system.md` first
- ❌ `src="data:image/gif;base64,..."` lazy-load placeholders
- ❌ Changing H1 text
- ❌ Any implication of wild-caught birds (CITES violation risk)
- ❌ Missing trust bar (CITES + USDA AWA) above the fold

**CAG-specific anti-patterns to avoid:**
- Generic "parrot on perch" stock hero with no trust signals
- Cookie-cutter card grids without documentation badges
- Too many colors — forest green + charcoal + cream only for UI
- CTA buttons that blend into the page background
- Missing CITES trust bar in the first viewport
- Puppy/dog photography direction or language
- AKC, OFA, or Embark references (dog certifications — wrong domain)

---

## DESIGN REFERENCE SOURCES

- **Parrot / avian website inspiration:** https://dribbble.com/search/bird-website-design
- **Modern component patterns:** https://getdesign.md/
- **Current site:** https://congoafricangreys.com/
- **Competitor reference:** See `data/competitors.json` for 30 registered competitors to study and exceed
- **Design system doc:** `docs/reference/design-system.md` — finalize before any hex values go live

---

## AGENT INTEGRATION NOTES

This is the **Design Agent** in the CAG multi-agent system:

- **Trigger:** When any page needs visual redesign or a new page is created
- **Input:** Page slug + GSC traffic data + current H1/content
- **Output:** New static HTML with CAG design system applied (trust bar + nature-inspired palette)
- **Paired with:** cag-website-health-skill.md (runs after to verify no broken images/canonicals)
- **Paired with:** cag-indexing-skill.md (runs after to submit redesigned pages to GSC/IndexNow)

### Session start checklist for design work:
1. Read `docs/reference/design-system.md` — confirm hex tokens are finalized before writing CSS
2. Run `/impeccable teach` to load CAG design vocabulary
3. Read current page HTML from `site/content/[slug]/index.html` before redesigning
4. Extract and preserve ALL schema JSON-LD blocks
5. Preserve ALL canonical tags
6. Preserve ALL meta description tags
7. Confirm CITES trust bar is included above every hero section
8. Run Impeccable audit on completed design before committing

### Photography direction for CAG pages:
- **Hero images:** African Grey parrot perched portrait (facing camera, grey body, red/maroon tail)
- **Lifestyle shots:** Bird-human bonding (step-up, shoulder perch, hand-feeding)
- **Aviary shots:** Bird room / aviary showing clean, enriched environment
- **Feather closeups:** Grey body feather detail, red tail feathers, beak and crest
- **Documentation shots:** Hatch certificates, band numbers, vet health certs (builds trust)
- **NEVER use:** Puppy/dog photos, kennel images, wild-caught bird imagery, anonymous stock parrots
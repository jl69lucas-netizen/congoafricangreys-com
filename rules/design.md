# Design system — the nine non-negotiable visual rules

Rules moved out of `CLAUDE.md` on 2026-08-02 (Phase 4). **The rule text is verbatim.**

`enforced:` says what actually holds the rule up.
`test` — a committed check fails when the rule is broken. `judgment` — no mechanical
decision procedure exists, and `data/quality/rule-index.json` records why.
`untested` — **a deletion candidate**: it is asserted and nothing enforces it.
`scripts/quality_report.py` §5 lists every one of those on every run, which is the point.

---
id: design-system-nine
enforced: untested
family: CSS
---

**Non-Negotiable Design Rules — enforced on every page build and rebuild:**
1. **Colors:** Three anchors only — Forest Green `#2D6A4F` (nav/headers), Clay `#e8604c` (all CTAs/buttons), Cream `#faf7f4` (page surface). `--gold` MUST always equal `--clay`. (Direction D does NOT change the palette.)
   - **WCAG AA contrast variants (2026-06-03 — do NOT revert):** `#e8604c` only clears AA as *large* text/fill (3.38:1 white). For accessibility, solid clay **button fills** render `--color-clay-ink #c8472f` (white text 4.78:1, via a global `.bg-clay` rule in `global.css`), and **clay as small readable text** (inline links, eyebrows, form prices) renders `#b04228` (4.5:1+ on light). Brand identity token `--clay #e8604c` is unchanged; it still applies to tints, large display, and clay text **on dark/green** (hero "Trust" accent, dark testimonial chips — kept bright via `.home-d` exceptions). See `DESIGN.md` §Color.
2. **Type:** Direction D is live → **Newsreader** serif for ALL headlines (H1–H6) and **IBM Plex Sans** for ALL body/labels/buttons, applied globally via `body.theme-d`. Keep using the `font-lora`/`font-sora` utility classes in markup — `direction-d.css` restyles them automatically; Lora/Sora remain the token-level fallback. Do not hard-code `font-family` on elements to fight the theme.
3. **Buttons:** Primary CTA = clay pill, `border-radius: 50px`. This is the brand signature. Form submit buttons only use `border-radius: 12px`.
4. **Cards:** 20px radius, 1px `--border`, warm shadow, white surface. Info cards use green header band.
5. **Shadows:** Always warm-tinted `rgba(60,30,10,…)`. Never neutral grey.
6. **Motion:** Max 0.2s transitions. No bounce, no parallax, no auto-playing video.
7. **Icons = line-icon SVGs, NOT emoji** (site-wide sweep 2026-06-03, commit `9ff570f`; full spec in `DESIGN.md §Iconography`). Use inline Feather-style SVGs (`width/height="1em"`, `stroke="currentColor"`) — map + transform in `scripts/emoji_to_icons.py`. The former canonical emoji set (📞 ✉️ 📍 🕐 ✈️ 🚗 ✅) is now line icons (✅ → green `#2D6A4F` check-circle). KEEP only the text glyphs ✔ ✗ ★ (list/rating markers). One per element. Banned: 🎉 🔥 🚀 and any colorful pictograph emoji. **Render rule:** a data-array icon rendered via `{x.icon}` must use `set:html`, then verify `grep -rl "&lt;svg" dist/` is empty. **NEVER put an `<svg>` inside CSS `content:`** — `content` only renders plain text, so `::before{content:'<svg…>'}` dumps the raw markup (or drops it) AND collapses badge spacing when the separator lived in that pseudo-element. Put the inline `<svg>` in the markup instead. Detect: `grep -rn "content: '<svg\|content:\"<svg" src/`. (Fixed on captive-bred / hand-raised / dna-tested trust bars, 2026-06-05.)
   - **African Grey bird icon — NEVER use 🦜** (generic green parrot, NOT an African Grey). Use custom images:
     - Congo African Grey: `<img src="/emoji/cag-congo.png" alt="Congo African Grey" class="cag-emoji" loading="lazy">`
     - Timneh African Grey: `<img src="/emoji/cag-timneh.png" alt="Timneh African Grey" class="cag-emoji" loading="lazy">`
     - Large decorative (100px+): `<img src="/emoji/cag-congo.png" style="width:Xpx;height:Xpx;object-fit:contain;" alt="" loading="lazy">` — match original font-size value
     - Plain text / email / JS string contexts: use `[CAG]` or `[TAG]` as text markers — HTML img not possible in strings
8. **Anti-copy:** NEVER add `user-select: none` CSS or JS.
9. **Infographic widths:** `760px` wrapper for species guides / blogs / care pages; `1100px` wrapper for homepage / location pages / hero sections. Height always `400px` fixed on desktop, `auto` on mobile. Never use `900px` or `max-w-4xl` — those are legacy values. See `docs/reference/page-width.md §Infographic Width Rules`.

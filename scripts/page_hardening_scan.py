#!/usr/bin/env python3
"""
CAG Page-Hardening Scanner — finds the UI/UX/perf/a11y defect classes that have
actually bitten this site, automatically, instead of waiting for the breeder to
spot them on a phone.

Every check below was banked from a real, confirmed defect (source noted inline).
Owned by skills/cag-page-hardening.md.

Usage:
  python3 scripts/page_hardening_scan.py                 # whole site
  python3 scripts/page_hardening_scan.py <slug> [<slug>] # specific pages
  python3 scripts/page_hardening_scan.py --fail-on-error # non-zero exit on ERROR

Severity:
  ERROR  = shipped-broken; fix before deploy
  WARN   = very likely wrong; eyeball it
"""
import re, sys, glob, os, json

SRC_GLOBS = ["src/pages/**/*.astro", "src/components/*.astro",
             "src/layouts/*.astro", "src/styles/*.css"]
DIST = "dist"

# The global MobileTabBar is `fixed bottom-0 ... z-50` (src/components/MobileTabBar.astro).
# Anything else pinned to the bottom must clear it or it renders invisible.
TABBAR_Z = 50
TABBAR_H = 56

findings = []
def add(sev, check, f, line, msg, fix):
    findings.append({"sev": sev, "check": check, "file": f, "line": line,
                     "msg": msg, "fix": fix})

def lines_of(path):
    try:
        return open(path, encoding="utf-8").read().split("\n")
    except Exception:
        return []

def src_files(slugs):
    out = []
    for g in SRC_GLOBS:
        out += glob.glob(g, recursive=True)
    if slugs:
        out = [f for f in out if any(s in f for s in slugs)]
    return sorted(set(out))


# ─────────────────────────────────────────────────────────────────────────────
# 1. Malformed clamp()/calc() — CSS math needs whitespace around + and -.
#    `clamp(1.7rem,1.2rem+2.2vw,2.6rem)` is INVALID: the whole declaration is
#    dropped and the element silently falls back to the global heading size.
#    This is why /hand-raised-.../ shipped a 48px h1 and a 524px hero while the
#    source said 2.26rem / ~400px (found 2026-07-23). Utterly invisible in review.
# ─────────────────────────────────────────────────────────────────────────────
def check_css_math(files):
    pat = re.compile(r"(?:clamp|calc|min|max)\([^)]*\)")
    bad = re.compile(r"[0-9a-z%)]\s*[+\-]\s*(?=[.\d])(?<![ ])|(?<=[0-9a-z%)])[+\-][.\d]")
    for f in files:
        for i, ln in enumerate(lines_of(f), 1):
            for m in pat.finditer(ln):
                expr = m.group(0)
                # a +/- with a non-space on either side, ignoring signs after ( or ,
                if re.search(r"(?<=[0-9a-z%\)])\+(?=[^\s])|(?<=[0-9a-z%\)])\s\-(?=[^\s])|(?<=[0-9a-z%\)])\-(?=[.\d])", expr):
                    add("ERROR", "css-math-spacing", f, i,
                        f"invalid CSS math (needs spaces around +/-): {expr}",
                        "rewrite as clamp(1.5rem, 1.02rem + 1.55vw, 1.98rem) — "
                        "without the spaces the declaration is dropped entirely")


# ─────────────────────────────────────────────────────────────────────────────
# 2. Bottom-pinned UI buried under the global MobileTabBar (z-50, 56px tall).
#    The hand-raised mobile jump-rail was `sticky; bottom:0; z-index:40` and
#    rendered *underneath* the tab bar — the breeder reported it as "broken".
# ─────────────────────────────────────────────────────────────────────────────
def check_bottom_bar_z(files):
    for f in files:
        ls = lines_of(f)
        for i, ln in enumerate(ls, 1):
            if not re.search(r"position:\s*(sticky|fixed)", ln):
                continue
            if not re.search(r"bottom:\s*0", ln):
                continue
            zm = re.search(r"z-index:\s*(\d+)", ln)
            z = int(zm.group(1)) if zm else 0
            if z <= TABBAR_Z:
                add("ERROR", "bottom-bar-under-tabbar", f, i,
                    f"bottom-pinned element at z-index:{z} sits under the global "
                    f"MobileTabBar (fixed bottom-0, z-{TABBAR_Z})",
                    f"bottom:calc({TABBAR_H}px + env(safe-area-inset-bottom)); "
                    f"z-index:{TABBAR_Z-5}; and pad the page bottom so content isn't covered")


# ─────────────────────────────────────────────────────────────────────────────
# 3. Infographics cover-cropped on mobile.
#    Forcing a 16:9 infographic into aspect-ratio:5/4 (or 4/5) with
#    object-fit:cover shaves ~30% off EACH side and cuts the baked-in text.
#    Only real OG photos get the taller mobile frame (IMAGE-DESIGNS §7).
# ─────────────────────────────────────────────────────────────────────────────
def check_infographic_crop(files):
    for f in files:
        for i, ln in enumerate(lines_of(f), 1):
            if ".inf-img" not in ln:
                continue
            has_tall = re.search(r"aspect-ratio:\s*(5\s*/\s*4|4\s*/\s*5)", ln)
            covers = "object-fit:contain" not in ln
            if has_tall and covers:
                add("ERROR", "infographic-cropped-mobile", f, i,
                    "infographic forced to a 5:4/4:5 box without object-fit:contain "
                    "— baked-in text will be cut off at both edges on mobile",
                    "keep infographics at their native aspect-ratio with "
                    "object-fit:contain; reserve the 5:4 mobile frame for .og-photo")


# ─────────────────────────────────────────────────────────────────────────────
# 4. 100vw full-bleed children inflating a grid track.
#    A `1fr` track sizes to its min-content, and a width:100vw child makes that
#    the viewport width — so the text column grew past the container padding and
#    body copy ran off-screen. Needs minmax(0,1fr) + min-width:0.
# ─────────────────────────────────────────────────────────────────────────────
def check_fullbleed_grid(files):
    """A width:100vw child inflates the `1fr` grid track that CONTAINS it — but
    which grid that is cannot be known statically (every attempt produced ~28
    false positives on one page). This defect is detected at RUNTIME instead:
    see the horizontal-overflow probe in skills/cag-page-hardening.md §Runtime.
    Kept as a no-op so the check list stays documented in one place."""
    return


# ─────────────────────────────────────────────────────────────────────────────
# 5. Absolutely-positioned hero art never unwound for mobile.
#    The hand-raised Hero-A polaroids were position:absolute with % widths; on
#    desktop they covered each other's heads, on mobile they collapsed to slivers.
# ─────────────────────────────────────────────────────────────────────────────
def check_absolute_hero(files):
    for f in files:
        txt = "\n".join(lines_of(f))
        for i, ln in enumerate(lines_of(f), 1):
            if not re.search(r"position:\s*absolute", ln):
                continue
            if not re.search(r"hero|polaroid|pofig|scatter|collage", ln, re.I):
                continue
            sel = ln.split("{")[0].strip()
            # captions/badges/chips/tags pinned inside a card are correct by design —
            # only the CARD ITSELF being absolute is the overlap/collapse bug.
            # NOTE single-colon `:before` too — `.chero-ribbon li:before{content:"✓"}`
            # is a bullet glyph, not hero art (it was firing before this).
            if re.search(r"figcaption|caption|badge|chip|label|tag|:{1,2}(before|after)",
                         sel, re.I):
                continue
            # A lone element pinned to `inset:0` (or all four offsets at 0) fills its
            # positioned parent — a cover-fill, not a scatter stack. It cannot overlap
            # a sibling at any width, so the overlap/collapse bug does not apply.
            # This is the comparison-cluster `.cvt-hero .hero-single img` pattern.
            decl = ln.split("{", 1)[1] if "{" in ln else ""
            fills = re.search(r"inset:\s*0", decl) or all(
                re.search(rf"{side}:\s*0", decl) for side in ("top", "right", "bottom", "left"))
            if fills:
                continue
            base = sel.split()[-1].lstrip(".")
            # is it reset inside any max-width media query?
            reset = re.search(
                r"@media[^{]*max-width[^{]*\{(?:[^{}]|\{[^{}]*\})*?"
                + re.escape(base) + r"[^{}]*\{[^{}]*position:\s*(static|relative)",
                txt, re.S)
            if not reset:
                add("WARN", "absolute-hero-not-unwound", f, i,
                    f"absolutely-positioned hero art ({sel}) is never reset to "
                    "static/relative in a mobile media query",
                    "lay hero art out with a grid (rotations for the scatter look) "
                    "so overlap is structurally impossible at every width")


# ─────────────────────────────────────────────────────────────────────────────
# 6. Small clay text below AA.  Brand --clay #e8604c is AA only as LARGE text.
#    Small text on light must be #b04228; solid clay fills use #c8472f.
# ─────────────────────────────────────────────────────────────────────────────
def check_clay_small_text(files):
    for f in files:
        for i, ln in enumerate(lines_of(f), 1):
            if not re.search(r"color:\s*(var\(--clay\)|#e8604c)", ln, re.I):
                continue
            fs = re.search(r"font-size:\s*([\d.]+)rem", ln)
            if fs and float(fs.group(1)) < 1.4:
                add("WARN", "clay-small-text-contrast", f, i,
                    f"--clay #e8604c as {fs.group(1)}rem text is 3.38:1 — below AA (4.5)",
                    "use --clay-ink #c8472f (4.78:1) or #b04228 for small clay text on light")


# ─────────────────────────────────────────────────────────────────────────────
# 7. opacity dimming text on a coloured fill — silently drops contrast below AA.
#    (`.k2-from{opacity:.9}` white on #c8472f measured 4.10 vs the 4.5 floor.)
# ─────────────────────────────────────────────────────────────────────────────
def check_opacity_text(files):
    for f in files:
        for i, ln in enumerate(lines_of(f), 1):
            m = re.search(r"opacity:\s*(0?\.\d+)", ln)
            if not m:
                continue
            if re.search(r"color:|font-size:|font-weight:", ln):
                add("WARN", "opacity-dims-text-contrast", f, i,
                    f"opacity:{m.group(1)} applied to a text rule — dims the "
                    "foreground and can drop it under AA",
                    "drop the opacity and pick an explicit colour that measures >= 4.5:1")


# ─────────────────────────────────────────────────────────────────────────────
# 8. Oversized image delivery — intrinsic width >> rendered width, no srcset.
#    (Lighthouse flagged 163 KiB on 620x720 hero polaroids shown at ~200px.)
# ─────────────────────────────────────────────────────────────────────────────
def check_img_srcset(pages):
    for p in pages:
        try:
            h = open(p, encoding="utf-8").read()
        except Exception:
            continue
        slug = p.replace(DIST + "/", "").replace("/index.html", "/")
        for m in re.finditer(r"<img\b[^>]*>", h):
            tag = m.group(0)
            if "srcset" in tag:
                continue
            w = re.search(r'width="(\d+)"', tag)
            if w and int(w.group(1)) >= 600:
                src = re.search(r'src="([^"]+)"', tag)
                add("WARN", "img-no-srcset", slug, 0,
                    f"{(src.group(1) if src else '?').split('/')[-1]} is "
                    f"{w.group(1)}px intrinsic with no srcset",
                    "ship a -320/-440/-760 sibling and add srcset+sizes")


# ─────────────────────────────────────────────────────────────────────────────
# 8b. Headings must be AP-style Title Case, matching the homepage and the
#     congo/timneh for-sale pages. The hand-raised page shipped 62 sentence-case
#     headings (2026-07-23). See skills/cag-page-hardening.md §1e-ter.
# ─────────────────────────────────────────────────────────────────────────────
MINOR_WORDS = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet",
               "at", "by", "in", "of", "on", "to", "as", "vs", "per", "via"}

# Genus names that legitimately precede a lowercase species epithet in a heading.
SPECIES_GENERA = {"Psittacus", "Ara", "Amazona", "Cacatua", "Eclectus", "Poicephalus"}

def check_title_case(pages):
    import html as _html
    for p in pages:
        try:
            raw = open(p, encoding="utf-8").read()
        except Exception:
            continue
        slug = p.replace(DIST + "/", "").replace("/index.html", "/")
        m = re.search(r"<main[^>]*>(.*)</main>", raw, re.S)
        if not m:
            continue
        seg = m.group(1)
        for lvl in range(1, 7):
            for inner in re.findall(rf"<h{lvl}[^>]*>(.*?)</h{lvl}>", seg, re.S):
                t = re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", inner))).strip()
                if not t:
                    continue
                words = t.split(" ")
                force = True
                for i, w in enumerate(words):
                    core = re.sub(r"[^\w'-]", "", w)
                    # Binomial species epithets are correctly lowercase — "Psittacus
                    # erithacus", "Psittacus timneh". Capitalising them would be the
                    # actual defect, so they sit in the same exemption class as acronyms.
                    prev = re.sub(r"[^\w'-]", "", words[i - 1]) if i else ""
                    if prev in SPECIES_GENERA and core.islower():
                        force = bool(re.search(r"[:?!]$", w))
                        continue
                    # skip acronyms, brands, domains, numbers, prices
                    if (not core or core[0].isdigit() or "." in w
                            or core.isupper() or re.search(r"[a-z][A-Z]", core)):
                        force = bool(re.search(r"[:?!]$", w))
                        continue
                    must_cap = (force or i == 0 or i == len(words) - 1
                                or core.lower() not in MINOR_WORDS)
                    if must_cap and core[0].islower():
                        add("ERROR", "header-not-title-case", slug, 0,
                            f'H{lvl} is not Title Case ("{w}" in "{t[:58]}")',
                            "AP-style Title Case: capitalise 4+ letter words and all "
                            "nouns/verbs/adjectives; lowercase only mid-title "
                            "a/an/the/and/or/for/at/by/in/of/on/to/as/vs")
                        break
                    force = bool(re.search(r"[:?!]$", w))


# ─────────────────────────────────────────────────────────────────────────────
# 9. Body links distinguishable by colour alone (WCAG 1.4.1).
# ─────────────────────────────────────────────────────────────────────────────
def check_link_underline(files):
    for f in files:
        txt = "\n".join(lines_of(f))
        if ".content p a" in txt or "content li a" in txt:
            if re.search(r"\.content (?:p|li) a[^{]*\{[^}]*text-decoration:\s*underline", txt):
                continue
        if re.search(r"\.content\b", txt) and "text-decoration:underline" not in txt.replace(" ", ""):
            add("WARN", "links-colour-only", f, 0,
                "no underline rule found for in-body content links",
                "add .content p a{text-decoration:underline;text-underline-offset:2px}")


# ─────────────────────────────────────────────────────────────────────────────
# 10. Known render traps already banked in MEMORY.
# ─────────────────────────────────────────────────────────────────────────────
def check_known_traps(files, pages):
    for f in files:
        for i, ln in enumerate(lines_of(f), 1):
            if re.search(r"content:\s*['\"]\s*<svg", ln):
                add("ERROR", "svg-in-css-content", f, i,
                    "an <svg> inside CSS content: renders as raw text and collapses spacing",
                    "put the inline <svg> in the markup instead")
            if "user-select:none" in ln.replace(" ", "") and ".select-none" not in ln:
                add("ERROR", "user-select-none", f, i,
                    "user-select:none is banned site-wide (anti-copy rule)",
                    "remove it")
            # scroll-behavior is now handled by check_smooth_scroll(), which allows
            # the reduced-motion-guarded global `html` rule and still warns on rails.
    for p in pages:
        try:
            h = open(p, encoding="utf-8").read()
        except Exception:
            continue
        slug = p.replace(DIST + "/", "").replace("/index.html", "/")
        if "&lt;svg" in h:
            add("ERROR", "escaped-svg", slug, 0,
                "an inline SVG rendered escaped (&lt;svg) — a data-array icon is "
                "missing set:html", "add set:html to the {x.icon} render")


# ═════════════════════════════════════════════════════════════════════════════
# The 2026-07-26 gate gaps. Every check below was banked from a defect that
# shipped on the for-sale cluster and was found by the breeder on a phone rather
# than by this scanner. Each takes [(label, text)] so it is unit-testable.
# See tests/test_page_hardening_new_checks.py.
# ═════════════════════════════════════════════════════════════════════════════

# ── hero-preload-srcset-drift ────────────────────────────────────────────────
# BaseLayout.astro:22-23 warns that heroPreloadSrcset/heroPreloadSizes must mirror
# the LCP <img>. When only heroPreloadSizes is passed, the preload scanner resolves
# a different candidate than the renderer, and the hero downloads twice.
def check_hero_preload_drift(sources):
    for label, text in sources:
        if "heroPreload" not in text:
            continue
        img_has_srcset = re.search(r"<img\b[^>]*fetchpriority=\"high\"[^>]*srcset=", text, re.S) \
            or re.search(r"<img\b[^>]*srcset=[^>]*fetchpriority=\"high\"", text, re.S)
        if img_has_srcset and "heroPreloadSrcset" not in text:
            line = text[: text.index("heroPreload")].count("\n") + 1
            add("ERROR", "hero-preload-srcset-drift", label, line,
                "heroPreload is set and the LCP <img> uses srcset, but "
                "heroPreloadSrcset is missing — the preload scanner will fetch a "
                "different candidate than the renderer uses (hero downloads twice)",
                "mirror the img's srcset/sizes into heroPreloadSrcset/heroPreloadSizes")


# ── tap-target-spacing ───────────────────────────────────────────────────────
# /african-greys-for-sale-with-health-guarantee/ shipped 28 failing target pairs on
# BOTH mobile and desktop. The pills are 36px tall so SIZE passed; `gap:7px` put
# each pill inside its neighbour's 24px exclusion zone. axe target-size minimum.
MIN_TARGET_GAP_PX = 10.0

def _px(val):
    """Resolve a CSS length to px. rem = 16px. Returns None if not resolvable."""
    m = re.match(r"^\s*(-?[\d.]+)(px|rem|em)?\s*$", val or "")
    if not m:
        return None
    n = float(m.group(1))
    return n * 16 if m.group(2) in ("rem", "em") else n

def check_tap_target_spacing(sources):
    for label, text in sources:
        # A flex/grid list that is a nav rail (has overflow-x or is a ul of links)
        for m in re.finditer(r"([^{}]*)\{([^}]*)\}", text):
            sel, body = m.group(1).strip(), m.group(2)
            if "display:flex" not in body.replace(" ", "") and \
               "display:grid" not in body.replace(" ", ""):
                continue
            if not re.search(r"\brail|\bnav|\bdial|\bjump|\btoc\b", sel, re.I):
                continue
            g = re.search(r"(?<![-\w])gap:\s*([^;]+);", body)
            if not g:
                continue
            gap = _px(g.group(1).split()[0])
            if gap is None or gap >= MIN_TARGET_GAP_PX:
                continue
            line = text[: m.start()].count("\n") + 1
            add("ERROR", "tap-target-spacing", label, line,
                f"nav pills in `{sel}` sit {gap:g}px apart — adjacent tap targets "
                f"fall inside each other's 24px exclusion zone (axe target-size)",
                f"raise gap to >={MIN_TARGET_GAP_PX:g}px and pad the pills to >=44px tall")


# ── form-control-overflow / form-control-ios-zoom ────────────────────────────
# The health-guarantee contact form was cut off on the right at mobile/tablet.
# A CSS grid child defaults to min-width:auto and refuses to shrink below its
# content — the single most common cause of exactly this symptom. Sub-16px inputs
# additionally trigger iOS Safari auto-zoom, which reads as "too zoomed, cut off".
def check_form_overflow(sources):
    for label, text in sources:
        flat = text.replace(" ", "")
        form_grid = re.search(r"([^{}]*form[^{}]*)\{([^}]*display:\s*grid[^}]*)\}",
                              text, re.I)
        if form_grid and "min-width:0" not in flat:
            line = text[: form_grid.start()].count("\n") + 1
            add("ERROR", "form-control-overflow", label, line,
                f"`{form_grid.group(1).strip()}` is a grid but no child sets "
                "min-width:0 — grid children default to min-width:auto and will "
                "not shrink below their content, overflowing the viewport",
                "add `.row>*{min-width:0}` and max-width:100%;box-sizing:border-box "
                "on every input/select")
        for m in re.finditer(r"([^{}]*(?:input|select|textarea)[^{}]*)\{([^}]*)\}",
                             text, re.I):
            sel, body = m.group(1).strip(), m.group(2)
            line = text[: m.start()].count("\n") + 1
            fs = re.search(r"font-size:\s*([^;]+);", body)
            if fs:
                size = _px(fs.group(1))
                if size is not None and size < 16:
                    add("ERROR", "form-control-ios-zoom", label, line,
                        f"`{sel}` sets font-size {size:g}px — anything under 16px "
                        "makes iOS Safari auto-zoom the page on focus, which reads "
                        "to users as the form being cut off",
                        "set font-size:16px on every input/select/textarea")
                continue
            # `font:inherit` is the sneaky case — the size is real but declared on an
            # ancestor. Resolve it against the nearest label/form rule in the same file.
            if not re.search(r"font:\s*inherit", body):
                continue
            scope = sel.split(",")[0].rsplit(" ", 1)[0].strip()
            inherited = None
            for anc in re.finditer(r"([^{}]*)\{([^}]*)\}", text):
                anc_sel = anc.group(1).strip()
                if scope and scope not in anc_sel:
                    continue
                if not re.search(r"\b(label|form|fieldset)\b", anc_sel, re.I):
                    continue
                afs = re.search(r"font-size:\s*([^;]+);", anc.group(2))
                if afs:
                    inherited = _px(afs.group(1))
            if inherited is not None and inherited < 16:
                add("ERROR", "form-control-ios-zoom", label, line,
                    f"`{sel}` uses font:inherit, which resolves to {inherited:g}px "
                    f"from its ancestor label — under 16px iOS Safari auto-zooms on "
                    "focus and the form's right edge leaves the viewport",
                    "set an explicit font-size:16px on every input/select/textarea "
                    "(the label can stay smaller)")


# ── font-family-loaded-unused ────────────────────────────────────────────────
# Lora and Sora were requested in BaseLayout on EVERY page of the site but never
# rendered: direction-d.css overrides .font-lora/.font-sora with !important. Two of
# the five woff2 files in every "Network dependency tree" PageSpeed finding.
def check_font_families(head_html, theme_css):
    requested = set()
    for m in re.finditer(r"family=([A-Za-z0-9+]+)[:&]", head_html):
        requested.add(m.group(1).replace("+", " "))
    for m in re.finditer(r"@font-face\s*\{[^}]*font-family:\s*['\"]([^'\"]+)", head_html):
        requested.add(m.group(1))
    rendered = set(re.findall(r"font-family:\s*[^;]*?['\"]([^'\"]+)['\"]", theme_css))
    for fam in sorted(requested):
        if fam in rendered:
            continue
        if any(fam in r for r in rendered):
            continue
        add("ERROR", "font-family-loaded-unused", "src/layouts/BaseLayout.astro", 0,
            f"'{fam}' is downloaded on every page but no CSS rule ever resolves to "
            f"it — it is pure dead weight in the critical font chain",
            f"remove {fam} from the font request")


# ── analytics-double-load ────────────────────────────────────────────────────
# /70de/ is GA4 served first-party via Cloudflare's Google Tag Gateway. The direct
# googletagmanager.com tag ALSO fired, so the same G-MEWJ9GVC4T container loaded
# twice — ~327 KiB of analytics on every page. NOT Rocket Loader, which was off.
GTAG_GATEWAY = re.compile(r"""<script[^>]*\bsrc=["']/[0-9a-f]{4,}/["']""", re.I)
GTAG_DIRECT = re.compile(r"googletagmanager\.com/(?:gtag/js|gtm\.js)", re.I)

def check_analytics_double_load(pages):
    for label, html in pages:
        direct = GTAG_DIRECT.search(html)
        gateway = GTAG_GATEWAY.search(html)
        if direct and gateway:
            line = html[: direct.start()].count("\n") + 1
            add("ERROR", "analytics-double-load", label, line,
                "the GA4 container loads twice — once directly from "
                "googletagmanager.com and once first-party via Cloudflare's Google "
                "Tag Gateway (~327 KiB of analytics on this page)",
                "keep ONE. Prefer the first-party gateway, loaded on the window "
                "load event so it never competes with LCP")


# ── deflist-label-not-differentiated ─────────────────────────────────────────
# The health-guarantee "guarantee on one receipt" component: Window / Covered /
# Remedy / Voided by / Confirmed by / From rendered in the same colour AND weight
# as their values, so the block read as one grey slab.
# `.dt` is a real class on this site (the dial-list tag chip), so the element must be
# matched without a leading . or - or word char, or the wrong rule gets paired.
EL = lambda n: re.compile(rf"([^{{}}]*(?<![.\w-]){n}(?![\w-])[^{{}}]*)\{{([^}}]*)\}}")

def check_deflist_labels(sources):
    for label, text in sources:
        dts = list(EL("dt").finditer(text))
        dds = list(EL("dd").finditer(text))
        if not (dts and dds):
            continue
        # Pair each dt rule with the dd rule sharing its scope (same ancestor chain).
        def scope_of(sel):
            # `[^{}]*` greedily swallows preceding comments/newlines, so keep only
            # the final selector line before the brace.
            last = sel.strip().split("\n")[-1].strip()
            last = re.sub(r"^.*\*/", "", last).strip()
            return last.rsplit(" ", 1)[0].strip()
        def is_css(sel):
            # These files are .astro — the same regex happily matches markup like
            # `<span class="dt">`. Only keep things that look like a CSS selector.
            return "<" not in sel and ">" not in sel and bool(re.match(r"^[.#a-z]", sel))

        def prop(body, name):
            m = re.search(rf"{name}:\s*([^;]+);", body)
            return m.group(1).strip() if m else None

        pairs = []
        for d in dts:
            sel = scope_of(d.group(1))
            full = d.group(1).strip().split("\n")[-1].strip()
            if not is_css(full):
                continue
            match = next((x for x in dds
                          if scope_of(x.group(1)) == sel
                          and is_css(x.group(1).strip().split("\n")[-1].strip())), None)
            if match:
                pairs.append((d, match))
        if not pairs:
            continue
        # Report the first pair that actually declares colours.
        dt, dd = next(((a, b) for a, b in pairs if prop(a.group(2), "color")), pairs[0])
        dt_colour, dd_colour = prop(dt.group(2), "color"), prop(dd.group(2), "color")
        same_colour = dt_colour == dd_colour
        same_weight = prop(dt.group(2), "font-weight") == prop(dd.group(2), "font-weight")
        line = text[: dt.start()].count("\n") + 1
        if same_colour and same_weight and dt_colour:
            add("WARN", "deflist-label-not-differentiated", label, line,
                "<dt> labels and their <dd> values share the same colour AND weight "
                "— the list reads as one undifferentiated block",
                "give the <dt> a distinct colour (var(--green-d)) and heavier weight, "
                "and lighten the <dd>")
        elif dt_colour and "muted" in dt_colour and dd_colour and "muted" not in dd_colour:
            # Different, but backwards: a muted label RECEDES behind its own value.
            # A label should lead the eye into the row, not sit quieter than it.
            add("WARN", "deflist-label-not-differentiated", label, line,
                f"<dt> labels use {dt_colour} while their values use {dd_colour} — the "
                "label is quieter than the thing it labels, so the block reads as one "
                "grey slab and the reader cannot scan the rows",
                "give the <dt> a distinct hue that leads (var(--green-d)), not a "
                "lower-contrast grey")


# ── icon-text-baseline-drift ─────────────────────────────────────────────────
# The health-guarantee trust ticks looked "scattered" on mobile: the flex row never
# set align-items, so each tick floated against a differently-wrapped label.
def check_icon_baseline(sources):
    for label, text in sources:
        for m in re.finditer(r"([^{}]*(?:tick|badge|check|trust|feat)[^{}]*)\{([^}]*)\}",
                             text, re.I):
            body = m.group(2).replace(" ", "")
            if "display:flex" not in body and "display:grid" not in body:
                continue
            if "align-items:" in body:
                continue
            line = text[: m.start()].count("\n") + 1
            sel = m.group(1).strip().split("\n")[-1].strip()
            add("WARN", "icon-text-baseline-drift", label, line,
                f"`{sel}` lays out an icon+label row but never sets "
                "align-items — when the label wraps, the glyph drifts off its text "
                "and the column reads as scattered",
                "use grid-template-columns:1rem 1fr with align-items:start so wrapped "
                "labels stay hanging-indented under themselves")


# ── smooth-scroll-breaks-anchors (refined 2026-07-26) ────────────────────────
# The original trap warned on ANY scroll-behavior:smooth. The pages now set
# scroll-margin-top to clear the header + sticky rail, so a reduced-motion-guarded
# GLOBAL rule on html is correct. A jump rail's own horizontal scroller must still
# warn — smooth there fights the active-pill auto-scroll.
def check_smooth_scroll(sources):
    for label, text in sources:
        for m in re.finditer(r"scroll-behavior:\s*smooth", text):
            before = text[: m.start()]
            line = before.count("\n") + 1
            block_start = max(before.rfind("{"), 0)
            selector = before[max(before.rfind("}", 0, block_start), 0):block_start]
            guarded = "prefers-reduced-motion" in before[-400:]
            global_rule = re.search(r"\bhtml\b\s*$", selector.strip()) is not None
            if guarded and global_rule:
                continue
            add("WARN", "smooth-scroll-breaks-anchors", label, line,
                "scroll-behavior:smooth here fights in-page navigation — on a jump "
                "rail it cancels the instant active-pill snap",
                "keep scroll-behavior:auto on rails/dials; the only allowed smooth "
                "rule is `html` inside @media (prefers-reduced-motion: no-preference)")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fail_on_error = "--fail-on-error" in sys.argv
    files = src_files(args)
    pages = sorted(glob.glob(f"{DIST}/**/index.html", recursive=True))
    if args:
        pages = [p for p in pages if any(s in p for s in args)]

    check_css_math(files)
    check_bottom_bar_z(files)
    check_infographic_crop(files)
    check_fullbleed_grid(files)
    check_absolute_hero(files)
    check_clay_small_text(files)
    check_opacity_text(files)
    check_link_underline(files)
    check_known_traps(files, pages)

    # 2026-07-26 gate gaps — see tests/test_page_hardening_new_checks.py
    src_pairs = [(f, "\n".join(lines_of(f))) for f in files]
    check_hero_preload_drift(src_pairs)
    check_tap_target_spacing(src_pairs)
    check_form_overflow(src_pairs)
    check_deflist_labels(src_pairs)
    check_icon_baseline(src_pairs)
    check_smooth_scroll(src_pairs)

    base = "src/layouts/BaseLayout.astro"
    theme = "\n".join(lines_of("src/styles/direction-d.css") +
                      lines_of("src/styles/global.css"))
    if os.path.exists(base):
        check_font_families("\n".join(lines_of(base)), theme)

    if pages:
        check_img_srcset(pages)
        check_title_case(pages)
        check_analytics_double_load(
            [(p.replace(DIST + "/", "").replace("/index.html", "/"),
              open(p, encoding="utf-8").read()) for p in pages])

    errs = [f for f in findings if f["sev"] == "ERROR"]
    warns = [f for f in findings if f["sev"] == "WARN"]
    print(f"CAG page-hardening scan — {len(files)} source files, {len(pages)} built pages\n")
    for group, title in ((errs, "ERROR"), (warns, "WARN")):
        if not group:
            continue
        print(f"── {title} ({len(group)}) " + "─" * 40)
        for f in group:
            loc = f"{f['file']}:{f['line']}" if f["line"] else f["file"]
            print(f"  [{f['check']}] {loc}\n      {f['msg']}\n      fix: {f['fix']}\n")
    if not findings:
        print("✅ clean — no known hardening defects found")
    else:
        print(f"{len(errs)} ERROR · {len(warns)} WARN")
    return 1 if (fail_on_error and errs) else 0


if __name__ == "__main__":
    sys.exit(main())

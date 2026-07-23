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
            # captions/badges/chips pinned inside a card are correct by design —
            # only the CARD ITSELF being absolute is the overlap/collapse bug
            if re.search(r"figcaption|caption|badge|chip|label|::(before|after)", sel, re.I):
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
            if re.search(r"scroll-behavior:\s*smooth", ln):
                add("WARN", "smooth-scroll-breaks-anchors", f, i,
                    "scroll-behavior:smooth cancels in-page #anchor navigation on this site",
                    "use scroll-behavior:auto for jump rails / dial TOCs")
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
    if pages:
        check_img_srcset(pages)

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

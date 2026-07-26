# tests/test_page_hardening_new_checks.py
#
# The 8 gate gaps found 2026-07-26. Every fixture below is a VERBATIM reduction of a
# defect that shipped to production on the for-sale cluster and was caught by the
# breeder on a phone rather than by this scanner. A check is only correct if it
# reproduces its own defect — that is the acceptance test for Phase 0.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import page_hardening_scan as H


def run(check, *args):
    """Call a check in isolation and return just the findings it produced."""
    H.findings.clear()
    check(*args)
    return list(H.findings)


def checks_named(found, name):
    return [f for f in found if f["check"] == name]


# ── 1. hero-preload-srcset-drift ─────────────────────────────────────────────
# Statically checkable half of the oversized-hero problem. BaseLayout.astro:22-23
# warns that heroPreloadSrcset/heroPreloadSizes MUST mirror the LCP <img>, or the
# preload scanner fetches a DIFFERENT candidate than the renderer uses — two
# downloads of the same hero. The sizes-vs-rendered-box half of the defect is NOT
# statically knowable (see check list in skills/cag-page-hardening.md) and lives
# in the runtime probe `srcset-sizes-mismatch`.

DRIFTED_PRELOAD = """
<BaseLayout
  heroPreload="/images/hand-raised-page/hero-mark-hand-scratch-grey.webp"
  heroPreloadSizes="(max-width:980px) 42vw, 158px"
>
<img src="/images/hand-raised-page/hero-mark-hand-scratch-grey.webp"
  srcset="/images/hand-raised-page/hero-mark-hand-scratch-grey-320.webp 320w"
  sizes="(max-width:980px) 42vw, 158px" fetchpriority="high">
"""

MIRRORED_PRELOAD = """
<BaseLayout
  heroPreload="/images/hand-raised-page/hero-mark-hand-scratch-grey.webp"
  heroPreloadSrcset="/images/hand-raised-page/hero-mark-hand-scratch-grey-320.webp 320w"
  heroPreloadSizes="(max-width:980px) 42vw, 158px"
>
<img src="/images/hand-raised-page/hero-mark-hand-scratch-grey.webp"
  srcset="/images/hand-raised-page/hero-mark-hand-scratch-grey-320.webp 320w"
  sizes="(max-width:980px) 42vw, 158px" fetchpriority="high">
"""


def test_flags_hero_preload_missing_srcset_mirror():
    found = checks_named(run(H.check_hero_preload_drift, [("hand-raised", DRIFTED_PRELOAD)]),
                         "hero-preload-srcset-drift")
    assert len(found) == 1, found


def test_passes_mirrored_hero_preload():
    assert checks_named(run(H.check_hero_preload_drift, [("hand-raised", MIRRORED_PRELOAD)]),
                        "hero-preload-srcset-drift") == []


# ── 2. tap-target-spacing ────────────────────────────────────────────────────
# Shipped on /african-greys-for-sale-with-health-guarantee/: 28 failing pairs on
# BOTH mobile and desktop. Pills are 36px tall (size passes) but gap:7px puts
# adjacent targets inside each other's 24px exclusion zone.

HG_RAIL_CSS = """
.hgar .railA ul{display:flex;gap:7px;overflow-x:auto;list-style:none;margin:0;padding:.45rem .75rem;}
.hgar .railA a{display:inline-flex;align-items:center;gap:.35rem;font-size:.76rem;border-radius:50px;padding:7px 14px;min-height:36px;}
"""

GOOD_RAIL_CSS = """
.hgar .railA ul{display:flex;gap:12px;overflow-x:auto;list-style:none;}
.hgar .railA a{display:inline-flex;align-items:center;padding:8px 16px;min-height:44px;}
"""


def test_flags_tight_gap_between_nav_pills():
    found = checks_named(run(H.check_tap_target_spacing, [("hg.astro", HG_RAIL_CSS)]),
                         "tap-target-spacing")
    assert len(found) >= 1, found


def test_passes_adequate_gap():
    assert checks_named(run(H.check_tap_target_spacing, [("hg.astro", GOOD_RAIL_CSS)]),
                        "tap-target-spacing") == []


# ── 3. form-control-overflow ─────────────────────────────────────────────────
# Shipped on the health-guarantee contact form: fields cut off on the right at
# mobile/tablet. Root cause is a grid child defaulting to min-width:auto, which
# refuses to shrink below its content.

BROKEN_FORM_CSS = """
.hgar .form-main .row{display:grid;grid-template-columns:1fr 1fr;gap:.7rem;}
.hgar .form-main input{padding:.6rem .8rem;font-size:.9rem;border:1px solid var(--bd);}
.hgar .form-main select{padding:.6rem .8rem;font-size:.9rem;}
"""

FIXED_FORM_CSS = """
.hgar .form-main .row{display:grid;grid-template-columns:1fr 1fr;gap:.7rem;}
.hgar .form-main .row>*{min-width:0;}
.hgar .form-main input,.hgar .form-main select{max-width:100%;box-sizing:border-box;font-size:16px;}
"""


def test_flags_grid_form_row_without_min_width_zero():
    found = checks_named(run(H.check_form_overflow, [("hg.astro", BROKEN_FORM_CSS)]),
                         "form-control-overflow")
    assert len(found) >= 1, found


def test_flags_sub_16px_font_on_inputs_ios_autozoom():
    found = checks_named(run(H.check_form_overflow, [("hg.astro", BROKEN_FORM_CSS)]),
                         "form-control-ios-zoom")
    assert len(found) >= 1, found


def test_passes_correctly_constrained_form():
    found = run(H.check_form_overflow, [("hg.astro", FIXED_FORM_CSS)])
    assert found == [], found


# The ACTUAL health-guarantee form bug, missed by the first cut of this check:
# the size is inherited, not declared. `font:inherit` on the input resolves to the
# label's .82rem = 13.1px, so iOS Safari auto-zooms on focus and the right-hand
# edge of the form leaves the viewport. Verbatim from index.astro:1079-1080.
HG_REAL_FORM_CSS = """
.hgar .form-main{padding:22px;background:#fff;display:grid;gap:.7rem;}
.hgar .form-main label{display:grid;gap:.25rem;font-size:.82rem;font-weight:600;color:var(--green-d);}
.hgar .form-main input,.hgar .form-main select,.hgar .form-main textarea{font:inherit;font-weight:400;padding:.55rem .65rem;border:1px solid var(--bd);border-radius:10px;}
"""


def test_flags_inherited_sub_16px_font_on_real_hg_form():
    found = checks_named(run(H.check_form_overflow, [("hg.astro", HG_REAL_FORM_CSS)]),
                         "form-control-ios-zoom")
    assert len(found) >= 1, "font:inherit resolving to 13.1px must be flagged"
    assert "inherit" in found[0]["msg"], found[0]["msg"]


def test_font_inherit_is_fine_when_ancestor_is_16px():
    ok = """
.form-main label{font-size:1rem;}
.form-main input{font:inherit;max-width:100%;box-sizing:border-box;}
.form-main .row>*{min-width:0;}
"""
    assert checks_named(run(H.check_form_overflow, [("ok.astro", ok)]),
                        "form-control-ios-zoom") == []


# ── 4. font-family-loaded-unused ─────────────────────────────────────────────
# Lora and Sora were requested in BaseLayout on EVERY page of the site but never
# rendered — direction-d.css overrides .font-lora/.font-sora with !important.
# Two of the five woff2 files in every "Network dependency tree" finding.

BASE_LAYOUT_4_FAMILIES = (
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Lora:wght@400;600;700&family=Sora:wght@400;500;600&'
    'family=Newsreader:ital,opsz,wght@0,6..72,400&'
    'family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">'
)

THEME_CSS_OVERRIDES_BOTH = """
body.theme-d .font-sora{font-family:'IBM Plex Sans','IBM Plex Sans Fallback',system-ui,sans-serif !important;}
body.theme-d h1,body.theme-d h2{font-family:'Newsreader','Newsreader Fallback',Georgia,serif !important;}
"""


def test_flags_requested_families_that_never_render():
    found = checks_named(
        run(H.check_font_families, BASE_LAYOUT_4_FAMILIES, THEME_CSS_OVERRIDES_BOTH),
        "font-family-loaded-unused")
    names = " ".join(f["msg"] for f in found)
    assert "Lora" in names and "Sora" in names, names
    assert "Newsreader" not in names and "IBM Plex Sans" not in names, names


def test_passes_when_only_used_families_are_requested():
    slim = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Newsreader:wght@400&family=IBM+Plex+Sans:wght@400&display=swap">')
    assert checks_named(run(H.check_font_families, slim, THEME_CSS_OVERRIDES_BOTH),
                        "font-family-loaded-unused") == []


# REGRESSION (2026-07-26): the first cut of this check reported Lora and Sora as dead
# weight. A runtime probe proved otherwise — Lora renders on 41 elements and Sora on 10.
# The check had only scanned `font-family:` declarations in two stylesheets, so it missed
# BOTH the custom-property definition and the page CSS that consumes it. Dropping the
# families on that advice would have degraded 51 elements to Georgia / system-ui.
TOKENS_AND_PAGE_CSS = """
:root{
  --font-lora: 'Lora', Georgia, serif;
  --font-sora: 'Sora', system-ui, sans-serif;
}
body.theme-d .font-sora{font-family:'IBM Plex Sans','IBM Plex Sans Fallback',system-ui,sans-serif !important;}
body.theme-d h1,body.theme-d h2{font-family:'Newsreader','Newsreader Fallback',Georgia,serif !important;}
.hgar .k1-head b{font-family:var(--font-lora,'Newsreader',serif);font-size:1.02rem;}
"""


def test_family_reachable_only_through_a_custom_property_is_not_dead():
    found = checks_named(
        run(H.check_font_families, BASE_LAYOUT_4_FAMILIES, TOKENS_AND_PAGE_CSS),
        "font-family-loaded-unused")
    names = " ".join(f["msg"] for f in found)
    assert "Lora" not in names, f"Lora reaches the page via var(--font-lora): {names}"
    assert "Sora" not in names, f"Sora reaches the page via var(--font-sora): {names}"


def test_still_flags_a_family_with_no_reference_at_all():
    head = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Newsreader:wght@400&family=Bitter:wght@400&display=swap">')
    found = checks_named(run(H.check_font_families, head, TOKENS_AND_PAGE_CSS),
                         "font-family-loaded-unused")
    assert len(found) == 1 and "Bitter" in found[0]["msg"], found


# ── 5. analytics-double-load ─────────────────────────────────────────────────
# /70de/ is GA4 served first-party via Cloudflare's Google Tag Gateway. The direct
# googletagmanager.com tag ALSO fires, so the same G-MEWJ9GVC4T container loads
# twice: ~327 KiB of analytics on every page.

DOUBLE_GA = """
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MEWJ9GVC4T"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
gtag('config','G-MEWJ9GVC4T');</script>
<script async src="/70de/"></script>
"""

SINGLE_GA = """
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
gtag('config','G-MEWJ9GVC4T');
addEventListener('load',()=>{const s=document.createElement('script');s.src='/70de/';s.async=true;document.head.appendChild(s);},{once:true});</script>
"""


def test_flags_gtag_loaded_directly_and_via_first_party_gateway():
    found = checks_named(run(H.check_analytics_double_load, [("hand-raised", DOUBLE_GA)]),
                         "analytics-double-load")
    assert len(found) == 1, found


def test_passes_single_deferred_gateway_load():
    assert checks_named(run(H.check_analytics_double_load, [("hand-raised", SINGLE_GA)]),
                        "analytics-double-load") == []


# ── 6. deflist-label-not-differentiated ──────────────────────────────────────
# The health-guarantee "guarantee on one receipt" component: Window / Covered /
# Remedy / Voided by / Confirmed by / From render in the same colour and weight as
# their values, so the whole block reads as one grey slab.

FLAT_RECEIPT_CSS = """
.hgar .receipt dt{color:var(--ink);font-weight:600;font-size:.85rem;}
.hgar .receipt dd{color:var(--ink);font-weight:600;font-size:.85rem;margin:0 0 .6rem;}
"""

DIFFERENTIATED_RECEIPT_CSS = """
.hgar .receipt dt{color:var(--green-d);font-weight:700;font-size:.72rem;letter-spacing:.04em;}
.hgar .receipt dd{color:var(--ink);font-weight:400;font-size:.9rem;margin:0 0 .6rem;}
"""


def test_flags_label_and_value_sharing_colour_and_weight():
    found = checks_named(run(H.check_deflist_labels, [("hg.astro", FLAT_RECEIPT_CSS)]),
                         "deflist-label-not-differentiated")
    assert len(found) == 1, found


def test_passes_differentiated_labels():
    assert checks_named(run(H.check_deflist_labels, [("hg.astro", DIFFERENTIATED_RECEIPT_CSS)]),
                        "deflist-label-not-differentiated") == []


# The REAL health-guarantee receipt (index.astro:935-936). The dt and dd are not
# identical — but the dt is var(--muted), a low-contrast grey, while the dd is
# var(--ink). The label RECEDES behind its own value instead of leading it, which
# is what the breeder reported as "same colour as the body text, hard to read".
HG_REAL_RECEIPT_CSS = """
.hgar .k1-rows dt{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);padding-top:.15rem;}
.hgar .k1-rows dd{margin:0;font-size:.9rem;line-height:1.5;color:var(--ink);}
"""


def test_flags_muted_label_receding_behind_its_value():
    found = checks_named(run(H.check_deflist_labels, [("hg.astro", HG_REAL_RECEIPT_CSS)]),
                         "deflist-label-not-differentiated")
    assert len(found) == 1, "a --muted dt against an --ink dd must be flagged"
    assert "muted" in found[0]["msg"], found[0]["msg"]


# ── 7. icon-text-baseline-drift ──────────────────────────────────────────────
# The health-guarantee trust ticks ("72-hour written guarantee / Avian-vet examined
# / DNA-sexed, certificate included / CITES") looked scattered on mobile: the flex
# row never set align-items, so each tick floated against a differently-wrapped label.

DRIFTING_TICKS_CSS = """
.hgar .ticks li{display:flex;gap:.5rem;font-size:.8rem;margin-bottom:.4rem;}
"""

ALIGNED_TICKS_CSS = """
.hgar .ticks li{display:grid;grid-template-columns:1rem 1fr;align-items:start;gap:.5rem;row-gap:.6rem;line-height:1.45;}
"""


def test_flags_icon_row_without_align_items():
    found = checks_named(run(H.check_icon_baseline, [("hg.astro", DRIFTING_TICKS_CSS)]),
                         "icon-text-baseline-drift")
    assert len(found) == 1, found


def test_passes_explicitly_aligned_icon_row():
    assert checks_named(run(H.check_icon_baseline, [("hg.astro", ALIGNED_TICKS_CSS)]),
                        "icon-text-baseline-drift") == []


# ── 8. smooth-scroll: the guarded global rule must be ALLOWED ────────────────
# The existing trap warns on any scroll-behavior:smooth because it once broke
# in-page anchors. The pages now set scroll-margin-top to clear the header and
# sticky rail, so a reduced-motion-guarded GLOBAL rule is correct and must not warn.
# A jump rail's own horizontal scroller must still warn.

GUARDED_GLOBAL = """
@media (prefers-reduced-motion: no-preference){
  html{scroll-behavior:smooth;}
}
"""

RAIL_SMOOTH = """
.hgar .railA ul{display:flex;overflow-x:auto;scroll-behavior:smooth;}
"""


def test_guarded_global_smooth_scroll_is_allowed():
    assert checks_named(run(H.check_smooth_scroll, [("global.css", GUARDED_GLOBAL)]),
                        "smooth-scroll-breaks-anchors") == []


def test_unguarded_rail_smooth_scroll_still_warns():
    found = checks_named(run(H.check_smooth_scroll, [("hg.astro", RAIL_SMOOTH)]),
                         "smooth-scroll-breaks-anchors")
    assert len(found) == 1, found


if __name__ == "__main__":
    import traceback, inspect
    fns = [f for n, f in sorted(globals().items())
           if n.startswith("test_") and inspect.isfunction(f)]
    fails = 0
    for f in fns:
        try:
            f(); print(f"  ok  {f.__name__}")
        except Exception:
            fails += 1; print(f"  FAIL {f.__name__}"); traceback.print_exc()
    print(f"\n{len(fns)-fails}/{len(fns)} passed")
    sys.exit(1 if fails else 0)

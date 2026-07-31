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

# The REAL failing elements, measured in the browser: the guarantee-index links, 12.8px
# text with no vertical padding = 17px tall. Their text matches the breeder's pasted
# list exactly ("What is covered, and what voids it", "Is seventy-two hours long
# enough?", ...). Verbatim from index.astro before the fix.
HG_INDEX_CSS = """
.hgar .t4-col ul{list-style:none;margin:0;padding:0;display:grid;gap:.3rem;}
.hgar .t4-col a{font-size:.8rem;line-height:1.35;color:#4a423b;text-decoration:none;border-left:2px solid var(--bd);padding-left:.55rem;display:block;}
"""

# The jump rail, which my first cut wrongly flagged on all six pages for its 7px gap.
# Measured in the browser these pills are 202x37 — comfortably over 24x24, so axe
# target-size PASSES them and the gap is irrelevant.
HG_RAIL_CSS = """
.hgar .railA ul{display:flex;gap:7px;overflow-x:auto;list-style:none;margin:0;padding:.45rem .75rem;}
.hgar .railA a{display:inline-flex;align-items:center;gap:.35rem;font-size:.76rem;border-radius:50px;padding:7px 14px;min-height:36px;}
"""

FIXED_INDEX_CSS = """
.hgar .t4-col ul{list-style:none;margin:0;padding:0;display:grid;gap:.1rem;}
.hgar .t4-col a{font-size:.8rem;line-height:1.35;color:#4a423b;text-decoration:none;display:block;padding:.36rem .5rem;border-radius:8px;}
"""


def test_flags_undersized_index_links():
    found = checks_named(run(H.check_tap_target_spacing, [("hg.astro", HG_INDEX_CSS)]),
                         "tap-target-spacing")
    assert len(found) == 1, found
    assert "17px" in found[0]["msg"] or "under the 24px" in found[0]["msg"], found[0]["msg"]


def test_does_not_flag_a_rail_whose_pills_are_36px_tall():
    # REGRESSION: a 7px gap between 37px-tall pills is NOT an axe failure.
    assert checks_named(run(H.check_tap_target_spacing, [("hg.astro", HG_RAIL_CSS)]),
                        "tap-target-spacing") == []


def test_passes_index_links_with_padding():
    assert checks_named(run(H.check_tap_target_spacing, [("hg.astro", FIXED_INDEX_CSS)]),
                        "tap-target-spacing") == []


# ── 2b. tap-target-spacing FALSE POSITIVES (found 2026-07-26) ────────────────
# The check reported 7 ERRORs across eggs/congo/timneh/hand-raised. All 7 were
# wrong. WCAG 2.5.8 applies to pointer TARGETS; none of these are targets, and
# the two badge rules declare an explicit height the check never read.

# A decorative counter badge. Declares width/height 28px, but the check only
# consulted min-height, then guessed 19px from font-size x line-height.
# It is also a ::before — a pseudo-element can never be a pointer target.
DECORATIVE_COUNTER_CSS = """
.ds-list li::before{content:counter(ds,decimal-leading-zero);position:absolute;left:0;top:10px;font-weight:700;font-size:.85rem;color:#fff;background:var(--f);width:28px;height:28px;border-radius:9px;display:grid;place-items:center}
"""

# Same shape, 24px tick glyph inside a non-interactive <li>.
DECORATIVE_TICK_CSS = """
.chkB-grid li::before{content:"\\2713";position:absolute;left:0;top:11px;width:24px;height:24px;border-radius:8px;background:#e7f1ec;color:var(--f);font-weight:700;font-size:.8rem;display:grid;place-items:center}
"""

# A <ul> of static trust labels. No <a>, no <button> — matched only because
# "chip" appears in the class name.
STATIC_TRUST_CHIPS_CSS = """
.handraised .hero-chips{list-style:none;display:grid;grid-template-columns:auto auto;justify-content:start;gap:.4rem 1.6rem;padding:0;margin:.3rem 0 0;font-size:.8rem;color:var(--green-d);font-weight:600;}
"""

# A real link that declares height instead of min-height still has to pass.
LINK_SIZED_BY_HEIGHT_CSS = """
.railA a{display:inline-flex;align-items:center;font-size:.76rem;height:36px;padding:0 14px;}
"""


def test_does_not_flag_a_decorative_counter_pseudo_element():
    assert checks_named(run(H.check_tap_target_spacing,
                            [("congo.astro", DECORATIVE_COUNTER_CSS)]),
                        "tap-target-spacing") == []


def test_does_not_flag_a_decorative_tick_pseudo_element():
    assert checks_named(run(H.check_tap_target_spacing,
                            [("congo.astro", DECORATIVE_TICK_CSS)]),
                        "tap-target-spacing") == []


def test_does_not_flag_a_static_label_list_named_chips():
    assert checks_named(run(H.check_tap_target_spacing,
                            [("hand-raised.astro", STATIC_TRUST_CHIPS_CSS)]),
                        "tap-target-spacing") == []


def test_honours_a_declared_height_on_a_real_link():
    assert checks_named(run(H.check_tap_target_spacing,
                            [("hg.astro", LINK_SIZED_BY_HEIGHT_CSS)]),
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


# ── 7b. icon-text-baseline-drift FALSE POSITIVES (found 2026-07-26) ──────────
# The keyword was matched against everything between the previous } and the next {,
# which includes comments. A nearby "GREEN TICK" comment therefore flagged rules
# whose own selector says nothing about icons.

# .faqA is a vertical stack of accordion cards, not an icon+label row. It was
# flagged only because a comment above it mentions a tick.
COMMENT_LEAKS_KEYWORD_CSS = """
/* FAQ-A GREEN TICK accordion */
.hgar .faqA{margin:1rem 0 6px;display:flex;flex-direction:column;gap:8px;}
"""

# A grid CONTAINER that merely lays out rows; the icon+label alignment lives on
# the child li, which sets align-items itself.
CONTAINER_WITH_ALIGNED_CHILD_CSS = """
/* One-line-each trust chips: 2x2 on desktop, 2x2 on mobile — never a 3+1 orphan */
.handraised .hero-chips{list-style:none;display:grid;grid-template-columns:auto auto;gap:.4rem 1.6rem;padding:0;font-size:.8rem;}
.handraised .hero-chips li{display:inline-flex;align-items:center;gap:.35rem;white-space:nowrap;}
"""


def test_does_not_flag_a_rule_whose_keyword_came_from_a_comment():
    assert checks_named(run(H.check_icon_baseline,
                            [("hg.astro", COMMENT_LEAKS_KEYWORD_CSS)]),
                        "icon-text-baseline-drift") == []


# place-items is the shorthand for align-items + justify-items. A badge box that
# centres its own glyph with it is aligned, and is not an icon+label row anyway.
PLACE_ITEMS_SHORTHAND_CSS = """
.vf-badge{flex:none;width:28px;height:28px;border-radius:9px;background:#e7f1ec;display:grid;place-items:center;margin-top:1px}
"""


def test_treats_place_items_as_alignment():
    assert checks_named(run(H.check_icon_baseline,
                            [("eggs.astro", PLACE_ITEMS_SHORTHAND_CSS)]),
                        "icon-text-baseline-drift") == []


def test_does_not_flag_a_container_whose_child_sets_alignment():
    assert checks_named(run(H.check_icon_baseline,
                            [("hand-raised.astro", CONTAINER_WITH_ALIGNED_CHILD_CSS)]),
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


# The congo-pair page documents WHY it sets scroll-behavior:auto, and the phrase
# `scroll-behavior:smooth` inside that comment was reported as a defect (2026-07-31).
# Third recurrence of the strip-comments trap, after icon-baseline (2026-07-26) and
# the §1l selector check (2026-07-29). Prose is not code.
COMMENTED_SMOOTH = """
/* A global `scroll-behavior:smooth` turns one rail tap into a multi-second crawl,
   so this page pins scroll-behavior:auto instead. */
:global(html:has(.cpair)){scroll-behavior:auto;}
"""


def test_smooth_scroll_quoted_in_a_comment_is_not_a_defect():
    assert checks_named(run(H.check_smooth_scroll, [("cpair.astro", COMMENTED_SMOOTH)]),
                        "smooth-scroll-breaks-anchors") == []


def test_comment_stripping_does_not_blind_the_check():
    """The real declaration must still warn when it sits beside such a comment."""
    src = COMMENTED_SMOOTH + "\n.cpair .railA ul{overflow-x:auto;scroll-behavior:smooth;}\n"
    found = checks_named(run(H.check_smooth_scroll, [("cpair.astro", src)]),
                         "smooth-scroll-breaks-anchors")
    assert len(found) == 1, found


# ── 10. markup-css-drift (§1k) ───────────────────────────────────────────────
# The 2026-07-28 adoption-cost defect. The page was assembled by porting the CSS
# kit and hand-writing markup that drifted from it: 101 classes styled and never
# rendered (5 of them spec-mandated components) and 2 rendered components pointing
# at the wrong class name — FAQ question text sat in `.faqC-x`, a 16x16 icon box,
# so every question crushed to 16px. The scanner returned 0 ERROR / 0 WARN.
DRIFT_SRC = '''---
const x = 1;
---
<main class="adopt">
  <p class="faqC-x">Is the fee the same as the cost?</p>
  <div class={`tile ${x ? "on" : "off"}`}></div>
</main>
<style>
.adopt{color:#111}
.faqC-x{width:16px}
.faqC-q{font-size:1.05rem}
.doc-stack{display:grid}
.tile{border:0}
.on{opacity:1}
.off{opacity:.4}
</style>'''


def _listed(found):
    """The class names a drift finding enumerates, as a set.

    Parse the message tail rather than substring-matching it: `on` and `off` are
    substrings of ordinary prose, so a naive `"on" in msg` check passes by accident.
    """
    out = set()
    for f in found:
        if ": " in f["msg"]:
            out.update(t.strip() for t in f["msg"].split(": ", 1)[1].split(","))
    return out


def test_class_drift_reports_styled_but_never_rendered():
    found = run(H.check_class_drift, [("src/pages/adoption/index.astro", DRIFT_SRC)])
    d = checks_named(found, "markup-css-drift")
    assert d, "must report the classes that are styled but never rendered"
    listed = _listed(d)
    assert {"faqC-q", "doc-stack"} <= listed, listed


def test_class_drift_flags_spec_mandated_components_as_ERROR():
    """.doc-stack is mandated by the for-sale spec — a missing component, not dead code."""
    found = checks_named(
        run(H.check_class_drift, [("src/pages/adoption/index.astro", DRIFT_SRC)]),
        "markup-css-drift")
    errors = [f for f in found if f["sev"] == "ERROR"]
    assert errors, "a spec-mandated component must raise ERROR, not WARN"
    assert "doc-stack" in _listed(errors)
    # …and it must NOT be lumped into the deletable WARN list.
    warns = [f for f in found if f["sev"] == "WARN"]
    assert "doc-stack" not in _listed(warns)
    assert "faqC-q" in _listed(warns), "non-mandated dead code belongs in the WARN list"


def test_class_drift_reports_classes_used_with_no_css():
    src = DRIFT_SRC.replace(".faqC-x{width:16px}\n", "")
    found = run(H.check_class_drift, [("src/pages/adoption/index.astro", src)])
    assert "faqC-x" in _listed(checks_named(found, "markup-css-orphan"))


def test_class_drift_understands_template_literal_classes():
    """`class={`tile ${x?"on":"off"}`}` must count tile AND on AND off as RENDERED.

    Harvesting only the first quoted branch misreports `off` as dead code.
    """
    found = run(H.check_class_drift, [("src/pages/adoption/index.astro", DRIFT_SRC)])
    listed = _listed(found)
    for cls in ("tile", "on", "off"):
        assert cls not in listed, f"{cls} is rendered dynamically, not dead: {listed}"


def test_class_drift_skips_files_with_no_style_block():
    found = run(H.check_class_drift, [("src/pages/x/index.astro", "<main class='a'></main>")])
    assert found == []


# ── 11. component-color-loses-to-descendant (§1l) ────────────────────────────
# `.ship-tier{color:#fff}` is (0,1,0) and loses to `.ship-c p{color:#5b524a}` at
# (0,1,1): dark grey on forest green, 1.19:1, on the live adoption-cost page.
# Colour-vs-colour only — the background half (the white-on-white FAQ, where a
# `.faq-d` wrapper set background:#fff inside a dark accordion) is §1k plus the
# runtime contrast sweep §2b, and must NOT be folded in here or the check floods.
SPECIFICITY_SRC = '''<div class="ship-c">
  <p class="ship-tier">Airport pickup $185</p>
</div>
<style>
.ship-c{background:#2D6A4F}
.ship-c p{color:#5b524a}
.ship-tier{color:#fff}
</style>'''


def test_component_color_loses_to_kit_descendant_rule():
    found = run(H.check_component_color_specificity,
                [("src/pages/adoption/index.astro", SPECIFICITY_SRC)])
    d = checks_named(found, "component-color-loses-to-descendant")
    assert d, "must flag .ship-tier losing to .ship-c p"
    assert "ship-tier" in d[0]["msg"] and "ship-c p" in d[0]["msg"], d[0]["msg"]


def test_qualified_component_rule_is_not_flagged():
    """The prescribed fix — qualify the component rule — must clear the check."""
    fixed = SPECIFICITY_SRC.replace(".ship-tier{color:#fff}",
                                    ".ship-c p.ship-tier{color:#fff}")
    found = run(H.check_component_color_specificity,
                [("src/pages/adoption/index.astro", fixed)])
    assert checks_named(found, "component-color-loses-to-descendant") == []


def test_no_flag_when_the_component_class_is_never_nested_there():
    """.ship-tier used outside .ship-c cannot be beaten by `.ship-c p`."""
    other = SPECIFICITY_SRC.replace('<div class="ship-c">', '<div class="other">')
    found = run(H.check_component_color_specificity,
                [("src/pages/adoption/index.astro", other)])
    assert checks_named(found, "component-color-loses-to-descendant") == []


def test_no_flag_without_a_bare_tag_descendant_rule():
    plain = '<p class="a">x</p><style>.a{color:#fff}</style>'
    found = run(H.check_component_color_specificity, [("src/pages/x/index.astro", plain)])
    assert found == []


def test_sibling_container_is_not_a_nesting_relationship():
    """The cartesian-product bug: 586 WARNs on 8 pages, 2026-07-29.

    `.dial-ring span` and `.availB-price` both exist on adoption-cost, but
    .availB-price is never inside a .dial-ring. Requiring only "both appear
    somewhere in the file" pairs every kit descendant rule with every component
    rule and floods the gate. Nesting must be established in the DOM.
    """
    src = '''<div class="dial-ring"><span class="dial-n">3</span></div>
<div class="availB"><span class="availB-price">$1,500</span></div>
<style>
.dial-ring span{color:#9fc7b0}
.availB-price{color:#b04228}
</style>'''
    found = run(H.check_component_color_specificity, [("src/pages/x/index.astro", src)])
    assert checks_named(found, "component-color-loses-to-descendant") == [], found


def test_real_nesting_is_still_caught_when_the_container_is_deep():
    """Tightening must not blind the check: nesting through an intermediate wrapper."""
    src = '''<div class="ship-c">
  <div class="row"><p class="ship-tier">Airport $185</p></div>
</div>
<style>
.ship-c p{color:#5b524a}
.ship-tier{color:#fff}
</style>'''
    found = run(H.check_component_color_specificity, [("src/pages/x/index.astro", src)])
    assert checks_named(found, "component-color-loses-to-descendant"), found


def test_an_existing_qualified_rescue_rule_clears_the_finding():
    """5 of 8 findings on 2026-07-29 were .btn-clay, which is already rescued.

    adoption-cost ships BOTH `.btn-clay{color:#fff}` (0,1,0) and, 69 lines later,
    `.adopt-main a.btn-clay{color:#fff}` — the prescribed fix, already applied. The
    check must notice the rescue, not just the unqualified rule.
    """
    src = '''<main class="adopt-main"><a class="btn-clay" href="#r">Reserve</a></main>
<style>
.btn-clay{background:var(--clay-ink);color:#fff}
.adopt-main a{color:var(--clay-t);text-decoration:underline}
.adopt-main a.btn-clay{color:#fff}
</style>'''
    found = run(H.check_component_color_specificity, [("src/pages/x/index.astro", src)])
    assert checks_named(found, "component-color-loses-to-descendant") == [], found


def test_a_not_exclusion_on_the_descendant_rule_clears_the_finding():
    """`.xsell p:not(.xsell-k){color:...}` deliberately spares .xsell-k."""
    src = '''<div class="xsell"><p class="xsell-k">Also from our aviary</p>
<p>Another line</p></div>
<style>
.xsell p:not(.xsell-k){color:var(--mid)}
.xsell-k{color:#b04228}
</style>'''
    found = run(H.check_component_color_specificity, [("src/pages/x/index.astro", src)])
    assert checks_named(found, "component-color-loses-to-descendant") == [], found


def test_rules_quoted_inside_css_comments_are_ignored():
    """The 2026-07-26 icon-baseline bug, repeated: matching inside comments.

    adoption-cost documents its own past fix in a comment that contains the literal
    text `.ship-c p{color:#5b524a}`, so the same defect was reported twice.
    """
    src = '''<div class="ship-c"><p class="ship-price">$185</p></div>
<style>
/* .ship-tier is a <p>, so the generic `.ship-c p{color:#5b524a}` below beat it */
.ship-price{color:var(--clay-t)}
.ship-c p{color:#5b524a}
</style>'''
    found = checks_named(
        run(H.check_component_color_specificity, [("src/pages/x/index.astro", src)]),
        "component-color-loses-to-descendant")
    assert len(found) == 1, f"one defect, reported once — got {len(found)}"


def test_background_only_collision_is_not_this_checks_job():
    """The white-on-white FAQ was a BACKGROUND collision — §1k / §2b own it."""
    bg = '''<div class="faqC-item"><div class="faq-d"><p>Answer</p></div></div>
<style>
.faqC-item p{color:rgba(255,255,255,.82)}
.faq-d{background:#fff}
</style>'''
    found = run(H.check_component_color_specificity, [("src/pages/x/index.astro", bg)])
    assert checks_named(found, "component-color-loses-to-descendant") == []


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

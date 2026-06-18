# tests/test_final_page_audit.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import final_page_audit as A

def test_nested_slug_resolves_to_available_path():
    # available/roys must map to dist/available/roys/index.html
    p = A.dist_path("available/roys")
    assert str(p).endswith("dist/available/roys/index.html"), p

def test_flat_slug_resolves_unchanged():
    p = A.dist_path("african-grey-parrot-price")
    assert str(p).endswith("dist/african-grey-parrot-price/index.html"), p

MINIMAL_BIRD = """
<html><head><title>Roys — Congo African Grey for Sale | C.A.Gs</title>
<link rel="canonical" href="https://congoafricangreys.com/available/roys/">
<meta name="description" content="Roys, our hand-raised Congo African Grey, $2,300.">
<script type="application/ld+json">{"@type":"Product","offers":{"@type":"Offer","availability":"https://schema.org/InStock"}}</script>
</head><body><main><h1>Roys</h1><h2>About Roys</h2><h3>Health</h3><h4>Shipping</h4>
<p>Ships nationwide &middot; $185 airport &middot; $350 home. Captive-bred, CITES Appendix I, USDA AWA. Lifespan 40-60 years.</p>
</main><footer>(844) 820-2234</footer></body></html>
"""

def test_profile_marks_newsletter_na_for_bird():
    r = A.audit_html("available/roys", MINIMAL_BIRD, "bird")
    assert r["_severity"]["newsletter_present"] == "NA", r["_severity"]

def test_profile_marks_newsletter_fail_for_interior():
    r = A.audit_html("african-grey-parrot-care-guide", MINIMAL_BIRD, "interior")
    assert r["_severity"]["newsletter_present"] in ("FAIL", "WARN"), r["_severity"]

if __name__ == "__main__":
    import traceback, inspect
    fns = [f for n, f in sorted(globals().items()) if n.startswith("test_") and inspect.isfunction(f)]
    fails = 0
    for f in fns:
        try:
            f(); print(f"  ok  {f.__name__}")
        except Exception:
            fails += 1; print(f"  FAIL {f.__name__}"); traceback.print_exc()
    print(f"\n{len(fns)-fails}/{len(fns)} passed")
    sys.exit(1 if fails else 0)

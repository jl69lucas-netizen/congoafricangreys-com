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

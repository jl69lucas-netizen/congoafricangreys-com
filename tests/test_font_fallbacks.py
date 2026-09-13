"""Font faces must be self-hosted, with fallbacks that exist on PageSpeed's Linux Chrome.

2026-09-13: the fallback faces were hand-tuned against local('Georgia') / local('Arial'), which
PageSpeed's Linux Chrome lacks, and had no bold or italic cut (a simulated swap measured 0.029
on the buy-with-shipping hero; the generated faces measure 0). Regenerate faces with
scripts/font_fallback_metrics.py; never hand-tune them.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
STYLES = ROOT / "src/styles"
LAYOUT = ROOT / "src/layouts/BaseLayout.astro"
# Linux clones metric-identical to Arial / Times New Roman.
LINUX_CLONES = ("Liberation Sans", "Arimo", "Liberation Serif", "Tinos")


def faces():
    text = "".join(p.read_text() for p in STYLES.glob("*.css") if p.name != "cag-design-system.css")
    return re.findall(r"@font-face\s*{([^}]*)}", text)


def fallback_faces():
    return [f for f in faces() if "Fallback" in f]


def web_faces():
    return [f for f in faces() if "Fallback" not in f]


def test_every_family_has_regular_and_bold_fallbacks_and_newsreader_an_italic():
    keys = {(re.search(r"font-family:\s*'([^']+)'", f).group(1),
             re.search(r"font-weight:\s*([^;]+);", f).group(1).strip(),
             re.search(r"font-style:\s*([^;]+);", f).group(1).strip()) for f in fallback_faces()}
    assert ("IBM Plex Sans Fallback", "100 500", "normal") in keys
    assert ("IBM Plex Sans Fallback", "550 900", "normal") in keys
    assert ("Newsreader Fallback", "100 500", "normal") in keys
    assert ("Newsreader Fallback", "550 900", "normal") in keys
    assert any(k[0] == "Newsreader Fallback" and k[2] == "italic" for k in keys)


def test_every_fallback_lists_a_linux_metric_compatible_local():
    for f in fallback_faces():
        names = re.findall(r"local\('([^']+)'\)", f)
        assert any(n.startswith(LINUX_CLONES) for n in names), f


def test_no_fallback_is_based_on_georgia_which_linux_chrome_lacks():
    assert not any("Georgia" in f for f in fallback_faces())


def test_every_fallback_carries_all_four_metric_overrides():
    for f in fallback_faces():
        for prop in ("size-adjust", "ascent-override", "descent-override", "line-gap-override"):
            assert re.search(rf"{prop}:\s*[\d.]+%", f), (prop, f)


def test_web_fonts_are_self_hosted_files_that_exist():
    assert len(web_faces()) == 3
    for f in web_faces():
        url = re.search(r"url\('(/fonts/[^']+)'\)", f)
        assert url, f
        assert (ROOT / "public" / url.group(1).lstrip("/")).exists(), url.group(1)
        assert "font-display: swap" in f


def test_layout_no_longer_loads_google_fonts():
    assert "fonts.googleapis.com" not in LAYOUT.read_text()

"""Homepage review slots: the mid feature block renders Brian Carr, and Catherine Kempf
appears once (Rule 50b: no two non-empty alts on a page may match). Measured on dist/,
never on source — the gates measure what ships."""
import re
import pytest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
HOME = DIST / "index.html"
pytestmark = pytest.mark.skipif(not DIST.exists(), reason="dist/ not built — gates measure dist, never source")

def test_mid_review_is_brian_carr():
    html = HOME.read_text(encoding="utf-8")
    mid = html.split('id="reviews-mid"', 1)[1].split('</section>', 1)[0]
    assert "Brian Carr" in mid and "Plainview, TX" in mid
    assert "african-grey-review-middle.webp" in mid

def test_kempf_alt_once():
    html = HOME.read_text(encoding="utf-8")
    assert len(re.findall(r'alt="Catherine Kempf"', html)) == 1

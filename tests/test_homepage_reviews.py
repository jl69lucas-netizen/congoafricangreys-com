"""Homepage review slots: mid feature = Brian Carr; Kempf appears once (Rule 50b alt)."""
import re
from pathlib import Path
HOME = Path(__file__).resolve().parents[1] / "dist" / "index.html"

def test_mid_review_is_brian_carr():
    html = HOME.read_text(encoding="utf-8")
    mid = html.split('id="reviews-mid"', 1)[1].split('</section>', 1)[0]
    assert "Brian Carr" in mid and "Plainview, TX" in mid
    assert "african-grey-review-middle.webp" in mid

def test_kempf_alt_once():
    html = HOME.read_text(encoding="utf-8")
    assert len(re.findall(r'alt="Catherine Kempf"', html)) == 1

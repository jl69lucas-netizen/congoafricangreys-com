# tests/test_form_contract_audit.py
#
# RED fixtures for the form contract. Every case is a shape that existed on the built
# site on 2026-09-11: 14 forms posting to a Netlify handler that does not exist on
# Cloudflare, a GET to /contact-us/, two POSTs to a /thank-you/ page that does not exist,
# one form on the retired xpqoeazq ID, and 11 newsletter boxes with no name attribute.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import form_contract_audit as F

END = "https://formspree.io/f/xrejpnvn"

GOOD = f"""<form action="{END}" method="POST">
<input type="hidden" name="_subject" value="x"><input type="text" name="_gotcha" class="hp">
<input name="first_name" required><input name="phone" type="tel" required>
<input name="phone_confirm" type="tel" required><input name="email" type="email" required>
<input name="email_confirm" type="email" required>
<input type="radio" name="resale_screening" value="yes" required><input type="radio" name="resale_screening" value="no">
<textarea name="surrender_history" required></textarea>
<input type="radio" name="experience" value="experienced" required><input type="radio" name="experience" value="first-time">
<input type="radio" name="delivery" value="Airport pickup — $185" required>
<textarea name="message" required></textarea></form>"""

def page(*forms):
    return "<html><body>" + "".join(forms) + '<form action="/search/" method="get"><input name="q"></form></body></html>'

def problems(html, slug="congo-vs-timneh-african-grey"):
    return [p for row in F.audit_html(html, slug) for p in row["problems"]]

def test_compliant_inquiry_form_has_no_problems():
    assert problems(page(GOOD)) == []

def test_search_form_is_not_examined():
    rows = F.audit_html(page(GOOD), "congo-vs-timneh-african-grey")
    assert [r["kind"] for r in rows] == ["inquiry"]

def test_missing_confirm_email_is_named():
    html = page(GOOD.replace('<input name="email_confirm" type="email" required>', ""))
    assert any("confirm_email absent" in p for p in problems(html))

def test_optional_message_is_named():
    html = page(GOOD.replace('<textarea name="message" required>', '<textarea name="message">'))
    assert any("message not required" in p for p in problems(html))

def test_netlify_form_fails_on_endpoint():
    html = page(GOOD.replace(f'action="{END}" method="POST"', 'name="x" method="POST" data-netlify="true"'))
    ps = problems(html)
    assert any("endpoint" in p for p in ps) and any("netlify" in p for p in ps)

def test_newsletter_box_needs_endpoint_and_name():
    html = page('<form action="/contact-us/"><input type="email" required></form>')
    ps = problems(html)
    assert any("endpoint" in p for p in ps) and any("email input has no name" in p for p in ps)

def test_homepage_and_contact_us_and_locations_skip_field_checks_but_not_endpoint():
    optional_msg = GOOD.replace('<textarea name="message" required>', '<textarea name="message">')
    for slug in ("index", "contact-us", "african-grey-parrot-for-sale-texas"):
        assert problems(page(optional_msg), slug) == []
        assert any("endpoint" in p for p in problems(page(optional_msg.replace(END, "/thank-you/")), slug))

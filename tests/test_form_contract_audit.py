# tests/test_form_contract_audit.py
#
# RED fixtures for the form contract. Every case is a shape that existed on the built
# site on 2026-09-11: 14 forms posting to a Netlify handler that does not exist on
# Cloudflare, a GET to /contact-us/, two POSTs to a /thank-you/ page that does not exist,
# one form on the retired xpqoeazq ID, and 11 newsletter boxes with no name attribute.
import subprocess
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import form_contract_audit as F

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "form_contract_audit.py"

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

def test_locations_skip_field_checks_but_not_endpoint():
    optional_msg = GOOD.replace('<textarea name="message" required>', '<textarea name="message">')
    for slug in ("african-grey-parrot-for-sale-texas", "buy-african-grey-parrots-with-shipping"):
        assert problems(page(optional_msg), slug) == []
        assert any("endpoint" in p for p in problems(page(optional_msg.replace(END, "/thank-you/")), slug))

def test_homepage_and_contact_us_now_carry_the_full_contract():
    # Breeder lifted the opt-out on 2026-09-11 (brief Flag 1): an optional message fails there now.
    optional_msg = GOOD.replace('<textarea name="message" required>', '<textarea name="message">')
    for slug in ("index", "contact-us"):
        assert problems(page(GOOD), slug) == []
        assert any("message not required" in p for p in problems(page(optional_msg), slug))

SHORT_BLOG = f"""<form action="{END}" method="POST">
<input type="hidden" name="_subject" value="x"><input type="text" name="_gotcha" class="cf-hp">
<input name="name" required><input name="email" type="email" required>
<input name="email_confirm" type="email" required><input name="phone" type="tel" required>
<input name="phone_confirm" type="tel" required><select name="interest"><option value="">-</option></select>
<input type="radio" name="resale_screening" value="yes" required><input type="radio" name="resale_screening" value="no">
<textarea name="surrender_history" required></textarea><textarea name="message"></textarea></form>"""

def test_blog_short_contract_passes_without_experience_delivery_or_required_message():
    assert problems(page(SHORT_BLOG), "blog/african-grey-parrot-facts") == []

def test_blog_short_contract_still_names_a_missing_screening_question():
    html = page(SHORT_BLOG.replace('<textarea name="surrender_history" required></textarea>', ""))
    assert any("surrender_history absent" in p for p in problems(html, "blog/african-grey-parrot-facts"))

def test_short_form_on_a_non_blog_page_fails_the_full_contract():
    ps = problems(page(SHORT_BLOG), "how-to-avoid-african-grey-parrot-scams")
    assert any("experience absent" in p for p in ps) and any("delivery absent" in p for p in ps)


# --- Finding 1: CRITICAL zero-page PASS -------------------------------------------

def test_audit_dist_empty_returns_no_rows(tmp_path):
    assert F.audit_dist(tmp_path) == []


def test_main_fails_loud_on_zero_forms_examined(tmp_path):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--dist", str(tmp_path)],
        capture_output=True, text=True,
    )
    assert result.returncode == 2
    assert "no forms examined" in result.stdout


# --- Finding 2: conservative inquiry/newsletter classification --------------------

def test_no_textarea_inquiry_form_is_still_classed_inquiry():
    html = page(
        f'<form action="{END}" method="POST">'
        '<input name="first_name" required><input name="phone" type="tel" required>'
        '<input name="email" type="email" required></form>'
    )
    rows = F.audit_html(html, "congo-vs-timneh-african-grey")
    assert rows[0]["kind"] == "inquiry"
    assert any("message absent" in p for p in rows[0]["problems"])


# --- Finding 3: parser alignment with document.forms ------------------------------

def test_nested_form_does_not_add_a_row_or_shift_n():
    nested = GOOD.replace(
        '<input name="phone_confirm"',
        '<form action="/x" method="post"></form><input name="phone_confirm"',
        1,
    )
    rows = F.audit_html(page(nested), "congo-vs-timneh-african-grey")
    assert len(rows) == 1
    assert rows[0]["n"] == 1


def test_form_inside_template_is_not_counted():
    html = "<html><body><template>" + GOOD + "</template><p>after</p></body></html>"
    rows = F.audit_html(html, "congo-vs-timneh-african-grey")
    assert rows == []


# --- Finding 4: pin the n contract -------------------------------------------------

def test_n_is_1_based_over_all_forms_document_order_search_included():
    html = page('<form action="/search/" method="get"><input name="q"></form>' + GOOD)
    rows = F.audit_html(html, "congo-vs-timneh-african-grey")
    assert len(rows) == 1
    assert rows[0]["n"] == 2
    assert rows[0]["in_scope"] is True
    assert "email_confirm" in rows[0]["fields"]


def test_required_empty_string_attribute_counts_as_required():
    html = GOOD.replace(
        'name="email_confirm" type="email" required',
        'name="email_confirm" type="email" required=""',
    )
    rows = F.audit_html(page(html), "congo-vs-timneh-african-grey")
    assert not any("confirm_email" in p for p in rows[0]["problems"])

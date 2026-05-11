---
name: cag-contact-form
description: Audits, fixes, and deploys the parrot inquiry contact form and newsletter signup across all CAG pages. Uses [PAYMENT_METHOD_TBD] backend (ID xpqoeazq).
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG Contact Form & Newsletter Agent Skill

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the specific task genuinely cannot be done with Claude Code alone.

## Purpose
Audit, fix, and deploy the parrot inquiry contact form and email newsletter signup across all pages of CongoAfricanGreys.com. Uses [PAYMENT_METHOD_TBD] as the form backend — no server required.

---

## Key Credentials

| Item | Value |
|---|---|
| [PAYMENT_METHOD_TBD] form ID (product pages + newsletter) | `xpqoeazq` |
| Contact form action URL (product pages) | `https://formspree.io/f/xpqoeazq` |
| Newsletter form action URL | `https://formspree.io/f/xpqoeazq` |
| [PAYMENT_METHOD_TBD] dashboard (product pages) | https://formspree.io/forms/xpqoeazq/submissions |
| **Contact-Us page Formspree ID** | **`xrejpnvn`** |
| **Contact-Us form action URL** | **`https://formspree.io/f/xrejpnvn`** |
| **Contact-Us dashboard** | https://formspree.io/forms/xrejpnvn/integration |
| Reply-to email | [INQUIRIES_EMAIL_TBD] |

> **NOTE:** The `/contact-us/` page uses a **separate** Formspree endpoint (`xrejpnvn`).
> All product pages and newsletter forms continue to use `xpqoeazq`.

Both forms use the same [PAYMENT_METHOD_TBD] endpoint — differentiated by `_subject` hidden field:
- Contact form: `_subject = "New Parrot Inquiry — CongoAfricanGreys.com"`
- Newsletter: `_subject = "Newsletter Signup — CongoAfricanGreys.com"`

---

## Step 1 — Audit: Check All Pages for Broken Forms

Run this Python script from `site/content/` to find pages with broken or missing forms:

```python
import os, re
from pathlib import Path

SITE_DIR = Path("/Users/apple/Downloads/CAG/site/content")
FORMSPREE_ID = "xpqoeazq"

issues = {"wrong_id": [], "no_form": [], "sureforms": [], "ok": []}

for html_file in sorted(SITE_DIR.rglob("index.html")):
    content = html_file.read_text(errors="ignore")
    slug = str(html_file.relative_to(SITE_DIR).parent)

    has_formspree_correct = f"formspree.io/f/{FORMSPREE_ID}" in content
    has_formspree_wrong   = "formspree.io/f/" in content and not has_formspree_correct
    has_sureforms         = "srfm-form" in content or "sureforms" in content.lower()
    has_any_form          = "<form" in content

    if has_formspree_correct:
        issues["ok"].append(slug)
    elif has_formspree_wrong:
        issues["wrong_id"].append(slug)
    elif has_sureforms:
        issues["sureforms"].append(slug)
    elif not has_any_form:
        issues["no_form"].append(slug)

print(f"\n✅ Correct [PAYMENT_METHOD_TBD] form:  {len(issues['ok'])} pages")
print(f"❌ Wrong [PAYMENT_METHOD_TBD] ID:      {len(issues['wrong_id'])} pages")
print(f"⚠️  Broken SureForms:       {len(issues['sureforms'])} pages")
print(f"🔴 No form at all:         {len(issues['no_form'])} pages")

for cat, label in [("wrong_id","WRONG ID"), ("sureforms","SUREFORMS"), ("no_form","NO FORM")]:
    if issues[cat]:
        print(f"\n--- {label} ---")
        for s in issues[cat][:10]:
            print(f"  /{s}/")
        if len(issues[cat]) > 10:
            print(f"  ...and {len(issues[cat])-10} more")
```

---

## Step 2 — The Standard Form HTML Blocks

### 2A — Full 17-Field Parrot Inquiry Contact Form

Use this HTML block wherever the contact form appears. Drop it inside the page's contact section.

```html
<!-- CAG CONTACT FORM — [PAYMENT_METHOD_TBD] xpqoeazq -->
<div id="contact-form-section" style="padding: 30px 20px 20px; max-width: 720px; margin: 0 auto;">
  <form id="cag-contact-form" action="https://formspree.io/f/xpqoeazq" method="POST">
    <input type="hidden" name="_subject" value="New Parrot Inquiry — CongoAfricanGreys.com">

    <div class="fg fg-row">
      <div>
        <label for="cag-fname">First Name *</label>
        <input type="text" id="cag-fname" name="first_name" placeholder="Jane" required>
      </div>
      <div>
        <label for="cag-lname">Last Name *</label>
        <input type="text" id="cag-lname" name="last_name" placeholder="Smith" required>
      </div>
    </div>

    <div class="fg fg-row">
      <div>
        <label for="cag-email">Email *</label>
        <input type="email" id="cag-email" name="email" placeholder="your@email.com" required>
      </div>
      <div>
        <label for="cag-email2">Confirm Email *</label>
        <input type="email" id="cag-email2" name="confirm_email" placeholder="your@email.com" required>
      </div>
    </div>

    <div class="fg fg-row">
      <div>
        <label for="cag-phone">Phone *</label>
        <input type="tel" id="cag-phone" name="phone" placeholder="+1 (555) 000-0000" required>
      </div>
      <div>
        <label for="cag-phone2">Confirm Phone *</label>
        <input type="tel" id="cag-phone2" name="confirm_phone" placeholder="+1 (555) 000-0000" required>
      </div>
    </div>

    <div class="fg">
      <label for="cag-state">State / Location *</label>
      <input type="text" id="cag-state" name="state_location" placeholder="e.g. Texas, New York, California…" required>
    </div>

    <div class="fg">
      <label>Have you owned an African Grey parrot before?</label>
      <div class="check-group">
        <label><input type="checkbox" name="prior_experience" value="Yes"> Yes, I have experience with African Greys</label>
      </div>
    </div>

    <div class="fg">
      <label>Which variant interests you? *</label>
      <div class="radio-group">
        <label><input type="radio" name="variant_interest" value="Congo African Grey" required> Congo African Grey</label>
        <label><input type="radio" name="variant_interest" value="Timneh African Grey"> Timneh African Grey</label>
        <label><input type="radio" name="variant_interest" value="Not sure yet"> Not sure yet</label>
      </div>
    </div>

    <div class="fg">
      <label>Age preference: *</label>
      <div class="radio-group">
        <label><input type="radio" name="age_preference" value="Young hatchling" required> Young hatchling (newly hatched)</label>
        <label><input type="radio" name="age_preference" value="Weaned juvenile"> Weaned juvenile (3-6 months)</label>
        <label><input type="radio" name="age_preference" value="No preference"> No preference</label>
      </div>
    </div>

    <div class="fg">
      <label>TIMELINE: When do you want your parrot? *<span class="section-label">Our birds go FAST — let us know your timeline.</span></label>
      <div class="radio-group">
        <label><input type="radio" name="timeline" value="Ready NOW" required> Ready NOW</label>
        <label><input type="radio" name="timeline" value="1-2 Months"> 1–2 Months</label>
        <label><input type="radio" name="timeline" value="3-6 Months"> 3–6 Months</label>
        <label><input type="radio" name="timeline" value="Just researching"> Just researching</label>
      </div>
    </div>

    <div class="fg">
      <label for="cag-parrot">Parrot Name *</label>
      <input type="text" id="cag-parrot" name="parrot_name" placeholder="Type the exact name of the parrot you want" required>
    </div>

    <div class="fg">
      <label for="cag-alone">How many hours a day would the parrot be left alone? *</label>
      <input type="text" id="cag-alone" name="hours_alone" placeholder="e.g. 4-6 hours" required>
    </div>

    <div class="fg">
      <label for="cag-reason">What is your main reason for getting an African Grey parrot right now? *</label>
      <textarea id="cag-reason" name="main_reason" placeholder="Please share your reasons…" required></textarea>
    </div>

    <div class="fg">
      <label>Do you have the funds to pay for the parrot &amp; shipping?</label>
      <div class="check-group">
        <label><input type="checkbox" name="has_funds" value="Yes"> Yes, I have the funds available</label>
      </div>
    </div>

    <div class="fg">
      <label>How would you like to receive your parrot? *</label>
      <div class="radio-group" style="flex-direction:column;">
        <label><input type="radio" name="delivery_preference" value="Airport IATA shipping" required> ✈️ <strong>AIRPORT IATA SHIPPING</strong> — Pick up at your nearest airport with a handler (our preferred method)</label>
        <label><input type="radio" name="delivery_preference" value="Doorstep Delivery (fee applies)"> 🚗 <strong>DOORSTEP DELIVERY</strong> — Ground transport from airport to your home (fee applies)</label>
        <label><input type="radio" name="delivery_preference" value="Hold & Deliver Later"> 📦 <strong>HOLD &amp; DELIVER LATER</strong> — We hold your parrot after payment for later shipment</label>
      </div>
    </div>

    <div class="fg">
      <label for="cag-message">Your message / questions? *</label>
      <textarea id="cag-message" name="message" placeholder="Any questions or additional details…" required></textarea>
    </div>

    <button type="submit">SUBMIT FORM &rarr;</button>
    <p style="font-size:13px;color:#888;text-align:center;margin-top:10px;">We respond within 24–48 hours &bull; [INQUIRIES_EMAIL_TBD]</p>
  </form>
  <div id="cag-form-success">
    &#10003; Thank you! Your inquiry has been received.
    <p>We'll be in touch within 24–48 hours. Check your email (including spam folder).</p>
  </div>
  <script>
  (function(){
    var form=document.getElementById('cag-contact-form');
    var ok=document.getElementById('cag-form-success');
    if(!form)return;
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var e2=form.querySelector('[name=email]').value;
      var e3=form.querySelector('[name=confirm_email]').value;
      if(e2!==e3){alert('Email addresses do not match. Please check and try again.');return;}
      var p2=form.querySelector('[name=phone]').value;
      var p3=form.querySelector('[name=confirm_phone]').value;
      if(p2!==p3){alert('Phone numbers do not match. Please check and try again.');return;}
      var btn=form.querySelector('button[type=submit]');
      btn.disabled=true;btn.textContent='Sending…';
      fetch(form.action,{method:'POST',body:new FormData(form),headers:{'Accept':'application/json'}})
        .then(function(r){
          if(r.ok){form.style.display='none';ok.style.display='block';}
          else{alert('Sorry, something went wrong. Please email [INQUIRIES_EMAIL_TBD] directly.');btn.disabled=false;btn.textContent='SUBMIT FORM →';}
        })
        .catch(function(){alert('Network error. Please email [INQUIRIES_EMAIL_TBD] directly.');btn.disabled=false;btn.textContent='SUBMIT FORM →';});
    });
  })();
  </script>
</div>
```

### 2B — Newsletter Email Signup (simple, inline)

```html
<!-- CAG NEWSLETTER FORM — [PAYMENT_METHOD_TBD] xpqoeazq -->
<form id="cag-newsletter-form" action="https://formspree.io/f/xpqoeazq" method="POST">
  <input type="hidden" name="_subject" value="Newsletter Signup — CongoAfricanGreys.com">
  <input type="email" name="email" placeholder="Enter your email address…" required>
  <button type="submit">Subscribe 🐾</button>
</form>
<div id="cag-nl-success">✅ You're on the list! We'll notify you first when new clutches arrive.</div>
<script>
(function(){
  var f=document.getElementById('cag-newsletter-form');
  var s=document.getElementById('cag-nl-success');
  if(!f)return;
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var btn=f.querySelector('button');btn.disabled=true;btn.textContent='Subscribing…';
    fetch(f.action,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}})
      .then(function(r){if(r.ok){f.style.display='none';s.style.display='block';}else{btn.disabled=false;btn.textContent='Subscribe 🐾';}})
      .catch(function(){btn.disabled=false;btn.textContent='Subscribe 🐾';});
  });
})();
</script>
```

---

## Step 3 — Required CSS (add to `<head>` or page `<style>` block)

This CSS must be present on any page using the CAG forms. On the homepage it lives in `<style id="wp-custom-css">`.

```css
/* CAG Contact & Newsletter Form Styles */
#cag-contact-form { font-family: inherit; }
#cag-contact-form .fg { margin-bottom: 16px; }
#cag-contact-form .fg-row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
#cag-contact-form label { display: block; font-weight: 600; margin-bottom: 5px; color: #2D6A4F; font-size: 14px; }
#cag-contact-form input[type=text],
#cag-contact-form input[type=email],
#cag-contact-form input[type=tel],
#cag-contact-form textarea {
  width: 100%; padding: 11px 14px; border: 1.5px solid #d4c9bc;
  border-radius: 8px; font-size: 15px; font-family: inherit;
  box-sizing: border-box; background: #fff; color: #333;
  transition: border-color .2s;
}
#cag-contact-form input:focus,
#cag-contact-form textarea:focus { outline: none; border-color: #2D6A4F; }
#cag-contact-form textarea { height: 110px; resize: vertical; }
#cag-contact-form .radio-group, #cag-contact-form .check-group { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }
#cag-contact-form .radio-group label, #cag-contact-form .check-group label {
  display: flex; align-items: center; gap: 6px; font-weight: 400;
  color: #333; cursor: pointer; font-size: 14px; margin-bottom: 0;
  background: #f7f4f0; border: 1.5px solid #ddd; border-radius: 6px; padding: 7px 12px;
  transition: border-color .2s, background .2s;
}
#cag-contact-form .radio-group label:has(input:checked),
#cag-contact-form .check-group label:has(input:checked) {
  border-color: #2D6A4F; background: #eaf4ef; color: #2D6A4F; font-weight: 600;
}
#cag-contact-form .radio-group input, #cag-contact-form .check-group input { accent-color: #2D6A4F; }
#cag-contact-form .section-label { font-size: 13px; color: #777; margin-bottom: 6px; margin-top: 4px; display: block; }
#cag-contact-form button[type=submit] {
  background: #F4A261; color: #fff; border: none; padding: 15px 40px;
  border-radius: 50px; font-size: 16px; font-weight: 700; cursor: pointer;
  transition: background .2s; width: 100%; margin-top: 8px; letter-spacing: .3px;
}
#cag-contact-form button[type=submit]:hover { background: #e8914d; }
#cag-form-success { display:none; background:#eaf4ef; border:1px solid #a5d6a7; border-radius:10px; padding:24px; text-align:center; color:#2D6A4F; font-weight:700; margin-top:20px; font-size:16px; }
#cag-form-success p { margin: 8px 0 0; font-weight:400; color:#444; font-size:14px; }
/* Newsletter */
#cag-newsletter-form { display:flex; gap:10px; flex-wrap:wrap; margin-top:16px; }
#cag-newsletter-form input[type=email] {
  flex:1; min-width:200px; padding:12px 18px; border:1.5px solid #d4c9bc;
  border-radius:50px; font-size:15px; font-family:inherit; outline:none; background:#fff;
}
#cag-newsletter-form input[type=email]:focus { border-color:#2D6A4F; }
#cag-newsletter-form button { background:#F4A261; color:#fff; border:none; padding:12px 28px; border-radius:50px; font-size:15px; font-weight:700; cursor:pointer; transition:background .2s; }
#cag-newsletter-form button:hover { background:#e8914d; }
#cag-nl-success { display:none; background:#eaf4ef; border:1px solid #a5d6a7; border-radius:8px; padding:14px 18px; color:#2D6A4F; font-weight:600; margin-top:12px; }
@media(max-width:600px){
  #cag-contact-form .fg-row { grid-template-columns: 1fr; }
}
```

---

## Step 4 — Batch Fix: Apply Form to All Pages

Run this Python script to insert the contact form into every page that has a contact section placeholder or broken SureForms:

```python
import os, re
from pathlib import Path

SITE_DIR = Path("/Users/apple/Downloads/CAG/site/content")
FORMSPREE_ID = "xpqoeazq"

# CSS block to inject into <head> if missing
CSS_BLOCK = """<style id="cag-form-css">
/* CAG Form Styles — see cag-contact-form.md for full CSS */
#cag-contact-form .fg{margin-bottom:16px}
#cag-contact-form .fg-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
#cag-contact-form label{display:block;font-weight:600;margin-bottom:5px;color:#2D6A4F;font-size:14px}
#cag-contact-form input,#cag-contact-form textarea{width:100%;padding:11px 14px;border:1.5px solid #d4c9bc;border-radius:8px;font-size:15px;box-sizing:border-box;background:#fff;color:#333}
#cag-contact-form input:focus,#cag-contact-form textarea:focus{outline:none;border-color:#2D6A4F}
#cag-contact-form .radio-group,#cag-contact-form .check-group{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}
#cag-contact-form .radio-group label,#cag-contact-form .check-group label{display:flex;align-items:center;gap:6px;font-weight:400;font-size:14px;margin-bottom:0;background:#f7f4f0;border:1.5px solid #ddd;border-radius:6px;padding:7px 12px}
#cag-contact-form .radio-group label:has(input:checked),#cag-contact-form .check-group label:has(input:checked){border-color:#2D6A4F;background:#eaf4ef;color:#2D6A4F;font-weight:600}
#cag-contact-form button[type=submit]{background:#F4A261;color:#fff;border:none;padding:15px 40px;border-radius:50px;font-size:16px;font-weight:700;cursor:pointer;width:100%;margin-top:8px}
#cag-form-success{display:none;background:#eaf4ef;border:1px solid #a5d6a7;border-radius:10px;padding:24px;text-align:center;color:#2D6A4F;font-weight:700;margin-top:20px}
#cag-newsletter-form{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
#cag-newsletter-form input{flex:1;min-width:200px;padding:12px 18px;border:1.5px solid #d4c9bc;border-radius:50px;font-size:15px}
#cag-newsletter-form button{background:#F4A261;color:#fff;border:none;padding:12px 28px;border-radius:50px;font-size:15px;font-weight:700;cursor:pointer}
#cag-nl-success{display:none;background:#eaf4ef;border-radius:8px;padding:14px 18px;color:#2D6A4F;font-weight:600;margin-top:12px}
@media(max-width:600px){#cag-contact-form .fg-row{grid-template-columns:1fr}}
</style>"""

CONTACT_FORM_HTML = """<div id="contact-form-section" style="padding:30px 20px;max-width:720px;margin:0 auto;">
  <form id="cag-contact-form" action="https://formspree.io/f/xpqoeazq" method="POST">
    <input type="hidden" name="_subject" value="New Parrot Inquiry — CongoAfricanGreys.com">
    <div class="fg fg-row"><div><label>First Name *</label><input type="text" name="first_name" placeholder="Jane" required></div><div><label>Last Name *</label><input type="text" name="last_name" placeholder="Smith" required></div></div>
    <div class="fg fg-row"><div><label>Email *</label><input type="email" name="email" placeholder="your@email.com" required></div><div><label>Confirm Email *</label><input type="email" name="confirm_email" placeholder="your@email.com" required></div></div>
    <div class="fg fg-row"><div><label>Phone *</label><input type="tel" name="phone" placeholder="+1 (555) 000-0000" required></div><div><label>Confirm Phone *</label><input type="tel" name="confirm_phone" placeholder="+1 (555) 000-0000" required></div></div>
    <div class="fg"><label>State / Location *</label><input type="text" name="state_location" placeholder="e.g. Texas, New York…" required></div>
    <div class="fg"><label>Have you owned an African Grey parrot before?</label><div class="check-group"><label><input type="checkbox" name="prior_experience" value="Yes"> Yes, I have experience with African Greys</label></div></div>
    <div class="fg"><label>Which variant interests you? *</label><div class="radio-group"><label><input type="radio" name="variant_interest" value="Congo African Grey" required> Congo African Grey</label><label><input type="radio" name="variant_interest" value="Timneh African Grey"> Timneh African Grey</label><label><input type="radio" name="variant_interest" value="Not sure yet"> Not sure yet</label></div></div>
    <div class="fg"><label>Age preference: *</label><div class="radio-group"><label><input type="radio" name="age_preference" value="Young hatchling" required> Young hatchling</label><label><input type="radio" name="age_preference" value="Weaned juvenile"> Weaned juvenile</label><label><input type="radio" name="age_preference" value="No preference"> No preference</label></div></div>
    <div class="fg"><label>TIMELINE: When do you want your parrot? *</label><div class="radio-group"><label><input type="radio" name="timeline" value="Ready NOW" required> Ready NOW</label><label><input type="radio" name="timeline" value="1-2 Months"> 1–2 Months</label><label><input type="radio" name="timeline" value="3-6 Months"> 3–6 Months</label><label><input type="radio" name="timeline" value="Just researching"> Just researching</label></div></div>
    <div class="fg"><label>Parrot Name *</label><input type="text" name="parrot_name" placeholder="Type the exact name of the parrot you want" required></div>
    <div class="fg"><label>Hours parrot would be left alone per day? *</label><input type="text" name="hours_alone" placeholder="e.g. 4-6 hours" required></div>
    <div class="fg"><label>Main reason for getting an African Grey parrot right now? *</label><textarea name="main_reason" style="height:100px;resize:vertical" required></textarea></div>
    <div class="fg"><label>Do you have funds for parrot &amp; shipping?</label><div class="check-group"><label><input type="checkbox" name="has_funds" value="Yes"> Yes, I have the funds available</label></div></div>
    <div class="fg"><label>How would you like to receive your parrot? *</label><div class="radio-group" style="flex-direction:column"><label><input type="radio" name="delivery_preference" value="Airport IATA shipping" required> ✈️ <strong>AIRPORT IATA SHIPPING</strong> — Pick up at your local airport with handler</label><label><input type="radio" name="delivery_preference" value="Doorstep Delivery (fee applies)"> 🚗 <strong>DOORSTEP DELIVERY</strong> — Ground transport (fee applies)</label><label><input type="radio" name="delivery_preference" value="Hold & Deliver Later"> 📦 <strong>HOLD &amp; DELIVER LATER</strong> — Hold after payment for later shipment</label></div></div>
    <div class="fg"><label>Your message / questions? *</label><textarea name="message" required placeholder="Any questions…" style="height:110px;resize:vertical"></textarea></div>
    <button type="submit">SUBMIT FORM &rarr;</button>
    <p style="font-size:13px;color:#888;text-align:center;margin-top:10px">We respond within 24–48 hours &bull; [INQUIRIES_EMAIL_TBD]</p>
  </form>
  <div id="cag-form-success">&#10003; Thank you! Your inquiry has been received.<br><small>We'll be in touch within 24–48 hours. Check your email including spam folder.</small></div>
  <script>(function(){var f=document.getElementById('cag-contact-form'),ok=document.getElementById('cag-form-success');if(!f)return;f.addEventListener('submit',function(e){e.preventDefault();if(f.querySelector('[name=email]').value!==f.querySelector('[name=confirm_email]').value){alert('Email addresses do not match.');return;}if(f.querySelector('[name=phone]').value!==f.querySelector('[name=confirm_phone]').value){alert('Phone numbers do not match.');return;}var btn=f.querySelector('button');btn.disabled=true;btn.textContent='Sending…';fetch(f.action,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}}).then(function(r){if(r.ok){f.style.display='none';ok.style.display='block';}else{btn.disabled=false;btn.textContent='SUBMIT FORM →';}}).catch(function(){btn.disabled=false;btn.textContent='SUBMIT FORM →';});});})();</script>
</div>"""

fixed = 0
for html_file in sorted(SITE_DIR.rglob("index.html")):
    content = html_file.read_text(errors="ignore")
    slug = str(html_file.relative_to(SITE_DIR).parent)

    changed = False

    # Inject CSS if not present
    if "cag-form-css" not in content and "cag-contact-form" not in content:
        content = content.replace("</head>", CSS_BLOCK + "\n</head>", 1)
        changed = True

    # Fix wrong [PAYMENT_METHOD_TBD] ID
    if "formspree.io/f/" in content and f"formspree.io/f/{FORMSPREE_ID}" not in content:
        content = re.sub(r'formspree\.io/f/[a-z0-9]+', f'formspree.io/f/{FORMSPREE_ID}', content)
        changed = True

    if changed:
        html_file.write_text(content)
        print(f"  Fixed: /{slug}/")
        fixed += 1

print(f"\nTotal fixed: {fixed} pages")
```

---

## Step 5 — Deploy After Fixes

```bash
cd /Users/apple/Downloads/CAG/site/content
# Stage changes and deploy via the CAG deployment process
# (Deploy method TBD — Phase 2)
```

---

## Step 6 — Submit Changed Pages to IndexNow

```python
import json, urllib.request

key = "[INDEXNOW_KEY_TBD]"
# List all pages where the form was added or fixed:
urls = [
    "https://congoafricangreys.com/",
    "https://congoafricangreys.com/contact/",
    # ...add any other fixed pages
]
payload = json.dumps({"host":"congoafricangreys.com","key":key,
    "keyLocation":f"https://congoafricangreys.com/{key}.txt","urlList":urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow",data=payload,
    headers={"Content-Type":"application/json; charset=utf-8"},method="POST")
print(urllib.request.urlopen(req).status)  # 202 = success
```

---

## What Was Fixed on Homepage (2026-04-21)

| Issue | Before | After |
|---|---|---|
| [PAYMENT_METHOD_TBD] form ID | `xdkobvpq` (wrong) | `xpqoeazq` (correct) |
| Contact form fields | 5 basic fields | 17 fields (full inquiry form) |
| Email validation | None | Client-side email + phone confirmation match |
| Newsletter | Broken SureForms WordPress plugin | Working [PAYMENT_METHOD_TBD] email subscription |
| Form CSS | Old gold color scheme | CAG design system (#2D6A4F green, #F4A261 orange) |
| Submit feedback | Basic alert | Inline success message, button state feedback |

---

## Reporting Format

```
CONTACT FORM AUDIT — congoafricangreys.com
==========================================
Pages scanned:           [SCANNED]
✅ Correct [PAYMENT_METHOD_TBD] ID:  [COUNT]
❌ Wrong [PAYMENT_METHOD_TBD] ID:    [COUNT]
⚠️  Broken legacy forms: [COUNT]
🔴 No form at all:       [COUNT]

ACTIONS TAKEN:
  ✅ Homepage: replaced 5-field form with 17-field form
  ✅ Newsletter: replaced broken SureForms with [PAYMENT_METHOD_TBD] email form
  ✅ CSS updated to CAG design system
  ✅ Deployed to Netlify via GitHub push
  ✅ IndexNow notified: 2 URLs
```
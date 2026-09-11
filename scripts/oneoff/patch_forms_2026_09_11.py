#!/usr/bin/env python3
"""One-off, idempotent: apply the 2026-09-11 form field contract to the near-identical
form families. Every substitution must match exactly once or the file is left untouched.

  python3 scripts/oneoff/patch_forms_2026_09_11.py --check   # report only
  python3 scripts/oneoff/patch_forms_2026_09_11.py           # write
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WRITE = "--check" not in sys.argv
STAR = ' <span class="req">*</span>'
NEXT = "https://congoafricangreys.com/contact-us/?success=true"

COMPARISON = ["congo-vs-timneh-african-grey", "african-grey-comparison", "african-grey-vs-cockatoo",
              "african-grey-parrot-breeders-comparison", "african-grey-vs-amazon-parrot",
              "african-grey-vs-macaw", "african-grey-pros-and-cons", "male-vs-female-african-grey-parrots-for-sale"]
FORSALE = ["congo-african-grey-for-sale", "timneh-african-grey-for-sale", "african-grey-parrot-bird-eggs-for-sale-usa"]
BIRDS = ["roys", "amie", "bery", "elad", "evie", "jins-jeni"]

DLV = [("airport", "Airport pickup — $185", "Airport Pickup · $185",
        "Flies on IATA live-animal terms with Delta, United or American to your nearest major airport; you collect at the airline's cargo desk."),
       ("home", "Home delivery — $350", "Home Delivery · $350",
        "Brought to the address you give us, on a date we agree with you first."),
       ("nanny", "Flight nanny — from $750", "Flight Nanny · from $750",
        "A nanny keeps your grey in the cabin for the whole flight; quoted per route."),
       ("midland", "Pickup in Midland, TX", "Local Pickup · Free",
        "Collect from us in Midland, TX if you live within two to three hours.")]


def sub1(s, pattern, repl, what, flags=0):
    new, n = re.subn(pattern, repl, s, flags=flags)
    if n != 1:
        raise RuntimeError(f"{what}: expected 1 match, got {n}")
    return new


def endpoint_block(slug):
    return (f'<input type="hidden" name="_subject" value="C.A.Gs inquiry — {slug}">\n'
            f'<input type="hidden" name="_next" value="{NEXT}">\n'
            '<input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">')


# ── cta-form vocabulary (comparison + for-sale) ─────────────────────────────────
def cta_screen(P):
    return f'''<fieldset class="fset">
  <legend>Are you involved in any pet store, commercial parrot breeding operation, or getting parrots for cheap resale?{STAR}</legend>
  <div class="rad">
    <label for="{P}-resale-yes"><input id="{P}-resale-yes" type="radio" name="resale_screening" value="yes" required> Yes</label>
    <label for="{P}-resale-no"><input id="{P}-resale-no" type="radio" name="resale_screening" value="no" required> No</label>
  </div>
</fieldset>
<label for="{P}-surrender">Have you ever surrendered a pet to a shelter or given one away?{STAR}<textarea id="{P}-surrender" name="surrender_history" rows="3" required placeholder="If yes, please explain in detail. Honest answers are appreciated."></textarea></label>
<fieldset class="fset">
  <legend>Are you a First-Time or Experienced Parrot Owner?{STAR}</legend>
  <div class="rad">
    <label for="{P}-exp-experienced"><input id="{P}-exp-experienced" type="radio" name="experience" value="experienced" required> Experienced owner</label>
    <label for="{P}-exp-first"><input id="{P}-exp-first" type="radio" name="experience" value="first-time" required> First-time owner</label>
  </div>
</fieldset>'''


def cta_delivery(P, legend="How would you like your grey to reach you?"):
    rows = "\n".join(
        f'    <label for="{P}-dlv-{k}"><input id="{P}-dlv-{k}" type="radio" name="delivery" value="{v}" required><span class="t">{t}</span><span class="d">{d}</span></label>'
        for k, v, t, d in DLV)
    return f'<fieldset class="fset">\n  <legend>{legend}{STAR}</legend>\n  <div class="dlv">\n{rows}\n  </div>\n</fieldset>'


CTA_CSS = """.cta-form .req{color:#b04228;font-weight:700}
.cta-form .fset{border:0;padding:0;margin:0;min-width:0;display:grid;gap:6px}
.cta-form .fset legend{padding:0;font-size:.85rem;font-weight:600;color:#3a332c}
.cta-form .rad{display:flex;flex-wrap:wrap;gap:10px}
.cta-form .rad label{display:flex;align-items:center;gap:8px;padding:9px 18px;border:1.5px solid #ede5dc;border-radius:50px;background:#fff9f6;cursor:pointer}
.cta-form .rad label:has(input:checked){border-color:#e8604c;background:rgba(232,96,76,.06);color:#b04228}
.cta-form .dlv{display:grid;gap:8px}
.cta-form .dlv label{display:grid;grid-template-columns:auto 1fr;column-gap:10px;row-gap:2px;align-items:start;padding:10px 14px;border:1.5px solid #ede5dc;border-radius:12px;background:#fff9f6;cursor:pointer}
.cta-form .dlv label:has(input:checked){border-color:#e8604c;background:rgba(232,96,76,.05)}
.cta-form .dlv input{grid-row:span 2;margin-top:3px}
.cta-form .dlv .t{font-weight:700}
.cta-form .dlv .d{grid-column:2;font-weight:400;font-size:.8rem;color:#7a6f64;line-height:1.45}
.cta-form .rad input,.cta-form .dlv input{width:auto;padding:0;border:0;border-radius:0;background:none;box-shadow:none;accent-color:#e8604c}
"""


def patch_cta(slug, family):
    path = ROOT / "src/pages" / slug / "index.astro"
    s = path.read_text()
    if 'name="resale_screening"' in s:
        return "already patched"
    # Every substitution runs on the FORM BLOCK only. Comparison pages carry other labelled
    # inputs (decision modules, calculators); a page-wide star regex would decorate them.
    fm = re.search(r'<form class="cta-form"[\s\S]*?</form>', s)
    if not fm:
        raise RuntimeError("no .cta-form block")
    page_before, s, page_after = s[:fm.start()], fm.group(0), s[fm.end():]
    P = re.search(r'id="([a-z]+)-delivery"', s).group(1)
    legend = "How would you like your eggs or grey to reach you?" if "eggs" in slug else "How would you like your grey to reach you?"
    # 1. form tag + endpoint, honeypot
    s = sub1(s, r'<form class="cta-form" name="[a-z-]+" method="POST" data-netlify="true" netlify-honeypot="bot-field">',
             f'<form class="cta-form" action="https://formspree.io/f/xrejpnvn" method="POST">\n' + endpoint_block(slug), "form tag")
    s = sub1(s, r'\n\s*<input type="hidden" name="form-name" value="[^"]+" />\s*<p class="hp"><label>[^<]*<input name="bot-field" /></label></p>', "", "netlify honeypot")
    # 2. for-sale family: split the cell|email row into cell|confirm + email|confirm
    if family == "forsale":
        s = sub1(s, rf'<div class="form-2col">\s*(<label for="{P}-cell">[^\n]*</label>)\s*(<label for="{P}-email">[^\n]*</label>)\s*</div>',
                 lambda m: (f'<div class="form-2col">\n{m.group(1)}\n'
                            f'<label for="{P}-cell2">Confirm cell number{STAR}<input id="{P}-cell2" name="cell_confirm" type="tel" required></label>\n</div>\n'
                            f'<div class="form-2col">\n{m.group(2)}\n'
                            f'<label for="{P}-email2">Confirm email{STAR}<input id="{P}-email2" name="email_confirm" type="email" required></label>\n</div>'),
                 "cell/email row", re.S)
    # 3. delivery select → screening block + delivery radios
    s = sub1(s, rf'<label for="{P}-delivery">[\s\S]*?</select>\s*</label>', cta_screen(P) + "\n" + cta_delivery(P, legend), "delivery select", re.S)
    # 4. message required
    s = sub1(s, r'<span class="opt">\(optional\)</span>(<textarea id="[\w-]+-msg" name="message" rows="\d")',
             r'<span class="req">*</span>\1 required', "message optional→required")
    # 5. stars on every remaining labelled input/select (message + screening already carry one)
    s = re.sub(r'(<label for="[\w-]+">)([^<\n]+?)(\s*)(<input|<select)',
               lambda m: m.group(1) + m.group(2).rstrip() + STAR + m.group(3) + m.group(4), s)
    # 6. splice the patched form back, then CSS on the whole page
    s = page_before + s + page_after
    s = sub1(s, r'\.form-note\{font-size:\.8rem', CTA_CSS + ".form-note{font-size:.8rem", "css anchor")
    if WRITE:
        path.write_text(s)
    return "patched"


# ── Tailwind bird-page vocabulary ───────────────────────────────────────────────
L = 'class="block font-sora text-xs font-semibold uppercase tracking-wide text-stone-600 mb-1.5"'
I = 'class="w-full rounded-xl border border-stone-300 bg-white px-4 py-3 font-sora text-sm text-stone-800 focus:border-green focus:ring-2 focus:ring-green/20 focus:outline-none"'
PILL = 'class="inline-flex items-center gap-2 rounded-full border border-stone-300 bg-white px-4 py-2 font-sora text-sm font-semibold text-stone-700 cursor-pointer has-[:checked]:border-clay has-[:checked]:text-clay-text"'
CARD = 'class="grid grid-cols-[auto_1fr] gap-x-3 gap-y-0.5 items-start rounded-xl border border-stone-300 bg-white px-4 py-3 cursor-pointer has-[:checked]:border-clay"'
REQ = '<span class="text-clay-text">*</span>'


def bird_block(P, name):
    dlv = "\n".join(
        f'      <label {CARD}><input type="radio" name="delivery" value="{v}" required class="row-span-2 mt-1" style="accent-color:#e8604c" /><span class="font-sora text-sm font-bold text-stone-800">{t}</span><span class="font-sora text-xs text-stone-600 leading-snug">{d}</span></label>'
        for k, v, t, d in DLV)
    return f'''<div class="grid sm:grid-cols-2 gap-4">
    <div>
      <label for="{P}-email-confirm" {L}>Confirm email {REQ}</label>
      <input id="{P}-email-confirm" name="email_confirm" type="email" required placeholder="Repeat your email" {I} />
    </div>
    <div>
      <label for="{P}-phone-confirm" {L}>Confirm number {REQ}</label>
      <input id="{P}-phone-confirm" name="phone_confirm" type="tel" required placeholder="Repeat your number" {I} />
    </div>
  </div>
  <fieldset class="border-0 p-0 min-w-0">
    <legend {L.replace("mb-1.5", "mb-2 p-0")}>Are you involved in any pet store, commercial parrot breeding operation, or getting parrots for cheap resale? {REQ}</legend>
    <div class="flex flex-wrap gap-2.5">
      <label {PILL}><input type="radio" name="resale_screening" value="yes" required style="accent-color:#e8604c" /> Yes</label>
      <label {PILL}><input type="radio" name="resale_screening" value="no" required style="accent-color:#e8604c" /> No</label>
    </div>
  </fieldset>
  <div>
    <label for="{P}-surrender" {L}>Have you ever surrendered a pet to a shelter or given one away? {REQ}</label>
    <textarea id="{P}-surrender" name="surrender_history" rows="3" required placeholder="If yes, please explain in detail. Honest answers are appreciated." {I}></textarea>
  </div>
  <fieldset class="border-0 p-0 min-w-0">
    <legend {L.replace("mb-1.5", "mb-2 p-0")}>Are you a First-Time or Experienced Parrot Owner? {REQ}</legend>
    <div class="flex flex-wrap gap-2.5">
      <label {PILL}><input type="radio" name="experience" value="experienced" required style="accent-color:#e8604c" /> Experienced owner</label>
      <label {PILL}><input type="radio" name="experience" value="first-time" required style="accent-color:#e8604c" /> First-time owner</label>
    </div>
  </fieldset>
  <fieldset class="border-0 p-0 min-w-0">
    <legend {L.replace("mb-1.5", "mb-2 p-0")}>How would you like {name} to reach you? {REQ}</legend>
    <div class="grid gap-2">
{dlv}
    </div>
  </fieldset>
  '''


def patch_bird(slug):
    path = ROOT / "src/pages/available" / slug / "index.astro"
    s = path.read_text()
    if 'name="resale_screening"' in s:
        return "already patched"
    P = slug
    name = {"roys": "Roys", "amie": "Amie", "bery": "Bery", "elad": "Elad", "evie": "Evie", "jins-jeni": "Jins and Jeni"}[slug]
    s = sub1(s, rf'(\n\s*)(<div>\s*<label for="{P}-msg")', lambda m: m.group(1) + bird_block(P, name) + m.group(2), "insert before message", re.S)
    s = sub1(s, r'Tell us about your home <span class="font-normal normal-case text-stone-600">\(optional\)</span>', f"Tell us about your home {REQ}", "message label")
    s = sub1(s, rf'(<textarea id="{P}-msg" name="message" rows="3")', r"\1 required", "message required")
    if slug == "evie":  # hidden bird value + subject said ELAD / Male (brief Open Flag 5)
        s = sub1(s, r'value="ELAD — Timneh African Grey, Male, 6 months \(\$1,500, was \$2,200\)"', 'value="EVIE — Timneh African Grey, Female, 6 months ($1,500, was $2,200)"', "evie bird value")
        s = sub1(s, r'value="Reserve Evie — Male Timneh', 'value="Reserve Evie — Female Timneh', "evie subject")
    if WRITE:
        path.write_text(s)
    return "patched"


if __name__ == "__main__":
    ok = True
    for slug in COMPARISON:
        try: print(f"{slug:55} {patch_cta(slug, 'comparison')}")
        except Exception as e: ok = False; print(f"{slug:55} ERROR {e}")
    for slug in FORSALE:
        try: print(f"{slug:55} {patch_cta(slug, 'forsale')}")
        except Exception as e: ok = False; print(f"{slug:55} ERROR {e}")
    for slug in BIRDS:
        try: print(f"{'available/' + slug:55} {patch_bird(slug)}")
        except Exception as e: ok = False; print(f"{'available/' + slug:55} ERROR {e}")
    print("MODE:", "wrote" if WRITE else "check only")
    sys.exit(0 if ok else 1)

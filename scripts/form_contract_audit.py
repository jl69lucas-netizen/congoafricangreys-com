#!/usr/bin/env python3
"""Form contract audit over dist/.

Every non-search <form> must POST to the one Formspree endpoint with no Netlify residue.
Every inquiry form (a form with a <textarea>) on an in-scope page must carry the seven
screening fields, each required. Excluded from the FIELD checks only: the homepage,
/contact-us/, and the location cluster (which has no forms today).

  python3 scripts/form_contract_audit.py              # table + exit 1 on any problem
  python3 scripts/form_contract_audit.py --json out.json   # rows for form_contract_browser.mjs
"""
import argparse, json, re, sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _slugs import page_key  # noqa: E402

ENDPOINT = "https://formspree.io/f/xrejpnvn"
KEYS = [
    ("confirm_number", re.compile(r"^(phone|cell|mobile)[_-]?confirm$")),
    ("confirm_email", re.compile(r"^email[_-]?confirm$")),
    ("resale_screening", re.compile(r"^resale_screening$")),
    ("surrender_history", re.compile(r"^surrender_history$")),
    ("experience", re.compile(r"^experience$")),
    ("delivery", re.compile(r"^delivery(_method)?$")),
    ("message", re.compile(r"^(message|msg)$")),
]
LOCATION = re.compile(r"^(african-grey-parrots?-for-sale-|buy-)")


def field_checks_apply(slug: str) -> bool:
    return slug not in ("index", "contact-us") and not LOCATION.match(slug)


class _Forms(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms, self._cur = [], None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "form":
            self._cur = {"attrs": a, "controls": []}
            self.forms.append(self._cur)
        elif tag in ("input", "select", "textarea") and self._cur is not None:
            self._cur["controls"].append({
                "tag": tag, "name": a.get("name"), "type": a.get("type", "text" if tag == "input" else tag),
                "required": "required" in a,
            })

    def handle_endtag(self, tag):
        if tag == "form":
            self._cur = None


def audit_html(html: str, slug: str):
    p = _Forms(); p.feed(html)
    rows = []
    for n, f in enumerate(p.forms, 1):
        a, ctl = f["attrs"], f["controls"]
        action = a.get("action", "") or ""
        if action.startswith("/search"):
            continue
        kind = "inquiry" if any(c["tag"] == "textarea" for c in ctl) else "newsletter"
        problems = []
        if action != ENDPOINT:
            problems.append(f'endpoint is "{action or "(none)"}", must be {ENDPOINT}')
        if "data-netlify" in a or "netlify-honeypot" in a or any(c["name"] in ("form-name", "bot-field") for c in ctl):
            problems.append("netlify residue (data-netlify / form-name / bot-field)")
        if (a.get("method") or "get").lower() != "post":
            problems.append(f'method is {a.get("method") or "GET"}, must be POST')
        if kind == "newsletter" and any(c["type"] == "email" and not c["name"] for c in ctl):
            problems.append("email input has no name attribute — Formspree receives nothing")
        if kind == "inquiry" and field_checks_apply(slug):
            for key, rx in KEYS:
                hits = [c for c in ctl if c["name"] and rx.match(c["name"])]
                if not hits:
                    problems.append(f"{key} absent")
                elif not any(c["required"] for c in hits):
                    problems.append(f"{key} not required")
        rows.append({"slug": slug, "n": n, "name": a.get("name") or a.get("class", "").split(" ")[0] or "form",
                     "kind": kind, "action": action, "fields": sorted({c["name"] for c in ctl if c["name"]}),
                     "in_scope": kind == "inquiry" and field_checks_apply(slug), "problems": problems})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json"); ap.add_argument("--dist", default="dist")
    args = ap.parse_args()
    dist = Path(args.dist)
    rows = []
    for path in sorted(dist.rglob("index.html")):
        rows += audit_html(path.read_text(encoding="utf-8"), page_key(path, dist))
    bad = [r for r in rows if r["problems"]]
    inquiry = [r for r in rows if r["kind"] == "inquiry"]
    print(f"forms examined: {len(rows)}  (inquiry {len(inquiry)}, in-scope {sum(r['in_scope'] for r in rows)}, newsletter {len(rows) - len(inquiry)})")
    for r in bad:
        print(f"FAIL {r['slug']} form#{r['n']} [{r['name']}] {r['action'] or '(no action)'}")
        for p in r["problems"]:
            print(f"     - {p}")
    if args.json:
        Path(args.json).write_text(json.dumps(rows, indent=1))
    print("PASS" if not bad else f"{len(bad)} form(s) fail the contract")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

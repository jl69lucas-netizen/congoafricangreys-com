#!/usr/bin/env python3
"""Form contract audit over dist/.

Every non-search <form> must POST to the one Formspree endpoint with no Netlify residue.
A form is classed "newsletter" only when its non-hidden, non-_gotcha controls are
exactly one type="email" input; every other form (including one with no textarea) is
classed "inquiry" and must carry its page's contract, each field required:
  full  — the seven screening fields (every in-scope page, incl. the homepage and
          /contact-us/ since the breeder lifted their opt-out, 2026-09-11 Flag 1)
  short — blog/* posts: confirm number, confirm email, resale, surrender (breeder,
          2026-09-11: "old short forms … only confirm email, numbers, the two questions")
  none  — the location cluster and buy-* slugs (no inquiry forms today).

`n` is 1-based over ALL <form> elements in a page's document order, search forms
included, matching what a browser script will find at `document.forms[n-1]` — it is
not scoped to in-scope or inquiry forms only. A `<form>` opened while another form is
still open is ignored on the start tag (browsers drop nested forms), and content inside
<template>/<noscript> is never scanned. `form=` attribute association (a control outside
its form's tags claimed via the HTML `form=""` attribute) is not modelled.

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
SHORT = ("confirm_number", "confirm_email", "resale_screening", "surrender_history")


def contract_keys(slug: str) -> list:
    """The (name, regex) pairs this page's inquiry forms must carry, each required."""
    if LOCATION.match(slug):
        return []
    if slug.startswith("blog/"):
        return [k for k in KEYS if k[0] in SHORT]
    return KEYS


def field_checks_apply(slug: str) -> bool:
    return bool(contract_keys(slug))


_SKIPPED = ("template", "noscript")


class _Forms(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms, self._cur = [], None
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in _SKIPPED:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        a = dict(attrs)
        if tag == "form":
            if self._cur is not None:
                return  # nested <form> start tag ignored, like a browser's parser
            self._cur = {"attrs": a, "controls": []}
            self.forms.append(self._cur)
        elif tag in ("input", "select", "textarea") and self._cur is not None:
            type_ = a.get("type") or ("text" if tag == "input" else tag)
            self._cur["controls"].append({
                "tag": tag, "name": a.get("name"), "type": type_.lower(),
                "required": "required" in a,
            })

    def handle_endtag(self, tag):
        if tag in _SKIPPED:
            if self._skip_depth:
                self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if tag == "form":
            self._cur = None


def audit_html(html: str, slug: str):
    p = _Forms(); p.feed(html); p.close()
    rows = []
    for n, f in enumerate(p.forms, 1):
        a, ctl = f["attrs"], f["controls"]
        action = a.get("action", "") or ""
        if action.startswith("/search"):
            continue
        # Conservative: a form is "newsletter" only when its real (non-hidden,
        # non-honeypot) controls are exactly one email input. Everything else —
        # including an inquiry form with no <textarea> — is "inquiry".
        real = [c for c in ctl if c["type"] != "hidden" and c["name"] != "_gotcha"]
        kind = "newsletter" if len(real) == 1 and real[0]["type"] == "email" else "inquiry"
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
            for key, rx in contract_keys(slug):
                hits = [c for c in ctl if c["name"] and rx.match(c["name"])]
                if not hits:
                    problems.append(f"{key} absent")
                elif not any(c["required"] for c in hits):
                    problems.append(f"{key} not required")
        rows.append({"slug": slug, "n": n, "name": a.get("name") or (a.get("class") or "").split(" ")[0] or "form",
                     "kind": kind, "action": action, "fields": sorted({c["name"] for c in ctl if c["name"]}),
                     "in_scope": kind == "inquiry" and field_checks_apply(slug), "problems": problems})
    return rows


def audit_dist(dist: Path) -> list:
    rows = []
    for path in sorted(dist.rglob("index.html")):
        rows += audit_html(path.read_text(encoding="utf-8"), page_key(path, dist))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json"); ap.add_argument("--dist", default="dist")
    args = ap.parse_args()
    dist = Path(args.dist)
    rows = audit_dist(dist)
    if not rows:
        print("FAIL: no forms examined — is dist/ built?")
        sys.exit(2)
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

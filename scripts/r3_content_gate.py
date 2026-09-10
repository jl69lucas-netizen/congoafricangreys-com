#!/usr/bin/env python3
"""Round-3 content gate: does every artboard actually carry the live page's content?

Round 2 shipped 9 shipping artboards that all silently dropped the Flight Nanny tier.
This gate exists so that cannot happen again. Prints its own examined count.
"""
import re, pathlib, sys, html

FOLDER = pathlib.Path("docs/design/homepage-variations-r3")

def text_of(p):
    s = p.read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S|re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S|re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s))

# prefix -> list of (label, [acceptable spellings])  — every one must appear
REQUIRED = {
    "Shipping-": [
        ("Airport Pickup tier", ["Airport Pickup"]),
        ("$185",               ["$185"]),
        ("Home Delivery tier", ["Home Delivery"]),
        ("$350",               ["$350"]),
        ("Flight Nanny tier",  ["Flight Nanny"]),
        ("$750",               ["$750"]),
    ],
    "Table-Price-": [
        ("Congo baby price",  ["$2,300"]), ("Congo adult price", ["$1,700"]),
        ("Timneh price",      ["$1,500"]), ("Pair price",        ["$3,500"]),
        ("Breeding pair",     ["$3,000"]), ("Egg price",         ["$95"]),
        ("TOP PICK marker",   ["TOP PICK", "Top Pick", "TOP-PICK"]),
        ("under-$1,500 note", ["wild-caught bird, a sick bird, or no bird at all"]),
    ],
    "Table-Cvt-": [
        ("Psittacus erithacus", ["Psittacus erithacus"]),
        ("Psittacus timneh",    ["Psittacus timneh"]),
        ("Congo price",         ["$1,700"]), ("Timneh price", ["$1,500"]),
        ("Talking onset row",   ["Talking onset", "talking onset"]),
        ("Paperwork row",       ["Paperwork", "paperwork"]),
    ],
    "Table-Mvf-": [
        ("Talking & mimicry", ["Talking & mimicry", "Talking &amp; mimicry", "Talking and mimicry"]),
        ("Temperament",       ["Temperament"]),
        ("Bonding style",     ["Bonding style"]),
        ("monomorphic note",  ["monomorphic"]),
        ("PCR DNA sexing",    ["DNA sexing", "DNA-sexing"]),
    ],
    "Table-Others-": [
        ("African Grey", ["African Grey"]), ("Macaw", ["Macaw"]),
        ("Cockatoo",     ["Cockatoo"]),     ("Amazon", ["Amazon"]),
        ("Noise level",  ["Noise level", "NOISE LEVEL", "Noise"]),
    ],
    "Counter-": [
        ("12+", ["12+"]), ("100%", ["100%"]), ("$1,500", ["$1,500"]), ("24h", ["24h"]),
        ("Years Aviary", ["Years Aviary"]), ("CITES Documented", ["CITES Documented"]),
        ("Floor Price", ["Floor Price"]), ("Reply Guarantee", ["Reply Guarantee"]),
    ],
    "Hero-": [
        ("H1 Midland",   ["Midland, Texas"]),
        ("Congo+Timneh", ["Congo and Timneh African Grey Breeder"]),
        ("clay CTA",     ["View Available Greys"]),
    ],
}

# banned anywhere
BANNED = [
    ("Appendix II (CITES is Appendix I)", re.compile(r"Appendix\s*II", re.I)),
    # Real emoji only. ★ ☆ ✓ ✔ are legitimate verbatim marks in the live CompareTableE
    # and pricing rows; a bare dingbat is only an emoji when a U+FE0F selector forces
    # emoji presentation. Flagging the stars was a harness bug, fixed 2026-09-10.
    ("emoji icon", re.compile("[\U0001F300-\U0001FAFF]|[\u2600-\u27BF]\uFE0F")),
]
BANNED_SRC = [
    ("side-stripe accent border", re.compile(r"border-left\s*:\s*[3-9]px\s+solid", re.I)),
    ("gradient text", re.compile(r"background-clip\s*:\s*text", re.I)),
    ("table-caption on mobile", re.compile(r"display\s*:\s*table-caption", re.I)),
]

files = sorted(FOLDER.glob("*.dc.html"))
files = [f for f in files if f.name != "Main.dc.html"]
examined = 0
findings = []

for p in files:
    txt = text_of(p)
    raw = p.read_text(encoding="utf-8", errors="replace")
    examined += 1
    for prefix, reqs in REQUIRED.items():
        if not p.name.startswith(prefix):
            continue
        for label, spellings in reqs:
            if not any(s in txt for s in spellings):
                findings.append((p.name, f"MISSING {label}"))
    for label, rx in BANNED:
        if rx.search(txt):
            findings.append((p.name, f"BANNED {label}"))
    for label, rx in BANNED_SRC:
        if rx.search(raw) and "-Mobile" in p.name or (rx.search(raw) and label != "table-caption on mobile"):
            findings.append((p.name, f"BANNED {label}"))
    # FAQ: all 21 questions reachable
    if p.name.startswith("Faq-"):
        n = txt.count("?")
        if n < 21:
            findings.append((p.name, f"only {n} question marks; 21 questions required"))

print(f"\nEXAMINED: {examined} artboards")
print(f"--- {len(findings)} CONTENT FINDING(S) ---")
for f, m in findings:
    print(f"  {f}: {m}")
if examined == 0:
    sys.exit("FAIL: examined zero artboards")
print(f"\nexamined={examined} findings={len(findings)}")

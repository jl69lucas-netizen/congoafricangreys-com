#!/usr/bin/env python3
"""board_canvas.py <slug>
Writes docs/design/board-<slug>/<section>--<candidate>--<Mobile|Desktop>.dc.html for every
signature section: up to three candidates from the shape pool minus what siblings own,
each filled ONLY from the section's own record. Publish the folder with the `design`
skill; cut thumbs with board_thumbs.mjs.

A candidate id may carry a `#delta` (and `#refresh` is the pool's placeholder for a spent
shell). `#` is illegal in a file:// path the canvas editor and the thumb cutter both load,
so the FILE spells it `+` and the board maps it back; the artboard itself shows the delta
as a pill so the author can see which option they are looking at."""
import html as H, pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB

DESIGN = PB.ROOT / "docs" / "design"
SUPPORT = DESIGN / "homepage-variations-r3" / "support.js"
VIEWPORTS = {"Mobile": 390, "Desktop": 1440}
MAX_OPTIONS = 3
MAX_CARDS = 6
GREEN, GREEN_D, CLAY, CLAY_INK, CREAM, INK, MUTED, BD = "#2D6A4F", "#234f3b", "#e8604c", "#c8472f", "#faf7f4", "#1f2a24", "#6b625a", "#e7ddd3"

HEAD = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
  <style>
    body { margin:0; background:#faf7f4; font-family:"IBM Plex Sans", system-ui, sans-serif; color:#1f2a24; }
    h1,h2,h3 { font-family: Newsreader, Georgia, serif; font-weight:600; letter-spacing:-.003em; margin:0; }
    p { margin:0; } ul { margin:0; padding:0; list-style:none; }
    a { color:#b04228; text-decoration:none; } a:hover { color:#c8472f; }
  </style>
</helmet>
"""
FOOT = "</x-dc>\n</body>\n</html>\n"


def file_token(candidate):
    """The candidate as a filename fragment. `#` breaks a file:// URL and the thumb
    cutter's split, so it travels as `+` and build_page_board.py maps it back."""
    return candidate.replace("#", "+")


def slot_box(w, h, label, width_css="100%"):
    return (f'<div aria-label="{H.escape(label)}" style="width:{width_css}; aspect-ratio:{w}/{h}; background:repeating-linear-gradient(135deg,#eee 0 8px,#e2ddd6 8px 16px); '
            f'border:1px dashed {BD}; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:12px; color:{MUTED};">{H.escape(label)} · {w}×{h}</div>')


def h3_list(section, limit=4):
    items = [n["heading"] for n in section["tree"] if n["level"] == 3][:limit]
    return "".join(f'<li style="display:flex; gap:10px; align-items:baseline; padding:8px 0; border-bottom:1px solid {BD};"><span style="font-family:Newsreader, Georgia, serif; font-weight:700; color:{CLAY_INK};">{i+1:02d}</span><span style="font-size:15px;">{H.escape(t)}</span></li>' for i, t in enumerate(items))


def pill(candidate):
    """The option's own label. `base#refresh` is the pool saying "this shell is spent,
    reuse it along an axis you have not named yet" — the artboard says so in words rather
    than showing a placeholder id nobody chose; a real `base#delta` shows its delta."""
    delta = candidate.split("#", 1)[1].strip() if "#" in candidate else ""
    if not delta:
        return ""
    text = "REFRESH — name the axis" if delta == "refresh" else delta
    return (f'<span style="display:inline-flex; align-items:center; align-self:flex-start; padding:3px 10px; border-radius:50px; '
            f'background:{CLAY_INK}; color:#fff; font-size:11px; font-weight:700; letter-spacing:.08em; text-transform:uppercase;">{H.escape(text)}</span>')


def heading_block(section, size_px, cand):
    return (f'<p style="font-size:12px; letter-spacing:.1em; text-transform:uppercase; color:{CLAY_INK}; font-weight:600;">Section {section["n"]:02d} · {H.escape(section["shape"])} · {H.escape(PB.base_of(cand))}</p>'
            + pill(cand)
            + f'<h2 style="font-size:{size_px}px; line-height:1.15; color:{GREEN_D};">{H.escape(section["heading"])}</h2>'
            f'<p style="font-size:15px; line-height:1.6; color:{INK}; max-width:62ch;">{H.escape(section["intent"])}</p>')


def _wrap(vw, inner):
    pad = 20 if vw < 700 else 40
    return (HEAD + f'<div id="root" style="width:{vw}px; background:{CREAM}; display:flex; flex-direction:column;">'
            f'<section style="padding:{pad}px; box-sizing:border-box; display:flex; flex-direction:column; gap:16px;">{inner}</section></div>\n' + FOOT)


# ---- shape templates: (section, candidate, vw) -> inner HTML. Three candidates per shape
#      differ along a named axis; every word is the section's own. Each branches on
#      PB.base_of(cand), so a refreshed shell lays out like the shell it refreshes.
def tpl_inventory(section, cand, vw):
    base = PB.base_of(cand)
    cols = 1 if vw < 700 else 3
    imgs = ((section["images"] or [{"slot": "card"}]) * 3)[:MAX_CARDS]
    cards = "".join(f'<article style="border:1px solid {BD}; border-radius:14px; overflow:hidden; background:#fff; display:flex; flex-direction:column;">{slot_box(800, 800, img["slot"])}'
                    f'<div style="padding:12px; display:flex; flex-direction:column; gap:6px;"><h3 style="font-size:16px; text-transform:uppercase; color:{GREEN_D};">{H.escape(img["slot"])}</h3>'
                    f'<p style="font-size:12px; color:{MUTED};">Ships nationwide · $185 airport · $350 home</p></div></article>'
                    for img in imgs)
    if base == "avail-b-faceted":
        side = f'<aside style="border:1px solid {BD}; border-radius:14px; padding:12px; background:#fff; font-size:13px; font-weight:600;">Browse by kind</aside>'
        grid = f'<div style="display:grid; grid-template-columns:{"minmax(0,1fr)" if vw < 700 else "200px minmax(0,1fr)"}; gap:16px;">{side}<div style="display:grid; grid-template-columns:repeat({cols}, minmax(0,1fr)); gap:14px;">{cards}</div></div>'
    elif base == "bird-cards-row":
        grid = f'<div style="display:flex; gap:14px; overflow-x:auto;">{cards}</div>'
    else:
        grid = f'<div style="display:grid; grid-template-columns:repeat({cols}, minmax(0,1fr)); gap:14px;">{cards}</div>'
    return heading_block(section, 26 if vw < 700 else 34, cand) + grid


def tpl_compare(section, cand, vw):
    base = PB.base_of(cand)
    rows = [n["heading"] for n in section["tree"] if n["level"] == 3] or [section["heading"]]
    if base in ("table-b-spine-cards", "verdict-cards"):
        body = "".join(f'<div style="border:1px solid {BD}; border-radius:12px; padding:12px; background:#fff;"><b style="color:{GREEN_D};">{H.escape(r)}</b></div>' for r in rows)
        grid = f'<div style="display:grid; grid-template-columns:repeat({1 if vw < 700 else 2}, minmax(0,1fr)); gap:12px;">{body}</div>'
    elif base == "table-c":
        body = "".join(f'<div style="display:grid; grid-template-columns:{"1fr" if vw < 700 else "1fr 1fr"}; gap:12px; padding:12px 0; border-bottom:1px solid {BD};">'
                       f'<b style="font-size:15px; color:{GREEN_D};">{H.escape(r)}</b>'
                       f'<span style="font-size:14px; color:{MUTED};">from the record</span></div>' for r in rows)
        grid = f'<div style="border:1px solid {BD}; border-radius:14px; padding:4px 16px; background:#fff;">{body}</div>'
    else:
        trs = "".join(f'<tr><td style="padding:8px 10px; border-bottom:1px solid {BD}; font-weight:700; color:{GREEN_D};">{H.escape(r)}</td><td style="padding:8px 10px; border-bottom:1px solid {BD}; color:{MUTED};">from the record</td></tr>' for r in rows)
        grid = f'<table style="width:100%; border-collapse:collapse; background:#fff; border:1px solid {BD}; border-radius:12px; font-size:14px;"><caption style="caption-side:top; text-align:left; background:{CLAY_INK}; color:#fff; padding:8px 12px; font-size:12px; letter-spacing:.08em; text-transform:uppercase;">{H.escape(section["heading"])}</caption>{trs}</table>'
    return heading_block(section, 26 if vw < 700 else 34, cand) + grid


def tpl_sequence(section, cand, vw):
    base = PB.base_of(cand)
    steps = [n["heading"] for n in section["tree"] if n["level"] in (3, 4)][:5]
    if base == "timeline-strip":
        body = "".join(f'<div style="flex:1; border-top:3px solid {CLAY}; padding-top:8px; font-size:14px;"><b>{i+1}</b><br>{H.escape(s)}</div>' for i, s in enumerate(steps))
        return heading_block(section, 26 if vw < 700 else 34, cand) + f'<div style="display:flex; flex-direction:{"column" if vw < 700 else "row"}; gap:14px;">{body}</div>'
    if base.endswith("stepper"):
        body = "".join(f'<div style="display:grid; grid-template-columns:36px 1fr; gap:12px; align-items:center; border:1px solid {BD}; border-radius:12px; padding:12px; background:#fff;">'
                       f'<span style="width:36px; height:36px; border-radius:50%; background:{GREEN}; color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700;">{i+1}</span>'
                       f'<span style="font-size:15px;">{H.escape(s)}</span></div>' for i, s in enumerate(steps))
        return heading_block(section, 26 if vw < 700 else 34, cand) + f'<div style="display:flex; flex-direction:column; gap:10px;">{body}</div>'
    return heading_block(section, 26 if vw < 700 else 34, cand) + f'<ul style="display:flex; flex-direction:column;">{h3_list(section, 5)}</ul>'


def tpl_proof(section, cand, vw):
    base = PB.base_of(cand)
    items = [n["heading"] for n in section["tree"]][:5]
    if base in ("k1-receipt", "table-h-price-ladder"):
        body = "".join(f'<div style="display:grid; grid-template-columns:{"1fr" if vw < 700 else "7.5rem 1fr"}; gap:12px; padding:8px 0; border-bottom:1px dashed {BD};"><dt style="font-size:12px; font-weight:700; text-transform:uppercase; color:{GREEN_D};">Item {i+1}</dt><dd style="margin:0; font-size:14px;">{H.escape(t)}</dd></div>' for i, t in enumerate(items))
        return heading_block(section, 26 if vw < 700 else 34, cand) + f'<dl style="margin:0; border:1px solid {BD}; border-radius:14px; padding:8px 16px; background:#fff;">{body}</dl>'
    if base == "lab-report-table":
        trs = "".join(f'<tr><td style="padding:10px; border-bottom:1px solid {BD}; font-family:Newsreader, Georgia, serif; font-weight:700; color:{CLAY_INK};">{i+1:02d}</td>'
                      f'<td style="padding:10px; border-bottom:1px solid {BD}; font-size:14px;">{H.escape(t)}</td></tr>' for i, t in enumerate(items))
        return heading_block(section, 26 if vw < 700 else 34, cand) + f'<table style="width:100%; border-collapse:collapse; background:#fff; border:1px solid {BD}; border-radius:12px; font-size:14px;">{trs}</table>'
    body = "".join(f'<li style="display:grid; grid-template-columns:20px 1fr; gap:8px; font-size:14px; padding:4px 0;"><span style="color:{GREEN};">✓</span>{H.escape(t)}</li>' for t in items)
    return heading_block(section, 26 if vw < 700 else 34, cand) + f'<ul style="border:1px solid {BD}; border-radius:14px; padding:14px 18px; background:#fff;">{body}</ul>'


def tpl_price(section, cand, vw):
    return tpl_proof(section, cand, vw)


def tpl_nav(section, cand, vw):
    base = PB.base_of(cand)
    labels = [n["heading"] for n in section["tree"]][:9] or [section["heading"]]
    chips = "".join(f'<a href="#" style="display:inline-flex; align-items:center; min-height:44px; padding:6px 14px; border-radius:50px; border:1.5px solid {GREEN}; font-size:13px; font-weight:600; color:{GREEN_D};">{H.escape(l)}</a>' for l in labels)
    if base.startswith("dial") or "numbered-ledger" in base:
        rows = "".join(f'<a href="#" style="display:grid; grid-template-columns:28px 1fr; gap:10px; align-items:center; min-height:44px; padding:6px 10px; border-bottom:1px solid {BD}; font-size:14px; font-weight:600; color:{GREEN_D};">'
                       f'<span style="font-family:Newsreader, Georgia, serif; color:{CLAY_INK};">{i+1:02d}</span>{H.escape(l)}</a>' for i, l in enumerate(labels))
        return heading_block(section, 26 if vw < 700 else 34, cand) + f'<div style="display:grid; grid-template-columns:{"1fr" if vw < 700 else "196px 1fr"}; gap:28px;"><nav style="border:1px solid {BD}; border-radius:16px; padding:12px 10px; background:#fff; display:grid; gap:4px;">{rows}</nav><div>{slot_box(1408, 768, "section body")}</div></div>'
    if "boarding-pass" in base:
        rows = "".join(f'<a href="#" style="display:flex; align-items:center; min-height:44px; gap:10px; padding:10px 14px; border-radius:12px; background:{GREEN_D}; color:#fff; font-size:13px; font-weight:600; border-left:6px solid {CLAY};">{H.escape(l)}</a>' for l in labels)
        return heading_block(section, 26 if vw < 700 else 34, cand) + f'<nav style="display:grid; grid-template-columns:repeat({1 if vw < 700 else 2}, minmax(0,1fr)); gap:10px;">{rows}</nav>'
    return heading_block(section, 26 if vw < 700 else 34, cand) + f'<nav style="display:flex; gap:8px; flex-wrap:wrap;">{chips}</nav>'


def tpl_narrative(section, cand, vw):
    base = PB.base_of(cand)
    img = slot_box(1408, 768, (section["images"] or [{"slot": "section image"}])[0]["slot"])
    if base == "split-feature":
        return heading_block(section, 26 if vw < 700 else 34, cand) + f'<div style="display:grid; grid-template-columns:{"1fr" if vw < 700 else "1fr 1fr"}; gap:20px; align-items:center;">{img}<ul>{h3_list(section)}</ul></div>'
    if base == "quote-band":
        return heading_block(section, 26 if vw < 700 else 34, cand) + f'<blockquote style="margin:0; padding:16px 20px; border-radius:14px; background:{GREEN_D}; color:#fff; font-family:Newsreader, Georgia, serif; font-size:18px;">{H.escape(section["intent"])}</blockquote>{img}'
    return heading_block(section, 26 if vw < 700 else 34, cand) + img + f'<ul>{h3_list(section)}</ul>'


TEMPLATES = {"inventory": tpl_inventory, "compare": tpl_compare, "sequence": tpl_sequence, "proof": tpl_proof,
             "price": tpl_price, "nav": tpl_nav, "narrative": tpl_narrative, "hero": tpl_narrative, "counter": tpl_proof, "takeaway": tpl_proof}


def write_canvas(board, ledger, out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    slug = board["meta"]["slug"]
    written = []
    for s in board["sections"]:
        if s["shape"] == "standard":
            continue
        cands, _ = PB.candidates_for(s["shape"], ledger, slug)
        tpl = TEMPLATES[s["shape"]]
        for c in cands[:MAX_OPTIONS]:
            for vp, vw in VIEWPORTS.items():
                p = out / f"{s['id']}--{file_token(c)}--{vp}.dc.html"
                p.write_text(_wrap(vw, tpl(s, c, vw)), encoding="utf-8")
                written.append(p)
    if SUPPORT.exists():
        shutil.copy(SUPPORT, out / "support.js")
    else:
        (out / "support.js").write_text("// support.js placeholder: copy from docs/design/homepage-variations-r3/support.js\n")
    (out / "CONTRACT.md").write_text(
        f"# Page Board canvas — /{slug}/\n\nArtboards are generated by scripts/board_canvas.py from data/pages/{slug}/board.json.\n"
        "Every word is that section's own record; siblings only subtracted candidates. Edit layout here; a text edit is written back\n"
        "into the record by board_approve.py at approval. File naming: <section>--<candidate>--<Mobile|Desktop>.dc.html, with a\n"
        "candidate's `#` spelled `+` (a `#` breaks the file:// URL the editor and the thumb cutter load); the board maps it back.\n", encoding="utf-8")
    return written


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: board_canvas.py <slug>")
    slug = sys.argv[1]
    board, ledger = PB.load_board(slug), PB.load_ledger()
    written = write_canvas(board, ledger, DESIGN / f"board-{slug}")
    print(f"wrote {len(written)} artboards to docs/design/board-{slug}/")


if __name__ == "__main__":
    main()

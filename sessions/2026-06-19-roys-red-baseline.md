# Roys Bird-Page Rebuild — RED Baseline (2026-06-19)

This is the **RED** step of a RED→GREEN build for `/available/roys/`. It records the
current (pre-expansion) state of the lean Roys bird page so the GREEN state can be
proven later. **No page edits were made in this task** — build, measure, record only.

- Branch: `main`
- Source page: `src/pages/available/roys/index.astro`
- Built artifact measured: `dist/available/roys/index.html`
- Build: `npx astro build` → exit 0 (success)
- Audit: `python3 scripts/final_page_audit.py --birds` (output also at `/tmp/roys-red.txt`)

## Current measured state (RED)

| Metric | Value | Target (GREEN) | Status |
|---|---|---|---|
| Visible/rendered word count | **1,446** | 2,974 | Well under target — must grow ~1,528 words |
| FAQ items (`<summary` count) | **4** | 5+ | Needs a 5th+ FAQ |
| Audit verdict for `available/roys` | **PASS-WITH-WARNINGS** | (clear `wordcount_in_band`) | — |

### Audit verdict line (verbatim)

```
[PASS-WITH-WARNINGS] available/roys   H1:1 H2:8 H3:12 H4:0 H5:0 H6:0 | FAQPage×1 | schema:Answer,Brand,BreadcrumbList,FAQPage,GeoCoordinates,ImageObject,ListItem,Offer,OpeningHoursSpecification,Organization,PetStore,PostalAddress,Product,Question
    WARN → all_h1_h4, wordcount_in_band, house_method
```

Batch summary: `0 PASS · 6 PASS-WITH-WARNINGS · 0 FAIL (of 6)`. All six `/available/`
pages (bery, amie, roys, jins-jeni, elad, evie) share the same three warnings
(`all_h1_h4`, `wordcount_in_band`, `house_method`).

## Deltas the GREEN build must ADD — confirmed ABSENT / minimal in RED

String presence checked via grep over `dist/available/roys/index.html`:

| Delta the build must add | Probe string(s) | Count in RED | Expected RED |
|---|---|---|---|
| AEO **Bird Snapshot** box | `Snapshot` | **0** | ABSENT ✓ |
| Counter-positioning ($2,300 vs $850) — the **$850** half | `$850` | **0** | ABSENT ✓ |
| Expanded **Shipping & Logistics** section (Flight Nanny tier) | `Flight Nanny` / `flight nanny` | **0** | ABSENT ✓ |
| **Newsletter** placement | `newsletter` | **0** | ABSENT ✓ |
| Newsletter placement (alt probe) | `subscribe` | **0** | ABSENT ✓ |
| 5th+ FAQ | `<summary` | **4** | Only 4 (one short) ✓ |

### Already-present anchors (context, not deltas)

- `$2,300` — present (11×): the bird's own price/the high side of the counter-positioning
  pair is already on the page; the **$850 contrast figure is what's missing**.
- `Shipping` — present (3×): a basic/minimal shipping mention exists, but the **expanded
  Shipping & Logistics** section (incl. "Flight Nanny" tier / `Logistics` framing = 0) is absent.

## Reproduce

```bash
npx astro build
python3 scripts/final_page_audit.py --birds 2>&1 | tee /tmp/roys-red.txt

# rendered word count
python3 - <<'PY'
import re,html
t=open('dist/available/roys/index.html').read()
t=re.sub(r'<script[^>]*>.*?</script>','',t,flags=re.S)
t=re.sub(r'<style[^>]*>.*?</style>','',t,flags=re.S)
t=html.unescape(re.sub(r'<[^>]+>',' ',t))
print('words:',len(t.split()))
PY

# FAQ count + delta strings
grep -o '<summary' dist/available/roys/index.html | wc -l
grep -o -i "Snapshot\|\$850\|Flight Nanny\|newsletter\|subscribe" dist/available/roys/index.html | wc -l
```

## Verdict

RED baseline captured. The GREEN build must grow Roys from **1,446 → ~2,974 words**,
add the **Bird Snapshot** AEO box, a **$2,300-vs-$850 counter-positioning** section,
an **expanded Shipping & Logistics** section, a **newsletter** placement, and a **5th+
FAQ** (currently 4) — clearing the `wordcount_in_band` warning while keeping the bird
gates (single Product/Offer, no PBFD, sold≠InStock, shipping line) intact.

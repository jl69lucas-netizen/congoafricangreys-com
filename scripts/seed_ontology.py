#!/usr/bin/env python3
"""seed_ontology.py — build data/cag-ontology.json from the entity catalog
(skills/cag-entity-agent.md) plus the Verified-Claim Ledger. Run once; later growth
comes from board approvals (board_approve.py). Re-running is idempotent: existing ids
keep their authorization and owner_page."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB

CATALOG = PB.ROOT / "skills" / "cag-entity-agent.md"
CLASS_BY_CATEGORY = {"breed": "Organism", "health": "Health", "credential": "Documentation",
                     "location": "Place", "pricing": "Commerce", "buyer": "People", "family": "People"}


def slug(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return "ont:" + s


def catalog_entities():
    """Rows of the catalog tables only. The catalog is the section under
    `## Complete Entity Catalog` and it ends at the next H2 — tables further down the
    skill (the page-type density table, for one) describe pages, not entities."""
    out, cls, inside = [], "Documentation", False
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if inside:
                break
            inside = line.strip() == "## Complete Entity Catalog"
            continue
        if not inside:
            continue
        h = re.match(r"^### Category \d+ — (.+)$", line)
        if h:
            key = h.group(1).lower()
            cls = next((v for k, v in CLASS_BY_CATEGORY.items() if k in key), "Documentation")
            continue
        m = re.match(r"^\| ([^|]+) \| ([^|]*) \| ([^|]*) \|$", line)
        if not m or m.group(1).strip() in ("Primary Entity", "---------------") or m.group(1).startswith("-"):
            continue
        name = m.group(1).strip()
        # MFS placeholders, and price rows — the LEDGER carries the real ranges with sources
        if name.startswith("[") or name.startswith("$"):
            continue
        aliases = [a.strip() for a in m.group(2).split(",") if a.strip()]
        out.append({"id": slug(name), "name": name, "aliases": aliases, "class": cls,
                    "authorization": "PROPOSED", "source": None, "owner_page": None})
    return out


# Verified-Claim Ledger: .claude/agents/cag-entity-incorporation-agent.md + docs/reference/credentials.md
LEDGER = [
    ("ont:cites-appendix-i", "CITES Appendix I", ["Appendix I", "CITES A-I"], "Documentation", "credentials.md#cites-compliance"),
    ("ont:captive-bred", "Captive-bred", ["bred in captivity", "domestically bred"], "Documentation", "credentials.md#cites-compliance"),
    ("ont:usda-awa-licence", "USDA AWA licence", ["USDA licensed", "Animal Welfare Act licence"], "Documentation", "credentials.md#usda-awa-license"),
    ("ont:pcr-dna-sexing", "PCR DNA sexing", ["DNA-sexed", "sexing certificate"], "Health", "ledger#pcr-dna-sexing"),
    ("ont:pbfd-screening", "PBFD PCR screening", ["Psittacine Beak and Feather Disease", "PBFD"], "Health", "ledger#pbfd-apv-2026-06-20"),
    ("ont:avian-polyomavirus-screening", "Avian polyomavirus PCR screening", ["APV", "polyomavirus"], "Health", "ledger#pbfd-apv-2026-06-20"),
    ("ont:psittacosis-screening", "Psittacosis screening", ["Chlamydia psittaci", "chlamydiosis"], "Health", "ledger#psittacosis-2026-06-05"),
    ("ont:avian-vet-health-certificate", "Avian veterinary health certificate", ["vet certificate", "health certificate"], "Health", "credentials.md#avian-vet-health-certificate"),
    ("ont:hatch-certificate-closed-band", "Hatch certificate and closed leg band", ["closed band", "band number", "leg band"], "Documentation", "credentials.md#hatch-certificate-band"),
    ("ont:72-hour-guarantee", "72-hour written health guarantee", ["3-day health guarantee", "72-hour guarantee"], "Commerce", "ledger#3-day-guarantee"),
    ("ont:airport-cargo-185", "$185 airport cargo pickup", ["airport pickup", "$185"], "Logistics", "data/price-matrix.json#airport_pickup_display"),
    ("ont:home-delivery-350", "$350 home delivery", ["home delivery", "$350"], "Logistics", "data/price-matrix.json#home_delivery_display"),
    ("ont:flight-nanny", "Cabin flight nanny (quoted per route)", ["flight nanny", "cabin seat"], "Logistics", "data/financial-entities.json#flight_nanny"),
    ("ont:iata-live-animals-regulations", "IATA Live Animals Regulations", ["IATA LAR"], "Logistics", "ledger#shipping"),
    ("ont:delta-cargo", "Delta Cargo", [], "Logistics", "ledger#shipping"),
    ("ont:united-cargo", "United Cargo", [], "Logistics", "ledger#shipping"),
    ("ont:american-airlines-cargo", "American Airlines Cargo", [], "Logistics", "ledger#shipping"),
    ("ont:midland-pickup-radius", "Midland pickup within a 2–3 hour drive", ["collect in person"], "Logistics", "skills/cag-for-sale-page-builder.md#3.5"),
    ("ont:deposit-200", "$200 deposit", ["deposit"], "Commerce", "data/price-matrix.json#deposit_display"),
    ("ont:congo-price-range", "Congo $1,700–$3,500", [], "Commerce", "data/price-matrix.json#congo_african_grey"),
    ("ont:timneh-price-range", "Timneh $1,500–$1,600", [], "Commerce", "data/price-matrix.json#timneh_african_grey"),
    ("ont:aviary-floor-1500", "$1,500 aviary floor price", [], "Commerce", "data/price-matrix.json#timneh_african_grey"),
    ("ont:psittacus-erithacus", "Psittacus erithacus", ["Congo African Grey", "Congo"], "Organism", "ledger#taxonomy"),
    ("ont:psittacus-timneh", "Psittacus timneh", ["Timneh African Grey", "Timneh"], "Organism", "ledger#taxonomy"),
    ("ont:lifespan-40-60", "40–60 year lifespan", [], "Organism", "IUCN 22724813"),
    ("ont:wean-12-16-weeks", "Fully weaned at 12–16 weeks", ["weaned"], "Method", "credentials.md#hand-raised"),
    ("ont:benjamin-home-raising-protocol", "The Benjamin Home-Raising Protocol", [], "Method", "skills/cag-aeo-pass.md#6a"),
    ("ont:midland-socialization-method", "The Midland Socialization Method", [], "Method", "skills/cag-aeo-pass.md#6a"),
    ("ont:uvb-d3", "UV-B lighting and vitamin D3", [], "Health", "ledger#uvb-d3-2026-06-05"),
    ("ont:mark-teri-benjamin", "Mark & Teri Benjamin", ["Mark and Teri Benjamin"], "People", "credentials.md#owners"),
    ("ont:cags-midland-tx", "C.A.Gs – Midland, TX", ["C.A.Gs", "CongoAfricanGreys.com"], "Place", "credentials.md#nap"),
    ("ont:founded-2014", "Founded 2014", ["since 2014"], "People", "credentials.md#founded"),
    ("ont:aav-find-a-vet", "Association of Avian Veterinarians find-a-vet", ["AAV"], "Health", "docs/reference/external-link-library.md"),
    ("ont:aphis-public-search", "APHIS Animal Care public search", [], "Documentation", "credentials.md#usda-awa-license"),
]
BLOCKED = [
    ("ont:wild-caught", "wild-caught"), ("ont:imported-from", "imported from"),
    ("ont:smuggled", "smuggled"), ("ont:undocumented-sale", "undocumented sale"),
]


def main():
    existing = {}
    if PB.ONTOLOGY.exists():
        existing = {e["id"]: e for e in json.loads(PB.ONTOLOGY.read_text(encoding="utf-8"))["entities"]}
    merged = {}
    for e in catalog_entities():
        merged[e["id"]] = e
    for eid, name, aliases, cls, src in LEDGER:
        merged[eid] = {"id": eid, "name": name, "aliases": aliases, "class": cls,
                       "authorization": "ASSERTED", "source": src, "owner_page": None}
    for eid, name in BLOCKED:
        merged[eid] = {"id": eid, "name": name, "aliases": [], "class": "Commerce",
                       "authorization": "BLOCKED", "source": "CLAUDE.md rule 2", "owner_page": None}
    for eid, old in existing.items():                       # idempotent: keep earlier decisions
        if eid in merged:
            if old["authorization"] != "PROPOSED":
                merged[eid]["authorization"] = old["authorization"]
                merged[eid]["source"] = old["source"] or merged[eid]["source"]
            merged[eid]["owner_page"] = old.get("owner_page")
        else:                                               # an entity the catalog never carried —
            merged.setdefault(eid, old)                     # a board added it (spec 3.2); keep it,
                                                            # PROPOSED included, until it is sourced
    ont = {"entities": sorted(merged.values(), key=lambda e: e["id"])}
    PB.validate_ontology(ont)
    PB.ONTOLOGY.write_text(json.dumps(ont, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    try:                                                    # a test may point ONTOLOGY outside ROOT
        where = PB.ONTOLOGY.relative_to(PB.ROOT)
    except ValueError:
        where = PB.ONTOLOGY
    print(f"wrote {where} — {len(ont['entities'])} entities "
          f"({sum(e['authorization']=='ASSERTED' for e in ont['entities'])} asserted, "
          f"{sum(e['authorization']=='BLOCKED' for e in ont['entities'])} blocked)")


if __name__ == "__main__":
    main()

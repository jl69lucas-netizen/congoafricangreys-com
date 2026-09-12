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
# The category heading is too coarse for a handful of rows; these are the corrections.
CLASS_OVERRIDES = {"ont:nationwide-shipping": "Logistics", "ont:hand-raised": "Method",
                   "ont:behavioral-socialization": "Method", "ont:nutritional-support": "Health",
                   "ont:avian-welfare-standards": "Documentation", "ont:transparent-pricing": "Commerce",
                   "ont:long-lived-companion": "Organism"}
# Catalog rows the Verified-Claim Ledger already carries under a better name and a source.
CATALOG_TWINS = {"dna sexing", "usda license", "cites documentation", "iata-compliant shipping",
                 "lifetime advisory"}
MIN_CATALOG_ROWS = 25          # the catalog holds 29 rows; a renamed H2 or a reformatted
                               # table drops that to ~0, and this is what catches it.


def slug(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return "ont:" + s


def _ledger_surface_forms():
    """Every name and alias the ledger already owns, lowercased."""
    forms = set()
    for _eid, name, aliases, _cls, _src in LEDGER:
        forms.add(name.lower())
        forms.update(a.lower() for a in aliases)
    return forms


def catalog_entities():
    """Rows of the catalog tables only. The catalog is the section under
    `## Complete Entity Catalog` and it ends at the next H2 — tables further down the
    skill (the page-type density table, for one) describe pages, not entities."""
    twins = _ledger_surface_forms() | CATALOG_TWINS
    out, cls, inside, rows = [], "Documentation", False, 0
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
        if not m or m.group(1).strip() == "Primary Entity" or m.group(1).startswith("-"):
            continue
        rows += 1
        name = m.group(1).strip()
        # MFS placeholders; price rows (the LEDGER carries the ranges with a source); and
        # rows the ledger already owns under a sourced name.
        if name.startswith("[") or name.startswith("$") or name.lower() in twins:
            continue
        eid = slug(name)
        aliases = [a.strip() for a in m.group(2).split(",") if a.strip()]
        out.append({"id": eid, "name": name, "aliases": aliases,
                    "class": CLASS_OVERRIDES.get(eid, cls),
                    "authorization": "PROPOSED", "source": None, "owner_page": None})
    if rows < MIN_CATALOG_ROWS:
        raise PB.BoardError(f"{CATALOG}: parsed {rows} catalog rows, expected at least "
                            f"{MIN_CATALOG_ROWS} — the catalog heading or its tables changed shape")
    return out


# Verified-Claim Ledger: .claude/agents/cag-entity-incorporation-agent.md + docs/reference/credentials.md
LEDGER = [
    ("ont:cites-appendix-i", "CITES Appendix I", ["Appendix I", "CITES A-I"], "Documentation", "docs/reference/credentials.md#cites-quick-reference-for-all-agents"),
    ("ont:captive-bred", "Captive-bred", ["bred in captivity", "domestically bred"], "Documentation", "docs/reference/credentials.md#cites-quick-reference-for-all-agents"),
    ("ont:usda-awa-licence", "USDA AWA licence", ["USDA licensed", "Animal Welfare Act licence"], "Documentation", "docs/reference/credentials.md#breeder-credentials"),
    ("ont:pcr-dna-sexing", "PCR DNA sexing", ["DNA-sexed", "sexing certificate"], "Health", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:pbfd-screening", "PBFD PCR screening", ["Psittacine Beak and Feather Disease", "PBFD"], "Health", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:avian-polyomavirus-screening", "Avian polyomavirus PCR screening", ["APV", "polyomavirus"], "Health", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:psittacosis-screening", "Psittacosis screening", ["Chlamydia psittaci", "chlamydiosis"], "Health", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:avian-vet-health-certificate", "Avian veterinary health certificate", ["vet certificate", "health certificate"], "Health", "docs/reference/credentials.md#medical-screenings"),
    ("ont:hatch-certificate-closed-band", "Hatch certificate and closed leg band", ["closed band", "band number", "leg band"], "Documentation", "docs/reference/credentials.md#breeder-credentials"),
    ("ont:72-hour-guarantee", "72-hour written health guarantee", ["3-day health guarantee", "72-hour guarantee"], "Commerce", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:airport-cargo-185", "$185 airport cargo pickup", ["airport pickup", "$185"], "Logistics", "data/price-matrix.json#airport_pickup_display"),
    ("ont:home-delivery-350", "$350 home delivery", ["home delivery", "$350"], "Logistics", "data/price-matrix.json#home_delivery_display"),
    ("ont:flight-nanny", "Cabin flight nanny (quoted per route)", ["flight nanny", "cabin seat"], "Logistics", "data/price-matrix.json#cabin_nanny_display"),
    ("ont:iata-live-animals-regulations", "IATA Live Animals Regulations", ["IATA LAR"], "Logistics", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:delta-cargo", "Delta Cargo", [], "Logistics", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:united-cargo", "United Cargo", [], "Logistics", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:american-airlines-cargo", "American Airlines Cargo", [], "Logistics", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:midland-pickup-radius", "Midland pickup within a 2–3 hour drive", ["collect in person"], "Logistics", "docs/reference/credentials.md#shipping"),
    ("ont:deposit-200", "$200 deposit", ["deposit"], "Commerce", "data/price-matrix.json#deposit_display"),
    ("ont:congo-price-range", "Congo $1,700–$3,500", [], "Commerce", "data/price-matrix.json#congo_african_grey"),
    ("ont:timneh-price-range", "Timneh $1,500–$1,600", [], "Commerce", "data/price-matrix.json#timneh_african_grey"),
    ("ont:aviary-floor-1500", "$1,500 aviary floor price (whole-aviary range $1,500–$3,500)",
     ["$1,500–$3,500 across the aviary"], "Commerce", "data/price-matrix.json#timneh_african_grey"),
    ("ont:psittacus-erithacus", "Psittacus erithacus", ["Congo African Grey", "Congo"], "Organism", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:psittacus-timneh", "Psittacus timneh", ["Timneh African Grey", "Timneh"], "Organism", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:lifespan-40-60", "40–60 year lifespan", [], "Organism", "IUCN 22724813"),
    ("ont:wean-12-16-weeks", "Fully weaned at 12–16 weeks", ["weaned"], "Method", "docs/reference/credentials.md#breeder-credentials"),
    ("ont:benjamin-home-raising-protocol", "The Benjamin Home-Raising Protocol", [], "Method", "skills/cag-aeo-pass.md#6a-label-the-method-so-the-expertise-stays-ours"),
    ("ont:midland-socialization-method", "The Midland Socialization Method", [], "Method", "skills/cag-aeo-pass.md#6a-label-the-method-so-the-expertise-stays-ours"),
    ("ont:uvb-d3", "UV-B lighting and vitamin D3", [], "Health", ".claude/agents/cag-entity-incorporation-agent.md#verified-claim-ledger-what-entities-you-may-assert"),
    ("ont:mark-teri-benjamin", "Mark & Teri Benjamin", ["Mark and Teri Benjamin"], "People", "docs/reference/credentials.md#breeder-credentials"),
    ("ont:cags-midland-tx", "C.A.Gs – Midland, TX", ["C.A.Gs", "CongoAfricanGreys.com"], "Place", "docs/reference/credentials.md#brand--nap"),
    ("ont:founded-2014", "Founded 2014", ["since 2014"], "People", "docs/reference/credentials.md#breeder-credentials"),
    ("ont:aav-find-a-vet", "Association of Avian Veterinarians find-a-vet", ["AAV"], "Health", "docs/reference/external-link-library.md"),
    ("ont:aphis-public-search", "APHIS Animal Care public search", [], "Documentation", "docs/reference/credentials.md#breeder-credentials"),
]
BLOCKED = [
    ("ont:wild-caught", "wild-caught"), ("ont:imported-from", "imported from"),
    ("ont:smuggled", "smuggled"), ("ont:undocumented-sale", "undocumented sale"),
]


def main():
    existing = {}
    if PB.ONTOLOGY.exists():
        existing = {e["id"]: e for e in PB._read_json(PB.ONTOLOGY)["entities"]}
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
                merged[eid]["source"] = old.get("source") or merged[eid]["source"]
            merged[eid]["owner_page"] = old.get("owner_page")
        else:                                               # an entity the catalog never carried —
            merged[eid] = old                               # a board added it (spec 3.2); keep it,
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

# C.A.Gs — Master NAP & Credentials Record

**Source of truth for all brand, contact, legal, and trust data.**
Agents must read this file before writing any page that references credentials, certifications, pricing, or shipping.
NAP Citation Agent compares every directory listing against this file.

---

## Brand / NAP

| Field | Value |
|---|---|
| **Display Name** | C.A.Gs – Midland, TX |
| **Legal / Alternate Name** | Congo African Greys For Sale |
| **Website** | congoafricangreys.com |
| **Phone** | +1-402-696-0317 |
| **Email** | Info@congoafricangreys.com |
| **Street Address** | 2508 Briaroaks Ct |
| **City / State / ZIP** | Midland, TX 79707 |
| **Country** | United States |
| **Geo** | 32.00275937134384, -102.17760079202473 |
| **Facebook** | https://www.facebook.com/people/Congo-African-grey/61571657313840/ |

NAP must match exactly across every directory submission, schema block, and contact page.
Never use "congoafricangreys.com" as a display/brand name — use "C.A.Gs – Midland, TX".

---

## Breeder Credentials

| Credential | Detail |
|---|---|
| **USDA AWA License** | Active — USDA Animal Welfare Act licensed aviary. Verifiable at aphis.usda.gov/awa/public-search. |
| **CITES Compliance** | CITES **Appendix I** compliant. All birds captive-bred with full captive-bred documentation issued per bird. Never wild-caught. "Appendix II" must never appear in reference to our birds. |
| **DNA Sexing** | DNA sexed — not visual. Certificate issued per bird. |
| **Avian Vet Health Certificate** | Issued per bird by a licensed avian veterinarian before placement. |
| **Hatch Certificate + Band** | Each bird has a hatch certificate and leg-band number on record. |
| **Hand-Raised / Fully Weaned** | All birds hand-raised from hatch and fully weaned before placement (12–16 weeks). |
| **Founded** | 2014 |
| **Owners** | Mark Benjamin & Teri Benjamin, family-owned aviary in Midland, TX. Family includes James and Allyson. |
| **Years Operating** | 12+ years (as of 2026) |

---

## Shipping

| Field | Value |
|---|---|
| **Method** | IATA-compliant airline transport — domestic USA only |
| **Coverage** | Ships nationally to all 50 US states |
| **Response Time** | Inquiry response within 24 hours |
| **Key States / Cities** | FL, CA, TX, NY, GA, CO, IL, AZ, OH, WA, PA, NC, NJ, MA (priority shipping markets) |
| **Deposit** | $200 to hold a bird |

---

## Medical Screenings

| Test | Status |
|---|---|
| **PBFD (Psittacine Beak and Feather Disease)** | Tested — negative required before placement |
| **Avian Polyomavirus** | Tested — negative required before placement |
| **DNA Sexing** | Confirmed per bird — certificate provided |

---

## Brands / Partners

| Brand | Role |
|---|---|
| **Harrison's Bird Foods** | Primary pelleted diet recommended and used in aviary |
| **ZuPreem** | Secondary pelleted diet used for weaning birds |
| **AFA (American Federation of Aviculture)** | Member / affiliated organization |

---

## Statistics (Verified Only — No Fabrication)

| Statistic | Value | Notes |
|---|---|---|
| **Birds Placed** | 2,000+ | Approximate lifetime total |
| **Disease Claim Rate** | 0% | No documented PBFD/Polyomavirus claims |
| **Aviary History** | 12+ years | Since 2014 |
| **CITES Compliance** | 100% | Every bird documented |
| **Price Floor — Congo** | $1,500 | Baby Congo starts at $1,500; adult $1,700–$2,500 |
| **Price Ceiling — Congo** | $3,500 | Pair pricing up to $3,500 |
| **Price Floor — Timneh** | $1,200 | Timneh range $1,200–$2,500 per CLAUDE.md |
| **Price Ceiling — Timneh** | $2,500 | |
| **Fertile Eggs** | $95 each | 5 eggs = free US shipping |
| **Breeding Pairs** | $3,000+ | Jins+Jeni pair listed at $3,500 |
| **Deposit** | $200 | Refundable hold |

---

## CITES Quick-Reference (for all agents)

- Species: *Psittacus erithacus* (Congo African Grey) and *Psittacus timneh* (Timneh African Grey)
- CITES status: **Appendix I** — uplisted from Appendix II at CoP17, effective January 2017
- IUCN status: Congo = Endangered; Timneh = Vulnerable
- Legal to own and transfer domestically in the USA as captive-bred birds with proper paperwork
- Permissible historical reference: "uplisted from Appendix II to Appendix I at CoP17, effective Jan 2017"
- Never write "Appendix II" as the current status of our birds or African Greys in general

---

## Schema Anchor

The canonical Organization schema `"name"` field is **"C.A.Gs – Midland, TX"**.
`"legalName"` / `"alternateName"` = "Congo African Greys For Sale" or "Congo African Greys".

All JSON-LD blocks site-wide must use this pattern:
```json
{
  "@type": ["Organization", "LocalBusiness", "PetStore"],
  "name": "C.A.Gs – Midland, TX",
  "alternateName": "Congo African Greys",
  "legalName": "Congo African Greys For Sale"
}
```

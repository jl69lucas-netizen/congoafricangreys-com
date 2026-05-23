# CongoAfricanGreys.com — Master NAP Record

> Source of truth for Name/Address/Phone across all directory listings.
> Used by: cag-nap-citation-agent
> **Fill in all (confirm with breeder) fields before running cag-nap-citation-agent or cag-directory-submission-agent.**

## Business Identity

| Field | Value |
|-------|-------|
| Business Name | Congo African Greys |
| Owner | Mark & Teri Benjamin |
| City | Midland |
| State | TX |
| Zip | (confirm with breeder) |
| Phone | (confirm with breeder) |
| Email | (confirm with breeder) |
| Website | https://congoafricangreys.com |
| USDA AWA License | Yes — license number: (confirm with breeder) |
| CITES Compliant | Yes — all birds captive-bred with full documentation |
| Founded | 2014 |

## Social Profiles

| Platform | URL |
|----------|-----|
| Facebook | (confirm with breeder) |
| YouTube | (confirm with breeder) |
| Instagram | (confirm with breeder) |

## NAP Consistency Rules

- Business name must always be **"Congo African Greys"** — never "CongoAfricanGreys.com" in directory listings
- Phone must use same format across all directories (e.g., always `(XXX) XXX-XXXX` or always `XXX-XXX-XXXX`)
- City must always be **"Midland"** — never "Midland, TX" unless the directory requires state in the city field
- Never publish partial NAP — if any field is unconfirmed, do not submit to that directory

## How This File Is Used

`cag-nap-citation-agent` reads this file as the master record and compares it against all directory listings in `data/directories.json`. Any mismatch triggers a WARN or FAIL flag.

Run `cag-nap-citation-agent` quarterly to verify NAP consistency.

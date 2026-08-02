# The transactional for-sale and buy cluster

Rules moved out of `CLAUDE.md` on 2026-08-02 (Phase 4). **The rule text is verbatim.**

`enforced:` says what actually holds the rule up.
`test` — a committed check fails when the rule is broken. `judgment` — no mechanical
decision procedure exists, and `data/quality/rule-index.json` records why.
`untested` — **a deletion candidate**: it is asserted and nothing enforces it.
`scripts/quality_report.py` §5 lists every one of those on every run, which is the point.


---
id: for-sale-extended-meta
enforced: untested
family: COPY
---

- **For-sale meta — extended 3-part format (ALWAYS, all for-sale/buy pages) — titles may run to ~280 chars** — Every for-sale-cluster page uses the extended 3-part meta (do NOT truncate to a short title): **Title** = `Primary Keyword | Related Conversational Query | Number + Positive Word | Brand — LSI/NLP Keywords` (front-load the primary keyword; extend toward but never past **280 characters**). **Description** = `Primary Benefit | Secondary Benefit | Trust Signal + CTA` (≤300). Real price floor + real credentials + branded ending, per the Verified-Claim Ledger. Canonical spec: `skills/cag-for-sale-page-builder.md §6a`.

---
id: shipping-cost-on-every-card
enforced: untested
family: COPY
---

- **Shipping cost on every card + shipping section (ALWAYS) — applies to every card/section builder** — Any bird/listing card MUST display shipping cost directly (canonical line under the trust badges: `Ships nationwide · $185 airport · $350 home`), and every shipping section MUST show the two delivery tiers (**Airport Pickup $185** · **Home Delivery $350**, IATA LAR, Delta/United/American). Figures live in `data/financial-entities.json` (`delivery_options`) + `data/price-matrix.json` — read them, never hardcode a different number. Never ship a card without the cost line.

# Directory Submission Playbook — 2026-06-06
Operator: cag-directory-submission-agent (run by main session)
Source of truth: `docs/reference/credentials.md` · Registry: `data/directories.json`

> **Realistic model for ALL submissions:** most directories (incl. GBP) require an
> account + email/phone/postcard verification. Account creation + password entry +
> verification are **user-only** steps (I cannot create accounts, enter passwords, or
> receive verification codes/postcards). The workflow is therefore:
> **(1) I prep the exact values + per-site quirks (this file) → (2) you log in / verify →
> (3) I co-drive the form-fill via your connected Chrome on sites where you're already
> logged in and no payment is involved → (4) you click the final submit.**

---

## MASTER FILL BLOCK (copy-paste — must match credentials.md exactly)

```
Business name:      C.A.Gs – Midland, TX
(never submit the bare domain "congoafricangreys.com" as the business name)
Alternate name:     Congo African Greys
Owner:              Mark & Teri Benjamin
Street:             2508 Briaroaks Ct           ← HIDE on public/service-area listings
City / State / ZIP: Midland, TX 79707
Country:            United States
Phone:              +1-281-545-3169             ← corrected 2026-06-06 (TX number; old 402/NE number retired)
Email:              Info@congoafricangreys.com
Website:            https://congoafricangreys.com
Facebook:           https://www.facebook.com/people/Congo-African-grey/61571657313840/
Founded:            2014
Primary category:   Pet Breeder        (fallback: Bird Shop)
Secondary category: Bird Shop / Pet Store
Service area:       Nationwide — ships to all 50 US states (IATA airline transport)
Hours:              By appointment / inquiry response within 24h

Short description (≤200 chars where required):
Captive-bred Congo & Timneh African Grey parrots from a USDA-AWA licensed, family-owned
Texas aviary (est. 2014). CITES Appendix I docs, DNA sexing, PBFD + Polyomavirus screening,
avian-vet health cert. Hand-raised, fully weaned. Ships nationwide.

Long description: (see credentials.md / agent business-info block)
```

---

## 1. GOOGLE BUSINESS PROFILE  (SKIPPED per user 2026-06-06 — revisit later)

**Status:** DEFERRED at user request. Kept here as a prepped kit for when you're ready.
**Cannot be automated by me** (Google login + verification are user-only). Resume any time.

**Setup decisions (my recommendations):**
- Business type → **Service-area business** (NOT storefront)
- Address → **enter for verification, then HIDE** (home-based privacy)
- Service area → add Midland TX + "United States" / key shipping metros
- Primary category → **Pet Breeder**; secondary → **Bird Shop**
- Hours → "Open by appointment" (or leave hours off for service-area)
- Add: logo, 3–5 bird photos, website, the short description above

**Verification:** Google will offer postcard / phone / email / video — **only you can
complete it.** Pick whichever Google offers fastest (often phone or video for SABs).

**Inputs needed when resumed:** 1. Which Google account owns it? 2. Hide home address?
(rec: yes) 3. Photos ready? (phone is now resolved → +1-281-545-3169)

**Why it's worth the friction later:** foundation citation — Yelp, Bing, Apple, MapQuest,
and dozens of aggregators cross-reference Google's NAP.

---

## ORDER OF ATTACK — EASIEST → HARDEST (GBP skipped)

Ranked by friction (account needed? verification? payment? audience-fit). Start at the top.

| Rank | Target | Difficulty | Why this rank |
|---|---|---|---|
| 🟢 1 | **Hoobly** | Easiest | Free, instant post, no real verification, huge AG volume. Fast win. |
| 🟢 2 | **Petzlover** | Easiest | "List for free", quick account, high AG traffic. |
| 🟢 3 | **BirdsNow** | Easy | Free tier, simple "Sell Your Bird" form. |
| 🟢 4 | **BirdTracks.io** | Easy | Free, UNTAPPED (0 competitors). Submit = one structured email (I draft, you send). |
| 🟡 5 | **Parrots Mag Registry** | Easy-Med | Free but submit by email/phone to the magazine (I draft, you send). |
| 🟡 6 | **BirdBreeders.com** | Medium | Account + list aviary (TX page). Verify free vs paid tier first. |
| 🟡 7 | **Yelp** | Medium | Account + (sometimes) phone verify. High trust/review value. Set SAB, hide address. |
| 🟡 8 | **FaunaClassifieds** | Medium | Free member ads; registration + forum norms. |
| 🟠 9 | **Bing Places** | Med-Hard | Microsoft acct + verification (can import from Google later). |
| 🟠 10 | **Apple Business Connect** | Med-Hard | Apple ID + verification. |
| 🟠 11 | **AFA listing** | Med-Hard | Member benefit — confirm/claim via the org. |
| 🔴 12 | **BBB** | Hardest (free part) | Listing free but heavy form; accreditation is paid (ask first). |
| ⏸️ — | **Google Business Profile** | Deferred | Skipped per user; resume when ready. |

**Recommended starting point: Hoobly** — zero account friction, free, instant, and it's
one of the Tier-2 platforms competitors already rely on. Fastest proof-of-concept for the
co-drive workflow before we hit the verification-heavy ones. Trade-off: Hoobly's domain
authority is lower than Yelp/Bing, so it's a warm-up win, not the highest-SEO-value link —
but starting easy de-risks the workflow and gets a live listing today.

## FIRST-WAVE SUBMISSION TABLE (detail)

| # | Target | Login needed? | Free? | Submission method | Per-site notes |
|---|---|---|---|---|---|
| 1 | Bing Places | Microsoft acct (user) | Free | Can import from Google | Do after GBP; mirrors NAP |
| 2 | Apple Business Connect | Apple ID (user) | Free | Web form | Service-area; hide address |
| 3 | Yelp for Business | acct (user) | Free | Claim/create | Trust+reviews; SAB, hide address |
| 4 | BBB | acct (user) | Free listing / paid accred. | Web form | Listing free; accreditation = paid (ask first) |
| 5 | Parrots Mag Registry | none | **Free** | **Email/phone** to magazine | Send-on-behalf → needs approval |
| 6 | BirdBreeders.com | acct (user) | Free + paid tiers | Create acct → list aviary (TX) | Verify which tier is free |
| 7 | BirdTracks.io | none | **Free** | **Email** (structured template) | Send-on-behalf → needs approval; untapped |
| 8 | Hoobly | acct (user) | Free | Post classified | Confirm CITES/captive-bred field |
| 9 | BirdsNow | acct (user) | Free tier | "Sell Your Bird" | Free unless paid ad upgrade |
| 10 | Petzlover | acct (user) | Free | Create listing | High AG volume |

**Co-drive candidates (I can fill the form via Chrome once you're logged in, you click submit):**
Yelp, BirdBreeders, Hoobly, BirdsNow, Petzlover, Apple, Bing — all web forms.

**Send-on-behalf candidates (I draft, you approve, then it's emailed):**
Parrots Mag Registry, BirdTracks.io — these submit by email, which is an approval-gated
"send a message on your behalf" action.

---

## 3. SECOND WAVE (after first wave verified live)
FaunaClassifieds · AFA member listing · PetClassifieds · The Avian Exchange (verify cost) ·
local citation batch (Manta, Foursquare, Yellowpages, Hotfrog, Cylex, Brownbook,
MerchantCircle, Chamberofcommerce.com) · MapQuest · hub.biz · Pinterest.

## Forums (separate track — earn, don't spam)
Avian Avenue (African Grey Alley) → ParrotForums → TalkParrots → r/AfricanGrey.
Profile bio + signature link, after genuine participation.

---

## NAP FLAG — RESOLVED 2026-06-06
Phone corrected to **+1-281-545-3169** (Texas / 281 Houston area code). The old
**+1-402-696-0317** (Nebraska) number has been retired site-wide: Footer.astro,
Schema.astro, index.astro + scams-page schema, credentials.md, and all agent/skill refs.
NAP is now in-state consistent. (281 is Houston-metro, not Midland-432, but it's an
in-state business line — a clear improvement over the out-of-state number.)

# CongoAfricanGreys.com — Website UI kit

Click-through prototype of the public marketing site at CongoAfricanGreys.com,
applying the "Terracotta Warmth" system from `uploads/design.md`.

## Routes (in `index.html`)

- **Home** — hero, trust row, current clutch (3 birds), founders block + visit info card, dark CTA, footer.
- **Available Birds** — page hero, trust row, full grid of 6 birds.
- **Contact** — page hero, contact form + reach-us-directly info card.
- **Confirmation** — post-submit thank-you with soft-hold on selected bird (if any).
- **About / Shipping** — scaffold pages (placeholder copy — real content lives in WordPress).

## Components

| File | Purpose |
|---|---|
| `Navbar.jsx`      | Forest-green sticky header, brand mark, links, clay CTA |
| `Hero.jsx`        | Warm-gradient hero with Lora display + clay italics |
| `TrustRow.jsx`    | Pill row of documentation & service signals |
| `BirdCard.jsx`    | Product-like card for an available bird (photo, tag, name, specs, inquire) |
| `InfoCard.jsx`    | White card with forest-green header + icon/key/value rows |
| `ContactForm.jsx` | Fake-submit form with pill selectors + clay square button |
| `DarkCTA.jsx`     | Bottom-of-page conversion block (uppercase clay on near-black) |
| `Footer.jsx`      | 4-column dark footer with brand, sitemap, contact, trust |

All components write to `window.<Name>` so each `<script type="text/babel">`
can find them in sibling files.

## Known shortcuts

- Bird photos are warm-tinted placeholder boxes labeled "Bird photo · drop in".
  Replace with real photography from production (`/wp-content/uploads/`) when available.
- Logo is the wordmark `🦜 CongoAfricanGreys` — swap for the real PNG when provided.
- Form is fake-submit. Real endpoint is Formspree `https://formspree.io/f/xrejpnvn`
  (per `uploads/design.md`) — wire that in when porting to production.
- The "About" and "Shipping & Care" pages are scaffolds only — there was no
  WordPress source to pull copy from.

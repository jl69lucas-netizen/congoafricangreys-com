# Higgsfield Image Generation Manifest — Homepage

Pending Higgsfield credit. Each job below is a **placeholder**: the live site uses the real OG photo (or current hero) noted under "Fallback in use." When credit is available, run via the `cag-photo-ingest` / `cag-infographic-builder` Higgsfield flow (MCP UUID `dd46f66a-ceb9-4042-b533-7b3fc3409318`).

Global CITES guardrails (from `data/parrot-image-schema.json`), append to every prompt:
- **Always:** captive-bred, domestic home setting, hand-raised
- **Never:** wild-caught, jungle, rainforest, imported, exotic wildlife, chains
- **Framing:** Bred in our Midland, TX home aviary with full CITES Appendix I documentation.

---

## JOB 1 — HERO (priority)

- **Model:** `soul_2` (reference) or `nano_banana_pro`
- **Reference photo:** `assets/brand/Male-and-Female-CONGO-African-Grey-Parrots.webp`
- **Aspect:** desktop 16:9 (export 1600×668) + mobile 9:16 (export 800×1126)
- **Fallback in use:** `/hero-desktop.webp`, `/hero-mobile.webp`
- **Prompt:**
  > Professional, warm hero photograph of two Congo African Grey parrots (bright scarlet red tails, pale yellow eyes, charcoal beaks) perched on a natural wood branch in a softly lit family living room, cream and forest-green palette, shallow depth of field, trustworthy and premium pet-breeder aesthetic. Captive-bred, domestic home setting, hand-raised. No wild-caught, no jungle, no cages.
- **On completion:** overwrite `public/hero-desktop.webp` (1600×668) and `public/hero-mobile.webp` (800×1126). No code change needed — `<picture>` in `index.astro` already references these.

## JOB 2 — Jins + Jeni pair — RESOLVED (real photo, no AI needed)

- Toy-figurine OG photo + $2,100 sign DELETED by breeder. Real pair photo provided.
- **Action pending:** breeder to save the real "kissing pair" photo to `assets/brand/jins-jeni-african-grey-pair.webp`, then copy → `public/jins-jeni-congo-african-grey-pair.webp` (overwrites stand-in). No AI generation required.

## JOB 3 — Talking video poster (optional)

- Currently the `<video>` poster reuses `/congo-african-grey-variant.webp`. Optional: generate a branded poster frame (9:16 or 16:9) with subtle "Hear them talk" treatment.

---

## Open data flags

1. ~~Jins + Jeni price ($2,100 vs $3,500)~~ — **RESOLVED**: toy/$2,100 image deleted; homepage keeps $3,500 pair.
2. ~~Elad variant~~ — **RESOLVED**: confirmed **Timneh** by breeder. No change.
3. **`.mov` videos** — `main-homepage-video-african-grey-parrots-video.mov` not browser-reliable (Chrome). Convert to `.mp4` (ffmpeg) before use. Only the `.mp4` talking video is wired in.
4. **Jins + Jeni real photo** — awaiting file drop at `assets/brand/jins-jeni-african-grey-pair.webp` (see JOB 2).

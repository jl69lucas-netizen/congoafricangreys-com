---
name: cag-photo-ingest
description: Ingests user-uploaded OG African Grey photos into the CAG content pipeline. Handles raw photo → AI enhancement → infographic → page placement workflow. Use when user uploads a photo and says "use this photo", "generate infographic from this photo", or provides an OG bird photo for a page section. Routes to Higgsfield (reference image), Nano Banana (lifestyle edit), or HTML/CSS infographic based on intent.
---

# CAG Photo Ingest Skill

**Announce at start:** "Using cag-photo-ingest skill to process uploaded photo for [page/purpose]."

---

## When to Use

Trigger when the user:
- Uploads a photo of a specific bird (ROYS, AMIE, BERY, ELAD, EVIE, etc.)
- Says "generate infographic from this photo"
- Says "use this as reference" for Higgsfield or Nano Banana
- Provides an OG African Grey photo for a page section
- Wants to create a video from a still photo ("animate this bird")

---

## Phase 1: Photo Assessment

1. **View the uploaded photo** using the Read tool (supports PNG, JPG, WEBP)
2. **Identify:** Which variant? (Congo = bright red tail / Timneh = dark maroon tail), setting (home/outdoor/aviary), bird name if visible in filename or metadata
3. **CITES safety check:** Photo must show a domestic setting (home, aviary, perch, human hand). If background is unclear or could be interpreted as wild/jungle, DO NOT use as-is — route to AI enhancement to swap background first
4. **Quality check:** Is the bird in focus? Adequate lighting? If poor quality, note — Higgsfield `soul_2` can enhance with a reference

---

## Phase 2: Route to Generation Mode

| User intent | Route | Tool |
|---|---|---|
| "Make an infographic from this" | HTML/CSS Types 1–3 using photo as visual reference only | `skills/cag-infographic.md` Type 1–3 |
| "Create an AI image based on this photo" | Higgsfield `generate_image` with uploaded photo as reference | Type 5 (below) |
| "Animate this / make a video" | Higgsfield `generate_video` | Higgsfield video tools |
| "Lifestyle edit (change background)" | Higgsfield `flux_kontext` or Nano Banana image-to-image | Higgsfield `flux_kontext` |
| "Make it look professional" | `soul_2` with reference photo | Higgsfield MCP |

---

## Phase 3: Higgsfield Reference Image Flow

If routing to Higgsfield with the uploaded photo as reference:

**Step 1: Load tools**
```
ToolSearch: select:mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__media_upload,mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__media_confirm,mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__generate_image,mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__balance
```

**Step 2: Check credits**
```
mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__balance
```
If credits < 2, pause and notify user.

**Step 3: Upload photo**
```
mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__media_upload
```
Confirm upload:
```
mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__media_confirm
```
Note the returned media ID.

**Step 4: Build CITES-safe prompt**

Read `data/parrot-image-schema.json`. Determine if bird is Congo or Timneh from Phase 1.

Prompt structure:
```
[Visual intent] — [Species-accurate description from schema] — [domestic setting from schema visual_style] — [certification_overlays if needed] — captive-bred, home aviary, hand-raised, Midland Texas. [NEVER: wild-caught, jungle, tropical, imported, exotic wildlife]
```

**Step 5: Generate**
```json
{
  "model": "soul_2",
  "prompt": "[CITES-safe prompt from above]",
  "aspect_ratio": "9:16",
  "medias": [{"value": "<media_id_from_step_3>", "role": "image"}]
}
```

**Step 6: Display result**
Call `mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__job_display` with the returned job ID. Show to user for approval before any page integration.

---

## Phase 4: Output Standards

- **File naming:** `[bird-name]-[context]-[date].webp` (e.g., `roys-portrait-2026-05.webp`)
- **File destination:** `src/public/images/birds/`
- **Display size:** `max-width: 350px; width: 100%; height: auto;` via CSS
- **Alt text:** "[Bird name] — [Congo/Timneh] African Grey parrot, captive-bred, Midland TX"
- **Hand off to:** `@cag-image-pipeline` for final placement + `<img>` ref updates in target page

---

## CITES Safety Rule

Every generated image MUST use these prompt guardrails from `data/parrot-image-schema.json`:

| Field | Value |
|---|---|
| `prompt_safety.always_include` | "captive-bred, domestic setting, hand-raised" |
| `prompt_safety.never_include` | "wild-caught, imported, trapped, CITES violation, illegal" |
| `prompt_safety.cites_framing` | "All birds bred in our Midland TX home aviary with full CITES Appendix I documentation" |

**If any uploaded photo shows an ambiguous background**, do NOT generate an image claiming that setting is domestic. Either use Higgsfield `flux_kontext` to swap the background first, or generate a fresh image using the photo only as a character reference (not a scene reference).

---

## Known Birds — Quick Reference

Read `data/clutch-inventory.json` for current availability status before referencing any bird in page copy.

| Bird | Variant | Notes |
|---|---|---|
| ROYS | Congo | Male, 4 months |
| AMIE | Congo | Female, 3 months |
| BERY | Congo | Female, 1 year |
| ELAD | Timneh | Male, 5 months |
| EVIE | Timneh | Female, 6 months |
| JINS+JENI | Congo pair | Unrelated bonded pair, $3,500 |

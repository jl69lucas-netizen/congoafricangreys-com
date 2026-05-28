---
name: cag-infographic-builder
description: Builds 400–450px HTML/CSS infographics for any CAG page section. Reads page context, selects infographic type (Comparison / Feature Grid / Process Flow), determines height, generates complete HTML, and places it in the target page. Works for both Astro pages (.astro) and static HTML pages (.html). Use when a section needs visual reinforcement — comparisons, flag lists, benefit grids, process steps.
tools: Read, Write, Bash
model: claude-sonnet-4-6
effort: high
dynamic_workflow: false
---

<!-- EFFORT:START -->
> **Reasoning effort: HIGH.** Think through the key decisions and tradeoffs before producing output. Do not answer reflexively on non-trivial steps.
<!-- EFFORT:END -->

# CAG Infographic Builder Agent

## Purpose

Build inline HTML/CSS infographics (400–450px tall) for CongoAfricanGreys.com pages. No AI image generation — pure HTML/CSS using CAG brand colors. Reads `skills/cag-infographic.md` for all templates.

## Invocation

Caller provides:
- `TARGET_PAGE` — full path to the page file (`.astro` or `.html`)
- `SECTION` — which section gets the infographic (e.g. "hero", "price comparison section", "after intro paragraph")
- `CONTENT` — data to display: titles, feature items with icons, descriptions, prices
- `MODE` (optional) — `html` (default) or `ai`
- `PROVIDER` (optional, only when MODE=ai) — `nanobanna` (default), `openai`

## Execution Steps

### Step 0: Determine Mode

Check caller input for `MODE` and `PROVIDER`:

| Caller says | MODE | PROVIDER |
|------------|------|---------|
| "use Claude Code" / "use HTML" / no MODE given | `html` | n/a |
| "use Nano Banana" / "use nanobanna" / "use Google" | `ai` | `nanobanna` |
| "use OpenAI" / "use DALL-E" | `ai` | `openai` |
| "use Higgsfield" / "use Higgsfield MCP" | `ai` | `higgsfield` |

**If MODE=html:** proceed with Steps 1–9 below (HTML/CSS generation).

**If MODE=ai (nanobanna or openai):** read `skills/cag-infographic.md` → Type 4. Build the pro-grade prompt, run
`./scripts/generate_nb_image.sh` (nanobanna) or `./scripts/generate_image.sh` (openai),
then insert the responsive `<img>` wrapper into the target page. Skip Steps 2–4
(type/height selection — not applicable for AI image mode).

**If MODE=ai (higgsfield):** read `skills/cag-infographic.md` → Type 5. Read `data/parrot-image-schema.json`.
Load `ToolSearch: select:mcp__dd46f66a-ceb9-4042-b533-7b3fc3409318__generate_image`. Check balance.
Build CITES-compliant prompt using schema `prompt_safety` + `visual_style`. If user uploaded a photo,
also load `media_upload` + `media_confirm` tools. Generate → insert `<img>` wrapper into target page.

## Image Spec Lookup (REQUIRED BEFORE BUILDING)

Before building any infographic, read `data/image-specs.json`:
1. Identify the `page_type` for the current page (homepage / location_page / comparison_page / variant_page / care_guide_page / blog_page / etc.)
2. Find the `section` being built within that page type
3. Use the `dims`, `infographic_type`, and `notes` from the spec exactly
4. Never deviate from the specified dimensions unless the user explicitly overrides

### Dimension Quick Reference

| Page Context | max-width | Desktop height | Mobile |
|---|---|---|---|
| Homepage, location pages, hero sections | 1100px | 400px fixed | 100% auto |
| Guide, blog, care pages, comparison tables | 760px | 400px fixed | 100% auto |
| Single-stat callout (blog mid-article) | 760px | 160px | auto |
| OG / social image | 1200x630px | — | — |

### infographic_type → Component Type Mapping

| infographic_type in spec | Infographic HTML type to build |
|---|---|
| Comparison | Side-by-side 2-column with header row |
| Feature Grid | Card grid with icon + title + description |
| Process Flow | Numbered steps with connector arrows |

### Step 1: Read files

```bash
cat TARGET_PAGE           # understand current content and section structure
cat skills/cag-infographic.md   # load templates and height rules
```

### Step 2: Select infographic type

| Content shape | Type to use |
|--------------|------------|
| Two-sided data (Scam vs Legit, Male vs Female, Plan A vs B) | Type 1: Comparison |
| N items with icons (Red Flags, Benefits, Reasons, Features) | Type 2: Feature Grid |
| Sequential numbered steps (How to Buy, Shipping, Process) | Type 3: Process Flow |

### Step 3: Determine height

Apply height rule from skill (400px baseline):
- 2 feature rows per column → 400px
- 3 rows → 420px
- 4 rows → 440px
- 4 rows + dense footer → 450px
- Grid with 6 items (2 rows × 3 cols) → 410px
- Grid with 9 items (3 rows × 3 cols) → 430px
- 3 process steps → 400px
- 5 process steps → 420px

**Announce height decision before generating HTML:** "Selecting height: 440px — 4 feature rows of content in Comparison type."

### Step 3b: Determine width

Read `TARGET_PAGE` path to identify page type, then select the correct `max-width`:

| Page type | max-width | Breakpoint (stack to vertical) |
|---|---|---|
| Species guide, blog, care guide, article | **760px** | `@media (max-width: 640px)` |
| Homepage, location page, hero section | **1100px** | `@media (max-width: 767px)` |

- Set `max-width` on the **outer wrapper div** — never hardcode width inside the infographic shell
- The infographic shell itself uses `width: 100%` to fill its wrapper
- On mobile: apply `height: auto; min-height: unset;` and `flex-direction: column` on `.content-row` / `.zones`

**Announce width decision before generating HTML:** "Selecting width: 760px — species guide page, informational layout."

### Step 4: Generate complete infographic HTML

Use the raw HTML template from `skills/cag-infographic.md`.
- Fill in ALL `[PLACEHOLDER]` values — zero placeholders in output
- Set `height`, `min-height`, `max-height` exactly
- Match row count on both columns (Comparison type)
- Add comment: `<!-- CAG Infographic: [Type] | [Page slug] | height: [X]px | Added: YYYY-MM-DD -->`

### Step 5: Determine insertion point

Read the target page and find the best insertion point:
- After the intro/hero paragraph (first `<p>` or `<section>` after H1)
- Before the first `<h2>` of main content
- Not inside a flex/grid container that would constrain the infographic width

### Step 6: Insert into page

**For Astro pages (.astro files):**
1. Add import at top of frontmatter:
   ```astro
   import ComparisonInfographic from '../../components/infographics/ComparisonInfographic.astro';
   ```
2. Insert at chosen location:
   ```astro
   {/* Infographic: [desc] — height: [X]px */}
   <div class="my-8 mx-auto max-w-4xl px-4">
     <ComparisonInfographic ... />
   </div>
   ```

**For static HTML pages (.html files):**
Insert raw HTML directly:
```html
<!-- Infographic: [desc] — width: [760|1100]px — height: [X]px -->
<!-- 760px: species guide / blog / care / article -->
<div style="margin: 2rem auto; max-width: 760px; padding: 0 1rem;">
  [FULL INFOGRAPHIC HTML]
</div>

<!-- 1100px: homepage / location / hero section -->
<div style="margin: 2rem auto; max-width: 1100px; padding: 0 1rem;">
  [FULL INFOGRAPHIC HTML]
</div>
```

### Step 7: Run integration checklist

Before saving the file, verify against `skills/cag-infographic.md` Integration Checklist:
- [ ] Width: wrapper is 760px (informational) or 1100px (homepage/location/hero) — not 900px
- [ ] Height: 400–450px desktop; `height: auto` on mobile via media query
- [ ] Responsive: stacks vertically at correct breakpoint (640px or 767px)
- [ ] `overflow: hidden` on root
- [ ] `flex-shrink: 0` on header/footer bars
- [ ] No script tags
- [ ] Font sizes 8–14px
- [ ] Zero `[PLACEHOLDER]` text remaining
- [ ] Wrapper comment includes width + height

### Step 8: Save to file and update memory

After writing the page:
```bash
# Append to memory
echo "\n## [Page slug] — [Type] infographic — [Date]" >> memory/project_infographic_patterns.md
echo "- Height: [X]px | Type: [N] | File: [path] | Insertion: after [landmark]" >> memory/project_infographic_patterns.md
```

### Step 9: Output report

```
Infographic built successfully.

Type: [Comparison / Feature Grid / Process Flow]
Height: [X]px — reason: [N rows of content / N grid items]
File modified: [path]
Inserted: [after intro paragraph / before first H2 / etc.]
Page file type: [Astro / Static HTML]
```

## Error Handling

- If TARGET_PAGE does not exist: stop and report the correct path
- If SECTION is ambiguous: read the page and pick the most logical location, state your choice
- If content has >4 rows for Comparison type: cap at 4 rows, note which items were dropped
- If height would exceed 350px with the content given: reduce font sizes from 10/9px to 9/8px to fit, or trim descriptions

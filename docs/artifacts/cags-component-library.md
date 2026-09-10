# C.A.Gs Component Library

**Artifact URL:** https://claude.ai/code/artifact/6be797ba-d2bf-4cb8-b8e2-601cbade03d2

Every live C.A.Gs component captured in a real browser at 375, 768 and 1280. 38 components, 104 captures, generated 2026-09-10 from commit `0766652`.

Rebuild: `node scripts/component_library_capture.mjs` to re-capture, then `node scripts/build_component_library.mjs` to regenerate this file and the HTML page beside it.

A capture marked `hidden` means the component does not render at that width, which is the component telling you its own responsive contract.

## hero (8)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| Hero V3:b Authority Green | [/](https://congoafricangreys.com/) | `src/components/cag-library/HeroV3.astro` | `.hero-v3-b` | ✓ | ✓ | ✓ | `import HeroV3 from 'src/components/cag-library/HeroV3.astro';` |
| Split-Hero (congo for-sale) | [/congo-african-grey-for-sale/](https://congoafricangreys.com/congo-african-grey-for-sale/) | `src/pages/congo-african-grey-for-sale/index.astro` | `.chero` | ✓ | ✓ | ✓ | Inline in `src/pages/congo-african-grey-for-sale/index.astro`; search for `.chero` |
| Split-Hero (timneh for-sale) | [/timneh-african-grey-for-sale/](https://congoafricangreys.com/timneh-african-grey-for-sale/) | `src/pages/timneh-african-grey-for-sale/index.astro` | `.chero` | ✓ | ✓ | ✓ | Inline in `src/pages/timneh-african-grey-for-sale/index.astro`; search for `.chero` |
| Dark + Grid (dna-tested) | [/dna-tested-african-grey-for-sale/](https://congoafricangreys.com/dna-tested-african-grey-for-sale/) | `src/pages/dna-tested-african-grey-for-sale/index.astro` | `header.hero` | ✓ | ✓ | ✓ | Inline in `src/pages/dna-tested-african-grey-for-sale/index.astro`; search for `header.hero` |
| Polaroid Scatter (breeding pair) | [/african-grey-breeding-pair-for-sale/](https://congoafricangreys.com/african-grey-breeding-pair-for-sale/) | `src/pages/african-grey-breeding-pair-for-sale/index.astro` | `.phero` | ✓ | ✓ | ✓ | Inline in `src/pages/african-grey-breeding-pair-for-sale/index.astro`; search for `.phero` |
| Mosaic Metrics (hub) | [/african-grey-parrots-for-sale/](https://congoafricangreys.com/african-grey-parrots-for-sale/) | `src/pages/african-grey-parrots-for-sale/index.astro` | `#main-content section.bg-logo-dark` | ✓ | ✓ | ✓ | Inline in `src/pages/african-grey-parrots-for-sale/index.astro`; search for `#main-content section.bg-logo-dark` |
| Eggs Hero | [/african-grey-parrot-bird-eggs-for-sale-usa/](https://congoafricangreys.com/african-grey-parrot-bird-eggs-for-sale-usa/) | `src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro` | `.egg-hero` | ✓ | ✓ | ✓ | Inline in `src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro`; search for `.egg-hero` |
| Comparison Two-Portrait Hero | [/congo-vs-timneh-african-grey/](https://congoafricangreys.com/congo-vs-timneh-african-grey/) | `src/pages/congo-vs-timneh-african-grey/index.astro` | `.cvt-hero` | ✓ | ✓ | ✓ | Inline in `src/pages/congo-vs-timneh-african-grey/index.astro`; search for `.cvt-hero` |

## counter (3)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| Counter Snippet (home) | [/](https://congoafricangreys.com/) | `src/components/cag-library/CounterSnippet.astro` | `.counter-snippet` | ✓ | ✓ | ✓ | `import CounterSnippet from 'src/components/cag-library/CounterSnippet.astro';` |
| Counter Strip (congo) | [/congo-african-grey-for-sale/](https://congoafricangreys.com/congo-african-grey-for-sale/) | `src/pages/congo-african-grey-for-sale/index.astro` | `.counter-row` | ✓ | ✓ | ✓ | Inline in `src/pages/congo-african-grey-for-sale/index.astro`; search for `.counter-row` |
| Counter Strip (eggs) | [/african-grey-parrot-bird-eggs-for-sale-usa/](https://congoafricangreys.com/african-grey-parrot-bird-eggs-for-sale-usa/) | `src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro` | `.counter-row` | ✓ | ✓ | ✓ | Inline in `src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro`; search for `.counter-row` |

## toc (8)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| Desktop Dial .tdial (canonical) | [/timneh-african-grey-for-sale/](https://congoafricangreys.com/timneh-african-grey-for-sale/) | `src/pages/timneh-african-grey-for-sale/index.astro` | `.tdial` | hidden | hidden | ✓ | Inline in `src/pages/timneh-african-grey-for-sale/index.astro`; search for `.tdial` |
| Desktop Dial .cdial | [/congo-african-grey-for-sale/](https://congoafricangreys.com/congo-african-grey-for-sale/) | `src/pages/congo-african-grey-for-sale/index.astro` | `.cdial` | hidden | hidden | ✓ | Inline in `src/pages/congo-african-grey-for-sale/index.astro`; search for `.cdial` |
| Mobile Rail .chero-rail | [/congo-african-grey-for-sale/](https://congoafricangreys.com/congo-african-grey-for-sale/) | `src/pages/congo-african-grey-for-sale/index.astro` | `.chero-rail` | ✓ | ✓ | hidden | Inline in `src/pages/congo-african-grey-for-sale/index.astro`; search for `.chero-rail` |
| Mobile Rail .egg-rail | [/african-grey-parrot-bird-eggs-for-sale-usa/](https://congoafricangreys.com/african-grey-parrot-bird-eggs-for-sale-usa/) | `src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro` | `.egg-rail` | ✓ | ✓ | hidden | Inline in `src/pages/african-grey-parrot-bird-eggs-for-sale-usa/index.astro`; search for `.egg-rail` |
| Comparison Rail .cvt-rail | [/congo-vs-timneh-african-grey/](https://congoafricangreys.com/congo-vs-timneh-african-grey/) | `src/pages/congo-vs-timneh-african-grey/index.astro` | `.cvt-rail` | ✓ | ✓ | hidden | Inline in `src/pages/congo-vs-timneh-african-grey/index.astro`; search for `.cvt-rail` |
| JumpRail Dot Rail (desktop) | [/](https://congoafricangreys.com/) | `src/components/cag-library/JumpRail.astro` | `#cag-jump-rail` | hidden | hidden | ✓ | `import JumpRail from 'src/components/cag-library/JumpRail.astro';` |
| JumpRail Sections Sheet (mobile) | [/](https://congoafricangreys.com/) | `src/components/cag-library/JumpRail.astro` | `#cag-section-sheet` | ✓ | ✓ | hidden | `import JumpRail from 'src/components/cag-library/JumpRail.astro';` |
| TocV3 Grouped | [/](https://congoafricangreys.com/) | `src/components/cag-library/TocV3.astro` | `nav.toc-v3` | ✓ | ✓ | ✓ | `import TocV3 from 'src/components/cag-library/TocV3.astro';` |

## table (6)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| Male vs Female (home) | [/](https://congoafricangreys.com/) | `src/pages/index.astro` | `#compare-species table` | ✓ | ✓ | ✓ | Inline in `src/pages/index.astro`; search for `#compare-species table` |
| Grey vs Macaw/Cockatoo/Amazon (home) | [/](https://congoafricangreys.com/) | `src/pages/index.astro` | `#compare-species table` | ✓ | ✓ | ✓ | Inline in `src/pages/index.astro`; search for `#compare-species table` |
| Comparison .cmp-tbl (congo-vs-timneh) | [/congo-vs-timneh-african-grey/](https://congoafricangreys.com/congo-vs-timneh-african-grey/) | `src/pages/congo-vs-timneh-african-grey/index.astro` | `table.cmp-tbl` | ✓ | ✓ | ✓ | Inline in `src/pages/congo-vs-timneh-african-grey/index.astro`; search for `table.cmp-tbl` |
| Comparison .score-tbl (congo-vs-timneh) | [/congo-vs-timneh-african-grey/](https://congoafricangreys.com/congo-vs-timneh-african-grey/) | `src/pages/congo-vs-timneh-african-grey/index.astro` | `table.score-tbl` | ✓ | ✓ | ✓ | Inline in `src/pages/congo-vs-timneh-african-grey/index.astro`; search for `table.score-tbl` |
| .tblC (hand-raised) | [/hand-raised-african-grey-parrot-for-sale/](https://congoafricangreys.com/hand-raised-african-grey-parrot-for-sale/) | `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro` | `.tblC` | ✓ | ✓ | ✓ | Inline in `src/pages/hand-raised-african-grey-parrot-for-sale/index.astro`; search for `.tblC` |
| PricingTable Classic | [/](https://congoafricangreys.com/) | `src/components/cag-library/PricingTable.astro` | `#pricing` | ✓ | ✓ | ✓ | `import PricingTable from 'src/components/cag-library/PricingTable.astro';` |

## bird-card (2)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| BirdCard | [/](https://congoafricangreys.com/) | `src/components/BirdCard.astro` | `#available-birds article` | ✓ | ✓ | ✓ | `import BirdCard from 'src/components/BirdCard.astro';` |
| MiniBirdCard | [/african-grey-breeding-pair-for-sale/](https://congoafricangreys.com/african-grey-breeding-pair-for-sale/) | `src/components/cag-library/MiniBirdCard.astro` | `.mbc` | ✓ | ✓ | ✓ | `import MiniBirdCard from 'src/components/cag-library/MiniBirdCard.astro';` |

## reviews (2)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| Testimonials Feature | [/](https://congoafricangreys.com/) | `src/components/cag-library/Testimonials.astro` | `#reviews-mid` | ✓ | ✓ | ✓ | `import Testimonials from 'src/components/cag-library/Testimonials.astro';` |
| Testimonials Grid | [/](https://congoafricangreys.com/) | `src/components/cag-library/Testimonials.astro` | `#reviews` | ✓ | ✓ | ✓ | `import Testimonials from 'src/components/cag-library/Testimonials.astro';` |

## trust (2)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| TrustStats Classic | [/](https://congoafricangreys.com/) | `src/components/cag-library/TrustStats.astro` | `#health` | ✓ | ✓ | ✓ | `import TrustStats from 'src/components/cag-library/TrustStats.astro';` |
| ScamAwareness Grid + Proof List | [/](https://congoafricangreys.com/) | `src/components/cag-library/ScamAwareness.astro` | `#trust` | ✓ | ✓ | ✓ | `import ScamAwareness from 'src/components/cag-library/ScamAwareness.astro';` |

## key-takeaway (1)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| KeyTakeawayV2 | [/](https://congoafricangreys.com/) | `src/components/cag-library/KeyTakeawayV2.astro` | `[class*="takeaway"]` | ✓ | ✓ | ✓ | `import KeyTakeawayV2 from 'src/components/cag-library/KeyTakeawayV2.astro';` |

## owner (1)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| OwnerCard | [/](https://congoafricangreys.com/) | `src/components/cag-library/OwnerCard.astro` | `#about` | ✓ | ✓ | ✓ | `import OwnerCard from 'src/components/cag-library/OwnerCard.astro';` |

## faq (1)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| FAQ Accordion (home) | [/](https://congoafricangreys.com/) | `src/pages/index.astro` | `#faq` | ✓ | ✓ | ✓ | Inline in `src/pages/index.astro`; search for `#faq` |

## shipping (1)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| Shipping Split (home) | [/](https://congoafricangreys.com/) | `src/pages/index.astro` | `#shipping` | ✓ | ✓ | ✓ | Inline in `src/pages/index.astro`; search for `#shipping` |

## seam (1)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| Seam Divider | [/](https://congoafricangreys.com/) | `src/pages/index.astro` | `.cag-seam` | ✓ | ✓ | ✓ | Inline in `src/pages/index.astro`; search for `.cag-seam` |

## newsletter (1)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| NewsletterV2 | [/](https://congoafricangreys.com/) | `src/components/cag-library/NewsletterV2.astro` | `div[style*="#f0f9f4"]` | ✓ | ✓ | ✓ | `import NewsletterV2 from 'src/components/cag-library/NewsletterV2.astro';` |

## form (1)

| Component | Page | Source | Selector | 375 | 768 | 1280 | Usage |
|---|---|---|---|:--:|:--:|:--:|---|
| InquiryForm | [/](https://congoafricangreys.com/) | `src/components/cag-inquiry-form.astro` | `#contact` | ✓ | ✓ | ✓ | `import CagInquiryForm from 'src/components/cag-inquiry-form.astro';` |

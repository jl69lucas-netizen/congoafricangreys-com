# CongoAfricanGreys.com AI Build Pack
Generated: 2026-05-10

## Includes
1. Prompt Pack
2. Codex CLI Autopilot Commands
3. Claude Code Batch Workflow
4. 100+ Page Generation System
5. Deployment Workflow
6. QA Checklist

---

# 1. MASTER SYSTEM PROMPT

Use this in Claude / Codex / GPT:

You are an elite SEO strategist and conversion copywriter creating premium USA-focused content for CongoAfricanGreys.com.
Goal: outrank all African Grey breeder competitors.
Write trustworthy, human, high-converting, SEO-optimized markdown pages.

Requirements:
- EEAT
- semantic entities
- headings
- FAQs
- CTA
- internal links
- readable formatting

---

# 2. FOLDER STRUCTURE

/content
  /money-pages
  /geo-pages
  /comparison-pages
  /trust-pages
  /blog-pages
  /faq-pages
  /schema

---

# 3. CODEX CLI AUTOPILOT

## Initialize project

mkdir congoafricangreys-build
cd congoafricangreys-build

mkdir -p content/{money-pages,geo-pages,comparison-pages,trust-pages,blog-pages,faq-pages,schema}

## Example batch generation loop

for topic in "african-grey-for-sale" "baby-african-grey-for-sale" "congo-african-grey-for-sale" "trusted-african-grey-breeder-usa"
do
  echo "Generate page for $topic"
done

## Suggested Codex pattern

codex generate "Create premium SEO markdown page for african grey for sale. 2200 words. Include title/meta/H1/FAQs/CTA." > content/money-pages/african-grey-for-sale.md

---

# 4. CLAUDE CODE BATCH WORKFLOW

## Prompt

Read pages.csv.
Generate one markdown file per row.
Use keyword, URL, page type, intent.
Write unique content.
Save into correct folder.

## Example CSV

keyword,url,type,intent
african grey for sale,/african-grey-for-sale/,money,transactional
african grey for sale texas,/african-grey-for-sale-texas/,geo,local
african grey vs macaw,/african-grey-vs-macaw/,comparison,commercial

---

# 5. PAGE PROMPT TEMPLATES

## Money Page

Create a premium landing page for [KEYWORD].
2200 words.
Include trust signals, available birds, shipping, FAQs, CTA.

## Geo Page

Create unique local SEO page for [LOCATION].
Include buying guide, shipping, local relevance, FAQs.

## Comparison Page

Compare [TOPIC A] vs [TOPIC B].
Include table, verdict, buyer guidance.

## Blog Page

Create expert guide for [TOPIC].
Helpful, detailed, SEO optimized.

---

# 6. FIRST 100 PAGE MAP

## Money Pages (10)
african-grey-for-sale
african-grey-parrot-for-sale
baby-african-grey-for-sale
congo-african-grey-for-sale
male-african-grey-for-sale
female-african-grey-for-sale
hand-raised-african-grey-for-sale
dna-tested-african-grey-for-sale
talking-african-grey-for-sale
healthy-african-grey-for-sale

## Geo Pages (30)
texas
florida
california
new-york
ohio
houston
dallas
miami
orlando
los-angeles
...expand all major states/cities

## Comparison Pages (20)
african-grey-vs-macaw
african-grey-vs-amazon
african-grey-vs-cockatoo
congo-vs-timneh
male-vs-female-african-grey
breeder-vs-pet-store
buy-local-vs-shipping
...etc

## Trust Pages (10)
trusted-breeder-usa
health-guarantee
shipping-usa
why-buy-from-us
reviews
vet-checked
dna-sexing
our-process
safe-purchase-guide
scam-warning

## Blog Pages (30)
african-grey-lifespan
do-african-greys-talk
african-grey-price-guide
african-grey-diet-guide
african-grey-cage-setup
best-age-to-buy
first-time-owner-guide
...etc

---

# 7. INTERNAL LINKING RULES

Every page links to:
- homepage
- one money page
- one trust page
- two related pages

Use descriptive anchor text.

---

# 8. METADATA TEMPLATE

Title: Primary Keyword | Trusted USA Breeder
Description: Discover healthy hand-raised African Grey parrots with USA shipping. Learn more today.

---

# 9. SCHEMA TYPES

- Organization
- FAQPage
- BreadcrumbList
- Product (where applicable)
- Review

---

# 10. QA CHECKLIST

Before publish:
- unique page?
- keyword targeted?
- no duplication?
- clear CTA?
- internal links?
- meta title?
- meta description?
- FAQs?
- mobile readable?
- grammar clean?

---

# 11. DEPLOYMENT TO CLOUDFLARE PAGES

## Suggested Static Stack

- Astro
- Next static export
- Eleventy
- Hugo

## Flow

/content markdown files
-> build templates
-> static HTML
-> deploy to Cloudflare Pages

---

# 12. WEEKLY PUBLISHING SPRINT

Week 1: 10 money + trust pages
Week 2: 10 geo pages
Week 3: 10 comparisons
Week 4: 10 blogs

Repeat monthly.

---

# 13. KPI TRACKING

- rankings
- indexed pages
- clicks
- leads
- conversions
- branded searches
- backlinks

---

# 14. HUMAN REVIEW LAYER

Always manually improve:
- intros
- trust claims
- testimonials
- local references
- images
- bird inventory

---

# 15. SCALE GOAL

100 pages in 30 days
250 pages in 90 days
Topical authority in 6 months


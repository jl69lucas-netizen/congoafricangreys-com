# Lighthouse Verification Checklist

Run after deploying the static export to Netlify.

## How to Run

Use Chrome DevTools MCP:
```
mcp__plugin_chrome-devtools-mcp_chrome-devtools__lighthouse_audit
Parameters: {
  "url": "https://congoafricangreys.com/",
  "categories": ["performance", "accessibility", "best-practices", "seo"]
}
```

Also run on:
- `https://congoafricangreys.com/where-to-buy-african-greys-near-me/`
- `https://congoafricangreys.com/african-grey-parrot-for-sale-near-me/`

## Expected Scores (Post-Deploy)

| Category | Target | Key Fixes Applied |
|----------|--------|-----------------|
| Performance | 100 | jQuery deferred, WooCommerce CSS removed, font-display:swap, hero fetchpriority, lazysizes removed |
| Accessibility | 100 | <main> landmark added |
| Best Practices | 100 | local_ga_js removed, siteground-optimizer type=module, _headers created |
| SEO | 100 | Canonical URLs now absolute (https://congoafricangreys.com/slug/) |

## If Scores Are Not 100

### Performance < 100
- Check FCP, LCP, TBT values in Lighthouse output
- If TBT is still high: find remaining `<script>` tags without `defer` in `<head>` and add defer
- If LCP resource load delay > 2s: the hero preload may be loading wrong srcset size — check `<link rel="preload" as="image" href="...">` matches the actual loaded img src
- If Speed Index is high: check for render-blocking CSS (any `<link rel="stylesheet">` without `media="print"` workaround)

### Best Practices < 100
- Check console errors tab in Lighthouse output
- Remaining errors likely from third-party scripts (Google Analytics, etc.) loaded by the page
- Check if `siteground-optimizer` `type="module"` fix propagated correctly

### SEO < 100
- Run: `grep -r 'rel="canonical"' /Users/apple/Downloads/CAG/site/content --include="*.html"`
- All results must start with `href="https://congoafricangreys.com/`
- Check sitemap for relative URLs: `curl https://congoafricangreys.com/sitemap_index.xml`

### Accessibility < 100
- Check which elements Lighthouse flags
- Common remaining issues: color contrast, aria attributes on form fields
- Run axe-core for deeper accessibility audit

## WooCommerce Redirect Verification

After deploy, verify each redirect returns 301:
```bash
curl -I https://congoafricangreys.com/product/african-grey-parrots-for-sale-near-me/
# Expected: HTTP/2 301, Location: https://congoafricangreys.com/african-grey-parrot-for-sale-near-me/

curl -I https://congoafricangreys.com/product-category/buy-male-african-gray-birds-for-sale-nyc-ny/
# Expected: HTTP/2 301, Location: https://congoafricangreys.com/african-grey-parrot-for-sale-new-york/
```

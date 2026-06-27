# Google Maps Embed — Root Cause & Fix Reference

**Issue:** Maps show "This content is blocked. Contact the site owner to fix the issue."
**Date diagnosed:** 2026-05-31
**Pages affected:** Homepage (`/`), Contact Us (`/contact-us/`)

---

## Root Cause

Google Maps blocks embeds that use the wrong URL format or fabricated `pb=` parameters. There are two distinct failure modes:

### Failure Mode 1 — Wrong subdomain
```html
<!-- BROKEN — www.google.com blocks output=embed requests -->
<iframe src="https://www.google.com/maps?q=ADDRESS&output=embed"></iframe>
```
Google routes map embeds through `maps.google.com`, not `www.google.com`. Using the `www` subdomain causes Google to display the "content is blocked" error.

### Failure Mode 2 — Fabricated `pb=` parameter
```html
<!-- BROKEN — fake pb= codes are rejected by Google -->
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3307.2!...!4v1715000000000"></iframe>
```
The `pb=` embed code that appears in the "Share → Embed a map" button on Google Maps is cryptographically tied to a real place ID and real coordinates. Any AI-generated or manually approximated `pb=` value will be rejected. The `!4v1715000000000` timestamp is also validated by Google.

### Failure Mode 3 — CSP missing `frame-src` (separate risk)
The `site/content/_headers` file (staging) was missing `frame-src`. This would silently block all Google Maps iframes on Cloudflare Pages. **The `public/_headers` file (deployed) is correct** and already has:
```
frame-src https://www.google.com https://maps.google.com https://www.youtube.com https://www.youtube-nocookie.com;
```
Always edit `public/_headers` — it is the file Astro copies into `dist/` and Cloudflare Pages deploys.

---

## The Fix — Correct URL Format

**Always use this format:**
```html
<iframe
  src="https://maps.google.com/maps?q=ENCODED_ADDRESS&z=ZOOM&hl=en&t=m&output=embed&iwloc=near"
  width="100%" height="350" style="border:0;display:block;"
  loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen
  title="DESCRIPTIVE TITLE">
</iframe>
```

**For the CAG breeder HQ (Midland TX):**
```html
<iframe
  src="https://maps.google.com/maps?q=2508+Briaroaks+Ct%2C+Midland%2C+TX+79707&z=15&hl=en&t=m&output=embed&iwloc=near"
  width="100%" height="350" style="border:0;display:block;"
  loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen
  title="C.A.Gs – 2508 Briaroaks Ct, Midland TX 79707">
</iframe>
```

**Key parameters:**
| Parameter | Value | Notes |
|-----------|-------|-------|
| `q=` | URL-encoded address | Use `%2C` for comma, `+` for space |
| `z=` | 15 for street-level, 7 for state-wide | |
| `hl=en` | English UI | Required for consistent rendering |
| `t=m` | Roadmap type | `k`=satellite, `h`=hybrid |
| `output=embed` | Embed mode | Required |
| `iwloc=near` | Disables info window | Optional but cleaner |

---

## Never Do This

| Pattern | Why it breaks |
|---------|---------------|
| `www.google.com/maps?output=embed` | Wrong subdomain — Google blocks it |
| `www.google.com/maps/embed?pb=AI_GENERATED` | Fake pb= rejected by Google |
| `<embed src="...maps.google.com...">` | CSP `object-src 'none'` blocks all `<embed>` tags silently |
| Copying `pb=` from a screenshot or manually constructing it | The pb= token is not human-constructible |

---

## How to Get a Real `pb=` Code (if needed)

1. Go to [maps.google.com](https://maps.google.com)
2. Search for the address
3. Click **Share** → **Embed a map**
4. Copy the full `<iframe src="...">` — the `pb=` value inside is real and valid
5. Paste only that `src` value

Note: Real `pb=` codes are very long (100+ chars) and contain encoded place IDs like `0x86fb0d4a7c25e4d1:0x12ab...`. AI-generated short versions with round numbers are always fake.

---

## CSP Checklist — Before Any Deploy

Verify `public/_headers` contains all of these in the CSP `frame-src` directive:
- `https://maps.google.com`
- `https://www.google.com`
- `https://www.youtube.com`
- `https://www.youtube-nocookie.com`

**Never edit `site/content/_headers` for production config** — only `public/_headers` is deployed.

---

## Why Repeated Fix Attempts Failed

This issue was attempted 4+ times before this fix. The pattern of failure:

| Commit | What was tried | Why it still failed |
|--------|---------------|---------------------|
| `8a0610e` | `maps.google.com?output=embed` | Correct format — but push may not have gone live |
| `28e25c8` | `www.google.com/maps/embed?pb=FAKE` | Labeled "working" but pb= was AI-fabricated → rejected |
| `c1b9b9f` | Fixed CSP `frame-src` + "corrected" pb= | pb= coordinates still not a real Google Maps embed token |
| `99cab2f` | Reverted pb= → `?output=embed` BUT used `www.google.com` | Wrong subdomain (`www` vs `maps`) |
| `d536c2c` | Both pages → `maps.google.com/maps?q=...&output=embed` | **Correct — push needed to go live** |

**Key lesson:** The push (`git push`) failing silently leaves a broken live site even when the local code is correct. Always verify the Cloudflare Pages build completed after every commit.

## CRITICAL: Always Push After Commit

The deploy is `git push origin main` → GitHub Actions → Cloudflare Pages. If push is blocked by the Claude Code permission system, the user must run it manually in terminal. A committed-but-not-pushed fix does nothing on the live site.

## Files Fixed (2026-05-31)

| File | Change |
|------|--------|
| `src/pages/index.astro` | Changed `www.google.com/maps?` → `maps.google.com/maps?` |
| `src/pages/contact-us/index.astro` | Replaced fake `pb=` URL → `maps.google.com/maps?q=` format |

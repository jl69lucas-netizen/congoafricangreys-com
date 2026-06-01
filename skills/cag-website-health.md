---
name: cag-website-health
description: Technical site audit and auto-fixer for CongoAfricanGreys.com. Astro → Cloudflare Pages. Checks git/deploy state, build, canonicals, images, live site, Core Web Vitals. Runs scripts/health-sweep.sh as the one-command sweep.
model: claude-sonnet-4-6
tools: [Read, Write, Bash]
---

# CAG WEBSITE HEALTH & TECHNICAL FIX SKILL
## Technical Site Auditor & Auto-Fixer for CongoAfricanGreys.com
**Version 2.0 — Astro / Cloudflare Pages (rewritten 2026-06-01; v1 was a stale MaltipoosForsale copy)**

## Golden Rule
> Use Claude Code and Playwright CLI to solve problems first.
> Only call MCPs, external CLIs, or APIs if the task genuinely cannot be done with Claude Code alone.

---

## SITE CONTEXT (authoritative — do not use v1's old values)

| Property | Value |
|---|---|
| Domain | https://congoafricangreys.com |
| Stack | **Astro** static build |
| Host | **Cloudflare Pages** (NOT Netlify) |
| Deploy | GitHub Actions (`.github/workflows/deploy.yml`) → auto on push to `main` |
| **Authoritative pages** | **`src/pages/<slug>/index.astro`** (or `index.html`) — ~91 pages |
| Built output (what ships) | **`dist/**/index.html`** — ~101 pages |
| `site/content/` | **Staging only** — does NOT build directly; do not scan it for live state |
| Redirects | `site/content/_redirects` → copied to `public/_redirects` at deploy |
| Headers | `site/content/_headers` → copied to `public/_headers` at deploy |
| Brand assets | `assets/brand/`, `public/` |

> ⚠️ v1 of this skill hardcoded `/Users/apple/Downloads/MFS/site2`, the domain
> "african grey parrotsforsale.com", and Netlify. All three were wrong. Never
> reintroduce them.

---

## STEP 0: THE ONE-COMMAND SWEEP (do this first)

For any "is the site/system healthy?" request, run the full sweep:

```bash
bash scripts/health-sweep.sh            # full sweep (runs npm run build)
bash scripts/health-sweep.sh --no-build # faster, skips the build
```

It checks, in order, and exits non-zero on any critical failure:
1. **Git/deploy state** — token leak in remote URL, unpushed commits, uncommitted (undeployed) files
2. **Agent integrity** — 65 agents have `name`/`description`/`model`; `verify_model_tiers.sh` PASS=65
3. **Astro build** — `npm run build` compiles; reports page count
4. **Live site** — homepage, Congo, Timneh pages return 200; www → 301
5. **Built-output hygiene** — scans `dist/` for broken lazy-load images, missing/relative canonicals

Only drop into the manual steps below when the sweep flags something or you need
a deeper look (CWV, page-speed, a specific fix).

---

## STEP 0.5: GIT / DEPLOY / SECRET-LEAK HEALTH

Sweep section 1 covers this. The fix procedures for what it flags:

### Token embedded in git remote URL (CRITICAL)
A token in `.git/config`'s remote URL (`https://user:ghp_...@github.com/...`) is a
credential leak — plaintext on disk, and it lands in any transcript that prints the remote.

**Fix (agent does the local half; USER must rotate):**
1. **User rotates** the token in the provider dashboard (revoke + regenerate). Agents
   must NOT delete/create tokens — that's a security-settings change.
2. Strip the token from the URL and move auth to the keychain helper:
   ```bash
   git remote set-url origin https://github.com/jl69lucas-netizen/congoafricangreys-com.git
   ```
3. Re-store the new token via the **clipboard method** (never put the literal in a command):
   ```bash
   printf 'protocol=https\nhost=github.com\nusername=jl69lucas-netizen\npassword=%s\n\n' "$(pbpaste)" | git credential approve
   ```
4. Verify: `git push --dry-run origin main` (success = auth OK) and re-run the sweep.

Full procedure + API-key recipes: **`docs/reference/secure-credentials.md`**.
⚠️ Classic GitHub PATs are account-wide — revoking one can break other repos (e.g. MFS)
that reused it. Note: `git ls-remote` works anonymously on **public** repos, so it does
NOT prove push auth — always test with `git push --dry-run`.

### Uncommitted / unpushed work (not deployed)
Per CLAUDE.md "Always commit + push after build", finished work must be committed and
pushed (push = deploy). The sweep WARNs on a dirty tree or unpushed commits.
Build artifacts (`dist/`, `.astro/`, `node_modules/`, `.build-extract/`) and key files
(`.env`, `.*-key`) are gitignored — confirm with `git check-ignore <path>` before committing.

---

## STEP 1: DIAGNOSE (manual / deeper checks)

### A. Broken lazy-load images (WordPress GIF placeholders)
Legacy export artifact — `src` is a 1×1 GIF, real URL in `data-src`. Scan the **built output**:

```python
import re, glob
DIST = "dist"
broken = []
for f in glob.glob(f"{DIST}/**/index.html", recursive=True):
    c = open(f, encoding="utf-8", errors="ignore").read()
    n = len(re.findall(r'src="data:image/gif;base64,[^"]*"', c))
    if n: broken.append((f.replace(DIST, ""), n))
print(f"Pages with broken imgs: {len(broken)}, Total: {sum(n for _, n in broken)}")
```

### B. Relative canonical tags
Every canonical must be an absolute `https://congoafricangreys.com/...` URL.

```python
import re, glob
DIST = "dist"
for f in glob.glob(f"{DIST}/**/index.html", recursive=True):
    c = open(f, encoding="utf-8", errors="ignore").read()
    for href in re.findall(r'<link[^>]*rel=["\']canonical["\'][^>]*href="([^"]*)"', c):
        if not href.startswith("http"):
            print(f"Relative canonical: {f.replace(DIST,'')} -> {href}")
```

### C. www redirect
```bash
curl -s -o /dev/null -w "www: %{http_code}\n" https://www.congoafricangreys.com/
# Expect 301 (or 308). Rule lives in site/content/_redirects, copied to public/_redirects at deploy.
```

### D. Live vs local
```bash
curl -s -o /dev/null -w "%{http_code} %{time_total}s\n" https://congoafricangreys.com/
curl -s https://congoafricangreys.com/ | grep -oiE '<link[^>]*canonical[^>]*>' | head -1
```

---

## STEP 2: APPLY FIXES

> **Confidence Gate (CLAUDE.md):** ≥97% confidence before writing any site file.
> Auto-fix scripts edit `dist/` (regenerated on build) or source — when touching
> source under `src/pages/`, preview before apply.

### Fix A — Broken lazy-load images (source-level)
If broken images exist, fix them at the **source** (`src/pages/` / components), not `dist/`,
or they return on next build. Pattern: replace `src="data:image/gif;base64,..."` with the
`data-src` value, then strip `data-src`/`data-srcset`.

### Fix B — Relative canonicals
Astro pages should emit absolute canonicals from layout/frontmatter. If a relative one
appears, fix the source layout/component, not the built file. `cag-canonical-fixer` agent
owns static-export canonical conversion.

### Fix C — www redirect
Ensure `site/content/_redirects` contains the www→non-www rule (Cloudflare honors `_redirects`):
```
https://www.congoafricangreys.com/* https://congoafricangreys.com/:splat 301!
```

### Fix D — CSP / headers
Check `site/content/_headers` `Content-Security-Policy` for required domains
(`www.googletagmanager.com`, `maps.googleapis.com`, etc.). The `cag-google-map-agent`
documents the embed→iframe CSP `object-src` fix.

---

## STEP 3: VERIFY
Re-run `bash scripts/health-sweep.sh` (or `--no-build`). It re-scans `dist/` and reports
0 remaining issues, or rebuild first if you changed source.

---

## STEP 4: ISSUES REQUIRING MANUAL ACTION

| Issue | What's needed | Where |
|---|---|---|
| **Token leaked in git remote** | Rotate GitHub PAT, reconfigure remote to use a credential helper (no token in URL) | GitHub → Settings → Developer settings; then `git remote set-url` |
| Uncommitted work not live | Commit + push (push = deploy) — but honor "breeder approves before going live" | `git` |
| Cloudflare deploy failed | Check GitHub Actions run + Cloudflare Pages dashboard | repo Actions tab / Cloudflare |
| Schema `@id`/url hardcoded wrong | Review JSON-LD blocks | each page's `<script type="application/ld+json">` |

---

## STEP 5: REPORTING FORMAT

```
## CAG Website Health Report — [DATE]

### Sweep result: [ALL PASSED | N FAILURES]
### Critical
- [token leak / build fail / live-site non-200 — each with the fix]
### Decisions needed
- [uncommitted files, unpushed commits]
### Clean
- [agents, build, canonicals, live 200s — summarized]
### Next actions
1. ...
```

---

## STEP 6: CORE WEB VITALS / PAGE SPEED (deeper, run after rebuilds or quarterly)

Targets: **LCP < 2.5s**, **CLS < 0.1**, **INP < 200ms**, FCP < 1.8s, TTFB < 800ms.
Primary method = Playwright CLI; fall back to `npx lighthouse@latest`. (`cag-performance-monitor-agent`
owns scheduled Lighthouse runs.)

```bash
npx lighthouse@latest https://congoafricangreys.com/ \
  --output json --quiet --form-factor=mobile --throttling-method=simulate \
  --chrome-flags="--headless --no-sandbox" \
  | python3 -c "import json,sys;d=json.load(sys.stdin);a=d['audits'];print('LCP',a['largest-contentful-paint']['displayValue']);print('CLS',a['cumulative-layout-shift']['displayValue']);print('FCP',a['first-contentful-paint']['displayValue'])"
```

### Page-speed audits (source-level)
```bash
# Non-WebP images referenced in source (WebP conversion candidates)
grep -rohE 'src="[^"]*\.(jpg|jpeg|png)"' src/ | sort -u | wc -l
# Images missing loading="lazy"
grep -rn "<img" src/ | grep -v 'loading=' | head -20
# Scripts missing defer/async
grep -rn "<script" src/ | grep -vE "defer|async|application/ld\+json|type=" | head -20
# Cache rules present
grep -n "Cache-Control" site/content/_headers 2>/dev/null || echo "No cache rules in _headers"
```

---

## AGENT INTEGRATION
This skill is the **Technical Health** layer. Related, narrower agents:
- `cag-agent-system-qa` — audits the agent system itself
- `cag-performance-monitor-agent` — scheduled Lighthouse / CWV
- `cag-deploy-verifier` — post-deploy 200 checks + IndexNow
- `cag-canonical-fixer` — static-export canonical conversion
- `cag-site-hygiene-agent` — monthly technical SEO maintenance

Trigger this skill: before/after any deploy, after a batch rebuild, or for any
"is the site healthy?" request — start with `scripts/health-sweep.sh`.

---

## KNOWN ISSUES LOG
| Date | Issue | Status |
|---|---|---|
| 2026-06-01 | v1 skill was a stale MFS/Netlify/dog-domain copy scanning an empty `site/content/` | ✅ Rewritten to Astro/Cloudflare/`dist` + `src/pages` |
| 2026-06-01 | GitHub PAT embedded in git remote URL (`.git/config`) | ⚠️ Needs token rotation + remote reconfig (manual) |

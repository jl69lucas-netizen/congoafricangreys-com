# Research Fallback — Reddit & Blocked Sites

> Binding for **every research agent/skill** (competitor-intel, framework-agent, paa-agent,
> llm-keyword-intel, reddit-strategy, keyword-gap, rank-tracker, and any Sprint-0 research).
> When a source blocks our normal fetchers, escalate through this ladder instead of reporting
> "not fetchable" and moving on.

## Fetch escalation ladder (try in order)

1. **Firecrawl MCP** (`firecrawl_scrape` / `firecrawl_search`) — default.
2. **WebFetch / WebSearch** — for simple pages; retry a 403/429 once with a real browser UA
   (curl 403 ≠ dead — see memory `reference_external_link_curl_403`).
3. **Headless browser** — Playwright MCP (`browser_navigate` + `browser_snapshot`) or
   chrome-devtools MCP. Reddit, Facebook, and some competitor pages block curl/Firecrawl but
   render fine in a real headless browser (see `skills/reddit-strategy.md`).
4. **`last30days-skill`** — recency-scoped research fallback, especially good for **Reddit threads,
   recent news, and freshly-changed pages** that the above miss or that need a "last 30 days" window.
   - Source: **https://github.com/mvanhorn/last30days-skill**
   - Use it when Firecrawl is rate-limited/blocked and you need recent, real thread content
     (it pairs with, does not replace, the Playwright headless route).
   - **Not installed by default** — it must be added as a skill/tool before it can run. If a task
     needs it and it isn't installed, tell the breeder so they can install it (do not silently skip).

## Rules that still apply

- **Only report data you actually fetched** (Confidence-Gate / data-integrity rule). Un-fetchable
  after the full ladder = mark `NOT FETCHED`, never invent metrics, quotes, or thread text.
- **Reddit ethics** — real threads/quotes only, per `skills/reddit-strategy.md`.
- **CITES safety** — never cite or link sources that promote wild-caught trade.

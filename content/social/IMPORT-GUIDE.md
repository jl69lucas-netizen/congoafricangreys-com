# How to bulk-schedule the launch week

File to import: **`content/social/cag-social-schedule.csv`** (10 posts, Jun 9–16).
Regenerate any time with `python3 scripts/social_to_csv.py` (edit the `POSTS` list to add weeks).

## Columns
| Column | Meaning |
|---|---|
| `date` / `time` | Suggested slot (US Eastern). Adjust to your buyers' timezone. |
| `platform` | Instagram / Facebook / Pinterest / TikTok / YouTube |
| `title` | Pinterest pin title + YouTube title (blank for IG/FB/TikTok) |
| `text` | The caption / post body / YT+Pinterest description |
| `first_comment` | Instagram hashtags — posted as the first comment, keeping the caption clean (best practice) |
| `link` | Destination URL |
| `media` | File to attach. **Rows marked "REFRAME to 9:16 first" need the vertical version before posting** (Reels/TikTok/Shorts). |
| `status` | `draft` — flip to `approved` once Mark & Teri sign off |

## Recommended tool: Metricool or Publer
Both support multi-platform + video + CSV/bulk import on entry-level paid plans.

**Metricool** (≈$18/mo, "Planner" tier): Connect IG/FB/Pinterest/TikTok/YouTube → *Planner → Import* → upload the CSV → it maps columns → review → media is attached manually per post (CSV can't carry local video). Schedule.

**Publer** (≈$12/mo): *Bulk → CSV* → upload → it creates drafts → attach media → schedule. Publer supports `first_comment` natively.

**Buffer**: limited CSV; you may paste captions per post instead. Fine for IG/FB; weaker for TikTok/Pinterest.

## Important caveats (platform rules, not tool bugs)
1. **Media isn't in the CSV** — schedulers can't pull local video from a CSV path. Upload each clip/image into the tool when reviewing the imported draft. The `media` column tells you which file.
2. **Reframe first** — the 3 hero rows (Reels/TikTok/YT Short) need the Maxy clip in **9:16** before posting. Not done yet (you chose free-graphics-only; reframing is the paid Higgsfield step).
3. **Graphics** — for Pinterest rows whose media is a `graphics/*.html` file, open it in your browser and screenshot at the labeled pixel size to get the PNG.
4. **TikTok / IG** may still send a phone push asking you to tap "confirm post" — that's their API rule for some account types.
5. **Re-read availability** before posting — `data/clutch-inventory.json` changes as birds sell.

## Approval flow (the system's rule: never auto-post)
draft → Mark & Teri read the row → flip `status` to `approved` → schedule in the tool → it publishes.

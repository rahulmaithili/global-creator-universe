# Hashtag Engine

Assembles the hashtag set per post, per `SOCIAL/` hashtag rules.

## Reads
- Idea object (pillar, region, country, platform, series)
- `data/hashtag-bank/` — sets tagged by pillar + region

## Process
1. Start: brand tags (`hs_brand_core`) — always.
2. Add: pillar set matching the idea's pillar.
3. Add: 1–2 region tags matching the idea's region/country — ONLY when the
   location is genuine (no misleading location hashtags).
4. Add: series tag when the idea belongs to a series.
5. Mix check: 1–3 broad + 2–4 niche + 1–2 location + 1 brand/series.
6. Dedupe, cap at 15 — platform adapters trim further
   (Instagram ~8–12, Facebook ~3–5, YouTube ~3–5).

## Writes
- Episode-tracker: final `hashtags` array.

## Output
Ordered hashtag list → platform adapters.

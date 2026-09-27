# OUTPUT layer

Takes finished prompt packs and turns them into platform-ready publishing units.

## Structure

- `platforms/facebook/` — Facebook adapter (Reels-first, relatable posts,
  photo stories, audience questions).
- `platforms/instagram/` — Instagram adapter (Reels, carousels/photos,
  Stories, concise captions).
- `platforms/youtube/` — YouTube adapter (Shorts for discovery, 8–15 min
  long-form, series playlists).
- `daily-content-generator/` — the `DAILY PACK` pipeline: implements all
  14 steps of `GENERATOR/DAILY_WORKFLOW.md` + the daily minimum package.
- `calendar-365/` — `calendar.yaml`: 365 generated days (region/pillar/series
  rotation, daypart slots, monthly focus markers). Regenerate with
  `gen_calendar.py` when the strategy changes.

## Adapter contract

Each platform adapter receives the same prompt pack and outputs:

1. Platform-formatted caption (hook-first variant where needed)
2. Hashtag set sized to the platform (IG ~8–12, FB ~3–5, YT ~3–5)
3. CTA placed per platform convention (exactly one ask)
4. Format checklist (ratio, duration, safe zones)
5. Posting slot from `calendar.yaml`

The creative core never changes per platform — only the packaging does.
Per `SOCIAL/PLATFORM_STRATEGY.md`: adapt, never blindly duplicate.

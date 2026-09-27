# Trend Engine

Watches trends and rebuilds them as original character stories
(`TREND ADAPT`).

## Reads
- Trend inputs (manual brief or trend feed — implementation-defined)
- `data/pillars/pillars.yaml` — the `trends` pillar (5%)
- `CHARACTER/CHARACTER_LOCK.md` — non-negotiable
- `data/anti-duplicate-db/` — the trend must not already be covered

## Process (from STRATEGY/MASTER_STRATEGY.md)
1. TREND → understand the format.
2. Rebuild with the locked character — never copy another creator's exact
   script, visuals, or identity.
3. Create a NEW story around the format's mechanics (map onto a DB
   location/hook).
4. Dedup check: same trend adapted in the last 30 days → drop or angle-shift.
5. Emit idea object → normal pipeline (story → video/photo → caption → hashtag).

## Writes
- Anti-duplicate-db entry with `notes: trend:<trend_id>` for traceability.

## Output
Trend-adapted idea object. Shorter dedup window (30 days) — trends expire.

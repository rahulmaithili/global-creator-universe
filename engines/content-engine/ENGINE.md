# Content Engine

Turns a command + calendar slot into **the idea**: pillar, concept, series
placement.

## Reads
- `output/calendar-365/calendar.yaml` — today's slot: region, pillar, series, platforms
- `data/pillars/pillars.yaml` — the 9 pillars + weights + combination axes
- `data/series/series.yaml` — the 10 series (for series slots)
- `data/episode-tracker/` — where each series stands (next episode number)
- `data/anti-duplicate-db/` — recent fingerprints (pillar-level collision check)

## Process
1. Take the slot: region (country rotation: Mon USA · Tue UK · Wed UAE ·
   Thu USA · Fri Saudi · Sat Qatar/Kuwait/Bahrain/Oman · Sun global) + pillar
   + optional series.
2. If series slot → next episode number from episode-tracker; concept must
   advance the series arc (see story-engine).
3. If standalone → combine one item per combination axis
   (location × activity × emotion × conflict × twist × camera × weather ×
   outfit × CTA) from `data/pillars/pillars.yaml`.
4. Emit candidate idea: `{pillar, concept (one line), series, episode_number,
   region, country, platform}`.
5. Reserve fingerprint in anti-duplicate-db at `idea` status. Collision →
   apply the variation matrix (change ≥3 major elements) → max 3 tries →
   escalate to human.

## Writes
- Anti-duplicate-db entry (`idea` status, fingerprint reserved).

## Output
The idea object → story-engine, then video/photo engines.

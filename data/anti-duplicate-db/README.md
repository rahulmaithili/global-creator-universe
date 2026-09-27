# Anti-duplicate DB

The dedup gate. Every generated idea gets a fingerprint **before** production;
if the fingerprint collides with recent history, the idea is rejected and the
engine must generate an alternative.

## Fingerprint

```
fingerprint = hash(pillar + hook_core + location_id + outfit_id + food_id + series + episode_concept)
```

- `hook_core`: the hook stripped to its structural pattern
  (e.g. "nobody talks about X" → `contrarian_callout`), not the exact wording —
  so reworded repeats still collide.
- **Similarity window**: default 90 days per platform (tune in `schema.json`).
- Near-miss (same pillar + same location within window) → warning, human decides.

## Registry

`registry.json` — JSON array, validated against `schema.json`. Append-only:
never edit or delete entries, only add. Status flows `idea → prompted →
produced → posted`; a fingerprint is reserved at `idea` stage so parallel
runs can't double-book it.

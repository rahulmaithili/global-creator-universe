# Episode tracker

The single source of truth for everything ever made. Every series, every
episode, every standalone post — one registry.

## What gets logged

Each entry covers the full lifecycle: idea → prompt → assets → caption pack →
post links → performance notes. The anti-duplicate-db references entries here
via `episode_ref`.

## Registry

`registry.json` — JSON array, validated against `schema.json`. Entries are
never deleted. Status is the only mutable field, and it only moves forward.

## Series numbering

`series` + `episode_number` is unique. Standalone (non-series) content uses
`series: null` and a sequential `standalone_number` per platform.

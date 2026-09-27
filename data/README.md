# DATA layer — machine-readable compilation of the Brand Bible.

Conventions:
- **Curated lists** → YAML, human-editable, each entry has `id` + tags.
- **Registries** → JSON arrays validated against `schema.json` in the folder.
- **Rule**: engines may only pick entries that exist here. Anything new is
  emitted as `NEW_CANDIDATE` for human approval.

## Databases

| Folder | Type | Source in Brand Bible |
|---|---|---|
| `anti-duplicate-db/` | registry | `STRATEGY/ANTI_DUPLICATE.md` |
| `episode-tracker/` | registry | `GENERATOR/DAILY_WORKFLOW.md` |
| `location-db/` | YAML | `STRATEGY/LOCATION_ENGINE.md` |
| `food-db/` | YAML | food video/photo categories |
| `outfit-db/` | YAML | `CHARACTER/CHARACTER_SHEET.md` |
| `hook-db/` | YAML | video formula + engagement engine |
| `cta-db/` | YAML | `SOCIAL/CAPTION_HASHTAG_CTA_ENGINE.md` |
| `hashtag-bank/` | YAML | `SOCIAL/` hashtag rules |
| `pillars/` | YAML | `STRATEGY/CONTENT_PILLARS.md` + `MASTER_STRATEGY.md` |
| `series/` | YAML | `STRATEGY/SERIES_BIBLE.md` |

## Tagging standard
- `pillar`: content pillar id from `pillars/pillars.yaml`
- `region`: `USA`, `UK`, `Gulf`, `Global` (or a list)
- `country`: real country for locations/foods (accuracy rule)
- `platform`: `facebook`, `instagram`, `youtube`, or `all`
- `status` (registries): `idea` → `prompted` → `produced` → `posted`

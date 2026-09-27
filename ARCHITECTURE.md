# Architecture

## The two layers

**Brand Bible** (human-authored, stable): `CHARACTER/`, `STRATEGY/`, `VIDEO/`,
`PHOTO/`, `SOCIAL/`, `GENERATOR/`. This is the source of truth. The automation
layer never contradicts it — it *compiles* it into machine-readable form.

**Automation** (this layer): `data/`, `engines/`, `output/`, `identity/`.

## Tier contracts

### 1. DATA — `data/`
Curated lists as **YAML** (human-editable); registries as **JSON** validated
against `schema.json`.

| Database | Source in Brand Bible |
|---|---|
| `location-db` | `STRATEGY/LOCATION_ENGINE.md` |
| `food-db` | food pillar + video/photo food categories |
| `outfit-db` | `CHARACTER/CHARACTER_SHEET.md` (reference outfit) + usage rules |
| `hook-db` | video formula (0–2s hook) + engagement engine |
| `cta-db` | `SOCIAL/CAPTION_HASHTAG_CTA_ENGINE.md` CTA rotation (verbatim) |
| `hashtag-bank` | `SOCIAL/` hashtag rules |
| `pillars` | `STRATEGY/CONTENT_PILLARS.md` + `MASTER_STRATEGY.md` percentages |
| `series` | `STRATEGY/SERIES_BIBLE.md` |
| `anti-duplicate-db` | `STRATEGY/ANTI_DUPLICATE.md` (variation matrix) |
| `episode-tracker` | `GENERATOR/DAILY_WORKFLOW.md` steps 12–14 |

**Rule**: engines may only pick entries that exist in `data/`. Anything new is
emitted as `NEW_CANDIDATE` for human approval before entering a DB.

### 2. ENGINES — `engines/`
Each `ENGINE.md` declares reads / process / writes / output, grounded in:

- Character master sentence (`CHARACTER/CHARACTER_LOCK.md`): *"Use the locked
  main character from the approved reference image and preserve the exact
  recognizable facial identity and core appearance throughout the generation."*
- Hard negatives (`CHARACTER/CHARACTER_SHEET.md`): no face replacement, no age
  change, no duplicate protagonist, no distorted hands, no watermark, no
  unwanted text, no cartoon look unless requested.
- Video formula (`STRATEGY/MASTER_STRATEGY.md`): 0–2s hook · 2–8s setup ·
  8–20s escalation · 20–28s twist/payoff · final seconds: comment-worthy
  choice/question.
- Output template (`GENERATOR/MASTER_OUTPUT_TEMPLATE.md`) — never omit the
  character lock.
- Quality gate (`GENERATOR/DAILY_WORKFLOW.md`): reject if identity unclear,
  hook too slow, no reason to keep watching, no payoff, generic CTA, duplicate,
  or misleading location claim.

### 3. OUTPUT — `output/`
- **Platform adapters** (`output/platforms/*`): apply `SOCIAL/PLATFORM_STRATEGY.md`
  — Facebook Reels-first, Instagram Reels/carousels/stories, YouTube Shorts +
  8–15 min long-form. Same core story, adapted hook/title/CTA per platform —
  never blind duplication.
- **Daily generator** (`output/daily-content-generator/`): the `DAILY PACK`
  pipeline implementing `GENERATOR/DAILY_WORKFLOW.md`'s 14 steps.
- **Calendar** (`output/calendar-365/calendar.yaml`): 365 generated days from
  `STRATEGY/365_DAY_ENGINE.md` (daily minimum 2 videos + 2 photos, weekly
  rotation, country rotation, monthly new-city/food/adventure rules).

### 4. IDENTITY — `identity/`
Platform-specific public identity. Core character identity stays in
`CHARACTER/`; each platform gets its own section here.

## The write-back loop

Every run **reads** `data/`, generates the pack, then **writes back** to
`episode-tracker` and `anti-duplicate-db`. The dedup fingerprint covers
location + activity + food + outfit + hook pattern + dialogue + camera +
emotional beat + twist + CTA + caption structure — per
`STRATEGY/ANTI_DUPLICATE.md`'s variation matrix, a repeated location must
change at least three major elements.

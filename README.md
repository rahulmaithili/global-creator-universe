# Global Creator Universe

Permanent source-of-truth for a global creator content system — now with an
automation layer.

## Mission
Create unlimited original short-form videos, photos, stories and lifestyle
content around one locked main character while changing locations, activities,
outfits, stories and situations.

## Target
Primary: USA · Secondary: UK · Expansion: UAE, Saudi Arabia, Qatar, Kuwait,
Bahrain, Oman and global English-speaking audiences.

## Core rule
CHARACTER IDENTITY STAYS CONSISTENT. WORLD, STORY, OUTFIT, LOCATION AND ACTIVITY MAY CHANGE.

## Repo layers

| Layer | Folders | Status |
|---|---|---|
| Brand Bible (the rulebook) | `CHARACTER/` `STRATEGY/` `VIDEO/` `PHOTO/` `SOCIAL/` `GENERATOR/` | ✅ Complete |
| Automation (the machine) | `data/` `engines/` `output/` `identity/` | ✅ Phase 1 complete |

- **Brand Bible** — character lock + sheet, content pillars, 365-day engine,
  location engine, master prompts, categories, series bible, caption/hashtag/CTA
  system, platform strategies, prompt commands, output template, daily workflow.
- **`data/`** — machine-readable databases built from the Brand Bible: locations,
  foods, outfits, hooks, CTAs, hashtags, pillars, series + the two registries
  (`anti-duplicate-db`, `episode-tracker`) that make the system automatic.
- **`engines/`** — the 7 engines as specs, each grounded in the real Brand Bible
  files (master prompts, video formula, output template, quality gate).
- **`output/`** — platform adapters, the `DAILY PACK` pipeline, and a generated
  `calendar.yaml` (365 days).
- **`identity/`** — platform-specific public identity, starting with Facebook.

## The loop (what makes it automatic)

```
command in → engines read data/ → dedup gate → prompt pack out
                                                ↓
                                   episode-tracker + anti-duplicate-db
                                                ↓
                                   next run sees history → no repeats
```

## Quick Commands
- VIDEO: `<location>` | `<topic>` | `<mood>` | `<duration>`
- PHOTO: `<location>` | `<topic>` | `<mood>`
- NEXT VIDEO / NEXT PHOTO
- REMAKE: `<concept>`
- SERIES: `<topic>` | episode `<number>`
- STORY: `<topic>`
- DAILY PACK: `[n]` videos + `[n]` photos
- TREND ADAPT: `<trend description>`
- GLOBAL: `<topic>`

Every command inherits `CHARACTER/CHARACTER_LOCK.md`. Every generated package
follows `GENERATOR/MASTER_OUTPUT_TEMPLATE.md`. See `ARCHITECTURE.md` for the
full contract between layers.

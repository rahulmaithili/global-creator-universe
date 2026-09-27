# 365-day calendar

`calendar.yaml` — 365 generated days from `STRATEGY/365_DAY_ENGINE.md`,
starting 2026-09-28 (Monday). Regenerate with the script noted at the bottom
when the strategy changes.

## Rotation logic (built into every entry)

**Country rotation** (region + country):
Mon USA · Tue UK · Wed UAE · Thu USA→Gulf lifestyle · Fri Saudi Arabia ·
Sat Qatar/Kuwait/Bahrain/Oman (rotating) · Sun Global

**Weekly pillar rotation:**
Mon lifestyle (USA everyday life) · Tue travel (city) · Wed food ·
Thu lifestyle (Gulf lifestyle) · Fri adventure · Sat luxury (cruise/ship) ·
Sun comedy (global relatable story)

**Series mapping:**
Mon everyday_unexpected_ending · Tue rahul_goes_global / airport_to_adventure
(alternating) · Wed food_i_didnt_expect · Thu rahul_goes_global ·
Fri sixty_seconds_comfort_zone · Sat cruise_life · Sun expectation_vs_reality

**Daypart slots** (every day): morning (lifestyle/coffee/gym/routine) ·
afternoon (food/travel/exploration) · evening (comedy/story/adventure) ·
night (interactive question/mini-story)

**Daily minimum:** 2 videos + 2 photos · **Trend slot:** open every day ·
**Monthly rule:** on the 1st of each month the entry carries
`monthly_focus` — 4 new cities, 4 new food experiences, 4 new adventure
settings, 2 new transport concepts, 1 connected mini-series.

## Entry fields
`date, weekday, region, country, pillar, theme, series, platforms,
videos, photos, trend_slot, dayparts[], monthly_focus (optional), notes`

## Consumers
- `daily-content-generator` reads today's entry every run.
- `content-engine` uses it as the slot definition.

## Regeneration
`python3 gen_calendar.py` (kept next to this file) rebuilds `calendar.yaml`
from the rules above.

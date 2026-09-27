#!/usr/bin/env python3
"""Regenerate calendar.yaml from the 365-day engine rotation rules."""
import datetime

START = datetime.date(2026, 9, 28)  # a Monday
DAYS = 365

WEEKLY = {
    # weekday: (region, country, pillar, theme, series)
    0: ("USA", "USA", "lifestyle", "USA everyday life", "everyday_unexpected_ending"),
    1: ("UK", "UK", "travel", "travel/city", None),  # series alternates below
    2: ("Gulf", "UAE", "food", "food", "food_i_didnt_expect"),
    3: ("Gulf", "Saudi Arabia", "lifestyle", "Gulf lifestyle", "rahul_goes_global"),
    4: ("Gulf", "Saudi Arabia", "adventure", "adventure", "sixty_seconds_comfort_zone"),
    5: ("Gulf", None, "luxury", "cruise/ship/luxury", "cruise_life"),  # country rotates
    6: ("Global", None, "comedy", "global relatable story", "expectation_vs_reality"),
}
SAT_COUNTRIES = ["Qatar", "Kuwait", "Bahrain", "Oman"]
TUE_SERIES = ["rahul_goes_global", "airport_to_adventure"]

DAYPARTS = [
    "morning: lifestyle/coffee/gym/routine",
    "afternoon: food/travel/exploration",
    "evening: comedy/story/adventure",
    "night: interactive question or mini-story",
]


def main():
    lines = ["# Generated from STRATEGY/365_DAY_ENGINE.md — see CALENDAR.md", ""]
    sat_i = tue_i = 0
    for n in range(DAYS):
        d = START + datetime.timedelta(days=n)
        wd = d.weekday()
        region, country, pillar, theme, series = WEEKLY[wd]
        if wd == 5:
            country = SAT_COUNTRIES[sat_i % len(SAT_COUNTRIES)]
            sat_i += 1
        if wd == 1:
            series = TUE_SERIES[tue_i % len(TUE_SERIES)]
            tue_i += 1
        lines.append(f"- date: {d.isoformat()}")
        lines.append(f"  weekday: {d.strftime('%A')}")
        lines.append(f"  region: {region}")
        lines.append(f"  country: {country if country else 'null'}")
        lines.append(f"  pillar: {pillar}")
        lines.append(f"  theme: {theme}")
        lines.append(f"  series: {series}")
        lines.append("  platforms: [facebook, instagram, youtube]")
        lines.append("  videos: 2")
        lines.append("  photos: 2")
        lines.append("  trend_slot: true")
        lines.append("  dayparts:")
        for dp in DAYPARTS:
            lines.append(f"    - {dp}")
        if d.day == 1:
            lines.append("  monthly_focus: 4 new cities, 4 new food experiences, "
                         "4 new adventure settings, 2 new transport concepts, "
                         "1 connected mini-series")
        lines.append(f'  notes: ""')
        lines.append("")
    with open("calendar.yaml", "w") as f:
        f.write("\n".join(lines))
    print(f"wrote calendar.yaml: {DAYS} days from {START}")


if __name__ == "__main__":
    main()

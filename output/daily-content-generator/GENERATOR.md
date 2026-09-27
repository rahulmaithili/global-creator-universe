# Daily Content Generator (`DAILY PACK`)

The end-to-end daily pipeline — implements `GENERATOR/DAILY_WORKFLOW.md`'s
14 steps. One command in, one publishing-ready pack out.

## Pipeline

```
1. calendar-365/calendar.yaml → today's slot: region, pillar, series, platforms
2. CHARACTER/CHARACTER_LOCK.md + CHARACTER_SHEET.md → re-read (steps 1–2)
3. trend-engine        → live trend to adapt? (optional slot)
4. content-engine      → the idea: pillar + concept + combination axes
5. story-engine        → beats + continuity check (series) or single beat
6. video-engine        → video prompt(s)      ┐ run in parallel
   photo-engine        → photo prompt(s)      ┘
7. caption-engine      → caption + one CTA (caption rules, no false claims)
8. hashtag-engine      → hashtag set (broad/niche/location/brand mix)
9. platform adapters   → facebook / instagram / youtube packaging
10. episode-tracker     → full entry, status = prompted
11. human review        → approve → produce → post → status = posted
12. anti-duplicate-db   → concept recorded so the next run avoids duplication
```

## Daily minimum package (from STRATEGY/365_DAY_ENGINE.md)
- 2 short videos · 2 photos · 3 story concepts · 1 audience interaction
- 1 longer-form concept each week (YouTube)

## Daypart rotation
- Morning: lifestyle / coffee / gym / routine
- Afternoon: food / travel / exploration
- Evening: comedy / story / adventure
- Night: interactive question or mini-story

## Quality gate (from GENERATOR/DAILY_WORKFLOW.md)
Reject a concept if: character identity unclear · hook too slow · no reason
to keep watching · no payoff · generic CTA · duplicates a recent concept ·
misleading location claim.

## Rules
- Steps 4–10 never run if the dedup gate rejects the idea.
- Every step writes its output to the episode-tracker entry — the pack is
  auditable after the fact.
- Human review is mandatory before `produced`. The generator proposes;
  the creator disposes.

## Output
`daily-pack-YYYY-MM-DD.md`: the full pack (prompts, captions, hashtags, CTAs,
posting slots, checklist) + episode-tracker ids.

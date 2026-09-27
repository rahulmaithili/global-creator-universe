# Story Engine

Keeps series continuity: every episode advances the arc, callbacks land,
nothing contradicts earlier episodes.

## Reads
- The idea object (from content-engine)
- `data/series/series.yaml` — the 10 series + continuity devices
- `data/episode-tracker/` — previous episodes' concepts (the canon)

## Process
1. Load the series premise + all prior episode concepts.
2. Place this episode in the arc; define beats following the video formula
   (hook → setup → escalation → twist/payoff → comment-worthy closer).
3. Continuity check: no contradiction with canon; use at most one continuity
   device per episode (wardrobe progression, travel route, recurring friend /
   animal, previous-episode reference, audience decision, challenge streak,
   food ranking, running gag).
4. Standalone ideas → single-beat structure (hook → moment → payoff).
5. Continuity is deliberate — never flag it as duplication.

## Writes
- Episode-tracker: `concept` finalized + story beats stored.

## Output
Beat outline → video-engine (action/camera mapping) and caption-engine
(narrative voice).

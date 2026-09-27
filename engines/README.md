# ENGINES layer — specs grounded in the Brand Bible.

Seven engines. Each folder holds an `ENGINE.md` (reads / process / writes /
output) and the video/photo engines include a worked `example-output.md`.

| Engine | Produces |
|---|---|
| `content-engine` | The idea: pillar + concept + series slot (combination axes) |
| `video-engine` | Video prompt via `VIDEO/VIDEO_MASTER_PROMPT.md` + formula timing |
| `photo-engine` | Photo prompt via `PHOTO/PHOTO_MASTER_PROMPT.md` |
| `story-engine` | Beats + continuity from `data/series/series.yaml` |
| `trend-engine` | `TREND ADAPT` rebuilds (format → locked character → new story) |
| `caption-engine` | Caption + one CTA (caption rules, no false claims) |
| `hashtag-engine` | Hashtag set (broad/niche/location/brand mix) |

## Command routing (from GENERATOR/PROMPT_COMMANDS.md)

| Command | Engine sequence |
|---|---|
| `VIDEO: loc \| topic \| mood \| dur` | content → story → video → caption → hashtag → dedup → tracker |
| `PHOTO: loc \| topic \| mood` | content → photo → caption → hashtag → dedup → tracker |
| `NEXT VIDEO` / `NEXT PHOTO` | same as above, concept must not repeat the previous one |
| `REMAKE: concept` | content (variation matrix) → rebuild, materially different |
| `SERIES: topic \| episode n` | content (series slot) → story (continuity) → video/photo → … |
| `DAILY PACK: n videos + m photos` | full pipeline → platform adapters → calendar → registries |
| `TREND ADAPT: trend` | trend → content → story → video/photo → caption → hashtag |
| `GLOBAL: topic` | content (auto-pick USA/UK/Gulf/Global location) → … |
| `STORY: topic` | content → story → caption (story-first pack) |

Every sequence ends at the **dedup gate** and logs to the **episode tracker**.
No write-back = the run didn't happen. Every command inherits
`CHARACTER/CHARACTER_LOCK.md`; every pack follows
`GENERATOR/MASTER_OUTPUT_TEMPLATE.md`.

# Caption Engine

Writes the caption + CTA from the idea and story beats.

## Reads
- Idea object + story beats (from story-engine)
- `SOCIAL/CAPTION_HASHTAG_CTA_ENGINE.md` — caption rules + CTA rotation
- `data/hook-db/` — caption opening hook (may differ from the video hook)
- `data/cta-db/` — exactly ONE CTA, matched to the post's goal

## Process
1. Caption rules: concise, natural English — English only, no Hindi/Hinglish
   anywhere (LANGUAGE.md). Match the actual scene. Never make
   false claims about real-world experiences for AI-generated/fictional content.
2. First line must survive truncation (hook or payoff tease).
3. Body: 1–3 short lines in brand voice (approachable, curious, humorous).
4. Exactly one CTA from cta-db — never two asks, never bare "like/share/follow".
5. Length variants: full (Facebook/YouTube) and short (Instagram-first-lines).

## Writes
- Episode-tracker: final `caption` + `cta`.

## Output
`{caption_full, caption_short, cta_id}` → platform adapters place them.

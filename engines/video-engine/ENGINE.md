# Video Engine

Turns the idea into a **video generation prompt** using `VIDEO/VIDEO_MASTER_PROMPT.md`.

## Reads
- The idea object (from content-engine) + story beats (from story-engine)
- `VIDEO/VIDEO_MASTER_PROMPT.md` — the framework (SCENE / ACTIVITY / STORY /
  HOOK / ACTION / DIALOGUE / EMOTION / CAMERA / LIGHTING / ENVIRONMENT /
  ENDING / ENGAGEMENT)
- `VIDEO/VIDEO_CATEGORIES.md` — the 7 categories + topic lists
- `data/location-db/`, `data/outfit-db/`, `data/hook-db/` — resolved picks
- `CHARACTER/CHARACTER_LOCK.md` — the master sentence (goes FIRST in the prompt)

## Process
1. Open every prompt with the character master sentence:
   *"Use the locked main character from the approved reference image and
   preserve the exact recognizable facial identity and core appearance
   throughout the generation."*
2. Fill the master-prompt blocks: SCENE → ACTIVITY → STORY (one line) →
   HOOK → ACTION → DIALOGUE → EMOTION → CAMERA → LIGHTING → ENVIRONMENT →
   ENDING → ENGAGEMENT.
3. Apply the video formula timing: 0–2s hook · 2–8s setup · 8–20s escalation ·
   20–28s twist/payoff · final seconds = comment-worthy choice/question.
   (Longer videos expand the architecture — never filler.)
4. Dialogue rule: short, natural, globally understandable English. No speeches.
5. Append hard negatives: no watermark, no random logos, no unwanted text, no
   face swap, no character replacement, no deformed hands, no duplicate
   protagonist, realistic skin texture, believable physics.
6. Quality gate (`GENERATOR/DAILY_WORKFLOW.md`): reject if identity unclear,
   hook too slow, no reason to keep watching, no payoff, or misleading
   location claim.

## Writes
- Episode-tracker: `video_prompt_ref` + status → `prompted`.

## Output
Per `GENERATOR/MASTER_OUTPUT_TEMPLATE.md` (VIDEO section): Concept, Episode,
Location, Pillar, Hook, Duration, Generation Prompt, Dialogue, Ending, Title,
Caption, Hashtags, CTA. See `example-output.md` for a worked assembly.

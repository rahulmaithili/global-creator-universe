# Photo Engine

Turns the idea into a **photo generation prompt** using `PHOTO/PHOTO_MASTER_PROMPT.md`.

## Reads
- The idea object (from content-engine)
- `PHOTO/PHOTO_MASTER_PROMPT.md` — the framework (LOCATION / ACTIVITY /
  OUTFIT / MOOD / STORY MOMENT / BACKGROUND / CAMERA / LIGHT / DETAILS)
- `PHOTO/PHOTO_CATEGORIES.md` — Food, Travel, Adventure, Lifestyle, Luxury,
  Ships, Comedy, Wholesome, Seasonal
- `data/location-db/`, `data/outfit-db/` — resolved picks
- `CHARACTER/CHARACTER_LOCK.md` — the master sentence (goes FIRST in the prompt)

## Process
1. Open every prompt with the character master sentence.
2. Fill the blocks: LOCATION → ACTIVITY → OUTFIT → MOOD → STORY MOMENT →
   BACKGROUND → CAMERA (lens/angle/framing) → LIGHT → DETAILS.
3. Target feel: "a genuine premium lifestyle photograph, not a generic AI
   portrait" — natural pose, believable hands, strong composition, realistic
   depth of field.
4. Hard negatives: no watermark, no random text, no face replacement,
   no plastic skin, no cartoon look unless requested.
5. Quality gate: reject if identity unclear, composition weak, or location
   claim misleading.

## Writes
- Episode-tracker: `photo_prompt_ref` + status → `prompted`.

## Output
Per `GENERATOR/MASTER_OUTPUT_TEMPLATE.md` (PHOTO section): Concept, Location,
Mood, Image Prompt, Title, Caption, Hashtags, CTA. See `example-output.md`.

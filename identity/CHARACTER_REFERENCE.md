# Canonical Character Photo Reference

`character-reference.png` — the user-approved CHARACTER SHEET image
(front view, three-quarter view, side profile, full body, casual lifestyle).

## Rule (absolute)

Every image AND every video generated for the Global Creator persona MUST
use this file as the identity reference:

- `media.generate_image` → pass as `kind: image` in the prompt
- `media.generate_video` → pass as `kind: image` in the prompt
- Prompt text must instruct: preserve the exact recognizable facial
  identity, face shape, hair/beard, skin tone and build from the reference.

Text-only description does NOT hold the lock — the reference image is
mandatory. This was set after the user rejected a batch for wrong face
(2026-09-27).

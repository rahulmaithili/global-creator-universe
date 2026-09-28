# Video Production Skill — Global Creator Universe

The complete method for every video. Follow it exactly; no shortcuts.

## 1. Identity lock (absolute)
- `identity/character-reference.png` is mandatory as `kind: image` input for
  EVERY `media.generate_video` call. Text description alone never holds the lock.
- Every prompt must state: preserve the exact recognizable facial identity —
  same face shape, same short black swept-back hair, same trimmed beard and
  moustache shape, same medium-brown skin tone, same dark-brown eyes — in
  every frame. No face drift between shots.
- **Face brightness**: every prompt must include explicit face lighting —
  "bright soft key light on the character's face, face well-exposed and
  clearly visible, no harsh shadows across the face." The face must never
  render dark or muddy.

## 2. Language
- English only — all dialogue, voiceover, titles, captions (LANGUAGE.md).

## 3. Higgsfield shot method
1. **Build list first**: write the shot list before generating anything. Each
   shot = ONE action, ONE beat. 60s film ≈ 8 shots.
2. **One generation per shot**: never cram multiple beats into one clip
   (that causes the rushed, "everything at once" feel).
3. **Measured camera** per shot: Start → Path → State change → Duration → End.
4. **Match-cut continuity** between shots: same outfit (lock one outfit for the
   whole film), same screen direction, pose/time/material handoffs. Show the
   journey — never teleport the character between locations. Every object
   transfer (food, tickets, bags) must be visibly shown, nothing appears
   from nowhere.
5. **Grade lock**: identical cinematic grade language in every shot prompt
   (e.g. warm golden highlights, deep teal shadows, balanced skin tones,
   filmic contrast).
6. **Continuity audit**: after stitching, watch for outfit changes, face drift,
   teleport cuts, appearing objects. Fix by re-planning the beat, not by
   hiding it.

## 4. Audio (every video ships WITH sound)
- **Character speaks natively (no voiceover)**: the creator talks to camera
  like a real vlog. Every shot is directed WITH NATIVE AUDIO and carries his
  exact spoken line in quotes, e.g. "he looks into the lens and speaks aloud
  the words '...' with clear audible speech and natural lip sync matching the
  words". Never add TTS voiceover — the dialogue comes from the generation
  itself. Keep every spoken line short enough to fit its shot. Verify each
  clip has an audio stream before stitching.
- **No TTS voiceover**: dialogue is generated natively in each shot by the
  video model — never layered on top with TTS. The locked voice
  `avocado_v2:chip` is retired for this format. The user records nothing.
- **SFX matched to scene**: e.g. Tube rumble + door hiss + announcements for
  subway; traffic + footsteps for street; crowd + sizzle for food market.
  One-shots placed at exact timestamps, beds looped under segments.
- **Music**: no-copyright background track only, matched to the mood
  (upbeat for adventure, warm for lifestyle). Mixed LOW under voice
  (around -20 dB relative), never competing with dialogue.
- **Mix levels**: voice full and clear → SFX supporting → music bed lowest.

## 5. Relatability + engagement (no-skip craft)
- 0–2s visual hook, open loop or bold claim up front.
- Stakes and a visible decision point in the middle.
- Payoff in the final third, then a comment-bait question.
- Relatable premise: a situation the public has lived (wrong train, bad
  coffee name, missed bus). Real emotion, no fake overacting.

## 6. Stitch recipe
```bash
ffmpeg -y -i shot1.mp4 -i shot2.mp4 ... \
 -filter_complex "[0:v]trim=0:7,setpts=PTS-STARTPTS[v0];...;[v0][v1]...concat=n=N:v=1:a=0[out]" \
 -map "[out]" -c:v libx264 -pix_fmt yuv420p -movflags +faststart out.mp4
```
- Use `xfade` (with `settb=AVTB` on both inputs) for time-passage dissolves.
- Mux final audio: `[video][voice][sfx][music]amix` then `-c:v copy -c:a aac`.

## 7. Delivery
- Final file → `~/workspace/your_files/gcu-videos/`
- Upload to the Drive folder "Global Creator Universe".
- Record the episode in `data/episode-tracker/` with status `posted`.

## 8. Audience
- USA target only: concepts, locations, food, humor, and references must be
  USA-focused (American cities, diners, road trips, everyday American life).
  Titles, captions, and hashtags are written for a USA audience.

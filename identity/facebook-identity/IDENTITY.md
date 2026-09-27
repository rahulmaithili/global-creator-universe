# Facebook Identity

Public identity for the Facebook creator profile of the Global Creator
Universe persona. Core character identity lives in `CHARACTER/` (male,
late-20s/early-30s, short black hair, trimmed beard, medium-brown skin —
fictional creator persona "Rahul"); this file is the Facebook-specific layer.

## 1. Profile setup
- [ ] Creator profile (not personal timeline) created
- [ ] Username/handle locked — same as Instagram + YouTube for consistency
- [ ] Category: Digital creator
- [ ] Contact email + location set

## 2. Bio (≤150 chars, max 3 emoji)
Line 1: who + what — "Rahul 🌍 | Same face, new city every day"
Line 2: rhythm — "New episode daily 🎬"
Line 3: CTA — "Where should I go next? 👇"

## 3. Profile photo rules
- Character face, centered, high contrast — readable at 40px
- Same crop as Instagram/YouTube avatar (one avatar everywhere)
- No text in the photo; no seasonal variants without updating all platforms

## 4. Cover rules
- 820×312 safe area; key art on the left (mobile crops the right)
- Shows: character + pillars (food/travel/comedy visual shorthand) + "New episode daily"
- Refresh quarterly or per season — never mid-series

## 5. Audience targeting
Primary USA · Secondary UK · Expansion UAE, Saudi Arabia, Qatar, Kuwait,
Bahrain, Oman + global English-speaking audiences.
- Page language: simple English (global default); selected Arabic subtitles
  for Gulf-targeted posts
- Region feel comes from `data/location-db` + `calendar.yaml` rotation —
  one page, global audience; never a misleading location claim
- The persona is a fictional creator character — no fabricated residence,
  education, employment, or official identity (CHARACTER/CHARACTER_LOCK.md)

## 6. Posting system
- Daily slot from `output/calendar-365/calendar.yaml` (Reels-first, 2 videos + 2 photos/day)
- `DAILY PACK` order: Reel → page post (photo) → story reshare
- First 60 minutes: reply to every comment (engagement window)
- Episode-tracker `post_url` filled within 1h of posting
- Weekly: review performance notes → feed back into hook-db / pillars

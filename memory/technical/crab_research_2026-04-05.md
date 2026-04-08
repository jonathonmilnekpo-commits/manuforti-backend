---
date: 2026-04-05
topic: technical
tags: ['technical']
---

# Crab Workflow Research - 2025-04-05
**Focus:** YouTube automation, multi-agent pipelines, thumbnail automation, content repurposing

---

## 1. Multi-Agent Content Pipeline Stack

The winning approach is treating YouTube like an assembly line — specialized AI agents handle each stage.

**Recommended Stack:**
| Stage | Tool | Purpose | API? |
|-------|------|---------|------|
| Research | vidIQ | SEO & trending topics | ✅ |
| Scripting | ChatGPT/GPT-4o | Structured scripts + JSON output | ✅ |
| Voiceover | ElevenLabs | Natural narration | ✅ |
| Visuals | Midjourney/Leonardo | B-roll, backgrounds | ✅ |
| Video Assembly | **Shotstack** | Automated editing via API | ✅ |
| Publishing | YouTube Data API | Upload + metadata | ✅ |

**Key Insight:** 83% of creators now use AI in their workflow (Digiday 2025). The differentiator isn't using AI — it's connecting tools via API so they talk to each other without manual export/import.

**GitHub Resource:** `darkzOGx/youtube-automation-agent` — Fully autonomous Python pipeline using Gemini/OpenAI to generate, optimize & publish videos 24/7.

---

## 2. Content Repurposing (Long → Shorts)

**Top Tool: OpusClip**
- **What it does:** AI analyzes long videos, identifies viral-worthy moments, auto-clips into Shorts/Reels/TikToks
- **Key features:** 
  - ClipAnything model works on any genre (gaming, vlogs, interviews)
  - ReframeAnything auto-centers moving subjects for vertical format
  - AI captions, brand templates, team workspaces
- **API available:** Yes — can integrate into CMS/workflow automation
- **Used by:** 16M+ creators including Mark Rober, Logan Paul, Dhar Mann Studios

**Alternatives:**
- **quso.ai** (formerly vidyo.ai) — AI clips + social scheduling + AI avatars
- **Wisecut** — Auto-highlight detection for quick clips
- **Canva AI Shorts Maker** — Good for simpler repurposing

**Workflow Integration:** OpusClip API → auto-generate 5-10 shorts per long video → schedule via Buffer/Later → track performance

---

## 3. Thumbnail Generation Automation

**Top Tools:**

**Thumber.app**
- AI thumbnail generator with face swap capability
- Upload face photo + game/product screenshots → AI composes
- Text-to-thumbnail: Describe video idea, get 3 variations
- **API available:** RESTful API for programmatic generation
- Free tier: 1 thumbnail

**Pikzels**
- Designed specifically for viral-looking YouTube thumbnails
- Remembers brand settings for consistent visual identity
- Good for batch-generating variations

**BananaThumbnail**
- A/B testing built-in
- Predictive performance analysis (CTR estimation)
- 4K output optimized for YouTube algorithm

**Workflow:** Script/title → AI generates 3 thumbnail options → A/B test → winner auto-uploaded with video

---

## Actionable Next Steps

1. **Immediate:** Set up Shotstack API + test automated video assembly with existing Crab voiceovers
2. **Week 1:** Integrate OpusClip for shorts — upload 3 long videos, extract 15 shorts, track performance
3. **Week 2:** Connect Thumber API for automated thumbnail generation on upload

---

## Links

- OpusClip: https://www.opus.pro/
- Shotstack: https://shotstack.io/
- Thumber: https://thumber.app/
- GitHub youtube-automation-agent: https://github.com/darkzOGx/youtube-automation-agent
- OpusClip API docs: https://www.opus.pro/api

---
*Research completed: 2026-04-05 04:00 CET*

---
date: 2026-03-29
topic: technical
tags: ['technical']
---

# Crab Workflow Research — YouTube Automation & Content Pipeline

**Date:** 2025-03-29 (CET)  
**Focus:** 3 actionable automation stacks — Video Editing, Thumbnails, Multi-Agent Pipelines

---

## 1. Video Editing & Repurposing Automation

### Shotstack API — Best for Full-Stack Video Assembly
- **Link:** https://shotstack.io/learn/best-ai-tools-for-youtube-automation/
- **What it does:** Cloud video editing API — add captions, stitch clips, apply templates, burn subtitles
- **Key feature:** Auto-captioning + template-based rendering via REST API
- **Cost:** Free tier available, pay-as-you-scale
- **Crab use case:** Auto-generate captioned clips from long-form content

### FFmpeg Micro — Best for n8n/Make Integration
- **Link:** https://www.ffmpeg-micro.com/
- **What it does:** Turn long-form → shorts/reels/quote clips via HTTP API
- **Key feature:** No self-hosting — add to n8n/Zapier as HTTP node
- **Operations:** Crop 9:16, add captions, stitch, resize, filters
- **Crab use case:** Plug into existing n8n workflows for batch clip generation

### FFmpeg MCP Server — Best for Agent-Driven Editing
- **Link:** https://skywork.ai/skypage/en/ffmpeg-video-manipulation-ai-editing/1980157318084022272
- **What it does:** MCP server that lets AI agents command video edits conversationally
- **Key feature:** "Create 3 clips: 5:30-6:00, 15:10-15:45, 32:00-32:20"
- **Crab use case:** Agent-driven workflows where OpenClaw agents edit videos directly

---

## 2. Thumbnail Generation Automation

### Pikzels — Best Dedicated Thumbnail AI
- **Link:** https://pikzels.com/
- **What it does:** AI thumbnail generator with A/B testing + title optimization
- **Key feature:** Full toolkit to create, test & iterate thumbnails that get clicked
- **Crab use case:** Generate face-aware thumbnails programmatically

### n8n + FLUX.1 + Apify Workflow — Best for DIY Pipeline
- **Link:** https://n8n.io/workflows/4504-automate-viral-youtube-titles-and-thumbnails-creation-flux1-apify/
- **What it does:** Automated viral thumbnail + title generation pipeline
- **Stack:** FLUX.1 (image gen) + Apify (data extraction) + n8n (orchestration)
- **Crab use case:** Fully automated title/thumbnail generation from video content

### DynaPictures API — Best for Bulk/Template Thumbnails
- **Link:** https://dynapictures.com/auto-generate/youtube-thumbnails-via-api
- **What it does:** Template-based thumbnail generation via API
- **Key feature:** Dynamic text overlay, bulk generation
- **Crab use case:** News-style thumbnails with dynamic headlines

---

## 3. Multi-Agent Content Pipelines (n8n-Based)

### YouTube Shorts Automation — End-to-End
- **Link:** https://n8n.io/workflows/2941-youtube-shorts-automation-tool/
- **Stack:** OpenAI (script) → ElevenLabs (voice) → Cloudinary/Replicate (media) → Creatomate (assembly)
- **Key feature:** Full pipeline: text → voiceover → visuals → rendered short
- **Crab use case:** Autonomous short-form content production

### Viral Shorts Research Agent
- **Link:** https://www.reddit.com/r/n8n/comments/1q21vf1/i_built_an_n8n_automation-that-researches-viral/
- **What it does:** Researches viral YouTube shorts overnight, scores virality potential
- **Stack:** n8n + Gemini + Google Sheets
- **Crab use case:** Trend detection + content opportunity identification

### AI Metadata Generation Workflow
- **Link:** https://n8n.io/workflows/3900-automated-youtube-video-scheduling-and-ai-metadata-generation/
- **What it does:** Auto-schedule + generate AI titles, descriptions, tags
- **Stack:** YouTube API + Apify (transcripts) + LLM for SEO metadata
- **Crab use case:** Upload → auto-optimize metadata → publish

---

## Quick Implementation Stack for Crab

| Stage | Tool | Integration |
|-------|------|-------------|
| Long-form → Clips | FFmpeg Micro | n8n HTTP node |
| Captions/Subtitles | Shotstack API | Direct API or n8n |
| Thumbnails | Pikzels or FLUX.1 + n8n | API or workflow |
| Voiceover | ElevenLabs | Already in TOOLS.md |
| Orchestration | n8n | Self-host or cloud |
| Upload/Metadata | YouTube Data API | n8n native node |

---

## Next Steps

1. **Set up n8n instance** (self-hosted or cloud) as the orchestration layer
2. **Test FFmpeg Micro** for clip generation with existing Crab content
3. **Evaluate Pikzels** vs. rolling own FLUX.1 thumbnail pipeline
4. **Connect ElevenLabs** (already configured) into the n8n workflow

---

**Research completed:** 2026-03-29  
**Token estimate:** ~1.2K tokens

# Pipeline Wiring Summary

## ✅ What's Wired Up

| Stage | Model | Integration | Status |
|-------|-------|-------------|--------|
| 1 | Qwen3 8B | Ollama local API | ✅ Wired (needs `ollama` installed) |
| 2 | Kimi K2.5 | OpenClaw Gateway HTTP | ✅ Wired (needs gateway running) |
| 3 | Sonnet 4.6 | OpenClaw Gateway HTTP | ✅ Wired (needs gateway running) |

## 🚀 To Go Live

### 1. Install Ollama (Stage 1 - Local/Free)
```bash
brew install ollama
ollama pull qwen3:8b
ollama serve  # Keep running
```

### 2. Ensure OpenClaw Gateway Running (Stages 2 & 3)
```bash
openclaw gateway start
openclaw gateway status  # Should show "running"
```

### 3. Install Dependencies
```bash
cd ~/.openclaw/workspace/pipeline
pip install -r requirements.txt
```

### 4. Run Pipeline
```bash
python3 run_pipeline.py --supplier "Boskalis"
```

## 📊 Expected Costs (When Live)

| Stage | Model | Cost | Notes |
|-------|-------|------|-------|
| 1 | Qwen3 8B | $0.00 | Local inference |
| 2 | Kimi K2.5 | ~$0.004 | Scoring + filtering |
| 3 | Sonnet 4.6 | ~$0.045 | Final report |
| **Total** | | **~$0.05** | vs $0.15 Sonnet-only (67% savings) |

## 🔄 Fallback Behaviour

If APIs aren't available, each stage gracefully falls back to mock data:
- Stage 1: Mock extraction with warnings
- Stage 2: Mock scoring with FLAG_FOR_REVIEW
- Stage 3: Mock generation with warnings

This lets you test the pipeline structure without burning API credits.

## 📁 Files Created

```
~/.openclaw/workspace/pipeline/
├── 01_extract/extract.py      # Qwen3 extraction (Ollama)
├── 02_score/score.py          # Kimi scoring (OpenClaw)
├── 03_generate/generate.py    # Sonnet generation (OpenClaw)
├── run_pipeline.py            # Orchestrator
├── requirements.txt           # Python deps
├── README.md                  # Full documentation
└── QUICKSTART.md              # This file
```

## 🎯 Next Steps After Wiring

1. **Add web scraping** → Integrate `requests/BeautifulSoup` to fetch real URLs
2. **Add Brave Search** → Auto-discover sources from search queries
3. **Connect PPTX generator** → Feed JSON output into `generate_boskalis_v15.py`
4. **Add caching** → Skip re-processing if output already exists

## 🔧 Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Qwen3 8B  │────▶│  Kimi K2.5  │────▶│ Sonnet 4.6  │
│   (Local)   │     │   (Cheap)   │     │  (Premium)  │
│  Extraction │     │   Scoring   │     │  Generation │
│   $0.000    │     │   $0.004    │     │   $0.045    │
└─────────────┘     └─────────────┘     └─────────────┘
      │                     │                   │
      ▼                     ▼                   ▼
01_extract/output/    02_score/output/   03_generate/output/
  raw_data.json        scored_data.json     final_report.json
```

**Total pipeline cost: ~$0.05 per report** (3x cheaper than Sonnet-only)

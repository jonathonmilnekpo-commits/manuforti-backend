# 3-Stage Supplier Analysis Pipeline

Cost-cascaded AI pipeline for Product 1 supplier intelligence reports.

## Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   STAGE 1   │───▶│   STAGE 2   │───▶│   STAGE 3   │
│  Extraction │    │   Scoring   │    │  Generation │
│  Qwen3 8B   │    │  Kimi K2.5  │    │ Sonnet 4.6  │
│   (Local)   │    │   (Cheap)   │    │  (Premium)  │
│    $0.00    │    │    $0.004   │    │   $0.045    │
└─────────────┘    └─────────────┘    └─────────────┘
```

**Total cost per report: ~$0.05** (vs ~$0.15 for Sonnet-only)

## Quick Start

```bash
# Run full pipeline
cd ~/.openclaw/workspace/pipeline
python3 run_pipeline.py --supplier "Boskalis"

# With custom sources
python3 run_pipeline.py --supplier "SupplierName" \
  --urls "https://supplier.com/investors" \
         "https://linkedin.com/company/supplier"

# Skip stages (if already run)
python3 run_pipeline.py --supplier "Boskalis" --skip-extract --skip-score
```

## Stage Details

### Stage 1: Extraction (`01_extract/extract.py`)
- **Model:** Qwen3 8B (local via Ollama/LM Studio)
- **Cost:** $0.00
- **Purpose:** Bulk scrape websites, extract raw facts
- **Output:** `{supplier}_extracted.json`

**Production Setup:**
```python
# Replace mock with actual Ollama call
import ollama
response = ollama.chat(
    model="qwen3:8b",
    messages=[{"role": "user", "content": extraction_prompt}]
)
```

### Stage 2: Scoring (`02_score/score.py`)
- **Model:** Kimi K2.5
- **Cost:** ~$0.004
- **Purpose:** Quality scoring, fact filtering, gap identification
- **Output:** `{supplier}_scored.json`

**Production Setup:**
```python
# Via OpenClaw sessions_spawn or direct API
result = sessions_spawn(
    task=scoring_prompt,
    model="kimi",
    mode="run"
)
```

### Stage 3: Generation (`03_generate/generate.py`)
- **Model:** Sonnet 4.6
- **Cost:** ~$0.045
- **Purpose:** Client-ready insights, v15 deck generation
- **Output:** `{supplier}_report.json` + PPTX deck

**Production Setup:**
```python
# Via OpenClaw with model override
result = sessions_spawn(
    task=generation_prompt,
    model="sonnet",
    mode="run"
)
```

## Data Flow

```
URLs → [Extract] → raw_facts.json ─┐
                                   ├──▶ [Score] → scored_facts.json ──▶ [Generate] → report.pptx
Search results ────────────────────┘
```

## Cost Comparison

| Approach | Cost/Report | Quality | Speed |
|----------|-------------|---------|-------|
| Sonnet-only | $0.15 | ⭐⭐⭐ | Fast |
| **3-Stage Pipeline** | **$0.05** | ⭐⭐⭐ | **Fast** |
| Kimi-only | $0.02 | ⭐⭐ | Fast |
| Qwen3-only | $0.00 | ⭐⭐ | Slow (local) |

## Directory Structure

```
pipeline/
├── 01_extract/
│   ├── extract.py          # Qwen3 extraction
│   └── output/
│       └── boskalis_extracted.json
├── 02_score/
│   ├── score.py            # Kimi scoring
│   └── output/
│       └── boskalis_scored.json
├── 03_generate/
│   ├── generate.py         # Sonnet generation
│   └── output/
│       ├── boskalis_report.json
│       └── boskalis_Product1_v15_Final.pptx
├── shared/                 # Common utilities
├── run_pipeline.py         # Orchestrator
├── README.md
└── pipeline_runs.jsonl     # Execution log
```

## Extending the Pipeline

### Add web scraping
```python
# In 01_extract/extract.py
import requests
from bs4 import BeautifulSoup

def scrape_url(url: str) -> str:
    response = requests.get(url, headers={"User-Agent": "..."})
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()
```

### Add search integration
```python
# In 01_extract/extract.py
from brave_search import search

search_results = search(f"{supplier} financial results 2024")
urls = [r['url'] for r in search_results['web']['results'][:5]]
```

### Parallel processing
```python
# In run_pipeline.py
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(run_pipeline, s) for s in suppliers]
```

## Monitoring

Check `pipeline_runs.jsonl` for execution history:

```bash
# View recent runs
tail -5 pipeline_runs.jsonl | jq '.'

# Calculate average cost
jq -s 'map(.total_cost) | add / length' pipeline_runs.jsonl
```

## Setup

### 1. Install Ollama (for Qwen3 local inference)

```bash
brew install ollama
ollama pull qwen3:8b
ollama serve  # Keep running in background
```

Test: `ollama run qwen3:8b "Hello"`

### 2. Configure OpenClaw (for Kimi + Sonnet)

Ensure your OpenClaw gateway is running and has API keys configured:

```bash
# Start gateway
openclaw gateway start

# Verify status
openclaw gateway status

# Check available models
openclaw models list
```

Required API keys in `~/.openclaw/config.yaml`:
- `moonshot` (Kimi K2.5)
- `anthropic` (Claude Sonnet 4.6)

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Test the pipeline

```bash
python3 run_pipeline.py --supplier "TestCorp"
```

Expected: Runs through all 3 stages with mock fallbacks (until APIs configured).

## Usage

```bash
# Run full pipeline
cd ~/.openclaw/workspace/pipeline
python3 run_pipeline.py --supplier "Boskalis"

# With custom sources
python3 run_pipeline.py --supplier "SupplierName" \
  --urls "https://supplier.com/investors" \
         "https://linkedin.com/company/supplier"

# Skip stages (if already run)
python3 run_pipeline.py --supplier "Boskalis" --skip-extract --skip-score
```

## Production Deployment

### Option A: Local Mode (all models local)
- Replace Kimi with local Qwen3 32B or Llama 3.3
- Replace Sonnet with local Qwen3 32B
- **Cost: $0.00** (slower, requires GPU)

### Option B: Hybrid Mode (current setup)
- Qwen3 8B local (free)
- Kimi via API (cheap)
- Sonnet via API (premium)
- **Cost: ~$0.05/report**

### Option C: Cloud Mode (all API)
- Kimi for extraction
- Kimi for scoring  
- Sonnet for generation
- **Cost: ~$0.06/report**

## Troubleshooting

### "Ollama not installed" warning
Stage 1 falls back to mock extraction. To enable real local inference:
```bash
brew install ollama
ollama pull qwen3:8b
# In separate terminal: ollama serve
```

### "API call failed" for Kimi/Sonnet
The pipeline falls back to mock scoring/generation. To enable real APIs:
1. Ensure `openclaw gateway status` shows "running"
2. Check `openclaw models list` includes `kimi` and `sonnet`
3. Verify API keys are configured in `~/.openclaw/config.yaml`

### Gateway connection refused
The pipeline tries `http://localhost:8080` by default. Override with:
```bash
export OPENCLAW_GATEWAY_URL="http://your-gateway:8080"
python3 run_pipeline.py --supplier "TestCorp"
```

## Next Steps

1. **Add web scraping** - integrate `requests/BeautifulSoup` into Stage 1
2. **Add Brave Search** - auto-discover source URLs
3. **Connect PPTX generator** - feed JSON to `generate_boskalis_v15.py`
4. **Add error retry** - handle API failures gracefully
5. **Add caching** - avoid re-processing same supplier

# Product 1 Skills Suite

Three integrated skills for supplier intelligence report generation.

## Quick Start

```bash
# 1. Extract financial data
python3 skills/financial-data-extractor/scripts/extract.py \
  --source /path/to/annual_report.pdf \
  --output financials.json

# 2. Generate v15 PPTX
python3 skills/product-1-generator/scripts/generate.py \
  financials.json \
  SupplierName_Product1_v15.pptx

# 3. Validate output
python3 skills/product-1-validator/scripts/validate.py \
  SupplierName_Product1_v15.pptx
```

## Skills Overview

### 1. financial-data-extractor
Extracts standardized financial metrics from documents.

**Required Metrics:**
- Revenue (latest + YoY %)
- EBITDA (amount + margin %)
- Net Profit
- 3-Year CAGR
- Order Book
- **Gross Debt** (mandatory)
- **Net Cash/Debt** (mandatory)
- **Debt/EBITDA** (mandatory)

**Usage:**
```bash
python3 skills/financial-data-extractor/scripts/extract.py \
  --source https://boskalis.com/investors \
  --format html \
  --supplier "Boskalis" \
  --output boskalis_financials.json
```

### 2. product-1-generator
Creates 9-slide v15 PPTX from structured JSON.

**Input:** Structured JSON with financials, risks, ESG data
**Output:** Product 1 v15 PPTX with all charts and styling

**Usage:**
```bash
python3 skills/product-1-generator/scripts/generate.py \
  input_data.json \
  output.pptx
```

### 3. product-1-validator
Validates PPTX compliance with locked v15 template.

**Checks:**
- 9-slide structure
- Required financial metrics
- Wood Mackenzie styling
- Branding consistency

**Usage:**
```bash
python3 skills/product-1-validator/scripts/validate.py deck.pptx
```

**Output:**
```json
{
  "valid": true,
  "score": 95,
  "errors": [],
  "warnings": []
}
```

## Integration with Pipeline

These skills integrate with the 3-stage pipeline:

```
Stage 1 (Qwen3) → Stage 2 (Kimi) → Stage 3 (Sonnet)
       ↓               ↓                  ↓
   Raw data      Structured JSON    PPTX + Validation
       ↓               ↓                  ↓
   extractor    →   generator    →   validator
```

## V15 Template Structure (LOCKED)

| Slide | Content | Key Elements |
|-------|---------|--------------|
| 1 | Title | Supplier name, sector tags, stats |
| 2 | Executive Summary | Risk gauge, snapshot panel |
| 3 | Recommendation | Amber/green banner, conditions |
| 4 | Supplier Profile | Org structure, leadership |
| 5 | Financial Health | Dual-axis chart + metrics panel |
| 6 | Market Position | Horizontal bar vs peers |
| 7 | Ops + Risk | Timeline + 2x2 matrix |
| 8 | Commercial | Radar + lollipop charts |
| 9 | ESG | E/S/G columns, overall rating |

## Dependencies

Install required packages:

```bash
python3 -m pip install python-pptx matplotlib requests beautifulsoup4 --break-system-packages
```

## Directory Structure

```
skills/
├── financial-data-extractor/
│   ├── SKILL.md
│   └── scripts/
│       └── extract.py
├── product-1-generator/
│   ├── SKILL.md
│   └── scripts/
│       └── generate.py
└── product-1-validator/
    ├── SKILL.md
    └── scripts/
        └── validate.py
```

## Workflow Example

```bash
# Complete workflow for new supplier
cd ~/.openclaw/workspace

# Extract
python3 skills/financial-data-extractor/scripts/extract.py \
  --source "https://example.com/annual-report.pdf" \
  --format pdf \
  --supplier "DemoCorp" \
  --output /tmp/democorp_fin.json

# Enhance with additional data (risks, ESG, etc.)
# ... edit /tmp/democorp_fin.json to add missing fields ...

# Generate
python3 skills/product-1-generator/scripts/generate.py \
  /tmp/democorp_fin.json \
  /tmp/DemoCorp_Product1_v15.pptx

# Validate
python3 skills/product-1-validator/scripts/validate.py \
  /tmp/DemoCorp_Product1_v15.pptx
```

## Cost per Report

With the 3-stage pipeline + skills:

| Step | Model | Cost |
|------|-------|------|
| Extraction | Qwen3 8B (local) | $0.000 |
| Scoring | Kimi K2.5 | $0.004 |
| Generation | Sonnet 4.6 | $0.045 |
| Validation | Local | $0.000 |
| **Total** | | **~$0.05** |

## Next Steps

1. Test skills with real supplier data
2. Integrate into 3-stage pipeline
3. Add visual chart generation (matplotlib)
4. Build web scraping automation

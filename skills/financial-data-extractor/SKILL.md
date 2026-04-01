---
name: financial-data-extractor
description: Extracts standardized financial metrics from supplier annual reports, earnings calls, and investor presentations. Use when sourcing financial data for Product 1 reports. Targets specific metrics: revenue, EBITDA, net profit, gross debt, net cash, debt/EBITDA ratio, order book, and 3-year CAGR. Handles PDFs, HTML tables, and image-based tables with OCR fallback. Outputs standardized JSON ready for Product 1 generator pipeline.
---

# Financial Data Extractor

Extracts financial metrics from supplier documents for Product 1 reports.

## Target Metrics

These 8 metrics are **required** for Product 1 Slide 5:

| Metric | Example | Source |
|--------|---------|--------|
| Revenue (latest) | "$2.4B" or "EUR 2.1B" | Income statement |
| Revenue YoY | "+12%" | Annual report |
| EBITDA | "$320M" | Income statement |
| EBITDA Margin | "13.3%" | Calculated or stated |
| Net Profit | "$180M" | Bottom line |
| 3-Year CAGR | "8.5%" | Growth calculation |
| Order Book | "$1.2B" | Backlog/forward orders |
| **Gross Debt** | "$450M" | Balance sheet |
| **Net Cash/Debt** | "+$85M" or "-$120M" | Cash minus debt |
| **Debt/EBITDA** | "1.4x" | Leverage ratio |

## Supported Formats

- PDF annual reports
- HTML investor pages
- Excel/CSV financial tables
- Image-based tables (OCR)

## Usage

```bash
# From PDF
python3 ~/.openclaw/workspace/skills/financial-data-extractor/scripts/extract.py \
  --source /path/to/annual_report.pdf \
  --format pdf \
  --output financials.json

# From URL
python3 ~/.openclaw/workspace/skills/financial-data-extractor/scripts/extract.py \
  --source https://supplier.com/investors \
  --format html \
  --output financials.json
```

## Output Format

```json
{
  "supplier": "Extracted from doc or provided",
  "fiscal_year": "2024",
  "currency": "EUR",
  "revenue": "4.4B",
  "revenue_yoy": "+3%",
  "ebitda": "520M",
  "ebitda_margin": "11.8%",
  "net_profit": "280M",
  "cagr_3yr": "6.2%",
  "order_book": "5.8B",
  "gross_debt": "890M",
  "net_cash": "+518M",
  "debt_ebitda": "1.7x",
  "extraction_confidence": 0.87,
  "source_url": "...",
  "extraction_date": "2026-03-02"
}
```

## Confidence Scoring

Each extraction gets a confidence score (0-1):
- 0.9-1.0: Explicit statement in financial table
- 0.7-0.9: Found in text with clear context
- 0.5-0.7: OCR extraction, requires verification
- <0.5: Missing or unclear — flag for manual review

## Pattern Matching

The extractor uses regex patterns for:
- Currency amounts (USD, EUR, GBP, NOK)
- Percentage changes
- Ratio formats (x, :1, times)
- Fiscal year indicators

See scripts/extract.py for pattern definitions.

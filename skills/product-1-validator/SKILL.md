---
name: product-1-validator
description: Validates Product 1 supplier analysis reports against the locked v15 template structure. Use when checking PPTX files for compliance with the 9-slide format, required metrics (debt/EBITDA, net cash, revenue), color palette (navy/steel blue), and Wood Mackenzie styling. Ensures all mandatory slides are present, validates financial data completeness, checks branding consistency, and flags deviations from the canonical v15 format.
---

# Product 1 Validator

Validates Product 1 v15 supplier analysis decks against the locked template structure.

## What It Validates

### Structure (9 Slides - MANDATORY)
1. Title slide with supplier name, sector tags, key stats
2. Executive Summary with **risk gauge** and supplier snapshot
3. Recommendation with amber/green banner, conditions, risk summary
4. Supplier Profile with org structure and leadership
5. Financial Health with **dual-axis chart** + metrics panel (must include debt/EBITDA, net cash)
6. Market Position with **horizontal bar chart** vs peers
7. Operational Capability + Risk Assessment with **timeline** + **2x2 risk matrix**
8. Commercial Intelligence + Peer Risk with **radar chart** + **peer risk comparison**
9. ESG Assessment with **E/S/G columns** and overall rating

### Graphics Validation (NEW)
Each slide is checked for required visual elements:

| Slide | Required Graphics | Detection Method |
|-------|-------------------|------------------|
| 2 | Risk gauge dial | Image detection + text patterns (LOW/MEDIUM/HIGH) |
| 5 | Dual-axis chart | Chart type detection (combo/bar+line) |
| 6 | Horizontal bar chart | Chart type + competitor text |
| 7 | Timeline + Risk matrix | Group/table detection + year markers |
| 8 | Radar chart + Peer risk | Chart type + benchmark/peer text |
| 9 | ESG columns | Table detection or E/S/G text patterns |

### Required Financial Metrics (Slide 5)
- Revenue (latest year + YoY %)
- EBITDA (amount + margin %)
- Net Profit
- Revenue CAGR (3yr)
- Order Book
- **Gross Debt** (mandatory)
- **Net Cash / Net Debt** (mandatory)
- **Debt/EBITDA ratio** (mandatory)

### Branding Standards
- Colors: Navy (#002147), Steel Blue (#2B6CB0), Mid-Grey (#718096)
- RAG only for status indicators (no green on Recommendation slide)
- Footer: "Powered by Manu Forti Intelligence"
- Source line: "Source: Manu Forti Intelligence | Confidential | [Month Year]"
- Minimum font: 14pt body, 16pt titles, 11pt footnotes

### Layout Standards
- Financial chart: 7.5" wide
- Ops+Risk timeline: 7.0", risk matrix: 5.5"
- Source line: y=7.15, size 8pt
- Company logo: top-right on every slide

## Usage

```bash
python3 ~/.openclaw/workspace/skills/product-1-validator/scripts/validate.py /path/to/deck.pptx
```

## Validation Output

```json
{
  "valid": false,
  "errors": [
    "Slide 5 missing: Debt/EBITDA ratio",
    "Slide 3: Green used on recommendation banner (should be amber)",
    "Slide 7: Risk matrix missing"
  ],
  "warnings": [
    "Slide 2: Risk gauge not detected",
    "Source line format incorrect on slides 2,4,8"
  ],
  "score": 85
}
```

## Rules Reference

See references/v15_spec.md for complete specification.

## Exit Codes

- 0: Valid (score >= 90)
- 1: Invalid (score < 90)
- 2: Critical structure missing

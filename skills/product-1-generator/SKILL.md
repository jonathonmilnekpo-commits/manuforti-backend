---
name: product-1-generator
description: Generates Product 1 v16 supplier analysis reports — 9-slide executive-ready PPTX decks for procurement supplier evaluation. Use when user requests "supplier analysis", "vendor evaluation", "due diligence report", "procurement assessment", or needs a comprehensive 9-slide report on a specific company. Creates risk gauges, financial charts, market position analysis, risk matrices, and ESG assessments with Wood Mackenzie styling. Requires supplier financial data, risk profile, and competitive intelligence as input.
---

# Product 1 Generator

Generates Product 1 v15 supplier analysis decks from structured JSON.

## Input Format

```json
{
  "supplier": "Supplier Name",
  "sector": "Industry Sector",
  "financials": {
    "revenue_2024": "$2.4B",
    "revenue_yoy": "+12%",
    "ebitda": "$320M",
    "ebitda_margin": "13.3%",
    "net_profit": "$180M",
    "cagr_3yr": "8.5%",
    "order_book": "$1.2B",
    "gross_debt": "$450M",
    "net_cash": "+$85M",
    "debt_ebitda": "1.4x"
  },
  "executive_summary": {
    "overall_risk": "MEDIUM",
    "risk_score": 42,
    "key_insight": "..."
  },
  "recommendation": {
    "verdict": "APPROVE with ESG CONDITIONS",
    "conditions": ["..."],
    "risk_summary": {"financial": "LOW", "operational": "LOW", "geopolitical": "MEDIUM", "esg": "MEDIUM"}
  },
  "profile": {
    "description": "...",
    "leadership": [{"name": "...", "role": "CEO", "tenure": "10 years"}],
    "headquarters": "...",
    "employees": "..."
  },
  "market_position": {
    "rank": 2,
    "competitors": [{"name": "...", "revenue": "$3.1B"}],
    "advantages": ["..."]
  },
  "risks": [
    {"category": "Financial", "description": "...", "impact": "Medium", "probability": "Low"}
  ],
  "esg": {
    "environmental": "MEDIUM",
    "social": "LOW",
    "governance": "LOW",
    "overall": "MEDIUM",
    "controversies": []
  }
}
```

## Usage

```bash
python3 ~/.openclaw/workspace/skills/product-1-generator/scripts/generate.py input.json output.pptx
```

## Output

Generates a 9-slide PPTX with:
- All required charts (matplotlib-based)
- Wood Mackenzie styling
- Proper branding and source lines
- Locked v15 layout structure

## Dependencies

- python-pptx
- matplotlib
- numpy

## Visual Generation

The skill generates these chart types:
- Financial Health: Dual-axis bar + line (revenue + EBITDA)
- Market Position: Horizontal bar chart
- Risk Matrix: 2x2 impact vs probability scatter
- Commercial Radar: 6-dimension spider chart
- Peer Risk: Lollipop comparison chart

See scripts/generate_visuals.py for chart generation.

## Quality Control

**ALWAYS run validation before declaring a report complete:**

```bash
python3 ~/.openclaw/workspace/skills/product-1-generator/scripts/validate.py <output.pptx>
```

### Validation Checks

| Check | Requirement | Critical? |
|-------|-------------|-----------|
| File size | >500 KB (indicates embedded charts) | ✅ Yes |
| Slide count | Exactly 9 slides | ✅ Yes |
| Chart count | 5+ images detected | ✅ Yes |
| Placeholder text | None allowed | ✅ Yes |
| Source lines | Present on all slides | ⚠️ Warn |
| Content density | >2 shapes per slide | ✅ Yes |

### Pre-Delivery Checklist

Before uploading to Google Drive:
- [ ] Run `validate.py` and confirm "ALL CHECKS PASSED"
- [ ] Open PPTX and visually inspect all 9 slides
- [ ] Verify risk gauge shows correct score
- [ ] Check all right-side panels present (slides 3-8)
- [ ] Confirm Manu Forti logo on every slide
- [ ] Verify no competitor names cross-contaminated

### Common Failures

| Issue | Cause | Fix |
|-------|-------|-----|
| "File size too small" | Charts not embedded | Regenerate at higher DPI (200+) |
| "Only X images found" | Missing chart files | Check visuals folder, regenerate |
| "Placeholder text" | Incomplete template | Search and replace all [Enter...] |
| "Wrong slide count" | Template error | Rebuild from scratch |

## Version

v16 - March 2026
- Updated to v16 template (9 charts + all panels)
- Added QC validation script
- Improved trigger phrases for better skill detection

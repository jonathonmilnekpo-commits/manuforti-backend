# Product 1 v15 - Master Template Documentation

Based on: `Boskalis_Product1_v15_Final-1.pptx`

## Template Files Created

1. **`v15_template_master.json`** - Complete technical specification
2. **`v15_template_placeholder.json`** - Fill-in-the-blanks template

## Quick Start

Use the placeholder template for new suppliers:

```json
{
  "template": "Product 1 v15",
  "supplier": "Supplier Name",
  "sector": "Sector | Sub-sector",
  "stats": "$X Revenue | Y Employees | Z Countries",
  ...
}
```

Then generate:
```bash
python3 skills/product-1-generator/scripts/generate.py \
  input.json \
  output.pptx
```

## Color Scheme (LOCKED)

| Color | Hex | Usage |
|-------|-----|-------|
| **Navy** | `#002147` | Primary bars, headers, key elements |
| **Steel Blue** | `#2B6CB0` | Lines, accents, insight callouts |
| **Mid Grey** | `#718096` | Competitors, secondary elements |
| **Green** | `#48BB78` | Positive indicators, LOW risk |
| **Amber** | `#D69E2E` | MEDIUM risk, conditions |
| **Red** | `#E53E3E` | HIGH risk, negative indicators |
| **Background** | `#FFFFFF` | Slide background |
| **Text Primary** | `#1A202C` | Body text |
| **Text Secondary** | `#4A5568` | Supporting text |

## Typography Standards (LOCKED)

| Element | Size | Color | Weight |
|---------|------|-------|--------|
| Slide Title | 28pt | Navy | Bold |
| Section Header | 20pt | Steel Blue | Bold |
| Body Text | 14pt | Text Primary | Regular |
| Source Line | 8pt | Mid Grey | Regular |

**Minimum font sizes:**
- Body: 14pt (never smaller)
- Source: 8pt
- Chart labels: 11pt

## 9-Slide Structure (LOCKED)

### Slide 1: Title
**Required fields:**
- `supplier_name` - Full company name
- `sector_tags` - Industry descriptors (e.g., "Marine Infrastructure | Offshore Energy")
- `key_stats_line` - Revenue, employees, countries, fleet size
- `report_date` - Month Year
- `confidentiality` - "Confidential | Manu Forti Intelligence"

**Branding:**
- Logo: Top-right, white rounded backing
- No source line on title slide

---

### Slide 2: Executive Summary
**Required fields:**
- `supplier_name` - For context
- `overall_risk` - LOW, MEDIUM, or HIGH
- `risk_score` - 0-100 numeric score
- `key_insight` - Single sentence summary (action title format)
- `risk_factors` - Array of 3-5 key risks
- `supplier_snapshot` - Key facts panel

**Visual elements:**
- Risk gauge dial (circular indicator)
- Supplier snapshot panel (right side)

**Positioning:**
- Source line: y=7.15 inches from top
- Source line size: 8pt

---

### Slide 3: Recommendation
**Required fields:**
- `verdict` - APPROVE / APPROVE with CONDITIONS / DECLINE
- `verdict_color` - Follow rules below
- `conditions` - Array of 4-6 conditions
- `risk_summary` - Financial, Operational, Geopolitical, ESG ratings
- `next_steps` - Action items

**CRITICAL RULES:**
- **NEVER use green on this slide**
- APPROVE with CONDITIONS → Amber banner
- LOW risk items → Navy (not green)
- MEDIUM risk → Amber
- HIGH risk → Red

**Visual elements:**
- Colored banner box (top)
- Risk summary strip (bottom)
- Conditions list (center)

---

### Slide 4: Supplier Profile
**Required fields:**
- `company_overview` - 2-3 paragraph description
- `leadership` - Array of {name, role, tenure}
- `org_structure` - Parent → Subsidiary relationships
- `headquarters` - City, Country
- `employee_count` - Number
- `global_footprint` - Countries/regions

**Visual elements:**
- Org structure diagram (hierarchy tree)
- Leadership panel with photos (if available)

---

### Slide 5: Financial Health
**Required fields (8 metrics - MANDATORY):**

| Metric | Example | Source |
|--------|---------|--------|
| revenue_2024 | "$380.2B" | Income statement |
| revenue_yoy | "+4.2%" | Annual report |
| ebitda | "$68.4B" | Income statement |
| ebitda_margin | "18.0%" | Calculated |
| net_profit | "$28.5B" | Bottom line |
| cagr_3yr | "8.2%" | 3-year calculation |
| order_book | "$45.2B" | Backlog |
| **gross_debt** | "$82.1B" | Balance sheet |
| **net_cash** | "-$42.8B" | Cash minus debt |
| **debt_ebitda** | "1.2x" | Leverage ratio |

**Chart specifications:**
- Type: Dual-axis (bars + line)
- Width: 7.5 inches
- Height: 4.55 inches
- Bar color: Navy (#002147)
- Line color: Steel Blue (#2B6CB0)

**Visual elements:**
- Left: Dual-axis chart (revenue bars + EBITDA line)
- Right: Metrics panel (8 key numbers)
- Trend annotation below chart

**Highlighting:**
- Net Cash positive → Green
- Debt/EBITDA < 2x → Green
- Low leverage signals → Highlighted

---

### Slide 6: Market Position
**Required fields:**
- `market_rank` - Position (1, 2, 3, etc.)
- `competitors` - Array of {name, revenue}
- `competitive_advantages` - Array of 3-5 strengths
- `market_share_data` - Percentages (optional)

**Chart specifications:**
- Type: Horizontal bar chart
- Subject supplier: Navy bar
- Competitors: Mid Grey bars
- Include revenue values on bars

---

### Slide 7: Operational Capability & Risk
**Required fields:**
- `investment_timeline` - Array of {year, milestone, investment}
- `risk_matrix_data` - Array of {risk, impact, probability, category}
- `risk_table` - Structured risk data
- `capabilities` - Key operational strengths

**Visual elements:**
- Top-left: Investment timeline (horizontal)
- Top-right: 2x2 Risk Matrix (Impact vs Probability)
- Bottom: Risk summary table + Capability list

**Layout specifications:**
- Timeline width: 7.0 inches
- Risk matrix width: 5.5 inches
- Bottom panels: Aligned at same y-coordinate

**Risk Matrix Axes:**
- X-axis: Probability (Low → High)
- Y-axis: Impact (Low → High)
- Bubbles positioned by risk assessment

---

### Slide 8: Commercial Intelligence
**Required fields:**
- `radar_chart_data` - 6 dimensions vs competitor
- `peer_risk_data` - Risk scores for comparison
- `commercial_terms` - Payment terms, contract structure
- `negotiation_notes` - Key negotiation insights
- `key_watch_points` - Red flags to monitor

**Chart specifications:**
- Left: Radar/spider chart (6 dimensions)
  - Dimensions: Price, Lead Time, Quality, Technical, Supply Chain, Service
  - Subject: Navy fill
  - Competitor: Steel Blue outline
- Right: Lollipop chart (peer risk comparison)
  - Subject dot: Navy
  - Peer dots: Mid Grey

---

### Slide 9: ESG Assessment
**Required fields:**
- `environmental_rating` - LOW, MEDIUM, or HIGH
- `social_rating` - LOW, MEDIUM, or HIGH
- `governance_rating` - LOW, MEDIUM, or HIGH
- `overall_esg_rating` - Composite rating
- `controversies` - Array of negative news/legal issues
- `esg_conditions` - 6 conditions for approval

**Visual elements:**
- Three columns: Environmental | Social | Governance
- Each column: Rating badge + bullet points
- Bottom: Controversy screening panel
- Overall rating banner (top-right)

**CRITICAL RULE:**
- ESG MEDIUM elevates overall rating to MEDIUM
- Even if Financial/Operational are LOW

---

## Risk Rating Logic

### Composite Calculation
```
Overall Risk = f(Financial, Operational, Geopolitical, ESG)
```

### ESG Elevation Rule
| Financial | Operational | Geopolitical | ESG | **OVERALL** |
|-----------|-------------|--------------|-----|-------------|
| LOW | LOW | LOW | **MEDIUM** | **MEDIUM** |
| LOW | LOW | MEDIUM | MEDIUM | MEDIUM |
| HIGH | HIGH | HIGH | HIGH | HIGH |

**Example:**
- Boskalis: Financial LOW + Operational LOW + Geopolitical MEDIUM + ESG MEDIUM = **MEDIUM (42/100)**
- Changes recommendation from "APPROVE" → "APPROVE with ESG Conditions"

---

## Design Standards Summary

### Action Titles
Every slide header sub-line must state the KEY INSIGHT as a complete sentence, not just a topic label.

**Bad:** "Financial Performance"
**Good:** "Revenue growth accelerating with improving margins"

### Chart Style
- Minimal gridlines (very light grey)
- No top/right spines
- Direct data labels on all data points
- Consistent color coding

### Insight Callouts (Bloomberg Style)
- Left accent border: Steel Blue (#2B6CB0)
- Background: Pale blue (#EBF4FF)
- **Never use colored boxes**

### Logo Placement
- Position: Top-right of every slide
- Backing: White rounded rectangle
- Coordinates: x=10.92", y=0.06"
- Size: 2.26" × 0.87"

### Source Lines
**Format:**
```
Source: Manu Forti Intelligence | Confidential | February 2026
```

**Footer:**
```
Powered by Manu Forti Intelligence
```

**NEVER use:** "AI-Powered Procurement Intelligence"

---

## JSON Template Usage

### Complete Data Example
```json
{
  "supplier": "Shell plc",
  "sector": "Integrated Energy | Oil & Gas | Renewables",
  "stats": "$380B Revenue (2024) | 90,000 Employees | 70+ Countries",
  "financials": {
    "revenue_2024": "$380.2B",
    "revenue_yoy": "+4.2%",
    "ebitda": "$68.4B",
    "ebitda_margin": "18.0%",
    "net_profit": "$28.5B",
    "cagr_3yr": "8.2%",
    "order_book": "$45.2B",
    "gross_debt": "$82.1B",
    "net_cash": "-$42.8B",
    "debt_ebitda": "1.2x",
    "trend": "Strong cash generation; debt reduction priority"
  },
  "executive_summary": {
    "overall_risk": "LOW",
    "risk_score": 32,
    "key_insight": "Shell demonstrates exceptional financial strength with conservative leverage and strong market position.",
    "risk_factors": [
      "Energy transition execution",
      "Geopolitical exposure",
      "Carbon pricing pressures"
    ]
  },
  "recommendation": {
    "verdict": "APPROVE",
    "conditions": [
      "Standard payment terms: Net-30 days",
      "Parent company guarantee for major contracts",
      "Quarterly business reviews",
      "ESG reporting aligned with standards"
    ],
    "risk_summary": {
      "financial": "LOW",
      "operational": "LOW",
      "geopolitical": "MEDIUM",
      "esg": "MEDIUM"
    }
  },
  ...
}
```

---

## Validation Checklist

Before generating, verify:

- [ ] All 9 slides have required fields
- [ ] All 8 financial metrics present
- [ ] Debt/EBITDA ratio included
- [ ] Risk ratings follow elevation rules
- [ ] No green used on Recommendation slide
- [ ] Source line format correct
- [ ] Logo specified for every slide
- [ ] Minimum font sizes respected

Run validator:
```bash
python3 skills/product-1-validator/scripts/validate.py output.pptx
```

---

## Version Control

**Template Version:** v15 CANONICAL
**Last Updated:** March 2, 2026
**Based On:** Boskalis_Product1_v15_Final-1.pptx
**Locked By:** Jonathon Milne

**DO NOT MODIFY** without explicit approval.

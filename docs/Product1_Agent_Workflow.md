# Product 1 Agent Workflow
**Version:** 1.0  
**Date:** March 7, 2026  
**Status:** Active

---

## Overview

This document defines the standardized workflow for generating Product 1 supplier analysis reports. It ensures consistency, quality, and efficiency across all reports.

## Agent Roles

| Agent | Role | Responsibility |
|-------|------|----------------|
| **Researcher** | Data Gathering | Financials, risks, ESG, competitors, leadership |
| **Analyst** | Scoring & Analysis | Apply risk framework, calculate scores, draft recommendation |
| **Venture** | Report Generation | Create visuals, build PPTX, apply branding |
| **Validator** | Quality Assurance | Check structure, graphics, metrics, branding compliance |
| **Vetter** | Security & Final Review | Security check, final sanitization |

## Phase 1: Intake & Scope (15 min)

### 1.1 Request Validation
- [ ] Verify supplier name and jurisdiction
- [ ] Check for sanctions/restricted entities
- [ ] Confirm data sources are accessible
- [ ] Determine service tier (Standard/Premium/Enterprise)

### 1.2 Data Requirements Checklist
- [ ] Financial statements (3 years minimum)
- [ ] Company website and annual reports
- [ ] ESG ratings and certifications
- [ ] Competitor intelligence
- [ ] News and controversy screening

## Phase 2: Research (45-90 min)

### 2.1 Financial Data (Researcher)
Gather for Slide 5:
- Revenue (latest year + YoY %)
- EBITDA (amount + margin %)
- Net Profit
- Revenue CAGR (3-year)
- Order Book/Backlog
- Gross Debt
- Net Cash/Net Debt position
- Debt/EBITDA ratio
- Interest Coverage ratio

**Sources:** Annual reports, Bloomberg, D&B, credit ratings

### 2.2 Risk Intelligence (Researcher)
Gather for Slide 7:
- Operational risks (capacity, quality, supply chain)
- Geopolitical risks (country, regulatory, sanctions)
- Financial risks (liquidity, leverage, profitability)
- ESG risks (environmental, social, governance)

**Minimum 6 risks required for risk matrix**

### 2.3 ESG Data (Researcher)
Gather for Slide 9:
- Environmental: ISO 14001, carbon footprint, EcoVadis
- Social: CoC, labor rights, H&S, diversity
- Governance: Ownership structure, board independence, transparency
- Controversies: Negative media, litigation, sanctions

### 2.4 Competitive Intelligence (Researcher)
Gather for Slides 6 & 8:
- 4-6 named competitors with revenue/shipments
- Market positioning
- Technology comparison
- Peer risk scores

## Phase 3: Risk Scoring (30 min)

### 3.1 Scoring Framework

| Pillar | Weight | Scale | Data Sources |
|--------|--------|-------|--------------|
| Financial | 35% | 0-100 | Annual reports, credit ratings |
| Operational | 25% | 0-100 | Site visits, certifications |
| Geopolitical | 20% | 0-100 | BMI Fitch, sanctions lists |
| ESG | 15% | 0-100 | EcoVadis, CDP, media screening |
| Commercial | 5% | 0-100 | RFQ analysis, benchmarks |

### 3.2 Rating Bands
- **0-33:** LOW (Green) — Acceptable risk
- **34-66:** MEDIUM (Amber) — Enhanced due diligence
- **67-100:** HIGH (Red) — Mitigation mandatory

### 3.3 Calculation
```
Overall Score = (Financial × 0.35) + 
                (Operational × 0.25) + 
                (Geopolitical × 0.20) + 
                (ESG × 0.15) + 
                (Commercial × 0.05)
```

### 3.4 Special Rules
- **ESG Elevation:** If ESG = MEDIUM and all others LOW → Overall = MEDIUM
- **ESG Override:** If any ESG sub-pillar = HIGH → Overall ESG = HIGH

## Phase 4: Report Generation (60-90 min)

### 4.1 Visual Generation (Venture)
Generate 9 chart files:
1. Risk gauge (Slide 2)
2. Org chart (Slide 4)
3. Financial dual-axis chart (Slide 5)
4. Market position horizontal bar (Slide 6)
5. Timeline (Slide 7)
6. Risk matrix (Slide 7)
7. Radar benchmarking (Slide 8)
8. Peer risk comparison (Slide 8)
9. ESG assessment (Slide 9)

### 4.2 PPTX Assembly (Venture)
Build 9 slides:
1. Title — Supplier name, tagline, key stats
2. Executive Summary — Risk gauge + supplier snapshot + "What This Means for Buyers"
3. Recommendation — Verdict + conditions + escalation triggers
4. Supplier Profile — Org structure + overview + leadership
5. Financial Health — Dual-axis chart + 10 metrics panel (incl. CAGR, Interest Coverage)
6. Market Position — Horizontal bar chart + competitive context
7. Ops + Risk — Timeline + risk matrix + risk table
8. Commercial — Radar chart + peer risk + negotiation leverage
9. ESG — 3-column assessment + controversy screening

### 4.3 V16 Quality Checklist
- [ ] 3-Year CAGR calculated and displayed
- [ ] Interest Coverage in financial metrics
- [ ] Facility photo placeholders in timeline
- [ ] Risk matrix labels 10pt minimum
- [ ] Negotiation leverage assessment included
- [ ] "What This Means for Buyers" in Executive Summary
- [ ] Escalation triggers in Recommendation
- [ ] Trend arrows in peer risk comparison

## Phase 5: Validation (15-30 min)

### 5.1 Quality Gates (Validator)

| Check | Critical? | Penalty |
|-------|-----------|---------|
| 9 slides present | YES | -20 points |
| Risk gauge on Slide 2 | YES | -8 points |
| Dual-axis chart on Slide 5 | YES | -8 points |
| Horizontal bar chart on Slide 6 | YES | -8 points |
| Timeline + risk matrix on Slide 7 | YES | -8 points each |
| Radar chart on Slide 8 | YES | -8 points |
| ESG columns on Slide 9 | YES | -8 points |
| All 10 financial metrics on Slide 5 | YES | -5 points each |
| Manu Forti branding | NO | -5 points |
| Source line format | NO | -3 points |

**PASS:** Score ≥ 90, no critical errors

### 5.2 Cross-Contamination Check
- [ ] No hydrogen references (unless hydrogen company)
- [ ] No references to other suppliers (Nel, T1, etc.)
- [ ] Correct company name throughout
- [ ] Correct industry context

## Phase 6: Delivery (5 min)

### 6.1 Final Steps
- [ ] Run Quality Gate
- [ ] Vetter security review
- [ ] Generate Excel scoring spreadsheet
- [ ] Save to workspace
- [ ] Upload to Google Drive
- [ ] Share with stakeholders

### 6.2 Deliverables
1. `[Supplier]_Product1_v[X].pptx` — Full 9-slide report
2. `[Supplier]_Product1_v[X]_Scoring.xlsx` — Risk scoring framework
3. Summary document with key findings

---

## Service Tiers

| Tier | Trigger | Turnaround | Price |
|------|---------|------------|-------|
| **Standard** | Automated request | 24 hours | €99 |
| **Premium** | >€10M contract or expert review | 48 hours | €149 |
| **Enterprise** | >€50M contract or complex assessment | 5-7 days | €499+ |

---

## Tools & Resources

- **Generator Script:** `generate_[supplier]_v16.py`
- **Visuals Folder:** `[supplier]_v16_visuals/`
- **Template:** `product1_v16_canonical_template.json`
- **Reference:** `Boskalis_Product1_v15_Final.pptx`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-07 | Initial workflow documentation |

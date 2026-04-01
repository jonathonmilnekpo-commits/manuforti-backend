# Product 1 Risk Scoring Framework & Process Definition
**Version:** 1.0  
**Date:** 6 March 2026  
**Status:** DRAFT — Pending Jonathon Approval

---

## 1. RISK SCORING FRAMEWORK

### 1.1 Risk Categories (5 Pillars)

| Pillar | Weight | Description | Data Sources |
|--------|--------|-------------|--------------|
| **Financial** | 35% | Liquidity, profitability, leverage, cash flow stability | Annual reports, credit ratings, D&B, Bloomberg |
| **Operational** | 25% | Delivery capability, capacity, quality control, supply chain resilience | Site visits, certifications, order book analysis |
| **Geopolitical** | 20% | Country risk, regulatory exposure, trade restrictions, sanctions | BMI Fitch, sanctions lists, trade policy |
| **ESG** | 15% | Environmental, Social, Governance compliance and controversies | EcoVadis, CDP, media screening, ISO certs |
| **Commercial** | 5% | Contract terms, pricing volatility, negotiation leverage | RFQ analysis, market benchmarks |

**Total: 100%**

### 1.2 Scoring Scale (0-100 per Pillar)

Each pillar scored 0-100, then weighted into overall score.

| Score | Rating | Color | Interpretation |
|-------|--------|-------|----------------|
| 0-33 | LOW | 🟢 Green | Acceptable risk, standard monitoring |
| 34-66 | MEDIUM | 🟡 Amber | Elevated risk, enhanced due diligence required |
| 67-100 | HIGH | 🔴 Red | Critical risk, mitigation mandatory or reject |

### 1.3 Pillar Scoring Sub-Criteria

#### Financial (35% weight)

| Metric | Threshold LOW (0-33) | Threshold MEDIUM (34-66) | Threshold HIGH (67-100) | Data Point |
|--------|----------------------|--------------------------|-------------------------|------------|
| Debt/EBITDA | < 2.0x | 2.0x – 4.0x | > 4.0x | Slide 5 metric |
| Net Cash Position | Positive | Neutral / Small debt | Significant net debt | Slide 5 metric |
| EBITDA Margin | > 12% | 5% – 12% | < 5% or negative | Slide 5 metric |
| Revenue CAGR (3yr) | > 5% | 0% – 5% | Negative | Slide 5 metric |
| Interest Coverage | > 3.0x | 1.5x – 3.0x | < 1.5x | Credit report |

**Financial Score Calculation:**
```
Financial = (Debt/EBITDA_score × 0.30) + 
            (NetCash_score × 0.25) + 
            (EBITDAMargin_score × 0.25) + 
            (CAGR_score × 0.15) + 
            (InterestCoverage_score × 0.05)
```

#### Operational (25% weight)

| Factor | LOW (0-33) | MEDIUM (34-66) | HIGH (67-100) | Source |
|--------|------------|----------------|---------------|--------|
| Order Book Coverage | > 18 months | 12-18 months | < 12 months | Slide 5 metric |
| Capacity Utilization | 70-85% | 85-95% or < 70% | > 95% or < 50% | Researcher estimate |
| Quality Certifications | ISO 9001 + industry cert | ISO 9001 only | No certifications | Slide 7/Research |
| Supply Chain Concentration | Diversified (>3 regions) | Moderate (2-3 regions) | Concentrated (1 region) | Researcher analysis |
| Delivery Track Record | > 95% on-time | 85-95% on-time | < 85% on-time | Reference checks |

#### Geopolitical (20% weight)

| Factor | LOW (0-33) | MEDIUM (34-66) | HIGH (67-100) | Source |
|--------|------------|----------------|---------------|--------|
| Country Risk Rating | BMI/Fitch: Low Risk | BMI/Fitch: Medium Risk | BMI/Fitch: High Risk | BMI Fitch reports |
| Regulatory Stability | Stable, predictable | Some uncertainty | High volatility, changing | Researcher analysis |
| Trade/Sanctions Exposure | No exposure | Minor indirect exposure | Direct sanctions risk | Sanctions lists |
| Currency Volatility | < 10% annual | 10-25% annual | > 25% annual | FX data |

#### ESG (15% weight)

| Factor | LOW (0-33) | MEDIUM (34-66) | HIGH (67-100) | Source |
|--------|------------|----------------|---------------|--------|
| Environmental (E) | EcoVadis A/B, ISO 14001 | EcoVadis C, no major violations | EcoVadis D/E, violations | Slide 9 |
| Social (S) | Strong CoC, no controversies | Minor controversies resolved | Active litigation, labor issues | Slide 9 + screening |
| Governance (G) | Transparent ownership, no sanctions | Complex structure, minor issues | Sanctions, corruption cases | Slide 9 + screening |

**ESG Override Rule:** If ANY ESG pillar is HIGH (controversy/litigation), overall ESG = HIGH regardless of other scores.

#### Commercial (5% weight)

| Factor | LOW (0-33) | MEDIUM (34-66) | HIGH (67-100) | Source |
|--------|------------|----------------|---------------|--------|
| Pricing Volatility | Stable, predictable | Moderate fluctuations | Highly volatile | RFQ analysis |
| Contract Flexibility | Standard terms acceptable | Some negotiation needed | Aggressive terms, high risk | Slide 8 notes |
| Market Position | Leader / strong #2 | Mid-tier | Weak, struggling | Slide 6 analysis |

### 1.4 Overall Risk Score Calculation

```
Overall Score = (Financial × 0.35) + 
                (Operational × 0.25) + 
                (Geopolitical × 0.20) + 
                (ESG × 0.15) + 
                (Commercial × 0.05)
```

**ESG Elevation Rule:** If ESG = MEDIUM (34-66) and all other pillars are LOW, overall rating elevates to MEDIUM. This reflects ESG's strategic importance.

**Final Rating Mapping:**
- 0-33: **LOW** → "APPROVE"
- 34-66: **MEDIUM** → "APPROVE with CONDITIONS"
- 67-100: **HIGH** → "REJECT" or "APPROVE with SIGNIFICANT MITIGATION"

---

## 2. PROCESS DEFINITION

### 2.1 Service Tiers

| Tier | Trigger | What's Included | Turnaround | Price |
|------|---------|-----------------|------------|-------|
| **Standard** | Automated request via web form or API | AI-generated report, all 9 slides, standard data sources | 24 hours | €99 |
| **Premium** | High-value supplier (>$10M contract) OR client requests expert review | Standard + expert analyst review + 30-min consultation call | 48 hours | €149 |
| **Enterprise** | Strategic supplier (>$50M contract) OR complex multi-site assessment | Premium + primary research (interviews) + custom deep-dive on 2 pillars + dedicated account manager | 5-7 days | €499+ (custom quote) |

### 2.2 Agent Workflow (All Tiers)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SUPPLIER REQUEST RECEIVED                        │
│                    (Web form / API / Email / Manual)                     │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. VETTER (🔒) — Security & Scope Validation                            │
│    • Check data sources are accessible and compliant                    │
│    • Validate supplier name and jurisdiction                            │
│    • Flag any sanctions or restricted entities                          │
│    • Output: Approved/Blocked with reason                               │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 2. RESEARCHER (🔍) — Data Gathering                                     │
│    • Financial data (3-year history, all 10 metrics)                    │
│    • Risk intelligence (operational, geopolitical, ESG)                 │
│    • Competitive landscape (5-6 peers)                                  │
│    • Leadership and ownership structure                                 │
│    • ESG certifications and controversies                               │
│    • Output: Structured JSON data file                                  │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 3. ANALYST (📊) — Scoring & Analysis                                    │
│    • Apply scoring framework to all 5 pillars                           │
│    • Calculate weighted overall score                                   │
│    • Determine risk rating (LOW/MEDIUM/HIGH)                            │
│    • Draft recommendation and conditions                                │
│    • Output: Scored data + recommendation JSON                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 4. VENTURE (🚀) — Report Generation                                     │
│    • Generate all 9 visuals (charts, diagrams, risk gauge)              │
│    • Build PPTX deck per v15 template                                   │
│    • Apply branding and source lines                                    │
│    • Output: Draft Product 1 PPTX                                       │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 5. VALIDATOR (✅) — Quality Assurance                                   │
│    • Run Quality Gate checklist (all 9 slides, all graphics)            │
│    • Verify all 10 financial metrics present                            │
│    • Check branding compliance                                          │
│    • Validate scoring calculations                                      │
│    • Output: PASS / FAIL with feedback                                  │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼ FAIL                          ▼ PASS
        ┌───────────────────────┐       ┌───────────────────────┐
        │ Return to Analyst     │       │ Proceed to Vetter     │
        │ for corrections       │       │ Final Review          │
        └───────────────────────┘       └───────────────────────┘
                                                    │
                                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 6. VETTER (🔒) — Final Security Sanitization                            │
│    • Remove any sensitive source attribution if needed                  │
│    • Final compliance check                                             │
│    • Output: Cleared for delivery                                       │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 7. DELIVERY                                                             │
│    • Send PPTX + Executive Summary PDF                                  │
│    • Include scoring spreadsheet (Excel)                                │
│    • Log to CRM / delivery tracking                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Tier-Specific Additions

**Premium Tier Additions (after Step 5):**
- Expert Analyst (human or senior AI) reviews scoring rationale
- 30-minute consultation call scheduled
- Custom insights added to Slide 3 (Recommendation)

**Enterprise Tier Additions (after Step 5):**
- Primary research: 2-3 supplier interviews conducted
- Deep-dive analysis on 2 selected pillars (client choice)
- Custom appendix slides (up to 3 additional)
- Dedicated account manager assigned

### 2.4 Quality Gates

| Gate | Check | Owner | Pass Criteria |
|------|-------|-------|---------------|
| G1 | Data completeness | Researcher | All 10 financial metrics + 5+ risks + ESG data |
| G2 | Scoring logic | Analyst | All 5 pillars scored 0-100, weights sum to 100% |
| G3 | Visual generation | Venture | All 9 chart files created, no errors |
| G4 | Deck structure | Venture | 9 slides, correct dimensions, all logos |
| G5 | Final validation | Validator | Score ≥ 90, no critical errors (see below) |

**Critical Errors (Auto-Fail G5):**
- Missing risk gauge on Slide 2
- Missing any of 8 required charts
- Missing >2 financial metrics
- Wrong supplier name anywhere
- Missing Manu Forti logo on any slide

---

## 3. EXCEL SCORING SPREADSHEET FORMAT

### 3.1 File Structure

**Filename:** `[SupplierName]_Product1_Scoring_YYYYMMDD.xlsx`

**Worksheets:**
1. **Summary** — Overall score, rating, recommendation
2. **Financial** — Detailed financial scoring
3. **Operational** — Operational risk scoring
4. **Geopolitical** — Country and regulatory scoring
5. **ESG** — Environmental, Social, Governance scoring
6. **Commercial** — Contract and market scoring
7. **Raw Data** — All input data from Researcher

### 3.2 Worksheet: Summary

| Cell | Content | Formula/Value |
|------|---------|---------------|
| A1 | **PRODUCT 1 RISK SCORING SUMMARY** | Header |
| A3 | Supplier Name | [Input] |
| A4 | Analysis Date | [Date] |
| A5 | Analyst | [Agent/Name] |
| A6 | Validation Status | [Pending/Pass/Fail] |
| A8 | **OVERALL RISK SCORE** | Weighted average |
| B8 | =SUMPRODUCT(B14:B18,C14:C18)/100 | 0-100 |
| A9 | **OVERALL RATING** | =IF(B8<=33,"LOW",IF(B8<=66,"MEDIUM","HIGH")) |
| A10 | **RECOMMENDATION** | =IF(B8<=33,"APPROVE",IF(B8<=66,"APPROVE with CONDITIONS","REJECT")) |
| A12 | **PILLAR BREAKDOWN** | Header |
| A14 | Financial | 35% |
| A15 | Operational | 25% |
| A16 | Geopolitical | 20% |
| A17 | ESG | 15% |
| A18 | Commercial | 5% |
| B14:B18 | Pillar Scores (0-100) | [From other sheets] |
| C14:C18 | Weights | 35, 25, 20, 15, 5 |
| D14:D18 | Weighted Contribution | =B14*C14/100 etc. |
| A20 | **CONDITIONS (if MEDIUM/HIGH)** | Header |
| A21+ | List of conditions | [From Analyst] |

### 3.3 Worksheet: Financial (Example)

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **FINANCIAL RISK SCORING** | | | | | | |
| 3 | Metric | Raw Value | Score (0-100) | Weight | Weighted Score | Thresholds | Notes |
| 4 | Debt/EBITDA | 1.4x | =IF(C4<2,20,IF(C4<4,50,85)) | 30% | =D4*E4 | <2=LOW, 2-4=MED, >4=HIGH | From annual report |
| 5 | Net Cash Position | +$85M | =IF(C5>0,15,IF(C5>-50,45,80)) | 25% | =D5*E5 | Positive=LOW, -50M=Med | Slide 5 metric |
| 6 | EBITDA Margin | 13.3% | =IF(C6>12,20,IF(C6>5,50,85)) | 25% | =D6*E6 | >12%=LOW, 5-12%=MED | Slide 5 metric |
| 7 | Revenue CAGR | 8.5% | =IF(C7>5,15,IF(C7>0,40,75)) | 15% | =D7*E7 | >5%=LOW, 0-5%=MED | 3-year |
| 8 | Interest Coverage | 4.2x | =IF(C8>3,10,IF(C8>1.5,40,70)) | 5% | =D8*E8 | >3x=LOW, 1.5-3x=MED | Credit report |
| 10 | **FINANCIAL PILLAR SCORE** | | | **100%** | =SUM(F4:F8) | | |
| 11 | **RATING** | | =IF(F10<=33,"LOW",IF(F10<=66,"MEDIUM","HIGH")) | | | | |

### 3.4 Worksheet: Raw Data

| Field | Value | Source | Date Sourced |
|-------|-------|--------|--------------|
| revenue_2024 | $2.4B | Annual Report 2024 | 2026-03-06 |
| revenue_yoy | +12% | Annual Report 2024 | 2026-03-06 |
| ebitda | $320M | Annual Report 2024 | 2026-03-06 |
| ... | ... | ... | ... |
| esg_environmental | MEDIUM | EcoVadis rating | 2026-03-06 |
| controversy_1 | Both ENDS litigation | Web search | 2026-03-06 |

---

## 4. IMPLEMENTATION CHECKLIST

- [ ] Jonathon approval of weights and thresholds
- [ ] Build Excel template with formulas
- [ ] Update `product1_generator_bulletproof.py` to include scoring calculations
- [ ] Create `product1_scoring_module.py` for Analyst agent
- [ ] Add scoring output to Quality Gate checks
- [ ] Document in AGENT_VENTURE.md
- [ ] Train Researcher on new data requirements
- [ ] Test with Jarotech dataset

---

## 5. APPENDIX: SCORING RATIONALE

### Why These Weights?

| Pillar | Weight | Rationale |
|--------|--------|-----------|
| Financial | 35% | Highest weight — financial distress is the #1 supplier failure mode. Buyers need confidence the supplier will survive the contract term. |
| Operational | 25% | Second highest — ability to deliver is core to procurement. Includes capacity, quality, and supply chain resilience. |
| Geopolitical | 20% | Significant for international suppliers. Can disrupt delivery even if supplier is financially healthy. |
| ESG | 15% | Growing importance due to regulatory pressure (CSRD, supply chain due diligence laws) and reputational risk. Elevation rule ensures it can't be ignored. |
| Commercial | 5% | Lower weight as it's more transactional — pricing and terms can be negotiated, whereas the other pillars reflect structural risk. |

### Why 0-100 Scale?

- Maps cleanly to LOW/MEDIUM/HIGH (33/33/34 split)
- Allows fine-grained differentiation within bands
- Easy to explain to clients ("42 out of 100 = Medium risk")
- Compatible with gauge visualization on Slide 2

---

**Next Step:** Await Jonathon feedback on weights and thresholds before building Excel template and updating generator code.

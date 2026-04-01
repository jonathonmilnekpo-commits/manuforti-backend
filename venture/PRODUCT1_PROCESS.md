# Product 1 — Process Documentation

## Overview

Product 1 is Manu Forti Intelligence's flagship AI-powered supplier analysis report. This document defines the end-to-end process, agent workflow, and risk scoring methodology.

## Report Specifications

### Output Format
- **9-slide PowerPoint deck** (13.333" × 7.5" dimensions)
- **Executive-ready** — designed for board/C-suite presentation
- **Delivery:** PDF + editable PPTX

### Pricing Tiers

| Tier | Price | Delivery | Scope |
|------|-------|----------|-------|
| Standard | $249 | 24 hours | Core analysis (Slides 1-7) |
| Premium | $349 | 12 hours | Full analysis including ESG (All 9 slides) |
| Enterprise | $499 | 6 hours | Custom scope + consultation call |

## Slide Structure (LOCKED)

| Slide | Title | Content | Visual Requirements |
|-------|-------|---------|---------------------|
| 1 | Title | Supplier name, tagline, key stats, source line | Navy background, Manu Forti logo |
| 2 | Executive Summary | Risk gauge + supplier snapshot panel | Semi-circular gauge (0-100), 4-pillar summary |
| 3 | Recommendation | Green/amber/red banner + conditions + risk summary | Conditional approval framework |
| 4 | Supplier Profile | Org structure diagram + company overview + leadership | Parent-subsidiary hierarchy chart |
| 5 | Financial Health | Dual-axis revenue/EBITDA chart + 10-metrics panel | Bar + line chart, metrics table |
| 6 | Market Position | Horizontal bar chart vs peers + competitive context | Lollipop/bars with named competitors |
| 7 | Operational Capability + Risk Assessment | Timeline + 2x2 risk matrix + risk table | Investment timeline, impact/probability matrix |
| 8 | Commercial Intelligence + Peer Risk | Radar chart + peer comparison + terms | 6-dimension radar, peer risk bars |
| 9 | ESG Assessment | E/S/G columns + controversy screening + rating | 3-pillar layout, 16pt controversy text |

## Agent Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PRODUCT 1 PIPELINE                                   │
└─────────────────────────────────────────────────────────────────────────────┘

    ORDER RECEIVED
          │
          ▼
    ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
    │ VETTER  │────→│RESEARCHER│────→│ VENTURE │────→│VALIDATOR│
    │  🔒     │     │   🔍    │     │   📊    │     │   ✅    │
    └────┬────┘     └────┬────┘     └────┬────┘     └────┬────┘
         │               │               │               │
    Security check    Data gathering   Deck generation  Quality gate
    Data sources      Financials       All 9 slides     Structure check
                      Risks            Visuals          Metrics validation
                      ESG              Branding         Branding check
                      Competitors                      
          │               │               │               │
          └───────────────┴───────────────┴───────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │      AIDEN      │
                    │      🤝         │
                    │  Lead Agent     │
                    │  Final review   │
                    │  Strategic add  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    JONATHON     │
                    │      👤         │
                    │  QC Approval    │
                    │  (Enterprise)   │
                    └────────┬────────┘
                             │
                             ▼
                         DELIVERY
```

### Agent Responsibilities

#### Vetter (🔒 Security)
- Validate data sources are secure and legitimate
- Check for potential data poisoning or malicious inputs
- Sanitize output for security-sensitive information
- Approve skills and external tools before use

#### Researcher (🔍 Data)
**Slide Contributions:** All slides

**Key Deliverables:**
- 3-year financials (revenue, EBITDA, debt, cash) → Slide 5
- Risk factors (financial, operational, geopolitical, ESG) → Slides 2, 7
- ESG ratings, certifications, controversies → Slide 9
- Competitor list with revenue/market share → Slide 6
- Peer risk comparison → Slide 8
- Leadership team, org structure, ownership → Slide 4
- Company timeline, milestones → Slide 7
- Commercial terms, negotiation notes → Slide 8

**Research Sources:**
- Company annual reports (primary)
- Bloomberg/Reuters/Capital IQ (financial data)
- Industry reports (Wood Mackenzie, IEA, etc.)
- News/media screening (negative coverage)
- ESG databases (Sustainalytics, MSCI, EcoVadis)
- Sanctions lists (OFAC, EU, UN)
- LinkedIn (leadership, headcount)

#### Venture (📊 Generation)
**Slide Contributions:** All slides

**Key Deliverables:**
- Generated PPTX with all 9 slides
- All visual elements (charts, gauges, matrices)
- Branding compliance (colors, logos, fonts)
- Formatting consistency across slides

**Tools:**
- `generate_[supplier]_v15.py` — Main deck generator
- `generate_[supplier]_visuals.py` — Chart generation
- `product1_quality_gate.py` — Pre-delivery validation

#### Validator (✅ Quality)
**Slide Contributions:** All slides (quality check)

**Quality Gates:**

| Check | Critical | Penalty |
|-------|----------|---------|
| 9 slides present | YES | -20 points |
| Risk gauge on Slide 2 | YES | -8 points |
| Dual-axis chart on Slide 5 | YES | -8 points |
| Horizontal bar chart on Slide 6 | YES | -8 points |
| Timeline + risk matrix on Slide 7 | YES | -8 points each |
| Radar chart on Slide 8 | YES | -8 points |
| ESG columns on Slide 9 | YES | -8 points |
| All 8 financial metrics on Slide 5 | YES | -5 points each |
| Manu Forti branding | NO | -5 points |
| Source line format | NO | -3 points |

**Pass Criteria:** Score ≥ 90, no critical errors

#### Aiden (🤝 Lead)
- Orchestrate entire pipeline
- Review Researcher output before Venture generation
- Final review of Venture output
- Add strategic insights and context
- Make go/no-go decisions on delivery

#### Jonathon (👤 QC)
- Spot-check Standard/Premium reports
- Review all Enterprise reports
- Provide feedback for continuous improvement
- Client escalation point

## Risk Scoring System

### Risk Categories

#### 1. Financial Risk (Weight: 30%)
**Indicators:**
- Revenue trend (3-year CAGR)
- EBITDA margin stability
- Debt/EBITDA ratio
- Net cash/debt position
- Order book coverage
- Credit rating (if available)

**Scoring:**
- LOW (0-33): Revenue growing, positive EBITDA, low leverage
- MEDIUM (34-66): Flat revenue, thin margins, moderate leverage
- HIGH (67-100): Declining revenue, negative EBITDA, high leverage

#### 2. Operational Risk (Weight: 25%)
**Indicators:**
- Manufacturing capacity vs demand
- Geographic diversification
- Key customer concentration
- Certification status (ISO, etc.)
- Track record (years in business)
- Supply chain resilience

**Scoring:**
- LOW (0-33): Diversified, certified, established
- MEDIUM (34-66): Some concentration, minor compliance gaps
- HIGH (67-100): Single point of failure, major operational issues

#### 3. Geopolitical Risk (Weight: 25%)
**Indicators:**
- Country risk rating (OECD/World Bank)
- Sanctions exposure
- Currency volatility
- Regulatory environment
- Political stability
- Trade agreement status

**Scoring:**
- LOW (0-33): Stable democracy, no sanctions, OECD member
- MEDIUM (34-66): Emerging market, some regulatory risk
- HIGH (67-100): Sanctioned, conflict zone, high volatility

#### 4. ESG Risk (Weight: 20%)
**Indicators:**
- Environmental violations
- Labor rights issues
- Governance concerns
- Controversies (media/legal)
- ESG ratings (if available)
- Sustainability commitments

**Scoring:**
- LOW (0-33): Clean record, strong ESG ratings
- MEDIUM (34-66): Minor violations, ongoing controversies
- HIGH (67-100): Major violations, legal action, poor ratings

### Overall Risk Calculation

```
Overall Risk Score = 
    (Financial × 0.30) + 
    (Operational × 0.25) + 
    (Geopolitical × 0.25) + 
    (ESG × 0.20)
```

**ESG Override Rule:**
- If ESG = MEDIUM and all others = LOW → Overall = MEDIUM
- If ESG = HIGH → Overall elevated by one tier (unless already HIGH)

### Risk Gauge Display

```
    0-33: LOW (Green)      → APPROVE
   34-66: MEDIUM (Amber)   → APPROVE with CONDITIONS  
   67-100: HIGH (Red)      → REJECT / EXTREME CAUTION
```

### Recommendation Framework

| Overall Score | Rating | Recommendation | Conditions |
|---------------|--------|----------------|------------|
| 0-33 | LOW | ✅ APPROVE | Standard terms |
| 34-50 | MEDIUM-LOW | ✅ APPROVE | Minor conditions |
| 51-66 | MEDIUM | ⚠️ CONDITIONAL | ESG/milestone requirements |
| 67-80 | MEDIUM-HIGH | ⚠️ CONDITIONAL | Significant safeguards |
| 81-100 | HIGH | ❌ REJECT | Do not proceed |

## SLA Tracking

### Delivery Commitments

| Tier | SLA | Clock Starts | Clock Ends |
|------|-----|--------------|------------|
| Standard | 24 hours | Payment confirmed | Report emailed |
| Premium | 12 hours | Payment confirmed | Report emailed |
| Enterprise | 6 hours | Payment confirmed | Report emailed |

### SLA Monitoring

```
Order Received
     │
     ▼
[Payment Pending] ──→ Timeout: 24h → Auto-cancel
     │
     ▼
[Payment Confirmed]
     │
     ▼
[Research Phase] ──→ SLA checkpoint at 20% of time
     │
     ▼
[Generation Phase] ──→ SLA checkpoint at 60% of time
     │
     ▼
[Validation Phase] ──→ SLA checkpoint at 80% of time
     │
     ▼
[QC Review] ──→ If approaching SLA, escalate to Aiden
     │
     ▼
[Delivered] ──→ Log actual vs committed SLA
```

### SLA Breach Protocol

1. **At 75% of SLA time:** Automated alert to Aiden
2. **At 90% of SLA time:** Escalate to Jonathon
3. **SLA breach:** Automatic refund + apology + expedited delivery

## Quality Standards

### Visual Standards (LOCKED)

**Colors:**
- Navy: #002147 (primary)
- Steel Blue: #2B6CB0 (secondary)
- Mid Grey: #718096 (text)
- Light Grey: #F7FAFC (backgrounds)
- RAG only for status indicators

**Typography:**
- Minimum body: 14pt
- Section titles: 16pt
- Headers: 18-20pt
- Source lines: 11pt

**Charts:**
- Bars: Navy (#002147)
- Lines: Steel Blue (#2B6CB0)
- Minimal gridlines
- Direct data labels
- No 3D effects

### Content Standards

**Action Titles:**
- Every slide subtitle must state the KEY INSIGHT
- Not just topic labels — actual conclusions
- Example: "Nel ASA shows improving revenue but negative EBITDA requires milestone-based payment terms"

**Data Requirements:**
- All financials must have source citations
- Risk ratings must have justification
- Competitors must be named (not "Competitor A")
- All claims must be verifiable

**Branding:**
- Manu Forti logo: bottom-right every slide
- Supplier logo: top-right every slide (white backing)
- Source line: "Source: Manu Forti Intelligence | Confidential | [Month Year]"

## Continuous Improvement

### Feedback Loop

```
Customer receives report
        │
        ▼
[Feedback collected] ──→ Rating + comments
        │
        ▼
[Monthly review] ──→ Analyze patterns
        │
        ▼
[Template updates] ──→ Implement improvements
        │
        ▼
[Version control] ──→ Document changes
```

### Metrics Tracked

- Delivery SLA compliance (%)
- Customer satisfaction score
- Report accuracy (fact-check samples)
- Visual quality score (Validator)
- Time per report by tier

## Appendices

### A. Financial Metrics Required (Slide 5)

1. Revenue (latest year + YoY %)
2. EBITDA (amount + margin %)
3. Net Profit
4. Revenue CAGR (3-year)
5. Order Book / Backlog
6. Gross Debt
7. Net Cash / Net Debt position
8. Debt/EBITDA ratio

### B. ESG Checklist (Slide 9)

**Environmental:**
- [ ] ISO 14001 certification
- [ ] Scope 1 & 2 emissions data
- [ ] EcoVadis rating
- [ ] Environmental violations check

**Social:**
- [ ] Code of Conduct published
- [ ] Labour rights compliance
- [ ] Health & Safety record
- [ ] Grievance mechanisms

**Governance:**
- [ ] Anti-corruption policy
- [ ] Beneficial ownership transparency
- [ ] Sanctions list check
- [ ] Board independence

### C. Controversy Screening (16pt minimum)

- Legal actions (ongoing/settled)
- Negative media coverage
- Regulatory investigations
- Product recalls
- Labor disputes
- Environmental incidents

---

*Document Version: 1.0*
*Last Updated: March 7, 2026*
*Owner: Venture Agent*

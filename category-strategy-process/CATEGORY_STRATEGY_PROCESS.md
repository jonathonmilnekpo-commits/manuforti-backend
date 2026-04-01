# Category Strategy — Generation Process
## Manu Forti Intelligence | Version 1.0 | March 2026

---

## Overview

This document defines the end-to-end process for generating a Manu Forti Category Strategy. 
It is designed for the Venture agent to execute autonomously via the nightly cron job.

**Product Tier (Single):**
- Strategy + Intelligence: €3,999 — Full strategy (Word + Excel) + 3× Product 1 supplier reports + 2× workshops (7–10 days)

**Workshops included in every engagement:**
- Workshop 1 (Evaluation Stage): 2-hour options workshop with client — explore strategic options, stress-test assumptions, uncover additional value opportunities
- Workshop 2 (Delivery Stage): 2-hour final presentation and discussion — walk through recommendation, financial case, implementation roadmap, agree next steps

---

## Phase 1: Client Intake

### Required Inputs (Intake Form)
Collect the following from the client before starting:

```
CATEGORY_STRATEGY_BRIEF = {
    "client_name": "",
    "category_name": "",           # e.g. "High Voltage Electrical Equipment"
    "annual_spend": "",            # e.g. "€15M"
    "spend_currency": "EUR",
    "incumbent_suppliers": [],     # list of current suppliers
    "key_pain_points": [],         # e.g. ["long lead times", "single source risk", "cost escalation"]
    "strategic_priorities": [],    # e.g. ["reduce cost", "improve resilience", "ESG compliance"]
    "evaluation_criteria": [],     # client's preferred criteria (optional — use defaults if blank)
    "evaluation_weights": {},      # client's preferred weights (optional — use defaults if blank)
    "project_pipeline": "",        # e.g. "9 projects/yr: 2 large, 3 mid, 4 small"
    "timeline_constraint": "",     # e.g. "DG2 gate in 6 months"
    "tier": "full"                 # "full" | "bundle" | "partner"
}
```

### Default Evaluation Criteria (AHP) — if client doesn't specify
```
DEFAULT_CRITERIA = {
    "Cost Reduction":        0.30,   # TCO, unit price, lifecycle cost
    "Supply Resilience":     0.25,   # lead time, supply security, dual-source capability
    "Risk Reduction":        0.20,   # financial, geopolitical, ESG, concentration risk
    "Strategic Alignment":   0.15,   # partnership depth, innovation, ESG goals
    "Implementation Ease":   0.10,   # speed to implement, change management burden
}
```

---

## Phase 2: Market Research

### Research Brief per Category
For each category, the Researcher agent should gather:

#### 2.1 Supplier Landscape
- [ ] Top 10 global suppliers — name, HQ, revenue, market share estimate
- [ ] Key European suppliers (or relevant geography)
- [ ] Tier 1 vs Tier 2 distinction
- [ ] Recent M&A activity (last 3 years)
- [ ] New entrants or disruptors

#### 2.2 Market Dynamics
- [ ] Market size (€) and growth rate (CAGR 3-year)
- [ ] Key pricing drivers (raw materials, energy, labour)
- [ ] Price trend: increasing / flat / decreasing (last 2 years)
- [ ] Supply/demand balance: surplus / balanced / constrained
- [ ] Lead time benchmarks for key items

#### 2.3 Risk Environment
- [ ] Geopolitical risks (supply chain geography, sanctions)
- [ ] Regulatory changes (EU CSRD, CSDDD, sector-specific)
- [ ] Technology disruption risks (substitutes, obsolescence)
- [ ] ESG hot spots (controversy, forced labour, emissions)

#### 2.4 Pricing Intelligence
- [ ] List price benchmarks vs negotiated price ranges
- [ ] Volume discount structure (typical)
- [ ] Payment terms norms
- [ ] Framework agreement typical discount (%)

#### 2.5 Cost Driver Analysis (5-Year Lookback)
This is the evidence basis for value claims. For each relevant cost driver:
- [ ] Identify the key cost components (raw materials, labour, energy, logistics, margin)
- [ ] Source 5-year index data (e.g. steel CRU, copper LME, energy Nordpool/TTF, freight Baltic)
- [ ] Quantify how each driver has moved over the period (% change, volatility)
- [ ] Attribute impact to supplier price movements where visible
- [ ] Project forward: Bear/Base/Bull for each key driver (2-year horizon)

**Key indices to check per category:**
- Materials: LME copper, CRU steel HRC/coil, aluminium, rare earth indices
- Energy: Nordpool electricity, TTF gas, Brent crude
- Labour: Eurostat labour cost indices, country-specific wage data
- Logistics: Baltic Dry Index, Freightos container index, fuel surcharge trends
- FX: EUR/USD, EUR/CNY, EUR/NOK for relevant geographies

**Output:** A cost driver summary table showing:
- Driver | 5yr trend | Price impact (%) | Forward projection | Risk rating

**Research Sources (use Brave Search + web fetch):**
- Company annual reports and investor presentations
- Industry reports (BNEF, IEA, Wood Mackenzie abstracts)
- News (Reuters, Bloomberg, FT)
- Supplier websites
- LinkedIn for leadership intelligence

---

## Phase 3: Strategic Options Development

### 3.1 Generating Options
Develop 4–6 mutually exclusive strategic options. Standard options framework:

| Option | Description | Typical When |
|---|---|---|
| Status Quo | Continue current approach | Baseline/reference only |
| Single Source (Preferred Supplier) | Consolidate to one OEM with framework | High volume, trust exists |
| Dual Source | Split between 2 OEMs | Risk management priority |
| Spot/Competitive Tender | Project-by-project open tender | Low volume or commodity |
| Consignment/VMI | OEM holds stock on client's behalf | Very long lead times |
| Strategic Alliance | Joint development, co-investment | Innovation priority |
| Consortium | Buying group with peers | Insufficient volume alone |

**Customise options based on the specific category and client context.**

---

## Phase 3b: Options Workshop (2 Hours — Client-Facing)

**Timing:** After initial options are developed, before MCDM scoring is finalised.

**Purpose:** Surface additional value, stress-test assumptions, validate options with the people who know the business best.

### Workshop Agenda (2 hours)

| Time | Activity | Output |
|------|----------|--------|
| 0:00–0:20 | **Context setting** — present market findings, cost driver analysis, current state assessment | Shared understanding |
| 0:20–0:50 | **Options review** — walk through each strategic option, mechanism, pros/cons | Client reaction + amendments |
| 0:50–1:20 | **Value excavation** — structured discussion: "What else could this unlock?" | Additional value streams identified |
| 1:20–1:45 | **Criteria weighting** — facilitate AHP discussion, agree weights with client | Confirmed AHP weights |
| 1:45–2:00 | **Next steps** — confirm options to evaluate, timeline, data gaps to close | Action list |

### Value Excavation Prompts
Use these questions to uncover value the client hasn't quantified:
- "What project delays have you experienced in the last 3 years — what did that cost?"
- "If you had 30% faster lead times, what would that enable?"
- "What's your biggest supply chain fear? How likely is it? What would it cost?"
- "Where are you paying a premium for certainty? Is it worth it?"
- "What does your best competitor do differently in this category?"
- "If you could change one thing about how you buy this category, what would it be?"

### Outputs from Workshop 1
- [ ] Confirmed or revised strategic options (max 6)
- [ ] Agreed AHP criteria weights
- [ ] Additional value streams quantified
- [ ] Data gaps identified and assigned for closure
- [ ] Client context captured (internal politics, constraints, timelines)

---

## Phase 3c: MCDM Evaluation (Post-Workshop)

### 3.2 AHP Weighting
Apply workshop-agreed or default criteria weights. Document the rationale for each weight.

### 3.3 TOPSIS Scoring
Score each option (1–10) against each criterion. Apply weights. Calculate:
- Normalised decision matrix
- Weighted normalised matrix
- Positive ideal solution (PIS) and Negative ideal solution (NIS)
- Euclidean distance from PIS and NIS
- TOPSIS score (0–1, higher = better)

**Template:** Use `/category-strategy-process/MCDM_TEMPLATE.xlsx`

---

## Phase 4: Business Case Construction

### 4.1 Baseline Establishment
Define the "do nothing" or "current approach" baseline clearly.
- What is the current total cost of ownership?
- What are the current pain points quantified in €?
- What is the cost of inaction per year?

### 4.2 Value Calculation (per strategic option)
For each main benefit type, quantify:

```
VALUE_STREAMS = {
    "Cost Reduction": {
        "method": "spend × discount_rate × probability",
        "example": "€15M spend × 8% discount × 70% confidence = €0.84M/yr"
    },
    "Delay Cost Avoided": {
        "method": "projects/yr × delay_months × monthly_cost × probability",
        "example": "2 projects × 9 months × €1.75M/month × 65% CP = €20.5M/yr"
    },
    "Risk Reduction": {
        "method": "risk_probability × impact × mitigation_factor",
        "example": "15% probability × €5M impact × 80% mitigation = €0.6M/yr"
    },
    "ESG/Compliance": {
        "method": "regulatory_fine_risk × mitigation + efficiency_gains",
        "example": "CSRD non-compliance risk = €0.5M/yr avoided"
    }
}
```

### 4.3 Programme Cost
Document all costs:
- Implementation costs (one-off)
- Annual running costs (fees, staffing, technology)
- Opportunity costs (internal time, transition)

### 4.4 Scenarios
Always model three scenarios:

| Scenario | Assumption Change | Example |
|---|---|---|
| Bear | Lower volume / lower confidence | 1 large project instead of 2 |
| Base | Central case | As modelled |
| Bull | Higher volume / higher realisation | 3 large projects |

### 4.5 Financial Outputs
Calculate for each scenario:
- Annual net value (€)
- 5-year NPV (at 8% discount rate)
- ROI (net value / programme cost)
- Break-even threshold (minimum activity to justify cost)
- Payback period (months)

---

## Phase 5: Document Generation

### 5.1 Word Document Structure (10 sections — LOCKED)

```
1. Executive Summary
   - One-paragraph problem statement
   - One-sentence financial summary (cost, return, ROI)
   - Recommended strategy (one sentence)

2. Strategic Context
   - Category positioning (Strategic/Leverage/Bottleneck/Routine)
   - Current approach and why it's being questioned
   - Key drivers for change

3. Market Analysis
   - Supplier landscape (table: name, HQ, revenue, notes)
   - Market dynamics
   - Pricing intelligence
   - Risk environment

4. Procurement Process (Category-Specific)
   - Current process mapping
   - Key decision gates and timelines
   - Stakeholder map

5. Strategic Options
   - Options table (4–6 options)
   - Narrative description of each option

6. MCDM Evaluation
   - AHP criteria and weights (table with rationale)
   - TOPSIS scoring matrix
   - Results table with scores and ranking
   - Commentary on winner and close competitors

7. Recommended Strategy
   - Clear recommendation (bold, unambiguous)
   - Implementation mechanism
   - Key conditions and dependencies

8. Business Case
   - Baseline and cost of inaction
   - Value streams (table)
   - Programme cost (table)
   - Financial summary table (Bear/Base/Bull)
   - NPV and ROI
   - Break-even analysis

9. Implementation Roadmap
   - Phase table (Phase 0.x, 1, 2, 3...)
   - Each phase: actions, owner, timeline, output
   - Key milestones

10. Appendices
    - Full MCDM workings
    - Data sources
    - Assumptions register
```

### 5.2 Excel Model Structure (5 sheets — LOCKED)

```
Sheet 0: Assumptions
Sheet 1: Executive Dashboard (KPI table, scenario summary)
Sheet 2: Financial Calculator (inputs + outputs)
Sheet 3: MCDM Scoring (AHP weights + TOPSIS calculation)
Sheet 4: Full Component/Item Analysis (if applicable)
```

**Template:** `/category-strategy-process/CATEGORY_STRATEGY_TEMPLATE.xlsx`

### 5.3 PowerPoint Structure (8 slides — LOCKED)

```
Slide 1: Title — product name, client, key stats (4 stat cards)
Slide 2: The Problem — visual diagram of the core challenge
Slide 3: The Solution — two-pane: mechanism A vs mechanism B
Slide 4: The Foundation — prerequisite step (Framework/Contract/etc.)
Slide 5: Business Case — stat cards + value table + scenario table
Slide 6: Technical/Operational Readiness — what needs to change
Slide 7: Implementation Roadmap — 5-phase visual (columns)
Slide 8: Next Steps — 3 decisions needed (numbered cards)
```

**Use:** `/tmp/build_exec_pptx.py` as reference for python-pptx generation pattern.
**Colors:** Navy #002147 / Cobalt #2B6CB0 / White #FFFFFF / Green #48BB78

---

## Phase 6: Quality Gate

### Pre-Delivery Checklist
Before delivering any Category Strategy:

- [ ] Word document: all 10 sections present and complete
- [ ] No placeholder text ([TBD], [INSERT], [...])
- [ ] Financial summary sentence matches numbers in Section 8
- [ ] ROI calculation: net value / programme cost (not gross / cost)
- [ ] All monetary values in EUR with € symbol
- [ ] TOPSIS winner = recommended strategy in Section 7
- [ ] Excel: all 5 sheets present, formulas working, no #REF errors
- [ ] All documents uploaded to Google Drive folder
- [ ] Shared with client email (writer permission)

---

## Phase 7: Delivery

### 7.1 Pre-Delivery Document Share
1. Upload to Google Drive folder: `[ClientName]_CategoryStrategy_[Category]_[YYYY-MM]`
2. Files: `[ClientName]_CategoryStrategy_v1.docx`, `[ClientName]_CategoryStrategy_v1.xlsx`
3. Share with client email (reader permission — writer after workshop)
4. Send pre-read message 24-48 hours before Workshop 2

### Pre-Read Message Template
```
Subject: Your Category Strategy — [Category Name] — Pre-Read for Workshop

[Client Name],

Your [Category Name] Category Strategy document is ready for your review ahead of our workshop.

📄 Strategy Document: [link]
📊 Financial Model: [link]

Please come prepared to discuss:
• Your reaction to the recommended strategy
• Any value streams we may have missed
• Internal constraints or considerations not captured
• Questions on the financial case

We'll use our 2 hours to stress-test the recommendation and agree next steps.

See you [date/time].

Manu Forti Intelligence
```

---

### 7.2 Workshop 2: Final Presentation and Discussion (2 Hours — Client-Facing)

**Timing:** After documents are delivered, before implementation begins.

**Purpose:** Walk through the recommendation, validate the financial case, address concerns, and agree concrete next steps.

### Workshop 2 Agenda (2 hours)

| Time | Activity | Output |
|------|----------|--------|
| 0:00–0:15 | **Recap** — summary of process, data sources, options considered | Alignment |
| 0:15–0:40 | **Recommendation walkthrough** — strategy, mechanism, conditions | Questions surfaced |
| 0:40–1:10 | **Financial deep-dive** — Bear/Base/Bull, NPV, ROI, break-even, key assumptions | Financial sign-off or challenges |
| 1:10–1:35 | **Implementation roadmap** — phases, owners, timelines, dependencies | Roadmap validated |
| 1:35–1:50 | **Risk and mitigations** — top 3-5 risks and how to manage them | Risk register seeded |
| 1:50–2:00 | **Decisions and next steps** — what needs to happen in the next 30 days | Action list with owners |

### Workshop 2 Outputs
- [ ] Recommendation confirmed or adjusted
- [ ] Financial case accepted
- [ ] Implementation owner(s) named
- [ ] 30-day action list agreed
- [ ] Follow-on engagement scoped (Category Partner tier?)

---

### 7.3 Post-Workshop Document Finalisation
1. Incorporate any amendments from Workshop 2
2. Issue final version: `[ClientName]_CategoryStrategy_FINAL.docx`
3. Update Google Drive — grant writer permission
4. Send final confirmation message

### Final Confirmation Message Template
```
Subject: Your Category Strategy — [Category Name] — Final Version

[Client Name],

Following our workshop, the final version of your [Category Name] Category Strategy is ready.

📄 Final Strategy: [link]
📊 Financial Model: [link]

Agreed recommendation: [one sentence]
Your 30-day actions: [3 bullet points from workshop]

Next review: [date if Category Partner, or "reach out when ready to implement"]

Manu Forti Intelligence
```

---

## Templates & Scripts

| File | Purpose |
|---|---|
| `CATEGORY_STRATEGY_TEMPLATE.xlsx` | Excel template (5 sheets, pre-formatted) |
| `CATEGORY_STRATEGY_TEMPLATE.docx` | Word template (10 sections, styles set) |
| `MCDM_CALCULATOR.py` | AHP + TOPSIS calculation script |
| `CATEGORY_STRATEGY_PROCESS.md` | This document |

---

## Reference Cases

| Client | Category | Tier | Date | Key Output |
|---|---|---|---|---|
| Statkraft (internal validation) | HV Electrical Equipment | Full | March 2026 | €55.6M/yr value, 90:1 ROI, Drive: `1HAjv1zzDbXvkxAwqarNpsfPsipxkhCEg` |

---

*Process Owner: Venture Agent | Approved by: Jonathon Milne | Version 1.0 | March 2026*

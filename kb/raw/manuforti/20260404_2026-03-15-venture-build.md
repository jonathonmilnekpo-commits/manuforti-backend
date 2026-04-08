---
date: 2026-03-15
topic: manuforti
tags: ['002147', 'E2E8F0', 'manuforti']
---

# Category Strategy Template Build — March 15, 2026

## Summary
Built complete Category Strategy template suite for Manu Forti Intelligence venture. This is the €3,999 product tier (Strategy + Intelligence) with full documentation, Excel model, and Word template.

## Files Built

### 1. CATEGORY_STRATEGY_TEMPLATE.xlsx (5 sheets)
**Location:** `/Users/jonathonmilne/.openclaw/workspace/category-strategy-process/CATEGORY_STRATEGY_TEMPLATE.xlsx`
**Size:** ~180KB with embedded charts

**Sheets:**
- **Sheet 0: Assumptions** — Client inputs, incumbent suppliers (3 rows), pain points (3 rows), strategic priorities (3 rows), AHP criteria with default weights (Cost 30%, Resilience 25%, Risk 20%, Strategic 15%, Ease 10%)
- **Sheet 1: Executive Dashboard** — KPI summary, Bear/Base/Bull scenario comparison, recommendation box. Charts: scenario bar chart, value stream donut chart. Pre-populated with Statkraft reference case (€55.6M value, 90:1 ROI)
- **Sheet 2: Financial Calculator** — 9 value streams with confidence weighting, programme costs, scenario analysis (Bear 70%, Base 100%, Bull 130%), NPV/ROI/payback calculations. Charts: waterfall value build-up, 5-year NPV trajectory
- **Sheet 3: MCDM Scoring** — AHP pairwise matrix, normalized weights, consistency ratio. TOPSIS full calculation: scoring matrix (6 options × 5 criteria), normalized matrix, weighted normalized, PIS/NIS, distances, scores, ranks. Charts: TOPSIS horizontal bar chart, radar chart comparing top 2 options
- **Sheet 4: Component Analysis** — Supplier landscape table, should-cost breakdown (raw materials, labour, energy, overheads, margin, logistics, warranty), cost driver analysis (5-year trends). Charts: should-cost pie chart, cost driver trend lines

**Styling:** Navy (#002147) headers, white text, alternating light blue rows, bold headers, thin borders throughout.

### 2. CATEGORY_STRATEGY_TEMPLATE.docx (10 sections)
**Location:** `/Users/jonathonmilne/.openclaw/workspace/category-strategy-process/CATEGORY_STRATEGY_TEMPLATE.docx`
**Size:** ~25KB

**Structure:**
- Front matter: CLIENT BRIEF intake table with all required fields
- Section 1: Executive Summary — Problem statement, financial summary, recommended strategy
- Section 2: Strategic Context — Kraljic positioning, current approach, change drivers
- Section 3: Market Analysis — Supplier landscape table, market dynamics, cost driver table, pricing intelligence, risk environment
- Section 4: Procurement Process — Current process, decision gates, stakeholder map
- Section 5: Strategic Options — Options table (4-6 options), narrative descriptions
- Section 6: MCDM Evaluation — AHP weights table, TOPSIS matrix, results table, commentary
- Section 7: Recommended Strategy — Bold recommendation, mechanism, conditions
- Section 8: Business Case — Baseline, value streams table, programme costs, Bear/Base/Bull summary, NPV/ROI/break-even
- Section 9: Implementation Roadmap — Phase table (0.x through 3), milestones, resource requirements
- Section 10: Appendices — MCDM workings, data sources, assumptions register

**Styling:** Navy (#002147) bold headings, grey (#E2E8F0) instruction boxes with italic text, tables with navy headers.

### 3. order.html Updated
**Location:** `/Users/jonathonmilne/.openclaw/workspace/manuforti-website/order.html`

**Changes:**
- Added "Category Strategy" as third product option (featured/amber styling)
- Price: €3,999 fixed
- Shows/hides appropriate sections based on product selection
- Category Strategy intake fields: Category Name, Annual Spend, Currency, Timeline Constraint (optional), Incumbent Suppliers (textarea), Key Pain Points (textarea), Strategic Priorities (textarea)
- Includes engagement details box listing deliverables (Word doc, Excel model, 3× Product 1 reports, 2× workshops)

### 4. Build Scripts
**Location:** `/Users/jonathonmilne/.openclaw/workspace/category-strategy-process/`
- `build_excel_part1.py` — Sheet 0 (Assumptions)
- `build_excel_part2.py` — Sheet 1 (Executive Dashboard)
- `build_excel_part3.py` — Sheet 2 (Financial Calculator)
- `build_excel_part4.py` — Sheet 3 (MCDM Scoring)
- `build_excel_part5.py` — Sheet 4 (Component Analysis)
- `build_word_template.py` — Word template generator

## Issues Encountered
1. **Matplotlib color format** — Initially used hex strings without '#' prefix, causing ValueError. Fixed by using f-strings with proper hex format: `f'#{GREEN}'`
2. **HTML file corruption** — Original order.html had malformed duplicate content. Rebuilt clean version with proper structure.

## What Jonathon Should Review

### Excel Template
1. **Formula validation** — Check that weighted value calculations (=B*C) work correctly when you input real data
2. **Scenario sensitivity** — Verify Bear/Base/Bull multipliers (70%/100%/130%) align with your methodology
3. **Chart rendering** — Open in Excel and confirm all 8 charts display correctly
4. **AHP defaults** — Confirm the 30/25/20/15/10 weight split is appropriate for most engagements

### Word Template
1. **Section flow** — Review if the 10-section structure matches your delivery expectations
2. **Instruction clarity** — Check if grey instruction boxes provide enough guidance for analysts
3. **Table formats** — Verify supplier landscape, cost driver, and options tables have right column counts

### Order Form
1. **Category Strategy positioning** — Currently featured (amber border). Confirm this is the desired prominence.
2. **Required vs optional fields** — Currently: Category Name, Annual Spend, Currency, Incumbent Suppliers, Pain Points, Priorities are required. Timeline is optional. Adjust if needed.
3. **Price display** — Fixed at €3,999. Confirm no discount codes apply to this tier.

## Next Steps
1. Test templates with a real category (e.g., Statkraft HV Electrical Equipment)
2. Create MCDM_CALCULATOR.py standalone script for command-line TOPSIS calculations
3. Build PowerPoint template (8 slides) if needed per PROCESS.md
4. Set up Google Drive folder structure for client deliverables

## Reference
- Process doc: `category-strategy-process/CATEGORY_STRATEGY_PROCESS.md`
- Methodology review: `category-strategy-process/METHODOLOGY_REVIEW.md`
- Statkraft reference case: Drive folder `1HAjv1zzDbXvkxAwqarNpsfPsipxkhCEg`

# Product 1 Format Lock-Down Plan
## Standardization Protocol for Supplier Intelligence Reports

**Goal:** Create a repeatable, consistent process where every report follows the same structure, design, and quality standards with minimal variation.

---

## Phase 1: Data Input Standardization (Week 1)

### Step 1: Create Supplier Data Template
**What:** JSON template that captures all raw data for any supplier
**Purpose:** Ensures consistent data collection regardless of supplier type

**Template structure:**
```json
{
  "supplier_name": "",
  "legal_name": "",
  "founded_year": 0,
  "headquarters": "",
  "employees": "",
  "duns": "",
  "cnpj": "",
  
  "financials": {
    "revenue_latest": 0,
    "revenue_yoy_percent": 0,
    "ebitda": 0,
    "ebitda_margin": 0,
    "net_profit": 0,
    "revenue_cagr_3yr": 0,
    "order_book": 0,
    "gross_debt": 0,
    "net_cash_debt": 0,
    "debt_to_ebitda": 0
  },
  
  "risk_ratings": {
    "overall": "LOW|MEDIUM|HIGH",
    "score": 0,
    "financial": "LOW|MEDIUM|HIGH",
    "operational": "LOW|MEDIUM|HIGH",
    "geopolitical": "LOW|MEDIUM|HIGH",
    "esg": "LOW|MEDIUM|HIGH"
  },
  
  "leadership": [
    {"name": "", "title": "", "background": ""}
  ],
  
  "operations": {
    "countries": [],
    "key_projects": [],
    "certifications": [],
    "facilities": []
  },
  
  "risks": [
    {"category": "", "description": "", "impact": "HIGH|MEDIUM|LOW", "probability": "HIGH|MEDIUM|LOW", "mitigation": ""}
  ],
  
  "esg": {
    "environmental": {"rating": "", "details": ""},
    "social": {"rating": "", "details": ""},
    "governance": {"rating": "", "details": ""},
    "controversies": []
  },
  
  "recommendation": {
    "status": "APPROVED|APPROVED_WITH_CONDITIONS|REJECTED",
    "conditions": [],
    "next_steps": []
  }
}
```

**Action:** Create `supplier_data_template.json` with validation rules

---

## Phase 2: Visual Generation Lock-Down (Week 1-2)

### Step 2: Standardize Chart Generation Script
**Current state:** `generate_boskalis_visuals.py` works but requires manual edits
**Target state:** Single script that reads JSON input, generates all 9 visuals automatically

**Requirements:**
- Script takes `--input` (JSON file) and `--output-dir` parameters only
- No hardcoded supplier names in the script
- All styling parameters (colors, fonts, sizes) defined as constants at top of file
- Generates exactly 9 PNG files: `01_title.png` through `09_esg.png`

**Lock-down measures:**
```python
# Constants that NEVER change
COLORS = {
    'navy': '#002147',
    'steel_blue': '#2B6CB0',
    'mid_grey': '#718096',
    'accent_bg': '#EBF4FF',
    'green': '#38A169',
    'amber': '#D69E2E',
    'red': '#C53030'
}

FONT_SIZES = {
    'title': 28,
    'subtitle': 16,
    'body': 14,
    'footnote': 11
}

CHART_SIZES = {
    'financial_chart_width': 7.5,
    'timeline_width': 7.0,
    'risk_matrix_width': 5.5
}
```

**Action:** Refactor `generate_supplier_visuals.py` to be fully data-driven

---

### Step 3: Create Logo Processing Tool
**What:** Script to standardize supplier logo preparation
**Purpose:** Ensures consistent logo appearance across all slides

**Function:**
```python
def process_logo(input_svg_or_png, output_path):
    # 1. Convert to PNG if SVG
    # 2. Remove white background (make transparent)
    # 3. Crop to content
    # 4. Resize to standard dimensions
    # 5. Save as [supplier]_logo_transparent.png
```

**Action:** Create `process_supplier_logo.py`

---

## Phase 3: Deck Assembly Automation (Week 2)

### Step 4: Build Report Generator
**Current state:** `generate_boskalis_v15.py` requires code edits per supplier
**Target state:** Single command: `python generate_report.py --data supplier.json --output report.pptx`

**How it works:**
1. Read `supplier_data_template.json`
2. Load logo from processed assets folder
3. Generate all 9 visuals using `generate_supplier_visuals.py`
4. Assemble PPTX using python-pptx
5. Apply branding (source line, footer, logo placement)
6. Output final report

**Lock-down principle:** Zero code changes between suppliers. Only the input JSON changes.

**Action:** Build `generate_report.py` (master orchestrator script)

---

### Step 5: Create Report Template File
**What:** Empty PPTX template with locked layouts
**Purpose:** Ensures consistent slide dimensions, placeholder positions, master slide formatting

**Contents:**
- 9 slides with correct dimensions (13.333" x 7.5")
- Placeholder text boxes in correct positions
- Master slide with source line and footer pre-positioned
- No content — just structure

**Action:** Create `product1_v15_master_template.pptx`

---

## Phase 4: Quality Control System (Week 2-3)

### Step 6: Pre-Generation Validation
**What:** Validate input data before generating report
**Purpose:** Catch missing data early, ensure completeness

**Script:** `validate_input_data.py`
```python
def validate_supplier_data(json_file):
    required_fields = ['supplier_name', 'financials.revenue_latest', ...]
    # Check all required fields present
    # Validate risk ratings are valid enums
    # Check financials are numbers
    # Return list of missing/wrong data
```

**Gate:** Generation only proceeds if validation passes

---

### Step 7: Post-Generation Validation
**Current state:** `validate_report.py` exists
**Enhancement:** Integrate into generation pipeline

**Workflow:**
1. Generate report
2. Auto-run `validate_report.py` on output
3. If errors found → flag for review, don't deliver
4. If only warnings → deliver with note
5. If clean → deliver as normal

**Action:** Update `generate_report.py` to include validation step

---

### Step 8: Create Diff/Compare Tool
**What:** Script to compare two reports and highlight differences
**Purpose:** Ensure consistency across reports, catch unintended changes

**Usage:** `python compare_reports.py report_a.pptx report_b.pptx`

**Output:**
- Slide-by-slide comparison
- Design element differences (fonts, colors, positions)
- Content differences (text changes)
- Structural differences (missing slides, wrong order)

**Action:** Build `compare_reports.py`

---

## Phase 5: Documentation & Process (Week 3)

### Step 9: Create Standard Operating Procedure (SOP)
**Document:** `PRODUCT1_SOP.md`

**Contents:**
1. **New Supplier Onboarding Checklist**
   - [ ] Collect financial data
   - [ ] Research leadership team
   - [ ] Gather ESG information
   - [ ] Identify 4 peer companies
   - [ ] Download logo (SVG preferred)

2. **Data Collection Standards**
   - Where to find DUNS numbers
   - How to calculate CAGR
   - What constitutes "gross debt" vs "net debt"
   - Peer selection criteria (revenue size, geography, sector)

3. **Report Generation Steps**
   ```
   Step 1: Fill out supplier_data_template.json
   Step 2: Run validate_input_data.py
   Step 3: Process logo with process_supplier_logo.py
   Step 4: Run generate_report.py
   Step 5: Review validation output
   Step 6: Deliver to client
   ```

4. **Quality Checklist**
   - [ ] All 9 slides present
   - [ ] No green on Recommendation slide
   - [ ] Debt metrics in Financial Health
   - [ ] 6 ESG conditions listed
   - [ ] Logo appears on every slide
   - [ ] Source line correct format

---

### Step 10: Version Control & Change Management
**Rule:** Template changes require explicit approval

**System:**
1. `product1_v15_schema.json` is canonical (locked)
2. Any proposed changes → create `product1_v16_schema.json` proposal
3. Changes must be:
   - Documented in CHANGELOG.md
   - Approved by Jonathon
   - Tested on sample report
   - Validator updated before deployment

**Change proposal template:**
```markdown
## Proposed Change: v15 → v16
**Date:** YYYY-MM-DD
**Proposed by:** [name]
**Change:** [description]
**Reason:** [why needed]
**Impact:** [what reports need regeneration]
**Approved:** Y/N
```

---

## Phase 6: Testing & Validation (Week 3-4)

### Step 11: Create Reference Reports
**What:** Set of 3 "gold standard" reports that pass all validation
**Purpose:** Benchmark for all future reports

**Reports:**
1. `REFERENCE_Boskalis_v15.pptx` (existing)
2. `REFERENCE_GEL_v15.pptx` (regenerate using new system)
3. `REFERENCE_TestSupplier_v15.pptx` (fictional, covers all edge cases)

**Usage:**
- New generator tested against reference reports
- Compare tool ensures similarity
- Any deviation flagged

---

### Step 12: End-to-End Testing
**Test scenarios:**
1. Generate report for known supplier (Boskalis data) → should match reference
2. Generate report with minimal data → should fail validation gracefully
3. Generate report with edge case data (negative revenue, zero employees) → handle gracefully
4. Run 5 reports back-to-back → all should pass validation

**Action:** Create `test_report_generation.py` with automated tests

---

## Summary: Locked Elements vs. Variable Elements

### 🔒 LOCKED (Never Changes Without Approval)
| Element | Current State | Locked By |
|---------|---------------|-----------|
| Slide count | 9 slides | product1_v15_schema.json |
| Slide order | Fixed sequence | Schema + generator script |
| Color palette | Navy/Steel/Mid-grey | generate_supplier_visuals.py constants |
| Font sizes | 14pt min body | Design system constants |
| Chart dimensions | 7.5" financial, etc. | Script constants |
| Source line format | "Source: Manu Forti..." | generate_report.py |
| Logo placement | Top-right, white backing | Deck assembly code |
| Financial metrics required | 8 metrics including debt | Schema + validator |
| ESG conditions count | 6 conditions | Schema validation |

### 📝 VARIABLE (Changes Per Supplier)
| Element | Input Method |
|---------|--------------|
| Supplier name | supplier_data_template.json |
| Financial numbers | JSON data |
| Risk ratings | JSON data |
| Leadership bios | JSON data |
| Peer companies | JSON data |
| ESG details | JSON data |
| Recommendation | JSON data |
| Logo file | Processed via script |

---

## Implementation Timeline

| Week | Deliverables |
|------|-------------|
| Week 1 | supplier_data_template.json, validate_input_data.py, process_supplier_logo.py |
| Week 2 | generate_report.py (refactored), product1_v15_master_template.pptx |
| Week 3 | compare_reports.py, PRODUCT1_SOP.md, validation integration |
| Week 4 | Reference reports, test suite, final validation |

---

## Success Metrics

- **Consistency:** 95%+ of generated reports pass validation on first attempt
- **Efficiency:** New supplier report generated in <30 minutes (currently ~2-3 hours)
- **Quality:** Zero client complaints about formatting inconsistencies
- **Maintainability:** New developer can generate a report within 1 hour of reading SOP

---

**Next Step:** Approve this plan, then start with Week 1 deliverables (data template + validation scripts).

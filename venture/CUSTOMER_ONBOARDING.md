# Manu Forti — Customer Onboarding & Order Fulfillment Guide

**Purpose:** Step-by-step guide for processing orders from receipt to delivery  
**Audience:** Jonathon (fulfillment), Aiden (automation support)  
**Target SLA:** Standard 24h / Premium 12h / Enterprise 6h

---

## Order Lifecycle Overview

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  ORDER   │───▶│ PAYMENT  │───▶│ RESEARCH │───▶│  REPORT  │───▶│ DELIVERY │
│ RECEIVED │    │ CONFIRMED│    │  PHASE   │    │ GENERATED│    │  & QC    │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
     │               │               │               │               │
     ▼               ▼               ▼               ▼               ▼
  Email sent    Webhook to      Aiden assigns   Venture runs     Final PDF
  to customer   Aiden           to Researcher   pipeline         to customer
                                (auto or        (automated       + Jonathon
                                manual)         + manual QC)     notified
```

---

## Phase 1: Order Receipt (Automated)

### What Happens
1. Customer submits order via website
2. Backend creates order record (status: `pending_payment`)
3. Payment processed (Stripe/Vipps/Invoice)
4. On payment confirmation:
   - Order status → `paid`
   - Confirmation email sent to customer
   - Webhook notification sent to Aiden
   - Order appears in admin dashboard

### Aiden Notification Format
```json
{
  "event": "order.paid",
  "order": {
    "id": "MF-2026-00123",
    "product_type": "report",
    "tier": "Premium",
    "customer_name": "John Smith",
    "customer_email": "john@company.com",
    "company_name": "Acme Corp",
    "supplier_name": "Nel ASA",
    "sla_hours": 12,
    "paid_at": "2026-03-17T09:30:00Z"
  }
}
```

### Your Action
- [ ] Verify order appears in admin dashboard
- [ ] Confirm SLA deadline (calculate from `paid_at`)
- [ ] Add to personal task list with deadline alert

---

## Phase 2: Research Phase (Manual + Automated)

### For Product 1: Supplier Analysis Reports

#### Step 1: Data Collection (Researcher Agent)
**Time:** 30-60 minutes  
**Tools:** Web search, financial databases, news sources

**Required Data Points:**
- [ ] Company overview (founded, employees, headquarters)
- [ ] Leadership team (CEO, CFO, key executives)
- [ ] Financials (revenue, EBITDA, debt, order book)
- [ ] Stock performance (if public)
- [ ] Market position vs competitors
- [ ] Recent news and controversies
- [ ] ESG ratings and reports
- [ ] Operational capabilities
- [ ] Commercial terms intelligence

**Data Sources:**
- Company annual reports / investor relations
- Yahoo Finance / Bloomberg / Reuters
- Industry reports (Wood Mackenzie, etc.)
- News search (Google News, industry publications)
- ESG databases (MSCI, Sustainalytics)
- LinkedIn (leadership, headcount)

#### Step 2: Risk Scoring (Automated)
**Tool:** `venture/Product1_Risk_Scoring_System.xlsx`

Input collected data → Spreadsheet calculates:
- Financial Risk (0-100)
- Operational Risk (0-100)
- Geopolitical Risk (0-100)
- ESG Risk (0-100)
- **Overall Risk** (composite with ESG elevation rule)

**ESG Elevation Rule:**
- If ESG = MEDIUM → Overall cannot be LOW
- If ESG = HIGH → Overall = HIGH regardless of other scores

#### Step 3: Report Generation (Venture Agent)
**Time:** 15-30 minutes automated

**Process:**
1. Run `product1_generator_bulletproof.py`
2. Input: Researcher data + risk scores
3. Output: 9-slide PPTX draft
4. Run `product1_quality_gate.py` for validation

**Quality Gate Checks:**
- [ ] All 9 slides present
- [ ] Risk gauge matches calculated score
- [ ] Financial metrics panel complete (10 metrics)
- [ ] Charts render correctly
- [ ] Branding consistent (navy/steel blue)
- [ ] No placeholder text remaining

### For Product 2: Media Monitoring

**Process:**
1. Set up Google Alerts for supplier name + variants
2. Configure weekly digest (Monitor tier) or real-time (Alert tier)
3. First report within 24 hours of setup
4. Ongoing monitoring per subscription

### For Product 3: Category Strategy

**Process:**
1. Schedule Options Workshop (within 48 hours)
2. Send Category Strategy intake template
3. Gather additional data during workshop
4. Build Excel model (5 sheets)
5. Write Word strategy document (10 sections)
6. Generate 3× Product 1 reports for key suppliers
7. Schedule Delivery Workshop (7-10 days total)

---

## Phase 3: Quality Control (Jonathon)

### QC Checklist for Product 1 Reports

**Slide-by-Slide Review:**

| Slide | Check | Standard |
|-------|-------|----------|
| 1. Title | Logo placement, supplier name, date | Manu Forti logo bottom-right |
| 2. Executive Summary | Risk gauge accurate, snapshot complete | Gauge matches calculated score |
| 3. Recommendation | Banner color matches risk, conditions clear | LOW=Green, MED=Amber, HIGH=Red |
| 4. Profile | Org chart readable, leadership accurate | Structure matches reality |
| 5. Financial | Dual-axis chart, 10 metrics complete | Debt/EBITDA highlighted |
| 6. Market Position | Peer comparison accurate, bars correct | Named competitors only |
| 7. Operational | Timeline realistic, risk matrix positioned | Matrix shows actual exposure |
| 8. Commercial | Radar chart balanced, peer risks accurate | No missing data points |
| 9. ESG | E/S/G columns balanced, controversy flagged | 16pt font for controversies |

**Common Issues to Fix:**
- [ ] Outdated financial data → Update to latest available
- [ ] Missing metrics → Research and fill gaps
- [ ] Chart formatting → Adjust colors to navy/steel blue
- [ ] Typos in company names → Double-check spelling
- [ ] Incorrect risk gauge → Verify spreadsheet calculation

**QC Time Budget:**
- Standard: 15 minutes
- Premium: 30 minutes
- Enterprise: 45 minutes

### Approval Decision

**If QC Passes:**
- Approve for delivery
- Update order status to `ready_for_delivery`

**If QC Fails:**
- Send back to Venture with specific fixes
- Reset SLA clock if significant rework needed
- Document issue for process improvement

---

## Phase 4: Delivery (Automated + Manual)

### Step 1: Finalize Report
- Convert PPTX to PDF for customer delivery
- Filename format: `[Supplier]_Product1_[Date].pdf`
- Example: `Nel_ASA_Product1_2026-03-17.pdf`

### Step 2: Upload to Storage
**Options:**
- AWS S3 (recommended for scale)
- Google Drive (shareable link)
- Railway volume (simplest for MVP)

**Security:**
- Generate pre-signed URL (expires in 7 days)
- Or password-protect PDF

### Step 3: Send to Customer
**Email Template:**
```
Subject: Your Supplier Analysis Report is Ready — Nel ASA

Hi [Customer Name],

Your [Tier] supplier analysis report for [Supplier Name] is now ready.

📊 Report Details:
• Supplier: [Supplier Name]
• Risk Rating: [LOW/MEDIUM/HIGH]
• Report Date: [Date]
• Order Reference: [MF-2026-XXXXX]

📥 Download Report:
[Secure Download Link — expires in 7 days]

📝 What's Included:
• 9-slide executive analysis
• Financial health assessment
• Market position vs peers
• Operational capability review
• ESG evaluation
• Risk assessment with mitigation recommendations

💬 Questions?
Reply to this email or contact support@manuforti.com

Best regards,
Jonathon Milne
Manu Forti Intelligence
```

### Step 4: Update Order Status
- Status: `delivered`
- Delivered at: [timestamp]
- Delivery method: Email + download link

### Step 5: Follow-Up (24 hours later)
**Email Template:**
```
Subject: How was your supplier analysis report?

Hi [Customer Name],

I hope you found the Nel ASA report valuable.

Quick questions:
1. Did the report meet your expectations?
2. Was the risk assessment helpful for your decision?
3. Any feedback for improvement?

If you need another supplier analyzed, reply with the supplier name.

Best,
Jonathon
```

---

## SLA Tracking

### Deadline Calculator
```
Order Paid: 2026-03-17 09:00
Tier: Premium (12 hours)
Deadline: 2026-03-17 21:00
Buffer: 2 hours (deliver by 19:00)
```

### Escalation Triggers
- **T-6 hours:** If research not complete → Prioritize
- **T-2 hours:** If report not generated → Alert Jonathon
- **T-30 min:** If QC not complete → Rush mode
- **Missed SLA:** Automatic refund + apology + free upgrade

---

## Order Status Reference

| Status | Meaning | Next Action |
|--------|---------|-------------|
| `pending_payment` | Awaiting payment | None (automated) |
| `paid` | Payment confirmed | Start research |
| `researching` | Data collection in progress | Monitor progress |
| `generating` | Report being generated | Wait for completion |
| `qc_review` | Awaiting Jonathon QC | Review and approve |
| `ready_for_delivery` | Approved, ready to send | Send to customer |
| `delivered` | Report sent | Schedule follow-up |
| `completed` | Follow-up done, order closed | Archive |
| `refunded` | Payment refunded | Close order |

---

## Tools & Resources

### File Locations
- Risk Scoring: `venture/Product1_Risk_Scoring_System.xlsx`
- Process Docs: `venture/PRODUCT1_PROCESS.md`
- Templates: `skills/product-1-generator/`
- Sample Reports: ` venture/samples/`

### Admin Dashboard
```
URL: https://your-api.railway.app/api/admin/orders
Header: X-API-Key: [your_admin_key]
```

### Generator Commands
```bash
# Generate report (Venture Agent)
python skills/product-1-generator/product1_generator_bulletproof.py --supplier "Nel ASA" --data research_data.json

# Quality gate
python skills/product-1-generator/product1_quality_gate.py --input Nel_ASA_draft.pptx
```

---

## First Customer Protocol

### Pre-Launch (Before First Order)
- [ ] All systems tested end-to-end
- [ ] Stripe in test mode (or live if activated)
- [ ] Email templates reviewed
- [ ] Personal calendar clear for rapid response

### First Order Received
- [ ] **Acknowledge within 1 hour** (even if just automated email)
- [ ] **Personal message from Jonathon:** "Thanks for being our first customer..."
- [ ] **Expedite processing:** Aim for 50% of SLA time
- [ ] **Extra QC attention:** Perfect delivery matters more than speed
- [ ] **Ask for testimonial:** After successful delivery

### Post-Delivery
- [ ] Thank you call/video (optional but powerful)
- [ ] Request LinkedIn recommendation
- [ ] Offer referral discount (20% off next report)
- [ ] Document learnings for process improvement

---

## Metrics to Track

### Per Order
- Time from payment to delivery
- QC pass rate (target: >95%)
- Customer satisfaction (follow-up survey)
- Issues/escalations

### Monthly
- Total orders
- Revenue by product
- SLA compliance rate
- Customer acquisition cost
- Net Promoter Score

---

## Emergency Procedures

### System Outage
1. Check Railway status: https://status.railway.app
2. Check Stripe status: https://status.stripe.com
3. If backend down: Switch to manual order intake (email/phone)
4. Communicate proactively to affected customers

### Missed SLA
1. Notify customer before deadline (don't wait for them to complain)
2. Offer compensation (refund + free upgrade)
3. Expedite remaining work
4. Document root cause
5. Update process to prevent recurrence

### Data Quality Issue
1. If report delivered with error: Recall and fix immediately
2. Send corrected version with apology
3. Offer compensation for inconvenience
4. Update QC checklist to catch similar issues

---

## Appendix: Email Templates

### Order Confirmation (Automated)
```
Subject: Order Received — [Supplier Name] Analysis

Thank you for your order!

Order: [MF-2026-XXXXX]
Supplier: [Supplier Name]
Tier: [Standard/Premium/Enterprise]
SLA: [X] hours
Expected delivery: [Date/Time]

We'll notify you when your report is ready.
```

### Payment Failed (Automated)
```
Subject: Payment Issue — Action Required

We couldn't process your payment.

Order: [MF-2026-XXXXX]
Issue: [Card declined / Expired / etc.]

Please update your payment method: [Link]
```

### Report Ready (Manual/Semi-automated)
```
Subject: Your Report is Ready — [Supplier Name]

Hi [Name],

Your [Tier] supplier analysis for [Supplier] is ready.

Download: [Link]
Password: [If applicable]

Questions? Just reply.

Jonathon
```

---

**Document Version:** 1.0  
**Last Updated:** March 17, 2026  
**Owner:** Venture Agent  
**Review Cycle:** Update after first 10 customers

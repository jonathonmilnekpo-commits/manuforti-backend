# SAP & Jaggaer AI Integration Plan
## Statkraft Procurement AI Programme — Data Access Architecture
**Prepared by Aiden | March 17, 2026 | CONFIDENTIAL**

---

## OVERVIEW

For AI agents to deliver value in procurement, they need clean, structured, real-time access to procurement data. Statkraft uses SAP (ERP/S4HANA) and Jaggaer (source-to-pay platform). This document outlines how to connect both systems to the AI agent layer securely.

---

## SYSTEM 1: SAP S/4HANA

### Available APIs

| API | Description | Use Cases |
|-----|-------------|-----------|
| **SAP Business Accelerator Hub (API Hub)** | 600+ REST/OData APIs for S4HANA | Purchase orders, supplier master, invoices |
| **SAP Procurement APIs** | MM module: POs, GRs, invoices, vendor master | Spend classification, demand forecasting |
| **SAP Joule** | Native AI copilot embedded in S4HANA | In-system RFQ drafting, contract summaries |
| **OData v4 / REST** | Standard protocol for all S4HANA APIs | Any agent integration |
| **SAP Integration Suite** | Middleware connecting SAP to external systems | Event-driven agent triggers |

### Key SAP APIs for Procurement AI

```
1. PurchaseOrderAPI_0001 — All PO data (header, items, conditions)
2. SupplierAPI_0001 — Supplier master data
3. ContractAPI_0001 — Contract header and items
4. PurchaseRequisitionAPI_0001 — PR data for demand forecasting
5. SupplierInvoiceAPI_0001 — Invoice data for spend analytics
6. Material API — Material master for MRO classification
```

### Integration Pattern: Read-Only Agent Access

```
┌─────────────┐      REST/OData      ┌──────────────────┐
│  SAP S4HANA │ ──────────────────▶  │  Data Layer       │
│  (source)   │   (read-only API     │  (sanitise +      │
└─────────────┘    service user)     │   classify data)  │
                                     └────────┬─────────┘
                                              │ structured
                                              │ JSON/MD
                                     ┌────────▼─────────┐
                                     │   AI Agent Layer  │
                                     │  (OpenClaw/       │
                                     │   LangChain)      │
                                     └──────────────────┘
```

### Implementation Steps (SAP)

**Step 1: Create a Dedicated API Service User**
- Create read-only service account in SAP (no write permissions)
- Assign roles: MM_PURCH_READ, FI_INVOICE_READ, SD_SUPPLIER_READ
- Enable OAuth 2.0 client credentials flow

**Step 2: Enable SAP Integration Suite (or direct OData)**
- Configure OData service endpoints for the 6 APIs above
- Set up API Gateway with rate limiting and logging
- Enable audit logging for all API calls (NIS2 compliance)

**Step 3: Data Extraction Script (Python)**
```python
import requests
import json

SAP_BASE = "https://statkraft.s4hana.ondemand.com/sap/opu/odata/sap/"
TOKEN_URL = "https://statkraft.authentication.eu10.hana.ondemand.com/oauth/token"

def get_token(client_id, client_secret):
    r = requests.post(TOKEN_URL, data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    })
    return r.json()["access_token"]

def get_purchase_orders(token, date_from, date_to):
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    url = f"{SAP_BASE}API_PURCHASEORDER_PROCESS_SRV/A_PurchaseOrder"
    params = {
        "$filter": f"CreationDate ge datetime'{date_from}' and CreationDate le datetime'{date_to}'",
        "$select": "PurchaseOrder,Supplier,TotalNetOrderAmount,Currency,DocumentCurrency",
        "$top": 1000,
        "$format": "json"
    }
    return requests.get(url, headers=headers, params=params).json()

def export_to_markdown(data, output_path):
    """Export SAP data to structured MD files for AI agent consumption"""
    with open(output_path, 'w') as f:
        f.write("# SAP Purchase Order Extract\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        for po in data['d']['results']:
            f.write(f"## PO {po['PurchaseOrder']}\n")
            f.write(f"- Supplier: {po['Supplier']}\n")
            f.write(f"- Value: {po['TotalNetOrderAmount']} {po['Currency']}\n\n")
```

**Step 4: Structured MD File Output (for AI consumption)**

AI agents work best with structured markdown files rather than raw API JSON. The integration layer should export:

```
/data/sap/
├── spend_summary_YYYY-MM.md      # Monthly spend by category/supplier
├── active_contracts.md           # Contract portfolio summary
├── supplier_master.md            # Top 100 supplier profiles
├── open_pos.md                   # Open POs by category
├── invoices_anomalies.md         # AI-flagged invoice exceptions
└── mro_demand_history.md         # 24-month MRO consumption data
```

**SAP Joule (Native AI — no custom integration needed):**
- Already available in S4HANA as embedded copilot
- Can draft RFQs, summarise contracts, query spend data in natural language
- No data leaves SAP perimeter — built-in compliance
- Recommend activating as Track A/B tool immediately

---

## SYSTEM 2: JAGGAER

### Available APIs

| API | Description | Use Cases |
|-----|-------------|-----------|
| **Jaggaer REST API v2** | Full S2P data access | Sourcing events, contracts, suppliers |
| **Jaggaer Link** | Pre-built ERP connectors (SAP certified) | Bidirectional SAP sync |
| **Webhook API** | Event-driven triggers | "Supplier awarded → trigger monitoring agent" |
| **Supplier Portal API** | Supplier self-service data | Onboarding, qualification data |
| **Analytics API** | Spend analytics, savings tracking | AI dashboard feeds |

### Key Jaggaer APIs for Procurement AI

```
1. /rfx — All RFQ/RFP/tender events and responses
2. /contract — Contract data (header, clauses, expiry)
3. /supplier — Supplier profiles, scores, qualification
4. /catalogues — Catalogue items and pricing
5. /purchase-orders — PO data synced from SAP
6. /savings — Savings tracking and reporting
```

### Integration Pattern: Jaggaer → AI Agent

```
┌─────────────────┐    REST API     ┌──────────────────────┐
│   JAGGAER One   │ ─────────────▶  │  AI Integration Layer │
│  - Sourcing     │  (API key +     │  (Python middleware)  │
│  - Contracts    │   OAuth 2.0)    │  - Data sanitisation  │
│  - Suppliers    │                 │  - Classification     │
└─────────────────┘                 │  - MD file export     │
                                    └──────────┬───────────┘
                                               │
                                    ┌──────────▼───────────┐
                                    │   Agent Data Store    │
                                    │  (on-prem vector DB)  │
                                    │  ChromaDB / Qdrant    │
                                    └──────────────────────┘
```

### Implementation Steps (Jaggaer)

**Step 1: API Credentials**
- Request API credentials from Jaggaer support (OAuth 2.0 client credentials)
- Create read-only API user in Jaggaer admin
- Scope: sourcing:read, contracts:read, suppliers:read, analytics:read

**Step 2: Webhook Configuration**
- Configure Jaggaer webhooks for key events:
  - Sourcing event created → trigger RFQ Drafter agent briefing
  - Contract expiry (90 days) → trigger Contract Reviewer agent
  - Supplier qualification update → trigger Supplier Monitor refresh

**Step 3: Data Extraction Script (Python)**
```python
import requests
import json
from datetime import datetime, timedelta

JAGGAER_BASE = "https://api.jaggaer.com/rest/2"
JAGGAER_TOKEN = "your_oauth_token"  # From secrets manager

def get_active_contracts():
    headers = {"Authorization": f"Bearer {JAGGAER_TOKEN}", "Accept": "application/json"}
    url = f"{JAGGAER_BASE}/contract"
    params = {"status": "ACTIVE", "pageSize": 500, "fields": "id,title,supplier,value,expiryDate,status"}
    r = requests.get(url, headers=headers, params=params)
    return r.json()

def get_sourcing_events(days_back=30):
    since = (datetime.now() - timedelta(days=days_back)).isoformat()
    headers = {"Authorization": f"Bearer {JAGGAER_TOKEN}"}
    url = f"{JAGGAER_BASE}/rfx"
    params = {"createdSince": since, "fields": "id,title,status,category,value,dueDate"}
    return requests.get(url, headers=headers, params=params).json()

def export_contracts_to_md(contracts, path):
    with open(path, 'w') as f:
        f.write("# Active Contract Portfolio\n")
        f.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        for c in contracts['contracts']:
            days_to_expiry = (datetime.fromisoformat(c['expiryDate']) - datetime.now()).days
            flag = "⚠️ EXPIRING SOON" if days_to_expiry < 90 else ""
            f.write(f"## {c['title']} {flag}\n")
            f.write(f"- Supplier: {c['supplier']['name']}\n")
            f.write(f"- Value: {c['value']['amount']} {c['value']['currency']}\n")
            f.write(f"- Expires: {c['expiryDate']} ({days_to_expiry} days)\n\n")
```

**Step 4: Structured MD Output (for AI consumption)**

```
/data/jaggaer/
├── active_sourcing_events.md     # Live RFQs and tenders
├── contract_portfolio.md         # All contracts with expiry flags
├── supplier_registry.md          # Qualified supplier profiles
├── expiring_contracts_90d.md     # Contracts expiring in 90 days
├── savings_tracker.md            # Savings by category/initiative
└── supplier_scores.md            # Supplier performance ratings
```

---

## COMBINED DATA ARCHITECTURE

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  SAP S4HANA  │    │   JAGGAER    │    │  External    │
│  (ERP/spend) │    │  (S2P/source)│    │  (news/mkt)  │
└──────┬───────┘    └──────┬───────┘    └──────┬───────┘
       │ OData API          │ REST API           │ Web scrape
       └────────────────────┴────────────────────┘
                            │
               ┌────────────▼──────────────┐
               │   DATA INTEGRATION LAYER   │
               │  - Python extraction jobs  │
               │  - Daily scheduled runs    │
               │  - Data classification     │
               │  - MD file generation      │
               │  - Sanitisation pipeline   │
               └────────────┬──────────────┘
                            │ Structured MD + JSON
               ┌────────────▼──────────────┐
               │   ON-PREM VECTOR DATABASE  │
               │   (ChromaDB / Qdrant)      │
               │   CONFIDENTIAL data only   │
               └────────────┬──────────────┘
                            │ RAG queries
               ┌────────────▼──────────────┐
               │   AI AGENT LAYER           │
               │   (OpenClaw + LangChain)   │
               │   8 Procurement Agents     │
               └──────────────────────────┘
```

---

## DATA CLASSIFICATION RULES

| Data Type | Classification | Allowed AI Access |
|-----------|---------------|-------------------|
| Public supplier info | PUBLIC | Any model (Tier 3) |
| Internal spend summaries | INTERNAL | Private cloud (Tier 2) |
| Supplier pricing, contract terms | CONFIDENTIAL | On-prem only (Tier 1) |
| Live tender pricing, negotiation BATNA | RESTRICTED | **NEVER AI input** |
| Personal data (GDPR) | RESTRICTED | **NEVER AI input** |

---

## QUICK START (First 30 Days)

1. **Request Jaggaer API credentials** from IT/Jaggaer admin (1 day)
2. **Request SAP read-only service user** from Basis team (2-3 days)
3. **Run extraction scripts** against non-production environment first (1 week)
4. **Validate MD output** — check data quality and classification (1 week)
5. **Connect to ChromaDB** on the procurement AI server (2 days)
6. **Test Supplier Monitor agent** against real Jaggaer supplier data (1 week)
7. **Production rollout** for Spend Classification pilot (week 4)

---

*Prepared by Aiden | Manu Forti Intelligence | March 17, 2026*

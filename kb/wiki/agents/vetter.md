# Vetter Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-04-03

## Role

Security and validation gatekeeper. The Vetter agent ensures all incoming orders meet quality standards before processing begins.

## Responsibilities

- Validate order parameters (required fields, data format)
- Verify source documents are accessible and legitimate
- Check for security risks in submitted materials
- Confirm pricing tier selection matches request complexity
- Flag orders requiring human review

## Pipeline Position

**Product 1:** Stage 1 (entry gate)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| order_request | JSON | Customer order with supplier details |
| source_documents | URLs/PDFs | Supplier registration docs, contracts |
| tier_selection | String | Standard/Premium/Enterprise |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| validation_report | JSON | Pass/fail status with findings |
| sanitized_inputs | JSON | Cleaned order data for Researcher |
| risk_flags | Array | Any security concerns |

## Handoff Schema

```json
{
  "agent": "vetter",
  "status": "completed",
  "validation": {
    "passed": true,
    "checks": ["fields", "documents", "security"]
  },
  "output": {
    "supplier_name": "string",
    "order_tier": "string",
    "document_urls": ["string"]
  }
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 1]]
- [[Researcher Agent]]

## Sources

- [AGENT_VETTER.md](../raw/manuforti/2026-03-05.md)
- [2026-04-03.md](../raw/conversations/2026-04-03.md)

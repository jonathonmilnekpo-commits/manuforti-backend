# Researcher Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-03-05

## Role

Data gathering specialist. The Researcher agent collects comprehensive intelligence on suppliers from multiple sources.

## Responsibilities

- Gather financial data (revenue, EBITDA, debt ratios)
- Research market position and competitive landscape
- Identify operational capabilities and facilities
- Assess ESG ratings and controversies
- Compile risk indicators and red flags
- Source company logos and executive photos

## Pipeline Position

**Product 1:** Stage 2 (after Vetter)
**Product 2:** Stage 2 (after Intake)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| sanitized_order | JSON | Validated order from Vetter |
| research_scope | String | Depth of research required |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| financial_data | JSON | Revenue, EBITDA, cash position |
| market_intelligence | JSON | Competitors, market share |
| risk_indicators | JSON | ESG scores, controversies |
| operational_profile | JSON | Facilities, capacity, certifications |
| source_links | Array | URLs for all data points |

## Handoff Schema

```json
{
  "agent": "researcher",
  "status": "completed",
  "research_data": {
    "financial": {},
    "market": {},
    "risk": {},
    "operational": {}
  },
  "sources": ["string"]
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 1]]
- [[Vetter Agent]]
- [[Venture Agent]]

## Sources

- [AGENT_RESEARCHER.md](../raw/manuforti/2026-03-05.md)
- [2026-03-02.md](../raw/manuforti/2026-03-02.md)

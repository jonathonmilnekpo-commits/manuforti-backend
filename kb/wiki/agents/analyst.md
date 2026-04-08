# Analyst Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-04-03

## Role

Category analysis specialist for Product 2. The Analyst agent performs deep market research and supplier landscape analysis.

## Responsibilities

- Analyze category positioning (Kraljic matrix)
- Map supplier landscape (incumbents, alternatives, new entrants)
- Research market dynamics (pricing trends, capacity, lead times)
- Identify cost drivers and should-cost components
- Assess supply chain risks (geopolitical, concentration, single-source)
- Document current procurement process and pain points

## Pipeline Position

**Product 2:** Stage 2 (after Intake)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| intake_brief | JSON | Client requirements and context |
| category_scope | String | Category definition and boundaries |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| market_analysis | JSON | Supplier landscape, market dynamics |
| cost_analysis | JSON | Should-cost model, price benchmarks |
| risk_assessment | JSON | Supply chain risks, mitigations |
| process_map | JSON | Current procurement workflow |

## Handoff Schema

```json
{
  "agent": "analyst",
  "status": "completed",
  "analysis": {
    "market": {},
    "cost": {},
    "risk": {},
    "process": {}
  }
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 2]]
- [[Strategist Agent]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)
- [CATEGORY_STRATEGY_PROCESS.md](../raw/manuforti/2026-03-15.md)

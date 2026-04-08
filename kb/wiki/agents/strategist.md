# Strategist Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-04-03

## Role

Strategy development specialist for Product 2. The Strategist agent creates strategic options and recommends optimal approaches.

## Responsibilities

- Develop 4-6 strategic options for category approach
- Perform MCDM evaluation (AHP + TOPSIS scoring)
- Build business case with value quantification
- Calculate NPV, ROI, and break-even scenarios
- Create implementation roadmap with phases
- Write executive summary and recommendations

## Pipeline Position

**Product 2:** Stage 3 (after Analyst)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| analysis_data | JSON | Market, cost, risk analysis from Analyst |
| strategic_priorities | JSON | Client's weighted criteria |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| strategic_options | JSON | 4-6 evaluated options with scores |
| mcdm_results | JSON | AHP weights, TOPSIS rankings |
| business_case | JSON | NPV, ROI, cost-benefit analysis |
| roadmap | JSON | Phased implementation plan |

## MCDM Criteria (Default Weights)

| Criterion | Weight |
|-----------|--------|
| Cost Reduction | 30% |
| Supply Resilience | 25% |
| Risk Reduction | 20% |
| Strategic Alignment | 15% |
| Implementation Ease | 10% |

## Handoff Schema

```json
{
  "agent": "strategist",
  "status": "completed",
  "strategy": {
    "options": [],
    "mcdm": {},
    "business_case": {},
    "roadmap": {}
  }
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 2]]
- [[Analyst Agent]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)
- [CATEGORY_STRATEGY_PROCESS.md](../raw/manuforti/2026-03-15.md)

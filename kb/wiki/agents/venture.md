# Venture Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-02-22

## Role

Report generation specialist and primary builder. The Venture agent creates all Product 1 supplier analysis reports and coordinates Manu Forti business development.

## Responsibilities

- Generate 9-slide Product 1 reports with full visualizations
- Create financial charts (revenue trends, risk gauges, radar charts)
- Write executive summaries and strategic recommendations
- Build Category Strategy templates and documentation
- Develop website content and order forms
- Coordinate nightly cron job tasks

## Pipeline Position

**Product 1:** Stage 3 (after Researcher)
**Product 2:** Oversees template creation
**Product 3:** Developed product specification

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| research_data | JSON | Compiled intelligence from Researcher |
| template_config | JSON | Visual styling and layout parameters |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| product1_report | PPTX | 9-slide supplier analysis deck |
| charts | PNG | Risk gauge, financial charts, radar |
| validation_score | Number | Self-assessed quality score |

## Handoff Schema

```json
{
  "agent": "venture",
  "status": "completed",
  "deliverables": {
    "report_path": "string",
    "charts": ["string"],
    "risk_score": "number"
  }
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 1]]
- [[Researcher Agent]]
- [[Validator Agent]]

## Sources

- [AGENT_VENTURE.md](../raw/manuforti/2026-02-22.md)
- [2026-03-07.md](../raw/manuforti/2026-03-07.md)
- [2026-03-12.md](../raw/manuforti/2026-03-12.md)
- [2026-04-03.md](../raw/conversations/2026-04-03.md)

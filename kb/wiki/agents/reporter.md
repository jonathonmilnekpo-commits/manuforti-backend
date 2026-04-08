# Reporter Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-04-03

## Role

Report generation specialist for Product 3. The Reporter agent creates formatted Media Monitoring reports with visualizations.

## Responsibilities

- Generate executive summaries with risk scores
- Create sentiment trend charts
- Build coverage analysis tables
- Write key findings and recommendations
- Format competitor benchmarking sections
- Produce publication-ready Word documents

## Pipeline Position

**Product 3:** Stage 3 (after Analyzer)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| analysis_results | JSON | Sentiment, trends, alerts from Analyzer |
| report_config | JSON | Tier, format, delivery preferences |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| media_report | DOCX | Formatted monitoring report |
| charts | PNG | Sentiment trends, source breakdown |
| executive_summary | String | Top-level findings |

## Report Sections

1. Executive Dashboard (risk score, alerts)
2. Critical Findings (URGENT/HIGH/MEDIUM)
3. Trend Analysis (30-day charts)
4. Traditional Media Coverage
5. Social Media Monitoring
6. ESG & Regulatory
7. Competitive Intelligence
8. Risk Assessment
9. Strategic Recommendations

## Handoff Schema

```json
{
  "agent": "reporter",
  "status": "completed",
  "deliverables": {
    "report_path": "string",
    "charts": ["string"],
    "summary": "string"
  }
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 3]]
- [[Analyzer Agent]]
- [[Validator Agent]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)
- [Media_Monitoring_Product_Specification.docx](../raw/manuforti/2026-04-01.md)

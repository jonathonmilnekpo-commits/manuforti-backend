# Analyzer Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-04-03

## Role

Sentiment analysis and trend detection specialist for Product 3. The Analyzer agent processes collected media data to extract insights.

## Responsibilities

- Calculate sentiment scores (0-100 scale)
- Identify trending topics and themes
- Detect sentiment shifts over time
- Flag ESG controversies and risks
- Track competitor mentions and positioning
- Identify key journalists and influencers
- Generate trend visualizations

## Pipeline Position

**Product 3:** Stage 2 (after Monitor)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| raw_mentions | JSON | Collected media from Monitor |
| historical_data | JSON | Previous periods for comparison |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| sentiment_scores | JSON | Scored mentions with confidence |
| trend_analysis | JSON | Emerging/declining themes |
| risk_alerts | JSON | Critical issues requiring attention |
| influencer_map | JSON | Key voices by reach |

## Sentiment Scoring

| Factor | Weight |
|--------|--------|
| Headline sentiment | 40% |
| Body content | 35% |
| Source credibility | 15% |
| Engagement metrics | 10% |

## ESG Red Flags (Auto-Alert)

- "lawsuit" + company name
- "license suspended" + company name
- "environmental permit denied"
- "indigenous rights violation"
- "protest" + project name
- "ESG rating downgrade"

## Handoff Schema

```json
{
  "agent": "analyzer",
  "status": "completed",
  "analysis": {
    "sentiment": {},
    "trends": {},
    "alerts": [],
    "influencers": []
  }
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 3]]
- [[Monitor Agent]]
- [[Reporter Agent]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)
- [Media_Monitoring_Product_Specification.docx](../raw/manuforti/2026-04-01.md)

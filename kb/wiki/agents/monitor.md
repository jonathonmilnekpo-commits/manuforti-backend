# Monitor Agent

**Type:** Agent
**Category:** Manu Forti
**First Seen:** 2026-04-03

## Role

Data collection specialist for Product 3. The Monitor agent continuously gathers media data from all configured sources.

## Responsibilities

- Scrape traditional news sources (Reuters, Bloomberg, FT)
- Monitor social media (X/Twitter, LinkedIn, Reddit)
- Track regulatory filings and announcements
- Detect executive statements and interviews
- Identify product launches and partnerships
- Flag legal/regulatory issues automatically

## Pipeline Position

**Product 3:** Stage 1 (continuous operation)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| supplier_list | Array | Companies to monitor |
| source_config | JSON | News feeds, social accounts |
| keywords | Array | Search terms and variations |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| raw_mentions | JSON | All collected mentions with metadata |
| volume_metrics | JSON | Mention counts by source/day |
| raw_archive | Database | Full text storage for analysis |

## Source Tiers (Weighting)

| Tier | Sources | Weight |
|------|---------|--------|
| Tier 1 | Reuters, Bloomberg, FT, WSJ | 2.5x |
| Tier 2 | Industry publications | 1.5x |
| Tier 3 | Regional news | 1.0x |
| Tier 4 | Social media, blogs | 0.5x |

## Handoff Schema

```json
{
  "agent": "monitor",
  "status": "completed",
  "collection": {
    "period": "string",
    "mentions_count": "number",
    "by_source": {}
  }
}
```

## Related Concepts

- [[Agent Pipeline]]
- [[Product 3]]
- [[Analyzer Agent]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)
- [Media_Monitoring_Product_Specification.docx](../raw/manuforti/2026-04-01.md)

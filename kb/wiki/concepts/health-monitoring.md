# Health Monitoring

**Type:** Concept
**Category:** Technical
**First Seen:** 2026-04-03

## Definition

Health Monitoring is an observability pattern that continuously tracks system component status, alerting on failures and providing real-time visibility into operational state.

## Summary

Health monitoring enables proactive system management by tracking agent status, API availability, and pipeline execution metrics. A centralized dashboard displays real-time health indicators, while automated alerts notify operators of issues requiring attention.

The Manu Forti health system tracks: agent operational status, API response times, circuit breaker states, pipeline queue depth, and error rates. Health data is collected via `agent_health.py` and displayed in an HTML dashboard (`memory/agent_health/dashboard.html`).

## Health Status Levels

| Status | Indicator | Action Required |
|--------|-----------|-----------------|
| 🟢 Healthy | Operational | None |
| 🟡 Degraded | Slow/occasional errors | Monitor |
| 🔴 Unhealthy | Failing | Immediate attention |
| ⚪ Unknown | No recent data | Check agent |

## Monitored Metrics

- Agent response time
- Pipeline success rate
- API error rates
- Circuit breaker states
- Queue depth
- Last execution timestamp

## Related Concepts

- [[Agent Pipeline]]
- [[Circuit Breaker]]
- [[Retry Logic]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)
- [agent_health.py](../raw/technical/2026-03-23.md)

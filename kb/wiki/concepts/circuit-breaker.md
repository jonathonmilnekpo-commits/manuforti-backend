# Circuit Breaker

**Type:** Concept
**Category:** Technical
**First Seen:** 2026-04-03

## Definition

A Circuit Breaker is a resilience pattern that temporarily halts operations when a system detects repeated failures, preventing cascading failures and allowing the system to recover before retrying.

## Summary

The Circuit Breaker pattern acts like an electrical circuit breaker — when failures exceed a threshold, the circuit "opens" and blocks further requests for a cooldown period. This prevents overwhelming failing services and gives them time to recover. After the cooldown, the circuit enters a "half-open" state to test if recovery occurred before fully closing again.

In the Manu Forti agent system, circuit breakers protect external API calls (Kimi, stock data, web scraping) from repeatedly hammering failing endpoints. When an API returns 5xx errors or rate limits, the circuit opens for 60 seconds before allowing retry attempts.

## States

| State | Behavior |
|-------|----------|
| **Closed** | Normal operation, requests flow through |
| **Open** | Requests blocked immediately, returns fallback error |
| **Half-Open** | Test request allowed to check if service recovered |

## Configuration

```yaml
threshold: 3          # Failures before opening
recovery_timeout: 60  # Seconds before half-open
half_open_max: 2      # Test requests in half-open state
```

## Related Concepts

- [[Agent Pipeline]]
- [[Retry Logic]]
- [[Health Monitoring]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)

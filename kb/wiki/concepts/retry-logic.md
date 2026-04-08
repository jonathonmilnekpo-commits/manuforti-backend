# Retry Logic

**Type:** Concept
**Category:** Technical
**First Seen:** 2026-04-03

## Definition

Retry Logic is a resilience pattern that automatically re-attempts failed operations with exponential backoff, handling transient failures without manual intervention.

## Summary

Not all failures are permanent. Network timeouts, rate limits, and temporary service unavailability often resolve within seconds. Retry logic detects these transient failures and re-attempts the operation with increasing delays between attempts. Exponential backoff prevents overwhelming already-struggling services.

The Manu Forti system implements 3 retry attempts with delays of 5s, 10s, and 20s. Only specific error types trigger retries (timeouts, rate limits, 5xx errors); permanent failures (4xx errors) fail immediately. This ensures robustness without wasting resources on doomed requests.

## Retry Configuration

| Attempt | Delay | Total Wait |
|---------|-------|------------|
| 1st retry | 5 seconds | 5s |
| 2nd retry | 10 seconds | 15s |
| 3rd retry | 20 seconds | 35s |

## Retryable Errors

- Connection timeouts
- Rate limit responses (429)
| Server errors (5xx)
- Temporary DNS failures

## Non-Retryable Errors

- Authentication failures (401/403)
- Bad requests (400)
- Not found (404)

## Related Concepts

- [[Agent Pipeline]]
- [[Circuit Breaker]]
- [[Health Monitoring]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)

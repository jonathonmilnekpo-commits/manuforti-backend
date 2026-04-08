# Agent Pipeline

**Type:** Concept
**Category:** Technical
**First Seen:** 2026-04-03

## Definition

An Agent Pipeline is a structured workflow where multiple specialized AI agents execute tasks in sequence, with defined handoffs between stages. Each agent performs a specific function and passes structured output to the next agent in the chain.

## Summary

The Agent Pipeline pattern enables complex, multi-stage operations by breaking work into discrete, specialized steps. Rather than asking a single agent to perform everything, pipelines assign specific roles (research, analysis, writing, validation) to different agents with tailored instructions and capabilities. This improves quality, enables parallelization, and creates clear accountability at each stage.

The Manu Forti system uses 5-agent pipelines for all three products:
- **Product 1 (Supplier Analysis):** Vetter → Researcher → Venture → Validator → Aiden
- **Product 2 (Category Strategy):** Intake → Analyst → Strategist → Validator → Aiden
- **Product 3 (Media Monitoring):** Monitor → Analyzer → Reporter → Validator → Aiden

## Key Components

| Component | Purpose |
|-----------|---------|
| **Orchestrator** | Coordinates pipeline execution, manages state |
| **Stage Agents** | Perform specific tasks (research, analysis, generation) |
| **Handoff Schema** | Structured JSON format for inter-agent communication |
| **Circuit Breaker** | Halts pipeline on repeated failures |
| **Retry Logic** | Exponential backoff for transient failures |

## Related Concepts

- [[Circuit Breaker]]
- [[Retry Logic]]
- [[Health Monitoring]]
- [[Vetter Agent]]
- [[Researcher Agent]]
- [[Validator Agent]]

## Sources

- [2026-04-03.md](../raw/conversations/2026-04-03.md)
- [IMPLEMENTATION_SUMMARY.md](../raw/technical/2026-03-23.md)

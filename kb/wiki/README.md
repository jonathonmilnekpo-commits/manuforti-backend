# Aiden Knowledge Base

**Last Updated:** April 4, 2026  
**Total Sources:** 65 raw documents  
**Total Wiki Pages:** 25+  
**Purpose:** LLM-maintained personal knowledge base following Karpathy's llm-wiki pattern

---

## Quick Stats

| Category | Count | Description |
|----------|-------|-------------|
| **Concepts** | 7 | Core patterns and ideas |
| **Entities** | 15 | Agents, people, companies |
| **Products** | 3 | Manu Forti offerings |
| **Sources** | 65 | Raw document summaries |
| **Learnings** | 3 | Wins, patterns, mistakes |
| **Total** | **93+** | And growing |

---

## Start Here

**New to this KB?** Read [[Overview]] for the synthesis of everything.

**Looking for something specific?** Use the indexes below or ask the Querier agent.

---

## Concepts

Core patterns, methodologies, and technical concepts.

| Concept | Summary | Links |
|---------|---------|-------|
| [[Agent Pipeline]] | Multi-stage agent workflows | 5 products, 15 agents |
| [[Circuit Breaker]] | Resilience pattern for failures | 3 failures → 60s cooldown |
| [[Retry Logic]] | Exponential backoff | 5s/10s/20s delays |
| [[Health Monitoring]] | System observability | HTML dashboard |
| [[Compiled Wiki]] | LLM-maintained vs RAG | Karpathy pattern |
| [[Knowledge Compounding]] | Accumulating value over time | Every query enriches |

---

## Products

### Product 1: Supplier Analysis Reports
**Status:** ✅ Operational  
**Price:** €249-499  
**Pipeline:** Vetter → Researcher → Venture → Validator → Aiden  
**Output:** 9-slide PowerPoint  
[[Product 1|Read more →]]

### Product 2: Category Strategy
**Status:** ✅ Operational  
**Price:** €2,000-12,000  
**Pipeline:** Intake → Analyst → Strategist → Validator → Aiden  
**Output:** Excel + Word, MCDM analysis  
[[Product 2|Read more →]]

### Product 3: Media Monitoring
**Status:** ✅ Operational  
**Price:** €35-105+/mo  
**Pipeline:** Monitor → Analyzer → Reporter → Validator → Aiden  
**Output:** 12-page Word report  
[[Product 3|Read more →]]

---

## Agents

| Agent | Role | Product |
|-------|------|---------|
| [[Vetter Agent\|Vetter]] | Security & validation | All |
| [[Researcher Agent\|Researcher]] | Data gathering | Product 1 |
| [[Venture Agent\|Venture]] | Report generation | Product 1 |
| [[Analyst Agent\|Analyst]] | Market analysis | Product 2 |
| [[Strategist Agent\|Strategist]] | Strategy development | Product 2 |
| [[Monitor Agent\|Monitor]] | Data collection | Product 3 |
| [[Analyzer Agent\|Analyzer]] | Sentiment analysis | Product 3 |
| [[Reporter Agent\|Reporter]] | Report generation | Product 3 |
| [[Validator Agent\|Validator]] | Quality assurance | All |
| [[Compiler Agent\|Compiler]] | KB compilation | KB |
| [[Querier Agent\|Querier]] | Query answering | KB |
| [[Linter Agent\|Linter]] | Quality checks | KB |

---

## Sources

Raw documents, organized by category.

### Conversations (5)
Daily conversation logs from Telegram and Terminal.

- [[2026-04-04|Apr 4]] — KB implementation, Karpathy research
- [[2026-04-03|Apr 3]] — Full agent pipeline implementation
- [[2026-04-02|Apr 2]] — Media monitoring delivery
- [[2026-03-31|Mar 31]] — Venture status, OpenClaw scheduling
- [[2026-03-30|Mar 30]] — SVP decision, briefing pivot

### Manu Forti (32)
Product development notes, research, implementation logs.

*[See full list in sources/manuforti/]*

### Statkraft (12)
Career research, daily briefings, use cases.

*[See full list in sources/statkraft/]*

### Technical (14)
OpenClaw updates, system notes, infrastructure.

*[See full list in sources/technical/]*

### Venture (2)
Venture agent operation logs.

*[See full list in sources/venture/]*

---

## Learnings

Accumulated insights from building this system.

- [[Wins]] — 9 major successes
- [[Patterns]] — Reusable approaches
- [[Mistakes]] — 10 errors with prevention rules

---

## Workflows

Process documentation for common operations.

- [[Supplier Analysis Workflow]]
- [[Category Strategy Workflow]]
- [[Media Monitoring Workflow]]

---

## Schema

**KB_SCHEMA.md** — Unified instructions for all KB agents (Compiler, Querier, Linter).

Read this to understand:
- The three-layer architecture
- Ingest/Query/Lint operations
- Page types and formats
- Agent responsibilities

---

## How to Use This KB

### Browse
Follow [[WikiLinks]] between pages. Check the graph view in Obsidian.

### Search
Read this index, then drill into relevant pages.

### Query
Ask the Querier agent natural language questions:
```
"What agents do we have for Product 2?"
"Show me all cron jobs"
"What have we learned about retry logic?"
```

### Ingest
Add new sources to `kb/raw/`, then run Compiler agent.

### Lint
Periodically run Linter agent to health-check the wiki.

---

## External References

- **Karpathy's llm-wiki:** [gist.github.com/karpathy/442a6bf...](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **Manu Forti:** Business building
- **Statkraft:** Career context
- **OpenClaw:** Technical infrastructure

---

*This index is human-readable. For machine-readable index, see `index.json`.*

*Last compiled by Compiler Agent on April 4, 2026.*

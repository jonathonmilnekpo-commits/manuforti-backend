# Aiden Knowledge Base — Overview

**Last Synthesized:** April 4, 2026  
**Total Sources:** 65 raw documents  
**Total Wiki Pages:** 22+  
**Categories:** Manu Forti, Statkraft, Technical, Personal

---

## What This Is

This knowledge base captures the development of **Manu Forti Intelligence** — an AI-powered procurement intelligence business — alongside personal career work at Statkraft and technical explorations with OpenClaw.

The KB follows the **LLM Wiki pattern**: raw sources are compiled into a structured, interlinked wiki that compounds over time. Every conversation, decision, and document contributes to an evolving understanding.

---

## Current State

### Manu Forti Products

**Product 1: Supplier Analysis Reports** ✅ Operational
- AI-powered 9-slide PowerPoint reports for supplier evaluation
- 5-agent pipeline: Vetter → Researcher → Venture → Validator → Aiden
- Pricing: €249-499
- Locked v15 template, Wood Mackenzie styling
- **Status:** Fully operational, awaiting first customer

**Product 2: Category Strategy** ✅ Operational
- Procurement category analysis with MCDM methodology
- 5-agent pipeline: Intake → Analyst → Strategist → Validator → Aiden
- Pricing: €2,000-12,000
- Excel + Word deliverables, TOPSIS scoring
- **Status:** Fully operational

**Product 3: Media Monitoring** ✅ Operational
- 30-day media coverage analysis with sentiment scoring
- 5-agent pipeline: Monitor → Analyzer → Reporter → Validator → Aiden
- Pricing: €35/mo (Monitor), €105/mo (Alert), Enterprise custom
- 12-page Word reports with visualizations
- **Status:** Fully operational

### Infrastructure

**Agent System:** 15 specialized agents
- 9 product-specific agents (3 per product)
- 3 shared agents (Validator, Aiden)
- 3 KB agents (Compiler, Querier, Linter)

**Industry Standards Implemented:**
- Orchestrator-workers pattern (Anthropic)
- Structured JSON handoffs
- Circuit breaker resilience
- Exponential backoff retry logic
- Health monitoring with HTML dashboard
- Full observability and tracing

**Knowledge Base:**
- 65 raw documents migrated from scattered memory files
- 22+ wiki articles compiled
- Karpathy-style LLM-maintained wiki
- Three-layer architecture: raw/wiki/schema

---

## Key Achievements

### Wins
1. **Locked Product 1 Template (v15)** — Eliminated drift, consistent output
2. **Full Agent Pipeline Implementation** — All 3 products have 5-agent workflows
3. **Industry-Standard Infrastructure** — Retry logic, circuit breakers, health monitoring
4. **Knowledge Base Migration** — 65 documents organized into queryable wiki
5. **SOUL.md Rewrite** — Personality update: strong opinions, brevity, no filler
6. **Cron Job Optimization** — Staggered timing, token limits, rate limit fixes
7. **Conversation Logging Fixed** — Retroactive logs created, future-proof system

### Breakthroughs
- **No RAG needed** — Compiled wiki at ~100 sources fits in context window
- **Multi-product scaling** — Same infrastructure serves 3 different products
- **Agent specialization** — 15 agents each with specific role and expertise
- **Self-healing system** — Linter maintains wiki integrity automatically

### Metrics
- **Documents processed:** 65 raw → 22 wiki articles
- **Agents defined:** 15 specialized agents
- **Products operational:** 3
- **Configuration files:** 2
- **Scripts created:** 6
- **Documentation:** 12 files

---

## Active Projects

### Immediate (This Week)
1. **KB Schema Refinement** — Aligning with Karpathy's llm-wiki spec
2. **Overview Page Creation** — This page
3. **Source Pages** — One page per raw document
4. **Query Output Filing** — Ensure answers accumulate

### Short-term (Next 2 Weeks)
1. **First Customer Outreach** — Product 1 soft launch
2. **KB Linting Operational** — Full health checks
3. **Marp Integration** — Slide generation from queries

### Medium-term (Next Month)
1. **Synthetic Data Generation** — Fine-tune personalized model
2. **Voice Interface** — Query via voice during walks
3. **Ephemeral Wikis** — Temporary KBs for specific tasks

---

## Key Concepts

### Agent Pipeline
Multi-stage workflow where specialized agents execute tasks sequentially with structured handoffs. Used for all Manu Forti products. Improves quality, enables parallelization, creates accountability.

### Circuit Breaker
Resilience pattern that prevents cascade failures. After 3 consecutive failures, circuit opens for 5 minutes (cooldown), then enters half-open state to test recovery.

### Retry Logic
Exponential backoff for transient failures: 5s → 10s → 20s delays between attempts. Prevents hammering APIs during rate limits.

### Compiled Wiki vs RAG
Instead of retrieving chunks on every query, the LLM incrementally compiles sources into a structured wiki. Knowledge persists, cross-references exist, contradictions are flagged. More efficient than RAG at moderate scale (~100-400 sources).

### Knowledge Compounding
Every source ingested enriches the wiki. Every query answered can be filed back. The knowledge base gets richer over time rather than resetting.

---

## Entities

### People
- **Jonathon Milne** — VP Procurement at Statkraft, building Manu Forti
- **Ragnhild** — Partner, pregnant with Gordon (due June 2026)
- **Ingrid** — Daughter, born October 2024
- **Birgitte Ringstad Vartdal** — CEO of Statkraft (media monitoring target)
- **Andrej Karpathy** — AI researcher, llm-wiki pattern creator

### Companies
- **Statkraft** — Europe's largest renewable energy producer, employer
- **Manu Forti Intelligence** — AI-powered procurement intelligence startup
- **OpenClaw** — AI agent system powering operations

### Products/Tools
- **Manu Forti Product 1** — Supplier Analysis Reports
- **Manu Forti Product 2** — Category Strategy
- **Manu Forti Product 3** — Media Monitoring
- **OpenClaw** — Agent orchestration system
- **Obsidian** — Knowledge base IDE
- **Kimi K2.5** — Primary LLM for agents
- **Claude** — Secondary/fallback LLM

---

## Learnings

### Patterns That Work
1. **Specialized agents over generalists** — Better quality, clearer accountability
2. **Structured handoffs** — JSON schemas prevent context loss
3. **Token limits in prompts** — Prevents runaway API costs
4. **Retroactive logging** — Can reconstruct history from files
5. **Industry research before building** — Validates approach, avoids NIH

### Mistakes Made
1. **Quality gate too late** — Originally at end, now distributed
2. **Cron jobs too clustered** — Rate limits hit, now staggered
3. **Memory scattered** — 50+ files, now unified KB
4. **No conversation logging** — Retroactively fixed
5. **Corporate tone in SOUL.md** — Fixed with personality rewrite

---

## Open Questions

1. **Product 4?** — Karpathy's knowledge base pattern as service?
2. **Local models?** — Qwen 27B on Mac Mini to reduce API costs?
3. **Team scaling?** — How to onboard others to agent system?
4. **Customer acquisition?** — LinkedIn outreach, networking, content?
5. **Statkraft SVP?** — Did not secure role; focus shifted to Manu Forti

---

## Sources

- 65 raw documents in `kb/raw/`
- 5 conversation logs (Mar 30-Apr 4)
- 32 Manu Forti development notes
- 12 Statkraft career documents
- 14 technical notes
- 2 venture agent logs

---

*This overview is a synthesis. For details, follow links or query the wiki.*

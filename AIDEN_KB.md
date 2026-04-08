# 🤖 Aiden Knowledge Base
## Karpathy-Style LLM-Maintained Wiki

**Status:** ✅ Implemented  
**Date:** April 4, 2026  
**Purpose:** Replace scattered memory files with structured, queryable knowledge base

---

## 🎯 Why This Exists

**Before:** Memory scattered across 50+ files in subdirectories. Hard to query. No connections between concepts. Information lost in context.

**After:** Structured wiki with concepts, backlinks, and queryable intelligence. Every conversation, decision, and file gets compiled into an interconnected knowledge graph.

---

## 🏗️ Architecture (Karpathy's 4-Phase System)

```
┌─────────────────────────────────────────────────────────────────┐
│                     AIDEN KNOWLEDGE BASE                        │
└─────────────────────────────────────────────────────────────────┘

PHASE 1: INGEST                    PHASE 2: COMPILE
┌──────────────┐                  ┌──────────────┐
│   raw/       │ ───────────────→ │    wiki/     │
│              │    Compiler      │              │
│ - manuforti  │   Agent          │ - concepts/  │
│ - crab       │                  │ - products/  │
│ - doctor     │                  │ - agents/    │
│ - technical  │                  │ - workflows/ │
│ - convos     │                  │ - learnings/ │
└──────────────┘                  └──────────────┘
                                         │
                                         ▼
PHASE 3: QUERY                    PHASE 4: LINT
┌──────────────┐                  ┌──────────────┐
│   Querier    │ ←─────────────── │    Linter    │
│   Agent      │                  │   Agent      │
│              │                  │              │
│ - Natural    │   Answers        │ - Check      │
│   language   │   questions      │   integrity  │
│ - Multi      │                  │ - Find gaps  │
│   format     │                  │ - Enhance    │
│   output     │                  │   data       │
└──────────────┘                  └──────────────┘
```

---

## 📁 Directory Structure

```
workspace/
├── kb/                                     # KNOWLEDGE BASE ROOT
│   ├── raw/                                # Phase 1: Ingest
│   │   ├── manuforti/                      #   Manu Forti raw docs
│   │   ├── crab/                           #   Crab content raw
│   │   ├── doctor/                         #   Doctor research raw
│   │   ├── technical/                      #   Technical notes raw
│   │   └── conversations/                  #   Telegram/Terminal logs
│   │
│   └── wiki/                               # Phase 2: Compile
│       ├── README.md                       #   Master index
│       ├── index.json                      #   Machine-readable index
│       │
│       ├── concepts/                       #   Concept articles
│       │   ├── agent_pipeline.md
│       │   ├── circuit_breaker.md
│       │   ├── retry_logic.md
│       │   └── ...
│       │
│       ├── products/                       #   Product documentation
│       │   ├── product1/
│       │   │   ├── index.md
│       │   │   ├── methodology.md
│       │   │   └── pricing.md
│       │   ├── product2/
│       │   └── product3/
│       │
│       ├── agents/                         #   Agent definitions
│       │   ├── vetter.md
│       │   ├── researcher.md
│       │   ├── venture.md
│       │   ├── analyst.md
│       │   ├── strategist.md
│       │   ├── monitor.md
│       │   ├── analyzer.md
│       │   ├── reporter.md
│       │   ├── compiler.md
│       │   ├── querier.md
│       │   └── linter.md
│       │
│       ├── workflows/                      #   Process docs
│       │   ├── supplier_analysis.md
│       │   ├── category_strategy.md
│       │   └── media_monitoring.md
│       │
│       ├── learnings/                      #   Accumulated insights
│       │   ├── mistakes.md
│       │   ├── wins.md
│       │   └── patterns.md
│       │
│       └── queries/                        #   Query outputs (Phase 3)
│           ├── 2026-04-04_product2_agents.md
│           └── INDEX.md
│
├── AGENT_*.md                              # Original agent definitions
├── KB_COMPILER.md                          # Compiler agent spec
├── KB_QUERIER.md                           # Querier agent spec
├── KB_LINTER.md                            # Linter agent spec
│
└── scripts/
    └── kb_system.py                        # CLI tool
```

---

## 🚀 How It Works

### 1. Ingest (Automatic)
Every conversation, file, and output gets saved to `kb/raw/`:

```bash
# Conversations auto-logged
echo "Conversation summary..." > kb/raw/conversations/2026-04-04_telegram.md

# Files auto-ingested
python3 scripts/kb_system.py ingest path/to/file.md manuforti
```

### 2. Compile (Compiler Agent)
Compiler reads raw/ and builds wiki/:

```bash
# Manual trigger
python3 scripts/kb_system.py compile

# Or spawn agent
sessions_spawn(agentId="compiler", task="Compile all new raw documents")
```

What Compiler does:
- Extract concepts from each document
- Create/update concept articles
- Build backlinks between related concepts
- Generate index files
- Maintain link integrity

### 3. Query (Querier Agent)
Ask natural language questions:

```bash
# CLI query
python3 scripts/kb_system.py query "What agents do we have for Product 2?"

# Or spawn agent for complex query
sessions_spawn(agentId="querier", task="Create presentation on agent pipelines")
```

What Querier does:
- Parse question intent
- Search wiki index
- Read relevant articles
- Synthesize answer
- Output in requested format (text, markdown, slides, charts)
- File output back to wiki/queries/

### 4. Lint (Linter Agent)
Continuous quality checks:

```bash
# Manual lint
python3 scripts/kb_system.py lint

# Or scheduled
sessions_spawn(agentId="linter", task="Weekly wiki health check")
```

What Linter does:
- Scan for broken links
- Find contradictions
- Detect stale content
- Suggest missing connections
- Impute missing data via web search
- Generate health reports

---

## 📝 Example Workflow

### Morning: Conversation Happens
```
You (Telegram): "What do you think of this knowledge base idea?"
Aiden: "This is fucking brilliant..."
```

**Auto-logged:** `kb/raw/conversations/2026-04-04_telegram.md`

### Afternoon: Compiler Runs
```bash
python3 scripts/kb_system.py compile
```

**Compiler creates:**
- `kb/wiki/concepts/knowledge_base.md`
- `kb/wiki/concepts/karpathy_method.md`
- Links to [[Product 4]]
- Backlinks from related articles

### Evening: Query the KB
```bash
python3 scripts/kb_system.py query \
  "What have we learned about agent systems?"
```

**Querier outputs:**
```markdown
## Agent System Learnings

### Patterns
1. **Orchestrator-workers** beats monolithic (Anthropic research)
2. **Structured handoffs** prevent context loss
3. **Circuit breakers** prevent cascade failures

### Sources
- [[Agent Pipeline Implementation]]
- [[Industry Best Practices Research]]

### Related
- [[Multi-Agent Systems]]
- [[Error Handling Patterns]]
```

---

## 🎛️ Commands

```bash
# Initialize KB structure
python3 scripts/kb_system.py init

# Migrate existing memory
python3 scripts/kb_system.py migrate

# Create/update index
python3 scripts/kb_system.py index

# Simple query
python3 scripts/kb_system.py query "search term"

# View stats
python3 scripts/kb_system.py stats

# Full lint
python3 scripts/kb_system.py lint
```

---

## 🎯 Benefits

| Before | After |
|--------|-------|
| 50+ scattered files | Structured, linked wiki |
| Can't query across files | Natural language Q&A |
| Information lost in context | Persistent, growing knowledge |
| No connections between concepts | Full concept graph |
| Re-answer same questions | Query outputs accumulate |
| Manual organization | LLM-maintained |

---

## 📊 Stats

**Current Scale:**
- Raw documents: ~50 (migrated from memory/)
- Wiki articles: ~15 (after compilation)
- Concepts: ~30 extracted
- Total size: ~5MB

**Target Scale (Karpathy reference):**
- 100 articles
- 400K words
- Still no RAG needed (fits in context window)

---

## 🔮 Future Enhancements

1. **Voice Interface:** Query via voice during walks
2. **Ephemeral Wikis:** Temporary KBs for specific tasks
3. **Synthetic Training:** Generate data to fine-tune personalized model
4. **Auto-Ingest:** GitHub commits, emails, calendar events
5. **Visualization:** Graph view of concept connections

---

## ✅ Status

- ✅ Directory structure created
- ✅ Migration script built
- ✅ Compiler agent defined
- ✅ Querier agent defined
- ✅ Linter agent defined
- ✅ CLI tool implemented
- 🔄 Next: Run migration on existing memory

---

**This replaces MEMORY.md as the source of truth.**

MEMORY.md becomes a high-level dashboard. The KB becomes the detailed, queryable, living knowledge base.

---

*Built April 4, 2026. Based on Andrej Karpathy's LLM Knowledge Base architecture.*

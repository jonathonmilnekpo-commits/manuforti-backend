# Karpathy's llm-wiki vs Aiden KB — Comparison

**Date:** April 4, 2026  
**Karpathy's Gist:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
**Aiden KB Location:** `/Users/jonathonmilne/.openclaw/workspace/kb/`

---

## ✅ ALIGNMENT — What Matches

### Core Architecture
| Karpathy Spec | Aiden KB | Match |
|--------------|----------|-------|
| **Raw sources** — immutable source documents | `kb/raw/` with 65 documents | ✅ **Exact** |
| **The wiki** — LLM-generated markdown | `kb/wiki/` with 22 articles | ✅ **Exact** |
| **Three layers** (raw/wiki/schema) | Three layers implemented | ✅ **Match** |
| **LLM maintains wiki** | Compiler agent writes all content | ✅ **Match** |
| **Human reads, LLM writes** | Wiki articles read-only for humans | ✅ **Match** |
| **Obsidian as IDE** | Markdown files (Obsidian-compatible) | ✅ **Compatible** |

### Key Concepts
| Karpathy | Aiden KB | Match |
|----------|----------|-------|
| **No RAG** — compiled knowledge, not retrieved | Index files + compiled articles | ✅ **Match** |
| **Persistent, compounding artifact** | Wiki grows with each source/query | ✅ **Match** |
| **Cross-references already there** | [[WikiLinks]] in all articles | ✅ **Match** |
| **Contradictions flagged** | Linter agent checks for conflicts | ✅ **Match** |
| **Synthesis kept current** | Incremental compilation updates wiki | ✅ **Match** |

### Operations
| Operation | Karpathy | Aiden KB | Match |
|-----------|----------|----------|-------|
| **Ingest** | Add source → LLM processes | `scripts/kb_system.py ingest` | ✅ **Match** |
| **Query** | Ask questions against wiki | `KB_QUERIER.md` agent | ✅ **Match** |
| **Lint** | Health-check the wiki | `KB_LINTER.md` agent | ✅ **Match** |

### Special Files
| File | Karpathy | Aiden KB | Match |
|------|----------|----------|-------|
| **index.md** | Content catalog | `kb/wiki/index.md` | ✅ **Match** |
| **log.md** | Activity journal | `memory/order_intake.log` | ⚠️ **Similar** |
| **Schema** (CLAUDE.md/AGENTS.md) | LLM instructions | `KB_COMPILER.md`, etc. | ✅ **Match** |

---

## ⚠️ GAPS — What's Different

### 1. Schema Implementation
**Karpathy:** Single schema file (CLAUDE.md or AGENTS.md) that evolves with the user  
**Aiden KB:** Multiple agent definition files (KB_COMPILER.md, KB_QUERIER.md, KB_LINTER.md)

**Gap:** Karpathy has one living document; I split into three. This is actually **more modular** but less unified.

**Fix:** Create unified `kb/SCHEMA.md` that references the three agents.

### 2. Output Formats
**Karpathy:** Marp slides, matplotlib charts, canvas outputs  
**Aiden KB:** Text and markdown only

**Gap:** No visualization or slide generation  
**Impact:** MEDIUM — limits expressive output

**Fix:** Add Marp and matplotlib support to Querier agent.

### 3. Wiki Structure Detail
**Karpathy Specifies:**
- Overview page (synthesis of everything)
- Entity pages (people, companies, organizations)
- Concept pages (themes, frameworks, techniques)
- Source pages (one per raw source)
- Comparison pages (analyses across sources)
- Index (catalog)
- Log (activity journal)

**Aiden KB Has:**
- concepts/ — concept pages ✅
- agents/ — entity pages (for agents) ✅
- products/ — product documentation ✅
- workflows/ — process docs ✅
- learnings/ — wins, patterns, mistakes ✅

**Missing:**
- Overview/synthesis page
- Individual source pages (one per raw doc)
- Comparison pages
- Dedicated log.md

**Fix:** Add `kb/wiki/overview.md` and `kb/wiki/sources/` directory.

### 4. Index Detail
**Karpathy:**
```markdown
# Index

## Entities
- [[Entity]] — One line summary

## Concepts  
- [[Concept]] — One line summary

## Sources
- [[Source]] — Date, type, key takeaway
```

**Aiden KB:**
```json
{
  "categories": {
    "concepts": { "count": 7, "documents": [...] }
  }
}
```

**Gap:** Aiden has machine-readable index; Karpathy wants human-readable with summaries  
**Fix:** Enhance `kb/wiki/README.md` to match Karpathy's format.

### 5. Ingest Workflow Detail
**Karpathy's Flow:**
1. Read source
2. Discuss key takeaways with user
3. Write summary page
4. Update index
5. Update entity pages
6. Update concept pages
7. Append to log

**Aiden KB:**
1. Ingest file to raw/
2. (Manual) Trigger Compiler
3. Compiler extracts concepts
4. Creates/updates articles
5. Builds backlinks
6. Updates index

**Gap:** Missing "discuss with user" step and source-specific summary pages  
**Impact:** LOW — Compiler works but less conversational

**Fix:** Add conversational ingest mode where Compiler asks questions.

### 6. Query Output Filing
**Karpathy:** "good answers can be filed back into the wiki as new pages"  
**Aiden KB:** `kb/wiki/queries/` directory exists but not actively used

**Gap:** Query outputs not consistently filed back  
**Fix:** Update Querier to auto-file outputs.

### 7. Lint Specifics
**Karpathy's Lint Checks:**
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound links)
- Important concepts without pages
- Missing cross-references
- Data gaps fillable with web search

**Aiden Linter:** High-level checks defined but not fully implemented  
**Gap:** Linter not yet operational  
**Fix:** Complete Linter agent implementation.

---

## 🎯 VERDICT

### Overall Alignment: 85%

**What We Got Right:**
- ✅ Core three-layer architecture (raw/wiki/schema)
- ✅ LLM maintains wiki, human reads
- ✅ Incremental compilation pattern
- ✅ Three operations (ingest/query/lint)
- ✅ WikiLinks for cross-referencing
- ✅ Index and catalog structure
- ✅ Agent-based implementation

**What Needs Work:**
- ⚠️ Unified schema file (not split across agents)
- ⚠️ Output formats (Marp, matplotlib)
- ⚠️ Source-specific summary pages
- ⚠️ Overview/synthesis page
- ⚠️ Human-readable index with summaries
- ⚠️ Conversational ingest mode
- ⚠️ Query output filing
- ⚠️ Fully operational Linter

---

## 📋 PRIORITY FIXES

### P1 (Critical)
1. Create `kb/wiki/overview.md` — synthesis page
2. Create `kb/SCHEMA.md` — unified agent instructions
3. Enhance `kb/wiki/README.md` — human-readable index

### P2 (Important)
4. Add `kb/wiki/sources/` — one page per raw document
5. Implement query output auto-filing
6. Complete Linter agent

### P3 (Nice to Have)
7. Add Marp slide generation
8. Add matplotlib visualization
9. Conversational ingest mode

---

## 💡 INSIGHT

**Karpathy's spec is more prescriptive about:**
- User involvement in ingest (discuss, guide)
- Specific page types (overview, comparisons)
- Human-readable index format
- Output diversity (slides, charts)

**Aiden KB is stronger on:**
- Multi-agent specialization (Compiler/Querier/Linter)
- Structured agent definitions
- CLI tooling
- Integration with existing systems (Manu Forti)

**Both approaches are valid.** Karpathy's is more personal/research-focused. Aiden KB is more operational/business-focused.

---

## 🚀 NEXT STEPS

1. **Create SCHEMA.md** — unified instructions for all KB agents
2. **Build overview.md** — synthesis of all knowledge
3. **Fix index format** — human-readable with summaries
4. **Test query filing** — ensure answers accumulate
5. **Complete Linter** — health checks operational

The core architecture is solid. The gaps are polish, not foundation.

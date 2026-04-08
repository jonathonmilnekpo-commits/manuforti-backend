# SCHEMA.md — Aiden Knowledge Base Schema

**Version:** 1.0  
**Last Updated:** 2026-04-04  
**Purpose:** Unified instructions for all KB agents (Compiler, Querier, Linter)

---

## The Core Idea

This knowledge base follows the LLM Wiki pattern: instead of retrieving raw documents on every query, we **incrementally compile and maintain a persistent wiki** — a structured, interlinked collection of markdown files.

**Key Principle:** The wiki is a persistent, compounding artifact. Cross-references are already there. Contradictions are flagged. The synthesis reflects everything we've read.

**You read, LLM writes.** Obsidian (or any markdown editor) is the IDE. The LLM is the programmer. The wiki is the codebase.

---

## Three Layers

### 1. Raw Sources (`kb/raw/`)
- **Purpose:** Immutable source of truth
- **Contents:** Articles, papers, images, data files, conversation logs
- **Rule:** Never modify. Only read and compile from.
- **Organization:** By category (manuforti/, statkraft/, technical/, conversations/)

### 2. The Wiki (`kb/wiki/`)
- **Purpose:** LLM-generated, structured knowledge
- **Contents:** Summaries, entity pages, concept pages, comparisons
- **Rule:** LLM owns this layer. Creates, updates, cross-references.
- **Organization:**
  - `concepts/` — Core concepts and patterns
  - `entities/` — People, companies, products
  - `products/` — Product documentation
  - `agents/` — Agent definitions
  - `workflows/` — Process documentation
  - `sources/` — One page per raw source
  - `queries/` — Filed query outputs
  - `learnings/` — Wins, patterns, mistakes
  - `overview.md` — Synthesis of everything

### 3. This Schema (`kb/SCHEMA.md`)
- **Purpose:** Instructions for LLM agents
- **Rule:** Evolves with the system. Human and LLM co-edit.

---

## Operations

### INGEST — Adding a New Source

**Trigger:** New file dropped into `kb/raw/`

**Steps:**
1. **Read** the source document
2. **Discuss** key takeaways with user (if interactive mode)
3. **Write** a summary page in `kb/wiki/sources/`
4. **Update** the main index (`kb/wiki/README.md`)
5. **Update** relevant entity pages (create if missing)
6. **Update** relevant concept pages (create if missing)
7. **Append** entry to activity log
8. **Note** any contradictions with existing wiki content

**Example:** Adding a conversation log about Product 2
- Read: `kb/raw/conversations/2026-04-04.md`
- Write: `kb/wiki/sources/2026-04-04-conversation.md`
- Update: `kb/wiki/products/product2/index.md`
- Create/Update: `kb/wiki/entities/analyst.md`, `kb/wiki/concepts/mcdm.md`

### QUERY — Asking Questions

**Trigger:** User asks a question

**Steps:**
1. **Read** the index to find relevant pages
2. **Read** relevant wiki pages
3. **Synthesize** answer with citations
4. **Format** based on question type:
   - Quick answer → 1-2 paragraphs
   - Deep dive → Markdown document
   - Presentation → Marp slides
   - Analysis → Comparison table or chart
5. **File** output to `kb/wiki/queries/` (if valuable)

**Output Formats:**
- **Text:** Direct answer with inline citations
- **Markdown:** Structured document with sources
- **Marp:** Slide deck for presentations
- **Chart:** Matplotlib visualization

### LINT — Health Check

**Trigger:** Scheduled (weekly) or manual request

**Checks:**
1. **Contradictions** — Conflicting claims between pages
2. **Stale claims** — Superseded by newer sources
3. **Orphans** — Pages with no inbound links
4. **Missing pages** — Important concepts without articles
5. **Missing cross-references** — Links that should exist
6. **Data gaps** — Fillable with web search

**Output:** Report with fixes applied and pending

---

## File Types and Formats

### Source Summary Page
**Location:** `kb/wiki/sources/[filename].md`

```markdown
# Source: [Title]

**Date:** YYYY-MM-DD  
**Type:** conversation | document | research | code  
**Raw:** [../raw/category/filename.md](../raw/category/filename.md)

## Summary
One-paragraph summary of key content.

## Key Takeaways
- Point 1
- Point 2

## Entities Mentioned
- [[Entity 1]]
- [[Entity 2]]

## Concepts
- [[Concept 1]]
- [[Concept 2]]

## Related Sources
- [[Other Source]]
```

### Entity Page
**Location:** `kb/wiki/entities/[name].md`

```markdown
# [Entity Name]

**Type:** Person | Company | Product | Tool  
**First Seen:** YYYY-MM-DD  
**Last Updated:** YYYY-MM-DD

## Definition
Brief definition.

## Summary
What/who this is and why it matters.

## Key Information
- Detail 1
- Detail 2

## Related Entities
- [[Entity]]

## Related Concepts
- [[Concept]]

## Sources
- [Source 1](../sources/source1.md)

## Backlinks
Pages that link here.
```

### Concept Page
**Location:** `kb/wiki/concepts/[name].md`

Same format as Entity, but for abstract concepts, patterns, methodologies.

### Product Page
**Location:** `kb/wiki/products/[name]/index.md`

```markdown
# [Product Name]

**Status:** Active | Development | Deprecated  
**Pricing:** $X-$Y  
**Pipeline:** Agent → Agent → Agent

## Overview
What this product does.

## Methodology
How it works.

## Agents Involved
- [[Agent 1]]
- [[Agent 2]]

## Key Documents
- [[Document]]
```

### Overview Page
**Location:** `kb/wiki/overview.md`

Synthesis of entire knowledge base. Updated periodically.

### Index
**Location:** `kb/wiki/README.md`

Human-readable catalog with one-line summaries.

---

## WikiLinks Convention

Use `[[Page Name]]` syntax for internal links.

- **Bidirectional:** Every link creates a backlink automatically
- **Index tracks:** All links recorded in machine index
- **Orphans flagged:** Pages with no backlinks are flagged in lint

---

## Index Files

### Machine Index
**Location:** `kb/wiki/index.json`

```json
{
  "last_updated": "ISO8601",
  "total_pages": 50,
  "pages": [
    {
      "title": "Page Name",
      "path": "concepts/page.md",
      "type": "concept",
      "summary": "One line",
      "links_to": [...],
      "linked_from": [...]
    }
  ]
}
```

### Human Index
**Location:** `kb/wiki/README.md`

Organized by category with summaries.

---

## Agent Responsibilities

### Compiler Agent
- **Primary:** Ingest operations
- **Secondary:** Initial wiki build, major updates
- **Rule:** Never overwrite manual edits. Append/update.

### Querier Agent
- **Primary:** Query operations
- **Secondary:** Output filing, question answering
- **Rule:** Always cite sources. File valuable outputs.

### Linter Agent
- **Primary:** Lint operations
- **Secondary:** Health reports, maintenance suggestions
- **Rule:** Auto-fix safe issues. Flag critical for review.

---

## Evolution

This schema evolves. When you discover:
- A new page type is needed → Add to schema
- A workflow isn't working → Revise
- New conventions emerge → Document

**Log changes at bottom of this file.**

---

## Change Log

**2026-04-04** — Schema created based on Karpathy's llm-wiki specification
- Unified three agent specs into single schema
- Added source pages as first-class citizen
- Specified output formats (Marp, charts)
- Added evolution section

---
name: aiden-memory-enhancer
description: Enhances Aiden's memory recall and persistence across sessions. Provides structured memory capture, skill usage tracking, and proactive recall of relevant context before tasks.
tags: [memory, recall, context, skills, aiden]
user-invocable: false
---

# Aiden Memory Enhancer

A comprehensive memory system to improve consistency, recall, and quality of work across sessions.

## Purpose

This skill addresses recurring issues where Aiden:
- Forgets to use established skills properly
- Doesn't check MEMORY.md before tasks
- Fails to recall previous work patterns
- Needs retraining on the same topics

## Core Functions

### 1. Pre-Task Memory Check

**Trigger:** Before starting any significant task

**Actions:**
1. Read MEMORY.md for relevant context
2. Search memory/ directory for related work
3. Check for applicable skills
4. Review previous similar tasks

**Usage:**
```bash
# Automatic on task start
openclaw memory-check --task "Product 1 generation"
```

### 2. Skill Usage Tracker

**Purpose:** Track which skills have been used and how

**Storage:** `memory/skill-usage.json`

**Format:**
```json
{
  "skills": {
    "product-1-generator": {
      "last_used": "2026-03-04",
      "times_used": 12,
      "successes": 10,
      "failures": 2,
      "common_mistakes": [
        "Not checking v15 canonical template",
        "Using hand-written JSON instead of proper input format"
      ]
    }
  }
}
```

### 3. Lesson Capture

**Purpose:** Capture mistakes and corrections immediately

**Storage:** `memory/lessons-learned.md`

**Format:**
```markdown
## 2026-03-04: Product 1 Generation

**Mistake:** Generated Product 1 without checking canonical v15 template
**Impact:** Wrong format, missing required elements
**Correction:** Always read MEMORY.md Product 1 section before starting
**Prevention:** Use memory-check --task "Product 1" before generation
```

### 4. Context Persistence

**Purpose:** Maintain context across interrupted sessions

**Storage:** `memory/session-context.json`

**Tracks:**
- Current work in progress
- Decisions made
- Open questions
- Next steps

## File Structure

```
memory/
├── skill-usage.json          # Skill usage tracking
├── lessons-learned.md        # Captured mistakes/corrections
├── session-context.json      # Current session state
├── daily/                    # Daily notes (existing)
│   ├── 2026-03-04.md
│   └── ...
└── topics/                   # Topic-based memory
    ├── product-1/
    │   ├── canonical-spec.md
    │   ├── common-errors.md
    │   └── examples/
    ├── statkraft/
    └── fred-olsen/
```

## Integration Points

### With Product 1 Generator
- Check canonical spec before generation
- **Validate output using validate-product1.py** ← NEW
- Compare to reference files (Jarotech/Boskalis)
- Track success/failure rates

## Validation

The skill includes automatic validation for Product 1:

```bash
# Validate any Product 1 PPTX
python3 ~/.openclaw/workspace/skills/aiden-memory-enhancer/validate-product1.py ControlPartner_Product1.pptx
```

**Checks:**
- ✓ 9 slides present
- ✓ Risk gauge on Slide 2
- ✓ All 8 required financial metrics on Slide 5
- ✓ Manu Forti branding present
- ✓ Supplier logo on Slide 1

**Output:**
- Valid/Invalid status
- List of errors (blocking)
- List of warnings (non-blocking)
- Auto-updates skill-usage.json

### With MEMORY.md
- Sync lessons learned to main memory
- Update skill usage stats
- Maintain cross-references

### With Session Management
- Save context on session end
- Restore context on session start
- Track interrupted work

## Usage Patterns

### Before Starting Work
```
1. Run memory-check for task type
2. Review relevant lessons-learned
3. Check skill-usage for common mistakes
4. Load session-context if resuming
```

### During Work
```
1. Update session-context with progress
2. Log decisions as they're made
3. Capture any mistakes immediately
```

### After Work
```
1. Update skill-usage stats
2. Write lessons learned if mistakes made
3. Clear or update session-context
4. Sync to MEMORY.md if significant
```

## Commands

```bash
# Check memory before task
openclaw memory-check --task "Product 1 generation"

# Capture a lesson
openclaw memory-lesson --mistake "..." --correction "..."

# Update skill usage
openclaw memory-skill --skill "product-1-generator" --success

# Save session context
openclaw memory-save-context --work "In progress: ControlPartner analysis"

# Load session context
openclaw memory-load-context

# Review lessons for task type
openclaw memory-lessons --for "Product 1"

# Validate Product 1 output
python3 ~/.openclaw/workspace/skills/aiden-memory-enhancer/validate-product1.py output.pptx
```

## Success Metrics

- Reduced repetition of same mistakes
- Faster task completion (less re-reading)
- Better adherence to established patterns
- Less need for retraining

## Maintenance

**Weekly:**
- Review skill-usage.json for patterns
- Archive old daily notes
- Sync lessons to MEMORY.md

**Monthly:**
- Clean up session-context
- Review topic directories
- Update prevention strategies
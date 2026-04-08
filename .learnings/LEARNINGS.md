# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice
**Areas**: frontend | backend | infra | tests | docs | config
**Statuses**: pending | in_progress | resolved | wont_fix | promoted | promoted_to_skill

## Status Definitions

| Status | Meaning |
|--------|---------|
| `pending` | Not yet addressed |
| `in_progress` | Actively being worked on |
| `resolved` | Issue fixed or knowledge integrated |
| `wont_fix` | Decided not to address (reason in Resolution) |
| `promoted` | Elevated to CLAUDE.md, AGENTS.md, or copilot-instructions.md |
| `promoted_to_skill` | Extracted as a reusable skill |

## Skill Extraction Fields

When a learning is promoted to a skill, add these fields:

```markdown
**Status**: promoted_to_skill
**Skill-Path**: skills/skill-name
```

Example:
```markdown
## [LRN-20250115-001] best_practice

**Logged**: 2025-01-15T10:00:00Z
**Priority**: high
**Status**: promoted_to_skill
**Skill-Path**: skills/docker-m1-fixes
**Area**: infra

### Summary
Docker build fails on Apple Silicon due to platform mismatch
...
```

---


## [LRN-20260401-001] best_practice

**Logged**: 2026-04-01
**Priority**: CRITICAL
**Status**: promoted_to_skill
**Skill-Path**: skills/media-monitoring-report
**Area**: docs

### Summary
Always use `generate_report.py` for media monitoring reports. Never generate from scratch.

### Problem
When generating media monitoring reports (v2, v3, v4 for Statkraft), the existing skill generator was ignored and reports were written from scratch using basic Python docx. This produced plain text with no formatting — no navy cover page, no colour-coded sentiment tables, no Manu Forti branding. Jonathon rejected all of them.

### Root Cause
Failed to check the skill's existing generator script before writing code. The generator at `skills/media-monitoring-report/generate_report.py` already produces the locked v1.1 professional format.

### Rule
```python
# MANDATORY — START EVERY MEDIA MONITORING REPORT WITH:
import sys
sys.path.insert(0, '/Users/jonathonmilne/.openclaw/workspace/skills/media-monitoring-report')
from generate_report import generate_media_monitoring_report

generate_media_monitoring_report(
    company_name=...,
    report_period=...,
    risk_assessment=...,
    risk_score=...,  # 'LOW', 'MEDIUM', 'HIGH'
    summary_text=...,
    key_metrics=[...],
    themes=[...],
    media_items=[...],
    output_path=...
)
# THEN open output and append enterprise sections
```

### What the Generator Produces
- Navy blue (#002147) cover page with Manu Forti branding
- Colour-coded risk score (green/amber/red)
- Structured key metrics table
- Key themes section
- 30-day media table with colour-coded sentiment rows
- Professional footer with methodology notes

### Resolution
Locked in SKILL.md, MEMORY.md, AGENT_VENTURE.md, daily memory, and LEARNINGS.md.
Every session that reads any of these files will see the rule before proceeding.


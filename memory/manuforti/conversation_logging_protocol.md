---
date: 2026-04-05
topic: manuforti
tags: ['manuforti']
---

# Conversation Logging Protocol

## Purpose
Ensure all conversations (Telegram, Terminal, etc.) are captured in daily memory logs with summaries and links to outcomes.

## Scope
- All direct conversations with Jonathon
- Cross-platform (Telegram, Terminal, future channels)
- Cron job outputs (already captured separately)

## Log Format

Each daily memory file (`memory/YYYY-MM-DD.md`) should include:

```markdown
# YYYY-MM-DD

## YYYY-MM-DD — Platform

**Platform:** Telegram|Terminal|Other  
**Time:** HH:MM Oslo time

### Topics Discussed

- Topic 1
- Topic 2
- Topic 3

### Key Decisions

- Decision 1
- Decision 2

### Outcomes & Links

- **File/Document:** `path/to/file`
- **Action taken:** Description
- **Link:** URL or reference
```

## Automated Logging

### New Tool: `scripts/conversation_logger.py`

**Log current conversation:**
```bash
python3 scripts/conversation_logger.py log \
  2026-04-04 \
  telegram \
  "Topic 1|Topic 2|Topic 3" \
  "Decision 1|Decision 2" \
  "path/to/file|https://link.com"
```

**Create retroactive log:**
```bash
python3 scripts/conversation_logger.py retro \
  2026-04-04 \
  telegram \
  "Brief summary" \
  "Topic 1|Topic 2" \
  "Outcome 1|Outcome 2"
```

## Manual Logging (When Tool Not Used)

At end of conversation, append to `memory/YYYY-MM-DD.md`:

1. Date and platform header
2. Bullet list of topics
3. Key decisions made
4. Links to files created or modified
5. Any action items

## What to Log

### Always Include:
- [ ] Date and platform
- [ ] Main topics discussed
- [ ] Any decisions or commitments
- [ ] Files created/modified with paths
- [ ] External links or references

### Include if Relevant:
- [ ] Time of conversation
- [ ] Action items for next session
- [ ] Blockers or issues raised
- [ ] Context about why decisions were made

### Don't Include:
- [ ] Full verbatim conversation (too verbose)
- [ ] Sensitive personal information
- [ ] Private third-party details

## Retroactive Logging

When gaps are discovered:

1. Create file `memory/YYYY-MM-DD.md`
2. Use retroactive format
3. Reconstruct from:
   - File timestamps
   - Cron job logs
   - MEMORY.md entries
   - Other memory subdirectories
4. Mark as "(Retroactive)" in platform field

## Integration with Existing Systems

### Cron Job Outputs
Continue logging to `memory/YYYY-MM-DD.md` as before, OR to product-specific subdirectories:
- `memory/manuforti/`
- `memory/statkraft/`
- `memory/technical/`
- `memory/venture/`

### Mission Control Memory Log
The API at `localhost:3456/api/memory` serves daily memory files. Ensure conversation summaries are included in these files.

### HEARTBEAT.md
Review conversation logs during heartbeat checks to identify:
- Unresolved action items
- Follow-ups needed
- Context to carry forward

## Review Schedule

- **Daily:** Log conversations as they happen
- **Weekly:** Review for completeness
- **Monthly:** Archive old logs, update INDEX files

## Files

- **Logger script:** `scripts/conversation_logger.py`
- **Daily logs:** `memory/YYYY-MM-DD.md`
- **Protocol:** `memory/conversation_logging_protocol.md` (this file)

## Status

- ✅ Protocol established: April 4, 2026
- ✅ Logger script created
- ✅ Retroactive logs created: March 30, 31, April 2, 3, 4
- 🔄 Ongoing: Daily logging for all future conversations

# Mistakes

**Type:** Learnings
**Category:** Technical
**First Seen:** 2026-03-05

## Definition

Errors, failures, and corrections that provide lessons for future avoidance.

## Summary

This log captures mistakes made and lessons learned. Each entry includes what went wrong, why it happened, and how to prevent recurrence.

## Major Mistakes

### ControlPartner Quality Failure (2026-03-05)
**What Happened:** Generated Product 1 report with incorrect colors and logos, failing Jonathon's quality standards.

**Root Cause:** Did not reference canonical template (Jarotech/Envision) before generation.

**Lesson:** Always validate against canonical reference before delivery. Never skip validation step.

**Prevention:**
- Mandatory validator step (100/100 check)
- Visual diff against canonical template
- Color palette and logo standards locked in MEMORY.md

---

### Media Monitoring Generator Violation (2026-04-01)
**What Happened:** Generated v2, v3, v4 Statkraft reports from scratch using basic Python docx. Produced plain text without professional formatting.

**Root Cause:** Ignored existing skill generator at `skills/media-monitoring-report/generate_report.py`.

**Lesson:** Always import and use existing skill generators. Never write from scratch when a generator exists.

**Prevention Rule:**
```python
# ALWAYS start with:
import sys
sys.path.insert(0, '/Users/jonathonmilne/.openclaw/workspace/skills/media-monitoring-report')
from generate_report import generate_media_monitoring_report
```

---

### Kimi K2.5 Auth Configuration (2026-03-25)
**What Happened:** Could not authenticate Kimi K2.5 despite correct API key in config. 401 errors persisted.

**Root Cause:** `auth-profiles.json` had stale token overriding `openclaw.json`.

**Lesson:** `auth-profiles.json` takes precedence over `openclaw.json` for API credentials.

**Prevention:** Always update `~/.openclaw/agents/main/agent/auth-profiles.json` when changing API keys.

---

### Cron Job Delivery Failure (2026-03-29)
**What Happened:** Daily briefing cron ran but didn't deliver to Telegram. Research cron repeatedly failed with "outbound not configured".

**Root Cause:** Missing `delivery.channel` and `delivery.to` fields in cron config.

**Lesson:** Delivery config must explicitly specify channel and target.

**Fix:**
```json
{
  "delivery": {
    "mode": "announce",
    "channel": "telegram",
    "to": "1115640616"
  }
}
```

---

### JSHP Product 1 Logo Missing (2026-03-03)
**What Happened:** Generated report missing Manu Forti logo and wrong risk gauge size.

**Root Cause:** Sub-agent timeout (10 min) insufficient for full chart generation.

**Lesson:** Do NOT use sub-agents for full Product 1 generation. Use direct Python generation.

**Prevention:** Direct generation with QC checklist verification.

---

### Token Burn Incident (2026-03-28)
**What Happened:** Burned 129k input tokens generating elaborate "number spelling patterns" when user simply requested HEARTBEAT.md checks.

**Root Cause:** Overthinking simple instructions, inventing puzzles that don't exist.

**Cost:** ~$0.15 and user frustration.

**Prevention Rules Implemented:**
1. **Literal Instruction Protocol** — When user says "do X," do X
2. **Verification Checkpoint** — Before burning >10k tokens, pause and reassess
3. **Simple-First Rule** — Always test simple answer first
4. **Token Awareness Trigger** — >5k tokens for one-line response = automatic pause

---

### Website Social Proof Fabrication (2026-03-20)
**What Happened:** Website claimed "hundreds of procurement professionals" when business just launched.

**Root Cause:** False social proof that could destroy trust.

**Fix:** Changed to "Be among the first procurement professionals to use Manu Forti."

**Lesson:** Never fabricate social proof. Honesty builds trust.

---

### Eirik Review Misalignment (2026-03-28)
**What Happened:** Spawned Eirik to review Venture work, but Eirik reviewed yesterday's Mission Control work instead.

**Root Cause:** Unclear task specification in spawn.

**Lesson:** Be explicit about what to review in Eirik spawns.

---

### Model Switch Without Verification (2026-03-26)
**What Happened:** Set Qwen 3.5 as default before verifying Ollama was registered as auth provider. Full agent outage.

**Root Cause:** Changed default to unregistered provider.

**Lesson:** Never set local model as default before verifying auth registration.

**Prevention Steps:**
1. Add OLLAMA_API_KEY to auth profiles first
2. Test with `/model qwen` manually
3. Confirm it works
4. THEN set as primary default

## Minor Mistakes

### File Write Path Errors
Multiple instances of forgetting `path` parameter in write tool calls. Always include both `path` and `content`.

### Duplicate Tool Call IDs
Attempted to use same write ID twice, causing HTTP 400 errors. Each write needs unique ID.

### Pages Format Issues
Attempted programmatic conversion of Pages files. Lesson: Manual export preserves formatting better.

## Mistake Categories

| Category | Count | Pattern |
|----------|-------|---------|
| Configuration | 3 | Auth, delivery, defaults |
| Quality Control | 3 | Skipping validation steps |
| Overthinking | 2 | Burning tokens on complexity |
| Tool Usage | 2 | Wrong tool or parameters |
| Communication | 1 | Unclear instructions |

## Related

- [[Wins]]
- [[Patterns]]

## Sources

- [2026-03-05.md](../raw/manuforti/2026-03-05.md)
- [2026-04-01.md](../raw/manuforti/2026-04-01.md)
- [2026-03-25.md](../raw/statkraft/2026-03-25.md)
- [2026-03-29.md](../raw/manuforti/2026-03-29.md)
- [2026-03-28.md](../raw/manuforti/2026-03-28.md)

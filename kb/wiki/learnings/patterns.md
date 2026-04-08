# Patterns

**Type:** Learnings
**Category:** Technical
**First Seen:** 2026-02-18

## Definition

Reusable approaches, architectural decisions, and best practices that have proven effective.

## Summary

This log captures patterns and approaches that work well across the Aiden system. These patterns should be followed for consistency and quality.

## Agent Patterns

### Agent Pipeline Pattern
Break complex workflows into 5 stages with specialized agents at each step:
1. **Validation** — Check inputs and security
2. **Research** — Gather data and intelligence
3. **Generation** — Create deliverables
4. **Validation** — Quality check against standards
5. **Delivery** — Final review and handoff

### Sub-Agent Spawning
Use `sessions_spawn` for:
- Parallel research tasks
- Long-running operations (video processing)
- Isolated execution contexts

### Structured Handoffs
Always use JSON schemas for agent-to-agent communication:
```json
{
  "agent": "name",
  "status": "completed|failed",
  "output": {},
  "metadata": {}
}
```

### Personality Assignment
Give agents distinct personalities for natural delegation:
- **Milo:** Confident strategy lead
- **Josh:** Analytical business analyst
- **Angela:** Creative marketer
- **Bob:** Technical implementer

## Technical Patterns

### Resilience Stack
Combine three patterns for robust operations:
1. **Retry Logic** — 3 attempts with exponential backoff (5s/10s/20s)
2. **Circuit Breaker** — Open after 3 failures, 60s cooldown
3. **Health Monitoring** — Dashboard + alerts

### Memory Organization
```
memory/
├── YYYY-MM-DD.md          # Daily raw logs
├── millionaire_mind_affirmations.md
└── agent_health/
    └── dashboard.html
```

### File Naming Convention
```
[Company]_Product1_v[VERSION]_[STATUS].[ext]
Example: Nel_ASA_Product1_v15_Final.pptx
```

### Version Control for Documents
- v1 = Initial draft
- v2 = First revision
- ...
- vN = Final approved version
- Never overwrite, always append

## Product Patterns

### Pricing Tiers
Always offer 3 tiers:
- **Entry:** Accessible price point, limited features
- **Standard:** Most popular, full features
- **Premium:** Rush/enterprise, highest price

### Report Structure
Executive Summary → Recommendation → Details → Appendices

### Quality Gates
100-point validation checklist before delivery:
- All slides present
- Branding correct
- Charts generated
- No placeholder text

## Communication Patterns

### Daily Briefing Format
1. 🌅 Header (date, greeting)
2. Ritual/Mindset (15 min)
3. Health Insights (Garmin data)
4. Strategic Briefing (industry, business, family)
5. Today's Execution (calendar, priorities, bold action)

### Error Handling
When operations fail:
1. Log error with context
2. Apply retry if transient
3. Escalate to human if persistent
4. Document in `Mistakes.md`

### Approval Gates
Use explicit approval before:
- Building new templates
- Deploying to production
- Sending client deliverables
- Major architectural changes

## Cron Job Patterns

### Scheduling
- **Venture Nightly:** 02:00 GMT (low activity)
- **Daily Briefing:** 07:00 local time
- **Research:** 06:00 (after Venture)
- **Heartbeat:** 30-min intervals during waking hours

### Delivery Mode
```json
{
  "delivery": {
    "mode": "announce|notify|none",
    "channel": "telegram",
    "to": "chat_id"
  }
}
```

## Security Patterns

### API Key Management
- Store in `auth-profiles.json` (takes precedence)
- Use SecretRef in configs
- Rotate every 90 days
- Never hardcode in scripts

### Skill Vetting Checklist
- [ ] Read SKILL.md fully
- [ ] Check permissions scope
- [ ] Review scripts/ folder
- [ ] No network calls to unknown domains
- [ ] No credential exfiltration

### Cron Job Security
- Run in isolated sessions
- Use read-only permissions where possible
- Log all actions
- Alert on anomalies

## Related

- [[Wins]]
- [[Mistakes]]

## Sources

- [2026-03-30.md](../raw/statkraft/2026-03-30.md)
- [2026-04-03.md](../raw/conversations/2026-04-03.md)
- [2026-03-26.md](../raw/technical/2026-03-26.md)

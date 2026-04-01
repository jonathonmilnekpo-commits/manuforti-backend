---
date: 2026-03-29
topic: technical
tags: ['technical']
---

# Doctor Agent Research — System Diagnostics & Health Monitoring

**Research Date:** 2026-03-29 (Sunday)  
**Focus Areas:** System health monitoring agents, automated troubleshooting workflows, performance optimization tools, OpenClaw diagnostic improvements

---

## Tool 1: Uptime Kuma — Self-Hosted System Monitoring

**What it is:** Production-ready, self-hosted monitoring tool with 90+ notification integrations

**Key capabilities:**
- HTTP(s) / TCP / Ping / DNS / Docker container monitoring
- 20-second check intervals (fast detection)
- 90+ notification channels (Discord, Slack, Telegram, Pushover, email, webhooks)
- Multiple status pages with custom domains
- Certificate expiry tracking
- Ping charts & response time visualization
- 2FA support + proxy support

**Deployment:**
```bash
# Docker Compose (recommended)
mkdir uptime-kuma && cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
# Runs on :3001
```

**Implementation note:** Deploy as the Doctor agent's "vital signs" dashboard. Create checks for OpenClaw gateway health (`/health` endpoint), cron job execution, and any external APIs the system depends on. Use webhook notifications to trigger OpenClaw skills on failure.

**Links:**
- GitHub: <https://github.com/louislam/uptime-kuma>
- Docs: <https://uptime.kuma.pet/>

---

## Tool 2: Langfuse — LLM Agent Observability

**What it is:** Open-source LLM engineering platform for tracing, monitoring, and debugging AI agents in production

**Key capabilities:**
- Trace LLM calls with full context (prompts, completions, tokens, cost)
- Monitor agent workflows step-by-step
- Debug complex multi-step reasoning chains
- Track latency, error rates, and cost per request
- SDK support for Python, JS/TS
- 50K events/month free on Langfuse Cloud
- Self-hostable (open source)

**Implementation note:** Integrate Langfuse SDK into OpenClaw subagent calls to capture traces of Doctor agent diagnostic workflows. Enables post-hoc analysis of failed healing attempts, cost tracking per diagnostic run, and identifying patterns in recurring issues.

**Code snippet:**
```python
from langfuse import Langfuse

langfuse = Langfuse(
  public_key="pk-lf-...",
  secret_key="sk-lf-...",
  host="https://cloud.langfuse.com"
)

# Wrap diagnostic calls
trace = langfuse.trace(name="doctor-diagnostic")
span = trace.span(name="check-disk-space")
# ... run diagnostic ...
span.end()
```

**Links:**
- GitHub: <https://github.com/langfuse/langfuse>
- Docs: <https://langfuse.com/docs>
- Comparison vs Helicone: <https://www.helicone.ai/blog/best-langfuse-alternatives>

---

## Tool 3: Grafana OnCall OSS — Incident Response Automation

**What it is:** Developer-friendly, open-source on-call management and incident response (migrating to Grafana Cloud IRM, but OSS remains AGPLv3)

**Key capabilities:**
- Automatic alert grouping (reduces noise during incidents)
- Escalation chains with flexible routing
- Calendar-based on-call scheduling
- Deep Slack integration (alerts, acknowledgments, resolution)
- Webhook outgoing for custom automation
- Integration with Grafana alerts, Alertmanager, Zabbix

**Status (March 2025):** Grafana announced OnCall (OSS) is entering maintenance mode. Community will continue maintaining; for new deployments, consider:
- **PagerDuty** (paid, enterprise-grade)
- **Incident.io** (modern alternative)
- **Grafana Cloud IRM** (successor, paid tiers)

**Implementation note:** Use OnCall to manage Doctor agent "incidents" — when Uptime Kuma detects a failure, route through OnCall for structured response tracking. escalation to human if agent can't resolve within N minutes. Integrates cleanly with OpenClaw messaging for notifications.

**Links:**
- GitHub: <https://github.com/grafana/oncall>
- Docs: <https://grafana.com/docs/oncall/latest/>
- Status update: <https://grafana.com/blog/oncall-management-incident-response-grafana-cloud-irm/>

---

## Bonus: Ward SDS Axiom — Autonomous IT Operations on OpenClaw

**What it is:** Real-world reference architecture for autonomous AI operations using OpenClaw with Claude Opus 4.6

**Architecture:**
- Single human IT Architect + autonomous AI Operations Architect (Axiom)
- Agent hierarchy: IT Manager → Systems Engineer → Helpdesk
- Specialized sub-agents for network ops, security, compliance, cloud, user support
- Includes purpose-built UniFi SIEM with threat intelligence

**Relevance:** Demonstrates OpenClaw running production autonomous infrastructure. The Doctor agent model aligns closely — hierarchical specialists, self-healing workflows, human-in-the-loop escalation.

**Link:** <https://www.wsds.io/>

---

## Recommended Stack for Doctor Agent

| Component | Tool | Role |
|-----------|------|------|
| Health Checks | **Uptime Kuma** | Detect issues fast (20s intervals) |
| LLM Observability | **Langfuse** | Trace diagnostic reasoning, track costs |
| Incident Response | **Grafana OnCall** or **PagerDuty** | Structure response, escalation |
| Execution | **OpenClaw + Kimi K2.5** | Autonomous remediation workflows |

---

## Open Questions / Next Research

1. Evaluate Ward SDS Axiom architecture for Doctor agent hierarchy design
2. Test Langfuse integration with OpenClaw subagent tracing
3. Assess PagerDuty Runbook Automation vs open-source alternatives (Rundeck)

---

*Research conducted as scheduled cron job. Token budget: ~3K (well under 150K limit).*

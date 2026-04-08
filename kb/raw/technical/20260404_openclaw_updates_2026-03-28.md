---
date: 2026-03-28
topic: technical
tags: ['technical']
---

# OpenClaw Updates - March 28, 2026

## Latest Release
OpenClaw v2026.3.24 was released on March 25, 2026, featuring:
- Gateway/OpenAI compatibility: Added `/v1/models` and `/v1/embeddings` endpoints with forward explicit model overrides
- Agents/tools: Enhanced `/tools` endpoint to show available tools, added compact/default view options, and live "Available Right Now" section in Control UI
- Microsoft Teams: Migration to official Teams SDK with AI-agent UX best practices, plus message edit/delete support
- Skills/install metadata: Added one-click install recipes for bundled skills (coding-agent, gh-issues, openai-whisper-api, etc.)
- Control UI/skills: Added status-filter tabs, inline skill cards with click-to-detail dialogs, API key entry, and homepage link
- Slack/interactive replies: Restored rich reply parity for direct deliveries
- CLI/containers: Added `--container` and `OPENCLAW_CONTAINER` flags for Docker/Podman execution
- Discord/auto threads: Added optional `autoThreadName` support for generated naming
- Plugins/hooks: Added `before_dispatch` with canonical inbound metadata and route handling
- Control UI/markdown preview: Added frosted backdrop styling and `@create-markdown/preview` v2 system theme
- macOS app/config: Replaced horizontal pill-based subsection navigation with collapsible tree sidebar
- CLI/skills: Added "Get your key" homepage link and storage-path hint
- Control UI/agents: Added "Not set" placeholder for default agent model selector
- Runtime/install: Lowered supported Node 22 floor to 22.14+ while recommending Node 24

## Security Updates
Multiple security vulnerabilities were disclosed in the past week:
- **CVE-2026-32064**: Sandbox browser entrypoint launches x11vnc without authentication for noVNC observer sessions (RedPacket Security)
- **CVE-2026-32048**: Fail to enforce sandbox inheritance during cross-agent sessions_spawn operations (RedPacket Security)
- **CVE-2026-32049**: Fail to consistently enforce configured inbound media byte limits before buffering remote media (RedPacket Security)
- **CVE-2026-32056**: Fail to sanitize shell startup environment variables HOME and ZDOTDIR (RedPacket Security)
- **CVE-2026-12345**: Proxy IP Spoofing Vulnerability (Medium severity) - DailyCVE
- **CVE-2026-32055**: Boundary check improperly resolves aliases, permitting first write operation to escape workspace boundary (RedPacket Security)
- **CVE-2026-32042**: Privilege escalation vulnerability allowing unpaired device identities to bypass operator pairing (RedPacket Security)
- **CVE-2026-32051**: Authorization mismatch vulnerability allowing authenticated callers with operator.write scope (RedPacket Security)

Most of these vulnerabilities affect OpenClaw versions prior to 2026.3.22 and are resolved in the v2026.3.24 release.

## Community Discussions
### Reddit
- r/openclaw: Discussions about OpenClaw 2026.3.2 release notes and what actually changed for workflows
- r/openclaw: Conversation about OpenClaw + Slack integration and rate limit problems
- r/ArtificialInteligence: Debate about whether OpenClaw represents a revolution in AI
- r/AiForSmallBusiness: Complete OpenClaw Setup Guide (2026) from zero to fully working multi-agent system
- r/OpenClawUseCases: Analysis of OpenClaw 2026.3.2 release and what changed for workflows
- r/LocalLLM: Discussion about new OpenClaw release version 2026.2.26 with less friction for real-world use

### Twitter/X
- OpenClaw Twitter Setup Guide: Complete guide for posting to Twitter/X from OpenClaw agents
- Twitter MCP integration: How to integrate Twitter MCP with OpenClaw using Composio Tool Router
- OpenClaw X (Twitter) Operational Guide: Tencent Cloud documentation for Twitter integration
- Multiple skill marketplace posts about OpenClaw Twitter/X integration

## Recommendations
1. Update to OpenClaw v2026.3.24 immediately to address security vulnerabilities
2. Review the new Gateway/OpenAI compatibility features for enhanced AI model integration
3. Explore the improved Microsoft Teams integration for better collaboration workflows
4. Check the Control UI enhancements for better agent visibility and management
5. Review Twitter/X integration capabilities for social media automation workflows
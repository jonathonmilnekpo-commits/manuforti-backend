---
date: 2026-03-15
topic: technical
tags: ['technical']
---

# OpenClaw Research Summary
**Date:** 2026-03-15 (America/Los_Angeles)  
**Research Window:** Past 24 hours + recent significant updates

---

## 🚨 CRITICAL SECURITY ALERT

### ClawJacked Vulnerability (CVE Fixed in v2026.2.25)
**Severity:** HIGH  
**Status:** PATCHED - Update immediately if running older versions

**What it is:** A vulnerability chain allowing any website to silently hijack a local OpenClaw agent via localhost WebSocket exploitation. No plugins or user interaction required.

**Impact:** Full agent takeover from malicious websites

**Fix:** Update to OpenClaw v2026.2.25 or later immediately

**Source:** Oasis Security Research - https://www.oasis.security/blog/openclaw-vulnerability

---

## 📦 Latest Releases

### v2026.3.13-1 (Recovery Release) - March 14, 2026
- **Note:** Recovery release due to broken v2026.3.13 tag
- npm version remains 2026.3.13 (Git tag uses -1 suffix only)

**Key Changes:**
- fix(compaction): Full-session token count for post-compaction sanity check
- fix(telegram): Thread media transport policy into SSRF protection
- fix(session): Preserve lastAccountId and lastThreadId on session reset
- fix(agents): Drop Anthropic thinking blocks on replay
- fix(agents): Avoid injecting memory file twice on case-insensitive mounts
- Docker: Add OPENCLAW_TZ timezone support
- fix(android): HttpURLConnection leak in TalkModeVoiceResolver
- fix(agents): Respect explicit user compat overrides for non-native openai-completions
- fix(agents): Rephrase session reset prompt to avoid Azure content filter
- fix(config): Add missing params field to agents.list[] validation schema
- fix(signal): Add groups config to Signal channel schema
- feat(ios): Onboarding welcome pager
- feat(android): Redesigned chat settings UI

### v2026.3.12 (Previous)
- Dashboard full redesign with modular views
- Browser automation upgrades
- Windows gateway stop improvements

---

## ⚠️ Breaking Changes & Deprecations

### 1. Zalo Personal Plugin Breaking Change
- **Change:** No longer depends on external zca-compatible CLI binaries (openzca, zca-cli)
- **Action Required:** Use `openclaw channels login --channel zalouser` after upgrade

### 2. Default Tools Profile Change (v2026.3.2+)
- **Change:** New installs default to `tools.profile = messaging` only
- **Impact:** New setups no longer start with broad coding/system tools unless explicitly configured
- **Warning:** Some users report config overwrites during upgrade - verify your tools.profile setting

### 3. Cron/Doctor Changes
- Tightened isolated cron delivery - cron jobs can no longer notify through ad hoc agent sends or fallback main-session summaries
- Added `openclaw doctor --fix` migration for legacy cron storage and legacy notify/webhook delivery metadata

---

## 🔧 New Capabilities for Agent Operations

### 1. Docker Timezone Support
- Environment variable: `OPENCLAW_TZ`
- Better timezone control for containerized deployments

### 2. ACP Provenance (v2026.3.8)
- Agents now know who's talking to them
- Improved authentication context for agent-to-agent communication

### 3. OpenClaw Backup Command
- New `openclaw backup` command for safety nets
- Critical for YOLO deploys

### 4. Agent Identity Management
- `openclaw agents set-identity` for workspace identity management
- Avatar support for agents

### 5. Multi-Agent Orchestration
- Community tools emerging for multi-agent dashboards
- OpenClaw Mission Control project for managing multiple agents

---

## 🛡️ Additional Security Updates

### Six New Vulnerabilities Patched (6 days ago)
Per Endor Labs research:
- Server-side request forgery (SSRF)
- Missing authentication bugs
- Path traversal bugs

### ClawHub Malicious Skills Alert
- 71+ malicious skills discovered spreading malware and crypto scams
- 1,000+ fake plugins discovered earlier in March
- **Recommendation:** Vet all skills before installation

---

## 📊 Community Sentiment (Reddit/X)

### Positive
- OpenClaw surpassed 250,000 GitHub stars (beat React's 10-year record in 60 days)
- Dashboard redesign well-received
- Docker timezone support appreciated

### Concerns
- v2026.3.2+ default tools change causing confusion
- Some users report update freezes (possibly npm-related)
- Community discussing forking due to capability restrictions

---

## ✅ Action Items for Our Setup

1. **SECURITY:** Verify running v2026.2.25+ (ClawJacked fix)
2. **CONFIG:** Check `tools.profile` setting if capabilities seem limited
3. **CRON:** Review cron jobs for legacy storage format (use `openclaw doctor --fix` if needed)
4. **BACKUP:** Consider implementing `openclaw backup` in workflow
5. **SKILLS:** Audit installed skills from ClawHub for security

---

## 📚 Sources

- GitHub Releases: https://github.com/openclaw/openclaw/releases
- Oasis Security: https://www.oasis.security/blog/openclaw-vulnerability
- The Hacker News: https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html
- Dark Reading: https://www.darkreading.com/application-security/critical-openclaw-vulnerability-ai-agent-risks
- Infosecurity Magazine: https://www.infosecurity-magazine.com/news/researchers-six-new-openclaw/
- Reddit r/openclaw: Various community discussions
